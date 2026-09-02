# CLASS_CONTRACTS — floor + Part A extensions

Run: 2026-09-02_survey-2 · Phase 0 step 3. Section 1 is the `<class_contracts>` table of `11_prompts/PROMPT-SURVEY-1_ecosystem_repleteness_surveyor.md` copied verbatim (extracted by `awk '/<class_contracts>/,/<\/class_contracts>/'` on 2026-09-02). Section 2 appends the two additions PROMPT-SURVEY-2 makes and the Part A lines that apply per class. Unsourced lines are marked `[ASSESSOR-PROPOSED]`.

## 1. Floor — inherited verbatim from PROMPT-SURVEY-1

Floor contracts — extend in Phase 0 step 2 with sourced lines; every line here already cites its source. "Must carry" means a FAIL row if absent.
| Label | Members (by example) | Must carry | Source |
|---|---|---|---|
| MANIFEST / INVENTORY | 00_MANIFEST.md, 00_inventory.txt, 03_/MANIFEST.md, 06_ MANIFEST.yaml | every file on disk in scope listed; counts equal disk; amendments appended not edited; honesty lines current against the tree | 00_MANIFEST §1, §4, §7–8; MT2 §3 |
| DIRECTIVE | MT2, EXEC-1 | the eight hardening properties applied to itself (triggers, deterministic steps, exit+evidence, failure handling, anti-rationalization, xrefs resolve, boundaries, safety closure); precedence statement; RFC 2119 where normative | MT2 §1, §7(5); EXEC-1 frontmatter |
| SPEC | HARDEN-2 | class bar per member class; mechanical checks named per class; universal exit bar; stop-the-line instantiated | HARDEN-2; MT2 §2.2 Define row |
| WORKLIST / PLAN | HARDEN-3, FOLD-1, REG-SPRINT (via 1.1), MET-4 roadmap | one task per in-scope artifact; dependency order stated with reason; every in-scope artifact on disk has a task (incl. 10_, 11_, 03_/butterfly-primers); every task names class, skills, exit | HARDEN-3 header; MT2 §3; EXEC-1 EX-5 |
| SEED / LEDGER | HARDEN-1, R30 seed | every row's artifact path resolves on disk; every in-scope artifact has a row; states drawn only from the schema enum; terminal-state law stated; amendments appended | HARDEN-1 header + A-001; R29 schema `state` enum |
| SCHEMA | REG-R29.schema.json, REG-R30 schema | valid JSON Schema (draft stated); at least one example instance validates; `$id` resolves to a repo path that exists or is a declared skeleton; md twin agrees with json field-for-field; ≥1 consumer names it | HARDEN-2 CC-7; Arch §12.1 register laws |
| REGISTER | R29, R30 (proposed), Arch §12.2 table | schema + seed + owner + mutability declared + join key present + opening level named | Arch §12.1(1)–(4), §12.3 |
| CONTRACT | CONTRACT-ARG-1 (+DEV-1, RRI-1) | fields, consumers, breaking-change rule, pointer stub in cdss-spine skeleton pointing to the canonical draft; HARDEN-1 row | HARDEN-2 CC-7; REPO-MAP skeleton index ("move-never-copy") |
| PRIMER (02_) | Primer 0, A–L, variants, harness, annex | §-8 execution contracts; §-9 work-register seed (TASK-X-001…); §-10/§-11 annex with the ten execution fields non-empty (Primer 0 charter-exempt); matching PROMPT in 11_; matching skeleton in 06_; HARDEN-1 row; original byte-exact prefix preserved | 00_MANIFEST §4.2; HARDEN-2 CC-1; PROMPT-SERIES |
| CORPUS VOLUME (03_) | 15 corpus-md files | frontmatter fields per briefing Part 1 (doc_id, req_prefixes, req_count, status, normative_language, subordinate_to, lineage, governed_by, changelog, change_policy); body spine (Contents → Thesis → Part 0 → … → traceability → ID census → self-audit); ID census equals req_count; artifacts-html twin; listed in 03_ MANIFEST; HARDEN-1 row | corpus_artifacts_briefing Part 1; 03_ MANIFEST; HARDEN-2 CC-3 |
| BUTTERFLY PRIMER (03_/butterfly-primers) | PRM-LWC … PRM-ANT, RUN-REPORT | Appendix A declared = mapped; X5/X8/X9/X10 present; listed in *some* manifest; HARDEN-1 row or a finding that none exists; RUN-REPORT byte counts equal disk | RUN-REPORT §1; 00_MANIFEST §4.1 (03_ "zero edits") |
| PROMPT (11_) | PROMPT-P0, PRM0, A–L, SERIES index | role/context/laws/phases/output contract/eval pack; every path it names exists; run-directory convention; inherits PROMPT-P0 laws 1–7; indexed in PROMPT-SERIES or a finding | PROMPT-SERIES header + eval gate |
| REPO SKELETON (06_) | 19 skeleton trees, 93 files | README + MANIFEST.yaml + ci/pipeline.yml with dormant R29 ratchet hook; CODEOWNERS where the primer mandates it (registry, library, compiler bundles, spine contracts); per-directory stubs mirroring primer §-4/§-8; every REPO-MAP row has a tree and vice versa; cdss-corpus minimal with firewall banner | REPO-MAP skeleton index; HARDEN-1 A-001 |
| DIAGRAM | 4 .mermaid, cdss_diagrams(_v2).html | parses; nodes/edges agree with Arch §10/§11 and REPO-MAP; successor/regeneration notice present where derived | HARDEN-2 CC-6; MET-4 G-10 |
| ARTIFACT-HTML (03_) | 16 pages | twin of a corpus-md volume or a declared dossier; listed in 03_ MANIFEST; renders (CC-6) | 03_ MANIFEST; HARDEN-2 CC-6 |
| DEPLOY / OPS / GOV / SEC | 07_ five files | every step has gate + status; rollback stated; RTO/RPO/DR defined or registered as [NEEDS DEFINITION] with owner; every OPS procedure step carries timeout/retry/idempotency/on-fail; owners named per role; SEC covers secrets, access, encryption, SBOM, vuln handling, supplier assessment, incident/CAPA | DEPLOY-1; Arch §13.6 via HARDEN-2 CC-5; DEPLOY-1 TASK-REG-010..014 |
| REGULATORY (10_) | REG-POSTURE, REG-NZ, MAK-GOV, REG-SPRINT(+1.1), EXEC-1, FOLD-1 | every OPEN item names attesting party and blocked gate; no ASSUME closed internally; WATCH cadences; delta-reading declared; canonical-vs-annex divergence listed, dated, owned | HARDEN-2 CC-4; EXEC-1 EX-2, EX-3, EX-7 |
| DELTA | MET-1.1, MET-2.1, R30.1, REG-SPRINT-1.1 | names its base and version; enumerates amendments D-n; base declares it is read only through the delta (or a finding) | EXEC-1 EX-2; PROMPT-P0 law 3 |
| RESEARCH | RESEARCH-1 | supplied vs newly-verified vs gaps vs proposed; fetch dates; no fabricated findings | RESEARCH-1 §1–4 |
| GAP / DECISION REGISTER | MET-2, MET-4 | both positions quoted; ruling state; owner; blocking gate; every ESCALATED item appears in the consolidated blocker list | MET-2 rule line; MT2 §6, §7(2) |
| ROOT LOOSE FILE | AI Evaluator Architecture.md | indexed somewhere, or a finding (class UNINDEXED-ROOT-FILE); does not contradict a governing doc | 00_MANIFEST §1 (nothing indexes root files) |

## 2. Extensions (this run)

### 2.1 Additions from PROMPT-SURVEY-2 `<class_contracts>` (sourced)
| Label | Must additionally carry | Source |
|---|---|---|
| Any target file that mints IDs | `req_prefix` + `req_count` in frontmatter; ID census section equal to count; retired IDs never reused | corpus briefing Part 1 (frontmatter table; `change_policy`); EXEC-1 and MAK-GOV already conform |
| Any target folder | an index of its own files (role · status · bytes · disposition · HARDEN row · HARDEN task) or a finding ABSENT-ITEM at folder level; a briefing or a finding | 02_ `primers_briefing.md`; 03_ `MANIFEST.md` + `corpus_artifacts_briefing.md`; 00_MANIFEST §3 — folder-level lines are `[ASSESSOR-PROPOSED]` until DEC ratifies |

### 2.2 Part A lines applied per class (P-IDs from PARITY_STANDARD.md; each P-line carries its own source there)
| Label | Applicable P-D lines | Notes |
|---|---|---|
| DIRECTIVE (MT2, EXEC-1) | 01,02,03,04,05,06,07,08,09,12,14,15,16 | MT2 is retained-verbatim → judged via companion/index (law 5); EXEC-1 is the in-target exemplar |
| SPEC (HARDEN-2) | 01,02,04,05,07,08,09,10,12,15,16 | class-bar rows CC-1..8 mint IDs → P-D-04/08 apply |
| WORKLIST / PLAN (HARDEN-3, FOLD-1, REG-SPRINT+1.1, MET-4) | 01,02,03,04,07,08,09,10,11,12,14,15,16 | T-/W- IDs minted → census; owner per task (P-D-14) |
| SEED / LEDGER (HARDEN-1, R30 seed, R30.1) | 01,02,04,08,09,10,12,13,14,16 | row IDs minted; terminal-state enum (P-D-10) |
| SCHEMA (REG-R29.schema.json, .schema.md, R30 schema) | 01,02,04,09,12,14,16 | P-D-09 = recorded validation run (CC-7); `.json` judged on `$id`/`title` in lieu of frontmatter |
| REGISTER (R29, R30) | 01,02,03,04,08,09,10,12,14,16 | Arch §12.1 laws (owner, mutability, opening level, join key) from the floor |
| CONTRACT (CONTRACT-ARG-1 +DEV-1/RRI-1) | 01,02,04,05,07,09,12,14,16 | fields → requirement-block form or a field table with source per row (P-D-05) |
| REPO SKELETON (06_, 93 files) | 01(banner in lieu),02,12,14,16 | README banner = frontmatter analogue; MANIFEST.yaml/pipeline.yml judged on P-D-15 |
| DIAGRAM (09_) | 01(header comment),02,07,13,16 | `.mermaid` header comment carries status + successor note; P-D-08 N/A |
| DEPLOY / OPS / GOV / SEC (07_) | 01,02,03,04,05,07,09,10,12,14,15,16 | steps/gates mint IDs (TASK-REG cited; DEPLOY steps) → P-D-04/08 where they mint |
| REGULATORY (10_) | 01,02,03,04,05,06,07,08,09,10,11,12,14,15,16 | REG-POSTURE/REG-NZ/REG-SPRINT carry `authority: ADVISORY_ONLY` (P-D-03 ✓ pattern) |
| DELTA (R30.1, REG-SPRINT-1.1) | 01,02,03,11,12,13,16 | P-D-11 is the defining line |
| RESEARCH (RESEARCH-1) | 01,02,04,07,09,12,16 | RG- IDs minted → census |
| GAP / DECISION REGISTER | 01,02,04,08,10,12,14,16 | reference-folder class (01_); cited when 04_–10_ rows point at DEC/G |
