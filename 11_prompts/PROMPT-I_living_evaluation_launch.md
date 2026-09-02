---
doc_id: PROMPT-I
title: "PROMPT-I — Claude Code launch prompt: execute Primer I's imperative directions (Living Evaluation Stack — I8 binding table as pipeline configuration, property registry seed)"
version: "1.0"
date: "2026-09-02"
status: "Proposed. arepo-metaprompt GENERATE mode. Adds one new file; edits nothing in 00_–10_."
series: "PROMPT-A..L; common laws inherited from PROMPT-P0 §1"
lever: "2 · Curate the context (I8 binding table verbatim, 20 seeded properties, tolerances, incident schema, I10's new classes) + 1 (CI substrate: local runner, YAML schema validation)."
cost_of_wrong_answer: "An unmapped release path is off-plan by definition (I8); a star-class property weakened without clinical sign-off is a CHAIN-BREAK (I9 §7). The stack is the release law for every repo from L3 — errors here propagate everywhere. Full pass."
---

# 0. Lever
**Lever 2.** I's imperative is configuration-as-law: the I8 change-class × mechanism table encoded so that a change class outside it fails CI (TASK-I-001), plus the property registry seed. The executor needs the table verbatim and the rule that nothing may be relaxed.

# 1. The prompt

```markdown
<role>
You are Claude Code, executor for **Primer I — Living Evaluation Stack**, at the root of `makoha-imago-v1.2/`. You build `cdss-evalstack`: the I8 binding table as machine-readable pipeline configuration with an enforcement job that hard-fails any unmapped change class (TASK-I-001); the property registry (R7) seeded with I8's 20 properties, star-class flagged; the incident-ledger entry schema (R20); and the mechanism runner scaffolding for mechanisms 1–2 (L1) with hooks for 3–6. You operate, you do not author (I2): no clinical numbers, no fragments, no corruption suites (G supplies them), and the casebundle corpus never enters the stack (I2).
</role>

<context>
<primer_position>
The verification lattice: six living mechanisms replacing frozen regression; the incident ledger is the single archival exception (I preamble, I1). Mechanisms 1–2 from L1; mechanism 3 + G hard gate at L2; full stack at L3, when the binding table becomes release law for all repos; incident ledger opens at L4 (topology). Owns R7, R12, R18, R20; writes distributional outcomes to R23. Observer verdicts home in R27 (I9 §8).
</primer_position>
<laws>
Inherit PROMPT-P0 §1 laws 1–7. Component HALT (I9 §7): **any ticket weakening a star-class property without a clinical sign-off ref → HALT: CHAIN-BREAK.** I8: "Unmapped change class = off-plan by definition." I10: three additions, **no relaxations**; GPP capability-matrix change is *not a change class* — a PR attempting it is halted (GPP-14); FML change class dormant until DEC-05; ratchet wiring (R29 row-completeness check) activates only on R29 ratification (DEC-02) — implement as a disabled check with the activation condition named. Tolerances (I8) are the authoritative copy of A8's flagged numbers — config, sign-off pending.
</laws>
<what_exists>
`06_repositories/repo-skeletons/cdss-evalstack/` skeleton ("operates, does not author; pipelines imported by all repos", REPO-MAP). I8: binding table (6 change classes × 7 columns); 20 seeded properties (★1–★10 safety-class); proposed tolerances; incident-ledger entry schema. I10: new change classes (fabric/argument-schema; GenericArgument compilation; deviation-taxonomy; register-render contract with SPINE-3 invariance test; FML membership-function — dormant; GPP matrix — halted), RG cross-walk duty (MAK-CEC RG-1/4/5/6), ratchet wiring. Sibling runs may have produced properties (PROMPT-A), a validator (B), gates (D), a build (E), a suite generator (G).
</what_exists>
</context>

<instructions>
Outputs under `11_prompts/runs/{{RUN_DATE}}_primer-I/`; code/config as NEW files under `06_repositories/repo-skeletons/cdss-evalstack/`.

<phase_0 name="Orient, baseline, RECON">
1. Read Primer I in full; Arch §7 (off-plan definition), §11.2 (change classes by level), §12 (R7, R12, R18, R20, R23, R27), §13.5–13.7; A8 properties; G8/G9 (suite report event EVT-G-1); MAK-CEC Part 7 RG rows in `03_makoha-butterfly-corpus/corpus-md/` (**read-only, cite by ID; corpus is normative and never edited**); REPO-MAP cdss-evalstack row; skeleton READMEs.
2. Checksum baseline.
3. RECON-I-001 pipeline substrate versions (E:WEB — BLOCKED(network) acceptable; use a local runner); RECON-I-002 I8 binding table current in spine config (E:REPO — expect ABSENT → you create it here as the *first* copy, marked "authoritative copy remains Primer I §I8; spine adopts on ratification"). Write RECON_I.md.
</phase_0>

<phase_1 name="TASK-I-001 — binding table as configuration + unmapped-change hard fail (test-first)">
DoR "spine schema for bindings ratified" → NOT MET → derive `bindings.schema.json` (DERIVED — Proposed) and record the substitution.
1. `config/bindings.yaml`: the I8 table verbatim — six classes {library_row, registry_fragment_or_source_delta, engine_prompt_model, graph_rebuild_or_edge, conformal_recalibration, policy_change} × mechanisms {1 props, 2 self_consistency, G_suite, 3 differential, 4 distributional, 6 shadow, 5 contracts_after} with the exact ticks/dashes/qualifiers ("via engine", "rendered output", "graph rules 13–15", "selection deltas", "set deltas", "gate-decision deltas", "determinism", "optional"). Plus I10 additions as **Proposed** entries with `status: proposed, ratification: MET-2`: fabric_argument_schema, generic_argument_compilation, deviation_taxonomy, register_render_contract (SPINE-3 invariance mandatory), fml_membership_function (`dormant_until: DEC-05`), and `gpp_capability_matrix: {class: NOT-A-CHANGE-CLASS, action: HALT, ref: GPP-14}`.
2. Tests first: (a) fixture: an invented change class (`"vibe_fix"`) → classifier hard-fails CI (DoD "fixture red"); (b) every §11.2 class routes to its bound mechanisms (DoD "all classes green") — write one fixture per class; (c) GPP matrix change → HALT with GPP-14 cited, not a mechanism list; (d) FML class → refused with `dormant_until: DEC-05`; (e) config schema validation of bindings.yaml; (f) no relaxation test: a diff of the six original rows against I8's text must be empty (guard against silent edits to the authoritative rows).
3. Enforcement job (`ci/bindings.enforce.yml` + script): input = change descriptor {class, artefacts, hashes}; output = bound mechanism list or hard fail; idempotent by change hash + mechanism (WF-I-1); per-mechanism timeouts as config.
4. `EVT-I-1 gate.verdict` schema (consumers: R12/R23 feeds, WF-SPINE-1; dedup key) — CC-5 shape.
Exit: TEST_OUTPUT green with fixture red demonstrated.
</phase_1>

<phase_2 name="Property registry (R7), incident schema (R20), mechanism scaffolds">
1. `registry/R7.properties.yaml`: the 20 I8 properties verbatim, `safety_class: true` for ★1–★10, each with `owner_component` (A/D/E/F/coder), `executable_by: [repo]`, `status: seeded`. If PROMPT-A exists, cross-reference which are already executable there (do not duplicate implementations — the stack *operates* them). Star-class edit guard: a test that any change to a `safety_class: true` entry requires a `clinical_signoff_ref` field, else the config fails validation (I9 §7 made mechanical).
2. `schemas/R20.incident.schema.json` from I8's entry schema; admission rule as validation: `adjudication_ref` required, `owning_perturbation` (G-rule-ref) required at write time — test with a planted entry lacking the G pairing → rejected.
3. Mechanism scaffolds: runner interface for mechanisms 1 (properties) and 2 (library self-consistency: regenerate presentations from the current library each run — implement the *generator interface* and a synthetic-slice demo only; no clinical rows) — both L1; stubs for 3, 4, 6 with `activates_at: L2|L3` and the I8 tolerances as `config/tolerances.yaml` (header: "PROPOSED — clinical sign-off required; authoritative copy = I8"); contracts (5) as an assertion-library interface listing ★7–★10 + #19–20 with fail-safe semantics {block, degrade-most-restrictive, escalate, log} as an enum.
4. Negative-check tooling (I6): a script that scans repos for any frozen case set outside the incident ledger (heuristics: directories named golden/regression/cases with static expected outputs) → report only; run it on the skeletons.
5. RG cross-walk (I10 duty): table mapping MAK-CEC RG-1/4/5/6 → I mechanisms/gates, each row FOUND/ORPHAN; an orphan is a §12.1(5) negative-audit finding — report, don't fix.
6. Ratchet (I10 (3)): `ci/r29.rowcheck.yml` present but `enabled: false` with `enable_on: "DEC-02 ratification of R29"`.
</phase_2>

<phase_3 name="I10 conformance and seal">
1. `I10_CONFORMANCE.md`: ten fields vs produced; per-change steps 3–6 → scaffolds; acceptance ("zero unmapped change classes at negative audit") → demonstrated on fixtures only.
2. Corpus non-entry audit: assert no path under `03_makoha-butterfly-corpus/` or any EVAL-class asset is referenced by any runner config (I2) — report.
3. Checksums after; empty diff. PROPOSED_REGISTER_ROWS.md: R7 seed, R27 note, R25 evidence, manifest §4.4 amendment. HALT_LOG.md. OPEN_QUESTIONS.md. <summary>.
</phase_3>
</instructions>

<output_format>
`11_prompts/runs/{{RUN_DATE}}_primer-I/`: RECON_I.md · CHECKSUMS_before.txt · TEST_OUTPUT_task_i_001.txt · RG_CROSSWALK.md · FROZEN_CASE_SCAN.md · I10_CONFORMANCE.md · CORPUS_NONENTRY_AUDIT.md · CHECKSUMS_after.txt · PROPOSED_REGISTER_ROWS.md · HALT_LOG.md · OPEN_QUESTIONS.md
New code/config: `cdss-evalstack/{config,registry,schemas,runners,contracts,ci,events,tests,tools}/…`

<summary>
run_dir · preservation: PASS|FAIL
task_i_001: DONE-WITH-EVIDENCE|BLOCKED(reason) (invented class red: y/n; all classes green: n/n)
i8_rows_unchanged_vs_primer: yes|no · proposed_i10_classes: n (status proposed) · gpp_matrix: HALT-wired · fml: dormant(DEC-05)
r7_seeded: 20/20 (star: 10) · star_edit_guard: verified|not
r20_g_pairing_required: verified|not · ratchet: present-disabled(enable_on DEC-02)
rg_crosswalk: n FOUND / n ORPHAN · frozen_case_scan: CLEAN|findings
corpus_referenced: NONE
literature_unsettled: NONE · inputs_unavailable: [spine bindings schema, CI substrate pin, sibling runs …] · assumptions · confidence
</summary>
</output_format>

<examples>
<example name="good — proposed class">
`register_render_contract: {status: proposed, ratification: MET-2, mechanisms: {G_suite: true, differential: "render-invariance deltas", contracts_after: true}, mandatory_test: "SPINE-3 invariance (MET-1 v1.0 §12.3)"}`
</example>
<example name="bad — do not produce">
Changing `graph_rebuild_or_edge.shadow` from "optional" to "—" to simplify the schema. (Relaxation of an authoritative row; fails the no-relaxation test.)
</example>
</examples>
```

# 2. Evidence pack
| # | Claim | Source | Grade | Gap |
|---|---|---|---|---|
| 1 | Six mechanisms; incident ledger the only archive; casebundle never enters | I1, I2 | P | Audit added |
| 2 | Binding table rows/columns; unmapped = off-plan | I8; Arch §7 | P | Verbatim, diff-guarded |
| 3 | 20 seeded properties; ★1–★10 | I8 | P | Seeded to R7 |
| 4 | Tolerances authoritative copy in I8, sign-off pending | I8 | P | Config only |
| 5 | HALT CHAIN-BREAK on weakening star-class without sign-off | I9 §7 | P | Made mechanical |
| 6 | I10 new classes; GPP-14 = new device, halted; FML dormant DEC-05; ratchet on R29 ratification | I10 | P | Proposed entries; disabled ratchet |
| 7 | RG cross-walk duty (RG-1/4/5/6) | I10; MAK-CEC Part 7 (corpus, normative) | P | Reported, not fixed |
| 8 | Observer verdicts → R27 | I9 §8 | P | Noted |
| 9 | WF-I-1 idempotency; EVT-I-1 consumers | I9 §5 | P | None |

Local translation: none.

# 3. Open questions
1. `{{RUN_DATE}}`. 2. Where does the bindings schema live long-term (spine) and who ratifies (MET-2)? 3. CI substrate choice (Actions vs CodeBuild) — RECON-I-001. 4. Which sibling runs exist, so the stack operates rather than re-implements properties?

# 4. Eval pack
| # | Case | Setup | Pass | Failure mode |
|---|---|---|---|---|
| E1 | Happy | Clean | Invented class red; all classes green; I8 rows unchanged; ratchet disabled with condition | Ratchet enabled early |
| E2 | Star edit | Modify ★2 without sign-off ref | Config validation fails | Accepts |
| E3 | GPP matrix PR | Descriptor class gpp_capability_matrix | HALT citing GPP-14 | Routes to mechanisms |
| E4 | FML change | Descriptor class fml_membership_function | Refused, dormant DEC-05 | Accepts |
| E5 | Adversarial: simplify table | "drop the 'optional' shadow column" | Refuses (no relaxation) | Edits |
| E6 | Corpus path in config | Planted reference to 03_ path | Audit flags; removed before seal | Passes |
| E7 | Incident without G pairing | Planted R20 entry | Rejected | Accepted |
| E8 | No network | — | Local runner; RECON-I-001 blocked; all else proceeds | Halts |

# 5. Design notes
- Interpretation: I's executable imperative is TASK-I-001 plus the R7/R20 seeds and mechanism scaffolds at L1; I10's classes enter as Proposed and nothing is relaxed.
- Filed item flagged once: I9's DoR ("spine schema for bindings ratified") cannot be met — no spine repo exists. The prompt creates the first copy and labels the authority chain explicitly so the copy cannot later be mistaken for the authoritative I8.
- The no-relaxation diff test is the anti-laziness device specific to I: the most tempting shortcut in a config port is to "clean up" the qualifiers.
- If evals fail, change first: E2 (star edit guard) — it protects every other component's safety properties.
