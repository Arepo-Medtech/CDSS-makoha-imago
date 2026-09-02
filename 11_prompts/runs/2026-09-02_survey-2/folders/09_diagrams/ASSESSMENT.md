# 09_diagrams — ASSESSMENT (Phase 2)

Census: 5 files, 12,753 B. All four `.mermaid` sources read in full; `cdss_diagrams_v2.html` head, status, blocks and footer read; parse results in `mermaid_parse.json` (Phase 1).

## 1. Discovery and labels
| Item | Bytes | Label | Why | Load-bearing? |
|---|---|---|---|---|
| `imago_architecture.mermaid` (IMAGO-1) | 1,862 | DIAGRAM (source) | "Merged (imago) architecture… Status: Proposed (MET-1 §5.4 successor)" | crit 1 |
| `merged_runtime_sequence.mermaid` (IMAGO-2) | 1,099 | DIAGRAM (source) | "One consultation under the fabric (Primer 0 §4 successor)" | crit 1 |
| `register_topology_v2.mermaid` (IMAGO-3) | 1,290 | DIAGRAM (source) | "Register topology with proposed additions" | crit 1 |
| `deployment_ladders.mermaid` (IMAGO-4) | 1,283 | DIAGRAM (source) | "Three ladders interleaved (DEPLOY-1)" | crit 1 |
| `cdss_diagrams_v2.html` | 7,219 | DIAGRAM (derived page) + ARTIFACT-HTML | "Successor to cdss_diagrams.html (preserved unedited…)"; inlines the four sources | crit 1 (derived; G-10) |

Frontmatter in lieu (P-D-01): each `.mermaid` opens `%% IMAGO-n — <title>. Status: Proposed` (id + title + status; **no version/date**); html carries `<title>`, a status paragraph and footer date "MET-1 pass, 2026-09-01".

## 2. Presence pass — folder chain
| Link | Applicability | PRESENT / ABSENT | Evidence |
|---|---|---|---|
| P-F-01 BRIEFING | APPLIES as index paragraph | ABSENT | `find 09_diagrams -iname '*index*' -o -iname 'readme*'` → none |
| P-F-02 INDEX | APPLIES | PARTIAL — the html's four `<h2>` sections list the diagrams for readers, but no file index (bytes, status, source↔inline identity, HARDEN row) | html h2 ×4 |
| P-F-03 corpus-grade | APPLIES (DIAGRAM lines) | §3–4 | — |
| P-F-04 PRIMER | DOES-NOT-APPLY | — | — |
| P-F-05 LAUNCH PROMPT | APPLIES (small) — regeneration after DEC-01 (G-10) is a Claude-Code-executable act | ABSENT | `ls 11_prompts | grep -i 'diagram\|regen'` → none |
| P-F-06 ARTIFACT-HTML | 09_ *is* the html twin of Arch §10/§11/§12, MET-1 §5.4, DEPLOY-1 | PRESENT | cdss_diagrams_v2.html |
| P-F-07 SKELETON home | APPLIES — the `.mermaid` sources are architecture artifacts; Arch §10 puts "the architecture document" in cdss-spine | ABSENT — no home named | `grep -rln mermaid 06_repositories` → 0 |
| P-F-08 HARDEN rows/tasks | APPLIES | PRESENT — row 43 (bundle "+4 source rows at pass time"); T-072 (W6) | HARDEN-1 l.24; HARDEN-3 l.19 |
| P-F-09 00_MANIFEST row | APPLIES | PRESENT (5 = 5) | CENSUS §1 |
| P-F-10 honesty | APPLIES | PRESENT — "Status: Proposed" on every source; html status + "preserved unedited" | headers |

## 3–4. Document contract + measurement (DIAGRAM floor: parses; nodes/edges agree with Arch §10/§11 and REPO-MAP; successor/regeneration notice where derived)
| Line | Result | Evidence |
|---|---|---|
| parses (CC-6) | PASS 4/4 sources + 4/4 inlined blocks | mermaid_parse.json (mermaid 10.9.0 via jsdom 24.1.3) |
| source ↔ inlined block identity (drift check) | PASS 4/4 — each inlined block is body-identical to its source (comment lines excluded) | script output: deployment_ladders→block 4, imago_architecture→1, merged_runtime_sequence→2, register_topology_v2→3 |
| successor / regeneration notice (derived) | PASS — status para "Successor to cdss_diagrams.html (preserved unedited…)"; footer "Regeneration: edit the .mermaid sources, re-inline, bump this page's date" | html l.17, l.121 |
| nodes/edges agree with Arch §10/§11/§12 | PASS with one exception — IMAGO-3 labels **R25 "property runs"** while Arch §12.2 row 25 is **"Build Evidence & Assumptions Ledger"** (Primer A A10 also says "R25 property-run outputs" — the divergence originates in the Ecosystem-v2.0 layer); all other register labels (R1, R4, R7, R9, R11, R13, R18, R19, R20, R21, R23, R26, R27, R28) match §12.2 rows; IMAGO-1 nodes (library B, registry D, compiler EN-3, coder, engine A, conformal F, graph E, evaluator, faces HDC/TXC/ABC, deviation, corruption G) match Arch §10 repos + REPO-MAP + MET-1 §5.1 Toulmin mapping | Arch l.369 vs register_topology_v2.mermaid l.6 |
| nodes agree with REPO-MAP | PASS (compiler, fabric ledger, faces present; GPP channel absent from IMAGO-1 — acceptable: channel, not a component) | — |
| IMAGO-4 ↔ DEPLOY-1 ↔ EXEC-1 | STALE — draws GATE-000..004, L1–L5, hardening; no RUN-0..4 / SG / NZ-GATE overlay (same staleness as DEPLOY-1, BSQ-0402) | deployment_ladders.mermaid (no 'RUN') |
| P-D-16 xrefs | FAIL ×2 — `MT2 §7.4` in IMAGO-3 and the html (BSQ-0002/0003) + CONTRADICTION with 00_MANIFEST §5 DEF-002 (BSQ-0004); all other anchors (Arch §12.2, MET-1 §5.4, Primer 0 §4, DEPLOY-1, SPINE-n, DEC-02/03/04/06, MT2 §7.4 aside) resolve | refcheck |
| P-D-01 version/date | PARTIAL — no version/date in sources; html footer date only | headers |
| P-D-08/09 | N/A for diagrams; the html's parse-and-identity check is the self-audit — not recorded in the folder (DEF-001 records it in 00_MANIFEST §5) | — |
| G-10 derived-artifact drift | DECISION-PENDING — "regeneration queued behind DEC-01" (relabel); until DEC-01 closes the page carries "exemption posture" deprecations by reference only | MET-4 G-10; HARDEN-1 row 41 |

## 5. Chain confirmation
CHAIN.md 09_ confirmed; additions: R25 label contradiction; source↔inline identity PASS.

## 6. Weighting summary
Queue (≥3): BSQ-0601 INDEX-09 (with recorded parse/identity self-audit), BSQ-0603 DEC-01 regeneration (DECISION-PENDING). Below: BSQ-0602 R25 label contradiction (2, ESCALATED to architecture owner), BSQ-0604 skeleton home (2), BSQ-0605 regeneration prompt (2, dismissed), BSQ-0606 IMAGO-4 run-map overlay (2, depends on DEPLOY-1.1). Phase-1 rows BSQ-0002..0005 belong to this folder.

## 7. Validation
rows=10 invalid=0 valid=10
