"""graph.py — inbound/outbound reference graph per in-scope file (references = backticked or bare path fragments and basenames of tracked files).
Reachability from README.md → 00_MANIFEST → INDEX files → file. Design-graph orphan = inbound edges only from HARDEN-1.1 / HARDEN-3.1 (ledger/tasks) or an INDEX §2 table, and none from any other document."""
import re, json, sys, os, collections; sys.path.insert(0, __file__.rsplit('/',1)[0]); import scope
fs=scope.files(); fset=set(fs); base={}
for f in fs: base.setdefault(os.path.basename(f),[]).append(f)
texts={f:open(f,encoding='utf-8',errors='replace').read() for f in fs if f.endswith(('.md','.html','.mermaid','.json','.jsonl','.yaml','.yml','.txt','.py'))}
# aliases: frontmatter doc_id; for 11_prompts the token before the first underscore (PROMPT-A, PROMPT-PRM-ABC, PROMPT-SURVEY-3)
alias={}
for f,t in texts.items():
    a=set()
    if t.startswith('---'):
        m=re.search(r'^doc_id:\s*"?([A-Za-z0-9][A-Za-z0-9.\-]+)',t.split('\n---',1)[0],re.M)
        if m and len(m.group(1))>=5: a.add(m.group(1))
    if f.startswith('11_prompts/') and '_' in os.path.basename(f): a.add(os.path.basename(f).split('_')[0])
    alias[f]=a
def mentions(t,tok): return re.search(re.escape(tok)+r'(?![A-Za-z0-9\-])',t) is not None
LEDGERS={'04_hardening/HARDEN-1.1_coverage_ledger_seed_delta.md','04_hardening/HARDEN-3.1_task_register_delta.md','04_hardening/HARDEN-1_coverage_ledger_seed.md','04_hardening/HARDEN-3_hardening_plan_worklist.md'}
INDEXES={f for f in fs if f.endswith('/INDEX.md')}|{'00_MANIFEST.md'}
inb=collections.defaultdict(set); outb=collections.defaultdict(set)
for src,t in texts.items():
    for tgt in fs:
        if tgt==src: continue
        b=os.path.basename(tgt); stem=b.rsplit('.',1)[0]
        if len(stem)<6 and b not in ('INDEX.md',): continue
        hit = (tgt in t) or (len(base[b])==1 and b!='README.md' and b!='INDEX.md' and b!='MANIFEST.yaml' and b!='CODEOWNERS' and b!='pipeline.yml' and b in t) or any(mentions(t,a) for a in alias.get(tgt,()) if not alias.get(src,set())&{a})
        if hit: outb[src].add(tgt); inb[tgt].add(src)
# reachability
reach=set(); frontier=['README.md']
while frontier:
    n=frontier.pop()
    if n in reach: continue
    reach.add(n); frontier.extend(outb.get(n,()))
rows=[]
for f in fs:
    src=inb.get(f,set()); non_ledger=[s for s in src if s not in LEDGERS and (s not in INDEXES or f.endswith('/INDEX.md'))]   # an INDEX's own parent is 00_MANIFEST/README — that inbound counts for it
    cls=('NO-INBOUND' if not src else 'LEDGER-ONLY' if all(s in LEDGERS for s in src) else 'LEDGER-OR-INDEX-ONLY' if not non_ledger else 'DESIGN-LINKED')
    rows.append({"file":f,"inbound":len(src),"outbound":len(outb.get(f,())),"reachable_from_README":f in reach,"class":cls,"design_inbound_examples":sorted(non_ledger)[:3]})
c=collections.Counter(r["class"] for r in rows)
print(json.dumps({"tool":"graph.py","files":len(fs),"reachable_from_README":sum(r["reachable_from_README"] for r in rows),"class_counts":dict(c),
 "orphans_in_design_graph":[r["file"] for r in rows if r["class"] in ('NO-INBOUND','LEDGER-ONLY','LEDGER-OR-INDEX-ONLY')],
 "unreachable":[r["file"] for r in rows if not r["reachable_from_README"]],"rows":rows},indent=1))
