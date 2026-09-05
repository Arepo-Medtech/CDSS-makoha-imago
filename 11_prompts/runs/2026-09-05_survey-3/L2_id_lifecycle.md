# L2_id_lifecycle — Layer 2 census (Q-D-09, Q-D-10) — `tools/idgrammar.py`

Families minted at heading or first-cell position: **155** (2194 mints). Columns: minted · minting files · zero-padding forms seen · files declaring the family (`req_prefix(es)`/`id_prefixes`) · register home (R30.3 by `reg_id`; HARDEN-1.1; MET-2/2.1; others by reading). A family is **requirement-bearing** when its IDs are cited by other documents as requirements, tasks, decisions or findings; **label-only** families (delta items `D-n`/`E-n`, eval cases `T-nn`/`P-nn`, amendment items `A-n`/`B-n`, alignment-map rows `M-n`) are excluded from Q-D-09 and listed at the end.

## Families by size (requirement-bearing; top 60)

| family | minted | files | padding | declared in | register home | reading |
|---|---|---|---|---|---|---|
| `T` | 300 | 4 | {'3d': 276, '2d': 24} | 1 | HARDEN-3.1 (self; R29 on DEC-02) | HARDEN-3.1 tasks (3d, 276) **collide with prompt eval-case labels `T-01..T-14`** (2d, PROMPT-SURVEY-1/3/3.1) — same grammar, unrelated meaning → TAXONOMY-DUPLICATE (OPTIMISATION: rename eval cases `EV-nn` in future prompts; retained prompts unchanged) |
| `TASK-REG` | 70 | 3 | {'3d': 70} | 2 | R30.3 | REG-POSTURE — declared ×12 families, censused §12.1, homed R30.3 — exemplar |
| `STD` | 55 | 3 | {'3d': 55} | 2 | R30.3 | declared and homed — PASS |
| `OBL` | 47 | 3 | {'3d': 47} | 2 | R30.3 | declared and homed — PASS |
| `SRC-REG` | 45 | 3 | {'3d': 45} | 2 | R30.3 | declared and homed — PASS |
| `REG-FIND` | 42 | 3 | {'3d': 42} | 2 | R30.3 | declared and homed — PASS |
| `GPP` | 34 | 4 | {'1d': 20, '2d': 14} | 1 | — | MAK-J3 — declared (16) and cited by MAK-FFC annex — PASS (1d/2d natural counting) |
| `ELSM` | 33 | 2 | {'2d': 33} | 0 | — | corpus sourcing-map entries (MAK-ELSM) — `req_prefixes` absent in `execution-layer-sourcing-map_v1.1.md` (informative volume) → CORPUS-OWNER note |
| `DEC` | 32 | 3 | {'2d': 32} | 0 | MET-2/MET-2.1 | minted by MET-1 §17, MET-2, MET-2.1 — **undeclared** in all three frontmatters (no `req_prefix`); home PENDING-REGISTER-HOME (R26) by MET-2 status → ID-LIFECYCLE-GAP (WARNING, radius 2) |
| `RG` | 31 | 5 | {'1d': 9, '2d': 22} | 2 | RESEARCH-1.1 / INDEX-08 §3 | **prefix collision**: MAK-CEC `RG-1..8` (compound-eyes corpus, 1d, declared in its `req_prefixes`) vs RESEARCH-1 `RG-01..08` (research gaps, 2d, declared by RESEARCH-1.1) — two requirement-bearing families, one prefix → TAXONOMY-CONFLICT (WARNING) |
| `ASSUME-REG` | 31 | 3 | {'3d': 31} | 2 | R30.3 | declared and homed — PASS |
| `Q-REG` | 30 | 3 | {'3d': 30} | 2 | R30.3 | declared and homed — PASS |
| `SPINE` | 28 | 4 | {'1d': 28} | 1 | — | MAK-FFC — declared, censused (Appendix B), homed by MANIFEST precedence — exemplar |
| `EU-STD` | 27 | 1 | {'3d': 27} | 1 | R30.3 | declared and homed — PASS |
| `US-STD` | 27 | 1 | {'3d': 27} | 1 | R30.3 | declared and homed — PASS |
| `C` | 26 | 3 | {'2d': 26} | 0 | MET-2/MET-2.1 | as DEC (MET-2 conflicts) — undeclared; home R27 pending → same row as DEC |
| `NZ-STD` | 26 | 1 | {'3d': 26} | 1 | R30.3 | REG-NZ — declared, censused — exemplar |
| `KTX` | 25 | 3 | {'3d': 25} | 2 | R30.3 | REG-POSTURE — declared; legacy prose-shape ids recorded by §12.2 check 2 — PASS (no invention beyond the file's own record — eval T-07) |
| `WATCH-REG` | 24 | 3 | {'3d': 24} | 2 | R30.3 | declared and homed — PASS |
| `NZ-OBL` | 23 | 2 | {'3d': 23} | 2 | R30.3 | declared and homed — PASS |
| `CC` | 22 | 4 | {'1d': 22} | 2 | HARDEN-2.1 | **prefix collision**: HARDEN-2 class bars `CC-1..8` (declared by HARDEN-2.1) vs MAK-LBP `CC-1..5` (labial-palps corpus, declared) → TAXONOMY-CONFLICT (WARNING) |
| `EN` | 22 | 3 | {'1d': 22} | 1 | — | declared, home by class (corpus MANIFEST precedence / primer) |
| `G` | 21 | 2 | {'2d': 21} | 0 | MET-4 | MET-4 / MET-1 gaps — undeclared; no register home stated → same row (01_ folder ID-LIFECYCLE-GAP) |
| `DR` | 21 | 1 | {'1d': 21} | 1 | DEPLOY-1.1 | DEPLOY-1.1 — declared (`req_prefix: DR`, 7), homed via EXEC-1 RUN → R30 gate rows — PASS |
| `NZ-FIND` | 21 | 2 | {'3d': 21} | 2 | R30.3 | declared and homed — PASS |
| `CF` | 20 | 3 | {'1d': 20} | 1 | — | declared, home by class (corpus MANIFEST precedence / primer) |
| `PF` | 20 | 3 | {'1d': 20} | 1 | — | declared, home by class (corpus MANIFEST precedence / primer) |
| `AF` | 20 | 3 | {'1d': 20} | 1 | — | declared, home by class (corpus MANIFEST precedence / primer) |
| `US-SRC` | 19 | 1 | {'3d': 19} | 1 | R30.3 | declared and homed — PASS |
| `TM` | 18 | 1 | {'2d': 18} | 1 | SEC-2 | SEC-2 — declared (`req_prefix: TM`, 18); no register home (no threat register in Arch §12.2) → ID-LIFECYCLE-GAP (home cell) folded into the SEC-2 PHASE-MAPPING row |
| `NZ-TASK` | 18 | 2 | {'3d': 18} | 2 | R30.3 | declared and homed — PASS |
| `NZ-SRC` | 18 | 2 | {'3d': 18} | 2 | R30.3 | declared and homed — PASS |
| `US-REG` | 17 | 1 | {'3d': 17} | 1 | R30.3 | declared and homed — PASS |
| `REG-KEEP` | 16 | 3 | {'3d': 16} | 2 | R30.3 | declared and homed — PASS |
| `EU-FIND` | 16 | 1 | {'3d': 16} | 1 | R30.3 | declared and homed — PASS |
| `EU-OBL` | 16 | 1 | {'3d': 16} | 1 | R30.3 | declared and homed — PASS |
| `US-FIND` | 16 | 1 | {'3d': 16} | 1 | R30.3 | declared and homed — PASS |
| `NDG` | 14 | 1 | {'1d': 9, '2d': 5} | 1 | R30.3 | MAK-GOV — declared, censused; R30.3 ×14 — PASS (padding 1d/2d natural counting) |
| `EU-LAW` | 14 | 1 | {'3d': 14} | 1 | R30.3 | declared and homed — PASS |
| `EU-SRC` | 14 | 1 | {'3d': 14} | 1 | R30.3 | declared and homed — PASS |
| `US-OBL` | 14 | 1 | {'3d': 14} | 1 | R30.3 | declared and homed — PASS |
| `FZ` | 13 | 3 | {'1d': 13} | 1 | — | declared, home by class (corpus MANIFEST precedence / primer) |
| `AN` | 13 | 2 | {'1d': 10, '2d': 3} | 1 | — | MAK-ANT — declared (12) — PASS |
| `HR` | 13 | 3 | {'1d': 13} | 1 | — | declared, home by class (corpus MANIFEST precedence / primer) |
| `HA` | 13 | 3 | {'1d': 13} | 1 | — | declared, home by class (corpus MANIFEST precedence / primer) |
| `EU-TASK` | 13 | 1 | {'3d': 13} | 1 | R30.3 | declared and homed — PASS |
| `US-TASK` | 13 | 1 | {'3d': 13} | 1 | R30.3 | declared and homed — PASS |
| `PROC` | 12 | 1 | {'2d': 12} | 1 | OPS-1.1 | OPS-1.1 — declared (12) — PASS |
| `SD` | 12 | 3 | {'2d': 12} | 2 | R30.3 | declared and homed — PASS |
| `HW` | 11 | 3 | {'1d': 11} | 1 | — | declared, home by class (corpus MANIFEST precedence / primer) |
| `HG` | 11 | 3 | {'1d': 11} | 1 | — | declared, home by class (corpus MANIFEST precedence / primer) |
| `TW` | 11 | 3 | {'1d': 11} | 1 | — | declared, home by class (corpus MANIFEST precedence / primer) |
| `TR` | 11 | 3 | {'1d': 11} | 1 | — | declared, home by class (corpus MANIFEST precedence / primer) |
| `TA` | 11 | 3 | {'1d': 11} | 1 | — | declared, home by class (corpus MANIFEST precedence / primer) |
| `TL` | 11 | 3 | {'1d': 11} | 1 | — | declared, home by class (corpus MANIFEST precedence / primer) |
| `EX` | 11 | 2 | {'1d': 10, '2d': 1} | 1 | R30.3 | EXEC-1 — declared (10) — PASS (`EX-10` 2d is natural counting) |
| `FS` | 10 | 2 | {'1d': 10} | 1 | — | declared, home by class (corpus MANIFEST precedence / primer) |
| `FE` | 10 | 2 | {'1d': 10} | 1 | — | declared, home by class (corpus MANIFEST precedence / primer) |
| `MS` | 10 | 2 | {'1d': 10} | 1 | — | declared, home by class (corpus MANIFEST precedence / primer) |
| `XC` | 10 | 3 | {'1d': 10} | 1 | — | declared, home by class (corpus MANIFEST precedence / primer) |

## Families never declared (minted ≥3, `declared_in_files` = 0)

`A`, `D`, `ELSM`, `DEC`, `C`, `E`, `G`, `B`, `M`, `P`, `RECON-CEC`, `RECON-LEG`, `RECON-RWC`, `DEF`, `RECON-ABC`, `RECON-ANT`, `RECON-HDC`, `RECON-LBP`, `RECON-PRB`, `RECON-TXC`, `RECON-A`, `RECON-B`, `RECON-D`, `RECON-E`, `RECON-HX`, `RECON-LWC`, `RECON-C`, `RECON-F`, `RECON-G`, `RECON-H`, `RECON-I`, `RECON-J`, `RECON-K`, `RECON-L`, `W`, `J`, `EXEC`

Reading: `RECON-*` (24 families) are the butterfly/component primers' reconciliation rows — the primers (02_ retained; 03_ corpus) declare nothing in frontmatter by design (primer form has no frontmatter; the RUN-REPORT R1 map is their census) → one CORPUS-OWNER/retained note, not 24 rows. `A/D/E/B/M/P` label-only. `W`, `J`, `EXEC` are prose mentions (`J-1`, `EXEC-1` doc ids) not mints. Requirement-bearing undeclared: `DEC`, `C`, `G` (01_), `ELSM` (03_), `DEF` (00_).

## Mixed-padding families
`T`, `A`, `GPP`, `RG`, `E`, `B`, `NDG`, `AN`, `EX`, `M` — of these, `RG`, `CC`, `T`, `A` are collisions or label overlaps (rows above); `GPP`, `NDG`, `AN`, `EX` are natural counting inside one family (no finding); `E`, `B`, `M` label-only.

## Alias-law exemplars (Q-D-09(e))
- `01_/MET-2.1` "**Alias law:** DEC-13..21 are the register homes; the SD-*/DEC-G* names remain valid citations and resolve here. One decision, two names, one row."
- `10_/REG-NZ_v1.1.md` §12.1 "v1.0 prose gates `NZ-GATE-0/1/2` are renamed `NZ-GATE-000/001/002` for pattern conformance; the v1.0 file is unedited."
- `02_/architecture_and_integration.md` §13.2 rename notice (coder_contract → IMPL).
No alias law exists for the two prefix collisions (`RG`, `CC`) or the `W` namespace — those are the Layer 2/3 rows.

