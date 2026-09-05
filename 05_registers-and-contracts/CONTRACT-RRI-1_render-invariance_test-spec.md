---
doc_id: CONTRACT-RRI-1-TEST
title: "CONTRACT-RRI-1 — register-render invariance: runnable property-test specification"
version: "1.0"
date: "2026-09-05"
status: "Proposed (DEC-02). Companion to CONTRACT-ARG-1_argument_schema.md (RRI-1 paragraph, unedited). Specifies the test; implements nothing. Home on ratification: cdss-spine (contracts) with the test itself in cdss-fabric's suite and DEPLOY-2 §3 as the acceptance hook. No clinical content appears here."
companion_to: "05_registers-and-contracts/CONTRACT-ARG-1_argument_schema.md — CONTRACT-RRI-1"
grounding: "MAK-FFC SPINE-3 (renderers compress or re-order only; never add, remove or reweight) and SPINE-9 (projections derived, disposable, rebuildable); Primer L L10 (narration is a register renderer bound by SPINE-3); DEPLOY-2 §3 (automated diff across three faces; add/remove/reweight = hard failure)"
req_prefix: RRI
req_count: 4
---

# CONTRACT-RRI-1 — render-invariance test specification

## 1. The property

For any released ActualArgument `A` (CONTRACT-ARG-1.schema.json) and any two faces
`f1, f2 ∈ {clinician, patient, auditor}` with registers `r(f1), r(f2)`:

```
content-set(render(A, f1)) ≡ content-set(render(A, f2))   up to compression and ordering
```

where `content-set(·)` is the set of argument elements a rendering carries, each
element identified by its stable key in `A`:

| Element | Key in A | Weight-bearing attribute |
|---|---|---|
| claim | `claim.content` (+ each `claim.verbatim_fragment_refs[i]`) | — |
| ground | `grounds[i].coded_finding` | `grounds[i].provenance` |
| warrant | `warrant.ga_id@ga_version` | `warrant.applicability` |
| backing | `backing[i].source` | `backing[i].tier` |
| qualifier | `qualifier` (whole) | every `posterior_set[i].posterior`; `coverage_stated` |
| rebuttal | `rebuttals[i].content` | `rebuttals[i].source` |
| evaluation | `evaluation.evaluator_version` | each `gate_results[i].result`; `override_state` |

A rendering **passes** when its content-set equals the reference content-set and every
weight-bearing attribute is unchanged. Compression (fewer words, merged sentences) and
re-ordering are permitted. **Add, remove or reweight ⇒ test failure** (SPINE-3).

## 2. Requirements on the test harness

### RRI-1 (MUST)
**Statement:** The harness extracts the content-set from a rendering by the renderer's
declared element map (each renderer publishes which output span carries which key),
never by natural-language parsing of the rendered text.
**Rationale trace:** SPINE-3; DEPLOY-2 §3 ("automated diff"); Primer L L10 — an LLM
narration must declare its element map like any deterministic renderer.

### RRI-2 (MUST)
**Statement:** Inputs to every run are `A`, `f1`, `f2`; outputs are the two content-sets
and a three-part verdict {ADDED, REMOVED, REWEIGHTED} each an explicit (possibly empty)
list. The test passes only when all three lists are empty. A verdict without the three
lists is not a verdict.
**Rationale trace:** REG-POSTURE §0.4 DONE-WITH-EVIDENCE; MT2 §5 (outputs pasted, never
claimed).

### RRI-3 (MUST)
**Statement:** The property is run pairwise over all three faces (three pairs) for every
argument in the release fixture set, and as a G-class suite in CI (DEPLOY-2 §3 hard
failure). An LLM-narrated rendering enters the same run with no relaxation (L10).
**Rationale trace:** SPINE-3; SPINE-9 ("three truths" is the named failure mode);
MAK-MIF beat 8 (the LLM never holds the pen that signs).

### RRI-4 (SHOULD)
**Statement:** Fixtures are synthetic arguments built from CONTRACT-ARG-1.examples.jsonl
shapes; no fixture carries a clinical number, fragment text or case content.
**Rationale trace:** law 9 of the survey/prompt series (no clinical content authored by
executors); firewall note REG-POSTURE §0.6.

## 3. Worked examples (executable statements)

**Example 1 — PASS by compression.** `A` carries claim C, grounds {g1, g2}, qualifier
Q(coverage 0.9), rebuttals {r1}. Clinician render lists all four elements in full;
patient render states C in plain language, names g1 and g2 in one sentence, states Q as
"about 9 in 10 cases like this", and r1 as one clause. Content-sets equal; weights
equal; ordering differs. Verdict: ADDED=[], REMOVED=[], REWEIGHTED=[] → PASS.

**Example 2 — FAIL by removal.** Same `A`; patient render omits r1 "to avoid alarming
the patient". Verdict: REMOVED=[rebuttals[0]] → FAIL (SPINE-3: a renderer MUST NOT
remove argument content per audience; the correct move is compression, not omission).

**Example 3 — FAIL by reweighting (the LLM-narration case, L10).** Same `A`; the
narration capability renders Q as "very likely" for a posterior of 0.5 in `A`. The
renderer's element map binds "very likely" to `qualifier.posterior_set[0].posterior`;
the harness compares the mapped value class against `A` and finds a shift.
Verdict: REWEIGHTED=[qualifier.posterior_set[0]] → FAIL. The narration capability is
halted and an incident opened (Primer L L10 failure handling).

## 4. Acceptance hook

DEPLOY-2 §3 is the acceptance criterion; this specification is what that criterion
runs. HARDEN-3 W1 (T-003, CONTRACT-RRI-1) hardens this file against HARDEN-2 CC-7.

## 5. ID census and self-audit

Census: RRI-1..RRI-4 (4) = `req_count` 4 · MUST 3, SHOULD 1.
Self-audit (2026-09-05): (1) every requirement header matches `### RRI-n (MUST|SHOULD)` — PASS (4/4);
(2) every block carries a Rationale trace — PASS; (3) every cited ID (SPINE-3, SPINE-9,
L10, MT2 §5, REG-POSTURE §0.4/§0.6, DEPLOY-2 §3, T-003, CC-7, MAK-MIF beat 8) resolves
in the tree — PASS by grep; (4) no clinical number, fragment or case text — PASS.
