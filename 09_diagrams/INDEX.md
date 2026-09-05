---
doc_id: INDEX-09
title: "INDEX-09 — 09_diagrams: briefing, file table with sources, recorded self-audit (parse + identity), regeneration procedure, known defects"
version: "1.0"
date: "2026-09-05"
status: "Added (sprint-1); indexes only; sources are canonical and the html pages are derived; v2 files preserved unedited (their fixes are v3/v2 successors); regeneration of the 02_ derived artifacts waits on DEC-01 (G-10); nothing here claims deployment"
folder: "09_diagrams/"
produced_by: "sprint-1 (survey-2 Build-Spec Queue) — generated tables from disk by 11_prompts/runs/2026-09-05_sprint-1/tools/render_index.py; briefing text authored; edits nothing"
---

# INDEX-09 — 09_diagrams

## §1 Briefing — sources are canonical, pages are derived

Each `.mermaid` file is the **source** of one diagram (IMAGO-n); each `cdss_diagrams_vN.html` is a **derived page** that inlines sources verbatim so a person can read them rendered. A **successor** (G-10; X1 append-only) is a new file beside the old one — v3 of the topology fixes a citation, v2 of the ladders adds the run overlay — and the old file is never edited (00_MANIFEST §5 DEF-001/DEF-002 pattern). The CC-6 bar (HARDEN-2) is: sources parse, inlined blocks are byte-identical to their sources, the page renders without console errors, links resolve.

## §2 File table

| path | class | doc_id | version | date | status (quoted) | bytes | disposition | HARDEN-1/1.1 row | HARDEN-3.1 task | 00_MANIFEST row | IMAGO id | source documents | standing |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `09_diagrams/INDEX.md` | CC-8 | INDEX-09 | 1.0 | 2026-09-05 | Added (sprint-1); indexes only; sources are canonical and the html pages are derived; v2 files preserved unedited (their fixes are v3/v2 successors); regeneration of the 02_ derived artifacts waits on DEC-01 (G-10); noth… | 10322 | Added (sprint-1) | 219 | T-716 | §1 row (5) + A-004 | INDEX-09 | — | — |
| `09_diagrams/cdss_diagrams_v2.html` | CC-6 | — | — | — | <!DOCTYPE html> | 7219 | Added (Proposed) | 43 | T-072 | §1 row (5) + A-004 | page v2 | inlines IMAGO-1..4 (v1/v2 sources) | superseded by v3; preserved unedited (footer date 2026-09-01) |
| `09_diagrams/cdss_diagrams_v3.html` | CC-6 | — | — | — | <!DOCTYPE html> | 10917 | Added (sprint-1) — Proposed | 220 | T-183 | §1 row (5) + A-004 | page v3 | inlines IMAGO-1, 2, 3 v3, 4 v2, 5 | current successor page |
| `09_diagrams/data_flow_v1.mermaid` | CC-6 | IMAGO-5 — Data-flow and trust boundaries | — | — | %% IMAGO-5 — Data-flow and trust boundaries (SEC-2 §1 source). Status: Proposed. Derived from Arch §11.5 topology + §11.4 mapping + §10 corpus firewall; substrate per DEC-03 (both drawn, Baseten marked pending). No deplo… | 2014 | Added (sprint-1) — Proposed | 221 | T-182 | §1 row (5) + A-004 | IMAGO-5 | Arch §11.1/§11.4/§11.5, §10 corpus firewall; SEC-1; SEC-2 §1 | current (v3 block 5) |
| `09_diagrams/deployment_ladders.mermaid` | CC-6 | IMAGO-4 — Three ladders interleaved (DEP | — | — | %% IMAGO-4 — Three ladders interleaved (DEPLOY-1). Status: Proposed | 1283 | Added (Proposed) | 222 | T-076 | §1 row (5) + A-004 | IMAGO-4 | DEPLOY-1 ladders; MAK-ANT §7 gates; Arch §11.2 levels | superseded by v2 (no RUN overlay); preserved unedited |
| `09_diagrams/deployment_ladders_v2.mermaid` | CC-6 | IMAGO-4 v2 — Three ladders interleaved ( | — | — | %% IMAGO-4 v2 — Three ladders interleaved (DEPLOY-1) with the EXEC-1 RUN-0..4 overlay (DEPLOY-1.1 D-1). Status: Proposed; in force as calendar on DEC-22. | 2229 | Added (sprint-1) — Proposed | 223 | T-181 | §1 row (5) + A-004 | IMAGO-4 v2 | as v1 + EXEC-1 RUN-0..4 via DEPLOY-1.1 D-1 | current (v3 block 4); in force as calendar on DEC-22 |
| `09_diagrams/imago_architecture.mermaid` | CC-6 | IMAGO-1 — Merged (imago) architecture: f | — | — | %% IMAGO-1 — Merged (imago) architecture: fabric wraps the release spine. Status: Proposed (MET-1 §5.4 successor) | 1862 | Added (Proposed) | 224 | T-073 | §1 row (5) + A-004 | IMAGO-1 | Arch §2/§10 (repos, spine), MET-1 §5.1/§5.4 (Toulmin mapping), MAK-FFC Part 2 | current (inlined in v2 block 1 and v3 block 1) |
| `09_diagrams/merged_runtime_sequence.mermaid` | CC-6 | IMAGO-2 — One consultation under the fab | — | — | %% IMAGO-2 — One consultation under the fabric (Primer 0 §4 successor). Status: Proposed | 1099 | Added (Proposed) | 225 | T-074 | §1 row (5) + A-004 | IMAGO-2 | Primer 0 §4 (worked consultation), Arch §3 (release path), MAK-FFC SPINE-2..5/8 | current (v2 block 2; v3 block 2); DEF-001 grammar note |
| `09_diagrams/register_topology_v2.mermaid` | CC-6 | IMAGO-3 — Register topology with propose | — | — | %% IMAGO-3 — Register topology with proposed additions. R1–R28 Existing/Ratified (Arch §12.2 + Ecosystem v2.0); R29–R30 Proposed (DEC-02) | 1290 | Added (Proposed) | 226 | T-075 | §1 row (5) + A-004 | IMAGO-3 v2 | Arch §12.2 register table, §12.4; DEC-02/04 | superseded by v3 (MT2 §7.4 notation — DEF-003); preserved unedited |
| `09_diagrams/register_topology_v3.mermaid` | CC-6 | IMAGO-3 v3 — Register topology with prop | — | — | %% IMAGO-3 v3 — Register topology with proposed additions. R1–R28 Existing/Ratified (Arch §12.2 + Ecosystem v2.0); R29–R30 Proposed (DEC-02). Status: Proposed. | 1721 | Added (sprint-1) — Proposed | 227 | T-180 | §1 row (5) + A-004 | IMAGO-3 v3 | as v2; notation fixed to §7(4); R25 label pending BSQ-0602 ruling | current (v3 block 3) |

## §3 Recorded self-audit (P-D-09 / CC-6) — `11_prompts/runs/2026-09-05_sprint-1/tools/mermaid/parse.mjs` and the identity script, run 2026-09-05

```
{
 "tool": "mermaid 10.9.8 via jsdom 24.1.3 (node v20.20.2)",
 "results": [
  {
   "file": "data_flow_v1.mermaid",
   "kind": "source",
   "result": "PASS"
  },
  {
   "file": "deployment_ladders.mermaid",
   "kind": "source",
   "result": "PASS"
  },
  {
   "file": "deployment_ladders_v2.mermaid",
   "kind": "source",
   "result": "PASS"
  },
  {
   "file": "imago_architecture.mermaid",
   "kind": "source",
   "result": "PASS"
  },
  {
   "file": "merged_runtime_sequence.mermaid",
   "kind": "source",
   "result": "PASS"
  },
  {
   "file": "register_topology_v2.mermaid",
   "kind": "source",
   "result": "PASS"
  },
  {
   "file": "register_topology_v3.mermaid",
   "kind": "source",
   "result": "PASS"
  },
  {
   "file": "cdss_diagrams_v2.html",
   "kind": "inlined block 1",
   "result": "PASS"
  },
  {
   "file": "cdss_diagrams_v2.html",
   "kind": "inlined block 2",
   "result": "PASS"
  },
  {
   "file": "cdss_diagrams_v2.html",
   "kind": "inlined block 3",
   "result": "PASS"
  },
  {
   "file": "cdss_diagrams_v2.html",
   "kind": "inlined block 4",
   "result": "PASS"
  },
  {
   "file": "cdss_diagrams_v3.html",
   "kind": "inlined block 1",
   "result": "PASS"
  },
  {
   "file": "cdss_diagrams_v3.html",
   "kind": "inlined block 2",
   "result": "PASS"
  },
  {
   "file": "cdss_diagrams_v3.html",
   "kind": "inlined block 3",
   "result": "PASS"
  },
  {
   "file": "cdss_diagrams_v3.html",
   "kind": "inlined block 4",
   "result": "PASS"
  },
  {
   "file": "cdss_diagrams_v3.html",
   "kind": "inlined block 5",
   "result": "PASS"
  }
 ]
}
```
```
block 1 ↔ imago_architecture.mermaid: IDENTICAL
  block 2 ↔ merged_runtime_sequence.mermaid: IDENTICAL
  block 3 ↔ register_topology_v3.mermaid: IDENTICAL
  block 4 ↔ deployment_ladders_v2.mermaid: IDENTICAL
  block 5 ↔ data_flow_v1.mermaid: IDENTICAL
  v2 block 1 ↔ imago_architecture.mermaid: IDENTICAL
  v2 block 2 ↔ merged_runtime_sequence.mermaid: IDENTICAL
  v2 block 3 ↔ register_topology_v2.mermaid: IDENTICAL
  v2 block 4 ↔ deployment_ladders.mermaid: IDENTICAL
  v3 notation check: grep 'MT2 §7.4' in register_topology_v3.mermaid + cdss_diagrams_v3.html → 0 occurrences
```

## §4 Regeneration procedure (CC-5 form) and known defects carried

**PROC-09-REGEN** — trigger: DEC-01 closes (portfolio-wide relabel → 02_ derived artifacts regenerate, G-10) **or** any `.mermaid` source changes. Steps: (1) edit or add a source as a new versioned file `{{name}}_vN.mermaid` (never edit v(N−1)) `{timeout: n/a, retry: n/a, idempotent: by file version, on_fail: revert; DEF row}` → (2) headless parse of every source and every inlined block `{timeout: 5m, retry: 1, idempotent: yes, on_fail: HALT — a source that does not parse is not inlined}` → (3) re-inline into a new `cdss_diagrams_vN.html` with the status paragraph naming what changed `{timeout: n/a, retry: n/a, idempotent: by block hash, on_fail: identity check fails → page not written}` → (4) source↔inline identity check 100% `{timeout: 1m, retry: 1, idempotent: yes, on_fail: HALT}` → (5) bump the page date; propose the 00_MANIFEST amendment row and the HARDEN-1.1 rows for the new files `{timeout: n/a, retry: n/a, idempotent: yes, on_fail: n/a}`. Exit evidence: parse JSON + identity output pasted in this INDEX §3 (or its successor). Owner: Architecture owner. Source: 00_MANIFEST §5 DEF-001 method; HARDEN-2 CC-6; G-10.

Known defects carried (not edited in place): `register_topology_v2.mermaid` l.17 and `cdss_diagrams_v2.html` l.96 read `MT2 §7.4` (DEF-002 item notation → `§7(4)`) — fixed in v3 successors (DEF-003, A-004). IMAGO-3 (v2 and v3) label **R25 "property runs"** while Arch §12.2 row 25 is "Build Evidence & Assumptions Ledger" and Primer A A10 says "property-run outputs" — a two-source disagreement the architecture owner rules (survey-2 BSQ-0602); carried unchanged with the ruling pending. No home is yet named in 06_ for the sources (BSQ-0604 → `cdss-spine/architecture/` after DEC-09).

## §5 Honesty line and self-audit

Every source header says "Status: Proposed"; the pages carry an R29 row PENDING, not HARDENED. Regeneration of `02_cdss-stack-augmented/cdss_complete_stack.md` and `cdss_diagrams.html` (HARDEN-1 rows 41–42) is queued behind DEC-01 and has not happened.

- Files in table = on disk = 10 — PASS. Parse: 7/7 sources, 4/4 v2 blocks, 5/5 v3 blocks — PASS. Identity: 9/9 — PASS. `MT2 §7.4` occurrences in v3 files: 0 — PASS.
- Every cited § (Arch §2/§3/§10/§11/§12; MET-1 §5.1/§5.4; Primer 0 §4; DEPLOY-1; EXEC-1; SEC-2) resolves — PASS (refcheck).
