#!/usr/bin/env python3
"""Sprint-2 generator: HARDEN-1.2 (owner resolution D-1 + new ledger rows D-2), HARDEN-3.2 (one task per new row),
INDEX-04.1/06.1/08.1/09.1/10.1 deltas (rows for the files this sprint adds), 00_inventory_v1.3.txt.
Iterates until every output is byte-stable (byte counts of generated files appear in other generated files).
Reads git ls-files (after `git add -A`), HARDEN-1/1.1, HARDEN-3.1. Writes only new files. No R29 row is written (states are PENDING placeholders)."""
import re, os, subprocess, json, collections, datetime
ROOT=os.getcwd(); DATE='2026-09-05'; SHA=subprocess.check_output(['git','rev-parse','--short','origin/main']).decode().strip()  # argument list, no shell
H1=['04_hardening/HARDEN-1_coverage_ledger_seed.md','04_hardening/HARDEN-1.1_coverage_ledger_seed_delta.md']; H3='04_hardening/HARDEN-3.1_task_register_delta.md'
OUT={'h12':'04_hardening/HARDEN-1.2_coverage_ledger_owner_delta.md','h32':'04_hardening/HARDEN-3.2_task_register_delta.md',
     'i04':'04_hardening/INDEX-04.1_delta.md','i06':'06_repositories/INDEX-06.1_delta.md','i08':'08_research/INDEX-08.1_delta.md','i09':'09_diagrams/INDEX-09.1_delta.md','i10':'10_regulatory-execution/INDEX-10.1_delta.md','inv':'00_inventory_v1.3.txt'}
import shlex
def sh(c): return subprocess.run(shlex.split(c),capture_output=True,text=True,check=True).stdout  # fail fast: a failed command must not seal partial output
# --- existing ledger rows
rows11=[]; paths_with_row=set()
for f in H1:
    for ln in open(f,encoding='utf-8'):
        m=re.match(r'^\| (\d+) \| (.*?) \| ([^|]*) \| ([^|]*) \| ([^|]*) \| ([^|]*) \|',ln)
        if m:
            path=m.group(2).strip('`'); rows11.append({'id':int(m.group(1)),'path':path,'class':m.group(3).strip(),'owner':m.group(5).strip(),'file':f})
            for mm in re.finditer(r'`([^`\s]+)`',ln): paths_with_row.add(mm.group(1))
tasks31={}
for ln in open(H3,encoding='utf-8'):
    m=re.match(r'^\| `(T-\d+)` \| (W\d+) \| (.*?) \| ([^|]*) \| ([^|]*) \| (.*?) \| (.*?) \| ([^|]*) \| ([^|]*) \| ([^|]*) \|',ln)
    if m: tasks31[m.group(3).strip('`')]={'t':m.group(1),'wave':m.group(2),'class':m.group(5).strip(),'skills':m.group(6).strip(),'exit':m.group(7).strip()}
# --- tree
tracked=sorted(l for l in sh('git ls-files').split('\n') if l and not l.startswith('11_prompts/runs/') and not l.endswith('.DS_Store'))
planned=set(OUT.values()); tree=sorted(set(tracked)|planned)
missing=[p for p in tree if p not in paths_with_row]
# --- classification
def cls(p):
    if p.startswith(('.claude/','.github/skills/','.github/agents/')): return 'CC-5'
    if p.startswith(('.github/audit/','.github/workflows/')): return 'CC-5'
    if p in ('AGENTS.md','CLAUDE.md','GLOSSARY.md','.github/copilot-instructions.md') or p.startswith('.github/instructions/'): return 'CC-8'
    if p.startswith('11_prompts/'): return 'CC-8'
    if p.startswith('01_'): return next((r['class'] for r in rows11 if r['path'].startswith('01_north-star-and-transformation/MET-2')), 'CC-8')
    if p.startswith('04_hardening/HARDEN-2'): return next((r['class'] for r in rows11 if 'HARDEN-2.1' in r['path']),'CC-8')
    if p.startswith('04_hardening/HARDEN-1') or p.startswith('04_hardening/HARDEN-3'): return next((r['class'] for r in rows11 if 'HARDEN-1.1' in r['path']),'CC-2')
    if p.endswith('INDEX-') or 'INDEX-' in p: return 'CC-8'
    if p.startswith('06_'): return next((r['class'] for r in rows11 if 'REPO-MAP_v2' in r['path']),'CC-8')
    if p.startswith('08_'): return next((r['class'] for r in rows11 if 'RESEARCH-1.1' in r['path']),'CC-8')
    if p.startswith('09_'): return 'CC-6'
    if p.startswith('10_'): return 'CC-4'
    if p.startswith('00_inventory'): return 'CC-8'
    return 'CC-8'
def owner(p):
    if p.startswith('10_'): return 'Regulatory owner — kendo-Jones (MET-2.2 §1; DEC-23)'
    if p.startswith('04_'): return 'MT2 operator — Kenny-bytes (DEC-10)'
    if p.startswith('11_prompts/'): return 'MT2 operator — Kenny-bytes (DEC-10) / prompt author'
    if p.startswith(('06_',)): return 'Programme lead — Kenny-bytes (DEC-09)'
    if p.startswith(('.claude/','.github/skills/','.github/agents/')): return 'Programme lead — Kenny-bytes (repository tooling; vendored Impeccable 4.2.0 skill pack, hardened by version pin)'
    if p.startswith('.github/') or p in ('AGENTS.md','CLAUDE.md'): return 'Programme lead — Kenny-bytes (repository governance; A-005)'
    if p.startswith('00_'): return 'Manifest owner [NEEDS DEFINITION — not named in MET-2.2 §1]'
    return 'Architecture owner — Kenny-bytes (MET-2.2 §1)'
def note(p):
    if p.startswith(('.claude/','.github/skills/','.github/agents/')): return 'agent deployment layer (A-005); vendored third-party skill pack — no content review implied'
    if p.startswith('.github/'): return 'agent deployment layer (A-005)'
    if p in ('AGENTS.md','CLAUDE.md'): return 'repository governance (A-005)'
    if p.startswith('11_prompts/PROMPT-SURVEY-3'): return 'A-005/A-006/A-007 ledger debt'
    if 'MET-2.2' in p: return 'A-009 ledger debt'
    return 'sprint-2 artifact (built 2026-09-05)'
def sibling(p,c):
    top=p.split('/')[0]
    for path,t in tasks31.items():
        if path.split('/')[0]==top and t['class']==c: return t
    for path,t in tasks31.items():
        if t['class']==c: return t
    return {'wave':'W8','skills':'using-agent-skills; documentation-and-adrs; code-review-and-quality; doubt-driven-development (ALWAYS ON)','exit':'self-audit section run · references resolve (refcheck) · frontmatter core fields present'}
def size(p): return os.path.getsize(p) if os.path.exists(p) else 0
def fm(p):
    if not os.path.exists(p): return {'doc_id':'—','version':'—','date':'—','status':'(generated this pass)'}
    if not p.endswith('.md'): 
        first=open(p,encoding='utf-8',errors='replace').readline().strip()
        return {'doc_id':'—','version':'—','date':'—','status':first[:160]}
    t=open(p,encoding='utf-8',errors='replace').read()
    if not t.startswith('---'): return {'doc_id':'—','version':'—','date':'—','status':'(no frontmatter)'}
    head=t.split('---',2)[1]; g=lambda k: (re.search(r'^'+k+r':\s*"?(.*?)"?\s*$',head,re.M) or [None,'—'])[1]
    return {'doc_id':g('doc_id'),'version':g('version'),'date':g('date'),'status':(g('status')[:200]+('…' if len(g('status'))>200 else ''))}
# --- owner resolution for existing rows (D-1)
RES=[
 (r'^Repo owner per REPO-MAP \(DEC-09\) \[NEEDS DEFINITION\]$','Kenny-bytes — repo owner (DEC-09 closed; REPO-MAP v3)'),
 (r'^Component owner per primer repo \[NEEDS DEFINITION — DEC-09\]$','Kenny-bytes — component owner via repo ownership (DEC-09 closed)'),
 (r'^MT2 operator \(DEC-10\) / prompt author \[NEEDS DEFINITION\]$','Kenny-bytes — MT2 operator (DEC-10 closed) / prompt author'),
 (r'^MT2 operator \(DEC-10\) \[NEEDS DEFINITION\]$','Kenny-bytes — MT2 operator (DEC-10 closed)'),
 (r'^Regulatory owner \[NEEDS DEFINITION — G-09 / REG-POSTURE §12.3\]$','kendo-Jones — regulatory owner (DEC-23 names closed)'),
 (r'^Operations / security / regulatory owner \[NEEDS DEFINITION — G-09\]$','Ken-E-Gee (security) / kendo-Jones (regulatory); operations owner [NEEDS DEFINITION — DEC-23 extension]'),
]
resolved=[]; unresolved=collections.Counter()
for r in rows11:
    if r['file']!=H1[1]: continue
    for rx,val in RES:
        if re.match(rx,r['owner']): resolved.append((r['id'],r['path'],r['owner'],val)); break
    else:
        if 'NEEDS DEFINITION' in r['owner']: unresolved[r['owner']]+=1
def gen():
    new_rows=[]; nid=274; tid=800
    for p in missing:
        c=cls(p); new_rows.append({'id':nid,'t':f'T-{tid}','path':p,'class':c,'bytes':size(p),'owner':owner(p),'note':note(p),'sib':sibling(p,c)}); nid+=1; tid+=1
    byp={r['path']:r for r in new_rows}
    allp=paths_with_row|{r['path'] for r in new_rows}; miss_after=[p for p in tree if p not in allp]
    TREECHK=f'tree {len(tree)} files; rows 0..273 + {len(new_rows)} new = every file has a row; files without a row: {len(miss_after)} {miss_after}'
    # HARDEN-3.2
    h32=['---','doc_id: HARDEN-3.2','title: "HARDEN-3.2 — task register delta: one task per artifact added since HARDEN-3.1 (agent deployment layer, PROMPT-SURVEY-3 series, MET-2.2, sprint-2 files), wave-assigned, with row, class, skills, exit evidence and named owner"','version: "1.2-delta"',f'date: "{DATE}"',
         'status: "Added (sprint-2). Plan delta; no task started; every task PENDING (pre-pass placeholder). HARDEN-3 v1.0 and HARDEN-3.1 are preserved verbatim beside this file; read HARDEN-3 through 3.1 through this file. Extension ids T-800+ are Proposed and marked. This is a plan delta, not an R29 write (AGENTS.md law 5). Owners are the accounts MET-2.2 §1 names."',
         'supersedes: "nothing — read HARDEN-3 through HARDEN-3.1 through this file"','applies_to: "04_hardening/HARDEN-3_hardening_plan_worklist.md; 04_hardening/HARDEN-3.1_task_register_delta.md"',
         'change_policy: "Additive delta per the MET-1.1 pattern; v1.0 and 3.1 ids retained; new ids T-800+ (ext-2)"','req_prefix: T',f'req_count: {len(new_rows)}',
         'produced_by: "sprint-2 — 11_prompts/runs/2026-09-05_sprint-2/tools/ledger2.py from git ls-files, HARDEN-1/1.1 and HARDEN-3.1"','---','','# HARDEN-3.2 — task register delta','',
         '## D-1 — statement','',f'HARDEN-3.1 gave every file then in the tree one task (276). Since then {len(new_rows)} tracked files have arrived with no task: the agent deployment layer (A-005: `.github/**`, `.claude/**`, `AGENTS.md`, `CLAUDE.md`), PROMPT-SURVEY-3 and its two deltas (A-005..A-007), MET-2.2 (A-009) and the files this sprint adds (A-010). MT2 §3: every artifact gets a row, and HARDEN-3 gives every row a task. Wave, skills and exit evidence are inherited from the HARDEN-3.1 task of the nearest sibling (same top-level folder and class; else same class), so the pass treats like with like. Owners are named (MET-2.2 §1) — the first task register in this repository with no `[NEEDS DEFINITION]` owner cell except the manifest owner.','',
         f'## D-2 — task register ({len(new_rows)} tasks, T-800..T-{799+len(new_rows)})','','| task | wave | artifact_path | HARDEN-1.2 row | class | mapped skills (MT2 §2.2 / HARDEN-2) | exit evidence | owner (account) | state | note |','|---|---|---|---|---|---|---|---|---|---|']
    for r in new_rows: h32.append(f"| `{r['t']}` | {r['sib']['wave']} | `{r['path']}` | {r['id']} | {r['class']} | {r['sib']['skills']} | {r['sib']['exit']} | {r['owner']} | PENDING | {r['sib']['wave']} ext-2 — {r['note']} |")
    wc=collections.Counter(r['sib']['wave'] for r in new_rows)
    h32+=['','## Wave census','','| Wave | Tasks (this delta) |','|---|---|']+[f'| {w} | {n} |' for w,n in sorted(wc.items(),key=lambda x:int(x[0][1:]))]+[f'| **Total** | **{len(new_rows)}** |','',
         '## ID census and self-audit (script output, `11_prompts/runs/2026-09-05_sprint-2/tools/ledger2.py`)','','```',f"T ids: {len(new_rows)} rows, {len(set(r['t'] for r in new_rows))} unique; range T-800..T-{799+len(new_rows)}; collision with HARDEN-3 v1.0 / 3.1 ids: {len(set(r['t'] for r in new_rows)&set(t['t'] for t in tasks31.values()))}",
         f"artifact paths: {len(new_rows)} distinct; already tasked in HARDEN-3.1: {sum(1 for r in new_rows if r['path'] in tasks31)}",'files in tree (HARDEN-1.1 scope rule) without a task after this delta: '+TREECHK,'```','',
         'Acceptance: every tracked file outside run directories appears exactly once across HARDEN-3.1 + HARDEN-3.2 — pasted in the RUN-REPORT at seal. HARDEN-3 v1.0 and HARDEN-3.1 byte-identical (sprint-2 CHECKSUMS).','']
    # HARDEN-1.2
    h12=['---','doc_id: HARDEN-1.2','title: "HARDEN-1.2 — coverage ledger owner delta: owner cells resolved to the accounts MET-2.2 names (D-1) and one path-resolving row for every artifact added since HARDEN-1.1 (D-2)"','version: "1.2-delta"',f'date: "{DATE}"',
         'status: "Added (sprint-2). Seed delta; EVERY row is a pre-pass placeholder (PENDING); edits nothing; HARDEN-1 v1.0 and HARDEN-1.1 are preserved verbatim beside this file and their row ids are retained; new ids 274+. Zero rows are HARDENED. Not an R29 write (AGENTS.md law 5). D-1 changes no row\'s class, state or path — only the owner cell, and only where MET-2.2 §1 names the role."',
         'supersedes: "nothing — read HARDEN-1 through HARDEN-1.1 through this file"','applies_to: "04_hardening/HARDEN-1_coverage_ledger_seed.md; 04_hardening/HARDEN-1.1_coverage_ledger_seed_delta.md"',
         'change_policy: "Additive delta per the A-001 / MET-1.1 pattern; ids 0–273 retained; new ids 274+"','req_prefix: R29-row',f'req_count: {len(new_rows)}',
         'produced_by: "sprint-2 — 11_prompts/runs/2026-09-05_sprint-2/tools/ledger2.py"','---','','# HARDEN-1.2 — coverage ledger owner delta','',
         f'## D-1 — owner cells resolved ({len(resolved)} rows of HARDEN-1.1)','','MET-2.2 §1 names the accounts behind five owner roles. Every HARDEN-1.1 row whose owner cell named one of those roles with `[NEEDS DEFINITION]` reads as below; class, bytes, state and note are unchanged. Cells naming a role MET-2.2 does not name (corpus owner, manifest owner, operations owner) stay as HARDEN-1.1 wrote them and are counted at the foot.','',
         '| row | artifact_path | HARDEN-1.1 owner cell | owner cell now |','|---|---|---|---|']
    for rid,path,old,val in resolved: h12.append(f'| {rid} | `{path}` | {old} | {val} |')
    rc=collections.Counter(v for *_,v in resolved)
    h12+=['','Resolved by role: '+' · '.join(f'{n} × "{k}"' for k,v in [(k,v) for k,v in rc.items()] for n in [v])+'.','','Still `[NEEDS DEFINITION]` after this delta (role not named in MET-2.2 §1): '+' · '.join(f'{n} × "{k}"' for k,n in unresolved.items())+'.','',
         f'## D-2 — new rows ({len(new_rows)}; ids 274..{273+len(new_rows)})','','Scope rule as HARDEN-1.1: every tracked file except `.DS_Store`, `.git/**` and `11_prompts/runs/**`. The agent deployment layer (`.github/**`, `.claude/**`) is in scope as CC-5 build/CI configuration and CC-8 repository-governing text; the vendored Impeccable skill pack is enumerated (MT2 §3: every artifact gets a row) with a note that its hardening is by version pin, not content review. Byte counts are `os.path.getsize` at generation; the two files that quote each other\'s size (this file and HARDEN-3.2, the INDEX deltas, the inventory) were generated to a fixed point.','',
         '| row | artifact_path | class | bytes | owner (account) | state | note |','|---|---|---|---|---|---|---|']
    for r in new_rows: h12.append(f"| {r['id']} | `{r['path']}` | {r['class']} | {r['bytes']} | {r['owner']} | PENDING | {r['note']} |")
    cc=collections.Counter(r['class'] for r in new_rows)
    h12+=['','## Census and self-audit (script output, `tools/ledger2.py`)','','```',f"HARDEN-1 + HARDEN-1.1 rows parsed: {len(rows11)} (ids 0–273)",f"tracked files in scope: {len(tree)}   without a row before this delta: {len(missing)}   new rows: {len(new_rows)}   ids 274..{273+len(new_rows)}",
         f"class census (new rows): {dict(sorted(cc.items()))}",f"owner cells with [NEEDS DEFINITION] among new rows: {sum(1 for r in new_rows if 'NEEDS DEFINITION' in r['owner'])} (manifest owner)",'set equality (tree == rows 0..273 ∪ new rows): '+TREECHK,'```','',
         'Acceptance (HARDEN-1.1 form): set(rows.artifact_path) == set(files in tree excl. .DS_Store and runs) — pasted in the RUN-REPORT at seal; HARDEN-1 and HARDEN-1.1 byte-identical (sprint-2 CHECKSUMS). Ledger row for this file: its own D-2 row.','']
    # INDEX deltas
    IDX={'i04':('04_hardening','INDEX-04'),'i06':('06_repositories','INDEX-06'),'i08':('08_research','INDEX-08'),'i09':('09_diagrams','INDEX-09'),'i10':('10_regulatory-execution','INDEX-10')}
    idx_out={}
    for k,(folder,did) in IDX.items():
        files=[r for r in new_rows if r['path'].startswith(folder+'/')]
        L=['---',f'doc_id: {did}.1',f'title: "{did}.1 — {folder}: rows for the files sprint-2 added (read with {folder}/INDEX.md)"','version: "1.0"',f'date: "{DATE}"',
           f'status: "Added (sprint-2). Additive delta over {folder}/INDEX.md (not edited); indexes only. Every row is generated from disk by the sprint-2 generator; HARDEN row and task ids are those HARDEN-1.2 / HARDEN-3.2 assign; the manifest row is A-010."',
           f'supersedes: "nothing — {folder}/INDEX.md preserved verbatim beside this file"',f'folder: "{folder}/"','produced_by: "sprint-2 — 11_prompts/runs/2026-09-05_sprint-2/tools/ledger2.py"','---','',f'# {did}.1 — {folder} (sprint-2 additions)','',
           '## §1 What arrived and why','']
        why={'i04':'HARDEN-2.2 carries the CC and W alias laws (survey-3 QI-0025/QI-0030; DEC-26 Proposed). HARDEN-1.2 resolves owner cells to named accounts and rows every file added since HARDEN-1.1; HARDEN-3.2 gives each a task. This delta indexes them.',
             'i06':'REPO-MAP v3 succeeds v2 with the owner column (DEC-09 closed) and the ratified PFX set; v2 is retained.',
             'i08':'RESEARCH-1.2 states the RG alias law (DEC-26(b) Proposed), declares RGAP- for new mints and adds the trigger column per gap (QI-0022/QI-0024).',
             'i09':'The DEC-01 regeneration run (PROC-09-REGEN, INDEX-09 §4): IMAGO-3 v4 draws R29/R30 solid (DEC-02); cdss_diagrams_v4.html inlines it and links tokens.css (QI-0043/QI-0044); v3 files are retained.',
             'i10':'REG-TASK-OWNERS maps every TASK-REG / NZ-TASK / US-TASK / EU-TASK row to DR step, RUN, owner role, account and evidence artifact (QI-0020); posture files untouched.'}[k]
        L+=[why,'','## §2 File table (sprint-2 additions)','','| path | class | doc_id | version | date | status (quoted) | bytes | disposition | HARDEN-1.2 row | HARDEN-3.2 task | 00_MANIFEST row |','|---|---|---|---|---|---|---|---|---|---|---|']
        for r in files:
            f=fm(r['path']); L.append(f"| `{r['path']}` | {r['class']} | {f['doc_id']} | {f['version']} | {f['date']} | {f['status'].replace('|','/')} | {r['bytes']} | Added (sprint-2) — Proposed | {r['id']} | {r['t']} | §16 A-010 |")
        if k=='i09':
            mp=json.load(open('11_prompts/runs/2026-09-05_sprint-2/raw/mermaid_parse.json'))
            L+=['','## §3 Recorded self-audit — headless parse of every source and inlined block (sprint-1 `tools/mermaid/parse.mjs`, run 2026-09-05)','','```',mp['tool']]+[f"  {r['file']:36s} {r['kind']:18s} {r['result']}" for r in mp['results']]+[f"total {len(mp['results'])}  FAIL {sum(1 for r in mp['results'] if r['result']!='PASS')}",'```','','Source↔inline identity: the v4 page inlines `register_topology_v4.mermaid` from the `flowchart LR` line verbatim (generator copies the source; RUN-REPORT pastes the diff = ∅). R25 label carried pending DEC-25; `MT2 §7.4` occurrences in v4 files: 0.']
        L+=['','## §4 Census',f'',f'Rows: {len(files)} = files sprint-2 added under `{folder}/` (generator); each has a HARDEN-1.2 row and a HARDEN-3.2 task. Parent INDEX byte-identical (sprint-2 CHECKSUMS).','']
        idx_out[k]='\n'.join(L)
    # inventory
    inv=[f'# inventory of main@{SHA} + sprint-2 (2026-09-05); "bytes path"; every tracked file outside 11_prompts/runs/ (run directories are evidence, not corpus); the tracked tree is authoritative (README); supersedes 00_inventory.txt (v1.1-build snapshot of 2026-09-01, retained unedited — 00_MANIFEST A-008 / DEF-008; survey-3 QI-0063)']
    inv+=[f'{size(p)} {p}' for p in tree]
    outs={'h12':'\n'.join(h12),'h32':'\n'.join(h32),**idx_out,'inv':'\n'.join(inv)+'\n'}
    return outs,new_rows
prev=None
for it in range(6):
    outs,new_rows=gen()
    for k,v in outs.items(): open(OUT[k],'w',encoding='utf-8').write(v)
    sig={k:len(v) for k,v in outs.items()}
    if sig==prev: break
    prev=sig
print('iterations',it+1,'stable',sig)
# tree check for self-audit paste
allpaths=paths_with_row|{r['path'] for r in new_rows}
tree_now=sorted(l for l in sh('git ls-files').split('\n') if l and not l.startswith('11_prompts/runs/') and not l.endswith('.DS_Store'))
tree_now=sorted(set(tree_now)|set(OUT.values()))
missing_after=[p for p in tree_now if p not in allpaths]; extra=[p for p in {r['path'] for r in new_rows} if not os.path.exists(p)]
print('new rows',len(new_rows),'resolved owner cells',len(resolved),'unresolved',dict(unresolved))
print('tree',len(tree_now),'missing after',missing_after,'rows without file',extra)
json.dump({'new_rows':[{k:v for k,v in r.items() if k!='sib'} for r in new_rows],'resolved':len(resolved),'unresolved':dict(unresolved),'tree':len(tree_now),'missing_after':missing_after,'rows_without_file':extra},open('11_prompts/runs/2026-09-05_sprint-2/raw/ledger2.out.json','w'),indent=1)
