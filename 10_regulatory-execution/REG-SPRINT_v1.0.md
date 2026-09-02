---
doc_id: REG-SPRINT
title: "Mākoha — Three-Version Sprint Plan"
version: 1.0
status: DRAFT
authority: ADVISORY_ONLY
entity: Arepo Medtech Pty Ltd
date_issued: 2026-09-01
companion_to: [REG-POSTURE v1.1, REG-NZ v1.0, MAK-GOV v0.9]
id_prefixes: [V1, V2, V3, SG, SD]
---

# Mākoha — Three-Version Sprint Plan

**Design principle:** speed comes from narrowing *scope*, never from thinning
*rigour*. Each version is a real product with real revenue, and each is a strict
subset of the next — so nothing built is discarded and evidence accumulates on one
continuous device history rather than three.

**The three clocks:**

| Clock | Pressure |
|---|---|
| NZ Medical Products Bill | Closes the notification-only window for SaMD and AI. Timing unpublished |
| Capital | Wholesale round follows friends-and-family; needs demonstrated traction |
| ARTG | 18–24 months from `GATE-000` on the current plan |

V1 answers the capital clock. V2 answers the NZ clock. V3 answers the ARTG clock.
They run overlapped, not sequentially.

---

## Version 1 — Governance Layer (non-device)

**Target: revenue and a named site inside 12 weeks. No notification, no technical file
gate, no device liability.**

### V1.1 Use case — recommendation

Three candidates were considered. Recommending the first.

**A. Pharmacist scope-expansion decision governance** ← recommended

Pharmacist prescribing under expanded scope is new, expanding, politically watched,
and structurally under-governed. Pharmacies now make prescribing decisions they were
not previously making, with no established apparatus for demonstrating those decisions
were justified against protocol. The buyer feels the exposure before you explain it.

- Buyer: pharmacy groups, and eventually the boards and insurers behind them
- Pain: "prove your prescribing decisions were protocol-consistent" has no current answer
- Fit: it is your wedge, already, in the market you already targeted
- Data: prescribing decisions plus protocol — narrow, structured, tractable
- Bonus: the guideline-gap analytics feed V2's clinical scope selection directly

**B. GP practice deviation review.** Larger market, but crowded with accreditation
tooling and a diffuse pain. Slower sale.

**C. After-hours / locum decision consistency.** Sharp pain, small market, hard to reach.

**Decision `SD-01`:** ratify use case A, or substitute. Blocks everything in V1.

### V1.2 Scope

In: retrospective conformance review of documented decisions against ratified
protocols; deviation classification with reasoned-deviation states; queue and owner
workflow; versioned projection with exported flattening; regulator-grade bundles;
guideline-gap analytics.

Out, structurally: any patient-specific output to a clinician; any real-time flagging;
any prospective scoring; the differential engine, conformal wrapper and runtime LLM —
absent from the artifact and dependency graph, proven in the release suite.

### V1.3 Sprints

| ID | Sprint | Weeks | Exit |
|---|---|---|---|
| `V1-S0` | Classification. Intended purpose statement; non-device counsel question bundled into `TASK-REG-002`; boundary spec B-1..B-4; latency floor ratified; claims inventory v0 | 1–4 | `SG-V1-0`: counsel attests non-device |
| `V1-S1` | Build. Read model over synthetic pharmacy data; review workflow; projection layer; conformance suite as CI gate | 4–8 | `SG-V1-1`: suite green, structural absence proven |
| `V1-S2` | Foothold. Named design-partner pharmacy group; data agreement and privacy assessment; bundles from real data; reconstruction exercise; pricing | 8–12 | `SG-V1-2`: one committed site, real bundles |

**`SG-V1-0` is blocking.** Nothing ships before counsel attests non-device status.

### V1.4 What V1 buys V2

A named site. Real decision data. A live relationship with a buyer who has already
paid. Guideline-gap analytics that tell you which clinical domain V2 should cover. And
a demonstrated post-market discipline — queues, owners, ageing alarms, governed
verdicts — which is a large part of what `GATE-002` asks for anyway.

---

## Version 2 — Minimum Deployable Device (NZ-first)

**Target: lawful supply of the classified device in New Zealand, roughly 12 months
ahead of where ARTG inclusion would permit it.**

### V2.1 The speed lever is clinical scope, not architecture

The release path stays deterministic. The evidence chain stays visible. The technical
file is complete. What shrinks is **how many conditions the device covers**.

A device covering one clinical domain needs one domain's differential library, one
domain's validation, one domain's usability analysis, one domain's risk file. That is
a fraction of the full-product burden and it is the same device, narrowed — so V3 is
a scope expansion under change control, not a new device.

**Decision `SD-02`:** name the V2 clinical domain. Criteria: high prevalence in the
pharmacy wedge, tractable differential, published instruments available for the
reviewable-basis argument, and low catastrophic-miss density. V1's guideline-gap
analytics inform this; do not decide it before that data exists.

### V2.2 Scope

In: one clinical domain; deterministic release path; full evidence chain per output;
clinician face only; human sign-off, fail-closed; complete technical file to `STD-001`
through `013`; post-market system operating before supply.

Out: additional domains; the patient face (blocked on DEC-07 regardless); ML at
runtime — that is V3's fork, not V2's.

### V2.3 Sprints

| ID | Sprint | Timing | Exit |
|---|---|---|---|
| `V2-S0` | NZ foundation. NZ counsel; sponsor structure decided; registrar/director conflict declared and cleared; Bill-timing model | months 0–3, parallel with V1 | `SG-V2-0`: `NZ-GATE-0` |
| `V2-S1` | Domain build. One-domain differential library; deterministic engine; clinician face; ISO 14971 risk file for that scope | months 3–9 | `SG-V2-1`: engine passes its own evaluation gate |
| `V2-S2` | Technical file. 13485 QMS operating; 62304 lifecycle records; 62366-1 usability for the clinician face; SBOM; vulnerability handling; independent penetration test | months 6–12, overlapped | `SG-V2-2`: file producible on demand |
| `V2-S3` | Supply. Post-market system live *before* notification; WAND notification; first NZ site | months 12–14 | `SG-V2-3`: lawful supply |

**`SG-V2-2` gates `SG-V2-3` absolutely.** New Zealand does not review the file before
supply, but Medsafe can demand it at any time and shares safety information with the
TGA. Supplying without a complete file is the one shortcut that converts the NZ
advantage into an ARTG liability.

### V2.4 The evidence study — design it before launch, not after

This is where the NZ window actually pays. Prospective, ethics-approved,
pre-registered, running from first supply, measuring the same intended purpose the
Australian submission will claim.

| ID | Task | Timing |
|---|---|---|
| `V2-E1` | Study design and pre-registration | months 6–9, before supply |
| `V2-E2` | NZ ethics approval | months 9–12 |
| `V2-E3` | Māori data sovereignty and Te Tiriti obligations addressed in the design | months 6–12 |
| `V2-E4` | Data collection from first supply | month 14 onward |
| `V2-E5` | Confirm with AU counsel that NZ evidence is admissible to conformity assessment, and on what conditions (`NZ-ASSUME-004`) | month 0–3 — **ask early, it may change the design** |

Incidental data from a fast launch is telemetry. Pre-registered prospective data from
the same device is evidence. The difference is a study protocol written before you
ship.

---

## Version 3 — Full Product (ARTG)

**Target: ARTG inclusion, full clinical scope, all faces.**

### V3.1 What changes from V2

Scope expansion across clinical domains, under change control on one device history.
The `FORK-REG-001` decision at L4 — deterministic runtime or ML at runtime — which
V2 deliberately does not pre-empt. The patient face, if DEC-07 permits. Conformity
assessment and ARTG inclusion. And the NZ evidence from `V2-E4`, carried into the
Australian submission.

### V3.2 Sequence

Runs on the REG-POSTURE v1.1 plan unchanged: `GATE-000` through `GATE-004`,
`TASK-REG-001` through `022`. V2 discharges much of Phase 1 and Phase 2 as a side
effect, because the technical file and the QMS are the same artefacts.

`GATE-003` is where NZ pays: clinical evidence exists, prospectively collected, on the
same device.

---

## Parallelism map

| Months | V1 | V2 | V3 |
|---|---|---|---|
| 0–3 | S0 classification, S1 build | S0 NZ foundation; `V2-E5` early question | `GATE-000` counsel — one engagement covers all three |
| 3–6 | S2 foothold → **revenue** | S1 domain build | Phase 1 tooling |
| 6–12 | operating; gap analytics feeding `SD-02` | S2 technical file; `V2-E1/E2/E3` | Phase 2 controls |
| 12–18 | expanding sites | S3 **NZ supply**; evidence collection begins | Phase 3 |
| 18+ | — | evidence accumulating | `GATE-004` submission |

**One counsel engagement, four questions:** Mākoha classification, exemption
confirmation, Governance Layer non-device status, and NZ evidence admissibility. Same
lead time, four answers. This is the single highest-leverage scheduling decision in
the plan.

---

## Decisions

| ID | Decision | Owner | Blocks |
|---|---|---|---|
| `SD-01` | V1 use case — pharmacist scope governance, or substitute | Founder + advisor | All V1 |
| `SD-02` | V2 clinical domain | Clinical + regulatory | `V2-S1` |
| `SD-03` | NZ sponsor structure — NZ entity vs contracted | Founder + counsel | `V2-S0` |
| `SD-04` | Whether V2 supplies Australia at all before ARTG, or NZ-only | Founder + counsel | `V2-S3` |
| `SD-05` | Governance Layer namespace and repository split | Architecture owner | `V1-S1` |

---

## What would make this plan wrong

Stated so it can be tested rather than assumed.

- **If NZ evidence is inadmissible to conformity assessment** (`NZ-ASSUME-004` closes
  badly), V2 is a revenue strategy, not an evidence strategy. Still worth doing;
  argue it differently, and reweight toward V1 expansion.
- **If the Medical Products Bill lands without transition provisions**, early
  notification buys less and V2's urgency drops relative to V1's.
- **If counsel refuses non-device status for the Governance Layer**, V1 collapses into
  V2 and the twelve-week foothold is lost. This is the largest single risk in the plan
  and it resolves at `SG-V1-0`, four weeks in — cheap to learn.
- **If the V1 use case doesn't sell**, the problem is commercial, not regulatory, and
  V2's timeline is unaffected.

---

*Advisory only. Every regulatory assertion here is carried in REG-POSTURE v1.1 or
REG-NZ v1.0 as an assumption requiring counsel attestation.*
