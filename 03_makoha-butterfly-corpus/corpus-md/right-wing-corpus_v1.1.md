---
doc_id: MAK-RWC
title: "The Right Wing Corpus"
version: "1.1"
date: "2026-09-01"
series: "Mākoha research series — volume 8 · sibling to MAK-LWC · operationalizes the right wing of MAK-MIF"
status: normative-draft
normative_language: RFC-2119 (MUST / SHOULD / MAY)
req_prefixes: [MS, MC, MP, MA, ME, MX]
req_count: 42
subordinate_to: "MAK-FFC v1.1 — no requirement here relaxes a corpus MUST; narrowings and extensions are explicit"
folds_in:
  - "MAK-FFC v1.1 (The Four Faces Corpus) — complete absorption/refinement map in Part 8; all 46 SPINE/CF/PF/AF/EN/XC IDs mapped to their right-wing operationalization"
  - "MAK-ELSM v1.1 (Execution Layer Sourcing Map) — folded as Part 9 execution sourcing annex, all 23 entries carried with verdicts and J-3 dispositions"
governed_by:
  - "REG-POSTURE v1.0 (Mākoha Regulatory Posture) — this corpus adopts the assume-inclusion posture; divergences from MAK-FFC XC-1/XC-2's earlier framing are flagged, never silent (Part 7)"
changelog:
  - "v1.1 (2026-09-01): additive — Part 9 refresh pass: carried statuses spot-re-verified (2026-09-01), four new sourcing entries (ELSM-R01..R04), regulatory-instrument rows (FDA PCCP final guidance; TGA AI guidance 22 Apr 2026), 2025+ deployment-monitoring research plane, Appendix C register, self-audit check 11. No v1.0 content altered or removed."
  - "v1.0 (2026-09-01): initial release — 42 requirements across MS/MC/MP/MA/ME/MX; MAK-FFC v1.1 fold-in map (Part 8); MAK-ELSM v1.1 folded as Part 9; REG-POSTURE update layer (Part 7)."
companions:
  - "MAK-FFC v1.1 (host architecture; all SPINE/CF/PF/AF/EN/XC/GPP IDs resolve there)"
  - "MAK-LWC v1.1 (sibling wing; FS/FC/FP/FA/FE/FX IDs resolve there)"
  - "MAK-MIF v1.0 (the eight beats; this corpus operationalizes each beat's right-wing contribution)"
  - "MAK-ELSM v1.1 (sourcing vocabulary; folded here as Part 9)"
  - "REG-POSTURE v1.0 (governing regulatory document; REG-FIND / REG-KEEP / FORK-REG / GATE / ASSUME-REG IDs resolve there)"
artifact_url: "https://claude.ai/code/artifact/7a81e9b0-da68-43d1-af5e-5d72e5f8f125"
change_policy: "Requirement IDs are stable; retired IDs never reused. Propose changes as argued deviations."
---

<!-- LLM USAGE CONTRACT (additive; not part of the source document)
1. Requirement blocks (### MS-n / MC-n / MP-n / MA-n / ME-n / MX-n) are NORMATIVE;
   all other prose is INFORMATIVE. Part 9 is an informative sourcing annex.
2. Family-name discipline: MC/MP/MA here are META-RATIONAL-scoped face families and
   never collide with or substitute for MAK-FFC's CF/PF/AF or MAK-LWC's FC/FP/FA.
   Cite with the doc prefix when ambiguity is possible ("MAK-RWC MC-1").
3. The routing rule (MS-9) binds generation: never present an ontology-fit problem
   as a degree problem or vice versa; never resolve a materialized conflict, a gap
   report, or a remodeling proposal by generation — those are governed human acts.
4. REG-POSTURE v1.0 governs regulatory content. Where this corpus restates MAK-FFC
   regulatory text, the Part 7 update notes prevail. ASSUME-REG-* items close only
   by written external attestation — an LLM must never mark one closed.
5. MUST violations in generated designs/code/documents require an explicit
   DEVIATION notice naming the ID.
6. Appendix A's ID census is authoritative for validator checks; Appendix B's
   self-audit checks gate any edit of this file.
7. Part 9 statuses are dated observations; re-verify before dependency decisions.
END LLM USAGE CONTRACT -->

# The Right Wing Corpus

A translatable research primer and execution manual for the meta-rational layer of the triple-facing CDSS — the judgment-of-systems spine, its expression in the Clinician, Patient, and Auditor faces, and its engine-plane machinery — folding in the Four Faces Corpus and the Execution Layer Sourcing Map, and carrying the revised regulatory posture as governing context.

**Document metadata:** Technical corpus · v1.1 · 1 Sep 2026 · eighth volume in the Mākoha research series · sibling to MAK-LWC · STATUS: normative draft · REQ IDS: MS · MC · MP · MA · ME · MX · SUBORDINATE TO: MAK-FFC v1.1 · FOLDS IN: MAK-FFC v1.1 (Part 8) · MAK-ELSM v1.1 (Part 9) · GOVERNED BY: REG-POSTURE v1.0.

## Contents

1. [Part 0 — How to use this document](#part-0--how-to-use-this-document)
2. [Part 1 — Foundation: meta-rationality operationalized](#part-1--foundation-meta-rationality-operationalized)
3. [Part 2 — The Meta-rational Spine](#part-2--the-meta-rational-spine)
4. [Part 3 — The Clinician Face](#part-3--the-clinician-face)
5. [Part 4 — The Patient Face](#part-4--the-patient-face)
6. [Part 5 — The Auditor Face](#part-5--the-auditor-face)
7. [Part 6 — The Engines](#part-6--the-engines)
8. [Part 7 — Cross-cutting execution: the regulatory update layer, low-resource profile, phasing, risks](#part-7--cross-cutting-execution)
9. [Part 8 — Fold-in maps & traceability: MAK-FFC absorption, MAK-MIF beats, sources](#part-8--fold-in-maps--traceability)
10. [Part 9 — Execution sourcing annex (folded from MAK-ELSM v1.1)](#part-9--execution-sourcing-annex)
11. [Appendix A — ID census](#appendix-a--id-census-additive)
12. [Appendix B — Self-audit checks](#appendix-b--self-audit-checks-additive)

## Thesis

> The Four Faces Corpus built the body: a justification fabric where every claim is an argument, three faces reading one truth in three registers, engines that propose but never release. What it left partly informal is the wing that made it possible — the *judgment of systems* that decides when a formal system fits the case in front of it, notices when the ontology has run out, changes the ontology without losing the audit trail, and holds multiple systems side by side without pretending they agree. Chapman names this competence meta-rationality and shows it is not itself a rational procedure — it cannot be computerized. But it can be *instrumented, supported, and governed*: the system can know its own envelope, invite the report that the map has failed, route that report into a governed remodeling lifecycle, and record every meta-rational act with the same evidentiary discipline as every rational one. This corpus turns the right wing from a temperament into requirements. Its sharpest consequence is regulatory: the revised posture (REG-POSTURE v1.0) found that Mākoha's diagnostic function forecloses the CDSS exemption regardless of determinism — the glass-box test is a *systems-judgment* test, and this corpus is where the architecture meets it honestly.

## Part 0 — How to use this document

This corpus is both a *primer* (why each commitment exists, with citations) and an *execution manual* (requirements you can build, test, and audit against). It is the right-wing sibling of MAK-LWC: where the Left Wing Corpus governs the semantics of degree *inside* a fixed ontology, this corpus governs the fit, change, and plurality of ontologies themselves. Both wings beat against the same body — the MAK-FFC spine — and neither replaces it.

- **Normative language.** MUST = conformance-defining; SHOULD = strong default, departure requires recorded justification; MAY = permitted design freedom.
- **Requirement IDs.** `MS-n` meta-rational spine; `MC-n` Clinician Face; `MP-n` Patient Face; `MA-n` Auditor Face; `ME-n` Engines; `MX-n` cross-cutting. IDs are stable; retired IDs never reused.
- **Fold-in discipline.** This corpus *hosts* MAK-FFC v1.1 rather than restating it: Part 8 maps every FFC requirement to its right-wing operationalization, and Part 9 carries the full MAK-ELSM v1.1 sourcing record. Where a requirement here extends an FFC requirement, the extension is named in the statement; absence of an extension note means the FFC requirement applies unmodified.
- **Regulatory precedence.** REG-POSTURE v1.0 governs. MAK-FFC XC-1/XC-2 were drafted before its findings; Part 7 carries the update notes. Nothing in this corpus reopens a REG-FIND without the attestation route REG-POSTURE itself specifies (ASSUME-REG-002).
- **Scope.** Architecture and component behaviour. Implementation technology is referenced as reasonable default, never constraint.

## Part 1 — Foundation: meta-rationality operationalized

Chapman's account gives meta-rationality a precise shape: rationality operates *within* a formal system — an ontology, an inference method, a criterion of correctness — while meta-rationality is the competence exercised *about* systems: choosing which system applies, judging how well its ontology fits the nebulous situation at hand, repairing or remodeling the ontology when it fails, coordinating multiple systems that each capture part of the truth, and knowing when to stop trusting formal output altogether. Three of his observations do the load-bearing work for a CDSS architecture.

**First, meta-rationality cannot be computerized — but its occasions can be detected and its acts can be recorded.** No algorithm decides whether an ontology fits, because fit is judged against a world that exceeds every ontology (nebulosity). What a system *can* do is know the envelope inside which its formalisms were validated, notice signals that a case is outside it, hand the judgment to a human with the evidence arranged, and treat the human's judgment as data. The design consequence is a standing division of labour: the system computerizes envelope-checking, gap detection, conflict materialization, and remodeling bookkeeping; humans supply the judgment those mechanisms exist to serve. This is MAK-FFC's "computerize criteria, never discretion" doctrine, extended one level up: *computerize the occasions of meta-rational judgment, never the judgment.*

**Second, ontological remodeling is real work with a lifecycle, not an exception.** Medicine remodels constantly — disease categories split, instruments are revalidated, thresholds move. The failure mode the sleep-CDSS lineage documented (the ICSD-2 freeze) is remodeling *denied*: the formal system fossilizes while practice moves. The failure mode Chapman warns against is remodeling *unaccountable*: meaning changes silently and old decisions become uninterpretable. The design answer is a governed lifecycle — detect, propose, deliberate, ratify, version, replay — that MAK-FFC sketched in AF-5 and this corpus specifies as the spine's central workflow (MS-4).

**Third, rationality theater is the standing adversary of any system that rewards the appearance of rationality.** Where compliance is scored, justifications become boilerplate; where metrics are targets, they stop measuring (Goodhart). MAK-FFC armed the auditor face against justification theater (AF-4); this corpus generalizes the guard to the meta-level: metrics themselves are versioned, argued artifacts, and gaming detection watches the watchers (MA-3).

The empirical anchors are unchanged from the series: Bayor et al.'s 37-of-40 clinician-only systems failing at the circumrational boundary; Cockburn et al.'s transfer failures as nebulosity in epidemiological form; Abbas et al.'s unvalidated explanation theater; the Miah–Blake–Kerr program honestly stopping at the judgment boundary; Stranieri's GAAM giving deviation a data structure. What is new since MAK-FFC v1.0 is the regulatory finding: REG-FIND-003 and REG-FIND-004 establish that *opacity is independent of machine learning* and the transparency test is "glass box" — the clinician must be able to see and review the internal logic, which a published named instrument satisfies and a novel composite computation does not. That is a meta-rationality test stated in regulatory language: the regulator is asking whether the clinician can exercise systems-judgment over the tool. The right wing is therefore not an optional refinement; under the assume-inclusion posture it is part of the Essential Principles case (REG-KEEP-002).

**Four working definitions** (used normatively throughout):

- **Applicability envelope.** The recorded population, context, validation status, and known gaps within which a formal element (instrument, guideline, model, codebook, claim type) has warrant. Envelopes are data, not prose.
- **Gap report (nebulosity flag).** A first-class fabric object asserting that the ontology does not fit a case — distinct from a deviation, which departs from a warrant *within* a fitting ontology.
- **Remodeling.** Any change to the ontology layer: instrument versions, category splits, new claim types, value-mapping ratifications, codebook changes (the left wing's FS-5 path is one instance).
- **Trading zone.** A designed interface where communities with different ontologies coordinate through shared boundary objects — the three registers are the built-in instance; governance forums are the institutional one.

> The doctrine in one sentence: the system cannot judge its own fit — so it must make the judgment of fit easy, evidenced, recorded, and consequential.

## Part 2 — The Meta-rational Spine

The meta-rational spine is a set of cross-face capabilities layered onto the MAK-FFC justification fabric. Nothing here forks the fabric: gap reports, envelopes, remodeling proposals, and conflict records are fabric entries with the same append-only, version-pinned, argued discipline as clinical claims (SPINE-4/5). The spine's job is to make the boundary — where the formal system meets the nebulous patient — a designed, instrumented, two-way crossing rather than an accident zone.

### The meta-rational spine (layered)

```text
┌──────────────────┬──────────────────────┬───────────────────────────────┐
│  Clinician Face  │    Patient Face      │  Auditor Face                 │
│  envelope render │    "does this fit    │  remodeling ledger ·          │
│  gap report ·    │    you?" · gap       │  gap analytics ·              │
│  conflict bench  │    report · values   │  Goodhart guard               │
└──────────────────┴──────────────────────┴───────────────────────────────┘
             ↓ ↑  meta-rational acts are fabric entries (MS-7)
┌──────────────────────────────────────────────────────────────────────────┐
│                    META-RATIONAL SPINE (this corpus)                     │
│  ApplicabilityEnvelope · GapReport · RemodelingProposal ·                │
│  ConflictRecord · TradingZoneArtifact · routing rules (MS-9)             │
└──────────────────────────────────────────────────────────────────────────┘
             ↓ ↑  hosted by, never forked from
┌──────────────────────────────────────────────────────────────────────────┐
│              JUSTIFICATION FABRIC (MAK-FFC SPINE-1..9)                   │
│  GenericArgument · ActualArgument · Deviation · append-only ledger       │
└──────────────────────────────────────────────────────────────────────────┘
             ↓ ↑
┌──────────────────────────────────────────────────────────────────────────┐
│  ENGINES (MAK-FFC EN-1..9) + envelope enforcement (ME-1) +               │
│  boundary-hunting corruption engine (ME-2) + remodeling replay (ME-5)    │
└──────────────────────────────────────────────────────────────────────────┘
```

### Spine requirements

### MS-1 (MUST)
**Statement:** Every formal element in the knowledge plane — instrument, guideline/GenericArgument lineage, model version, claim type, codebook (MAK-LWC FS-5 artifacts included) — carries a machine-readable ApplicabilityEnvelope: target population, validated context, validation status and evidence tier, known exclusions, and known gaps. An element without an envelope is not deployable; "envelope unknown" is a recordable state that renders as such, never as silent universality.
**Rationale trace:** Chapman (ontology fit is judged against a stated scope); REG-FIND-004 glass-box test (a named published instrument carries its own envelope); Blake 2014 instrument-gap finding (no OSA screen tuned to women); MAK-FFC PF-1.

### MS-2 (MUST)
**Statement:** The GapReport is a first-class fabric object: any authenticated face-side actor (clinician, patient, auditor) can attach "this does not fit" to any instrument item, rendered argument, category, or claim — with a structured locus (which element failed), free text, and author identity. Gap reports are distinct from Deviations (SPINE-8): a deviation departs from a warrant; a gap asserts the ontology itself has run out. Filing a gap report never blocks care and never requires resolution before proceeding.
**Rationale trace:** Chapman nebulosity (the world exceeds every ontology); Bayor rigidity findings ("restrict users from incorporating their own perspectives"); GAAM generic/actual split extended one level up.

### MS-3 (MUST)
**Statement:** Circumrational load is measured: the system instruments the translation work humans do at its boundary — override and deviation rates, free-text supplement volume, "other/none-of-these" selections, abandoned or partially completed instruments, re-entry loops, and workaround signatures — and publishes the telemetry to the auditor face's system lens (AF-8 discipline). Boundary friction is a monitored system property with an owner, not anecdote.
**Rationale trace:** Chapman circumrational work; Bayor workflow-mismatch catalogue; MAK-MIF beat 2 (the boundary as designed, instrumented crossing); MAK-FFC EN-9 telemetry pattern.

### MS-4 (MUST)
**Statement:** Ontological remodeling follows one governed lifecycle for every ontology-layer change: **detect** (gap analytics, deviation aggregates, drift telemetry, corruption findings) → **propose** (a RemodelingProposal carrying its evidence and affected element versions) → **deliberate** (the trading-zone forum for the affected communities, MS-8) → **ratify** (authorized, attributed, versioned) → **version** (old element retained, pinned to its historical decisions per SPINE-5) → **replay** (ME-5 divergence review). No stage is skippable; no ontology change takes effect by configuration, runtime learning, or edit-in-place. MAK-FFC AF-5 and PF-3 and MAK-LWC FS-5 ratifications are instances of this lifecycle, not parallel mechanisms.
**Rationale trace:** Chapman (remodeling is prior to rationality and cannot be done by the system's own rules); ICSD-2 freeze anti-pattern; MAK-FFC AF-5/PF-3; MAK-LWC governance path; SPINE-5.

### MS-5 (MUST)
**Statement:** Plural rational systems coordinate only through materialized artifacts: when co-resident systems (guidelines, terminologies, instruments, or the two wings' own outputs) yield conflicting applicable conclusions, the conflict is a ConflictRecord (DetectedIssue-bound per SPINE-6) carrying both sides' arguments and envelopes. The system MUST NOT resolve, rank, average, or suppress; a human's navigation of the conflict is recorded as a meta-rational act (MS-7). This extends SPINE-6 from guideline pairs to every system pair, including fuzzy-versus-crisp disagreements at the MAK-LWC boundary.
**Rationale trace:** Chapman (holding multiple systems is the meta-rational move); SPINE-6; MAK-MIF beats 4–5; Stranieri coalescing-systems line; Delphi accuracy-vs-consensus caution.

### MS-6 (MUST)
**Statement:** The system's own limits are queryable content: every face can answer, in its register, "what is this system validated for, what is it known to be bad at, and what has changed recently" — assembled from envelopes (MS-1), confirmed corruption findings (EN-5 rebuttals), drift telemetry, and the remodeling ledger. This self-description is generated from fabric data, version-pinned, and never hand-maintained marketing prose.
**Rationale trace:** Chapman reasoning-about-systems; REG-KEEP-002 (reviewable basis is the product thesis); Abbas 2025 (unvalidated explanation is a liability); trust-calibration literature via Bayor.

### MS-7 (MUST)
**Statement:** Meta-rational acts are ledgered with the same discipline as rational ones: gap reports, envelope changes, remodeling proposals and ratifications, conflict navigations, trust-override events ("clinician proceeded against an out-of-envelope warning"), and trading-zone decisions are all append-only, attributed, version-pinned fabric entries, renderable in all three registers per SPINE-3.
**Rationale trace:** SPINE-4/5 extended to the meta-level; auditor evidentiary needs (MA-1); the corpus's own doctrine (practice what you audit).

### MS-8 (SHOULD)
**Statement:** Trading zones are designed, not improvised: each cross-community interface (clinical governance forum, patient council, auditor/regulator interface, wing-coordination review) has a charter naming its participants, its boundary objects (which fabric artifacts it deliberates over), its register, and its authority (what it can ratify). Trading-zone outputs enter the fabric through MS-4, never informally.
**Rationale trace:** Galison via Chapman (trading zones); MAK-FFC AF-5 governance; MAK-LWC reasoning-community ratification; MP-6/MA-5 instances.

### MS-9 (MUST)
**Statement:** The wing-coordination contract: signals of *degree* (graded criterion fit, membership values, linguistic qualifiers — MAK-LWC's domain) and signals of *fit* (envelope mismatch, gap reports, OOD/atypicality findings — this corpus's domain) are typed distinctly, routed distinctly, and never substituted: a degree problem routes to the fuzzy layer's machinery (fuzzification, codebooks, CWW), a fit problem routes to judgment and the remodeling loop (MS-2/MS-4). Borderline-but-in-ontology cases render as degrees; out-of-ontology cases render as gaps; a case can be both, and then both render. Conflation in either direction is a schema violation.
**Rationale trace:** MAK-MIF beats 1–2 (the coordination that gives flight); MAK-LWC A1 axiom discipline as the sibling precedent; Chapman (vagueness and nebulosity are different failures of formalism).

## Part 3 — The Clinician Face

**What the research revealed.** The clinician is the system's resident meta-rationalist: the person who must judge, case by case, whether the formal apparatus fits the patient in front of them. Bayor et al.'s catalogue shows what happens when the face ignores this — rigid structures that "restrict users from incorporating their own perspectives," trust collapse when recommendations cannot be interrogated, workarounds that vanish from the record. The Blake program's boundary honesty (computerize ICSD criteria, cite Croskerry, leave discretion outside) was correct but incomplete: discretion left *outside* the system is discretion the system cannot support, evidence, or learn from. MAK-FFC brought discretion inside as the Deviation (SPINE-8); this face brings *fit-judgment* inside the same way — as envelope rendering, one-interaction gap reporting, and a conflict workbench — while guarding the line Croskerry drew: the system arranges the evidence for judgment; it never simulates the judgment.

### Component inventory

| Component | Function | Research anchor |
|---|---|---|
| Envelope Renderer | Every recommendation displays its ApplicabilityEnvelope against this patient: in-envelope, out-of-envelope (with the mismatching attributes named), or envelope-unknown | MS-1; REG-FIND-004 glass-box; reference-class transparency |
| Gap Reporter | One-interaction "this doesn't fit my patient" from any screen, pre-populated with the element in focus; distinct affordance from the Deviation Composer | MS-2; Bayor rigidity findings |
| Conflict Workbench | Side-by-side rendering of ConflictRecords: both arguments, both envelopes, graded applicability where the left wing supplies it; records the clinician's navigation | MS-5; MAK-MIF beat 4; SPINE-6 |
| Self-Description Panel | "What is this system bad at" on demand: confirmed rebuttals, drift notices, and envelope boundaries relevant to the current case | MS-6; trust calibration |
| Boundary-Work Capture | Free text, "other" categories, and workarounds captured as legitimate signals (MS-3 telemetry), never validation errors | Chapman circumrational work; Bayor workaround findings |
| Meta-Prompt Governor | Evidence-gated meta-rational prompts (envelope mismatch, active rebuttal, live conflict) — rare by construction, governed like alerts (CF-5) | Alert-fatigue evidence; anti-theater discipline |

### Clinician Face requirements

### MC-1 (MUST)
**Statement:** Every rendered recommendation displays its applicability status for the current patient — in-envelope, out-of-envelope with the mismatching attributes named, or envelope-unknown — computed from the ApplicabilityEnvelope (MS-1) against the patient's grounds. Out-of-envelope and envelope-unknown render with visual weight at least equal to the recommendation itself; the clinician sees the reference class before the advice.
**Rationale trace:** MS-1; REG-FIND-004 (the clinician must be able to review the basis); Cockburn transfer failures (context mismatch is the expected case); MAK-FFC CF-2 extended.

### MC-2 (MUST)
**Statement:** Gap reporting is one interaction from any screen, pre-populated with the element in focus, and never gated on completing the current workflow. The face renders the distinction plainly: *deviate* ("the rule fits but I am departing from it") versus *report a gap* ("the rule does not fit this patient") — and a single case can carry both.
**Rationale trace:** MS-2; SPINE-8/CF-3 friction discipline applied to the meta-level; GAAM warrant-level grain.

### MC-3 (MUST)
**Statement:** Boundary work is legitimate work: free-text supplements, "other/none-of-these" selections, and out-of-form annotations are captured, preserved, rendered to downstream readers, and counted in MS-3 telemetry. The face MUST NOT treat them as validation failures, block progression on them, or silently discard them.
**Rationale trace:** Chapman circumrational practice; Bayor ("restrict users from incorporating their own perspectives"); MP-5 symmetry.

### MC-4 (SHOULD)
**Statement:** The Conflict Workbench renders every live ConflictRecord side by side — both arguments at full Toulmin structure, both envelopes, graded applicability from the left wing where available — and supports recorded synthesis: the clinician's choice, its reasons, and its residue enter the fabric as a meta-rational act (MS-7). No default ordering implies a winner.
**Rationale trace:** MS-5; SPINE-6; MAK-MIF beat 4; Stranieri reasoning-communities.

### MC-5 (MUST)
**Statement:** The system argues against itself where evidence exists: confirmed corruption-engine findings (EN-5), drift notices, and envelope narrowings relevant to the current claim are renderable within one interaction of the claim, in the clinical register. Withholding an applicable known-failure finding from the point of decision is a conformance violation.
**Rationale trace:** MS-6; MAK-FFC SPINE-2 rebuttal mandate; MAK-MIF beat 7; Abbas (explanation must include limits, not just support).

### MC-6 (SHOULD)
**Statement:** Meta-rational prompts are evidence-gated and rare: the face prompts for fit-judgment only on envelope mismatch, active applicable rebuttal, or live conflict — never as routine "are you sure?" friction. Prompt rules are governed like alert-suppression rules (CF-5): ratified, versioned, logged, budgeted.
**Rationale trace:** alert-fatigue evidence (Bayor; Kesselheim via Miah 2020); rationality-theater risk; CF-5 governance pattern.

### MC-7 (MUST)
**Statement:** Face evaluation (extending CF-7) measures meta-rational outcomes: gap-report rate and downstream disposition, calibration of reliance (agreement rates in-envelope versus scrutiny rates out-of-envelope), conflict-navigation quality, and comprehension of envelope renderings — with evaluators who did not co-design the system.
**Rationale trace:** CF-7; trust-calibration literature via Bayor; the n=2 co-designer anti-pattern; MA-2 analytics dependency.

### Clinician Face anti-requirements

- Never simulate judgment: no component recommends *whether to trust* a recommendation; it renders the evidence for that judgment (Croskerry boundary, held).
- Never bury out-of-envelope status in drill-down while the recommendation renders at the surface (violates MC-1 weight parity).
- Never convert gap reports into workflow punishment — extra forms, mandatory review meetings, or metric penalties for the reporter (kills MS-2 at the root; see MA-6).
- Never let the Meta-Prompt Governor's rules accrete unsupervised (CF-5 discipline applies; silence and nagging are both failure modes).

## Part 4 — The Patient Face

**What the research revealed.** The patient stands at the steepest ontology gradient in the system: their lived situation must be translated into instruments and categories that were validated, at best, on people statistically like them — and at worst, on nobody like them (the Blake program's own instrument-gap finding: no OSA screen tuned to women). The 37-of-40 clinician-only norm means patient-side meta-rationality has essentially no precedent to copy; the nearest materials are the Blake intake-at-home patterns, Stranieri's custody doctrine, and MAK-FFC's values machinery (PF-3), which this corpus stages through the governed remodeling lifecycle. The face's meta-rational duties are honesty about fit ("this advice was tested on people in these groups — you are/are not in them"), an affordance to say "this does not describe me" that actually goes somewhere, and preservation of everything the ontology could not capture.

### Component inventory

| Component | Function | Research anchor |
|---|---|---|
| Fit Renderer (plain register) | "Was this tested on people like you?" — envelope status in plain language, honest in both directions | MS-1; MP-1; PF-2 register fidelity |
| Patient Gap Reporter | "This doesn't describe me" on every instrument item and rendered argument; routes to MS-2 with patient authorship | MS-2; instrument-gap finding; equity lens (MA-2) |
| Escape-Hatch Capture | Free-text and "none of these" always available; answers outside the ontology preserved and clinician-visible | MP-5; Chapman nebulosity; Bayor rigidity |
| Values Remodeling Gateway | PF-3 value-mapping ratification staged through the MS-4 lifecycle with patient visibility at every stage | PF-3; MS-4; shared-decision-making literature via Blake 2016 |
| Fit-vs-Degree Renderer | Plain-language separation of "we're not sure this applies to you" (fit) from "your answer is near the boundary" (degree, MAK-LWC's domain) | MS-9; MAK-LWC FP family; MAK-MIF beats 1–2 |
| Patient Council Interface | Trading-zone artifacts for patient-affecting remodeling: proposed instrument changes and register changes reviewed with patient representation | MS-8; MP-6 |

### Patient Face requirements

### MP-1 (MUST)
**Statement:** Every patient-visible recommendation renders its applicability honestly in the plain register: the population it was validated for, whether the patient is inside it, and — when outside or unknown — what that means for confidence in the advice. The plain register MUST NOT omit envelope status that the clinical register carries (SPINE-3 register fidelity applies to the meta-level).
**Rationale trace:** MS-1; PF-2; SPINE-3; "demystified uncertainty" design note; equity honesty (Cockburn heterogeneity).

### MP-2 (MUST)
**Statement:** Patients can file gap reports: "this doesn't describe me" is available on every intake instrument item and every rendered argument, in one interaction, with optional free text. Patient gap reports carry patient authorship into the fabric (MS-2), feed MA-2 analytics with demographic context under consent, and visibly acknowledge receipt — the report goes somewhere, and the patient can see that it did.
**Rationale trace:** MS-2; Blake instrument-gap finding; Bayor dual-facing agenda; procedural-justice rationale for acknowledgment.

### MP-3 (MUST)
**Statement:** Values-to-weighting mappings (PF-3) are remodeling: each proposed mapping passes the full MS-4 lifecycle — detection (elicited values), proposal, deliberation with the patient as a party, ratification, versioning, replay — with the patient able to see, contest, and revoke every active mapping at every stage. Runtime inference of values from behaviour remains prohibited (PF-3 anti-requirement, restated).
**Rationale trace:** PF-3; MS-4; Chapman (remodeling governed, never silent); patient-autonomy doctrine.

### MP-4 (SHOULD)
**Statement:** The plain register renders fit-uncertainty and degree-uncertainty distinctly: "we're not sure this question applies to you" (ontology fit, this corpus) is worded and styled differently from "your answer is near a boundary" (degree, MAK-LWC FP family), and the two are never merged into a single vague hedge.
**Rationale trace:** MS-9 routing; MAK-LWC A1 discipline; plain-language comprehension evidence via Blake patient-education findings.

### MP-5 (MUST)
**Statement:** No coercive formalization: every structured instrument offers an escape hatch (free text, "none of these," skip-with-reason), the escape-hatch content is preserved verbatim, rendered to the clinician in Consult-Prep, and counted in MS-3 telemetry. Completion metrics MUST NOT be optimized by removing escape hatches.
**Rationale trace:** Chapman circumrational boundary; MC-3 symmetry; Bayor rigidity; Goodhart guard (MA-3) applied to completion rates.

### MP-6 (SHOULD)
**Statement:** Patient-affecting remodeling — instrument changes, plain-register template changes, values-mapping classes — passes a patient-council stage in the MS-4 deliberation: a chartered trading zone (MS-8) with patient representation, whose review is recorded in the proposal's lifecycle.
**Rationale trace:** MS-8; participatory-design evidence via Bayor UCD agenda; procedural legitimacy for remodeling.

### Patient Face anti-requirements

- Never render out-of-envelope advice to a patient with in-envelope confidence language (violates MP-1; the plain register lies by omission).
- Never let a patient gap report vanish — unacknowledged, unrouted, or silently closed (violates MP-2).
- Never infer and apply values, priorities, or risk tolerance from behaviour (PF-3 anti-requirement, carried).
- Never optimize instrument-completion metrics by removing escape hatches or free text (violates MP-5).

## Part 5 — The Auditor Face

**What the research revealed.** MAK-FFC gave the auditor face its reason to exist: reframing "non-compliance" as "documented rational intent." The right wing gives it a second, deeper duty: *auditing the meta-level*. Every ontology change, every envelope, every gap report, every metric is itself an artifact that can rot, drift, or be gamed — and no external precedent exists for watching them (the sourcing record's central absence finding, Part 9). The materials are the fabric's evidentiary discipline (SPINE-4/5), the corruption engine's second career as theater detector (AF-4), and the regulatory posture's demand for glass-box evidence (REG-FIND-004, REG-KEEP-002): under assume-inclusion, the remodeling ledger and envelope discipline are not internal hygiene — they are Essential Principles evidence.

### Component inventory

| Component | Function | Research anchor |
|---|---|---|
| Remodeling Ledger | Every ontology change with full MS-4 lifecycle provenance: evidence in, deliberation record, ratifier identity, version diff, replay results | MS-4/MS-7; SPINE-5 |
| Gap Analytics | Aggregation of gap reports by instrument, element, population, site; equity lens surfaces subpopulation clustering as a safety finding | MS-2; MA-2; Cockburn heterogeneity |
| Goodhart Guard | Metrics-about-the-system are versioned, argued artifacts; gaming detection (distributional anomalies, threshold bunching, pre-audit spikes) runs beside AF-4's theater detector | Chapman rationality theater; AF-4; Goodhart's law |
| Envelope Compliance Monitor | Out-of-envelope releases as a distinct reviewable state with its own queue | ME-1; MA-4 |
| Regulator Trading Zone | AF-7 export extended with the meta-level: remodeling history, gap analytics, envelope discipline — the glass-box evidence bundle | AF-7; REG-FIND-004; REG-KEEP-002 |
| Cross-Wing Review | Joint lens over left-wing drift telemetry (MAK-LWC FA family) and right-wing gap pressure: degree drift as an ontology-misfit early signal | MS-9; MAK-LWC FA-5..7; MAK-MIF beat 3 |

### Auditor Face requirements

### MA-1 (MUST)
**Statement:** The remodeling ledger renders every ontology-layer change with its complete MS-4 lifecycle: triggering evidence, proposal, deliberation record (including trading-zone stage outputs), ratifier identity and authority, version delta, replay results (ME-5), and the set of historical decisions pinned to the superseded version. Any auditor can reconstruct *why the ontology is what it is* for any element at any date.
**Rationale trace:** MS-4/MS-7; SPINE-5 replay; AF-2 argument-pair pattern applied to ontology change.

### MA-2 (MUST)
**Statement:** Gap analytics aggregate gap reports by element, instrument, population, and site, with an equity lens: gap reports clustering on a demographic subpopulation or a deployment class (low-resource sites foremost) are a first-class safety finding routed to the MS-4 detect stage and to the clinical-safety owner — not a usability footnote.
**Rationale trace:** MS-2; Blake instrument-gap finding; Cockburn LMIC heterogeneity; north star (the gap the system exists to close appears first in its own gap reports).

### MA-3 (MUST)
**Statement:** Every metric computed over fabric states (compliance rates, completion rates, deviation rates, gap-report dispositions, alert PPV) is itself a versioned, argued artifact with a stated purpose and known failure modes; metric changes pass MS-4. Gaming detection — distributional anomalies, threshold bunching, boilerplate justification clusters, pre-audit spikes — runs continuously beside AF-4 theater detection, and its flags follow AF-4's human-review-only discipline.
**Rationale trace:** Goodhart's law; Chapman rationality theater generalized; AF-4; MP-5/MC-3 completion-metric hazards.

### MA-4 (MUST)
**Statement:** Out-of-envelope release is a distinct compliance state: alongside AF-3's four states, the projector distinguishes "released in-envelope," "released out-of-envelope with recorded fit-judgment (MS-7)," and "released out-of-envelope without recorded judgment" — the last is the reviewable anomaly. The state derives from ME-1's enforcement records, never from retrospective inference.
**Rationale trace:** ME-1; AF-3 state discipline extended; REG-KEEP-002 reviewable basis.

### MA-5 (SHOULD)
**Statement:** The regulator export (AF-7) includes the meta-level bundle: remodeling ledger extracts, gap analytics summaries, envelope-compliance states, and the self-description content (MS-6) at pinned versions — the demonstration that the system's basis is not only reviewable per decision but *governed over time*. This is the glass-box evidence REG-FIND-004 describes, produced natively.
**Rationale trace:** AF-7; REG-FIND-004; REG-KEEP-002; Essential Principles conformity posture under assume-inclusion (REG-POSTURE §3).

### MA-6 (MUST)
**Statement:** Meta-rational acts are never punished by default: gap reports, justified deviations, escape-hatch use, and recorded fit-judgments MUST NOT feed individual performance management, credentialing, or sanction without a governed human process with notice to the affected person (AF-4/AF-8 discipline extended). The system's ability to see the boundary depends on the reporters staying unafraid.
**Rationale trace:** Bayor surveillance-anxiety findings; AF-4/AF-8; MS-2's viability condition; procedural fairness.

### MA-7 (SHOULD)
**Statement:** Cross-wing review runs on a schedule: left-wing telemetry (membership-credibility drift, codebook divergence — MAK-LWC FA family) and right-wing gap pressure (MA-2) are reviewed together, because sustained degree-drift on an element is evidence of ontology misfit and vice versa; joint findings route to MS-4 detection.
**Rationale trace:** MS-9; MAK-LWC FA-5..7; MAK-MIF beat 3 (meaning under governance); drift-as-early-warning pattern.

### Auditor Face anti-requirements

- Never audit the meta-level into silence: remodeling backlogs, gap-report queues, and envelope anomalies are aged and owned, not accumulated (the ICSD-2 freeze reborn as a queue).
- Never let a metric become a target without its Goodhart review (violates MA-3).
- Never expose individual gap-reporters or deviators in aggregate views by default (MA-6; AF-8 lens discipline).
- Never present the meta-level bundle (MA-5) as evidence while its underlying checks (Appendix B; ME-5 replays) are failing — conformity theater is theater.

## Part 6 — The Engines

**What the research revealed.** The engine plane already carries the right wing's hard machinery in embryo: the corruption engine is institutionalized meta-rational vigilance (MAK-MIF beat 7), the evaluation firewall is anti-self-deception as infrastructure, and version pinning is what makes remodeling survivable. What MAK-FFC left informal is *fit enforcement*: engines that know their envelopes as data, an evaluator that checks the envelope before release, an adversary that hunts the ontology's edges specifically, and a replay harness that can answer "what would the old ontology have said?" — the question every remodeling ratification must face. The 2025+ research plane (Part 9) supplies the newest instrument: out-of-distribution and atypicality signals from the conformal machinery, which this corpus routes to the meta-rational layer as fit-evidence rather than letting them masquerade as mere low confidence.

### The fit-enforcement contract

```text
// Extends the MAK-FFC engine contract (EN-1); nothing here replaces it.
interface EnvelopeCheckedRelease {
  draft:    ActualArgumentDraft        // per EN-1, all six Toulmin elements
  envelope: ApplicabilityEnvelope      // per MS-1, machine-readable, pinned
  fit:      FitReport {
    status:     in | out(attrs[]) | unknown
    signals:    OODScore? | atypicality? | gapReports[]   // typed fit-evidence (MS-9)
  }
  // Release semantics (deterministic, per SPINE-7):
  //   in       → normal release path
  //   out/unknown → flagged path only: release requires a recorded human
  //                 fit-judgment (MS-7); silent release is a build error
}
```

### Component inventory

| Component | Function | Research anchor |
|---|---|---|
| Envelope Enforcer | Deterministic envelope check at the release gate; out/unknown routes to the flagged path | ME-1; SPINE-7 |
| Boundary Hunter | Corruption-engine perturbation classes aimed at ontology edges: atypical presentations, missing-category cases, envelope-boundary cohorts, instrument-gap populations | ME-2; MAK-MIF beat 7; EN-5 |
| Commitments Register | Per-GenericArgument record of what the ontology excludes: source-guideline stated exclusions + discovered gaps | ME-3; MS-1 |
| Remodeling Replayer | Replays sentinel and affected historical decisions across old/new ontology versions; divergence report gates ratification | ME-5; SPINE-5; EN-8 |
| Model Applicability Data | Training-population descriptors, validation cohorts, known failure regions shipped as machine-checkable data with every model version | ME-6; MS-1; REG-KEEP-002 |
| Fit-Signal Router | OOD scores, conformal atypicality, and gap-report density routed as typed fit-evidence to faces and MS-4 detection (never rendered as raw confidence) | ME-7; MS-9; EN-4 |

### Engine requirements

### ME-1 (MUST)
**Statement:** The deterministic evaluator (SPINE-7) checks every draft's grounds against the warrant's ApplicabilityEnvelope before release. In-envelope drafts follow the normal path; out-of-envelope and envelope-unknown drafts release only through the flagged path — rendered with MC-1/MP-1 status and, where a human proceeds, a recorded fit-judgment (MS-7). A build in which the flagged path can be bypassed silently is non-conformant.
**Rationale trace:** MS-1; SPINE-7 (the release gate is where enforcement lives); REG-FIND-004; Cockburn transfer failures.

### ME-2 (MUST)
**Statement:** The corruption engine maintains boundary-hunting perturbation classes: atypical presentations, cases synthesized at and beyond envelope edges, missing-category constructions, and cohorts matching gap-report clusters (MA-2). Confirmed findings publish as rebuttals (EN-5) and, where they demonstrate systematic misfit, as evidence into MS-4 detection — the adversary feeds the remodeling loop.
**Rationale trace:** EN-5; MAK-MIF beat 7; Chapman vigilance made procedural; MA-2 coupling.

### ME-3 (MUST)
**Statement:** The Guideline Compiler records ontological commitments: every GenericArgument lineage carries the source guideline's stated exclusions and scope conditions, plus discovered gaps accepted through MS-4, as a machine-readable commitments register feeding MS-1 envelopes. A compiled guideline whose source states exclusions the register omits fails compilation.
**Rationale trace:** EN-3 single change surface; MS-1; Blake per-criterion grain; glass-box discipline (MX-2).

### ME-4 (SHOULD)
**Statement:** LLM-assisted gap mining runs at authoring time (EN-6 Classes 1–3 posture): mining free-text supplements, escape-hatch content, and gap-report text for candidate ontology extensions and envelope corrections, proposed into MS-4 under human ratification only. The miner's outputs are proposals with evidence links, never direct changes.
**Rationale trace:** EN-6; MS-4; MAK-MIF beat 8 (the LLM on a leash); ArgTumour/ArgEval guideline-mining pattern (Part 9).

### ME-5 (MUST)
**Statement:** Remodeling replay gates ratification: before an ontology change ratifies, the affected sentinel set and a sample of pinned historical decisions replay against old and new versions; the divergence report (which decisions change, how, and why) is a mandatory deliberation input in MS-4, and post-ratification both versions remain replayable per SPINE-5.
**Rationale trace:** SPINE-5; EN-8 sentinel practice raised to ontology scope; MA-1 evidentiary needs; ICSD-2 anti-pattern.

### ME-6 (MUST)
**Statement:** Model applicability is versioned, machine-checkable data: every model version ships training-population descriptors, validation-cohort characteristics, subgroup performance where measured, and known failure regions — consumed by MS-1 envelopes and ME-1 enforcement. Prose model cards are a rendering of this data, never its source of truth.
**Rationale trace:** MS-1; REG-KEEP-002; EN-8 pinning; subgroup-validity evidence base (Part 9 research plane).

### ME-7 (SHOULD)
**Statement:** Out-of-distribution and atypicality signals — conformal nonconformity extremes, OOD detector scores, unusually large prediction sets — route to the meta-rational layer as typed fit-evidence (MS-9): rendered as possible ontology misfit on the faces and aggregated into MS-4 detection. They are not rendered as generic low confidence, and they never auto-block care.
**Rationale trace:** EN-4 machinery reused; MS-9 routing; mARC-QA overconfidence caution (Part 9); MAK-MIF beats 1/7.

### ME-8 (MAY)
**Statement:** A sandbox "what-if" mode may support remodeling deliberation: proposed ontology changes explored against historical cases and synthetic cohorts inside the evaluation firewall (EN-7), clearly labeled non-clinical, with no write path to the fabric beyond the proposal record it annotates.
**Rationale trace:** MS-4 deliberation quality; EN-7 firewall discipline; ME-5 replay machinery reused pre-ratification.

## Part 7 — Cross-cutting execution

### The regulatory update layer

This corpus is the first series volume authored after REG-POSTURE v1.0 and carries its findings as governing. The posture in one line: **build to SaMD standard; test exemption honestly at a named gate; assume inclusion** (REG-POSTURE §3). The update notes below are flagged divergences from earlier series framing, per REG-POSTURE's own precedence rule; none reopens a finding without the attestation route it specifies.

**Update note 1 — exemption unavailability (supersedes-in-part MAK-FFC XC-1's framing).** MAK-FFC XC-1 reasoned from the TGA's statement that an *AI-enabled* CDSS will not meet the exemption criteria. REG-FIND-001/002 sharpen this decisively: the disqualifier is the *diagnostic function itself* — a ranked differential with posteriors is making a diagnosis, providing new diagnostic information, and contributing to diagnosis, all three of which the "recommendation" definition excludes. Determinism does not rescue eligibility (REG-FIND-003: opacity is independent of ML; determinism is necessary but not sufficient for transparency). XC-1's conclusion (plan for ARTG inclusion) stands; its reasoning is updated.

**Update note 2 — the J-fork relabel (FORK-REG-001).** J-1 no longer means "exempt"; the fork is now *lower-class included* (J-1, deterministic runtime) versus *higher-class included* (J-2, ML runtime), decision point unchanged at Maturity Level 4 on Level 3 abstention evidence. Every series document that reads J-1 as an exempt pathway reads it under this relabel.

**Update note 3 — J-3's standing.** MAK-J3's Guideline-Prompt Profile (MAK-FFC Annex 1) remains a lawful, code-enforced scoped product — REG-POSTURE §2 confirms the shape of a product that could hold the exemption and it is J-3's shape (named published instruments only, no differential, no posteriors, no monitoring, no patient surface). But REG-POSTURE's own verdict governs its weight: such a product "does not deliver the thesis," and the recommendation is **do not contort the product to fit the exemption**. J-3 is therefore a reserve and an evidence vehicle (GPP-13), not the main line; exemption eligibility for any J-3 supply is tested at the named gate under ASSUME-REG-002, never assumed.

**Update note 4 — stack changes.** REG-POSTURE moves runtime inference from Bedrock to Baseten Sydney dedicated deployments with contractual version pinning (TASK-REG-009, contingent on ASSUME-REG-004), splits the Amplify path (synthetic/demo push-to-deploy versus gated regulated releases, TASK-REG-010), and adopts Ketryx-on-Jira as the lifecycle system of record (KTX-001..012). Part 9's AWS-native sourcing rows are read under this migration; MX-4 binds the toolchain accordingly.

**Update note 5 — gates govern phasing.** GATE-000 (counsel opinion; ASSUME-REG-001/002 closed) blocks Phase 1 work in REG-POSTURE's plan. This corpus's phasing table below sequences build work that is lawful pre-gate (synthetic-only per REG-KEEP-004/GATE-002) and marks the gate dependencies explicitly.

### Cross-cutting requirements

### MX-1 (MUST)
**Statement:** REG-POSTURE v1.0 governs this corpus's regulatory content: the assume-inclusion posture, REG-FIND-001..008, REG-KEEP-001..004, FORK-REG-001, and the gate structure GATE-000..004 are adopted as stated; ASSUME-REG-001..007 close only by the written external attestation REG-POSTURE requires. Any future series document that contradicts a REG-FIND flags the divergence explicitly and routes it through ASSUME-REG closure — silent contradiction is a conformance violation.
**Rationale trace:** REG-POSTURE §0.2 precedence and citation convention; XC-1 honesty posture generalized; MS-7 (regulatory judgments are ledgered acts).

### MX-2 (MUST)
**Statement:** The glass-box discipline: every released computation is either (i) a named, published, versioned instrument or guideline rule, cited in the warrant (the shape REG-FIND-004 says satisfies transparency), or (ii) a Mākoha-novel computation explicitly labeled as such in the argument, with its basis rendered per REG-KEEP-002 and its envelope per MS-1. A novel computation presenting under a published instrument's name, or blending into one, is prohibited — the auditor face can enumerate every novel computation in any release.
**Rationale trace:** REG-FIND-004 (named instrument vs novel composite); REG-FIND-003 (determinism ≠ transparency); MX-1; AF-7/MA-5 export needs.

### MX-3 (MUST)
**Statement:** The meta-rational layer functions in the low-resource profile: envelope rendering, gap reporting, escape hatches, and remodeling participation (asynchronous where connectivity requires) operate offline-first within XC-3's gates — because ontology misfit concentrates precisely where instruments were validated elsewhere. Low-resource gap-report streams receive MA-2's equity lens by default.
**Rationale trace:** XC-3; north star; Cockburn LMIC heterogeneity; MA-2; Blake instrument-gap finding generalized to deployment geography.

### MX-4 (SHOULD)
**Statement:** Toolchain bindings follow REG-POSTURE: the MS-4 remodeling lifecycle's gates and records are managed in the Ketryx-on-Jira configuration (KTX-001..012) as the lifecycle system of record; model-version pinning (ME-6, SPINE-5) rides the Baseten dedicated-deployment contract terms (ASSUME-REG-004); regulated-path releases flow through the split pipeline (TASK-REG-010). These bindings are reasonable defaults contingent on their ASSUME-REG closures, not architecture.
**Rationale trace:** REG-POSTURE KTX schema and TASK-REG-005..013; MX-1; SPINE-5.

### MX-5 (MUST)
**Statement:** Two-wing conformance is tested as a suite: integration tests verify MS-9 routing with adversarial confusion cases — degree problems that mimic gaps, gaps that mimic degrees, cases carrying both — and verify that each wing's artifacts (codebook changes, envelope changes) pass through the single MS-4 lifecycle rather than parallel side doors. The suite gates releases that touch either wing.
**Rationale trace:** MS-9; MAK-LWC FX-3 testing pattern as sibling precedent; MAK-MIF coordination doctrine; EN-7 firewall discipline.

### Phased execution plan

| Phase | Builds | Gate to exit |
|---|---|---|
| `R0 · Envelope substrate` | ApplicabilityEnvelope schema; commitments register in the compiler (ME-3); envelope data for the first compiled guideline domain; MS-1 conformance suite | Every deployed element enveloped or explicitly envelope-unknown; synthetic-only per GATE-002 posture |
| `R1 · Fit enforcement` | ME-1 evaluator extension; MC-1/MP-1 renderers; flagged-path release with MS-7 fit-judgment capture | MX-5 suite green on routing; out-of-envelope release impossible without recorded judgment |
| `R2 · Gap machinery` | GapReport object; MC-2/MP-2 reporters; escape-hatch capture (MC-3/MP-5); MS-3 telemetry | Gap reports flow end-to-end to MA-2 analytics; no punishment path exists (MA-6 audit) |
| `R3 · Remodeling lifecycle` | MS-4 workflow; MA-1 ledger; ME-5 replayer; trading-zone charters (MS-8); Ketryx binding (MX-4) | First governed remodeling ratified with replay evidence; both versions replayable |
| `R4 · Vigilance & pluralism` | ME-2 boundary hunter; MA-3 Goodhart guard; MC-4 conflict workbench; ME-7 fit-signal routing; MA-7 cross-wing review | A boundary-hunter finding drives an envelope narrowing through MS-4 end-to-end |
| `R5 · Meta-level evidence` | MS-6 self-description; MA-5 regulator bundle; MX-2 novel-computation enumeration; low-resource meta-rational profile (MX-3) | An external reviewer reconstructs the ontology's history and every novel computation from exports alone |

### Risk register

| Risk | Mechanism | Standing control |
|---|---|---|
| Gap-report suppression | Reporting is punished, socially or by metric, and the boundary goes dark | MA-6 prohibition; MC-2/MP-2 friction floors; MA-2 monitors report-rate collapse as an anomaly |
| Remodeling paralysis | MS-4's governance is so heavy the ontology freezes anyway (ICSD-2 by process) | Lifecycle SLAs with aged queues owned (MA anti-requirement); ME-8 sandbox lowers deliberation cost; MS-4 stages sized to change class |
| Remodeling theater | Lifecycle stages rubber-stamp; deliberation records are boilerplate | MA-3 gaming detection over the meta-level's own records; trading-zone charters name real parties (MS-8) |
| Envelope inflation | Envelopes quietly widened to reduce flagged-path friction | Envelope changes are remodeling (MS-4); MA-1 ledger; ME-2 hunts the widened edges |
| Fit-signal alarm fatigue | ME-7/MC-1 render so often they train dismissal | MC-6 evidence-gating; MS-9 typing keeps fit-signals rare and meaningful; CF-5-style governance of prompt rules |
| Wing confusion | Degree and fit conflated; fuzzy machinery asked to fix ontology problems or vice versa | MS-9 typed routing; MX-5 adversarial suite; MA-7 joint review |
| Regulatory drift | Series documents cite superseded framing (exempt J-1, Bedrock stack) | MX-1 flag-and-route rule; Part 7 update notes as the citation surface; ASSUME-REG closure discipline |
| Meta-level surveillance capture | Gap/deviation analytics drift into individual policing | MA-6; AF-8 lens discipline; Bayor surveillance-anxiety evidence as standing rationale |

### Open research agenda

- **Gap-report elicitation quality.** No validated instrument exists for structured "this doesn't fit" capture at point of care or from patients; MC-2/MP-2's one-interaction bound and locus taxonomy are hypotheses to test.
- **Reliance calibration measurement.** MC-7's in-envelope-agreement / out-of-envelope-scrutiny metric needs an operationalization study; the automation-bias literature supplies designs but not CDSS-argument-specific instruments.
- **Remodeling lifecycle economics.** MS-4's stage costs versus ontology-freshness benefits have no published evidence base; instrument the R3 phase to produce one.
- **Envelope formalism.** MS-1/ME-6 need a schema expressive enough for population descriptors and failure regions yet checkable at release time; candidate ground in the subgroup-validity and dataset/model documentation literatures (Part 9 research plane).
- **Regulatory recognition of the meta-level bundle.** MA-5's glass-box evidence has no precedent as conformity material; test its reception through the GATE-000 counsel engagement (TASK-REG-002) and the Lumos pathway (TASK-REG-015).
- **The GAAM collaboration.** Unchanged from MAK-FFC: co-developing deviation/gap/remodeling formalization with Stranieri remains the highest-leverage de-risking move.

## Part 8 — Fold-in maps & traceability

### MAK-FFC v1.1 fold-in map (complete)

This corpus hosts MAK-FFC v1.1 rather than restating it. Every FFC requirement is mapped below to its right-wing disposition: **carried** (applies unmodified; this corpus adds nothing), **operationalized** (this corpus supplies the mechanism the FFC requirement presumes), or **extended** (a requirement here adds obligations on top). No FFC requirement is relaxed.

| MAK-FFC ID | Disposition | Right-wing linkage |
|---|---|---|
| SPINE-1 | carried | Meta-rational acts also argue (MS-7 extends the pattern to the meta-level) |
| SPINE-2 | extended | Rebuttal slot fed by boundary hunter (ME-2); qualifier joined by fit status (ME-1) |
| SPINE-3 | extended | Register fidelity applies to envelope/gap content (MP-1); meta-rational acts render in all registers (MS-7) |
| SPINE-4 | carried | GapReport/RemodelingProposal/ConflictRecord are fabric entries under the same ledger discipline |
| SPINE-5 | operationalized | Ontology-scope replay (ME-5); remodeling ledger (MA-1); pinning is what makes MS-4 survivable |
| SPINE-6 | extended | Generalized to every system pair via MS-5; navigations recorded (MC-4) |
| SPINE-7 | extended | The release gate also checks envelopes (ME-1); "computerize the occasions of judgment, never the judgment" |
| SPINE-8 | extended | Deviation joined by its sibling object, the GapReport (MS-2); the distinction is normative (MC-2) |
| SPINE-9 | carried | Meta-level read models are projections of the same fabric |
| CF-1 | carried | — |
| CF-2 | extended | Envelope status renders with the argument (MC-1) |
| CF-3 | extended | Friction discipline extended to gap reporting (MC-2) |
| CF-4 | carried | Hard-stop class unchanged; fit-flags are never hard stops (ME-7) |
| CF-5 | extended | Governance pattern reused for meta-prompts (MC-6) |
| CF-6 | carried | Group navigation of conflicts records per MS-7 |
| CF-7 | extended | Evaluation adds meta-rational outcome measures (MC-7) |
| CF-8 | carried | — |
| PF-1 | extended | Instrument envelopes and gaps representable and patient-reportable (MS-1, MP-2) |
| PF-2 | extended | Envelope honesty joins register fidelity (MP-1) |
| PF-3 | operationalized | Value mappings staged through MS-4 (MP-3) |
| PF-4 | carried | Gap reports and consent ride the same custody machinery |
| PF-5 | carried | — |
| PF-6 | extended | Meta-rational functions inside the accessibility floor (MX-3) |
| PF-7 | carried | WHO SMART alignment; jurisdictional adaptation is remodeling under MS-4/XC-4 |
| PF-8 | carried | — |
| AF-1 | carried | Meta-level writes (proposals, reviews) follow the same attributed-entry rule |
| AF-2 | extended | Argument-pair pattern applied to ontology versions (MA-1) |
| AF-3 | extended | Envelope-compliance states added beside the four (MA-4) |
| AF-4 | extended | Goodhart guard runs beside theater detection (MA-3) |
| AF-5 | operationalized | The full MS-4 lifecycle is AF-5's mechanism |
| AF-6 | carried | Disputes over remodeling decisions use the same ODR mode |
| AF-7 | extended | Meta-level bundle joins the export (MA-5) |
| AF-8 | extended | Lens discipline extended to gap/deviation analytics (MA-6) |
| EN-1 | extended | Fit-enforcement contract layers on the engine contract (ME-1) |
| EN-2 | carried | Criterion grain is what makes envelope/commitment tracking tractable |
| EN-3 | extended | Compiler records ontological commitments (ME-3) |
| EN-4 | extended | Conformal machinery's extremes routed as fit-signals (ME-7) |
| EN-5 | extended | Boundary-hunting perturbation classes (ME-2) |
| EN-6 | extended | Authoring-time gap mining added to the permitted class (ME-4) |
| EN-7 | carried | ME-8 sandbox lives inside the firewall |
| EN-8 | extended | Sentinel replay raised to ontology scope (ME-5) |
| EN-9 | extended | Telemetry joined by circumrational-load metrics (MS-3) |
| XC-1 | carried with update | Conclusion stands (plan for inclusion); reasoning updated per REG-FIND-001..004 — see Part 7 update note 1 (MX-1) |
| XC-2 | carried with update | J-3 remains the code-enforced reserve; weight updated per REG-POSTURE §2 — see Part 7 update note 3 |
| XC-3 | extended | Meta-rational low-resource profile (MX-3) |
| XC-4 | carried | Localization-as-pluralism is MS-5 practice; adaptations remodel under MS-4 |
| Annex 1 (GPP-1..16) | carried | J-3 boundary machinery unchanged; its exemption test now runs at the named gate under ASSUME-REG-002 (Part 7 update note 3) |

### MAK-MIF beat map (right-wing contributions operationalized)

| Beat | Right-wing contribution (MAK-MIF) | Operationalized by |
|---|---|---|
| 1 · The borderline patient | Partial fit routes to judgment, never silent forcing | ME-1 flagged path; MS-9 routing; MC-1 |
| 2 · The full translation loop | Formalization-awareness as standing duty | MS-3 load telemetry; MC-3/MP-5 boundary-work capture |
| 3 · Meaning under governance | Meaning change ratified, versioned, replayed | MS-4 lifecycle; MA-7 cross-wing review; ME-5 replay |
| 4 · Conflict with a metric | Conflicts surfaced unresolved; choice recorded as meta-rational act | MS-5; MC-4 workbench; MS-7 ledger |
| 5 · Disagreement held, not averaged | Ratification adopts honest disagreement artifacts | MS-8 trading zones; MS-4 deliberation records |
| 6 · Reliability-aware listening | Belief semantics kept separate and honest | MS-9 typing (with MAK-LWC Z-machinery on the left) |
| 7 · The adversary's map | Vigilance as scheduled, targeted process | ME-2 boundary hunter; MA-3 Goodhart guard |
| 8 · The LLM on a leash | Proposal-only LLM posture, governed correction loop | ME-4 gap mining; EN-6 class discipline carried |

### Findings → requirements

| Finding | Source | Requirements it drives |
|---|---|---|
| Meta-rationality judges systems and cannot be computerized; its occasions can be instrumented | Chapman corpus (uploaded) | MS-1..9; MC-1/2/5; ME-1 |
| Failures concentrate at the circumrational boundary; boundary work is invisible labour | Chapman; Bayor 2025 | MS-3; MC-3; MP-5 |
| Ontological remodeling is real, constant, and must be governed, not denied or silent | Chapman; ICSD-2 freeze (Sleep Tools Dossier) | MS-4; MA-1; ME-5 |
| Rationality theater and Goodhart dynamics attack any rationality-rewarding system | Chapman; MAK-FFC AF-4 lineage | MA-3; MC-6; risk register |
| Instruments carry population gaps (no OSA screen tuned to women) | Blake 2014; Sleep Tools Dossier | MS-1; MP-2; MA-2 |
| CDSS transfer fails across contexts; LMIC heterogeneity is the expected case | Cockburn 2024 | MC-1; MX-3; MA-2 equity lens |
| Rigidity, surveillance anxiety, workarounds, trust collapse | Bayor 2025 | MC-3; MA-6; MP-5 |
| Deviation formalizable at warrant grain; generic/actual split | GAAM 2006; Stranieri corpus | MS-2 (gap as sibling object); MA-1 |
| Exemption unavailable: diagnostic function disqualifies; determinism ≠ transparency; glass-box test | REG-POSTURE v1.0 (REG-FIND-001..004) | MX-1; MX-2; MA-5; Part 7 update notes |
| Retained commitments: deterministic release, reviewable basis, human sign-off, synthetic-only | REG-POSTURE (REG-KEEP-001..004) | ME-1; MS-6; MA-5; phasing gates |
| J-fork relabel: lower-class vs higher-class included | REG-POSTURE (FORK-REG-001) | Part 7 update note 2; MX-1 |
| Stack: Baseten Sydney pinning, Amplify split, Ketryx-on-Jira | REG-POSTURE (TASK-REG-009/010, KTX-001..012) | MX-4 |
| OOD/atypicality signals as fit-evidence; LLM overconfidence in flexible reasoning | mARC-QA 2025; conformal-LLM literature (Part 9) | ME-7; MS-9 |
| Argument-shaped explanation outperforms bare outputs | Spitzer et al. 2026 (npj Digit. Med.); Abbas 2025 | MS-6; MC-5 |

### Sources

- Chapman, meta-rationality materials (uploaded corpus, this series) — the right wing's theoretical base: circumrational boundary, nebulosity, ontological remodeling, trading zones, rationality theater, reasoning about systems.
- MAK-FFC v1.1 (The Four Faces Corpus) — folded via the Part 8 map; all SPINE/CF/PF/AF/EN/XC/GPP citations resolve there.
- MAK-ELSM v1.1 (Execution Layer Sourcing Map) — folded as Part 9.
- MAK-LWC v1.1 (The Left Wing Corpus) — sibling wing; FS/FC/FP/FA/FE/FX citations resolve there.
- MAK-MIF v1.0 (Mākoha in Flight) — the eight beats; beat map above.
- REG-POSTURE v1.0 (Mākoha Regulatory Posture, uploaded 2026-09-01) — governing regulatory document; cited by stable IDs throughout per its §0.2 convention. Per its own firewall note it is never a source for clinical content.
- Bayor et al. (2025). Designing CDSS — a user-centered lens. JMIR 27:e63733.
- Abbas, Jeong & Lee (2025). Explainable AI in CDSS. Healthcare 13:2154.
- Cockburn et al. (2024). CDSS for maternity care. eClinicalMedicine 76:102822.
- Blake & Kerr (2014); Blake, Kerr & Gammack (2016); Miah, Blake & Kerr (2020) — the artifact lineage (full provenance in the Sleep Tools Dossier).
- Stranieri corpus — GAAM (DSS 2006), Split-Up, ward rounds, MDT, ODR, PCA (full provenance in The Stranieri File).
- Spitzer et al. (2026). Explanation formats RCT, npj Digital Medicine; Kim et al. (2025). mARC-QA, Scientific Reports — via MAK-ELSM §05.
- WHO SMART Guidelines program — via MAK-FFC PF-7/XC-4 lineage.

*Document footer (source artifact):* The Right Wing Corpus v1.0 · requirement IDs are stable; propose changes as argued deviations — this document practices its own doctrine. Compiled from the series' primary-source research, the folded MAK-FFC v1.1 and MAK-ELSM v1.1, and REG-POSTURE v1.0 read in full on 2026-09-01.

## Part 9 — Execution sourcing annex

**Folded from MAK-ELSM v1.1** (all 23 entries, verdicts and J-3 dispositions carried unmodified; repo statuses are direct-fetch observations dated 2026-08-29 and are re-verified in this corpus's v1.1 sourcing pass before any dependency decision). This annex adds the right-wing serving map: which entries carry the meta-rational spine's load, and where the right wing's own build list sits.

### Carried inventory (MAK-ELSM v1.1, unmodified) with right-wing serving map

| ELSM entry | Verdict (carried) | J-3 disposition (carried) | Right-wing service |
|---|---|---|---|
| ELSM-01 cqframework/clinical_quality_language | ADOPT | IN_PROFILE | Compiler substrate that ME-3's commitments register annotates |
| ELSM-02 cqframework/clinical-reasoning | ADOPT | IN_PROFILE | Same; $apply machinery under envelope-carrying GenericArguments |
| ELSM-03 cqframework/cqf-ruler | LEGACY | NA | Deploy upstream (ELSM-20) in every tier |
| ELSM-04 google/android-fhir | ADOPT | IN_PROFILE | MX-3 offline meta-rational profile: intake + gap reporting on-device |
| ELSM-05 opensrp/fhircore | ADOPT / STUDY | IN_PROFILE | The deployed low-resource embodiment MX-3 extends |
| ELSM-06 WHO SMART Guidelines IGs | ADOPT | IN_PROFILE | Source ontologies whose adaptations remodel under MS-4/XC-4 |
| ELSM-07 TweetyProjectTeam/TweetyProject | ADAPT | IN_PROFILE (evaluator only) | Conflict semantics behind MS-5 ConflictRecords |
| ELSM-08 carneades/carneades-4 | ADAPT / STUDY | IN_PROFILE (evaluator only) | Design mine for argument evaluation; dormant |
| ELSM-09 CLArg-group/argumentative-llms | ADAPT | AUTHORING_TIME_ONLY | ME-4 gap-mining pattern precedent ("LLM proposes, formal layer decides") |
| ELSM-10 GAAM implementation | BUILD | IN_PROFILE (build) | MS-2's sibling-object grain (gap vs deviation) rides the GAAM service |
| ELSM-11 Justification fabric / deviation ledger / compliance projector | BUILD | IN_PROFILE (build) | Hosts every MS-7 meta-rational entry; MA-1/MA-4 read models |
| ELSM-12 scikit-learn-contrib/MAPIE | ADOPT | EXCLUDED (J-1/J-2 only) | ME-7's fit-signals reuse its nonconformity machinery |
| ELSM-13 babylonhealth/counterfactual-diagnosis | STUDY ONLY | EXCLUDED | Evaluation baseline only; patent-encumbered |
| ELSM-14 pgmpy | ADOPT | EXCLUDED | Engine internals; envelope data (ME-6) wraps whatever it builds |
| ELSM-15 Giskard-AI/giskard | ADOPT | CI_ONLY | ME-2 boundary-hunter harness scaffolding; MA-3 experiments |
| ELSM-16 Trusted-AI/adversarial-robustness-toolbox | ADOPT | CI_ONLY | ME-2 perturbation ammunition |
| ELSM-17 codenotary/immudb | ADAPT | IN_PROFILE | SPINE-4 ledger option; BUSL legal review stands |
| ELSM-18 AWS QLDB | AVOID | NA | Retired 2025-07-31; unchanged |
| ELSM-19 Aurora PostgreSQL + transparency-log pattern | ADOPT PATTERN | IN_PROFILE | Post-QLDB ledger; MA-1 remodeling ledger rides the same store |
| ELSM-20 HAPI FHIR jpaserver-starter | ADOPT | IN_PROFILE | Data plane; Provenance/AuditEvent for MS-7 entries |
| ELSM-21 fastenhealth/fasten-onprem | STUDY | NA | Archived; PF-4 remains more build than it looks |
| ELSM-22 SuperMedIntel/Medical-Graph-RAG | STUDY | AUTHORING_TIME_ONLY | Credibility-hierarchy pattern for evidence retrieval behind MS-6 |
| ELSM-23 Teddy-XiongGZ/MedRAG (MIRAGE) | ADOPT_BENCH | AUTHORING_TIME_ONLY | Benchmark harness for any ME-4 retrieval component |

### The right wing's own build list (no precedent found — carried and extended)

MAK-ELSM's central absence finding carries directly to this corpus, and the right wing adds entries to it. No public code was found (targeted-and-verified search, per the carried methodology note) for: the justification fabric and deviation ledger (ELSM-11); a GAAM service (ELSM-10); and — new to this corpus's scope — an **applicability-envelope enforcement layer at a release gate** (ME-1), a **gap-report/nebulosity-flag object with analytics** (MS-2/MA-2), a **governed ontological-remodeling lifecycle with replay gating** (MS-4/ME-5), and a **Goodhart guard over compliance metrics** (MA-3). These are the moat, extended: everything around the differentiator remains buyable; the differentiator itself is not.

### The 2025+ research plane (carried highlights, right-wing reading)

- **Guideline-grounded RAG** (JAMIA meta-analysis OR 1.35; preoperative-fitness 96.4%; ESUR radiology; pediatric myopia) — carried: the common success factor is a *tight, versioned, curated corpus*, which is knowledge-plane envelope discipline (MS-1) stated as retrieval practice.
- **Argumentation × LLMs** (ArgMed-Agents; Argumentative LLMs; ArgEval/ArgTumour) — carried: the "LLM proposes, formal layer decides" pattern is SPINE-7; ArgTumour's *global contestability* (modify the shared framework, not one case) is MS-4's remodeling loop running as a research prototype.
- **Cautionary evidence** (mARC-QA overconfident uncertainty; Spitzer et al. explanation-format RCT) — carried: the empirical case for ME-7's routing (big nonconformity = fit evidence, not just low confidence) and MS-6's argument-shaped self-description.
- **Conformal for LLM outputs** (2026 arXiv cluster) — carried: the literature that decides whether an LLM output can ever carry a valid qualifier; track, do not ship ahead of it (EN-6 posture).

### Sourcing landmines (carried, plus this corpus's additions)

- Carried unchanged: QLDB retired (2025-07-31); immudb BUSL-1.1; cqf-ruler legacy; fasten-onprem archived (2026-07); Babylon patent encumbrance; Carneades dormancy.
- **New — stack migration:** REG-POSTURE moves runtime inference Bedrock → Baseten Sydney dedicated (TASK-REG-009, ASSUME-REG-004 open). Any sourcing row assuming Bedrock runtime invocation reads under this migration; the J-3 prohibited-namespace manifest's "LLM runtime SDKs (Bedrock runtime invocation paths included)" extends to Baseten client namespaces in a J-3 build.
- **New — lifecycle tooling:** Ketryx-on-Jira (KTX-001..012) is commercial SaaS, not OSS; MX-4 binds to it as a reasonable default contingent on ASSUME-REG-006 (tier/validation-package timing). No OSS equivalent with validated-status claims was identified in the carried pass; the v1.1 refresh examines the space.

> **Refresh note.** This annex's v1.0 content is the fold; the Task-2 sourcing pass (this corpus's v1.1) re-verifies statuses as of its own date and adds right-wing-specific entries — envelope/model-documentation tooling, OOD/drift detection, regulated-lifecycle tooling, and 2025+ research on subgroup validity and predetermined change control — as additive ELSM-R rows.


### v1.1 refresh pass (additive; verified 2026-09-01)

**Re-verification.** Spot-re-verification of the carried inventory's most load-bearing volatile rows on 2026-09-01 found no status changes: TweetyProject active (v1.31, Jul 2026; LGPL-3.0 from v1.6 onward, GPL-3.0 before — a licensing nuance sharpened since the carried row, which listed LGPL-3.0 only); opensrp/fhircore active (v2.2.2, Nov 2025, Apache-2.0). All other carried statuses remain dated 2026-08-29 observations; the carried re-verification rule stands for any dependency decision.

**New sourcing entries (right-wing-specific).** Verified by direct repo fetch 2026-09-01:

| ID | Repo / artifact | What it gives you | Status (verified 2026-09-01) | Verdict | Serves |
|---|---|---|---|---|---|
| ELSM-R01 | [SeldonIO/alibi-detect](https://github.com/SeldonIO/alibi-detect) | Outlier, adversarial, and drift detection across modalities (TF/PyTorch backends) — the OOD detector layer behind fit-signal routing | 2.5k★ · Apache-2.0 · v0.13.0 Dec 2025 · active | ADOPT | ME-7, MA-7 |
| ELSM-R02 | [evidentlyai/evidently](https://github.com/evidentlyai/evidently) | ML/LLM evaluation, testing, and monitoring framework (100+ metrics, dashboards) — circumrational-load and drift telemetry scaffolding | 7.8k★ · Apache-2.0 · active | ADOPT | MS-3, MA-7, EN-9 |
| ELSM-R03 | [mlcommons/medperf](https://github.com/mlcommons/medperf) | Open federated-evaluation platform for medical AI — multi-site validation evidence without moving data; subgroup and site-level performance for envelope data | 169★ · Apache-2.0 · active | ADAPT / STUDY | ME-6, MC-7, EN-7 |
| ELSM-R04 | [openregulatory/templates](https://github.com/openregulatory/templates) | Markdown template set for ISO 13485, IEC 62304, ISO 14971, IEC 62366 — the OSS complement to the Ketryx binding for document-layer conformity | 159★ · active · license per repo LICENSE.md | ADAPT | MX-4, MA-5 |

**Regulatory instruments (governance precedent, not code).**

- **FDA PCCP final guidance** — *Marketing Submission Recommendations for a Predetermined Change Control Plan for AI-Enabled Device Software Functions* (final guidance; Federal Register availability notice 4 Dec 2024). A PCCP is a pre-authorized change protocol: the modification set, its verification methods, and its impact assessment ratified *before* the change ships. This is the MS-4 remodeling lifecycle recognized in regulatory form — detection/proposal/deliberation mapped to the modification protocol, ME-5 replay mapped to the verification methods — and the strongest external precedent that governed ontology change can be a submission artifact rather than a per-change re-approval. US-market relevance only; noted for MA-5 bundle design and the MS-4 stage vocabulary.
- **TGA AI guidance (22 Apr 2026)** — clarifies that existing medical-device rules apply to AI-enabled products ("same rules, smarter tools"): updates introducing new functionality are regulatory events before deployment (the GPP-3/MS-4 reassessment discipline, stated by the regulator); manufacturers must monitor for scope/feature creep and off-label use; transparency must cover training data, validation, and ongoing performance monitoring (MS-6/ME-6/MA-5 territory); and **synthetic data will generally not replace clinical data** for safety-and-performance evidence. No PCCP-equivalent mechanism exists in Australia per this guidance. Two consequences carried forward: (i) it reinforces, and nowhere contradicts, REG-FIND-001..004 — no MX-1 flag required; (ii) the synthetic-data caution sharpens REG-KEEP-004's reading — synthetic-only is a *development* posture (GATE-002), never a *validation evidence* posture, which is what the Lumos pathway (TASK-REG-015) exists to supply.

**The 2025+ deployment-monitoring research plane (new).** The right wing's engine-plane bets (ME-7 fit-signal routing, MA-7 cross-wing drift review, MS-1/ME-6 envelope discipline) now have a fast-maturing literature:

- **OOD detection as a deployment guardrail is empirically validated:** OOD detectors consistently identify patients on whom models perform worse, including *training-underrepresented subsets* — the equity-lens mechanism (MA-2) observed in the wild (Weng et al. 2025, Clinical and Translational Science).
- **Label-agnostic shift monitoring works at hospital scale:** a monitoring pipeline over 143k admissions detected harmful shifts from demographics, assay changes, and COVID, with drift-triggered remediation maintaining performance (Subasri et al. 2025, JAMA Network Open) — the MS-3/MA-7 telemetry loop with outcome evidence.
- **The field is systematized:** a 2025 systematic review of dataset-shift detection/correction in health ML (32 studies) finds no single generalizable method and explicitly calls for subgroup-specific analyses and CDSS integration (Santos Silva et al. 2025, J. Biomed. Informatics) — the integration gap this corpus's ME-7/MA-7 requirements occupy.
- **Anytime-valid monitoring theory has arrived:** weighted conformal test martingales give false-alarm-controlled, online-adaptive changepoint monitoring with cause diagnosis (Prinster et al. 2025); sequential risk-violation monitoring under unknown shift (Timans et al. 2025) and disagreement-based label-free deterioration detection (D3M, Nguyen et al. 2025) complete the toolkit — candidate mathematics for MA-7's scheduled review and ME-7's alarm discipline.
- **Conformal triage under shift, with stratified coverage:** a 2026 Scientific Reports study combines conformal sets, cost-aware deferral, and group-conditional (Mondrian) coverage that narrows the gender coverage gap to 1.4 points under temporal shift (Kwon et al. 2026) — ME-7 and MA-2's equity lens realized in one pipeline, with deferral-to-human as the action (the flagged path, independently discovered).

**Refresh landmines.**

- Alibi-detect and evidently are general-purpose ML tooling: neither ships clinical perturbation classes or argument-aware telemetry — the ME-2 boundary-hunter content and MS-3's fabric coupling remain builds on top.
- TweetyProject's pre-1.6 versions are GPL-3.0; the LGPL posture holds only for current versions — pin accordingly.
- PCCP is a US instrument; building MS-4 to PCCP vocabulary aids a future FDA submission but confers nothing at the TGA, which (per the 22 Apr 2026 guidance) treats functional updates as regulatory events without a pre-authorization mechanism.

## Appendix C — v1.1 sourcing register (additive)

Mirrors the refresh tables; keep in sync (self-audit check 11).

```json
{
  "doc_id": "MAK-RWC",
  "version": "1.1",
  "verified": "2026-09-01",
  "reverified_carried": {"ELSM-07": "active v1.31 2026-07; LGPL-3.0 (GPL-3.0 pre-1.6)", "ELSM-05": "active v2.2.2 2025-11"},
  "entries": [
    {"id":"ELSM-R01","name":"SeldonIO/alibi-detect","verdict":"ADOPT","license":"Apache-2.0","status":"active; v0.13.0 2025-12","serves":["ME-7","MA-7"]},
    {"id":"ELSM-R02","name":"evidentlyai/evidently","verdict":"ADOPT","license":"Apache-2.0","status":"active","serves":["MS-3","MA-7","EN-9"]},
    {"id":"ELSM-R03","name":"mlcommons/medperf","verdict":"ADAPT_STUDY","license":"Apache-2.0","status":"active","serves":["ME-6","MC-7","EN-7"]},
    {"id":"ELSM-R04","name":"openregulatory/templates","verdict":"ADAPT","license":"see repo","status":"active","serves":["MX-4","MA-5"]}
  ],
  "regulatory_instruments": [
    {"name":"FDA PCCP final guidance (AI-enabled device software functions)","date":"2024-12","relevance":["MS-4","ME-5","MA-5"],"jurisdiction":"US"},
    {"name":"TGA AI guidance (same rules, smarter tools)","date":"2026-04-22","relevance":["MS-4","MS-6","ME-6","MA-5","REG-KEEP-004 reading"],"jurisdiction":"AU"}
  ]
}
```

---

## Appendix A — ID census (additive)

Authoritative enumeration for validator checks. Count: **42**.

```json
{
  "doc_id": "MAK-RWC",
  "version": "1.0",
  "requirements": {
    "MS": ["MS-1","MS-2","MS-3","MS-4","MS-5","MS-6","MS-7","MS-8","MS-9"],
    "MC": ["MC-1","MC-2","MC-3","MC-4","MC-5","MC-6","MC-7"],
    "MP": ["MP-1","MP-2","MP-3","MP-4","MP-5","MP-6"],
    "MA": ["MA-1","MA-2","MA-3","MA-4","MA-5","MA-6","MA-7"],
    "ME": ["ME-1","ME-2","ME-3","ME-4","ME-5","ME-6","ME-7","ME-8"],
    "MX": ["MX-1","MX-2","MX-3","MX-4","MX-5"]
  },
  "levels": {
    "MUST":   ["MS-1","MS-2","MS-3","MS-4","MS-5","MS-6","MS-7","MS-9","MC-1","MC-2","MC-3","MC-5","MC-7","MP-1","MP-2","MP-3","MP-5","MA-1","MA-2","MA-3","MA-4","MA-6","ME-1","ME-2","ME-3","ME-5","ME-6","MX-1","MX-2","MX-3","MX-5"],
    "SHOULD": ["MS-8","MC-4","MC-6","MP-4","MP-6","MA-5","MA-7","ME-4","ME-7","MX-4"],
    "MAY":    ["ME-8"]
  },
  "retired": []
}
```

Census arithmetic: 31 MUST + 10 SHOULD + 1 MAY = 42.

## Appendix B — Self-audit checks (additive)

Run against this file after any edit; all must pass before a version increments.

1. **ID uniqueness** — no requirement ID appears in more than one requirement header.
2. **ID census parity** — headers matching `^### (MS|MC|MP|MA|ME|MX)-\d+ \((MUST|SHOULD|MAY)\)$` exactly equal Appendix A's enumeration (42).
3. **Level parity** — the level in each header matches its bucket in Appendix A `levels`.
4. **Trace presence** — every requirement block contains a non-empty `**Rationale trace:**` line.
5. **Normative leakage** — no capitalized MUST/SHOULD/MAY in informative prose outside requirement blocks, anti-requirement bullets, quoted source text, or this appendix.
6. **Cross-reference integrity** — every MS/MC/MP/MA/ME/MX ID cited in prose or tables exists in the census; every MAK-FFC, MAK-LWC, GPP, and REG-POSTURE ID cited resolves in its host document.
7. **Fold-in completeness** — the Part 8 FFC map covers all 46 MAK-FFC IDs plus the Annex 1 row; the Part 9 table covers all 23 ELSM entries with verdicts and dispositions carried unmodified.
8. **Regulatory precedence** — no statement contradicts a REG-FIND without an explicit Part 7 update note; ASSUME-REG items are never described as closed.
9. **Table integrity** — all markdown tables have consistent column counts per row.
10. **Stability** — IDs present in a previous version are present or explicitly retired in Appendix A; retired IDs never reused.
11. **Refresh register parity (v1.1)** — every ELSM-Rnn row in the refresh table has exactly one Appendix C entry and vice versa; refresh statuses carry the 2026-09-01 verification date; regulatory-instrument rows appear in both the prose and the register.
