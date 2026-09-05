#!/usr/bin/env python3
"""Frontmatter schema census over authored markdown. Retained originals (02_, MT2) and skeleton stubs (06_) are
reported by class, not as findings. Exits 0 always (report-only); writes a markdown summary to stdout."""
import subprocess, re, collections
files = [f for f in subprocess.check_output(["git", "ls-files"]).decode().split("\n") if f.endswith(".md") and not f.startswith(("11_prompts/runs/", ".github/", ".impeccable/", ".claude/"))]
core = ["doc_id", "title", "version", "date", "status"]
nofm = collections.defaultdict(list); gaps = collections.Counter(); ids = collections.Counter(); minted_undeclared = []
for f in files:
    t = open(f, encoding="utf-8", errors="replace").read()
    if not t.startswith("---"):
        cls = "retained-original" if f.startswith("02_") or "MAJOR_TASK_2" in f else "skeleton-stub" if f.startswith("06_repositories/repo-skeletons") else "companion-or-omission"
        nofm[cls].append(f); continue
    head = t.split("---", 2)[1]
    for k in core:
        if not re.search(rf"^{k}:", head, re.M) and not (k == "date" and re.search(r"^date_issued:", head, re.M)): gaps[(f, k)] += 1
    m = re.search(r"^doc_id:\s*(.+)$", head, re.M)
    if m: ids[m.group(1).strip().strip('"')] += 1
    mints = set(re.findall(r"(?m)^### ([A-Z][A-Z0-9-]{1,12})-\d+ \((?:MUST|SHOULD|MAY)\)", t))
    if mints and not re.search(r"^req_prefix(es)?:", head, re.M): minted_undeclared.append((f, sorted(mints)))
print(f"## Frontmatter census\n\n- markdown files in scope: {len(files)}; with frontmatter: {len(files)-sum(len(v) for v in nofm.values())}")
for cls, fs in nofm.items(): print(f"- without frontmatter — {cls}: {len(fs)}" + ("" if cls != "companion-or-omission" else " → " + ", ".join(f"`{x}`" for x in fs)))
print(f"- core-field gaps (file, field): {len(gaps)}" + (" → " + "; ".join(f"`{f}`:{k}" for (f, k) in list(gaps)[:20]) if gaps else ""))
dups = {k: v for k, v in ids.items() if v > 1}
print(f"- doc_id repeats: {dups or 'none'} (superseded versions sharing an id need a supersedes: field)")
print(f"- files minting requirement blocks without req_prefix: {len(minted_undeclared)}" + (" → " + "; ".join(f"`{f}` {m}" for f, m in minted_undeclared) if minted_undeclared else ""))
