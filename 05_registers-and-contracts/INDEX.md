---
doc_id: INDEX-05
title: "INDEX-05 — 05_registers-and-contracts: briefing, file table with carried doc_ids, reading rule, honesty line, recorded validation"
version: "1.0"
date: "2026-09-05"
status: "Added (sprint-1); indexes only; nothing ratified (DEC-02 Open); no schema moved (DEC-09 Open); R30 now has a JSON Schema and a row-form seed (sprint-1) — Proposed, not ratified"
folder: "05_registers-and-contracts/"
produced_by: "sprint-1 (survey-2 Build-Spec Queue) — generated tables from disk by 11_prompts/runs/2026-09-05_sprint-1/tools/render_index.py; briefing text authored; edits nothing"
---

# INDEX-05 — 05_registers-and-contracts

## §1 Briefing — what these documents are

A **CONTRACT** is a shared interface specification that lives once, versioned, in the spine and is consumed as a pinned dependency; a change is a spine PR that visibly breaks consumers (Arch §10). A **SCHEMA** is the machine-checkable form of a contract or of a register row (JSON Schema draft 2020-12 here; `jsonschema` validates instances). A **REGISTER** is a governed table of what currently holds (versioned) or what happened (append-only), with one owning repo, a declared mutability, an opening level and the universal join key `version_stamp` — the six register laws of Arch §12.1. A **SEED** is a register's proposed opening content; a **DELTA** adds to a base file without editing it (MET-1.1 pattern). The **register of registers** idea (Arch §12): R1–R28 are the ratified registers; R29 (hardening coverage) and R30 (regulatory posture) are Proposed here and enter the RoR on DEC-02; every register's schema lives in cdss-spine (§12.1(1)), and a scheduled negative audit proves nothing exists outside its register (§12.1(5)). Form exemplar: `02_cdss-stack-augmented/primers_briefing.md`.

## §2 File table

| path | class | doc_id | version | date | status (quoted) | bytes | disposition | HARDEN-1/1.1 row | HARDEN-3.1 task | 00_MANIFEST row | doc_id(s) carried | skeleton home on ratification | DEC gate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `05_registers-and-contracts/CONTRACT-ARG-1.examples.jsonl` | CC-7 | — | — | — | {"_example": "GA-valid", "_expect": "VALID", "object_type": "GenericArgument", "ga_id": "GA-EXAMPLE-001", "ga_version": "1.0.0", "warrant_type": "guideline-rule | 4101 | Added (sprint-1) — Proposed | 99 | T-141 | §1 row (4) + §8 A-002 (+1 R30.1) + §9 A-003 (+1 R30.2) + A-004 | examples for ARG-1 | cdss-spine/contracts/ (pointer stub `CONTRACT-ARG-1.pointer.md` covers ARG/DEV/RRI) | DEC-02 (ratify R29/R30) + DEC-09 (repo owners) — MOVE, never copy |
| `05_registers-and-contracts/CONTRACT-ARG-1.schema.json` | CC-7 | cdss-spine/contracts/contract-arg-1.schema.json | — | — | CONTRACT-ARG-1 — GenericArgument / ActualArgument (Proposed, DEC-02; staged draft, MOVES to cdss-spine on DEC-02 + DEC-09) | 7405 | Added (sprint-1) — Proposed | 100 | T-140 | §1 row (4) + §8 A-002 (+1 R30.1) + §9 A-003 (+1 R30.2) + A-004 | CONTRACT-ARG-1 (JSON Schema) | cdss-spine/contracts/ (pointer stub `CONTRACT-ARG-1.pointer.md` covers ARG/DEV/RRI) | DEC-02 (ratify R29/R30) + DEC-09 (repo owners) — MOVE, never copy |
| `05_registers-and-contracts/CONTRACT-ARG-1_argument_schema.md` | CC-7 | CONTRACT-ARG-1 | — | — | Proposed. Home on ratification: cdss-spine (contracts live here once, versioned; never duplicated — Arch §10). A change is a spine PR that visibly breaks consumers. | 2204 | Proposed (DEC-02) | 1,2,3 | T-001 | §1 row (4) + §8 A-002 (+1 R30.1) + §9 A-003 (+1 R30.2) + A-004 | CONTRACT-ARG-1 (+DEV-1, RRI-1 paragraphs) | cdss-spine/contracts/ (pointer stub `CONTRACT-ARG-1.pointer.md` covers ARG/DEV/RRI) | DEC-02 (ratify R29/R30) + DEC-09 (repo owners) — MOVE, never copy |
| `05_registers-and-contracts/CONTRACT-DEV-1.examples.jsonl` | CC-7 | — | — | — | {"_example": "DEV-valid", "_expect": "VALID", "object_type": "Deviation", "dev_id": "DEV-EXAMPLE-001", "arg_id": "AA-EXAMPLE-001", "reason_taxonomy_code": "EXAM | 674 | Added (sprint-1) — Proposed | 101 | T-142 | §1 row (4) + §8 A-002 (+1 R30.1) + §9 A-003 (+1 R30.2) + A-004 | examples for DEV-1 | cdss-spine/contracts/ (pointer stub `CONTRACT-ARG-1.pointer.md` covers ARG/DEV/RRI) | DEC-02 (ratify R29/R30) + DEC-09 (repo owners) — MOVE, never copy |
| `05_registers-and-contracts/CONTRACT-DEV-1.schema.json` | CC-7 | cdss-spine/contracts/contract-dev-1.schema.json | — | — | CONTRACT-DEV-1 — Deviation object (Proposed, DEC-02; staged draft, MOVES to cdss-spine on DEC-02 + DEC-09) | 1953 | Added (sprint-1) — Proposed | 102 | T-002 | §1 row (4) + §8 A-002 (+1 R30.1) + §9 A-003 (+1 R30.2) + A-004 | CONTRACT-DEV-1 (JSON Schema) | cdss-spine/contracts/ (pointer stub `CONTRACT-ARG-1.pointer.md` covers ARG/DEV/RRI) | DEC-02 (ratify R29/R30) + DEC-09 (repo owners) — MOVE, never copy |
| `05_registers-and-contracts/CONTRACT-RRI-1_render-invariance_test-spec.md` | CC-7 | CONTRACT-RRI-1-TEST | 1.0 | 2026-09-05 | Proposed (DEC-02). Companion to CONTRACT-ARG-1_argument_schema.md (RRI-1 paragraph, unedited). Specifies the test; implements nothing. Home on ratification: cdss-spine (contracts) with the test itself in cdss-fabric's su… | 5657 | Added (sprint-1) — Proposed | 103 | T-003 | §1 row (4) + §8 A-002 (+1 R30.1) + §9 A-003 (+1 R30.2) + A-004 | CONTRACT-RRI-1-TEST (RRI-1..4) | cdss-spine/contracts/ (pointer stub `CONTRACT-ARG-1.pointer.md` covers ARG/DEV/RRI) | DEC-02 (ratify R29/R30) + DEC-09 (repo owners) — MOVE, never copy |
| `05_registers-and-contracts/INDEX.md` | CC-8 | INDEX-05 | 1.0 | 2026-09-05 | Added (sprint-1); indexes only; nothing ratified (DEC-02 Open); no schema moved (DEC-09 Open); R30 now has a JSON Schema and a row-form seed (sprint-1) — Proposed, not ratified | 16390 | Added (sprint-1) | 104 | T-712 | §1 row (4) + §8 A-002 (+1 R30.1) + §9 A-003 (+1 R30.2) + A-004 | INDEX-05 | — (index) | — |
| `05_registers-and-contracts/REG-R29.1_schema_twin_delta.md` | CC-2 | REG-R29.1 | 1.1-delta | 2026-09-05 | Added. Additive delta over REG-R29_hardening_coverage_ledger.schema.md; neither the md base nor REG-R29.schema.json is edited. Read REG-R29 (md) through this file. Nothing here is an R29 row (law 6): the examples file ca… | 2645 | Added (sprint-1) — Proposed | 105 | T-145 | §1 row (4) + §8 A-002 (+1 R30.1) + §9 A-003 (+1 R30.2) + A-004 | REG-R29.1 | cdss-spine/registers/ (README: "MOVE here on DEC-02, never copy"); R30 owner cdss-governance | DEC-02 (ratify R29/R30) + DEC-09 (repo owners) — MOVE, never copy |
| `05_registers-and-contracts/REG-R29.examples.jsonl` | CC-2 | — | — | — | {"_example": "HARDENED-row-shape", "_expect": "VALID", "_note": "EXAMPLE ONLY — not an R29 write (law 6). Shows a fully evidenced HARDENED row; the mechanical_c | 3922 | Added (sprint-1) — Proposed | 106 | T-144 | §1 row (4) + §8 A-002 (+1 R30.1) + §9 A-003 (+1 R30.2) + A-004 | examples for R29 (EXAMPLE rows only) | cdss-spine/registers/ (README: "MOVE here on DEC-02, never copy"); R30 owner cdss-governance | DEC-02 (ratify R29/R30) + DEC-09 (repo owners) — MOVE, never copy |
| `05_registers-and-contracts/REG-R29.schema.json` | CC-2 | cdss-spine/registers/r29-hardening-coverage-row.schema.json | — | — | R29 Hardening Coverage Ledger row (Proposed, DEC-02) | 2048 | Proposed (DEC-02) | 4 | T-004 | §1 row (4) + §8 A-002 (+1 R30.1) + §9 A-003 (+1 R30.2) + A-004 | REG-R29 (JSON Schema) | cdss-spine/registers/ (README: "MOVE here on DEC-02, never copy"); R30 owner cdss-governance | DEC-02 (ratify R29/R30) + DEC-09 (repo owners) — MOVE, never copy |
| `05_registers-and-contracts/REG-R29_hardening_coverage_ledger.schema.md` | CC-2 | REG-R29 | — | — | Proposed (DEC-02). Owner: cdss-spine. Opens: immediately (pre-L1 work permitted). Mutability: append-only. Written by: the MT2 hardening pass only. Readers: operator, all build CI (row-completeness ratchet). | 1212 | Proposed (DEC-02) | 4 | T-143 | §1 row (4) + §8 A-002 (+1 R30.1) + §9 A-003 (+1 R30.2) + A-004 | REG-R29 (md twin) | cdss-spine/registers/ (README: "MOVE here on DEC-02, never copy"); R30 owner cdss-governance | DEC-02 (ratify R29/R30) + DEC-09 (repo owners) — MOVE, never copy |
| `05_registers-and-contracts/REG-R30.1_seed_delta.md` | CC-4 | REG-R30.1 | 1.0 | 2026-09-01 | Added. Additive seed rows over REG-R30 schema+seed; the v1.0 seed file is not edited. Same row fields; same write law (external attestations only for ASSUME closures). | 2024 | Proposed (DEC-02) | 107 | T-151 | §1 row (4) + §8 A-002 (+1 R30.1) + §9 A-003 (+1 R30.2) + A-004 | REG-R30.1 | cdss-spine/registers/ (README: "MOVE here on DEC-02, never copy"); R30 owner cdss-governance | DEC-02 (ratify R29/R30) + DEC-09 (repo owners) — MOVE, never copy |
| `05_registers-and-contracts/REG-R30.2_seed_delta.md` | CC-4 | REG-R30.2 | 1.0 | 2026-09-02 | Added. Additive seed rows over REG-R30 schema+seed and R30.1; neither earlier file is edited. Same row fields; same write law (external attestations only for ASSUME closures). | 4623 | Proposed (DEC-02) | 108 | T-152 | §1 row (4) + §8 A-002 (+1 R30.1) + §9 A-003 (+1 R30.2) + A-004 | REG-R30.2 | cdss-spine/registers/ (README: "MOVE here on DEC-02, never copy"); R30 owner cdss-governance | DEC-02 (ratify R29/R30) + DEC-09 (repo owners) — MOVE, never copy |
| `05_registers-and-contracts/REG-R30.3_row-form_seed.jsonl` | CC-4 | — | — | — | {"reg_id": "REG-FIND-001", "statement": "Mākoha is assessed as **not eligible** for the CDSS exemption. The disqualifier is the diagnostic function, not the use | 317670 | Added (sprint-1) — Proposed | 109 | T-021 | §1 row (4) + §8 A-002 (+1 R30.1) + §9 A-003 (+1 R30.2) + A-004 | REG-R30.3 (row-form seed, 549 rows) | cdss-spine/registers/ (README: "MOVE here on DEC-02, never copy"); R30 owner cdss-governance | DEC-02 (ratify R29/R30) + DEC-09 (repo owners) — MOVE, never copy |
| `05_registers-and-contracts/REG-R30.schema.json` | CC-4 | cdss-spine/registers/r30-regulatory-posture-row.schema.json | — | — | R30 Regulatory Posture Register row (Proposed, DEC-02; owner cdss-governance; mutability versioned; written by regulatory owner + external attestations only) | 4414 | Added (sprint-1) — Proposed | 110 | T-150 | §1 row (4) + §8 A-002 (+1 R30.1) + §9 A-003 (+1 R30.2) + A-004 | REG-R30 (JSON Schema) | cdss-spine/registers/ (README: "MOVE here on DEC-02, never copy"); R30 owner cdss-governance | DEC-02 (ratify R29/R30) + DEC-09 (repo owners) — MOVE, never copy |
| `05_registers-and-contracts/REG-R30_regulatory_posture_register.schema+seed.md` | CC-4 | REG-R30 | — | — | Proposed (DEC-02). Owner: cdss-governance. Opens: L1. Mutability: versioned. Written by: regulatory owner + external attestations only (no ASSUME-REG-* closes by internal reasoning — MAK-ANT §8). Readers: R19/R23 joins, … | 1308 | Proposed (DEC-02) | 5 | T-005 | §1 row (4) + §8 A-002 (+1 R30.1) + §9 A-003 (+1 R30.2) + A-004 | REG-R30 (base) | cdss-spine/registers/ (README: "MOVE here on DEC-02, never copy"); R30 owner cdss-governance | DEC-02 (ratify R29/R30) + DEC-09 (repo owners) — MOVE, never copy |

## §3 Reading rule (P-D-11)

R30 is read as **REG-R30 (base) → R30.1 → R30.2 → R30.3 (row form)**: the base is the field list and prose seed; R30.1 extends the `reg_id` enum and seeds v1.1/NZ/GOV/SPRINT ids; R30.2 adds US/EU/NZ-STD/NZ-GATE/STD and the `jurisdiction` field; R30.3 (`REG-R30.3_row-form_seed.jsonl`) is the same content one row per ID, crosswalked per REG-POSTURE §0.7 with `source_status_verbatim` preserved and `mapping_pending: true` where the regulatory owner's ruling is awaited (survey-2 BSQ-0208). R29 is read as REG-R29 (json + md) → R29.1 (adds `blocker` to the md reading; states the placeholder rule). CONTRACT-ARG-1 (.md) is the field list; the two `.schema.json` files and the RRI test spec are its companions, staged for the DEC-02 + DEC-09 move.

## §4 Honesty line

Nothing in this folder is ratified (DEC-02 Open); no schema has moved to cdss-spine (DEC-09 Open); the skeleton pointer stub still points here. Statuses in the R30 seeds are the *source's* words (standing / not started / not passed / recorded) — the row-form seed maps them to `OPEN` and flags the mapping as pending where §0.7 gives no rule; no ASSUME status is changed anywhere. R29 example rows are EXAMPLES, not ledger writes.

## §5 Self-audit (run 2026-09-05)

- File count in the table = files on disk under `05_registers-and-contracts/` (excluding `.DS_Store`): **16** = 16 — PASS.
- Every path in the table exists — PASS (16/16 at generation; this INDEX itself is written by the same run).
- Every HARDEN-1/1.1 row id and HARDEN-3.1 task id in the table resolves in `04_hardening/HARDEN-1.1_coverage_ledger_seed_delta.md` / `HARDEN-3.1_task_register_delta.md` — PASS (ids taken from the same generated data; 0 ABSENT).
- Recorded validation (P-D-09 / CC-7; `11_prompts/runs/2026-09-05_sprint-1/tools/validate_examples.py`, jsonschema 4.25.1):

```
check_schema 05_registers-and-contracts/CONTRACT-ARG-1.schema.json → OK (Draft 2020-12)
  line 1  GA-valid                                 → VALID   [agrees with _expect]
  line 2  GA-GPP-violates-GPP-9                    → INVALID: {'object_type': 'GenericArgument', 'ga_id': 'GA-EXAMPLE-002', 'ga_version': '1.0.0', 'warrant_type':    [agrees with _expect]
  line 3  AA-valid                                 → VALID   [agrees with _expect]
  line 4  AA-missing-qualifier-SPINE-2             → INVALID: {'object_type': 'ActualArgument', 'arg_id': 'AA-EXAMPLE-002', 'claim': {'type': 'recommendation', 'co   [agrees with _expect]
  line 5  AA-empty-rebuttals-with-grounds-SPINE-2  → INVALID: {'object_type': 'ActualArgument', 'arg_id': 'AA-EXAMPLE-003', 'claim': {'type': 'recommendation', 'co   [agrees with _expect]
  expected/actual agreement: 5/5

check_schema 05_registers-and-contracts/CONTRACT-DEV-1.schema.json → OK (Draft 2020-12)
  line 1  DEV-valid                                → VALID   [agrees with _expect]
  line 2  DEV-missing-author                       → INVALID: 'author_identity' is a required property   [agrees with _expect]
  expected/actual agreement: 2/2

check_schema 05_registers-and-contracts/REG-R29.schema.json → OK (Draft 2020-12)
  line 1  HARDENED-row-shape                       → VALID   [agrees with _expect]
  line 2  ESCALATED-row-0                          → VALID   [agrees with _expect]
  line 3  INVALID-PENDING-placeholder              → INVALID: 'PENDING' is not one of ['HARDENED', 'ESCALATED']   [agrees with _expect]
  expected/actual agreement: 3/3

check_schema REG-R30.schema.json → OK (Draft 2020-12)
rows=549 invalid=0 valid=549 duplicates=0 self-statement=0 ASSUME-not-OPEN=0
```
- Pointer stub exists: `06_repositories/repo-skeletons/cdss-spine/contracts/CONTRACT-ARG-1.pointer.md` — PASS; `cdss-spine/registers/README.md` names R29/R30 — PASS.
```
$ ls -l 05_registers-and-contracts
total 840
-rw-r--r--@ 1 ken-lee-arepo  staff    4101 Sep  5 15:41 CONTRACT-ARG-1.examples.jsonl
-rw-r--r--@ 1 ken-lee-arepo  staff    7405 Sep  5 15:41 CONTRACT-ARG-1.schema.json
-rw-r--r--@ 1 ken-lee-arepo  staff    2204 Sep  4 05:13 CONTRACT-ARG-1_argument_schema.md
-rw-r--r--@ 1 ken-lee-arepo  staff     674 Sep  5 15:41 CONTRACT-DEV-1.examples.jsonl
-rw-r--r--@ 1 ken-lee-arepo  staff    1953 Sep  5 15:41 CONTRACT-DEV-1.schema.json
-rw-r--r--@ 1 ken-lee-arepo  staff    5657 Sep  5 15:41 CONTRACT-RRI-1_render-invariance_test-spec.md
-rw-r--r--@ 1 ken-lee-arepo  staff   16390 Sep  5 16:12 INDEX.md
-rw-r--r--@ 1 ken-lee-arepo  staff    2645 Sep  5 15:42 REG-R29.1_schema_twin_delta.md
-rw-r--r--@ 1 ken-lee-arepo  staff    3922 Sep  5 15:42 REG-R29.examples.jsonl
-rw-r--r--@ 1 ken-lee-arepo  staff    2048 Sep  4 05:13 REG-R29.schema.json
-rw-r--r--@ 1 ken-lee-arepo  staff    1212 Sep  4 05:13 REG-R29_hardening_coverage_ledger.schema.md
-rw-r--r--@ 1 ken-lee-arepo  staff    2024 Sep  4 05:13 REG-R30.1_seed_delta.md
-rw-r--r--@ 1 ken-lee-arepo  staff    4623 Sep  4 05:13 REG-R30.2_seed_delta.md
-rw-r--r--@ 1 ken-lee-arepo  staff  317670 Sep  5 15:44 REG-R30.3_row-form_seed.jsonl
-rw-r--r--@ 1 ken-lee-arepo  staff    4414 Sep  5 15:42 REG-R30.schema.json
-rw-r--r--@ 1 ken-lee-arepo  staff    1308 Sep  4 05:13 REG-R30_regulatory_posture_register.schema+seed.md
```
