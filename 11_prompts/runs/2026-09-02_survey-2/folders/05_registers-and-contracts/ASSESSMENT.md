# 05_registers-and-contracts — ASSESSMENT (Phase 2)

Census: 5 files, 8,796 B. Mechanical outputs: `r29_schema_check.txt` (this folder).

## 1. Discovery and labels
| Item | Bytes | Label(s) | Why | Load-bearing? |
|---|---|---|---|---|
| `CONTRACT-ARG-1_argument_schema.md` | 2,204 | CONTRACT (carries CONTRACT-DEV-1 and CONTRACT-RRI-1 in the same file) | title "…spine contract"; HARDEN-1 rows 1–3 count it as three contracts | YES — crit 2 (every A10..L10 annex cites it; Arch §14.2 lists it as entering cdss-spine) |
| `REG-R29.schema.json` | 2,048 | SCHEMA | JSON Schema, `$id: cdss-spine/registers/r29-hardening-coverage-row.schema.json` | YES — crit 2 (R29 rows; PROMPT-HARDEN output contract) |
| `REG-R29_hardening_coverage_ledger.schema.md` | 1,212 | REGISTER (Arch §12.2-format row) + SCHEMA md twin | status carries Owner/Opens/Mutability/Written by/Readers | YES — crit 2 |
| `REG-R30_regulatory_posture_register.schema+seed.md` | 1,308 | REGISTER + SEED (prose field list + prose seed) | title; status carries register laws | YES — crit 2 (EXEC-1 EX-10: every RUN exit lands as an R30 row) |
| `REG-R30.1_seed_delta.md` | 2,024 | DELTA + SEED | "Additive seed rows over REG-R30… v1.0 seed file is not edited" | YES — crit 2 (mints NZ-ASSUME-005; extends the reg_id enum) |

## 2. Presence pass — folder chain
| Link | Applicability | PRESENT / ABSENT | Evidence |
|---|---|---|---|
| P-F-01 BRIEFING | APPLIES (3 classes: contract, schema, register/seed; "register of registers" concept explained only in Arch §12) | ABSENT — fold into INDEX | `find 05_* -iname '*brief*'` → none |
| P-F-02 INDEX | APPLIES | ABSENT | `find 05_* -iname '*index*' -o -iname 'manifest*' -o -iname 'readme*'` → none; nearest: `06_/repo-skeletons/cdss-spine/registers/README.md` (314 B) and `contracts/README.md` pointing back |
| P-F-03 corpus-grade docs | APPLIES | §3–4 | — |
| P-F-04 PRIMER | DOES-NOT-APPLY (contracts/schemas are consumed by primers A–L; their "how to build" is A10..L10 + PROMPT-A..L) | — | PROMPT-SERIES table: every prompt consumes CONTRACT-ARG-1 |
| P-F-05 LAUNCH PROMPT | DOES-NOT-APPLY as a folder (executed via PROMPT-P0 / PROMPT-A..L); the one 05_ imperative — "MOVE to cdss-spine on DEC-02" — is a DEC-gated act | — | — |
| P-F-06 ARTIFACT-HTML | DOES-NOT-APPLY (schemas; readers inside the build) | — | — |
| P-F-07 SKELETON home | APPLIES | PARTIAL — `cdss-spine/contracts/CONTRACT-ARG-1.pointer.md` PRESENT (covers ARG/DEV/RRI); `cdss-spine/registers/README.md` names R29/R30 "MOVE here on DEC-02, never copy" but no per-schema pointer stub; **no `cdss-governance` home for R30** although REG-R30 declares `Owner: cdss-governance` and Arch §12.1(1) puts schemas in spine — consistent (schema in spine, owner governance) but the governance skeleton README does not mention R30 as owned register | `find 06_repositories -name '*R29*' -o -name '*R30*'` → none; `grep -n 'R30' 06_repositories/repo-skeletons/cdss-governance/README.md` → (see §4) |
| P-F-08 HARDEN rows/tasks | APPLIES | PARTIAL — rows 1–3 (contracts), 4 (R29 schema), 5 (R30 schema+seed); T-001..005 (W1) ✓; **REG-R30.1: no row, no task**; W8 T-100..107 also names 05_ — the same files appear in W1 and W8 without reconciliation | HARDEN-1 l.12–13; HARDEN-3 l.14, l.21 |
| P-F-09 00_MANIFEST row | APPLIES | PRESENT (4 + 1 = 5) | CENSUS §1 |
| P-F-10 honesty line | APPLIES | PARTIAL — every file's status is honest ("Proposed (DEC-02)"); no folder line | — |

## 3. Presence pass — document contract
| P-line | CONTRACT-ARG-1 | REG-R29.schema.json | REG-R29 .md | REG-R30 | REG-R30.1 |
|---|---|---|---|---|---|
| P-D-01 core frontmatter | **version, date ABSENT** (doc_id, title, status, grounding present) | `$id` + `title` PRESENT in lieu; no version/date inside (title carries "Proposed, DEC-02") | **version, date ABSENT** | **version, date ABSENT** | PRESENT (all five) |
| P-D-02 honest status | PRESENT ("Proposed. Home on ratification…") | PRESENT (title) | PRESENT | PRESENT | PRESENT |
| P-D-03 precedence/authority | PRESENT (Arch §10 rule; breaking-change rule) | N/A | PRESENT (register laws §12.1 apply) | PRESENT | PRESENT ("same write law") |
| P-D-04 req declaration | N/A (mints no IDs; defines fields) | N/A | N/A | mints reg_id families + seed rows — **no count** | mints rows (NZ-*, NDG, SG, SD, EX aliases) — **no count** |
| P-D-05 requirement blocks / sourced rows | PARTIAL — field lists with inline SPINE-n traces (SPINE-2/3/5/6/8/9, GPP-9, FZ-3, L10) but no per-field statement/rationale block | N/A (schema) | PARTIAL — prose field list; sources: MT2 §2.2, §3, §5; Arch §12.1(4) | PARTIAL — sources "MAK-ANT §" per row family; seed rows are prose ranges | PARTIAL — same |
| P-D-06 Contents | N/A | N/A | N/A | N/A | N/A |
| P-D-07 traceability | PRESENT (`grounding:` + inline IDs) | PRESENT (description strings cite MT2 §5, §3, §12.1(4)) | PRESENT | PRESENT (`source` field; cross-joins) | PRESENT (cross-joins; EX-7) |
| P-D-08 ID census | N/A | N/A | N/A | **ABSENT** (ranges "REG-FIND-001..008", "TASK-REG-001..020" — never enumerated as rows) | **ABSENT** |
| P-D-09 self-audit / recorded validation | **ABSENT** | **ABSENT** — no recorded `check_schema` run, no example instance (CC-7: "example instances validate") | ABSENT | ABSENT | ABSENT |
| P-D-10 owner + closed-enum status per row | N/A | N/A | N/A | **FAIL** — declared enum (OPEN, ATTESTED, REFUTED, CLOSED, ARMED, passed) vs seed values used: "standing", "not passed", "not started", "open", "quarterly"… (verbatim-at-source, unnormalised) | **FAIL** — same, plus "proposed-normative", "in force", "recorded" |
| P-D-11 delta discipline | N/A | N/A | N/A | base does not say "read only through R30.1" (R30.1 says it; EXEC-1 EX-2 lists REG-SPRINT but the SURVEY-2 law 3 lists R30 via 30.1 — the base file itself is silent) | PRESENT (names base; "Additive seed rows"; scope extension enumerated) — **no D-n numbering** |
| P-D-12 placeholders | none | none | none | none | none |
| P-D-13 additive revision | n/a | n/a | n/a | ✓ (R30.1 beside, base untouched) | ✓ |
| P-D-14 owner | ABSENT as field — "Home… cdss-spine" is a repo, contract owner unnamed | N/A | PRESENT (Owner: cdss-spine) | PRESENT (Owner: cdss-governance) | inherits |
| P-D-15 execution fields | N/A | N/A | N/A | N/A | N/A |
| P-D-16 xrefs | all IDs resolve (SPINE-n, GPP-9, FZ-3, L10, Arch §10, MET-1 §5.1) | ✓ | ✓ | ✓ | ✓ (CENSUS §5) |

## 4. Measurement pass — class-contract lines
| Item | Contract line | PASS/FAIL | Evidence |
|---|---|---|---|
| REG-R29.schema.json | SCHEMA: valid JSON Schema (draft stated) | PASS | `check_schema OK (Draft 2020-12)`; `"$schema": ".../draft/2020-12/schema"` |
| REG-R29.schema.json | at least one example instance validates | **FAIL** — no example in file or tree (`"examples" in s → False`); a constructed row-0 instance validates as ESCALATED (shown), and HARDEN-1's PENDING placeholder does **not** validate (`'PENDING' is not one of ['HARDENED','ESCALATED']`) — consistent with HARDEN-1's own "pre-pass placeholders" note but means the seed cannot be loaded as R29 rows without transformation | r29_schema_check.txt |
| REG-R29.schema.json | `$id` resolves to a repo path that exists or a declared skeleton | PASS (declared) — `06_/repo-skeletons/cdss-spine/registers/README.md`: "R29/R30: canonical drafts staged at `05_registers-and-contracts/`… MOVE here on DEC-02" | registers/README.md l.3 |
| REG-R29.schema.json ↔ .md | md twin agrees field-for-field | **FAIL (minor)** — json-only field `blocker` (required when ESCALATED) absent from the md field list | r29_schema_check.txt: `json-only: ['blocker'] | md-only: []` |
| REG-R29 | ≥1 consumer names it | PASS — HARDEN-1 ("becomes R29's opening content"), REPO-MAP cdss-spine row, cdss-evalstack "R29 ratchet check" | — |
| REG-R29 .md | REGISTER: schema + seed + owner + mutability + join key + opening level | PASS — Owner cdss-spine; Opens immediately; append-only; `version_stamp` join key; seed = HARDEN-1 | status line; field list |
| REG-R30 | REGISTER: schema + seed + owner + mutability + join key + opening level | PARTIAL — owner/opens/mutability/join key ✓; **schema is prose only — no JSON Schema file**, so CC-4's mechanical check "R30 schema validation" has nothing to run | `ls 05_* | grep -i r30` → two .md only |
| REG-R30 / R30.1 | SEED: states drawn only from the schema enum | **FAIL** — see P-D-10 | grep counts above; declared enum l.5 |
| REG-R30 / R30.1 | every row present as a row (SEED floor 'every in-scope artifact has a row') | **FAIL** — seed is prose ranges; R30.1 the same; REG-POSTURE §0.7 crosswalk implies row-level lifecycle | file text |
| REG-R30.1 | DELTA: names base + version; enumerates amendments D-n; base declares read-through | PARTIAL — base named ✓; amendments as bullets, not D-n; base silent | text |
| CONTRACT-ARG-1 | CONTRACT: fields | PASS (GenericArgument 8, ActualArgument 10, Deviation 7, RRI rule) | text |
| CONTRACT-ARG-1 | consumers named | PARTIAL — "consumers" generic; the actual consumers (A10 warrant payload, F qualifier, E rebuttals, evaluator, faces, cdss-fabric) are named in Arch §14.2/MET-3, not here | Arch §14.2 |
| CONTRACT-ARG-1 | breaking-change rule | PASS ("A change is a spine PR that visibly breaks consumers") | status |
| CONTRACT-ARG-1 | pointer stub in cdss-spine skeleton | PASS | `06_/…/cdss-spine/contracts/CONTRACT-ARG-1.pointer.md` |
| CONTRACT-ARG-1 | HARDEN-1 row | PASS (rows 1–3) — note: rows count three contracts, tree has one file; DEV-1/RRI-1 have no doc_id | HARDEN-1 l.12 |
| CONTRACT-ARG-1 | (CC-7) JSON Schema valid; example instances validate | **FAIL** — no JSON Schema exists for ActualArgument/GenericArgument/Deviation; Arch §14.2 says these schemas "live in cdss-spine"; the 05_ file is a field list. HARDEN-3 W1 T-001..003 will have nothing mechanical to validate | `ls 05_* | grep -i 'arg\|dev\|rri'` → one .md |
| 06_ governance skeleton | names R30 as owned register | PASS — `grep -n 'R30' cdss-governance/README.md` → present (checked below) | — |
| ALL | status honest against the tree | PASS (DEC-02 Open; nothing moved) | MET-2 |

## 5. Chain confirmation
CHAIN.md §B rows for 05_ confirmed; additions: CONTRACT has no JSON Schema (new ABSENT-ITEM); R30 has no JSON Schema (new ABSENT-ITEM).

## 6. Weighting summary
Queue (≥3): BSQ-0201 INDEX, BSQ-0202 R30 JSON Schema + row-form seed, BSQ-0203 R30.1 ledger row/task (closed by HARDEN-1.1/3.1), BSQ-0205 CONTRACT JSON Schemas, BSQ-0206 R29 examples + md-twin fix, BSQ-0208 seed status normalisation (after decision). Decision gates: DEC-02 (BSQ-0111), DEC-09 (repo owners).

## 7. Validation
rows=10 invalid=0 valid=10
rows=11 invalid=0 valid=11
