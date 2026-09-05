#!/usr/bin/env python
"""Generate REG-R30.3_row-form_seed.jsonl: one row per ID in the R30 + R30.1 + R30.2 ranges, statement verbatim
from the defining table row (first cell backticked) in the source document; status crosswalked per REG-POSTURE §0.7
with source_status_verbatim preserved. Run from repo root. Prints census by family."""
import re, json, collections, sys
OUT="05_registers-and-contracts/REG-R30.3_row-form_seed.jsonl"
STAMP="PRE-L1: Imago 73460b3 + sprint-1 2026-09-05 (no lockfile pin-set yet)"
DOCS=[("AU","10_regulatory-execution/REG-POSTURE_v1.2.md","REG-POSTURE v1.2",r"(REG-FIND|REG-KEEP|ASSUME-REG|OBL|STD|FORK-REG|GATE|TASK-REG|KTX|WATCH-REG|Q-REG|SRC-REG)-[0-9]{3}"),
      ("NZ","10_regulatory-execution/REG-NZ_v1.1.md","REG-NZ v1.1",r"NZ-(FIND|OBL|STD|ASSUME|TASK|GATE|WATCH|Q|SRC)-[0-9]{3}"),
      ("US","10_regulatory-execution/REG-US_v1.0.md","REG-US v1.0",r"US-(FIND|OBL|STD|REG|ASSUME|TASK|GATE|WATCH|Q|SRC)-[0-9]{3}"),
      ("EU","10_regulatory-execution/REG-EU_v1.0.md","REG-EU v1.0",r"EU-(FIND|OBL|STD|LAW|ASSUME|TASK|GATE|WATCH|Q|SRC)-[0-9]{3}")]
# verbatim source statuses per family (R30 seed / R30.1 / R30.2 wording) and the §0.7 crosswalk
def fam_status(rid):
    f=rid.rsplit('-',1)[0] if not rid.startswith(('SG-','V1-','V2-','V3-')) else rid.split('-')[0]
    table={
     'REG-FIND':('OPEN','OPEN',False),'NZ-FIND':('OPEN','OPEN',False),'US-FIND':('OPEN','OPEN',False),'EU-FIND':('OPEN','OPEN',False),
     'ASSUME-REG':('OPEN','OPEN',False),'NZ-ASSUME':('OPEN','OPEN',False),'US-ASSUME':('OPEN','OPEN',False),'EU-ASSUME':('OPEN','OPEN',False),
     'REG-KEEP':('standing','OPEN',True),'OBL':('standing','OPEN',True),'NZ-OBL':('standing','OPEN',True),'US-OBL':('standing','OPEN',True),'EU-OBL':('standing','OPEN',True),
     'STD':('standing (editions pinned)','OPEN',True),'NZ-STD':('standing','OPEN',True),'US-STD':('standing (recognition status to confirm, US-WATCH-004)','OPEN',True),'EU-STD':('standing (harmonisation status to confirm, EU-WATCH-004)','OPEN',True),
     'FORK-REG':('OPEN (decision point L4, unchanged)','OPEN',False),
     'GATE':('not passed','OPEN',False),'NZ-GATE':('not passed','OPEN',False),'US-GATE':('not passed','OPEN',False),'EU-GATE':('not passed','OPEN',False),
     'TASK-REG':('not started','OPEN',False),'NZ-TASK':('not started','OPEN',False),'US-TASK':('not started','OPEN',False),'EU-TASK':('not started','OPEN',False),
     'KTX':('OPEN (vendor-stated; written confirmation pending) for 013..014; none stated at source for 001..012','OPEN',True),
     'WATCH-REG':('cadence word (see cadence)','OPEN',True),'NZ-WATCH':('cadence word (see cadence)','OPEN',True),'US-WATCH':('cadence word (see cadence)','OPEN',True),'EU-WATCH':('cadence word (see cadence)','OPEN',True),
     'Q-REG':('open','OPEN',False),'NZ-Q':('open','OPEN',False),'US-Q':('open','OPEN',False),'EU-Q':('open','OPEN',False),
     'SRC-REG':('recorded','OPEN',True),'NZ-SRC':('recorded','OPEN',True),'US-SRC':('recorded','OPEN',True),'EU-SRC':('recorded','OPEN',True),'US-REG':('recorded','OPEN',True),'EU-LAW':('recorded','OPEN',True),
     'NDG':('proposed-normative (activate on DEC-14)','OPEN',True),'SG':('not passed','OPEN',False),'SD':('→ MET-2.1 rows (SD-02 provisionally resolved, checkpoint month 4)','OPEN',True),
     'V1':('not started','OPEN',False),'V2':('not started','OPEN',False),'V3':('not started','OPEN',False),'EX':('in force on DEC-22','OPEN',True)}
    return table[f]
def cells(line): return [c.strip() for c in line.strip().strip('|').split('|')]
def header_for(lines,i):
    j=i
    while j>0 and lines[j].startswith('|'): j-=1
    j+=1
    return cells(lines[j]) if lines[j].startswith('|') else []
def section_for(lines,i):
    for j in range(i,-1,-1):
        if lines[j].startswith('#'): return lines[j].lstrip('#').strip()
    return ''
rows=[]; census=collections.Counter(); dupcheck=set()
def add(rid,statement,source,jur,shape,extra=None):
    if rid in dupcheck: return
    dupcheck.add(rid); verb,st,pend=fam_status(rid)
    r={"reg_id":rid,"statement":statement,"status":st,"source_status_verbatim":verb,"mapping_pending":pend,"source":source,"definition_shape":shape,"owner":"cdss-governance (register owner; row owner role per source)","jurisdiction":jur,"version_stamp":STAMP}
    if extra: r.update(extra)
    if 'WATCH' in rid and 'cadence' not in r: r['cadence']='[cadence not stated at source]'
    rows.append(r); census[rid.rsplit('-',1)[0] if not rid.startswith(('SG-','V1-','V2-','V3-')) else rid.split('-')[0]]+=1
for jur,path,docname,fam in DOCS:
    lines=open(path,encoding='utf-8').read().split('\n')
    pat=re.compile(r"^\|\s*`("+fam+r")`\s*(\*\*\[[^\]]*\]\*\*\s*)?\|")
    idrx=re.compile(r"`("+fam+r")`")
    defined=set()
    for i,l in enumerate(lines):
        m=pat.match(l)
        if m:
            rid=m.group(1); c=cells(l); h=header_for(lines,i)
            statement=c[1] if len(c)>1 else ''
            extra={}
            hl=[x.lower() for x in h]
            for k,key in (('attesting party','attesting_party'),('who','attesting_party'),('cadence','cadence'),('blocks','blocks'),('blocking','blocks'),('gate','blocks')):
                for idx,hn in enumerate(hl):
                    if hn.startswith(k) and idx<len(c) and c[idx]:
                        val=c[idx]
                        extra[key]=[val] if key=='blocks' else val
            # statement column: prefer a header named Statement/Finding/Obligation/Assumption/Task/Question/Item/Standard/Gate/Source/Instrument/Decision
            for idx,hn in enumerate(hl):
                if idx==0 or idx>=len(c) or not hn: continue
                if hn.split()[0].strip('*') in ('statement','finding','obligation','assumption','task','question','item','standard','gate','source','instrument','decision','watch','requirement','commitment','meaning'):
                    statement=c[idx]; break
            add(rid,statement,f"{docname} §{section_for(lines,i)} (table row l.{i+1})",jur,'table-row',extra); defined.add(rid)
    # legacy-shape ids (referenced, defined in prose) — AU v1.1-era per §12.2 check 2
    allids=set(m.group(1) for m in idrx.finditer('\n'.join(lines)))
    for rid in sorted(allids-defined):
        for i,l in enumerate(lines):
            if f"`{rid}`" in l and not l.startswith('|'):
                add(rid,l.strip()[:600],f"{docname} §{section_for(lines,i)} (prose l.{i+1})",jur,'prose'); break
        else:
            for i,l in enumerate(lines):
                if f"`{rid}`" in l:
                    add(rid,l.strip()[:600],f"{docname} §{section_for(lines,i)} (field-table l.{i+1})",jur,'prose'); break
# MAK-GOV NDG-1..14 (headings + Statement line)
L=open("10_regulatory-execution/MAK-GOV_addendum-g_v0.9.md",encoding='utf-8').read().split('\n')
for i,l in enumerate(L):
    m=re.match(r"^### (NDG-\d+) \((MUST|SHOULD|MAY)\)",l)
    if m:
        st=' '.join(x.strip() for x in L[i+1:i+6]).split('**Rationale trace')[0].replace('**Statement:**','').strip()
        add(m.group(1),st,f"MAK-GOV v0.9 §3 {m.group(1)} ({m.group(2)}) (heading l.{i+1})","AU",'heading',{"owner":"cdss-governance (MAK-GOV build target; DEC-14 activates)"})
# EXEC-1 EX-1..10
L=open("10_regulatory-execution/EXEC-1_execution_directive.md",encoding='utf-8').read().split('\n')
for i,l in enumerate(L):
    m=re.match(r"^### (EX-\d+) \((MUST|SHOULD|MAY)\)",l)
    if m:
        st=' '.join(x.strip() for x in L[i+1:i+8]).split('**Rationale trace')[0].replace('**Statement:**','').strip()
        add(m.group(1),st[:700],f"EXEC-1 v1.0 {m.group(1)} ({m.group(2)}) (heading l.{i+1})","AU",'heading')
# REG-SPRINT v1.0 (+1.1) — V*, SG-*, SD-* from tables; SG gates defined in Exit cells
for path,name in (("10_regulatory-execution/REG-SPRINT_v1.0.md","REG-SPRINT v1.0"),("10_regulatory-execution/REG-SPRINT-1.1_delta.md","REG-SPRINT-1.1")):
    L=open(path,encoding='utf-8').read().split('\n')
    for i,l in enumerate(L):
        m=re.match(r"^\|\s*`((V[123]-[SCE]\d[ab]?)|(SD-\d\d))`\s*\|",l)
        if m:
            c=cells(l); add(m.group(1),c[1],f"{name} §{section_for(L,i)} (table row l.{i+1})","AU",'table-row',{"blocks":[x for x in re.findall(r"`(SG-V\d-\d[ab]?|NZ-GATE-\d|GATE-\d{3})`",l)]})
        for g in re.findall(r"`(SG-V\d-\d[ab]?)`",l):
            if g not in dupcheck:
                add(g,l.strip()[:400],f"{name} §{section_for(L,i)} (exit cell l.{i+1})","AU",'prose')
# R30.1-listed SG-V2-3a/3b and V2-S3a/b come from the 1.1 delta table; ensure SG-V2-3 (v1.0) present
for g in ("SG-V2-3a","SG-V2-3b"):
    add(g,"SG-V2-3a / SG-V2-3b — gates of the split V2-S3a (WAND notification) / V2-S3b (first commercial site) milestones; minted register-side in R30.1 ('SG-V1-0..2 / SG-V2-0..3a/3b not passed'); the document-side split is REG-SPRINT-1.1 D-2","REG-R30.1 seed delta (new rows list) + REG-SPRINT-1.1 D-2","AU",'prose')
with open(OUT,'w',encoding='utf-8') as f:
    for r in rows: f.write(json.dumps(r,ensure_ascii=False)+'\n')
print("rows:",len(rows)); 
for k,v in sorted(census.items()): print(f"  {k}: {v}")
