---
doc_id: HARDEN-2
title: "Hardening SPEC — per document class (the /spec artifact of the MT2 pass)"
version: "1.0"
date: "2026-09-01"
status: "Proposed — this SPEC is itself an artifact of the pass (MT2 §2.2) and gets its own R29 row; NOT yet executed"
---

# Trigger
This SPEC applies whenever the MT2 pass processes an artifact of one of the classes below. "When appropriate" does not appear in this document by design.

# Universal exit bar (every class)
An artifact is HARDENED only when, with captured evidence: (1) explicit triggers; (2) deterministic, ordered, testable steps; (3) exit criteria with named evidence artifacts; (4) failure handling for malformed input, failed steps, missing dependencies; (5) anti-rationalization coverage written into the artifact; (6) every cross-reference resolves (IDs per Arch §13.3 namespaces + MAK families per their MANIFEST); (7) every declared boundary verified intact (corpus firewall; five-gate/evaluator path; GPP capability wall; scoring-store separations); (8) safety logic closed — no unhandled escalation/red-flag/safety-netting branch; plus the pack's `references/definition-of-done.md` bar and the artifact-class bar below. Mechanical-check outputs are pasted into the R29 row; "checks pass" without output is a directive violation (MT2 §5).

# Class bars
| Class | Members | Class-specific bar | Mechanical checks available |
|---|---|---|---|
| CC-1 Primers + execution layers | Primer 0, A–L, variants, harness, annex, + their new §-10/§-11 annexes | ten execution fields present and non-empty; §-8 numbers still flagged for clinical sign-off; §-9 blocks untouched; annex additive (diff shows appends only) | `validate_build_plan.py` fragment checks; link/ID resolution; git diff append-only proof |
| CC-2 Architecture + registers | Arch (+§14), register schemas, RoR rows | register laws §12.1 hold for every proposed row; opening levels named; mutability declared; join-key field present | schema validation of R29/R30 JSON; ID census |
| CC-3 Mākoha corpus volumes | 15 corpus-md + MANIFEST | cross-walk rows verified against live CDSS anchors; consolidation volumes retire nothing; RFC 2119 usage consistent; ID census matches Appendix A of each volume | census diff; anchor grep; link resolution |
| CC-4 Regulatory artifacts | MAK-ANT/REG-POSTURE extracts, R30 seed | every OPEN item names its attesting party and blocked gate; no ASSUME-REG-* closable internally; WATCH cadences present | R30 schema validation |
| CC-5 Workflows/orchestration | WF-*/EVT-* blocks, OPS-1 procedures | every step carries timeout/retry/idempotency/on-fail (the Arch §13.6 pattern, generalized); events name producer/consumers/delivery/dedup | YAML lint; field-presence check |
| CC-6 Browser-borne | cdss_diagrams.html, cdss_diagrams_v2.html, 16 artifacts-html | renders without console errors; mermaid sources parse; links resolve; accessibility-checklist applied | browser-testing-with-devtools; /webperf |
| CC-7 Contracts/schemas | argument, deviation, render-invariance, coded-finding provenance fields | JSON Schema valid; example instances validate; breaking-change note per Arch §10 consumer-break rule | jsonschema validation runs |
| CC-8 The directive + this SPEC + HARDEN-3 + MET set | self-referential class, hardened LAST | the pass's own artifacts clear the same bar; C-11 reconciliation recorded | as CC-1/CC-2 |

# Anti-rationalization coverage (portfolio-specific rows added to MT2 §4)
| Temptation | Foreclosure |
|---|---|
| "The 15 Mākoha volumes were just written; they're clean." | Recency is not verification (MT2: in-use/tenure proves nothing). Each volume gets its own row, census diff, and anchor check |
| "The annexes were authored together; harden one, batch the rest." | Batching is sampling — prohibited. Each annex's cross-references differ (different MAK families, registers, DEC rows) |
| "Corpus files can't be opened from dev, so mark them HARDENED by proxy." | Prohibited. They are hardened inside the corpus account by the evaluation-role holder; aggregates exported via R28; a row without in-account evidence is ESCALATED, not HARDENED |
| "The relabel is obviously right; apply it now everywhere." | ASSUME-REG-002 is externally attested only. Until then: deprecation notices, never deletions |

# Stop-the-line (instantiated)
MT2 §6 verbatim, plus MET-1 §9.4's five portfolio rules: corpus-credential grant, gate/evaluator bypass, μ-as-confidence render, GPP boundary extension, internal ASSUME-REG closure — each halts the artifact and escalates.
