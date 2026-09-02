# CENSUS — seven target folders (mechanical)

Produced by `python3 11_prompts/runs/2026-09-02_survey-2/tools/census.py` from repository root on 2026-09-02. Every number below is script output; `.DS_Store` excluded; run directory excluded.

## 1. Per-folder counts vs 00_MANIFEST

| Folder | Declared (source) | On disk | Bytes | Match |
|---|---|---|---|---|
| 04_hardening | 4 (00_MANIFEST §1) | 4 | 26,841 | PASS |
| 05_registers-and-contracts | 5 (00_MANIFEST §1 (4) + §8 (+1 REG-R30.1)) | 5 | 8,796 | PASS |
| 06_repositories | 91 (00_MANIFEST §7 A-001 ('5 files to 91')) | 91 | 48,662 | PASS |
| 07_deployment-and-operations | 5 (00_MANIFEST §1) | 5 | 11,842 | PASS |
| 08_research | 1 (00_MANIFEST §1) | 1 | 3,129 | PASS |
| 09_diagrams | 5 (00_MANIFEST §1) | 5 | 12,753 | PASS |
| 10_regulatory-execution | 7 (00_MANIFEST §8 A-002) | 7 | 121,972 | PASS |

## 2. File list, frontmatter census, declared-vs-counted

Legend: core = doc_id·title·version·date·status present in YAML frontmatter; `—` = not a .md; `NONE` = no frontmatter.

### 04_hardening (4 files, 26,841 B)

| Path | Bytes | Frontmatter core missing | req_prefix / req_count | req blocks counted | Rationale-trace lines | Contents | census | self-audit | placeholders | head-in-lieu |
|---|---|---|---|---|---|---|---|---|---|---|
| `04_hardening/HARDEN-1_coverage_ledger_seed.md` | 3,517 | all present |  /  | 0 | 0 | N | N | N | [NEEDS SOURCE×1, PENDING-VALIDATOR×1, PENDING-ENUMERATION×1 |  |
| `04_hardening/HARDEN-2_hardening_spec.md` | 4,572 | all present |  /  | 0 | 0 | N | Y | N | none |  |
| `04_hardening/HARDEN-3_hardening_plan_worklist.md` | 2,558 | all present |  /  | 0 | 0 | N | N | N | none |  |
| `04_hardening/MAJOR_TASK_2_anti-laziness-hardening-directive.md` | 16,194 | NONE (no frontmatter) |  /  | 0 | 0 | N | N | N | none | # ANTI-LAZINESS DIRECTIVE — EXECUTION-LAYER HARDENING |

### 05_registers-and-contracts (5 files, 8,796 B)

| Path | Bytes | Frontmatter core missing | req_prefix / req_count | req blocks counted | Rationale-trace lines | Contents | census | self-audit | placeholders | head-in-lieu |
|---|---|---|---|---|---|---|---|---|---|---|
| `05_registers-and-contracts/CONTRACT-ARG-1_argument_schema.md` | 2,204 | version, date |  /  | 0 | 0 | N | N | N | none |  |
| `05_registers-and-contracts/REG-R29.schema.json` | 2,048 | — |  /  | 0 | 0 | N | N | N | none | $id=cdss-spine/registers/r29-hardening-coverage-row.schema.json title=R29 Hardening Covera |
| `05_registers-and-contracts/REG-R29_hardening_coverage_ledger.schema.md` | 1,212 | version, date |  /  | 0 | 0 | N | N | N | none |  |
| `05_registers-and-contracts/REG-R30.1_seed_delta.md` | 2,024 | all present |  /  | 0 | 0 | N | N | N | none |  |
| `05_registers-and-contracts/REG-R30_regulatory_posture_register.schema+seed.md` | 1,308 | version, date |  /  | 0 | 0 | N | N | N | none |  |

### 06_repositories (91 files, 48,662 B)

| Path | Bytes | Frontmatter core missing | req_prefix / req_count | req blocks counted | Rationale-trace lines | Contents | census | self-audit | placeholders | head-in-lieu |
|---|---|---|---|---|---|---|---|---|---|---|
| `06_repositories/REPO-MAP_v2.md` | 4,322 | version, date |  /  | 0 | 0 | N | Y | N | none |  |
| `06_repositories/repo-skeletons/cdss-coder/MANIFEST.yaml` | 605 | — |  /  | 0 | 0 | N | N | N | none | # MANIFEST stub — cdss-coder (Skeleton, Proposed; format per Arch §10 / Harness manifest d |
| `06_repositories/repo-skeletons/cdss-coder/README.md` | 955 | NONE (no frontmatter) |  /  | 0 | 0 | N | N | N | none | <!-- SKELETON — Proposed (DEC-09; Arch §10 mirrored). No code, build, or deployment is cla |
| `06_repositories/repo-skeletons/cdss-coder/ci/pipeline.yml` | 711 | — |  /  | 0 | 0 | N | N | N | none | # ci/pipeline.yml — STUB (Proposed; not runnable; wired for real in cdss-evalstack imports |
| `06_repositories/repo-skeletons/cdss-compiler/CODEOWNERS` | 130 | — |  /  | 0 | 0 | N | N | N | none |  |
| `06_repositories/repo-skeletons/cdss-compiler/MANIFEST.yaml` | 545 | — |  /  | 0 | 0 | N | N | N | none | # MANIFEST stub — cdss-compiler (Skeleton, Proposed; format per Arch §10 / Harness manifes |
| `06_repositories/repo-skeletons/cdss-compiler/README.md` | 832 | NONE (no frontmatter) |  /  | 0 | 0 | N | N | N | none | # cdss-compiler (Proposed — DEC-09; skeleton only) |
| `06_repositories/repo-skeletons/cdss-compiler/assist/README.md` | 163 | NONE (no frontmatter) |  /  | 0 | 0 | N | N | N | none | # cdss-compiler/assist (skeleton stub) |
| `06_repositories/repo-skeletons/cdss-compiler/bundles/README.md` | 132 | NONE (no frontmatter) |  /  | 0 | 0 | N | N | N | none | # cdss-compiler/bundles (skeleton stub) |
| `06_repositories/repo-skeletons/cdss-compiler/ci/pipeline.yml` | 653 | — |  /  | 0 | 0 | N | N | N | none | # ci/pipeline.yml — STUB (Proposed; not runnable; wired for real in cdss-evalstack imports |
| `06_repositories/repo-skeletons/cdss-compiler/lift/README.md` | 153 | NONE (no frontmatter) |  /  | 0 | 0 | N | N | N | none | # cdss-compiler/lift (skeleton stub) |
| `06_repositories/repo-skeletons/cdss-compiler/sources/README.md` | 97 | NONE (no frontmatter) |  /  | 0 | 0 | N | N | N | none | # cdss-compiler/sources (skeleton stub) |
| `06_repositories/repo-skeletons/cdss-compiler/tests/README.md` | 147 | NONE (no frontmatter) |  /  | 0 | 0 | N | N | N | none | # cdss-compiler/tests (skeleton stub) |
| `06_repositories/repo-skeletons/cdss-conformal/MANIFEST.yaml` | 572 | — |  /  | 0 | 0 | N | N | N | none | # MANIFEST stub — cdss-conformal (Skeleton, Proposed; format per Arch §10 / Harness manife |
| `06_repositories/repo-skeletons/cdss-conformal/README.md` | 702 | NONE (no frontmatter) |  /  | 0 | 0 | N | N | N | none | <!-- SKELETON — Proposed (DEC-09; Arch §10 mirrored). No code, build, or deployment is cla |
| `06_repositories/repo-skeletons/cdss-conformal/ci/pipeline.yml` | 734 | — |  /  | 0 | 0 | N | N | N | none | # ci/pipeline.yml — STUB (Proposed; not runnable; wired for real in cdss-evalstack imports |
| `06_repositories/repo-skeletons/cdss-corpus/MANIFEST.yaml` | 657 | — |  /  | 0 | 0 | N | N | N | none | # MANIFEST stub — cdss-corpus (Skeleton, Proposed; format per Arch §10 / Harness manifest  |
| `06_repositories/repo-skeletons/cdss-corpus/README.md` | 1,038 | NONE (no frontmatter) |  /  | 0 | 0 | N | N | N | none | <!-- SKELETON — Proposed (DEC-09; Arch §10 mirrored). No code, build, or deployment is cla |
| `06_repositories/repo-skeletons/cdss-corruption/MANIFEST.yaml` | 595 | — |  /  | 0 | 0 | N | N | N | none | # MANIFEST stub — cdss-corruption (Skeleton, Proposed; format per Arch §10 / Harness manif |
| `06_repositories/repo-skeletons/cdss-corruption/README.md` | 891 | NONE (no frontmatter) |  /  | 0 | 0 | N | N | N | none | <!-- SKELETON — Proposed (DEC-09; Arch §10 mirrored). No code, build, or deployment is cla |
| `06_repositories/repo-skeletons/cdss-corruption/ci/pipeline.yml` | 739 | — |  /  | 0 | 0 | N | N | N | none | # ci/pipeline.yml — STUB (Proposed; not runnable; wired for real in cdss-evalstack imports |
| `06_repositories/repo-skeletons/cdss-corruption/rulebook/README.md` | 273 | NONE (no frontmatter) |  /  | 0 | 0 | N | N | N | none | # Rulebook (R8) |
| `06_repositories/repo-skeletons/cdss-engine/MANIFEST.yaml` | 620 | — |  /  | 0 | 0 | N | N | N | none | # MANIFEST stub — cdss-engine (Skeleton, Proposed; format per Arch §10 / Harness manifest  |
| `06_repositories/repo-skeletons/cdss-engine/README.md` | 867 | NONE (no frontmatter) |  /  | 0 | 0 | N | N | N | none | <!-- SKELETON — Proposed (DEC-09; Arch §10 mirrored). No code, build, or deployment is cla |
| `06_repositories/repo-skeletons/cdss-engine/ci/pipeline.yml` | 700 | — |  /  | 0 | 0 | N | N | N | none | # ci/pipeline.yml — STUB (Proposed; not runnable; wired for real in cdss-evalstack imports |
| `06_repositories/repo-skeletons/cdss-engine/properties/README.md` | 155 | NONE (no frontmatter) |  /  | 0 | 0 | N | N | N | none | # Property suite (I mechanism 1) |
| `06_repositories/repo-skeletons/cdss-engine/service/README.md` | 203 | NONE (no frontmatter) |  /  | 0 | 0 | N | N | N | none | # Engine service (stub) |
| `06_repositories/repo-skeletons/cdss-engine/tests/README.md` | 222 | NONE (no frontmatter) |  /  | 0 | 0 | N | N | N | none | # Acceptance (from A10 + DEPLOY-2) |
| `06_repositories/repo-skeletons/cdss-evalstack/MANIFEST.yaml` | 597 | — |  /  | 0 | 0 | N | N | N | none | # MANIFEST stub — cdss-evalstack (Skeleton, Proposed; format per Arch §10 / Harness manife |
| `06_repositories/repo-skeletons/cdss-evalstack/README.md` | 928 | NONE (no frontmatter) |  /  | 0 | 0 | N | N | N | none | <!-- SKELETON — Proposed (DEC-09; Arch §10 mirrored). No code, build, or deployment is cla |
| `06_repositories/repo-skeletons/cdss-evalstack/pipelines/README.md` | 253 | NONE (no frontmatter) |  /  | 0 | 0 | N | N | N | none | # Shared pipeline definitions |
| `06_repositories/repo-skeletons/cdss-fabric/MANIFEST.yaml` | 541 | — |  /  | 0 | 0 | N | N | N | none | # MANIFEST stub — cdss-fabric (Skeleton, Proposed; format per Arch §10 / Harness manifest  |
| `06_repositories/repo-skeletons/cdss-fabric/README.md` | 1,023 | NONE (no frontmatter) |  /  | 0 | 0 | N | N | N | none | # cdss-fabric (Proposed — DEC-09; skeleton only, no code claimed) |
| `06_repositories/repo-skeletons/cdss-fabric/ci/pipeline.yml` | 653 | — |  /  | 0 | 0 | N | N | N | none | # ci/pipeline.yml — STUB (Proposed; not runnable; wired for real in cdss-evalstack imports |
| `06_repositories/repo-skeletons/cdss-fabric/deviation/README.md` | 129 | NONE (no frontmatter) |  /  | 0 | 0 | N | N | N | none | # cdss-fabric/deviation (skeleton stub) |
| `06_repositories/repo-skeletons/cdss-fabric/ledger/README.md` | 126 | NONE (no frontmatter) |  /  | 0 | 0 | N | N | N | none | # cdss-fabric/ledger (skeleton stub) |
| `06_repositories/repo-skeletons/cdss-fabric/projector/README.md` | 140 | NONE (no frontmatter) |  /  | 0 | 0 | N | N | N | none | # cdss-fabric/projector (skeleton stub) |
| `06_repositories/repo-skeletons/cdss-fabric/service/README.md` | 195 | NONE (no frontmatter) |  /  | 0 | 0 | N | N | N | none | # cdss-fabric/service (skeleton stub) |
| `06_repositories/repo-skeletons/cdss-fabric/tests/README.md` | 159 | NONE (no frontmatter) |  /  | 0 | 0 | N | N | N | none | # cdss-fabric/tests (skeleton stub) |
| `06_repositories/repo-skeletons/cdss-governance/MANIFEST.yaml` | 622 | — |  /  | 0 | 0 | N | Y | N | none | # MANIFEST stub — cdss-governance (Skeleton, Proposed; format per Arch §10 / Harness manif |
| `06_repositories/repo-skeletons/cdss-governance/README.md` | 847 | NONE (no frontmatter) |  /  | 0 | 0 | N | Y | N | none | <!-- SKELETON — Proposed (DEC-09; Arch §10 mirrored). No code, build, or deployment is cla |
| `06_repositories/repo-skeletons/cdss-graph/MANIFEST.yaml` | 625 | — |  /  | 0 | 0 | N | N | N | none | # MANIFEST stub — cdss-graph (Skeleton, Proposed; format per Arch §10 / Harness manifest d |
| `06_repositories/repo-skeletons/cdss-graph/README.md` | 731 | NONE (no frontmatter) |  /  | 0 | 0 | N | N | N | none | <!-- SKELETON — Proposed (DEC-09; Arch §10 mirrored). No code, build, or deployment is cla |
| `06_repositories/repo-skeletons/cdss-graph/ci/pipeline.yml` | 730 | — |  /  | 0 | 0 | N | N | N | none | # ci/pipeline.yml — STUB (Proposed; not runnable; wired for real in cdss-evalstack imports |
| `06_repositories/repo-skeletons/cdss-graph/tests/README.md` | 221 | NONE (no frontmatter) |  /  | 0 | 0 | N | N | N | none | # Acceptance |
| `06_repositories/repo-skeletons/cdss-harness/MANIFEST.yaml` | 619 | — |  /  | 0 | 0 | N | Y | N | none | # MANIFEST stub — cdss-harness (Skeleton, Proposed; format per Arch §10 / Harness manifest |
| `06_repositories/repo-skeletons/cdss-harness/README.md` | 914 | NONE (no frontmatter) |  /  | 0 | 0 | N | N | N | none | <!-- SKELETON — Proposed (DEC-09; Arch §10 mirrored). No code, build, or deployment is cla |
| `06_repositories/repo-skeletons/cdss-integration/GPP-CHANNEL.md` | 815 | NONE (no frontmatter) |  /  | 0 | 0 | N | N | N | none | # GPP release channel (Proposed — MAK-J3 v0.9; DEC-06 ratifies) |
| `06_repositories/repo-skeletons/cdss-integration/MANIFEST.yaml` | 603 | — |  /  | 0 | 0 | N | N | N | none | # MANIFEST stub — cdss-integration (Skeleton, Proposed; format per Arch §10 / Harness mani |
| `06_repositories/repo-skeletons/cdss-integration/README.md` | 1,039 | NONE (no frontmatter) |  /  | 0 | 0 | N | N | N | none | <!-- SKELETON — Proposed (DEC-09; Arch §10 mirrored). No code, build, or deployment is cla |
| `06_repositories/repo-skeletons/cdss-integration/lockfile/README.md` | 207 | NONE (no frontmatter) |  /  | 0 | 0 | N | N | N | none | # Integration lockfile |
| `06_repositories/repo-skeletons/cdss-library/CODEOWNERS` | 110 | — |  /  | 0 | 0 | N | N | N | none |  |
| `06_repositories/repo-skeletons/cdss-library/MANIFEST.yaml` | 609 | — |  /  | 0 | 0 | N | N | N | none | # MANIFEST stub — cdss-library (Skeleton, Proposed; format per Arch §10 / Harness manifest |
| `06_repositories/repo-skeletons/cdss-library/README.md` | 753 | NONE (no frontmatter) |  /  | 0 | 0 | N | N | N | none | <!-- SKELETON — Proposed (DEC-09; Arch §10 mirrored). No code, build, or deployment is cla |
| `06_repositories/repo-skeletons/cdss-library/ci/pipeline.yml` | 704 | — |  /  | 0 | 0 | N | N | N | none | # ci/pipeline.yml — STUB (Proposed; not runnable; wired for real in cdss-evalstack imports |
| `06_repositories/repo-skeletons/cdss-library/rows/README.md` | 193 | NONE (no frontmatter) |  /  | 0 | 0 | N | N | N | none | # Evidence rows |
| `06_repositories/repo-skeletons/cdss-library/validator/README.md` | 177 | NONE (no frontmatter) |  /  | 0 | 0 | N | N | N | none | # Validator (B8) |
| `06_repositories/repo-skeletons/cdss-llm-lattice/MANIFEST.yaml` | 614 | — |  /  | 0 | 0 | N | N | N | none | # MANIFEST stub — cdss-llm-lattice (Skeleton, Proposed; format per Arch §10 / Harness mani |
| `06_repositories/repo-skeletons/cdss-llm-lattice/README.md` | 1,039 | NONE (no frontmatter) |  /  | 0 | 0 | N | N | N | none | <!-- SKELETON — Proposed (DEC-09; Arch §10 mirrored). No code, build, or deployment is cla |
| `06_repositories/repo-skeletons/cdss-lumos/MANIFEST.yaml` | 585 | — |  /  | 0 | 0 | N | N | N | none | # MANIFEST stub — cdss-lumos (Skeleton, Proposed; format per Arch §10 / Harness manifest d |
| `06_repositories/repo-skeletons/cdss-lumos/README.md` | 782 | NONE (no frontmatter) |  /  | 0 | 0 | N | N | N | none | <!-- SKELETON — Proposed (DEC-09; Arch §10 mirrored). No code, build, or deployment is cla |
| `06_repositories/repo-skeletons/cdss-registry/CODEOWNERS` | 169 | — |  /  | 0 | 0 | N | N | N | none |  |
| `06_repositories/repo-skeletons/cdss-registry/MANIFEST.yaml` | 570 | — |  /  | 0 | 0 | N | N | N | none | # MANIFEST stub — cdss-registry (Skeleton, Proposed; format per Arch §10 / Harness manifes |
| `06_repositories/repo-skeletons/cdss-registry/README.md` | 791 | NONE (no frontmatter) |  /  | 0 | 0 | N | N | N | none | <!-- SKELETON — Proposed (DEC-09; Arch §10 mirrored). No code, build, or deployment is cla |
| `06_repositories/repo-skeletons/cdss-registry/ci/pipeline.yml` | 690 | — |  /  | 0 | 0 | N | N | N | none | # ci/pipeline.yml — STUB (Proposed; not runnable; wired for real in cdss-evalstack imports |
| `06_repositories/repo-skeletons/cdss-registry/policy/README.md` | 171 | NONE (no frontmatter) |  /  | 0 | 0 | N | N | N | none | # Five-gate OPA policy (D8) |
| `06_repositories/repo-skeletons/cdss-spine/CODEOWNERS` | 183 | — |  /  | 0 | 0 | N | N | N | none |  |
| `06_repositories/repo-skeletons/cdss-spine/MANIFEST.yaml` | 750 | — |  /  | 0 | 0 | N | N | N | none | # MANIFEST stub — cdss-spine (Skeleton, Proposed; format per Arch §10 / Harness manifest d |
| `06_repositories/repo-skeletons/cdss-spine/README.md` | 1,089 | NONE (no frontmatter) |  /  | 0 | 0 | N | N | N | none | <!-- SKELETON — Proposed (DEC-09; Arch §10 mirrored). No code, build, or deployment is cla |
| `06_repositories/repo-skeletons/cdss-spine/ci/pipeline.yml` | 717 | — |  /  | 0 | 0 | N | N | N | none | # ci/pipeline.yml — STUB (Proposed; not runnable; wired for real in cdss-evalstack imports |
| `06_repositories/repo-skeletons/cdss-spine/contracts/CONTRACT-ARG-1.pointer.md` | 260 | NONE (no frontmatter) |  /  | 0 | 0 | N | N | N | none | # POINTER STUB — no duplication (Arch §10) |
| `06_repositories/repo-skeletons/cdss-spine/contracts/README.md` | 576 | NONE (no frontmatter) |  /  | 0 | 0 | N | N | N | none | # Shared contracts (single home; consumed as cdss-spine@vX) |
| `06_repositories/repo-skeletons/cdss-spine/north-star/README.md` | 151 | NONE (no frontmatter) |  /  | 0 | 0 | N | N | N | none | # SPINE-NS-1 (Arch §13.1) |
| `06_repositories/repo-skeletons/cdss-spine/registers/README.md` | 314 | NONE (no frontmatter) |  /  | 0 | 0 | N | N | N | [NEEDS SOURCE×1 | # Register schemas (register laws §12.1 govern) |
| `06_repositories/repo-skeletons/cdss-spine/templates/README.md` | 177 | NONE (no frontmatter) |  /  | 0 | 0 | N | N | N | none | # Templates |
| `06_repositories/repo-skeletons/cdss-spine/tolerances/README.md` | 246 | NONE (no frontmatter) |  /  | 0 | 0 | N | N | N | none | # Metric tolerances — versioned configuration |
| `06_repositories/repo-skeletons/cdss-spine/validator/README.md` | 338 | NONE (no frontmatter) |  /  | 0 | 0 | N | N | N | [NEEDS SOURCE×1, PENDING-VALIDATOR×1 | # validate_build_plan.py wiring (Arch §13.8) |
| `06_repositories/repo-skeletons/cdss-ui-clinician/MANIFEST.yaml` | 553 | — |  /  | 0 | 0 | N | N | N | none | # MANIFEST stub — cdss-ui-clinician (Skeleton, Proposed; format per Arch §10 / Harness man |
| `06_repositories/repo-skeletons/cdss-ui-clinician/README.md` | 650 | NONE (no frontmatter) |  /  | 0 | 0 | N | N | N | none | # cdss-ui-clinician (Proposed — DEC-09; skeleton only) |
| `06_repositories/repo-skeletons/cdss-ui-clinician/ci/pipeline.yml` | 653 | — |  /  | 0 | 0 | N | N | N | none | # ci/pipeline.yml — STUB (Proposed; not runnable; wired for real in cdss-evalstack imports |
| `06_repositories/repo-skeletons/cdss-ui-clinician/components/README.md` | 102 | NONE (no frontmatter) |  /  | 0 | 0 | N | N | N | none | # cdss-ui-clinician/components (skeleton stub) |
| `06_repositories/repo-skeletons/cdss-ui-clinician/conformance/README.md` | 141 | NONE (no frontmatter) |  /  | 0 | 0 | N | N | N | none | # cdss-ui-clinician/conformance (skeleton stub) |
| `06_repositories/repo-skeletons/cdss-ui-clinician/face/README.md` | 137 | NONE (no frontmatter) |  /  | 0 | 0 | N | N | N | none | # cdss-ui-clinician/face (skeleton stub) |
| `06_repositories/repo-skeletons/cdss-ui-clinician/tokens/README.md` | 113 | NONE (no frontmatter) |  /  | 0 | 0 | N | N | N | none | # cdss-ui-clinician/tokens (skeleton stub) |
| `06_repositories/repo-skeletons/cdss-ui-patient/MANIFEST.yaml` | 549 | — |  /  | 0 | 0 | N | N | N | none | # MANIFEST stub — cdss-ui-patient (Skeleton, Proposed; format per Arch §10 / Harness manif |
| `06_repositories/repo-skeletons/cdss-ui-patient/README.md` | 629 | NONE (no frontmatter) |  /  | 0 | 0 | N | N | N | none | # cdss-ui-patient (Proposed — DEC-09; skeleton only; scope Blocked beyond the J-3-safe sub |
| `06_repositories/repo-skeletons/cdss-ui-patient/android/README.md` | 164 | NONE (no frontmatter) |  /  | 0 | 0 | N | N | N | none | # cdss-ui-patient/android (skeleton stub) |
| `06_repositories/repo-skeletons/cdss-ui-patient/capture/README.md` | 99 | NONE (no frontmatter) |  /  | 0 | 0 | N | N | N | none | # cdss-ui-patient/capture (skeleton stub) |
| `06_repositories/repo-skeletons/cdss-ui-patient/ci/pipeline.yml` | 653 | — |  /  | 0 | 0 | N | N | N | none | # ci/pipeline.yml — STUB (Proposed; not runnable; wired for real in cdss-evalstack imports |
| `06_repositories/repo-skeletons/cdss-ui-patient/components/README.md` | 117 | NONE (no frontmatter) |  /  | 0 | 0 | N | N | N | none | # cdss-ui-patient/components (skeleton stub) |
| `06_repositories/repo-skeletons/cdss-ui-patient/face/README.md` | 214 | NONE (no frontmatter) |  /  | 0 | 0 | N | N | N | none | # cdss-ui-patient/face (skeleton stub) |

### 07_deployment-and-operations (5 files, 11,842 B)

| Path | Bytes | Frontmatter core missing | req_prefix / req_count | req blocks counted | Rationale-trace lines | Contents | census | self-audit | placeholders | head-in-lieu |
|---|---|---|---|---|---|---|---|---|---|---|
| `07_deployment-and-operations/DEPLOY-1_deployment_plan_and_sequencing.md` | 3,805 | date |  /  | 0 | 0 | N | Y | N | [NEEDS DEFINITION×1 |  |
| `07_deployment-and-operations/DEPLOY-2_testing_verification_acceptance.md` | 1,839 | date |  /  | 0 | 0 | N | N | N | none |  |
| `07_deployment-and-operations/GOV-1_ownership_governance_postdeploy.md` | 1,518 | date |  /  | 0 | 0 | N | N | N | [NEEDS DEFINITION×4 |  |
| `07_deployment-and-operations/OPS-1_operating_procedures.md` | 2,475 | date |  /  | 0 | 0 | N | Y | N | none |  |
| `07_deployment-and-operations/SEC-1_security_privacy_compliance.md` | 2,205 | date |  /  | 0 | 0 | N | N | N | none |  |

### 08_research (1 files, 3,129 B)

| Path | Bytes | Frontmatter core missing | req_prefix / req_count | req blocks counted | Rationale-trace lines | Contents | census | self-audit | placeholders | head-in-lieu |
|---|---|---|---|---|---|---|---|---|---|---|
| `08_research/RESEARCH-1_findings_gaps_source_map.md` | 3,129 | status |  /  | 0 | 0 | N | N | N | none |  |

### 09_diagrams (5 files, 12,753 B)

| Path | Bytes | Frontmatter core missing | req_prefix / req_count | req blocks counted | Rationale-trace lines | Contents | census | self-audit | placeholders | head-in-lieu |
|---|---|---|---|---|---|---|---|---|---|---|
| `09_diagrams/cdss_diagrams_v2.html` | 7,219 | — |  /  | 0 | 0 | N | Y | N | none | <!DOCTYPE html> |
| `09_diagrams/deployment_ladders.mermaid` | 1,283 | — |  /  | 0 | 0 | N | N | N | none | %% IMAGO-4 — Three ladders interleaved (DEPLOY-1). Status: Proposed |
| `09_diagrams/imago_architecture.mermaid` | 1,862 | — |  /  | 0 | 0 | N | N | N | none | %% IMAGO-1 — Merged (imago) architecture: fabric wraps the release spine. Status: Proposed |
| `09_diagrams/merged_runtime_sequence.mermaid` | 1,099 | — |  /  | 0 | 0 | N | N | N | none | %% IMAGO-2 — One consultation under the fabric (Primer 0 §4 successor). Status: Proposed |
| `09_diagrams/register_topology_v2.mermaid` | 1,290 | — |  /  | 0 | 0 | N | Y | N | none | %% IMAGO-3 — Register topology with proposed additions. R1–R28 Existing/Ratified (Arch §12 |

### 10_regulatory-execution (7 files, 121,972 B)

| Path | Bytes | Frontmatter core missing | req_prefix / req_count | req blocks counted | Rationale-trace lines | Contents | census | self-audit | placeholders | head-in-lieu |
|---|---|---|---|---|---|---|---|---|---|---|
| `10_regulatory-execution/EXEC-1_execution_directive.md` | 11,180 | all present | EX / 10 | 10 | 10 | N | Y | Y | none |  |
| `10_regulatory-execution/FOLD-1_antennae_fold_worklist.md` | 2,799 | all present |  /  | 0 | 0 | N | N | N | [NEEDS DEFINITION×1 |  |
| `10_regulatory-execution/MAK-GOV_addendum-g_v0.9.md` | 17,124 | all present | NDG / 14 | 14 | 14 | N | N | N | none |  |
| `10_regulatory-execution/REG-NZ_v1.0.md` | 13,194 | date |  /  | 0 | 0 | N | N | N | none |  |
| `10_regulatory-execution/REG-POSTURE_v1.1.md` | 60,793 | date |  /  | 0 | 0 | N | Y | Y | [NEEDS DEFINITION×1 |  |
| `10_regulatory-execution/REG-SPRINT-1.1_delta.md` | 6,141 | date |  /  | 0 | 0 | N | N | N | none |  |
| `10_regulatory-execution/REG-SPRINT_v1.0.md` | 10,741 | date |  /  | 0 | 0 | N | N | N | none |  |

## 3. ID census — cited-but-undefined candidates (DANGLING-REF candidates; confirmed manually in Phase 1 step 3)

- `04_hardening/HARDEN-1_coverage_ledger_seed.md`: A-001
- `04_hardening/HARDEN-3_hardening_plan_worklist.md`: T-000, T-004, T-005, T-010, T-011, T-020, T-021, T-110, T-120, T-121, T-122, T-130, T-131, T-132
- `05_registers-and-contracts/REG-R30.1_seed_delta.md`: NZ-ASSUME-005, SG-V2-0
- `10_regulatory-execution/EXEC-1_execution_directive.md`: A-001, A-002, NZ-ASSUME-005, SG-V1-2, SG-V2-2
- `10_regulatory-execution/FOLD-1_antennae_fold_worklist.md`: A-002, NZ-ASSUME-005
- `10_regulatory-execution/MAK-GOV_addendum-g_v0.9.md`: REG-FIND-013, TASK-REG-023
- `10_regulatory-execution/REG-SPRINT-1.1_delta.md`: SG-V1-1, SG-V1-2, SG-V2-2
- `10_regulatory-execution/REG-SPRINT_v1.0.md`: SG-V1-1, SG-V1-2, SG-V2-0, SG-V2-1, SG-V2-2, SG-V2-3

## 4. IDs defined in target files (heading / first-cell / list / range positions)

- `04_hardening/HARDEN-2_hardening_spec.md` defines: CC-1, CC-2, CC-3, CC-4, CC-5, CC-6, CC-7, CC-8 (8)
- `04_hardening/HARDEN-3_hardening_plan_worklist.md` defines: T-001, T-002, T-003, T-030, T-031, T-032, T-033, T-034, T-035, T-036, T-037, T-038, T-039, T-040, T-041, T-042, T-043, T-044, T-045, T-050, T-051, T-052, T-053, T-054, T-055, T-056, T-057, T-058, T-059, T-060, T-061, T-062, T-070, T-071, T-072, T-080, T-081, T-082, T-083, T-084, T-085, T-086, T-087, T-088, T-089, T-090, T-091, T-092, T-093, T-094, T-095, T-100, T-101, T-102, T-103, T-104, T-105, T-106, T-107, W0 … (71)
- `05_registers-and-contracts/REG-R29.schema.json` defines: CC-1 (1)
- `05_registers-and-contracts/REG-R30.1_seed_delta.md` defines: ASSUME-REG-008, NDG-1, NZ-ASSUME-001, NZ-ASSUME-002, NZ-ASSUME-003, NZ-ASSUME-004, NZ-FIND-001, NZ-FIND-002, NZ-FIND-003, NZ-FIND-004, NZ-FIND-005, NZ-FIND-006, NZ-FIND-007, NZ-FIND-008, NZ-FIND-009, NZ-OBL-001, NZ-OBL-002, NZ-OBL-003, NZ-OBL-004, NZ-OBL-005, NZ-OBL-006, NZ-OBL-007, NZ-OBL-008, NZ-OBL-009, NZ-OBL-010, NZ-Q-001, NZ-Q-002, NZ-Q-003, NZ-Q-004, NZ-TASK-001, NZ-TASK-002, NZ-TASK-003, NZ-TASK-004, NZ-TASK-005, NZ-TASK-006, NZ-TASK-007, NZ-TASK-008, OBL-013, OBL-014, Q-REG-008, Q-REG-009, Q-REG-010, R30, REG-FIND-009, REG-FIND-010, REG-FIND-011, SD-01, SD-02, SD-03, SD-04, SD-05, SRC-REG-011, SRC-REG-012, SRC-REG-013, SRC-REG-014, TASK-REG-021, TASK-REG-022, WATCH-REG-006 (58)
- `05_registers-and-contracts/REG-R30_regulatory_posture_register.schema+seed.md` defines: ASSUME-REG-001, ASSUME-REG-002, ASSUME-REG-003, ASSUME-REG-004, ASSUME-REG-005, ASSUME-REG-006, ASSUME-REG-007, GATE-000, GATE-001, GATE-002, GATE-003, GATE-004, Q-REG-001, Q-REG-002, Q-REG-003, Q-REG-004, Q-REG-005, Q-REG-006, Q-REG-007, REG-FIND-001, REG-FIND-002, REG-FIND-003, REG-FIND-004, REG-FIND-005, REG-FIND-006, REG-FIND-007, REG-FIND-008, REG-KEEP-001, REG-KEEP-002, REG-KEEP-003, REG-KEEP-004, TASK-REG-001, TASK-REG-002, TASK-REG-003, TASK-REG-004, TASK-REG-005, TASK-REG-006, TASK-REG-007, TASK-REG-008, TASK-REG-009, TASK-REG-010, TASK-REG-011, TASK-REG-012, TASK-REG-013, TASK-REG-014, TASK-REG-015, TASK-REG-016, TASK-REG-017, TASK-REG-018, TASK-REG-019, TASK-REG-020 (51)
- `06_repositories/repo-skeletons/cdss-spine/registers/README.md` defines: R1 (1)
- `07_deployment-and-operations/GOV-1_ownership_governance_postdeploy.md` defines: WATCH-REG-001, WATCH-REG-002, WATCH-REG-003, WATCH-REG-004, WATCH-REG-005 (5)
- `08_research/RESEARCH-1_findings_gaps_source_map.md` defines: RG-01, RG-02, RG-03, RG-04, RG-05, RG-06, SRC-REG-001, SRC-REG-002, SRC-REG-003, SRC-REG-004 (10)
- `09_diagrams/cdss_diagrams_v2.html` defines: R28, R29, R30 (3)
- `09_diagrams/register_topology_v2.mermaid` defines: R28, R29, R30 (3)
- `10_regulatory-execution/EXEC-1_execution_directive.md` defines: EX-1, EX-10, EX-2, EX-3, EX-4, EX-5, EX-6, EX-7, EX-8, EX-9, NZ-ASSUME-001, NZ-ASSUME-002, NZ-ASSUME-003, RUN-0, RUN-1, RUN-2, RUN-3, RUN-4, TASK-REG-010, TASK-REG-011, TASK-REG-012, TASK-REG-013, TASK-REG-014, TASK-REG-015, TASK-REG-016, TASK-REG-017, TASK-REG-018 (27)
- `10_regulatory-execution/FOLD-1_antennae_fold_worklist.md` defines: NZ-WATCH-001, NZ-WATCH-002, NZ-WATCH-003, W1, W2, W3, W4, W5 (8)
- `10_regulatory-execution/MAK-GOV_addendum-g_v0.9.md` defines: NDG-1, NDG-10, NDG-11, NDG-12, NDG-13, NDG-14, NDG-2, NDG-3, NDG-4, NDG-5, NDG-6, NDG-7, NDG-8, NDG-9 (14)
- `10_regulatory-execution/REG-NZ_v1.0.md` defines: NZ-ASSUME-001, NZ-ASSUME-002, NZ-ASSUME-003, NZ-ASSUME-004, NZ-FIND-001, NZ-FIND-002, NZ-FIND-003, NZ-FIND-004, NZ-FIND-005, NZ-FIND-006, NZ-FIND-007, NZ-FIND-008, NZ-FIND-009, NZ-Q-001, NZ-Q-002, NZ-Q-003, NZ-TASK-001, NZ-TASK-002, NZ-TASK-003, NZ-TASK-004, NZ-TASK-005, NZ-TASK-006, NZ-TASK-007, NZ-TASK-008, STD-001, STD-002, STD-003, STD-004, STD-005, STD-006, STD-007, STD-008, STD-009, STD-010, STD-011, STD-012, STD-013, TASK-REG-006, TASK-REG-007, TASK-REG-008, TASK-REG-009, TASK-REG-010, TASK-REG-011, TASK-REG-012, TASK-REG-013, TASK-REG-014 (46)
- `10_regulatory-execution/REG-POSTURE_v1.1.md` defines: ASSUME-REG-001, ASSUME-REG-002, ASSUME-REG-003, ASSUME-REG-004, ASSUME-REG-005, ASSUME-REG-006, ASSUME-REG-007, ASSUME-REG-008, GATE-000, GATE-001, GATE-002, GATE-003, GATE-004, KTX-001, KTX-002, KTX-003, KTX-004, KTX-005, KTX-006, KTX-007, KTX-008, KTX-009, KTX-010, KTX-011, KTX-012, OBL-001, OBL-002, OBL-003, OBL-004, OBL-005, OBL-006, OBL-007, OBL-008, OBL-009, OBL-010, OBL-011, OBL-012, OBL-013, OBL-014, Q-REG-001, Q-REG-002, Q-REG-003, Q-REG-004, Q-REG-005, Q-REG-006, Q-REG-007, Q-REG-008, Q-REG-009, R30, REG-FIND-001, REG-FIND-002, REG-FIND-003, REG-FIND-004, REG-FIND-005, REG-FIND-006, REG-FIND-007, REG-FIND-008, REG-FIND-009, REG-FIND-010, REG-FIND-011 … (104)
- `10_regulatory-execution/REG-SPRINT-1.1_delta.md` defines: D-1, D-2, D-3, D-4, D-5, SG-V1-0, V1-C1, V1-C2, V1-S0, V1-S1, V1-S2, V2-S3a, V2-S3b (13)
- `10_regulatory-execution/REG-SPRINT_v1.0.md` defines: V1-S0, V1-S1, V1-S2, V2-E1, V2-E2, V2-E3, V2-E4, V2-E5, V2-S0, V2-S1, V2-S2, V2-S3 (12)

## 5. Manual confirmation of §3 candidates (Phase 1 step 3)
| Candidate | Verdict | Evidence |
|---|---|---|
| A-001, A-002 (HARDEN-1, EXEC-1, FOLD-1) | RESOLVED — defined by heading `# 7. Amendment A-001 …`, `# 8. Amendment A-002 …` in 00_MANIFEST.md (ID not at heading start, so the script missed it) | `grep -n 'Amendment A-00' 00_MANIFEST.md` → l.73, l.77 |
| T-000, T-004, T-005, T-010, T-011, T-020, T-021, T-110, T-120..122, T-130..132 | RESOLVED as *defined mid-cell* in HARDEN-3 wave table; but no per-task row exists anywhere → filed as QUALITY-BELOW-BAR **BSQ-0006** (not DANGLING) | HARDEN-3 l.13–24 |
| NZ-ASSUME-005 (R30.1, EXEC-1, FOLD-1) | RESOLVED — minted in R30.1 l.23 (`**NZ-ASSUME-005 OPEN** (transition-provisions working assumption; owner founder; …`) | `grep -n 'NZ-ASSUME-005' 05_*/REG-R30.1_seed_delta.md` → l.23, l.34 |
| SG-V1-0..2, SG-V2-0..3 (R30.1, EXEC-1, REG-SPRINT, 1.1) | RESOLVED — gate names introduced in the Exit column of REG-SPRINT sprint tables (e.g. l.78 `| \`V1-S1\` | Build… | 4–8 | \`SG-V1-1\`: suite green…`) | `grep -n 'SG-V' 10_*/REG-SPRINT_v1.0.md` |
| REG-FIND-013, TASK-REG-023 (MAK-GOV l.288) | **DANGLING-REF** — forward references to a "REG-POSTURE v1.2" not in the tree; defined nowhere | **BSQ-0001** |

## 6. Reference resolution (Phase 1 step 5) — `tools/refcheck.py` → `refcheck.json`, `refcheck_output.txt`
- path refs checked: 19 · anchor refs checked: 129 · unresolved paths: 15 · resolved-by-basename-only: 1 · unresolved anchors: 2.
- The 15 unresolved paths are all **external or intentional**: agent-skills pack files (`docs/agents.md`, `references/*.md` ×9 incl. `references/definition-of-done.md` cited by MT2 and HARDEN-2) — external repo, never in this tree; `validate_build_plan.py` — lives in `cdss-spine` (Arch §13.8), not here; `antennae-corpus_v1.1.md` — FOLD-1's *future output* (intentional); `observer_adjudication.md` — external repo doc cited by REG-POSTURE; `06_repositories/**` — a glob, not a path. No in-repo path reference is unresolved. Filed as none; recorded here.
- Resolved by basename only: `06_repositories/REPO-MAP_v2.md:30` cites `GPP-CHANNEL.md` without directory; file is `repo-skeletons/cdss-integration/GPP-CHANNEL.md` — cosmetic; noted in folders/06.
- Unresolved anchors: `MT2 §7.4` in `09_diagrams/register_topology_v2.mermaid:17` and `cdss_diagrams_v2.html:96` → **BSQ-0002, BSQ-0003**, and the resulting contradiction with 00_MANIFEST §5 DEF-002 ("residual-notation grep = NONE") → **BSQ-0004**.

## 7. Browser-borne (Phase 1 step 6) — `tools/mermaid/parse.mjs` → `mermaid_parse.json`
Tool: mermaid 10.9.0 via jsdom 24.1.3 (node v22.23.2), installed under `tools/mermaid/node_modules` (run-directory local; 77 MB; `.gitignore`d). Result: 4/4 `.mermaid` sources PASS; 4/4 blocks inlined in `cdss_diagrams_v2.html` PASS (selector `<pre class="mermaid">`). → **BSQ-0005** PRESENT-CONFORMANT.

## 8. Census rows
`census_rows.jsonl`: 6 rows; `.venv/bin/python tools/validate_rows.py BSQ.schema.json census_rows.jsonl` → `rows=6 invalid=0 valid=6`.

## 9. Corrections to the prompt's seeds (confirm-not-assume)
- 06_ carries **91** files excluding `.DS_Store` (the seed's "93" counted two `.DS_Store`). 00_MANIFEST A-001 "91" is exact, not "~91".
- REG-POSTURE / REG-NZ / REG-SPRINT / REG-SPRINT-1.1 carry `date_issued:` rather than `date:` — a field-name variant, recorded as such in Phase 2 (P-D-01 PASS-with-variant), not as a missing date.
