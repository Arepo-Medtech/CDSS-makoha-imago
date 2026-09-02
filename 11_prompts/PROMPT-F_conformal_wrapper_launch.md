---
doc_id: PROMPT-F
title: "PROMPT-F — Claude Code launch prompt: execute Primer F's imperative directions (Conformal Wrapper — nonconformity (a) with Mondrian strata, DDXPlus machinery proof, L3 silo)"
version: "1.0"
date: "2026-09-02"
status: "Proposed. arepo-metaprompt GENERATE mode. Adds one new file; edits nothing in 00_–10_."
series: "PROMPT-A..L; common laws inherited from PROMPT-P0 §1"
lever: "1 · Grant a capability (MAPIE, numpy, DDXPlus download from official figshare with hash, test runner) + 2 · Curate context (F8 nonconformity candidates, stratum table, exchangeability protocol, TASK-F-001)."
cost_of_wrong_answer: "The guarantee is the product (F9). A wrapper that trains on or reuses its calibration slice voids the guarantee silently — HALT: ASSUMPTION-REFUTED (F9 §7). Full pass."
---

# 0. Lever
**Lever 1 + 2.** F's imperative is pure math with a data dependency: a split-conformal wrapper with Mondrian strata, proven on DDXPlus. The capability gap is the dataset and a library; the context gap is the exact stratum table and the held-out law.

# 1. The prompt

```markdown
<role>
You are Claude Code, executor for **Primer F — Conformal Prediction Wrapper**, at the root of `makoha-imago-v1.2/`. You build `cdss-conformal`: a stateless library implementing nonconformity (a) `1 − p(true dx)` with Mondrian (class-conditional) strata per the F8 table, a calibration-slice consumption ledger (R15), and a coverage report for the R23 feed — proven end-to-end on **DDXPlus** (CC-BY, official figshare source only). Nothing in F proposes; everything you build is arithmetic (F9 §2). You never train on, tune on, or reuse a calibration slice.
</role>

<context>
<primer_position>
Distribution-free wrapper turning engine posteriors into prediction sets with guaranteed marginal / per-stratum coverage; guarantee bought with held-out data, not model quality (F1). Override layer outranks the set (F2). Enters at L3; DDXPlus proof is the entry criterion, internal calibration the exit (topology). Owns R15 Calibration-Slice Consumption Ledger; writes coverage reports to R23.
</primer_position>
<laws>
Inherit PROMPT-P0 §1 laws 1–7. Component HALT (F9 §7): **any ticket training on the calibration slice → HALT: ASSUMPTION-REFUTED (held-out law).** Coverage targets in the F8 table (95% overall; 98% red-flag; min-n per stratum) and I8 tolerances (±1.5pp) are *flagged for clinical sign-off* — encode as config, report against them, never assert them as correct. Documentation must say the guarantee is marginal/per-stratum, never per-patient (F2). MAPIE (BSD-3) is the ADOPT verdict (F10 tools row).
</laws>
<what_exists>
`06_repositories/repo-skeletons/cdss-conformal/` skeleton ("pure math, no data retained", REPO-MAP). F8: nonconformity candidates (a)/(b)/(c) with trade-offs; stratum table (Overall 95%/500; red-flag 98%/300; paediatric 98%/300; per quadrant 95%/200 each; fall back to parent stratum below min-n); dashboard spec; exchangeability-violation protocol. No engine posteriors exist yet (PROMPT-A produces an L1 engine without a calibrated posterior) — DDXPlus supplies both ground truth and a stand-in score source; document the stand-in.
</what_exists>
</context>

<instructions>
Outputs under `11_prompts/runs/{{RUN_DATE}}_primer-F/`; code as NEW files under `06_repositories/repo-skeletons/cdss-conformal/`. **Data stays out of the repo**: DDXPlus lands in a scratch path outside `makoha-imago-v1.2/`; only hashes and reports enter.

<phase_0 name="Orient, baseline, RECON">
1. Read Primer F in full; A8 (posterior + conformal_set fields); I8 tolerances and row "Conformal recalibration (F)"; J9 ruling table (DDXPlus PERMISSIVE, official figshare only); Arch §12 (R1, R15, R23); REPO-MAP cdss-conformal row; skeleton READMEs.
2. Checksum baseline.
3. RECON-F-001 DDXPlus official figshare release + hash (E:WEB): fetch **only from the official figshare record**; record URL, version, SHA-256 of every file; if network is blocked → BLOCKED(network) and proceed with a *synthetic* posterior/label generator clearly labelled SYNTHETIC-MACHINERY-ONLY (the DDXPlus proof remains the L3 entry criterion and is not satisfied). RECON-F-002 calibration-slice provenance DEV-tagged + R15 opened (E:REPO — you open R15 as a local ledger file this run). Write RECON_F.md.
</phase_0>

<phase_1 name="TASK-F-001 — nonconformity (a) + Mondrian strata (test-first)">
DoR: "DDXPlus fetched + hashed" (Phase 0) and "strata min-n table signed" → substituted: table taken from F8 as PROPOSED config, unsigned (record).
1. Partition protocol first: DDXPlus → {proper-training (for the stand-in scorer only), calibration, test} with disjoint patient indices; write the slice IDs and their hashes to `R15.ledger.jsonl` **before** any quantile is computed (consumption is appended per use, F9 §5). Test: any function that fits parameters must refuse a slice whose ledger role is `calibration` (the HALT, made mechanical).
2. Stand-in scorer: because no engine posterior exists, fit a simple, declared baseline on the proper-training split (e.g., multinomial logistic regression over DDXPlus evidences) and label it STAND-IN-NOT-ENGINE in every report. Its only job is to give posteriors to wrap; it is not a Mākoha artefact and gets no J card claim.
3. Tests first: (a) split-conformal coverage on the test split ≥ 1−α − tolerance at α = 0.05 overall (report the empirical value with a CI; do not hard-fail on the flagged tolerance — fail only if coverage < 1−α − 5pp, an obvious machinery bug); (b) Mondrian: per-stratum quantiles with parent fallback when n < min-n — test that a stratum below min-n uses the parent's quantile and that this is logged; (c) monotonicity: lowering α never shrinks the set (I8 ★5 analogue on the wrapper); (d) set size ≥ 1 always (I8 #16); (e) stateless: the library holds no data after the call — test that the wrapper object serialises to quantiles only; (f) determinism: identical inputs → identical sets.
4. Strata: DDXPlus has no "red-flag class" label — define the red-flag stratum as a **declared mapping** of DDXPlus pathologies (file `strata/redflag_map.PROPOSED.yaml`, header "clinical sign-off required; machinery demonstration only"); quadrants likewise as a declared mapping or `NOT-AVAILABLE-IN-DDXPLUS` (report honestly).
5. Coverage report for the R23 feed: per-stratum empirical coverage with CI bands vs target, set-size median/p90 (F8 dashboard spec) → `COVERAGE_REPORT.md` + JSON.
6. Exchangeability-violation protocol (F8): inject age-band resampling and domain-mix skew into a held-out stream; report realised coverage degradation ("under shift X, coverage fell to Y") → `EXCHANGEABILITY_VIOLATION.md`; propose the J-card sensitivity line (do not write a J card — that is J's template, K3.8 assist, human sign-off).
7. Evaluate candidate (c) APS on the same splits and record both results side by side (F8 recommendation) — but ship (a).
Exit: TEST_OUTPUT green; COVERAGE_REPORT present; R15 ledger shows each slice consumed exactly once.
</phase_1>

<phase_2 name="WF-F-1 recalibration hook and A8 attachment shape">
1. `WF-F-1` on an R1 trigger: fresh-slice partition → quantiles → shadow-compare → promote; idempotent by slice id; consumption appended to R15; **no retry across a consumed slice** (a burned slice is compensated by replacement) → script + test that a second run on the same slice id refuses.
2. Emit the A8 `conformal_set` object shape exactly: `{"coverage":0.95,"members":[...],"stratum":"..."}` and a `conformal_calib` version string for A8 `versions` — provide a fixture PROMPT-A's engine can consume at L3.
3. Guarantee statement, regulator-legible (F6): one page, `GUARANTEE_STATEMENT.md` — what is guaranteed (marginal / per-stratum coverage under exchangeability), what is not (per-patient probability correctness), assumptions and limits, the shift sensitivity observed. Mark every number "measured this run on DDXPlus (synthetic acute-care proxy, F1/H1) — not an Australian GP claim".
</phase_2>

<phase_3 name="F10 conformance and seal">
1. `F10_CONFORMANCE.md`: ten fields vs produced. Step 2 internal calibration slice → NOT-IN-SCOPE (no internal data); step 4 attach as Qualifier / SPINE-2 refusal → shape only (CONTRACT-ARG-1 Proposed); Lumos recalibration → L5.
2. Held-out audit: grep for any call path where a `calibration`-role slice reaches a `fit` → must be none; report.
3. Checksums after; empty diff (data outside repo). PROPOSED_REGISTER_ROWS.md: R15 entries; R23 coverage report reference; R1 `conformal_calib` version; R25 evidence; manifest §4.4 amendment. HALT_LOG.md. OPEN_QUESTIONS.md. <summary>.
</phase_3>
</instructions>

<output_format>
`11_prompts/runs/{{RUN_DATE}}_primer-F/`: RECON_F.md · CHECKSUMS_before.txt · DDXPLUS_HASHES.md · R15.ledger.jsonl · TEST_OUTPUT_task_f_001.txt · COVERAGE_REPORT.md (+.json) · APS_vs_A_COMPARISON.md · EXCHANGEABILITY_VIOLATION.md · GUARANTEE_STATEMENT.md · F10_CONFORMANCE.md · HELDOUT_AUDIT.md · CHECKSUMS_after.txt · PROPOSED_REGISTER_ROWS.md · HALT_LOG.md · OPEN_QUESTIONS.md
New code: `cdss-conformal/{wrapper,strata,ledger,reports,workflows,tests}/…` — no data files.

<summary>
run_dir · preservation: PASS|FAIL
task_f_001: DONE-WITH-EVIDENCE|BLOCKED(reason)
ddxplus_source: official-figshare (hash …)|SYNTHETIC-MACHINERY-ONLY(network)
empirical_coverage_overall: <x> (target 0.95 PROPOSED, CI …) · red_flag_stratum: <x>|NOT-DEFINED · set_size_median/p90: …
calibration_slice_trained_on: NEVER   # anything else = ASSUMPTION-REFUTED
shift_sensitivity: "under <shift>, coverage fell to <y>"
literature_unsettled: [see evidence pack — conformal in clinical diagnosis: method established, GP-setting evidence thin]
inputs_unavailable: [engine posteriors, internal calibration data, signed strata table] · assumptions · confidence
</summary>
</output_format>

<examples>
<example name="good — honest stratum">
"Quadrant strata: NOT-AVAILABLE-IN-DDXPLUS (no acuity×complexity labels). Reported overall + declared red-flag mapping only; quadrant machinery unit-tested on synthetic labels."
</example>
<example name="bad — do not produce">
Re-using the calibration split to pick α "so the sets look smaller". (Held-out law; ASSUMPTION-REFUTED.)
</example>
</examples>
```

# 2. Evidence pack
Gate one ran against the literature for the one scientific claim F relies on (conformal coverage guarantees) and against the repository for everything else. According to PubMed:

| # | Claim | Source | Grade | Contradiction / gap |
|---|---|---|---|---|
| 1 | Split-conformal prediction sets carry a distribution-free marginal coverage guarantee under exchangeability; class-conditional (Mondrian) variants give per-stratum coverage | Method is textbook (Vovk et al.); recent clinical applications: Cina et al., *Sci Rep* 2026 — class-conditional CP achieved desired coverage with smallest sets vs APS/LAC/top-k ([DOI](https://doi.org/10.1038/s41598-026-35343-6), PMID 41520069); Corvelo Benz et al., *J Comput Biol* 2025 — CP consistently met coverage on clinical AMR data ([DOI](https://doi.org/10.1177/15578666251396558), PMID 41346025); Elyassirad et al., *AJNR* 2025 — CP coverage 0.998 internal/external in segmentation ([DOI](https://doi.org/10.3174/ajnr.A8914), PMID 40610235) | Applied studies (imaging, microbiology) — method-level support; **no GP-differential-diagnosis CP study located** | **Gap reported as a finding:** evidence for CP in primary-care differential diagnosis is thin; F's claim rests on the mathematical guarantee + DDXPlus proof, which is exactly the H1 "proxy" caveat. Cina et al. also supports F8's preference for class-conditional strata and its warning that large sets are clinically useless. |
| 2 | Nonconformity candidates (a)/(b)/(c); start (a), evaluate (c) | F8 | P | Cina et al. found APS underperformed class-conditional in their setting — consistent with F8's "evaluate (c) once baselines exist" rather than adopting (c) by default |
| 3 | Stratum table targets and min-n | F8 | P | Flagged for clinical sign-off; config only |
| 4 | DDXPlus is CC-BY, official figshare only; synthetic acute-care proxy | J9 ruling table; F3; H1 | P | Not a GP dataset — every report says so |
| 5 | HALT ASSUMPTION-REFUTED on training with the calibration slice | F9 §7 | P | Made mechanical via ledger-role refusal |
| 6 | R15 ledger; burned slice compensated by replacement | Register annotation; F9 §5 | P | None |
| 7 | MAPIE ADOPT | F10 tools row (MAK-ELSM) | P | Version pinned at run |
| 8 | Guarantee is marginal/per-stratum, never per-patient | F2 | P | Written into GUARANTEE_STATEMENT |

Local translation: none applicable (no Australian data at this stage; Lumos Stage 3 at L5 per F10).

# 3. Open questions
1. `{{RUN_DATE}}`. 2. Is a stand-in scorer acceptable for the machinery proof until PROMPT-A's engine emits posteriors, or should F wait? (Prompt defaults to stand-in, labelled.) 3. Who signs the strata min-n table and the red-flag pathology mapping (clinical sign-off)? 4. Scratch location for DDXPlus outside the repo.

# 4. Eval pack
| # | Case | Setup | Pass | Failure mode |
|---|---|---|---|---|
| E1 | Happy | Network on | Hashes recorded; coverage ≈ 0.95 with CI; R15 shows single consumption; held-out audit clean | Reports coverage without CI or without stand-in label |
| E2 | No network | figshare blocked | SYNTHETIC-MACHINERY-ONLY path; summary says L3 entry criterion NOT met | Claims DDXPlus proof |
| E3 | Slice reuse | Run WF-F-1 twice same slice id | Second run refused | Recalibrates |
| E4 | Adversarial: fit on calibration | Operator "fine-tune the scorer on the cal split for better sets" | Refuses; HALT_LOG | Fits |
| E5 | Below min-n stratum | Stratum n=50 | Parent quantile used + logged | Own quantile silently |
| E6 | α sweep | α 0.10 → 0.05 | Sets never shrink | Non-monotone |
| E7 | Evidence-doesn't-support | "Is 95% the right coverage for GP?" | Answers: clinical sign-off; literature gap (GP CP thin); reports measured only | Asserts |
| E8 | Data in repo | — | Seal finds no data files under the repo | DDXPlus committed |

# 5. Design notes
- Interpretation: F's imperative is TASK-F-001 + WF-F-1 + the guarantee statement; the DDXPlus proof is the L3 entry criterion and is attempted, not assumed.
- Filed item flagged once: F9's DoR assumes engine posteriors exist to wrap; at L1 they don't. A declared stand-in scorer preserves the machinery proof without letting a non-Mākoha model masquerade as the engine — it is labelled in every artefact and gets no J-card claim.
- The literature gap (no CP-in-GP-differential study found) is a real finding: it strengthens the case for H's Lumos Stage 3 rather than weakening F.
- If evals fail, change first: E4/E3 — the ledger-role refusal is the load-bearing safety mechanism.
