#!/usr/bin/env python3
"""Directory-depth census: flags any tracked file nested deeper than four directory levels (architect threshold). Exit 1 if any."""
import subprocess, collections, sys
files = [f for f in subprocess.check_output(["git", "ls-files"]).decode().split("\n") if f and not f.startswith((".github/", ".impeccable/", ".claude/", "11_prompts/runs/"))]
hist = collections.Counter(f.count("/") for f in files); deep = [f for f in files if f.count("/") > 4]
print(f"## Depth census\n\n- files: {len(files)}; depth histogram: {dict(sorted(hist.items()))}; deeper than four levels: {len(deep)}")
for f in deep: print(f"  - DEPTH `{f}`")
sys.exit(1 if deep else 0)
