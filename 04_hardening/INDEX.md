---
doc_id: INDEX-04
title: "INDEX-04 — 04_hardening: briefing, file table, retained-verbatim note, honesty line, self-audit"
version: "1.0"
date: "2026-09-05"
status: "Added (sprint-1); indexes only; edits nothing; the MT2 pass has NOT run — every ledger row is a pre-pass placeholder and zero rows are HARDENED"
folder: "04_hardening/"
produced_by: "sprint-1 (survey-2 Build-Spec Queue) — generated tables from disk by 11_prompts/runs/2026-09-05_sprint-1/tools/render_index.py; briefing text authored; edits nothing"
---

# INDEX-04 — 04_hardening

## §1 Briefing — what these documents are

*Ecosystem-agnostic first.* A **DIRECTIVE** is a standing order: it says what must be true of every artifact it governs and cannot be waived by anything inside a governed document (MT2 preamble). A **SPEC** states the bar an artifact must clear, per class (HARDEN-2: eight classes CC-1..CC-8, a universal exit bar, anti-rationalization rows, stop-the-line rules). A **WORKLIST / PLAN** orders the work — one task per artifact, waves with a stated reason (HARDEN-3 W0–W11; HARDEN-3.1 one row per artifact). A **SEED** is a register's opening content before the register exists (HARDEN-1 + HARDEN-1.1: one row per artifact, all PENDING until the pass converts each on contact). They compose in that order — directive → spec → plan → ledger seed → R29 (the Hardening Coverage Ledger, `05_registers-and-contracts/REG-R29.schema.json`, ratified on DEC-02, written only by the pass). Read the seed's states as placeholders, never as results (HARDEN-1 l.30). The pass is launched wave by wave with `11_prompts/PROMPT-HARDEN_mt2_pass_launch.md` (draft; runnable after DEC-10/DEC-11 and row zero). Form exemplar: `02_cdss-stack-augmented/primers_briefing.md` Part 1.

## §2 File table

| path | class | doc_id | version | date | status (quoted) | bytes | disposition | HARDEN-1/1.1 row | HARDEN-3.1 task | 00_MANIFEST row |
|---|---|---|---|---|---|---|---|---|---|---|
| `04_hardening/HARDEN-1.1_coverage_ledger_seed_delta.md` | CC-8 | HARDEN-1.1 | 1.1-delta | 2026-09-05 | Seed delta; EVERY row is a pre-pass placeholder (PENDING; row 0 BLOCKED; row 72 ESCALATED-placeholder; row 73 PENDING-ENUMERATION); edits nothing; HARDEN-1 v1.0 is preserved verbatim beside this file and its row ids are … | 51782 | Added (sprint-1) — Proposed | 95 | T-702 | §1 row 04_hardening (declared 4) + A-004 (sprint-1 additions) |
| `04_hardening/HARDEN-1_coverage_ledger_seed.md` | CC-8 | HARDEN-1 | 1.0 | 2026-09-01 | Seed only. EVERY row below is PENDING. Zero rows are HARDENED. Row zero is BLOCKED (engine not installed in any evidenced environment). This file becomes R29's opening content on DEC-02 ratification; thereafter the ledge… | 3517 | Proposed (seed) | 68 | T-121 | §1 row 04_hardening (declared 4) + A-004 (sprint-1 additions) |
| `04_hardening/HARDEN-2.1_spec_census_and_self-audit_delta.md` | CC-8 | HARDEN-2.1 | 1.1-delta | 2026-09-05 | Proposed — a SPEC delta is itself an artifact of the pass (CC-8) and gets its own R29 row (HARDEN-1.1 row for this file); NOT hardening (law 6): it adds sources, ids and a self-audit to HARDEN-2 v1.0, which is preserved … | 8836 | Added (sprint-1) — Proposed | 96 | T-703 | §1 row 04_hardening (declared 4) + A-004 (sprint-1 additions) |
| `04_hardening/HARDEN-2_hardening_spec.md` | CC-8 | HARDEN-2 | 1.0 | 2026-09-01 | Proposed — this SPEC is itself an artifact of the pass (MT2 §2.2) and gets its own R29 row; NOT yet executed | 4572 | Proposed | 66 | T-700 | §1 row 04_hardening (declared 4) + A-004 (sprint-1 additions) |
| `04_hardening/HARDEN-3.1_task_register_delta.md` | CC-8 | HARDEN-3.1 | 1.1-delta | 2026-09-05 | Plan delta; no task started; every task PENDING (pre-pass placeholder). HARDEN-3 v1.0 is preserved verbatim beside this file; read HARDEN-3 through this file. Every T-nnn HARDEN-3 v1.0 mints appears here exactly once; ex… | 134486 | Added (sprint-1) — Proposed | 97 | T-704 | §1 row 04_hardening (declared 4) + A-004 (sprint-1 additions) |
| `04_hardening/HARDEN-3_hardening_plan_worklist.md` | CC-8 | HARDEN-3 | 1.0 | 2026-09-01 | Proposed — no task started; ledger rows in HARDEN-1 all PENDING | 2558 | Proposed | 67 | T-701 | §1 row 04_hardening (declared 4) + A-004 (sprint-1 additions) |
| `04_hardening/INDEX.md` | CC-8 | INDEX-04 | 1.0 | 2026-09-05 | Added (sprint-1); indexes only; edits nothing; the MT2 pass has NOT run — every ledger row is a pre-pass placeholder and zero rows are HARDENED | 7701 | Added (sprint-1) | 98 | T-711 | §1 row 04_hardening (declared 4) + A-004 (sprint-1 additions) |
| `04_hardening/MAJOR_TASK_2_anti-laziness-hardening-directive.md` | CC-8 | — | — | — | # ANTI-LAZINESS DIRECTIVE — EXECUTION-LAYER HARDENING | 16194 | Retained (verbatim) | 65 | T-120 | §1 row 04_hardening (declared 4) + A-004 (sprint-1 additions) |

## §3 Retained-verbatim note for MT2

`MAJOR_TASK_2_anti-laziness-hardening-directive.md` is the directive **preserved verbatim** (00_MANIFEST §1 "MT2 directive (verbatim)", §4.1 "VERBATIM copies: 34/34 checksum-identical"). sha256 at 2026-09-05: `d286d8425ecc27930d5e6015f1248f89248196d19d6381188f6e9528095f728e` — identical to `11_prompts/runs/2026-09-05_sprint-1/CHECKSUMS_BEFORE.txt`. It has no YAML frontmatter by design; it is judged by this index row and hardened as a companion set (T-120), never edited. **Citation notation rule (00_MANIFEST §5 DEF-002):** MT2 §1 and §7 contain numbered *items*, not subsections — cite `§1(7)`, `§7(4)`, never `§1.7`/`§7.4` (§2.1–2.3 are real subsections). The two residual `§7.4` instances DEF-002 missed (09_ v2 topology source + page) are carried in superseded files and fixed in their v3 successors (DEF-003, A-004).

## §4 Honesty line (mirrors 00_MANIFEST §4.4)

The MT2 pass has **not** been executed: R29 rows 0–73 (v1.0) and 74–273 (HARDEN-1.1) are PENDING; row 0 is BLOCKED (no installation evidence; DEC-10/DEC-11 open); `validate_build_plan.py` is not in the tree (PENDING-VALIDATOR); no task in HARDEN-3 / HARDEN-3.1 has started (`ls 11_prompts/runs` → survey-2, sprint-1, primer-0 partial — no `_harden-W*` run exists). HARDEN-2.1, HARDEN-1.1 and HARDEN-3.1 are Proposed deltas awaiting the architecture owner (DEC-02) and the MT2 operator (DEC-10).

## §5 Self-audit (run 2026-09-05)

- File count in the table = files on disk under `04_hardening/` (excluding `.DS_Store`): **8** = 8 — PASS.
- Every path in the table exists — PASS (8/8 at generation; this INDEX itself is written by the same run).
- Every HARDEN-1/1.1 row id and HARDEN-3.1 task id in the table resolves in `04_hardening/HARDEN-1.1_coverage_ledger_seed_delta.md` / `HARDEN-3.1_task_register_delta.md` — PASS (ids taken from the same generated data; 0 ABSENT).
- HARDEN-1.1 ↔ HARDEN-3.1 parity: every 04_ path has exactly one row and one task — PASS.
- MT2 sha256 matches CHECKSUMS_BEFORE — PASS.
```
$ ls -l 04_hardening
total 472
-rw-r--r--@ 1 ken-lee-arepo  staff   51782 Sep  5 16:12 HARDEN-1.1_coverage_ledger_seed_delta.md
-rw-r--r--@ 1 ken-lee-arepo  staff    3517 Sep  4 05:13 HARDEN-1_coverage_ledger_seed.md
-rw-r--r--@ 1 ken-lee-arepo  staff    8836 Sep  5 16:04 HARDEN-2.1_spec_census_and_self-audit_delta.md
-rw-r--r--@ 1 ken-lee-arepo  staff    4572 Sep  4 05:13 HARDEN-2_hardening_spec.md
-rw-r--r--@ 1 ken-lee-arepo  staff  134486 Sep  5 16:12 HARDEN-3.1_task_register_delta.md
-rw-r--r--@ 1 ken-lee-arepo  staff    2558 Sep  4 05:13 HARDEN-3_hardening_plan_worklist.md
-rw-r--r--@ 1 ken-lee-arepo  staff    7701 Sep  5 16:12 INDEX.md
-rw-r--r--@ 1 ken-lee-arepo  staff   16194 Sep  4 05:13 MAJOR_TASK_2_anti-laziness-hardening-directive.md
```
