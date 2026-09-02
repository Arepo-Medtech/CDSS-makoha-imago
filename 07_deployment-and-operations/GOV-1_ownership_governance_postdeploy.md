---
doc_id: GOV-1
title: "Ownership, governance, maintenance & post-deployment model"
version: "1.0"
status: "Retained + Added; person-level owners [NEEDS DEFINITION] throughout"
---
Retained: register owners per Arch §12.2; Observer prohibitions (§13.7) and cadence (per-level minimum; quarterly-from-L4 proposed, DEC-08); PR gateways with pharmacist+clinician CODEOWNERS; freshness monitor + correction pipeline loops (Arch §5); negative audits as scheduled jobs from L5 (now covering hardening rows and REG-* IDs on ratification).
Added/Proposed: R29 owner = spine, sole writer = the pass; R30 owner = governance, closure by external attestation only; regulatory owner for Phase 0 [NEEDS DEFINITION]; owners for cdss-fabric/-compiler/-ui-* [NEEDS DEFINITION] (DEC-09); MT2 operator [NEEDS DEFINITION] (DEC-10); corpus custodian confirmation for DEC-12.
Post-deployment: post-market surveillance + adverse-event readiness operating from GATE-003 (TASK-REG-017; OBL-002 applies even under exempt supply per REG-FIND-005 — relevant to the GPP channel); WATCH-REG-001..005 cadences run standing; in-clinic model monitoring (higher-class branch/L) is first-class production telemetry beside Security Hub (Arch §11.1 T5); MT2 remains standing — every new instruction-bearing artifact opens an R29 row, and the CI ratchet keeps verification from silently coming back off (directive §7(4)/§7(5)'s "name the ratchet" statement is drafted at pass close-out, per class, as targets in HARDEN-2 — not achievements).
