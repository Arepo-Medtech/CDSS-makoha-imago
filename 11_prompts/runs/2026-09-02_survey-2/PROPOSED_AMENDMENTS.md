# PROPOSED_AMENDMENTS — text for the manifest owner to append (this run appends nothing)

All three blocks follow the 00_MANIFEST §7/§8 amendment form and the §5 defect-log form. Dates are the day the owner appends them.

## A-003 (proposed) — 11_prompts/ indexed; 03_ additions indexed; survey run recorded

**What was added.** An eleventh directory, `11_prompts/` (29 files at 2026-09-02: PROMPT-P0, PROMPT-A..L (12), PROMPT-PRM-SERIES index + PROMPT-PRM0 + PROMPT-PRM-* (10), PROMPT-SERIES_A-L_index, PROMPT-SURVEY-1, PROMPT-SURVEY-2, plus the run directory `runs/2026-09-02_survey-2/`), and, under `03_makoha-butterfly-corpus/`, three additions not indexed by §1 or by the 03_ MANIFEST: `butterfly-primers/` (10 primers + RUN-REPORT.md), `butterfly-primer-programme_prompt_v1.0.md`, `corpus_artifacts_briefing.md`. Also `02_cdss-stack-augmented/primers_briefing.md` and the root file `AI Evaluator Architecture.md`. Nothing pre-existing was edited: all 223 files (excl. `.DS_Store`; excl. the run directory) verified checksum-identical at the survey's seal (`11_prompts/runs/2026-09-02_survey-2/CHECKSUMS_{BEFORE,AFTER}.txt`, diff ∅).

| Dir | Contents | Files | Disposition |
|---|---|---|---|
| 11_prompts | launch prompts (P0, A–L, PRM-series), series indexes, SURVEY-1/-2 prompts, `runs/` (survey-2 outputs) | 29 + run dir | Proposed (prompts); survey outputs are recommendations only |
| 03_ (additions) | butterfly-primers (11), programme prompt, corpus briefing | 13 | Proposed (primers, prompt); Added (briefing) — the 03_ MANIFEST precedence law still governs its fifteen volumes; these additions are *beside* them, unindexed by that MANIFEST |
| 02_ (addition) | primers_briefing.md | 1 | Added |
| ROOT | AI Evaluator Architecture.md | 1 | Unclassified — generic cloud-infrastructure checklist; superseded for this repository's purposes by PROMPT-SURVEY-1 (its status line says so) |

**Honesty lines (extending §8).** PROMPT-SURVEY-2 run 2026-09-02: 118 target files censused (04_–10_), 177 rows, 0 files edited; verdict BELOW-PARITY for all seven target folders; 42 queue items of which 27 Claude-Code-executable now and 10 human decisions; no ASSUME/DEC closed · counsel packets are *specified* (EXEC-1 EX-6; PROMPT-P0 Phase 2) and **not yet assembled** — see DEF-005 · the hardening pass remains unexecuted; HARDEN-1 has no rows for 10_ (7 files), R30.1, MET-2.1, 11_ or the 03_ additions; HARDEN-1.1/HARDEN-3.1 deltas are proposed (survey rows BSQ-0104/BSQ-0006).

## Post-delivery defect log — proposed rows (append to §5)

| # | Defect | Fix | Verification |
|---|---|---|---|
| DEF-003 (proposed, found 2026-09-02) | DEF-002's residual scan missed two files: `09_diagrams/register_topology_v2.mermaid` l.17 and its inlined block in `cdss_diagrams_v2.html` l.96 still read `MT2 §7.4` (item notation should be `§7(4)`); DEF-002's "residual-notation grep = NONE" was therefore incomplete | Successor sources (`register_topology_v3.mermaid`, `cdss_diagrams_v3.html`) per survey row BSQ-0002/0003 — v2 files preserved unedited | `tools/refcheck.py` (survey-2) unresolved_anchors → 2 (before); expected 0 after v3 lands; mermaid.parse on v3 |
| DEF-004 (proposed, found 2026-09-02) | §7 A-001 states "all skeleton files carry Proposed/skeleton banners"; 13 of 90 skeleton files carry no Proposed/skeleton/stub marker (list in `11_prompts/runs/2026-09-02_survey-2/folders/06_repositories/ASSESSMENT.md §4`) | INDEX-06 §4 carries the list until the trees instantiate (survey row BSQ-0390/0393); no skeleton file edited | `grep -L -i 'skeleton\|proposed\|stub\|pointer'` over `06_repositories/repo-skeletons/**` → 13 files |
| DEF-005 (proposed, found 2026-09-02) | §8 states "Counsel packets drafted, not sent"; no packet artifact exists in the tree — the packet is *specified* (EXEC-1 EX-6; PROMPT-P0 Phase 2 assembly spec) and not yet assembled | Either read "drafted" as "specified" here, or assemble via PROMPT-P0 Phase 2 (survey row BSQ-0702) and cite the run directory | `grep -rln -i 'counsel packet'` → spec files only; `ls 11_prompts/runs` |

## Register-name query (for the architecture owner; not a manifest row)
R25 is "Build Evidence & Assumptions Ledger" in Arch §12.2 l.369 and "property runs / property-run outputs" in Primer A A10 and IMAGO-3. Ruling requested (survey row BSQ-0602); on ruling, the losing side takes an annex note, never an in-place edit.

## Proposed DEC-23 (for MET-2.2, the founder's call)
"Name the infrastructure owner; set RTO/RPO targets; approve the L5 multi-region DR drill protocol" — closes G-09's RTO/RPO/DR component (DEPLOY-1 `[NEEDS DEFINITION]`; survey row BSQ-0405). Blocking: L5 exit; GATE-004.
