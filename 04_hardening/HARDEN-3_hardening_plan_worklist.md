---
doc_id: HARDEN-3
title: "Hardening Worklist — dependency-ordered, one task per artifact (the /plan artifact)"
version: "1.0"
date: "2026-09-01"
status: "Proposed — no task started; ledger rows in HARDEN-1 all PENDING"
rules: "/build auto permitted: plan approved once, every task still runs test-driven, commits individually (~100-line atomic), pauses on failures. Context growth is handled by ledger checkpointing + phase-scoped skill loading, never by summarizing coverage (MT2 §4)."
---

# Wave order (dependency-driven)
| Wave | Tasks | Why this order |
|---|---|---|
| W0 | T-000 row zero: install whole pack; confirm inventory vs live repo (C-11); record output | nothing starts before it (MT2 §2.1) |
| W1 | T-001..003: spine contracts — CONTRACT-ARG-1, CONTRACT-DEV-1, CONTRACT-RRI-1; T-004 R29 schema; T-005 R30 schema+seed | everything else cross-references these |
| W2 | T-010 MAK-FFC (+Annex J-3); T-011 MANIFEST | host law before anything that cites it |
| W3 | T-020 MAK-ANT/REG-POSTURE; T-021 R30 reconciliation | governs regulatory content; feeds CC-4 checks everywhere |
| W4 | T-030..045: Arch(+§14), Primer 0(+§11), A..L(+annexes), J-1, J-2, harness, annex H-1, integration report(+addendum 2) — one task each, sixteen tasks | components after their host + contracts |
| W5 | T-050..062: remaining Mākoha volumes (MIF, DOT, LWC, RWC, CEC, HDC, TXC, ABC, PRB, LBP, LEG, ELSM, J-3 standalone) — one each | consolidations/faces after host + components |
| W6 | T-070..072: derived artifacts — complete stack regeneration-notice row, cdss_diagrams.html, cdss_diagrams_v2.html + mermaid sources | after their sources settle |
| W7 | T-080..095: artifacts-html (16) — CC-6 bar each | browser class, independent |
| W8 | T-100..107: 05_/06_/07_/08_ documents of this repository | after everything they index |
| W9 | T-110 corpus-side rows (in-account execution, aggregate evidence via R28) — ESCALATED placeholder until DEC-12 + credentials | firewall-preserving path |
| W10 | T-120 MT2 directive; T-121 HARDEN-1/2/3; T-122 MET set — the self-referential class, last | CC-8 |
| W11 | T-130 cross-portfolio integrity sweep AFTER last edit (all refs, shared IDs, partitions) — output captured; T-131 /ship gate; T-132 wire checks into CI (ratchet) | MT2 §7(3)–(4) |

Every task: load mapped skills per HARDEN-2 class bar; doubt-driven-development ALWAYS ON; per-task ledger row closed HARDENED-with-evidence or ESCALATED-with-blocker before the next task starts (in /build auto, pause-on-failure preserves this).
