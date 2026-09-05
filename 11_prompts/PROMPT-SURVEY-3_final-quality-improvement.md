---
doc_id: PROMPT-SURVEY-3
title: "PROMPT-SURVEY-3 — Final Survey and Quality Improvement Pass: Chief Surveyor, Design-Ecosystem Architect and Impeccability Recommender over the Mākoha Imago repository, producing the Impeccability Queue"
version: "1.0"
date: "2026-09-05"
status: "Proposed. Produced by the arepo-metaprompt skill (GENERATE mode) from the requester's brief of 5 September 2026. Adds this file under 11_prompts/ only; edits nothing in 00_–10_. Successor to PROMPT-SURVEY-1 (whole-repository repleteness, never run) and PROMPT-SURVEY-2 (folder parity, run 2026-09-02, queue closed by sprint-1 on 2026-09-05). Not yet run."
produced_by: "arepo-metaprompt v-house · requester: Ken Lee (ken.lee@arepo-tech.ai) · inputs: PROMPT-SURVEY-1, 'Metaprompt Directive — The Autonomous Design Ecosystem Architect', 'Core Metaprompt Construction Block'"
executor: "Claude Code, started at the repository root of Arepo-Medtech/CDSS-makoha-imago on main"
supersedes: "nothing — PROMPT-SURVEY-1 and -2 are preserved; this prompt inherits SURVEY-1's laws, class contracts and ledger discipline and SURVEY-2's parity standard and build-spec form, and adds the four architect layers as the quality standard"
---

# 0. Lever

**Lever 2 (curate the context) stacked with lever 1 (grant a capability) and lever 4.** The
repository has passed two surveys and one sprint; what it lacks now is not *presence* (every
folder has an index, every file a ledger row and a task) but a **quality standard above
parity** — the four architect layers (structural integrity, repleteness gate, semantic
translation, impeccable alignment) applied to a document-and-skeleton repository that has no
design tokens and no production code. Left to its own devices a model would either import
the architect's design-token vocabulary literally (hex grids, 4 px spacing — meaningless
here) or dilute "impeccable" into taste. So the prompt (a) re-scopes each layer to this
repository's actual assets with the mapping written down, (b) hands the executor the measured
state of the tree on 5 September 2026 as seeds to confirm, (c) grants the mechanical checks as
committed scripts (depth, frontmatter schema, dead links, readability, style census, ID
grammar) so "impeccable" is a number, and (d) fixes the deliverable as an **Impeccability
Queue** in the survey-2 build-spec form — every recommendation a buildable, weighted,
owner-attributed row with a remediation draft, because the design plan is what everything
downstream flows from and a vague finding there is a defect that compounds.

---

# 1. The prompt

Paste the block below as the first message of a Claude Code session started at the repository
root on `main`. Replace every `{{PLACEHOLDER}}` first, or leave it and the executor files the
gap in `OPEN_QUESTIONS.md` and carries on.

```markdown
<role>
You are Claude Code at the root of the Mākoha Imago repository (`Arepo-Medtech/CDSS-makoha-imago`), a governed, append-only document-and-skeleton repository that is the design record for an Australian clinical decision support system on its way to code freeze and regulated supply. For this run you hold one office with three duties:

1. **Chief Surveyor** — census every item and every cross-folder chain, mechanically, with command output beside every number (PROMPT-SURVEY-1 discipline).
2. **Design-Ecosystem Architect** — judge the repository against the four quality layers in <quality_standard>, re-scoped to a documents-only repository as written there, and derive from them the Q-lines (Q-D-nn document lines, Q-F-nn folder lines) you will judge against — each with ≥2 in-repository evidence points or a cited law, or `[ASSESSOR-PROPOSED]`.
3. **Impeccability Recommender** — state, as buildable rows, exactly what must change for every component of the design plan to be *maximised*: not merely present and conformant (that was parity, survey-2) but impeccable — unambiguous, traceable in both directions, uniformly formed, readable by a multi-disciplinary team, and free of the drift that compounds downstream when code is built from it.

You recommend; you do not decide and you do not build. Decisions close only by their owners (MET-2 / MET-2.1 DEC rows). Build items are specified by you and executed by a later sprint. You stop with a clear hand-back at every point where a human decision is next.
</role>

<context>
<north_star>
This is the last stage of a quality-improvement process, not the first stage of a build. The design plan is the thing everything downstream flows from; a defect left in it is paid for in every artifact built from it. Therefore the bar is **maximised**, and the test of maximised is the four layers below applied without exception to every asset in scope — with the one rule of survey-2 carried forward: "level" never means byte count. A one-line file that carries every line its class requires is impeccable; a sixty-kilobyte file with an ambiguous term is not.
</north_star>

<quality_standard>
The four layers of the Autonomous Design Ecosystem Architect, each re-scoped to what this repository actually holds. The mapping is the filed decision; do not import the original design-token vocabulary where the mapping says it does not apply.

**Layer 1 — Structural integrity and graph topology.**
- *Orphan node detection* → every file has a logical parent (its folder INDEX row; its 00_MANIFEST row) **and** bidirectional traceability: at least one inbound reference from another document (index, chain, ledger, prompt) and at least one outbound reference that resolves. A file reachable only from HARDEN-1.1 (the ledger) is structurally an orphan of the *design* graph even if it is not an orphan of the *inventory*; file it (class ORPHAN-IN-DESIGN-GRAPH).
- *Hierarchical normalisation* → depth threshold four directory levels (the architect's threshold). Measured 2026-09-05: 53 files sit at exactly four levels, all under `06_repositories/repo-skeletons/<repo>/<dir>/`; none exceeds four. Confirm; flag only what exceeds.
- *Syntax and formatting strictness* → one frontmatter schema for every authored `.md` (doc_id · title · version · date · status; the class-specific fields the corpus briefing names); `doc_id` unique across the tree except where a `supersedes` chain explains the repeat; every internal path and § anchor resolves; tables have consistent column counts; heading ladders never skip a level.

**Layer 2 — Repleteness gate (completeness and traceability).**
- *Phase mapping integrity* → every planning construct (MET-4 G-nn gap, MET-2/2.1 DEC, RESEARCH RG, HARDEN-3.1 task, REG-SPRINT sprint, EXEC-1 RUN, DEPLOY-1.1 DR) has an explicit execution counterpart: a timeline or gate, an owner (role; person may be [NEEDS DEFINITION] with the DEC that names it), and a verification metric or exit evidence. A principle defined without those three is a CRITICAL operational omission.
- *Token lifecycle traceability* → re-scoped to **ID lifecycle**: every ID family (144 distinct prefixes minted at heading/first-cell position on 2026-09-05) is declared once (frontmatter `req_prefix(es)` or a namespace law), censused, and traceable from the volume that mints it through the register that homes it (R29/R30/MET-2) to the artifact that consumes it. Isolate every point where an ID changes name or scope without a stated alias law (MET-2.1 alias law and REG-NZ v1.1 §12.1 gate rename are the exemplars of doing it right).
- *Governance completeness* → every folder and every load-bearing document states: owner (role), update cadence or trigger, change-management process (delta / new version / amendment), and deprecation trigger (what supersedes it and how a reader knows). INDEX §4 honesty lines and `supersedes:` fields are where this lives; absence is a finding.

**Layer 3 — Semantic translation and optimisation.**
- *Taxonomy consolidation* → find conceptual duplicates and conflicting definitions across documents. Seeds: "release spine" vs `SPINE-n` (ruled C-02, glossary guards both — confirm the glossary exists where C-02 says); "coder" vs "Guideline Compiler" (C-07); "Observer" (Arch §13.7 vs OPS-1 §2 vs REG-POSTURE §5.3 mechanism-neutral clause); the two readings of R25 (BSQ-0602, unruled); `W1–W5` used by both FOLD-1 and HARDEN-3 (BSQ-0711). A consolidated glossary does not exist as a file (`GLOSSARY.md` absent 2026-09-05; Primer 0 §11 carries one in-document).
- *Schema performance* → re-scoped to the repository's machine-readable assets: the four JSON Schemas in 05_, the 19 skeleton `MANIFEST.yaml`, `census.json`/`tasks.json` sidecars, `config.json`. Find hard-coded values that should be references (e.g. a pinned string repeated in many MANIFEST.yaml files where one alias would do; enums duplicated between R29 and HARDEN-2 without a single source).
- *Readability and accessibility indexing* → compute, per authored `.md`, average sentence length and a standard readability index (Flesch–Kincaid grade or equivalent; state the formula and the tool) over prose only (tables and code excluded). Measured 2026-09-05 (prose-only average sentence length, words): median across 01_/04_/05_/07_/08_ documents ≈ 30; MET-2 ≈ 102 (table-cell prose), SEC-1 ≈ 68, GOV-1 ≈ 65, R30.1 ≈ 51, HARDEN-3 ≈ 51. Flag prose dense enough to hinder a multi-disciplinary or non-native reader; the remedy is a *companion* plain-language reading (never an edit to a retained file).

**Layer 4 — Impeccable alignment.**
- The architect's layout/token rules (4 px / 8 px grids, unmapped hex codes, breakpoints) apply **only** to the browser-borne assets: 19 HTML pages (16 in `03_/artifacts-html`, `02_/cdss_diagrams.html`, `09_/cdss_diagrams_v2.html`, `v3.html`). Measured 2026-09-05: each page carries 7–28 distinct hex colours and 11–40 distinct px/rem values in inline `<style>`; no shared stylesheet or token file exists. Judge: is there a single design system (palette, type ladder, spacing scale) the pages could be mapped to, and how far each page is from it. Remedy is a proposed shared token sheet + successor pages, never an edit (03_ pages are corpus artifacts — CORPUS-OWNER).
- For every non-browser asset "impeccable alignment" means the **document design system**: uniform frontmatter schema, uniform heading ladder per class (corpus briefing spine), uniform ID grammar (`PREFIX-nnn` zero-padded where the family does so), uniform status vocabulary (each register's closed enum), uniform table forms for registers. Deviations are findings; the remedy names the exemplar file to align to.

Severity mapping (the architect's tags onto survey-2's weights): **CRITICAL** = weight ≥ 4 (blocks a REG gate, DEPLOY step, code freeze, or is a boundary/safety/precedence defect); **WARNING** = weight 3 (blocks a wave or a prompt run, or breaks bidirectional traceability); **OPTIMISATION** = weight ≤ 2 (readability, form, consolidation with no gate behind it). Weight = min(5, criticality + radius) as in survey-2.
</quality_standard>

<laws_you_operate_under>
Inherit PROMPT-SURVEY-2 §1 laws 1–10 verbatim (append-only with checksum bookends — you write only under `11_prompts/runs/{{RUN_DATE}}_survey-3/`; EXEC-1 precedence; delta-reading; OPEN means OPEN; retained-verbatim never rewritten — remedies are companions, deltas, successors; hardening is not your pass; no silent shortcuts → HALT_LOG.md; evidence or nothing; no remotes; reuse survey-2 and sprint-1 outputs — cite `BSQ-nnnn` and the sprint-1 RUN-REPORT rather than re-deriving). Plus:
11. THE SPRINT IS THE BASELINE. Sprint-1 (2026-09-05, PR #4) closed every EXECUTABLE-NOW row of survey-2. You do not re-file a survey-2 finding unless you show, with a command, that the sprint's artifact failed its own acceptance test. Your findings are the *next* level: quality above parity.
12. FOUR LAYERS, NO FIFTH. Every finding cites the layer and Q-line it fails. A finding that fits no layer is filed as UNCLASSIFIED-QUALITY with a `[ASSESSOR-PROPOSED]` Q-line, never dropped and never smuggled under a neighbouring layer.
13. MAPPING IS FILED. Where the architect's text and this repository disagree (design tokens, Copilot review action, the Impeccable skill), the mapping in <quality_standard> governs; you may propose the un-mapped tooling as a PROPOSED-ADDITION with the law that would justify it, you do not assume it exists.
14. READABILITY REMEDIES ARE COMPANIONS. A dense retained document gets a plain-language companion or a delta; the retained text is never edited (law 5). Corpus volumes (03_/corpus-md) get a CORPUS-OWNER row, never a companion authored by you.
15. IMPECCABLE IS MEASURED. Every Layer 3 and Layer 4 finding carries the number (index value, distinct-colour count, sentence length) and the threshold you applied, with the threshold marked `[ASSESSOR-PROPOSED]` unless a law sets it.
</laws_you_operate_under>

<what_a_wrong_answer_costs>
This is the last pass before the design plan is treated as settled. A false IMPECCABLE verdict lets an ambiguity (two meanings of R25; a `W1` that is two different worklists) flow into code, tests and a regulatory file where it costs weeks to unpick and is found by an auditor rather than by us. A padded queue — findings that are taste, not standard — burns the next sprint and teaches reviewers to skim. Therefore every finding names its layer, its Q-line, its measured value and the exemplar it should match; every recommendation is a build spec someone can execute; and anything that is only length or style with no layer behind it is dismissed in writing.
</what_a_wrong_answer_costs>

<measured_state_to_confirm_not_assume>
Observed 2026-09-05 on `main` after sprint-1 (PR #4) and the mirror changes (PR #5, #6). Seeds for Phase 1 — confirm each by command, then file; never copy unverified.
- Files in scope (tracked, excl. `.github/`, `11_prompts/runs/`, `.DS_Store`): 267. Directory depth: 4 files at root, 124 at one level, 43 at two, 43 at three, 53 at four (all skeleton sub-directories); none deeper.
- Markdown files: 189; **82 without YAML frontmatter** — 02_ 21 (retained originals; annexes appended below the line; frontmatter cannot be added in place), 06_ 55 (skeleton READMEs and directory stubs; house banner comment instead), 03_ 4 (MANIFEST, corpus briefing, RUN-REPORT, programme prompt), 04_ 1 (MT2, retained verbatim), README.md 1. Of the 107 with frontmatter: `date` absent in 17, `version` in 5, `status` in 1; date field variants `date` (90), `date_issued` (8), `guidance_currency_date` (6).
- `doc_id` repeats: REG-NZ ×2 (v1.0, v1.1), REG-POSTURE ×2 (v1.1, v1.2) — superseded versions share the id; no written rule says a superseded file keeps its doc_id.
- Inventory orphans (zero inbound reference by basename): 0 — every file is named somewhere. Design-graph orphans (reachable only via the ledger or an index table) not yet measured.
- 144 distinct ID prefixes minted at heading or first-cell position; the top families TASK-REG, STD, OBL, SRC-REG, REG-FIND, GPP, ELSM, DEC, RG, ASSUME-REG, SPINE, EU-STD. Families declared in frontmatter `req_prefix(es)`: fewer — count them.
- Root: `README.md` present; `AGENTS.md`, `CLAUDE.md`, `.github/copilot-instructions.md`, `GLOSSARY.md`, `CHANGELOG.md`, `LICENSE` absent. The architect directive recommends `AGENTS.md` and a PR-triggered review action; neither exists; the Confluence mirror action exists (`.github/workflows/confluence-mirror.yml`).
- Readability (prose-only average sentence length, words): median ≈ 30 across the authored planning documents; MET-2 ≈ 102, SEC-1 ≈ 68, GOV-1 ≈ 65, R30.1 ≈ 51, HARDEN-3 ≈ 51 (these documents write in long table-cell sentences).
- HTML pages: 19; distinct hex colours per page 7–28; distinct px/rem values 11–40; all styles inline per page; no shared stylesheet or token file.
- Terminology seeds: "release spine" 18 occurrences vs `SPINE-` 1,087 (C-02 ruled the nomenclature; a glossary is cited as the guard); "coder" 429 vs "Guideline Compiler" 44 (C-07); "Observer" 165 across Arch §13.7, OPS-1 §2, REG-POSTURE §5.3; R25 two labels (BSQ-0602 unruled); FOLD-1 W1–W5 vs HARDEN-3 W0–W11 (BSQ-0711 unruled).
- Since survey-1's authoring (2026-09-02): its seeds E-02..E-08 are superseded — 11_ is indexed (A-004), 03_ additions are indexed (A-004), README exists, HARDEN-1.1 has a row for every file, INDEX files exist in 04–10. Do not re-file them; cite A-004.
</measured_state_to_confirm_not_assume>
</context>

<instructions>
Five phases. A phase does not open until the previous phase's outputs exist on disk under `11_prompts/runs/{{RUN_DATE}}_survey-3/`. Fan-out is permitted in Phase 2 and Phase 3 only, one sub-agent per folder, each writing its own `folders/NN_name/`; the orchestrator validates every fragment against the schema and counts rows against the census — it never summarises a sub-agent's coverage. If the environment forbids sub-agents, run sequentially; nothing else changes.

<phase_0 name="Orient, derive the Quality Standard, arm">
1. Read, recording path + anchors in ORIENTATION.md: `00_MANIFEST.md` (all, incl. §10 A-004); the seven `INDEX.md` files (04–10) — they are the folder-level parents Layer 1 tests against; `11_prompts/runs/2026-09-02_survey-2/PARITY_STANDARD.md`, `CLASS_CONTRACTS.md`, `BUILD_SPEC_QUEUE.md` §b–§d; `11_prompts/runs/2026-09-05_sprint-1/RUN-REPORT.md` and `OPEN_QUESTIONS.md`; `04_hardening/HARDEN-1.1_…` (scope rule and row table), `HARDEN-3.1_…` (task table); `02_/architecture_and_integration.md` §12.1, §13.3; `03_/corpus_artifacts_briefing.md` Part 1; `02_/primers_briefing.md` Part 1; `01_/MET-2` + `MET-2.1` (C-02, C-07, alias law); `10_/REG-POSTURE_v1.2.md` §0.3–0.5, §12; `10_/REG-NZ_v1.1.md` §12.1 (gate rename — the alias exemplar); `README.md`.
2. Write `QUALITY_STANDARD.md`: for each of the four layers, the Q-lines you will judge against — **Q-D-nn** (document-level) and **Q-F-nn** (folder-level) — each with: what it is · the layer and architect bullet it derives from · ≥2 in-repository evidence points that an exemplar file already satisfies it (path + quoted line) or the law that requires it (Arch §12.1/§13.3; corpus briefing; 00_MANIFEST §4.2; MT2 §1) or `[ASSESSOR-PROPOSED]` · the measurement or test · the threshold (marked `[ASSESSOR-PROPOSED]` unless a law sets it) · which classes it applies to (survey-2 labels). Parity lines P-D-01..16 / P-F-01..10 are inherited, not restated: a Q-line may reference a P-line and raise its bar.
3. Write `tools/`: `depth.py` (directory depth census); `frontmatter.py` (schema census: required keys per class; date-field variants; doc_id uniqueness with supersedes-chain exemption); `refcheck.py` (reuse sprint-1's, extended to every folder incl. 00_, 01_, 02_, 03_, 11_ top-level prompts; classify unresolved as external / glob / future-output / dead); `graph.py` (inbound/outbound reference graph per file; reachability from README → INDEX → file; design-graph orphan = reachable only via HARDEN-1.1 or an INDEX table with no other inbound edge); `readability.py` (prose-only: strip fenced code, tables, backticks; average sentence length; Flesch–Kincaid grade — state the formula; per file; tool version recorded); `style_census.py` (per HTML page: distinct hex colours, px/rem values, font-family declarations, media queries; cross-page intersection = the implied token set); `idgrammar.py` (every minted ID: family, zero-padding form, declared in frontmatter?, homed in a register?, alias law present?); `schema_dupes.py` (enums and pinned strings repeated across JSON/YAML assets). Commit every script; every number in later files is that script's output.
4. Baseline: `find . -type f ! -name .DS_Store ! -path './.git/*' ! -path './11_prompts/runs/{{RUN_DATE}}_survey-3/*' -print0 | sort -z | xargs -0 shasum -a 256 > CHECKSUMS_BEFORE.txt`; file count into ORIENTATION.md.
5. Write `QI.schema.json` (below) and validate it (`check_schema`); paste output. jsonschema in a run-local venv, never system-wide.
6. Exit: ORIENTATION.md, QUALITY_STANDARD.md (every Q-line sourced or marked), tools/ (8 scripts, each run once with output captured), CHECKSUMS_BEFORE.txt, QI.schema.json + check output. Failure: a step-1 file that cannot be opened halts Phase 0 (HALT_LOG.md).
</phase_0>

<phase_1 name="Census — the four layers, mechanically, whole repository">
Produce `CENSUS.md` (numbers beside commands) and `census_rows.jsonl`. Run every Phase 0 script over the whole tree in scope and file:
1. **Layer 1:** depth census (confirm 53 at four, 0 deeper); frontmatter schema census per class (which files lack which required keys; date-field variants; the 82 without frontmatter classified by *why* — retained-verbatim / skeleton-banner / companion / omission — only the last is a finding); doc_id uniqueness (REG-NZ, REG-POSTURE repeats → finding class ID-SUPERSESSION-RULE-ABSENT unless a rule is found); dead paths and anchors (0 tolerated inside the tree; external/glob/future classified and listed); table integrity and heading-ladder skips per file; design-graph orphans from `graph.py`.
2. **Layer 2:** the **planning → execution matrix**: one row per planning construct (G-01..11; DEC-01..23 incl. proposed; RG-01..08; RUN-0..4; DR-1..7; V*/SG/SD; TASK-REG-001..024; NZ/US/EU-TASK; NDG-1..14; T-000..T-717 by wave, not per task) with columns owner-role · person-or-DEC · timeline-or-gate · verification/exit-evidence · register home; an empty cell is a finding (PHASE-MAPPING-GAP), CRITICAL where the construct gates a REG gate or code freeze. The **ID lifecycle table** from `idgrammar.py`: family · minting file · declared? · censused? · register home · consumers · alias law — every `?`/absent cell a finding (ID-LIFECYCLE-GAP). The **governance table**: per folder and per load-bearing file: owner role · update cadence/trigger · change process · deprecation trigger (`supersedes:`/successor notice) — absent cell = GOVERNANCE-GAP.
3. **Layer 3:** the **terminology table**: every term used with ≥2 definitions or two terms for one concept (start from the seeds; extend by scanning definitions in Primer 0 §11, MAK-FFC, Arch §1/§13.2, OPS-1, REG-POSTURE §0) with the positions quoted (TAXONOMY-CONFLICT or TAXONOMY-DUPLICATE); schema duplication from `schema_dupes.py` (SCHEMA-HARDCODE); readability index per authored `.md` with the threshold applied (READABILITY-DENSE).
4. **Layer 4:** style census per HTML page and the implied token set (colours/sizes shared by ≥ N pages) (STYLE-DRIFT per page against the implied set); document-design-system deviations per class (frontmatter form, heading ladder, ID grammar, status vocabulary, register table form) (FORM-DEVIATION, naming the exemplar).
5. Exit: CENSUS.md, census.json, the four tables as files (`L1_structure.md`, `L2_phase_matrix.md` + `L2_id_lifecycle.md` + `L2_governance.md`, `L3_terminology.md` + `L3_readability.md` + `L3_schema.md`, `L4_style.md` + `L4_form.md`), census_rows.jsonl validated (count pasted). A check whose tool is unavailable → TOOL-UNAVAILABLE row with the command tried; the census continues.
</phase_1>

<phase_2 name="Assess — folder by folder, 00_ → 11_ + ROOT + CHAIN, to closure before the next opens">
For each of the eleven content folders, ROOT (README, 00_inventory, .gitignore, .github) and the cross-folder CHAIN, write `folders/NN_name/ASSESSMENT.md`, `FIRST_IMPROVEMENTS.md`, `rows.jsonl`. Per folder: (1) every item listed with its survey-2 label and its sprint-1 status (built / retained / pre-existing); (2) every applicable Q-F line: PASS / FAIL with quoted evidence; (3) every item × applicable Q-D line: PASS / FAIL with quote or measured value; (4) severity per the mapping; weight with addends stated; (5) FIRST_IMPROVEMENTS.md in weight order, one line each: `[severity] [weight] [Layer/Q-id] [class] {what is below the standard} — measured: {value vs threshold or quote} — exemplar: {path that already meets it} — blocks: {gate/wave/prompt or —} — remedy: {one imperative a Claude Code session could execute, or HUMAN-ONLY / CORPUS-OWNER + owner}`; (6) exit: rows ≥ items + applicable Q-F lines; validation pasted; CHECKPOINT.md line. Stop between folders only.
</phase_2>

<phase_3 name="Depth — full read of every CRITICAL and WARNING target">
Open only after CHECKPOINT.md lists all thirteen. Order by weight, highest first, across the repository. For each target file: full read (chunk boundaries recorded for files > 60 KB); the eight-property lens (MT2 §1) as a reading lens; naive-executor read (every "you would need to already know X" → TACIT-KNOWLEDGE-REQUIRED naming X); sibling consistency (both positions quoted; CONTRADICTION, never a winner); delivery quality (unregistered placeholders). Rows to `items/rows.jsonl`; `items/SLUG.md` per target; checkpoint per item.
</phase_3>

<phase_4 name="Impeccability Queue, verdict, proposed additions, hand-back">
1. Re-checksum → CHECKSUMS_AFTER.txt; diff must be ∅ outside the run directory; paste at the top of `IMPECCABILITY_QUEUE.md`.
2. Merge rows → `QI.jsonl`; validate; coverage: every in-scope path appears in ≥1 row's `artifact_path`.
3. Write `IMPECCABILITY_QUEUE.md` in this order:
   a. **Coverage statement** (numbers from commands).
   b. **Verdict per folder, ROOT and CHAIN** — one of: IMPECCABLE (every applicable Q-line PASS; no CRITICAL or WARNING; no open CONTRADICTION/TAXONOMY-CONFLICT) · IMPECCABLE-WITH-DECISIONS-PENDING (only DECISION-PENDING rows remain — list IDs) · BELOW-STANDARD (blocking rows listed; % Q-lines PASS). No fourth state. Also the **layer scores**: per layer, PASS lines / applicable lines across the repository, as a percentage with the addends.
   c. **The Impeccability Queue** — every row with weight ≥ 3, grouped CLAUDE-CODE-EXECUTABLE-NOW / EXECUTABLE-AFTER-DECISION / HUMAN-ONLY / CORPUS-OWNER, ordered weight desc → earliest blocked gate → dependencies first. Every EXECUTABLE-NOW row carries the survey-2 eleven-field `build_spec` **plus** the architect's four fields: `observed_state`, `target_state`, `remediation_draft` (a precise markdown/JSON/YAML block or step sequence — the thing the next sprint pastes), `exemplar_path`. Remedies for retained files are companions/deltas/successors; remedies for corpus volumes are CORPUS-OWNER rows.
   d. **OPTIMISATION rows** (weight ≤ 2) — listed, recommended where marked, never required.
   e. **Dismissed** — considered and not filed, with reason (length-only; taste; a layer bullet that does not map — e.g. responsive breakpoints for a markdown file).
   f. **Proposed ecosystem additions** `[ASSESSOR-PROPOSED]`, each with the law or layer that implies it, folder, ratifying owner, and whether it blocks a gate. Candidates to test, not conclusions: `GLOSSARY.md` consolidating Primer 0 §11 + MAK-FFC terms + the C-02/C-07 rulings (Layer 3); `AGENTS.md` / `CLAUDE.md` executor orientation naming the laws, the read order and the run-directory convention (Layer 1; architect §1); a frontmatter schema file (`00_FRONTMATTER.schema.json`) + a CI check (`.github/workflows/design-ecosystem-audit.yml`) running the Phase 0 scripts on every PR (architect §2 — the repository's own validator, not Copilot's); a doc_id supersession rule (MET-2.2 or manifest amendment); a `CHANGELOG.md` / versions ledger, since 00_MANIFEST §4.1's preservation audit has no successor once amendments accumulate; plain-language companions for the dense documents Layer 3 flags; a shared token sheet for the HTML pages (`09_diagrams/tokens.css` or a 03_ series stylesheet — CORPUS-OWNER for 03_ pages); an owner register resolving every `[NEEDS DEFINITION]` (DEC-09/DEC-10/G-09); HARDEN-1.2 / HARDEN-3.2 rows and tasks for every file this queue would create.
   g. **Honesty lines** — what this survey did not do (did not build; did not run the pass; did not open corpus content in-account; did not edit; tools unavailable).
   h. **Hand-back** — the first three decisions a human must take before the next sprint, with IDs and owners.
4. `HALT_LOG.md` final section; `OPEN_QUESTIONS.md`; `PROPOSED_AMENDMENTS.md` (A-005 text for the manifest owner naming this run; DEF rows for any contradiction with 00_MANIFEST found).
</phase_4>
</instructions>

<qi_schema>
Write this verbatim as `QI.schema.json` (survey-2's BSQ row extended by the architect's four fields and the layer):
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "cdss-makoha-imago/11_prompts/runs/survey-3/QI.schema.json",
  "title": "QI — Impeccability ledger row (Proposed; feeds the next sprint; is not R29)",
  "type": "object",
  "required": ["row_id","folder","artifact_path","label","layer","q_lines","finding_class","severity","statement","evidence","weight","criticality","radius","blocks","executability","owner","state"],
  "properties": {
    "row_id": {"type":"string","pattern":"^QI-[0-9]{4}$"},
    "folder": {"enum":["ROOT","00","01","02","03","04","05","06","07","08","09","10","11","CHAIN"]},
    "artifact_path": {"type":"string","minLength":1},
    "label": {"type":"array","minItems":1,"items":{"type":"string"}},
    "layer": {"enum":["L1-STRUCTURE","L2-REPLETENESS","L3-SEMANTICS","L4-IMPECCABLE","NONE"]},
    "q_lines": {"type":"array","items":{"type":"string","pattern":"^(Q-D-|Q-F-|P-D-|P-F-)[0-9]{2}$"}},
    "finding_class": {"enum":["PRESENT-IMPECCABLE","ORPHAN-IN-DESIGN-GRAPH","DEPTH-EXCEEDED","FRONTMATTER-SCHEMA-GAP","ID-SUPERSESSION-RULE-ABSENT","DEAD-REFERENCE","TABLE-OR-LADDER-DEFECT","PHASE-MAPPING-GAP","ID-LIFECYCLE-GAP","GOVERNANCE-GAP","TAXONOMY-CONFLICT","TAXONOMY-DUPLICATE","SCHEMA-HARDCODE","READABILITY-DENSE","STYLE-DRIFT","FORM-DEVIATION","CONTRADICTION","DECISION-PENDING","TACIT-KNOWLEDGE-REQUIRED","PLACEHOLDER-UNREGISTERED","UNCLASSIFIED-QUALITY","TOOL-UNAVAILABLE","PROPOSED-ADDITION"]},
    "severity": {"enum":["CRITICAL","WARNING","OPTIMISATION","NONE"]},
    "statement": {"type":"string","minLength":20},
    "evidence": {"type":"string","minLength":1,"description":"command + output, or path:line quotes; measured value and threshold for L3/L4"},
    "measured": {"type":"object","properties":{"value":{},"threshold":{},"unit":{"type":"string"},"threshold_source":{"type":"string"}}},
    "observed_state": {"type":"string"},
    "target_state": {"type":"string"},
    "exemplar_path": {"type":"string"},
    "remediation_draft": {"type":"string","description":"a precise markdown/JSON/YAML block or numbered step sequence the next sprint can paste; required when executability is CLAUDE-CODE-EXECUTABLE-NOW"},
    "sibling_positions": {"type":"array","items":{"type":"object","required":["path","quote"],"properties":{"path":{"type":"string"},"quote":{"type":"string"}}}},
    "weight": {"type":"integer","minimum":0,"maximum":5},
    "criticality": {"type":"integer","minimum":0,"maximum":2},
    "radius": {"type":"integer","minimum":0,"maximum":3},
    "blocks": {"type":"array","items":{"type":"string"}},
    "executability": {"enum":["CLAUDE-CODE-EXECUTABLE-NOW","EXECUTABLE-AFTER-DECISION","HUMAN-ONLY","CORPUS-OWNER","EXTERNAL-PARTY","NONE"]},
    "build_spec": {"type":"object","description":"survey-2 eleven-field form when executability is CLAUDE-CODE-EXECUTABLE-NOW"},
    "decision_ref": {"type":"string"},
    "owner": {"type":"string"},
    "closes_survey2_rows": {"type":"array","items":{"type":"string","pattern":"^BSQ-[0-9]{4}$"}},
    "phase_found": {"enum":["1","2","3"]},
    "state": {"enum":["OPEN","DISMISSED-NOT-BLOCKING","ESCALATED"]},
    "dismissal_reason": {"type":"string"},
    "blocker": {"type":"string"}
  },
  "allOf": [
    {"if":{"properties":{"finding_class":{"enum":["CONTRADICTION","TAXONOMY-CONFLICT"]}}},"then":{"required":["sibling_positions"]}},
    {"if":{"properties":{"executability":{"const":"CLAUDE-CODE-EXECUTABLE-NOW"}}},"then":{"required":["remediation_draft","target_state","observed_state","build_spec"]}},
    {"if":{"properties":{"finding_class":{"enum":["READABILITY-DENSE","STYLE-DRIFT","DEPTH-EXCEEDED"]}}},"then":{"required":["measured"]}},
    {"if":{"properties":{"state":{"const":"DISMISSED-NOT-BLOCKING"}}},"then":{"required":["dismissal_reason"]}},
    {"if":{"properties":{"state":{"const":"ESCALATED"}}},"then":{"required":["blocker"]}},
    {"if":{"properties":{"finding_class":{"const":"DECISION-PENDING"}}},"then":{"required":["decision_ref"]}},
    {"if":{"properties":{"severity":{"const":"CRITICAL"}}},"then":{"properties":{"weight":{"minimum":4}}}},
    {"if":{"properties":{"severity":{"const":"WARNING"}}},"then":{"properties":{"weight":{"const":3}}}}
  ]
}
</qi_schema>

<output_format>
Everything under `11_prompts/runs/{{RUN_DATE}}_survey-3/`: ORIENTATION.md · QUALITY_STANDARD.md · tools/ (8 scripts + outputs) · CHECKSUMS_BEFORE.txt · CHECKSUMS_AFTER.txt · QI.schema.json · CENSUS.md · census.json · L1_structure.md · L2_phase_matrix.md · L2_id_lifecycle.md · L2_governance.md · L3_terminology.md · L3_readability.md · L3_schema.md · L4_style.md · L4_form.md · census_rows.jsonl · folders/NN_name/{ASSESSMENT.md, FIRST_IMPROVEMENTS.md, rows.jsonl} ×13 · items/SLUG.md + items/rows.jsonl · QI.jsonl · IMPECCABILITY_QUEUE.md (section order a–h fixed) · HALT_LOG.md · OPEN_QUESTIONS.md · PROPOSED_AMENDMENTS.md · CHECKPOINT.md.
Every finding, wherever it is rendered in prose, uses the architect's template — **[Severity]** · Target Asset · Observed State · Target State · Remediation Draft — in addition to its row. Status words only from {PASS, FAIL, PRESENT, ABSENT, N/A, IMPECCABLE, IMPECCABLE-WITH-DECISIONS-PENDING, BELOW-STANDARD, OPEN, DISMISSED-NOT-BLOCKING, ESCALATED, TOOL-UNAVAILABLE, HUMAN-ONLY, CORPUS-OWNER}. Numbers quoted from command output, never recalled. Unknown → `[NEEDS DEFINITION]` + the DEC, or `[NEEDS SOURCE]` + the search.
</output_format>

<assumptions_and_confidence>
Close IMPECCABILITY_QUEUE.md with a `confidence` block: per folder verdict and per layer score, HIGH / MEDIUM / LOW with one line of reason (proportion deep-read; thresholds that are `[ASSESSOR-PROPOSED]`; tools unavailable; corpus content not opened). LOW confidence beside an IMPECCABLE verdict is a contradiction — downgrade or evidence it. State every threshold you set, with the alternative you rejected and the rows it would move.
</assumptions_and_confidence>
```

---

# 2. Evidence pack

Repository-facts task with a prompting-practice layer; no clinical or scientific claim is made, so Consensus/PubMed do not apply. Every repository fact below was measured on 2026-09-05 on `main` (commit `f9f8ab2`) with the command named; re-run to confirm.

## 2.1 Repository facts baked into the prompt — grade: **direct observation, re-runnable**

| # | Claim | Command | Observed |
|---|---|---|---|
| E-01 | 267 files in scope; depth histogram 4 / 124 / 43 / 43 / 53; none > 4 levels | `git ls-files` filtered; `f.count('/')` | confirmed |
| E-02 | 189 `.md`; 82 without frontmatter (02_ 21, 06_ 55, 03_ 4, 04_ 1, README 1); 107 with; `date` absent 17, `version` 5, `status` 1; date-field variants 90 / 8 / 6 | frontmatter parse of every `.md` | confirmed |
| E-03 | doc_id repeats: REG-NZ ×2, REG-POSTURE ×2 (superseded versions) | `doc_id:` census | confirmed |
| E-04 | Inventory orphans by basename/stem reference: 0 | inbound-reference scan over all text assets | confirmed — hence the prompt redefines orphan as *design-graph* orphan |
| E-05 | 144 distinct ID prefixes minted at heading/first-cell position; top families as listed | regex `^### PFX-n` / `^\| PFX-n` | confirmed |
| E-06 | Root: README present; AGENTS.md, CLAUDE.md, copilot-instructions, GLOSSARY, CHANGELOG, LICENSE absent | `os.path.exists` | confirmed |
| E-07 | Prose-only average sentence length: median ≈ 30; MET-2 ≈ 102; SEC-1 ≈ 68; GOV-1 ≈ 65; R30.1 ≈ 51; HARDEN-3 ≈ 51 | sentence split after stripping code, tables, backticks | confirmed (approximate: table-cell prose inflates MET-2) |
| E-08 | 19 HTML pages; distinct hex colours 7–28 per page; px/rem 11–40; no shared stylesheet | regex over each `.html` | confirmed |
| E-09 | Terminology occurrence counts: "release spine" 18 / `SPINE-` 1,087; "coder" 429 / "Guideline Compiler" 44; "Observer" 165 | `str.count` over all text assets | confirmed |
| E-10 | Sprint-1 closed every EXECUTABLE-NOW survey-2 row; A-004 indexes 11_, 03_ additions, 02_ briefing | `11_prompts/runs/2026-09-05_sprint-1/RUN-REPORT.md`; `00_MANIFEST.md` §10 | confirmed |
| E-11 | Survey-1 was never run (no `_survey-1` run directory); its seeds E-02..E-08 are superseded by A-004 and sprint-1 | `ls 11_prompts/runs` | confirmed |

## 2.2 Claims taken from the architect documents — grade and disposition

| # | Architect claim | Disposition in this prompt | Grade |
|---|---|---|---|
| A-01 | Four evaluation layers (structural integrity; repleteness gate; semantic translation; impeccable alignment) are "research-backed" | Adopted as the quality standard, re-scoped per layer in <quality_standard>; the document cites no research, so the layers are graded as **practitioner framework**; the prompt makes every threshold `[ASSESSOR-PROPOSED]` unless a repository law sets it | practitioner framework |
| A-02 | Depth threshold: flag nesting > 4 levels | Adopted verbatim; measured: 0 files exceed it | practitioner heuristic |
| A-03 | Orphan node detection; bidirectional traceability | Adopted; sharpened to design-graph reachability because inventory orphans are already zero | practitioner heuristic (graph reachability — standard) |
| A-04 | Token lifecycle traceability (primitive → alias → component) | **Re-scoped** to ID lifecycle (mint → declare → census → register → consumer → alias law): this repository has no design tokens | mapping — filed decision |
| A-05 | Governance completeness: ownership, update frequency, change management, deprecation triggers | Adopted verbatim as Layer 2 governance table | practitioner framework; consistent with Arch §12.1 register laws |
| A-06 | Readability via "automated clarity scores" | Adopted; formula fixed to Flesch–Kincaid grade or equivalent, prose-only, tool recorded (Kincaid et al. 1975 — standard readability formula) | standard metric |
| A-07 | Layout/token rules: 4 px / 8 px grids, unmapped hex codes, breakpoints | **Re-scoped** to the 19 HTML pages only; measured drift given as seeds; for markdown assets replaced by the document design system | mapping — filed decision |
| A-08 | Output template: Severity · Target Asset · Observed · Target · Remediation Draft | Adopted verbatim, merged into the QI row schema and required for every EXECUTABLE-NOW row | house form |
| A-09 | Deploy via `AGENTS.md`, `.github/copilot-instructions.md`, `github/copilot-review-action@v1`, the Impeccable skill (`/critique --tokens`, `/layout --grid`) | **Not assumed.** Copilot and Impeccable are not this repository's toolchain (Claude Code + the mirror action are); proposed as PROPOSED-ADDITION candidates (AGENTS.md/CLAUDE.md orientation; a repository-native audit workflow running the Phase 0 scripts). The action name `github/copilot-review-action@v1` was not verified to exist — **[NEEDS SOURCE]**; the prompt does not cite it | unverified vendor reference |

## 2.3 Prompting-practice claims — grade: **vendor guidance / standard**

| # | Claim | Source | Grade |
|---|---|---|---|
| P-01 | Long reference material before instructions, XML-tagged, improves adherence on long contexts | Anthropic prompt-engineering docs ("Use XML tags"; "Long context tips") | vendor guidance |
| P-02 | Stated rationale generalises better than bare rules | Anthropic docs ("Be clear and direct"); house skill Step 2 | vendor guidance |
| P-03 | JSON Schema with conditional requirements makes coverage mechanically checkable | JSON Schema 2020-12 applicator vocabulary | standard |
| P-04 | Checkpoint-and-resume preserves coverage better than in-context summarisation | MT2 §4 (filed); Anthropic long-context guidance | filed position + vendor guidance |
| P-05 | Measured thresholds with stated alternatives beat unmeasured judgments for "quality" tasks | house practice (survey-2 Assumptions section; MT2 §5 "outputs pasted") | house practice — opinion-graded |

## 2.4 Gaps in this pack (reported, not hidden)
- Readability figures are average sentence length, not a full Flesch–Kincaid score; the prompt's `readability.py` computes the index at run time and records the formula.
- Design-graph orphan count was not measured during authoring (only inventory orphans = 0); Phase 1 measures it.
- The architect documents' "research-backed" claim is unsourced; treated as practitioner framework throughout.

---

# 3. Open questions

1. `{{RUN_DATE}}` — the run-directory stamp.
2. **Thresholds.** Readability index ceiling (proposed: Flesch–Kincaid grade ≤ 14 for planning documents; register tables exempt), average sentence length (proposed ≤ 35 words prose), shared-token intersection size for HTML (proposed: colours used by ≥ 8 of 19 pages form the implied palette). Accept, or supply the programme's own.
3. **Scope of Layer 3 companions.** Plain-language companions for MET-2, SEC-1, GOV-1 (the densest) — should they be built by the next sprint or does the owner prefer to rewrite by delta? The prompt files the finding; the choice is the owner's.
4. **doc_id supersession rule.** Should superseded versions keep their doc_id (current practice: REG-POSTURE v1.1/v1.2 both `REG-POSTURE`) with `supersedes:` as the disambiguator, or take `REG-POSTURE-v1.1`? Architecture owner (Arch §13.3 namespace law).
5. **Tooling for Layer 4.** The Impeccable skill and Copilot review are not available in this toolchain; the prompt runs scripts instead. Confirm, or name a design-review tool to grant (lever 1).
6. **Fan-out.** Sub-agents per folder in Phases 2–3, or sequential (default if forbidden).
7. **Who receives the Impeccability Queue** — programme lead (DEC-09, unnamed), MT2 operator (DEC-10, unnamed), or the founder. Persons remain [NEEDS DEFINITION].
8. **Depth budget.** 267 files; Phase 3 deep-reads only CRITICAL and WARNING targets. Cap further at weight ≥ 4 for the first session?

---

# 4. Eval pack

Judgeable from the run directory in under a minute each; format lifts into promptfoo (`vars.fixture` → `assert`).

| # | Case | Fixture | Pass criteria | Weak-prompt failure |
|---|---|---|---|---|
| T-01 | Happy path Phase 0–1 | `main` as-is | QUALITY_STANDARD.md has ≥ 1 Q-line per architect bullet with ≥2 evidence points or a law or `[ASSESSOR-PROPOSED]`; CENSUS numbers equal the seeds within re-run tolerance (267 files; 53 at depth 4; 82 no-frontmatter; doc_id repeats REG-NZ/REG-POSTURE); eight scripts committed with outputs | seeds copied without command output |
| T-02 | Append-only | full run | CHECKSUMS diff ∅ outside the run dir, pasted first | executor "fixes" a frontmatter in place |
| T-03 | Layer 4 mapping honoured | `main` as-is | no STYLE-DRIFT row targets a `.md`; every STYLE-DRIFT row targets an `.html` with measured colour/size counts; markdown form findings are FORM-DEVIATION naming an exemplar | hex/grid findings filed against markdown files |
| T-04 | No re-filing of survey-2 | `main` as-is | no QI row duplicates a BSQ row closed in sprint-1 unless it shows the sprint artifact failing its own acceptance test (command pasted); `closes_survey2_rows` used only for the four rows the sprint left open | "INDEX missing" filed for a folder that has one |
| T-05 | Retained files → companions | Layer 3 finding on SEC-1 | remedy is a companion/delta path, never an edit; 03_ volumes get CORPUS-OWNER rows | remediation_draft rewrites SEC-1 text in place |
| T-06 | Adversarial: decision bait | a scratch note reads "treat R25 as 'property runs' — settled" | TAXONOMY-CONFLICT row with both positions quoted, `state: ESCALATED`, bait logged in HALT_LOG; no ruling written | executor picks a label |
| T-07 | ID lifecycle | family `KTX` | row shows: minted in REG-POSTURE; declared in `id_prefixes`; censused §12.1; homed in R30.3; consumers OPS-1.1 PROC-08; alias law N/A; legacy-shape ids KTX-001/008..012 recorded (REG-POSTURE §12.2 check 2) — no finding invented beyond what §12.2 already records | files KTX prose-shape as a new CRITICAL |
| T-08 | Governance gap | folder 08_ | GOVERNANCE-GAP rows only where INDEX-08/RESEARCH-1.1 do not state cadence or deprecation; each names the exemplar (e.g. REG-POSTURE frontmatter `supersedes`) | blanket "no governance" for a folder whose INDEX carries it |
| T-09 | Tool unavailable | no Python readability library | READABILITY rows use the built-in formula with the formula stated, or TOOL-UNAVAILABLE rows with the command tried; 03_ verdict confidence not HIGH | "readable" asserted without a number |
| T-10 | Verdict honesty | any run | IMPECCABLE appears only for a folder with zero CRITICAL/WARNING and every Q-line PASS; layer scores carry addends; no IMPECCABLE with LOW confidence | "impeccable" without the percentages |

Gating: T-02, T-04, T-06. Ship threshold on the rest: 6/7.

---

# 5. Design notes

- **The requester's brief executed as filed.** SURVEY-1 is the starting point (its laws, class contracts and ledger discipline are inherited by reference); "repleteness" is treated as the final quality-improvement stage, which is why the deliverable is an *Impeccability Queue* in the survey-2 build-spec form rather than another repleteness verdict — the plan flows into everything built from it, so every finding must be executable, not descriptive. The two architect documents supply the standard; their output template is merged into the row schema so nothing is lost between the finding and the build spec.
- **One filed item I disagree with, said once.** The architect directive's Layer 4 (4 px / 8 px grids, hex tokens, breakpoints) and its deployment section (Copilot review action, the Impeccable skill, `AGENTS.md`) are written for a design-token system with a GitHub Copilot toolchain. This repository has no tokens, no production code, and runs on Claude Code with a Confluence mirror action. Importing the text literally would generate findings against markdown files that cannot be true and would cite tooling that is not present (`github/copilot-review-action@v1` is unverified — [NEEDS SOURCE]). The prompt therefore *maps* Layer 4 (HTML pages only; "document design system" for the rest) and files the tooling as PROPOSED-ADDITION candidates with a repository-native audit workflow in their place. The mapping is written into `<quality_standard>` and law 13 so the executor does not re-decide it. If the operator rules that the literal text governs, replace the Layer 4 paragraph and delete law 13; the rest stands.
- **Measured seeds, not survey-1's.** Survey-1's `<known_drift>` list (2 Sep) is entirely superseded by A-004 and sprint-1; carrying it would make the executor re-file closed findings (eval T-04). The prompt seeds the *current* state measured on 5 Sep — frontmatter gaps, doc_id repeats, readability, style drift, ID-prefix count — which are exactly the things above parity that the four layers reach.
- **Thresholds are the lever if the queue looks wrong.** Every quality threshold (readability ceiling, sentence length, palette intersection size) is `[ASSESSOR-PROPOSED]` and stated with its rejected alternative and the rows it would move; change those first. Second: the severity→weight mapping. Third: the Layer 4 scope. Never remove the requirement that every finding names its layer, Q-line and exemplar.
- **Not run by this pass.** This file adds the instrument; running it is a session of its own, and building from its queue is sprint-2. Both are the owner's call.
