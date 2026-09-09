# RUN-REPORT — sprint-mak66 (2026-09-09): TASK-HDC-002 face-acts contract and design spec

Run: `11_prompts/runs/2026-09-09_sprint-mak66/` · Branch: `claude/MAK-66/face-acts-contract-act-1`
(from `main` 99033be) · Executor: Claude agent (MAK-66) · Mandate: MAK-66 / TASK-HDC-002
"Six act writers with fail-closed sign-off (CONTRACT-ACT-1)" · Status: **built on branch;
PR raised; merge awaits review.**

## 0. Append-only proof (law 1) — read this first

Pasted at seal from `CHECKSUMS_BEFORE.txt` / `CHECKSUMS_AFTER.txt`. The only pre-existing
file whose hash changed is `00_MANIFEST.md` (appended, A-012). No other file under `00_`–`11_`
was modified. Every retained file under `00_`–`11_` is byte-identical to `main` at branch point
`99033be`. Five new files were added outside the run directory; two bookend files in the run
directory.

Changed (pre-existing): `./00_MANIFEST.md` (appended only — A-012 section)
New (outside run dir): `./05_registers-and-contracts/CONTRACT-ACT-1.examples.jsonl`
                       `./05_registers-and-contracts/CONTRACT-ACT-1.schema.json`
                       `./05_registers-and-contracts/CONTRACT-ACT-1_act_schema.md`
                       `./06_repositories/repo-skeletons/cdss-ui-clinician/face/FACE-ACTS.md`

## 1. Coverage

| Measure | Value |
|---|---|
| New files outside run directories | 5 |
| Files modified outside 00_–11_ | 0 |
| Manifest | appended only (A-012) |
| Source task | TASK-HDC-002 (MAK-66) |
| Primary source | `03_makoha-butterfly-corpus/butterfly-primers/primer_HDC_clinician_face.md` |
| Reconciliation read-through | `docs/CLINICIAN_REQUIREMENT_RECONCILIATION_2026-09-08.md` (commit `a8db2b0`) |
| DoD properties targeted | HDC8 properties 6, 8, 10 |
| RECON addressed | RECON-HDC-007 (CONTRACT-ACT-1 path taken) |
| New gap IDs minted | GAP-ACT-001..004 |
| Schema meta-validation | PASS (jsonschema Draft202012Validator.check_schema) |
| Example validation (annotation-stripped) | 14/14 PASS |

## 2. Deliverables

| File | Bytes (sha256) | Contents | Disposition |
|---|---|---|---|
| `05_registers-and-contracts/CONTRACT-ACT-1_act_schema.md` | da899cf7… | 12 ACT-n MUST requirements; test plan; HDC8 properties 6/8/10; gap register; self-audit | Added — Proposed |
| `05_registers-and-contracts/CONTRACT-ACT-1.schema.json` | 9f2907… | JSON Schema 2020-12 discriminated union; six act kind variants; 7 supporting $defs | Added — Proposed |
| `05_registers-and-contracts/CONTRACT-ACT-1.examples.jsonl` | 014132… | 7 valid examples; 7 invalid examples; fault-injection scenario comment; 14/14 PASS | Added — Proposed |
| `06_repositories/repo-skeletons/cdss-ui-clinician/face/FACE-ACTS.md` | e5332377… | Face-acts component spec; HALT triggers; HDC8 property table; observability; open items | Added — Proposed (skeleton) |

## 3. HDC8 property test results

| Property | Statement (abridged) | Result |
|---|---|---|
| 6 | No release-class action without SignoffAct, any elapsed time or focus event | EXECUTABLE against stub — SignoffAct is the only schema path to a release; fault-injection scenario documented in CONTRACT-ACT-1.examples.jsonl §3 |
| 8 | One attributed pinned fabric entry per act; replay from projection_context | Stub: EXECUTABLE (7 valid examples each carry fabric_entry + attribution; signoff carries projection_context; 14/14 schema PASS). Replay round-trip: UNVERIFIED — requires live SPINE-9 projection (RECON-HDC-001/002; GAP-ACT-002) |
| 10 | No unanimous rendering with recorded dissent | EXECUTABLE against stub — conflict_navigation-valid-with-stances carries two AuthorStance records with distinct positions; PASS |

## 4. Test plan results

| Test | Outcome |
|---|---|
| One-act fixtures (all six kinds) | PASS — each kind has a valid example; all 7 validate against schema (annotation-stripped) |
| Both-acts fixture (deviation + gap_report, one encounter_id ENC-EXAMPLE-001) | PASS — two entries share encounter_id; no schema constraint blocks coexistence |
| Fault-injection (timeout/inactivity/focus loss) | EXECUTABLE — schema structural argument: no SignoffAct = no release pathway; scenario documented in examples §3 |
| Fault-injection — missing actor on signoff | PASS — signoff-missing-actor validates as INVALID |
| Wrong authority class on signoff | PASS — signoff-wrong-authority validates as INVALID (allOf clinical-release rule) |
| Missing projection_context on signoff | PASS — signoff-missing-projection-context validates as INVALID |
| Missing locus on gap report | PASS — gap_report-missing-locus validates as INVALID |
| arg_id without arg_version on gap report | PASS — gap_report-arg_id-without-arg_version validates as INVALID (if/then rule) |
| Missing basis on fit_judgment | PASS — fit_judgment-missing-basis validates as INVALID |
| Empty verbatim_text on boundary_work | PASS — boundary_work-empty-verbatim validates as INVALID (minLength 1) |
| Friction audit (one interaction per act) | UNVERIFIED — requires UI fixture (TASK-HDC-001 dependency; GAP-ACT-004) |
| Replay round-trip | UNVERIFIED — requires RECON-HDC-001/002 (GAP-ACT-002) |
| Per-author stances (property 10) | PASS — two-author ConflictNavigationAct example with distinct positions validates |

No UNVERIFIED item is claimed as passed.

## 5. Gaps and open items

| ID | Description |
|---|---|
| GAP-ACT-001 | `severity_tier` vocabulary [NEEDS DEFINITION — DEC-02]; pattern `^[A-Z0-9][A-Z0-9-]*$` only |
| GAP-ACT-002 | Replay round-trip UNVERIFIED — RECON-HDC-001/002 |
| GAP-ACT-003 | FabricEntryRef stub — full SPINE-4 chain protocol owned by cdss-fabric (GAP-HDC-002) |
| GAP-ACT-004 | Friction audit UNVERIFIED — UI fixture required (TASK-HDC-001) |
| RECON-HDC-007 | CONTRACT-ACT-1 ratification into cdss-spine pending |

## 6. Reference check (new files in this sprint)

- Dead in-repo paths: **0**
- Unresolved anchors: **0**
- Cited corpus IDs verified by read-through at ALPHA `99033be`:
  HA-1..6 ✓ · SPINE-4/5/8 ✓ · MS-2/3/7 ✓ · PF-8 ✓ · RG-2 ✓ · FC-2 ✓
  REG-KEEP-003 ✓ · HT-1/3 ✓ · MAK-LBP CV-1 ✓ · MA-6 ✓ · OM-5 ✓
  DEC-02 ✓ · DEC-09 ✓ · GAP-HDC-001/002/003 ✓ · RECON-HDC-001/002/007 ✓
  OPS-1 ✓ · HDC9 §7 ✓ — **PASS**
- No clinical number, fragment, or case content authored — **PASS**
- No R29 row written — **PASS**
- No corpus file (03_) written — **PASS**
- Schema meta-validation (Draft202012Validator.check_schema): **PASS**
- Example validation (14 examples, annotation keys stripped): **14/14 PASS**
- JSON parse of schema and examples: **PASS**

## 7. Reconciliation corrections applied

From `CLINICIAN_REQUIREMENT_RECONCILIATION_2026-09-08.md` §Contracts (commit `a8db2b0`):

1. **Discriminated union** — schema is oneOf by `kind`; GapReportAct requires no
   ActualArgument (HA-3 "available from any screen"). Contract-DEV-1's monolithic shape
   not reused as the six-act envelope.
2. **Actor authority-class** — `recording` vs `clinical-release` distinguished; signoff
   enforces `clinical-release` via allOf constraint; schema encodes shape, endpoint
   enforces authentication.
3. **Idempotency key** — `idempotency_key` is caller-supplied at render time; prevents
   retry duplication without collapsing distinct submissions; entry hash not used alone.
4. **Projection context for replay** — `projection_context` on SignoffAct records
   projection, renderer, identity sheet, codebook, and layout versions; argument version
   pin alone is not claimed as sufficient replay evidence.
