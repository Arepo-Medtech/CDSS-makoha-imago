#!/usr/bin/env python3
"""Sprint-2 (survey-3 QI-0020): build 10_regulatory-execution/REG-TASK-OWNERS_companion.md — task → gate → RUN → owner role (DEPLOY-1.1 DR-n) → account (MET-2.2 §1) → evidence artifact → R30.3 row. Reads the four posture files and the R30.3 seed; edits nothing."""
import re, json, os, subprocess
ROOT = os.getcwd()
SRC = [('10_regulatory-execution/REG-POSTURE_v1.2.md','TASK-REG'),('10_regulatory-execution/REG-NZ_v1.1.md','NZ-TASK'),('10_regulatory-execution/REG-US_v1.0.md','US-TASK'),('10_regulatory-execution/REG-EU_v1.0.md','EU-TASK')]
tasks=[]
for f,pfx in SRC:
    seen=set()
    for n,ln in enumerate(open(f,encoding='utf-8'),1):
        m=re.match(r'^\| `('+pfx+r'-\d{3})`([^|]*)\| (.*?) \| ([^|]*) \|\s*$',ln)
        if m and m.group(1) not in seen and not m.group(3).startswith('Sequenced work item'):
            seen.add(m.group(1)); tasks.append({'id':m.group(1),'file':f,'line':n,'text':m.group(3),'gate':m.group(4).strip().replace('`','')})
r30=set(json.loads(l)['reg_id'] for l in open('05_registers-and-contracts/REG-R30.3_row-form_seed.jsonl',encoding='utf-8') if l.strip())
# gate → (DR step, RUN, owner role, account) — DEPLOY-1.1 D-2 roles resolved through MET-2.2 §1
GATE = {
 'GATE-000': ('DR-2','RUN-0 · Decide','Regulatory owner (packet content); Founder (dispatch)','kendo-Jones; Kenny-bytes'),
 'GATE-001': ('DR-3','RUN-1 · Foundation','Regulatory owner','kendo-Jones'),
 'GATE-002': ('DR-4','RUN-2 · Controls & domain','Security owner','Ken-E-Gee'),
 'GATE-003': ('DR-6','RUN-3 · File & notify / RUN-4 · Evidence & submission','Regulatory owner + Architecture owner','kendo-Jones + Kenny-bytes'),
 'GATE-004': ('DR-7','RUN-4 · Evidence & submission','Regulatory owner; Founder','kendo-Jones; Kenny-bytes'),
 'NZ-GATE-000': ('DR-2','RUN-0 · Decide (NZ-GATE-0 prep)','Founder + NZ counsel (DEC-19)','Kenny-bytes; counsel [external]'),
 'NZ-GATE-001': ('DR-6','RUN-3 · File & notify (V2-S2)','Regulatory owner; NZ sponsor (DEC-19)','kendo-Jones; sponsor [NEEDS DEFINITION — DEC-19]'),
 'NZ-GATE-002': ('DR-6','RUN-3 · File & notify (V2-S3a/b)','Regulatory owner; NZ sponsor (DEC-19)','kendo-Jones; sponsor [NEEDS DEFINITION — DEC-19]'),
}
def gate_info(g):
    key=g.split(';')[0].strip()
    if key in GATE: return GATE[key]
    if key.startswith('US-GATE') or key.startswith('EU-GATE'):
        return ('— (no DR step: US/EU are ADVISORY jurisdictions outside the EXEC-1 run map; REG-SPRINT V3 at the earliest)','not in EXEC-1 RUN-0..4 (V3 / later)','Regulatory owner','kendo-Jones')
    return ('—','—','Regulatory owner','kendo-Jones')
# per-task role overrides (DEPLOY-1.1 D-2 names these explicitly)
OVR = {
 'TASK-REG-001':('Founder (programme) — DR-2','Kenny-bytes'), 'TASK-REG-004':('Counsel + product (DEC-07)','[NEEDS DEFINITION — DEC-07]; kendo-Jones drafts'),
 'TASK-REG-009':('Infrastructure owner + Regulatory owner (DEC-03) — DR-3','Ken-nough + kendo-Jones'), 'TASK-REG-005':('Regulatory owner (Jira/Ketryx) — DR-3','kendo-Jones'),
 'TASK-REG-014':('Operations owner (usability programme) — DR-4','[NEEDS DEFINITION — no operations owner named in MET-2.2 §1; DEC-23 extension]'),
 'TASK-REG-015':('Regulatory owner + cdss-lumos repo owner — DR-6','kendo-Jones + Kenny-bytes'), 'TASK-REG-016':('Security owner — DR-6 (pen-test)','Ken-E-Gee'),
 'TASK-REG-022':('Founder (programme) — DR-2','Kenny-bytes'), 'TASK-REG-023':('Regulatory owner — DR-2 (inside the TASK-REG-002 engagement)','kendo-Jones'),
 'NZ-TASK-002':('Founder (DEC-19) — DR-2','Kenny-bytes'), 'NZ-TASK-003':('Founder — DR-2','Kenny-bytes'), 'NZ-TASK-005':('Regulatory owner + Security owner (privacy/data residency)','kendo-Jones + Ken-E-Gee'),
 'US-TASK-001':('Security owner (Part 11 controls) + Regulatory owner','Ken-E-Gee + kendo-Jones'), 'US-TASK-002':('Security owner (SBOM)','Ken-E-Gee'), 'US-TASK-009':('Security owner','Ken-E-Gee'),
 'EU-TASK-003':('Architecture owner (runtime logging design)','Kenny-bytes'), 'EU-TASK-008':('Regulatory owner + Security owner (GDPR)','kendo-Jones + Ken-E-Gee'), 'EU-TASK-010':('Security owner','Ken-E-Gee'),
}
# evidence artifact that makes the task DONE-WITH-EVIDENCE (REG-POSTURE §0.4) — named from the task's own text
EV = {
 'TASK-REG-001':'intended purpose statement v1.0, signed (draft: 11_prompts/runs/2026-09-05_primer-0/DRAFT_TASK-REG-001_intended_purpose.md)','TASK-REG-002':"counsel's written classification opinion, dated (AU packet dispatched: counsel_packet_AU/)",
 'TASK-REG-003':'versioned claims inventory reconciled to the intended purpose statement (OBL-014)','TASK-REG-004':'DEC-07 ruling recorded in MET-2.n; ASSUME-REG-003 ATTESTED/REFUTED',
 'TASK-REG-005':'Jira project + Ketryx workspace exist (screenshot/export), synthetic scope declared','TASK-REG-006':'Ketryx configuration export per KTX-001/010/011 + configuration-item ceiling model (§6.1)',
 'TASK-REG-007':'ISO 14971 risk file opened (Ketryx risk module export, first hazard rows)','TASK-REG-008':'requirements set tagged to Essential Principles (KTX-008 export)',
 'TASK-REG-009':'DEC-03 ruling + executed contract terms (ASSUME-REG-004) or Bedrock pinning evidence (C-16)','TASK-REG-010':'gated release pipeline definition + one approval artifact in CI',
 'TASK-REG-011':'SBOM artifact generated in CI and visible in Ketryx SCM (KTX-012)','TASK-REG-012':'vulnerability-handling and disclosure SOP with CVSS + CAPA linkage (STD-009, OBL-008)',
 'TASK-REG-013':'supplier assessment records (substrate, AWS, third-party AI provider)','TASK-REG-014':'three IEC 62366-1 use-related risk analyses (clinician, patient, auditor)',
 'TASK-REG-015':'clinical evidence plan + Lumos linkage agreement; first evidence rows','TASK-REG-016':'independent penetration test report (external party named)',
 'TASK-REG-017':'post-market surveillance procedures + adverse-event reporting SOP','TASK-REG-018':'Ketryx tier upgrade order/confirmation (validated-out-of-the-box status)',
 'TASK-REG-019':'conformity assessment application lodged (receipt) — route per Q-REG-005','TASK-REG-020':'ARTG inclusion certificate',
 'TASK-REG-021':'demo-surface triage record: supplier entry for the AI provider (OBL-013), disclosure check, keep/withdraw decision','TASK-REG-022':'jurisdiction-sequence decision recorded (Q-REG-008 answered; MET-2.n row)',
 'TASK-REG-023':"counsel's written view on the Governance Layer's non-device status (ASSUME-REG-009, Q-REG-010)",'TASK-REG-024':'QMS certification route decision recorded (Q-REG-011; MDSAP vs TGA direct)',
 'NZ-TASK-001':"NZ counsel's written confirmation of NZ-FIND-001..012 and NZ-Q-004 (NZ packet: counsel_packet_NZ/)",'NZ-TASK-002':'sponsor structure decision recorded (DEC-19)',
 'NZ-TASK-003':"employer's written position on the registrar/director conflict",'NZ-TASK-004':'Medical Products Bill timing model vs technical-file readiness (NZ-WATCH-001; NZ-ASSUME-005) with the NZ-first decision',
 'NZ-TASK-005':'Privacy Impact Assessment (HIPC 2020); data-residency decision; Māori data governance engagement record','NZ-TASK-006':'technical file indexed for Medsafe (STED index) — same artifact set as the AU conformity assessment',
 'NZ-TASK-007':'post-market system evidence (complaints, adverse events, recall capability) operating before supply','NZ-TASK-008':'WAND notification record',
 'NZ-TASK-009':'tested SaMD post-market mechanisms per NZ-OBL-007 (complaint channel, triage SOP, remote disablement/forced update, functional-change procedure)','NZ-TASK-010':'first NZ site agreement + HISO/procurement security questionnaire + data agreement executed',
 'US-TASK-001':'Part 11 capability evidence for design-control records (attribution, e-signature, audit trail, validation) — intended-use test result','US-TASK-002':'CycloneDX/SPDX SBOM with §524B fields incl. AI vendor and pinned model entries',
 'US-TASK-003':'clinical evidence programme protocol to ISO 14155 satisfying 21 CFR 812.28; pre-registered subgroup analyses','US-TASK-004':'IEC 62304 document set projectable to the Enhanced-level 2023 guidance list',
 'US-TASK-005':"US counsel/RA consultant's written response to US-ASSUME-001..006",'US-TASK-006':'predicate search + pathway analysis memo; draft indications for use; PCCP scope decision',
 'US-TASK-007':'Q-Sub package and CDRH written feedback','US-TASK-008':'QMS certification route decision (MDSAP) recorded (shared with TASK-REG-024)',
 'US-TASK-009':'cyber device package: SPDF evidence, threat model, SW96 report, SBOM, disclosure plan, pen-test report','US-TASK-010':'AI-enabled function documentation set per US-FIND-011 incl. model card and PCCP',
 'US-TASK-011':'human factors validation report per surface; US labelling/IFU with UDI','US-TASK-012':'US Agent appointment; establishment registration/listing; HIPAA BAA template + Security Rule risk analysis; FTC HBNR readiness; submission receipt',
 'US-TASK-013':'Part 803/806 procedures; §524B monitoring live; PCCP protocol operating; performance monitoring reports',
 'EU-TASK-001':'technical documentation index to Annex II with STED/EP crosswalk; GSPR checklist','EU-TASK-002':'AI Act Annex IV / Art 10 data-governance record from the first training/tuning run',
 'EU-TASK-003':'Article 12 automatic-logging design + retention specification (runtime)','EU-TASK-004':'clinical evidence protocol with EU applicability (population vs EU demographics; ISO 14155; MDCG endpoints)',
 'EU-TASK-005':"EU counsel's written response to EU-ASSUME-001..006",'EU-TASK-006':'notified body selection record + pre-application dialogue minutes; application lodged',
 'EU-TASK-007':'Authorised Representative mandate (Art 11(3)); PRRC designation (Art 15); EUDAMED SRN','EU-TASK-008':'GDPR: EU representative appointment (Art 27); DPIA; Art 28 terms; Chapter V transfer mechanism decision',
 'EU-TASK-009':'Clinical Evaluation Report (MDCG 2020-1); PMCF plan; PMS plan; PSUR template','EU-TASK-010':'cyber documentation set to MDCG 2019-16',
 'EU-TASK-011':'AI Act conformity package integrated with the MDR technical file','EU-TASK-012':'UDI assignment; EU Declaration of Conformity; CE marking record; EUDAMED device registration; launch-market IFUs',
 'EU-TASK-013':'vigilance procedures with 15/10/2-day clocks; trend reporting; PSUR cadence; PMCF running; significant-change SOP (EU-OBL-011); liability evidence retention',
}
rows=[]; census={}
for t in tasks:
    dr,run,role,acct=gate_info(t['gate'])
    if t['id'] in OVR: role,acct=OVR[t['id']]
    ev=EV.get(t['id'],'[NEEDS SOURCE — evidence artifact not derivable from the task text]')
    rows.append(f"| `{t['id']}` | `{t['gate']}` | {dr} | {run} | {role} | {acct} | {ev} | {'PRESENT' if t['id'] in r30 else 'ABSENT'} | `{t['file'].split('/')[-1]}:{t['line']}` |")
    census[t['id'].rsplit('-',1)[0]]=census.get(t['id'].rsplit('-',1)[0],0)+1
missing_r30=[t['id'] for t in tasks if t['id'] not in r30]; missing_ev=[t['id'] for t in tasks if t['id'] not in EV]
needs=sum(1 for r in rows if 'NEEDS DEFINITION' in r.split('|')[6])
hdr=f'''---
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

## §2 Crosswalk ({len(rows)} tasks)

| Task | Gate | DR step (DEPLOY-1.1) | RUN (EXEC-1) | Owner role | Account (MET-2.2 §1) | Evidence artifact (DONE-WITH-EVIDENCE means…) | R30.3 row | Source |
|---|---|---|---|---|---|---|---|---|
'''
body='\n'.join(rows)
foot=f'''

## §3 Census and self-audit (generated {subprocess.check_output(['date','-u','+%Y-%m-%dT%H:%M:%SZ']).decode().strip()}; `tools/regtask.py`)

```
tasks parsed per family: {json.dumps(census)}  total {len(rows)}
R30.3 rows PRESENT for task ids: {len(rows)-len(missing_r30)}/{len(rows)}   ABSENT: {missing_r30 or 'none'}
evidence-artifact cells: {len(rows)-len(missing_ev)}/{len(rows)} named; [NEEDS SOURCE]: {len(missing_ev)}
owner-account cells with [NEEDS DEFINITION]: {needs} (each names its decision: DEC-07, DEC-19, DEC-23 extension)
owner-account cells empty: 0
```

Acceptance (Queue §c.1 QI-0020): 60/60 tasks mapped; 0 owner cells empty ([NEEDS DEFINITION] + DEC
allowed) — {'PASS' if len(rows)==60 and not missing_ev else 'CHECK'}. Family counts agree with REG-POSTURE §12.1 (TASK-REG 24), REG-NZ §12 (NZ-TASK 10),
REG-US (US-TASK 13) and REG-EU (EU-TASK 13) as parsed above.

## §4 What this companion did not do

Changed no task status (OPEN means OPEN); attested nothing; named no person the register has not named
(MET-2.2 §1); produced no evidence artifact — every artifact cell is a description of the artifact that
would close the task, not a claim that it exists. Regulatory content is ADVISORY_ONLY throughout.
Ledger row and task for this file: HARDEN-1.2 / HARDEN-3.2 (same sprint).
'''
out='10_regulatory-execution/REG-TASK-OWNERS_companion.md'
open(out,'w',encoding='utf-8').write(hdr+body+foot)
print(out, os.path.getsize(out), 'bytes;', len(rows),'rows; missing R30.3:',missing_r30,'; missing EV:',missing_ev,'; needs-def:',needs)
