# ASSESSMENT — 04_hardening (survey-3, Phase 2, 2026-09-05)

04_ = MT2 (retained), HARDEN-1/1.1, HARDEN-2/2.1, HARDEN-3/3.1, INDEX-04.

## 1. Items (8) — survey-2 label · sprint-1 / baseline status

| # | Path | Bytes | Label | Status |
|---|---|---|---|---|
| 1 | `04_hardening/HARDEN-1.1_coverage_ledger_seed_delta.md` | 51782 | DELTA | built (sprint-1) |
| 2 | `04_hardening/HARDEN-1_coverage_ledger_seed.md` | 3517 | SEED / LEDGER | pre-existing (v1.2 seal / A-001..A-003) |
| 3 | `04_hardening/HARDEN-2.1_spec_census_and_self-audit_delta.md` | 8836 | DELTA | built (sprint-1) |
| 4 | `04_hardening/HARDEN-2_hardening_spec.md` | 4572 | SPEC | pre-existing (v1.2 seal / A-001..A-003) |
| 5 | `04_hardening/HARDEN-3.1_task_register_delta.md` | 134486 | DELTA | built (sprint-1) |
| 6 | `04_hardening/HARDEN-3_hardening_plan_worklist.md` | 2558 | WORKLIST/PLAN | pre-existing (v1.2 seal / A-001..A-003) |
| 7 | `04_hardening/INDEX.md` | 7701 | INDEX | built (sprint-1) |
| 8 | `04_hardening/MAJOR_TASK_2_anti-laziness-hardening-directive.md` | 16194 | DIRECTIVE (retained verbatim) | retained (verbatim) |

## 2. Folder lines (Q-F) — PASS / FAIL with evidence

| Q-F | Result | Evidence |
|---|---|---|
| Q-F-01 | **PASS** | INDEX-04 §1 |
| Q-F-02 | **PASS** | INDEX-04 §2 = 8 files |
| Q-F-03 | **PASS** | PROMPT-HARDEN named (decision-gated) |
| Q-F-04 | **PASS** | INDEX-04 §4 |
| Q-F-05 | **PASS** | ladder; deltas exemplary |

## 3. Items × Q-D lines

Mechanical lines from the Phase 0 tools (`tools/*.out.json`); hand lines (Q-D-08/09/11/12/13/14/17) cite the reading. `N/A` = line not applicable to the class; `EXEMPT` = Q-D-02 skeleton-stub rule.

### `04_hardening/HARDEN-1.1_coverage_ledger_seed_delta.md`
| Q-line | Result | Evidence |
|---|---|---|
| Q-D-01 | PASS | reachable from README via manifest/INDEX |
| Q-D-02 | PASS | graph class DESIGN-LINKED; inbound 14 |
| Q-D-03 | PASS | depth 1 |
| Q-D-04 | PASS | core keys present |
| Q-D-05 | PASS | unique or n/a |
| Q-D-06 | PASS | refcheck: 0 dead paths / 0 unresolved anchors tree-wide |
| Q-D-07 | PASS | ladder skips 0; tables 0 |
| Q-D-08 | N/A | ledger |
| Q-D-09 | PASS | req_prefix R29-row / 275; census; owner column |
| Q-D-10 | PASS/N/A | one padding form per family in this file |
| Q-D-11 | PASS | change_policy; status |
| Q-D-15 | PASS | ASL 27.6 (≤35); FK 12.4 |
| Q-D-17 | PASS | exemplar |
### `04_hardening/HARDEN-1_coverage_ledger_seed.md`
| Q-line | Result | Evidence |
|---|---|---|
| Q-D-01 | PASS | reachable from README via manifest/INDEX |
| Q-D-02 | PASS | graph class DESIGN-LINKED; inbound 37 |
| Q-D-03 | PASS | depth 1 |
| Q-D-04 | PASS | core keys present |
| Q-D-05 | PASS | unique or n/a |
| Q-D-06 | PASS | refcheck: 0 dead paths / 0 unresolved anchors tree-wide |
| Q-D-07 | PASS | ladder skips 0; tables 0 |
| Q-D-10 | PASS/N/A | one padding form per family in this file |
| Q-D-15 | PASS | ASL 19.8 (≤35); FK 12.5 |
### `04_hardening/HARDEN-2.1_spec_census_and_self-audit_delta.md`
| Q-line | Result | Evidence |
|---|---|---|
| Q-D-01 | PASS | reachable from README via manifest/INDEX |
| Q-D-02 | PASS | graph class DESIGN-LINKED; inbound 5 |
| Q-D-03 | PASS | depth 1 |
| Q-D-04 | PASS | core keys present |
| Q-D-05 | PASS | unique or n/a |
| Q-D-06 | PASS | refcheck: 0 dead paths / 0 unresolved anchors tree-wide |
| Q-D-07 | PASS | ladder skips 0; tables 0 |
| Q-D-10 | FAIL | prefix collision or label overlap (see L2_id_lifecycle) |
| Q-D-15 | PASS | ASL 25.9 (≤35); FK 12.5 |
### `04_hardening/HARDEN-2_hardening_spec.md`
| Q-line | Result | Evidence |
|---|---|---|
| Q-D-01 | PASS | reachable from README via manifest/INDEX |
| Q-D-02 | PASS | graph class DESIGN-LINKED; inbound 20 |
| Q-D-03 | PASS | depth 1 |
| Q-D-04 | PASS | core keys present |
| Q-D-05 | PASS | unique or n/a |
| Q-D-06 | PASS | refcheck: 0 dead paths / 0 unresolved anchors tree-wide |
| Q-D-07 | PASS | ladder skips 0; tables 0 |
| Q-D-09 | PASS (via 2.1) | CC declared and censused by HARDEN-2.1 |
| Q-D-10 | FAIL | prefix collision or label overlap (see L2_id_lifecycle) |
| Q-D-11 | PASS | status 'Proposed — this SPEC is itself an artifact…' |
| Q-D-12 | FAIL | CC prefix collides with MAK-LBP CC-1..5 (QI-0025) |
| Q-D-15 | PASS | ASL 32.2 (≤35); FK 20.4 |
### `04_hardening/HARDEN-3.1_task_register_delta.md`
| Q-line | Result | Evidence |
|---|---|---|
| Q-D-01 | PASS | reachable from README via manifest/INDEX |
| Q-D-02 | PASS | graph class DESIGN-LINKED; inbound 15 |
| Q-D-03 | PASS | depth 1 |
| Q-D-04 | PASS | core keys present |
| Q-D-05 | PASS | unique or n/a |
| Q-D-06 | PASS | refcheck: 0 dead paths / 0 unresolved anchors tree-wide |
| Q-D-07 | PASS | ladder skips 0; tables 0 |
| Q-D-08 | PASS | 276/276 owner + exit evidence (QI-0053 exemplar) |
| Q-D-09 | PASS | req_prefix T / 276; census; R29 on DEC-02 |
| Q-D-10 | PASS/N/A | one padding form per family in this file |
| Q-D-11 | PASS | supersedes/applies_to/change_policy; status honesty |
| Q-D-15 | FAIL | ASL 37.7 (≤35); FK 16.9 |
| Q-D-17 | PASS | delta form exemplar |
### `04_hardening/HARDEN-3_hardening_plan_worklist.md`
| Q-line | Result | Evidence |
|---|---|---|
| Q-D-01 | PASS | reachable from README via manifest/INDEX |
| Q-D-02 | PASS | graph class DESIGN-LINKED; inbound 33 |
| Q-D-03 | PASS | depth 1 |
| Q-D-04 | PASS | core keys present |
| Q-D-05 | PASS | unique or n/a |
| Q-D-06 | PASS | refcheck: 0 dead paths / 0 unresolved anchors tree-wide |
| Q-D-07 | PASS | ladder skips 0; tables 0 |
| Q-D-10 | FAIL | prefix collision or label overlap (see L2_id_lifecycle) |
| Q-D-15 | N/A | <50 prose words |
### `04_hardening/INDEX.md`
| Q-line | Result | Evidence |
|---|---|---|
| Q-D-01 | PASS | reachable from README via manifest/INDEX |
| Q-D-02 | PASS | graph class DESIGN-LINKED; inbound 4 |
| Q-D-03 | PASS | depth 1 |
| Q-D-04 | PASS | core keys present |
| Q-D-05 | PASS | unique or n/a |
| Q-D-06 | PASS | refcheck: 0 dead paths / 0 unresolved anchors tree-wide |
| Q-D-07 | PASS | ladder skips 0; tables 0 |
| Q-D-10 | PASS/N/A | one padding form per family in this file |
| Q-D-15 | PASS | ASL 22.6 (≤35); FK 10.7 |
### `04_hardening/MAJOR_TASK_2_anti-laziness-hardening-directive.md`
| Q-line | Result | Evidence |
|---|---|---|
| Q-D-01 | PASS | reachable from README via manifest/INDEX |
| Q-D-02 | PASS | graph class DESIGN-LINKED; inbound 10 |
| Q-D-03 | PASS | depth 1 |
| Q-D-04 | N/A (judged on parent, P-F-02) | retained-original |
| Q-D-05 | PASS | unique or n/a |
| Q-D-06 | PASS | refcheck: 0 dead paths / 0 unresolved anchors tree-wide |
| Q-D-10 | PASS/N/A | one padding form per family in this file |
| Q-D-11 | PASS (via INDEX-04 §3) | retained verbatim; retention note in INDEX |
| Q-D-15 | PASS | ASL 17.5 (≤35); FK 11.5 |
| Q-D-17 | N/A | retained; judged on companion set (law 5) |

## 4. Severity and weight

Per v1.0 mapping (CRITICAL ≥4 · WARNING 3 · OPTIMISATION ≤2; weight = min(5, criticality + radius)); addends are in each row. Rows in `rows.jsonl`: 6.

## 5. Preliminary folder verdict (final in IMPECCABILITY_QUEUE §b after calibration)

IMPECCABLE-WITH-DECISIONS-PENDING — no folder-level defect; the CC prefix collision is a CHAIN row with an alias-law draft; DEC-02/10/11 pending

## 6. Exit

rows.jsonl: 6 rows (items 8 + applicable Q-F lines 5 → coverage: every item appears in ≥1 row: yes). Validation pasted in CHECKPOINT.md.

