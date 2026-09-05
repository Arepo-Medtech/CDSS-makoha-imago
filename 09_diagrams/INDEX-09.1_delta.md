---
doc_id: INDEX-09.1
title: "INDEX-09.1 — 09_diagrams: rows for the files sprint-2 added (read with 09_diagrams/INDEX.md)"
version: "1.0"
date: "2026-09-05"
status: "Added (sprint-2). Additive delta over 09_diagrams/INDEX.md (not edited); indexes only. Every row is generated from disk by the sprint-2 generator; HARDEN row and task ids are those HARDEN-1.2 / HARDEN-3.2 assign; the manifest row is A-010."
supersedes: "nothing — 09_diagrams/INDEX.md preserved verbatim beside this file"
folder: "09_diagrams/"
produced_by: "sprint-2 — 11_prompts/runs/2026-09-05_sprint-2/tools/ledger2.py"
---

# INDEX-09.1 — 09_diagrams (sprint-2 additions)

## §1 What arrived and why

The DEC-01 regeneration run (PROC-09-REGEN, INDEX-09 §4): IMAGO-3 v4 draws R29/R30 solid (DEC-02); cdss_diagrams_v4.html inlines it and links tokens.css (QI-0043/QI-0044); v3 files are retained.

## §2 File table (sprint-2 additions)

| path | class | doc_id | version | date | status (quoted) | bytes | disposition | HARDEN-1.2 row | HARDEN-3.2 task | 00_MANIFEST row |
|---|---|---|---|---|---|---|---|---|---|---|
| `09_diagrams/INDEX-09.1_delta.md` | CC-8 | INDEX-09.1 | 1.0 | 2026-09-05 | Added (sprint-2). Additive delta over 09_diagrams/INDEX.md (not edited); indexes only. Every row is generated from disk by the sprint-2 generator; HARDEN row and task ids are those HARDEN-1.2 / HARDEN… | 4155 | Added (sprint-2) — Proposed | 408 | T-934 | §16 A-010 |
| `09_diagrams/cdss_diagrams_v4.html` | CC-6 | — | — | — | <!DOCTYPE html> | 11671 | Added (sprint-2) — Proposed | 409 | T-935 | §16 A-010 |
| `09_diagrams/register_topology_v4.mermaid` | CC-6 | — | — | — | %% IMAGO-3 v4 — Register topology. R1–R28 Existing/Ratified (Arch §12.2 + Ecosystem v2.0); R29–R30 RATIFIED by DEC-02 (MET-2.2 §3.4, 2026-09-05) and drawn solid | 1894 | Added (sprint-2) — Proposed | 410 | T-936 | §16 A-010 |
| `09_diagrams/tokens.css` | CC-6 | — | — | — | /* tokens.css — Mākoha Imago design tokens for browser-borne pages (sprint-2, 2026-09-05). | 2124 | Added (sprint-2) — Proposed | 411 | T-937 | §16 A-010 |

## §3 Recorded self-audit — headless parse of every source and inlined block (sprint-1 `tools/mermaid/parse.mjs`, run 2026-09-05)

```
mermaid 10.9.8 via jsdom 24.1.3 (node v20.20.2)
  data_flow_v1.mermaid                 source             PASS
  deployment_ladders.mermaid           source             PASS
  deployment_ladders_v2.mermaid        source             PASS
  imago_architecture.mermaid           source             PASS
  merged_runtime_sequence.mermaid      source             PASS
  register_topology_v2.mermaid         source             PASS
  register_topology_v3.mermaid         source             PASS
  register_topology_v4.mermaid         source             PASS
  cdss_diagrams_v2.html                inlined block 1    PASS
  cdss_diagrams_v2.html                inlined block 2    PASS
  cdss_diagrams_v2.html                inlined block 3    PASS
  cdss_diagrams_v2.html                inlined block 4    PASS
  cdss_diagrams_v3.html                inlined block 1    PASS
  cdss_diagrams_v3.html                inlined block 2    PASS
  cdss_diagrams_v3.html                inlined block 3    PASS
  cdss_diagrams_v3.html                inlined block 4    PASS
  cdss_diagrams_v3.html                inlined block 5    PASS
  cdss_diagrams_v4.html                inlined block 1    PASS
  cdss_diagrams_v4.html                inlined block 2    PASS
  cdss_diagrams_v4.html                inlined block 3    PASS
  cdss_diagrams_v4.html                inlined block 4    PASS
  cdss_diagrams_v4.html                inlined block 5    PASS
total 22  FAIL 0
```

Source↔inline identity: the v4 page inlines `register_topology_v4.mermaid` from the `flowchart LR` line verbatim (generator copies the source; RUN-REPORT pastes the diff = ∅). R25 label carried pending DEC-25; `MT2 §7.4` occurrences in v4 files: 0.

## §4 Census

Rows: 4 = files sprint-2 added under `09_diagrams/` (generator); each has a HARDEN-1.2 row and a HARDEN-3.2 task. Parent INDEX byte-identical (sprint-2 CHECKSUMS).
