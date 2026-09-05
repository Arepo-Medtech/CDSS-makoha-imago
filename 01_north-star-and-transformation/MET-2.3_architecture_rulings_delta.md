---
doc_id: MET-2.3
title: "MET-2.3 — Decision Register Delta: DEC-24, DEC-25 and DEC-26 ruled as drafted (doc_id supersession rule; R25 label; W / RG / CC alias laws)"
version: "1.0"
date: "2026-09-05"
status: "Added. Additive delta to MET-2, MET-2.1 and MET-2.2 (none edited). Read MET-2 through 2.1 through 2.2 through this file. Where a row here states a State, it governs over the same row in MET-2.2 §2."
supersedes: "nothing — MET-2, MET-2.1 and MET-2.2 preserved verbatim beside this file"
applies_to: "01_north-star-and-transformation/MET-2.2_decision_closures_delta.md §2 rows DEC-24..26 and §5; 08_research/RESEARCH-1.2_alias_and_triggers_delta.md D-2; 04_hardening/HARDEN-2.2_alias_laws_delta.md D-2, D-4; GLOSSARY.md rows W-n, CC-n, RG-nn, R25; 09_diagrams/register_topology_v4.mermaid (R25 label)"
change_policy: "Additive delta. The three rulings were given by the Architecture owner on 2026-09-05 in the words 'Rule DEC-24 to DEC-26 as drafted'; the law text below is the MET-2.2 §5 draft quoted verbatim. No other decision changes State."
ruled_by: "Kenny-bytes (Architecture owner per MET-2.2 §1) — 2026-09-05, in the Claude Code session that produced this file"
req_prefixes: [DEC]
req_count: 0
id_families: "DEC: DEC-01..DEC-26 unchanged in count (26); this file mints none and closes three (DEC-24, DEC-25, DEC-26)"
---

# MET-2.3 — Architecture rulings DEC-24..26

## 0. Provenance

MET-2.2 §5 drafted three decisions from survey-3 rows QI-0001, QI-0029, QI-0030, QI-0024 and QI-0025
and left them Open for the Architecture owner. Sprint-2 wrote the alias-law text into RESEARCH-1.2 D-2
and HARDEN-2.2 D-2/D-4 marked Proposed. On 2026-09-05 the Architecture owner ruled all three **as
drafted**. This file is the register record; the law text is quoted, not rewritten.

## 1. Rulings (verbatim from MET-2.2 §5)

### DEC-24 — doc_id supersession rule — CLOSED
> "Superseded versions keep their doc_id and MUST carry `supersedes:`; a citation of a versioned file
> MUST name the version (README 'How to cite' already requires the commit)."

Effect: `REG-POSTURE` (v1.1, v1.2) and `REG-NZ` (v1.0, v1.1) sharing a doc_id is lawful; the
frontmatter census's "doc_id repeats" line is a report, not a defect. Reading of the drafted sentence, as
the tree already practises it: the file that supersedes carries `supersedes:` naming what it replaces
(REG-POSTURE v1.2 → v1.1, v1.0; REG-POSTURE v1.1 → v1.0; REG-NZ v1.1 → v1.0); a first version has
nothing to supersede and carries none (REG-NZ v1.0). A citation reads "REG-POSTURE v1.2", never bare
"REG-POSTURE".

### DEC-25 — R25 label — CLOSED
> One label in Arch §12.2 is authoritative ("Build Evidence & Assumptions Ledger"); "property runs"
> (Primer A A10 / IMAGO-3) becomes its alias; IMAGO-3 v4 carries the authoritative label.

Effect: the register is **R25 Build Evidence & Assumptions Ledger**; "property runs" is an alias and
resolves to it. `09_diagrams/register_topology_v4.mermaid` was regenerated before this ruling and
still reads "R25 property runs (label under ruling — DEC-25)"; the ruling's last clause is therefore
owed by the next regeneration (a v5 successor under PROC-09-REGEN), recorded in §3.

### DEC-26 — namespace alias laws — CLOSED
> (a) Unqualified `W-n` means HARDEN-3 (the pass); FOLD-1 steps are cited `FOLD-1 W-n` or `FW-n`.
> (b) `RG-nn` (two-digit) = research gap, home RESEARCH-1.n; `RG-n` (one-digit) = MAK-CEC
> requirement, home MAK-CEC; citations use the padded form; new research gaps mint as `RGAP-`.
> (c) `CC-n` in 04_/05_/06_ and HARDEN rows = HARDEN-2 class bar; MAK-LBP `CC-n` resolves only
> inside 03_; the R29 schema `class` enum spells the bars `HCC-n` on ratification. The corpus is
> untouched in every case.

Effect: RESEARCH-1.2 D-2 and HARDEN-2.2 D-2 / D-4 are law, no longer Proposed. On clause (c)'s last
sentence: the R29 schema was ratified as-is by DEC-02 and HARDEN-2.2 D-2 states "the R29 `class`
field keeps `CC-n` (schema unchanged, DEC-02); the qualifier is prose-only". The two texts differ on
whether the schema enum is respelled. The ruling "as drafted" adopts the MET-2.2 wording; the respelling
to `HCC-n` is therefore a schema change owed at the next R29 schema version (a REG-R29.2 twin delta),
not an edit to the ratified schema. Until then `CC-n` stands in the enum and the prose qualifier
applies. Recorded in §3 rather than silently reconciled.

## 2. Register rows (govern over MET-2.2 §2)

| DEC | Decision (short) | Owner | Closes on | Closed on | State |
|---|---|---|---|---|---|
| DEC-24 | doc_id supersession rule | Architecture owner (Kenny-bytes) | this ruling (§1) | 2026-09-05 | **Closed — ruled as drafted** |
| DEC-25 | R25 label | Architecture owner (Kenny-bytes) | this ruling (§1); diagram label owed (§3) | 2026-09-05 | **Closed — ruled as drafted** |
| DEC-26 | W / RG / CC alias laws | Architecture owner (Kenny-bytes) | this ruling (§1); R29 enum respelling owed (§3) | 2026-09-05 | **Closed — ruled as drafted** |

Census: DEC-01..26 = 26 rows; Closed after this file: 12 (DEC-01, 02, 08, 09, 10, 11, 13, 14, 22, 24,
25, 26) + DEC-21 namespace component + DEC-23 names. Open: 11 (DEC-03..07, 12, 15..17, 19, 20) +
DEC-18 provisional + DEC-21 repo component + DEC-23 values. No decision minted.

## 3. Read-through and owed work

| # | Text that now reads differently | Read it now as | Owed |
|---|---|---|---|
| R-01 | `08_research/RESEARCH-1.2_alias_and_triggers_delta.md` D-2 "Proposed; becomes law on DEC-26" | law | — |
| R-02 | `04_hardening/HARDEN-2.2_alias_laws_delta.md` D-2 and D-4 "Proposed; becomes law on DEC-26(c)/(a)" | law | REG-R29.2 twin delta to respell the `class` enum `HCC-n` (schema change; DEC-02 ratified the current enum) |
| R-03 | `GLOSSARY.md` rows W-n, CC-n, RG-nn "DEC-26 … Proposed — OPEN"; row R25 "DEC-25 Proposed — OPEN (label under ruling)" | Closed — law / R25 = Build Evidence & Assumptions Ledger, alias "property runs" | GLOSSARY v1.1 or companion at the next glossary pass |
| R-04 | `09_diagrams/register_topology_v4.mermaid` and `cdss_diagrams_v4.html` §3 "R25 property runs (label under ruling — DEC-25)" | R25 Build Evidence & Assumptions Ledger (alias: property runs) | register_topology v5 + cdss_diagrams v5 under PROC-09-REGEN, with INDEX-09.2 |
| R-05 | `01_north-star-and-transformation/MET-2.2_decision_closures_delta.md` §2 rows DEC-24..26 "Proposed — Open"; §5 | Closed (this file) | — |
| R-06 | `.github/audit/frontmatter_census.py` line "doc_id repeats … need a supersedes: field" | DEC-24 law; §4 check 3 shows every superseding file carries `supersedes:` — the repeats are lawful | — |
| R-07 | Primer A A10 / IMAGO-3 "property runs" (02_, 03_ retained) | alias of R25 | — (alias law; no edit) |

## 4. What this file did not do

Minted no decision; changed no State but DEC-24..26; edited nothing retained; respelled no schema
enum; regenerated no diagram; wrote no R29 row. Ledger debt: this file has no HARDEN-1.x row or
HARDEN-3.x task — owed by the next HARDEN-1.3 / HARDEN-3.3 delta together with the files §3 owes.

## 5. Self-audit (run 2026-09-05 from the repository root; outputs quoted)

```
1. grep -c '^| DEC-2[4-6]' 01_north-star-and-transformation/MET-2.3_architecture_rulings_delta.md        → 3
2. grep -n 'DEC-2[4-6]' 01_north-star-and-transformation/MET-2.2_decision_closures_delta.md | grep -c 'Proposed — Open'   → 3   (the rows this file closes)
3. grep -n '^supersedes' 10_regulatory-execution/REG-POSTURE_v1.2.md 10_regulatory-execution/REG-POSTURE_v1.1.md 10_regulatory-execution/REG-NZ_v1.1.md 10_regulatory-execution/REG-NZ_v1.0.md
   → REG-POSTURE_v1.2.md:13 supersedes: REG-POSTURE v1.1 (2026-09-01); REG-POSTURE v1.0 (2026-08-31)
   → REG-POSTURE_v1.1.md:11 supersedes: REG-POSTURE v1.0 (2026-08-31)
   → REG-NZ_v1.1.md:13 supersedes: REG-NZ v1.0 (2026-09-01)
   (grep prints no line for REG-NZ_v1.0.md — it has no supersedes: field)
   note, not output: REG-NZ v1.0 is a first version with nothing to supersede; every superseding file complies; nothing owed
4. grep -c 'Proposed; becomes law on DEC-26' 08_research/RESEARCH-1.2_alias_and_triggers_delta.md 04_hardening/HARDEN-2.2_alias_laws_delta.md → 1 + 2 (retained; read via R-01/R-02)
5. python3 .github/audit/refcheck.py 01_north-star-and-transformation/MET-2.3_architecture_rulings_delta.md → dead in-repo paths: 0; unresolved anchors: 0
```

