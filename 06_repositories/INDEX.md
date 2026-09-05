---
doc_id: INDEX-06
title: "INDEX-06 — 06_repositories: briefing, tree table (19 repos), file table (skeletons), known gaps, honesty line, self-audit"
version: "1.0"
date: "2026-09-05"
status: "Added (sprint-1); indexes only; no code exists anywhere in this folder; every skeleton is Proposed (DEC-09 Open); REPO-MAP v2 is stale against RUN-REPORT R6 (five proposed repos) pending DEC-09 — recorded, not resolved here"
folder: "06_repositories/"
produced_by: "sprint-1 (survey-2 Build-Spec Queue) — generated tables from disk by 11_prompts/runs/2026-09-05_sprint-1/tools/render_index.py; briefing text authored; edits nothing"
---

# INDEX-06 — 06_repositories

## §1 Briefing — what a skeleton is

A **repository skeleton** is the shape of a repo before any code exists: a README that states what its owning primer requires, a MANIFEST.yaml stub (Arch §10 / Harness manifest discipline) that becomes the artifact manifest on first emit, a `ci/pipeline.yml` stub (Tier 1+2 shape, Arch §11.1; imports from cdss-evalstack; carries the dormant R29 ratchet hook that activates on DEC-02, MT2 §7(4)), per-directory READMEs mirroring the primer's §-4/§-8 layout, and CODEOWNERS where a primer mandates them. Trees mirror **REPO-MAP v2** (14 existing repos + 4 proposed + cdss-integration + the GPP channel file). Doctrine: contracts appear only as **pointer stubs** to the canonical drafts in 05_ — move-never-copy on ratification ("duplication is where drift begins"); cdss-corpus is intentionally minimal (firewall banner; instantiate in-account only); the lockfile home is DEC-09's call (cdss-integration or the spine). Every skeleton file is a CC-5 (README/MANIFEST/CI — instruction-bearing) or CC-2 (CODEOWNERS/pointer) artifact with its own HARDEN-1.1 row (the A-001 glob, now enumerated).

## §2 Tree table (19 trees)

| repo | owning primer / volume (REPO-MAP) | REPO-MAP status | files | README | MANIFEST | CI | CODEOWNERS | sub-dir stubs | launch prompt in 11_ | HARDEN-1.1 rows | HARDEN-3.1 tasks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `cdss-coder` | J-1/J-2 | Existing (labels per C-01) | 3 | Y | Y | Y | N | — | — (fork channel; J-1/J-2 via PROMPT-J posture) | 112–114 | T-405–T-407 |
| `cdss-compiler` | EN-3/CP | **Proposed** | 9 | Y | Y | Y | Y | assist, bundles, lift, sources, tests | **NONE — no owning primer, no prompt (survey-2 BSQ-0391; after DEC-09/DEC-13)** | 115–123 | T-408–T-416 |
| `cdss-conformal` | F | Existing | 3 | Y | Y | Y | N | — | PROMPT-F | 124–126 | T-417–T-419 |
| `cdss-corpus` | C | Existing (firewall untouched) | 2 | Y | Y | N | N | — | PROMPT-C | 127–128 | T-420–T-421 |
| `cdss-corruption` | G | Existing+Transformed | 4 | Y | Y | Y | N | rulebook | PROMPT-G | 129–132 | T-422–T-425 |
| `cdss-engine` | A | Existing | 6 | Y | Y | Y | N | properties, service, tests | PROMPT-A | 133–138 | T-426–T-431 |
| `cdss-evalstack` | I | Existing+Transformed | 4 | Y | Y | Y | N | pipelines | PROMPT-I | 139–142 | T-432–T-435 |
| `cdss-fabric` | MAK-FFC/ABC | **Proposed** | 8 | Y | Y | Y | N | deviation, ledger, projector, service, tests | PROMPT-PRM-ABC / PRM-HDC (fabric modules per RUN-REPORT R6) | 143–150 | T-436–T-443 |
| `cdss-governance` | J | Existing+Transformed | 3 | Y | Y | Y | N | — | PROMPT-J (+PRM-ANT regulatory-sensing/) | 151–153 | T-444–T-446 |
| `cdss-graph` | E | Existing+Transformed | 4 | Y | Y | Y | N | tests | PROMPT-E | 154–157 | T-447–T-450 |
| `cdss-harness` | HX | Existing | 3 | Y | Y | Y | N | — | — (HX; no prompt) | 158–160 | T-451–T-453 |
| `cdss-integration` | — | — | 5 | Y | Y | Y | N | lockfile | — (lockfile home per DEC-09) | 161–165 | T-454–T-458 |
| `cdss-library` | B | Existing | 6 | Y | Y | Y | Y | rows, validator | PROMPT-B | 166–171 | T-459–T-464 |
| `cdss-llm-lattice` | K/L | Existing | 3 | Y | Y | Y | N | — | PROMPT-K / PROMPT-L | 172–174 | T-465–T-467 |
| `cdss-lumos` | H | Existing | 3 | Y | Y | Y | N | — | PROMPT-H | 175–177 | T-468–T-470 |
| `cdss-registry` | D | Existing | 5 | Y | Y | Y | Y | policy | PROMPT-D | 178–182 | T-471–T-475 |
| `cdss-spine` | Arch | Existing+Transformed | 11 | Y | Y | Y | Y | contracts, north-star, registers, templates, tolerances, validator | PROMPT-P0 (BUILD_PLAN_V1-S1) | 183–193 | T-476–T-486 |
| `cdss-ui-clinician` | MAK-LBP/HDC | **Proposed** | 7 | Y | Y | Y | N | components, conformance, face, tokens | PROMPT-PRM-LBP / PRM-HDC | 194–200 | T-487–T-493 |
| `cdss-ui-patient` | MAK-PRB/TXC | **Proposed** | 7 | Y | Y | Y | N | android, capture, components, face | PROMPT-PRM-PRB / PRM-TXC (Blocked beyond J-3-safe subset) | 201–207 | T-494–T-500 |

## §3 File table — skeleton files (96) with the per-file floor check (skeleton_check method, survey-2, re-run 2026-09-05)

| path | bytes | banner | class | HARDEN-1.1 row | HARDEN-3.1 task | check |
|---|---|---|---|---|---|---|
| `06_repositories/repo-skeletons/cdss-coder/MANIFEST.yaml` | 605 | Y | CC-5 | 112 | T-405 | conformant |
| `06_repositories/repo-skeletons/cdss-coder/README.md` | 955 | Y | CC-5 | 113 | T-406 | conformant |
| `06_repositories/repo-skeletons/cdss-coder/ci/pipeline.yml` | 711 | Y | CC-5 | 114 | T-407 | conformant |
| `06_repositories/repo-skeletons/cdss-compiler/CODEOWNERS` | 130 | N | CC-2 | 115 | T-408 | no Proposed/skeleton/stub marker |
| `06_repositories/repo-skeletons/cdss-compiler/MANIFEST.yaml` | 545 | Y | CC-5 | 116 | T-409 | conformant |
| `06_repositories/repo-skeletons/cdss-compiler/README.md` | 832 | Y | CC-5 | 117 | T-410 | conformant |
| `06_repositories/repo-skeletons/cdss-compiler/assist/README.md` | 163 | Y | CC-5 | 118 | T-411 | conformant |
| `06_repositories/repo-skeletons/cdss-compiler/bundles/README.md` | 132 | Y | CC-5 | 119 | T-412 | conformant |
| `06_repositories/repo-skeletons/cdss-compiler/ci/pipeline.yml` | 653 | Y | CC-5 | 120 | T-413 | conformant |
| `06_repositories/repo-skeletons/cdss-compiler/lift/README.md` | 153 | Y | CC-5 | 121 | T-414 | conformant |
| `06_repositories/repo-skeletons/cdss-compiler/sources/README.md` | 97 | Y | CC-5 | 122 | T-415 | conformant |
| `06_repositories/repo-skeletons/cdss-compiler/tests/README.md` | 147 | Y | CC-5 | 123 | T-416 | conformant |
| `06_repositories/repo-skeletons/cdss-conformal/MANIFEST.yaml` | 572 | Y | CC-5 | 124 | T-417 | conformant |
| `06_repositories/repo-skeletons/cdss-conformal/README.md` | 702 | Y | CC-5 | 125 | T-418 | conformant |
| `06_repositories/repo-skeletons/cdss-conformal/ci/pipeline.yml` | 734 | Y | CC-5 | 126 | T-419 | conformant |
| `06_repositories/repo-skeletons/cdss-corpus/MANIFEST.yaml` | 657 | Y | CC-5 | 127 | T-420 | conformant |
| `06_repositories/repo-skeletons/cdss-corpus/README.md` | 1038 | Y | CC-5 | 128 | T-421 | conformant |
| `06_repositories/repo-skeletons/cdss-corruption/MANIFEST.yaml` | 595 | Y | CC-5 | 129 | T-422 | conformant |
| `06_repositories/repo-skeletons/cdss-corruption/README.md` | 891 | Y | CC-5 | 130 | T-423 | conformant |
| `06_repositories/repo-skeletons/cdss-corruption/ci/pipeline.yml` | 739 | Y | CC-5 | 131 | T-424 | conformant |
| `06_repositories/repo-skeletons/cdss-corruption/rulebook/README.md` | 273 | Y | CC-5 | 132 | T-425 | conformant |
| `06_repositories/repo-skeletons/cdss-engine/MANIFEST.yaml` | 620 | Y | CC-5 | 133 | T-426 | conformant |
| `06_repositories/repo-skeletons/cdss-engine/README.md` | 867 | Y | CC-5 | 134 | T-427 | conformant |
| `06_repositories/repo-skeletons/cdss-engine/ci/pipeline.yml` | 700 | Y | CC-5 | 135 | T-428 | conformant |
| `06_repositories/repo-skeletons/cdss-engine/properties/README.md` | 155 | N | CC-5 | 136 | T-429 | no Proposed/skeleton/stub marker |
| `06_repositories/repo-skeletons/cdss-engine/service/README.md` | 203 | Y | CC-5 | 137 | T-430 | conformant |
| `06_repositories/repo-skeletons/cdss-engine/tests/README.md` | 222 | N | CC-5 | 138 | T-431 | no Proposed/skeleton/stub marker |
| `06_repositories/repo-skeletons/cdss-evalstack/MANIFEST.yaml` | 597 | Y | CC-5 | 139 | T-432 | conformant |
| `06_repositories/repo-skeletons/cdss-evalstack/README.md` | 928 | Y | CC-5 | 140 | T-433 | conformant |
| `06_repositories/repo-skeletons/cdss-evalstack/ci/pipeline.yml` | 851 | Y | CC-5 | 141 | T-434 | conformant |
| `06_repositories/repo-skeletons/cdss-evalstack/pipelines/README.md` | 253 | Y | CC-5 | 142 | T-435 | conformant |
| `06_repositories/repo-skeletons/cdss-fabric/MANIFEST.yaml` | 541 | Y | CC-5 | 143 | T-436 | conformant |
| `06_repositories/repo-skeletons/cdss-fabric/README.md` | 1023 | Y | CC-5 | 144 | T-437 | conformant |
| `06_repositories/repo-skeletons/cdss-fabric/ci/pipeline.yml` | 653 | Y | CC-5 | 145 | T-438 | conformant |
| `06_repositories/repo-skeletons/cdss-fabric/deviation/README.md` | 129 | Y | CC-5 | 146 | T-439 | conformant |
| `06_repositories/repo-skeletons/cdss-fabric/ledger/README.md` | 126 | Y | CC-5 | 147 | T-440 | conformant |
| `06_repositories/repo-skeletons/cdss-fabric/projector/README.md` | 140 | Y | CC-5 | 148 | T-441 | conformant |
| `06_repositories/repo-skeletons/cdss-fabric/service/README.md` | 195 | Y | CC-5 | 149 | T-442 | conformant |
| `06_repositories/repo-skeletons/cdss-fabric/tests/README.md` | 159 | Y | CC-5 | 150 | T-443 | conformant |
| `06_repositories/repo-skeletons/cdss-governance/MANIFEST.yaml` | 622 | Y | CC-5 | 151 | T-444 | conformant |
| `06_repositories/repo-skeletons/cdss-governance/README.md` | 847 | Y | CC-5 | 152 | T-445 | conformant |
| `06_repositories/repo-skeletons/cdss-governance/ci/pipeline.yml` | 941 | Y | CC-5 | 153 | T-446 | conformant |
| `06_repositories/repo-skeletons/cdss-graph/MANIFEST.yaml` | 625 | Y | CC-5 | 154 | T-447 | conformant |
| `06_repositories/repo-skeletons/cdss-graph/README.md` | 731 | Y | CC-5 | 155 | T-448 | conformant |
| `06_repositories/repo-skeletons/cdss-graph/ci/pipeline.yml` | 730 | Y | CC-5 | 156 | T-449 | conformant |
| `06_repositories/repo-skeletons/cdss-graph/tests/README.md` | 221 | N | CC-5 | 157 | T-450 | no Proposed/skeleton/stub marker |
| `06_repositories/repo-skeletons/cdss-harness/MANIFEST.yaml` | 619 | Y | CC-5 | 158 | T-451 | conformant |
| `06_repositories/repo-skeletons/cdss-harness/README.md` | 914 | Y | CC-5 | 159 | T-452 | conformant |
| `06_repositories/repo-skeletons/cdss-harness/ci/pipeline.yml` | 884 | Y | CC-5 | 160 | T-453 | conformant |
| `06_repositories/repo-skeletons/cdss-integration/GPP-CHANNEL.md` | 815 | Y | CC-5 | 161 | T-454 | conformant |
| `06_repositories/repo-skeletons/cdss-integration/MANIFEST.yaml` | 603 | Y | CC-5 | 162 | T-455 | conformant |
| `06_repositories/repo-skeletons/cdss-integration/README.md` | 1039 | Y | CC-5 | 163 | T-456 | conformant |
| `06_repositories/repo-skeletons/cdss-integration/ci/pipeline.yml` | 1160 | Y | CC-5 | 164 | T-457 | conformant |
| `06_repositories/repo-skeletons/cdss-integration/lockfile/README.md` | 207 | N | CC-5 | 165 | T-458 | no Proposed/skeleton/stub marker |
| `06_repositories/repo-skeletons/cdss-library/CODEOWNERS` | 110 | Y | CC-2 | 166 | T-459 | conformant |
| `06_repositories/repo-skeletons/cdss-library/MANIFEST.yaml` | 609 | Y | CC-5 | 167 | T-460 | conformant |
| `06_repositories/repo-skeletons/cdss-library/README.md` | 753 | Y | CC-5 | 168 | T-461 | conformant |
| `06_repositories/repo-skeletons/cdss-library/ci/pipeline.yml` | 704 | Y | CC-5 | 169 | T-462 | conformant |
| `06_repositories/repo-skeletons/cdss-library/rows/README.md` | 193 | N | CC-5 | 170 | T-463 | no Proposed/skeleton/stub marker |
| `06_repositories/repo-skeletons/cdss-library/validator/README.md` | 177 | N | CC-5 | 171 | T-464 | no Proposed/skeleton/stub marker |
| `06_repositories/repo-skeletons/cdss-llm-lattice/MANIFEST.yaml` | 614 | Y | CC-5 | 172 | T-465 | conformant |
| `06_repositories/repo-skeletons/cdss-llm-lattice/README.md` | 1039 | Y | CC-5 | 173 | T-466 | conformant |
| `06_repositories/repo-skeletons/cdss-llm-lattice/ci/pipeline.yml` | 1085 | Y | CC-5 | 174 | T-467 | conformant |
| `06_repositories/repo-skeletons/cdss-lumos/MANIFEST.yaml` | 585 | Y | CC-5 | 175 | T-468 | conformant |
| `06_repositories/repo-skeletons/cdss-lumos/README.md` | 782 | Y | CC-5 | 176 | T-469 | conformant |
| `06_repositories/repo-skeletons/cdss-lumos/ci/pipeline.yml` | 963 | Y | CC-5 | 177 | T-470 | conformant |
| `06_repositories/repo-skeletons/cdss-registry/CODEOWNERS` | 169 | N | CC-2 | 178 | T-471 | no Proposed/skeleton/stub marker |
| `06_repositories/repo-skeletons/cdss-registry/MANIFEST.yaml` | 570 | Y | CC-5 | 179 | T-472 | conformant |
| `06_repositories/repo-skeletons/cdss-registry/README.md` | 791 | Y | CC-5 | 180 | T-473 | conformant |
| `06_repositories/repo-skeletons/cdss-registry/ci/pipeline.yml` | 690 | Y | CC-5 | 181 | T-474 | conformant |
| `06_repositories/repo-skeletons/cdss-registry/policy/README.md` | 171 | N | CC-5 | 182 | T-475 | no Proposed/skeleton/stub marker |
| `06_repositories/repo-skeletons/cdss-spine/CODEOWNERS` | 183 | Y | CC-2 | 183 | T-476 | conformant |
| `06_repositories/repo-skeletons/cdss-spine/MANIFEST.yaml` | 750 | Y | CC-5 | 184 | T-477 | conformant |
| `06_repositories/repo-skeletons/cdss-spine/README.md` | 1089 | Y | CC-5 | 185 | T-478 | conformant |
| `06_repositories/repo-skeletons/cdss-spine/ci/pipeline.yml` | 717 | Y | CC-5 | 186 | T-479 | conformant |
| `06_repositories/repo-skeletons/cdss-spine/contracts/CONTRACT-ARG-1.pointer.md` | 260 | Y | CC-2 | 187 | T-480 | conformant |
| `06_repositories/repo-skeletons/cdss-spine/contracts/README.md` | 576 | Y | CC-5 | 188 | T-481 | conformant |
| `06_repositories/repo-skeletons/cdss-spine/north-star/README.md` | 151 | Y | CC-5 | 189 | T-482 | conformant |
| `06_repositories/repo-skeletons/cdss-spine/registers/README.md` | 314 | N | CC-5 | 190 | T-483 | no Proposed/skeleton/stub marker |
| `06_repositories/repo-skeletons/cdss-spine/templates/README.md` | 177 | N | CC-5 | 191 | T-484 | no Proposed/skeleton/stub marker |
| `06_repositories/repo-skeletons/cdss-spine/tolerances/README.md` | 246 | N | CC-5 | 192 | T-485 | no Proposed/skeleton/stub marker |
| `06_repositories/repo-skeletons/cdss-spine/validator/README.md` | 338 | N | CC-5 | 193 | T-486 | no Proposed/skeleton/stub marker |
| `06_repositories/repo-skeletons/cdss-ui-clinician/MANIFEST.yaml` | 553 | Y | CC-5 | 194 | T-487 | conformant |
| `06_repositories/repo-skeletons/cdss-ui-clinician/README.md` | 650 | Y | CC-5 | 195 | T-488 | conformant |
| `06_repositories/repo-skeletons/cdss-ui-clinician/ci/pipeline.yml` | 653 | Y | CC-5 | 196 | T-489 | conformant |
| `06_repositories/repo-skeletons/cdss-ui-clinician/components/README.md` | 102 | Y | CC-5 | 197 | T-490 | conformant |
| `06_repositories/repo-skeletons/cdss-ui-clinician/conformance/README.md` | 141 | Y | CC-5 | 198 | T-491 | conformant |
| `06_repositories/repo-skeletons/cdss-ui-clinician/face/README.md` | 137 | Y | CC-5 | 199 | T-492 | conformant |
| `06_repositories/repo-skeletons/cdss-ui-clinician/tokens/README.md` | 113 | Y | CC-5 | 200 | T-493 | conformant |
| `06_repositories/repo-skeletons/cdss-ui-patient/MANIFEST.yaml` | 549 | Y | CC-5 | 201 | T-494 | conformant |
| `06_repositories/repo-skeletons/cdss-ui-patient/README.md` | 629 | Y | CC-5 | 202 | T-495 | conformant |
| `06_repositories/repo-skeletons/cdss-ui-patient/android/README.md` | 164 | Y | CC-5 | 203 | T-496 | conformant |
| `06_repositories/repo-skeletons/cdss-ui-patient/capture/README.md` | 99 | Y | CC-5 | 204 | T-497 | conformant |
| `06_repositories/repo-skeletons/cdss-ui-patient/ci/pipeline.yml` | 653 | Y | CC-5 | 205 | T-498 | conformant |
| `06_repositories/repo-skeletons/cdss-ui-patient/components/README.md` | 117 | Y | CC-5 | 206 | T-499 | conformant |
| `06_repositories/repo-skeletons/cdss-ui-patient/face/README.md` | 214 | Y | CC-5 | 207 | T-500 | conformant |

Folder-level files:

| path | class | doc_id | version | date | status (quoted) | bytes | disposition | HARDEN-1/1.1 row | HARDEN-3.1 task | 00_MANIFEST row |
|---|---|---|---|---|---|---|---|---|---|---|
| `06_repositories/INDEX.md` | CC-8 | INDEX-06 | 1.0 | 2026-09-05 | Added (sprint-1); indexes only; no code exists anywhere in this folder; every skeleton is Proposed (DEC-09 Open); REPO-MAP v2 is stale against RUN-REPORT R6 (five proposed repos) pending DEC-09 — recorded, not resolved h… | 49928 | Added (sprint-1) | 111 | T-713 | §1 row (5) superseded by §7 A-001 (91) + A-004 |
| `06_repositories/REPO-MAP_v2.md` | CC-5 | REPO-MAP-v2 | — | — | Existing rows Retained verbatim in intent from Arch §10; new rows Proposed (DEC-09). Pragmatic-phasing rule retained: spine, corpus, registry are load-bearing from day one; others may begin as folders in one working repo… | 4322 | Retained (REPO-MAP existing rows) / Proposed (skeletons, DEC-09) | 69 | T-100 | §1 row (5) superseded by §7 A-001 (91) + A-004 |
| `06_repositories/repo-skeletons/cdss-coder/MANIFEST.yaml` | CC-5 | — | — | — | # MANIFEST stub — cdss-coder (Skeleton, Proposed; format per Arch §10 / Harness manifest discipline) | 605 | Retained (REPO-MAP existing rows) / Proposed (skeletons, DEC-09) | 112 | T-405 | §1 row (5) superseded by §7 A-001 (91) + A-004 |
| `06_repositories/repo-skeletons/cdss-coder/README.md` | CC-5 | — | — | — | <!-- SKELETON — Proposed (DEC-09; Arch §10 mirrored). No code, build, or deployment is claimed. Every directory README states what its owning primer/annex requi | 955 | Retained (REPO-MAP existing rows) / Proposed (skeletons, DEC-09) | 113 | T-406 | §1 row (5) superseded by §7 A-001 (91) + A-004 |
| `06_repositories/repo-skeletons/cdss-coder/ci/pipeline.yml` | CC-5 | — | — | — | # ci/pipeline.yml — STUB (Proposed; not runnable; wired for real in cdss-evalstack imports) | 711 | Retained (REPO-MAP existing rows) / Proposed (skeletons, DEC-09) | 114 | T-407 | §1 row (5) superseded by §7 A-001 (91) + A-004 |
| `06_repositories/repo-skeletons/cdss-compiler/CODEOWNERS` | CC-2 | — | — | — | # Bundles enter through the registry gateway discipline | 130 | Retained (REPO-MAP existing rows) / Proposed (skeletons, DEC-09) | 115 | T-408 | §1 row (5) superseded by §7 A-001 (91) + A-004 |
| `06_repositories/repo-skeletons/cdss-compiler/MANIFEST.yaml` | CC-5 | — | — | — | # MANIFEST stub — cdss-compiler (Skeleton, Proposed; format per Arch §10 / Harness manifest discipline) | 545 | Retained (REPO-MAP existing rows) / Proposed (skeletons, DEC-09) | 116 | T-409 | §1 row (5) superseded by §7 A-001 (91) + A-004 |
| `06_repositories/repo-skeletons/cdss-compiler/README.md` | CC-5 | — | — | — | # cdss-compiler (Proposed — DEC-09; skeleton only) | 832 | Retained (REPO-MAP existing rows) / Proposed (skeletons, DEC-09) | 117 | T-410 | §1 row (5) superseded by §7 A-001 (91) + A-004 |
| `06_repositories/repo-skeletons/cdss-compiler/assist/README.md` | CC-5 | — | — | — | # cdss-compiler/assist (skeleton stub) | 163 | Retained (REPO-MAP existing rows) / Proposed (skeletons, DEC-09) | 118 | T-411 | §1 row (5) superseded by §7 A-001 (91) + A-004 |
| `06_repositories/repo-skeletons/cdss-compiler/bundles/README.md` | CC-5 | — | — | — | # cdss-compiler/bundles (skeleton stub) | 132 | Retained (REPO-MAP existing rows) / Proposed (skeletons, DEC-09) | 119 | T-412 | §1 row (5) superseded by §7 A-001 (91) + A-004 |
| `06_repositories/repo-skeletons/cdss-compiler/ci/pipeline.yml` | CC-5 | — | — | — | # ci/pipeline.yml — STUB (Proposed; not runnable; wired for real in cdss-evalstack imports) | 653 | Retained (REPO-MAP existing rows) / Proposed (skeletons, DEC-09) | 120 | T-413 | §1 row (5) superseded by §7 A-001 (91) + A-004 |
| `06_repositories/repo-skeletons/cdss-compiler/lift/README.md` | CC-5 | — | — | — | # cdss-compiler/lift (skeleton stub) | 153 | Retained (REPO-MAP existing rows) / Proposed (skeletons, DEC-09) | 121 | T-414 | §1 row (5) superseded by §7 A-001 (91) + A-004 |
| `06_repositories/repo-skeletons/cdss-compiler/sources/README.md` | CC-5 | — | — | — | # cdss-compiler/sources (skeleton stub) | 97 | Retained (REPO-MAP existing rows) / Proposed (skeletons, DEC-09) | 122 | T-415 | §1 row (5) superseded by §7 A-001 (91) + A-004 |
| `06_repositories/repo-skeletons/cdss-compiler/tests/README.md` | CC-5 | — | — | — | # cdss-compiler/tests (skeleton stub) | 147 | Retained (REPO-MAP existing rows) / Proposed (skeletons, DEC-09) | 123 | T-416 | §1 row (5) superseded by §7 A-001 (91) + A-004 |
| `06_repositories/repo-skeletons/cdss-conformal/MANIFEST.yaml` | CC-5 | — | — | — | # MANIFEST stub — cdss-conformal (Skeleton, Proposed; format per Arch §10 / Harness manifest discipline) | 572 | Retained (REPO-MAP existing rows) / Proposed (skeletons, DEC-09) | 124 | T-417 | §1 row (5) superseded by §7 A-001 (91) + A-004 |
| `06_repositories/repo-skeletons/cdss-conformal/README.md` | CC-5 | — | — | — | <!-- SKELETON — Proposed (DEC-09; Arch §10 mirrored). No code, build, or deployment is claimed. Every directory README states what its owning primer/annex requi | 702 | Retained (REPO-MAP existing rows) / Proposed (skeletons, DEC-09) | 125 | T-418 | §1 row (5) superseded by §7 A-001 (91) + A-004 |
| `06_repositories/repo-skeletons/cdss-conformal/ci/pipeline.yml` | CC-5 | — | — | — | # ci/pipeline.yml — STUB (Proposed; not runnable; wired for real in cdss-evalstack imports) | 734 | Retained (REPO-MAP existing rows) / Proposed (skeletons, DEC-09) | 126 | T-419 | §1 row (5) superseded by §7 A-001 (91) + A-004 |
| `06_repositories/repo-skeletons/cdss-corpus/MANIFEST.yaml` | CC-5 | — | — | — | # MANIFEST stub — cdss-corpus (Skeleton, Proposed; format per Arch §10 / Harness manifest discipline) | 657 | Retained (REPO-MAP existing rows) / Proposed (skeletons, DEC-09) | 127 | T-420 | §1 row (5) superseded by §7 A-001 (91) + A-004 |
| `06_repositories/repo-skeletons/cdss-corpus/README.md` | CC-5 | — | — | — | <!-- SKELETON — Proposed (DEC-09; Arch §10 mirrored). No code, build, or deployment is claimed. Every directory README states what its owning primer/annex requi | 1038 | Retained (REPO-MAP existing rows) / Proposed (skeletons, DEC-09) | 128 | T-421 | §1 row (5) superseded by §7 A-001 (91) + A-004 |
| `06_repositories/repo-skeletons/cdss-corruption/MANIFEST.yaml` | CC-5 | — | — | — | # MANIFEST stub — cdss-corruption (Skeleton, Proposed; format per Arch §10 / Harness manifest discipline) | 595 | Retained (REPO-MAP existing rows) / Proposed (skeletons, DEC-09) | 129 | T-422 | §1 row (5) superseded by §7 A-001 (91) + A-004 |
| `06_repositories/repo-skeletons/cdss-corruption/README.md` | CC-5 | — | — | — | <!-- SKELETON — Proposed (DEC-09; Arch §10 mirrored). No code, build, or deployment is claimed. Every directory README states what its owning primer/annex requi | 891 | Retained (REPO-MAP existing rows) / Proposed (skeletons, DEC-09) | 130 | T-423 | §1 row (5) superseded by §7 A-001 (91) + A-004 |
| `06_repositories/repo-skeletons/cdss-corruption/ci/pipeline.yml` | CC-5 | — | — | — | # ci/pipeline.yml — STUB (Proposed; not runnable; wired for real in cdss-evalstack imports) | 739 | Retained (REPO-MAP existing rows) / Proposed (skeletons, DEC-09) | 131 | T-424 | §1 row (5) superseded by §7 A-001 (91) + A-004 |
| `06_repositories/repo-skeletons/cdss-corruption/rulebook/README.md` | CC-5 | — | — | — | # Rulebook (R8) | 273 | Retained (REPO-MAP existing rows) / Proposed (skeletons, DEC-09) | 132 | T-425 | §1 row (5) superseded by §7 A-001 (91) + A-004 |
| `06_repositories/repo-skeletons/cdss-engine/MANIFEST.yaml` | CC-5 | — | — | — | # MANIFEST stub — cdss-engine (Skeleton, Proposed; format per Arch §10 / Harness manifest discipline) | 620 | Retained (REPO-MAP existing rows) / Proposed (skeletons, DEC-09) | 133 | T-426 | §1 row (5) superseded by §7 A-001 (91) + A-004 |
| `06_repositories/repo-skeletons/cdss-engine/README.md` | CC-5 | — | — | — | <!-- SKELETON — Proposed (DEC-09; Arch §10 mirrored). No code, build, or deployment is claimed. Every directory README states what its owning primer/annex requi | 867 | Retained (REPO-MAP existing rows) / Proposed (skeletons, DEC-09) | 134 | T-427 | §1 row (5) superseded by §7 A-001 (91) + A-004 |
| `06_repositories/repo-skeletons/cdss-engine/ci/pipeline.yml` | CC-5 | — | — | — | # ci/pipeline.yml — STUB (Proposed; not runnable; wired for real in cdss-evalstack imports) | 700 | Retained (REPO-MAP existing rows) / Proposed (skeletons, DEC-09) | 135 | T-428 | §1 row (5) superseded by §7 A-001 (91) + A-004 |
| `06_repositories/repo-skeletons/cdss-engine/properties/README.md` | CC-5 | — | — | — | # Property suite (I mechanism 1) | 155 | Retained (REPO-MAP existing rows) / Proposed (skeletons, DEC-09) | 136 | T-429 | §1 row (5) superseded by §7 A-001 (91) + A-004 |
| `06_repositories/repo-skeletons/cdss-engine/service/README.md` | CC-5 | — | — | — | # Engine service (stub) | 203 | Retained (REPO-MAP existing rows) / Proposed (skeletons, DEC-09) | 137 | T-430 | §1 row (5) superseded by §7 A-001 (91) + A-004 |
| `06_repositories/repo-skeletons/cdss-engine/tests/README.md` | CC-5 | — | — | — | # Acceptance (from A10 + DEPLOY-2) | 222 | Retained (REPO-MAP existing rows) / Proposed (skeletons, DEC-09) | 138 | T-431 | §1 row (5) superseded by §7 A-001 (91) + A-004 |
| `06_repositories/repo-skeletons/cdss-evalstack/MANIFEST.yaml` | CC-5 | — | — | — | # MANIFEST stub — cdss-evalstack (Skeleton, Proposed; format per Arch §10 / Harness manifest discipline) | 597 | Retained (REPO-MAP existing rows) / Proposed (skeletons, DEC-09) | 139 | T-432 | §1 row (5) superseded by §7 A-001 (91) + A-004 |
| `06_repositories/repo-skeletons/cdss-evalstack/README.md` | CC-5 | — | — | — | <!-- SKELETON — Proposed (DEC-09; Arch §10 mirrored). No code, build, or deployment is claimed. Every directory README states what its owning primer/annex requi | 928 | Retained (REPO-MAP existing rows) / Proposed (skeletons, DEC-09) | 140 | T-433 | §1 row (5) superseded by §7 A-001 (91) + A-004 |
| `06_repositories/repo-skeletons/cdss-evalstack/ci/pipeline.yml` | CC-5 | — | — | — | # ci/pipeline.yml — STUB (Proposed; not runnable; this repo is the SOURCE of the pipeline definitions every other repo imports — Primer I) | 851 | Added (sprint-1) — Proposed | 141 | T-434 | §1 row (5) superseded by §7 A-001 (91) + A-004 |
| `06_repositories/repo-skeletons/cdss-evalstack/pipelines/README.md` | CC-5 | — | — | — | # Shared pipeline definitions | 253 | Retained (REPO-MAP existing rows) / Proposed (skeletons, DEC-09) | 142 | T-435 | §1 row (5) superseded by §7 A-001 (91) + A-004 |
| `06_repositories/repo-skeletons/cdss-fabric/MANIFEST.yaml` | CC-5 | — | — | — | # MANIFEST stub — cdss-fabric (Skeleton, Proposed; format per Arch §10 / Harness manifest discipline) | 541 | Retained (REPO-MAP existing rows) / Proposed (skeletons, DEC-09) | 143 | T-436 | §1 row (5) superseded by §7 A-001 (91) + A-004 |
| `06_repositories/repo-skeletons/cdss-fabric/README.md` | CC-5 | — | — | — | # cdss-fabric (Proposed — DEC-09; skeleton only, no code claimed) | 1023 | Retained (REPO-MAP existing rows) / Proposed (skeletons, DEC-09) | 144 | T-437 | §1 row (5) superseded by §7 A-001 (91) + A-004 |
| `06_repositories/repo-skeletons/cdss-fabric/ci/pipeline.yml` | CC-5 | — | — | — | # ci/pipeline.yml — STUB (Proposed; not runnable; wired for real in cdss-evalstack imports) | 653 | Retained (REPO-MAP existing rows) / Proposed (skeletons, DEC-09) | 145 | T-438 | §1 row (5) superseded by §7 A-001 (91) + A-004 |
| `06_repositories/repo-skeletons/cdss-fabric/deviation/README.md` | CC-5 | — | — | — | # cdss-fabric/deviation (skeleton stub) | 129 | Retained (REPO-MAP existing rows) / Proposed (skeletons, DEC-09) | 146 | T-439 | §1 row (5) superseded by §7 A-001 (91) + A-004 |
| `06_repositories/repo-skeletons/cdss-fabric/ledger/README.md` | CC-5 | — | — | — | # cdss-fabric/ledger (skeleton stub) | 126 | Retained (REPO-MAP existing rows) / Proposed (skeletons, DEC-09) | 147 | T-440 | §1 row (5) superseded by §7 A-001 (91) + A-004 |
| `06_repositories/repo-skeletons/cdss-fabric/projector/README.md` | CC-5 | — | — | — | # cdss-fabric/projector (skeleton stub) | 140 | Retained (REPO-MAP existing rows) / Proposed (skeletons, DEC-09) | 148 | T-441 | §1 row (5) superseded by §7 A-001 (91) + A-004 |
| `06_repositories/repo-skeletons/cdss-fabric/service/README.md` | CC-5 | — | — | — | # cdss-fabric/service (skeleton stub) | 195 | Retained (REPO-MAP existing rows) / Proposed (skeletons, DEC-09) | 149 | T-442 | §1 row (5) superseded by §7 A-001 (91) + A-004 |
| `06_repositories/repo-skeletons/cdss-fabric/tests/README.md` | CC-5 | — | — | — | # cdss-fabric/tests (skeleton stub) | 159 | Retained (REPO-MAP existing rows) / Proposed (skeletons, DEC-09) | 150 | T-443 | §1 row (5) superseded by §7 A-001 (91) + A-004 |
| `06_repositories/repo-skeletons/cdss-governance/MANIFEST.yaml` | CC-5 | — | — | — | # MANIFEST stub — cdss-governance (Skeleton, Proposed; format per Arch §10 / Harness manifest discipline) | 622 | Retained (REPO-MAP existing rows) / Proposed (skeletons, DEC-09) | 151 | T-444 | §1 row (5) superseded by §7 A-001 (91) + A-004 |
| `06_repositories/repo-skeletons/cdss-governance/README.md` | CC-5 | — | — | — | <!-- SKELETON — Proposed (DEC-09; Arch §10 mirrored). No code, build, or deployment is claimed. Every directory README states what its owning primer/annex requi | 847 | Retained (REPO-MAP existing rows) / Proposed (skeletons, DEC-09) | 152 | T-445 | §1 row (5) superseded by §7 A-001 (91) + A-004 |
| `06_repositories/repo-skeletons/cdss-governance/ci/pipeline.yml` | CC-5 | — | — | — | # ci/pipeline.yml — STUB (Proposed; not runnable; wired for real in cdss-evalstack imports) | 941 | Added (sprint-1) — Proposed | 153 | T-446 | §1 row (5) superseded by §7 A-001 (91) + A-004 |
| `06_repositories/repo-skeletons/cdss-graph/MANIFEST.yaml` | CC-5 | — | — | — | # MANIFEST stub — cdss-graph (Skeleton, Proposed; format per Arch §10 / Harness manifest discipline) | 625 | Retained (REPO-MAP existing rows) / Proposed (skeletons, DEC-09) | 154 | T-447 | §1 row (5) superseded by §7 A-001 (91) + A-004 |
| `06_repositories/repo-skeletons/cdss-graph/README.md` | CC-5 | — | — | — | <!-- SKELETON — Proposed (DEC-09; Arch §10 mirrored). No code, build, or deployment is claimed. Every directory README states what its owning primer/annex requi | 731 | Retained (REPO-MAP existing rows) / Proposed (skeletons, DEC-09) | 155 | T-448 | §1 row (5) superseded by §7 A-001 (91) + A-004 |
| `06_repositories/repo-skeletons/cdss-graph/ci/pipeline.yml` | CC-5 | — | — | — | # ci/pipeline.yml — STUB (Proposed; not runnable; wired for real in cdss-evalstack imports) | 730 | Retained (REPO-MAP existing rows) / Proposed (skeletons, DEC-09) | 156 | T-449 | §1 row (5) superseded by §7 A-001 (91) + A-004 |
| `06_repositories/repo-skeletons/cdss-graph/tests/README.md` | CC-5 | — | — | — | # Acceptance | 221 | Retained (REPO-MAP existing rows) / Proposed (skeletons, DEC-09) | 157 | T-450 | §1 row (5) superseded by §7 A-001 (91) + A-004 |
| `06_repositories/repo-skeletons/cdss-harness/MANIFEST.yaml` | CC-5 | — | — | — | # MANIFEST stub — cdss-harness (Skeleton, Proposed; format per Arch §10 / Harness manifest discipline) | 619 | Retained (REPO-MAP existing rows) / Proposed (skeletons, DEC-09) | 158 | T-451 | §1 row (5) superseded by §7 A-001 (91) + A-004 |
| `06_repositories/repo-skeletons/cdss-harness/README.md` | CC-5 | — | — | — | <!-- SKELETON — Proposed (DEC-09; Arch §10 mirrored). No code, build, or deployment is claimed. Every directory README states what its owning primer/annex requi | 914 | Retained (REPO-MAP existing rows) / Proposed (skeletons, DEC-09) | 159 | T-452 | §1 row (5) superseded by §7 A-001 (91) + A-004 |
| `06_repositories/repo-skeletons/cdss-harness/ci/pipeline.yml` | CC-5 | — | — | — | # ci/pipeline.yml — STUB (Proposed; not runnable; wired for real in cdss-evalstack imports) | 884 | Added (sprint-1) — Proposed | 160 | T-453 | §1 row (5) superseded by §7 A-001 (91) + A-004 |
| `06_repositories/repo-skeletons/cdss-integration/GPP-CHANNEL.md` | CC-5 | — | — | — | # GPP release channel (Proposed — MAK-J3 v0.9; DEC-06 ratifies) | 815 | Retained (REPO-MAP existing rows) / Proposed (skeletons, DEC-09) | 161 | T-454 | §1 row (5) superseded by §7 A-001 (91) + A-004 |
| `06_repositories/repo-skeletons/cdss-integration/MANIFEST.yaml` | CC-5 | — | — | — | # MANIFEST stub — cdss-integration (Skeleton, Proposed; format per Arch §10 / Harness manifest discipline) | 603 | Retained (REPO-MAP existing rows) / Proposed (skeletons, DEC-09) | 162 | T-455 | §1 row (5) superseded by §7 A-001 (91) + A-004 |
| `06_repositories/repo-skeletons/cdss-integration/README.md` | CC-5 | — | — | — | <!-- SKELETON — Proposed (DEC-09; Arch §10 mirrored). No code, build, or deployment is claimed. Every directory README states what its owning primer/annex requi | 1039 | Retained (REPO-MAP existing rows) / Proposed (skeletons, DEC-09) | 163 | T-456 | §1 row (5) superseded by §7 A-001 (91) + A-004 |
| `06_repositories/repo-skeletons/cdss-integration/ci/pipeline.yml` | CC-5 | — | — | — | # ci/pipeline.yml — STUB (Proposed; not runnable; wired for real in cdss-evalstack imports) | 1160 | Added (sprint-1) — Proposed | 164 | T-457 | §1 row (5) superseded by §7 A-001 (91) + A-004 |
| `06_repositories/repo-skeletons/cdss-integration/lockfile/README.md` | CC-5 | — | — | — | # Integration lockfile | 207 | Retained (REPO-MAP existing rows) / Proposed (skeletons, DEC-09) | 165 | T-458 | §1 row (5) superseded by §7 A-001 (91) + A-004 |
| `06_repositories/repo-skeletons/cdss-library/CODEOWNERS` | CC-2 | — | — | — | # Stub — clinician CODEOWNERS on row changes (B8 gateway) | 110 | Retained (REPO-MAP existing rows) / Proposed (skeletons, DEC-09) | 166 | T-459 | §1 row (5) superseded by §7 A-001 (91) + A-004 |
| `06_repositories/repo-skeletons/cdss-library/MANIFEST.yaml` | CC-5 | — | — | — | # MANIFEST stub — cdss-library (Skeleton, Proposed; format per Arch §10 / Harness manifest discipline) | 609 | Retained (REPO-MAP existing rows) / Proposed (skeletons, DEC-09) | 167 | T-460 | §1 row (5) superseded by §7 A-001 (91) + A-004 |
| `06_repositories/repo-skeletons/cdss-library/README.md` | CC-5 | — | — | — | <!-- SKELETON — Proposed (DEC-09; Arch §10 mirrored). No code, build, or deployment is claimed. Every directory README states what its owning primer/annex requi | 753 | Retained (REPO-MAP existing rows) / Proposed (skeletons, DEC-09) | 168 | T-461 | §1 row (5) superseded by §7 A-001 (91) + A-004 |
| `06_repositories/repo-skeletons/cdss-library/ci/pipeline.yml` | CC-5 | — | — | — | # ci/pipeline.yml — STUB (Proposed; not runnable; wired for real in cdss-evalstack imports) | 704 | Retained (REPO-MAP existing rows) / Proposed (skeletons, DEC-09) | 169 | T-462 | §1 row (5) superseded by §7 A-001 (91) + A-004 |
| `06_repositories/repo-skeletons/cdss-library/rows/README.md` | CC-5 | — | — | — | # Evidence rows | 193 | Retained (REPO-MAP existing rows) / Proposed (skeletons, DEC-09) | 170 | T-463 | §1 row (5) superseded by §7 A-001 (91) + A-004 |
| `06_repositories/repo-skeletons/cdss-library/validator/README.md` | CC-5 | — | — | — | # Validator (B8) | 177 | Retained (REPO-MAP existing rows) / Proposed (skeletons, DEC-09) | 171 | T-464 | §1 row (5) superseded by §7 A-001 (91) + A-004 |
| `06_repositories/repo-skeletons/cdss-llm-lattice/MANIFEST.yaml` | CC-5 | — | — | — | # MANIFEST stub — cdss-llm-lattice (Skeleton, Proposed; format per Arch §10 / Harness manifest discipline) | 614 | Retained (REPO-MAP existing rows) / Proposed (skeletons, DEC-09) | 172 | T-465 | §1 row (5) superseded by §7 A-001 (91) + A-004 |
| `06_repositories/repo-skeletons/cdss-llm-lattice/README.md` | CC-5 | — | — | — | <!-- SKELETON — Proposed (DEC-09; Arch §10 mirrored). No code, build, or deployment is claimed. Every directory README states what its owning primer/annex requi | 1039 | Retained (REPO-MAP existing rows) / Proposed (skeletons, DEC-09) | 173 | T-466 | §1 row (5) superseded by §7 A-001 (91) + A-004 |
| `06_repositories/repo-skeletons/cdss-llm-lattice/ci/pipeline.yml` | CC-5 | — | — | — | # ci/pipeline.yml — STUB (Proposed; not runnable; wired for real in cdss-evalstack imports) | 1085 | Added (sprint-1) — Proposed | 174 | T-467 | §1 row (5) superseded by §7 A-001 (91) + A-004 |
| `06_repositories/repo-skeletons/cdss-lumos/MANIFEST.yaml` | CC-5 | — | — | — | # MANIFEST stub — cdss-lumos (Skeleton, Proposed; format per Arch §10 / Harness manifest discipline) | 585 | Retained (REPO-MAP existing rows) / Proposed (skeletons, DEC-09) | 175 | T-468 | §1 row (5) superseded by §7 A-001 (91) + A-004 |
| `06_repositories/repo-skeletons/cdss-lumos/README.md` | CC-5 | — | — | — | <!-- SKELETON — Proposed (DEC-09; Arch §10 mirrored). No code, build, or deployment is claimed. Every directory README states what its owning primer/annex requi | 782 | Retained (REPO-MAP existing rows) / Proposed (skeletons, DEC-09) | 176 | T-469 | §1 row (5) superseded by §7 A-001 (91) + A-004 |
| `06_repositories/repo-skeletons/cdss-lumos/ci/pipeline.yml` | CC-5 | — | — | — | # ci/pipeline.yml — STUB (Proposed; not runnable; wired for real in cdss-evalstack imports) | 963 | Added (sprint-1) — Proposed | 177 | T-470 | §1 row (5) superseded by §7 A-001 (91) + A-004 |
| `06_repositories/repo-skeletons/cdss-registry/CODEOWNERS` | CC-2 | — | — | — | # Mandated by D8 | 169 | Retained (REPO-MAP existing rows) / Proposed (skeletons, DEC-09) | 178 | T-471 | §1 row (5) superseded by §7 A-001 (91) + A-004 |
| `06_repositories/repo-skeletons/cdss-registry/MANIFEST.yaml` | CC-5 | — | — | — | # MANIFEST stub — cdss-registry (Skeleton, Proposed; format per Arch §10 / Harness manifest discipline) | 570 | Retained (REPO-MAP existing rows) / Proposed (skeletons, DEC-09) | 179 | T-472 | §1 row (5) superseded by §7 A-001 (91) + A-004 |
| `06_repositories/repo-skeletons/cdss-registry/README.md` | CC-5 | — | — | — | <!-- SKELETON — Proposed (DEC-09; Arch §10 mirrored). No code, build, or deployment is claimed. Every directory README states what its owning primer/annex requi | 791 | Retained (REPO-MAP existing rows) / Proposed (skeletons, DEC-09) | 180 | T-473 | §1 row (5) superseded by §7 A-001 (91) + A-004 |
| `06_repositories/repo-skeletons/cdss-registry/ci/pipeline.yml` | CC-5 | — | — | — | # ci/pipeline.yml — STUB (Proposed; not runnable; wired for real in cdss-evalstack imports) | 690 | Retained (REPO-MAP existing rows) / Proposed (skeletons, DEC-09) | 181 | T-474 | §1 row (5) superseded by §7 A-001 (91) + A-004 |
| `06_repositories/repo-skeletons/cdss-registry/policy/README.md` | CC-5 | — | — | — | # Five-gate OPA policy (D8) | 171 | Retained (REPO-MAP existing rows) / Proposed (skeletons, DEC-09) | 182 | T-475 | §1 row (5) superseded by §7 A-001 (91) + A-004 |
| `06_repositories/repo-skeletons/cdss-spine/CODEOWNERS` | CC-2 | — | — | — | # Stub — contract changes require architecture-owner review | 183 | Retained (REPO-MAP existing rows) / Proposed (skeletons, DEC-09) | 183 | T-476 | §1 row (5) superseded by §7 A-001 (91) + A-004 |
| `06_repositories/repo-skeletons/cdss-spine/MANIFEST.yaml` | CC-5 | — | — | — | # MANIFEST stub — cdss-spine (Skeleton, Proposed; format per Arch §10 / Harness manifest discipline) | 750 | Retained (REPO-MAP existing rows) / Proposed (skeletons, DEC-09) | 184 | T-477 | §1 row (5) superseded by §7 A-001 (91) + A-004 |
| `06_repositories/repo-skeletons/cdss-spine/README.md` | CC-5 | — | — | — | <!-- SKELETON — Proposed (DEC-09; Arch §10 mirrored). No code, build, or deployment is claimed. Every directory README states what its owning primer/annex requi | 1089 | Retained (REPO-MAP existing rows) / Proposed (skeletons, DEC-09) | 185 | T-478 | §1 row (5) superseded by §7 A-001 (91) + A-004 |
| `06_repositories/repo-skeletons/cdss-spine/ci/pipeline.yml` | CC-5 | — | — | — | # ci/pipeline.yml — STUB (Proposed; not runnable; wired for real in cdss-evalstack imports) | 717 | Retained (REPO-MAP existing rows) / Proposed (skeletons, DEC-09) | 186 | T-479 | §1 row (5) superseded by §7 A-001 (91) + A-004 |
| `06_repositories/repo-skeletons/cdss-spine/contracts/CONTRACT-ARG-1.pointer.md` | CC-2 | — | — | — | # POINTER STUB — no duplication (Arch §10) | 260 | Retained (REPO-MAP existing rows) / Proposed (skeletons, DEC-09) | 187 | T-480 | §1 row (5) superseded by §7 A-001 (91) + A-004 |
| `06_repositories/repo-skeletons/cdss-spine/contracts/README.md` | CC-5 | — | — | — | # Shared contracts (single home; consumed as cdss-spine@vX) | 576 | Retained (REPO-MAP existing rows) / Proposed (skeletons, DEC-09) | 188 | T-481 | §1 row (5) superseded by §7 A-001 (91) + A-004 |
| `06_repositories/repo-skeletons/cdss-spine/north-star/README.md` | CC-5 | — | — | — | # SPINE-NS-1 (Arch §13.1) | 151 | Retained (REPO-MAP existing rows) / Proposed (skeletons, DEC-09) | 189 | T-482 | §1 row (5) superseded by §7 A-001 (91) + A-004 |
| `06_repositories/repo-skeletons/cdss-spine/registers/README.md` | CC-5 | — | — | — | # Register schemas (register laws §12.1 govern) | 314 | Retained (REPO-MAP existing rows) / Proposed (skeletons, DEC-09) | 190 | T-483 | §1 row (5) superseded by §7 A-001 (91) + A-004 |
| `06_repositories/repo-skeletons/cdss-spine/templates/README.md` | CC-5 | — | — | — | # Templates | 177 | Retained (REPO-MAP existing rows) / Proposed (skeletons, DEC-09) | 191 | T-484 | §1 row (5) superseded by §7 A-001 (91) + A-004 |
| `06_repositories/repo-skeletons/cdss-spine/tolerances/README.md` | CC-5 | — | — | — | # Metric tolerances — versioned configuration | 246 | Retained (REPO-MAP existing rows) / Proposed (skeletons, DEC-09) | 192 | T-485 | §1 row (5) superseded by §7 A-001 (91) + A-004 |
| `06_repositories/repo-skeletons/cdss-spine/validator/README.md` | CC-5 | — | — | — | # validate_build_plan.py wiring (Arch §13.8) | 338 | Retained (REPO-MAP existing rows) / Proposed (skeletons, DEC-09) | 193 | T-486 | §1 row (5) superseded by §7 A-001 (91) + A-004 |
| `06_repositories/repo-skeletons/cdss-ui-clinician/MANIFEST.yaml` | CC-5 | — | — | — | # MANIFEST stub — cdss-ui-clinician (Skeleton, Proposed; format per Arch §10 / Harness manifest discipline) | 553 | Retained (REPO-MAP existing rows) / Proposed (skeletons, DEC-09) | 194 | T-487 | §1 row (5) superseded by §7 A-001 (91) + A-004 |
| `06_repositories/repo-skeletons/cdss-ui-clinician/README.md` | CC-5 | — | — | — | # cdss-ui-clinician (Proposed — DEC-09; skeleton only) | 650 | Retained (REPO-MAP existing rows) / Proposed (skeletons, DEC-09) | 195 | T-488 | §1 row (5) superseded by §7 A-001 (91) + A-004 |
| `06_repositories/repo-skeletons/cdss-ui-clinician/ci/pipeline.yml` | CC-5 | — | — | — | # ci/pipeline.yml — STUB (Proposed; not runnable; wired for real in cdss-evalstack imports) | 653 | Retained (REPO-MAP existing rows) / Proposed (skeletons, DEC-09) | 196 | T-489 | §1 row (5) superseded by §7 A-001 (91) + A-004 |
| `06_repositories/repo-skeletons/cdss-ui-clinician/components/README.md` | CC-5 | — | — | — | # cdss-ui-clinician/components (skeleton stub) | 102 | Retained (REPO-MAP existing rows) / Proposed (skeletons, DEC-09) | 197 | T-490 | §1 row (5) superseded by §7 A-001 (91) + A-004 |
| `06_repositories/repo-skeletons/cdss-ui-clinician/conformance/README.md` | CC-5 | — | — | — | # cdss-ui-clinician/conformance (skeleton stub) | 141 | Retained (REPO-MAP existing rows) / Proposed (skeletons, DEC-09) | 198 | T-491 | §1 row (5) superseded by §7 A-001 (91) + A-004 |
| `06_repositories/repo-skeletons/cdss-ui-clinician/face/README.md` | CC-5 | — | — | — | # cdss-ui-clinician/face (skeleton stub) | 137 | Retained (REPO-MAP existing rows) / Proposed (skeletons, DEC-09) | 199 | T-492 | §1 row (5) superseded by §7 A-001 (91) + A-004 |
| `06_repositories/repo-skeletons/cdss-ui-clinician/tokens/README.md` | CC-5 | — | — | — | # cdss-ui-clinician/tokens (skeleton stub) | 113 | Retained (REPO-MAP existing rows) / Proposed (skeletons, DEC-09) | 200 | T-493 | §1 row (5) superseded by §7 A-001 (91) + A-004 |
| `06_repositories/repo-skeletons/cdss-ui-patient/MANIFEST.yaml` | CC-5 | — | — | — | # MANIFEST stub — cdss-ui-patient (Skeleton, Proposed; format per Arch §10 / Harness manifest discipline) | 549 | Retained (REPO-MAP existing rows) / Proposed (skeletons, DEC-09) | 201 | T-494 | §1 row (5) superseded by §7 A-001 (91) + A-004 |
| `06_repositories/repo-skeletons/cdss-ui-patient/README.md` | CC-5 | — | — | — | # cdss-ui-patient (Proposed — DEC-09; skeleton only; scope Blocked beyond the J-3-safe subset until ASSUME-REG-003 closes) | 629 | Retained (REPO-MAP existing rows) / Proposed (skeletons, DEC-09) | 202 | T-495 | §1 row (5) superseded by §7 A-001 (91) + A-004 |
| `06_repositories/repo-skeletons/cdss-ui-patient/android/README.md` | CC-5 | — | — | — | # cdss-ui-patient/android (skeleton stub) | 164 | Retained (REPO-MAP existing rows) / Proposed (skeletons, DEC-09) | 203 | T-496 | §1 row (5) superseded by §7 A-001 (91) + A-004 |
| `06_repositories/repo-skeletons/cdss-ui-patient/capture/README.md` | CC-5 | — | — | — | # cdss-ui-patient/capture (skeleton stub) | 99 | Retained (REPO-MAP existing rows) / Proposed (skeletons, DEC-09) | 204 | T-497 | §1 row (5) superseded by §7 A-001 (91) + A-004 |
| `06_repositories/repo-skeletons/cdss-ui-patient/ci/pipeline.yml` | CC-5 | — | — | — | # ci/pipeline.yml — STUB (Proposed; not runnable; wired for real in cdss-evalstack imports) | 653 | Retained (REPO-MAP existing rows) / Proposed (skeletons, DEC-09) | 205 | T-498 | §1 row (5) superseded by §7 A-001 (91) + A-004 |
| `06_repositories/repo-skeletons/cdss-ui-patient/components/README.md` | CC-5 | — | — | — | # cdss-ui-patient/components (skeleton stub) | 117 | Retained (REPO-MAP existing rows) / Proposed (skeletons, DEC-09) | 206 | T-499 | §1 row (5) superseded by §7 A-001 (91) + A-004 |
| `06_repositories/repo-skeletons/cdss-ui-patient/face/README.md` | CC-5 | — | — | — | # cdss-ui-patient/face (skeleton stub) | 214 | Retained (REPO-MAP existing rows) / Proposed (skeletons, DEC-09) | 207 | T-500 | §1 row (5) superseded by §7 A-001 (91) + A-004 |

## §4 Known gaps carried until instantiation

- **13 files carry no Proposed/skeleton/stub marker** (contradiction with 00_MANIFEST §7 A-001 "all skeleton files carry Proposed/skeleton banners" — survey-2 BSQ-0393 → DEF-004 in A-004): `06_repositories/repo-skeletons/cdss-compiler/CODEOWNERS`, `06_repositories/repo-skeletons/cdss-engine/properties/README.md`, `06_repositories/repo-skeletons/cdss-engine/tests/README.md`, `06_repositories/repo-skeletons/cdss-graph/tests/README.md`, `06_repositories/repo-skeletons/cdss-integration/lockfile/README.md`, `06_repositories/repo-skeletons/cdss-library/rows/README.md`, `06_repositories/repo-skeletons/cdss-library/validator/README.md`, `06_repositories/repo-skeletons/cdss-registry/CODEOWNERS`, `06_repositories/repo-skeletons/cdss-registry/policy/README.md`, `06_repositories/repo-skeletons/cdss-spine/registers/README.md`, `06_repositories/repo-skeletons/cdss-spine/templates/README.md`, `06_repositories/repo-skeletons/cdss-spine/tolerances/README.md`, `06_repositories/repo-skeletons/cdss-spine/validator/README.md`. Not edited (append-only); the marker lands at instantiation.
- CI stubs: **18/19** trees now carry `ci/pipeline.yml` (six added in sprint-1 — BSQ-0392: evalstack, governance, harness, llm-lattice, lumos, integration); the remaining tree without one is `cdss-corpus`, intentionally minimal (firewall).
- REPO-MAP's skeleton-index paragraph claims "all 14 existing repos (README + MANIFEST.yaml stub + CI stub + per-directory stubs…)": per-directory stubs are absent in coder, conformal, corpus, governance, harness, llm-lattice, lumos (root files only) — the claim over-reaches; recorded here, REPO-MAP v2 unedited.
- **cdss-compiler has no owning primer** in 02_ or 03_ and no launch prompt in 11_ (BSQ-0391) — EXECUTABLE-AFTER-DECISION (DEC-09 repo + prefix CMP; DEC-13 namespace).
- RUN-REPORT R6 (03_/butterfly-primers/RUN-REPORT.md l.256) proposes `cdss-fuzzy`, `cdss-meta`, `cdss-ui-auditor`, `cdss-infra`, `cdss-dataplane` and PFX additions {FUZ, MRL, CEC (+CMP), ABC, LEG, ANT}; REPO-MAP v2 (2026-09-01) predates it — REPO-MAP v3 after DEC-09 (BSQ-0394).
- `GPP-CHANNEL.md` is cited by basename only in REPO-MAP l.30 (resolves to `repo-skeletons/cdss-integration/GPP-CHANNEL.md`).

## §5 Honesty line and self-audit

No code, build or deployment is claimed anywhere in this folder (`find 06_repositories -name '*.py' -o -name '*.ts' -o -name '*.java'` → none, 2026-09-05). Every skeleton is Proposed; owners are `[NEEDS DEFINITION]` (DEC-09).

- Tree rows = `ls repo-skeletons` = 19 — PASS; REPO-MAP rows (14 existing + 4 proposed + cdss-integration; GPP = file, not tree) ↔ trees — PASS (19 ↔ 19).
- Skeleton files on disk = 96 = file rows — PASS (`find 06_repositories/repo-skeletons -type f ! -name .DS_Store | wc -l`).
- Per-file check re-run: 83 conformant, 13 with the banner finding, 0 MANIFEST/CI/CODEOWNERS findings; every CI stub carries the r29 hook (18/18).
- Every path exists; every HARDEN-1.1 row and HARDEN-3.1 task id resolves — PASS.
