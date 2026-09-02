---
doc_id: REPO-MAP-v2
title: "Repository map — 14 existing + 4 proposed + 1 channel"
status: "Existing rows Retained verbatim in intent from Arch §10; new rows Proposed (DEC-09). Pragmatic-phasing rule retained: spine, corpus, registry are load-bearing from day one; others may begin as folders in one working repo provided manifest discipline holds."
---
| Repo | Primer/volume | Emits | Isolation | Status |
|---|---|---|---|---|
| cdss-spine | Arch | contracts (now incl. ARG/DEV/RRI, R29/R30 schemas), templates, tolerances | consumed by all | Existing+Transformed |
| cdss-engine | A | stateless compute + trace/argument-payload emitter | no clinical numbers of its own | Existing |
| cdss-library | B | data releases + validator | answers to sources, never scores | Existing |
| cdss-corpus | C | checkpoint aggregates only | own account; dev CI credential-free | Existing (firewall untouched) |
| cdss-registry | D | signed fragments + OPA policy (+GPP stamps) | keys never leave | Existing |
| cdss-graph | E | deterministic builds (+rebuttal records, DetectedIssues) | rebuild=f(registry version) | Existing+Transformed |
| cdss-conformal | F | wrapper + calibration reports | pure math, no data retained | Existing |
| cdss-corruption | G | suites (+ARG-class; FZ-5 dormant) + rulebook | clinician-reviewable in isolation | Existing+Transformed |
| cdss-lumos | H | protocol/SAP/rows | no data ever enters | Existing |
| cdss-evalstack | I | pipelines (+R29 ratchet check on ratification) | operates, does not author | Existing+Transformed |
| cdss-governance | J | validator + census (+R30) | runs in every CI | Existing+Transformed |
| cdss-coder | J-1/J-2 | det-coder+dictionary or ml-coder container | fork = release channel | Existing (labels per C-01) |
| cdss-harness | HX | learners/checker/cascade | EVAL-refusing loaders proven here | Existing |
| cdss-llm-lattice | K/L | prompt registry, orchestration, L services | prompt changes are I events | Existing |
| **cdss-fabric** | MAK-FFC/ABC | fabric service, deviation machinery, compliance projector | schemas in spine, never here; ledger per DEC-04 | **Proposed** |
| **cdss-compiler** | EN-3/CP | GenericArgument bundles from CQL/FHIR-CPG/WHO-SMART | outputs via registry gateway | **Proposed** |
| **cdss-ui-clinician** | MAK-LBP/HDC | component library + clinician face | conformance suite = CI acceptance | **Proposed** |
| **cdss-ui-patient** | MAK-PRB/TXC | component library + patient face | beyond J-3-safe subset: Blocked (ASSUME-REG-003) | **Proposed** |
| *(channel)* GPP | MAK-J3 | J-3 build artifact | integration-repo release channel; GPP-14 boundary | **Proposed** |
Stack notes (C-04 reconciliation): AWS topology per Arch §11.4 stands; LS-2 (replayability/single-gate/telemetry/SBOM by construction), LS-3 (bounded polyglot: JVM for CQL/clinical-reasoning/HAPI, Python for MAPIE/pgmpy-class, TypeScript app layer; no clinical logic reimplemented across languages), LS-4 (boring bias; runtime-tech count is a reviewed metric) adopted as MUSTs; L1-2 UI bindings are the frontend acceptance bar.

## Skeleton index (appended — skeletons generated 2026-09-01; every file marked Proposed, no code claimed)
`repo-skeletons/` now carries: all **14 existing repos** (README + MANIFEST.yaml stub + CI stub + per-directory stubs mirroring each primer's §-4/§-8 and this pass's annex), **cdss-integration** (Proposed home for the lockfile — Arch §10: "an integration repo (or the spine itself)"; its ownership of R14 in the Arch §12.2 table supports the standalone home; DEC-09 decides) with `GPP-CHANNEL.md` (the J-3 channel spec: not a repo), and directory trees for the **4 proposed repos**. Doctrinal notes honoured in the skeletons: contracts appear in cdss-spine as **pointer stubs** to the canonical drafts in `05_registers-and-contracts/` (move-never-copy on ratification — "duplication is where drift begins"); the cdss-corpus skeleton is intentionally minimal with a firewall banner (instantiate only in-account; no case structure stubbed dev-side); CODEOWNERS stubs land where the primers mandate them (registry: pharmacist+clinician; library: clinician; compiler bundles: gateway discipline; spine contracts: architecture owner). Every CI stub carries the dormant R29 ratchet hook (activates on DEC-02; MT2 §7(4)).
