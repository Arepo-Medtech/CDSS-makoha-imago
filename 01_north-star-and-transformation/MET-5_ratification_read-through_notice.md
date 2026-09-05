---
doc_id: MET-5
title: "MET-5 — ratification read-through notice: every retained sentence that the 2026-09-05 rulings (MET-2.2) supersede, by path and line, with the reading that now applies"
version: "1.0"
date: "2026-09-05"
status: "Added (sprint-2). Companion to MET-2.2. Retained files are never edited (AGENTS.md law 1); this notice is the one place a reader checks to learn that a 'proposed' or '[NEEDS DEFINITION]' sentence in a retained file has been overtaken by a ruling. It closes nothing itself; it points at the closure."
change_policy: "Additive; later rulings extend this notice as MET-5.1, MET-5.2 … (never edited in place)"
applies_to: "02_cdss-stack-augmented/architecture_and_integration.md; 01_north-star-and-transformation/MET-1_metamorphosis_plan_v1.0.md; 07_deployment-and-operations/GOV-1_ownership_governance_postdeploy.md; 07_deployment-and-operations/DEPLOY-1.1_run-map_delta.md; 06_repositories/REPO-MAP_v2.md; 09_diagrams/register_topology_v3.mermaid; 10_regulatory-execution/MAK-GOV_addendum-g_v0.9.md; 10_regulatory-execution/REG-POSTURE_v1.2.md"
produced_by: "sprint-2 (MET-2.2 §6 'wording deltas' row) — 11_prompts/runs/2026-09-05_sprint-2/"
---

# MET-5 — ratification read-through notice

Read order: the retained file → this notice → MET-2.2 for the ruling. Line numbers are as on `main`
at 21b9675 (2026-09-05); retained files do not change, so they stay valid.

| # | Retained text (path:line, quoted or summarised) | Ruling | Read it now as |
|---|---|---|---|
| N-01 | `02_cdss-stack-augmented/architecture_and_integration.md` l.511–512 — R29 and R30 rows in the §12.2 register table (pre-ratification; the surrounding text and IMAGO-3 v2/v3 call them "Proposed (DEC-02)") | DEC-02 closed — MET-2.2 §3.4 | R29 Hardening Coverage Ledger and R30 Regulatory Posture Register are ratified registers; schemas of record in `05_registers-and-contracts/` until the cdss-spine move |
| N-02 | `02_cdss-stack-augmented/architecture_and_integration.md` l.515 — "### 14.4 Namespace law extension (amends §13.3 — Proposed) — PFX set gains {FAB, UIC, UIP, GPP}" | DEC-09 closed — MET-2.2 §3.5 | the §13.3 PFX set includes FAB, UIP, UIC, GPP; "Proposed" reads as ratified. The four repositories themselves remain Proposed until created |
| N-03 | `02_cdss-stack-augmented/architecture_and_integration.md` l.441–443 — "### 13.2 Rename notice — `coder_contract.md` is adopted under the name Implementer Contract (IMPL)" (MET-1 l.80: "rename in operational use, ratification open") | DEC-08 closed — MET-2.2 §3.6 | the rename is ratified; IMPL is the documentary name |
| N-04 | `02_cdss-stack-augmented/architecture_and_integration.md` l.481 (§13.7) — "Cadence: one adjudication per level exit plus a standing quarterly review from L4"; `07_deployment-and-operations/GOV-1_ownership_governance_postdeploy.md` l.7 — "cadence (per-level minimum; quarterly-from-L4 proposed, DEC-08)"; `01_north-star-and-transformation/MET-1_metamorphosis_plan_v1.0.md` l.83, 431 — "(proposed quarterly from L4)" | DEC-08 closed — MET-2.2 §3.6 | quarterly from L4 is the ratified Observer cadence; every "proposed" qualifier on it is spent |
| N-05 | `01_north-star-and-transformation/MET-2_conflict_and_decision_register.md` l.39–41 — DEC-09 "Programme lead [NEEDS DEFINITION]", DEC-10 "[NEEDS DEFINITION]" | DEC-09, DEC-10 closed — MET-2.2 §1, §3.2, §3.5 | Programme lead = Kenny-bytes; MT2 operator = Kenny-bytes |
| N-06 | `07_deployment-and-operations/DEPLOY-1.1_run-map_delta.md` l.45–51 — D-2 "Person: [NEEDS DEFINITION]" for DR-1..DR-7 | MET-2.2 §1 | DR-1 Kenny-bytes · DR-2 Kenny-bytes (dispatch) + kendo-Jones (content) · DR-3 kendo-Jones, Kenny-bytes (DEC-02), Ken-nough + kendo-Jones (DEC-03) · DR-4 Ken-E-Gee; operations owner still [NEEDS DEFINITION] · DR-5 Kenny-bytes · DR-6 kendo-Jones + Kenny-bytes; NZ sponsor [NEEDS DEFINITION — DEC-19] · DR-7 kendo-Jones; Kenny-bytes |
| N-07 | `06_repositories/REPO-MAP_v2.md` l.4 — "new rows Proposed (DEC-09)" and no owner column | DEC-09 closed | owners in `06_repositories/REPO-MAP_v3.md`; the proposed repositories stay Proposed as repositories |
| N-08 | `09_diagrams/register_topology_v3.mermaid` l.1 and `09_diagrams/cdss_diagrams_v3.html` §3 — "R29–R30 Proposed (DEC-02)", dashed | DEC-02 closed; DEC-01 regeneration | `09_diagrams/register_topology_v4.mermaid` and `09_diagrams/cdss_diagrams_v4.html` draw them solid; v3 preserved |
| N-09 | `10_regulatory-execution/MAK-GOV_addendum-g_v0.9.md` l.13–16 — `naming_note`: "'Addendum G' and doc_id MAK-GOV are provisional … Namespace is an open decision — see DEC-G1" | DEC-13 closed — MET-2.2 §3.7 | doc_id `MAK-GOV` is permanent; not J-series; the note is spent and is corrected by the corpus/volume owner in the next version (nothing under 10_ edited) |
| N-10 | `10_regulatory-execution/REG-POSTURE_v1.2.md` l.473 — "Ratification: DEC-01 (relabel portfolio-wide) remains Open; closes only on `ASSUME-REG-002`" | DEC-01 closed — MET-2.2 §3.9; C-17 | DEC-01 is Closed (ratified); `ASSUME-REG-002` is OPEN (counsel); GATE-000 unchanged |
| N-11 | `01_north-star-and-transformation/MET-4_gap_analysis_and_roadmap.md` l.19 — "G-09 DR/RTO/RPO, org owners, commercial thresholds — [NEEDS DEFINITION]" | DEC-23 names closed — MET-2.2 §3.10 | owners named (kendo-Jones, Ken-nough, Ken-E-Gee); RTO/RPO, drill protocol and commercial thresholds still owed (MET-4.1 G-09) |
| N-12 | `04_hardening/HARDEN-1.1_coverage_ledger_seed_delta.md` — owner cells "Repo owner per REPO-MAP (DEC-09) [NEEDS DEFINITION]" ×98, "MT2 operator (DEC-10) … [NEEDS DEFINITION]" ×38, "Component owner per primer repo [NEEDS DEFINITION — DEC-09]" ×22, "Regulatory owner [NEEDS DEFINITION — G-09 …]" ×15, "Operations / security / regulatory owner [NEEDS DEFINITION — G-09]" ×9 | DEC-09, DEC-10, DEC-23 | resolved row by row in `04_hardening/HARDEN-1.2_coverage_ledger_owner_delta.md` D-1 |

## Census and self-audit

Notices: N-01..N-12 = 12. Every path:line above was read on `main` 21b9675 on 2026-09-05; the quoted
fragments are verbatim where quotation marks appear. `grep -c '^| N-' 01_north-star-and-transformation/MET-5_ratification_read-through_notice.md` → 12.
Every ruling cited is a Closed row in MET-2.2 §2 (DEC-01, 02, 08, 09, 10, 13, 23-names). No retained
byte changed (sprint-2 CHECKSUMS). Ledger row and task for this file: HARDEN-1.2 / HARDEN-3.2 (same sprint).
