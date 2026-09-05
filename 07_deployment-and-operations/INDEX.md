---
doc_id: INDEX-07
title: "INDEX-07 — 07_deployment-and-operations: briefing, file table, precedence note, honesty line, self-audit"
version: "1.0"
date: "2026-09-05"
status: "Added (sprint-1); indexes only; nothing is deployed; every file Proposed/Retained per its own status; person-level owners [NEEDS DEFINITION] throughout (GOV-1); RTO/RPO/DR [NEEDS DEFINITION] (G-09, proposed DEC-23)"
folder: "07_deployment-and-operations/"
produced_by: "sprint-1 (survey-2 Build-Spec Queue) — generated tables from disk by 11_prompts/runs/2026-09-05_sprint-1/tools/render_index.py; briefing text authored; edits nothing"
---

# INDEX-07 — 07_deployment-and-operations

## §1 Briefing — what these documents are

A **DEPLOY plan** sequences what is built and gated when (DEPLOY-1: three ladders — the hardening pass, the regulatory gates GATE-000..004, the maturity levels L1–L5 — interleaved); **acceptance criteria** say what proves a level or gate is passed (DEPLOY-2: Arch §11.2 exits + eight added criteria); an **OPS procedure** says how a recurring act is performed — in this ecosystem every step carries timeout/retry/idempotency/on_fail (HARDEN-2 CC-5, the Arch §13.6 pattern; OPS-1.1 gives OPS-1's prose that form); **GOV** names owners and post-deployment duties; **SEC** carries the security, privacy and compliance surface (SEC-1) and, since sprint-1, the threat model and data-flow map it hangs from (SEC-2). They compose with Arch §11 (tiers and levels, Retained) and with EXEC-1 (which now governs their *sequence*, EX-1/EX-5). Form exemplar: `02_cdss-stack-augmented/primers_briefing.md`.

## §2 File table

| path | class | doc_id | version | date | status (quoted) | bytes | disposition | HARDEN-1/1.1 row | HARDEN-3.1 task | 00_MANIFEST row | read-through rule |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `07_deployment-and-operations/DEPLOY-1.1_run-map_delta.md` | CC-5 | DEPLOY-1.1 | 1.1-delta | 2026-09-05 | Added; DEPLOY-1 v1.0 not edited; read DEPLOY-1 through this file (EXEC-1 EX-5). In force as sequencing only when DEC-22 closes (adopt EXEC-1 precedence and the run map); until then it is the drafted mapping the decision … | 10334 | Added (sprint-1) — Proposed | 208 | T-501 | §1 row (5) + A-004 | — |
| `07_deployment-and-operations/DEPLOY-1_deployment_plan_and_sequencing.md` | CC-5 | DEPLOY-1 | 1.0 | — | Proposed. Grounded in Arch §11 (levels/tiers, Retained), MAK-ANT §7 (phases/gates, Added), MT2 (pass, Proposed). The tier pipeline T1+2→T5 never relaxes under any step. | 3805 | Retained + Added/Proposed (per status) | 71 | T-101 | §1 row (5) + A-004 | read through DEPLOY-1.1 (run map; in force on DEC-22) |
| `07_deployment-and-operations/DEPLOY-2_testing_verification_acceptance.md` | CC-5 | DEPLOY-2 | 1.0 | — | Retained (all Arch §11.2 exits, register checks §12.3, 100% catch, I8 tolerances, checkpoint floors, Observer checkpoints §13.5) + eight Added criteria (Proposed) | 1839 | Retained + Added/Proposed (per status) | 209 | T-102 | §1 row (5) + A-004 | — |
| `07_deployment-and-operations/GOV-1_ownership_governance_postdeploy.md` | CC-5 | GOV-1 | 1.0 | — | Retained + Added; person-level owners [NEEDS DEFINITION] throughout | 1518 | Retained + Added/Proposed (per status) | 210 | T-104 | §1 row (5) + A-004 | — |
| `07_deployment-and-operations/INDEX.md` | CC-8 | INDEX-07 | 1.0 | 2026-09-05 | Added (sprint-1); indexes only; nothing is deployed; every file Proposed/Retained per its own status; person-level owners [NEEDS DEFINITION] throughout (GOV-1); RTO/RPO/DR [NEEDS DEFINITION] (G-09, proposed DEC-23) | 7451 | Added (sprint-1) | 211 | T-714 | §1 row (5) + A-004 | — |
| `07_deployment-and-operations/OPS-1.1_procedures_cc5_delta.md` | CC-5 | OPS-1.1 | 1.1-delta | 2026-09-05 | Added; OPS-1 v1.0 not edited; read OPS-1 through this file. Every procedure below restates an OPS-1 paragraph or a DEPLOY-1 step-2 control as steps with timeout/retry/idempotency/on_fail per Arch §13.6. Where the source … | 13837 | Added (sprint-1) — Proposed | 212 | T-502 | §1 row (5) + A-004 | — |
| `07_deployment-and-operations/OPS-1_operating_procedures.md` | CC-5 | OPS-1 | 1.0 | — | Retained (§1–2) + Added from REG-POSTURE (§3) + Proposed (§4) | 2475 | Retained + Added/Proposed (per status) | 213 | T-103 | §1 row (5) + A-004 | read through OPS-1.1 (CC-5 procedures) |
| `07_deployment-and-operations/SEC-1_security_privacy_compliance.md` | CC-5 | SEC-1 | 1.0 | — | Retained (Arch §11.1) + Added (REG-POSTURE) — no new claims | 2205 | Retained + Added/Proposed (per status) | 214 | T-105 | §1 row (5) + A-004 | read with SEC-2 (threat model; encryption/SBOM/CAPA cross-refs) |
| `07_deployment-and-operations/SEC-2_threat-model_and_data-flow.md` | CC-5 | SEC-2 | 1.0 | 2026-09-05 | Proposed; derived from Arch §11 (Retained) + SEC-1 (Retained/Added) + REG-POSTURE v1.2 §4.3–§4.4 (ADVISORY_ONLY); no new regulatory claim. Documents the boundaries MT2 §1(7) says are never weakened — it does not change t… | 14581 | Added (sprint-1) — Proposed | 215 | T-503 | §1 row (5) + A-004 | — |

## §3 Precedence note

For sequencing, **EXEC-1 EX-1/EX-5 govern**: DEPLOY-1's steps 0a–5 resolve to RUN-0..4 through `DEPLOY-1.1_run-map_delta.md` D-1 (in force as the working calendar when DEC-22 closes). For content, DEPLOY-1's sources (REG-POSTURE §7 phases, Arch §11.2 exits, MT2) govern and the run rows are extensions. The five v1.0 files carry no `date` field (00_MANIFEST dates them 2026-09-01); the three sprint-1 deltas carry dates.

## §4 Honesty line

Nothing is deployed; no code beyond skeleton READMEs is claimed (00_MANIFEST §4.4). The OPS-1.1 procedures for the regulated controls (PROC-10..12) are stubs whose SLAs are `[NEEDS DEFINITION]`; SEC-2 records encryption-in-transit as a gap, not a control; DEC-03 (substrate), DEC-07 (patient surface), DEC-08 (Observer cadence) and DEC-22 (calendar) are Open.

## §5 Self-audit (run 2026-09-05)

- File count in the table = files on disk under `07_deployment-and-operations/` (excluding `.DS_Store`): **9** = 9 — PASS.
- Every path in the table exists — PASS (9/9 at generation; this INDEX itself is written by the same run).
- Every HARDEN-1/1.1 row id and HARDEN-3.1 task id in the table resolves in `04_hardening/HARDEN-1.1_coverage_ledger_seed_delta.md` / `HARDEN-3.1_task_register_delta.md` — PASS (ids taken from the same generated data; 0 ABSENT).
- Every cited ID in the three deltas resolves (refcheck, sprint-1) — PASS; `07_/*` v1.0 files byte-identical (CHECKSUMS_BEFORE/AFTER) — PASS.
```
$ ls -l 07_deployment-and-operations
total 144
-rw-r--r--@ 1 ken-lee-arepo  staff  10334 Sep  5 16:04 DEPLOY-1.1_run-map_delta.md
-rw-r--r--@ 1 ken-lee-arepo  staff   3805 Sep  4 05:13 DEPLOY-1_deployment_plan_and_sequencing.md
-rw-r--r--@ 1 ken-lee-arepo  staff   1839 Sep  4 05:13 DEPLOY-2_testing_verification_acceptance.md
-rw-r--r--@ 1 ken-lee-arepo  staff   1518 Sep  4 05:13 GOV-1_ownership_governance_postdeploy.md
-rw-r--r--@ 1 ken-lee-arepo  staff   7451 Sep  5 16:12 INDEX.md
-rw-r--r--@ 1 ken-lee-arepo  staff  13837 Sep  5 16:04 OPS-1.1_procedures_cc5_delta.md
-rw-r--r--@ 1 ken-lee-arepo  staff   2475 Sep  4 05:13 OPS-1_operating_procedures.md
-rw-r--r--@ 1 ken-lee-arepo  staff   2205 Sep  4 05:13 SEC-1_security_privacy_compliance.md
-rw-r--r--@ 1 ken-lee-arepo  staff  14581 Sep  5 15:50 SEC-2_threat-model_and_data-flow.md
```
