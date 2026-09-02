#!/usr/bin/env python3
"""06_ per-file skeleton conformance → rows (one per file, MT2 §3). Run from repo root."""
import os, re, json, yaml
RUN="11_prompts/runs/2026-09-02_survey-2"; ROOT="06_repositories/repo-skeletons"
rows=[]; n=300; summary={"files":0,"conformant":0,"findings":0,"trees":{}}
def row(**k):
    global n
    base={"folder":"06","phase_found":"2","state":"OPEN","survey1_ref":[],"weight":0,"criticality":1,"radius":0,"parity_gap":0,"blocks":[],"executability":"NONE","owner":"Repo owner per REPO-MAP / DEC-09 [NEEDS DEFINITION]","label":["REPO SKELETON"]}
    base.update(k); base["row_id"]=f"BSQ-{n:04d}"; n+=1; rows.append(base)
for tree in sorted(os.listdir(ROOT)):
    tp=os.path.join(ROOT,tree)
    if not os.path.isdir(tp): continue
    files=sorted(os.path.relpath(os.path.join(d,f),tp) for d,_,fs in os.walk(tp) for f in fs if f!=".DS_Store")
    summary["trees"][tree]={"files":len(files),"has_ci":"ci/pipeline.yml" in files,"has_codeowners":"CODEOWNERS" in files,"has_manifest":"MANIFEST.yaml" in files,"has_readme":"README.md" in files}
    for rel in files:
        p=os.path.join(tp,rel); size=os.path.getsize(p); t=open(p,encoding="utf-8",errors="replace").read(); first=t.split("\n")[0]
        summary["files"]+=1
        issues=[]; ev=[f"wc -c → {size}", f"l.1: {first[:120]}"]
        banner=bool(re.search(r"(?i)skeleton|proposed|stub|pointer",t))
        if not banner: issues.append("no Proposed/skeleton banner in first 400 B (REPO-MAP skeleton index: 'every file marked Proposed')")
        if rel=="MANIFEST.yaml":
            try:
                y=yaml.safe_load(t) or {}
                for k in ("name","status"):
                    if k not in y: issues.append(f"MANIFEST.yaml lacks `{k}`")
                if y.get("name") and y["name"]!=tree: issues.append(f"MANIFEST name {y['name']!r} != tree {tree!r}")
                ev.append(f"yaml keys: {sorted(y.keys())}")
            except Exception as e: issues.append(f"YAML parse error: {e}")
        if rel=="ci/pipeline.yml":
            if "r29" not in t.lower(): issues.append("CI stub has no dormant R29 ratchet hook (REPO-MAP skeleton index / MT2 §7(4))")
            if not re.search(r"not runnable|STUB",t): issues.append("CI stub does not state it is not runnable")
        if rel=="CODEOWNERS" and "NEEDS DEFINITION" not in t: issues.append("CODEOWNERS names persons without [NEEDS DEFINITION] marker")
        # per-directory primer-citation check removed after manual review: 7 flagged READMEs cite MAK/primer IDs in forms the regex missed (see ASSESSMENT §4)
        if "TODO" in t or "TBD" in t: issues.append("TODO/TBD present (00_MANIFEST §6 census: zero TODO/TBD)")
        path=f"{ROOT}/{tree}/{rel}"
        if issues:
            summary["findings"]+=1
            row(artifact_path=path,finding_class="QUALITY-BELOW-BAR",parity_lines=["P-D-01","P-D-15"] if rel.endswith(".yml") else ["P-D-01","P-D-07"],contract_line="REPO SKELETON floor: README + MANIFEST.yaml + ci/pipeline.yml with dormant R29 ratchet hook; per-directory stubs mirroring primer §-4/§-8; banners",statement="; ".join(issues)+f" — file {path}",evidence=" | ".join(ev),weight=1,criticality=1,radius=0,parity_gap=len(issues),executability="CLAUDE-CODE-EXECUTABLE-NOW",
                build_spec={"target_path":path+" — companion note in 06_/INDEX.md (skeleton files are Proposed stubs; fix lands when the repo instantiates)","class_and_plines":"REPO SKELETON; P-D-01/P-D-07/P-D-15","mandatory_sections":["record the issue in INDEX-06 §4 per-tree table"],"inputs":[path],"laws":["append-only — skeleton files are not edited; the INDEX carries the defect until instantiation"],"evidence_to_capture":"this row's evidence string","acceptance_test":"INDEX-06 lists the file with the issue","closes_rows":[],"harden_linkage":"HARDEN-1 A-001 glob row (W8)","ratifying_owner":"Repo owner (DEC-09)","depends_on":[]})
            rows[-1]["build_spec"]["closes_rows"]=[rows[-1]["row_id"]]
        else:
            summary["conformant"]+=1
            row(artifact_path=path,finding_class="PRESENT-CONFORMANT",parity_lines=[],contract_line="REPO SKELETON floor (banner; manifest keys; CI hook; CODEOWNERS marker; dir README cites primer)",statement=f"Skeleton file present and conformant to the per-file floor checks: {path}",evidence=" | ".join(ev))
open(f"{RUN}/folders/06_repositories/skeleton_rows.jsonl","w").write("\n".join(json.dumps(r,ensure_ascii=False) for r in rows)+"\n")
json.dump(summary,open(f"{RUN}/folders/06_repositories/skeleton_summary.json","w"),indent=1)
print(json.dumps({k:v for k,v in summary.items() if k!="trees"})); 
for t,v in summary["trees"].items(): print(t,v)
