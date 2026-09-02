# Butterfly Primer Programme — Run Report

**Run date:** 2026-09-02 · **Scope:** ten primers in `/tmp/scratch/04_butterfly-primers/` (PRM-LWC, PRM-RWC, PRM-CEC, PRM-HDC, PRM-TXC, PRM-ABC, PRM-PRB, PRM-LBP, PRM-LEG, PRM-ANT) · **Method:** every primer's X5 (Consumes/Emits + Fabric binding), X8 asset table, Register topology annotation, X9 parts 3 and 8, X10 findings, Appendix A/B and Assumptions block read in full; X8 tables parsed programmatically (`x8stats.py`, scratchpad) so the totals in §5 are counted, not transcribed. Where a primer's self-reported count differs from the parsed count, both are shown.

**Headline numbers.** 10 primers · 296 requirement IDs mapped 296/296 (+16 MAK-J3 GPP IDs held provisionally in PRM-CEC) · 271 asset rows (89 BUILD) · 81 validity findings · 57 GAP proposals · 73 RECON items · 19 integration seams with no matching counterpart row · 10 ruling clusters · 20 errata/status items against source volumes · Appendix B: 100/100 checks Pass.

---

## 1. Mapping table as executed

The manifest has 15 rows; 10 received primers. Declared/mapped from each primer's Appendix A. File sizes as on disk 2026-09-02.

| doc_id | Primer file | Declared → mapped (Appendix A) | Families | Size |
|---|---|---|---|---|
| MAK-LWC v1.1 | `primer_LWC_fuzzy_spine.md` (PRM-LWC) | 43 → 43 | FS 9 · FC 7 · FP 8 · FA 7 · FE 9 · FX 3 | 48,752 B |
| MAK-RWC v1.1 | `primer_RWC_meta_rationality.md` (PRM-RWC) | 42 → 42 | MS 9 · MC 7 · MP 6 · MA 7 · ME 8 · MX 5 | 77,754 B |
| MAK-CEC v1.1 | `primer_CEC_engines.md` (PRM-CEC) | 38 → 38, plus MAK-J3 GPP 16 → 16 (provisional, v0.9-proposed) | OM 7 · CP 6 · DX 7 · QU 5 · AD 5 · RG 8 · GPP 16 | 92,580 B |
| MAK-HDC v1.0 | `primer_HDC_clinician_face.md` (PRM-HDC) | 30 → 30 | HW 5 · HR 6 · HA 6 · HG 5 · HT 4 · HE 4 | 77,550 B |
| MAK-TXC v1.0 | `primer_TXC_patient_face.md` (PRM-TXC) | 28 → 28 | TW 5 · TR 5 · TA 5 · TC 4 · TL 5 · TE 4 | 77,932 B |
| MAK-ABC v1.0 | `primer_ABC_auditor_face.md` (PRM-ABC) | 27 → 27 (21 MUST / 6 SHOULD) | AL 5 · AR 5 · AG 4 · AT 5 · AX 4 · AE 4 | 82,793 B |
| MAK-PRB v1.0 | `primer_PRB_patient_ui.md` (PRM-PRB) | 27 → 27 | PV 5 · PS 6 · PC 5 · PI 5 · PA 6 | 74,418 B |
| MAK-LBP v1.0 | `primer_LBP_clinician_ui.md` (PRM-LBP) | 26 → 26 | CV 5 · CS 6 · CC 5 · CI 5 · CA 5 | 70,005 B |
| MAK-LEG v1.0 | `primer_LEG_stack.md` (PRM-LEG) | 23 → 23 (10 MUST / 8 SHOULD / 5 MAY) | LS 4 · L1 3 · L2 3 · L3 3 · L4 3 · L5 3 · L6 4 | 81,097 B |
| MAK-ANT v1.0 | `primer_ANT_regulatory_sensing.md` (PRM-ANT) | 12 → 12 | AN 12 (Annex 1 IDs cited, never censused) | 69,234 B |
| MAK-FFC v1.1 | no primer — host law; every primer is `subordinate_to` it and cites SPINE/CF/PF/AF/EN/XC IDs | — | — | — |
| MAK-ELSM v1.1 | no primer — sourcing vocabulary; folded into every X8 table (verdict set + DEAD-REPLACE) | — | — | — |
| MAK-MIF v1.0 | no primer — coordination doctrine; beats cited in every Fabric-binding paragraph | — | — | — |
| MAK-DOT | no primer — FZ-1..6 absorbed by MAK-LWC (cited via MAK-LWC Part 8 only; GAP-LWC-004 asks Arch §14.5 to stop citing FZ) | — | — | — |
| MAK-J3 v0.9-proposed | no primer — GPP-1..16 land in PRM-CEC provisionally; move to a retired-citations list if MAK-J3 ratifies elsewhere (CEC Assumptions) | — | — | — |

**Totals:** 296 owned IDs declared, 296 mapped; +16 provisional GPP. Total primer text 751,715 B (761,743 B with the brief). Every Appendix A reports "Gap: none" for every family.

---

## 2. Cross-primer edge check

### 2.1 Edge table (X5 Emits → target primer's X5 Consumes, and the reverse)

Only edges whose target is another PRM- primer are listed; edges to 02_ primers (A, B, D, E, F, G, I, J, K, L), registers, `cdss-fabric`/`cdss-spine`, EHR hosts and the data plane are out of this check. "Y" = a matching row exists in the counterpart's table; "Y (partial)" = a row exists but names different content or a different source; "N" = no counterpart row.

| # | Source primer | Emits (X5 row) | Target primer | Matched consume | Note |
|---|---|---|---|---|---|
| 1 | LWC | Graded warrant-applicability + decode traces (FE-3, FE-6) | CEC | **Y** | CEC5 Consumes "PRM-LWC (fuzzy spine)" — checked "Consistent" |
| 2 | LWC | Codebook words + μ graphics via single CWW path; borderline flag (FE-6, FC-2) | HDC | **Y** | HDC5 Consumes "PRM-LWC (linguistic layer)" |
| 3 | LWC | same | TXC | **Y** | TXC5 Consumes "PRM-LWC (fuzzy layer)" |
| 4 | LWC | same | ABC | **Y (partial)** | ABC5 consumes FA-1/3/4/5 and FE-8 findings, not the compliance-codebook render itself; FS-4 compliance register implied |
| 5 | LWC | same | LBP, PRB | **Y (asymmetric)** | LBP5 and PRB5 both consume the decoder, but LWC5 names only the face-law primers as callers — LBP-F4 asks LWC's row to read "PRM-HDC (law) via PRM-LBP (renderer)" |
| 6 | LWC | FA-1 math traces, FA-3 drift, FA-4 projection, FA-5 diffs | ABC | **Y** | ABC5 Consumes "PRM-LWC (fuzzy spine)"; ABC-F5 pins ownership (LWC computes, RG-5 schema, ABC schedules MA-7) |
| 7 | CEC | Pinned GenericArgument templates with FS-8/FE-2 fields | LWC | **N** | LWC5 Consumes names PRM-CEC as template source; CEC5 Emits has no row to PRM-LWC — the hand-off exists only as `EVT-CEC-1 template.released` in CEC9 hook 5 |
| 8 | RWC | FitReport as RG-1 stage 3; ConflictRecords for stage 4 (ME-1, MS-5) | CEC | **Y** | CEC5 Consumes "PRM-RWC (meta-rational spine)" — envelopes, commitments, fit-judgments |
| 9 | RWC | Envelope status, gap affordances, conflict rendering, MA-1..5 | HDC | **Y** | HDC5 Consumes "PRM-RWC" (MC-1 weight parity carried into HR-3/HA-4/HA-5) |
| 10 | RWC | same | TXC | **Y (partial)** | TXC5 consumes envelopes "via `cdss-compiler`" (MS-1 on instruments/warrants) — not gap affordances or MP-1 render content directly |
| 11 | RWC | same (MA-1, MA-2, MA-4, MS-6, MS-8) | ABC | **Y** | ABC5 Consumes "PRM-RWC" |
| 12 | RWC | Fit-side typing of MS-9; MA-7 cross-wing findings; MX-5 confusion cases | LWC | **N** | LWC5 Consumes has no PRM-RWC row (LWC was written first, as exemplar) |
| 13 | RWC | Update-note pattern; S-1/S-2 signals | ANT | **Y** | ANT5 Consumes "Every series volume" names MAK-RWC Part 7 update notes explicitly |
| 14 | LWC | (RWC consumes) graded applicability for MC-4/MP-4; drift telemetry for MA-7 | RWC | **N** | RWC5 Consumes "PRM-LWC (sibling wing)" exists; LWC5 Emits has no PRM-RWC row — reverse of #12 |
| 15 | CEC | (RWC consumes) typed fit-signals QU-2 → ME-7; confirmed boundary-hunter findings | RWC | **N (partial)** | CEC5 Emits to RWC only "Unified telemetry (RG-5)" for MA-7; the QU-2 typed fit signal path to ME-7 is a CEC BUILD row ("typed double-duty router") with no emit row; CEC-F4 places the fit_signal at Primer F's interface |
| 16 | CEC | Evaluator-released arguments + stage traces + five signals | HDC / TXC / ABC (+ LBP, PRB via fabric) | **Y** | HDC5, TXC5, ABC5 each consume from PRM-CEC; LBP5 and PRB5 consume via the fabric read API |
| 17 | CEC | Unified telemetry (RG-5) | ABC, RWC (MA-7) | **Y** | ABC5 "PRM-CEC" row; RWC5 receives MA-7 inputs (from LWC row) — CEC named as schema owner throughout |
| 18 | CEC | RG-8 results, SBOM/tier diffs, DX-6 abstention rates as conformity/fork evidence | ANT (R30, R23) | **N** | ANT5 Consumes from PRM-ABC (AX-4 bundles) and Primer J only; ANT5 states gate bundles cite I's evidence "through AX-4, not through this component" — CEC routes direct, ANT expects via ABC |
| 19 | HDC | Recorded fit-judgment completing a flagged verdict (HA-4) | CEC | **Y (partial)** | CEC5 consumes "recorded fit-judgments (MS-7)" but attributes them to **PRM-RWC**, not PRM-HDC (the authoring face) |
| 20 | HDC | Act records, MA-4 compliance states, HE-2 telemetry | ABC | **Y (partial)** | ABC5 "PRM-HDC" row consumes Deviation objects and HG-4 hazards; HE-2 telemetry not named (ABC reads RG-5 from CEC) |
| 21 | HDC | The lawful specification the UI renders | LBP | **Y** | LBP5 Consumes "PRM-HDC (face law)" — budgets, weights, prohibited vocabulary, identity checklist |
| 22 | HDC | Sign-off record → patient projection (HA-1 → PF-8) | TXC | **Y** | TXC5 Consumes "PRM-HDC" — HA-1 and TR-3 agree on fail-closed default |
| 23 | ABC | Ratified suppression and meta-prompt rules; class-weight changes (HG-1/HG-3) | HDC | **N** | HDC5 Consumes "PRM-ABC" expects these; ABC5 Emits to HDC lists only lens-grant visibility (AL-4) and rebuttals — the ratified-rule hand-off is unclaimed on ABC's side |
| 24 | ABC | Lens-grant notice to affected clinician (AL-4); face-visible rebuttals | HDC | **N** | Reverse of #23 — HDC5 has no consume row for AL-4 notices |
| 25 | ABC | Acknowledgment → rebuttal published (AR-3, AR-5); AT-4 coverage-floor breaches | CEC / Primer G | **N** | CEC5 Consumes has no PRM-ABC row; CEC consumes confirmed findings from Primer G only. CEC-F5's default has PRM-ABC author map-iii rows into R8 — also absent from CEC5 |
| 26 | ABC | Systematic-misfit verdicts and clustered evidence → MS-4 detect (AR-5, AG-3, AT-1) | RWC | **N** | RWC5 Consumes has no PRM-ABC row (MS-4 detect inputs are listed from faces and PRM-CEC AD-3) |
| 27 | ABC | Ratification-stage records with FA-5 preview → curve-change workbench (AG-1, AG-2) | LWC | **N** | LWC5 Consumes has no PRM-ABC row; LWC4 only says the workbench "depends on MAK-FFC AF-5's governance roles" |
| 28 | ABC | Obligation status (AX-3), gate bundles (AX-4), signals for the watch log | ANT | **Y** | ANT5 Consumes "PRM-ABC" |
| 29 | ABC | ODR workflow state (AR-4) | TXC | **Y** | TXC5 Consumes "PRM-ABC" (TA-5) |
| 30 | TXC | Dispute entries (TA-5), values proposals (TA-2), council records (TA-4), completion hazards (TA-3) | ABC | **Y** | ABC5 Consumes "PRM-TXC" — but TXC5's Emits addresses these to "Fabric (meta-rational acts)", not PRM-ABC; content matches |
| 31 | TXC | Face telemetry under RG-5 (TE-2) | ABC | **Y (partial)** | ABC5 consumes telemetry from PRM-CEC's RG-5 row, not from TXC; TXC-F7/GAP-TXC-005 record that RG-5 does not enumerate patient-face streams |
| 32 | TXC | Intake, monitoring, escape-hatch content → Consult-Prep (TA-3 → HW-2/HA-6) | HDC | **Y** | HDC5 Consumes "PRM-TXC / PRM-PRB" |
| 33 | TXC | PIS profile custody edge (TW-5, TC-2) | LWC | **Y** | LWC5 Consumes "Patient (via PRM-TXC / PRM-PRB)"; TXC-F2 confirms GAP-LWC-002 (under PF-4, not PF-3) |
| 34 | TXC / PRB | Grounds (QuestionnaireResponse/Observation with modality, reliability) | LWC → CEC | **Y** | LWC5 Consumes "Data plane (grounds preparation) … PRM-TXC / PRM-PRB intake controls write the ground" |
| 35 | PRB | TE-1 instrumentation (comprehension, equity, calibration uptake) | TXC | **N** | TXC5 Consumes has no PRM-PRB row at all |
| 36 | TXC | (PRB consumes) PDA access ledger, consent state, routing explanation, export bundles | PRB | **N** | PRB5 records "PDA read/write API (shape unspecified in any volume — RECON-PRB-005)"; TXC5 Emits custody objects to the data plane, not to PRB; TXC RECON-TXC-007 similarly asks HDC for the sign-off schema — the PDA API is unowned on both sides |
| 37 | PRB, LBP, TXC, HDC | RG-5 telemetry streams (modality mix, budget spend, act latencies …) | ABC / CEC | **N** | No consume row on ABC or CEC names UI-originated telemetry; the sink is the unresolved telemetry-register ruling (§6, cluster R5) |
| 38 | LBP | CV-5 conflation kit and CA-5 results as conformity artifacts | HDC | **N** | HDC5 Consumes has no PRM-LBP row (HDC emits to LBP; the return path is unclaimed) |
| 39 | LBP | Acceptance tests the leg must pass (CA-5, CA-2) | LEG | **Y** | LEG5 Consumes "PRM-PRB / PRM-LBP (UIs)" |
| 40 | PRB | PA-6 suite results, SBOM, manifest | LEG | **Y (partial)** | PRB5 addresses them to "CI / conformity file (R25; MAK-ABC AX-3)", LEG5 consumes "the two conformance suites" — content matches, addressee differs |
| 41 | LEG | Register-scoped projections over one read API per face (L2-1) | HDC / TXC / ABC | **Y (seam)** | HDC5 consumes "`cdss-fabric` SPINE-9 read API" — and GAP-HDC-003 proposes the face gateway live in `cdss-fabric`, while LEG5 says the stack hosts the per-face gateways (TASK-LEG-003 builds a NestJS gateway skeleton). Three homes proposed for one component: LEG (stack), HDC (`cdss-fabric`), ABC-F1 (`cdss-fabric` module + `cdss-ui-auditor`) |
| 42 | LEG | Ops metrics on the unified schema (L6-3); standing evidence answers for AX-3 | ABC | **Y (partial)** | ABC5 consumes R3 SBOMs "Per-repo CI" and R30; not an ops-metrics row |
| 43 | CEC | (LEG consumes) tier manifests per build; telemetry schema artifact | LEG | **N** | CEC5 Emits has no row to PRM-LEG; GAP-CEC-003/004 place both as `cdss-spine` contracts — LEG5 flags this (GAP-LEG-001 / LEG-F6) |
| 44 | ABC | (LEG consumes) retention rules, bundle definitions, gate-bundle definitions | LEG | **N** | ABC5 Emits has no PRM-LEG row |
| 45 | LEG | Stack defaults, L1-2 bindings, vehicle decision (L1-3) | PRB, LBP | **N (formal)** | PRB5 and LBP5 both consume from PRM-LEG; LEG5 Emits has no row to either UI — the hand-off is the LEG8 binding map, not an X5 edge |
| 46 | LBP / PRB | Claims-inventory sources (in-product copy) | ANT | **N** | ANT5 Consumes "PRM-LBP / PRM-PRB / programme marketing"; neither UI primer emits copy to ANT |
| 47 | ANT | R30 posture: ASSUME-REG status, gate positions, tier labels | CEC, RWC, TXC, PRB, HDC, ABC, LEG, LBP | **Y** | Every primer's Register topology reads R30; ANT5 emits to R30 and "PRM-RWC / every volume" (validator findings) |
| 48 | HDC and LBP | Both claim to write the six clinical acts to `cdss-fabric` (HDC5 "Emits → cdss-fabric"; LBP5 "Emits → cdss-fabric") | fabric | **overlap** | Not unmatched — double-claimed. HDC is the law, LBP the writer; CONTRACT-ACT-1 (HDC8) should name one writer of record |

### 2.2 Unmatched edges — integration seams nobody has claimed

Nineteen edges have no counterpart row (rows marked **N** above, #37 and #45 counted once each):

1. **CEC → LWC pinned templates** (#7) — only in CEC9 hook 5, not X5.
2. **RWC → LWC** MS-9 fit typing, MA-7 joint review, MX-5 suite (#12).
3. **LWC → RWC** graded applicability for MC-4/MP-4, drift for MA-7 (#14). Items 2–3 mean the **two-wing coordination contract (MS-9) has no X5 row in PRM-LWC at all**; PRM-LWC needs an additive Consumes/Emits pair.
4. **CEC → RWC typed fit signals** (QU-2 → ME-7) (#15) — the router is a CEC BUILD with no emit row.
5. **CEC → ANT/R30/R23 conformity and fork evidence** (#18) — CEC routes direct, ANT accepts only via ABC AX-4.
6. **ABC → HDC ratified suppression / meta-prompt rules** (#23) — the HG-3 governance hand-off has no emitter.
7. **ABC → HDC lens-grant notice** (#24).
8. **ABC → CEC/G acknowledgment → rebuttal publication** (#25) — the AR-5 routing consequence lands nowhere in CEC5.
9. **ABC → RWC systematic-misfit → MS-4 detect** (#26).
10. **ABC → LWC ratification records → curve-change workbench** (#27) — FA-2's ratification stage has no producer named on either side.
11. **PRB → TXC TE-1 instrumentation** (#35).
12. **TXC ↔ PRB Personal Data Agent API** (#36) — unspecified on both sides (RECON-PRB-005); the PDA is a BUILD with no OSS champion (fasten-onprem archived 18 Jul 2026).
13. **UI/face telemetry → sink** (#37) — every face and UI emits RG-5 streams; no consume row names them; register home unresolved (§6).
14. **LBP → HDC CV-5 kit / CA-5 results** (#38).
15. **CEC → LEG tier manifests + telemetry schema** (#43) — GAP-CEC-003/004 vs GAP-LEG-001.
16. **ABC → LEG retention rules and bundle definitions** (#44).
17. **LEG → PRB/LBP stack defaults and vehicle decision** (#45) — no X5 row; LEG8 binding map only.
18. **LBP/PRB → ANT claims-inventory sources** (#46).
19. **Face-gateway home** (#41) — LEG, HDC and ABC each place the per-face projection gateway somewhere different; the same seam recurs as GAP-HDC-003, TASK-LEG-003 and ABC-F1.

Plus two partial-attribution seams worth a one-line fix: CEC5 attributes recorded fit-judgments to PRM-RWC rather than the authoring face PRM-HDC (#19); LWC5 names face-law primers, not the UI primers, as decoder callers (#5, LBP-F4).

### 2.3 Fabric binding — argument-slot claims

From each primer's "Fabric binding (MAK-FFC)" paragraph (X5 and X10):

| Slot | Claimed by | Assessment |
|---|---|---|
| **Claim** | PRM-CEC only — "the fabric's release … the only path by which a draft becomes a Claim" (SPINE-1/7). RWC, HDC, TXC, ABC, PRB, LBP, LEG, ANT each state "never a Claim / never releases" | **One claimant — clean.** |
| **Grounds** | PRM-TXC ("supplies the grounds slot … patient-reported data with provenance, capture context, modality and reliability"); PRM-PRB ("supplies grounds — the patient's answers … upstream of PRM-LWC's gradedness annotation"); PRM-LWC ("grounds gradedness — μ-vectors on grounds, SPINE-1's grounds slot") | **Claimed by three.** Coherent as a pipeline (PRB captures → TXC face law → LWC annotates additively per FS-2) but no primer states the layering as a single owner statement; PRB and TXC both say "supplies grounds". Ruling: TXC owns the slot's content law; PRB is the capture instrument; LWC adds annotation only. |
| **Warrant** | PRM-CEC ("the Warrant's compiled form — GenericArgument templates via CP-1"); PRM-LWC supplies "warrant-applicability grades (graded preconditions inside GenericArguments, EN-2)" | **One owner (CEC), one contributor (LWC) — coherent.** |
| **Backing** | **None of the ten.** PRM-CEC explicitly excludes it ("never … backing rows (Primer B)"); CEC5 consumes backing from Primer B via Primer A. | **Claimed by none** — owned by 02_ Primer B. The slot is nonetheless where HDC-F2 (Primer D `tier.{E,V}` vs fabric evidence tier) and CEC-F2 (SNout/red-flag rows as compiled warrants with E-tier backing) land; someone in the PRM set must own the rendered-tier mapping (RECON-HDC-004). |
| **Qualifier** | PRM-CEC ("the Qualifier's typing discipline, SPINE-2 via OM-3 — posterior and coverage are the Qualifier's content"); PRM-RWC ("joins the Qualifier with a typed fit status, ME-1"); PRM-LWC, TXC, PRB, LBP, LEG, ANT each "never the Qualifier" | **Two claimants — coherent** (fit is one of OM-3's five types). Two open items sit on this slot: **CEC-F7** (GPP `applicability` is not one of the five signal types) and **ABC-F3** (governance entries need a qualifier type; ABC proposes reusing `applicability`). Both point at the same missing ruling: is `applicability` a sixth type or an instance of Fit? |
| **Rebuttal** | PRM-CEC ("the Rebuttal slot's adversarial content — AD-2"); PRM-RWC ("feeds the Rebuttal slot — envelope narrowings and boundary-hunter findings via EN-5"); PRM-ABC's own review arguments carry "Rebuttal = the open dispute path (AR-4)" | **Claimed by two for clinical arguments** (CEC and RWC). Coherent if RWC's ME-2 findings enter through Primer G → AD-2 (CEC5 consumes G, not RWC, for rebuttals) — but edge #25/#26 show the ABC→CEC and ABC→RWC publication paths are unclaimed, so the rebuttal supply chain has one confirmed producer (CEC via AD-2) and two unconfirmed feeders. |
| **New fabric object classes** (not Toulmin slots) | PRM-RWC: GapReport, ConflictRecord, RemodelingProposal, TradingZoneArtifact, ApplicabilityEnvelope (MS-7). PRM-HDC: sign-off, Deviation (SPINE-8), fit-judgment, conflict navigation, boundary work (CONTRACT-ACT-1). PRM-TXC/PRB: GapReports, Goals, Consent. PRM-ABC: review states, dispute records, change proposals. | No slot conflict, but **none has a `cdss-spine` schema yet** — RWC-F4 (four contracts), GAP-HDC-005 (CONTRACT-ACT-1), RECON-ABC-001 (review-item), RECON-PRB-003 (`PatientProjection`, `NotificationPayload`), TXC8 `PatientGround` + content-class discriminator. See cluster R1b. |

MAK-MIF beat coverage across the fabric-binding paragraphs: beats 1 (LWC, RWC shared, HDC, LBP), 2 (LWC, RWC shared, HDC, TXC, PRB, LBP), 3 (LWC, RWC shared, ABC, LEG, ANT), 4 (RWC, HDC, ABC, LBP), 5 (RWC, HDC, LBP), 6 (LWC, TXC, PRB, LEG), 7 (RWC, ABC), 8 (RWC, ANT); CEC claims all eight. Every beat has at least two primers; none is orphaned.

---

## 3. Consolidated findings

### 3.1 All 81 findings

Axis codes as filed: P4-i internal, P4-e ecosystem, P4-x external. "Default" = the primer proposed a default ruling. "Joins" = other primers' findings on the same object.

| ID | Axis | One-line summary | Default | Joins |
|---|---|---|---|---|
| LWC-F1 | P4-e | Arch §14.5 enters fuzzy layer at L4 per DEC-05; MAK-LWC LW-P0..P5 is level-agnostic — reconcile LW-P0 as L3 harness, face render at L4 | Y | RWC-F1, HDC-F1, LBP-F1, TXC-F1, PRB-F2, ABC-F4 (level alignment) |
| LWC-F2 | P4-e | Primer D §D2 gateway admits *fragments*; a LinguisticVariable/FML artifact is a new type — add artifact-type discriminator | Y | TXC-F3, RWC-F7, CEC-F6, CEC5 (templates), PRB5 (language packs), ABC5 (template versions) |
| LWC-F3 | P4-e | Primer A `findings[]` has no μ field; FE-5 coupling needs `graded: {term, mu, fml_version}` + template `coupling_map` | N (schema shape stated) | CEC-F1 |
| LWC-F4 | P4-i | FA-3 drift telemetry has no register home (GAP-LWC-001) | N | RWC GAP-002, HDC-F7, TXC-F7, ABC-F5, LBP-F6, PRB-F4 |
| LWC-F5 | P4-x | IEEE 1855 revision under discussion; scikit-fuzzy 2 years; py4jfml located, activity unverified | — | (currency) |
| RWC-F1 | P4-e | Arch §14.5 has no meta-rational row; propose additive row R0–R2 at L3, R3–R4 at L4 | Y | LWC-F1 cluster; GAP-RWC-006 |
| RWC-F2 | P4-x / P1 | **MAK-RWC Part 9 ELSM-R01 records alibi-detect as Apache-2.0; LICENSE is BUSL-1.1 since v0.11.5** — corpus row false at its own verification date | Y (ADAPT + erratum) | CEC-F8; ABC X8 row still says Apache-2.0 ADOPT |
| RWC-F3 | P4-x | openregulatory/templates is CC BY-NC-SA 4.0 (non-commercial); MAK-RWC says ADAPT "per repo LICENSE.md" | Y (STUDY) | ABC-F6; CEC and ANT rows still ADAPT |
| RWC-F4 | P4-e | Arch §14.2 `cdss-spine` contract list lacks GapReport/Envelope/ConflictRecord/RemodelingProposal schemas — propose CONTRACT-ENV/GAP/CONF/REMODEL-1 | Y | GAP-HDC-005, RECON-ABC-001, RECON-PRB-003, RECON-LBP-001, RECON-CEC-001 |
| RWC-F5 | P4-e | Primer I §I8/§I10 has no "ontology/envelope remodeling" change class for MS-4/ME-5 | Y | CEC5 (Primer I edge), RECON-RWC-004 |
| RWC-F6 | P4-e | Primer J §J9 card lacks population/cohort/failure-region block ME-6 needs — add `applicability:` block | Y | RECON-RWC-005 |
| RWC-F7 | P4-e | Primer D §D8 fragment carries partial envelope fields but no ApplicabilityEnvelope or `unknown` state — `envelope_ref` at gateway, one ruling with LWC-F2 | Y | LWC-F2, TXC-F3, CEC-F6 |
| RWC-F8 | P4-e | MX-4/Part 7 read Bedrock → Baseten; Arch §11.4 still names Bedrock (C-03, DEC-03 ESCALATED) | N (recorded) | LEG-F1, ANT-F5 |
| RWC-F9 | P4-x | Giskard 3.0.0 rewrite (WATCH); MAPIE 1.5.0, TweetyProject 1.31 confirmed; PCCP via Federal Register; TGA via secondary source; evidently date conflict | — | CEC-F9 |
| RWC-F10 | P1 | MAK-RWC Appendix A JSON stamped `"version": "1.0"` inside a v1.1 document | Y (erratum) | — |
| CEC-F1 | P4-e | Primer A §A8 trace lacks backing/rebuttals/fit slots and graded ground; OM-2 draft must wrap it | Y | LWC-F3 |
| CEC-F2 | P4-e | Primer A's red-flag/SnNout override layer is rule logic outside CP-1; represent as compiled warrant nodes, `tier` a claim not a verdict | Y | HDC-F2 (backing tier) |
| CEC-F3 | P4-e | **RG-6 puts Bayesian differential + conformal in J-2 only; Arch §9 says J-1/J-2 identical downstream of coding** — substantive tier-composition difference | Y (read J-2 list as "ML runtime"; argued deviation vs RG-6) | PRB-F1, TXC-F8, ABC-F10, LBP production topology (J-3 manifest) |
| CEC-F4 | P4-e | Primer F emits set + coverage only, no typed fit signal; strata not QU-3's subgroup schema | N (interface stated) | RWC5 (ME-7 consume), RECON-CEC-004 |
| CEC-F5 | P4-e | Primer G rulebook has no rows for AD-1 maps ii/iii and no AD-5 coverage telemetry — CE-P4 exit unreachable from G as written | Y (RWC/ABC author rows into R8) | GAP-CEC-002, edge #25 |
| CEC-F6 | P4-e | Primer D's OPA gate chain releases fragments to render outside RG-1's five stages — a structural second gate | Y (fold D's checks into stages 1/3) | LWC-F2, RWC-F7, TXC-F3, HDC-F1 |
| CEC-F7 | P4-e | GPP-9 `applicability` qualifier is none of OM-3's five types — treat as Fit instance, not sixth type | Y | ABC-F3 |
| CEC-F8 | P4-x | alibi-detect BUSL-1.1 (duplicate confirmation of RWC-F2) | Y | RWC-F2 |
| CEC-F9 | P4-x | netcal landmine resolved (1.4.0); CQL translator 5.0.0 major; Giskard 3.0.0 seven days old; ART 14 months; tga.gov.au unfetchable; ELSM-R rows resolve in MAK-RWC not MAK-ELSM | — | RWC-F9 |
| HDC-F1 | P4-e | Arch §14.5 L2 "verbatim render surface" read literally violates HR-1; amend wording to "verbatim render inside released claims" | Y | LBP-F1, LWC-F1 cluster |
| HDC-F2 | P4-e | Primer D `tier:{E,V}` and MAK-FFC Backing evidence tier are two vocabularies meeting at the face | Y (`tier.E` = evidence tier) | CEC-F2; §2.3 Backing slot |
| HDC-F3 | P4-e | HW-4 narrative generation vs Primer L L7/L3 (posture-gated, L5) — two paths; deterministic path satisfies HW-4 from L3 | Y | HDC-F4, TXC-F4 (Primer L edges) |
| HDC-F4 | P4-e | Primer L L6 critic / L5 sentinel are interruptions outside HG-1's four classes — admit as fifth class via MS-4 at L5 | Y | HDC-F3 |
| HDC-F5 | P4-i | HW-1 act list omits fit-judgment (HA-4) and boundary work (HA-6) that Part 4 mandates | Y (erratum) | LBP-F2 |
| HDC-F6 | P4-i | Four unnamed SHOULD→MUST elevations in MAK-HDC Part 7 map (CF-8, FC-4, MC-4, MC-6) | Y (erratum: label "elevated") | ABC-F9 |
| HDC-F7 | P4-i | HE-2 telemetry, fabric ledger, face gateway have no register/repo homes (GAP-HDC-001..003) | N | LWC-F4 cluster; ABC-F2; edge #41 |
| HDC-F8 | P4-x | CDS Hooks 2.0.1 is STU; client-js 12 months; openmrs year inferred; WCAG 2.2 current; HAPI 8.10.0 retires cqf-ruler | — | LBP-F7 |
| TXC-F1 | P4-e | Arch enters patient face at L3 as J-3-safe subset; MAK-FFC P3 presumes renderer; **MAK-TXC has no phase table** (AN-7 requires one) | Y (split P3 into L3/L4 slices) | PRB-F2, GAP-TXC-004 |
| TXC-F2 | P4-e | GAP-LWC-002 confirmed: PIS custody sits with TXC under **PF-4** (TC-2), not PF-3 as PRM-LWC cites | Y (PRM-LWC citation correction) | LWC GAP-002 |
| TXC-F3 | P4-e | Questionnaires, codebook packs, plain templates are three more non-fragment artifact types at D's gateway | Y (with LWC-F2) | LWC-F2 cluster |
| TXC-F4 | P4-e | Primer L L8 elicitation must inherit TW-2/TW-3 non-coercion on the *answer* path | Y | HDC-F3/F4 |
| TXC-F5 | P4-x | android-fhir SDC last release Nov 2024; fhircore 2.2.2; fasten archived; RapidPro AGPL new candidate; FHIR R5 Consent FMM 2 | — | PRB-F3/F7, LEG-F4 |
| TXC-F6 | P4-e | TE-1 real-patient evaluation vs GATE-002 identifiable-data gate — pre-register before, fieldwork after | Y | PRB production topology |
| TXC-F7 | P4-i | RG-5 does not enumerate patient-face streams; no register for patient-face telemetry (GAP-TXC-001/005) | N | LWC-F4 cluster |
| TXC-F8 | P4-e | TW-4 own-observation feedback is *not* J-3-safe (GPP-4 excludes monitoring feedback) — must be structurally absent in J-3 variant | N (design stated) | PRB-F1, CEC-F3 |
| ABC-F1 | P4-e | Arch §14.2 has no repo and §14.4 no PFX for the auditor face — `cdss-fabric` module + thin `cdss-ui-auditor`, PFX ABC | Y | ANT-F7, GAP-HDC-003, GAP-LEG-006 |
| ABC-F2 | P4-i | Fabric ledger unnumbered; remodeling/review records are governance-grain vs Primer I's engineering-grain R12 — R31 + R32 or grain discriminator | Y | GAP-HDC-002, GAP-RWC-001, LEG-F6, PRB GAP-001 |
| ABC-F3 | P4-e | OM-3 has no qualifier type for a governance verdict; reuse GPP-9 `applicability` | Y | CEC-F7 |
| ABC-F4 | P4-e | Arch §14.5 puts external projection at L5 — too late for GATE-003 evidence; bundles v0 at L4 | Y | LWC-F1 cluster |
| ABC-F5 | P4-e | Drift telemetry touched by MAK-ABC AT-1, MAK-LWC FA-3, MAK-CEC RG-5 with no owner of record — LWC computes, RG-5 schema, ABC schedules | Y | LWC-F4, GAP-ABC-003 |
| ABC-F6 | P4-x | openregulatory CC BY-NC-SA 4.0 — commercial manufacturer use needs legal reading | Y (STUDY) | RWC-F3 |
| ABC-F7 | P4-x | ELSM-19 cites Trillian; Trillian is in maintenance mode, Tessera recommended; Rekor v2 on Tessera | Y (reference-set update) | LEG (ledger pattern row), RECON-ABC-006 |
| ABC-F8 | P4-x | Ketryx pricing page tiers Free/Startup/Business/Enterprise; annex names "Essentials" — route as AN-6 signal | Y (signal, not amendment) | ANT-F2 (W-3) |
| ABC-F9 | P4-e | Elevations FA-6→AR-3, MA-5→AX-1 recorded | — (no action) | HDC-F6 |
| ABC-F10 | P4-e | J-3 artifact: AF-4 shadow-mode only, GPP-16 flag; RG-6 manifest should record compiled AT analytics | N (design stated) | CEC-F3 cluster |
| PRB-F1 | P4-e | PS-2/PC-3 diary reflection is MUST; GPP-4 forbids monitoring feedback in J-3 — need per-profile capability manifest | Y (GAP-PRB-007) | TXC-F8, CEC-F3, ABC-F10 |
| PRB-F2 | P4-e | MAK-PRB has no phasing table (AN-7); P0/P1/P2 plan proposed as erratum | Y | TXC-F1 |
| PRB-F3 | P4-x | **google/android-fhir has moved to `ohs-foundation/android-fhir`**; ELSM-04 and TXC ELSM-T01 cite the old org | Y (provenance erratum; OBL-005 supplier item) | LEG-F4 |
| PRB-F4 | P4-i | Patient-act dispositions, notification deliveries, sync conflicts have no register (GAP-PRB-001..003) | N | LWC-F4 cluster |
| PRB-F5 | P4-e | PC-1 "single governed library" vs MAK-LEG L1-3 two vehicles — read as one library per vehicle | Y | LEG-F3 |
| PRB-F6 | P4-e | PI-2 additive conflict (both kept + flag) is not a CRDT merge (MAK-LEG L4-3); yjs STUDY | — | LEG L4 rows |
| PRB-F7 | P4-x | WCAG 2.2 current, 3.0 WATCH; fhircore 10 months; PouchDB not selected; RapidPro AGPL; fasten archived | — | TXC-F5 |
| PRB-F8 | P4-i | TA-5 dispute entry has no PV/PS/PC/PI/PA carrier — reserve a tray state | — (informative) | TXC TA-5 row, ABC AR-4 |
| LBP-F1 | P4-e | Arch §14.5 L2 v0 vs HR-1 MUST — holds by construction at L2, proven by CA-5 at L3 | Y | HDC-F1 |
| LBP-F2 | P4-e | Act list widens CF-1 → HW-1 → CI-2; HW-1 under-inclusive vs HDC Part 4 — build to CI-2, erratum to HW-1 | Y | HDC-F5 |
| LBP-F3 | P4-x/e | CDS Hooks 2.0.1 `indicator` is a severity traffic-light; map only to interruption class weight, never a signal | Y | HDC-F8, RECON-LBP-004 |
| LBP-F4 | P4-i | PRM-LWC names face-law primers as decoder callers; the UI is the caller | Y (LWC row wording) | edge #5 |
| LBP-F5 | P4-i | Shared Stage-Trace strip (CC-5 / MAK-ABC AL-2) needs one owning package or it is fork-by-copy | Y | RECON-LBP-005 |
| LBP-F6 | P4-i | CA-5 conformity artifacts, budget telemetry, identity sheet have no register (GAP-LBP-001..003) | N | LWC-F4 cluster |
| LBP-F7 | P4-x | WCAG 2.2, CDS Hooks STU, npm versions confirmed; Vale licence unconfirmed | — | HDC-F8 |
| LEG-F1 | P4-e | Arch §11.4 Bedrock vs RG-7/TASK-REG-009 Baseten (C-03 / DEC-03) — rule authoring-time and runtime separately | Y | RWC-F8, ANT-F5 |
| LEG-F2 | P4-x | **Redis ≥ 8.0 is RSALv2 / SSPLv1 / AGPLv3** (7.2.x BSD-3); Valkey (BSD-3) ADOPT as recorded LS-1 substitution | Y | — |
| LEG-F3 | P4-e | L1-1 treats the two UI libraries as symmetric; patient UI is Blocked beyond intake/consent | — (DoD adjusted) | PRB-F5, TXC-F1 |
| LEG-F4 | P4-x | android-fhir org move; **fhircore v2.2.2 dated 10 Nov 2024 on releases page vs "Nov 2025" in ELSM-05 / TXC ELSM-T02** — unadjudicated | Y (ELSM erratum) | PRB-F3, TXC-F5 (TXC fetched "10 Nov 2025"), PRB RECON-002 |
| LEG-F5 | P4-e | Amplify demo lane vs CodePipeline regulated lane — regulated pipeline must be the only path to non-synthetic data | Y | — |
| LEG-F6 | P4-i | Tier manifests, ledger attestations, residency policy, fabric ledger have no register (GAP-LEG-001..003) | N | ABC-F2, GAP-CEC-003 |
| LEG-F7 | P4-e | DEC-04 ledger substrate pending; build Aurora/PostgreSQL default as interim StackChoice | Y | ABC-F7, RECON-CEC-008 |
| LEG-F8 | P4-x | Next.js 15 EOL 21 Oct 2026; Node 20 EOL 30 Apr 2026; TypeScript 7.0.2 — pin Next 16 / Node 24 | Y | — |
| ANT-F1 | P4-x | FDA CDS guidance re-issued 29 Jan 2026 + 11 Mar 2026 town hall; series anchors 6 Jan only — log S-4 | Y | W-1 |
| ANT-F2 | P4-x | Ketryx "Essentials" tier absent from vendor page — signal W-3, potential amendment of WATCH-REG-004 | Y | ABC-F8 |
| ANT-F3 | P4-x | IEC 62304 Ed.2 expected Aug–Sep 2026, not confirmed published — STD-002 edition may change inside the window | Y | W-2 |
| ANT-F4 | P4-e | R30 declared versioned; AN-6 signal log is additive; Arch §12.1 law 2 forbids mixed class — versioned R30 + append-only sub-ledger (or R31) | Y | GAP-ANT-001; **R31 numbering collision with GAP-HDC-002 / GAP-ABC-001** |
| ANT-F5 | P4-e | Arch §11.4 Bedrock line is an AN-8 quarantined framing without its update note | Y | LEG-F1, RWC-F8 |
| ANT-F6 | P4-e | MAK-FFC Part 8 / MAK-J3 cite TGA/FDA directly (pre-MAK-ANT); whitelist via SRC-REG-001 / S-3; no standalone REG-POSTURE file staged | Y | RECON-ANT-002 |
| ANT-F7 | P4-i | R30 owner "governance" = `cdss-governance` shared with Primer J — explicit module boundary | Y | ABC-F1 |
| ANT-F8 | P4-x | TGA consultation closed May 2024; no legislative amendment located; 7 Oct 2025 guidance rewrite is the visible outcome | — | — |

Counts: LWC 5 · RWC 10 · CEC 9 · HDC 8 · TXC 8 · ABC 10 · PRB 8 · LBP 7 · LEG 8 · ANT 8 = **81**. By axis: P4-e 44 · P4-i 14 · P4-x 22 · P1-only 1 (RWC-F10). Defaults proposed on 56.

### 3.2 Rulings requested — ten operator decisions

Each cluster resolves the findings listed; the default is the one the primers proposed (where they agree) or the strongest-argued one (where noted).

**R1a — Knowledge-plane gateway: artifact types, envelope reference, and the gate chain's relation to RG-1.**
Resolves LWC-F2, TXC-F3, RWC-F7, CEC-F6, HDC-F1 (partly), plus CEC5's template row, PRB5's language-pack inheritance and ABC5's template-version emit. RECON-LWC-002 = RECON-TXC-001 = RECON-CEC-003 = RECON-RWC-002.
*Default proposed (LWC, TXC, CEC, RWC agree):* Primer D's fragment schema gains an artifact-type discriminator admitting FML artifacts, GenericArgument templates, FHIR Questionnaires, codebook/language packs and plain-register templates; "bounds" for a non-fragment is its envelope; fragments and bundles carry an `envelope_ref` resolving to a spine-schema ApplicabilityEnvelope; D's five OPA checks execute *inside* RG-1 stage 1 (hash/tier/currency) and stage 3 (bounds/context) so there is one gate. CEC states the alternative (compiler as gateway with D's signing reused) is equally coherent; confidence low-medium across all four primers.

**R1b — The `cdss-spine` contract set.**
Resolves RWC-F4, GAP-HDC-005, RECON-ABC-001, RECON-PRB-003, RECON-LBP-001, RECON-CEC-001, RECON-HDC-001/007, GAP-CEC-003/004, GAP-LEG-004.
*Default proposed:* ratify, beside CONTRACT-ARG-1 (carrying OM-2's slots and the five non-coercible signal types), the following additive contracts: CONTRACT-ENV-1, -GAP-1, -CONF-1, -REMODEL-1 (RWC); CONTRACT-ACT-1 (HDC8 shape); review-item/verdict/proposal (ABC8 shape); `PatientGround` + content-class discriminator (TXC8); `PatientProjection<ReleasedArgument>` + `NotificationPayload` (PRB8); `ClinicianRenderInput` / register-render contract (LBP8); `StackChoice` (LEG8); `SignalEntry` + assumption-state (ANT8); the RG-5 telemetry schema and RG-6 tier manifests as versioned spine contracts stamped in R1. Every one is marked Proposed in its primer; none is corpus text.

**R2 — Level alignment: Arch §14.5 additive errata.**
Resolves LWC-F1, RWC-F1, HDC-F1, LBP-F1, TXC-F1, PRB-F2, ABC-F4, LEG-F3; GAP-LWC-004, GAP-RWC-006, GAP-CEC-007, GAP-TXC-004, GAP-PRB-006, GAP-LBP-005; RECON-LWC-005, RECON-HDC-005, RECON-LBP-007.
*Default proposed:* (i) fuzzy row cites MAK-LWC FS/FC/FP/FA/FE/FX not FZ-1..6, LW-P0 as L3 harness, face rendering at L4 per DEC-05; (ii) new "Meta-rational layer" row — schema in harness L2, envelopes + flagged path (R0–R2) L3, remodeling lifecycle (R3–R4) L4, meta-level evidence (R5) L5; (iii) clinician row reworded "v0 (verbatim render inside released claims)" at L2 and "one-surface negative tests gating (HE-4/CA-5)" at L3, split into HDC and LBP checkpoints; (iv) patient row: MAK-FFC P3 split into J-3-safe L3 slice and ASSUME-REG-003-gated L4 slice, with MAK-TXC and MAK-PRB each gaining a phasing table marking GATE-000/GATE-002; (v) auditor row: AX-1/AX-2 bundles v0 at L4 for GATE-003, external projection at L5; (vi) CE-P0..P5 named against L1–L4 as in CEC's Production topology annotation.

**R3 — Engine-plane contracts at the A/F/G boundaries and the qualifier type registry.**
Resolves LWC-F3, CEC-F1, CEC-F2, CEC-F4, CEC-F5, CEC-F7, ABC-F3; RECON-CEC-002/004/005/009, RECON-LWC-006.
*Default proposed:* Primer A's §A8 record becomes the payload inside the OM-2 draft with `findings[].graded: {term, mu, fml_version}` mirrored by the template `coupling_map`; SNout/red-flag library rows compile as warrant nodes (`local-rule`/`guideline-rule`) with E-tier backing and `tier` becomes a claim type; Primer F gains a `fit_signal` output and a QU-3-extensible stratum schema; Primer G's R8 gains map-ii rows (authored by PRM-RWC) and map-iii rows (by PRM-ABC) plus an AD-5 telemetry hook; `applicability` (GPP-9) is ruled an instance of OM-3's **Fit** type rather than a sixth signal, and governance entries (ABC) use it as their qualifier.

**R4 — J-tier composition and the J-3 (GPP) profile.**
Resolves **CEC-F3** (the most consequential single finding), PRB-F1, TXC-F8, ABC-F10; GAP-PRB-007; RECON-CEC-006.
*Default proposed (CEC, confidence low-medium):* read MAK-CEC RG-6's J-2 list as "ML runtime" components in REG-POSTURE's sense — a library-parameterised Bayesian calculator and a conformal quantile are deterministic arithmetic and are J-1-eligible alongside the evaluator, consistent with Arch §9 ("downstream of coding, the two runtimes are identical"), Primer A §A1 and Primer F §F9 — and file an argued deviation against RG-6's wording via MAK-CEC's change policy. Until ruled, PRM-CEC builds to RG-6 as filed and CE-P5 tier manifests are blocked. Companion decisions: a per-profile capability manifest in `cdss-spine`, diffed in CI like the SBOM, under which PS-2/PC-3 (diary reflection), TW-4, the posterior/coverage identities and the Graded Criterion Chip/Qualifier Block are structurally absent in the GPP build; AF-4 shadow-mode and GPP-16 flags recorded in the RG-6 manifest. The operator may instead read RG-6 literally (J-1 without a differential) — the two readings produce different supplied artifacts and different FORK-REG-001 evidence.

**R5 — Register homes: R31, R32, and one telemetry register.** See §6 for the consolidated proposals.
Resolves LWC-F4, HDC-F7, TXC-F7, ABC-F2, ABC-F5, PRB-F4, LBP-F6, LEG-F6, ANT-F4; all telemetry/ledger GAPs.
*Default proposed:* R31 Justification Fabric Ledger (owner `cdss-fabric`, opens L2, append-only) absorbing the verdict ledger (GAP-CEC-001); R32 Remodeling & Review Ledger (opens L4, append-only) or R12 with a mandatory `change_class`/grain discriminator; **one** append-only Telemetry Register keyed by RG-5 schema version with a stream discriminator (drift, circumrational load, gap analytics, campaign coverage, interruption budget, act latency, patient-face modality/floor) — R13 stays clinician acceptance telemetry; R30 versioned plus a separately declared append-only signal sub-ledger. **Numbering collision to resolve:** GAP-ANT-001 also proposes "R31 Regulatory Signal Log".

**R6 — Repository homes and namespace prefixes (Arch §10, §14.2, §14.4).**
Resolves ABC-F1, ANT-F7, LBP-F5, LEG-F7 (repo side); GAP-LWC-003, GAP-RWC-005, GAP-CEC-006, GAP-HDC-003/004, GAP-TXC-003, GAP-ABC-005/006, GAP-PRB-005, GAP-LBP-004, GAP-LEG-005/006, GAP-ANT-002; RECON-ABC-002, RECON-ANT-007, RECON-LBP-005, RECON-PRB-006.
*Default proposed:* new repos `cdss-fuzzy` (LWC), `cdss-meta` (RWC), `cdss-ui-auditor` (thin, ABC), `cdss-infra` and `cdss-dataplane` (LEG); the face gateways (clinical projection, Consult-Prep composer, budget governor, act writers) and the auditor read model/projector/assemblers as `cdss-fabric` modules (HDC, ABC) — **but LEG's TASK-LEG-003 builds the per-face gateway in the stack**; regulatory sensing as `cdss-governance/regulatory-sensing/`; a shared stage-trace-strip package owned by whichever face ships first. PFX additions: FUZ, MRL, CEC (+ CMP for compiler-local), ABC, LEG, ANT; UIC covers LBP and UIP covers both PRB and TXC (or HDC/TXC join the PFX set) — TASK-<suffix>-n IDs in all ten primers are declared interim.

**R7 — Licence rulings before dependency freeze.** See §5.2 for the full exposure list.
Resolves RWC-F2, CEC-F8, RWC-F3, ABC-F6, LEG-F2, TXC-F5/PRB-F7 (RapidPro), LWC RECON-003/004; RECON-RWC-003, RECON-CEC-007, RECON-ABC-004, RECON-TXC-003, RECON-PRB-004, RECON-LEG-002/004, RECON-LBP-006.
*Default proposed:* alibi-detect ADAPT with legal review (CI-only vs supplied-artifact use) — corpus erratum; openregulatory/templates STUDY only, re-author independently; Valkey (BSD-3) as the recorded LS-1 substitution for Redis ≥ 8; RapidPro STUDY until AGPL network-copyleft ruling for a hosted SMS/IVR tier; pyfuzzylite commercial licence vs GPL-3.0 for the shipped fuzzy runtime (simpful AFL-3.0 as fallback); pyFUME offline-only; immudb only if BUSL-1.1 clears; TweetyProject pinned ≥ 1.6 (LGPL); JuzzyPython, py4jfml, Vale, lforms, openmrs-esm-core licences confirmed before any use beyond reading.

**R8 — Architecture decision queue: DEC-03 (inference substrate), DEC-04 (ledger substrate), DEC-05 (fuzzy entry).**
Resolves LEG-F1, RWC-F8, ANT-F5, LEG-F7, ABC-F7; RECON-LEG-001/002/005, RECON-CEC-008, RECON-LWC-005, RECON-ABC-006.
*Default proposed:* DEC-03 — rule authoring-time harness/K/L calls (Bedrock-via-PrivateLink under Primer-I change control) separately from release-path runtime inference (Baseten-class, ASSUME-REG-004-gated), and attach the AN-8 update note to Arch §11.4 naming TASK-REG-009; DEC-04 — Aurora PostgreSQL + transparency-log pattern with the ELSM-19 reference set updated to Tessera / Rekor v2 (Trillian is in maintenance mode), immudb as the BUSL-gated alternative; DEC-05 — ratify fuzzy-layer L4 entry substantially as §14.5 proposes.

**R9 — 02_ primer extensions (I, J, L) that the wings and faces depend on.**
Resolves RWC-F5, RWC-F6, HDC-F3, HDC-F4, TXC-F4; RECON-RWC-004/005.
*Default proposed:* Primer I §I8 gains one row "Ontology / envelope / metric remodeling (MS-4)" → G suite (ME-2) + ME-5 replay via RG-4 + distributional gate + MS-4 record in R12, with the FML class as a sub-row; Primer J's card gains an `applicability:` block mirroring the MS-1 field list; HW-4 is realised by the deterministic codebook path from L3 and Primer L L7/L3 are additive at L5 under HR-1/SPINE-3; L6 critic and L5 sentinel enter HG-1 as a fifth interruption class by MS-4 record at the L5 gate; L8's reply path emits `PatientGround` with `modality = llm-elicited`, raw utterance preserved, and a new Primer L G-family corruption row "LLM-structured reply scalarises a hedged answer".

**R10 — Clinician-face act list, CDS Hooks card mapping, and elevation labelling.**
Resolves HDC-F5, LBP-F2, LBP-F3, LBP-F4, HDC-F6, ABC-F9, PRB-F5, PRB-F6, PRB-F8; RECON-LBP-004.
*Default proposed:* build to MAK-LBP CI-2 (confirm, sign off, deviate, report gap, judge fit, navigate conflict, free-text annotation) and file an additive erratum to MAK-HDC HW-1 adding fit-judgment and HA-6 free text — no MAK-FFC change; CDS Hooks `indicator` maps only to interruption class weight (hard-stop → `critical`, advisory → `info`/`warning`), never to any of the five signals, and a summary-only host gets a link-out; MAK-HDC Part 7 map labels CF-8/FC-4/MC-4/MC-6 rows "elevated"; PC-1 read as one governed library per vehicle bound to the same content artifacts and PA-6 suite; the acknowledgment-tray state enum reserves a dispute class.

**Operator-bearing signals (not rulings — AN-6 reserves bearing assessment to the operator):** ANT W-1 (FDA re-issue 29 Jan 2026, ANT-F1), W-2 (IEC 62304 Ed.2, ANT-F3), W-3 (Ketryx tier wording, ANT-F2 / ABC-F8), W-4 (TGA AI guidance reinforced; SaMD an enforcement priority 2026–27), TXC-F6 (TE-1 timing vs GATE-002), LEG-F5 (Amplify lane), ANT-F6 (citation whitelist for pre-MAK-ANT host text), ANT-F8.

### 3.3 Errata proposed to source volumes

| # | Volume · location | What is wrong | Evidence | Filed by |
|---|---|---|---|---|
| 1 | MAK-RWC v1.1 Part 9 ELSM-R01; Appendix C | alibi-detect recorded Apache-2.0, ADOPT. Actual: **BUSL-1.1 from v0.11.5 (22 Jan 2024)**, Change License Apache-2.0 four years per release. False at the corpus's own verification date | GitHub LICENSE + PyPI classifier fetched 2026-09-02 (two independent fetches) | RWC-F2, CEC-F8 |
| 2 | MAK-RWC v1.1 Part 9 ELSM-R04; Appendix C | openregulatory/templates "license per repo LICENSE.md", ADAPT. Actual: **CC BY-NC-SA 4.0** (non-commercial) | LICENSE.md fetched 2026-09-02 | RWC-F3, ABC-F6 |
| 3 | MAK-RWC v1.1 Appendix A (JSON) | `"version": "1.0"` inside a v1.1 document; Appendix C says 1.1 | Document read | RWC-F10 |
| 4 | MAK-ELSM v1.1 ELSM-04; MAK-TXC Part 8 ELSM-T01 | Cite `google/android-fhir`; canonical repo is now **`ohs-foundation/android-fhir`** (google/ redirects); also an OBL-005 supplier-assessment item | GitHub redirect + Google docs, fetched 2026-09-02 | PRB-F3, LEG-F4 |
| 5 | MAK-ELSM v1.1 ELSM-05; MAK-TXC Part 8 ELSM-T02 | fhircore v2.2.2 recorded "Nov 2025" (re-verified 2026-09-01). LEG's releases-page fetch reads **10 Nov 2024**; PRB got one fetch rendering "2024" and a landing-page reading of 2025; TXC's fetch reads 10 Nov 2025. **Unadjudicated** — GitHub omits the year on sub-12-month dates | Three primers, conflicting fetches 2026-09-02 | LEG-F4, PRB RECON-002, TXC-F5 |
| 6 | MAK-ELSM v1.1 §04 ELSM-19 | Reference set "trillian, rekor designs" — Trillian README: **maintenance mode, recommends Tessera**; Rekor v1 maintenance, v2 on Tessera. Pattern verdict unchanged; reference set stale; DEC-04 must not target Trillian APIs | Trillian v1.7.3, Rekor v1.5.2, Tessera v0.2.0 pages fetched 2026-09-02 | ABC-F7 |
| 7 | MAK-CEC v1.1 Part 9 landmine "netcal slow-moving (v1.3.6 Aug 2024)" | Resolved — netcal **1.4.0 released 16 Apr 2026**; ADAPT → ADOPT, vendoring contingency unnecessary | PyPI JSON 2026-09-02 | CEC-F9 |
| 8 | MAK-CEC v1.1 Part 9 / Appendix C citation surface | Cites ELSM-R01/R02/R04 as if in MAK-ELSM; they resolve in MAK-RWC Part 9 / Appendix C | Cross-check | CEC-F9 |
| 9 | MAK-FFC v1.1 Part 8; MAK-J3 frontmatter `regulatory_anchors`; MAK-ANT Part 4 S-3 | FDA CDS guidance anchored 6 Jan 2026 only; FDA records **re-issue 29 Jan 2026** and an 11 Mar 2026 town hall — anchor string incomplete | fda.gov guidance + town-hall pages fetched 2026-09-02 | ANT-F1 (W-1) |
| 10 | MAK-ANT Annex 1 WATCH-REG-004 (by ID) | Names a Ketryx "Essentials" tier as validated-out-of-the-box; vendor page shows Free/Startup/Business/Enterprise and "validation evidence on request". Annex cannot be edited — handle as signal W-3, potential amendment | ketryx.com/pricing fetched 2026-09-02 (ABC, LEG, ANT independently) | ANT-F2, ABC-F8 |
| 11 | MAK-ANT Annex 1 STD-002 (by ID) | IEC 62304 Ed.2 reported in final coordination, publication expected Aug–Sep 2026; not confirmed published — edition may change inside the currency window | Quickbird 19 Jun 2026; no publication record found 2026-09-02 | ANT-F3 (W-2) |
| 12 | MAK-HDC v1.0 HW-1 | Act enumeration omits fit-judgment (HA-4) and boundary-work capture (HA-6), both MUSTs in Part 4; MAK-LBP CI-2 lists them | Text comparison | HDC-F5, LBP-F2 |
| 13 | MAK-HDC v1.0 Part 7 consolidation map | Four SHOULD/MAY → MUST elevations (CF-8→HW-4, FC-4→HW-2, MC-4→HA-5, MC-6→HG-1/HG-3) not labelled "elevated" per the map's own convention (Appendix B check 6) | Text comparison | HDC-F6 |
| 14 | MAK-TXC v1.0 Part 7; MAK-PRB v1.0 Part 7 | No phasing table, though MAK-ANT AN-7 requires every volume's table to mark gate dependencies | Document read | TXC-F1, PRB-F2 (GAP-TXC-004, GAP-PRB-006) |
| 15 | Architecture §14.5 "Fuzzy layer" row | Cites "FZ-1..6"; superseded by MAK-LWC FS/FC/FP/FA/FE/FX on ratification (MAK-LWC `absorbs`) | Document read | GAP-LWC-004 |
| 16 | Architecture §11.4 | Names Amazon Bedrock via PrivateLink — an AN-8 quarantined framing without its update note naming TASK-REG-009 / ASSUME-REG-004 (C-03 / DEC-03 already flagged in §14.6) | Document read | ANT-F5, LEG-F1, RWC-F8 |
| 17 | Architecture §14.2 / §14.4 | No repo or PFX for the auditor face; no repo for FHIR data plane or IaC; PFX set lacks fuzzy, meta-rational, plane, stack, sensing prefixes | Document read | ABC-F1, GAP-LEG-006, all PFX GAPs |
| 18 | MAK-LWC v1.1 Part 9 landmine "Py4JFML activity not verified" | Repo located (`cmencar/py4jfml`); activity still unverified — status update, not error | GitHub search 2026-09-02 | LWC-F5 |
| 19 | PRM-LWC v1.0 (primer, not volume) GAP-LWC-002 and LWC5 Consumes row | Cites MAK-FFC **PF-3** for PIS custody; MAK-TXC TC-2 places it under **PF-4** (FS-9 reserves PF-3 for value-to-weight mappings) | MAK-TXC TC-2, TW-5; MAK-LWC FS-9 | TXC-F2 |
| 20 | PRM-LWC v1.0 (primer) LWC5 Emits row to faces | Names PRM-HDC/TXC/ABC as decoder callers; the UI primers (LBP CC-3, PRB PC-3) make the call — should read "PRM-HDC (law) via PRM-LBP (renderer)" | MAK-LBP CC-3; MAK-HDC Part 0 | LBP-F4 |

Internal inconsistency inside the primer set (not a volume erratum, but the operator will trip on it): **PRM-ABC's X8 row for alibi-detect still records "Apache-2.0 · ADOPT (machinery)"**, while PRM-RWC and PRM-CEC fetched BUSL-1.1 the same day; PRM-CEC's and PRM-ANT's openregulatory rows still carry "per repo LICENSE.md · ADAPT" while PRM-RWC and PRM-ABC read CC BY-NC-SA 4.0. ABC's row should be corrected additively before any ADOPT is acted on.

---

## 4. Consolidated open questions (operator-facing, deduplicated)

**Register homes** (→ §6 and cluster R5)
- Where does the justification fabric ledger itself live in the RoR — R31, or a ruling that the fabric is the substrate *of* registers and exempt? (GAP-HDC-002, GAP-ABC-001, LEG-F6, RWC register annotation)
- Governance-grain remodeling/review/dispute records vs Primer I's engineering-grain R12 — R32 or a grain discriminator? Where do curve-change ratifications (PRM-LWC writes R12), pack locality reviews (GAP-PRB-004) and patient-act dispositions (GAP-PRB-001) go? (ABC-F2, GAP-RWC-001)
- One telemetry register for all wings, faces and UIs, or R13 extensions? Who is producer of record for drift telemetry? (GAP-LWC-001, GAP-RWC-002, GAP-HDC-001, GAP-TXC-001/005, GAP-ABC-003, GAP-LBP-002, GAP-CEC-002/004, ABC-F5)
- R30 mutability: versioned plus an append-only signal sub-ledger, or a separate register — and which number, given R31 is already claimed twice? (GAP-ANT-001, ANT-F4)
- Verdict ledger (RG-2): R11 extension or new register owned by `cdss-fabric`? (GAP-CEC-001)
- Homes for versioned configuration artifacts: tier manifests (GAP-CEC-003 / GAP-LEG-001), identity sheet (GAP-LBP-003), trading-zone charters (GAP-RWC-003), StackChoice (GAP-LEG-004), metric & mapping definitions (GAP-ABC-004), claims inventory (GAP-ANT-003), TL-5 boundary document (GAP-TXC-002), residency policy (GAP-LEG-003), watch schedule owners (GAP-ANT-006), anchor-currency outcomes (GAP-ANT-004), GPP obligations register (GAP-CEC-005), ledger attestations (GAP-LEG-002), notification deliveries and sync-conflict queue (GAP-PRB-002/003), conformity-file R25→R23 mapping (GAP-LBP-001).

**Namespace prefixes** (Arch §14.4; cluster R6)
- Ratify FUZ (LWC), MRL (RWC), CEC + CMP (CEC), ABC, LEG, ANT; decide whether HDC/TXC join the PFX set or file under UIC/UIP with a scope tag; confirm UIC = LBP, UIP = PRB (+TXC). All TASK-<suffix>-n IDs in the ten primers are interim aliases. (GAP-LWC-003, GAP-RWC-005, GAP-CEC-006, GAP-HDC-004, GAP-TXC-003, GAP-ABC-005, GAP-PRB-005, GAP-LBP-004, GAP-LEG-005, GAP-ANT-002)

**Repo homes** (Arch §10, §14.2; cluster R6)
- `cdss-fuzzy`, `cdss-meta`, `cdss-ui-auditor`, `cdss-infra`, `cdss-dataplane` — new, or absorbed by `cdss-fabric`/`cdss-governance`? (LWC/RWC execution tables, ABC-F1, GAP-LEG-006)
- Where does the per-face projection gateway live — stack (LEG TASK-LEG-003), `cdss-fabric` (GAP-HDC-003), or `cdss-fabric` module + UI (ABC-F1)? Three primers, three answers. (edge #41)
- Does the evaluator live in `cdss-fabric` ("evaluator wrap" row) or its own repo? (CEC Assumptions)
- Regulatory sensing as `cdss-governance/regulatory-sensing/` or a new repo? (ANT-F7, RECON-ANT-007)
- Owner of the shared stage-trace-strip package (LBP-F5); writer of record for the six clinical acts (HDC vs LBP, edge #48); PDA API owner (RECON-PRB-005).
- Component owners: every execution table carries `component owner [NEEDS DEFINITION]`; RWC additionally a clinical-safety owner for MA-2 findings; ABC and ANT a regulatory owner for AX-3/AX-4 and R30 writes.

**Licence rulings** (cluster R7; §5.2)
- alibi-detect BUSL-1.1: CI-only vs supplied J-2 artifact use, or commercial quote/alternative detector. (RECON-RWC-003, RECON-CEC-007)
- openregulatory/templates CC BY-NC-SA 4.0: is a commercial manufacturer's QMS documentation "commercial use"? (RECON-ABC-004)
- Redis ≥ 8 tri-licence vs Valkey for any redistributable/in-country image. (RECON-LEG-004)
- RapidPro AGPL-3.0 for a hosted SMS/IVR tier. (RECON-TXC-003, RECON-PRB-004)
- pyfuzzylite GPL-3.0/commercial for the shipped fuzzy runtime; pyFUME GPL offline. (RECON-LWC-003)
- immudb BUSL-1.1 if DEC-04 prefers it. (RECON-LEG-002)
- Unknown/unconfirmed: JuzzyPython, py4jfml, JFML, FisPro, pyDecision, FCMpy, Vale, lforms, openmrs-esm-core, argumentative-llms.

**Regulatory assumptions** (all OPEN; no primer may close them — MAK-ANT AN-3)
- ASSUME-REG-003 (patient face beyond intake/consent/logistics) — blocks TXC TR/TW-4/TA/TE-1/TE-3 scope and PRB P1 screens at L4; is GPP-4's subset the accepted reading of "intake/consent/logistics"? (TXC, PRB, LEG-F3; RECON-TXC-005, RECON-PRB-001)
- ASSUME-REG-004 (Baseten Sydney dedicated deployment) — Sydney not publicly listed; written confirmation required; DEC-03 pending. (LEG-F1, RWC-F8, ANT-F5, RECON-LEG-005)
- ASSUME-REG-006 (Ketryx as lifecycle system of record) — tier wording drift (W-3). (ABC-F8, ANT-F2, RECON-ABC-005, RECON-ANT-006)
- GATE-000 (counsel) governs regulated-tooling configuration and the L4 patient decision; GATE-002 precedes any identifiable data anywhere — TE-1, HE-1, MC-7, DX-5/QU-3 real-data validation all wait. (TXC-F6, HDC/RWC/CEC production topology)
- Does a standalone REG-POSTURE file exist anywhere (MAK-ANT LLM contract rule 2)? None staged. (RECON-ANT-002)
- tga.gov.au refuses automated fetch — SRC-REG-001..004 currency must be checked manually; IEC 62304 Ed.2 status at every STD-002 ticket. (RECON-ANT-004/005, CEC-F9)
- Row-level carrier map (103 annex IDs vs 15 family rows) does not yet exist. (RECON-ANT-003, GAP-ANT-005)
- CEC-F3's J-1 composition question is also a FORK-REG-001 evidence question (which artifact produces Level-3 abstention evidence).

**Schema / contract pins** (cluster R1b)
- CONTRACT-ARG-1 pinned with OM-2 slots and five non-coercible types (RECON-LWC-001, RECON-CEC-001, RECON-HDC-001, RECON-LBP-001).
- Primer A `findings[].graded`, `fit`/`backing`/`rebuttals` slots; Primer F `fit_signal`; Primer G map-ii/iii rows; Primer I remodeling class; Primer J `applicability:` block; Primer D artifact-type discriminator + `envelope_ref` (RECON-CEC-002/003/004/005, RECON-RWC-002/004/005, RECON-TXC-001).
- Envelope schema shape (MS-1 gives a field list, not a schema); GapReport FHIR binding is `{{UNSOURCED — operator to confirm}}` (RWC8 — the only UNSOURCED marker in the set).
- HA-1 sign-off record schema (RECON-TXC-007); PDA API shape (RECON-PRB-005); register-render contract and `PatientProjection` (RECON-PRB-003); SDC extension for hesitant/sentinel answers (RECON-TXC-002, RECON-PRB-007); FHIR R4 vs R5 for Consent granularity (RECON-TXC-004 — a PRM-LEG ruling).
- Ratified encounter-class taxonomy, reading budgets, interruption class weights, prohibited-vocabulary list and its owner (RECON-HDC-006, RECON-LBP-002/003); trading-zone charters per change class before first L4 ratification (RECON-ABC-007).
- SPINE-9 register API exists in `cdss-fabric` — HR-1 depends on a host SHOULD (RECON-HDC-002).
- Version pins: CQL translator 4.9.0 vs 5.0.0 (major API change); TypeScript 7.x peer ranges vs Next 16 / NestJS 12; Node 24; CDS Hooks 2.0.1 STU pinned in the card adapter; cosign 3.x (v4 flag removals). (CEC-F9, RECON-LEG-003, LBP-F3/F7)
- Every X8 "proposed tolerances" paragraph (10 primers) is flagged for clinical/governance sign-off; none is a corpus number except MAK-LBP CS-1's ninety-second read and CI-1's interaction count of one.

---

## 5. Asset library totals

### 5.1 Per primer and grand total

Rows counted by parsing each X8 table (header `| Asset | Type | Satisfies | Licence | Currency | Verified | Verdict |`). **Primary verdict** = first verdict token in the Verdict cell (e.g. "ADOPT; WATCH revision" counts as ADOPT; "DEAD-REPLACE → STUDY" counts as DEAD-REPLACE). "Multi" = rows carrying more than one verdict token. **Verified this run** = Verified cell dated 2026-09-02 or "this run"; **Carried** = Verified cell says carried / not re-fetched / not verified / not separately fetched; **Build/internal** = BUILD rows and research/theory rows whose verification is a corpus or primer citation only. Where the primer's own Appendix B / coverage-check count differs, it is shown in brackets.

| Primer | Rows | Verified this run | Carried | Build/internal-cited | ADOPT | ADAPT | STUDY | BUILD | WATCH | DEAD-REPLACE | Multi |
|---|---|---|---|---|---|---|---|---|---|---|---|
| LWC | 23 | 5 | 7 | 11 | 4 | 3 | 7 | 8 [primer says 9] | 1 | 0 | 4 |
| RWC | 29 [28] | 7 [8] | 10 | 12 | 8 | 4 | 4 | 11 [12] | 2 | 0 | 5 |
| CEC | 35 | 16 [13 load-bearing] | 10 | 9 | 15 | 8 | 2 | 10 | 0 | 0 | 10 |
| HDC | 21 | 9 [6 fetched] | 4 | 8 | 10 | 0 | 2 | 8 | 0 | 1 | 4 |
| TXC | 22 [24] | 9 [8] | 4 | 9 | 7 | 1 | 3 | 10 | 0 | 1 | 5 |
| ABC | 27 | 13 [11] | 5 | 9 | 8 | 3 | 7 | 8 | 1 | 0 | 7 |
| PRB | 31 [30] | 20 [17] | 1 | 10 | 10 | 3 | 6 | 11 | 1 | 0 | 2 |
| LBP | 24 | 11 [10] | 4 [3 + 2 not verified] | 9 | 10 | 3 | 1 | 9 | 1 | 0 | 4 |
| LEG | 36 | 23 | 8 | 5 | 27 | 2 | 0 | 4 | 2 | 1 | 6 |
| ANT | 23 [24] | 9 | 4 | 10 | 6 | 2 | 0 | 10 | 5 | 0 | 5 |
| **Total** | **271** | **122** | **57** | **92** | **105** | **29** | **32** | **89** | **13** | **3** | **52** |

Notes on the discrepancies: RWC/TXC/PRB/ANT self-counts differ from parsed rows by ±1–2 (ANT's "24" likely includes the four post-currency WATCH signal rows W-1..W-4, tabled separately; TXC's "24" is unexplained). LWC's "9 BUILD" and RWC's "12 BUILD" each count one row whose primary verdict is ADAPT but whose cell says a sub-component "remains BUILD" (LWC pyDecision → HFLTS; RWC likely the Ketryx/remodeling split). The three DEAD-REPLACE rows are cqf-ruler (HDC), fasten-onprem (TXC; PRB carries it as STUDY-cautionary), and AWS QLDB (LEG). Assets that appear in several primers (HAPI FHIR ×6, WCAG 2.2 ×4, android-fhir/fhircore ×5, alibi-detect ×3, evidently ×3, TweetyProject ×3, openregulatory ×4, Ketryx ×5, immudb ×3, MAPIE ×2, Giskard/ART ×3, RapidPro ×2, CDS Hooks/sandbox/client-js ×2, Playwright/axe/Storybook/React Aria ×2) are counted once per primer, so 271 rows ≈ 200 distinct assets.

Coverage: every primer's P5 coverage-check paragraph reports every requirement family covered — 43/43, 42/42, 38/38 + 16/16, 30/30, 28/28, 27/27, 27/27, 26/26, 23/23, 12/12.

### 5.2 Licence exposure list

Every asset any primer flagged as GPL / AGPL / BUSL / SSPL / CC-NC / RSAL or with an unknown or unconfirmed licence, with the primer(s) and the requirement(s) served. Commercial assumption-gated services are listed at the end for completeness.

| Asset | Licence as found | Primer(s) | Requirement(s) served | Verdict(s) |
|---|---|---|---|---|
| SeldonIO/alibi-detect (ELSM-R01) | **BUSL-1.1** since v0.11.5 (RWC, CEC fetched); ABC row still says Apache-2.0 | RWC, CEC, ABC | ME-7 OOD, MA-7 drift; QU-2; AT-1 | ADAPT + legal review (RWC, CEC); ADOPT (ABC — stale) |
| openregulatory/templates (ELSM-R04 / SRC-REG-010) | **CC BY-NC-SA 4.0** (RWC, ABC fetched); CEC/ANT rows "per repo LICENSE.md" | RWC, ABC, CEC, ANT | MX-4, MA-5; AG-1, AX-4; RG-7, GPP-2; AN-10, STD-001..004 records | STUDY (RWC, ABC); ADAPT (CEC, ANT — stale) |
| Redis ≥ 8.0 | **RSALv2 / SSPLv1 / AGPLv3** tri-licence (≤ 7.2.x BSD-3) | LEG | L4-1 cache | ADAPT; Valkey (BSD-3) ADOPT as LS-1 substitution |
| rapidpro/rapidpro | **AGPL-3.0** | TXC, PRB | TL-1/TL-2 SMS/IVR intake; PA-2 modality tier | ADAPT/STUDY pending legal |
| Grafana OSS (dashboards) | AGPLv3 (CloudWatch alternative under AWS terms) | LEG | L6-3 ops lens | ADOPT (any) — lens discipline is the binding |
| codenotary/immudb (ELSM-17) | **BUSL-1.1** | CEC, ABC, LEG | RG-2 verdict ledger alt; AL-1/AL-3 alt; L3-2 alt | ADAPT only if BUSL clears legal |
| fuzzylite/pyfuzzylite | **GPL-3.0 + commercial dual** | LWC, CEC | FE-1, FE-2, FE-9 runtime; OM-7 fuzzy ommatidia, RG-1 stage 2 | ADAPT — licence review before LW-P0 freeze |
| CaroFuchs/pyFUME | **GPL-3.0** | LWC | FE-4 draft-curve generator (offline) | ADAPT — offline only |
| babylonhealth/counterfactual-diagnosis (ELSM-13) | **GPL-3.0 + patent application** | CEC | DX-5 evaluation baseline | STUDY ONLY — never ship |
| fastenhealth/fasten-onprem (ELSM-21) | **GPL-3.0**; archived 18 Jul 2026 | TXC, PRB | TC-1 design mine; PS-5 design mine | DEAD-REPLACE → STUDY (cautionary) |
| TweetyProject (ELSM-07) | **LGPL-3.0 ≥ v1.6; GPL-3.0 before** | RWC, CEC, ABC | MS-5 conflict semantics; RG-1 stage 4; AR-1/AR-4 | ADAPT — pin ≥ 1.6 |
| LUCIDresearch/JuzzyPython | **none surfaced in repo** | LWC | FE-7 general type-2 | STUDY — licence must be confirmed |
| cmencar/py4jfml | not surfaced (verify); commit log unfetchable | LWC | FS-1 from Python | STUDY |
| sotillo19/JFML | per repo (verify) | LWC, ABC | FS-1 FML I/O; AG-2 diff substrate | ADOPT as reference impl — licence unconfirmed |
| FisPro (CRAN) | per CRAN (unstated) | LWC | FS-1 drafting, FA-2 design reference | STUDY/ADOPT authoring-side |
| Valdecy/pyDecision; SamvelMK/FCMpy | per repo (unstated) | LWC | FA-5 ranking, MDT view; authoring aids | ADAPT / STUDY |
| ANFIS lineage; demo-grade medical fuzzy repos | various (unstated) | LWC | FE-4 alternatives; negative examples | STUDY |
| CLArg-group/argumentative-llms (ELSM-09) | "see repo" (unstated) | RWC, CEC | ME-4 gap mining; CP-5 proposal pipeline | ADAPT authoring-time only |
| lhncbc/lforms (NLM) | NLM terms — confirm | PRB | PS-1 alternative renderer | STUDY |
| errata-ai/vale | MIT per repo — not surfaced on releases page | LBP | CV-4 prohibited-vocabulary lint engine | ADAPT — confirm before CI dependency |
| openmrs/openmrs-esm-core (ELSM-H03) | "open source (MPL-2.0 per convention — verify)" | HDC, LBP | HW-5 low-resource host; CA-2 host candidate | STUDY/ADAPT |
| smart-on-fhir/client-js (ELSM-H02) | Apache-2.0 per MAK-HDC; not shown on releases page | HDC, LBP | HW-1, HW-5, CA-2 SMART vector | ADOPT (confirm maintenance) |
| Ketryx-on-Jira (KTX-001..012) | commercial; ASSUME-REG-006 OPEN | RWC, CEC, ABC, LEG, ANT | MX-4, RG-7, AG-1/AX-3/AX-4, L6-2, AN-4/AN-6 | WATCH / ADAPT contingent — never architecture |
| Baseten Sydney dedicated deployments | commercial; ASSUME-REG-004 OPEN; Sydney not publicly listed | RWC, CEC, LEG, ANT | MX-4, RG-7, L6-2 | WATCH contingent |

---

## 6. Register proposals consolidated

57 GAP items filed (LWC 4 · RWC 6 · CEC 7 · HDC 5 · TXC 5 · ABC 6 · PRB 7 · LBP 5 · LEG 6 · ANT 6). Deduplicated into nine rulings; namespace/repo/phasing GAPs are in §3.2 clusters R2 and R6.

**6.1 R31 — Justification Fabric Ledger.** Proposed independently by GAP-HDC-002 and GAP-ABC-001 (owner `cdss-fabric`; opens L2 with the evaluator wrap; append-only; written by the evaluator and the faces' governed writes; read by all three faces). LEG-F6 and RWC's register annotation both note the fabric is hosted but unnumbered. **Fold in GAP-CEC-001** (verdict ledger — the evaluator's RG-2 verdicts + stage traces are fabric entries; R11 stays render-attempt grain). **Collision:** GAP-ANT-001 also proposes "R31 Regulatory Signal Log" — assign the signal log a different number (see 6.4). One ruling: R31 exists, or the fabric is declared the substrate *of* registers and exempt from RoR enumeration.

**6.2 R32 — Remodeling & Review Ledger, or R12 with a grain discriminator.** GAP-ABC-002 (governance-grain: MS-7 entries, AR verdicts, AR-4 outcomes, AG stage records; opens L4) vs GAP-RWC-001 (R12 extension with `change_class: ontology`) vs PRM-LWC's practice of writing curve-change adjudications to R12. Also-affected: GAP-PRB-001 (patient-act disposition states: received / being-reviewed / outcome, plus a reserved dispute class per PRB-F8) and GAP-PRB-004 (language-pack locality-review records → R12). ABC-F2's argument: Primer I §I1 makes R12 the engineering change-control record; mixing grains blurs both AE-1 reconstruction and I's record. One ruling: R32, or R12 with a mandatory grain discriminator.

**6.3 One Telemetry Register (proposed R33) — the most-duplicated gap.** Six primers propose a home for telemetry: GAP-LWC-001 (FA-3 semantic drift per LinguisticVariable), GAP-RWC-002 (MS-3 circumrational load + MA-2 gap analytics — explicitly "one telemetry register for both wings rather than two"), GAP-HDC-001 (HE-2: interruption-budget spend, act latencies, drill-down, reading-budget adherence), GAP-TXC-001 + GAP-TXC-005 (TE-2: modality mix, escape-hatch and gap-report rates, dial usage, acknowledgment latency, floor conformance — and RG-5's enumerated streams do not name them), GAP-ABC-003 (drift, gap pressure, RG-5 unified, AD-5 coverage), GAP-LBP-002 (interruption-budget spend), GAP-CEC-002 (AD-5 campaign-coverage register beside R8) and GAP-CEC-004 (the RG-5 schema itself as a `cdss-spine` contract). Every one says "same shape as GAP-LWC-001" or "one ruling covering both". **Proposed single ruling:** one append-only Telemetry Register owned by `cdss-fabric` (or `cdss-corruption` for the AD-5 sub-stream), keyed by RG-5 schema version (the schema being a versioned `cdss-spine` contract extended with patient-face and UI streams), with a stream discriminator {drift, circumrational-load, gap-analytics, campaign-coverage, interruption-budget, act-latency, patient-face-modality/floor, cost/latency, calibration/coverage, abstention}; rendered only on the auditor system lens (RG-5, AF-8); R13 remains "clinician accept/modify/reject". Producer of record per stream per ABC-F5 (LWC computes drift; CEC owns schema; ABC owns the MA-7 review schedule).

**6.4 R30 extensions and mutability.** GAP-ANT-001 / ANT-F4: R30 is declared versioned (Arch §14.3) but AN-6's signal log is additive and §12.1 law 2 forbids a mixed class — ruling: R30 versioned (annex pin, carrier map version, ASSUME-REG state, jurisdiction-map reviews) plus a separately declared append-only signal sub-ledger (number it R34, not R31). Sub-tables/extensions also proposed for R30: claims inventory `claims_inventory@version` (GAP-ANT-003), anchor-currency outcomes — confirm R30 not R25 (GAP-ANT-004), `watch_schedule` {WATCH-REG id, cadence, owner, last_checked} (GAP-ANT-006), GPP obligations register with named owners (GAP-CEC-005), residency/routing policy (GAP-LEG-003 — or a governance-owned Residency Policy Register), metric & mapping definitions (GAP-ABC-004 — or a new versioned register), TL-5 boundary document cross-reference (GAP-TXC-002, primary home R25). GAP-RWC-004: R30 must be ratified before MX-1's "never mark an ASSUME-REG closed" is machine-checkable.

**6.5 Versioned configuration artifacts as `cdss-spine` contracts stamped in R1.** GAP-CEC-003 (RG-6 tier manifests — CEC) vs GAP-LEG-001 (R3 extension storing manifest + diff beside each SBOM, or a PRM-CEC-owned Tier Manifest Register) — one ruling; GAP-CEC-004 (RG-5 schema); GAP-LBP-003 (identity sheet as pinned artifact — R1 + R2, stored per MAK-LEG L5-2); GAP-RWC-003 (trading-zone charters — spine-owned register or R25/R26 sub-table); GAP-LEG-004 (StackChoice — R25 interim, Stack Choice Register if too coarse); GAP-PRB-007 (per-profile UI capability manifest, diffed in CI like the SBOM).

**6.6 Runtime append ledgers with no home.** GAP-LEG-002 (ledger anchor-check and replay-attestation results — Ledger Attestation Register owned by `cdss-fabric`, or R11 extension; interim R25; MAK-ABC AX-3 standing queries need it); GAP-PRB-002 (notification payload/delivery log evidencing the PS-4/PI-3 payload law — append-only, runtime-owned, opens PRB-P0); GAP-PRB-003 (PI-2 sync-conflict review queue — R13-adjacent register or fabric annotation class).

**6.7 Conformity-file routing.** GAP-LBP-001: CA-5 (and by extension PA-6, HE-4, TE-4, AE-4, RG-8) results write R25 as build evidence and are *mapped* into R23 by the regulatory owner under MAK-ABC AX-3 retention — never double-written.

**6.8 Custody confirmation — resolved.** GAP-LWC-002 (PIS profile custody) is confirmed by TXC-F2: patient-custodied meta-data under MAK-TXC TC-2 / MAK-FFC **PF-4**, not a register row (Arch §12.1 law 4); PRM-LWC's citation of PF-3 to be corrected additively.

**6.9 Not registers, recorded to prevent second paths.** TXC and PRB: grounds, Consent, AuditEvent, GapReports, Goals and PIS profiles are data-plane/fabric objects keyed by R1 stamps, not register rows; LBP: R11 is not read directly (fabric projection only); PRB: R13 not written (patient acts go to the fabric), R17 not read.

---

## 7. Self-audit summary (Appendix B, run 2026-09-02)

| Primer | Checks | Pass | Fail | Notes recorded inside a Pass |
|---|---|---|---|---|
| LWC | 10 | 10 | 0 | 7 exclusions / 7 owners; 23 rows, 9 BUILD (parsed: 8) |
| RWC | 10 | 10 | 0 | 9 exclusions / 9 owners; 28 rows [parsed 29], 12 BUILD [parsed 11], 8 fetched; **1 `{{UNSOURCED}}` marker** (GapReport data-plane binding) flagged for operator; RWC-F10 census stamp noted under check 9 |
| CEC | 10 | 10 | 0 | 11 exclusions / 11 owners; 35 rows, 10 BUILD, 13 load-bearing verified; 38 + 16 provisional GPP |
| HDC | 10 | 10 | 0 | 10 exclusions / 10 owners; 21 rows, 8 BUILD, 6 fetched, 4 carried, 1 DEAD-REPLACE; elevations noted (HDC-F6) |
| TXC | 10 | 10 | 0 | 10 exclusions / 10 owners; 24 rows [parsed 22], 10 BUILD, 8 re-fetched |
| ABC | 10 | 10 | 0 | 11 exclusions / 11 owners; 27 rows, 8 BUILD, 11 fetched; MUST/SHOULD 21/6 matches source; Ketryx routed as AN-6 signal |
| PRB | 10 | 10 | 0 | 10 exclusions (9 owners + 1 declared-silent: visual identity); 30 rows [parsed 31], 11 BUILD, 17 verified, 1 carried |
| LBP | 10 | 10 | 0 | 10 exclusions / 10 owners (no direct 02_ border, stated); 24 rows, 9 BUILD, 10 verified, 3 carried, 2 not verified (WATCH/owner-elsewhere) |
| LEG | 10 | 10 | 0 | 8 exclusions / 8 owners; 36 rows, 4 BUILD, 2 DEAD-REPLACE, 2 WATCH; MUST/SHOULD/MAY 10/8/5 matches source; two-layer integrity (defaults ≠ law) honoured |
| ANT | 10 | 10 | 0 | 8 exclusions / 8 owners; 24 rows [parsed 23 + 4 W rows], 10 BUILD; annex non-reproduction checked by reading every mention; 7 ASSUME-REG stated OPEN |
| **Total** | **100** | **100** | **0** | Every primer: eleven sections in order, epigraph verbatim with only the position sentence varied, census parity, trace lines present, subordination held, cross-doc IDs resolve, additive-only v1.0 |

Confidence blocks: every primer rates its BUILD verdicts *high* (no precedent found by the volume's search, MAK-ELSM's, and this run's), its fetched external rows *high*, its carried rows *medium*, and its assumption-gated commercial rows (Ketryx, Baseten) *low*; every level-alignment default is *medium*; every gateway/schema default (LWC-F2 family) is *low-medium* — "either is coherent; default stated".

---

## Blocking items for the operator (in dependency order)

1. **CEC-F3 / cluster R4** — J-1 composition (RG-6 vs Arch §9). Blocks CE-P5 tier manifests, the J-3 artifact's shape, FORK-REG-001 evidence and every UI's per-tier component manifest. Nothing else in the set changes the supplied artifact this much.
2. **Cluster R1a** — gateway artifact type + gate chain. Blocks TASK-CEC-003, TASK-LWC-001's definition-of-ready, TXC instrument installation, PRB language packs, ABC template feedback.
3. **Cluster R1b / CONTRACT-ARG-1** — every primer's first task has a definition-of-ready that reads "CONTRACT-ARG-1 pinned or local placeholder recorded".
4. **Cluster R5 / §6.3** — one telemetry ruling; six primers are waiting on the same decision and all currently degrade to "local placeholder".
5. **DEC-03 / DEC-04 / DEC-05** (cluster R8) — LEG cannot pin the ledger substrate or the inference substrate; LWC cannot enter L4.
6. **Licence rulings** (cluster R7) — alibi-detect, openregulatory, Redis/Valkey, RapidPro, pyfuzzylite must be ruled before the L3 dependency freeze; PRM-ABC's alibi-detect row must be corrected first.
7. **ASSUME-REG-003/004/006 and GATE-000/002** — not rulings the programme can make; every primer stops at the same wall and says so.
