---
doc_id: REG-POSTURE
title: "Mākoha — Regulatory Posture: AUSTRALIA (TGA) and Ketryx Implementation Plan"
jurisdiction: AUSTRALIA
regulator: Therapeutic Goods Administration (TGA)
version: 1.2
status: DRAFT
authority: ADVISORY_ONLY
entity: Arepo Medtech Pty Ltd
product: Mākoha
date_issued: 2026-09-02
guidance_currency_date: 2026-09-02
supersedes: REG-POSTURE v1.1 (2026-09-01); REG-POSTURE v1.0 (2026-08-31)
review_basis: "Makoha Imago v1.2 repository (MANIFEST-IMAGO A-002, 2026-09-01; 179 files) + Ketryx pre-demo correspondence (2026-09-01) + survey-2 run BSQ-0001 (2026-09-02)"
standalone_rule: "REPLETE-STANDALONE. This document carries the complete standards stack and every Australian obligation itself. It never says 'see elsewhere' for anything a reader needs in order to act in Australia. Companion jurisdiction documents follow the same rule and repeat the stack by design."
companions:
  - "REG-NZ v1.1 — NEW ZEALAND (Medsafe)"
  - "REG-US v1.0 — UNITED STATES (FDA)"
  - "REG-EU v1.0 — EUROPEAN UNION (MDR 2017/745)"
depends_on:
  - Addendum J-1 (deterministic runtime posture)
  - Addendum J-2 (ML runtime, SaMD classification posture)
  - Addendum J-3 / MAK-J3 v0.9-proposed (Guideline-Prompt Profile, exempt-tier reserve — retirement pending DEC-06)
  - MAK-GOV v0.9-proposed (Addendum G, Governance Layer non-device line)
  - Build Ecosystem v2.0 (Implementer Contract, Observer adjudication)
  - MAK-FFC v1.1 (XC-1 classification honesty; XC-2 profile boundary; XC-3 low-resource)
  - EXEC-1 v1.0 (precedence EX-1..10; run map RUN-0..4)
wrapped_by: "MAK-ANT (Antennae Corpus) — folds this document verbatim as Annex 1 at the next FOLD (FOLD-1 W1 now targets v1.2)"
runtime_register: "R30 — Regulatory Posture Register (Proposed, DEC-02; owner cdss-governance); seed deltas R30.1, R30.2"
blocks:
  - GATE-000
id_prefixes: [REG-FIND, REG-KEEP, ASSUME-REG, OBL, STD, FORK-REG, GATE, TASK-REG, KTX, WATCH-REG, Q-REG, SRC-REG]
attestation_required: true
attestation_by: Australian regulatory counsel
---

# Mākoha — Regulatory Posture: AUSTRALIA (TGA) and Ketryx Implementation Plan

**Jurisdiction:** AUSTRALIA · Therapeutic Goods Administration
**Prepared for:** Arepo Medtech Pty Ltd
**Version:** 1.2 · 2 September 2026 · supersedes v1.1 (1 September 2026) and v1.0 (31 August 2026)
**Status:** Working document. Not regulatory advice. Requires counsel attestation before any commitment.

> **How to read this document.** It is the Australian authority for Mākoha's regulatory
> posture and is written to stand alone: the complete standards stack (§4.3), every
> Australian obligation (§4.4), the gate structure (§7) and the Ketryx projection (§6)
> are all here. Three companion documents — REG-NZ (New Zealand), REG-US (United
> States) and REG-EU (European Union) — are written to the same replete-standalone
> rule. They deliberately repeat the standards stack rather than pointing here, so a
> reader holding any one of the four can act in that jurisdiction without the others.
> Where the four disagree, each is authoritative for its own jurisdiction and none
> governs another.

---

## §B Amendment log (v1.1 → v1.2) **[NEW v1.2]**

This revision was produced by (i) reconciling the posture against the Ketryx pre-demo
correspondence of 1 September 2026, (ii) closing the dangling forward references that
the survey-2 run flagged as BSQ-0001, and (iii) folding in a standards-gap review that
compared the `STD-*` stack against what TGA conformity assessment, an FDA submission and
an EU notified-body review would each expect to find. No v1.0 or v1.1 content is
deleted. Amended passages carry an inline **[AMENDED v1.2]** note. Every item that
originates from the gap review rather than from a TGA source is labelled
**[recommendation]** and carries a confidence tag so counsel can see provenance.

| # | Amendment | Trigger | Affected IDs |
|---|---|---|---|
| B-1 | Document declared **AUSTRALIA** in title, frontmatter and every section heading that carries jurisdiction-specific content. v1.1 was Australia-only by omission; v1.2 is Australia-only by declaration, with companions named. | User direction 2026-09-02; `Q-REG-008` | frontmatter; §0.9; §13 |
| B-2 | Standards stack extended from 13 to 26 rows. Editions pinned for `STD-001..013` (v1.1 named standards without editions; `WATCH-REG-005` said "confirm versions" but none were recorded). Thirteen rows added from the gap review. | Gap review; `WATCH-REG-005` | `STD-001..013` (editions); new `STD-014..026` |
| B-3 | MAK-GOV forward references homed. MAK-GOV §5 cites `REG-FIND-013`, `TASK-REG-023`, `ASSUME-REG-009` and `Q-REG-010` as belonging to "REG-POSTURE v1.2". They are defined here. `REG-FIND-012` is minted so the family has no gap. Closes survey-2 BSQ-0001 (DANGLING-REF). | MAK-GOV §5; BSQ-0001 | new `REG-FIND-012`, `REG-FIND-013`, `ASSUME-REG-009`, `Q-REG-010`, `TASK-REG-023` |
| B-4 | Electronic-record and electronic-signature integrity made a standing obligation. The "automated systems propose, humans release" rule is evidenced through e-signatures in Ketryx; that record must satisfy ISO 13485 §4.2.5 now and be 21 CFR Part 11-capable so the same record serves the later FDA file. v1.1 held the rule but not the record requirement. | Ketryx correspondence Q6 | new `OBL-015` |
| B-5 | Ketryx findings from the vendor's written answers folded: system-of-record position confirmed (design controls under an external ISO 13485 QMS); free-tier validation package position; configuration-item metering caveat (dependencies-as-items); Referenceable vs Incorporated cross-project semantics; manual-dependency mechanism for AI SOUP. All carried as vendor statements pending written confirmation. | Ketryx correspondence Q1–Q7 | `KTX-001`, `KTX-012` notes; new `KTX-013`, `KTX-014`; `Q-REG-006`; `ASSUME-REG-006` |
| B-6 | MDSAP raised as a question. A single MDSAP audit covers Australia (TGA accepts MDSAP certification as conformity-assessment evidence), the US, Canada, Brazil and Japan. Given the stated multi-jurisdiction sequence it is the QMS-certification route most likely to be author-once. | Gap review | new `Q-REG-011`; new `TASK-REG-024` |
| B-7 | ISO/IEC 27001 position reconciled with SEC-1. `REG-FIND-007` (TGA does not name 27001) and SEC-1 (Annex A controls retained as the equivalent-rigour set) are both correct and are now stated together, so nobody reads the posture as forbidding what SEC-1 requires. | SEC-1 §"Retained" | `STD-010` note; new `STD-024` |
| B-8 | IMDRF framework documents recorded as sources. TGA, Medsafe and FDA all cite IMDRF SaMD and cybersecurity documents; they are the jurisdiction-neutral spine beneath the jurisdiction-specific guidance and were absent from `SRC-REG-*`. | Gap review | new `SRC-REG-015..017` |
| B-9 | Standards-revision watch made specific: IEC 62304 Edition 2 (in development), ISO 13485 revision cycle, and TGA's periodic update of the standards matrix. | `WATCH-REG-005` | new `WATCH-REG-008` |
| B-10 | Census and self-audit updated; range endpoints checked at both ends per DEF-REG-001. | §12 | §12 |

### B.1 Provenance and confidence tags used in this revision

| Tag | Meaning |
|---|---|
| **[TGA-sourced]** | Traceable to a primary TGA or Commonwealth instrument named in §11 |
| **[vendor-stated]** | From Ketryx written correspondence; carries vendor interest; requires written confirmation before reliance |
| **[recommendation]** | Originates from the gap review, not from any Australian source; counsel and quality lead should confirm applicability before adoption |
| **[confidence: high / medium / low]** | Author's confidence that the item is correctly stated and currently in force; low-confidence items must be re-anchored to a primary source before `GATE-000` |

### B.2 What the review confirmed unchanged

`REG-FIND-001..011`, `REG-KEEP-001..004`, `FORK-REG-001` (three branches), the gate
structure `GATE-000..004`, `TASK-REG-001..022` and `KTX-001..012` stand. Nothing in
the Ketryx correspondence or the gap review contradicts the exemption finding or the
posture sentence in §3.

---

## §A Amendment log (v1.0 → v1.1)

This revision was produced by review against the Makoha Imago v1.1 repository. No
v1.0 content is deleted. Amended passages carry an inline **[AMENDED v1.1]** note and
the original reasoning is preserved beside the amendment.

| # | Amendment | Trigger | Affected IDs |
|---|---|---|---|
| A-1 | Status vocabulary reconciled with R30's register enum. Divergence between this document and its runtime register was a live AN-2 validator error. | R30 schema row fields vs §0.4 | §0.4 (extended); new §0.7 crosswalk |
| A-2 | `FORK-REG-001` extended from two branches to three. J-3 is not "contorting the product to fit the exemption" — it is a separate build artifact with the boundary enforced in code. v1.0 §2 posed the question correctly and answered it too narrowly. | MAK-J3 v0.9; MAK-FFC XC-2 realization note | `FORK-REG-001`; new `REG-FIND-009`; §2 amendment note |
| A-3 | Synthetic-data posture corrected. TGA AI guidance indicates synthetic data will generally **not** substitute for clinical data as safety-and-performance evidence. v1.0 `REG-KEEP-004` was silent on this and could be misread as validation sufficiency. | MAK-ANT Part 4 signal S-2 | new `REG-FIND-010`; `REG-KEEP-004` reading note; `GATE-002`; `TASK-REG-015` |
| A-4 | Live demo surface raised to Phase 0. demo.makoha.ai presents an AI conversational surface with third-party AI processing — simultaneously a claims exposure and an unassessed supplier. | Conflict C-10 (escalated) | new `TASK-REG-021`; new `OBL-013`; `TASK-REG-003` |
| A-5 | `TASK-REG-009` (Bedrock → Baseten) re-gated. v1.0 asserted the migration; the architecture self-declares service choice as changeable configuration but the decision is human and unmade. | Conflict C-03 → DEC-03 | `TASK-REG-009`; `ASSUME-REG-004` |
| A-6 | `ASSUME-REG-003` gains its interim rule. Patient-face work beyond the J-3-safe intake/consent/logistics subset is Blocked pending DEC-07, rather than merely undecided. | Conflict C-06 → DEC-07 | `ASSUME-REG-003` |
| A-7 | Jurisdiction breadth acknowledged. v1.0 is Australia-only; the north star is global and explicitly includes low-resource settings. Foreign instruments are now watched, not assumed absent. | MAK-FFC XC-3; MAK-J3 jurisdiction map; signals S-1, S-3 | new `WATCH-REG-006`, `WATCH-REG-007`; new `Q-REG-008` |
| A-8 | Third-party AI processing on any externally reachable surface becomes a standing obligation, not a Phase 2 task. | C-10; `OBL-005` scope | new `OBL-013` |
| A-9 | Claims inventory made a versioned artifact rather than a one-off reconciliation. | MAK-ANT AN-9 | new `OBL-014`; `TASK-REG-003` |
| A-10 | Ecosystem position documented: wrapper, runtime register, carrier map. v1.0 predated all three. | MAK-ANT AN-1/AN-5; R30 | new §0.8 |
| A-11 | Counsel packet scope widened to include the J-3 legal flags, which currently sit outside the `Q-REG` family and would otherwise reach counsel late. | MAK-J3 ⚑ flags; DEC-06; RG-02 | new `ASSUME-REG-008`; new `Q-REG-009`; `TASK-REG-002` |
| A-12 | New standard added to the stack: IEC 62304 §5.1.4 tool validation is called out explicitly rather than left implicit, because three tools now sit in the authoring path. | Nimbalyst, Ketryx free tier, GPP channel | new `STD-013` |

### A.1 Defect found in the review

**DEF-REG-001.** The Imago integrity audit records the obligations endpoint check as
`OBL-001..009 present ✓`. v1.0 defines `OBL-001..012`. The audit verified a prefix of
the range, not its endpoints, so `OBL-010`, `OBL-011` and `OBL-012` passed unchecked.
No content defect in either document; the check itself was incomplete. Recommend the
range-endpoint check be re-run against `OBL-014` after this fold.

### A.2 What the review confirmed unchanged

`REG-FIND-001` through `008` stand. Nothing in the ecosystem contradicts the exemption
finding, and MAK-J3 explicitly concurs: the diagnostic engine is diagnosis-contributing
and an AI-enabled CDSS will not meet the criteria. `REG-KEEP-001..003`, the standards
stack `STD-001..012`, the gate structure, and the Ketryx mapping `KTX-001..012` are
carried without change.

---

## §0 Document control and prompt-work conventions

### 0.1 Purpose in the ecosystem

This document is **advisory input**, not a governing contract. It does not carry
Implementer Contract authority and cannot be cited as evidence for a DONE. Its
findings are assertions about external regulation, and every material one is
carried as an `ASSUME-REG-*` requiring counsel attestation before it may be
relied upon.

Where this document and any governing document conflict, the governing document
prevails until an `ASSUME-REG-*` is closed by attestation, at which point the
governing document is amended to match.

### 0.2 Citation form for later prompts

Cite by stable ID, never by section number or page:

```
Per REG-FIND-001, the CDSS exemption is assessed unavailable.
Close ASSUME-REG-002 before actioning TASK-REG-005.
GATE-000 blocks all Phase 1 work.
```

Section numbers may move between versions. IDs are stable across versions and
are never reused after retirement.

### 0.3 ID scheme

| Prefix | Meaning | Closure condition |
|---|---|---|
| `REG-FIND-nnn` | Research finding about external regulation | Superseded by later finding or by attestation |
| `REG-KEEP-nnn` | Commitment retained regardless of pathway | Standing; retired only by pathway change |
| `ASSUME-REG-nnn` | Assumption requiring external closure | Written attestation from named party |
| `OBL-nnn` | Standing regulatory obligation | Never closes; evidence maintained continuously |
| `STD-nnn` | Standard in scope | Retired only by pathway change |
| `FORK-REG-nnn` | Pre-registered decision fork | Closed by trigger firing or by attestation |
| `GATE-nnn` | Blocking phase gate | All predecessor tasks DONE-with-evidence |
| `TASK-REG-nnn` | Sequenced work item | DONE-with-evidence or typed HALT |
| `KTX-nnn` | Ketryx configuration decision | Configured and verified in tooling |
| `WATCH-REG-nnn` | External change to monitor | Never closes; reviewed at stated cadence |
| `Q-REG-nnn` | Open question requiring external input | Answer received in writing |
| `SRC-REG-nnn` | Source reference | Retired when superseded upstream |

> **[AMENDED v1.1]** `REG-KEEP` was used in v1.0 §3.2 but omitted from the v1.0 ID
> scheme table and frontmatter `id_prefixes`. Added here. This was a latent
> validator failure against v1.0 check 1.

### 0.4 Status vocabulary

Aligned to Implementer Contract vocabulary. Permitted values only:

- `OPEN` — not started
- `IN-PROGRESS` — started, no evidence yet
- `DONE-WITH-EVIDENCE` — complete, evidence artifact named
- `HALT-TYPED` — blocked, with typed halt reason
- `SUPERSEDED` — replaced by a later ID, which must be named
- `ATTESTED` — closed by named external party, with date
- `REFUTED` — external attestation contradicted the item **[AMENDED v1.1]**

`ASSUME-REG-*` items may hold only `OPEN`, `ATTESTED`, `REFUTED` or `SUPERSEDED`.
No `ASSUME-REG-*` may be closed by internal reasoning.

> **[AMENDED v1.1]** `REFUTED` added. v1.0 had no state for "counsel attested, and
> the attestation went against us." Without it, a refuted assumption could only be
> recorded as `ATTESTED`, which reads as confirmation. This is the state
> `REG-FIND-001` enters if `ASSUME-REG-002` closes in favour of exemption.

### 0.5 Validator conventions

A companion validator over this document should enforce:

1. Every ID matches `^(REG-FIND|REG-KEEP|ASSUME-REG|OBL|STD|FORK-REG|GATE|TASK-REG|KTX|WATCH-REG|Q-REG|SRC-REG)-[0-9]{3}$`
2. Every ID appears exactly once in a definition table and zero-or-more times in prose
3. Every `TASK-REG-*` names its gate
4. Every `GATE-*` names its predecessor tasks, and every named predecessor exists
5. Every `ASSUME-REG-*` names an attesting party and a blocking gate
6. Every `REG-FIND-*` names at least one `SRC-REG-*`
7. Status values are drawn only from §0.4
8. No `ASSUME-REG-*` in `ATTESTED` or `REFUTED` state lacks an attestation date

Two additional checks introduced by this revision:

9. Every ID family declared in frontmatter `id_prefixes` appears in the §0.3 table
   and in the §12 census — **range endpoints checked at both ends** (per DEF-REG-001)
10. Every status value used anywhere in this document maps to an R30 register state
    under the §0.7 crosswalk

These are the same check shape used elsewhere in the ecosystem; see §12.

### 0.6 Firewall note

This document contains no case content, no evidence-library values, no
sensitivities, specificities or likelihood ratios. It is safe to load alongside
scoring-store material. It must **not** be used as a source for clinical content
under any circumstance.

### 0.7 R30 status crosswalk **[NEW v1.1]**

R30 (Regulatory Posture Register) carries a register-lifecycle enum that is broader
than this document's item vocabulary. The two are not in conflict once the layers are
distinguished: §0.4 states what a *document item* holds; R30 additionally holds
*register-row* lifecycle. Crosswalk:

| §0.4 document state | R30 register state | Note |
|---|---|---|
| `OPEN` | `OPEN` | direct |
| `IN-PROGRESS` | `OPEN` | R30 does not distinguish; document grain is finer |
| `ATTESTED` | `ATTESTED` | direct; date mandatory both sides |
| `REFUTED` | `REFUTED` | direct **[new both sides]** |
| `SUPERSEDED` | `CLOSED` | R30 closes the row; document names the successor |
| `DONE-WITH-EVIDENCE` | `CLOSED` | evidence artifact named in both |
| `HALT-TYPED` | `OPEN` + blocks | R30 carries the blocker in `blocks` |
| — | `ARMED` | register-only: `FORK-REG` trigger armed, not yet fired |
| — | `passed` | register-only: `GATE-*` passed |

`ARMED` and `passed` have no document-item equivalent and must not be written into
this document. Writing them here is a validator error under check 7.

### 0.8 Position in the document ecosystem **[NEW v1.1]**

| Relationship | Artifact | Effect |
|---|---|---|
| Wrapper | MAK-ANT v1.0, Antennae Corpus | Folds this document verbatim as Annex 1; adds twelve normative sensing duties (AN-1..12) that bind the series to it |
| Runtime register | R30, Regulatory Posture Register (Proposed, DEC-02) | Row-level home for every ID here; owner `cdss-governance`; opens at L1 |
| Carrier map | MAK-ANT Part 3 | Maps each ID family to the corpus volume(s) that carry it; maintained under AN-5 |
| Signal log | MAK-ANT Part 4 | Additive log of regulatory signals received after this document's currency date |
| Canonicity | This file | Where a standalone REG-POSTURE file is maintained, it is canonical and the MAK-ANT annex mirrors it. Divergence is a validator error |

Consequence for revision: a new posture version is **folded**, never edited in place
in the annex, and the fold re-runs the carrier map before completing.

### 0.9 Jurisdiction declaration and the replete-standalone rule **[NEW v1.2]**

**This document is AUSTRALIA.** Every finding, obligation, gate and task in it is
stated against the Therapeutic Goods Act 1989, the Therapeutic Goods (Medical Devices)
Regulations 2002, and TGA guidance. Where a foreign instrument appears (FDA, EU MDR,
Medsafe) it appears only as a watch item or a cross-reference explaining why an
Australian choice was made a particular way.

The four jurisdiction documents share one standards stack and one architecture. They
do **not** share text by reference. The rule, adopted 2 September 2026:

1. Each jurisdiction document carries the **complete** standards stack, with the
   recognition status of each standard in that jurisdiction.
2. Each carries its own obligations, gates, tasks, assumptions, questions, watch items
   and sources, in its own ID namespace (`REG-*` here; `NZ-*`; `US-*`; `EU-*`).
3. Shared programme artifacts — the intended purpose statement, the ISO 14971 risk
   file, the IEC 62304 lifecycle records, the technical documentation — are built
   **once** and projected per regulator. The documents describe the projection; they
   do not duplicate the artifact.
4. A change to the shared stack is made in all four documents in the same revision
   cycle, or the divergence is logged in the wrapper (MAK-ANT) as a signal.

Rationale: a reader holding one document — counsel in one country, a notified body,
a sponsor — must be able to act without the others. Duplication of the stack table is
the price of that, and it is cheap relative to the cost of a reader missing a
standard because it lived in another file.

---

## §1 The headline finding

The working assumption in recent discussion was that a deterministic release path
("ML proposes and tests; only arithmetic releases") would keep the CDSS exemption
available, and that documenting to SaMD standard would give both-ways optionality.

**Having read the current TGA guidance in full, that assumption does not survive
contact.** Mākoha, as a Bayesian differential-diagnosis engine, is very unlikely to
qualify for the CDSS exemption — and the reason is not AI. It is the diagnostic
function itself.

This is a better finding to have now than after building for it.

### 1.1 Findings register

| ID | Finding | Status | Sources |
|---|---|---|---|
| `REG-FIND-001` | Mākoha is assessed as **not eligible** for the CDSS exemption. The disqualifier is the diagnostic function, not the use of AI. | OPEN | `SRC-REG-001` |
| `REG-FIND-002` | "Recommendation" is defined to exclude making a diagnosis, providing new diagnostic information, **or contributing to the diagnosis** of a particular condition. A ranked differential with posteriors is all three. | OPEN | `SRC-REG-001` |
| `REG-FIND-003` | Opacity is independent of machine learning. A CDSS can be opaque without ML and thereby fail criterion (c). Determinism is necessary but not sufficient for transparency. | OPEN | `SRC-REG-001` |
| `REG-FIND-004` | The transparency test is "glass box" — the clinician must be able to see and review the internal logic. A published, named instrument satisfies this; a novel composite computation does not. | OPEN | `SRC-REG-001` |
| `REG-FIND-005` | Exempt status does not remove Essential Principles, adverse event reporting, advertising compliance, notification, or recall exposure. | OPEN | `SRC-REG-001` |
| `REG-FIND-006` | ISO 13485:2016 compliance carries **deemed** conformity status for specified parts of the conformity assessment procedures. AS ISO 13485:2017 is accepted as identical. | OPEN | `SRC-REG-004` |
| `REG-FIND-007` | TGA cyber security expectations are device-specific and do not name ISO 27001; ISO 27799 (27002 applied to health) and ISO/IEC 29147 / 30111 are the recognised mapping path. | OPEN | `SRC-REG-003` |
| `REG-FIND-008` | IEC 82304-1 is the only standard in the TGA matrix marked relevant to every applicable Essential Principle for health software on general computing platforms. | OPEN | `SRC-REG-008` |
| `REG-FIND-009` **[NEW v1.1]** | The exemption tier is reachable as a **separate build artifact**, not as a constrained version of the classified product. Where the capability boundary is structurally absent from the artifact and its dependency graph — not disabled by configuration — an exempt-tier product can ship beside the classified track without contaminating it. Crossing the boundary is a new device, not an update. | OPEN | `SRC-REG-001`, `SRC-REG-011` |
| `REG-FIND-010` **[NEW v1.1]** | Synthetic data will **generally not substitute for clinical data** as safety-and-performance evidence. Synthetic-only development is a control posture, not validation evidence. | OPEN | `SRC-REG-012` |
| `REG-FIND-011` **[NEW v1.1]** | Functional updates to AI-enabled medical device software are regulatory events to be handled **pre-deployment**, and transparency expectations extend to training data, validation and ongoing monitoring — not only to the runtime output shown to a clinician. | OPEN | `SRC-REG-012` |
| `REG-FIND-012` **[NEW v1.2]** | No standard in the TGA standards matrix is mandatory. Every `STD-*` row is a **voluntary evidence route** to demonstrating compliance with an Essential Principle; the Essential Principles themselves are the legal test (Regulations Schedule 1; Act s41FN). Consequence: the stack is chosen for evidential leverage, not because any standard is "required", and a standard absent from the matrix (e.g. BS/AAMI 34971) is still admissible as evidence if the EP mapping is argued. **[TGA-sourced; confidence: high]** | OPEN | `SRC-REG-002`, `SRC-REG-008` |
| `REG-FIND-013` **[NEW v1.2]** | A **non-device line is available** beside the classified track: the Governance Layer (MAK-GOV) analyses organisational conformance, not patient state, has no clinical write path and makes no patient-specific recommendation. On that architecture the s41BD device definition is arguably not met. This is the replacement for the J-3 exempt-tier reserve as the non-classified route. It is a finding about availability, **not** a classification: nothing ships before counsel attests (`ASSUME-REG-009`). **[programme-sourced; confidence: medium — accessory question and "analysing for a medical purpose" unresolved]** | OPEN | `SRC-REG-018`, `SRC-REG-006` |

### 1.2 Why determinism doesn't rescue it

Two things in the October 2025 guidance rewrite are decisive.

**First, "recommendation" is defined narrowly and explicitly excludes diagnostic
contribution** (`REG-FIND-002`). A recommendation means advice to take steps, gather
further inputs, or follow a course of action, plus general information about
conditions, risks, treatment pathways and prevention. It expressly does *not* mean
making a diagnosis, providing new diagnostic information, or contributing to the
diagnosis of a particular disease or condition.

A ranked differential with posterior probabilities is, on any honest reading,
new diagnostic information contributing to the diagnosis of a particular condition.

**Second, opacity is not the same as machine learning** (`REG-FIND-003`). The
guidance states plainly that a CDSS can be opaque regardless of whether it
incorporates ML, and that opaque systems fail criterion (c). "Glass box" means the
clinician can see and review the internal logic — a computerised flowchart following
an established guideline is the worked example. A deterministic Bayesian computation
over a proprietary evidence library is deterministic but not thereby transparent. The
clinician cannot independently verify the posterior.

### 1.3 The two examples that bind hardest

The guidance gives worked examples. Two of them sit almost exactly on Mākoha.

**Non-exempt, Example 4 (sepsis flagging).** An evidence-based, *proprietary*,
threshold-based tool that alerts and recommends a management plan. Not exempt —
partly for monitoring, but critically because the software does not reference or
step through the logic and calculations behind its alerts. No ML involved. It fails
anyway.

**Not-a-medical-device, Example 1.** A web app returning referenced information
about conditions from a practitioner's symptom search — and the guidance
specifically notes it does **not** indicate probability of a match, red flags, or
priorities. Adding any of those three is what pushes a tool out of that category.
Mākoha does all three by design.

### 1.4 The one example that shows what exempt actually looks like

**Exempt, Example 1 (McIsaac / Modified Centor).** The GP enters age, fever, cough,
exudate, swelling. The software computes a probability score *according to the
referenced published scoring tool* and outputs recommended pathways.

Note what makes this work: it is a single, named, published instrument. The clinician
knows the score, can compute it by hand, and can check the software. The probability
output is fine *because the instrument is external and verifiable*.

Mākoha's engine is not a published instrument. Its likelihood ratios may be sourced
from literature, but the combination — the prior selection, the LR chaining, the
conformal interval — is a novel computation. That is the gap. Not the arithmetic.
The novelty.

---

## §2 What exemption-compatible would actually cost

It is worth being explicit about the product you would have to build to hold the
exemption, because it is not Mākoha with a flag flipped.

You would need to ship a tool that:

- Executes **named published instruments only** (Wells, CHA₂DS₂-VASc, Centor,
  CURB-65, etc.), each cited with version and date
- Never combines instruments into a novel composite score
- Never outputs a ranked differential, a posterior probability, or a red-flag
  priority ordering derived from its own model
- Never performs monitoring — no threshold-crossing alerts on patient state
- Never processes or interprets a signal or image from another device
- Serves health professionals only — no patient surface

That is a legitimate and useful product. It is a guideline execution and
documentation layer. It is not a differential diagnosis engine, and it does not
deliver the thesis on the Mākoha site.

**Recommendation: do not contort the product to fit the exemption.** The exemption is
sized for guideline digitisation. Mākoha is aiming past it.

### 2.1 Amendment note **[AMENDED v1.1]**

The v1.0 recommendation above is **retained and still correct as to J-1 and J-2**:
neither classified branch should be contorted to fit the exemption.

It was, however, answered too narrowly. The specification above — published
instruments only, no composite scores, no differential, no monitoring, health
professionals only — is not merely a description of what you would have to give up.
It is a **product specification**, and the ecosystem has since written it as one:
Addendum J-3, the Guideline-Prompt Profile, realising MAK-FFC XC-2.

The distinction v1.0 missed is between *constraining the product* and *building a
second artifact*. J-3 is the latter: the same spine — justification fabric, guideline
compiler, versioning, ledger, deviation machinery — assembled into a distinct build
whose inference plane contains only ratified published guidelines evaluated
deterministically, with differential, conformal, runtime-LLM and RPM capabilities
structurally absent from the artifact and its dependency graph. Absent, not disabled.

This matters for three reasons the posture should have carried:

1. **Market entry** where classification timelines or economics block deployment,
   including the low-resource settings the north star names (XC-3).
2. **Evidence accumulation** — deployed guideline-prompt use generates real usage,
   deviation and guideline-gap evidence that seeds classified-track validation. Given
   `REG-FIND-010`, this is now materially more valuable than it looked in v1.0,
   because it is a route to *clinical* rather than synthetic evidence.
3. **Regulatory hedge** — if the classified timeline slips, something lawful and
   spine-true still ships.

The honesty constraint is absolute and is XC-1's, not this document's: J-3 is never
marketed, configured, or quietly extended to do classified work under an exempt
label. Crossing the boundary is a new device, not a channel upgrade.

**Consequence:** `FORK-REG-001` gains a third branch. See §3.1.

**Caution retained:** J-3 remains v0.9-proposed with two unresolved legal flags and
awaits DEC-06 ratification. It is a reserve, not a plan. Carried as
`ASSUME-REG-008` / `Q-REG-009`.

---

## §3 Revised posture

> **Build to SaMD standard. Test exemption honestly at a named gate. Assume
> inclusion.**

This is a change from "build exemption-compatible, document to SaMD standard." The
architectural constraint is dropped; the documentation discipline is not.

> **[AMENDED v1.1]** The posture sentence stands. Read it now with J-3 in view: the
> exemption is not tested by asking whether Mākoha squeezes into it, but by asking
> whether a separate lawful artifact is worth shipping beside it. Those are different
> questions with different answers, and v1.0 collapsed them.

### 3.1 The fork, restated

| Field | Value |
|---|---|
| ID | `FORK-REG-001` |
| Prior framing (v1.0) | Exempt (J-1) vs ARTG-included (J-2) |
| v1.0 revision | Lower-class included (J-1) vs higher-class included (J-2) |
| **v1.1 revision** | **Three branches: J-1 lower-class included · J-2 higher-class included · J-3 exempt-tier reserve, shipped as a separate artifact beside either** |
| Decision point | Maturity Level 4, on Level 3 abstention evidence — **unchanged** |
| J-3 decision point | Independent of L4. J-3 is not a fork outcome; it is a parallel channel. Gated on DEC-06 |
| Status | OPEN |
| Blocking | `ASSUME-REG-001`, `ASSUME-REG-002`, `ASSUME-REG-008` |
| Ratification | DEC-01 (relabel portfolio-wide) remains Open; closes only on `ASSUME-REG-002` |

The maturity-gate mechanism survives. J-1 and J-2 remain a genuine either/or resolved
at L4. J-3 is **not** a third outcome of that gate — it is a separate release channel
that can run concurrently with either branch, which is why it carries its own decision
(DEC-06) rather than waiting on L4.

### 3.2 Retained regardless of pathway

| ID | Commitment | Rationale after `REG-FIND-001` |
|---|---|---|
| `REG-KEEP-001` | Deterministic release path | No longer exemption-motivated; remains correct safety architecture and strengthens the Essential Principles case |
| `REG-KEEP-002` | Reviewable basis for every output | Not a ticket to exemption; directly responsive to Essential Principle 13 and to clinician trust, which is the product thesis |
| `REG-KEEP-003` | Human sign-off, fail-closed | Unchanged |
| `REG-KEEP-004` | Synthetic-only until controls operate | Unchanged as a *control* commitment. **[AMENDED v1.1]** Explicitly **not** a validation-evidence commitment — see `REG-FIND-010`. Synthetic-only satisfies `GATE-002`; it does not contribute to `GATE-003` |

> **[AMENDED v1.1] Reading note on `REG-KEEP-004`.** v1.0 stated the commitment
> without stating its limit, and the limit matters more than the commitment. Synthetic
> data protects patients during development. It does not evidence that the device
> works. Any programme plan that treats the synthetic corpus as reducing the clinical
> evidence burden is reading `REG-KEEP-004` wrongly, and the error would surface at
> the most expensive possible moment — conformity assessment. `TASK-REG-015` is
> therefore not deferrable behind the synthetic phase; it runs in parallel from
> Phase 1.

### 3.3 Changed

- Stop treating the exemption as the target. Treat it as a fallback to be tested
  once, formally, and then closed (`ASSUME-REG-002`).
- Stop deferring ARTG classification work. It is now the live path.
- The J-1/J-2 fork is no longer *exempt vs included*. It is *lower-class included vs
  higher-class included*. Still worth having, but reframe it.
- **[NEW v1.1]** Treat J-3 as a standing reserve with its own ratification path, not
  as a consolation prize reachable by degrading the classified product.

### 3.4 The one honest caveat

A narrow reading could argue Mākoha "supports a recommendation" and never asserts a
diagnosis. Do not rely on this without counsel. The guidance's definition of
recommendation explicitly excludes *contributing to* diagnosis, which is a low bar to
cross, and the sepsis example shows TGA applying it strictly to proprietary
evidence-based logic. Get a written opinion before spending anything on the
assumption.

This caveat is carried as `ASSUME-REG-002` and is the only permitted route to
reversing `REG-FIND-001`. **[AMENDED v1.1]** If it closes in our favour,
`REG-FIND-001` takes state `REFUTED`, not `ATTESTED` — see §0.4.

---

## §4 Regulatory obligations under the assumed path

### 4.1 Classification

Software as a medical device, providing diagnostic information. Under the software
classification rules introduced in February 2021, diagnostic SaMD classification
depends on the seriousness of the condition and the role of the information. Expect
Class IIa at minimum; Class IIb is plausible where output bears on serious
conditions. **This requires counsel** (`ASSUME-REG-001`) — it drives cost, timeline
and conformity assessment route.

### 4.2 Conformity assessment

ARTG inclusion requires conformity assessment evidence. The TGA route or an
EU-notified-body route are both available; for an Australian-first product with a
pharmacy wedge, TGA Conformity Assessment certification is the natural path
(`Q-REG-005`).

**The lever that matters** (`REG-FIND-006`): under the Therapeutic Goods (Conformity
Assessment Standard for Quality Management Systems) Order 2019, a QMS complying with
ISO 13485:2016 is *treated as* complying with specified parts of the conformity
assessment procedures. AS ISO 13485:2017 is the identical Australian adoption and is
accepted. This is deemed status, not persuasion — it is the single highest-leverage
compliance investment available to you.

### 4.3 Standards stack — AUSTRALIA **[AMENDED v1.2]**

> **[AMENDED v1.2]** The v1.1 table is carried in full and extended. Editions are now
> pinned (column "Edition"); the v1.1 rows named standards without editions. Column
> "TGA status" records whether the standard appears in the TGA standards matrix
> (`SRC-REG-002`/`SRC-REG-008`) — recall `REG-FIND-012`: appearance in the matrix is
> evidential convenience, not obligation. Rows `STD-014..026` are **[recommendation]**
> rows from the 2 September 2026 gap review and carry a confidence tag. Priority 1 =
> conformity assessment cannot proceed without it; 2 = expected in the technical
> documentation; 3 = expected for the cyber/EP 12 case; 4 = situational.

#### 4.3.1 Core lifecycle and quality (carried from v1.1, editions pinned)

| ID | Standard | Edition | Role in the Australian file | TGA status | Priority |
|---|---|---|---|---|---|
| `STD-001` | ISO 13485 | :2016 (AS ISO 13485:2017 identical adoption) | QMS — **deemed conformity** for specified parts of the conformity assessment procedures under the Therapeutic Goods (Conformity Assessment Standard for QMS) Order 2019 (`REG-FIND-006`) | Named in the 2019 Order | **1** |
| `STD-002` | IEC 62304 | :2006 + A1:2015 | Software lifecycle, software safety classification (expect Class B or C per §4.3 of the standard), SOUP management, change control, problem resolution. §5.1.4 tool validation → `STD-013` | In matrix | **1** |
| `STD-003` | ISO 14971 | :2019 | Risk management — the risk file (`TASK-REG-007`) is the spine everything else hangs from | In matrix | **1** |
| `STD-004` | IEC 62366-1 | :2015 + A1:2020 | Usability engineering — three surfaces (clinician, pharmacist, patient), three use-related risk analyses (`TASK-REG-014`) | In matrix | **2** |
| `STD-005` | IEC 82304-1 | :2016 | Health software product safety and security requirements — the only standard marked relevant to every applicable EP for software on general computing platforms (`REG-FIND-008`) | In matrix, all EPs | **2** |
| `STD-006` | BS/AAMI 34971 | :2023 | Application of ISO 14971 to machine learning — the ML risk hook; carried into the Ketryx Risk item (`KTX-003`) | Not in matrix — admissible per `REG-FIND-012` | **2** |
| `STD-013` | IEC 62304 §5.1.4 + ISO 13485 §4.1.6 | as above | Validation of software tools in the authoring and release path — the authoring surface (Nimbalyst), the Ketryx free tier (validation package is Essentials-tier; see `KTX-013`), and the release channel | Implicit in `STD-001`/`STD-002` | **2** |

#### 4.3.2 Cyber security and information security (carried from v1.1, editions pinned)

| ID | Standard | Edition | Role in the Australian file | TGA status | Priority |
|---|---|---|---|---|---|
| `STD-007` | ANSI/AAMI SW96 | :2023 | Security risk management for device manufacturers — companion to ISO 14971 for the security risk file | In matrix | 3 |
| `STD-008` | IEC 81001-5-1 | :2021 | Security activities in the health software product lifecycle — the secure-development-lifecycle evidence for EP 12.1(5) (`OBL-009`) | In matrix | 3 |
| `STD-009` | ISO/IEC 29147 and ISO/IEC 30111 | 29147:2018; 30111:2019 | Vulnerability disclosure (29147) and vulnerability handling (30111) — the disclosure-to-users duty in EP 12.1(5) and the CAPA linkage (`TASK-REG-012`, `OBL-008`) | Named in TGA cyber guidance (`REG-FIND-007`) | 3 |
| `STD-010` | ISO 27799 | :2016 | Information security management in health — ISO/IEC 27002 controls applied to health information. TGA's recognised mapping for organisational infosec (`REG-FIND-007`). **[AMENDED v1.2]** Read with `STD-024`: TGA does not name ISO/IEC 27001, but SEC-1 retains 27001 Annex A technical controls as the equivalent-rigour set. Both hold: 27799 is what you cite to the TGA; Annex A is what you implement | Named in TGA cyber guidance | 3 |
| `STD-011` | IEC 80001-1 | :2021 | Risk management for health IT systems incorporating medical devices — the deployment-side (practice/pharmacy network) risk conversation | In matrix | 4 |
| `STD-012` | UL 2900-2-1 | :2017 | Network-connectable healthcare product security testing — the penetration-test yardstick (`OBL-007`, `TASK-REG-016`) | In matrix | 4 |

#### 4.3.3 Added in v1.2 — gap-review rows **[NEW v1.2 — recommendation]**

| ID | Standard | Edition | Why it is load-bearing for Mākoha in Australia | TGA status | Priority | Confidence |
|---|---|---|---|---|---|---|
| `STD-014` | ISO/TR 24971 | :2020 | The official guidance on applying ISO 14971:2019. A conformity assessor will expect the risk file's method (risk acceptability criteria, benefit-risk, production and post-production information) to follow it. Without it the risk file is method-less | Not in matrix (TR) | **2** | high |
| `STD-015` | IEC/TR 80002-1 | :2009 | Application of ISO 14971 to medical device software — the bridge between the risk file and the IEC 62304 software safety classification; the reference for arguing Class B vs C | Not in matrix (TR) | **2** | high |
| `STD-016` | AAMI TIR45 | :2023 | Agile practices in medical device software development. Directly relevant to a git-native, AI-assisted, continuously integrated build: it is how you show that continuous delivery **is** an IEC 62304 lifecycle, not an exception to one | Not in matrix | **2** | high |
| `STD-017` | AAMI TIR57 | :2016 (R2023) | Principles for medical device security — risk management. Already implicit in `KTX-007` (Ketryx STRIDE threat-model item types reference it). Formalised as a standard so the threat model has a cited method | Not in matrix | 3 | high |
| `STD-018` | ISO 14155 | :2020 | Clinical investigation of medical devices — good clinical practice. Governs any prospective clinical evidence collection (`TASK-REG-015`, Lumos linkage) and is what makes NZ- or AU-collected evidence admissible to conformity assessment | Recognised for clinical evidence | **2** | high |
| `STD-019` | ISO 20417 | :2021 | Information to be supplied by the manufacturer — labelling, instructions for use, the information EP 13 requires. Replaces the labelling parts of the withdrawn ISO/EN 1041 | In matrix (EP 13) | **2** | high |
| `STD-020` | ISO 15223-1 | :2021 | Symbols used with information supplied by the manufacturer — where any symbol appears in UI, IFU or labelling | In matrix (EP 13) | 3 | high |
| `STD-021` | ISO/IEC 42001 | :2023 | AI management system. Not device-specific, but increasingly the organisational evidence regulators and procurement ask for behind BS/AAMI 34971; the EU AI Act's QMS expectation maps onto it. Recommend **alignment**, not certification, at this stage | Not in matrix | 4 | medium |
| `STD-022` | ISO/IEC 23894 | :2023 | AI risk management guidance — the AI-general companion to ISO 14971 + 34971; useful for the model-governance argument (Primer J) and for the transparency expectations in `REG-FIND-011` | Not in matrix | 4 | medium |
| `STD-023` | IEC 60601-4-5 | :2021 | Safety-related technical security specifications — security capability levels referenced by IEC 81001-5-1. Applicable **only if** Mākoha claims security capability levels; otherwise record as considered-not-applicable in the technical file | Not in matrix | 4 | medium |
| `STD-024` | ISO/IEC 27001 | :2022 | Information security management system. **Not required by TGA** (`REG-FIND-007`) — recorded here so the stack is honest about what SEC-1 already implements (Annex A controls) and what Australian PHN/hospital procurement and NZ Te Whatu Ora procurement routinely ask for. Certification is a commercial decision, not a regulatory one | Not named by TGA | 4 | high |
| `STD-025` | IMDRF SaMD framework documents | N10:2013 (key definitions), N12:2014 (risk categorisation), N23:2015 (QMS), N41:2017 (clinical evaluation) | The jurisdiction-neutral spine beneath TGA, Medsafe and FDA software guidance. Not standards, but the vocabulary every regulator uses; the N12 risk category (state of healthcare situation × significance of information) is the argument structure for classification under `ASSUME-REG-001` | Referenced by TGA guidance | **2** | high |
| `STD-026` | IMDRF cyber and ML documents | N60:2020 (cybersecurity principles), N70:2023 (legacy devices), N73:2023 (SBOM), N88:2025 (GMLP) | Same role for cyber and ML: N73 is the SBOM content expectation behind `OBL-004`; N88 is the good-machine-learning-practice reference behind the ML risk file | Referenced by TGA cyber guidance | 3 | medium (N88 currency to verify) |

#### 4.3.4 Considered and not adopted **[NEW v1.2]**

| Standard | Reason not adopted |
|---|---|
| IEC 60601-1 family (other than 60601-4-5) | Medical electrical equipment; Mākoha has no hardware |
| ISO/IEC TS 82304-2:2021 | Health app quality label; consumer-app oriented, subsumed by 82304-1 for a regulated device |
| PCI-DSS | Already ruled inapt in Arch §11.1 T4 / SEC-1 |
| ISO 9001 | Superseded in this context by ISO 13485; no additional evidential value |

#### 4.3.5 Australian instruments in scope that are not standards

Also in scope and not covered by any of the above: Australian Privacy Principles,
the Notifiable Data Breach scheme, advertising requirements for therapeutic goods,
and adverse event reporting. **[AMENDED v1.2]** Each is carried as an `OBL-*` row in
§4.4; the legislative instruments are listed as `SRC-REG-005`, `SRC-REG-006` and the
Privacy Act 1988 (`OBL-011`).

### 4.4 Standing obligations register

Non-closing. Evidence maintained continuously.

| ID | Obligation | Source of duty |
|---|---|---|
| `OBL-001` | Comply with Essential Principles (Schedule 1) | Applies whether exempt or included |
| `OBL-002` | Report adverse events to TGA | Applies whether exempt or included |
| `OBL-003` | Comply with therapeutic goods advertising requirements | Applies whether exempt or included |
| `OBL-004` | Maintain SBOM for vulnerability cross-referencing | TGA cyber guidance |
| `OBL-005` | Assess third-party platform security, explicitly including cloud and web services | TGA cyber guidance |
| `OBL-006` | Contractual cyber security expectations with suppliers, including agreed incident reporting thresholds | TGA cyber guidance |
| `OBL-007` | Penetration testing by a party independent of the development team | TGA cyber guidance |
| `OBL-008` | Vulnerability monitoring feeding CAPA, documented regardless of risk outcome | TGA cyber guidance |
| `OBL-009` | EP 12.1(5): protection against unauthorised access, minimisation of known vulnerabilities, update/patch pathway, **disclosure of known vulnerabilities to users** | Essential Principle 12.1(5) |
| `OBL-010` | Maintain sufficient information to substantiate Essential Principles compliance, available to TGA on request | Act s41FN(3) |
| `OBL-011` | Australian Privacy Principles and Notifiable Data Breach scheme | Privacy Act 1988 |
| `OBL-012` | Notify TGA within 30 working days of supply — **exempt pathway only** (J-3 channel, or if `ASSUME-REG-002` closes in favour of exemption) | Schedule 4 Part 2 notification duty |
| `OBL-013` **[NEW v1.1]** | Every externally reachable surface that routes user input to a third-party AI provider is inventoried as a supplier under `OBL-005`/`OBL-006`, its processing disclosed, and its presence reconciled against the intended-purpose statement before the surface remains public | `OBL-005`; conflict C-10 |
| `OBL-014` **[NEW v1.1]** | The claims inventory — public positioning, marketing copy, in-product copy — is versioned and diffed against the intended-purpose statement every release | MAK-ANT AN-9; `OBL-003` |
| `OBL-015` **[NEW v1.2 — recommendation; confidence: high]** | Every electronic record and electronic signature that evidences a human release decision (the "automated systems propose, humans release" rule, `REG-KEEP-003`) is controlled as a quality record under ISO 13485 §4.2.5 — identifiable, legible, retrievable, protected against alteration, retained for the device lifetime — **and** is generated in a form that satisfies 21 CFR Part 11 (unique user attribution, MFA-backed signature, append-only audit trail, signature manifestation with meaning and date/time). Australia does not require Part 11; it is adopted now so the same record serves the later US file without re-creation. Ketryx states its signatures and audit trail are Part 11 compliant **[vendor-stated]**; that statement is verified, not assumed (`KTX-014`) | ISO 13485 §4.2.5; `REG-KEEP-003`; author-once rule §0.9 |

`OBL-007`, `OBL-009` and `OBL-014` are explicitly **outside the scope of any
compliance platform** and must be resourced separately. **[AMENDED v1.2]** `OBL-015`
is *partly* inside the platform (the signature and audit-trail mechanism) and partly
outside it (the SOP that says who may sign what, and the tool-validation evidence that
the mechanism works as stated).

> **[AMENDED v1.1]** `OBL-012` scope widened. v1.0 conditioned it solely on
> `ASSUME-REG-002` closing in favour of exemption. With J-3 as a standing channel, the
> notification duty attaches to any J-3 supply regardless of how `ASSUME-REG-002`
> resolves for the classified track.

---

## §5 Stack implications

### 5.1 Bedrock → Baseten (Sydney, dedicated)

Confirmed rationale, unchanged by the exemption finding:

- **Version pinning.** Deploying your own weights on dedicated infrastructure means
  the model changes when you say so. Managed endpoints do not give you this, and
  without it your change control is fiction.
- **Environment promotion** as a native change-control gate.
- **Region-locked deployment**, Sydney — satisfies data residency.
- Region-restricted, single-tenant and self-hosted/VPC options; stated non-retention
  of model inputs and outputs; SOC 2 Type II and HIPAA posture.

Caveats: HIPAA is not the APPs — evidence of maturity, not compliance with your
regime. Only the *dedicated* path delivers the pinning benefit; their hosted model
APIs put you back where Bedrock had you. And SOUP obligations do not disappear —
Baseten and the model remain SOUP, you just gain the ability to discharge the
obligations properly.

> **[AMENDED v1.1] Status correction.** v1.0 presented this migration as settled. It
> is not. The architecture specifies Bedrock via PrivateLink with no public egress;
> this document proposed Baseten. That is conflict C-03, escalated to **DEC-03**, and
> the decision is human and unmade. The architecture self-declares service choices as
> changeable configuration, so the change path exists — but `TASK-REG-009` may not
> proceed until DEC-03 rules. The pinning argument above stands as the case *for* the
> change; it is not the change.
>
> Note also that the Bedrock option is not merely inferior: PrivateLink with no public
> egress is a real network-posture advantage that the Baseten comparison in v1.0 did
> not weigh. DEC-03 should weigh both.

| ID | Item | Status |
|---|---|---|
| `ASSUME-REG-004` | Baseten Sydney region available on dedicated deployment with contractual version-stability and change-notice terms | OPEN — closes on written confirmation from Baseten; **and is moot unless DEC-03 rules for Baseten** |

### 5.2 Amplify git-push

Fine for the synthetic demo. A finding on a regulated release path. Needs a gate
before first clinical supply — see `TASK-REG-010`.

> **[AMENDED v1.1]** `REG-FIND-011` sharpens this: functional updates to AI-enabled
> medical device software are regulatory events handled **pre-deployment**. A
> push-to-deploy path is not merely a documentation gap at that point; it is a
> pre-deployment control that does not exist.

### 5.3 Nimbalyst

Keep as the pre-regulatory authoring and agent-orchestration surface. Do **not**
build a shim into Jira. Both write to git; inserting a translator between two things
that already share a substrate adds a validated-tool obligation and breaks record
provenance. Promotion from Nimbalyst into the regulated system should be a deliberate
human act landing as a commit or a Jira issue.

Disable PostHog telemetry (Settings → Advanced → Analytics) before anything
non-synthetic goes near it.

**Ecosystem interaction (carried forward, unchanged):**

- **Observer independence.** The shared workspace, context graph and searchable
  session history make it easy to accidentally give the Observer the builder's
  context. The session-level file read/write record is, conversely, good independence
  evidence. Any clause added to `observer_adjudication.md` should be
  mechanism-neutral, not vendor-named.
- **Diff-review provenance.** Accept/reject decisions in the diff pane live in the
  app, not in git. A human approval only counts as admissible if it lands as a commit
  or CI artifact.
- **Toolchain pinning.** If Nimbalyst enters the authoring path it is a versioned
  tool — one `RECON-SPINE-n` row or an ASSUME. This is also the IEC 62304 §5.1.4
  answer, now carried as `STD-013`.

### 5.4 The live demo surface **[NEW v1.1]**

demo.makoha.ai presents an AI conversational surface and discloses that conversations
are processed via third-party AI providers. This creates two exposures that v1.0 did
not capture, because v1.0 treated the demo as a synthetic-data question only:

1. **Claims exposure.** Advertising obligations bind exempt and included devices
   alike (`OBL-003`). A public AI conversational surface is a claim about what the
   product does, made before the intended-purpose statement exists to be matched
   against. This is conflict C-10, escalated to Phase 0.
2. **Supplier exposure.** Third-party AI processing of user input is a supplier
   relationship under `OBL-005`/`OBL-006` — unassessed, uncontracted, and currently
   undocumented in the SBOM. This holds regardless of the data being synthetic,
   because the obligation attaches to the processing arrangement, not the data.

Neither is resolved by the surface being a demo. Actioned as `TASK-REG-021` and
`OBL-013`.

---

## §6 Ketryx integration

Ketryx is the right shape for this: an overlay on Jira and Git that derives
traceability from work as it happens, rather than a parallel document world you
maintain by hand. Critically, it does not become the system of record for your code
or your work items — it reads them.

### 6.1 Commercial

Free tier for pre-market companies under $2M funding: 3 projects, up to 150
configuration items, Jira + Git integration with unlimited repos, 4 users,
50 generated documents/year, 10 GB storage, self-serve Jira integration, docs and
on-demand training videos.

**Watch item** (`WATCH-REG-004`): "fully validated out of the box" is an
Essentials-tier feature. On the free tier you carry tool validation yourself
(`STD-013`). Acceptable while building on synthetic data; a decision point before
clinical supply.

**Prerequisite:** Jira. This is the real cost of the choice — adopting Jira as the
regulated work-item tracker.

> **[AMENDED v1.1] Capacity check.** The free tier caps configuration items at 150.
> The obligations, standards, findings and tasks in this document alone total 119 IDs
> before a single requirement, risk, software item specification or test case is
> written. Not all posture IDs become Ketryx configuration items — most live in R30 —
> but the tier ceiling is closer than it looks and should be modelled before
> `TASK-REG-006`, not discovered during it. Added to `Q-REG-006`.

### 6.2 Configuration approach

Two modes exist: use the Ketryx Jira schema, or connect to an existing Jira project
in observe-only mode with issue mapping. **Start from the Ketryx schema**
(`KTX-001`). You have no legacy Jira to preserve, and the predefined work type
schemes encode the item model correctly. Copy a Ketryx scheme and tweak rather than
building custom.

### 6.3 Item type mapping for Mākoha

| ID | Ketryx item | Mākoha content |
|---|---|---|
| `KTX-002` | Requirement | Product requirements per surface; Essential Principles as parent requirements |
| `KTX-003` | Risk | ISO 14971 risk file; ML-specific risks per BS/AAMI 34971 (`STD-006`) |
| `KTX-004` | Software Item Specification | Architecture units — differential engine, registry chain, corruption engine, evaluation firewall |
| `KTX-005` | Test Case | Evaluation corpus cases; extractable from Git via `@tests:ID` / `@implements:ID` annotations |
| `KTX-006` | Anomaly | Defects; vulnerability findings |
| `KTX-007` | Threat / Asset / Threat Source / Threat Surface / Trust Boundary | STRIDE threat model — custom item types, requires Jira admin setup |

Notes on specific fields:

- **`Relevant standards`** on Requirement items is your hook for tagging Essential
  Principles and standards clauses directly onto requirements (`KTX-008`). Use it
  consistently from day one; it is what makes the EP coverage argument generatable
  rather than reconstructed.
- **`Introduced in version` / `Obsolete in version`** make items long-lived
  (`KTX-009`). Needed for anything that persists across releases — set these up
  before you have volume.
- **Traceability matrix** is configurable to your desired V-model and enforces
  configured checks before release (`KTX-010`). Configure only checks that genuinely
  must be complete pre-release, or you will fight it.
- **Risk module strict modes** enforce predefined harms and severities (`KTX-011`).
  Turn strict mode on early — retrofitting a risk taxonomy over an existing risk file
  is painful.

> **[AMENDED v1.1] J-3 separation.** If the GPP channel proceeds (DEC-06), it is a
> distinct build artifact and a distinct device. It therefore needs its own Ketryx
> project, not a variant within the classified project — sharing a project would put
> structurally-absent capabilities into the same traceability graph as the artifact
> that must not contain them. Three projects is exactly the free-tier ceiling
> (classified, GPP, and nothing spare). Note in `Q-REG-006`.

### 6.4 Threat modelling

Ketryx supports STRIDE-based threat modelling referencing AAMI TIR57, with custom
item types. This maps directly onto the TGA cyber security expectations. Requires
Jira administrator configuration of the five custom item types with the long-lived
fields. Not a day-one task, but it is the answer to the cyber security portion of the
Essential Principles, so plan for it.

### 6.5 SOUP and SBOM

Ketryx's supply chain management module is where Baseten, the model, AWS services and
every dependency get inventoried with version and vulnerability tracking
(`KTX-012`). This is the single strongest reason to choose Ketryx over a
document-oriented eQMS: it generates the SBOM from the repo rather than asking you to
maintain one. Discharges `OBL-004`.

> **[AMENDED v1.1]** `OBL-013` extends this: third-party AI providers reachable from
> public surfaces are inventoried here too, even when they sit outside the build's
> dependency graph, because the obligation attaches to the processing arrangement.

### 6.6 Ecosystem boundary

Ketryx becomes the system of record for **regulated work items and design controls
only**. It does not displace:

- The corpus and its precedence law — which remains the governing architecture
- The Build Ecosystem v2.0 Implementer Contract and Observer adjudication protocol
- The firewalled evaluation corpus — Test Case items reference corpus cases by ID;
  **corpus content does not enter Ketryx**
- The differential library and its validator — clinical content, firewall-partitioned
- **[NEW v1.1]** R30, which remains the register home for every ID in this document.
  Ketryx holds design controls; R30 holds regulatory posture. They join by reference

Mapping between ecosystem IDs and Ketryx items is by reference, not by copy.

### 6.7 Vendor positions from the pre-demo correspondence **[NEW v1.2]**

The following are Ketryx's written answers of 1 September 2026 to the seven questions
put before the demo. They are recorded as **[vendor-stated]** and none is relied upon
until confirmed in writing against the contract or the product documentation.

| ID | Position | Consequence for the plan | Status |
|---|---|---|---|
| `KTX-013` | **System of record.** Ketryx does not assume it is the QMS; it is a lifecycle-management and design-controls system operating *under* an external QMS. Two clean configurations: (a) policies and SOPs held in Ketryx document management, or (b) QMS documents held elsewhere with plans referencing them. Vendor recommends (a) for a greenfield team. | Confirms §6.6's boundary. Decision between (a) and (b) is `Q-REG-006` scope. If (a), the ISO 13485 document-control procedure must name Ketryx as the controlled repository and `STD-013` tool validation extends to document control | OPEN — written confirmation pending |
| `KTX-014` | **Human release, evidenced.** Only a human can apply a 21 CFR Part 11 electronic signature; the AI has no approve/sign capability; the audit trail is append-only for every actor including the AI; all AI traffic runs through zero-data-retention endpoints; the AI agents are themselves validated as software with revalidation on model/prompt change. | This is the mechanism for `OBL-015`. Verification, not acceptance: obtain the validation package section covering signatures and audit trail, and run one intended-use test in which an AI-drafted item is shown unable to reach a controlled state without a named human signature | OPEN |
| `KTX-001` note | **Greenfield start.** Vendor recommends the Ketryx Jira schema with enforcement on from day one rather than observe-only mode; mechanical setup "measured in days"; first controlled release document "inside the first few weeks" for a small git-native team. | Consistent with `KTX-001`. Elapsed time is authoring-bound, not platform-bound — plan `TASK-REG-006..008` accordingly | Confirmed in principle |
| `KTX-012` note | **AI dependencies as SOUP.** Scanned dependencies come from repo manifests or CycloneDX/SPDX SBOMs, checked against GitHub Security Advisory (default) or NVD (opt-in). A hosted model-serving vendor with pinned weights has no CVE feed; the mechanism is a **manual dependency** item carrying the IEC 62304 SOUP metadata (manufacturer, version, licence, level of support, end-of-life, intended use, security and reliability impact with justification), entering the same approval workflow, with accepted versions declared explicitly and vulnerability/version-change information maintained by Arepo from the vendor's disclosures. | Discharges the mechanism half of `OBL-004` for Baseten/Bedrock and the model. The monitoring half is an SOP: who reads the vendor's version announcements, how often, and what a version change triggers (re-approval + `REG-FIND-011` pre-deployment assessment). Dependency risk assessments are **not** shared across projects — correct for the device/non-device split | Confirmed in principle |
| `Q-REG-006` note | **Free-tier metering.** Requirements, software item specifications, risks, test cases and anomalies each count as configuration items. If "dependencies as items" is enabled, **every SBOM entry counts**, and transitive dependencies multiply the count quickly. Vendor advice for a capped tier: scope dependency items to direct dependencies only. Precise metering rules to be confirmed in writing. | Feeds the ceiling model that `TASK-REG-006` must build first. With three projects (classified, GPP-or-GOV, spine components) the 150-item ceiling is the binding constraint, not the 3-project cap | OPEN — metering rules pending |
| `ASSUME-REG-006` note | **Validation package.** Vendor validates continuously (each version built inside an already-validated version); each major/minor release produces a customer-shareable, version-controlled, independently reviewed validation package. Vendor characterises the customer burden as "receiving and filing our package plus intended-use testing your SOPs require", consistent with FDA Computer Software Assurance thinking. | Does not change `WATCH-REG-004`: the package is described as available on upgrade; free-tier availability is unconfirmed. `STD-013` burden on the free tier remains Arepo's | OPEN |
| `KTX-004` note | **System of systems.** Regulated device and adjacent non-device product as separate projects, independently versioned and releasable, with shared spine components in their own component projects. Cross-project references have two levels: *Referenceable* (linkable, does not enter the referencing project's traceability matrix) and *Incorporated* (formally in scope, matrix and coverage checks). | This is the mechanism that keeps the Governance Layer (`REG-FIND-013`) and the classified device from cross-contaminating traceability graphs. Rule: spine items are *Incorporated* into the device project only where the device actually depends on them; the Governance Layer never *Incorporates* any inference-plane item | Confirmed in principle |
| `Q-REG-001`-adjacent | **Jurisdiction mapping.** Vendor states templates and traceability views are customer-authored (Word/Excel templates over a query language) and that an Essential Principles checklist template is configuration, not a product limitation. Vendor did **not** cite any customer who has taken a Ketryx-generated file through TGA conformity assessment or a Medsafe technical-file request. | The author-once/project-per-regulator model is technically supported. The absence of an Australian precedent is recorded as a risk, not a blocker: the EP checklist template is Arepo's to build (`TASK-REG-008`, `KTX-008`) and to have counsel review before `GATE-004` | Recorded; no precedent evidenced |

---

## §7 Sequenced plan

### Phase 0 — Decide (weeks 1–4). Blocking.

| ID | Task | Gate |
|---|---|---|
| `TASK-REG-001` | Write the intended purpose statement. One document, one claim. Everything downstream depends on it. Include the three surfaces explicitly and what each does. | `GATE-000` |
| `TASK-REG-002` | Engage Australian regulatory counsel for a written classification opinion: medical device status, classification rule and class, exemption eligibility (expected: not eligible), conformity assessment route. **[AMENDED v1.1]** Scope extended to the J-3 legal flags (`Q-REG-009`) and the patient-surface question (`ASSUME-REG-003`) in the same engagement — three separate engagements for one counsel relationship wastes the longest lead time in the programme. | `GATE-000` |
| `TASK-REG-003` | Reconcile public positioning. The site currently markets AI capability. Under an inclusion path this is fine and stops being a liability — but the claims must match the intended purpose statement exactly, because advertising requirements for therapeutic goods apply to exempt and included devices alike (`OBL-003`). **[AMENDED v1.1]** Output is a versioned claims inventory (`OBL-014`), not a one-off edit. | `GATE-000` |
| `TASK-REG-004` | Decide the patient surface. Separate product, non-decision-support, or in-scope for the same submission. Each has different consequences. | `GATE-000` |
| `TASK-REG-021` **[NEW v1.1]** | Triage the live demo surface: inventory the third-party AI provider as a supplier (`OBL-013`), confirm the disclosure is accurate, and decide whether the conversational surface remains public before the intended-purpose statement exists. Do not defer behind `TASK-REG-001` — the surface is live now. | `GATE-000` |
| `TASK-REG-022` **[NEW v1.1]** | Decide the jurisdiction sequence (`Q-REG-008`). The north star names low-resource settings; the posture is Australia-only; J-3's jurisdiction map already spans TGA, FDA and EU MDR. An unstated sequence will be set by accident. **[AMENDED v1.2]** Working sequence as stated to Ketryx on 1 September 2026: New Zealand first (notification), Australia second (conformity assessment + ARTG), FDA and EU MDR later. Recorded as the working assumption; DEC on `Q-REG-008` still required. | `GATE-000` |
| `TASK-REG-023` **[NEW v1.2]** | Governance Layer classification. Put the non-device question to counsel inside the single `TASK-REG-002` engagement (`ASSUME-REG-009`, `Q-REG-010`): does software that analyses documented clinical decisions for organisational conformance, with no clinical write path and no patient-specific output, meet s41BD — and specifically, is it an *accessory* to Mākoha, and is "analysing for a medical purpose" engaged. Attach MAK-GOV §2 and the Governance Layer intended purpose statement (`T-G01`). Homes the MAK-GOV §5 forward reference. | `GATE-000` |

**`GATE-000`:** counsel opinion in hand; `ASSUME-REG-001`, `ASSUME-REG-002` and
`ASSUME-REG-003` ATTESTED or REFUTED. Do not configure tooling before this.
**[AMENDED v1.2]** `ASSUME-REG-009` is asked in the same engagement but does **not**
gate `GATE-000`: it gates MAK-GOV `GATE-G0` / REG-SPRINT `SG-V1-0`. A refusal on the
non-device question must not stall the classified track.

> **[AMENDED v1.1] Interim rule pending `GATE-000`.** Patient-face work beyond the
> J-3-safe subset — intake, consent, logistics — is **Blocked**, not merely undecided
> (conflict C-06 → DEC-07). This is stronger than v1.0's framing and should be
> enforced in the phase plans, not just recorded here.

### Phase 1 — Foundation (weeks 4–12)

| ID | Task | Gate |
|---|---|---|
| `TASK-REG-005` | Adopt Jira. Ketryx free tier. One project, synthetic scope. | `GATE-001` |
| `TASK-REG-006` | Configure from the Ketryx schema (`KTX-001`). Risk module strict mode on (`KTX-011`). Traceability V-model configured minimally (`KTX-010`). **[AMENDED v1.1]** Model the configuration-item ceiling first (§6.1). | `GATE-001` |
| `TASK-REG-007` | Stand up the ISO 14971 risk file. This is the spine everything else hangs from — before requirements, before design controls. | `GATE-001` |
| `TASK-REG-008` | Requirements from the intended purpose statement, tagged with `Relevant standards` against Essential Principles (`KTX-008`). | `GATE-001` |
| `TASK-REG-009` | Migrate inference to Baseten Sydney, dedicated deployment, pinned weights. Get version-stability and change-notice commitments in the contract (`ASSUME-REG-004`). **[AMENDED v1.1] Blocked on DEC-03.** If DEC-03 rules for Bedrock, this task is superseded and the pinning requirement must be met another way — the requirement survives the substrate choice. | `GATE-001`; DEC-03 |
| `TASK-REG-024` **[NEW v1.2 — recommendation]** | Decide the QMS certification route (`Q-REG-011`): (a) TGA conformity assessment of the QMS directly; (b) MDSAP audit by a recognised auditing organisation, accepted by TGA as evidence and simultaneously by FDA (in lieu of routine inspection), Health Canada (mandatory), ANVISA and MHLW; (c) EU notified-body ISO 13485 certification. For the stated NZ → AU → FDA → EU sequence, (b) is the only option that is author-once across three of the four regulators. Decide before the QMS is audited by anyone, because the audit-scope documents differ. Output: a decision row in MET-2 and the certification body engaged. | `GATE-001` |

**`GATE-001`:** risk file exists, requirements traced, model version pinned **by
whichever substrate DEC-03 selects**. **[AMENDED v1.2]** QMS certification route
decided (`TASK-REG-024`) — not yet certified, decided.

### Phase 2 — Controls (months 3–6)

| ID | Task | Gate |
|---|---|---|
| `TASK-REG-010` | Split the Amplify path: synthetic/demo continues push-to-deploy; regulated releases go through a gated pipeline with approval landing as a CI artifact. **[AMENDED v1.1]** Per `REG-FIND-011`, the gate must be pre-deployment, and functional-update assessment happens inside it. | `GATE-002` |
| `TASK-REG-011` | SBOM generation in CI, flowing into Ketryx supply chain management (`KTX-012`, `OBL-004`). | `GATE-002` |
| `TASK-REG-012` | Vulnerability handling and disclosure processes (`STD-009`), with CVSS scoring and CAPA linkage (`OBL-008`). | `GATE-002` |
| `TASK-REG-013` | Supplier assessments — Baseten or Bedrock per DEC-03, AWS, and any third-party AI provider on a public surface (`OBL-005`, `OBL-006`, `OBL-013`). | `GATE-002` |
| `TASK-REG-014` | IEC 62366-1 use-related risk analysis (`STD-004`). Three surfaces, three analyses. The patient surface is hardest; do it last but do not skip it. | `GATE-002` |

**`GATE-002`:** controls operating. **This is the line before any identifiable
clinical data touches any environment.** Enforces `REG-KEEP-004`.
**[AMENDED v1.1]** Passing `GATE-002` is what makes clinical data collection lawful;
it is not itself evidence that the device works. That is `GATE-003`.

### Phase 3 — Evidence (months 6–18)

| ID | Task | Gate |
|---|---|---|
| `TASK-REG-015` | Clinical evidence and validation — the Lumos linkage pathway. Longest lead item in the programme; started in parallel from Phase 1, not sequentially. **[AMENDED v1.1]** Now load-bearing rather than merely long: per `REG-FIND-010`, synthetic evidence does not reduce this burden. Ethics and custodian engagement (`Q-REG-007`) begins in Phase 0, not Phase 3. | `GATE-003` |
| `TASK-REG-016` | Independent penetration testing, by a party outside the development team (`OBL-007`). | `GATE-003` |
| `TASK-REG-017` | Post-market surveillance procedures, adverse event reporting readiness (`OBL-002`). | `GATE-003` |
| `TASK-REG-018` | Ketryx tier upgrade for validated-out-of-the-box status and post-market surveillance features (`WATCH-REG-004`, `STD-013`). | `GATE-003` |

**`GATE-003`:** clinical evidence sufficient, security testing complete, post-market
processes operating.

### Phase 4 — Submission

| ID | Task | Gate |
|---|---|---|
| `TASK-REG-019` | Conformity assessment application. Route per counsel opinion (`Q-REG-005`). | `GATE-004` |
| `TASK-REG-020` | ARTG inclusion. | `GATE-004` |

**`GATE-004`:** ARTG inclusion granted. First lawful clinical supply.

> **[NEW v1.1] J-3 phasing.** The GPP channel does not run through `GATE-003` or
> `GATE-004`, because it does not seek ARTG inclusion. It runs through DEC-06
> ratification, `ASSUME-REG-008`, its own `OBL-012` notification, and Essential
> Principles compliance — then supplies. Its phase plan is shorter and is owned by
> MAK-J3, not by this document. What this document owns is the constraint that J-3
> supply does not relieve any classified-track obligation and does not constitute
> evidence for classified-track claims.

---

## §8 Assumptions register

No `ASSUME-REG-*` may be closed by internal reasoning. Each requires written
external attestation.

| ID | Assumption | Attesting party | Blocks | Status |
|---|---|---|---|---|
| `ASSUME-REG-001` | Mākoha's device classification and applicable classification rule | AU regulatory counsel | `GATE-000` | OPEN |
| `ASSUME-REG-002` | CDSS exemption is unavailable to Mākoha (`REG-FIND-001` confirmed) | AU regulatory counsel | `GATE-000` | OPEN |
| `ASSUME-REG-003` | Patient surface treatment — separate product, non-decision-support, or in-scope. **Interim rule: work beyond the J-3-safe subset is Blocked** (DEC-07) | Counsel + product | `GATE-000` | OPEN |
| `ASSUME-REG-004` | Baseten Sydney region on dedicated deployment, with version-stability and change-notice terms | Baseten | `GATE-001` | OPEN — conditional on DEC-03 |
| `ASSUME-REG-005` | Conformity assessment route (TGA vs notified body) | AU regulatory counsel | `GATE-004` | OPEN |
| `ASSUME-REG-006` | Ketryx tier and validation package timing | Ketryx | `GATE-003` | OPEN |
| `ASSUME-REG-007` | Lumos linkage ethics and custodian requirements | Data custodian | `GATE-003` | OPEN — **[AMENDED v1.1]** engagement starts Phase 0 given `REG-FIND-010` |
| `ASSUME-REG-008` **[NEW v1.1]** | J-3 / GPP exempt-tier eligibility as specified, including resolution of its two outstanding legal flags | AU regulatory counsel | DEC-06; `FORK-REG-001` | OPEN |
| `ASSUME-REG-009` **[NEW v1.2]** | The Governance Layer (MAK-GOV) is **not a medical device** under s41BD and is not an accessory to Mākoha — organisational-conformance analysis with no clinical write path and no patient-specific recommendation (`REG-FIND-013`). Homes the R30.1 row of the same ID | AU regulatory counsel | MAK-GOV `GATE-G0`; REG-SPRINT `SG-V1-0` (does **not** block `GATE-000`) | OPEN |

---

## §9 Open questions requiring external input

| ID | Question | Who | Blocking |
|---|---|---|---|
| `Q-REG-001` | Device classification and rule | AU regulatory counsel | Phase 1 |
| `Q-REG-002` | Exemption eligibility — written opinion | AU regulatory counsel | Phase 1 |
| `Q-REG-003` | Patient surface treatment | Counsel + product | Phase 1 |
| `Q-REG-004` | Baseten: Sydney region, version-stability and change-notice terms | Baseten sales | Phase 1, conditional on DEC-03 |
| `Q-REG-005` | Conformity assessment route (TGA vs notified body) | Counsel | Phase 3 |
| `Q-REG-006` | Ketryx tier and validation package timing; **[AMENDED v1.1]** configuration-item ceiling modelling; whether a separate J-3 project fits the free tier | Ketryx | Phase 1 (ceiling), Phase 3 (tier) |
| `Q-REG-007` | Lumos linkage — ethics and custodian requirements | Data custodian | Phase 0 (parallel) |
| `Q-REG-008` **[NEW v1.1]** | Jurisdiction sequence: Australia-first is assumed but never decided. What is the intended order across TGA, FDA and the low-resource settings the north star names, and does J-3 lead in any of them? | Counsel + product + programme | Phase 0 |
| `Q-REG-009` **[NEW v1.1]** | J-3's two outstanding legal flags — the boundary questions the addendum deliberately declines to decide | AU regulatory counsel | DEC-06 |
| `Q-REG-010` **[NEW v1.2]** | Governance Layer non-device status: s41BD device definition, the accessory question, and whether "analysing for a medical purpose" is engaged by organisational-conformance analysis of clinical records (`ASSUME-REG-009`, `TASK-REG-023`). Homes the R30.1 row of the same ID | AU regulatory counsel | MAK-GOV `GATE-G0` |
| `Q-REG-011` **[NEW v1.2 — recommendation]** | QMS certification route: TGA direct vs MDSAP vs EU notified body (`TASK-REG-024`). Sub-questions: which MDSAP auditing organisations operate in Australia/NZ; whether TGA accepts an MDSAP certificate as complete QMS evidence for a Class IIa/IIb SaMD conformity assessment or requires supplementary review; cost and lead time versus TGA direct | AU regulatory counsel + QMS consultant | Phase 1 |

---

## §10 Watch items

Non-closing. Review cadence stated per item. Received signals are logged additively in
MAK-ANT Part 4 under AN-6; this table names what is watched, not what has arrived.

| ID | Item | Cadence |
|---|---|---|
| `WATCH-REG-001` | TGA has consulted on amending the CDSS exemption, including introducing a legislative definition of CDSS in the Regulations and clarifying the transparency conditions. Outcome may shift the boundary in either direction — **and would bear directly on J-3's viability**, not only on the classified track. | Quarterly |
| `WATCH-REG-002` | TGA guidance on AI-enabled medical device software, applying from 5 February 2026. **[AMENDED v1.1]** Partially discharged: signal S-2 logged, yielding `REG-FIND-010` and `REG-FIND-011`. The remaining duty — read it against the intended purpose statement — stays open pending `TASK-REG-001`. | Once against intended purpose, then annually |
| `WATCH-REG-003` | The exemption guidance was fully rewritten on 7 October 2025 — anything written before that date about the CDSS exemption, including consultancy commentary, may describe the previous position. | Standing caution |
| `WATCH-REG-004` | Ketryx tier: validated-out-of-the-box is Essentials-tier. Free-tier validation burden is yours (`STD-013`). | At `GATE-002` |
| `WATCH-REG-005` | Standards revision — confirm current version of each `STD-*` before citing in submission. | Annually |
| `WATCH-REG-006` **[NEW v1.1]** | US instruments: FDA revised CDS final guidance (6 January 2026) and the FDA predetermined change control plan framework. No bearing on TGA findings; relevant to `Q-REG-008` jurisdiction sequencing and to J-3's jurisdiction map. PCCP is a US-only pre-authorised change-control instrument with no TGA equivalent — do not assume it transfers. | Semi-annually |
| `WATCH-REG-007` **[NEW v1.1]** | EU MDR 2017/745 Rule 11 — **no equivalent exemption carve-out exists**. A J-3-style exempt-tier artifact has no European analogue and would classify. Material to any European ambition and to the low-resource jurisdictions that follow CE marking. **[AMENDED v1.2]** The European position is now carried in full in REG-EU v1.0; this row remains as the Australian-side trigger only. | Annually, and before any EU commitment |
| `WATCH-REG-008` **[NEW v1.2]** | Standards revision, made specific: (a) **IEC 62304 Edition 2** — in development for several years; if published before submission, decide whether to claim Ed.1+A1 or Ed.2 and record the decision; (b) **ISO 13485** — under systematic review; (c) **ISO 14971 / ISO/TR 24971** amendment cycle; (d) **TGA standards matrix** (`SRC-REG-002`/`008`) — TGA updates it periodically and the "relevant to every EP" status of IEC 82304-1 (`REG-FIND-008`) should be re-read each time; (e) **BS/AAMI 34971** — possible progression to an ISO/IEC document. Editions pinned in §4.3 are re-confirmed against this row before any submission. | Annually; and at `GATE-004` |

---

## §11 Sources

| ID | Source | Currency |
|---|---|---|
| `SRC-REG-001` | TGA — Understanding clinical decision support software (guidance): exemption criteria, worked examples, transparency test | Last updated 7 October 2025 |
| `SRC-REG-002` | TGA — Standards for software-based medical devices | Last updated 5 February 2026 |
| `SRC-REG-003` | TGA — Complying with medical device cyber security requirements: Essential Principles mapping table, standards matrix | Last updated 2 October 2025 |
| `SRC-REG-004` | TGA — Guidance on Therapeutic Goods (Conformity Assessment Standard for Quality Management Systems) Order 2019 | Version 1.0, June 2019 |
| `SRC-REG-005` | Therapeutic Goods (Medical Devices) Regulations 2002 — Schedule 4 Part 2 (exemption); Schedule 1 (Essential Principles) | Current |
| `SRC-REG-006` | Therapeutic Goods Act 1989 — s41BD (device definition), s41FN (ARTG conditions) | Current |
| `SRC-REG-007` | Ketryx documentation — Jira integration, risk management (MAN-08), test management (MAN-06), threat modelling, advanced settings, WI-01 Requirement; Ketryx pricing | Accessed August 2026 |
| `SRC-REG-008` | TGA cyber security guidance Table 2 — standards-to-Essential-Principles matrix (source for `REG-FIND-008`) | Last updated 2 October 2025 |
| `SRC-REG-009` | Baseten deployment, region and compliance documentation | Accessed August 2026 |
| `SRC-REG-010` | OpenRegulatory — eQMS comparison and free ISO 13485 / IEC 62304 templates | Independent; updated March 2026 |
| `SRC-REG-011` **[NEW v1.1]** | MAK-J3 v0.9-proposed, Addendum J-3 Guideline-Prompt Profile — exemption criteria mapped to enforcement families, capability matrix, tier-promotion protocol | 29 August 2026 |
| `SRC-REG-012` **[NEW v1.1]** | MAK-ANT v1.0 Part 4 signal S-2 — TGA AI-enabled medical device software guidance content, via practitioner analyses of 22 April 2026 | Logged 1 September 2026. **Secondary source — primary guidance not yet read directly. `REG-FIND-010` and `REG-FIND-011` carry lower confidence than `001`–`008` until the primary is read.** |
| `SRC-REG-013` **[NEW v1.1]** | MAK-FFC v1.1 — XC-1 classification honesty, XC-2 profile boundary, XC-3 low-resource obligation | 29 August 2026 |
| `SRC-REG-014` **[NEW v1.1]** | MET-2 conflict and decision register (C-01..C-12, DEC-01..DEC-12) | 1 September 2026 |
| `SRC-REG-015` **[NEW v1.2]** | IMDRF SaMD Working Group documents: N10 (key definitions, 2013), N12 (risk categorisation framework, 2014), N23 (QMS, 2015), N41 (clinical evaluation, 2017) | Published; stable |
| `SRC-REG-016` **[NEW v1.2]** | IMDRF cybersecurity and ML documents: N60 (principles and practices for medical device cybersecurity, 2020), N70 (legacy devices, 2023), N73 (SBOM, 2023), N88 (good machine learning practice, 2025) | Published; **N88 currency to verify** |
| `SRC-REG-017` **[NEW v1.2]** | Ketryx written response to Arepo's pre-demo questions (Dror → Ken, 1 September 2026): system of record, free tier and validation, capacity metering, system-of-systems, AI SOUP mechanism, AI guardrails, greenfield path | 1 September 2026. **Vendor correspondence — vendor interest; every position requires written confirmation before reliance** |
| `SRC-REG-018` **[NEW v1.2]** | MAK-GOV v0.9-proposed, Addendum G — Governance Layer classification argument (§2), sprint plan (§4), integration ledger (§5) | 1 September 2026. Internal programme document |
| `SRC-REG-019` **[NEW v1.2]** | Standards-gap review, 2 September 2026 — comparison of the v1.1 `STD-*` stack against TGA conformity-assessment, FDA premarket and EU notified-body expectations for a CDSS SaMD | 2 September 2026. **Author's analysis; every row it produced is tagged [recommendation] and requires counsel/QMS-lead confirmation** |
| `SRC-REG-020` **[NEW v1.2]** | Survey-2 run (2026-09-02): CENSUS.md, BUILD_SPEC_QUEUE.md — BSQ-0001 DANGLING-REF on `REG-FIND-013` / `TASK-REG-023` | 2 September 2026. Internal |

**Source caution:** `SRC-REG-001` through `SRC-REG-006` and `SRC-REG-008` are primary.
`SRC-REG-007`, `SRC-REG-009` and `SRC-REG-017` are vendor documentation or
correspondence and carry vendor interest. `SRC-REG-010` is independent but commercially
adjacent. `SRC-REG-011`, `013`, `014`, `018` and `020` are internal programme documents
— authoritative for programme intent, not for external regulation. `SRC-REG-015` and
`016` are international framework documents, not Australian law; they carry
persuasive weight with the TGA because TGA guidance cites them. `SRC-REG-019` is the
author's own analysis. **`SRC-REG-012` is secondary and should be replaced by direct
reading of the primary guidance before `GATE-000`.**

---

## §12 ID census and self-audit

### 12.1 Census **[AMENDED v1.2]**

| Prefix | v1.1 count | v1.2 count | Range | Δ v1.1 → v1.2 |
|---|---|---|---|---|
| `REG-FIND` | 11 | 13 | 001–013 | +2 (`012`, `013`) |
| `REG-KEEP` | 4 | 4 | 001–004 | 0 |
| `ASSUME-REG` | 8 | 9 | 001–009 | +1 |
| `OBL` | 14 | 15 | 001–015 | +1 |
| `STD` | 13 | 26 | 001–026 | +13 |
| `FORK-REG` | 1 | 1 | 001 | 0 |
| `GATE` | 5 | 5 | 000–004 | 0 (two amended) |
| `TASK-REG` | 22 | 24 | 001–024 | +2 |
| `KTX` | 12 | 14 | 001–014 | +2 |
| `WATCH-REG` | 7 | 8 | 001–008 | +1 |
| `Q-REG` | 9 | 11 | 001–011 | +2 |
| `SRC-REG` | 14 | 20 | 001–020 | +6 |
| **Total** | **120** | **150** | | **+30** |

Retired: none. No ID reused. The v1.0 → v1.1 census is preserved in the v1.1 file.

### 12.2 Self-audit checks **[AMENDED v1.2]**

| # | Check | Result |
|---|---|---|
| 1 | All IDs conform to the pattern in §0.5 | PASS |
| 2 | Every ID defined exactly once in a table | PASS by the §0.5 reading. **Mechanical caveat [NEW v1.2]:** a strict row-start parser run over this file (validate_reg.py, 2026-09-02) finds twelve v1.1-era IDs defined in prose or field-table shape rather than as a first-cell table row — `GATE-000..004` (bold prose), `FORK-REG-001` (field table), `KTX-001`, `KTX-008..012` (prose/bullets) — and one v1.1-era double definition, `ASSUME-REG-004` (§5.1 and §8). Carried unchanged under append-only law and recorded here so the next revision can normalise them; every v1.2-minted ID is first-cell-table defined. §6.7 rows labelled "note" against `KTX-001`, `KTX-004`, `KTX-012`, `Q-REG-006`, `ASSUME-REG-006` are annotations, not definitions |
| 3 | Every `TASK-REG-*` names its gate | PASS (24/24) |
| 4 | Every `GATE-*` names predecessors; all predecessors exist | PASS (5/5) |
| 5 | Every `ASSUME-REG-*` names attesting party and blocking gate | PASS (9/9) |
| 6 | Every `REG-FIND-*` names at least one `SRC-REG-*` | PASS (13/13) |
| 7 | Status values drawn only from §0.4 | PASS |
| 8 | No `ATTESTED`/`REFUTED` item lacks an attestation date | PASS (vacuous — zero closed) |
| 9 | Frontmatter `id_prefixes` ↔ §0.3 ↔ §12.1, endpoints checked both ends | PASS (12/12 families; low end 001/000 and high end per §12.1 both verified) |
| 10 | Every status value maps to an R30 state under §0.7 | PASS |
| 11 **[NEW v1.2]** | Every `STD-*` row carries an edition | PASS (26/26) |
| 12 **[NEW v1.2]** | Every row originating from `SRC-REG-019` carries [recommendation] and a confidence tag | PASS (`STD-014..026`, `OBL-015`, `TASK-REG-024`, `Q-REG-011`) |
| 13 **[NEW v1.2]** | MAK-GOV §5 forward references resolve (`REG-FIND-013`, `TASK-REG-023`, `ASSUME-REG-009`, `Q-REG-010`) | PASS — BSQ-0001 closes on adoption of this file |
| 14 **[NEW v1.2]** | Jurisdiction declared in frontmatter, title and §0.9; no "see companion" used for any Australian-actionable content | PASS |

### 12.3 Known gaps

- `Q-REG-*` and `ASSUME-REG-*` overlap by design: the question is the mechanism,
  the assumption is the state. They are deliberately not merged, so that a question
  can be answered without the assumption automatically closing.
- No `REG-FIND-*` currently holds `SUPERSEDED` or `REFUTED`. On any counsel finding
  that contradicts `REG-FIND-001`, mark it `REFUTED` with a date; do not edit it in
  place.
- Check 8 passes vacuously and will become meaningful only after `GATE-000`.
- **[NEW v1.1]** `REG-FIND-010` and `REG-FIND-011` rest on a secondary source
  (`SRC-REG-012`). They are actionable — both point the same direction as the primary
  guidance's known posture — but they should be re-anchored to the primary before
  `GATE-000`, and their confidence stated whenever cited.
- **[NEW v1.1]** This document has no owner field. R30 names `cdss-governance` as
  register owner, but the *regulatory owner* who runs the AN-6 watch cadence and
  commissions folds is `[NEEDS DEFINITION]`. This is the same gap the ecosystem
  records as G-09; naming it is a prerequisite for the watch program actually running.

### 12.4 Fold checklist for MAK-ANT **[NEW v1.1]**

Per AN-5, a posture revision re-runs the carrier map before the fold completes. This
revision adds ID families and rows requiring new or amended carriers:

| New/amended ID | Carrier needed |
|---|---|
| `REG-FIND-009` (J-3 as separate artifact) | MAK-J3; MAK-FFC XC-2; `FORK-REG-001` row in the map |
| `REG-FIND-010` (synthetic ≠ validation) | All phase plans; MAK-CEC RG-3; AN-7 already carries the consequence |
| `REG-FIND-011` (pre-deployment update control) | MAK-CEC; GPP-3/MS-4 alignment already noted in signal S-2 |
| `OBL-013` (third-party AI on public surfaces) | MAK-ABC AX-3 obligations register |
| `OBL-014` (versioned claims inventory) | AN-9 — already the duty; needs the artifact named |
| `STD-013` (tool validation) | Legs volume bindings |
| `TASK-REG-021`, `TASK-REG-022` | Phase 0 plans; C-10 and `Q-REG-008` owners |
| `WATCH-REG-006`, `WATCH-REG-007` | This wrapper; AN-11 jurisdiction map |
| `ASSUME-REG-008`, `Q-REG-009` | MAK-J3; DEC-06 |

Also required at fold: re-run the range-endpoint check per DEF-REG-001, and update the
R30 seed to the v1.1 counts.

### 12.5 Fold checklist addendum for v1.2 **[NEW v1.2]**

FOLD-1 W1 now folds **v1.2**, not v1.1 (the v1.1 fold had not executed at the time
of this revision; the divergence window in EX-3 simply widens by one version and
closes on the same W5 check). Additional carriers:

| New/amended ID | Carrier needed |
|---|---|
| `REG-FIND-012` (standards are voluntary evidence routes) | MAK-ANT Part 3; SEC-1 (already faithful to `REG-FIND-006..008`, extend) |
| `REG-FIND-013`, `ASSUME-REG-009`, `Q-REG-010`, `TASK-REG-023` | MAK-GOV §5 row "REG-POSTURE v1.2" — now satisfied; MET-2.1 DEC-G rows; R30.2 |
| `STD-014..026` | Legs volume bindings; SEC-1 (cyber rows); DEPLOY-2 (TIR45 → CI acceptance); Primer J (42001/23894) |
| `OBL-015` (e-record / e-signature integrity) | MAK-ABC AX-4 gate bundles (signature evidence); SEC-1 audit spine |
| `KTX-013`, `KTX-014`, §6.7 notes | REG-SPRINT `V1-S1`/`TASK-REG-005..006`; `Q-REG-006` ceiling model |
| `TASK-REG-024`, `Q-REG-011` | EXEC-1 RUN-1 row; MET-2 decision table |
| `WATCH-REG-008` (standards revision, specific) | MAK-ANT AN-6 watch program |
| `SRC-REG-015..020` | MAK-ANT Part 4 signal log (S-7: Ketryx correspondence; S-8: gap review) |
| §0.9 replete-standalone rule; §13 companions | MAK-ANT AN-11 jurisdiction map; MANIFEST A-003 |

---

## §13 Companion jurisdiction documents **[NEW v1.2]**

This document is Australia. The programme's other jurisdictions are carried in
companion documents written to the same conventions (§0) and the same
replete-standalone rule (§0.9). Each carries the full standards stack with that
regulator's recognition status, and its own obligations, gates, tasks, assumptions,
questions, watch items and sources.

| Document | Jurisdiction | Regulator / instrument | Entry model | Working sequence position |
|---|---|---|---|---|
| **REG-NZ v1.1** | NEW ZEALAND | Medsafe; Medicines Act 1981; Medicines (Database of Medical Devices) Regulations 2003; WAND | Sponsor notification; technical file **held**, producible on request; no pre-market review | **First** (per `TASK-REG-022` working assumption) |
| **REG-POSTURE v1.2** (this document) | AUSTRALIA | TGA; Therapeutic Goods Act 1989; Regulations 2002 | Conformity assessment + ARTG inclusion before supply | **Second** |
| **REG-US v1.0** | UNITED STATES | FDA; FD&C Act; 21 CFR | Premarket submission (De Novo or 510(k) expected) + QMSR; Part 11 records | Later |
| **REG-EU v1.0** | EUROPEAN UNION | MDR 2017/745; notified body; EU AI Act 2024/1689 | CE marking via notified-body conformity assessment; Rule 11 | Later |

What is shared and built once: the intended purpose statement (`TASK-REG-001`), the
ISO 14971 risk file (`TASK-REG-007`), the IEC 62304 lifecycle records, the usability
file, the security risk file and SBOM, the clinical evidence, and the technical
documentation set. What differs per document: the legal test, the entry model, the
classification rule, the post-market duties, the labelling language and content, and
the sponsor/agent/representative arrangements. The Ketryx projection (§6) is
Australia-shaped here (Essential Principles checklist as the parent requirement
set); each companion states its own projection (GSPR checklist, FDA
software-documentation level, Medsafe technical-file index).

**Divergence rule:** the four documents are revised in the same cycle when the shared
stack changes. If one is revised alone, the wrapper (MAK-ANT) logs the divergence as a
signal and the next revision of the others carries it. No document governs another.

---

*This document reflects publicly available guidance as at 2 September 2026 and is not
a substitute for regulatory advice. Classification and exemption eligibility must be
determined by qualified counsel before commercial commitment. Items tagged
[recommendation] originate from the author's gap review and require confirmation by
counsel and the quality lead before adoption.*
