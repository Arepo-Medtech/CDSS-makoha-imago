---
doc_id: PROMPT-SURVEY-2
title: "PROMPT-SURVEY-2 — Folder-Parity Survey: Surveyor, Assessor and Final-Pass Recommender over 04_–10_, measured against the 01_–03_ standard, producing the Build-Spec Queue"
version: "1.0"
date: "2026-09-02"
status: "Proposed. Produced by the arepo-metaprompt skill (GENERATE mode, from the requester's first draft). Adds this file under 11_prompts/ only; edits nothing in 00_–10_. Successor to PROMPT-SURVEY-1 (whole-repository repleteness survey): narrower scope (seven folders), different deliverable (a build-specification queue, not a repleteness verdict). Neither prompt has been run; no 11_prompts/runs/ directory exists at authoring."
produced_by: "arepo-metaprompt v-house · requester: Kendo-Jones (ken.lee@arepo-tech.ai)"
executor: "Claude Code, started at the repository root (makoha-imago-v1.2/)"
---

# 0. Lever

**Lever 2 (curate the context) stacked with Lever 4 (sharpen the wording).** The draft's one rule — "bring 04–10 up to the level of 01–03" — is unexecutable as written because "the level of 01–03" is nowhere defined; an executor would substitute its own taste (most likely *length*, since the 01–03 files are 25–93 KB and the 04–10 files are mostly 1.5–5 KB). The prompt therefore (a) makes the executor **derive the parity standard from 01–03 itself**, as sourced contract lines, before it judges anything, and (b) hands it a fixed **Build-Spec Queue** row schema so every recommendation is a buildable, weighted, owner-attributed item rather than prose. The PRESENT/ABSENT census the draft asks for becomes a mechanical step (paths and byte counts), and the "measure against class contract" step reuses HARDEN-2's CC-1..CC-8 bars and PROMPT-SURVEY-1's class-contract table, both already in the tree. No new tool is needed: `ls`, `wc -c`, `grep`, `sha256sum`, `python3 -c "import json,jsonschema"` and a mermaid parser cover every check named.

---

# 1. The prompt

Paste the block below as the first message of a Claude Code session started at `makoha-imago-v1.2/`. Replace every `{{PLACEHOLDER}}` first, or leave it and the executor files the gap in `OPEN_QUESTIONS.md` and carries on.

```markdown
<role>
You are Claude Code operating at the root of the Mākoha Imago repository (`makoha-imago-v1.2/`), a governed, append-only document-and-skeleton repository for an Australian general-practice clinical decision support system that is on its way to code freeze, deployment and regulated supply. For this run you hold one office with three duties:

1. **Surveyor** — discover and census every item in the seven target folders; nothing sampled, nothing summarised.
2. **Assessor** — for every item and every chain link the parity standard requires: first PRESENT or ABSENT (a path and byte count, or the exact search that failed); then, for PRESENT items, PASS/FAIL against each contract line, with a quoted line as evidence.
3. **Final-pass recommender** — state, in writing, exactly what must exist in each target folder before an elite ecosystem orchestrator could carry this repository to completion, code freeze and deployment with nothing left behind — as a dependency-ordered, weighted **Build-Spec Queue** whose every row a Claude Code session or a named human could act on.

You recommend; you do not decide and you do not build. Decisions close only by their named owners (MET-2 / MET-2.1 DEC rows). Build items are specified by you and executed by later runs. You stop with a clear hand-back at every point where a human decision is the next step.
</role>

<context>
<the_one_rule>
BRING FOLDERS 04_–10_ UP TO THE SAME LEVEL OF SPECIFICATION AND STANDARD AS ESTABLISHED IN FOLDERS 01_–03_.
"Level" means *conformance to the document contracts 01_–03_ actually exhibit* (Phase 0 derives them, with citations). It never means byte count. A 1.5 KB file that carries every contract line its class requires is at parity; a 60 KB file missing its ID census is not.
</the_one_rule>

<scope>
Target folders (work them in this order, one at a time, to closure): `04_hardening/` → `05_registers-and-contracts/` → `06_repositories/` → `07_deployment-and-operations/` → `08_research/` → `09_diagrams/` → `10_regulatory-execution/`.
Reference folders (the standard; read, never judged, never edited): `01_north-star-and-transformation/`, `02_cdss-stack-augmented/`, `03_makoha-butterfly-corpus/`.
Out of scope for judgement (cite as needed): `00_MANIFEST.md`, `00_inventory.txt`, `11_prompts/`, root loose files. If a target-folder finding depends on one of these (e.g. 00_MANIFEST §1 does not index a file), file it as a row with `folder` = the target folder and the out-of-scope path in `evidence`.
</scope>

<laws_you_operate_under>
1. APPEND-ONLY. No byte of any pre-existing file may change. You write only under `11_prompts/runs/{{RUN_DATE}}_survey-2/` (create it). Checksums before (Phase 0 step 5) and after (Phase 3 step 1); a non-empty diff outside your run directory is reported above everything else. Source: 00_MANIFEST §1 (X1 discipline), §4.1, §8; EXEC-1 preamble.
2. PRECEDENCE. Sequencing: EXEC-1 (10_) governs over MET-4 / DEPLOY-1 / volume phasing (EX-1). Content: 03_ corpus volumes are normative for architecture under their own `03_makoha-butterfly-corpus/MANIFEST.md`; REG-POSTURE v1.1 is canonical posture and ADVISORY_ONLY for regulation (EX-3); MT2 is a standing order over the execution layer. A parity requirement you derive can never relax a host MUST.
3. DELTA-READING. REG-SPRINT v1.0 only through REG-SPRINT-1.1 (EX-2); MET-1 through MET-1.1; MET-2 with MET-2.1; R30 seed with R30.1. A row citing a superseded position is itself a defect.
4. OPEN MEANS OPEN. No ASSUME-* closes by anything you write (EX-7). J-3 is not retired until DEC-06 closes (EX-4). A missing decision is a row of class DECISION-PENDING carrying its DEC/ASSUME/Q-REG/NZ-Q ID — never a gap you fill and never a build item you spec around it.
5. RETAINED-VERBATIM IS NOT REWRITTEN. Many 04_–10_ files carry status "Retained" or "verbatim" (MT2 directive; Arch-derived §§ in 07_). Parity is reached by *companion* files (briefing, primer, prompt, delta, index) or by an appended annex under the delta pattern (MET-1.1, R30.1, REG-SPRINT-1.1) — never by editing the retained text. A build item whose remedy would edit a retained file is malformed; rewrite it as a companion or delta.
6. HARDENING IS NOT YOUR PASS. HARDEN-3 W0–W11 and the R29 ledger belong to the MT2 pass. You do not open, write or pre-empt R29 rows. Where an item needs hardening, the remedy is a pointer to its HARDEN-3 task ID, or a row of class ABSENT-WORKLIST-TASK if none exists.
7. NO SILENT SHORTCUTS. MT2 §4 anti-rationalization applies verbatim. Specifically prohibited: sampling the 93 files of 06_ ("they are all the same shape"); treating the seven 10_ files as one because they share an authority line; inferring a folder's contents from 00_MANIFEST §1 instead of `ls`; deriving the parity standard from memory of "what good docs look like" instead of from the 01_–03_ files. Every temptation you notice is one line in `HALT_LOG.md`, then the full step is done.
8. EVIDENCE OR NOTHING. Every PRESENT carries path + byte count; every ABSENT carries the exact `find`/`grep` that failed; every FAIL carries the contract line and the quoted line (or "no such heading") that fails it; every number is pasted from command output. REG-POSTURE §0.4 DONE-WITH-EVIDENCE; MT2 §5.
9. PRIVACY / LICENSING / REMOTES. No patient data exists here and none may be created or fetched. Licensed guideline text is cited by reference. Nothing is pushed, deployed or published. You do not clone `Arepo-Medtech/Makoha` (DEC-12 / G-08).
10. REUSE, DON'T REDO. If `11_prompts/runs/*_survey-1/` exists with a validated `SURVEY-L.jsonl`, load it: its CENSUS, CHAIN.md and CLASS_CONTRACTS.md are inputs to your Phase 0, and every SURVEY-L row for a 04_–10_ path is cited by `SL-nnnn` in your rows rather than re-derived. If it does not exist, say so once in ORIENTATION.md and proceed; do not run SURVEY-1.
</laws_you_operate_under>

<what_a_wrong_answer_costs>
A Build-Spec Queue that declares a folder at parity while a load-bearing companion is absent sends the orchestrator into code freeze with a hole that surfaces at GATE-000 (counsel), GATE-002 (identifiable data) or GATE-004 (first lawful clinical supply) — where a missing artifact costs months. A queue padded with "write a longer version of X" items burns build sessions on prose that changes no contract and, worse, trains reviewers to skim the queue. Therefore every build item names the contract line(s) it satisfies, and any item whose only justification is length is dismissed in writing.
</what_a_wrong_answer_costs>

<known_state_to_confirm_not_assume>
Observed 2026-09-02 during prompt authoring. Seeds for Phase 1 — confirm each by command, then file; never copy unverified.
- Byte counts. 01_–03_ load-bearing files run 20–93 KB (MET-1 64,435 B; corpus volumes 19,982–93,334 B; butterfly primers 48,752–92,580 B; programme prompt 27,473 B; RUN-REPORT 73,803 B). 04_–10_ files outside MT2/EXEC-1/REG-POSTURE/MAK-GOV/REG-NZ/REG-SPRINT run 1,212–4,572 B (HARDEN-3 2,558 B; DEPLOY-2 1,839 B; GOV-1 1,518 B; SEC-1 2,205 B; REG-R30 1,308 B). This is the visible symptom; the parity standard you derive is what turns it into findings, or dismisses it.
- Companion chain. 02_ has `primers_briefing.md`; 03_ has `corpus_artifacts_briefing.md`, its own `MANIFEST.md`, `butterfly-primers/` (11 primers + RUN-REPORT), a programme prompt, `artifacts-html/` (16), and launch prompts in 11_ for every primer and every butterfly primer. No target folder has a briefing, an index/manifest of its own (06_ REPO-MAP is the nearest), a primer, a launch prompt in 11_, or an artifact page.
- Frontmatter. 04_ MT2 directive: none (retained verbatim). 05_ CONTRACT-ARG-1, REG-R29 (md), REG-R30: no `version`/`date`. 06_ REPO-MAP: no `version`/`date`. 07_ all five: no `date`. `req_prefix`/`req_count` appear only in EXEC-1 (EX, 10) and MAK-GOV (NDG, 14); no other target file declares an ID namespace or count. No target file carries an ID census or self-audit section of the 03_ kind.
- Ownership. GOV-1 states "person-level owners [NEEDS DEFINITION] throughout"; FOLD-1 owner is "[NEEDS DEFINITION — same gap as G-09]"; REG-R29 owner cdss-spine, REG-R30 owner cdss-governance (roles, not persons).
- Worklist coverage. HARDEN-3 W8 covers 05_/06_/07_/08_ (T-100..107); W10 covers 04_'s own artifacts; EXEC-1 EX-5 adds 10_ to the W11 sweep. No HARDEN-3 wave names 09_ by folder (W6 T-070..072 names the diagram files). No HARDEN-1 row exists for any 10_ file.
- 06_. 93 files: 53 README.md, 19 MANIFEST.yaml, 12 pipeline.yml, 4 CODEOWNERS, REPO-MAP_v2.md, GPP-CHANNEL.md, CONTRACT-ARG-1.pointer.md, 2 .DS_Store (exclude). 19 skeleton trees; REPO-MAP declares 14 existing + 4 proposed + 1 channel.
- 09_. Four `.mermaid` sources + `cdss_diagrams_v2.html`; DEF-001 (00_MANIFEST §5) records all four parse @ mermaid 10.9.0; none carries frontmatter (format has no YAML block — judge by header comment instead).
- 11_prompts/runs/ does not exist; PROMPT-SURVEY-1 has not been executed.
</known_state_to_confirm_not_assume>
</context>

<instructions>
Work in four phases. A phase does not open until the previous phase's outputs exist on disk under `11_prompts/runs/{{RUN_DATE}}_survey-2/`. Fan-out is permitted in Phase 2 only, one sub-agent per target folder, each writing its own `folders/NN_name/` directory; the orchestrator validates every sub-agent's `rows.jsonl` against the schema and counts rows against that folder's census — it never summarises a sub-agent's coverage.

<phase_0 name="Orient, derive the parity standard, arm">
1. Read, in this order, recording path + section anchors in `ORIENTATION.md`:
   a. `00_MANIFEST.md` in full (§3 production sequence; §4.4 and §8 honesty lines — copy verbatim; §7 A-001, §8 A-002).
   b. `10_regulatory-execution/EXEC-1_execution_directive.md` EX-1..EX-10 and the RUN table.
   c. `04_hardening/MAJOR_TASK_2_anti-laziness-hardening-directive.md` §1 (eight properties), §4, §5, §6; `HARDEN-2_hardening_spec.md` (CC-1..CC-8); `HARDEN-3`; `HARDEN-1` (all rows).
   d. `01_north-star-and-transformation/` — all six files (MET-1 through MET-1.1; MET-2 with MET-2.1; MET-3; MET-4).
   e. `03_makoha-butterfly-corpus/corpus_artifacts_briefing.md` Part 1 and Part 2; `03_.../MANIFEST.md`; the frontmatter, Contents, ID-census and self-audit sections of `corpus-md/four-faces-corpus_v1.1.md`; `butterfly-primers/RUN-REPORT.md` §1; the first 120 lines of `butterfly-primer-programme_prompt_v1.0.md`.
   f. `02_cdss-stack-augmented/primers_briefing.md` in full; `primer_A_bayesian_engine.md` headings A1–A10 and the annex A10 ten-field block; `architecture_and_integration.md` §10, §12.1–12.3, §13.3, §13.6, §13.9.
   g. `11_prompts/PROMPT-SERIES_A-L_index.md` header and laws; `11_prompts/PROMPT-SURVEY-1_ecosystem_repleteness_surveyor.md` §1 `<class_contracts>` table and `<ledger_schema>` (inherit both; do not re-derive).
2. Write `PARITY_STANDARD.md` — the deliverable that makes the one rule executable. It has two parts:
   **Part A — Document-level contract lines (P-D-nn).** For each thing the 01_–03_ files *consistently do*, one line: what it is · the 01_–03_ evidence (≥2 files, path + quoted line or heading) · the law that requires it if one exists (corpus briefing Part 1; Arch §13.9; 00_MANIFEST §4.2's ten execution fields; PROMPT-SERIES laws) or `[ASSESSOR-PROPOSED]` if none does · which target classes it applies to (from the inherited class-contracts table). Expect at minimum: YAML frontmatter with `doc_id`, `title`, `version`, `date`, `status` stating what is and is not claimed; `supersedes`/`precedence`/`authority` where the class has one; `req_prefix`/`req_count` for any document that mints IDs; numbered requirement blocks with `Statement` + `Rationale trace` for normative text; RFC 2119 usage declared; a Contents section for files > 15 KB; a traceability/sources section; an ID census equal to declared count; a self-audit section; delta files that name base + version and enumerate D-n amendments; every table row that mints an ID names an owner and a status from a closed enum; every `[NEEDS DEFINITION]`/`[NEEDS SOURCE]` registered in MET-2/MET-4/R30 or a finding.
   **Part B — Folder-level chain (P-F-nn).** The companion set a *folder* at 01_–03_ level carries, derived from what 02_ and 03_ carry: BRIEFING (what this folder's documents are, as ecosystem items — `primers_briefing`, `corpus_artifacts_briefing` pattern) · INDEX/MANIFEST (every file listed with role, status, byte count, disposition) · CORPUS-GRADE LOAD-BEARING DOCUMENTS (Part A) · PRIMER (how to build/operate the thing the documents specify — 02_ A1–A10 spine or 03_ butterfly-primer spine, with the ten execution fields) · LAUNCH PROMPT in 11_ (PROMPT-SERIES form, inheriting PROMPT-P0 laws) · ARTIFACT-HTML twin where the folder's readers include humans outside the build (03_ pattern) · REPO-SKELETON home in 06_ where the folder specifies something that will be code · HARDEN-1 row + HARDEN-3 task for every file · 00_MANIFEST index row current. For each link, state the applicability test you will use per folder (e.g. "ARTIFACT-HTML applies where the folder's declared readers include counsel, clinicians or the board — REG-POSTURE, MAK-GOV, DEPLOY-1; it does not apply to a JSON schema") and mark the test `[ASSESSOR-PROPOSED]`. A chain link is a *requirement*, not a suggestion, only when a cited law demands it; otherwise it is a PROPOSED-ADDITION with weight computed honestly.
   Every line in Parts A and B carries a stable ID (P-D-01…, P-F-01…). Rows in later phases cite these IDs; a finding that cites no P-line is out of order.
3. Write `CLASS_CONTRACTS.md`: copy PROMPT-SURVEY-1's table verbatim, then append any lines Part A adds per class, each with its source. Mark unsourced lines `[ASSESSOR-PROPOSED]`.
4. Write `BSQ.schema.json` exactly as given in the queue schema section; validate it (`python3 -c "import json,jsonschema; jsonschema.Draft202012Validator.check_schema(json.load(open('BSQ.schema.json')))"`); paste output into ORIENTATION.md. If `jsonschema` is missing, install in a venv under the run directory, never system-wide; record the command.
5. Baseline: `find . -type f ! -name .DS_Store -print0 | sort -z | xargs -0 sha256sum > CHECKSUMS_BEFORE.txt`; file count into ORIENTATION.md.
6. Exit: ORIENTATION.md, PARITY_STANDARD.md (Parts A+B, every line with ≥2 reference-folder evidence points or a law), CLASS_CONTRACTS.md, BSQ.schema.json + check output, CHECKSUMS_BEFORE.txt. Failure handling: a step-1 file that cannot be opened halts Phase 0 — exact error to `HALT_LOG.md`, stop; a survey that could not read its own standard has no standing to judge against it.
</phase_0>

<phase_1 name="Census of the seven target folders (mechanical)">
Produce `CENSUS.md` and `census.json`. Every number is beside the command that produced it.
1. Per target folder: full file list with byte counts, `.DS_Store` excluded; count; count vs 00_MANIFEST §1/§7/§8 declared count (a mismatch is a row: INVENTORY-DRIFT).
2. Frontmatter census per `.md`: opens with `---`? carries `doc_id`, `title`, `version`, `date`, `status`? `req_prefix`/`req_count`? `owner`? `supersedes`/`authority`/`precedence`? Table it. For `.json`, `.yaml`/`.yml`, `.mermaid`, `.html`: record the header comment or `$id`/`title` in lieu.
3. ID census per target file: IDs *defined* (introduced in a heading or table row) vs *cited*. Namespaces to grep: `CC-\d`, `T-\d{3}`, `W\d{1,2}`, `R\d{1,2}`, `DEC-\d\d`, `C-\d\d`, `G-\d\d`, `RG-\d\d`, `EX-\d{1,2}`, `RUN-\d`, `NDG-\d{1,3}`, `TASK-REG-\d{3}`, `ASSUME-REG-\d{3}`, `NZ-ASSUME-\d{3}`, `NZ-Q-\d{3}`, `NZ-TASK-\d{3}`, `Q-REG-\d{3}`, `GATE-\d{3}`, `SG-V\d-\d`, `REG-FIND-\d{3}`, `WATCH-REG-\d{3}`, `OBL-\d{3}`, `KTX-\d{3}`, `GPP-\d{1,2}`, `SPINE-\d`, `D-\d`, `A-\d{3}`, `DEF-\d{3}`, `V\d-[SCE]\d[a-z]?`, `AN-\d{1,2}`. Cited-but-defined-nowhere-in-tree → DANGLING-REF row. Declared `req_count` ≠ counted definitions → STALE-COUNT row.
4. Chain census — `CHAIN.md`, one row per target folder and one per load-bearing target file, columns = the Part B links, each cell a path + bytes or `ABSENT` (with the search). Plus, per file: HARDEN-1 row id or ABSENT · HARDEN-3 task id or ABSENT · 00_MANIFEST index row or ABSENT · 11_ launch prompt or ABSENT · 06_ skeleton home or ABSENT/N-A.
5. Reference resolution: every backtick path and markdown link in every target `.md` → exists? Every `§n`/`Part n`/`EX-n`/`CC-n` anchor into a named document → resolves? Script it as `tools/refcheck.py` (reuse SURVEY-1's if present). Unresolved → DANGLING-REF rows.
6. Browser-borne (09_ only, plus any `.html` elsewhere in targets): mermaid parse per source (tool + version recorded); `.html` inlined blocks extracted and parsed.
7. Exit: CENSUS.md, census.json, CHAIN.md, tools/refcheck.py, `census_rows.jsonl` (validated; count pasted). A check whose tool is missing → TOOL-UNAVAILABLE row with the command tried; census continues.
</phase_1>

<phase_2 name="Assess — folder by folder, 04_ → 10_, to closure before the next opens">
For each target folder write `folders/NN_name/ASSESSMENT.md`, `folders/NN_name/FIRST_REQUIREMENTS.md` and `folders/NN_name/rows.jsonl`. Do not open the next folder until all three exist and rows validate.
1. **Discovery.** Every item listed; each assigned ≥1 class label from CLASS_CONTRACTS.md (REPOSITORY / SCHEMA / SEED / SPEC / WORKLIST / DIRECTIVE / CONTRACT / REGISTER / DELTA / REGULATORY / DEPLOY-OPS-GOV-SEC / RESEARCH / DIAGRAM / REPO SKELETON / …). Record the label decision and why. No fit → UNCLASSIFIED-ITEM with an `[ASSESSOR-PROPOSED]` label. State which items are **load-bearing** (criticality 2 per the weighting section) and why.
2. **Presence pass (folder chain).** For every Part B link: applicability verdict for this folder (APPLIES / DOES-NOT-APPLY, with the P-F test cited and one line of reason) → PRESENT (path, bytes) or ABSENT (search). Every ABSENT-and-APPLIES is a Build-Spec Queue candidate.
3. **Presence pass (document contract).** For every item and every applicable Part A line: PRESENT / ABSENT (heading or field name quoted, or "no such heading/field").
4. **Measurement pass.** For every PRESENT item: every applicable CLASS_CONTRACTS line PASS/FAIL with quoted evidence; declared counts (rows, tasks, fields, "sixteen", "ten") equal to what is on the page; every cross-reference resolvable (Phase 1 step 5); owner named where the class requires it; status line honest against the tree (e.g. "no task started" while a run directory exists). For retained-verbatim items, measure the *companion set* and the honesty of the retention notice — never the retained text itself (law 5).
5. **Chain confirmation.** Confirm or correct CHAIN.md rows for this folder.
6. **Weighting.** Every row gets `weight`, `criticality`, `radius`, `executability` per the weighting section.
7. **FIRST_REQUIREMENTS.md** — the folder's *immediate first requirements*, in queue order: the things that must exist before deep work on this folder's items is even meaningful (typically: an index; a briefing; corpus-grade frontmatter + ID census on the load-bearing file; a HARDEN-1 row and HARDEN-3 task for every file; a launch prompt). Each is one line: `[weight] [P-id] [class] {what is absent or fails} — evidence: {command/quote} — blocks: {gate/run/wave/prompt IDs} — remedy: {one imperative sentence a Claude Code session could execute, or "HUMAN-ONLY: DEC id / owner"}`.
8. **Folder exit.** rows.jsonl row count ≥ item count + applicable-chain-link count (presence is also evidence — a PRESENT-CONFORMANT row carries path and bytes). Validation output pasted at the foot of ASSESSMENT.md. Append `CHECKPOINT.md` line: folder, rows, timestamp. If context runs long, stop *between* folders, never inside one; resume rule: "read CHECKPOINT.md, continue at the first target folder not listed".
</phase_2>

<phase_3 name="Build-Spec Queue, dismissals and hand-back">
1. Re-checksum → `CHECKSUMS_AFTER.txt`; diff against BEFORE; paste diff (or "∅") at the top of `BUILD_SPEC_QUEUE.md`. Non-empty outside the run directory = stop-the-line; report first.
2. Merge all `rows.jsonl` → `BSQ.jsonl`; validate every row; paste count + output. Coverage check: every path in the Phase 1 census appears in ≥1 row's `artifact_path`, or the queue names the paths that have none and why.
3. Write `BUILD_SPEC_QUEUE.md` in this fixed order:
   a. **Coverage statement** — files censused / files with ≥1 row / chain links assessed / items measured. Numbers from commands only.
   b. **Parity verdict per folder** — one of: AT-PARITY (every applicable P-line and contract line PASS; no ABSENT-and-APPLIES; no CONTRADICTION; no DANGLING-REF) · AT-PARITY-WITH-DECISIONS-PENDING (only DECISION-PENDING rows remain — list IDs) · BELOW-PARITY (list blocking row IDs and the count of P-lines FAIL / total applicable, as a percentage). No fourth state.
   c. **The Build-Spec Queue** — every row with `weight ≥ 3`, grouped by `executability` (CLAUDE-CODE-EXECUTABLE-NOW first, then EXECUTABLE-AFTER-DECISION, then HUMAN-ONLY, then CORPUS-OWNER / EXTERNAL-PARTY), within group ordered by weight desc, then by earliest blocked gate (GATE-000 first per EXEC-1 RUN-0), then by dependency (`depends_on` before dependents). For every CLAUDE-CODE-EXECUTABLE-NOW row, `build_spec` is a complete, self-contained specification: target path (new file, or delta/companion beside a retained file — law 5) · class and the P-lines/contract lines it must satisfy · mandatory sections and fields · inputs it reads (paths) · laws it obeys (append-only; delta pattern; precedence) · evidence it must capture · acceptance test (mechanical where possible) · the row IDs it closes · the HARDEN-1 row / HARDEN-3 task it should be entered under or the ABSENT-WORKLIST-TASK row it depends on · owner who ratifies. Write these to the standard of PROMPT-P0 §1 and the PROMPT-SERIES form — they are what the operator will actually run.
   d. **Sequenced first-requirements roll-up** — the seven FIRST_REQUIREMENTS lists merged into one ordered list with cross-folder dependencies made explicit (e.g. "05_ index before 04_ HARDEN-1 parity row, because HARDEN-1 cites R29 schema by path"). State the ordering rule used and its source (00_MANIFEST §3 production sequence; HARDEN-3 wave order; EXEC-1 RUN order).
   e. **What is NOT required** — rows considered and dismissed as not blocking completion, code freeze or deployment, each with a reason. Length-only findings are dismissed here by name. ORPHAN-ID and cosmetic frontmatter on informative files go here unless a P-line with a cited law says otherwise.
   f. **Proposed ecosystem additions** — chain links and document classes the 01_–03_ pattern or a cited law implies but no target folder provides. Candidates to test, not conclusions: a briefing per target folder; a per-folder INDEX.md; `04_` primer for running the MT2 pass (operator's runbook); `05_` register-of-registers index reconciling R29/R30 with Arch §12.2; `06_` skeleton conformance report and REPO-MAP↔tree reconciliation; `07_` RTO/RPO/DR-drill definition (G-09) and owner register (DEC-09/DEC-10); `07_` threat model / data-flow diagram SEC-1 can hang from; `08_` RG-01..06 resolution worklist; `09_` diagram↔Arch §10/§11↔REPO-MAP node reconciliation and a diagram index; `10_` counsel-packet index + RUN-0..4 calendar as a checkable worklist; launch prompts `PROMPT-HARDEN`, `PROMPT-REG-EXEC`, `PROMPT-DEPLOY` in 11_; `00_MANIFEST` amendment A-003 text indexing 11_ and 03_ additions. Each marked `[ASSESSOR-PROPOSED]`, citing the P-line and law, naming folder, ratifying owner, and whether it blocks a gate. You propose; you do not create.
   g. **Honesty lines** — mirror 00_MANIFEST §4.4/§8: what this run did NOT do (did not edit any file; did not execute any HARDEN-3 task; did not open 03_ corpus content beyond the sections named in Phase 0; did not clone HeyDoc; did not run `validate_build_plan.py`; TOOL-UNAVAILABLE checks listed; SURVEY-1 outputs used or absent).
   h. **Hand-back** — the first three human decisions that gate the queue, each with DEC/ASSUME ID, owner, and the queue rows it unblocks.
4. `HALT_LOG.md` final section: every temptation logged and what you did instead.
5. `OPEN_QUESTIONS.md`: every `{{PLACEHOLDER}}` unresolved; every ambiguity in this prompt you interpreted (with your interpretation); every question for the operator.
6. `PROPOSED_AMENDMENTS.md`: text of a 00_MANIFEST amendment A-003 (indexing 11_ and this run) and one honesty line naming this run — for the manifest owner to append; you do not append it.
</phase_3>
</instructions>

<class_contracts>
Inherit the `<class_contracts>` table of `11_prompts/PROMPT-SURVEY-1_ecosystem_repleteness_surveyor.md` verbatim as the floor for every label used here (DIRECTIVE, SPEC, WORKLIST/PLAN, SEED/LEDGER, SCHEMA, REGISTER, CONTRACT, REPO SKELETON, DIAGRAM, DEPLOY/OPS/GOV/SEC, REGULATORY, DELTA, RESEARCH, GAP/DECISION REGISTER). Extend in Phase 0 step 3 with the Part A lines that apply per class. Two additions this run makes to the floor, both sourced:
| Label | Must additionally carry | Source |
|---|---|---|
| Any target file that mints IDs | `req_prefix` + `req_count` in frontmatter; ID census section equal to count; retired IDs never reused | corpus briefing Part 1 (frontmatter table; `change_policy`); EXEC-1 and MAK-GOV already conform |
| Any target folder | an index of its own files (role · status · bytes · disposition · HARDEN row · HARDEN task) or a finding ABSENT-ITEM at folder level; a briefing or a finding | 02_ `primers_briefing.md`; 03_ `MANIFEST.md` + `corpus_artifacts_briefing.md`; 00_MANIFEST §3 (read order needs per-folder entry points) — folder-level lines are `[ASSESSOR-PROPOSED]` until DEC ratifies |
</class_contracts>

<weighting>
`weight` = min(5, criticality + radius), integers, both addends stated in the row.
- `criticality` ∈ {0 informative · 1 load-bearing for its folder · 2 load-bearing for the ecosystem — a DIRECTIVE, SPEC, SCHEMA, CONTRACT, REGISTER, precedence rule, safety/firewall boundary, or any file another folder cites by path}.
- `radius` ∈ {0 blocks nothing · 1 blocks a HARDEN-3 wave or a PROMPT run · 2 blocks a DEPLOY-1 step or a regulatory gate (GATE-000..004, SG-*, NZ-GATE-*) · 3 blocks code freeze or first lawful supply}.
- `executability` orders the queue within weight and is the field that makes the queue useful to a Claude Code session: CLAUDE-CODE-EXECUTABLE-NOW (all inputs on disk, no open decision in the path, remedy is a new or companion file) · EXECUTABLE-AFTER-DECISION (spec can be written now; creation waits on a named DEC/ASSUME) · HUMAN-ONLY (decision, attestation, appointment of an owner) · CORPUS-OWNER (defect in 03_ content) · EXTERNAL-PARTY (counsel, TGA/Medsafe, supplier).
- `parity_gap` (integer) = number of applicable P-lines FAIL/ABSENT for the item; tie-break only, never an addend. Length is not a P-line and never contributes.
Weight ≥ 3 enters the queue. Weight 5 rows are listed first in the hand-back. A row that would have weight ≥ 3 only because of `parity_gap` is mis-scored; re-derive the addends.
</weighting>

<build_spec_queue>
The queue is the deliverable. Every queue row is a `BSQ.jsonl` record and, for CLAUDE-CODE-EXECUTABLE-NOW rows, a `build_spec` block in BUILD_SPEC_QUEUE.md §c with these headed fields, in order: **Target path** · **Class + P-lines satisfied** · **Mandatory sections/fields** · **Inputs (paths)** · **Laws** · **Evidence to capture** · **Acceptance test** · **Closes rows** · **HARDEN linkage** · **Ratifying owner** · **Depends on** (row IDs). A build_spec with any empty field is malformed and fails validation of the queue. Build specs are written so that the very next Claude Code session can execute one with no context beyond the repository and the spec — the MT2 §5 naive-executor test applied to your own output. Where a build item is a launch prompt for 11_, the spec names the PROMPT-SERIES laws it must inherit and the folder's P-lines it must enforce; where it is a briefing or index, the spec names the 02_/03_ exemplar it mirrors by path.
</build_spec_queue>

<queue_schema>
Write this verbatim as `BSQ.schema.json`:
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "makoha-imago-v1.2/11_prompts/runs/survey-2/BSQ.schema.json",
  "title": "BSQ — Build-Spec Queue row (Proposed; feeds the MT2 operator, the P0 queue and 11_ launch prompts; is not R29)",
  "type": "object",
  "required": ["row_id","folder","artifact_path","label","finding_class","parity_lines","statement","evidence","weight","criticality","radius","parity_gap","blocks","executability","owner","state"],
  "properties": {
    "row_id": {"type":"string","pattern":"^BSQ-[0-9]{4}$"},
    "folder": {"enum":["04","05","06","07","08","09","10","CHAIN"]},
    "artifact_path": {"type":"string","minLength":1,"description":"repo-relative path, or the path that SHOULD exist for ABSENT-* classes"},
    "label": {"type":"array","minItems":1,"items":{"type":"string"}},
    "finding_class": {"enum":["PRESENT-CONFORMANT","ABSENT-ITEM","ABSENT-SECTION","ABSENT-CHAIN-LINK","ABSENT-WORKLIST-TASK","ABSENT-LEDGER-ROW","ABSENT-INDEX-ROW","INVENTORY-DRIFT","STALE-COUNT","DANGLING-REF","ORPHAN-ID","CONTRADICTION","DECISION-PENDING","PLACEHOLDER-UNREGISTERED","TACIT-KNOWLEDGE-REQUIRED","UNDEFINED-OWNER","QUALITY-BELOW-BAR","UNCLASSIFIED-ITEM","TOOL-UNAVAILABLE","PROPOSED-ADDITION"]},
    "parity_lines": {"type":"array","items":{"type":"string","pattern":"^P-[DF]-[0-9]{2}$"},"description":"P-lines judged; may be [] only for PRESENT-CONFORMANT, INVENTORY-DRIFT, TOOL-UNAVAILABLE"},
    "contract_line": {"type":"string"},
    "statement": {"type":"string","minLength":20},
    "evidence": {"type":"string","minLength":1,"description":"verbatim command + output, or quoted lines with path:line; a bare assertion is a violation (MT2 §5)"},
    "sibling_positions": {"type":"array","items":{"type":"object","required":["path","quote"],"properties":{"path":{"type":"string"},"quote":{"type":"string"}}}},
    "weight": {"type":"integer","minimum":0,"maximum":5},
    "criticality": {"type":"integer","minimum":0,"maximum":2},
    "radius": {"type":"integer","minimum":0,"maximum":3},
    "parity_gap": {"type":"integer","minimum":0},
    "blocks": {"type":"array","items":{"type":"string"}},
    "executability": {"enum":["CLAUDE-CODE-EXECUTABLE-NOW","EXECUTABLE-AFTER-DECISION","HUMAN-ONLY","CORPUS-OWNER","EXTERNAL-PARTY","NONE"]},
    "build_spec": {"type":"object","required":["target_path","class_and_plines","mandatory_sections","inputs","laws","evidence_to_capture","acceptance_test","closes_rows","harden_linkage","ratifying_owner","depends_on"],"properties":{"target_path":{"type":"string","minLength":1},"class_and_plines":{"type":"string","minLength":1},"mandatory_sections":{"type":"array","minItems":1,"items":{"type":"string"}},"inputs":{"type":"array","minItems":1,"items":{"type":"string"}},"laws":{"type":"array","minItems":1,"items":{"type":"string"}},"evidence_to_capture":{"type":"string","minLength":1},"acceptance_test":{"type":"string","minLength":1},"closes_rows":{"type":"array","minItems":1,"items":{"type":"string"}},"harden_linkage":{"type":"string","minLength":1},"ratifying_owner":{"type":"string","minLength":1},"depends_on":{"type":"array","items":{"type":"string"}}}},
    "decision_ref": {"type":"string"},
    "survey1_ref": {"type":"array","items":{"type":"string","pattern":"^SL-[0-9]{4}$"}},
    "owner": {"type":"string","description":"named role/owner, or [NEEDS DEFINITION] with the DEC that would define it"},
    "phase_found": {"enum":["1","2"]},
    "state": {"enum":["OPEN","DISMISSED-NOT-BLOCKING","ESCALATED"]},
    "dismissal_reason": {"type":"string"},
    "blocker": {"type":"string"}
  },
  "allOf": [
    {"if":{"properties":{"finding_class":{"const":"CONTRADICTION"}}},"then":{"required":["sibling_positions"]}},
    {"if":{"properties":{"executability":{"const":"CLAUDE-CODE-EXECUTABLE-NOW"}},"required":["executability"]},"then":{"required":["build_spec"]}},
    {"if":{"properties":{"executability":{"enum":["EXECUTABLE-AFTER-DECISION","HUMAN-ONLY"]}},"required":["executability"]},"then":{"required":["decision_ref"]}},
    {"if":{"properties":{"finding_class":{"const":"DECISION-PENDING"}}},"then":{"required":["decision_ref"]}},
    {"if":{"properties":{"state":{"const":"DISMISSED-NOT-BLOCKING"}}},"then":{"required":["dismissal_reason"]}},
    {"if":{"properties":{"state":{"const":"ESCALATED"}}},"then":{"required":["blocker"]}}
  ]
}
</queue_schema>

<output_format>
Everything under `11_prompts/runs/{{RUN_DATE}}_survey-2/`:
ORIENTATION.md · PARITY_STANDARD.md · CLASS_CONTRACTS.md · BSQ.schema.json · CHECKSUMS_BEFORE.txt · CHECKSUMS_AFTER.txt · CENSUS.md · census.json · CHAIN.md · census_rows.jsonl · tools/refcheck.py (+ other scripts) · folders/NN_name/ASSESSMENT.md + FIRST_REQUIREMENTS.md + rows.jsonl (×7) · BSQ.jsonl · BUILD_SPEC_QUEUE.md · HALT_LOG.md · OPEN_QUESTIONS.md · PROPOSED_AMENDMENTS.md · CHECKPOINT.md.
BUILD_SPEC_QUEUE.md section order is fixed (Phase 3 step 3 a–h). Every status word is drawn from {PRESENT, ABSENT, APPLIES, DOES-NOT-APPLY, PASS, FAIL, N/A, AT-PARITY, AT-PARITY-WITH-DECISIONS-PENDING, BELOW-PARITY, OPEN, DISMISSED-NOT-BLOCKING, ESCALATED, TOOL-UNAVAILABLE, HUMAN-ONLY}. Numbers are pasted from command output, never recalled. Unknown field → `[NEEDS DEFINITION]` + the DEC that would define it, or `[NEEDS SOURCE]` + the search you ran — never a guess. The two missing-support states are distinct and both have a home: "the repository does not settle this" → DECISION-PENDING or PROPOSED-ADDITION; "this input was not available to me" → TOOL-UNAVAILABLE or a `[NEEDS SOURCE]` field.
</output_format>

<assumptions_and_confidence>
Close BUILD_SPEC_QUEUE.md with two blocks.
**Assumptions** — every interpretive call you made, one line each, with the alternative you rejected and why: which chain links you ruled DOES-NOT-APPLY per folder; which files you treated as load-bearing; which P-lines you marked `[ASSESSOR-PROPOSED]` and would drop if the operator disagrees; how you treated retained-verbatim files; whether SURVEY-1 outputs existed. An assumption that changed a weight names the row.
**Confidence** — for each of the seven folder verdicts and the CHAIN verdict: HIGH / MEDIUM / LOW with one line of reason (proportion of items fully measured vs. shallow-read; TOOL-UNAVAILABLE checks; reliance on `[ASSESSOR-PROPOSED]` P-lines). A LOW confidence beside an AT-PARITY verdict is a contradiction — downgrade the verdict or raise the confidence with evidence. Separately, for the queue as a whole: the count of CLAUDE-CODE-EXECUTABLE-NOW rows whose build_spec you would bet a build session on unchanged, versus those you expect the operator to amend, and why.
</assumptions_and_confidence>
```

---

# 2. Evidence pack

This is a repository-facts task, not a clinical one; the checkable claims are about the tree and about the prompting practice the design relies on. Consensus/PubMed do not apply. Each claim is graded on the evidence available to a reader of this file.

## 2.1 Repository facts baked into the prompt (observed 2026-09-02 via shell on the connected folder; grade: **direct observation — verifiable by re-running the command**)

| Claim in prompt | Command | Result |
|---|---|---|
| 01_–03_ load-bearing files 20–93 KB; 04_–10_ stubs 1.2–4.6 KB | `wc -c` over 01_, 03_/corpus-md, 03_/butterfly-primers, 04_–10_ | MET-1 64,435 · four-faces 93,334 · makoha-in-flight 19,982 · primer_CEC 92,580 · primer_LWC 48,752 · RUN-REPORT 73,803 · programme prompt 27,473 · HARDEN-3 2,558 · DEPLOY-2 1,839 · GOV-1 1,518 · SEC-1 2,205 · REG-R29 md 1,212 · REG-R30 1,308 · HARDEN-2 4,572 |
| Companion chain exists in 02_/03_, absent in 04_–10_ | `ls` of each folder; `ls 11_prompts/` | 02_: primers_briefing.md · 03_: MANIFEST.md, corpus_artifacts_briefing.md, butterfly-primers/ (12 files), programme prompt, artifacts-html/ · 11_: 27 PROMPT-* files, all for 02_ primers (A–L, P0) and 03_ butterfly primers (PRM-*), plus SERIES indexes and SURVEY-1. No briefing/index/primer/prompt/html for any of 04_–10_ |
| Frontmatter gaps in targets | `head -12` + grep of frontmatter keys per file | MT2 directive: no frontmatter · CONTRACT-ARG-1, REG-R29.schema.md, REG-R30: no `version`, no `date` · REPO-MAP_v2: no `version`/`date` · DEPLOY-1/2, OPS-1, GOV-1, SEC-1: no `date` · `req_prefix`/`req_count` only in EXEC-1 (EX/10) and MAK-GOV (NDG/14) |
| Ownership placeholders | grep `NEEDS DEFINITION` in 07_, 10_ | GOV-1 status line; FOLD-1 `owner:` line |
| HARDEN-3 wave coverage of target folders | HARDEN-3 wave table lines 13–24 | W8 = "05_/06_/07_/08_ documents of this repository"; W6 = diagram files by name; W10 = MT2 + HARDEN-1/2/3 + MET set; no wave names 09_ or 10_ by folder; EXEC-1 EX-5 adds 10_ to W11 (per 00_MANIFEST §8) |
| 06_ composition | `find 06_repositories -type f \| sed 's\|.*/\|\|' \| sort \| uniq -c` | 93 files: 53 README.md, 19 MANIFEST.yaml, 12 pipeline.yml, 4 CODEOWNERS, REPO-MAP_v2.md, GPP-CHANNEL.md, CONTRACT-ARG-1.pointer.md, 2 .DS_Store; 19 skeleton directories |
| 09_ composition and parse status | `ls 09_diagrams`; 00_MANIFEST §5 DEF-001 | 4 `.mermaid` + `cdss_diagrams_v2.html`; DEF-001 records 4/4 sources + 4/4 inlined blocks parse @ mermaid 10.9.0 |
| SURVEY-1 not run | `ls -d 11_prompts/runs` | no such directory |
| Class-contract table and CC-1..CC-8 exist to inherit | `grep '^| CC-' 04_hardening/HARDEN-2_hardening_spec.md`; PROMPT-SURVEY-1 §1 | 8 CC rows; SURVEY-1 `<class_contracts>` table of 22 labels |
| 03_ document contract (frontmatter fields; body spine; requirement block; ID census; self-audit) | `corpus_artifacts_briefing.md` Part 1 | Quoted in prompt Phase 0 step 2 Part A list |

## 2.2 Prompting-practice claims the design relies on (grade: **vendor documentation / published guidance**)

| Claim | Where used | Source |
|---|---|---|
| XML-tagged sections improve instruction following and reduce cross-talk between context and instructions | whole prompt | Anthropic docs — "Use XML tags to structure your prompts" |
| Stating the rationale beside a rule improves generalisation to unlisted cases | "say why" in laws 5, 7; what_a_wrong_answer_costs | Anthropic docs — "Be clear, direct, and detailed"; skill Step 2 item 2 |
| A place to register doubt (assumptions/confidence field) raises the quality of the primary content | assumptions_and_confidence block | skill Step 2 item 9; Anthropic docs — "Reduce hallucinations: give Claude permission to say it doesn't know" |
| Precise output contract with a defined value for unknown fields reduces fabricated fills | output_format; BSQ schema; two missing-support states | Anthropic docs — "Increase output consistency"; skill Step 3 ("two distinct states for missing support") |
| Long-horizon multi-file tasks benefit from on-disk checkpoints and explicit resume rules | CHECKPOINT.md; stop-between-folders | Anthropic Claude Code best practices (context management; write progress to files) |
| Sub-agent fan-out with orchestrator-side validation rather than summarisation preserves coverage | Phase 2 fan-out rule | Anthropic — "Building effective agents" (orchestrator-workers; verify outputs mechanically) |
| Anti-rationalization text works when it names the specific shortcut, not the abstract vice | law 7 named shortcuts | MT2 §4 (in-repo, house evidence); skill design note from PROMPT-SURVEY-1 |

## 2.3 Gaps in this evidence pack (reported, not hidden)

- The parity standard itself is deliberately *not* fixed in this prompt — it is derived at run time from 01_–03_ so it carries file-level evidence. The cost is that two runs could derive slightly different P-line sets. Mitigation: Part A/B minimum lists in Phase 0 step 2 are the floor, and every P-line must cite ≥2 reference files.
- Applicability of ARTIFACT-HTML and PRIMER links to 04_–10_ is a judgement call; the prompt forces it to be stated and marked `[ASSESSOR-PROPOSED]`, but there is no in-repo law settling it. Candidate ratifier: the 00_MANIFEST owner via A-003, or a new DEC.
- No prior run of SURVEY-1 or SURVEY-2 exists, so there is no measured baseline for how many rows or how much context a full run consumes. The stop-between-folders rule is the safeguard.

---

# 3. Open questions

1. `{{RUN_DATE}}` — the run-directory date stamp (ISO, e.g. `2026-09-03`).
2. Should the executor run SURVEY-1 first, or is SURVEY-2 intended to stand alone? The prompt is written to stand alone and to *reuse* SURVEY-1 outputs if they exist (law 10). If you want SURVEY-1 executed first, say so; the prompt does not need to change.
3. Do you want ARTIFACT-HTML twins treated as a *requirement* for any 04_–10_ documents (REG-POSTURE, MAK-GOV, DEPLOY-1 are the natural candidates) or only as a PROPOSED-ADDITION? The prompt currently leaves it to the executor's applicability test, marked `[ASSESSOR-PROPOSED]`.
4. The filed scope is 04_–10_. `11_prompts/` (27 files, no manifest row, no HARDEN wave) and the root loose file `AI Evaluator Architecture.md` are out of scope here and were in scope for SURVEY-1. Confirm that exclusion is intended.
5. Who is the operator receiving the hand-back — the MT2 operator, the manifest owner, or you? The queue's ratifying-owner field will name roles from GOV-1/REPO-MAP; person-level owners remain `[NEEDS DEFINITION]` (DEC-09/DEC-10) unless supplied.
6. Fan-out budget: one sub-agent per target folder (seven) is permitted in Phase 2. If the run is single-context, delete the fan-out sentence; nothing else changes.

---

# 4. Eval pack

Format lifts into promptfoo as one test per row; the "checkable in under a minute" criterion is a grep or a file-exists check on the run directory.

| # | Case | Input / setup | Pass criteria | Expected failure mode if the prompt is weak |
|---|---|---|---|---|
| E1 | Happy path, small folder | 08_research (1 file) | `folders/08_research/` has all three files; ≥1 row per applicable chain link (briefing, index, HARDEN row, HARDEN task, launch prompt) each PRESENT or ABSENT with a search; RESEARCH-1 measured against RESEARCH contract lines with quotes; FIRST_REQUIREMENTS ordered by weight | Executor writes prose about the file being "thin" with no P-line cited |
| E2 | No-sampling law | 06_repositories (93 files) | rows.jsonl ≥ 91 artifact_paths (93 − 2 .DS_Store); every skeleton tree has README/MANIFEST/pipeline presence rows; REPO-MAP 19 rows ↔ 19 trees reconciled both ways | "Skeletons are uniform; sampled 5" — must appear in HALT_LOG if tempted, and full census still done |
| E3 | Retained-verbatim guard | 04_hardening MT2 directive (no frontmatter, retained) | No build item proposes editing MT2; any frontmatter/index gap is remedied via a folder INDEX row or companion; row cites law 5 | Build spec says "add frontmatter to MAJOR_TASK_2…" |
| E4 | Decision-gated item | 05_ REG-R29 (opens on DEC-02) — a "register not opened" finding | Row is DECISION-PENDING or EXECUTABLE-AFTER-DECISION with `decision_ref` = DEC-02; not CLAUDE-CODE-EXECUTABLE-NOW; appears in hand-back if weight 5 | Executor specs "open R29 and write row 0" as a build item |
| E5 | Non-markdown class | 09_diagrams (4 .mermaid + 1 .html) | Frontmatter P-lines judged N/A-with-reason (header comment used instead); mermaid parse re-run with tool+version pasted; DIAGRAM contract (nodes agree with Arch §10/§11, REPO-MAP) measured or ESCALATED with reason; folder chain (index, HARDEN task naming 09_) assessed | Executor applies YAML-frontmatter FAIL rows to .mermaid files |
| E6 | Length is not parity | 07_ GOV-1 (1,518 B, owners [NEEDS DEFINITION]) | Findings cite P-lines (owner named; placeholders registered in MET-2/MET-4) and UNDEFINED-OWNER with DEC-09/DEC-10; no row whose statement is "too short"; any length remark lands in §e dismissals | Build spec: "expand GOV-1 to ~20 KB" |
| E7 | Adversarial: superseded reading | 10_ REG-SPRINT v1.0 timing cited without 1.1 delta | Any row citing REG-SPRINT timing quotes the 1.1 position; a v1.0-only citation is itself flagged as a defect per law 3 | Row cites v1.0 sprint dates as current |
| E8 | Context exhaustion | Simulate stop after 06_ | CHECKPOINT.md lists 04, 05, 06 only; no partial `folders/07_*`; resume instruction present in ORIENTATION or CHECKPOINT | Partial 07_ files with no checkpoint line |
| E9 | Append-only integrity | Any full run | CHECKSUMS_AFTER vs BEFORE diff = ∅ outside `11_prompts/runs/…_survey-2/`; pasted at top of BUILD_SPEC_QUEUE.md | Executor "fixes" a frontmatter field in place |
| E10 | Schema discipline | Any full run | `BSQ.jsonl` 100% validates; every CLAUDE-CODE-EXECUTABLE-NOW row has all 11 build_spec fields non-empty; every EXECUTABLE-AFTER-DECISION / HUMAN-ONLY row has `decision_ref` | Rows with `build_spec` prose in `statement` instead of the object |

**Rubric weights** (for a scorer): E9 and E10 are gates — fail either and the run fails regardless of the rest. E2, E3, E4, E6 are the four ways this prompt can be *wrong in a way the operator would act on*; each is worth 2 points. E1, E5, E7, E8 are worth 1 point each. Pass ≥ 10/12 with both gates clear.

---

# 5. Design notes

- **The standard is derived, not dictated.** The draft's one rule pointed at 01_–03_ as the bar but did not say what the bar was. Hard-coding my own reading of it into the prompt would have made the prompt the authority instead of the repository. Instead Phase 0 forces the executor to write `PARITY_STANDARD.md` with two reference-file citations per line; the Part A/B minimum lists exist only so a weak run cannot derive an empty standard. If the evals show P-line drift between runs, freeze Part A into a versioned file under 05_ (a proposed `CONTRACT-DOC-1`) and cite it — that is the first change to make.
- **Length is explicitly disarmed.** The visible gap between folders is 20–60× in byte count, and an executor asked to "bring it up to the same level" will chase that number. `the_one_rule`, the weighting section (`parity_gap` is a tie-break, not an addend) and eval E6 all close that route. The build items that come out should be *companions with contracts* (index, briefing, primer, prompt, delta) — the way 02_ and 03_ actually reach their level.
- **One filed item I disagree with, stated once.** The draft names the third duty "final-pass modifier". In this repository "modify" collides with the append-only law, and the draft's own text says the office recommends and never decides. I built it as "final-pass recommender" and kept every other word of the role. If you want the original title, change one word in `<role>`; nothing downstream depends on it.
- **Build-Spec Queue over survey ledger.** SURVEY-1's deliverable is a verdict plus remedy prompts; this run's deliverable is the queue itself, so the row schema carries a typed `build_spec` object with eleven mandatory fields and a schema `if/then` that makes an executable row without a spec invalid. That is what lets the *next* session pick up row BSQ-0007 and build it with no other context — the MT2 §5 naive-executor test turned on the prompt's own output.
- **What to change first if evals fail.** E2/E9/E10 failures → the prompt is fine, the executor needs the fan-out removed or the folder order split across sessions. E3/E4/E6 failures → strengthen laws 4–5 with a worked negative example inside `<build_spec_queue>` (one malformed spec shown and corrected). E1/E5 failures → the applicability tests in Part B need to be pre-written for 08_ and 09_ rather than left to the executor.
