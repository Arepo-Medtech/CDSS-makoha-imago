---
doc_id: FOLD-1
title: "FOLD-1 — MAK-ANT v1.1 fold worklist (REG-POSTURE v1.0 → v1.1)"
version: 1.0
date: "2026-09-01"
status: "Added (Imago v1.2). Worklist only — executing it produces MAK-ANT v1.1 as a NEW file; antennae-corpus_v1.0.md is never edited."
owner: "Regulatory owner [NEEDS DEFINITION — same gap as G-09/REG-POSTURE §12.3]"
---

# FOLD-1 — Antennae fold worklist

Per MAK-ANT change policy, the annex changes only by folding a new REG-POSTURE
version. This worklist is everything that fold must do, so it completes in one
sitting under AN-5's rule that the carrier map re-runs before the fold seals.

## W1 — Fold the annex
Produce `antennae-corpus_v1.1.md` as a new file: wrapper Parts 0–4 carried, Annex 1
replaced with REG-POSTURE v1.1 verbatim (from 10_/REG-POSTURE_v1.1.md, the canonical
copy). Frontmatter: version 1.1; changelog entry; `folds_in` updated to v1.1.

## W2 — Re-run the carrier map (AN-5)
Apply REG-POSTURE v1.1 §12.4's fold checklist verbatim — new carriers for
REG-FIND-009/010/011, OBL-013/014, STD-013, TASK-REG-021/022, WATCH-REG-006/007,
ASSUME-REG-008, Q-REG-009 — **plus** rows this worklist adds beyond §12.4:

| New ID family | Carrier |
|---|---|
| MAK-GOV NDG-1..14, ASSUME-REG-009, Q-REG-010 | MAK-GOV; MAK-ABC Part 6 (the face it releases); MET-2.1 DEC-G rows |
| REG-NZ NZ-* families (FIND/OBL/ASSUME/TASK/WATCH/Q/SRC) + NZ-ASSUME-005 | REG-NZ; this wrapper's watch program (AN-6 owns NZ-WATCH-001..003) |
| REG-SPRINT SD-*, SG-*, V1/V2/V3-*, V1-C* | REG-SPRINT (read through the 1.1 delta per EX-2); R30.1 rows |
| EXEC-1 EX-1..10 | EXEC-1; MANIFEST A-002 |

## W3 — Log the signals (AN-6, additive to Part 4)
- **S-4** · NZ TPA repealed; Medicines Act 1981 interim; notification-only device regime confirmed (sources: REG-NZ SRC-001/003/004). Bearing: **new jurisdiction instrument** — feeds AN-11 map.
- **S-5** · Medical Products Bill will regulate SaMD incl. AI (Cabinet, Jul 2025; REG-NZ SRC-005). Bearing: **window-closing signal**; carried as NZ-WATCH-001 monthly.
- **S-6** · REG-POSTURE v1.1 D-2/EX-7 working assumption registered (`NZ-ASSUME-005`). Bearing: internal, logged for completeness.

## W4 — Range-endpoint re-check (DEF-REG-001 discipline)
Verify **both ends** of every family: REG-FIND-011 ✓ OBL-014 ✓ STD-013 ✓
TASK-REG-022 ✓ WATCH-REG-007 ✓ Q-REG-009 ✓ ASSUME-REG-009 (post-GOV) ✓ SRC-REG-014 ✓
NDG-14 ✓ NZ-* endpoints per REG-NZ ✓ EX-10 ✓. Record the check output in the fold's
build log.

## W5 — Seal checks
MAK-ANT Appendix B checks 1–10 against the new file; annex-verbatim byte check
against 10_/REG-POSTURE_v1.1.md; update R30 pointer if the register home moved.
Divergence window (EX-3) closes when W5 passes; record the closure date in MET-2.1
row C-13.
