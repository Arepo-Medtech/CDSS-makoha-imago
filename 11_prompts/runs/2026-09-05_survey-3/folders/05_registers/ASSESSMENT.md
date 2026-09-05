# ASSESSMENT — 05_registers (survey-3, Phase 2, 2026-09-05)

05_ = contracts (ARG-1, DEV-1, RRI-1), schemas + examples, R29 (schema json/md, examples, R29.1), R30 (schema+seed md, R30.1/2, schema json, R30.3 jsonl), INDEX-05.

## 1. Items (16) — survey-2 label · sprint-1 / baseline status

| # | Path | Bytes | Label | Status |
|---|---|---|---|---|
| 1 | `05_registers-and-contracts/CONTRACT-ARG-1.examples.jsonl` | 4101 | SCHEMA (examples) | built (sprint-1) |
| 2 | `05_registers-and-contracts/CONTRACT-ARG-1.schema.json` | 7405 | SCHEMA | built (sprint-1) |
| 3 | `05_registers-and-contracts/CONTRACT-ARG-1_argument_schema.md` | 2204 | SCHEMA | pre-existing (v1.2 seal / A-001..A-003) |
| 4 | `05_registers-and-contracts/CONTRACT-DEV-1.examples.jsonl` | 674 | SCHEMA (examples) | built (sprint-1) |
| 5 | `05_registers-and-contracts/CONTRACT-DEV-1.schema.json` | 1953 | SCHEMA | built (sprint-1) |
| 6 | `05_registers-and-contracts/CONTRACT-RRI-1_render-invariance_test-spec.md` | 5657 | CONTRACT | built (sprint-1) |
| 7 | `05_registers-and-contracts/INDEX.md` | 16390 | INDEX | built (sprint-1) |
| 8 | `05_registers-and-contracts/REG-R29.1_schema_twin_delta.md` | 2645 | DELTA | built (sprint-1) |
| 9 | `05_registers-and-contracts/REG-R29.examples.jsonl` | 3922 | SCHEMA (examples) | built (sprint-1) |
| 10 | `05_registers-and-contracts/REG-R29.schema.json` | 2048 | SCHEMA | pre-existing (v1.2 seal / A-001..A-003) |
| 11 | `05_registers-and-contracts/REG-R29_hardening_coverage_ledger.schema.md` | 1212 | SCHEMA | pre-existing (v1.2 seal / A-001..A-003) |
| 12 | `05_registers-and-contracts/REG-R30.1_seed_delta.md` | 2024 | DELTA | pre-existing (v1.2 seal / A-001..A-003) |
| 13 | `05_registers-and-contracts/REG-R30.2_seed_delta.md` | 4623 | DELTA | pre-existing (v1.2 seal / A-001..A-003) |
| 14 | `05_registers-and-contracts/REG-R30.3_row-form_seed.jsonl` | 317670 | SEED / LEDGER | built (sprint-1) |
| 15 | `05_registers-and-contracts/REG-R30.schema.json` | 4414 | SCHEMA | built (sprint-1) |
| 16 | `05_registers-and-contracts/REG-R30_regulatory_posture_register.schema+seed.md` | 1308 | REGISTER | pre-existing (v1.2 seal / A-001..A-003) |

## 2. Folder lines (Q-F) — PASS / FAIL with evidence

| Q-F | Result | Evidence |
|---|---|---|
| Q-F-01 | **PASS** | INDEX-05 §1 |
| Q-F-02 | **PASS** | INDEX-05 §2 = 16 files |
| Q-F-04 | **PASS** | INDEX-05 §3 reading rule + §4 |
| Q-F-05 | **PARTIAL** | R30.1/R30.2 delta form (QI-0050); R29.1 minor |

## 3. Items × Q-D lines

Mechanical lines from the Phase 0 tools (`tools/*.out.json`); hand lines (Q-D-08/09/11/12/13/14/17) cite the reading. `N/A` = line not applicable to the class; `EXEMPT` = Q-D-02 skeleton-stub rule.

### `05_registers-and-contracts/CONTRACT-ARG-1.examples.jsonl`
| Q-line | Result | Evidence |
|---|---|---|
| Q-D-01 | PASS | reachable from README via manifest/INDEX |
| Q-D-02 | PASS | graph class DESIGN-LINKED; inbound 4 |
| Q-D-03 | PASS | depth 1 |
| Q-D-04 | FAIL | no header comment / $id |
| Q-D-05 | PASS | unique or n/a |
| Q-D-06 | PASS | refcheck: 0 dead paths / 0 unresolved anchors tree-wide |
| Q-D-10 | PASS/N/A | one padding form per family in this file |
### `05_registers-and-contracts/CONTRACT-ARG-1.schema.json`
| Q-line | Result | Evidence |
|---|---|---|
| Q-D-01 | PASS | reachable from README via manifest/INDEX |
| Q-D-02 | PASS | graph class DESIGN-LINKED; inbound 4 |
| Q-D-03 | PASS | depth 1 |
| Q-D-04 | PASS | header/$id/title present |
| Q-D-05 | PASS | unique or n/a |
| Q-D-06 | PASS | refcheck: 0 dead paths / 0 unresolved anchors tree-wide |
| Q-D-10 | PASS/N/A | one padding form per family in this file |
### `05_registers-and-contracts/CONTRACT-ARG-1_argument_schema.md`
| Q-line | Result | Evidence |
|---|---|---|
| Q-D-01 | PASS | reachable from README via manifest/INDEX |
| Q-D-02 | PASS | graph class DESIGN-LINKED; inbound 38 |
| Q-D-03 | PASS | depth 1 |
| Q-D-04 | FAIL | missing ['version', 'date'] |
| Q-D-05 | PASS | unique or n/a |
| Q-D-06 | PASS | refcheck: 0 dead paths / 0 unresolved anchors tree-wide |
| Q-D-07 | PASS | ladder skips 0; tables 0 |
| Q-D-10 | PASS/N/A | one padding form per family in this file |
| Q-D-15 | FAIL | ASL 39.0 (≤35); FK 26.2 |
### `05_registers-and-contracts/CONTRACT-DEV-1.examples.jsonl`
| Q-line | Result | Evidence |
|---|---|---|
| Q-D-01 | PASS | reachable from README via manifest/INDEX |
| Q-D-02 | FAIL | graph class LEDGER-OR-INDEX-ONLY; inbound 3 |
| Q-D-03 | PASS | depth 1 |
| Q-D-04 | FAIL | no header comment / $id |
| Q-D-05 | PASS | unique or n/a |
| Q-D-06 | PASS | refcheck: 0 dead paths / 0 unresolved anchors tree-wide |
| Q-D-10 | PASS/N/A | one padding form per family in this file |
### `05_registers-and-contracts/CONTRACT-DEV-1.schema.json`
| Q-line | Result | Evidence |
|---|---|---|
| Q-D-01 | PASS | reachable from README via manifest/INDEX |
| Q-D-02 | FAIL | graph class LEDGER-OR-INDEX-ONLY; inbound 3 |
| Q-D-03 | PASS | depth 1 |
| Q-D-04 | PASS | header/$id/title present |
| Q-D-05 | PASS | unique or n/a |
| Q-D-06 | PASS | refcheck: 0 dead paths / 0 unresolved anchors tree-wide |
| Q-D-10 | PASS/N/A | one padding form per family in this file |
### `05_registers-and-contracts/CONTRACT-RRI-1_render-invariance_test-spec.md`
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
| Q-D-15 | PASS | ASL 17.9 (≤35); FK 10.6 |
### `05_registers-and-contracts/INDEX.md`
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
| Q-D-15 | PASS | ASL 26.2 (≤35); FK 11.8 |
### `05_registers-and-contracts/REG-R29.1_schema_twin_delta.md`
| Q-line | Result | Evidence |
|---|---|---|
| Q-D-01 | PASS | reachable from README via manifest/INDEX |
| Q-D-02 | FAIL | graph class LEDGER-OR-INDEX-ONLY; inbound 4 |
| Q-D-03 | PASS | depth 1 |
| Q-D-04 | PASS | core keys present |
| Q-D-05 | PASS | unique or n/a |
| Q-D-06 | PASS | refcheck: 0 dead paths / 0 unresolved anchors tree-wide |
| Q-D-07 | PASS | ladder skips 0; tables 0 |
| Q-D-10 | PASS/N/A | one padding form per family in this file |
| Q-D-15 | N/A | <50 prose words |
### `05_registers-and-contracts/REG-R29.examples.jsonl`
| Q-line | Result | Evidence |
|---|---|---|
| Q-D-01 | PASS | reachable from README via manifest/INDEX |
| Q-D-02 | PASS | graph class DESIGN-LINKED; inbound 6 |
| Q-D-03 | PASS | depth 1 |
| Q-D-04 | FAIL | no header comment / $id |
| Q-D-05 | PASS | unique or n/a |
| Q-D-06 | PASS | refcheck: 0 dead paths / 0 unresolved anchors tree-wide |
| Q-D-10 | PASS/N/A | one padding form per family in this file |
### `05_registers-and-contracts/REG-R29.schema.json`
| Q-line | Result | Evidence |
|---|---|---|
| Q-D-01 | PASS | reachable from README via manifest/INDEX |
| Q-D-02 | PASS | graph class DESIGN-LINKED; inbound 10 |
| Q-D-03 | PASS | depth 1 |
| Q-D-04 | PASS | header/$id/title present |
| Q-D-05 | PASS | unique or n/a |
| Q-D-06 | PASS | refcheck: 0 dead paths / 0 unresolved anchors tree-wide |
| Q-D-10 | PASS/N/A | one padding form per family in this file |
| Q-D-11 | PASS (via twin + INDEX-05) | owner cdss-spine in the md twin |
| Q-D-14 | PASS | enum unique |
### `05_registers-and-contracts/REG-R29_hardening_coverage_ledger.schema.md`
| Q-line | Result | Evidence |
|---|---|---|
| Q-D-01 | PASS | reachable from README via manifest/INDEX |
| Q-D-02 | PASS | graph class DESIGN-LINKED; inbound 13 |
| Q-D-03 | PASS | depth 1 |
| Q-D-04 | FAIL | missing ['version', 'date'] |
| Q-D-05 | PASS | unique or n/a |
| Q-D-06 | PASS | refcheck: 0 dead paths / 0 unresolved anchors tree-wide |
| Q-D-07 | PASS | ladder skips 0; tables 0 |
| Q-D-10 | PASS/N/A | one padding form per family in this file |
| Q-D-15 | FAIL | ASL 50.5 (≤35); FK 22.3 |
### `05_registers-and-contracts/REG-R30.1_seed_delta.md`
| Q-line | Result | Evidence |
|---|---|---|
| Q-D-01 | PASS | reachable from README via manifest/INDEX |
| Q-D-02 | PASS | graph class DESIGN-LINKED; inbound 11 |
| Q-D-03 | PASS | depth 1 |
| Q-D-04 | PASS | core keys present |
| Q-D-05 | PASS | unique or n/a |
| Q-D-06 | PASS | refcheck: 0 dead paths / 0 unresolved anchors tree-wide |
| Q-D-07 | PASS | ladder skips 0; tables 0 |
| Q-D-10 | PASS/N/A | one padding form per family in this file |
| Q-D-11 | PASS (via INDEX-05 §3) | reading rule external |
| Q-D-15 | FAIL | ASL 66.3 (≤35); FK 27.4 |
| Q-D-17 | FAIL | delta form keys absent (QI-0050) |
### `05_registers-and-contracts/REG-R30.2_seed_delta.md`
| Q-line | Result | Evidence |
|---|---|---|
| Q-D-01 | PASS | reachable from README via manifest/INDEX |
| Q-D-02 | PASS | graph class DESIGN-LINKED; inbound 6 |
| Q-D-03 | PASS | depth 1 |
| Q-D-04 | PASS | core keys present |
| Q-D-05 | PASS | unique or n/a |
| Q-D-06 | PASS | refcheck: 0 dead paths / 0 unresolved anchors tree-wide |
| Q-D-07 | PASS | ladder skips 0; tables 0 |
| Q-D-10 | PASS/N/A | one padding form per family in this file |
| Q-D-11 | PASS (via INDEX-05 §3) | reading rule external |
| Q-D-15 | PASS | ASL 30.1 (≤35); FK 13.0 |
| Q-D-17 | FAIL | delta form keys absent (QI-0050) |
### `05_registers-and-contracts/REG-R30.3_row-form_seed.jsonl`
| Q-line | Result | Evidence |
|---|---|---|
| Q-D-01 | PASS | reachable from README via manifest/INDEX |
| Q-D-02 | PASS | graph class DESIGN-LINKED; inbound 6 |
| Q-D-03 | PASS | depth 1 |
| Q-D-04 | FAIL | no header comment / $id |
| Q-D-05 | PASS | unique or n/a |
| Q-D-06 | PASS | refcheck: 0 dead paths / 0 unresolved anchors tree-wide |
| Q-D-10 | PASS/N/A | one padding form per family in this file |
### `05_registers-and-contracts/REG-R30.schema.json`
| Q-line | Result | Evidence |
|---|---|---|
| Q-D-01 | PASS | reachable from README via manifest/INDEX |
| Q-D-02 | PASS | graph class DESIGN-LINKED; inbound 7 |
| Q-D-03 | PASS | depth 1 |
| Q-D-04 | PASS | header/$id/title present |
| Q-D-05 | PASS | unique or n/a |
| Q-D-06 | PASS | refcheck: 0 dead paths / 0 unresolved anchors tree-wide |
| Q-D-10 | PASS/N/A | one padding form per family in this file |
### `05_registers-and-contracts/REG-R30_regulatory_posture_register.schema+seed.md`
| Q-line | Result | Evidence |
|---|---|---|
| Q-D-01 | PASS | reachable from README via manifest/INDEX |
| Q-D-02 | PASS | graph class DESIGN-LINKED; inbound 25 |
| Q-D-03 | PASS | depth 1 |
| Q-D-04 | FAIL | missing ['version', 'date'] |
| Q-D-05 | PASS | unique or n/a |
| Q-D-06 | PASS | refcheck: 0 dead paths / 0 unresolved anchors tree-wide |
| Q-D-07 | PASS | ladder skips 0; tables 0 |
| Q-D-09 | PASS (via R30.3) | families homed in the row-form seed |
| Q-D-10 | PASS/N/A | one padding form per family in this file |
| Q-D-11 | PASS (via INDEX-05 §3) | reading rule external; file has no change_policy |
| Q-D-14 | PASS | no enum duplicated (schema_dupes) |
| Q-D-15 | FAIL | ASL 38.3 (≤35); FK 15.4 |

## 4. Severity and weight

Per v1.0 mapping (CRITICAL ≥4 · WARNING 3 · OPTIMISATION ≤2; weight = min(5, criticality + radius)); addends are in each row. Rows in `rows.jsonl`: 18.

## 5. Preliminary folder verdict (final in IMPECCABILITY_QUEUE §b after calibration)

BELOW-STANDARD (3 ORPHAN WARNING candidates at confidence 60 → resolve in Phase 3; else OPTIMISATION only) — if the three orphans read as cited, the folder is IMPECCABLE-WITH-DECISIONS-PENDING (DEC-02/09)

## 6. Exit

rows.jsonl: 18 rows (items 16 + applicable Q-F lines 4 → coverage: every item appears in ≥1 row: yes). Validation pasted in CHECKPOINT.md.

