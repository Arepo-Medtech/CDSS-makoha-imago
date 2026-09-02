# ORIENTATION — run 2026-09-02_survey-2 (PROMPT-SURVEY-2)

Executor: Claude Code (Cowork session), repository root `makoha-imago-v1.2/`, operating on the user's machine via mounted folder. `{{RUN_DATE}}` was not supplied → resolved to today's ISO date `2026-09-02` (filed in OPEN_QUESTIONS.md).

## 0. Prior-run check (law 10)
`ls 11_prompts/runs` → "No such file or directory" at run start. **No SURVEY-1 outputs exist**; nothing is reused; SURVEY-1 is not run (law 10). `survey1_ref` fields stay empty throughout.

## 1. Documents read (Phase 0 step 1), with anchors relied on
| Step | Path | Anchors relied on |
|---|---|---|
| a | `00_MANIFEST.md` | §1 table (declared counts 04:4 · 05:4 · 06:5→A-001 "~91" · 07:5 · 08:1 · 09:5 · 10:7 per §8; 05 +1 per §8); §3 production sequence; §4.1–4.5; §5 DEF-001/DEF-002; §6 authoring-integrity audit; §7 A-001; §8 A-002 |
| b | `10_regulatory-execution/EXEC-1_execution_directive.md` | frontmatter (`req_prefix: EX`, `req_count: 10`, `subordinate_to`); EX-1..EX-10; RUN-0..RUN-4 table; Part 4 integration ledger; Part 5 self-audit (8 checks) |
| c | `04_hardening/MAJOR_TASK_2_anti-laziness-hardening-directive.md` | §1 (eight properties); §3; §4 (13 rationalizations); §5; §6; §7 · `HARDEN-2` (trigger; universal exit bar; CC-1..CC-8; anti-rationalization rows; stop-the-line) · `HARDEN-3` (W0–W11; rules line) · `HARDEN-1` (rows 0–73; terminal-state law; A-001) |
| d | `01_north-star-and-transformation/` | MET-1 v1.0 frontmatter + §9.1–9.5 + §16 heading (64,435 B read by headings + §9; not full) · MET-1.1 (change table; honesty line) · MET-2 (C-01..C-12; DEC-01..DEC-12; standing escalations) · MET-2.1 (C-13..C-16; DEC-13..DEC-22; alias law) · MET-3 (source→output; family→binding) · MET-4 (G-01..G-11; roadmap) |
| e | `03_makoha-butterfly-corpus/` | `corpus_artifacts_briefing.md` Part 1 + Part 2 · `MANIFEST.md` (volume table; reading order; precedence paragraph) · `corpus-md/four-faces-corpus_v1.1.md` frontmatter (l.1-19), LLM usage contract, `## Contents` (l.44), Appendix A/B/C (l.518-585) · `butterfly-primers/RUN-REPORT.md` §1 (l.1-60) · `butterfly-primer-programme_prompt_v1.0.md` l.1-120 · spot checks: `antennae-corpus_v1.0.md`, `legs-corpus_v1.0.md`, `makoha-in-flight_v1.0.md` frontmatter + appendix headings |
| f | `02_cdss-stack-augmented/` | `primers_briefing.md` Part 1 (eleven-part skeleton) · `primer_A_bayesian_engine.md` headings A1–A10 + A10 ten-field table (l.141-160) · `primer_I_living_evaluation.md` headings I1–I10 · `architecture_and_integration.md` §10 (l.194-200), §12.1–12.3 (l.328-379), §13.3, §13.6, §13.9, §14.2–14.3 |
| g | `11_prompts/PROMPT-SERIES_A-L_index.md` (header, shared laws, table, eval gate) · `11_prompts/PROMPT-SURVEY-1_ecosystem_repleteness_surveyor.md` §1 `<class_contracts>` + `<ledger_schema>` (inherited) |

## 2. Honesty lines copied verbatim from 00_MANIFEST.md
### §4.4 Honesty lines (what this repository does NOT claim)
**4.4 Honesty lines (what this repository does NOT claim):** the MT2 pass has **not** been executed (R29 rows 0–73 PENDING; row 0 BLOCKED on install evidence) · `validate_build_plan.py` has **not** been run on the annexes (PENDING-VALIDATOR) · no counsel attestation exists (C-01 relabel = Needs confirmation; GATE-000 unpassed) · nothing is deployed; no code beyond skeleton READMEs is claimed · corpus content untouched (row 72 = in-account path only) · HeyDoc below-README = [NEEDS SOURCE] · RTO/RPO/DR-drill + person-level owners = [NEEDS DEFINITION].

### §8 Honesty lines (extending §4.4)
**Honesty lines (extending §4.4).** Counsel packets drafted, not sent; no attestation exists; GATE-000/SG-V1-0/NZ-GATE-0 unpassed · the standalone-vs-annex divergence is open until FOLD-1 W5 · REG-FIND-010/011 rest on a secondary source pending primary re-anchor · MAK-GOV non-device status is an argument at moderate confidence, not a determination · NZ-ASSUME-005 is a working assumption with its failure consequence pre-registered, not a finding · regulatory-owner for the AN-6 watch cadence remains [NEEDS DEFINITION] (G-09).

The verdicts in this run must be consistent with these lines or explain the difference (Phase 3 §g).

## 3. Arming
- `BSQ.schema.json` written verbatim from the prompt; check output (`schema_check.txt`):
    BSQ.schema.json: check_schema OK (Draft 2020-12, jsonschema 4.26.0 in ./.venv)
- `jsonschema` on the device is 3.2.0 system-wide (no Draft 2020-12 validator). Installed 4.26.0 in a venv **under the run directory** (`.venv/`, never system-wide): `python3 -m venv .venv && .venv/bin/pip install -q jsonschema` (ensurepip emitted a non-fatal error; pip and the package landed — verified by import). `.venv/` is excluded from checksums and census (tooling, not artifact).
- Row validator: `tools/validate_rows.py <schema> <jsonl>...` (Draft202012Validator; duplicate row_id check).
- Baseline: `find . -type f ! -name .DS_Store ! -path "./11_prompts/runs/2026-09-02_survey-2/*" -print0 | sort -z | xargs -0 sha256sum > CHECKSUMS_BEFORE.txt` → **223 files** (`.DS_Store` ×4 excluded; run directory excluded). Note: 223 includes `11_prompts/PROMPT-SURVEY-2_folder-parity_build-spec-queue.md`, added to the tree earlier on 2026-09-02 before this run started.
- Tools available on device: python3 3.10.12, node v22.23.2, npx, sha256sum. Mermaid parse: attempted in Phase 1 via `npx -y @mermaid-js/mermaid-cli` / `mermaid` package (network permitting; recorded there).

## 4. Phase 0 exit
ORIENTATION.md · PARITY_STANDARD.md (16 P-D + 10 P-F lines, each with ≥2 reference evidence points or a law) · CLASS_CONTRACTS.md (floor verbatim + extensions) · BSQ.schema.json + schema_check.txt · CHECKSUMS_BEFORE.txt — all present. No step-1 file failed to open.
