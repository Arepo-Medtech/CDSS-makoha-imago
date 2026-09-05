#!/usr/bin/env python3
"""Dead-path and §-anchor check over the corpus folders (00_–11_ top level, excluding run directories).
Classifies unresolved paths: external (agent-skills pack, validate_build_plan.py, observer doc), glob, future output, DEAD.
Exits 1 if any DEAD in-repo path or unresolved anchor is found in a file changed by the PR (pass changed file list via argv), else 0."""
import os, re, sys, subprocess
changed = set(sys.argv[1:])
DOCS = {"Arch": "02_cdss-stack-augmented/architecture_and_integration.md", "MT2": "04_hardening/MAJOR_TASK_2_anti-laziness-hardening-directive.md", "MET-1": "01_north-star-and-transformation/MET-1_metamorphosis_plan_v1.0.md", "REG-POSTURE": "10_regulatory-execution/REG-POSTURE_v1.2.md", "Primer 0": "02_cdss-stack-augmented/primer_0_ecosystem_explainer.md", "HARDEN-2": "04_hardening/HARDEN-2_hardening_spec.md", "REG-NZ": "10_regulatory-execution/REG-NZ_v1.1.md", "EXEC-1": "10_regulatory-execution/EXEC-1_execution_directive.md", "MAK-GOV": "10_regulatory-execution/MAK-GOV_addendum-g_v0.9.md", "OPS-1": "07_deployment-and-operations/OPS-1_operating_procedures.md"}
heads = {}
for k, p in DOCS.items():
    hs = set()
    for ln in open(p, encoding="utf-8", errors="replace"):
        m = re.match(r"^#{1,6}\s*(?:§)?([0-9]+(?:\.[0-9]+)?|[A-Z](?:\.[0-9]+)?)\b", ln)
        if m: hs.add(m.group(1))
    heads[k] = hs
tracked = set(subprocess.check_output(["git", "ls-files"]).decode().split("\n"))
EXTERNAL = (".venv", "node_modules", "validate_regulatory_sensing.py", "coder_contract.md", "pharm-check.schema.json", "x8stats.py", "references/", "docs/agents.md", "validate_build_plan.py", "observer_adjudication.md", "definition-of-done.md", "testing-patterns.md", "security-checklist.md", "performance-checklist.md", "accessibility-checklist.md", "observability-checklist.md", "orchestration-patterns.md")
PATHRX = re.compile(r"`((?:\d\d_[A-Za-z0-9_\-]+/)[^`\s]*)`|`([^`\s]+?\.(?:md|json|jsonl|yaml|yml|py|html|mermaid|txt|mjs))`")
ANCH = re.compile(r"(Arch|MT2|MET-1|REG-POSTURE|Primer 0|HARDEN-2|REG-NZ|EXEC-1|MAK-GOV|OPS-1)\s*§\s*([0-9]+(?:\.[0-9]+)?|[A-Z](?:\.[0-9]+)?)")
dead = []; ext = glob = fut = shorthand = 0; anchors_bad = []
RETAINED_PRE_DEF002 = ("01_north-star-and-transformation/MET-1_metamorphosis_plan_v1.0.md",)
for f in sorted(tracked):
    if not f.endswith((".md", ".yaml", ".yml", ".mermaid", ".html", ".json")) or f.startswith(("11_prompts/runs/", ".github/", ".impeccable/", ".claude/")) or not f[:1].isdigit(): continue
    for n, ln in enumerate(open(f, encoding="utf-8", errors="replace"), 1):
        for m in PATHRX.finditer(ln):
            c = (m.group(1) or m.group(2)).split("#")[0].rstrip("/")
            if c in tracked or os.path.exists(c) or os.path.exists(os.path.join(os.path.dirname(f), c)): continue
            if any(k in c for k in EXTERNAL): ext += 1
            elif "**" in c or "{{" in c or "<" in c or "vN" in c or c.startswith(".") or c in ("04_butterfly-primers",): glob += 1   # templates / scratch paths in retained prompts
            elif "antennae-corpus_v1.1" in c or f.startswith("11_prompts/"): fut += 1   # prompts declare their future outputs
            elif re.fullmatch(r"\d\d_[a-z\-]+/[A-Z][A-Z0-9\-/]*", c): shorthand += 1   # doc-id shorthand like 04_hardening/HARDEN-2
            elif os.path.basename(c) in {os.path.basename(t) for t in tracked}: continue  # basename-resolvable
            else: dead.append((f, n, c))
        for m in ANCH.finditer(re.sub(r"`[^`]*`", "", ln)):   # quoted anchors (inside backticks) are citations of defects, not references
            if f in RETAINED_PRE_DEF002 or f.startswith("11_prompts/"): continue
            if m.group(2) not in heads[m.group(1)] and not (f.endswith(("register_topology_v2.mermaid", "cdss_diagrams_v2.html", "09_diagrams/INDEX.md")) and m.group(2) == "7.4"):
                anchors_bad.append((f, n, f"{m.group(1)} §{m.group(2)}"))
print(f"## Reference check\n\n- dead in-repo paths: {len(dead)}; unresolved anchors: {len(anchors_bad)} (the two carried v2 `MT2 §7.4` defects excluded — DEF-003); external refs: {ext}; globs/placeholders: {glob}; prompt-declared future outputs: {fut}; doc-id shorthand: {shorthand}")
for f, n, c in dead: print(f"  - DEAD `{f}:{n}` → `{c}`")
for f, n, c in anchors_bad: print(f"  - ANCHOR `{f}:{n}` → {c}")
fail = [x for x in dead + anchors_bad if x[0] in changed]   # gate only on files this PR changed; the baseline is report-only
sys.exit(1 if fail else 0)
