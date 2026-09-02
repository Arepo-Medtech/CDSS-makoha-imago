## c. The Build-Spec Queue (weight ≥ 3; grouped by executability; within group: weight desc → earliest blocked gate → dependencies first)

42 rows. Every CLAUDE-CODE-EXECUTABLE-NOW row carries an eleven-field `build_spec` in `BSQ.jsonl` (validated); the table shows the spec's target path and its closes/depends links; the full spec text is in the row.


### CLAUDE-CODE-EXECUTABLE-NOW (27)

| # | Row | W (c+r) | Folder | Class | Statement (short) | Blocks | Target / decision | Closes | Depends on | Owner |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | BSQ-0006 | 4 (2+2) | 04 | QUALITY-BELOW-BAR | HARDEN-3 mints T-000..T-132 only as ranges inside wave cells (e.g. 'T-100..107: 05_/06_/07_/08_ documents'); no per-task row exists naming artifact path, class, skills, e… | W0–W11 (no task is individually startable/closable); MET-4 P0 'start the pass'; GATE-000 indirectly (MT2 row zero per EX | 04_hardening/HARDEN-3.1_task_register_delta.md (companion delta; HARDEN-3 v1.0 untouched) | BSQ-0006 | — | MT2 operator (DEC-10) [NEEDS DEFINITION] |
| 2 | BSQ-0202 | 4 (2+2) | 05 | ABSENT-ITEM | R30 exists only as a prose field list and a prose seed ('REG-FIND-001..008 OPEN'); there is no JSON Schema and no row-form seed, so CC-4's named mechanical check cannot r… | W1 T-005; W3 T-021 (R30 reconciliation); RUN-0 exit (EX-10 — GATE-000 row must land in R30) | 05_registers-and-contracts/REG-R30.schema.json + 05_registers-and-contracts/REG-R30.2_row-form_seed.jsonl (companions; the .md base and R30.1 untouched) | BSQ-0202 | — | cdss-governance (owner) / Architecture owner (DEC-02) |
| 3 | BSQ-0402 | 4 (2+2) | 07 | ABSENT-SECTION | DEPLOY-1 (2026-09-01) predates the 10_ layer; no file maps its steps 0a–5 to RUN-0..4, carries the RUN-0 additions (TASK-REG-021/022, V1-*, NZ-TASK-*, MAK-GOV G0), or nam… | RUN-0 (EX-8 week-one board) — two calendars in force; GATE-000/GATE-001 step ordering | 07_deployment-and-operations/DEPLOY-1.1_run-map_delta.md | BSQ-0402 | — | Founder (programme) — DEC-22 adopts EXEC-1 precedence |
| 4 | BSQ-0702 | 4 (2+2) | 10 | ABSENT-ITEM | No counsel packet artifact exists in the tree — EX-6 specifies the five AU questions and the NZ packet, PROMPT-P0 Phase 2 specifies the assembly (`counsel_packet_AU/`, `c… | GATE-000; SG-V1-0; NZ-GATE-0; RUN-0 exit | run 11_prompts/PROMPT-P0_primer0_launch.md Phase 2 as written → 11_prompts/runs/{{RUN_DATE}}_primer-0/counsel_packet_AU/, counsel_packet_NZ/, DRAFT_TASK-REG-001 | BSQ-0702 | — | Founder (programme) dispatches; executor assembles (PROMPT-P |
| 5 | BSQ-0106 | 4 (2+2) | 04 | ABSENT-WORKLIST-TASK | No HARDEN-3 task covers 10_ (7 files), 11_ (28), 03_/butterfly-primers (12) + 03_ briefing/prompt (2), 05_/REG-R30.1, 01_/MET-2.1; EXEC-1 EX-5 adds 10_ only to the W11 *s… | W8/W10/W11; GATE-000 indirectly: REG-POSTURE v1.1 (counsel attachment, EX-6) is unhardened with no task | 04_hardening/HARDEN-3.1_task_register_delta.md (same file as BSQ-0006 build_spec — one deliverable closes both) | BSQ-0106, BSQ-0006, BSQ-0704 | BSQ-0104 | MT2 operator (DEC-10) [NEEDS DEFINITION] |
| 6 | BSQ-0703 | 4 (2+2) | 10 | ABSENT-LEDGER-ROW | None of the seven 10_ files has a HARDEN-1 row; REG-POSTURE v1.1 — the canonical posture (EX-3) and a counsel attachment — is covered only indirectly by row 8 (v1.0 annex… | W3/W11; GATE-000 (unhardened counsel attachment) | 04_hardening/HARDEN-1.1_coverage_ledger_seed_delta.md D-2 (seven rows) — same deliverable as BSQ-0104 | BSQ-0703 | BSQ-0104 | cdss-spine / MT2 operator (DEC-10) [NEEDS DEFINITION] |
| 7 | BSQ-0704 | 4 (2+2) | 10 | ABSENT-WORKLIST-TASK | No HARDEN-3 task covers any 10_ file; EX-5 adds 10_ only to the W11 sweep, and T-020 (W3) names MAK-ANT/REG-POSTURE v1.0. Closed by HARDEN-3.1 (BSQ-0006/0106) with a W3 e… | W3; W11; GATE-000 | 04_hardening/HARDEN-3.1_task_register_delta.md (tasks added there — BSQ-0006/BSQ-0106) | BSQ-0704 | BSQ-0006 | MT2 operator (DEC-10) [NEEDS DEFINITION] |
| 8 | BSQ-0403 | 4 (2+2) | 07 | QUALITY-BELOW-BAR | OPS-1's four sections are prose; not one procedure is written as ordered steps with trigger, timeout/retry/idempotency, exit evidence, on-fail and owner — the CC-5 bar HA… | W8 (CC-5 bar unmeasurable); GATE-001 (Jira/Ketryx configuration procedure) and GATE-002 (TASK-REG-010 gated pipeline pro | 07_deployment-and-operations/OPS-1.1_procedures_cc5_delta.md | BSQ-0403 | — | Operations / regulatory owner [NEEDS DEFINITION — G-09] |
| 9 | BSQ-0205 | 4 (2+2) | 05 | ABSENT-ITEM | CONTRACT-ARG-1 is a prose field list; no JSON Schema exists for GenericArgument, ActualArgument or Deviation, and the render-invariance contract has no test specification… | W1 T-001..003; PROMPT-A (argument payload), PROMPT-F (qualifier), PROMPT-E (rebuttals) — L1 exits per DEPLOY-2 §1–2 fabr | 05_registers-and-contracts/CONTRACT-ARG-1.schema.json, CONTRACT-DEV-1.schema.json, CONTRACT-RRI-1_render-invariance_test-spec.md (companions; CONTRACT-ARG-1 .md | BSQ-0205 | — | Architecture owner (DEC-02) / cdss-spine |
| 10 | BSQ-0404 | 4 (2+2) | 07 | ABSENT-ITEM | SEC-1 ('no new claims') omits encryption, SBOM and CAPA (present only in DEPLOY-1 / Arch §11.4) and there is no threat model or data-flow diagram anywhere in the tree; th… | GATE-002 (identifiable-data line — controls need a threat model); TASK-REG-016 pen-test scoping (GATE-003 evidence) | 07_deployment-and-operations/SEC-2_threat-model_and_data-flow.md + 09_diagrams/data_flow_v1.mermaid | BSQ-0404 | — | Security owner [NEEDS DEFINITION — G-09] |
| 11 | BSQ-0101 | 3 (2+1) | 04 | ABSENT-CHAIN-LINK | 04_hardening has no index or briefing of its own; the four files' composition (directive → spec → plan → ledger seed → R29) is explained only in 01_/MET-1.1 and 00_MANIFE… | W10 T-121 (self-referential class needs per-file enumeration); PROMPT-HARDEN run orientation | 04_hardening/INDEX.md | BSQ-0101 | — | Manifest owner [NEEDS DEFINITION] |
| 12 | BSQ-0104 | 3 (2+1) | 04 | ABSENT-LEDGER-ROW | HARDEN-1 has no row for 10_ (7 files), 05_/REG-R30.1, 01_/MET-2.1, 11_ (28), 03_/butterfly-primers (12), 03_ briefing + programme prompt, 02_/primers_briefing, root loose… | W8 (05_/06_/07_/08_ rows); W10 T-121; W11 sweep incl. 10_ (EX-5) — no rows to sweep into | 04_hardening/HARDEN-1.1_coverage_ledger_seed_delta.md | BSQ-0104, BSQ-0703, BSQ-0203 | — | cdss-spine (register owner per REG-R29) / MT2 operator (DEC- |
| 13 | BSQ-0105 | 3 (2+1) | 04 | ABSENT-SECTION | HARDEN-2 mints CC-1..CC-8 and eight anti-rationalization rows without a count declaration, ID census or self-audit; 4 of 8 class-bar rows carry no source for their bar; C… | W10 T-121 (CC-8 self-clearance) | 04_hardening/HARDEN-2.1_spec_census_and_self-audit_delta.md | BSQ-0105 | — | MT2 operator (DEC-10) [NEEDS DEFINITION] |
| 14 | BSQ-0201 | 3 (2+1) | 05 | ABSENT-CHAIN-LINK | 05_ has no index or briefing; the folder mixes a contract (carrying three contract IDs in one file), a JSON schema, its md twin, a prose register and a delta, and nothing… | W1 T-001..005 orientation; W8 T-100..107 enumeration | 05_registers-and-contracts/INDEX.md | BSQ-0201 | — | Manifest owner [NEEDS DEFINITION] |
| 15 | BSQ-0206 | 3 (2+1) | 05 | QUALITY-BELOW-BAR | REG-R29.schema.json is valid (check_schema OK) but ships no example instance, and its md twin omits the `blocker` field; HARDEN-1's PENDING placeholder does not validate … | W1 T-004; PROMPT-HARDEN output contract | 05_registers-and-contracts/REG-R29.examples.jsonl + REG-R29.1_schema_twin_delta.md (companions; .json and .md untouched) | BSQ-0206 | — | cdss-spine |
| 16 | BSQ-0701 | 3 (2+1) | 10 | ABSENT-CHAIN-LINK | 10_ has no index; EXEC-1 Part 4 lists 6/7 files with Type only; nothing in the folder states the read-through rules together (REG-SPRINT via 1.1; REG-POSTURE canonical ov… | W11 sweep of 10_ (EX-5) — nothing enumerates the layer; RUN-0 packet assembly orientation | 10_regulatory-execution/INDEX.md | BSQ-0701 | — | Manifest owner [NEEDS DEFINITION] |
| 17 | BSQ-0705 | 3 (2+1) | 10 | ABSENT-SECTION | REG-POSTURE v1.1 — the largest target file and a counsel attachment — has no Contents section and no owner field (its own §12.3 records the owner gap as G-09); counsel re… | RUN-0 packet usability (EX-6 attachments); FOLD-1 W1 (the v1.1 text is folded verbatim — a Contents block should exist b | 10_regulatory-execution/REG-POSTURE_v1.1_CONTENTS.md (companion: a navigational map — the v1.1 text is never edited; a v1.2 can absorb it under §A) | BSQ-0705 | — | Regulatory owner [NEEDS DEFINITION — G-09 / REG-POSTURE §12. |
| 18 | BSQ-0113 | 3 (2+1) | 04 | STALE-COUNT | Row band 60–71 allocates 12 row ids to 21 named artifacts (01_ MET set 5, 04_ 4, 06_ REPO-MAP+4 READMEs 5, 07_ 5, 08_ 1, 00_MANIFEST 1) — the seed's own arithmetic does n… | W8; W10 | 04_hardening/HARDEN-1.1_coverage_ledger_seed_delta.md (D-1 of BSQ-0104 — same deliverable) | BSQ-0113 | BSQ-0104 | cdss-spine |
| 19 | BSQ-0203 | 3 (2+1) | 05 | ABSENT-LEDGER-ROW | REG-R30.1 (added in A-002) has no HARDEN-1 row; row 5 names 'REG-R30 schema+seed' only. | W1/W3; W11 | 04_hardening/HARDEN-1.1_coverage_ledger_seed_delta.md (row added there — see BSQ-0104) | BSQ-0203 | BSQ-0104 | cdss-spine |
| 20 | BSQ-0708 | 3 (2+1) | 10 | ABSENT-CHAIN-LINK | FOLD-1 is an executable worklist with no launch prompt and no failure handling per step; its output (`antennae-corpus_v1.1.md`) is a corpus volume — the fold can be execu… | C-13 closure (MET-2.1); W2/W3 of HARDEN-3 (host law + posture tasks read the folded annex) | 11_prompts/PROMPT-FOLD-1_antennae_v1.1_fold.md | BSQ-0708 | — | Regulatory owner [NEEDS DEFINITION — G-09 / REG-POSTURE §12. |
| 21 | BSQ-0204 | 3 (2+1) | 05 | ABSENT-WORKLIST-TASK | No HARDEN-3 task covers REG-R30.1; T-021 'R30 reconciliation' predates the delta and does not name it. Closed by HARDEN-3.1 (BSQ-0006/BSQ-0106). | W3 | 04_hardening/HARDEN-3.1_task_register_delta.md (task added there — see BSQ-0006) | BSQ-0204 | BSQ-0006 | MT2 operator (DEC-10) [NEEDS DEFINITION] |
| 22 | BSQ-0390 | 3 (2+1) | 06 | ABSENT-CHAIN-LINK | REPO-MAP indexes 19 repos but no document indexes the 90 skeleton files; the skeleton index paragraph over-claims (all 14 existing repos with CI stubs and per-directory s… | W8 T-100..107 (per-file enumeration is the wave's precondition); PROMPT-A..L runs (each writes inside a tree whose stub  | 06_repositories/INDEX.md | BSQ-0390 | — | Manifest owner [NEEDS DEFINITION] |
| 23 | BSQ-0401 | 3 (2+1) | 07 | ABSENT-CHAIN-LINK | 07_ has no index/briefing; five plan-grade files of five classes, none dated, none stating that EXEC-1's run map now governs their sequence. | W8 T-100..107 enumeration; RUN-0 week-one board orientation (EX-8) | 07_deployment-and-operations/INDEX.md | BSQ-0401 | — | Manifest owner [NEEDS DEFINITION] |
| 24 | BSQ-0501 | 3 (2+1) | 08 | ABSENT-CHAIN-LINK | 08_ has no index; RESEARCH-1 carries no `status` field and no statement of what a research map is or how RG-* gaps close (into MET-4 G-*, R30, or DEC rows). | W8 T-100..107 enumeration | 08_research/INDEX.md | BSQ-0501 | — | Manifest owner [NEEDS DEFINITION] |
| 25 | BSQ-0601 | 3 (2+1) | 09 | ABSENT-CHAIN-LINK | 09_ has no index; the parse evidence lives only in 00_MANIFEST §5 DEF-001 and in this run; no file states each diagram's source doc, version/date, HARDEN row, or the rege… | W6 T-072 (CC-6 evidence should be in-folder); G-10 regeneration (procedure + gate) | 09_diagrams/INDEX.md | BSQ-0601 | — | Manifest owner [NEEDS DEFINITION] |
| 26 | BSQ-0706 | 3 (2+1) | 10 | ABSENT-SECTION | REG-NZ declares 7 ID families but no counts, has no census or self-audit, does not name the blocked gate per OPEN row, and lacks NZ-Q-004 — the transition-provisions ques… | NZ packet assembly (EX-6) — source-of-truth mismatch; FOLD-1 W2 carrier map (NZ-* families) | 10_regulatory-execution/REG-NZ-1.1_delta.md | BSQ-0706 | — | Regulatory owner [NEEDS DEFINITION — G-09 / REG-POSTURE §12. |
| 27 | BSQ-0709 | 3 (2+1) | 10 | ABSENT-SECTION | REG-SPRINT v1.0 + 1.1 mint ~25 IDs across five families (V1-S0..S2, V1-C1..C2, V2-S0..S3b, V2-E1..E5, SG-V1-0..2, SG-V2-0..3b, SD-01..05) with no declaration, census or p… | RUN-0..4 exits (EX-10 register rows need stable ids); R30 reconciliation T-021 | 10_regulatory-execution/REG-SPRINT-1.2_census_delta.md (delta over v1.0+1.1; both untouched) | BSQ-0709 | — | Founder (programme) |

### EXECUTABLE-AFTER-DECISION (5)

| # | Row | W (c+r) | Folder | Class | Statement (short) | Blocks | Target / decision | Closes | Depends on | Owner |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | BSQ-0707 | 4 (2+2) | 10 | STALE-COUNT | MAK-GOV §5 declares ten integrations; two exist (MET-2.1 DEC-13..16/C-15; R30.1 NDG rows), eight do not (abdomen/four-faces/antennae annexes; REG-POSTURE v1.2; MET-4 gap … | SG-V1-0 / DEC-14 (first revenue) — integration debt is the build's precondition; GATE-000 item 3 (counsel packet attache | DEC-13 (namespace/doc_id — the delta's own doc_id depends on it) and DEC-14 (ship the non-device layer); the status table and census can be drafted now; the eig | — | — | Architecture owner (DEC-13) / Founder (programme) (DEC-14) |
| 2 | BSQ-0391 | 4 (2+2) | 06 | ABSENT-CHAIN-LINK | cdss-compiler (Proposed repo, 9 skeleton files, CODEOWNERS mandated) is the only tree with no owning primer in 02_ or 03_/butterfly-primers and no launch prompt in 11_; R… | L2/L3 (Arch §14.5: GenericArgument bundles via registry gateway); DEPLOY-1 compiler adoption spike (MET-4 P2); DEC-09 (n | DEC-09 (repo + prefix CMP) and DEC-13 (namespace family); the primer can be drafted now under the butterfly-primer-programme prompt with MAK-CEC CP-* + MAK-FFC  | — | — | Architecture owner / Programme lead [NEEDS DEFINITION — DEC- |
| 3 | BSQ-0103 | 3 (2+1) | 04 | ABSENT-CHAIN-LINK | The MT2 pass (W0–W11) has no launch prompt and no operator runbook: HARDEN-2 says what the bar is, HARDEN-3 in what order, HARDEN-1 what rows exist — nothing says how a C… | W0 (pass start) — MET-4 P0 'row zero → start the pass'; G-03 (MET-4, High) | 11_prompts/PROMPT-HARDEN_mt2_pass_launch.md | BSQ-0103 | BSQ-0006, BSQ-0104 | MT2 operator (DEC-10) [NEEDS DEFINITION] |
| 4 | BSQ-0001 | 3 (2+1) | 10 | DANGLING-REF | MAK-GOV cites REG-FIND-013 and TASK-REG-023 as IDs of a REG-POSTURE v1.2 that does not exist in the tree; neither ID is defined anywhere (R30.1 defines ASSUME-REG-009 and… | W11 sweep (EX-5); RUN-0 counsel packet item 3 (EX-6) cites MAK-GOV §2 | DEC-13 (MAK-GOV namespace) / regulatory owner [NEEDS DEFINITION] (G-09) — the IDs land either in REG-POSTURE v1.2 or in R30.1 as minted rows | — | — | Regulatory owner [NEEDS DEFINITION — G-09] |
| 5 | BSQ-0208 | 3 (2+1) | 05 | QUALITY-BELOW-BAR | The R30 seed and R30.1 record statuses verbatim from source ('standing', 'not passed', 'not started', 'open', cadence words, 'proposed-normative', 'in force', 'recorded')… | W3 T-021 (R30 reconciliation) | Regulatory owner ruling on the enum mapping for OBL-* 'standing' and WATCH cadences (no DEC exists — [NEEDS DEFINITION]; ratifies with DEC-02) | — | — | Regulatory owner [NEEDS DEFINITION — G-09] |

### HUMAN-ONLY (10)

| # | Row | W (c+r) | Folder | Class | Statement (short) | Blocks | Target / decision | Closes | Depends on | Owner |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | BSQ-0407 | 5 (2+3) | 07 | DECISION-PENDING | Step 0b cannot close without DEC-07 (TASK-REG-004) and step 1 cannot execute TASK-REG-009 without DEC-03; GOV-1's Observer cadence is DEC-08. All three Open. | GATE-000; GATE-001; first lawful supply | DEC-07 (Counsel + product), DEC-03 (Infra + regulatory), DEC-08 (Architecture owner) | — | — | Counsel + product; Infra + regulatory; Architecture owner |
| 2 | BSQ-0713 | 5 (2+3) | 10 | DECISION-PENDING | The V1 Governance Layer track — MAK-GOV's build, its repo home, its namespace and its use case — is gated by five open decisions; MET-2.1 names DEC-17 as blocking all V1 … | SG-V1-0..2; V1-S1 build placement; first revenue (REG-SPRINT V1) | DEC-13, DEC-14, DEC-16, DEC-17, DEC-19, DEC-20 | — | — | Founder (programme) + advisor; Architecture owner; NZ counse |
| 3 | BSQ-0110 | 5 (2+3) | 04 | DECISION-PENDING | No 04_ artifact can be executed until a human names the MT2 operator and accepts the row-zero rule; every 04_ build item's ratifying owner is therefore [NEEDS DEFINITION]… | W0 → all waves; code freeze (MT2 §7 completion precedes /ship) | DEC-10, DEC-11 | — | — | Programme lead / Founder [NEEDS DEFINITION — DEC-09 names th |
| 4 | BSQ-0111 | 5 (2+3) | 04 | DECISION-PENDING | HARDEN-1 becomes R29's opening content only on DEC-02; until then the seed (and any HARDEN-1.1 delta) is a proposal and no R29 row may be written. | W0 (R29 must exist to hold row zero); code freeze | DEC-02 | — | — | Architecture owner |
| 5 | BSQ-0209 | 5 (2+3) | 05 | DECISION-PENDING | Every 05_ artifact's home ('MOVE to cdss-spine, never copy') and owner depend on DEC-02 and DEC-09; until then all 05_ build items are staged drafts. | W1; L1 register check (Arch §12.3: rows 1–9 open at L1; R30 opens L1); code freeze | DEC-02, DEC-09 | — | — | Architecture owner; Programme lead [NEEDS DEFINITION] |
| 6 | BSQ-0394 | 5 (2+3) | 06 | DECISION-PENDING | REPO-MAP v2 (2026-09-01) predates the butterfly primer programme's R6 ruling cluster (2026-09-02), which proposes five new repos (cdss-fuzzy, cdss-meta, cdss-ui-auditor, … | repo creation (DEC-09 'Blocking: repo creation'); PROMPT-PRM-* build placement; code freeze (no code home for LWC/RWC/LE | DEC-09 (+DEC-13/DEC-16/DEC-21 alias family for governance) | — | — | Programme lead [NEEDS DEFINITION — DEC-09] |
| 7 | BSQ-0712 | 5 (2+3) | 10 | DECISION-PENDING | EXEC-1's precedence over MET-4/DEPLOY-1/volume phasing is proposed, not adopted; every sequencing recommendation in this survey (DEPLOY-1.1, IMAGO-4 v2, the queue's gate … | RUN-0 start; every downstream calendar item; code freeze | DEC-22 | — | — | Founder (programme) |
| 8 | BSQ-0405 | 4 (2+2) | 07 | UNDEFINED-OWNER | RTO/RPO targets and the L5 multi-region DR drill protocol are registered as [NEEDS DEFINITION] (G-09) but no owner is named to define them; G-09 severity is 'Low→rising'. | L5 exit (Arch §11.2); GATE-004 (first lawful supply needs DR evidence per TASK-REG-017 post-market readiness) | G-09 — no DEC row exists; propose DEC-23 'Name infra owner; set RTO/RPO; approve DR drill protocol' (PROPOSED_AMENDMENTS.md) | — | — | Infra owner [NEEDS DEFINITION] |
| 9 | BSQ-0714 | 4 (2+2) | 10 | DECISION-PENDING | MAK-GOV's 'supersedes_role_of: MAK-J3… pending DEC-06 retirement' and REG-POSTURE v1.1 §2.1/§3.1's retirement argument stand unratified; MAK-GOV §5's 'MAK-J3 retirement n… | GPP first release / retirement; MAK-GOV §5 integration row 10 | DEC-06 (Counsel + product) | — | — | Counsel + product |
| 10 | BSQ-0603 | 3 (1+2) | 09 | DECISION-PENDING | The derived diagrams (and cdss_complete_stack.md in 02_) are regenerated only once DEC-01 ratifies the C-01 relabel portfolio-wide; until then the successor page stands w… | GATE-000 (DEC-01 executes on counsel attestation); W6 T-070..072 final state | DEC-01 | — | — | Regulatory + architecture owners |

### c.1 Build specs — CLAUDE-CODE-EXECUTABLE-NOW rows, full text (eleven headed fields, in order)


#### BSQ-0006 — 04_hardening/HARDEN-3_hardening_plan_worklist.md

**Target path** · 04_hardening/HARDEN-3.1_task_register_delta.md (companion delta; HARDEN-3 v1.0 untouched)

**Class + P-lines satisfied** · WORKLIST/PLAN + DELTA; P-D-01,02,04,08,10,11,14,15,16

**Mandatory sections/fields** ·
- frontmatter (doc_id HARDEN-3.1, version 1.0-delta, date, status honesty line, supersedes: nothing — read HARDEN-3 through this file, req_prefix T, req_count = rows)
- D-1 statement: expands every wave range into one row per artifact
- task table: task_id · wave · artifact_path (resolves on disk) · HARDEN-1 row · CC class · mapped skills (MT2 §2.2) · exit evidence · owner/role · state ∈ {PENDING} (pre-pass placeholder per HARDEN-1 law)
- new IDs for uncovered artifacts: 10_ (7 files) and 05_/REG-R30.1 and 11_/ (flag 11_ as out-of-wave; propose W8 extension) — each marked Proposed
- ID census: T-count equals rows; every T-nnn from HARDEN-3 ranges present exactly once
- self-audit: every artifact_path exists (script output pasted); every T id unique; no artifact without a task

**Inputs (paths)** ·
- `04_hardening/HARDEN-3_hardening_plan_worklist.md`
- `04_hardening/HARDEN-1_coverage_ledger_seed.md`
- `04_hardening/HARDEN-2_hardening_spec.md`
- `11_prompts/runs/2026-09-02_survey-2/census.json (file list)`
- `00_MANIFEST.md §1/§7/§8`

**Laws** · append-only (new file) · delta pattern (MET-1.1/REG-SPRINT-1.1) · MT2 §3 one row per artifact — no batching · law 6: this is a *plan* delta, not an R29 write

**Evidence to capture** · paste of `python3 -c` path-existence check over the task table; T-id uniqueness count; diff showing HARDEN-3 v1.0 byte-identical

**Acceptance test** · every file under 04_–10_ (and 00_, 01_, 02_, 03_ per HARDEN-3 W2–W7) appears exactly once in the table; grep of HARDEN-3 ranges expands to the same set

**Closes rows** · BSQ-0006

**HARDEN linkage** · T-121 (W10, HARDEN-1/2/3 self-referential class) — the delta joins that row; ABSENT-WORKLIST-TASK rows in folders/10_ depend on it

**Ratifying owner** · MT2 operator (DEC-10) / Architecture owner for the W8 extension

**Depends on** · — (none)


#### BSQ-0202 — 05_registers-and-contracts/REG-R30.schema.json

**Target path** · 05_registers-and-contracts/REG-R30.schema.json + 05_registers-and-contracts/REG-R30.2_row-form_seed.jsonl (companions; the .md base and R30.1 untouched)

**Class + P-lines satisfied** · SCHEMA + SEED; P-D-08, P-D-09, P-D-10, P-D-16; CC-4, CC-7

**Mandatory sections/fields** ·
- JSON Schema draft 2020-12 with `$id: cdss-spine/registers/r30-regulatory-posture-row.schema.json`, `title` carrying 'Proposed (DEC-02)'
- properties = REG-R30 field list verbatim (reg_id, statement, status, attesting_party, blocks, cadence, source, version_stamp) + `owner` (register law §12.1(1)) + `blocker` for HALT-TYPED crosswalk
- reg_id pattern enum covering REG-R30 families + R30.1 extension (NDG, NZ-*, SD, SG, EX, REG-KEEP)
- status enum exactly {OPEN, ATTESTED, REFUTED, CLOSED, ARMED, passed} per REG-POSTURE §0.7 crosswalk; if/then: ATTESTED/REFUTED require attesting_party + date; WATCH rows require cadence
- row-form seed: one JSON line per ID enumerated from the R30 + R30.1 ranges, `status` = the *crosswalked* enum value, `source_status_verbatim` field preserving the seed's wording ('standing', 'not started'…) — no source status is altered, only mapped
- recorded validation run (check_schema + every seed row validates) pasted into a companion REG-R30.schema.md § or into INDEX-05 §5

**Inputs (paths)** ·
- `05_registers-and-contracts/REG-R30_regulatory_posture_register.schema+seed.md`
- `05_registers-and-contracts/REG-R30.1_seed_delta.md`
- `10_regulatory-execution/REG-POSTURE_v1.1.md §0.3 (ID scheme), §0.4, §0.7 (crosswalk)`
- `10_regulatory-execution/REG-NZ_v1.0.md (NZ-* rows)`
- `10_regulatory-execution/MAK-GOV_addendum-g_v0.9.md (NDG-1..14)`
- `05_registers-and-contracts/REG-R29.schema.json (house schema form)`

**Laws** · append-only (new files) · EX-7 / MAK-ANT §8: no ASSUME status changes — statuses are mapped, never closed · register law §12.1(2) mutability declared: versioned · law 4: the mapping of 'standing' (obligations) to an enum value is the regulatory owner's call — ship the row with status OPEN and `source_status_verbatim: standing` and file the mapping question (BSQ-0208)

**Evidence to capture** · check_schema output; validator run over the seed rows (count valid = count rows); ID census: rows per family equal the ranges declared in R30/R30.1

**Acceptance test** · every ID in the R30 + R30.1 ranges appears exactly once in the .jsonl; all rows validate; zero ASSUME rows with status other than OPEN

**Closes rows** · BSQ-0202

**HARDEN linkage** · T-005 (W1) R30 schema+seed; T-021 (W3) reconciliation

**Ratifying owner** · Architecture owner (DEC-02) for the schema; regulatory owner for status mapping

**Depends on** · — (none)


#### BSQ-0402 — 07_deployment-and-operations/DEPLOY-1.1_run-map_delta.md

**Target path** · 07_deployment-and-operations/DEPLOY-1.1_run-map_delta.md

**Class + P-lines satisfied** · DEPLOY + DELTA; P-D-01,02,03,10,11,14,15,16

**Mandatory sections/fields** ·
- frontmatter (doc_id DEPLOY-1.1, version 1.1-delta, date, status 'Added; DEPLOY-1 v1.0 not edited; read DEPLOY-1 through this file (EX-5)', supersedes: nothing)
- D-1 step→RUN mapping table: 0a → RUN-0 parallel (MT2 row zero) · 0b → RUN-0 (+TASK-REG-021/022, NZ-TASK-002/003, V1-C1/C2, T-G01/T-G05) · 1 → RUN-1 (+V1-S2, V2-S0) · 2 → RUN-2 (+V2-S1 month-4 checkpoint, V2-E1..E3) · 3 → RUN-2/3 · 4 → RUN-3/4 · 5 → RUN-4; exits = GATE + SG + NZ-GATE per EXEC-1
- D-2 owner column per step (role; person [NEEDS DEFINITION] → DEC-09/DEC-10/G-09)
- D-3 per-step exit evidence + failure handling (what halts the step; where the halt is registered — R30 per EX-10)
- D-4 the DEC-22 dependency stated (delta is in force when DEC-22 closes)
- census: 7 steps mapped; self-audit: every RUN/GATE/TASK id resolves (grep pasted)

**Inputs (paths)** ·
- `07_deployment-and-operations/DEPLOY-1_deployment_plan_and_sequencing.md`
- `10_regulatory-execution/EXEC-1_execution_directive.md (RUN table, EX-1, EX-5, EX-8, EX-10)`
- `10_regulatory-execution/REG-SPRINT-1.1_delta.md (D-1..D-5)`
- `01_north-star-and-transformation/MET-2.1 DEC-22`

**Laws** · append-only · delta pattern · law 3 (REG-SPRINT via 1.1) · law 4 (no ASSUME closed; DEC-07 patient surface stays Blocked in step 0b)

**Evidence to capture** · grep outputs for every cited ID; diff proving DEPLOY-1 v1.0 byte-identical

**Acceptance test** · every DEPLOY-1 step appears once in D-1; every RUN row's contents are either in a DEPLOY-1 step or listed as an addition

**Closes rows** · BSQ-0402

**HARDEN linkage** · W8 (T-100..107 → HARDEN-3.1 row for DEPLOY-1.1)

**Ratifying owner** · Founder (programme) via DEC-22; Architecture owner

**Depends on** · — (none)


#### BSQ-0702 — 11_prompts/runs/{{RUN_DATE}}_primer-0/counsel_packet_AU/ + counsel_packet_NZ/ (PROMPT-P0 Phase 2 outputs)

**Target path** · run 11_prompts/PROMPT-P0_primer0_launch.md Phase 2 as written → 11_prompts/runs/{{RUN_DATE}}_primer-0/counsel_packet_AU/, counsel_packet_NZ/, DRAFT_TASK-REG-001_intended_purpose.md, DRAFT_T-G01_intended_purpose.md

**Class + P-lines satisfied** · REGULATORY packet (ADVISORY_ONLY; HUMAN-ONLY to dispatch); P-D-07, P-D-12, P-D-16

**Mandatory sections/fields** ·
- per PROMPT-P0 Phase 2 item 1: the five EX-6 questions verbatim with ASSUME/Q IDs; attachments by reference (REG-POSTURE §1–§3, MAK-GOV §2, REG-NZ §6 + NZ-Q-004 wording from REG-SPRINT-1.1 D-2); the ASSUME table with current OPEN statuses; a cover note stating what is asked and what is not (no drafting of the answer)
- NZ packet: NZ-ASSUME-001..003 + NZ-Q-004 (D-2) with the three sub-questions EX-6 lists
- dispatch checklist: HUMAN-ONLY send; R30 row lands on dispatch (EX-10) — proposed row text included

**Inputs (paths)** ·
- `10_regulatory-execution/EXEC-1_execution_directive.md EX-6, EX-8`
- `10_regulatory-execution/REG-POSTURE_v1.1.md §1–§3, §8, §9`
- `10_regulatory-execution/MAK-GOV_addendum-g_v0.9.md §2`
- `10_regulatory-execution/REG-NZ_v1.0.md §6`
- `10_regulatory-execution/REG-SPRINT-1.1_delta.md D-2`
- `11_prompts/PROMPT-P0_primer0_launch.md`

**Laws** · PROMPT-P0 laws 1–7 · law 4 (no ASSUME closed; no answer drafted) · ADVISORY_ONLY; licensed/guidance text by reference

**Evidence to capture** · PROMPT-P0's own run outputs (checksum bookends; OPEN_QUESTIONS)

**Acceptance test** · five AU questions present verbatim with IDs; NZ packet carries NZ-Q-004; no status changed anywhere

**Closes rows** · BSQ-0702

**HARDEN linkage** · packet files are instruction-bearing → HARDEN-1.1 rows (CC-4)

**Ratifying owner** · Founder (programme) (dispatch); regulatory owner

**Depends on** · — (none)


#### BSQ-0106 — 04_hardening/HARDEN-3_hardening_plan_worklist.md

**Target path** · 04_hardening/HARDEN-3.1_task_register_delta.md (same file as BSQ-0006 build_spec — one deliverable closes both)

**Class + P-lines satisfied** · as BSQ-0006

**Mandatory sections/fields** ·
- as BSQ-0006, plus: W8 extension row proposing T-108.. for 10_ (before W11), 11_ and 03_ additions; W3 note that T-020 (MAK-ANT/REG-POSTURE v1.0) does not cover REG-POSTURE v1.1 (EX-3 canonical) — new task

**Inputs (paths)** ·
- `as BSQ-0006`
- `10_regulatory-execution/EXEC-1_execution_directive.md EX-3, EX-5`

**Laws** · as BSQ-0006

**Evidence to capture** · as BSQ-0006

**Acceptance test** · as BSQ-0006; additionally: every 10_ file has a task before W11

**Closes rows** · BSQ-0106, BSQ-0006, BSQ-0704

**HARDEN linkage** · T-121 (W10)

**Ratifying owner** · MT2 operator (DEC-10) [NEEDS DEFINITION] / Architecture owner (wave extension)

**Depends on** · BSQ-0104


#### BSQ-0703 — 10_regulatory-execution/* (7 files) — HARDEN-1 rows

**Target path** · 04_hardening/HARDEN-1.1_coverage_ledger_seed_delta.md D-2 (seven rows) — same deliverable as BSQ-0104

**Class + P-lines satisfied** · as BSQ-0104

**Mandatory sections/fields** ·
- rows: EXEC-1 (CC-8), REG-POSTURE_v1.1 (CC-4), REG-NZ (CC-4), MAK-GOV (CC-4 + CC-1 build target), REG-SPRINT_v1.0 (CC-4/CC-5), REG-SPRINT-1.1 (CC-4), FOLD-1 (CC-5/CC-8); owner cdss-governance/regulatory owner; state PENDING

**Inputs (paths)** ·
- `as BSQ-0104`
- `10_regulatory-execution/*`

**Laws** · as BSQ-0104

**Evidence to capture** · as BSQ-0104

**Acceptance test** · 7 rows with resolvable paths

**Closes rows** · BSQ-0703

**HARDEN linkage** · W3 (posture) / W11 (sweep) — HARDEN-3.1 must place them

**Ratifying owner** · Architecture owner (DEC-02)

**Depends on** · BSQ-0104


#### BSQ-0704 — 10_regulatory-execution/* (7 files) — HARDEN-3 tasks

**Target path** · 04_hardening/HARDEN-3.1_task_register_delta.md (tasks added there — BSQ-0006/BSQ-0106)

**Class + P-lines satisfied** · as BSQ-0006

**Mandatory sections/fields** ·
- W3: task for REG-POSTURE_v1.1 (canonical) beside T-020; W8 extension: EXEC-1, REG-NZ, MAK-GOV, REG-SPRINT+1.1, FOLD-1; W11 sweep scope line naming 10_ (EX-5)

**Inputs (paths)** ·
- `as BSQ-0006`

**Laws** · as BSQ-0006

**Evidence to capture** · as BSQ-0006

**Acceptance test** · 7 tasks present before W11

**Closes rows** · BSQ-0704

**HARDEN linkage** · W3/W8/W11

**Ratifying owner** · MT2 operator (DEC-10)

**Depends on** · BSQ-0006


#### BSQ-0403 — 07_deployment-and-operations/OPS-1.1_procedures_cc5_delta.md

**Target path** · 07_deployment-and-operations/OPS-1.1_procedures_cc5_delta.md

**Class + P-lines satisfied** · OPS + DELTA; P-D-01,02,04,05,08,09,10,11,14,15,16; CC-5

**Mandatory sections/fields** ·
- frontmatter (doc_id OPS-1.1, version 1.1-delta, date, status honesty, read-through rule, req_prefix PROC, req_count)
- D-1: each OPS-1 §1–§4 paragraph re-expressed as PROC-nn procedures in Arch §13.6 form: trigger · ordered steps {timeout, retry, idempotent-by, on_fail} · exit evidence artifact (register row) · owner role · source (OPS-1 §, REG-POSTURE §, Arch §)
- D-2: procedure stubs (fields present, values [NEEDS DEFINITION] where the source is silent) for the regulated controls DEPLOY-1 step 2 names — TASK-REG-010 gated pipeline split, -011 SBOM→Ketryx, -012 vuln/CVSS/CAPA, -013 supplier assessment, -014 IEC 62366-1 — and post-market/adverse-event TASK-REG-017 (OBL-002)
- ID census PROC-nn = count; self-audit: every step has all four fields (script output)

**Inputs (paths)** ·
- `07_deployment-and-operations/OPS-1_operating_procedures.md`
- `02_cdss-stack-augmented/architecture_and_integration.md §13.6`
- `10_regulatory-execution/REG-POSTURE_v1.1.md §5–§6 (regulated-work model source), §4.4 obligations`
- `07_deployment-and-operations/DEPLOY-1 step 2`
- `02_cdss-stack-augmented/primer_I_living_evaluation.md I8 (change classes)`

**Laws** · append-only · delta pattern · law 4 (no regulatory position asserted; ADVISORY_ONLY carried) · no vendor-named observer clauses (OPS-1 §3)

**Evidence to capture** · field-presence check output over every PROC step

**Acceptance test** · 0 steps lacking timeout/retry/idempotency/on_fail; every PROC cites its OPS-1 § or TASK-REG id

**Closes rows** · BSQ-0403

**HARDEN linkage** · W8 — CC-5 row for OPS-1 measures against this delta

**Ratifying owner** · Operations owner [NEEDS DEFINITION]; regulatory owner for §3-derived procedures

**Depends on** · — (none)


#### BSQ-0205 — 05_registers-and-contracts/CONTRACT-ARG-1.schema.json (+ CONTRACT-DEV-1.schema.json, CONTRACT-RRI-1.test-spec.md)

**Target path** · 05_registers-and-contracts/CONTRACT-ARG-1.schema.json, CONTRACT-DEV-1.schema.json, CONTRACT-RRI-1_render-invariance_test-spec.md (companions; CONTRACT-ARG-1 .md untouched)

**Class + P-lines satisfied** · CONTRACT + SCHEMA; P-D-01 (title/$id), P-D-09 (recorded validation), P-D-16; CC-7

**Mandatory sections/fields** ·
- ARG schema: `$defs` GenericArgument (8 fields verbatim from CONTRACT-ARG-1 incl. `profile` enum default|GPP and the GPP-9 warrant_type restriction as if/then) and ActualArgument (10 fields; `qualifier` required — SPINE-2; `rebuttals` minItems 1 when grounds non-empty — SPINE-2 via if/then; `pins.version_stamp` required — SPINE-5)
- DEV schema: 7 fields; `severity_tier` enum [NEEDS DEFINITION → DEC/owner]; note 'never blocked except deterministic safety classes (SPINE-8)'
- RRI test-spec: the invariance property as a runnable property test contract (inputs A, f1, f2; content-set equality up to compression/ordering; add/remove/reweight ⇒ fail) with 3 worked examples incl. the LLM-narration case (L10)
- ≥2 example instances per schema (one valid, one violating SPINE-2) with recorded validator output
- breaking-change note per Arch §10
- pointer stubs updated? NO — the existing cdss-spine pointer covers the family; add one line to INDEX-05 instead

**Inputs (paths)** ·
- `05_registers-and-contracts/CONTRACT-ARG-1_argument_schema.md`
- `03_makoha-butterfly-corpus/corpus-md/four-faces-corpus_v1.1.md Part 2 (SPINE-1..9)`
- `02_cdss-stack-augmented/primer_A_bayesian_engine.md A10 (payload supplier)`
- `02_cdss-stack-augmented/primer_F_conformal_wrapper.md F10 (qualifier)`
- `02_cdss-stack-augmented/architecture_and_integration.md §10, §14.2`
- `05_registers-and-contracts/REG-R29.schema.json (house form)`

**Laws** · append-only · Arch §10 contracts live once in spine — these are staged drafts that MOVE on DEC-02+DEC-09 · no clinical numbers authored (thresholds are structure, not values) · MAK-FFC MUSTs are not relaxed (SPINE-2 required fields)

**Evidence to capture** · check_schema outputs; example validation outputs (valid + violating)

**Acceptance test** · a synthetic ActualArgument lacking `qualifier` fails validation; one with all fields passes; the RRI spec's three examples are executable statements

**Closes rows** · BSQ-0205

**HARDEN linkage** · T-001..003 (W1) — CC-7

**Ratifying owner** · Architecture owner (DEC-02)

**Depends on** · — (none)


#### BSQ-0404 — 07_deployment-and-operations/SEC-2_threat-model_and_data-flow.md (+ .mermaid)

**Target path** · 07_deployment-and-operations/SEC-2_threat-model_and_data-flow.md + 09_diagrams/data_flow_v1.mermaid

**Class + P-lines satisfied** · SEC + DIAGRAM; P-D-01,02,04,05,07,08,09,14,16; CC-6 for the diagram

**Mandatory sections/fields** ·
- frontmatter (doc_id SEC-2, version 1.0, date, status 'Proposed; derived from Arch §11 + SEC-1 + REG-POSTURE; no new regulatory claims', req_prefix TM, req_count)
- §1 Data-flow diagram (mermaid) over Arch §11.5 topology: trust boundaries = per-environment accounts, corpus account firewall, registry signing enclave, substrate (Bedrock/Baseten per DEC-03 — both drawn, one marked pending)
- §2 Asset table: data classes (synthetic, EVAL, identifiable-after-GATE-002), keys, ledgers, prompts
- §3 STRIDE-per-boundary table TM-nn: threat · control (cite SEC-1 / Arch §11.1 T1–T5 / REG-FIND-007 mapping) · gap → TASK-REG id or [NEEDS DEFINITION]
- §4 Cross-reference table carrying encryption (KMS/object-lock/TLS), SBOM (TASK-REG-011), CAPA (TASK-REG-012) into the SEC surface by reference
- §5 Pen-test scope statement for TASK-REG-016 derived from §3
- ID census + self-audit (mermaid parse output; every cited control resolves)

**Inputs (paths)** ·
- `07_deployment-and-operations/SEC-1_security_privacy_compliance.md`
- `02_cdss-stack-augmented/architecture_and_integration.md §11.1, §11.4, §11.5`
- `10_regulatory-execution/REG-POSTURE_v1.1.md §4.3 standards stack, §4.4 obligations`
- `07_deployment-and-operations/DEPLOY-1 step 2`
- `09_diagrams/imago_architecture.mermaid (node names)`

**Laws** · append-only · law 4 (DEC-03 substrate open — draw both) · MT2 §1(7) boundaries never weakened — the model documents them · ADVISORY_ONLY carried for regulatory mappings

**Evidence to capture** · mermaid parse output; grep proving every control cited exists in SEC-1/Arch

**Acceptance test** · every trust boundary in Arch §11.5 appears in §1; every SEC floor topic (secrets, access, encryption, SBOM, vuln, supplier, incident/CAPA) has ≥1 TM row

**Closes rows** · BSQ-0404

**HARDEN linkage** · new artifacts → HARDEN-1.1 rows (CC-5 doc, CC-6 diagram); W8/W6

**Ratifying owner** · Security owner [NEEDS DEFINITION]; Architecture owner

**Depends on** · — (none)


#### BSQ-0101 — 04_hardening/INDEX.md

**Target path** · 04_hardening/INDEX.md

**Class + P-lines satisfied** · MANIFEST/INVENTORY (folder index) + BRIEFING; P-F-01, P-F-02, P-F-10, P-D-01, P-D-02, P-D-16

**Mandatory sections/fields** ·
- frontmatter: doc_id INDEX-04, title, version 1.0, date, status ('Added; indexes only; edits nothing; the pass has not run')
- §1 Briefing (≤12 lines): what a DIRECTIVE, SPEC, WORKLIST, SEED are and how they compose into R29 — mirror 02_/primers_briefing.md Part 1 form
- §2 File table: path · class (CC-8) · doc_id · version · status (quoted) · bytes · disposition (Retained/Proposed) · HARDEN-1 row · HARDEN-3 task · 00_MANIFEST row
- §3 Retained-verbatim note for MT2: checksum source (00_MANIFEST §4.1), citation notation rule (DEF-002: §1(7), §7(4) item notation)
- §4 Honesty line mirroring 00_MANIFEST §4.4 for this folder
- §5 Self-audit: file count = disk (`ls` output pasted); every path resolves

**Inputs (paths)** ·
- `04_hardening/* (4 files)`
- `00_MANIFEST.md §1, §4.1, §4.4, §5`
- `04_hardening/HARDEN-1_coverage_ledger_seed.md rows 60–71`
- `04_hardening/HARDEN-3_hardening_plan_worklist.md W10`
- `02_cdss-stack-augmented/primers_briefing.md (form exemplar)`
- `03_makoha-butterfly-corpus/MANIFEST.md (table exemplar)`

**Laws** · append-only (new file only) · law 5 (describe MT2, never edit it) · P-D-02 honesty

**Evidence to capture** · ls -l 04_hardening output; sha256 of MT2 matching 00_MANIFEST §4.1 baseline; grep proving every HARDEN row/task cited exists

**Acceptance test** · table row count == 4 (+INDEX itself); every path exists; every HARDEN-1 row id / T-id resolves in HARDEN-1/HARDEN-3 (or HARDEN-1.1/HARDEN-3.1 once built)

**Closes rows** · BSQ-0101

**HARDEN linkage** · new artifact → needs its own HARDEN-1.1 row and HARDEN-3.1 task (depends on BSQ-0104/BSQ-0006); class CC-8

**Ratifying owner** · Manifest owner [NEEDS DEFINITION] (indexes are manifest-class); proposed as part of 00_MANIFEST A-003

**Depends on** · — (none)


#### BSQ-0104 — 04_hardening/HARDEN-1.1_coverage_ledger_seed_delta.md

**Target path** · 04_hardening/HARDEN-1.1_coverage_ledger_seed_delta.md

**Class + P-lines satisfied** · SEED/LEDGER + DELTA (A-001 pattern); P-D-01,02,04,08,09,10,11,13,14,16; P-F-08

**Mandatory sections/fields** ·
- frontmatter: doc_id HARDEN-1.1, version 1.1-delta, date, status ('Seed delta; all rows PENDING; edits nothing; becomes R29 opening content with HARDEN-1 on DEC-02'), supersedes: nothing — read HARDEN-1 through this file, req_prefix R29-row, req_count = rows added
- D-1: expand rows 60–71 into one row per artifact with resolvable `artifact_path` (21 rows) — HARDEN-1 v1.0 row ids retained, new ids 74+
- D-2: add rows for 10_ ×7 (class CC-4 for REG-*, CC-8 for EXEC-1/FOLD-1, CC-4+CC-1 for MAK-GOV), 05_/REG-R30.1 (CC-2), 01_/MET-2.1 (CC-8), 11_ ×28 (CC-8 — instruction-bearing), 03_/butterfly-primers ×12 + programme prompt + corpus briefing (CC-1/CC-3), 02_/primers_briefing (CC-1), root `AI Evaluator Architecture.md` (UNCLASSIFIED → operator)
- D-3: owner column (role) per row per Arch §12.1(1)
- ID census: total rows; per-class counts; every artifact_path checked by script (output pasted)
- self-audit: no artifact in `find . -type f` (excl. .DS_Store, runs/) lacks a row — paste the diff

**Inputs (paths)** ·
- `04_hardening/HARDEN-1_coverage_ledger_seed.md`
- `05_registers-and-contracts/REG-R29.schema.json`
- `11_prompts/runs/2026-09-02_survey-2/census.json`
- `11_prompts/runs/2026-09-02_survey-2/CHAIN.md`
- `00_MANIFEST.md §1/§7/§8`

**Laws** · append-only (new file) · delta pattern · MT2 §3 one row per artifact · law 6: seed rows are PENDING placeholders — this is pre-ratification seeding (A-001 precedent), not an R29 write

**Evidence to capture** · script output: every artifact_path exists; count of files vs count of rows equal; duplicate-id check

**Acceptance test** · set(rows.artifact_path) == set(files in tree excl. .DS_Store and 11_prompts/runs) — zero missing, zero extra

**Closes rows** · BSQ-0104, BSQ-0703, BSQ-0203

**HARDEN linkage** · T-121 (W10) HARDEN-1/2/3 class — the delta is enumerated there; feeds HARDEN-3.1 (BSQ-0006) which needs the same artifact set

**Ratifying owner** · Architecture owner (DEC-02 ratifies R29 with its opening content)

**Depends on** · — (none)


#### BSQ-0105 — 04_hardening/HARDEN-2.1_spec_census_and_self-audit_delta.md

**Target path** · 04_hardening/HARDEN-2.1_spec_census_and_self-audit_delta.md

**Class + P-lines satisfied** · SPEC + DELTA; P-D-01,02,04,05,08,09,11,16

**Mandatory sections/fields** ·
- frontmatter (doc_id HARDEN-2.1, version 1.1-delta, date, status honesty, supersedes: nothing — read HARDEN-2 through this file, req_prefix CC, req_count 8)
- D-1 source column for every class-bar row: CC-1 → MT2 §1 + 00_MANIFEST §4.2; CC-2 → Arch §12.1; CC-3 → 03_ MANIFEST + MAK-FFC App. C; CC-4 → MAK-ANT §8 / REG-POSTURE §0.4; CC-5 → Arch §13.6; CC-6 → MT2 §2.2 browser-testing; CC-7 → Arch §10; CC-8 → MT2 §7(5)
- D-2 ID census: CC-1..8 (8), anti-rationalization rows AR-1..4 (mint ids), stop-the-line rules STL-1..5 (= MET-1 §9.4 (a)–(e))
- D-3 self-audit (≥6 checks: id uniqueness, census parity, every member list resolves to files, every mechanical check names a tool that exists in MT2 §2.3 or the tree, xref resolution incl. external-pack refs flagged, table integrity) with results

**Inputs (paths)** ·
- `04_hardening/HARDEN-2_hardening_spec.md`
- `04_hardening/MAJOR_TASK_2_anti-laziness-hardening-directive.md §1, §2.2, §2.3, §4–§7`
- `01_north-star-and-transformation/MET-1_metamorphosis_plan_v1.0.md §9.4`
- `03_makoha-butterfly-corpus/corpus-md/four-faces-corpus_v1.1.md Appendix B/C (form exemplar)`

**Laws** · append-only · delta pattern · law 6 (spec delta is not hardening)

**Evidence to capture** · grep outputs proving each cited anchor exists; census count

**Acceptance test** · every CC-n in HARDEN-2 appears once in the census; every source anchor resolves (tools/refcheck.py extended to HARDEN-2.1 shows 0 unresolved)

**Closes rows** · BSQ-0105

**HARDEN linkage** · T-121 (W10)

**Ratifying owner** · MT2 operator (DEC-10) [NEEDS DEFINITION]

**Depends on** · — (none)


#### BSQ-0201 — 05_registers-and-contracts/INDEX.md

**Target path** · 05_registers-and-contracts/INDEX.md

**Class + P-lines satisfied** · folder INDEX + BRIEFING; P-F-01, P-F-02, P-F-10, P-D-01, P-D-02, P-D-16

**Mandatory sections/fields** ·
- frontmatter (doc_id INDEX-05, version, date, status honesty)
- §1 Briefing: what a CONTRACT, SCHEMA, REGISTER, SEED, DELTA are (mirror 02_/primers_briefing.md Part 1); the register-of-registers idea in 6 lines citing Arch §12.1
- §2 File table: path · class · doc_id(s) carried (ARG-1/DEV-1/RRI-1) · version · status · bytes · HARDEN-1 row · HARDEN-3 task · skeleton home on ratification (cdss-spine/contracts, cdss-spine/registers) · DEC gate (DEC-02/DEC-09)
- §3 Reading rule: R30 through R30.1 (P-D-11)
- §4 Honesty line: nothing ratified; no schema moved; R30 has no JSON Schema; no example instances
- §5 Self-audit with pasted `ls -l` and `check_schema` output

**Inputs (paths)** ·
- `05_registers-and-contracts/* (5 files)`
- `06_repositories/repo-skeletons/cdss-spine/registers/README.md`
- `06_repositories/repo-skeletons/cdss-spine/contracts/CONTRACT-ARG-1.pointer.md`
- `04_hardening/HARDEN-1 rows 1–5`
- `02_cdss-stack-augmented/architecture_and_integration.md §12.1, §14.2–14.3`

**Laws** · append-only · law 5 (describe, never edit) · P-D-02

**Evidence to capture** · ls output; check_schema output for REG-R29.schema.json; grep proving pointer stubs exist

**Acceptance test** · 5 rows (+INDEX); every path/HARDEN id/skeleton path resolves

**Closes rows** · BSQ-0201

**HARDEN linkage** · new artifact → HARDEN-1.1 row + HARDEN-3.1 task (W8)

**Ratifying owner** · Manifest owner [NEEDS DEFINITION]; A-003

**Depends on** · — (none)


#### BSQ-0206 — 05_registers-and-contracts/REG-R29.schema.json

**Target path** · 05_registers-and-contracts/REG-R29.examples.jsonl + REG-R29.1_schema_twin_delta.md (companions; .json and .md untouched)

**Class + P-lines satisfied** · SCHEMA; P-D-09, P-D-11

**Mandatory sections/fields** ·
- examples: one HARDENED row (all required fields, mechanical_check_outputs verbatim), one ESCALATED row with blocker (row 0 as in r29_schema_check.txt), one INVALID example (PENDING) with the validator's message — documenting that seed placeholders are not rows
- R29.1 delta: adds `blocker` to the md field list; states 'seed PENDING/BLOCKED marks are pre-pass placeholders and are not R29 rows (HARDEN-1 l.33)'; recorded check_schema + example validation output

**Inputs (paths)** ·
- `05_registers-and-contracts/REG-R29.schema.json`
- `05_registers-and-contracts/REG-R29_hardening_coverage_ledger.schema.md`
- `04_hardening/HARDEN-1_coverage_ledger_seed.md rows 0, 9`

**Laws** · append-only · delta pattern

**Evidence to capture** · validator output for the three examples

**Acceptance test** · 2/2 valid examples validate; the invalid example fails with the quoted message

**Closes rows** · BSQ-0206

**HARDEN linkage** · T-004 (W1)

**Ratifying owner** · Architecture owner (DEC-02)

**Depends on** · — (none)


#### BSQ-0701 — 10_regulatory-execution/INDEX.md

**Target path** · 10_regulatory-execution/INDEX.md

**Class + P-lines satisfied** · folder INDEX + BRIEFING; P-F-01, P-F-02, P-F-10, P-D-01, P-D-02, P-D-11, P-D-16

**Mandatory sections/fields** ·
- frontmatter (doc_id INDEX-10, version, date, status honesty: 'ADVISORY_ONLY content; nothing attested; no packet sent')
- §1 Briefing (≤12 lines): what a posture, a jurisdiction brief, a non-device addendum, a run plan + delta, a fold worklist and an execution directive are; how EX-1/EX-3 precedence works
- §2 File table: path · class · doc_id · version/date_issued · authority · status · bytes · req_prefix/count (or 'none declared') · HARDEN-1 row (ABSENT ×7 until HARDEN-1.1) · HARDEN-3 task (ABSENT ×7 until HARDEN-3.1) · read-through rule · counsel-packet role (EX-6 attachments: REG-POSTURE §1–§3, MAK-GOV §2, REG-NZ §6)
- §3 ID-family map: which file mints which families (REG-POSTURE 12; REG-NZ 7; MAK-GOV NDG; REG-SPRINT V/SG/SD; EXEC-1 EX; FOLD-1 W) and where R30/R30.1 mirror them
- §4 Known gaps carried: REG-FIND-013/TASK-REG-023 forward refs; NZ-Q-004 not in REG-NZ; MAK-GOV §5 integration 2/10; W-namespace collision; no Contents in REG-POSTURE/MAK-GOV
- §5 Honesty line; self-audit (ls; ID resolution)

**Inputs (paths)** ·
- `10_regulatory-execution/* (7 files)`
- `00_MANIFEST.md §8`
- `05_registers-and-contracts/REG-R30.1_seed_delta.md`
- `01_north-star-and-transformation/MET-2.1_decision_register_delta.md`
- `11_prompts/PROMPT-P0_primer0_launch.md Phase 2 (packet spec)`

**Laws** · append-only · law 3 delta reading · law 4 OPEN means OPEN · ADVISORY_ONLY carried; no regulatory position asserted

**Evidence to capture** · ls; grep outputs for every ID family endpoint (both ends — DEF-REG-001 discipline)

**Acceptance test** · 7 rows; every family endpoint resolves; §4 gaps each cite a BSQ row

**Closes rows** · BSQ-0701

**HARDEN linkage** · new artifact → HARDEN-1.1 row (CC-4/CC-8) + HARDEN-3.1 task before W11

**Ratifying owner** · Manifest owner [NEEDS DEFINITION]; regulatory owner for §3

**Depends on** · — (none)


#### BSQ-0705 — 10_regulatory-execution/REG-POSTURE_v1.1_CONTENTS.md (companion) or a §Contents block in v1.2

**Target path** · 10_regulatory-execution/REG-POSTURE_v1.1_CONTENTS.md (companion: a navigational map — the v1.1 text is never edited; a v1.2 can absorb it under §A)

**Class + P-lines satisfied** · REGULATORY companion; P-D-06, P-D-16

**Mandatory sections/fields** ·
- frontmatter (doc_id REG-POSTURE-TOC, companion_to REG-POSTURE v1.1, version, date, authority ADVISORY_ONLY, status 'navigational companion; adds no content')
- § map: every `## §n` / `### n.m` heading with line anchor and one-line gloss; the 12 ID families with their home §; the counsel-attachment set (EX-6: §1–§3) marked
- owner line: 'Regulatory owner [NEEDS DEFINITION — G-09]' repeated so the gap travels with the map

**Inputs (paths)** ·
- `10_regulatory-execution/REG-POSTURE_v1.1.md (headings via grep '^#')`
- `10_regulatory-execution/EXEC-1 EX-6`

**Laws** · append-only · law 5 (companion, not edit) · ADVISORY_ONLY carried

**Evidence to capture** · grep '^#' output pasted beside the map (proves completeness)

**Acceptance test** · every heading in the grep appears once in the map

**Closes rows** · BSQ-0705

**HARDEN linkage** · W3 (beside the REG-POSTURE v1.1 task)

**Ratifying owner** · Regulatory owner [NEEDS DEFINITION — G-09 / REG-POSTURE §12.3]

**Depends on** · — (none)


#### BSQ-0113 — 04_hardening/HARDEN-1_coverage_ledger_seed.md

**Target path** · 04_hardening/HARDEN-1.1_coverage_ledger_seed_delta.md (D-1 of BSQ-0104 — same deliverable)

**Class + P-lines satisfied** · as BSQ-0104

**Mandatory sections/fields** ·
- as BSQ-0104 D-1

**Inputs (paths)** ·
- `as BSQ-0104`

**Laws** · as BSQ-0104

**Evidence to capture** · as BSQ-0104

**Acceptance test** · rows 60–71 expanded to 21 path-resolving rows

**Closes rows** · BSQ-0113

**HARDEN linkage** · T-121

**Ratifying owner** · Architecture owner (DEC-02)

**Depends on** · BSQ-0104


#### BSQ-0203 — 05_registers-and-contracts/REG-R30.1_seed_delta.md

**Target path** · 04_hardening/HARDEN-1.1_coverage_ledger_seed_delta.md (row added there — see BSQ-0104)

**Class + P-lines satisfied** · as BSQ-0104

**Mandatory sections/fields** ·
- row: 05_registers-and-contracts/REG-R30.1_seed_delta.md · CC-2/CC-4 · PENDING · owner cdss-governance

**Inputs (paths)** ·
- `as BSQ-0104`

**Laws** · as BSQ-0104

**Evidence to capture** · as BSQ-0104

**Acceptance test** · row present with resolvable path

**Closes rows** · BSQ-0203

**HARDEN linkage** · T-005/T-021 + new task in HARDEN-3.1

**Ratifying owner** · Architecture owner (DEC-02)

**Depends on** · BSQ-0104


#### BSQ-0708 — 11_prompts/PROMPT-FOLD-1_antennae_v1.1_fold.md

**Target path** · 11_prompts/PROMPT-FOLD-1_antennae_v1.1_fold.md

**Class + P-lines satisfied** · PROMPT (11_) in PROMPT-SERIES form; P-F-05, P-D-15; inherits PROMPT-P0 laws 1–7

**Mandatory sections/fields** ·
- lever · prompt · evidence pack · open questions · eval pack · design notes
- <role>: fold executor; never edits antennae-corpus_v1.0.md; writes `03_makoha-butterfly-corpus/corpus-md/antennae-corpus_v1.1.md` as a NEW file **into the run directory first**, moved into 03_ only by the corpus owner (03_ MANIFEST precedence law; law 2 of SURVEY-2)
- Phases = FOLD-1 W1–W5 verbatim, each with trigger · steps · exit evidence · on_fail (halt + HALT_LOG; never partial fold) · owner
- W2 carrier-map rows as a table the run must fill; W4 both-ends check as a script with pasted output; W5 seal = MAK-ANT Appendix B checks 1–10 run + byte-identity of Annex 1 vs REG-POSTURE_v1.1.md (sha256 pasted)
- Output contract: the new volume + RUN-REPORT + proposed MET-2.1 C-13 closure-date text + proposed 03_ MANIFEST row (never written by the run)
- Eval pack ≥ 5 (incl. 'annex not byte-identical → halt'; 'missing carrier → ESCALATE not invent')

**Inputs (paths)** ·
- `10_regulatory-execution/FOLD-1_antennae_fold_worklist.md`
- `10_regulatory-execution/REG-POSTURE_v1.1.md (§12.4 fold checklist; full text for the annex)`
- `03_makoha-butterfly-corpus/corpus-md/antennae-corpus_v1.0.md (wrapper Parts 0–4; Appendix B checks)`
- `03_makoha-butterfly-corpus/MANIFEST.md`
- `11_prompts/PROMPT-P0_primer0_launch.md §1 laws`
- `11_prompts/PROMPT-SERIES_A-L_index.md`

**Laws** · append-only · 03_ MANIFEST precedence — corpus owner moves the file · AN-5 (carrier map re-run before seal) · EX-3 (canonical = 10_/REG-POSTURE_v1.1.md) · law 4 (no ASSUME closes in the fold)

**Evidence to capture** · sha256 of Annex 1 vs canonical; Appendix B check outputs; carrier-map completeness count

**Acceptance test** · W5 passes with pasted outputs; v1.0 file byte-identical; new file validates against MAK-ANT frontmatter contract (req_count 12 unchanged)

**Closes rows** · BSQ-0708

**HARDEN linkage** · HARDEN-3.1 W3 task (MAK-ANT v1.1 supersedes T-020's target); the prompt itself is CC-8

**Ratifying owner** · Regulatory owner [NEEDS DEFINITION — G-09 / REG-POSTURE §12.3] + corpus owner

**Depends on** · — (none)


#### BSQ-0204 — 05_registers-and-contracts/REG-R30.1_seed_delta.md

**Target path** · 04_hardening/HARDEN-3.1_task_register_delta.md (task added there — see BSQ-0006)

**Class + P-lines satisfied** · as BSQ-0006

**Mandatory sections/fields** ·
- task row for REG-R30.1 in W3 beside T-021

**Inputs (paths)** ·
- `as BSQ-0006`

**Laws** · as BSQ-0006

**Evidence to capture** · as BSQ-0006

**Acceptance test** · task present

**Closes rows** · BSQ-0204

**HARDEN linkage** · W3

**Ratifying owner** · MT2 operator (DEC-10)

**Depends on** · BSQ-0006


#### BSQ-0390 — 06_repositories/INDEX.md

**Target path** · 06_repositories/INDEX.md

**Class + P-lines satisfied** · folder INDEX + BRIEFING; P-F-01, P-F-02, P-F-10, P-D-01, P-D-02, P-D-09, P-D-16

**Mandatory sections/fields** ·
- frontmatter (doc_id INDEX-06, version, date, status honesty: 'no code; skeletons Proposed; DEC-09 open')
- §1 Briefing (≤12 lines): what a skeleton tree is, how it mirrors a primer's §-4/§-8, the move-never-copy rule, the lockfile home question (DEC-09)
- §2 Tree table (19 rows): repo · owning primer/volume (or 'NONE — see BSQ-0391' for cdss-compiler) · REPO-MAP status · files · README/MANIFEST/CI/CODEOWNERS present (Y/N) · sub-dir stubs · launch prompt in 11_ · HARDEN-1 row (A-001 glob) · HARDEN-3 task
- §3 File table (90 rows, generated by tools/skeleton_check.py and pasted): path · bytes · banner Y/N · check result
- §4 Known gaps carried until instantiation: 13 unbannered files (list); 5 existing repos without CI stub; RUN-REPORT R6 repo proposals pending DEC-09
- §5 Honesty line + self-audit (counts pasted; every path exists)

**Inputs (paths)** ·
- `06_repositories/REPO-MAP_v2.md`
- `06_repositories/repo-skeletons/** (90 files)`
- `11_prompts/runs/2026-09-02_survey-2/folders/06_repositories/skeleton_summary.json`
- `11_prompts/runs/2026-09-02_survey-2/folders/06_repositories/skeleton_rows.jsonl`
- `04_hardening/HARDEN-1_coverage_ledger_seed.md A-001`
- `03_makoha-butterfly-corpus/butterfly-primers/RUN-REPORT.md R6`

**Laws** · append-only (new file; no skeleton file edited) · law 5 · P-D-02 honesty

**Evidence to capture** · re-run of tools/skeleton_check.py pasted; `find … | wc -l` = 91

**Acceptance test** · 19 tree rows and 90 file rows; every path exists; counts equal disk; every REPO-MAP row appears once

**Closes rows** · BSQ-0390

**HARDEN linkage** · A-001 glob row (W8) — the INDEX is the enumeration the glob will produce; new artifact needs its own row in HARDEN-1.1

**Ratifying owner** · Manifest owner [NEEDS DEFINITION]; A-003

**Depends on** · — (none)


#### BSQ-0401 — 07_deployment-and-operations/INDEX.md

**Target path** · 07_deployment-and-operations/INDEX.md

**Class + P-lines satisfied** · folder INDEX + BRIEFING; P-F-01, P-F-02, P-F-10, P-D-01, P-D-02, P-D-16

**Mandatory sections/fields** ·
- frontmatter (doc_id INDEX-07, version, date, status honesty: 'nothing deployed; all Proposed/Retained per file')
- §1 Briefing: what DEPLOY (plan), acceptance criteria, OPS procedure, GOV and SEC documents are and how they compose with Arch §11 and EXEC-1
- §2 File table: path · class · doc_id · version · date (as of manifest: 2026-09-01) · status quoted · bytes · HARDEN-1 row · HARDEN-3 task · read-through rule (DEPLOY-1 via DEPLOY-1.1 once built)
- §3 Precedence note: EXEC-1 EX-1/EX-5 govern sequencing — steps map to RUN rows (pointer to DEPLOY-1.1)
- §4 Honesty line; §5 self-audit (ls pasted; paths resolve)

**Inputs (paths)** ·
- `07_deployment-and-operations/* (5 files)`
- `10_regulatory-execution/EXEC-1_execution_directive.md EX-1, EX-5, RUN table`
- `04_hardening/HARDEN-1 l.29; HARDEN-3 W8`
- `02_cdss-stack-augmented/primers_briefing.md (form)`

**Laws** · append-only · law 5 (Retained §§ described, never edited)

**Evidence to capture** · ls output; grep proving each cited ID resolves

**Acceptance test** · 5 rows + INDEX; every path/ID resolves

**Closes rows** · BSQ-0401

**HARDEN linkage** · W8 (new artifact → HARDEN-1.1 row)

**Ratifying owner** · Manifest owner [NEEDS DEFINITION]; A-003

**Depends on** · — (none)


#### BSQ-0501 — 08_research/INDEX.md

**Target path** · 08_research/INDEX.md

**Class + P-lines satisfied** · folder INDEX + BRIEFING; P-F-01, P-F-02, P-F-10, P-D-01, P-D-02

**Mandatory sections/fields** ·
- frontmatter (doc_id INDEX-08, version, date, status)
- §1 Briefing (≤8 lines): what a research/source map is; how RG-nn gaps close (owner acts → finding lands in RESEARCH-1.n delta → MET-4/R30 row updated by its owner)
- §2 File table (1 row + this index): path · class · doc_id · version · date · status (as-of note: 'no status field in v1.0; honesty in §1/§3 text') · bytes · HARDEN-1 row (60–71 collapsed) · HARDEN-3 task (T-100..107) · read-through (RESEARCH-1.1 when built)
- §3 RG register mirror: RG-01..06 · Who · state OPEN · closes-into (DEC-12 / GATE-000 / ASSUME-REG-004 / DEC-04 / MAK-ELSM §05 / WATCH-REG-002)
- §4 Honesty line; §5 self-audit (ls; ID resolution)

**Inputs (paths)** ·
- `08_research/RESEARCH-1_findings_gaps_source_map.md`
- `01_north-star-and-transformation/MET-4_gap_analysis_and_roadmap.md`
- `05_registers-and-contracts/REG-R30.1_seed_delta.md (SRC-REG-011..014)`

**Laws** · append-only · law 5 (RESEARCH-1 not edited)

**Evidence to capture** · ls; grep proving RG/SRC/DEC ids resolve

**Acceptance test** · 1 file row; 6 RG rows each with owner + closes-into

**Closes rows** · BSQ-0501

**HARDEN linkage** · W8; HARDEN-1.1 row for the index

**Ratifying owner** · Manifest owner [NEEDS DEFINITION]; A-003

**Depends on** · — (none)


#### BSQ-0601 — 09_diagrams/INDEX.md

**Target path** · 09_diagrams/INDEX.md

**Class + P-lines satisfied** · folder INDEX + BRIEFING; P-F-01, P-F-02, P-F-10, P-D-01, P-D-09, P-D-16

**Mandatory sections/fields** ·
- frontmatter (doc_id INDEX-09, version, date, status honesty)
- §1 Briefing: sources are canonical, the html is derived; what 'successor' means (G-10, X1)
- §2 File table: path · IMAGO id · source documents (Arch §, MET-1 §, DEPLOY-1, Primer 0 §4) · status · version/date (as-of 2026-09-01) · bytes · HARDEN-1 row 43 · T-072 · inlined-block # in html
- §3 Recorded self-audit: mermaid parse output (tool+version) and source↔inline identity output (paste from tools/mermaid/parse.mjs and the identity script — commit both scripts beside the index as 09_diagrams/tools/ or reference 11_/runs)
- §4 Regeneration procedure in CC-5 form (trigger: DEC-01 close or any source edit; steps with idempotent re-inline; exit: parse PASS + identity PASS + date bump; on_fail: halt, DEF row) and the known defects carried (MT2 §7.4 → §7(4) in IMAGO-3; R25 label) until v3 successors land
- §5 Honesty line

**Inputs (paths)** ·
- `09_diagrams/* (5 files)`
- `00_MANIFEST.md §5 DEF-001`
- `04_hardening/HARDEN-1 row 43; HARDEN-3 T-072`
- `01_north-star-and-transformation/MET-4 G-10`
- `11_prompts/runs/2026-09-02_survey-2/mermaid_parse.json`
- `11_prompts/runs/2026-09-02_survey-2/tools/mermaid/parse.mjs`

**Laws** · append-only (new file) · law 5 (v2 files never edited; fixes are v3 successors) · CC-6

**Evidence to capture** · parse + identity outputs

**Acceptance test** · 5 rows; both outputs pasted; every cited § resolves

**Closes rows** · BSQ-0601

**HARDEN linkage** · T-072 (W6); row 43 bundle

**Ratifying owner** · Manifest owner [NEEDS DEFINITION]; architecture owner for §4

**Depends on** · — (none)


#### BSQ-0706 — 10_regulatory-execution/REG-NZ-1.1_delta.md

**Target path** · 10_regulatory-execution/REG-NZ-1.1_delta.md

**Class + P-lines satisfied** · REGULATORY + DELTA (REG-SPRINT-1.1 form); P-D-01,02,03,04,08,09,10,11,13,16

**Mandatory sections/fields** ·
- frontmatter (doc_id REG-NZ-1.1, version 1.1-delta, authority ADVISORY_ONLY, date_issued, applies_to REG-NZ v1.0, change_policy additive)
- D-1 §6 row NZ-Q-004 quoted verbatim from REG-SPRINT-1.1 D-2 with party (NZ counsel / MoH) and status OPEN; cross-join to NZ-ASSUME-005 (EX-7)
- D-2 blocked-gate column for every §6 row (NZ-GATE-0/1/2 per REG-NZ §5 sequencing)
- D-3 ID census per family (NZ-FIND 9, NZ-OBL 10, NZ-ASSUME 4(+005 per R30.1 — state where it is defined), NZ-TASK 8, NZ-WATCH 3, NZ-Q 4, NZ-SRC 5) with endpoints checked both ends
- D-4 self-audit in REG-POSTURE §12.2 form (≥6 checks) with results
- statement that REG-NZ v1.0 is read only through this delta (EX-2 pattern)

**Inputs (paths)** ·
- `10_regulatory-execution/REG-NZ_v1.0.md`
- `10_regulatory-execution/REG-SPRINT-1.1_delta.md D-2`
- `05_registers-and-contracts/REG-R30.1_seed_delta.md`
- `10_regulatory-execution/EXEC-1 EX-6, EX-7`
- `10_regulatory-execution/REG-POSTURE_v1.1.md §12 (form exemplar)`

**Laws** · append-only · delta pattern · law 4: NZ-ASSUME-* stay OPEN; no regulatory position asserted · ADVISORY_ONLY

**Evidence to capture** · grep outputs for family endpoints; self-audit results

**Acceptance test** · NZ-Q-004 present; census counts equal greps; every §6 row has party + gate

**Closes rows** · BSQ-0706

**HARDEN linkage** · HARDEN-3.1 W8 task for REG-NZ (+1.1)

**Ratifying owner** · Regulatory owner [NEEDS DEFINITION — G-09 / REG-POSTURE §12.3]

**Depends on** · — (none)


#### BSQ-0709 — 10_regulatory-execution/REG-SPRINT_ID-census_companion.md

**Target path** · 10_regulatory-execution/REG-SPRINT-1.2_census_delta.md (delta over v1.0+1.1; both untouched)

**Class + P-lines satisfied** · WORKLIST + DELTA; P-D-04, P-D-08, P-D-09, P-D-10, P-D-11

**Mandatory sections/fields** ·
- frontmatter (doc_id REG-SPRINT-1.2, version 1.2-delta, authority ADVISORY_ONLY, applies_to v1.0 + 1.1, change_policy)
- D-6 ID census: every V*/SG-*/SD-* id with defining location (v1.0 § / 1.1 D-n), current R30.1 status, owner role, exit gate
- D-7 declaration block: prefixes {V1-S, V1-C, V2-S, V2-E, SG-V1, SG-V2, SD}, counts
- self-audit: census equals grep; every SD-nn resolves to MET-2.1 DEC-17..21; every SG names its sprint

**Inputs (paths)** ·
- `10_regulatory-execution/REG-SPRINT_v1.0.md`
- `10_regulatory-execution/REG-SPRINT-1.1_delta.md`
- `05_registers-and-contracts/REG-R30.1_seed_delta.md`
- `01_north-star-and-transformation/MET-2.1_decision_register_delta.md`

**Laws** · append-only · EX-2 (v1.0 read through deltas) · law 4 (statuses quoted from R30.1, not changed)

**Evidence to capture** · grep outputs; count

**Acceptance test** · census count equals the union of ids grepped from v1.0 + 1.1; zero ids without owner/gate

**Closes rows** · BSQ-0709

**HARDEN linkage** · HARDEN-3.1 W8 task for REG-SPRINT family

**Ratifying owner** · Founder (programme)

**Depends on** · — (none)


## e. What is NOT required (dismissed, below-threshold, and escalated-not-buildable)


### e.1 Dismissed as not blocking (7)

| Row | Folder | Class | Statement (short) | Dismissal reason |
|---|---|---|---|---|
| BSQ-0102 | 04 | ABSENT-CHAIN-LINK | No briefing exists for 04_; a briefing section inside INDEX.md (BSQ-0101) satisfies P-F-01 for a four-file folder, so a standalone briefing  | Folded into BSQ-0101 §1; a separate file would duplicate 01_/MET-1.1's table |
| BSQ-0112 | 04 | TACIT-KNOWLEDGE-REQUIRED | MT2 cites 11 pack-internal files (docs/agents.md, references/*.md ×9 incl. definition-of-done.md, orchestration-patterns.md) and HARDEN-2 ci | By design: MT2 §2.1 makes row zero (whole-pack install) the precondition; the INDEX (BSQ-0101) will state which references are external and where they come from |
| BSQ-0210 | 05 | ABSENT-CHAIN-LINK | The registers/ skeleton names R29/R30 in its README but carries no per-schema pointer stub as contracts/ does for CONTRACT-ARG-1; cosmetic u | README already names the drafts and the move rule; a stub adds no check until the move happens on DEC-02 |
| BSQ-0395 | 06 | ABSENT-CHAIN-LINK | No launch prompt runs the skeleton conformance check; this run's tools/skeleton_check.py is the first. A prompt is not required — the script | tools/skeleton_check.py is committed in this run directory and is cited by INDEX-06's build spec; a prompt wrapper adds nothing until repos exist |
| BSQ-0406 | 07 | PROPOSED-ADDITION | A rendered page for DEPLOY-1 (as 03_ volumes have) does not exist; the ladders are drawn in 09_/deployment_ladders.mermaid and inlined in cd | the diagram twin in 09_ already serves the board-facing need; a page would duplicate DEPLOY-1 text (drift risk, X1) |
| BSQ-0408 | 07 | ABSENT-CHAIN-LINK | No DEPLOY launch prompt exists; the Claude-Code-executable portion of DEPLOY-1 (L1 synthetic build) is PROMPT-P0 + PROMPT-A..L; the remainde | covered by PROMPT-SERIES; a DEPLOY prompt would instruct humans, not a Claude Code session |
| BSQ-0605 | 09 | ABSENT-CHAIN-LINK | No regeneration prompt exists; the procedure fits in INDEX-09 §4 (CC-5 form) and is gated on DEC-01, so a standalone prompt is not required  | procedure lands in INDEX-09 §4; a prompt is warranted only when DEC-01 closes and the regeneration touches 02_ derived files too |

### e.2 Open but below the queue threshold (weight 1–2; 21) — recommended where marked, never required for code freeze

| Row | W | Folder | Class | Statement (short) | Executability |
|---|---|---|---|---|---|
| BSQ-0002 | 2 | 09 | DANGLING-REF | Node label cites 'MT2 §7.4' — MT2 §7 contains numbered items, not subsections; DEF-002 normalized this notation elsewhere but this file was  | CLAUDE-CODE-EXECUTABLE-NOW |
| BSQ-0003 | 2 | 09 | DANGLING-REF | Node label cites 'MT2 §7.4' — MT2 §7 contains numbered items, not subsections; DEF-002 normalized this notation elsewhere but this file was  | CLAUDE-CODE-EXECUTABLE-NOW |
| BSQ-0392 | 2 | 06 | ABSENT-ITEM | Six trees have no CI stub — including cdss-evalstack (where every other stub says pipeline definitions are imported from) and cdss-governanc | CLAUDE-CODE-EXECUTABLE-NOW |
| BSQ-0502 | 2 | 08 | PLACEHOLDER-UNREGISTERED | Research findings made after 2026-09-01 live only in 11_/PROMPT-SERIES's evidence pack — the Lumos cohort figure discrepancy (indexed paper  | CLAUDE-CODE-EXECUTABLE-NOW |
| BSQ-0503 | 2 | 08 | DECISION-PENDING | RG-01 closes only when DEC-12 commissions the HeyDoc clone inventory; RG-02..06 close by counsel/Baseten/Legal/owners (EXTERNAL-PARTY) — non | HUMAN-ONLY |
| BSQ-0604 | 2 | 09 | PROPOSED-ADDITION | No skeleton directory is named as the future home of the four .mermaid sources; Arch §10 places the architecture document in cdss-spine, whi | EXECUTABLE-AFTER-DECISION |
| BSQ-0606 | 2 | 09 | PROPOSED-ADDITION | IMAGO-4 draws DEPLOY-1's pre-EXEC-1 calendar; once DEPLOY-1.1 (BSQ-0402) maps steps to RUN-0..4, a v2 source with the run overlay keeps the  | CLAUDE-CODE-EXECUTABLE-NOW |
| BSQ-0710 | 2 | 10 | PROPOSED-ADDITION | Counsel-facing documents have no rendered page (antennae-corpus.html carries v1.0); the packet can attach markdown/PDF, so a page is a conve | EXECUTABLE-AFTER-DECISION |
| BSQ-03xx ×13 | 1 | 06 | QUALITY-BELOW-BAR | 13 skeleton files with no Proposed/skeleton/stub marker (listed in folders/06_repositories/ASSESSMENT.md §4 and skeleton_rows.jsonl) | CLAUDE-CODE-EXECUTABLE-NOW (via INDEX-06 §4) |

### e.3 Escalated — cannot be built by a session, must be ruled (5)

| Row | W | Folder | Class | Blocker | Decision ref |
|---|---|---|---|---|---|
| BSQ-0004 | 2 | 09 | CONTRADICTION | manifest is append-only and owner-written; this run may only propose the DEF-003 text | Manifest owner appends DEF-003 (PROPOSED_AMENDMENTS.md carries the text); no DEC row exists for manifest defects — [NEEDS DEFINITION] |
| BSQ-0393 | 2 | 06 | CONTRADICTION | 00_MANIFEST is owner-written and append-only; the 13 files are skeleton stubs whose banner fix lands at instantiation or via INDEX-06 §4 | Manifest owner: DEF-004 text in PROPOSED_AMENDMENTS.md (no DEC row exists for manifest defects — [NEEDS DEFINITION]) |
| BSQ-0602 | 2 | 09 | CONTRADICTION | two ratified-layer sources disagree on a register's name; a survey may not pick a winner (MT2 §6) | Architecture owner ruling on the R25 house name (register-law change if the name moves — Arch §12.1; no DEC exists → [NEEDS DEFINITION]) |
| BSQ-0711 | 2 | 10 | CONTRADICTION | two worklists own the same bare ids; a survey may not rename either (MT2 §6) | Architecture owner (namespace law §13.3) — rename FOLD-1 steps FW-1..5 in a FOLD-1.1 delta; no DEC exists → [NEEDS DEFINITION] |
| BSQ-0715 | 2 | 10 | CONTRADICTION | manifest is owner-written and append-only | Manifest owner: either point 'drafted' at EX-6 explicitly or amend to 'specified (EX-6), not yet assembled' — text in PROPOSED_AMENDMENTS.md; [NEEDS DEFINITION] |

**Length-only findings dismissed by name:** none were filed. The 20–60× byte gap between 01_–03_ and 04_–10_ appears in no row as a defect; every row cites a P-line or a class-contract line (the_one_rule).

