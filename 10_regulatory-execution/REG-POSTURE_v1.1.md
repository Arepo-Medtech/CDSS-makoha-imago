---
doc_id: REG-POSTURE
title: Mākoha — Regulatory Posture and Ketryx Implementation Plan
version: 1.1
status: DRAFT
authority: ADVISORY_ONLY
entity: Arepo Medtech Pty Ltd
product: Mākoha
date_issued: 2026-09-01
guidance_currency_date: 2026-09-01
supersedes: REG-POSTURE v1.0 (2026-08-31)
review_basis: "Makoha Imago v1.1 repository (MANIFEST-IMAGO, 2026-09-01; 170 files)"
depends_on:
  - Addendum J-1 (deterministic runtime posture)
  - Addendum J-2 (ML runtime, SaMD classification posture)
  - Addendum J-3 / MAK-J3 v0.9-proposed (Guideline-Prompt Profile, exempt-tier reserve)
  - Build Ecosystem v2.0 (Implementer Contract, Observer adjudication)
  - MAK-FFC v1.1 (XC-1 classification honesty; XC-2 profile boundary; XC-3 low-resource)
wrapped_by: "MAK-ANT v1.0 (Antennae Corpus) — folds this document verbatim as Annex 1"
runtime_register: "R30 — Regulatory Posture Register (Proposed, DEC-02; owner cdss-governance)"
blocks:
  - GATE-000
id_prefixes: [REG-FIND, REG-KEEP, ASSUME-REG, OBL, STD, FORK-REG, GATE, TASK-REG, KTX, WATCH-REG, Q-REG, SRC-REG]
attestation_required: true
attestation_by: Australian regulatory counsel
---

# Mākoha — Regulatory Posture and Ketryx Implementation Plan

**Prepared for:** Arepo Medtech Pty Ltd
**Version:** 1.1 · 1 September 2026 · supersedes v1.0 (31 August 2026)
**Status:** Working document. Not regulatory advice. Requires counsel attestation before any commitment.

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

### 4.3 Standards stack

| ID | Standard | Role | Priority |
|---|---|---|---|
| `STD-001` | ISO 13485:2016 | QMS — deemed conformity under the 2019 Order | **1** |
| `STD-002` | IEC 62304 | Software lifecycle, SOUP, change control | **1** |
| `STD-003` | ISO 14971 | Risk management — foundational to everything | **1** |
| `STD-004` | IEC 62366-1 | Usability engineering — three surfaces, three analyses | **2** |
| `STD-005` | IEC 82304-1 | Health software product safety; maps to all relevant EPs | **2** |
| `STD-006` | BS/AAMI 34971 | ISO 14971 applied to ML — the AI risk hook | **2** |
| `STD-007` | ANSI/AAMI SW96 | Security risk management for manufacturers | 3 |
| `STD-008` | IEC 81001-5-1 | Security activities in the product lifecycle | 3 |
| `STD-009` | ISO/IEC 29147 / 30111 | Vulnerability disclosure and handling | 3 |
| `STD-010` | ISO 27799 | InfoSec management in health (27002-derived) | 3 |
| `STD-011` | IEC 80001 series | Risk management for IT networks with devices | 4 |
| `STD-012` | UL 2900-2-1 | Network-connectable healthcare product security | 4 |
| `STD-013` **[NEW v1.1]** | IEC 62304 §5.1.4 (software development tools) + ISO 13485 tool validation | Validation of tools in the authoring and release path — now three: the authoring surface, the Ketryx free tier (not validated out of the box), and the GPP release channel | **2** |

Also in scope and not covered by any of the above: Australian Privacy Principles,
the Notifiable Data Breach scheme, advertising requirements for therapeutic goods,
and adverse event reporting.

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

`OBL-007`, `OBL-009` and `OBL-014` are explicitly **outside the scope of any
compliance platform** and must be resourced separately.

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
| `TASK-REG-022` **[NEW v1.1]** | Decide the jurisdiction sequence (`Q-REG-008`). The north star names low-resource settings; the posture is Australia-only; J-3's jurisdiction map already spans TGA, FDA and EU MDR. An unstated sequence will be set by accident. | `GATE-000` |

**`GATE-000`:** counsel opinion in hand; `ASSUME-REG-001`, `ASSUME-REG-002` and
`ASSUME-REG-003` ATTESTED or REFUTED. Do not configure tooling before this.

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

**`GATE-001`:** risk file exists, requirements traced, model version pinned **by
whichever substrate DEC-03 selects**.

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
| `WATCH-REG-007` **[NEW v1.1]** | EU MDR 2017/745 Rule 11 — **no equivalent exemption carve-out exists**. A J-3-style exempt-tier artifact has no European analogue and would classify. Material to any European ambition and to the low-resource jurisdictions that follow CE marking. | Annually, and before any EU commitment |

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

**Source caution:** `SRC-REG-001` through `SRC-REG-006` and `SRC-REG-008` are primary.
`SRC-REG-007` and `SRC-REG-009` are vendor documentation and carry vendor interest.
`SRC-REG-010` is independent but commercially adjacent. `SRC-REG-011`, `013` and `014`
are internal programme documents — authoritative for programme intent, not for
external regulation. **`SRC-REG-012` is secondary and should be replaced by direct
reading of the primary guidance before `GATE-000`.**

---

## §12 ID census and self-audit

### 12.1 Census

| Prefix | Count | Range | Δ v1.0 |
|---|---|---|---|
| `REG-FIND` | 11 | 001–011 | +3 |
| `REG-KEEP` | 4 | 001–004 | 0 |
| `ASSUME-REG` | 8 | 001–008 | +1 |
| `OBL` | 14 | 001–014 | +2 |
| `STD` | 13 | 001–013 | +1 |
| `FORK-REG` | 1 | 001 | 0 (amended) |
| `GATE` | 5 | 000–004 | 0 |
| `TASK-REG` | 22 | 001–022 | +2 |
| `KTX` | 12 | 001–012 | 0 |
| `WATCH-REG` | 7 | 001–007 | +2 |
| `Q-REG` | 9 | 001–009 | +2 |
| `SRC-REG` | 14 | 001–014 | +4 |
| **Total** | **120** | | **+17** |

Retired: none. No ID reused.

### 12.2 Self-audit checks

| # | Check | Result |
|---|---|---|
| 1 | All IDs conform to the pattern in §0.5 | PASS |
| 2 | Every ID defined exactly once in a table | PASS |
| 3 | Every `TASK-REG-*` names its gate | PASS (22/22) |
| 4 | Every `GATE-*` names predecessors; all predecessors exist | PASS (5/5) |
| 5 | Every `ASSUME-REG-*` names attesting party and blocking gate | PASS (8/8) |
| 6 | Every `REG-FIND-*` names at least one `SRC-REG-*` | PASS (11/11) |
| 7 | Status values drawn only from §0.4 | PASS |
| 8 | No `ATTESTED`/`REFUTED` item lacks an attestation date | PASS (vacuous — zero closed) |
| 9 | Frontmatter `id_prefixes` ↔ §0.3 ↔ §12.1, endpoints checked both ends | PASS (12/12 families; `REG-KEEP` added this revision) |
| 10 | Every status value maps to an R30 state under §0.7 | PASS |

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

---

*This document reflects publicly available guidance as at 1 September 2026 and is not
a substitute for regulatory advice. Classification and exemption eligibility must be
determined by qualified counsel before commercial commitment.*
