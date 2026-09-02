---
doc_id: OPS-1
title: "Operating procedures & implementation instructions"
version: "1.0"
status: "Retained (§1–2) + Added from REG-POSTURE (§3) + Proposed (§4)"
---
# 1. Change flow (Retained, extended)
All changes are Primer I events under the I8 binding table (authoritative numbers there). Proposed new classes (I10 annex): fabric/argument-schema (spine PR; consumers break visibly) · GenericArgument compilation release (registry-gateway class, pharmacist+clinician CODEOWNERS) · deviation-taxonomy · register-render contract (RRI-1 test mandatory) · FML membership change (AF-5-governed per FZ-4 — dormant) · GPP capability change = **not a change**: a new device (GPP-14), PR halted.
# 2. Build-execution model (Retained)
IMPL sessions dispatch from R26; Observer adjudicates level exits from registers only (never corpus content; adjudications touching corpus content are void); validate_build_plan.py on every ECOSYSTEM-V2 block change; namespace law extended {FAB, UIC, UIP, GPP} (Proposed).
# 3. Regulated-work model (Added — REG-POSTURE §5–6, faithful)
Jira = regulated work-item tracker; Ketryx free tier from the Ketryx schema (KTX-001), strict risk (KTX-011), minimal V-model (KTX-010); free tier ⇒ tool validation carried in-house until the GATE-003 tier decision (WATCH-REG-004). Nimbalyst: pre-regulatory authoring surface only; **no Jira shim** (a translator between two things already sharing git adds a validated-tool obligation and breaks provenance); promotion into the regulated system is a deliberate human act landing as a commit or Jira issue; PostHog telemetry disabled before anything non-synthetic; diff-pane approvals count only when they land as commits/CI artifacts; if Nimbalyst enters the authoring path it becomes a versioned tool (RECON row or ASSUME — also the IEC 62304 §5.1.4 answer). Observer-independence clauses stay mechanism-neutral, not vendor-named.
# 4. Integrator instructions (Proposed)
Read in MANIFEST order (FFC → MIF → wings → CEC → faces → UIs → LEG → **ANT last and always**). Author additions as appends only (X1). Namespace every new ID; census it. Flag every proposed clinical number for sign-off exactly as the §-8 layers already do. Between volumes, MAK-FFC governs; on regulatory content, REG-POSTURE governs; on defaults, bindings are law (LS-1). When two documents disagree and no precedence rule speaks: record both verbatim, escalate (MT2 §6) — never pick silently.
