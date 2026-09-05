# Dispatch checklist — HUMAN-ONLY (founder)

1. Founder engages New Zealand regulatory counsel (`NZ-TASK-001`) in the same week as the Australian packet (EX-6). The executor does not send.
2. On dispatch, proposed R30 row (register owner writes it; EX-10):

```json
{"reg_id": "NZ-TASK-001", "statement": "Engage New Zealand regulatory counsel. Confirm NZ-FIND-001..012, the notification window, sponsor structure, expected classification, and NZ-Q-004.", "status": "OPEN", "source_status_verbatim": "IN-PROGRESS — packet dispatched <date>", "mapping_pending": false, "source": "REG-NZ v1.1 §8 Tasks", "owner": "Founder; NZ sponsor [NEEDS DEFINITION — DEC-19]", "jurisdiction": "NZ", "blocks": ["NZ-GATE-000"], "version_stamp": "PRE-L1: Imago 73460b3 + sprint-1", "definition_shape": "table-row"}
```

3. On receipt: `NZ-ASSUME-001..003` → ATTESTED/REFUTED with date; `NZ-Q-004` answer → `NZ-ASSUME-005` closes (or re-plan per EX-7: `V2-S3a` loses its urgency ranking and RUN-3 re-weights toward `V2-S3b`).
