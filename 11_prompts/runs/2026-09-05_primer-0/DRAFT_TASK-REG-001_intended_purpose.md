DRAFT — ADVISORY_ONLY — not a claim — for TASK-REG-001 owner review

# Mākoha — intended purpose statement (DRAFT, assembled 2026-09-05 from language already present in REG-POSTURE v1.2; every sentence carries its source; no new product claim is minted — OBL-014 / NDG-9 / EX-9 claims discipline)

**Rule applied (REG-POSTURE v1.2 §7 `TASK-REG-001`):** "Write the intended purpose statement. One document, one claim. Everything downstream depends on it. Include the three surfaces explicitly and what each does." `[src: REG-POSTURE_v1.2.md §7 TASK-REG-001]`

## 1. The one claim (candidate wording — assembled, not authored)

Mākoha is "Software as a medical device, providing diagnostic information." `[src: §4.1]` It is "a Bayesian differential-diagnosis engine" `[src: §1]` that produces "a ranked differential with posteriors" `[src: §1.1 REG-FIND-002]` for registered health professionals, under a "deterministic release path" `[src: §3.2 REG-KEEP-001]` with a "reviewable basis for every output" `[src: §3.2 REG-KEEP-002]` and "human sign-off, fail-closed" `[src: §3.2 REG-KEEP-003]`.

## 2. Regulatory frame the statement must sit inside

- "Build to SaMD standard. Test exemption honestly at a named gate. Assume inclusion." `[src: §3]`
- "Mākoha is assessed as **not eligible** for the CDSS exemption. The disqualifier is the diagnostic function, not the use of AI." `[src: §1.1 REG-FIND-001]` — status OPEN; closes only via `ASSUME-REG-002`.
- "Under the software classification rules introduced in February 2021, diagnostic SaMD classification depends on the seriousness of the condition and the role of the information. Expect Class IIa at minimum; Class IIb is plausible where output bears on serious conditions. This requires counsel (`ASSUME-REG-001`)". `[src: §4.1]`
- "Synthetic-only until controls operate" — "Explicitly **not** a validation-evidence commitment". `[src: §3.2 REG-KEEP-004]`

## 3. The three surfaces (explicit, per TASK-REG-001)

| Surface | What it does — in words already on record | Source |
|---|---|---|
| Clinician surface | receives the differential and its reviewable basis; "human sign-off, fail-closed" | `[src: §3.2 REG-KEEP-002/003]`; usability "three surfaces (clinician, pharmacist, patient), three use-related risk analyses (`TASK-REG-014`)" `[src: §4.3.1 STD-004]` |
| Pharmacist surface | same device, pharmacy wedge: "for an Australian-first product with a pharmacy wedge" | `[src: §4.2]`; `[src: §4.3.1 STD-004]` |
| Patient surface | **undecided**: "Patient surface treatment — separate product, non-decision-support, or in-scope. Interim rule: work beyond the J-3-safe subset is Blocked (DEC-07)" | `[src: §8 ASSUME-REG-003]`; `[src: §7 interim rule]` |

The patient-surface row is a placeholder by law: the statement cannot fix the patient surface until `ASSUME-REG-003` / DEC-07 closes (`Q-REG-003`, counsel question 4).

## 4. What this draft does not do
It does not decide classification (`ASSUME-REG-001`), exemption (`ASSUME-REG-002`), the patient surface (`ASSUME-REG-003`) or the conformity route (`ASSUME-REG-005`). It restates no clinical content (§0.6 firewall note). It is not the claims inventory (`OBL-014`; `TASK-REG-003`) — that inventory is diffed against this statement once the owner adopts it.

## 5. Sentence census
Every quoted sentence above was located by grep in `10_regulatory-execution/REG-POSTURE_v1.2.md` on 2026-09-05; no sentence originates in this draft except the connective text, which makes no claim.
