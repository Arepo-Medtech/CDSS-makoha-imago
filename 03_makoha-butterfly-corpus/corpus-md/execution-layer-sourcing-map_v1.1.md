---
doc_id: MAK-ELSM
title: "Execution Layer Sourcing Map"
version: "1.1"
date: "2026-08-29"
changelog:
  - "v1.1 (2026-08-29): additive — Section 08 (J-3 Guideline-Prompt Profile applicability per sourcing entry), Appendix C machine-readable J-3 applicability register, FDA revised CDS guidance source, self-audit check 7. No v1.0 content altered or removed."
  - "v1.0 (2026-08-29): initial release."
series: "Mākoha research series — volume 4"
status: informative-sourcing-record
normative_language: "none — verdicts (ADOPT/ADAPT/BUILD/STUDY/LEGACY/AVOID) are recommendations, not requirements"
depends_on:
  - "MAK-FFC v1.0 (The Four Faces Corpus) — all requirement IDs referenced here resolve there; v1.1 folds MAK-J3 as Annex 1"
  - "MAK-J3 v0.9-proposed (Addendum J-3, Guideline-Prompt Profile) — GPP-n IDs referenced in Section 08 resolve there"
verdict_vocabulary:
  ADOPT: "use as dependency; maintained and license-compatible"
  ADAPT: "use with modification, license review, or as solver/backend behind own interface"
  BUILD: "no usable precedent exists; construct from scratch (studied ancestors noted)"
  STUDY: "mine for design; never take as a dependency"
  LEGACY: "superseded; deploy the named successor"
  AVOID: "retired or incompatible; do not select"
verification_method: "Every repository row reflects a direct fetch of the repo page on 2026-08-29, not training-data memory"
artifact_url: "https://claude.ai/code/artifact/6bb4c619-cb0c-4495-a37e-4045873cc867"
---

<!-- LLM USAGE CONTRACT (additive; not part of the source document)
This file is formatted for prompt work within the Mākoha CDSS Build Ecosystem.
Rules for any LLM consuming this document:
1. This document is INFORMATIVE. It never overrides MAK-FFC requirements; where a
   sourcing verdict and a requirement conflict, the requirement wins.
2. Verdicts use the controlled vocabulary in the frontmatter. Do not invent verdicts.
3. Statuses (archived, dormant, migrated, retired) are dated observations
   (2026-08-29) and MUST be re-verified before any dependency decision made after
   that date.
4. "No precedent found" claims are bounded by the methodology note in the footer:
   targeted-and-verified search, not exhaustive; treat as strong prior, not proof.
5. Requirement IDs (SPINE-n, CF-n, PF-n, AF-n, EN-n, XC-n) resolve to MAK-FFC v1.0.
6. The machine-readable inventory in Appendix A mirrors the tables; on any edit,
   tables and Appendix A must be updated together (self-audit check 3).
END LLM USAGE CONTRACT -->

# Execution Layer Sourcing Map

What actually runs: worked examples, demos, and production code on GitHub for every Four Faces Corpus subsystem — verified repo by repo — and, where no code exists, the 2025+ RAG and ML research that fits the niche. Verdicts: ADOPT / ADAPT / BUILD per component.

**Document metadata:** Research dossier · compiled 29 Aug 2026 · fourth volume in the Mākoha research series.

## The short version

> The corpus splits cleanly into three sourcing tiers. **Tier 1 — adopt:** the guideline-execution plane is production-grade open source today (HL7's CQL compiler/runtime, the clinical-reasoning operations library, Google's Android FHIR Workflow, and OpenSRP FHIR Core — which literally ships "WHO SMART Guidelines on Android" for LMIC community health, your low-resource profile as a maintained product). Conformal prediction is commodity (MAPIE), adversarial/robustness tooling exists (Giskard, ART), and tamper-evident storage has mature primitives (immudb, Merkle patterns) — with one landmine: AWS retired QLDB in July 2025, so the obvious AWS-native ledger is gone. **Tier 2 — adapt:** formal argumentation has real engines (TweetyProject actively maintained with ASPIC+/ABA/Dung semantics; Carneades dormant but complete), and the 2024–26 argumentation-LLM cluster (ArgLLMs, ArgMed-Agents, ArgEval/ArgTumour) has public code that mines guidelines into argument structures — the guideline-compiler assist, prototyped. **Tier 3 — build:** no GAAM implementation, no justification fabric, no deviation ledger, no compliance projector exists anywhere in public code. That absence is the moat: everything around your differentiator is buyable; the differentiator itself is not.

## 01 — Guideline execution plane — EN-2, EN-3, PF-7, XC-3

This is the strongest tier: the "narrative → computable → executable" pipeline the corpus mandates (EN-3) exists as maintained, Apache-licensed infrastructure, and the low-resource deployment profile (XC-3) has an entire product line built on it.

| Repo / artifact | What it gives you | Status (verified) | Verdict |
|---|---|---|---|
| [cqframework/clinical_quality_language](https://github.com/cqframework/clinical_quality_language) | The HL7 CQL reference stack: CQL→ELM compiler, ELM runtime, FHIR integration — the executable form your Guideline Compiler emits | 320★ · Apache-2.0 · Kotlin/Java · active | ADOPT |
| [cqframework/clinical-reasoning](https://github.com/cqframework/clinical-reasoning) | FHIR Clinical Reasoning operations as a library: PlanDefinition processing, measure evaluation, CDS — the $apply machinery behind GenericArgument execution | 47★ · Apache-2.0 · v4.7.0 May 2026 · active (Smile Digital Health) | ADOPT |
| [cqframework/cqf-ruler](https://github.com/cqframework/cqf-ruler) | Reference CDS server (HAPI plugin, CDS Hooks) | 71★ · Apache-2.0 · functionality migrating upstream to hapi-fhir-jpaserver-starter — treat as reference, deploy the upstream | LEGACY |
| [google/android-fhir](https://github.com/google/android-fhir) | Open Health Stack SDK: offline-first FHIR Engine, Structured Data Capture (your PF-1 intake instruments), and a Workflow library for on-device clinical logic | 599★ · Apache-2.0 · Kotlin · active | ADOPT |
| [opensrp/fhircore](https://github.com/opensrp/fhircore) | "Offline-capable, mobile-first healthcare… using FHIR and WHO Smart Guidelines on Android" — a running, deployed instance of the corpus's low-resource profile, community-health-worker-first | 68★ · Apache-2.0 · v2.2.2 Nov 2025 · 136 releases · active (Ona) | ADOPT / STUDY |
| [WHO SMART Guidelines IGs](https://smart.who.int/index.html) (WorldHealthOrganization GitHub org) | Published machine-readable guideline content (ANC, immunizations, HIV…) — GenericArgument source material for LMIC jurisdictions | FHIR IGs · CC/Apache mix · active program | ADOPT |

**Integration note.** The corpus's Guideline Compiler (EN-3) becomes a thinner build than it looked: consume WHO SMART / CPG-on-FHIR artifacts where they exist, compile CQL via the reference translator, and add the one layer nobody ships — the lift from PlanDefinition/CQL into GenericArgument templates with per-warrant evidence-tier backing. The delta is the argument annotation, not the execution machinery.

## 02 — Argumentation and the justification fabric — SPINE-1..3, AF-2, EN-1

| Repo / artifact | What it gives you | Status (verified) | Verdict |
|---|---|---|---|
| [TweetyProjectTeam/TweetyProject](https://github.com/TweetyProjectTeam/TweetyProject) | The maintained formal-argumentation workhorse: Dung semantics solvers, ASPIC+, assumption-based argumentation, probabilistic argumentation — candidate backend for the Deterministic Evaluator's conflict semantics | 41★ · LGPL-3.0 · Java · v1.31 Jul 2026 · active since 2010 | ADAPT |
| [carneades/carneades-4](https://github.com/carneades/carneades-4) | Complete structured-argument evaluator (CAES): schemes, weighing functions, cyclic graphs, AIF/LKIF import, visual export — the closest ancestor to an argument-fabric evaluator ever shipped | 61★ · MPL-2.0 · Go · dormant since 2017 — mine for design, don't depend | ADAPT / STUDY |
| [CLArg-group/argumentative-llms](https://github.com/CLArg-group/argumentative-llms) | Official code for Argumentative LLMs (Imperial CLArg, AAAI 2025): LLMs construct argumentation frameworks; formal semantics do the deciding — a running instance of "LLM proposes, formal layer releases" | Python · public · paper code, research-grade | ADAPT |
| GAAM (Generic/Actual Argument Model) implementation | The corpus's chosen formalism for GenericArgument/ActualArgument/Deviation | No public implementation found — Stranieri-era tooling (ArgumentDeveloper, JustSys) never open-sourced | BUILD |
| Justification fabric / deviation ledger / compliance projector (SPINE-4/8, AF-1..7) | The corpus's differentiator | No precedent found in public code, any language, any domain | BUILD |

**Build note.** The GAAM data structures are small (typed nodes, warrant references, version pins); the hard part was never the schema but the semantics of evaluation and deviation — and TweetyProject's solvers plus Carneades's CAES design document both, under compatible licenses. Budget the fabric as a from-scratch service with two studied ancestors, not a greenfield guess. Direct collaboration with Stranieri on the GAAM formalization remains the highest-leverage de-risking move (see The Stranieri File).

## 03 — Engine plane: inference, uncertainty, adversary — EN-4..8

| Repo / artifact | What it gives you | Status (verified) | Verdict |
|---|---|---|---|
| [scikit-learn-contrib/MAPIE](https://github.com/scikit-learn-contrib/MAPIE) | Conformal prediction sets and risk control for classification/regression/time-series; 2026 releases add LLM-as-judge and adaptive conformal — EN-4's qualifier discipline, off the shelf | 1.6k★ · BSD-3 · v1 API 2025 · very active | ADOPT |
| [babylonhealth/counterfactual-diagnosis](https://github.com/babylonhealth/counterfactual-diagnosis) | Reference code for counterfactual (causal) diagnosis over noisy-OR networks (Richens et al., Nat. Comms 2020) — the strongest public Bayesian-DDx baseline for your differential engine's evaluation harness | 66★ · GPL-3.0 · Python · dormant · algorithm under patent application — study, never ship | STUDY ONLY |
| pgmpy / general PGM stacks | Bayesian network construction and inference primitives for the differential engine's internals | Mature, MIT, active | ADOPT |
| [Giskard-AI/giskard](https://github.com/Giskard-AI/giskard) | Automated ML/LLM testing: metamorphic tests, performance and drift scanning, RAG evaluation — scaffolding for the corruption engine's harness (EN-5) and theater-detector experiments (AF-4) | Open source · active · framework-agnostic | ADOPT |
| Trusted-AI/adversarial-robustness-toolbox | Adversarial example generation and robustness evaluation — corruption-engine ammunition for perturbation classes | ~5k★ · MIT · active (LF AI) | ADOPT |

**Gap note.** There is no open-source, production Bayesian differential-diagnosis engine — the commercial ones (Infermedica, Isabel, Ada) are closed, and Babylon's public code is patent-encumbered reference material. Your differential engine remains a build; what changed is that its *evaluation* (firewalled harness, adversarial suites, conformal wrapping) is assembled from maintained parts.

## 04 — Ledger, data plane, patient custody — SPINE-4, PF-4, AF-1

| Repo / artifact | What it gives you | Status (verified) | Verdict |
|---|---|---|---|
| [codenotary/immudb](https://github.com/codenotary/immudb) | Immutable KV/document/SQL store with cryptographic commit log + Merkle tree, client-side verification — SPINE-4's tamper evidence as a database | 9k★ · Business Source License 1.1 (not OSI — check redistribution terms for SaMD) · active | ADAPT |
| AWS QLDB | The obvious AWS-native ledger for your Amplify/Bedrock stack | RETIRED — end of support 31 Jul 2025; AWS's own guidance: migrate to Aurora PostgreSQL with verification patterns | AVOID |
| Aurora PostgreSQL + hash-chain/Merkle pattern (or google/trillian, sigstore/rekor designs) | The post-QLDB AWS-native answer: application-level hash chaining with periodic external anchoring; transparency-log designs are the studied precedent | Patterns + Apache-2.0 reference implementations · active | ADOPT PATTERN |
| HAPI FHIR (jpaserver-starter) | Production FHIR server with Provenance/AuditEvent/Consent support; now absorbing the clinical-reasoning module — one deployable for data plane + guideline ops | Very active · Apache-2.0 | ADOPT |
| [fastenhealth/fasten-onprem](https://github.com/fastenhealth/fasten-onprem) | Self-hosted personal health record aggregating FHIR from providers — the nearest built thing to PF-4's Personal Data Agent | 2.8k★ · GPL-3.0 · ARCHIVED Jul 2026 — cautionary tale and design mine, not a dependency | STUDY |

## 05 — The 2025+ research plane: RAG and ML for the niche

Where code is thin, the literature since 2025 is not — and it is converging on exactly the corpus's carve-out from two directions.

### Guideline-grounded RAG (the compiler-assist and evidence-retrieval layer)

- **The effect is real and quantified:** a JAMIA systematic review and meta-analysis of biomedical RAG found a pooled OR of 1.35 (95% CI 1.19–1.53) over baseline LLMs, and ships clinical development guidelines — the field's Cockburn analogue, and the evidentiary floor for any EN-6 authoring-time use.
- **Guideline-corpus RAG works when the corpus is curated:** the npj Digital Medicine preoperative-fitness study (10 LLMs, 58 guidelines, 3,234 responses) reports GPT-4+RAG at 96.4% vs 86.6% human accuracy with no observed hallucinations; a 2026 ESUR radiology-guideline RAG shows factual accuracy 0.89 vs 0.68 over baseline; a 2026 pediatric-myopia study (41 guidelines) eliminated high-risk recommendations (0% vs 6–14% baseline). Pattern across all three: tight, versioned guideline corpora — precisely a knowledge-plane discipline, not open-web retrieval.
- **Graph-structured medical RAG** (MedGraphRAG, ACL 2025; code public at [SuperMedIntel/Medical-Graph-RAG](https://github.com/SuperMedIntel/Medical-Graph-RAG), MIT, 825★) grounds generation through a three-layer graph — clinical records → literature → UMLS — a credibility hierarchy that rhymes with the tiered evidence library; [Teddy-XiongGZ/MedRAG](https://github.com/Teddy-XiongGZ/MedRAG) (ACL 2024, 590★) supplies the benchmark harness (MIRAGE, 7,663 questions) for evaluating any retrieval component you adopt.

### Argumentation × LLMs (the fabric's research frontier)

- **ArgMed-Agents** (2024): LLM agents conduct self-argumentation via clinical argumentation schemes; a symbolic solver — not the LLM — identifies the coherent argument set. The corpus's SPINE-7 doctrine, independently discovered.
- **Argumentative LLMs** (Imperial CLArg, AAAI 2025, code public): LLMs construct argumentation frameworks; formal reasoning makes the decision — explainable and, critically, *contestable*.
- **ArgEval / ArgTumour** (2025–26, same group): LLMs mine NICE glioblastoma guidelines into structured pro/con arguments per treatment option (159 arguments, 77% faithfulness-verified, NICE-supported options scored 73% vs 0% for unsupported), with *global contestability* — modifying the shared argumentation framework rather than one case. That is the corpus's Guideline Compiler assist (EN-3/EN-6) plus the guideline feedback loop (AF-5), running as a research prototype against a real guideline corpus.
- **Cautionary evidence:** mARC-QA (Sci. Reports 2025) shows frontier LLMs failing flexible clinical reasoning with overconfident uncertainty estimates — the empirical case for why the fabric's deterministic evaluator, not the LLM, must hold the release key; and an npj Digital Medicine 2026 randomized study (N=2,020 radiologist assessments) finds reasoning-style explanations improve clinician accuracy (+12.2%) where bare outputs and even differential lists do not — direct evidence for argument-shaped explanation over naked scores (SPINE-1).

### Conformal methods for LLM outputs (the qualifier discipline, extended)

- 2026 arXiv work is actively extending conformal guarantees to generation: conformal risk control for selective prediction in language models (hierarchical group-conditional, Jul 2026), bounds and impossibility results for certifying structured LLM outputs (Jun 2026), uncertainty-calibrated multimodal RAG with abstention (FinAbstain, Jul 2026), and budgeted conformal evidence acquisition before abstaining (Jun 2026). For EN-6 Class-4+ ambitions, this is the literature that decides whether an LLM output can ever carry a valid qualifier — track it; do not ship ahead of it.

## 06 — Build-vs-adopt summary

| Corpus subsystem | Verdict | Sourcing |
|---|---|---|
| Guideline execution (EN-3, PF-7) | ADOPT | CQL stack + clinical-reasoning + WHO SMART content; build only the GenericArgument annotation lift |
| Low-resource profile (XC-3) | ADOPT / STUDY | Android FHIR SDK + OpenSRP FHIR Core — a maintained, deployed embodiment; study before building anything |
| Conformal qualifiers (EN-4) | ADOPT | MAPIE (BSD-3), active into 2026 |
| Corruption/adversary harness (EN-5, AF-4) | ADOPT + BUILD | Giskard + ART for machinery; the clinical perturbation classes and theater heuristics are yours |
| Data plane + FHIR ops | ADOPT | HAPI FHIR (absorbing clinical-reasoning) |
| Tamper-evident ledger (SPINE-4) | ADAPT | Aurora PostgreSQL + transparency-log pattern (QLDB is retired); immudb if BUSL terms clear legal review |
| Formal argumentation semantics | ADAPT | TweetyProject (LGPL) as solver; Carneades as design document; ArgLLMs code as LLM-bridge reference |
| Bayesian differential engine | BUILD | pgmpy primitives; Babylon counterfactual code as patent-encumbered study material; no adoptable engine exists |
| Justification fabric, GAAM service, Deviation Composer, Compliance Projector, Dispute Mode | BUILD | No precedent in public code — the moat; de-risk via Stranieri collaboration and the ArgEval/ArgTumour pattern |

### Landmines logged this pass

- AWS QLDB retired 31 July 2025 — do not let older Mākoha docs assume it; AWS's own migration target is Aurora PostgreSQL with verification.
- immudb is Business Source License 1.1, not OSI open source — fine to run, but redistribution/embedding in a commercial SaMD needs legal reading.
- cqf-ruler is a legacy shell; deploy hapi-fhir-jpaserver-starter and the clinical-reasoning library instead.
- fasten-onprem (nearest PHR precedent) was archived July 2026 — the patient-custody space has no maintained OSS champion; PF-4 is more build than it looks.
- Babylon's counterfactual-diagnosis algorithm is under patent application and GPL-3.0 — evaluation baseline only.
- Carneades is nine years dormant; treat as literature with a compiler, not a dependency.

## 08 — J-3 Guideline-Prompt Profile applicability (v1.1, additive)

Addendum J-3 (MAK-J3) defines the exempt-tier build target realizing XC-2: guideline prompts to health professionals only, deterministic evaluation only, with Bayesian/conformal/LLM-runtime/device-ingest modules structurally absent (GPP-5/6/8). That boundary re-sorts this map: several ADOPT verdicts serve J-3 directly; others are J-1/J-2-only by construction. This section adds the per-entry disposition without altering any v1.0 verdict.

| Sourcing entry | J-3 disposition | Basis |
|---|---|---|
| ELSM-01 CQL stack · ELSM-02 clinical-reasoning · ELSM-06 WHO SMART IGs · ELSM-20 HAPI FHIR | **IN-PROFILE** | The entire J-3 engine plane is guideline execution (GPP-9: warrant type `guideline-rule` only) — these are its load-bearing dependencies |
| ELSM-04 android-fhir · ELSM-05 opensrp/fhircore | **IN-PROFILE** | J-3's low-resource delivery vehicle; intake (SDC) and offline-first faces sit inside the exempt scope; note fhircore's device-integration features must be excluded from a J-3 build (GPP-6) |
| ELSM-07 TweetyProject · ELSM-08 Carneades | **IN-PROFILE (evaluator only)** | Deterministic conflict semantics for the evaluator; no probabilistic argumentation modes in-profile (GPP-9) |
| ELSM-17 immudb · ELSM-19 Aurora+transparency-log pattern | **IN-PROFILE** | SPINE-4 ledger applies in full inside J-3 (GPP-11 stamps, GPP-2 conformity evidence) |
| ELSM-15 Giskard · ELSM-16 ART | **CI-ONLY** | GPP-CONF and adversarial testing run against the J-3 artifact in CI (GPP-10); the harness is never part of the supplied artifact |
| ELSM-12 MAPIE (conformal) · ELSM-14 pgmpy · ELSM-13 Babylon counterfactual | **EXCLUDED (J-1/J-2 only)** | Probabilistic inference is structurally absent from the J-3 build (GPP-7/8); their SBOM namespaces belong on the prohibited-namespace manifest |
| ELSM-09 argumentative-llms · ELSM-22 Medical-Graph-RAG · ELSM-23 MedRAG/MIRAGE | **AUTHORING-TIME ONLY** | LLM-assisted guideline mining (the ArgTumour pattern) may assist GenericArgument authoring under human ratification, outside the supplied artifact (EN-6 Classes 1–3; GPP capability matrix) |
| ELSM-10 GAAM implementation · ELSM-11 justification fabric | **IN-PROFILE (build)** | The fabric ships in J-3 with warrant/qualifier types narrowed (GPP-9); the build-tier verdict is unchanged |
| ELSM-18 AWS QLDB · ELSM-21 fasten-onprem | **N/A** | AVOID/STUDY verdicts unchanged; no J-3 relevance |
| ELSM-03 cqf-ruler | **N/A (legacy)** | Deploy the upstream (ELSM-20) in every tier |

**Prohibited-namespace manifest seed (GPP-8).** From this map, the initial SBOM-diff denylist for a J-3 build: `mapie`, `pgmpy` (and any PGM/Bayesian runtime), LLM runtime SDKs (Bedrock runtime invocation paths included), device-ingest/waveform libraries, and any conformal or counterfactual-diagnosis package. The manifest is a versioned conformity artifact.

## 07 — Sources

- GitHub repositories verified individually 29 Aug 2026 (stars/licenses/activity as fetched): cqframework/clinical_quality_language, cqframework/clinical-reasoning, cqframework/cqf-ruler, google/android-fhir, opensrp/fhircore, TweetyProjectTeam/TweetyProject, carneades/carneades-4, CLArg-group/argumentative-llms, scikit-learn-contrib/MAPIE, codenotary/immudb, Giskard-AI/giskard, babylonhealth/counterfactual-diagnosis, fastenhealth/fasten-onprem, Teddy-XiongGZ/MedRAG, SuperMedIntel/Medical-Graph-RAG.
- RAG evidence (2025–26): Liu et al., JAMIA systematic review & meta-analysis (RAG OR 1.35); Ke et al., npj Digital Medicine (preoperative guideline RAG, 96.4%); Komenda et al., J. Imaging Informatics in Medicine (ESUR radiology-guideline RAG); Kang et al., Scientific Reports (pediatric myopia, high-risk elimination); Gargari et al., Digital Health (narrative review); Song et al., Cancer Research & Treatment (multimodal KG-RAG, pediatric leukemia); Wu et al., MedGraphRAG (ACL 2025, arXiv:2408.04187); Xiong et al., MedRAG/MIRAGE (ACL 2024 Findings).
- Argumentation × LLM (2024–26): Hong et al., [ArgMed-Agents (arXiv:2403.06294)](https://arxiv.org/abs/2403.06294); Freedman et al., Argumentative LLMs (AAAI 2025); Dejl et al., ArgEval (arXiv 2026) and ArgTumour (Neuro-Oncology 2025); Kim et al., mARC-QA (Sci. Reports 2025); Spitzer et al., explanation formats RCT (npj Digital Medicine 2026); Ayoub et al., structured clinical framework (Communications Medicine 2026).
- Conformal for LLMs (arXiv, 2026): hierarchical group-conditional conformal risk control for selective prediction (2607.24562); conformal risk control certification bounds for structured generation (2606.29054); FinAbstain uncertainty-calibrated RAG abstention (2607.24875); budgeted conformal evidence acquisition (2606.16667).
- QLDB retirement: AWS end-of-support 31 Jul 2025; AWS migration guidance to Aurora PostgreSQL (aws.amazon.com blogs; InfoQ, Jul 2024 announcement coverage).
- Companion volumes: *The Four Faces Corpus* (requirement IDs referenced throughout), *Sleep Tools Dossier*, *The Stranieri File*.
- Addendum J-3 (MAK-J3, v0.9-proposed) — GPP-n requirements cited in Section 08; folded verbatim as Annex 1 of MAK-FFC v1.1.
- FDA. [Clinical Decision Support Software — revised final guidance](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/clinical-decision-support-software) (6 Jan 2026) · [Covington & Burling analysis](https://www.cov.com/news-and-insights/insights/2026/01/5-key-takeaways-from-fdas-revised-clinical-decision-support-cds-software-guidance) — jurisdiction-map anchor for Section 08 / MAK-J3 §2.3.

*Document footer (source artifact):* Execution Layer Sourcing Map v1.0 · every repo row reflects a direct fetch of the repository page on 29 Aug 2026, not training-data memory; statuses (archived, migrated, dormant, retired) are the load-bearing finding. GitHub's search API was unavailable from this environment, so coverage is curated-and-verified rather than exhaustive — absence claims ("no GAAM implementation found") are based on targeted searching and may be falsified by private or obscure code.

---

## Appendix A — Machine-readable inventory (additive)

Mirrors the tables above; keep in sync (self-audit check 3).

```json
{
  "doc_id": "MAK-ELSM",
  "version": "1.0",
  "verified": "2026-08-29",
  "entries": [
    {"id":"ELSM-01","name":"cqframework/clinical_quality_language","verdict":"ADOPT","license":"Apache-2.0","status":"active","serves":["EN-3"]},
    {"id":"ELSM-02","name":"cqframework/clinical-reasoning","verdict":"ADOPT","license":"Apache-2.0","status":"active; v4.7.0 2026-05","serves":["EN-3"]},
    {"id":"ELSM-03","name":"cqframework/cqf-ruler","verdict":"LEGACY","license":"Apache-2.0","status":"migrating upstream to hapi-fhir-jpaserver-starter","serves":["EN-3"]},
    {"id":"ELSM-04","name":"google/android-fhir","verdict":"ADOPT","license":"Apache-2.0","status":"active","serves":["PF-1","XC-3"]},
    {"id":"ELSM-05","name":"opensrp/fhircore","verdict":"ADOPT_STUDY","license":"Apache-2.0","status":"active; v2.2.2 2025-11","serves":["XC-3","PF-6","PF-7"]},
    {"id":"ELSM-06","name":"WHO SMART Guidelines IGs","verdict":"ADOPT","license":"CC/Apache mix","status":"active program","serves":["EN-3","PF-7","XC-4"]},
    {"id":"ELSM-07","name":"TweetyProjectTeam/TweetyProject","verdict":"ADAPT","license":"LGPL-3.0","status":"active; v1.31 2026-07","serves":["SPINE-6","EN-1"]},
    {"id":"ELSM-08","name":"carneades/carneades-4","verdict":"ADAPT_STUDY","license":"MPL-2.0","status":"dormant since 2017","serves":["SPINE-1","AF-2"]},
    {"id":"ELSM-09","name":"CLArg-group/argumentative-llms","verdict":"ADAPT","license":"see repo","status":"research-grade paper code","serves":["EN-6","SPINE-7"]},
    {"id":"ELSM-10","name":"GAAM implementation","verdict":"BUILD","license":null,"status":"no public implementation found","serves":["SPINE-1","SPINE-8","AF-2"]},
    {"id":"ELSM-11","name":"Justification fabric / deviation ledger / compliance projector","verdict":"BUILD","license":null,"status":"no precedent found","serves":["SPINE-4","SPINE-8","AF-1","AF-3","AF-7"]},
    {"id":"ELSM-12","name":"scikit-learn-contrib/MAPIE","verdict":"ADOPT","license":"BSD-3-Clause","status":"very active; v1 API 2025","serves":["EN-4"]},
    {"id":"ELSM-13","name":"babylonhealth/counterfactual-diagnosis","verdict":"STUDY_ONLY","license":"GPL-3.0","status":"dormant; patent application","serves":["EN-7 baseline"]},
    {"id":"ELSM-14","name":"pgmpy","verdict":"ADOPT","license":"MIT","status":"mature, active","serves":["EN internals"]},
    {"id":"ELSM-15","name":"Giskard-AI/giskard","verdict":"ADOPT","license":"open source","status":"active","serves":["EN-5","AF-4"]},
    {"id":"ELSM-16","name":"Trusted-AI/adversarial-robustness-toolbox","verdict":"ADOPT","license":"MIT","status":"active (LF AI)","serves":["EN-5"]},
    {"id":"ELSM-17","name":"codenotary/immudb","verdict":"ADAPT","license":"BUSL-1.1","status":"active; license review required","serves":["SPINE-4"]},
    {"id":"ELSM-18","name":"AWS QLDB","verdict":"AVOID","license":null,"status":"RETIRED 2025-07-31","serves":["SPINE-4"]},
    {"id":"ELSM-19","name":"Aurora PostgreSQL + transparency-log pattern (trillian/rekor designs)","verdict":"ADOPT_PATTERN","license":"Apache-2.0 references","status":"active","serves":["SPINE-4"]},
    {"id":"ELSM-20","name":"HAPI FHIR jpaserver-starter","verdict":"ADOPT","license":"Apache-2.0","status":"very active; absorbing clinical-reasoning","serves":["SPINE-4 data plane","EN-3"]},
    {"id":"ELSM-21","name":"fastenhealth/fasten-onprem","verdict":"STUDY","license":"GPL-3.0","status":"ARCHIVED 2026-07","serves":["PF-4"]},
    {"id":"ELSM-22","name":"SuperMedIntel/Medical-Graph-RAG","verdict":"STUDY","license":"MIT","status":"active; ACL 2025","serves":["EN-6","knowledge plane"]},
    {"id":"ELSM-23","name":"Teddy-XiongGZ/MedRAG (MIRAGE)","verdict":"ADOPT_BENCH","license":"see repo","status":"maintained; ACL 2024","serves":["EN-7 evaluation"]}
  ]
}
```

## Appendix C — J-3 applicability register (v1.1, additive)

Mirrors Section 08; keep in sync (self-audit check 7). Dispositions: IN_PROFILE, IN_PROFILE_EVALUATOR_ONLY, IN_PROFILE_BUILD, CI_ONLY, AUTHORING_TIME_ONLY, EXCLUDED, NA.

```json
{
  "doc_id": "MAK-ELSM",
  "version": "1.1",
  "profile": "MAK-J3 GPP",
  "dispositions": {
    "ELSM-01": "IN_PROFILE", "ELSM-02": "IN_PROFILE", "ELSM-03": "NA",
    "ELSM-04": "IN_PROFILE", "ELSM-05": "IN_PROFILE", "ELSM-06": "IN_PROFILE",
    "ELSM-07": "IN_PROFILE_EVALUATOR_ONLY", "ELSM-08": "IN_PROFILE_EVALUATOR_ONLY",
    "ELSM-09": "AUTHORING_TIME_ONLY", "ELSM-10": "IN_PROFILE_BUILD", "ELSM-11": "IN_PROFILE_BUILD",
    "ELSM-12": "EXCLUDED", "ELSM-13": "EXCLUDED", "ELSM-14": "EXCLUDED",
    "ELSM-15": "CI_ONLY", "ELSM-16": "CI_ONLY",
    "ELSM-17": "IN_PROFILE", "ELSM-18": "NA", "ELSM-19": "IN_PROFILE",
    "ELSM-20": "IN_PROFILE", "ELSM-21": "NA",
    "ELSM-22": "AUTHORING_TIME_ONLY", "ELSM-23": "AUTHORING_TIME_ONLY"
  }
}
```

## Appendix B — Self-audit checks (additive)

1. **Verdict vocabulary** — every verdict in tables and Appendix A appears in the frontmatter `verdict_vocabulary` (compound forms allowed: ADOPT / STUDY, ADOPT + BUILD, ADOPT PATTERN, STUDY ONLY, ADOPT_BENCH).
2. **Requirement ID resolution** — every SPINE/CF/PF/AF/EN/XC ID cited here exists in MAK-FFC v1.0 Appendix B.
3. **Table/inventory parity** — every repo row in sections 01–04 has a corresponding Appendix A entry and vice versa.
4. **Status dating** — every dependency-blocking status (RETIRED, ARCHIVED, dormant, migrating) carries a date or version anchor.
5. **Absence hedging** — every "no precedent / not found" claim is qualified by the methodology footer, never stated as proof.
6. **Link integrity** — every named GitHub repo has exactly one canonical URL in the document.
7. **J-3 register parity (v1.1)** — every ELSM-nn in Appendix A has exactly one disposition in Appendix C, the Section 08 table is consistent with it, and every GPP-n cited in Section 08 resolves in MAK-J3 v0.9-proposed (equivalently, MAK-FFC v1.1 Annex 1).
