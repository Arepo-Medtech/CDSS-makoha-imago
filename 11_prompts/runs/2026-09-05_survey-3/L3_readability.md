# L3_readability — Layer 3 census (Q-D-15) — `tools/readability.py`

Formula: FK grade = 0.39*ASL + 11.8*ASW - 15.59; prose only. Syllables by vowel-group heuristic (stated; not a dictionary). Files scored: **154/194** (files under 50 prose words not scored). Median ASL **22.1** words; median FK grade **13.2**. Thresholds `[ASSESSOR-PROPOSED]`: primary ASL ≤ 35; FK reported, flagged only with ASL (see QUALITY_STANDARD threshold policy).

## Files over the ASL threshold (READABILITY-DENSE candidates): 9

| File | prose words | sentences | ASL | FK | Class → remedy |
|---|---|---|---|---|---|
| `07_deployment-and-operations/SEC-1_security_privacy_compliance.md` | 244 | 3 | **81.3** | 40.4 | companion/delta |
| `06_repositories/REPO-MAP_v2.md` | 202 | 3 | **67.3** | 32.6 | companion/delta |
| `05_registers-and-contracts/REG-R30.1_seed_delta.md` | 199 | 3 | **66.3** | 27.4 | companion/delta |
| `07_deployment-and-operations/GOV-1_ownership_governance_postdeploy.md` | 173 | 3 | **57.7** | 29.6 | companion/delta |
| `05_registers-and-contracts/REG-R29_hardening_coverage_ledger.schema.md` | 101 | 2 | **50.5** | 22.3 | companion/delta |
| `05_registers-and-contracts/CONTRACT-ARG-1_argument_schema.md` | 156 | 4 | **39.0** | 26.2 | companion/delta |
| `11_prompts/PROMPT-SURVEY-3.2_confidence_erratum_delta.md` | 657 | 17 | **38.6** | 16.7 | companion/delta |
| `05_registers-and-contracts/REG-R30_regulatory_posture_register.schema+seed.md` | 115 | 3 | **38.3** | 15.4 | companion/delta |
| `04_hardening/HARDEN-3.1_task_register_delta.md` | 264 | 7 | **37.7** | 16.9 | companion/delta |

Note on the v1.0 seeds: the survey-authoring method (2 Sep) measured MET-2 ≈ 102 and HARDEN-3 ≈ 51 by counting table-cell prose; this tool strips tables, so MET-2 (register, almost all table) falls below 50 prose words and is not scored — the finding for register-style documents is FORM (Layer 4), not readability. SEC-1 (81.3) and GOV-1 (57.7) are confirmed dense by both methods.

## Exemplars (ASL ≤ 22, ≥ 500 prose words)

- `10_regulatory-execution/REG-SPRINT-1.1_delta.md` ASL 22.0 FK 13.2 (551 words)
- `11_prompts/PROMPT-PRM0_butterfly_primer0_launch.md` ASL 22.0 FK 10.8 (925 words)
- `02_cdss-stack-augmented/primer_0_ecosystem_explainer.md` ASL 21.9 FK 13.6 (2040 words)
- `03_makoha-butterfly-corpus/corpus-md/head-corpus_v1.0.md` ASL 21.7 FK 14.6 (3521 words)
- `02_cdss-stack-augmented/primer_D_content_registry.md` ASL 21.4 FK 15.1 (1091 words)
- `03_makoha-butterfly-corpus/corpus-md/addendum-j3-guideline-prompt-profile_v0.9.md` ASL 21.3 FK 16.7 (1896 words)
- `03_makoha-butterfly-corpus/corpus-md/left-wing-corpus_v1.1.md` ASL 21.3 FK 15.2 (5434 words)
- `02_cdss-stack-augmented/harness_ml_primer.md` ASL 21.2 FK 15.6 (2376 words)
- `11_prompts/PROMPT-SURVEY-3_final-quality-improvement.md` ASL 21.1 FK 11.7 (972 words)
- `02_cdss-stack-augmented/primer_C_casebundle_corpus.md` ASL 21.0 FK 15.4 (1342 words)
- `03_makoha-butterfly-corpus/corpus-md/four-faces-corpus_v1.1.md` ASL 20.8 FK 16.1 (7311 words)
- `11_prompts/PROMPT-SURVEY-2_folder-parity_build-spec-queue.md` ASL 20.7 FK 9.8 (1034 words)

## Full table (scored files, ASL descending)

| File | words | ASL | FK |
|---|---|---|---|
| `07_deployment-and-operations/SEC-1_security_privacy_compliance.md` | 244 | 81.3 | 40.4 |
| `06_repositories/REPO-MAP_v2.md` | 202 | 67.3 | 32.6 |
| `05_registers-and-contracts/REG-R30.1_seed_delta.md` | 199 | 66.3 | 27.4 |
| `07_deployment-and-operations/GOV-1_ownership_governance_postdeploy.md` | 173 | 57.7 | 29.6 |
| `05_registers-and-contracts/REG-R29_hardening_coverage_ledger.schema.md` | 101 | 50.5 | 22.3 |
| `05_registers-and-contracts/CONTRACT-ARG-1_argument_schema.md` | 156 | 39.0 | 26.2 |
| `11_prompts/PROMPT-SURVEY-3.2_confidence_erratum_delta.md` | 657 | 38.6 | 16.7 |
| `05_registers-and-contracts/REG-R30_regulatory_posture_register.schema+seed.md` | 115 | 38.3 | 15.4 |
| `04_hardening/HARDEN-3.1_task_register_delta.md` | 264 | 37.7 | 16.9 |
| `00_MANIFEST.md` | 2218 | 33.6 | 16.6 |
| `01_north-star-and-transformation/MET-1_metamorphosis_plan_v1.0.md` | 3614 | 33.2 | 19.6 |
| `01_north-star-and-transformation/MET-4_gap_analysis_and_roadmap.md` | 130 | 32.5 | 14.3 |
| `04_hardening/HARDEN-2_hardening_spec.md` | 161 | 32.2 | 20.4 |
| `06_repositories/repo-skeletons/cdss-spine/contracts/README.md` | 63 | 31.5 | 20.3 |
| `06_repositories/repo-skeletons/cdss-spine/README.md` | 93 | 31.0 | 17.6 |
| `08_research/RESEARCH-1_findings_gaps_source_map.md` | 93 | 31.0 | 20.9 |
| `05_registers-and-contracts/REG-R30.2_seed_delta.md` | 512 | 30.1 | 13.0 |
| `01_north-star-and-transformation/MET-1.1_metamorphosis_plan_delta.md` | 89 | 29.7 | 18.7 |
| `06_repositories/repo-skeletons/cdss-evalstack/README.md` | 88 | 29.3 | 15.3 |
| `06_repositories/INDEX.md` | 435 | 29.0 | 14.4 |
| `03_makoha-butterfly-corpus/butterfly-primers/primer_CEC_engines.md` | 7404 | 28.6 | 16.0 |
| `11_prompts/PROMPT-PRM-SERIES_index.md` | 1539 | 28.0 | 13.3 |
| `11_prompts/PROMPT-SERIES_A-L_index.md` | 700 | 28.0 | 13.6 |
| `02_cdss-stack-augmented/variant_2_ml_coder_runtime.md` | 835 | 27.8 | 18.1 |
| `04_hardening/HARDEN-1.1_coverage_ledger_seed_delta.md` | 386 | 27.6 | 12.4 |
| `10_regulatory-execution/INDEX.md` | 523 | 27.5 | 13.6 |
| `03_makoha-butterfly-corpus/corpus-md/execution-layer-sourcing-map_v1.1.md` | 1641 | 27.4 | 18.2 |
| `03_makoha-butterfly-corpus/butterfly-primers/primer_LBP_clinician_ui.md` | 6101 | 27.0 | 14.5 |
| `02_cdss-stack-augmented/primer_K_llm_augmentation.md` | 1638 | 26.9 | 17.5 |
| `03_makoha-butterfly-corpus/butterfly-primers/primer_HDC_clinician_face.md` | 6127 | 26.9 | 15.0 |
| `02_cdss-stack-augmented/primer_I_living_evaluation.md` | 1878 | 26.8 | 17.2 |
| `03_makoha-butterfly-corpus/butterfly-primers/primer_TXC_patient_face.md` | 6218 | 26.8 | 15.4 |
| `11_prompts/PROMPT-PRM-LWC_fuzzy_spine_launch.md` | 692 | 26.6 | 13.1 |
| `03_makoha-butterfly-corpus/butterfly-primers/RUN-REPORT.md` | 4440 | 26.4 | 14.2 |
| `11_prompts/PROMPT-FOLD-1_antennae_v1.2_fold.md` | 264 | 26.4 | 11.6 |
| `11_prompts/PROMPT-PRM-ABC_auditor_face_launch.md` | 553 | 26.3 | 14.7 |
| `05_registers-and-contracts/INDEX.md` | 420 | 26.2 | 11.8 |
| `08_research/INDEX.md` | 210 | 26.2 | 11.7 |
| `02_cdss-stack-augmented/architecture_and_integration.md` | 3528 | 26.1 | 16.8 |
| `03_makoha-butterfly-corpus/butterfly-primers/primer_LEG_stack.md` | 6243 | 26.0 | 14.9 |
| `03_makoha-butterfly-corpus/butterfly-primers/primer_RWC_meta_rationality.md` | 6293 | 26.0 | 15.7 |
| `04_hardening/HARDEN-2.1_spec_census_and_self-audit_delta.md` | 181 | 25.9 | 12.5 |
| `07_deployment-and-operations/INDEX.md` | 310 | 25.8 | 12.5 |
| `03_makoha-butterfly-corpus/butterfly-primers/primer_PRB_patient_ui.md` | 6000 | 25.5 | 14.0 |
| `06_repositories/repo-skeletons/cdss-fabric/README.md` | 102 | 25.5 | 20.3 |
| `03_makoha-butterfly-corpus/butterfly-primers/primer_ABC_auditor_face.md` | 6270 | 25.4 | 14.9 |
| `02_cdss-stack-augmented/primer_J_model_governance.md` | 1987 | 25.2 | 16.7 |
| `03_makoha-butterfly-corpus/corpus-md/abdomen-corpus_v1.0.md` | 3565 | 25.1 | 16.4 |
| `03_makoha-butterfly-corpus/corpus-md/degrees-of-truth_v1.0.md` | 2053 | 25.0 | 16.7 |
| `02_cdss-stack-augmented/grounding_and_weak_supervision.md` | 2353 | 24.8 | 14.7 |
| `02_cdss-stack-augmented/primer_F_conformal_wrapper.md` | 1242 | 24.8 | 17.0 |
| `02_cdss-stack-augmented/variant_1b_deterministic_coder.md` | 918 | 24.8 | 16.8 |
| `07_deployment-and-operations/OPS-1_operating_procedures.md` | 297 | 24.8 | 16.0 |
| `02_cdss-stack-augmented/primer_L_runtime_llm.md` | 2001 | 24.7 | 16.8 |
| `03_makoha-butterfly-corpus/corpus-md/compound-eyes-corpus_v1.1.md` | 5181 | 24.7 | 16.2 |
| `07_deployment-and-operations/DEPLOY-1.1_run-map_delta.md` | 315 | 24.2 | 10.5 |
| `03_makoha-butterfly-corpus/corpus-md/legs-corpus_v1.0.md` | 2582 | 24.1 | 15.7 |
| `02_cdss-stack-augmented/primer_E_graph_rag.md` | 1264 | 23.8 | 17.0 |
| `11_prompts/PROMPT-PRM-LEG_stack_launch.md` | 571 | 23.8 | 10.6 |
| `02_cdss-stack-augmented/cdss_complete_stack.md` | 28586 | 23.7 | 15.9 |
| `03_makoha-butterfly-corpus/butterfly-primers/primer_ANT_regulatory_sensing.md` | 5374 | 23.7 | 13.2 |
| `11_prompts/PROMPT-PRM-RWC_meta_rationality_launch.md` | 470 | 23.5 | 12.6 |
| `03_makoha-butterfly-corpus/corpus-md/proboscis-corpus_v1.0.md` | 2298 | 23.4 | 15.1 |
| `03_makoha-butterfly-corpus/corpus-md/labial-palps-corpus_v1.0.md` | 2371 | 23.2 | 14.9 |
| `11_prompts/PROMPT-SURVEY-1_ecosystem_repleteness_surveyor.md` | 975 | 23.2 | 11.8 |
| `10_regulatory-execution/REG-US_v1.0.md` | 1246 | 23.1 | 14.2 |
| `02_cdss-stack-augmented/primer_H_lumos_pathway.md` | 1887 | 23.0 | 16.3 |
| `03_makoha-butterfly-corpus/corpus-md/right-wing-corpus_v1.1.md` | 7348 | 23.0 | 16.4 |
| `02_cdss-stack-augmented/primer_G_corruption_engine.md` | 1235 | 22.9 | 15.6 |
| `03_makoha-butterfly-corpus/corpus-md/thorax-corpus_v1.0.md` | 3428 | 22.7 | 15.0 |
| `11_prompts/PROMPT-HARDEN_mt2_pass_launch.md` | 227 | 22.7 | 10.2 |
| `04_hardening/INDEX.md` | 407 | 22.6 | 10.7 |
| `11_prompts/PROMPT-SURVEY-3.1_deep-review_fold_delta.md` | 2104 | 22.6 | 10.9 |
| `10_regulatory-execution/REG-SPRINT-1.2_census_delta.md` | 225 | 22.5 | 9.6 |
| `03_makoha-butterfly-corpus/butterfly-primers/primer_0_butterfly_explainer.md` | 3559 | 22.4 | 12.8 |
| `11_prompts/PROMPT-L_runtime_llm_launch.md` | 245 | 22.3 | 12.9 |
| `02_cdss-stack-augmented/primer_B_evidence_library.md` | 1282 | 22.1 | 15.0 |
| `10_regulatory-execution/REG-SPRINT-1.1_delta.md` | 551 | 22.0 | 13.2 |
| `11_prompts/PROMPT-PRM0_butterfly_primer0_launch.md` | 925 | 22.0 | 10.8 |
| `02_cdss-stack-augmented/primer_0_ecosystem_explainer.md` | 2040 | 21.9 | 13.6 |
| `03_makoha-butterfly-corpus/corpus-md/head-corpus_v1.0.md` | 3521 | 21.7 | 14.6 |
| `03_makoha-butterfly-corpus/corpus_artifacts_briefing.md` | 456 | 21.7 | 11.6 |
| `07_deployment-and-operations/SEC-2_threat-model_and_data-flow.md` | 345 | 21.6 | 11.7 |
| `11_prompts/PROMPT-K_llm_augmentation_launch.md` | 238 | 21.6 | 14.5 |
| `06_repositories/repo-skeletons/cdss-compiler/README.md` | 86 | 21.5 | 19.3 |
| `07_deployment-and-operations/DEPLOY-1_deployment_plan_and_sequencing.md` | 86 | 21.5 | 14.1 |
| `02_cdss-stack-augmented/primer_D_content_registry.md` | 1091 | 21.4 | 15.1 |
| `03_makoha-butterfly-corpus/corpus-md/addendum-j3-guideline-prompt-profile_v0.9.md` | 1896 | 21.3 | 16.7 |
| `03_makoha-butterfly-corpus/corpus-md/left-wing-corpus_v1.1.md` | 5434 | 21.3 | 15.2 |
| `02_cdss-stack-augmented/harness_ml_primer.md` | 2376 | 21.2 | 15.6 |
| `11_prompts/PROMPT-PRM-PRB_patient_ui_launch.md` | 487 | 21.2 | 10.3 |
| `11_prompts/PROMPT-SURVEY-3_final-quality-improvement.md` | 972 | 21.1 | 11.7 |
| `02_cdss-stack-augmented/primer_C_casebundle_corpus.md` | 1342 | 21.0 | 15.4 |
| `02_cdss-stack-augmented/ecosystem_integration_report.md` | 396 | 20.8 | 13.7 |
| `03_makoha-butterfly-corpus/corpus-md/four-faces-corpus_v1.1.md` | 7311 | 20.8 | 16.1 |
| `06_repositories/repo-skeletons/cdss-coder/README.md` | 83 | 20.8 | 14.7 |
| `09_diagrams/INDEX.md` | 353 | 20.8 | 9.6 |
| `11_prompts/PROMPT-SURVEY-2_folder-parity_build-spec-queue.md` | 1034 | 20.7 | 9.8 |
| `10_regulatory-execution/REG-EU_v1.0.md` | 1209 | 20.5 | 12.4 |
| `03_makoha-butterfly-corpus/corpus-md/makoha-in-flight_v1.0.md` | 1980 | 20.4 | 13.0 |
| `11_prompts/PROMPT-P0_primer0_launch.md` | 694 | 20.4 | 10.3 |
| `03_makoha-butterfly-corpus/butterfly-primers/primer_LWC_fuzzy_spine.md` | 3662 | 20.3 | 13.0 |
| `06_repositories/repo-skeletons/cdss-integration/GPP-CHANNEL.md` | 101 | 20.2 | 14.7 |
| `10_regulatory-execution/REG-NZ_v1.1.md` | 1954 | 20.1 | 12.2 |
| `11_prompts/PROMPT-PRM-LBP_clinician_ui_launch.md` | 399 | 19.9 | 10.4 |
| `02_cdss-stack-augmented/primer_A_bayesian_engine.md` | 1309 | 19.8 | 14.5 |
| `04_hardening/HARDEN-1_coverage_ledger_seed.md` | 99 | 19.8 | 12.5 |
| `06_repositories/repo-skeletons/cdss-governance/README.md` | 79 | 19.8 | 11.8 |
| `06_repositories/repo-skeletons/cdss-harness/README.md` | 79 | 19.8 | 13.5 |
| `07_deployment-and-operations/DEPLOY-2_testing_verification_acceptance.md` | 218 | 19.8 | 12.8 |
| `10_regulatory-execution/REG-NZ_v1.0.md` | 892 | 19.8 | 12.0 |
| `11_prompts/PROMPT-PRM-TXC_patient_face_launch.md` | 552 | 19.7 | 10.2 |
| `11_prompts/PROMPT-H_lumos_pathway_launch.md` | 274 | 19.6 | 11.8 |
| `10_regulatory-execution/EXEC-1_execution_directive.md` | 995 | 19.5 | 11.9 |
| `06_repositories/repo-skeletons/cdss-llm-lattice/README.md` | 97 | 19.4 | 13.5 |
| `AGENTS.md` | 783 | 19.1 | 11.1 |
| `06_repositories/repo-skeletons/cdss-engine/README.md` | 76 | 19.0 | 13.2 |
| `11_prompts/PROMPT-J_model_governance_launch.md` | 209 | 19.0 | 13.2 |
| `06_repositories/repo-skeletons/cdss-integration/README.md` | 74 | 18.5 | 11.9 |
| `11_prompts/PROMPT-A_bayesian_engine_launch.md` | 241 | 18.5 | 10.0 |
| `08_research/RESEARCH-1.1_findings_delta.md` | 165 | 18.3 | 8.5 |
| `05_registers-and-contracts/CONTRACT-RRI-1_render-invariance_test-spec.md` | 537 | 17.9 | 10.6 |
| `11_prompts/PROMPT-PRM-CEC_engines_launch.md` | 483 | 17.9 | 9.0 |
| `06_repositories/repo-skeletons/cdss-ui-clinician/README.md` | 71 | 17.8 | 12.6 |
| `11_prompts/PROMPT-PRM-ANT_regulatory_sensing_launch.md` | 463 | 17.8 | 9.5 |
| `11_prompts/PROMPT-PRM-HDC_clinician_face_launch.md` | 528 | 17.6 | 9.0 |
| `04_hardening/MAJOR_TASK_2_anti-laziness-hardening-directive.md` | 1402 | 17.5 | 11.5 |
| `10_regulatory-execution/REG-POSTURE_v1.2_CONTENTS.md` | 140 | 17.5 | 8.6 |
| `11_prompts/PROMPT-B_evidence_library_launch.md` | 227 | 17.5 | 11.5 |
| `03_makoha-butterfly-corpus/corpus-md/antennae-corpus_v1.0.md` | 4321 | 17.4 | 12.5 |
| `10_regulatory-execution/REG-POSTURE_v1.2.md` | 5105 | 17.4 | 11.6 |
| `11_prompts/PROMPT-F_conformal_wrapper_launch.md` | 243 | 17.4 | 10.6 |
| `06_repositories/repo-skeletons/cdss-corpus/README.md` | 104 | 17.3 | 13.7 |
| `06_repositories/repo-skeletons/cdss-corruption/README.md` | 86 | 17.2 | 9.6 |
| `02_cdss-stack-augmented/primers_briefing.md` | 324 | 17.1 | 10.7 |
| `03_makoha-butterfly-corpus/MANIFEST.md` | 188 | 17.1 | 11.8 |
| `11_prompts/PROMPT-G_corruption_engine_launch.md` | 205 | 17.1 | 9.7 |
| `11_prompts/PROMPT-I_living_evaluation_launch.md` | 188 | 17.1 | 10.7 |
| `03_makoha-butterfly-corpus/butterfly-primer-programme_prompt_v1.0.md` | 591 | 16.9 | 9.3 |
| `10_regulatory-execution/REG-POSTURE_v1.1.md` | 4089 | 16.5 | 11.5 |
| `11_prompts/PROMPT-D_content_registry_launch.md` | 212 | 16.3 | 10.3 |
| `11_prompts/PROMPT-E_graph_rag_launch.md` | 208 | 16.0 | 10.8 |
| `06_repositories/repo-skeletons/cdss-registry/README.md` | 63 | 15.8 | 11.9 |
| `README.md` | 441 | 15.8 | 9.2 |
| `06_repositories/repo-skeletons/cdss-library/README.md` | 62 | 15.5 | 11.4 |
| `10_regulatory-execution/FOLD-1_antennae_fold_worklist.md` | 233 | 15.5 | 8.9 |
| `10_regulatory-execution/REG-SPRINT_v1.0.md` | 925 | 15.2 | 11.7 |
| `11_prompts/PROMPT-C_casebundle_corpus_launch.md` | 183 | 15.2 | 9.4 |
| `06_repositories/repo-skeletons/cdss-ui-patient/README.md` | 59 | 14.8 | 15.8 |
| `10_regulatory-execution/MAK-GOV_addendum-g_v0.9.md` | 1459 | 14.4 | 12.4 |
| `06_repositories/repo-skeletons/cdss-graph/README.md` | 57 | 14.2 | 10.7 |
| `07_deployment-and-operations/OPS-1.1_procedures_cc5_delta.md` | 986 | 13.7 | 8.5 |
| `06_repositories/repo-skeletons/cdss-conformal/README.md` | 54 | 13.5 | 12.4 |
| `06_repositories/repo-skeletons/cdss-lumos/README.md` | 51 | 12.8 | 11.4 |
