---
doc_id: MAK-PRB
title: "The Proboscis Corpus"
version: "1.0"
date: "2026-09-01"
series: "Mākoha research series — volume 14 · the Patient UI, implementing MAK-TXC"
status: normative-draft
normative_language: RFC-2119 (MUST / SHOULD / MAY)
req_prefixes: [PV, PS, PC, PI, PA]
req_count: 27
subordinate_to: "MAK-TXC v1.0 — this volume specifies interaction and presentation for the Patient Face; every TXC requirement governs; nothing here relaxes one"
implements:
  - "MAK-TXC v1.0 (The Thorax Corpus) — the Patient Face behaviour this UI realizes"
  - "MAK-LWC v1.1 patient components (word-chips, reliability dial, membership scale visual, plain codebook)"
  - "MAK-RWC v1.1 patient components (fit renderer, gap reporter, escape hatches)"
governed_by:
  - "REG-POSTURE v1.0 via MAK-ANT — TR-3's bright line is a UI law here (PS-4); ASSUME-REG-003 separability carried"
changelog:
  - "v1.0 (2026-09-01): initial release — 27 requirements across PV/PS/PC/PI/PA; screen and component inventories; UI conformance suite."
companions:
  - "MAK-TXC v1.0 (governing face corpus) · MAK-HDC v1.0 / MAK-LBP (the clinician-side siblings) · MAK-ANT v1.0 (regulatory sensing)"
artifact_url: "https://claude.ai/code/artifact/c627b26a-8211-48db-887d-5d55b9568884"
change_policy: "Requirement IDs are stable; retired IDs never reused. Propose changes as argued deviations."
---

<!-- LLM USAGE CONTRACT (additive; not part of the source document)
1. Requirement blocks (### PV-n / PS-n / PC-n / PI-n / PA-n) are NORMATIVE; all other
   prose is INFORMATIVE. Inventories are component/screen catalogues, normative only
   where a requirement cites them.
2. This volume IMPLEMENTS MAK-TXC: every screen and component realizes named TXC
   requirements, and a UI decision that would violate a TXC (or deeper host) MUST
   is invalid regardless of anything written here.
3. The bright line binds generation (PS-4): never design a patient-visible surface,
   preview, notification, or share card that can show diagnostic content before
   clinician sign-off.
4. The plain register's vocabulary law binds generation: no percentages,
   probabilities, μ values, scores, or blended-confidence displays anywhere in
   patient UI copy or components.
5. MUST violations in generated designs/code/documents require an explicit DEVIATION
   notice naming the ID.
6. Appendix A's ID census is authoritative for validator checks; Appendix B's
   self-audit checks gate any edit of this file.
END LLM USAGE CONTRACT -->

# The Proboscis Corpus

A translatable execution manual for the Patient UI of the triple-facing CDSS — the visual and verbal design language of the plain register, the screen set, the component library, the interaction laws, and the accessibility and localization floor — implementing the Thorax Corpus at the pixel and utterance level.

**Document metadata:** UI corpus · v1.0 · 1 Sep 2026 · fourteenth volume in the Mākoha research series · STATUS: normative draft · REQ IDS: PV · PS · PC · PI · PA (27) · SUBORDINATE TO: MAK-TXC v1.0 · IMPLEMENTS: the Patient Face.

## Contents

1. [Part 0 — How to use this document](#part-0--how-to-use-this-document)
2. [Part 1 — Why proboscis](#part-1--why-proboscis)
3. [Part 2 — The plain design language (PV)](#part-2--the-plain-design-language)
4. [Part 3 — The screen set (PS)](#part-3--the-screen-set)
5. [Part 4 — The component library (PC)](#part-4--the-component-library)
6. [Part 5 — Interaction laws (PI)](#part-5--interaction-laws)
7. [Part 6 — Accessibility & localization floor (PA)](#part-6--accessibility--localization-floor)
8. [Part 7 — Traceability & conformance](#part-7--traceability--conformance)
9. [Appendix A — ID census](#appendix-a--id-census-additive)
10. [Appendix B — Self-audit checks](#appendix-b--self-audit-checks-additive)

## Thesis

> The proboscis is how the butterfly actually drinks — a precision instrument for the one interface where nourishment crosses into the body. The Patient UI is that instrument: nearly everything the system knows arrives through these screens, in the words patients actually use, and nearly everything the system owes the patient — honesty about fit, sureness, and who decided what — is paid out through them. The Thorax Corpus says what the face does; this volume says how it feels in the hand: word-chips before keypads, pictures before numbers, one thumb before two, the escape hatch on every screen, the acknowledgment that a report went somewhere, and a bright line no notification ever crosses. The design language has one test: a tired person with a cheap phone, low literacy, and thirty seconds of patience can answer honestly, see their own data reflected, and never be lied to by simplification.

## Part 0 — How to use this document

This volume is the interaction-level companion to MAK-TXC: every requirement here realizes named TXC requirements (the Part 7 trace table is complete), and TXC governs on any apparent conflict. It is written to be handed to a design-and-build team: inventories name the screens and components; requirements state the laws they must obey; the conformance suite (PA-6, Part 7) makes the laws testable. Visual identity (brand, exact type, color values) is deliberately unfixed — the laws constrain structure, vocabulary, and behaviour, not taste.

- **Normative language.** MUST / SHOULD / MAY per RFC 2119.
- **Requirement IDs.** `PV-n` design language; `PS-n` screens; `PC-n` components; `PI-n` interaction laws; `PA-n` accessibility and localization.
- **Stack note.** UI technology is the Legs volume's concern; nothing here presumes a framework.

## Part 1 — Why proboscis

Three design facts govern everything below. First, **the patient UI is an instrument of capture before it is a display**: the Blake program moved history-taking home and proved (n=267, across ages and computer-literacy bands) that accessibility-first intake works — so intake ergonomics, not dashboard aesthetics, are the primary design surface. Second, **the plain register is a translation with rules, not a simplification**: TXC's rendering law (same argument, second register, envelope and deviation honesty intact) means every patient screen is a register projection with lint — the UI cannot invent softer content, only plainer words for the same content. Third, **the floor is the product**: the north star lives on cheap devices, low bandwidth, low literacy, and interrupted connectivity; a UI law that fails at the floor is not a law, it is a demo.

> The doctrine in one sentence: capture without coercion, reflect without diagnosing, translate without simplifying, and pass the tired-thumb test on every screen.

## Part 2 — The plain design language

### PV-1 (MUST)
**Statement:** The plain register's vocabulary is the ratified plain codebook, enforced by lint in the build: no percentages, probabilities, μ values, numeric scores, or blended-confidence displays anywhere in patient-visible copy, components, notifications, or share surfaces (MAK-TXC TR-2). Belief renders as honest plain hedging; gradedness renders as codebook words with the scale visual; fit renders as tested-on-people-like-you language.
**Rationale trace:** MAK-TXC TR-2 (realized); MAK-LWC FP-5; the lint as CI gate.

### PV-2 (MUST)
**Statement:** The two uncertainty voices are visually and verbally distinct system-wide: fit-uncertainty ("we're not sure this applies to you") and degree-uncertainty ("your answer is near a boundary") have separate phrasings, separate iconography, and never share a component (MAK-TXC TR-4).
**Rationale trace:** MAK-TXC TR-4 (realized); MS-9 routing at the pixel layer.

### PV-3 (MUST)
**Statement:** Content classes are visually typed: the patient's own data (immediate reflection) and clinician-released content (signed, attributed) have distinct, consistent visual treatments, with released content always carrying the releasing clinician's identity — so the bright line (PS-4) is legible, not just enforced.
**Rationale trace:** MAK-TXC TR-3; trust-through-attribution; *(new — the visual typing)*.

### PV-4 (MUST)
**Statement:** Every screen passes the tired-thumb test as a design gate: primary action reachable one-handed on the smallest supported device, one primary action per screen, comprehension at a ratified reading level for the deployment language, and a thirty-second happy path for the screen's core task, verified in PA-6's suite.
**Rationale trace:** Blake accessibility-first evidence; MAK-TXC TL-1; *(new — the gate formulation)*.

### PV-5 (SHOULD)
**Statement:** Words carry the interface and pictures carry the meaning: iconography supports but never replaces codebook words; illustrations of body sites, routines, and instructions are locality-reviewed in localization (PA-3); decorative imagery is absent from clinical surfaces.
**Rationale trace:** low-literacy comprehension evidence; localization realities; plain-register primacy.

## Part 3 — The screen set

The screen inventory (informative catalogue; the requirements below govern):

| Screen | Purpose | TXC anchor |
|---|---|---|
| Home / Today | Today's tasks (instruments due, diary entry), acknowledgment tray, nothing diagnostic | TW-1/4, TA-1 |
| Intake Instrument | One question per screen; word-chips + numeric + free text; escape hatch standing | TW-1/2, TA-3 |
| Diary / Self-monitoring | Capture + immediate membership-scale reflection; offline-first | TW-4 |
| My Results | Clinician-released content only; signed, attributed, plain-register argument | TR-1/3 |
| How sure / Does this fit me | The two uncertainty voices, per-item drill-down | TR-2/4 |
| My Data & Consent | Access ledger, consent toggles, calibration profile, exports, revocations | TC-1..3 |
| Values & Priorities | Elicitation, active mappings with plain meaning, contest/revoke | TA-2 |
| Report a Gap | "This doesn't describe me" flow with acknowledgment state | TA-1 |
| Settings & Accessibility | Language, text size, modality preferences (incl. IVR/SMS enrolment) | TL-1/2 |

### PS-1 (MUST)
**Statement:** Intake renders one question per screen with linguistic answers first-class: word-chips and hedged options at parity with numeric entry, "between X and Y" hesitant input supported, free text and "none of these" standing on every question, and the reliability dial offered (never demanded) beside every self-report (MAK-TXC TW-2/3).
**Rationale trace:** MAK-TXC TW-2/3 (realized); MAK-LWC FP-1/2 components.

### PS-2 (MUST)
**Statement:** The diary reflects immediately: on entry, the membership-scale visual (or plain trend card) renders offline, from the same artifacts the clinician sees; no diary reflection ever waits on connectivity or clinician action (MAK-TXC TW-4).
**Rationale trace:** MAK-TXC TW-4 (realized); Blake diary lesson.

### PS-3 (MUST)
**Statement:** My Results renders only clinician-released argument objects in the plain register — claim, plain reasons, how sure, does-this-fit-you, what you can choose, who signed — with any deviation stated plainly ("your doctor departed from the usual guideline because…") and drill-down to the fuller plain argument (MAK-TXC TR-1).
**Rationale trace:** MAK-TXC TR-1 (realized); register fidelity at screen grain.

### PS-4 (MUST)
**Statement:** The bright line is structural in the UI: no surface reachable by the patient — screen, preview, notification, widget, share card, email digest, IVR prompt — can render diagnostic or recommendation content that lacks sign-off; pre-release content has no patient-facing route, and notification payloads carry task prompts, never clinical content (MAK-TXC TR-3, TE-4).
**Rationale trace:** MAK-TXC TR-3 (realized structurally); notification-leak risk *(new — payload law)*.

### PS-5 (MUST)
**Statement:** My Data & Consent gives working controls, not documents: the access ledger renders who saw what and when in plain language; consent toggles enforce on the data plane; the calibration profile shows its plain meaning with one-action revocation; secondary-use consent is a separate, unbundled flow (MAK-TXC TC-1/2, TC-4).
**Rationale trace:** MAK-TXC TC-1/2/4 (realized); Stranieri custody doctrine.

### PS-6 (SHOULD)
**Statement:** The Gap Report flow completes in three steps or fewer from any renderable element (select what didn't fit → say more if you wish → done), and the acknowledgment tray on Home shows each report's state (received / being reviewed / outcome) until dismissed by the patient (MAK-TXC TA-1).
**Rationale trace:** MAK-TXC TA-1 (realized); acknowledgment loop as trust mechanism.

## Part 4 — The component library

The component inventory (informative catalogue; requirements govern):

| Component | Function | Source spec |
|---|---|---|
| Word-Chip Set | Codebook terms + hedges as tappable answers; "between" gesture for hesitant input | MAK-LWC FP-1 |
| Reliability Dial | One-tap "sure / fairly sure / guessing"; unstated by default | MAK-LWC FP-2 |
| Membership Scale Visual | "Where today sits" on the term's curve, plain-labelled | MAK-LWC FP-4 |
| Plain Trend Card | Ratified trend words over a series, picture attached | MAK-LWC component set |
| Fit Badge | Tested-on-people-like-you status, plain-language drill-down | MAK-RWC MP-1 |
| Gap Button | "This doesn't describe me," present on instruments and results | MAK-RWC MP-2 |
| Escape Hatch | Free text / "none of these" / skip-with-reason, standing | MAK-RWC MP-5 |
| Acknowledgment Tray | Gap-report and dispute states until patient-dismissed | MAK-TXC TA-1 |
| Consent Toggle | Granular, enforcing, plain-labelled, revocable | MAK-TXC TC-1 |
| Signed-Release Header | Releasing clinician identity + date on all released content | MAK-TXC TR-1/3 |

### PC-1 (MUST)
**Statement:** Components are a single governed library: every patient surface composes from the library, components carry their register lint and accessibility conformance as tested properties, and no screen ships a bespoke variant of a library component (fork-by-copy is a conformance violation).
**Rationale trace:** register-fidelity economics; PA-6 testability; drift prevention *(new)*.

### PC-2 (MUST)
**Statement:** The Word-Chip Set renders codebook terms and ratified hedges only, in the deployment language's ratified pack; chips never display terms outside the pack, and an answer outside the vocabulary routes to the escape hatch, preserved verbatim (MAK-TXC TW-2, TA-3).
**Rationale trace:** MAK-TXC TW-2/TA-3; MAK-LWC FS-5 vocabulary discipline at the component.

### PC-3 (MUST)
**Statement:** The Membership Scale Visual and Plain Trend Card are the only patient-facing renderings of gradedness: plain-labelled, never numeric-scored, axis context on demand, identical artifacts to the clinician's register-styled view (MAK-TXC TW-4; MAK-LWC FC-5 accessibility rules inherited).
**Rationale trace:** MAK-TXC TW-4; MAK-LWC FP-4/FC-5; single-render-source discipline.

### PC-4 (MUST)
**Statement:** The Gap Button and Escape Hatch are standing components: present on every instrument item and every rendered argument (gap), and every structured input (escape hatch); neither is ever hidden behind menus, disabled by configuration, or removed to improve completion metrics.
**Rationale trace:** MAK-TXC TA-1/TA-3 (realized); MAK-RWC MA-3 Goodhart guard at the component layer.

### PC-5 (SHOULD)
**Statement:** The Reliability Dial defaults to unstated and renders as an invitation, not a gate: answering never requires it, its copy names its purpose ("helps your care team read this"), and its value renders back to the patient wherever the answer renders.
**Rationale trace:** MAK-TXC TW-3 (realized); honesty-without-punishment doctrine.

## Part 5 — Interaction laws

### PI-1 (MUST)
**Statement:** Capture is resumable and lossless: every instrument and diary flow saves per-answer, survives interruption, app death, and offline periods without data loss, and resumes at the point of departure; partial completions are visible on Home, never silently discarded, and never nag more than the attention budget allows.
**Rationale trace:** MAK-TXC TL-1 offline discipline; interruption reality of the deployment contexts *(new — the resumability law)*.

### PI-2 (MUST)
**Statement:** Offline is a first-class state, not an error: every screen renders its offline behaviour (what works now, what syncs later) in plain language; queued items show sync state; nothing patient-entered is lost to connectivity, and sync conflicts resolve additively (both records kept, flagged for review) rather than by overwrite.
**Rationale trace:** MAK-TXC TL-1; XC-3; deferred-sync integrity *(new — additive conflict law)*.

### PI-3 (MUST)
**Statement:** Notifications follow the payload law and a patient-set budget: task prompts and acknowledgment updates only (PS-4), frequency and channels patient-controlled, quiet by default, and never engagement-motivated ("streaks," shaming, re-engagement hooks are prohibited patterns).
**Rationale trace:** PS-4; MAK-HDC HG-4's evidence-gating sibling; dark-pattern prohibition *(new)*.

### PI-4 (MUST)
**Statement:** Every consequential act confirms in plain language what will happen and shows what happened: consent changes state their effect before commit; revocations state what stops; gap reports confirm receipt; values changes show the active mapping's plain meaning — and each renders its fabric-recorded state afterward.
**Rationale trace:** MAK-TXC TC-1/2, TA-1/2 (realized); informed-act discipline.

### PI-5 (SHOULD)
**Statement:** Error and empty states teach instead of blame: validation failures name what is needed without discarding what was given; empty states explain what will appear and why; no patient-facing error exposes internal identifiers, stack language, or blame framing.
**Rationale trace:** low-literacy comprehension; MC-3/MP-5 boundary-work dignity, at copy level.

## Part 6 — Accessibility & localization floor

### PA-1 (MUST)
**Statement:** The floor is the release gate (MAK-TXC TL-1, realized): WCAG 2.2 AA equivalent on every screen; never color-only encodings; full function at the smallest supported device and at 200% text scaling; screen-reader complete; and the whole face functional offline-first at the stated bandwidth and device floors, tested per release.
**Rationale trace:** MAK-TXC TL-1; MAK-LWC FC-5 inheritance; floor-as-gate doctrine.

### PA-2 (MUST)
**Statement:** Modality parity holds at the floor: the IVR/SMS tier covers intake, reminders, escalation, and gap reporting with the same codebook vocabulary and the same bright line (no diagnostic content pre-release in any channel); IVR menus speak ratified terms (MAK-TXC TL-2).
**Rationale trace:** MAK-TXC TL-2 (realized); channel-parity of the laws.

### PA-3 (MUST)
**Statement:** Localization is a knowledge-plane act: language packs (codebooks, instrument text, illustration reviews) install per jurisdiction under lineage rules with locality review recorded; the UI never machine-translates ratified vocabulary at runtime.
**Rationale trace:** MAK-TXC TL-4; MAK-LWC FS-5/FP-6; WHO SMART localization pattern.

### PA-4 (MUST)
**Statement:** Meta-rational functions hold at the floor (MAK-TXC TL-3, realized in UI): the gap button, fit badge, escape hatches, and acknowledgment tray function offline, at the device floor, and in the IVR/SMS tier's equivalents.
**Rationale trace:** MAK-TXC TL-3; misfit concentrates at the periphery.

### PA-5 (SHOULD)
**Statement:** Assisted use is designed, not accidental: a helper mode supports a family member or community health worker assisting entry — assistance is recorded in capture context, the patient's own voice (reliability, escape hatches) remains distinct, and nothing in helper mode widens data access beyond the session.
**Rationale trace:** MAK-TXC TW-1 capture context; CHW deployment reality (fhircore pattern); custody integrity.

### PA-6 (MUST)
**Statement:** The UI conformance suite gates releases: register lint (PV-1), two-voices separation (PV-2), bright-line structural tests including notification payloads (PS-4), tired-thumb gates (PV-4), component-library integrity (PC-1), resumability and offline-loss tests (PI-1/2), floor tests (PA-1/2), and localization-pack integrity (PA-3). Results are conformity-file artifacts.
**Rationale trace:** MAK-TXC TE-4 (realized as the UI's suite); MAK-CEC RG-8 pattern.

## Part 7 — Traceability & conformance

### Realization map (complete against MAK-TXC)

| MAK-TXC requirement | Realized by |
|---|---|
| TW-1 (capture before encounter, versioned instruments) | PS-1, PA-5 (capture context) |
| TW-2 (speech as data, no coercion) | PS-1, PC-2, PC-4 |
| TW-3 (reliability dial) | PS-1, PC-5 |
| TW-4 (immediate feedback) | PS-2, PC-3 |
| TW-5 (PIS calibration) | PS-5 (profile view) |
| TR-1 (same argument, plain register) | PS-3, PC (Signed-Release Header, Fit Badge) |
| TR-2 (words and pictures, never scores) | PV-1, PC-3 |
| TR-3 (bright line) | PS-4, PV-3, PI-3, PA-2 |
| TR-4 (fit vs degree voices) | PV-2 |
| TR-5 (self-description) | PS-3 drill-down surface |
| TA-1 (gap reports with acknowledgment) | PS-6, PC-4, PI-4 |
| TA-2 (values as remodeling, patient as party) | PS (Values screen), PI-4 |
| TA-3 (escape hatches preserved) | PC-2/4 |
| TA-4 (patient council) | out of UI scope — governance stage (MAK-ABC AG-4) |
| TA-5 (dispute entry) | Acknowledgment Tray states; dispute flow reachable from My Results |
| TC-1 (access ledger + enforcing consent) | PS-5, PC (Consent Toggle), PI-4 |
| TC-2 (meta-data custody) | PS-5 |
| TC-3 (explainable routing) | PS-5 (My Data plain-language view) |
| TC-4 (unbundled secondary-use consent) | PS-5 |
| TL-1 (floor as gate) | PA-1, PV-4, PI-1/2 |
| TL-2 (linguistic primary at floor; IVR/SMS) | PA-2 |
| TL-3 (meta-rational at floor) | PA-4 |
| TL-4 (WHO SMART localization) | PA-3 |
| TL-5 (separability pending ASSUME-REG-003) | PS-4 structural bright line; PV-3 typing (the UI keeps the classes separable) |
| TE-1..4 (evaluation, telemetry, audits, suite) | PA-6 realizes TE-4; TE-1..3 consume this UI's instrumentation |

### Findings → requirements

| Finding | Source | Requirements it drives |
|---|---|---|
| Accessibility-first intake works across literacy and age bands (n=267) | Blake 2014 | PV-4, PS-1, PA-1 |
| Patients speak in hedges and ranges; coercion loses the data | CWW/HFLTS literature via MAK-LWC | PS-1, PC-2 |
| Immediate reflection drives engagement | Blake diary lesson | PS-2 |
| The plain register is a rules-bearing translation, not a simplification | MAK-TXC TR family | PV-1/2/3, PS-3 |
| Diagnostic content requires sign-off in every channel | MAK-TXC TR-3; REG-KEEP-003 | PS-4, PI-3, PA-2 |
| Custody is a face function | Stranieri PCA lineage via MAK-TXC TC | PS-5, PI-4 |
| Misfit concentrates at the deployment periphery | MAK-RWC MA-2; Cockburn 2024 | PA-4 |
| Completion metrics corrupt capture honesty | MAK-RWC MA-3 via MAK-TXC TA-3 | PC-4, PI-3 |

### Sources

- Governing: MAK-TXC v1.0 (all TW/TR/TA/TC/TL/TE citations) · MAK-LWC v1.1 (FP components, FS-5, FC-5) · MAK-RWC v1.1 (MP components) · MAK-ANT v1.0 (regulatory bindings).
- Evidence base via the series: Blake 2014/2016 (intake, diary, 267-user study); Bayor 2025; Cockburn 2024; Stranieri custody lineage; WHO SMART localization; WCAG 2.2.

*Document footer (source artifact):* The Proboscis Corpus v1.0 · requirement IDs are stable; propose changes as argued deviations. Compiled as the interaction-level realization of MAK-TXC v1.0, 1 Sep 2026.

## Appendix A — ID census (additive)

Authoritative enumeration for validator checks. Count: **27**.

```json
{
  "doc_id": "MAK-PRB",
  "version": "1.0",
  "requirements": {
    "PV": ["PV-1","PV-2","PV-3","PV-4","PV-5"],
    "PS": ["PS-1","PS-2","PS-3","PS-4","PS-5","PS-6"],
    "PC": ["PC-1","PC-2","PC-3","PC-4","PC-5"],
    "PI": ["PI-1","PI-2","PI-3","PI-4","PI-5"],
    "PA": ["PA-1","PA-2","PA-3","PA-4","PA-5","PA-6"]
  },
  "levels": {
    "MUST":   ["PV-1","PV-2","PV-3","PV-4","PS-1","PS-2","PS-3","PS-4","PS-5","PC-1","PC-2","PC-3","PC-4","PI-1","PI-2","PI-3","PI-4","PA-1","PA-2","PA-3","PA-4","PA-6"],
    "SHOULD": ["PV-5","PS-6","PC-5","PI-5","PA-5"],
    "MAY":    []
  },
  "retired": []
}
```

Census arithmetic: 22 MUST + 5 SHOULD + 0 MAY = 27 across five families (5+6+5+5+6).

## Appendix B — Self-audit checks (additive)

1. **ID uniqueness** — no requirement ID appears in more than one requirement header.
2. **ID census parity** — headers matching `^### (PV|PS|PC|PI|PA)-\d+ \((MUST|SHOULD|MAY)\)$` exactly equal Appendix A's enumeration.
3. **Level parity** — header levels match Appendix A buckets.
4. **Trace presence** — every requirement block has a non-empty rationale trace.
5. **Normative leakage** — no capitalized MUST/SHOULD/MAY outside requirement blocks, quoted text, or this appendix.
6. **Realization completeness** — every MAK-TXC requirement appears in the Part 7 realization map (out-of-scope rows permitted and named).
7. **Cross-reference integrity** — every PV/PS/PC/PI/PA ID cited exists in the census; every host-document ID cited resolves in its host.
8. **Bright-line coverage** — every patient-reachable surface class named in this document (screens, previews, notifications, widgets, share cards, IVR/SMS) is covered by a PS-4/PA-2 test in PA-6.
9. **Table integrity** — consistent column counts per row.
10. **Stability** — IDs from previous versions present or explicitly retired; never reused.
