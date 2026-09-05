# Assumptions in scope — current statuses (verbatim from REG-POSTURE v1.2 §8 / REG-NZ v1.1 §9; nothing closed by this packet)

| ID | Assumption (verbatim) | Attesting party | Blocks | Status at 2026-09-05 |
|---|---|---|---|---|
| `ASSUME-REG-001` | Mākoha's device classification and applicable classification rule | AU regulatory counsel | `GATE-000` | OPEN |
| `ASSUME-REG-002` | CDSS exemption is unavailable to Mākoha (`REG-FIND-001` confirmed) | AU regulatory counsel | `GATE-000` | OPEN |
| `ASSUME-REG-003` | Patient surface treatment — separate product, non-decision-support, or in-scope. Interim rule: work beyond the J-3-safe subset is Blocked (DEC-07) | Counsel + product | `GATE-000` | OPEN |
| `ASSUME-REG-009` | The Governance Layer (MAK-GOV) is not a medical device under s41BD and is not an accessory to Mākoha (`REG-FIND-013`) | AU regulatory counsel | MAK-GOV `GATE-G0`; REG-SPRINT `SG-V1-0` (does not block `GATE-000`) | OPEN |
| `NZ-ASSUME-004` | Whether NZ clinical evidence will be accepted in an Australian conformity assessment, and on what conditions (expect: ISO 14155 conduct, HDEC approval, identical intended purpose) | AU counsel | Australian `GATE-003`; NZ evidence strategy | OPEN |

Closure rule (REG-POSTURE §0.4): an `ASSUME-REG-*` may hold only OPEN, ATTESTED, REFUTED or SUPERSEDED; closure requires written attestation from the named party with a date; if `ASSUME-REG-002` closes in favour of exemption, `REG-FIND-001` takes state REFUTED, not ATTESTED.
