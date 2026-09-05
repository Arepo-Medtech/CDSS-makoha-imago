#!/usr/bin/env python3
"""HARDEN-1.1 generator: one path-resolving row per artifact in the tree (excl. .DS_Store, .git, 11_prompts/runs, .playwright-mcp).
Emits 04_hardening/HARDEN-1.1_coverage_ledger_seed_delta.md and a JSON sidecar for HARDEN-3.1 / INDEX generators. Run from repo root.
PLANNED paths (files this sprint creates after the ledger) are included and verified present at the end of the sprint (acceptance test)."""
import os, json, subprocess, re, sys, hashlib
RUN="11_prompts/runs/2026-09-05_sprint-1"
tracked=set(subprocess.check_output(['git','ls-files']).decode().split('\n'))-{''}
untracked=set(subprocess.check_output(['git','ls-files','--others','--exclude-standard']).decode().split('\n'))-{''}
files=sorted(p for p in tracked|untracked if not p.startswith(('11_prompts/runs/','.playwright-mcp/')) and not p.endswith('.DS_Store') and os.path.isfile(p))
PLANNED=["04_hardening/HARDEN-1.1_coverage_ledger_seed_delta.md","04_hardening/HARDEN-2.1_spec_census_and_self-audit_delta.md","04_hardening/HARDEN-3.1_task_register_delta.md",
 "04_hardening/INDEX.md","05_registers-and-contracts/INDEX.md","06_repositories/INDEX.md","07_deployment-and-operations/INDEX.md","08_research/INDEX.md","09_diagrams/INDEX.md","10_regulatory-execution/INDEX.md"]
allfiles=sorted(set(files)|set(PLANNED))
# ---- v1.0 row resolution (D-0): row id -> paths
V2="02_cdss-stack-augmented/"; V3="03_makoha-butterfly-corpus/"
res={0:["(engine) addyosmani/agent-skills whole-pack install — no path in tree"],
 1:["05_registers-and-contracts/CONTRACT-ARG-1_argument_schema.md"],2:["05_registers-and-contracts/CONTRACT-ARG-1_argument_schema.md"],3:["05_registers-and-contracts/CONTRACT-ARG-1_argument_schema.md"],
 4:["05_registers-and-contracts/REG-R29.schema.json","05_registers-and-contracts/REG-R29_hardening_coverage_ledger.schema.md"],5:["05_registers-and-contracts/REG-R30_regulatory_posture_register.schema+seed.md"],
 6:[V3+"corpus-md/four-faces-corpus_v1.1.md"],7:[V3+"MANIFEST.md"],8:[V3+"corpus-md/antennae-corpus_v1.0.md"],9:[V2+"architecture_and_integration.md"],10:[V2+"primer_0_ecosystem_explainer.md"],
 27:[V2+"ecosystem_integration_report.md"],41:[V2+"cdss_complete_stack.md"],42:[V2+"cdss_diagrams.html"],43:["09_diagrams/cdss_diagrams_v2.html"],
 72:["(corpus) corpus-side artifacts — in-account only; no path in tree"],73:["(external) HeyDoc instruction-bearing files — Arepo-Medtech/Makoha below-README [NEEDS SOURCE]"]}
for i,n in enumerate("ABCDEFGHIJKL"):
    names={"A":"primer_A_bayesian_engine.md","B":"primer_B_evidence_library.md","C":"primer_C_casebundle_corpus.md","D":"primer_D_content_registry.md","E":"primer_E_graph_rag.md","F":"primer_F_conformal_wrapper.md","G":"primer_G_corruption_engine.md","H":"primer_H_lumos_pathway.md","I":"primer_I_living_evaluation.md","J":"primer_J_model_governance.md","K":"primer_K_llm_augmentation.md","L":"primer_L_runtime_llm.md"}
    res[11+i]=[V2+names[n]]
res[23]=[V2+"variant_1b_deterministic_coder.md"];res[24]=[V2+"variant_2_ml_coder_runtime.md"];res[25]=[V2+"harness_ml_primer.md"];res[26]=[V2+"grounding_and_weak_supervision.md"]
vols=["makoha-in-flight_v1.0.md","degrees-of-truth_v1.0.md","left-wing-corpus_v1.1.md","right-wing-corpus_v1.1.md","compound-eyes-corpus_v1.1.md","head-corpus_v1.0.md","thorax-corpus_v1.0.md","abdomen-corpus_v1.0.md","proboscis-corpus_v1.0.md","labial-palps-corpus_v1.0.md","legs-corpus_v1.0.md","execution-layer-sourcing-map_v1.1.md","addendum-j3-guideline-prompt-profile_v0.9.md"]
for i,v in enumerate(vols): res[28+i]=[V3+"corpus-md/"+v]
html=sorted(p for p in files if p.startswith(V3+"artifacts-html/"))
assert len(html)==16, len(html)
for i,h in enumerate(html): res[44+i]=[h]
# D-1: rows 60–71 retained ids → 12 of the 21 collapsed artifacts
d1={60:"01_north-star-and-transformation/MET-1_metamorphosis_plan_v1.0.md",61:"01_north-star-and-transformation/MET-1.1_metamorphosis_plan_delta.md",62:"01_north-star-and-transformation/MET-2_conflict_and_decision_register.md",63:"01_north-star-and-transformation/MET-3_traceability_map.md",64:"01_north-star-and-transformation/MET-4_gap_analysis_and_roadmap.md",
    65:"04_hardening/MAJOR_TASK_2_anti-laziness-hardening-directive.md",66:"04_hardening/HARDEN-2_hardening_spec.md",67:"04_hardening/HARDEN-3_hardening_plan_worklist.md",68:"04_hardening/HARDEN-1_coverage_ledger_seed.md",
    69:"06_repositories/REPO-MAP_v2.md",70:"00_MANIFEST.md",71:"07_deployment-and-operations/DEPLOY-1_deployment_plan_and_sequencing.md"}
covered=set(p for v in res.values() for p in v if not p.startswith('('))|set(d1.values())
# ---- class + owner rules
def cls(p):
    b=os.path.basename(p)
    if p.startswith('.github/') or p=='.gitignore': return 'CC-5'
    if p in ('00_inventory.txt','README.md'): return 'CC-8'
    if p.startswith('01_'): return 'CC-8'
    if p.startswith('02_'): return 'CC-1'
    if p.startswith(V3+'butterfly-primers/primer_'): return 'CC-1'
    if p.startswith(V3+'butterfly-primers/RUN-REPORT') or 'programme_prompt' in p: return 'CC-8'
    if p.startswith(V3+'corpus_artifacts_briefing'): return 'CC-3'
    if p.startswith(V3+'corpus-md/') or p==V3+'MANIFEST.md': return 'CC-3'
    if p.startswith(V3+'artifacts-html/'): return 'CC-6'
    if p==V2+'cdss_diagrams.html': return 'CC-6'
    if p.startswith('04_'): return 'CC-8'
    if p.startswith('05_'):
        if b.startswith('CONTRACT'): return 'CC-7'
        if b.startswith('REG-R30'): return 'CC-4'
        if b=='INDEX.md': return 'CC-8'
        return 'CC-2'
    if p.startswith('06_'):
        if b=='INDEX.md': return 'CC-8'
        if b in ('CODEOWNERS',) or b.endswith('.pointer.md'): return 'CC-2'
        return 'CC-5'
    if p.startswith('07_'): return 'CC-8' if b=='INDEX.md' else 'CC-5'
    if p.startswith('08_'): return 'CC-8'
    if p.startswith('09_'): return 'CC-8' if b=='INDEX.md' else 'CC-6'
    if p.startswith('10_'):
        if b=='INDEX.md' or b.startswith('EXEC-1'): return 'CC-8'
        if b.startswith('FOLD-1') or b.endswith('.py'): return 'CC-5'
        return 'CC-4'
    if p.startswith('11_'): return 'CC-8'
    return 'CC-8'
def owner(p):
    if p.startswith(('00_','01_','README','.git')): return 'Manifest owner [NEEDS DEFINITION]'
    if p.startswith('02_'): return 'Component owner per primer repo [NEEDS DEFINITION — DEC-09]'
    if p.startswith('03_'): return 'Corpus owner (03_ MANIFEST precedence) [NEEDS DEFINITION]'
    if p.startswith('04_'): return 'MT2 operator (DEC-10) [NEEDS DEFINITION]'
    if p.startswith('05_'): return 'Architecture owner (DEC-02) / cdss-spine; R30 rows: cdss-governance'
    if p.startswith('06_'): return 'Repo owner per REPO-MAP (DEC-09) [NEEDS DEFINITION]'
    if p.startswith('07_'): return 'Operations / security / regulatory owner [NEEDS DEFINITION — G-09]'
    if p.startswith('08_'): return 'Research author; RG owners per RESEARCH-1 §3'
    if p.startswith('09_'): return 'Architecture owner'
    if p.startswith('10_'): return 'Regulatory owner [NEEDS DEFINITION — G-09 / REG-POSTURE §12.3]'
    if p.startswith('11_'): return 'MT2 operator (DEC-10) / prompt author [NEEDS DEFINITION]'
    return '[NEEDS DEFINITION]'
def note(p):
    if p in PLANNED: return 'sprint-1 artifact (built 2026-09-05)'
    if p in untracked: return 'sprint-1 artifact (built 2026-09-05)'
    if p.startswith('06_repositories/repo-skeletons/'): return 'A-001 glob row, enumerated'
    if p.startswith('10_'): return 'no v1.0 row (survey-2 BSQ-0703)'
    if p.startswith('11_'): return 'no v1.0 row (survey-2 BSQ-0104)'
    return ''
rows=[]  # (row_id, path, class, state, owner, note, origin)
for rid in sorted(res):
    for p in res[rid]: rows.append(dict(row=rid,path=p,cls=None,origin='v1.0 (D-0 resolution)'))
for rid,p in d1.items(): rows.append(dict(row=rid,path=p,cls=None,origin='v1.0 rows 60–71 (D-1 retained id)'))
nid=74
for p in allfiles:
    if p in covered: continue
    rows.append(dict(row=nid,path=p,cls=None,origin='D-2 new row')); nid+=1
for r in rows:
    r['cls']= {0:'engine',72:'corpus',73:'external'}.get(r['row']) or cls(r['path'])
    r['owner']=owner(r['path']) if not r['path'].startswith('(') else ('MT2 operator (DEC-10)' if r['row']==0 else ('Corpus custodian (DEC-12)' if r['row']==72 else 'DEC-12 executor'))
    r['state']={0:'BLOCKED (pre-pass placeholder)',72:'ESCALATED-placeholder',73:'PENDING-ENUMERATION'}.get(r['row'],'PENDING')
    r['note']=note(r['path']) if not r['path'].startswith('(') else 'no path — v1.0 row carried as-is'
    r['exists']=os.path.isfile(r['path']) if not r['path'].startswith('(') else None
    r['bytes']=os.path.getsize(r['path']) if r['exists'] else None
# acceptance: set equality
ledger_paths=set(r['path'] for r in rows if not r['path'].startswith('('))
missing=sorted(set(allfiles)-ledger_paths); extra=sorted(ledger_paths-set(allfiles))
byclass={}
for r in rows: byclass[r['cls']]=byclass.get(r['cls'],0)+1
json.dump(dict(rows=rows,allfiles=allfiles,planned=PLANNED,missing=missing,extra=extra,byclass=byclass),open(f"{RUN}/ledger_rows.json","w"),indent=1)
print("files in tree (incl. planned):",len(allfiles),"| ledger rows:",len(rows),"| distinct paths:",len(ledger_paths),"| missing:",len(missing),"| extra:",len(extra))
print("by class:",json.dumps(byclass))
print("planned not yet on disk:",[p for p in PLANNED if not os.path.isfile(p)])
