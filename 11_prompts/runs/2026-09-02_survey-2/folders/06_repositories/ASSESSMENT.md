# 06_repositories — ASSESSMENT (Phase 2)

Census: 91 files, 48,662 B (REPO-MAP_v2.md + 90 skeleton files in 19 trees). Per-file mechanical pass: `tools/skeleton_check.py` → `skeleton_rows.jsonl` (90 rows, one per file — no sampling, law 7) + `skeleton_summary.json`.

## 1. Discovery and labels
| Item | Bytes | Label(s) | Why | Load-bearing? |
|---|---|---|---|---|
| `REPO-MAP_v2.md` | 4,322 | INDEX (repo map) + WORKLIST-adjacent (skeleton index paragraph) | "Repository map — 14 existing + 4 proposed + 1 channel"; Arch §10 mirror | YES — crit 2 (every PROMPT-A..L targets a tree it names; Arch §14.2 amends via it) |
| 19 trees / 90 files: 19 `README.md` (root), 34 per-directory `README.md`, 19 `MANIFEST.yaml`, 12 `ci/pipeline.yml`, 4 `CODEOWNERS`, `GPP-CHANNEL.md`, `CONTRACT-ARG-1.pointer.md` | 44,340 | REPO SKELETON (CC-5 for READMEs/MANIFEST/CI per HARDEN-1 A-001; CC-2 for CODEOWNERS/pointer) | HARDEN-1 A-001 class ruling | crit 1 each (load-bearing for the folder; instantiation targets), except `cdss-spine/*` and `GPP-CHANNEL.md` crit 2 (contracts home; GPP-14 boundary) |

Counts by name: `find 06_repositories -type f ! -name .DS_Store | sed 's|.*/||' | sort | uniq -c` → 53 README.md · 19 MANIFEST.yaml · 12 pipeline.yml · 4 CODEOWNERS · 1 REPO-MAP_v2.md · 1 GPP-CHANNEL.md · 1 CONTRACT-ARG-1.pointer.md = 91.

## 2. Presence pass — folder chain
| Link | Applicability | PRESENT / ABSENT | Evidence |
|---|---|---|---|
| P-F-01 BRIEFING | APPLIES (what a skeleton is; how trees relate to primers, contracts and the lockfile) | PARTIAL — REPO-MAP "Skeleton index (appended)" paragraph explains the doctrine in one paragraph | REPO-MAP l.30 |
| P-F-02 INDEX | APPLIES | PARTIAL — REPO-MAP indexes 19 repos (rows) with primer/emits/isolation/status; **no per-file index** (90 files: role, bytes, banner, HARDEN row) | REPO-MAP table 19 rows; `skeleton_summary.json` is this run's substitute |
| P-F-03 corpus-grade | APPLIES to REPO-MAP; skeleton files judged on floor | §3–4 | — |
| P-F-04 PRIMER | DOES-NOT-APPLY (skeletons are primer *outputs*) — but every tree must have an owning primer: **cdss-compiler has none** (02_ has no compiler primer; 03_/butterfly-primers has none; EN-3 is a MAK-FFC requirement, not a primer) | ABSENT for cdss-compiler | `grep -c compiler 02_cdss-stack-augmented/primers_briefing.md` → 0; `ls 11_prompts | grep -i compiler` → none; RUN-REPORT names `cdss-compiler` only as a consumer path |
| P-F-05 LAUNCH PROMPT | APPLIES (small): skeleton-conformance / REPO-MAP↔tree reconciliation is a repeatable check | ABSENT — this run's `tools/skeleton_check.py` is the first such check | `ls 11_prompts | grep -i 'skel\|repo'` → none |
| P-F-06 ARTIFACT-HTML | DOES-NOT-APPLY | — | — |
| P-F-07 SKELETON home | IS the skeleton layer | — | — |
| P-F-08 HARDEN rows/tasks | APPLIES | PARTIAL-by-design — HARDEN-1 A-001 defers 06_ rows to "path glob at pass time" (one row per file); HARDEN-3 T-100..107 collapsed (W8) | HARDEN-1 l.35; HARDEN-3 l.21 |
| P-F-09 00_MANIFEST row | APPLIES | PRESENT — A-001 "91" = disk 91 | CENSUS §1 |
| P-F-10 honesty line | APPLIES | PRESENT — REPO-MAP status + skeleton index "every file marked Proposed, no code claimed"; **but 13 files carry no Proposed/skeleton/stub marker anywhere** → contradiction with 00_MANIFEST §7 "all skeleton files carry Proposed/skeleton banners" (BSQ-0393) | skeleton_check: 13 findings |

## 3. Presence pass — document contract (REPO-MAP_v2.md)
P-D-01: doc_id, title, status PRESENT; **version, date ABSENT** · P-D-02 PRESENT ("Existing rows Retained verbatim in intent from Arch §10; new rows Proposed (DEC-09)…") · P-D-03 PRESENT (Arch §10 mirror; DEC-09) · P-D-04 N/A (mints no IDs; names repos) · P-D-05 PARTIAL (table rows carry Status, not source) · P-D-07 PRESENT (Arch §10/§14.2; C-04; LS-2/3/4) · P-D-08 census: N/A but **declared "14 existing + 4 proposed + 1 channel" = 19 trees on disk ✓** · P-D-09 self-audit ABSENT · P-D-10 rows carry Status ✓, **owner ABSENT** (DEC-09) · P-D-12 none · P-D-13 skeleton index "appended" ✓ · P-D-14 owner ABSENT · P-D-16: `GPP-CHANNEL.md` cited by basename only (refcheck) — resolves to `repo-skeletons/cdss-integration/GPP-CHANNEL.md`.

## 4. Measurement pass
| Contract line | PASS/FAIL | Evidence |
|---|---|---|
| REPO SKELETON: README + MANIFEST.yaml + ci/pipeline.yml with dormant R29 ratchet hook | PARTIAL — README 19/19, MANIFEST 19/19 (all parse; keys name/status present; name == tree), CI stub **12/19**; of the 14 existing repos, CI stubs exist in 8 (coder, conformal, corruption, engine, graph, library, registry, spine) — **missing in evalstack, governance, harness, llm-lattice, lumos** (corpus intentionally minimal); all 12 CI stubs carry the r29-ratchet line and "not runnable" | skeleton_summary.json `has_ci`; `grep -l r29 06_repositories/repo-skeletons/*/ci/pipeline.yml | wc -l` → 12 |
| REPO-MAP skeleton index claim "all 14 existing repos (README + MANIFEST.yaml stub + CI stub + per-directory stubs…)" | **CONTRADICTION** with tree (5 existing repos lack CI stub; 8 of 14 have no per-directory stubs — coder, conformal, corpus, governance, harness, llm-lattice, lumos have root files only) | REPO-MAP l.30 vs `find` |
| CODEOWNERS where the primer mandates (registry, library, compiler bundles, spine contracts) | PASS 4/4; each carries `[NEEDS DEFINITION]` person markers (registered under DEC-09) | files |
| every REPO-MAP row has a tree and vice versa | PASS 19 ↔ 19 (14 existing + 4 proposed + cdss-integration; GPP channel = file inside cdss-integration, not a tree — consistent with REPO-MAP "channel, not repo") | REPO-MAP rows vs `ls repo-skeletons` |
| cdss-corpus minimal with firewall banner | PASS | `head -3 cdss-corpus/README.md` (see skeleton_rows evidence) |
| per-directory README states what its owning primer/annex requires | PASS after manual review — regex flagged 7, all cite MAK/primer IDs (K, PI-1/2, PA-1, CC-1, EN-3 text); the 4 `cdss-compiler` sub-dirs cite EN-3/K/ELSM because no compiler primer exists (see P-F-04) | manual read of the 7 |
| every file marked Proposed/skeleton | **FAIL 13/90** — no such marker anywhere in: cdss-integration/lockfile/README.md · cdss-engine/tests, properties · cdss-library/validator, rows · cdss-spine/tolerances, validator, registers, templates · cdss-compiler/CODEOWNERS · cdss-registry/CODEOWNERS, policy/README.md · cdss-graph/tests/README.md | `grep -L -i 'skeleton\|proposed\|stub\|pointer'` |
| REPO-MAP ↔ butterfly-primer programme proposals | **DECISION-PENDING** — RUN-REPORT R6 proposes `cdss-fuzzy`, `cdss-meta`, `cdss-ui-auditor`, `cdss-infra`, `cdss-dataplane` + PFX additions {FUZ, MRL, CEC, CMP, ABC, LEG, ANT}; REPO-MAP v2 (2026-09-01) predates and lists none; DEC-09 owns new repos/prefixes | RUN-REPORT l.256–258 |
| status honest against the tree | PASS — no code anywhere (`find 06_repositories -name '*.py' -o -name '*.ts' -o -name '*.java'` → none) | — |

## 5. Chain confirmation
CHAIN.md §A 06_ confirmed; corrections: 91 (not 93) files; CI stub coverage 12/19; cdss-compiler has no owning primer anywhere in 02_/03_/11_.

## 6. Weighting summary
Queue (≥3): BSQ-0390 INDEX-06 (per-file index incl. banner/CI gaps), BSQ-0391 cdss-compiler primer gap, BSQ-0394 REPO-MAP v3 reconciliation (after DEC-09). Low: 13 banner rows (weight 1, executable via INDEX), BSQ-0392 CI stub gap (weight 2), BSQ-0393 contradiction (weight 2, ESCALATED to manifest owner), BSQ-0395 launch prompt (weight 2, dismissed). Decision: BSQ-0396 DEC-09.

## 7. Validation
rows=97 invalid=0 valid=97
