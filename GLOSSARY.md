---
doc_id: GLOSSARY
title: "GLOSSARY — house vocabulary of the Mākoha Imago design record: term, quoted source line, ruling that guards it, aliases and near-misses, owning home"
version: "1.0"
date: "2026-09-05"
status: "Added (sprint-2). Consolidates by reference; defines nothing new. Every row quotes its source (path:line on main 21b9675) or cites a corpus volume by id and part without restating corpus text beyond one line. Rulings marked OPEN are open. A term is never deleted; a superseded term gains a 'superseded by' note in a later version."
change_policy: "Additive; later versions are new files (GLOSSARY_v1.1.md …) or a companion delta; this file is never edited once merged"
produced_by: "sprint-2 (survey-3 Queue §c.1 row QI-0032) — 11_prompts/runs/2026-09-05_sprint-2/"
---

# GLOSSARY — house vocabulary

Five places defined house terms until now: Primer 0 §9 and its §11 annex, MAK-FFC Part 1–2, the
MAK-LWC/RWC vocabularies, and the MET-2 rulings C-02 and C-07 (survey-3 QI-0032). This file is the
one citable location. It adds no meaning: where a definition is quoted it is the source's sentence;
where a corpus volume owns the term the row points into the volume.

## §1 Terms

| Term | Definition (quoted or pointed) | Source (path:line) | Ruling / status | Aliases · not to be confused with | Home |
|---|---|---|---|---|---|
| Spine (release spine) | "the deterministic release path plus the signed registry; the architecture's core" | `02_cdss-stack-augmented/primer_0_ecosystem_explainer.md` l.70; "Release spine — house term … to distinguish it from the fabric's SPINE-n requirement IDs" `02_cdss-stack-augmented/primer_0_ecosystem_explainer.md` l.98; Arch §14.1 `02_cdss-stack-augmented/architecture_and_integration.md` l.494 | C-02 Ruled (proposed) — nomenclature only | ≠ **SPINE-n** (MAK-FFC Part 2 requirement ids, e.g. SPINE-7) | Arch §1; MAK-FFC Part 2 |
| SPINE-n | MAK-FFC fabric requirement ids (Part 2, "The shared spine") | `03_makoha-butterfly-corpus/corpus-md/four-faces-corpus_v1.1.md` l.87 (Part 2), l.165 (SPINE-7) | — | ≠ release spine | MAK-FFC |
| Doctrine | "ML proposes and tests; only arithmetic releases" (SPINE-7 statement) | `03_makoha-butterfly-corpus/corpus-md/four-faces-corpus_v1.1.md` l.166; AGENTS.md law 2 | non-negotiable (AGENTS.md) | — | MAK-FFC SPINE-7 |
| Glass box | "a system whose internal logic a clinician can inspect (the regulator's term; this project's design goal)" | `02_cdss-stack-augmented/primer_0_ecosystem_explainer.md` l.70 | — | — | Primer 0 §9 |
| LR (likelihood ratio) | "how much a finding shifts the odds of a diagnosis; the library's working currency" | `02_cdss-stack-augmented/primer_0_ecosystem_explainer.md` l.70 | — | — | Primer 0 §9; Primer B |
| Conformal set | "a diagnosis list with a mathematical coverage guarantee" | `02_cdss-stack-augmented/primer_0_ecosystem_explainer.md` l.70 | — | qualifier (Toulmin slot, see Argument) | Primer 0 §9; Primer F |
| Casebundle | "one authored exam case in the firewalled corpus" | `02_cdss-stack-augmented/primer_0_ecosystem_explainer.md` l.70 | — | no patient data exists in this repository (AGENTS.md law 7) | Primer 0 §9; Primer C |
| Corruption / perturbation | "a deliberate, label-guaranteed breakage used to prove the gates work" | `02_cdss-stack-augmented/primer_0_ecosystem_explainer.md` l.70 | — | — | Primer 0 §9; Primer G |
| Lattice | "a governance layer running across all components (I: changes, J: models, K/L: LLMs)" | `02_cdss-stack-augmented/primer_0_ecosystem_explainer.md` l.70 | — | — | Primer 0 §9 |
| Register | "a ledger; there are 28; if it's not in one, it didn't happen" — now 30 (R29, R30 ratified) | `02_cdss-stack-augmented/primer_0_ecosystem_explainer.md` l.70; Arch §12.2 `02_cdss-stack-augmented/architecture_and_integration.md` l.511–512 | DEC-02 Closed (MET-2.2 §3.4) | R-n ids; register laws Arch §12.1 | Arch §12 |
| Fork / posture | "the J-1 vs J-2 coder decision" | `02_cdss-stack-augmented/primer_0_ecosystem_explainer.md` l.70 | C-01 transformed; DEC-01 Closed (MET-2.2 §3.9); `ASSUME-REG-002` OPEN | posture (regulatory) ≠ posture (fork) — REG-POSTURE §0.1 is the regulatory sense | Primer 0 §7; REG-POSTURE v1.2 |
| Level | "one of five progressively complete versions of the product" | `02_cdss-stack-augmented/primer_0_ecosystem_explainer.md` l.70; Arch §11.2 | — | L1–L5 ≠ tier T1–T5 (Arch §11.1) | Arch §11 |
| Fragment | "one signed, statement-level piece of authoritative content in the registry" | `02_cdss-stack-augmented/primer_0_ecosystem_explainer.md` l.70 | — | — | Primer D |
| Trace | "the replayable arithmetic record of one engine run" | `02_cdss-stack-augmented/primer_0_ecosystem_explainer.md` l.70 | — | — | Primer A |
| Abstention | "a component saying 'I don't know' instead of guessing; always a legal output here" | `02_cdss-stack-augmented/primer_0_ecosystem_explainer.md` l.70 | — | — | Primer 0 §9 |
| Fabric | "the justification layer (MAK-FFC): every released claim is a Toulmin-structured argument, append-only and hash-chained" | `02_cdss-stack-augmented/primer_0_ecosystem_explainer.md` l.98 | DEC-04 (ledger substrate) OPEN | — | MAK-FFC |
| Argument (ActualArgument) | "the canonical release unit: claim, grounds, warrant, backing, qualifier, rebuttal" | `02_cdss-stack-augmented/primer_0_ecosystem_explainer.md` l.98; schema `05_registers-and-contracts/CONTRACT-ARG-1.schema.json` | — | GenericArgument (compiler output) | MAK-FFC; CONTRACT-ARG-1 |
| Face | "one of three role surfaces (clinician, patient, auditor) rendering the same argument in its own register" | `02_cdss-stack-augmented/primer_0_ecosystem_explainer.md` l.98 | patient face scope: DEC-07 OPEN | ≠ Governance Layer (C-15: "different faces") | MAK-FFC Parts 3–5 |
| Register-render law | "renderers may compress or reorder, never add, remove, or reweight (SPINE-3)" | `02_cdss-stack-augmented/primer_0_ecosystem_explainer.md` l.98 | — | — | MAK-FFC SPINE-3 |
| Deviation | "a clinician's structured, first-class departure from a recommendation (SPINE-8)" | `02_cdss-stack-augmented/primer_0_ecosystem_explainer.md` l.98; schema `05_registers-and-contracts/CONTRACT-DEV-1.schema.json` | — | — | MAK-FFC SPINE-8 |
| GPP | "the J-3 exempt-tier build artifact (guideline prompts only; diagnosis-contributing capabilities structurally absent)" | `02_cdss-stack-augmented/primer_0_ecosystem_explainer.md` l.98; `06_repositories/REPO-MAP_v3.md` channel row | DEC-06 OPEN (J-3 neither built nor retired, EX-4) | GPP is a release channel, not a repository; PFX GPP ratified (DEC-09) | MAK-J3 |
| Wing-beat | "one of eight fuzzy × meta-rationality coordination patterns (MAK-MIF beat n)" | `02_cdss-stack-augmented/primer_0_ecosystem_explainer.md` l.98 | DEC-05 (FZ ratification) OPEN | — | MAK-MIF / MAK-LWC / MAK-RWC |
| Coder | the clinical concept coder — "'coder' is a reserved house term — the clinical concept coder, subject of the J-1/J-2 fork" | `02_cdss-stack-augmented/architecture_and_integration.md` l.442 (§13.2); C-07 `01_north-star-and-transformation/MET-2_conflict_and_decision_register.md` l.20 | C-07 No conflict — "glossary guards both terms" | ≠ Guideline Compiler; ≠ the former file name coder_contract.md (external pack; see IMPL) | Arch §9, §13.2 |
| Guideline Compiler | MAK-FFC EN-3: the path by which guideline logic enters the engine plane as GenericArguments | `03_makoha-butterfly-corpus/corpus-md/four-faces-corpus_v1.1.md` l.394 (EN-3); Arch §14.5 | C-07 | ≠ coder; repository `cdss-compiler` (Proposed) | MAK-FFC Part 6 |
| Implementer Contract (IMPL) | "coder_contract.md is adopted under the name Implementer Contract (IMPL)" | `02_cdss-stack-augmented/architecture_and_integration.md` l.442 (§13.2) | DEC-08 Closed — rename ratified (MET-2.2 §3.6) | coder_contract.md — external pack file, not in this tree | Arch §13.2 |
| Observer | adjudicates level exits "from registers only, never corpus content"; "one adjudication per level exit plus a standing quarterly review from L4" | `02_cdss-stack-augmented/architecture_and_integration.md` l.481 (§13.7) | DEC-08 Closed — cadence ratified (MET-2.2 §3.6) | ≠ auditor face | Arch §13.7; GOV-1 |
| MT2 operator | the person who receives the consolidated blocker report of the hardening pass | `04_hardening/MAJOR_TASK_2_anti-laziness-hardening-directive.md` l.73, l.116 | DEC-10 Closed — Kenny-bytes (MET-2.2 §3.2) | — | MT2 §6–7; HARDEN-3 |
| HARDENED / ESCALATED | the only two end states of a ledger row: "HARDENED (with evidence) or ESCALATED (with the specific blocker …). There is no third state." | `04_hardening/MAJOR_TASK_2_anti-laziness-hardening-directive.md` l.73 | — | PENDING is a pre-pass placeholder, not a state (HARDEN-1.1) | R29 |
| Row zero | W0 / T-000: whole-pack install and inventory reconciliation before any wave | `04_hardening/HARDEN-3_hardening_plan_worklist.md` l.13 | DEC-11 Closed — C-11 rule accepted (MET-2.2 §3.3) | — | HARDEN-3; R29 row 0 |
| W-n | HARDEN-3 wave (unqualified); FOLD-1 step only when qualified `FOLD-1 W-n` / `FW-n` | `04_hardening/HARDEN-2.2_alias_laws_delta.md` D-4 | DEC-26(a) Proposed — OPEN | — | HARDEN-3 / FOLD-1 |
| CC-n | HARDEN-2 class bar (04_–10_, ledger rows) or MAK-LBP requirement (03_) — cross-folder citations qualify | `04_hardening/HARDEN-2.2_alias_laws_delta.md` D-2 | DEC-26(c) Proposed — OPEN | — | HARDEN-2 / MAK-LBP |
| RG-nn / RG-n | two-digit = research gap (RESEARCH-1); one-digit = MAK-CEC requirement; new gaps mint RGAP-nnn | `08_research/RESEARCH-1.2_alias_and_triggers_delta.md` D-2 | DEC-26(b) Proposed — OPEN | — | RESEARCH-1 / MAK-CEC |
| R25 | Arch §12.2 "Build Evidence & Assumptions Ledger" vs IMAGO-3 / Primer A "property runs" | `02_cdss-stack-augmented/architecture_and_integration.md` l.450 (§13.4 row); `09_diagrams/register_topology_v4.mermaid` | DEC-25 Proposed — OPEN (label under ruling) | — | Arch §12.2 |
| Governance Layer (MAK-GOV) | the non-device organisational-conformance artifact; "different face" from the patient face (C-15) | `10_regulatory-execution/MAK-GOV_addendum-g_v0.9.md` l.2; MET-2.1 C-15 | DEC-13 Closed — doc_id MAK-GOV permanent; DEC-14 Closed for build scope (MET-2.2 §3.7–3.8) | Addendum G (display title); DEC-G1..G4 = DEC-13..16 | MAK-GOV |
| ADVISORY_ONLY | the standing of every regulatory posture document: assumptions requiring counsel attestation, never attested here | `10_regulatory-execution/REG-POSTURE_v1.2.md` l.139 (§0.1) | — | — | REG-POSTURE §0 |
| DONE-WITH-EVIDENCE / HALT-TYPED | task end states: evidence artifact named, or a typed halt | `10_regulatory-execution/REG-POSTURE_v1.2.md` l.185 (§0.4); `10_regulatory-execution/REG-TASK-OWNERS_companion.md` names the artifact per task | — | ≠ HARDENED/ESCALATED (ledger rows) | REG-POSTURE §0.4 |
| Delta · companion · successor | the three forms a change takes under the append-only law: a file named X-1.1_…_delta.md beside X; a companion read with X; a new version beside the old | `AGENTS.md` law 1; `README.md` "Laws of the corpus" | — | erratum = a delta over a delta (PROMPT-SURVEY-3.2) | README; AGENTS.md |
| OPEN means OPEN | no ASSUME, DEC, gate or posture is closed by an agent; owners close in MET-2 / MET-2.1 / MET-2.2 | `AGENTS.md` law 4 | — | — | AGENTS.md |

## §2 Census and self-audit

Rows: 38 terms. `grep -c '^| [A-Z]' GLOSSARY.md` → 39 (38 term rows + header). Every source path resolves
(`.github/audit/refcheck.py` on this file: 0 dead paths). Lines quoted were read on `main` 21b9675
(2026-09-05). Rulings cited: C-01, C-02, C-07, C-15, DEC-01, 02, 04, 05, 06, 07, 08, 10, 11, 13, 14,
25, 26 — states as in MET-2.2 §2 (OPEN rows say OPEN). Corpus text quoted: one statement (SPINE-7) by
line; everything else in 03_ is pointed to, not restated. Ledger row and task for this file:
HARDEN-1.2 / HARDEN-3.2 (same sprint); manifest row A-010; README "Where to read it" row.
