# CENSUS — survey-3 Phase 1 (2026-09-05) — the four layers, mechanically, whole repository

Every number is a command's output; the command or tool is named beside it. Tool outputs: `tools/*.out.json`, `tools/refcheck.out.txt`; raw extracts: `raw/`. Row file: `census_rows.jsonl` (validated: `census_rows_validation.txt`). Detail tables: `L1_structure.md`, `L2_phase_matrix.md`, `L2_id_lifecycle.md`, `L2_governance.md`, `L3_terminology.md`, `L3_readability.md`, `L3_schema.md`, `L4_style.md`, `L4_form.md`.

## Scope and baseline
```
$ git rev-parse HEAD → 99e47f39e799be7a9e15dfefbce03396f88698f3 (main, A-007)
$ git ls-files | wc -l → 511
$ scope.files() (git ls-files minus .github/ .claude/ .impeccable/ 11_prompts/runs/ .gitignore .gitattributes .DS_Store) → 271
$ CHECKSUMS_BEFORE.txt → 511 lines (whole tree incl. tooling, excl. run dir, node_modules, .venv, engine binaries)
```
v1.0 seed said 267 at `f9f8ab2`; +4 = PROMPT-SURVEY-3, 3.1, 3.2 and AGENTS.md/CLAUDE.md (root) minus the seed's counting of `.gitignore` — reconciled: 271 is the count this run judges.

## Layer 1 (`depth.py`, `frontmatter.py`, `refcheck.py`, `graph.py`)

- depth histogram {'0': 5, '1': 127, '2': 43, '3': 43, '4': 53}; exceeding 4: **0**
- markdown 194; with frontmatter 110; without 84 → {'retained-original': 22, 'corpus-companion': 4, 'skeleton-banner': 55, 'root-governance': 3}; **omissions 0**
- core-key gaps **11** files; date-field variants {'date': 93, 'date_issued': 8, 'guidance_currency_date': 6}; doc_id repeats ['REG-NZ', 'REG-POSTURE'] (rule absent); ladder skips 2; inconsistent tables **0**
- references: dead 0 · anchors 0 · external 55 · glob 91 · future-output 608 · shorthand 3
- graph: reachable 271/271; classes {'DESIGN-LINKED': 174, 'LEDGER-OR-INDEX-ONLY': 97}; orphan candidates outside 06_: **7** (06_ stubs ×90 exempt)

## Layer 2 (`idgrammar.py`; `raw/L2_constructs_*.txt`; `raw/governance_census.json`)

- ID families 155 (2194 mints); mixed padding ['T', 'A', 'GPP', 'RG', 'E', 'B', 'NDG', 'AN', 'EX', 'M']; never declared (≥3 mints) ['A', 'D', 'ELSM', 'DEC', 'C', 'E', 'G', 'B', 'M', 'P', 'RECON-CEC', 'RECON-LEG', 'RECON-RWC', 'DEF', 'RECON-ABC', 'RECON-ANT', 'RECON-HDC', 'RECON-LBP', 'RECON-PRB', 'RECON-TXC', 'RECON-A', 'RECON-B', 'RECON-D', 'RECON-E', 'RECON-HX', 'RECON-LWC', 'RECON-C', 'RECON-F', 'RECON-G', 'RECON-H', 'RECON-I', 'RECON-J', 'RECON-K', 'RECON-L', 'W', 'J', 'EXEC']
- planning-construct families judged: 17 (L2_phase_matrix): PRESENT 7 (DR, T, ASSUME-REG, RUN+DR pair, PROC, V/SG/SD, CC/EX n/a) · PHASE-MAPPING-GAP 6 (G **CRITICAL**; C/DEC, TASK-REG, NZ/US/EU-TASK, TM WARNING; RG OPTIMISATION) · NDG cited to BSQ-0707 (law 11)
- governance over 51 load-bearing documents: owner 34 · cadence 40 · change_policy 22 · supersession 17 · read-through 21 · honesty 40 (see L2_governance for the per-file table; Phase 2 confirms each absence by reading)
- placeholders tree-wide: NEEDS DEFINITION 557 (67 files) · NEEDS SOURCE 19 · UNAVAILABLE 2 · PENDING-VALIDATOR 46 · PENDING-REGISTER-HOME 6 · PENDING-ENUMERATION 7 — vs 00_MANIFEST §6 (22/4/1/4/5/1, 2026-09-01)

## Layer 3 (`raw/terms_counts.txt`, `readability.py`, `schema_dupes.py`)

- terminology seeds: release spine 21 / SPINE- 1,092 (ruled C-02, glossed) · coder 432 / Guideline Compiler 47 (ruled C-07) · Observer 168 (consistent; cadence DEC-08) · R25 two labels (**unruled**) · W1–W5 vs W0–W11 (**unruled**) · glossary at Primer 0 §9+§11, cited as §11 (anchor drift) · `GLOSSARY.md` absent
- prefix collisions found by the ID census: **RG** (MAK-CEC vs RESEARCH-1), **CC** (HARDEN-2 vs MAK-LBP); label overlap T (tasks vs eval cases)
- readability: 154 files scored; median ASL 22.1, median FK 13.2; over ASL 35: **9**
- schema: 41 assets, 16 enums, duplicated enums **0**; template strings ×19 in skeleton stubs

## Layer 4 (`style_census.py`; L4_form)

- 19 HTML pages; implied token set 28 colours; pages with drift: **3** (the three diagram pages); 16 corpus pages drift 0
- document design system: INDEX ladder 7/7 identical; delta form 7/16 deviate (3 filed, 4 minor); frontmatter key aliases (date ×3 spellings; ID declaration ×3 keys) without a rule; status vocabulary = two class-appropriate conventions (no finding)

## Rows filed in Phase 1 (`census_rows.jsonl`, 59/59 valid)

```
{
 "total": 59,
 "valid": 59,
 "by_severity": {
  "WARNING": 18,
  "OPTIMISATION": 29,
  "NONE": 11,
  "CRITICAL": 1
 },
 "by_layer": {
  "L1-STRUCTURE": 18,
  "L2-REPLETENESS": 15,
  "L3-SEMANTICS": 17,
  "L4-IMPECCABLE": 9
 },
 "by_class": {
  "ID-SUPERSESSION-RULE-ABSENT": 1,
  "FRONTMATTER-SCHEMA-GAP": 6,
  "ORPHAN-IN-DESIGN-GRAPH": 7,
  "TABLE-OR-LADDER-DEFECT": 2,
  "PRESENT-IMPECCABLE": 10,
  "PHASE-MAPPING-GAP": 5,
  "ID-LIFECYCLE-GAP": 2,
  "TAXONOMY-CONFLICT": 4,
  "TAXONOMY-DUPLICATE": 2,
  "GOVERNANCE-GAP": 1,
  "PROPOSED-ADDITION": 1,
  "READABILITY-DENSE": 9,
  "SCHEMA-HARDCODE": 1,
  "STYLE-DRIFT": 3,
  "FORM-DEVIATION": 4,
  "TOOL-UNAVAILABLE": 1
 },
 "by_folder": {
  "CHAIN": 9,
  "00": 3,
  "05": 11,
  "06": 4,
  "07": 6,
  "10": 6,
  "11": 4,
  "01": 7,
  "03": 2,
  "08": 1,
  "09": 3,
  "04": 2,
  "02": 1
 },
 "by_executability": {
  "EXECUTABLE-AFTER-DECISION": 4,
  "CLAUDE-CODE-EXECUTABLE-NOW": 42,
  "CORPUS-OWNER": 1,
  "NONE": 12
 }
}
```
The single CRITICAL is MET-4's gap table (G-02 gates GATE-000; G-03 gates code freeze) with no owner/timeline/verification cells. Every CRITICAL/WARNING row carries `confidence`, `confidence_reason` and `attribution` (laws 16–17); all are PRE-EXISTING except the readability row on PROMPT-SURVEY-3.2 (NEW-SINCE-BASELINE).

## Tools unavailable
- mermaid parse (`node_modules` absent locally) → TOOL-UNAVAILABLE row QI-0059; CI result 2026-09-05 cited.
- Sub-agent fan-out not used (sequential run; ORIENTATION §Fan-out) → no COVERAGE-GAP possible from missing fragments.

