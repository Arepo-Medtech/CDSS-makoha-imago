---
doc_id: HARDEN-1
title: "R29 Hardening Coverage Ledger — SEED"
version: "1.0"
date: "2026-09-01"
status: "Seed only. EVERY row below is PENDING. Zero rows are HARDENED. Row zero is BLOCKED (engine not installed in any evidenced environment). This file becomes R29's opening content on DEC-02 ratification; thereafter the ledger is append-only and written only by the pass."
---

| row | artifact | class | state | blocker / note |
|---|---|---|---|---|
| 0 | agent-skills whole-pack install + inventory confirmation (incl. C-11 reconciliation: live pack = 25 skills incl. meta; release 0.6.4 eval framework) | engine | **BLOCKED** | no installation evidence exists; DEC-10/DEC-11 open |
| 1–3 | CONTRACT-ARG-1 / CONTRACT-DEV-1 / CONTRACT-RRI-1 | CC-7 | PENDING | drafted in 05_ |
| 4–5 | REG-R29 schema / REG-R30 schema+seed | CC-2 | PENDING | |
| 6 | MAK-FFC v1.1 (+Annex J-3) | CC-3 | PENDING | host law |
| 7 | MANIFEST.md | CC-3 | PENDING | precedence law |
| 8 | MAK-ANT v1.0 (+REG-POSTURE verbatim) | CC-4 | PENDING | governs regulatory content |
| 9 | architecture_and_integration.md (+§14) | CC-2 | PENDING | PENDING-VALIDATOR |
| 10 | primer_0 (+§11) | CC-1 | PENDING | charter-exempt from exec blocks; erratum row |
| 11–26 | primer_A..L (+annexes), variant_1b (+§8), variant_2 (+§7), harness (+§10), grounding annex (+§10) | CC-1 | PENDING | sixteen rows, one each |
| 27 | ecosystem_integration_report.md (+addendum 2) | CC-1 | PENDING | validator honesty row |
| 28–40 | makoha-in-flight, degrees-of-truth, left-wing, right-wing, compound-eyes, head, thorax, abdomen, proboscis, labial-palps, legs, execution-layer-sourcing-map, addendum-j3 (standalone) | CC-3 | PENDING | thirteen rows |
| 41 | cdss_complete_stack.md (+notice) | CC-1 derived | PENDING | regeneration queued behind DEC-01 |
| 42 | cdss_diagrams.html (+comment) | CC-6 | PENDING | |
| 43 | 09_diagrams/cdss_diagrams_v2.html + 4 mermaid sources | CC-6 | PENDING | five rows collapsed to one bundle row + 4 source rows at pass time |
| 44–59 | artifacts-html/ (16 pages incl. sleep-tools + stranieri dossiers) | CC-6 | PENDING | sixteen rows |
| 60–71 | 01_ MET set (5), 04_ HARDEN set (3+directive), 06_ REPO-MAP+4 skeleton READMEs → per-file rows, 07_ (5), 08_ (1), 00_MANIFEST | CC-8/CC-2/CC-5 | PENDING | self-referential class last (W10) |
| 72 | corpus-side artifacts (path/class enumeration only; content hardened in-account, evidence via R28) | corpus | **ESCALATED-placeholder** | DEC-12 + corpus credentials; dev-side pass never opens content |
| 73 | HeyDoc instruction-bearing files (CLAUDE.md, AGENTS.md, PROJECT_START_HERE.md, docs/grounding/*, trunk prompts, schemas) | external | PENDING-ENUMERATION | [NEEDS SOURCE] below-README clone inventory (DEC-12/G-08) |

Terminal-state law restated: every row ends HARDENED (evidence attached) or ESCALATED (specific blocker, surfaced in the consolidated report). There is no third state. This seed's PENDING marks are pre-pass placeholders, not a third state — the pass converts each on contact.

**Amendment A-001 (2026-09-01, appended):** the 06_ skeleton set expanded to ~91 files (14 existing-repo skeletons + cdss-integration/GPP-CHANNEL + proposed-repo trees). Ledger consequence: the W8 wave's 06_ rows are enumerated at pass time by path glob over `06_repositories/**` (one row per file, per MT2 §3 — no batching); their class is CC-5 (READMEs/MANIFESTs/CI stubs are instruction-bearing) except CODEOWNERS/pointer stubs (CC-2). All PENDING.
