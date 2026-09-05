#!/usr/bin/env python3
"""Append-only check for a pull request: every file that exists on the base ref must be byte-identical on the head,
except 00_MANIFEST.md, which may only GROW by appending (base content is a byte prefix of the head content).
Usage: append_only.py <base_ref>   (run from repo root; exits 1 on violation)."""
import subprocess, sys, hashlib
base = sys.argv[1] if len(sys.argv) > 1 else "origin/main"
def sh(c): return subprocess.run(c, shell=True, capture_output=True, text=True).stdout
changed = [l for l in sh(f"git diff --name-status {base}...HEAD").split("\n") if l.strip()]
viol = []; ok = 0
for l in changed:
    status, *paths = l.split("\t"); path = paths[-1]
    if status.startswith("A"): ok += 1; continue
    if status.startswith(("D", "R")): viol.append(f"{status} {path}: pre-existing file removed or renamed"); continue
    if not path.startswith(("00_", "01_", "02_", "03_", "04_", "05_", "06_", "07_", "08_", "09_", "10_", "11_")): ok += 1; continue  # repo tooling may change
    if path == "00_MANIFEST.md":
        b = subprocess.run(["git", "show", f"{base}:{path}"], capture_output=True).stdout; h = open(path, "rb").read()
        if h.startswith(b): ok += 1; print(f"00_MANIFEST.md: appended {len(h)-len(b)} bytes; prefix preserved (sha256 {hashlib.sha256(b).hexdigest()[:12]})")
        else: viol.append("00_MANIFEST.md: base content is NOT a prefix of the head content — edited above the line")
        continue
    viol.append(f"{status} {path}: pre-existing corpus file modified (append-only law; use a delta/companion/successor)")
print(f"append-only: {len(changed)} changed paths, {ok} permitted, {len(viol)} violations")
for v in viol: print("  VIOLATION:", v)
sys.exit(1 if viol else 0)
