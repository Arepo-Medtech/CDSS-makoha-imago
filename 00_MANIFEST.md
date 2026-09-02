---
doc_id: MANIFEST-IMAGO
title: "Makoha Imago v1.1 — Artifact Manifest, Availability Report, Production Sequence, Completeness Audit"
date: "2026-09-01"
status: "Added. This manifest indexes the complete artifact repository; it does not supersede the Mākoha corpus MANIFEST.md (precedence law), which governs its own fifteen volumes and is preserved verbatim in 03_."
---

# 1. Artifact manifest (84 files)

| Dir | Contents | Files | Disposition |
|---|---|---|---|
| 00 | this manifest | 1 | Added |
| 01_north-star-and-transformation | MET-1 v1.0 (verbatim) · MET-1.1 delta · MET-2 conflicts C-01..C-12 + decisions DEC-01..DEC-12 · MET-3 traceability · MET-4 gaps G-01..G-11 + roadmap | 5 | Retained + Added |
| 02_cdss-stack-augmented | all 21 CDSS originals, each **byte-exact preserved + additive annex**: Primer 0 §11 · Arch §14 · A10 B10 C10 D10 E10 F10 G10 H11 I10 J11 · J-1 §8 · J-2 §7 · K10 L10 · Harness §10 · Annex H-1 §10 · integration-report addendum 2 · complete-stack regeneration notice · diagrams HTML comment | 21 | Existing/Retained + Transformed/Added (annexes Proposed) |
| 03_makoha-butterfly-corpus | 15 corpus volumes + MANIFEST + 16 artifacts-html — **verbatim, zero edits** (append-only law; MAK-FFC hosts; REG-POSTURE governs regulatory content) | 32 | Existing/Retained |
| 04_hardening | MT2 directive (verbatim) · HARDEN-2 spec (CC-1..CC-8 class bars) · HARDEN-3 worklist (waves W0–W11) · HARDEN-1 R29 ledger seed (rows 0–73, **all PENDING; row 0 BLOCKED**) | 4 | Retained + Proposed |
| 05_registers-and-contracts | R29 schema (md+json) · R30 schema+seed · CONTRACT-ARG-1 (with DEV-1/RRI-1) | 4 | Proposed |
| 06_repositories | REPO-MAP v2 (14 existing + 4 proposed + GPP channel) · 4 skeleton READMEs | 5 | Retained + Proposed |
| 07_deployment-and-operations | DEPLOY-1 sequencing · DEPLOY-2 acceptance (8 added criteria) · OPS-1 · GOV-1 · SEC-1 | 5 | Retained + Added/Proposed |
| 08_research | RESEARCH-1 (supplied / newly-verified / gaps RG-01..06 / proposed sources) | 1 | Added |
| 09_diagrams | 4 editable .mermaid sources + cdss_diagrams_v2.html (renderable successor) | 5 | Added (Proposed) |

# 2. Source & attachment availability report

| Source | State |
|---|---|
| cdss_document_set.zip (21 files) | Readable in full; all 21 preserved + augmented |
| MAJOR_TASK_1 set (15 volumes + MANIFEST + 16 html) | Readable in full; all 32 preserved verbatim |
| MAJOR_TASK_2 directive | Readable; preserved verbatim; **pass NOT executed** |
| metamorphosis_document_set_v1_0.md | Readable; preserved verbatim as MET-1 v1.0 |
| github.com/Arepo-Medtech/Makoha | README fetched 1 Sep 2026; **below-README contents [NEEDS SOURCE]** (clone inventory = DEC-12/G-08) |
| demo.makoha.ai | Surface fetched; demos session-gated **[UNAVAILABLE]** beyond landing (C-10 raised from what is visible) |
| github.com/addyosmani/agent-skills | Fetched 1 Sep 2026: live; 25 skills (24 lifecycle + meta) vs directive's "24" → C-11; issue #361 confirmed → C-12; release 0.6.4 eval framework noted (G-11) |
| Duplicate uploads (architecture, complete stack, primer 0, MET v1.0 also supplied loose) | Byte-identical to zip copies; single canonical copy used |
| Unreadable/missing items | **None** |

# 3. Production sequence
01 plan → 02 originals preserved-then-annexed (X1 append-only discipline) → 03 corpus carried verbatim → 05 contracts/registers the annexes cite → 04 hardening spec/plan/ledger → 06 repos → 07 deploy/ops → 08 research → 09 diagrams → 00 audit. Read in this order; build in HARDEN-3's wave order; decide in MET-2's DEC order.

# 4. Completeness audit (run 2026-09-01, mechanical where possible)

**4.1 Preservation (mechanical, outputs captured in build log):** PREFIX-PRESERVATION: **ALL PASS** — each of the 21 augmented files carries its original byte-exact (45,516 B architecture … 8,559 B variant_2) with only appended annexes. VERBATIM copies: **34/34 checksum-identical** (15 corpus + MANIFEST + 16 html + MT2 + MET-1 v1.0).

**4.2 Primer/execution-layer coverage:** exact count established from files = **21 CDSS documents**, of which execution-layer-bearing primers = Primer 0 + Arch + A–L (12) + J-1 + J-2 + harness + Annex H-1 = 18 carrying §-8/§-9 layers. Every one now also carries a metamorphosis annex with the ten required execution fields (purpose, inputs, steps, tools, outputs/acceptance, dependencies, evidence, failure handling, ownership/status, traceability) — except Primer 0 (charter-exempt from execution blocks per Arch §13.9: erratum + glossary only) and the two derived artifacts (complete stack, diagrams: notices + successor). The "13+1" estimate in the brief resolves to this exact inventory.

**4.3 Deliverables checklist (brief → location):** executive summary + North Star + baseline + disposition → MET-1 v1.0 §1–4 (Retained) · target architecture → MET-1 §5 + Arch §14 + IMAGO-1 · MT1 traceability → MET-3 · MT2 plan → 04_ · execution layers → 02_ annexes · worked primers → 02_ (originals ARE the worked primers, preserved) · research → 08_ · repositories → 06_ · ops/deploy/test/security/governance → 07_ · assumptions/decisions → MET-2 · index/cross-reference → this file + MET-3 · gaps/roadmap → MET-4 · audit → §4 here. **No deliverable omitted; none silently reduced.**

**4.4 Honesty lines (what this repository does NOT claim):** the MT2 pass has **not** been executed (R29 rows 0–73 PENDING; row 0 BLOCKED on install evidence) · `validate_build_plan.py` has **not** been run on the annexes (PENDING-VALIDATOR) · no counsel attestation exists (C-01 relabel = Needs confirmation; GATE-000 unpassed) · nothing is deployed; no code beyond skeleton READMEs is claimed · corpus content untouched (row 72 = in-account path only) · HeyDoc below-README = [NEEDS SOURCE] · RTO/RPO/DR-drill + person-level owners = [NEEDS DEFINITION].

**4.5 Known open items surfaced (not hidden):** C-03, C-06, C-09, C-10 escalations; DEC-01..DEC-12 open; G-01..G-11 open per MET-4.

# 5. Post-delivery defect log (append-only)
| # | Defect | Fix | Verification |
|---|---|---|---|
| DEF-001 (2026-09-01) | `merged_runtime_sequence.mermaid` (and its inlined block in `cdss_diagrams_v2.html`) failed to render under mermaid 10.9.0 — a `;` inside a sequence-diagram message is a statement terminator, splitting the evaluator self-message mid-line | Message rewritten without in-text semicolons; refusal rules moved to a `Note over V`; grammar note added to the source header; page re-inlined | Headless `mermaid.parse` @10.9.0 (jsdom): 4/4 `.mermaid` sources PASS + 4/4 blocks extracted back out of the HTML PASS — outputs captured. This is exactly the CC-6 class bar HARDEN-2 prescribes ("mermaid sources parse"), applied early; the page's R29 row remains PENDING until the full pass runs |
| DEF-002 (2026-09-01) | MT2 citation notation collided with real subsections: seven authored instances wrote item references as `§1.7`, `§1.8`, `§7.2`, `§7.3–7.4`, `§7.4`, `§7.5` although MT2 §1 and §7 contain numbered *items*, not subsections (unlike §2.1–2.3, which are real subsections) | Normalized to `§1(7)`, `§7(4)` item notation in SEC-1, GOV-1, MET-2, HARDEN-3, and the Arch/Primer-I/Primer-C annexes; residual scan clean | Post-fix: prefix-preservation re-run ALL 21 PASS (edits confined to appended tails); residual-notation grep = NONE |

# 6. Authoring-level integrity audit (run 2026-09-01, after DEF-002 — outputs captured in build log)

*Scope note: this is the authoring pass's own sweep over what this repository writes. It does not discharge MT2 §7(3) — that cross-portfolio sweep is W11 of the hardening pass, run by the pass, after its last edit.*

| Check | Method | Result |
|---|---|---|
| ID citation resolution | 181 distinct ID tokens extracted from the 49 authored units (annex tails + new files); every externally-owned token verified by search against its owning source volume/document | **121/121 external tokens FOUND at source**; 50 minted-this-pass tokens (DEC/C/G/CC/DEF/RG-0x/R29/R30/CONTRACT/T-/W-) self-consistent; 0 dangling |
| Volume↔code map | MAK- code grepped from each corpus volume header | 15/15 exact (FFC=four-faces, ANT=antennae, HDC=head, TXC=thorax, ABC=abdomen, PRB=proboscis, LBP=labial-palps, LWC/RWC=wings, CEC=compound-eyes, LEG=legs, DOT=degrees-of-truth, MIF=makoha-in-flight, ELSM=sourcing-map, J3=addendum); HARDEN-1 row names match filenames |
| ID range endpoints | Every range claimed in R30 seed / MET-3 checked at both ends | GPP-…-16 ✓ · ASSUME-REG-…-007 ✓ · TASK-REG-…-020 ✓ · Q-REG-…-007 ✓ · WATCH-REG-…-005 ✓ · REG-KEEP-…-004 ✓ · REG-FIND-…-008 ✓ · OBL-001..009 present ✓ · SRC-REG-…-004 ✓ · KTX rows ✓ |
| Section-anchor resolution | Every §/Part anchor cited by authored text grepped in its source | Arch §1–13 incl. §12.1(1–6), §13.2–13.9 ✓ · A8…L8/H10/J9/G8-18-rows/I8 ✓ · FFC Parts 0–8 + Annex 1 ✓ · CEC Part 7 (release gate) ✓ · ELSM §01–08 ✓ · REG-POSTURE §3.4/§4/§5.1–5.3 ✓ · MIF Beats 1–8 ✓ · X1 ✓ · MT2 §2.1–2.3/§3/§5/§6/§7 ✓ (item notation per DEF-002) |
| House-notation conformance | Suspect tokens checked against the architecture's own usage | `M4` = Arch §4 diagram node for distributional gates ✓ retained · `I-1/2`, `I-5` = Arch §11.2/§11.1 house forms ✓ retained · `T1+2` = Arch diagram/register-table token ✓ retained · `PI-1/2` valid (PI-2 exists) ✓ · R16 exists as master-table row 16 (bare-number style) ✓ |
| Semantic spot-checks | Read-backs at source | MT2 §3 holds the two-terminal-states law as cited ✓ · ANT's own table marks REG-FIND rows `OPEN`, so the R30 seed is verbatim ✓ · MANIFEST reading order matches OPS-1 §4 word-for-word incl. "ANT last and always" ✓ · "Four Faces" = three role faces + the Engines ("the three faces are not three products" — Thesis), so authored "three role surfaces" phrasing is corpus-consistent ✓ |
| Preservation & structure | Byte-prefix + checksum re-run post-fix | 21/21 originals byte-exact prefixes ✓ · 34/34 verbatim copies identical ✓ · annex §-numbering collision-free (each annex = last original § + 1) ✓ |
| Paths, placeholders, diagrams | Mechanical | All 11 cited repo-relative paths resolve ✓ · placeholder census all intentional: 22 [NEEDS DEFINITION], 4 [NEEDS SOURCE], 1 [UNAVAILABLE], 4 PENDING-VALIDATOR, 5 PENDING-REGISTER-HOME (3 in pre-existing Ecosystem-v2.0 text), 1 PENDING-ENUMERATION; zero TODO/TBD/XXX ✓ · mermaid 4/4 sources + 4/4 inlined blocks parse @10.9.0 ✓ |

# 7. Amendment A-001 (2026-09-01) — repository skeletons expanded
06_repositories grew from 5 files to 91 (REPO-MAP + skeletons for 14 existing repos, cdss-integration + GPP-CHANNEL.md, and trees for the 4 proposed repos). Repository total: 84 → 170 files. §1's table row for 06 reads superseded by this amendment; all other rows unchanged. New content audited per §6 method: register-name claims verified against Arch §12.2 (one defect caught and fixed pre-seal: R2 = Artifact Manifest Register, not a contract registry — contracts live versioned in the spine repo itself, unnumbered); R14's owner row ("integration") verified as supporting the cdss-integration home; all skeleton files carry Proposed/skeleton banners; no code, build, or deployment claimed anywhere.

# 8. Amendment A-002 (2026-09-01) — regulatory-execution layer added (Imago v1.2)

**What was added.** A tenth directory, `10_regulatory-execution/` (7 files), plus two delta files in existing directories and this manifest section. Nothing pre-existing was edited: all 170 v1.1-era files verified checksum-identical at seal (ledger in build log). §1's table gains the row below; all other rows unchanged. Repository total: 170 → 179 files (7 in 10_, plus MET-2.1 and REG-R30.1).

| Dir | Contents | Files | Disposition |
|---|---|---|---|
| 10_regulatory-execution | REG-POSTURE v1.1 (canonical standalone; supersedes-by-fold the MAK-ANT Annex 1 v1.0 mirror — divergence dated and owned, C-13/EX-3, closes on FOLD-1) · REG-NZ v1.0 (NZ jurisdiction brief) · MAK-GOV v0.9 (Addendum G, non-device Governance Layer, proposed; DEC-14 ships it) · REG-SPRINT v1.0 + REG-SPRINT-1.1 delta (three-version run plan; v1.0 read only through the delta, EX-2) · EXEC-1 (precedence, run map RUN-0..4, P0 queue, counsel packet ×5+NZ) · FOLD-1 (MAK-ANT v1.1 fold worklist) | 7 | Added (regulatory content ADVISORY_ONLY per each file's authority line; sequencing normative per EXEC-1) |
| 01_ (delta) | MET-2.1 — conflicts C-13..C-16; decisions DEC-13..DEC-22 (SD-* aliases); DEC-18/SD-02 provisionally resolved: respiratory, checkpoint month 4 | +1 | Added |
| 05_ (delta) | REG-R30.1 — seed rows for all new ID families incl. NZ-ASSUME-005 (the transition-provisions working assumption, pre-registered consequence per EX-7) | +1 | Added |

**Precedence effected.** EXEC-1 EX-1: the 10_ layer governs *sequencing* portfolio-wide (RUN-0..4 merges REG-POSTURE phases, MAK-GOV sprints, REG-NZ gates, and MET-4 P0/P1 into one calendar); content authority is unchanged — corpus volumes normative for architecture, posture advisory for regulation, no ASSUME closed by anything in this amendment. J-3 remains folded, unedited, undecided (EX-4; C-14 → DEC-06 reframed as retirement ratification with MAK-GOV the named replacement).

**Honesty lines (extending §4.4).** Counsel packets drafted, not sent; no attestation exists; GATE-000/SG-V1-0/NZ-GATE-0 unpassed · the standalone-vs-annex divergence is open until FOLD-1 W5 · REG-FIND-010/011 rest on a secondary source pending primary re-anchor · MAK-GOV non-device status is an argument at moderate confidence, not a determination · NZ-ASSUME-005 is a working assumption with its failure consequence pre-registered, not a finding · regulatory-owner for the AN-6 watch cadence remains [NEEDS DEFINITION] (G-09).

**Week-one board (EX-8).** Counsel packets out · both intended-purpose statements begun · V1-S1 synthetic build begins (decoupled per D-1) · demo-surface triage (TASK-REG-021) · R&D-window question (V1-C1) · NZ conflict declaration drafted (NZ-TASK-003) · MT2 row zero per MET-4 P0.

# 9. Amendment A-003 (2026-09-02) — jurisdiction posture set made replete-standalone

**What was added.** Four jurisdiction documents in `10_regulatory-execution/` and one seed delta in `05_`. Nothing pre-existing was edited except this manifest (appended, per the A-001/A-002 pattern): REG-POSTURE_v1.1.md and REG-NZ_v1.0.md remain in place, unedited, and are **superseded** by the new versions below. Repository total: 179 → 184 files.

| Dir | Contents | Files | Disposition |
|---|---|---|---|
| 10_regulatory-execution | **REG-POSTURE v1.2 — AUSTRALIA (TGA)**: v1.1 carried verbatim with [AMENDED v1.2] notes; standards stack 13 → 26 rows with editions pinned; MAK-GOV forward references homed (REG-FIND-013, TASK-REG-023, ASSUME-REG-009, Q-REG-010 — closes survey-2 BSQ-0001); Ketryx pre-demo answers folded as [vendor-stated] (KTX-013/014); OBL-015 e-record integrity; MDSAP question (Q-REG-011/TASK-REG-024). Canonical posture per EX-3; FOLD-1 W1 now targets v1.2 · **REG-NZ v1.1 — NEW ZEALAND (Medsafe)**: replete-standalone; NZ-STD-001..026 rolled in; Medsafe technical-file contents (§6); NZ privacy/HISO/Māori-data instruments; NZ-Q-004 and NZ-ASSUME-005 homed; NZ-GATE-000..002 formalised · **REG-US v1.0 — UNITED STATES (FDA)**: new; §520(o)(1)(E) analysis, De Novo/510(k), QMSR, Part 11, §524B, PCCP, AI lifecycle guidance, HIPAA/FTC; "now" tasks US-TASK-001..004 run during the NZ/AU build · **REG-EU v1.0 — EUROPEAN UNION (MDR)**: new; MDCG 2019-11/Rule 11 (no exemption exists), Annex IX route, GSPR 17, MDCG 2020-1 clinical evaluation, PMS/PSUR/vigilance, AI Act high-risk integration, GDPR (NZ adequacy vs AU SCCs), CRA exclusion, EHDS, PLD; "now" tasks EU-TASK-001..004 | +4 | Added (ADVISORY_ONLY per each file's authority line; supersedes REG-POSTURE v1.1 and REG-NZ v1.0, which are retained unedited) |
| 05_ (delta) | REG-R30.2 — enum extension for US-*/EU-*/NZ-STD-*/NZ-GATE-*/STD-*; `jurisdiction` row field; seed rows for every new ID; cross-joins (shared-stack alignment, evidence transfer, records, Governance Layer status, QMS route, pre-deployment change control) | +1 | Added |

**Replete-standalone rule (new, all four documents §0.x).** Each jurisdiction document carries the complete standards stack with that regulator's recognition status and its own obligations, gates, tasks, assumptions, questions, watch items and sources; none says "see elsewhere" for anything a reader needs in that jurisdiction. Shared artifacts (intended purpose, ISO 14971 risk file, IEC 62304 records, technical documentation) are built once and projected per regulator. `STD-nnn` = `NZ-STD-nnn` = `US-STD-nnn` = `EU-STD-nnn` for 001..026. A change to the shared stack is made in all four in the same cycle or logged in MAK-ANT as a divergence signal.

**Provenance discipline.** Every row that originates from the author's 2 September 2026 standards-gap review rather than from a regulator's instrument is tagged [recommendation] with a confidence tag; every vendor statement (Ketryx correspondence, SRC-REG-017) is tagged [vendor-stated]; every instrument known to have changed recently is tagged [currency: verify]. Counsel can see at a glance what came from a regulator, what came from a vendor, and what came from analysis.

**Honesty lines (extending §4.4 and A-002).** No attestation exists in any jurisdiction; GATE-000, NZ-GATE-000, US-GATE-000, EU-GATE-000 all unpassed · standards editions and FDA-recognition / EU-harmonisation status are from the author's knowledge and must be confirmed against the live FDA database and OJ list before any submission (WATCH-REG-008, US-WATCH-004, EU-WATCH-004) · the January 2026 FDA CDS guidance revision and the 2025 FDA cybersecurity guidance revision have **not** been read in the primary (US-WATCH-001) · the EU AI Act high-risk application date is uncertain pending the Digital Omnibus outcome (EU-WATCH-002) · REG-FIND-010/011 still rest on a secondary source · a strict row-start parser finds twelve v1.1-era IDs in prose/field-table shape and one v1.1-era double definition (ASSUME-REG-004), recorded in REG-POSTURE v1.2 §12.2 check 2 and left for the next revision under append-only law · regulatory owner for the watch cadence remains [NEEDS DEFINITION] (G-09) · MAK-ANT Annex 1 still mirrors v1.0; the divergence window (EX-3) now closes on a fold of **v1.2**.

**Verification at seal.** validate_reg.py (kept beside the documents at `10_regulatory-execution/validate_reg.py`) run 2026-09-02: NZ 93/93, US 129/129, EU 123/123 IDs referenced = defined, all families contiguous at both range endpoints, every TASK names a gate, every FIND names a source, shared stack 001..026 present in all four, no standalone-rule violations; AU 150 referenced / 138 first-cell-defined with the twelve legacy-shape IDs and one legacy duplicate itemised above. REG-POSTURE_v1.1.md and REG-NZ_v1.0.md checksum-identical to their A-002 state (d8ff7aaf…, 2a384b1b…).
