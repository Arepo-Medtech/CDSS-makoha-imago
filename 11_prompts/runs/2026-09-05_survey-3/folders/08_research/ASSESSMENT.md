# ASSESSMENT — 08_research (survey-3, Phase 2, 2026-09-05)

08_ = RESEARCH-1, RESEARCH-1.1, INDEX-08.

## 1. Items (3) — survey-2 label · sprint-1 / baseline status

| # | Path | Bytes | Label | Status |
|---|---|---|---|---|
| 1 | `08_research/INDEX.md` | 4680 | INDEX | built (sprint-1) |
| 2 | `08_research/RESEARCH-1.1_findings_delta.md` | 5357 | DELTA | built (sprint-1) |
| 3 | `08_research/RESEARCH-1_findings_gaps_source_map.md` | 3129 | RESEARCH | pre-existing (v1.2 seal / A-001..A-003) |

## 2. Folder lines (Q-F) — PASS / FAIL with evidence

| Q-F | Result | Evidence |
|---|---|---|
| Q-F-01 | **PASS** | INDEX-08 §1 |
| Q-F-02 | **PASS** | 3 files |
| Q-F-04 | **PASS** | closure path stated |
| Q-F-05 | **PASS** | RESEARCH-1.1 exemplary delta |

## 3. Items × Q-D lines

Mechanical lines from the Phase 0 tools (`tools/*.out.json`); hand lines (Q-D-08/09/11/12/13/14/17) cite the reading. `N/A` = line not applicable to the class; `EXEMPT` = Q-D-02 skeleton-stub rule.

### `08_research/INDEX.md`
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
| Q-D-15 | PASS | ASL 26.2 (≤35); FK 11.7 |
### `08_research/RESEARCH-1.1_findings_delta.md`
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
| Q-D-15 | PASS | ASL 18.3 (≤35); FK 8.5 |
### `08_research/RESEARCH-1_findings_gaps_source_map.md`
| Q-line | Result | Evidence |
|---|---|---|
| Q-D-01 | PASS | reachable from README via manifest/INDEX |
| Q-D-02 | PASS | graph class DESIGN-LINKED; inbound 13 |
| Q-D-03 | PASS | depth 1 |
| Q-D-04 | FAIL | missing ['status'] |
| Q-D-05 | PASS | unique or n/a |
| Q-D-06 | PASS | refcheck: 0 dead paths / 0 unresolved anchors tree-wide |
| Q-D-07 | PASS | ladder skips 0; tables 0 |
| Q-D-08 | FAIL (timeline) | RG rows: owner ✓, closes-into ✓ (1.1), trigger ✗ (QI-0022 OPTIMISATION) |
| Q-D-09 | PASS (via 1.1) | req_prefix RG declared by RESEARCH-1.1 |
| Q-D-10 | FAIL | prefix collision or label overlap (see L2_id_lifecycle) |
| Q-D-12 | FAIL | RG prefix collides with MAK-CEC RG-1..8 (QI-0024) |
| Q-D-15 | PASS | ASL 31.0 (≤35); FK 20.9 |

## 4. Severity and weight

Per v1.0 mapping (CRITICAL ≥4 · WARNING 3 · OPTIMISATION ≤2; weight = min(5, criticality + radius)); addends are in each row. Rows in `rows.jsonl`: 2.

## 5. Preliminary folder verdict (final in IMPECCABILITY_QUEUE §b after calibration)

BELOW-STANDARD only through the RG prefix collision (CHAIN WARNING) — otherwise IMPECCABLE; RG trigger column is OPTIMISATION

## 6. Exit

rows.jsonl: 2 rows (items 3 + applicable Q-F lines 4 → coverage: every item appears in ≥1 row: yes). Validation pasted in CHECKPOINT.md.

