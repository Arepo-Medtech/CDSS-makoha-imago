# ORIENTATION — sprint-1 (2026-09-05): close the survey-2 Build-Spec Queue

**Executor:** Claude Code (Fable 5.1), desktop session at the repository root; branch `sprint-1-build-spec-queue` from `main` (6aae5d6). **Mandate:** the repository owner asked to "run a SPRINT to close the Build-Spec Queue which finalises the Design Ecosystem" (5 Sep 2026). **Laws inherited:** PROMPT-SURVEY-2 §1 laws 1–10 (append-only with checksum bookends; EXEC-1 precedence; delta-reading; OPEN means OPEN; retained-verbatim never rewritten; hardening is not this pass; no silent shortcuts; evidence or nothing; no remotes beyond this repository's own PR flow; reuse survey-2 outputs).

## Inputs read in full
`11_prompts/runs/2026-09-02_survey-2/BUILD_SPEC_QUEUE.md` (all 1,162 lines: §0–§h, 27 build specs, assumptions, confidence) · `PARITY_STANDARD.md` · `CENSUS.md` · `CHAIN.md` · `PROPOSED_AMENDMENTS.md` · `OPEN_QUESTIONS.md` · `HALT_LOG.md` · all seven `folders/*/ASSESSMENT.md` and `FIRST_REQUIREMENTS.md` · `tools/*.py`, `tools/mermaid/parse.mjs` · `00_MANIFEST.md` (all, A-001..A-003) · `README.md` · 04_ all four files · 05_ all six · 06_ REPO-MAP + skeleton listing (90) + eight exemplar files · 07_ all five · 08_ RESEARCH-1 · 09_ four sources + page · 10_ EXEC-1, FOLD-1, REG-SPRINT v1.0 + 1.1, validate_reg.py in full; REG-POSTURE v1.2 §0.3–0.9, §1–§1.1, §3–§4.4, §7 Phase 0, §8–§13; REG-NZ v1.1 §1, §6, §8–§12; MAK-GOV §1–§2, NDG-1..5, §4 G0, §5–§6; heads of REG-US / REG-EU · 01_ MET-1.1, MET-2, MET-2.1, MET-3, MET-4; MET-1 §9.4 · 02_ primers_briefing; Arch §10, §11.1–11.5, §12.1–12.3, §13.3, §13.6, §13.9, §14.2, §14.5; A10/F10/E10/L10 annexes · 03_ MANIFEST, corpus_artifacts_briefing, MAK-FFC headings + SPINE-1..9 + App. A–C, MAK-ANT frontmatter/headings/App. B, RUN-REPORT §1 + R6 · 11_ PROMPT-P0 (all), PROMPT-SERIES index, PROMPT-SURVEY-2 §0–§1.

## What changed since the survey (confirmed by diff of census.json against `git ls-files`)
+ `05_/REG-R30.2_seed_delta.md`, `10_/REG-EU_v1.0.md`, `10_/REG-NZ_v1.1.md`, `10_/REG-POSTURE_v1.2.md`, `10_/REG-US_v1.0.md`, `10_/validate_reg.py` (00_MANIFEST §9 A-003, 2026-09-02); README.md and the Confluence mirror action (2026-09-05). Consequences: BSQ-0001 and BSQ-0706 CLOSED by A-003; BSQ-0705 built over v1.2; PROMPT-FOLD-1 folds v1.2 (REG-POSTURE §12.5); R30 row-form seed carries R30.2's four jurisdictions (549 rows, not the ~250 the survey implied).

## Tooling (run-local; gitignored where large)
`.venv` with jsonschema 4.25.1 + pyyaml · `tools/mermaid/` with mermaid 10.9.8 + jsdom 24.1.3 (node v20.20.2; the survey used 10.9.0 — version recorded) · `tools/`: validate_examples.py, r30_seed.py, ledger.py, render_harden.py, render_index.py, proc_fields.py, refcheck.py (survey-2's, re-pointed), identity check (inline).

## Baseline
`CHECKSUMS_BEFORE.txt`: 292 files (sha256; excludes .DS_Store, .git, .playwright-mcp and this run directory) taken on `main` before any write.
