---
doc_id: EXEC-1
title: "EXEC-1 — Regulatory Execution Directive: precedence, run alignment, and the P0 queue"
version: 1.0
date: "2026-09-01"
status: "Added (Imago v1.2). Normative for sequencing and precedence; regulatory content within the documents it sequences remains ADVISORY_ONLY per those documents' own authority lines."
normative_language: RFC-2119 (MUST / SHOULD / MAY)
req_prefix: EX
req_count: 10
governs: "10_regulatory-execution/ — REG-POSTURE v1.1, REG-NZ v1.0, MAK-GOV v0.9, REG-SPRINT v1.0 + REG-SPRINT-1.1 delta"
subordinate_to:
  - "MANIFEST precedence law (03_ corpus MANIFEST governs its fifteen volumes; nothing here edits any corpus volume)"
  - "MAK-ANT AN-1..12 (the sensing duties; this directive schedules the fold, it does not substitute for it)"
  - "XC-1 classification honesty (no run in this directive ships classified work under any other label)"
---

# EXEC-1 — Regulatory Execution Directive

The 10_ layer exists because four instruments landed after Imago v1.1 sealed:
the amended posture (v1.1), the New Zealand brief, the Governance Layer addendum,
and the three-version sprint plan with its delta. This directive does three things:
gives that layer a precedence position inside the ecosystem, aligns its runs to the
phase structures that already exist, and states the P0 queue so an operator can
start today without archaeology.

Nothing in 00_–09_ is edited. Integration is by delta files (MET-2.1, R30.1),
manifest amendment (A-002), and the fold worklist (FOLD-1).

---

## Part 1 — Precedence

### EX-1 (MUST)
**Statement:** For **sequencing and scheduling**, the 10_ layer takes precedence over
every earlier phase plan in this repository: where REG-SPRINT v1.0 + the v1.1 delta
orders work differently from MET-4's roadmap, a volume's phasing table, or
DEPLOY-1's sequencing, REG-SPRINT's ordering governs. For **content and authority**,
nothing changes: corpus volumes remain normative for architecture, REG-POSTURE
remains advisory for regulation, and no ASSUME closes by anything in this directive.
**Rationale trace:** the sprint plan is the only artifact that prices all three
clocks (Bill, capital, ARTG); precedence-of-sequence without precedence-of-content
keeps XC-1 intact.

### EX-2 (MUST)
**Statement:** REG-SPRINT v1.0 is read **only through** REG-SPRINT-1.1. The delta's
five amendments (D-1..D-5) are in force: V1 build decoupled from counsel; WAND
notification split from first supply with `NZ-Q-004` added; `SD-02` provisionally
resolved to respiratory with a month-4 checkpoint; corporate rows `V1-C1`/`V1-C2`;
register homes per D-5. Citing v1.0 timing that the delta amends is a conformance
violation.
**Rationale trace:** MET-1/MET-1.1 delta-reading pattern, applied identically.

### EX-3 (MUST)
**Statement:** The standalone REG-POSTURE_v1.1.md in 10_ is now the **canonical**
posture file. The MAK-ANT Annex 1 copy (v1.0) is a known, deliberate divergence
until the FOLD-1 worklist executes. Until the fold: cite v1.1 IDs from the
standalone; cite nothing that exists only in the v1.0 annex; the divergence is
listed, dated, and owned — not silent.
**Rationale trace:** MAK-ANT annex banner ("standalone file is canonical; annex
mirrors it"); AN-2 flag-and-route satisfied by this clause plus FOLD-1.

### EX-4 (MUST)
**Statement:** J-3 disposition pending. MAK-J3 remains folded and unedited; its
retirement is argued in conversation record and REG-POSTURE v1.1 §2.1/§3.1 but is
**not decided** — it is DEC-06's call, now framed as a retirement ratification with
MAK-GOV named as the replacement non-classified route. No document in this
repository may treat J-3 as retired until DEC-06 closes.
**Rationale trace:** append-only law; decisions close by their owners, not by drafts.

---

## Part 2 — Run alignment

The ecosystem now has one merged execution calendar. Names map as follows; where a
row shows two names, they are the same work and MUST NOT be duplicated.

### The runs

| Run | Contents | Source phases merged | Exit |
|---|---|---|---|
| **RUN-0 · Decide** (weeks 1–4) | The single counsel engagement (five questions, EX-6) · intended purpose statements ×2 (Mākoha `TASK-REG-001`; Governance Layer `T-G01`) · claims inventories (`TASK-REG-003`/`OBL-014`; `T-G05`) · demo-surface triage `TASK-REG-021` · jurisdiction sequence `TASK-REG-022` · NZ sponsor + conflict (`NZ-TASK-002/003`) · corporate `V1-C1`/`V1-C2` · **parallel:** `V1-S1` build on synthetic (D-1) · MT2 row zero + pass start (unchanged from MET-4 P0) | REG-POSTURE Phase 0 = MAK-GOV Sprint G0 = REG-NZ `NZ-GATE-0` prep = MET-4 "P0 now, parallel" | `GATE-000` **and** `SG-V1-0` **and** `NZ-GATE-0` — one counsel packet feeds all three |
| **RUN-1 · Foundation** (weeks 4–12) | `V1-S2` foothold → first revenue (weeks 5–9, D-1) · Jira/Ketryx per `TASK-REG-005/006` with the ceiling modelled first · risk file `TASK-REG-007` · requirements `TASK-REG-008` · DEC-03 ruling then `TASK-REG-009` · `V2-S0` NZ foundation completes | REG-POSTURE Phase 1 = MAK-GOV G1+G2 = MET-4 P1 | `GATE-001` + `SG-V1-2` |
| **RUN-2 · Controls & domain** (months 3–9) | `V2-S1` respiratory domain build (D-3; **month-4 checkpoint** against V1 gap analytics) · Phase 2 controls `TASK-REG-010..014` · study design `V2-E1/E3` · ethics `V2-E2` | REG-POSTURE Phase 2 = REG-SPRINT V2-S1 | `GATE-002` |
| **RUN-3 · File & notify** (months 6–14) | `V2-S2` technical file · `V2-S3a` WAND notification at earliest lawful point after `SG-V2-2` (D-2) · `V2-S3b` first NZ site on commercial readiness · evidence collection `V2-E4` from first supply | REG-NZ `NZ-GATE-1/2` = REG-SPRINT V2-S2/S3 | `SG-V2-3a` then `SG-V2-3b` |
| **RUN-4 · Evidence & submission** (months 12+) | Phase 3 `TASK-REG-015..018` with NZ evidence accruing · Phase 4 `TASK-REG-019/020` | REG-POSTURE Phases 3–4 = REG-SPRINT V3 | `GATE-004` |

### EX-5 (MUST)
**Statement:** Every volume phasing table, HARDEN-3 wave note, and DEPLOY-1 sequence
is read against this run map. Where a pre-existing phase name appears, it resolves
to its RUN row above. The hardening pass (MT2/HARDEN-3, W0–W11) is **not**
rescheduled by this directive — it proceeds per MET-4 P0 in parallel with RUN-0 —
but its W11 cross-portfolio sweep MUST include the 10_ layer in scope.
**Rationale trace:** one calendar; no duplicated work; MT2 §7(3) sweep completeness.

---

## Part 3 — The P0 queue (start today)

### EX-6 (MUST) — the counsel packet
**Statement:** One Australian engagement, five questions, dispatched as the first
external act of RUN-0; NZ counsel engaged in the same week as a second, smaller
packet. The Australian five:
1. Mākoha device classification and rule (`ASSUME-REG-001` / `Q-REG-001`)
2. Exemption unavailability confirmation (`ASSUME-REG-002` / `Q-REG-002`) — attach REG-POSTURE §1–§3
3. Governance Layer non-device status, including the accessory question (`ASSUME-REG-009` / `Q-REG-010`) — attach MAK-GOV §2
4. Patient-surface treatment (`ASSUME-REG-003` / `Q-REG-003` / DEC-07)
5. NZ evidence admissibility to Australian conformity assessment (`NZ-ASSUME-004` / `V2-E5`)

The NZ packet: `NZ-ASSUME-001..003` plus `NZ-Q-004` (earliest lawful notification;
obligations on a notified-but-unsupplied device; whether transition regimes key on
notification or supply).
**Rationale trace:** AN-10 packet duty; the delta's finding that question 5 shapes
the V2 study design and `NZ-Q-004` carries the working assumption.

### EX-7 (MUST) — the working assumption is registered, not silent
**Statement:** The programme currently operates on the stated working assumption
that the Medical Products Bill will carry transition provisions for
already-notified devices. This is recorded as an OPEN assumption (`NZ-ASSUME-005`,
minted in R30.1), owner: founder; closure: `NZ-Q-004` answer or Bill text; and every
schedule consequence that depends on it (`V2-S3a` pull-forward) names it. If it
closes badly, `V2-S3a` loses its urgency ranking and RUN-3 re-weights toward
`V2-S3b` commercial readiness — pre-registered here so the re-plan is a lookup, not
a debate.
**Rationale trace:** ASSUME discipline (AN-3); decisions-on-evidence doctrine.

### EX-8 (MUST) — the week-one board
**Statement:** These start within five working days of adopting this directive, in
parallel, no dependencies among them: counsel packets out (EX-6) · `TASK-REG-001` +
`T-G01` drafting begins · `V1-S1` synthetic build begins (D-1) · `TASK-REG-021` demo
triage · `V1-C1` R&D-window question to the specialist · `NZ-TASK-003` conflict
declaration drafted · MT2 row zero per MET-4 P0.
**Rationale trace:** RUN-0 contents; "move now" priced without thinning any gate.

### EX-9 (SHOULD) — audience track
**Statement:** The zero-regulatory-cost public track (clinical epistemology,
diagnostic reasoning, governance-infrastructure thesis, under the founder's name,
no product claims) runs from week 1, subject to `NDG-9`/`OBL-014` claims discipline
and reviewed against the claims inventory once `TASK-REG-001` lands.
**Rationale trace:** advisor sequencing (coverage precedes capital) made compatible
with `OBL-003`.

### EX-10 (MUST) — evidence of execution
**Statement:** Every RUN exit, SG gate, and SD/DEC closure lands as a register row
(R30 per D-5; MET-2.1 for decisions) with an evidence artifact named. A run exit
asserted without its row is not passed. The AX-4 gate-bundle definitions extend to
`SG-V1-*`, `SG-V2-*`, and `NZ-GATE-*`.
**Rationale trace:** REG-POSTURE §0.4 DONE-WITH-EVIDENCE; MAK-ABC AX-4; house law.

---

## Part 4 — Integration ledger (what v1.2 adds, where)

| Artifact | Location | Type |
|---|---|---|
| REG-POSTURE_v1.1.md | 10_ | Canonical posture (EX-3) |
| REG-NZ_v1.0.md | 10_ | New jurisdiction brief |
| MAK-GOV_addendum-g_v0.9.md | 10_ | Non-device build target (proposed; DEC-G2) |
| REG-SPRINT_v1.0.md + REG-SPRINT-1.1_delta.md | 10_ | The run plan (EX-2 reading rule) |
| EXEC-1 (this file) | 10_ | Precedence + runs + P0 |
| FOLD-1_antennae_fold_worklist.md | 10_ | The AN-5/AN-6 fold instructions for MAK-ANT v1.1 |
| MET-2.1_decision_register_delta.md | 01_ | New DEC/SD/conflict rows, additive |
| REG-R30.1_seed_delta.md | 05_ | New register rows for v1.1/NZ/GOV/SPRINT IDs |
| 00_MANIFEST.md §8 Amendment A-002 | 00_ | Appended per the A-001 pattern |

Untouched, verified by checksum at seal: all 170 pre-existing files, including every
corpus volume, every annex, and MAK-J3.

---

## Part 5 — Self-audit (run at seal)

1. EX census: 10 requirements, 8 MUST + 1 SHOULD + 1 MAY? — **correction: 9 MUST + 1 SHOULD; no MAY.** Census: EX-1..8, EX-10 MUST; EX-9 SHOULD.
2. Every RUN row names its source phases and its exit gate — PASS.
3. Every P0 item carries an existing ID from the 10_ documents — PASS.
4. No corpus volume edited — verified by checksum ledger in A-002.
5. No ASSUME closed by this directive — PASS (EX-7 mints one OPEN; closes none).
6. Delta-reading rule stated for every superseded timing — PASS (EX-2).
7. Canonical-vs-annex divergence is dated and owned — PASS (EX-3, FOLD-1).
8. J-3 status untouched pending DEC-06 — PASS (EX-4).
