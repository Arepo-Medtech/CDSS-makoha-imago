---
doc_id: MAK-ANT
title: "The Antennae Corpus"
version: "1.0"
date: "2026-09-01"
series: "Mākoha research series — volume 13 · regulatory sensing; folds REG-POSTURE v1.0 verbatim as Annex 1"
status: normative-draft (wrapper) + advisory (annex, per its own authority line)
normative_language: RFC-2119 (MUST / SHOULD / MAY)
req_prefixes: [AN]
req_count: 12
subordinate_to: "MAK-FFC v1.1 for architecture; the folded REG-POSTURE v1.0 governs regulatory content per its own §0 conventions"
folds_in:
  - "REG-POSTURE v1.0 (Mākoha — Regulatory Posture and Ketryx Implementation Plan, Arepo Medtech Pty Ltd, 2026-08-31) — folded VERBATIM as Annex 1; its IDs (REG-FIND, ASSUME-REG, OBL, STD, FORK-REG, GATE, TASK-REG, KTX, WATCH-REG, Q-REG, SRC-REG) resolve inside the annex"
changelog:
  - "v1.0 (2026-09-01): initial release — 12 AN requirements (the sensing duties); butterfly-to-posture carrier map; watch-program annotations (signals received since the annex's currency date); REG-POSTURE v1.0 folded verbatim as Annex 1."
companions:
  - "MAK-FFC v1.1 · MAK-LWC v1.1 · MAK-RWC v1.1 · MAK-CEC v1.1 · MAK-HDC v1.0 · MAK-TXC v1.0 · MAK-ABC v1.0 (the volumes this wrapper binds to the posture)"
  - "MAK-J3 v0.9-proposed (the exempt-tier reserve the posture re-weighs)"
artifact_url: "https://claude.ai/code/artifact/31281f0e-4a92-4f32-9718-d0af4fddd70f"
change_policy: "AN IDs are stable; the annex changes only by folding a new REG-POSTURE version, never by editing in place."
---

<!-- LLM USAGE CONTRACT (additive; not part of the source document)
1. AN-n blocks are NORMATIVE for the series' regulatory-sensing duties. The folded
   annex is ADVISORY per its own authority line (ADVISORY_ONLY): it cannot be cited
   as evidence for a DONE, and every material finding is carried as an ASSUME-REG-*
   requiring counsel attestation.
2. The annex is folded VERBATIM. If a standalone REG-POSTURE file is maintained in
   the document ecosystem, that file is canonical and this annex mirrors it;
   divergence is a validator error.
3. An LLM must never: mark an ASSUME-REG-* closed; resolve a Q-REG-*; treat a
   WATCH-REG signal as having changed the posture without a folded revision; or
   cite superseded framings (exempt J-1, Bedrock runtime) except through an update
   note.
4. Cite annex content by stable ID (e.g. "REG-FIND-004"), never by paraphrase alone.
5. MUST violations in generated designs/code/documents require an explicit DEVIATION
   notice naming the ID.
6. Appendix A's ID census (wrapper IDs only) is authoritative for validator checks.
END LLM USAGE CONTRACT -->

# The Antennae Corpus

The butterfly's regulatory sensing organ: the Mākoha Regulatory Posture and Ketryx Implementation Plan folded verbatim, wrapped in the series-integration layer — who carries which obligation, what the antennae are listening for, and the standing duties that keep the whole document set honest as the regulatory environment moves.

**Document metadata:** Wrapper corpus + verbatim annex · v1.0 · 1 Sep 2026 · thirteenth volume in the Mākoha research series · STATUS: normative wrapper over an advisory annex · REQ IDS: AN (12) · ANNEX: REG-POSTURE v1.0 (2026-08-31, Arepo Medtech Pty Ltd) · ANNEX AUTHORITY: ADVISORY_ONLY, counsel attestation required.

## Contents

1. [Part 0 — How to use this document](#part-0--how-to-use-this-document)
2. [Part 1 — Why antennae](#part-1--why-antennae)
3. [Part 2 — The sensing duties (AN)](#part-2--the-sensing-duties)
4. [Part 3 — The carrier map: posture IDs → butterfly volumes](#part-3--the-carrier-map)
5. [Part 4 — Signals received since the annex's currency date](#part-4--signals-received)
6. [Appendix A — ID census (wrapper)](#appendix-a--id-census-wrapper-additive)
7. [Appendix B — Self-audit checks](#appendix-b--self-audit-checks-additive)
8. [Annex 1 — REG-POSTURE v1.0, folded verbatim](#annex-1--reg-posture-v10-folded-verbatim)

## Thesis

> Antennae are not decoration; they are how the butterfly smells the wind before it commits its wings. The regulatory environment is Mākoha's wind: the posture document folded below found that the CDSS exemption is unavailable to a differential engine on the diagnostic function alone (REG-FIND-001), that determinism does not purchase transparency (REG-FIND-003), that the test is a glass box (REG-FIND-004) — and it converted those findings into a posture ("build to SaMD standard, test exemption honestly at a named gate, assume inclusion"), an obligations register, a standards stack, a relabelled fork, five gates, twenty tasks, and a watch list. What the posture cannot do for itself is stay bound to a living document set: eight other volumes now carry its consequences, its assumptions await attestation, and its watch items have already received signals. This wrapper is the binding — the sensing duties that keep every volume citing the same wind, and the map that says which segment of the butterfly carries which obligation.

## Part 0 — How to use this document

Two layers with two authorities. The **wrapper** (Parts 0–4, the AN requirements) is normative series law: how the Mākoha document set relates to its regulatory posture. The **annex** (REG-POSTURE v1.0, folded verbatim) is advisory per its own §0: assertions about external regulation carried as assumptions until counsel attests. The wrapper never edits the annex; a revised posture is folded as a new annex version, and the wrapper's maps update to match.

- **Citation.** Annex content is cited by stable ID (REG-FIND-004, OBL-003, GATE-002…), per the annex's own §0.2 convention. Wrapper duties are AN-n.
- **Precedence.** For regulatory content, the annex governs the series (subject to its advisory status); for architecture, MAK-FFC v1.1 and its subordinate corpora govern. Where the two meet, the flag-and-route rule (AN-2) applies.
- **Freshness.** The annex's guidance currency date is 2026-08-31. Part 4 records signals received after that date; none amends the annex — each is an input to the next folded revision.

## Part 1 — Why antennae

The series' earlier regulatory anchors were point readings: MAK-FFC XC-1 read the TGA's CDSS guidance as revised October 2025; MAK-J3 mapped the exemption criteria to a code-enforced scoped product; MAK-RWC Part 7 absorbed the posture's findings as update notes. The posture document consolidated all of it into one advisory instrument with stable IDs, an attestation discipline, and — critically — a *sensing apparatus*: watch items with cadences, questions with owners, assumptions with closure conditions. That apparatus is what makes the posture an antenna rather than a snapshot: it is built to notice change.

The wrapper's job is threefold. First, **binding**: eight volumes now carry posture consequences (the carrier map, Part 3) — the binding must be explicit so a posture revision propagates by checklist, not archaeology. Second, **discipline**: the series' own rules for regulatory content (flag-and-route on divergence, no silent superseded framings, assumptions never self-closed) were stated piecemeal in MAK-RWC MX-1 and the volumes' self-audit checks; the AN family states them once, series-wide. Third, **listening**: watch items only work if received signals are logged somewhere additive — Part 4 is that log, and AN-6 is the duty to keep it.

> The doctrine in one sentence: one posture, one citation surface, every assumption labelled, every signal logged, every volume bound by name.

## Part 2 — The sensing duties

### AN-1 (MUST)
**Statement:** The folded REG-POSTURE (Annex 1, at its stated version) is the series' single regulatory citation surface: every Mākoha document that makes a regulatory claim cites an annex ID or a Part 4 signal entry. Direct citation of external guidance without an annex or signal anchor is a conformance violation — the fix is to log the signal (AN-6) or fold a revision, not to bypass the antennae.
**Rationale trace:** annex §0.2 conventions; single-source-of-truth discipline; WATCH-REG-003 (pre-rewrite commentary hazard).

### AN-2 (MUST)
**Statement:** Flag-and-route on divergence (MAK-RWC MX-1, carried series-wide): no series document contradicts a REG-FIND without an explicit update note naming the finding, and reversal of a finding travels only through the annex's own route (ASSUME-REG closure by written counsel attestation). Silent contradiction anywhere in the document set is a validator error.
**Rationale trace:** MAK-RWC MX-1 (carried); annex §0.1 (advisory, attestation-gated).

### AN-3 (MUST)
**Statement:** Assumptions are never self-closed: ASSUME-REG-001..007 close only by the written external attestation the annex specifies, the closure record enters the ledger, and until closure every dependent statement carries its dependence. No LLM, no internal review, and no series document may mark one closed.
**Rationale trace:** annex attestation_required discipline; MAK-RWC LLM-contract rule 4; GATE-000 blocking structure.

### AN-4 (MUST)
**Statement:** Anchor currency is checked before commitment: any submission, supply decision, or external claim re-verifies the annex's regulatory anchors (guidance versions, standards editions per WATCH-REG-005, STD-001..012 currency) as of the decision date; the check and its outcome are ledgered.
**Rationale trace:** MAK-J3 LLM-contract rule 3, generalized; WATCH-REG-005; annex guidance_currency_date mechanics.

### AN-5 (MUST)
**Statement:** The carrier map (Part 3) is a maintained artifact: every annex obligation (OBL), standard (STD), task (TASK-REG), Ketryx element (KTX), and gate (GATE) names the series volume(s) and requirement(s) that carry it; unmapped annex IDs and orphaned carriers are validator errors. A posture revision re-runs the map before the fold completes.
**Rationale trace:** eight-volume propagation reality; MAK-ABC AX-3 (generated obligations register) as the runtime twin *(new)*.

### AN-6 (MUST)
**Statement:** The watch program runs: each WATCH-REG item is checked at its stated cadence by a named owner; received signals are logged additively in Part 4 with date, source, and assessed bearing (reinforces / no bearing / potential amendment — the last triggering a fold-revision proposal). New watch-worthy instruments are added as signal entries pending the next fold.
**Rationale trace:** annex §watch structure; Part 4 entries already logged; sensing-that-stays-alive doctrine.

### AN-7 (MUST)
**Statement:** Gates govern series phasing: no volume's phase plan schedules work that the annex's gate structure forbids at its position — GATE-000 blocks Phase 1 regulatory-dependent work; GATE-002 is the line before identifiable clinical data (REG-KEEP-004), with the Part 4 note that synthetic-only is a development posture and generally not validation evidence. Every volume's phasing table marks its gate dependencies.
**Rationale trace:** annex GATE-000..004; REG-KEEP-004; Part 4 signal S-2 (TGA synthetic-data caution).

### AN-8 (MUST)
**Statement:** Superseded framings are quarantined: "exempt J-1," Bedrock-runtime assumptions, and pre-October-2025 exemption commentary are cited only through update notes (MAK-RWC Part 7; this wrapper) that name the superseding ID (FORK-REG-001; TASK-REG-009; WATCH-REG-003). Series search-and-audit for unquarantined superseded framings is a release check on the document set.
**Rationale trace:** FORK-REG-001 relabel; WATCH-REG-003 standing caution; MAK-RWC update-note pattern.

### AN-9 (MUST)
**Statement:** The claims boundary is a conformance artifact: public positioning, marketing, and in-product copy match the intended-purpose statement exactly (TASK-REG-001/003; OBL advertising obligations), for exempt and included devices alike; the claims inventory is versioned and diffed against the intended-purpose statement per release.
**Rationale trace:** annex TASK-REG-003; MAK-J3 GPP-1 pattern at series scope; advertising obligations.

### AN-10 (SHOULD)
**Statement:** Counsel-interface packets stand ready: each Q-REG question carries a maintained evidence packet (the relevant volume extracts, carrier-map rows, and MAK-ABC AX-4 gate bundles) so the GATE-000 counsel engagement reads prepared material; packet freshness follows AN-4.
**Rationale trace:** annex Q-REG-001..007; TASK-REG-002; MAK-ABC AX-4.

### AN-11 (SHOULD)
**Statement:** The jurisdiction map (MAK-J3 GPP-15's artifact) is maintained under this wrapper's watch program: TGA, FDA (revised CDS guidance; PCCP as a US-only change-control instrument), EU MDR Rule 11, and per-country low-resource assessments — reviewed annually and before any new-market supply, with review records ledgered.
**Rationale trace:** MAK-J3 GPP-15 (carried under the wrapper); Part 4 signals S-1/S-3; XC-3/XC-4.

### AN-12 (MAY)
**Statement:** Regulatory what-if exercises may run against the document set (e.g. "the CDSS exemption consultation lands amendment X" per WATCH-REG-001): impact traced through the carrier map to affected requirements, results logged as preparedness notes — clearly labelled non-normative and never treated as predictions.
**Rationale trace:** WATCH-REG-001 consultation risk; carrier-map utility; scenario-planning discipline.

## Part 3 — The carrier map

Which segment of the butterfly carries which posture ID family. Grain: family-to-carrier here; the maintained artifact (AN-5) tracks row-level bindings.

| Annex ID family | What it demands | Primary carrier(s) | Carrier requirements |
|---|---|---|---|
| REG-FIND-001..005 (exemption findings) | Assume inclusion; glass-box design target | MAK-RWC Part 7 (update notes); MAK-RWC MX-1/MX-2 | MX-1, MX-2 |
| REG-FIND-006..008 (standards levers) | ISO 13485 deemed conformity; 27799/29147/30111 mapping; IEC 82304-1 breadth | Legs volume (infra/process); MAK-ABC AX-3 evidence | AX-3; LEG bindings |
| REG-KEEP-001 (deterministic release) | The gate stays | MAK-CEC | RG-1 |
| REG-KEEP-002 (reviewable basis) | Argument transparency everywhere | MAK-FFC SPINE-1; MAK-HDC HR-1/3; MAK-ABC AX-1 | SPINE-1, HR-3, AX-1 |
| REG-KEEP-003 (human sign-off, fail-closed) | Terminal human act | MAK-HDC | HA-1 |
| REG-KEEP-004 (synthetic-only until controls) | GATE-002 line | all phase plans; MAK-CEC RG-3 | AN-7; RG-3 |
| FORK-REG-001 (tier relabel) | J-1/J-2 as lower/higher-class included | MAK-CEC RG-6; MAK-RWC Part 7 note 2 | RG-6 |
| OBL-001..012 (obligations) | Evidenced register with owners | MAK-ABC | AX-3 |
| STD-001..012 (standards stack) | Standards bindings and currency | Legs volume; AN-4 currency duty | AN-4; LEG bindings |
| GATE-000..004 (gates) | Phase governance + evidence bundles | all volumes' phasing; MAK-ABC AX-4 | AN-7; AX-4 |
| TASK-REG-001..020 (tasks) | The programme plan | Legs volume (stack tasks 009–013); MAK-ABC (015–020 evidence); AN-9 (003); MAK-TXC TL-5 (004) | per-row in the maintained map |
| KTX-001..012 (Ketryx schema) | Lifecycle system of record | MAK-RWC MX-4; MAK-CEC RG-7; MAK-ABC AG bindings | MX-4, RG-7 |
| WATCH-REG-001..005 (watch items) | Cadenced sensing | this wrapper | AN-6; Part 4 |
| Q-REG-001..007 (questions) | Owned open questions | this wrapper + MAK-ABC | AN-10; AX-4 |
| ASSUME-REG-001..007 (assumptions) | Attestation-gated closure | this wrapper; every dependent volume | AN-3; (TL-5 for 003; RG-7 for 004/006) |

## Part 4 — Signals received

Additive log of regulatory signals received after the annex's currency date (2026-08-31). None amends the annex; each is an input to the next folded revision. Format per AN-6.

- **S-1 · FDA PCCP final guidance (logged 2026-09-01; source: Federal Register availability notice, 4 Dec 2024, verified via MAK-RWC v1.1 Part 9).** *Bearing: no amendment; enrichment.* A US-only pre-authorized change-control instrument; maps naturally onto the MS-4 remodeling lifecycle and MA-5 bundles. Feeds AN-11's jurisdiction map; no bearing on TGA findings.
- **S-2 · TGA AI guidance content (logged 2026-09-01; source: guidance discussed in practitioner analyses of 22 Apr 2026; the annex's WATCH-REG-002 anticipated this instrument applying from 5 Feb 2026).** *Bearing: reinforces.* Same-rules posture; functional updates are regulatory events pre-deployment (aligns GPP-3/MS-4); transparency expectations cover training data, validation, ongoing monitoring (aligns ME-6/MA-5); **synthetic data will generally not replace clinical data** for safety-and-performance evidence — sharpens the reading of REG-KEEP-004 as development posture, not validation evidence (AN-7 carries the consequence). WATCH-REG-002's "read against the intended purpose statement once written" remains open pending TASK-REG-001.
- **S-3 · FDA revised CDS guidance (carried; 6 Jan 2026, pre-dates the annex and is anchored in MAK-FFC v1.1/MAK-J3).** *Bearing: already absorbed.* Logged here so the wrapper's signal log is complete from series inception.

## Appendix A — ID census (wrapper, additive)

Wrapper IDs only; annex IDs are enumerated by the annex itself and are not re-censused here (self-audit check 6 verifies their presence).

```json
{
  "doc_id": "MAK-ANT",
  "version": "1.0",
  "requirements": {"AN": ["AN-1","AN-2","AN-3","AN-4","AN-5","AN-6","AN-7","AN-8","AN-9","AN-10","AN-11","AN-12"]},
  "levels": {
    "MUST": ["AN-1","AN-2","AN-3","AN-4","AN-5","AN-6","AN-7","AN-8","AN-9"],
    "SHOULD": ["AN-10","AN-11"],
    "MAY": ["AN-12"]
  },
  "retired": []
}
```

Census arithmetic: 9 MUST + 2 SHOULD + 1 MAY = 12.

## Appendix B — Self-audit checks (additive)

1. **ID uniqueness** — no AN ID appears in more than one requirement header.
2. **ID census parity** — headers matching `^### AN-\d+ \((MUST|SHOULD|MAY)\)$` exactly equal Appendix A (12).
3. **Level parity** — header levels match Appendix A buckets.
4. **Trace presence** — every AN block has a non-empty rationale trace.
5. **Normative leakage** — no capitalized MUST/SHOULD/MAY in wrapper prose outside requirement blocks, quoted annex text, or this appendix; the annex's own normative language is annex-internal and untouched.
6. **Annex verbatim integrity** — the Annex 1 text is byte-identical to REG-POSTURE v1.0 as uploaded, except for the annex banner; every ID family the annex frontmatter declares appears in the annex body.
7. **Carrier-map completeness** — every annex ID family has a carrier row; every carrier requirement cited resolves in its host volume.
8. **Signal-log discipline** — Part 4 entries are additive, dated, sourced, and bearing-assessed; no entry claims to amend the annex.
9. **Table integrity** — consistent column counts per row.
10. **Stability** — AN IDs from previous versions present or explicitly retired; never reused.

---

# Annex 1 — REG-POSTURE v1.0, folded verbatim

> **Annex banner (additive).** The following is the complete text of **REG-POSTURE v1.0** (Mākoha — Regulatory Posture and Ketryx Implementation Plan, Arepo Medtech Pty Ltd, issued 2026-08-31), folded into this corpus unmodified. Its own frontmatter is preserved below as a fenced block. Authority: ADVISORY_ONLY per that frontmatter — see the wrapper's LLM usage contract. If a standalone REG-POSTURE file is maintained in the document ecosystem, that file is canonical and this annex mirrors it; divergence is a validator error.

```yaml
doc_id: REG-POSTURE
title: Mākoha — Regulatory Posture and Ketryx Implementation Plan
version: 1.0
status: DRAFT
authority: ADVISORY_ONLY
entity: Arepo Medtech Pty Ltd
product: Mākoha
date_issued: 2026-08-31
guidance_currency_date: 2026-08-31
supersedes: none
depends_on:
  - Addendum J-1 (deterministic runtime posture)
  - Addendum J-2 (ML runtime, SaMD classification posture)
  - Build Ecosystem v2.0 (Implementer Contract, Observer adjudication)
blocks:
  - GATE-000
id_prefixes: [REG-FIND, ASSUME-REG, OBL, STD, FORK-REG, GATE, TASK-REG, KTX, WATCH-REG, Q-REG, SRC-REG]
attestation_required: true
attestation_by: Australian regulatory counsel
```

# Mākoha — Regulatory Posture and Ketryx Implementation Plan

**Prepared for:** Arepo Medtech Pty Ltd
**Date:** 31 August 2026
**Status:** Working document. Not regulatory advice. Requires counsel attestation before any commitment.

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

### 0.4 Status vocabulary

Aligned to Implementer Contract vocabulary. Permitted values only:

- `OPEN` — not started
- `IN-PROGRESS` — started, no evidence yet
- `DONE-WITH-EVIDENCE` — complete, evidence artifact named
- `HALT-TYPED` — blocked, with typed halt reason
- `SUPERSEDED` — replaced by a later ID, which must be named
- `ATTESTED` — closed by named external party, with date

`ASSUME-REG-*` items may hold only `OPEN`, `ATTESTED` or `SUPERSEDED`.
No `ASSUME-REG-*` may be closed by internal reasoning.

### 0.5 Validator conventions

A companion validator over this document should enforce:

1. Every ID matches `^(REG-FIND|ASSUME-REG|OBL|STD|FORK-REG|GATE|TASK-REG|KTX|WATCH-REG|Q-REG|SRC-REG)-[0-9]{3}$`
2. Every ID appears exactly once in a definition table and zero-or-more times in prose
3. Every `TASK-REG-*` names its gate
4. Every `GATE-*` names its predecessor tasks, and every named predecessor exists
5. Every `ASSUME-REG-*` names an attesting party and a blocking gate
6. Every `REG-FIND-*` names at least one `SRC-REG-*`
7. Status values are drawn only from §0.4
8. No `ASSUME-REG-*` in `ATTESTED` state lacks an attestation date

These are the same eight-check shape used elsewhere in the ecosystem; see §12.

### 0.6 Firewall note

This document contains no case content, no evidence-library values, no
sensitivities, specificities or likelihood ratios. It is safe to load alongside
scoring-store material. It must **not** be used as a source for clinical content
under any circumstance.

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
| `REG-FIND-008` | IEC 82304-1 is the only standard in the TGA matrix marked relevant to every applicable Essential Principle for health software on general computing platforms. | OPEN | `SRC-REG-003` |

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

---

## §3 Revised posture

> **Build to SaMD standard. Test exemption honestly at a named gate. Assume
> inclusion.**

This is a change from "build exemption-compatible, document to SaMD standard." The
architectural constraint is dropped; the documentation discipline is not.

### 3.1 The fork, restated

| Field | Value |
|---|---|
| ID | `FORK-REG-001` |
| Prior framing | Exempt (J-1) vs ARTG-included (J-2) |
| Revised framing | Lower-class included (J-1) vs higher-class included (J-2) |
| Decision point | Maturity Level 4, on Level 3 abstention evidence — **unchanged** |
| Status | OPEN |
| Blocking | `ASSUME-REG-001`, `ASSUME-REG-002` |

The maturity-gate mechanism survives. Only the two branch labels change. J-1 no
longer means "exempt"; it means deterministic runtime with a lower expected
classification. This is a relabelling, not a re-derivation — the underlying
architectural fork and its pre-registered reversal triggers stand.

### 3.2 Retained regardless of pathway

| ID | Commitment | Rationale after `REG-FIND-001` |
|---|---|---|
| `REG-KEEP-001` | Deterministic release path | No longer exemption-motivated; remains correct safety architecture and strengthens the Essential Principles case |
| `REG-KEEP-002` | Reviewable basis for every output | Not a ticket to exemption; directly responsive to Essential Principle 13 and to clinician trust, which is the product thesis |
| `REG-KEEP-003` | Human sign-off, fail-closed | Unchanged |
| `REG-KEEP-004` | Synthetic-only until controls operate | Unchanged; now enforced by `GATE-002` |

### 3.3 Changed

- Stop treating the exemption as the target. Treat it as a fallback to be tested
  once, formally, and then closed (`ASSUME-REG-002`).
- Stop deferring ARTG classification work. It is now the live path.
- The J-1/J-2 fork is no longer *exempt vs included*. It is *lower-class included vs
  higher-class included*. Still worth having, but reframe it.

### 3.4 The one honest caveat

A narrow reading could argue Mākoha "supports a recommendation" and never asserts a
diagnosis. Do not rely on this without counsel. The guidance's definition of
recommendation explicitly excludes *contributing to* diagnosis, which is a low bar to
cross, and the sepsis example shows TGA applying it strictly to proprietary
evidence-based logic. Get a written opinion before spending anything on the
assumption.

This caveat is carried as `ASSUME-REG-002` and is the only permitted route to
reversing `REG-FIND-001`.

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
| `OBL-012` | Notify TGA within 30 working days of supply — **exempt pathway only** | Applies only if `ASSUME-REG-002` closes in favour of exemption |

`OBL-009` and `OBL-007` are explicitly **outside the scope of any compliance
platform** and must be resourced separately.

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

| ID | Item | Status |
|---|---|---|
| `ASSUME-REG-004` | Baseten Sydney region available on dedicated deployment with contractual version-stability and change-notice terms | OPEN — closes on written confirmation from Baseten |

### 5.2 Amplify git-push

Fine for the synthetic demo. A finding on a regulated release path. Needs a gate
before first clinical supply — see `TASK-REG-010`.

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
  answer.

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
Essentials-tier feature. On the free tier you carry tool validation yourself.
Acceptable while building on synthetic data; a decision point before clinical supply.

**Prerequisite:** Jira. This is the real cost of the choice — adopting Jira as the
regulated work-item tracker.

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

### 6.6 Ecosystem boundary

Ketryx becomes the system of record for **regulated work items and design controls
only**. It does not displace:

- The 21-file document set — which remains the governing architecture
- The Build Ecosystem v2.0 Implementer Contract and Observer adjudication protocol
- The firewalled evaluation corpus — Test Case items reference corpus cases by ID;
  **corpus content does not enter Ketryx**
- The differential library and its validator — clinical content, firewall-partitioned

Mapping between ecosystem IDs and Ketryx items is by reference, not by copy.

---

## §7 Sequenced plan

### Phase 0 — Decide (weeks 1–4). Blocking.

| ID | Task | Gate |
|---|---|---|
| `TASK-REG-001` | Write the intended purpose statement. One document, one claim. Everything downstream depends on it. Include the three surfaces explicitly and what each does. | `GATE-000` |
| `TASK-REG-002` | Engage Australian regulatory counsel for a written classification opinion: medical device status, classification rule and class, exemption eligibility (expected: not eligible), conformity assessment route. | `GATE-000` |
| `TASK-REG-003` | Reconcile public positioning. The site currently markets AI capability. Under an inclusion path this is fine and stops being a liability — but the claims must match the intended purpose statement exactly, because advertising requirements for therapeutic goods apply to exempt and included devices alike (`OBL-003`). | `GATE-000` |
| `TASK-REG-004` | Decide the patient surface. Separate product, non-decision-support, or in-scope for the same submission. Each has different consequences. | `GATE-000` |

**`GATE-000`:** counsel opinion in hand; `ASSUME-REG-001` and `ASSUME-REG-002`
ATTESTED. Do not configure tooling before this.

### Phase 1 — Foundation (weeks 4–12)

| ID | Task | Gate |
|---|---|---|
| `TASK-REG-005` | Adopt Jira. Ketryx free tier. One project, synthetic scope. | `GATE-001` |
| `TASK-REG-006` | Configure from the Ketryx schema (`KTX-001`). Risk module strict mode on (`KTX-011`). Traceability V-model configured minimally (`KTX-010`). | `GATE-001` |
| `TASK-REG-007` | Stand up the ISO 14971 risk file. This is the spine everything else hangs from — before requirements, before design controls. | `GATE-001` |
| `TASK-REG-008` | Requirements from the intended purpose statement, tagged with `Relevant standards` against Essential Principles (`KTX-008`). | `GATE-001` |
| `TASK-REG-009` | Migrate inference to Baseten Sydney, dedicated deployment, pinned weights. Get version-stability and change-notice commitments in the contract (`ASSUME-REG-004`). | `GATE-001` |

**`GATE-001`:** risk file exists, requirements traced, model version pinned.

### Phase 2 — Controls (months 3–6)

| ID | Task | Gate |
|---|---|---|
| `TASK-REG-010` | Split the Amplify path: synthetic/demo continues push-to-deploy; regulated releases go through a gated pipeline with approval landing as a CI artifact. | `GATE-002` |
| `TASK-REG-011` | SBOM generation in CI, flowing into Ketryx supply chain management (`KTX-012`, `OBL-004`). | `GATE-002` |
| `TASK-REG-012` | Vulnerability handling and disclosure processes (`STD-009`), with CVSS scoring and CAPA linkage (`OBL-008`). | `GATE-002` |
| `TASK-REG-013` | Supplier assessments — Baseten, AWS — with contractual security expectations and incident reporting thresholds (`OBL-005`, `OBL-006`). | `GATE-002` |
| `TASK-REG-014` | IEC 62366-1 use-related risk analysis (`STD-004`). Three surfaces, three analyses. The patient surface is hardest; do it last but do not skip it. | `GATE-002` |

**`GATE-002`:** controls operating. **This is the line before any identifiable
clinical data touches any environment.** Enforces `REG-KEEP-004`.

### Phase 3 — Evidence (months 6–18)

| ID | Task | Gate |
|---|---|---|
| `TASK-REG-015` | Clinical evidence and validation — the Lumos linkage pathway. Longest lead item in the programme; started in parallel from Phase 1, not sequentially. | `GATE-003` |
| `TASK-REG-016` | Independent penetration testing, by a party outside the development team (`OBL-007`). | `GATE-003` |
| `TASK-REG-017` | Post-market surveillance procedures, adverse event reporting readiness (`OBL-002`). | `GATE-003` |
| `TASK-REG-018` | Ketryx tier upgrade for validated-out-of-the-box status and post-market surveillance features (`WATCH-REG-004`). | `GATE-003` |

**`GATE-003`:** clinical evidence sufficient, security testing complete, post-market
processes operating.

### Phase 4 — Submission

| ID | Task | Gate |
|---|---|---|
| `TASK-REG-019` | Conformity assessment application. Route per counsel opinion (`Q-REG-005`). | `GATE-004` |
| `TASK-REG-020` | ARTG inclusion. | `GATE-004` |

**`GATE-004`:** ARTG inclusion granted. First lawful clinical supply.

---

## §8 Assumptions register

No `ASSUME-REG-*` may be closed by internal reasoning. Each requires written
external attestation.

| ID | Assumption | Attesting party | Blocks | Status |
|---|---|---|---|---|
| `ASSUME-REG-001` | Mākoha's device classification and applicable classification rule | AU regulatory counsel | `GATE-000` | OPEN |
| `ASSUME-REG-002` | CDSS exemption is unavailable to Mākoha (`REG-FIND-001` confirmed) | AU regulatory counsel | `GATE-000` | OPEN |
| `ASSUME-REG-003` | Patient surface treatment — separate product, non-decision-support, or in-scope | Counsel + product | `GATE-000` | OPEN |
| `ASSUME-REG-004` | Baseten Sydney region on dedicated deployment, with version-stability and change-notice terms | Baseten | `GATE-001` | OPEN |
| `ASSUME-REG-005` | Conformity assessment route (TGA vs notified body) | AU regulatory counsel | `GATE-004` | OPEN |
| `ASSUME-REG-006` | Ketryx tier and validation package timing | Ketryx | `GATE-003` | OPEN |
| `ASSUME-REG-007` | Lumos linkage ethics and custodian requirements | Data custodian | `GATE-003` | OPEN |

---

## §9 Open questions requiring external input

| ID | Question | Who | Blocking |
|---|---|---|---|
| `Q-REG-001` | Device classification and rule | AU regulatory counsel | Phase 1 |
| `Q-REG-002` | Exemption eligibility — written opinion | AU regulatory counsel | Phase 1 |
| `Q-REG-003` | Patient surface treatment | Counsel + product | Phase 1 |
| `Q-REG-004` | Baseten: Sydney region, version-stability and change-notice terms | Baseten sales | Phase 1 |
| `Q-REG-005` | Conformity assessment route (TGA vs notified body) | Counsel | Phase 3 |
| `Q-REG-006` | Ketryx tier and validation package timing | Ketryx | Phase 3 |
| `Q-REG-007` | Lumos linkage — ethics and custodian requirements | Data custodian | Phase 1 (parallel) |

---

## §10 Watch items

Non-closing. Review cadence stated per item.

| ID | Item | Cadence |
|---|---|---|
| `WATCH-REG-001` | TGA has consulted on amending the CDSS exemption, including introducing a legislative definition of CDSS in the Regulations and clarifying the transparency conditions. Outcome may shift the boundary in either direction. | Quarterly |
| `WATCH-REG-002` | TGA guidance on AI-enabled medical device software applies from 5 February 2026. Read it against the intended purpose statement once written (`TASK-REG-001`). | Once, then annually |
| `WATCH-REG-003` | The exemption guidance was fully rewritten on 7 October 2025 — anything written before that date about the CDSS exemption, including consultancy commentary, may describe the previous position. | Standing caution |
| `WATCH-REG-004` | Ketryx tier: validated-out-of-the-box is Essentials-tier. Free-tier validation burden is yours. | At `GATE-002` |
| `WATCH-REG-005` | Standards revision — confirm current version of each `STD-*` before citing in submission. | Annually |

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
| `SRC-REG-007` | Ketryx documentation — Jira integration, risk management (MAN-08), test management (MAN-06), threat modelling, advanced settings, WI-01 Requirement | Accessed August 2026 |
| `SRC-REG-008` | Ketryx pricing page | Accessed August 2026 |
| `SRC-REG-009` | Baseten deployment, region and compliance documentation | Accessed August 2026 |
| `SRC-REG-010` | OpenRegulatory — eQMS comparison and free ISO 13485 / IEC 62304 templates. Recommended starting point for learning the record structures. | Independent; updated March 2026 |

**Source caution:** `SRC-REG-001` through `SRC-REG-004` are primary. `SRC-REG-007`
through `SRC-REG-009` are vendor documentation and carry vendor interest.
`SRC-REG-010` is independent but commercially adjacent. Most eQMS comparison material
encountered during research was content marketing by competing vendors and was not
relied upon.

---

## §12 ID census and self-audit

### 12.1 Census

| Prefix | Count | Range |
|---|---|---|
| `REG-FIND` | 8 | 001–008 |
| `REG-KEEP` | 4 | 001–004 |
| `ASSUME-REG` | 7 | 001–007 |
| `OBL` | 12 | 001–012 |
| `STD` | 12 | 001–012 |
| `FORK-REG` | 1 | 001 |
| `GATE` | 5 | 000–004 |
| `TASK-REG` | 20 | 001–020 |
| `KTX` | 12 | 001–012 |
| `WATCH-REG` | 5 | 001–005 |
| `Q-REG` | 7 | 001–007 |
| `SRC-REG` | 10 | 001–010 |
| **Total** | **103** | |

### 12.2 Self-audit checks

| # | Check | Result |
|---|---|---|
| 1 | All IDs conform to the pattern in §0.5 | PASS |
| 2 | Every ID defined exactly once in a table | PASS |
| 3 | Every `TASK-REG-*` names its gate | PASS (20/20) |
| 4 | Every `GATE-*` names predecessors; all predecessors exist | PASS (5/5) |
| 5 | Every `ASSUME-REG-*` names attesting party and blocking gate | PASS (7/7) |
| 6 | Every `REG-FIND-*` names at least one `SRC-REG-*` | PASS (8/8) |
| 7 | Status values drawn only from §0.4 | PASS |
| 8 | No `ATTESTED` item lacks an attestation date | PASS (vacuous — zero attested) |

### 12.3 Known gaps

- `Q-REG-*` and `ASSUME-REG-*` overlap by design: the question is the mechanism,
  the assumption is the state. They are deliberately not merged, so that a question
  can be answered without the assumption automatically closing.
- No `REG-FIND-*` currently holds `SUPERSEDED`. On any counsel finding that
  contradicts `REG-FIND-001`, mark it SUPERSEDED and name the replacement; do not
  edit it in place.
- Check 8 passes vacuously and will become meaningful only after `GATE-000`.

---

*This document reflects publicly available guidance as at 31 August 2026 and is not a
substitute for regulatory advice. Classification and exemption eligibility must be
determined by qualified counsel before commercial commitment.*
