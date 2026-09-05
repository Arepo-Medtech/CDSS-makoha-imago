---
doc_id: REG-R29.1
title: "R29.1 — schema twin delta: `blocker` field, placeholder rule, recorded validation"
version: "1.1-delta"
date: "2026-09-05"
status: "Added. Additive delta over REG-R29_hardening_coverage_ledger.schema.md; neither the md base nor REG-R29.schema.json is edited. Read REG-R29 (md) through this file. Nothing here is an R29 row (law 6): the examples file carries EXAMPLE rows only."
applies_to: "05_registers-and-contracts/REG-R29_hardening_coverage_ledger.schema.md (md twin) and REG-R29.schema.json (Draft 2020-12)"
change_policy: "Additive delta per the MET-1.1 pattern. Base text stands except where a D-row names it."
---

# R29.1 — schema twin delta

## D-1 — `blocker` added to the md field list

The JSON Schema requires `blocker` when `state = ESCALATED` (`allOf` if/then); the md
twin's field list omitted it (survey-2 `r29_schema_check.txt`: `json-only: ['blocker']
| md-only: []`). The md field list is read as including:

> `blocker` (string — required when `state` is ESCALATED; the specific blocker that
> surfaces in the operator's consolidated report, MT2 §7(2))

## D-2 — placeholder rule stated register-side

HARDEN-1's `PENDING`, `BLOCKED`, `ESCALATED-placeholder` and `PENDING-ENUMERATION` marks
are **pre-pass placeholders and are not R29 rows** (HARDEN-1 l.30: "This seed's PENDING
marks are pre-pass placeholders, not a third state"). The schema enforces this: a row
with `state: PENDING` fails validation. Loading the seed into R29 on DEC-02 therefore
requires the pass to convert each row on contact; no transformation of the seed itself
is permitted (append-only; written only by the pass).

## D-3 — recorded validation (P-D-09 / CC-7)

Run 2026-09-05 from the repository root with `jsonschema 4.25.1` (run-local venv,
`11_prompts/runs/2026-09-05_sprint-1/.venv`):

```
$ check_schema REG-R29.schema.json → OK (Draft 2020-12)
$ validate REG-R29.examples.jsonl against REG-R29.schema.json
  line 1  HARDENED-row-shape        → VALID
  line 2  ESCALATED-row-0           → VALID
  line 3  INVALID-PENDING-placeholder → INVALID: 'PENDING' is not one of ['HARDENED', 'ESCALATED']
  expected/actual agreement: 3/3
```

(Output reproduced in `11_prompts/runs/2026-09-05_sprint-1/RUN-REPORT.md` §validation.)

## Census and self-audit

D-rows: 3. Fields added to the md reading: 1 (`blocker`). Checks: (1) every field in
REG-R29.schema.json `properties` appears in the md field list or in D-1 — PASS (13/13);
(2) examples validate as expected — PASS (3/3); (3) no R29 row written — PASS (examples
carry `_example`, `_expect`, `_note` keys and live outside any register).
