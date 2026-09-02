---
doc_id: MAK-ABC
title: "The Abdomen Corpus"
version: "1.0"
date: "2026-09-01"
series: "Mākoha research series — volume 12 · the Auditor Face, consolidated from both wings"
status: normative-draft
normative_language: RFC-2119 (MUST / SHOULD / MAY)
req_prefixes: [AL, AR, AG, AT, AX, AE]
req_count: 27
subordinate_to: "MAK-FFC v1.1 — no requirement here relaxes a corpus MUST; consolidations state their sources"
builds_from:
  - "MAK-FFC v1.1 Part 5 — the host Auditor Face (AF-1..8): the read model, argument pairs, the reframing, theater detection, the feedback loop, dispute mode, regulator export"
  - "MAK-LWC v1.1 Part 5 — the fuzzy auditor face (FA-1..7): membership math view, curve-change workbench, drift telemetry, projection honesty"
  - "MAK-RWC v1.1 Part 5 — the meta-rational auditor face (MA-1..7): remodeling ledger, gap analytics, Goodhart guard, envelope compliance, meta-level export"
  - "MAK-CEC v1.1 — the plane it reads: verdict traces (RG-2), unified telemetry (RG-5), campaign coverage (AD-5), unified replay (RG-4)"
governed_by:
  - "REG-POSTURE v1.0 — REG-KEEP-002 (reviewable basis), REG-FIND-004 (glass box), OBL-001..012 obligations register, GATE structure; this face produces the evidence the posture consumes"
changelog:
  - "v1.0 (2026-09-01): initial release — 27 requirements across AL/AR/AG/AT/AX/AE; three-corpus consolidation map (Part 7); sourcing annex (Part 8)."
companions:
  - "MAK-FFC v1.1 (host) · MAK-LWC v1.1 (left wing) · MAK-RWC v1.1 (right wing) · MAK-CEC v1.1 (engine plane) · MAK-HDC v1.0 · MAK-TXC v1.0"
  - "MAK-MIF v1.0 (beats 3, 4, 7 land on this face)"
  - "REG-POSTURE v1.0 (governing regulatory document)"
artifact_url: "https://claude.ai/code/artifact/2b3791d7-76b2-43af-9b13-055966926ac8"
change_policy: "Requirement IDs are stable; retired IDs never reused. Propose changes as argued deviations."
---

<!-- LLM USAGE CONTRACT (additive; not part of the source document)
1. Requirement blocks (### AL-n / AR-n / AG-n / AT-n / AX-n / AE-n) are NORMATIVE;
   all other prose is INFORMATIVE. Part 8 is an informative sourcing annex.
2. This corpus CONSOLIDATES the auditor-face requirements of MAK-FFC (AF),
   MAK-LWC (FA), and MAK-RWC (MA). Source IDs remain valid in their hosts; the
   Part 7 map is the cross-walk; a host requirement governs over any apparent
   difference here.
3. The read-model law binds generation: this face holds no write path into clinical
   data, arguments, deviations, curves, or envelopes — its writes are review states,
   dispute records, and governed change proposals, each argued and attributed. Never
   design an auditor affordance that edits clinical or knowledge-plane content
   directly.
4. Detector and telemetry outputs are flags for governed human review — never design
   auto-sanction, auto-downgrade, or auto-ratification from any signal in this face.
5. MUST violations in generated designs/code/documents require an explicit DEVIATION
   notice naming the ID.
6. Appendix A's ID census is authoritative for validator checks; Appendix B's
   self-audit checks gate any edit of this file.
END LLM USAGE CONTRACT -->

# The Abdomen Corpus

A translatable research primer and execution manual for the Auditor Face of the triple-facing CDSS — the ledger read model, review workflows, governed change, watchfulness over drift and gaming, external projection, and evaluation — consolidating the auditor-face requirements of the host corpus and both wings into one buildable face.

**Document metadata:** Technical corpus · v1.0 · 1 Sep 2026 · twelfth volume in the Mākoha research series · STATUS: normative draft · REQ IDS: AL · AR · AG · AT · AX · AE · SUBORDINATE TO: MAK-FFC v1.1 · BUILDS FROM: AF + FA + MA + MAK-CEC · GOVERNED BY: REG-POSTURE v1.0.

## Contents

1. [Part 0 — How to use this document](#part-0--how-to-use-this-document)
2. [Part 1 — Foundation: the abdomen of the butterfly](#part-1--foundation-the-abdomen-of-the-butterfly)
3. [Part 2 — The ledger read model (AL)](#part-2--the-ledger-read-model)
4. [Part 3 — Review workflows (AR)](#part-3--review-workflows)
5. [Part 4 — Governed change (AG)](#part-4--governed-change)
6. [Part 5 — Watchfulness: drift, gaming, coverage (AT)](#part-5--watchfulness-drift-gaming-coverage)
7. [Part 6 — External projection (AX)](#part-6--external-projection)
8. [Part 7 — Evaluation & consolidation maps (AE)](#part-7--evaluation--consolidation-maps)
9. [Part 8 — Execution sourcing annex](#part-8--execution-sourcing-annex)
10. [Appendix A — ID census](#appendix-a--id-census-additive)
11. [Appendix B — Self-audit checks](#appendix-b--self-audit-checks-additive)

## Thesis

> The abdomen is where the butterfly digests, stores, and reproduces — unglamorous, and the reason there is a next generation. The Auditor Face is the system's abdomen: it metabolizes everything the other surfaces produce (decisions, deviations, gaps, drift, findings) into review, governed change, and external evidence — and it is where the ecosystem reproduces itself, because the guideline feedback loop and the remodeling lifecycle are how today's practice becomes tomorrow's ratified knowledge. The series established that this face has no precedent to copy and that its reframing — documented justified deviation as a compliant state, not a mitigated violation — is the attack on the root cause of upstream rigidity. Three corpora then armed it: the host with the read-model law, argument pairs, theater detection, the feedback loop, dispute mode, and the regulator export; the left wing with the mathematics rendered on demand, the curve-change workbench, and drift telemetry; the right wing with the remodeling ledger, gap analytics, the Goodhart guard, envelope compliance, and the meta-level bundle. The face law that integrates them: one review discipline for every queue, one governed-change lifecycle behind every workbench, watchfulness that watches itself, and projections that export their own flattening. Under the assume-inclusion posture this face is not back office — it is the conformity evidence factory.

## Part 0 — How to use this document

This corpus is the Auditor Face's single execution manual, sibling to MAK-HDC and MAK-TXC. It consolidates AF, FA, and MA sources (named in traces; Part 7 is the complete cross-walk); genuinely new face law is marked *(new)*. No separate UI volume exists for this face in the butterfly plan; interaction specification stays here at behaviour level.

- **Normative language.** MUST / SHOULD / MAY per RFC 2119.
- **Requirement IDs.** `AL-n` ledger read model; `AR-n` review workflows; `AG-n` governed change; `AT-n` watchfulness; `AX-n` external projection; `AE-n` evaluation.
- **Consolidation discipline.** AF/FA/MA remain valid in their hosts; this corpus adds integration constraints and never relaxes a source MUST.
- **Regulatory precedence.** REG-POSTURE v1.0 governs. This face is where the posture's demands become artifacts: the obligations register (OBL-001..012) is evidenced from the fabric, the glass-box test (REG-FIND-004) is met by the export bundles, and gate evidence (GATE-000..004) assembles here.

## Part 1 — Foundation: the abdomen of the butterfly

**The face's evidence base, in one paragraph.** The founding finding stands: no system in the reviewed literature serves the compliance stakeholder as more than a viewer, yet the compliance apparatus is the load-bearing cause of upstream rigidity — a clinician who deviates wisely is punished by machinery that can only read deviation as error. GAAM supplies the review formalism (generic versus actual, departures localized to warrant nodes); Stranieri's ODR line supplies the contested-record workflow; the fabric supplies evidence that is append-only, version-pinned, replayable; and the corruption engine supplies the antibody against this face's own failure mode, justification theater. Both wings then doubled the face's estate: the left wing made meanings auditable (the math view, the workbench, drift telemetry) and the right wing made the meta-level auditable (remodeling ledger, gap analytics, the Goodhart guard, envelope states). The regulatory posture completes the reframing of the face itself: under assume-inclusion, its outputs are Essential Principles evidence — REG-KEEP-002's reviewable basis, REG-FIND-004's glass box, and the OBL register's proof all render here.

**What consolidation adds.** Four face-level laws emerge from reading AF, FA, and MA together. (i) *One review discipline:* deviations, gap reports, boundary findings, drift alerts, gaming flags, and envelope anomalies arrive through different pipes but get one workflow grammar — severity-ranked queues, anchored evidence, attributed verdicts at the right grain, aging with owners (AR-1). (ii) *One governed-change lifecycle:* the curve workbench, the guideline feedback loop, metric changes, and envelope changes are all instances of the MS-4 lifecycle with different evidence panels — behind every workbench, the same stages (AG-1). (iii) *Watchfulness watches itself:* drift telemetry, theater detection, and gaming detection are themselves gameable and drift-prone; the Goodhart guard applies to the face's own instruments, and campaign coverage (AD-5) renders here (AT-4). (iv) *Projections export their flattening:* every mapping from fabric states to external vocabularies — compliance categories, quality metrics, regulator formats — is a versioned artifact exported with its outputs (AX-2).

> The doctrine in one sentence: the face that judges the system must be the most judged surface in it — read-only toward care, argued in every write, and honest about every flattening.

## Part 2 — The ledger read model

**What the research revealed.** The read-model law (AF-1) is the face's constitution, and both wings widened what it reads: the left wing's math view makes any graded evaluation recomputable by hand from FML artifacts; the right wing's remodeling ledger makes the ontology's whole history reconstructible. The engine plane's verdict traces (RG-2) complete the estate: the face can now show not just what was decided but which gate stage decided it.

### Ledger requirements

### AL-1 (MUST)
**Statement:** The auditor face is a read model (MAK-FFC AF-1, carried): no write path into clinical data, arguments, deviations, curves, envelopes, or templates; its only writes are review states, dispute records, and governed change proposals — each an argued, attributed fabric entry. This law is verified by negative tests in the face's conformance suite (AE-4).
**Rationale trace:** MAK-FFC AF-1 (carried); separation of powers; Bayor surveillance-anxiety findings.

### AL-2 (MUST)
**Statement:** Every reviewable decision renders as its argument pair — GenericArgument at pinned version versus ActualArgument as it happened — with departures localized to warrant nodes (MAK-FFC AF-2, carried), extended with the evaluator's stage trace (which gate stage released, held, or flagged it — MAK-CEC RG-2) and, where graded, the full membership math on demand (MAK-LWC FA-1: fired rules, activation strengths, μ-vectors with pins, defuzzification, thresholds — recomputable by hand from the FML artifacts).
**Rationale trace:** MAK-FFC AF-2 + MAK-LWC FA-1 + MAK-CEC RG-2, consolidated; GAAM; REG-FIND-004 glass box.

### AL-3 (MUST)
**Statement:** The remodeling ledger renders the ontology's history (MAK-RWC MA-1, carried): every ontology-layer change with its complete lifecycle — triggering evidence, proposal, deliberation record, ratifier identity and authority, version delta, replay results, and the decisions pinned to superseded versions — reconstructible for any element at any date.
**Rationale trace:** MAK-RWC MA-1 (carried); SPINE-5; AG-1 dependency.

### AL-4 (MUST)
**Statement:** Every fabric query the face runs is itself ledgered (AuditEvent-bound), and clinician-level lenses inherit the governed-grant discipline in full (MAK-FFC AF-8 + MAK-LWC FA-7, consolidated): system-level and guideline-level lenses by default; individual lenses only by governed grant, logged, and visible to the affected clinician.
**Rationale trace:** MAK-FFC AF-8 + MAK-LWC FA-7; MAK-RWC MA-6; procedural fairness.

### AL-5 (SHOULD)
**Statement:** The face renders the system's self-description at audit grain (MAK-RWC MS-6): current envelopes, active rebuttals, drift state, and open change proposals per element — the auditor's "what does the system believe about itself today" view, generated from fabric data.
**Rationale trace:** MAK-RWC MS-6/MA-5; conformity-evidence readiness.

## Part 3 — Review workflows

**What the research revealed.** The consolidated face inherits six review streams (deviations, gap reports, boundary-sweep findings, drift alerts, gaming/theater flags, envelope anomalies) from three corpora, each specified separately. The face law is one workflow grammar — because six bespoke workflows guarantee six inconsistent disciplines, and reviewer capacity is the scarcest resource this face has.

### Review requirements

### AR-1 (MUST)
**Statement:** One review grammar serves every queue: items arrive severity-ranked with their evidence anchored (argument pair, finding object, telemetry extract), verdicts attach at the correct grain (warrant node for deviations and findings per MAK-FFC AF-2; element for drift; case set for gaming flags), every verdict is attributed and argued, and queues age visibly with named owners — accumulation without ownership is a monitored anomaly.
**Rationale trace:** MAK-FFC AF-2 + MAK-LWC FA-6 + MAK-RWC MA anti-requirement (aged queues), consolidated *(new as one grammar)*; reviewer-capacity economics.

### AR-2 (MUST)
**Statement:** The compliance vocabulary distinguishes the consolidated states as first-class: guideline-concordant; documented justified deviation (a compliant state, not a mitigated violation — the reframing); documented deviation under review; undocumented deviation (MAK-FFC AF-3, carried); plus the envelope states — released in-envelope, released out-of-envelope with recorded fit-judgment, released out-of-envelope without recorded judgment (MAK-RWC MA-4, carried) — the last being the reviewable anomaly, derived from gate records, never retrospective inference.
**Rationale trace:** MAK-FFC AF-3 + MAK-RWC MA-4, consolidated; the series' central reframing.

### AR-3 (MUST)
**Statement:** Boundary-sweep and campaign findings queue with the review discipline of deviations (MAK-LWC FA-6, elevated): severity-ranked, warrant-anchored, resolvable only by acknowledgment (rebuttal published) or governed change (AG-1 path) — never by silent dismissal.
**Rationale trace:** MAK-LWC FA-6 (elevated to MUST at the consolidated face); MAK-CEC AD-2/AD-3.

### AR-4 (SHOULD)
**Statement:** Dispute mode implements the structured ODR workflow (MAK-FFC AF-6, carried): contested decision or record, positions entered as arguments, mediated exchange, outcome ledgered — reachable from payer disputes, patient record challenges (MAK-TXC TA-5), and inter-clinician escalation.
**Rationale trace:** MAK-FFC AF-6 (carried); Stranieri Re-Consider → medical ODR lineage.

### AR-5 (MUST)
**Statement:** Review outcomes feed forward deterministically: a verdict that acknowledges a finding publishes the rebuttal; one that confirms systematic misfit routes to remodeling detection; one that confirms gaming routes to the governed human process (never automatic sanction — MAK-FFC AF-4 discipline); and every route is recorded on the item.
**Rationale trace:** MAK-CEC AD-3 routing read from the face side; MAK-FFC AF-4; MAK-RWC MS-4.

## Part 4 — Governed change

**What the research revealed.** This face owns the system's reproduction: the guideline feedback loop (AF-5), the curve-change workbench (FA-2/5), values-mapping ratification, metric changes (MA-3), and envelope changes are all ontology-layer change — and the right wing unified them under one lifecycle (MS-4). The consolidation duty is to make the workbenches instances, not siblings: same stages, same replay gates, same ledger, different evidence panels.

### Governed-change requirements

### AG-1 (MUST)
**Statement:** Every workbench is an instance of the one lifecycle: guideline feedback (MAK-FFC AF-5), curve change (MAK-LWC FA-2), values mappings (MAK-TXC TA-2), metric definitions (MAK-RWC MA-3), and envelope changes all pass detect → propose → deliberate → ratify → version → replay (MAK-RWC MS-4), with stage records in the remodeling ledger (AL-3) and no side door: no face, role, or configuration path changes any governed artifact outside its workbench — including temporary, per-site, or emergency changes.
**Rationale trace:** MAK-RWC MS-4 + MAK-FFC AF-5 + MAK-LWC FA-2, consolidated; the corrected-dial doctrine.

### AG-2 (MUST)
**Statement:** Proposals carry their evidence and their consequences: the evidence panel (deviation aggregates, gap analytics, drift metrics, credibility scores, campaign findings — per change class) plus the impact preview — a human-readable diff (FML diff for curves per MAK-LWC FA-5; template diff for guideline nodes; schema diff for metrics) and the replay divergence report (MAK-CEC RG-4) with flips enumerated. Ratification without a current impact preview is invalid.
**Rationale trace:** MAK-LWC FA-5 + MAK-CEC RG-4 + MAK-RWC ME-5, consolidated; informed-ratification doctrine.

### AG-3 (MUST)
**Statement:** Aggregated practice generates change pressure through the loop, never around it: recurring justified deviations against a warrant node, clustered gap reports, and sustained drift generate proposals carrying that evidence (MAK-FFC AF-5 + MAK-RWC MA-2, consolidated); ratification versions the template and the old version stays pinned to its history. Telemetry informs proposals; nothing auto-ratifies (MAK-LWC FA-3, carried in force).
**Rationale trace:** MAK-FFC AF-5 + MAK-RWC MA-2 + MAK-LWC FA-3; Chapman (remodeling is a governed human act).

### AG-4 (SHOULD)
**Statement:** Deliberation stages are chartered trading zones (MAK-RWC MS-8): each change class names its forum, participants, boundary objects, and authority — patient-affecting changes include the patient-council stage (MAK-TXC TA-4); clinical-content changes include practising clinicians who did not author the proposal.
**Rationale trace:** MAK-RWC MS-8/MP-6; ratification legitimacy; evaluation-incest lesson at the governance layer.

## Part 5 — Watchfulness: drift, gaming, coverage

**What the research revealed.** The face's standing instruments — semantic drift telemetry (FA-3), theater detection (AF-4), gaming detection (MA-3), campaign coverage (AD-5) — share a failure mode: instruments become targets, watchers go stale, and vigilance becomes theater. The right wing's Goodhart guard generalizes: every metric the face computes is a versioned, argued artifact, and the guard applies reflexively to the face's own instruments.

### Watchfulness requirements

### AT-1 (MUST)
**Statement:** Semantic drift telemetry runs continuously per LinguisticVariable — boundary-band density, override clustering near thresholds, aggregate PIS divergence, credibility trend (MAK-LWC FA-3, carried) — alongside the right wing's streams: gap-report pressure by element and population with the equity lens (MAK-RWC MA-2, carried), and the cross-wing joint review on schedule (MA-7: degree drift and fit pressure read together).
**Rationale trace:** MAK-LWC FA-3 + MAK-RWC MA-2/MA-7, consolidated; MAK-MIF beat 3.

### AT-2 (MUST)
**Statement:** Theater and gaming detection run continuously over the justification ledger and the metric streams — boilerplate similarity, duplication clusters, temporal anomalies, taxonomy/free-text divergence (MAK-FFC AF-4, carried); distributional anomalies, threshold bunching, pre-audit spikes (MAK-RWC MA-3, carried) — producing flags for governed human review only: no auto-sanction, no auto-downgrade, no individual performance feed without the governed process.
**Rationale trace:** MAK-FFC AF-4 + MAK-RWC MA-3, consolidated; procedural fairness; Chapman rationality theater.

### AT-3 (MUST)
**Statement:** Every metric this face computes — compliance rates, queue ages, drift indices, detector precision — is a versioned, argued artifact with stated purpose and known failure modes, changed only through AG-1 (MAK-RWC MA-3's Goodhart law, carried as face law); completion-rate and throughput metrics over clinical surfaces carry their documented hazards (MAK-TXC TA-3, MAK-HDC HG-4).
**Rationale trace:** MAK-RWC MA-3 (carried); Goodhart's law; metric-as-target risk.

### AT-4 (MUST)
**Statement:** Watchfulness watches itself: campaign coverage (which surface the adversary has never attacked — MAK-CEC AD-5) renders on this face's system lens; detector performance (flag precision from review outcomes) is telemetry; and stale instruments — detectors unchanged while the ledger's character shifts, telemetry silent on active elements — are surfaced as anomalies with owners.
**Rationale trace:** MAK-CEC AD-5 (rendered here) + the reflexive Goodhart move *(new — the face audits its own instruments)*.

### AT-5 (SHOULD)
**Statement:** Anytime-valid monitoring methods (conformal test martingales and successors) are the preferred mathematics for the face's continuous streams, so alarm rates are controlled and alarms carry diagnostic type (drift class, shift class) rather than bare thresholds.
**Rationale trace:** WCTM/monitoring literature (MAK-RWC Part 9); false-alarm economics; AR-1 queue protection.

## Part 6 — External projection

**What the research revealed.** The regulator export (AF-7) was designed to TGA criterion (c)'s language; REG-POSTURE re-grounds it: the same bundles now serve Essential Principle 13 evidence under assume-inclusion (REG-KEEP-002), the glass-box demonstration (REG-FIND-004), the obligations register (OBL-001..012), and gate evidence (GATE-000..004). The wings added what must not be lost in flattening: the graded-state projection (FA-4) and the meta-level bundle (MA-5).

### Projection requirements

### AX-1 (MUST)
**Statement:** Regulator export produces self-contained conformity bundles (MAK-FFC AF-7, carried): the decision set with pinned versions, replay attestation, argument transparency (basis, logic, evidence references), deviation and envelope states, and adverse-event linkage — extended with the meta-level bundle (MAK-RWC MA-5, elevated): remodeling ledger extracts, gap analytics summaries, envelope-compliance states, and pinned self-description — the operational glass-box evidence.
**Rationale trace:** MAK-FFC AF-7 + MAK-RWC MA-5 (elevated to MUST at the consolidated face); REG-FIND-004; REG-KEEP-002.

### AX-2 (MUST)
**Statement:** Every projection exports its flattening: the mapping from fabric states to any external vocabulary — compliance categories (AF-3 states), quality metrics, the graded-state projection (MAK-LWC FA-4, carried), regulator formats — is a ratified, versioned artifact shipped with its outputs, so the reviewer can audit the mapping, not merely its results.
**Rationale trace:** MAK-LWC FA-4 (carried, generalized); honesty at the reporting boundary *(generalization new)*.

### AX-3 (MUST)
**Statement:** The obligations register is evidenced from the fabric: each REG-POSTURE obligation (OBL-001..012) and each J-3 residual (MAK-J3 §5) has a named owner and a standing evidence query — SBOMs and suite results, adverse-event chains, advertising-claims boundary, notification records — such that obligation status is generated, not asserted.
**Rationale trace:** REG-POSTURE OBL register; MAK-J3 GPP-2 pattern generalized; conformity-evidence-factory doctrine *(new as face duty)*.

### AX-4 (SHOULD)
**Statement:** Gate evidence assembles here: the artifacts each REG-POSTURE gate consumes (GATE-000 counsel records, GATE-001 risk-file and pinning evidence, GATE-002 controls-operating proof, GATE-003 clinical-evidence and testing records, GATE-004 conformity application set) have standing bundle definitions, so gate reviews read prepared evidence rather than commissioning archaeology.
**Rationale trace:** REG-POSTURE GATE-000..004 / TASK-REG structure; Ketryx binding (MAK-RWC MX-4).

## Part 7 — Evaluation & consolidation maps

### Evaluation requirements

### AE-1 (MUST)
**Statement:** The face's founding validation is reconstruction: an external reviewer, from exports alone, reconstructs a month of decisions (MAK-FFC P2 gate, carried), any graded evaluation by hand from FML artifacts (MAK-LWC FA-1 test), and the ontology's history for any element (MAK-RWC MA-1 test) — run as a recurring exercise, not a one-time gate.
**Rationale trace:** MAK-FFC phasing P2 + MAK-LWC FA-1 + MAK-RWC MA-1, consolidated into a standing audit *(new as recurring)*.

### AE-2 (MUST)
**Statement:** Reviewer-facing evaluation is measured: verdict consistency across reviewers on seeded cases, time-to-verdict by queue class, flag-precision curves per detector, and reframing fidelity — documented justified deviations projected as compliant in external reporting, verified per release (the reframing is worthless if the projection betrays it).
**Rationale trace:** AR-1/AR-2; MAK-FFC AF-3; detector-quality economics *(new)*.

### AE-3 (SHOULD)
**Statement:** Institutional acceptance is studied, not assumed: the AF-3 reframing requires payers and accreditors to accept "documented justified deviation" as compliant — a study design with a real payer, using AX-1 bundles, remains the face's highest-stakes open validation (carried from the host corpus's research agenda).
**Rationale trace:** MAK-FFC open research agenda (auditor acceptance); AX-1/AX-2 evidence.

### AE-4 (MUST)
**Statement:** The face's conformance suite gates its releases: read-model negative tests (no write path to clinical or knowledge-plane content — AL-1), workbench-bypass negative tests (no governed artifact changeable outside AG-1), projection-parity tests (external outputs match their exported mappings — AX-2), lens-discipline tests (AL-4), and no-auto-consequence tests (no detector output reaches sanction, downgrade, or ratification without the governed step — AT-2, AG-3). Results are conformity-file artifacts.
**Rationale trace:** MAK-CEC RG-8 pattern at this face; the face's own anti-capture laws *(new)*.

### Auditor Face anti-requirements (consolidated)

- Never a write path into clinical or knowledge-plane content — the auditor observes and proposes; it does not practice medicine or edit meanings (AF-1/FA-2, carried).
- Never automatic sanction, metric downgrade, clinician flagging, or curve ratification from any detector or telemetry output (AF-4/FA-3/MA-3, carried).
- Never real-time individual surveillance dashboards; review is retrospective and governed (AF-8, carried).
- Never resolve plural-guideline conflicts by fiat in any projection; conflicts project as conflicts (SPINE-6, carried).
- Never export a flattened state without the versioned mapping that produced it (FA-4/AX-2).
- Never let queues age without owners, or instruments go stale without alarm (AR-1, AT-4).
- Never treat activation strengths or any signal in the math view as confidence — the compliance register obeys the five-signal registry like every other register (MAK-LWC, carried; MAK-CEC OM-3).

### Three-corpus consolidation map (complete for the auditor face)

| Source requirement | Disposition here | Carrier |
|---|---|---|
| MAK-FFC AF-1 (read model) | carried | AL-1 |
| MAK-FFC AF-2 (argument pairs, warrant grain) | consolidated | AL-2, AR-1 |
| MAK-FFC AF-3 (compliance states; the reframing) | consolidated | AR-2, AE-2 |
| MAK-FFC AF-4 (theater detection, human-review-only) | consolidated | AT-2 |
| MAK-FFC AF-5 (guideline feedback loop) | consolidated | AG-1, AG-3 |
| MAK-FFC AF-6 (dispute mode) | carried | AR-4 |
| MAK-FFC AF-7 (regulator export) | consolidated | AX-1 |
| MAK-FFC AF-8 (governed lenses) | consolidated | AL-4 |
| MAK-LWC FA-1 (membership math view) | consolidated | AL-2, AE-1 |
| MAK-LWC FA-2 (curve change only via workbench) | consolidated | AG-1 |
| MAK-LWC FA-3 (drift telemetry, never auto-trigger) | consolidated | AT-1, AG-3 |
| MAK-LWC FA-4 (versioned graded-state projection) | carried, generalized | AX-2 |
| MAK-LWC FA-5 (FML diff + impact preview) | consolidated | AG-2 |
| MAK-LWC FA-6 (findings reviewed like deviations) | elevated (SHOULD→MUST) | AR-3 |
| MAK-LWC FA-7 (lens discipline over graded data) | consolidated | AL-4 |
| MAK-RWC MA-1 (remodeling ledger) | carried | AL-3 |
| MAK-RWC MA-2 (gap analytics, equity lens) | consolidated | AT-1, AG-3 |
| MAK-RWC MA-3 (Goodhart guard) | carried as face law | AT-3 |
| MAK-RWC MA-4 (envelope compliance states) | consolidated | AR-2 |
| MAK-RWC MA-5 (meta-level bundle) | elevated (SHOULD→MUST) | AX-1 |
| MAK-RWC MA-6 (meta-rational acts never punished by default) | carried | AL-4, AT-2 |
| MAK-RWC MA-7 (cross-wing review) | consolidated | AT-1 |

### MAK-MIF beat map (face landings)

| Beat | Face landing | Carrier |
|---|---|---|
| 3 · Meaning under governance | Drift telemetry feeds the workbench; ratification versions; old meanings replay | AT-1, AG-1..3 |
| 4 · Conflict with a metric | Recorded conflict navigations reviewable; projections never resolve by fiat | AR-2, AX-2 |
| 7 · The adversary's map | Findings queued with review discipline; coverage of the attack surface rendered | AR-3, AT-4 |

### Findings → requirements

| Finding | Source | Requirements it drives |
|---|---|---|
| No precedent serves the compliance stakeholder; compliance machinery causes upstream rigidity | MAK-FFC Part 5 founding finding; Bayor 2025 | the corpus's existence; AR-2 |
| Deviation is formalizable at warrant grain (generic vs actual) | GAAM 2006 | AL-2, AR-1 |
| Contested records need structured ODR | Stranieri Re-Consider 2008 → medical ODR 2020 | AR-4 |
| Whoever tunes the curve tunes the meaning; change must be governed and replayed | MAK-LWC corrected-dial doctrine; MAK-DOT FZ-4 | AG-1/2 |
| Meanings drift measurably; telemetry informs, never ratifies | Pei 2024; MAK-MIF beat 3 | AT-1, AG-3 |
| Metrics become targets; justifications become boilerplate | Goodhart; Chapman rationality theater | AT-2/3/4 |
| Gaps cluster on underserved subpopulations; equity is a ledger property | MAK-RWC MA-2; Cockburn 2024 | AT-1 |
| The glass-box test and reviewable basis are the conformity case | REG-FIND-003/004; REG-KEEP-002 | AX-1, AE-1 |
| Obligations and gates need generated evidence, not assertions | REG-POSTURE OBL/GATE/TASK-REG structure | AX-3/4 |
| Anytime-valid monitoring controls false alarms on live streams | WCTM literature (MAK-RWC Part 9) | AT-5 |

### Sources

- Series: MAK-FFC v1.1 Part 5 · MAK-LWC v1.1 Part 5 · MAK-RWC v1.1 Part 5 · MAK-CEC v1.1 (verdict traces, telemetry, replay, campaign coverage) · MAK-HDC v1.0 · MAK-TXC v1.0 · MAK-MIF v1.0 · REG-POSTURE v1.0 (REG-KEEP-002, REG-FIND-004, OBL-001..012, GATE-000..004; cited by stable ID).
- GAAM (DSS 2006); Split-Up lineage; Re-Consider (2008); medical ODR (2020); EHR disputes & emotional intelligence (BIT 2020) — provenance in The Stranieri File.
- Bayor et al. 2025 (JMIR); Cockburn et al. 2024 (eClinicalMedicine); Abbas et al. 2025 (Healthcare).
- Pei et al. 2024 (membership-function credibility, IEEE TFS) via MAK-LWC; anytime-valid monitoring literature (Prinster 2025; Timans 2025) via MAK-RWC Part 9.
- TGA guidance lineage and FDA revised CDS guidance via MAK-FFC/MAK-J3; ISO 13485 deemed-conformity lever via REG-POSTURE (REG-FIND-006).

*Document footer (source artifact):* The Abdomen Corpus v1.0 · requirement IDs are stable; propose changes as argued deviations — this document practices its own doctrine. Compiled from the three host corpora, MAK-CEC/HDC/TXC, REG-POSTURE v1.0, and the series' verified evidence base, 1 Sep 2026.

## Part 8 — Execution sourcing annex

The auditor face inherits the series' deepest confirmed absence: MAK-ELSM found no precedent in public code for the justification fabric, deviation ledger, or compliance projector, and both wings' annexes confirmed the pattern for their estates (no curve-governance workbench; no remodeling ledger). This annex consolidates the face's sourcing view; carried statuses are dated observations from their host annexes.

### Consolidated sourcing view

| Face part | Adopt/adapt (verified in host annexes) | Build (no precedent found) |
|---|---|---|
| Ledger read model (AL) | Aurora + transparency-log pattern (ELSM-19) or immudb (ELSM-17, BUSL review) as the store; HAPI FHIR Provenance/AuditEvent (ELSM-20) as the data plane | The read model itself: argument pairs, stage-trace rendering, membership math view, remodeling history |
| Review workflows (AR) | TweetyProject/Carneades semantics for argument evaluation support (ELSM-07/08); Stranieri ODR literature as design source | The one-grammar review system; the compliance-state projector; dispute mode |
| Governed change (AG) | openregulatory/templates (ELSM-R04) for document-layer records; Ketryx-on-Jira (commercial, ASSUME-REG-006) as lifecycle system of record; JFML/IEEE 1855 (MAK-LWC Part 9) for FML diffing substrate | Every workbench: curve change, guideline feedback, metric governance — the moat's governance floor |
| Watchfulness (AT) | evidently (ELSM-R02) and alibi-detect (ELSM-R01) as telemetry/drift machinery; Giskard/ART (ELSM-15/16) harnesses; WCTM-class methods (literature) | Semantic-drift metrics per LinguisticVariable; theater/gaming detectors' clinical content; the reflexive coverage view (AT-4) |
| External projection (AX) | FHIR bulk-export machinery (HAPI); CycloneDX SBOM tooling (via MAK-J3 GPP-8 practice) | Conformity bundles, flattening-mapping exports, the generated obligations register |

### The face's build list (consolidated; methodology hedge carried)

The compliance projector with exported flattenings; the one-grammar review system over six queues; the remodeling ledger read model; the curve-change and guideline workbenches as lifecycle instances; theater/gaming detection content; the generated obligations register and gate bundles. MAK-ELSM's verdict stands, sharpened: this face is the moat's largest contiguous parcel — nothing here is buyable beyond storage, semantics, and telemetry machinery.

### Face-relevant research plane (carried)

Anytime-valid monitoring (AT-5's mathematics); the auditor-acceptance study (AE-3) remains the field's open institutional question with no published precedent; detector-precision economics for clinical justification ledgers is unstudied — AE-2 produces first evidence.

## Appendix A — ID census (additive)

Authoritative enumeration for validator checks. Count: **27**.

```json
{
  "doc_id": "MAK-ABC",
  "version": "1.0",
  "requirements": {
    "AL": ["AL-1","AL-2","AL-3","AL-4","AL-5"],
    "AR": ["AR-1","AR-2","AR-3","AR-4","AR-5"],
    "AG": ["AG-1","AG-2","AG-3","AG-4"],
    "AT": ["AT-1","AT-2","AT-3","AT-4","AT-5"],
    "AX": ["AX-1","AX-2","AX-3","AX-4"],
    "AE": ["AE-1","AE-2","AE-3","AE-4"]
  },
  "levels": {
    "MUST":   ["AL-1","AL-2","AL-3","AL-4","AR-1","AR-2","AR-3","AR-5","AG-1","AG-2","AG-3","AT-1","AT-2","AT-3","AT-4","AX-1","AX-2","AX-3","AE-1","AE-2","AE-4"],
    "SHOULD": ["AL-5","AR-4","AG-4","AT-5","AX-4","AE-3"],
    "MAY":    []
  },
  "retired": []
}
```

Census arithmetic: 21 MUST + 6 SHOULD + 0 MAY = 27 (5+5+4+5+4+4 across the six families).

## Appendix B — Self-audit checks (additive)

1. **ID uniqueness** — no requirement ID appears in more than one requirement header.
2. **ID census parity** — headers matching `^### (AL|AR|AG|AT|AX|AE)-\d+ \((MUST|SHOULD|MAY)\)$` exactly equal Appendix A's enumeration.
3. **Level parity** — header levels match Appendix A buckets.
4. **Trace presence** — every requirement block has a non-empty rationale trace.
5. **Normative leakage** — no capitalized MUST/SHOULD/MAY outside requirement blocks, anti-requirement bullets, quoted text, or this appendix.
6. **Consolidation integrity** — every AF/FA/MA requirement appears in the Part 7 map with a disposition; no source requirement relaxed (elevation permitted and named).
7. **Cross-reference integrity** — every AL/AR/AG/AT/AX/AE ID cited exists in the census; every host-document ID cited resolves in its host.
8. **Regulatory precedence** — OBL/GATE/REG-KEEP/REG-FIND cited as stated; ASSUME-REG items never described as closed.
9. **Table integrity** — consistent column counts per row.
10. **Stability** — IDs from previous versions present or explicitly retired; never reused.
