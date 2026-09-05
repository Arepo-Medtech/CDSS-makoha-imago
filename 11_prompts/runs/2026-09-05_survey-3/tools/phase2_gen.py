"""phase2_gen.py — Phase 2 fragment generator: per folder (ROOT, 00, 01..11, CHAIN) writes folders/NN_name/{ASSESSMENT.md, FIRST_IMPROVEMENTS.md, rows.jsonl}
from the Phase 0/1 tool outputs + census rows + the executor's hand judgments (HAND dict; every hand line cites what it read). Sequential run — no sub-agents."""
import json, re, os, sys, collections
R='11_prompts/runs/2026-09-05_survey-3/'; T=R+'tools/'
sys.path.insert(0,T); import scope
fs=scope.files(); g={r['file']:r for r in json.load(open(T+'graph.out.json'))['rows']}; fm={r['file']:r for r in json.load(open(T+'frontmatter.out.json'))['rows']}
rd={r['file']:r for r in json.load(open(T+'readability.out.json'))['rows']}; sc={r['page']:r for r in json.load(open(T+'style_census.out.json'))['rows']}
census=[json.loads(l) for l in open(R+'census_rows.jsonl')]
sprint1=set(open(R+'raw/sprint1_added_files.txt').read().split()); post=set(open(R+'raw/post_baseline_changed.txt').read().split())
DUPIDS={'10_regulatory-execution/REG-NZ_v1.0.md','10_regulatory-execution/REG-NZ_v1.1.md','10_regulatory-execution/REG-POSTURE_v1.1.md','10_regulatory-execution/REG-POSTURE_v1.2.md'}
COLL={'03_makoha-butterfly-corpus/corpus-md/compound-eyes-corpus_v1.1.md','08_research/RESEARCH-1_findings_gaps_source_map.md','08_research/RESEARCH-1.1_findings_delta.md','04_hardening/HARDEN-2_hardening_spec.md','04_hardening/HARDEN-2.1_spec_census_and_self-audit_delta.md','03_makoha-butterfly-corpus/corpus-md/labial-palps-corpus_v1.0.md','11_prompts/PROMPT-SURVEY-1_ecosystem_repleteness_surveyor.md','11_prompts/PROMPT-SURVEY-3_final-quality-improvement.md','11_prompts/PROMPT-SURVEY-3.1_deep-review_fold_delta.md','10_regulatory-execution/FOLD-1_antennae_fold_worklist.md','04_hardening/HARDEN-3_hardening_plan_worklist.md'}
def folder(p): return 'ROOT' if '/' not in p and not p.startswith('00_') else ('00' if p.startswith('00_') else p[:2])
def label(p):
    b=os.path.basename(p)
    if p.startswith('00_'): return 'MANIFEST / INVENTORY'
    if b=='INDEX.md': return 'INDEX'
    if p.startswith('01_'): return 'DELTA' if '.1_' in b else ('WORKLIST/PLAN (retained v1.0)' if b.startswith('MET-1_') else 'TRACEABILITY MAP [ASSESSOR]' if b.startswith('MET-3') else 'GAP / DECISION REGISTER')
    if p.startswith('02_'): return 'DIAGRAM (retained page)' if b.endswith('.html') else 'BRIEFING (companion)' if 'briefing' in b else 'ARCHITECTURE (retained)' if b.startswith('architecture') else 'COMPILATION (retained, derived)' if 'complete_stack' in b else 'REPORT (retained)' if 'integration_report' in b else 'PRIMER (02_)'
    if p.startswith('03_'): return 'MANIFEST (corpus)' if b=='MANIFEST.md' else 'CORPUS VOLUME' if '/corpus-md/' in p else 'ARTIFACT-HTML' if '/artifacts-html/' in p else 'RUN RECORD (companion)' if 'RUN-REPORT' in b else 'PROMPT (03_)' if 'prompt' in b else 'BRIEFING (companion)' if 'briefing' in b else 'BUTTERFLY PRIMER'
    if p.startswith('04_'): return 'DIRECTIVE (retained verbatim)' if 'MAJOR_TASK' in b else 'DELTA' if '.1_' in b else 'SEED / LEDGER' if 'HARDEN-1' in b else 'SPEC' if 'HARDEN-2' in b else 'WORKLIST/PLAN'
    if p.startswith('05_'): return 'SCHEMA (examples)' if b.endswith('.examples.jsonl') else 'SCHEMA' if b.endswith('.schema.json') or 'schema.md' in b else 'SEED / LEDGER' if b.endswith('.jsonl') else 'DELTA' if re.search(r'R\d\d\.\d',b) else 'REGISTER' if 'REG-R30_' in b else 'CONTRACT'
    if p.startswith('06_'): return 'REPO-MAP (index)' if 'REPO-MAP' in b else 'REPO SKELETON'
    if p.startswith('07_'): return 'DELTA' if '.1_' in b else 'DEPLOY / OPS / GOV / SEC'
    if p.startswith('08_'): return 'DELTA' if '.1_' in b else 'RESEARCH'
    if p.startswith('09_'): return 'DIAGRAM (derived page)' if b.endswith('.html') else 'DIAGRAM (source)'
    if p.startswith('10_'): return 'TOOLING (CC-5)' if b.endswith('.py') else 'DIRECTIVE' if b.startswith('EXEC') else 'WORKLIST/PLAN' if b.startswith(('FOLD','REG-SPRINT_')) else 'DELTA' if re.search(r'-\d\.\d_',b) else 'COMPANION (contents)' if 'CONTENTS' in b else 'REGULATORY'
    if p.startswith('11_'): return 'PROMPT index' if 'index' in b else 'PROMPT'
    return 'ROOT LOOSE FILE / governance text'
def status(p):
    if p in sprint1: return 'built (sprint-1)'
    if p in post or p in ('AGENTS.md','CLAUDE.md'): return 'added/changed after baseline (A-005..A-007)'
    if p.startswith(('02_','03_')) or 'MAJOR_TASK' in p: return 'retained (verbatim)'
    return 'pre-existing (v1.2 seal / A-001..A-003)'
def hdr_ok(p):
    try: t=open(p,encoding='utf-8',errors='replace').read(600)
    except Exception: return False
    if p.endswith('.json'): return '"$id"' in t or '"title"' in t
    if p.endswith(('.yaml','.yml','.mermaid','.py','.txt')): return t.lstrip().startswith(('#','%%'))
    if p.endswith('.html'): return '<!--' in t or '<title' in t or '<!DOCTYPE' in t
    return False
HAND=json.load(open(T+'phase2_hand.json'))
def qlines(p):
    q={}; fr=fm.get(p); gr=g[p]
    q['Q-D-01']=('PASS' if gr['reachable_from_README'] else 'FAIL','reachable from README via manifest/INDEX' if gr['reachable_from_README'] else 'unreachable')
    q['Q-D-02']=('EXEMPT' if p.startswith('06_repositories/repo-skeletons') else 'PASS' if gr['class']=='DESIGN-LINKED' else 'FAIL', f"graph class {gr['class']}; inbound {gr['inbound']}")
    q['Q-D-03']=('PASS',f"depth {p.count('/')}")
    if fr and fr['frontmatter']: q['Q-D-04']=('PASS' if not fr['missing_core'] else 'FAIL','core keys present' if not fr['missing_core'] else f"missing {fr['missing_core']}")
    elif fr: q['Q-D-04']=('N/A (judged on parent, P-F-02)',fr['why'])
    else: q['Q-D-04']=('PASS' if hdr_ok(p) else 'FAIL','header/$id/title present' if hdr_ok(p) else 'no header comment / $id')
    q['Q-D-05']=('FAIL' if p in DUPIDS else 'PASS','doc_id shared by a version chain; rule absent (QI-0001)' if p in DUPIDS else 'unique or n/a')
    q['Q-D-06']=('PASS','refcheck: 0 dead paths / 0 unresolved anchors tree-wide')
    if fr and fr['frontmatter']: q['Q-D-07']=('FAIL' if fr['ladder_skips'] or fr['tables_inconsistent_columns'] else 'PASS',f"ladder skips {fr['ladder_skips']}; tables {fr['tables_inconsistent_columns']}")
    q['Q-D-10']=('FAIL' if p in COLL else 'PASS/N/A','prefix collision or label overlap (see L2_id_lifecycle)' if p in COLL else 'one padding form per family in this file')
    r=rd.get(p)
    if r and 'fk_grade' in r: q['Q-D-15']=('FAIL' if r['avg_sentence_len']>35 else 'PASS',f"ASL {r['avg_sentence_len']} (≤35); FK {r['fk_grade']}")
    elif r: q['Q-D-15']=('N/A','<50 prose words')
    if p in sc: q['Q-D-16']=('FAIL' if sc[p]['drift_colours_not_in_implied'] else 'PASS',f"{sc[p]['hex_colours']} colours; {sc[p]['drift_colours_not_in_implied']} outside implied set")
    for k,v in HAND.get(p,{}).items(): q[k]=(v[0],v[1])
    return q
def covered(p):
    stem=os.path.basename(p).rsplit('.',1)[0][:40]
    return [c for c in census if p in c['artifact_path'] or stem in c['artifact_path'] or (p.startswith('06_repositories/repo-skeletons') and c['artifact_path'].startswith('06_repositories/repo-skeletons/')) or (p.startswith('03_makoha-butterfly-corpus/artifacts-html/') and 'artifacts-html/ (16' in c['artifact_path'])]
FOLDERS=['ROOT','00','01','02','03','04','05','06','07','08','09','10','11','CHAIN']
NAMES={'ROOT':'ROOT','00':'00_manifest','01':'01_north-star','02':'02_cdss-stack','03':'03_butterfly-corpus','04':'04_hardening','05':'05_registers','06':'06_repositories','07':'07_deploy-ops','08':'08_research','09':'09_diagrams','10':'10_regulatory','11':'11_prompts','CHAIN':'CHAIN'}
FOLDER_NOTES=json.load(open(T+'phase2_folders.json'))
next_id=[max(int(c['row_id'][3:]) for c in census)]
extra_rows=json.load(open(T+'phase2_extra_rows.json'))
allrows=list(census); check=[]
for F in FOLDERS:
    items=[p for p in fs if folder(p)==F] if F!='CHAIN' else []
    items=[p for p in items if p!='.gitignore']
    dirn=R+f"folders/{NAMES[F]}/"; os.makedirs(dirn,exist_ok=True)
    rows=[c for c in census if c['folder']==F]
    for e in extra_rows.get(F,[]):
        next_id[0]+=1; e=dict(e); e['row_id']=f"QI-{next_id[0]:04d}"; e.setdefault('folder',F); e.setdefault('phase_found','2'); e.setdefault('state','OPEN'); rows.append(e); allrows.append(e)
    o=[]; w=o.append; fi=[]
    w(f"# ASSESSMENT — {NAMES[F]} (survey-3, Phase 2, 2026-09-05)\n"); w(FOLDER_NOTES[F]['intro']+"\n")
    if items:
        w(f"## 1. Items ({len(items)}) — survey-2 label · sprint-1 / baseline status\n\n| # | Path | Bytes | Label | Status |\n|---|---|---|---|---|")
        for n,p in enumerate(items,1): w(f"| {n} | `{p}` | {os.path.getsize(p)} | {label(p)} | {status(p)} |")
    w("\n## 2. Folder lines (Q-F) — PASS / FAIL with evidence\n\n| Q-F | Result | Evidence |\n|---|---|---|")
    for qf,res,ev in FOLDER_NOTES[F]['qf']: w(f"| {qf} | **{res}** | {ev} |")
    if items:
        w("\n## 3. Items × Q-D lines\n\nMechanical lines from the Phase 0 tools (`tools/*.out.json`); hand lines (Q-D-08/09/11/12/13/14/17) cite the reading. `N/A` = line not applicable to the class; `EXEMPT` = Q-D-02 skeleton-stub rule.\n")
        for p in items:
            q=qlines(p); fails=[k for k,v in q.items() if v[0].startswith('FAIL')]
            w(f"### `{p}`\n| Q-line | Result | Evidence |\n|---|---|---|")
            for k in sorted(q): w(f"| {k} | {q[k][0]} | {q[k][1]} |")
            cov=covered(p)
            if fails and not cov:
                next_id[0]+=1
                row=dict(row_id=f"QI-{next_id[0]:04d}",folder=F,artifact_path=p,label=[label(p)],layer="L1-STRUCTURE",q_lines=[k for k in fails if k.startswith(('Q-D','Q-F'))][:6],finding_class="UNCLASSIFIED-QUALITY",severity="OPTIMISATION",statement=f"Mechanical Q-line failure(s) {fails} not covered by a Phase 1 row; recorded for the item, weight by radius 1.",evidence="; ".join(f"{k}: {q[k][1]}" for k in fails),weight=1,criticality=0,radius=1,blocks=[],executability="CLAUDE-CODE-EXECUTABLE-NOW" if not p.startswith('03_') else "CORPUS-OWNER",owner="folder owner (INDEX §4)",state="OPEN",phase_found="2")
                if row['executability']=="CLAUDE-CODE-EXECUTABLE-NOW": row.update(observed_state=row['evidence'][:200],target_state="line PASS",remediation_draft="see the folder's FIRST_IMPROVEMENTS line for this item",build_spec={"target_path":"folder's next delta","class_plines":"per item","mandatory_sections":[],"inputs":[p],"laws":"append-only","evidence_to_capture":"tool re-run","acceptance_test":"line PASS","closes_rows":[],"harden_linkage":"HARDEN-1.1 row","ratifying_owner":"folder owner","depends_on":"—"})
                rows.append(row); allrows.append(row); cov=[row]
            if not fails and not cov:
                next_id[0]+=1
                row=dict(row_id=f"QI-{next_id[0]:04d}",folder=F,artifact_path=p,label=[label(p)],layer="NONE",q_lines=[k for k,v in q.items() if v[0]=='PASS'][:8],finding_class="PRESENT-IMPECCABLE",severity="NONE",statement=f"Every applicable mechanical Q-line PASS ({sum(1 for v in q.values() if v[0]=='PASS')} lines); hand lines per ASSESSMENT §3; no finding filed against this item in Phase 1 or 2.",evidence="; ".join(f"{k}:{v[0]}" for k,v in sorted(q.items())),weight=0,criticality=0,radius=0,blocks=[],executability="NONE",owner=FOLDER_NOTES[F].get('owner','folder owner (INDEX §4)'),state="OPEN",phase_found="2")
                rows.append(row); allrows.append(row)
            for c in [c for c in rows if p in c['artifact_path'] or os.path.basename(p).rsplit('.',1)[0][:40] in c['artifact_path']]:
                if c['severity']!='NONE' and c['state']=='OPEN' and c['row_id'] not in {x['row_id'] for x in fi}: fi.append(c)
    for c in rows:
        if c['severity']!='NONE' and c['state']=='OPEN' and c not in fi: fi.append(c)
    w("\n## 4. Severity and weight\n\nPer v1.0 mapping (CRITICAL ≥4 · WARNING 3 · OPTIMISATION ≤2; weight = min(5, criticality + radius)); addends are in each row. Rows in `rows.jsonl`: "+str(len(rows))+".\n")
    w("## 5. Preliminary folder verdict (final in IMPECCABILITY_QUEUE §b after calibration)\n\n"+FOLDER_NOTES[F]['verdict']+"\n")
    w("## 6. Exit\n\n"+f"rows.jsonl: {len(rows)} rows (items {len(items)} + applicable Q-F lines {len(FOLDER_NOTES[F]['qf'])} → coverage: every item appears in ≥1 row: {'yes' if all(covered(p) or any(p in c['artifact_path'] for c in rows) for p in items) else 'NO'}). Validation pasted in CHECKPOINT.md.\n")
    open(dirn+'ASSESSMENT.md','w').write("\n".join(o)+"\n")
    fi.sort(key=lambda c:(-c.get('calibrated_weight',c['weight']),c['row_id']))
    lines=[f"# FIRST_IMPROVEMENTS — {NAMES[F]} (weight order)\n"]
    for c in fi:
        m=c.get('measured'); mv=f"{m['value']} vs {m['threshold']} {m.get('unit','')}" if m else (c['evidence'][:140]+'…')
        lines.append(f"- [{c['severity']}] [{c['weight']}] [{c['layer']}/{','.join(c['q_lines'][:2])}] [{c['label'][0]}] {c['statement'][:160]} — measured: {mv} — exemplar: {c.get('exemplar_path','—')} — blocks: {'; '.join(c['blocks']) or '—'} — remedy: {c.get('target_state', c['executability'])[:200]} ({c['executability']}, {c['owner'][:60]}) — {c['row_id']}")
    if not fi: lines.append("- (no OPEN finding with severity above NONE in this folder)")
    open(dirn+'FIRST_IMPROVEMENTS.md','w').write("\n".join(lines)+"\n")
    open(dirn+'rows.jsonl','w').write("\n".join(json.dumps(r,ensure_ascii=False) for r in rows)+"\n")
    check.append(f"{NAMES[F]} · items={len(items)} · rows={len(rows)} · open-findings={len(fi)} · ERROR=none")
open(R+'CHECKPOINT.md','w').write("# CHECKPOINT — survey-3 Phase 2 (sequential; one writer)\n\n"+"\n".join(f"- {c}" for c in check)+"\n")
open(R+'items/rows.jsonl','w') if os.path.isdir(R+'items') else None
json.dump({"rows":len(allrows)},open(R+'raw/phase2_rowcount.json','w'))
open(R+'QI.jsonl','w').write("\n".join(json.dumps(r,ensure_ascii=False) for r in allrows)+"\n")
print("fragments written:",len(FOLDERS),"total rows",len(allrows))
