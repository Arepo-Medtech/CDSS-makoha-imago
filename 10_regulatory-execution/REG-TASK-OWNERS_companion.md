---
doc_id: REG-TASK-OWNERS
title: "REG-TASK-OWNERS — task → gate → run → owner role → account → evidence artifact → R30.3 row, for TASK-REG, NZ-TASK, US-TASK and EU-TASK"
version: "1.0"
date: "2026-09-05"
status: "Added (sprint-2). Proposed companion read WITH REG-POSTURE v1.2 §7, REG-NZ v1.1 §8, REG-US v1.0 and REG-EU v1.0; edits none of them and changes no task status. ADVISORY_ONLY (REG-POSTURE §0.1 posture). Owner roles are DEPLOY-1.1 D-2 roles resolved to accounts through MET-2.2 §1; where MET-2.2 names no one the cell reads [NEEDS DEFINITION] with its decision. Every evidence-artifact cell names what DONE-WITH-EVIDENCE means for that task (REG-POSTURE §0.4); none exists yet."
authority: ADVISORY_ONLY
applies_to: "10_regulatory-execution/REG-POSTURE_v1.2.md §7 (read with REG-POSTURE_v1.2_CONTENTS.md); 10_regulatory-execution/REG-NZ_v1.1.md §8; 10_regulatory-execution/REG-US_v1.0.md; 10_regulatory-execution/REG-EU_v1.0.md"
change_policy: "Companion; a later version supersedes as a new file. Task ids are cited, never minted."
produced_by: "sprint-2 (survey-3 Queue §c.1 row QI-0020) — 11_prompts/runs/2026-09-05_sprint-2/tools/regtask.py; generated from the four posture files and 05_registers-and-contracts/REG-R30.3_row-form_seed.jsonl"
---

# REG-TASK-OWNERS — regulatory task crosswalk

## §1 Why

Every task row in the four posture files carries ID · Task · Gate only (survey-3 QI-0020, confidence
85). Owners reached a task only through DEPLOY-1.1's DR-n → phase mapping, and DONE-WITH-EVIDENCE
(REG-POSTURE §0.4) had no cell naming the evidence. This companion supplies both, per task, without
touching the posture files. The RUN column is the EXEC-1 run map, in force since DEC-22 closed
(MET-2.2 §3.1). US and EU tasks sit outside RUN-0..4 by design (EXEC-1 covers AU and NZ; REG-US and
REG-EU are ADVISORY jurisdiction postures) and say so rather than inventing a run.

## §2 Crosswalk (60 tasks)

| Task | Gate | DR step (DEPLOY-1.1) | RUN (EXEC-1) | Owner role | Account (MET-2.2 §1) | Evidence artifact (DONE-WITH-EVIDENCE means…) | R30.3 row | Source |
|---|---|---|---|---|---|---|---|---|
| `TASK-REG-001` | `GATE-000` | DR-2 | RUN-0 · Decide | Founder (programme) — DR-2 | Kenny-bytes | intended purpose statement v1.0, signed (draft: 11_prompts/runs/2026-09-05_primer-0/DRAFT_TASK-REG-001) | PRESENT | `REG-POSTURE_v1.2.md:874` |
| `TASK-REG-002` | `GATE-000` | DR-2 | RUN-0 · Decide | Regulatory owner (packet content); Founder (dispatch) | kendo-Jones; Kenny-bytes | counsel's written classification opinion, dated (AU packet dispatched: counsel_packet_AU/) | PRESENT | `REG-POSTURE_v1.2.md:875` |
| `TASK-REG-003` | `GATE-000` | DR-2 | RUN-0 · Decide | Regulatory owner (packet content); Founder (dispatch) | kendo-Jones; Kenny-bytes | versioned claims inventory reconciled to the intended purpose statement (OBL-014) | PRESENT | `REG-POSTURE_v1.2.md:876` |
| `TASK-REG-004` | `GATE-000` | DR-2 | RUN-0 · Decide | Counsel + product (DEC-07) | [NEEDS DEFINITION — DEC-07]; kendo-Jones drafts | DEC-07 ruling recorded in MET-2.n; ASSUME-REG-003 ATTESTED/REFUTED | PRESENT | `REG-POSTURE_v1.2.md:877` |
| `TASK-REG-021` | `GATE-000` | DR-2 | RUN-0 · Decide | Regulatory owner (packet content); Founder (dispatch) | kendo-Jones; Kenny-bytes | demo-surface triage record: supplier entry for the AI provider (OBL-013), disclosure check, keep/withdraw decision | PRESENT | `REG-POSTURE_v1.2.md:878` |
| `TASK-REG-022` | `GATE-000` | DR-2 | RUN-0 · Decide | Founder (programme) — DR-2 | Kenny-bytes | jurisdiction-sequence decision recorded (Q-REG-008 answered; MET-2.n row) | PRESENT | `REG-POSTURE_v1.2.md:879` |
| `TASK-REG-023` | `GATE-000` | DR-2 | RUN-0 · Decide | Regulatory owner — DR-2 (inside the TASK-REG-002 engagement) | kendo-Jones | counsel's written view on the Governance Layer's non-device status (ASSUME-REG-009, Q-REG-010) | PRESENT | `REG-POSTURE_v1.2.md:880` |
| `TASK-REG-005` | `GATE-001` | DR-3 | RUN-1 · Foundation | Regulatory owner (Jira/Ketryx) — DR-3 | kendo-Jones | Jira project + Ketryx workspace exist (screenshot/export), synthetic scope declared | PRESENT | `REG-POSTURE_v1.2.md:897` |
| `TASK-REG-006` | `GATE-001` | DR-3 | RUN-1 · Foundation | Regulatory owner | kendo-Jones | Ketryx configuration export per KTX-001/010/011 + configuration-item ceiling model (§6.1) | PRESENT | `REG-POSTURE_v1.2.md:898` |
| `TASK-REG-007` | `GATE-001` | DR-3 | RUN-1 · Foundation | Regulatory owner | kendo-Jones | ISO 14971 risk file opened (Ketryx risk module export, first hazard rows) | PRESENT | `REG-POSTURE_v1.2.md:899` |
| `TASK-REG-008` | `GATE-001` | DR-3 | RUN-1 · Foundation | Regulatory owner | kendo-Jones | requirements set tagged to Essential Principles (KTX-008 export) | PRESENT | `REG-POSTURE_v1.2.md:900` |
| `TASK-REG-009` | `GATE-001; DEC-03` | DR-3 | RUN-1 · Foundation | Infrastructure owner + Regulatory owner (DEC-03) — DR-3 | Ken-nough + kendo-Jones | DEC-03 ruling + executed contract terms (ASSUME-REG-004) or Bedrock pinning evidence (C-16) | PRESENT | `REG-POSTURE_v1.2.md:901` |
| `TASK-REG-024` | `GATE-001` | DR-3 | RUN-1 · Foundation | Regulatory owner | kendo-Jones | QMS certification route decision recorded (Q-REG-011; MDSAP vs TGA direct) | PRESENT | `REG-POSTURE_v1.2.md:902` |
| `TASK-REG-010` | `GATE-002` | DR-4 | RUN-2 · Controls & domain | Security owner | Ken-E-Gee | gated release pipeline definition + one approval artifact in CI | PRESENT | `REG-POSTURE_v1.2.md:912` |
| `TASK-REG-011` | `GATE-002` | DR-4 | RUN-2 · Controls & domain | Security owner | Ken-E-Gee | SBOM artifact generated in CI and visible in Ketryx SCM (KTX-012) | PRESENT | `REG-POSTURE_v1.2.md:913` |
| `TASK-REG-012` | `GATE-002` | DR-4 | RUN-2 · Controls & domain | Security owner | Ken-E-Gee | vulnerability-handling and disclosure SOP with CVSS + CAPA linkage (STD-009, OBL-008) | PRESENT | `REG-POSTURE_v1.2.md:914` |
| `TASK-REG-013` | `GATE-002` | DR-4 | RUN-2 · Controls & domain | Security owner | Ken-E-Gee | supplier assessment records (substrate, AWS, third-party AI provider) | PRESENT | `REG-POSTURE_v1.2.md:915` |
| `TASK-REG-014` | `GATE-002` | DR-4 | RUN-2 · Controls & domain | Operations owner (usability programme) — DR-4 | [NEEDS DEFINITION — no operations owner named in MET-2.2 §1; DEC-23 extension] | three IEC 62366-1 use-related risk analyses (clinician, patient, auditor) | PRESENT | `REG-POSTURE_v1.2.md:916` |
| `TASK-REG-015` | `GATE-003` | DR-6 | RUN-3 · File & notify / RUN-4 · Evidence & submission | Regulatory owner + cdss-lumos repo owner — DR-6 | kendo-Jones + Kenny-bytes | clinical evidence plan + Lumos linkage agreement; first evidence rows | PRESENT | `REG-POSTURE_v1.2.md:927` |
| `TASK-REG-016` | `GATE-003` | DR-6 | RUN-3 · File & notify / RUN-4 · Evidence & submission | Security owner — DR-6 (pen-test) | Ken-E-Gee | independent penetration test report (external party named) | PRESENT | `REG-POSTURE_v1.2.md:928` |
| `TASK-REG-017` | `GATE-003` | DR-6 | RUN-3 · File & notify / RUN-4 · Evidence & submission | Regulatory owner + Architecture owner | kendo-Jones + Kenny-bytes | post-market surveillance procedures + adverse-event reporting SOP | PRESENT | `REG-POSTURE_v1.2.md:929` |
| `TASK-REG-018` | `GATE-003` | DR-6 | RUN-3 · File & notify / RUN-4 · Evidence & submission | Regulatory owner + Architecture owner | kendo-Jones + Kenny-bytes | Ketryx tier upgrade order/confirmation (validated-out-of-the-box status) | PRESENT | `REG-POSTURE_v1.2.md:930` |
| `TASK-REG-019` | `GATE-004` | DR-7 | RUN-4 · Evidence & submission | Regulatory owner; Founder | kendo-Jones; Kenny-bytes | conformity assessment application lodged (receipt) — route per Q-REG-005 | PRESENT | `REG-POSTURE_v1.2.md:939` |
| `TASK-REG-020` | `GATE-004` | DR-7 | RUN-4 · Evidence & submission | Regulatory owner; Founder | kendo-Jones; Kenny-bytes | ARTG inclusion certificate | PRESENT | `REG-POSTURE_v1.2.md:940` |
| `NZ-TASK-001` | `NZ-GATE-000` | DR-2 | RUN-0 · Decide (NZ-GATE-0 prep) | Founder + NZ counsel (DEC-19) | Kenny-bytes; counsel [external] | NZ counsel's written confirmation of NZ-FIND-001..012 and NZ-Q-004 (NZ packet: counsel_packet_NZ/) | PRESENT | `REG-NZ_v1.1.md:420` |
| `NZ-TASK-002` | `NZ-GATE-000` | DR-2 | RUN-0 · Decide (NZ-GATE-0 prep) | Founder (DEC-19) — DR-2 | Kenny-bytes | sponsor structure decision recorded (DEC-19) | PRESENT | `REG-NZ_v1.1.md:421` |
| `NZ-TASK-003` | `NZ-GATE-000` | DR-2 | RUN-0 · Decide (NZ-GATE-0 prep) | Founder — DR-2 | Kenny-bytes | employer's written position on the registrar/director conflict | PRESENT | `REG-NZ_v1.1.md:422` |
| `NZ-TASK-004` | `NZ-GATE-000` | DR-2 | RUN-0 · Decide (NZ-GATE-0 prep) | Founder + NZ counsel (DEC-19) | Kenny-bytes; counsel [external] | Medical Products Bill timing model vs technical-file readiness (NZ-WATCH-001; NZ-ASSUME-005) with the NZ-first decision | PRESENT | `REG-NZ_v1.1.md:423` |
| `NZ-TASK-005` | `NZ-GATE-001` | DR-6 | RUN-3 · File & notify (V2-S2) | Regulatory owner + Security owner (privacy/data residency) | kendo-Jones + Ken-E-Gee | Privacy Impact Assessment (HIPC 2020); data-residency decision; Māori data governance engagement record | PRESENT | `REG-NZ_v1.1.md:424` |
| `NZ-TASK-006` | `NZ-GATE-001` | DR-6 | RUN-3 · File & notify (V2-S2) | Regulatory owner; NZ sponsor (DEC-19) | kendo-Jones; sponsor [NEEDS DEFINITION — DEC-19] | technical file indexed for Medsafe (STED index) — same artifact set as the AU conformity assessment | PRESENT | `REG-NZ_v1.1.md:425` |
| `NZ-TASK-007` | `NZ-GATE-001` | DR-6 | RUN-3 · File & notify (V2-S2) | Regulatory owner; NZ sponsor (DEC-19) | kendo-Jones; sponsor [NEEDS DEFINITION — DEC-19] | post-market system evidence (complaints, adverse events, recall capability) operating before supply | PRESENT | `REG-NZ_v1.1.md:426` |
| `NZ-TASK-008` | `NZ-GATE-002` | DR-6 | RUN-3 · File & notify (V2-S3a/b) | Regulatory owner; NZ sponsor (DEC-19) | kendo-Jones; sponsor [NEEDS DEFINITION — DEC-19] | WAND notification record | PRESENT | `REG-NZ_v1.1.md:427` |
| `NZ-TASK-009` | `NZ-GATE-001` | DR-6 | RUN-3 · File & notify (V2-S2) | Regulatory owner; NZ sponsor (DEC-19) | kendo-Jones; sponsor [NEEDS DEFINITION — DEC-19] | tested SaMD post-market mechanisms per NZ-OBL-007 (complaint channel, triage SOP, remote disablement/forced update, functional-change procedure) | PRESENT | `REG-NZ_v1.1.md:428` |
| `NZ-TASK-010` | `NZ-GATE-002` | DR-6 | RUN-3 · File & notify (V2-S3a/b) | Regulatory owner; NZ sponsor (DEC-19) | kendo-Jones; sponsor [NEEDS DEFINITION — DEC-19] | first NZ site agreement + HISO/procurement security questionnaire + data agreement executed | PRESENT | `REG-NZ_v1.1.md:429` |
| `US-TASK-001` | `US-GATE-000` | — (no DR step: US/EU are ADVISORY jurisdictions outside the EXEC-1 run map; REG-SPRINT V3 at the earliest) | not in EXEC-1 RUN-0..4 (V3 / later) | Security owner (Part 11 controls) + Regulatory owner | Ken-E-Gee + kendo-Jones | Part 11 capability evidence for design-control records (attribution, e-signature, audit trail, validation) — intended-use test result | PRESENT | `REG-US_v1.0.md:337` |
| `US-TASK-002` | `US-GATE-000` | — (no DR step: US/EU are ADVISORY jurisdictions outside the EXEC-1 run map; REG-SPRINT V3 at the earliest) | not in EXEC-1 RUN-0..4 (V3 / later) | Security owner (SBOM) | Ken-E-Gee | CycloneDX/SPDX SBOM with §524B fields incl. AI vendor and pinned model entries | PRESENT | `REG-US_v1.0.md:338` |
| `US-TASK-003` | `US-GATE-000` | — (no DR step: US/EU are ADVISORY jurisdictions outside the EXEC-1 run map; REG-SPRINT V3 at the earliest) | not in EXEC-1 RUN-0..4 (V3 / later) | Regulatory owner | kendo-Jones | clinical evidence programme protocol to ISO 14155 satisfying 21 CFR 812.28; pre-registered subgroup analyses | PRESENT | `REG-US_v1.0.md:339` |
| `US-TASK-004` | `US-GATE-000` | — (no DR step: US/EU are ADVISORY jurisdictions outside the EXEC-1 run map; REG-SPRINT V3 at the earliest) | not in EXEC-1 RUN-0..4 (V3 / later) | Regulatory owner | kendo-Jones | IEC 62304 document set projectable to the Enhanced-level 2023 guidance list | PRESENT | `REG-US_v1.0.md:340` |
| `US-TASK-005` | `US-GATE-001` | — (no DR step: US/EU are ADVISORY jurisdictions outside the EXEC-1 run map; REG-SPRINT V3 at the earliest) | not in EXEC-1 RUN-0..4 (V3 / later) | Regulatory owner | kendo-Jones | US counsel/RA consultant's written response to US-ASSUME-001..006 | PRESENT | `REG-US_v1.0.md:346` |
| `US-TASK-006` | `US-GATE-001` | — (no DR step: US/EU are ADVISORY jurisdictions outside the EXEC-1 run map; REG-SPRINT V3 at the earliest) | not in EXEC-1 RUN-0..4 (V3 / later) | Regulatory owner | kendo-Jones | predicate search + pathway analysis memo; draft indications for use; PCCP scope decision | PRESENT | `REG-US_v1.0.md:347` |
| `US-TASK-007` | `US-GATE-001` | — (no DR step: US/EU are ADVISORY jurisdictions outside the EXEC-1 run map; REG-SPRINT V3 at the earliest) | not in EXEC-1 RUN-0..4 (V3 / later) | Regulatory owner | kendo-Jones | Q-Sub package and CDRH written feedback | PRESENT | `REG-US_v1.0.md:348` |
| `US-TASK-008` | `US-GATE-001` | — (no DR step: US/EU are ADVISORY jurisdictions outside the EXEC-1 run map; REG-SPRINT V3 at the earliest) | not in EXEC-1 RUN-0..4 (V3 / later) | Regulatory owner | kendo-Jones | QMS certification route decision (MDSAP) recorded (shared with TASK-REG-024) | PRESENT | `REG-US_v1.0.md:349` |
| `US-TASK-009` | `US-GATE-002` | — (no DR step: US/EU are ADVISORY jurisdictions outside the EXEC-1 run map; REG-SPRINT V3 at the earliest) | not in EXEC-1 RUN-0..4 (V3 / later) | Security owner | Ken-E-Gee | cyber device package: SPDF evidence, threat model, SW96 report, SBOM, disclosure plan, pen-test report | PRESENT | `REG-US_v1.0.md:350` |
| `US-TASK-010` | `US-GATE-002` | — (no DR step: US/EU are ADVISORY jurisdictions outside the EXEC-1 run map; REG-SPRINT V3 at the earliest) | not in EXEC-1 RUN-0..4 (V3 / later) | Regulatory owner | kendo-Jones | AI-enabled function documentation set per US-FIND-011 incl. model card and PCCP | PRESENT | `REG-US_v1.0.md:351` |
| `US-TASK-011` | `US-GATE-002` | — (no DR step: US/EU are ADVISORY jurisdictions outside the EXEC-1 run map; REG-SPRINT V3 at the earliest) | not in EXEC-1 RUN-0..4 (V3 / later) | Regulatory owner | kendo-Jones | human factors validation report per surface; US labelling/IFU with UDI | PRESENT | `REG-US_v1.0.md:352` |
| `US-TASK-012` | `US-GATE-002` | — (no DR step: US/EU are ADVISORY jurisdictions outside the EXEC-1 run map; REG-SPRINT V3 at the earliest) | not in EXEC-1 RUN-0..4 (V3 / later) | Regulatory owner | kendo-Jones | US Agent appointment; establishment registration/listing; HIPAA BAA template + Security Rule risk analysis; FTC HBNR readiness; submission receipt | PRESENT | `REG-US_v1.0.md:353` |
| `US-TASK-013` | `US-GATE-003` | — (no DR step: US/EU are ADVISORY jurisdictions outside the EXEC-1 run map; REG-SPRINT V3 at the earliest) | not in EXEC-1 RUN-0..4 (V3 / later) | Regulatory owner | kendo-Jones | Part 803/806 procedures; §524B monitoring live; PCCP protocol operating; performance monitoring reports | PRESENT | `REG-US_v1.0.md:354` |
| `EU-TASK-001` | `EU-GATE-000` | — (no DR step: US/EU are ADVISORY jurisdictions outside the EXEC-1 run map; REG-SPRINT V3 at the earliest) | not in EXEC-1 RUN-0..4 (V3 / later) | Regulatory owner | kendo-Jones | technical documentation index to Annex II with STED/EP crosswalk; GSPR checklist | PRESENT | `REG-EU_v1.0.md:329` |
| `EU-TASK-002` | `EU-GATE-000` | — (no DR step: US/EU are ADVISORY jurisdictions outside the EXEC-1 run map; REG-SPRINT V3 at the earliest) | not in EXEC-1 RUN-0..4 (V3 / later) | Regulatory owner | kendo-Jones | AI Act Annex IV / Art 10 data-governance record from the first training/tuning run | PRESENT | `REG-EU_v1.0.md:330` |
| `EU-TASK-003` | `EU-GATE-000` | — (no DR step: US/EU are ADVISORY jurisdictions outside the EXEC-1 run map; REG-SPRINT V3 at the earliest) | not in EXEC-1 RUN-0..4 (V3 / later) | Architecture owner (runtime logging design) | Kenny-bytes | Article 12 automatic-logging design + retention specification (runtime) | PRESENT | `REG-EU_v1.0.md:331` |
| `EU-TASK-004` | `EU-GATE-000` | — (no DR step: US/EU are ADVISORY jurisdictions outside the EXEC-1 run map; REG-SPRINT V3 at the earliest) | not in EXEC-1 RUN-0..4 (V3 / later) | Regulatory owner | kendo-Jones | clinical evidence protocol with EU applicability (population vs EU demographics; ISO 14155; MDCG endpoints) | PRESENT | `REG-EU_v1.0.md:332` |
| `EU-TASK-005` | `EU-GATE-001` | — (no DR step: US/EU are ADVISORY jurisdictions outside the EXEC-1 run map; REG-SPRINT V3 at the earliest) | not in EXEC-1 RUN-0..4 (V3 / later) | Regulatory owner | kendo-Jones | EU counsel's written response to EU-ASSUME-001..006 | PRESENT | `REG-EU_v1.0.md:338` |
| `EU-TASK-006` | `EU-GATE-001` | — (no DR step: US/EU are ADVISORY jurisdictions outside the EXEC-1 run map; REG-SPRINT V3 at the earliest) | not in EXEC-1 RUN-0..4 (V3 / later) | Regulatory owner | kendo-Jones | notified body selection record + pre-application dialogue minutes; application lodged | PRESENT | `REG-EU_v1.0.md:339` |
| `EU-TASK-007` | `EU-GATE-001` | — (no DR step: US/EU are ADVISORY jurisdictions outside the EXEC-1 run map; REG-SPRINT V3 at the earliest) | not in EXEC-1 RUN-0..4 (V3 / later) | Regulatory owner | kendo-Jones | Authorised Representative mandate (Art 11(3)); PRRC designation (Art 15); EUDAMED SRN | PRESENT | `REG-EU_v1.0.md:340` |
| `EU-TASK-008` | `EU-GATE-001` | — (no DR step: US/EU are ADVISORY jurisdictions outside the EXEC-1 run map; REG-SPRINT V3 at the earliest) | not in EXEC-1 RUN-0..4 (V3 / later) | Regulatory owner + Security owner (GDPR) | kendo-Jones + Ken-E-Gee | GDPR: EU representative appointment (Art 27); DPIA; Art 28 terms; Chapter V transfer mechanism decision | PRESENT | `REG-EU_v1.0.md:341` |
| `EU-TASK-009` | `EU-GATE-002` | — (no DR step: US/EU are ADVISORY jurisdictions outside the EXEC-1 run map; REG-SPRINT V3 at the earliest) | not in EXEC-1 RUN-0..4 (V3 / later) | Regulatory owner | kendo-Jones | Clinical Evaluation Report (MDCG 2020-1); PMCF plan; PMS plan; PSUR template | PRESENT | `REG-EU_v1.0.md:342` |
| `EU-TASK-010` | `EU-GATE-002` | — (no DR step: US/EU are ADVISORY jurisdictions outside the EXEC-1 run map; REG-SPRINT V3 at the earliest) | not in EXEC-1 RUN-0..4 (V3 / later) | Security owner | Ken-E-Gee | cyber documentation set to MDCG 2019-16 | PRESENT | `REG-EU_v1.0.md:343` |
| `EU-TASK-011` | `EU-GATE-002` | — (no DR step: US/EU are ADVISORY jurisdictions outside the EXEC-1 run map; REG-SPRINT V3 at the earliest) | not in EXEC-1 RUN-0..4 (V3 / later) | Regulatory owner | kendo-Jones | AI Act conformity package integrated with the MDR technical file | PRESENT | `REG-EU_v1.0.md:344` |
| `EU-TASK-012` | `EU-GATE-002` | — (no DR step: US/EU are ADVISORY jurisdictions outside the EXEC-1 run map; REG-SPRINT V3 at the earliest) | not in EXEC-1 RUN-0..4 (V3 / later) | Regulatory owner | kendo-Jones | UDI assignment; EU Declaration of Conformity; CE marking record; EUDAMED device registration; launch-market IFUs | PRESENT | `REG-EU_v1.0.md:345` |
| `EU-TASK-013` | `EU-GATE-003` | — (no DR step: US/EU are ADVISORY jurisdictions outside the EXEC-1 run map; REG-SPRINT V3 at the earliest) | not in EXEC-1 RUN-0..4 (V3 / later) | Regulatory owner | kendo-Jones | vigilance procedures with 15/10/2-day clocks; trend reporting; PSUR cadence; PMCF running; significant-change SOP (EU-OBL-011); liability evidence retention | PRESENT | `REG-EU_v1.0.md:346` |

## §3 Census and self-audit (generated 2026-09-05T12:15:07Z; `tools/regtask.py`)

```
tasks parsed per family: {"TASK-REG": 24, "NZ-TASK": 10, "US-TASK": 13, "EU-TASK": 13}  total 60
R30.3 rows PRESENT for task ids: 60/60   ABSENT: none
evidence-artifact cells: 60/60 named; [NEEDS SOURCE]: 0
owner-account cells with [NEEDS DEFINITION]: 7 (each names its decision: DEC-07, DEC-19, DEC-23 extension)
owner-account cells empty: 0
```

Acceptance (Queue §c.1 QI-0020): 60/60 tasks mapped; 0 owner cells empty ([NEEDS DEFINITION] + DEC
allowed) — PASS. Family counts agree with REG-POSTURE §12.1 (TASK-REG 24), REG-NZ §12 (NZ-TASK 10),
REG-US (US-TASK 13) and REG-EU (EU-TASK 13) as parsed above.

## §4 What this companion did not do

Changed no task status (OPEN means OPEN); attested nothing; named no person the register has not named
(MET-2.2 §1); produced no evidence artifact — every artifact cell is a description of the artifact that
would close the task, not a claim that it exists. Regulatory content is ADVISORY_ONLY throughout.
Ledger row and task for this file: HARDEN-1.2 / HARDEN-3.2 (same sprint).
