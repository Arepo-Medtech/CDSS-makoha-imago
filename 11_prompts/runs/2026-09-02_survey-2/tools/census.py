#!/usr/bin/env python3
"""Phase 1 census for PROMPT-SURVEY-2. Run from repository root:
   python3 11_prompts/runs/2026-09-02_survey-2/tools/census.py
Writes census.json, CENSUS.md, id_census.json into the run dir. Stdlib only."""
import os, re, json, sys, hashlib
ROOT = os.getcwd()
RUN = "11_prompts/runs/2026-09-02_survey-2"
TARGETS = ["04_hardening","05_registers-and-contracts","06_repositories","07_deployment-and-operations","08_research","09_diagrams","10_regulatory-execution"]
DECLARED = {"04_hardening":("4","00_MANIFEST §1"),"05_registers-and-contracts":("5","00_MANIFEST §1 (4) + §8 (+1 REG-R30.1)"),"06_repositories":("91","00_MANIFEST §7 A-001 ('5 files to 91')"),"07_deployment-and-operations":("5","00_MANIFEST §1"),"08_research":("1","00_MANIFEST §1"),"09_diagrams":("5","00_MANIFEST §1"),"10_regulatory-execution":("7","00_MANIFEST §8 A-002")}
NS = {
 "CC":r"CC-\d", "T":r"T-\d{3}", "W":r"W\d{1,2}", "R":r"R\d{1,2}", "DEC":r"DEC-\d\d", "C":r"C-\d\d", "G":r"G-\d\d", "RG":r"RG-\d\d",
 "EX":r"EX-\d{1,2}", "RUN":r"RUN-\d", "NDG":r"NDG-\d{1,3}", "TASK-REG":r"TASK-REG-\d{3}", "ASSUME-REG":r"ASSUME-REG-\d{3}", "NZ-ASSUME":r"NZ-ASSUME-\d{3}",
 "NZ-Q":r"NZ-Q-\d{3}", "NZ-TASK":r"NZ-TASK-\d{3}", "Q-REG":r"Q-REG-\d{3}", "GATE":r"GATE-\d{3}", "SG":r"SG-V\d-\d", "REG-FIND":r"REG-FIND-\d{3}", "WATCH-REG":r"WATCH-REG-\d{3}",
 "OBL":r"OBL-\d{3}", "KTX":r"KTX-\d{3}", "GPP":r"GPP-\d{1,2}", "SPINE":r"SPINE-\d", "D":r"D-\d", "A":r"A-\d{3}", "DEF":r"DEF-\d{3}", "V":r"V\d-[SCE]\d[a-z]?", "AN":r"AN-\d{1,2}",
}
LB = r"(?<![A-Za-z0-9_\-./])"; LA = r"(?![A-Za-z0-9_])"
def tok_re(p): return re.compile(LB + p + LA)
RANGE = re.compile(r"(?<![A-Za-z0-9\-])([A-Z][A-Z\-]*-)(\d{2,3})\s*(?:\.\.|–|-)\s*(\d{2,3})(?![0-9])")
def expand_ranges(text):
    out=set()
    for m in RANGE.finditer(text):
        pfx,a,b=m.group(1),m.group(2),m.group(3)
        if int(b)>=int(a) and int(b)-int(a)<200:
            for n in range(int(a),int(b)+1): out.add(f"{pfx}{str(n).zfill(len(a))}")
    return out
def walk(root=ROOT):
    for d,_,fs in os.walk(root):
        rel=os.path.relpath(d,ROOT)
        if rel.startswith(RUN) or "/.git" in d or rel.startswith(".git"): continue
        for f in fs:
            if f==".DS_Store": continue
            yield os.path.normpath(os.path.join(rel,f))
def read(p):
    try: return open(p,encoding="utf-8",errors="replace").read()
    except Exception as e: return ""
def frontmatter(text):
    if not text.startswith("---"): return None
    lines=text.split("\n"); fm={}; 
    for ln in lines[1:]:
        if ln.strip()=="---": return fm
        m=re.match(r"^([A-Za-z_][A-Za-z0-9_\-]*):\s*(.*)$",ln)
        if m: fm[m.group(1)]=m.group(2).strip().strip('"')
    return None  # unterminated
allfiles=sorted(walk())
# --- definition positions across whole tree
DEFPOS=[re.compile(r"^\s{0,3}#{1,6}\s*\**\s*("+"|".join(NS.values())+")"),  # heading start
        re.compile(r"^\|\s*[`*]*\s*("+"|".join(NS.values())+")"),               # first table cell (backtick/bold allowed)
        re.compile(r"^\s*[-*]\s+\**\s*("+"|".join(NS.values())+")"),          # list item start
        re.compile(r"^\s*[`*]*("+"|".join(NS.values())+")[`*]*\s*[:—–\-(]|^\s*[`*]*("+"|".join(NS.values())+")\s+(OPEN|MUST|SHOULD|MAY)\b"),  # "ID —" / "ID OPEN" line start
        re.compile(r'"('+"|".join(NS.values())+r')"')]                        # JSON census strings
defined={}  # id -> set(files)
texts={}
for p in allfiles:
    if not p.endswith((".md",".json",".yaml",".yml",".mermaid",".html",".txt")): continue
    t=read(p); texts[p]=t
    for ln in t.split("\n"):
        for rx in DEFPOS:
            m=rx.match(ln) if rx.pattern.startswith("^") else rx.search(ln)
            if m:
                tok=m.group(1); defined.setdefault(tok,set()).add(p)
    for tok in expand_ranges(t): defined.setdefault(tok,set()).add(p+" (range)")
# R-registers: Arch §12.2 defines rows by bare number; treat R1..R30 as defined by Arch §12.2 / §14.3
for n in range(1,29): defined.setdefault(f"R{n}",set()).add("02_cdss-stack-augmented/architecture_and_integration.md (§12.2 master table, bare-number row)")
for n in (29,30): defined.setdefault(f"R{n}",set()).add("02_cdss-stack-augmented/architecture_and_integration.md (§14.3)")
# W waves defined in HARDEN-3
for n in range(0,12): defined.setdefault(f"W{n}",set()).add("04_hardening/HARDEN-3_hardening_plan_worklist.md (wave table)")
census={"run":RUN,"targets":{}}
for T in TARGETS:
    files=[p for p in allfiles if p.startswith(T+"/")]
    rows=[]
    for p in files:
        size=os.path.getsize(p); ext=os.path.splitext(p)[1]
        t=texts.get(p,"")
        fm=frontmatter(t) if ext==".md" else None
        head=""
        if ext==".md" and fm is None: head=t.split("\n")[0][:120]
        if ext in (".json",):
            try: j=json.loads(t); head=f"$id={j.get('$id','')} title={j.get('title','')}"
            except Exception as e: head=f"JSON PARSE ERROR: {e}"
        if ext in (".yaml",".yml",".mermaid",".html",".py"): head=t.split("\n")[0][:160]
        cited={}
        for ns,pat in NS.items():
            for m in tok_re(pat).finditer(t): cited.setdefault(m.group(0),0); cited[m.group(0)]+=1
        # defined here?
        defined_here=sorted({tok for tok,fs in defined.items() if any(f.split(" ")[0]==p for f in fs)})
        dangling=sorted(tok for tok in cited if tok not in defined)
        # declared counts
        req_count=fm.get("req_count") if fm else None; req_prefix=(fm.get("req_prefix") or fm.get("req_prefixes")) if fm else None
        counted_blocks=len(re.findall(r"^#{2,4}\s+(?:[A-Z]{1,6}-\d{1,3})\s*\((MUST|SHOULD|MAY)\)",t,re.M))
        rows.append({"path":p,"bytes":size,"ext":ext,"frontmatter":fm,"frontmatter_keys":sorted(fm.keys()) if fm else None,"head_in_lieu":head,
                     "has_doc_id":bool(fm and "doc_id" in fm),"missing_core_fields":[k for k in ("doc_id","title","version","date","status") if not fm or k not in fm] if ext==".md" else None,
                     "req_prefix":req_prefix,"req_count":req_count,"requirement_blocks_counted":counted_blocks,
                     "rationale_trace_lines":len(re.findall(r"Rationale trace",t)),
                     "has_contents":bool(re.search(r"^##?#?\s*(Contents|Table of contents|§?16 — Document-set index)",t,re.M|re.I)),
                     "has_id_census":bool(re.search(r"census",t,re.I)),
                     "has_self_audit":bool(re.search(r"self-audit|Self-audit",t)),
                     "has_traceability":bool(re.search(r"traceab|Rationale trace|Source",t,re.I)),
                     "placeholders":{k:len(re.findall(re.escape(k),t)) for k in ("[NEEDS DEFINITION","[NEEDS SOURCE","[UNAVAILABLE]","PENDING-VALIDATOR","PENDING-REGISTER-HOME","PENDING-ENUMERATION","TODO","TBD")},
                     "ids_cited":cited,"ids_defined_here":defined_here,"ids_dangling_candidates":dangling})
    declared,src=DECLARED[T]
    census["targets"][T]={"declared_count":declared,"declared_source":src,"disk_count":len(files),"total_bytes":sum(r["bytes"] for r in rows),"files":rows}
json.dump(census,open(f"{RUN}/census.json","w"),indent=1,ensure_ascii=False)
json.dump({k:sorted(v) for k,v in sorted(defined.items())},open(f"{RUN}/id_definitions.json","w"),indent=0,ensure_ascii=False)
# CENSUS.md
L=["# CENSUS — seven target folders (mechanical)","",f"Produced by `python3 {RUN}/tools/census.py` from repository root on 2026-09-02. Every number below is script output; `.DS_Store` excluded; run directory excluded.","",
   "## 1. Per-folder counts vs 00_MANIFEST","","| Folder | Declared (source) | On disk | Bytes | Match |","|---|---|---|---|---|"]
for T,d in census["targets"].items():
    L.append(f"| {T} | {d['declared_count']} ({d['declared_source']}) | {d['disk_count']} | {d['total_bytes']:,} | {'PASS' if str(d['disk_count'])==d['declared_count'] else 'INVENTORY-DRIFT'} |")
L+=["","## 2. File list, frontmatter census, declared-vs-counted","","Legend: core = doc_id·title·version·date·status present in YAML frontmatter; `—` = not a .md; `NONE` = no frontmatter.",""]
for T,d in census["targets"].items():
    L+=[f"### {T} ({d['disk_count']} files, {d['total_bytes']:,} B)","","| Path | Bytes | Frontmatter core missing | req_prefix / req_count | req blocks counted | Rationale-trace lines | Contents | census | self-audit | placeholders | head-in-lieu |","|---|---|---|---|---|---|---|---|---|---|---|"]
    for r in d["files"]:
        miss = "—" if r["missing_core_fields"] is None else ("NONE (no frontmatter)" if r["frontmatter"] is None else (", ".join(r["missing_core_fields"]) or "all present"))
        ph=", ".join(f"{k}×{v}" for k,v in r["placeholders"].items() if v) or "none"
        L.append(f"| `{r['path']}` | {r['bytes']:,} | {miss} | {r['req_prefix'] or ''} / {r['req_count'] or ''} | {r['requirement_blocks_counted']} | {r['rationale_trace_lines']} | {'Y' if r['has_contents'] else 'N'} | {'Y' if r['has_id_census'] else 'N'} | {'Y' if r['has_self_audit'] else 'N'} | {ph} | {r['head_in_lieu'].replace('|','/')[:90]} |")
    L.append("")
L+=["## 3. ID census — cited-but-undefined candidates (DANGLING-REF candidates; confirmed manually in Phase 1 step 3)",""]
for T,d in census["targets"].items():
    for r in d["files"]:
        if r["ids_dangling_candidates"]:
            L.append(f"- `{r['path']}`: {', '.join(r['ids_dangling_candidates'])}")
L+=["","## 4. IDs defined in target files (heading / first-cell / list / range positions)",""]
for T,d in census["targets"].items():
    for r in d["files"]:
        if r["ids_defined_here"]: L.append(f"- `{r['path']}` defines: {', '.join(r['ids_defined_here'][:60])}{' …' if len(r['ids_defined_here'])>60 else ''} ({len(r['ids_defined_here'])})")
open(f"{RUN}/CENSUS.md","w").write("\n".join(L)+"\n")
print("files in tree (excl .DS_Store, run dir):",len(allfiles))
for T,d in census["targets"].items(): print(T,d["disk_count"],d["total_bytes"])
