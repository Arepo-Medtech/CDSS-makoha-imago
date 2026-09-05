#!/usr/bin/env python3
"""check_schema every *.schema.json under 05_ and validate every *.examples.jsonl against its schema; validate the R30 row-form seed. Exit 1 on any invalid."""
import json, glob, jsonschema, sys
from jsonschema import Draft202012Validator as V
bad = 0; out = ["## Schema validation", ""]
for sp in sorted(glob.glob("05_registers-and-contracts/*.schema.json")):
    s = json.load(open(sp)); V.check_schema(s); out.append(f"- `{sp}` check_schema OK")
    ex = sp.replace(".schema.json", ".examples.jsonl")
    try: rows = [json.loads(l) for l in open(ex) if l.strip()]
    except FileNotFoundError: rows = []
    v = V(s); agree = 0
    for r in rows:
        meta = {k: r.pop(k) for k in list(r) if k.startswith("_")}; errs = list(v.iter_errors(r)); verdict = "VALID" if not errs else "INVALID"
        exp = meta.get("_expect", "").startswith("VALID"); agree += (verdict == "VALID") == exp
    if rows: out.append(f"  - examples `{ex}`: {agree}/{len(rows)} verdicts agree with `_expect`"); bad += len(rows) - agree
seed = "05_registers-and-contracts/REG-R30.3_row-form_seed.jsonl"
s = json.load(open("05_registers-and-contracts/REG-R30.schema.json")); v = V(s); n = inv = 0
for l in open(seed):
    if l.strip(): n += 1; inv += bool(list(v.iter_errors(json.loads(l))))
out.append(f"- `{seed}`: {n} rows, {inv} invalid"); bad += inv
print("\n".join(out)); sys.exit(1 if bad else 0)
