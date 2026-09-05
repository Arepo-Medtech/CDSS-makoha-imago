"""frontmatter.py — schema census per authored .md: core keys (doc_id,title,version,date,status), date-field variants, doc_id uniqueness with
supersedes-chain exemption, class-specific keys (req_prefix(es)+req_count when IDs are minted), heading-ladder skips, table column-count consistency.
Files without frontmatter are classified by WHY (retained-verbatim / skeleton-banner / companion / root-governance / omission)."""
import re, json, sys, collections; sys.path.insert(0, __file__.rsplit('/',1)[0]); import scope
CORE=["doc_id","title","version","date","status"]
rows=[]; ids=collections.defaultdict(list); nofm=collections.defaultdict(list); datevar=collections.Counter()
MINT=re.compile(r'(?m)^(?:### |\| )([A-Z][A-Z0-9]{0,11}(?:-[A-Z][A-Z0-9]{0,11})?)-(\d{1,4}[a-z]?)\b')
for f in scope.md_files():
    t=open(f,encoding='utf-8',errors='replace').read()
    if not t.startswith('---\n'):
        cls=('root-governance' if '/' not in f else 'retained-original' if f.startswith('02_') or 'MAJOR_TASK_2' in f else 'skeleton-banner' if f.startswith('06_repositories/repo-skeletons') else 'corpus-companion' if f.startswith('03_') else 'omission')
        nofm[cls].append(f); rows.append({"file":f,"frontmatter":False,"why":cls}); continue
    head=t.split('\n---',1)[0][4:]; keys=[l.split(':',1)[0].strip() for l in head.split('\n') if re.match(r'^[A-Za-z_]+\s*:',l)]
    missing=[k for k in CORE if k not in keys and not (k=='date' and any(x in keys for x in ('date_issued','guidance_currency_date')))]
    for k in keys:
        if k.startswith('date') or k.endswith('_date'): datevar[k]+=1
    m=re.search(r'^doc_id:\s*"?([^"\n]+)"?',head,re.M); did=m.group(1).strip() if m else None
    if did: ids[did].append(f)
    sup=bool(re.search(r'^supersedes:',head,re.M)); decl=bool(re.search(r'^req_prefix(es)?:|^id_prefixes:',head,re.M))
    body=t.split('\n---',1)[1]; body=re.sub(r'```.*?```','',body,flags=re.S)
    mints=sorted(set(MINT.findall(body)))
    fams=sorted(set(p for p,_ in mints))
    # heading ladder skips
    lv=[len(h) for h in re.findall(r'(?m)^(#{1,6}) ',body)]; skips=sum(1 for a,b in zip(lv,lv[1:]) if b>a+1)
    # table column consistency
    bad_tables=0
    for tb in re.findall(r'(?m)((?:^\|[^\n]*\n)+)',body):
        tb=re.sub(r'`[^`\n]*`','`c`',tb.replace('\\|','¦'))   # escaped pipes and code spans are not column separators
        cols={l.count('|') for l in tb.strip().split('\n') if l.strip()}
        if len(cols)>1: bad_tables+=1
    rows.append({"file":f,"frontmatter":True,"missing_core":missing,"doc_id":did,"supersedes":sup,"declares_prefix":decl,"minted_families":fams,"minted_count":len(mints),"ladder_skips":skips,"tables_inconsistent_columns":bad_tables})
dups={k:v for k,v in ids.items() if len(v)>1}
dup_report={k:{"files":v,"all_but_one_carry_supersedes":sum(1 for f in v if next(r for r in rows if r["file"]==f)["supersedes"])>=len(v)-1} for k,v in dups.items()}
withfm=[r for r in rows if r["frontmatter"]]
print(json.dumps({"tool":"frontmatter.py","md_files":len(rows),"with_frontmatter":len(withfm),"without_by_why":{k:len(v) for k,v in nofm.items()},"omissions":nofm.get('omission',[]),
 "missing_core_files":[(r["file"],r["missing_core"]) for r in withfm if r["missing_core"]],"date_field_variants":dict(datevar),"doc_id_repeats":dup_report,
 "mint_without_declaration":[(r["file"],r["minted_families"],r["minted_count"]) for r in withfm if r["minted_count"]>=3 and not r["declares_prefix"]],
 "ladder_skips_files":[(r["file"],r["ladder_skips"]) for r in withfm if r["ladder_skips"]],"tables_inconsistent":[(r["file"],r["tables_inconsistent_columns"]) for r in withfm if r["tables_inconsistent_columns"]],
 "rows":rows},indent=1))
