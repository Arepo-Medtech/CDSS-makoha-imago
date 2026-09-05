"""schema_dupes.py — enums and pinned strings repeated across machine-readable assets (JSON schemas, MANIFEST.yaml, pipeline.yml, config.json)."""
import re, json, sys, collections, os; sys.path.insert(0, __file__.rsplit('/',1)[0]); import scope
fs=[f for f in scope.files() if f.endswith(('.json','.yaml','.yml')) and not f.endswith('.jsonl')]
enums=collections.defaultdict(set); strings=collections.defaultdict(set)
for f in fs:
    t=open(f,encoding='utf-8',errors='replace').read()
    for m in re.finditer(r'"enum"\s*:\s*\[([^\]]*)\]',t): enums[tuple(sorted(re.findall(r'"([^"]+)"',m.group(1))))].add(f)
    for m in re.finditer(r'"([^"\n]{8,})"|:\s*([A-Za-z\[][^\n#]{7,}?)\s*(?:#.*)?$',t,re.M):
        s=(m.group(1) or m.group(2)).strip(); strings[s].add(f)
dup_enums=[{"enum":list(k),"files":sorted(v)} for k,v in enums.items() if len(v)>1]
dup_strings=sorted([{"string":k,"files":len(v),"examples":sorted(v)[:3]} for k,v in strings.items() if len(v)>=3 and not k.startswith(('http','#'))],key=lambda x:-x["files"])[:40]
print(json.dumps({"tool":"schema_dupes.py","assets":len(fs),"enums_total":len(enums),"enums_duplicated_across_files":dup_enums,"pinned_strings_in_3plus_files":dup_strings},indent=1))
