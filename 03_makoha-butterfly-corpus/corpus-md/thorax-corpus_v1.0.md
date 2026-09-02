---
doc_id: MAK-TXC
title: "The Thorax Corpus"
version: "1.0"
date: "2026-09-01"
series: "Mākoha research series — volume 11 · the Patient Face, consolidated from both wings"
status: normative-draft
normative_language: RFC-2119 (MUST / SHOULD / MAY)
req_prefixes: [TW, TR, TA, TC, TL, TE]
req_count: 28
subordinate_to: "MAK-FFC v1.1 — no requirement here relaxes a corpus MUST; consolidations state their sources"
builds_from:
  - "MAK-FFC v1.1 Part 4 — the host Patient Face (PF-1..8, component inventory, anti-requirements)"
  - "MAK-LWC v1.1 Part 4 — the fuzzy patient face (FP-1..8): linguistic intake, reliability dial, membership visuals, PIS calibration"
  - "MAK-RWC v1.1 Part 4 — the meta-rational patient face (MP-1..6): fit honesty, patient gap reports, values-as-remodeling, escape hatches"
  - "MAK-CEC v1.1 — the engine plane this face feeds and reads: grounds preparation, verdict stream, five-signal registry"
governed_by:
  - "REG-POSTURE v1.0 — ASSUME-REG-003 (patient-surface treatment is an OPEN counsel question gating GATE-000); REG-KEEP-003 (human sign-off); PF-8 release discipline carried"
changelog:
  - "v1.0 (2026-09-01): initial release — 28 requirements across TW/TR/TA/TC/TL/TE; three-corpus consolidation map (Part 7); sourcing annex (Part 8)."
companions:
  - "MAK-FFC v1.1 (host) · MAK-LWC v1.1 (left wing) · MAK-RWC v1.1 (right wing) · MAK-CEC v1.1 (engine plane) · MAK-HDC v1.0 (the face that releases to this one)"
  - "MAK-MIF v1.0 (beats 2 and 6 land on this face)"
  - "REG-POSTURE v1.0 (governing regulatory document)"
artifact_url: "https://claude.ai/code/artifact/04b4c517-5e26-426c-89b5-1ae6ba0c740a"
change_policy: "Requirement IDs are stable; retired IDs never reused. Propose changes as argued deviations."
---

<!-- LLM USAGE CONTRACT (additive; not part of the source document)
1. Requirement blocks (### TW-n / TR-n / TA-n / TC-n / TL-n / TE-n) are NORMATIVE;
   all other prose is INFORMATIVE. Part 8 is an informative sourcing annex.
2. This corpus CONSOLIDATES the patient-face requirements of MAK-FFC (PF),
   MAK-LWC (FP), and MAK-RWC (MP). Source IDs remain valid in their hosts; the
   Part 7 map is the cross-walk; a host requirement governs over any apparent
   difference here.
3. The release discipline binds generation: nothing diagnostic renders to a patient
   before clinician sign-off (PF-8/HA-1 via TR-1); the patient's own observations
   render immediately. Never design content that blurs the two classes.
4. ASSUME-REG-003 (patient-surface regulatory treatment) is OPEN and closes only by
   counsel attestation — an LLM must never resolve it, and TL-5 carries it.
5. Scope: face behaviour and components. Interaction-level specification is the
   Proboscis volume (Patient UI).
6. MUST violations in generated designs/code/documents require an explicit DEVIATION
   notice naming the ID.
7. Appendix A's ID census is authoritative for validator checks; Appendix B's
   self-audit checks gate any edit of this file.
END LLM USAGE CONTRACT -->

# The Thorax Corpus

A translatable research primer and execution manual for the Patient Face of the triple-facing CDSS — intake and self-monitoring, the plain register's rendering law, the patient's recorded acts, data custody and consent, the low-resource floor, and evaluation — consolidating the patient-face requirements of the host corpus and both wings into one buildable face.

**Document metadata:** Technical corpus · v1.0 · 1 Sep 2026 · eleventh volume in the Mākoha research series · STATUS: normative draft · REQ IDS: TW · TR · TA · TC · TL · TE · SUBORDINATE TO: MAK-FFC v1.1 · BUILDS FROM: PF + FP + MP + MAK-CEC · GOVERNED BY: REG-POSTURE v1.0.

## Contents

1. [Part 0 — How to use this document](#part-0--how-to-use-this-document)
2. [Part 1 — Foundation: the thorax of the butterfly](#part-1--foundation-the-thorax-of-the-butterfly)
3. [Part 2 — Intake & self-monitoring (TW)](#part-2--intake--self-monitoring)
4. [Part 3 — The plain register's rendering law (TR)](#part-3--the-plain-registers-rendering-law)
5. [Part 4 — Patient acts (TA)](#part-4--patient-acts)
6. [Part 5 — Custody & consent (TC)](#part-5--custody--consent)
7. [Part 6 — The low-resource floor (TL)](#part-6--the-low-resource-floor)
8. [Part 7 — Evaluation & consolidation maps (TE)](#part-7--evaluation--consolidation-maps)
9. [Part 8 — Execution sourcing annex](#part-8--execution-sourcing-annex)
10. [Appendix A — ID census](#appendix-a--id-census-additive)
11. [Appendix B — Self-audit checks](#appendix-b--self-audit-checks-additive)

## Thesis

> The thorax is the butterfly's engine room: every wingbeat is powered there, though the wings get the attention. The Patient Face is the system's thorax — the surface where nearly all of the system's grounds originate (intake, self-monitoring, values, reliability), where the north star lives or dies (a face unusable at low literacy or low bandwidth closes no gap), and where the literature's largest quantified hole sits (37 of 40 systems never faced the patient at all). Three corpora specified its layers: the host corpus placed capture before the encounter and gave the patient custody machinery and register fidelity; the left wing gave the face a mathematics for how patients actually speak — hedged words, hesitant ranges, stated unsureness — and the diary lesson upgraded with curves; the right wing gave it fit honesty ("was this tested on people like you?"), the gap report ("this doesn't describe me"), and escape hatches that never punish the unformalizable. The face law that integrates them: the patient's words arrive as data without coercion, the patient's view is the same truth in a second register — never a sanitized one — and everything diagnostic waits for a human signature. This corpus states it.

## Part 0 — How to use this document

This corpus is the Patient Face's single execution manual, sibling to MAK-HDC. It consolidates PF, FP, and MP sources (named in traces; Part 7 is the complete cross-walk); genuinely new face law is marked *(new)*. Interaction-level specification belongs to the Proboscis volume (Patient UI).

- **Normative language.** MUST / SHOULD / MAY per RFC 2119.
- **Requirement IDs.** `TW-n` intake and self-monitoring; `TR-n` plain-register rendering law; `TA-n` patient acts; `TC-n` custody and consent; `TL-n` low-resource floor; `TE-n` evaluation.
- **Consolidation discipline.** PF/FP/MP remain valid in their hosts; this corpus adds integration constraints and never relaxes a source MUST.
- **Regulatory precedence.** REG-POSTURE v1.0 governs. One open item shapes this face directly: ASSUME-REG-003 — whether the patient surface is a separate product, non-decision-support, or in-scope for the same submission — is a counsel question gating GATE-000. TL-5 carries the design consequence: build so any of the three answers is survivable.

## Part 1 — Foundation: the thorax of the butterfly

**The face's evidence base, in one paragraph.** Bayor et al. quantify the gap (37/40 clinician-only) and name dual-facing design the structural opening. The Blake program supplies the working patterns with unusual evaluation depth for this field: intake instruments completed at home made consultations patient-driven, and the diary's immediate day-by-day feedback drove reflection and engagement, usable across ages and computer-literacy bands in a 267-user study. Stranieri contributes the custody doctrine — the Patient Centric Agent, repository-allocation policy, patient-empowered EHR work — that makes the patient a data principal rather than a data subject. The left wing's CWW literature (hesitant term sets, ELICIT expressions, Z-numbers) exists precisely to accept hedged human speech as data; the right wing's instrument-gap finding (no OSA screen tuned to women, in the Blake program's own record) makes fit honesty a patient-safety property, sharpened by Cockburn's evidence that context transfer failure is the expected case. The regulatory posture adds two constraints: diagnostic content waits for clinician release (PF-8, REG-KEEP-003), and the face's regulatory treatment is genuinely open (ASSUME-REG-003) — a reason for clean separability, not for building less.

**What consolidation adds.** Four face-level laws emerge from reading PF, FP, and MP together. (i) *No coercion at capture:* hedges, ranges, "none of these," free text, and stated unsureness are stored as given — the intake instrument is a listening device, not a formalization funnel (TW-2, TA-3). (ii) *One truth, second register:* the patient reads the same argument objects the clinician signed, decoded to plain words — including deviations, envelopes, and how-sure-we-are — never a simplified fork (TR-1/2). (iii) *Two content classes, one bright line:* the patient's own observations reflect back immediately; anything diagnostic waits for signature (TR-3). (iv) *The patient is an auditor of their own record:* access ledger, consent controls, gap reports, and calibration profiles are patient-visible and patient-revocable — custody is a face function, not a policy document (TC family).

> The doctrine in one sentence: the face listens without coercing, reflects without diagnosing, shows the same truth in plainer words, and leaves the patient holding the keys.

## Part 2 — Intake & self-monitoring

**What the research revealed.** The Blake placement law starts here: routine history capture moved to the patient, before the encounter, validated at entry (PF-1). The left wing upgrades the instrument's ears — linguistic answers, hesitant ranges, the reliability dial (FP-1/2) — and the right wing keeps the instrument honest about itself: versioned artifacts with envelopes and representable gaps (MS-1 via PF-1), escape hatches that never punish (MP-5).

### Intake & self-monitoring requirements

### TW-1 (MUST)
**Statement:** Routine history and condition-specific capture happens on this face, before the encounter, with point-of-entry validation; instruments are versioned knowledge-plane artifacts carrying target population, validation status, and known gaps (MAK-FFC PF-1, carried, with MS-1 envelopes). Capture context (device class, assistance, modality) is recorded with every response.
**Rationale trace:** MAK-FFC PF-1 (carried); MAK-RWC MS-1; Blake 2014/2016.

### TW-2 (MUST)
**Statement:** Instruments accept the patient's actual speech as data: linguistic answers (single terms, ratified hedges, hesitant "between X and Y"), numeric entry, and free text are all first-class; hedged or hesitant answers are stored as given, never averaged or coerced to points at capture (MAK-LWC FP-1, carried); every structured item offers "none of these" and skip-with-reason (MAK-RWC MP-5, carried).
**Rationale trace:** MAK-LWC FP-1 + MAK-RWC MP-5, consolidated; HFLTS/ELICIT literature; Chapman nebulosity.

### TW-3 (MUST)
**Statement:** The reliability dial is offered, never demanded, on every self-reported ground; declining stores "unstated," and no engine or renderer treats unstated as either sure or unsure (MAK-LWC FP-2, carried). Reliability informs interpretation, never worth — no down-weighting of "guessing" patients out of their own narrative.
**Rationale trace:** MAK-LWC FP-2 + anti-requirement (carried); MAK-CEC OM-3 reliability type; MAK-MIF beat 6.

### TW-4 (MUST)
**Statement:** Self-monitoring returns immediate, legible feedback on the patient's own data — the membership-scale visual and plain trend cards where terms are graded, the diary-graph pattern everywhere else — offline-capable, rendered from the same artifacts the clinician sees (MAK-FFC PF-5 + MAK-LWC FP-4, consolidated).
**Rationale trace:** MAK-FFC PF-5 + MAK-LWC FP-4; Blake diary lesson (feedback → reflection → engagement).

### TW-5 (SHOULD)
**Statement:** Personal scale calibration (the PIS profile) is offered at onboarding and editable thereafter: patient-visible in plain language, revocable in one action, applied only to encoding this patient's inputs, never inferred from behaviour (MAK-LWC FP-3, carried in force).
**Rationale trace:** MAK-LWC FP-3/FS-9 (carried); Li 2016 PIS; Pei 2024 credibility.

## Part 3 — The plain register's rendering law

**What the research revealed.** Register fidelity is the host corpus's hardest patient-face rule: the patient sees the same argument, not a sanitized fork (PF-2). The left wing supplies the decoding mathematics (plain codebook, no belief-language for μ, words and pictures over scores); the right wing adds the honesty layers the literature never reached: envelope status in plain language ("was this tested on people like you?") and fit-uncertainty worded distinctly from degree-uncertainty.

### Rendering requirements

### TR-1 (MUST)
**Statement:** Every patient-visible recommendation renders from the same argument object the clinician signed, in the plain register — including qualifiers ("how sure we are"), envelope status (MAK-RWC MP-1), and the existence and plain-language reason of any deviation. The patient face never receives a sanitized, simplified-fork, or divergent version of the decision (MAK-FFC PF-2, carried).
**Rationale trace:** MAK-FFC PF-2/SPINE-3 + MAK-RWC MP-1, consolidated; trust and shared-decision-making evidence.

### TR-2 (MUST)
**Statement:** The plain register speaks words and pictures, never scores: gradedness renders as decoded codebook words with the scale visual (MAK-LWC FP-5, carried); belief renders as honest plain hedging; fit renders as tested-on-people-like-you language; and the prohibited-vocabulary lint (no percentages, probabilities, μ values, or composite confidence anywhere patient-visible) is a release check.
**Rationale trace:** MAK-LWC FP-5 (carried); MAK-CEC OM-3 at the plain register; A1 discipline.

### TR-3 (MUST)
**Statement:** The two content classes hold a bright line: the patient's own observations and their gradedness reflect back immediately (TW-4); diagnostic claims, risk statements, and recommendation content render only after clinician sign-off (MAK-HDC HA-1), with the releasing clinician identified (MAK-FFC PF-8 + MAK-LWC FP-7, consolidated). No preview, digest, or notification crosses the line.
**Rationale trace:** MAK-FFC PF-8 + MAK-LWC FP-7 + MAK-HDC HA-1; REG-KEEP-003; ASSUME-REG-003 prudence.

### TR-4 (MUST)
**Statement:** Fit-uncertainty and degree-uncertainty render distinctly in plain language: "we're not sure this question/advice applies to you" (fit) is worded and styled differently from "your answer is near a boundary" (degree), and the two never merge into one vague hedge (MAK-RWC MP-4, elevated).
**Rationale trace:** MAK-RWC MP-4 (elevated to MUST at the consolidated face); MS-9 routing; plain-language comprehension evidence.

### TR-5 (SHOULD)
**Statement:** The plain register's self-description is reachable: what this system is for, what it was tested on, what it is known to be bad at, and what changed recently — generated from fabric data (MAK-RWC MS-6) in plain language, never marketing prose.
**Rationale trace:** MAK-RWC MS-6; REG-KEEP-002 in the second register.

## Part 4 — Patient acts

**What the research revealed.** The right wing gave patients their first recorded acts beyond form-filling: the gap report with acknowledgment (MP-2), values as governed remodeling with the patient as party (MP-3). The custody lineage adds consent acts; the left wing adds calibration acts (FP-3). The face law: every patient act is acknowledged, attributable, revocable where it grants, and never punished.

### Patient-act requirements

### TA-1 (MUST)
**Statement:** Patients can file gap reports — "this doesn't describe me" — on every instrument item and every rendered argument, in one interaction, with optional free text; reports carry patient authorship into the fabric, feed gap analytics with demographic context under consent, and visibly acknowledge receipt and disposition (MAK-RWC MP-2, carried).
**Rationale trace:** MAK-RWC MP-2/MS-2 (carried); instrument-gap finding; procedural-justice acknowledgment.

### TA-2 (MUST)
**Statement:** Values and priorities are patient-authored structured data whose mappings to clinical weightings pass the full remodeling lifecycle with the patient as a party — see, contest, revoke at every stage (MAK-FFC PF-3 + MAK-RWC MP-3, consolidated); runtime inference of values from behaviour remains prohibited.
**Rationale trace:** MAK-FFC PF-3 + MAK-RWC MP-3/MS-4; patient-autonomy doctrine.

### TA-3 (MUST)
**Statement:** Escape-hatch content is preserved and consequential: free text, "none of these," and skip-with-reason answers are stored verbatim, rendered to the clinician in Consult-Prep, counted in circumrational telemetry, and never optimized away for completion metrics (MAK-RWC MP-5, carried; MAK-HDC HA-6 mirror).
**Rationale trace:** MAK-RWC MP-5 (carried); MAK-RWC MA-3 Goodhart guard on completion rates.

### TA-4 (SHOULD)
**Statement:** Patient-affecting remodeling — instrument changes, plain-register templates, values-mapping classes — passes a patient-council stage in deliberation: a chartered trading zone with patient representation, its review recorded in the proposal lifecycle (MAK-RWC MP-6, carried).
**Rationale trace:** MAK-RWC MP-6/MS-8 (carried); participatory-design evidence.

### TA-5 (MAY)
**Statement:** The face may support patient-initiated dispute entry (contesting a record or decision) routed to the auditor face's dispute mode (MAK-FFC AF-6), with positions entered in the plain register and the ODR workflow's state visible to the patient.
**Rationale trace:** MAK-FFC AF-6; Stranieri medical-ODR lineage; patient-empowered EHR work.

## Part 5 — Custody & consent

**What the research revealed.** Stranieri's Patient Centric Agent line is the design source: the patient as custodian, with an agent mediating access, routing, and storage — plus the open-banking analogy for data rights. The host corpus bound it to FHIR Consent and the access ledger (PF-4). Consolidation adds the meta-layer: calibration profiles, gap reports, and values are patient data under the same custody discipline.

### Custody & consent requirements

### TC-1 (MUST)
**Statement:** The Personal Data Agent gives the patient a complete access ledger — every read of their record, bound to its AuditEvent and the argument context it served — and consent controls the data plane actually enforces (MAK-FFC PF-4, carried). Consent objects are granular, revocable, and mirrored in the ledger; consent is never a wall of text.
**Rationale trace:** MAK-FFC PF-4 + anti-requirement (carried); Stranieri PCA (IEEE Access 2018); repository allocation (HIJ 2020).

### TC-2 (MUST)
**Statement:** Patient-generated meta-data is patient-custodied: PIS calibration profiles, reliability components, gap reports, and values structures are visible in the patient's data view, export with their record, and revoke where they grant (calibration and values) — with revocation effects stated in plain language before confirmation.
**Rationale trace:** MAK-LWC FP-3/FS-9 + MAK-RWC MP-2/MP-3 custody implications, consolidated *(new as custody law)*.

### TC-3 (MUST)
**Statement:** Repository routing is policy-driven and explainable in the plain register (MAK-FFC PF-4, carried): where the patient's data lives, under which jurisdiction's rules, and why — with routing decisions ledgered and the policy a versioned artifact.
**Rationale trace:** MAK-FFC PF-4 (carried); Stranieri repository-allocation policy; data-sovereignty realities in low-resource deployment.

### TC-4 (SHOULD)
**Statement:** Secondary-use consent (research, validation evidence, the GPP-13-class evidence vehicle) is separate, specific, and never bundled with care consent; declining secondary use changes nothing about care functionality, and the separation is a conformance test.
**Rationale trace:** MAK-J3 GPP-13 deployment agreements; ethics-approval realities; consent-quality doctrine *(new)*.

## Part 6 — The low-resource floor

**What the research revealed.** The north star makes this face's floor the product: Cockburn's meta-analysis finds 44% of maternity CDSS evidence is LMIC — demand is proven; the Anidra deployment shows cheap-device RPM in low-resource wards is field-real; the Blake 267-user study proves accessibility-first intake works across literacy bands; and the right wing's sharpest equity finding applies here twice over — ontology misfit concentrates where instruments were validated elsewhere, so the low-resource profile needs the meta-rational functions most, not least.

### Low-resource requirements

### TL-1 (MUST)
**Statement:** The accessibility floor is a release gate, not an aspiration (MAK-FFC PF-6, carried): usable at low literacy and low computer literacy, WCAG-conformant, functional offline with deferred sync, with stated bandwidth and device floors tested per release; SMS/IVR fallback covers intake, reminders, and escalation.
**Rationale trace:** MAK-FFC PF-6/XC-3 (carried); Blake accessibility-first evidence; Anidra field reality.

### TL-2 (MUST)
**Statement:** Linguistic intake is the low-resource primary modality: word-chips over keypads, IVR menus speaking codebook terms, codebook and instrument packs installable per jurisdiction and language under knowledge-plane lineage rules (MAK-LWC FP-6, elevated; MAK-FFC PF-7 alignment).
**Rationale trace:** MAK-LWC FP-6 (elevated to MUST at the consolidated face); WHO SMART localization; accessibility evidence.

### TL-3 (MUST)
**Statement:** Meta-rational functions hold at the floor: gap reporting, envelope rendering, escape hatches, and acknowledgment loops function offline and at the device floor (MAK-RWC MX-3, carried); low-resource gap-report streams receive the equity lens by default.
**Rationale trace:** MAK-RWC MX-3/MA-2 (carried); ontology misfit concentrates at the periphery.

### TL-4 (SHOULD)
**Statement:** Patient-face computable content aligns with WHO SMART Guidelines artifact layers so low-resource deployments adopt nationally adapted content without re-authoring (MAK-FFC PF-7, carried), including plain-codebook packs as localization artifacts.
**Rationale trace:** MAK-FFC PF-7 (carried); MAK-LWC FP-6 codebook packs; XC-4 pluralism.

### TL-5 (MUST)
**Statement:** The face is built separable pending ASSUME-REG-003: the patient surface's boundaries (its claim classes, its data flows into the decision path, its release dependencies on clinician sign-off) are documented and structurally clean, so that any counsel outcome — separate product, non-decision-support, or in-scope — is implementable without architectural surgery. The assumption is never treated as closed in design documents.
**Rationale trace:** REG-POSTURE ASSUME-REG-003 / TASK-REG-004; MAK-J3 GPP-4 patient-face narrowing as the exempt-tier precedent *(new — separability as design consequence)*.

## Part 7 — Evaluation & consolidation maps

### Evaluation requirements

### TE-1 (MUST)
**Statement:** Face evaluation runs the consolidated program with real patients across literacy bands and device classes (never proxy-only): comprehension of plain-register arguments, deviations, and envelope honesty; linguistic-equity measures (completion and comprehension, linguistic vs numeric, by literacy band — MAK-LWC FP-8, elevated); gap-report usability and acknowledgment comprehension; and calibration uptake/revocation rates — evaluators independent of the design team.
**Rationale trace:** MAK-LWC FP-8 (elevated) + MAK-FFC CF-7 independence discipline applied to this face; Blake 267-user precedent; north-star measurement.

### TE-2 (MUST)
**Statement:** Face telemetry flows under the unified schema: modality mix, escape-hatch and gap-report rates by instrument and population, reliability-dial usage, acknowledgment latencies, and floor-conformance metrics (offline sync success, IVR completion) — auditor system lens only, with the equity lens standing.
**Rationale trace:** MAK-CEC RG-5; MAK-RWC MA-2; AF-8 discipline.

### TE-3 (SHOULD)
**Statement:** Register-fidelity audits run per release: sampled argument objects rendered in both registers are compared for content parity (nothing added, removed, or reweighted — SPINE-3), with envelope and deviation honesty checked explicitly (TR-1); failures block the release.
**Rationale trace:** MAK-FFC SPINE-3/PF-2; MAK-RWC MP-1; *(new — the audit as recurring gate)*.

### TE-4 (MUST)
**Statement:** The face's conformance suite gates its releases: bright-line tests (no diagnostic content path bypasses sign-off — TR-3), coercion tests (hedged input stored as given — TW-2), custody tests (consent enforcement, revocation effects — TC-1/2), floor tests (TL-1), and plain-register lint (TR-2). Results are conformity-file artifacts.
**Rationale trace:** MAK-CEC RG-8 pattern at this face; REG-KEEP-002 *(new)*.

### Patient Face anti-requirements (consolidated)

- Never coerce a hedged, hesitant, or out-of-ontology answer into a point or a category at capture (MAK-LWC + MAK-RWC, carried).
- Never infer values, semantics, or risk tolerance from behaviour and apply them silently (all three hosts, carried).
- Never render diagnostic content before clinician sign-off, in any preview, digest, or notification (TR-3).
- Never show a patient a naked μ, percentage, score, or blended confidence (MAK-LWC, carried; OM-3 at the plain register).
- Never use the reliability dial punitively (MAK-LWC, carried).
- Never let a patient gap report vanish — unacknowledged, unrouted, or silently closed (MAK-RWC, carried).
- Never gate core function on connectivity, device class, or app-store availability in low-resource profiles (MAK-FFC, carried).
- Never bundle secondary-use consent with care consent (TC-4).

### Three-corpus consolidation map (complete for the patient face)

| Source requirement | Disposition here | Carrier |
|---|---|---|
| MAK-FFC PF-1 (capture before encounter; versioned instruments) | carried | TW-1 |
| MAK-FFC PF-2 (register fidelity) | consolidated | TR-1 |
| MAK-FFC PF-3 (values as ratified mappings) | consolidated | TA-2 |
| MAK-FFC PF-4 (Personal Data Agent) | carried + extended | TC-1, TC-3 |
| MAK-FFC PF-5 (immediate visual feedback) | consolidated | TW-4 |
| MAK-FFC PF-6 (accessibility floor as gate) | carried | TL-1 |
| MAK-FFC PF-7 (WHO SMART alignment) | carried | TL-4 |
| MAK-FFC PF-8 (no patient-facing diagnosis pre-release) | consolidated | TR-3 |
| MAK-LWC FP-1 (linguistic intake first-class) | consolidated | TW-2 |
| MAK-LWC FP-2 (reliability dial) | carried | TW-3 |
| MAK-LWC FP-3 (PIS calibration, patient-owned) | carried + custody extension | TW-5, TC-2 |
| MAK-LWC FP-4 (membership scale visual) | consolidated | TW-4 |
| MAK-LWC FP-5 (words and pictures, never scores) | carried | TR-2 |
| MAK-LWC FP-6 (linguistic as low-resource primary) | elevated (SHOULD→MUST) | TL-2 |
| MAK-LWC FP-7 (fuzzy renderings inside release discipline) | consolidated | TR-3 |
| MAK-LWC FP-8 (linguistic-equity evaluation) | elevated (SHOULD→MUST) | TE-1 |
| MAK-RWC MP-1 (envelope honesty in plain register) | consolidated | TR-1 |
| MAK-RWC MP-2 (patient gap reports) | carried | TA-1 |
| MAK-RWC MP-3 (values as remodeling) | consolidated | TA-2 |
| MAK-RWC MP-4 (fit vs degree wording) | elevated (SHOULD→MUST) | TR-4 |
| MAK-RWC MP-5 (no coercive formalization) | carried | TW-2, TA-3 |
| MAK-RWC MP-6 (patient council) | carried | TA-4 |

### MAK-MIF beat map (face landings)

| Beat | Face landing | Carrier |
|---|---|---|
| 2 · The full translation loop | Intake encodes without coercion; feedback decodes to owned words; what encoding lost is preserved | TW-2/4, TA-3 |
| 6 · Reliability-aware listening | The dial writes (restriction, reliability); unstated stays unstated; honesty never punished | TW-3 |

### Findings → requirements

| Finding | Source | Requirements it drives |
|---|---|---|
| 37/40 systems clinician-only; dual-facing is the structural opening | Bayor 2025 | the corpus's existence; TE-1 |
| Home intake makes consultations patient-driven; diary feedback drives reflection; accessibility-first works across literacy (n=267) | Blake 2014/2016 | TW-1/4, TL-1 |
| Patients speak in hedges, ranges, and stated unsureness; CWW accepts it as data | HFLTS/ELICIT/Z-number literature via MAK-LWC | TW-2/3 |
| Instruments carry population gaps; misfit concentrates where validation didn't happen | Blake 2014 gap; Cockburn 2024; MAK-RWC equity lens | TA-1, TL-3, TR-4 |
| The patient as data principal: custody, routing, patient-empowered records | Stranieri PCA/HIJ/EHR lineage | TC-1..3 |
| Register fidelity is the trust mechanism; sanitized forks corrode it | MAK-FFC PF-2 doctrine; shared-decision-making literature | TR-1, TE-3 |
| Diagnostic content requires human sign-off, fail-closed | REG-KEEP-003; MAK-FFC PF-8 | TR-3 |
| Patient-surface regulatory treatment is an open counsel question | REG-POSTURE ASSUME-REG-003 / TASK-REG-004 | TL-5 |
| LMIC demand is proven (44% of maternity CDSS evidence) | Cockburn 2024 | TL-1..4 |

### Sources

- Series: MAK-FFC v1.1 Part 4 · MAK-LWC v1.1 Part 4 · MAK-RWC v1.1 Part 4 · MAK-CEC v1.1 · MAK-HDC v1.0 (sign-off act) · MAK-MIF v1.0 · REG-POSTURE v1.0 (ASSUME-REG-003, REG-KEEP-003; cited by stable ID).
- Blake & Kerr 2010/2014; Blake, Kerr & Gammack 2016 — the intake, diary, and 267-user usability evidence.
- Bayor et al. 2025 (JMIR); Cockburn et al. 2024 (eClinicalMedicine); Abbas et al. 2025 (Healthcare).
- Stranieri corpus: Patient Centric Agent (IEEE Access 2018); repository allocation (HIJ 2020); patient-empowered EHR (2019); medical ODR (2020) — provenance in The Stranieri File.
- CWW/Z-number literature via MAK-LWC Part 8 sources (Zadeh, Mendel, Herrera lineages; Li 2016; Pei 2024).
- WHO SMART Guidelines program; Anidra RPM deployment corpus (via the series' earlier volumes).

*Document footer (source artifact):* The Thorax Corpus v1.0 · requirement IDs are stable; propose changes as argued deviations — this document practices its own doctrine. Compiled from the three host corpora, MAK-CEC and MAK-HDC, REG-POSTURE v1.0, and the series' verified evidence base, 1 Sep 2026.

## Part 8 — Execution sourcing annex

The patient face's delivery substrate is the best-sourced surface in the whole series — the low-resource intake stack is maintained, deployed open source — while its distinctive components (custody agent, plain-register decoder, gap machinery) remain builds. Entries verified by direct fetch on the dates shown; carried entries cite their host annexes.

### Verified entries (this face's pass)

| ID | Repo / artifact | What it gives you | Status | Verdict | Serves |
|---|---|---|---|---|---|
| ELSM-T01 | [google/android-fhir](https://github.com/google/android-fhir) — Structured Data Capture library | FHIR SDC questionnaire rendering, skip logic, validation, offline-first — TW-1's intake engine on-device | carried (ELSM-04, active; re-verify per rule) | ADOPT | TW-1, TL-1 |
| ELSM-T02 | [opensrp/fhircore](https://github.com/opensrp/fhircore) | Deployed WHO-SMART-on-Android for community health — the TL profile as a maintained product; its device-integration features excluded per tier rules | carried (ELSM-05, active v2.2.2 2025-11, re-verified 2026-09-01) | ADOPT / STUDY | TL-1..4 |
| ELSM-T03 | [fastenhealth/fasten-onprem](https://github.com/fastenhealth/fasten-onprem) | Nearest built thing to the Personal Data Agent — self-hosted PHR aggregating provider FHIR | carried (ELSM-21, ARCHIVED 2026-07) | STUDY (cautionary) | TC-1 |
| ELSM-T04 | WHO SMART Guidelines IGs + national adaptation layers | Localized computable content and the adaptation model TL-4 rides | carried (ELSM-06, active program) | ADOPT | TL-2/4 |

### The face's build list (no precedent found; methodology hedge carried)

The Personal Data Agent as a face function (access ledger + enforcing consent + explainable routing — the fasten-onprem archive left the space without a maintained champion, per MAK-ELSM's landmine); the plain-register decoder path (CWW decode with similarity floor — MAK-LWC's confirmed no-precedent core); the patient gap reporter with acknowledgment loop; the reliability dial writing Z-grounds; the bright-line release discipline as tested structure (TR-3); PIS calibration with custody semantics (TC-2). The intake shell is buyable; the listening discipline is not.

### Face-relevant research plane (carried)

The linguistic-equity hypothesis (TL-2/TE-1) remains unmeasured in CDSS settings — MAK-LWC's open agenda item, now a pre-registration duty in the low-resource pilot; patient-facing explanation comprehension has no analogue of the Spitzer RCT — TE-1 produces first evidence; custody and consent UX for granular FHIR Consent remains a design-research gap flagged since the host corpus.

## Appendix A — ID census (additive)

Authoritative enumeration for validator checks. Count: **28**.

```json
{
  "doc_id": "MAK-TXC",
  "version": "1.0",
  "requirements": {
    "TW": ["TW-1","TW-2","TW-3","TW-4","TW-5"],
    "TR": ["TR-1","TR-2","TR-3","TR-4","TR-5"],
    "TA": ["TA-1","TA-2","TA-3","TA-4","TA-5"],
    "TC": ["TC-1","TC-2","TC-3","TC-4"],
    "TL": ["TL-1","TL-2","TL-3","TL-4","TL-5"],
    "TE": ["TE-1","TE-2","TE-3","TE-4"]
  },
  "levels": {
    "MUST":   ["TW-1","TW-2","TW-3","TW-4","TR-1","TR-2","TR-3","TR-4","TA-1","TA-2","TA-3","TC-1","TC-2","TC-3","TL-1","TL-2","TL-3","TL-5","TE-1","TE-2","TE-4"],
    "SHOULD": ["TW-5","TR-5","TA-4","TC-4","TL-4","TE-3"],
    "MAY":    ["TA-5"]
  },
  "retired": []
}
```

Census arithmetic: 21 MUST + 6 SHOULD + 1 MAY = 28 (5+5+5+4+5+4 across the six families).

## Appendix B — Self-audit checks (additive)

1. **ID uniqueness** — no requirement ID appears in more than one requirement header.
2. **ID census parity** — headers matching `^### (TW|TR|TA|TC|TL|TE)-\d+ \((MUST|SHOULD|MAY)\)$` exactly equal Appendix A's enumeration.
3. **Level parity** — header levels match Appendix A buckets.
4. **Trace presence** — every requirement block has a non-empty rationale trace.
5. **Normative leakage** — no capitalized MUST/SHOULD/MAY outside requirement blocks, anti-requirement bullets, quoted text, or this appendix.
6. **Consolidation integrity** — every PF/FP/MP requirement appears in the Part 7 map with a disposition; no source requirement relaxed (elevation permitted and named).
7. **Cross-reference integrity** — every TW/TR/TA/TC/TL/TE ID cited exists in the census; every host-document ID cited resolves in its host.
8. **Regulatory precedence** — ASSUME-REG-003 never described as closed; REG-KEEP-003 honoured; no REG-FIND contradicted.
9. **Table integrity** — consistent column counts per row.
10. **Stability** — IDs from previous versions present or explicitly retired; never reused.
