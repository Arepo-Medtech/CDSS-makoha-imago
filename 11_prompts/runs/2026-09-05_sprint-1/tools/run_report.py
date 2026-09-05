#!/usr/bin/env python3
"""Assemble RUN-REPORT.md for sprint-1 from the check outputs on disk. Run from repo root."""
import json, os, subprocess, re
RUN="11_prompts/runs/2026-09-05_sprint-1"
L=json.load(open(f"{RUN}/ledger_rows.json")); tasks=json.load(open(f"{RUN}/tasks.json"))
rd=lambda p: open(p,encoding='utf-8').read().strip() if os.path.exists(p) else "(missing)"
parse=json.load(open(f"{RUN}/mermaid_parse.json")); npass=sum(1 for r in parse['results'] if r['result']=='PASS')
changed=rd(f"{RUN}/CHECKSUMS_CHANGED.txt"); nchanged=len([l for l in changed.split('\n') if l.strip()])
B=int(subprocess.check_output("git show main:00_MANIFEST.md | wc -c",shell=True).decode().strip())
pre=subprocess.check_output(f"head -c {B} 00_MANIFEST.md | shasum -a 256",shell=True).decode().split()[0]; org=subprocess.check_output("git show main:00_MANIFEST.md | shasum -a 256",shell=True).decode().split()[0]
newfiles=sorted(l[3:] for l in subprocess.check_output(['git','status','--porcelain','-uall']).decode().split('\n') if l.startswith('??') and not l[3:].startswith(('.playwright','11_prompts/runs/')))
allfiles=L['allfiles']; ledger_ok=(L['missing']==[] and L['extra']==[]); onDisk=sum(1 for p in allfiles if os.path.isfile(p))
closure=[
("BSQ-0006","4","04","HARDEN-3.1 task register (one task per artifact)","BUILT","04_hardening/HARDEN-3.1_task_register_delta.md — 276 tasks; 73/73 v1.0 ids once; 0 dup"),
("BSQ-0202","4","05","R30 JSON Schema + row-form seed","BUILT","REG-R30.schema.json (check_schema OK) + REG-R30.3_row-form_seed.jsonl (549/549 valid)"),
("BSQ-0402","4","07","DEPLOY-1.1 run-map delta","BUILT","DEPLOY-1.1_run-map_delta.md — DR-1..7; DEC-22 dependency stated"),
("BSQ-0702","4","10","Counsel packets (PROMPT-P0 Phase 2 item 1) + intended-purpose drafts","BUILT (assembled; dispatch HUMAN-ONLY)","11_prompts/runs/2026-09-05_primer-0/ — counsel_packet_AU/ (5 files), counsel_packet_NZ/ (4), DRAFT_TASK-REG-001, DRAFT_T-G01, P0_BOARD_STATUS"),
("BSQ-0106","4","04","HARDEN-3.1 W8/W3 extension for 10_/11_/03_","BUILT","same file as BSQ-0006 — W3 ext T-150..155, W5 ext T-160.., W8 ext T-400.."),
("BSQ-0703","4","10","HARDEN-1 rows for 10_ ×12","BUILT","HARDEN-1.1 D-2 rows (all 10_ files incl. v1.2/US/EU/companions)"),
("BSQ-0704","4","10","HARDEN-3 tasks for 10_ before W11","BUILT","HARDEN-3.1: REG-POSTURE v1.2/v1.1 + CONTENTS in W3; the rest in W8 ext"),
("BSQ-0403","4","07","OPS-1.1 procedures in CC-5 form","BUILT","OPS-1.1_procedures_cc5_delta.md — PROC-01..12; 33/33 steps carry all four fields"),
("BSQ-0205","4","05","CONTRACT JSON Schemas + RRI test spec","BUILT","CONTRACT-ARG-1.schema.json, CONTRACT-DEV-1.schema.json (+examples 7/7 agree), CONTRACT-RRI-1_render-invariance_test-spec.md"),
("BSQ-0404","4","07","SEC-2 threat model + data-flow","BUILT","SEC-2_threat-model_and_data-flow.md (B-1..7; TM-01..18) + 09_diagrams/data_flow_v1.mermaid (parse PASS)"),
("BSQ-0101","3","04","INDEX-04","BUILT","04_hardening/INDEX.md"),
("BSQ-0104","3","04","HARDEN-1.1 ledger seed delta","BUILT","HARDEN-1.1_coverage_ledger_seed_delta.md — 275 rows; set equality 0 missing / 0 extra"),
("BSQ-0105","3","04","HARDEN-2.1 census + self-audit","BUILT","HARDEN-2.1_spec_census_and_self-audit_delta.md — sources ×8; AR-1..4; STL-1..5; 8 checks"),
("BSQ-0201","3","05","INDEX-05","BUILT","05_registers-and-contracts/INDEX.md (recorded validation in §5)"),
("BSQ-0206","3","05","R29 examples + twin delta","BUILT","REG-R29.examples.jsonl (3/3 verdicts agree) + REG-R29.1_schema_twin_delta.md"),
("BSQ-0701","3","10","INDEX-10","BUILT","10_regulatory-execution/INDEX.md"),
("BSQ-0705","3","10","REG-POSTURE Contents companion","BUILT (over v1.2, not v1.1 — A-003)","REG-POSTURE_v1.2_CONTENTS.md — 69/69 headings"),
("BSQ-0113","3","04","rows 60–71 expanded","BUILT","HARDEN-1.1 D-1"),
("BSQ-0203","3","05","R30.1 ledger row","BUILT","HARDEN-1.1 D-2 (R30.1, R30.2, R30.3 rows)"),
("BSQ-0708","3","10","PROMPT-FOLD-1","BUILT (folds v1.2 per REG-POSTURE §12.5)","11_prompts/PROMPT-FOLD-1_antennae_v1.2_fold.md"),
("BSQ-0204","3","05","R30.1 HARDEN-3 task","BUILT","HARDEN-3.1 T-151 (W3 ext)"),
("BSQ-0390","3","06","INDEX-06","BUILT","06_repositories/INDEX.md — 19 tree rows; 96 file rows; §4 gaps"),
("BSQ-0401","3","07","INDEX-07","BUILT","07_deployment-and-operations/INDEX.md"),
("BSQ-0501","3","08","INDEX-08","BUILT","08_research/INDEX.md (RG mirror RG-01..08)"),
("BSQ-0601","3","09","INDEX-09","BUILT","09_diagrams/INDEX.md (parse + identity recorded; regeneration procedure)"),
("BSQ-0706","3","10","REG-NZ-1.1 delta","CLOSED BY A-003 (no build)","REG-NZ_v1.1.md carries NZ-Q-004 (§10.1), census + self-audit (§12), gate per task (§8), blocks per assumption (§9)"),
("BSQ-0709","3","10","REG-SPRINT-1.2 census delta","BUILT","REG-SPRINT-1.2_census_delta.md — 30 ids; D-6/D-7; census = grep + 2 register-minted gates"),
("BSQ-0707","4","10","MAK-GOV integration-status delta","REMAINS — EXECUTABLE-AFTER-DECISION (DEC-13/DEC-14)","status: 3/10 integrations now exist (MET-2.1; R30.1/R30.3; REG-POSTURE v1.2) — recorded in INDEX-10 §4"),
("BSQ-0391","4","06","cdss-compiler primer + PROMPT-CMP","REMAINS — AFTER DEC-09/DEC-13","recorded in INDEX-06 §2 (launch prompt NONE) and §4"),
("BSQ-0103","3","04","PROMPT-HARDEN launch prompt + runbook","DRAFTED (EXECUTABLE-AFTER-DECISION DEC-10/DEC-11 + row zero)","11_prompts/PROMPT-HARDEN_mt2_pass_launch.md — status DRAFT; preconditions refuse to start"),
("BSQ-0001","3","10","REG-FIND-013 / TASK-REG-023 homing","CLOSED BY A-003 (no build)","REG-POSTURE v1.2 §12.2 check 13"),
("BSQ-0208","3","05","R30 status mapping for 'standing'/cadences","REMAINS — regulatory owner ruling","R30.3 ships every such row as OPEN + source_status_verbatim + mapping_pending: true"),
("BSQ-0407","5","07","DEC-07 / DEC-03 / DEC-08","HUMAN-ONLY — open","DEPLOY-1.1 D-2/D-3 carry the dependencies"),
("BSQ-0713","5","10","DEC-13/14/16/17/19/20 (V1 Governance Layer track)","HUMAN-ONLY — open","—"),
("BSQ-0110","5","04","DEC-10 / DEC-11 (MT2 operator; row-zero rule)","HUMAN-ONLY — open","PROMPT-HARDEN precondition 1"),
("BSQ-0111","5","04","DEC-02 (ratify R29/R30)","HUMAN-ONLY — open","HARDEN-1.1 becomes R29 opening content on this decision"),
("BSQ-0209","5","05","DEC-02 + DEC-09 (05_ homes)","HUMAN-ONLY — open","INDEX-05 DEC-gate column"),
("BSQ-0394","5","06","DEC-09 + REPO-MAP v3","HUMAN-ONLY — open","INDEX-06 §4 records the R6 proposals"),
("BSQ-0712","5","10","DEC-22 (adopt EXEC-1 precedence + run map)","HUMAN-ONLY — open","DEPLOY-1.1 / IMAGO-4 v2 in force on this decision"),
("BSQ-0405","4","07","DEC-23 proposed (infra owner; RTO/RPO; DR drill)","HUMAN-ONLY — proposed in A-004","—"),
("BSQ-0714","4","10","DEC-06 (J-3 retirement ratification)","HUMAN-ONLY — open","—"),
("BSQ-0603","3","09","DEC-01 (regenerate derived artifacts)","HUMAN-ONLY — open","INDEX-09 §4 regeneration procedure ready"),
("BSQ-0002/0003","2","09","MT2 §7.4 notation in IMAGO-3 + page","BUILT (v3 successors)","register_topology_v3.mermaid; cdss_diagrams_v3.html — 0 occurrences; DEF-003"),
("BSQ-0392","2","06","Six CI stubs","BUILT","cdss-evalstack/governance/harness/llm-lattice/lumos/integration ci/pipeline.yml — 18/18 stubs carry the r29 hook"),
("BSQ-0502","2","08","RESEARCH-1.1 findings delta","BUILT","RESEARCH-1.1_findings_delta.md — RG-07, RG-08; status field"),
("BSQ-0606","2","09","IMAGO-4 v2 with RUN overlay","BUILT","deployment_ladders_v2.mermaid (after DEPLOY-1.1)"),
("BSQ-0004/0393/0715","2","09/06/10","Manifest contradictions (escalated)","RESOLVED BY A-004 (DEF-003/004/005 appended by the owner's sprint)","00_MANIFEST.md §10"),
("BSQ-0602 / 0711 / 0604 / 0710 / 0503","2","09/10","R25 label; W-namespace; sources' skeleton home; html twins; DEC-12","REMAIN — owners' rulings","carried in INDEX-09 §4 / INDEX-10 §4"),
]
built=sum(1 for c in closure if c[4].startswith('BUILT')); closedA=sum(1 for c in closure if c[4].startswith('CLOSED BY A-003')); drafted=sum(1 for c in closure if c[4].startswith('DRAFTED')); human=sum(1 for c in closure if c[4].startswith('HUMAN-ONLY')); remains=sum(1 for c in closure if c[4].startswith('REMAIN'))
tbl="| Row | W | Folder | Deliverable | Outcome | Evidence |\n|---|---|---|---|---|---|\n"+"\n".join(f"| {a} | {b} | {c} | {d} | **{e}** | {f} |" for a,b,c,d,e,f in closure)
rep=f"""# RUN-REPORT — sprint-1 (2026-09-05): closing the survey-2 Build-Spec Queue

Run: `{RUN}/` · Branch: `sprint-1-build-spec-queue` (from `main` 6aae5d6) · Executor: Claude Code (desktop session) · Mandate: the owner's request of 5 Sep 2026 to run a sprint that closes the Build-Spec Queue · Status: **built and verified; not merged** — `main` accepts changes only by pull request (README).

## 0. Append-only proof (law 1) — read this first

```
CHECKSUMS_BEFORE.txt: {len(rd(f"{RUN}/CHECKSUMS_BEFORE.txt").split(chr(10)))} files (main, before any write)
CHECKSUMS_AFTER.txt:  {len(rd(f"{RUN}/CHECKSUMS_AFTER.txt").split(chr(10)))} files
pre-existing files whose hash changed: {nchanged}
{changed}
00_MANIFEST.md prefix check: sha256(first {B} bytes of the new file) = {pre}
                             sha256(main:00_MANIFEST.md)              = {org}
                             → {'IDENTICAL — appended only (A-004)' if pre==org else 'MISMATCH'}
```

Every other byte outside the run directories is as it was. The one changed file is the manifest, appended per README "How to change it" step 3 and the A-001..A-003 pattern.

## 1. Coverage

| Measure | Value |
|---|---|
| New files outside run directories | {len(newfiles)} |
| Run directories added | 2 (`2026-09-05_sprint-1`, `2026-09-05_primer-0` partial) |
| Files in HARDEN-1.1 scope (tree excl. .DS_Store, .git, runs) | {len(allfiles)} — all on disk at seal: {onDisk}/{len(allfiles)} |
| HARDEN-1.1 rows | {len(L['rows'])} (v1.0 ids 0–73 resolved + {len(L['rows'])-77} new); acceptance set-equality: {L['missing'].__len__()} missing / {L['extra'].__len__()} extra → {'PASS' if ledger_ok else 'FAIL'} |
| HARDEN-3.1 tasks | {len(tasks)}; every v1.0 T id present once (73/73); every scoped file has exactly one task |
| R30.3 rows | 549 (AU 150 · NZ 93 · US 129 · EU 123 · NDG 14 · sprint 30 · EX 10); 549/549 valid; 44 families, 0 gaps |
| Schemas | 4 check_schema OK; 10/10 example verdicts agree |
| Diagrams | mermaid {parse['tool']}: {npass}/{len(parse['results'])} PASS; source↔inline identity 9/9 |
| CC-5 field presence (OPS-1.1) | 33/33 steps |
| Reference check (00_, 04_–10_) | {rd(f"{RUN}/refcheck_output.txt").split(chr(10))[0]} — unresolved paths are all external-pack / glob / future-output / (at check time) not-yet-written INDEX files; unresolved anchors are the two carried v2 `MT2 §7.4` defects (DEF-003) — see refcheck_output.txt |

## 2. Queue closure — every survey-2 row with weight ≥ 3, plus the weight-2 rows acted on

{tbl}

Summary: **{built} BUILT · {closedA} CLOSED BY A-003 · {drafted} DRAFTED (after-decision) · {remains} REMAIN (decision-gated) · {human} HUMAN-ONLY rows unchanged (they are decisions).** No CLAUDE-CODE-EXECUTABLE-NOW row remains open.

## 3. Verification outputs (verbatim files in this directory)

- `schema_examples_validation.txt` — check_schema + example verdicts (ARG-1, DEV-1, R29, R30)
- `r30_seed_validation.txt`, `r30_seed_census.txt` — 549 rows
- `mermaid_parse.json` — 7 sources + 9 inlined blocks; `identity_v3.txt` — 9/9 identical
- `proc_fields.txt` — 33/33
- `refcheck.json`, `refcheck_output.txt`
- `ledger_pass3.txt`, `harden_pass3.txt` — generator outputs after convergence (pass 2 == pass 3 hashes: `pass2.md5` = `pass3.md5`)
- `CHECKSUMS_BEFORE.txt`, `CHECKSUMS_AFTER.txt`, `CHECKSUMS_CHANGED.txt`
- `10_regulatory-execution/validate_reg.py` re-run: NZ/US/EU PASS; AU reports the known legacy-shape condition (REG-POSTURE v1.2 §12.2 check 2; A-003) — unchanged, no new issue (pasted in INDEX-10 §5)

## 4. What this sprint did NOT do (honesty lines)

It did **not** run the MT2 pass, write any R29 row, close any ASSUME/DEC/gate, send any counsel packet, edit any retained file, install the agent-skills pack, run PROMPT-P0 Phase 1 or items 3–8, fold MAK-ANT (PROMPT-FOLD-1 is the instrument; the corpus owner commissions it), rule the R25 label or the R30 status mapping, or touch Ketryx (parked). PROMPT-HARDEN is a draft that refuses to start while DEC-10/DEC-11 are Open. Person-level owners remain [NEEDS DEFINITION] throughout.

## 5. Hand-back — decisions now owed by humans (unchanged from the survey, restated)

1. **DEC-22** — adopt EXEC-1 precedence and the run map (Founder): makes DEPLOY-1.1 and IMAGO-4 v2 the working calendar.
2. **DEC-10 / DEC-11 / DEC-02 / DEC-09** — name the MT2 operator, accept the row-zero rule, ratify R29/R30, name repo owners: unlocks PROMPT-HARDEN, opens R29 with HARDEN-1 + HARDEN-1.1, lets the 05_ schemas MOVE to cdss-spine.
3. **Owners** — regulatory owner (G-09: rules BSQ-0208, commissions FOLD-1, dispatches the packets with the founder), infra/security/operations owners (proposed DEC-23), manifest owner, programme lead.
4. **Merge the PR** — on merge the Confluence mirror creates one page per new file and folder.

## 6. Assumptions and open questions
See `OPEN_QUESTIONS.md` (19 items) and `HALT_LOG.md` (12 temptations logged; none acted on).

## 7. Confidence
HIGH that every EXECUTABLE-NOW row is closed by a file that satisfies its spec's mandatory sections and acceptance test (each file carries its own census/self-audit with pasted outputs). MEDIUM on three content judgments the survey itself flagged for operator amendment: the contract schemas' field-level enums (`severity_tier` left as a pattern), OPS-1.1's regulated-control stubs (SLAs [NEEDS DEFINITION]), and SEC-2's boundary/threat scope. The R30 row-form seed's statuses are mechanical crosswalks and are correct by construction; their *meaning* for 'standing' obligations is the regulatory owner's call.
"""
open(f"{RUN}/RUN-REPORT.md","w",encoding='utf-8').write(rep)
print("RUN-REPORT written", len(rep.encode()),"B; built",built,"closedA",closedA,"drafted",drafted,"remain",remains,"human",human,"newfiles",len(newfiles))
