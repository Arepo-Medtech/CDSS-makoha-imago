---
doc_id: MAK-CEC
title: "The Compound Eyes Corpus"
version: "1.1"
date: "2026-09-01"
series: "Mākoha research series — volume 9 · the engine plane, consolidated from both wings"
status: normative-draft
normative_language: RFC-2119 (MUST / SHOULD / MAY)
req_prefixes: [OM, CP, DX, QU, AD, RG]
req_count: 38
subordinate_to: "MAK-FFC v1.1 — no requirement here relaxes a corpus MUST; consolidations state their sources"
builds_from:
  - "MAK-RWC v1.1 (The Right Wing Corpus) — meta-rational engine machinery: envelopes, fit enforcement, boundary hunting, remodeling replay (ME-1..8, MS-1/9)"
  - "MAK-LWC v1.1 (The Left Wing Corpus) — fuzzy engine machinery: fuzzification service, method metadata, coupling law, boundary sweeps (FE-1..9, FS-3/8)"
  - "MAK-FFC v1.1 Part 6 — the host engine plane (EN-1..9) and the Toulmin output contract"
governed_by:
  - "REG-POSTURE v1.0 — assume-inclusion posture; FORK-REG-001 tier labels; REG-KEEP-001 deterministic release; stack bindings (Baseten, Ketryx)"
changelog:
  - "v1.1 (2026-09-01): additive — Part 9 refresh pass: four engine-plane entries verified 2026-09-01 (ELSM-E01..E04: pgmpy, PyMC, crepes, netcal), differential/qualifier sourcing notes, Appendix C register, self-audit check 11. No v1.0 content altered or removed."
  - "v1.0 (2026-09-01): initial release — 38 requirements across OM/CP/DX/QU/AD/RG; three-corpus consolidation map (Part 8); engine-plane sourcing annex (Part 9)."
companions:
  - "MAK-FFC v1.1 (host; SPINE/CF/PF/AF/EN/XC/GPP IDs resolve there)"
  - "MAK-RWC v1.1 (right wing; MS/MC/MP/MA/ME/MX IDs resolve there)"
  - "MAK-LWC v1.1 (left wing; FS/FC/FP/FA/FE/FX IDs resolve there)"
  - "MAK-MIF v1.0 (the eight beats; the engine plane is where the wings' beats mechanically couple)"
  - "MAK-ELSM v1.1 (sourcing vocabulary and carried entries)"
  - "REG-POSTURE v1.0 (governing regulatory document)"
artifact_url: "https://claude.ai/code/artifact/33b64712-546c-49f1-b281-fa02cab058cb"
change_policy: "Requirement IDs are stable; retired IDs never reused. Propose changes as argued deviations."
---

<!-- LLM USAGE CONTRACT (additive; not part of the source document)
1. Requirement blocks (### OM-n / CP-n / DX-n / QU-n / AD-n / RG-n) are NORMATIVE;
   all other prose is INFORMATIVE. Part 9 is an informative sourcing annex.
2. This corpus CONSOLIDATES engine-plane requirements from MAK-FFC (EN), MAK-LWC (FE),
   and MAK-RWC (ME). Consolidation never retires a source requirement: EN/FE/ME IDs
   remain valid in their host documents, and the Part 8 map records which corpus
   requirement each consolidation carries. Where texts appear to differ, the host
   document's requirement governs and the difference is a validator error here.
3. The five-signal registry (OM-3) binds generation: posterior, conformal coverage,
   membership degree, reliability, and fit status are distinct types — never merge,
   relabel, or render any of them as generic "confidence."
4. The single release gate (RG-1) binds generation: never design, describe, or code
   a path by which engine output reaches a face except through the deterministic
   evaluator's pipeline.
5. MUST violations in generated designs/code/documents require an explicit DEVIATION
   notice naming the ID.
6. Appendix A's ID census is authoritative for validator checks; Appendix B's
   self-audit checks gate any edit of this file.
7. Part 9 statuses are dated observations; re-verify before dependency decisions.
END LLM USAGE CONTRACT -->

# The Compound Eyes Corpus

A translatable research primer and execution manual for the engine plane of the triple-facing CDSS — the ommatidial decomposition discipline, the compiler, the Bayesian differential, the qualifier machinery, the standing adversary, and the single release gate — consolidating the engine requirements of both wings and the host corpus into one buildable plane.

**Document metadata:** Technical corpus · v1.1 · 1 Sep 2026 · ninth volume in the Mākoha research series · STATUS: normative draft · REQ IDS: OM · CP · DX · QU · AD · RG · SUBORDINATE TO: MAK-FFC v1.1 · BUILDS FROM: MAK-RWC v1.1 + MAK-LWC v1.1 · GOVERNED BY: REG-POSTURE v1.0.

## Contents

1. [Part 0 — How to use this document](#part-0--how-to-use-this-document)
2. [Part 1 — Foundation: the compound eye](#part-1--foundation-the-compound-eye)
3. [Part 2 — The ommatidial discipline](#part-2--the-ommatidial-discipline)
4. [Part 3 — The compiler plane](#part-3--the-compiler-plane)
5. [Part 4 — The differential and inference plane](#part-4--the-differential-and-inference-plane)
6. [Part 5 — The qualifier machinery](#part-5--the-qualifier-machinery)
7. [Part 6 — The standing adversary](#part-6--the-standing-adversary)
8. [Part 7 — The release gate, firewall, lifecycle, and tiers](#part-7--the-release-gate-firewall-lifecycle-and-tiers)
9. [Part 8 — Consolidation maps & traceability](#part-8--consolidation-maps--traceability)
10. [Part 9 — Execution sourcing annex](#part-9--execution-sourcing-annex)
11. [Appendix A — ID census](#appendix-a--id-census-additive)
12. [Appendix B — Self-audit checks](#appendix-b--self-audit-checks-additive)

## Thesis

> A compound eye is not one big eye that sees poorly; it is thousands of small eyes — ommatidia — each with its own lens and its own narrow receptive field, integrated into a single mosaic image by structures the ommatidia do not contain, and unmatched at exactly one thing: detecting change. The Mākoha engine plane is built the same way, and the series' three corpora each specified a facet of it: the host corpus gave the plane its output contract (every engine emits argument fragments, never released claims) and its decomposition law (criterion-grain micro-engines, from Blake's twenty-eight decision points); the left wing gave it a semantics of degree (fuzzification as a pure service, method choice as template metadata, thresholds owned by the evaluator); the right wing gave it a judgment of systems (envelopes checked at release, an adversary that hunts the ontology's edges, replay that gates remodeling). What no single corpus states is the plane law that makes them one machine: five signal types that never merge, one compiler that is the only way clinical logic enters, one adversary with three target maps, one release gate with a fixed pipeline, and one lifecycle replay across every class of change. This corpus states it — the mosaic integration the ommatidia cannot do for themselves.

## Part 0 — How to use this document

This corpus is the engine plane's single execution manual. It consolidates rather than invents: most requirements below carry one or more source requirements from MAK-FFC (EN), MAK-LWC (FE), or MAK-RWC (ME/MS), named in the statement or trace; the Part 8 map is the complete cross-walk. What is genuinely new is marked *(new)* in the trace — chiefly the plane-law requirements: the five-signal registry, the unified release-gate pipeline, the unified adversary program, the campaign-coverage duty, subgroup-stratified conformal coverage, and the unified telemetry schema.

- **Normative language.** MUST / SHOULD / MAY per RFC 2119, as across the series.
- **Requirement IDs.** `OM-n` ommatidial discipline; `CP-n` compiler plane; `DX-n` differential and inference; `QU-n` qualifier machinery; `AD-n` adversary; `RG-n` release gate, firewall, lifecycle, tiers.
- **Consolidation discipline.** Source requirements (EN/FE/ME) remain valid in their host documents; this corpus adds the integration constraints and never relaxes a source MUST. A conformant engine plane satisfies its host-corpus requirements *and* this corpus's plane law.
- **Regulatory precedence.** REG-POSTURE v1.0 governs; tier language follows FORK-REG-001 (J-1 lower-class included, J-2 higher-class included, J-3 exempt reserve), and MAK-RWC Part 7's update notes are carried, not restated.

## Part 1 — Foundation: the compound eye

Three engineering lineages meet in this plane, and the metaphor is doing real work in each.

**Decomposition is the proven survival trait.** The Blake artefact's twenty-eight small, testable, per-criterion decision units were the property its authors singled out as making the system "flexible and easy to change in the event of additions to or changes in the diagnostic criteria" — and the counterfactual is documented in the same lineage: the ICSD-2 freeze stranded the system when its knowledge was too entangled to re-version. An ommatidium is small enough to validate exhaustively, version independently, and replace without touching its neighbours. Monolithic inference is where guideline drift goes to hide; MAK-FFC made the grain a requirement (EN-2), and this corpus makes it the plane's organizing principle.

**Integration lives outside the units.** No ommatidium sees the image. In the engine plane, no micro-engine sees the patient: each evaluates its criterion cluster and emits an argument fragment; the mosaic — the ranked differential with its qualifiers, rebuttals, and envelopes — is assembled by the fabric and released (or held, or flagged) by the deterministic evaluator alone. This is why the plane can host heterogeneous machinery — CQL rule evaluation, Bayesian networks, fuzzy inference, conformal wrappers — behind one contract (EN-1): the integration layer, not the engines, owns coherence.

**Compound eyes are motion detectors.** The biological design trades acuity for change-sensitivity — flicker-fusion rates far beyond camera eyes. The engine plane inherits the duty: drift telemetry (curve drift from the left wing, envelope pressure and gap analytics from the right, calibration drift from the qualifier machinery), sentinel replay on every change class, and a standing adversary sweeping the boundaries. The plane is instrumented to notice the world moving before the faces feel it.

**What consolidation adds.** Reading EN, FE, and ME side by side exposes five places where the corpora each hold a piece of one mechanism: (i) *signal typing* — FS-3 forbids fuzzy/probability conflation, MS-9 forbids degree/fit conflation; the plane needs the full registry stated once (OM-3). (ii) *The release gate* — SPINE-7's evaluator, FS-8's thresholds, ME-1's envelope check, and SPINE-6's conflict materialization are one pipeline, and its stage order matters (RG-1). (iii) *The adversary* — EN-5's corruption engine, FE-8's boundary sweeps, ME-2's envelope hunting, and AF-4's theater detection are one program with three target maps (AD-1). (iv) *Proposal pipelines* — EN-6's LLM classes, FE-4's curve learning, and ME-4's gap mining are one offline architecture with one ratification interface (CP-5). (v) *Lifecycle replay* — EN-8's sentinel practice, ME-5's remodeling replay, and the left wing's curve-change replay are one harness parameterized by change class (RG-4).

> The doctrine in one sentence: many small eyes, one mosaic, one gate — and the plane, not the engines, owns the image.

## Part 2 — The ommatidial discipline

### The unified engine contract

```text
// Consolidates MAK-FFC EN-1, MAK-LWC's fuzzification/annotation contract,
// and MAK-RWC's fit-enforcement contract into the plane contract.
interface Ommatidium {
  binding: CriterionRef            // exactly which GenericArgument node(s), pinned
  inputs:  Grounds[]               // FHIR-sourced, provenance-bearing,
                                   // graded annotations attached (FE-1), reliability preserved (FS-6)
  context: GenericArgument         // template at pinned version, with method metadata (FE-2),
                                   // thresholds (FS-8), envelope + commitments (MS-1/ME-3)
  propose(): ActualArgumentDraft {
    claim:     Assertion           // candidate only — never released content
    grounds:   Grounds[]           // what it actually used, with encoding traces
    warrant:   WarrantRef          // versioned; type per tier rules (RG-6)
    backing:   EvidenceTierRef
    qualifier: TypedSignals        // per the five-signal registry (OM-3)
    rebuttals: Defeater[]          // applicable confirmed adversary findings (AD-2)
    fit:       FitReport           // envelope status + typed fit-signals (ME-1/ME-7)
    pins:      VersionSet          // model, config hash, terminology, template, codebook, MF versions
  }
}
// Purity: propose() is a pure function of (inputs, context, pins) — no state, no learning,
// no side channels (OM-4). Release is not an engine capability (OM-5, RG-1).
```

### The five-signal registry

| Signal | Type semantics | Owner mathematics | Source law |
|---|---|---|---|
| Posterior | Degree of belief in a claim | Probability (Bayesian differential) | MAK-FFC EN-1, SPINE-2 |
| Coverage | Calibrated uncertainty of a claim set | Conformal prediction (sets + stated coverage) | MAK-FFC EN-4 |
| Membership (μ) | Degree of meaning-fit of a ground or warrant applicability | Fuzzy sets on ratified LinguisticVariables | MAK-LWC FS-3, FE-3 |
| Reliability | Stated confidence of a source in its own report | Z-number reliability component, passthrough | MAK-LWC FS-6 |
| Fit | Ontology/envelope match of case to formal element | Envelope check + OOD/atypicality evidence | MAK-RWC MS-1/MS-9, ME-7 |

### Ommatidial requirements

### OM-1 (MUST)
**Statement:** Inference decomposes to criterion granularity: one ommatidium per guideline criterion or declared criterion cluster, independently versioned, exhaustively testable, and swappable without recompiling unaffected nodes. Monolithic engines spanning a guideline are prohibited; a declared cluster names its criteria and justifies its cohesion in the template.
**Rationale trace:** MAK-FFC EN-2 (carried); Blake 28 decision points; ICSD-2 anti-pattern; CP-3 recompilation grain.

### OM-2 (MUST)
**Statement:** Every ommatidium — rule-based, Bayesian, fuzzy, ML, or hybrid — implements the unified engine contract above: pinned criterion binding, versioned graded grounds in, ActualArgumentDrafts out with all six Toulmin elements, typed signals, fit report, and full pins. Contract conformance is verified per engine version by the RG-8 suite.
**Rationale trace:** MAK-FFC EN-1 + MAK-LWC fuzzification contract + MAK-RWC fit contract, consolidated *(new as one contract)*.

### OM-3 (MUST)
**Statement:** The five-signal registry is plane law: posterior, coverage, membership, reliability, and fit are distinct, non-coercible types from schema through transport to render. No engine, schema, aggregation, or renderer converts one into another, sums across them, or presents any of them as generic "confidence." Cross-signal use happens only through template-declared, ratified mappings (e.g. the DX-4 coupling law), each leaving an evaluation trace.
**Rationale trace:** MAK-LWC FS-3 + MAK-RWC MS-9, unified and extended to all five types *(new as plane law)*; semantic-soup risk (MAK-LWC risk register).

### OM-4 (MUST)
**Statement:** Ommatidia are stateless pure functions of inputs, context, and pins: identical calls yield identical drafts, bit-for-bit, at any later date. Anything stateful — learning, adaptation, personalization calibration — lives in offline proposal pipelines (CP-5) and reaches runtime only as newly ratified, pinned versions.
**Rationale trace:** MAK-LWC FE-1 purity generalized to every engine class; SPINE-5 replayability; REG-KEEP-001.

### OM-5 (MUST)
**Statement:** No engine has a path to a face: drafts are the plane's only output, the deterministic evaluator's pipeline (RG-1) is the only consumer of drafts, and no engine holds render, notification, or write-to-face capability in any build. This restates SPINE-7 and MAK-LWC FE-3 as a structural property verified by negative tests (RG-8).
**Rationale trace:** MAK-FFC SPINE-7; MAK-LWC FE-3; MAK-RWC ME-1 flagged-path discipline.

### OM-6 (SHOULD)
**Statement:** Every ommatidium publishes machine-readable metadata — criterion binding, method family, signal types emitted, envelope, current version and pins, campaign-coverage status (AD-5) — queryable as engine-plane self-description feeding MAK-RWC MS-6.
**Rationale trace:** MAK-RWC MS-6; MAK-LWC FE-2 method metadata; operability of the mosaic.

### OM-7 (MAY)
**Statement:** Ommatidia may be implemented in heterogeneous runtimes and languages (JVM CQL evaluation, Python inference services, native fuzzy runtimes) provided each passes the same contract-conformance and purity suites; the plane's coherence lives in the contract, not in implementation homogeneity.
**Rationale trace:** MAK-FFC Miah 2020 reasoning-agnostic lineage; Part 9 polyglot reality (CQL/Kotlin/Java + Python stacks).

## Part 3 — The compiler plane

**What the research revealed.** The compiler is the plane's only door, and three corpora each put a lock on it: the host corpus made it the sole path for clinical logic (EN-3) so that the auditor's feedback loop has one change surface; the left wing made method choice and thresholds template metadata (FE-2, FS-8) so semantics live in ratified artifacts rather than code; the right wing made it record what the ontology excludes (ME-3) so envelopes are compiled, not curated after the fact. The sourcing record's strongest finding holds: the execution machinery below the compiler is production-grade open source (the CQL stack, clinical-reasoning, WHO SMART content), and the lift Mākoha builds is the argument annotation — templates, evidence tiers, envelopes, method metadata — on top of artifacts the ecosystem already ships.

### Compiler requirements

### CP-1 (MUST)
**Statement:** One compilation path carries all clinical logic: narrative guideline → computable form (CQL / PlanDefinition / WHO SMART machine-readable layer) → GenericArgument templates bearing, per warrant node: evidence-tier backing, inference-method metadata (MAK-LWC FE-2), ratified thresholds (FS-8), and the applicability envelope with stated exclusions (MS-1, ME-3). Hand-coded runtime rules outside this path are prohibited in every tier.
**Rationale trace:** MAK-FFC EN-3 + MAK-LWC FE-2/FS-8 + MAK-RWC ME-3, consolidated; WHO SMART layering; AF-5's single change surface.

### CP-2 (MUST)
**Statement:** Compiled artifacts pin everything they depend on: guideline version and lineage, terminology release, evidence-library snapshot, codebook and LinguisticVariable versions (FML artifacts), envelope version, and compiler version. A template with an unresolved pin does not enter the knowledge plane.
**Rationale trace:** SPINE-5; MAK-LWC FX-1 serialization discipline; RG-4 replay dependency.

### CP-3 (MUST)
**Statement:** Recompilation granularity matches the ommatidial grain: a guideline or ontology change recompiles exactly the affected warrant nodes and their bound engines, producing a diff and an impact preview (affected sentinel decisions, per RG-4) that enters the change's ratification record (MS-4). Whole-plane recompiles for local changes indicate a grain violation.
**Rationale trace:** MAK-FFC EN-2; MAK-RWC MS-4/ME-5; MAK-LWC curve-change impact-preview pattern (FA-5).

### CP-4 (MUST)
**Statement:** Plural lineages co-reside without merging: jurisdictional adaptations and localizations (WHO SMART national layers; MAK-FFC XC-4) compile as sibling lineages with their own ratification trails; the compiler never synthesizes a hybrid template from conflicting lineages, and cross-lineage conflicts surface per SPINE-6/MS-5 at runtime.
**Rationale trace:** MAK-FFC SPINE-6/XC-4; MAK-RWC MS-5; Stranieri coalescing-systems caution.

### CP-5 (SHOULD)
**Statement:** All learning and LLM assistance converges on one offline proposal pipeline with one ratification interface: guideline mining into draft argument structures (the ArgTumour pattern), curve learning and fuzzy-predicate extraction (MAK-LWC FE-4), gap mining from free text and gap reports (MAK-RWC ME-4), and instrument drafting — each emitting draft artifacts with training/extraction provenance into the same MS-4-governed review queue. Proposal pipelines have no write path to the knowledge plane and no runtime presence in any supplied artifact.
**Rationale trace:** MAK-FFC EN-6 Classes 1–3 + MAK-LWC FE-4 + MAK-RWC ME-4, consolidated *(new as one pipeline)*; MAK-MIF beat 8.

### CP-6 (MUST)
**Statement:** Compiler output validation is a gate: every compiled template passes schema checks — six Toulmin elements representable, method metadata present, thresholds ratified, envelope and commitments present, pins resolved, tier markings valid (RG-6) — before entering the knowledge plane; failures are compiler errors, never runtime discoveries.
**Rationale trace:** CP-1/CP-2 verifiability; MAK-J3 GPP-9 schema-enforcement pattern generalized *(new)*.

## Part 4 — The differential and inference plane

**What the research revealed.** The Bayesian differential is the one engine no corpus had yet specified in execution detail, and the sourcing record explains why: there is no adoptable open-source differential-diagnosis engine — the commercial ones are closed, Babylon's public counterfactual code is patent-encumbered study material, and the primitives (pgmpy-class PGM stacks) are mature but unassembled. The design constraints, however, are fully determined by the series: likelihood structures are warrants and posteriors are qualifier inputs (the Toulmin mapping), decomposition follows the ommatidial grain, fuzzy coupling follows the left wing's one-directional law, envelope and calibration discipline follow the right wing, and abstention — the engine declining to rank when grounds are insufficient — is not a failure mode but the Maturity Level 3 evidence stream that FORK-REG-001's decision point consumes.

### Differential and inference requirements

### DX-1 (MUST)
**Statement:** The Bayesian differential service decomposes per criterion cluster (OM-1): likelihood structures are versioned warrant content with evidence-tier backing; posteriors emit only as qualifier inputs on drafts (never as released scores); and the ranked differential a clinician sees is the evaluator-released mosaic, not a single engine's output.
**Rationale trace:** MAK-FFC EN-1/Part 6 Toulmin mapping; SPINE-1/7; OM-1/OM-5.

### DX-2 (MUST)
**Statement:** Model structure is ratified knowledge-plane content: network topology, independence and noisy-OR assumptions, and prior provenance are versioned artifacts with envelopes (MS-1), entering through the compiler path (CP-1) and changing only through MS-4. Runtime structure learning is prohibited; offline structure learning is a CP-5 proposal pipeline.
**Rationale trace:** SPINE-5; MAK-RWC MS-4; OM-4 purity; *(new — structure as ratified content)*.

### DX-3 (MUST)
**Statement:** Every parameter carries backing: priors and likelihoods cite tiered evidence-library entries (source, tier, currency) per parameter or declared parameter family; a parameter without backing fails compilation (CP-6). Elicited parameters record their elicitation provenance and are flagged as such in the argument's backing.
**Rationale trace:** MAK-FFC tiered evidence library doctrine; Toulmin backing slot; CP-6 *(new — per-parameter grain)*.

### DX-4 (MUST)
**Statement:** Fuzzy-probabilistic coupling follows the left wing's law, carried as plane law: graded grounds may inform likelihood inputs only under template-declared mappings; a ground's gradedness and its crisp value never both enter one likelihood as if independent; no posterior feeds back into a μ; and every coupling application leaves an evaluation trace (OM-3).
**Rationale trace:** MAK-LWC FE-5 (carried verbatim in force); OM-3 registry.

### DX-5 (MUST)
**Statement:** Calibration is a release property: each differential version's posteriors are calibration-tested on the firewalled corpus (reliability curves, subgroup-resolved where the corpus supports it) before release, with ratified acceptance bounds; post-release calibration drift beyond bounds is a blocking finding routed per AD-3. A posterior whose version lacks current calibration evidence does not satisfy SPINE-2's qualifier mandate.
**Rationale trace:** MAK-FFC EN-4/EN-7; MAK-RWC ME-6; *(new — calibration as explicit release bar)*.

### DX-6 (SHOULD)
**Statement:** Abstention is a first-class output: the differential emits "insufficient grounds to rank" with the missing-grounds list (rendering as gather-more-information recommendations) rather than forcing a ranking from weak evidence. Abstention rates and their contexts are telemetry (RG-5) and constitute the Maturity Level 3 abstention evidence that FORK-REG-001's decision point consumes.
**Rationale trace:** REG-POSTURE FORK-REG-001 (decision on Level 3 abstention evidence); TGA recommendation definition ("gather more information" is within scope); honest-uncertainty doctrine.

### DX-7 (MUST)
**Statement:** LLM runtime inference stays outside the differential: no LLM participates in posterior computation, ranking, or release in any tier. LLM assistance is CP-5 authoring-time work; any future Class 4+ runtime ambition is a J-2 (higher-class included) matter under MAK-FFC EN-6 and the conformal-LLM literature's maturity, and in every case remains subject to OM-5/RG-1.
**Rationale trace:** MAK-FFC EN-6; FORK-REG-001; mARC-QA overconfidence evidence; MAK-MIF beat 8.

## Part 5 — The qualifier machinery

**What the research revealed.** The qualifier is where the series' honesty doctrine becomes mathematics, and the 2025–26 literature moved fast in exactly the needed directions: conformal prediction is commodity tooling (MAPIE-class, active into 2026); group-conditional (Mondrian) variants demonstrably narrow subgroup coverage gaps under real distribution shift; selective-prediction-with-deferral pipelines show that the safe action on low-confidence cases is a governed handoff to humans — which is precisely the flagged path the right wing specified; and anytime-valid monitoring theory (conformal test martingales and successors) supplies false-alarm-controlled machinery for watching coverage hold in deployment. The plane's consolidation duty: the same conformal machinery serves two masters — the Qualifier slot (calibrated uncertainty) and the fit-signal stream (nonconformity extremes as ontology-misfit evidence) — and OM-3 keeps the two readings typed apart.

### Qualifier requirements

### QU-1 (MUST)
**Statement:** Every probabilistic claim carries a conformal qualifier — prediction set and stated coverage — computed by a wrapper validated on the firewalled corpus per version (MAK-FFC EN-4, carried). A posterior without coverage semantics does not satisfy SPINE-2.
**Rationale trace:** MAK-FFC EN-4 (carried); Abbas 2025 fidelity gap.

### QU-2 (MUST)
**Statement:** Conformal double duty is typed: nonconformity extremes, unusually large prediction sets, and OOD-detector findings route as *fit* signals (OM-3, MAK-RWC ME-7) — rendered as possible ontology misfit and aggregated into remodeling detection — and never as mere low confidence. The same computation may feed both the qualifier and the fit report; the two readings never share a type or a rendering.
**Rationale trace:** MAK-RWC ME-7/MS-9 (carried); OM-3 *(new — the double-duty rule stated for the plane)*.

### QU-3 (MUST)
**Statement:** Coverage is measured per ratified subgroup: conformal coverage is validated and monitored group-conditionally (Mondrian or equivalent) over the subgroup schema the governance process ratifies (demographics, site class, deployment profile at minimum); coverage gaps across subgroups are equity findings routed to MAK-RWC MA-2 and block release when they exceed ratified bounds.
**Rationale trace:** Kwon 2026 (Mondrian gender-stratified coverage under shift, Part 9); MAK-RWC MA-2; Cockburn heterogeneity *(new)*.

### QU-4 (SHOULD)
**Statement:** Selective prediction with cost-aware deferral is the preferred action policy on low-confidence and out-of-envelope cases: the pipeline defers to human judgment (the RG-1 flagged path) under an explicit, ratified clinical-cost model, rather than suppressing or force-ranking. Deferral thresholds are template metadata, ratified and versioned.
**Rationale trace:** conformal selective-prediction literature (Part 9); MAK-RWC ME-1 flagged path; REG-KEEP-003 human sign-off.

### QU-5 (MUST)
**Statement:** Qualifier telemetry — realized coverage by subgroup, calibration metrics, set-size distributions, deferral and abstention rates — flows to the auditor face's system lens under the unified schema (RG-5); sustained coverage degradation is a governance event with an owner (MAK-RWC MA-7 review input).
**Rationale trace:** MAK-FFC EN-9; MAK-RWC MA-7; QU-3.

## Part 6 — The standing adversary

**What the research revealed.** Each corpus armed the corruption engine for a different hunt: the host corpus for engine failure regions and justification theater (EN-5, AF-4), the left wing for membership-geometry cliffs (FE-8 — the curve is a pre-drawn map of where behaviour changes fastest), the right wing for ontology edges (ME-2 — atypical presentations, envelope boundaries, gap-cluster cohorts). Consolidation reveals these as one program with three target maps and shared machinery — and exposes the gap none of the corpora closed: nobody watches what the adversary has *not* attacked. A standing adversary whose campaigns cluster on easy targets is vigilance theater; coverage of the attack surface must itself be measured.

### Adversary requirements

### AD-1 (MUST)
**Statement:** One corruption-engine program runs three target maps on scheduled campaigns: (i) *membership geometry* — supports, crossover points, threshold neighbourhoods of every ratified MF (MAK-LWC FE-8); (ii) *ontology edges* — envelope boundaries, atypical and missing-category constructions, gap-report-cluster cohorts (MAK-RWC ME-2); (iii) *justification and metrics* — boilerplate, duplication, temporal anomalies, metric gaming (MAK-FFC AF-4, MAK-RWC MA-3). Maps share harness machinery and finding schemas; campaign scheduling is governed and recorded.
**Rationale trace:** MAK-FFC EN-5/AF-4 + MAK-LWC FE-8 + MAK-RWC ME-2/MA-3, consolidated *(new as one program)*; MAK-MIF beat 7.

### AD-2 (MUST)
**Statement:** Confirmed findings publish as rebuttal objects bound to the warrants, curves, or envelopes they defeat, face-visible wherever those elements fire (SPINE-2's rebuttal slot); an engine, curve, or template version with unacknowledged confirmed findings inherits the release bar (MAK-FFC EN-5, MAK-LWC FE-8, carried).
**Rationale trace:** MAK-FFC EN-5 (carried); MAK-LWC FE-8 (carried); SPINE-2.

### AD-3 (MUST)
**Statement:** Findings route by type per the signal registry and MS-9: cliff and instability findings → curve/threshold review (MAK-LWC FA-6/FA-2); systematic-misfit findings → remodeling detection (MAK-RWC MS-4); calibration and coverage findings → QU-5/DX-5 owners; gaming and theater findings → human-review-only queues (MAK-FFC AF-4 discipline). Routing is deterministic from finding type; no finding class auto-sanctions or auto-changes any artifact.
**Rationale trace:** MAK-RWC MS-9 routing; MAK-LWC FA-6; MAK-FFC AF-4 human-review rule.

### AD-4 (SHOULD)
**Statement:** The adversary rides maintained harness machinery (the Giskard/ART class) with Mākoha-owned perturbation content — the clinical perturbation classes, curve-geometry sweeps, and cohort constructions are proprietary corpus assets versioned like code. Harnesses run in CI and campaign infrastructure only; no adversary component ships in a supplied artifact (CI-only per MAK-ELSM §08).
**Rationale trace:** MAK-ELSM ELSM-15/16 verdicts; MAK-J3 GPP-10 pattern; build-vs-buy economics.

### AD-5 (MUST)
**Statement:** The adversary is itself measured: campaign-coverage telemetry records, per warrant, curve, envelope, and engine version, when it was last attacked, by which map, and with what outcome; never-attacked and stale surface renders on the auditor system lens, and coverage floors are ratified per criticality class. Unattacked surface is a monitored risk, not an assumption of safety.
**Rationale trace:** *(new — closes the vigilance-theater gap)*; MAK-RWC MA-3 Goodhart logic applied to the adversary itself; AF-8 lens discipline.

## Part 7 — The release gate, firewall, lifecycle, and tiers

**What the research revealed.** Everything converges here. REG-KEEP-001 states the regulatory reading: the deterministic release path is "no longer exemption-motivated; remains correct safety architecture and strengthens the Essential Principles case." The consolidation duty is to state the gate as one pipeline with a fixed stage order — because the corpora's separate requirements (argument completeness, threshold conversion, envelope check, conflict materialization) interleave, and order ambiguity is where a second release path would hide. The firewall, the lifecycle replay, the telemetry schema, and the tier map complete the plane.

### The release pipeline

```text
// The single gate (RG-1). Deterministic, versioned, learned-parameter-free.
evaluate(draft: ActualArgumentDraft, template: GenericArgument) →
  stage 1  COMPLETENESS   all six Toulmin elements present; qualifier typed (OM-3);
                          rebuttal slot reconciled against confirmed findings (AD-2)     [SPINE-2]
  stage 2  THRESHOLDS     graded applicability → ratified template thresholds (FS-8);
                          method metadata honoured (FE-2)                                 [MAK-LWC]
  stage 3  ENVELOPE       grounds vs warrant envelope; in / out(attrs) / unknown (ME-1)   [MAK-RWC]
  stage 4  CONFLICTS      co-applicable template conclusions reconciled into
                          ConflictRecords — materialized, never resolved (SPINE-6/MS-5)
  stage 5  VERDICT        released | held(reason) | flagged(fit-judgment required)
                          — every verdict ledgered with its full stage trace (RG-2)
// No stage is skippable; no component other than this evaluator produces verdicts.
```

### Release, firewall, lifecycle, and tier requirements

### RG-1 (MUST)
**Statement:** One deterministic evaluator per deployment executes the five-stage pipeline above, in that order, as the sole path by which any draft becomes face-visible content. The evaluator is versioned, exhaustively unit-tested, free of learned parameters, and its stage order is normative: completeness before thresholds, thresholds before envelope, envelope before conflicts, conflicts before verdict. Negative tests prove no second path exists (RG-8).
**Rationale trace:** MAK-FFC SPINE-7 + MAK-LWC FS-8/FE-3 + MAK-RWC ME-1 + SPINE-6/MS-5, consolidated with a normative stage order *(new)*; REG-KEEP-001.

### RG-2 (MUST)
**Statement:** Every verdict — released, held, flagged — is ledgered with its complete stage trace: which stage produced the verdict, the evaluated values (typed per OM-3), the pins in force, and, for flagged releases, the recorded human fit-judgment (MS-7). The stage trace is argument content, renderable per register.
**Rationale trace:** SPINE-4; MAK-RWC MA-4 state derivation ("never from retrospective inference"); AF-7 export needs.

### RG-3 (MUST)
**Statement:** The evaluation firewall is absolute and hosts the plane's entire validation surface: training/tuning corpora disjoint from scoring corpora; evaluation code versioned; every reported figure reproducible by a party with no engine write access (MAK-FFC EN-7, carried); and the resident suites — the fuzzy harness (MAK-LWC FX-3), the two-wing routing suite (MAK-RWC MX-5), calibration and coverage validation (DX-5, QU-1/3), and contract conformance (RG-8) — run inside it.
**Rationale trace:** MAK-FFC EN-7 (carried); MAK-LWC FX-3; MAK-RWC MX-5; REG-KEEP-004 synthetic-only posture pre-GATE-002.

### RG-4 (MUST)
**Statement:** One lifecycle replay harness serves every change class: model version, curve/codebook version (MAK-LWC FA-5 impact preview), template/ontology version (MAK-RWC ME-5), and terminology release (MAK-FFC EN-8) all replay the sentinel decision set — plus a change-class-specific affected sample — across old and new versions, producing a divergence report that gates the respective ratification and remains attached to the change record (MA-1).
**Rationale trace:** MAK-FFC EN-8 + MAK-RWC ME-5 + MAK-LWC FA-5, consolidated into one harness *(new)*; SPINE-5.

### RG-5 (MUST)
**Statement:** One telemetry schema covers the plane: per-decision cost and latency (MAK-LWC FE-9), calibration and coverage by subgroup (QU-5), drift streams (curve drift, data shift, calibration drift), circumrational load (MAK-RWC MS-3), abstention and deferral rates (DX-6, QU-4), and campaign coverage (AD-5) — versioned as an artifact, emitted by every engine and the evaluator, and rendered only on the auditor face's system lens (AF-8/EN-9 discipline).
**Rationale trace:** MAK-FFC EN-9 + MAK-LWC FE-9 + MAK-RWC MS-3, consolidated *(new as one schema)*; MA-7 joint review needs.

### RG-6 (MUST)
**Statement:** Tier placement of every engine is a build-time property with SBOM evidence, per the consolidated map: **J-1 (lower-class included, deterministic runtime)** — evaluator, compiler, fuzzy layer (native per MAK-LWC FX-2), rule/CQL ommatidia; **J-2 (higher-class included, ML runtime)** — adds the Bayesian differential, conformal wrappers, OOD detectors, and any Class 4+ ambition; **J-3 (exempt reserve)** — evaluator and compiler only, warrant type `guideline-rule`, with Bayesian, conformal, fuzzy-inference-over-patient-data, LLM-runtime, and device-ingest modules structurally absent (MAK-J3 GPP-5/6/8/9; MAK-LWC FX-2). Tier labels follow FORK-REG-001; every build's SBOM diffs against its tier's manifest in CI.
**Rationale trace:** REG-POSTURE FORK-REG-001; MAK-J3 GPP-8; MAK-LWC FX-2; MAK-ELSM §08 dispositions.

### RG-7 (SHOULD)
**Statement:** Runtime substrate bindings follow REG-POSTURE as reasonable defaults contingent on their ASSUME-REG closures: inference serves from dedicated deployments with contractual version-stability and change-notice terms (Baseten Sydney per TASK-REG-009 / ASSUME-REG-004); regulated releases flow through the split gated pipeline (TASK-REG-010); engine versions, risk-file entries, and release approvals link through the Ketryx-on-Jira configuration (KTX-001..012, ASSUME-REG-006).
**Rationale trace:** REG-POSTURE TASK-REG-009/010, KTX schema; MAK-RWC MX-4 sibling binding.

### RG-8 (MUST)
**Statement:** A plane-level conformance suite gates every release: contract and purity conformance per ommatidium (OM-2/OM-4), signal-type non-coercion tests (OM-3), single-gate negative tests (OM-5/RG-1 — attempts to reach a face bypassing the evaluator must fail structurally), tier-boundary negative tests per build (RG-6, the GPP-CONF pattern generalized), and replay determinism checks (RG-4). Suite results are conformity-file artifacts (Essential Principles evidence under the assume-inclusion posture).
**Rationale trace:** MAK-J3 GPP-10 pattern generalized to all tiers *(new)*; MAK-RWC MX-5; REG-KEEP-002.

### Engine-plane anti-requirements

- Never a second gate: no cache, notification service, summary job, or "preview" path that shows a face un-evaluated engine output (violates OM-5/RG-1).
- Never merge signals: no schema field, aggregation, or render that presents posterior, coverage, μ, reliability, or fit as one number (violates OM-3).
- Never let the adversary idle on easy targets: campaign scheduling that never revisits stale surface is vigilance theater (violates AD-5).
- Never ship a proposal pipeline: learning, mining, and extraction code is structurally absent from supplied artifacts in every tier (CP-5; GPP-8 pattern).
- Never tune a curve, threshold, envelope, or metric in place to quiet telemetry — every such change is a governed, replayed version (RG-4; MAK-RWC MA-3).

### Phased execution plan

| Phase | Builds | Gate to exit |
|---|---|---|
| `CE-P0 · Contract & registry` | Unified engine contract; five-signal schema; evaluator pipeline skeleton (stages 1–2); RG-8 suite v1 | Contract conformance green on the first rule/CQL ommatidia; signal non-coercion tests pass |
| `CE-P1 · Compiler lift` | CP-1 path over one guideline domain: CQL/PlanDefinition ingest → templates with tiers, methods, thresholds, envelopes; CP-6 validation | One domain compiled end-to-end; every template enveloped; impact preview works (CP-3) |
| `CE-P2 · Gate complete` | Stages 3–5 (envelope, conflicts, verdict); RG-2 stage traces; flagged path with fit-judgment capture | Single-gate negative tests pass; out-of-envelope release impossible without recorded judgment |
| `CE-P3 · Differential` | DX-1..5 on the pilot domain: decomposed likelihood warrants, parameter backing, calibration harness; abstention output (DX-6) | Calibration bounds ratified and met on firewalled corpus; abstention telemetry flowing |
| `CE-P4 · Qualifier & adversary` | Conformal wrappers with subgroup coverage (QU-1/3); fit-signal routing (QU-2); AD-1 three-map program; AD-5 coverage telemetry | Subgroup coverage within bounds; first campaign cycle complete on all three maps |
| `CE-P5 · Lifecycle & tiers` | RG-4 unified replay across all change classes; RG-5 telemetry schema; RG-6 tier builds with SBOM evidence; RG-7 substrate bindings | A change of each class replayed and ratified end-to-end; J-tier builds pass boundary tests |

### Risk register

| Risk | Mechanism | Standing control |
|---|---|---|
| Second-path erosion | Convenience features (caches, previews, digests) leak un-evaluated output to faces | RG-1/OM-5 negative tests in CI; architecture review on every face-adjacent feature |
| Signal soup at the seams | Aggregators and dashboards blend the five signals where schemas meet UI | OM-3 non-coercible types end-to-end; RG-8 tests; MAK-LWC FC-6 lint inheritance |
| Mosaic incoherence | Ommatidia version-skew: fragments computed under different pins assemble into one argument | OM-2 pins on every fragment; evaluator refuses mixed-pin drafts (stage 1); RG-4 replay |
| Monolith regression | Deadline pressure fuses criteria into one model "temporarily" | OM-1 cluster-declaration duty; CP-3 grain telemetry (whole-plane recompiles as alarms) |
| Calibration rot | Posteriors drift post-release while headline metrics hold | DX-5 blocking bounds; QU-5 telemetry; AD-3 routing to owners |
| Adversary capture | Campaign content tunes to what engines already survive | AD-5 coverage floors; governed campaign scheduling; MA-3 Goodhart lens on the adversary's own metrics |
| Tier seepage | Shared modules drift probabilistic code into J-3 or unpinned models into J-1 | RG-6 SBOM diffs in CI; GPP-CONF-pattern negative tests; MAK-ELSM §08 namespace manifest |
| Substrate drift | Managed-service model updates change behaviour under pinned labels | RG-7 contractual version-stability terms (ASSUME-REG-004); RG-4 sentinel replay on substrate change notices |

### Open research agenda

- **Mosaic assembly semantics.** When ommatidia disagree (overlapping criteria, plural lineages), the assembly of fragments into one differential needs formal semantics beyond conflict materialization — candidate ground in argumentation-theoretic aggregation (TweetyProject semantics) against clinical validity constraints.
- **Subgroup schema governance.** QU-3 requires a ratified subgroup schema; who ratifies it, at what grain, and how it evolves without Goodhart effects is an open governance-design question with equity stakes.
- **Abstention economics.** DX-6's abstention rate trades against utility; the Maturity Level 3 evidence stream needs a pre-registered protocol for what abstention profile justifies which FORK-REG-001 branch.
- **Campaign-coverage metrics.** AD-5 needs a defensible attack-surface enumeration (warrants × curves × envelopes × cohorts) and staleness model; no precedent exists in the adversarial-ML literature for governed clinical campaign coverage.
- **Cross-signal display research.** OM-3 keeps five signals apart in the schema; whether clinicians can read five typed signals without conflation is an MC-7/FC-7-class evaluation question the display literature has not answered.

## Part 8 — Consolidation maps & traceability

### Three-corpus consolidation map (complete for the engine plane)

| Source requirement | Disposition here | Carrier |
|---|---|---|
| MAK-FFC EN-1 (engine contract) | consolidated | OM-2 |
| MAK-FFC EN-2 (criterion grain) | carried + organizing principle | OM-1, CP-3 |
| MAK-FFC EN-3 (compiler sole path) | consolidated | CP-1 |
| MAK-FFC EN-4 (conformal qualifier) | carried + extended | QU-1, QU-2, QU-3 |
| MAK-FFC EN-5 (standing adversary) | consolidated | AD-1, AD-2 |
| MAK-FFC EN-6 (LLM classes) | consolidated | CP-5, DX-7 |
| MAK-FFC EN-7 (evaluation firewall) | carried + hosting duty | RG-3 |
| MAK-FFC EN-8 (drift as versioned change) | consolidated | RG-4 |
| MAK-FFC EN-9 (telemetry lens) | consolidated | RG-5, QU-5 |
| MAK-LWC FE-1 (pure fuzzification service) | generalized | OM-4 (purity for all engines) |
| MAK-LWC FE-2 (method as template metadata) | carried | CP-1, RG-1 stage 2 |
| MAK-LWC FE-3 (no fuzzy release) | generalized | OM-5 |
| MAK-LWC FE-4 (curve learning proposal-only) | consolidated | CP-5 |
| MAK-LWC FE-5 (coupling law) | carried as plane law | DX-4 |
| MAK-LWC FE-6 (CWW single render path) | carried in host | remains MAK-LWC-governed; consumes evaluator output only (OM-5) |
| MAK-LWC FE-7 (type-2 trigger-gated) | carried in host | knowledge-plane matter; enters via CP-1 when triggered |
| MAK-LWC FE-8 (boundary sweeps) | consolidated | AD-1 map i |
| MAK-LWC FE-9 (vectorized, budgeted) | consolidated | RG-5 |
| MAK-LWC FS-3 (type separation) | extended | OM-3 (five-signal registry) |
| MAK-LWC FS-8 (evaluator owns thresholds) | consolidated | RG-1 stage 2 |
| MAK-LWC FX-2 (fuzzy J-tier map) | consolidated | RG-6 |
| MAK-LWC FX-3 (fuzzy validation harness) | hosted | RG-3 |
| MAK-RWC ME-1 (envelope enforcement) | consolidated | RG-1 stage 3 |
| MAK-RWC ME-2 (boundary hunting) | consolidated | AD-1 map ii |
| MAK-RWC ME-3 (commitments register) | consolidated | CP-1, CP-6 |
| MAK-RWC ME-4 (gap mining authoring-time) | consolidated | CP-5 |
| MAK-RWC ME-5 (remodeling replay) | consolidated | RG-4 |
| MAK-RWC ME-6 (model applicability as data) | carried + extended | DX-2, DX-5, QU-3 |
| MAK-RWC ME-7 (fit-signal routing) | consolidated | QU-2, AD-3 |
| MAK-RWC ME-8 (what-if sandbox) | carried in host | lives inside RG-3's firewall |
| MAK-RWC MS-9 (wing routing) | carried as plane law | OM-3, AD-3 |
| MAK-RWC MX-5 (two-wing suite) | hosted | RG-3, RG-8 |

### MAK-MIF beat map (engine-plane couplings)

| Beat | Engine-plane coupling | Carrier |
|---|---|---|
| 1 · The borderline patient | Graded fit measured (stage 2) then governed at the gate (stages 3/5) | RG-1 |
| 2 · The full translation loop | Encoding traces on grounds in; evaluator traces out | OM-2, RG-2 |
| 3 · Meaning under governance | Curve versions replay through the unified harness | RG-4 |
| 4 · Conflict with a metric | Graded applicability shapes conflicts the gate materializes | RG-1 stage 4 |
| 5 · Disagreement held, not averaged | Plural lineages compile side by side; the compiler never merges | CP-4 |
| 6 · Reliability-aware listening | Reliability passes through typed, never transformed | OM-3 |
| 7 · The adversary's map | Three target maps, one program, measured coverage | AD-1, AD-5 |
| 8 · The LLM on a leash | One proposal pipeline, one ratification interface, no runtime presence | CP-5, DX-7 |

### Findings → requirements

| Finding | Source | Requirements it drives |
|---|---|---|
| Small per-criterion units survive guideline change; monoliths fossilize | Blake 2016 ("flexible and easy to change"); ICSD-2 freeze | OM-1, CP-3 |
| Engine-agnostic reasoning layers work behind one interface | Miah, Blake & Kerr 2020 | OM-2, OM-7 |
| Attribution ≠ justification; unvalidated explanation is liability | Abbas 2025 | OM-5, QU-1, DX-5 |
| Transfer fails across contexts; heterogeneity is the expected case | Cockburn 2024 | QU-3, RG-1 stage 3, AD-1 map ii |
| Vagueness ≠ uncertainty ≠ reliability; type separation is load-bearing | Zadeh lineage via MAK-LWC; MAK-DOT | OM-3, DX-4 |
| Fit ≠ degree; ontology misfit needs its own routing | Chapman via MAK-RWC; MAK-MIF beats 1–2 | OM-3, QU-2, AD-3 |
| No adoptable OSS differential engine exists; primitives are mature | MAK-ELSM §03 gap note | DX-1..5 (build specification) |
| Group-conditional conformal narrows subgroup coverage gaps under shift; deferral is the safe action | Kwon 2026 (Sci. Reports); conformal selective-prediction literature | QU-3, QU-4 |
| OOD detectors find underrepresented, worse-served subgroups | Weng 2025 (CTS); Subasri 2025 (JAMA Netw Open) via MAK-RWC Part 9 | QU-2, RG-5 |
| Anytime-valid monitoring controls false alarms in deployment streams | Prinster 2025 (WCTM); Timans 2025 | QU-5, RG-5 candidates |
| LLMs fail flexible clinical reasoning with overconfident uncertainty | Kim 2025 (mARC-QA) | DX-7, CP-5 |
| Deterministic release is correct safety architecture independent of exemption | REG-POSTURE REG-KEEP-001 | RG-1 |
| Tier labels: lower-class vs higher-class included; abstention evidence decides | REG-POSTURE FORK-REG-001 | RG-6, DX-6 |
| Substrate pinning requires contract terms, not configuration | REG-POSTURE TASK-REG-009 / ASSUME-REG-004 | RG-7 |

### Sources

- Series (host and wings): MAK-FFC v1.1 Part 6 and SPINE law · MAK-LWC v1.1 Parts 2/6/7 · MAK-RWC v1.1 Parts 2/6/7 · MAK-MIF v1.0 · MAK-ELSM v1.1 (all sourcing rows cited here resolve there) · MAK-J3 (tier-boundary patterns).
- REG-POSTURE v1.0 — REG-KEEP-001, FORK-REG-001, TASK-REG-009/010, KTX-001..012, ASSUME-REG-004/006; cited by stable ID per its convention.
- Blake, Kerr & Gammack 2016 (Information Systems 56) — the 28-decision-point decomposition evidence; Miah, Blake & Kerr 2020 (AJIS 24) — reasoning-agnostic layer.
- Abbas, Jeong & Lee 2025 (Healthcare 13:2154); Cockburn et al. 2024 (eClinicalMedicine 76); Bayor et al. 2025 (JMIR 27:e63733) — uploaded evidence base.
- Deployment-monitoring and conformal literature (verified in MAK-RWC Part 9 refresh): Weng et al. 2025 (Clinical and Translational Science); Subasri et al. 2025 (JAMA Network Open); Santos Silva et al. 2025 (J. Biomed. Informatics); Prinster et al. 2025 (WCTM); Timans et al. 2025; Nguyen et al. 2025 (D3M); Kwon et al. 2026 (Scientific Reports); Kim et al. 2025 (mARC-QA, Scientific Reports).
- Tooling verifications: carried from MAK-ELSM v1.1, MAK-LWC v1.1 Part 9, and MAK-RWC v1.1 Part 9; new engine-plane verifications in Part 9 below carry their own dates.

*Document footer (source artifact):* The Compound Eyes Corpus v1.0 · requirement IDs are stable; propose changes as argued deviations — this document practices its own doctrine. Compiled from the three host corpora read in full, REG-POSTURE v1.0, and the series' verified sourcing record, 1 Sep 2026.

## Part 9 — Execution sourcing annex

The engine plane's sourcing record is already the deepest in the series: MAK-ELSM v1.1 (host plane), MAK-LWC v1.1 Part 9 (fuzzy runtimes and CWW gaps), and MAK-RWC v1.1 Part 9 (monitoring, OOD, regulatory instruments) each carry verified entries this corpus consumes. This annex does not restate them; it consolidates the engine-plane view and records what each part of *this* corpus adopts, adapts, or builds. Carried statuses are dated observations from their host annexes; re-verify before dependency decisions.

### Consolidated engine-plane sourcing view

| Plane part | Adopt/adapt (verified in host annexes) | Build (no precedent found) |
|---|---|---|
| Ommatidial substrate (OM) | CQL stack (ELSM-01/02), HAPI (ELSM-20) for rule/CQL ommatidia; fuzzy runtimes (MAK-LWC Part 9: pyfuzzylite/scikit-fuzzy/Simpful class) for fuzzy ommatidia | The unified contract layer and five-signal schema (OM-2/3) |
| Compiler plane (CP) | CQL translator, clinical-reasoning $apply, WHO SMART IGs (ELSM-01/02/06); ArgLLMs/ArgTumour pattern code (ELSM-09) for proposal pipelines | The GenericArgument annotation lift: tiers, methods, thresholds, envelopes per warrant (the MAK-ELSM integration note, extended by ME-3/MS-1) |
| Differential (DX) | pgmpy-class PGM primitives (ELSM-14); Babylon counterfactual code as study-only baseline (ELSM-13) | The decomposed differential itself: likelihood-as-warrant structure, per-parameter backing, calibration harness (the ELSM §03 gap, now specified) |
| Qualifier (QU) | MAPIE (ELSM-12); alibi-detect (ELSM-R01) for OOD; WCTM/D3M-class monitoring literature (MAK-RWC Part 9) | Subgroup-coverage governance (QU-3) and typed double-duty routing (QU-2) |
| Adversary (AD) | Giskard (ELSM-15), ART (ELSM-16) as harness machinery, CI-only | The three target maps' content: clinical perturbation classes, curve-geometry sweeps, cohort constructions, campaign-coverage model (AD-1/5) |
| Gate & lifecycle (RG) | Aurora + transparency-log pattern (ELSM-19) or immudb (ELSM-17, BUSL review) for verdict ledger; evidently (ELSM-R02) for telemetry scaffolding; openregulatory templates (ELSM-R04) + Ketryx (commercial) for lifecycle records | The five-stage evaluator, the unified replay harness, the tier manifests (RG-1/4/6) — the moat's engine-room floor |

### The engine plane's build list (consolidated)

No public precedent found (methodology hedge carried from MAK-ELSM): the five-stage deterministic evaluator with normative stage order; the unified engine contract with typed five-signal output; the decomposed Bayesian differential with per-parameter evidence backing; the unified lifecycle replay harness parameterized by change class; the campaign-coverage model for a standing clinical adversary; the tier-manifest SBOM discipline generalized from MAK-J3 GPP-8. Everything around them remains buyable; they are not.


### v1.1 refresh pass (additive; verified 2026-09-01)

New engine-plane entries, each a direct repo fetch on 2026-09-01:

| ID | Repo / artifact | What it gives you | Status (verified) | Verdict | Serves |
|---|---|---|---|---|---|
| ELSM-E01 | [pgmpy/pgmpy](https://github.com/pgmpy/pgmpy) | Causal and probabilistic graphical models: construction, exact/approximate inference, causal discovery — the differential's PGM primitives, now verified in detail (carried generically as ELSM-14) | 3.3k★ · MIT · active (3,650 commits, busy tracker) | ADOPT | DX-1, DX-2 |
| ELSM-E02 | [pymc-devs/pymc](https://github.com/pymc-devs/pymc) | Probabilistic programming with MCMC/VI — the offline path for parameter estimation, prior elicitation checks, and calibration studies feeding DX-3/DX-5; too heavy and too stochastic for runtime ommatidia | 9.7k★ · Apache-2.0 · v6.0.1 May 2026 · active | ADAPT (offline/CP-5 pipelines only) | DX-3, DX-5 |
| ELSM-E03 | [henrikbostrom/crepes](https://github.com/henrikbostrom/crepes) | Conformal classifiers, regressors, and predictive systems (p-values, CDFs, sets/intervals with coverage guarantees) — a second maintained conformal implementation beside MAPIE, useful for cross-validating QU-1 wrappers and for Mondrian variants | 579★ · BSD-3-Clause · v0.9.1 Jun 2026 · active | ADOPT | QU-1, QU-3, RG-3 |
| ELSM-E04 | [EFS-OpenSource/calibration-framework](https://github.com/EFS-OpenSource/calibration-framework) (netcal) | Calibration measurement and recalibration methods (reliability metrics, binning/scaling families) — DX-5's calibration harness has off-the-shelf metrics | 379★ · Apache-2.0 · v1.3.6 Aug 2024 — slow-moving; verify maintenance before adoption | ADAPT | DX-5, QU-5 |

**Refresh notes.**

- The DX build thesis survives verification: primitives (ELSM-E01/E02) and evaluation machinery (ELSM-E03/E04) are mature and license-clean, and no adoptable decomposed differential exists — the build list stands.
- Dual-implementation discipline: running MAPIE (ELSM-12) and crepes (ELSM-E03) against the same firewalled corpus gives the qualifier wrapper an implementation cross-check, cheap insurance for a component whose failure is silent (miscoverage).
- netcal's release cadence (last release 2024-08) makes it a candidate for vendoring or metric re-implementation rather than dependency adoption if maintenance has not resumed at decision time — the fasten-onprem lesson at library scale.
- PyMC placement is a tier matter: it appears only in CP-5 proposal pipelines and firewall studies; its namespaces belong on the J-1 and J-3 tier manifests' denylists (RG-6), since runtime stochastic sampling violates OM-4 purity in every tier.

## Appendix C — v1.1 sourcing register (additive)

Mirrors the refresh table; keep in sync (self-audit check 11).

```json
{
  "doc_id": "MAK-CEC",
  "version": "1.1",
  "verified": "2026-09-01",
  "entries": [
    {"id":"ELSM-E01","name":"pgmpy/pgmpy","verdict":"ADOPT","license":"MIT","status":"active","serves":["DX-1","DX-2"]},
    {"id":"ELSM-E02","name":"pymc-devs/pymc","verdict":"ADAPT_OFFLINE","license":"Apache-2.0","status":"active; v6.0.1 2026-05","serves":["DX-3","DX-5"]},
    {"id":"ELSM-E03","name":"henrikbostrom/crepes","verdict":"ADOPT","license":"BSD-3-Clause","status":"active; v0.9.1 2026-06","serves":["QU-1","QU-3","RG-3"]},
    {"id":"ELSM-E04","name":"EFS-OpenSource/calibration-framework","verdict":"ADAPT","license":"Apache-2.0","status":"slow-moving; v1.3.6 2024-08","serves":["DX-5","QU-5"]}
  ]
}
```

## Appendix A — ID census (additive)

Authoritative enumeration for validator checks. Count: **38**.

```json
{
  "doc_id": "MAK-CEC",
  "version": "1.0",
  "requirements": {
    "OM": ["OM-1","OM-2","OM-3","OM-4","OM-5","OM-6","OM-7"],
    "CP": ["CP-1","CP-2","CP-3","CP-4","CP-5","CP-6"],
    "DX": ["DX-1","DX-2","DX-3","DX-4","DX-5","DX-6","DX-7"],
    "QU": ["QU-1","QU-2","QU-3","QU-4","QU-5"],
    "AD": ["AD-1","AD-2","AD-3","AD-4","AD-5"],
    "RG": ["RG-1","RG-2","RG-3","RG-4","RG-5","RG-6","RG-7","RG-8"]
  },
  "levels": {
    "MUST":   ["OM-1","OM-2","OM-3","OM-4","OM-5","CP-1","CP-2","CP-3","CP-4","CP-6","DX-1","DX-2","DX-3","DX-4","DX-5","DX-7","QU-1","QU-2","QU-3","QU-5","AD-1","AD-2","AD-3","AD-5","RG-1","RG-2","RG-3","RG-4","RG-5","RG-6","RG-8"],
    "SHOULD": ["OM-6","CP-5","DX-6","QU-4","AD-4","RG-7"],
    "MAY":    ["OM-7"]
  },
  "retired": []
}
```

Census arithmetic: 31 MUST + 6 SHOULD + 1 MAY = 38.

## Appendix B — Self-audit checks (additive)

Run against this file after any edit; all must pass before a version increments.

1. **ID uniqueness** — no requirement ID appears in more than one requirement header.
2. **ID census parity** — headers matching `^### (OM|CP|DX|QU|AD|RG)-\d+ \((MUST|SHOULD|MAY)\)$` exactly equal Appendix A's enumeration (38).
3. **Level parity** — the level in each header matches its bucket in Appendix A `levels`.
4. **Trace presence** — every requirement block contains a non-empty `**Rationale trace:**` line.
5. **Normative leakage** — no capitalized MUST/SHOULD/MAY in informative prose outside requirement blocks, anti-requirement bullets, quoted source text, or this appendix.
6. **Consolidation integrity** — every EN/FE/ME requirement of the three host corpora's engine planes appears in the Part 8 consolidation map with a disposition; no source requirement is described as relaxed or retired.
7. **Cross-reference integrity** — every OM/CP/DX/QU/AD/RG ID cited in prose or tables exists in the census; every MAK-FFC, MAK-LWC, MAK-RWC, GPP, ELSM, and REG-POSTURE ID cited resolves in its host document.
8. **Regulatory precedence** — tier language follows FORK-REG-001; no statement contradicts a REG-FIND; ASSUME-REG items are never described as closed.
9. **Table integrity** — all markdown tables have consistent column counts per row.
10. **Stability** — IDs present in a previous version are present or explicitly retired in Appendix A; retired IDs never reused.
11. **Refresh register parity (v1.1)** — every ELSM-Enn row in the refresh table has exactly one Appendix C entry and vice versa; refresh statuses carry the 2026-09-01 verification date.
