---
doc_id: MAK-LBP
title: "The Labial Palps Corpus"
version: "1.0"
date: "2026-09-01"
series: "Mākoha research series — volume 15 · the Clinician UI, implementing MAK-HDC"
status: normative-draft
normative_language: RFC-2119 (MUST / SHOULD / MAY)
req_prefixes: [CV, CS, CC, CI, CA]
req_count: 26
subordinate_to: "MAK-HDC v1.0 — this volume specifies interaction and presentation for the Clinician Face; every HDC requirement governs; nothing here relaxes one"
implements:
  - "MAK-HDC v1.0 (The Head Corpus) — the Clinician Face behaviour this UI realizes"
  - "MAK-LWC v1.1 clinician components (graded criterion chips, borderline flag, membership sketch, ratified trend descriptors)"
  - "MAK-RWC v1.1 clinician components (envelope renderer, gap reporter, conflict workbench, self-description panel)"
  - "MAK-CEC v1.1 (the five-signal registry and verdict stream this UI renders)"
governed_by:
  - "REG-POSTURE v1.0 via MAK-ANT — REG-KEEP-002/003 realized at the interaction layer (sign-off sheet, basis always reachable)"
changelog:
  - "v1.0 (2026-09-01): initial release — 26 requirements across CV/CS/CC/CI/CA; screen and component inventories; UI conformance suite."
companions:
  - "MAK-HDC v1.0 (governing face corpus) · MAK-PRB v1.0 (patient-side sibling) · MAK-ANT v1.0 (regulatory sensing)"
artifact_url: "https://claude.ai/code/artifact/7548629d-db1a-4e7f-b60d-c88dc37123c6"
change_policy: "Requirement IDs are stable; retired IDs never reused. Propose changes as argued deviations."
---

<!-- LLM USAGE CONTRACT (additive; not part of the source document)
1. Requirement blocks (### CV-n / CS-n / CC-n / CI-n / CA-n) are NORMATIVE; all other
   prose is INFORMATIVE. Inventories are catalogues, normative only where a
   requirement cites them.
2. This volume IMPLEMENTS MAK-HDC: every screen and component realizes named HDC
   requirements; a UI decision violating an HDC (or deeper host) MUST is invalid.
3. The five-signal identity system binds generation (CV-1): posterior, coverage,
   membership, reliability, and fit each have exactly one visual identity — never
   design a gauge, score, or color scale that blends them.
4. The one-surface law binds generation: every widget renders evaluator-released
   argument objects; never design a display fed by a side channel (MAK-HDC HR-1).
5. MUST violations in generated designs/code/documents require an explicit DEVIATION
   notice naming the ID.
6. Appendix A's ID census is authoritative for validator checks; Appendix B's
   self-audit checks gate any edit of this file.
END LLM USAGE CONTRACT -->

# The Labial Palps Corpus

A translatable execution manual for the Clinician UI of the triple-facing CDSS — the clinical register's visual identity system, the screen set, the component library, the interaction laws, and the density, embedding, and accessibility rules — implementing the Head Corpus at the pixel and keystroke level.

**Document metadata:** UI corpus · v1.0 · 1 Sep 2026 · fifteenth volume in the Mākoha research series · STATUS: normative draft · REQ IDS: CV · CS · CC · CI · CA (26) · SUBORDINATE TO: MAK-HDC v1.0 · IMPLEMENTS: the Clinician Face.

## Contents

1. [Part 0 — How to use this document](#part-0--how-to-use-this-document)
2. [Part 1 — Why labial palps](#part-1--why-labial-palps)
3. [Part 2 — The clinical identity system (CV)](#part-2--the-clinical-identity-system)
4. [Part 3 — The screen set (CS)](#part-3--the-screen-set)
5. [Part 4 — The component library (CC)](#part-4--the-component-library)
6. [Part 5 — Interaction laws (CI)](#part-5--interaction-laws)
7. [Part 6 — Density, embedding & accessibility (CA)](#part-6--density-embedding--accessibility)
8. [Part 7 — Traceability & conformance](#part-7--traceability--conformance)
9. [Appendix A — ID census](#appendix-a--id-census-additive)
10. [Appendix B — Self-audit checks](#appendix-b--self-audit-checks-additive)

## Thesis

> Labial palps are the butterfly's food-testers: paired sensors flanking the proboscis that judge, before anything is drunk, whether this is nourishment. The Clinician UI is the system's paired tester — the surface where a professional judges, case by case and in seconds, whether the machinery's output deserves trust. The Head Corpus says what that surface does: one argument surface, five typed signals, evidence-gated interruptions, fail-closed sign-off, acts that cost one interaction. This volume says how it survives contact with a nine-minute consultation: a brief that reads in ninety seconds, chips that show degree without pretending it is probability, an envelope badge that cannot be missed at the moment it matters, a deviation sheet that costs one tap and no shame, and a sign-off act that feels like signing — deliberate, attributed, and reversible until committed. The design has one test: a competent clinician who has never seen the system can, within one consultation, find the basis of any recommendation, disagree with it honestly, and leave a record that protects both patient and practitioner.

## Part 0 — How to use this document

This volume is the interaction-level companion to MAK-HDC: every requirement realizes named HDC requirements (the Part 7 map is complete), and HDC governs on any apparent conflict. It is written to be handed to a design-and-build team; visual identity (brand, exact type, color values) is deliberately unfixed — the laws constrain structure, identity separation, and behaviour, not taste.

- **Normative language.** MUST / SHOULD / MAY per RFC 2119.
- **Requirement IDs.** `CV-n` identity system; `CS-n` screens; `CC-n` components; `CI-n` interaction laws; `CA-n` density, embedding, accessibility.
- **Stack note.** UI technology is the Legs volume's concern; nothing here presumes a framework. EHR embedding follows the delivery vectors verified in MAK-HDC Part 8 (CDS Hooks cards, SMART apps).

## Part 1 — Why labial palps

Three design facts govern everything below. First, **time is the clinician's scarcest signal**: the Blake pattern won by making the consultation read-and-decide; this UI's core discipline is the reading budget (HDC HW-3) — density without noise, drill-down without hunting. Second, **the five signals live or die at the pixel**: the series' hardest-won law (OM-3) fails silently the first time a designer draws one gauge over two signals; the identity system (CV-1) is the law's last line of defence, and the conflation rate is a measured evaluation outcome (HDC HE-1). Third, **acts must be cheaper than avoidance**: deviation, gap reporting, and fit-judgment protect the patient and the record only if the honest path costs one interaction and no shame — friction anywhere in those flows is a safety defect, not a polish issue.

> The doctrine in one sentence: ninety seconds to the picture, one interaction to the basis, one interaction to disagree, and five signals that never wear each other's clothes.

## Part 2 — The clinical identity system

### CV-1 (MUST)
**Statement:** The five-signal identity system is the design system's core: posterior (belief), coverage (set + stated coverage), membership (degree with term label), reliability (source-stated sureness), and fit (envelope status) each have exactly one visual identity — distinct encoding family, distinct label vocabulary, distinct placement grammar — applied identically on every screen. No gauge, composite score, ranking glyph, or color scale blends two signals; the identity sheet is a versioned design artifact and its violation is a build failure (MAK-HDC HR-2).
**Rationale trace:** MAK-HDC HR-2 (realized); MAK-CEC OM-3; MAK-LWC FC-3; conflation as the face's measured failure mode (HE-1).

### CV-2 (MUST)
**Statement:** Degree never wears verdict's clothes: membership renders as chip + term + glanceable graphic (never traffic-light red/green), with the ratified cut shown wherever release logic binarized (MAK-LWC FC-1); boundary proximity renders as the borderline flag, an invitation styled distinctly from alerts.
**Rationale trace:** MAK-LWC FC-1/FC-2 + anti-requirements (realized); MAK-HDC HA-2.

### CV-3 (MUST)
**Statement:** Fit has surface-level weight parity: the envelope badge (in / out-with-named-attributes / unknown) renders at the recommendation's own visual weight, adjacent to it, before drill-down — never as a footnote, tooltip, or secondary tab (MAK-HDC HR-3's parity clause).
**Rationale trace:** MAK-HDC HR-3 / MAK-RWC MC-1 (realized); REG-FIND-004 glass-box at the surface.

### CV-4 (MUST)
**Statement:** Microcopy is linted against the prohibited-vocabulary list at build time: no confidence/probability language for membership or fit, no "overall score" phrasing anywhere, and rebuttal and drift notices use the ratified caution vocabulary (MAK-HDC HR-5's lint, realized).
**Rationale trace:** MAK-HDC HR-5; MAK-LWC FC-6; copy-as-conformance.

### CV-5 (SHOULD)
**Statement:** The identity system ships with a conflation test kit: standardized screens and tasks measuring signal-identification and cross-signal confusion rates, used in HE-1 evaluations and re-run on any identity-sheet change.
**Rationale trace:** MAK-HDC HE-1/HE-3; MAK-LWC FC-7 μ-misreading ceiling; instrumented design.

## Part 3 — The screen set

The screen inventory (informative catalogue; requirements govern):

| Screen | Purpose | HDC anchor |
|---|---|---|
| Consult-Prep Brief | The pre-encounter read: synthesis, triage proposal with argument, active envelopes, applicable rebuttals — under the reading budget | HW-2/3 |
| Differential Board | Ranked hypotheses; per-row: qualifier, envelope badge, rebuttal marker; expand to argument tree | HR-3/4 |
| Argument View | Full Toulmin tree at criterion grain; graded chips; stage trace on demand | HR-3, AL-2 twin |
| Deviation Sheet | One-tap structured departure + preview of the auditor view | HA-2 |
| Gap Sheet | One-tap "doesn't fit"; deviate-vs-gap distinction rendered | HA-3 |
| Fit-Judgment Sheet | Flagged-content flow: mismatch named, judgment recorded | HA-4 |
| Conflict Bench | Side-by-side conflict rendering; recorded navigation | HA-5 |
| Sign-off Bar | The terminal act: what will be released, to whom, at which argument version | HA-1 |
| Self-Description Panel | "What is this system bad at," current envelopes, recent changes | HR-6 |
| My Attention | The clinician's own interruption analytics and suppression rules | HG-5 |

### CS-1 (MUST)
**Statement:** The Consult-Prep Brief renders within its ratified reading budget (MAK-HDC HW-3): a ninety-second core read at the top (situation, triage proposal, what changed, what needs deciding), with every element one interaction from its full argument and overflow collapsed behind drill-down — never a longer default page per encounter class than the budget allows.
**Rationale trace:** MAK-HDC HW-2/3 (realized); Blake assimilable-brief evidence.

### CS-2 (MUST)
**Statement:** The Differential Board renders each hypothesis row with its three inseparables — qualifier (posterior + coverage per identity system), envelope badge (CV-3), and rebuttal marker where confirmed findings apply — and expansion opens the Argument View in place. Rows never render a bare rank or score (MAK-HDC HR-3).
**Rationale trace:** MAK-HDC HR-3 (realized); SPINE-2 at the row.

### CS-3 (MUST)
**Statement:** The Argument View renders the Toulmin tree at criterion granularity: claim, grounds with encoding traces on demand, warrant with its guideline citation and version, backing with evidence tier, qualifier and rebuttals per identity system, graded chips with cuts (CV-2), and the evaluator's stage trace on demand ("why am I seeing this / why flagged") — all within one interaction of any displayed recommendation (MAK-HDC HR-3/HR-4).
**Rationale trace:** MAK-HDC HR-3/4 (realized); REG-KEEP-002; Spitzer 2026 (argument-shaped display).

### CS-4 (MUST)
**Statement:** The three act sheets (Deviation, Gap, Fit-Judgment) share one interaction grammar: one tap to open from the element in focus, pre-populated context, structured reason + optional free text, explicit preview of how the record will appear to the auditor face, one tap to commit — and the deviate-versus-gap distinction is rendered at the point of choice (MAK-HDC HA-2/3/4).
**Rationale trace:** MAK-HDC HA-2/3/4 (realized); one-grammar economy; CF-3 friction law.

### CS-5 (MUST)
**Statement:** The Sign-off Bar is the only release control: it states exactly what will be released, to whom, in which register, at which argument version; it is a deliberate distinct act (never bundled into navigation, never default-focused, never keyboard-fallthrough), attributable, and absent sign-off the state is no action (MAK-HDC HA-1).
**Rationale trace:** MAK-HDC HA-1 / REG-KEEP-003 (realized); fail-closed at the control.

### CS-6 (SHOULD)
**Statement:** The Conflict Bench renders both sides at full argument structure with envelopes and graded applicability per identity system, supports a recorded navigation (choice + reasons + residue), and displays sides in ratified neutral order (never model-ranked).
**Rationale trace:** MAK-HDC HA-5 (realized); MS-5 no-pre-ranking.

## Part 4 — The component library

The component inventory (informative catalogue; requirements govern):

| Component | Function | Source spec |
|---|---|---|
| Graded Criterion Chip | μ + term + glanceable graphic + ratified cut | MAK-LWC FC-1 |
| Borderline Flag | Distance-to-threshold invitation, one-tap to Deviation Sheet | MAK-LWC FC-2 |
| Envelope Badge | in / out(attrs) / unknown at weight parity | MAK-RWC MC-1 |
| Qualifier Block | Posterior + conformal set + stated coverage, identity-styled | MAK-CEC QU-1 |
| Rebuttal Marker | Confirmed findings applicable to this claim, one tap to detail | MAK-HDC HR-3 |
| Stage-Trace Peek | The evaluator pipeline trace, on demand | MAK-CEC RG-2 |
| Act Sheets (×3) | Deviation / Gap / Fit-judgment, one grammar | MAK-HDC HA-2..4 |
| Sign-off Bar | The terminal act control | MAK-HDC HA-1 |
| Interruption Cards | Alerts, flags, prompts, fit warnings — one budgeted presentation system | MAK-HDC HG-1 |
| Free-Text Wells | Boundary work captured, never validated away | MAK-HDC HA-6 |

### CC-1 (MUST)
**Statement:** Components are a single governed library with the identity sheet compiled in: every clinician surface composes from it; register lint, identity conformance, and accessibility are tested component properties; fork-by-copy is a conformance violation.
**Rationale trace:** MAK-PRB PC-1 sibling law; CV-1 enforcement locus *(new at this face)*.

### CC-2 (MUST)
**Statement:** All interruption classes render through one presentation system — Interruption Cards — visually ranked by class weight, individually dismissible where advisory, carrying their fabric-grounded trigger ("why am I seeing this") on the card, and drawing from the single attention budget (MAK-HDC HG-1/HG-4). Hard stops use a distinct reserved treatment (MAK-HDC HG-2) that nothing else may imitate.
**Rationale trace:** MAK-HDC HG-1/2/4 (realized); alert-fatigue evidence; one-economy law at the pixel.

### CC-3 (MUST)
**Statement:** The Graded Criterion Chip and Borderline Flag implement the left wing's rules verbatim: never color-only, never traffic-light, tabular-numeric alignment where digits appear, membership sketch with axis context on demand, borderline flag invites (one tap to the Deviation Sheet) and never gates (MAK-LWC FC-1/2/5 realized).
**Rationale trace:** MAK-LWC FC-1/2/5; MAK-HDC HA-2.

### CC-4 (MUST)
**Statement:** Free-Text Wells are standing on every capture and act surface: accepting annotation without validation gates, preserved verbatim, rendered downstream, counted in telemetry — and never shrunk, hidden, or removed to improve structured-completion metrics.
**Rationale trace:** MAK-HDC HA-6 (realized); MAK-RWC MA-3 Goodhart guard at the component.

### CC-5 (SHOULD)
**Statement:** The Stage-Trace Peek renders the five-stage verdict pipeline as a compact, consistent strip (completeness → thresholds → envelope → conflicts → verdict) with the deciding stage highlighted — the same rendering the auditor face uses, so the two faces share one trace literacy.
**Rationale trace:** MAK-CEC RG-1/2; MAK-ABC AL-2 twin; cross-face literacy economy.

## Part 5 — Interaction laws

### CI-1 (MUST)
**Statement:** The one-interaction law is measured and enforced: from any displayed recommendation — argument tree, one interaction (CS-3); from any element — deviation, gap, or fit-judgment sheet, one interaction (CS-4); from any claim — applicable rebuttals, one interaction (MAK-HDC HR-3). Interaction-count regressions are release blockers.
**Rationale trace:** MAK-HDC HR-3/HA-2..4 (realized as a measured law); CF-3 lineage.

### CI-2 (MUST)
**Statement:** In-consultation input is confined to the recorded acts: confirm, sign off, deviate, report gap, judge fit, navigate conflict — plus free-text annotation (CC-4). No screen reachable during an encounter demands structured data entry beyond these (MAK-HDC HW-1).
**Rationale trace:** MAK-HDC HW-1 (realized); Blake read-and-decide placement.

### CI-3 (MUST)
**Statement:** Keyboard-first parity holds: every act, drill-down, and navigation is operable keyboard-only with visible focus, and the act sheets' one-interaction law holds under keyboard operation — the consultation workflow never requires a pointer.
**Rationale trace:** clinical-workstation reality; WCAG operability; CS-4 grammar under both modalities *(new)*.

### CI-4 (MUST)
**Statement:** State is never silently lost or silently acted: drafts of act sheets survive interruption; navigation away from an uncommitted act warns once, plainly; and nothing commits on timeout, focus loss, or navigation — the no-action default holds everywhere (MAK-HDC HA-1's fail-closed at interaction grain).
**Rationale trace:** MAK-HDC HA-1; MAK-PRB PI-1 sibling law; interruption-saturated clinical reality.

### CI-5 (SHOULD)
**Statement:** Offline degradation is legible: the face renders which content is current versus cached (with age), which acts queue for sync, and never renders a stale envelope or rebuttal state without its age visible (MAK-HDC HW-5 realized at interaction grain).
**Rationale trace:** MAK-HDC HW-5; XC-3; stale-safety-signal hazard.

## Part 6 — Density, embedding & accessibility

### CA-1 (MUST)
**Statement:** Density is layered, not crowded: the surface layer carries the ninety-second read (CS-1) and the inseparables (CS-2); the first drill layer carries full arguments; deeper layers carry traces and mathematics — with layer discipline versioned in the design system, so new signals compete for placement through governed layout change, never accretion (MAK-HDC HW-3's budget at the visual layer).
**Rationale trace:** MAK-HDC HW-3 (realized); Bayor overload findings.

### CA-2 (MUST)
**Statement:** EHR embedding preserves the laws: in CDS Hooks card or SMART-app form, every card carries its argument link (one interaction to the Argument View), envelope badge, and identity-system styling — a card that renders a naked recommendation string is non-conformant regardless of host constraints; where a host cannot carry the laws, the integration is reduced to a link-out rather than a lawless summary.
**Rationale trace:** MAK-HDC Part 8 delivery vectors (ELSM-H01/H02); HR-1 one-surface law under embedding *(new — the embedding floor)*.

### CA-3 (MUST)
**Statement:** The accessibility floor holds (MAK-HDC HR-5, realized): WCAG 2.2 AA equivalent, never color-only for any signal identity, legible at the minimum supported display and 200% scaling, screen-reader complete including chip and badge semantics, and functional in the low-resource profile.
**Rationale trace:** MAK-HDC HR-5; MAK-LWC FC-5; MX-3.

### CA-4 (SHOULD)
**Statement:** My Attention gives the clinician their own lens: budget spend by class, active suppression rules affecting them, their prompt history — the same numbers the auditor's system lens sees, rendered personally (MAK-HDC HG-5 realized).
**Rationale trace:** MAK-HDC HG-5; observability symmetry; surveillance-anxiety mitigation.

### CA-5 (MUST)
**Statement:** The UI conformance suite gates releases: identity-system conformance and conflation kit (CV-1/5), one-interaction measurements (CI-1), one-surface negative tests (no side-channel widget — HDC HR-1), verdict-fidelity tests (held content unreachable, flagged content only via the Fit-Judgment Sheet), sign-off isolation tests (CS-5), interruption-budget enforcement (CC-2), keyboard parity (CI-3), and embedding-floor tests per delivery vector (CA-2). Results are conformity-file artifacts.
**Rationale trace:** MAK-HDC HE-4 (realized as the UI's suite); MAK-CEC RG-8 pattern.

## Part 7 — Traceability & conformance

### Realization map (complete against MAK-HDC)

| MAK-HDC requirement | Realized by |
|---|---|
| HW-1 (read-and-decide; confined input) | CI-2 |
| HW-2 (brief as fabric projection) | CS-1 |
| HW-3 (reading budget) | CS-1, CA-1 |
| HW-4 (handover narratives) | Argument View export affordance; generated-content marking (CV-4 vocabulary) |
| HW-5 (offline-first) | CI-5, CA-3 |
| HR-1 (one-surface law) | CC-1, CA-5 negative tests |
| HR-2 (five identities) | CV-1, CC-1 |
| HR-3 (argument + qualifier + envelope + rebuttals reachable) | CS-2/3, CV-3, CI-1 |
| HR-4 (verdict fidelity) | CS-3 stage trace; CA-5 tests |
| HR-5 (accessibility + lint) | CV-4, CA-3 |
| HR-6 (self-description panel) | screen set (Self-Description Panel) |
| HA-1 (fail-closed sign-off) | CS-5, CI-4 |
| HA-2 (deviation friction law) | CS-4, CC-3 |
| HA-3 (gap reporting) | CS-4 |
| HA-4 (fit-judgment flow) | CS-4 |
| HA-5 (conflict navigation) | CS-6 |
| HA-6 (boundary work legitimate) | CC-4 |
| HG-1 (one attention budget) | CC-2 |
| HG-2 (hard-stop class) | CC-2 reserved treatment |
| HG-3 (governed suppression) | My Attention surfaces rules; governance out of UI scope (MAK-ABC AG) |
| HG-4 (evidence-gated interruptions) | CC-2 trigger-on-card |
| HG-5 (clinician's own analytics) | CA-4 |
| HT-1..4 (team modes) | Conflict Bench multi-author states (CS-6); band views per CC-3 sketch rules; asynchronous modes inherit CI-4/5 |
| HE-1..4 (evaluation, telemetry, suite) | CV-5 kit; CA-5 realizes HE-4; HE-1..3 consume this UI's instrumentation |

### Findings → requirements

| Finding | Source | Requirements it drives |
|---|---|---|
| The consultation is minutes; the brief must read in seconds | Blake pattern via MAK-HDC HW | CS-1, CA-1 |
| Signal conflation is the face's silent failure mode | MAK-CEC OM-3; MAK-LWC FC-3 | CV-1/2/5, CC-1 |
| Reference-class visibility at the moment of decision | MAK-RWC MC-1; REG-FIND-004 | CV-3, CS-2 |
| Honest acts must be cheaper than avoidance | MAK-HDC HA family; Bayor rigidity | CS-4, CI-1 |
| Sign-off must feel like signing — deliberate, attributed, fail-closed | REG-KEEP-003 via MAK-HDC HA-1 | CS-5, CI-4 |
| Interruptions are one economy or they are noise | MAK-HDC HG-1; alert-fatigue evidence | CC-2 |
| Embedded delivery must not strip the laws | MAK-HDC Part 8 vectors | CA-2 |

### Sources

- Governing: MAK-HDC v1.0 (all HW/HR/HA/HG/HT/HE citations) · MAK-LWC v1.1 (FC components) · MAK-RWC v1.1 (MC components) · MAK-CEC v1.1 (signal registry, verdict stream) · MAK-ANT v1.0 (regulatory bindings).
- Delivery vectors verified in MAK-HDC Part 8: CDS Hooks + sandbox; SMART on FHIR client-js; OpenMRS ESM (host/design mine).
- Evidence base via the series: Blake briefs; Bayor overload/rigidity; Spitzer 2026 argument-shaped display; Kesselheim alert fatigue; WCAG 2.2.

*Document footer (source artifact):* The Labial Palps Corpus v1.0 · requirement IDs are stable; propose changes as argued deviations. Compiled as the interaction-level realization of MAK-HDC v1.0, 1 Sep 2026.

## Appendix A — ID census (additive)

Authoritative enumeration for validator checks. Count: **26**.

```json
{
  "doc_id": "MAK-LBP",
  "version": "1.0",
  "requirements": {
    "CV": ["CV-1","CV-2","CV-3","CV-4","CV-5"],
    "CS": ["CS-1","CS-2","CS-3","CS-4","CS-5","CS-6"],
    "CC": ["CC-1","CC-2","CC-3","CC-4","CC-5"],
    "CI": ["CI-1","CI-2","CI-3","CI-4","CI-5"],
    "CA": ["CA-1","CA-2","CA-3","CA-4","CA-5"]
  },
  "levels": {
    "MUST":   ["CV-1","CV-2","CV-3","CV-4","CS-1","CS-2","CS-3","CS-4","CS-5","CC-1","CC-2","CC-3","CC-4","CI-1","CI-2","CI-3","CI-4","CA-1","CA-2","CA-3","CA-5"],
    "SHOULD": ["CV-5","CS-6","CC-5","CI-5","CA-4"],
    "MAY":    []
  },
  "retired": []
}
```

Census arithmetic: 21 MUST + 5 SHOULD + 0 MAY = 26 (5+6+5+5+5 across the five families).

## Appendix B — Self-audit checks (additive)

1. **ID uniqueness** — no requirement ID appears in more than one requirement header.
2. **ID census parity** — headers matching `^### (CV|CS|CC|CI|CA)-\d+ \((MUST|SHOULD|MAY)\)$` exactly equal Appendix A's enumeration (26).
3. **Level parity** — header levels match Appendix A buckets.
4. **Trace presence** — every requirement block has a non-empty rationale trace.
5. **Normative leakage** — no capitalized MUST/SHOULD/MAY outside requirement blocks, quoted text, or this appendix.
6. **Realization completeness** — every MAK-HDC requirement appears in the Part 7 realization map (out-of-scope rows permitted and named).
7. **Cross-reference integrity** — every CV/CS/CC/CI/CA ID cited exists in the census; every host-document ID cited resolves in its host.
8. **Identity coverage** — all five signals of the registry have exactly one identity each in the identity-sheet requirements, and every component that renders a signal names its identity conformance.
9. **Table integrity** — consistent column counts per row.
10. **Stability** — IDs from previous versions present or explicitly retired; never reused.
