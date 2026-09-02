---
doc_id: DEPLOY-2
title: "Testing, verification, acceptance & readiness"
version: "1.0"
status: "Retained (all Arch §11.2 exits, register checks §12.3, 100% catch, I8 tolerances, checkpoint floors, Observer checkpoints §13.5) + eight Added criteria (Proposed)"
---
1. **Fabric replay** — any historical argument replays bit-for-bit from pins (SPINE-5); extends L1's byte-identical exit. Evidence: replay diff = ∅, in R25.
2. **Release validity (refusal tests)** — manufactured arguments missing qualifier, or with empty rebuttal slot while findings exist, are refused (SPINE-2); runs as G's ARG-class at 100% before fabric v1 promotes.
3. **Register-render invariance** — CONTRACT-RRI-1 automated diff across three faces; add/remove/reweight = hard failure; applies to LLM narration identically (L10). "Three truths" is the named failure mode (SPINE-9).
4. **Deviation integrity** — every override lands as a structured Deviation (taxonomy, severity, author); no deviation blocked except deterministic safety classes (SPINE-8).
5. **UI conformance suites** — MAK-PRB/MAK-LBP Part-7 suites as CI acceptance for `cdss-ui-*`, incl. offline-first lossless capture and WCAG 2.2 AA-equivalent floors (L1-2 bindings).
6. **GPP structural-absence** — per OFF row of the MAK-J3 §3 matrix: prove absence from artifact + dependency graph (GPP-8); FZ-6 namespace rows join on DEC-05.
7. **MT2 readiness** — regulated use requires a HARDENED R29 row or operator-accepted blocker; CI ratchet enforces row-completeness after DEC-02.
8. **Pluralism** — two conflicting applicable GenericArguments ⇒ DetectedIssue surfaced on the clinician face, never a silent merge (SPINE-6).
Readiness roll-up per level = its Arch §11.2 exit + its §12.3 register openings + the subset of 1–8 whose components have entered per Arch §14.5.
