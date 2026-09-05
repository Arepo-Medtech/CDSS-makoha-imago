# IMPECCABILITY_QUEUE — survey-3 (2026-09-05) · PROMPT-SURVEY-3 v1.0 through 3.1 and 3.2

## 0. Append-only proof (law 1)
```
$ diff CHECKSUMS_BEFORE.txt CHECKSUMS_AFTER.txt | wc -l → 0      (511 files each; nothing outside 11_prompts/runs/2026-09-05_survey-3/ changed)
$ git status --short | grep -v '^?? 11_prompts/runs/2026-09-05_survey-3/' → (empty)
```

## a. Coverage statement

- Files in scope: **271** (`scope.files()`); every one appears in ≥1 row's `artifact_path` by path or by its declared group row (06_ skeleton stubs → `06_repositories/repo-skeletons/`; 16 corpus pages → `artifacts-html/ (16 pages)`; 07_ retained set → grouped FRONTMATTER row) — coverage check in each ASSESSMENT §6: 14/14 'yes'.
- Rows: **174** in `QI.jsonl` (174/174 valid — `QI_validation.txt`); Phase 1 59, Phase 2 +115, Phase 3 updated 12 (items/rows.jsonl). Severity: {'WARNING': 17, 'OPTIMISATION': 46, 'NONE': 104, 'CRITICAL': 7}; state {'OPEN': 170, 'DISMISSED-NOT-BLOCKING': 4}.
- Fragments: 14 (`CHECKPOINT.md`); COVERAGE-GAP events: 0 (sequential run).
- Calibration (3.1 D-4): 11 rows given `calibrated_weight` with a note; row count before/after identical (174); `evidence`/`attribution`/`confidence` untouched by calibration (Phase 3 changed confidence on 12 rows with reasons, before calibration). Re-examination trigger: CRITICAL 7 of 24 rows with weight ≥ 3 = 29 % > 10 % → each CRITICAL re-read: 1 is an executable document defect (MET-4), 6 are DECISION-PENDING rows whose weight mirrors survey-2's HUMAN-ONLY set (5/5/5/5/4/4) — they are decisions, not padding; retained.

## b. Verdict per folder, ROOT and CHAIN · layer scores

Verdict rule (v1.0 three states, applied mechanically then read): IMPECCABLE = no FAIL line and no OPEN row above NONE (own or CHAIN touching the folder) · IMPECCABLE-WITH-DECISIONS-PENDING = every remaining row is DECISION-PENDING / EXECUTABLE-AFTER-DECISION (own or CHAIN) · BELOW-STANDARD = an executable row remains (weights shown; '(OPTIMISATION rows only)' when none ≥ 3). CHAIN rows are attributed once (CHAIN) and listed under each folder they touch.

| Folder | Verdict | Q-line PASS rate (items × applicable lines) | Rows |
|---|---|---|---|
| ROOT | **IMPECCABLE-WITH-DECISIONS-PENDING** | 27/27 = 100 % | QI-0031 (TAXONOMY-DUPLICATE) |
| 00 | **BELOW-STANDARD (OPTIMISATION rows only)** | 19/26 = 73 % | QI-0002 w2 FRONTMATTER-SCHEMA-GAP; QI-0028 w2 GOVERNANCE-GAP; QI-0063 w2 GOVERNANCE-GAP; QI-0027 w1 ID-LIFECYCLE-GAP; QI-0064 w1 UNCLASSIFIED-QUALITY |
| 01 | **BELOW-STANDARD** | 55/66 = 83 % | QI-0018 w4 PHASE-MAPPING-GAP; QI-0019 w3 PHASE-MAPPING-GAP; QI-0023 w3 ID-LIFECYCLE-GAP; QI-0015 w1 TABLE-OR-LADDER-DEFECT; QI-0048 w1 FORM-DEVIATION; QI-0049 w1 FORM-DEVIATION; CHAIN: QI-0031 |
| 02 | **IMPECCABLE-WITH-DECISIONS-PENDING** | 158/159 = 99 % | QI-0031 (TAXONOMY-DUPLICATE) |
| 03 | **BELOW-STANDARD (OPTIMISATION rows only)** | 391/394 = 99 % | QI-0016 w1 TABLE-OR-LADDER-DEFECT; CHAIN: QI-0024, QI-0025 |
| 04 | **BELOW-STANDARD (OPTIMISATION rows only)** | 78/83 = 94 % | QI-0041 w1 READABILITY-DENSE; QI-0113 w1 UNCLASSIFIED-QUALITY; CHAIN: QI-0025, QI-0030 |
| 05 | **BELOW-STANDARD (OPTIMISATION rows only)** | 118/134 = 88 % | QI-0003 w2 FRONTMATTER-SCHEMA-GAP; QI-0004 w2 FRONTMATTER-SCHEMA-GAP; QI-0005 w2 FRONTMATTER-SCHEMA-GAP; QI-0010 w2 ORPHAN-IN-DESIGN-GRAPH; QI-0035 w1 READABILITY-DENSE; QI-0037 w1 READABILITY-DENSE; QI-0038 w1 READABILITY-DENSE; QI-0040 w1 READABILITY-DENSE; QI-0050 w1 FORM-DEVIATION; QI-0115 w1 UNCLASSIFIED-QUALITY; QI-0118 w1 UNCLASSIFIED-QUALITY; QI-0120 w1 UNCLASSIFIED-QUALITY |
| 06 | **BELOW-STANDARD (OPTIMISATION rows only)** | 560/566 = 99 % | QI-0006 w2 FRONTMATTER-SCHEMA-GAP; QI-0034 w1 READABILITY-DENSE |
| 07 | **BELOW-STANDARD (OPTIMISATION rows only)** | 80/88 = 91 % | QI-0007 w2 FRONTMATTER-SCHEMA-GAP; QI-0021 w2 PHASE-MAPPING-GAP; QI-0033 w2 READABILITY-DENSE; QI-0036 w2 READABILITY-DENSE; QI-0122 w1 UNCLASSIFIED-QUALITY; QI-0123 w1 UNCLASSIFIED-QUALITY |
| 08 | **BELOW-STANDARD (OPTIMISATION rows only)** | 28/32 = 88 % | QI-0022 w2 PHASE-MAPPING-GAP; QI-0124 w1 UNCLASSIFIED-QUALITY; CHAIN: QI-0024 |
| 09 | **BELOW-STANDARD (OPTIMISATION rows only)** | 78/81 = 96 % | QI-0043 w2 STYLE-DRIFT; QI-0044 w2 STYLE-DRIFT |
| 10 | **BELOW-STANDARD** | 140/148 = 95 % | QI-0020 w3 PHASE-MAPPING-GAP; QI-0011 w2 ORPHAN-IN-DESIGN-GRAPH; QI-0132 w1 UNCLASSIFIED-QUALITY; QI-0133 w1 UNCLASSIFIED-QUALITY; QI-0134 w1 UNCLASSIFIED-QUALITY; CHAIN: QI-0001, QI-0030 |
| 11 | **BELOW-STANDARD (OPTIMISATION rows only)** | 296/301 = 98 % | QI-0013 w2 ORPHAN-IN-DESIGN-GRAPH; QI-0014 w2 ORPHAN-IN-DESIGN-GRAPH; QI-0026 w1 TAXONOMY-DUPLICATE; QI-0039 w1 READABILITY-DENSE; QI-0165 w1 UNCLASSIFIED-QUALITY; QI-0166 w1 UNCLASSIFIED-QUALITY |
| CHAIN | **BELOW-STANDARD** | 1/5 = 20 % | QI-0024 w3 TAXONOMY-CONFLICT; QI-0025 w3 TAXONOMY-CONFLICT; QI-0032 w3 PROPOSED-ADDITION; QI-0031 w2 TAXONOMY-DUPLICATE; QI-0047 w2 FORM-DEVIATION |

No fourth state is used. "100 % complete" is not written anywhere in this run.

**Layer scores** (PASS lines / applicable PASS+FAIL lines across all fragments; N/A and EXEMPT excluded; addends shown):

| Layer | PASS | FAIL | Score |
|---|---|---|---|
| L1 | 1547 | 34 | 1547/1581 = 98 % |
| L2 | 300 | 21 | 300/321 = 93 % |
| L3 | 152 | 15 | 152/167 = 91 % |
| L4 | 30 | 11 | 30/41 = 73 % |

Reading: Layer 1 and Layer 4 are near-impeccable by measurement; Layer 2 carries the executable debt (owner/verification cells on gated constructs; ID declaration in 01_); Layer 3's failures are the two prefix collisions, two unruled labels and the glossary location — all with drafted alias laws.

## c. The Impeccability Queue (weight ≥ 3 after calibration; grouped by executability; ordered weight desc → earliest blocked gate → dependencies first)


### CLAUDE-CODE-EXECUTABLE-NOW (7)

| # | Row | W (c+r → cal) | Sev | Folder | Layer / Q | Class | Target asset | Observed state | Target state | Blocks | Confidence | Attribution | Owner |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | QI-0018 | 4 (2+2) | CRITICAL | 01 | L2/Q-D-08,P-D-10 | PHASE-MAPPING-GAP | `01_north-star-and-transformation/MET-4_gap_analysis_and_roadmap.md` | G rows carry evidence and severity only | MET-4.1 delta: one row per G with owner-role · person-or-DEC · RUN/gate (from EXEC-1) · exit evidence · register home (R | GATE-000 (G-02); code freeze (G-03); MET-4 P0 sequencing | 90 | PRE-EXISTING | Architecture owner / Programme lead [NEEDS DEFINIT |
| 2 | QI-0020 | 3 (1+2 → 3) | WARNING | 10 | L2/Q-D-08,P-D-14 | PHASE-MAPPING-GAP | `10_regulatory-execution/REG-POSTURE_v1.2.md §7; REG-NZ_v1.1 §8; REG-US` | tasks carry gate only | a companion 'REG-TASK-OWNER-MAP' (one table: task · owner-role from DR-n · evidence artifact named · R30.3 row) read wit | RUN-0..4 task-level accountability; R30.3 owner column (inherits 'none stated at | 85 | PRE-EXISTING | Regulatory owner [NEEDS DEFINITION — G-09] (drafti |
| 3 | QI-0025 | 3 (1+2 → 3) | WARNING | CHAIN | L3/Q-D-12,Q-D-10 | TAXONOMY-CONFLICT | `04_hardening/HARDEN-2_hardening_spec.md (CC-1..8) ↔ 03_makoha-butterfl` | prefix collision across a spec and a corpus volume | alias law in HARDEN-2.2 (or MET-2.2): 'CC-n in 04_/05_/06_/HARDEN rows = HARDEN-2 class bar; MAK-LBP CC-n resolves only  | every HARDEN-1.1/3.1 class cell; R29 class enum (DEC-02) | 90 | PRE-EXISTING | Architecture owner + Corpus owner (MAK-LBP) |
| 4 | QI-0019 | 3 (1+2 → 3) | WARNING | 01 | L2/Q-D-08,Q-D-09 | PHASE-MAPPING-GAP | `01_north-star-and-transformation/MET-2_conflict_and_decision_register.` | DEC rows: owner/gate/state; no closure evidence; families undeclared | MET-2.2 delta: (a) 'Closes on' column per DEC (evidence artifact + where recorded), per C (the DEC or the ruling record) | every DEC closure (what counts as closed?); R26/R27 opening (DEC-02) | 85 | PRE-EXISTING | Architecture owner |
| 5 | QI-0024 | 3 (1+2 → 3) | WARNING | CHAIN | L3/Q-D-12,Q-D-10 | TAXONOMY-CONFLICT | `03_makoha-butterfly-corpus/corpus-md/compound-eyes-corpus_v1.1.md (RG-` | prefix collision, no alias law | alias law in RESEARCH-1.2 (and MET-2.2 as the namespace register): 'RG-nn (2-digit) = research gap, home RESEARCH-1.n; R | R30/RG resolution in any register join; INDEX-08 §3 RG mirror | 90 | PRE-EXISTING | Architecture owner (namespace) + Corpus owner (MAK |
| 6 | QI-0032 | 3 (1+2 → 3) | WARNING | CHAIN | L3/Q-D-13,Q-D-12 | PROPOSED-ADDITION | `GLOSSARY.md (absent)` | five definition sites, no consolidation | GLOSSARY.md at root: term · definition (quoted, with source path:line) · ruled by (C-nn / §) · aliases · owning volume;  | every reader of two-term pairs (release spine/SPINE-n; coder/Guideline Compiler; | 80 | PRE-EXISTING | Architecture owner (ratifies); executor drafts |
| 7 | QI-0023 | 3 (1+2 → 3) | WARNING | 01 | L2/Q-D-09,P-D-04 | ID-LIFECYCLE-GAP | `01_north-star-and-transformation/` | undeclared, uncensused | declared + censused in MET-2.2 / MET-4.1 (rows QI-0018/QI-0019 carry the drafts) | R26/R27 opening (DEC-02); every citation of a DEC-nn (resolution by grep only) | 90 | PRE-EXISTING | Architecture owner |

### EXECUTABLE-AFTER-DECISION (3)

| # | Row | W (c+r → cal) | Sev | Folder | Layer / Q | Class | Target asset | Observed state | Target state | Blocks | Confidence | Attribution | Owner |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | QI-0001 | 3 (1+2 → 3) | WARNING | CHAIN | L1/Q-D-05,P-D-03 | ID-SUPERSESSION-RULE-ABSENT | `10_regulatory-execution/REG-POSTURE_v1.2.md; 10_regulatory-execution/R` | superseded versions share doc_id; disambiguation only by `supersedes:` and INDEX-10 §4 pro | one sentence of law: superseded versions keep doc_id and MUST carry `supersedes:`; citations MUST name version (README ' | W11 sweep of 10_ (which file is `REG-POSTURE`?); every future versioned file | 90 | PRE-EXISTING | Architecture owner (Arch §13.3 namespace law) |
| 2 | QI-0029 | 3 (1+2 → 3) | WARNING | 09 | L3/Q-D-12 | TAXONOMY-CONFLICT | `09_diagrams/register_topology_v3.mermaid; 02_/architecture_and_integra` | two labels | one label in Arch §12.2 (authoritative) with the other as alias; IMAGO-3 v4 successor | IMAGO-3 v4 label; R25 opening (L1) | 90 | PRE-EXISTING | Architecture owner |
| 3 | QI-0030 | 3 (1+2 → 3) | WARNING | CHAIN | L3/Q-D-12,Q-D-10 | TAXONOMY-CONFLICT | `10_regulatory-execution/FOLD-1_antennae_fold_worklist.md (W1–W5) ↔ 04_` | one token, two worklists | alias law: 'Unqualified W-n means HARDEN-3 (the pass); FOLD-1 steps are cited FW-n or FOLD-1 W-n' — PROMPT-FOLD-1 alread | PROMPT-FOLD-1 and PROMPT-HARDEN run instructions; HARDEN-3.1 wave census | 90 | PRE-EXISTING | Architecture owner |

### HUMAN-ONLY (8)

| # | Row | W (c+r → cal) | Sev | Folder | Layer / Q | Class | Target asset | Observed state | Target state | Blocks | Confidence | Attribution | Owner |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | QI-0170 | 5 (2+3) | CRITICAL | CHAIN | L2/Q-D-08,Q-D-11 | DECISION-PENDING | `DEC-22` | — | DEC-22 (MET-2.1) | RUN-0 start; DEPLOY-1.1 / IMAGO-4 v2 in force | 100 | PRE-EXISTING | Founder (programme) |
| 2 | QI-0169 | 5 (2+3) | CRITICAL | CHAIN | L2/Q-D-08,Q-D-11 | DECISION-PENDING | `DEC-10` | — | DEC-10 / DEC-11 (MET-2) | W0 → all waves; PROMPT-HARDEN start; code freeze | 100 | PRE-EXISTING | Programme lead / Founder [NEEDS DEFINITION] |
| 3 | QI-0167 | 5 (2+3) | CRITICAL | CHAIN | L2/Q-D-08,Q-D-11 | DECISION-PENDING | `DEC-02` | — | DEC-02 (MET-2) | R29/R30 existence; register homes for T-nnn, R29-row and every R30.3 row; 05_ MO | 100 | PRE-EXISTING | Architecture owner |
| 4 | QI-0168 | 5 (2+3) | CRITICAL | CHAIN | L2/Q-D-08,Q-D-11 | DECISION-PENDING | `DEC-09` | — | DEC-09 (MET-2) | 98 HARDEN owner cells; REPO-MAP v3; cdss-compiler primer (BSQ-0391) | 100 | PRE-EXISTING | Programme lead [NEEDS DEFINITION] |
| 5 | QI-0171 | 4 (2+2) | CRITICAL | CHAIN | L2/Q-D-08,Q-D-11 | DECISION-PENDING | `G-09` | — | G-09 / proposed DEC-23 (MET-4; A-004) | regulatory owner cells ×15 (HARDEN-1.1); REG-POSTURE owner field (§12.3); infra  | 100 | PRE-EXISTING | Founder |
| 6 | QI-0173 | 4 (2+2) | CRITICAL | CHAIN | L2/Q-D-08,Q-D-11 | DECISION-PENDING | `DEC-13` | — | DEC-13 / DEC-14 (MET-2.1) | MAK-GOV integration delta (BSQ-0707); NDG verification cells; cdss-compiler prim | 100 | PRE-EXISTING | Architecture owner; Founder + advisor |
| 7 | QI-0172 | 3 (2+1) | WARNING | CHAIN | L2/Q-D-08,Q-D-11 | DECISION-PENDING | `DEC-08` | — | DEC-08 (MET-2) | Observer cadence text in Arch §13.7 / GOV-1 / OPS-1 | 100 | PRE-EXISTING | Architecture owner |
| 8 | QI-0174 | 3 (2+1) | WARNING | CHAIN | L2/Q-D-08,Q-D-11 | DECISION-PENDING | `DEC-01` | — | DEC-01 (MET-2) | regeneration of derived artifacts (PROC-09-REGEN); IMAGO-3 v4 / cdss_diagrams_v4 | 100 | PRE-EXISTING | Regulatory + architecture owners |

### CORPUS-OWNER (0)

(none at weight ≥ 3)

### c.1 Build specs and remediation drafts — every EXECUTABLE-NOW row at weight ≥ 3, full text (survey-2 eleven fields + the architect's four)


#### QI-0018 — `01_north-star-and-transformation/MET-4_gap_analysis_and_roadmap.md`

- **[CRITICAL]** · **Target Asset:** `01_north-star-and-transformation/MET-4_gap_analysis_and_roadmap.md` · **Observed State:** G rows carry evidence and severity only · **Target State:** MET-4.1 delta: one row per G with owner-role · person-or-DEC · RUN/gate (from EXEC-1) · exit evidence · register home (R26/R27/R30/MET-2), plus req_prefix G / req_count 11 and a census · **Exemplar:** `07_deployment-and-operations/DEPLOY-1.1_run-map_delta.md (DR table: owner · person/DEC · exit evidence · failure → gate)`
- **Statement:** The eleven gaps G-01..G-11 are tabled with Gap · Evidence · Severity · Delta only: no owner, no person-or-DEC, no timeline or gate per row, no verification/exit evidence and no register home; the roadmap P0–P3 bullets allude to some gaps by phase. G-02 gates GATE-000 and G-03 gates code freeze, so an architectural principle (each gap) is defined without an implementation timeline, resource owner or verification metric.
- **Evidence:** 01_/MET-4 l.9 `| Gap | Evidence | Severity | Delta since v1.0 |`; l.24–27 roadmap bullets; MET-4 frontmatter has no req_prefix; DEPLOY-1.1 DR-1..7 (l.45–66) is the form that would satisfy the cells
- **Confidence:** 90 — Phase 3 full read (2,400 bytes): the table has exactly four columns; the roadmap is four bullets naming decisions and gates but no gap ids except by allusion; no owner appears anywhere in the file; MET-2 supplies owners only for the decisions, not the gaps
- **Target path** · 01_north-star-and-transformation/MET-4.1_gap_register_delta.md
- **Class + lines** · GAP/DECISION REGISTER + DELTA; P-D-01,02,04,08,10,11,14
- **Mandatory sections/fields** · frontmatter with req_prefix G / req_count 11; D-1 table with the five execution columns; census; self-audit (every cited DEC/RUN/GATE exists)
- **Inputs** · MET-4; MET-2; MET-2.1; EXEC-1 RUN table; DEPLOY-1.1 DR table
- **Laws** · append-only; delta pattern; OPEN means OPEN (no DEC closed by filling a cell); persons stay [NEEDS DEFINITION] + DEC
- **Evidence to capture** · grep of each cited ID in its source, pasted
- **Acceptance test** · 11 rows, no empty cell (or [NEEDS DEFINITION] + DEC), census = 11
- **Closes rows** · —
- **HARDEN linkage** · HARDEN-1.1 row for MET-4 (+ new row for the delta — HARDEN-1.2 debt)
- **Ratifying owner** · Architecture owner
- **Depends on** · —

**Remediation draft:**

```
---
doc_id: MET-4.1
title: "MET-4.1 — gap register delta: owner, decision, run/gate, exit evidence and register home per gap"
version: "1.1-delta"
status: "Proposed. Additive delta over MET-4 v1.1 (not edited); read MET-4 through this file."
supersedes: "nothing"
applies_to: "01_north-star-and-transformation/MET-4_gap_analysis_and_roadmap.md"
change_policy: "Additive delta per the MET-1.1 pattern"
req_prefix: G
req_count: 11
---
## D-1 — execution columns
| Gap | Owner (role) | Person / DEC | RUN / gate (EXEC-1) | Exit evidence | Register home |
|---|---|---|---|---|---|
| G-01 | Architecture owner | DEC-04 | RUN-1 (fabric v0) | fabric-v0 schema in cdss-spine; R25 row | R26 |
| G-02 | Regulatory owner | DEC-01; ASSUME-REG-001/002 | RUN-0 → GATE-000 | counsel opinion (ATTESTED/REFUTED, dated) | R30 |
| G-03 | MT2 operator | DEC-10, DEC-11 | MET-4 P0 (parallel with RUN-0) | R29 row zero HARDENED; W0 report | R29 |
| … (G-04..G-11 from MET-2 DEC rows and EXEC-1 RUN table; every person [NEEDS DEFINITION] names its DEC) |
## Census — G: 11 = 11 rows
## Self-audit — every DEC/RUN/GATE cited exists (grep pasted)
```

#### QI-0020 — `10_regulatory-execution/REG-POSTURE_v1.2.md §7; REG-NZ_v1.1 §8; REG-US_v1.0; REG-EU_v1.0`

- **[WARNING]** · **Target Asset:** `10_regulatory-execution/REG-POSTURE_v1.2.md §7; REG-NZ_v1.1 §8; REG-US_v1.0; REG-EU_v1.0` · **Observed State:** tasks carry gate only · **Target State:** a companion 'REG-TASK-OWNER-MAP' (one table: task · owner-role from DR-n · evidence artifact named · R30.3 row) read with each posture; never an edit to the posture files · **Exemplar:** `07_deployment-and-operations/DEPLOY-1.1_run-map_delta.md (DR-1..7 owner + exit evidence)`
- **Statement:** Every TASK-REG / NZ-TASK / US-TASK / EU-TASK row carries ID · Task · Gate only: no owner-role per task and no named evidence artifact per task (the §0.4 vocabulary says DONE-WITH-EVIDENCE means 'evidence artifact named', but the table has no cell for it). Owners reach a task only through DEPLOY-1.1's DR-n → phase mapping.
- **Evidence:** REG-POSTURE l.872 `| ID | Task | Gate |` (×5 phase tables, l.874–940); REG-NZ l.420–429; REG-EU l.329–346; REG-US l.337–; DEPLOY-1.1 l.45–51 owner roles per DR; R30.3 rows carry `owner: cdss-governance (register owner; row owner role per source)` — i.e. the source names none
- **Confidence:** 85 — Phase 3: all four task tables read in full (REG-POSTURE §7 five phase tables l.872–940; REG-NZ §8 l.420–429; REG-US l.337–; REG-EU l.329–346) — every header is ID · Task · Gate; no owner word appears in any task cell except as a cross-reference to a DEC
- **Target path** · 10_regulatory-execution/REG-TASK-OWNERS_companion.md
- **Class + lines** · REGULATORY companion; P-D-01,02,03,07,10,14
- **Mandatory sections/fields** · frontmatter ADVISORY_ONLY; crosswalk table for 60 tasks; census 24+10+13+13; self-audit: every task id exists in its posture and in R30.3
- **Inputs** · REG-POSTURE v1.2 §7; REG-NZ v1.1 §8; REG-US §; REG-EU §; DEPLOY-1.1 DR table; R30.3
- **Laws** · append-only; ADVISORY_ONLY; no clinical content; OPEN means OPEN (no task status touched)
- **Evidence to capture** · grep of every task id in R30.3 pasted
- **Acceptance test** · 60/60 tasks mapped; 0 owner cells empty ([NEEDS DEFINITION] + DEC allowed)
- **Closes rows** · —
- **HARDEN linkage** · new HARDEN-1.2 row (debt)
- **Ratifying owner** · Regulatory owner [NEEDS DEFINITION — G-09]
- **Depends on** · —

**Remediation draft:**

```
---
doc_id: REG-TASK-OWNERS
title: "REG-TASK-OWNERS — task → owner-role → evidence artifact crosswalk for TASK-REG, NZ-TASK, US-TASK, EU-TASK"
status: "Proposed companion; ADVISORY_ONLY; edits nothing; owner roles are DEPLOY-1.1 DR-n roles, persons [NEEDS DEFINITION]"
authority: ADVISORY_ONLY
applies_to: REG-POSTURE v1.2 §7; REG-NZ v1.1 §8; REG-US v1.0; REG-EU v1.0
---
| Task | Gate | Owner role (DR-n) | Evidence artifact (DONE-WITH-EVIDENCE means…) | R30.3 row |
|---|---|---|---|---|
| TASK-REG-001 | GATE-000 | Founder (programme) — DR-2 | intended purpose statement v1.0 (DRAFT_TASK-REG-001 → signed) | TASK-REG-001 |
| TASK-REG-002 | GATE-000 | Regulatory owner — DR-2 | counsel's written opinion (dated) | TASK-REG-002 |
| … 24 + 10 + 13 + 13 rows |
```

#### QI-0025 — `04_hardening/HARDEN-2_hardening_spec.md (CC-1..8) ↔ 03_makoha-butterfly-corpus/corpus-md/l`

- **[WARNING]** · **Target Asset:** `04_hardening/HARDEN-2_hardening_spec.md (CC-1..8) ↔ 03_makoha-butterfly-corpus/corpus-md/labial-palps-corpus_v1.0.md (CC-1..5)` · **Observed State:** prefix collision across a spec and a corpus volume · **Target State:** alias law in HARDEN-2.2 (or MET-2.2): 'CC-n in 04_/05_/06_/HARDEN rows = HARDEN-2 class bar; MAK-LBP CC-n resolves only inside 03_; the R29 schema `class` enum spells the bars HCC-n or CLASS-n on ratification' — corpus untouched · **Exemplar:** `01_north-star-and-transformation/MET-2.1_decision_register_delta.md (Alias law)`
- **Statement:** One prefix, two families: HARDEN-2/2.1 class bars CC-1..CC-8 (cited by every HARDEN row, INDEX and ledger as 'class CC-5') and MAK-LBP requirements CC-1..5 (clinician-UI corpus). 'CC-5' means a CI-configuration class bar in 04_/06_ and a clinician-UI requirement in 03_.
- **Evidence:** tools/idgrammar.py CC: minted 22 in 4 files — HARDEN-2.1 8, HARDEN-2 8, labial-palps-corpus_v1.0.md 5, primer_LBP 1; HARDEN-1.1 class column uses CC-n on 275 rows
- **Confidence:** 90 — Phase 3: HARDEN-2 CC-1..8 table and MAK-LBP req_prefixes re-read; HARDEN-1.1 class column cites CC-n 275 times
- **Target path** · 04_hardening/HARDEN-2.2_alias_delta.md (or the MET-2.2 namespace section)
- **Class + lines** · SPEC DELTA; P-D-04
- **Mandatory sections/fields** · alias-law paragraph
- **Inputs** · HARDEN-2; HARDEN-2.1; labial-palps-corpus_v1.0.md
- **Laws** · append-only; corpus never edited; R29 schema unchanged (DEC-02)
- **Evidence to capture** · grep counts pasted
- **Acceptance test** · both families enumerated
- **Closes rows** · —
- **HARDEN linkage** · HARDEN-1.1 rows
- **Ratifying owner** · Architecture owner
- **Depends on** · —

**Remediation draft:**

```
**Alias law (CC):** In 04_, 05_, 06_ and every HARDEN/R29 row, `CC-n` names a HARDEN-2 class bar (CC-1..CC-8). In 03_, `CC-n` names a MAK-LBP requirement (CC-1..5). A cross-folder citation MUST qualify: `HARDEN-2 CC-5` / `MAK-LBP CC-2`. The R29 `class` field keeps `CC-n` (schema unchanged); the qualifier is prose-only.
```

#### QI-0019 — `01_north-star-and-transformation/MET-2_conflict_and_decision_register.md; MET-2.1`

- **[WARNING]** · **Target Asset:** `01_north-star-and-transformation/MET-2_conflict_and_decision_register.md; MET-2.1` · **Observed State:** DEC rows: owner/gate/state; no closure evidence; families undeclared · **Target State:** MET-2.2 delta: (a) 'Closes on' column per DEC (evidence artifact + where recorded), per C (the DEC or the ruling record); (b) frontmatter req_prefixes [C, DEC] with counts and a census; (c) the doc_id supersession rule (QI-0001) if the Architecture owner rules it here; (d) glossary anchor erratum (§9 not §11) · **Exemplar:** `10_regulatory-execution/REG-POSTURE_v1.2.md §0.4 (closure evidence rule) + §12.1 census`
- **Statement:** DEC-01..22 carry owner, blocking gate/trigger and state, but no column says what artifact evidences closure (e.g. 'ratification recorded as an Arch §12.2 amendment', 'counsel letter dated'); C-01..16 carry rulings but no exit evidence beyond the DEC they escalate to. The DEC/C/G families are minted across MET-1 §17, MET-2, MET-2.1 and MET-4 with no req_prefix declaration and their register homes are PENDING-REGISTER-HOME (R26/R27).
- **Evidence:** MET-2 l.29 `| DEC | Decision | Blocking | Owner | State |`; MET-2.1 l.22 `| ID | Decision | Trigger/When | Owner | Status |`; tools/idgrammar.py DEC 32 mints / declared_in_files 0; C 26 / 0; G 21 / 0; MET-2 status 'PENDING-REGISTER-HOME'
- **Confidence:** 85 — columns read from the two tables; the missing cell is unambiguous; the ID declaration gap is tool-confirmed
- **Target path** · 01_north-star-and-transformation/MET-2.2_decision_register_delta.md
- **Class + lines** · GAP/DECISION REGISTER + DELTA; P-D-04,08,10,11,14
- **Mandatory sections/fields** · D-1 closes-on table (every DEC); D-2 req_prefixes + census; D-3 glossary anchor erratum; self-audit
- **Inputs** · MET-2; MET-2.1; Arch §12.2/§14.1; Primer 0 §9/§11
- **Laws** · append-only; OPEN means OPEN (a 'closes on' cell describes evidence, it closes nothing)
- **Evidence to capture** · census counts pasted
- **Acceptance test** · 23 DEC rows + 16 C rows each with a non-empty closes-on cell; census = counts
- **Closes rows** · —
- **HARDEN linkage** · HARDEN-1.1 rows for MET-2/MET-2.1; new row (debt)
- **Ratifying owner** · Architecture owner
- **Depends on** · —

**Remediation draft:**

```
## D-1 — closure evidence per decision
| DEC | Closes on (evidence artifact) | Recorded in |
|---|---|---|
| DEC-01 | counsel attestation + regenerated derived artifacts (G-10 PROC-09-REGEN run) | R30 GATE-000 row; 00_MANIFEST amendment |
| DEC-02 | Arch §12.2 amendment naming R29/R30 | Arch annex; R29 row zero |
| … |
## D-2 — ID declaration
req_prefixes: [C, DEC]; req_count: 16 + 23 (incl. proposed DEC-23) — census table
## D-3 — glossary anchor
C-02 and Arch §14.1 cite 'Primer 0 §11 glossary'; the glossary heading is §9 (l.68) and the additions are under §11 (l.98). Read both as 'Primer 0 §9 + §11 annex'.
```

#### QI-0024 — `03_makoha-butterfly-corpus/corpus-md/compound-eyes-corpus_v1.1.md (RG-1..8) ↔ 08_research/`

- **[WARNING]** · **Target Asset:** `03_makoha-butterfly-corpus/corpus-md/compound-eyes-corpus_v1.1.md (RG-1..8) ↔ 08_research/RESEARCH-1_findings_gaps_source_map.md (RG-01..08)` · **Observed State:** prefix collision, no alias law · **Target State:** alias law in RESEARCH-1.2 (and MET-2.2 as the namespace register): 'RG-nn (2-digit) = research gap, home RESEARCH-1.n; RG-n (1-digit) = MAK-CEC requirement, home MAK-CEC. Citations MUST use the padded form; RESEARCH-1's family is renamed RGAP- in any new minting' — corpus untouched · **Exemplar:** `01_north-star-and-transformation/MET-2.1_decision_register_delta.md (Alias law paragraph)`
- **Statement:** One prefix, two requirement-bearing families: MAK-CEC mints RG-1..8 (regulatory-guardrail requirements, 1-digit) and RESEARCH-1 mints RG-01..08 (research gaps, 2-digit). A citation 'RG-3' resolves to a corpus MUST; 'RG-03' to a research gap; nothing states this.
- **Evidence:** tools/idgrammar.py RG: minted 31 in 5 files, padding {'1d': 9 (compound-eyes-corpus_v1.1.md 8, primer_CEC 1), '2d': 22 (INDEX-08 8, RESEARCH-1.1 8, RESEARCH-1 6)}
- **Confidence:** 90 — Phase 3: both minting positions re-read (MAK-CEC req_prefixes frontmatter + §RG blocks; RESEARCH-1 §3 table); no alias law found by grep "alias" in 08_/03_
- **Target path** · 08_research/RESEARCH-1.2_triggers_delta.md (same file as the RG trigger row) + MET-2.2 namespace note
- **Class + lines** · RESEARCH DELTA; P-D-04
- **Mandatory sections/fields** · alias-law paragraph; census
- **Inputs** · RESEARCH-1; compound-eyes-corpus_v1.1.md frontmatter
- **Laws** · append-only; corpus never edited
- **Evidence to capture** · grep counts of both forms pasted
- **Acceptance test** · both forms enumerated; new prefix declared
- **Closes rows** · —
- **HARDEN linkage** · HARDEN-1.1 rows
- **Ratifying owner** · Architecture owner; Corpus owner
- **Depends on** · —

**Remediation draft:**

```
**Alias law (RG):** `RG-nn` two-digit ids are research gaps (RESEARCH-1/1.1; INDEX-08 §3); `RG-n` one-digit ids are MAK-CEC requirements (compound-eyes-corpus v1.1, Part 4). The two families share a prefix by accident; neither is renamed retrospectively. New research gaps from RESEARCH-1.2 onward are minted `RGAP-nnn`; `RG-01..08` remain valid citations and resolve to RESEARCH-1.
```

#### QI-0032 — `GLOSSARY.md (absent)`

- **[WARNING]** · **Target Asset:** `GLOSSARY.md (absent)` · **Observed State:** five definition sites, no consolidation · **Target State:** GLOSSARY.md at root: term · definition (quoted, with source path:line) · ruled by (C-nn / §) · aliases · owning volume; corpus definitions cited by reference, never restated beyond one line · **Exemplar:** `02_cdss-stack-augmented/primer_0_ecosystem_explainer.md §9 (form) + MET-2.1 alias law (aliases column)`
- **Statement:** No consolidated glossary exists; house terms are defined in Primer 0 §9 + §11 annex (8 additions), MAK-FFC Part 1, MAK-LWC/RWC vocabularies and the C-02/C-07 rulings — five places for a multi-disciplinary reader to check. The architect's Layer 3 (taxonomy consolidation) and both rulings ('glossary guards both terms') imply one citable location.
- **Evidence:** ls GLOSSARY.md → absent; raw/terms_counts.txt: 'glossary' 26 occurrences in 13 files; Primer 0 l.68, l.98; MET-2 C-07; Arch §14.1
- **Confidence:** 80 — absence is command output; the implied law is the architect's Layer 3 plus two in-repo rulings that cite a glossary
- **Target path** · GLOSSARY.md (root)
- **Class + lines** · ROOT LOOSE FILE; P-D-01,02,07,13,16
- **Mandatory sections/fields** · frontmatter; term table with source path:line per row; aliases column; open rulings marked OPEN
- **Inputs** · Primer 0 §9/§11; MAK-FFC Part 1; MAK-LWC/RWC vocab (by reference); MET-2/2.1 C rows; Arch §13.2/§14.1
- **Laws** · append-only (new file); no corpus text restated beyond one quoted line; OPEN rulings stay OPEN
- **Evidence to capture** · grep of each source line pasted
- **Acceptance test** · every C-02/C-07/§13.2 term present; every row's source resolves (refcheck)
- **Closes rows** · —
- **HARDEN linkage** · HARDEN-1.2 row (debt); 00_MANIFEST A-00n row; README 'Where to read it' row (README is outside 00_–11_ law? no — README.md is root; a successor line via amendment)
- **Ratifying owner** · Architecture owner
- **Depends on** · —

**Remediation draft:**

```
---
doc_id: GLOSSARY
title: "GLOSSARY — house vocabulary of the Mākoha Imago design record: terms, sources, rulings, aliases"
version: "1.0"
date: "2026-09-0x"
status: "Proposed. Consolidates by reference; defines nothing new; every row cites its source line and, where a term was ruled, the C-nn row. Corpus terms are one-line citations into their volume."
change_policy: "Additive; a term is never deleted — superseded terms gain a 'superseded by' cell."
---
| Term | Definition (quoted) | Source | Ruling | Aliases / not to be confused with |
|---|---|---|---|---|
| release spine | "house term for this project's deterministic release path + signed registry" | Primer 0 l.98 | C-02; Arch §14.1 | ≠ SPINE-n (MAK-FFC requirement ids) |
| Guideline Compiler | "the only path by which clinical logic enters the engine plane" | MAK-FFC EN-3 | C-07 | ≠ coder (concept coder, Arch §13.2) |
| Implementer Contract (IMPL) | "coder_contract.md is adopted under the name Implementer Contract" | Arch §13.2 | rename notice | coder_contract.md |
| Observer | "never holds EVAL credentials, never reads casebundle content… one adjudication per level exit" | Arch §13.7 | DEC-08 (cadence, Open) | — |
| R25 | two labels — Arch §12.2 / IMAGO-3 | … | BSQ-0602 OPEN | label under ruling |
| W-n | HARDEN-3 wave (unqualified) / FOLD-1 step (qualified) | … | BSQ-0711 OPEN | — |
| … Fabric, Argument, Face, Register-render law, Deviation, GPP, Wing-beat (Primer 0 l.98) …
```

#### QI-0023 — `01_north-star-and-transformation/`

- **[WARNING]** · **Target Asset:** `01_north-star-and-transformation/` · **Observed State:** undeclared, uncensused · **Target State:** declared + censused in MET-2.2 / MET-4.1 (rows QI-0018/QI-0019 carry the drafts) · **Exemplar:** `10_regulatory-execution/REG-SPRINT-1.2_census_delta.md (declares and censuses an older file's families)`
- **Statement:** The C, DEC and G families (26 + 32 + 21 mints across MET-1 §17, MET-2, MET-2.1, MET-4) are declared in no frontmatter, censused nowhere, and their register homes are PENDING-REGISTER-HOME; every other requirement-bearing family in the tree (REG-*, T, DR, TM, PROC, NDG, EX, corpus families) is declared and censused.
- **Evidence:** tools/idgrammar.py: DEC minted 32 / declared_in_files 0 / home MET-2/MET-2.1 (by reading); C 26/0; G 21/0; MET-2 status 'PENDING-REGISTER-HOME per the Ecosystem v2.0 precedent'
- **Confidence:** 90 — tool-confirmed on all four files; the exemplar form exists in the same tree
- **Target path** · MET-2.2 + MET-4.1 (same deliverables as the PHASE-MAPPING rows)
- **Class + lines** · DELTA; P-D-04, P-D-08
- **Mandatory sections/fields** · req_prefixes + census in each
- **Inputs** · MET-1 §17; MET-2; MET-2.1; MET-4
- **Laws** · append-only
- **Evidence to capture** · census pasted
- **Acceptance test** · counts equal grep
- **Closes rows** · —
- **HARDEN linkage** · HARDEN-1.1 rows
- **Ratifying owner** · Architecture owner
- **Depends on** · MET-2.2, MET-4.1

**Remediation draft:**

```
see MET-2.2 D-2 and MET-4.1 frontmatter in the two rows above
```

## d. OPTIMISATION rows (weight ≤ 2 after calibration) — listed, recommended where marked, never required

| Row | W | Folder | Class | Target asset | Target state / remedy | Exec |
|---|---|---|---|---|---|---|
| QI-0021 | 2 | 07 | PHASE-MAPPING-GAP | `07_deployment-and-operations/SEC-2_threat-model_and_data-flo` | SEC-2.1: a 'Verification evidence' column per TM (the artifact GATE-002/003 will hold) and a register-home pro | CLAUDE-CODE-EXECUTABLE |
| QI-0002 | 2 | 00 | FRONTMATTER-SCHEMA-GAP | `00_MANIFEST.md` | a one-line frontmatter delta (RESEARCH-1.1 D-1 pattern: 'Read as: version/date …') in the folder's next delta | CLAUDE-CODE-EXECUTABLE |
| QI-0003 | 2 | 05 | FRONTMATTER-SCHEMA-GAP | `05_registers-and-contracts/CONTRACT-ARG-1_argument_schema.md` | a one-line frontmatter delta (RESEARCH-1.1 D-1 pattern: 'Read as: version/date …') in the folder's next delta | CLAUDE-CODE-EXECUTABLE |
| QI-0004 | 2 | 05 | FRONTMATTER-SCHEMA-GAP | `05_registers-and-contracts/REG-R29_hardening_coverage_ledger` | a one-line frontmatter delta (RESEARCH-1.1 D-1 pattern: 'Read as: version/date …') in the folder's next delta | CLAUDE-CODE-EXECUTABLE |
| QI-0005 | 2 | 05 | FRONTMATTER-SCHEMA-GAP | `05_registers-and-contracts/REG-R30_regulatory_posture_regist` | a one-line frontmatter delta (RESEARCH-1.1 D-1 pattern: 'Read as: version/date …') in the folder's next delta | CLAUDE-CODE-EXECUTABLE |
| QI-0006 | 2 | 06 | FRONTMATTER-SCHEMA-GAP | `06_repositories/REPO-MAP_v2.md` | a one-line frontmatter delta (RESEARCH-1.1 D-1 pattern: 'Read as: version/date …') in the folder's next delta | CLAUDE-CODE-EXECUTABLE |
| QI-0007 | 2 | 07 | FRONTMATTER-SCHEMA-GAP | `07_deployment-and-operations/DEPLOY-1_deployment_plan_and_se` | a one-line frontmatter delta (RESEARCH-1.1 D-1 pattern: 'Read as: version/date …') in the folder's next delta | CLAUDE-CODE-EXECUTABLE |
| QI-0010 | 2 | 05 | ORPHAN-IN-DESIGN-GRAPH | `05_registers-and-contracts/REG-R29.1_schema_twin_delta.md` | ≥1 citation from the consuming document (e.g. CONTRACT-ARG-1's next delta names CONTRACT-DEV-1.schema.json; RE | CLAUDE-CODE-EXECUTABLE |
| QI-0011 | 2 | 10 | ORPHAN-IN-DESIGN-GRAPH | `10_regulatory-execution/REG-POSTURE_v1.2_CONTENTS.md` | ≥1 citation from the consuming document (e.g. CONTRACT-ARG-1's next delta names CONTRACT-DEV-1.schema.json; RE | CLAUDE-CODE-EXECUTABLE |
| QI-0013 | 2 | 11 | ORPHAN-IN-DESIGN-GRAPH | `11_prompts/PROMPT-FOLD-1_antennae_v1.2_fold.md` | ≥1 citation from the consuming document (e.g. CONTRACT-ARG-1's next delta names CONTRACT-DEV-1.schema.json; RE | CLAUDE-CODE-EXECUTABLE |
| QI-0014 | 2 | 11 | ORPHAN-IN-DESIGN-GRAPH | `11_prompts/PROMPT-PRM-SERIES_index.md` | ≥1 citation from the consuming document (e.g. CONTRACT-ARG-1's next delta names CONTRACT-DEV-1.schema.json; RE | CLAUDE-CODE-EXECUTABLE |
| QI-0022 | 2 | 08 | PHASE-MAPPING-GAP | `08_research/RESEARCH-1_findings_gaps_source_map.md; RESEARCH` | RESEARCH-1.2: 'Trigger/when' column (RUN-n or DEC) per RG | CLAUDE-CODE-EXECUTABLE |
| QI-0028 | 2 | 00 | GOVERNANCE-GAP | `00_MANIFEST.md §6 placeholder census` | A-008 carries a re-run placeholder census with the same six categories, the command, and the top resolving DEC | CLAUDE-CODE-EXECUTABLE |
| QI-0033 | 2 | 07 | READABILITY-DENSE | `07_deployment-and-operations/SEC-1_security_privacy_complian` | plain-language companion (≤ 25 words/sentence) or, for a register/schema document, a form finding instead of a | CLAUDE-CODE-EXECUTABLE |
| QI-0036 | 2 | 07 | READABILITY-DENSE | `07_deployment-and-operations/GOV-1_ownership_governance_post` | plain-language companion (≤ 25 words/sentence) or, for a register/schema document, a form finding instead of a | CLAUDE-CODE-EXECUTABLE |
| QI-0042 | 2 | 06 | SCHEMA-HARDCODE | `06_repositories/repo-skeletons/*/MANIFEST.yaml (19); */ci/pi` | DEC-09 (lockfile home: cdss-integration or spine) — stubs are replaced at instantiation (INDEX-06 §4) | EXECUTABLE-AFTER-DECIS |
| QI-0043 | 2 | 09 | STYLE-DRIFT | `09_diagrams/cdss_diagrams_v2.html` | `09_diagrams/tokens.css` (series palette + diagram sub-palette, one file) and `cdss_diagrams_v4.html` successo | CLAUDE-CODE-EXECUTABLE |
| QI-0044 | 2 | 09 | STYLE-DRIFT | `09_diagrams/cdss_diagrams_v3.html` | `09_diagrams/tokens.css` (series palette + diagram sub-palette, one file) and `cdss_diagrams_v4.html` successo | CLAUDE-CODE-EXECUTABLE |
| QI-0047 | 2 | CHAIN | FORM-DEVIATION | `frontmatter keys: date / date_issued / guidance_currency_dat` | `00_FRONTMATTER.schema.json` (proposed addition, v1.0 §f) naming canonical keys and accepted aliases; the CI c | CLAUDE-CODE-EXECUTABLE |
| QI-0063 | 2 | 00 | GOVERNANCE-GAP | `00_inventory.txt` | a successor `00_inventory_v1.3.txt` regenerated from `git ls-files` with a header line (`# inventory of main@< | CLAUDE-CODE-EXECUTABLE |
| QI-0031 | 2 | CHAIN | TAXONOMY-DUPLICATE | `02_cdss-stack-augmented/primer_0_ecosystem_explainer.md §9/§` | MET-2.2 D-3 erratum (row QI-0017 carries the draft) | CLAUDE-CODE-EXECUTABLE |
| QI-0015 | 1 | 01 | TABLE-OR-LADDER-DEFECT | `01_north-star-and-transformation/MET-1_metamorphosis_plan_v1` | note in MET-1.2 or the 01_ INDEX (proposed) | CLAUDE-CODE-EXECUTABLE |
| QI-0018 | 1 | 03 | TABLE-OR-LADDER-DEFECT | `03_makoha-butterfly-corpus/butterfly-primers/primer_0_butter` | — | CORPUS-OWNER |
| QI-0026 | 1 | 11 | TAXONOMY-DUPLICATE | `11_prompts/PROMPT-SURVEY-1_ecosystem_repleteness_surveyor.md` | future prompts label eval cases EV-nn; retained prompts unchanged; PROMPT-SERIES index notes the convention | CLAUDE-CODE-EXECUTABLE |
| QI-0027 | 1 | 00 | ID-LIFECYCLE-GAP | `00_MANIFEST.md` | next amendment carries 'ID census: DEF-001..007 (7); A-001..008 (8)' | CLAUDE-CODE-EXECUTABLE |
| QI-0034 | 1 | 06 | READABILITY-DENSE | `06_repositories/REPO-MAP_v2.md` | plain-language companion (≤ 25 words/sentence) or, for a register/schema document, a form finding instead of a | CLAUDE-CODE-EXECUTABLE |
| QI-0035 | 1 | 05 | READABILITY-DENSE | `05_registers-and-contracts/REG-R30.1_seed_delta.md` | plain-language companion (≤ 25 words/sentence) or, for a register/schema document, a form finding instead of a | CLAUDE-CODE-EXECUTABLE |
| QI-0037 | 1 | 05 | READABILITY-DENSE | `05_registers-and-contracts/REG-R29_hardening_coverage_ledger` | plain-language companion (≤ 25 words/sentence) or, for a register/schema document, a form finding instead of a | CLAUDE-CODE-EXECUTABLE |
| QI-0038 | 1 | 05 | READABILITY-DENSE | `05_registers-and-contracts/CONTRACT-ARG-1_argument_schema.md` | plain-language companion (≤ 25 words/sentence) or, for a register/schema document, a form finding instead of a | CLAUDE-CODE-EXECUTABLE |
| QI-0039 | 1 | 11 | READABILITY-DENSE | `11_prompts/PROMPT-SURVEY-3.2_confidence_erratum_delta.md` | plain-language companion (≤ 25 words/sentence) or, for a register/schema document, a form finding instead of a | CLAUDE-CODE-EXECUTABLE |
| QI-0040 | 1 | 05 | READABILITY-DENSE | `05_registers-and-contracts/REG-R30_regulatory_posture_regist` | plain-language companion (≤ 25 words/sentence) or, for a register/schema document, a form finding instead of a | CLAUDE-CODE-EXECUTABLE |
| QI-0041 | 1 | 04 | READABILITY-DENSE | `04_hardening/HARDEN-3.1_task_register_delta.md` | plain-language companion (≤ 25 words/sentence) or, for a register/schema document, a form finding instead of a | CLAUDE-CODE-EXECUTABLE |
| QI-0048 | 1 | 01 | FORM-DEVIATION | `01_north-star-and-transformation/MET-1.1_metamorphosis_plan_` | the next delta in the chain (MET-2.2 / R30.4) carries the full key set and a 'reads through' line for its pred | CLAUDE-CODE-EXECUTABLE |
| QI-0049 | 1 | 01 | FORM-DEVIATION | `01_north-star-and-transformation/MET-2.1_decision_register_d` | the next delta in the chain (MET-2.2 / R30.4) carries the full key set and a 'reads through' line for its pred | CLAUDE-CODE-EXECUTABLE |
| QI-0050 | 1 | 05 | FORM-DEVIATION | `05_registers-and-contracts/REG-R30.1_seed_delta.md; REG-R30.` | the next delta in the chain (MET-2.2 / R30.4) carries the full key set and a 'reads through' line for its pred | CLAUDE-CODE-EXECUTABLE |
| QI-0064 | 1 | 00 | UNCLASSIFIED-QUALITY | `00_inventory.txt` | line PASS | CLAUDE-CODE-EXECUTABLE |
| QI-0113 | 1 | 04 | UNCLASSIFIED-QUALITY | `04_hardening/HARDEN-2.1_spec_census_and_self-audit_delta.md` | line PASS | CLAUDE-CODE-EXECUTABLE |
| QI-0115 | 1 | 05 | UNCLASSIFIED-QUALITY | `05_registers-and-contracts/CONTRACT-ARG-1.examples.jsonl` | line PASS | CLAUDE-CODE-EXECUTABLE |
| QI-0118 | 1 | 05 | UNCLASSIFIED-QUALITY | `05_registers-and-contracts/REG-R29.examples.jsonl` | line PASS | CLAUDE-CODE-EXECUTABLE |
| QI-0120 | 1 | 05 | UNCLASSIFIED-QUALITY | `05_registers-and-contracts/REG-R30.3_row-form_seed.jsonl` | line PASS | CLAUDE-CODE-EXECUTABLE |
| QI-0122 | 1 | 07 | UNCLASSIFIED-QUALITY | `07_deployment-and-operations/DEPLOY-2_testing_verification_a` | line PASS | CLAUDE-CODE-EXECUTABLE |
| QI-0123 | 1 | 07 | UNCLASSIFIED-QUALITY | `07_deployment-and-operations/OPS-1_operating_procedures.md` | line PASS | CLAUDE-CODE-EXECUTABLE |
| QI-0124 | 1 | 08 | UNCLASSIFIED-QUALITY | `08_research/RESEARCH-1.1_findings_delta.md` | line PASS | CLAUDE-CODE-EXECUTABLE |
| QI-0132 | 1 | 10 | UNCLASSIFIED-QUALITY | `10_regulatory-execution/MAK-GOV_addendum-g_v0.9.md` | line PASS | CLAUDE-CODE-EXECUTABLE |
| QI-0133 | 1 | 10 | UNCLASSIFIED-QUALITY | `10_regulatory-execution/REG-NZ_v1.0.md` | line PASS | CLAUDE-CODE-EXECUTABLE |
| QI-0134 | 1 | 10 | UNCLASSIFIED-QUALITY | `10_regulatory-execution/REG-POSTURE_v1.1.md` | line PASS | CLAUDE-CODE-EXECUTABLE |
| QI-0165 | 1 | 11 | UNCLASSIFIED-QUALITY | `11_prompts/PROMPT-SURVEY-3.1_deep-review_fold_delta.md` | line PASS | CLAUDE-CODE-EXECUTABLE |
| QI-0166 | 1 | 11 | UNCLASSIFIED-QUALITY | `11_prompts/PROMPT-SURVEY-3_final-quality-improvement.md` | line PASS | CLAUDE-CODE-EXECUTABLE |

Recommended for sprint-2 despite weight 2 (marked): the four confirmed orphan citations (one line each, in deltas sprint-2 writes anyway); the 00_ census/inventory pair (one appended amendment A-008 closes both plus the DEF/A census); `09_diagrams/tokens.css` + v4 only together with the DEC-01 regeneration run.

## e. Dismissed — considered and not filed, or filed then dismissed on reading

| Row / item | Reason |
|---|---|
| QI-0008 `05_registers-and-contracts/CONTRACT-DEV-1.examples.jsonl` | the contract id CONTRACT-DEV-1 is cited by CONTRACT-ARG-1_argument_schema.md l.11 ('Deviation (CONTRACT-DEV-1, same file family)'), OPS-1.1, HARDEN-1/3 and two PRM prompts; the .examples.jsonl is the machine twin of that |
| QI-0009 `05_registers-and-contracts/CONTRACT-DEV-1.schema.json` | same as the examples file: the contract id is cited by five design documents (grep 2026-09-05); the schema is its machine twin (INDEX-05 §2/§5; HARDEN-3.1 T-002) |
| QI-0012 `10_regulatory-execution/REG-SPRINT-1.2_census_delta.md` | AGENTS.md law 3 reads 'REG-SPRINT v1.0 only through REG-SPRINT-1.1 (and 1.2 for its IDs)' — a design citation in short form the graph tool could not match; INDEX-10 §1 repeats it |
| QI-0046 `02_cdss-stack-augmented/cdss_diagrams.html` | retained original (law 1); successor page is the remedy — see the 09_ STYLE-DRIFT rows |
| FK grade > 14 on 70 files | length/density metric inflated by identifiers; ASL is primary (QUALITY_STANDARD policy; H-2) |
| 90 skeleton stubs as design-graph orphans | stub reader = instantiating primer; INDEX-06 §3 is the parent (H-4) |
| ~20 label families (D-n, E-n, T-nn eval cases, A-n, M-n, P-nn) as undeclared IDs | labels, not requirement IDs (H-5); one TAXONOMY-DUPLICATE for the T overlap |
| responsive breakpoints / 4 px grids on markdown files | architect Layer 4 bullet does not map to markdown (v1.0 law 13) |
| Observer 'three definitions' | read: one definition (Arch §13.7) restated consistently; cadence is DEC-08 — DECISION-PENDING, not taxonomy |
| REG-POSTURE's missing owner field; person-level owners across 07_/10_; regulatory/infra/repo owners | survey-2 HUMAN-ONLY rows BSQ-0110/0209/0394/0405 stand; re-filed only as DECISION-PENDING with their DEC ids (law 11) |
| NDG verification cells (MAK-GOV) | BSQ-0707 EXECUTABLE-AFTER-DECISION already carries it (law 11) |
| 13 unbannered skeleton files | DEF-004 recorded in A-004 and INDEX-06 §4 (law 11) |
| 00_inventory.txt byte drifts as append-only breaches | git show 73460b3 proves the drifts predate the seal (H-9); filed as a governance/status row instead |
| status vocabulary: corpus enum vs prose honesty sentence | two class-appropriate conventions (corpus briefing vs P-D-02); not a deviation (L4_form §3) |

## f. Proposed ecosystem additions `[ASSESSOR-PROPOSED]` — candidates, not conclusions

| Candidate | Law / layer implying it | Folder | Ratifying owner | Blocks a gate? | Row |
|---|---|---|---|---|---|
| `GLOSSARY.md` consolidating Primer 0 §9/§11 + C-02/C-07/§13.2 rulings + corpus terms by reference | Layer 3 taxonomy; MET-2 C-07 'glossary guards both terms'; Arch §14.1 | ROOT | Architecture owner | no | QI-0032 |
| `00_FRONTMATTER.schema.json` naming canonical keys and accepted aliases; `.github/audit/frontmatter_census.py` reads it | Layer 1 syntax strictness; Layer 4 document design system; architect §2 (repository-native validator — exists since A-005) | ROOT | Manifest owner | no | QI-0047 |
| `MET-4.1` gap register delta (owner · DEC · RUN/gate · exit evidence · home per G) | Layer 2 phase mapping — the one CRITICAL | 01 | Architecture owner | GATE-000 (G-02), code freeze (G-03) — the *cells*, not the delta | QI-0018 |
| `MET-2.2` decision register delta (closes-on column; C/DEC declaration; doc_id rule; glossary anchor; alias laws for RG/CC/W as the namespace register) | Layer 2 governance + Layer 3 | 01 | Architecture owner | R26/R27 opening on DEC-02 | QI-0019, 0001, 0023, 0031 |
| `REG-TASK-OWNERS` companion (task → owner role → evidence artifact, 60 tasks) | Layer 2 phase mapping on RUN-0..4 | 10 | Regulatory owner [NEEDS DEFINITION — G-09] | RUN-0 accountability | QI-0020 |
| `SEC-2.1` verification column + register-home proposal (R31?) | Layer 2 | 07 | Security owner | GATE-002/003 evidence chain | QI-0021 |
| `RESEARCH-1.2` triggers + RG alias law | Layer 2/3 | 08 | Research author; Corpus owner (MAK-CEC) | no | QI-0022/0024 |
| `09_diagrams/tokens.css` + `cdss_diagrams_v4.html` (with the DEC-01 regeneration) | Layer 4 browser-borne | 09 | Architecture owner | no | QI-0043/0044 |
| `00_inventory_v1.3.txt` + A-008 (placeholder census re-run; DEF/A census; inventory status) | Layer 2 governance | 00 | Manifest owner | no | QI-0027/0028/0063 |
| `HARDEN-1.2` / `HARDEN-3.2` ledger rows and tasks for every file since A-005 and every file this Queue would create | MT2 §3; P-F-08 (law-grade) | 04 | MT2 operator (DEC-10) | W8/W10/W11 (no rows to sweep into) | ledger debt A-005/006/007 |
| Owner register resolving every `[NEEDS DEFINITION]` (557 placeholders → 6 roles) | Layer 2 governance; G-09 | 07 (GOV-1.1) or 01 | Founder / Programme lead | every owner cell | QI-0171 (G-09/DEC-23) |
| PR-time instruction-file review (`/deep-review agent-instructions review --pr`) on AGENTS.md/CLAUDE.md/.github/**/11_prompts changes; `a11y` on 09_ successor pages | 3.1 D-9 (AGENTS.md mechanical checks extended to the governance layer) | ROOT/.github | Programme lead (DEC-09) | no | 3.1 D-9 |
| Required status check on `main` for the Copilot review / mechanical audit (merge waited for review on PR #12/#13 — it did not) | 3.2 §2 process note; AGENTS.md 'How work lands' | ROOT/.github | Repository owner | no | 3.2 §2 |

## g. Honesty lines — what this survey did not do

- Did not build anything; did not run the MT2 pass; wrote no R29 row; closed no ASSUME/DEC/gate; edited no file outside the run directory (§0 proof).
- Did not open corpus (03_) content in depth: corpus volumes and butterfly primers were measured mechanically (frontmatter, IDs, readability, style) and read only at the positions quoted; every 03_ remedy is CORPUS-OWNER.
- Did not run the mermaid parser locally (TOOL-UNAVAILABLE, QI-0059); cited CI.
- Did not fan out sub-agents (H-1); the 3.1 D-6 template is therefore untested in this run.
- Confidence scores were assigned by the same writer after each row (OPEN_QUESTIONS 8), not by an independent scorer; no row is `scorer_failed`.
- Thresholds ASL ≤ 35, implied-set 40 %, entry ≥ 60, CRITICAL-presentation ≥ 80 are `[ASSESSOR-PROPOSED]` (OPEN_QUESTIONS 10).
- 202 files created since 00_inventory.txt, and every file since A-005, have no HARDEN-1.1/3.1 row (ledger debt recorded in A-005/006/007; §f).

## h. Hand-back — the first three decisions a human must take before sprint-2

1. **DEC-22** (Founder): adopt EXEC-1 precedence and the run map — every timeline cell the MET-4.1 and REG-TASK-OWNERS drafts would fill is in force only on this.
2. **DEC-02 + DEC-09 + DEC-10/DEC-11** (Architecture owner; Programme lead; Founder): ratify R29/R30, name repo owners, name the MT2 operator — 98 + 41 + 16 ledger owner cells, every register-home cell, and the start of the pass.
3. **Architecture owner's three rulings this Queue drafts but cannot make:** the doc_id supersession rule (QI-0001, proposed DEC-24), the R25 label (BSQ-0602 / QI-0029, proposed DEC-25) and the W-namespace / RG / CC alias laws (BSQ-0711 / QI-0030 + QI-0024/0025, proposed DEC-26) — one MET-2.2 delta carries all of them once ruled. With G-09 (regulatory/infra/security owners, proposed DEC-23) as the fourth if only persons are being named this week.

## i. Exemplar register — files that PASS every applicable Q-line (from PRESENT-IMPECCABLE rows); every `exemplar_path` in §c appears here

| Class / layer | Exemplar | Q-lines it evidences |
|---|---|---|
| DELTA / L2-REPLETENESS | `01_north-star-and-transformation/MET-2.1_decision_register_delta.md` | Q-D-09 — Alias-law exemplar ('One decision, two names, one row') — cited by every alias remedy in this run. |
| ARTIFACT-HTML / L4-IMPECCABLE | `03_makoha-butterfly-corpus/artifacts-html/ (16 pages)` | Q-D-16 — The sixteen corpus pages share one token set — 28 hex colours (drift 0 on every page), three faces, one Google Fonts sty |
| WORKLIST/PLAN / L2-REPLETENESS | `04_hardening/HARDEN-3.1_task_register_delta.md` | Q-D-08 — Phase-mapping exemplar: 276 tasks each with wave, artifact_path, row, class, skills, exit evidence (0 empty), owner role |
| INDEX / L4-IMPECCABLE | `04_hardening/INDEX.md … 10_regulatory-execution/INDEX.md (7)` | Q-F-05 — Seven identical §1–§5 ladders; §4 honesty line and §5 self-audit on each; file counts equal disk (sprint-1 render_index. |
| REPO SKELETON / L1-STRUCTURE | `06_repositories/repo-skeletons/` | Q-D-02, Q-D-01 — 90 skeleton stubs have inbound edges only from INDEX-06 §3 and the HARDEN rows — exempt under Q-D-02 (the stub's reader  |
| DEPLOY / L2-REPLETENESS | `07_deployment-and-operations/DEPLOY-1.1_run-map_delta.md` | Q-D-08 — DR-1..7: owner role · person/DEC · exit evidence · failure handling → gate; the pair EXEC-1 + DEPLOY-1.1 makes RUN-0..4  |
| OPS / L2-REPLETENESS | `07_deployment-and-operations/OPS-1.1_procedures_cc5_delta.md` | Q-D-08 — PROC-01..12: trigger · steps{timeout,retry,idempotent,on_fail} · exit evidence · owner · source — 33/33 CC-5 fields. |
| REGULATORY / L2-REPLETENESS | `10_regulatory-execution/REG-NZ_v1.1.md` | Q-D-09 — Alias/rename exemplar: NZ-GATE-0/1/2 → 000/001/002 with the v1.0 file unedited and the rename stated in §12.1. |
| REGULATORY / L2-REPLETENESS | `10_regulatory-execution/REG-POSTURE_v1.2.md` | Q-D-09 — ID lifecycle exemplar: 12 families declared (frontmatter), censused (§12.1: 150), homed (R30.3 549 rows), validator rule |
| DELTA / L2-REPLETENESS | `10_regulatory-execution/REG-SPRINT-1.2_census_delta.md` | Q-D-09 — Declares and censuses an older file's families (30 ids) with owner role and exit gate per row — the model for MET-2.2/ME |

Plus 93 Phase 2 PRESENT-IMPECCABLE item rows (every mechanical line PASS; see folder rows.jsonl). Classes with **no** exemplar in the tree: GAP / DECISION REGISTER with closure evidence (the MET-2.2 draft would create one); a threat register (SEC-2.1 / R31 proposal).

## j. Needs verification

(none — no CRITICAL row has confidence < 80 and no row is `scorer_failed`)

## Assumptions (interpretive calls) — see OPEN_QUESTIONS.md items 1–9; every threshold states the alternative and the rows it would move.

## Confidence

| Verdict / score | Confidence | Reason |
|---|---|---|
| ROOT — IMPECCABLE-WITH-DECISIONS-PENDING | HIGH | every item read or measured; thresholds stated; deep reads on every CRITICAL/WARNING target |
| 00 — BELOW-STANDARD (OPTIMISATION rows only) | HIGH | every item read or measured; thresholds stated; deep reads on every CRITICAL/WARNING target |
| 01 — BELOW-STANDARD | HIGH | every item read or measured; thresholds stated; deep reads on every CRITICAL/WARNING target |
| 02 — IMPECCABLE-WITH-DECISIONS-PENDING | MEDIUM | 21 retained originals measured mechanically and read at quoted positions only; annex content not deep-read |
| 03 — BELOW-STANDARD (OPTIMISATION rows only) | MEDIUM | corpus volumes and primers not opened in depth (CORPUS-OWNER); mechanical lines only |
| 04 — BELOW-STANDARD (OPTIMISATION rows only) | HIGH | every item read or measured; thresholds stated; deep reads on every CRITICAL/WARNING target |
| 05 — BELOW-STANDARD (OPTIMISATION rows only) | MEDIUM | three Phase 1 orphan rows resolved on reading (two dismissed, one confirmed) — tool-level classification was the weak point |
| 06 — BELOW-STANDARD (OPTIMISATION rows only) | MEDIUM | 96 stubs judged by class exemption and INDEX-06; no stub read individually |
| 07 — BELOW-STANDARD (OPTIMISATION rows only) | HIGH | every item read or measured; thresholds stated; deep reads on every CRITICAL/WARNING target |
| 08 — BELOW-STANDARD (OPTIMISATION rows only) | HIGH | every item read or measured; thresholds stated; deep reads on every CRITICAL/WARNING target |
| 09 — BELOW-STANDARD (OPTIMISATION rows only) | HIGH | every item read or measured; thresholds stated; deep reads on every CRITICAL/WARNING target |
| 10 — BELOW-STANDARD | MEDIUM | REG-POSTURE v1.2 (96 KB) read in sections (frontmatter, §0.3–0.5, §7, §8, §12); REG-US/EU task tables by grep |
| 11 — BELOW-STANDARD (OPTIMISATION rows only) | MEDIUM | 31 prompts measured mechanically; only PROMPT-SURVEY-1/3 and the two indexes read |
| CHAIN — BELOW-STANDARD | HIGH | every item read or measured; thresholds stated; deep reads on every CRITICAL/WARNING target |
| L1 score | HIGH | mechanical tools over every file |
| L2 score | MEDIUM | hand lines on load-bearing documents only; 03_/06_/11_ items carry N/A on Q-D-08/09/11 rather than a read |
| L3 score | MEDIUM | hand lines on load-bearing documents only; 03_/06_/11_ items carry N/A on Q-D-08/09/11 rather than a read |
| L4 score | HIGH | mechanical tools over every file |

No IMPECCABLE verdict above carries LOW confidence.

