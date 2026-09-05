---
doc_id: DEPLOY-1.1
title: "DEPLOY-1.1 — run-map delta: DEPLOY-1 steps 0a–5 read against EXEC-1 RUN-0..4"
version: "1.1-delta"
date: "2026-09-05"
status: "Added; DEPLOY-1 v1.0 not edited; read DEPLOY-1 through this file (EXEC-1 EX-5). In force as sequencing only when DEC-22 closes (adopt EXEC-1 precedence and the run map); until then it is the drafted mapping the decision would adopt. Nothing here closes an ASSUME, moves a gate, or changes DEPLOY-1's content authority."
supersedes: "nothing — DEPLOY-1 v1.0 is preserved verbatim beside this file"
applies_to: "07_deployment-and-operations/DEPLOY-1_deployment_plan_and_sequencing.md"
precedence: "EXEC-1 EX-1 (10_ governs sequencing) · EX-2 (REG-SPRINT read through 1.1) · EX-5 (every DEPLOY-1 sequence is read against the run map). Content: Arch §11 (levels/tiers, Retained), MAK-ANT §7 / REG-POSTURE §7 (phases/gates), MT2 (pass) — unchanged."
change_policy: "Additive delta per the MET-1.1 / REG-SPRINT-1.1 pattern. DEPLOY-1 text stands except where a D-row names it."
req_prefix: DR
req_count: 7
---

# DEPLOY-1.1 — run-map delta

DEPLOY-1 (2026-09-01) predates the 10_ regulatory-execution layer. EXEC-1 (2026-09-01,
A-002) merged REG-POSTURE's phases, MAK-GOV's sprints, REG-NZ's gates and MET-4's P0/P1
into one calendar, RUN-0..4, and EX-5 says every DEPLOY-1 sequence is read against it.
This delta is that reading: one row per DEPLOY-1 step, mapped to its RUN row, carrying
the RUN-0 additions DEPLOY-1 could not know about, an owner role, per-step exit
evidence and failure handling, and the DEC-22 dependency.

## D-1 — step → RUN mapping (DR-1..DR-7)

| DR | DEPLOY-1 step | RUN row (EXEC-1) | Additions the run row carries beyond DEPLOY-1's content | Exit (per EXEC-1) |
|---|---|---|---|---|
| `DR-1` | **0a** MT2 pass over the portfolio (row zero → 100% ledger) | **RUN-0 · parallel track** — EX-5: the pass is *not* rescheduled; it proceeds per MET-4 P0 in parallel with RUN-0, and its W11 sweep MUST include the 10_ layer | none to the pass itself; W11 scope gains 10_ (EX-5); HARDEN-1.1 / HARDEN-3.1 deltas (04_) enumerate the rows and tasks the pass needs | MT2 §7 completion (100% HARDENED or ESCALATED); not a RUN exit |
| `DR-2` | **0b** GATE-000 — Phase 0: `TASK-REG-001..004`; do not configure regulated tooling before this | **RUN-0 · Decide** (weeks 1–4) | `TASK-REG-021` demo-surface triage · `TASK-REG-022` jurisdiction sequence · `TASK-REG-023` Governance Layer classification (REG-POSTURE v1.2) · `T-G01` Governance Layer intended purpose · `T-G05` claims inventory · `NZ-TASK-002/003` sponsor + conflict · `V1-C1/V1-C2` corporate rows (D-4) · `V1-S1` synthetic build **starts week 1** (D-1) · the single counsel packet ×5 + NZ packet (EX-6) | `GATE-000` **and** `SG-V1-0` **and** `NZ-GATE-000` (one counsel packet feeds all three) |
| `DR-3` | **1** GATE-001 — Phase 1: Jira + Ketryx from the Ketryx schema · ISO 14971 risk file · requirements → Essential Principles · substrate decision (`TASK-REG-009` / DEC-03); parallel L1 + Lumos ethics contact | **RUN-1 · Foundation** (weeks 4–12) | `V1-S2` foothold → first revenue (weeks 5–9, D-1) · `TASK-REG-005/006` with the Ketryx ceiling modelled first (`Q-REG-006`) · `TASK-REG-007/008` · `V2-S0` NZ foundation completes · `TASK-REG-024` QMS certification route (v1.2) | `GATE-001` + `SG-V1-2` |
| `DR-4` | **2** GATE-002 — Phase 2 controls `TASK-REG-010..014`; parallel L2 + clinician face/UI v0; REG-KEEP-004 synthetic-only until controls operate | **RUN-2 · Controls & domain** (months 3–9) | `V2-S1` respiratory domain build with the **month-4 checkpoint** (D-3) · study design `V2-E1/E3` · ethics `V2-E2` | `GATE-002` |
| `DR-5` | **3** L3 Honest Uncertainty + Coded Intake; first externally showable prototype; fork evidence | **RUN-2 → RUN-3** boundary — L3 has no gate of its own; its evidence feeds `SG-V2-1` (engine passes its own evaluation gate) and the technical file `V2-S2` | none minted; `V2-S2` technical file begins (months 6–12, overlapped) | L3 exit (Arch §11.2) — no RUN exit |
| `DR-6` | **4** L4 exit; GATE-003 evidence — posture decision under relabelled branches; first checkpoint; limited pilot; Phase-3 evidence `TASK-REG-015..018`; GPP first release if DEC-06 | **RUN-3 · File & notify** (months 6–14) for `V2-S2/S3a/S3b` and `V2-E4`; **RUN-4 · Evidence & submission** (months 12+) for `TASK-REG-015..018` | `V2-S3a` WAND notification at the earliest lawful point after `SG-V2-2` (D-2) · `V2-S3b` first NZ site on commercial readiness · `V2-E4` data collection from first supply · `NZ-ASSUME-004`/`V2-E5` admissibility (asked in RUN-0) | `SG-V2-3a` then `SG-V2-3b`; L4 exit |
| `DR-7` | **5** GATE-004 = first lawful clinical supply — Phase 4: `TASK-REG-019/020` beside L5 | **RUN-4 · Evidence & submission** (months 12+) | NZ evidence carried into the Australian submission (V3.1) | `GATE-004` |

Reading rule: where DEPLOY-1 and a RUN row differ on **timing**, the RUN row governs
(EX-1); where they differ on **content** (what a gate requires), DEPLOY-1's source
(REG-POSTURE §7, Arch §11.2) governs and the RUN row is an extension, not a
contradiction (survey-2 ASSESSMENT-07 §4 sibling check).

## D-2 — owner role per step

| DR | Owner role | Person | Resolves via |
|---|---|---|---|
| DR-1 | MT2 operator | [NEEDS DEFINITION] | DEC-10 (name the operator), DEC-11 (row-zero rule) |
| DR-2 | Founder (programme) — dispatch of counsel packets; regulatory owner — packet content | [NEEDS DEFINITION] | G-09 / REG-POSTURE §12.3 (regulatory owner); DEC-22 (programme calendar) |
| DR-3 | Regulatory owner (Jira/Ketryx, risk file); Architecture owner (DEC-02 registers); Infra + regulatory (DEC-03 substrate) | [NEEDS DEFINITION] | G-09; DEC-02; DEC-03; proposed DEC-23 (infra owner) |
| DR-4 | Security owner (`TASK-REG-010..013`); Operations owner (`TASK-REG-014` usability programme) | [NEEDS DEFINITION] | G-09; proposed DEC-23 |
| DR-5 | Architecture owner (L3 exit adjudication via Observer, Arch §13.7) | [NEEDS DEFINITION] | DEC-08 (Observer cadence) |
| DR-6 | Regulatory + architecture owners (posture decision, GATE-003 evidence); NZ sponsor (`V2-S3a/b`) | [NEEDS DEFINITION] | DEC-01; DEC-19 (NZ sponsor structure); DEC-20 |
| DR-7 | Regulatory owner; Founder | [NEEDS DEFINITION] | G-09; DEC-22 |

Every person-level owner is `[NEEDS DEFINITION]`, consistently with GOV-1 and 00_MANIFEST
§4.4; the resolving decisions are named so the gap travels with the step.

## D-3 — per-step exit evidence and failure handling

| DR | Exit evidence artifact | What halts the step | Where the halt is registered (EX-10) |
|---|---|---|---|
| DR-1 | R29 rows (HARDENED with evidence / ESCALATED with blocker) — 100% of enumerated artifacts; MT2 §7(2) consolidated blocker report | engine tooling failure (MT2 §6); any stop-the-line rule (HARDEN-2) | R29 row (ESCALATED); operator report |
| DR-2 | counsel's written opinion → `ASSUME-REG-001/002/003` ATTESTED or REFUTED with date; `TASK-REG-001` statement; claims inventory (`OBL-014`); packet dispatch receipt | counsel refuses non-device status → `SG-V1-0` fails (V1 collapses into V2 — REG-SPRINT "what would make this plan wrong"); this MUST NOT stall `GATE-000` (REG-POSTURE v1.2 §7) | R30 rows for `GATE-000`, `SG-V1-0`, `NZ-GATE-000`; MET-2.1 for DEC closures |
| DR-3 | Ketryx/Jira configured per `KTX-*` with verification evidence; risk file `TASK-REG-007` opened; DEC-03 ruling recorded; L1 exit evidence (Arch §11.2) | ceiling model shows free tier insufficient before `V1-S2` (`Q-REG-006`) → HALT-TYPED, re-plan tier; DEC-03 unruled → `TASK-REG-009` waits, L1 proceeds (no substrate dependency at L1) | R30 `GATE-001`, `SG-V1-2`; DEC-03 in MET-2 |
| DR-4 | controls operating with evidence per `TASK-REG-010..014`; month-4 checkpoint record (D-3) confirming or reversing `SD-02` | month-4 analytics contradict respiratory → `SD-02` reversal (low cost at month 4, high at month 7 — D-3) | R30 `GATE-002`; MET-2.1 DEC-18 |
| DR-5 | L3 exit evidence (coverage within tolerance external + internal; abstention baseline; graph determinism) → R19 fork evidence | any L3 exit criterion fails → level not exited; no RUN penalty (no RUN gate here) | R25 property runs; R19 |
| DR-6 | technical file producible on demand (`SG-V2-2`); WAND notification record (`V2-S3a`); first-site agreement (`V2-S3b`); `TASK-REG-015..018` evidence | `SG-V2-2` not passed → `V2-S3a` MUST NOT proceed (notifying without a producible file converts the NZ position into an ARTG liability — D-2); `NZ-ASSUME-005` closes badly → `V2-S3a` loses urgency, RUN-3 re-weights to `V2-S3b` (EX-7, pre-registered) | R30 `SG-V2-2/3a/3b`, `NZ-GATE-001/002` |
| DR-7 | conformity assessment certificate; ARTG inclusion (`TASK-REG-020`) | route undecided (`Q-REG-005` / `ASSUME-REG-005`) → HALT-TYPED at Phase 4 entry | R30 `GATE-004` |

## D-4 — the DEC-22 dependency

This delta is **in force as the working calendar when DEC-22 closes** (MET-2.1: "Open —
adopting v1.2 as working set closes it"). Until then DEPLOY-1's own sequence remains the
only *ratified* sequence and this file is the drafted mapping. No row above presumes
DEC-22 closed; DR-1's statement that the pass is not rescheduled holds under either
reading (EX-5 and MET-4 P0 agree).

## Census and self-audit (run 2026-09-05)

- Census: DR-1..DR-7 = 7 = `req_count` = DEPLOY-1 steps 0a, 0b, 1, 2, 3, 4, 5 (7) — each appears exactly once in D-1.
- Every RUN row's contents are in a DEPLOY-1 step or listed as an addition: RUN-0 (DR-2 + DR-1 parallel) · RUN-1 (DR-3) · RUN-2 (DR-4, DR-5) · RUN-3 (DR-6) · RUN-4 (DR-6, DR-7) — PASS.
- Every cited ID resolves in the tree (grep, both ends): GATE-000..004, SG-V1-0/2, SG-V2-1/2/3a/3b, NZ-GATE-000..002, TASK-REG-001..024, T-G01/T-G05, NZ-TASK-002/003, V1-C1/C2, V1-S1/S2, V2-S0/S1/S2/S3a/S3b, V2-E1..E5, NZ-ASSUME-004/005, ASSUME-REG-001..003/005, Q-REG-005/006, KTX-*, SD-02, DEC-01/02/03/08/10/11/18/19/20/22, EX-1/2/5/6/7/10, R19/R25/R29/R30 — PASS (recorded in `11_prompts/runs/2026-09-05_sprint-1/refcheck_output.txt`).
- DEPLOY-1 v1.0 byte-identical: sha256 unchanged against `CHECKSUMS_BEFORE.txt` — PASS.
- No ASSUME closed; DEC-07 patient surface stays Blocked in DR-2 — PASS.
