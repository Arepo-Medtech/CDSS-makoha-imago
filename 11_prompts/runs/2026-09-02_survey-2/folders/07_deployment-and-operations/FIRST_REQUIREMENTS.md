# 07_deployment-and-operations — FIRST REQUIREMENTS (queue order)

1. `[5] [P-D-10] [DECISION]` DEC-07 (patient surface, GATE-000), DEC-03 (substrate, GATE-001), DEC-08 (Observer cadence) gate steps 0b–1 (BSQ-0407) — remedy: **HUMAN-ONLY** — Counsel + product; Infra + regulatory; Architecture owner.
2. `[4] [P-D-03] [DEPLOY]` DEPLOY-1 predates EXEC-1; no step→RUN-0..4 mapping, no RUN-0 additions, no owner per step (BSQ-0402) — evidence: `grep -c 'EXEC-1\|RUN-' 07_*/*.md` → 0 ×5 — blocks: RUN-0 week-one board; GATE-000/001 ordering — remedy: write `DEPLOY-1.1_run-map_delta.md` (D-1 mapping table, D-2 owners, D-3 per-step exit/failure, DEC-22 dependency).
3. `[4] [P-D-15] [OPS]` OPS-1 has no procedure in CC-5 form (BSQ-0403) — evidence: 0 timeout/retry/idempotency/on-fail occurrences — blocks: W8 CC-5 bar; GATE-001/002 procedures — remedy: write `OPS-1.1_procedures_cc5_delta.md` (PROC-nn in Arch §13.6 form; stubs for TASK-REG-010..014/017).
4. `[4] [P-D-07] [SEC]` No threat model / data-flow; SEC-1 omits encryption, SBOM, CAPA (BSQ-0404) — blocks: GATE-002; TASK-REG-016 scoping — remedy: write `SEC-2_threat-model_and_data-flow.md` + `09_diagrams/data_flow_v1.mermaid` (STRIDE per boundary; cross-reference table).
5. `[4] [P-D-14] [DEPLOY]` RTO/RPO/DR registered but ownerless (BSQ-0405) — blocks: L5 exit; GATE-004 — remedy: **HUMAN-ONLY: propose DEC-23 (infra owner; RTO/RPO; DR drill protocol)**.
6. `[3] [P-F-02] [INDEX]` No index/briefing; no `date` on any file; no precedence note (BSQ-0401) — remedy: write `07_deployment-and-operations/INDEX.md`.

Dismissed: BSQ-0406 DEPLOY-1 html page (diagram twin exists); BSQ-0408 DEPLOY prompt (covered by PROMPT-SERIES). PRESENT-CONFORMANT ×5 (BSQ-0410..0414).

Folder parity verdict (provisional): **BELOW-PARITY** — P-D-01 date ×5; P-D-08/09 ABSENT ×5; CC-5 FAIL (OPS-1); SEC floor 4/7 topics; chain INDEX/BRIEFING/PRIMER ABSENT, SKELETON PARTIAL.
