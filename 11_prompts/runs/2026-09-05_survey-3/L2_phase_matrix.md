# L2_phase_matrix — Layer 2 census (Q-D-08, Q-F-03): planning construct → execution counterpart

Run 2026-09-05_survey-3 · Phase 1 step 2. One row per planning-construct **family** (per-ID detail is in the minting file; the column test is whether the family's table carries the cell at all, then whether any cell is empty). Evidence: `raw/L2_constructs_a.txt`, `raw/L2_constructs_b.txt` (grep of the minting tables with line numbers), the awk owner/exit distributions pasted below. Cell values: ✓ present as a column/field for every row · **partial** present for some rows or only by cross-reference · **✗** absent · n/a not a planning construct.

| Family (count) | Minting file | owner-role | person-or-DEC | timeline-or-gate | verification / exit evidence | register home | Verdict |
|---|---|---|---|---|---|---|---|
| G-01..11 (11) | `01_/MET-4_gap_analysis_and_roadmap.md` l.9 columns `Gap · Evidence · Severity · Delta since v1.0` | ✗ (no owner column; owner inferable only where the Evidence cell names a DEC/C) | ✗ | **partial** — roadmap bullets P0–P3 (l.24–27) give phase windows for *some* gaps by allusion, no per-row cell | ✗ (no "closes when" / exit evidence) | ✗ (MET-4 is "Carried forward from MET-1 v1.0 §17"; no register named — R26/R27 per MET-2's PENDING-REGISTER-HOME applies to C/DEC, not G) | **PHASE-MAPPING-GAP — CRITICAL** (G-02 gates GATE-000; G-03 gates code freeze; weight 2+2) |
| C-01..16 (16) | `01_/MET-2` l.11 `ID · Both positions · Ruling/state`; `MET-2.1` | partial (ruling names ESCALATED → DEC owner) | via DEC | via DEC's Blocking cell | ✗ (ruling state only; "closes when" absent except through the DEC) | PENDING-REGISTER-HOME (R27) — stated in status | PHASE-MAPPING-GAP — WARNING (MT2 §6 requires both positions + state; exit evidence is the missing cell) |
| DEC-01..22 (+ proposed 23) | `01_/MET-2` l.29 `DEC · Decision · Blocking · Owner · State`; `MET-2.1` l.22 `ID · Decision · Trigger/When · Owner · Status` | ✓ | ✓ (persons [NEEDS DEFINITION] on DEC-09/10 — registered) | ✓ (`Blocking` gate / `Trigger/When`) | ✗ — no column says what artifact evidences closure (e.g. "ratification recorded in Arch §12.2 amendment"; "counsel letter dated") | PENDING-REGISTER-HOME (R26) — stated | PHASE-MAPPING-GAP — WARNING (weight 1+2) |
| RG-01..08 (8) | `08_/RESEARCH-1` l.18 `Gap · What's needed · Who`; `RESEARCH-1.1` D-3 `+ Closes into` | ✓ (`Who`) | partial (roles; DEC-12 executor) | ✗ (no trigger/when) | ✓ ("Closes into" register/DEC row — RESEARCH-1.1 D-3) | ✓ (MET-4 G / MET-2 DEC / R30 via D-3) | PHASE-MAPPING-GAP — OPTIMISATION (timeline only; weight 1+1) |
| RUN-0..4 (5) | `10_/EXEC-1` l.81–85 (`RUN · contents · source phases · gate`) | ✗ in EXEC-1; **✓ via `07_/DEPLOY-1.1` DR-1..7** (owner roles per DR, l.45–51) | ✓ via DR (all `[NEEDS DEFINITION]` + resolving DEC) | ✓ (weeks/months + gate) | ✓ via DR-n exit evidence + failure handling (l.60–66) | ✓ R30 gate rows (EX-10) | PRESENT-IMPECCABLE (as a pair EXEC-1 + DEPLOY-1.1; read-through stated in DEPLOY-1.1) |
| DR-1..7 (7) | `07_/DEPLOY-1.1_run-map_delta.md` l.45–66 | ✓ | ✓ | ✓ | ✓ | ✓ | PRESENT-IMPECCABLE — exemplar for Q-D-08 |
| TASK-REG-001..024 (24) | `10_/REG-POSTURE_v1.2.md` §7 tables l.872–940 columns `ID · Task · Gate` | ✗ per task (owner reaches a task only through DEPLOY-1.1 DR-n → phase → task) | ✗ | ✓ (phase window + `Gate`) | partial (status vocabulary §0.4 "DONE-WITH-EVIDENCE — evidence artifact named" is the *rule*; the evidence artifact is not named per task) | ✓ R30.3 (549 rows) | PHASE-MAPPING-GAP — WARNING (owner + evidence cells; weight 1+2; counsel-facing → not CRITICAL because the gate cell is present) |
| NZ-TASK-001..010, US-TASK-001..013, EU-TASK-001..013 | `REG-NZ_v1.1` l.420–429; `REG-US_v1.0` l.337–; `REG-EU_v1.0` l.329–346 — `ID · Task · Gate` | ✗ | ✗ | ✓ | partial (as above) | ✓ R30.3 | PHASE-MAPPING-GAP — WARNING (one row per jurisdiction file) |
| GATE-000..004, NZ/US/EU-GATE | REG-POSTURE l.882–921 (bold prose, §12.2 check 2 caveat); REG-NZ l.408–410, REG-EU l.320–323, REG-US l.328–331 (`Gate · Meaning · Predecessors · Exit`) | ✗ (gate owner = attesting party, named in the ASSUME rows not the gate row) | via ASSUME-REG | ✓ | ✓ (`Exit` column in NZ/US/EU; prose in AU) | ✓ R30.3 | partial — AU gates in prose (carried defect REG-POSTURE §12.2 check 2) → FORM-DEVIATION already recorded by the file itself; no new row |
| ASSUME-REG-001..009 (+NZ/US/EU) | REG-POSTURE l.961–969 `ID · Assumption · Attesting party · Gate · Status` | ✓ | ✓ (external party) | ✓ | ✓ (ATTESTED/REFUTED with date, §0.4) | ✓ R30.3 | PRESENT-IMPECCABLE — exemplar |
| T-000..T-717 (276) | `04_/HARDEN-3.1` D-2 columns `task · wave · artifact_path · row · class · skills · exit evidence · owner (role) · state · note` | ✓ (awk: 276/276; roles + resolving DEC) | ✓ ([NEEDS DEFINITION] + DEC in every cell) | ✓ (wave; PROMPT-HARDEN sequencing) | ✓ (awk: 0 empty exit-evidence cells) | ✓ (HARDEN-1/1.1 row → R29 on DEC-02) | PRESENT-IMPECCABLE — exemplar |
| V1/V2 sprints, SG gates, SD decisions (30) | `10_/REG-SPRINT-1.2` l.31–60 `ID · Defined at · shape · R30.3 status · Owner role · Exit gate / blocks` | ✓ | partial (roles; SD → MET-2.1 DEC alias) | ✓ (sprint weeks in v1.0; gate) | ✓ (gate rows; `passed` register-only) | ✓ R30 | PRESENT-IMPECCABLE |
| NDG-1..14 (14) | `10_/MAK-GOV` §3 requirement blocks (Statement · Rationale trace); §4 Sprint plan G0–G2 | requirement, not plan — owner is the build (cdss-governance, DEC-16) | via DEC-13/14/16 | ✓ (§4 sprints weeks 1–12) | ✗ per NDG (no acceptance/verification per requirement; DEPLOY-2 NDG criteria are in the seven unbuilt integrations — INDEX-10 §4) | R30.3 (NDG ×14) | PHASE-MAPPING-GAP — WARNING (verification cell; EXECUTABLE-AFTER-DECISION DEC-13/14 — BSQ-0707 already carries the build) → **no new row** (law 11); cited |
| PROC-01..12 (12; 33 steps) | `07_/OPS-1.1` §PROC blocks: Trigger · Steps{timeout,retry,idempotent,on_fail} · Exit evidence · Owner · Source | ✓ | ✓ ([NEEDS DEFINITION] + DEC-09) | ✓ (trigger) | ✓ | — (procedures; R12 adjudication where required) | PRESENT-IMPECCABLE (33/33 CC-5 fields — sprint-1 `proc_fields.txt`) |
| TM-01..18 (18) | `07_/SEC-2` l.100 `TM · Boundary · STRIDE · Threat · Existing control (source) · Gap →` | ✗ (no owner per threat; SEC-2 names the Security owner [NEEDS DEFINITION] once) | ✗ | partial (`Gap →` points at TASK-REG-016 / GATE-002 for some) | ✗ (no verification per threat — the "Gap →" cell is the intent, not the evidence) | — (no register; R-series has no threat register — Arch §12.2 R3 SBOM is the nearest) | PHASE-MAPPING-GAP — WARNING (GATE-002/003 evidence chain; weight 2+1) |
| CC-1..8 (8) | `04_/HARDEN-2` class bars + `HARDEN-2.1` census | spec, not plan (n/a) | | | HARDEN-2.1 self-audit ✓ | HARDEN-2.1 | n/a — PRESENT |
| EX-1..10 (10) | `10_/EXEC-1` requirement blocks | directive, not plan (n/a); EX-10 names the evidence rule for every RUN | | | ✓ (EX-10) | R30 | n/a — PRESENT |

## Folder level (Q-F-03)

| Folder | Execution counterpart named in INDEX | Verdict |
|---|---|---|
| 04 | INDEX-04 §1: "The pass is launched wave by wave with `11_prompts/PROMPT-HARDEN_mt2_pass_launch.md` (draft; runnable after DEC-10/DEC-11 and row zero)" | PASS (decision-gated, stated) |
| 07 | INDEX-07 §3 precedence note: EXEC-1 governs sequence; DEPLOY-1.1 DR table; OPS-1.1 procedures | PASS |
| 10 | INDEX-10 §1: "Read EXEC-1 first…"; §3 ID-family map → R30; counsel packets assembled (`11_prompts/runs/2026-09-05_primer-0/`) | PASS |
| 09 | INDEX-09 §4 PROC-09-REGEN (trigger DEC-01 or source change; owner Architecture owner) | PASS |
| 06 | INDEX-06 §1 instantiation via primers; §4 gaps; REPO-MAP v3 after DEC-09 | PASS (decision-gated, stated) |
| 01 | no INDEX; MET-4 roadmap P0–P3 is the execution counterpart for G/DEC, without owner/verification cells (rows above) | FAIL → the MET-4.1 row |
| 05, 08 | not applicable (P-F-05: contracts executed by PROMPT-A..L; RG resolution HUMAN/EXTERNAL) | n/a |

## Owner-column distributions (awk, 2026-09-05)

```
HARDEN-3.1 owner (role) column, 276 tasks — top values:
  98 Repo owner per REPO-MAP (DEC-09) [NEEDS DEFINITION]
  46 Corpus owner (03_ MANIFEST precedence) [NEEDS DEFINITION]
  30 MT2 operator (DEC-10) / prompt author [NEEDS DEFINITION]
  22 Component owner per primer repo [NEEDS DEFINITION — DEC-09]
  16 Architecture owner (DEC-02) / cdss-spine; R30 rows: cdss-governance
  15 Regulatory owner [NEEDS DEFINITION — G-09 / REG-POSTURE §12.3]
  13 Manifest owner [NEEDS DEFINITION]
tasks 276  empty exit evidence 0
HARDEN-1.1 owner (role) column, 275 rows — same distribution (98/46/30/22/18/15/13/10/9/8/3/1)
```
Every person-level placeholder names its resolving decision (DEC-09, DEC-10, DEC-02, G-09) — P-D-12 satisfied row by row; the *persons* are the survey-2 HUMAN-ONLY rows (BSQ-0110/0209/0394/0405) and are not re-filed (law 11).
