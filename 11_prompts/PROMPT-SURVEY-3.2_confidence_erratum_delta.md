---
doc_id: PROMPT-SURVEY-3.2
title: "PROMPT-SURVEY-3.2 — erratum delta over PROMPT-SURVEY-3.1: D-1 property count corrected (six, not four); the scorer-failure sentinel `confidence: 100` replaced by an explicit `scorer_failed` flag routed to §j"
version: "1.2-delta"
date: "2026-09-05"
status: "Proposed. Additive erratum over PROMPT-SURVEY-3.1 (not edited — it was merged to main in PR #12 before the Copilot review that found these two defects had posted). Read PROMPT-SURVEY-3 through 3.1 and 3.1 through this file. Adds this file under 11_prompts/ only; edits nothing in 00_–10_. Not yet run."
supersedes: "nothing — PROMPT-SURVEY-3 v1.0 and PROMPT-SURVEY-3.1 preserved verbatim beside this file"
applies_to: "11_prompts/PROMPT-SURVEY-3.1_deep-review_fold_delta.md (D-1, D-2, §j, T-11, §4)"
change_policy: "Additive erratum per the MET-1.1 pattern. Items E-1..E-3 each quote the 3.1 line they correct (path:line as merged, commit 9374803) and give the replacement text. Where 3.1 and this file disagree, this file governs; everything else in 3.1 stands."
produced_by: "Claude Code session 2026-09-05 · requester: Ken Lee (ken.lee@arepo-tech.ai) · source of the findings: GitHub Copilot code review on PR #12 (two inline comments, 2026-09-05T09:12:34Z), both accepted"
---

# PROMPT-SURVEY-3.2 — erratum over PROMPT-SURVEY-3.1

## 0. Provenance and delta-reading rule

PROMPT-SURVEY-3.1 was opened as PR #12 by Kenny-bytes at 09:10 UTC on 5 September 2026, merged by
Kenny-bytes at 09:11:21, and reviewed by Copilot at 09:12:34 — after the merge. Copilot's review
("Changes recommended", two inline comments, effort level Lite) found two defects, both correct:

1. `PROMPT-SURVEY-3.1_deep-review_fold_delta.md:138` — "Section title says 'four additive properties'
   but the snippet adds five properties (confidence, confidence_reason, attribution, calibrated_weight,
   calibration_note)".
2. `PROMPT-SURVEY-3.1_deep-review_fold_delta.md:176` — "D-2 specifies setting `confidence: 100` when
   the scorer fails and claims this matches deep-review, but §1.1 only establishes that deep-review
   keeps findings when scoring fails (not that it assigns 100). Also, 100 on failure undermines the
   meaning of a confidence score."

Because 3.1 was already on `main`, it is retained and cannot be edited (AGENTS.md law 1). This file
is the correction. An executor applies PROMPT-SURVEY-3 v1.0, then 3.1's D-1..D-9, then E-1..E-3 below,
before Phase 0 opens.

## 1. Errata

### E-1 — D-1 title and property set (corrects 3.1 `:138–152`)

3.1 line 138 reads `### D-1 — QI schema: four additive properties and two conditions`. Read it as:

> **D-1 — QI schema: six additive properties and two conditions.**

The five properties 3.1 lists (`confidence`, `confidence_reason`, `attribution`, `calibrated_weight`,
`calibration_note`) stand. Add a sixth to the `properties` merge:

```json
"scorer_failed": {"type":"boolean",
  "description":"D-2 as corrected by 3.2 E-2: true when the confidence-scoring step could not score this row; the row is kept, `confidence` is omitted, and the row is listed under §j Needs verification"}
```

Replace the first of 3.1's two `allOf` conditions with:

```json
{"if":{"properties":{"severity":{"enum":["CRITICAL","WARNING"]}}},
 "then":{"required":["confidence_reason","attribution"],
         "oneOf":[{"required":["confidence"],"not":{"required":["scorer_failed"]}},
                  {"required":["scorer_failed"],"properties":{"scorer_failed":{"const":true}},
                   "not":{"required":["confidence"]}}]}}
```

The second condition (`calibrated_weight` ⇒ `calibration_note`) is unchanged. Net effect: every
CRITICAL and WARNING row carries attribution and a confidence reason, and either a confidence score or
an explicit statement that scoring failed — exactly one of the two, never both, never a number that was not assigned.

### E-2 — Law 16, scorer-failure sentence (corrects 3.1 `:175–177`)

3.1 lines 175–177 read: "A row whose scorer step failed keeps `confidence: 100` with
`confidence_reason: "scorer failed — kept by default"`, exactly as deep-review does, so a broken step
never makes a finding disappear." Read instead:

> A row whose scorer step failed is **kept**, as deep-review keeps it, but is not given a number: it
> carries `scorer_failed: true`, no `confidence`, and `confidence_reason: "scorer failed — unscored,
> kept"`, and is listed under §j "Needs verification" until scored. A broken step never makes a
> finding disappear, and it never manufactures certainty either.

Evidence the erratum rests on: deep-review's headless script does write the sentinel `SCORE=100` for
an unscored finding (`scripts/standalone-review.sh:439` and `:447`, plugin version 5.8.0) — so 3.1's
"exactly as deep-review does" was true of the script but not quoted in 3.1 §1.1, which is Copilot's
first point; and a failure recorded as certainty would corrupt the confidence column, which is its
second. 3.1 §4 therefore gains a fifth not-imported item:

> 5. **`SCORE=100` on scorer failure.** deep-review's safe default records an unscored finding as
> certain (`standalone-review.sh:439`, `:447`). The *keeping* is imported; the *number* is not — an
> unscored row is marked `scorer_failed: true` and routed to §j, so the confidence column only ever
> holds scores that were actually assigned.

### E-3 — Consequential wording in §j and T-11 (3.1 `:284`, `:292`)

- §j — 3.1 `:284` currently reads: "**Needs verification** — CRITICAL rows with confidence < 80 (law
  16), each with the one check that would settle it." Replace with: "**Needs verification** — CRITICAL
  rows with confidence < 80 **and every CRITICAL or WARNING row with `scorer_failed: true`** (law 16),
  each with the one check that would settle it."
- T-11 pass criteria — 3.1 `:292` currently reads: "every CRITICAL/WARNING row in `QI.jsonl` has
  `confidence` + `confidence_reason`; no CRITICAL with confidence < 80 appears in §c; rows < 60 appear
  in §e with score; `jq` count pasted". Replace with: "every CRITICAL/WARNING row in `QI.jsonl` has
  `confidence_reason` + `attribution` and exactly one of `confidence` or `scorer_failed: true`; no
  CRITICAL with confidence < 80 and no `scorer_failed` row appears in §c; rows < 60 appear in §e with
  score; unscored rows appear in §j; `jq` counts pasted"."

## 2. Process note (recorded, not adjudicated)

The Copilot review under ruleset 22326380 does not block merging: PR #12 was merged 73 seconds
before the review posted. The two defects above would have been fixed on the branch had the review
been read first. Whether the "Running Copilot Code Review" job (or the mechanical audit) should become
a required status check on `main` is a governance decision for the repository owner; it is noted here
as a candidate for the next amendment, not decided.

## 3. What this erratum did not do

Did not edit PROMPT-SURVEY-3 v1.0, PROMPT-SURVEY-3.1 or A-006; did not run PROMPT-SURVEY-3; did not
change any tooling. Ledger debt: this file joins the A-005/A-006 debt owed by a HARDEN-1.2 / HARDEN-3.2
delta.
