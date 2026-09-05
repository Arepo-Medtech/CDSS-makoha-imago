---
doc_id: MET-4.1
title: "MET-4.1 — gap register delta: owner, person-or-decision, run/gate, exit evidence and register home per gap; G declared and censused; G-09 narrowed"
version: "1.1-delta"
date: "2026-09-05"
status: "Added (sprint-2). Additive delta over MET-4 v1.1 (not edited); read MET-4 through this file. Fills the execution columns the survey-3 Queue found absent (QI-0018, CRITICAL). Persons are the accounts named in MET-2.2 §1; where a role is unnamed the cell reads [NEEDS DEFINITION] and names its decision. No gap is closed by this file; no decision is closed by this file."
supersedes: "nothing — MET-4 v1.1 preserved verbatim beside this file"
applies_to: "01_north-star-and-transformation/MET-4_gap_analysis_and_roadmap.md"
change_policy: "Additive delta per the MET-1.1 pattern; gap ids G-01..G-11 retained; no gap re-severed"
req_prefix: G
req_count: 11
produced_by: "sprint-2 (survey-3 Queue §c.1 row QI-0018) — 11_prompts/runs/2026-09-05_sprint-2/"
---

# MET-4.1 — gap register delta

## D-0 — why

MET-4 v1.1 tables the eleven gaps as Gap · Evidence · Severity · Delta only. G-02 gates GATE-000 and
G-03 gates code freeze, yet no row says who owns the gap, which decision or person resolves it, which
EXEC-1 run it sits in, what evidence closes it, or which register records the closure (survey-3
QI-0018, confidence 90). The form below is DEPLOY-1.1 D-2/D-3 (owner · person/DEC · exit evidence)
applied to gaps. Timeline cells are read against the EXEC-1 run map, in force since DEC-22 closed
(MET-2.2 §3.1).

## D-1 — execution columns

| Gap | Owner (role) | Person / DEC (MET-2.2 §1, §2) | RUN / gate (EXEC-1) | Exit evidence | Register home |
|---|---|---|---|---|---|
| G-01 fabric/GAAM: no public implementation | Architecture owner; cdss-fabric repo owner | Kenny-bytes; DEC-04 (Open — ledger substrate) | RUN-1 · Foundation (L1 fabric-v0 schema in spine; MET-4 P0/P1) | fabric-v0 argument schema landed in `cdss-spine` (pointer stub → `05_registers-and-contracts/CONTRACT-ARG-1.schema.json`); Stranieri collaboration opened (P1) and recorded as a RESEARCH-1.n finding | R26 (build work); R25 (build evidence) |
| G-02 regulatory relabel unattested | Regulatory owner | kendo-Jones; DEC-01 (Closed — ratified 2026-09-05; attestation separate); `ASSUME-REG-001/002` (OPEN, counsel) | RUN-0 · Decide → `GATE-000` (`TASK-REG-001/002`) | counsel's written classification opinion, dated; `ASSUME-REG-001/002` marked ATTESTED or REFUTED with date in REG-POSTURE's next version | R30 (`GATE-000`, `ASSUME-REG-*` rows) |
| G-03 MT2 pass unexecuted; engine uninstalled | MT2 operator | Kenny-bytes; DEC-10, DEC-11 (Closed 2026-09-05) | RUN-0 · parallel track (EX-5: not rescheduled; MET-4 P0) | R29 row zero written by the pass (whole-pack install; inventory directive-says/observed/installed); W0 report; 100 % of ledger rows HARDENED or ESCALATED at W11 | R29 (schema of record `05_registers-and-contracts/REG-R29.schema.json` with its twin `05_registers-and-contracts/REG-R29.1_schema_twin_delta.md`) |
| G-04 patient-surface scope undecided | Counsel + product | [NEEDS DEFINITION — DEC-07]; DEC-07 (Open) | RUN-0 · Decide → `GATE-000` (`TASK-REG-004`) | DEC-07 ruling recorded in MET-2.n; `ASSUME-REG-003` ATTESTED/REFUTED; `TASK-REG-004` DONE-WITH-EVIDENCE | MET-2 (DEC-07); R30 (`ASSUME-REG-003`) |
| G-05 FZ ratification ambiguity | Corpus owner + clinical review | [NEEDS DEFINITION — DEC-05]; DEC-05 (Open) | RUN-2 · Controls & domain (MET-4 P2 "DEC-05 fuzzy review") | DEC-05 ruling (ratify or defer FZ-1..6) recorded; MAK-DOT successor page by the corpus owner if ratified | MET-2 (DEC-05); R26 |
| G-06 substrate conflict | Infrastructure owner + Regulatory owner | Ken-nough + kendo-Jones; DEC-03 (Open) | RUN-1 · Foundation → `GATE-001` (`TASK-REG-009`) | DEC-03 ruling recorded; `ASSUME-REG-004` (Baseten terms) or Bedrock pinning evidence per C-16 | MET-2 (DEC-03); R30 (`ASSUME-REG-004`) |
| G-07 PF-4 custody more build than it looks | cdss-fabric repo owner (Architecture owner) | Kenny-bytes; no decision — build item under DEC-09 (Closed) | RUN-1 → RUN-2 (L1 → L2 fabric evaluator wrap; Arch §14.5) | custody design recorded in `cdss-fabric` README/MANIFEST (repo skeleton → repo); property runs in R25 | R26; R25 |
| G-08 HeyDoc below-README uninventoried | Corpus custodian | [NEEDS DEFINITION — DEC-12]; DEC-12 (Open) | RUN-1 · Foundation (MET-4 P1 "DEC-12 HeyDoc inventory") | inventory delivered and registered as a RESEARCH-1.n finding; `RG-01` closes | RESEARCH-1.n (`RG-01`); R9 (seed provenance) |
| G-09 DR/RTO/RPO, org owners, commercial thresholds | Founder (names); Infrastructure owner (values) | Kenny-bytes (names — Closed in MET-2.2 §1/§3.10); Ken-nough (values); DEC-23 (names closed; values Open) | RUN-1 for the owner map (this delta + REG-TASK-OWNERS); L5 / `GATE-004` for the DR drill (DEPLOY-1 §T5) | **narrowed:** regulatory / infrastructure / security owners named (MET-2.2 §1); still owed: RTO/RPO targets, L5 multi-region drill protocol and commercial thresholds in a DEPLOY-1.2 delta by the infrastructure owner | MET-2.2 (DEC-23); DEPLOY-1.2 when written |
| G-10 derived-artifact drift | Architecture owner | Kenny-bytes; DEC-01 (Closed 2026-09-05) | RUN-1 (MET-4 P1 "regenerate derived artifacts") — EXECUTABLE-NOW since DEC-01 closed | PROC-09-REGEN run: `09_diagrams/register_topology_v4.mermaid` + `09_diagrams/cdss_diagrams_v4.html` (this sprint, parse pasted in INDEX-09.1); regeneration of `02_cdss-stack-augmented/cdss_complete_stack.md` and `cdss_diagrams.html` successors still queued (HARDEN-1 rows 41–42) | INDEX-09 §4; R29 rows 41–42, 220+ |
| G-11 skill-pack count drift; 0.6.4 eval framework unmapped | MT2 operator | Kenny-bytes; DEC-11 (Closed 2026-09-05) | RUN-0 · parallel track (row zero, W0) | row-zero inventory table (directive-says / observed / installed) with any delta recorded verbatim; halt if irreconcilable (C-11) | R29 row 0 |

## D-2 — census

G family: G-01..G-11 = 11 rows minted in MET-1 v1.0 §17 and carried by MET-4 v1.1; 11 rows above;
no gap added, none retired. Cells: 66; empty: 0; `[NEEDS DEFINITION]` cells: 3 (G-04, G-05, G-08 —
each names its resolving decision: DEC-07, DEC-05, DEC-12). Severity column of MET-4 unchanged.

## D-3 — self-audit (run 2026-09-05; commands from the repository root)

Every DEC, RUN and GATE cited in D-1 exists in its source:

```
grep -c '^| DEC-0[1-9]\|^| DEC-1[0-9]\|^| DEC-2[0-6]' 01_north-star-and-transformation/MET-2.2_decision_closures_delta.md   → 26
grep -o 'DEC-[0-9]*' 01_north-star-and-transformation/MET-4.1_gap_register_delta.md | sort -u                            → DEC-01 DEC-03 DEC-04 DEC-05 DEC-07 DEC-09 DEC-10 DEC-11 DEC-12 DEC-23 (all in MET-2.2 §2)
grep -c '^| \*\*RUN-[0-4]' 10_regulatory-execution/EXEC-1_execution_directive.md                                           → 5
grep -o 'GATE-00[0-4]' 01_north-star-and-transformation/MET-4.1_gap_register_delta.md | sort -u                            → GATE-000 GATE-001 GATE-004 (REG-POSTURE v1.2 §7 phase headers)
grep -c '^| G-' 01_north-star-and-transformation/MET-4.1_gap_register_delta.md                                             → 11
```

Person cells resolve to MET-2.2 §1 (Kenny-bytes, kendo-Jones, Ken-nough) or to `[NEEDS DEFINITION]`
with a decision id. No cell states a date the run map does not state.

## D-4 — what this delta did not do

Closed no gap (a gap closes when its exit evidence exists and is registered), closed no decision,
edited MET-4 or MET-2/2.1/2.2, wrote no R29 row, set no RTO/RPO value. Ledger row and task for this
file: HARDEN-1.2 / HARDEN-3.2 (same sprint).
