---
doc_id: REG-EU
title: "Mākoha — Regulatory Posture: EUROPEAN UNION (MDR 2017/745)"
jurisdiction: EUROPEAN UNION
regulator: Notified body (conformity assessment) under Regulation (EU) 2017/745; national competent authorities (vigilance, market surveillance); European Commission / MDCG (guidance)
version: 1.0
status: DRAFT
authority: ADVISORY_ONLY
entity: Arepo Medtech Pty Ltd
product: Mākoha
date_issued: 2026-09-02
guidance_currency_date: 2026-09-02
standalone_rule: "REPLETE-STANDALONE. This document carries the complete standards stack, the EU legal instruments and every EU obligation itself. It never says 'see REG-POSTURE' for anything a reader needs in order to act in the European Union. Companion documents follow the same rule and repeat the stack by design."
companions:
  - "REG-POSTURE v1.2 — AUSTRALIA (TGA)"
  - "REG-NZ v1.1 — NEW ZEALAND (Medsafe)"
  - "REG-US v1.0 — UNITED STATES (FDA)"
sequence_position: "Later — after New Zealand (first) and Australia (second), per the programme's working jurisdiction sequence (Australian TASK-REG-022 / Q-REG-008; DEC pending)"
runtime_register: "R30 — Regulatory Posture Register; EU-* rows seeded in R30.2"
id_prefixes: [EU-FIND, EU-OBL, EU-STD, EU-LAW, EU-ASSUME, EU-TASK, EU-GATE, EU-WATCH, EU-Q, EU-SRC]
attestation_required: true
attestation_by: EU medical device regulatory counsel; notified body pre-application dialogue
---

# Mākoha — Regulatory Posture: EUROPEAN UNION (MDR 2017/745)

**Jurisdiction:** EUROPEAN UNION (and EEA) · Medical Devices Regulation (EU) 2017/745 · Artificial Intelligence Act (EU) 2024/1689 · GDPR (EU) 2016/679
**Prepared for:** Arepo Medtech Pty Ltd
**Version:** 1.0 · 2 September 2026
**Status:** Working document. Not regulatory advice. Requires EU regulatory counsel attestation before any commitment.

> **How to read this document.** It is the European Union authority for Mākoha's
> regulatory posture and is written to stand alone. The EU is a **later** jurisdiction
> in the programme's working sequence; the document exists now for two reasons. First,
> the EU is the only one of the four jurisdictions with **no** CDSS exemption of any
> kind — Rule 11 classifies every piece of decision-support software — so it is the
> jurisdiction that most clearly shows why the classified track, not an exempt tier,
> is the product. Second, the EU AI Act layers a second conformity regime on top of
> the MDR for exactly this class of device, and its requirements (data governance,
> logging, human oversight, technical documentation) are cheap to satisfy from the
> first artifact and expensive to retrofit. Every finding is carried as an assumption
> requiring EU counsel attestation. Items from the author's analysis carry
> **[recommendation]** and a confidence tag; instruments known to be in flux carry
> **[currency: verify]**.

---

## §0 Conventions

### 0.1 Authority

Advisory input only. Cannot be cited as evidence for a DONE. Every material finding
about EU regulation is carried as an `EU-ASSUME-*` requiring written attestation from
EU counsel, or written notified-body feedback, before reliance.

### 0.2 ID scheme

| Prefix | Meaning | Closure |
|---|---|---|
| `EU-FIND-nnn` | Finding about EU regulation | Superseded or attested |
| `EU-OBL-nnn` | Standing EU obligation | Never closes |
| `EU-STD-nnn` | Standard in scope, with EU harmonisation status | Retired only by pathway change |
| `EU-LAW-nnn` | Legal instrument or MDCG guidance | Retired when superseded |
| `EU-ASSUME-nnn` | Assumption requiring external closure | Written attestation, named party, dated |
| `EU-TASK-nnn` | Sequenced work item | DONE-with-evidence or typed HALT |
| `EU-GATE-nnn` | Blocking gate | All predecessors DONE-with-evidence |
| `EU-WATCH-nnn` | External change to monitor | Never closes; cadence stated |
| `EU-Q-nnn` | Open question | Answer in writing |
| `EU-SRC-nnn` | Source | Retired when superseded |

### 0.3 Status vocabulary

`OPEN` · `IN-PROGRESS` · `DONE-WITH-EVIDENCE` · `HALT-TYPED` · `SUPERSEDED` ·
`ATTESTED` · `REFUTED`. Assumptions hold only `OPEN`, `ATTESTED`, `REFUTED`,
`SUPERSEDED` and never close by internal reasoning. R30 crosswalk as in the Australian
posture.

### 0.4 Provenance and confidence tags

| Tag | Meaning |
|---|---|
| **[EU-sourced]** | Traceable to a Regulation article/annex, Commission implementing decision or MDCG document named in §11 |
| **[recommendation]** | Author's analysis; requires counsel or notified-body confirmation |
| **[confidence: high / medium / low]** | Author's confidence the item is correctly stated and currently in force |
| **[currency: verify]** | Instrument known to be under amendment or recently changed; read the primary before reliance |

### 0.5 Firewall note

No case content, no evidence-library values, no sensitivities, specificities or
likelihood ratios. Not a source for clinical content.

### 0.6 Jurisdiction declaration and the replete-standalone rule

**This document is the EUROPEAN UNION.** The four jurisdiction documents share one
standards stack and one architecture; they do not share text by reference. Each carries
the complete stack with that regulator's recognition status and its own obligations,
gates, tasks, assumptions, questions, watch items and sources. Shared programme
artifacts are built once and projected per regulator. A change to the shared stack is
made in all four documents in the same cycle, or the divergence is logged in the
wrapper (MAK-ANT) as a signal.

---

## §1 Headline

**In the European Union Mākoha is a Class IIa medical device at minimum, Class IIb
plausibly, with no exemption available, and it will also be a high-risk AI system
under the AI Act.** Both regimes are assessed by the same notified body, and both
must be satisfied before CE marking.

Three things distinguish the EU from the other three jurisdictions:

1. **No carve-out exists.** The TGA has a CDSS exemption (assessed unavailable to
   Mākoha); the FDA has the §520(o)(1)(E) exclusion (assessed unavailable); Medsafe
   has notification-only entry. The MDR has none of these. Rule 11 classifies any
   software intended to provide information used to take diagnostic or therapeutic
   decisions. The J-3 exempt-tier idea has no European analogue at all
   (`EU-FIND-003`).
2. **Two conformity regimes, one notified body.** Once the AI Act's high-risk
   obligations apply, a Class IIa+ device whose AI is a safety component — or is the
   product — is a high-risk AI system, and the MDR notified body must also be
   designated under the AI Act to assess it (`EU-FIND-009`). The AI Act's technical
   requirements overlap heavily with what IEC 62304, ISO 14971, BS/AAMI 34971 and
   IEC 81001-5-1 already produce; the marginal cost is in data governance
   documentation, logging and the human-oversight design, all of which the programme
   already has architecturally.
3. **Notified-body capacity is the schedule risk, not the standards.** EU
   notified-body queues for software have run 12–18 months from application to
   certificate. The EU is entered by applying early, not by building differently.

Nothing in this document is a plan to enter the EU soon. It is a plan to make the EU a
projection of the same file, and to avoid two known traps: assuming a lighter tier
exists, and building an AI system whose training-data lineage cannot be documented
after the fact.

---

## §2 Findings

| ID | Finding | Status | Source |
|---|---|---|---|
| `EU-FIND-001` | Software is a medical device under MDR Article 2(1) where the manufacturer intends it for a medical purpose, including diagnosis, prevention, monitoring, prediction, prognosis, treatment or alleviation of disease. MDCG 2019-11 qualifies software as *medical device software* (MDSW) where it performs an action on data going beyond storage, archival, communication, simple search or lossless compression, for the benefit of individual patients. Mākoha is MDSW. **[EU-sourced; high]** | OPEN | `EU-SRC-001`, `EU-SRC-002` |
| `EU-FIND-002` | **Rule 11** (Annex VIII, 6.3): software intended to provide information used to take decisions with diagnosis or therapeutic purposes is **Class IIa**, except: Class **III** if such decisions may cause death or an irreversible deterioration of health; Class **IIb** if they may cause a serious deterioration of health or a surgical intervention. Software intended to monitor physiological processes is IIa (IIb for vital parameters where variations could result in immediate danger). All other software is Class I. For a differential-diagnosis engine whose output bears on serious conditions, **IIb is the conservative planning class; IIa the floor**. **[EU-sourced; high (rule) / medium (which sub-rule)]** | OPEN | `EU-SRC-001`, `EU-SRC-002`, `EU-SRC-003` |
| `EU-FIND-003` | **No exemption or notification-only tier exists** for clinical decision support software under the MDR. An exempt-tier artifact of the J-3 type would classify under Rule 11 exactly as the full product does. Any European ambition — and any low-resource jurisdiction that follows CE marking — must be planned against the classified track only. **[EU-sourced; high]** | OPEN | `EU-SRC-001`, `EU-SRC-002` |
| `EU-FIND-004` | Conformity assessment for Class IIa is via a notified body under **Annex IX Chapters I and III** (QMS assessment plus technical-documentation assessment on a representative-sample basis) or **Annex XI Part A** (production quality assurance). For Class IIb, Annex IX with technical documentation assessed for at least one representative device per generic device group (Annex IX §4.4–4.8), or Annex X + XI. In practice a QMS certificate and technical documentation assessment by a notified body designated for software codes. **[EU-sourced; high]** | OPEN | `EU-SRC-001` |
| `EU-FIND-005` | The device must meet the **General Safety and Performance Requirements** of Annex I. For software the decisive ones are GSPR 17 (electronic programmable systems: repeatability, reliability and performance; state-of-the-art development lifecycle, risk management, information security, verification and validation; minimum IT security requirements) and GSPR 23 (label and IFU). **[EU-sourced; high]** | OPEN | `EU-SRC-001` |
| `EU-FIND-006` | **Clinical evaluation** is mandatory (Article 61; Annex XIV Part A) and for MDSW follows MDCG 2020-1's three-part structure: **valid clinical association** (scientific validity of the association between the software output and the clinical condition), **technical performance** (analytical/technical validation), and **clinical performance** (the software yields clinically meaningful output in the target population). Clinical data may come from literature, clinical investigation, or clinical experience; equivalence to another device is available but constrained. Synthetic data supports technical performance only; it is not clinical data. **[EU-sourced; high]** | OPEN | `EU-SRC-004` |
| `EU-FIND-007` | Clinical investigations are governed by Articles 62–82 and harmonised EN ISO 14155:2020. **Data from investigations conducted outside the EU are acceptable** where conducted to equivalent ethical and scientific standards — NZ/AU evidence to ISO 14155 with ethics approval and identical intended purpose transfers, subject to the notified body's assessment of population applicability to the EU. **[EU-sourced; high (rule) / medium (applicability)]** | OPEN | `EU-SRC-001`, `EU-SRC-004` |
| `EU-FIND-008` | **Post-market obligations** are substantive: a PMS system and plan (Articles 83–84; Annex III); a **Periodic Safety Update Report** (Article 86) — for Class IIa updated when necessary and at least every two years, for IIb at least annually, and for IIb submitted to the notified body via EUDAMED; **PMCF** (Annex XIV Part B); **vigilance** reporting of serious incidents (Article 87: 15 days; 10 days for death or unanticipated serious deterioration; 2 days for serious public health threat) and trend reporting (Article 88); field safety corrective actions (Article 89). **[EU-sourced; high]** | OPEN | `EU-SRC-001`, `EU-SRC-005` |
| `EU-FIND-009` | Under the **AI Act** (Regulation (EU) 2024/1689) an AI system is **high-risk** where it is a safety component of, or is itself, a product covered by Annex I Section A Union harmonisation legislation that requires third-party conformity assessment — the MDR is listed (Annex I, Section A, point 11). A Class IIa+ MDSW with an AI component that is subject to notified-body assessment is therefore high-risk. Obligations for Annex I high-risk systems apply from **2 August 2027**; the conformity assessment is integrated with the MDR assessment (Article 43(3)) by a notified body also designated under the AI Act. **[EU-sourced; high (rule) / [currency: verify] — the "Digital Omnibus" proposal of late 2025 proposed deferring high-risk application dates; status must be checked]** | OPEN | `EU-SRC-006`, `EU-SRC-007` |
| `EU-FIND-010` | High-risk AI system requirements (AI Act Articles 9–15): risk management system (Art 9); data and data governance (Art 10 — training, validation and testing data relevance, representativeness, error-freedom to the extent possible, bias examination); technical documentation (Art 11, Annex IV — may be integrated into the MDR technical documentation); record-keeping / automatic logging (Art 12); transparency and information to deployers (Art 13); **human oversight** (Art 14 — the deployer must be able to understand, monitor, override and interrupt); accuracy, robustness and cybersecurity (Art 15). Provider obligations (Art 16–21) include a QMS (Art 17, integrable with ISO 13485), corrective actions, and cooperation with authorities. **[EU-sourced; high]** | OPEN | `EU-SRC-006` |
| `EU-FIND-011` | Arepo, as a manufacturer outside the EU, must appoint an **Authorised Representative** established in the EU (Article 11) with a written mandate, register as an economic operator in **EUDAMED** to obtain a Single Registration Number (Article 31), assign **Basic UDI-DI and UDI-DI** (Articles 27–29) and register the device, issue an **EU Declaration of Conformity** (Article 19, Annex IV), affix the **CE marking** with the notified body number (Article 20), and have a **Person Responsible for Regulatory Compliance** (Article 15 — micro and small enterprises need not employ one but must have one permanently and continuously at their disposal). **[EU-sourced; high]** | OPEN | `EU-SRC-001` |
| `EU-FIND-012` | **GDPR** applies to processing of EU patient data. Health data is a special category (Article 9); a **Data Protection Impact Assessment** is mandatory for large-scale processing of health data and for new technologies (Article 35); Article 22 (automated individual decision-making) is engaged unless a human decision intervenes — the clinician-in-the-loop design is the mitigation and must be real, not nominal; Arepo as a non-EU processor/controller needs an **EU representative** (Article 27); transfers to Australia require a Chapter V mechanism (Standard Contractual Clauses plus transfer impact assessment) because Australia has **no adequacy decision** — whereas **New Zealand does** (Commission Decision 2013/65/EU). **[EU-sourced; high]** | OPEN | `EU-SRC-008` |
| `EU-FIND-013` | The **Cyber Resilience Act** (EU) 2024/2847 excludes products covered by the MDR (Article 2(2)) — Mākoha's cyber obligations in the EU run through GSPR 17.4 and MDCG 2019-16, not the CRA. **NIS2** (Directive 2022/2555) lists manufacture of medical devices as an "important entity" sector but applies by size threshold; Arepo is currently below it, but EU health-sector customers (essential entities) pass supply-chain security requirements down contractually. **[EU-sourced; high]** | OPEN | `EU-SRC-009` |
| `EU-FIND-014` | The **European Health Data Space** Regulation (EU) 2025/327 imposes self-certification essential requirements on EHR systems and, for MDSW claiming interoperability with EHR systems, requires demonstration of conformity with the relevant EHDS interoperability requirements alongside MDR conformity. Application dates run from 2027–2029. Bears on any EU EHR integration; **[EU-sourced; medium — application dates and MDSW provisions to verify]** | OPEN | `EU-SRC-010` |
| `EU-FIND-015` | The revised **Product Liability Directive** (EU) 2024/2853 expressly treats software (including AI systems and software updates) as a product, applies to products placed on the market from **9 December 2026**, and includes disclosure-of-evidence and presumption-of-defect provisions that make technical documentation, logging (`EU-FIND-010` Art 12) and change records the manufacturer's principal defence. **[EU-sourced; high]** | OPEN | `EU-SRC-011` |
| `EU-FIND-016` | Language: the IFU and label must be in the official language(s) accepted by each Member State where the device is made available (Article 10(11); national rules). For a SaMD this is the in-product text and IFU per market. **[EU-sourced; high]** | OPEN | `EU-SRC-001` |

---

## §3 Qualification and classification

### 3.1 Qualification

MDSW (`EU-FIND-001`). The Governance Layer (organisational-conformance analysis, no
clinical write path, no patient-specific output) is assessed as **not MDSW**: MDCG
2019-11 places software for administrative, quality-management or general
data-processing purposes without a medical purpose for individual patients outside the
MDR. **[recommendation; medium]** Carried as `EU-ASSUME-006`. It is also assessed as
not a high-risk AI system on its own (no Annex I product; no Annex III use case
engaged for organisational analytics) — but the AI Act's transparency duties for AI
that interacts with natural persons (Article 50) may apply to any conversational
surface. **[recommendation; medium]**

### 3.2 Classification

Rule 11 (`EU-FIND-002`). Planning class **IIb**; floor **IIa**. The choice turns on
whether decisions taken on Mākoha's output "may cause a serious deterioration of a
person's state of health" — for a differential that ranks serious conditions (sepsis,
PE, ACS in a respiratory presentation) the notified body is likely to read IIb. The
classification is proposed by the manufacturer and confirmed by the notified body; a
dispute goes to the competent authority (Article 51). Carried as `EU-ASSUME-001`.

Practical consequence of IIb over IIa: annual PSUR submitted to the notified body;
technical documentation assessed per generic device group rather than by sampling;
higher notified-body fees; otherwise the file is the same.

### 3.3 AI Act status

High-risk (`EU-FIND-009`), on the working assumption that the Bayesian engine, the
conformal wrapper and any runtime LLM component are safety components of the device.
Carried as `EU-ASSUME-002`. A deterministic-only build (Addendum J-1) does not escape
this: the AI Act's definition of an AI system is broad (machine-based system inferring
outputs from inputs with some autonomy), and the engine infers.

---

## §4 Obligations register — EUROPEAN UNION

Non-closing. Attach from CE marking unless stated.

| ID | Obligation | Instrument | Note |
|---|---|---|---|
| `EU-OBL-001` | QMS covering the Article 10(9) elements | MDR Art 10(9); Annex IX Ch I | ISO 13485 with MDR-specific additions (regulatory strategy, UDI, PMS, vigilance, clinical evaluation, PRRC, communication with NB/CA). The same QMS as Australia/NZ/US with the EU overlay |
| `EU-OBL-002` | Technical documentation to Annex II and Annex III, kept current for the device lifetime and at least 10 years after the last device is placed on the market | MDR Art 10(4); Annexes II, III | The STED-shaped file built for Medsafe/TGA **is** this, re-indexed to Annex II headings |
| `EU-OBL-003` | GSPR conformity, evidenced in a GSPR checklist naming the standard or solution applied and the evidence location | Annex I | GSPR 17 (software) and 23 (information supplied) are the load-bearing rows; harmonised standards give presumption of conformity |
| `EU-OBL-004` | Clinical evaluation, maintained through PMCF | Art 61; Annex XIV; MDCG 2020-1 | CER structured as valid clinical association / technical performance / clinical performance |
| `EU-OBL-005` | PMS system and plan; PSUR (biennial IIa; annual IIb, submitted to NB) | Arts 83–86; Annex III | PSUR content: benefit-risk conclusions, PMCF findings, sales volumes, user population, complaint and trend data |
| `EU-OBL-006` | Vigilance: serious incidents, trend reports, FSCAs via EUDAMED | Arts 87–89; MDCG 2023-3 | 15 / 10 / 2 day clocks; software "incident" includes malfunction that could lead to serious deterioration |
| `EU-OBL-007` | Authorised Representative; PRRC; EUDAMED actor registration (SRN) | Arts 11, 15, 31 | AR mandate covers verification of DoC and technical documentation availability; AR is jointly and severally liable for defective devices |
| `EU-OBL-008` | UDI and device registration | Arts 27–29; Annex VI | UDI carrier displayed in software (e.g. about screen) and in EUDAMED; Basic UDI-DI on DoC and certificate |
| `EU-OBL-009` | EU Declaration of Conformity and CE marking with NB number | Arts 19–20; Annex IV | Updated on every change affecting conformity |
| `EU-OBL-010` | Information security "according to the state of the art" and minimum IT security requirements, with disclosure of residual risks and security-relevant information to users | GSPR 17.2, 17.4; MDCG 2019-16 | Secure development lifecycle evidence (IEC 81001-5-1), threat model, SBOM, vulnerability handling, IFU security section |
| `EU-OBL-011` | Significant-change control: changes to design or intended purpose assessed for notified-body notification before implementation | Annex IX §4.10; MDCG 2020-3 (by analogy) | Functional changes to the inference plane are assessed **pre-deployment**; the same rule as TGA and FDA, formalised here as a NB notification test |
| `EU-OBL-012` | AI Act high-risk provider obligations from the application date | AI Act Arts 9–21, 43, 49 | Risk management (integrated with ISO 14971), data governance record, Annex IV technical documentation (integrated into Annex II), automatic logging, instructions for deployers, human-oversight design, accuracy/robustness/cyber, QMS, registration in the EU AI database (Art 49) |
| `EU-OBL-013` | GDPR: DPIA; Article 9 lawful basis (via the controller); Article 22 human-intervention design; EU representative; Chapter V transfer mechanism for any processing in Australia; processor agreements (Art 28) | GDPR | **Not equivalent to** APP, NZ HIPC or HIPAA compliance |
| `EU-OBL-014` | Labelling and IFU in Member-State languages; "notified body assessed" is not "approved" in claims | Art 10(11); Annex I Ch III; national law; UCPD 2005/29/EC | The versioned claims inventory is diffed against the certified intended purpose per market and language |
| `EU-OBL-015` | Product liability readiness: technical documentation, logs and change records retained and producible | PLD 2024/2853 | Disclosure-of-evidence provisions make the Article 12 logs and the DHF the defence |
| `EU-OBL-016` **[recommendation; high]** | Author-once records rule | Programme rule | Every shared artifact is generated in a form that satisfies the EU instruments above now: Annex II-indexable technical documentation; GSPR checklist alongside the Australian EP checklist; AI Act Annex IV data-governance and logging content captured from the first training run; clinical evidence to ISO 14155 with EU-applicability considered in the protocol |

---

## §5 Standards stack — EUROPEAN UNION

Under the MDR, conformity with a **harmonised standard** whose reference is published
in the Official Journal (Commission Implementing Decision (EU) 2021/1182, as amended)
gives a **presumption of conformity** with the GSPRs it covers. Non-harmonised
standards remain admissible as evidence of state of the art, which GSPR 17.2 requires.
Column "EU status" records harmonisation to the author's knowledge; **the current OJ
list must be checked before the notified-body application** (`EU-WATCH-004`). The
AI Act will have its own harmonised standards (CEN-CENELEC JTC 21 work programme) —
none yet published; `EU-WATCH-002`. Editions are pinned. Priority 1 = the file cannot
be assessed without it; 2 = expected in the technical documentation; 3 = expected for
the GSPR 17.4 cyber case; 4 = situational.

### 5.1 Core lifecycle and quality

| ID | Standard | Edition (EN) | Role in the EU technical documentation | EU status | Priority |
|---|---|---|---|---|---|
| `EU-STD-001` | ISO 13485 | EN ISO 13485:2016 + A11:2021 | QMS — Annex IX Chapter I assessment; Article 10(9) | **Harmonised** (MDR) | **1** |
| `EU-STD-002` | IEC 62304 | EN IEC 62304:2006 + A1:2015 | Software lifecycle — GSPR 17.2 "state of the art development life cycle"; software safety class (expect B or C) | **Harmonised** (MDR) **[verify current OJ listing]** | **1** |
| `EU-STD-003` | ISO 14971 | EN ISO 14971:2019 + A11:2021 | Risk management — GSPR 1–9; the A11 annex Z maps clauses to GSPRs and is the reason to cite the EN edition | **Harmonised** (MDR) | **1** |
| `EU-STD-004` | IEC 62366-1 | EN IEC 62366-1:2015 + A1:2020 | Usability engineering — GSPR 5, 14.1, 17 | **Harmonised** (MDR) **[verify]** | **2** |
| `EU-STD-005` | IEC 82304-1 | EN 82304-1:2017 | Health software product safety — GSPR 17 product-level requirements | Not harmonised (state of the art) **[verify]** | **2** |
| `EU-STD-006` | BS/AAMI 34971 | BS/AAMI 34971:2023 | ISO 14971 applied to ML — the ML risk method; the natural bridge to AI Act Article 9 | Not harmonised (state of the art) | **2** |
| `EU-STD-013` | IEC 62304 §5.1.4 + ISO 13485 §4.1.6 | as above | Software tool validation — the notified body will ask how the design-controls platform and authoring tools are validated | Implicit in 001/002 | **2** |

### 5.2 Cyber security and information security

| ID | Standard | Edition | Role in the EU technical documentation | EU status | Priority |
|---|---|---|---|---|---|
| `EU-STD-007` | ANSI/AAMI SW96 | :2023 | Security risk management — MDCG 2019-16 expects a security risk management process beside safety risk management | Not harmonised (state of the art) | 3 |
| `EU-STD-008` | IEC 81001-5-1 | EN IEC 81001-5-1:2022 | Secure development lifecycle — GSPR 17.2/17.4; MDCG 2019-16 | **Harmonised** (MDR) **[verify — listed in a 2024/2025 amending decision to the author's knowledge]** | 3 |
| `EU-STD-009` | ISO/IEC 29147 and ISO/IEC 30111 | 29147:2018; 30111:2019 | Coordinated vulnerability disclosure and handling — MDCG 2019-16 postmarket cyber expectations | Not harmonised (state of the art) | 3 |
| `EU-STD-010` | ISO 27799 | EN ISO 27799:2016 | Health information security controls — supports GDPR Article 32 and customer assurance; not a device-conformity item | Not harmonised | 3 |
| `EU-STD-011` | IEC 80001-1 | EN IEC 80001-1:2021 | Health IT network risk management — deployment-side; referenced by MDCG 2019-16 for the operator's responsibilities | Not harmonised | 4 |
| `EU-STD-012` | UL 2900-2-1 | :2017 | Security testing yardstick — accepted as state of the art for penetration testing | Not harmonised | 4 |

### 5.3 Additional rows load-bearing in the EU **[recommendation unless stated]**

| ID | Standard | Edition | Why it is load-bearing in the EU | EU status | Priority | Confidence |
|---|---|---|---|---|---|---|
| `EU-STD-014` | ISO/TR 24971 | :2020 | Guidance on ISO 14971 — the risk file's method; notified bodies read the risk file against it | Not harmonised (TR) | **2** | high |
| `EU-STD-015` | IEC/TR 80002-1 | :2009 | ISO 14971 applied to software — software safety class argument | Not harmonised (TR) | **2** | high |
| `EU-STD-016` | AAMI TIR45 | :2023 | Agile in medical device software — how a continuous build is shown to satisfy EN IEC 62304 | Not harmonised | **2** | high |
| `EU-STD-017` | AAMI TIR57 | :2016 (R2023) | Device security risk management — the threat model's cited method | Not harmonised | 3 | high |
| `EU-STD-018` | ISO 14155 | EN ISO 14155:2020 + A11:2024 | Clinical investigation GCP — Articles 62–82; the conduct standard that makes NZ/AU evidence admissible (`EU-FIND-007`) | **Harmonised** (MDR) | **1** | high |
| `EU-STD-019` | ISO 20417 | EN ISO 20417:2021 | Information supplied by the manufacturer — GSPR 23 | **Harmonised** (MDR) | **2** | high |
| `EU-STD-020` | ISO 15223-1 | EN ISO 15223-1:2021 | Symbols — GSPR 23 | **Harmonised** (MDR) | 3 | high |
| `EU-STD-021` | ISO/IEC 42001 | :2023 | AI management system — the closest existing standard to the AI Act Article 17 QMS expectation; alignment recommended; certification may become commercially expected | Not harmonised; AI Act harmonised standards pending | 3 | medium |
| `EU-STD-022` | ISO/IEC 23894 | :2023 | AI risk management guidance — bridges ISO 14971/34971 to AI Act Article 9 | Not harmonised | 3 | medium |
| `EU-STD-023` | IEC 60601-4-5 | :2021 | Security capability levels — only if claimed | Not harmonised | 4 | medium |
| `EU-STD-024` | ISO/IEC 27001 | :2022 | ISMS — GDPR Article 32 evidence; EU health-sector and NIS2-essential-entity customers routinely require it or its Annex A controls | Not harmonised | 4 | high |
| `EU-STD-025` | IMDRF SaMD documents | N10:2013, N12:2014, N23:2015, N41:2017 | MDCG 2019-11 and 2020-1 are built on N12 and N41 respectively; the classification and clinical-evaluation arguments use their vocabulary | Basis of MDCG guidance | **2** | high |
| `EU-STD-026` | IMDRF cyber and ML documents | N60:2020, N70:2023, N73:2023, N88:2025 | MDCG 2019-16 aligns with N60; SBOM per N73; GMLP N88 | Basis of MDCG guidance | 3 | medium |
| `EU-STD-027` | ISO/IEC 5259 series (data quality for ML); ISO/IEC TS 8200 (controllability); ISO/IEC 24029 (robustness) | 5259-1..-4:2024; 8200:2024; 24029-2:2023 | The AI Act Article 10 (data governance) and Article 15 (robustness) evidence has no harmonised standard yet; these are the ISO/IEC SC 42 documents the CEN-CENELEC JTC 21 programme is building from | Not harmonised; **watch** | 4 | medium |

### 5.4 Considered and not adopted

| Standard | Reason |
|---|---|
| IEC 60601-1 family (other than 60601-4-5) | No hardware |
| EN 62366 (old, undated) | Superseded by EN IEC 62366-1 |
| ISO/IEC TS 82304-2 | Consumer health-app quality label; not an MDR item |
| Cyber Resilience Act conformity | MDR devices excluded (`EU-FIND-013`) |
| ISO 9001 | Superseded by ISO 13485 |

---

## §6 EU legal instruments and MDCG guidance register

| ID | Instrument | Type | Bearing on Mākoha | Currency |
|---|---|---|---|---|
| `EU-LAW-001` | Regulation (EU) 2017/745 (MDR) — Arts 2, 10, 11, 15, 19–20, 27–31, 51–52, 61–62, 83–89; Annexes I, II, III, IV, VI, VIII, IX, XIV | Regulation | Core device law | Consolidated text current; **Commission targeted revision proposal (Dec 2025) [currency: verify]** |
| `EU-LAW-002` | MDCG 2019-11 — Qualification and classification of software (rev.1) | Guidance | `EU-FIND-001..003` | Current |
| `EU-LAW-003` | MDCG 2021-24 — Classification of medical devices | Guidance | Rule 11 application | Current |
| `EU-LAW-004` | MDCG 2020-1 — Clinical evaluation of MDSW | Guidance | `EU-FIND-006` | Current |
| `EU-LAW-005` | MDCG 2019-16 rev.1 — Cybersecurity for medical devices | Guidance | `EU-OBL-010` | Current |
| `EU-LAW-006` | MDCG 2023-3 — Vigilance terms and concepts; MDCG 2022-21 — PSUR guidance | Guidance | `EU-OBL-005`, `EU-OBL-006` | Current |
| `EU-LAW-007` | MDCG 2025-6 — Interplay between the MDR/IVDR and the AI Act (FAQ) | Guidance | `EU-FIND-009`, `EU-OBL-012` | 2025 **[verify number and content]** |
| `EU-LAW-008` | Commission Implementing Decision (EU) 2021/1182 on harmonised standards for medical devices, as amended | Implementing decision | `EU-STD-*` status column | **Amended repeatedly; check current OJ list [currency: verify]** |
| `EU-LAW-009` | Regulation (EU) 2024/1689 (AI Act) — Arts 6, 9–21, 43, 49, 50, 113; Annexes I, IV | Regulation | `EU-FIND-009`, `010`; `EU-OBL-012` | In force; high-risk Annex I obligations 2 Aug 2027 **[Digital Omnibus deferral proposal — verify]** |
| `EU-LAW-010` | Regulation (EU) 2016/679 (GDPR) — Arts 9, 22, 27, 28, 32, 35, Ch V; Commission Decision 2013/65/EU (NZ adequacy) | Regulation | `EU-FIND-012`; `EU-OBL-013` | Current |
| `EU-LAW-011` | Directive (EU) 2022/2555 (NIS2); Regulation (EU) 2024/2847 (CRA) | Directive / Regulation | `EU-FIND-013` | Current |
| `EU-LAW-012` | Regulation (EU) 2025/327 (EHDS) | Regulation | `EU-FIND-014` | Application 2027–2029 **[verify]** |
| `EU-LAW-013` | Directive (EU) 2024/2853 (Product Liability) | Directive | `EU-FIND-015`; `EU-OBL-015` | Applies from 9 Dec 2026 |
| `EU-LAW-014` | Directive 2005/29/EC (Unfair Commercial Practices); national therapeutic-advertising rules | Directive | `EU-OBL-014` | Current |

---

## §7 Sequenced plan

Split into **now** (during the NZ/AU build, so the EU remains a projection) and **at
entry**.

### Gates

| ID | Gate | Predecessors | Meaning |
|---|---|---|---|
| `EU-GATE-000` | EU-capable foundations | `EU-TASK-001..004` | Technical documentation Annex II-indexable; GSPR checklist alive; AI Act data-governance and logging captured from first training run; clinical evidence EU-applicable |
| `EU-GATE-001` | EU decision and notified body engaged | `EU-TASK-005..008` | Counsel attested; NB selected (MDR + AI Act designation) and application lodged; AR and PRRC appointed |
| `EU-GATE-002` | Certification | `EU-TASK-009..012` | QMS certificate and technical documentation assessment complete; AI Act conformity assessed; DoC issued; CE marked; EUDAMED registrations done |
| `EU-GATE-003` | EU market | `EU-TASK-013` | Placed on the market in named Member States with language-compliant IFU; PMS/PSUR/vigilance operating |

### Tasks — now

| ID | Task | Gate |
|---|---|---|
| `EU-TASK-001` | Index the technical documentation to Annex II headings alongside the Medsafe STED index and the Australian EP checklist — one Ketryx document template per regulator over the same items. Maintain a GSPR checklist from the first requirement. | `EU-GATE-000` |
| `EU-TASK-002` | Capture AI Act Annex IV / Article 10 content from the first training or tuning run: data provenance, selection criteria, representativeness assessment, bias examination, labelling procedures, data-set splits. Retrofitting this is the single most expensive EU omission. | `EU-GATE-000` |
| `EU-TASK-003` | Design automatic logging (Article 12) into the runtime: per-inference record of model version, inputs summary, output, confidence/conformal interval, clinician action — retained for the period the AI Act and PLD require. Already close to the programme's justification ledger; make the retention and access provisions explicit. | `EU-GATE-000` |
| `EU-TASK-004` | Clinical evidence protocol (NZ/AU) written with EU applicability in mind: population description against EU demographics, ISO 14155 conduct, endpoints structured as valid clinical association / technical performance / clinical performance. | `EU-GATE-000` |

### Tasks — at entry

| ID | Task | Gate |
|---|---|---|
| `EU-TASK-005` | Engage EU regulatory counsel; put `EU-ASSUME-001..006` to them with the intended purpose statement, classification rationale and AI Act analysis. | `EU-GATE-001` |
| `EU-TASK-006` | Notified body selection: designated for MDR software codes **and** under the AI Act; pre-application dialogue on class (IIa/IIb), clinical evidence sufficiency including foreign data, AI Act integration, and timeline. Lodge application. | `EU-GATE-001` |
| `EU-TASK-007` | Appoint Authorised Representative (mandate per Article 11(3)); designate PRRC (Article 15); register actor in EUDAMED (SRN). | `EU-GATE-001` |
| `EU-TASK-008` | GDPR: appoint EU representative (Art 27); DPIA; Article 28 processor terms; Chapter V transfer mechanism for Australian processing or EU-region hosting decision. | `EU-GATE-001` |
| `EU-TASK-009` | Clinical Evaluation Report to MDCG 2020-1; PMCF plan; PMS plan; PSUR template. | `EU-GATE-002` |
| `EU-TASK-010` | Cyber documentation to MDCG 2019-16: secure lifecycle evidence (EN IEC 81001-5-1), threat model, security risk management report, SBOM, vulnerability handling process, IFU security information, residual-risk disclosure. | `EU-GATE-002` |
| `EU-TASK-011` | AI Act conformity package integrated with the MDR file: risk management (Art 9 within ISO 14971 file), data governance record, Annex IV documentation, logging design, instructions for deployers, human-oversight design evidence, accuracy/robustness/cyber evidence; register in the EU AI database (Art 49). | `EU-GATE-002` |
| `EU-TASK-012` | UDI assignment (Basic UDI-DI, UDI-DI); EU Declaration of Conformity; CE marking; EUDAMED device registration; Member-State language IFU for launch markets. | `EU-GATE-002` |
| `EU-TASK-013` | Post-market operating: vigilance procedures with 15/10/2-day clocks; trend reporting; PSUR cadence (annual if IIb); PMCF running; significant-change assessment procedure (`EU-OBL-011`); product-liability evidence retention. | `EU-GATE-003` |

---

## §8 Assumptions

No `EU-ASSUME-*` closes by internal reasoning.

| ID | Assumption | Attesting party | Blocks | Status |
|---|---|---|---|---|
| `EU-ASSUME-001` | Mākoha is MDSW under Rule 11, Class IIb (planning) / IIa (floor); no exemption or lower tier available | EU counsel + NB pre-application feedback | `EU-GATE-001` | OPEN |
| `EU-ASSUME-002` | Mākoha is a high-risk AI system under AI Act Article 6(1) / Annex I point 11, with the notified body performing the integrated assessment | EU counsel + NB | `EU-GATE-001` | OPEN |
| `EU-ASSUME-003` | Conformity assessment route: Annex IX Chapters I and III (QMS + technical documentation) | NB | `EU-GATE-001` | OPEN |
| `EU-ASSUME-004` | NZ/AU clinical evidence to ISO 14155 is acceptable for the CER without an EU confirmatory investigation, subject to population-applicability justification | NB | `EU-GATE-002` | OPEN |
| `EU-ASSUME-005` | Arepo acts as processor (not controller) for EU clinical customers; Article 22 is satisfied by the clinician decision; Australian processing is lawful under SCCs with a transfer impact assessment | EU privacy counsel | `EU-GATE-001` | OPEN |
| `EU-ASSUME-006` | The Governance Layer is not MDSW and not a high-risk AI system | EU counsel | Governance Layer EU supply | OPEN |

---

## §9 Questions and watch items

### 9.1 Questions

| ID | Question | Who | Blocking |
|---|---|---|---|
| `EU-Q-001` | IIa or IIb: does the notified body read a ranked differential covering serious conditions as software whose decisions "may cause a serious deterioration of health"? | NB pre-application | `EU-ASSUME-001` |
| `EU-Q-002` | What is the current application date for Annex I high-risk AI obligations after the Digital Omnibus process, and does the NB expect the AI Act assessment to be lodged with the MDR application or later? | EU counsel; NB | `EU-ASSUME-002`; `EU-TASK-006` |
| `EU-Q-003` | Which harmonised standards are currently listed in the OJ under the MDR for the `EU-STD-*` rows marked [verify] — 62304, 62366-1, 82304-1, 81001-5-1? | RA / QMS lead | `EU-WATCH-004` |
| `EU-Q-004` | Is EU-region hosting a precondition for EU health-sector customers irrespective of the GDPR transfer analysis? | EU privacy counsel; customers | `EU-TASK-008` |
| `EU-Q-005` | Does the EHDS MDSW-interoperability provision engage Mākoha if it integrates with EU EHR systems, and from when? | EU counsel | `EU-WATCH-005` |
| `EU-Q-006` | Notified-body capacity and timeline for software Class IIb with AI Act designation — which bodies, what queue? | RA consultant | `EU-TASK-006` |

### 9.2 Watch items

| ID | Item | Cadence |
|---|---|---|
| `EU-WATCH-001` | MDR targeted revision (Commission proposal, late 2025) — software provisions, notified-body process changes | Semi-annually |
| `EU-WATCH-002` | AI Act: Digital Omnibus deferral outcome; Commission guidelines on high-risk classification; CEN-CENELEC JTC 21 harmonised standards; AI Office guidance on Article 6 | Quarterly until application date settled; then semi-annually |
| `EU-WATCH-003` | MDCG guidance on AI/MDR interplay (2025-6 and successors); MDCG 2019-11 and 2020-1 revisions | Semi-annually |
| `EU-WATCH-004` | OJ harmonised-standards list under the MDR — status of every `EU-STD-*` row | Before NB application; annually |
| `EU-WATCH-005` | EHDS implementing acts and MDSW interoperability provisions | Annually |
| `EU-WATCH-006` | Product Liability Directive transposition (Member States, by Dec 2026) — software-defect presumptions | Once at transposition; then annually |
| `EU-WATCH-007` | Standards revision: IEC 62304 Ed.2, ISO 13485 review, ISO 14971/TR 24971 cycle, BS/AAMI 34971 progression, ISO/IEC 5259/24029 maturation | Annually |

---

## §10 Ketryx projection — EUROPEAN UNION

| EU deliverable | Ketryx source |
|---|---|
| Annex II technical documentation | Document template over Requirement, Software Item Specification, Risk, Test Case, Anomaly and dependency items, indexed to Annex II §1–6 |
| GSPR checklist | Requirement items with `Relevant standards` carrying the GSPR number beside the Australian EP and the US CFR reference |
| Clinical evaluation report inputs | Test Case items referencing evaluation-corpus cases by ID; clinical investigation records as controlled documents |
| Cyber file (MDCG 2019-16) | Threat-model item types; supply-chain module SBOM; vulnerability workflow |
| AI Act Annex IV documentation | Data-governance records and model descriptions as controlled documents traced to Risk items; logging design as a Software Item Specification |
| PSUR | Generated report over Anomaly, complaint and vigilance items per period |
| Declaration of Conformity | Controlled document with Basic UDI-DI, NB number, harmonised standards list |

---

## §11 Sources

| ID | Source | Currency | Class |
|---|---|---|---|
| `EU-SRC-001` | Regulation (EU) 2017/745 consolidated text | Current **[revision proposal — verify]** | Primary |
| `EU-SRC-002` | MDCG 2019-11 rev.1 — Qualification and classification of software | Current | Primary (guidance) |
| `EU-SRC-003` | MDCG 2021-24 — Classification of medical devices | Current | Primary (guidance) |
| `EU-SRC-004` | MDCG 2020-1 — Clinical evaluation of MDSW; EN ISO 14155:2020 | Current | Primary |
| `EU-SRC-005` | MDCG 2023-3 vigilance; MDCG 2022-21 PSUR | Current | Primary |
| `EU-SRC-006` | Regulation (EU) 2024/1689 (AI Act) | In force **[application-date deferral proposal — verify]** | Primary |
| `EU-SRC-007` | MDCG 2025-6 — MDR/IVDR and AI Act interplay FAQ | 2025 **[verify]** | Primary (guidance) |
| `EU-SRC-008` | Regulation (EU) 2016/679 (GDPR); Commission Decision 2013/65/EU (New Zealand adequacy) | Current | Primary |
| `EU-SRC-009` | Directive (EU) 2022/2555 (NIS2); Regulation (EU) 2024/2847 (CRA) Art 2(2) | Current | Primary |
| `EU-SRC-010` | Regulation (EU) 2025/327 (EHDS) | Current **[verify MDSW provisions and dates]** | Primary |
| `EU-SRC-011` | Directive (EU) 2024/2853 (Product Liability) | Current | Primary |
| `EU-SRC-012` | Commission Implementing Decision (EU) 2021/1182 and amending decisions — harmonised standards under the MDR | **Check current OJ list** | Primary |
| `EU-SRC-013` | Standards-gap review, 2 September 2026 — author's analysis | 2 Sept 2026 | **Author's analysis; rows tagged [recommendation]** |
| `EU-SRC-014` | Australian REG-POSTURE v1.2 `WATCH-REG-007` (Rule 11 watch) — origin of `EU-FIND-003` | 2 Sept 2026 | Internal |

**Confidence note.** Findings resting on Regulation text (`EU-FIND-001`, `002`,
`004`, `005`, `008`, `011`, `012`, `013`, `015`, `016`) are high confidence.
`EU-FIND-003` is high. `EU-FIND-006`, `007` rest on MDCG guidance and are high.
`EU-FIND-009` is high as to the rule and **uncertain as to the application date**
because of the Digital Omnibus process. `EU-FIND-014` is medium. Harmonisation status
in `EU-STD-*` is from the author's knowledge of the OJ list and **must be confirmed**
(`EU-Q-003`, `EU-WATCH-004`).

---

## §12 Census and self-audit

### 12.1 Census

| Prefix | Count | Range |
|---|---|---|
| `EU-FIND` | 16 | 001–016 |
| `EU-OBL` | 16 | 001–016 |
| `EU-STD` | 27 | 001–027 (013 defined in §5.1; numbering aligned to the shared stack; `EU-STD-027` is EU-only) |
| `EU-LAW` | 14 | 001–014 |
| `EU-ASSUME` | 6 | 001–006 |
| `EU-TASK` | 13 | 001–013 |
| `EU-GATE` | 4 | 000–003 |
| `EU-WATCH` | 7 | 001–007 |
| `EU-Q` | 6 | 001–006 |
| `EU-SRC` | 14 | 001–014 |
| **Total** | **123** | |

### 12.2 Self-audit

| # | Check | Result |
|---|---|---|
| 1 | All IDs match `^EU-(FIND|OBL|STD|LAW|ASSUME|TASK|GATE|WATCH|Q|SRC)-[0-9]{3}$` | PASS |
| 2 | Every ID defined exactly once in a table | PASS |
| 3 | Every `EU-TASK-*` names its gate | PASS (13/13) |
| 4 | Every `EU-GATE-*` names predecessors; all exist | PASS (4/4) |
| 5 | Every `EU-ASSUME-*` names attesting party and what it blocks | PASS (6/6) |
| 6 | Every `EU-FIND-*` names at least one `EU-SRC-*` | PASS (16/16) |
| 7 | Every `EU-STD-*` row carries an edition and an EU status | PASS (27/27) |
| 8 | Every instrument known to be in flux carries [currency: verify] | PASS |
| 9 | Shared-stack numbering: `EU-STD-001..026` name the same standards as `STD-001..026` (AU), `NZ-STD-001..026`, `US-STD-001..026` | PASS |
| 10 | No "see REG-POSTURE" for EU-actionable content | PASS |
| 11 | Frontmatter `id_prefixes` ↔ §0.2 ↔ §12.1; range endpoints both ends | PASS (10/10 families) |

---

*Advisory only. EU regulatory counsel and notified-body feedback must confirm before
any commitment. Nothing here authorises placing on the EU market. Items tagged
[recommendation] originate from the author's analysis; items tagged [currency: verify]
name instruments known to be changing and must be read in the primary before reliance.*
