#!/usr/bin/env python
"""Validate schema files (check_schema) and example .jsonl files; compare each row's _expect with the actual verdict."""
import sys, json, jsonschema
from jsonschema import Draft202012Validator as V
def check_schema(p):
    s=json.load(open(p)); V.check_schema(s); print(f"check_schema {p} → OK (Draft 2020-12)"); return s
def run(schema_path, examples_path):
    s=check_schema(schema_path); v=V(s); agree=0; n=0
    for i,line in enumerate(open(examples_path),1):
        line=line.strip()
        if not line: continue
        n+=1; row=json.loads(line); meta={k:row.pop(k) for k in list(row) if k.startswith('_')}
        errs=sorted(v.iter_errors(row), key=lambda e: str(e.path))
        verdict="VALID" if not errs else "INVALID: "+errs[0].message
        exp=meta.get('_expect','')
        ok = (verdict=="VALID")==(exp.startswith("VALID"))
        agree+=ok
        print(f"  line {i}  {meta.get('_example','?'):40s} → {verdict[:110]}   [{'agrees' if ok else 'DISAGREES'} with _expect]")
    print(f"  expected/actual agreement: {agree}/{n}\n")
if __name__=="__main__":
    for i in range(1,len(sys.argv),2): run(sys.argv[i], sys.argv[i+1])
