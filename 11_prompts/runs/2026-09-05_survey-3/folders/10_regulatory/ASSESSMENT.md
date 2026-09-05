# ASSESSMENT — 10_regulatory (survey-3, Phase 2, 2026-09-05)

10_ = EXEC-1, FOLD-1, REG-POSTURE v1.1/v1.2 (+CONTENTS), REG-NZ v1.0/v1.1, REG-US, REG-EU, MAK-GOV, REG-SPRINT v1.0/1.1/1.2, validate_reg.py, INDEX-10. ADVISORY_ONLY throughout.

## 1. Items (15) — survey-2 label · sprint-1 / baseline status

| # | Path | Bytes | Label | Status |
|---|---|---|---|---|
| 1 | `10_regulatory-execution/EXEC-1_execution_directive.md` | 11180 | DIRECTIVE | pre-existing (v1.2 seal / A-001..A-003) |
| 2 | `10_regulatory-execution/FOLD-1_antennae_fold_worklist.md` | 2799 | WORKLIST/PLAN | pre-existing (v1.2 seal / A-001..A-003) |
| 3 | `10_regulatory-execution/INDEX.md` | 12762 | INDEX | built (sprint-1) |
| 4 | `10_regulatory-execution/MAK-GOV_addendum-g_v0.9.md` | 17124 | REGULATORY | pre-existing (v1.2 seal / A-001..A-003) |
| 5 | `10_regulatory-execution/REG-EU_v1.0.md` | 46101 | REGULATORY | pre-existing (v1.2 seal / A-001..A-003) |
| 6 | `10_regulatory-execution/REG-NZ_v1.0.md` | 13194 | REGULATORY | pre-existing (v1.2 seal / A-001..A-003) |
| 7 | `10_regulatory-execution/REG-NZ_v1.1.md` | 47377 | REGULATORY | pre-existing (v1.2 seal / A-001..A-003) |
| 8 | `10_regulatory-execution/REG-POSTURE_v1.1.md` | 60793 | REGULATORY | pre-existing (v1.2 seal / A-001..A-003) |
| 9 | `10_regulatory-execution/REG-POSTURE_v1.2.md` | 96260 | REGULATORY | pre-existing (v1.2 seal / A-001..A-003) |
| 10 | `10_regulatory-execution/REG-POSTURE_v1.2_CONTENTS.md` | 9915 | COMPANION (contents) | built (sprint-1) |
| 11 | `10_regulatory-execution/REG-SPRINT-1.1_delta.md` | 6141 | DELTA | pre-existing (v1.2 seal / A-001..A-003) |
| 12 | `10_regulatory-execution/REG-SPRINT-1.2_census_delta.md` | 8986 | DELTA | built (sprint-1) |
| 13 | `10_regulatory-execution/REG-SPRINT_v1.0.md` | 10741 | WORKLIST/PLAN | pre-existing (v1.2 seal / A-001..A-003) |
| 14 | `10_regulatory-execution/REG-US_v1.0.md` | 47772 | REGULATORY | pre-existing (v1.2 seal / A-001..A-003) |
| 15 | `10_regulatory-execution/validate_reg.py` | 3904 | TOOLING (CC-5) | pre-existing (v1.2 seal / A-001..A-003) |

## 2. Folder lines (Q-F) — PASS / FAIL with evidence

| Q-F | Result | Evidence |
|---|---|---|
| Q-F-01 | **PASS** | INDEX-10 §1 |
| Q-F-02 | **PASS** | 15 files |
| Q-F-03 | **PASS** | EXEC-1 RUN map; packets assembled |
| Q-F-04 | **PARTIAL** | regulatory owner [NEEDS DEFINITION] (HUMAN-ONLY, survey-2); supersession rule stated (EX-3) |
| Q-F-05 | **PARTIAL** | REG-SPRINT-1.1/1.2 lack supersedes (minor) |

## 3. Items × Q-D lines

Mechanical lines from the Phase 0 tools (`tools/*.out.json`); hand lines (Q-D-08/09/11/12/13/14/17) cite the reading. `N/A` = line not applicable to the class; `EXEMPT` = Q-D-02 skeleton-stub rule.

### `10_regulatory-execution/EXEC-1_execution_directive.md`
| Q-line | Result | Evidence |
|---|---|---|
| Q-D-01 | PASS | reachable from README via manifest/INDEX |
| Q-D-02 | PASS | graph class DESIGN-LINKED; inbound 40 |
| Q-D-03 | PASS | depth 1 |
| Q-D-04 | PASS | core keys present |
| Q-D-05 | PASS | unique or n/a |
| Q-D-06 | PASS | refcheck: 0 dead paths / 0 unresolved anchors tree-wide |
| Q-D-07 | PASS | ladder skips 0; tables 0 |
| Q-D-08 | PASS (with DEPLOY-1.1) | RUN table + DR owners |
| Q-D-09 | PASS | req_prefix EX / 10; census Part 5 |
| Q-D-10 | PASS/N/A | one padding form per family in this file |
| Q-D-11 | PASS | governs/subordinate_to; EX-10 evidence rule |
| Q-D-15 | PASS | ASL 19.5 (≤35); FK 11.9 |
### `10_regulatory-execution/FOLD-1_antennae_fold_worklist.md`
| Q-line | Result | Evidence |
|---|---|---|
| Q-D-01 | PASS | reachable from README via manifest/INDEX |
| Q-D-02 | PASS | graph class DESIGN-LINKED; inbound 19 |
| Q-D-03 | PASS | depth 1 |
| Q-D-04 | PASS | core keys present |
| Q-D-05 | PASS | unique or n/a |
| Q-D-06 | PASS | refcheck: 0 dead paths / 0 unresolved anchors tree-wide |
| Q-D-07 | PASS | ladder skips 0; tables 0 |
| Q-D-08 | PASS (via PROMPT-FOLD-1) | steps with owner = regulatory owner; gate = C-13 closure |
| Q-D-10 | FAIL | prefix collision or label overlap (see L2_id_lifecycle) |
| Q-D-12 | FAIL | W1–W5 namespace (QI-0030) |
| Q-D-15 | PASS | ASL 15.5 (≤35); FK 8.9 |
### `10_regulatory-execution/INDEX.md`
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
| Q-D-15 | PASS | ASL 27.5 (≤35); FK 13.6 |
### `10_regulatory-execution/MAK-GOV_addendum-g_v0.9.md`
| Q-line | Result | Evidence |
|---|---|---|
| Q-D-01 | PASS | reachable from README via manifest/INDEX |
| Q-D-02 | PASS | graph class DESIGN-LINKED; inbound 34 |
| Q-D-03 | PASS | depth 1 |
| Q-D-04 | PASS | core keys present |
| Q-D-05 | PASS | unique or n/a |
| Q-D-06 | PASS | refcheck: 0 dead paths / 0 unresolved anchors tree-wide |
| Q-D-07 | PASS | ladder skips 0; tables 0 |
| Q-D-08 | FAIL (verification per NDG) — cited to BSQ-0707, no new row | §3 NDG blocks; §4 sprints; DEPLOY-2 NDG criteria among the 7 unbuilt integrations |
| Q-D-09 | PASS | req_prefix NDG / 14; R30.3 |
| Q-D-10 | PASS/N/A | one padding form per family in this file |
| Q-D-11 | PASS | authority line; DEC-13/14 named |
| Q-D-15 | PASS | ASL 14.4 (≤35); FK 12.4 |
| Q-D-17 | FAIL (no Contents; no census/self-audit) — INDEX-10 §4 carries it under BSQ-0707 | 17 KB, 6 parts |
### `10_regulatory-execution/REG-EU_v1.0.md`
| Q-line | Result | Evidence |
|---|---|---|
| Q-D-01 | PASS | reachable from README via manifest/INDEX |
| Q-D-02 | PASS | graph class DESIGN-LINKED; inbound 15 |
| Q-D-03 | PASS | depth 1 |
| Q-D-04 | PASS | core keys present |
| Q-D-05 | PASS | unique or n/a |
| Q-D-06 | PASS | refcheck: 0 dead paths / 0 unresolved anchors tree-wide |
| Q-D-07 | PASS | ladder skips 0; tables 0 |
| Q-D-08 | FAIL (owner per task) | EU-TASK ID·Task·Gate |
| Q-D-09 | PASS | declared, censused |
| Q-D-10 | PASS/N/A | one padding form per family in this file |
| Q-D-15 | PASS | ASL 20.5 (≤35); FK 12.4 |
### `10_regulatory-execution/REG-NZ_v1.0.md`
| Q-line | Result | Evidence |
|---|---|---|
| Q-D-01 | PASS | reachable from README via manifest/INDEX |
| Q-D-02 | PASS | graph class DESIGN-LINKED; inbound 28 |
| Q-D-03 | PASS | depth 1 |
| Q-D-04 | PASS | core keys present |
| Q-D-05 | FAIL | doc_id shared by a version chain; rule absent (QI-0001) |
| Q-D-06 | PASS | refcheck: 0 dead paths / 0 unresolved anchors tree-wide |
| Q-D-07 | PASS | ladder skips 0; tables 0 |
| Q-D-10 | PASS/N/A | one padding form per family in this file |
| Q-D-15 | PASS | ASL 19.8 (≤35); FK 12.0 |
### `10_regulatory-execution/REG-NZ_v1.1.md`
| Q-line | Result | Evidence |
|---|---|---|
| Q-D-01 | PASS | reachable from README via manifest/INDEX |
| Q-D-02 | PASS | graph class DESIGN-LINKED; inbound 28 |
| Q-D-03 | PASS | depth 1 |
| Q-D-04 | PASS | core keys present |
| Q-D-05 | FAIL | doc_id shared by a version chain; rule absent (QI-0001) |
| Q-D-06 | PASS | refcheck: 0 dead paths / 0 unresolved anchors tree-wide |
| Q-D-07 | PASS | ladder skips 0; tables 0 |
| Q-D-08 | FAIL (owner per task) | NZ-TASK ID·Task·Gate |
| Q-D-09 | PASS | alias exemplar (QI-0052) |
| Q-D-10 | PASS/N/A | one padding form per family in this file |
| Q-D-11 | PASS | supersedes; attestation_by |
| Q-D-15 | PASS | ASL 20.1 (≤35); FK 12.2 |
### `10_regulatory-execution/REG-POSTURE_v1.1.md`
| Q-line | Result | Evidence |
|---|---|---|
| Q-D-01 | PASS | reachable from README via manifest/INDEX |
| Q-D-02 | PASS | graph class DESIGN-LINKED; inbound 101 |
| Q-D-03 | PASS | depth 1 |
| Q-D-04 | PASS | core keys present |
| Q-D-05 | FAIL | doc_id shared by a version chain; rule absent (QI-0001) |
| Q-D-06 | PASS | refcheck: 0 dead paths / 0 unresolved anchors tree-wide |
| Q-D-07 | PASS | ladder skips 0; tables 0 |
| Q-D-10 | PASS/N/A | one padding form per family in this file |
| Q-D-15 | PASS | ASL 16.5 (≤35); FK 11.5 |
### `10_regulatory-execution/REG-POSTURE_v1.2.md`
| Q-line | Result | Evidence |
|---|---|---|
| Q-D-01 | PASS | reachable from README via manifest/INDEX |
| Q-D-02 | PASS | graph class DESIGN-LINKED; inbound 101 |
| Q-D-03 | PASS | depth 1 |
| Q-D-04 | PASS | core keys present |
| Q-D-05 | FAIL | doc_id shared by a version chain; rule absent (QI-0001) |
| Q-D-06 | PASS | refcheck: 0 dead paths / 0 unresolved anchors tree-wide |
| Q-D-07 | PASS | ladder skips 0; tables 0 |
| Q-D-08 | FAIL (owner/evidence per task) | TASK-REG tables ID·Task·Gate (QI-0020) |
| Q-D-09 | PASS | exemplar (QI-0051) |
| Q-D-10 | PASS/N/A | one padding form per family in this file |
| Q-D-11 | PASS with recorded gap | §12.3 'no owner field… G-09' — the gap is stated by the file (HUMAN-ONLY, survey-2) |
| Q-D-12 | PASS | §0.3 one prefix one meaning; Observer caveat consistent |
| Q-D-15 | PASS | ASL 17.4 (≤35); FK 11.6 |
| Q-D-17 | PASS | §0.4 closed status enum; census; self-audit |
### `10_regulatory-execution/REG-POSTURE_v1.2_CONTENTS.md`
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
| Q-D-15 | PASS | ASL 17.5 (≤35); FK 8.6 |
### `10_regulatory-execution/REG-SPRINT-1.1_delta.md`
| Q-line | Result | Evidence |
|---|---|---|
| Q-D-01 | PASS | reachable from README via manifest/INDEX |
| Q-D-02 | PASS | graph class DESIGN-LINKED; inbound 24 |
| Q-D-03 | PASS | depth 1 |
| Q-D-04 | PASS | core keys present |
| Q-D-05 | PASS | unique or n/a |
| Q-D-06 | PASS | refcheck: 0 dead paths / 0 unresolved anchors tree-wide |
| Q-D-07 | PASS | ladder skips 0; tables 0 |
| Q-D-10 | PASS/N/A | one padding form per family in this file |
| Q-D-15 | PASS | ASL 22.0 (≤35); FK 13.2 |
### `10_regulatory-execution/REG-SPRINT-1.2_census_delta.md`
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
| Q-D-15 | PASS | ASL 22.5 (≤35); FK 9.6 |
### `10_regulatory-execution/REG-SPRINT_v1.0.md`
| Q-line | Result | Evidence |
|---|---|---|
| Q-D-01 | PASS | reachable from README via manifest/INDEX |
| Q-D-02 | PASS | graph class DESIGN-LINKED; inbound 26 |
| Q-D-03 | PASS | depth 1 |
| Q-D-04 | PASS | core keys present |
| Q-D-05 | PASS | unique or n/a |
| Q-D-06 | PASS | refcheck: 0 dead paths / 0 unresolved anchors tree-wide |
| Q-D-07 | PASS | ladder skips 0; tables 0 |
| Q-D-10 | PASS/N/A | one padding form per family in this file |
| Q-D-15 | PASS | ASL 15.2 (≤35); FK 11.7 |
### `10_regulatory-execution/REG-US_v1.0.md`
| Q-line | Result | Evidence |
|---|---|---|
| Q-D-01 | PASS | reachable from README via manifest/INDEX |
| Q-D-02 | PASS | graph class DESIGN-LINKED; inbound 15 |
| Q-D-03 | PASS | depth 1 |
| Q-D-04 | PASS | core keys present |
| Q-D-05 | PASS | unique or n/a |
| Q-D-06 | PASS | refcheck: 0 dead paths / 0 unresolved anchors tree-wide |
| Q-D-07 | PASS | ladder skips 0; tables 0 |
| Q-D-08 | FAIL (owner per task) | US-TASK ID·Task·Gate |
| Q-D-09 | PASS | declared, censused (INDEX-10 §3) |
| Q-D-10 | PASS/N/A | one padding form per family in this file |
| Q-D-15 | PASS | ASL 23.1 (≤35); FK 14.2 |
### `10_regulatory-execution/validate_reg.py`
| Q-line | Result | Evidence |
|---|---|---|
| Q-D-01 | PASS | reachable from README via manifest/INDEX |
| Q-D-02 | PASS | graph class DESIGN-LINKED; inbound 8 |
| Q-D-03 | PASS | depth 1 |
| Q-D-04 | PASS | header/$id/title present |
| Q-D-05 | PASS | unique or n/a |
| Q-D-06 | PASS | refcheck: 0 dead paths / 0 unresolved anchors tree-wide |
| Q-D-10 | PASS/N/A | one padding form per family in this file |

## 4. Severity and weight

Per v1.0 mapping (CRITICAL ≥4 · WARNING 3 · OPTIMISATION ≤2; weight = min(5, criticality + radius)); addends are in each row. Rows in `rows.jsonl`: 13.

## 5. Preliminary folder verdict (final in IMPECCABILITY_QUEUE §b after calibration)

BELOW-STANDARD — WARNING rows: task owner/evidence cells (QI-0018 REGULATORY), doc_id rule (CHAIN), two ORPHAN candidates (confidence 60); W-namespace after decision

## 6. Exit

rows.jsonl: 13 rows (items 15 + applicable Q-F lines 5 → coverage: every item appears in ≥1 row: yes). Validation pasted in CHECKPOINT.md.

