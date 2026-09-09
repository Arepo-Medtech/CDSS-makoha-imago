---
doc_id: CONTRACT-ACT-1-SPEC
title: "CONTRACT-ACT-1 — ClinicalAct discriminated-union schema: specification and test plan"
version: "1.0"
date: "2026-09-09"
status: "Proposed (DEC-02; staged draft, MOVES to cdss-spine on DEC-02 + DEC-09 ratification). DoR: CONTRACT-ACT-1 accepted path per RECON-HDC-007."
companion_to: "05_registers-and-contracts/CONTRACT-ACT-1.schema.json · CONTRACT-ACT-1.examples.jsonl · CONTRACT-DEV-1.schema.json (Deviation act superseded-and-extended by ACT-6 below; CONTRACT-DEV-1 is retained as a standalone Deviation object; CONTRACT-ACT-1 is the six-act envelope)"
grounding: "MAK-HDC HA-1..6; MAK-FFC SPINE-4/5/8, PF-8; MAK-RWC MS-2/3/7; PRM-HDC HDC8 properties 6/8/10; CLINICIAN_REQUIREMENT_RECONCILIATION_2026-09-08 §Contracts"
req_prefix: ACT
req_count: 12
---

# CONTRACT-ACT-1 — ClinicalAct discriminated-union schema

## 1. The contract shape

A `ClinicalAct` is the fabric record of one intentional clinical act performed by an
identified actor on a specific encounter. Six act kinds are defined; the `kind` field
discriminates the union. The contract is a discriminated-union, not a single interface:
sign-off requires an exact eligible argument and version; a gap report may bind only an
encounter context or screen element, with argument references when available. No act kind
may invent a dummy clinical argument to satisfy shape validation.

Every act kind shares a set of common fields and adds its own required fields. The common
fields are repeated in each variant schema (not referenced through an abstract base) so
that each variant validates independently against `additionalProperties: false`.

```
ClinicalAct = one of:
  SignoffAct               kind: "signoff"
  DeviationAct             kind: "deviation"
  GapReportAct             kind: "gap_report"
  FitJudgmentAct           kind: "fit_judgment"
  ConflictNavigationAct    kind: "conflict_navigation"
  BoundaryWorkAct          kind: "boundary_work"
```

**Common fields (present on every act kind):**

| Field | Type | Note |
|---|---|---|
| `act_id` | string | Stable UUID assigned at act creation; unique per logical act instance |
| `kind` | const string | Discriminator; one of the six values above |
| `actor` | ActorIdentity | Attribution and authority class (ACT-2) |
| `encounter_id` | string | The encounter this act belongs to |
| `timestamp` | date-time | Wall-clock time of the act |
| `idempotency_key` | string (SHOULD) | UI-generated key per render event; prevents retry duplication without collapsing distinct submissions (ACT-3) |
| `fabric_entry` | FabricEntryRef | Reference to the append-only fabric entry (ACT-4) |

**Supporting definitions:**

*ActorIdentity* — `actor_id` (string) + `authority_class` (enum: `recording` \|
`clinical-release`). Recording authority suffices for deviation, gap report, fit
judgment, conflict navigation, and boundary work. Clinical-release authority is required
for sign-off only (ACT-5).

*FabricEntryRef* — `entry_id` (string) + `entry_hash` (string). The hash chain
(SPINE-4) is maintained by cdss-fabric; this schema carries only the consumer-side
reference. Full chain protocol is GAP-ACT-003.

*ProjectionContext* — records the versions of every artifact that determined the
rendered state the actor saw at sign-off: `projection_version` (R1 pin for the SPINE-9
clinical projection), `renderer_version` (UI renderer build), `identity_sheet_version`
(MAK-LBP CV-1 identity sheet), `codebook_version` (optional — present when codebook
vocabulary was in use), `layout_config_hash`. Defined for SignoffAct only (ACT-11).

*GapLocus* — discriminated on `locus_kind`: `"arg"` (arg_id present), `"template"`
(template_id present), `"encounter"` (encounter_context string), `"element"`
(element_ref string). Exactly one locus kind applies per gap report (ACT-7).

*FitJudgmentBasis* — `mismatch_description` (string) + `clinical_grounds` (string) +
`decision` (string). Required on FitJudgmentAct (ACT-8).

*AuthorStance* — `author_id` (string) + `position` (string) + `reasoning` (string).
Used in ConflictNavigationAct for team-mode per-author stances (ACT-12).

*BoundaryContext* — `threshold_ref` (string) + `distance` (string). Attached to
DeviationAct when opened from a borderline-flagged argument (ACT-6); optional on
BoundaryWorkAct.

## 2. Requirements

### ACT-1 (MUST)
**Statement:** The schema is a discriminated union on `kind`; exactly six act kinds are
defined; every conforming act document matches exactly one variant and no other. A
document that matches zero or more than one variant is invalid.
**Rationale trace:** MAK-HDC HA-1..6; PRM-HDC HDC4 "Act writers"; CLINICIAN_REQUIREMENT_RECONCILIATION
§Contracts "Use a discriminated act schema."

### ACT-2 (MUST)
**Statement:** Every act carries an `actor` object with `actor_id` (the attributed
identity, not an authentication token) and `authority_class`. Two authority classes are
defined: `recording` (sufficient for deviation, gap report, fit judgment, conflict
navigation, boundary work) and `clinical-release` (required for sign-off only).
Enforcing the distinction at the endpoint is the implementation's responsibility; this
schema encodes the shape, not the authentication.
**Rationale trace:** MAK-HDC HA-1 "attributed, clinical authority"; PRM-HDC HDC5 emits
table "actor with clinical authority (HA-1; SPINE-8)"; CLINICIAN_REQUIREMENT_RECONCILIATION
§Contracts "Distinguish permission to record a factual boundary report from authority to
sign a clinical release."

### ACT-3 (MUST)
**Statement:** Every act SHOULD carry an `idempotency_key` supplied by the calling UI at
render time (not at submission time). The fabric treats a duplicate idempotency_key from
the same actor on the same encounter as a no-op and returns the existing entry reference;
it never collapses two submissions with distinct keys even when their payload is otherwise
identical.
**Rationale trace:** CLINICIAN_REQUIREMENT_RECONCILIATION §Contracts "Entry hash alone
cannot distinguish two separately intended identical contributions. Idempotency must
prevent retry duplication without collapsing legitimate repeated acts."

### ACT-4 (MUST)
**Statement:** Every act, when committed, produces exactly one append-only fabric entry.
The act record carries a `fabric_entry` object with `entry_id` and `entry_hash`; the
fabric maintains the hash chain (SPINE-4). No act schema admits a committed act without
a fabric_entry reference.
**Rationale trace:** MAK-HDC HA-1..6 "each a fabric entry with the argument version it
acted on"; MAK-FFC SPINE-4 "append-only, hash-chained"; PRM-HDC HDC8 property 8.

### ACT-5 (MUST)
**Statement:** `SignoffAct` requires `arg_id`, `arg_version`, `verdict_ref`, and
`projection_context`. The actor must carry `authority_class: clinical-release`. The
invariant: absent a sign-off act, no release-class action (order, prescription, referral,
patient-visible diagnostic statement) exists for the encounter, regardless of elapsed
time, inactivity, focus loss, or navigation — these events produce no action. Fault
injection of timeout, inactivity, and focus loss must each produce zero SignoffAct
records and zero downstream release actions.
**Rationale trace:** MAK-HDC HA-1; REG-KEEP-003; MAK-FFC PF-8; PRM-HDC HDC8 property 6
"∀ encounter: with no signoff act, no release-class action exists after any elapsed time
or focus event."

### ACT-6 (MUST)
**Statement:** `DeviationAct` requires `arg_id`, `arg_version`, `reason_taxonomy_code`,
`severity_tier`, and `free_text`. `free_text` is never blocked or validated away.
`boundary_context` (threshold_ref + distance) is optional and is auto-attached when the
act is opened from a borderline-flagged argument (HA-2; FC-2). `severity_tier`
vocabulary is [NEEDS DEFINITION — architecture owner, DEC-02]; the schema constrains
shape only. The deviation taxonomy lives in the registry (OPS-1 change class:
deviation-taxonomy); this schema carries only `reason_taxonomy_code` as a string
reference. A DeviationAct and a GapReportAct may coexist on one encounter without
either blocking or implying the other (HA-3).
**Rationale trace:** MAK-HDC HA-2; MAK-FFC SPINE-8 Deviation object; PRM-HDC HDC4
"deviation: taxonomy + free text + severity + auditor preview payload."

### ACT-7 (MUST)
**Statement:** `GapReportAct` is available from any screen; it does not require a
released ActualArgument. The `locus` field is a discriminated object (GapLocus) with
`locus_kind` set to one of: `"arg"` (with arg_id), `"template"` (with template_id),
`"encounter"` (with encounter_context), or `"element"` (with element_ref). Exactly one
locus kind must be present. `free_text` is optional. `arg_id` and `arg_version` at the
top level of GapReportAct are optional and are present only when a released argument
contextualizes the gap. A GapReportAct and a DeviationAct may both be committed on the
same encounter without either blocking the other (HA-3 "deviate-vs-gap both allowed on
one case").
**Rationale trace:** MAK-HDC HA-3; MAK-RWC MS-2; PRM-HDC HDC4 "gap: locus pre-population;
deviate-vs-gap both allowed on one case"; CLINICIAN_REQUIREMENT_RECONCILIATION §Contracts
"a gap may bind its actual template, source, encounter, screen or element context, with
argument references when available. Do not invent a dummy clinical argument to satisfy
shape validation."

### ACT-8 (MUST)
**Statement:** `FitJudgmentAct` requires `arg_id`, `arg_version`, `verdict_ref` (which
must reference a flagged verdict per RG-2), and `basis` (FitJudgmentBasis: three
required strings — `mismatch_description`, `clinical_grounds`, `decision`). `free_text`
is optional and supplementary. Proceeding past a flagged verdict without a committed
FitJudgmentAct is a contract violation (HDC8 property 3; HA-4).
**Rationale trace:** MAK-HDC HA-4; MAK-RWC MS-7; MAK-CEC RG-2 "for flagged releases,
the recorded human fit-judgment"; PRM-HDC HDC4 "fit-judgment: structured basis, same
pattern as deviation."

### ACT-9 (MUST)
**Statement:** `ConflictNavigationAct` requires `conflict_record_ref` (the ConflictRecord
reference), `choice` (string — which path was chosen), `reasons` (string — clinician's
stated reasons), and `residue` (string — unresolved aspects preserved verbatim). `arg_ids`
(array of conflicting argument IDs) and `author_stances` (array of AuthorStance) are
optional at the schema level but must be present when the corresponding data is available.
Alternatives are never pre-ranked; the order of `arg_ids` carries no preference semantics.
**Rationale trace:** MAK-HDC HA-5, HT-3; MAK-RWC MS-7; PRM-HDC HDC4 "conflict navigation:
choice + reasons + residue; per-author stances."

### ACT-10 (MUST)
**Statement:** `BoundaryWorkAct` requires `verbatim_text` — the clinician's authored text
preserved exactly as written. No validation gate may block, truncate, or silently rewrite
`verbatim_text`. `display_safe_text` is optional; its absence does not suppress rendering
of `verbatim_text` (which is shown with display escaping applied at the rendering layer,
not at the schema layer). `boundary_context` is optional.
**Rationale trace:** MAK-HDC HA-6; MAK-RWC MS-3; PRM-HDC HDC4 "boundary work: verbatim
preservation, no validation gate"; CLINICIAN_REQUIREMENT_RECONCILIATION §Contracts
"Preserve clinical free text in its authorised store and escape it at display boundaries.
'Never validate away boundary work' does not require executing user HTML or abandoning
structural/security validation."

### ACT-11 (MUST)
**Statement:** `SignoffAct` carries a `projection_context` object recording the versions
of every artifact that determined the rendered state the actor saw: `projection_version`
(R1 pin for the SPINE-9 clinical projection), `renderer_version` (UI renderer build),
`identity_sheet_version` (MAK-LBP CV-1 identity sheet), `codebook_version` (optional —
present when codebook vocabulary was in use), and `layout_config_hash`. Replay from a
stored `projection_context` must reproduce the rendered state the actor signed. An
argument version pin alone does not constitute sufficient replay evidence.
**Rationale trace:** MAK-FFC SPINE-5; PRM-HDC HDC8 property 8 "replay from pins
reproduces the rendered state acted upon"; CLINICIAN_REQUIREMENT_RECONCILIATION §Contracts
"Replay of the state the actor saw needs more than the argument version: record projection,
renderer/identity/codebook and applicable layout/configuration versions."

### ACT-12 (MUST)
**Statement:** `ConflictNavigationAct` carries an `author_stances` array in multi-author
(team mode) contexts. Each AuthorStance carries `author_id`, `position` (string), and
`reasoning` (string). A fixture with two authors holding distinct positions must not
render as unanimous; the presence of recorded dissent in `author_stances` is a mandatory
non-unanimous signal for any projection of that conflict record.
**Rationale trace:** MAK-HDC HA-5, HT-1, HT-3; PRM-HDC HDC8 property 10 "∀ multi-author
fixture with recorded dissent: no unanimous rendering"; PRM-HDC HDC6 item 11.

## 3. Executable properties (HDC8 subset — face-acts scope)

These are the three HDC8 first-executable properties this contract directly enables.
Fixture inputs are synthetic; no property run on a fixture claims production-readiness.

**Property 6** — Fail-closed sign-off:
```
∀ encounter: with no SignoffAct committed, no release-class action exists
after any elapsed time or focus event (HA-1; REG-KEEP-003).
```
Test method: fault-inject timeout, inactivity, and focus-loss events; assert zero
`SignoffAct` records written; assert zero release-class downstream events emitted.
See Examples §2 in `CONTRACT-ACT-1.examples.jsonl` for the fault-injection scenario.

**Property 8** — Act-record completeness and replay:
```
∀ act: exactly one fabric entry, attributed, argument version pinned;
replay from projection_context reproduces the rendered state the actor saw
(HA-1..6; SPINE-5).
```
Test method (stub portion): commit one of each act kind against a synthetic fabric
stub; assert one `fabric_entry` per act; assert all common fields present and non-empty;
for SignoffAct, assert `projection_context` fields non-empty. Replay round-trip
(re-projecting from stored `projection_context` yields bit-identical rendered state):
UNVERIFIED — requires live SPINE-9 projection (RECON-HDC-001/002; GAP-ACT-002).

**Property 10** — No unanimous rendering of recorded dissent:
```
∀ multi-author fixture with recorded dissent: no unanimous rendering (HT-1).
```
Test method: construct a `ConflictNavigationAct` with two `author_stances` holding
distinct positions; assert any projection of the parent ConflictRecord carries both
positions and does not render as resolved or unanimous. See Examples §3 in
`CONTRACT-ACT-1.examples.jsonl`.

## 4. Test plan

| Test | Act(s) | Method | Outcome |
|---|---|---|---|
| One-act fixtures (all six) | All | Validate each .jsonl valid example against its schema variant | EXECUTABLE — JSON Schema validation |
| Both-acts fixture | deviation + gap_report | One encounter_id; two entries; assert no schema constraint blocks coexistence | EXECUTABLE — two examples share encounter_id in .jsonl |
| Fault-injection: timeout/inactivity/focus loss | signoff | No SignoffAct written; no release action emitted | EXECUTABLE against stub; schema invariant: absent SignoffAct = no release |
| Fault-injection: missing actor on signoff | signoff | Schema-invalid example; validator rejects | EXECUTABLE — JSON Schema validation |
| Missing locus on gap report | gap_report | Schema-invalid example; validator rejects | EXECUTABLE — JSON Schema validation |
| Friction audit (one interaction per act) | All | One pointer or keyboard action opens each act | UNVERIFIED — requires UI fixture (TASK-HDC-001; GAP-ACT-004) |
| Replay round-trip | signoff | Re-project from projection_context; assert bit-identical state | UNVERIFIED — requires live SPINE-9 projection (RECON-HDC-001/002; GAP-ACT-002) |
| Per-author stances (property 10) | conflict_navigation | Two-author fixture; assert non-unanimous projection | EXECUTABLE against stub |

No UNVERIFIED item is claimed as passed.

## 5. Gaps carried forward

| ID | Description |
|---|---|
| GAP-ACT-001 | `severity_tier` vocabulary for DeviationAct is [NEEDS DEFINITION — architecture owner, DEC-02]; schema constrains shape (pattern: `^[A-Z0-9][A-Z0-9-]*$`) only |
| GAP-ACT-002 | Replay round-trip (Property 8 full verification) requires a live SPINE-9 projection; UNVERIFIED without RECON-HDC-001/002 |
| GAP-ACT-003 | `FabricEntryRef` (entry_id + entry_hash) is a stub; the full SPINE-4 chain protocol is owned by cdss-fabric and has no numbered register entry yet (GAP-HDC-002) |
| GAP-ACT-004 | Friction audit (one interaction per act) requires a UI fixture; UNVERIFIED without TASK-HDC-001 |

## 6. ID census and self-audit

Census: ACT-1..ACT-12 (12) = `req_count` 12 · MUST 12, SHOULD 0.

Self-audit (2026-09-09):
1. Every requirement header matches `### ACT-n (MUST)` — **PASS** (12/12).
2. Every requirement carries a Rationale trace — **PASS** (12/12).
3. Every cited ID (HA-1..6, SPINE-4/5/8, MS-2/3/7, PF-8, RG-2, FC-2, REG-KEEP-003,
   HT-1/3, MAK-LBP CV-1, PRM-HDC HDC4/HDC6/HDC8, RECON-HDC-001/002, GAP-HDC-002,
   OPS-1, DEC-02, DEC-09, FC-2, MA-6) resolves in the corpus tree at ALPHA
   `99033be` — **PASS** by read-through.
4. No clinical number, fragment, or case text authored — **PASS**.
5. UNVERIFIED items named explicitly; no fixture result claimed as production
   evidence — **PASS**.
6. GAP-ACT-001 preserves the [NEEDS DEFINITION] from CONTRACT-DEV-1 without
   inventing a vocabulary value — **PASS**.
7. No statement relaxes a MAK-FFC, MAK-HDC, or MAK-RWC MUST — **PASS**.
8. `req_count` 12 equals declared ACT-n range — **PASS**.
