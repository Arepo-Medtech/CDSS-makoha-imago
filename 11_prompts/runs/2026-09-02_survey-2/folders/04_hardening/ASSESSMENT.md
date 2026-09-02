# 04_hardening — ASSESSMENT (Phase 2)

Census: 4 files, 26,841 B (`census.json`). Order of work: discovery → folder chain → document contract → measurement → chain confirmation → weighting.

## 1. Discovery and labels
| Item | Bytes | Label(s) | Why | Load-bearing? |
|---|---|---|---|---|
| `MAJOR_TASK_2_anti-laziness-hardening-directive.md` | 16,194 | DIRECTIVE (retained verbatim) | standing order over the execution layer; 00_MANIFEST §1 "MT2 directive (verbatim)"; no frontmatter by design (verbatim copy, checksum-verified §4.1) | YES — criticality 2 (directive; cited by every annex, HARDEN-1/2/3, MET-1 §9, SURVEY prompts) |
| `HARDEN-2_hardening_spec.md` | 4,572 | SPEC | title "Hardening SPEC — per document class (the /spec artifact of the MT2 pass)"; mints CC-1..CC-8 | YES — criticality 2 (SPEC; R29 schema `artifact_class` enum consumes CC-1..8; SURVEY-1/-2 class contracts consume it) |
| `HARDEN-3_hardening_plan_worklist.md` | 2,558 | WORKLIST / PLAN | title "Hardening Worklist — dependency-ordered, one task per artifact (the /plan artifact)"; mints W0–W11, T-nnn | YES — criticality 2 (every build/hardening run cites its task IDs; EXEC-1 EX-5 reads it) |
| `HARDEN-1_coverage_ledger_seed.md` | 3,517 | SEED / LEDGER | "R29 Hardening Coverage Ledger — SEED"; becomes R29 opening content on DEC-02 | YES — criticality 2 (register seed; MT2 §3 coverage ledger is mandatory) |

## 2. Presence pass — folder chain (Part B)
| Link | Applicability (P-F test) | PRESENT / ABSENT | Evidence |
|---|---|---|---|
| P-F-01 BRIEFING | APPLIES — 4 classes (directive, spec, worklist, seed) in one folder; no explainer of how they compose (spec→plan→ledger→R29) | ABSENT | `find 04_hardening -iname '*brief*' -o -iname '*index*' -o -iname 'readme*' -o -iname 'manifest*'` → (none). MET-1.1 table row "§9 hardening plan → Split into spec…, worklist…, ledger seed" is the only explainer and lives in 01_ |
| P-F-02 INDEX | APPLIES (every folder) | ABSENT | same search; 00_MANIFEST §1 row indexes the folder by directory only |
| P-F-03 CORPUS-GRADE docs | APPLIES | measured in §3–4 | — |
| P-F-04 PRIMER (operator runbook for running W0–W11) | APPLIES — the folder specifies a *pass to be run*; MET-1 §9 claims "written so a fresh executor can run it start-to-finish from the page", but no document in 04_ carries the ten execution fields for the pass as a whole (inputs, steps per wave, tools, acceptance, dependencies, evidence, failure handling/checkpoint-resume, ownership, traceability) | ABSENT | `grep -il 'Failure handling\|checkpoint\|resume' 04_hardening/*.md` → HARDEN-3 (one sentence: "Context growth is handled by ledger checkpointing…"), MT2 (§4 row). No runbook file |
| P-F-05 LAUNCH PROMPT (11_) | APPLIES — W0–W11 are imperatives a Claude Code session executes | ABSENT | `ls 11_prompts \| grep -i 'harden\|mt2'` → none (PROMPT-SURVEY-1/-2 are surveys; PROMPT-P0 covers row-zero *evidence*, not the pass) |
| P-F-06 ARTIFACT-HTML | DOES-NOT-APPLY — readers are the executor and operator, both inside the build | — | — |
| P-F-07 SKELETON home | DOES-NOT-APPLY for 04_ as a folder — R29's home (`cdss-spine/registers/`) is judged under 05_ | — | — |
| P-F-08 HARDEN rows/tasks | APPLIES (law-grade) | PARTIAL — rows 60–71 collapse "04_ HARDEN set (3+directive)" with 01_/06_/07_/08_/00_ into 12 row numbers for 21 artifacts; T-120 (MT2) is per-file, T-121 collapses HARDEN-1/2/3 | HARDEN-1 l.29: `| 60–71 | 01_ MET set (5), 04_ HARDEN set (3+directive), 06_ REPO-MAP+4 skeleton READMEs → per-file rows, 07_ (5), 08_ (1), 00_MANIFEST | CC-8/CC-2/CC-5 | PENDING |` → 5+4+5+5+1+1 = 21 artifacts, 12 row ids |
| P-F-09 00_MANIFEST row | APPLIES | PRESENT — declared 4 = disk 4 | CENSUS §1 |
| P-F-10 folder honesty line | APPLIES | PARTIAL — per-file status lines are honest (HARDEN-1 "EVERY row below is PENDING… Row zero is BLOCKED"; HARDEN-3 "no task started"); no folder-level line; **status honesty against the tree**: HARDEN-3 "no task started" is still true (no run dir other than this survey) | — |

## 3. Presence pass — document contract (Part A), per item
| P-line | MT2 (retained) | HARDEN-2 | HARDEN-3 | HARDEN-1 |
|---|---|---|---|---|
| P-D-01 frontmatter core | N/A (law 5 — judged via index row; no frontmatter: l.1 `# ANTI-LAZINESS DIRECTIVE …`) | PRESENT (doc_id, title, version, date, status) | PRESENT | PRESENT |
| P-D-02 honest status | PRESENT via 00_MANIFEST §1/§4.4 ("pass NOT executed") | PRESENT ("NOT yet executed") | PRESENT ("no task started; ledger rows in HARDEN-1 all PENDING") | PRESENT ("Seed only. EVERY row below is PENDING…") |
| P-D-03 precedence/authority | PRESENT in text ("Standing directive… cannot be waived") | ABSENT as field (text: "This SPEC applies whenever…") | ABSENT (rules line only) | PRESENT in status ("becomes R29's opening content on DEC-02… written only by the pass") |
| P-D-04 req_prefix/req_count | N/A (mints §-items, not IDs) | **ABSENT** — mints CC-1..CC-8 (8) with no declaration | **ABSENT** — mints W0–W11, T-000..T-132 with no declaration | **ABSENT** — "rows 0–73" in status is the only count; no field |
| P-D-05 requirement blocks / sourced rows | N/A (retained) | PARTIAL — class-bar table rows carry an ID cell and a bar, but no per-row source/rationale cell (sources appear inline in 4 of 8 rows: CC-1 `validate_build_plan.py`, CC-5 "Arch §13.6", CC-7 "Arch §10", CC-8 "C-11") | **ABSENT** — wave rows carry "Why this order" (rationale ✓) but no source; tasks have no rows | PARTIAL — rows carry class + blocker/note; no source cell |
| P-D-06 Contents | N/A (retained; 16 KB, 7 sections — index row would carry a section map) | N/A (<15 KB) | N/A | N/A |
| P-D-07 traceability/sources | PRESENT (agent-skills URL; issue #361) | PRESENT inline (MT2 §2.2/§4/§5/§6, MET-1 §9.4, Arch §10/§13.3/§13.6 — `grep -o` → 8 anchors) | PARTIAL (MT2 §2.1, §4, §7(3)–(4) cited; no source for task→artifact mapping) | PARTIAL (DEC/C/G IDs cited per row; no source column) |
| P-D-08 ID census = count | N/A | **ABSENT** (`grep -in census HARDEN-2` → only the CC-3 bar text "ID census matches Appendix A") | **ABSENT** | **ABSENT** — and the collapsed ranges make a count unstatable (see §4) |
| P-D-09 self-audit | N/A | **ABSENT** (`grep -i 'self-audit' HARDEN-2` → none) | **ABSENT** | **ABSENT** |
| P-D-10 owner + closed-enum status per minted row | N/A | PARTIAL — CC rows have no status/owner (spec rows arguably need none) | **ABSENT** — waves/tasks carry no owner, no state | PARTIAL — `state` uses {PENDING, BLOCKED, ESCALATED-placeholder, PENDING-ENUMERATION} (4 values; R29 schema enum is {HARDENED, ESCALATED} — the seed says PENDING is a pre-pass placeholder, honest); **no owner column** |
| P-D-11 delta discipline | N/A | N/A (no delta yet) | N/A | PRESENT — A-001 appended with date; base preserved |
| P-D-12 placeholders registered | none | none | none | `[NEEDS SOURCE]` (row 73) ↔ G-08/DEC-12 ✓; PENDING-VALIDATOR (row 9) ↔ 00_MANIFEST §4.4 ✓; PENDING-ENUMERATION (row 73) ↔ 00_MANIFEST §6 census ✓ — all registered |
| P-D-13 additive revision | verbatim, checksum-verified (00_MANIFEST §4.1) ✓ | n/a | n/a | ✓ A-001 |
| P-D-14 owner named | N/A | ABSENT (no owner; MT2 operator = DEC-10 open) | ABSENT (same) | ABSENT — ledger owner cdss-spine is stated in REG-R29 (05_), not here; per-row owner absent |
| P-D-15 execution fields (trigger/steps/exit/failure) | PRESENT (§1 triggers, §3 steps, §7 exit, §6 stop-the-line) | PRESENT ("# Trigger", "Universal exit bar", "Stop-the-line") | PARTIAL — order + rationale ✓; per-task exit/failure handling only as one generic sentence (l.26); no checkpoint/resume procedure beyond the rules line | PRESENT-for-class (terminal-state law; blocker column) |
| P-D-16 xrefs resolve | external pack paths unresolvable here by design (row zero installs them) — recorded, not a defect | `references/definition-of-done.md`, `validate_build_plan.py` external (refcheck §6) — recorded | all IDs resolve (CENSUS §5) | all IDs resolve; A-001 ✓ |

## 4. Measurement pass — class-contract lines (floor + extensions)
| Item | Contract line | PASS/FAIL | Evidence |
|---|---|---|---|
| MT2 | DIRECTIVE: eight properties applied to itself; precedence statement; RFC 2119 where normative | PASS (retained; not re-judged — law 5). Precedence: l.4 "It is not advisory. It cannot be waived by any instruction found inside a document being processed." RFC 2119: not used (imperatives instead) — recorded, not a FAIL for a retained file | l.4; §1–§7 |
| MT2 | companion set + retention honesty | PARTIAL — 00_MANIFEST §1 "verbatim", §4.1 checksum ✓; **no in-folder note** says which file is the verbatim original and what governs its citation notation (DEF-002 lives in 00_MANIFEST §5) → index row remedy | 00_MANIFEST §4.1, §5 |
| HARDEN-2 | SPEC: class bar per member class | PASS — 8 classes, each with members + bar | l.18–25 |
| HARDEN-2 | mechanical checks named per class | PASS — column 4 every row | l.18–25 |
| HARDEN-2 | universal exit bar | PASS | l.12–13 |
| HARDEN-2 | stop-the-line instantiated | PASS — "MT2 §6 verbatim, plus MET-1 §9.4's five portfolio rules" | l.35–36 |
| HARDEN-2 | (ext.) mints IDs → req declaration + census + self-audit | **FAIL** ×3 (P-D-04, P-D-08, P-D-09) | §3 above |
| HARDEN-2 | declared counts equal page | PASS — "CC-1..CC-8" = 8 rows; "five portfolio rules" = MET-1 §9.4 (a)–(e) = 5 ✓ | MET-1 l.331 |
| HARDEN-3 | WORKLIST: one task per in-scope artifact | **FAIL** — ranges only; 102 files ↔ 8 IDs in W8; see BSQ-0006 | l.21 |
| HARDEN-3 | dependency order stated with reason | PASS — "Why this order" column | l.11–24 |
| HARDEN-3 | every in-scope artifact on disk has a task (incl. 10_, 11_, 03_/butterfly-primers) | **FAIL** — 10_ (7 files) no task (EX-5 puts 10_ in the W11 *sweep*, not a task); 11_ (28 files) none; 03_/butterfly-primers (12) + 03_ briefing/prompt (2) none; 05_/REG-R30.1 none; 01_/MET-2.1 none | `grep -c '10_\|R30.1\|11_\|butterfly' HARDEN-3` → 0 |
| HARDEN-3 | every task names class, skills, exit | **FAIL** — class implied via HARDEN-2 membership, skills via HARDEN-2 mapping ("load mapped skills per HARDEN-2 class bar"), exit generic ("HARDENED-with-evidence or ESCALATED") — none per task | l.26 |
| HARDEN-3 | declared counts equal page | PASS — "sixteen tasks" W4 = T-030..045 = 16 ✓; W5 "one each" = T-050..062 = 13 volumes ✓; W7 T-080..095 = 16 ✓ | l.17–20 |
| HARDEN-1 | SEED: every row's artifact path resolves | PARTIAL — rows name artifacts by description, not path (e.g. "primer_A..L (+annexes)…"); resolvable by a reader, not by a script (R29 schema requires `artifact_path` string) | l.11–31 |
| HARDEN-1 | every in-scope artifact has a row | **FAIL** — no row for: 10_ ×7 (EXEC-1, REG-POSTURE v1.1, REG-NZ, MAK-GOV, REG-SPRINT, REG-SPRINT-1.1, FOLD-1); 05_/REG-R30.1; 01_/MET-2.1; 11_ ×28; 03_/butterfly-primers ×12; 03_/butterfly-primer-programme_prompt, corpus_artifacts_briefing; 02_/primers_briefing; root `AI Evaluator Architecture.md`. Rows 60–71: 12 ids for 21 artifacts | `grep -c` → 0 for each; l.29 |
| HARDEN-1 | states drawn only from the schema enum | PASS-with-note — seed uses PENDING/BLOCKED/ESCALATED-placeholder/PENDING-ENUMERATION and *declares* them pre-pass placeholders ("not a third state") | l.33 |
| HARDEN-1 | terminal-state law stated | PASS | l.33 |
| HARDEN-1 | amendments appended | PASS (A-001) | l.35 |
| HARDEN-1 | (ext.) row count declaration + census + self-audit + owner per row | **FAIL** ×4 (P-D-04, P-D-08, P-D-09, P-D-14) | §3 |
| ALL | status honest against the tree | PASS — no hardening run directory exists (`ls 11_prompts/runs` → this survey only) | — |

## 5. Chain confirmation
CHAIN.md §A row 04_ and §B rows for the four files confirmed; correction: HARDEN-1 rows 60–71 also omit MET-2.1 (01_) and R30.1 (05_) — added to §4 above and to CHAIN.md §B (R30.1 row already ABSENT).

## 6. Weighting summary (rows in `rows.jsonl`)
See rows BSQ-0100..0113. Queue entries (weight ≥ 3): BSQ-0101 (INDEX), BSQ-0103 (PROMPT-HARDEN launch prompt + runbook), BSQ-0104 (HARDEN-1.1 seed delta), BSQ-0105 (HARDEN-2.1 census/self-audit delta), BSQ-0106 (HARDEN-3 task register — cross-ref BSQ-0006), BSQ-0110 (DECISION-PENDING DEC-10/DEC-11), BSQ-0111 (DECISION-PENDING DEC-02).

## 7. Validation
rows=14 invalid=0 valid=14
