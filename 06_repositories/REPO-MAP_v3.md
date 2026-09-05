---
doc_id: REPO-MAP-v3
title: "Repository map v3 — 14 existing + 4 proposed + 1 channel, with the owner column (DEC-09 closed) and the ratified prefix set"
version: "3.0"
date: "2026-09-05"
status: "Added (sprint-2). Successor to REPO-MAP_v2.md (preserved unedited beside this file). Existing rows Retained verbatim in intent from Arch §10; the four proposed repositories and the GPP channel remain Proposed as repositories (none has been created — this repository contains zero production code); what changed is that every row now names its owner (DEC-09, MET-2.2 §3.5) and the PFX set {FAB, UIP, UIC, GPP} is ratified into Arch §13.3 (§14.4 Proposed → ratified). Pragmatic-phasing rule retained."
supersedes: "06_repositories/REPO-MAP_v2.md (retained; v2 text carried verbatim below with two columns appended per row)"
change_policy: "Successor file per the X1 append-only discipline; v2 is never edited"
produced_by: "sprint-2 (MET-2.2 §6 owed file; survey-3 QI-0018 chain) — 11_prompts/runs/2026-09-05_sprint-2/"
---

# Repository map v3

## What v3 adds (and nothing else)

Two columns per repository row: **Owner** — every repository is owned by Kenny-bytes as Programme lead
(DEC-09, closed 2026-09-05); any later per-repository delegation draws from the four accounts named in
MET-2.2 §1. **PFX** — the namespace prefix each repository's ecosystem IDs carry under Arch §13.3, with
the four prefixes DEC-09 ratified marked. The compiler repository has no prefix in the ratified set and
says so ([PENDING-ENUMERATION]) rather than minting one. Every other cell is v2's text, unchanged.

The launch prompts that would open these repositories are indexed in `11_prompts/PROMPT-SERIES_A-L_index.md` (A–L) and `11_prompts/PROMPT-PRM-SERIES_index.md` (the primer series); none has been run against a repository — this map describes intent, not code.

## Repository table (v2 columns + owner + PFX)

| Repo | Primer/volume | Emits | Isolation | Status (v2, retained) | Owner (DEC-09, MET-2.2 §3.5) | PFX (Arch §13.3 + §14.4) |
|---|---|---|---|---|---|---|
| cdss-spine | Arch | contracts (now incl. ARG/DEV/RRI, R29/R30 schemas), templates, tolerances | consumed by all | Existing+Transformed | Kenny-bytes (Programme lead; pool: Kenny-bytes, kendo-Jones, Ken-nough, Ken-E-Gee — MET-2.2 §1) | SPINE |
| cdss-engine | A | stateless compute + trace/argument-payload emitter | no clinical numbers of its own | Existing | Kenny-bytes (Programme lead; pool: Kenny-bytes, kendo-Jones, Ken-nough, Ken-E-Gee — MET-2.2 §1) | A |
| cdss-library | B | data releases + validator | answers to sources, never scores | Existing | Kenny-bytes (Programme lead; pool: Kenny-bytes, kendo-Jones, Ken-nough, Ken-E-Gee — MET-2.2 §1) | B |
| cdss-corpus | C | checkpoint aggregates only | own account; dev CI credential-free | Existing (firewall untouched) | Kenny-bytes (Programme lead; pool: Kenny-bytes, kendo-Jones, Ken-nough, Ken-E-Gee — MET-2.2 §1) | C |
| cdss-registry | D | signed fragments + OPA policy (+GPP stamps) | keys never leave | Existing | Kenny-bytes (Programme lead; pool: Kenny-bytes, kendo-Jones, Ken-nough, Ken-E-Gee — MET-2.2 §1) | D |
| cdss-graph | E | deterministic builds (+rebuttal records, DetectedIssues) | rebuild=f(registry version) | Existing+Transformed | Kenny-bytes (Programme lead; pool: Kenny-bytes, kendo-Jones, Ken-nough, Ken-E-Gee — MET-2.2 §1) | E |
| cdss-conformal | F | wrapper + calibration reports | pure math, no data retained | Existing | Kenny-bytes (Programme lead; pool: Kenny-bytes, kendo-Jones, Ken-nough, Ken-E-Gee — MET-2.2 §1) | F |
| cdss-corruption | G | suites (+ARG-class; FZ-5 dormant) + rulebook | clinician-reviewable in isolation | Existing+Transformed | Kenny-bytes (Programme lead; pool: Kenny-bytes, kendo-Jones, Ken-nough, Ken-E-Gee — MET-2.2 §1) | G |
| cdss-lumos | H | protocol/SAP/rows | no data ever enters | Existing | Kenny-bytes (Programme lead; pool: Kenny-bytes, kendo-Jones, Ken-nough, Ken-E-Gee — MET-2.2 §1) | H |
| cdss-evalstack | I | pipelines (+R29 ratchet check on ratification) | operates, does not author | Existing+Transformed | Kenny-bytes (Programme lead; pool: Kenny-bytes, kendo-Jones, Ken-nough, Ken-E-Gee — MET-2.2 §1) | I |
| cdss-governance | J | validator + census (+R30) | runs in every CI | Existing+Transformed | Kenny-bytes (Programme lead; pool: Kenny-bytes, kendo-Jones, Ken-nough, Ken-E-Gee — MET-2.2 §1) | J |
| cdss-coder | J-1/J-2 | det-coder+dictionary or ml-coder container | fork = release channel | Existing (labels per C-01) | Kenny-bytes (Programme lead; pool: Kenny-bytes, kendo-Jones, Ken-nough, Ken-E-Gee — MET-2.2 §1) | J (J-1/J-2 channel labels) |
| cdss-harness | HX | learners/checker/cascade | EVAL-refusing loaders proven here | Existing | Kenny-bytes (Programme lead; pool: Kenny-bytes, kendo-Jones, Ken-nough, Ken-E-Gee — MET-2.2 §1) | HX |
| cdss-llm-lattice | K/L | prompt registry, orchestration, L services | prompt changes are I events | Existing | Kenny-bytes (Programme lead; pool: Kenny-bytes, kendo-Jones, Ken-nough, Ken-E-Gee — MET-2.2 §1) | K, L |
| **cdss-fabric** | MAK-FFC/ABC | fabric service, deviation machinery, compliance projector | schemas in spine, never here; ledger per DEC-04 | **Proposed** | Kenny-bytes (Programme lead; pool: Kenny-bytes, kendo-Jones, Ken-nough, Ken-E-Gee — MET-2.2 §1) | FAB (ratified 2026-09-05) |
| **cdss-compiler** | EN-3/CP | GenericArgument bundles from CQL/FHIR-CPG/WHO-SMART | outputs via registry gateway | **Proposed** | Kenny-bytes (Programme lead; pool: Kenny-bytes, kendo-Jones, Ken-nough, Ken-E-Gee — MET-2.2 §1) | CP — not in the §13.3 set; cited as EN-3/CP (Arch §14.5) [PENDING-ENUMERATION — DEC-09 named four prefixes] |
| **cdss-ui-clinician** | MAK-LBP/HDC | component library + clinician face | conformance suite = CI acceptance | **Proposed** | Kenny-bytes (Programme lead; pool: Kenny-bytes, kendo-Jones, Ken-nough, Ken-E-Gee — MET-2.2 §1) | UIC (ratified 2026-09-05) |
| **cdss-ui-patient** | MAK-PRB/TXC | component library + patient face | beyond J-3-safe subset: Blocked (ASSUME-REG-003) | **Proposed** | Kenny-bytes (Programme lead; pool: Kenny-bytes, kendo-Jones, Ken-nough, Ken-E-Gee — MET-2.2 §1) | UIP (ratified 2026-09-05) |
| *(channel)* GPP | MAK-J3 | J-3 build artifact | integration-repo release channel; GPP-14 boundary | **Proposed** | Kenny-bytes (Programme lead; pool: Kenny-bytes, kendo-Jones, Ken-nough, Ken-E-Gee — MET-2.2 §1) | GPP (ratified 2026-09-05) |
Stack notes (C-04 reconciliation): AWS topology per Arch §11.4 stands; LS-2 (replayability/single-gate/telemetry/SBOM by construction), LS-3 (bounded polyglot: JVM for CQL/clinical-reasoning/HAPI, Python for MAPIE/pgmpy-class, TypeScript app layer; no clinical logic reimplemented across languages), LS-4 (boring bias; runtime-tech count is a reviewed metric) adopted as MUSTs; L1-2 UI bindings are the frontend acceptance bar.

## Skeleton index (appended — skeletons generated 2026-09-01; every file marked Proposed, no code claimed)
`repo-skeletons/` now carries: all **14 existing repos** (README + MANIFEST.yaml stub + CI stub + per-directory stubs mirroring each primer's §-4/§-8 and this pass's annex), **cdss-integration** (Proposed home for the lockfile — Arch §10: "an integration repo (or the spine itself)"; its ownership of R14 in the Arch §12.2 table supports the standalone home; DEC-09 decides) with `GPP-CHANNEL.md` (the J-3 channel spec: not a repo), and directory trees for the **4 proposed repos**. Doctrinal notes honoured in the skeletons: contracts appear in cdss-spine as **pointer stubs** to the canonical drafts in `05_registers-and-contracts/` (move-never-copy on ratification — "duplication is where drift begins"); the cdss-corpus skeleton is intentionally minimal with a firewall banner (instantiate only in-account; no case structure stubbed dev-side); CODEOWNERS stubs land where the primers mandate them (registry: pharmacist+clinician; library: clinician; compiler bundles: gateway discipline; spine contracts: architecture owner). Every CI stub carries the dormant R29 ratchet hook (activates on DEC-02; MT2 §7(4)).

## Self-audit

`grep -c '^| \*\?\*\?cdss-\|^| \*(channel)\*' 06_repositories/REPO-MAP_v3.md` → 19 repository rows (14 existing + 4 proposed + 1 channel), each with a non-empty owner cell; v2 byte-identical (sprint-2 CHECKSUMS). Ledger row and task for this file: HARDEN-1.2 / HARDEN-3.2 (same sprint).
