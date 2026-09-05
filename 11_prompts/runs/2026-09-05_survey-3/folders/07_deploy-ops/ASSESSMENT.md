# ASSESSMENT — 07_deploy-ops (survey-3, Phase 2, 2026-09-05)

07_ = DEPLOY-1/2, GOV-1, OPS-1, SEC-1 (1 Sep), DEPLOY-1.1, OPS-1.1, SEC-2 (sprint-1), INDEX-07.

## 1. Items (9) — survey-2 label · sprint-1 / baseline status

| # | Path | Bytes | Label | Status |
|---|---|---|---|---|
| 1 | `07_deployment-and-operations/DEPLOY-1.1_run-map_delta.md` | 10334 | DELTA | built (sprint-1) |
| 2 | `07_deployment-and-operations/DEPLOY-1_deployment_plan_and_sequencing.md` | 3805 | DEPLOY / OPS / GOV / SEC | pre-existing (v1.2 seal / A-001..A-003) |
| 3 | `07_deployment-and-operations/DEPLOY-2_testing_verification_acceptance.md` | 1839 | DEPLOY / OPS / GOV / SEC | pre-existing (v1.2 seal / A-001..A-003) |
| 4 | `07_deployment-and-operations/GOV-1_ownership_governance_postdeploy.md` | 1518 | DEPLOY / OPS / GOV / SEC | pre-existing (v1.2 seal / A-001..A-003) |
| 5 | `07_deployment-and-operations/INDEX.md` | 7451 | INDEX | built (sprint-1) |
| 6 | `07_deployment-and-operations/OPS-1.1_procedures_cc5_delta.md` | 13837 | DELTA | built (sprint-1) |
| 7 | `07_deployment-and-operations/OPS-1_operating_procedures.md` | 2475 | DEPLOY / OPS / GOV / SEC | pre-existing (v1.2 seal / A-001..A-003) |
| 8 | `07_deployment-and-operations/SEC-1_security_privacy_compliance.md` | 2205 | DEPLOY / OPS / GOV / SEC | pre-existing (v1.2 seal / A-001..A-003) |
| 9 | `07_deployment-and-operations/SEC-2_threat-model_and_data-flow.md` | 14581 | DEPLOY / OPS / GOV / SEC | built (sprint-1) |

## 2. Folder lines (Q-F) — PASS / FAIL with evidence

| Q-F | Result | Evidence |
|---|---|---|
| Q-F-01 | **PASS** | INDEX-07 §1 |
| Q-F-02 | **PASS** | INDEX-07 §2 = 9 files |
| Q-F-03 | **PASS** | INDEX-07 §3 precedence; DR table |
| Q-F-04 | **PARTIAL** | person-level owners [NEEDS DEFINITION] (HUMAN-ONLY, survey-2) |
| Q-F-05 | **PASS** | ladder; deltas exemplary |

## 3. Items × Q-D lines

Mechanical lines from the Phase 0 tools (`tools/*.out.json`); hand lines (Q-D-08/09/11/12/13/14/17) cite the reading. `N/A` = line not applicable to the class; `EXEMPT` = Q-D-02 skeleton-stub rule.

### `07_deployment-and-operations/DEPLOY-1.1_run-map_delta.md`
| Q-line | Result | Evidence |
|---|---|---|
| Q-D-01 | PASS | reachable from README via manifest/INDEX |
| Q-D-02 | PASS | graph class DESIGN-LINKED; inbound 9 |
| Q-D-03 | PASS | depth 1 |
| Q-D-04 | PASS | core keys present |
| Q-D-05 | PASS | unique or n/a |
| Q-D-06 | PASS | refcheck: 0 dead paths / 0 unresolved anchors tree-wide |
| Q-D-07 | PASS | ladder skips 0; tables 0 |
| Q-D-10 | PASS/N/A | one padding form per family in this file |
| Q-D-15 | PASS | ASL 24.2 (≤35); FK 10.5 |
### `07_deployment-and-operations/DEPLOY-1_deployment_plan_and_sequencing.md`
| Q-line | Result | Evidence |
|---|---|---|
| Q-D-01 | PASS | reachable from README via manifest/INDEX |
| Q-D-02 | PASS | graph class DESIGN-LINKED; inbound 23 |
| Q-D-03 | PASS | depth 1 |
| Q-D-04 | FAIL | missing ['date'] |
| Q-D-05 | PASS | unique or n/a |
| Q-D-06 | PASS | refcheck: 0 dead paths / 0 unresolved anchors tree-wide |
| Q-D-07 | PASS | ladder skips 0; tables 0 |
| Q-D-10 | PASS/N/A | one padding form per family in this file |
| Q-D-15 | PASS | ASL 21.5 (≤35); FK 14.1 |
### `07_deployment-and-operations/DEPLOY-2_testing_verification_acceptance.md`
| Q-line | Result | Evidence |
|---|---|---|
| Q-D-01 | PASS | reachable from README via manifest/INDEX |
| Q-D-02 | PASS | graph class DESIGN-LINKED; inbound 21 |
| Q-D-03 | PASS | depth 1 |
| Q-D-04 | FAIL | missing ['date'] |
| Q-D-05 | PASS | unique or n/a |
| Q-D-06 | PASS | refcheck: 0 dead paths / 0 unresolved anchors tree-wide |
| Q-D-07 | PASS | ladder skips 0; tables 0 |
| Q-D-10 | PASS/N/A | one padding form per family in this file |
| Q-D-15 | PASS | ASL 19.8 (≤35); FK 12.8 |
### `07_deployment-and-operations/GOV-1_ownership_governance_postdeploy.md`
| Q-line | Result | Evidence |
|---|---|---|
| Q-D-01 | PASS | reachable from README via manifest/INDEX |
| Q-D-02 | PASS | graph class DESIGN-LINKED; inbound 10 |
| Q-D-03 | PASS | depth 1 |
| Q-D-04 | FAIL | missing ['date'] |
| Q-D-05 | PASS | unique or n/a |
| Q-D-06 | PASS | refcheck: 0 dead paths / 0 unresolved anchors tree-wide |
| Q-D-07 | PASS | ladder skips 0; tables 0 |
| Q-D-10 | PASS/N/A | one padding form per family in this file |
| Q-D-11 | PASS (role level) | owners per role; persons [NEEDS DEFINITION] → BSQ-0405/DEC-23 (HUMAN-ONLY, not re-filed) |
| Q-D-15 | FAIL | ASL 57.7 (QI-0036) |
### `07_deployment-and-operations/INDEX.md`
| Q-line | Result | Evidence |
|---|---|---|
| Q-D-01 | PASS | reachable from README via manifest/INDEX |
| Q-D-02 | PASS | graph class DESIGN-LINKED; inbound 3 |
| Q-D-03 | PASS | depth 1 |
| Q-D-04 | PASS | core keys present |
| Q-D-05 | PASS | unique or n/a |
| Q-D-06 | PASS | refcheck: 0 dead paths / 0 unresolved anchors tree-wide |
| Q-D-07 | PASS | ladder skips 0; tables 0 |
| Q-D-10 | PASS/N/A | one padding form per family in this file |
| Q-D-15 | PASS | ASL 25.8 (≤35); FK 12.5 |
### `07_deployment-and-operations/OPS-1.1_procedures_cc5_delta.md`
| Q-line | Result | Evidence |
|---|---|---|
| Q-D-01 | PASS | reachable from README via manifest/INDEX |
| Q-D-02 | PASS | graph class DESIGN-LINKED; inbound 7 |
| Q-D-03 | PASS | depth 1 |
| Q-D-04 | PASS | core keys present |
| Q-D-05 | PASS | unique or n/a |
| Q-D-06 | PASS | refcheck: 0 dead paths / 0 unresolved anchors tree-wide |
| Q-D-07 | PASS | ladder skips 0; tables 0 |
| Q-D-10 | PASS/N/A | one padding form per family in this file |
| Q-D-15 | PASS | ASL 13.7 (≤35); FK 8.5 |
### `07_deployment-and-operations/OPS-1_operating_procedures.md`
| Q-line | Result | Evidence |
|---|---|---|
| Q-D-01 | PASS | reachable from README via manifest/INDEX |
| Q-D-02 | PASS | graph class DESIGN-LINKED; inbound 16 |
| Q-D-03 | PASS | depth 1 |
| Q-D-04 | FAIL | missing ['date'] |
| Q-D-05 | PASS | unique or n/a |
| Q-D-06 | PASS | refcheck: 0 dead paths / 0 unresolved anchors tree-wide |
| Q-D-07 | PASS | ladder skips 0; tables 0 |
| Q-D-10 | PASS/N/A | one padding form per family in this file |
| Q-D-15 | PASS | ASL 24.8 (≤35); FK 16.0 |
### `07_deployment-and-operations/SEC-1_security_privacy_compliance.md`
| Q-line | Result | Evidence |
|---|---|---|
| Q-D-01 | PASS | reachable from README via manifest/INDEX |
| Q-D-02 | PASS | graph class DESIGN-LINKED; inbound 15 |
| Q-D-03 | PASS | depth 1 |
| Q-D-04 | FAIL | missing ['date'] |
| Q-D-05 | PASS | unique or n/a |
| Q-D-06 | PASS | refcheck: 0 dead paths / 0 unresolved anchors tree-wide |
| Q-D-07 | PASS | ladder skips 0; tables 0 |
| Q-D-10 | PASS/N/A | one padding form per family in this file |
| Q-D-11 | PASS (via INDEX-07 §4 + SEC-2) | 'no new claims' status |
| Q-D-15 | FAIL | ASL 81.3 (QI-0033) |
### `07_deployment-and-operations/SEC-2_threat-model_and_data-flow.md`
| Q-line | Result | Evidence |
|---|---|---|
| Q-D-01 | PASS | reachable from README via manifest/INDEX |
| Q-D-02 | PASS | graph class DESIGN-LINKED; inbound 7 |
| Q-D-03 | PASS | depth 1 |
| Q-D-04 | PASS | core keys present |
| Q-D-05 | PASS | unique or n/a |
| Q-D-06 | PASS | refcheck: 0 dead paths / 0 unresolved anchors tree-wide |
| Q-D-07 | PASS | ladder skips 0; tables 0 |
| Q-D-08 | FAIL | TM rows lack owner/verification/home (QI-0021) |
| Q-D-09 | PASS/FAIL | declared TM/18; no register home |
| Q-D-10 | PASS/N/A | one padding form per family in this file |
| Q-D-11 | PASS | status; owner Security owner [NEEDS DEFINITION] |
| Q-D-15 | PASS | ASL 21.6 (≤35); FK 11.7 |

## 4. Severity and weight

Per v1.0 mapping (CRITICAL ≥4 · WARNING 3 · OPTIMISATION ≤2; weight = min(5, criticality + radius)); addends are in each row. Rows in `rows.jsonl`: 8.

## 5. Preliminary folder verdict (final in IMPECCABILITY_QUEUE §b after calibration)

BELOW-STANDARD — 1 WARNING (SEC-2 TM owner/verification cells, QI-0019) + readability OPTIMISATION (SEC-1, GOV-1); remedy SEC-2.1

## 6. Exit

rows.jsonl: 8 rows (items 9 + applicable Q-F lines 5 → coverage: every item appears in ≥1 row: yes). Validation pasted in CHECKPOINT.md.

