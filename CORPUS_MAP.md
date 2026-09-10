---
doc_id: CORPUS-MAP
title: "Imago Corpus Map — top-level volumes at a glance"
date: "2026-09-10"
status: "Proposed. Drafted by Claude agent (MAK-2); pending Ken Lee's review and edit in Confluence before the task is closed."
produced_by: "claude/MAK-2/corpus-map-page — MAK-2"
---

# Imago Corpus Map

> **Rule.** This page cites Imago; it is not a copy of it.
> Descriptions are one-line summaries of each volume's purpose, drawn from `00_MANIFEST.md` §1 at the sealed baseline (`73460b3`).
> For authoritative detail, open the linked folder.
> **Ken: please review and edit this page directly in Confluence, then close MAK-2.**

Each link goes to the GitHub rendering of the folder or file at the sealed v1.2 baseline (`73460b3`).

| # | Folder / File | What it is for | What governs it |
|---|---|---|---|
| 00 | [00\_MANIFEST.md](https://github.com/Arepo-Medtech/CDSS-makoha-imago/blob/73460b3/00_MANIFEST.md) | Master artifact manifest, availability report, production sequence and completeness audit for the entire Imago repository; grows only by appended A-nnn amendments. | Append-only law (AGENTS.md law 1); each amendment section is the source of truth for what was added and when. |
| 01 | [01\_north-star-and-transformation](https://github.com/Arepo-Medtech/CDSS-makoha-imago/tree/73460b3/01_north-star-and-transformation) | Metamorphosis planning: North Star vision (MET-1), conflict and decision register (MET-2 series), traceability map (MET-3) and gap analysis with roadmap (MET-4). | MET-2 and its delta chain (MET-2.1 → MET-2.2 → MET-2.3); decisions close only by their owners. |
| 02 | [02\_cdss-stack-augmented](https://github.com/Arepo-Medtech/CDSS-makoha-imago/tree/73460b3/02_cdss-stack-augmented) | All 21 CDSS stack documents preserved byte-exact with additive annexes: Primer 0, Architecture, Primers A–L, J-1/J-2, Harness, Annex H-1 and two derived artifacts. | Architecture §14; append-only discipline (X1): originals are never edited, annexes are appended. |
| 03 | [03\_makoha-butterfly-corpus](https://github.com/Arepo-Medtech/CDSS-makoha-imago/tree/73460b3/03_makoha-butterfly-corpus) | The Mākoha butterfly corpus: fifteen canonical volumes and sixteen HTML artifacts, carried verbatim and never written by an agent; the corpus owner handles any defect. | MAK-FFC v1.1 (host law); REG-POSTURE v1.2 (regulatory content); `03_makoha-butterfly-corpus/MANIFEST.md` (volume precedence). |
| 04 | [04\_hardening](https://github.com/Arepo-Medtech/CDSS-makoha-imago/tree/73460b3/04_hardening) | MT2 hardening-pass materials: anti-laziness directive, class-bar specification (HARDEN-2), task worklist (HARDEN-3) and R29 coverage ledger (HARDEN-1); the pass itself has not run. | HARDEN-2 class bars (CC-1..CC-8); EXEC-1 run sequencing; the pass may run only after DEC-10 and DEC-11 via `PROMPT-HARDEN`. |
| 05 | [05\_registers-and-contracts](https://github.com/Arepo-Medtech/CDSS-makoha-imago/tree/73460b3/05_registers-and-contracts) | Schemas and seeds for the R29 coverage ledger and R30 register, plus contract templates (CONTRACT-ARG-1, DEV-1, RRI-1). | Architecture §12.1 register laws; DEC-02 (R29/R30 ratified as real registers). |
| 06 | [06\_repositories](https://github.com/Arepo-Medtech/CDSS-makoha-imago/tree/73460b3/06_repositories) | Repository map (REPO-MAP) and skeleton READMEs for all existing and proposed Mākoha repositories, plus CI pipeline stubs. | Architecture §14.4 prefix laws ratified in DEC-09; REPO-MAP v3 is the current map. |
| 07 | [07\_deployment-and-operations](https://github.com/Arepo-Medtech/CDSS-makoha-imago/tree/73460b3/07_deployment-and-operations) | Deployment sequencing (DEPLOY-1/1.1), acceptance criteria (DEPLOY-2), operating procedures (OPS-1/1.1), governance layer (GOV-1) and security/threat model (SEC-1/SEC-2). | EXEC-1 (run sequencing); regulatory mappings in this folder are ADVISORY\_ONLY. |
| 08 | [08\_research](https://github.com/Arepo-Medtech/CDSS-makoha-imago/tree/73460b3/08_research) | Research findings register (RESEARCH-1 series): sourced evidence, newly-verified items, open gaps (RG-01..08), alias laws and proposed sources. | MAK-ELSM (sourcing map); RESEARCH-1 delta chain (read through 1.1 and 1.2). |
| 09 | [09\_diagrams](https://github.com/Arepo-Medtech/CDSS-makoha-imago/tree/73460b3/09_diagrams) | Editable Mermaid diagram sources and rendered HTML successor pages for the system architecture, register topology, deployment ladders and data flow. | HARDEN-2 CC-6 (mermaid parse gate); PROC-09-REGEN (regeneration procedure in INDEX-09). |
| 10 | [10\_regulatory-execution](https://github.com/Arepo-Medtech/CDSS-makoha-imago/tree/73460b3/10_regulatory-execution) | Regulatory posture for four jurisdictions (AU/NZ/US/EU, REG-POSTURE v1.2), governance layer draft (MAK-GOV), sprint plan (REG-SPRINT) and execution directive (EXEC-1). | EXEC-1 (sequencing across the portfolio); every file's own authority line (content is ADVISORY\_ONLY). |
| 11 | [11\_prompts](https://github.com/Arepo-Medtech/CDSS-makoha-imago/tree/73460b3/11_prompts) | Launch prompts for every primer and pass (PROMPT-A..L, P0, PRM-series, HARDEN), survey instruments (PROMPT-SURVEY-1/2/3 series); run records live under `11_prompts/runs/` and are excluded from the Confluence mirror. | Survey/sprint run protocol (AGENTS.md "How work lands"); run directories are evidence only. |

---

*Source: `00_MANIFEST.md` §1 table at sealed baseline [`73460b3`](https://github.com/Arepo-Medtech/CDSS-makoha-imago/commit/73460b3). Agent contribution: drafted by Claude (MAK-2); human owner Ken Lee.*
