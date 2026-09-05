#!/usr/bin/env bash
# Design Ecosystem audit — mechanical layer. Run from repo root. $1 = base ref (default origin/main). Writes ${GITHUB_STEP_SUMMARY:-/dev/stdout}.
set -u
BASE="${1:-origin/main}"; OUT="${GITHUB_STEP_SUMMARY:-/dev/stdout}"; rc=0
CHANGED=$(git diff --name-only "$BASE"...HEAD 2>/dev/null | tr '\n' ' ')
{ echo "# Design Ecosystem Agentic Audit — mechanical layer"; echo; echo "Base: \`$BASE\` · changed paths: $(echo $CHANGED | wc -w | tr -d ' ')"; echo; } >> "$OUT"
run() { local name="$1"; shift; local o; o="$("$@" 2>&1)"; local r=$?; { echo "$o"; echo; echo "→ **$name: $([ $r -eq 0 ] && echo PASS || echo FAIL)**"; echo; } >> "$OUT"; [ $r -ne 0 ] && rc=1; }
run "append-only"   python3 .github/audit/append_only.py "$BASE"
run "frontmatter"   python3 .github/audit/frontmatter_census.py
run "references"    python3 .github/audit/refcheck.py $CHANGED
run "depth"         python3 .github/audit/depth.py
run "schemas"       python3 .github/audit/schemas.py
if command -v node >/dev/null && [ -d .github/audit/mermaid/node_modules ]; then
  o="$(cd .github/audit/mermaid && node parse.mjs ../../../09_diagrams 2>/dev/null)"; f=$(echo "$o" | grep -c '"FAIL"')
  { echo "## Mermaid parse (09_diagrams)"; echo; echo '```'; echo "$o" | python3 -c "import json,sys; d=json.load(sys.stdin); print(d['tool']); [print(f\"  {r['file']:40s} {r['kind']:18s} {r['result']}\") for r in d['results']]"; echo '```'; echo; echo "→ **mermaid: $([ "$f" -eq 0 ] && echo PASS || echo FAIL)**"; echo; } >> "$OUT"; [ "$f" -ne 0 ] && rc=1
else { echo "## Mermaid parse"; echo; echo "TOOL-UNAVAILABLE (node or node_modules missing)"; echo; } >> "$OUT"; fi
exit $rc
