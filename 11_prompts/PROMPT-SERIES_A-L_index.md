---
doc_id: PROMPT-SERIES
title: "PROMPT series A–L — index, shared laws, run order, and cross-run dependencies"
version: "1.0"
date: "2026-09-02"
status: "Proposed. Produced by the arepo-metaprompt skill (GENERATE mode ×12). Adds files under 11_prompts/ only; edits nothing in 00_–10_."
---

# What this is
Twelve Claude Code launch prompts, one per component primer (A–L), each written by the same house workflow used for PROMPT-P0: lever → prompt → evidence pack → open questions → eval pack → design notes. Each prompt executes *that primer's own imperatives* — its §-9 work-register seed (TASK-X-001…), its RECON register, its §-8 execution-layer contracts and its §-10/§-11 annex execution fields — inside the corresponding `06_repositories/repo-skeletons/cdss-*` skeleton, as **new files only**, against **synthetic material only**, and stops exactly where the primer's own HALT triggers say to stop.

# Shared laws (every prompt inherits PROMPT-P0 §1 laws 1–7)
Append-only with sha256 bookends and a mandatory empty diff · EXEC-1 precedence for sequencing, corpus/REG-POSTURE for content · delta-reading (REG-SPRINT via 1.1, MET-1 via 1.1, MET-2 via 2.1, R30 via 30.1) · OPEN means OPEN (no ASSUME closes; J-3 pending DEC-06; posture labels Needs confirmation pending ASSUME-REG-002) · HARDEN-3 W0 precedes hardening — these runs are *build* work under EXEC-1 D-1/MET-4 P0 ("L1 on synthetic scope"), not hardening, and they do not touch R29 · no patient data, licensed text by reference · no silent shortcuts (temptations go in HALT_LOG.md).

Every run writes to `11_prompts/runs/{{RUN_DATE}}_primer-<X>/`, proposes register rows (never writes registers), and proposes the `00_MANIFEST.md` §4.4 honesty-line amendment ("no code beyond skeleton READMEs") — never edits the manifest.

# The twelve, with the one-line imperative each executes
| Prompt | Component / repo | Level | Executes | Primary HALT it enforces |
|---|---|---|---|---|
| PROMPT-A | Bayesian engine / `cdss-engine` | L1 | TASK-A-001 LR updater + TASK-A-002 `/v1/differential`; A8 properties; byte-identical replay | CHAIN-BREAK on authoring a clinical number (float-literal grep) |
| PROMPT-B | Evidence library / `cdss-library` | L1 | TASK-B-001 validator (10 invariants) + G rows 1–5, 16–17 as merge-blocking CI | CHAIN-BREAK on restating a value; DOR-FAIL on uncarded LLM row → `rows_authored: 0` |
| PROMPT-C | Casebundle corpus / `cdss-corpus` (dev-side) | L1 | TASK-C-001 loader-refusal library + sev-1 alarm, synthetic EVAL fixture only | SPEC-CONFLICT on any EVAL credential dev-side (Phase 0 self-check) |
| PROMPT-D | Content registry / `cdss-registry` | L2 | TASK-D-001 five-gate chain + R11 decision log; 100% catch on G rows 6–12 | SPEC-CONFLICT on a model in the gate path |
| PROMPT-E | Graph RAG / `cdss-graph` | L3 v0 | TASK-E-001 deterministic build + unanchored-edge failure; worked traversals 1–2; rebuttal/DetectedIssue shapes | DOR-FAIL on an edge without asserting fragment |
| PROMPT-F | Conformal wrapper / `cdss-conformal` | L3 | TASK-F-001 nonconformity (a) + Mondrian strata on DDXPlus; R15 ledger; guarantee statement | ASSUMPTION-REFUTED on training with a calibration slice (ledger-role refusal) |
| PROMPT-G | Corruption engine / `cdss-corruption` | L1 v0 | TASK-G-001 seeded generator + certifier + per-gate catch report, rows 1–18 | SPEC-CONFLICT on admitting an uncertified label; rows never invented |
| PROMPT-H | Lumos pathway / `cdss-lumos` | L4 (Stage 1) | TASK-H-001 as *candidates* (quoted values, cited); protocol/SAP skeletons; H10 status | SPEC-CONFLICT on any training route; no library row written |
| PROMPT-I | Living evaluation / `cdss-evalstack` | L1→L3 | TASK-I-001 binding table as config + unmapped-class hard fail; R7 seed; R20 schema | CHAIN-BREAK on weakening a ★ property without sign-off |
| PROMPT-J | Model governance / `cdss-governance` | L2→L4 | TASK-J-001 admissibility validator (constructed violations) + TASK-J-002 posture-neutral census | CHAIN-BREAK on presupposing J-1/J-2; SPEC-CONFLICT on NC in training |
| PROMPT-K | LLM lattice / `cdss-llm-lattice` | L4 | Prompt registry + card schema + injection fixtures 23–25 (dormant) + K3.2 scaffold with stub proposer; **0 LLM calls** (DEC-03 open) | SPEC-CONFLICT on any path to an encounter |
| PROMPT-L | Runtime LLM / (none built) | L5 | RECON-L-001 ruling → **HALT: DOR-FAIL**; posture-neutral prep filed to A, G, I, J | DOR-FAIL until R19 holds a decision written by its owners |

# Recommended run order and cross-run dependencies
Run **PROMPT-P0** first (row zero evidence, checksum baseline, P0 board). Then, respecting the build order Arch §11 implies and the sibling artefacts each prompt consumes:

1. **A, B, G, C** (L1 silos; independent) — G attacks A's override layer and B's validator once they exist, and reuses C's refusal library for its EVAL guard.
2. **I** (operates A's properties, B's validator, G's suites; does not re-implement).
3. **D** (L2) — then **E** (L3 v0), which should consume D's synthetic fragment slice so the two silos stay coherent.
4. **F** (L3) — DDXPlus proof; provides the `conformal_set` fixture shape A consumes at L3.
5. **J** (creates R4/R5 seeds and an *empty* R19) — then **K** (cards need J census rows; 0 model calls until DEC-03) — then **H** (its extraction is a K2.9-class assist and should carry a prompt-card ref; without one it files K-RUN-FINDING).
6. **L** last — its ruling reads the R19 J created (empty) and halts correctly.

Each prompt tolerates missing siblings: absent stacks become FINDINGS (G), substitutions are recorded in RECON files, and nothing fakes a dependency.

# Evidence pack — series-level findings worth the operator's eye
- **Two literature findings surfaced (PubMed, 2026-09-02):** (i) the only indexed Lumos paper (Correll et al. 2021, [DOI](https://doi.org/10.1136/ihj-2021-000074)) reports 1.3M patients / 16% of NSW, not Primer H1's "6.8M+"; the "2025 data-quality cohort study" was not located in PubMed — PROMPT-H must source both or mark NOT-LOCATED. (ii) Conformal prediction's coverage guarantee is well supported in recent clinical applications (e.g., Cina et al. 2026, [DOI](https://doi.org/10.1038/s41598-026-35343-6)), but **no CP study in primary-care differential diagnosis was found** — a gap that strengthens the case for H's Stage 3 rather than weakening F.
- **Repository findings:** G9 cites "rows 1–30" but only 18 rows are specified (23–25 in K8; 26–30 named in L3 only) — no prompt invents the rest. The D8 Rego skeleton cannot catch G8 row 7 (unit swap) or rows 9–10 as written — PROMPT-D extends the policy and files the extension as Proposed. Every §-9 DoR that presupposes a spine tag, a library release, or a ratified schema is unmet in this repository — every prompt substitutes and records rather than waits, per EXEC-1 D-1.
- **Self-reference:** the executors are LLMs. PROMPT-B therefore enforces `rows_authored: 0`; PROMPT-H and PROMPT-K stamp `assisted_by` and ask for a prompt-card ref for the builder itself (K-RUN-FINDING-001 if absent).

# Open questions common to the series
1. `{{RUN_DATE}}` and the scratch location for datasets outside the repo (F).
2. Language/runtime per skeleton (`ci/pipeline.yml` decides; default Python 3.12 + pytest).
3. Whether `11_prompts/` should be indexed as `00_MANIFEST.md` amendment A-003 (manifest owner's call).
4. Component owners (`[NEEDS DEFINITION]` throughout) — who ratifies each run's proposed R1/R25 rows.
5. DEC-03 (inference substrate) — prerequisite for any real proposer in K, and for L after posture.

# Eval — series gate
A run in this series passes only if: preservation diff is empty; every status uses the enum {DONE-WITH-EVIDENCE, IN-PROGRESS, BLOCKED(reason), ESCALATED(owner), HUMAN-ONLY, NOT-IN-SCOPE}; the component's HALT counter is zero or explained; no clinical number, row, fragment, case, or dialogue text was authored by the executor; and no ASSUME, DEC, or posture was closed or presupposed.
