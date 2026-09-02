---
doc_id: DEPLOY-1
title: "Deployment plan & sequencing — three ladders interleaved"
version: "1.0"
status: "Proposed. Grounded in Arch §11 (levels/tiers, Retained), MAK-ANT §7 (phases/gates, Added), MT2 (pass, Proposed). The tier pipeline T1+2→T5 never relaxes under any step."
---
# The ladders
| Step | Gate | Content | Status |
|---|---|---|---|
| 0a | — | MT2 pass over the portfolio (row zero → 100% ledger). Engineering exploration is not blocked; regulated use of an artifact is, until its row is HARDENED or its blocker operator-accepted | Proposed |
| 0b | **GATE-000 (blocking)** | Phase 0: TASK-REG-001 intended-purpose statement (three surfaces explicit) · TASK-REG-002 counsel opinion → ASSUME-REG-001/002 ATTESTED · TASK-REG-003 positioning reconciliation (closes C-10) · TASK-REG-004 patient-surface decision (closes C-06/DEC-07). Do not configure regulated tooling before this | Blocked on counsel |
| 1 | GATE-001 | Phase 1: Jira+Ketryx from the Ketryx schema (KTX-001; strict risk KTX-011; minimal V-model KTX-010) · ISO 14971 risk file — the spine everything hangs from, before requirements · requirements traced to Essential Principles (KTX-008) · substrate decision executed (TASK-REG-009/DEC-03). **In parallel:** L1 Glass-Box Core on synthetic scope (registers R1–R9 + proposed R29/R30 open; fabric-v0 argument schema in spine so L1 trace replay already replays arguments) · Lumos ethics contact opened (Q-REG-007, parallel from Phase 1 — longest lead) | Proposed |
| 2 | **GATE-002 (identifiable-data line)** | Phase 2 controls: gated regulated pipeline split from synthetic push-to-deploy (TASK-REG-010) · SBOM→Ketryx (TASK-REG-011) · vuln handling + CVSS + CAPA (TASK-REG-012) · supplier assessments (TASK-REG-013) · IEC 62366-1 ×3 surfaces, patient last but never skipped (TASK-REG-014). **In parallel:** L2 Signed Content Loop (gates at 100% ×3 releases) + clinician face/UI v0 as L2's verbatim-render surface. REG-KEEP-004 enforced: synthetic-only until controls operate | Proposed |
| 3 | — | L3 Honest Uncertainty + Coded Intake (conformal proven external-then-internal; det-coder; graph v0; full I stack) + compiler v0 + auditor read model v0. First externally showable prototype; produces fork evidence (abstention baseline → R19) | Proposed |
| 4 | L4 exit; GATE-003 evidence | L4 Full Lattices: posture decision on L3 evidence **under relabeled branches** (lower- vs higher-class included) · first casebundle checkpoint · census total · limited pilot under Tier-5 monitoring (MoUs close ASSUME-SPINE-001) · Phase-3 evidence: Lumos study (TASK-REG-015), independent pen-test (TASK-REG-016), post-market procedures (TASK-REG-017), Ketryx tier decision (TASK-REG-018) · GPP first release if DEC-06 ratifies | Proposed / Needs confirmation (GPP) |
| 5 | **GATE-004 = first lawful clinical supply** | Phase 4: conformity assessment route per Q-REG-005 (TASK-REG-019) → ARTG inclusion (TASK-REG-020) beside L5 Target State (L capabilities staged per posture; Lumos Stage 2→3 against a named freeze; dossier = a join over registers; negative audits scheduled) | Proposed |

# Rollback & recovery (Retained + gaps)
Lockfile pin-set (R14): rollback = redeploy prior pin-set; version stamp keeps traces attributable across the boundary. Append-only ledgers never roll back — corrections supersede (SPINE-4). Kill criteria stand: corruption catch <100% twice consecutively halts the release train; R19 reversal triggers per branch and per L-capability; fork reversal costs the coder layer alone; GPP-14 forbids rolling the GPP artifact forward across the exemption boundary. **[NEEDS DEFINITION]:** RTO/RPO targets and the L5 multi-region DR drill protocol are named in Arch §11.2 but specified nowhere in the supplied material.
