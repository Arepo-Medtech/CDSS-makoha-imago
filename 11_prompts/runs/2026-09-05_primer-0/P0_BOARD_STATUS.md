# P0 week-one board — status (PROMPT-P0 Phase 2, PARTIAL execution under sprint-1)

This run executed **only** PROMPT-P0 Phase 2 items 1 and 2 (the two the Build-Spec Queue row BSQ-0702 names). Phase 1 (row zero install) and Phase 2 items 3–8 were **not run**: row zero is gated on DEC-10/DEC-11 and installs software outside the repository; items 3–7 are separate executor tasks not in BSQ-0702's spec. Every status below uses the PROMPT-P0 enum.

| EX-8 item | Source ID | Status | Evidence |
|---|---|---|---|
| Counsel packet AU | EX-6; ASSUME-REG-001/002/003/009; Q-REG-001/002/003/010; NZ-ASSUME-004/V2-E5 | IN-PROGRESS — assembled, dispatch is HUMAN-ONLY (founder) | `counsel_packet_AU/COVER.md`, `QUESTIONS.md`, `ATTACHMENTS.md`, `ASSUME_TABLE.md`, `DISPATCH_CHECKLIST.md` |
| Counsel packet NZ | EX-6; NZ-ASSUME-001..003; NZ-Q-004 | IN-PROGRESS — assembled, dispatch is HUMAN-ONLY | `counsel_packet_NZ/*` |
| TASK-REG-001 intended purpose (Mākoha) | REG-POSTURE v1.2 §7 | IN-PROGRESS — executor-drafts-human-decides; DRAFT produced | `DRAFT_TASK-REG-001_intended_purpose.md` |
| T-G01 intended purpose (Governance Layer) | MAK-GOV §4 | IN-PROGRESS — DRAFT produced | `DRAFT_T-G01_intended_purpose.md` |
| V1-S1 synthetic build start | REG-SPRINT-1.1 D-1 | NOT-RUN this sprint (PROMPT-P0 item 3) | — |
| TASK-REG-021 demo-surface triage | REG-POSTURE §7 | NOT-RUN this sprint (item 4) | — |
| V1-C1 R&D-window question | REG-SPRINT-1.1 D-4 | HUMAN-ONLY (specialist) — question text: "Confirm Arepo registration timing against the 10-year R&D incentive window running from inception; first question to the R&D specialist" | REG-SPRINT-1.1 D-4 |
| NZ-TASK-003 conflict declaration draft | REG-NZ v1.1 §8 | NOT-RUN this sprint (item 6) | — |
| DEC-02 validator on annexes | MET-4 P0 | NOT-RUN this sprint (item 7); `find . -name validate_build_plan.py` → none (00_MANIFEST §4.4 PENDING-VALIDATOR confirmed 2026-09-05) | ESCALATED(DEC-02 owner) standing |
| MT2 row zero | HARDEN-3 W0 / T-000 | BLOCKED — DEC-10/DEC-11 open; no install evidence; PROMPT-P0 Phase 1 not run | HARDEN-1 row 0 |

No ASSUME, DEC or posture was closed or presupposed by this partial run.
