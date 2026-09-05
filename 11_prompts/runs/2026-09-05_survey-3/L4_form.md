# L4_form — Layer 4 census, document design system (Q-D-17, Q-F-05)

Evidence commands run 2026-09-05 (outputs pasted in the run log): `grep -o '^## §[0-9]' */INDEX.md`; frontmatter keys of every `*delta*`/`_v1.[12]`/`erratum` file; `grep -h "^status:" … | sort | uniq -c`; `tools/frontmatter.py` (date-field variants); `tools/idgrammar.py` (padding forms).

## 1. INDEX form (Q-F-05) — PASS

All seven INDEX files (04–10) carry the identical ladder `§1 §2 §3 §4 §5`; §1 briefing, §2 file table, §4 honesty line, §5 self-audit; §3 varies by folder (reading rule / tree table / precedence / RG mirror / recorded parse / ID-family map) — a permitted class-specific slot. 7/7 PASS. Exemplar for the class: any of them; `05_registers-and-contracts/INDEX.md` for a folder with mixed classes.

## 2. Delta form (Q-F-05, P-D-11 raised) — 7 of 16 deltas deviate

The exemplar (MET-1.1 pattern as realised by sprint-1): frontmatter `supersedes:` + `applies_to:` + `change_policy:` (+ `req_prefix`/`req_count` when the delta mints), body `# … delta` → `## D-n` items → census/self-audit.

| Delta file | supersedes | applies_to | change_policy | mints declared | Verdict |
|---|---|---|---|---|---|
| `01_/MET-1.1_metamorphosis_plan_delta.md` | ✓ | — | — | n/a | FORM-DEVIATION (the pattern's own namesake lacks `applies_to`/`change_policy`; it predates the form) |
| `01_/MET-2.1_decision_register_delta.md` | — | — | — | mints C/DEC undeclared | FORM-DEVIATION + ID-LIFECYCLE-GAP (status text carries "Read MET-2 through this file" — the sentence exists, the keys do not) |
| `04_/HARDEN-1.1`, `HARDEN-2.1`, `HARDEN-3.1` | ✓ | ✓ | ✓ | ✓ | PASS (exemplars) |
| `05_/REG-R29.1_schema_twin_delta.md` | — | ✓ | ✓ | n/a | minor: no `supersedes` |
| `05_/REG-R30.1_seed_delta.md`, `REG-R30.2_seed_delta.md` | — | — | — | — | FORM-DEVIATION (A-002/A-003 deltas written before the form; INDEX-05 §3 supplies the reading rule externally) |
| `07_/DEPLOY-1.1`, `OPS-1.1` | ✓ | ✓ | ✓ | ✓ | PASS |
| `08_/RESEARCH-1.1` | ✓ | ✓ | ✓ | ✓ | PASS |
| `10_/REG-SPRINT-1.1_delta.md` | — | ✓ | ✓ | — | minor: no `supersedes`; IDs declared by 1.2 |
| `10_/REG-SPRINT-1.2_census_delta.md` | — | ✓ | ✓ | ✓ (`id_prefixes`) | minor: no `supersedes` |
| `10_/REG-POSTURE_v1.1`, `_v1.2`, `REG-NZ_v1.1` | ✓ | n/a (new version, not delta) | via `standalone_rule`/§A–§B logs | ✓ | PASS (version form, not delta form) |
| `11_/PROMPT-SURVEY-3.1`, `3.2` | ✓ | ✓ | ✓ | n/a | PASS |
| `03_/*_v1.1.md` corpus volumes | corpus form (`changelog`, `change_policy`, `req_prefixes`) | | | ✓ | PASS on the corpus form (CORPUS-OWNER anyway) |

## 3. Frontmatter key variants (Q-D-17)

- **Date**: `date` ×93 · `date_issued` ×8 · `guidance_currency_date` ×6. The REG-* files carry two deliberately (issue vs guidance currency); the deviation is that no other class carries `date_issued`, and `frontmatter_census.py` (the CI check) accepts `date_issued` as `date` — an accepted alias with no written rule → FORM-DEVIATION at CHAIN level (a one-line frontmatter rule in the proposed `00_FRONTMATTER.schema.json`), weight 2.
- **ID declaration**: `req_prefix` (singular) · `req_prefixes` (corpus) · `id_prefixes` (REG-*) — three keys for one concept; `frontmatter.py` and the CI census accept all three. FORM-DEVIATION at CHAIN level, weight 2; exemplar rule text: "`req_prefixes` (list) is canonical; `req_prefix`/`id_prefixes` are read as aliases".
- **Status vocabulary**: two conventions coexist — the corpus enum (`normative-draft` ×19, `proposed-normative-draft` ×3, `DRAFT` ×10 in REG-*, `informative-*`) and the house prose-status sentence (P-D-02 honesty: "Proposed. Additive delta… Not yet run." ×30+). Both are the *class's* form (corpus briefing vs survey-2 P-D-02) — not a deviation; recorded so no row is filed for it. Register **row** statuses are closed enums per register (REG-POSTURE §0.4; R29 `state`; QI `state`) — PASS where checked (REG-POSTURE §12.2 check 7; R30.3 549/549 valid).

## 4. ID grammar (Q-D-10, from `idgrammar.py`)

Families with mixed zero-padding across the tree: `T`, `A`, `GPP`, `RG`, `E`, `B`, `NDG`, `AN`, `EX`, `M`. Reading per family is in `L2_id_lifecycle.md` (several are **prefix collisions between unrelated families**, which is a Layer 3 conflict, not a padding slip). Within-family padding slips proper: `NDG-1..9` vs `NDG-10..14` (one file, natural counting — no finding); `GPP-1..16` in MAK-J3 vs `GPP-nn` elsewhere (check in Phase 2).

## 5. Heading ladder per class (Q-D-17)

- Corpus spine (Contents → Thesis → Part 0 → … → ID census → self-audit): 15/15 corpus volumes (survey-2 CORPUS VOLUME floor PASS; not re-measured — law 11).
- Primer X1–X10: 13/13 (02_) and 10/10 (03_/butterfly-primers) per survey-2 / RUN-REPORT R1 declared→mapped 296/296.
- Registers (05_, 04_ seeds): each carries its own table form; R29 md twin vs json agree after R29.1 (INDEX-05 §5).
- Two ladder skips (frontmatter.py): `01_/MET-1_metamorphosis_plan_v1.0.md` (retained) and `03_/butterfly-primers/primer_0_butterfly_explainer.md` (corpus) → companion note / CORPUS-OWNER, weight 1.
