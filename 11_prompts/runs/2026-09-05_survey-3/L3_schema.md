# L3_schema — Layer 3 census (Q-D-14) — `tools/schema_dupes.py`

Assets scanned: **41** (4 JSON Schemas, `MANIFEST.yaml` ×19, `pipeline.yml` ×18); enums found: 16; enums duplicated across files: **0**.

## Pinned strings repeated in ≥3 assets

| files | string | reading |
|---|---|---|
| 19 | `skeleton-proposed` | status value ×19 — one source would be REPO-MAP or a `06_/SKELETON.schema.yaml`; today 19 literal copies |
| 19 | `cdss-spine: "[PIN NEEDS DEFINITION]"` | pipeline-stub prose repeated per tree — the stubs themselves say every repo imports pipeline definitions from cdss-evalstack (Arch §11.1) |
| 19 | `[joins the integration lockfile pin-set — register law §12.1(4)]` | prose in a YAML value ×19 — a comment or a reference to Arch §12.1(4) would do |
| 17 | `consume cdss-spine@[PIN]; fail on contract drift (spine PR breaks consum` | pipeline-stub prose repeated per tree — the stubs themselves say every repo imports pipeline definitions from cdss-evalstack (Arch §11.1) |
| 15 | `admissibility validator (cdss-governance shared CI action) — no card, no` | pipeline-stub prose repeated per tree — the stubs themselves say every repo imports pipeline definitions from cdss-evalstack (Arch §11.1) |
| 15 | `row-completeness check on instruction-bearing artifacts (ACTIVATES on DE` | pipeline-stub prose repeated per tree — the stubs themselves say every repo imports pipeline definitions from cdss-evalstack (Arch §11.1) |
| 4 | `required` | JSON Schema keyword (not a value) |
| 4 | `properties` | JSON Schema keyword (not a value) |
| 4 | `minLength` | JSON Schema keyword (not a value) |
| 4 | `description` | JSON Schema keyword (not a value) |
| 4 | `[per README — nothing emitted yet]` | stub prose ×4 — same family |
| 4 | `[per annex bindings]` | stub prose ×4 — same family |
| 3 | `$comment` | JSON Schema keyword (not a value) |
| 3 | `additionalProperties` | JSON Schema keyword (not a value) |

Reading: the 19 `MANIFEST.yaml` and 18 `pipeline.yml` stubs are byte-similar templates; the repeats are the template, not values that bypass an alias architecture. One SCHEMA-HARDCODE row at folder level (06_) for `status: skeleton-proposed` and `[PIN NEEDS DEFINITION]` ×19 (a change = 19 co-ordinated edits; the design says one pin-set — Arch §12.1(4)); weight 2 because stubs are replaced at instantiation (INDEX-06 §4). The four JSON Schemas share no enum → PRESENT-IMPECCABLE for 05_ on Q-D-14.

