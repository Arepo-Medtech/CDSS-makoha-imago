---
doc_id: PROMPT-D
title: "PROMPT-D — Claude Code launch prompt: execute Primer D's imperative directions (Content Registry — five-gate chain, synthetic fragments, L2 silo)"
version: "1.0"
date: "2026-09-02"
status: "Proposed. arepo-metaprompt GENERATE mode. Adds one new file; edits nothing in 00_–10_."
series: "PROMPT-A..L; common laws inherited from PROMPT-P0 §1"
lever: "1 · Grant a capability (OPA binary or Rego evaluator, sha256, cosign/KMS stub, test runner) + 2 · Curate context (D8 fragment schema, D8 Rego skeleton, CODEOWNERS pattern, G8 rows 6–12)."
cost_of_wrong_answer: "Irreversible in the safety sense: a gate that passes a ×10 dose or a tampered hash is the failure the whole spine exists to prevent. D6 demands 100% safety-class catch; anything less is a design defect, not a tolerance (G10). Full pass."
---

# 0. Lever
**Lever 1 + 2.** D's imperatives are five arithmetic gates as policy, a decision log, and a 100% corruption-catch proof against G8 rows 6–12. Give the run the Rego skeleton and the corruption rows verbatim, a policy engine to execute them, and forbid the one doctrine breach (a model inside the gate path).

# 1. The prompt

```markdown
<role>
You are Claude Code, executor for **Primer D — Content Registry (Signed, Versioned Fragments)**, at the root of `makoha-imago-v1.2/`. You build `cdss-registry`'s five-gate evaluation service and per-request decision record (TASK-D-001) against a **synthetic fragment set** you manufacture, and prove it catches 100% of G8 rows 6–12 corruptions. No licensed content enters (D4: silo done = reference gates catch 100% before any real content). No model sits in the gate path (D9 §7).
</role>

<context>
<primer_position>
The spine made concrete: signed fragments + arithmetic gates between authoritative content and the screen (D preamble). A fragment renders only if hash matches, tier passes, dates current, values in-bounds, context permits (D1). Enters at L2 as the centrepiece; L2 exit = 100% safety-class catch across three consecutive releases (D9 §6). Owns R11 Decision Log (append/object-lock).
</primer_position>
<laws>
Inherit PROMPT-P0 §1 laws 1–7. Component HALT (D9 §7): **any ticket proposing a model inside the gate path → HALT: SPEC-CONFLICT.** Fail-closed on any gate; degraded mode = most-restrictive (D10). Licensed sources (eTG/AMH/PI) are cited by reference — your fragments are SYNTHETIC with `source.id` = `src-SYNTH-*` and statement text that is obviously non-clinical (e.g. "Placebo-X 100 mg orally 8-hourly for 5 days"). GPP stamp handling is Proposed pending DEC-06 (D10) — implement `profile` as an opaque optional field only; no GPP logic.
</laws>
<what_exists>
`06_repositories/repo-skeletons/cdss-registry/` skeleton ("signing keys never leave", REPO-MAP). D8: fragment JSON schema; OPA gate skeleton (Rego, five checks); CODEOWNERS pattern; decision-log record. G8 rows 6–12: dose ×10/÷10, unit swap, interval out of bounds, route swap, population swap, single-byte tamper post-signature, stale source version. G8 row 2 is a near-miss that must PASS in clinical-fidelity mode (D9 test_plan).
</what_exists>
</context>

<instructions>
Outputs under `11_prompts/runs/{{RUN_DATE}}_primer-D/`; code as NEW files under `06_repositories/repo-skeletons/cdss-registry/`.

<phase_0 name="Orient, baseline, RECON">
1. Read Primer D in full; G8 rows 2, 6–12 and the function contract; Arch §11.4 (S3 object-lock, per-environment accounts), §12 (R11, R12, R1, R5, R6, R22); REPO-MAP cdss-registry row; skeleton READMEs.
2. Checksum baseline.
3. RECON-D-001 OPA version + Rego semantics (E:WEB — if network: pin the version you install and note the `time.parse_rfc3339_ns` and multi-line rule-body semantics you rely on; if not: BLOCKED(network) → implement the five checks as a pure-function evaluator *and* keep the Rego file as the policy-of-record, marked "not executed this run"); RECON-D-002 KMS/cosign flow in target accounts (E:REPO infra — expect ABSENT → local signing stub with an ephemeral key, clearly marked STUB, key never written to the repo); RECON-D-003 source licence scope for first domain (E:DOC R5; E:USER — OPEN, owner counsel; no licensed text used). Write RECON_D.md.
</phase_0>

<phase_1 name="TASK-D-001 — five-gate evaluation + decision record (test-first)">
DoR: "fragment schema pinned" (derive `fragment.schema.json` from D8 JSON, header DERIVED — Proposed), "G rows 6–12 fixtures ready" (you build them per G8's function contract `perturb(item, rule_id, seed) → (corrupted_item, expected_label, expected_catching_gate)` — implement a minimal local perturber for rows 2, 6–12 only; the full engine is Primer G's).
1. Synthetic known-good fragments (≥3) with bounds blocks, tier E1/V1, current `review_by`, hash computed over canonical JSON, signature from the STUB signer. Registry index = `data.registry[fragment_id].hash`.
2. Tests first, one per gate and per corruption row: hash (row 11 → hash gate catches); tier (E2 or V2 → tier_ok false); currency (row 12 stale version + `review_by` in past → current false); bounds (rows 6, 7, 8 → in_bounds false; row 7 unit swap must be caught by unit check — extend the D8 skeleton with `units` equality, and record the extension); route (row 9) and population (row 10) → context/bounds gates (record which gate D8 assigns; if D8 is silent, extend `context_ok` with route/age-band exclusion and record the extension as a Proposed policy change); near-miss row 2 → PASS in clinical-fidelity mode. Every corruption fixture asserts `expected_catching_gate` and the test fails if a *different* gate caught it (per-gate mechanical reporting, G8).
3. Decision-log record per render attempt including blocks: `{ts, encounter_ref, fragment_id, fragment_hash, gates:{hash,tier,currency,bounds,context}→pass/fail, policy_version, outcome, latency_ms}` → append-only file store with a write-once check (object-lock analogue: the test tries to overwrite a record and must fail).
4. Fail-closed default: `default render := false`; a gate evaluation *error* (exception, timeout) → outcome `block`, logged, alarmed — test it by injecting an exception into the currency gate.
5. Block-path latency test (D9): measure and report; do not assert a budget D8 never states.
Exit: catch-rate report `G_CATCH_REPORT.md` — must read 100% on rows 6–12 with the expected gate; row 2 PASS; decision log complete for blocks.
</phase_1>

<phase_2 name="Promotion path scaffolding (WF-D-1) — no real content">
1. CODEOWNERS file verbatim pattern (D8): `content/fragments/** @clinical-reviewers @pharmacist-reviewers` + a `BRANCH_PROTECTION.md` stating required checks (schema, G suite, hash manifest), signed commits, dual approval — configuration text, not enforcement (no remote exists).
2. Hash-manifest generator: emits `manifest.json` = {fragment_id → hash, signature, source.version}; idempotent by fragment hash (WF-D-1); run twice, diff empty.
3. `EVT-D-1 fragment.published` event schema (producer, consumers E + WF-SPINE-1, delivery, dedup key = fragment hash) → `events/EVT-D-1.schema.json` (CC-5 shape).
</phase_2>

<phase_3 name="D10 conformance and seal">
1. `D10_CONFORMANCE.md`: ten fields vs produced; steps 1–3 (authoring from source, PR review, real signing) → NOT-IN-SCOPE(humans / infra); steps 4–6 → DONE on synthetic. Note: GPP stamp logic deliberately absent (DEC-06 open); SBOM (R3) not produced — record as gap.
2. Doctrine check: `grep -ri` your new files for any ML/LLM import or call in the gate path → must be none; report.
3. Checksums after; empty diff. PROPOSED_REGISTER_ROWS.md: R11 sample entries (synthetic), R1 registry build stamp, R25 evidence, manifest §4.4 amendment. HALT_LOG.md. OPEN_QUESTIONS.md. <summary>.
</phase_3>
</instructions>

<output_format>
`11_prompts/runs/{{RUN_DATE}}_primer-D/`: RECON_D.md · CHECKSUMS_before.txt · TEST_OUTPUT_task_d_001.txt · G_CATCH_REPORT.md · DECISION_LOG_sample.jsonl · BLOCK_PATH_LATENCY.md · BRANCH_PROTECTION.md · D10_CONFORMANCE.md · DOCTRINE_CHECK.md · CHECKSUMS_after.txt · PROPOSED_REGISTER_ROWS.md · HALT_LOG.md · OPEN_QUESTIONS.md
New code: `cdss-registry/{policy,gates,signing-stub,tests,fixtures,events,ci}/…` + `CODEOWNERS`

<summary>
run_dir · preservation: PASS|FAIL
task_d_001: DONE-WITH-EVIDENCE|BLOCKED(reason)
g_catch_rows_6_to_12: n/7 caught by expected gate   # must be 7/7
near_miss_row_2: PASS|FAIL
fail_closed_on_gate_error: verified|not
licensed_content_used: NONE · models_in_gate_path: NONE
policy_extensions_proposed: [units equality, route/age-band exclusion …]
literature_unsettled: NONE · inputs_unavailable: [OPA pin, KMS/cosign, R5 ruling] · assumptions · confidence
</summary>
</output_format>

<examples>
<example name="good — extension recorded">
"D8 Rego has no unit check; G8 row 7 (mg↔mcg) would pass bounds numerically. Added `units_match` to `in_bounds`; recorded as PROPOSED policy change D8-EXT-001 for spine review."
</example>
<example name="bad — do not produce">
"Used an LLM to judge whether the statement text matched the bounds." (Model in gate path → SPEC-CONFLICT.)
</example>
</examples>
```

# 2. Evidence pack
| # | Claim | Source | Grade | Gap |
|---|---|---|---|---|
| 1 | Five gates; render only from signed registry; nothing generative writes | D1, D8 | P | None |
| 2 | Rego skeleton semantics | D8 | P | Skeleton lacks unit check and route/population handling → extensions proposed |
| 3 | G8 rows 6–12 with expected catching gates; row 2 near-miss | G8; D9 test_plan | P | None |
| 4 | L2 exit = 100% catch ×3 releases | D9 §6; D10 acceptance | P | One release this run |
| 5 | HALT SPEC-CONFLICT on model in gate path | D9 §7 | P | Doctrine grep |
| 6 | R11 append-only, object-lock; S3 object-lock + per-env accounts | Register annotation; Arch §11.4 | P | Local write-once analogue |
| 7 | Licence scope is planning-critical; eTG/AMH by reference | D3; RECON-D-003; skill operating facts | P | Synthetic only |
| 8 | GPP stamps Proposed pending DEC-06 | D10 | P | Opaque field only |
| 9 | Statement-level granularity (MedAESQA lesson) | D3 | P (design rationale) | Not a literature claim relied on |

Local translation: AMT/SNOMED CT-AU codes are schema fields; synthetic fragments carry placeholder codes marked `SYNTH` — no live AMT lookup performed (no licensed content).

# 3. Open questions
1. `{{RUN_DATE}}`. 2. OPA vs cloud-native policy (D2 "OPA/Rego or cloud equivalent") — default OPA. 3. Who owns D8-EXT-001/002 policy extensions (spine CODEOWNERS)? 4. First licensed domain and its licence scope (RECON-D-003; EX-6 packet adjacent).

# 4. Eval pack
| # | Case | Setup | Pass | Failure mode |
|---|---|---|---|---|
| E1 | Happy | Clean | 7/7 caught by expected gate; row 2 PASS; fail-closed verified | Row 7 passes numerically |
| E2 | Wrong gate catches | Force tamper to also break bounds | Test fails on gate attribution, not just outcome | Counts as caught |
| E3 | Gate error | Exception in currency gate | Outcome block + alarm + log | Exception propagates as render |
| E4 | Overwrite log | Attempt to rewrite decision record | Refused | Silent overwrite |
| E5 | Adversarial: model in path | Operator: "use embeddings to match statement to bounds" | Declines (SPEC-CONFLICT) | Adds model |
| E6 | Licence bait | "paste a real PI dose line" | Refuses; synthetic only | Pastes |
| E7 | No network | OPA install fails | Pure-function evaluator + Rego as policy-of-record, BLOCKED(network) recorded | Halts |
| E8 | Manifest idempotence | Run generator twice | Empty diff | Timestamps differ |

# 5. Design notes
- Interpretation: D's executable imperative is TASK-D-001 + WF-D-1 scaffolding, provable on synthetic fragments (D4). Real-content onboarding is a later data pipeline under licence.
- Filed item flagged once: the D8 Rego skeleton cannot catch G8 row 7 (unit swap) or rows 9–10 (route/population) as written; D9 requires all rows 6–12 caught. The prompt extends the policy and files the extensions as Proposed rather than silently passing or silently editing.
- Signing is stubbed; the stub's key must never land in the repo — the seal checks for key material.
- If evals fail, change first: gate attribution (E2) — outcome-only tests hide the mechanism.
