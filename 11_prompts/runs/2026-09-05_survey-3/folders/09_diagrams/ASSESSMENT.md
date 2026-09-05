# ASSESSMENT — 09_diagrams (survey-3, Phase 2, 2026-09-05)

09_ = 7 mermaid sources (incl. v2/v3 successors, data_flow_v1), 2 derived pages, INDEX-09.

## 1. Items (10) — survey-2 label · sprint-1 / baseline status

| # | Path | Bytes | Label | Status |
|---|---|---|---|---|
| 1 | `09_diagrams/INDEX.md` | 10322 | INDEX | built (sprint-1) |
| 2 | `09_diagrams/cdss_diagrams_v2.html` | 7219 | DIAGRAM (derived page) | pre-existing (v1.2 seal / A-001..A-003) |
| 3 | `09_diagrams/cdss_diagrams_v3.html` | 10917 | DIAGRAM (derived page) | built (sprint-1) |
| 4 | `09_diagrams/data_flow_v1.mermaid` | 2014 | DIAGRAM (source) | built (sprint-1) |
| 5 | `09_diagrams/deployment_ladders.mermaid` | 1283 | DIAGRAM (source) | pre-existing (v1.2 seal / A-001..A-003) |
| 6 | `09_diagrams/deployment_ladders_v2.mermaid` | 2229 | DIAGRAM (source) | built (sprint-1) |
| 7 | `09_diagrams/imago_architecture.mermaid` | 1862 | DIAGRAM (source) | pre-existing (v1.2 seal / A-001..A-003) |
| 8 | `09_diagrams/merged_runtime_sequence.mermaid` | 1099 | DIAGRAM (source) | pre-existing (v1.2 seal / A-001..A-003) |
| 9 | `09_diagrams/register_topology_v2.mermaid` | 1290 | DIAGRAM (source) | pre-existing (v1.2 seal / A-001..A-003) |
| 10 | `09_diagrams/register_topology_v3.mermaid` | 1721 | DIAGRAM (source) | built (sprint-1) |

## 2. Folder lines (Q-F) — PASS / FAIL with evidence

| Q-F | Result | Evidence |
|---|---|---|
| Q-F-01 | **PASS** | INDEX-09 §1 |
| Q-F-02 | **PASS** | 10 files |
| Q-F-03 | **PASS** | PROC-09-REGEN |
| Q-F-04 | **PASS** | §4 defects carried; DEC-01 gate |
| Q-F-05 | **PASS** | header comments on every source |

## 3. Items × Q-D lines

Mechanical lines from the Phase 0 tools (`tools/*.out.json`); hand lines (Q-D-08/09/11/12/13/14/17) cite the reading. `N/A` = line not applicable to the class; `EXEMPT` = Q-D-02 skeleton-stub rule.

### `09_diagrams/INDEX.md`
| Q-line | Result | Evidence |
|---|---|---|
| Q-D-01 | PASS | reachable from README via manifest/INDEX |
| Q-D-02 | PASS | graph class DESIGN-LINKED; inbound 5 |
| Q-D-03 | PASS | depth 1 |
| Q-D-04 | PASS | core keys present |
| Q-D-05 | PASS | unique or n/a |
| Q-D-06 | PASS | refcheck: 0 dead paths / 0 unresolved anchors tree-wide |
| Q-D-07 | PASS | ladder skips 0; tables 0 |
| Q-D-10 | PASS/N/A | one padding form per family in this file |
| Q-D-15 | PASS | ASL 20.8 (≤35); FK 9.6 |
### `09_diagrams/cdss_diagrams_v2.html`
| Q-line | Result | Evidence |
|---|---|---|
| Q-D-01 | PASS | reachable from README via manifest/INDEX |
| Q-D-02 | PASS | graph class DESIGN-LINKED; inbound 15 |
| Q-D-03 | PASS | depth 1 |
| Q-D-04 | PASS | header/$id/title present |
| Q-D-05 | PASS | unique or n/a |
| Q-D-06 | PASS | refcheck: 0 dead paths / 0 unresolved anchors tree-wide |
| Q-D-10 | PASS/N/A | one padding form per family in this file |
| Q-D-16 | FAIL | 7 colours; 7 outside implied set |
### `09_diagrams/cdss_diagrams_v3.html`
| Q-line | Result | Evidence |
|---|---|---|
| Q-D-01 | PASS | reachable from README via manifest/INDEX |
| Q-D-02 | PASS | graph class DESIGN-LINKED; inbound 5 |
| Q-D-03 | PASS | depth 1 |
| Q-D-04 | PASS | header/$id/title present |
| Q-D-05 | PASS | unique or n/a |
| Q-D-06 | PASS | refcheck: 0 dead paths / 0 unresolved anchors tree-wide |
| Q-D-10 | PASS/N/A | one padding form per family in this file |
| Q-D-16 | FAIL | 7 colours; 7 outside implied set |
### `09_diagrams/data_flow_v1.mermaid`
| Q-line | Result | Evidence |
|---|---|---|
| Q-D-01 | PASS | reachable from README via manifest/INDEX |
| Q-D-02 | PASS | graph class DESIGN-LINKED; inbound 6 |
| Q-D-03 | PASS | depth 1 |
| Q-D-04 | PASS | header/$id/title present |
| Q-D-05 | PASS | unique or n/a |
| Q-D-06 | PASS | refcheck: 0 dead paths / 0 unresolved anchors tree-wide |
| Q-D-10 | PASS/N/A | one padding form per family in this file |
### `09_diagrams/deployment_ladders.mermaid`
| Q-line | Result | Evidence |
|---|---|---|
| Q-D-01 | PASS | reachable from README via manifest/INDEX |
| Q-D-02 | PASS | graph class DESIGN-LINKED; inbound 5 |
| Q-D-03 | PASS | depth 1 |
| Q-D-04 | PASS | header/$id/title present |
| Q-D-05 | PASS | unique or n/a |
| Q-D-06 | PASS | refcheck: 0 dead paths / 0 unresolved anchors tree-wide |
| Q-D-10 | PASS/N/A | one padding form per family in this file |
### `09_diagrams/deployment_ladders_v2.mermaid`
| Q-line | Result | Evidence |
|---|---|---|
| Q-D-01 | PASS | reachable from README via manifest/INDEX |
| Q-D-02 | PASS | graph class DESIGN-LINKED; inbound 5 |
| Q-D-03 | PASS | depth 1 |
| Q-D-04 | PASS | header/$id/title present |
| Q-D-05 | PASS | unique or n/a |
| Q-D-06 | PASS | refcheck: 0 dead paths / 0 unresolved anchors tree-wide |
| Q-D-10 | PASS/N/A | one padding form per family in this file |
### `09_diagrams/imago_architecture.mermaid`
| Q-line | Result | Evidence |
|---|---|---|
| Q-D-01 | PASS | reachable from README via manifest/INDEX |
| Q-D-02 | PASS | graph class DESIGN-LINKED; inbound 5 |
| Q-D-03 | PASS | depth 1 |
| Q-D-04 | PASS | header/$id/title present |
| Q-D-05 | PASS | unique or n/a |
| Q-D-06 | PASS | refcheck: 0 dead paths / 0 unresolved anchors tree-wide |
| Q-D-10 | PASS/N/A | one padding form per family in this file |
### `09_diagrams/merged_runtime_sequence.mermaid`
| Q-line | Result | Evidence |
|---|---|---|
| Q-D-01 | PASS | reachable from README via manifest/INDEX |
| Q-D-02 | PASS | graph class DESIGN-LINKED; inbound 6 |
| Q-D-03 | PASS | depth 1 |
| Q-D-04 | PASS | header/$id/title present |
| Q-D-05 | PASS | unique or n/a |
| Q-D-06 | PASS | refcheck: 0 dead paths / 0 unresolved anchors tree-wide |
| Q-D-10 | PASS/N/A | one padding form per family in this file |
### `09_diagrams/register_topology_v2.mermaid`
| Q-line | Result | Evidence |
|---|---|---|
| Q-D-01 | PASS | reachable from README via manifest/INDEX |
| Q-D-02 | PASS | graph class DESIGN-LINKED; inbound 7 |
| Q-D-03 | PASS | depth 1 |
| Q-D-04 | PASS | header/$id/title present |
| Q-D-05 | PASS | unique or n/a |
| Q-D-06 | PASS | refcheck: 0 dead paths / 0 unresolved anchors tree-wide |
| Q-D-10 | PASS/N/A | one padding form per family in this file |
### `09_diagrams/register_topology_v3.mermaid`
| Q-line | Result | Evidence |
|---|---|---|
| Q-D-01 | PASS | reachable from README via manifest/INDEX |
| Q-D-02 | PASS | graph class DESIGN-LINKED; inbound 5 |
| Q-D-03 | PASS | depth 1 |
| Q-D-04 | PASS | header/$id/title present |
| Q-D-05 | PASS | unique or n/a |
| Q-D-06 | PASS | refcheck: 0 dead paths / 0 unresolved anchors tree-wide |
| Q-D-10 | PASS/N/A | one padding form per family in this file |
| Q-D-11 | PASS | header comment names v2 predecessor and DEF-002 fix |
| Q-D-12 | FAIL | R25 label under ruling (QI-0029) |

## 4. Severity and weight

Per v1.0 mapping (CRITICAL ≥4 · WARNING 3 · OPTIMISATION ≤2; weight = min(5, criticality + radius)); addends are in each row. Rows in `rows.jsonl`: 9.

## 5. Preliminary folder verdict (final in IMPECCABILITY_QUEUE §b after calibration)

IMPECCABLE-WITH-DECISIONS-PENDING (R25 label BSQ-0602; DEC-01) — STYLE-DRIFT on the two pages is OPTIMISATION with a v4 successor draft

## 6. Exit

rows.jsonl: 9 rows (items 10 + applicable Q-F lines 5 → coverage: every item appears in ≥1 row: yes). Validation pasted in CHECKPOINT.md.

