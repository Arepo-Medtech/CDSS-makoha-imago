---
doc_id: MAK-HDC
title: "The Head Corpus"
version: "1.0"
date: "2026-09-01"
series: "Mākoha research series — volume 10 · the Clinician Face, consolidated from both wings"
status: normative-draft
normative_language: RFC-2119 (MUST / SHOULD / MAY)
req_prefixes: [HW, HR, HA, HG, HT, HE]
req_count: 30
subordinate_to: "MAK-FFC v1.1 — no requirement here relaxes a corpus MUST; consolidations state their sources"
builds_from:
  - "MAK-FFC v1.1 Part 3 — the host Clinician Face (CF-1..8, component inventory, anti-requirements)"
  - "MAK-LWC v1.1 Part 3 — the fuzzy clinician face (FC-1..7): graded chips, borderline flags, channel separation"
  - "MAK-RWC v1.1 Part 3 — the meta-rational clinician face (MC-1..7): envelope rendering, gap reporting, conflict workbench"
  - "MAK-CEC v1.1 — the engine plane this face consumes: verdicts with stage traces (RG-1/2), the five-signal registry (OM-3)"
governed_by:
  - "REG-POSTURE v1.0 — REG-KEEP-002 (reviewable basis is the product thesis), REG-KEEP-003 (human sign-off, fail-closed), glass-box discipline (REG-FIND-004 via MAK-RWC MX-2)"
changelog:
  - "v1.0 (2026-09-01): initial release — 30 requirements across HW/HR/HA/HG/HT/HE; three-corpus consolidation map (Part 7); sourcing annex (Part 8)."
companions:
  - "MAK-FFC v1.1 (host) · MAK-LWC v1.1 (left wing) · MAK-RWC v1.1 (right wing) · MAK-CEC v1.1 (engine plane)"
  - "MAK-MIF v1.0 (beats 1, 2, 4, 5 land on this face)"
  - "REG-POSTURE v1.0 (governing regulatory document)"
artifact_url: "https://claude.ai/code/artifact/f4313ff2-3da1-4250-ad17-187119f555f0"
change_policy: "Requirement IDs are stable; retired IDs never reused. Propose changes as argued deviations."
---

<!-- LLM USAGE CONTRACT (additive; not part of the source document)
1. Requirement blocks (### HW-n / HR-n / HA-n / HG-n / HT-n / HE-n) are NORMATIVE;
   all other prose is INFORMATIVE. Part 8 is an informative sourcing annex.
2. This corpus CONSOLIDATES the clinician-face requirements of MAK-FFC (CF),
   MAK-LWC (FC), and MAK-RWC (MC). Source IDs remain valid in their host documents;
   the Part 7 map is the cross-walk, and a host requirement always governs over any
   apparent difference here.
3. The one-surface law (HR-1) binds generation: every clinician-facing display is a
   projection of evaluator-released argument objects — never design a widget fed by
   a side channel.
4. Scope: this corpus specifies face behaviour and components. Interaction-level and
   visual specification is the Labial Palps volume (Clinician UI); where this corpus
   states a rendering duty, that volume says how it looks.
5. MUST violations in generated designs/code/documents require an explicit DEVIATION
   notice naming the ID.
6. Appendix A's ID census is authoritative for validator checks; Appendix B's
   self-audit checks gate any edit of this file.
END LLM USAGE CONTRACT -->

# The Head Corpus

A translatable research primer and execution manual for the Clinician Face of the triple-facing CDSS — workflow placement, the clinical register's rendering law, the clinician's recorded acts, attention governance, team modes, and evaluation — consolidating the clinician-face requirements of the host corpus and both wings into one buildable face.

**Document metadata:** Technical corpus · v1.0 · 1 Sep 2026 · tenth volume in the Mākoha research series · STATUS: normative draft · REQ IDS: HW · HR · HA · HG · HT · HE · SUBORDINATE TO: MAK-FFC v1.1 · BUILDS FROM: CF + FC + MC + MAK-CEC · GOVERNED BY: REG-POSTURE v1.0.

## Contents

1. [Part 0 — How to use this document](#part-0--how-to-use-this-document)
2. [Part 1 — Foundation: the head of the butterfly](#part-1--foundation-the-head-of-the-butterfly)
3. [Part 2 — Workflow placement (HW)](#part-2--workflow-placement)
4. [Part 3 — The rendering law (HR)](#part-3--the-rendering-law)
5. [Part 4 — Clinical acts (HA)](#part-4--clinical-acts)
6. [Part 5 — Attention governance (HG)](#part-5--attention-governance)
7. [Part 6 — Team modes (HT)](#part-6--team-modes)
8. [Part 7 — Evaluation, telemetry & consolidation maps (HE)](#part-7--evaluation-telemetry--consolidation-maps)
9. [Part 8 — Execution sourcing annex](#part-8--execution-sourcing-annex)
10. [Appendix A — ID census](#appendix-a--id-census-additive)
11. [Appendix B — Self-audit checks](#appendix-b--self-audit-checks-additive)

## Thesis

> The head is where the butterfly's senses concentrate and where decisions about motion are made — but the head does not fly; the wings and body do. The Clinician Face is built on the same division: it is the surface where the system's whole evidentiary machinery concentrates into one register for one judgment — the clinician's — and it performs no inference of its own. Three corpora specified its layers: the host corpus placed it in the workflow (capture before the encounter, read-and-decide inside it) and armed it with the deviation machinery; the left wing taught it to show degree (graded chips, borderline flags, channels that never blend); the right wing taught it to show fit (envelopes with weight parity, gap reporting one interaction away, the system arguing against itself). What no corpus states is the face law that integrates them: one argument surface fed only by evaluator verdicts, five typed signals rendered without conflation, one attention budget across every interruption class, and a sign-off act that is fail-closed because the regulatory posture — not the exemption — demands it. This corpus states it.

## Part 0 — How to use this document

This corpus is the Clinician Face's single execution manual. Like MAK-CEC for the engine plane, it consolidates rather than invents: most requirements carry CF, FC, or MC sources, named in the trace; the Part 7 map is the complete cross-walk; genuinely new face law is marked *(new)*. Interaction-level specification (screens, components, states) belongs to the Labial Palps volume; this corpus states what the face does and never how it is drawn beyond what conformance requires.

- **Normative language.** MUST / SHOULD / MAY per RFC 2119.
- **Requirement IDs.** `HW-n` workflow placement; `HR-n` rendering law; `HA-n` clinical acts; `HG-n` attention governance; `HT-n` team modes; `HE-n` evaluation and telemetry.
- **Consolidation discipline.** CF/FC/MC remain valid in their hosts; this corpus adds integration constraints and never relaxes a source MUST.
- **Regulatory precedence.** REG-POSTURE v1.0 governs. Two of its retained commitments are this face's law: REG-KEEP-002 (a reviewable basis for every output is the product thesis) and REG-KEEP-003 (human sign-off, fail-closed).

## Part 1 — Foundation: the head of the butterfly

**The face's evidence base, in one paragraph.** Bayor et al.'s review gives the failure catalogue this face must not repeat: 37 of 40 systems clinician-only yet still failing clinicians — rigid structures, workflow mismatch, prompt fatigue, trust collapse when recommendations cannot be interrogated, surveillance anxiety. The Blake program supplies the working counter-pattern (capture before the consultation, pre-digested briefs, per-criterion argument trees) and the honest boundary (Croskerry cited, discretion left to the human). Spitzer et al.'s 2,020-assessment RCT gives the rendering direction empirical teeth: reasoning-shaped explanation improves clinician accuracy where bare outputs and even differential lists do not. Stranieri's ward-round and MDT fieldwork establishes that consequential clinical reasoning is narrative, social, and often collective. And the regulatory posture reframes the face's transparency duty: after REG-FIND-003/004, a reviewable, glass-box basis is not an exemption strategy — it is the Essential Principles case and the product thesis (REG-KEEP-002).

**What consolidation adds.** Reading CF, FC, and MC side by side exposes four face-level laws no single corpus states. (i) *One surface:* the face renders projections of evaluator-released argument objects and nothing else — the moment a widget draws on a side channel (a cache of engine output, a convenience score, an un-evaluated preview), SPINE-1 dies at the last mile (HR-1). (ii) *Five signals, one grammar:* posterior, coverage, μ, reliability, and fit each have a rendering identity; the face is where OM-3's type discipline either survives contact with pixels or does not (HR-2). (iii) *One attention budget:* alerts (CF-4/5), borderline flags (FC-2), meta-prompts (MC-6), and fit warnings (MC-1) are one interruption economy — governed separately, they will separately exhaust the clinician (HG-1). (iv) *Sign-off is an act with a record:* REG-KEEP-003's fail-closed human sign-off is the face's terminal act, and it must be as evidenced as everything upstream (HA-1).

> The doctrine in one sentence: the face concentrates evidence into judgment — it never dilutes judgment into compliance.

## Part 2 — Workflow placement

**What the research revealed.** The Blake pattern is the spine of this part: physicians were spending consultation time on routine history questions; moving capture to the patient before the encounter made the consultation "patient-driven not form-driven" and cut the read to an assimilable brief. Bayor's review names workflow mismatch — "information only several steps ahead of the operational workflow" — as a dominant failure mode. The consolidation duty is to hold that pattern while the face absorbs both wings' additions without re-inflating the encounter.

### Workflow requirements

### HW-1 (MUST)
**Statement:** The face follows the Blake placement law (MAK-FFC CF-1, carried): data capture happens before the consultation on the patient face; synthesis happens before the encounter (Consult-Prep Composer); in-consultation interaction is read-and-decide. In-consultation input is limited to confirmation, sign-off, deviation, gap report, and conflict navigation — the recorded clinical acts of Part 4 — and nothing else.
**Rationale trace:** MAK-FFC CF-1 (carried); Blake 2014; Bayor workflow-mismatch findings.

### HW-2 (MUST)
**Statement:** The Consult-Prep brief is a projection of the fabric: intake, monitoring, history, triage-urgency proposal with its argument, active envelopes and applicable rebuttals for the expected decision set, and ratified trend descriptors (MAK-LWC FC-4) — assembled server-side from evaluator-released content, with every element one interaction from its full argument.
**Rationale trace:** MAK-FFC Consult-Prep component; MAK-LWC FC-4; MAK-RWC MC-5 (known-failure visibility); HR-1.

### HW-3 (MUST)
**Statement:** The brief is bounded: a ratified reading-budget (length and structure ceiling per encounter class) governs Consult-Prep; overflow content collapses behind drill-down rather than expanding the surface. Adding a wing's new signal class never grows the default brief beyond budget — signals compete for the budget through governed layout, not accretion.
**Rationale trace:** Blake "assimilable report" finding; Bayor information-overload; *(new — the reading budget as conformance property)*.

### HW-4 (SHOULD)
**Statement:** Handover and referral narratives (MAK-FFC CF-8) generate from the fabric in the clinical register, marked as derived content, using ratified trend and codebook vocabulary (MAK-LWC FS-5); free-text additions by the clinician are preserved distinctly from generated text.
**Rationale trace:** MAK-FFC CF-8 (carried); MAK-LWC FC-4/FS-5; ward-round narrative finding.

### HW-5 (MUST)
**Statement:** The face degrades gracefully to the low-resource profile: Consult-Prep, argument drill-down, and the Part 4 acts function offline-first with deferred sync inside XC-3's gates and MX-3's meta-rational floor; no workflow step depends on real-time connectivity to complete an encounter.
**Rationale trace:** MAK-FFC XC-3; MAK-RWC MX-3; north star.

## Part 3 — The rendering law

**What the research revealed.** The face inherits five typed signals (MAK-CEC OM-3) and a verdict stream with stage traces (RG-2), and the literature is unambiguous about the rendering direction: argument-shaped beats naked-score (Spitzer 2026; Nunes & Jannach taxonomy); unvalidated explanation is liability (Abbas 2025); binary chrome hides exactly the cases needing judgment (the left wing's cliff evidence); and reference-class transparency — was this validated for someone like this patient? — is both the trust mechanism and the regulator's glass-box demand (MC-1; REG-FIND-004).

### Rendering requirements

### HR-1 (MUST)
**Statement:** The one-surface law: every clinician-facing display element is a projection of evaluator-released argument objects (verdicts with stage traces, per MAK-CEC RG-1/2) read through the fabric's register API (SPINE-9). No widget consumes engine output, caches of pre-verdict state, or any side channel; face-local caches are derived, disposable, and rebuildable from the ledger.
**Rationale trace:** MAK-FFC SPINE-1/9 + MAK-CEC OM-5/RG-1, stated as face law *(new)*; second-path erosion risk.

### HR-2 (MUST)
**Statement:** The five signals render as five identities: posterior (belief), coverage (set + stated coverage), μ (graded meaning with term label, per MAK-LWC FC-1), reliability (source-stated confidence), and fit (envelope status) each have a distinct, consistent visual and verbal identity across the face; no composite score, gauge, or color scale blends them. The separation is a design-review checklist item (MAK-LWC FC-3, carried) extended to all five types.
**Rationale trace:** MAK-LWC FC-3/FS-3 + MAK-RWC MS-9 + MAK-CEC OM-3, consolidated at the pixel layer *(new as face law)*.

### HR-3 (MUST)
**Statement:** Every displayed recommendation exposes its full argument tree within one interaction at criterion granularity, with qualifier adjacent to claim (MAK-FFC CF-2, carried); graded criteria show degree and the ratified cut applied (MAK-LWC FC-1); envelope status renders with weight parity to the recommendation itself (MAK-RWC MC-1); and applicable confirmed rebuttals render within one interaction (MC-5). No claim renders without its uncertainty, its fit, and its known failures reachable.
**Rationale trace:** MAK-FFC CF-2 + MAK-LWC FC-1 + MAK-RWC MC-1/MC-5, consolidated; Spitzer 2026; REG-KEEP-002.

### HR-4 (MUST)
**Statement:** Verdict fidelity: the face renders exactly the evaluator's verdict class — released content as content; flagged content only through the fit-judgment flow (HA-4); held content never, in any preview or digest. Stage traces render on demand in the clinical register ("why am I seeing this / why is this flagged").
**Rationale trace:** MAK-CEC RG-1/2; MAK-RWC ME-1 flagged path; *(new — verdict fidelity stated for the face)*.

### HR-5 (MUST)
**Statement:** Rendering meets the accessibility floor: never color-only encodings (MAK-LWC FC-5, carried, extended to all five signal identities), legible at the minimum supported display, WCAG-conformant, and functional in the low-resource profile. Microcopy is linted against the prohibited-vocabulary list — no confidence/probability vocabulary for μ or fit (MAK-LWC FC-6 extended).
**Rationale trace:** MAK-LWC FC-5/FC-6 (carried, extended); MAK-FFC PF-6 floor; MX-3.

### HR-6 (SHOULD)
**Statement:** The self-description panel (MAK-RWC MS-6) is reachable from every screen: current envelopes, recent remodeling affecting this encounter's templates, confirmed findings, and drift notices, rendered in the clinical register from fabric data.
**Rationale trace:** MAK-RWC MS-6/MC-5; trust-calibration support.

## Part 4 — Clinical acts

**What the research revealed.** The face's writes are few, consequential, and all evidentiary: sign-off, deviation, gap report, conflict navigation. The GAAM lineage gives deviation its data structure; the right wing gives gap its sibling structure and insists the two never blur; REG-KEEP-003 makes sign-off fail-closed; and Bayor's evidence makes friction the enemy — an act that is punished by workflow will simply not be recorded, and the fabric goes blind exactly where it matters.

### Clinical-act requirements

### HA-1 (MUST)
**Statement:** Human sign-off is the face's terminal act and is fail-closed (REG-KEEP-003): no recommendation becomes an order, prescription, referral, or patient-visible diagnostic statement without an attributed clinician sign-off recorded in the fabric with the argument version signed. Absent sign-off, the default state is no action — the system never acts on timeout, inactivity, or implied consent.
**Rationale trace:** REG-POSTURE REG-KEEP-003; MAK-FFC CF anti-requirement (never auto-act), elevated to a requirement *(new as explicit act)*; MAK-FFC PF-8.

### HA-2 (MUST)
**Statement:** The Deviation Composer holds the friction law (MAK-FFC CF-3, carried): one interaction to open, structured reason plus optional free text, explicit preview of the auditor-face appearance, no dark patterns. Borderline flags (MAK-LWC FC-2) offer the composer directly; deviation on a flagged borderline case carries the boundary context automatically.
**Rationale trace:** MAK-FFC CF-3/SPINE-8 (carried); MAK-LWC FC-2; GAAM.

### HA-3 (MUST)
**Statement:** The Gap Reporter is one interaction from any screen, pre-populated with the element in focus, never gated on workflow completion (MAK-RWC MC-2, carried); the face renders the deviate-versus-gap distinction plainly, and a single case can carry both acts.
**Rationale trace:** MAK-RWC MC-2/MS-2 (carried); Bayor rigidity findings.

### HA-4 (MUST)
**Statement:** The fit-judgment flow governs flagged content: out-of-envelope or envelope-unknown verdicts render with the mismatch named; proceeding requires a recorded fit-judgment (MAK-RWC MS-7) captured in the same interaction pattern as deviation — one interaction, structured basis, fabric entry. Fit-judgments are never punished by friction or follow-up burden.
**Rationale trace:** MAK-RWC ME-1/MC-1/MS-7; MAK-CEC RG-1 stage 5.

### HA-5 (MUST)
**Statement:** Conflict navigation is a recorded act: when ConflictRecords render (side-by-side per MAK-RWC MC-4), the clinician's choice, reasons, and residue enter the fabric as a meta-rational act; the face never pre-ranks the sides, and graded applicability from the left wing renders per HR-2 where available.
**Rationale trace:** MAK-RWC MC-4/MS-5/MS-7; MAK-FFC SPINE-6; MAK-MIF beat 4.

### HA-6 (MUST)
**Statement:** Boundary work is captured, not corrected: free text, "other" selections, and workarounds are preserved verbatim, rendered downstream, and counted in circumrational telemetry (MAK-RWC MC-3, carried); the face treats none of them as validation errors.
**Rationale trace:** MAK-RWC MC-3/MS-3 (carried); Chapman circumrational work.

## Part 5 — Attention governance

**What the research revealed.** Alert fatigue is the best-documented CDSS killer (Bayor; Kesselheim via Miah 2020), and the consolidated face now has four interruption classes where the host corpus had one: alerts (CF-4/5), borderline flags (FC-2), meta-prompts (MC-6), and fit warnings (MC-1/HA-4). Governed separately, each is defensible; delivered together, they are a wall of noise. The consolidation duty is a single attention economy.

### Attention-governance requirements

### HG-1 (MUST)
**Statement:** One attention budget governs all interruption classes: alerts, borderline flags, meta-prompts, and fit warnings share a per-encounter and per-clinician interruption budget with ratified class weights; budget spend is fabric-visible telemetry (HE-4). Introducing a new interruption class or raising a class weight is a governed change (MS-4), never a product decision alone.
**Rationale trace:** MAK-FFC CF-5 suppression-budget pattern + MAK-LWC FC-2 + MAK-RWC MC-6, unified *(new as one economy)*; alert-fatigue evidence.

### HG-2 (MUST)
**Statement:** Hard stops remain reserved for the deterministic safety class (MAK-FFC CF-4, carried): arithmetic contraindication with ratified GenericArgument backing; everything else — including every fit warning and borderline flag — is advisory and dismissible. Every hard-stop firing is an argument in the fabric, reviewable and contestable.
**Rationale trace:** MAK-FFC CF-4 (carried); Croskerry boundary; MAK-LWC anti-requirement (flags invite, never gatekeep).

### HG-3 (MUST)
**Statement:** Suppression stays governed (MAK-FFC CF-5, carried): suppression rules are ratified GenericArguments, versioned, logged, budgeted; silent unlogged suppression is prohibited. Meta-prompt rules (MAK-RWC MC-6) are governed under the same machinery.
**Rationale trace:** MAK-FFC CF-5 (carried); MAK-RWC MC-6.

### HG-4 (SHOULD)
**Statement:** Interruption classes are evidence-gated by construction: an interruption fires only on a fabric-grounded trigger (threshold band entry, active applicable rebuttal, envelope mismatch, live conflict) — never on schedule, engagement, or completion-rate motives.
**Rationale trace:** MAK-RWC MC-6 gating generalized; MAK-RWC MA-3 Goodhart guard (completion metrics as hazard).

### HG-5 (SHOULD)
**Statement:** The face exposes per-clinician interruption analytics to the clinician themself (their own budget spend, their suppression rules in force) — the same lens discipline the auditor face observes (AF-8): the observed can see what the system does to their attention.
**Rationale trace:** MAK-FFC AF-8 symmetry; surveillance-anxiety evidence; procedural fairness.

## Part 6 — Team modes

**What the research revealed.** Stranieri's MDT and ward-round studies establish that consequential decisions are often collective, narrative, and disagreement-bearing; the Delphi literature warns that consensus and accuracy diverge; the left wing adds the mathematics of held disagreement (type-2 bands when a community cannot agree a point); the host corpus mandates multi-author arguments that never present false unanimity.

### Team-mode requirements

### HT-1 (MUST)
**Statement:** Group decisions are captured as multi-author actual arguments (MAK-FFC CF-6, elevated): participants contribute grounds and warrants under their own identity; residual disagreement is recorded as disagreement; the face never renders a group output as unanimous when the fabric knows otherwise.
**Rationale trace:** MAK-FFC CF-6 (elevated to MUST at the consolidated face); Stranieri MDT 2016; Delphi caution.

### HT-2 (SHOULD)
**Statement:** Where ratified meanings carry community bands (MAK-LWC FE-7 type-2 artifacts), team views render the band honestly — the spread of meanings, not a false point — and individual assessments locate within it.
**Rationale trace:** MAK-LWC FE-7; MAK-MIF beat 5; honest-disagreement doctrine.

### HT-3 (MUST)
**Statement:** Conflict navigation in group mode preserves per-author positions: each participant's stance on a ConflictRecord is attributable; the recorded navigation (HA-5) names the deciding rationale and the dissent that remains.
**Rationale trace:** HA-5; HT-1; MAK-RWC MS-5/MS-7.

### HT-4 (MAY)
**Statement:** Asynchronous team modes (case queued for specialist input, low-resource tele-consultation) may extend the group machinery across time and sites, provided every contribution carries identity, register, and pins, and the low-resource profile's offline discipline holds.
**Rationale trace:** MAK-FFC XC-3; Anidra-class field reality; HT-1 machinery reused.

## Part 7 — Evaluation, telemetry & consolidation maps

### Evaluation and telemetry requirements

### HE-1 (MUST)
**Statement:** Face evaluation runs the consolidated program: independent evaluators (never co-designers, n materially greater than the design panel — MAK-FFC CF-7 carried), measuring at minimum justified-override rate, alert PPV, time-in-consult delta, argument comprehension (CF-7); graded-chip comprehension, borderline-flag utility, μ-misreading rate under a ratified ceiling (MAK-LWC FC-7); gap-report rate and disposition, reliance calibration in- versus out-of-envelope, conflict-navigation quality (MAK-RWC MC-7); and five-signal conflation rate *(new — the OM-3 discipline's face-level measure)*.
**Rationale trace:** MAK-FFC CF-7 + MAK-LWC FC-7 + MAK-RWC MC-7, consolidated; the n=2 anti-pattern.

### HE-2 (MUST)
**Statement:** Face telemetry flows under the unified schema (MAK-CEC RG-5): interruption-budget spend by class, act latencies (time-to-deviate, time-to-gap-report), drill-down depth distributions, and brief reading-budget adherence — auditor system lens only, never individual performance surfacing without MA-6's governed process.
**Rationale trace:** MAK-CEC RG-5; MAK-RWC MA-6; AF-8 discipline.

### HE-3 (SHOULD)
**Statement:** Rendering changes to signal identities, argument layouts, or interruption classes ship behind evaluation: a change that could alter comprehension or reliance runs an HE-1-class measure (or a ratified proxy) before full release.
**Rationale trace:** Abbas 2025 (unvalidated explanation is liability); HE-1 machinery reuse.

### HE-4 (MUST)
**Statement:** The face's conformance suite gates its releases: one-surface negative tests (no side-channel data path renders — HR-1), verdict-fidelity tests (held content unreachable — HR-4), signal-identity lint (HR-2/HR-5), act-record completeness (every Part 4 act writes its fabric entry), and budget enforcement (HG-1). Results are conformity-file artifacts.
**Rationale trace:** MAK-CEC RG-8 pattern at the face; REG-KEEP-002 evidence posture *(new)*.

### Clinician Face anti-requirements (consolidated)

- Never a bare probability, score, or ranking without argument, qualifier, and fit reachable (MAK-FFC, carried).
- Never auto-act, auto-order, or act-on-timeout — sign-off is fail-closed (HA-1).
- Never a blended "overall confidence" across the five signals, and never a traffic-light metaphor for μ or fit (MAK-LWC + MAK-RWC, carried).
- Never punish deviation, gap reporting, or fit-judgment with friction, nagging, or metric consequence (all three hosts, carried; MA-6).
- Never surface auditor-face analytics, league tables, or peer comparisons inside this face (MAK-FFC, carried).
- Never let a digest, preview, or notification render held or pre-verdict content (HR-4).

### Three-corpus consolidation map (complete for the clinician face)

| Source requirement | Disposition here | Carrier |
|---|---|---|
| MAK-FFC CF-1 (workflow placement) | carried | HW-1 |
| MAK-FFC CF-2 (argument in one interaction) | consolidated | HR-3 |
| MAK-FFC CF-3 (deviation friction law) | carried | HA-2 |
| MAK-FFC CF-4 (hard-stop class) | carried | HG-2 |
| MAK-FFC CF-5 (governed suppression) | carried | HG-3 |
| MAK-FFC CF-6 (multi-author group capture) | elevated (SHOULD→MUST at this face) | HT-1 |
| MAK-FFC CF-7 (independent evaluation) | consolidated | HE-1 |
| MAK-FFC CF-8 (narrative summaries) | carried | HW-4 |
| MAK-LWC FC-1 (graded rendering + ratified cut) | consolidated | HR-3 |
| MAK-LWC FC-2 (borderline flag) | consolidated | HA-2, HG-1 |
| MAK-LWC FC-3 (channel separation) | extended to five signals | HR-2 |
| MAK-LWC FC-4 (ratified trend descriptors) | carried | HW-2, HW-4 |
| MAK-LWC FC-5 (accessibility of encodings) | carried, extended | HR-5 |
| MAK-LWC FC-6 (honest microcopy, lint) | carried, extended | HR-5 |
| MAK-LWC FC-7 (fuzzy evaluation measures) | consolidated | HE-1 |
| MAK-RWC MC-1 (envelope weight parity) | consolidated | HR-3, HA-4 |
| MAK-RWC MC-2 (gap reporting) | carried | HA-3 |
| MAK-RWC MC-3 (boundary work legitimate) | carried | HA-6 |
| MAK-RWC MC-4 (conflict workbench) | consolidated | HA-5, HT-3 |
| MAK-RWC MC-5 (system argues against itself) | consolidated | HR-3, HR-6 |
| MAK-RWC MC-6 (evidence-gated meta-prompts) | consolidated | HG-1, HG-3, HG-4 |
| MAK-RWC MC-7 (meta-rational evaluation) | consolidated | HE-1 |

### MAK-MIF beat map (face landings)

| Beat | Face landing | Carrier |
|---|---|---|
| 1 · The borderline patient | Borderline flag + fit-judgment flow, one interaction each | HA-2, HA-4 |
| 2 · The full translation loop | Boundary work captured; encoding traces reachable in drill-down | HA-6, HR-3 |
| 4 · Conflict with a metric | Side-by-side conflicts, graded applicability shown, navigation recorded | HA-5 |
| 5 · Disagreement held, not averaged | Multi-author capture; band views; dissent preserved | HT-1..3 |

### Findings → requirements

| Finding | Source | Requirements it drives |
|---|---|---|
| Capture-before-consult makes encounters patient-driven; assimilable briefs work | Blake 2014/2016 | HW-1..3 |
| Workflow mismatch, overload, prompt fatigue, trust collapse, surveillance anxiety | Bayor 2025 | HW-3, HG-1..5, HE-2, anti-requirements |
| Reasoning-shaped explanation improves accuracy; bare outputs do not | Spitzer 2026; Nunes & Jannach 2017 | HR-3 |
| Unvalidated explanation is liability | Abbas 2025 | HE-1, HE-3 |
| Binary chrome hides boundary cases; graded display is reasoning-shaped | MAK-LWC cliff evidence; Seising lineage | HR-2/3, HA-2 |
| Reference-class transparency is the trust mechanism and the glass-box demand | MAK-RWC MC-1; REG-FIND-004 | HR-3, HA-4 |
| Collective decisions are narrative and disagreement-bearing; consensus ≠ accuracy | Stranieri ward rounds/MDT; Delphi (TFSC 2011) | HT-1..4 |
| Sign-off must be human and fail-closed regardless of pathway | REG-POSTURE REG-KEEP-003 | HA-1 |
| Reviewable basis is the product thesis | REG-POSTURE REG-KEEP-002 | HR-1/3/4, HE-4 |

### Sources

- Series: MAK-FFC v1.1 Part 3 · MAK-LWC v1.1 Part 3 · MAK-RWC v1.1 Part 3 · MAK-CEC v1.1 (verdict stream and signal registry) · MAK-MIF v1.0 · REG-POSTURE v1.0 (REG-KEEP-002/003; cited by stable ID).
- Blake & Kerr 2014 (Decision Analytics); Blake, Kerr & Gammack 2016 (Information Systems 56); Miah, Blake & Kerr 2020 (AJIS 24).
- Bayor et al. 2025 (JMIR 27:e63733); Abbas, Jeong & Lee 2025 (Healthcare 13:2154); Spitzer et al. 2026 (npj Digital Medicine RCT); Nunes & Jannach 2017 (UMUAI).
- Stranieri corpus: ward rounds (BMC HSR 2018), MDT (JDS 2016), GAAM (DSS 2006); Delphi accuracy-vs-consensus (TFSC 2011) — provenance in The Stranieri File.
- Kesselheim et al. 2011 (alert fatigue and litigation, via Miah 2020); Croskerry dual-process boundary (via the Blake program).

*Document footer (source artifact):* The Head Corpus v1.0 · requirement IDs are stable; propose changes as argued deviations — this document practices its own doctrine. Compiled from the three host corpora and MAK-CEC read in full, REG-POSTURE v1.0, and the series' verified evidence base, 1 Sep 2026.

## Part 8 — Execution sourcing annex

The face's integration substrate is standards-shaped and verifiable; its distinctive components are builds. Entries below verified by direct fetch 2026-09-01; carried entries cite their host annexes. Verdict vocabulary per MAK-ELSM.

### Verified entries (this face's pass)

| ID | Repo / artifact | What it gives you | Status (verified 2026-09-01) | Verdict | Serves |
|---|---|---|---|---|---|
| ELSM-H01 | [CDS Hooks](https://cds-hooks.org) + [cds-hooks/sandbox](https://github.com/cds-hooks/sandbox) | The HL7 standard for injecting decision-support cards into EHR workflows at hook points (patient-view, order-select…) — the deployment vector for HW-1's read-and-decide placement inside third-party EHRs; sandbox for integration testing | Sandbox: 40★ · Apache-2.0 · active | ADOPT (standard) / ADAPT (card content must carry argument links, not naked text) | HW-1, HR-1 |
| ELSM-H02 | [smart-on-fhir/client-js](https://github.com/smart-on-fhir/client-js) | SMART App Launch client: EHR-embedded app authentication and FHIR access — the face-as-SMART-app integration path | 350★ · Apache-2.0 · v2.6.3 Sep 2025 · active | ADOPT | HW-1, HW-5 |
| ELSM-H03 | [openmrs/openmrs-esm-core](https://github.com/openmrs/openmrs-esm-core) | OpenMRS 3.0 frontend framework (modular ESM microfrontends) — the maintained open-source EHR frontend with LMIC deployment reality; a host candidate and design mine for the low-resource clinician face | 89★ · open source · v10.0.0 Jun 2026 · active | STUDY / ADAPT (host integration) | HW-5, XC-3 |

### Carried entries (host annexes)

- Data and workflow substrate: HAPI FHIR (ELSM-20), clinical-reasoning $apply (ELSM-02) — the face's server side; verdicts carried from MAK-ELSM.
- Offline-first delivery: android-fhir (ELSM-04), opensrp/fhircore (ELSM-05) — HW-5's vehicle; carried.
- Rendering-law inputs: the verdict stream and stage traces are MAK-CEC RG-1/2 builds; the five-signal schema is MAK-CEC OM-3.

### The face's build list (no precedent found; methodology hedge carried)

The argument renderer at criterion grain with five typed signal identities (HR-2/3); the Deviation Composer, Gap Reporter, and fit-judgment flow as one-interaction recorded acts (HA-2..4); the unified attention budget across four interruption classes (HG-1); the Consult-Prep composer as a fabric projection under a reading budget (HW-2/3). CDS Hooks cards, SMART apps, and OpenMRS frontends supply delivery vectors — none supplies the acts, the budget, or the rendering law.

### Face-relevant research plane (carried)

Spitzer et al. 2026 (argument-shaped explanation RCT — the rendering direction); Bayor et al. 2025 (the failure catalogue HG exists to avoid); MAK-RWC Part 9's monitoring literature (reliance-calibration measurement candidates for HE-1). The open questions specific to this face — μ-literacy, five-signal conflation rates, gap-report elicitation quality — remain unmeasured in the literature; HE-1 produces the first evidence.

## Appendix A — ID census (additive)

Authoritative enumeration for validator checks. Count: **30**.

```json
{
  "doc_id": "MAK-HDC",
  "version": "1.0",
  "requirements": {
    "HW": ["HW-1","HW-2","HW-3","HW-4","HW-5"],
    "HR": ["HR-1","HR-2","HR-3","HR-4","HR-5","HR-6"],
    "HA": ["HA-1","HA-2","HA-3","HA-4","HA-5","HA-6"],
    "HG": ["HG-1","HG-2","HG-3","HG-4","HG-5"],
    "HT": ["HT-1","HT-2","HT-3","HT-4"],
    "HE": ["HE-1","HE-2","HE-3","HE-4"]
  },
  "levels": {
    "MUST":   ["HW-1","HW-2","HW-3","HW-5","HR-1","HR-2","HR-3","HR-4","HR-5","HA-1","HA-2","HA-3","HA-4","HA-5","HA-6","HG-1","HG-2","HG-3","HT-1","HT-3","HE-1","HE-2","HE-4"],
    "SHOULD": ["HW-4","HR-6","HG-4","HG-5","HT-2","HE-3"],
    "MAY":    ["HT-4"]
  },
  "retired": []
}
```

Census arithmetic: 23 MUST + 6 SHOULD + 1 MAY = 30.

## Appendix B — Self-audit checks (additive)

1. **ID uniqueness** — no requirement ID appears in more than one requirement header.
2. **ID census parity** — headers matching `^### (HW|HR|HA|HG|HT|HE)-\d+ \((MUST|SHOULD|MAY)\)$` exactly equal Appendix A (30).
3. **Level parity** — header levels match Appendix A buckets.
4. **Trace presence** — every requirement block has a non-empty rationale trace.
5. **Normative leakage** — no capitalized MUST/SHOULD/MAY outside requirement blocks, anti-requirement bullets, quoted text, or this appendix.
6. **Consolidation integrity** — every CF/FC/MC requirement of the three hosts appears in the Part 7 map with a disposition; no source requirement is relaxed (elevation is permitted and named).
7. **Cross-reference integrity** — every HW/HR/HA/HG/HT/HE ID cited exists in the census; every host-document ID cited resolves in its host.
8. **Regulatory precedence** — REG-KEEP-002/003 are honoured; no statement contradicts a REG-FIND; ASSUME-REG items never described as closed.
9. **Table integrity** — consistent column counts per row.
10. **Stability** — IDs from previous versions present or explicitly retired; never reused.
