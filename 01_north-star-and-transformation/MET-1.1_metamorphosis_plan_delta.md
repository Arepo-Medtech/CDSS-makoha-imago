---
doc_id: MET-1.1
title: "Metamorphosis Plan — v1.1 delta (repository edition)"
version: "1.1-delta"
date: "2026-09-01"
supersedes: "nothing — MET-1 v1.0 is preserved verbatim beside this file; this delta records what changed between the single-document plan (v1.0) and the full artifact repository (v1.1)"
status: "Proposed"
---

# MET-1 v1.1 — what changed from v1.0

v1.0 (preserved as `MET-1_metamorphosis_plan_v1.0.md`) was the single-document master plan: executive summary, North Star, baseline, disposition register, target architecture, MT1 traceability, conflict register C-01..C-10, MT2 plan §9, deployment ladders, decision queue DEC-01..DEC-10, index, and gap analysis G-01..G-10. **All of that content stands and is not restated here.** v1.1 executes the plan's documentation obligations as a repository:

| v1.0 section | v1.1 realization | Location |
|---|---|---|
| §4 disposition register | Every original preserved verbatim **and** augmented in place with additive annexes (X1 discipline: zero edits above the annex line) | `02_cdss-stack-augmented/` (21 files), `03_makoha-butterfly-corpus/` (32 files, verbatim) |
| §6.2/§6.3 contracts & bindings | Contract specs drafted; per-primer Fabric Binding + Execution annexes written with the ten required execution fields each | `05_registers-and-contracts/`, annexes §A10…§L10 |
| §6.4 registers | R29/R30 schemas drafted to Arch §12.2 format; R30 seeded from REG-POSTURE; R29 seeded with the full enumeration, all rows PENDING | `05_registers-and-contracts/` |
| §8 conflict register | Extracted to a standalone, citable register joined with the decision queue | `MET-2_conflict_and_decision_register.md` |
| §9 hardening plan | Split into spec (/spec output), dependency-ordered worklist (/plan output), and ledger seed; engine research delta recorded (live pack = 25 skills incl. meta vs directive's "24" — row-zero reconciliation duty added) | `04_hardening/HARDEN-1/2/3` |
| §11 deployment | Expanded into deployment, testing, ops, governance, and security documents | `07_deployment-and-operations/` |
| §16 index | Machine-checkable manifest with per-file disposition, checksummable inventory, and completeness audit | `00_MANIFEST.md` |
| §17 roadmap | Carried forward unchanged; G-08 (HeyDoc below-README inventory) remains open | MET-4 |
| — (new) | Traceability map (source → output, requirement-family → binding site) | `MET-3_traceability_map.md` |
| — (new) | Repository map + skeletons for the four proposed repos | `06_repositories/` |
| — (new) | Research report separating supplied / newly-found / proposed sources | `08_research/RESEARCH-1` |
| — (new) | Renderable diagram successor + editable mermaid sources | `09_diagrams/` |

**Unchanged honesty line:** nothing in v1.1 claims execution v1.0 did not claim. The hardening pass remains unexecuted (row zero Blocked); the validator has not run on the annexes; every proposal awaits its DEC row.
