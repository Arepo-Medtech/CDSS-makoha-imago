---
doc_id: HARDEN-2.1
title: "HARDEN-2.1 — hardening SPEC delta: source per class bar, ID census (CC / AR / STL), self-audit"
version: "1.1-delta"
date: "2026-09-05"
status: "Proposed — a SPEC delta is itself an artifact of the pass (CC-8) and gets its own R29 row (HARDEN-1.1 row for this file); NOT hardening (law 6): it adds sources, ids and a self-audit to HARDEN-2 v1.0, which is preserved verbatim beside this file. Read HARDEN-2 through this file."
supersedes: "nothing — read HARDEN-2 through this file"
applies_to: "04_hardening/HARDEN-2_hardening_spec.md"
change_policy: "Additive delta per the MET-1.1 pattern"
req_prefix: CC
req_count: 8
also_mints: "AR-1..AR-4 (anti-rationalization rows, ids assigned here to HARDEN-2's four unnumbered rows); STL-1..STL-5 (the five portfolio stop-the-line rules HARDEN-2 cites from MET-1 §9.4 (a)–(e))"
---

# HARDEN-2.1 — SPEC census and self-audit delta

HARDEN-2 v1.0 mints CC-1..CC-8 and four anti-rationalization rows with no count
declaration, no ID census and no self-audit, and four of its eight class-bar rows carry
no source for their bar (survey-2 BSQ-0105; P-D-04/08/09). Under P-D-05 a table-form
rule satisfies the requirement-block contract only if each row carries an ID and a
source/rationale cell. This delta supplies the source column, ids for the unnumbered
rows, the census and the self-audit. It changes no bar.

## D-1 — source column for every class-bar row

| Class | Bar (HARDEN-2 v1.0, unchanged) | Source of the bar | Mechanical check tool named in HARDEN-2 — exists? |
|---|---|---|---|
| `CC-1` Primers + execution layers | ten execution fields present and non-empty; §-8 numbers flagged; §-9 untouched; annex additive | MT2 §1 (eight properties); 00_MANIFEST §4.2 ("ten required execution fields"); X1 append-only (00_MANIFEST §1) | `validate_build_plan.py` — **not in the tree** (00_MANIFEST §4.4 PENDING-VALIDATOR; lives in cdss-spine per Arch §13.8); link/ID resolution — `11_prompts/runs/2026-09-05_sprint-1/tools/refcheck.py` (survey-2 / sprint-1); git diff — yes |
| `CC-2` Architecture + registers | register laws §12.1 hold; opening levels; mutability; join key | Arch §12.1 (six register laws), §12.3 (per-level register checks) | schema validation — `jsonschema` (run-local venv); ID census — grep |
| `CC-3` Mākoha corpus volumes | cross-walk rows verified; consolidation retires nothing; RFC 2119 consistent; census = Appendix A | 03_ MANIFEST "Precedence in one paragraph"; MAK-FFC Appendix A (block grammar), B (census), C (self-audit checks) | census diff, anchor grep, link resolution — grep-based |
| `CC-4` Regulatory artifacts | every OPEN item names attesting party + blocked gate; no ASSUME closable internally; WATCH cadences present | REG-POSTURE §0.4 status vocabulary, §0.5 validator conventions, §8 ("No ASSUME-REG-* may be closed by internal reasoning"), §10; MAK-ANT annex §8 | R30 schema validation — `05_/REG-R30.schema.json` + `REG-R30.3_row-form_seed.jsonl` (sprint-1); `10_/validate_reg.py` (A-003) |
| `CC-5` Workflows / orchestration | every step carries timeout/retry/idempotency/on-fail; events name producer/consumers/delivery/dedup | Arch §13.6 orchestration hooks (WF-SPINE-1/2, EVT-SPINE-1 field pattern) | YAML lint — `python -c "import yaml"` (venv); field-presence — `11_prompts/runs/2026-09-05_sprint-1/tools/proc_fields.py` (sprint-1) |
| `CC-6` Browser-borne | renders without console errors; mermaid sources parse; links resolve; accessibility checklist | MT2 §2.2 VERIFY row (`browser-testing-with-devtools`); 00_MANIFEST §5 DEF-001 (mermaid.parse method) | `browser-testing-with-devtools`, `/webperf` — agent-skills pack (external; row zero installs); headless mermaid.parse — `11_prompts/runs/2026-09-05_sprint-1/tools/mermaid/parse.mjs` (sprint-1, mermaid 10.9.8) |
| `CC-7` Contracts / schemas | JSON Schema valid; example instances validate; breaking-change note per Arch §10 | Arch §10 ("A contract change is a spine PR that visibly breaks consumers in CI"); Arch §14.2 (new shared contracts) | `jsonschema` validation runs — `11_prompts/runs/2026-09-05_sprint-1/tools/validate_examples.py` (sprint-1) |
| `CC-8` Directive + SPEC + HARDEN-3 + MET set | the pass's own artifacts clear the same bar; C-11 reconciliation recorded | MT2 §7(5) ("If you cannot name the ratchet, the pass did not happen"); MET-2 C-11; DEC-11 | as CC-1/CC-2 |

Universal exit bar source (HARDEN-2 "Universal exit bar (every class)"): MT2 §1 items 1–8
verbatim + `references/definition-of-done.md` (agent-skills pack — external path; resolves
only after row zero installs the pack, MT2 §2.1).

## D-2 — ID census

| Family | IDs | Count | Where defined |
|---|---|---|---|
| `CC` | CC-1, CC-2, CC-3, CC-4, CC-5, CC-6, CC-7, CC-8 | **8** = `req_count` | HARDEN-2 "Class bars" table (8 rows, first cell) |
| `AR` (minted here for HARDEN-2's four unnumbered anti-rationalization rows, in table order) | AR-1 "The 15 Mākoha volumes were just written; they're clean." · AR-2 "The annexes were authored together; harden one, batch the rest." · AR-3 "Corpus files can't be opened from dev, so mark them HARDENED by proxy." · AR-4 "The relabel is obviously right; apply it now everywhere." | **4** | HARDEN-2 "Anti-rationalization coverage" table (4 rows) — MT2 §4's thirteen generic rows keep their MT2 home and are not re-minted |
| `STL` (minted here for the five portfolio rules HARDEN-2 cites) | STL-1 corpus-credential grant · STL-2 gate/evaluator bypass · STL-3 μ-as-confidence render · STL-4 GPP boundary extension · STL-5 internal ASSUME-REG closure | **5** | MET-1 §9.4 (a)–(e), quoted by HARDEN-2 "Stop-the-line (instantiated)"; MT2 §6 generic rules keep their MT2 home |

Consumers of CC-1..8 checked both ends: `05_/REG-R29.schema.json` `artifact_class` enum
(CC-1..CC-8 + engine/corpus/external) ✓; HARDEN-1 / HARDEN-1.1 class column ✓; HARDEN-3.1
class column ✓; survey-2 CLASS_CONTRACTS ✓.

## D-3 — self-audit (run 2026-09-05; commands in `11_prompts/runs/2026-09-05_sprint-1/RUN-REPORT.md`)

| # | Check | Result |
|---|---|---|
| 1 | ID uniqueness — no CC/AR/STL id defined twice | PASS (8 + 4 + 5, all unique) |
| 2 | Census parity — `grep -c '^| CC-' HARDEN-2` = 8 = req_count; anti-rationalization rows = 4 = AR census; MET-1 §9.4 items (a)–(e) = 5 = STL census | PASS (8/8; 4/4; 5/5) |
| 3 | Every member list resolves to files — CC-1 (Primer 0, A–L, variants, harness, annex + annexes), CC-2 (Arch, register schemas), CC-3 (15 corpus-md + MANIFEST), CC-4 (MAK-ANT, REG-POSTURE, R30 seed), CC-5 (OPS-1; WF-/EVT- blocks in Arch §13.6), CC-6 (cdss_diagrams.html, cdss_diagrams_v2.html, 16 artifacts-html), CC-7 (05_ contracts), CC-8 (MT2, HARDEN-1/2/3, MET set) | PASS — every named member has a HARDEN-1.1 row with a resolvable path (HARDEN-1.1 self-audit: 0 missing) |
| 4 | Every mechanical check names a tool that exists in MT2 §2.3 or the tree | PASS-with-record — pack skills (`browser-testing-with-devtools`, `/webperf`) and `references/definition-of-done.md` are external (row zero); `validate_build_plan.py` is **not in the tree** (PENDING-VALIDATOR, 00_MANIFEST §4.4) — recorded, not hidden; all other tools exist (`11_prompts/runs/2026-09-05_sprint-1/tools/` refcheck.py, validate_examples.py, proc_fields.py, mermaid/parse.mjs; `10_regulatory-execution/validate_reg.py`; venv `jsonschema`/`yaml`) |
| 5 | Cross-reference resolution — every anchor cited in D-1 exists: MT2 §1, §2.2, §2.3, §4, §5, §6, §7; Arch §10, §12.1, §12.3, §13.3, §13.6, §13.8, §14.2; 00_MANIFEST §1, §4.2, §4.4, §5 DEF-001; 03_ MANIFEST precedence paragraph; MAK-FFC App. A/B/C; MAK-ANT annex §8; REG-POSTURE §0.4/§0.5/§8/§10; MET-1 §9.4; MET-2 C-11; DEC-11 | PASS (grep, each → 1 heading; external-pack refs flagged as such) |
| 6 | Table integrity — consistent column counts per row in HARDEN-2 v1.0 and in this delta | PASS (HARDEN-2: class-bar table 6 cells × 10 lines; anti-rationalization table 4 cells × 6 lines; this file checked at seal) |
| 7 | No bar changed — D-1 quotes each bar from HARDEN-2 v1.0; HARDEN-2 byte-identical (CHECKSUMS_BEFORE/AFTER) | PASS |
| 8 | Stop-the-line instantiation is complete — MT2 §6 (4 generic rules) + STL-1..5 = 9 rules; every STL maps to a named artifact class where it bites (STL-1 CC-3/corpus; STL-2 CC-2/CC-7; STL-3 CC-1/CC-6 renderers; STL-4 CC-1 GPP profile; STL-5 CC-4) | PASS |

## What this delta does not do
It does not run the pass (W10 T-700 hardens HARDEN-2; T-703 hardens this file), does not
relax any bar, and does not add a class: the eight classes stand; artifacts that fit none
(repository files `.gitignore`, `.github/**`) are classed CC-5/CC-8 in HARDEN-1.1 by rule
and that ruling is recorded there, not here.
