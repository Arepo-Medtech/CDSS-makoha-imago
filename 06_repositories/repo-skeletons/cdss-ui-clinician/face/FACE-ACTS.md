---
doc_id: FACE-ACTS
title: "cdss-ui-clinician/face — act writers: design spec (TASK-HDC-002)"
version: "1.0"
date: "2026-09-09"
status: "Proposed — skeleton; DEC-09 repo home ratified (cdss-ui-clinician, owner Kenny-bytes, PFX UIC)"
source_task: "TASK-HDC-002 (MAK-66)"
grounding: "PRM-HDC HDC4 act writers; CONTRACT-ACT-1 (05_registers-and-contracts/CONTRACT-ACT-1_act_schema.md); MAK-HDC HA-1..6; MAK-FFC SPINE-4/5/8; MAK-RWC MS-2/3/7; REG-KEEP-003"
---

# face/FACE-ACTS — Six act writers with fail-closed sign-off

The face-acts component is the write path of the Clinician Face. It owns exactly six
act writers, each producing one CONTRACT-ACT-1 fabric entry attributed to the acting
clinician and pinned to the argument version the actor saw. It never evaluates, never
releases, and never produces a verdict — those are PRM-CEC's domain (MAK-CEC OM-5).

Each act opens in one interaction (one pointer action or one keystroke sequence from the
element in focus — the friction bound from PRM-HDC HDC8 tolerances). Each act writes
exactly one fabric entry; no act writes zero or more than one entry.

## 1. Sign-off writer (HA-1 · REG-KEEP-003)

Produces a `SignoffAct` (CONTRACT-ACT-1). The actor must hold
`authority_class: clinical-release`. Requires `arg_id`, `arg_version`, `verdict_ref`,
and `projection_context` (all versions of the artifacts that determined the rendered
state — not only the argument version; ACT-11).

**Fail-closed invariant:** timeout, inactivity, focus loss, and navigation produce no
action and no act record. There is no default release, no implied consent, and no action
on absence. A release-class action (order, prescription, referral, patient-visible
diagnostic statement per MAK-FFC PF-8) requires exactly one committed SignoffAct.

## 2. Deviation writer (HA-2 · SPINE-8)

Produces a `DeviationAct` (CONTRACT-ACT-1). Opens in one interaction from any displayed
recommendation. Requires `reason_taxonomy_code` (from the ratified deviation taxonomy
in the registry — OPS-1 change class), `severity_tier`
([NEEDS DEFINITION — DEC-02]; shape-constrained only), and `free_text` (never blocked
or validated away; the clinician may leave it empty or fill it freely).

`boundary_context` (threshold_ref + distance) is pre-populated automatically when the
act is opened from a borderline-flagged argument (FC-2). A DeviationAct and a
GapReportAct may coexist on the same encounter without either blocking or implying the
other (HA-3).

## 3. Gap reporter (HA-3 · MS-2)

Produces a `GapReportAct` (CONTRACT-ACT-1). Available from any screen — no released
ActualArgument required. The `locus` field is a discriminated reference
(`locus_kind` ∈ `{arg, template, encounter, element}`) and is pre-populated from the
current screen context. A GapReportAct and a DeviationAct may both be committed on the
same encounter without either blocking the other.

## 4. Fit-judgment writer (HA-4 · MS-7)

Produces a `FitJudgmentAct` (CONTRACT-ACT-1). Triggered by a flagged verdict (RG-2
flagged class); the fit-judgment flow is the only path through which a flagged verdict
may proceed. Requires a structured `basis` (`mismatch_description`, `clinical_grounds`,
`decision`). Opens in one interaction from the flagged recommendation. The flagged state
of the verdict is not a hard stop — proceeding requires a committed FitJudgmentAct, not
a barrier or confirmation dialog.

## 5. Conflict-navigation writer (HA-5 · MS-7)

Produces a `ConflictNavigationAct` (CONTRACT-ACT-1). Records `conflict_record_ref`,
`choice`, `reasons`, and `residue` (unresolved aspects preserved verbatim — never
discarded). In team mode, records per-author stances (`author_stances`); dissent is
preserved, not averaged. Alternatives are never pre-ranked; the ordering of `arg_ids`
carries no preference semantics.

## 6. Boundary-work writer (HA-6 · MS-3)

Produces a `BoundaryWorkAct` (CONTRACT-ACT-1). Captures `verbatim_text` exactly as
authored. No validation gate may block, truncate, or silently rewrite the text. Display
escaping is applied at the rendering layer, not at this writer. The writer has no
friction beyond the one interaction that opens it.

## Component HALT triggers (from PRM-HDC HDC9 §7)

- Any act, order, referral, or release on timeout, inactivity, default focus, or
  implied consent → **HALT: HA-1 / REG-KEEP-003**
- Any act that attaches metric consequence, rate display, or peer comparison to
  deviation, gap, or fit-judgment within this face → **HALT: anti-requirements /
  MAK-RWC MA-6**
- Any deviation act that is blocked except where a deterministic safety class
  applies → **HALT: SPINE-8**
- Any act path that adds friction, nagging, or follow-up burden beyond the single
  opening interaction → **HALT: HA-2..6 friction law; PRM-HDC HDC6 item 6**

## HDC8 properties this component must prove

| Property | Statement (abridged) | Test status |
|---|---|---|
| 6 | ∀ encounter: with no SignoffAct, no release-class action exists after any elapsed time or focus event | EXECUTABLE against stub — schema enforces no signoff = no release; fault-injection examples in CONTRACT-ACT-1.examples.jsonl §2 |
| 8 | ∀ act: exactly one attributed fabric entry, argument version pinned; replay from projection_context reproduces the rendered state the actor saw | Stub portion EXECUTABLE (14/14 PASS, CONTRACT-ACT-1.examples.jsonl validated); replay round-trip UNVERIFIED — requires live SPINE-9 projection (RECON-HDC-001/002; GAP-ACT-002) |
| 10 | ∀ multi-author fixture with recorded dissent: no unanimous rendering | EXECUTABLE against stub — conflict_navigation-valid-with-stances example carries two AuthorStance records with distinct positions |

## Observability

Act latency histograms (time-to-deviate p50, time-to-gap) emitted to R13 under the
RG-5 schema extension (GAP-HDC-001). Alert on any committed act that lacks `arg_version`
where the act kind requires it (signoff, deviation, fit_judgment). Budget spend and act
counts to R13.

## Open items

| ID | Description |
|---|---|
| GAP-ACT-001 | `severity_tier` vocabulary [NEEDS DEFINITION — DEC-02]; shape-constrained only |
| GAP-ACT-002 | Replay round-trip (HDC8 property 8 full verification) UNVERIFIED — RECON-HDC-001/002 |
| GAP-ACT-003 | FabricEntryRef stub — full SPINE-4 chain protocol owned by cdss-fabric (GAP-HDC-002) |
| GAP-ACT-004 | Friction audit (one interaction per act) UNVERIFIED — requires UI fixture (TASK-HDC-001) |
| RECON-HDC-007 | CONTRACT-ACT-1 ratification into cdss-spine pending |
| Component owner | [NEEDS DEFINITION — DEC-09] |
