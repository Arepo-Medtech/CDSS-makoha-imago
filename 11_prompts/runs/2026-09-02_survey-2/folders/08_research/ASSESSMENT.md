# 08_research — ASSESSMENT (Phase 2)

Census: 1 file, 3,129 B. Read in full.

## 1. Discovery and labels
| Item | Bytes | Label | Why | Load-bearing? |
|---|---|---|---|---|
| `RESEARCH-1_findings_gaps_source_map.md` | 3,129 | RESEARCH | "supplied vs newly-found vs proposed sources"; mints RG-01..06 | crit 1 (folder) — cited by MET-1.1, MET-3, MET-4 (G-08/G-11 evidence), HARDEN-1 row 0 |

## 2. Presence pass — folder chain
| Link | Applicability | PRESENT / ABSENT | Evidence |
|---|---|---|---|
| P-F-01 BRIEFING | APPLIES as a paragraph inside the index (one-file folder) | ABSENT | `find 08_research -iname '*brief*' -o -iname '*index*'` → none |
| P-F-02 INDEX | APPLIES (one row) | ABSENT | same |
| P-F-03 corpus-grade | APPLIES | §3–4 | — |
| P-F-04 PRIMER | DOES-NOT-APPLY | — | — |
| P-F-05 LAUNCH PROMPT | DOES-NOT-APPLY (RG-01..06 are HUMAN/EXTERNAL: DEC-12 executor, counsel, Baseten, Legal, owners) | — | RESEARCH-1 §3 "Who" column |
| P-F-06 ARTIFACT-HTML | DOES-NOT-APPLY | — | — |
| P-F-07 SKELETON home | DOES-NOT-APPLY | — | — |
| P-F-08 HARDEN rows/tasks | APPLIES | PARTIAL — row 60–71 "08_ (1)" collapsed; T-100..107 collapsed | HARDEN-1 l.29 |
| P-F-09 00_MANIFEST row | APPLIES | PRESENT (1 = 1) | CENSUS §1 |
| P-F-10 honesty | APPLIES | PARTIAL — §1 "not re-verified this pass unless noted", §3 "no findings fabricated" — honest in text; **no `status` field** | frontmatter keys: doc_id, title, version, date |

## 3–4. Document contract + measurement (RESEARCH-1)
| Line | Result | Evidence |
|---|---|---|
| P-D-01 core frontmatter | **status ABSENT** (4/5) | keys: doc_id, title, version, date |
| P-D-02 honest status | PARTIAL (in text, not in field) | §1, §3 headers |
| P-D-04 req declaration | **ABSENT** — mints RG-01..06 (6) | §3 table |
| P-D-05 sourced rows | PASS — §2 rows: Source · Finding · Feeds (with fetch date "1 Sep 2026"); §3 rows: Gap · What's needed · Who | tables |
| P-D-07 traceability | PASS (fetch dates; feeds column) | §2 |
| P-D-08 census | ABSENT | — |
| P-D-09 self-audit | ABSENT | — |
| P-D-10 owner + status per row | PARTIAL — RG rows have Who ✓; status only in the section header "(open)" | §3 |
| P-D-12 placeholders | none | — |
| P-D-14 owner | PARTIAL — "DEC-12 executor", "Regulatory owner", "cdss-conformal owner" (roles; persons [NEEDS DEFINITION] via DEC-09/10/12/G-09) | §3 |
| P-D-16 xrefs | PASS (RG, SRC-REG-001..004, ASSUME-REG-004, C-05, C-10, C-11/C-12, DEC-11/12, G-08, H10, WATCH-REG-002 all resolve — CENSUS §3 no dangling) | census |
| RESEARCH floor: supplied vs newly-verified vs gaps vs proposed; fetch dates; no fabricated findings | PASS (four sections exactly; dates "1 Sep 2026"; §3 "no findings fabricated") | headings §1–§4 |
| sibling consistency | PASS — §2 "25 skills total" ↔ MT2 "24" is registered as C-11 ✓; §2 HeyDoc facts ↔ MET-1 §4.1 ✓ | MET-2 C-11 |
| currency against the tree (2026-09-02) | **STALE** — findings surfaced after 2026-09-01 are registered only in 11_: PROMPT-SERIES evidence pack (i) Lumos indexed paper reports 1.3M patients / 16% of NSW vs Primer H1 "6.8M+"; the "2025 data-quality cohort study" NOT-LOCATED in PubMed; (ii) conformal-for-LLM literature (RG-05 watch) has a 2026 hit; R30.1 adds SRC-REG-011..014 (012 secondary, "caution carried") — none appears in RESEARCH-1; no RG for the Lumos cohort discrepancy exists in MET-2/MET-4/R30 either | PROMPT-SERIES_A-L_index.md "Evidence pack" §; R30.1 l.20 |

## 5. Chain confirmation
CHAIN.md 08_ confirmed (P-F-04/05/06/07 DOES-NOT-APPLY).

## 6. Weighting summary
Queue (≥3): BSQ-0501 INDEX-08 (carries briefing + status). Below threshold, recommended: BSQ-0502 RESEARCH-1.1 delta (RG-07 Lumos figure; RG-08 conformal-LLM hit; SRC-REG-011..014; status field) weight 2; BSQ-0503 DEC-12 decision weight 2. PRESENT row BSQ-0500.

## 7. Validation
rows=4 invalid=0 valid=4
