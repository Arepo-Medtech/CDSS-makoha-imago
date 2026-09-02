---
doc_id: MAK-J3
title: "Addendum J-3 — Guideline-Prompt Profile (GPP): the exempt-tier reserve"
version: "0.9-proposed"
date: "2026-08-29"
series: "Mākoha regulatory fork — Addendum J series"
status: proposed-normative-draft
naming_note: "J-3 designation is provisional pending ratification against the existing Addendum J-1 (deterministic runtime) / J-2 (ML runtime) conventions — an open naming decision consistent with the programme's IMPL-rename precedent."
normative_language: RFC-2119 (MUST / SHOULD / MAY)
req_prefix: GPP
req_count: 16
realizes: "MAK-FFC XC-2 (MAY): 'Ship a scoped guideline-prompt profile … provided the profile boundary is enforced in code, not policy.'"
subordinate_to:
  - "MAK-FFC XC-1 (classification honesty) — J-3 never substitutes for the classified track; it is the lawful floor beside it"
  - "MAK-FFC SPINE-1..9 — the shared spine applies in full inside the profile"
depends_on:
  - "MAK-FFC v1.0 (The Four Faces Corpus)"
  - "MAK-ELSM v1.0 (Execution Layer Sourcing Map)"
regulatory_anchors:
  - "TGA, Understanding clinical decision support system software regulation (guidance, rev. 7 Oct 2025) — exemption criteria (a)(b)(c), Schedule 4 Part 2, Therapeutic Goods (Medical Devices) Regulations 2002"
  - "TGA, Excluded software: interpretation of exclusion criteria (Jul 2024)"
  - "FDA, Clinical Decision Support Software — revised final guidance (6 Jan 2026), FD&C Act §520(o)(1)(E) Non-Device CDS criteria"
  - "EU MDR 2017/745, Rule 11 (no equivalent carve-out)"
---

<!-- LLM USAGE CONTRACT (additive)
1. GPP-n blocks are NORMATIVE for the J-3 build target only; they add to, and never
   relax, MAK-FFC requirements. Where a GPP-n narrows a MAK-FFC requirement's scope
   inside the profile, the narrowing is stated explicitly; absence of narrowing means
   MAK-FFC applies unmodified.
2. The Capability Matrix (§3) is normative: ON means compiled and enabled; OFF means
   STRUCTURALLY ABSENT from the build artifact (GPP-8), not disabled by flag.
3. Regulatory quotations are paraphrase-faithful to the anchored guidance versions in
   the frontmatter; re-verify anchors before any submission or supply decision.
4. Legal-review flags (⚑) mark boundary questions this document deliberately does not
   decide; an LLM must never resolve a ⚑ by generation.
END LLM USAGE CONTRACT -->

# Addendum J-3 — Guideline-Prompt Profile (GPP)

**The exempt-tier reserve: a code-enforced configuration of the shared Mākoha codebase that supplies only what the TGA's CDSS exemption permits — guideline prompts, alerts, reminders, and pathway recommendations to health professionals, on a transparent, independently verifiable basis — while every classification-attracting capability is structurally absent from the build.**

## 1 — Purpose and position in the J-fork

The J-fork to date holds two branches: **J-1** (deterministic runtime, classified SaMD track) and **J-2** (ML runtime, classified, higher classification posture). Both plan for ARTG inclusion per XC-1, because Mākoha's diagnostic engine is diagnosis-contributing and the TGA states plainly that an AI-enabled CDSS will not meet the exemption criteria.

**J-3 adds the lawful floor beside them.** It is not a lesser Mākoha; it is the same spine — justification fabric, guideline compiler, versioning, ledger, deviation machinery — shipped as a distinct build artifact whose inference plane contains nothing but ratified published guidelines evaluated deterministically. Three strategic functions:

1. **Market entry** where classification timelines or economics block deployment — including low-resource jurisdictions (XC-3) where guideline-prompt support is itself the north-star payload.
2. **Evidence accumulation**: every GPP deployment feeds the fabric with real usage, deviation, and guideline-gap evidence that seeds J-1/J-2 validation (GPP-13).
3. **Regulatory hedge**: if classified-track timelines slip, the programme still ships something lawful, useful, and spine-true.

J-3 is subordinate to XC-1's honesty posture. It is never marketed, configured, or quietly extended to do classified work under an exempt label. The boundary is enforced in code (GPP-8..11), and crossing it is a new device, not an update (GPP-14).

## 2 — Regulatory basis, mapped to design

### 2.1 The TGA two-off-ramp structure

The TGA guidance distinguishes **excluded** software (not a regulated medical device at all) from **exempt** CDSS (a medical device, exempt from ARTG inclusion, but still subject to TGA oversight). J-3 targets the **exempt** tier: it accepts the residual obligations (§5) in exchange for supplying without ARTG inclusion. The guidance's own scope sentence for the exempt tier is J-3's product definition:

> Exempt CDSS "may include software that collects, performs simple analysis, and displays data from EMRs, EHRs or CISs" and "may provide prompts, alerts, reminders, and recommendations to help health professionals apply evidence-based clinical guidelines or hospital procedures."

And its own warning is J-3's boundary: CDSS performing "more advanced analysis and functions such as specifying a diagnosis or treatment for a patient" is unlikely to qualify.

### 2.2 The three exemption criteria as design constraints

| Criterion (TGA, Sch. 4 Pt 2) | Design consequence in J-3 |
|---|---|
| **(a)** Sole purpose: providing or supporting a *recommendation to a health professional* about preventing, diagnosing, curing or alleviating disease. A recommendation means advice to take steps, gather inputs, or follow a course of action, or general information — *not* making a diagnosis, providing new diagnostic information, or specifying/customising a treatment. | Recommendations render to authenticated health professionals only (GPP-4). Claim-type whitelist excludes diagnosis, differential, risk-score, treatment-customization, screening, monitoring — structurally, not by flag (GPP-5). Patient face reduces to intake, consent, logistics (GPP-4). |
| **(b)** Not intended to directly process or analyse a medical image or a signal from another medical device (incl. IVD). Displaying EMR-retrieved values can be acceptable; interpreting them, or displaying for patient monitoring, is not. | Device-originated data is refused at the API boundary; no imaging, waveform, or sensor endpoints exist in the build; EMR-retrieved values display without interpretation or trending-for-monitoring (GPP-6). Anidra-class RPM ingestion is a J-1/J-2 capability only. |
| **(c)** Not intended to replace clinical judgement: must be transparent (no proprietary AI generating recommendations), allow the professional to easily understand and verify the recommendation's accuracy, and clearly reference the logic, guidelines, process or evidence — information the professional cannot independently verify fails the criterion. | The justification fabric satisfies this by construction: warrant → published guideline clause with citation and version; backing → evidence tier and source. J-3 adds the release gate: a recommendation whose basis is not reproducible from cited public sources MUST NOT release (GPP-7). No learned parameters in the inference path — the TGA's note that AI-enabled CDSS cannot qualify is honoured by structural absence (GPP-7/8). |

### 2.3 Jurisdiction map (GPP-15)

| Jurisdiction | Mechanism | J-3 posture |
|---|---|---|
| **Australia (TGA)** | CDSS exemption, criteria (a)(b)(c); notification-based supply | Primary target; this addendum's design basis |
| **USA (FDA)** | Non-Device CDS, §520(o)(1)(E), four criteria per revised final guidance (6 Jan 2026): revision permits *singular* recommendations where clinically appropriate; strengthens criterion 4 (basis from "well-understood and accepted sources" — clinical guidelines, peer-reviewed literature — presented for independent review); relocates time-critical decision-making under criterion 4; offers no AI-specific analysis | J-3's transparent guideline-referenced basis is precisely criterion 4's demand; avoid time-critical deployment contexts (§4 edge cases); re-map before any US supply |
| **EU (MDR)** | Rule 11 — software providing information used for diagnostic/therapeutic decisions is class IIa minimum; **no exempt-tier equivalent** | J-3 does not confer an EU pathway; EU supply follows the classified track |
| **Low-resource jurisdictions** | National regimes vary; WHO SMART Guidelines alignment (PF-7/XC-4) eases national adaptation and approval | Assess individually; the exemption logic does not transfer automatically |

## 3 — Capability matrix (normative)

ON = compiled, enabled, conformance-tested. OFF = structurally absent from the build artifact and its dependency graph (GPP-8). ⚑ = legal-review flag, undecided here.

| Capability | J-3 GPP | Notes |
|---|---|---|
| Justification fabric, ledger, version pinning (SPINE-1..5) | ON | Full spine; arguments carry `profile: GPP` stamps (GPP-11) |
| Guideline Compiler → GenericArgument (EN-3) | ON | Warrant type restricted to `guideline-rule` (GPP-9) |
| Deterministic Evaluator (SPINE-7) | ON | The only release path; refuses probabilistic qualifiers (GPP-9) |
| Clinician face: guideline prompts, alerts, reminders, pathway recommendations, information summaries | ON | Claim-type whitelist (GPP-5) |
| Deviation Composer + deviation ledger (SPINE-8, CF-3) | ON | Recording departure from a prompt is documentation, not diagnosis (GPP-16) |
| Auditor face read model, compliance projector, exports (AF-1..3, AF-7) | ON | Internal QA and conformity evidence; not a clinical function |
| Alert Governor (CF-5) | ON | Suppression rules remain ratified GenericArguments |
| Patient face: intake instruments, consent, logistics (PF-1, PF-4 consent subset) | ON | No patient-directed clinical recommendations (GPP-4) |
| Bayesian Differential Service | OFF | Diagnosis-contributing; defeats criteria (a) and (c) |
| Conformal Wrapper | OFF | Nothing probabilistic to qualify; qualifier type = `applicability` only (GPP-9) |
| LLM runtime (all Class 4+ uses) | OFF | TGA: AI-enabled CDSS will not meet the exemption; authoring-time LLM use (EN-6 Classes 1–3) remains permitted *outside* the supplied artifact, with human ratification |
| RPM / device-signal / imaging ingestion (Anidra-class, ECG, SpO₂ streams) | OFF | Criterion (b); refused at API boundary (GPP-6) |
| Diagnosis, differential, risk-score, screening, triage-urgency scoring claim types | OFF | Unrepresentable types in GPP build (GPP-5); triage scoring derived from patient data is new diagnostic information |
| Treatment customization (patient-specific dose calculation, regimen tailoring) | OFF | Criterion (a) "specifying or customising a particular treatment" |
| Verbatim display of published guideline dose tables (uninterpreted) | ⚑ | Arguably guideline content, not customization — obtain legal reading before enabling |
| Patient-monitoring displays / trending of EMR vitals | OFF | Criterion (b) explanation disqualifies display-for-monitoring |
| Values & Priorities engine weighting (PF-3 mappings) | OFF | Weighting recommendations by patient values is customization; elicitation-and-display MAY remain ⚑ |

## 4 — Requirements

### GPP-1 (MUST)
**Statement:** J-3 is a distinct supplied artifact of the shared codebase with its own intended-purpose statement, limited to: providing or supporting recommendations to health professionals to apply ratified, published, evidence-based clinical guidelines and facility procedures — prompts, alerts, reminders, pathway recommendations, and information summaries. The intended-purpose statement MUST NOT claim or imply diagnosis, screening, monitoring, or treatment specification, and marketing/advertising materials are conformance artifacts bound to it.
**Rationale trace:** TGA criterion (a) + recommendation definition; XC-1/XC-2; TGA advertising obligations for exempt devices.

### GPP-2 (MUST)
**Statement:** Exempt is not unregulated. The J-3 obligations register is maintained and evidenced from the fabric: (i) TGA notification via the Clinical Decision Support Software Exemption Notification Form within 30 working days of supply; (ii) conformity with the Essential Principles for safety and performance, evidenced by AF-7-style bundles; (iii) adverse-event reporting; (iv) therapeutic-goods advertising compliance; (v) recall/hazard-alert cooperation. Each obligation has a named owner in the responsibility register.
**Rationale trace:** TGA guidance, "Regulatory requirements that apply to exempt CDSS" (verbatim-reviewed); MAK-FFC AF-7.

### GPP-3 (MUST)
**Statement:** Any change to J-3's function or intended purpose re-runs the full exclusion/exemption assessment before release. The assessment record (criteria walk-through, verdict, assessor) enters the ledger; the release pipeline blocks on its presence.
**Rationale trace:** TGA guidance ("if your product is updated or its intended purpose changes, you must reassess"); XC-1 risk register (regulatory misclassification).

### GPP-4 (MUST)
**Statement:** Criterion (a) enforcement — recommendations render only to authenticated health professionals (role-verified per the Regulations' health-professional definition). The patient face in J-3 is limited to intake instruments, consent management, access ledger, and logistics; it MUST NOT render clinical recommendations, diagnoses, risk information, or monitoring feedback to patients.
**Rationale trace:** TGA criterion (a) sole-purpose language; MAK-FFC PF-8 narrowed for the profile.

### GPP-5 (MUST)
**Statement:** Criterion (a) claim-type enforcement — the GPP build's released claim types are exactly: `guideline-prompt`, `pathway-recommendation`, `reminder`, `information-summary`, `gather-more-information`. The types `diagnosis`, `differential`, `risk-score`, `screening-result`, `triage-score`, `treatment-customization`, and `monitoring-alert` are structurally unrepresentable in the J-3 artifact (types not compiled in), not merely disabled by configuration.
**Rationale trace:** TGA recommendation definition (excludes diagnosis, new diagnostic information, treatment specification); XC-2 "enforced in code, not policy."

### GPP-6 (MUST)
**Statement:** Criterion (b) enforcement — the data plane's J-3 ingestion allowlist admits QuestionnaireResponse, practitioner-entered data, and EMR/EHR-retrieved records. FHIR resources bearing device origin (populated `Observation.device`, device-sourced Provenance, or waveform/imaging content types) are rejected at the API boundary with a ledgered refusal. No imaging, waveform, sensor-stream, or IVD-output endpoint is linked into the build. EMR-retrieved values may be displayed but MUST NOT be interpreted, trended for monitoring, or used as grounds for inferences over device-signal content.
**Rationale trace:** TGA criterion (b) + its "directly analyse or process," "signal," and display-for-monitoring explanations.

### GPP-7 (MUST)
**Statement:** Criterion (c) enforcement — every J-3 recommendation's argument renders with: warrant → the published guideline clause (publisher, citation, version, effective date); backing → evidence tier and public source link; and deterministic evaluation trace. The release gate enforces independent verifiability: a recommendation whose complete basis is not reproducible by a health professional from cited, publicly accessible sources MUST NOT release. No learned parameters exist anywhere in the J-3 inference path.
**Rationale trace:** TGA criterion (c) verbatim requirements (transparent; easily understand and verify; clearly references logic/guidelines/evidence; independently verifiable); TGA note that AI-enabled CDSS will not meet the criteria; SPINE-7.

### GPP-8 (MUST)
**Statement:** The profile boundary is enforced at build time by exclusion: the modules for Bayesian inference, conformal wrapping, LLM runtime, device-signal ingestion, and the prohibited claim types are absent from the compiled J-3 artifact and its dependency graph. Each release generates an SBOM (CycloneDX or equivalent) that CI diffs against the prohibited-namespace manifest; a match fails the build. Feature flags, environment variables, or configuration MUST NOT be capable of enabling an excluded capability in a J-3 artifact.
**Rationale trace:** XC-2 ("enforced in code, not policy"); supply-chain evidence for Essential Principles conformity.

### GPP-9 (MUST)
**Statement:** Schema-level enforcement — J-3 GenericArgument templates carry `profile: GPP`; the compiler and validator reject, for this profile, any warrant type other than `guideline-rule` and any qualifier type other than `applicability` (a deterministic statement of which guideline population/conditions the prompt applies to). The Deterministic Evaluator refuses drafts bearing `posterior` or `conformal` qualifiers, and the refusal is ledgered.
**Rationale trace:** SPINE-2 adapted to a non-probabilistic profile; GPP-5/7 coherence.

### GPP-10 (MUST)
**Statement:** A conformance suite (GPP-CONF) runs as a release gate: negative tests attempt each prohibited capability (invoke Bayesian inference, ingest a device-originated Observation, construct a diagnosis-type claim, render a patient-facing recommendation, enable an excluded module by configuration) and pass only on structural absence or refusal-with-ledger-record. Static analysis forbids imports from excluded namespaces. The suite's results are conformity-file artifacts.
**Rationale trace:** GPP-8/9 verifiability; MAK-FFC evaluation-firewall discipline (EN-7) applied to the boundary itself.

### GPP-11 (MUST)
**Statement:** Runtime attestation and defense in depth — the J-3 artifact cryptographically attests its profile identity at startup; every fabric entry it writes is stamped `profile: GPP`; and a spine-level boundary monitor alarms if any claim type, qualifier type, or ingestion class outside the J-3 whitelist ever appears in a J-3 deployment's ledger. A boundary alarm is triaged as a potential adverse event and a mandatory GPP-3 reassessment trigger.
**Rationale trace:** defense in depth over GPP-8..10; TGA adverse-event obligation; SPINE-4 evidentiary chain.

### GPP-12 (MUST)
**Statement:** Single-codebase discipline — J-3 shares the justification fabric, ledger, guideline compiler, version pinning, deviation machinery, and register renderers with J-1/J-2. J-3 diverges by exclusion only: no J-3-only clinical logic, schema branches, or guideline content forks. A guideline compiled for J-3 is byte-identical to the same guideline's GenericArguments in J-1/J-2 at the same version.
**Rationale trace:** fork-drift risk; SPINE-5 replay integrity across tiers; AF-5 feedback loop must aggregate across tiers.

### GPP-13 (SHOULD)
**Statement:** Evidence-vehicle doctrine — J-3 deployments accumulate fabric evidence (prompt usage, deviation patterns, guideline-gap findings, workflow telemetry) that, under ethics approval and appropriate consent, feeds J-1/J-2 validation submissions and the AF-5 guideline feedback loop. Deployment agreements SHOULD secure this secondary-use basis at signing.
**Rationale trace:** §1 strategic function 2; CF-7/EN-7 evaluation needs; XC-3 field-pilot phasing.

### GPP-14 (MUST)
**Statement:** Tier-promotion protocol — enabling any excluded capability for any deployment constitutes supply of a different device under the classified track (J-1/J-2): new artifact, new intended-purpose statement, new conformity record, new (or amended) regulatory footing. In-place upgrades of a J-3 installation across the profile boundary are prohibited; migration is an explicit re-supply with the receiving governance's sign-off.
**Rationale trace:** GPP-3; XC-1 honesty posture; TGA reassessment doctrine.

### GPP-15 (SHOULD)
**Statement:** The jurisdiction map (§2.3) is a maintained artifact reviewed at least annually and before any new-market supply: TGA criteria (a)(b)(c) for Australia; FDA §520(o)(1)(E) four criteria per the revised final guidance (6 Jan 2026) for the USA, noting the singular-recommendation allowance, the strengthened criterion-4 independent-review basis, and the time-critical relocation; EU MDR Rule 11's absence of a carve-out; and per-country assessment for low-resource jurisdictions with WHO SMART alignment as the adaptation vehicle.
**Rationale trace:** verified TGA guidance (Oct 2025 rev.); Covington analysis of FDA revised guidance (Jan 2026); MDR Rule 11; XC-3/XC-4.

### GPP-16 (MAY)
**Statement:** The Deviation Composer and deviation ledger remain enabled in J-3 — recording that a clinician departed from a guideline prompt, with reasons, is clinical documentation, not diagnosis or treatment specification — and the auditor read model over J-3 ledgers operates as internal quality assurance. ⚑ If a legal reading finds deviation-pattern analytics drift toward "new diagnostic information" in a jurisdiction, the analytics (not the recording) are excluded there.
**Rationale trace:** SPINE-8 preserved at the exempt tier; GPP-13 evidence value; conservative flag.

## 5 — Obligations register (exempt-tier residuals)

| Obligation | Trigger | Evidence source | Owner field |
|---|---|---|---|
| TGA exemption notification (CDSS Exemption Notification Form) | Within 30 working days of first supply | Ledger supply record + submitted form copy | `regulatory` |
| Essential Principles conformity | Continuous; per release | GPP-CONF results, SBOM, AF-7-style bundles, risk file | `quality` |
| Adverse event reporting | On event, incl. GPP-11 boundary alarms triaged positive | Ledger incident chain | `safety` |
| Advertising compliance | All external claims | Intended-purpose statement (GPP-1) as the claims boundary | `regulatory` |
| Recall / hazard-alert cooperation | On TGA action | Deployment registry + version pinning (SPINE-5) | `operations` |
| Reassessment on change | Any functional or intended-purpose change | GPP-3 assessment records | `regulatory` |

## 6 — Boundary edge cases (decided and flagged)

- **Triage urgency scoring — OFF.** Deriving an urgency tier from patient data is new diagnostic information / risk stratification. J-3 may present the *guideline's own* triage pathway text as a prompt; it may not compute a patient's tier.
- **Time-critical contexts — avoid.** The FDA's revised guidance relocates time-critical decision support outside the non-device envelope (no time for independent review); TGA criterion (c) points the same direction. J-3 deployment contexts SHOULD exclude emergency/time-critical workflows; this is a deployment-scoping control, recorded per site.
- **Verbatim guideline dose tables — ⚑ legal review.** Displaying a published table uninterpreted is arguably guideline content; any patient-specific computation over it is customization and OFF.
- **Values elicitation display — ⚑ legal review.** Eliciting and displaying patient priorities to the clinician may be permissible information; using them to reweight recommendations is customization and OFF (PF-3 machinery is J-1/J-2).
- **EMR value display — narrow.** Display without interpretation is within the exempt scope; the moment a displayed value participates in an inference beyond guideline-applicability matching, GPP-6/9 must refuse it.

## 7 — Delta summary against MAK-FFC

| MAK-FFC requirement | J-3 disposition |
|---|---|
| SPINE-1..5, SPINE-7..9 | Apply unmodified |
| SPINE-6 (plural guidelines) | Applies; conflicts between co-resident guidelines surface as prompts-with-conflict, never resolved by the system |
| CF-1..5, CF-7, CF-8 | Apply; CF-2's qualifier renders as `applicability`, not posterior |
| CF-6 (MDT multi-author) | Applies (documentation function) |
| PF-1, PF-4 (consent subset), PF-6 | Apply |
| PF-2, PF-3, PF-5 clinical-feedback aspects, PF-8 | Suspended in-profile (no patient-facing clinical content); PF-3 machinery excluded (GPP capability matrix) |
| AF-1..3, AF-7, AF-8 | Apply as internal QA + conformity evidence |
| AF-4 theater detector | SHOULD run in shadow mode only ⚑ (see GPP-16 flag) |
| EN-1..3, EN-7, EN-8 | Apply (evaluator + compiler are the whole engine plane) |
| EN-4, EN-5 runtime, EN-6 runtime, EN-9 | Excluded with their modules; EN-5 adversarial testing still runs in CI against the J-3 artifact (harness, not runtime) |
| XC-1, XC-3, XC-4 | Apply; XC-2 is realized by this addendum |

## Appendix A — ID census (additive)

```json
{
  "doc_id": "MAK-J3",
  "version": "0.9-proposed",
  "requirements": {
    "GPP": ["GPP-1","GPP-2","GPP-3","GPP-4","GPP-5","GPP-6","GPP-7","GPP-8","GPP-9","GPP-10","GPP-11","GPP-12","GPP-13","GPP-14","GPP-15","GPP-16"]
  },
  "levels": {
    "MUST":   ["GPP-1","GPP-2","GPP-3","GPP-4","GPP-5","GPP-6","GPP-7","GPP-8","GPP-9","GPP-10","GPP-11","GPP-12","GPP-14"],
    "SHOULD": ["GPP-13","GPP-15"],
    "MAY":    ["GPP-16"]
  },
  "legal_review_flags": ["dose-table display (§3, §6)", "values elicitation display (§3, §6)", "deviation-pattern analytics in-profile (GPP-16)"],
  "retired": []
}
```

## Appendix B — Self-audit checks (additive)

1. **ID census parity** — GPP-n headers exactly match Appendix A (16).
2. **Level parity** — header levels match Appendix A buckets.
3. **Matrix/requirement coherence** — every OFF row in §3 is enforced by at least one MUST (GPP-5/6/7/8/9), and every ⚑ in §3 appears in §6 and Appendix A flags.
4. **No relaxation** — no GPP-n weakens a MAK-FFC MUST; deltas in §7 only narrow scope or suspend patient-facing clinical functions.
5. **Anchor currency** — frontmatter regulatory anchors carry version dates; any submission re-verifies them (LLM contract rule 3).
6. **Boundary language** — "disabled," "flagged off," or "configurable" never appears where "structurally absent" is required (GPP-8).
7. **Trace presence** — every GPP-n has a non-empty rationale trace.
8. **Cross-doc resolution** — every MAK-FFC ID cited resolves in MAK-FFC v1.0 Appendix B.
