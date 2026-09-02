---
doc_id: MET-2
title: "Conflict, Reconciliation, Escalation & Decision Register"
version: "1.0"
date: "2026-09-01"
status: "Open register — Proposed home: joins R27 (Build Drift & Adjudication) for conflicts and R26 (Build Work) for decisions on ratification; interim entries marked PENDING-REGISTER-HOME per the Ecosystem v2.0 precedent"
rule: "Per MT2 §6: both positions recorded; no silent winner; ESCALATED rows go to the operator's consolidated blocker report."
---

# Conflicts (C-01 … C-12)

| ID | Both positions (sources) | Ruling / state |
|---|---|---|
| C-01 | CDSS stack: J-1 = "exemption posture… designed to meet all three TGA exempt-CDSS criteria" (Arch §9; Primer 0 §7; J-1 title/§5; complete-stack header) ⟷ REG-POSTURE: "not eligible… the disqualifier is the diagnostic function, not the use of AI" (REG-FIND-001); relabel to lower-/higher-class included (FORK-REG-001) | **Transformed per MANIFEST precedence; Needs confirmation** — closes only on ASSUME-REG-002 written counsel attestation (GATE-000). Deprecation notices appended (Primer 0 §11, J-1 §8, J-2 §7, Arch §14, complete-stack notice); reversal path preserved verbatim in REG-POSTURE §3.4 |
| C-02 | "spine" = release path + registry (Arch §1) ⟷ SPINE-1..9 = fabric requirements (MAK-FFC Part 2) | **Ruled (proposed):** nomenclature only; SPINE-7 restates the doctrine. House terms: "release spine" vs "SPINE-n". Arch §14.1; Primer 0 §11 glossary |
| C-03 | LLM substrate: "Amazon Bedrock via PrivateLink, no public egress" (Arch §11.4) ⟷ "Bedrock → Baseten (Sydney, dedicated)" for pinning/promotion/residency (REG-POSTURE §5.1; ASSUME-REG-004 OPEN) | **ESCALATED → DEC-03.** Arch §11.4 self-declares service choices Primer-I-changeable configuration, so the change path exists; the decision is human |
| C-04 | AWS-native indicative stack (Arch §11.4) ⟷ MAK-LEG legs (React/Next/TS, NestJS, JVM+Python presences) | **Reconciled by LS-1:** defaults are suggestions, bindings are law. Topology stands; LS-2/3/4 + L1-2 bindings adopted as MUSTs |
| C-05 | Runtime ledgers as S3 object-lock streams (R11 et al.) ⟷ SPINE-4 hash-chained fabric w/ FHIR bindings ⟷ ELSM: Aurora + transparency-log pattern; QLDB AVOID (retired 31 Jul 2025); immudb BUSL flag | **Ruled (proposed) → DEC-04:** one physical fabric ledger (Aurora + hash-chain); R11/R13/R18 become views; owners/mutability unchanged; S3 object-lock as archival anchor. Register-law change — architecture-owner ratification required |
| C-06 | No patient face in CDSS stack (L intake only, L5) ⟷ MAK-TXC/MAK-PRB full patient face/UI ⟷ TASK-REG-004: "decide the patient surface" (ASSUME-REG-003 OPEN) | **ESCALATED → DEC-07 (GATE-000).** Until closed: patient-face work beyond intake/consent/logistics (J-3-safe subset) is Blocked |
| C-07 | "coder" reserved for the concept coder (Arch §13.2) ⟷ "Guideline Compiler" (MAK-FFC EN-3) | **No conflict** — distinct components; glossary guards both terms |
| C-08 | Primer F ⟷ MAK-CEC QU/EN-4 qualifier machinery | **No conflict** — consolidation volume; never retires source requirements (MANIFEST); F + I8 numbers authoritative |
| C-09 | MAK-DOT: FZ-1..6 "proposals… not ratified" (its own footer) ⟷ MAK-LWC v1.1 written as normative (43 reqs) over that foundation | **ESCALATED → DEC-05.** Until ruled: all fuzzy machinery Proposed/dormant; MAK-DOT anti-patterns enforced meanwhile (never render μ as confidence, anywhere) |
| C-10 | demo.makoha.ai presents an AI conversational surface ("conversations are processed via third-party AI providers") ⟷ TASK-REG-003: public claims must match the intended-purpose statement exactly; advertising rules bind exempt and included alike (OBL-003) | **ESCALATED → Phase 0** (after TASK-REG-001) |
| C-11 | MT2 §2.2: "The 24 skills… all deployed" ⟷ live repo README (verified 1 Sep 2026): "25 skills total — 24 lifecycle skills plus the using-agent-skills meta-skill"; release 0.6.4 adds an in-repo eval framework | **Ruled (proposed):** the directive's own §2.2 list includes using-agent-skills among its 24, so intent = whole pack either way; row zero confirms against the live inventory at install time and records any delta verbatim; a mismatch that cannot be reconciled halts the pass (directive §6, engine-tooling rule) |
| C-12 | MT2 §2.1 names "issue #361" as the per-skill-install defect ⟷ live docs confirm the gap and track it at addyosmani/agent-skills#361 | **No conflict** — corroborated by fetch; recorded as verification evidence for §2.1's whole-pack rule |

# Decisions requiring human approval (DEC-01 … DEC-12)

| DEC | Decision | Blocking | Owner | State |
|---|---|---|---|---|
| DEC-01 | Ratify C-01 relabel portfolio-wide; regenerate derived artifacts once | GATE-000 | Regulatory + architecture owners | Open |
| DEC-02 | Ratify R29 + R30 into Arch §12.2 (schemas in 05_) | pass start (R29); L1 (R30) | Architecture owner | Open |
| DEC-03 | Rule C-03 substrate (Bedrock ⟷ Baseten) | GATE-001 / TASK-REG-009 | Infra + regulatory | Open |
| DEC-04 | Rule C-05 ledger substrate; registers-as-views | fabric v0 design | Architecture owner | Open |
| DEC-05 | Ratify or defer FZ-1..6 (activates MAK-LWC bindings, FZ-5 suite class, FZ-6 namespace rows) | fuzzy entry | Corpus owner + clinical review | Open |
| DEC-06 | Ratify MAK-J3 from v0.9; resolve its two ⚑ flags with legal reading | GPP first release | Counsel + product | Open |
| DEC-07 | Patient-surface scope (C-06/ASSUME-REG-003/TASK-REG-004) | GATE-000 | Counsel + product | Open |
| DEC-08 | Carry-overs: IMPL rename ratification; Observer cadence (proposed quarterly from L4) | — | Architecture owner | Open (pre-existing) |
| DEC-09 | New repo owners + namespace prefixes {FAB, UIC, UIP, GPP} | repo creation | Programme lead [NEEDS DEFINITION] | Open |
| DEC-10 | Name the MT2 operator (receives the consolidated blocker report) | pass start | [NEEDS DEFINITION] | Open |
| DEC-11 | Accept C-11 row-zero reconciliation rule | pass start | MT2 operator | Open |
| DEC-12 | Approve HeyDoc corpus-seed intake procedure (C10 annex) and commission the below-README inventory (G-08) | corpus seeding | Corpus custodian | Open |

**Standing escalations for the operator's consolidated blocker report (MT2 §7(2)):** C-03, C-06, C-09, C-10, plus row zero (engine uninstalled) and PENDING-VALIDATOR on all annexes.
