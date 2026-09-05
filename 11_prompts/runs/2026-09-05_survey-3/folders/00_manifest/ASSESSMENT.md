# ASSESSMENT — 00_manifest (survey-3, Phase 2, 2026-09-05)

Folder 00 = `00_MANIFEST.md` (the manifest, appended by amendment) and `00_inventory.txt` (a v1.1-build byte inventory).

## 1. Items (2) — survey-2 label · sprint-1 / baseline status

| # | Path | Bytes | Label | Status |
|---|---|---|---|---|
| 1 | `00_MANIFEST.md` | 37488 | MANIFEST / INVENTORY | added/changed after baseline (A-005..A-007) |
| 2 | `00_inventory.txt` | 5049 | MANIFEST / INVENTORY | pre-existing (v1.2 seal / A-001..A-003) |

## 2. Folder lines (Q-F) — PASS / FAIL with evidence

| Q-F | Result | Evidence |
|---|---|---|
| Q-F-01 | **PASS** | 00_MANIFEST §1–§3 briefs the whole repository |
| Q-F-02 | **PASS** | §1 + A-001..A-007 rows equal disk (render_index self-audits per folder; this run's count 271 reconciled in CENSUS) |
| Q-F-04 | **FAIL** | §6 placeholder census stale (QI-0028); the inventory file states no status (row below) |
| Q-F-05 | **PASS** | amendment form uniform |

## 3. Items × Q-D lines

Mechanical lines from the Phase 0 tools (`tools/*.out.json`); hand lines (Q-D-08/09/11/12/13/14/17) cite the reading. `N/A` = line not applicable to the class; `EXEMPT` = Q-D-02 skeleton-stub rule.

### `00_MANIFEST.md`
| Q-line | Result | Evidence |
|---|---|---|
| Q-D-01 | PASS | reachable from README via manifest/INDEX |
| Q-D-02 | PASS | graph class DESIGN-LINKED; inbound 20 |
| Q-D-03 | PASS | depth 0 |
| Q-D-04 | FAIL | missing ['version'] |
| Q-D-05 | PASS | unique or n/a |
| Q-D-06 | PASS | refcheck: 0 dead paths / 0 unresolved anchors tree-wide |
| Q-D-07 | PASS | ladder skips 0; tables 0 |
| Q-D-08 | N/A | manifest, not a plan |
| Q-D-09 | FAIL | DEF-001..007 / A-001..007 minted without a census line since §6 (QI-0027) |
| Q-D-10 | PASS/N/A | one padding form per family in this file |
| Q-D-11 | FAIL | §6 placeholder census stale 22→557 (QI-0028); owner = 'Manifest owner [NEEDS DEFINITION]' (HARDEN-1.1 row) |
| Q-D-12 | PASS | terminology consistent with README laws (read §1–§13) |
| Q-D-15 | PASS | ASL 33.6 (≤35); FK 16.6 |
| Q-D-17 | PASS | amendment form A-001..A-007 uniform (header · What was added · table · Ledger debt · Honesty lines) |
### `00_inventory.txt`
| Q-line | Result | Evidence |
|---|---|---|
| Q-D-01 | PASS | reachable from README via manifest/INDEX |
| Q-D-02 | PASS | graph class DESIGN-LINKED; inbound 5 |
| Q-D-03 | PASS | depth 0 |
| Q-D-04 | FAIL | no header comment / $id |
| Q-D-05 | PASS | unique or n/a |
| Q-D-06 | PASS | refcheck: 0 dead paths / 0 unresolved anchors tree-wide |
| Q-D-10 | PASS/N/A | one padding form per family in this file |
| Q-D-11 | FAIL | no header, date, status or supersession statement; byte counts differ from disk for 13 of 82 lines and 16 paths no longer exist (03_ files moved under corpus-md/) — raw/inventory_drift.txt; README says the tracked tree is authoritative but the file does not say so itself |
| Q-D-17 | FAIL | a bare `bytes path` list with no frontmatter analogue (header comment) |

## 4. Severity and weight

Per v1.0 mapping (CRITICAL ≥4 · WARNING 3 · OPTIMISATION ≤2; weight = min(5, criticality + radius)); addends are in each row. Rows in `rows.jsonl`: 5.

## 5. Preliminary folder verdict (final in IMPECCABILITY_QUEUE §b after calibration)

BELOW-STANDARD (WARNING rows QI-0023 and the inventory row; no CRITICAL) — remedied by one appended amendment A-008

## 6. Exit

rows.jsonl: 5 rows (items 2 + applicable Q-F lines 4 → coverage: every item appears in ≥1 row: yes). Validation pasted in CHECKPOINT.md.

