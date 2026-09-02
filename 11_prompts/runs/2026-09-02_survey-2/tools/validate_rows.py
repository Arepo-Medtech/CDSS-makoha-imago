#!/usr/bin/env python
"""Validate a .jsonl of BSQ rows against BSQ.schema.json. Usage: validate_rows.py <schema> <jsonl> [<jsonl>...]"""
import sys, json, jsonschema
schema = json.load(open(sys.argv[1]))
V = jsonschema.Draft202012Validator(schema)
total = bad = 0; ids = {}
for path in sys.argv[2:]:
    for n, line in enumerate(open(path), 1):
        line = line.strip()
        if not line: continue
        total += 1
        try:
            row = json.loads(line)
        except Exception as e:
            bad += 1; print(f"{path}:{n} JSON ERROR {e}"); continue
        errs = sorted(V.iter_errors(row), key=lambda e: e.path)
        if errs:
            bad += 1
            for e in errs: print(f"{path}:{n} {row.get('row_id','?')}: {e.message}")
        rid = row.get("row_id")
        if rid in ids: bad += 1; print(f"{path}:{n} DUPLICATE row_id {rid} (first {ids[rid]})")
        else: ids[rid] = f"{path}:{n}"
print(f"rows={total} invalid={bad} valid={total-bad}")
sys.exit(1 if bad else 0)
