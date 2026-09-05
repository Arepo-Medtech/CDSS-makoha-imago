DRAFT — ADVISORY_ONLY — not a claim — for T-G01 owner review

# The Governance Layer — intended purpose statement (DRAFT, assembled 2026-09-05 from language already present in MAK-GOV v0.9 and REG-POSTURE v1.2; every sentence carries its source; separate document from Mākoha's per NDG-1)

**Rule applied (MAK-GOV §4 `T-G01`):** "Write the Governance Layer intended purpose statement. Separate document from Mākoha's. State the subject of analysis as organisational conformance in the first sentence." `[src: MAK-GOV §4 Sprint G0 T-G01]`

## 1. First sentence (subject of analysis = organisational conformance)

"**The subject of analysis is the organisation, not the patient.** The Governance Layer analyses whether documented clinical decisions were justified against ratified guidelines, whether deviations were reasoned, whether queues are owned, whether instruments have gone stale. Its outputs describe *practice quality*. They do not describe a patient's condition, do not predict a patient's course, and are not returned to anyone making a decision about that patient's care." `[src: MAK-GOV §2.2]`

## 2. What it is
"A non-device first artifact: the auditor face shipped independently, analysing organisational conformance rather than patient state, with no clinical write path and no patient-specific recommendation — sold as clinical governance infrastructure while the classified track proceeds." `[src: MAK-GOV title block]` "This addendum does not build a new product. It ships an existing one separately." `[src: MAK-GOV §1]`

## 3. Boundaries the statement carries (enforced in code, not policy)
- "The Governance Layer is a separate build artifact with its own intended purpose statement, its own claims inventory, and its own repository." `[src: NDG-1]`
- "No output is patient-specific at the point of delivery." `[src: NDG-2]`
- "A minimum latency floor is enforced in code between an encounter and its availability for conformance review." `[src: NDG-3]` (value: DEC-15 / T-G04, open)
- "No prospective scoring." `[src: NDG-4]`
- "The differential engine, conformal wrapper, runtime LLM and any probability-bearing clinical inference are **structurally absent** from the artifact and its dependency graph — absent, not disabled." `[src: NDG-5]`
- "The first customers must therefore be practices with no Mākoha deployment at all." `[src: MAK-GOV §2.3 B-4]`

## 4. Regulatory status the statement must not overstate
"A **non-device line is available** beside the classified track … It is a finding about availability, **not** a classification: nothing ships before counsel attests (`ASSUME-REG-009`)." `[src: REG-POSTURE v1.2 §1.1 REG-FIND-013]` "Moderate, not high. The argument is well-founded but it is an argument, not a precedent." `[src: MAK-GOV §2.4]` "This ships nothing before counsel attests." `[src: MAK-GOV §2.4]`

## 5. What this draft does not do
It does not assert non-device status (counsel question 3; `Q-REG-010`; `TASK-REG-023`); it is attached to that question as context. It is not the claims inventory (`T-G05` / `NDG-9`). It names no customer, price or launch date.

## 6. Sentence census
Every quoted sentence was located by grep in `10_regulatory-execution/MAK-GOV_addendum-g_v0.9.md` or `REG-POSTURE_v1.2.md` on 2026-09-05; connective text makes no claim.
