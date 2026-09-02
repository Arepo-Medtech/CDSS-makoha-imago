---
doc_id: MAK-DOT
title: "Degrees of Truth"
version: "1.0"
date: "2026-08-30"
series: "Mākoha research series — volume 5"
status: informative-research-record-with-proposed-deltas
normative_language: "FZ-n blocks are PROPOSED requirements (argued deviations under MAK-FFC change policy) — not ratified"
req_prefix: FZ (provisional)
req_count: 6
depends_on:
  - "MAK-FFC v1.1 (The Four Faces Corpus) — all SPINE/CF/PF/AF/EN/XC IDs resolve there"
  - "MAK-ELSM v1.1 (Execution Layer Sourcing Map) — §08 J-3 denylist referenced by FZ-6"
  - "MAK-J3 v0.9-proposed (Addendum J-3) — GPP-8 referenced by FZ-6"
verification_method: "Every repository row reflects a direct fetch of the repo page on 2026-08-30; literature from 2023+ database search plus the series' primary-source base"
artifact_url: "https://claude.ai/code/artifact/5b2456b6-b3d9-468c-978f-190c42f85304"
---

<!-- LLM USAGE CONTRACT (additive; not part of the source document)
1. This document is INFORMATIVE except the FZ-n blocks, which are PROPOSED
   requirements awaiting ratification — cite them as "FZ-n (proposed)" until they
   are folded into MAK-FFC by a versioned change.
2. The load-bearing semantic rule (§03): membership degree μ = vagueness (gradedness
   of meaning); posterior/conformal = uncertainty (belief/coverage). Any generated
   design, code, or copy that renders μ or rule-activation strength as a confidence
   or probability violates FZ-1 and MAK-FFC SPINE-2 semantics.
3. Verdict vocabulary follows MAK-ELSM (ADOPT/ADAPT/STUDY etc.); statuses are dated
   observations (2026-08-30) — re-verify before dependency decisions.
4. Anti-pattern bullets carry MUST NOT force once FZ-n are ratified.
5. Requirement IDs from other documents resolve per depends_on.
END LLM USAGE CONTRACT -->

# Degrees of Truth

Fuzzy logic in a triple-facing CDSS: the sixty-year lineage, the current literature, the verified tooling, and the precise — deliberately narrow — place where fuzzy methods strengthen the Four Faces Corpus without corrupting its uncertainty semantics.

**Document metadata:** Research dossier · compiled 30 Aug 2026 · fifth volume in the Mākoha research series.

## The short version

> Fuzzy logic earns a place in Mākoha — but not the place the primer sketches. Its rightful role is at the **circumrational boundary**: formalizing the vague linguistic terms that guidelines and patients actually use ("elderly," "mildly elevated," "poor sleep") as versioned, ratified membership functions attached to *grounds and warrant applicability* — killing the cliff effects where 139 mmHg and 141 mmHg produce different universes. What it must never become is a rival inference engine or a source of pseudo-confidence: **fuzziness is vagueness (degrees of meaning), not uncertainty (degrees of belief)**, and the primer's "78% confidence" — a rule-activation strength dressed as a probability — is precisely the semantic soup the argument schema exists to prevent. The good news is structural: fuzzy inference is deterministic arithmetic with zero learned parameters, so it is natively SPINE-7-compatible and J-1-compatible; the tooling is mature, verified, and even has an IEEE standard (1855-2016 FML) that makes membership functions serializable, versionable, ratifiable knowledge-plane artifacts. The field's own 2025–26 literature is asking for "regulation-ready, interpretable, expert-editable" fuzzy CDSS — which is to say, it is asking for the governance your corpus already specifies.

## 01 — The lineage: fuzzy medicine is older than most of CDSS

Zadeh's fuzzy sets (1965) reached medicine early and deeply. Kazem Sadegh-Zadeh built a philosophy of medicine on the insight that disease categories are graded; Klaus-Peter Adlassnig's **CADIAG-2** at the Vienna General Hospital (1980s) encoded symptom–disease relationships as fuzzy relations and ran against real hospital data for decades — one of the few knowledge-based diagnostic systems ever routinely connected to a hospital information system. The series has already met this lineage without naming it: the Blake–Kerr–Gammack program cites **Seising (2006)** — "it is very difficult to define sharp borders between various symptoms… and between various diseases" — as its warrant for pairing formal criteria with clinical judgment, and **Stranieri himself** published fuzzy work at both ends of his career: fuzzy-evolutionary macroeconomic forecasting (1999) and a pruned fuzzy min–max neural network *with rule extraction* for patient admission prediction (Neural Computing & Applications, 2015) — characteristically insisting that the fuzzy model surrender readable rules. Fuzzy logic is not an exotic bolt-on to this project's intellectual base; it is a suppressed premise of it.

## 02 — The current literature (2024–2026)

The field is active and — read against the corpus — converging on your problems without your machinery:

- **Reviews:** a 2025 PRISMA review of fuzzy logic across chronic-disease diagnosis (25 studies: diabetes, CVD, cancers, liver, thyroid…) finds broad diagnostic use but a research agenda still centred on single-disease scorers; a 2025 systematic review of ANN + attention + fuzzy hybrids (32 studies) credits fuzzy specifically with "robust handling of ambiguity… through continuous degrees of membership" inside otherwise black-box stacks.
- **The agenda paper:** a 2026 fuzzy-expert-systems roadmap calls for structured elicitation of fuzzy knowledge bases from clinicians, adaptive membership tuning, an explainability layer of human-readable IF–THEN rules, uncertainty quantification, conflict resolution between knowledge sources, and "regulation-ready" architectures that preserve clinician autonomy — a near-verbatim request for the knowledge plane, the argument fabric, SPINE-6 conflict materialization, and AF-5 governance.
- **Type-2 fuzzy** (membership functions whose boundaries are themselves uncertain) is the growth area: interval type-2 knowledge bases for anaesthesia pre-op assessment (2024), type-2 + DEMATEL/VIKOR for patient bed allocation (2025), type-2 semantic-ontology diabetes CDSS (2024). Type-2's clinical meaning: *the experts disagree about where "elderly" begins* — a formal home for inter-clinician disagreement.
- **Fuzzy cognitive maps:** a 2026 *Scientific Reports* framework couples data-driven FCM weight learning with an explicit *expert-correction operator* and stability proofs — governed human override of learned structure, which is AF-5's ratification loop discovered independently in the FCM idiom.
- **Hybrids:** fuzzy preprocessing + logistic regression for T2DM prediction (2025) reports AUC gains over pure-ML baselines with interpretability retained — evidence for fuzzy as *input semantics for a probabilistic engine* rather than as the engine itself.

The persistent gap mirrors the CDSS literature at large: no multi-stakeholder rendering, no deviation machinery, no membership-function governance, no regulatory mapping. The fuzzy community has the mathematics and asks for the governance; the corpus has the governance and can adopt the mathematics.

## 03 — The load-bearing distinction: vagueness ≠ uncertainty

Everything in this dossier hangs on one distinction the primer blurs. A membership degree μ_elevated(142/92) = 0.72 says the reading *partially satisfies the meaning* of "elevated" — a fact about language and category boundaries, true even with a perfect measurement. A posterior P(hypertensive disease | evidence) = 0.72 says how strongly the evidence supports a claim — a fact about belief under incomplete information. Conformal coverage says how often the claim-set traps the truth. These three numbers can coexist in one decision and mean entirely different things; collapse them into one "confidence %" and the clinician face misleads, the patient face lies, and the auditor face cannot audit. The corpus's argument schema already has distinct homes for all three:

| Quantity | Semantics | Home in the argument object |
|---|---|---|
| Membership degree μ | Gradedness of a linguistic ground or of a warrant's applicability precondition ("elderly to degree 0.8") | **Grounds annotation** and **warrant-applicability grading** — never the Qualifier |
| Posterior probability | Belief in the claim given the evidence | Qualifier (Bayesian differential) |
| Conformal set + coverage | Distribution-free guarantee on the claim set | Qualifier (conformal wrapper, EN-4) |
| Rule-activation strength | Degree to which a fuzzy rule fired — an *intermediate computation* | Evaluation trace (auditor-visible), never rendered as confidence |

## 04 — Where fuzzy slots into the Four Faces architecture

The primer's pipeline (fuzzify → infer → defuzzify → per-persona adaptation layer) is the classic Mamdani control loop. Mapped onto the corpus, its pieces land in different places than it assumes — and two of its moves must be corrected, not adopted.

### Adopted, with placement

| Fuzzy component | Corpus placement | What it does there |
|---|---|---|
| Fuzzy Knowledge Base (linguistic variables, membership functions) | **Knowledge plane** (SPINE-5/6, EN-3) | Membership functions become versioned, ratified artifacts — serialized in IEEE 1855-2016 FML — entering only through the Guideline Compiler, exactly like every other piece of clinical logic. "Elderly," "elevated," "poor sleep efficiency" get one governed definition per guideline lineage, jurisdiction-adaptable under XC-4. |
| Fuzzification Engine | **Data plane → grounds preparation** | Crisp values acquire gradedness annotations against the ratified linguistic variables at capture time; the annotation carries the membership-function version pin. This is circumrational boundary work given a formalism — the corpus's Chapman thesis, operationalized. |
| Fuzzy Inference (rule evaluation) | **Warrant-applicability grading inside per-criterion engines** (EN-2) | Where a guideline criterion is inherently hedged ("consider X in elderly patients with borderline control"), the GenericArgument warrant carries a fuzzy precondition; its evaluation yields graded applicability. Release still requires the ratified crisp threshold recorded in the template — deterministic, replayable, SPINE-7-clean. |
| Defuzzification | **Inside the deterministic evaluator, against template-ratified thresholds** | The defuzzified value never leaves as a bare score (SPINE-1); it feeds the argument's evaluation trace, and any face-visible consequence is a claim with the full argument attached. |
| Membership visualisations ("where 145/90 sits on the scale") | **Register renderings** (SPINE-3, PF-5) | The primer's patient flow is right and matches the Blake diary lesson: gradedness renders as a sliding scale in the plain register, as μ-annotated criteria in the clinical register, as full membership math + rule firings in the compliance register — one argument, three renderings. |
| Fuzzy boundary structure | **Corruption engine test class** (EN-5) | Membership supports mark exactly where cliff-effect adversarial cases live; the corruption engine sweeps membership boundaries and publishes failures as rebuttals. Fuzzy sets double as an adversarial-test map. |
| Fuzzy cognitive maps | **Authoring-time only** (EN-6 Classes 1–3 analogue) | Causal sketching during guideline compilation and AF-5 change-proposal analysis; never a runtime engine. |

### Corrected, with reasons

- **The "Triple-Facing Adaptation Layer" is already built — and stricter.** The corpus renders one argument object in three registers (SPINE-3) and forbids renderers to add, remove, or reweight content per audience. The primer's layer, read literally, would let each face receive differently shaped decisions; that is the three-truths failure mode SPINE-9 exists to prevent. Keep the persona sensitivity; discard the per-persona content shaping.
- **"78% confidence" is prohibited output.** A defuzzified activation is not a probability; rendering it as one violates the vagueness/uncertainty separation (§03) and would poison the conformal qualifier's meaning. The clinician sees μ-graded criteria plus the Bayesian/conformal qualifier, each labelled as what it is.
- **The auditor's "nudge the membership curve to reduce alert fatigue" dial is an ontology change, not a UI affordance.** Membership functions are ratified knowledge-plane artifacts; changing one to suppress alerts is precisely the alert-governor-abuse risk in the corpus register. The correct loop exists: deviation and override aggregates → AF-5 change proposal → governed ratification → new membership-function version, with the old version pinned to its historical decisions (SPINE-5). The primer's instinct (tune curves from override evidence) is right; only the governance is missing.
- **Fuzzy risk scoring stays out of J-3.** The subtle point: fuzzy inference is deterministic and transparent — criterion (c)-friendly in *form* — but a fuzzy-derived patient risk grade is new diagnostic information, which fails exemption criterion (a) regardless of transparency. Fuzzy engines are J-1/J-2 components; the J-3 SBOM denylist (MAK-ELSM §08) gains the fuzzy namespaces (`skfuzzy, simpful, pyfuzzylite, pyit2fls`). Verbatim display of a guideline's own hedge language remains fine in J-3.

### Type-2: the disagreement formalism — deferred

Interval type-2 fuzzy sets put uncertainty bands around the membership functions themselves — formally: the experts do not agree where "elderly" begins. That is a natural fit for MDT disagreement (CF-6) and for pluralist guideline lineages (SPINE-6), and the tooling exists (PyIT2FLS, MIT, active 2025). Verdict: **defer**. Type-1 with governed versioning captures most of the value at a fraction of the explanatory burden; adopt type-2 only when a real ratification dispute produces evidence that a disagreement band, not a decision, is what the community can ratify. Record the trigger, not the machinery.

## 05 — Verified tooling and standards

| Tool / standard | What it gives you | Status (verified 30 Aug 2026) | Verdict |
|---|---|---|---|
| [scikit-fuzzy](https://github.com/scikit-fuzzy/scikit-fuzzy) | General Python fuzzy toolkit on SciPy: membership functions, Mamdani control, fuzzy c-means | 872★ · Python · v0.5.0 Aug 2024 · active | ADOPT (prototyping) |
| [Simpful](https://github.com/aresio/simpful) | Fuzzy inference with rules as *readable strings* — Mamdani + Sugeno; the natural-language rule format is ideal for clinician-reviewable warrant preconditions; companion pyFUME learns fuzzy models from data | 148★ · AFL-3.0 · IJCIS 2020 paper · maintained | ADOPT |
| [pyfuzzylite / fuzzylite](https://github.com/fuzzylite/pyfuzzylite) | Six controller types, 25 term shapes, 7 defuzzifiers, vectorized; FLL language plus FCL/FIS interchange via the C++ sibling | 81★ · GPL-3.0 + commercial dual license · v8.0.6 · active | ADAPT (license review for SaMD) |
| [PyIT2FLS](https://github.com/Haghrah/PyIT2FLS) | Type-1 and interval type-2 systems, Mamdani/TSK, NumPy/SciPy-based | 87★ · MIT · v0.8.6 Apr 2025 · active | STUDY (type-2 deferral) |
| [JFML](https://github.com/sotillo19/JFML) + **IEEE Std 1855-2016 (FML)** | The IEEE-standard XML serialization for fuzzy systems, with the reference Java library — membership functions as standard, versionable, diffable knowledge-plane artifacts; conformity-file-grade provenance for every linguistic variable | IEEE standard · Java reference lib (Univ. Córdoba) · IEEE Access 2018 paper | ADOPT AS FORMAT |
| jFuzzyLogic + IEC 61131-7 (FCL) | The older Fuzzy Control Language standard and its Java implementation | Aging; FML supersedes for interchange | STUDY |
| [FCMpy](https://github.com/SamvelMK/FCMpy) | Fuzzy cognitive map construction, simulation, and learning (PeerJ CS 2022; arXiv:2111.12749) | Python · open source · research-grade | AUTHORING-TIME STUDY |
| MATLAB Fuzzy Logic Toolbox | Rapid membership-function design and surface visualization | Commercial | PROTOTYPING ONLY |

**The standards finding matters most.** IEEE 1855-2016 gives membership functions and rule bases a standard, machine-readable, human-diffable serialization. That converts the corpus requirement "fuzzy semantics are governed knowledge-plane artifacts" from aspiration to file format: a linguistic variable's definition becomes an FML document with a version, an author, a ratification record, and a place in the SPINE-5 pin-set — reviewable by an auditor and exportable in an AF-7 conformity bundle.

## 06 — Proposed corpus deltas (for ratification, not yet ratified)

Six candidate requirements, offered as argued deviations to MAK-FFC per its own change policy. Prefix `FZ` provisional.

### FZ-1 (MUST — proposed)
**Statement:** Vagueness and uncertainty are type-separated end to end: membership degrees attach to grounds and warrant-applicability only; posteriors and conformal sets own the Qualifier; rule-activation strengths live in the evaluation trace. No face renders a membership degree or activation strength as a probability, confidence, or percentage of certainty.
**Rationale trace:** §03; SPINE-2; Abbas 2025 (unvalidated confidence is a liability).

### FZ-2 (MUST — proposed)
**Statement:** Every linguistic variable and membership function is a knowledge-plane artifact: serialized in IEEE 1855-2016 FML, versioned, ratified through the Guideline Compiler path (EN-3), pinned per decision (SPINE-5), and jurisdiction-adaptable as a sibling lineage (XC-4). Ad-hoc or code-embedded membership definitions are prohibited.
**Rationale trace:** §05 standards finding; EN-3 single change surface; ICSD-freeze lesson.

### FZ-3 (MUST — proposed)
**Statement:** Fuzzy evaluation releases nothing directly: graded applicability feeds the deterministic evaluator, whose release thresholds are crisp values ratified inside the GenericArgument template. Defuzzified values are evaluation-trace content, never face-released scores.
**Rationale trace:** SPINE-1/7; §04 corrections.

### FZ-4 (MUST — proposed)
**Statement:** Membership-function change is AF-5 governed change: proposals may cite override and alert-fatigue evidence, ratification produces a new FML version, and prior decisions replay against their pinned versions. No runtime, per-user, or UI-mediated tuning of membership functions exists in any face.
**Rationale trace:** §04 correction of the primer's auditor dial; CF-5 alert-governor discipline; SPINE-5.

### FZ-5 (SHOULD — proposed)
**Statement:** The corruption engine maintains a boundary-sweep test class derived from the ratified membership supports, publishing cliff-effect and boundary-instability findings as rebuttals on the affected warrants.
**Rationale trace:** EN-5; fuzzy sets as adversarial map (§04).

### FZ-6 (MUST — proposed)
**Statement:** Fuzzy inference namespaces (`skfuzzy`, `simpful`, `pyfuzzylite`, `pyit2fls` and equivalents) join the J-3 prohibited-namespace manifest (MAK-J3 GPP-8; MAK-ELSM §08): fuzzy-derived patient grading is new diagnostic information and fails exemption criterion (a) notwithstanding its deterministic transparency. Verbatim display of a guideline's own hedge language remains in-profile.
**Rationale trace:** MAK-J3 §2.2; TGA criterion (a) recommendation definition; §04 regulatory note.

### Anti-patterns (carry MUST NOT force once FZ-n are ratified)

- Never render μ, activation strength, or defuzzified output as "confidence" — in any register.
- Never let fuzzy inference become a parallel engine emitting its own recommendations beside the Bayesian differential; it grades inputs and applicability for the one argument pipeline.
- Never tune membership functions outside AF-5 governance — including "just for this clinic."
- Never adopt type-2 machinery before a real ratification dispute demonstrates the need (§04 deferral trigger).

## 07 — Sources

- Repositories verified individually 30 Aug 2026: [scikit-fuzzy/scikit-fuzzy](https://github.com/scikit-fuzzy/scikit-fuzzy) · [aresio/simpful](https://github.com/aresio/simpful) · [fuzzylite/pyfuzzylite](https://github.com/fuzzylite/pyfuzzylite) · [Haghrah/PyIT2FLS](https://github.com/Haghrah/PyIT2FLS) · [sotillo19/JFML](https://github.com/sotillo19/JFML) · [SamvelMK/FCMpy](https://github.com/SamvelMK/FCMpy).
- Standards: IEEE Std 1855-2016 (Fuzzy Markup Language; [JFML paper, IEEE Access 2018](https://ieeexplore.ieee.org/document/8476558/); [uco.es/JFML](http://www.uco.es/JFML/)) · IEC 61131-7 (Fuzzy Control Language).
- Literature (2024–26, via Consensus): Thukral et al. 2025, fuzzy logic in chronic-disease decision-making (Informatics for Health & Social Care) · Zacarias-Morales et al. 2025, ANN + attention + fuzzy systematic review (AI) · Cherukuri et al. 2026, fuzzy-logic-driven expert systems for clinical decision-making (IJDDT) · Zakaria 2026, human-centric FCM decision support (Scientific Reports) · Chen et al. 2025, interval type-2 MCDM bed allocation (Scientific Reports) · Malyar et al. 2024, type-2 fuzzy knowledge bases for anaesthesia assessment · Dadashkarimi 2025, hybrid fuzzy + logistic regression T2DM · Manikandabalaji et al. 2024, type-2 fuzzy semantic-ontology diabetes CDSS · Sabahi 2024, extended fuzzy logic causality in CHD.
- Lineage: Zadeh 1965 (fuzzy sets) · Adlassnig, CADIAG-2 (Vienna, 1980s–) · Seising 2006 (cited by the Blake–Kerr–Gammack program; see Sleep Tools Dossier) · Stranieri et al. 2015, pruned fuzzy min–max NN with rule extraction for patient admission (Neural Computing & Applications; see The Stranieri File) · Dubois & Prade on possibility vs probability.
- Companion volumes: *The Four Faces Corpus* (MAK-FFC v1.1), *Execution Layer Sourcing Map* (MAK-ELSM v1.1), *Addendum J-3* (MAK-J3), *Sleep Tools Dossier*, *The Stranieri File*.

*Document footer (source artifact):* Degrees of Truth v1.0 · repo rows reflect direct fetches on 30 Aug 2026; literature drawn from 2023+ database search plus the series' primary-source base. The FZ-n deltas are proposals under MAK-FFC's change policy — argued deviations awaiting ratification, not ratified requirements.

---

## Appendix A — Proposed-ID census (additive)

```json
{
  "doc_id": "MAK-DOT",
  "version": "1.0",
  "proposed_requirements": {
    "FZ": ["FZ-1","FZ-2","FZ-3","FZ-4","FZ-5","FZ-6"]
  },
  "levels": {
    "MUST": ["FZ-1","FZ-2","FZ-3","FZ-4","FZ-6"],
    "SHOULD": ["FZ-5"]
  },
  "ratification_status": "proposed — argued deviations under MAK-FFC change policy",
  "fold_target_on_ratification": "MAK-FFC (new FZ section or SPINE/EN amendments) + MAK-ELSM §08 denylist (FZ-6) + MAK-J3 capability matrix (FZ-6)"
}
```

## Appendix B — Self-audit checks (additive)

1. **ID census parity** — FZ-n headers exactly match Appendix A (6).
2. **Level parity** — header levels match Appendix A buckets.
3. **Proposed status discipline** — every FZ-n header carries "(… — proposed)" until ratification; on ratification, this document gains a changelog entry and the fold targets in Appendix A are updated together.
4. **Semantic-separation guard** — no table, example, or rendering in this document presents μ, activation strength, or a defuzzified value as a probability/confidence (the §03 rule applied to the document itself).
5. **Cross-doc resolution** — every SPINE/CF/PF/AF/EN/XC/GPP ID cited resolves in MAK-FFC v1.1 (Annex 1 included) — and every ELSM-nn in MAK-ELSM v1.1.
6. **Status dating** — every tooling status carries its verification date; re-verify before dependency decisions.
