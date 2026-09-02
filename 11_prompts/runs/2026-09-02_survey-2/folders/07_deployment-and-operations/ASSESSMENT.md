# 07_deployment-and-operations — ASSESSMENT (Phase 2)

Census: 5 files, 11,842 B. All five read in full.

## 1. Discovery and labels
| Item | Bytes | Label(s) | Why | Load-bearing? |
|---|---|---|---|---|
| `DEPLOY-1_deployment_plan_and_sequencing.md` | 3,805 | DEPLOY (plan) + WORKLIST-adjacent | "three ladders interleaved"; steps 0a–5 with gates | YES crit 2 — cited by 09_ deployment_ladders.mermaid, EXEC-1 EX-1/EX-5, MET-1 §11 |
| `DEPLOY-2_testing_verification_acceptance.md` | 1,839 | DEPLOY (acceptance criteria) | eight Added criteria + readiness roll-up | YES crit 2 — PROMPT-SERIES cites DEPLOY-2 §1–§8 as L-exit tests |
| `OPS-1_operating_procedures.md` | 2,475 | OPS (procedures) | four sections: change flow, build-execution model, regulated-work model, integrator instructions | YES crit 2 — CC-5 class member by name (HARDEN-2 'OPS-1 procedures') |
| `GOV-1_ownership_governance_postdeploy.md` | 1,518 | GOV | ownership + post-deployment | crit 2 — names R29/R30 owners; DEC-08/09/10/12 |
| `SEC-1_security_privacy_compliance.md` | 2,205 | SEC | "limited to supplied + verified material — no new claims" | crit 2 — safety boundaries list (MT2 §1(7)) |

## 2. Presence pass — folder chain
| Link | Applicability | PRESENT / ABSENT | Evidence |
|---|---|---|---|
| P-F-01 BRIEFING | APPLIES (5 classes) | ABSENT (fold into INDEX) | `find 07_* -iname '*brief*'` → none |
| P-F-02 INDEX | APPLIES | ABSENT | `find 07_* -iname '*index*' -o -iname 'manifest*' -o -iname 'readme*'` → none |
| P-F-03 corpus-grade | APPLIES | §3–4 | — |
| P-F-04 PRIMER / runbook | APPLIES — OPS-1 is titled "Operating procedures & implementation instructions" but carries no procedure with the CC-5 fields; the regulated controls DEPLOY-1 step 2 names (TASK-REG-010..014) and the post-market/CAPA procedures (TASK-REG-012/017) have no procedure documents anywhere in 04_–10_ | ABSENT | `grep -ic 'timeout\|retry\|idempot\|on.fail\|rollback' 07_*/*.md` → DEPLOY-1: 2 (rollback prose), others 0; OPS-1 has 4 prose sections, 0 numbered steps |
| P-F-05 LAUNCH PROMPT | APPLIES (small) — the Claude-Code-executable part of DEPLOY-1 (L1 synthetic build) is already PROMPT-P0 + PROMPT-A..L; the rest is human/organisational | PRESENT-by-proxy (PROMPT-SERIES) — no DEPLOY prompt needed | PROMPT-SERIES run order §; DEPLOY-1 step 1 "L1 Glass-Box Core on synthetic scope" |
| P-F-06 ARTIFACT-HTML | APPLIES to DEPLOY-1 (board/regulator-facing ladders) per P-F-06 test | ABSENT — 09_/deployment_ladders.mermaid + cdss_diagrams_v2.html render the ladders (a *diagram* twin exists; a document page does not) | `ls 03_*/artifacts-html | grep -i deploy` → none; 09_/deployment_ladders.mermaid l.1 "IMAGO-4 — Three ladders interleaved (DEPLOY-1)" |
| P-F-07 SKELETON home | APPLIES — SEC-1/OPS-1 CI duties → `cdss-governance` shared actions (Arch §12.3) | PARTIAL — `cdss-governance/` has README + MANIFEST only, **no ci/** (BSQ-0392) | skeleton_summary.json |
| P-F-08 HARDEN rows/tasks | APPLIES | PARTIAL — rows 60–71 "07_ (5)" collapsed; T-100..107 collapsed (BSQ-0104/0006) | HARDEN-1 l.29 |
| P-F-09 00_MANIFEST row | APPLIES | PRESENT (5 = 5) | CENSUS §1 |
| P-F-10 honesty line | APPLIES | PRESENT per file (Retained/Added/Proposed split in each status); no folder line | — |

## 3. Presence pass — document contract
| P-line | DEPLOY-1 | DEPLOY-2 | OPS-1 | GOV-1 | SEC-1 |
|---|---|---|---|---|---|
| P-D-01 | **date ABSENT** (others present) | date ABSENT | date ABSENT | date ABSENT | date ABSENT |
| P-D-02 | PRESENT (Proposed; grounded…) | PRESENT (Retained + eight Added) | PRESENT (Retained/Added/Proposed per §) | PRESENT (+ "[NEEDS DEFINITION] throughout") | PRESENT ("no new claims") |
| P-D-03 precedence | PARTIAL — "tier pipeline never relaxes"; **no statement that EXEC-1 RUN-0..4 now governs its sequence (EX-1/EX-5)** | N/A | PRESENT (§4 precedence rules) | N/A | N/A |
| P-D-04 req declaration | mints steps 0a–5 (unnamed IDs) — ABSENT | mints criteria 1–8 (unnamed) — ABSENT | none | none | none |
| P-D-05 req blocks / sourced rows | PARTIAL — table rows carry gate + content + status; sources inline (TASK-REG, KTX, Arch §11) | PARTIAL — each criterion states evidence + SPINE trace (near-requirement form) but no ID/level | ABSENT — prose | ABSENT — prose (IDs inline) | ABSENT — prose (REG-FIND/OBL inline) |
| P-D-06 Contents | N/A | N/A | N/A | N/A | N/A |
| P-D-07 traceability | PRESENT (inline) | PRESENT | PRESENT | PRESENT | PRESENT (REG-FIND-005..008, OBL, TASK-REG) |
| P-D-08 census | ABSENT | ABSENT ("eight" = 8 ✓ by count) | N/A | N/A | N/A |
| P-D-09 self-audit | ABSENT ×5 | | | | |
| P-D-10 owner + status per row | steps carry Status ✓, **owner ABSENT** | criteria carry evidence ✓, owner ABSENT | N/A | roles named, persons [NEEDS DEFINITION] | N/A |
| P-D-12 placeholders registered | RTO/RPO/DR ↔ G-09 ✓ | — | — | ×4 ↔ DEC-09/DEC-10/DEC-12/G-09 ✓ | — |
| P-D-14 owner | ABSENT per step | ABSENT | ABSENT | PRESENT (roles) | ABSENT |
| P-D-15 execution fields | PARTIAL — gate + status per step; rollback section; **no per-step exit evidence / failure handling**; RTO/RPO undefined | N/A (criteria) | **ABSENT** — CC-5 bar (timeout/retry/idempotency/on-fail) unmet for every procedure | N/A | N/A |
| P-D-16 xrefs | PASS (CENSUS §3 no dangling for 07_) | PASS | PASS | PASS | PASS |

## 4. Measurement pass — class-contract lines (DEPLOY/OPS/GOV/SEC floor)
| Contract line | PASS/FAIL | Evidence |
|---|---|---|
| every step has gate + status | PASS (steps 0a–5; gates GATE-000..004; L4 exit) | DEPLOY-1 table |
| rollback stated | PASS | "Rollback & recovery (Retained + gaps)" |
| RTO/RPO/DR defined or registered as [NEEDS DEFINITION] with owner | PARTIAL — registered (G-09 "Low→rising") but **no owner** on the placeholder | DEPLOY-1 last para; MET-4 G-09 |
| every OPS procedure step carries timeout/retry/idempotency/on-fail (CC-5) | **FAIL** — OPS-1 has no step structure; 0 occurrences | grep → 0 |
| owners named per role | PARTIAL — GOV-1 names roles; persons [NEEDS DEFINITION] ×4 (registered) | GOV-1 |
| SEC covers secrets, access, encryption, SBOM, vuln handling, supplier assessment, incident/CAPA | PARTIAL — secrets ✓ (signing keys), access ✓ (per-env accounts, Organizations), **encryption ✗** (0 mentions in SEC-1; Arch §11.4 l.300 has KMS/object-lock — not carried), **SBOM ✗** (in DEPLOY-1 only), vuln handling ✓ (29147/30111), supplier ✓, incident ✓ thresholds / **CAPA ✗** (DEPLOY-1 only) | grep table above |
| threat model / data-flow diagram SEC can hang from | **ABSENT** | grep 'threat model\|data-flow' → 0 |
| DEPLOY-1 read against EXEC-1 run map (EX-5) | **ABSENT-SECTION** — DEPLOY-1 predates 10_; no delta maps steps 0a–5 → RUN-0..4 | `grep -c 'EXEC-1\|RUN-' 07_*/*.md` → 0 ×5 |
| declared counts equal page | PASS — "eight Added criteria" = 8; "three ladders" = MT2 / regulatory / L-levels ✓ | DEPLOY-2 |
| status honest against the tree | PASS — nothing deployed; consistent with 00_MANIFEST §4.4 "nothing is deployed" | — |
| sibling consistency | PASS on spot checks: DEPLOY-1 step 0b lists TASK-REG-001..004 = REG-POSTURE Phase 0 = EXEC-1 RUN-0 contents (RUN-0 adds TASK-REG-021/022, V1-*, NZ-*) — not a contradiction, an *extension* the DEPLOY-1.1 delta should carry | EXEC-1 RUN table |

## 5. Chain confirmation
CHAIN.md §A/§B 07_ confirmed; correction: P-F-05 is PRESENT-by-proxy (PROMPT-SERIES), not ABSENT; P-F-06 has a diagram twin (09_) but no page.

## 6. Weighting summary
Queue (≥3): BSQ-0401 INDEX-07, BSQ-0402 DEPLOY-1.1 run-map delta, BSQ-0403 OPS-1.1 CC-5 procedures delta, BSQ-0404 SEC-2 threat model + data-flow (+ encryption/SBOM/CAPA cross-refs), BSQ-0405 RTO/RPO/DR definition (HUMAN-ONLY), BSQ-0407 DECISION-PENDING DEC-03/DEC-07. Below: BSQ-0406 DEPLOY-1 html page (2), BSQ-0408 PROMPT-DEPLOY (dismissed), PRESENT rows ×5.

## 7. Validation
rows=13 invalid=0 valid=13
