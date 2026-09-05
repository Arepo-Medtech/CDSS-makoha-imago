---
doc_id: RESEARCH-1.1
title: "RESEARCH-1.1 — findings delta: post-2026-09-01 findings registered; status field; RG closure path"
version: "1.1-delta"
date: "2026-09-05"
status: "Added. Additive delta over RESEARCH-1 v1.0 (not edited); read RESEARCH-1 through this file. Registers findings that until now lived only in 11_prompts (PROMPT-SERIES evidence pack) and 05_ (R30.1/R30.2 sources). Quotes, never re-verifies: every figure below is carried exactly as its source states it, with the source named; no literature was re-fetched this pass and no clinical number is asserted."
supersedes: "nothing — RESEARCH-1 v1.0 preserved verbatim beside this file"
applies_to: "08_research/RESEARCH-1_findings_gaps_source_map.md"
change_policy: "Additive delta per the MET-1.1 pattern."
req_prefix: RG
req_count: 8
---

# RESEARCH-1.1 — findings delta

## D-1 — status field for the base (P-D-01/P-D-02)

RESEARCH-1 v1.0 carries `doc_id`, `title`, `version`, `date` and no `status`. Read as:

> status: "Added (2026-09-01). §1 sources not re-verified this pass unless noted; §2 fetches dated 1 Sep 2026; §3 gaps OPEN, no findings fabricated; §4 sources named, not consulted."

## D-2 — findings surfaced after 2026-09-01 (quoted from their registering documents)

| Source (in-tree) | Finding as stated there | Feeds |
|---|---|---|
| `11_prompts/PROMPT-SERIES_A-L_index.md` — Evidence pack, item (i) (PubMed, 2026-09-02) | "the only indexed Lumos paper (Correll et al. 2021, DOI 10.1136/ihj-2021-000074) reports 1.3M patients / 16% of NSW, not Primer H1's '6.8M+'; the '2025 data-quality cohort study' was not located in PubMed — PROMPT-H must source both or mark NOT-LOCATED" | **RG-07** (new, below); PROMPT-H run; Primer H §H1 erratum candidate (annex, never edit) |
| `11_prompts/PROMPT-SERIES_A-L_index.md` — Evidence pack, item (ii) | "Conformal prediction's coverage guarantee is well supported in recent clinical applications (e.g., Cina et al. 2026, DOI 10.1038/s41598-026-35343-6), but no CP study in primary-care differential diagnosis was found" | **RG-08** (new); RG-05 watch (MAK-ELSM §05: "track it; do not ship ahead of it") |
| `05_registers-and-contracts/REG-R30.1_seed_delta.md` — `SRC-REG-011..014` | SRC-REG-011 MAK-J3 v0.9 · SRC-REG-012 MAK-ANT Part 4 signal S-2 (**secondary source**; REG-FIND-010/011 carry lower confidence until the primary is read) · SRC-REG-013 MAK-FFC v1.1 XC-1..3 · SRC-REG-014 MET-2 register | REG-POSTURE §11; RG-06 (the primary AI-SaMD guidance read against the intended purpose) |
| `05_registers-and-contracts/REG-R30.2_seed_delta.md` — `SRC-REG-015..020`; `US-SRC-001..019`; `EU-SRC-001..014`; `NZ-SRC-006..013` | REG-POSTURE v1.2 §11 rows 015–020 (IMDRF N10/N12/N23/N41; N60/N70/N73/N88 — "N88 currency to verify"; Ketryx correspondence — vendor-stated; MAK-GOV) and the three jurisdiction source registers | REG-POSTURE v1.2 §11; REG-US §11; REG-EU §11; REG-NZ v1.1 §11 — cited here, not restated |

## D-3 — research gaps added (RG-07, RG-08) and the closure path for every RG

| Gap | What's needed | Who | Closes into |
|---|---|---|---|
| `RG-01` (v1.0) | HeyDoc below-README clone inventory | DEC-12 executor | DEC-12 (MET-2); G-08 (MET-4) |
| `RG-02` (v1.0) | Counsel reading of the two MAK-J3 ⚑ flags | AU counsel | `Q-REG-009` / `ASSUME-REG-008` (R30); DEC-06 |
| `RG-03` (v1.0) | Baseten Sydney dedicated terms in writing | Baseten | `ASSUME-REG-004` (R30); DEC-03 |
| `RG-04` (v1.0) | immudb BUSL redistribution terms | Legal | C-05 / DEC-04 (MET-2) |
| `RG-05` (v1.0) | Conformal-for-LLM literature watch | cdss-conformal owner | MAK-ELSM §05 watch; no register row — recommend a `WATCH-*` row on DEC-02 |
| `RG-06` (v1.0) | TGA AI-enabled-SaMD guidance read against the intended-purpose statement | Regulatory owner | `WATCH-REG-002` (R30); `TASK-REG-001` |
| `RG-07` **(new)** | Reconcile Primer H §H1's Lumos cohort figure ("6.8M+") with the indexed paper's 1.3M / 16% of NSW; locate or mark NOT-LOCATED the "2025 data-quality cohort study" | cdss-lumos owner / PROMPT-H run | Primer H annex erratum (append-only); `TASK-REG-015` evidence plan; H10 status |
| `RG-08` **(new)** | Primary-care differential-diagnosis conformal-prediction evidence: none located 2026-09-02; the gap argues for Primer H Stage 3, not against Primer F | cdss-conformal owner | RG-05 watch; Primer F F10 evidence row; DEPLOY-2 §1 coverage acceptance |

Closure mechanism (the rule RESEARCH-1 v1.0 did not state): an RG closes when its
owner's action lands as a finding in a RESEARCH-1.n delta **and** the register or
decision row named in "Closes into" is updated by *that row's* owner. RESEARCH-1 never
closes a DEC, ASSUME or WATCH itself.

## Census and self-audit (run 2026-09-05)

- Census: RG-01..RG-08 = 8 = `req_count` (6 carried from v1.0 + 2 new). No ID retired or reused.
- Every quoted figure appears verbatim in its named source file (grep: "1.3M patients / 16% of NSW", "6.8M+", "s41598-026-35343-6", "ihj-2021-000074") — PASS.
- Every "Closes into" target resolves in the tree (DEC-03/04/06/12, G-08, C-05, Q-REG-009, ASSUME-REG-004/008, WATCH-REG-002, TASK-REG-001/015, MAK-ELSM §05, H10) — PASS.
- No literature re-fetched; no clinical number asserted by this delta — PASS.
- RESEARCH-1 v1.0 byte-identical — PASS (CHECKSUMS_BEFORE/AFTER).
