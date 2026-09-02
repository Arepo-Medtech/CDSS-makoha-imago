#!/usr/bin/env python3
"""Generate the queue/dismissal tables (sections c, d, e) of BUILD_SPEC_QUEUE.md from BSQ.jsonl."""
import json,collections,re
rows=[json.loads(l) for l in open("BSQ.jsonl") if l.strip()]
byid={r["row_id"]:r for r in rows}
GATE_ORDER=["GATE-000","SG-V1-0","NZ-GATE-0","W0","GATE-001","W1","W3","GATE-002","W8","W10","W11","GATE-003","GATE-004","code freeze"]
def gate_rank(r):
    b=" ".join(r["blocks"])
    for i,g in enumerate(GATE_ORDER):
        if g in b: return i
    return len(GATE_ORDER)
EXEC_ORDER=["CLAUDE-CODE-EXECUTABLE-NOW","EXECUTABLE-AFTER-DECISION","HUMAN-ONLY","CORPUS-OWNER","EXTERNAL-PARTY"]
q=[r for r in rows if r["weight"]>=3 and r["state"]!="DISMISSED-NOT-BLOCKING"]
# dependency order: rows whose depends_on is empty first (stable)
def dep_rank(r):
    d=r.get("build_spec",{}).get("depends_on",[]) if r.get("build_spec") else []
    return len(d)
q.sort(key=lambda r:(EXEC_ORDER.index(r["executability"]) if r["executability"] in EXEC_ORDER else 9, -r["weight"], gate_rank(r), dep_rank(r), r["row_id"]))
out=[]
out.append("## c. The Build-Spec Queue (weight ≥ 3; grouped by executability; within group: weight desc → earliest blocked gate → dependencies first)\n")
out.append(f"{len(q)} rows. Every CLAUDE-CODE-EXECUTABLE-NOW row carries an eleven-field `build_spec` in `BSQ.jsonl` (validated); the table shows the spec's target path and its closes/depends links; the full spec text is in the row.\n")
for ex in EXEC_ORDER:
    grp=[r for r in q if r["executability"]==ex]
    if not grp: continue
    out.append(f"\n### {ex} ({len(grp)})\n")
    out.append("| # | Row | W (c+r) | Folder | Class | Statement (short) | Blocks | Target / decision | Closes | Depends on | Owner |")
    out.append("|---|---|---|---|---|---|---|---|---|---|---|")
    for i,r in enumerate(grp,1):
        bs=r.get("build_spec")
        target=(bs["target_path"] if bs else r.get("decision_ref","—")).replace("|","/")
        closes=", ".join(bs["closes_rows"]) if bs else "—"
        deps=", ".join(bs["depends_on"]) if bs and bs["depends_on"] else "—"
        st=r["statement"].replace("|","/"); st=st[:170]+("…" if len(st)>170 else "")
        out.append(f"| {i} | {r['row_id']} | {r['weight']} ({r['criticality']}+{r['radius']}) | {r['folder']} | {r['finding_class']} | {st} | {'; '.join(r['blocks'])[:120].replace('|','/')} | {target[:160]} | {closes} | {deps} | {r['owner'][:60].replace('|','/')} |")
# full build specs for executable-now rows
out.append("\n### c.1 Build specs — CLAUDE-CODE-EXECUTABLE-NOW rows, full text (eleven headed fields, in order)\n")
for r in [r for r in q if r["executability"]=="CLAUDE-CODE-EXECUTABLE-NOW"]:
    bs=r["build_spec"]
    out.append(f"\n#### {r['row_id']} — {r['artifact_path'][:120]}\n")
    out.append(f"**Target path** · {bs['target_path']}\n\n**Class + P-lines satisfied** · {bs['class_and_plines']}\n\n**Mandatory sections/fields** ·\n" + "\n".join(f"- {s}" for s in bs["mandatory_sections"]) + f"\n\n**Inputs (paths)** ·\n" + "\n".join(f"- `{s}`" for s in bs["inputs"]) + f"\n\n**Laws** · " + " · ".join(bs["laws"]) + f"\n\n**Evidence to capture** · {bs['evidence_to_capture']}\n\n**Acceptance test** · {bs['acceptance_test']}\n\n**Closes rows** · {', '.join(bs['closes_rows'])}\n\n**HARDEN linkage** · {bs['harden_linkage']}\n\n**Ratifying owner** · {bs['ratifying_owner']}\n\n**Depends on** · {', '.join(bs['depends_on']) if bs['depends_on'] else '— (none)'}\n")
# d. roll-up handled in main file; e. dismissals
dis=[r for r in rows if r["state"]=="DISMISSED-NOT-BLOCKING"]
low=[r for r in rows if r["weight"] in (1,2) and r["state"]=="OPEN" and r["finding_class"]!="PRESENT-CONFORMANT"]
esc=[r for r in rows if r["state"]=="ESCALATED"]
out.append("\n## e. What is NOT required (dismissed, below-threshold, and escalated-not-buildable)\n")
out.append(f"\n### e.1 Dismissed as not blocking ({len(dis)})\n\n| Row | Folder | Class | Statement (short) | Dismissal reason |\n|---|---|---|---|---|")
for r in dis: out.append(f"| {r['row_id']} | {r['folder']} | {r['finding_class']} | {r['statement'][:140].replace('|','/')} | {r['dismissal_reason'].replace('|','/')} |")
out.append(f"\n### e.2 Open but below the queue threshold (weight 1–2; {len(low)}) — recommended where marked, never required for code freeze\n\n| Row | W | Folder | Class | Statement (short) | Executability |\n|---|---|---|---|---|---|")
sk=[r for r in low if r["row_id"]>="BSQ-0300" and r["row_id"]<"BSQ-0390"]
for r in [r for r in low if not (r["row_id"]>="BSQ-0300" and r["row_id"]<"BSQ-0390")]: out.append(f"| {r['row_id']} | {r['weight']} | {r['folder']} | {r['finding_class']} | {r['statement'][:140].replace('|','/')} | {r['executability']} |")
out.append(f"| BSQ-03xx ×{len(sk)} | 1 | 06 | QUALITY-BELOW-BAR | {len(sk)} skeleton files with no Proposed/skeleton/stub marker (listed in folders/06_repositories/ASSESSMENT.md §4 and skeleton_rows.jsonl) | CLAUDE-CODE-EXECUTABLE-NOW (via INDEX-06 §4) |")
out.append(f"\n### e.3 Escalated — cannot be built by a session, must be ruled ({len(esc)})\n\n| Row | W | Folder | Class | Blocker | Decision ref |\n|---|---|---|---|---|---|")
for r in esc: out.append(f"| {r['row_id']} | {r['weight']} | {r['folder']} | {r['finding_class']} | {r['blocker'].replace('|','/')} | {r.get('decision_ref','—').replace('|','/')} |")
out.append("\n**Length-only findings dismissed by name:** none were filed. The 20–60× byte gap between 01_–03_ and 04_–10_ appears in no row as a defect; every row cites a P-line or a class-contract line (the_one_rule).\n")
open("queue_sections.md","w").write("\n".join(out)+"\n")
print("queue rows",len(q),"dismissed",len(dis),"low",len(low),"escalated",len(esc))
