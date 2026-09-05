# Dispatch checklist — HUMAN-ONLY (founder)

1. Founder reviews COVER.md, QUESTIONS.md, ATTACHMENTS.md; decides whether to bundle `Q-REG-005/009` into the same engagement.
2. Founder engages Australian regulatory counsel (`TASK-REG-002`) and sends the packet. **The executor does not send.**
3. On dispatch, the following R30 row lands (EXEC-1 EX-10 — "a run exit asserted without its row is not passed"). Proposed row text (register owner writes it):

```json
{"reg_id": "TASK-REG-002", "statement": "Engage Australian regulatory counsel for a written classification opinion … (REG-POSTURE v1.2 §7)", "status": "OPEN", "source_status_verbatim": "IN-PROGRESS — packet dispatched <date>; opinion awaited", "mapping_pending": false, "source": "REG-POSTURE v1.2 §7 Phase 0", "owner": "Founder (programme); regulatory owner [NEEDS DEFINITION]", "jurisdiction": "AU", "blocks": ["GATE-000"], "version_stamp": "PRE-L1: Imago 73460b3 + sprint-1", "definition_shape": "table-row"}
```

4. On receipt of the written opinion: the regulatory owner records ATTESTED or REFUTED with the attestation date against each of `ASSUME-REG-001/002/003/009` and `NZ-ASSUME-004` (R30 rows; REG-POSTURE §8 by a new version, never in place); MET-2 DEC-01 and DEC-07 become decidable.
5. Week-one board status (EX-8): "counsel packets out" → DONE-WITH-EVIDENCE only when step 2 has a dispatch receipt; until then IN-PROGRESS (this packet).
