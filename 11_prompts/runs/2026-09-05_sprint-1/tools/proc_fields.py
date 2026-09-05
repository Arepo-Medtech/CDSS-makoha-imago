#!/usr/bin/env python3
"""CC-5 field-presence check over OPS-1.1: every step line `{...}` must carry timeout, retry, idempotent, on_fail."""
import re,sys
t=open("07_deployment-and-operations/OPS-1.1_procedures_cc5_delta.md",encoding="utf-8").read()
steps=re.findall(r"\{[^{}]*\}",t)
steps=[s for s in steps if 'timeout' in s or 'retry' in s or 'idempotent' in s or 'on_fail' in s]
bad=[s for s in steps if not all(k in s for k in ("timeout","retry","idempotent","on_fail"))]
procs=re.findall(r"^### (PROC-\d\d)",t,re.M)
print(f"PROC ids: {len(procs)} ({', '.join(procs)})")
print(f"step field-blocks: {len(steps)}; lacking a field: {len(bad)}")
for b in bad: print("  MISSING:",b[:120])
cites=[p for p in procs if re.search(re.escape(p)+r"[^\n]*\((OPS-1 §|`TASK-REG-)",t)]
print(f"PROC citing OPS-1 § or TASK-REG in heading: {len(cites)}/{len(procs)}")
sys.exit(1 if bad else 0)
