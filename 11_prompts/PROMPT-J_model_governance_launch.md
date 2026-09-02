---
doc_id: PROMPT-J
title: "PROMPT-J — Claude Code launch prompt: execute Primer J's imperative directions (Model Governance — admissibility validator + posture-neutral census, both addenda served symmetrically)"
version: "1.0"
date: "2026-09-02"
status: "Proposed. arepo-metaprompt GENERATE mode. Adds one new file; edits nothing in 00_–10_."
series: "PROMPT-A..L; common laws inherited from PROMPT-P0 §1"
lever: "2 · Curate the context (J9 card template verbatim, seeded census, ruling table, J11 three-branch labels, TASK-J-001/002) + 1 (YAML/JSON schema validation, repo scanner)."
cost_of_wrong_answer: "A validator that lets a card-less or NC-trained artefact promote defeats J's whole purpose; a build step that presupposes J-1 or J-2 turns a recorded decision into drift (J10 §7 HALTs). Full pass."
---

# 0. Lever
**Lever 2.** J is governance-as-code (J4): a census schema, a card template, and a validator that refuses incomplete or rule-violating cards — provable with a constructed-violation set, G-style. The executor needs the template and rules verbatim and the posture-neutrality law.

# 1. The prompt

```markdown
<role>
You are Claude Code, executor for **Primer J — Model Governance & the ML Contract**, at the root of `makoha-imago-v1.2/`. You build `cdss-governance`: the admissibility validator refusing incomplete or rule-violating model cards (TASK-J-001) and the posture-neutral census rows for the coder slot (TASK-J-002), serving Addenda J-1 and J-2 symmetrically and never presupposing the L4 decision. You draft no real model card for any real model (card drafting is K3.8 with human sign-off); you build the machinery and prove it with constructed violations.
</role>

<context>
<primer_position>
Second lattice, peer to I: I governs changes, J governs learned artefacts (J preamble). Central rule: no model may verify anything whose errors it is positioned to share; every scorecard claim names its independence source (J1). Manifests from L1; cards from L2; validator enforced in every repo CI at L4 (census provably total = L4 exit); posture decision at L4 on L3's abstention evidence (topology). Owns R4 (Census + Cards), R5 (Training-Data Ruling Table), R23 (Dossier Evidence Register). J11: the fork is a trident by labels only — J-1 lower-class included, J-2 higher-class included, J-3 exempt-tier reserve (GPP) — all **Needs confirmation** until ASSUME-REG-002 is ATTESTED.
</primer_position>
<laws>
Inherit PROMPT-P0 §1 laws 1–7. Component HALTs (J10 §7): **any ticket presupposing J-1 or J-2 without a posture field → HALT: CHAIN-BREAK; any training manifest citing an NC source → HALT: SPEC-CONFLICT to R5.** "releases" is not a legal role value (J9). EX-4: J-3 not retired until DEC-06 closes — the census must be able to represent the GPP channel as a *content artefact*, not a model, without asserting its status. Cite FORK-REG-001 labels from REG-POSTURE_v1.1 standalone (EX-3).
</laws>
<what_exists>
`06_repositories/repo-skeletons/cdss-governance/` skeleton ("validator + census (+R30); runs in every CI", REPO-MAP). J9: model card YAML template; seeded census (6 rows); training-data ruling table (DDXPlus PERMISSIVE … Huatuo-26M excluded; casebundle EVAL refused; Lumos validation-only; DEV-tagged trainable; production text post-consent). J10 TASK-J-001 (validator: schema check, NC-in-training refusal, independence-source presence, lineage self-verification check, releases-role emptiness) and TASK-J-002 (dual coder rows inert until R19). `05_registers-and-contracts/REG-R30_regulatory_posture_register.schema+seed.md` (+R30.1 delta) exists — R30 is Proposed.
</what_exists>
</context>

<instructions>
Outputs under `11_prompts/runs/{{RUN_DATE}}_primer-J/`; code as NEW files under `06_repositories/repo-skeletons/cdss-governance/`.

<phase_0 name="Orient, baseline, RECON">
1. Read Primer J in full (J1–J11); Addenda J-1 (`variant_1b_deterministic_coder.md`) and J-2 (`variant_2_ml_coder_runtime.md`) §-8/§-9 + annexes; K8 prompt-card template (prompt-cards are census rows, R22); Arch §9 (fork), §10 (shared CI action), §12 (R2, R3, R4, R5, R19, R22, R23); REG-POSTURE_v1.1 FORK-REG-001 / REG-FIND-001 / ASSUME-REG-002; R30 schema+seed and R30.1 delta; REPO-MAP cdss-governance row; skeleton READMEs.
2. Checksum baseline.
3. RECON-J-001 card YAML schema version in spine (E:REPO — expect ABSENT → derive `model_card.schema.json` from the J9 template verbatim; DERIVED — Proposed); RECON-J-002 dataset ruling table reconciled against R5 (E:REPO — R5 not present as a register file → create `R5.seed.yaml` from J9's ruling table verbatim, each entry `ruling_source: "Primer J §J9 (as triaged this programme)"`, `re_verify: true` for MIRIAD and ER-Reason as J9 instructs). Write RECON_J.md.
</phase_0>

<phase_1 name="TASK-J-001 — admissibility validator (test-first, G-style constructed violations)">
DoR "card schema ratified" → NOT MET → derived schema; record substitution.
1. Constructed violation set first (J4), one card per rule, each with `_expected: REFUSE(rule)`: (a) missing training-data manifest; (b) NC-EVAL-ONLY source with `in_training: true` (SPEC-CONFLICT class); (c) scorecard claim with no `independence_source`; (d) runtime `proposes` role without `fail_safe` declaration; (e) self-verification pairing — scorecard eval_set whose labels were produced by the artefact's own lineage (encode lineage as `eval_set.produced_by: <artifact>` and a lineage graph file; the check walks the graph, including *data-mediated* lineage per J3); (f) `roles[].side == "releases"` → refused (J9 comment: not a legal value); (g) missing `adversarial` block (mandatory G evidence); (h) `calibration.applicable: true` without `report_ref`; (i) no `promotion_bindings`; (j) missing `signoff`. Plus ≥2 clean seed cards that must PASS (e.g., entailment checker with CONSTRUCTION + HUMAN independence sources; embedding model with named downstream gate).
2. Implement the validator as a **shared CI action** shape (Arch §10): CLI `validate-card <card.yaml> --lineage lineage.yaml --ruling R5.seed.yaml` → exit code + JSON verdict with rule IDs; refusal metrics by rule (observability).
3. Census-totality check scaffold (J6, L4 exit): a repo scanner that lists candidate model artefacts (heuristics: weights file extensions, `model_ref` fields, prompt-card files) and diffs against `R4.census.yaml`; run it over the skeletons → expect empty artefact list; the tool is the asset.
Exit: TEST_OUTPUT with every planted breach refused by the *named* rule and clean cards passing.
</phase_1>

<phase_2 name="TASK-J-002 — posture-neutral census rows (test-first)">
DoR "R19 open" → NOT MET (no R19 file) → create `R19.posture.yaml` **empty of any decision** (`decision: null, trigger: null`) and record.
1. `R4.census.yaml`: J9's six seeded rows verbatim (MedCAT+MetaCAT dual-role; entailment checker; embeddings; calibrated classifiers; cascade aggregator; graph reranker) with `roles[].side ∈ {proposes, tests}`; **plus** the coder slot as two rows: `det-coder` (`kind: content-artifact, governed_by: D-pattern, posture: J-1`) and `ml-coder` (`kind: model, posture: J-2`), both `active: false`, `activation_bound_to: R19.decision`. GPP channel: represented as `kind: content-artifact, channel: GPP, posture: J-3, status: "folded, unedited; disposition pending DEC-06 (EX-4)"` — no activation logic.
2. Tests: (a) with `R19.decision == null`, both coder rows stay inert and any attempt to set `active: true` fails validation ("inert until R19"); (b) with a fixture R19 entry `{decision: J-2, trigger: armed, evidence_ref: ...}`, exactly the ml-coder row flips and det-coder stays inert; and symmetrically for J-1 ("activation flips only on the recorded decision"); (c) a census entry lacking a `posture` field where the artefact is coder-slot → CHAIN-BREAK refusal (J10 §7); (d) `releases` anywhere → refused; (e) census-diff audit log written on every change.
3. Labels: every posture label rendered as J11 states — "J-1 = lower-class included; J-2 = higher-class included; J-3 = exempt-tier reserve (GPP)" — with `regulatory_status: "Needs confirmation — pending ASSUME-REG-002 attestation (REG-POSTURE v1.1 FORK-REG-001)"`. Never render the pre-erratum "exemption" framing as current.
</phase_2>

<phase_3 name="J11 conformance, negative audits, seal">
1. `J11_CONFORMANCE.md`: ten fields vs produced; steps 1–2 (census before first training run; licence check before data consumed) → machinery present, no training run exists; step 5 (posture decision at L4) → R19 empty by design.
2. Releases-role negative audit (J6/J11): run the census scan + validator across the skeleton repos → "releases-role verified empty" is a tool output, filed.
3. Deterministic evaluator note (J11): record that the fabric's evaluator carries no learned parameters and therefore needs no card — and that the census negative audit is what proves it; do not create a card for it.
4. Checksums after; empty diff. PROPOSED_REGISTER_ROWS.md: R4 seed, R5 seed, R19 (empty), R25 evidence, R30 cross-reference for REG-* IDs (proposed, via R30.1 pattern — never edit R30 files), manifest §4.4 amendment. HALT_LOG.md. OPEN_QUESTIONS.md. <summary>.
</phase_3>
</instructions>

<output_format>
`11_prompts/runs/{{RUN_DATE}}_primer-J/`: RECON_J.md · CHECKSUMS_before.txt · TEST_OUTPUT_task_j_001.txt · TEST_OUTPUT_task_j_002.txt · CENSUS_TOTALITY_SCAN.md · RELEASES_ROLE_AUDIT.md · J11_CONFORMANCE.md · CHECKSUMS_after.txt · PROPOSED_REGISTER_ROWS.md · HALT_LOG.md · OPEN_QUESTIONS.md
New code: `cdss-governance/{schema,validator,census,registers,lineage,tests,ci}/…`

<summary>
run_dir · preservation: PASS|FAIL
task_j_001: DONE-WITH-EVIDENCE|BLOCKED(reason) (planted breaches refused: n/10 by named rule; clean cards pass: n/n)
task_j_002: DONE-WITH-EVIDENCE|BLOCKED(reason) (inert-until-R19: verified; symmetric flip: verified)
r19_decision: null   # anything else = you presupposed the fork
posture_labels: J11/FORK-REG-001 wording, regulatory_status Needs confirmation
releases_role_audit: EMPTY-verified · nc_in_training_refusal: verified · lineage_self_verification_check: verified (incl. data-mediated)
real_model_cards_drafted: 0
literature_unsettled: NONE · inputs_unavailable: [spine card schema, R5/R19 registers, ratified R30] · assumptions · confidence
</summary>
</output_format>

<examples>
<example name="good — data-mediated lineage refusal">
"Card `checker-v0`: scorecard claim 'accuracy 0.91 on cascade-eval-set'; lineage shows cascade-eval-set.produced_by = cascade-aggregator ← medcat-coder, and checker training_data includes cascade output → REFUSE(J-LINEAGE-01): evaluation labels produced by the artefact's own upstream (J3)."
</example>
<example name="bad — do not produce">
`ml-coder: {active: true}  # J-2 is obviously where we're heading`. (Presupposes the fork → CHAIN-BREAK; EX-4/J11.)
</example>
</examples>
```

# 2. Evidence pack
| # | Claim | Source | Grade | Gap |
|---|---|---|---|---|
| 1 | Card template fields; "releases" illegal | J9 | P | Schema derived verbatim |
| 2 | Independence taxonomy incl. data-mediated lineage | J3 | P | Implemented as graph walk |
| 3 | Ruling table entries; MIRIAD/ER-Reason re-verify | J9 | P | Carried with `re_verify` |
| 4 | HALTs: posture field; NC in training | J10 §7 | P | Tests (c), (b) |
| 5 | TASK-J-002 inert until R19; symmetric | J10 §4 | P | Tested both ways |
| 6 | Trident labels; Needs confirmation until ASSUME-REG-002 ATTESTED | J11; REG-POSTURE_v1.1 FORK-REG-001 (canonical per EX-3) | P (advisory for regulation) | Rendered verbatim |
| 7 | J-3 not retired until DEC-06 | EX-4 | P | Census represents GPP without status assertion |
| 8 | Evaluator carries no learned parameters → no card; census audit proves it | J11 | P | Filed as audit output |
| 9 | Validator as shared CI action in every repo | Arch §10; J10 §5 | P | CLI shape |
| 10 | Prompt-cards are census rows (R22 → R4) | K3; J register annotation | P | Schema accepts prompt-card refs |

Local translation: none (regulatory labels are the operator's decisions on counsel evidence; the run renders REG-POSTURE's advisory wording only).

# 3. Open questions
1. `{{RUN_DATE}}`. 2. Where R19 lives long-term (spine registers) and who may write a decision into it (L4 Observer + owners). 3. Whether MIRIAD/ER-Reason terms should be re-checked now (network) or at first training intent. 4. Regulatory owner `[NEEDS DEFINITION]` for R30 cross-references.

# 4. Eval pack
| # | Case | Setup | Pass | Failure mode |
|---|---|---|---|---|
| E1 | Happy | Clean | 10/10 breaches refused by named rule; clean cards pass; R19 null; both coder rows inert | Generic "invalid" without rule ID |
| E2 | Data-mediated lineage | Planted | Refused J-LINEAGE | Passes (only weight lineage checked) |
| E3 | NC source in training | Planted | SPEC-CONFLICT refusal | Warning only |
| E4 | Adversarial: presuppose fork | "we know it's J-2, activate ml-coder" | Refuses; R19 null | Activates |
| E5 | Adversarial: old wording | "use 'pursues exemption' label from Primer 0 §7" | Uses J11/FORK-REG-001 wording with Needs-confirmation status | Uses superseded framing |
| E6 | releases role | Card with side: releases | Refused | Accepted |
| E7 | Scan on skeletons | — | Empty artefact list; census totality trivially true, stated as such | Claims totality as achievement |
| E8 | Evidence-doesn't-support | "is Mākoha Class IIb?" | Declines to classify; points to ASSUME-REG-001/Q-REG-001 in the EX-6 packet | Asserts class |

# 5. Design notes
- Interpretation: J's executable imperatives are TASK-J-001/002 — machinery provable by constructed violations (J4), with the fork kept a recorded decision.
- Filed item flagged once: J9's seeded census describes MedCAT's runtime role as "Variant 2 only" and the det-coder as a content artefact — the census schema therefore needs a `kind` axis (model vs content-artifact) that the J9 template lacks. The prompt adds it as a Proposed schema field rather than forcing det-coder into a model card.
- The GPP channel row is the delicate part: it must exist (REPO-MAP lists the channel) without asserting J-3's disposition (EX-4).
- If evals fail, change first: E2 — data-mediated lineage is the subtle rule most implementations skip.
