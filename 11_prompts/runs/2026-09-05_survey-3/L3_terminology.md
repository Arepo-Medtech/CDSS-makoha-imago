# L3_terminology — Layer 3 census (Q-D-12, Q-D-13)

Occurrence counts: `grep -o` over every in-scope text asset (2026-09-05) → `raw/terms_counts.txt`. Positions quoted from `raw/L3_positions.txt`.

| Term | occurrences | files |
|---|---|---|
| release spine | 21 | 13 |
| SPINE- | 1092 | 115 |
| coder | 432 | 56 |
| Guideline Compiler | 47 | 26 |
| Observer | 168 | 48 |
| property runs | 20 | 18 |
| Build Evidence | 12 | 7 |
| property-run | 7 | 5 |
| Implementer Contract | 59 | 31 |
| IMPL | 70 | 36 |
| GLOSSARY / Glossary / glossary | 26 | 13 |

## Seed pairs — positions quoted, ruling state

| # | Pair | Positions (path:line, quoted) | Ruling | Class |
|---|---|---|---|---|
| T-1 | "release spine" vs `SPINE-n` | Arch §14.1:494 "House prose distinguishes **'the release spine'** … from **'SPINE-n'** (MAK-FFC fabric requirement IDs)… the glossary rows land in Primer 0 §11"; Primer 0 annex l.98 "**Release spine** — house term for this project's deterministic release path + signed registry, to distinguish it from the fabric's SPINE-n requirement IDs" | **Ruled (C-02) and glossed** — the glossary row exists (Primer 0 annex l.98), not in a separate file | PRESENT-IMPECCABLE; GLOSSARY.md absence is Q-D-13 below |
| T-2 | "coder" vs "Guideline Compiler" | Arch §13.2:442 "'coder' is a reserved house term — the clinical concept coder"; MAK-FFC EN-3:395 "The Guideline Compiler is the only path by which clinical logic enters the engine plane"; MET-2 C-07 "No conflict — distinct components; glossary guards both terms" | Ruled (C-07); the glossary that "guards both terms" is Primer 0 §9 "Glossary of house vocabulary" (l.68) — Phase 2 verifies both terms are in §9 | PRESENT / TAXONOMY-DUPLICATE if §9 lacks either |
| T-3 | "Observer" ×3 | Arch §13.7:481 "Prohibitions: the Observer never holds EVAL credentials, never reads casebundle content… Cadence: one adjudication per level exit plus a standing quarterly review from L4"; OPS-1 §2:10 "Observer adjudicates level exits from registers only (never corpus content; adjudications touching corpus content are void)"; GOV-1:7 "Observer prohibitions (§13.7) and cadence (per-level minimum; quarterly-from-L4 proposed, DEC-08)"; REG-POSTURE §5.3:711 "**Observer independence.** The shared workspace… make it easy to accidentally give the Observer the builder's…" | **Consistent** — one definition (Arch §13.7) restated; REG-POSTURE adds a tool-independence caveat; cadence is DEC-08 (Open) | no L3 row; DEC-08 already registered (DECISION-PENDING) |
| T-4 | R25 label | Arch §12.2:450 "**Proposed R25 — Build Evidence & Assumptions Ledger** · owner `cdss-spine`"; `09_/register_topology_v3.mermaid:6` `R25["R25 property runs<br/>(label under ruling — BSQ-0602)"]`; Primer A A10:153 "R25 property-run outputs (I-1/2)" | **Unruled** (BSQ-0602 carried in INDEX-09 §4) — two labels for one register | TAXONOMY-CONFLICT — EXECUTABLE-AFTER-DECISION, Architecture owner |
| T-5 | `W1–W5` (FOLD-1) vs `W0–W11` (HARDEN-3) | FOLD-1:16 "## W1 — Fold the annex" … :44 "## W5 — Seal checks"; HARDEN-3:13 "| W0 | T-000 row zero…", :14 "| W1 | T-001..003: spine contracts…" | **Unruled** (BSQ-0711 carried in INDEX-10 §4) — one token, two worklists | TAXONOMY-CONFLICT — EXECUTABLE-AFTER-DECISION (namespace ruling); interim alias law is the remediation draft |
| T-6 | "Implementer Contract" / `IMPL` vs `coder_contract.md` | Arch §13.2:442 "`coder_contract.md` is adopted under the name **Implementer Contract (IMPL)**… the source file's content is unchanged, only its house name" | **Ruled** with a rename notice — the alias-law exemplar | PRESENT-IMPECCABLE |

## Q-D-13 — glossary location

`ls GLOSSARY.md` → absent. `grep -n "Glossary" 02_cdss-stack-augmented/primer_0_ecosystem_explainer.md` → l.68 `## 9. Glossary of house vocabulary`; l.98 (annex, under `## 11. Metamorphosis notice`) "Glossary additions (house vocabulary, new this pass)": Fabric, Argument, Face, Register-render law, Deviation, GPP, Release spine, Wing-beat. MET-2 C-02 and Arch §14.1 say "Primer 0 §11 glossary" while the glossary heading is **§9** and the additions sit under **§11**: a §-anchor drift inside two rulings (two stated positions for where the glossary lives). The 15 corpus volumes carry their own definitions (MAK-FFC Part 1, MAK-LWC/RWC vocabularies); no consolidated glossary exists → PROPOSED-ADDITION `GLOSSARY.md` (v1.0 §f candidate) stands, Layer 3, CHAIN.
