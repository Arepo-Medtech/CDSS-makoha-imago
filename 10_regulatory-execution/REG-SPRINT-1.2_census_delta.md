---
doc_id: REG-SPRINT-1.2
title: "REG-SPRINT-1.2 — ID census delta: declaration, census and register homes for the sprint-plan ID families"
version: "1.2-delta"
date: "2026-09-05"
status: DRAFT
authority: ADVISORY_ONLY
applies_to: "REG-SPRINT v1.0 (makoha_sprint_plan_v1_v2_v3.md) + REG-SPRINT-1.1 delta — both untouched; read v1.0 only through 1.1 (EXEC-1 EX-2) and both through this file for ID matters"
change_policy: "Additive delta per the MET-1.1 pattern. Amendment rows continue the 1.1 numbering: D-6, D-7. Statuses are quoted from R30.3 (which quotes R30.1), never changed."
id_prefixes: [V1, V2, V3, SG, SD]
req_count: 30
---

# Sprint Plan Delta v1.1 → v1.2 — ID census

REG-SPRINT v1.0 declared `id_prefixes: [V1, V2, V3, SG, SD]` and minted ~30 IDs across five
families with no count, no census and no per-ID owner or status (survey-2 BSQ-0709).
REG-SPRINT-1.1 D-5 named the register homes (SD-* → MET-2 decision table; SG-* and sprint
tasks → R30) but did not enumerate. This delta enumerates.

## D-6 — ID census

Every V*/SG-*/SD-* ID with its defining location, its R30.3 row-form seed status
(`05_registers-and-contracts/REG-R30.3_row-form_seed.jsonl`, which carries the R30.1
verbatim statuses), its owner role and its exit gate. `SG-V2-3a`/`SG-V2-3b` are minted
register-side in R30.1 (the document-side split is D-2); `V3-*` is a declared prefix with
no minted ID (V3 runs on the REG-POSTURE plan unchanged — V3.2).

| ID | Defined at (source location) | Definition shape | R30.3 status (verbatim at source) | Owner role | Exit gate / blocks |
|---|---|---|---|---|---|
| `V1-S0` | REG-SPRINT v1.0 §V1.3 Sprints (table row l.77) | table-row | OPEN (not started) | Founder (programme) — V1 track | SG-V1-0 |
| `V1-S1` | REG-SPRINT v1.0 §V1.3 Sprints (table row l.78) | table-row | OPEN (not started) | Founder (programme) — V1 track | SG-V1-1 |
| `V1-S2` | REG-SPRINT v1.0 §V1.3 Sprints (table row l.79) | table-row | OPEN (not started) | Founder (programme) — V1 track | SG-V1-2 |
| `V1-C1` | REG-SPRINT-1.1 §D-4 — Corporate track rows (from the advisor's letter, missing from v1.0) (table row l.107) | table-row | OPEN (not started) | Founder + accountant / R&D specialist (D-4) | — (corporate track; no regulatory gate) |
| `V1-C2` | REG-SPRINT-1.1 §D-4 — Corporate track rows (from the advisor's letter, missing from v1.0) (table row l.108) | table-row | OPEN (not started) | Founder + accountant / R&D specialist (D-4) | — (before the wholesale round) |
| `V2-S0` | REG-SPRINT v1.0 §V2.3 Sprints (table row l.125) | table-row | OPEN (not started) | Founder + NZ counsel / NZ sponsor (SD-03) | SG-V2-0 (= NZ-GATE-000) |
| `V2-S1` | REG-SPRINT v1.0 §V2.3 Sprints (table row l.126) | table-row | OPEN (not started) | Founder + NZ counsel / NZ sponsor (SD-03) | SG-V2-1 |
| `V2-S2` | REG-SPRINT v1.0 §V2.3 Sprints (table row l.127) | table-row | OPEN (not started) | Founder + NZ counsel / NZ sponsor (SD-03) | SG-V2-2 |
| `V2-S3` | REG-SPRINT v1.0 §V2.3 Sprints (table row l.128) | table-row | OPEN (not started) | Founder + NZ counsel / NZ sponsor (SD-03) | SG-V2-3 (split by D-2 into 3a/3b) |
| `V2-S3a` | REG-SPRINT-1.1 §D-2 — WAND notification split from first supply; new counsel question (table row l.54) | table-row | OPEN (not started) | Founder + NZ counsel / NZ sponsor (SD-03) | SG-V2-3a |
| `V2-S3b` | REG-SPRINT-1.1 §D-2 — WAND notification split from first supply; new counsel question (table row l.55) | table-row | OPEN (not started) | Founder + NZ counsel / NZ sponsor (SD-03) | SG-V2-3b |
| `V2-E1` | REG-SPRINT v1.0 §V2.4 The evidence study — design it before launch, not after (table row l.143) | table-row | OPEN (not started) | Clinical + regulatory (study design); AU counsel for V2-E5 | feeds GATE-003 evidence; NZ-GATE-001 |
| `V2-E2` | REG-SPRINT v1.0 §V2.4 The evidence study — design it before launch, not after (table row l.144) | table-row | OPEN (not started) | Clinical + regulatory (study design); AU counsel for V2-E5 | NZ ethics (HDEC) → NZ-GATE-001 |
| `V2-E3` | REG-SPRINT v1.0 §V2.4 The evidence study — design it before launch, not after (table row l.145) | table-row | OPEN (not started) | Clinical + regulatory (study design); AU counsel for V2-E5 | NZ-GATE-001 (NZ-TASK-005) |
| `V2-E4` | REG-SPRINT v1.0 §V2.4 The evidence study — design it before launch, not after (table row l.146) | table-row | OPEN (not started) | Clinical + regulatory (study design); AU counsel for V2-E5 | from first supply (SG-V2-3b) |
| `V2-E5` | REG-SPRINT v1.0 §V2.4 The evidence study — design it before launch, not after (table row l.147) | table-row | OPEN (not started) | Clinical + regulatory (study design); AU counsel for V2-E5 | NZ-ASSUME-004 / GATE-003 admissibility |
| `SG-V1-0` | REG-SPRINT v1.0 §V1.3 Sprints (exit cell l.77) | prose | OPEN (not passed) | Founder (programme); counsel attests SG-V1-0 | gate itself — counsel attests non-device (blocking) |
| `SG-V1-1` | REG-SPRINT v1.0 §V1.3 Sprints (exit cell l.78) | prose | OPEN (not passed) | Founder (programme); counsel attests SG-V1-0 | gate itself — suite green, structural absence proven |
| `SG-V1-2` | REG-SPRINT v1.0 §V1.3 Sprints (exit cell l.79) | prose | OPEN (not passed) | Founder (programme); counsel attests SG-V1-0 | gate itself — one committed site, real bundles |
| `SG-V2-0` | REG-SPRINT v1.0 §V2.3 Sprints (exit cell l.125) | prose | OPEN (not passed) | NZ sponsor / regulatory owner | gate itself — NZ-GATE-000 |
| `SG-V2-1` | REG-SPRINT v1.0 §V2.3 Sprints (exit cell l.126) | prose | OPEN (not passed) | NZ sponsor / regulatory owner | gate itself — engine passes its evaluation gate |
| `SG-V2-2` | REG-SPRINT v1.0 §V2.3 Sprints (exit cell l.127) | prose | OPEN (not passed) | NZ sponsor / regulatory owner | gate itself — file producible on demand; gates SG-V2-3a absolutely |
| `SG-V2-3` | REG-SPRINT v1.0 §V2.3 Sprints (exit cell l.128) | prose | OPEN (not passed) | NZ sponsor / regulatory owner | gate itself (v1.0) — lawful supply; split by D-2 |
| `SG-V2-3a` | REG-R30.1 seed delta (new rows list) + REG-SPRINT-1.1 D-2 | prose | OPEN (not passed) | NZ sponsor / regulatory owner | gate itself — WAND notification (Bill-clock milestone) |
| `SG-V2-3b` | REG-R30.1 seed delta (new rows list) + REG-SPRINT-1.1 D-2 | prose | OPEN (not passed) | NZ sponsor / regulatory owner | gate itself — first commercial site (revenue milestone) |
| `SD-01` | REG-SPRINT v1.0 §Decisions (table row l.199) | table-row | OPEN (→ MET-2.1 rows (SD-02 provisionally resolved, checkpoint month 4)) | Founder + advisor | blocks all V1 |
| `SD-02` | REG-SPRINT v1.0 §Decisions (table row l.200) | table-row | OPEN (→ MET-2.1 rows (SD-02 provisionally resolved, checkpoint month 4)) | Clinical + regulatory | blocks V2-S1 — provisionally resolved (D-3), checkpoint month 4 |
| `SD-03` | REG-SPRINT v1.0 §Decisions (table row l.201) | table-row | OPEN (→ MET-2.1 rows (SD-02 provisionally resolved, checkpoint month 4)) | Founder + counsel | blocks V2-S0 |
| `SD-04` | REG-SPRINT v1.0 §Decisions (table row l.202) | table-row | OPEN (→ MET-2.1 rows (SD-02 provisionally resolved, checkpoint month 4)) | Founder + counsel | blocks V2-S3 (3b) |
| `SD-05` | REG-SPRINT v1.0 §Decisions (table row l.203) | table-row | OPEN (→ MET-2.1 rows (SD-02 provisionally resolved, checkpoint month 4)) | Architecture owner | blocks V1-S1 |

## D-7 — declaration block (what v1.0's frontmatter should have carried)

| Prefix | Meaning | Count | Register home (D-5) |
|---|---|---|---|
| `V1-S` | V1 sprints | 3 | R30 (sprint tasks) |
| `V1-C` | V1 corporate track rows (D-4) | 2 | R30 (D-5: sprint tasks) — corporate, no regulatory content |
| `V2-S` | V2 sprints incl. the D-2 split | 6 | R30 |
| `V2-E` | V2 evidence-study tasks | 5 | R30 |
| `V3-*` | V3 — declared, none minted | 0 | — |
| `SG-V1` | V1 gates | 3 | R30 (gate rows; `passed` register-only) |
| `SG-V2` | V2 gates incl. 3a/3b | 6 | R30 |
| `SD` | sprint decisions (aliases of DEC-17..21 per MET-2.1) | 5 | MET-2.1 decision table |
| **Total** | | **30** | |

## Self-audit (run 2026-09-05)

1. Census equals the union of IDs grepped from v1.0 + 1.1 (`grep -o` over both files → 28 distinct) plus the two register-minted gates (`SG-V2-3a`, `SG-V2-3b`) — PASS (30 = 28 + 2).
2. Every `SD-nn` resolves to a MET-2.1 row: SD-01→DEC-17, SD-02→DEC-18, SD-03→DEC-19, SD-04→DEC-20, SD-05→DEC-21 (alias law) — PASS (5/5).
3. Every SG names its sprint (table above) — PASS (9/9).
4. Zero IDs without owner role or gate — PASS (30/30).
5. Every row's R30.3 status agrees with R30.1 verbatim wording ('not started' / 'not passed' / SD → MET-2.1) — PASS; no status changed (law 4).
6. v1.0 and 1.1 files byte-identical — PASS (CHECKSUMS_BEFORE/AFTER).

*Advisory only. Every regulatory assertion remains carried in REG-POSTURE v1.2 or REG-NZ v1.1 as an assumption requiring counsel attestation.*
