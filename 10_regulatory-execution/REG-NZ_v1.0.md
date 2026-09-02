---
doc_id: REG-NZ
title: "Mākoha — New Zealand Regulatory Brief"
version: 1.0
status: DRAFT
authority: ADVISORY_ONLY
entity: Arepo Medtech Pty Ltd
date_issued: 2026-09-01
guidance_currency_date: 2026-09-01
companion_to: REG-POSTURE v1.1
id_prefixes: [NZ-FIND, NZ-OBL, NZ-ASSUME, NZ-TASK, NZ-WATCH, NZ-Q, NZ-SRC]
attestation_required: true
attestation_by: New Zealand regulatory counsel
---

# Mākoha — New Zealand Regulatory Brief

**Companion to REG-POSTURE v1.1.** Same conventions: advisory, ID-cited, every
material finding carried as an assumption requiring counsel attestation.

---

## 1 — Headline

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

---

## 2 — Findings

| ID | Finding | Status | Source |
|---|---|---|---|
| `NZ-FIND-001` | No pre-market approval, technical review or licensing is required for medical devices. Market entry is by sponsor notification. | OPEN | `NZ-SRC-001`, `NZ-SRC-004` |
| `NZ-FIND-002` | Devices must be notified to the WAND database. Sources differ on whether the window is 30 calendar days or 30 working days from becoming sponsor; Medsafe's own guideline text says 30 working days. **Verify before relying on either.** | OPEN | `NZ-SRC-001`, `NZ-SRC-002` |
| `NZ-FIND-003` | WAND notification is explicitly **not** an approval and does not imply Medsafe has assessed quality, safety or efficacy. It must never be represented as approval in any claim, IM or marketing material. | OPEN | `NZ-SRC-001` |
| `NZ-FIND-004` | The Therapeutic Products Act 2023 has been repealed. The Medicines Act 1981 and Dietary Supplements Regulations 1985 continue in the interim. | OPEN | `NZ-SRC-003` |
| `NZ-FIND-005` | The replacement Medical Products Bill will regulate SaMD including AI used for a therapeutic purpose, per Cabinet agreement of July 2025. Timing and detail unpublished. | OPEN | `NZ-SRC-005` |
| `NZ-FIND-006` | A New Zealand sponsor — a NZ person or company that imports or supplies — is required. The sponsor carries the legal responsibility. | OPEN | `NZ-SRC-001`, `NZ-SRC-002` |
| `NZ-FIND-007` | Medsafe may request the technical file. The sponsor must be able to provide it, and failure can result in removal from market. There is no pre-market review, but there is a standing evidentiary expectation. | OPEN | `NZ-SRC-002` |
| `NZ-FIND-008` | Medsafe operates active post-market controls including recall powers, and communicates safety information to other regulators — **the TGA specifically**. | OPEN | `NZ-SRC-002` |
| `NZ-FIND-009` | The Medicines Act does not provide for recognition of other regulators' authorisations. NZ entry is not a reliance pathway from an ARTG listing, and an ARTG listing is not a prerequisite. | OPEN | `NZ-SRC-004` |

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

## 3 — What NZ entry actually requires

| ID | Obligation | Note |
|---|---|---|
| `NZ-OBL-001` | Appoint a New Zealand sponsor | Arepo NZ entity or a contracted sponsor. Decision, not formality — the sponsor carries legal responsibility |
| `NZ-OBL-002` | Notify to WAND within the required window | Free. No fee, no review |
| `NZ-OBL-003` | Classify by risk (I, IIa, IIb, III) | Self-classified; expect the same reasoning as the Australian analysis |
| `NZ-OBL-004` | Maintain a technical file, producible on request | `NZ-FIND-007`. This is where ISO 13485 / 62304 / 14971 work pays back |
| `NZ-OBL-005` | Hold evidence the device is safe for its intended purpose | Not filed. Held |
| `NZ-OBL-006` | Meet labelling and instructions-for-use requirements | NZ-specific even where relying on overseas material |
| `NZ-OBL-007` | Post-market: complaints, adverse events, recalls, changes | The substance of the regime |
| `NZ-OBL-008` | Advertising and promotion compliance | Applies independently of device status |
| `NZ-OBL-009` | NZ privacy law and health information privacy | **Separate from the Australian APPs. Do not assume equivalence** |
| `NZ-OBL-010` | Māori data sovereignty and Te Tiriti obligations in health data | Not a formality in NZ health research and service delivery. Material to any linkage or evaluation work |

**What does not change:** the standards stack. ISO 13485, IEC 62304, ISO 14971, IEC
62366-1 and IEC 82304-1 are what the technical file is made of, and they are the same
artefacts `STD-001..013` already require. Nothing in the NZ path is wasted on the
Australian path.

**What does change:** sequence. In Australia the evidence must exist before supply. In
New Zealand supply can precede the assessment of that evidence — but the evidence must
still exist, and Medsafe can ask for it at any time.

---

## 4 — Strategic reading

### 4.1 The honest version of the argument

Not "regulate light, move fast." The defensible version:

> New Zealand permits supply on the manufacturer's own evidence, under sponsor
> accountability and active post-market oversight, without pre-market review. This
> lets a device with a complete technical file reach real clinical use — same species,
> same intended purpose, same standards — and generate genuine clinical evidence that
> transfers to the Australian submission, because the intended purpose is identical.

That last clause is the whole argument, and it is the one thing the dog-cancer story
lacks. Evidence transfers when intended purpose is held constant. It does not transfer
across species, and it did not transfer from J-3's exempt tier.

### 4.2 What it does not buy

It does not reduce the technical-file burden. It does not substitute for conformity
assessment. It does not create an ARTG reliance pathway (`NZ-FIND-009`). And it does
not lower the standard of care owed to New Zealand patients, who are not a pilot
cohort.

### 4.3 The timing argument

Two clocks run against each other. The Medical Products Bill will bring SaMD and AI
into scope (`NZ-FIND-005`), and the technical file has to exist regardless. So the
question is not "how fast can we ship in NZ" but "can the technical file be ready
before the regime changes" — and if the answer is no, NZ-first delivers less than it
appears to.

Worth modelling honestly. If the Bill lands with transition provisions for existing
notified devices, early notification is valuable. If it does not, the advantage is
smaller than the effort.

### 4.4 The registrar question

You are taking up a Medical Registrar post in New Zealand. That is an asset — local
clinical credibility, network, and a reason to be in-country — and a governance
exposure. Any arrangement where you are simultaneously a clinician in a health service
and a director of a company supplying software into that service needs conflict
declaration and probably employer sign-off before conversations begin. Get that clean
first; it is much harder to retrofit than to declare.

---

## 5 — Sequenced actions

| ID | Task | Gate |
|---|---|---|
| `NZ-TASK-001` | Engage New Zealand regulatory counsel. Confirm `NZ-FIND-001..009`, the notification window, sponsor structure, and expected classification. | `NZ-GATE-0` |
| `NZ-TASK-002` | Resolve the sponsor question: Arepo NZ entity vs contracted sponsor. Cost, control and liability differ materially. | `NZ-GATE-0` |
| `NZ-TASK-003` | Declare the registrar/director conflict to the employer; obtain written position before any commercial conversation in-country. | `NZ-GATE-0` |
| `NZ-TASK-004` | Model the Medical Products Bill timing against technical-file readiness (`NZ-WATCH-001`). Decide whether NZ-first survives the analysis. | `NZ-GATE-0` |
| `NZ-TASK-005` | NZ privacy, health information, and Māori data sovereignty assessment — distinct from the Australian work. | `NZ-GATE-1` |
| `NZ-TASK-006` | Technical file assembled to the same standard as the Australian submission. This is `TASK-REG-006..014`, not a separate effort. | `NZ-GATE-1` |
| `NZ-TASK-007` | Post-market system operating **before** supply: complaints, adverse events, recall capability (`NZ-FIND-008`). | `NZ-GATE-1` |
| `NZ-TASK-008` | WAND notification. | `NZ-GATE-2` |

**`NZ-GATE-0`:** counsel attested; sponsor decided; conflict cleared; timing modelled.
**`NZ-GATE-1`:** technical file complete; post-market operating; privacy cleared.
**`NZ-GATE-2`:** notified; first supply.

`NZ-GATE-1` is deliberately equivalent to REG-POSTURE `GATE-002` plus the technical
file. New Zealand's lighter *entry* does not license lighter *controls*, and
`NZ-FIND-008` is the reason.

---

## 6 — Assumptions and questions

| ID | Item | Party | Status |
|---|---|---|---|
| `NZ-ASSUME-001` | The notification window and its trigger point | NZ counsel | OPEN |
| `NZ-ASSUME-002` | Mākoha's NZ classification and whether any WAND exemption applies | NZ counsel | OPEN |
| `NZ-ASSUME-003` | Sponsor structure and liability allocation | NZ counsel | OPEN |
| `NZ-ASSUME-004` | Whether NZ clinical evidence will be accepted in an Australian conformity assessment, and on what conditions | AU counsel | OPEN |
| `NZ-Q-001` | Does the Medical Products Bill contemplate transition for devices already notified? | NZ counsel / MoH | OPEN |
| `NZ-Q-002` | Registrar/director conflict position | Employer | OPEN |
| `NZ-Q-003` | Does the Governance Layer (MAK-GOV) need WAND notification, or is it out of scope as a non-device in NZ too? | NZ counsel | OPEN |

`NZ-ASSUME-004` is the highest-value question in this brief. If NZ evidence does not
transfer, NZ-first is a revenue strategy rather than an evidence strategy — still
legitimate, but a different case, and it should be argued as one.

---

## 7 — Watch items

| ID | Item | Cadence |
|---|---|---|
| `NZ-WATCH-001` | Medical Products Bill — introduction, scope, SaMD and AI provisions, transition arrangements | Monthly until introduced |
| `NZ-WATCH-002` | Medsafe guidance on software and AI under the interim regime | Quarterly |
| `NZ-WATCH-003` | PHARMAC centralised device procurement — changes the buyer, not the regulator | Semi-annually |

---

## 8 — Sources

| ID | Source | Currency |
|---|---|---|
| `NZ-SRC-001` | Medsafe, GRTPNZ — overview of therapeutic product regulation; product and activity controls for medical devices | Current under Medicines Act 1981 |
| `NZ-SRC-002` | Commercial regulatory-consultancy guides to NZ device registration and WAND | 2025–2026. **Secondary — vendor-authored** |
| `NZ-SRC-003` | Beehive releases: TPA repeal announced and repeal bill passed | Current |
| `NZ-SRC-004` | Ministry of Health Regulatory Impact Statement — product and activity controls for medical devices | October 2024 |
| `NZ-SRC-005` | Medical Products Bill Cabinet material — July 2025 agreement to regulate SaMD including AI for therapeutic purpose | 2025 |

**Confidence note.** `NZ-FIND-001`, `003`, `004` and `009` rest on primary government
sources and are high confidence. `NZ-FIND-002` (the window) shows a genuine
discrepancy across sources and must be verified. `NZ-FIND-006` and `007` rest partly
on consultancy material with an interest in selling sponsorship services — directionally
consistent with the primary sources, but confirm with counsel rather than with a
vendor.

---

*Advisory only. New Zealand counsel must confirm before any commitment. Nothing here
authorises supply.*
