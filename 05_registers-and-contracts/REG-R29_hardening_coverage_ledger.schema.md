---
doc_id: REG-R29
title: "R29 — Hardening Coverage Ledger (schema, Arch §12.2 format)"
status: "Proposed (DEC-02). Owner: cdss-spine. Opens: immediately (pre-L1 work permitted). Mutability: append-only. Written by: the MT2 hardening pass only. Readers: operator, all build CI (row-completeness ratchet)."
---
Row fields (JSON Schema beside this file): `row_id` (int, unique) · `artifact_path` (string) · `artifact_class` (enum CC-1..CC-8 | engine | corpus | external) · `skills_deployed` (array of pack skill names) · `non_applicability_notes` (array of {skill, reason} — a stated reason, never a silent omission, MT2 §2.2) · `mechanical_check_outputs` (verbatim text/attachment refs) · `doubt_pass_record` (CLAIM→EXTRACT→DOUBT→RECONCILE→STOP) · `sibling_consistency_set` (artifact IDs checked) · `defects` (array of {found, fix|escalation}) · `state` (enum HARDENED | ESCALATED — no third value) · `evidence_refs` · `version_stamp` (lockfile pin-set — register law §12.1(4), the universal join key). Register laws §12.1(1–6) apply unchanged; the negative audit (§12.1(5)) extends to hardening rows on ratification: an instruction-bearing artifact without a row is a finding.
