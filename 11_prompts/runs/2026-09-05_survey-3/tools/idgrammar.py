"""idgrammar.py — every minted ID (heading `### PFX-n` or first table cell `| PFX-n`): family, zero-padding form(s), minting file(s),
declared in that file's frontmatter (req_prefix/req_prefixes/id_prefixes)?, homed in a register (R30.3 seed / HARDEN-1.1 / MET-2)?, alias law present nearby?"""
import re, json, sys, collections; sys.path.insert(0, __file__.rsplit('/',1)[0]); import scope
MINT=re.compile(r'(?m)^(?:#{2,4} |\| )`?([A-Z][A-Z0-9]{0,11}(?:-[A-Z][A-Z0-9]{0,11})?)-(\d{1,4}[a-z]?)\b')
fam=collections.defaultdict(lambda:{"count":0,"files":collections.Counter(),"forms":collections.Counter(),"declared_in":set(),"undeclared_in":set()})
for f in scope.md_files():
    t=open(f,encoding='utf-8',errors='replace').read(); head=t.split('\n---',1)[0] if t.startswith('---') else ''
    decl=set()
    for m in re.finditer(r'^(?:req_prefix|req_prefixes|id_prefixes):\s*(.+)$',head,re.M): decl|=set(re.findall(r'[A-Z][A-Z0-9-]*',m.group(1)))
    body=re.sub(r'```.*?```','',t.split('\n---',1)[1] if head else t,flags=re.S)
    for p,n in MINT.findall(body):
        d=fam[p]; d["count"]+=1; d["files"][f]+=1; d["forms"][f"{len(n.rstrip('abcdefghijklmnopqrstuvwxyz'))}d"]+=1
        (d["declared_in"] if p in decl or any(p.startswith(x+'-') for x in decl) else d["undeclared_in"]).add(f)
# register homes
homes={}
try:
    import json as _j
    for l in open('05_registers-and-contracts/REG-R30.3_row-form_seed.jsonl',encoding='utf-8'):
        try: r=_j.loads(l); homes.setdefault(r.get('reg_id','').rsplit('-',1)[0],'R30.3')
        except Exception: pass
except FileNotFoundError: pass
for k in ('R29-row',): homes[k]='HARDEN-1.1'
homes['T']='HARDEN-3.1 (self; R29 on DEC-02)'; homes['G']='MET-4'; homes['RG']='RESEARCH-1.1 / INDEX-08 §3'; homes['CC']='HARDEN-2.1'; homes['DR']='DEPLOY-1.1'; homes['PROC']='OPS-1.1'; homes['TM']='SEC-2'
for k in ('DEC','C'): homes[k]='MET-2/MET-2.1'
out=[]
for p,d in sorted(fam.items(),key=lambda x:-x[1]["count"]):
    out.append({"family":p,"minted":d["count"],"minting_files":len(d["files"]),"top_file":d["files"].most_common(1)[0][0],"padding_forms":dict(d["forms"]),"declared_in_files":len(d["declared_in"]),"undeclared_in_files":sorted(d["undeclared_in"])[:4],"register_home":homes.get(p,"—")})
print(json.dumps({"tool":"idgrammar.py","families":len(out),"total_minted":sum(o["minted"] for o in out),"families_with_mixed_padding":[o["family"] for o in out if len(o["padding_forms"])>1],"families_never_declared":[o["family"] for o in out if o["declared_in_files"]==0 and o["minted"]>=3],"rows":out},indent=1))
