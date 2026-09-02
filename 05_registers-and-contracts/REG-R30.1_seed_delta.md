---
doc_id: REG-R30.1
title: "R30.1 — Regulatory Posture Register seed delta (Imago v1.2)"
version: 1.0
date: "2026-09-01"
status: "Added. Additive seed rows over REG-R30 schema+seed; the v1.0 seed file is not edited. Same row fields; same write law (external attestations only for ASSUME closures)."
---

# R30.1 — Seed delta

**Scope extension:** R30's `reg_id` enum extends additively with: `NDG-*`,
`NZ-FIND-*`, `NZ-OBL-*`, `NZ-ASSUME-*`, `NZ-TASK-*`, `NZ-WATCH-*`, `NZ-Q-*`,
`SD-*` (as DEC aliases per MET-2.1), `SG-*`, `EX-*`, `REG-KEEP-*` (present in v1.0
usage, formalised in the enum here per REG-POSTURE v1.1 §0.3 note).

**New rows (verbatim statuses at source, 2026-09-01):**
- REG-FIND-009..011 OPEN (011 flagged: secondary source `SRC-REG-012`, re-anchor before GATE-000)
- ASSUME-REG-008 OPEN (counsel; DEC-06) · ASSUME-REG-009 OPEN (counsel; `SG-V1-0`)
- OBL-013..014 standing · STD-013 standing · TASK-REG-021..022 not started
- WATCH-REG-006 semi-annually · WATCH-REG-007 annually+pre-EU
- Q-REG-008..010 open · SRC-REG-011..014 recorded (012 = secondary, caution carried)
- NZ-FIND-001..009 OPEN · NZ-OBL-001..010 standing · NZ-ASSUME-001..004 OPEN ·
  **NZ-ASSUME-005 OPEN** (transition-provisions working assumption; owner founder;
  closes on `NZ-Q-004` answer or Bill text; consequence pre-registered in EX-7) ·
  NZ-TASK-001..008 not started · NZ-WATCH-001 monthly, 002 quarterly, 003
  semi-annually · NZ-Q-001..004 open
- NDG-1..14 proposed-normative (activate on DEC-14) · SG-V1-0..2 / SG-V2-0..3a/3b
  not passed · SD-01..05 → MET-2.1 rows (SD-02 provisionally resolved, checkpoint
  month 4) · V1-C1..C2 not started · EX-1..10 in force on DEC-22
- **Status-vocabulary note:** rows use the REG-POSTURE v1.1 §0.4/§0.7 crosswalk;
  `REFUTED` is now available register-side per the v1.1 amendment A-1.

**Cross-joins added:** NZ-ASSUME-004 ↔ V2-E5 ↔ GATE-003 evidence · ASSUME-REG-009 ↔
DEC-14 ↔ SG-V1-0 · NZ-ASSUME-005 ↔ V2-S3a scheduling · C-13 ↔ FOLD-1 W5.
