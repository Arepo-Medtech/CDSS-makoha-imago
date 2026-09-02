---
doc_id: REG-US
title: "Mākoha — Regulatory Posture: UNITED STATES (FDA)"
jurisdiction: UNITED STATES
regulator: U.S. Food and Drug Administration, Center for Devices and Radiological Health (CDRH)
version: 1.0
status: DRAFT
authority: ADVISORY_ONLY
entity: Arepo Medtech Pty Ltd
product: Mākoha
date_issued: 2026-09-02
guidance_currency_date: 2026-09-02
standalone_rule: "REPLETE-STANDALONE. This document carries the complete standards stack, the US regulatory instruments and every US obligation itself. It never says 'see REG-POSTURE' for anything a reader needs in order to act in the United States. Companion documents follow the same rule and repeat the stack by design."
companions:
  - "REG-POSTURE v1.2 — AUSTRALIA (TGA)"
  - "REG-NZ v1.1 — NEW ZEALAND (Medsafe)"
  - "REG-EU v1.0 — EUROPEAN UNION (MDR 2017/745)"
sequence_position: "Later — after New Zealand (first) and Australia (second), per the programme's working jurisdiction sequence (Australian TASK-REG-022 / Q-REG-008; DEC pending)"
runtime_register: "R30 — Regulatory Posture Register; US-* rows seeded in R30.2"
id_prefixes: [US-FIND, US-OBL, US-STD, US-REG, US-ASSUME, US-TASK, US-GATE, US-WATCH, US-Q, US-SRC]
attestation_required: true
attestation_by: US FDA regulatory counsel / regulatory affairs consultant
---

# Mākoha — Regulatory Posture: UNITED STATES (FDA)

**Jurisdiction:** UNITED STATES · FDA / CDRH · Federal Food, Drug, and Cosmetic Act; Title 21 CFR
**Prepared for:** Arepo Medtech Pty Ltd
**Version:** 1.0 · 2 September 2026
**Status:** Working document. Not regulatory advice. Requires US regulatory counsel attestation before any commitment.

> **How to read this document.** It is the United States authority for Mākoha's
> regulatory posture and is written to stand alone. The US is a **later** jurisdiction
> in the programme's working sequence; this document exists now because the standards
> stack, the records discipline and the clinical-evidence design must be US-capable from
> the first artifact if the later submission is to be author-once rather than
> re-created. Every finding is carried as an assumption requiring US counsel
> attestation. Items that originate from the author's analysis rather than an FDA
> instrument carry **[recommendation]** and a confidence tag. **The FDA instruments
> named here were current to the author's knowledge; several have moved recently
> (CDS guidance revision January 2026; QMSR effective February 2026; cybersecurity
> guidance revision 2025) and each carries a currency flag that must be discharged by
> reading the primary before `US-GATE-000`.**

---

## §0 Conventions

### 0.1 Authority

Advisory input only. Cannot be cited as evidence for a DONE. Every material finding
about US regulation is carried as a `US-ASSUME-*` requiring written attestation from
US counsel or a qualified US regulatory affairs professional before reliance.

### 0.2 ID scheme

| Prefix | Meaning | Closure |
|---|---|---|
| `US-FIND-nnn` | Finding about US regulation | Superseded or attested |
| `US-OBL-nnn` | Standing US obligation | Never closes |
| `US-STD-nnn` | Standard in scope, with FDA recognition status | Retired only by pathway change |
| `US-REG-nnn` | Statutory or regulatory instrument (FD&C Act section; CFR part; guidance) | Retired when superseded |
| `US-ASSUME-nnn` | Assumption requiring external closure | Written attestation, named party, dated |
| `US-TASK-nnn` | Sequenced work item | DONE-with-evidence or typed HALT |
| `US-GATE-nnn` | Blocking gate | All predecessors DONE-with-evidence |
| `US-WATCH-nnn` | External change to monitor | Never closes; cadence stated |
| `US-Q-nnn` | Open question | Answer in writing |
| `US-SRC-nnn` | Source | Retired when superseded |

### 0.3 Status vocabulary

`OPEN` · `IN-PROGRESS` · `DONE-WITH-EVIDENCE` · `HALT-TYPED` · `SUPERSEDED` ·
`ATTESTED` · `REFUTED`. Assumptions hold only `OPEN`, `ATTESTED`, `REFUTED`,
`SUPERSEDED` and never close by internal reasoning. R30 crosswalk as in the Australian
posture: `IN-PROGRESS` → `OPEN`; `DONE-WITH-EVIDENCE`/`SUPERSEDED` → `CLOSED`.

### 0.4 Provenance and confidence tags

| Tag | Meaning |
|---|---|
| **[FDA-sourced]** | Traceable to an FD&C Act section, CFR part or FDA guidance named in §11 |
| **[recommendation]** | Author's analysis; requires counsel/RA confirmation |
| **[confidence: high / medium / low]** | Author's confidence the item is correctly stated and currently in force |
| **[currency: verify]** | Instrument known to have been revised recently; read the primary before reliance |

### 0.5 Firewall note

No case content, no evidence-library values, no sensitivities, specificities or
likelihood ratios. Not a source for clinical content.

### 0.6 Jurisdiction declaration and the replete-standalone rule

**This document is the UNITED STATES.** The four jurisdiction documents share one
standards stack and one architecture; they do not share text by reference. Each carries
the complete stack with that regulator's recognition status and its own obligations,
gates, tasks, assumptions, questions, watch items and sources. Shared programme
artifacts — intended purpose statement, ISO 14971 risk file, IEC 62304 lifecycle
records, technical documentation — are built once and projected per regulator. A
change to the shared stack is made in all four documents in the same cycle, or the
divergence is logged in the wrapper (MAK-ANT) as a signal.

---

## §1 Headline

**Mākoha is a device in the United States, and the reason is the same as in Australia:
the diagnostic function, not the AI.** The 21st Century Cures Act carved certain
clinical decision support software out of the device definition (FD&C Act §520(o)(1)(E)),
but only where all four statutory criteria are met. The fourth — that the software is
intended to enable the health care professional to **independently review the basis**
for its recommendations so that they do not rely primarily on it — is the US analogue
of the TGA's glass-box test, and FDA's guidance has read it to exclude software that
outputs a probability, risk score or specific diagnostic output for an individual
patient from a model the clinician cannot verify. A ranked differential with posterior
probabilities is that.

Two US-specific consequences matter more than the classification itself:

1. **The US is where the records discipline is tested.** 21 CFR Part 11 governs the
   electronic records and signatures that evidence design control and release decisions.
   The programme's "automated systems propose, humans release" rule is evidenced through
   e-signatures; if those records are not Part 11-capable from the first artifact, the
   US file is re-created rather than projected.
2. **The US is where AI-specific instruments are most developed.** FDA's predetermined
   change control plan (PCCP) framework, its AI-enabled device lifecycle guidance, its
   transparency principles and the section 524B cyber-device requirements are the most
   specific regulatory texts anywhere on how an AI-enabled SaMD is built, changed and
   secured. Building to them early costs little and de-risks all three other
   jurisdictions.

Nothing in this document is a plan to enter the US soon. It is a plan to avoid
foreclosing the US by building the wrong records now.

---

## §2 Findings

| ID | Finding | Status | Source |
|---|---|---|---|
| `US-FIND-001` | A software function is a device if it meets the FD&C Act §201(h) definition — intended for use in the diagnosis of disease or other conditions, or in the cure, mitigation, treatment or prevention of disease. Mākoha's intended purpose (diagnostic information for clinicians) meets it on its face. **[FDA-sourced; high]** | OPEN | `US-SRC-001` |
| `US-FIND-002` | §520(o)(1)(E) excludes CDS software from the device definition only where **all four** criteria hold: (1) not intended to acquire, process or analyse a medical image or a signal from an IVD or a pattern/signal acquisition system; (2) intended to display, analyse or print medical information about a patient or other medical information; (3) intended to support or provide recommendations to a health care professional about prevention, diagnosis or treatment; (4) intended to enable the HCP to independently review the basis for the recommendations so that it is not the intent that the HCP rely primarily on them. **[FDA-sourced; high]** | OPEN | `US-SRC-001`, `US-SRC-002` |
| `US-FIND-003` | Mākoha is assessed as **not meeting criterion (4)** and, on FDA's 2022 reading, **not criterion (3)**: a ranked differential with posteriors is a specific diagnostic output for a specific patient from a proprietary model, not a recommendation the clinician can independently verify from its stated basis. The programme's reviewable-basis commitment (Australian `REG-KEEP-002`) strengthens the transparency argument but does not make the posterior independently verifiable. **[FDA-sourced (2022 guidance); medium — the January 2026 revision of the CDS guidance must be read before this finding is relied upon; `US-WATCH-001`]** | OPEN | `US-SRC-002` |
| `US-FIND-004` | Any **patient-facing** software function is outside §520(o)(1)(E) regardless of the other criteria, because the criteria address recommendations to health care professionals. The patient surface, if it does more than intake/consent/logistics, is a device function in the US. Aligns with the Australian interim rule (patient-face work beyond the J-3-safe subset is Blocked). **[FDA-sourced; high]** | OPEN | `US-SRC-002` |
| `US-FIND-005` | Expected classification is **Class II**. Diagnostic CDS software of this kind has reached market through **De Novo** (creating a new classification regulation and product code) where no predicate exists, and through **510(k)** where one does. Which applies depends on the predicate landscape at the time of submission and is a Pre-Submission question. Class III (PMA) is not expected for a clinician-facing differential-support tool. **[FDA-sourced (pathway mechanics); medium (pathway choice)]** | OPEN | `US-SRC-003`, `US-SRC-004` |
| `US-FIND-006` | The Quality Management System Regulation (QMSR), 21 CFR Part 820 as amended, took effect **2 February 2026** and incorporates **ISO 13485:2016 by reference**, with FDA-specific additions (Part 11 records; Part 803 MDR; Part 806 corrections and removals; Part 830 UDI; labelling and packaging controls). An ISO 13485 QMS is therefore the US QMS with a thin overlay — the same author-once lever as the Australian deemed-conformity Order. **[FDA-sourced; high]** | OPEN | `US-SRC-005` |
| `US-FIND-007` | FDA accepts **MDSAP** audit reports in lieu of routine FDA inspection (not in lieu of for-cause inspection). A single MDSAP audit covers the US, Australia (TGA accepts as conformity-assessment evidence), Canada (mandatory), Brazil and Japan. **[FDA-sourced; high]** | OPEN | `US-SRC-006` |
| `US-FIND-008` | Mākoha is a **cyber device** under FD&C Act §524B (added by FDORA, 2022; in force for submissions from 29 March 2023): it includes software, connects to the internet, and could be vulnerable to cybersecurity threats. Consequence: the premarket submission **must** include a plan to monitor, identify and address postmarket vulnerabilities (including coordinated disclosure), evidence of secure-by-design and reasonable assurance of cybersecurity, and a **software bill of materials** covering commercial, open-source and off-the-shelf components. **[FDA-sourced; high]** | OPEN | `US-SRC-007`, `US-SRC-008` |
| `US-FIND-009` | Software documentation level in the premarket submission is **Basic** or **Enhanced** per the 2023 software guidance; Enhanced applies where a failure or flaw could present a hazardous situation with probable serious injury or death, or where the device is a constituent of a combination product. Expect **Enhanced** to be the conservative assumption for a diagnostic SaMD bearing on serious conditions; confirm in the Pre-Sub. **[FDA-sourced; high (rule) / medium (level)]** | OPEN | `US-SRC-009` |
| `US-FIND-010` | A **Predetermined Change Control Plan** (PCCP) may be authorised in a marketing submission for an AI-enabled device software function, pre-authorising specified modifications (description of modifications, modification protocol, impact assessment) so they do not require a new submission. This is a US-only instrument with no TGA, Medsafe or EU MDR equivalent; **do not assume it transfers.** For Mākoha it is the mechanism by which evidence-library updates and model re-training could be pre-authorised. **[FDA-sourced; high]** | OPEN | `US-SRC-010` |
| `US-FIND-011` | FDA's AI-enabled device lifecycle guidance (draft, January 2025) and the GMLP and transparency guiding principles set expectations for the marketing submission that go beyond IEC 62304: data management (training/tuning/test data description, representativeness, independence), model description, performance validation with subgroup analysis, usability and transparency (a model card-style "device description" for users), cybersecurity for AI-specific threats (data poisoning, model inversion), and postmarket performance monitoring. **[FDA-sourced; high (principles) / medium (draft status)]** | OPEN | `US-SRC-011`, `US-SRC-012` |
| `US-FIND-012` | Clinical data collected outside the US is acceptable in support of a submission where the study was conducted to good clinical practice (21 CFR 812.28) — in practice, ISO 14155 conduct with ethics-committee approval, informed consent and data of adequate quality. **New Zealand and Australian clinical evidence therefore transfers to the US file** on the same conditions that make it transfer to the TGA, provided intended purpose is held constant. **[FDA-sourced; high]** | OPEN | `US-SRC-013` |
| `US-FIND-013` | 21 CFR Part 11 applies to electronic records and signatures created, modified, maintained, archived, retrieved or transmitted under any FDA records requirement — including QMSR design-history and device-master records. Requirements: validated systems, secure computer-generated time-stamped audit trails, unique user attribution, signature manifestation (printed name, date/time, meaning), signature/record linking, and controls for open systems. **[FDA-sourced; high]** | OPEN | `US-SRC-014` |
| `US-FIND-014` | Arepo, as a foreign manufacturer, must register its establishment and list the device (21 CFR 807), designate a **US Agent** resident in the US (21 CFR 807.40), and comply with Part 803 medical device reporting, Part 806 corrections and removals, Part 830 UDI and Part 801 labelling from the date of US marketing. **[FDA-sourced; high]** | OPEN | `US-SRC-015` |
| `US-FIND-015` | Privacy in the US is sectoral. If Mākoha is supplied to HIPAA covered entities (practices, pharmacies as providers), Arepo is a **business associate** and needs a Business Associate Agreement and HIPAA Security Rule compliance. A patient-facing function that is not within a covered entity's scope falls under the **FTC Act §5** and the **FTC Health Breach Notification Rule** (as amended 2024, expressly covering health apps), plus state laws (California CCPA/CPRA; Washington My Health My Data Act; others). **HIPAA compliance is not evidence of Australian or New Zealand privacy compliance, and vice versa.** **[US-sourced; high]** | OPEN | `US-SRC-016` |
| `US-FIND-016` | If Mākoha is delivered through an ONC-certified health IT module (EHR integration), the developer of that module carries **HTI-1 decision-support-intervention transparency** obligations — "source attributes" for predictive DSIs (training data, performance, fairness, update cadence). Not an FDA requirement and not on Arepo directly, but a US EHR partner will pass it down contractually, and the model-card content in `US-FIND-011` satisfies most of it. **[US-sourced; medium]** | OPEN | `US-SRC-017` |

---

## §3 Classification and pathway

### 3.1 Device status

Device (`US-FIND-001..004`). The §520(o)(1)(E) carve-out is assessed unavailable for
the same structural reason the Australian CDSS exemption is: the output is a
probabilistic diagnostic contribution from a proprietary model. `US-ASSUME-001` carries
this; the January 2026 CDS guidance revision (`US-WATCH-001`) is the one thing that
could move it, and it is read before the assumption is put to counsel.

### 3.2 The non-device Governance Layer

The Governance Layer (organisational-conformance analysis, no clinical write path, no
patient-specific output) is assessed as **not a device** in the US on the same
reasoning as Australia: it is not intended for the diagnosis or treatment of an
individual, and FDA's software-functions policy treats administrative and
quality-management software as outside device regulation. **[recommendation; medium]**
Carried as `US-ASSUME-006`. If it is ever repositioned to analyse individual patient
decisions in a way that influences current care, it becomes a device.

### 3.3 Class and pathway

Class II expected (`US-FIND-005`). Pathway is a Pre-Submission (Q-Sub) question:

| Route | When | What it requires |
|---|---|---|
| **De Novo** (21 CFR 860 Subpart D) | No legally marketed predicate with the same intended use and technological characteristics | Full risk-based classification request; clinical performance data expected; results in a new classification regulation with special controls that then bind the product — and become the predicate for others |
| **510(k)** (21 CFR 807 Subpart E) | A predicate exists | Substantial equivalence to the predicate; software documentation per `US-FIND-009`; may still need clinical performance data for an AI-enabled function |
| **PMA** | Class III | Not expected |

Working assumption for planning: **De Novo, Enhanced documentation level, clinical
performance study required, PCCP included.** Carried as `US-ASSUME-002`.

### 3.4 IMDRF risk category

Under IMDRF N12 (`US-STD-025`), Mākoha informs clinical management (not drives or
treats/diagnoses directly) in a range of healthcare situations from non-serious to
serious. Category **II** (serious / inform) is the conservative planning category; it
is the same category the Australian classification reasoning lands on. FDA uses N12
vocabulary in its SaMD guidance but does not classify by it; the category is the
argument structure, not the class.

---

## §4 Obligations register — UNITED STATES

Non-closing. Attach from the date of US marketing unless stated otherwise.

| ID | Obligation | Instrument | Note |
|---|---|---|---|
| `US-OBL-001` | Operate a QMS meeting the QMSR (ISO 13485:2016 + FDA additions) | 21 CFR 820 (QMSR) | The ISO 13485 QMS built for Australia and New Zealand **is** this, with the overlay in `US-OBL-002..005` |
| `US-OBL-002` | Electronic records and signatures compliant with Part 11 | 21 CFR 11 | From the **first** design-control record, not from US entry — the record cannot be retro-fitted. The Ketryx e-signature and audit-trail claims are verified against Part 11 as part of tool validation |
| `US-OBL-003` | Medical device reporting — deaths, serious injuries, malfunctions | 21 CFR 803 | 30-day and 5-day reports; complaint files per QMSR; the same adverse-event system that serves Medsafe and TGA, with US timeframes |
| `US-OBL-004` | Reports of corrections and removals | 21 CFR 806 | A software update issued to reduce a risk to health is a correction and is reportable |
| `US-OBL-005` | Unique Device Identification | 21 CFR 830; 801 Subpart B | UDI for a SaMD is carried in the software (about screen / accessible display) and in the GUDID |
| `US-OBL-006` | Establishment registration and device listing; US Agent | 21 CFR 807; 807.40 | Annual registration fee; US Agent must be a US resident or business |
| `US-OBL-007` | Labelling | 21 CFR 801 | IFU, indications for use statement matching the cleared/granted intended use exactly, UDI, manufacturer and US agent particulars |
| `US-OBL-008` | Cyber device requirements | FD&C Act §524B | SBOM; postmarket vulnerability monitoring and coordinated disclosure plan; secure product development framework evidence; patch/update pathway with timelines; all carried in the submission and maintained thereafter |
| `US-OBL-009` | Design controls and design history file | 21 CFR 820 via ISO 13485 §7.3 | The Ketryx design-controls system is the DHF; traceability requirement → risk → test → release generated, not assembled |
| `US-OBL-010` | Software validation of production and quality-system software | QMSR (ISO 13485 §4.1.6, §7.5.6) + CSA guidance | Tool validation of the authoring surface, Ketryx and the release channel — same obligation as the Australian `STD-013`, evidenced the same way |
| `US-OBL-011` | Postmarket performance monitoring of the AI-enabled function | AI lifecycle guidance; PCCP conditions if granted | Drift monitoring, subgroup performance, triggers for re-evaluation; where a PCCP is granted, the modification protocol becomes a binding condition |
| `US-OBL-012` | Privacy and security of health information | HIPAA (as business associate); FTC Act §5; FTC HBNR; state law | BAA with each covered-entity customer; HIPAA Security Rule risk analysis; breach notification duties; **separate from and not equivalent to** APP or NZ HIPC compliance |
| `US-OBL-013` | Claims discipline | FD&C Act misbranding provisions; 21 CFR 801; FTC Act | Promotional claims must not exceed the cleared/granted indications for use. The versioned claims inventory built for Australia is diffed against the US indications statement as well |
| `US-OBL-014` **[recommendation; high]** | Author-once records rule | Programme rule | Every shared artifact (risk file, lifecycle records, usability file, security file, SBOM, clinical evidence, technical documentation) is generated in a form that satisfies the US instruments above **now**, so the US submission is a projection. Specifically: Part 11-capable records; SBOM in CycloneDX or SPDX with the §524B-required fields; software documentation organised so the Enhanced-level document set can be extracted; clinical evidence to ISO 14155 |

---

## §5 Standards stack — UNITED STATES

FDA maintains a **Recognized Consensus Standards** database; a declaration of
conformity to a recognised standard (with the recognised edition and any recognised
extent) is accepted in a premarket submission without further justification. Column
"FDA status" records recognition to the author's knowledge; **recognition numbers and
recognised editions must be confirmed against the database before the submission**
(`US-WATCH-004`). Editions are pinned. Priority 1 = the submission cannot be assembled
without it; 2 = expected in the software/risk/usability documentation; 3 = expected
for the §524B cyber case; 4 = situational.

### 5.1 Core lifecycle and quality

| ID | Standard | Edition | Role in the US submission | FDA status | Priority |
|---|---|---|---|---|---|
| `US-STD-001` | ISO 13485 | :2016 | The QMS — incorporated by reference into the QMSR (`US-FIND-006`) | Incorporated by reference in 21 CFR 820 | **1** |
| `US-STD-002` | IEC 62304 | :2006 + A1:2015 | Software lifecycle; the software documentation in the submission (`US-FIND-009`) maps onto its outputs (SRS, architecture, detailed design, V&V, unresolved anomalies, revision history, SOUP) | Recognised | **1** |
| `US-STD-003` | ISO 14971 | :2019 | Risk management file; the submission's risk management report and hazard analysis | Recognised | **1** |
| `US-STD-004` | IEC 62366-1 | :2015 + A1:2020 | Usability engineering — FDA additionally applies its own human-factors guidance (`US-REG-010`); the 62366-1 file is the input, the HF validation report is the submission deliverable | Recognised | **2** |
| `US-STD-005` | IEC 82304-1 | :2016 | Health software product safety — product-level requirements; useful frame for the device description | Recognised | **2** |
| `US-STD-006` | BS/AAMI 34971 | :2023 (AAMI CR34971 consensus report) | ISO 14971 applied to ML — the ML risk hook behind `US-FIND-011` expectations | Recognised as consensus report **[verify]** | **2** |
| `US-STD-013` | IEC 62304 §5.1.4 + ISO 13485 §4.1.6 + CSA guidance | as above | Tool validation — the US frames this as Computer Software Assurance: risk-based, intended-use testing, vendor documentation leveraged. Ketryx's validation package is supplier evidence, not a substitute for Arepo's intended-use assurance | CSA guidance (`US-REG-011`) | **2** |

### 5.2 Cyber security and information security

| ID | Standard | Edition | Role in the US submission | FDA status | Priority |
|---|---|---|---|---|---|
| `US-STD-007` | ANSI/AAMI SW96 | :2023 | Security risk management — the security risk management report FDA's cyber guidance expects beside the safety risk file | Recognised | 3 |
| `US-STD-008` | IEC 81001-5-1 | :2021 | Secure product development framework evidence — FDA's cyber guidance names it as an acceptable SPDF basis | Recognised | 3 |
| `US-STD-009` | ISO/IEC 29147 and ISO/IEC 30111 | 29147:2018; 30111:2019 | Coordinated vulnerability disclosure and handling — the §524B postmarket plan | Recognised **[verify current edition recognised]** | 3 |
| `US-STD-010` | ISO 27799 | :2016 | Health information security controls — supports the HIPAA Security Rule risk analysis; not an FDA submission item | Not recognised (not device-specific) | 3 |
| `US-STD-011` | IEC 80001-1 | :2021 | Health IT network risk management — deployment-side; useful for customer security questionnaires | Recognised | 4 |
| `US-STD-012` | UL 2900-2-1 | :2017 | Network-connectable healthcare product security testing — penetration-test yardstick; FDA-recognised | Recognised | 4 |

### 5.3 Additional rows load-bearing in the US **[recommendation unless stated]**

| ID | Standard | Edition | Why it is load-bearing in the US | FDA status | Priority | Confidence |
|---|---|---|---|---|---|---|
| `US-STD-014` | ISO/TR 24971 | :2020 | Guidance on ISO 14971 — the risk file's method | Recognised (informational) **[verify]** | **2** | high |
| `US-STD-015` | IEC/TR 80002-1 | :2009 | ISO 14971 applied to software — bridge to the software safety classification and the FDA documentation level | Recognised | **2** | high |
| `US-STD-016` | AAMI TIR45 | :2023 | Agile in medical device software — FDA-recognised; the reference for a continuously integrated build being a compliant lifecycle | Recognised | **2** | high |
| `US-STD-017` | AAMI TIR57 | :2016 (R2023) | Device security risk management principles — the cited method for the threat model FDA's cyber guidance requires | Recognised | 3 | high |
| `US-STD-018` | ISO 14155 | :2020 | Clinical investigation GCP — the conduct standard that makes foreign (NZ/AU) clinical data admissible (`US-FIND-012`) | Recognised | **1** | high |
| `US-STD-019` | ISO 20417 | :2021 | Information supplied by the manufacturer — IFU content; FDA labelling rules (21 CFR 801) govern, 20417 organises | Recognised **[verify]** | **2** | medium |
| `US-STD-020` | ISO 15223-1 | :2021 | Symbols — FDA accepts recognised-standard symbols on labelling without adjacent text (21 CFR 801.15) | Recognised | 3 | high |
| `US-STD-021` | ISO/IEC 42001 | :2023 | AI management system — not an FDA item; alignment supports the "organisational" GMLP principles and customer procurement | Not recognised | 4 | medium |
| `US-STD-022` | ISO/IEC 23894 | :2023 | AI risk management guidance — companion to 14971/34971 for the AI lifecycle documentation | Not recognised | 4 | medium |
| `US-STD-023` | IEC 60601-4-5 | :2021 | Security capability levels — only if claimed | Recognised | 4 | medium |
| `US-STD-024` | ISO/IEC 27001 | :2022 | ISMS — not an FDA item; HIPAA Security Rule risk analysis maps onto it; US enterprise health customers routinely require SOC 2 Type II or 27001 | Not recognised | 4 | high |
| `US-STD-025` | IMDRF SaMD documents | N10:2013, N12:2014, N23:2015, N41:2017 | FDA co-authored these; its SaMD guidance uses N12 risk categories and N41 clinical-evaluation structure (valid clinical association, analytical validation, clinical validation) | Adopted as FDA guidance (N41) | **2** | high |
| `US-STD-026` | IMDRF cyber and ML documents | N60:2020, N70:2023, N73:2023, N88:2025 | N60/N73 are the basis of FDA's cyber guidance and SBOM expectations; N88 the GMLP reference | Referenced in FDA guidance | 3 | medium (N88 currency to verify) |
| `US-STD-027` | NIST Cybersecurity Framework 2.0; NIST SP 800-53 / 800-218 (SSDF) | CSF 2.0:2024; SSDF 1.1:2022 | Referenced by FDA cyber guidance and by US customers; SSDF is the secure-development yardstick US procurement uses alongside 81001-5-1 | Referenced | 3 | medium |

### 5.4 Considered and not adopted

| Standard | Reason |
|---|---|
| IEC 60601-1 family (other than 60601-4-5) | No hardware |
| ISO/IEC TS 82304-2 | Consumer app label; not an FDA item |
| ANSI/AAMI/ISO 15189, CLIA | Laboratory; not applicable |
| ISO 9001 | Superseded by ISO 13485 / QMSR |

---

## §6 US regulatory instruments register

Statute, regulation and guidance that the submission and the postmarket system are
built against. Guidance is not binding but describes FDA's current thinking; deviating
from it is possible with justification and is a Pre-Sub conversation.

| ID | Instrument | Type | Bearing on Mākoha | Currency |
|---|---|---|---|---|
| `US-REG-001` | FD&C Act §201(h) — device definition | Statute | `US-FIND-001` | Stable |
| `US-REG-002` | FD&C Act §520(o)(1)(E) — CDS software exclusion (21st Century Cures Act 2016) | Statute | `US-FIND-002..004` | Stable |
| `US-REG-003` | FDA guidance — *Clinical Decision Support Software* | Guidance | Interpretation of the four criteria; **revised 6 January 2026** — the revision must be read before `US-ASSUME-001` is put to counsel | **[currency: verify]** |
| `US-REG-004` | FDA guidance — *Policy for Device Software Functions and Mobile Medical Applications* | Guidance | Enforcement-discretion categories; confirms administrative/quality software is outside device regulation (Governance Layer, `US-ASSUME-006`) | Sept 2022 **[verify]** |
| `US-REG-005` | 21 CFR Part 820 — Quality Management System Regulation | Regulation | `US-FIND-006`; `US-OBL-001` | Effective 2 Feb 2026 |
| `US-REG-006` | 21 CFR Part 11 — Electronic Records; Electronic Signatures (+ 2003 scope-and-application guidance) | Regulation | `US-FIND-013`; `US-OBL-002` | Stable |
| `US-REG-007` | 21 CFR Part 807 (registration, listing, 510(k)); 21 CFR 860 Subpart D (De Novo) | Regulation | `US-FIND-005`; `US-OBL-006` | Stable |
| `US-REG-008` | 21 CFR Parts 803, 806, 801, 830 | Regulation | `US-OBL-003..005`, `US-OBL-007` | Stable |
| `US-REG-009` | FD&C Act §524B — Ensuring Cybersecurity of Devices (FDORA 2022) + FDA guidance *Cybersecurity in Medical Devices: Quality System Considerations and Content of Premarket Submissions* | Statute + guidance | `US-FIND-008`; `US-OBL-008` | Statute stable; guidance **revised 2025 [currency: verify]** |
| `US-REG-010` | FDA guidance — *Content of Premarket Submissions for Device Software Functions* (June 2023); *Applying Human Factors and Usability Engineering to Medical Devices* (2016; draft revision 2022); *Off-the-Shelf Software Use in Medical Devices* (2023) | Guidance | `US-FIND-009`; software and HF documentation; SOUP/OTS documentation for the AI service vendor and model | 2023 |
| `US-REG-011` | FDA guidance — *Computer Software Assurance for Production and Quality System Software* | Guidance | `US-STD-013`; tool validation approach | Final **2025 [currency: verify]** |
| `US-REG-012` | FDA guidance — *Marketing Submission Recommendations for a Predetermined Change Control Plan for AI-Enabled Device Software Functions* (final, December 2024) | Guidance | `US-FIND-010` | Dec 2024 |
| `US-REG-013` | FDA draft guidance — *AI-Enabled Device Software Functions: Lifecycle Management and Marketing Submission Recommendations* (January 2025); *Good Machine Learning Practice* guiding principles (2021); *Transparency for Machine Learning-Enabled Medical Devices* guiding principles (2024) | Draft guidance + principles | `US-FIND-011`; `US-OBL-011` | Draft; **check for finalisation [currency: verify]** |
| `US-REG-014` | 21 CFR Parts 812 (IDE), 50 (informed consent), 56 (IRB); 21 CFR 812.28 (foreign clinical data) | Regulation | `US-FIND-012`; any US clinical study; admissibility of NZ/AU evidence | Stable |
| `US-REG-015` | HIPAA Privacy, Security and Breach Notification Rules (45 CFR 160, 164); FTC Act §5; FTC Health Breach Notification Rule (16 CFR 318, as amended 2024); state privacy laws | Regulation | `US-FIND-015`; `US-OBL-012` | HIPAA Security Rule **amendment proposed 2025 [watch]** |
| `US-REG-016` | ONC HTI-1 Final Rule — decision support interventions (45 CFR 170.315(b)(11)) | Regulation (on certified health IT developers) | `US-FIND-016` | 2024; **HTI-2/HTI-4 amendments [watch]** |
| `US-REG-017` | MDSAP programme documents | Programme | `US-FIND-007` | Stable |

---

## §7 Sequenced plan

The US is a later jurisdiction. The tasks below are split into **now** (things that
must be done during the NZ/AU build so the US remains a projection) and **at entry**
(things done when the US decision is taken).

### Gates

| ID | Gate | Predecessors | Meaning |
|---|---|---|---|
| `US-GATE-000` | US-capable foundations | `US-TASK-001..004` | Records, SBOM, clinical-evidence design and documentation structure are US-capable; no US-specific spend yet |
| `US-GATE-001` | US decision and Pre-Sub | `US-TASK-005..008` | Counsel attested; Pre-Sub held; pathway, documentation level and PCCP scope agreed with FDA in writing (Pre-Sub feedback) |
| `US-GATE-002` | Submission | `US-TASK-009..012` | De Novo / 510(k) submitted with PCCP; US Agent and registration in place |
| `US-GATE-003` | US market | `US-TASK-013` | Granted/cleared; listed; postmarket system operating with US timeframes |

### Tasks — now (during NZ/AU build)

| ID | Task | Gate |
|---|---|---|
| `US-TASK-001` | Make every design-control record Part 11-capable from the first artifact: unique attribution, MFA-backed e-signature with meaning and timestamp, append-only audit trail, validated system. Verify the Ketryx claim by intended-use test (an AI-drafted item cannot reach a controlled state without a named human signature). Evidence: tool-validation record. | `US-GATE-000` |
| `US-TASK-002` | Generate the SBOM in CycloneDX or SPDX with the §524B-expected fields (component name, version, supplier, level of support, end-of-support, known vulnerabilities) including manual entries for the AI service vendor and pinned model. Same SBOM serves TGA `OBL-004` and the Medsafe file. | `US-GATE-000` |
| `US-TASK-003` | Design the clinical evidence programme (NZ and AU) to ISO 14155 with ethics approval and informed consent so it satisfies 21 CFR 812.28; hold intended purpose constant across jurisdictions; pre-register subgroup analyses that FDA's AI guidance expects. | `US-GATE-000` |
| `US-TASK-004` | Organise the software documentation (IEC 62304 outputs) so the Enhanced-level document set of the 2023 software guidance can be generated as a projection: SRS, architecture, detailed design, V&V, unresolved anomalies, revision history, SOUP/OTS. Configure the Ketryx document template for it now, even if unused until entry. | `US-GATE-000` |

### Tasks — at entry

| ID | Task | Gate |
|---|---|---|
| `US-TASK-005` | Engage US regulatory counsel / RA consultant. Put `US-ASSUME-001..006` to them with the intended purpose statement, the reviewable-basis design, and the January 2026 CDS guidance read. | `US-GATE-001` |
| `US-TASK-006` | Predicate search and pathway analysis (De Novo vs 510(k)); draft indications for use statement; decide PCCP scope (evidence-library updates; model re-training; UI). | `US-GATE-001` |
| `US-TASK-007` | Pre-Submission (Q-Sub) to CDRH: pathway, classification, documentation level, clinical evidence sufficiency (including foreign data), PCCP scope, cyber documentation. | `US-GATE-001` |
| `US-TASK-008` | Decide QMS certification route if not already decided in Australia: MDSAP covers FDA routine inspection (`US-FIND-007`). | `US-GATE-001` |
| `US-TASK-009` | Cyber device package: SPDF evidence (81001-5-1), threat model (TIR57/STRIDE), security risk management report (SW96), SBOM, postmarket vulnerability and coordinated-disclosure plan (29147/30111), penetration test report, security architecture views per FDA cyber guidance. | `US-GATE-002` |
| `US-TASK-010` | AI-enabled function documentation per `US-FIND-011`: data management, model description, performance validation with subgroups, transparency/model card, postmarket performance monitoring plan, PCCP (description, modification protocol, impact assessment). | `US-GATE-002` |
| `US-TASK-011` | Human factors validation report per FDA HF guidance for each US-marketed surface; US labelling and IFU (21 CFR 801) with UDI. | `US-GATE-002` |
| `US-TASK-012` | Appoint US Agent; establishment registration and listing; HIPAA business-associate readiness (Security Rule risk analysis, BAA template); FTC HBNR readiness for any patient-facing function. Submit. | `US-GATE-002` |
| `US-TASK-013` | Postmarket: MDR (Part 803) and corrections/removals (Part 806) procedures with US timeframes; §524B vulnerability monitoring live; PCCP modification protocol operating; performance monitoring reporting. | `US-GATE-003` |

---

## §8 Assumptions

No `US-ASSUME-*` closes by internal reasoning.

| ID | Assumption | Attesting party | Blocks | Status |
|---|---|---|---|---|
| `US-ASSUME-001` | Mākoha is a device; the §520(o)(1)(E) CDS exclusion is unavailable (`US-FIND-003`), including after the January 2026 CDS guidance revision | US regulatory counsel | `US-GATE-001` | OPEN |
| `US-ASSUME-002` | Class II; De Novo (or 510(k) if a predicate is identified); Enhanced documentation level; clinical performance data required; PCCP available for the intended modifications | US counsel + Pre-Sub feedback | `US-GATE-001` | OPEN |
| `US-ASSUME-003` | Part 11 applies to the design-history and release records, and the Ketryx e-signature/audit-trail mechanism satisfies it as configured | US counsel + tool-validation evidence | `US-GATE-000` | OPEN |
| `US-ASSUME-004` | NZ/AU clinical evidence conducted to ISO 14155 is admissible under 21 CFR 812.28 without a US confirmatory study, given identical intended purpose | US counsel + Pre-Sub feedback | `US-GATE-001` | OPEN |
| `US-ASSUME-005` | Arepo is a HIPAA business associate for covered-entity customers and not itself a covered entity; patient-facing functions fall under FTC HBNR | US privacy counsel | `US-GATE-002` | OPEN |
| `US-ASSUME-006` | The Governance Layer is not a device in the US (administrative / quality-management software) | US regulatory counsel | Governance Layer US supply | OPEN |

---

## §9 Questions and watch items

### 9.1 Questions

| ID | Question | Who | Blocking |
|---|---|---|---|
| `US-Q-001` | What did the January 2026 CDS guidance revision change about criteria (3) and (4), and does a reviewable-basis design (inputs, cited likelihood ratios, logic shown) bring a probabilistic differential within the exclusion? | US counsel, after reading the primary | `US-ASSUME-001` |
| `US-Q-002` | Is there a legally marketed predicate for a clinician-facing differential-diagnosis support SaMD, or is De Novo the route? | RA consultant | `US-ASSUME-002` |
| `US-Q-003` | Will FDA accept a PCCP covering evidence-library updates and periodic model re-training within stated performance bounds, and what modification protocol would it expect? | Pre-Sub | `US-TASK-010` |
| `US-Q-004` | Documentation level: Basic or Enhanced for this intended use? | Pre-Sub | `US-TASK-004` |
| `US-Q-005` | Which MDSAP auditing organisation, and does the Australian decision (`TASK-REG-024` in the Australian posture) already settle this? | QMS lead | `US-TASK-008` |
| `US-Q-006` | Data residency and processing location for US patient data — US-region hosting as a HIPAA/customer precondition? | US privacy counsel | `US-TASK-012` |

### 9.2 Watch items

| ID | Item | Cadence |
|---|---|---|
| `US-WATCH-001` | CDS guidance (revised January 2026) — read the primary; further revision possible | Once now; then semi-annually |
| `US-WATCH-002` | AI-enabled device lifecycle guidance finalisation; PCCP guidance extension to non-AI devices; any FDA AI-specific rulemaking | Semi-annually |
| `US-WATCH-003` | Cybersecurity guidance revisions; §524B enforcement posture; SBOM format expectations | Semi-annually |
| `US-WATCH-004` | Recognized Consensus Standards database — recognised editions of every `US-STD-*` row | Before Pre-Sub; before submission |
| `US-WATCH-005` | HIPAA Security Rule amendment (proposed 2025); FTC HBNR enforcement; state health-data and AI laws (Colorado AI Act, Washington MHMDA, California) | Semi-annually |
| `US-WATCH-006` | ONC HTI rules on decision-support transparency (HTI-1 in force; HTI-2/HTI-4 amendments) — bears on EHR-partner contracts | Annually |
| `US-WATCH-007` | QMSR implementation — FDA inspection approach under ISO 13485 incorporation; any QMSR guidance | Annually |

---

## §10 Ketryx projection — UNITED STATES

The same item graph that generates the Australian Essential Principles checklist and
the Medsafe technical-file index generates the US submission. Configuration, not
re-authoring:

| US deliverable | Ketryx source |
|---|---|
| Software documentation (Enhanced level) | Requirement, Software Item Specification, Test Case, Anomaly items; revision history from releases; SOUP from dependency items |
| Risk management report | Risk items (ISO 14971 + 34971 strict-mode taxonomy) |
| Cyber documentation (§524B) | Threat / Asset / Threat Source / Threat Surface / Trust Boundary items; SBOM from supply-chain module; vulnerability workflow records |
| PCCP | Requirement items tagged as PCCP scope; modification protocol as a controlled document; impact assessment traced to Risk items |
| Design history file | The traceability matrix and approval records — Part 11 signatures and append-only audit trail |
| Labelling / IFU | Controlled documents; indications-for-use statement as a parent Requirement |

The `Relevant standards` field on Requirement items carries the CFR part or guidance
section beside the Essential Principle, so one requirement traces to all four
regulators' checklists.

---

## §11 Sources

| ID | Source | Currency | Class |
|---|---|---|---|
| `US-SRC-001` | FD&C Act §201(h); §520(o) (21 U.S.C. 321(h); 360j(o)) | Stable | Primary |
| `US-SRC-002` | FDA guidance — Clinical Decision Support Software (Sept 2022; **revised Jan 2026 — not yet read directly**) | **[currency: verify]** | Primary — **secondary knowledge of the 2026 revision** |
| `US-SRC-003` | 21 CFR 860 Subpart D (De Novo); 21 CFR 807 Subpart E (510(k)) | Stable | Primary |
| `US-SRC-004` | FDA De Novo and 510(k) databases — predicate landscape for CDS product codes | To be searched at `US-TASK-006` | Primary |
| `US-SRC-005` | 21 CFR Part 820 QMSR final rule (Feb 2024; effective 2 Feb 2026) | Current | Primary |
| `US-SRC-006` | FDA MDSAP programme page and MDSAP audit approach | Current | Primary |
| `US-SRC-007` | FD&C Act §524B (FDORA 2022) | Stable | Primary |
| `US-SRC-008` | FDA guidance — Cybersecurity in Medical Devices: Quality System Considerations and Content of Premarket Submissions (Sept 2023; **revised 2025**) | **[currency: verify]** | Primary |
| `US-SRC-009` | FDA guidance — Content of Premarket Submissions for Device Software Functions (June 2023) | Current | Primary |
| `US-SRC-010` | FDA guidance — Marketing Submission Recommendations for a PCCP for AI-Enabled Device Software Functions (Dec 2024) | Current | Primary |
| `US-SRC-011` | FDA draft guidance — AI-Enabled Device Software Functions: Lifecycle Management and Marketing Submission Recommendations (Jan 2025) | Draft **[verify finalisation]** | Primary |
| `US-SRC-012` | FDA/Health Canada/MHRA — GMLP guiding principles (2021); Transparency for MLMDs guiding principles (2024) | Current | Primary |
| `US-SRC-013` | 21 CFR 812.28 — acceptance of data from clinical investigations conducted outside the US | Stable | Primary |
| `US-SRC-014` | 21 CFR Part 11; FDA guidance Part 11 Scope and Application (2003) | Stable | Primary |
| `US-SRC-015` | 21 CFR Parts 801, 803, 806, 807, 830 | Stable | Primary |
| `US-SRC-016` | HIPAA rules (45 CFR 160/164); FTC Health Breach Notification Rule (16 CFR 318, 2024 amendment); state statutes | Current **[HIPAA Security Rule amendment proposed 2025]** | Primary |
| `US-SRC-017` | ONC HTI-1 Final Rule, 45 CFR 170.315(b)(11) decision support interventions | 2024 | Primary |
| `US-SRC-018` | Standards-gap review, 2 September 2026 — author's analysis | 2 Sept 2026 | **Author's analysis; rows tagged [recommendation]** |
| `US-SRC-019` | Australian REG-POSTURE v1.2 `WATCH-REG-006` (US instruments watch) — origin of the January 2026 CDS revision reference | 2 Sept 2026 | Internal |

**Confidence note.** Statutory and CFR findings (`US-FIND-001`, `002`, `004`, `006`,
`008`, `012`, `013`, `014`) are high confidence. `US-FIND-003` is medium: it rests on
the 2022 CDS guidance and the January 2026 revision has not been read. `US-FIND-005`
and `009` are high as to mechanics and medium as to which option applies. `US-FIND-011`
rests partly on draft guidance. Standards recognition status (`US-STD-*` "FDA status"
column) is from the author's knowledge of the Recognized Consensus Standards database
and **must be confirmed against the live database** before any submission
(`US-WATCH-004`).

---

## §12 Census and self-audit

### 12.1 Census

| Prefix | Count | Range |
|---|---|---|
| `US-FIND` | 16 | 001–016 |
| `US-OBL` | 14 | 001–014 |
| `US-STD` | 27 | 001–027 (013 defined in §5.1; numbering aligned to the shared stack so `NNN` means the same standard in every jurisdiction document; `US-STD-027` is US-only) |
| `US-REG` | 17 | 001–017 |
| `US-ASSUME` | 6 | 001–006 |
| `US-TASK` | 13 | 001–013 |
| `US-GATE` | 4 | 000–003 |
| `US-WATCH` | 7 | 001–007 |
| `US-Q` | 6 | 001–006 |
| `US-SRC` | 19 | 001–019 |
| **Total** | **129** | |

### 12.2 Self-audit

| # | Check | Result |
|---|---|---|
| 1 | All IDs match `^US-(FIND|OBL|STD|REG|ASSUME|TASK|GATE|WATCH|Q|SRC)-[0-9]{3}$` | PASS |
| 2 | Every ID defined exactly once in a table | PASS |
| 3 | Every `US-TASK-*` names its gate | PASS (13/13) |
| 4 | Every `US-GATE-*` names predecessors; all exist | PASS (4/4) |
| 5 | Every `US-ASSUME-*` names attesting party and what it blocks | PASS (6/6) |
| 6 | Every `US-FIND-*` names at least one `US-SRC-*` | PASS (16/16) |
| 7 | Every `US-STD-*` row carries an edition and an FDA status | PASS (27/27) |
| 8 | Every instrument with a known recent revision carries [currency: verify] | PASS (`US-REG-003`, `009`, `011`, `013`, `015`, `016`) |
| 9 | Shared-stack numbering: `US-STD-001..026` name the same standards as `STD-001..026` (AU) and `NZ-STD-001..026` (NZ) | PASS |
| 10 | No "see REG-POSTURE" for US-actionable content | PASS |
| 11 | Frontmatter `id_prefixes` ↔ §0.2 ↔ §12.1; range endpoints both ends | PASS (10/10 families) |

---

*Advisory only. US regulatory counsel must confirm before any commitment. Nothing here
authorises US marketing. Items tagged [recommendation] originate from the author's
analysis and require confirmation. Items tagged [currency: verify] name instruments
known to have changed recently; the primary text must be read before reliance.*
