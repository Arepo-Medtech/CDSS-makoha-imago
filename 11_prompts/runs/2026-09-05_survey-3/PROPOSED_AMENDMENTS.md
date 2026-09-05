# PROPOSED_AMENDMENTS — survey-3 (2026-09-05)

Text for the manifest owner. Nothing here is applied by the survey; the manifest grows only by the owner's appended amendment (README "How to change it"). (This file was truncated by a write-before-read bug in the cross-reference fix of the first PR #14 push — found by Copilot review; rewritten here with the corrected row ids. Logged as H-16.)

## A-008 (proposed) — survey-3 run recorded; placeholder census re-run; DEF/A census; 00_inventory status

**What was added.** Nothing pre-existing under `00_`–`11_` was edited except this manifest (appended). One run directory: `11_prompts/runs/2026-09-05_survey-3/` (excluded from the Confluence mirror; evidence, not corpus).

| Location | Contents added | Disposition |
|---|---|---|
| `11_prompts/runs/2026-09-05_survey-3/` | PROMPT-SURVEY-3 v1.0 run, read through 3.1 and 3.2: ORIENTATION, QUALITY_STANDARD (17 Q-D + 5 Q-F lines), 8 tools + outputs, CENSUS + L1–L4 tables, 14 folder fragments, 13 depth-read items, `QI.jsonl` (174 rows, 174 valid), IMPECCABILITY_QUEUE (§a–§j), HALT_LOG, OPEN_QUESTIONS, CHECKSUMS_BEFORE/AFTER (diff ∅) | Evidence; Proposed queue for sprint-2 |

**Placeholder census (re-run 2026-09-05, in-scope files).** `[NEEDS DEFINITION]` 557 in 67 files (98 = repo owners DEC-09; 46 = corpus owner; 41 = MT2 operator DEC-10; 22 = component owners DEC-09; 15 = regulatory owner G-09; 13 = manifest owner; …) · `[NEEDS SOURCE]` 19 in 11 · `[UNAVAILABLE]` 2 in 1 · `PENDING-VALIDATOR` 46 in 10 · `PENDING-REGISTER-HOME` 6 in 4 · `PENDING-ENUMERATION` 7 in 5. Every placeholder names its resolving DEC or gap; none is unregistered. Supersedes the §6 line of 2026-09-01 (22 / 4 / 1 / 4 / 5 / 1) as the current census (QI-0028).

**ID census (this manifest).** `DEF-001..007` = 7 defect rows (§5, §10, §13); `A-001..008` = 8 amendments. Retired: none (QI-0027).

**Inventory status.** `00_inventory.txt` is the v1.1-build byte inventory of 2026-09-01 (82 lines; 13 counts and 16 paths differ from disk — `11_prompts/runs/2026-09-05_survey-3/raw/inventory_drift.txt`). It is retained as a snapshot; the tracked tree is authoritative (README). A regenerated `00_inventory_v1.3.txt` with a header line is queued (QI-0063).

**Verdicts (survey-3 §b).** ROOT and 02 are IMPECCABLE-WITH-DECISIONS-PENDING; 01, 10 and CHAIN are BELOW-STANDARD on WARNING/CRITICAL rows with drafted remedies; every other folder is BELOW-STANDARD on OPTIMISATION rows only. One CRITICAL document defect: the MET-4 gap table (QI-0018). Layer scores in the Queue §b.

**Ledger debt.** No file created since A-005 (governance files, PROMPT-SURVEY-3/3.1/3.2, this run) has a HARDEN-1.1 row or HARDEN-3.1 task; a HARDEN-1.2 / HARDEN-3.2 delta owes them, plus rows for every file the Queue's EXECUTABLE-NOW set would create.

**Honesty lines (extending §11–§13).** The survey built nothing, ran no pass, wrote no R29 row, closed no decision · thresholds are `[ASSESSOR-PROPOSED]` (Queue §Assumptions; OPEN_QUESTIONS 10) · mermaid parse cited from CI, not run locally · confidence scored by the writer, not an independent scorer.

## DEF rows proposed (none contradict 00_MANIFEST)

- **DEF-008 (proposed)** — `00_inventory.txt` presents byte counts without a date, status or supersession line; 13 counts and 16 paths differ from disk. Not an append-only breach (`git show 73460b3` sizes equal disk). Fix: A-008 inventory status paragraph + `00_inventory_v1.3.txt` successor (QI-0063).

## Decisions proposed for MET-2.2 (register rows, not amendments — Architecture owner)

- **DEC-24** doc_id supersession rule (QI-0001) · **DEC-25** R25 label (BSQ-0602 / QI-0029) · **DEC-26** namespace alias laws: W-n (FOLD-1 vs HARDEN-3), RG (MAK-CEC vs RESEARCH-1), CC (HARDEN-2 vs MAK-LBP) (QI-0030 / QI-0024 / QI-0025).
