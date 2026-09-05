# ORIENTATION — survey-3 run (2026-09-05)

Run directory: `11_prompts/runs/2026-09-05_survey-3/` · Executor: Claude Code (desktop session, same session that authored PROMPT-SURVEY-3.1/3.2) · Instrument: `11_prompts/PROMPT-SURVEY-3_final-quality-improvement.md` v1.0 **read through** `PROMPT-SURVEY-3.1_deep-review_fold_delta.md` (D-1..D-9) **and** `PROMPT-SURVEY-3.2_confidence_erratum_delta.md` (E-1..E-3), per AGENTS.md read order (A-007).

## Baseline

```
$ git rev-parse HEAD
99e47f39e799be7a9e15dfefbce03396f88698f3        (main; merge of PR #13 — A-007)
$ git status --short | wc -l
0
$ git ls-files | wc -l
511
$ git ls-files | grep -v '^\.github/\|^\.claude/\|^\.impeccable/\|^11_prompts/runs/\|\.DS_Store$\|^\.gitignore$\|^\.gitattributes$' | wc -l
271                                              (files in survey scope — v1.0 seed said 267 at f9f8ab2; +4 since: PROMPT-SURVEY-3, 3.1, 3.2, and A-005's .github/copilot-instructions.md is excluded → see CENSUS for the exact reconciliation)
```

Attribution baseline (3.1 D-3): sprint-1 merge `b810db0`. Commits to `main` after it and before this run: PR #5/#6 (mirror config), PR #7 (PROMPT-SURVEY-3), PR #8 (A-005: AGENTS.md, CLAUDE.md, .github/*, Impeccable skill), PR #9/#10 (copilot-review-test run dir), PR #12 (A-006: 3.1), PR #13 (A-007: 3.2). Text changed by those commits is NEW-SINCE-BASELINE; everything else PRE-EXISTING.

Tools: Python 3.9.6 (system); run-local interpreter for `yaml`/`jsonschema` = `11_prompts/runs/2026-09-05_sprint-1/.venv/bin/python` (PyYAML 6.0.3, jsonschema 4.25.1) — reused, not reinstalled; node v20.20.2; mermaid parser `.github/audit/mermaid/parse.mjs` (node_modules absent locally → TOOL-UNAVAILABLE for mermaid in this run; CI result of 2026-09-05 cited instead).

## Phase 0 step 1 — files read, with anchors

| File | Bytes | Anchors read | Why it matters here |
|---|---|---|---|
| `00_MANIFEST.md` | 37,488 | §1–§6; §7 A-001 … §13 A-007 (all amendments) | parent of every file (Layer 1); honesty lines §4.4; defect log §5 + DEF-003..007 |
| `04_hardening/INDEX.md` | 7,701 | §1 briefing; §2 file table; §4 honesty; §5 self-audit | folder parent; honesty line = governance evidence |
| `05_registers-and-contracts/INDEX.md` | 16,390 | §1; §2; §3 reading rule (P-D-11); §4; §5 | same |
| `06_repositories/INDEX.md` | 49,928 | §1; §2 tree table (19); §3 file table (96); §4 known gaps; §5 | same; §4 carries 13 unbannered files (DEF-004) |
| `07_deployment-and-operations/INDEX.md` | 7,451 | §1; §2; §3 precedence; §4; §5 | same |
| `08_research/INDEX.md` | 4,680 | §1; §2; §3 RG mirror; §4; §5 | same |
| `09_diagrams/INDEX.md` | 10,322 | §1; §2; §3 recorded parse; §4 regeneration PROC-09-REGEN + defects (R25 label; §7.4); §5 | same; Layer 3 seed R25 |
| `10_regulatory-execution/INDEX.md` | 12,762 | §1; §2; §3 ID-family map; §4 known gaps (FOLD-1 W-namespace; MAK-GOV no Contents/census); §5 | same; Layer 3 seed W1–W5 |
| `11_prompts/runs/2026-09-02_survey-2/PARITY_STANDARD.md` | 20,799 | Part A P-D-01..16; Part B P-F-01..10; notes | inherited parity lines (v1.0 Phase 0 step 2: Q-lines reference, never restate) |
| `11_prompts/runs/2026-09-02_survey-2/CLASS_CONTRACTS.md` | 9,141 | §1 floor (21 labels); §2.1 additions; §2.2 P-line applicability per class | class labels used in every row |
| `11_prompts/runs/2026-09-02_survey-2/BUILD_SPEC_QUEUE.md` | 95,298 | §b verdicts; §c queue (27/5/10); §d sequenced roll-up | law 11: sprint-1 closed every EXECUTABLE-NOW row |
| `11_prompts/runs/2026-09-05_sprint-1/RUN-REPORT.md` | 12,465 | §0 append-only proof; §1 coverage; §2 queue closure table; §4 honesty; §5 hand-back | baseline for attribution; what was built |
| `11_prompts/runs/2026-09-05_sprint-1/OPEN_QUESTIONS.md` | 4,393 | items 1–19 | interpretive calls already made (not re-litigated) |
| `04_hardening/HARDEN-1.1_coverage_ledger_seed_delta.md` | 51,782 | frontmatter (`req_prefix: R29-row`, `req_count: 275`); scope rule (l.22–26); D-0..D-3; ID census; self-audit | Layer 1 ledger parent; Layer 2 owner column |
| `04_hardening/HARDEN-3.1_task_register_delta.md` | 134,486 | frontmatter (`req_prefix: T`, `req_count: 276`); D-1 statement; D-2 table head; wave census | Layer 2 planning construct T-nnn by wave |
| `02_cdss-stack-augmented/architecture_and_integration.md` | 50,574 | §12 + §12.1 register laws (1)–(6); §13.2 rename; §13.3 namespace law; §14.1 (C-02 ruling); §14.4 PFX extension | Layer 2 ID lifecycle law; Layer 3 seeds |
| `03_makoha-butterfly-corpus/corpus_artifacts_briefing.md` | 6,891 | Part 1 (frontmatter table; body spine; requirement block; three conventions) | the document design system (Layer 4 for markdown) |
| `02_cdss-stack-augmented/primers_briefing.md` | 5,786 | Part 1 (eleven-part skeleton; two conventions) | same, for primers |
| `01_north-star-and-transformation/MET-2_conflict_and_decision_register.md` | 6,414 | C-01..C-12 (C-02, C-07 quoted); DEC-01..12 | Layer 3 seeds; Layer 2 decisions |
| `01_north-star-and-transformation/MET-2.1_decision_register_delta.md` | 2,952 | C-13..16; DEC-13..22; **alias law** ("One decision, two names, one row") | Layer 2 alias-law exemplar |
| `10_regulatory-execution/REG-POSTURE_v1.2.md` | 96,260 | frontmatter (`id_prefixes` ×12; `supersedes`); §0.3 ID scheme; §0.4 status vocabulary; §0.5 validator conventions (10 checks); §12.1 census (150); §12.2 self-audit (14 checks; check 2 legacy-shape caveat); §12.3 known gaps (no owner field — G-09) | exemplar for Q-D lines on ID lifecycle, status enum, self-audit |
| `10_regulatory-execution/REG-NZ_v1.1.md` | 47,377 | frontmatter (`id_prefixes` ×9); §12.1 census (93; **gate rename** NZ-GATE-0/1/2 → 000/001/002 "v1.0 file is unedited"); §12.2 (12 checks) | the alias/rename exemplar (v1.0 <quality_standard> Layer 2) |
| `README.md` | 6,013 | Layout; Laws of the corpus; How to cite; How to change it | root parent; law text |
| `AGENTS.md` | — | laws 1–7; read order (through 3.1 and 3.2) | executor's standing order |

Also read for the delta-reading rule: `11_prompts/PROMPT-SURVEY-3.1_deep-review_fold_delta.md` §3 D-1..D-9; `11_prompts/PROMPT-SURVEY-3.2_confidence_erratum_delta.md` §1 E-1..E-3. Applied before Phase 0 opened: QI schema gains `confidence`, `confidence_reason`, `attribution`, `calibrated_weight`, `calibration_note`, `scorer_failed` (oneOf); laws 16–17; Phase 4 step 2a; COVERAGE-GAP rule; §i/§j; T-11..T-14.

## Scope statement

In scope: every tracked file except `.github/**`, `.claude/**`, `.impeccable/**`, `11_prompts/runs/**`, `.DS_Store`, `.gitignore`, `.gitattributes` (271 files). ROOT = `README.md`, `AGENTS.md`, `CLAUDE.md`, `00_inventory.txt` (if present), `00_MANIFEST.md` is folder 00. `.github/` is read as tooling evidence (audit scripts) but not surveyed as a design asset; its governance text (`copilot-instructions.md`) is cited where Layer 2 governance needs it.

## Fan-out decision

Phases 2–3 run **sequentially in this session** (v1.0: "If the environment forbids sub-agents, run sequentially; nothing else changes"). Reason recorded: the session already holds the orientation context; per-folder sub-agents would re-read ~600 KB each and the coverage-gap rule (3.1 D-5) is easier to satisfy in one writer. The D-6 template is therefore not instantiated this run; HALT_LOG notes it.
