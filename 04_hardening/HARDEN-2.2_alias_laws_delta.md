---
doc_id: HARDEN-2.2
title: "HARDEN-2.2 — alias laws for the CC prefix (HARDEN-2 class bars vs MAK-LBP requirements) and the W token (HARDEN-3 waves vs FOLD-1 steps)"
version: "1.2-delta"
date: "2026-09-05"
status: "Added (sprint-2). Additive delta over HARDEN-2 v1.0 and HARDEN-2.1 (neither edited); read HARDEN-2 through 2.1 through this file. Both laws are drafted here and in MET-2.2 §5 as DEC-26(a) and DEC-26(c); they are Proposed until the Architecture owner rules DEC-26. The R29 schema `class` enum is unchanged (DEC-02 ratified it as-is). The corpus (03_) is untouched."
supersedes: "nothing — HARDEN-2 and HARDEN-2.1 preserved verbatim beside this file"
applies_to: "04_hardening/HARDEN-2_hardening_spec.md (CC-1..8); 04_hardening/HARDEN-2.1_spec_census_and_self-audit_delta.md; 04_hardening/HARDEN-3_hardening_plan_worklist.md (W0–W11); 10_regulatory-execution/FOLD-1_antennae_fold_worklist.md (W1–W5)"
change_policy: "Additive delta per the MET-1.1 pattern; no class bar, wave or step renamed"
req_prefix: CC
req_count: 8
produced_by: "sprint-2 (survey-3 Queue §c.1 row QI-0025; §c EXECUTABLE-AFTER-DECISION row QI-0030) — 11_prompts/runs/2026-09-05_sprint-2/"
---

# HARDEN-2.2 — alias laws (CC, W)

## D-1 — CC: the collision (survey-3 QI-0025, confidence 90)

HARDEN-2 / HARDEN-2.1 mint the class bars `CC-1..CC-8`, cited by every HARDEN-1.1 ledger row, every
INDEX file table and every HARDEN-3.1 task as "class CC-n". MAK-LBP (`03_makoha-butterfly-corpus/corpus-md/labial-palps-corpus_v1.0.md`)
mints `CC-1..CC-5` as clinician-UI requirements. "CC-5" is a CI-configuration class bar in 04_/06_ and a
clinician-UI requirement in 03_.

```
grep -o 'CC-[1-8]\b' 04_hardening/HARDEN-2_hardening_spec.md | sort | uniq -c
   2 CC-1   2 CC-2   1 CC-3   1 CC-4   1 CC-5   1 CC-6   1 CC-7   1 CC-8                       (8 ids)
grep -o 'CC-[1-5]\b' 03_makoha-butterfly-corpus/corpus-md/labial-palps-corpus_v1.0.md | sort | uniq -c
   6 CC-1   8 CC-2   5 CC-3   5 CC-4   3 CC-5                                                   (5 ids)
grep -c '^| [0-9]* | `[^`]*` | CC-' 04_hardening/HARDEN-1.1_coverage_ledger_seed_delta.md   → 272 ledger rows carry a CC-n class
```

## D-2 — alias law (CC) — Proposed; becomes law on DEC-26(c)

> **Alias law (CC).** In 04_, 05_, 06_, 07_, 09_, 10_ and every HARDEN / R29 row, `CC-n` names a
> HARDEN-2 class bar (CC-1..CC-8). In 03_, `CC-n` names a MAK-LBP requirement (CC-1..CC-5). A
> cross-folder citation MUST qualify: `HARDEN-2 CC-5` / `MAK-LBP CC-2`. The R29 `class` field keeps
> `CC-n` (schema unchanged, DEC-02); the qualifier is prose-only. Neither family is renamed.

## D-3 — W: the collision (survey-3 QI-0030, confidence 90)

HARDEN-3 waves are `W0..W11`; FOLD-1 (`10_regulatory-execution/FOLD-1_antennae_fold_worklist.md`) steps
are `W1..W5`. PROMPT-FOLD-1 already cites the fold steps in qualified form.

```
grep -o '\bW[1-5]\b' 10_regulatory-execution/FOLD-1_antennae_fold_worklist.md | sort | uniq -c
   1 W1   1 W2   1 W3   1 W4   2 W5
```

## D-4 — alias law (W) — Proposed; becomes law on DEC-26(a)

> **Alias law (W).** An unqualified `W-n` / `Wn` means a HARDEN-3 wave (the pass, W0–W11). A FOLD-1
> step is cited `FOLD-1 W-n` or `FW-n`. HARDEN-3.1's wave census and PROMPT-HARDEN read waves only;
> PROMPT-FOLD-1 reads steps only.

## D-5 — census and self-audit

CC class bars: 8 (unchanged; HARDEN-2.1 D-2 census stands). Laws drafted: 2 (CC, W). Register home:
MET-2.2 §5 DEC-26 (Open). No class bar, wave or step renamed; R29 schema byte-identical
(`05_registers-and-contracts/REG-R29.schema.json` in CHECKSUMS_BEFORE = AFTER). Ledger row and task for
this file: HARDEN-1.2 / HARDEN-3.2 (same sprint).
