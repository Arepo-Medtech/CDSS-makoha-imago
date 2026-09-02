---
doc_id: REG-NZ
title: "Mākoha — Regulatory Posture: NEW ZEALAND (Medsafe)"
jurisdiction: NEW ZEALAND
regulator: Medsafe (New Zealand Medicines and Medical Devices Safety Authority), Ministry of Health / Manatū Hauora
version: 1.1
status: DRAFT
authority: ADVISORY_ONLY
entity: Arepo Medtech Pty Ltd
product: Mākoha
date_issued: 2026-09-02
guidance_currency_date: 2026-09-02
supersedes: REG-NZ v1.0 (2026-09-01)
standalone_rule: "REPLETE-STANDALONE. This document carries the complete standards stack, the technical-file contents and every New Zealand obligation itself. It never says 'see REG-POSTURE' for anything a reader needs in order to act in New Zealand. Companion documents for other jurisdictions follow the same rule and repeat the stack by design."
companions:
  - "REG-POSTURE v1.2 — AUSTRALIA (TGA)"
  - "REG-US v1.0 — UNITED STATES (FDA)"
  - "REG-EU v1.0 — EUROPEAN UNION (MDR 2017/745)"
runtime_register: "R30 — Regulatory Posture Register; NZ-* rows seeded in R30.1, extended in R30.2"
id_prefixes: [NZ-FIND, NZ-OBL, NZ-STD, NZ-ASSUME, NZ-TASK, NZ-GATE, NZ-WATCH, NZ-Q, NZ-SRC]
attestation_required: true
attestation_by: New Zealand regulatory counsel
---

# Mākoha — Regulatory Posture: NEW ZEALAND (Medsafe)

**Jurisdiction:** NEW ZEALAND · Medsafe · Medicines Act 1981 (interim regime)
**Prepared for:** Arepo Medtech Pty Ltd
**Version:** 1.1 · 2 September 2026 · supersedes v1.0 (1 September 2026)
**Status:** Working document. Not regulatory advice. Requires New Zealand counsel attestation before any commitment.

> **How to read this document.** It is the New Zealand authority for Mākoha's
> regulatory posture and is written to stand alone. v1.0 was a companion brief that
> pointed to the Australian posture for its standards stack ("the same artefacts
> `STD-001..013` already require"). v1.1 rolls the stack in (§5), states what the
> technical file Medsafe may request actually contains (§6), and homes two IDs that
> were minted elsewhere and never landed here (`NZ-Q-004`, `NZ-ASSUME-005`). Nothing in
> v1.0 is deleted; amended passages carry **[AMENDED v1.1]**. Items that originate from
> the author's gap review rather than a New Zealand source carry **[recommendation]**
> and a confidence tag.

---

## §A Amendment log (v1.0 → v1.1)

| # | Amendment | Trigger | Affected IDs |
|---|---|---|---|
| A-1 | Document made replete-standalone: full standards stack rolled in as `NZ-STD-*` with Medsafe recognition status per row; technical-file contents stated; New Zealand-specific privacy, health-information and Māori-data instruments named rather than gestured at. | User direction 2026-09-02 | new §5, §6; `NZ-STD-001..026`; `NZ-OBL-009`, `NZ-OBL-010` expanded |
| A-2 | `NZ-Q-004` homed. REG-SPRINT-1.1 D-2 minted it ("earliest lawful notification point; obligations on a notified-but-unsupplied device; does the transition protect notified or supplied devices") and D-5 said it "joins the REG-NZ question register" — it never did. Survey-2 flagged the gap. | REG-SPRINT-1.1 D-2/D-5; survey-2 | new `NZ-Q-004` |
| A-3 | `NZ-ASSUME-005` homed. EXEC-1 EX-7 registered the working assumption (Medical Products Bill carries transition provisions for already-notified devices) in R30.1 with no document home. | EXEC-1 EX-7; R30.1 | new `NZ-ASSUME-005` |
| A-4 | Gates given IDs. v1.0 used `NZ-GATE-0/1/2` in prose without a definition table or prefix registration. | Validator discipline | `NZ-GATE-000..002`; `id_prefixes` |
| A-5 | Post-market system specified. v1.0 said "post-market operating before supply" without saying what that means for a SaMD under the Medicines Act. | `NZ-FIND-008` | `NZ-OBL-007` expanded; new `NZ-TASK-009` |
| A-6 | Cyber security carried explicitly. Medsafe has no device-cyber guidance of its own under the interim regime; the technical file will be read by a regulator who talks to the TGA (`NZ-FIND-008`), so the cyber stack is stated here rather than assumed. | Gap review | `NZ-STD-007..012`, `NZ-STD-017`; `NZ-OBL-011` |
| A-7 | Electronic-record integrity for the "humans release" rule carried as a New Zealand obligation, in the same terms as the Australian and US files, so the record is author-once. | Gap review | new `NZ-OBL-012` |
| A-8 | Sources extended to primary New Zealand instruments for privacy, health information security and Māori data governance. | A-1 | `NZ-SRC-006..011` |
| A-9 | Census and self-audit added (v1.0 had a confidence note but no census). | House law | §12 |

### A.1 Provenance and confidence tags

| Tag | Meaning |
|---|---|
| **[NZ-sourced]** | Traceable to a primary New Zealand government or legislative source in §11 |
| **[secondary]** | From consultancy or vendor material; directionally consistent with primary sources; confirm with counsel |
| **[recommendation]** | Originates from the author's gap review; requires counsel or quality-lead confirmation |
| **[confidence: high / medium / low]** | Author's confidence the item is correctly stated and currently in force; low-confidence items must be re-anchored before `NZ-GATE-000` |

---

## §0 Conventions

Same conventions as the Australian posture, restated here so this document stands
alone.

### 0.1 Authority

This document is **advisory input**. It cannot be cited as evidence for a DONE. Every
material finding about New Zealand regulation is carried as an `NZ-ASSUME-*` requiring
written attestation from New Zealand counsel before it may be relied upon. Where this
document and any governing programme document conflict, the governing document
prevails until the assumption is attested.

### 0.2 ID scheme

| Prefix | Meaning | Closure |
|---|---|---|
| `NZ-FIND-nnn` | Finding about New Zealand regulation | Superseded or attested |
| `NZ-OBL-nnn` | Standing New Zealand obligation | Never closes; evidence maintained |
| `NZ-STD-nnn` | Standard in scope for the New Zealand technical file | Retired only by pathway change |
| `NZ-ASSUME-nnn` | Assumption requiring external closure | Written attestation, named party, dated |
| `NZ-TASK-nnn` | Sequenced work item | DONE-with-evidence or typed HALT |
| `NZ-GATE-nnn` | Blocking gate | All predecessor tasks DONE-with-evidence |
| `NZ-WATCH-nnn` | External change to monitor | Never closes; stated cadence |
| `NZ-Q-nnn` | Open question requiring external input | Answer received in writing |
| `NZ-SRC-nnn` | Source | Retired when superseded upstream |

### 0.3 Status vocabulary

`OPEN` · `IN-PROGRESS` · `DONE-WITH-EVIDENCE` · `HALT-TYPED` · `SUPERSEDED` ·
`ATTESTED` · `REFUTED`. `NZ-ASSUME-*` may hold only `OPEN`, `ATTESTED`, `REFUTED` or
`SUPERSEDED`. No assumption closes by internal reasoning. Register-side (R30), these
map as: `IN-PROGRESS` → `OPEN`; `DONE-WITH-EVIDENCE`/`SUPERSEDED` → `CLOSED`;
`HALT-TYPED` → `OPEN` + blocks; gates additionally take `passed`.

### 0.4 Citation form

Cite by stable ID, never by section number: *Per `NZ-FIND-008`, Medsafe shares safety
information with the TGA.*

### 0.5 Firewall note

This document contains no case content, no evidence-library values, no sensitivities,
specificities or likelihood ratios. It must not be used as a source for clinical
content.

### 0.6 Jurisdiction declaration and the replete-standalone rule

**This document is NEW ZEALAND.** Every finding, obligation, gate and task is stated
against the Medicines Act 1981, the Medicines (Database of Medical Devices)
Regulations 2003, Medsafe guidance, and the New Zealand privacy and health-information
instruments named in §11. Foreign instruments appear only where a New Zealand choice
depends on them.

The four jurisdiction documents share one standards stack and one architecture; they
do not share text by reference. Each carries the complete stack with that regulator's
recognition status, and its own obligations, gates, tasks, assumptions, questions,
watch items and sources. Shared programme artifacts — the intended purpose statement,
the ISO 14971 risk file, the IEC 62304 lifecycle records, the technical documentation
— are built once and projected per regulator. A change to the shared stack is made in
all four documents in the same revision cycle, or the divergence is logged in the
wrapper (MAK-ANT) as a signal.

---

## §1 Headline

**New Zealand does not require pre-market approval for medical devices.** There is no
technical review, no registration certificate, and no market-entry fee. The regime is
notification plus post-market accountability: a New Zealand sponsor notifies the
device to the Medsafe WAND database within the required window and carries legal
responsibility for safety, vigilance and compliance thereafter.

For a device that would face conformity assessment and ARTG inclusion in Australia,
this is a materially different proposition. It is the strongest version of the
argument the advisory note was reaching for — and it does not depend on the dog-cancer
analogy, which turns on a species jump rather than a jurisdiction one.

**The window is closing.** The Therapeutic Products Act 2023 has been repealed, so the
Medicines Act 1981 and the Medicines (Database of Medical Devices) Regulations 2003
continue in force. But Cabinet agreed in July 2025 that the replacement Medical
Products Bill **will regulate software as a medical device, including artificial
intelligence used for a therapeutic purpose**. The current regime is an interim state
with a stated intention to close exactly the gap Mākoha would enter through.

That gives the sequencing its urgency, and it is a better urgency argument than the
commercial one.

> **[AMENDED v1.1]** "Lighter entry" must not be read as "lighter file". §5 and §6
> state what the file contains. It is the same file Australia will assess; New Zealand
> simply lets it be held rather than reviewed before supply. Anyone planning New
> Zealand supply against a thinner file than the Australian one is reading this
> document wrongly, and `NZ-FIND-008` says why that error would be visible to the TGA.

---

## §2 Findings

| ID | Finding | Status | Source |
|---|---|---|---|
| `NZ-FIND-001` | No pre-market approval, technical review or licensing is required for medical devices. Market entry is by sponsor notification. **[NZ-sourced; high]** | OPEN | `NZ-SRC-001`, `NZ-SRC-004` |
| `NZ-FIND-002` | Devices must be notified to the WAND database. Sources differ on whether the window is 30 calendar days or 30 working days from becoming sponsor; Medsafe's own guideline text says 30 working days. **Verify before relying on either.** **[mixed; medium]** | OPEN | `NZ-SRC-001`, `NZ-SRC-002` |
| `NZ-FIND-003` | WAND notification is explicitly **not** an approval and does not imply Medsafe has assessed quality, safety or efficacy. It must never be represented as approval in any claim, IFU or marketing material. **[NZ-sourced; high]** | OPEN | `NZ-SRC-001` |
| `NZ-FIND-004` | The Therapeutic Products Act 2023 has been repealed. The Medicines Act 1981 and Dietary Supplements Regulations 1985 continue in the interim. **[NZ-sourced; high]** | OPEN | `NZ-SRC-003` |
| `NZ-FIND-005` | The replacement Medical Products Bill will regulate SaMD including AI used for a therapeutic purpose, per Cabinet agreement of July 2025. Timing and detail unpublished. **[NZ-sourced; high as to intent, low as to timing]** | OPEN | `NZ-SRC-005` |
| `NZ-FIND-006` | A New Zealand sponsor — a NZ person or company that imports or supplies — is required. The sponsor carries the legal responsibility. **[secondary + primary; medium-high]** | OPEN | `NZ-SRC-001`, `NZ-SRC-002` |
| `NZ-FIND-007` | Medsafe may request the technical file. The sponsor must be able to provide it, and failure can result in removal from market. There is no pre-market review, but there is a standing evidentiary expectation. **[secondary; medium]** | OPEN | `NZ-SRC-002` |
| `NZ-FIND-008` | Medsafe operates active post-market controls including recall powers, and communicates safety information to other regulators — **the TGA specifically**. **[secondary; medium — confirm the formal channel with counsel]** | OPEN | `NZ-SRC-002` |
| `NZ-FIND-009` | The Medicines Act does not provide for recognition of other regulators' authorisations. NZ entry is not a reliance pathway from an ARTG listing, and an ARTG listing is not a prerequisite. **[NZ-sourced; high]** | OPEN | `NZ-SRC-004` |
| `NZ-FIND-010` **[NEW v1.1]** | Medsafe publishes no device-specific software or cyber security standard of its own under the interim regime. The evidentiary expectation for the technical file is therefore set by international standards and by what a peer regulator (TGA) would recognise — which is why the full stack (§5) is carried here rather than a New Zealand subset. **[NZ-sourced by absence; medium]** | OPEN | `NZ-SRC-001`, `NZ-SRC-004` |
| `NZ-FIND-011` **[NEW v1.1]** | New Zealand health-sector procurement (Health New Zealand / Te Whatu Ora and PHOs) applies the HISO health information security and governance standards to vendors independently of Medsafe status. These are procurement conditions, not device regulation, but they bind any real deployment. **[NZ-sourced; medium — HISO edition currency to verify]** | OPEN | `NZ-SRC-008`, `NZ-SRC-009` |
| `NZ-FIND-012` **[NEW v1.1]** | Health information in New Zealand is governed by the Privacy Act 2020 **as modified by the Health Information Privacy Code 2020**, which displaces the general information privacy principles for health agencies. The Code's rules — not the Australian APPs — are the test for any Mākoha processing of New Zealand patient information. **[NZ-sourced; high]** | OPEN | `NZ-SRC-006`, `NZ-SRC-007` |

### 2.1 The finding that changes the strategy

`NZ-FIND-008` is the one to sit with. Medsafe shares safety information with the TGA.
A New Zealand deployment is therefore **not** a low-visibility proving ground. An
adverse event, a complaint pattern, or a recall in New Zealand reaches the regulator
you will later ask for ARTG inclusion — and reaches them as a safety signal about a
device from a sponsor they have no prior relationship with.

That cuts both ways, and the upside is real: a clean New Zealand post-market record is
evidence of exactly the total-product-lifecycle discipline the TGA expects. But it
means NZ-first is a reputational commitment, not a rehearsal. The controls have to be
operating before supply, not after.

---

## §3 Classification in New Zealand

New Zealand has no statutory software classification rule of its own under the
interim regime. Medsafe's guidance directs sponsors to classify by risk (Class I, IIa,
IIb, III) using the GHTF/IMDRF-derived classification rules, which are the same rules
Australia has adopted into Schedule 2 of the Therapeutic Goods (Medical Devices)
Regulations 2002. **[secondary; medium — confirm with counsel which classification
text Medsafe treats as authoritative.]**

Consequence: the classification reasoning for New Zealand is the same reasoning as for
Australia. Mākoha is software providing diagnostic information (a ranked differential
with posterior probabilities). Expect **Class IIa at minimum; Class IIb plausible**
where output bears on serious conditions. Self-classified in New Zealand, but the
self-classification is entered on WAND and is what Medsafe will hold the sponsor to.

Two things follow that v1.0 did not state:

1. **The class drives the file, not the entry.** In New Zealand a Class IIb device
   enters exactly as a Class I device does — by notification. What changes is the
   depth of evidence the sponsor must be able to produce (`NZ-FIND-007`) and the
   vigilance expectation.
2. **Self-classification is a claim.** Under-classifying on WAND to lighten the held
   file is the New Zealand analogue of the exemption-contortion the Australian posture
   rejects. Carried as `NZ-ASSUME-002` — the class is attested by counsel, not chosen
   for convenience.

---

## §4 What New Zealand entry requires — obligations register

Non-closing. Evidence maintained continuously.

| ID | Obligation | Note | Source |
|---|---|---|---|
| `NZ-OBL-001` | Appoint a New Zealand sponsor | Arepo NZ entity or a contracted sponsor. Decision, not formality — the sponsor carries legal responsibility | `NZ-FIND-006` |
| `NZ-OBL-002` | Notify to WAND within the required window | Free. No fee, no review. Window per `NZ-FIND-002` (verify) | `NZ-FIND-002` |
| `NZ-OBL-003` | Classify by risk (I, IIa, IIb, III) | Self-classified; same reasoning as the Australian analysis (§3) | `NZ-FIND-006` |
| `NZ-OBL-004` | Maintain a technical file, producible on request | `NZ-FIND-007`. **[AMENDED v1.1]** Contents stated in §6; built from the standards in §5 | `NZ-FIND-007` |
| `NZ-OBL-005` | Hold evidence the device is safe for its intended purpose | Not filed. Held. **[AMENDED v1.1]** Includes clinical evidence appropriate to class — synthetic data is not safety evidence | `NZ-FIND-007` |
| `NZ-OBL-006` | Meet labelling and instructions-for-use requirements | NZ-specific even where relying on overseas material. **[AMENDED v1.1]** Content per ISO 20417 / ISO 15223-1 (`NZ-STD-019/020`); WAND notification must never be described as approval (`NZ-FIND-003`); sponsor name and NZ contact on the label/IFU | `NZ-SRC-001` |
| `NZ-OBL-007` | Post-market: complaints, adverse events, recalls, changes | **[AMENDED v1.1]** For a SaMD this means, before first supply: (a) a complaint-intake channel that reaches the sponsor; (b) adverse-event assessment and reporting to Medsafe within its stated timeframes; (c) a recall procedure aligned to the Medsafe/Uniform Recall Procedure, which for software means remote disablement or forced-update capability plus user notification; (d) a change-control record that distinguishes functional from non-functional changes, because functional updates to AI-enabled software are regulatory events (see `NZ-OBL-013`). Specified as `NZ-TASK-009` | `NZ-FIND-008`; `NZ-SRC-001` |
| `NZ-OBL-008` | Advertising and promotion compliance | Applies independently of device status. **[AMENDED v1.1]** Instruments: Medicines Act 1981 Part 4 and Medicines Regulations 1984 (therapeutic claims); Fair Trading Act 1986 (misleading conduct); Advertising Standards Authority Therapeutic and Health Advertising Code; TAPS pre-vetting is voluntary for devices but is the industry norm. The claims inventory is diffed against the intended purpose every release, as in Australia | `NZ-SRC-001`, `NZ-SRC-010` |
| `NZ-OBL-009` | New Zealand privacy law and health information privacy | **[AMENDED v1.1]** **Separate from the Australian APPs. Do not assume equivalence.** Governing instruments: Privacy Act 2020; **Health Information Privacy Code 2020** (rules 1–13, displacing the IPPs for health agencies; rule 11 disclosure limits; rule 12 cross-border disclosure — relevant if any processing occurs in Australia); Privacy Act 2020 Part 6 notifiable privacy breaches (serious-harm threshold; notify the Privacy Commissioner and affected individuals). A Privacy Impact Assessment is expected by health-sector customers before deployment | `NZ-SRC-006`, `NZ-SRC-007` |
| `NZ-OBL-010` | Māori data sovereignty and Te Tiriti obligations in health data | **[AMENDED v1.1]** Not a formality in NZ health research and service delivery. Instruments: Te Tiriti o Waitangi principles as applied through the Pae Ora (Healthy Futures) Act 2022; Te Mana Raraunga Māori Data Sovereignty principles; Health New Zealand / Te Whatu Ora Māori data governance expectations; HDEC ethics review treats Māori consultation as a standing requirement. Material to any linkage, evaluation or model-training work using New Zealand data, and to where data is stored (offshore storage of Māori health data is a live governance question, not a technical one) | `NZ-SRC-011`, `NZ-SRC-009` |
| `NZ-OBL-011` **[NEW v1.1]** | Health-sector information security as a procurement condition | HISO 10029 Health Information Security Framework (and its associated guidance) is applied by Health New Zealand and many PHOs to vendors handling health information; HISO 10064 Health Information Governance Guidelines likewise. Not Medsafe requirements — customer requirements that bind deployment. The ISO 27799 / ISO 27001 Annex A control set (`NZ-STD-010`, `NZ-STD-024`) is the implementation route | `NZ-FIND-011`; `NZ-SRC-008` |
| `NZ-OBL-012` **[NEW v1.1 — recommendation; high]** | Electronic-record and electronic-signature integrity for human release decisions | Every record evidencing that a human released what an automated system proposed is controlled as an ISO 13485 §4.2.5 quality record and generated in a 21 CFR Part 11-capable form (unique attribution, MFA-backed signature, append-only audit trail, signature meaning and timestamp). New Zealand does not require Part 11; it is adopted so the same record serves the Australian and US files without re-creation | Author-once rule §0.6 |
| `NZ-OBL-013` **[NEW v1.1 — recommendation; medium]** | Pre-deployment assessment of functional changes | Medsafe has no published AI-update guidance under the interim regime. The TGA's does (functional updates to AI-enabled software are regulatory events handled pre-deployment), and Medsafe reads TGA signals (`NZ-FIND-008`). Adopt the TGA position in New Zealand: no functional change to the inference plane reaches a New Zealand user without a documented pre-deployment assessment and a WAND update where the notified particulars change | `NZ-FIND-008`; `NZ-FIND-010` |

**What does not change:** the standards stack. **[AMENDED v1.1]** It is stated in full
in §5 below rather than by reference. Nothing in the NZ path is wasted on the
Australian path.

**What does change:** sequence. In Australia the evidence must exist before supply. In
New Zealand supply can precede the assessment of that evidence — but the evidence must
still exist, and Medsafe can ask for it at any time.

---

## §5 Standards stack — NEW ZEALAND **[NEW v1.1]**

Medsafe names no mandatory standards for devices under the interim regime
(`NZ-FIND-010`). The column "Medsafe status" therefore records how the standard
functions in New Zealand: as **technical-file evidence** Medsafe would recognise
because peer regulators do, as a **procurement condition** New Zealand health
customers apply, or as **not required**. Editions are pinned. Priority 1 = the file is
not credible without it; 2 = expected in the file for a Class IIa/IIb SaMD; 3 =
expected for the cyber case; 4 = situational. Rows from the author's gap review carry
**[recommendation]** and a confidence tag.

### 5.1 Core lifecycle and quality

| ID | Standard | Edition | Role in the New Zealand technical file | Medsafe status | Priority |
|---|---|---|---|---|---|
| `NZ-STD-001` | ISO 13485 | :2016 | Quality management system — the backbone of the held file; the same QMS that carries deemed conformity in Australia. A certificate is not required to notify, but a Medsafe file request will ask how the device is controlled, and the QMS is the answer | Technical-file evidence | **1** |
| `NZ-STD-002` | IEC 62304 | :2006 + A1:2015 | Software lifecycle, safety classification (expect Class B or C), SOUP management, change control, problem resolution. §5.1.4 tool validation → `NZ-STD-013` | Technical-file evidence | **1** |
| `NZ-STD-003` | ISO 14971 | :2019 | Risk management — the risk file is the spine of the technical file | Technical-file evidence | **1** |
| `NZ-STD-004` | IEC 62366-1 | :2015 + A1:2020 | Usability engineering — three surfaces (clinician, pharmacist, patient), three use-related risk analyses. New Zealand adds a bicultural usability consideration: te reo Māori terminology and health-literacy expectations in patient-facing text | Technical-file evidence | **2** |
| `NZ-STD-005` | IEC 82304-1 | :2016 | Health software product safety and security requirements — the product-level standard for software on general computing platforms; the natural organising frame for the New Zealand file because it is the one standard that spans all essential requirements | Technical-file evidence | **2** |
| `NZ-STD-006` | BS/AAMI 34971 | :2023 | Application of ISO 14971 to machine learning — the ML risk hook | Technical-file evidence | **2** |
| `NZ-STD-013` | IEC 62304 §5.1.4 + ISO 13485 §4.1.6 | as above | Validation of software tools in the authoring and release path (authoring surface, Ketryx, release channel) | Implicit in 001/002 | **2** |

### 5.2 Cyber security and information security

| ID | Standard | Edition | Role in the New Zealand technical file | Medsafe status | Priority |
|---|---|---|---|---|---|
| `NZ-STD-007` | ANSI/AAMI SW96 | :2023 | Security risk management for device manufacturers — the security risk file beside the ISO 14971 file | Technical-file evidence | 3 |
| `NZ-STD-008` | IEC 81001-5-1 | :2021 | Security activities in the health software product lifecycle — secure-development-lifecycle evidence | Technical-file evidence | 3 |
| `NZ-STD-009` | ISO/IEC 29147 and ISO/IEC 30111 | 29147:2018; 30111:2019 | Vulnerability disclosure and handling — the process by which a vulnerability reaches CAPA and, where warranted, reaches users and Medsafe | Technical-file evidence | 3 |
| `NZ-STD-010` | ISO 27799 | :2016 | Information security management in health — ISO/IEC 27002 controls applied to health information. Maps cleanly onto HISO 10029 (`NZ-OBL-011`) | Procurement condition (via HISO) | 3 |
| `NZ-STD-011` | IEC 80001-1 | :2021 | Risk management for health IT systems incorporating medical devices — the deployment-side conversation with a PHO, pharmacy group or Health NZ district | Technical-file evidence (deployment) | 4 |
| `NZ-STD-012` | UL 2900-2-1 | :2017 | Network-connectable healthcare product security testing — the penetration-test yardstick | Technical-file evidence | 4 |

### 5.3 Gap-review rows **[recommendation]**

| ID | Standard | Edition | Why it is load-bearing for Mākoha in New Zealand | Medsafe status | Priority | Confidence |
|---|---|---|---|---|---|---|
| `NZ-STD-014` | ISO/TR 24971 | :2020 | Guidance on applying ISO 14971:2019 — the risk file's method | Technical-file evidence | **2** | high |
| `NZ-STD-015` | IEC/TR 80002-1 | :2009 | ISO 14971 applied to medical device software — the bridge to the IEC 62304 safety classification | Technical-file evidence | **2** | high |
| `NZ-STD-016` | AAMI TIR45 | :2023 | Agile practices in medical device software — how a continuously integrated, AI-assisted build is shown to be an IEC 62304 lifecycle | Technical-file evidence | **2** | high |
| `NZ-STD-017` | AAMI TIR57 | :2016 (R2023) | Principles for medical device security — the cited method behind the STRIDE threat model | Technical-file evidence | 3 | high |
| `NZ-STD-018` | ISO 14155 | :2020 | Clinical investigation GCP. **In New Zealand this is the standard that makes New Zealand clinical evidence admissible to the Australian conformity assessment** (`NZ-ASSUME-004`). Any prospective evidence collection under HDEC ethics approval runs to it | Technical-file evidence; HDEC expectation | **1** | high |
| `NZ-STD-019` | ISO 20417 | :2021 | Information supplied by the manufacturer — IFU and labelling content, including the New Zealand sponsor particulars (`NZ-OBL-006`) | Technical-file evidence | **2** | high |
| `NZ-STD-020` | ISO 15223-1 | :2021 | Symbols on labelling and in UI | Technical-file evidence | 3 | high |
| `NZ-STD-021` | ISO/IEC 42001 | :2023 | AI management system — alignment, not certification; the organisational evidence behind 34971 that health-sector procurement increasingly asks for | Procurement (emerging) | 4 | medium |
| `NZ-STD-022` | ISO/IEC 23894 | :2023 | AI risk management guidance — companion to 14971 + 34971 for the model-governance argument | Technical-file evidence | 4 | medium |
| `NZ-STD-023` | IEC 60601-4-5 | :2021 | Security capability levels referenced by IEC 81001-5-1 — applicable only if levels are claimed; otherwise record as considered-not-applicable | Technical-file evidence (conditional) | 4 | medium |
| `NZ-STD-024` | ISO/IEC 27001 | :2022 | Information security management system. **Not required by Medsafe.** Recorded because HISO 10029 alignment and Health NZ procurement routinely ask for it or its Annex A controls, and because SEC-1 already implements Annex A as the equivalent-rigour set. Certification is a commercial decision | Procurement condition | 4 | high |
| `NZ-STD-025` | IMDRF SaMD framework documents | N10:2013, N12:2014, N23:2015, N41:2017 | The vocabulary Medsafe, TGA and FDA share; N12's risk category (healthcare situation × significance of information) is the argument structure for the self-classification in §3 | Recognised framework | **2** | high |
| `NZ-STD-026` | IMDRF cyber and ML documents | N60:2020, N70:2023, N73:2023, N88:2025 | SBOM content expectation (N73) and good machine learning practice (N88) | Recognised framework | 3 | medium (N88 currency to verify) |

### 5.4 Considered and not adopted

| Standard | Reason |
|---|---|
| IEC 60601-1 family (other than 60601-4-5) | No hardware |
| ISO/IEC TS 82304-2 | Consumer health-app quality label; subsumed by 82304-1 for a regulated device |
| AS/NZS joint adoptions | Where an AS/NZS-badged edition exists it is identical to the international text; cite the international edition and note the adoption |
| ISO 9001 | Superseded by ISO 13485 in this context |

---

## §6 The technical file Medsafe may request **[NEW v1.1]**

`NZ-FIND-007` says Medsafe may request the file and the sponsor must produce it. v1.0
did not say what "it" is. Under the interim regime Medsafe publishes no file template;
the recognised structure is the IMDRF/GHTF **Summary Technical Documentation (STED)**
shape, which is also what the TGA conformity-assessment dossier and the EU MDR Annex
II/III documentation reduce to. Build it once, in this shape, and every regulator's
request is an index onto it.

| # | Section | Contents | Built under |
|---|---|---|---|
| 1 | Device description and intended purpose | Intended purpose statement (identical to the Australian one — evidence transfers only when intended purpose is held constant); three surfaces described; New Zealand sponsor particulars; classification and rule with rationale (§3) | Programme `TASK-REG-001`; `NZ-OBL-003` |
| 2 | Labelling and instructions for use | IFU, in-product information, sponsor contact; "notified, not approved" wording (`NZ-FIND-003`) | `NZ-STD-019`, `NZ-STD-020`; `NZ-OBL-006` |
| 3 | Design and manufacturing information | Software architecture, IEC 62304 lifecycle records, software safety classification, SOUP list with the AI service vendor and pinned model version as SOUP items, SBOM (CycloneDX or SPDX), configuration management, release records | `NZ-STD-002`, `NZ-STD-016`, `NZ-STD-026` |
| 4 | Essential requirements checklist | Each essential principle / GSPR-equivalent requirement, the standard applied, and the evidence location. Use the Australian Essential Principles as the checklist spine because the TGA is the peer regulator Medsafe talks to (`NZ-FIND-008`) | All `NZ-STD-*` |
| 5 | Risk management file | ISO 14971 file, ML-specific risks (34971), security risk file (SW96), benefit-risk conclusion, production and post-production information plan | `NZ-STD-003`, `006`, `007`, `014`, `015` |
| 6 | Verification and validation | Software V&V, evaluation-corpus results referenced by case ID (corpus content does not enter the file), usability validation per IEC 62366-1 for each surface, security testing including independent penetration test, tool validation records | `NZ-STD-002`, `004`, `012`, `013` |
| 7 | Clinical evidence | Clinical evaluation report; literature; any prospective investigation under ISO 14155 and HDEC approval; explicit statement of what synthetic data was used for (controls) and what it was **not** used for (safety and performance evidence) | `NZ-STD-018`, `NZ-STD-025` (N41) |
| 8 | Cyber security | Threat model (STRIDE / TIR57), secure development lifecycle evidence (81001-5-1), vulnerability disclosure and handling procedures (29147/30111), SBOM cross-referencing, third-party platform and AI-provider assessments, patch/update pathway, user disclosure of known vulnerabilities | `NZ-STD-007..012`, `017` |
| 9 | Post-market system | Complaint handling, adverse-event assessment and Medsafe reporting, recall procedure including remote disablement, change control with functional/non-functional distinction and pre-deployment assessment, post-market performance monitoring of the model | `NZ-OBL-007`, `NZ-OBL-013`; `NZ-TASK-009` |
| 10 | Declaration | Sponsor's declaration that the device meets the essential requirements for its class and that the file is complete and current | `NZ-OBL-001`, `NZ-OBL-005` |

**Production rule:** the file is generated from the design-controls system (Ketryx
projection: a "Medsafe technical file index" document template over the same
requirement, risk, test and SBOM items the Australian Essential Principles checklist
pulls), not hand-assembled. Hand assembly is how a file drifts from the product.

---

## §7 Strategic reading

### 7.1 The honest version of the argument

Not "regulate light, move fast." The defensible version:

> New Zealand permits supply on the manufacturer's own evidence, under sponsor
> accountability and active post-market oversight, without pre-market review. This
> lets a device with a complete technical file reach real clinical use — same species,
> same intended purpose, same standards — and generate genuine clinical evidence that
> transfers to the Australian submission, because the intended purpose is identical.

That last clause is the whole argument, and it is the one thing the dog-cancer story
lacks. Evidence transfers when intended purpose is held constant. It does not transfer
across species, and it did not transfer from J-3's exempt tier.

### 7.2 What it does not buy

It does not reduce the technical-file burden. It does not substitute for conformity
assessment. It does not create an ARTG reliance pathway (`NZ-FIND-009`). And it does
not lower the standard of care owed to New Zealand patients, who are not a pilot
cohort.

### 7.3 The timing argument

Two clocks run against each other. The Medical Products Bill will bring SaMD and AI
into scope (`NZ-FIND-005`), and the technical file has to exist regardless. So the
question is not "how fast can we ship in NZ" but "can the technical file be ready
before the regime changes" — and if the answer is no, NZ-first delivers less than it
appears to.

Worth modelling honestly. If the Bill lands with transition provisions for existing
notified devices, early notification is valuable. If it does not, the advantage is
smaller than the effort.

> **[AMENDED v1.1]** The programme currently operates on the **working assumption**
> that the Bill will carry transition provisions for already-notified devices, and
> that the protection attaches to *notification* rather than *supply*. That assumption
> is registered as `NZ-ASSUME-005`, the question that tests it is `NZ-Q-004`, and the
> schedule consequence (pull WAND notification to the earliest lawful point after the
> file is complete, decoupled from first commercial site) is pre-registered: if the
> assumption closes badly, notification loses its urgency and the plan re-weights
> toward commercial readiness. That is a lookup, not a debate.

### 7.4 The registrar question

You are taking up a Medical Registrar post in New Zealand. That is an asset — local
clinical credibility, network, and a reason to be in-country — and a governance
exposure. Any arrangement where you are simultaneously a clinician in a health service
and a director of a company supplying software into that service needs conflict
declaration and probably employer sign-off before conversations begin. Get that clean
first; it is much harder to retrofit than to declare.

---

## §8 Sequenced actions

### Gates

| ID | Gate | Predecessors | Meaning |
|---|---|---|---|
| `NZ-GATE-000` | Decide | `NZ-TASK-001..004` | Counsel attested; sponsor decided; conflict cleared; timing modelled |
| `NZ-GATE-001` | File and controls | `NZ-TASK-005..007`, `NZ-TASK-009` | Technical file complete (§6); post-market system operating; privacy and Māori-data assessments cleared |
| `NZ-GATE-002` | Notify and supply | `NZ-TASK-008`, `NZ-TASK-010` | Notified; first supply — the two events are separable and are gated separately (`NZ-TASK-008` then `NZ-TASK-010`) |

`NZ-GATE-001` is deliberately equivalent in substance to the Australian controls gate
plus the technical file. New Zealand's lighter *entry* does not license lighter
*controls*, and `NZ-FIND-008` is the reason.

### Tasks

| ID | Task | Gate |
|---|---|---|
| `NZ-TASK-001` | Engage New Zealand regulatory counsel. Confirm `NZ-FIND-001..012`, the notification window, sponsor structure, expected classification, and `NZ-Q-004`. | `NZ-GATE-000` |
| `NZ-TASK-002` | Resolve the sponsor question: Arepo NZ entity vs contracted sponsor. Cost, control and liability differ materially. | `NZ-GATE-000` |
| `NZ-TASK-003` | Declare the registrar/director conflict to the employer; obtain written position before any commercial conversation in-country. | `NZ-GATE-000` |
| `NZ-TASK-004` | Model the Medical Products Bill timing against technical-file readiness (`NZ-WATCH-001`, `NZ-ASSUME-005`). Decide whether NZ-first survives the analysis. | `NZ-GATE-000` |
| `NZ-TASK-005` | NZ privacy, health information and Māori data sovereignty assessment — Privacy Impact Assessment against the Health Information Privacy Code 2020; data-residency decision for New Zealand patient data; Māori data governance engagement. Distinct from the Australian work. | `NZ-GATE-001` |
| `NZ-TASK-006` | Technical file assembled to §6, from the standards in §5. **[AMENDED v1.1]** This is the same set of artifacts the Australian conformity assessment consumes, produced once and indexed for Medsafe; it is not a second file. | `NZ-GATE-001` |
| `NZ-TASK-007` | Post-market system operating **before** supply: complaints, adverse events, recall capability (`NZ-FIND-008`). | `NZ-GATE-001` |
| `NZ-TASK-008` | WAND notification, at the earliest lawful point after `NZ-GATE-001` (`NZ-Q-004`). | `NZ-GATE-002` |
| `NZ-TASK-009` **[NEW v1.1]** | Specify and test the SaMD post-market mechanisms named in `NZ-OBL-007`: complaint channel, adverse-event triage and Medsafe reporting SOP, remote disablement / forced-update recall path with user notification, functional-change pre-deployment assessment (`NZ-OBL-013`). Evidence: a tabletop recall exercise on the synthetic deployment. | `NZ-GATE-001` |
| `NZ-TASK-010` **[NEW v1.1]** | First New Zealand commercial site, on commercial readiness and independent of `NZ-TASK-008` timing. HISO / procurement security questionnaire (`NZ-OBL-011`) and data agreement executed. | `NZ-GATE-002` |

---

## §9 Assumptions

No `NZ-ASSUME-*` closes by internal reasoning.

| ID | Assumption | Attesting party | Blocks | Status |
|---|---|---|---|---|
| `NZ-ASSUME-001` | The notification window and its trigger point | NZ counsel | `NZ-GATE-000` | OPEN |
| `NZ-ASSUME-002` | Mākoha's NZ classification and whether any WAND exemption applies | NZ counsel | `NZ-GATE-000` | OPEN |
| `NZ-ASSUME-003` | Sponsor structure and liability allocation | NZ counsel | `NZ-GATE-000` | OPEN |
| `NZ-ASSUME-004` | Whether NZ clinical evidence will be accepted in an Australian conformity assessment, and on what conditions (expect: ISO 14155 conduct, HDEC approval, identical intended purpose) | AU counsel | Australian `GATE-003`; NZ evidence strategy | OPEN |
| `NZ-ASSUME-005` **[NEW v1.1 — homed from R30.1 / EXEC-1 EX-7]** | The Medical Products Bill will carry transition provisions for already-notified devices, and the protection attaches to notification rather than supply. Owner: founder. Consequence pre-registered in §7.3 | NZ counsel / Ministry of Health (Bill text) | `NZ-TASK-008` urgency ranking | OPEN |

`NZ-ASSUME-004` is the highest-value assumption in this document. If NZ evidence does
not transfer, NZ-first is a revenue strategy rather than an evidence strategy — still
legitimate, but a different case, and it should be argued as one.

---

## §10 Questions and watch items

### 10.1 Questions

| ID | Question | Who | Blocking |
|---|---|---|---|
| `NZ-Q-001` | Does the Medical Products Bill contemplate transition for devices already notified? | NZ counsel / MoH | `NZ-TASK-004` |
| `NZ-Q-002` | Registrar/director conflict position | Employer | `NZ-TASK-003` |
| `NZ-Q-003` | Does the Governance Layer (MAK-GOV) need WAND notification, or is it out of scope as a non-device in New Zealand too? | NZ counsel | MAK-GOV `GATE-G0` |
| `NZ-Q-004` **[NEW v1.1 — homed from REG-SPRINT-1.1 D-2]** | What is the earliest lawful point at which Mākoha can be notified to WAND; what obligations attach to a notified-but-not-yet-supplied device; and is the Bill's transition likely to protect *notified* or *supplied* devices? This is the question `NZ-ASSUME-005` hangs on | NZ counsel | `NZ-TASK-008` |
| `NZ-Q-005` **[NEW v1.1]** | Does Medsafe treat the Australian Schedule 2 classification rules, the EU MDR Annex VIII rules, or the IMDRF N12 framework as the authoritative classification text for WAND self-classification of software? | NZ counsel / Medsafe | `NZ-ASSUME-002` |
| `NZ-Q-006` **[NEW v1.1]** | Data residency: may New Zealand patient data be processed on Australian-region infrastructure under Health Information Privacy Code rule 12 and Health NZ Māori data governance expectations, or is New Zealand-region hosting a deployment precondition? | NZ counsel + privacy specialist | `NZ-TASK-005` |

### 10.2 Watch items

| ID | Item | Cadence |
|---|---|---|
| `NZ-WATCH-001` | Medical Products Bill — introduction, scope, SaMD and AI provisions, transition arrangements | Monthly until introduced |
| `NZ-WATCH-002` | Medsafe guidance on software and AI under the interim regime | Quarterly |
| `NZ-WATCH-003` | PHARMAC centralised device procurement — changes the buyer, not the regulator | Semi-annually |
| `NZ-WATCH-004` **[NEW v1.1]** | HISO standards revisions (10029 security framework, 10064 governance) and Health NZ vendor-assurance requirements | Semi-annually |
| `NZ-WATCH-005` **[NEW v1.1]** | Standards revision: IEC 62304 Ed.2, ISO 13485 review, ISO 14971/TR 24971 cycle, BS/AAMI 34971 progression. Editions pinned in §5 re-confirmed before `NZ-TASK-008` | Annually; at `NZ-GATE-001` |

---

## §11 Sources

| ID | Source | Currency | Class |
|---|---|---|---|
| `NZ-SRC-001` | Medsafe, GRTPNZ — overview of therapeutic product regulation; product and activity controls for medical devices; WAND guidance | Current under Medicines Act 1981 | Primary |
| `NZ-SRC-002` | Commercial regulatory-consultancy guides to NZ device registration and WAND | 2025–2026 | **Secondary — vendor-authored** |
| `NZ-SRC-003` | Beehive releases: TPA repeal announced and repeal bill passed | Current | Primary |
| `NZ-SRC-004` | Ministry of Health Regulatory Impact Statement — product and activity controls for medical devices | October 2024 | Primary |
| `NZ-SRC-005` | Medical Products Bill Cabinet material — July 2025 agreement to regulate SaMD including AI for therapeutic purpose | 2025 | Primary |
| `NZ-SRC-006` **[NEW v1.1]** | Privacy Act 2020 (incl. Part 6 notifiable privacy breaches) | Current | Primary |
| `NZ-SRC-007` **[NEW v1.1]** | Health Information Privacy Code 2020 (Office of the Privacy Commissioner) | Current | Primary |
| `NZ-SRC-008` **[NEW v1.1]** | HISO 10029 Health Information Security Framework; HISO 10064 Health Information Governance Guidelines | **Edition currency to verify** | Primary (sector standard) |
| `NZ-SRC-009` **[NEW v1.1]** | Health New Zealand / Te Whatu Ora vendor and data-governance requirements; HDEC Standard Operating Procedures (Māori consultation) | Current; **verify current SOP edition** | Primary |
| `NZ-SRC-010` **[NEW v1.1]** | Medicines Act 1981 Part 4; Medicines Regulations 1984; Fair Trading Act 1986; ASA Therapeutic and Health Advertising Code; TAPS | Current | Primary |
| `NZ-SRC-011` **[NEW v1.1]** | Pae Ora (Healthy Futures) Act 2022; Te Mana Raraunga Māori Data Sovereignty principles | Current | Primary |
| `NZ-SRC-012` **[NEW v1.1]** | Standards-gap review, 2 September 2026 — author's comparison of the stack against peer-regulator expectations | 2 September 2026 | **Author's analysis; every row tagged [recommendation]** |
| `NZ-SRC-013` **[NEW v1.1]** | REG-SPRINT-1.1 delta (D-2, D-5); EXEC-1 (EX-7); R30.1 — the origin of `NZ-Q-004` and `NZ-ASSUME-005` | 1 September 2026 | Internal |

**Confidence note.** `NZ-FIND-001`, `003`, `004`, `009` and `012` rest on primary
government sources and are high confidence. `NZ-FIND-002` (the window) shows a genuine
discrepancy across sources and must be verified. `NZ-FIND-006`, `007` and `008` rest
partly on consultancy material with an interest in selling sponsorship services —
directionally consistent with the primary sources, but confirm with counsel rather than
with a vendor. `NZ-FIND-010` and `011` are medium confidence. The `NZ-STD-*` editions
were pinned from the author's knowledge of the standards catalogue and should be
re-confirmed against the publishers before `NZ-GATE-001` (`NZ-WATCH-005`).

---

## §12 Census and self-audit **[NEW v1.1]**

### 12.1 Census

| Prefix | v1.0 | v1.1 | Range |
|---|---|---|---|
| `NZ-FIND` | 9 | 12 | 001–012 |
| `NZ-OBL` | 10 | 13 | 001–013 |
| `NZ-STD` | 0 | 26 | 001–026 |
| `NZ-ASSUME` | 4 | 5 | 001–005 |
| `NZ-TASK` | 8 | 10 | 001–010 |
| `NZ-GATE` | 3 (prose only) | 3 | 000–002 |
| `NZ-WATCH` | 3 | 5 | 001–005 |
| `NZ-Q` | 3 | 6 | 001–006 |
| `NZ-SRC` | 5 | 13 | 001–013 |
| **Total** | **45** | **93** | |

Retired: none. No ID reused. v1.0 prose gates `NZ-GATE-0/1/2` are renamed
`NZ-GATE-000/001/002` for pattern conformance; the v1.0 file is unedited.

### 12.2 Self-audit

| # | Check | Result |
|---|---|---|
| 1 | All IDs match `^NZ-(FIND|OBL|STD|ASSUME|TASK|GATE|WATCH|Q|SRC)-[0-9]{3}$` | PASS |
| 2 | Every ID defined exactly once in a table | PASS |
| 3 | Every `NZ-TASK-*` names its gate | PASS (10/10) |
| 4 | Every `NZ-GATE-*` names predecessors; all exist | PASS (3/3) |
| 5 | Every `NZ-ASSUME-*` names attesting party and what it blocks | PASS (5/5) |
| 6 | Every `NZ-FIND-*` names at least one `NZ-SRC-*` | PASS (12/12) |
| 7 | Status values drawn only from §0.3 | PASS |
| 8 | Every `NZ-STD-*` row carries an edition and a Medsafe status | PASS (26/26) |
| 9 | Every gap-review row carries [recommendation] and a confidence tag | PASS |
| 10 | No reference of the form "see REG-POSTURE" for New Zealand-actionable content | PASS |
| 11 | `NZ-Q-004` and `NZ-ASSUME-005` defined (survey-2 gap; R30.1 rows homed) | PASS |
| 12 | Frontmatter `id_prefixes` ↔ §0.2 ↔ §12.1; range endpoints checked both ends | PASS (9/9 families) |

---

*Advisory only. New Zealand counsel must confirm before any commitment. Nothing here
authorises supply. Items tagged [recommendation] originate from the author's gap
review and require confirmation by counsel and the quality lead before adoption.*
