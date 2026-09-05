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

# 10. Amendment A-004 (2026-09-05) — sprint-1: the survey-2 Build-Spec Queue closed; 11_prompts indexed; 03_/02_ additions indexed; defects DEF-003..DEF-006

**What was added.** Nothing pre-existing was edited except this manifest (appended, per the A-001..A-003 pattern; prefix-preservation proven in `11_prompts/runs/2026-09-05_sprint-1/RUN-REPORT.md`). Sprint-1 (branch `sprint-1-build-spec-queue`, 5 September 2026) executed every CLAUDE-CODE-EXECUTABLE-NOW row of the survey-2 Build-Spec Queue (`11_prompts/runs/2026-09-02_survey-2/BUILD_SPEC_QUEUE.md` §c) plus the weight-2 rows the survey recommended, as **new files only** — companions, deltas and successors beside the retained files. 37 files added outside run directories; three run directories now exist under `11_prompts/runs/` (`2026-09-02_survey-2`, `2026-09-05_sprint-1`, `2026-09-05_primer-0` — the last a partial PROMPT-P0 Phase 2 run: counsel packets assembled, not sent).

| Dir | Contents added (sprint-1) | Files | Disposition |
|---|---|---|---|
| 04_hardening | INDEX-04 · HARDEN-1.1 coverage ledger seed delta (275 rows, one path-resolving row per artifact in the tree; v1.0 ids retained; all PENDING) · HARDEN-2.1 spec census + self-audit delta (source per class bar; AR-1..4, STL-1..5 minted) · HARDEN-3.1 task register delta (276 tasks, one per artifact; every v1.0 T id present once; extensions marked) | +4 | Proposed (seed/plan/spec deltas; the pass has NOT run) |
| 05_registers-and-contracts | INDEX-05 · CONTRACT-ARG-1 / CONTRACT-DEV-1 JSON Schemas + examples (validated) · CONTRACT-RRI-1 render-invariance test spec (RRI-1..4) · REG-R29.examples.jsonl + REG-R29.1 twin delta · REG-R30.schema.json + REG-R30.3 row-form seed (549 rows: AU 150, NZ 93, US 129, EU 123, NDG 14, sprint 30, EX 10; all validate; statuses crosswalked with `source_status_verbatim` preserved; mapping for 'standing'/cadence rows flagged pending the regulatory owner — BSQ-0208) | +10 | Proposed (DEC-02); nothing moved (DEC-09) |
| 06_repositories | INDEX-06 (19 tree rows; 96 file rows; known gaps) · six `ci/pipeline.yml` stubs (evalstack, governance, harness, llm-lattice, lumos, integration) | +7 | Proposed (skeletons; DEC-09) |
| 07_deployment-and-operations | INDEX-07 · DEPLOY-1.1 run-map delta (DR-1..7; in force on DEC-22) · OPS-1.1 procedures in CC-5 form (PROC-01..12; 33 steps, all four fields) · SEC-2 threat model + data-flow (B-1..7; TM-01..18) | +4 | Proposed; regulatory mappings ADVISORY_ONLY |
| 08_research | INDEX-08 · RESEARCH-1.1 findings delta (status field; RG-07, RG-08; closure path) | +2 | Added |
| 09_diagrams | INDEX-09 (recorded parse + identity self-audit; regeneration procedure) · register_topology_v3.mermaid (§7(4) notation fix — DEF-003) · deployment_ladders_v2.mermaid (RUN-0..4 overlay) · data_flow_v1.mermaid (IMAGO-5, SEC-2 §1) · cdss_diagrams_v3.html (successor page; v2 preserved) | +5 | Added (Proposed) |
| 10_regulatory-execution | INDEX-10 · REG-POSTURE_v1.2_CONTENTS.md (69-heading map; owner gap carried) · REG-SPRINT-1.2 census delta (30 ids; D-6, D-7) | +3 | Added; ADVISORY_ONLY |
| 11_prompts | **Directory indexed for the first time** (the survey's proposed A-003 text, never appended): PROMPT-P0, PROMPT-A..L (12), PROMPT-PRM-SERIES index + PROMPT-PRM0 + PROMPT-PRM-* (10), PROMPT-SERIES_A-L_index, PROMPT-SURVEY-1, PROMPT-SURVEY-2 (28 pre-existing) · sprint-1: PROMPT-FOLD-1 (fold of REG-POSTURE v1.2 into MAK-ANT v1.1; output staged for the corpus owner) · PROMPT-HARDEN (DRAFT — EXECUTABLE-AFTER-DECISION DEC-10/DEC-11) · `runs/` | 28 + 2 + runs | Proposed (prompts); run outputs are evidence, not programme facts |
| 03_ / 02_ (additions, indexed for the first time) | `03_/butterfly-primers/` (10 primers + RUN-REPORT), `butterfly-primer-programme_prompt_v1.0.md`, `corpus_artifacts_briefing.md`; `02_/primers_briefing.md` — beside the fifteen volumes, unindexed by the 03_ MANIFEST, which still governs its volumes | 13 + 1 | Proposed (primers, prompt); Added (briefings) |
| repository files | README.md, `.github/confluence-mirror/*`, `.github/workflows/confluence-mirror.yml`, `.gitignore`, `00_inventory.txt` — now carried as CC-5/CC-8 rows in HARDEN-1.1 | — | Added (2026-09-03/05) |

**Queue closure.** Of the 42 queue rows: 27 CLAUDE-CODE-EXECUTABLE-NOW → 25 built, 2 closed by A-003 before the sprint (BSQ-0001 REG-FIND-013/TASK-REG-023 homed in REG-POSTURE v1.2; BSQ-0706 REG-NZ v1.1 carries NZ-Q-004, census, self-audit, gate per row); 5 EXECUTABLE-AFTER-DECISION → 1 drafted (PROMPT-HARDEN, BSQ-0103), 4 remain (BSQ-0707 MAK-GOV integration delta — DEC-13/14; BSQ-0391 compiler primer — DEC-09/13; BSQ-0208 R30 status mapping — regulatory owner; BSQ-0001 closed as above); 10 HUMAN-ONLY remain (DEC-22; DEC-10/11; DEC-02; DEC-09; DEC-07/03/08; DEC-13/14/16/17/19/20; DEC-06; DEC-01; proposed DEC-23). Weight-2 rows built: BSQ-0002/0003 (v3 successors), BSQ-0392 (six CI stubs), BSQ-0502 (RESEARCH-1.1), BSQ-0606 (IMAGO-4 v2). Full table: `11_prompts/runs/2026-09-05_sprint-1/RUN-REPORT.md`.

**Post-delivery defect log — rows appended to §5 (append-only; recorded here to avoid a mid-file edit):**

| # | Defect | Fix | Verification |
|---|---|---|---|
| DEF-003 (2026-09-05; found 2026-09-02) | DEF-002's residual scan missed `09_diagrams/register_topology_v2.mermaid` l.17 and its inlined block in `cdss_diagrams_v2.html` l.96 (`MT2 §7.4`); §5 DEF-002 "residual-notation grep = NONE" was therefore incomplete | Successor sources `register_topology_v3.mermaid` + `cdss_diagrams_v3.html` (v2 files preserved unedited) | sprint-1 refcheck: unresolved anchors in v3 files = 0; the two v2 anchors remain by design in superseded files; mermaid.parse 7/7 sources + 9/9 blocks PASS |
| DEF-004 (2026-09-05; found 2026-09-02) | §7 A-001 states "all skeleton files carry Proposed/skeleton banners"; 13 of 90 skeleton files carry no Proposed/skeleton/stub marker | INDEX-06 §4 lists the 13 until the trees instantiate; no skeleton file edited | `grep -L -i 'skeleton\|proposed\|stub\|pointer'` over `06_repositories/repo-skeletons/**` → 13 (INDEX-06 §3 per-file check) |
| DEF-005 (2026-09-05; found 2026-09-02) | §8 states "Counsel packets drafted, not sent"; at 2026-09-02 no packet artifact existed — the packet was *specified* (EX-6; PROMPT-P0 Phase 2) | Packets **assembled** 2026-09-05 in `11_prompts/runs/2026-09-05_primer-0/counsel_packet_AU/`, `counsel_packet_NZ/` (by reference; ADVISORY_ONLY; dispatch HUMAN-ONLY). Read §8 as "specified, now assembled, not sent" | `ls 11_prompts/runs/2026-09-05_primer-0`; P0_BOARD_STATUS.md |
| DEF-006 (2026-09-05) | HARDEN-3 v1.0 W4 says "one task each, sixteen tasks" (T-030..045) but names 19 artifacts (Arch, Primer 0, A–L, J-1, J-2, harness, annex H-1, integration report); T-121 and T-122 collapse several artifacts | HARDEN-3.1: T-030..045 = the sixteen HARDEN-1 rows 11–26 name; T-046..048 minted for Arch, Primer 0, integration report; T-121/T-122 expanded into W10 extension tasks; HARDEN-3 v1.0 unedited | HARDEN-3.1 census: 73/73 v1.0 ids present once; 276 tasks; 0 duplicates; every file has a task |

**Register-name query and proposed decision (carried from survey-2, unresolved):** R25 label divergence (Arch §12.2 "Build Evidence & Assumptions Ledger" vs Primer A A10 / IMAGO-3 "property runs") — architecture owner rules (BSQ-0602; v3 topology carries the label unchanged). **Proposed DEC-23** for MET-2.2: "Name the infrastructure owner; set RTO/RPO targets; approve the L5 multi-region DR drill protocol" (closes the RTO/RPO/DR component of G-09; blocking L5 exit and GATE-004; BSQ-0405).

**Honesty lines (extending §4.4, §8, §9).** The MT2 pass remains unexecuted — HARDEN-1.1's 275 rows are placeholders; PROMPT-HARDEN is a draft that MUST NOT run before DEC-10/DEC-11 and row zero · no ASSUME, DEC, gate or posture was closed or presupposed; every R30.3 row is OPEN · counsel packets are assembled and **not sent**; GATE-000, SG-V1-0, NZ-GATE-000 unpassed · the intended-purpose drafts are assembled quotations for their owners' review, not statements · nothing is deployed; the six new CI stubs are not runnable · person-level owners remain [NEEDS DEFINITION] (30+ queue rows carry the gap; DEC-09/DEC-10/G-09) · the R25 label, the FOLD-1↔HARDEN-3 W-namespace collision (BSQ-0711) and the R30 'standing'/cadence status mapping (BSQ-0208) await their owners · the Ketryx system-of-record question is parked by the owner's instruction (5 September 2026): R29/R30's physical home after DEC-02 is an open question, not a decision · `validate_reg.py` still reports the known AU legacy-shape condition (§9), unchanged.

**Verification at seal (2026-09-05; outputs in `11_prompts/runs/2026-09-05_sprint-1/`).** Schemas: check_schema OK ×4 (ARG-1, DEV-1, R29, R30); examples 10/10 agree with their expected verdicts; R30.3 549/549 rows valid, 0 duplicates, 44 families contiguous · mermaid 10.9.8 via jsdom: 7/7 sources, 4/4 v2 blocks, 5/5 v3 blocks PASS; source↔inline identity 9/9 · CC-5 field presence 33/33 steps · ledger acceptance: set(rows.artifact_path) == set(files in tree excl. .DS_Store and runs) — 0 missing, 0 extra · HARDEN-3.1: every file has exactly one task · every pre-existing file checksum-identical (CHECKSUMS_BEFORE/AFTER diff = this manifest only, appended — prefix preserved).

# 11. Amendment A-005 (2026-09-05) — agent deployment layer enacted; PROMPT-SURVEY-3 indexed

**What was added.** Nothing pre-existing was edited except this manifest (appended). The three integration layers of the requester's "Directives for Agent Deployment" are enacted for this repository's actual toolchain (Claude Code + GitHub Copilot + GitHub Actions), and the final-survey instrument written after A-004 is indexed.

| Location | Contents added | Disposition |
|---|---|---|
| `AGENTS.md` (root) | Repository governance blueprint for every agent: the directive's three Agent System Rules (domain; PR context = architecture-graph impact; prioritise structural/ID consistency over phrasing) plus the seven laws of the corpus restated for agents, the read order, how work lands, the mechanical checks, and the Impeccable scope. Read by Copilot coding agent, Copilot code review (github.com) and Copilot CLI | Added — governance |
| `CLAUDE.md` (root) | Claude Code entry point; imports `AGENTS.md` | Added |
| `.github/copilot-instructions.md` | The Core Metaprompt Construction Block (DesignOps Systems Architect role; four evaluation layers; Severity / Target Asset / Observed / Target / Remediation output template), adapted with this repository's layer mapping (tokens → IDs; Layer 4 → the 19 HTML pages; document design system for markdown). Read by Copilot code review and Chat | Added — governance |
| `.github/instructions/corpus-never-edited.instructions.md`, `retained-files.instructions.md` | Path-specific Copilot instructions: 03_ is never edited by an agent; 0n_ files change only by delta/companion/successor + amendment | Added |
| `.github/workflows/design-ecosystem-audit.yml` + `.github/audit/` (append_only.py, frontmatter_census.py, refcheck.py, depth.py, schemas.py, mermaid/parse.mjs, run_all.sh) | "Design Ecosystem Agentic Audit" on every pull request: (1) mechanical layer — append-only prefix check against main, frontmatter schema census, dead-path/anchor check, depth ≤ 4, JSON Schema + example validation, mermaid parse; (2) Copilot code review requested via the REST API (`copilot-pull-request-reviewer[bot]`); (3) Impeccable detector over changed HTML pages | Added — verification |
| `.claude/skills/impeccable/`, `.claude/agents/impeccable-*.md`, `.github/skills/impeccable/`, `.github/agents/impeccable-*.md` | Impeccable v4.0.1 skill (23 commands incl. `critique`, `audit`, `layout`) installed at project scope for Claude Code and GitHub Copilot, without hooks; platform engine binaries untracked (`.gitignore`; restore with `npx impeccable install`) | Added — third-party skill (pbakaus/impeccable, reviewed as a dependency: skill text only is tracked) |
| `11_prompts/PROMPT-SURVEY-3_final-quality-improvement.md` | Final survey and quality-improvement prompt (Impeccability Queue; four architect layers mapped; QI ledger schema) — merged 2026-09-05 (PR #7) after A-004 | Proposed; not yet run |
| `.github/confluence-mirror/config.json` | `excludePrefixes` extended: `.impeccable/`, `.claude/`, `AGENTS.md`, `CLAUDE.md` (agent tooling is not corpus) | tooling |

**Ledger debt.** These files have no HARDEN-1.1 row or HARDEN-3.1 task yet; a HARDEN-1.2 / HARDEN-3.2 delta owes them (CC-5 workflows and scripts; CC-8 governance text). Recorded, not hidden.

**Honesty lines (extending §4.4, §10).** `github/copilot-review-action@v1`, named in the directive, does not exist (HTTP 404, verified 2026-09-05); the workflow requests Copilot review through the REST API instead · the organisation's Copilot plan is Business with **zero seats assigned** at 2026-09-05, so Copilot code review will not run until a seat is assigned to the PR author · the repository ruleset "Automatically request Copilot code review" (rule type `copilot_code_review`) was **not created by the agent** — the API call was blocked by the session's permission policy; the owner creates it (Settings → Rules → Rulesets, or `gh api -X POST repos/Arepo-Medtech/CDSS-makoha-imago/rulesets` with the body recorded in the sprint hand-back) · `/impeccable init` has not been run (it must be run inside a coding-agent chat and writes the product-context file PRODUCT.md, not yet present); the detector baseline over the 19 HTML pages was not run locally (blocked) and runs in CI on changed pages · the directive's `/critique --tokens` and `/layout --grid` flags do not exist in Impeccable v4; the commands are `/impeccable critique`, `/impeccable audit`, `/impeccable layout` · no corpus content, ASSUME, DEC or posture was touched.

# 12. Amendment A-006 (2026-09-05) — PROMPT-SURVEY-3.1: deep-review fold

**What was added.** Nothing pre-existing under `00_`–`11_` was edited except this manifest (appended). Outside the append-only law, the root governance file `AGENTS.md` gained one read-order sentence (see table). One file is added under `11_prompts/`, a delta over PROMPT-SURVEY-3 v1.0, which is preserved verbatim and is now read through it.

| Location | Contents added | Disposition |
|---|---|---|
| `11_prompts/PROMPT-SURVEY-3.1_deep-review_fold_delta.md` | Review of the `deep-review@claude-deep-review` 5.8.0 plugin (53 reviewers + synthesizer; scope detection; confidence scoring; holistic re-prioritisation), quoted by path, byte count and line; an alignment map of eleven of its structural elements onto PROMPT-SURVEY-3's laws, phases and QI schema; and nine additive delta items — D-1 four QI schema properties (`confidence`, `confidence_reason`, `attribution`, `calibrated_weight` + note), D-2 law 16 confidence per row (entry ≥ 60, CRITICAL presented only ≥ 80, both `[ASSESSOR-PROPOSED]`; low scores listed, never dropped), D-3 law 17 attribution is not severity (baseline = sprint-1 merge `b810db0`), D-4 Phase 4 cross-folder calibration step, D-5 coverage gaps recorded never filled, D-6 sub-agent prompt template with an untrusted-content boundary, D-7 Queue §i exemplar register and §j needs-verification list, D-8 evals T-11..T-14, D-9 two PROPOSED-ADDITION candidates. Four deep-review positions filed as not imported. | Proposed; not yet run |
| `AGENTS.md` (root, governance file outside 00_–11_) | Read-order sentence extended: PROMPT-SURVEY-3 is read through PROMPT-SURVEY-3.1 | governance text |

**Ledger debt.** `PROMPT-SURVEY-3.1` has no HARDEN-1.1 row or HARDEN-3.1 task; it joins the A-005 debt owed by a HARDEN-1.2 / HARDEN-3.2 delta.

**Honesty lines (extending §4.4, §10, §11).** deep-review was not run on this repository and is not part of its tree; it is a user-scope Claude Code plugin on one maintainer's machine · the plugin's confidence-scoring and re-prioritisation stages exist only in its headless script, not in its in-session skill, and were read as text, not executed · PROMPT-SURVEY-3 remains unrun; the fold changes what a run will record, not what has been recorded.

# 13. Amendment A-007 (2026-09-05) — PROMPT-SURVEY-3.2: erratum over PROMPT-SURVEY-3.1; defect DEF-007

**What was added.** Nothing pre-existing under `00_`–`11_` was edited except this manifest (appended). Outside the append-only law, the root governance file `AGENTS.md` read-order sentence now names both deltas. One file is added under `11_prompts/`.

| Location | Contents added | Disposition |
|---|---|---|
| `11_prompts/PROMPT-SURVEY-3.2_confidence_erratum_delta.md` | Erratum over PROMPT-SURVEY-3.1 (retained; merged in PR #12 before its Copilot review posted): E-1 D-1 counts six properties and adds `scorer_failed`; E-2 law 16 keeps an unscored row with `scorer_failed: true` and no confidence number instead of the sentinel `confidence: 100`, routed to §j; E-3 consequential wording in §j and T-11; 3.1 §4 gains item 5 (sentinel not imported). Read PROMPT-SURVEY-3 through 3.1 and 3.1 through 3.2. | Proposed; not yet run |

**Defect log (continuing §5, §10).**

| ID | Found | Where | What | Disposition |
|---|---|---|---|---|
| DEF-007 | 2026-09-05, Copilot code review on PR #12 (posted 09:12:34Z, 73 s after merge) | `PROMPT-SURVEY-3.1` `:138` and `:175–177`; A-006 row text "four QI schema properties" | D-1 title said four properties, the snippet added five; law 16 recorded an unscored row as `confidence: 100`, a failure disguised as certainty | Corrected by PROMPT-SURVEY-3.2 (this amendment); 3.1 and A-006 retained as written |

**Ledger debt.** `PROMPT-SURVEY-3.2` has no HARDEN-1.1 row or HARDEN-3.1 task; it joins the A-005/A-006 debt owed by a HARDEN-1.2 / HARDEN-3.2 delta.

**Honesty lines (extending §11, §12).** The Copilot review ruleset does not gate merging; PR #12 merged before its review posted, which is why this is an erratum file and not a branch fix · making the review or the mechanical audit a required status check is a candidate for a later amendment, not decided here.

# 14. Amendment A-008 (2026-09-05) — survey-3 run recorded (PR #14, merge ac3b052); placeholder census re-run; DEF/A census; 00_inventory status

**What was added.** Nothing pre-existing under `00_`–`11_` was edited except this manifest (appended). One run directory: `11_prompts/runs/2026-09-05_survey-3/` (excluded from the Confluence mirror; evidence, not corpus).

| Location | Contents added | Disposition |
|---|---|---|
| `11_prompts/runs/2026-09-05_survey-3/` | PROMPT-SURVEY-3 v1.0 run, read through 3.1 and 3.2: ORIENTATION, QUALITY_STANDARD (17 Q-D + 5 Q-F lines), 8 tools + outputs, CENSUS + L1–L4 tables, 14 folder fragments, 13 depth-read items, `QI.jsonl` (174 rows, 174 valid), IMPECCABILITY_QUEUE (§a–§j), HALT_LOG, OPEN_QUESTIONS, CHECKSUMS_BEFORE/AFTER (diff ∅) | Evidence; Proposed queue for sprint-2 |

**Placeholder census (re-run 2026-09-05, in-scope files).** `[NEEDS DEFINITION]` 557 in 67 files (98 = repo owners DEC-09; 46 = corpus owner; 41 = MT2 operator DEC-10; 22 = component owners DEC-09; 15 = regulatory owner G-09; 13 = manifest owner; …) · `[NEEDS SOURCE]` 19 in 11 · `[UNAVAILABLE]` 2 in 1 · `PENDING-VALIDATOR` 46 in 10 · `PENDING-REGISTER-HOME` 6 in 4 · `PENDING-ENUMERATION` 7 in 5. Every placeholder names its resolving DEC or gap; none is unregistered. Supersedes the §6 line of 2026-09-01 (22 / 4 / 1 / 4 / 5 / 1) as the current census (QI-0028).

**ID census (this manifest).** `DEF-001..007` = 7 defect rows (§5, §10, §13); `A-001..008` = 8 amendments. Retired: none (QI-0027).

**Inventory status.** `00_inventory.txt` is the v1.1-build byte inventory of 2026-09-01 (82 lines; 13 counts and 16 paths differ from disk — `11_prompts/runs/2026-09-05_survey-3/raw/inventory_drift.txt`). It is retained as a snapshot; the tracked tree is authoritative (README). A regenerated 00_inventory_v1.3.txt with a header line is queued (QI-0063).

**Verdicts (survey-3 §b).** ROOT and 02 are IMPECCABLE-WITH-DECISIONS-PENDING; 01, 10 and CHAIN are BELOW-STANDARD on WARNING/CRITICAL rows with drafted remedies; every other folder is BELOW-STANDARD on OPTIMISATION rows only. One CRITICAL document defect: the MET-4 gap table (QI-0018). Layer scores in the Queue §b.

**Ledger debt.** No file created since A-005 (governance files, PROMPT-SURVEY-3/3.1/3.2, this run) has a HARDEN-1.1 row or HARDEN-3.1 task; a HARDEN-1.2 / HARDEN-3.2 delta owes them, plus rows for every file the Queue's EXECUTABLE-NOW set would create.

**Honesty lines (extending §11–§13).** The survey built nothing, ran no pass, wrote no R29 row, closed no decision · thresholds are `[ASSESSOR-PROPOSED]` (Queue §Assumptions; OPEN_QUESTIONS 10) · mermaid parse cited from CI, not run locally · confidence scored by the writer, not an independent scorer.

**Defect rows.**

| DEF | Found | Location | Nature | Disposition |
|---|---|---|---|---|
| DEF-008 (2026-09-05, survey-3 QI-0063) | survey-3 | `00_inventory.txt` | `00_inventory.txt` presents byte counts without a date, status or supersession line; 13 counts and 16 paths differ from disk. | Not an append-only breach (`git show 73460b3` sizes equal disk). Fix: this inventory-status paragraph + 00_inventory_v1.3.txt successor (QI-0063) |

**Decisions proposed for MET-2.2 (register rows, not amendments — Architecture owner; carried as DEC-24..26 in A-009 below).**

- **DEC-24** doc_id supersession rule (QI-0001) · **DEC-25** R25 label (BSQ-0602 / QI-0029) · **DEC-26** namespace alias laws: W-n (FOLD-1 vs HARDEN-3), RG (MAK-CEC vs RESEARCH-1), CC (HARDEN-2 vs MAK-LBP) (QI-0030 / QI-0024 / QI-0025).

# 15. Amendment A-009 (2026-09-05) — MET-2.2: nine decisions closed by owner ruling; roles named to accounts; DEC-23 accepted; DEC-24..26 proposed

**What was added.** One file, `01_north-star-and-transformation/MET-2.2_decision_closures_delta.md` (21,013 bytes; additive delta to MET-2 and MET-2.1, neither edited), and this section. On 2026-09-05 the owner (Kenny-bytes: Founder, Programme lead, Architecture owner) walked the eight HUMAN-ONLY rows of the survey-3 Queue (`11_prompts/runs/2026-09-05_survey-3/IMPECCABILITY_QUEUE.md` §c: QI-0167..QI-0174) and ruled on each; MET-2.2 is the register record.

| Location | Contents added | Disposition |
|---|---|---|
| `01_north-star-and-transformation/MET-2.2_decision_closures_delta.md` | §1 roles → accounts (Kenny-bytes, kendo-Jones, Ken-nough, Ken-E-Gee — logins as returned by the GitHub org members API; seniority order as ruled) · §2 full DEC table DEC-01..26 with closure-evidence column · §3 rulings: DEC-22 adopted (EXEC-1 EX-1/EX-5; 10_ v1.2 working set) · DEC-10 operator = Kenny-bytes · DEC-11 C-11 rule accepted · DEC-02 R29/R30 ratified as real registers · DEC-09 repo owners named, PFX {FAB, UIP, UIC, GPP} ratified (Arch §14.4 → ratified) · DEC-08 IMPL rename + quarterly Observer cadence ratified · DEC-13 doc_id `MAK-GOV` permanent, not J-series (delegated naming ruling) · DEC-14 Governance Layer built to finish and held ready; commercial timing outside the register · DEC-01 C-01 relabel ratified; `ASSUME-REG-002` stays OPEN (C-17 dated divergence with REG-POSTURE v1.2 l.473) · DEC-23 accepted: owners named, RTO/RPO values open · §5 DEC-24..26 drafted, Open · §6 consequential files owed (sprint-2) · §8 self-audit with pasted outputs | Added — register delta; closures are owner facts, drafts are Proposed |

**Census.** C-01..C-17 (17; +1 C-17) · DEC-01..DEC-26 (26 = 23 minted + 3 proposed; 9 closed by A-009: DEC-01, 02, 08, 09, 10, 11, 13, 14, 22; DEC-21 namespace component closed; DEC-23 names closed) · G-01..G-11 unchanged (G-09 narrowed in MET-4.1 when written). `A-001..009` = 9 amendments; `DEF-001..008` = 8 defect rows.

**Placeholder effect (not yet applied — cells resolve only in the owed deltas).** DEC-09 → 98 repo-owner + 22 component-owner cells; DEC-10 → 41 MT2-operator cells; DEC-23 → 15 regulatory-owner cells; these 176 of the 557 `[NEEDS DEFINITION]` counted in A-008 now have a name and resolve in HARDEN-1.2 / HARDEN-3.2.

**Not done by A-009.** No `ASSUME-*`, `GATE-*` or posture closed; no R29 row written; no pass launched; nothing under 03_ or 10_ edited (the MAK-GOV `naming_note` and the REG-POSTURE l.473 DEC-01 clause read as superseded on the point only, carried by their owners into next versions). DEC-03..07, 12, 15..17, 19, 20 keep their State.

**Ledger debt.** MET-2.2 has no HARDEN-1.1 row or HARDEN-3.1 task; it joins the A-005..A-008 debt owed by a HARDEN-1.2 / HARDEN-3.2 delta — which now also fills the 176 named cells above.

**Process (requirement).** The PR carrying this amendment is opened by Kenny-bytes so that the Copilot review is auto-requested under ruleset 22326380; it is to be merged only after that review has posted and its findings have been addressed on the branch, per the A-007 process note.

# 16. Amendment A-010 (2026-09-05) — sprint-2: the survey-3 EXECUTABLE-NOW set built; HARDEN-1.2/3.2 clear the ledger debt and name owners; GLOSSARY.md; REPO-MAP v3; IMAGO-3 v4 (DEC-01 regeneration); MET-4.1; MET-5; REG-TASK-OWNERS; inventory v1.3

**What was added.** Nothing pre-existing under `00_`–`11_` was edited except this manifest (appended). Root `README.md` (outside the 00_–11_ law) gained one "Where to read it" row pointing at `GLOSSARY.md`. Sprint-2 (branch `sprint-2-executable-now` from `main` 21b9675, 5 September 2026; run record `11_prompts/runs/2026-09-05_sprint-2/`, excluded from the Confluence mirror) executed every CLAUDE-CODE-EXECUTABLE-NOW row of the survey-3 Impeccability Queue (`11_prompts/runs/2026-09-05_survey-3/IMPECCABILITY_QUEUE.md` §c/§c.1), the weight-2 rows the Queue marked recommended (§d), and the files MET-2.2 §6 owes now that nine decisions are closed (A-009) — 18 new files, as deltas, companions and successors beside retained files.

| Location | Contents added (bytes) | Disposition |
|---|---|---|
| root | `GLOSSARY.md` (12,064) — 38 house terms: quoted or pointed source by path and line, guarding ruling with its state, aliases and near-misses, home (survey-3 QI-0032) · `00_inventory_v1.3.txt` (24,257) — regenerated inventory with a header line; supersedes `00_inventory.txt` (retained; DEF-008; QI-0063) | Added — Proposed |
| 01_ | `MET-4.1_gap_register_delta.md` (7,720) — owner · person/DEC · RUN/gate · exit evidence · register home per G-01..G-11; `req_prefix: G`, census 11; G-09 narrowed (owners named, values owed) — the one CRITICAL survey-3 document row (QI-0018) · `MET-5_ratification_read-through_notice.md` (6,489) — N-01..N-12: every retained "proposed" / "[NEEDS DEFINITION]" sentence the A-009 rulings supersede, by path and line, with the reading that applies | Added — Proposed (MET-5 is a read-through notice; it closes nothing) |
| 04_ | `HARDEN-1.2_coverage_ledger_owner_delta.md` (76,468) — D-1: 182 HARDEN-1.1 owner cells resolved to the accounts MET-2.2 §1 names (Kenny-bytes ×158, kendo-Jones ×15, Ken-E-Gee/kendo-Jones ×9 partial); D-2: 146 new rows (ids 274..419) for every tracked file without a row — the agent deployment layer (A-005), PROMPT-SURVEY-3/3.1/3.2 (A-005..A-007), MET-2.2 (A-009) and this sprint's files · `HARDEN-3.2_task_register_delta.md` (86,892) — 146 tasks T-800..T-945, one per new row, wave/skills/exit inherited from the nearest HARDEN-3.1 sibling · `HARDEN-2.2_alias_laws_delta.md` (3,713) — CC and W alias laws drafted (QI-0025/QI-0030; DEC-26 Proposed) · `INDEX-04.1_delta.md` (2,798) | Added — Proposed; every ledger row PENDING (no R29 row written) |
| 06_ | `REPO-MAP_v3.md` (8,510) — v2 rows carried with owner column (Kenny-bytes; DEC-09) and PFX column ({FAB, UIP, UIC, GPP} ratified; cdss-compiler [PENDING-ENUMERATION]) · `INDEX-06.1_delta.md` (1,921) | Added — successor; v2 retained |
| 08_ | `RESEARCH-1.2_alias_and_triggers_delta.md` (4,631) — RG alias law (QI-0024; DEC-26 Proposed), `RGAP-` declared, trigger column per RG-01..08 (QI-0022) · `INDEX-08.1_delta.md` (1,957) | Added — Proposed |
| 09_ | `register_topology_v4.mermaid` (1,894) — IMAGO-3 v4: R29/R30 solid (DEC-02), Observer cadence (DEC-08), R25 label carried pending DEC-25 · `cdss_diagrams_v4.html` (11,671) — successor page inlining v4, styled from `tokens.css` (2,124: 28 series colours + 3 fonts from the survey-3 census, 7 diagram tokens; QI-0043/0044) · `INDEX-09.1_delta.md` (4,155) with the parse paste (22/22 PASS) — this is the DEC-01 regeneration run for IMAGO-3 (PROC-09-REGEN; MET-4.1 G-10); the 02_ derived pair remains queued | Added — Proposed; v2/v3 retained |
| 10_ | `REG-TASK-OWNERS_companion.md` (20,821) — 60 tasks (TASK-REG 24 · NZ 10 · US 13 · EU 13) → DR step · RUN · owner role · account · evidence artifact · R30.3 row (60/60 PRESENT); 7 owner cells [NEEDS DEFINITION] with DEC (QI-0020) · `INDEX-10.1_delta.md` (2,075) | Added — companion; ADVISORY_ONLY; no task status changed |

**Queue closure (survey-3).** EXECUTABLE-NOW 7/7: QI-0018, 0020, 0025, 0024, 0032 BUILT; QI-0019, 0023 CLOSED-BY-MET-2.2 (+ MET-4.1 for G). EXECUTABLE-AFTER-DECISION: QI-0030 drafted (HARDEN-2.2 D-4); QI-0001, QI-0029 remain with the Architecture owner (DEC-24, DEC-25; text in MET-2.2 §5). Recommended weight-2: QI-0022, 0043, 0044, 0063, 0010, 0011, 0013, 0014 BUILT. Not built: DEPLOY-1.2 (RTO/RPO — infrastructure owner's values, DEC-23 values Open); 00_FRONTMATTER.schema.json and SEC-2.1 (future files; not recommended by the Queue). Full table: `11_prompts/runs/2026-09-05_sprint-2/RUN-REPORT.md` §2.

**Ledger debt — cleared.** Every tracked file outside run directories (416) now has exactly one HARDEN-1/1.1/1.2 row and one HARDEN-3.1/3.2 task (files without a row after this sprint: 0); the A-005..A-009 debt is paid. Owner cells still `[NEEDS DEFINITION]` after HARDEN-1.2: 46 corpus owner (03_), 13 manifest owner — neither role is named in MET-2.2 §1 (OPEN_QUESTIONS 3).

**ID census (this amendment).** G: 11 declared (MET-4.1). RGAP: declared, 0 minted. R29-row ids: 0..419. T: 000..945 across HARDEN-3, 3.1, 3.2 (422 tasks). C/DEC unchanged (17 / 26, A-009). `A-001..010` = 10 amendments; `DEF-001..008` = 8 defect rows (DEF-008 closed by the inventory successor; its row stands).

**Verification at seal (2026-09-05; outputs in the run directory).** Reference check over every changed file: dead paths 0, unresolved anchors 0 · frontmatter: 0 core-field gaps among new files, 0 minting files without a prefix · depth: 0 deeper than four · schemas: 4 check_schema OK, examples agree, R30.3 549/549 valid · mermaid 10.9.8: 22/22 sources and inlined blocks PASS (v2, v3, v4) · byte counts quoted inside generated files brought to a fixed point and equal to disk · CHECKSUMS_BEFORE/AFTER: pre-existing changes = this manifest (appended) and `README.md` (+1 row) only.

**Honesty lines (extending §11–§15).** Sprint-2 built documents; it ran no pass, wrote no R29 row, closed no decision, gap, ASSUME or gate; the alias laws are Proposed until DEC-26; no RTO/RPO value exists; nothing under 03_ was written; the Impeccable detector's verdict on the v4 page is the audit workflow's · the vendored Impeccable skill pack is enumerated in the ledger because MT2 §3 says every artifact gets a row — its hardening is by version pin (OPEN_QUESTIONS 7).

**Process (requirement).** The PR carrying this amendment is opened by Kenny-bytes so that the Copilot review is auto-requested under ruleset 22326380; it is to be merged only after that review has posted and its findings have been addressed on the branch, per the A-007 process note.
