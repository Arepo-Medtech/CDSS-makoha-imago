#!/usr/bin/env bash
# Idempotent bootstrap for the Mākoha Imago design-ecosystem audit tooling.
# Mirrors .github/workflows/design-ecosystem-audit.yml so .github/audit/run_all.sh
# (append-only · frontmatter · references · depth · schemas · mermaid) runs locally.
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

# Python deps for the frontmatter, reference, depth and JSON Schema audits
# (matches the CI "pip install jsonschema pyyaml" step).
python3 -m pip install --quiet --user jsonschema pyyaml

# Node deps for the mermaid parse audit over 09_diagrams
# (matches the CI "npm install" step in .github/audit/mermaid).
cd "${repo_root}/.github/audit/mermaid"
npm install --silent --no-audit --no-fund
