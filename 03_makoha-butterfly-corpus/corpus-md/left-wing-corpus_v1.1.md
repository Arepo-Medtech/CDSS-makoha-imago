---
doc_id: MAK-LWC
title: "The Left Wing Corpus"
version: "1.1"
date: "2026-09-01"
series: "Mākoha research series — volume 7 · sibling to MAK-FFC"
status: normative-draft
normative_language: RFC-2119 (MUST / SHOULD / MAY)
req_prefixes: [FS, FC, FP, FA, FE, FX]
req_count: 43
subordinate_to: "MAK-FFC v1.1 — no requirement here relaxes a corpus MUST; narrowings are explicit"
absorbs: "MAK-DOT FZ-1..6 (mapping in Part 8); on ratification of this corpus the FZ set is superseded"
changelog:
  - "v1.1 (2026-09-01): additive Part 9 — execution sourcing annex (verified repos mapped to requirement IDs, confirmed build list, 2025+ research plane, sourcing landmines). No v1.0 content altered."
  - "v1.0 (2026-09-01): initial release — 43 requirements across FS/FC/FP/FA/FE/FX."
companions:
  - "MAK-FFC v1.1 (host architecture; all SPINE/CF/PF/AF/EN/XC/GPP IDs resolve there)"
  - "MAK-DOT v1.0 (research base; absorbed proposals)"
  - "MAK-MIF v1.0 (the eight beats this corpus operationalizes)"
  - "MAK-ELSM v1.1, MAK-J3 (sourcing vocabulary; exempt-tier boundary)"
artifact_url: "https://claude.ai/code/artifact/57179980-fb67-45d1-a88d-78638d8bbd09"
change_policy: "Requirement IDs are stable; retired IDs never reused. Propose changes as argued deviations."
---

<!-- LLM USAGE CONTRACT (additive; not part of the source document)
1. Requirement blocks (### FS-n / FC-n / FP-n / FA-n / FE-n / FX-n) are NORMATIVE;
   all other prose is INFORMATIVE. Part 9 is an informative sourcing annex.
2. Note the family-name distinction: FC/FP/FA here are FUZZY-scoped face families and
   never collide with or substitute for MAK-FFC's CF/PF/AF. Cite with the doc prefix
   when ambiguity is possible ("MAK-LWC FC-1").
3. The four axioms (A1–A4, Part 1) bind generation: never render μ, activation
   strength, or a defuzzified value as probability/confidence (A1); never emit
   membership definitions outside the governed knowledge-plane path (A2); never
   invent vocabulary outside a ratified codebook (A3/FS-5).
4. MUST violations in generated designs/code/documents require an explicit
   DEVIATION notice naming the ID.
5. Appendix A's ID census is authoritative for validator checks; Appendix B's
   self-audit checks gate any edit of this file.
6. Part 9 statuses are dated observations (verified 2026-08-30 – 2026-09-01);
   re-verify before dependency decisions.
END LLM USAGE CONTRACT -->

# The Left Wing Corpus

A translatable research primer and execution manual for the fuzzy-logic layer of the triple-facing CDSS — the linguistic spine, its expression in the Clinician, Patient, and Auditor faces, and its engine-plane machinery — with every commitment traced to evidence and every boundary guarded against semantic corruption.

**Document metadata:** Technical corpus · v1.1 · 1 Sep 2026 · seventh volume in the Mākoha research series · sibling to MAK-FFC · STATUS: normative draft · REQ IDS: FS · FC · FP · FA · FE · FX · SUBORDINATE TO: MAK-FFC v1.1 · ABSORBS: MAK-DOT FZ-1..6.

## Contents

1. [Part 0 — How to use this document](#part-0--how-to-use-this-document)
2. [Part 1 — Foundation: the semantics of degree, and four axioms](#part-1--foundation-the-semantics-of-degree-and-four-axioms)
3. [Part 2 — The Fuzzy Spine: the linguistic layer (FS)](#part-2--the-fuzzy-spine-the-linguistic-layer)
4. [Part 3 — The Clinician Face (FC)](#part-3--the-clinician-face)
5. [Part 4 — The Patient Face (FP)](#part-4--the-patient-face)
6. [Part 5 — The Auditor Face (FA)](#part-5--the-auditor-face)
7. [Part 6 — The Engines (FE)](#part-6--the-engines)
8. [Part 7 — Cross-cutting execution (FX)](#part-7--cross-cutting-execution)
9. [Part 8 — Traceability, FZ absorption & sources](#part-8--traceability-fz-absorption--sources)
10. [Part 9 — Execution sourcing annex (v1.1, additive)](#part-9--execution-sourcing-annex-v11-additive)
11. [Appendix A — ID census](#appendix-a--id-census-additive) · [Appendix B — Self-audit checks](#appendix-b--self-audit-checks-additive)

## Thesis

> Clinical language is graded; clinical software pretends it is not, and the pretence is paid for at the boundaries — the 139-vs-141 cliff, the "elderly" that means five different things in five clinics, the patient's "pretty bad, I think" flattened into a 7. Sixty years of fuzzy-logic research, from Zadeh's fuzzy sets through CADIAG-2, Computing with Words, Z-numbers, and 2026's fuzzy-neuro-symbolic frameworks, supplies exactly one missing layer for the Four Faces architecture: **a governed linguistic spine** — ratified, versioned meanings for the vague words the system runs on, with a mathematics for encoding them in, reasoning over them, and decoding them back out in each face's register. This corpus specifies that layer. Its cardinal law never bends: **fuzzy machinery grades meaning, never belief** — μ lives on grounds and warrant-applicability, probability and conformal coverage own the Qualifier, and nothing fuzzy ever releases to a face except through the deterministic evaluator as part of an argument.

## Part 0 — How to use this document

This corpus is the left wing's equivalent of MAK-FFC: a primer (why each commitment exists, with citations) and an execution manual (requirements you can build, test, and audit against), formatted for lifting verbatim into specifications, validator rules, and conformity files.

- **Normative language.** MUST / SHOULD / MAY per RFC 2119, with MAK-FFC's conventions: MUST is conformance-defining; SHOULD departures require recorded justification; MAY is design freedom.
- **Requirement IDs.** `FS-n` the Fuzzy Spine (linguistic layer); `FC-n` Clinician Face; `FP-n` Patient Face; `FA-n` Auditor Face; `FE-n` Engines; `FX-n` cross-cutting. IDs are stable; retired IDs never reused. (Note: FC/FP/FA here are fuzzy-scoped families and do not collide with MAK-FFC's CF/PF/AF.)
- **Subordination.** Every requirement here operates *inside* MAK-FFC v1.1. Where this corpus narrows an FFC requirement, the narrowing is explicit; nothing here relaxes an FFC MUST. MAK-DOT's proposed FZ-1..6 are absorbed and expanded here (Part 8 maps them); on ratification of this corpus, the FZ set is superseded.
- **Scope.** Architecture and component behaviour for the fuzzy layer. The Mākoha stack (Bayesian differential, conformal wrapper, corruption engine, justification fabric) is the reference implementation context, not a constraint.

## Part 1 — Foundation: the semantics of degree, and four axioms

Three quantities travel together through a clinical decision and must never exchange clothes. A **membership degree** μ_elevated(142/92) = 0.72 is a fact about *meaning* — how well a reading satisfies a graded category, true even under perfect measurement. A **probability** is a fact about *belief* under incomplete information; a **conformal set** is a guarantee about how often claim-sets trap truth. And a **Z-number's reliability component** is a fact about the *source* — how sure the speaker is of what they reported. The literature that powers this corpus is precisely the literature that learned to keep these apart: Zadeh's move from manipulating measurements to manipulating perceptions; Mendel's Perceptual Computer, which demands that every computed output decode back into a word a human recognizes; Zadeh's Z = (restriction, reliability) for partially reliable information; and the 2024–26 work that grades the credibility of a membership function itself and couples LLM narrative extraction to auditable fuzzy-symbolic verification.

Four axioms govern everything that follows:

- **A1 — Fuzzy grades meaning, never belief.** μ annotates grounds and warrant-applicability; the Qualifier belongs to probability and coverage. No exceptions, in any face, ever.
- **A2 — Membership is governed meaning.** A membership function is a community's ratified definition of a word — an ontology object with a version, an author, and a ratification trail, never a tuning parameter.
- **A3 — The linguistic round trip is a contract.** What enters as words must be encodable without distortion, and what leaves must decode into words from a ratified vocabulary — no orphan outputs a person cannot recognize.
- **A4 — Deterministic transparency is the licence.** Fuzzy inference carries zero learned parameters; every step is a readable rule; the whole knowledge base serializes to an open standard. This is why the left wing may sit inside the J-1 deterministic runtime at all.

> The left wing's one-sentence doctrine: give every vague clinical word one governed meaning per lineage, measure how well each case fits that meaning, and say so — in each face's own tongue — without ever confusing fit with belief.

## Part 2 — The Fuzzy Spine: the linguistic layer

The spine is one new plane inside the MAK-FFC architecture: a **linguistic layer** living in the knowledge plane and expressed at every boundary. Its unit is the *LinguisticVariable* — a named clinical vague term ("elderly", "elevated BP", "poor sleep efficiency", "severe pain") with its term set, membership functions, hedge algebra, and provenance. Its per-face expression is the *codebook* — the ratified vocabulary each register may speak, after Mendel: an encoder maps inputs to fuzzy models, engines reason over them, and a decoder maps results back to codebook words.

### The fuzzy spine (layered)

```text
┌───────────────────┬───────────────────┬──────────────────────────┐
│ Clinical codebook │  Plain codebook   │  Compliance codebook     │
│ criterion-grade   │  everyday words   │  exact μ, curves,        │
│ terms + μ chips   │  + scales         │  rule firings            │
└───────────────────┴───────────────────┴──────────────────────────┘
        ↓ ↑  encoder / decoder services (the linguistic round trip, A3)
┌──────────────────────────────────────────────────────────────────┐
│           LINGUISTIC LAYER (knowledge plane)                     │
│  LinguisticVariables · membership functions · hedge algebra ·    │
│  Z-ground schema · IEEE 1855 FML serialization ·                 │
│  versioned, ratified, jurisdiction lineages                      │
└──────────────────────────────────────────────────────────────────┘
        ↓ ↑
┌───────────────────┬───────────────────┬──────────────────────────┐
│ Grounds annotation│ Warrant           │ Boundary map             │
│ data plane:       │ applicability     │ corruption engine:       │
│ μ-vectors pinned  │ engine plane:     │ membership supports as   │
│ to MF versions    │ graded            │ sweep targets            │
│                   │ preconditions in  │                          │
│                   │ GenericArguments  │                          │
└───────────────────┴───────────────────┴──────────────────────────┘
```

### Spine requirements

### FS-1 (MUST)
**Statement:** Every clinical vague term the system computes over is a *LinguisticVariable* artifact in the knowledge plane: name, universe of discourse, term set, membership functions, permitted hedges, authorship, evidence backing, ratification record, and version — serialized in IEEE 1855-2016 FML. Code-embedded or ad-hoc membership definitions are prohibited; the Guideline Compiler path (MAK-FFC EN-3) is the only entry.
**Rationale trace:** A2; IEEE 1855/JFML; MAK-DOT FZ-2; ICSD-freeze lesson.

### FS-2 (MUST)
**Statement:** Gradedness annotations attach to Grounds as μ-vectors: for each applicable LinguisticVariable, the term memberships computed at capture or preparation time, pinned to the MF version used. Annotations are additive metadata — the crisp source value is always preserved beside them, and re-annotation under a new MF version never overwrites a prior annotation.
**Rationale trace:** SPINE-5 pinning; replayability; MAK-DOT FZ-1 (placement half).

### FS-3 (MUST)
**Statement:** Type separation is enforced end to end (A1): μ and rule-activation strengths never populate, blend into, or render as the argument Qualifier; posteriors and conformal sets never masquerade as degrees of meaning; Z-reliability components map to grounds-level source-confidence, not to claim belief. Schema types are distinct and non-coercible; a validator rejects any argument object that mixes them.
**Rationale trace:** A1; MAK-DOT §03 and FZ-1; Abbas 2025 (unvalidated confidence is liability).

### FS-4 (MUST)
**Statement:** Each register has a ratified *codebook*: the vocabulary of words (with their fuzzy models) that the register's renderer may emit. All three codebooks derive from the same LinguisticVariables — same meanings, different words — so register translation can never reweight content (MAK-FFC SPINE-3). Codebooks are versioned knowledge-plane artifacts.
**Rationale trace:** Mendel Per-C codebook doctrine; Miah–Blake–Kerr shared-ontology principle; SPINE-3.

### FS-5 (MUST)
**Statement:** The linguistic round trip is guaranteed (A3): the decoder maps every fuzzy output to the nearest codebook word (with its similarity recorded in the evaluation trace), and outputs that fall below a ratified similarity floor are not rendered linguistically — they surface as "outside vocabulary" and route to judgment. No renderer invents words or emits orphan outputs.
**Rationale trace:** Mendel's perceptual-reasoning FOU-resemblance requirement; anti-hallucination of meaning.

### FS-6 (MUST)
**Statement:** Patient-reported and secondhand grounds support the Z-ground schema: value component (crisp, linguistic, or hesitant expression) paired with an optional reliability component from a small ratified reliability vocabulary ("sure / fairly sure / guessing"). Reliability defaults to unstated rather than assumed; engines consume it as source-confidence on grounds and MUST NOT convert it into claim probability by fiat.
**Rationale trace:** Zadeh Z-numbers; medical Z-number methods corpus; FS-3 separation.

### FS-7 (MUST)
**Statement:** Hedges ("very", "slightly", "borderline") are ratified operators in the linguistic layer with defined semantics per LinguisticVariable — not free-text modifiers. The hedge inventory is deliberately small; adding a hedge is a governed change with the same ceremony as adding a term.
**Rationale trace:** hedge-explosion risk (FX risk register); Zadeh hedge algebra; governance economy.

### FS-8 (MUST)
**Statement:** Every crisp threshold that converts graded applicability into a release decision (α-cuts, activation floors, similarity floors) lives in the GenericArgument template, ratified and versioned — never in engine code or configuration. The deterministic evaluator reads thresholds only from the pinned template.
**Rationale trace:** MAK-FFC SPINE-7; MAK-DOT FZ-3; auditability of the cut itself.

### FS-9 (MUST)
**Statement:** Personalized semantics are patient-owned calibration data: a per-person mapping of that patient's words and scale usage onto the ratified LinguisticVariables (the PIS pattern). The profile is visible and revocable by the patient, applies only to *encoding that patient's own inputs*, and never alters engine weighting, thresholds, or another patient's meanings — value-to-weight mappings remain governed by MAK-FFC PF-3 exclusively.
**Rationale trace:** Li et al. 2016 PIS; MAK-FFC PF-3/PF-4 custody discipline; personalization-creep risk.

## Part 3 — The Clinician Face

**What the research reveals for this face.** Clinicians already think in graded language — Stranieri's ward-round fieldwork shows bedside reasoning as narrative and context-saturated, and Seising's point that symptom and disease borders are not sharp was cited by the Blake program as its own boundary warrant. What clinicians are given instead is binary chrome: criteria that are "met/not met," alerts that fire at 141 and sleep at 139, and (per Bayor's review) rigid structures that "restrict users from incorporating their own perspectives." The 2,020-assessment radiology RCT adds a sharper lesson: *reasoning-shaped* explanation improves clinician accuracy where bare outputs don't — and a graded criterion display is reasoning-shaped by construction. The fuzzy layer's job on this face is to show the clinician what the system can now see: how well, not merely whether, each criterion fits — and to convert boundary proximity into an invitation for judgment rather than a hidden coin-flip.

### Component inventory

| Component | Function | Research anchor |
|---|---|---|
| Graded Criterion Chips | Each criterion in an argument renders with its μ (numeric + miniature membership sketch), never a bare met/unmet binary where the underlying term is graded | A1/A3; radiology-RCT reasoning-shape finding; Blake per-criterion grain |
| Borderline Flag | Cases within a ratified proximity band of any release threshold auto-flag "borderline — judgment recommended," pre-opening the Deviation Composer with the boundary context | MAK-MIF beat 1; MAK-FFC SPINE-8/CF-3 |
| Applicability Column | On the Differential Board, guideline-applicability grades render in a column visually and semantically distinct from the posterior/conformal Qualifier column, each labelled as what it is | FS-3; MAK-DOT §03 table |
| Trend Descriptors | Consult-Prep narratives use ratified fuzzy temporal terms ("gradually worsening," "stable," "fluctuating") computed from monitoring series, decoded per FS-5 | CWW decoding; Blake diary statistics lesson |
| MDT Band View | Where a type-2 band exists (deferred trigger, FE-7), the disagreement band renders in MDT mode as the community's honest spread, attributed per FFC CF-6 | Type-2 literature; reasoning-communities line |

### Clinician Face requirements

### FC-1 (MUST)
**Statement:** Wherever a criterion is defined over a graded LinguisticVariable, the clinical register renders its degree of satisfaction (μ with its term label and a glanceable graphic), not a binarized verdict alone. Where a template's release logic binarizes (FS-8), both render: the grade and the ratified cut that was applied to it.
**Rationale trace:** A1/A3; MAK-FFC CF-2 (argument at criterion granularity); Spitzer 2026 (reasoning-shaped displays).

### FC-2 (MUST)
**Statement:** Boundary proximity is an event: when any operative value lies within the template's ratified borderline band of a threshold, the face flags the case as borderline, shows the distance-to-threshold, and offers the Deviation Composer with one interaction. Borderline flags are arguments in the fabric (auditable), not transient UI states.
**Rationale trace:** MAK-MIF beat 1; MAK-FFC SPINE-8, CF-3; cliff-effect evidence.

### FC-3 (MUST)
**Statement:** Graded applicability and belief render as separated channels: distinct columns/regions, distinct visual encodings, distinct labels ("fit to guideline term" vs "diagnostic probability"), and no composite score that blends them. A design review checklist item verifies the separation before any release of the face.
**Rationale trace:** FS-3; A1; anti-semantic-soup discipline.

### FC-4 (SHOULD)
**Statement:** Consult-Prep narratives and handover summaries use ratified trend descriptors computed from time-series grounds and decoded per FS-5, with the underlying series one interaction away. Free-text trend adjectives generated outside the codebook are marked as unratified language.
**Rationale trace:** FS-4/5; Blake sleep-statistics precedent; CWW decoding.

### FC-5 (MUST)
**Statement:** μ visual encodings meet the accessibility floor: never colour-only (shape/position/valence-redundant), tabular-numeric where digits align, and legible at the face's minimum supported display. Membership sketches carry axis context on demand.
**Rationale trace:** MAK-FFC PF-6 floor generalized; WCAG discipline.

### FC-6 (SHOULD)
**Statement:** Clinician-facing microcopy names gradedness honestly ("fits 'elevated' to 0.7") and never uses confidence/probability vocabulary for μ or activation strengths; the copy deck is linted against a prohibited-vocabulary list derived from FS-3.
**Rationale trace:** A1; copy-as-conformance; MAK-DOT anti-patterns.

### FC-7 (MUST)
**Statement:** Face evaluation (per MAK-FFC CF-7's independent-evaluator rule) adds fuzzy-specific measures: comprehension of graded chips vs binary chips, borderline-flag utility (justified-deviation rate on flagged vs unflagged boundary cases), and misreading rate of μ as probability — the last with a pass ceiling ratified before pilot.
**Rationale trace:** MAK-FFC CF-7; the field's missing usability evidence (Abbas 2025; MAK-FFC research agenda).

### Clinician Face anti-requirements

- Never a blended "overall score" that mixes μ, activation, posterior, or coverage into one number (violates FS-3/A1).
- Never colour-only encoding of gradedness (FC-5), and never a traffic-light metaphor for μ — red/green implies verdict, not degree of meaning.
- Never let a borderline flag block or nag — it invites judgment (one interaction), it does not gatekeep (MAK-FFC CF-3/CF-4 hold).
- Never render an unratified word for a graded state (FS-5's orphan-output ban applies to microcopy too).

## Part 4 — The Patient Face

**What the research reveals for this face.** This is where the left wing pays for itself twice. First, intake: patients speak in hedged, hesitant language — "somewhat better," "between mild and moderate," "pretty bad, I think" — and the CWW literature (2-tuple models, hesitant fuzzy linguistic term sets, ELICIT comparative expressions) exists precisely to accept such input *as data* rather than coerce it into a brittle 1–10. Second, feedback: the Blake diary's day-by-day graph proved that immediate, legible reflection of a patient's own data drives engagement; a membership-scale visual ("here is where today sits on 'elevated'") is that lesson upgraded with mathematics. And for the north star: in low-literacy, low-resource contexts, words and pictures work where numeric instruments intimidate — the linguistic layer is an accessibility technology before it is anything else. The personalization literature adds the caution this corpus hard-codes: words mean different things to different people, so calibration is per-person, patient-owned, and strictly input-side (FS-9).

### Component inventory

| Component | Function | Research anchor |
|---|---|---|
| Linguistic Intake Controls | Word-chips, hedged options, and "between X and Y" hesitant expressions as first-class answers alongside numeric entry; encoded per the plain codebook | HFLTS/ELICIT; CWW encoder; Blake accessibility-first design |
| Reliability Dial | Optional one-tap "how sure?" companion to self-reported answers ("sure / fairly sure / guessing") writing the Z-ground reliability component | FS-6; Z-number medical corpus |
| Personal Scale Calibration | Short onboarding exercises anchoring the patient's words to reference descriptions; stores the PIS profile (patient-owned, revocable) | FS-9; Li 2016 PIS; Pei 2024 credibility |
| Membership Scale Visual | "Where today sits" sliding-scale rendering of a reading against the relevant term — the diary-graph lesson with a ratified curve behind it | Blake 2014 feedback→reflection; FS-5 decoding; MAK-FFC PF-5 |
| Plain Trend Cards | Ratified plain-codebook trend words ("settling," "creeping up") over self-monitoring series, always with the underlying picture | FC-4 mirror; SPINE-3 register fidelity |

### Patient Face requirements

### FP-1 (MUST)
**Statement:** Intake instruments accept linguistic answers as first-class data: single terms, ratified hedges, and hesitant "between X and Y" expressions, encoded against the plain codebook into the same LinguisticVariables the clinical register reads. Numeric entry remains available; neither modality is second-class, and the stored ground records which modality was used.
**Rationale trace:** HFLTS/ELICIT literature; MAK-FFC PF-1; low-literacy accessibility (north star).

### FP-2 (MUST)
**Statement:** Every self-reported ground offers (never demands) the reliability dial; the answer writes the Z-ground reliability component from the ratified reliability vocabulary. Declining to answer stores "unstated." No renderer or engine treats unstated as either sure or unsure.
**Rationale trace:** FS-6; Z-number corpus; consent-grade honesty about what we know of what we know.

### FP-3 (MUST)
**Statement:** Personal scale calibration is offered at onboarding and editable thereafter; the resulting PIS profile is visible to the patient in plain language ("when you say 'bad pain' we read it as …"), revocable in one action, and applied only to encoding that patient's inputs (FS-9). Calibration never runs silently from behavioural inference.
**Rationale trace:** FS-9; MAK-FFC PF-3's no-silent-inference doctrine extended to semantics.

### FP-4 (MUST)
**Statement:** Self-monitoring feedback renders the membership-scale visual: the patient's value positioned on the relevant term's curve in plain-codebook words, immediately on entry, offline-capable. The same artifact (register-styled) is what the clinician sees, preserving the shared vocabulary.
**Rationale trace:** Blake diary lesson; MAK-FFC PF-5/PF-6; SPINE-3.

### FP-5 (MUST)
**Statement:** The plain register renders gradedness in everyday words with honest hedging ("a little high today") and never as percentages, probabilities, or scores of any kind; where the clinical register shows μ = 0.7, the plain register shows the decoded word plus the scale visual. The plain codebook's prohibited-vocabulary lint includes all belief-language.
**Rationale trace:** A1/A3; FS-4/5; MAK-FFC PF-2 register fidelity.

### FP-6 (SHOULD)
**Statement:** Low-resource profiles prefer linguistic intake as the primary modality (word-chips over keypads; IVR menus speak codebook terms), with codebook packs installable per jurisdiction and language under the knowledge plane's lineage rules.
**Rationale trace:** MAK-FFC XC-3/XC-4; WHO SMART localization pattern; accessibility evidence.

### FP-7 (MUST)
**Statement:** Patient-face fuzzy renderings appear only within MAK-FFC PF-8's release discipline: gradedness of the patient's own observations may render immediately (self-monitoring feedback); gradedness attached to diagnostic claims renders only after clinician release, in the plain register, with the deviation-honesty rule intact.
**Rationale trace:** MAK-FFC PF-2/PF-8; regulatory posture (XC-1; MAK-J3 boundary).

### FP-8 (SHOULD)
**Statement:** Patient-face evaluation includes linguistic-equity measures: completion and comprehension rates for linguistic vs numeric modalities across literacy bands, and PIS-calibration uptake/revocation rates — reported to the auditor face's system lens.
**Rationale trace:** north star measurement; MAK-FFC research agenda (gap-closing metric); AF-8 lens discipline.

### Patient Face anti-requirements

- Never coerce a hedged or hesitant answer into a point value at capture ("between mild and moderate" is stored as such, not averaged).
- Never infer a patient's semantics from behaviour and apply it silently (FS-9/FP-3); calibration is explicit or absent.
- Never use the reliability dial punitively (down-weighting "guessing" patients out of their own care narrative); reliability informs interpretation, not worth.
- Never show a patient a naked μ, percentage, or score (FP-5); the plain register speaks words and pictures.

## Part 5 — The Auditor Face

**What the research reveals for this face.** Fuzzy systems are the auditor's dream and nightmare at once. Dream: every inference is a readable rule over a published curve — the compliance register can show the exact mathematics behind any graded state, and IEEE 1855 gives the whole knowledge base a diffable serialization. Nightmare: the curves themselves are power — whoever tunes a membership function tunes what "elevated" means for every downstream decision, which is why the primer's "nudge the curve to reduce alert fatigue" dial was this corpus's canonical corrected move. The auditor face therefore gets three fuzzy duties: *render the math* (transparency), *govern the meanings* (the curve-change workbench specializing MAK-FFC AF-5), and *watch the semantics drift* — using membership-credibility measures (Pei 2024) and boundary-clustered override patterns as the evidence stream that a ratified meaning no longer matches practice.

### Component inventory

| Component | Function | Research anchor |
|---|---|---|
| Membership Math View | For any decision: the fired rules, activation strengths, μ-vectors, defuzzification method and value, thresholds applied — the full trace, on demand | Primer's auditor flow, governed; A4; FS-8 |
| Curve-Change Workbench | AF-5 specialization: proposals against specific LinguisticVariables, evidence panels (drift metrics, override clusters, credibility scores), FML diff view, ratification workflow, version pinning | MAK-FFC AF-5; MAK-DOT FZ-4; Pei 2024 |
| Semantic Drift Telemetry | Standing metrics per LinguisticVariable: boundary-band case density, override clustering near thresholds, PIS-population divergence from ratified curves, credibility trend | MAK-MIF beat 3; Pei 2024; FS-9 aggregates |
| Boundary-Sweep Findings | Corruption-engine cliff/boundary findings rendered as rebuttals against the warrants they defeat, queued for review | MAK-FFC EN-5; MAK-DOT FZ-5 |
| Graded-State Compliance Projector | Ratified mapping from graded applicability states to the binary compliance vocabularies external reporting demands, with the mapping itself versioned and exported | MAK-FFC AF-3/AF-7; honesty at the reporting boundary |

### Auditor Face requirements

### FA-1 (MUST)
**Statement:** The compliance register renders, for any argument on demand: every fired fuzzy rule with its activation strength, the grounds μ-vectors with MF version pins, the defuzzification method and value, and the ratified thresholds applied — sufficient for an external reviewer to recompute the graded evaluation by hand from the FML artifacts.
**Rationale trace:** A4; TGA criterion (c) independent-verifiability language; AF-7 conformity bundles.

### FA-2 (MUST)
**Statement:** Membership-function change flows only through the Curve-Change Workbench implementing MAK-FFC AF-5: evidence-bearing proposal → governed ratification → new FML version → old versions pinned to their decisions. No face, role, or configuration path can alter a curve outside this flow — including "temporary," per-site, or emergency changes.
**Rationale trace:** A2; MAK-DOT FZ-4; the primer's corrected dial; alert-governor-abuse risk.

### FA-3 (MUST)
**Statement:** Semantic drift telemetry runs continuously per LinguisticVariable — boundary-band density, override clustering near thresholds, aggregate PIS divergence, and membership-credibility trend — and feeds the workbench as evidence. Telemetry informs proposals; it never auto-triggers curve change.
**Rationale trace:** MAK-MIF beat 3; Pei et al. 2024; AF-5's human-ratification boundary.

### FA-4 (MUST)
**Statement:** The graded-state compliance projection is itself a ratified, versioned artifact: which graded applicability states map to which external binary/categorical compliance vocabularies, exported with AF-7 bundles so a regulator can audit the flattening, not merely its output.
**Rationale trace:** MAK-FFC AF-3/AF-7; the flattening is where graded honesty is most easily lost.

### FA-5 (MUST)
**Statement:** FML diffs are first-class review objects: any curve-change proposal renders as a human-readable diff (terms, parameters, supports, thresholds affected) plus an impact preview replaying a sentinel decision set under old and new versions, with flips enumerated.
**Rationale trace:** IEEE 1855 diffability; MAK-FFC EN-8 sentinel replay; informed ratification.

### FA-6 (SHOULD)
**Statement:** Boundary-sweep findings (FE-8) queue in the auditor face with the same review discipline as deviations: severity-ranked, warrant-anchored, resolvable only by acknowledgment (rebuttal published) or template change (AF-5 path).
**Rationale trace:** MAK-FFC EN-5/AF workflow symmetry; MAK-DOT FZ-5.

### FA-7 (SHOULD)
**Statement:** Aggregate fuzzy views default to variable-level and guideline-level lenses; clinician-level lenses over graded data (e.g., an individual's override pattern near boundaries) inherit MAK-FFC AF-8's governed-grant discipline in full.
**Rationale trace:** MAK-FFC AF-8; surveillance-capture risk.

### Auditor Face anti-requirements

- Never a curve-tuning affordance outside the workbench — no dial, no slider, no "preview in production" (FA-2).
- Never auto-ratification of drift-suggested curves, however strong the telemetry (FA-3).
- Never export flattened compliance states without the versioned projection that produced them (FA-4).
- Never treat activation strengths in the math view as confidence measures — the compliance register obeys FS-3 like every other register.

## Part 6 — The Engines

**What the research reveals for this plane.** Four engineering facts organize everything. First, fuzzy inference is cheap, deterministic, and vectorizable — the FuzzyLite family and scikit-fuzzy make graded evaluation a solved runtime problem (A4). Second, method choice is semantic: Mamdani inference preserves linguistic interpretability end-to-end (right for graded applicability that must decode to words); Takagi–Sugeno produces functional outputs (right for internal numeric blending) — so the choice belongs in the template, not the code. Third, curves can be *learned but never self-ratified*: fuzzy c-means and pyFUME-class pipelines propose membership functions from data, and the ArgTumour/Fan-2026 pattern extends proposal to LLM extraction of fuzzy predicates from narrative — all of it lands as draft artifacts for human ratification, the "ML proposes" doctrine verbatim. Fourth, the fuzzy layer gives the corruption engine a gift: the geometry of every membership function is a pre-drawn map of where the system's behaviour changes fastest — the natural coordinates for adversarial sweeps.

### The fuzzification service contract

```text
interface FuzzificationService {
  inputs:  CrispOrLinguisticGround      // value | codebook word | hesitant expression | Z-ground
  context: LinguisticVariable[]         // pinned versions, jurisdiction lineage resolved
  emit():  GradedGroundAnnotation {
    memberships: { term: string, mu: number }[]   // per applicable term
    encoding:    EncodingTrace                     // modality, PIS profile version if applied
    reliability: ZReliability | "unstated"         // FS-6 passthrough, never transformed
    pins:        VersionSet                        // MF versions, codebook version
  }
}
// Placement: data plane, grounds preparation (FS-2). Pure function of inputs+pins.
// Downstream: warrant-applicability grading inside per-criterion engines (MAK-FFC EN-2),
// then the deterministic evaluator applies template-ratified thresholds (FS-8) — release
// only as argument content (MAK-FFC SPINE-1/7).
```

### Engine requirements

### FE-1 (MUST)
**Statement:** Fuzzification is a pure, versioned service: identical inputs and pins yield identical annotations, with no state, no learning, and no side channels. It implements the contract above and is exhaustively property-tested (monotonicity where the MF is monotone, boundary values, hedge composition).
**Rationale trace:** A4; SPINE-5 replayability; MAK-FFC EN-1 contract discipline.

### FE-2 (MUST)
**Statement:** Inference and defuzzification methods are template metadata: each GenericArgument's fuzzy preconditions declare their inference family (Mamdani for linguistic outputs, TSK for functional blends) and defuzzifier, ratified and pinned like any warrant content. Engines refuse templates whose method metadata is absent.
**Rationale trace:** method choice is semantics, not implementation; FS-8; fuzzylite method inventory.

### FE-3 (MUST)
**Statement:** Graded applicability computed by per-criterion engines lands in the ActualArgument as warrant-applicability content and evaluation-trace entries only; the deterministic evaluator alone converts grades to release decisions via FS-8 thresholds. No fuzzy component emits claims, recommendations, or scores toward any face.
**Rationale trace:** MAK-FFC SPINE-1/7; MAK-DOT FZ-3; A1.

### FE-4 (MUST)
**Statement:** Curve learning is proposal-only: data-driven pipelines (fuzzy c-means/pyFUME-class) and LLM extraction of fuzzy predicates from narrative run offline, emit draft LinguisticVariable artifacts with their training provenance, and enter the knowledge plane only through the Curve-Change Workbench's ratification (FA-2). Learned drafts never serve runtime traffic.
**Rationale trace:** "ML proposes and tests; only arithmetic releases"; Fan 2026 fuzzy-neuro-symbolic pattern; MAK-FFC EN-6 classes.

### FE-5 (MUST)
**Statement:** Coupling to the Bayesian differential is one-directional and double-counting-safe: graded grounds may inform likelihood inputs under template-declared mappings, but a ground's gradedness and its crisp value never both enter the same likelihood as if independent, and no posterior ever feeds back into a μ. The coupling map is part of the template and replays with it.
**Rationale trace:** hybrid fuzzy-probabilistic literature (fuzzy as input semantics); FS-3; statistical hygiene.

### FE-6 (MUST)
**Statement:** The CWW render path (encoder → reasoning → decoder) is engine-plane machinery under the same discipline: codebook-pinned, similarity-floored (FS-5), with decode traces in the argument. Register renderers call it; they never implement private linguistic logic.
**Rationale trace:** Mendel Per-C; SPINE-3 single render source; FS-4/5.

### FE-7 (MAY)
**Statement:** An interval type-2 module may be introduced only on the ratified trigger: a real curve-ratification dispute where the community can agree a band but not a point. Its adoption is a governed change adding footprint-of-uncertainty semantics to the affected LinguisticVariables; type-reduction method becomes template metadata per FE-2.
**Rationale trace:** MAK-DOT type-2 deferral; Mendel IT2 doctrine; complexity economy.

### FE-8 (MUST)
**Statement:** The corruption engine maintains the boundary-sweep class: for every ratified MF, adversarial cases are generated across supports, crossover points, and threshold neighbourhoods; confirmed cliff or instability findings publish as rebuttals on the affected warrants and queue per FA-6. An engine version with unacknowledged boundary findings inherits MAK-FFC EN-5's release bar.
**Rationale trace:** MAK-FFC EN-5; MAK-DOT FZ-5; membership geometry as adversarial map.

### FE-9 (SHOULD)
**Statement:** Runtime fuzzy evaluation is vectorized and budgeted (the FuzzyLite-class implementations set the bar); the linguistic layer's per-decision cost is measured in the engine telemetry so gradedness never becomes the latency excuse for binarizing.
**Rationale trace:** pyfuzzylite vectorization; EN-9 telemetry lens; pragmatic defence of A1.

## Part 7 — Cross-cutting execution

### Standards bindings

### FX-1 (MUST)
**Statement:** IEEE Std 1855-2016 (FML) is the canonical serialization for LinguisticVariables, rule bases, and codebooks; IEC 61131-7 (FCL) and FIS formats are import-only legacies. Data-plane bindings: gradedness annotations travel as FHIR Observation components/extensions referencing the FML artifact and version; Z-ground reliability as a paired component; nothing fuzzy is stored without its pins.
**Rationale trace:** FS-1/2; JFML/IEEE 1855; MAK-FFC SPINE-4 data-plane discipline.

### J-tier map

### FX-2 (MUST)
**Statement:** Tier placement is fixed: the fuzzy layer is native to J-1 (deterministic, transparent — A4) and available to J-2; fuzzy *inference over patient data* is excluded from J-3 builds (structurally absent per MAK-J3 GPP-8, namespaces on the denylist per MAK-ELSM §08), because fuzzy-derived patient grading is new diagnostic information under TGA criterion (a) regardless of its transparency. Verbatim display of guideline hedge language remains J-3-permissible.
**Rationale trace:** MAK-DOT FZ-6 absorbed; MAK-J3 §2.2; TGA recommendation definition.

### Testing & validation regime

### FX-3 (MUST)
**Statement:** The fuzzy layer ships with a validation harness inside the evaluation firewall: (i) golden linguistic corpora per LinguisticVariable (expert-labelled cases with expected term assignments); (ii) round-trip tests — encode→decode word-recovery rate with a ratified floor; (iii) curve sensitivity analysis — decision-flip counts under parameter perturbation, reported per template; (iv) misreading studies per FC-7/FP-8. Results version with the artifacts they test.
**Rationale trace:** MAK-FFC EN-7 firewall; A3 contract testability; the field's validation gap (Abbas 2025).

### Phased execution plan

| Phase | Builds | Gate to exit |
|---|---|---|
| `LW-P0 · Linguistic layer` | LinguisticVariable schema + FML pipeline; fuzzification service; FS-8 thresholds in one guideline domain's templates | FS-1..8 conformance suite green; round-trip floor ratified; sentinel replay clean |
| `LW-P1 · Clinician gradedness` | Graded Criterion Chips, Borderline Flag, Applicability Column on the P1 pathway | FC-7 study with independent clinicians; μ-misreading under ratified ceiling |
| `LW-P2 · Patient words` | Linguistic intake controls, membership scale visual, plain codebook + lint | FP-8 linguistic-equity baseline recorded; PF-6 floor holds with linguistic modality |
| `LW-P3 · Meaning governance` | Curve-Change Workbench, drift telemetry, FML diff + impact preview, boundary-sweep queue | First governed curve change ratified from drift evidence and replayed against both versions |
| `LW-P4 · Reliability & person` | Z-ground capture (reliability dial), PIS calibration (patient-owned) | FS-6/9 audits pass; revocation path tested; no engine-weighting leakage |
| `LW-P5 · Proposal pipelines` | Curve-learning drafts (c-means/pyFUME-class); LLM fuzzy-predicate extraction pilot (offline, ratification-gated) | FE-4 boundary holds under red-team attempt to reach runtime; draft-quality review |

### Risk register

| Risk | Mechanism | Standing control |
|---|---|---|
| Semantic soup | μ, activation, posterior, reliability blur into one "confidence" in UI, copy, or code | FS-3 non-coercible types; FC-3/FP-5 channel separation; prohibited-vocabulary lint (FC-6) |
| Curve gaming | Meanings tuned to suppress alerts or flatter metrics | FA-2 single change path; FA-3 telemetry-not-trigger; FA-5 flip-preview at ratification; theater detector inheritance (MAK-FFC AF-4) |
| False precision theater | μ = 0.72 read as accuracy about the world rather than a ratified meaning's fit | FC-6/FP-5 copy discipline; FA-1 math-on-demand keeps μ anchored to its curve; calibration studies (FX-3) |
| Hedge & term explosion | Vocabulary sprawl until nothing is ratifiable or learnable | FS-7 small ratified hedge inventory; codebook governance (FS-4); annual vocabulary review in AF-5 cadence |
| Orphan outputs | Decoded language drifts from the ratified codebook (LLM-assisted copy is the vector) | FS-5 similarity floor + "outside vocabulary" routing; FE-6 single render path |
| Personalization creep | PIS profiles leak from input calibration into weighting or across patients | FS-9/FP-3 hard boundary; FX-3 leakage audit; patient-visible profile |
| Binarization relapse | Latency or UI pressure quietly restores met/unmet everywhere | FC-1 render mandate; FE-9 cost telemetry; conformance suite checks graded paths exist per template |
| J-3 seepage | Fuzzy inference lands in the exempt build via a shared module | FX-2 + MAK-J3 GPP-8 SBOM denylist; GPP-CONF negative tests |

### Open research agenda

- **μ-literacy.** No published evidence exists on clinicians' misreading rates of membership degrees in live decision UIs; FC-7's ceiling needs an instrument and a baseline study.
- **Linguistic-equity effect size.** FP-8's hypothesis — linguistic intake outperforms numeric in low-literacy cohorts — is well-motivated and unmeasured in CDSS settings; pre-register it in the low-resource pilot.
- **Drift-to-ratification latency.** How fast should governed meaning change be? FA-3/FA-5 create the telemetry; the governance cadence is an empirical question with safety stakes on both sides.
- **Z-ground utilization.** When and how should engines consume reliability components without punishing honest uncertainty (FP anti-requirement)? The Z-number MCDM literature offers methods; none is validated at point-of-care.
- **Fuzzy-predicate extraction fidelity.** The Fan-2026 pattern needs a Mākoha-grade evaluation: extraction precision/recall against clinician-annotated narratives before LW-P5 exits.

## Part 8 — Traceability, FZ absorption & sources

### FZ absorption map (MAK-DOT → this corpus)

| MAK-DOT proposal | Absorbed into |
|---|---|
| FZ-1 (type separation) | FS-3 (schema law) + FC-3/FC-6, FP-5 (register enforcement) |
| FZ-2 (FML knowledge-plane artifacts) | FS-1 + FX-1 |
| FZ-3 (no direct release) | FS-8 + FE-3 |
| FZ-4 (governed curve change) | FA-2/FA-3/FA-5 (+ workbench component) |
| FZ-5 (boundary sweeps) | FE-8 + FA-6 |
| FZ-6 (J-3 exclusion) | FX-2 |

### Findings → requirements

| Finding | Source | Requirements it drives |
|---|---|---|
| Vagueness ≠ uncertainty ≠ reliability; each has distinct mathematics and must not exchange clothes | Zadeh 1965/1999; Dubois & Prade; MAK-DOT §03 synthesis | A1, FS-3, FC-3, FP-5, FE-5 |
| Linguistic in / linguistic out with codebooks, word-models, and decode-to-vocabulary discipline | Zadeh CWW 1999; Mendel Per-C 2008/2010; Herrera CWW line 2009–2021; ELICIT 2020 | FS-4/5, FP-1, FC-4, FE-6 |
| Words mean different things to different people; per-person semantics are learnable and must be governed | Li et al. 2016 (PIS); Pei et al. 2024 (membership credibility) | FS-9, FP-3, FA-3 |
| Partially reliable self-report as (restriction, reliability) pairs with mature decision methods | Zadeh Z-numbers; Aliev 2016; Wang 2017; Ren 2020; Zhao 2022; Alam 2023 review | FS-6, FP-2 |
| Deterministic, standard-serializable fuzzy systems; production-grade runtimes; method inventories | IEEE 1855/JFML; IEC 61131-7; fuzzylite/pyfuzzylite; scikit-fuzzy; Simpful (MAK-ELSM/MAK-DOT verified) | A4, FS-1, FE-1/2/9, FX-1 |
| Experts disagree about meanings themselves; bands are ratifiable when points are not | Mendel IT2 doctrine; type-2 clinical literature 2024–25 | FE-7 (trigger-gated), FC MDT band view |
| Curves can be learned from data and narrative but must land as human-ratified drafts | pyFUME/fuzzy c-means; Fan et al. 2026 (LLM fuzzy predicates, symbolic verification); ArgTumour pattern | FE-4, LW-P5, FA-2 |
| Graded, reasoning-shaped displays help clinicians; naked scores and blended confidences do not | Spitzer et al. 2026 RCT; Abbas et al. 2025 XAI gaps; Bayor et al. 2025 rigidity findings | FC-1/3/7, FP-5 |
| Immediate visual feedback on one's own data drives patient reflection; accessibility-first intake works across literacy bands | Blake & Kerr 2010/2014 (diary, 267-user study) | FP-1/4, FP-6 |
| Fuzzy patient-grading is diagnosis-contributing regardless of transparency; exempt tier excludes it structurally | TGA criteria (a)/(c) (verbatim-reviewed); MAK-J3 | FX-2 |

### Sources

- Foundations: Zadeh 1965 (fuzzy sets) · Zadeh 1999, *From computing with numbers to computing with words* · Zadeh 2011 (Z-numbers) · Dubois & Prade (possibility vs probability) · Seising 2006 (vagueness in medical thought; the Blake program's own citation).
- Computing with Words & perceptual computing: Mendel & Wu 2010, *Perceptual Computing* · Mendel et al. 2008, Perceptual Reasoning (IEEE TFS) · Herrera et al. 2009 · Martínez-López et al. 2010 · Herrera-Viedma et al. 2021 (IEEE TSMC fifty-year tour) · Li et al. 2016, personalized individual semantics (Inf. Fusion) · Romero et al. 2020, ELICIT (IEEE TFS) · Pei et al. 2024, membership-function credibility (IEEE TFS).
- Z-numbers in medicine and decision: Aliev et al. 2016 · Wang et al. 2017 (Cognitive Computation) · Wu et al. 2017 (Applied Intelligence) · Ren et al. 2020 (COVID-19 medicine selection) · Zhao et al. 2022 (PLoS ONE) · Alam et al. 2023 state-of-the-art.
- Clinical fuzzy systems, 2024–26: Thukral et al. 2025 (chronic-disease PRISMA review) · Zacarias-Morales et al. 2025 (ANN+attention+fuzzy review) · Cherukuri et al. 2026 (regulation-ready fuzzy expert systems agenda) · Zakaria 2026 (human-centric FCM, Sci. Reports) · type-2 clinical set (Chen 2025; Malyar 2024; Manikandabalaji 2024) · Dadashkarimi 2025 (hybrid fuzzy+LR) · CADIAG-2 lineage (Adlassnig, Vienna).
- Fuzzy × LLM frontier: Fan et al. 2026 (arXiv — fuzzy symptom predicates, symbolic verification, auditable paths) · Yang 2025, CLMN (IEEE SMC) · neuro-symbolic surveys and design patterns (Yang et al. 2024; de Boer et al. 2025).
- Standards & tooling (verified in MAK-ELSM/MAK-DOT): IEEE Std 1855-2016 + [JFML](https://github.com/sotillo19/JFML) · IEC 61131-7 · [scikit-fuzzy](https://github.com/scikit-fuzzy/scikit-fuzzy) · [Simpful](https://github.com/aresio/simpful) · [pyfuzzylite](https://github.com/fuzzylite/pyfuzzylite) · [PyIT2FLS](https://github.com/Haghrah/PyIT2FLS) · [FCMpy](https://github.com/SamvelMK/FCMpy).
- Series: MAK-FFC v1.1 (host architecture and all cited SPINE/CF/PF/AF/EN/XC/GPP IDs) · MAK-DOT (absorbed proposals) · MAK-MIF (the eight beats this corpus operationalizes) · MAK-ELSM v1.1 · MAK-J3 · Sleep Tools Dossier · The Stranieri File · uploaded evidence base (Bayor 2025; Abbas 2025; Cockburn 2024; Chapman corpus).

## Part 9 — Execution sourcing annex (v1.1, additive)

Parts 0–8 say what to build; this annex says what already runs. Every repository row below reflects a direct fetch of the repo page (30 Aug – 1 Sep 2026), not training-data memory, and every entry is mapped to the corpus requirements it serves. Verdict vocabulary follows MAK-ELSM: **ADOPT / ADAPT / STUDY / BUILD / WATCH**. The honest headline: the *inference core* is a solved, multiply-implemented problem; the *authoring and learning path* has real tooling with license caveats; and the corpus's most distinctive components — the CWW decoder with a similarity floor, the Z-ground schema, membership-credibility telemetry — have **no open-source precedent anywhere**, which is the same moat pattern MAK-ELSM found for the justification fabric.

### 9.1 Inference core & type-2 (FE-1/2/3/9, FE-7)

| Repo / artifact | What it gives you | Status (verified) | Verdict → serves |
|---|---|---|---|
| [fuzzylite/pyfuzzylite](https://github.com/fuzzylite/pyfuzzylite) (+ C++ sibling) | Production-grade controllers (Mamdani, TSK, Tsukamoto…), 25 term shapes, 7 defuzzifiers, *vectorized*; FLL language, FCL/FIS import | 81★ · GPL-3.0 + commercial dual · v8.0.6 · active | ADAPT (license review) → FE-1/2/9 |
| [scikit-fuzzy](https://github.com/scikit-fuzzy/scikit-fuzzy) | SciPy-native membership functions, Mamdani control, fuzzy c-means — the prototyping bench | 872★ · BSD · v0.5.0 Aug 2024 · active | ADOPT (prototyping) → LW-P0 spikes, FE-4 c-means |
| [aresio/simpful](https://github.com/aresio/simpful) | Rules as readable strings — the natural authoring surface for clinician-reviewable warrant preconditions | 148★ · AFL-3.0 · maintained · IJCIS 2020 paper | ADOPT → FS-1 authoring, FE-2 templates |
| [Haghrah/PyIT2FLS](https://github.com/Haghrah/PyIT2FLS) | Type-1 + interval type-2 Mamdani/TSK on NumPy | 87★ · MIT · v0.8.6 Apr 2025 · active | STUDY (FE-7 trigger-gated) |
| [LUCIDresearch/JuzzyPython](https://github.com/LUCIDresearch/JuzzyPython) (+ [JuzzyV2](https://github.com/chwagnLUCID/JuzzyV2) Java) | Wagner's academic reference toolkit: T1, IT2, and *general* type-2 systems, non-singleton inputs — the fullest type-2 semantics in open code | 11★ · license not surfaced in repo page — confirm before use · active (172 commits) | STUDY → FE-7 semantics reference |

### 9.2 Serialization, authoring & governance path (FS-1/4, FA-2/5, FX-1)

| Repo / artifact | What it gives you | Status (verified) | Verdict → serves |
|---|---|---|---|
| [sotillo19/JFML](https://github.com/sotillo19/JFML) + IEEE Std 1855-2016 | The FML reference implementation: parse, build, import/export standard fuzzy-system XML — the file format FS-1 mandates (a Python wrapper, Py4JFML, exists in the literature: FUZZ-IEEE 2019) | Java · Univ. Córdoba · IEEE Access 2018 paper | ADOPT AS FORMAT → FS-1, FX-1, FA-5 diffs |
| [FisPro](https://github.com/cran/FisPro) (fispro.org · CRAN pkg v1.1.4) | Expert-in-the-loop FIS *design* tool from INRAE with an interpretability doctrine (strong fuzzy partitions, readable rule bases) plus an R runtime — the closest existing thing to a Curve-Change Workbench authoring bench | GUI + R package · long-maintained research software | STUDY/ADOPT (authoring-side) → FS-1 drafting, FA-2 workbench design |
| [SamvelMK/FCMpy](https://github.com/SamvelMK/FCMpy) | Fuzzy cognitive map construction/simulation/learning — authoring-time causal sketching only, per MAK-DOT | Python · PeerJ CS 2022 | STUDY (authoring-time) → guideline-compilation aids |

### 9.3 Learning-as-proposal pipelines (FE-4, LW-P5)

| Repo / artifact | What it gives you | Status (verified) | Verdict → serves |
|---|---|---|---|
| [CaroFuchs/pyFUME](https://github.com/CaroFuchs/pyFUME) | Estimates Takagi–Sugeno fuzzy models from data (clustering → membership functions → consequents), emitting executable Simpful models — the draft-curve generator FE-4 specifies, nearly verbatim | 20★ · GPL-3.0 · 208 commits · FUZZ-IEEE 2020 paper | ADAPT (GPL review; offline-only anyway) → FE-4 drafts |
| ANFIS lineage (twmeggs/anfis; PyTorch ports) | Neuro-fuzzy parameter learning — an alternative draft-proposal family | Classic repos dormant; treat as literature with code | STUDY → FE-4 alternatives |
| scikit-fuzzy `cmeans` | The minimal in-house path: cluster → fit parametric MFs → serialize FML → workbench ratification | BSD · maintained | ADOPT → FE-4 default |

### 9.4 Graded group decision & MDT support (FC MDT view, FA prioritization)

| Repo / artifact | What it gives you | Status (verified) | Verdict → serves |
|---|---|---|---|
| [Valdecy/pyDecision](https://github.com/Valdecy/pyDecision) | 80+ MCDA methods including fuzzy AHP/TOPSIS/VIKOR/DEMATEL/EDAS/WASPAS — the computational bench for graded multi-criteria steps (e.g., FA-5 impact ranking, MDT option scoring). No hesitant-fuzzy variants — HFLTS/ELICIT encoding (FP-1) remains a build | 360★ · 395 commits · active · LLM-assisted interpretation UI | ADAPT → FA workbench analytics, MDT scoring experiments |

### 9.5 Worked medical examples (calibration for expectations)

Public fuzzy-medical code is demo-grade: a published walk-through of a scikit-fuzzy diabetes expert system (IJ-AI 2024) and typical student repositories (e.g., [Fuzzy_Diabetes_Detection](https://github.com/ChamaniS/Fuzzy_Diabetes_Detection); heart/diabetes rule bases). Verdict: **STUDY** — useful as onboarding exercises and as negative examples (hand-coded MFs, no versioning, no governance — everything FS-1/FA-2 exist to prevent). CADIAG-2, the one system with decades of hospital operation, was never open-sourced; its papers remain the design literature. No open repository anywhere implements *governed* fuzzy semantics — versioned membership functions with ratification workflows — which is this corpus's moat, confirmed empirically.

### 9.6 Confirmed build list (no OSS precedent found)

- **CWW decoder with similarity floor (FS-5, FE-6).** Perceptual-computing decoders exist as book MATLAB code and papers, not as maintained libraries; the codebook-pinned, trace-emitting decoder is a build with Mendel's perceptual-reasoning papers as the spec.
- **Z-ground schema and capture (FS-6, FP-2).** Targeted search found no maintained Z-number library in any ecosystem — the rich methods literature (Aliev ranking; Wang linguistic-Z; Alam review) is spec, not dependency.
- **Membership-credibility & drift telemetry (FA-3).** Pei et al. 2024 supplies the mathematics; no implementation ships.
- **PIS calibration service (FS-9, FP-3).** The 2016 Information Fusion model has no public reference implementation; the consistency-driven optimization is reproducible from the paper.
- **FML-native fuzzification microservice (FE-1) and Curve-Change Workbench (FA-2).** Assembled from ADOPT parts (runtime + FML + FisPro-style authoring), but the governed service itself is a build.

### 9.7 The 2025+ research plane (where code is absent, the frontier is not)

- **Fuzzy × LLM verification loops:** Fan et al. 2026 (LLM-extracted fuzzy symptom predicates, symbolic verification, physician-correctable inference paths — no public code confirmed: WATCH) and CLMN (IEEE SMC 2025, fuzzy-logic concept reasoning inside language models) define LW-P5's evaluation bar.
- **Membership credibility as a discipline:** Pei et al. 2024 (IEEE TFS) turns "is this curve still right?" into a measurable — the FA-3 telemetry spec.
- **Z-number decision methods keep compounding:** the 2025–26 wave (multipolar Z-Dombi; Pythagorean fuzzy Z-numbers with full arithmetic, ranking, and WASPAS extension) supplies increasingly practical operator sets for FS-6 consumption rules.
- **Type-2 clinical applications** (anaesthesia knowledge bases 2024; bed-allocation MCDM 2025) continue to accumulate the dispute-evidence FE-7's trigger waits for.
- **Regulation-ready fuzzy CDSS agenda** (Cherukuri 2026) is converging on this corpus's governance shape — a citation ally for the conformity file, and a signal the field will meet Mākoha where it already stands.

### Sourcing landmines (this annex's pass)

- License gradient across the fuzzy stack: pyfuzzylite GPL/commercial dual, pyFUME GPL-3.0, Simpful AFL-3.0, scikit-fuzzy BSD, PyIT2FLS MIT — the runtime you ship and the drafts pipeline you run offline have different license exposure; route legal review before LW-P0 dependency freeze.
- JuzzyPython surfaces no license in-repo — confirm with the maintainers before any use beyond reading.
- Py4JFML is paper-verified (FUZZ-IEEE 2019) but its repository activity was not verified this pass — treat as unconfirmed until fetched.
- Demo-grade medical repos embed hand-coded membership functions — import their *shapes* as draft evidence if ever, never their governance-free pattern (FS-1 prohibition).
- Fan 2026 has no confirmed public code; do not schedule LW-P5 against its availability.

*Document footer (source artifact):* The Left Wing Corpus v1.1 · 43 requirements (FS 9 · FC 7 · FP 8 · FA 7 · FE 9 · FX 3) · subordinate to MAK-FFC v1.1; absorbs MAK-DOT FZ-1..6 · propose changes as argued deviations. Research base: the series' verified tooling and literature plus the CWW, Z-number, and fuzzy-neuro-symbolic searches of 30 Aug–1 Sep 2026.

---

## Appendix A — ID census (additive)

Authoritative enumeration for validator checks. Count: **43**.

```json
{
  "doc_id": "MAK-LWC",
  "version": "1.1",
  "requirements": {
    "FS": ["FS-1","FS-2","FS-3","FS-4","FS-5","FS-6","FS-7","FS-8","FS-9"],
    "FC": ["FC-1","FC-2","FC-3","FC-4","FC-5","FC-6","FC-7"],
    "FP": ["FP-1","FP-2","FP-3","FP-4","FP-5","FP-6","FP-7","FP-8"],
    "FA": ["FA-1","FA-2","FA-3","FA-4","FA-5","FA-6","FA-7"],
    "FE": ["FE-1","FE-2","FE-3","FE-4","FE-5","FE-6","FE-7","FE-8","FE-9"],
    "FX": ["FX-1","FX-2","FX-3"]
  },
  "levels": {
    "MUST":   ["FS-1","FS-2","FS-3","FS-4","FS-5","FS-6","FS-7","FS-8","FS-9","FC-1","FC-2","FC-3","FC-5","FC-7","FP-1","FP-2","FP-3","FP-4","FP-5","FP-7","FA-1","FA-2","FA-3","FA-4","FA-5","FE-1","FE-2","FE-3","FE-4","FE-5","FE-6","FE-8","FX-1","FX-2","FX-3"],
    "SHOULD": ["FC-4","FC-6","FP-6","FP-8","FA-6","FA-7","FE-9"],
    "MAY":    ["FE-7"]
  },
  "absorbs": {"MAK-DOT": ["FZ-1","FZ-2","FZ-3","FZ-4","FZ-5","FZ-6"]},
  "retired": []
}
```

## Appendix B — Self-audit checks (additive)

1. **ID uniqueness** — no requirement ID appears in more than one requirement header.
2. **ID census parity** — headers matching `^### (FS|FC|FP|FA|FE|FX)-\d+ \((MUST|SHOULD|MAY)\)$` exactly equal Appendix A (43).
3. **Level parity** — each header's level matches its Appendix A bucket.
4. **Trace presence** — every requirement block carries a non-empty `**Rationale trace:**` line.
5. **Axiom compliance** — nothing in this document (tables and examples included) renders μ, activation strength, or a defuzzified value as probability/confidence (A1 applied to the document itself).
6. **Cross-doc resolution** — every MAK-FFC ID cited resolves in MAK-FFC v1.1 Appendix B (Annex 1 included); FZ-n citations resolve in MAK-DOT and in Part 8's absorption map.
7. **Subordination** — no FS/FC/FP/FA/FE/FX requirement relaxes a MAK-FFC MUST; deltas only narrow or specialize.
8. **Annex integrity (v1.1)** — Part 9 repo rows each carry a dated verification status and a requirement mapping; no verdict outside the MAK-ELSM vocabulary; the confirmed-build list and landmines stay consistent with the tables.
9. **Table integrity** — all markdown tables have consistent column counts per row.
10. **Stability** — IDs present in a previous version remain present or move to `retired`; retired IDs never reused.


