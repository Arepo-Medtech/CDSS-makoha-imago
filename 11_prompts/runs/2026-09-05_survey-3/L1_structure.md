# L1_structure — Layer 1 census (structural integrity and graph topology)

Run 2026-09-05_survey-3 · Phase 1 step 1 · every number below is the named tool's output (`tools/*.out.json`, `tools/refcheck.out.txt`).

## 1. Depth (Q-D-03) — `tools/depth.py`

```
{
 "files": 271,
 "histogram": {
  "0": 5,
  "1": 127,
  "2": 43,
  "3": 43,
  "4": 53
 },
 "threshold": 4,
 "exceeding": []
}
```
Result: **0 files exceed four levels**; 53 sit at four (all `06_repositories/repo-skeletons/<repo>/<dir>/`). No DEPTH-EXCEEDED row.

## 2. Frontmatter schema (Q-D-04) — `tools/frontmatter.py`

- markdown files in scope: **194**; with frontmatter **110**; without **84**, classified by why: retained-original 22, corpus-companion 4, skeleton-banner 55, root-governance 3; omissions (a finding): **0** []
- retained-original 22 = the 21 CDSS originals in 02_ + MT2 (frontmatter cannot be added in place — law 1); skeleton-banner 55 = 06_ stubs (banner in lieu, survey-2 rule); corpus-companion 4 = 03_ MANIFEST, briefing, RUN-REPORT, programme prompt; root-governance 3 = README.md, AGENTS.md, CLAUDE.md.
- core-key gaps on frontmatter-bearing files: **11** →
  - `00_MANIFEST.md` missing ['version']
  - `05_registers-and-contracts/CONTRACT-ARG-1_argument_schema.md` missing ['version', 'date']
  - `05_registers-and-contracts/REG-R29_hardening_coverage_ledger.schema.md` missing ['version', 'date']
  - `05_registers-and-contracts/REG-R30_regulatory_posture_register.schema+seed.md` missing ['version', 'date']
  - `06_repositories/REPO-MAP_v2.md` missing ['version', 'date']
  - `07_deployment-and-operations/DEPLOY-1_deployment_plan_and_sequencing.md` missing ['date']
  - `07_deployment-and-operations/DEPLOY-2_testing_verification_acceptance.md` missing ['date']
  - `07_deployment-and-operations/GOV-1_ownership_governance_postdeploy.md` missing ['date']
  - `07_deployment-and-operations/OPS-1_operating_procedures.md` missing ['date']
  - `07_deployment-and-operations/SEC-1_security_privacy_compliance.md` missing ['date']
  - `08_research/RESEARCH-1_findings_gaps_source_map.md` missing ['status']
- date-field variants: {'date': 93, 'date_issued': 8, 'guidance_currency_date': 6} (three spellings for one concept — Layer 4 FORM-DEVIATION candidate; REG-* files declare `date_issued` + `guidance_currency_date` deliberately as two dates)
- doc_id repeats (Q-D-05): {"REG-NZ": {"files": ["10_regulatory-execution/REG-NZ_v1.0.md", "10_regulatory-execution/REG-NZ_v1.1.md"], "all_but_one_carry_supersedes": true}, "REG-POSTURE": {"files": ["10_regulatory-execution/REG-POSTURE_v1.1.md", "10_regulatory-execution/REG-POSTURE_v1.2.md"], "all_but_one_carry_supersedes": true}} — both repeats are version chains where the later file carries `supersedes:`; **no written rule** says a superseded file keeps its doc_id (v1.0 open question 4) → one ID-SUPERSESSION-RULE-ABSENT row at CHAIN level.
- files minting ≥3 IDs of a family without a `req_prefix(es)`/`id_prefixes` declaration: **23** →
  - `00_MANIFEST.md` — families ['DEF'] (7 mints)
  - `01_north-star-and-transformation/MET-1_metamorphosis_plan_v1.0.md` — families ['C', 'DEC', 'G'] (30 mints)
  - `01_north-star-and-transformation/MET-2.1_decision_register_delta.md` — families ['C', 'DEC'] (14 mints)
  - `01_north-star-and-transformation/MET-2_conflict_and_decision_register.md` — families ['C', 'DEC'] (24 mints)
  - `01_north-star-and-transformation/MET-3_traceability_map.md` — families ['FZ', 'GPP', 'SPINE'] (8 mints)
  - `01_north-star-and-transformation/MET-4_gap_analysis_and_roadmap.md` — families ['G'] (11 mints)
  - `03_makoha-butterfly-corpus/butterfly-primers/primer_ABC_auditor_face.md` — families ['AE', 'AG', 'AL', 'AR', 'AT', 'AX', 'RECON-ABC'] (13 mints)
  - `03_makoha-butterfly-corpus/butterfly-primers/primer_ANT_regulatory_sensing.md` — families ['AN', 'RECON-ANT', 'W'] (12 mints)
  - `03_makoha-butterfly-corpus/butterfly-primers/primer_CEC_engines.md` — families ['AD', 'CP', 'DX', 'GPP', 'OM', 'QU', 'RECON-CEC', 'RG'] (16 mints)
  - `03_makoha-butterfly-corpus/butterfly-primers/primer_HDC_clinician_face.md` — families ['HA', 'HE', 'HG', 'HR', 'HT', 'HW', 'RECON-HDC'] (13 mints)
  - `03_makoha-butterfly-corpus/butterfly-primers/primer_LBP_clinician_ui.md` — families ['CA', 'CC', 'CI', 'CS', 'CV', 'RECON-LBP'] (12 mints)
  - `03_makoha-butterfly-corpus/butterfly-primers/primer_LEG_stack.md` — families ['L1', 'L2', 'L3', 'L4', 'L5', 'L6', 'LS', 'RECON-LEG'] (15 mints)
  - `03_makoha-butterfly-corpus/butterfly-primers/primer_LWC_fuzzy_spine.md` — families ['FA', 'FC', 'FE', 'FP', 'FS', 'FX', 'RECON-LWC'] (12 mints)
  - `03_makoha-butterfly-corpus/butterfly-primers/primer_PRB_patient_ui.md` — families ['PA', 'PC', 'PI', 'PS', 'PV', 'RECON-PRB'] (12 mints)
  - `03_makoha-butterfly-corpus/butterfly-primers/primer_RWC_meta_rationality.md` — families ['MA', 'MC', 'ME', 'MP', 'MS', 'MX', 'RECON-RWC'] (14 mints)
  - `03_makoha-butterfly-corpus/butterfly-primers/primer_TXC_patient_face.md` — families ['RECON-TXC', 'TA', 'TC', 'TE', 'TL', 'TR', 'TW'] (13 mints)
  - `03_makoha-butterfly-corpus/corpus-md/execution-layer-sourcing-map_v1.1.md` — families ['ELSM'] (10 mints)
  - `04_hardening/HARDEN-2_hardening_spec.md` — families ['CC'] (8 mints)
  - `08_research/RESEARCH-1_findings_gaps_source_map.md` — families ['RG'] (6 mints)
  - `11_prompts/PROMPT-SURVEY-1_ecosystem_repleteness_surveyor.md` — families ['E', 'P', 'T'] (26 mints)
  - `11_prompts/PROMPT-SURVEY-3.1_deep-review_fold_delta.md` — families ['D', 'M', 'T'] (24 mints)
  - `11_prompts/PROMPT-SURVEY-3.2_confidence_erratum_delta.md` — families ['E'] (3 mints)
  - `11_prompts/PROMPT-SURVEY-3_final-quality-improvement.md` — families ['A', 'E', 'P', 'T'] (35 mints)
  Classification: delta-item / eval-case / amendment labels (`D-n`, `E-n`, `A-nn`, `M-n`, `P-nn`, `T-nn` in prompts, `DEF-nnn`) are not requirement families and are **not** findings; `C`/`DEC`/`G` (MET-1/2/2.1/4), `CC` (HARDEN-2), `RG` (RESEARCH-1), `ELSM`, the ten butterfly-primer families and `RECON-*` **are** requirement-bearing families minted without declaration → ID-LIFECYCLE-GAP rows in L2.
- heading-ladder skips (Q-D-07): [['01_north-star-and-transformation/MET-1_metamorphosis_plan_v1.0.md', 1], ['03_makoha-butterfly-corpus/butterfly-primers/primer_0_butterfly_explainer.md', 1]] — both retained/corpus files (MET-1 v1.0; butterfly primer 0) → remedy is a companion note, weight ≤ 2.
- tables with inconsistent column counts (Q-D-07): **0** (after excluding escaped pipes and code spans).

## 3. Reference integrity (Q-D-06) — `tools/refcheck.py` (copy of `.github/audit/refcheck.py`)
```
## Reference check

- dead in-repo paths: 0; unresolved anchors: 0 (the two carried v2 `MT2 §7.4` defects excluded — DEF-003); external refs: 55; globs/placeholders: 91; prompt-declared future outputs: 608; doc-id shorthand: 3
```
Result: **0 dead in-repo paths, 0 unresolved anchors**; 55 external, 91 glob/placeholder, 608 prompt-declared future outputs, 3 doc-id shorthand — classified, not dead.

## 4. Design-graph reachability and orphans (Q-D-01, Q-D-02) — `tools/graph.py`

- files: 271; reachable from README → 00_MANIFEST → INDEX → file: **271/271** (0 unreachable — Q-D-01 parent test PASS for every file)
- inbound-edge classes: {'DESIGN-LINKED': 174, 'LEDGER-OR-INDEX-ONLY': 97} (edges = full path, unique basename, frontmatter `doc_id`, or the prompt's short name e.g. `PROMPT-A`)
- design-graph orphans (inbound only from the ledger, the task register, an INDEX table or the manifest): **97** → by folder {'05_registers-and-contracts': 3, '06_repositories': 90, '10_regulatory-execution': 2, '11_prompts': 2}
  - `06_repositories` ×90: skeleton stubs whose only parent is INDEX-06 §3 + HARDEN rows — **exempt** under Q-D-02 (a stub's reader is the instantiating primer; the primer names the *tree*, not each stub) → recorded, no row per file; one folder-level PRESENT-IMPECCABLE note.
  - `05_registers-and-contracts/CONTRACT-DEV-1.examples.jsonl` — ORPHAN-IN-DESIGN-GRAPH candidate (Phase 2 confirms by reading: is it cited by any non-index document under its doc_id or title?)
  - `05_registers-and-contracts/CONTRACT-DEV-1.schema.json` — ORPHAN-IN-DESIGN-GRAPH candidate (Phase 2 confirms by reading: is it cited by any non-index document under its doc_id or title?)
  - `05_registers-and-contracts/REG-R29.1_schema_twin_delta.md` — ORPHAN-IN-DESIGN-GRAPH candidate (Phase 2 confirms by reading: is it cited by any non-index document under its doc_id or title?)
  - `10_regulatory-execution/REG-POSTURE_v1.2_CONTENTS.md` — ORPHAN-IN-DESIGN-GRAPH candidate (Phase 2 confirms by reading: is it cited by any non-index document under its doc_id or title?)
  - `10_regulatory-execution/REG-SPRINT-1.2_census_delta.md` — ORPHAN-IN-DESIGN-GRAPH candidate (Phase 2 confirms by reading: is it cited by any non-index document under its doc_id or title?)
  - `11_prompts/PROMPT-FOLD-1_antennae_v1.2_fold.md` — ORPHAN-IN-DESIGN-GRAPH candidate (Phase 2 confirms by reading: is it cited by any non-index document under its doc_id or title?)
  - `11_prompts/PROMPT-PRM-SERIES_index.md` — ORPHAN-IN-DESIGN-GRAPH candidate (Phase 2 confirms by reading: is it cited by any non-index document under its doc_id or title?)

## 5. Layer 1 summary

| Q-line | Applicable files | PASS | FAIL | Notes |
|---|---|---|---|---|
| Q-D-01 parent | 271 | 271 | 0 | every file reachable |
| Q-D-02 bidirectional | 181 (06_ stubs exempt) | 174 | 7 | candidates listed above |
| Q-D-03 depth | 271 | 271 | 0 | — |
| Q-D-04 frontmatter core | 110 | 99 | 11 | retained/skeleton/companion judged elsewhere |
| Q-D-05 doc_id unique | 110 | 106 | 4 (2 chains) | rule absent → 1 CHAIN row |
| Q-D-06 references | 271 | 271 | 0 | — |
| Q-D-07 tables/ladders | 110 | 108 | 2 | retained files; companion note |
