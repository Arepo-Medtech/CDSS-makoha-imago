---
doc_id: RESEARCH-1.2
title: "RESEARCH-1.2 — alias law for the RG prefix (research gaps vs MAK-CEC requirements), RGAP- declared for new mints, trigger column per gap"
version: "1.2-delta"
date: "2026-09-05"
status: "Added (sprint-2). Additive delta over RESEARCH-1 v1.0 and RESEARCH-1.1 (neither edited); read RESEARCH-1 through 1.1 through this file. The alias law is drafted here and in MET-2.2 §5 as DEC-26(b); it is Proposed until the Architecture owner rules DEC-26. The corpus (03_) is untouched: MAK-CEC keeps RG-1..8."
supersedes: "nothing — RESEARCH-1 v1.0 and RESEARCH-1.1 preserved verbatim beside this file"
applies_to: "08_research/RESEARCH-1_findings_gaps_source_map.md §3; 08_research/RESEARCH-1.1_findings_delta.md D-3; 08_research/INDEX.md §3"
change_policy: "Additive delta per the MET-1.1 pattern. RG-01..08 keep their ids and remain valid citations; no research gap is renamed; new research gaps from this delta onward mint as RGAP-nnn."
req_prefixes: [RG, RGAP]
req_count: 8
produced_by: "sprint-2 (survey-3 Queue §c.1 row QI-0024; §d row QI-0022) — 11_prompts/runs/2026-09-05_sprint-2/"
---

# RESEARCH-1.2 — RG alias law and triggers

## D-1 — the collision (survey-3 QI-0024, confidence 90)

One prefix, two requirement-bearing families. MAK-CEC (`03_makoha-butterfly-corpus/corpus-md/compound-eyes-corpus_v1.1.md`,
Part 4) mints `RG-1..RG-8` as regulatory-guardrail **requirements**; RESEARCH-1 §3 and RESEARCH-1.1 D-3
mint `RG-01..RG-08` as research **gaps**. A citation "RG-3" resolves to a corpus MUST; "RG-03" to a
research gap; until now nothing said so.

Counts (run 2026-09-05 from the repository root):

```
grep -o 'RG-[1-8]\b' 03_makoha-butterfly-corpus/corpus-md/compound-eyes-corpus_v1.1.md | sort | uniq -c
  21 RG-1    6 RG-2    9 RG-3   14 RG-4   10 RG-5   11 RG-6    6 RG-7   10 RG-8        (one-digit: 87 citations, 8 ids)
grep -oh 'RG-0[1-8]' 08_research/*.md | sort | uniq -c
   6 RG-01   3 RG-02   3 RG-03   3 RG-04   6 RG-05   4 RG-06   5 RG-07   5 RG-08       (two-digit: 35 citations, 8 ids)
```

## D-2 — alias law (RG) — Proposed; becomes law on DEC-26

> **Alias law (RG).** `RG-nn` two-digit ids are research gaps (RESEARCH-1 §3; RESEARCH-1.1 D-3;
> INDEX-08 §3). `RG-n` one-digit ids are MAK-CEC requirements (compound-eyes-corpus v1.1, Part 4). The
> two families share a prefix by accident; neither is renamed retrospectively. A cross-folder citation
> MUST use the padded form for a gap (`RG-03`) and MAY qualify either (`MAK-CEC RG-3`, `RESEARCH-1
> RG-03`). New research gaps from this delta onward are minted `RGAP-nnn` (three-digit); `RG-01..08`
> remain valid citations and resolve to RESEARCH-1.

Register home for the law: MET-2.2 §5 (DEC-26, Open). Home for the gaps: RESEARCH-1.n (unchanged).

## D-3 — trigger column per gap (survey-3 QI-0022)

RESEARCH-1 §3 carries Gap · What's needed · Who; RESEARCH-1.1 D-3 adds Closes into. Neither says when.
Read against the EXEC-1 run map (in force on DEC-22, MET-2.2 §3.1):

| Gap | Who (RESEARCH-1.1) | Account (MET-2.2 §1) where a house role | Trigger / when (RUN or DEC) |
|---|---|---|---|
| `RG-01` | DEC-12 executor | [NEEDS DEFINITION — DEC-12] | RUN-1 · Foundation (MET-4 P1 "DEC-12 HeyDoc inventory"; MET-4.1 G-08) |
| `RG-02` | AU counsel | external | RUN-0 · Decide — inside the `TASK-REG-002` engagement (`Q-REG-009`) |
| `RG-03` | Baseten | external | RUN-1 · Foundation — on DEC-03 ruling for Baseten (`TASK-REG-009`); moot if DEC-03 rules Bedrock |
| `RG-04` | Legal | [NEEDS DEFINITION] | on DEC-04 ruling (fabric v0 design; RUN-1) — only if the ruling prefers immudb |
| `RG-05` | cdss-conformal owner | Kenny-bytes (repo owner, DEC-09) | standing watch; re-read before any L-capability qualifier claim (L3 → RUN-2/RUN-3 boundary) |
| `RG-06` | Regulatory owner | kendo-Jones | RUN-0 · Decide — once `TASK-REG-001` exists (`WATCH-REG-002`) |
| `RG-07` | cdss-lumos owner / PROMPT-H run | Kenny-bytes (repo owner, DEC-09) | RUN-1 · Foundation — before the `TASK-REG-015` evidence plan is written |
| `RG-08` | cdss-conformal owner | Kenny-bytes (repo owner, DEC-09) | with RG-05; DEPLOY-2 §1 coverage acceptance (L3) |

## D-4 — census and self-audit

RG (two-digit research gaps): `RG-01..RG-08` = 8, all present in D-3; RGAP: 0 minted (prefix declared,
first use reserved for RESEARCH-1.3+). `grep -c '^| \`RG-0' 08_research/RESEARCH-1.2_alias_and_triggers_delta.md` → 8.
No gap closed, none added, none renamed. Corpus untouched (CHECKSUMS in the sprint-2 run directory).
Ledger row and task for this file: HARDEN-1.2 / HARDEN-3.2 (same sprint).
