# HALT_LOG — survey-3 (2026-09-05)

Temptations logged, not acted on (MT2 §4 / law "no silent shortcuts"); each names the shortcut, the law it would breach, and what was done instead.

| # | Phase | Temptation | Law | Done instead |
|---|---|---|---|---|
| H-1 | 0 | Fan out one sub-agent per folder as v1.0 permits, to finish faster | 3.1 D-5/D-6 (coverage-gap and template obligations); v1.0 "if the environment forbids sub-agents, run sequentially" | Ran sequentially in one writer; recorded in ORIENTATION §Fan-out; D-6 template not instantiated this run |
| H-2 | 0 | Adopt Flesch–Kincaid ≤ 14 as the readability threshold because the architect says "clarity scores" | law 15 (thresholds stated with alternative and rows moved) | FK reported; ASL ≤ 35 primary; alternative and the 70 rows it would move recorded in QUALITY_STANDARD |
| H-3 | 0 | Trust the first `frontmatter.py` table check (97 "inconsistent tables") | law 6 (evidence or nothing) | Debugged: regex spanned sections; fixed (`(?m)` with `[^\n]*`); re-run → 0. Both runs kept in the tool log |
| H-4 | 1 | File the 90 skeleton stubs as ORPHAN-IN-DESIGN-GRAPH (tool says LEDGER-OR-INDEX-ONLY) | Q-D-02 exemption stated in QUALITY_STANDARD before the census | One PRESENT-IMPECCABLE folder note; the 7 non-06_ candidates filed at confidence 60 for Phase 2 reading |
| H-5 | 1 | Treat delta-item labels (`D-n`, `E-n`, `T-nn` eval cases) as undeclared ID families and file ~20 ID-LIFECYCLE-GAP rows | law "no padded queue" (<what_a_wrong_answer_costs>) | Classified label-only in L2_id_lifecycle; only requirement-bearing families filed; the T-nn overlap filed once as TAXONOMY-DUPLICATE (OPTIMISATION) |
| H-6 | 1 | Re-file survey-2's owner gaps (regulatory/infra/repo owners) as new GOVERNANCE-GAP rows | law 11 (the sprint is the baseline; HUMAN-ONLY rows stand) | Cited BSQ-0110/0209/0394/0405; filed only the *census* staleness (00_MANIFEST §6) and DECISION-PENDING rows with their DEC ids |
| H-7 | 1 | Write the MET-4.1 / MET-2.2 remediation drafts with owners filled in from my own judgment | law 4 (OPEN means OPEN); D-3 attribution never closes | Drafts carry roles + resolving DEC only; every person cell stays `[NEEDS DEFINITION]` |
| H-8 | 1 | Score `confidence: 100` on rows whose evidence is a tool output | 3.1 D-2 rubric (81–100 = double-checked against the file, exemplar named) | Tool-only rows scored 60–90 with the reason stating what a read would add; only rows with quoted positions and a named exemplar reach 90–95 |
| H-9 | 2 | Treat `00_inventory.txt` size drifts (13) as append-only violations | law 6 (verify before claiming) | Checked `git show 73460b3:MET-2 | wc -c` = 6414 = disk → the inventory predates the seal; filed as a governance/status finding on the inventory file, not as edits |
| H-10 | 2 | Skip items with no finding to save space | v1.0 Phase 4 coverage ("every in-scope path appears in ≥1 row") | PRESENT-IMPECCABLE row per clean item (severity NONE, weight 0) |

## Final section (Phase 4)

| # | Phase | Temptation | Law | Done instead |
|---|---|---|---|---|
| H-11 | 3 | Keep the SEC-2 row at WARNING because Phase 1 had filed it so | law 6; 3.1 D-2 (confidence is scored against the file) | Full read; row narrowed and downgraded with the reason recorded; calibration untouched |
| H-12 | 4 | Cap CRITICAL rows at "0–2" (deep-review heuristic) when the trigger fired (7 of 28) | 3.1 §4 item 3 (trigger to re-check, not a cap) | Each CRITICAL re-read; 6 are decisions mirroring survey-2 weights; 1 executable; all retained with the reasoning in §a |
| H-13 | 4 | Write "IMPECCABLE" for 04_/09_ because no executable row remains | v1.0 §b three states; DEC-02/10/11/01 open | IMPECCABLE-WITH-DECISIONS-PENDING with the DEC ids listed |
| H-14 | 4 | Append A-008 to 00_MANIFEST.md myself (sprint-1 did append A-004) | this run's law 1 as written in v1.0: "you write only under the run directory"; CHECKSUMS diff must be ∅ | PROPOSED_AMENDMENTS.md carries the A-008 text; diff outside the run dir = 0 lines |
| H-15 | 4 | Merge the run PR after opening it | README "main accepts changes only by PR"; the owner merges | PR opened as Kenny-bytes; not merged by the run |

Twelve temptations in Phases 0–2 (H-1..H-10) and five in Phases 3–4; none acted on.
