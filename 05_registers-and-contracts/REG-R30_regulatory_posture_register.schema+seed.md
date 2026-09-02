---
doc_id: REG-R30
title: "R30 — Regulatory Posture Register (schema + seed rows from REG-POSTURE v1.0)"
status: "Proposed (DEC-02). Owner: cdss-governance. Opens: L1. Mutability: versioned. Written by: regulatory owner + external attestations only (no ASSUME-REG-* closes by internal reasoning — MAK-ANT §8). Readers: R19/R23 joins, dossier assembly, board."
---
Row fields: `reg_id` (REG-FIND-* | REG-KEEP-* | ASSUME-REG-* | OBL-* | WATCH-REG-* | Q-REG-* | GATE-* | TASK-REG-* | FORK-REG-*) · `statement` (verbatim from source) · `status` (OPEN | ATTESTED | REFUTED | CLOSED | ARMED | passed) · `attesting_party` · `blocks` · `cadence` (WATCH rows) · `source` (MAK-ANT §) · `version_stamp`.

**Seed (verbatim statuses at source, 2026-09-01):** REG-FIND-001..008 OPEN · REG-KEEP-001..004 standing · FORK-REG-001 OPEN (decision point L4, unchanged) · ASSUME-REG-001..007 OPEN (attesting parties: AU counsel ×3, Baseten, counsel, Ketryx, data custodian) · GATE-000..004 not passed · TASK-REG-001..020 not started · Q-REG-001..007 open · WATCH-REG-001 quarterly · WATCH-REG-002 once-then-annually · WATCH-REG-003 standing caution · WATCH-REG-004 at GATE-002 · WATCH-REG-005 annually. Cross-joins: FORK-REG-001 ↔ R19; dossier substantiation ↔ R23; ASSUME-REG-007 ↔ ASSUME-H-001.
