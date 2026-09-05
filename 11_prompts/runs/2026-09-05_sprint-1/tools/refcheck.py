#!/usr/bin/env python3
"""Reference resolution for target folders. Run from repo root. Writes refcheck.json + prints summary.
Checks: (1) backtick paths & markdown links → file exists; (2) §-anchors into named documents → heading exists."""
import os, re, json, glob
RUN="11_prompts/runs/2026-09-05_sprint-1"
TARGETS=["00_MANIFEST.md","04_hardening","05_registers-and-contracts","06_repositories","07_deployment-and-operations","08_research","09_diagrams","10_regulatory-execution"]
DOCS={"Arch":"02_cdss-stack-augmented/architecture_and_integration.md","MT2":"04_hardening/MAJOR_TASK_2_anti-laziness-hardening-directive.md",
      "MET-1":"01_north-star-and-transformation/MET-1_metamorphosis_plan_v1.0.md","REG-POSTURE":"10_regulatory-execution/REG-POSTURE_v1.2.md",
      "Primer 0":"02_cdss-stack-augmented/primer_0_ecosystem_explainer.md","HARDEN-2":"04_hardening/HARDEN-2_hardening_spec.md","REG-NZ":"10_regulatory-execution/REG-NZ_v1.1.md","EXEC-1":"10_regulatory-execution/EXEC-1_execution_directive.md","MAK-GOV":"10_regulatory-execution/MAK-GOV_addendum-g_v0.9.md","OPS-1":"07_deployment-and-operations/OPS-1_operating_procedures.md"}
heads={}
for k,p in DOCS.items():
    hs=set()
    for ln in open(p,encoding="utf-8",errors="replace"):
        m=re.match(r"^#{1,6}\s*(?:§)?([0-9]+(?:\.[0-9]+)?|[A-Z](?:\.[0-9]+)?)\b",ln)
        if m: hs.add(m.group(1))
    heads[k]=hs
allpaths=set()
for d,_,fs in os.walk("."):
    if RUN in d or "/.git" in d: continue
    for f in fs: allpaths.add(os.path.normpath(os.path.join(d,f)))
bynames={}
for p in allpaths: bynames.setdefault(os.path.basename(p),[]).append(p)
PATHRX=re.compile(r"`([^`\s]+?\.(?:md|json|yaml|yml|py|html|mermaid|txt|csv|rego|toml))`|`((?:\d\d_[A-Za-z0-9_\-]+/)[^`\s]*)`")
LINKRX=re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")
ANCH=re.compile(r"(Arch|MT2|MET-1|REG-POSTURE|Primer 0|HARDEN-2|REG-NZ|EXEC-1|MAK-GOV|OPS-1)\s*§\s*([0-9]+(?:\.[0-9]+)?|[A-Z](?:\.[0-9]+)?)")
out={"unresolved_paths":[],"resolved_by_basename":[],"unresolved_anchors":[],"stats":{}}
np=na=0
def iterfiles():
    for T in TARGETS:
        if os.path.isfile(T): yield os.path.dirname(T) or ".", os.path.basename(T); continue
        for d,_,fs in os.walk(T):
            if "/runs" in d or d.endswith("runs"): continue
            for f in fs: yield d,f
for d,f in iterfiles():
    if True:
        if True:
            if not f.endswith((".md",".yaml",".yml",".mermaid",".html",".json")): continue
            p=os.path.normpath(os.path.join(d,f)); t=open(p,encoding="utf-8",errors="replace").read()
            for n,ln in enumerate(t.split("\n"),1):
                cands=[]
                for m in PATHRX.finditer(ln): cands.append(m.group(1) or m.group(2))
                for m in LINKRX.finditer(ln):
                    u=m.group(1)
                    if not u.startswith(("http","#","mailto")): cands.append(u)
                for c in cands:
                    c=c.rstrip("/").split("#")[0]
                    if not c or c.startswith(("./","../")): c=os.path.normpath(os.path.join(d,c)) if c.startswith((".","..")) else c
                    np+=1
                    if os.path.normpath(c) in allpaths or os.path.exists(c): continue
                    if os.path.exists(os.path.join(d,c)): continue
                    b=os.path.basename(c)
                    if b in bynames: out["resolved_by_basename"].append({"file":p,"line":n,"ref":c,"found":bynames[b]}); continue
                    out["unresolved_paths"].append({"file":p,"line":n,"ref":c,"context":ln.strip()[:160]})
                for m in ANCH.finditer(ln):
                    doc,sec=m.group(1),m.group(2); na+=1
                    if sec not in heads[doc]:
                        out["unresolved_anchors"].append({"file":p,"line":n,"ref":f"{doc} §{sec}","context":ln.strip()[:160]})
out["stats"]={"path_refs_checked":np,"anchor_refs_checked":na,"unresolved_paths":len(out["unresolved_paths"]),"resolved_by_basename_only":len(out["resolved_by_basename"]),"unresolved_anchors":len(out["unresolved_anchors"])}
json.dump(out,open(f"{RUN}/refcheck.json","w"),indent=1)
print(json.dumps(out["stats"]))
for k in ("unresolved_paths","resolved_by_basename","unresolved_anchors"):
    print("==",k)
    for r in out[k]: print(f"  {r['file']}:{r['line']} {r['ref']}" + (f" -> {r['found']}" if 'found' in r else f" | {r['context'][:110]}"))
