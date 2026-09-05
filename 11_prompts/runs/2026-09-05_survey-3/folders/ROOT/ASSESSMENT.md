# ASSESSMENT — ROOT (survey-3, Phase 2, 2026-09-05)

ROOT = `README.md`, `AGENTS.md`, `CLAUDE.md` (`.gitignore` excluded from scope; `00_inventory.txt` and `00_MANIFEST.md` are folder 00). Governance text outside the 00_–11_ append-only law; judged for terminology consistency, reference integrity and governance statements.

## 1. Items (3) — survey-2 label · sprint-1 / baseline status

| # | Path | Bytes | Label | Status |
|---|---|---|---|---|
| 1 | `AGENTS.md` | 6379 | ROOT LOOSE FILE / governance text | added/changed after baseline (A-005..A-007) |
| 2 | `CLAUDE.md` | 294 | ROOT LOOSE FILE / governance text | added/changed after baseline (A-005..A-007) |
| 3 | `README.md` | 6013 | ROOT LOOSE FILE / governance text | added/changed after baseline (A-005..A-007) |

## 2. Folder lines (Q-F) — PASS / FAIL with evidence

| Q-F | Result | Evidence |
|---|---|---|
| Q-F-01 | **PASS** | README 'Layout' + 'Laws of the corpus' = the root briefing; AGENTS.md restates the laws for agents |
| Q-F-02 | **PASS** | README Layout table = folder-level index; 00_MANIFEST §1 |
| Q-F-04 | **PASS** | README 'How to change it'; AGENTS.md 'How work lands' |
| Q-F-05 | **N/A** | no INDEX/delta at root |

## 3. Items × Q-D lines

Mechanical lines from the Phase 0 tools (`tools/*.out.json`); hand lines (Q-D-08/09/11/12/13/14/17) cite the reading. `N/A` = line not applicable to the class; `EXEMPT` = Q-D-02 skeleton-stub rule.

### `AGENTS.md`
| Q-line | Result | Evidence |
|---|---|---|
| Q-D-01 | PASS | reachable from README via manifest/INDEX |
| Q-D-02 | PASS | graph class DESIGN-LINKED; inbound 9 |
| Q-D-03 | PASS | depth 0 |
| Q-D-04 | N/A (judged on parent, P-F-02) | root-governance |
| Q-D-05 | PASS | unique or n/a |
| Q-D-06 | PASS | refcheck: 0 dead paths / 0 unresolved anchors tree-wide |
| Q-D-10 | PASS/N/A | one padding form per family in this file |
| Q-D-11 | PASS (governance text) | changed by PR only; outside 00_–11_ law by design |
| Q-D-12 | PASS | laws restate README/MANIFEST terms; read order through 3.1/3.2 |
| Q-D-15 | PASS | ASL 19.1 (≤35); FK 11.1 |
### `CLAUDE.md`
| Q-line | Result | Evidence |
|---|---|---|
| Q-D-01 | PASS | reachable from README via manifest/INDEX |
| Q-D-02 | PASS | graph class DESIGN-LINKED; inbound 10 |
| Q-D-03 | PASS | depth 0 |
| Q-D-04 | N/A (judged on parent, P-F-02) | root-governance |
| Q-D-05 | PASS | unique or n/a |
| Q-D-06 | PASS | refcheck: 0 dead paths / 0 unresolved anchors tree-wide |
| Q-D-10 | PASS/N/A | one padding form per family in this file |
| Q-D-11 | PASS | imports AGENTS.md |
| Q-D-15 | N/A | <50 prose words |
### `README.md`
| Q-line | Result | Evidence |
|---|---|---|
| Q-D-01 | PASS | reachable from README via manifest/INDEX |
| Q-D-02 | PASS | graph class DESIGN-LINKED; inbound 14 |
| Q-D-03 | PASS | depth 0 |
| Q-D-04 | N/A (judged on parent, P-F-02) | root-governance |
| Q-D-05 | PASS | unique or n/a |
| Q-D-06 | PASS | refcheck: 0 dead paths / 0 unresolved anchors tree-wide |
| Q-D-10 | PASS/N/A | one padding form per family in this file |
| Q-D-11 | PASS | Laws of the corpus; How to change it; Provenance |
| Q-D-12 | PASS | consistent |
| Q-D-15 | PASS | ASL 15.8 (≤35); FK 9.2 |

## 4. Severity and weight

Per v1.0 mapping (CRITICAL ≥4 · WARNING 3 · OPTIMISATION ≤2; weight = min(5, criticality + radius)); addends are in each row. Rows in `rows.jsonl`: 3.

## 5. Preliminary folder verdict (final in IMPECCABILITY_QUEUE §b after calibration)

IMPECCABLE (every applicable line PASS; the GLOSSARY.md proposal is a CHAIN row, not a root defect)

## 6. Exit

rows.jsonl: 3 rows (items 3 + applicable Q-F lines 4 → coverage: every item appears in ≥1 row: yes). Validation pasted in CHECKPOINT.md.

