---
doc_id: MET-2.1
title: "MET-2.1 — Conflict & Decision Register Delta (Imago v1.2)"
version: 1.0
date: "2026-09-01"
status: "Added. Additive delta to MET-2 per the MET-1.1 pattern; MET-2 v1.0 is not edited. Read MET-2 through this file."
---

# MET-2.1 — Register delta

## New conflicts

| # | Conflict | Handling |
|---|---|---|
| C-13 | REG-POSTURE standalone v1.1 (10_, canonical) ⟷ MAK-ANT Annex 1 (v1.0, mirror) | **Deliberate, dated divergence** under EX-3; closes when FOLD-1 W5 passes. Not silent; validator exception recorded until fold |
| C-14 | MAK-J3 (exempt-tier reserve, folded) ⟷ REG-POSTURE v1.1 §2.1/§3.1 + MAK-GOV (retirement argued; GOV named as replacement non-classified route) | **ESCALATED → DEC-06 (reframed)**: retirement ratification, not approval. Until closed, J-3 is neither built nor retired (EX-4) |
| C-15 | MAK-TXC/PRB patient face ⟷ MAK-GOV NDG-2 (no patient-specific output) | **No conflict** — different faces; GOV releases the abdomen, not the thorax. Recorded to prevent the misreading |
| C-16 | Arch §11.4 Bedrock-PrivateLink ⟷ REG-SPRINT V2 pinning requirement | Same substance as C-03; **no new escalation** — DEC-03 already owns it; sprint plan defers to DEC-03 per REG-POSTURE v1.1 §5.1 |

## New decisions

| ID | Decision | Trigger/When | Owner | Status |
|---|---|---|---|---|
| DEC-13 (=DEC-G1) | MAK-GOV namespace & doc_id (G-series vs J-series vs new) | Before FOLD-1 | Architecture owner | Open |
| DEC-14 (=DEC-G2) | Ship the non-device Governance Layer as first revenue | `SG-V1-0` (counsel attests) | Founder + advisor | Open |
| DEC-15 (=DEC-G3) | NDG-3 latency floor value | Sprint V1-S0 | Regulatory + product | Open |
| DEC-16 (=DEC-G4) | cdss-governance repo split (register-home vs product) | V1-S1 | Architecture owner | Open |
| DEC-17 (=SD-01) | V1 use case — pharmacist scope-expansion governance recommended | RUN-0, week 1–2 | Founder + advisor | Open |
| DEC-18 (=SD-02) | V2 clinical domain | — | Clinical + regulatory | **Provisionally resolved: respiratory** (REG-SPRINT-1.1 D-3); checkpoint month 4 |
| DEC-19 (=SD-03) | NZ sponsor structure (NZ entity vs contracted) | `NZ-GATE-0` | Founder + NZ counsel | Open |
| DEC-20 (=SD-04) | V2 supplies Australia pre-ARTG, or NZ-only | Before `V2-S3b` | Founder + counsel | Open |
| DEC-21 (=SD-05) | Governance Layer namespace/repo (merges into DEC-13/16 at ratification) | — | Architecture owner | Open |
| DEC-22 | Adopt EXEC-1 precedence (EX-1) and the run map (EX-5) | Now | Founder (programme) | Open — adopting v1.2 as working set closes it |

**Alias law:** DEC-13..21 are the register homes; the SD-*/DEC-G* names remain valid
citations and resolve here. One decision, two names, one row.

## Standing escalations (extends MET-2's list)
C-13 (until fold) · C-14/DEC-06 · DEC-17 (blocks all V1 commercial work) ·
`NZ-Q-004` + `NZ-ASSUME-005` (the working assumption the schedule leans on).
