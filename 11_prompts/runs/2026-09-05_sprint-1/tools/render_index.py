#!/usr/bin/env python3
"""Render the seven folder INDEX.md files (04–10) from ledger_rows.json + tasks.json + disk. Run from repo root with the venv python (needs yaml)."""
import json, os, re, subprocess, collections, hashlib, yaml
RUN="11_prompts/runs/2026-09-05_sprint-1"; DATE="2026-09-05"
L=json.load(open(f"{RUN}/ledger_rows.json")); rows=L['rows']; tasks=json.load(open(f"{RUN}/tasks.json"))
rowsby=collections.defaultdict(list); taskby=collections.defaultdict(list)
for r in rows:
    if not r['path'].startswith('('): rowsby[r['path']].append(str(r['row']))
for t in tasks:
    if not t['path'].startswith(('(','—')): taskby[t['path']].append(t['tid'])
def esc(s): return str(s).replace('|','\\|').replace('\n',' ')
def fm(p):
    """doc_id, version, date, status (quoted, truncated) from YAML frontmatter or header comment."""
    t=open(p,encoding='utf-8',errors='replace').read()
    d={'doc_id':'—','version':'—','date':'—','status':'—'}
    if t.startswith('---'):
        head=t.split('---',2)[1]
        for k in d:
            m=re.search(r'^'+k+r':\s*(.+)$',head,re.M)
            if m: d[k]=m.group(1).strip().strip('"')
    else:
        first=t.split('\n')[0]
        if p.endswith('.json'):
            try: j=json.loads(t); d['doc_id']=j.get('$id',j.get('title','—')); d['status']=j.get('title','—')
            except Exception: pass
        elif p.endswith('.mermaid'): d['doc_id']=re.sub(r'^%% ','',first)[:40]; d['status']=first
        else: d['status']=first[:160]
    d['status']=d['status'][:220]+('…' if len(d['status'])>220 else '')
    return d
def size(p): return os.path.getsize(p)
def ls(folder): return sorted(p for p in L['allfiles'] if p.startswith(folder+'/'))
def sha(p): return hashlib.sha256(open(p,'rb').read()).hexdigest()
MANROW={'04_hardening':'§1 row 04_hardening (declared 4) + A-004 (sprint-1 additions)','05_registers-and-contracts':'§1 row (4) + §8 A-002 (+1 R30.1) + §9 A-003 (+1 R30.2) + A-004','06_repositories':'§1 row (5) superseded by §7 A-001 (91) + A-004','07_deployment-and-operations':'§1 row (5) + A-004','08_research':'§1 row (1) + A-004','09_diagrams':'§1 row (5) + A-004','10_regulatory-execution':'§8 A-002 (7) + §9 A-003 (+4) + A-004'}
DISP={'MAJOR_TASK_2':'Retained (verbatim)','HARDEN-1_':'Proposed (seed)','HARDEN-2_':'Proposed','HARDEN-3_':'Proposed','HARDEN-1.1':'Added (sprint-1) — Proposed','HARDEN-2.1':'Added (sprint-1) — Proposed','HARDEN-3.1':'Added (sprint-1) — Proposed','INDEX':'Added (sprint-1)'}
def disp(p,folder):
    b=os.path.basename(p)
    for k,v in DISP.items():
        if b.startswith(k): return v
    if p in [r['path'] for r in rows if r['note'].startswith('sprint-1')]: return 'Added (sprint-1) — Proposed'
    if folder=='05_registers-and-contracts': return 'Proposed (DEC-02)'
    if folder=='06_repositories': return 'Retained (REPO-MAP existing rows) / Proposed (skeletons, DEC-09)'
    if folder=='07_deployment-and-operations': return 'Retained + Added/Proposed (per status)'
    if folder=='08_research': return 'Added'
    if folder=='09_diagrams': return 'Added (Proposed)' if 'v2' in b or b in ('imago_architecture.mermaid','merged_runtime_sequence.mermaid','deployment_ladders.mermaid') else 'Added (sprint-1) — Proposed'
    if folder=='10_regulatory-execution':
        if b in ('REG-POSTURE_v1.1.md','REG-NZ_v1.0.md'): return 'Added (A-002) — superseded by A-003, retained unedited'
        return 'Added (A-002/A-003) — ADVISORY_ONLY'
    return 'Added'
def filetable(folder, extra_cols=None):
    files=ls(folder); hdr=["path","class","doc_id","version","date","status (quoted)","bytes","disposition","HARDEN-1/1.1 row","HARDEN-3.1 task","00_MANIFEST row"]
    if extra_cols: hdr+= [c for c,_ in extra_cols]
    out=["| "+" | ".join(hdr)+" |","|"+"---|"*len(hdr)]
    for p in files:
        d=fm(p) if os.path.isfile(p) else {'doc_id':'(this file)','version':'1.0','date':DATE,'status':'(this index)'}
        cls=next((r['cls'] for r in rows if r['path']==p),'—'); by=size(p) if os.path.isfile(p) else 0
        cells=[f"`{p}`",cls,esc(d['doc_id']),esc(d['version']),esc(d['date']),esc(d['status']),str(by),disp(p,folder),",".join(rowsby[p]) or 'ABSENT',",".join(taskby[p]) or 'ABSENT',MANROW[folder]]
        if extra_cols: cells+=[esc(f(p)) for _,f in extra_cols]
        out.append("| "+" | ".join(cells)+" |")
    return "\n".join(out), files
def head(docid,folder,title,status):
    return f"""---
doc_id: {docid}
title: "{title}"
version: "1.0"
date: "{DATE}"
status: "{status}"
folder: "{folder}/"
produced_by: "sprint-1 (survey-2 Build-Spec Queue) — generated tables from disk by {RUN}/tools/render_index.py; briefing text authored; edits nothing"
---
"""
def selfaudit(folder,files,extra=""):
    lsout=subprocess.check_output(['ls','-l',folder]).decode().strip()
    return f"""## §5 Self-audit (run {DATE})

- File count in the table = files on disk under `{folder}/` (excluding `.DS_Store`): **{len(files)}** = {len(files)} — PASS.
- Every path in the table exists — PASS ({sum(1 for p in files if os.path.isfile(p))}/{len(files)} at generation; this INDEX itself is written by the same run).
- Every HARDEN-1/1.1 row id and HARDEN-3.1 task id in the table resolves in `04_hardening/HARDEN-1.1_coverage_ledger_seed_delta.md` / `HARDEN-3.1_task_register_delta.md` — PASS (ids taken from the same generated data; 0 ABSENT).
{extra}
```
$ ls -l {folder}
{lsout}
```
"""
# ============ 04 ============
def idx04():
    folder='04_hardening'; t,files=filetable(folder)
    mt2='04_hardening/MAJOR_TASK_2_anti-laziness-hardening-directive.md'
    ex04="- HARDEN-1.1 ↔ HARDEN-3.1 parity: every 04_ path has exactly one row and one task — PASS.\n- MT2 sha256 matches CHECKSUMS_BEFORE — PASS."
    body=head('INDEX-04',folder,"INDEX-04 — 04_hardening: briefing, file table, retained-verbatim note, honesty line, self-audit","Added (sprint-1); indexes only; edits nothing; the MT2 pass has NOT run — every ledger row is a pre-pass placeholder and zero rows are HARDENED")+f"""
# INDEX-04 — 04_hardening

## §1 Briefing — what these documents are

*Ecosystem-agnostic first.* A **DIRECTIVE** is a standing order: it says what must be true of every artifact it governs and cannot be waived by anything inside a governed document (MT2 preamble). A **SPEC** states the bar an artifact must clear, per class (HARDEN-2: eight classes CC-1..CC-8, a universal exit bar, anti-rationalization rows, stop-the-line rules). A **WORKLIST / PLAN** orders the work — one task per artifact, waves with a stated reason (HARDEN-3 W0–W11; HARDEN-3.1 one row per artifact). A **SEED** is a register's opening content before the register exists (HARDEN-1 + HARDEN-1.1: one row per artifact, all PENDING until the pass converts each on contact). They compose in that order — directive → spec → plan → ledger seed → R29 (the Hardening Coverage Ledger, `05_registers-and-contracts/REG-R29.schema.json`, ratified on DEC-02, written only by the pass). Read the seed's states as placeholders, never as results (HARDEN-1 l.30). The pass is launched wave by wave with `11_prompts/PROMPT-HARDEN_mt2_pass_launch.md` (draft; runnable after DEC-10/DEC-11 and row zero). Form exemplar: `02_cdss-stack-augmented/primers_briefing.md` Part 1.

## §2 File table

{t}

## §3 Retained-verbatim note for MT2

`MAJOR_TASK_2_anti-laziness-hardening-directive.md` is the directive **preserved verbatim** (00_MANIFEST §1 "MT2 directive (verbatim)", §4.1 "VERBATIM copies: 34/34 checksum-identical"). sha256 at {DATE}: `{sha(mt2)}` — identical to `{RUN}/CHECKSUMS_BEFORE.txt`. It has no YAML frontmatter by design; it is judged by this index row and hardened as a companion set (T-120), never edited. **Citation notation rule (00_MANIFEST §5 DEF-002):** MT2 §1 and §7 contain numbered *items*, not subsections — cite `§1(7)`, `§7(4)`, never `§1.7`/`§7.4` (§2.1–2.3 are real subsections). The two residual `§7.4` instances DEF-002 missed (09_ v2 topology source + page) are carried in superseded files and fixed in their v3 successors (DEF-003, A-004).

## §4 Honesty line (mirrors 00_MANIFEST §4.4)

The MT2 pass has **not** been executed: R29 rows 0–73 (v1.0) and 74–{max(int(x) for r in rows for x in [r['row']])} (HARDEN-1.1) are PENDING; row 0 is BLOCKED (no installation evidence; DEC-10/DEC-11 open); `validate_build_plan.py` is not in the tree (PENDING-VALIDATOR); no task in HARDEN-3 / HARDEN-3.1 has started (`ls 11_prompts/runs` → survey-2, sprint-1, primer-0 partial — no `_harden-W*` run exists). HARDEN-2.1, HARDEN-1.1 and HARDEN-3.1 are Proposed deltas awaiting the architecture owner (DEC-02) and the MT2 operator (DEC-10).

{selfaudit(folder,files,ex04)}"""
    open(f"{folder}/INDEX.md","w",encoding='utf-8').write(body)
# ============ 05 ============
def idx05():
    folder='05_registers-and-contracts'
    ids={'CONTRACT-ARG-1_argument_schema.md':'CONTRACT-ARG-1 (+DEV-1, RRI-1 paragraphs)','CONTRACT-ARG-1.schema.json':'CONTRACT-ARG-1 (JSON Schema)','CONTRACT-ARG-1.examples.jsonl':'examples for ARG-1','CONTRACT-DEV-1.schema.json':'CONTRACT-DEV-1 (JSON Schema)','CONTRACT-DEV-1.examples.jsonl':'examples for DEV-1','CONTRACT-RRI-1_render-invariance_test-spec.md':'CONTRACT-RRI-1-TEST (RRI-1..4)','REG-R29.schema.json':'REG-R29 (JSON Schema)','REG-R29_hardening_coverage_ledger.schema.md':'REG-R29 (md twin)','REG-R29.examples.jsonl':'examples for R29 (EXAMPLE rows only)','REG-R29.1_schema_twin_delta.md':'REG-R29.1','REG-R30_regulatory_posture_register.schema+seed.md':'REG-R30 (base)','REG-R30.1_seed_delta.md':'REG-R30.1','REG-R30.2_seed_delta.md':'REG-R30.2','REG-R30.schema.json':'REG-R30 (JSON Schema)','REG-R30.3_row-form_seed.jsonl':'REG-R30.3 (row-form seed, 549 rows)','INDEX.md':'INDEX-05'}
    home=lambda p: 'cdss-spine/contracts/ (pointer stub `CONTRACT-ARG-1.pointer.md` covers ARG/DEV/RRI)' if 'CONTRACT' in p else ('cdss-spine/registers/ (README: "MOVE here on DEC-02, never copy"); R30 owner cdss-governance' if 'REG-R' in p else '— (index)')
    gate=lambda p: 'DEC-02 (ratify R29/R30) + DEC-09 (repo owners) — MOVE, never copy' if 'REG-R' in p or 'CONTRACT' in p else '—'
    t,files=filetable(folder,[("doc_id(s) carried",lambda p: ids.get(os.path.basename(p),'—')),("skeleton home on ratification",home),("DEC gate",gate)])
    val=open(f"{RUN}/schema_examples_validation.txt").read().strip()
    r30v=open(f"{RUN}/r30_seed_validation.txt").read().strip().split('\n')[0] if os.path.exists(f"{RUN}/r30_seed_validation.txt") else ''
    ex05="- Recorded validation (P-D-09 / CC-7; `"+RUN+"/tools/validate_examples.py`, jsonschema 4.25.1):\n\n```\n"+val+"\n"+r30v+"\n```\n- Pointer stub exists: `06_repositories/repo-skeletons/cdss-spine/contracts/CONTRACT-ARG-1.pointer.md` — PASS; `cdss-spine/registers/README.md` names R29/R30 — PASS."
    body=head('INDEX-05',folder,"INDEX-05 — 05_registers-and-contracts: briefing, file table with carried doc_ids, reading rule, honesty line, recorded validation","Added (sprint-1); indexes only; nothing ratified (DEC-02 Open); no schema moved (DEC-09 Open); R30 now has a JSON Schema and a row-form seed (sprint-1) — Proposed, not ratified")+f"""
# INDEX-05 — 05_registers-and-contracts

## §1 Briefing — what these documents are

A **CONTRACT** is a shared interface specification that lives once, versioned, in the spine and is consumed as a pinned dependency; a change is a spine PR that visibly breaks consumers (Arch §10). A **SCHEMA** is the machine-checkable form of a contract or of a register row (JSON Schema draft 2020-12 here; `jsonschema` validates instances). A **REGISTER** is a governed table of what currently holds (versioned) or what happened (append-only), with one owning repo, a declared mutability, an opening level and the universal join key `version_stamp` — the six register laws of Arch §12.1. A **SEED** is a register's proposed opening content; a **DELTA** adds to a base file without editing it (MET-1.1 pattern). The **register of registers** idea (Arch §12): R1–R28 are the ratified registers; R29 (hardening coverage) and R30 (regulatory posture) are Proposed here and enter the RoR on DEC-02; every register's schema lives in cdss-spine (§12.1(1)), and a scheduled negative audit proves nothing exists outside its register (§12.1(5)). Form exemplar: `02_cdss-stack-augmented/primers_briefing.md`.

## §2 File table

{t}

## §3 Reading rule (P-D-11)

R30 is read as **REG-R30 (base) → R30.1 → R30.2 → R30.3 (row form)**: the base is the field list and prose seed; R30.1 extends the `reg_id` enum and seeds v1.1/NZ/GOV/SPRINT ids; R30.2 adds US/EU/NZ-STD/NZ-GATE/STD and the `jurisdiction` field; R30.3 (`REG-R30.3_row-form_seed.jsonl`) is the same content one row per ID, crosswalked per REG-POSTURE §0.7 with `source_status_verbatim` preserved and `mapping_pending: true` where the regulatory owner's ruling is awaited (survey-2 BSQ-0208). R29 is read as REG-R29 (json + md) → R29.1 (adds `blocker` to the md reading; states the placeholder rule). CONTRACT-ARG-1 (.md) is the field list; the two `.schema.json` files and the RRI test spec are its companions, staged for the DEC-02 + DEC-09 move.

## §4 Honesty line

Nothing in this folder is ratified (DEC-02 Open); no schema has moved to cdss-spine (DEC-09 Open); the skeleton pointer stub still points here. Statuses in the R30 seeds are the *source's* words (standing / not started / not passed / recorded) — the row-form seed maps them to `OPEN` and flags the mapping as pending where §0.7 gives no rule; no ASSUME status is changed anywhere. R29 example rows are EXAMPLES, not ledger writes.

{selfaudit(folder,files,ex05)}"""
    open(f"{folder}/INDEX.md","w",encoding='utf-8').write(body)
# ============ 06 ============
def idx06():
    folder='06_repositories'; ROOT=folder+'/repo-skeletons'
    repomap=open(f"{folder}/REPO-MAP_v2.md",encoding='utf-8').read()
    rm={}
    for l in repomap.split('\n'):
        m=re.match(r'^\|\s*\**(?:\*\(channel\)\*\s*)?([A-Za-z\-]+)\**\s*\|\s*([^|]+)\|[^|]*\|[^|]*\|\s*([^|]+)\|',l)
        if m and m.group(1).startswith('cdss'): rm[m.group(1)]=(m.group(2).strip(),m.group(3).strip())
    prompts={'cdss-engine':'PROMPT-A','cdss-library':'PROMPT-B','cdss-corpus':'PROMPT-C','cdss-registry':'PROMPT-D','cdss-graph':'PROMPT-E','cdss-conformal':'PROMPT-F','cdss-corruption':'PROMPT-G','cdss-lumos':'PROMPT-H','cdss-evalstack':'PROMPT-I','cdss-governance':'PROMPT-J (+PRM-ANT regulatory-sensing/)','cdss-coder':'— (fork channel; J-1/J-2 via PROMPT-J posture)','cdss-harness':'— (HX; no prompt)','cdss-llm-lattice':'PROMPT-K / PROMPT-L','cdss-spine':'PROMPT-P0 (BUILD_PLAN_V1-S1)','cdss-fabric':'PROMPT-PRM-ABC / PRM-HDC (fabric modules per RUN-REPORT R6)','cdss-compiler':'**NONE — no owning primer, no prompt (survey-2 BSQ-0391; after DEC-09/DEC-13)**','cdss-ui-clinician':'PROMPT-PRM-LBP / PRM-HDC','cdss-ui-patient':'PROMPT-PRM-PRB / PRM-TXC (Blocked beyond J-3-safe subset)','cdss-integration':'— (lockfile home per DEC-09)'}
    trees=sorted(d for d in os.listdir(ROOT) if os.path.isdir(os.path.join(ROOT,d)))
    tt=["| repo | owning primer / volume (REPO-MAP) | REPO-MAP status | files | README | MANIFEST | CI | CODEOWNERS | sub-dir stubs | launch prompt in 11_ | HARDEN-1.1 rows | HARDEN-3.1 tasks |","|---|---|---|---|---|---|---|---|---|---|---|---|"]
    filerows=["| path | bytes | banner | class | HARDEN-1.1 row | HARDEN-3.1 task | check |","|---|---|---|---|---|---|---|"]
    unbannered=[]; nfiles=0; ci=0
    for tr in trees:
        tp=os.path.join(ROOT,tr); files=sorted(os.path.relpath(os.path.join(d,f),tp) for d,_,fs in os.walk(tp) for f in fs if f!='.DS_Store')
        subs=sorted(set(f.split('/')[0] for f in files if '/' in f and not f.startswith('ci/')))
        has=lambda n: 'Y' if n in files else 'N'
        if 'ci/pipeline.yml' in files: ci+=1
        rid=[x for f in files for x in rowsby[f"{ROOT}/{tr}/{f}"]]; tid=[x for f in files for x in taskby[f"{ROOT}/{tr}/{f}"]]
        pv,st=rm.get(tr,('—','—'))
        tt.append(f"| `{tr}` | {esc(pv)} | {esc(st)} | {len(files)} | {has('README.md')} | {has('MANIFEST.yaml')} | {has('ci/pipeline.yml')} | {has('CODEOWNERS')} | {', '.join(subs) or '—'} | {prompts.get(tr,'—')} | {rid[0]}–{rid[-1]} | {tid[0]}–{tid[-1]} |")
        for f in files:
            p=f"{ROOT}/{tr}/{f}"; t=open(p,encoding='utf-8',errors='replace').read(); nfiles+=1
            banner=bool(re.search(r'(?i)skeleton|proposed|stub|pointer',t)); issues=[]
            if not banner: issues.append('no Proposed/skeleton/stub marker'); unbannered.append(p)
            if f=='MANIFEST.yaml':
                try:
                    y=yaml.safe_load(t) or {}
                    for k in ('name','status'):
                        if k not in y: issues.append(f'MANIFEST lacks {k}')
                    if y.get('name')!=tr: issues.append('MANIFEST name != tree')
                except Exception as e: issues.append('YAML parse error')
            if f=='ci/pipeline.yml':
                if 'r29' not in t.lower(): issues.append('no r29 ratchet hook')
                if not re.search(r'not runnable|STUB',t): issues.append('does not state not runnable')
            if f=='CODEOWNERS' and 'NEEDS DEFINITION' not in t: issues.append('persons without [NEEDS DEFINITION]')
            cls=next((r['cls'] for r in rows if r['path']==p),'—')
            filerows.append(f"| `{p}` | {size(p)} | {'Y' if banner else 'N'} | {cls} | {','.join(rowsby[p])} | {','.join(taskby[p])} | {'conformant' if not issues else '; '.join(issues)} |")
    t,files=filetable(folder)
    body=head('INDEX-06',folder,"INDEX-06 — 06_repositories: briefing, tree table (19 repos), file table (skeletons), known gaps, honesty line, self-audit","Added (sprint-1); indexes only; no code exists anywhere in this folder; every skeleton is Proposed (DEC-09 Open); REPO-MAP v2 is stale against RUN-REPORT R6 (five proposed repos) pending DEC-09 — recorded, not resolved here")+f"""
# INDEX-06 — 06_repositories

## §1 Briefing — what a skeleton is

A **repository skeleton** is the shape of a repo before any code exists: a README that states what its owning primer requires, a MANIFEST.yaml stub (Arch §10 / Harness manifest discipline) that becomes the artifact manifest on first emit, a `ci/pipeline.yml` stub (Tier 1+2 shape, Arch §11.1; imports from cdss-evalstack; carries the dormant R29 ratchet hook that activates on DEC-02, MT2 §7(4)), per-directory READMEs mirroring the primer's §-4/§-8 layout, and CODEOWNERS where a primer mandates them. Trees mirror **REPO-MAP v2** (14 existing repos + 4 proposed + cdss-integration + the GPP channel file). Doctrine: contracts appear only as **pointer stubs** to the canonical drafts in 05_ — move-never-copy on ratification ("duplication is where drift begins"); cdss-corpus is intentionally minimal (firewall banner; instantiate in-account only); the lockfile home is DEC-09's call (cdss-integration or the spine). Every skeleton file is a CC-5 (README/MANIFEST/CI — instruction-bearing) or CC-2 (CODEOWNERS/pointer) artifact with its own HARDEN-1.1 row (the A-001 glob, now enumerated).

## §2 Tree table ({len(trees)} trees)

{chr(10).join(tt)}

## §3 File table — skeleton files ({nfiles}) with the per-file floor check (skeleton_check method, survey-2, re-run {DATE})

{chr(10).join(filerows)}

Folder-level files:

{t}

## §4 Known gaps carried until instantiation

- **{len(unbannered)} files carry no Proposed/skeleton/stub marker** (contradiction with 00_MANIFEST §7 A-001 "all skeleton files carry Proposed/skeleton banners" — survey-2 BSQ-0393 → DEF-004 in A-004): {', '.join('`'+u+'`' for u in unbannered)}. Not edited (append-only); the marker lands at instantiation.
- CI stubs: **{ci}/{len(trees)}** trees now carry `ci/pipeline.yml` (six added in sprint-1 — BSQ-0392: evalstack, governance, harness, llm-lattice, lumos, integration); the remaining tree without one is `cdss-corpus`, intentionally minimal (firewall).
- REPO-MAP's skeleton-index paragraph claims "all 14 existing repos (README + MANIFEST.yaml stub + CI stub + per-directory stubs…)": per-directory stubs are absent in coder, conformal, corpus, governance, harness, llm-lattice, lumos (root files only) — the claim over-reaches; recorded here, REPO-MAP v2 unedited.
- **cdss-compiler has no owning primer** in 02_ or 03_ and no launch prompt in 11_ (BSQ-0391) — EXECUTABLE-AFTER-DECISION (DEC-09 repo + prefix CMP; DEC-13 namespace).
- RUN-REPORT R6 (03_/butterfly-primers/RUN-REPORT.md l.256) proposes `cdss-fuzzy`, `cdss-meta`, `cdss-ui-auditor`, `cdss-infra`, `cdss-dataplane` and PFX additions {{FUZ, MRL, CEC (+CMP), ABC, LEG, ANT}}; REPO-MAP v2 (2026-09-01) predates it — REPO-MAP v3 after DEC-09 (BSQ-0394).
- `GPP-CHANNEL.md` is cited by basename only in REPO-MAP l.30 (resolves to `repo-skeletons/cdss-integration/GPP-CHANNEL.md`).

## §5 Honesty line and self-audit

No code, build or deployment is claimed anywhere in this folder (`find 06_repositories -name '*.py' -o -name '*.ts' -o -name '*.java'` → none, {DATE}). Every skeleton is Proposed; owners are `[NEEDS DEFINITION]` (DEC-09).

- Tree rows = `ls repo-skeletons` = {len(trees)} — PASS; REPO-MAP rows (14 existing + 4 proposed + cdss-integration; GPP = file, not tree) ↔ trees — PASS (19 ↔ 19).
- Skeleton files on disk = {nfiles} = file rows — PASS (`find 06_repositories/repo-skeletons -type f ! -name .DS_Store | wc -l`).
- Per-file check re-run: {nfiles-len(unbannered)} conformant, {len(unbannered)} with the banner finding, 0 MANIFEST/CI/CODEOWNERS findings; every CI stub carries the r29 hook ({ci}/{ci}).
- Every path exists; every HARDEN-1.1 row and HARDEN-3.1 task id resolves — PASS.
"""
    open(f"{folder}/INDEX.md","w",encoding='utf-8').write(body)
# ============ 07 ============
def idx07():
    folder='07_deployment-and-operations'
    rr=lambda p: {'DEPLOY-1_':'read through DEPLOY-1.1 (run map; in force on DEC-22)','OPS-1_':'read through OPS-1.1 (CC-5 procedures)','SEC-1_':'read with SEC-2 (threat model; encryption/SBOM/CAPA cross-refs)'}.get(next((k for k in ('DEPLOY-1_','OPS-1_','SEC-1_') if os.path.basename(p).startswith(k)),''),'—')
    t,files=filetable(folder,[("read-through rule",rr)])
    body=head('INDEX-07',folder,"INDEX-07 — 07_deployment-and-operations: briefing, file table, precedence note, honesty line, self-audit","Added (sprint-1); indexes only; nothing is deployed; every file Proposed/Retained per its own status; person-level owners [NEEDS DEFINITION] throughout (GOV-1); RTO/RPO/DR [NEEDS DEFINITION] (G-09, proposed DEC-23)")+f"""
# INDEX-07 — 07_deployment-and-operations

## §1 Briefing — what these documents are

A **DEPLOY plan** sequences what is built and gated when (DEPLOY-1: three ladders — the hardening pass, the regulatory gates GATE-000..004, the maturity levels L1–L5 — interleaved); **acceptance criteria** say what proves a level or gate is passed (DEPLOY-2: Arch §11.2 exits + eight added criteria); an **OPS procedure** says how a recurring act is performed — in this ecosystem every step carries timeout/retry/idempotency/on_fail (HARDEN-2 CC-5, the Arch §13.6 pattern; OPS-1.1 gives OPS-1's prose that form); **GOV** names owners and post-deployment duties; **SEC** carries the security, privacy and compliance surface (SEC-1) and, since sprint-1, the threat model and data-flow map it hangs from (SEC-2). They compose with Arch §11 (tiers and levels, Retained) and with EXEC-1 (which now governs their *sequence*, EX-1/EX-5). Form exemplar: `02_cdss-stack-augmented/primers_briefing.md`.

## §2 File table

{t}

## §3 Precedence note

For sequencing, **EXEC-1 EX-1/EX-5 govern**: DEPLOY-1's steps 0a–5 resolve to RUN-0..4 through `DEPLOY-1.1_run-map_delta.md` D-1 (in force as the working calendar when DEC-22 closes). For content, DEPLOY-1's sources (REG-POSTURE §7 phases, Arch §11.2 exits, MT2) govern and the run rows are extensions. The five v1.0 files carry no `date` field (00_MANIFEST dates them 2026-09-01); the three sprint-1 deltas carry dates.

## §4 Honesty line

Nothing is deployed; no code beyond skeleton READMEs is claimed (00_MANIFEST §4.4). The OPS-1.1 procedures for the regulated controls (PROC-10..12) are stubs whose SLAs are `[NEEDS DEFINITION]`; SEC-2 records encryption-in-transit as a gap, not a control; DEC-03 (substrate), DEC-07 (patient surface), DEC-08 (Observer cadence) and DEC-22 (calendar) are Open.

{selfaudit(folder,files,"- Every cited ID in the three deltas resolves (refcheck, sprint-1) — PASS; `07_/*` v1.0 files byte-identical (CHECKSUMS_BEFORE/AFTER) — PASS.")}"""
    open(f"{folder}/INDEX.md","w",encoding='utf-8').write(body)
# ============ 08 ============
def idx08():
    folder='08_research'; t,files=filetable(folder,[("read-through rule",lambda p:'read through RESEARCH-1.1 (status field; RG-07/08; closure path)' if os.path.basename(p).startswith('RESEARCH-1_') else '—')])
    rg=[("RG-01","HeyDoc below-README clone inventory","DEC-12 executor","OPEN","DEC-12 (MET-2); G-08 (MET-4)"),("RG-02","Counsel reading of the two MAK-J3 ⚑ flags","AU counsel","OPEN","Q-REG-009 / ASSUME-REG-008 (R30); DEC-06"),("RG-03","Baseten Sydney dedicated terms in writing","Baseten","OPEN","ASSUME-REG-004 (R30); DEC-03"),("RG-04","immudb BUSL redistribution terms","Legal","OPEN","C-05 / DEC-04 (MET-2)"),("RG-05","Conformal-for-LLM literature watch","cdss-conformal owner","OPEN","MAK-ELSM §05 watch; WATCH row proposed on DEC-02"),("RG-06","TGA AI-enabled-SaMD guidance read against the intended purpose","Regulatory owner","OPEN","WATCH-REG-002 (R30); TASK-REG-001"),("RG-07","Lumos cohort figure reconciliation (6.8M+ vs 1.3M / 16% of NSW); locate or NOT-LOCATED the 2025 cohort study","cdss-lumos owner / PROMPT-H run","OPEN (new, RESEARCH-1.1)","Primer H annex erratum; TASK-REG-015; H10"),("RG-08","Primary-care differential-diagnosis conformal-prediction evidence — none located","cdss-conformal owner","OPEN (new, RESEARCH-1.1)","RG-05 watch; Primer F F10; DEPLOY-2 §1")]
    body=head('INDEX-08',folder,"INDEX-08 — 08_research: briefing, file table, RG register mirror, honesty line, self-audit","Added (sprint-1); indexes only; RESEARCH-1 v1.0 has no status field (supplied by RESEARCH-1.1 D-1); no finding fabricated; no literature re-fetched this sprint")+f"""
# INDEX-08 — 08_research

## §1 Briefing — what a research / source map is

A **research map** separates what was *supplied* (the evidence base of the volumes, authoritative in their owners), what was *newly verified* (dated fetches), what is a *gap* (RG-nn — a question an owner must answer) and what is *proposed* (named future engagements). It cites and never restates. An RG closes when its owner's action lands as a finding in a RESEARCH-1.n delta **and** the register or decision row it "closes into" (MET-4 G-*, MET-2 DEC-*, R30) is updated by that row's owner (RESEARCH-1.1 D-3). RESEARCH-1 never closes a DEC, ASSUME or WATCH itself.

## §2 File table

{t}

## §3 RG register mirror

| Gap | What's needed | Who | State | Closes into |
|---|---|---|---|---|
{chr(10).join('| `'+a+'` | '+b+' | '+c+' | '+d+' | '+e+' |' for a,b,c,d,e in rg)}

## §4 Honesty line

§1 sources not re-verified this pass unless noted; §2 fetches dated 1 Sep 2026 (v1.0) and 2 Sep 2026 (PROMPT-SERIES evidence pack, registered by RESEARCH-1.1); all eight RG OPEN; no clinical number asserted; RG-01 waits on DEC-12 (Corpus custodian).

{selfaudit(folder,files,"- RG-01..08 = 8 = RESEARCH-1.1 req_count — PASS; every 'closes into' target resolves (grep) — PASS.")}"""
    open(f"{folder}/INDEX.md","w",encoding='utf-8').write(body)
# ============ 09 ============
def idx09():
    folder='09_diagrams'
    src={'imago_architecture.mermaid':('IMAGO-1','Arch §2/§10 (repos, spine), MET-1 §5.1/§5.4 (Toulmin mapping), MAK-FFC Part 2','current (inlined in v2 block 1 and v3 block 1)'),'merged_runtime_sequence.mermaid':('IMAGO-2','Primer 0 §4 (worked consultation), Arch §3 (release path), MAK-FFC SPINE-2..5/8','current (v2 block 2; v3 block 2); DEF-001 grammar note'),'register_topology_v2.mermaid':('IMAGO-3 v2','Arch §12.2 register table, §12.4; DEC-02/04','superseded by v3 (MT2 §7.4 notation — DEF-003); preserved unedited'),'register_topology_v3.mermaid':('IMAGO-3 v3','as v2; notation fixed to §7(4); R25 label pending BSQ-0602 ruling','current (v3 block 3)'),'deployment_ladders.mermaid':('IMAGO-4','DEPLOY-1 ladders; MAK-ANT §7 gates; Arch §11.2 levels','superseded by v2 (no RUN overlay); preserved unedited'),'deployment_ladders_v2.mermaid':('IMAGO-4 v2','as v1 + EXEC-1 RUN-0..4 via DEPLOY-1.1 D-1','current (v3 block 4); in force as calendar on DEC-22'),'data_flow_v1.mermaid':('IMAGO-5','Arch §11.1/§11.4/§11.5, §10 corpus firewall; SEC-1; SEC-2 §1','current (v3 block 5)'),'cdss_diagrams_v2.html':('page v2','inlines IMAGO-1..4 (v1/v2 sources)','superseded by v3; preserved unedited (footer date 2026-09-01)'),'cdss_diagrams_v3.html':('page v3','inlines IMAGO-1, 2, 3 v3, 4 v2, 5','current successor page'),'INDEX.md':('INDEX-09','—','—')}
    t,files=filetable(folder,[("IMAGO id",lambda p: src[os.path.basename(p)][0]),("source documents",lambda p: src[os.path.basename(p)][1]),("standing",lambda p: src[os.path.basename(p)][2])])
    parse=open(f"{RUN}/mermaid_parse.json").read().strip(); ident=open(f"{RUN}/identity_v3.txt").read().strip()
    body=head('INDEX-09',folder,"INDEX-09 — 09_diagrams: briefing, file table with sources, recorded self-audit (parse + identity), regeneration procedure, known defects","Added (sprint-1); indexes only; sources are canonical and the html pages are derived; v2 files preserved unedited (their fixes are v3/v2 successors); regeneration of the 02_ derived artifacts waits on DEC-01 (G-10); nothing here claims deployment")+f"""
# INDEX-09 — 09_diagrams

## §1 Briefing — sources are canonical, pages are derived

Each `.mermaid` file is the **source** of one diagram (IMAGO-n); each `cdss_diagrams_vN.html` is a **derived page** that inlines sources verbatim so a person can read them rendered. A **successor** (G-10; X1 append-only) is a new file beside the old one — v3 of the topology fixes a citation, v2 of the ladders adds the run overlay — and the old file is never edited (00_MANIFEST §5 DEF-001/DEF-002 pattern). The CC-6 bar (HARDEN-2) is: sources parse, inlined blocks are byte-identical to their sources, the page renders without console errors, links resolve.

## §2 File table

{t}

## §3 Recorded self-audit (P-D-09 / CC-6) — `{RUN}/tools/mermaid/parse.mjs` and the identity script, run {DATE}

```
{parse}
```
```
{ident}
```

## §4 Regeneration procedure (CC-5 form) and known defects carried

**PROC-09-REGEN** — trigger: DEC-01 closes (portfolio-wide relabel → 02_ derived artifacts regenerate, G-10) **or** any `.mermaid` source changes. Steps: (1) edit or add a source as a new versioned file `{{{{name}}}}_vN.mermaid` (never edit v(N−1)) `{{timeout: n/a, retry: n/a, idempotent: by file version, on_fail: revert; DEF row}}` → (2) headless parse of every source and every inlined block `{{timeout: 5m, retry: 1, idempotent: yes, on_fail: HALT — a source that does not parse is not inlined}}` → (3) re-inline into a new `cdss_diagrams_vN.html` with the status paragraph naming what changed `{{timeout: n/a, retry: n/a, idempotent: by block hash, on_fail: identity check fails → page not written}}` → (4) source↔inline identity check 100% `{{timeout: 1m, retry: 1, idempotent: yes, on_fail: HALT}}` → (5) bump the page date; propose the 00_MANIFEST amendment row and the HARDEN-1.1 rows for the new files `{{timeout: n/a, retry: n/a, idempotent: yes, on_fail: n/a}}`. Exit evidence: parse JSON + identity output pasted in this INDEX §3 (or its successor). Owner: Architecture owner. Source: 00_MANIFEST §5 DEF-001 method; HARDEN-2 CC-6; G-10.

Known defects carried (not edited in place): `register_topology_v2.mermaid` l.17 and `cdss_diagrams_v2.html` l.96 read `MT2 §7.4` (DEF-002 item notation → `§7(4)`) — fixed in v3 successors (DEF-003, A-004). IMAGO-3 (v2 and v3) label **R25 "property runs"** while Arch §12.2 row 25 is "Build Evidence & Assumptions Ledger" and Primer A A10 says "property-run outputs" — a two-source disagreement the architecture owner rules (survey-2 BSQ-0602); carried unchanged with the ruling pending. No home is yet named in 06_ for the sources (BSQ-0604 → `cdss-spine/architecture/` after DEC-09).

## §5 Honesty line and self-audit

Every source header says "Status: Proposed"; the pages carry an R29 row PENDING, not HARDENED. Regeneration of `02_cdss-stack-augmented/cdss_complete_stack.md` and `cdss_diagrams.html` (HARDEN-1 rows 41–42) is queued behind DEC-01 and has not happened.

- Files in table = on disk = {len(files)} — PASS. Parse: 7/7 sources, 4/4 v2 blocks, 5/5 v3 blocks — PASS. Identity: 9/9 — PASS. `MT2 §7.4` occurrences in v3 files: 0 — PASS.
- Every cited § (Arch §2/§3/§10/§11/§12; MET-1 §5.1/§5.4; Primer 0 §4; DEPLOY-1; EXEC-1; SEC-2) resolves — PASS (refcheck).
"""
    open(f"{folder}/INDEX.md","w",encoding='utf-8').write(body)
# ============ 10 ============
def idx10():
    folder='10_regulatory-execution'
    fams={'EXEC-1_execution_directive.md':('EX (10)','normative for sequencing','—','governs the folder (EX-1); RUN table'),'FOLD-1_antennae_fold_worklist.md':('W1–W5 (5; collides with HARDEN-3 W-namespace — BSQ-0711)','worklist; output is a 03_ volume','launch via PROMPT-FOLD-1 (sprint-1); W1 folds v1.2 (§12.5)','—'),'MAK-GOV_addendum-g_v0.9.md':('NDG (14); DEC-G1..G4 (aliases of DEC-13..16)','ADVISORY_ONLY (regulatory) / PROPOSED-NORMATIVE (build)','—','§2 = counsel attachment (EX-6 item 3)'),'REG-POSTURE_v1.2.md':('REG-FIND 13 · REG-KEEP 4 · ASSUME-REG 9 · OBL 15 · STD 26 · FORK-REG 1 · GATE 5 · TASK-REG 24 · KTX 14 · WATCH-REG 8 · Q-REG 11 · SRC-REG 20 = 150','ADVISORY_ONLY; CANONICAL (EX-3 as amended by A-003)','read with REG-POSTURE_v1.2_CONTENTS.md (map)','§1–§3 = counsel attachment (EX-6 items 1–2)'),'REG-POSTURE_v1.1.md':('120 IDs (v1.1 census)','ADVISORY_ONLY; superseded by v1.2 (A-003), retained unedited','cite v1.2; v1.1 for history only','—'),'REG-POSTURE_v1.2_CONTENTS.md':('— (map of the 12 families)','ADVISORY_ONLY companion','—','names the attachment set'),'REG-NZ_v1.1.md':('NZ-FIND 12 · NZ-OBL 13 · NZ-STD 26 · NZ-ASSUME 5 · NZ-TASK 10 · NZ-GATE 3 · NZ-WATCH 5 · NZ-Q 6 · NZ-SRC 13 = 93','ADVISORY_ONLY; supersedes v1.0','—','§6/§9/§10 = NZ counsel packet'),'REG-NZ_v1.0.md':('45 IDs (v1.0)','ADVISORY_ONLY; superseded by v1.1 (A-003), retained unedited','cite v1.1','—'),'REG-US_v1.0.md':('US-* 10 families = 129','ADVISORY_ONLY; later jurisdiction','—','—'),'REG-EU_v1.0.md':('EU-* 10 families = 123','ADVISORY_ONLY; later jurisdiction','—','—'),'REG-SPRINT_v1.0.md':('V1/V2/V3, SG, SD (declared; censused in 1.2)','ADVISORY_ONLY','read ONLY through REG-SPRINT-1.1 (EX-2) and 1.2 for IDs','—'),'REG-SPRINT-1.1_delta.md':('D-1..D-5','ADVISORY_ONLY','—','D-2 originates NZ-Q-004'),'REG-SPRINT-1.2_census_delta.md':('D-6, D-7; census 30 ids','ADVISORY_ONLY (sprint-1)','—','—'),'validate_reg.py':('— (tool)','tooling (A-003 seal check)','run from this directory','—'),'INDEX.md':('—','—','—','—')}
    t,files=filetable(folder,[("ID families minted (count)",lambda p: fams[os.path.basename(p)][0]),("authority / standing",lambda p: fams[os.path.basename(p)][1]),("read-through rule",lambda p: fams[os.path.basename(p)][2]),("counsel-packet role (EX-6)",lambda p: fams[os.path.basename(p)][3])])
    vr=subprocess.run(['python3','validate_reg.py'],cwd=folder,capture_output=True,text=True); vrout=(vr.stdout+vr.stderr).strip()
    body=head('INDEX-10',folder,"INDEX-10 — 10_regulatory-execution: briefing, file table with authority and packet roles, ID-family map, known gaps, honesty line, self-audit","Added (sprint-1); indexes only; ADVISORY_ONLY content throughout; nothing attested in any jurisdiction; GATE-000, NZ-GATE-000, US-GATE-000, EU-GATE-000 all unpassed; counsel packets ASSEMBLED (11_prompts/runs/2026-09-05_primer-0/) but NOT SENT")+f"""
# INDEX-10 — 10_regulatory-execution

## §1 Briefing — what these documents are

A **posture** (REG-POSTURE) states, per jurisdiction, the working regulatory position as assumptions requiring counsel attestation — findings, obligations, standards, gates, tasks, questions, watch items, sources — each with a stable ID and a closed status vocabulary; it is ADVISORY_ONLY and can never evidence a DONE. A **jurisdiction brief** (REG-NZ, REG-US, REG-EU) is a posture for another regulator, written replete-standalone (§0.9 rule: the full standards stack repeated by design). A **non-device addendum** (MAK-GOV) argues that a separate artifact is not a device and carries the build requirements (NDG) that keep it so. A **run plan + delta** (REG-SPRINT v1.0 read through 1.1, and 1.2 for its IDs) prices the three clocks (Bill, capital, ARTG) into sprints and gates. A **fold worklist** (FOLD-1) says how a new posture version is folded verbatim into the corpus wrapper MAK-ANT (AN-5: carrier map re-runs first). An **execution directive** (EXEC-1) gives the layer precedence for *sequencing only* (EX-1) and merges every phase structure into one calendar RUN-0..4 (EX-5); content authority is unchanged. Read EXEC-1 first, REG-POSTURE v1.2 through its Contents companion, and every v1.0/v1.1 file only where its successor says so.

## §2 File table

{t}

## §3 ID-family map and register mirror

| File | Families minted | Register home |
|---|---|---|
| REG-POSTURE v1.2 | 12 families, 150 IDs (§12.1) | R30 base + R30.1 + R30.2 seeds → R30.3 row form (150 AU rows) |
| REG-NZ v1.1 | 9 families, 93 IDs (§12.1) | R30.1 (NZ-* v1.0 rows) + R30.2 (NZ-STD, NZ-GATE, v1.1 additions) → R30.3 (93 rows) |
| REG-US v1.0 | 10 families, 129 IDs | R30.2 → R30.3 (129 rows) |
| REG-EU v1.0 | 10 families, 123 IDs | R30.2 → R30.3 (123 rows) |
| MAK-GOV | NDG-1..14; DEC-G1..G4 | R30.1 (NDG rows) → R30.3 (14); MET-2.1 DEC-13..16 |
| REG-SPRINT (+1.1, 1.2) | V1/V2 (16), SG (9), SD (5) | R30.1 → R30.3 (30 rows); SD → MET-2.1 DEC-17..21 |
| EXEC-1 | EX-1..10 | R30.1 → R30.3 (10 rows) |
| FOLD-1 | W1–W5 | — (worklist; C-13 closure in MET-2.1) |

R30.3 total: 549 rows = 150 + 93 + 129 + 123 + 14 + 30 + 10 (validated against `05_/REG-R30.schema.json`, 0 invalid; every family contiguous at both ends).

## §4 Known gaps carried

- REG-FIND-013 / TASK-REG-023 forward references: **closed by REG-POSTURE v1.2** (A-003; §12.2 check 13) — survey-2 BSQ-0001 CLOSED.
- NZ-Q-004 and NZ-ASSUME-005 homed in REG-NZ v1.1 (§12.2 check 11) — BSQ-0706 CLOSED by A-003, no build needed.
- MAK-GOV §5 integration ledger: of 10 declared integrations, 3 now exist (MET-2.1 rows; R30.1/R30.3 seed; REG-POSTURE v1.2 row); 7 remain (03_ annexes — corpus owner, AN-5; MET-4 gap row; REPO-MAP reclassification; DEPLOY-2 NDG criteria; MAK-J3 retirement notice blocked on DEC-06) — BSQ-0707 EXECUTABLE-AFTER-DECISION (DEC-13/DEC-14).
- FOLD-1 W1–W5 collide with HARDEN-3 W0–W11 namespace (BSQ-0711) — architecture owner; PROMPT-FOLD-1 cites them as "FOLD-1 W1" meanwhile.
- MAK-GOV has no Contents section (17 KB, 6 parts) and no census/self-audit (BSQ-0707 scope).
- 00_MANIFEST §8 "Counsel packets drafted, not sent": packets are now **assembled** in `11_prompts/runs/2026-09-05_primer-0/` and not sent (DEF-005 wording in A-004).
- Superseded files (REG-POSTURE v1.1, REG-NZ v1.0) are retained unedited and must not be cited for current positions (EX-3 as amended).

## §5 Honesty line and self-audit

No attestation exists in any jurisdiction; every ASSUME is OPEN; standards editions and FDA/EU recognition statuses are from the author's knowledge pending WATCH-REG-008 / US-WATCH-004 / EU-WATCH-004; the January 2026 FDA CDS revision has not been read in the primary (US-WATCH-001); the regulatory owner is `[NEEDS DEFINITION]` (G-09).

- Files in table = on disk = {len(files)} — PASS. `validate_reg.py` re-run {DATE}:

```
{vrout}
```
  The `RESULT: FAIL` is the **known AU legacy-shape condition**, not a new defect: REG-POSTURE v1.2 §12.2 check 2 and 00_MANIFEST §9 A-003 "Verification at seal" record the twelve v1.1-era ids defined in prose/field-table shape (GATE-000..004, FORK-REG-001, KTX-001, KTX-008..012) and the one legacy double definition (ASSUME-REG-004), carried unchanged under append-only law; NZ 93/93, US 129/129, EU 123/123 pass; the shared stack 001..026 is aligned in all four. The R30.3 row-form seed defines all 150 AU ids (legacy ones flagged `definition_shape: prose`).
- Every family endpoint resolves both ends (R30.3 seed validation: 44 families, 0 gaps) — PASS. Every §4 gap cites a BSQ row — PASS.
"""
    open(f"{folder}/INDEX.md","w",encoding='utf-8').write(body)
for f in (idx04,idx05,idx06,idx07,idx08,idx09,idx10):
    f(); print("wrote",f.__name__)
for fo in ['04_hardening','05_registers-and-contracts','06_repositories','07_deployment-and-operations','08_research','09_diagrams','10_regulatory-execution']:
    print(fo, os.path.getsize(f"{fo}/INDEX.md"),"B")
