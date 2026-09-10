---
doc_id: INTENDED-PURPOSE
title: "Mākoha — Intended Purpose Statement v0.1"
version: "0.1-draft"
date: "2026-09-09"
status: "DRAFT — not attested; GATE-000 unpassed; human review required before any regulatory reliance"
authority: "ADVISORY_ONLY — requires Ken Lee review and edit in Confluence; task closes only when Ken marks TASK-REG-001 DONE-WITH-EVIDENCE"
produced_by: "Drafted by Claude (Fable 5.1) in session e789cd7e on 3 Sep 2026 per MAK-1 (TASK-REG-001); human owner Ken Lee"
supersedes: "nothing"
sources:
  - "MET-1 §2 (North Star, WHAT/WHERE/WHO/WHY/DONE) — github.com/Arepo-Medtech/CDSS-makoha-imago @ 73460b3"
  - "Arch §13.1 SPINE-NS-1 — github.com/Arepo-Medtech/CDSS-makoha-imago @ 73460b3"
  - "REG-POSTURE v1.2 §1, §3, §4.1, §8, TASK-REG-001 — github.com/Arepo-Medtech/CDSS-makoha-imago @ 73460b3"
  - "MAK-FFC v1.1 SPINE-3, CF-1, PF-1, AF-1, XC-1 — github.com/Arepo-Medtech/CDSS-makoha-imago @ 73460b3"
  - "MAK-HDC v1.0, MAK-TXC v1.0, MAK-ABC v1.0 — github.com/Arepo-Medtech/CDSS-makoha-imago @ 73460b3"
open_items:
  - "ASSUME-REG-001 — device classification: OPEN"
  - "ASSUME-REG-002 — CDSS exemption unavailability: OPEN"
  - "ASSUME-REG-003 — patient surface scope: OPEN"
  - "Q-REG-008 — jurisdiction sequence: OPEN"
  - "DEC-07 — patient surface scope decision: OPEN"
not_in_scope:
  - "TASK-REG-002 — counsel attestation"
  - "TASK-REG-003 — claims inventory"
  - "TASK-REG-004 — patient-surface decision"
closes: "TASK-REG-001 (pending Ken Lee review and DONE-WITH-EVIDENCE marking)"
---

> **⚠ DRAFT — review required before any regulatory reliance.**
>
> This page is an agent-drafted working document. It does not constitute regulatory advice.
> It has not been attested by counsel; `ASSUME-REG-001`, `ASSUME-REG-002`, and `ASSUME-REG-003`
> remain **OPEN** (see §7). `GATE-000` is not passed. Ken Lee must review, edit in place,
> and mark `TASK-REG-001` DONE-WITH-EVIDENCE before this statement may be cited downstream.

---

# Mākoha — Intended Purpose Statement

**Product:** Mākoha  
**Entity:** Arepo Medtech Pty Ltd  
**Version:** 0.1-draft  
**Date:** 9 September 2026  
**Imago repo:** github.com/Arepo-Medtech/CDSS-makoha-imago @ 73460b3  
**Task:** TASK-REG-001 (REG-POSTURE v1.2 §7 Phase 0)

---

## §1 What Mākoha is

Mākoha is a clinical decision support system for registered health professionals.
Its purpose is to assist AHPRA-registered general practitioners during live consultations
by surfacing ranked differential-diagnosis information, evidence-grounded recommendations,
and uncertainty quantification — rendered as structured, argued, reviewable justifications
rather than bare outputs.

The system assembles a justification fabric: every recommendation is an *actual argument*
carrying claim, grounds, warrant, backing, qualifier, and rebuttal — all traceable to
pinned evidence-library entries and rendered in a register appropriate to each surface
(MET-1 §2; MAK-FFC SPINE-3).

The organizing doctrine is stated in Arch §13.1 SPINE-NS-1 and MET-1 §2:
**ML proposes and tests; only arithmetic releases.** Every probabilistic component
(Bayesian differential engine, conformal wrapper, Graph RAG, concept coder) sits on
the proposes-and-tests side of a deterministic gate chain. Nothing probabilistic stands
between authoritative content and any face (MAK-FFC SPINE-7).

---

## §2 Who uses Mākoha and in what setting

**Primary users:** AHPRA-registered general practitioners during live clinical consultations,
from the L3 pilot onward (MET-1 §2 / Arch §13.1 SPINE-NS-1 WHO/WHEN element).

**Setting:** Live GP consultations in general practice. Routine data capture (history,
condition-specific instruments) occurs before the encounter on the patient face;
synthesis occurs before the encounter in the Consult-Prep Composer; in-consultation
interaction is read-and-decide (MAK-FFC CF-1; MAK-HDC).

**Pilot practices:** Not yet named — ASSUME-SPINE-001 is open; pilot MoUs are required
before the L4 exit.

**Deployment infrastructure:** AWS ap-southeast-2; per-environment accounts under
AWS Organizations; corpus in its own account (MET-1 §2 / Arch §13.1 SPINE-NS-1
WHERE element).

**Patient surface scope:** Under active decision — see §7, ASSUME-REG-003 / DEC-07.
Patient-face work beyond the J-3-safe intake, consent, and logistics subset is **Blocked**
pending DEC-07 (REG-POSTURE v1.2 §8).

---

## §3 Regulatory posture

The working posture is stated in REG-POSTURE v1.2 §3:

> **Build to SaMD standard. Test exemption honestly at a named gate. Assume inclusion.**

REG-FIND-001 assesses Mākoha as **not eligible** for the CDSS exemption. The
disqualifier is the diagnostic function, not the use of AI: a ranked differential
with posteriors constitutes contribution to diagnosis under the current TGA guidance
(REG-POSTURE v1.2 §1). This finding remains open pending ASSUME-REG-002 (written
counsel opinion).

Classification is expected at Class IIa minimum; Class IIb is plausible (REG-POSTURE v1.2 §4.1).
Neither class is confirmed — ASSUME-REG-001 is open and blocks GATE-000.

A separate exempt-tier reserve artifact (Addendum J-3, Guideline-Prompt Profile) is
proposed beside the classified track (MAK-FFC XC-1/XC-2; REG-POSTURE v1.2 §3.1
FORK-REG-001). J-3 is v0.9-proposed; DEC-06 is open. J-3 is never marketed,
configured, or extended to do classified work under an exempt label (MAK-FFC XC-1).

---

## §4 What Mākoha claims

Mākoha provides, for AHPRA-registered GPs during live consultations:

1. **A ranked differential diagnosis** — posterior probabilities produced by a Bayesian
   engine over a tiered evidence library, with conformal coverage guarantees
   (MET-1 §2 WHY element; Arch §13.1 SPINE-NS-1).

2. **Evidence-grounded recommendations** — verbatim content from a signed content
   registry, passed through a five-gate deterministic chain (hash, tier, currency,
   dose-range, context), rendered as actual arguments carrying all six Toulmin elements
   (MAK-FFC SPINE-1/SPINE-7).

3. **Qualified uncertainty** — every claim carries a qualifier (posterior plus conformal
   set at a stated coverage level); no claim releases without its qualifier
   (MAK-FFC SPINE-2).

4. **Rebuttal disclosure** — known corruptions, contraindications, and unresolved
   guideline conflicts are surfaced as first-class argument content, not suppressed
   (MAK-FFC SPINE-6/SPINE-8; MAK-FFC AF-1).

5. **A reviewable, replayable decision basis** — every released argument pins the
   versions of the guideline, terminology, evidence library, engine model, and
   configuration that produced it; any historical decision is replayable bit-for-bit
   (MAK-FFC SPINE-5; MAK-ABC AF-7; REG-KEEP-002).

---

## §5 What Mākoha does not claim

The following are explicit non-claims, grounded in the sources cited:

- **Does not replace clinical judgment.** Deviation is always available; the system
  computerizes criteria, never discretion (MAK-FFC SPINE-7/SPINE-8; MAK-HDC; CF-3/CF-4).
- **Does not diagnose.** The patient face presents recommendations and choices; diagnostic
  claims render to patients only after clinician release (MAK-FFC PF-8; MAK-TXC).
- **Does not release probabilistic output directly.** The five-gate deterministic chain
  stands between every probabilistic component and every face; shadow candidates are never
  rendered (Arch §3 runtime path; MAK-FFC SPINE-7).
- **Does not claim exemption.** REG-FIND-001 assesses the CDSS exemption as unavailable
  to the classified track (REG-POSTURE v1.2 §1). ASSUME-REG-002 is open.
- **Does not validate on synthetic data alone.** Synthetic-only development is a control
  posture, not validation evidence (REG-FIND-010; REG-KEEP-004 reading note in
  REG-POSTURE v1.2 §3.2).
- **Does not handle identifiable clinical data before GATE-002.** No identifiable clinical
  data touches any environment before the Phase 2 controls gate (REG-KEEP-004;
  REG-POSTURE v1.2 §7 GATE-002).

---

## §6 The three surfaces

Per MET-1 §2 and MAK-FFC SPINE-3, one argument object renders in three registers.
Renderers may compress or re-order; they must not add, remove, or reweight argument
content per audience.

### 6.1 Clinician Face (MAK-HDC; MAK-FFC CF-1)

**Who:** AHPRA-registered GPs.

**What it does:**
- Delivers a pre-consultation brief (Consult-Prep Composer) from evaluator-released
  argument objects; in-consultation interaction is read-and-decide only (MAK-FFC CF-1;
  MAK-HDC).
- Renders every recommendation with its full argument tree within one interaction,
  at per-criterion granularity, with qualifier adjacent to every claim (MAK-FFC CF-2).
- Provides a Deviation Composer: at most one interaction to open, structured reason plus
  optional free text, explicit preview of auditor-face appearance (MAK-FFC CF-3; MAK-HDC).
- Hard stops are reserved for the deterministic safety class only; everything else is
  advisory (MAK-FFC CF-4).
- Sign-off is fail-closed: no recommendation becomes an order, prescription, referral,
  or patient-visible diagnostic statement without attributed clinician sign-off recorded
  in the fabric (MAK-HDC HA-1; REG-KEEP-003).
- Renders only projections of evaluator-released argument objects; no widget consumes
  engine output or side channels (MAK-HDC HR-1).

**What it does not do:**
- Does not demand in-consultation data entry beyond confirmation and deviation (MAK-FFC CF-1).
- Does not surface auditor-face analytics, league tables, or peer comparisons (MAK-FFC CF-7 anti-requirement).
- Does not perform inference of its own (MAK-HDC).

### 6.2 Patient Face (MAK-TXC; MAK-FFC PF-1)

**Who:** Patients of the GP practice. Scope under active decision (ASSUME-REG-003 / DEC-07 — see §7).

**What it does:**
- Captures routine history and condition-specific data before the encounter, with
  point-of-entry validation; instruments are versioned artifacts in the knowledge plane
  (MAK-FFC PF-1; MAK-TXC).
- Renders patient-visible recommendations in the plain register from the same argument
  object the clinician saw — including qualifiers and the existence of any deviation
  (MAK-FFC PF-2; MAK-FFC SPINE-3).
- Provides the Personal Data Agent: complete access ledger (every read of the patient's
  record) and consent controls that the data plane enforces (MAK-FFC PF-4; MAK-TXC).
- Accessibility floor is non-negotiable: WCAG-conformant, functional offline with
  deferred sync, low-literacy and low-resource profile as a release gate (MAK-FFC PF-6;
  MAK-FFC XC-3; MAK-TXC).

**What it does not do:**
- Does not diagnose patients; diagnostic claims render to patients only after clinician
  release (MAK-FFC PF-8).
- Does not present a sanitized or divergent version of the argument (MAK-FFC PF-2;
  MAK-FFC SPINE-3).
- Patient-face work beyond intake, consent, and logistics is **Blocked** until
  DEC-07 resolves ASSUME-REG-003 (REG-POSTURE v1.2 §8; REG-POSTURE v1.2 §7 interim rule).

### 6.3 Auditor Face (MAK-ABC; MAK-FFC AF-1)

**Who:** Internal quality, compliance, and regulatory reviewers; external conformity
assessment bodies and, via regulator export, the TGA.

**What it does:**
- Is a read model only: no write path into clinical data, arguments, or deviations;
  its only writes are review states, dispute records, and guideline-change proposals,
  each a fabric-ledgered entry (MAK-FFC AF-1; MAK-ABC).
- Presents every reviewable item as an argument pair — the GenericArgument (what the
  ratified guideline licensed) and the ActualArgument (what happened) — with departures
  localized to specific warrant nodes (MAK-FFC AF-2).
- Distinguishes, as first-class states: guideline-concordant; documented justified
  deviation; documented deviation under review; undocumented deviation (MAK-FFC AF-3).
- Produces regulator export: self-contained conformity bundles with decision set, pinned
  versions, replay attestation, argument transparency, deviation states, and adverse-event
  linkage (MAK-FFC AF-7; REG-KEEP-002; XC-1).
- Runs theater-detection continuously (boilerplate similarity, duplication clusters,
  temporal anomalies) producing flags for human review — flags do not auto-sanction
  (MAK-FFC AF-4).

**What it does not do:**
- Does not hold a write path into clinical content (MAK-FFC AF-1; MAK-ABC).
- Does not auto-sanction, auto-downgrade compliance states, or feed individual
  performance management without a governed human process (MAK-FFC AF-4).
- Does not surface clinician-level lenses without a governed access grant logged to
  the fabric (MAK-FFC AF-8).

---

## §7 Open items — not resolved by this page

The following items are explicitly **OPEN**. They are recorded here so downstream
requirements, the risk file, and the claims inventory can cite them. None may be
closed by internal reasoning; each requires the named external attestation.

| ID | Item | Attesting party | Blocking |
|---|---|---|---|
| `ASSUME-REG-001` | Mākoha's device classification and applicable classification rule | AU regulatory counsel | `GATE-000` |
| `ASSUME-REG-002` | CDSS exemption is unavailable to Mākoha (`REG-FIND-001` confirmed) | AU regulatory counsel | `GATE-000` |
| `ASSUME-REG-003` | Patient surface treatment — separate product, non-decision-support, or in-scope. Patient-face work beyond the J-3-safe subset is Blocked (DEC-07). | Counsel + product | `GATE-000` |
| `Q-REG-008` | Jurisdiction sequence: Australia-first is assumed but not decided. What is the intended order across TGA, FDA, and the low-resource settings the north star names? | Counsel + product + programme | Phase 0 |
| `DEC-07` | Patient surface scope (conflict C-06 / ASSUME-REG-003): separate product, non-decision-support, or in-scope for the same submission | Counsel + product | `GATE-000` |

This page also records, but does not resolve:

- **TASK-REG-002** — counsel classification opinion: not in scope for this page
- **TASK-REG-003** — claims inventory: not in scope for this page
- **TASK-REG-004** — patient-surface decision: not in scope for this page

---

## §8 What this page is and is not

**This page is:**
- The Phase 0 narrative that `TASK-REG-001` calls for (REG-POSTURE v1.2 §7)
- The source the first Requirement of type "Intended use" in MAK will cite
- The narrative against which `WATCH-REG-002` (TGA AI-enabled device guidance) is read
  (REG-POSTURE v1.2 §10)
- The reference point for reconciling public positioning under `TASK-REG-003`

**This page is not:**
- Regulatory advice
- An attested classification opinion
- A completed claims inventory
- Evidence that `GATE-000` has passed

**Downstream dependencies:** Requirements (TASK-REG-008), the ISO 14971 risk file
(TASK-REG-007), and the claims inventory (TASK-REG-003) all await this page.
`GATE-000` awaits `ASSUME-REG-001`, `ASSUME-REG-002`, and `ASSUME-REG-003` being
ATTESTED or REFUTED.

---

## §9 Provenance and authorship

- **Drafted by:** Claude (Fable 5.1) in session e789cd7e, 3 Sep 2026
- **Human owner:** Ken Lee
- **Sources cited:** by ID and link only; no controlled wording invented or restated
  (see frontmatter `sources` field and per-section citations)
- **Repo commit:** github.com/Arepo-Medtech/CDSS-makoha-imago @ 73460b3
- **Closes (pending human review):** TASK-REG-001 — to be marked DONE-WITH-EVIDENCE
  by Ken Lee after Confluence review and edit

---

*This document is part of the Mākoha regulatory programme. It contains no case content,
no evidence-library values, no clinical numbers, sensitivities, specificities, or
likelihood ratios. It is safe to load alongside scoring-store material and must not be
used as a source for clinical content under any circumstance (REG-POSTURE v1.2 §0.6).*
