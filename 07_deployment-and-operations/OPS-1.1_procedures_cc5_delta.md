---
doc_id: OPS-1.1
title: "OPS-1.1 — operating procedures re-expressed in CC-5 form (trigger · ordered steps · exit evidence · on_fail · owner)"
version: "1.1-delta"
date: "2026-09-05"
status: "Added; OPS-1 v1.0 not edited; read OPS-1 through this file. Every procedure below restates an OPS-1 paragraph or a DEPLOY-1 step-2 control as steps with timeout/retry/idempotency/on_fail per Arch §13.6. Where the source is silent the value is [NEEDS DEFINITION] and named as such — nothing is invented. Regulatory content stays ADVISORY_ONLY; no vendor-named Observer clause is introduced (OPS-1 §3)."
supersedes: "nothing — OPS-1 v1.0 is preserved verbatim beside this file"
applies_to: "07_deployment-and-operations/OPS-1_operating_procedures.md"
change_policy: "Additive delta per the MET-1.1 pattern."
req_prefix: PROC
req_count: 12
form: "Arch §13.6 orchestration-hook pattern generalised (HARDEN-2 CC-5 bar): every step carries {timeout, retry, idempotent-by, on_fail}"
---

# OPS-1.1 — procedures in CC-5 form

HARDEN-2 CC-5 requires that "every step carries timeout/retry/idempotency/on-fail".
OPS-1's four sections are prose. This delta gives each OPS-1 paragraph a procedure
identifier `PROC-nn` with the four fields on every step (D-1), and adds procedure
**stubs** for the regulated controls DEPLOY-1 step 2 names (D-2). Stubs carry the
fields with `[NEEDS DEFINITION]` values where OPS-1 and REG-POSTURE are silent: a
missing value is stated, never guessed.

Field grammar (per step): `{timeout, retry: {max, backoff}, idempotent: by <key>, on_fail: <action>}`.

## D-1 — OPS-1 §1–§4 as procedures

### PROC-01 — Change intake (OPS-1 §1 "All changes are Primer I events under the I8 binding table")
- **Trigger:** a PR opens against any repository in REPO-MAP.
- **Steps:**
  1. Classify the change against the I8 binding table (authoritative numbers there) and the OPS-1 §1 proposed classes (fabric/argument-schema · GenericArgument compilation release · deviation-taxonomy · register-render contract · FML membership change · GPP capability change) `{timeout: 10m, retry: {max: 1, backoff: none}, idempotent: by PR head SHA, on_fail: label PR UNCLASSIFIED and block merge}`
  2. If class = GPP capability change → **not a change**: a new device (GPP-14); halt the PR `{timeout: n/a, retry: none, idempotent: yes, on_fail: n/a — halting is the outcome}`
  3. Run the class-mapped mechanisms (I8) `{timeout: per I8 mechanism, retry: {max: 1}, idempotent: by artifact hash, on_fail: PR blocked; adjudication record required (R12)}`
- **Exit evidence:** CI status + I8 class label on the PR; adjudication record in R12 where required.
- **Owner:** repo owner per REPO-MAP (DEC-09) [NEEDS DEFINITION]. **Source:** OPS-1 §1; Primer I I8/I10; GPP-14.

### PROC-02 — Spine contract release (OPS-1 §1 "fabric/argument-schema (spine PR; consumers break visibly)")
- **Trigger:** a PR touches `cdss-spine/contracts/**`.
- **Steps:** 1 schema diff `{timeout: 15m, retry: {max: 1}, idempotent: yes, on_fail: PR blocked}` → 2 consumer-matrix build across all repos (Arch §10: breaks are visible, never silent) `{timeout: 60m, retry: 1, idempotent: by pin-set hash, on_fail: PR blocked with the consumer list}` → 3 breaking-change note per Arch §10 attached `{timeout: n/a, retry: n/a, idempotent: yes, on_fail: PR blocked}`.
- **Exit evidence:** WF-SPINE-2 record (Arch §13.6); consumer-matrix output attached to the PR.
- **Owner:** Architecture owner (CODEOWNERS `cdss-spine/contracts`). **Source:** OPS-1 §1; Arch §10, §13.6 WF-SPINE-2.

### PROC-03 — GenericArgument compilation release (OPS-1 §1 "registry-gateway class, pharmacist+clinician CODEOWNERS")
- **Trigger:** compiler emits a GenericArgument bundle for release.
- **Steps:** 1 bundle enters through the registry PR gateway `{timeout: 24h for review, retry: none, idempotent: by bundle hash, on_fail: bundle rejected, not queued}` → 2 pharmacist + clinician CODEOWNERS approval `{timeout: [NEEDS DEFINITION — review SLA], retry: none, idempotent: yes, on_fail: no release}` → 3 five-gate chain (D8) `{timeout: 15m, retry: {max: 2}, idempotent: by content hash, on_fail: refuse; decision log R11}`.
- **Exit evidence:** signed bundle in registry; R11 decision-log entry. **Owner:** registry owner; CODEOWNERS. **Source:** OPS-1 §1; Arch §14.2; Primer D.

### PROC-04 — Deviation-taxonomy change (OPS-1 §1)
- **Trigger:** PR changes the reason taxonomy CONTRACT-DEV-1 consumes.
- **Steps:** 1 taxonomy diff `{timeout: 10m, retry: 1, idempotent: yes, on_fail: blocked}` → 2 re-validate historical Deviation objects against the new taxonomy (append-only: superseding mapping, never rewrite) `{timeout: 60m, retry: 1, idempotent: by taxonomy version, on_fail: blocked; SPINE-4 corrections supersede}`.
- **Exit evidence:** taxonomy version bump + mapping record. **Owner:** [NEEDS DEFINITION — DEC-02]. **Source:** OPS-1 §1; SPINE-8; SPINE-4.

### PROC-05 — Register-render contract change (OPS-1 §1 "RRI-1 test mandatory")
- **Trigger:** PR changes any renderer or the narration capability.
- **Steps:** 1 run CONTRACT-RRI-1 test spec pairwise over three faces `{timeout: 30m, retry: {max: 1}, idempotent: by fixture set hash, on_fail: hard failure (DEPLOY-2 §3)}` → 2 attach ADDED/REMOVED/REWEIGHTED lists `{timeout: n/a, retry: n/a, idempotent: yes, on_fail: no verdict → blocked}`.
- **Exit evidence:** RRI verdict with three empty lists. **Owner:** face repo owners (DEC-09). **Source:** OPS-1 §1; CONTRACT-RRI-1_render-invariance_test-spec.md; DEPLOY-2 §3.

### PROC-06 — FML membership change (OPS-1 §1 "AF-5-governed per FZ-4 — dormant")
- **Trigger:** none while DEC-05 is Open (dormant). **Steps:** 1 refuse `{timeout: n/a, retry: none, idempotent: yes, on_fail: n/a}`. **Exit evidence:** refusal logged. **Owner:** Corpus owner + clinical review (DEC-05). **Source:** OPS-1 §1; MAK-DOT FZ-4; DEC-05.

### PROC-07 — IMPL dispatch and Observer adjudication (OPS-1 §2)
- **Trigger:** a level-exit claim or an IMPL session start.
- **Steps:** 1 dispatch from R26 `{timeout: n/a, retry: n/a, idempotent: by R26 row, on_fail: no dispatch without a row}` → 2 `validate_build_plan.py` on every ECOSYSTEM-V2 block change `{timeout: 15m, retry: 1, idempotent: yes, on_fail: blocked — PENDING-VALIDATOR until the script exists (00_MANIFEST §4.4)}` → 3 Observer adjudicates from registers only `{timeout: per DEC-08 cadence, retry: none, idempotent: by register snapshot, on_fail: adjudication touching corpus content is VOID}` → 4 namespace check {FAB, UIC, UIP, GPP} `{timeout: 5m, retry: 1, idempotent: yes, on_fail: blocked}`.
- **Exit evidence:** R26/R27 rows; validator output. **Owner:** Architecture owner (DEC-08). **Source:** OPS-1 §2; Arch §13.7, §13.8, §14.4.

### PROC-08 — Regulated work-item tracking and tool validation (OPS-1 §3, faithful to REG-POSTURE §5–§6)
- **Trigger:** GATE-000 passed (do not configure regulated tooling before — DEPLOY-1 step 0b).
- **Steps:** 1 Jira as regulated tracker; Ketryx from the Ketryx schema (`KTX-001`), strict risk (`KTX-011`), minimal V-model (`KTX-010`) `{timeout: [NEEDS DEFINITION — configuration sprint], retry: n/a, idempotent: by KTX row verified, on_fail: KTX row stays OPEN}` → 2 free tier ⇒ tool validation in-house until the GATE-003 tier decision (`WATCH-REG-004`, `STD-013`) `{timeout: standing, retry: n/a, idempotent: by validation record, on_fail: regulated use blocked}` → 3 Nimbalyst: pre-regulatory authoring only; **no Jira shim**; promotion is a deliberate human act landing as a commit or Jira issue `{timeout: n/a, retry: none, idempotent: by commit/issue id, on_fail: promotion void}` → 4 PostHog telemetry disabled before anything non-synthetic `{timeout: before GATE-002, retry: n/a, idempotent: yes, on_fail: GATE-002 blocked}` → 5 diff-pane approvals count only as commits/CI artifacts `{timeout: n/a, retry: none, idempotent: by commit/CI artifact id, on_fail: approval not counted}` → 6 if Nimbalyst enters the authoring path → versioned tool (RECON row or ASSUME; IEC 62304 §5.1.4) `{timeout: n/a, retry: n/a, idempotent: by RECON/ASSUME id, on_fail: authoring path blocked}`.
- **Exit evidence:** KTX rows verified; tool-validation records; RECON/ASSUME row where item 6 fires. **Owner:** Regulatory owner [NEEDS DEFINITION — G-09]. **Source:** OPS-1 §3; REG-POSTURE §5.3, §6.1–6.3; STD-013; WATCH-REG-004.

### PROC-09 — Integrator instructions (OPS-1 §4)
- **Trigger:** an author adds to any Imago folder or corpus volume.
- **Steps:** 1 read in MANIFEST order (FFC → MIF → wings → CEC → faces → UIs → LEG → ANT last) `{timeout: n/a, retry: n/a, idempotent: yes, on_fail: authoring without the read is a §4 violation}` → 2 append only (X1) `{timeout: n/a, retry: none, idempotent: by checksum bookend, on_fail: revert; DEF row proposed}` → 3 namespace every new ID; census it `{timeout: n/a, retry: n/a, idempotent: by census, on_fail: STALE-COUNT finding}` → 4 flag every proposed clinical number for sign-off `{timeout: n/a, retry: none, idempotent: by §-8 flag census, on_fail: CHAIN-BREAK}` → 5 precedence: MAK-FFC between volumes; REG-POSTURE on regulatory content; bindings are law (LS-1) `{timeout: n/a, retry: none, idempotent: by precedence rule cited, on_fail: unresolved → step 6}` → 6 disagreement with no precedence rule → record both verbatim, escalate (MT2 §6) `{timeout: n/a, retry: none, idempotent: by escalation record id, on_fail: n/a — escalation is the outcome}`.
- **Exit evidence:** checksum bookends; census; escalation record. **Owner:** Manifest owner [NEEDS DEFINITION]. **Source:** OPS-1 §4; 03_ MANIFEST; MT2 §6.

## D-2 — procedure stubs for the DEPLOY-1 step-2 regulated controls (fields present; values [NEEDS DEFINITION] where the source is silent)

### PROC-10 — Gated regulated pipeline split from synthetic push-to-deploy (`TASK-REG-010`) and SBOM → Ketryx (`TASK-REG-011`)
- **Trigger:** GATE-001 passed; before any non-synthetic input (GATE-002 line).
- **Steps:** 1 split pipelines: synthetic push-to-deploy vs gated regulated `{timeout: [NEEDS DEFINITION], retry: [NEEDS DEFINITION], idempotent: by pipeline definition hash, on_fail: regulated pipeline does not exist → GATE-002 blocked}` → 2 signed SBOM (Syft/CycloneDX) per artifact manifest → R3 → Ketryx SOUP item (`KTX-*` per REG-POSTURE §6.5; `OBL-004`) `{timeout: per build, retry: {max: 2}, idempotent: by artifact digest, on_fail: build fails; no artifact promoted}`.
- **Exit evidence:** two pipeline definitions in `cdss-evalstack`; SBOM attached to every manifest; Ketryx SOUP entries. **Owner:** Security owner [NEEDS DEFINITION — G-09]. **Source:** DEPLOY-1 step 2; Arch §11.1 T1+2; REG-POSTURE §6.5; OBL-004.

### PROC-11 — Vulnerability handling, CVSS and CAPA (`TASK-REG-012`); supplier assessments (`TASK-REG-013`)
- **Trigger:** any vulnerability disclosure or monitoring hit (ISO/IEC 29147/30111, `STD-009`); any new supplier or annually.
- **Steps:** 1 triage + CVSS score `{timeout: [NEEDS DEFINITION — SLA by severity], retry: n/a, idempotent: by CVE/advisory id, on_fail: escalate to security owner}` → 2 CAPA record regardless of risk outcome (`OBL-008`) `{timeout: [NEEDS DEFINITION], retry: n/a, idempotent: by CAPA id, on_fail: OBL-008 breach logged}` → 3 supplier assessment with contractual thresholds (`OBL-005/006`; Baseten-or-substrate, AWS, third-party AI providers per `OBL-013`) `{timeout: [NEEDS DEFINITION], retry: n/a, idempotent: by supplier + period, on_fail: supplier not approved}`.
- **Exit evidence:** CAPA register entries; supplier assessment records. **Owner:** Security owner [NEEDS DEFINITION]. **Source:** DEPLOY-1 step 2; REG-POSTURE §4.4 OBL-005/006/008/013; SEC-1.

### PROC-12 — Usability engineering ×3 surfaces (`TASK-REG-014`) and post-market / adverse-event readiness (`TASK-REG-017`, `OBL-002`)
- **Trigger:** `TASK-REG-014` — each surface's first clinician-visible release (patient last but never skipped); `TASK-REG-017` — from GATE-003, operating before any supply.
- **Steps:** 1 IEC 62366-1 use-related risk analysis per surface (`STD-004`) `{timeout: [NEEDS DEFINITION], retry: n/a, idempotent: by surface + version, on_fail: surface not released}` → 2 adverse-event intake → assessment → TGA report (`OBL-002`; Medsafe `NZ-OBL-007` in NZ) `{timeout: [NEEDS DEFINITION — statutory reporting windows to be confirmed by counsel], retry: n/a, idempotent: by event id, on_fail: escalate to regulatory owner}` → 3 recall capability incl. remote disablement (`NZ-TASK-009` tabletop exercise as the evidence pattern) `{timeout: [NEEDS DEFINITION], retry: n/a, idempotent: by exercise record, on_fail: supply blocked}`.
- **Exit evidence:** usability files ×3; post-market SOPs; tabletop recall record. **Owner:** Regulatory owner; Operations owner [NEEDS DEFINITION]. **Source:** DEPLOY-1 steps 2 and 4; REG-POSTURE §4.4 OBL-002; REG-NZ v1.1 §8 NZ-TASK-009; STD-004.

## Census and self-audit (run 2026-09-05)

- Census: PROC-01..PROC-12 = 12 = `req_count`. D-1 = 9 procedures covering OPS-1 §1 (6 classes → PROC-01..06), §2 (PROC-07), §3 (PROC-08), §4 (PROC-09); D-2 = 3 stubs covering `TASK-REG-010..014` and `TASK-REG-017`.
- Field-presence check (`11_prompts/runs/2026-09-05_sprint-1/tools/proc_fields.py`, sprint-1): every step line carries `timeout`, `retry`, `idempotent`, `on_fail` — PASS (0 steps lacking a field; output in `11_prompts/runs/2026-09-05_sprint-1/proc_fields.txt`).
- Every PROC cites its OPS-1 § or TASK-REG id — PASS (12/12).
- OPS-1 v1.0 byte-identical — PASS (CHECKSUMS_BEFORE/AFTER).
- No regulatory position asserted; ADVISORY_ONLY carried; no vendor-named Observer clause — PASS.
