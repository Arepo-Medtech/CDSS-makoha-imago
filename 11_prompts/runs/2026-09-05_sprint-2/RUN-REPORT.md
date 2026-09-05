# RUN-REPORT — sprint-2 (2026-09-05): the survey-3 EXECUTABLE-NOW set and the MET-2.2 owed files

Run: `11_prompts/runs/2026-09-05_sprint-2/` · Branch: `sprint-2-executable-now` (from `main` 21b9675) · Executor: Claude Code (desktop session) · Mandate: the owner's instruction of 5 Sep 2026 "merge the PR - proceed with sprint-2" · Status: **built and verified on the branch; PR opened by Kenny-bytes; merge waits on the Copilot review and the owner's word.**

## 0. Append-only proof (law 1) — read this first

Pasted at seal from `CHECKSUMS_BEFORE.txt` / `CHECKSUMS_AFTER.txt` / `CHECKSUMS_CHANGED.txt` (see §5). Expected and required: the only pre-existing files whose hash changes are `00_MANIFEST.md` (appended, A-010) and two root governance files outside the 00_–11_ law — `README.md` (one row added under "Where to read it") and `AGENTS.md` (one sentence, H-12). Every file under 00_–11_ that existed on `main` is byte-identical.

## 1. Coverage

| Measure | Value |
|---|---|
| New files outside run directories | 18 |
| Files modified outside 00_–11_ | 2 (`README.md`, +1 table row; `AGENTS.md`, one "How work lands" sentence — H-12) |
| Manifest | appended only (A-010) |
| Tracked files in HARDEN scope (excl. .DS_Store, .git, runs) | 416 — every one has a ledger row (HARDEN-1/1.1/1.2) and a task (HARDEN-3.1/3.2): files without a row after this sprint = 0 |
| HARDEN-1.2 | D-1 owner cells resolved: 182 (98 repo owner + 22 component owner + 30 + 8 MT2 operator + 15 regulatory owner + 9 partial security/regulatory); still [NEEDS DEFINITION]: {'Corpus owner (03_ MANIFEST precedence) [NEEDS DEFINITION]': 46, 'Manifest owner [NEEDS DEFINITION]': 13}; D-2 new rows: 146 (ids 274..419) |
| HARDEN-3.2 | 146 tasks T-800..T-945; 0 id collisions with HARDEN-3/3.1; every new row has exactly one task |
| REG-TASK-OWNERS | 60/60 tasks; R30.3 rows PRESENT 60/60; evidence cells 60/60; [NEEDS DEFINITION] owner cells 7 (each with its DEC) |
| Diagrams | mermaid 10.9.8 via jsdom 24.1.3: 22/22 PASS (all 09_ sources + every inlined block of v2, v3, v4 pages); v4 page inlines the v4 source verbatim |
| Reference check (changed files) | - dead in-repo paths: 0; unresolved anchors: 0 (the two carried v2 `MT2 §7.4` defects excluded — DEF-003); external refs: 56; globs/placeholders: 92; prompt-declared future outputs: 604; doc-id shorthand: 3 |
| Frontmatter census | core-field gaps (file, field): 15 → `00_MANIFEST.md`:version; `05_registers-and-contracts/CONTRACT-ARG-1_argument_schema.md`:version; `05_registers-and-contracts/CONTRACT-ARG-1_argument_schema.md`:date; `05_registers-and-contracts/REG-R29_hardening_coverage_ledger.schema.md`:version; `05_registers-and-contracts/REG-R29_hardening_coverage_ledger.schema.md`:date; `05_registers-and-contracts/REG-R30_regulatory_posture_register.schema+seed.md`:version; `05_registers-and-contracts/REG-R30_regulatory_posture_register.schema+seed.md`:date; `06_repositories/REPO-MAP_v2.md`:version; `06_repositories/REPO-MAP_v2.md`:date; `07_deployment-and-operations/DEPLOY-1_deployment_plan_and_sequencing.md`:date; `07_deployment-and-operations/DEPLOY-2_testing_verification_acceptance.md`:date; `07_deployment-and-operations/GOV-1_ownership_governance_postdeploy.md`:date; `07_deployment-and-operations/OPS-1_operating_procedures.md`:date; `07_deployment-and-operations/SEC-1_security_privacy_compliance.md`:date; `08_research/RESEARCH-1_findings_gaps_source_map.md`:status · files minting requirement blocks without req_prefix: 0 (the 15 core-field gaps are pre-existing files, unchanged) |
| Depth | files: 291; depth histogram: {0: 8, 1: 144, 2: 43, 3: 43, 4: 53}; deeper than four levels: 0 |
| Schemas | - `05_registers-and-contracts/REG-R30.schema.json` check_schema OK · - `05_registers-and-contracts/REG-R30.3_row-form_seed.jsonl`: 549 rows, 0 invalid |
| Mermaid parse in CI | `.github/audit/mermaid/` — run by the audit workflow on the PR (local node_modules absent, H-11) |

## 2. Queue closure — every survey-3 EXECUTABLE-NOW row, the recommended weight-2 rows, and the MET-2.2 §6 owed files

| Row | W / class | Folder | Deliverable | Outcome | Evidence |
|---|---|---|---|---|---|
| QI-0018 | 4 CRITICAL | 01 | MET-4.1 gap register delta (owner · person/DEC · RUN/gate · exit evidence · register home per G; G declared, req_count 11; G-09 narrowed) | **BUILT** | 01_north-star-and-transformation/MET-4.1_gap_register_delta.md — 11 rows, 0 empty cells, 3 [NEEDS DEFINITION] each naming its DEC; D-3 grep pasted |
| QI-0020 | 3 WARNING | 10 | REG-TASK-OWNERS companion (60 tasks → DR · RUN · role · account · evidence artifact · R30.3 row) | **BUILT** | 10_regulatory-execution/REG-TASK-OWNERS_companion.md — 60/60 mapped; R30.3 PRESENT 60/60; 7 owner cells [NEEDS DEFINITION] with DEC (H-3); generator tools/regtask.py |
| QI-0025 | 3 WARNING | CHAIN | CC alias law | **BUILT (Proposed — DEC-26)** | 04_hardening/HARDEN-2.2_alias_laws_delta.md D-1/D-2 — grep counts pasted; corpus untouched |
| QI-0030 | 3 WARNING | CHAIN | W alias law (was EXECUTABLE-AFTER-DECISION; text drafted) | **DRAFTED (Proposed — DEC-26)** | HARDEN-2.2 D-3/D-4 |
| QI-0019 | 3 WARNING | 01 | MET-2.2 closure-evidence column + req_prefixes | **CLOSED-BY-MET-2.2 (PR #15)** | 01_north-star-and-transformation/MET-2.2_decision_closures_delta.md §2 (26 rows with Closes-on) and frontmatter req_prefixes [C, DEC]; glossary-anchor erratum (§9 vs §11) recorded in GLOSSARY.md (both lines cited) |
| QI-0024 | 3 WARNING | CHAIN | RG alias law + RGAP- declaration | **BUILT (Proposed — DEC-26)** | 08_research/RESEARCH-1.2_alias_and_triggers_delta.md D-1/D-2 — grep counts pasted |
| QI-0032 | 3 WARNING | ROOT | GLOSSARY.md | **BUILT** | GLOSSARY.md — 38 terms, each with a quoted or pointed source and a ruling state; README "Where to read it" row added |
| QI-0023 | 3 WARNING | 01 | C / DEC / G declared and censused | **CLOSED-BY-MET-2.2 + MET-4.1** | MET-2.2 frontmatter id_families + req_prefixes [C, DEC]; MET-4.1 req_prefix G / req_count 11 + D-2 census |
| QI-0022 | 2 OPT (recommended) | 08 | RG trigger column | **BUILT** | RESEARCH-1.2 D-3 — 8 rows |
| QI-0043/0044 | 2 OPT (recommended with DEC-01 regeneration) | 09 | tokens.css + cdss_diagrams_v4.html | **BUILT** | 09_diagrams/tokens.css (2124 B: 28 series colours, 3 fonts, 7 diagram tokens) · cdss_diagrams_v4.html links it; parse 22/22 PASS |
| QI-0063 / DEF-008 | 2 OPT (recommended) | 00 | 00_inventory_v1.3.txt successor with header line | **BUILT** | 00_inventory_v1.3.txt — 416 tracked files outside runs; header names main@21b9675, supersession and authority |
| QI-0010/0011/0013/0014 | 2 OPT (recommended) | 05/10/11 | four orphan citations from consuming documents | **BUILT** | R29.1 ← MET-4.1 G-03 register-home cell; REG-POSTURE CONTENTS ← REG-TASK-OWNERS applies_to; PROMPT-FOLD-1 ← HARDEN-2.2 D-3; PRM-SERIES index ← REPO-MAP v3 preamble |
| MET-2.2 §6 | owed | 04 | HARDEN-1.2 owner delta + HARDEN-3.2 task delta | **BUILT** | HARDEN-1.2: D-1 182 owner cells resolved; D-2 146 new rows (274..419); HARDEN-3.2: 146 tasks T-800..T-945; tree 416 files, without a row after: 0 |
| MET-2.2 §6 | owed | 06 | REPO-MAP v3 (owner column; PFX ratified) | **BUILT** | 06_repositories/REPO-MAP_v3.md — 19 rows with owner; cdss-compiler PFX [PENDING-ENUMERATION] (H-4) |
| MET-2.2 §6 / MET-4.1 G-10 | owed | 09 | IMAGO-3 v4 + v4 page (DEC-01 regeneration, PROC-09-REGEN) | **BUILT** | register_topology_v4.mermaid (R29/R30 solid) + cdss_diagrams_v4.html; INDEX-09.1 §3 parse paste |
| MET-2.2 §6 | owed | 01 | wording read-through for retained "proposed"/[NEEDS DEFINITION] sentences | **BUILT** | 01_north-star-and-transformation/MET-5_ratification_read-through_notice.md — N-01..N-12 by path and line |
| MET-2.2 §6 | owed | 07 | DEPLOY-1.2 (RTO/RPO, drill protocol) | **NOT BUILT — EXECUTABLE-AFTER-INPUT** | values are the infrastructure owner's (DEC-23 values Open); H-9; OPEN_QUESTIONS 4 |
| chain | — | 04/06/08/09/10 | INDEX-0n.1 deltas so no new file dangles in its folder chain | **BUILT** | INDEX-04.1, -06.1, -08.1, -09.1, -10.1 — rows for every sprint-2 file in those folders; parents byte-identical |

Survey-3 HUMAN-ONLY rows (QI-0167..0174) were closed by the owner in MET-2.2 (PR #15) before this sprint; EXECUTABLE-AFTER-DECISION rows QI-0001 (doc_id rule, DEC-24) and QI-0029 (R25 label, DEC-25) remain with the Architecture owner — their draft text stands in MET-2.2 §5; the v4 topology carries the R25 label unchanged.

## 3. Files added (bytes from `00_inventory_v1.3.txt`, which is itself one of them)

| path | bytes |
|---|---|
| `00_inventory_v1.3.txt` | 24,257 |
| `01_north-star-and-transformation/MET-4.1_gap_register_delta.md` | 7,720 |
| `01_north-star-and-transformation/MET-5_ratification_read-through_notice.md` | 6,489 |
| `04_hardening/HARDEN-1.2_coverage_ledger_owner_delta.md` | 76,468 |
| `04_hardening/HARDEN-2.2_alias_laws_delta.md` | 3,713 |
| `04_hardening/HARDEN-3.2_task_register_delta.md` | 86,892 |
| `04_hardening/INDEX-04.1_delta.md` | 2,798 |
| `06_repositories/INDEX-06.1_delta.md` | 1,921 |
| `06_repositories/REPO-MAP_v3.md` | 8,510 |
| `08_research/INDEX-08.1_delta.md` | 1,957 |
| `08_research/RESEARCH-1.2_alias_and_triggers_delta.md` | 4,631 |
| `09_diagrams/INDEX-09.1_delta.md` | 4,155 |
| `09_diagrams/cdss_diagrams_v4.html` | 11,671 |
| `09_diagrams/register_topology_v4.mermaid` | 1,894 |
| `09_diagrams/tokens.css` | 2,124 |
| `10_regulatory-execution/INDEX-10.1_delta.md` | 2,075 |
| `10_regulatory-execution/REG-TASK-OWNERS_companion.md` | 20,821 |
| `GLOSSARY.md` | 12,063 |

## 4. Halts and open questions

`HALT_LOG.md` H-1..H-11 (two tool defects fixed in-run, two citation corrections before commit, four DECISION-PENDING / EXECUTABLE-AFTER-INPUT scope statements, two tool-environment notes). `OPEN_QUESTIONS.md` 1–8 for the owner. Nothing assumed closed.

## 5. Seal

`CHECKSUMS_AFTER.txt` and `CHECKSUMS_CHANGED.txt` (pre-existing files whose hash changed) are written after the manifest append and pasted here by the seal step:

```
CHECKSUMS_BEFORE.txt: 630 files (main 21b9675, before any write)
CHECKSUMS_AFTER.txt:  648 files
pre-existing files whose hash changed: 3
< c356fa706f01d5f0833bab9608953cca4607fa5b8c091109c6758e9671d0fde6  ./00_MANIFEST.md
< 7a84add8af59b962917535a231283ca3fd9bdaace9039d3f0b6fa25e1b6b2319  ./AGENTS.md
< e772ec9e74ff5c560a1b05cb7e94ffa70267280facb997ca3fa78946eade614a  ./README.md
pre-existing files removed: 0 []
files added (outside this run directory): 18
00_MANIFEST.md prefix check: head.startswith(main:00_MANIFEST.md) = True; appended 7280 bytes; sha256(main:00_MANIFEST.md) = c356fa706f01d5f0833bab9608953cca4607fa5b8c091109c6758e9671d0fde6
README.md, AGENTS.md: root governance files outside the 00_–11_ law; README +1 table row, AGENTS.md one 'How work lands' sentence (H-12)
```

## 6. Honesty lines

Built 18 files; ran no pass; wrote no R29 row (every ledger row PENDING); closed no decision, gap, ASSUME or gate; set no RTO/RPO; wrote nothing under 03_; the alias laws are Proposed until DEC-26; owner accounts come from MET-2.2 §1 and nowhere else; byte counts inside generated files were brought to a fixed point and checked against disk (HALT_LOG foot); mermaid parsed locally with the sprint-1 toolchain, CI re-runs it; the Impeccable detector's verdict on the v4 page is CI's, not this run's.
