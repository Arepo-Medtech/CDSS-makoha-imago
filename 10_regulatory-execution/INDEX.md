---
doc_id: INDEX-10
title: "INDEX-10 — 10_regulatory-execution: briefing, file table with authority and packet roles, ID-family map, known gaps, honesty line, self-audit"
version: "1.0"
date: "2026-09-05"
status: "Added (sprint-1); indexes only; ADVISORY_ONLY content throughout; nothing attested in any jurisdiction; GATE-000, NZ-GATE-000, US-GATE-000, EU-GATE-000 all unpassed; counsel packets ASSEMBLED (11_prompts/runs/2026-09-05_primer-0/) but NOT SENT"
folder: "10_regulatory-execution/"
produced_by: "sprint-1 (survey-2 Build-Spec Queue) — generated tables from disk by 11_prompts/runs/2026-09-05_sprint-1/tools/render_index.py; briefing text authored; edits nothing"
---

# INDEX-10 — 10_regulatory-execution

## §1 Briefing — what these documents are

A **posture** (REG-POSTURE) states, per jurisdiction, the working regulatory position as assumptions requiring counsel attestation — findings, obligations, standards, gates, tasks, questions, watch items, sources — each with a stable ID and a closed status vocabulary; it is ADVISORY_ONLY and can never evidence a DONE. A **jurisdiction brief** (REG-NZ, REG-US, REG-EU) is a posture for another regulator, written replete-standalone (§0.9 rule: the full standards stack repeated by design). A **non-device addendum** (MAK-GOV) argues that a separate artifact is not a device and carries the build requirements (NDG) that keep it so. A **run plan + delta** (REG-SPRINT v1.0 read through 1.1, and 1.2 for its IDs) prices the three clocks (Bill, capital, ARTG) into sprints and gates. A **fold worklist** (FOLD-1) says how a new posture version is folded verbatim into the corpus wrapper MAK-ANT (AN-5: carrier map re-runs first). An **execution directive** (EXEC-1) gives the layer precedence for *sequencing only* (EX-1) and merges every phase structure into one calendar RUN-0..4 (EX-5); content authority is unchanged. Read EXEC-1 first, REG-POSTURE v1.2 through its Contents companion, and every v1.0/v1.1 file only where its successor says so.

## §2 File table

| path | class | doc_id | version | date | status (quoted) | bytes | disposition | HARDEN-1/1.1 row | HARDEN-3.1 task | 00_MANIFEST row | ID families minted (count) | authority / standing | read-through rule | counsel-packet role (EX-6) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `10_regulatory-execution/EXEC-1_execution_directive.md` | CC-8 | EXEC-1 | 1.0 | 2026-09-01 | Added (Imago v1.2). Normative for sequencing and precedence; regulatory content within the documents it sequences remains ADVISORY_ONLY per those documents' own authority lines. | 11180 | Added (A-002/A-003) — ADVISORY_ONLY | 228 | T-504 | §8 A-002 (7) + §9 A-003 (+4) + A-004 | EX (10) | normative for sequencing | — | governs the folder (EX-1); RUN table |
| `10_regulatory-execution/FOLD-1_antennae_fold_worklist.md` | CC-5 | FOLD-1 | 1.0 | 2026-09-01 | Added (Imago v1.2). Worklist only — executing it produces MAK-ANT v1.1 as a NEW file; antennae-corpus_v1.0.md is never edited. | 2799 | Added (A-002/A-003) — ADVISORY_ONLY | 229 | T-505 | §8 A-002 (7) + §9 A-003 (+4) + A-004 | W1–W5 (5; collides with HARDEN-3 W-namespace — BSQ-0711) | worklist; output is a 03_ volume | launch via PROMPT-FOLD-1 (sprint-1); W1 folds v1.2 (§12.5) | — |
| `10_regulatory-execution/INDEX.md` | CC-8 | INDEX-10 | 1.0 | 2026-09-05 | Added (sprint-1); indexes only; ADVISORY_ONLY content throughout; nothing attested in any jurisdiction; GATE-000, NZ-GATE-000, US-GATE-000, EU-GATE-000 all unpassed; counsel packets ASSEMBLED (11_prompts/runs/2026-09-05_… | 12762 | Added (sprint-1) | 230 | T-717 | §8 A-002 (7) + §9 A-003 (+4) + A-004 | — | — | — | — |
| `10_regulatory-execution/MAK-GOV_addendum-g_v0.9.md` | CC-4 | MAK-GOV | 0.9-proposed | 2026-09-01 | proposed-normative-draft | 17124 | Added (A-002/A-003) — ADVISORY_ONLY | 231 | T-506 | §8 A-002 (7) + §9 A-003 (+4) + A-004 | NDG (14); DEC-G1..G4 (aliases of DEC-13..16) | ADVISORY_ONLY (regulatory) / PROPOSED-NORMATIVE (build) | — | §2 = counsel attachment (EX-6 item 3) |
| `10_regulatory-execution/REG-EU_v1.0.md` | CC-4 | REG-EU | 1.0 | — | DRAFT | 46101 | Added (A-002/A-003) — ADVISORY_ONLY | 232 | T-507 | §8 A-002 (7) + §9 A-003 (+4) + A-004 | EU-* 10 families = 123 | ADVISORY_ONLY; later jurisdiction | — | — |
| `10_regulatory-execution/REG-NZ_v1.0.md` | CC-4 | REG-NZ | 1.0 | — | DRAFT | 13194 | Added (A-002) — superseded by A-003, retained unedited | 233 | T-508 | §8 A-002 (7) + §9 A-003 (+4) + A-004 | 45 IDs (v1.0) | ADVISORY_ONLY; superseded by v1.1 (A-003), retained unedited | cite v1.1 | — |
| `10_regulatory-execution/REG-NZ_v1.1.md` | CC-4 | REG-NZ | 1.1 | — | DRAFT | 47377 | Added (A-002/A-003) — ADVISORY_ONLY | 234 | T-509 | §8 A-002 (7) + §9 A-003 (+4) + A-004 | NZ-FIND 12 · NZ-OBL 13 · NZ-STD 26 · NZ-ASSUME 5 · NZ-TASK 10 · NZ-GATE 3 · NZ-WATCH 5 · NZ-Q 6 · NZ-SRC 13 = 93 | ADVISORY_ONLY; supersedes v1.0 | — | §6/§9/§10 = NZ counsel packet |
| `10_regulatory-execution/REG-POSTURE_v1.1.md` | CC-4 | REG-POSTURE | 1.1 | — | DRAFT | 60793 | Added (A-002) — superseded by A-003, retained unedited | 235 | T-154 | §8 A-002 (7) + §9 A-003 (+4) + A-004 | 120 IDs (v1.1 census) | ADVISORY_ONLY; superseded by v1.2 (A-003), retained unedited | cite v1.2; v1.1 for history only | — |
| `10_regulatory-execution/REG-POSTURE_v1.2.md` | CC-4 | REG-POSTURE | 1.2 | — | DRAFT | 96260 | Added (A-002/A-003) — ADVISORY_ONLY | 236 | T-153 | §8 A-002 (7) + §9 A-003 (+4) + A-004 | REG-FIND 13 · REG-KEEP 4 · ASSUME-REG 9 · OBL 15 · STD 26 · FORK-REG 1 · GATE 5 · TASK-REG 24 · KTX 14 · WATCH-REG 8 · Q-REG 11 · SRC-REG 20 = 150 | ADVISORY_ONLY; CANONICAL (EX-3 as amended by A-003) | read with REG-POSTURE_v1.2_CONTENTS.md (map) | §1–§3 = counsel attachment (EX-6 items 1–2) |
| `10_regulatory-execution/REG-POSTURE_v1.2_CONTENTS.md` | CC-4 | REG-POSTURE-TOC | 1.0 | 2026-09-05 | Navigational companion; adds no content; REG-POSTURE v1.2 is never edited (a v1.3 may absorb this map under its own §A). Survey-2 BSQ-0705 named a v1.1 companion; v1.2 superseded v1.1 under A-003 before this sprint, so t… | 9915 | Added (sprint-1) — Proposed | 237 | T-155 | §8 A-002 (7) + §9 A-003 (+4) + A-004 | — (map of the 12 families) | ADVISORY_ONLY companion | — | names the attachment set |
| `10_regulatory-execution/REG-SPRINT-1.1_delta.md` | CC-4 | REG-SPRINT-1.1 | 1.1-delta | — | DRAFT | 6141 | Added (A-002/A-003) — ADVISORY_ONLY | 238 | T-510 | §8 A-002 (7) + §9 A-003 (+4) + A-004 | D-1..D-5 | ADVISORY_ONLY | — | D-2 originates NZ-Q-004 |
| `10_regulatory-execution/REG-SPRINT-1.2_census_delta.md` | CC-4 | REG-SPRINT-1.2 | 1.2-delta | 2026-09-05 | DRAFT | 8986 | Added (sprint-1) — Proposed | 239 | T-511 | §8 A-002 (7) + §9 A-003 (+4) + A-004 | D-6, D-7; census 30 ids | ADVISORY_ONLY (sprint-1) | — | — |
| `10_regulatory-execution/REG-SPRINT_v1.0.md` | CC-4 | REG-SPRINT | 1.0 | — | DRAFT | 10741 | Added (A-002/A-003) — ADVISORY_ONLY | 240 | T-512 | §8 A-002 (7) + §9 A-003 (+4) + A-004 | V1/V2/V3, SG, SD (declared; censused in 1.2) | ADVISORY_ONLY | read ONLY through REG-SPRINT-1.1 (EX-2) and 1.2 for IDs | — |
| `10_regulatory-execution/REG-US_v1.0.md` | CC-4 | REG-US | 1.0 | — | DRAFT | 47772 | Added (A-002/A-003) — ADVISORY_ONLY | 241 | T-513 | §8 A-002 (7) + §9 A-003 (+4) + A-004 | US-* 10 families = 129 | ADVISORY_ONLY; later jurisdiction | — | — |
| `10_regulatory-execution/validate_reg.py` | CC-5 | — | — | — | #!/usr/bin/env python3 | 3904 | Added (A-002/A-003) — ADVISORY_ONLY | 242 | T-514 | §8 A-002 (7) + §9 A-003 (+4) + A-004 | — (tool) | tooling (A-003 seal check) | run from this directory | — |

## §3 ID-family map and register mirror

| File | Families minted | Register home |
|---|---|---|
| REG-POSTURE v1.2 | 12 families, 150 IDs (§12.1) | R30 base + R30.1 + R30.2 seeds → R30.3 row form (150 AU rows) |
| REG-NZ v1.1 | 9 families, 93 IDs (§12.1) | R30.1 (NZ-* v1.0 rows) + R30.2 (NZ-STD, NZ-GATE, v1.1 additions) → R30.3 (93 rows) |
| REG-US v1.0 | 10 families, 129 IDs | R30.2 → R30.3 (129 rows) |
| REG-EU v1.0 | 10 families, 123 IDs | R30.2 → R30.3 (123 rows) |
| MAK-GOV | NDG-1..14; DEC-G1..G4 | R30.1 (NDG rows) → R30.3 (14); MET-2.1 DEC-13..16 |
| REG-SPRINT (+1.1, 1.2) | V1/V2 (16), SG (9), SD (5) | R30.1 → R30.3 (30 rows); SD → MET-2.1 DEC-17..21 |
| EXEC-1 | EX-1..10 | R30.1 → R30.3 (10 rows) |
| FOLD-1 | W1–W5 | — (worklist; C-13 closure in MET-2.1) |

R30.3 total: 549 rows = 150 + 93 + 129 + 123 + 14 + 30 + 10 (validated against `05_/REG-R30.schema.json`, 0 invalid; every family contiguous at both ends).

## §4 Known gaps carried

- REG-FIND-013 / TASK-REG-023 forward references: **closed by REG-POSTURE v1.2** (A-003; §12.2 check 13) — survey-2 BSQ-0001 CLOSED.
- NZ-Q-004 and NZ-ASSUME-005 homed in REG-NZ v1.1 (§12.2 check 11) — BSQ-0706 CLOSED by A-003, no build needed.
- MAK-GOV §5 integration ledger: of 10 declared integrations, 3 now exist (MET-2.1 rows; R30.1/R30.3 seed; REG-POSTURE v1.2 row); 7 remain (03_ annexes — corpus owner, AN-5; MET-4 gap row; REPO-MAP reclassification; DEPLOY-2 NDG criteria; MAK-J3 retirement notice blocked on DEC-06) — BSQ-0707 EXECUTABLE-AFTER-DECISION (DEC-13/DEC-14).
- FOLD-1 W1–W5 collide with HARDEN-3 W0–W11 namespace (BSQ-0711) — architecture owner; PROMPT-FOLD-1 cites them as "FOLD-1 W1" meanwhile.
- MAK-GOV has no Contents section (17 KB, 6 parts) and no census/self-audit (BSQ-0707 scope).
- 00_MANIFEST §8 "Counsel packets drafted, not sent": packets are now **assembled** in `11_prompts/runs/2026-09-05_primer-0/` and not sent (DEF-005 wording in A-004).
- Superseded files (REG-POSTURE v1.1, REG-NZ v1.0) are retained unedited and must not be cited for current positions (EX-3 as amended).

## §5 Honesty line and self-audit

No attestation exists in any jurisdiction; every ASSUME is OPEN; standards editions and FDA/EU recognition statuses are from the author's knowledge pending WATCH-REG-008 / US-WATCH-004 / EU-WATCH-004; the January 2026 FDA CDS revision has not been read in the primary (US-WATCH-001); the regulatory owner is `[NEEDS DEFINITION]` (G-09).

- Files in table = on disk = 15 — PASS. `validate_reg.py` re-run 2026-09-05:

```
== AU REG-POSTURE_v1.2.md: 150 distinct IDs referenced, 138 defined
  DUP definitions: ['ASSUME-REG-004']
  REFERENCED BUT UNDEFINED: ['FORK-REG-001', 'GATE-000', 'GATE-001', 'GATE-002', 'GATE-003', 'GATE-004', 'KTX-001', 'KTX-008', 'KTX-009', 'KTX-010', 'KTX-011', 'KTX-012']
  ASSUME-REG: 9 defined, 001-009
  KTX: 8 defined, 001-014  GAP [1, 8, 9, 10, 11, 12]
  OBL: 15 defined, 001-015
  Q-REG: 11 defined, 001-011
  REG-FIND: 13 defined, 001-013
  REG-KEEP: 4 defined, 001-004
  SRC-REG: 20 defined, 001-020
  STD: 26 defined, 001-026
  TASK-REG: 24 defined, 001-024
  WATCH-REG: 8 defined, 001-008
== NZ REG-NZ_v1.1.md: 93 distinct IDs referenced, 93 defined
  NZ-ASSUME: 5 defined, 001-005
  NZ-FIND: 12 defined, 001-012
  NZ-GATE: 3 defined, 000-002
  NZ-OBL: 13 defined, 001-013
  NZ-Q: 6 defined, 001-006
  NZ-SRC: 13 defined, 001-013
  NZ-STD: 26 defined, 001-026
  NZ-TASK: 10 defined, 001-010
  NZ-WATCH: 5 defined, 001-005
== US REG-US_v1.0.md: 129 distinct IDs referenced, 129 defined
  US-ASSUME: 6 defined, 001-006
  US-FIND: 16 defined, 001-016
  US-GATE: 4 defined, 000-003
  US-OBL: 14 defined, 001-014
  US-Q: 6 defined, 001-006
  US-REG: 17 defined, 001-017
  US-SRC: 19 defined, 001-019
  US-STD: 27 defined, 001-027
  US-TASK: 13 defined, 001-013
  US-WATCH: 7 defined, 001-007
== EU REG-EU_v1.0.md: 123 distinct IDs referenced, 123 defined
  EU-ASSUME: 6 defined, 001-006
  EU-FIND: 16 defined, 001-016
  EU-GATE: 4 defined, 000-003
  EU-LAW: 14 defined, 001-014
  EU-OBL: 16 defined, 001-016
  EU-Q: 6 defined, 001-006
  EU-SRC: 14 defined, 001-014
  EU-STD: 27 defined, 001-027
  EU-TASK: 13 defined, 001-013
  EU-WATCH: 7 defined, 001-007

RESULT: FAIL (3 issues)
```
  The `RESULT: FAIL` is the **known AU legacy-shape condition**, not a new defect: REG-POSTURE v1.2 §12.2 check 2 and 00_MANIFEST §9 A-003 "Verification at seal" record the twelve v1.1-era ids defined in prose/field-table shape (GATE-000..004, FORK-REG-001, KTX-001, KTX-008..012) and the one legacy double definition (ASSUME-REG-004), carried unchanged under append-only law; NZ 93/93, US 129/129, EU 123/123 pass; the shared stack 001..026 is aligned in all four. The R30.3 row-form seed defines all 150 AU ids (legacy ones flagged `definition_shape: prose`).
- Every family endpoint resolves both ends (R30.3 seed validation: 44 families, 0 gaps) — PASS. Every §4 gap cites a BSQ row — PASS.
