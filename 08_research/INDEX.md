---
doc_id: INDEX-08
title: "INDEX-08 — 08_research: briefing, file table, RG register mirror, honesty line, self-audit"
version: "1.0"
date: "2026-09-05"
status: "Added (sprint-1); indexes only; RESEARCH-1 v1.0 has no status field (supplied by RESEARCH-1.1 D-1); no finding fabricated; no literature re-fetched this sprint"
folder: "08_research/"
produced_by: "sprint-1 (survey-2 Build-Spec Queue) — generated tables from disk by 11_prompts/runs/2026-09-05_sprint-1/tools/render_index.py; briefing text authored; edits nothing"
---

# INDEX-08 — 08_research

## §1 Briefing — what a research / source map is

A **research map** separates what was *supplied* (the evidence base of the volumes, authoritative in their owners), what was *newly verified* (dated fetches), what is a *gap* (RG-nn — a question an owner must answer) and what is *proposed* (named future engagements). It cites and never restates. An RG closes when its owner's action lands as a finding in a RESEARCH-1.n delta **and** the register or decision row it "closes into" (MET-4 G-*, MET-2 DEC-*, R30) is updated by that row's owner (RESEARCH-1.1 D-3). RESEARCH-1 never closes a DEC, ASSUME or WATCH itself.

## §2 File table

| path | class | doc_id | version | date | status (quoted) | bytes | disposition | HARDEN-1/1.1 row | HARDEN-3.1 task | 00_MANIFEST row | read-through rule |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `08_research/INDEX.md` | CC-8 | INDEX-08 | 1.0 | 2026-09-05 | Added (sprint-1); indexes only; RESEARCH-1 v1.0 has no status field (supplied by RESEARCH-1.1 D-1); no finding fabricated; no literature re-fetched this sprint | 4680 | Added (sprint-1) | 216 | T-715 | §1 row (1) + A-004 | — |
| `08_research/RESEARCH-1.1_findings_delta.md` | CC-8 | RESEARCH-1.1 | 1.1-delta | 2026-09-05 | Added. Additive delta over RESEARCH-1 v1.0 (not edited); read RESEARCH-1 through this file. Registers findings that until now lived only in 11_prompts (PROMPT-SERIES evidence pack) and 05_ (R30.1/R30.2 sources). Quotes, … | 5357 | Added (sprint-1) — Proposed | 217 | T-107 | §1 row (1) + A-004 | — |
| `08_research/RESEARCH-1_findings_gaps_source_map.md` | CC-8 | RESEARCH-1 | 1.0 | 2026-09-01 | — | 3129 | Added | 218 | T-106 | §1 row (1) + A-004 | read through RESEARCH-1.1 (status field; RG-07/08; closure path) |

## §3 RG register mirror

| Gap | What's needed | Who | State | Closes into |
|---|---|---|---|---|
| `RG-01` | HeyDoc below-README clone inventory | DEC-12 executor | OPEN | DEC-12 (MET-2); G-08 (MET-4) |
| `RG-02` | Counsel reading of the two MAK-J3 ⚑ flags | AU counsel | OPEN | Q-REG-009 / ASSUME-REG-008 (R30); DEC-06 |
| `RG-03` | Baseten Sydney dedicated terms in writing | Baseten | OPEN | ASSUME-REG-004 (R30); DEC-03 |
| `RG-04` | immudb BUSL redistribution terms | Legal | OPEN | C-05 / DEC-04 (MET-2) |
| `RG-05` | Conformal-for-LLM literature watch | cdss-conformal owner | OPEN | MAK-ELSM §05 watch; WATCH row proposed on DEC-02 |
| `RG-06` | TGA AI-enabled-SaMD guidance read against the intended purpose | Regulatory owner | OPEN | WATCH-REG-002 (R30); TASK-REG-001 |
| `RG-07` | Lumos cohort figure reconciliation (6.8M+ vs 1.3M / 16% of NSW); locate or NOT-LOCATED the 2025 cohort study | cdss-lumos owner / PROMPT-H run | OPEN (new, RESEARCH-1.1) | Primer H annex erratum; TASK-REG-015; H10 |
| `RG-08` | Primary-care differential-diagnosis conformal-prediction evidence — none located | cdss-conformal owner | OPEN (new, RESEARCH-1.1) | RG-05 watch; Primer F F10; DEPLOY-2 §1 |

## §4 Honesty line

§1 sources not re-verified this pass unless noted; §2 fetches dated 1 Sep 2026 (v1.0) and 2 Sep 2026 (PROMPT-SERIES evidence pack, registered by RESEARCH-1.1); all eight RG OPEN; no clinical number asserted; RG-01 waits on DEC-12 (Corpus custodian).

## §5 Self-audit (run 2026-09-05)

- File count in the table = files on disk under `08_research/` (excluding `.DS_Store`): **3** = 3 — PASS.
- Every path in the table exists — PASS (3/3 at generation; this INDEX itself is written by the same run).
- Every HARDEN-1/1.1 row id and HARDEN-3.1 task id in the table resolves in `04_hardening/HARDEN-1.1_coverage_ledger_seed_delta.md` / `HARDEN-3.1_task_register_delta.md` — PASS (ids taken from the same generated data; 0 ABSENT).
- RG-01..08 = 8 = RESEARCH-1.1 req_count — PASS; every 'closes into' target resolves (grep) — PASS.
```
$ ls -l 08_research
total 40
-rw-r--r--@ 1 ken-lee-arepo  staff  4680 Sep  5 16:12 INDEX.md
-rw-r--r--@ 1 ken-lee-arepo  staff  5357 Sep  5 15:48 RESEARCH-1.1_findings_delta.md
-rw-r--r--@ 1 ken-lee-arepo  staff  3129 Sep  4 05:13 RESEARCH-1_findings_gaps_source_map.md
```
