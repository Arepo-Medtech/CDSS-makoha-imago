# L2_governance — Layer 2 census (Q-D-11, Q-F-04) — `raw/governance_census.json` (script in the run log) + INDEX §4 readings

Columns are mechanical presences: **owner** = an owner-type frontmatter key (`owner`, `attestation_by`, `produced_by`, `executor`) or an `Owner` column/phrase in the body; **cadence** = a cadence/trigger word in the body; **change** = `change_policy` key; **supersession** = `supersedes`/`applies_to` key; **read-through** = the base-is-read-through-this-file sentence; **honesty** = an execution-honesty statement. `✓`/`—`. Absences are candidates; Phase 2 reads each before filing GOVERNANCE-GAP (a governance statement may live in the INDEX §4 for the folder rather than the file).

## Load-bearing documents (01_, 04_–10_, 00_; corpus, skeleton stubs and launch prompts excluded here — see notes)

| File | owner | cadence | change | supersession | read-through | honesty | placeholders (ND/NS/UA/PEND) |
|---|---|---|---|---|---|---|---|
| `00_MANIFEST.md` | — | ✓ | — | — | ✓ | ✓ | 5/3/2/4 |
| `01_north-star-and-transformation/MET-1.1_metamorphosis_plan_delta.md` | — | — | — | ✓ | — | ✓ | 0/0/0/0 |
| `01_north-star-and-transformation/MET-1_metamorphosis_plan_v1.0.md` | ✓ | ✓ | — | ✓ | — | ✓ | 7/2/0/0 |
| `01_north-star-and-transformation/MET-2.1_decision_register_delta.md` | ✓ | — | — | — | ✓ | — | 0/0/0/0 |
| `01_north-star-and-transformation/MET-2_conflict_and_decision_register.md` | ✓ | ✓ | — | — | — | — | 2/0/0/2 |
| `01_north-star-and-transformation/MET-3_traceability_map.md` | — | — | — | — | — | — | 0/0/0/0 |
| `01_north-star-and-transformation/MET-4_gap_analysis_and_roadmap.md` | — | — | — | — | — | — | 1/0/0/0 |
| `04_hardening/HARDEN-1.1_coverage_ledger_seed_delta.md` | ✓ | — | ✓ | ✓ | ✓ | — | 196/1/0/3 |
| `04_hardening/HARDEN-1_coverage_ledger_seed.md` | — | — | — | — | — | ✓ | 0/1/0/2 |
| `04_hardening/HARDEN-2.1_spec_census_and_self-audit_delta.md` | — | ✓ | ✓ | ✓ | ✓ | ✓ | 0/0/0/2 |
| `04_hardening/HARDEN-2_hardening_spec.md` | — | ✓ | — | — | — | — | 0/0/0/0 |
| `04_hardening/HARDEN-3.1_task_register_delta.md` | ✓ | — | ✓ | ✓ | ✓ | — | 198/1/0/33 |
| `04_hardening/HARDEN-3_hardening_plan_worklist.md` | — | — | — | — | — | — | 0/0/0/0 |
| `04_hardening/INDEX.md` | ✓ | — | — | — | ✓ | ✓ | 0/0/0/2 |
| `05_registers-and-contracts/CONTRACT-ARG-1_argument_schema.md` | — | — | — | — | — | — | 0/0/0/0 |
| `05_registers-and-contracts/CONTRACT-RRI-1_render-invariance_test-spec.md` | — | — | — | — | — | — | 0/0/0/0 |
| `05_registers-and-contracts/INDEX.md` | ✓ | — | — | — | ✓ | ✓ | 0/0/0/0 |
| `05_registers-and-contracts/REG-R29.1_schema_twin_delta.md` | — | — | ✓ | ✓ | ✓ | — | 0/0/0/1 |
| `05_registers-and-contracts/REG-R29_hardening_coverage_ledger.schema.md` | — | — | — | — | — | — | 0/0/0/0 |
| `05_registers-and-contracts/REG-R30.1_seed_delta.md` | — | ✓ | — | — | — | — | 0/0/0/0 |
| `05_registers-and-contracts/REG-R30.2_seed_delta.md` | — | — | — | — | — | — | 0/0/0/0 |
| `05_registers-and-contracts/REG-R30_regulatory_posture_register.schema+seed.md` | — | ✓ | — | — | — | — | 0/0/0/0 |
| `06_repositories/INDEX.md` | ✓ | — | — | — | — | ✓ | 1/0/0/0 |
| `06_repositories/REPO-MAP_v2.md` | — | — | — | — | — | — | 0/0/0/0 |
| `07_deployment-and-operations/DEPLOY-1.1_run-map_delta.md` | ✓ | ✓ | ✓ | ✓ | ✓ | — | 8/0/0/0 |
| `07_deployment-and-operations/DEPLOY-1_deployment_plan_and_sequencing.md` | — | — | — | — | — | — | 1/0/0/0 |
| `07_deployment-and-operations/DEPLOY-2_testing_verification_acceptance.md` | — | — | — | — | — | — | 0/0/0/0 |
| `07_deployment-and-operations/GOV-1_ownership_governance_postdeploy.md` | — | ✓ | — | — | — | — | 4/0/0/0 |
| `07_deployment-and-operations/INDEX.md` | ✓ | ✓ | — | — | ✓ | ✓ | 6/0/0/0 |
| `07_deployment-and-operations/OPS-1.1_procedures_cc5_delta.md` | ✓ | ✓ | ✓ | ✓ | ✓ | — | 13/0/0/1 |
| `07_deployment-and-operations/OPS-1_operating_procedures.md` | — | ✓ | — | — | — | — | 0/0/0/0 |
| `07_deployment-and-operations/SEC-1_security_privacy_compliance.md` | — | — | — | — | — | — | 0/0/0/0 |
| `07_deployment-and-operations/SEC-2_threat-model_and_data-flow.md` | ✓ | — | — | — | — | — | 2/0/0/0 |
| `08_research/INDEX.md` | ✓ | — | — | — | ✓ | ✓ | 0/0/0/0 |
| `08_research/RESEARCH-1.1_findings_delta.md` | — | — | ✓ | ✓ | ✓ | — | 0/0/0/0 |
| `08_research/RESEARCH-1_findings_gaps_source_map.md` | — | — | — | — | — | — | 0/0/0/0 |
| `09_diagrams/INDEX.md` | ✓ | ✓ | — | — | — | ✓ | 0/0/0/0 |
| `10_regulatory-execution/EXEC-1_execution_directive.md` | — | — | — | — | — | ✓ | 0/0/0/0 |
| `10_regulatory-execution/FOLD-1_antennae_fold_worklist.md` | ✓ | ✓ | — | — | ✓ | — | 0/0/0/0 |
| `10_regulatory-execution/INDEX.md` | ✓ | — | — | — | ✓ | ✓ | 1/0/0/0 |
| `10_regulatory-execution/MAK-GOV_addendum-g_v0.9.md` | ✓ | — | — | — | — | ✓ | 0/0/0/0 |
| `10_regulatory-execution/REG-EU_v1.0.md` | ✓ | ✓ | — | — | — | — | 0/0/0/0 |
| `10_regulatory-execution/REG-NZ_v1.0.md` | ✓ | ✓ | — | — | — | — | 0/0/0/0 |
| `10_regulatory-execution/REG-NZ_v1.1.md` | ✓ | ✓ | — | ✓ | — | — | 0/0/0/0 |
| `10_regulatory-execution/REG-POSTURE_v1.1.md` | ✓ | ✓ | — | ✓ | — | ✓ | 1/0/0/0 |
| `10_regulatory-execution/REG-POSTURE_v1.2.md` | ✓ | ✓ | — | ✓ | — | ✓ | 1/0/0/0 |
| `10_regulatory-execution/REG-POSTURE_v1.2_CONTENTS.md` | ✓ | ✓ | — | — | — | — | 0/0/0/0 |
| `10_regulatory-execution/REG-SPRINT-1.1_delta.md` | — | — | ✓ | ✓ | — | — | 0/0/0/0 |
| `10_regulatory-execution/REG-SPRINT-1.2_census_delta.md` | ✓ | — | ✓ | ✓ | ✓ | — | 0/0/0/0 |
| `10_regulatory-execution/REG-SPRINT_v1.0.md` | ✓ | — | — | — | — | — | 0/0/0/0 |
| `10_regulatory-execution/REG-US_v1.0.md` | ✓ | ✓ | — | — | — | — | 0/0/0/0 |

Totals over 51 documents: owner 26 · cadence 21 · change_policy 9 · supersession 14 · read-through 16 · honesty 16.

## Folder-level governance (Q-F-04) — INDEX §4 readings

| Folder | executed-vs-proposed stated | cadence owner named | supersession rule stated | Evidence |
|---|---|---|---|---|
| 04 | ✓ ("The MT2 pass has **not** been executed… every ledger row is a pre-pass placeholder") | ✓ MT2 operator (DEC-10) — person [NEEDS DEFINITION] | ✓ ("Read the seed's states as placeholders"; deltas read-through) | INDEX-04 §1, §4 |
| 05 | ✓ ("Nothing in this folder is ratified (DEC-02 Open)") | ✓ Architecture owner (DEC-02); cdss-governance for R30 | ✓ §3 reading rule (P-D-11) | INDEX-05 §3, §4 |
| 06 | ✓ ("no code exists anywhere in this folder; every skeleton is Proposed") | ✓ Repo owner per REPO-MAP (DEC-09) [NEEDS DEFINITION] | partial — REPO-MAP v3 "after DEC-09" named; per-stub supersession = instantiation | INDEX-06 §4, §5 |
| 07 | ✓ ("Nothing is deployed") | partial — person-level owners [NEEDS DEFINITION] (GOV-1); infra owner proposed DEC-23 | ✓ ("every file Proposed/Retained per its own status"; EXEC-1 governs sequence) | INDEX-07 §3, §4 |
| 08 | ✓ ("all eight RG OPEN; no clinical number asserted") | ✓ RG owners per RESEARCH-1 §3; closure path RESEARCH-1.1 D-3 | ✓ ("An RG closes when…") | INDEX-08 §1, §4 |
| 09 | ✓ ("sources are canonical and the html pages are derived; v2 files preserved unedited") | ✓ Architecture owner (PROC-09-REGEN) | ✓ successor rule (G-10; X1 append-only) | INDEX-09 §1, §4 |
| 10 | ✓ ("ADVISORY_ONLY content throughout; nothing attested… packets ASSEMBLED but NOT SENT") | partial — regulatory owner [NEEDS DEFINITION] (G-09 / REG-POSTURE §12.3) | ✓ ("Superseded files… retained unedited and must not be cited for current positions (EX-3)") | INDEX-10 §1, §4 |
| 01, 02, 03, 11, ROOT | 01: MET-1.1 "Unchanged honesty line"; 02: annex banners; 03: MANIFEST precedence + "zero edits"; 11: PROMPT-SERIES header + A-004; ROOT: README "Laws of the corpus" | 01/02/03: owners by role in MET-2 DEC rows / 00_MANIFEST §4.4 (persons [NEEDS DEFINITION]); 03: corpus owner; 11: prompt author = MT2 operator/prompt author (HARDEN-1.1) | 01: delta pattern; 02: X1 append-only; 03: change_policy per volume; 11: new prompt version beside old | no INDEX file for 01/02/03/11 — parents are MET-1 §16 / primers_briefing / 03_ MANIFEST / PROMPT-SERIES index (survey-2 P-F-02 ruling) |

## Placeholder registration (P-D-12, carried into Q-D-11)

Tree-wide (in scope, `grep -o`): `[NEEDS DEFINITION]` **557** in 67 files · `[NEEDS SOURCE]` 19 in 11 · `[UNAVAILABLE]` 2 in 1 · `PENDING-VALIDATOR` 46 in 10 · `PENDING-REGISTER-HOME` 6 in 4 · `PENDING-ENUMERATION` 7 in 5. The only registered census is `00_MANIFEST.md §6` (2026-09-01): "22 [NEEDS DEFINITION], 4 [NEEDS SOURCE], 1 [UNAVAILABLE], 4 PENDING-VALIDATOR, 5 PENDING-REGISTER-HOME… 1 PENDING-ENUMERATION". The growth (22 → 557) is almost entirely HARDEN-1.1/3.1 owner cells (`Repo owner per REPO-MAP (DEC-09) [NEEDS DEFINITION]` ×98, `Corpus owner… [NEEDS DEFINITION]` ×46, …) — each placeholder names its resolving DEC/G, which satisfies P-D-12's *registration* test row by row, but **no census line after §6 states the current totals** → GOVERNANCE-GAP at 00_ level (a §6-style placeholder census line owed by the next amendment), weight 3 (blocks nothing; breaks the manifest's own self-audit chain).

