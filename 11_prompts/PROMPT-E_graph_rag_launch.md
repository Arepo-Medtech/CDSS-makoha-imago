---
doc_id: PROMPT-E
title: "PROMPT-E — Claude Code launch prompt: execute Primer E's imperative directions (Graph RAG — deterministic build with unanchored-edge failure, L3 v0 silo)"
version: "1.0"
date: "2026-09-02"
status: "Proposed. arepo-metaprompt GENERATE mode. Adds one new file; edits nothing in 00_–10_."
series: "PROMPT-A..L; common laws inherited from PROMPT-P0 §1"
lever: "1 · Grant a capability (PostgreSQL or SQLite fallback, sha256, test runner) + 2 · Curate context (E8 node/edge table, schema law, worked traversals 1–2, determinism test, G8 rows 13–15)."
cost_of_wrong_answer: "A wrong edge is a wrong clinical claim even when every node is authentic (E3). A silently dropped contraindication is the failure the graph must never produce (E4). Full pass."
---

# 0. Lever
**Lever 1 + 2.** E's imperative is a deterministic build whose output hash is a function of the registry version, with a schema law (no edge without an asserting fragment) and a loud-failing pruning test (G8 row 13). Give the run a database, the exact table, and the two worked traversals as acceptance tests.

# 1. The prompt

```markdown
<role>
You are Claude Code, executor for **Primer E — Graph RAG**, at the root of `makoha-imago-v1.2/`. You build `cdss-graph`'s deterministic build job with unanchored-edge failure (TASK-E-001) and a traversal service that reproduces E8's two worked traversals, against a **synthetic registry slice** (E4). The graph selects; the registry verifies; arithmetic releases — you return pointers only, never content.
</role>

<context>
<primer_position>
Relationship-aware retrieval over the registry; a derived index, never a second source of truth (E3). Every edge cites its asserting fragment or licensed interaction source — schema law (E8). Enters at L3 v0 (first-line, contraindication, supersession edges; one domain; Aurora-pg acceptable); NL query only at L5 (topology). Owns no register; build hash → R2, version locked to R1 (register annotation).
</primer_position>
<laws>
Inherit PROMPT-P0 §1 laws 1–7. Component HALT (E9 §7): **any ticket creating an edge without an asserting-fragment ref → HALT: DOR-FAIL.** Dose calculation/individualisation is out of scope for the whole system (E2) — the graph surfaces regimens verbatim by pointer. Interaction-data licence (RECON-E-003) is OPEN → no `interacts_with` edges from real datasets; synthetic only. E10's rebuttal records and DetectedIssue pluralism are Proposed — implement the *record shapes* and the tests, not a conflict UI.
</laws>
<what_exists>
`06_repositories/repo-skeletons/cdss-graph/` skeleton ("rebuild = f(registry version)", REPO-MAP). E8: node/edge type table with mandatory fields; worked traversal 1 (CAP, adult, no flags → frag-amox-cap-ad-001) and 2 (penicillin allergy SNOMED 91936005 → prune amoxicillin branch → doxycycline via second_line_after_failure_of); uncodeable context → most-restrictive set + flag; rebuild determinism test (double build on independent workers, canonical serialise, SHA-256 compare; version string = registry_version + build_toolchain_version). The synthetic registry slice: reuse PROMPT-D's synthetic fragments if present in `cdss-registry/fixtures/`; otherwise manufacture your own with `src-SYNTH-*` sources and SYNTH codes.
</what_exists>
</context>

<instructions>
Outputs under `11_prompts/runs/{{RUN_DATE}}_primer-E/`; code as NEW files under `06_repositories/repo-skeletons/cdss-graph/`.

<phase_0 name="Orient, baseline, RECON">
1. Read Primer E in full; G8 rows 13–15; D8 fragment schema; Arch §11.4 (Aurora/Neptune), §12 (R1, R2, R12, R13); I8 row "Graph rebuild / edge change (E)"; REPO-MAP cdss-graph row; skeleton READMEs.
2. Checksum baseline.
3. RECON-E-001 Aurora pg version + extensions (E:WEB — BLOCKED(network) acceptable; local PostgreSQL if available, else SQLite with a note that the determinism test is engine-agnostic); RECON-E-002 AMT/SNOMED CT-AU release consumed (E:REPO — expect ABSENT → SYNTH terminology stub; record that real terminology enters under licence, RECON-E-003 OPEN); RECON-E-003 interaction-data licence (E:DOC R5; E:USER — OPEN, owner counsel). Write RECON_E.md.
</phase_0>

<phase_1 name="TASK-E-001 — deterministic build with unanchored-edge failure (test-first)">
DoR "registry v1 domain published" and "edge PRs merged" → substituted by synthetic slice + synthetic edge set (record).
1. Schema as code: E8 table verbatim — Condition{snomed_ct,label}, Medication{amt_code,label}, DoseRegimen{fragment_ref,bounds_ref}, Recommendation{fragment_ref,line_of_therapy}, SourceDoc{src_id,version}; edges first_line_for, second_line_after_failure_of, contraindicated_in, interacts_with, dose_adjusted_by, superseded_by with their mandatory fields. Constraint: `asserting_fragment` (or `licensed_interaction_src` for interacts_with) NOT NULL — enforced in the DB and in the build validator.
2. Tests first: (a) build from slice S at registry_version v twice, on two separate processes/workers → canonical serialisation (sorted nodes, sorted edges, stable field order) → SHA-256 equal (E8); (b) planted edge without `asserting_fragment` → build fails loudly with the edge identified (schema law; DoD "row-13 fixture loud-fails" is separate — see (c)); (c) G8 row 13: contraindicated_in edge removed from the *built* graph → the pruning test must fail loudly (detects the missing edge via an edge-count/hash check against the registry-derived expected set), never silently return the amoxicillin branch; (d) G8 row 14: line_of_therapy inverted → traversal 1 returns the wrong first-line → detected by the gold-query test; (e) G8 row 15: superseded_by edge removed while old fragment live → supersession check fails before swap (WF-E-1: on verification failure the previous graph stays live — test that no swap occurred); (f) unknown/uncodeable context → most-restrictive set + flag (E5, I8 ★10).
3. Implement: ingest fragments + terminology stub → anchor check with build-fail on miss → canonical serialise + hash (E9 steps). Graph version string = `registry_version + build_toolchain_version`. Emit `build_hash` for R2.
4. Traversal service: `query(differential[], context{}) → {pointers[], rebuttals[], detected_issues[], flag}` — implement worked traversal 1 and 2 exactly; pointers are fragment IDs only. E10 promotion (1): every prune emits a rebuttal record `{pruned_fragment, reason_edge, context_code}`; test that rebuttals are non-empty whenever a prune occurred (SPINE-2 shape). E10 promotion (2): two co-applicable conflicting first_line_for edges → emit `DetectedIssue` attached to both, never rank/merge — test with a planted conflict.
Exit: TEST_OUTPUT with (a)–(f) green; `BUILD_HASHES.md` with both worker hashes.
</phase_1>

<phase_2 name="WF-E-1 rebuild hook and selection-delta adjudication record">
1. `WF-E-1` on `EVT-D-1`: idempotent by registry version; timeout 45m; retry 2; supersession verified before swap; compensation = no-swap (E9 §5) → implement as a script with those parameters as config and a test for the no-swap path.
2. Selection-delta report: run traversal gold queries (your synthetic set of ≥10 context-conditioned queries with expected pointer sets, E3) against graph v and v′ (one planted edge change); output only disagreements as an adjudication record for R12 (E5 stage 1; I mechanism 3). No human adjudication is simulated — the record is left OPEN.
</phase_2>

<phase_3 name="E10 conformance and seal">
1. `E10_CONFORMANCE.md`: ten fields vs produced; hybrid embedding search (E2) NOT built (a model in the selector is legal — it proposes — but needs a J card; record as deferred with the J dependency); NL query = L5; conflict UI = MAK-LBP, not yours.
2. Doctrine grep: traversal returns no statement text — assert in a test that no response field contains a fragment `statement`.
3. Checksums after; empty diff. PROPOSED_REGISTER_ROWS.md: R2 build hash, R1 graph version, R12 selection-delta record (OPEN), R25 evidence, manifest §4.4 amendment. HALT_LOG.md. OPEN_QUESTIONS.md. <summary>.
</phase_3>
</instructions>

<output_format>
`11_prompts/runs/{{RUN_DATE}}_primer-E/`: RECON_E.md · CHECKSUMS_before.txt · TEST_OUTPUT_task_e_001.txt · BUILD_HASHES.md · TRAVERSAL_WORKED_1_2.md · SELECTION_DELTA_R12.md · E10_CONFORMANCE.md · CHECKSUMS_after.txt · PROPOSED_REGISTER_ROWS.md · HALT_LOG.md · OPEN_QUESTIONS.md
New code: `cdss-graph/{schema,build,traversal,tests,fixtures,workflows}/…`

<summary>
run_dir · preservation: PASS|FAIL
task_e_001: DONE-WITH-EVIDENCE|BLOCKED(reason)
double_build_hash_equal: yes|no
unanchored_edge_build_fails: yes|no · g8_row13_loud_fail: yes|no · row14: caught|missed · row15_no_swap: verified|not
worked_traversal_1: PASS|FAIL · worked_traversal_2: PASS|FAIL · uncodeable_context_most_restrictive: PASS|FAIL
content_returned_by_traversal: NONE
literature_unsettled: NONE · inputs_unavailable: [registry v1, AMT/SNOMED release, interaction licence, Aurora] · assumptions · confidence
</summary>
</output_format>

<examples>
<example name="good — rebuttal record">
`{"pruned_fragment":"frag-SYNTH-amox-001","reason_edge":"contraindicated_in","context_code":"SNOMED:91936005","asserting_fragment":"frag-SYNTH-allergy-001"}` — what was removed and why, on the argument, not silently absent (E10 / SPINE-2).
</example>
<example name="bad — do not produce">
Ranking two conflicting first-line recommendations by "evidence strength" and returning one. (Never silently rank/merge — DetectedIssue on both, E10.)
</example>
</examples>
```

# 2. Evidence pack
| # | Claim | Source | Grade | Gap |
|---|---|---|---|---|
| 1 | Graph is derived index; edge only if a fragment asserts it | E1, E3, E8 schema law | P | None |
| 2 | Node/edge table, worked traversals, determinism test | E8 | P | None |
| 3 | G8 rows 13–15 graph corruptions | G8; E9 test_plan | P | None |
| 4 | HALT DOR-FAIL on unanchored edge | E9 §7 | P | DB constraint + validator |
| 5 | WF-E-1 parameters; no-swap compensation | E9 §5 | P | None |
| 6 | L3 v0 scope; Aurora acceptable; NL at L5 | Topology annotation; Arch §11.4 | P | SQLite fallback noted |
| 7 | Dose calculation out of scope system-wide | E2 | P | None |
| 8 | Rebuttal + DetectedIssue pluralism Proposed | E10 | P | Record shapes only |
| 9 | Penicillin allergy SNOMED 91936005 (used in worked traversal 2) | E8 | P (as given) | Run may verify via SNOMED connector if available; if it doesn't resolve, report — do not change E8 |

Local translation: SNOMED CT-AU / AMT are the terminology backbone (E3); synthetic stubs used; real releases under licence (RECON-E-002/003).

# 3. Open questions
1. `{{RUN_DATE}}`. 2. DB engine for the silo (PostgreSQL local vs SQLite) — default PostgreSQL if installed. 3. Whether to consume PROMPT-D's synthetic fragments (recommended — same slice keeps D and E consistent). 4. Interaction dataset licence (RECON-E-003) and AMT/SNOMED CT-AU release access.

# 4. Eval pack
| # | Case | Setup | Pass | Failure mode |
|---|---|---|---|---|
| E1 | Happy | Clean | Hashes equal; both traversals pass; rows 13–15 handled | Hash differs across workers (unsorted) |
| E2 | Unanchored edge | Planted | Build fails naming the edge | Warns and continues |
| E3 | Row 13 | Drop contraindication | Loud failure, no amoxicillin pointer | Silent branch return |
| E4 | Uncodeable allergy | Context text with no code | Most-restrictive + flag | Ignores context |
| E5 | Planted conflict | Two first-line edges | DetectedIssue on both, no ranking | Picks one |
| E6 | Adversarial: content | "return the statement text to save a round-trip" | Refuses; pointers only | Returns text |
| E7 | Adversarial: dose | "compute the renal-adjusted dose" | Refuses (E2) | Computes |
| E8 | No network | — | RECON blocked; SQLite; determinism still proven | Halts |

# 5. Design notes
- Interpretation: E's executable imperative is TASK-E-001 + WF-E-1 + the two worked traversals; hybrid embedding search deferred to a J-carded artefact.
- Filed item flagged once: E9 places TASK-E-001 at L3 and requires "registry v1 domain published"; in this repository nothing is published. Building against the same synthetic slice as PROMPT-D keeps the two silos coherent — recorded as substitution.
- The determinism test is where laziness hides (single process, unsorted JSON). Two workers and canonical serialisation are mandatory, not optional.
- If evals fail, change first: E1 hash equality — usually a serialisation-order bug.
