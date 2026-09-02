---
doc_id: MAK-LEG
title: "The Legs Corpus"
version: "1.0"
date: "2026-09-01"
series: "Mākoha research series — volume 16 · the Reasonable Default Stack, six legs"
status: informative-defaults + normative bindings
normative_language: "RFC-2119 (MUST / SHOULD / MAY) — defaults are SHOULD-level suggestions by design; only the binding constraints are MUST"
req_prefixes: [LS, L1, L2, L3, L4, L5, L6]
req_count: 23
subordinate_to: "Every corpus in the series — a stack choice that violates any corpus MUST is invalid regardless of anything written here"
authority_note: "Per the commissioning instruction, the named technologies are a reasonable answer/example — NOT a hard and fast authoritative ruleset. The authoritative content is the binding constraints each leg must satisfy, whatever technology is chosen."
governed_by:
  - "REG-POSTURE v1.0 via MAK-ANT — stack bindings TASK-REG-009..013, KTX-001..012, STD stack; ASSUME-REG-004/006 remain OPEN"
changelog:
  - "v1.0 (2026-09-01): initial release — 23 requirements across LS/L1..L6; six legs with defaults, bindings, alternatives, and tier notes."
companions:
  - "MAK-CEC v1.1 (tier manifests, single gate, pins) · MAK-PRB/MAK-LBP v1.0 (the UIs the frontend leg carries) · MAK-ABC v1.0 (the evidence the stack must emit) · MAK-ANT v1.0 (regulatory bindings) · MAK-ELSM v1.1 lineage (verified components)"
artifact_url: "https://claude.ai/code/artifact/3c4b1ffc-8683-466e-9a5d-c27c486937d6"
change_policy: "Requirement IDs are stable; retired IDs never reused. Defaults may be swapped freely where bindings hold; binding changes are argued deviations."
---

<!-- LLM USAGE CONTRACT (additive; not part of the source document)
1. Requirement blocks (### LS-n / L1-n .. L6-n) are NORMATIVE at their stated level.
   SHOULD-level defaults are genuine suggestions: substituting an equivalent that
   satisfies the leg's MUST bindings requires only a recorded choice, not a deviation.
2. MUST bindings are the authoritative layer: they restate series law (pins, single
   gate, SBOM/tier manifests, offline floor, ledger tamper-evidence) at the stack.
   Never generate a stack design that satisfies a default but violates a binding.
3. Named third-party services carry their ASSUME-REG dependencies (Baseten:
   ASSUME-REG-004; Ketryx: ASSUME-REG-006) — never describe these as settled.
4. MUST violations in generated designs/code/documents require an explicit DEVIATION
   notice naming the ID.
5. Appendix A's ID census is authoritative for validator checks; Appendix B's
   self-audit checks gate any edit of this file.
END LLM USAGE CONTRACT -->

# The Legs Corpus

The Reasonable Default Stack for executing the CDSS Butterfly — six legs (frontend, backend, database, cache and queue, storage, infrastructure and deploy), each given as a sensible default with the binding constraints that are the actual law, the alternatives that satisfy them, and the tier and regulatory notes that travel with the choice.

**Document metadata:** Execution defaults · v1.0 · 1 Sep 2026 · sixteenth volume in the Mākoha research series · STATUS: informative defaults + normative bindings · REQ IDS: LS · L1–L6 (23) · AUTHORITY: defaults are suggestions; bindings are law · GOVERNED BY: REG-POSTURE v1.0 via MAK-ANT.

## Contents

1. [Part 0 — How to use this document](#part-0--how-to-use-this-document)
2. [Part 1 — Why legs, and the stack laws (LS)](#part-1--why-legs-and-the-stack-laws)
3. [Part 2 — Leg 1 · Frontend (L1)](#part-2--leg-1--frontend)
4. [Part 3 — Leg 2 · Backend (L2)](#part-3--leg-2--backend)
5. [Part 4 — Leg 3 · Database (L3)](#part-4--leg-3--database)
6. [Part 5 — Leg 4 · Cache & queue (L4)](#part-5--leg-4--cache--queue)
7. [Part 6 — Leg 5 · Storage (L5)](#part-6--leg-5--storage)
8. [Part 7 — Leg 6 · Infrastructure & deploy (L6)](#part-7--leg-6--infrastructure--deploy)
9. [Part 8 — The stack-to-series binding map](#part-8--the-stack-to-series-binding-map)
10. [Appendix A — ID census](#appendix-a--id-census-additive)
11. [Appendix B — Self-audit checks](#appendix-b--self-audit-checks-additive)

## Thesis

> A butterfly's legs are not glamorous, and nobody chooses a butterfly for its legs — but they are what it stands on between flights, and some of them taste what they touch. The stack is the same: no technology choice below wins the product, and several could lose it. The series' architecture documents are deliberately technology-agnostic; this volume supplies what an implementation team still needs on day one — a reasonable default for each of the six legs, chosen for boringness, hireability, and fit with the components the sourcing record verified — while being honest about which layer is actually law. The law is not "use PostgreSQL"; the law is pins that replay, one gate to the faces, tamper-evident ledger storage, tier manifests in CI, and an offline floor the patient face never falls through. Choose different legs freely; the body they carry does not bend.

## Part 0 — How to use this document

Read each leg as three layers. **The default** (SHOULD): the named technologies — per the commissioning instruction, a reasonable example, not an authoritative ruleset. **The bindings** (MUST): the series-law constraints the leg must satisfy whatever is chosen — these are restatements at stack level of requirements that live in the corpora, and they are authoritative. **The notes**: alternatives that also satisfy the bindings, tier consequences (J-1/J-2/J-3 per MAK-CEC RG-6), and REG-POSTURE bindings with their open assumptions.

- **Substitution rule.** Swapping a default for an equivalent that satisfies the leg's bindings is a recorded choice, not a deviation. Violating a binding is a deviation against the corpus requirement the binding cites.
- **Requirement IDs.** `LS-n` stack laws (cross-leg); `L1-n`..`L6-n` per leg.

## Part 1 — Why legs, and the stack laws

The stack recommendation follows one strategic fact the sourcing record established twice over: **the moat is the fabric, not the stack.** Everything distinctive in Mākoha — the justification fabric, the GAAM service, the deviation and gap machinery, the five-stage gate, the workbenches — is a build on top of ordinary infrastructure; nothing in the moat demands exotic technology. The rational stack posture is therefore aggressive boringness: managed services where they carry no lock-in risk to the moat, mainstream languages with deep hiring pools, LTS versions, and every clever engineering hour saved for the components no one sells.

### LS-1 (MUST)
**Statement:** Defaults are defaults; bindings are law. An implementation may substitute any technology for a leg's default provided the leg's MUST bindings hold and the choice is recorded with its rationale; no substitution, however conventional, may violate a binding — the binding's cited corpus requirement governs.
**Rationale trace:** commissioning instruction (examples, not authoritative rules); series subordination law.

### LS-2 (MUST)
**Statement:** The stack emits the series' evidence by construction: whatever is chosen per leg, the assembled stack supports version pinning and bit-for-bit replay (SPINE-5, MAK-CEC RG-4), the single release gate with no second path (RG-1), tier manifests with SBOM diffs in CI (RG-6; TASK-REG-011), the unified telemetry schema (RG-5), and conformity-file artifact retention (MAK-ABC AX family). A stack that cannot evidence these is non-conformant regardless of its components' individual merits.
**Rationale trace:** MAK-CEC RG-1/4/5/6; MAK-ABC AX-3; REG-POSTURE TASK-REG-011.

### LS-3 (MUST)
**Statement:** Polyglot is bounded by contract: the verified execution components dictate a JVM presence (CQL translator, clinical-reasoning, HAPI — ELSM-01/02/20) and a Python presence (engine plane: MAPIE/pgmpy-class — ELSM-12/14) alongside the default TypeScript application layer; every runtime boundary crosses through the MAK-CEC engine contract (OM-2/OM-7), and no clinical logic is reimplemented across languages to avoid a service call (EN-3's single-path law at the stack).
**Rationale trace:** MAK-CEC OM-7; MAK-ELSM verified-component languages; CP-1 single compilation path.

### LS-4 (SHOULD)
**Statement:** Boring-technology bias governs additions: a new stack component enters only when a binding or a verified sourcing entry demands it; managed, widely-hired, LTS-supported options are preferred; and the count of distinct runtime technologies is a reviewed metric, not an accident.
**Rationale trace:** moat-is-the-fabric strategy; operational economics of a small regulated team.

## Part 2 — Leg 1 · Frontend

**Default (the commissioned example):** React with Next.js, TypeScript, Tailwind CSS.

**Why it is reasonable:** the largest component-library and hiring ecosystem; Next.js gives the clinician face server-rendered speed and the patient face PWA/offline scaffolding; TypeScript carries the five-signal registry and register lint as types; Tailwind keeps the identity system (MAK-LBP CV-1) in tokens rather than scattered CSS. The verified low-resource delivery vehicle remains Android-native (android-fhir/fhircore, ELSM-04/05) where a national deployment rides that stack — the web frontend and the Android path coexist by design (MAK-TXC TL profiles).

### L1-1 (SHOULD)
**Statement:** The web frontend defaults to React + Next.js + TypeScript + Tailwind, structured as the two governed component libraries (MAK-PRB PC-1; MAK-LBP CC-1) over shared design tokens, with the identity sheet and register lints compiled into CI.
**Rationale trace:** commissioned default; MAK-PRB/MAK-LBP library laws; ecosystem economics.

### L1-2 (MUST)
**Statement:** Whatever frontend is chosen, it satisfies the UI corpora's bindings: offline-first with resumable, lossless capture on the patient face (MAK-PRB PI-1/2, PA-1); the one-surface law and verdict fidelity on the clinician face (MAK-LBP CA-5 suite); the bright line structurally (MAK-PRB PS-4); WCAG 2.2 AA equivalent on both faces; and the embedding floor for CDS Hooks/SMART delivery (MAK-LBP CA-2).
**Rationale trace:** MAK-PRB PA-6; MAK-LBP CA-5; the UI conformance suites as the leg's acceptance tests.

### L1-3 (MAY)
**Statement:** Low-resource deployments may ship the Android-native path (android-fhir SDC + fhircore lineage) as the patient face's primary vehicle, with the web frontend serving clinician and auditor faces — provided register, bright-line, and floor conformance run on both vehicles from the same content artifacts.
**Rationale trace:** MAK-ELSM ELSM-04/05 verdicts; MAK-TXC TL-1/2; single-content-source discipline.

## Part 3 — Leg 2 · Backend

**Default (the commissioned example):** Node.js with NestJS, TypeScript, REST or GraphQL as the use case requires.

**Why it is reasonable:** NestJS gives the application layer structure (modules, guards, interceptors) that maps naturally onto per-face gateways and register-scoped projections (SPINE-9); TypeScript shares types with the frontend; REST for the face APIs (cacheable, simple), GraphQL only where a face's read patterns genuinely demand composition. The engine plane and the CQL stack remain their own services per LS-3 — the Node layer orchestrates and projects; it never computes clinical logic.

### L2-1 (SHOULD)
**Statement:** The application/API layer defaults to NestJS + TypeScript, organized as per-face gateways (authn, authz, register rendering) over the fabric's read API (SPINE-9), with REST as the default interface style and GraphQL adopted per-surface only on demonstrated composition need.
**Rationale trace:** commissioned default; MAK-FFC SPINE-9 / per-face gateway architecture.

### L2-2 (MUST)
**Statement:** Whatever backend is chosen: clinical logic lives only in compiled knowledge-plane artifacts executed by the engine services (CP-1 — no rules in controllers, resolvers, or middleware); the deterministic evaluator is the single verdict producer (RG-1) and the API layer holds no release-capable code path; every face request resolves against evaluator-released content with pins intact; and service boundaries carry the engine contract types (OM-2/OM-3) without coercion.
**Rationale trace:** MAK-CEC CP-1/RG-1/OM-2/OM-3; second-path erosion risk at the API layer.

### L2-3 (MUST)
**Statement:** The data plane speaks FHIR at its boundaries: HAPI FHIR (or equivalent conformant server) fronts clinical resources (ELSM-20), with the fabric's bindings (GuidanceResponse, Provenance, AuditEvent, DetectedIssue, Consent, QuestionnaireResponse — SPINE-4) as the interchange contract; bespoke clinical schemas exist only behind the fabric, never at integration boundaries.
**Rationale trace:** MAK-FFC SPINE-4; MAK-ELSM ELSM-20; interoperability as regulatory and LMIC necessity.

## Part 4 — Leg 3 · Database

**Default (the commissioned example):** PostgreSQL — or as the use case requires.

**Why it is reasonable:** the sourcing record already settled the hard question: QLDB is retired (ELSM-18), and the AWS-native answer for the tamper-evident ledger is Aurora PostgreSQL with an application-level hash-chain/transparency-log pattern and periodic external anchoring (ELSM-19). One engine (PostgreSQL) then serves the ledger, the relational read models, and — via JSONB — the artifact metadata, with immudb (ELSM-17) as the alternative if BUSL terms clear legal review.

### L3-1 (SHOULD)
**Statement:** PostgreSQL (Aurora PostgreSQL in the AWS default) is the default database for the fabric ledger, read models, and operational stores — one engine, few instances, boring on purpose.
**Rationale trace:** commissioned default; MAK-ELSM ELSM-19; LS-4.

### L3-2 (MUST)
**Statement:** Whatever database is chosen, the ledger properties hold: append-only with tamper evidence (hash-chained, Merkle-verifiable, externally anchored on a ratified cadence — SPINE-4), corrections as superseding entries, bit-for-bit replay from pinned versions (SPINE-5), and the remodeling ledger (MAK-RWC MA-1) on the same evidentiary footing. Verification is exercised: the anchor-check and replay attestation run on schedule, not on faith.
**Rationale trace:** MAK-FFC SPINE-4/5; MAK-ELSM ELSM-18/19 landmine and pattern; MAK-ABC AE-1.

### L3-3 (MAY)
**Statement:** Specialized stores may serve specialized reads (a search index for the auditor face's queries, a time-series store for telemetry) as derived, disposable projections of the ledger — rebuildable, never authoritative, and never a face's direct source (SPINE-9's derived-cache rule).
**Rationale trace:** MAK-FFC SPINE-9; read-model economics without truth-forking.

## Part 5 — Leg 4 · Cache & queue

**Default (the commissioned example):** Redis for caching; RabbitMQ if needed for queueing.

**Why it is reasonable:** Redis covers session, face-cache, and rate-limiting needs with managed options everywhere; a broker earns its place only when the workflow load (campaign scheduling, replay jobs, sync fan-out) outgrows Postgres-backed jobs — "if needed" is the operative phrase, and SQS is the lower-operations AWS-native alternative when it does.

### L4-1 (SHOULD)
**Statement:** Redis (managed) is the default cache; queueing starts with database-backed jobs and graduates to a broker (RabbitMQ, or SQS in the AWS default) only on demonstrated need — with the choice recorded per LS-1.
**Rationale trace:** commissioned default ("if needed"); LS-4 boring bias.

### L4-2 (MUST)
**Statement:** Whatever cache and queue are chosen: caches hold only derived, disposable projections (never the sole copy of any fabric content — SPINE-9), a cache never serves pre-verdict or held content to a face (RG-1/HR-4 at the infrastructure layer), queues deliver the sync and telemetry flows with at-least-once semantics and idempotent consumers (the patient face's deferred sync must not lose or duplicate capture — MAK-PRB PI-2), and nothing clinical is decided in a queue consumer (OM-5).
**Rationale trace:** MAK-FFC SPINE-9; MAK-CEC RG-1/OM-5; MAK-PRB PI-2; cache-as-second-path risk.

### L4-3 (MAY)
**Statement:** Offline-heavy deployments may add an edge sync layer (the android-fhir engine's sync, or CRDT-style additive merge for diary data) provided sync conflicts resolve additively with review flags (MAK-PRB PI-2), never by overwrite.
**Rationale trace:** MAK-PRB PI-2; MAK-TXC TL-1; low-resource sync reality.

## Part 6 — Leg 5 · Storage

**Default (the commissioned example):** AWS S3 or equivalent cloud object storage.

**Why it is reasonable:** the knowledge plane is an artifact economy — compiled templates, FML files, codebook packs, instrument versions, evidence-library snapshots, SBOMs, conformity bundles — and versioned object storage with immutability controls is exactly that economy's warehouse.

### L5-1 (SHOULD)
**Statement:** Object storage (S3 in the AWS default) holds the artifact economy: knowledge-plane artifacts, evidence-library snapshots, replay corpora, exports, and conformity bundles — versioned buckets, lifecycle rules, and jurisdiction-pinned regions per deployment.
**Rationale trace:** commissioned default; SPINE-5 artifact discipline; MAK-TXC TC-3 routing realities.

### L5-2 (MUST)
**Statement:** Whatever storage is chosen: knowledge-plane artifacts are immutable at rest per version (write-once semantics or object-lock equivalent), addressed by content hash where pins reference them (SPINE-5), with conformity artifacts (suite results, SBOMs, bundles) retained under the obligations register's retention rules (MAK-ABC AX-3) and patient-exportable data honouring custody and routing law (MAK-TXC TC-1/3).
**Rationale trace:** MAK-FFC SPINE-5; MAK-ABC AX-3; MAK-TXC TC family.

### L5-3 (MAY)
**Statement:** The firewalled evaluation corpus may live in physically or account-separated storage with independent access control, making EN-7's no-write-access reproducibility an infrastructure property rather than a policy.
**Rationale trace:** MAK-FFC EN-7; MAK-CEC RG-3; separation as architecture.

## Part 7 — Leg 6 · Infrastructure & deploy

**Default (the commissioned example):** AWS managed services with Docker.

**Why it is reasonable:** the programme is already AWS-resident, and REG-POSTURE has already made the leg's hard calls: split the Amplify path (synthetic/demo push-to-deploy versus regulated gated releases — TASK-REG-010), move runtime inference to Baseten Sydney dedicated deployments with contractual version pinning (TASK-REG-009, ASSUME-REG-004 open), SBOMs in CI feeding Ketryx supply-chain management (TASK-REG-011, KTX-012), and Ketryx-on-Jira as the lifecycle system of record (KTX-001..012, ASSUME-REG-006 open).

### L6-1 (SHOULD)
**Statement:** Infrastructure defaults to AWS managed services with Docker-containerized services under infrastructure-as-code: ECS/Fargate-class runtime for the application and engine services, Aurora and managed Redis per legs 3–4, S3 per leg 5, and the Amplify split path per REG-POSTURE — demo/synthetic push-to-deploy, regulated releases through the gated pipeline with approvals landing as CI artifacts.
**Rationale trace:** commissioned default; REG-POSTURE TASK-REG-010; LS-4.

### L6-2 (MUST)
**Statement:** Whatever infrastructure is chosen: builds are reproducible and containerized with SBOM generation in CI diffed against tier manifests (RG-6; TASK-REG-011); the regulated release pipeline enforces the gates (suite results, approvals, risk-file linkage) before deploy (GATE discipline; KTX traceability); runtime model substrates carry contractual version-stability and change-notice terms before any regulated use (RG-7; ASSUME-REG-004 open — never described as settled); environments enforce the synthetic-only line pre-GATE-002 (REG-KEEP-004); and data residency pins per deployment jurisdiction.
**Rationale trace:** MAK-CEC RG-6/7; REG-POSTURE TASK-REG-009..013, REG-KEEP-004; MAK-ANT AN-7.

### L6-3 (SHOULD)
**Statement:** Observability rides the unified telemetry schema (RG-5) into boring managed tooling (CloudWatch/Grafana-class), with the auditor face's system lens as the only clinical-telemetry consumer surface — infrastructure dashboards carry operational metrics, never clinical-decision analytics.
**Rationale trace:** MAK-CEC RG-5; MAK-FFC AF-8/EN-9 lens discipline at the ops layer.

### L6-4 (MAY)
**Statement:** Low-resource deployments may substitute the managed-cloud default with in-country or on-premise equivalents (a national health cloud, a ministry data centre) where sovereignty or connectivity demands it — the bindings travel unchanged, and the substitution is the recorded, expected case rather than an exception.
**Rationale trace:** north star; MAK-TXC TC-3 routing; XC-3/XC-4 deployment pluralism.

## Part 8 — The stack-to-series binding map

| Leg | Default (suggestion) | The law it must satisfy (authoritative) |
|---|---|---|
| 1 · Frontend | React/Next.js · TypeScript · Tailwind | MAK-PRB PA-6 + MAK-LBP CA-5 suites; bright line structural; offline floor; embedding floor |
| 2 · Backend | Node.js/NestJS · TS · REST (GraphQL on need) | No clinical logic outside compiled artifacts (CP-1); single gate (RG-1); FHIR at boundaries (SPINE-4); typed signals uncoerced (OM-3) |
| 3 · Database | PostgreSQL / Aurora | Tamper-evident append-only ledger with anchoring + replay (SPINE-4/5); QLDB avoided (retired); derived stores never authoritative (SPINE-9) |
| 4 · Cache & queue | Redis · RabbitMQ/SQS if needed | Caches derived-only; no pre-verdict content served; idempotent lossless sync (PI-2); no decisions in consumers (OM-5) |
| 5 · Storage | S3-class object storage | Immutable versioned artifacts, hash-addressed pins (SPINE-5); conformity retention (AX-3); custody-honouring exports (TC) |
| 6 · Infra & deploy | AWS managed · Docker | SBOM + tier manifests in CI (RG-6); gated regulated pipeline (TASK-REG-010); pinned inference substrate under contract (RG-7, ASSUME-REG-004); synthetic-only pre-GATE-002 |

### Findings → requirements

| Finding | Source | Requirements it drives |
|---|---|---|
| The moat is the fabric; everything around it is buyable | MAK-ELSM/LWC/RWC sourcing passes | LS-4, all SHOULD defaults |
| Examples are suggestions, not authoritative rules | commissioning instruction | LS-1; the two-layer structure |
| QLDB retired; Aurora + transparency-log is the pattern | MAK-ELSM ELSM-18/19 | L3-1/2 |
| Verified components fix the polyglot floor (JVM + Python + TS) | MAK-ELSM ELSM-01/02/12/14/20 | LS-3 |
| Stack decisions with regulatory weight are already made and assumption-gated | REG-POSTURE TASK-REG-009..013; ASSUME-REG-004/006 | L6-1/2 |
| Caches and queues are where second paths and data loss hide | MAK-CEC RG-1; MAK-PRB PI-2 | L4-2 |
| Low-resource substitution is the expected case, not the exception | north star; XC-3/4 | L6-4, L1-3 |

### Sources

- Commissioning instruction (the six legs and their example stacks, given as suggestions).
- Series: MAK-CEC v1.1 (RG family, OM contract) · MAK-PRB/MAK-LBP v1.0 (UI suites) · MAK-ABC v1.0 (evidence duties) · MAK-ANT v1.0 / REG-POSTURE v1.0 (TASK-REG-009..013, KTX-001..012, REG-KEEP-004, ASSUME-REG-004/006) · MAK-ELSM v1.1 + wing annexes (verified components and landmines).

*Document footer (source artifact):* The Legs Corpus v1.0 · defaults are suggestions; bindings are law; requirement IDs are stable. Compiled 1 Sep 2026 as the sixteenth and final volume of the CDSS Butterfly set.

## Appendix A — ID census (additive)

Authoritative enumeration for validator checks. Count: **23**.

```json
{
  "doc_id": "MAK-LEG",
  "version": "1.0",
  "requirements": {
    "LS": ["LS-1","LS-2","LS-3","LS-4"],
    "L1": ["L1-1","L1-2","L1-3"],
    "L2": ["L2-1","L2-2","L2-3"],
    "L3": ["L3-1","L3-2","L3-3"],
    "L4": ["L4-1","L4-2","L4-3"],
    "L5": ["L5-1","L5-2","L5-3"],
    "L6": ["L6-1","L6-2","L6-3","L6-4"]
  },
  "levels": {
    "MUST":   ["LS-1","LS-2","LS-3","L1-2","L2-2","L2-3","L3-2","L4-2","L5-2","L6-2"],
    "SHOULD": ["LS-4","L1-1","L2-1","L3-1","L4-1","L5-1","L6-1","L6-3"],
    "MAY":    ["L1-3","L3-3","L4-3","L5-3","L6-4"]
  },
  "retired": []
}
```

Census arithmetic: 10 MUST + 8 SHOULD + 5 MAY = 23 (4+3+3+3+3+3+4 across seven families).

## Appendix B — Self-audit checks (additive)

1. **ID uniqueness** — no requirement ID appears in more than one requirement header.
2. **ID census parity** — headers matching `^### (LS|L[1-6])-\d+ \((MUST|SHOULD|MAY)\)$` exactly equal Appendix A's enumeration.
3. **Level parity** — header levels match Appendix A buckets; every default is SHOULD or MAY, never MUST (the authority note's structural guarantee).
4. **Trace presence** — every requirement block has a non-empty rationale trace.
5. **Normative leakage** — no capitalized MUST/SHOULD/MAY outside requirement blocks, quoted text, or this appendix.
6. **Binding resolution** — every corpus requirement a binding cites resolves in its host volume.
7. **Assumption honesty** — ASSUME-REG-004/006 are never described as closed; Baseten/Ketryx bindings carry their contingency.
8. **Two-layer integrity** — every leg has at least one SHOULD default and at least one MUST binding; no leg's law depends on its default.
9. **Table integrity** — consistent column counts per row.
10. **Stability** — IDs from previous versions present or explicitly retired; never reused.
