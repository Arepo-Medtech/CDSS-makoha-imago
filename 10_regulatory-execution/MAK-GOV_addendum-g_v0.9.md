---
doc_id: MAK-GOV
title: "Addendum G — The Governance Layer: a non-device first artifact"
version: "0.9-proposed"
date: "2026-09-01"
series: "Mākoha regulatory fork — non-device branch"
status: proposed-normative-draft
authority: ADVISORY_ONLY (regulatory content); PROPOSED-NORMATIVE (build target)
normative_language: RFC-2119 (MUST / SHOULD / MAY)
req_prefix: NDG
req_count: 14
entity: Arepo Medtech Pty Ltd
naming_note: >
  "Addendum G" and doc_id MAK-GOV are provisional. The J-series denotes regulatory
  fork branches; this is a fork branch but not a J-1/J-2 alternative, and J-3 is
  under retirement. Namespace is an open decision — see DEC-G1.
realizes: "MAK-ABC Part 6 (AX-1..4) shipped as an independently releasable artifact"
subordinate_to:
  - "MAK-FFC XC-1 (classification honesty) — this artifact never does classified work under a non-device label"
  - "MAK-ABC anti-requirements — all seven carry unmodified and become the classification argument"
  - "REG-POSTURE v1.1 — regulatory content governed by the posture's §0 conventions"
depends_on:
  - "MAK-ABC v1.0 (The Abdomen Corpus) — the auditor face"
  - "MAK-FFC v1.1 AF-1..AF-8"
  - "REG-POSTURE v1.1"
supersedes_role_of: "MAK-J3 (as the non-classified revenue and entry route), pending DEC-06 retirement"
attestation_required: true
attestation_by: Australian regulatory counsel (non-device status)
---

# Addendum G — The Governance Layer

**A non-device first artifact: the auditor face shipped independently, analysing
organisational conformance rather than patient state, with no clinical write path and
no patient-specific recommendation — sold as clinical governance infrastructure while
the classified track proceeds.**

---

## 1 — Why this exists

Three pressures converge on the same answer.

**Regulatory.** `REG-FIND-001` closed the exemption. The exempt-tier reserve (J-3) is
under retirement because Rule 11 has no carve-out, its evidence-accumulation rationale
does not survive the intended-purpose test, and it costs a second device for a
schedule hedge. What remains unanswered is how anything ships before `GATE-004`.

**Commercial.** Health-science investors carry a live objection that Australian
companies take a decade from inception to scale. Mākoha's classified path is not a
decade, but it is not months either. A non-device line answers the objection with
revenue rather than argument.

**Positional.** The market is rotating into healthcare for defensive earnings with no
AI-disruption exposure. A governance layer is the thing organisations buy *because* AI
is arriving. That is the trend, not the thing being rotated away from.

**The thing that makes this available at all:** the auditor face is already specified
as architecturally incapable of being decision support. MAK-ABC AL-1 makes it a read
model with no write path into clinical or knowledge-plane content. AF-8 makes review
retrospective, never real-time individual surveillance. AF-4 and AT-2 forbid any
detector output reaching sanction without a governed human step. Those were written as
integrity constraints. They are also, read together, a non-device argument.

This addendum does not build a new product. It ships an existing one separately.

---

## 2 — The classification argument

### 2.1 The test

Under s41BD of the Therapeutic Goods Act 1989, a product is a medical device if
intended for diagnosis, monitoring, prediction, prognosis, treatment, alleviation or
prevention of disease in persons — or is an accessory to a medical device.

### 2.2 The argument

**The subject of analysis is the organisation, not the patient.** The Governance Layer
analyses whether documented clinical decisions were justified against ratified
guidelines, whether deviations were reasoned, whether queues are owned, whether
instruments have gone stale. Its outputs describe *practice quality*. They do not
describe a patient's condition, do not predict a patient's course, and are not
returned to anyone making a decision about that patient's care.

**It is retrospective by construction.** AF-8 prohibits real-time individual
surveillance. The temporal separation is not a policy setting; it is a face law. A
retrospective conformance review cannot inform the decision it reviews.

**It has no clinical write path.** AL-1. Nothing the Governance Layer produces enters
a clinical record, a care plan, or a clinician's decision surface.

**Its closest regulatory analogue is favourable.** TGA's own worked example of a tool
that is *not* a medical device is a management-plan tool that extracts from the record
without analysing it for a medical purpose. The guidance is explicit that recording or
extracting does not make a tool a device — but that analysing information *for a
medical purpose* does. The Governance Layer's purpose is administrative and quality
assurance. That is the line it must stay on.

### 2.3 Where the argument fails — the four boundaries

These are the failure modes, stated so they can be enforced in code rather than
policy. Each is an `NDG` requirement below.

| # | Failure mode | Why it breaks non-device status |
|---|---|---|
| B-1 | Patient-specific output reaching a clinician | Becomes information contributing to that patient's care |
| B-2 | Real-time or near-real-time flagging | Collapses the retrospective separation; approaches monitoring |
| B-3 | Prospective risk scoring of patients or cohorts | Prediction is named in s41BD |
| B-4 | Accessory coupling to the classified engine | An accessory to a medical device is itself regulated |

B-4 is the subtle one and the reason this ships as a **separate artifact with a
separate intended purpose statement**, not as a module of Mākoha. If the Governance
Layer's function is to audit Mākoha's outputs, it is plausibly an accessory. If its
function is to audit *clinical practice* — of which Mākoha-assisted decisions may
later be a subset — it is not. The first customers must therefore be practices with no
Mākoha deployment at all. That is a commercial constraint imposed by a regulatory
argument, and it is not negotiable.

### 2.4 Honest confidence

Moderate, not high. The argument is well-founded but it is an argument, not a
precedent. Two things make it stronger than the exemption argument that failed: there
is no probability output, and there is no patient-level recommendation of any kind.
Two things keep it short of certain: "analysing information for a medical purpose" is
interpretively broad, and a governance tool that reads clinical records to assess
decision quality is at least arguably doing so.

Carried as `ASSUME-REG-009`. **This ships nothing before counsel attests.**

---

## 3 — Requirements (NDG)

### NDG-1 (MUST)
**Statement:** The Governance Layer is a separate build artifact with its own intended
purpose statement, its own claims inventory, and its own repository. It shares spine
components by versioned dependency; it is never a configuration of the classified
build.
**Rationale trace:** B-4; MAK-J3 GPP-8 pattern (structural absence, not flags).

### NDG-2 (MUST)
**Statement:** No output is patient-specific at the point of delivery. Findings are
delivered at cohort, clinician, service or organisation grain. Where a finding
necessarily references an individual encounter, it is delivered only into the governed
review queue (AR-1) and never to a clinician acting on that patient.
**Rationale trace:** B-1; MAK-ABC AL-1, AF-8.

### NDG-3 (MUST)
**Statement:** A minimum latency floor is enforced in code between an encounter and
its availability for conformance review. The floor is a build constant, not a
configuration value, and its value is a ratified decision recorded in the register.
**Rationale trace:** B-2; AF-8 retrospective-only; enforcement-in-code doctrine.

### NDG-4 (MUST)
**Statement:** No prospective scoring. The artifact contains no forward-looking risk
model over patients or cohorts. Trend and drift analytics describe what has happened;
they never project what will.
**Rationale trace:** B-3; s41BD "prediction"; MAK-ABC AT-1 (telemetry never
auto-triggers).

### NDG-5 (MUST)
**Statement:** The differential engine, conformal wrapper, runtime LLM and any
probability-bearing clinical inference are **structurally absent** from the artifact
and its dependency graph — absent, not disabled. Absence is proven in the release
suite.
**Rationale trace:** MAK-J3 GPP-8 pattern, carried; B-3; B-4.

### NDG-6 (MUST)
**Statement:** Crossing any boundary in §2.3 creates a new product with a new
classification analysis. It is never a release, a feature flag, or a channel upgrade.
Any change request that would cross a boundary halts.
**Rationale trace:** MAK-J3 GPP-14 pattern, carried; XC-1 honesty posture.

### NDG-7 (MUST)
**Statement:** All seven MAK-ABC anti-requirements carry unmodified and are release
gates, not aspirations: no clinical write path; no automatic sanction or clinician
flagging; no real-time individual surveillance; conflicts project as conflicts; no
flattened state exported without its versioned mapping; no queue ageing without an
owner; no signal rendered as confidence.
**Rationale trace:** MAK-ABC anti-requirements; AE-4 conformance suite.

### NDG-8 (MUST)
**Statement:** Every projection ships its flattening (AX-2, carried): the versioned,
ratified mapping from fabric states to any external vocabulary accompanies its
outputs, so a reviewer audits the mapping rather than trusting its results.
**Rationale trace:** MAK-ABC AX-2.

### NDG-9 (MUST)
**Statement:** Claims discipline. Marketing, positioning and in-product copy describe
clinical governance and quality assurance. The artifact is never described as
providing clinical decision support, diagnostic assistance, or patient risk
assessment. The claims inventory is versioned and diffed against the intended purpose
statement every release.
**Rationale trace:** `OBL-003`, `OBL-014`; MAK-ANT AN-9; the advertising rules bind
regardless of device status.

### NDG-10 (MUST)
**Statement:** Privacy obligations attach regardless of device status. Australian
Privacy Principles, the Notifiable Data Breach scheme, state health-record
requirements, and any practice-level data agreement apply in full. Non-device is not
non-regulated.
**Rationale trace:** `OBL-011`; Privacy Act 1988.

### NDG-11 (MUST)
**Statement:** First deployments are to organisations with no Mākoha classified
deployment. The customer list is itself an accessory-status control until counsel
rules otherwise.
**Rationale trace:** B-4; §2.3.

### NDG-12 (SHOULD)
**Statement:** Evidence posture. Deployment generates conformance, deviation and
guideline-gap evidence about *practice*. This is commercially and scientifically
valuable and may inform guideline work. It is **not** clinical validation evidence for
the classified device — different intended purpose, different claim. Any programme
document asserting otherwise is in error.
**Rationale trace:** the intended-purpose transfer rule that retired J-3's evidence
rationale; `REG-FIND-010` sibling reasoning.

### NDG-13 (SHOULD)
**Statement:** Commercial shape follows the sector's language: recurring subscription
revenue, per-site or per-clinician, positioned inside the regulated care environment.
**Rationale trace:** investor-facing framing; sector comparables.

### NDG-14 (MAY)
**Statement:** Where a customer later deploys the classified device, the Governance
Layer's relationship to it is re-analysed before any coupling — including whether
auditing Mākoha-assisted decisions triggers accessory status. Until that analysis, the
two run unlinked at that customer.
**Rationale trace:** B-4; NDG-11.

---

## 4 — Sprint plan (Phase G, weeks 1–12)

Runs **in parallel with** REG-POSTURE Phase 0. It does not consume `GATE-000`
capacity except for the counsel question, which is bundled into `TASK-REG-002`.

### Sprint G0 — Classification (weeks 1–4). Blocking.

| ID | Task | Output |
|---|---|---|
| `T-G01` | Write the Governance Layer intended purpose statement. Separate document from Mākoha's. State the subject of analysis as organisational conformance in the first sentence. | Intended purpose statement |
| `T-G02` | Add non-device status to the `TASK-REG-002` counsel brief (`ASSUME-REG-009`, `Q-REG-010`). Ask specifically about the accessory question and about "analysing for a medical purpose". | Counsel question set |
| `T-G03` | Boundary specification: B-1..B-4 written as testable assertions with named enforcement points. | Boundary spec |
| `T-G04` | Ratify the NDG-3 latency floor value. | Register decision |
| `T-G05` | Claims inventory v0 for the Governance Layer (`NDG-9`). | Claims inventory |

**`GATE-G0`:** counsel attests non-device status. Nothing below proceeds first.

### Sprint G1 — Foundation (weeks 4–8)

| ID | Task | Output |
|---|---|---|
| `T-G06` | Stand up `cdss-governance` as a releasable repository, not a register home. Namespace prefix per DEC-09. | Repository |
| `T-G07` | Ledger read model (AL-1..AL-4) over a synthetic practice dataset. No clinical write path, proven by negative test. | Read model v0 |
| `T-G08` | Review workflow: queues, owners, ageing alarms (AR-1), governed verdicts. | Workflow v0 |
| `T-G09` | Projection layer with exported flattening (AX-2 / `NDG-8`). | Projection v0 |
| `T-G10` | Release conformance suite: the seven anti-requirement negative tests plus structural-absence proof (`NDG-5`, `NDG-7`). | Suite; CI gate |

**`GATE-G1`:** conformance suite green; structural absence proven; no clinical write
path demonstrable.

### Sprint G2 — First foothold (weeks 8–12)

| ID | Task | Output |
|---|---|---|
| `T-G11` | Name a design-partner practice with no Mākoha deployment (`NDG-11`). Closes the pilot-naming decision that has been open in the spine. | Named partner |
| `T-G12` | Data agreement, privacy assessment, APP compliance (`NDG-10`). | Executed agreement |
| `T-G13` | Regulator-grade bundle generation (AX-1) demonstrated on real practice data. | Bundle exemplar |
| `T-G14` | Reconstruction exercise (AE-1): external reviewer reconstructs a month of decisions from exports alone. | Validation record |
| `T-G15` | Pricing and recurring-revenue model (`NDG-13`). | Commercial model |

**`GATE-G2`:** one paying or committed site; bundles generated from real data;
reconstruction passed.

---

## 5 — Integration into Makoha Imago

Additive only. No corpus volume is edited in place; the append-only law holds.

| Artifact | Change | Type |
|---|---|---|
| `03_/abdomen-corpus` | Annex: the auditor face as an independently releasable non-device artifact; NDG requirements cited; no AX/AL/AR/AT/AG requirement altered | Additive annex |
| `03_/four-faces-corpus` | Annex note: the abdomen face acquires a second release form. XC-1 honesty posture governs it as it governs J-1/J-2 | Additive annex |
| `03_/antennae-corpus` | Carrier map row: `ASSUME-REG-009`, `Q-REG-010`, `NDG-*` → MAK-GOV. Requires an AN-5 map re-run | Carrier map update |
| REG-POSTURE | v1.2: new `REG-FIND-013` (non-device line available), `ASSUME-REG-009`, `Q-REG-010`, `TASK-REG-023`; `TASK-REG-002` scope extended | New version, folded |
| `01_/MET-2` | New conflict row: does a non-device governance artifact contradict "no patient face" scoping? (It does not — different face.) New decision DEC-G1 (namespace), DEC-G2 (ship the non-device line) | Register rows |
| `01_/MET-4` | G-04 (patient-surface scope) unchanged. New gap: non-device classification unattested | Gap row |
| `05_/REG-R30` | Seed extended with the new posture IDs | Register seed |
| `06_/REPO-MAP` | `cdss-governance` reclassified from register home to releasable repository; add release channel | Repo map |
| `07_/DEPLOY-2` | Acceptance criteria for the `NDG-5` structural-absence proof and the `NDG-7` negative tests | Added criteria |
| MAK-J3 | Retirement notice references this addendum as the non-classified route that replaces the exempt-tier reserve | Retirement notice |

### Decisions this raises

| ID | Decision | Owner | Timing |
|---|---|---|---|
| `DEC-G1` | Namespace and doc_id for this addendum (J-series vs new) | Architecture owner | Before fold |
| `DEC-G2` | Ship the non-device line as first revenue | Founder + advisor | GATE-G0 |
| `DEC-G3` | NDG-3 latency floor value | Regulatory + product | Sprint G0 |
| `DEC-G4` | Whether `cdss-governance` splits into register-home and product repos | Architecture owner | Sprint G1 |

---

## 6 — What this does not do

It does not accelerate `GATE-004`. It does not generate clinical validation evidence
(`NDG-12`). It does not reduce any classified-track obligation. It does not resolve the
patient-surface question, which remains blocked on DEC-07.

It puts a foothold down: revenue, a named site, real data, regulator-grade bundles
demonstrated in production, and a commercial answer to the ten-year objection — while
the classified device proceeds on its own timeline.

---

*Regulatory content is advisory and requires counsel attestation. Non-device status is
an argument, not a determination.*
