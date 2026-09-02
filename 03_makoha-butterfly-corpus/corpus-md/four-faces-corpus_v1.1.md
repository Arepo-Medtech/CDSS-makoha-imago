---
doc_id: MAK-FFC
title: "The Four Faces Corpus"
version: "1.1"
date: "2026-08-29"
changelog:
  - "v1.1 (2026-08-29): additive fold-in of Addendum J-3 (MAK-J3, Guideline-Prompt Profile) as Annex 1; XC-2 realization note; traceability row and sources for the FDA revised CDS guidance (6 Jan 2026); Appendix B annex census; Appendix C check 9. No v1.0 content altered or removed."
  - "v1.0 (2026-08-29): initial release."
series: "Mākoha research series — volume 3"
status: normative-draft
normative_language: RFC-2119 (MUST / SHOULD / MAY)
req_prefixes: [SPINE, CF, PF, AF, EN, XC]
req_count: 46
companions:
  - "Sleep Tools Dossier (series vol. 1)"
  - "The Stranieri File (series vol. 2)"
  - "Execution Layer Sourcing Map (series vol. 4, doc_id MAK-ELSM) — sourcing verdicts per subsystem"
  - "Addendum J-3 (doc_id MAK-J3, v0.9-proposed) — folded verbatim as Annex 1 of this document; realizes XC-2"
artifact_url: "https://claude.ai/code/artifact/ab807ff5-1e80-4977-8cdb-3f2449e855fc"
change_policy: "Requirement IDs are stable across versions; retired IDs are never reused. Propose changes as argued deviations."
---

<!-- LLM USAGE CONTRACT (additive; not part of the source document)
This file is formatted for prompt work within the Mākoha CDSS Build Ecosystem.
Rules for any LLM consuming this document:
1. Requirement blocks (### SPINE-n / CF-n / PF-n / AF-n / EN-n / XC-n) are NORMATIVE.
   All other prose is INFORMATIVE rationale and context.
2. Cite requirements by bare ID (e.g. "SPINE-7"), never by paraphrase alone.
3. MUST-level requirements are conformance-defining. Do not generate designs, code,
   or documents that violate a MUST without emitting an explicit DEVIATION notice
   naming the ID — this document practices its own doctrine.
4. "Rationale trace" lines bind each requirement to its evidence; keep them attached
   when quoting requirements into downstream documents.
5. The ID census in Appendix B is the authoritative enumeration for validator checks.
6. Anti-requirement blocks are prohibitions with the same force as MUST NOT.
END LLM USAGE CONTRACT -->

# The Four Faces Corpus

A translatable research primer and execution manual for the architecture of a triple-facing clinical decision support system — Clinician Face, Patient Face, Auditor Face, and the Engines beneath them — with every design commitment traced to the evidence that motivates it.

**Document metadata:** Technical corpus · v1.0 · 29 Aug 2026 · third volume in the Mākoha research series · STATUS: normative draft · KEYWORDS: MUST / SHOULD / MAY per RFC 2119 · REQ IDS: SPINE · CF · PF · AF · EN · XC · COMPANIONS: Sleep Tools Dossier · The Stranieri File

## Contents

1. [Part 0 — How to use this document](#part-0--how-to-use-this-document)
2. [Part 1 — Theoretical foundation: the boundary thesis](#part-1--theoretical-foundation-the-boundary-thesis)
3. [Part 2 — The shared spine: justification fabric & reference architecture](#part-2--the-shared-spine)
4. [Part 3 — The Clinician Face](#part-3--the-clinician-face)
5. [Part 4 — The Patient Face](#part-4--the-patient-face)
6. [Part 5 — The Auditor Face](#part-5--the-auditor-face)
7. [Part 6 — The Engines](#part-6--the-engines)
8. [Part 7 — Cross-cutting execution: regulation, low-resource profile, phasing, risks](#part-7--cross-cutting-execution)
9. [Part 8 — Traceability matrix & sources](#part-8--traceability-matrix--sources)
10. [Appendix A — Requirement block format (additive)](#appendix-a--requirement-block-format-additive)
11. [Appendix B — ID census (additive)](#appendix-b--id-census-additive)
12. [Appendix C — Self-audit checks (additive)](#appendix-c--self-audit-checks-additive)
13. [Annex 1 — Addendum J-3: Guideline-Prompt Profile (folded verbatim, v1.1)](#annex-1--addendum-j-3--guideline-prompt-profile-gpp-folded-verbatim)

## Thesis

> Thirty years of CDSS research keeps rediscovering the same failure: systems computerize the guideline and neglect the boundary where formal rules meet messy clinical reality. The evidence base assembled in this series — Chapman's account of meta-rationality, the Miah–Blake–Kerr design theory and its working sleep-clinic artefact, Stranieri's argumentation lineage from Split-Up to GAAM to deployed remote monitoring, and the 2024–25 systematic reviews of CDSS design, XAI, and maternity CDSS — converges on one architectural answer. **Make justification the system's native data structure.** One argument object, rendered in three registers, carries every recommendation, every override, every suppression, and every release. The three faces are not three products; they are three circumrational interfaces to a single justification fabric. The engines are not oracles; they are argument-emitting components whose claims only deterministic evaluation can release. This document turns that finding into buildable requirements.

## Part 0 — How to use this document

This corpus is both a *primer* (it explains why each commitment exists, with citations) and an *execution manual* (it states requirements you can build, test, and audit against). It is designed for translation into a document ecosystem: every requirement carries a stable ID, a normative keyword, and a rationale trace, so it can be lifted verbatim into specifications, conformance checklists, validator rules, and regulatory submissions.

- **Normative language.** MUST = conformance-defining; violating it breaks a safety, integrity, or evidentiary property. SHOULD = strong default; departure requires a recorded justification (the corpus practices its own doctrine). MAY = permitted design freedom.
- **Requirement IDs.** `SPINE-n` cross-face architecture; `CF-n` Clinician Face; `PF-n` Patient Face; `AF-n` Auditor Face; `EN-n` Engines; `XC-n` cross-cutting execution. IDs are stable across future versions; retired IDs are never reused.
- **Rationale traces.** Each requirement cites its evidence in compressed form (e.g. *Bayor 2025*, *GAAM 2006*); Part 8 expands every trace to a full source.
- **Scope.** The corpus specifies architecture and component behaviour. It does not fix implementation technology; where the Mākoha stack (AWS Amplify/Bedrock, Bayesian differential engine, conformal wrapper, corruption engine) is referenced, it is as the reference implementation, not a constraint.

## Part 1 — Theoretical foundation: the boundary thesis

Every formal system in clinical computing has the same anatomy: an ontology that fixes what can be represented, an inference core that manipulates those representations, and a *circumrational boundary* — the human work of translating a nebulous patient into the system's terms and translating the system's outputs back into care. Chapman's analysis of rationality predicts that failures concentrate at this boundary, because the world does not conform to any fixed ontology; the practical remedies he catalogues are precisely the ones available to a system designer: widen the ontology, improve circumrational practice on both sides of the interface, improve material cognitive supports, and hold multiple rational systems side by side when one is not enough.

The empirical CDSS literature confirms the prediction without possessing the vocabulary. Bayor et al.'s systematic review of CDSS design found 37 of 40 systems clinician-facing only, mostly stand-alone, with rigid recommendation structures that "restrict users from incorporating their own perspectives," pervasive alert fatigue, and even covert-surveillance anxiety — a catalogue of circumrational neglect. Cockburn et al.'s maternity meta-analysis found benefit (pooled OR 1.69) drowned in heterogeneity: what works in one context fails to transfer, which is the nebulosity thesis in epidemiological form. Abbas et al.'s XAI meta-analysis found explanation technology everywhere in the lab and almost nowhere validated for fidelity, trust, or real-world usability — explanations produced because the genre demands them. And the one artefact program that did most things right — the Blake–Kerr–Gammack sleep CDSS, theorized by Miah, Blake & Kerr into a generic architecture and six design principles — honestly stopped at the judgment boundary, computerizing the ICSD criteria while citing Croskerry to leave discretion outside the system, and leaving its third face a read-only administrative viewer.

Three findings from this series supply the constructive move:

- **Justification is the explanation form that works for every stakeholder.** The sleep CDSS's Toulmin argument trees — claim, grounds, warrant — descend from Stranieri's Split-Up, built for *discretionary* judicial reasoning, and were explicitly designed "to meet expectations of different users." Feature attribution (SHAP, Grad-CAM) answers "which inputs moved the number"; an argument answers "why is this defensible" — the question clinicians, patients, and auditors actually ask.
- **GAAM formalizes the guideline/deviation relationship.** Stranieri's Generic/Actual Argument Model separates the *generic argument* — a community-ratified template of admissible data, warrants, and claims — from the *actual argument* a specific case instantiates. A justified deviation is then not an exception outside the system but a first-class object inside it: an actual argument whose warrant departs from the generic template, with the departure recorded, reasoned, and reviewable.
- **The auditor face is the unclaimed keystone.** No system in the reviewed literature serves the compliance stakeholder as more than a viewer, yet the compliance apparatus is what punishes meta-rational practice and drives rigidity everywhere upstream. Reframing "non-compliance" as "documented rational intent" attacks the root cause; everything in this corpus is arranged so that the auditor face is a read model over evidence the system produces natively, not a bolted-on surveillance layer.

> The doctrine in one sentence: the system computerizes criteria, never discretion — and gives discretion a data structure instead.

## Part 2 — The shared spine

The spine is what makes three faces one system: a single justification fabric that every component writes to and every face reads from, in its own register. The reference architecture extends the Miah–Blake–Kerr layered design (role interfaces → shared tools → argument-tree explanation → knowledge base → swappable ontology), replacing its read-only administration face with an active auditor face and inserting the deviation and versioning machinery the original never had.

### Reference architecture (layered)

```text
┌──────────────────┬──────────────────────┬───────────────────────────────┐
│  Clinician Face  │    Patient Face      │  Auditor Face                 │
│  clinical        │    plain-language    │  compliance register ·        │
│  register        │    register          │  read model                   │
└──────────────────┴──────────────────────┴───────────────────────────────┘
             ↓ ↑  per-face gateways (authn, authz, register rendering)
┌──────────────────────────────────────────────────────────────────────────┐
│                        JUSTIFICATION FABRIC                              │
│  GenericArgument · ActualArgument · Deviation ·                          │
│  append-only, hash-chained, version-pinned (GAAM + Toulmin schema)       │
└──────────────────────────────────────────────────────────────────────────┘
             ↓ ↑  engine contract: arguments in, arguments out
┌────────────────┬──────────────────┬───────────────────┬─────────────────┐
│ Guideline      │ Bayesian         │ Conformal         │ Corruption      │
│ Compiler       │ Differential     │ Wrapper           │ Engine          │
│ narrative →    │ posteriors as    │ coverage-         │ standing        │
│ computable →   │ qualifiers       │ guaranteed        │ rebuttal        │
│ GenericArgument│                  │ uncertainty       │ generator       │
└────────────────┴──────────────────┴───────────────────┴─────────────────┘
             ↓ ↑
┌──────────────────────────────────────────────────────────────────────────┐
│ KNOWLEDGE PLANE — terminologies (SNOMED CT, ICD-10) · computable         │
│ guidelines (FHIR CPG / CQL / WHO SMART L3) · tiered evidence library ·   │
│ plural, versioned, swappable                                             │
└──────────────────────────────────────────────────────────────────────────┘
             ↓ ↑
┌──────────────────────────────────────────────────────────────────────────┐
│ DATA PLANE — FHIR: QuestionnaireResponse · Observation · Condition ·     │
│ GuidanceResponse · DetectedIssue · Provenance · AuditEvent · Consent     │
└──────────────────────────────────────────────────────────────────────────┘
```

### The canonical argument object

Every recommendation, alert, suppression, override, and release in the system is an instance of one schema, whose elements are Toulmin's — and whose element assignments are not decorative: each maps to a concrete Mākoha component.

| Toulmin element | Definition | What supplies it |
|---|---|---|
| **Claim** | The assertion released to a face (diagnosis candidate, recommendation, alert, suppression) | Deterministic evaluation of the argument tree — never an ML output directly |
| **Grounds** | The patient-specific data the claim rests on | Data plane resources, each with provenance and capture context |
| **Warrant** | The inference rule licensing grounds → claim | A GenericArgument node: guideline criterion, Bayesian likelihood structure, or ratified local rule — always versioned |
| **Backing** | Why the warrant deserves trust | The tiered evidence library entry behind the warrant (evidence tier, source, currency) |
| **Qualifier** | The strength and uncertainty of the claim | Posterior probabilities and conformal prediction sets with stated coverage — uncertainty is a first-class schema element, not a footnote |
| **Rebuttal** | Known conditions under which the claim fails | Corruption-engine findings, contraindications, DetectedIssue conflicts, and unresolved guideline disagreements |

### Spine requirements

### SPINE-1 (MUST)
**Statement:** Every claim that crosses a face boundary — recommendation, alert, alert suppression, override acknowledgment, triage decision — is represented as an ActualArgument instantiating (or explicitly deviating from) a versioned GenericArgument. No component may release a bare score, label, or unexplained alert to any face.
**Rationale trace:** GAAM 2006; Blake 2016 argument trees; Abbas 2025 (attribution ≠ justification); Nunes & Jannach 2017.

### SPINE-2 (MUST)
**Statement:** The argument schema carries all six Toulmin elements; Qualifier and Rebuttal are mandatory, not optional. An argument without a stated qualifier (uncertainty) or with an empty rebuttal slot that the corruption engine has findings for is invalid and MUST NOT be released.
**Rationale trace:** Toulmin 1958; conformal-prediction doctrine (Mākoha); Cockburn 2024 heterogeneity (context-failure modes are rebuttals, not surprises).

### SPINE-3 (MUST)
**Statement:** One argument object renders in three registers — clinical, plain-language, compliance — from a shared ontology and controlled vocabulary. Register renderers may compress or re-order; they MUST NOT add, remove, or reweight argument content per audience.
**Rationale trace:** Miah–Blake–Kerr Principle 2 (shared ontology); Split-Up 1998 ("expectations of different users"); patient-education findings in Blake 2016.

### SPINE-4 (MUST)
**Statement:** The justification fabric is append-only and tamper-evident (hash-chained). Standard bindings: recommendations as FHIR `GuidanceResponse`, decision lineage as `Provenance`, access as `AuditEvent`, conflicts as `DetectedIssue`, permissions as `Consent`, intake as `QuestionnaireResponse`. Corrections are new entries that supersede, never edits.
**Rationale trace:** auditor-face evidentiary needs; TGA Essential Principles conformity evidence; Stranieri EHR-dispute work (contested records need untampered lineage).

### SPINE-5 (MUST)
**Statement:** Every argument pins the versions of everything that produced it: guideline/GenericArgument version, terminology release, evidence-library snapshot, engine model version, and engine configuration hash. Any historical decision MUST be replayable bit-for-bit from its pinned versions.
**Rationale trace:** the ICSD-2 freeze that stranded the sleep CDSS; regulatory replay obligations; drift management (EN-8).

### SPINE-6 (MUST)
**Statement:** The knowledge plane supports plural, co-resident guideline systems. When two applicable GenericArguments conflict, the conflict is materialized as a DetectedIssue attached to both arguments and surfaced to the clinician face; the system MUST NOT silently rank, merge, or suppress one side.
**Rationale trace:** Stranieri coalescing-medical-systems line; Chapman on alternative rational systems; the meta-rational design note (conflicting-guideline synthesis).

### SPINE-7 (MUST)
**Statement:** "ML proposes and tests; only arithmetic releases." Probabilistic and generative components may propose grounds, candidate warrants, and draft arguments; release to any face requires deterministic evaluation of the completed argument tree against its GenericArgument. The releasing evaluator is versioned, testable, and free of learned parameters.
**Rationale trace:** Mākoha core doctrine; TGA exemption criterion (c) transparency language as the design target even for classified software (XC-1).

### SPINE-8 (MUST)
**Statement:** Deviation machinery exists at every recommendation point. A face-side actor with clinical authority can depart from any GenericArgument; the departure produces a Deviation object (structured reason taxonomy + free text + severity tier + author identity) linked to the actual argument. The system computerizes criteria, never discretion — and never blocks a deviation except where a deterministic safety class applies.
**Rationale trace:** the gap every source leaves open — Blake/Croskerry boundary, Bayor rigidity findings, GAAM generic/actual split; auditor-face reframing (AF-3).

### SPINE-9 (SHOULD)
**Statement:** The fabric exposes one read API with register-scoped projections rather than per-face databases, so the three faces can never drift into three truths. Face-specific caches are derived, disposable, and rebuildable from the ledger.
**Rationale trace:** single-source-of-truth integrity; audit replay economics.

## Part 3 — The Clinician Face

**What the research revealed.** Clinicians are not failing to use CDSS because they distrust computers; they are defending their circumrational boundary against systems that neglect it. Bayor et al. found the dominant failure modes are rigid recommendation structures, workflow mismatch ("information only several steps ahead of the operational workflow"), information overload and prompt fatigue, and trust collapse when recommendations conflict with clinical judgment and cannot be interrogated. Stranieri's ward-rounds field study shows bedside reasoning is social, narrative, and context-saturated — not a form-filling exercise — and his MDT study shows the consequential decisions are often *group* decisions. The Blake program demonstrated the successful counter-pattern: move routine data capture out of the consultation entirely, deliver pre-digested, assimilable reports, triage before the first visit, and explain every criterion hit as an argument. Croskerry's dual-process account, cited by that program as its own boundary marker, tells us what not to attempt: the system supports judgment; it does not simulate it.

### Component inventory

| Component | Function | Research anchor |
|---|---|---|
| Consult-Prep Composer | Pre-consultation synthesis of intake, monitoring, and history into one assimilable brief; triage-urgency proposal with its argument | Blake 2014/2016 (history-taking out of consult; 3-tier urgency; "patient-driven not form-driven") |
| Differential Board | Ranked diagnostic hypotheses; each row expands to its full argument tree; qualifiers always visible; conflicts (DetectedIssue) shown side-by-side, never pre-resolved | Mākoha Bayesian engine; SPINE-2/6; Bayor validity-trust findings |
| Deviation Composer | One-interaction justified departure: structured reason taxonomy + free text + severity; writes the Deviation object; confirms what the record will show | SPINE-8; GAAM; auditor reframing (AF-3) |
| Alert Governor | Context-conditional alert suppression whose suppression rules are themselves GenericArguments — ratified, versioned, argued, and audited; per-clinician suppression budget with fabric-visible spend | Bayor fatigue findings; Kesselheim 2011 (alert fatigue vs litigation risk, cited in Miah 2020); contextual-alerting design note |
| MDT / Group Mode | Multi-author actual arguments: participants contribute grounds and warrants under their own identity; disagreement is recorded, not averaged | Stranieri MDT 2016; reasoning-communities books; Delphi accuracy-vs-consensus caution |
| Argument Renderer (clinical register) | Toulmin-structured explanation at criterion granularity; drill-down from claim to backing to evidence tier; never a naked score, never a feature-attribution heatmap as primary explanation | Blake argument trees; Abbas 2025 gaps; Nunes & Jannach taxonomy |

### Clinician Face requirements

### CF-1 (MUST)
**Statement:** Workflow placement follows the Blake pattern: data capture happens before the consultation (patient-side, PF-1), synthesis happens before the encounter (Consult-Prep Composer), and in-consultation interaction is read-and-decide. The face MUST NOT demand in-consultation data entry beyond confirmation and deviation actions.
**Rationale trace:** Blake 2014 (physicians spend consult time on routine questions); Miah–Blake–Kerr Principle 4 (workflow fit).

### CF-2 (MUST)
**Statement:** Every displayed recommendation exposes its full argument tree within one interaction, at the granularity of individual criteria (the sleep CDSS's per-criterion decision points are the reference grain). The qualifier (posterior + conformal set) renders adjacent to every claim — no claim without its uncertainty.
**Rationale trace:** SPINE-1/2; Blake 28 decision points; TGA criterion (c) transparency language.

### CF-3 (MUST)
**Statement:** Deviation is always available, never punished by friction: at most one interaction to open, structured reason plus optional free text, and an explicit preview of how the deviation will appear to the auditor face. The face MUST NOT use dark patterns (nagging, repeated confirmation, delay) to discourage justified departure.
**Rationale trace:** SPINE-8; Bayor ("users may feel obligated to follow system recommendations"); rationality-theater risk (XC-6 risk register).

### CF-4 (MUST)
**Statement:** Hard stops are reserved for the deterministic safety class (arithmetic contraindication with ratified GenericArgument backing). Everything else is advisory. Every hard stop's firing is itself an argument in the fabric, reviewable and contestable.
**Rationale trace:** SPINE-7/8; alert-fatigue evidence; Croskerry boundary.

### CF-5 (MUST)
**Statement:** Alert suppression is governed, not ad hoc: a suppression rule is proposed, argued, ratified as a GenericArgument, versioned, and its firings logged. Silent, unlogged suppression is prohibited — suppression without audit converts alert fatigue into invisible risk.
**Rationale trace:** contextual-alerting design note, hardened against its own abuse; SPINE-4.

### CF-6 (SHOULD)
**Statement:** Group decisions (MDT, ward round) are captured as multi-author arguments preserving who contributed which grounds and warrants and where disagreement remained. The system SHOULD NOT present a group output as unanimous when the fabric knows otherwise.
**Rationale trace:** Stranieri MDT 2016; Delphi consensus-vs-accuracy finding (TFSC 2011).

### CF-7 (MUST)
**Statement:** Face evaluation uses clinicians who did not co-design the system, n materially greater than the design panel, measuring at minimum: justified-override rate, alert positive-predictive value, time-in-consult delta, and comprehension of rendered arguments. The Blake program's n=2 co-designer evaluation is the documented anti-pattern.
**Rationale trace:** Sleep Tools Dossier assessment; Cockburn 2024 (evaluation heterogeneity); XC phasing gates.

### CF-8 (MAY)
**Statement:** Provide narrative-register summaries (a prose account of the case's argument state) for handover and referral, generated from the fabric and marked as derived content.
**Rationale trace:** ward-rounds narrative finding; SPINE-3 register discipline.

### Clinician Face anti-requirements

- Never release a bare probability, score, or ranking without its argument and qualifier (violates SPINE-1/2).
- Never auto-act on a recommendation — ordering, prescribing, and referral remain human acts the system prepares but does not perform.
- Never treat an unjustified override as an error state; absence of justification is a prompt, then a fabric fact — not a block.
- Never surface auditor-face analytics (league tables, deviation rates) inside the clinician face; surveillance anxiety is a documented adoption killer (Bayor).

## Part 4 — The Patient Face

**What the research revealed.** The patient face is where the literature's largest quantified gap sits: 37 of 40 reviewed CDSS served clinicians only, and Bayor et al. name dual-facing design as the structural opening for virtual care. The Blake program supplies the working patterns: intake instruments completed at home, validated at entry, that make the consultation patient-driven; and a self-monitoring loop (the diary's day-by-day graph) whose immediate visual feedback made patients reflect on their own patterns — evaluated usable across ages and computer literacy by 267 users. Stranieri contributes the custody doctrine: the Patient Centric Agent that mediates access, routing, and storage of the patient's own data stream (his repository-allocation ML paper is that agent's decision policy), plus patient-empowered EHR work and an open-banking data-rights analogy. The meta-rational layer adds the requirement the literature never reaches: patient values and priorities as first-class data that can legitimately reweight decisions — with the mapping from a life goal to a clinical priority treated as governed ontological remodeling, never silent inference.

### Component inventory

| Component | Function | Research anchor |
|---|---|---|
| Intake Instruments | Structured history and condition-specific questionnaires done at home, validated at entry, feeding the fabric as QuestionnaireResponse with capture context | Blake Q-SHOQ pattern; 267-user usability evidence |
| Self-Monitoring Loop | Diary/observation capture with immediate visual feedback to the patient; the same data stream feeds Consult-Prep | Blake sleep-diary graph; Anidra RPM ingestion |
| Values & Priorities Module | Elicited trade-off preferences (mobility vs longevity, cost sensitivity, side-effect tolerances) stored as structured Goals; enters engine weighting only through ratified mappings | Meta-rational design note; Chapman ontological-remodeling constraint; shared-decision-making literature via Blake 2016 |
| Personal Data Agent | Custody, consent ledger (FHIR Consent), access visibility ("who saw what, when, under which argument"), and repository routing policy | Stranieri PCA (IEEE Access 2018); repository allocation (HIJ 2020); patient-empowered EHR 2019 |
| Argument Renderer (plain register) | The same argument tree in plain language: what we think, why, how sure, what would change it, and what you can choose — including honest rendering of clinician deviations ("your doctor departed from the standard guideline because…") | SPINE-3; "demystified uncertainty" note; Blake patient-education finding |
| Low-Resource Delivery Profile | Offline-first client, low-bandwidth sync, SMS/IVR fallback tier, cheap-device support, RPM device ingestion | North star; Anidra deployment reality; teledentistry cost evidence; WHO SMART Guidelines alignment |

### Patient Face requirements

### PF-1 (MUST)
**Statement:** Routine history and condition-specific data capture happens on the patient face, before the encounter, with point-of-entry validation. Instruments are versioned artifacts in the knowledge plane, with their target population and validation status recorded (the missing-instrument case — e.g. no OSA screen tuned to women — is representable, not hidden).
**Rationale trace:** Blake 2014/2016; CF-1 pairing; instrument-gap finding in Blake 2014.

### PF-2 (MUST)
**Statement:** Every patient-visible recommendation renders in the plain register from the same argument object the clinician saw — including qualifiers ("how sure we are") and the existence of any deviation. The patient face MUST NOT receive a sanitized or divergent version of the decision.
**Rationale trace:** SPINE-3; trust and shared-decision-making evidence; register discipline.

### PF-3 (MUST)
**Statement:** Patient values and priorities are captured as explicit, patient-authored structured data. A mapping from a stated life goal to a clinical weighting (e.g. mobility-over-longevity) takes effect only after ratification into the knowledge plane as a versioned mapping — never by runtime inference from free text. The patient can see and revoke every active mapping.
**Rationale trace:** Chapman (ontological remodeling cannot be done rationally, so it must be governed); value-alignment design note; SPINE-7.

### PF-4 (MUST)
**Statement:** The Personal Data Agent gives the patient a complete access ledger (every read of their record, bound to the AuditEvent and the argument context it served) and consent controls that the data plane actually enforces. Repository routing decisions are policy-driven and explainable in the plain register.
**Rationale trace:** Stranieri PCA + repository allocation; AF evidentiary symmetry — the patient audits too.

### PF-5 (MUST)
**Statement:** Self-monitoring capture returns immediate, legible visual feedback to the patient on their own data. Feedback visualisations are the same artifacts the clinician sees (register-styled), preserving the shared vocabulary.
**Rationale trace:** Blake diary finding (feedback → reflection → engagement); Miah–Blake–Kerr Principle 2.

### PF-6 (MUST)
**Statement:** The accessibility floor is non-negotiable: usable at low literacy and low computer literacy, WCAG-conformant, and functional offline with deferred sync. The low-resource profile — bandwidth budget, device floor, SMS/IVR fallback for intake and reminders — is a release gate, not an aspiration.
**Rationale trace:** Blake accessibility-first design; north star; Anidra field constraints; XC-3.

### PF-7 (SHOULD)
**Statement:** Align patient-face computable content with WHO SMART Guidelines artifact layers (narrative → operational → machine-readable FHIR) so low-resource deployments can adopt nationally adapted guideline content without re-authoring.
**Rationale trace:** WHO SMART Guidelines program; north star; SPINE-6 pluralism.

### PF-8 (MUST)
**Statement:** The patient face presents recommendations and choices; it does not diagnose. Diagnostic claims render to patients only after clinician release, in the plain register, with the releasing clinician identified.
**Rationale trace:** regulatory posture (XC-1); Blake precedent (patients received diary feedback, not the physician report).

### Patient Face anti-requirements

- Never infer values, priorities, or risk tolerance from behavioural signals and apply them silently (violates PF-3).
- Never render uncertainty as false confidence — a point estimate without its set is a schema violation, in the plain register as everywhere.
- Never make consent a wall of text: consent objects are granular, revocable, and mirrored in the access ledger.
- Never gate core function on connectivity, device class, or app-store availability in low-resource profiles.

## Part 5 — The Auditor Face

**What the research revealed.** This face has no precedent to copy — that is the finding. The Miah–Blake–Kerr architecture's third interface was a read-access administrative viewer; Bayor et al.'s review stops at dual-facing; nobody in the corpus serves the compliance stakeholder as a designed-for user. Yet the compliance apparatus is the load-bearing cause of upstream rigidity: a clinician who deviates wisely is punished by machinery that can only read deviation as error, so systems are built rigid to keep audits clean. The constructive materials exist in pieces: GAAM supplies the formalism (deviation = actual argument departing from a generic template, reviewable at the warrant level); Stranieri's online-dispute-resolution work supplies the contested-record workflow; the fabric (Part 2) supplies evidence that is append-only, version-pinned, and replayable; and the corruption engine supplies the antibody against the face's own failure mode — justification theater, where templated rationales game the ledger. TGA criterion (c)'s language — recommendations whose basis a professional can independently verify, with logic and evidence clearly referenced — describes, almost verbatim, what this face's export must demonstrate.

### Component inventory

| Component | Function | Research anchor |
|---|---|---|
| Justification Ledger | The read model over the fabric: every decision, argument, deviation, suppression, and access event, queryable and exportable | SPINE-4/5; FHIR Provenance/AuditEvent |
| Deviation Review Workbench | Queues by severity, pattern, and recency; each deviation opens as the full argument pair (generic vs actual) with the departure highlighted at the warrant node | GAAM; AF-3 reframing |
| Compliance Projector | Maps argument states onto external compliance vocabularies (quality metrics, accreditation standards, billing integrity): "guideline-concordant," "documented justified deviation," "undocumented deviation," "under review" | Quality-metric-adjustment design note; reframing doctrine |
| Theater Detector | The corruption engine pointed at justifications: boilerplate similarity, copy-paste clustering, temporal anomalies (batch back-fill), reason-code/free-text mismatch — flags for human review only | Rationality-theater risk; Mākoha corruption engine repurposed |
| Guideline Feedback Loop | Aggregates deviation patterns into change proposals against specific GenericArgument nodes; proposals enter a governed ratification workflow and, if accepted, version the template | Systemic-feedback design note; Chapman ontological remodeling as governed process; SPINE-5 versioning |
| Dispute Mode | Structured ODR workflow for contested decisions and records: positions as arguments, mediated exchange, resolution recorded into the ledger | Stranieri ODR for medical disputes 2020; EHR disputes & emotional intelligence 2020 |
| Regulator Export | Conformity bundles: replayable decision sets with pinned versions, argument transparency demonstrating reviewable basis, adverse-event linkage | TGA Essential Principles; SaMD evidence posture (XC-1) |

### Auditor Face requirements

### AF-1 (MUST)
**Statement:** The auditor face is a read model. It holds no write path into clinical data, arguments, or deviations; its only writes are review states, dispute records, and guideline-change proposals — each itself an argued, attributed fabric entry.
**Rationale trace:** separation of powers; Bayor surveillance-anxiety finding; AF anti-capture.

### AF-2 (MUST)
**Statement:** Every reviewable item presents as an argument pair — the GenericArgument (what the ratified guideline licensed, at its pinned version) and the ActualArgument (what happened) — with departures localized to specific warrant nodes. Review verdicts attach at node granularity, not case granularity.
**Rationale trace:** GAAM 2006; Split-Up warrant-level reasoning; replayability (SPINE-5).

### AF-3 (MUST)
**Statement:** The compliance vocabulary distinguishes, as first-class states: guideline-concordant; documented justified deviation; documented deviation under review; undocumented deviation. External reporting maps from these states. "Documented justified deviation" is a compliant state, not a mitigated violation — this reframing is the face's reason to exist.
**Rationale trace:** the series' central gap; the "justified personalization" doctrine; quality-metric adjustment note.

### AF-4 (MUST)
**Statement:** Theater detection runs continuously over the justification ledger — boilerplate similarity, duplication clusters, temporal anomalies, taxonomy/free-text divergence — and produces flags for human review. Flags MUST NOT auto-sanction, auto-downgrade compliance states, or feed individual performance management without a governed human process.
**Rationale trace:** rationality-theater risk (Chapman); corruption-engine doctrine; procedural fairness.

### AF-5 (MUST)
**Statement:** Deviation aggregates feed a governed guideline-change workflow: recurring justified departures against a GenericArgument node generate a change proposal carrying its evidence; ratification produces a new template version; the old version remains pinned to its historical decisions. Ontology and template change is a human, governed act — never automatic.
**Rationale trace:** systemic-feedback loop design note; Chapman (ontological remodeling is prior to rationality); SPINE-5.

### AF-6 (SHOULD)
**Statement:** Dispute mode implements a structured ODR workflow — contested decision, positions entered as arguments, mediated exchange, outcome ledgered — usable for payer disputes, patient record challenges, and inter-clinician disagreement escalation.
**Rationale trace:** Stranieri Re-Consider 2008 → medical ODR 2020; BIT 2020 emotional-intelligence findings.

### AF-7 (MUST)
**Statement:** Regulator export produces self-contained conformity bundles: the decision set, pinned versions, replay attestation, argument transparency (basis, logic, evidence references), deviation states, and adverse-event linkage — the operational realization of "the health professional can independently verify the basis."
**Rationale trace:** TGA criterion (c) language; Essential Principles; XC-1.

### AF-8 (SHOULD)
**Statement:** Aggregate views default to system-level and guideline-level lenses; clinician-level lenses require a governed access grant, are logged to the fabric, and are visible to the affected clinician.
**Rationale trace:** surveillance-anxiety evidence; sustaining CF trust while preserving audit capability.

### Auditor Face anti-requirements

- Never a write path into clinical content — the auditor observes and proposes; it does not practice medicine (AF-1).
- Never automatic sanction, automatic metric downgrade, or automatic clinician flagging from detector output (AF-4).
- Never real-time individual surveillance dashboards; review is retrospective and governed (AF-8).
- Never resolve a plural-guideline conflict by fiat in the compliance projection; conflicts project as conflicts (SPINE-6).

## Part 6 — The Engines

**What the research revealed.** Three durable engineering lessons and one synthesis. Lesson one, from the Blake artefact: *decompose*. Twenty-eight small, testable, per-criterion decision units proved "flexible and easy to change in the event of additions to or changes in the diagnostic criteria" — monolithic inference is where guideline drift goes to hide. Lesson two, from the Miah–Blake–Kerr architecture: *engine agnosticism* — the reasoning layer explicitly admits rule bases, statistical models, pattern recognition, or Bayesian models behind one interface, and the ontology beneath it is swappable. Lesson three, from Abbas et al.: the XAI mainstream's post-hoc attributions do not meet any face's actual question, and unvalidated explanation is a liability, not a feature. The synthesis is this corpus's sharpest structural claim: **Mākoha's engine components map one-to-one onto Toulmin's argument elements** — the Bayesian differential supplies claims with posteriors, the tiered evidence library supplies backing, the conformal wrapper supplies the qualifier, and the corruption engine supplies rebuttals. The argument schema is not documentation added after inference; it is the engine plane's output contract.

### The engine contract

```text
interface Engine {
  // Everything an engine consumes is versioned and pinned
  inputs:  Grounds[]            // FHIR-sourced, provenance-bearing
  context: GenericArgument      // the template node(s) in scope, at pinned version

  // Everything an engine produces is an argument fragment — never a released claim
  propose(): ActualArgumentDraft {
    claim:     Assertion         // candidate only
    grounds:   Grounds[]         // what it actually used
    warrant:   WarrantRef        // versioned rule/model licensing the step
    backing:   EvidenceTierRef   // from the tiered evidence library
    qualifier: Uncertainty       // posterior + conformal set + coverage
    rebuttals: Defeater[]        // known failure conditions, incl. corruption findings
    pins:      VersionSet        // model, config hash, terminology, guideline
  }
}
// Release path (deterministic, learned-parameter-free):
// evaluate(ActualArgumentDraft, GenericArgument) → released | held | conflict(DetectedIssue)
```

### Component inventory

| Component | Function | Research anchor |
|---|---|---|
| Guideline Compiler | Narrative guideline → operational logic → computable artifacts (FHIR CPG / CQL; WHO SMART machine-readable layer) → GenericArgument templates with evidence-tier backing per warrant node | WHO SMART layer model; SPINE-5/6; Blake per-criterion grain |
| Bayesian Differential Service | Posterior computation over the differential; likelihood structures are warrants, posteriors are qualifier inputs; decomposed per criterion cluster, not monolithic | Mākoha core; Miah 2020 reasoning-agnostic layer ("likelihood ratios or Bayesian models") |
| Conformal Wrapper | Distribution-free prediction sets with stated coverage wrapped around every probabilistic output; the qualifier discipline that makes SPINE-2 satisfiable | Mākoha doctrine; Abbas fidelity gap (uncertainty must be validated, not asserted) |
| Corruption Engine | Standing adversary: perturbs inputs, hunts failure regions, and publishes findings as rebuttals attached to the warrants they defeat; second duty as the AF-4 theater detector | Mākoha doctrine; Cockburn heterogeneity (context failure is the expected case); Toulmin rebuttal slot |
| Deterministic Evaluator | The release gate: evaluates completed argument drafts against GenericArgument templates; versioned, exhaustively unit-tested, no learned parameters | SPINE-7 ("only arithmetic releases"); TGA criterion (c) transparency target |
| Evaluation Firewall | Sequestered corpus and harness; nothing that trained or tuned an engine may score it; replay harness re-executes historical decisions against pinned versions | Mākoha doctrine; CF-7 evaluation-incest lesson generalized |

### Engine requirements

### EN-1 (MUST)
**Statement:** Every engine — rule-based, Bayesian, ML, or LLM-assisted — implements the engine contract: consumes versioned grounds and template context, emits ActualArgument drafts with all six Toulmin elements populated, and never releases directly to a face.
**Rationale trace:** SPINE-1/2/7; Miah 2020 engine-agnostic layer, hardened into a contract.

### EN-2 (MUST)
**Statement:** Inference is decomposed to criterion granularity: small engines per guideline criterion or criterion cluster, independently versioned, testable, and swappable. A guideline change recompiles affected GenericArgument nodes and their engines without touching the rest of the plane.
**Rationale trace:** Blake 28 decision points ("flexible and easy to change"); ICSD-freeze failure mode; SPINE-5.

### EN-3 (MUST)
**Statement:** The Guideline Compiler is the only path by which clinical logic enters the engine plane: narrative → computable → GenericArgument, with authorship, evidence tier, and ratification recorded per warrant node. Hand-coded rules outside the compiler pipeline are prohibited.
**Rationale trace:** SPINE-5/6 integrity; AF-5 feedback loop needs one change surface; WHO SMART layering.

### EN-4 (MUST)
**Statement:** Every probabilistic claim carries a conformal qualifier: prediction set and stated coverage, computed by a wrapper that is itself validated on the firewalled corpus. A posterior without coverage semantics does not satisfy SPINE-2.
**Rationale trace:** Mākoha conformal doctrine; Abbas (explanation fidelity unvalidated across the field).

### EN-5 (MUST)
**Statement:** The corruption engine runs as a standing adversary against every released engine version; its confirmed findings are published as rebuttal objects bound to the defeated warrants and are face-visible wherever those warrants fire. An engine version with unacknowledged confirmed findings MUST NOT release.
**Rationale trace:** Mākoha doctrine; SPINE-2 rebuttal mandate; Cockburn transfer-failure evidence.

### EN-6 (MUST)
**Statement:** LLM components follow the classified posture: authoring-time and test-time uses (guideline compilation assistance, instrument drafting, corruption-case generation, register rendering drafts) are permitted as proposers under human ratification; runtime clinical inference by LLM is a classification-attracting change managed under the regulatory fork, and in every case remains subject to SPINE-7 — an LLM never releases.
**Rationale trace:** Mākoha LLM Class 1–3 vs 4+ doctrine; TGA note that AI-enabled CDSS does not meet the exemption criteria.

### EN-7 (MUST)
**Statement:** The evaluation firewall is absolute: corpora used for training/tuning are disjoint from scoring corpora; evaluation code is versioned; and every reported performance figure is reproducible from the firewall by a party with no write access to the engines.
**Rationale trace:** Mākoha firewalled-corpus doctrine; CF-7 (the n=2 co-designer lesson at engine scale).

### EN-8 (MUST)
**Statement:** Drift is managed as versioned change, never silent update: terminology releases, guideline versions, evidence-library snapshots, and model weights all pin per decision (SPINE-5); scheduled replay of a sentinel decision set across versions detects behavioural drift before it reaches a face.
**Rationale trace:** SPINE-5; regulatory change management; sentinel-replay practice.

### EN-9 (SHOULD)
**Statement:** Engines expose calibration and coverage telemetry to the auditor face's system lens (not the clinician face), so degradation is a governance event with an owner rather than a surprise.
**Rationale trace:** AF-8 lens discipline; EN-8.

## Part 7 — Cross-cutting execution

### Regulatory posture (Australia first)

### XC-1 (MUST)
**Statement:** Classification honesty: the TGA's CDSS exemption requires all three criteria — (a) sole purpose of supporting a health professional's recommendation, (b) no direct processing of medical-device images/signals, (c) does not replace clinical judgment, with transparent, independently verifiable logic — and the TGA states plainly that an AI-enabled CDSS will not meet them. Mākoha's diagnostic engine therefore plans for ARTG inclusion and SaMD classification (the Addendum J fork), while criterion (c)'s transparency language is adopted as the design target the fabric must demonstrably meet: every recommendation's basis independently reviewable, its logic and evidence clearly referenced (AF-7).
**Rationale trace:** TGA CDSS guidance (criteria a/b/c verbatim review, Oct 2025 revision); Mākoha regulatory fork.

### XC-2 (MAY)
**Statement:** Ship a scoped guideline-prompt profile (recommendations from ratified guidelines, no device-signal processing, no diagnosis generation) as a separately-supplied configuration where an exempt or lower-classification posture serves deployment — provided the profile boundary is enforced in code, not policy.
**Rationale trace:** TGA exempt-CDSS scope ("prompts, alerts, reminders, and recommendations… apply evidence-based clinical guidelines"); low-resource market entry.

> **Realization note (v1.1, additive):** XC-2 is realized by **Addendum J-3 — Guideline-Prompt Profile (MAK-J3, v0.9-proposed)**, folded verbatim into this document as Annex 1. J-3 specifies the exempt-tier build target: TGA criteria (a)(b)(c) mapped to enforcement families GPP-4..7, four-layer code enforcement GPP-8..11, tier-promotion protocol GPP-14, obligations register, jurisdiction map (including the FDA revised CDS guidance of 6 Jan 2026 and EU MDR Rule 11), and a capability matrix in which excluded functions are structurally absent from the artifact, never disabled by configuration.

### Low-resource deployment profile

### XC-3 (MUST)
**Statement:** The low-resource profile is a first-class build target with its own release gate: offline-first faces with deferred sync; bandwidth and device floors stated and tested; terminology and guideline packs installable per jurisdiction (WHO SMART-aligned where available); RPM ingestion from low-cost certified devices (the Anidra class); and graceful degradation to SMS/IVR for intake, reminders, and escalation.
**Rationale trace:** north star; Anidra field reality; teledentistry cost evidence (asynchronous beats face-to-face on cost); Cockburn (44% of maternity CDSS evidence is LMIC — the demand is proven).

### XC-4 (SHOULD)
**Statement:** Treat guideline localization as pluralism, not forking: a jurisdiction's adaptation is a sibling GenericArgument lineage with its own ratification trail, co-resident with the source lineage under SPINE-6 — so low-resource adaptations remain first-class, comparable, and upgradeable.
**Rationale trace:** WHO SMART adaptation model; Stranieri coalescing-systems practice; SPINE-6.

### Phased execution plan

| Phase | Builds | Gate to exit |
|---|---|---|
| `P0 · Spine` | Justification fabric, argument schema, deterministic evaluator, version pinning, guideline compiler for one guideline domain | Replay attestation passes; one guideline compiled end-to-end to GenericArguments; SPINE-1..9 conformance suite green |
| `P1 · Clinician MVP` | Consult-Prep, Differential Board, Deviation Composer, Alert Governor on one clinical pathway | CF-7 evaluation with non-designer clinicians; justified-override and alert-PPV baselines recorded |
| `P2 · Auditor read` | Justification Ledger, Deviation Review Workbench, Compliance Projector; theater detector in shadow mode | An external reviewer reconstructs a month of decisions from exports alone (AF-7 dry run) |
| `P3 · Patient face` | Intake instruments, self-monitoring loop, plain-register renderer, Personal Data Agent, values module (elicitation only) | PF-6 accessibility floor passes; PF-2 register-fidelity audit passes |
| `P4 · Loops & pluralism` | Values mappings ratification (PF-3 live), guideline feedback loop (AF-5), plural-guideline conflict surfacing (SPINE-6), dispute mode | First governed template version change driven by deviation evidence, replayed cleanly against both versions |
| `P5 · Low-resource profile` | Offline-first, device floor, SMS/IVR tier, jurisdiction packs, RPM ingestion; pilot in one low-resource site | XC-3 gate; field pilot with pre-registered evaluation protocol (not co-designer-scored) |

### Risk register

| Risk | Mechanism | Standing control |
|---|---|---|
| Justification theater | Templated rationales game AF-3's compliant-deviation state; the ledger fills with boilerplate | AF-4 theater detector (human-review flags only); deviation UX kept low-friction so honesty stays cheaper than gaming (CF-3) |
| Alert-governor abuse | Suppression rules accrete until the system is silent | CF-5 governance (suppression rules are ratified arguments); suppression budgets; AF system-lens telemetry |
| Ontology freeze | The ICSD-2 failure: knowledge plane fossilizes while medicine moves | EN-2/EN-3 recompilation path; SPINE-5 versioning; AF-5 feedback loop generating change pressure from practice |
| Evaluation incest | Co-designers evaluate their own artefact (the Blake n=2 pattern) at any scale | CF-7; EN-7 firewall; pre-registered pilot protocols (P5) |
| Pluralism collapse | Convenience pressure to auto-resolve guideline conflicts | SPINE-6 conflict materialization; AF anti-requirement against fiat resolution |
| Surveillance capture | Auditor face drifts into clinician performance policing, killing CF trust | AF-1 read-model boundary; AF-8 governed lenses; CF anti-requirement on league tables |
| Equity drift | High-resource features become load-bearing; low-resource profile decays into a demo | XC-3 as release gate; instrument-gap representability (PF-1); LMIC pilot in phasing |
| Regulatory misclassification | Scope creep quietly crosses exemption/classification boundaries | XC-1 honesty posture; XC-2 profile boundary enforced in code; reassessment on every intended-purpose change (TGA guidance) |

### Open research agenda

- **Deviation-composer ergonomics.** The literature contains no usability evidence for structured justified-departure capture at the point of care; CF-3's one-interaction bound is a hypothesis to test, not a settled fact.
- **Auditor acceptance.** AF-3's reframing requires payers and accreditors to accept "documented justified deviation" as a compliant state; this is an institutional negotiation with an evidence component (AF-7 bundles) — study design needed with a real payer.
- **Value-mapping formalization.** PF-3's ratified mappings from life goals to clinical weightings have no validated elicitation instrument; candidate ground exists in shared-decision-making and GAAM qualifier literature.
- **Gap-closing measurement.** The north star needs a metric: pre-registered comparison of decision quality and access outcomes between a high-resource and low-resource deployment of the same fabric (Cockburn's heterogeneity findings define the confounders to control).
- **The GAAM collaboration.** The formalism's author is alive, aligned, and one message away; co-developing the deviation/dispute formalization with Stranieri would anchor the auditor face academically and practically.

## Part 8 — Traceability matrix & sources

### Findings → requirements

| Finding | Source | Requirements it drives |
|---|---|---|
| CDSS failures concentrate at the formal/nebulous boundary; remedies are ontology-widening, circumrational care, cognitive supports, plural systems | Chapman, meta-rationality corpus (uploaded) | SPINE-6/8, PF-3, AF-5, XC-4 |
| Argument trees as diagnostic explanation for multiple user classes; per-criterion micro-engines; workflow-first consultation redesign; shared ontology; swappable classification layer | Blake, Kerr & Gammack 2016 (Inf. Syst.; AJIS); Blake & Kerr 2010/2014; Miah, Blake & Kerr 2020 | SPINE-1/3, CF-1/2, PF-1/5, EN-2 |
| Six design principles; three-interface generic architecture; reasoning-model agnosticism | Miah, Blake & Kerr 2020 (AJIS 24) | SPINE-3/6, EN-1, Part 2 architecture |
| Generic vs actual arguments; warrant-level reasoning for discretionary domains; multi-user explanation; ODR for medical/EHR disputes; patient-centric data agent; repository allocation; coalescing medical systems; ward-round and MDT reasoning | Stranieri corpus: GAAM (DSS 2006), Split-Up (1995–99), medical ODR (2020), PCA (IEEE Access 2018), HIJ 2020, MedInfo 2010, BMC HSR 2018, JDS 2016 | SPINE-1/6, CF-6, PF-4, AF-2/5/6 |
| 37/40 CDSS clinician-only; rigidity, fatigue, surveillance anxiety, integration failure; dual-facing + XAI + UCD as the forward agenda | Bayor et al. 2025 (JMIR 27:e63733) | CF-3/4/5, PF-1..8, AF-8, anti-requirements |
| XAI dominated by unvalidated post-hoc attribution; no fidelity/trust/usability evidence at scale | Abbas, Jeong & Lee 2025 (Healthcare 13:2154) | SPINE-1/2, EN-4, CF-2 |
| Benefit exists (OR 1.69) but transfer fails across contexts; heterogeneity in everything; HCD urged | Cockburn et al. 2024 (eClinicalMedicine 76:102822) | EN-5, XC-3/4, risk register (equity drift) |
| Explanations in decision support: taxonomy and evidence base | Nunes & Jannach 2017 (UMUAI) | SPINE-1, CF-2 |
| Exemption criteria (a)(b)(c); AI-enabled CDSS excluded from exemption; transparency and independent verifiability language | TGA, Understanding CDSS regulation (rev. Oct 2025) | XC-1/2, AF-7, SPINE-7 |
| Layered computable-guideline artifacts and national adaptation model for LMIC deployment | WHO SMART Guidelines (Lancet Digit. Health 2021; smart.who.int starter kit v2) | PF-7, EN-3, XC-3/4 |
| Deployed low-cost RPM in low-resource wards; alarm-signal reduction; POC devices + AI for public health | Anidra program; Balasubramanian & Stranieri RPM corpus (2014–2023) | PF-6, XC-3, EN-9 |
| Mākoha doctrines: Bayesian differential + tiered evidence library; conformal uncertainty; corruption engine; firewalled corpus; "ML proposes and tests; only arithmetic releases"; LLM class posture; regulatory fork | Mākoha program documents (user's corpus) | SPINE-7, EN-1..9, XC-1, Toulmin mapping |
| FDA revised CDS final guidance (6 Jan 2026): singular recommendations permitted where clinically appropriate; criterion-4 independent-review basis strengthened; time-critical relocated under criterion 4; no AI-specific analysis | FDA guidance + Covington analysis (Jan 2026) | XC-2 via Annex 1 (GPP-15, §2.3, §6 edge cases) |

### Sources

- Miah, Blake & Kerr (2020). [Meta-design knowledge for Clinical Decision Support Systems](https://ajis.aaisnet.org/index.php/ajis/article/view/2049). AJIS 24.
- Blake, Kerr & Gammack (2016). [Streamlining patient consultations for sleep disorders with a knowledge-based CDSS](https://www.sciencedirect.com/science/article/abs/pii/S0306437915001593). Information Systems 56. · [AJIS 20 methodology companion](https://ajis.aaisnet.org/index.php/ajis/article/view/1303) · [Blake & Kerr 2014, Decision Analytics](https://link.springer.com/article/10.1186/2193-8636-1-7).
- Stranieri corpus: [GAAM (DSS 2006)](https://doi.org/10.1016/j.dss.2004.07.004) · [Split-Up (AI & Law 1995)](https://doi.org/10.1007/BF00871852) · [Ward rounds (BMC HSR 2018)](https://doi.org/10.1186/s12913-018-3446-6) · [MDT meetings (JDS 2016)](https://doi.org/10.1080/12460125.2016.1187388) · [Medical ODR (2020)](https://doi.org/10.1145/3373017.3373059) · [Patient Centric Agent (IEEE Access 2018)](https://doi.org/10.1109/ACCESS.2018.2846779) · [Repository allocation (HIJ 2020)](https://journals.sagepub.com/doi/10.1177/1460458220957486) · [Coalescing medical systems (MedInfo 2010)](https://doi.org/10.3233/978-1-60750-659-1-159).
- Bayor, Li, Yang & Varnfield (2025). [Designing CDSS — a user-centered lens](https://www.jmir.org/2025/1/e63733). JMIR 27:e63733. (Uploaded PDF.)
- Abbas, Jeong & Lee (2025). [Explainable AI in CDSS: methods, applications, usability](https://doi.org/10.3390/healthcare13172154). Healthcare 13:2154. (Uploaded PDF.)
- Cockburn et al. (2024). [CDSS for maternity care: systematic review and meta-analysis](https://doi.org/10.1016/j.eclinm.2024.102822). eClinicalMedicine 76. (Uploaded PDF.)
- Nunes & Jannach (2017). [A systematic review and taxonomy of explanations in decision support](https://doi.org/10.1007/s11257-017-9195-0). UMUAI.
- TGA. [Understanding clinical decision support system software regulation](https://www.tga.gov.au/resources/guidance/understanding-clinical-decision-support-system-software-regulation) (guidance PDF, rev. 7 Oct 2025 — exemption criteria (a)(b)(c) reviewed verbatim) · [Excluded software: interpretation of exclusion criteria](https://www.tga.gov.au/sites/default/files/2024-07/excluded-software.pdf).
- WHO SMART Guidelines: [Mehl et al., Lancet Digital Health 2021](https://www.thelancet.com/journals/landig/article/PIIS2589-7500(21)00038-8/fulltext) · [smart.who.int](https://smart.who.int/index.html) · [Starter Kit v2 authoring layers](https://smart.who.int/ig-starter-kit/v2.0.0/l2_authoring_overview.html).
- Chapman, meta-rationality materials and the triple-facing CDSS design note (uploaded documents, this series).
- Companion volumes: *Sleep Tools Dossier* and *The Stranieri File* (this series) — full provenance for every lineage claim above.
- FDA. [Clinical Decision Support Software — revised final guidance](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/clinical-decision-support-software) (6 Jan 2026) · [Covington & Burling, 5 Key Takeaways](https://www.cov.com/news-and-insights/insights/2026/01/5-key-takeaways-from-fdas-revised-clinical-decision-support-cds-software-guidance) — anchors for Annex 1 §2.3.
- Addendum J-3 (MAK-J3, v0.9-proposed) — authored in this series; folded verbatim as Annex 1.

*Document footer (source artifact):* The Four Faces Corpus v1.0 · requirement IDs are stable; propose changes as argued deviations — this document follows its own doctrine. Compiled from full-text reads of the uploaded papers, the two companion dossiers' primary-source research, TGA guidance retrieved 29 Aug 2026, and the Mākoha program corpus.

---

## Appendix A — Requirement block format (additive)

Machine-parsable grammar for validator ingestion. Every normative block in this file conforms to:

```text
### <PREFIX>-<n> (<MUST|SHOULD|MAY>)
**Statement:** <normative text; may contain MUST NOT / SHOULD NOT>
**Rationale trace:** <semicolon-separated compressed citations>
```

Validator regex (one requirement header per block):
`^### (SPINE|CF|PF|AF|EN|XC)-\d+ \((MUST|SHOULD|MAY)\)$`

Anti-requirement blocks are the bulleted lists under headings matching `^### .* anti-requirements$`; each bullet has MUST NOT force.

## Appendix B — ID census (additive)

Authoritative enumeration for validator ID-census checks. Count: **46**.

```json
{
  "doc_id": "MAK-FFC",
  "version": "1.0",
  "requirements": {
    "SPINE": ["SPINE-1","SPINE-2","SPINE-3","SPINE-4","SPINE-5","SPINE-6","SPINE-7","SPINE-8","SPINE-9"],
    "CF":    ["CF-1","CF-2","CF-3","CF-4","CF-5","CF-6","CF-7","CF-8"],
    "PF":    ["PF-1","PF-2","PF-3","PF-4","PF-5","PF-6","PF-7","PF-8"],
    "AF":    ["AF-1","AF-2","AF-3","AF-4","AF-5","AF-6","AF-7","AF-8"],
    "EN":    ["EN-1","EN-2","EN-3","EN-4","EN-5","EN-6","EN-7","EN-8","EN-9"],
    "XC":    ["XC-1","XC-2","XC-3","XC-4"]
  },
  "levels": {
    "MUST":   ["SPINE-1","SPINE-2","SPINE-3","SPINE-4","SPINE-5","SPINE-6","SPINE-7","SPINE-8","CF-1","CF-2","CF-3","CF-4","CF-5","CF-7","PF-1","PF-2","PF-3","PF-4","PF-5","PF-6","PF-8","AF-1","AF-2","AF-3","AF-4","AF-5","AF-7","EN-1","EN-2","EN-3","EN-4","EN-5","EN-6","EN-7","EN-8","XC-1","XC-3"],
    "SHOULD": ["SPINE-9","CF-6","PF-7","AF-6","AF-8","EN-9","XC-4"],
    "MAY":    ["CF-8","XC-2"]
  },
  "retired": []
}
```

**Annex census (v1.1, additive).** Annex 1 folds MAK-J3 verbatim; its GPP-prefix requirements are registered here for validator resolution but remain governed by MAK-J3's own census and self-audits (reproduced inside the annex):

```json
{
  "annex": "MAK-J3 v0.9-proposed (Annex 1)",
  "requirements": {"GPP": ["GPP-1","GPP-2","GPP-3","GPP-4","GPP-5","GPP-6","GPP-7","GPP-8","GPP-9","GPP-10","GPP-11","GPP-12","GPP-13","GPP-14","GPP-15","GPP-16"]},
  "levels": {"MUST": ["GPP-1","GPP-2","GPP-3","GPP-4","GPP-5","GPP-6","GPP-7","GPP-8","GPP-9","GPP-10","GPP-11","GPP-12","GPP-14"], "SHOULD": ["GPP-13","GPP-15"], "MAY": ["GPP-16"]}
}
```

## Appendix C — Self-audit checks (additive)

Run these against this file after any edit; all eight must pass before a version increments.

1. **ID uniqueness** — no requirement ID appears in more than one requirement header.
2. **ID census parity** — headers found by the Appendix A regex exactly equal Appendix B's enumeration (46).
3. **Level parity** — the level in each header matches its bucket in Appendix B `levels`.
4. **Trace presence** — every requirement block contains a non-empty `**Rationale trace:**` line.
5. **Normative leakage** — no MUST/SHOULD/MAY (capitalized) appears in informative prose outside requirement blocks, anti-requirement bullets, quoted TGA/source text, or this appendix.
6. **Cross-reference integrity** — every requirement ID mentioned in prose, tables, or traces exists in the census (no dangling IDs).
7. **Table integrity** — all markdown tables have consistent column counts per row.
8. **Stability** — IDs present in the previous version are present or explicitly listed under `retired` in Appendix B; retired IDs never reused.
9. **Annex parity (v1.1)** — GPP-n headers inside Annex 1 exactly match the annex census in Appendix B (16), and the annex text is byte-identical to MAK-J3 v0.9-proposed except for the annex banner; the main census (check 2) continues to exclude GPP-prefix IDs.



---

# Annex 1 — Addendum J-3: Guideline-Prompt Profile (GPP), folded verbatim

> **Annex banner (v1.1, additive).** The following is the complete text of **MAK-J3 v0.9-proposed** (authored 2026-08-29), folded into this corpus unmodified per the additive-integration instruction. If a standalone MAK-J3 file is maintained in the document ecosystem, that file is canonical and this annex mirrors it; divergence is a validator error. The addendum's own frontmatter is preserved below as a fenced block.

```yaml
doc_id: MAK-J3
title: "Addendum J-3 — Guideline-Prompt Profile (GPP): the exempt-tier reserve"
version: "0.9-proposed"
date: "2026-08-29"
series: "Mākoha regulatory fork — Addendum J series"
status: proposed-normative-draft
naming_note: "J-3 designation is provisional pending ratification against the existing Addendum J-1 (deterministic runtime) / J-2 (ML runtime) conventions — an open naming decision consistent with the programme's IMPL-rename precedent."
normative_language: RFC-2119 (MUST / SHOULD / MAY)
req_prefix: GPP
req_count: 16
realizes: "MAK-FFC XC-2 (MAY): 'Ship a scoped guideline-prompt profile … provided the profile boundary is enforced in code, not policy.'"
subordinate_to:
  - "MAK-FFC XC-1 (classification honesty) — J-3 never substitutes for the classified track; it is the lawful floor beside it"
  - "MAK-FFC SPINE-1..9 — the shared spine applies in full inside the profile"
depends_on:
  - "MAK-FFC v1.0 (The Four Faces Corpus)"
  - "MAK-ELSM v1.0 (Execution Layer Sourcing Map)"
regulatory_anchors:
  - "TGA, Understanding clinical decision support system software regulation (guidance, rev. 7 Oct 2025) — exemption criteria (a)(b)(c), Schedule 4 Part 2, Therapeutic Goods (Medical Devices) Regulations 2002"
  - "TGA, Excluded software: interpretation of exclusion criteria (Jul 2024)"
  - "FDA, Clinical Decision Support Software — revised final guidance (6 Jan 2026), FD&C Act §520(o)(1)(E) Non-Device CDS criteria"
  - "EU MDR 2017/745, Rule 11 (no equivalent carve-out)"
```

<!-- LLM USAGE CONTRACT (additive)
1. GPP-n blocks are NORMATIVE for the J-3 build target only; they add to, and never
   relax, MAK-FFC requirements. Where a GPP-n narrows a MAK-FFC requirement's scope
   inside the profile, the narrowing is stated explicitly; absence of narrowing means
   MAK-FFC applies unmodified.
2. The Capability Matrix (§3) is normative: ON means compiled and enabled; OFF means
   STRUCTURALLY ABSENT from the build artifact (GPP-8), not disabled by flag.
3. Regulatory quotations are paraphrase-faithful to the anchored guidance versions in
   the frontmatter; re-verify anchors before any submission or supply decision.
4. Legal-review flags (⚑) mark boundary questions this document deliberately does not
   decide; an LLM must never resolve a ⚑ by generation.
END LLM USAGE CONTRACT -->

# Addendum J-3 — Guideline-Prompt Profile (GPP)

**The exempt-tier reserve: a code-enforced configuration of the shared Mākoha codebase that supplies only what the TGA's CDSS exemption permits — guideline prompts, alerts, reminders, and pathway recommendations to health professionals, on a transparent, independently verifiable basis — while every classification-attracting capability is structurally absent from the build.**

## 1 — Purpose and position in the J-fork

The J-fork to date holds two branches: **J-1** (deterministic runtime, classified SaMD track) and **J-2** (ML runtime, classified, higher classification posture). Both plan for ARTG inclusion per XC-1, because Mākoha's diagnostic engine is diagnosis-contributing and the TGA states plainly that an AI-enabled CDSS will not meet the exemption criteria.

**J-3 adds the lawful floor beside them.** It is not a lesser Mākoha; it is the same spine — justification fabric, guideline compiler, versioning, ledger, deviation machinery — shipped as a distinct build artifact whose inference plane contains nothing but ratified published guidelines evaluated deterministically. Three strategic functions:

1. **Market entry** where classification timelines or economics block deployment — including low-resource jurisdictions (XC-3) where guideline-prompt support is itself the north-star payload.
2. **Evidence accumulation**: every GPP deployment feeds the fabric with real usage, deviation, and guideline-gap evidence that seeds J-1/J-2 validation (GPP-13).
3. **Regulatory hedge**: if classified-track timelines slip, the programme still ships something lawful, useful, and spine-true.

J-3 is subordinate to XC-1's honesty posture. It is never marketed, configured, or quietly extended to do classified work under an exempt label. The boundary is enforced in code (GPP-8..11), and crossing it is a new device, not an update (GPP-14).

## 2 — Regulatory basis, mapped to design

### 2.1 The TGA two-off-ramp structure

The TGA guidance distinguishes **excluded** software (not a regulated medical device at all) from **exempt** CDSS (a medical device, exempt from ARTG inclusion, but still subject to TGA oversight). J-3 targets the **exempt** tier: it accepts the residual obligations (§5) in exchange for supplying without ARTG inclusion. The guidance's own scope sentence for the exempt tier is J-3's product definition:

> Exempt CDSS "may include software that collects, performs simple analysis, and displays data from EMRs, EHRs or CISs" and "may provide prompts, alerts, reminders, and recommendations to help health professionals apply evidence-based clinical guidelines or hospital procedures."

And its own warning is J-3's boundary: CDSS performing "more advanced analysis and functions such as specifying a diagnosis or treatment for a patient" is unlikely to qualify.

### 2.2 The three exemption criteria as design constraints

| Criterion (TGA, Sch. 4 Pt 2) | Design consequence in J-3 |
|---|---|
| **(a)** Sole purpose: providing or supporting a *recommendation to a health professional* about preventing, diagnosing, curing or alleviating disease. A recommendation means advice to take steps, gather inputs, or follow a course of action, or general information — *not* making a diagnosis, providing new diagnostic information, or specifying/customising a treatment. | Recommendations render to authenticated health professionals only (GPP-4). Claim-type whitelist excludes diagnosis, differential, risk-score, treatment-customization, screening, monitoring — structurally, not by flag (GPP-5). Patient face reduces to intake, consent, logistics (GPP-4). |
| **(b)** Not intended to directly process or analyse a medical image or a signal from another medical device (incl. IVD). Displaying EMR-retrieved values can be acceptable; interpreting them, or displaying for patient monitoring, is not. | Device-originated data is refused at the API boundary; no imaging, waveform, or sensor endpoints exist in the build; EMR-retrieved values display without interpretation or trending-for-monitoring (GPP-6). Anidra-class RPM ingestion is a J-1/J-2 capability only. |
| **(c)** Not intended to replace clinical judgement: must be transparent (no proprietary AI generating recommendations), allow the professional to easily understand and verify the recommendation's accuracy, and clearly reference the logic, guidelines, process or evidence — information the professional cannot independently verify fails the criterion. | The justification fabric satisfies this by construction: warrant → published guideline clause with citation and version; backing → evidence tier and source. J-3 adds the release gate: a recommendation whose basis is not reproducible from cited public sources MUST NOT release (GPP-7). No learned parameters in the inference path — the TGA's note that AI-enabled CDSS cannot qualify is honoured by structural absence (GPP-7/8). |

### 2.3 Jurisdiction map (GPP-15)

| Jurisdiction | Mechanism | J-3 posture |
|---|---|---|
| **Australia (TGA)** | CDSS exemption, criteria (a)(b)(c); notification-based supply | Primary target; this addendum's design basis |
| **USA (FDA)** | Non-Device CDS, §520(o)(1)(E), four criteria per revised final guidance (6 Jan 2026): revision permits *singular* recommendations where clinically appropriate; strengthens criterion 4 (basis from "well-understood and accepted sources" — clinical guidelines, peer-reviewed literature — presented for independent review); relocates time-critical decision-making under criterion 4; offers no AI-specific analysis | J-3's transparent guideline-referenced basis is precisely criterion 4's demand; avoid time-critical deployment contexts (§4 edge cases); re-map before any US supply |
| **EU (MDR)** | Rule 11 — software providing information used for diagnostic/therapeutic decisions is class IIa minimum; **no exempt-tier equivalent** | J-3 does not confer an EU pathway; EU supply follows the classified track |
| **Low-resource jurisdictions** | National regimes vary; WHO SMART Guidelines alignment (PF-7/XC-4) eases national adaptation and approval | Assess individually; the exemption logic does not transfer automatically |

## 3 — Capability matrix (normative)

ON = compiled, enabled, conformance-tested. OFF = structurally absent from the build artifact and its dependency graph (GPP-8). ⚑ = legal-review flag, undecided here.

| Capability | J-3 GPP | Notes |
|---|---|---|
| Justification fabric, ledger, version pinning (SPINE-1..5) | ON | Full spine; arguments carry `profile: GPP` stamps (GPP-11) |
| Guideline Compiler → GenericArgument (EN-3) | ON | Warrant type restricted to `guideline-rule` (GPP-9) |
| Deterministic Evaluator (SPINE-7) | ON | The only release path; refuses probabilistic qualifiers (GPP-9) |
| Clinician face: guideline prompts, alerts, reminders, pathway recommendations, information summaries | ON | Claim-type whitelist (GPP-5) |
| Deviation Composer + deviation ledger (SPINE-8, CF-3) | ON | Recording departure from a prompt is documentation, not diagnosis (GPP-16) |
| Auditor face read model, compliance projector, exports (AF-1..3, AF-7) | ON | Internal QA and conformity evidence; not a clinical function |
| Alert Governor (CF-5) | ON | Suppression rules remain ratified GenericArguments |
| Patient face: intake instruments, consent, logistics (PF-1, PF-4 consent subset) | ON | No patient-directed clinical recommendations (GPP-4) |
| Bayesian Differential Service | OFF | Diagnosis-contributing; defeats criteria (a) and (c) |
| Conformal Wrapper | OFF | Nothing probabilistic to qualify; qualifier type = `applicability` only (GPP-9) |
| LLM runtime (all Class 4+ uses) | OFF | TGA: AI-enabled CDSS will not meet the exemption; authoring-time LLM use (EN-6 Classes 1–3) remains permitted *outside* the supplied artifact, with human ratification |
| RPM / device-signal / imaging ingestion (Anidra-class, ECG, SpO₂ streams) | OFF | Criterion (b); refused at API boundary (GPP-6) |
| Diagnosis, differential, risk-score, screening, triage-urgency scoring claim types | OFF | Unrepresentable types in GPP build (GPP-5); triage scoring derived from patient data is new diagnostic information |
| Treatment customization (patient-specific dose calculation, regimen tailoring) | OFF | Criterion (a) "specifying or customising a particular treatment" |
| Verbatim display of published guideline dose tables (uninterpreted) | ⚑ | Arguably guideline content, not customization — obtain legal reading before enabling |
| Patient-monitoring displays / trending of EMR vitals | OFF | Criterion (b) explanation disqualifies display-for-monitoring |
| Values & Priorities engine weighting (PF-3 mappings) | OFF | Weighting recommendations by patient values is customization; elicitation-and-display MAY remain ⚑ |

## 4 — Requirements

### GPP-1 (MUST)
**Statement:** J-3 is a distinct supplied artifact of the shared codebase with its own intended-purpose statement, limited to: providing or supporting recommendations to health professionals to apply ratified, published, evidence-based clinical guidelines and facility procedures — prompts, alerts, reminders, pathway recommendations, and information summaries. The intended-purpose statement MUST NOT claim or imply diagnosis, screening, monitoring, or treatment specification, and marketing/advertising materials are conformance artifacts bound to it.
**Rationale trace:** TGA criterion (a) + recommendation definition; XC-1/XC-2; TGA advertising obligations for exempt devices.

### GPP-2 (MUST)
**Statement:** Exempt is not unregulated. The J-3 obligations register is maintained and evidenced from the fabric: (i) TGA notification via the Clinical Decision Support Software Exemption Notification Form within 30 working days of supply; (ii) conformity with the Essential Principles for safety and performance, evidenced by AF-7-style bundles; (iii) adverse-event reporting; (iv) therapeutic-goods advertising compliance; (v) recall/hazard-alert cooperation. Each obligation has a named owner in the responsibility register.
**Rationale trace:** TGA guidance, "Regulatory requirements that apply to exempt CDSS" (verbatim-reviewed); MAK-FFC AF-7.

### GPP-3 (MUST)
**Statement:** Any change to J-3's function or intended purpose re-runs the full exclusion/exemption assessment before release. The assessment record (criteria walk-through, verdict, assessor) enters the ledger; the release pipeline blocks on its presence.
**Rationale trace:** TGA guidance ("if your product is updated or its intended purpose changes, you must reassess"); XC-1 risk register (regulatory misclassification).

### GPP-4 (MUST)
**Statement:** Criterion (a) enforcement — recommendations render only to authenticated health professionals (role-verified per the Regulations' health-professional definition). The patient face in J-3 is limited to intake instruments, consent management, access ledger, and logistics; it MUST NOT render clinical recommendations, diagnoses, risk information, or monitoring feedback to patients.
**Rationale trace:** TGA criterion (a) sole-purpose language; MAK-FFC PF-8 narrowed for the profile.

### GPP-5 (MUST)
**Statement:** Criterion (a) claim-type enforcement — the GPP build's released claim types are exactly: `guideline-prompt`, `pathway-recommendation`, `reminder`, `information-summary`, `gather-more-information`. The types `diagnosis`, `differential`, `risk-score`, `screening-result`, `triage-score`, `treatment-customization`, and `monitoring-alert` are structurally unrepresentable in the J-3 artifact (types not compiled in), not merely disabled by configuration.
**Rationale trace:** TGA recommendation definition (excludes diagnosis, new diagnostic information, treatment specification); XC-2 "enforced in code, not policy."

### GPP-6 (MUST)
**Statement:** Criterion (b) enforcement — the data plane's J-3 ingestion allowlist admits QuestionnaireResponse, practitioner-entered data, and EMR/EHR-retrieved records. FHIR resources bearing device origin (populated `Observation.device`, device-sourced Provenance, or waveform/imaging content types) are rejected at the API boundary with a ledgered refusal. No imaging, waveform, sensor-stream, or IVD-output endpoint is linked into the build. EMR-retrieved values may be displayed but MUST NOT be interpreted, trended for monitoring, or used as grounds for inferences over device-signal content.
**Rationale trace:** TGA criterion (b) + its "directly analyse or process," "signal," and display-for-monitoring explanations.

### GPP-7 (MUST)
**Statement:** Criterion (c) enforcement — every J-3 recommendation's argument renders with: warrant → the published guideline clause (publisher, citation, version, effective date); backing → evidence tier and public source link; and deterministic evaluation trace. The release gate enforces independent verifiability: a recommendation whose complete basis is not reproducible by a health professional from cited, publicly accessible sources MUST NOT release. No learned parameters exist anywhere in the J-3 inference path.
**Rationale trace:** TGA criterion (c) verbatim requirements (transparent; easily understand and verify; clearly references logic/guidelines/evidence; independently verifiable); TGA note that AI-enabled CDSS will not meet the criteria; SPINE-7.

### GPP-8 (MUST)
**Statement:** The profile boundary is enforced at build time by exclusion: the modules for Bayesian inference, conformal wrapping, LLM runtime, device-signal ingestion, and the prohibited claim types are absent from the compiled J-3 artifact and its dependency graph. Each release generates an SBOM (CycloneDX or equivalent) that CI diffs against the prohibited-namespace manifest; a match fails the build. Feature flags, environment variables, or configuration MUST NOT be capable of enabling an excluded capability in a J-3 artifact.
**Rationale trace:** XC-2 ("enforced in code, not policy"); supply-chain evidence for Essential Principles conformity.

### GPP-9 (MUST)
**Statement:** Schema-level enforcement — J-3 GenericArgument templates carry `profile: GPP`; the compiler and validator reject, for this profile, any warrant type other than `guideline-rule` and any qualifier type other than `applicability` (a deterministic statement of which guideline population/conditions the prompt applies to). The Deterministic Evaluator refuses drafts bearing `posterior` or `conformal` qualifiers, and the refusal is ledgered.
**Rationale trace:** SPINE-2 adapted to a non-probabilistic profile; GPP-5/7 coherence.

### GPP-10 (MUST)
**Statement:** A conformance suite (GPP-CONF) runs as a release gate: negative tests attempt each prohibited capability (invoke Bayesian inference, ingest a device-originated Observation, construct a diagnosis-type claim, render a patient-facing recommendation, enable an excluded module by configuration) and pass only on structural absence or refusal-with-ledger-record. Static analysis forbids imports from excluded namespaces. The suite's results are conformity-file artifacts.
**Rationale trace:** GPP-8/9 verifiability; MAK-FFC evaluation-firewall discipline (EN-7) applied to the boundary itself.

### GPP-11 (MUST)
**Statement:** Runtime attestation and defense in depth — the J-3 artifact cryptographically attests its profile identity at startup; every fabric entry it writes is stamped `profile: GPP`; and a spine-level boundary monitor alarms if any claim type, qualifier type, or ingestion class outside the J-3 whitelist ever appears in a J-3 deployment's ledger. A boundary alarm is triaged as a potential adverse event and a mandatory GPP-3 reassessment trigger.
**Rationale trace:** defense in depth over GPP-8..10; TGA adverse-event obligation; SPINE-4 evidentiary chain.

### GPP-12 (MUST)
**Statement:** Single-codebase discipline — J-3 shares the justification fabric, ledger, guideline compiler, version pinning, deviation machinery, and register renderers with J-1/J-2. J-3 diverges by exclusion only: no J-3-only clinical logic, schema branches, or guideline content forks. A guideline compiled for J-3 is byte-identical to the same guideline's GenericArguments in J-1/J-2 at the same version.
**Rationale trace:** fork-drift risk; SPINE-5 replay integrity across tiers; AF-5 feedback loop must aggregate across tiers.

### GPP-13 (SHOULD)
**Statement:** Evidence-vehicle doctrine — J-3 deployments accumulate fabric evidence (prompt usage, deviation patterns, guideline-gap findings, workflow telemetry) that, under ethics approval and appropriate consent, feeds J-1/J-2 validation submissions and the AF-5 guideline feedback loop. Deployment agreements SHOULD secure this secondary-use basis at signing.
**Rationale trace:** §1 strategic function 2; CF-7/EN-7 evaluation needs; XC-3 field-pilot phasing.

### GPP-14 (MUST)
**Statement:** Tier-promotion protocol — enabling any excluded capability for any deployment constitutes supply of a different device under the classified track (J-1/J-2): new artifact, new intended-purpose statement, new conformity record, new (or amended) regulatory footing. In-place upgrades of a J-3 installation across the profile boundary are prohibited; migration is an explicit re-supply with the receiving governance's sign-off.
**Rationale trace:** GPP-3; XC-1 honesty posture; TGA reassessment doctrine.

### GPP-15 (SHOULD)
**Statement:** The jurisdiction map (§2.3) is a maintained artifact reviewed at least annually and before any new-market supply: TGA criteria (a)(b)(c) for Australia; FDA §520(o)(1)(E) four criteria per the revised final guidance (6 Jan 2026) for the USA, noting the singular-recommendation allowance, the strengthened criterion-4 independent-review basis, and the time-critical relocation; EU MDR Rule 11's absence of a carve-out; and per-country assessment for low-resource jurisdictions with WHO SMART alignment as the adaptation vehicle.
**Rationale trace:** verified TGA guidance (Oct 2025 rev.); Covington analysis of FDA revised guidance (Jan 2026); MDR Rule 11; XC-3/XC-4.

### GPP-16 (MAY)
**Statement:** The Deviation Composer and deviation ledger remain enabled in J-3 — recording that a clinician departed from a guideline prompt, with reasons, is clinical documentation, not diagnosis or treatment specification — and the auditor read model over J-3 ledgers operates as internal quality assurance. ⚑ If a legal reading finds deviation-pattern analytics drift toward "new diagnostic information" in a jurisdiction, the analytics (not the recording) are excluded there.
**Rationale trace:** SPINE-8 preserved at the exempt tier; GPP-13 evidence value; conservative flag.

## 5 — Obligations register (exempt-tier residuals)

| Obligation | Trigger | Evidence source | Owner field |
|---|---|---|---|
| TGA exemption notification (CDSS Exemption Notification Form) | Within 30 working days of first supply | Ledger supply record + submitted form copy | `regulatory` |
| Essential Principles conformity | Continuous; per release | GPP-CONF results, SBOM, AF-7-style bundles, risk file | `quality` |
| Adverse event reporting | On event, incl. GPP-11 boundary alarms triaged positive | Ledger incident chain | `safety` |
| Advertising compliance | All external claims | Intended-purpose statement (GPP-1) as the claims boundary | `regulatory` |
| Recall / hazard-alert cooperation | On TGA action | Deployment registry + version pinning (SPINE-5) | `operations` |
| Reassessment on change | Any functional or intended-purpose change | GPP-3 assessment records | `regulatory` |

## 6 — Boundary edge cases (decided and flagged)

- **Triage urgency scoring — OFF.** Deriving an urgency tier from patient data is new diagnostic information / risk stratification. J-3 may present the *guideline's own* triage pathway text as a prompt; it may not compute a patient's tier.
- **Time-critical contexts — avoid.** The FDA's revised guidance relocates time-critical decision support outside the non-device envelope (no time for independent review); TGA criterion (c) points the same direction. J-3 deployment contexts SHOULD exclude emergency/time-critical workflows; this is a deployment-scoping control, recorded per site.
- **Verbatim guideline dose tables — ⚑ legal review.** Displaying a published table uninterpreted is arguably guideline content; any patient-specific computation over it is customization and OFF.
- **Values elicitation display — ⚑ legal review.** Eliciting and displaying patient priorities to the clinician may be permissible information; using them to reweight recommendations is customization and OFF (PF-3 machinery is J-1/J-2).
- **EMR value display — narrow.** Display without interpretation is within the exempt scope; the moment a displayed value participates in an inference beyond guideline-applicability matching, GPP-6/9 must refuse it.

## 7 — Delta summary against MAK-FFC

| MAK-FFC requirement | J-3 disposition |
|---|---|
| SPINE-1..5, SPINE-7..9 | Apply unmodified |
| SPINE-6 (plural guidelines) | Applies; conflicts between co-resident guidelines surface as prompts-with-conflict, never resolved by the system |
| CF-1..5, CF-7, CF-8 | Apply; CF-2's qualifier renders as `applicability`, not posterior |
| CF-6 (MDT multi-author) | Applies (documentation function) |
| PF-1, PF-4 (consent subset), PF-6 | Apply |
| PF-2, PF-3, PF-5 clinical-feedback aspects, PF-8 | Suspended in-profile (no patient-facing clinical content); PF-3 machinery excluded (GPP capability matrix) |
| AF-1..3, AF-7, AF-8 | Apply as internal QA + conformity evidence |
| AF-4 theater detector | SHOULD run in shadow mode only ⚑ (see GPP-16 flag) |
| EN-1..3, EN-7, EN-8 | Apply (evaluator + compiler are the whole engine plane) |
| EN-4, EN-5 runtime, EN-6 runtime, EN-9 | Excluded with their modules; EN-5 adversarial testing still runs in CI against the J-3 artifact (harness, not runtime) |
| XC-1, XC-3, XC-4 | Apply; XC-2 is realized by this addendum |

## Appendix A — ID census (additive)

```json
{
  "doc_id": "MAK-J3",
  "version": "0.9-proposed",
  "requirements": {
    "GPP": ["GPP-1","GPP-2","GPP-3","GPP-4","GPP-5","GPP-6","GPP-7","GPP-8","GPP-9","GPP-10","GPP-11","GPP-12","GPP-13","GPP-14","GPP-15","GPP-16"]
  },
  "levels": {
    "MUST":   ["GPP-1","GPP-2","GPP-3","GPP-4","GPP-5","GPP-6","GPP-7","GPP-8","GPP-9","GPP-10","GPP-11","GPP-12","GPP-14"],
    "SHOULD": ["GPP-13","GPP-15"],
    "MAY":    ["GPP-16"]
  },
  "legal_review_flags": ["dose-table display (§3, §6)", "values elicitation display (§3, §6)", "deviation-pattern analytics in-profile (GPP-16)"],
  "retired": []
}
```

## Appendix B — Self-audit checks (additive)

1. **ID census parity** — GPP-n headers exactly match Appendix A (16).
2. **Level parity** — header levels match Appendix A buckets.
3. **Matrix/requirement coherence** — every OFF row in §3 is enforced by at least one MUST (GPP-5/6/7/8/9), and every ⚑ in §3 appears in §6 and Appendix A flags.
4. **No relaxation** — no GPP-n weakens a MAK-FFC MUST; deltas in §7 only narrow scope or suspend patient-facing clinical functions.
5. **Anchor currency** — frontmatter regulatory anchors carry version dates; any submission re-verifies them (LLM contract rule 3).
6. **Boundary language** — "disabled," "flagged off," or "configurable" never appears where "structurally absent" is required (GPP-8).
7. **Trace presence** — every GPP-n has a non-empty rationale trace.
8. **Cross-doc resolution** — every MAK-FFC ID cited resolves in MAK-FFC v1.0 Appendix B.
