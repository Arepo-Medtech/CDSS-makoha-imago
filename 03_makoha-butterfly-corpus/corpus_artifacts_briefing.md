# The Mākoha Butterfly Corpus — Briefing

**Source:** `ECOSYSTEM/makoha-imago-v1.2/03_makoha-butterfly-corpus`
**Contents:** 15 prompt-ready corpus files (`corpus-md/`) and 16 published artifact pages (`artifacts-html/`), assembled 1 Sep 2026.

---

## Part 1 — What a corpus is, and what an artifact is

*Ecosystem-agnostic. Two document types, one pipeline.*

### The CORPUS document

A corpus is a **normative specification for one domain of a system, written as numbered requirements with their reasoning attached**. Where a primer specifies a *component to build*, a corpus specifies a *law to satisfy* — closer to an RFC than to a design doc, and written to be loaded into a model's context as prompt-ready source.

Machine-readable frontmatter carries the contract:

| Field | Function |
| --- | --- |
| `doc_id` | Stable short identifier; requirements resolve against it |
| `req_prefixes` / `req_count` | The ID namespaces this volume owns, and how many it declares |
| `status` | `normative-draft`, or a split like `informative-defaults + normative bindings` |
| `normative_language` | RFC 2119 — MUST / SHOULD / MAY |
| `subordinate_to` | Which volume outranks this one, stated explicitly |
| `builds_from` / `absorbs` / `folds_in` | Lineage — what it consolidates, supersedes, or carries verbatim |
| `governed_by` | The cross-cutting policy that binds it |
| `changelog` | Per-version, with an explicit no-content-altered assertion |
| `change_policy` | IDs stable across versions; retired IDs never reused |

The body follows a fixed spine:

**Contents → Thesis → Part 0 (how to use) → Part 1 (foundation) → domain parts → traceability & sources → ID census → self-audit checks.**

The unit of content is the requirement block, and its shape is the design decision that matters most:

```
### FS-3 (MUST)
**Statement:** Type separation is enforced end to end…
**Rationale trace:** A1; MAK-DOT §03 and FZ-1; Abbas 2025.
```

Every requirement carries its provenance inline. A reader challenging a rule does not hunt for the argument — the axiom, the prior document, and the citation sit on the same line. The **ID census** and **self-audit checks** appendices then let a document verify itself: declared count against actual, cross-references against targets.

Three conventions make the set composable:

- **Additive-only revision** — v1.1 appends a new Part, alters nothing in v1.0.
- **Explicit subordination** — no volume relaxes a host MUST, and narrowings are stated.
- **Consolidation without retirement** — a volume that maps three sources produces cross-walks, never replacements.

### The ARTIFACT document

Each corpus has a published HTML companion at a stable URL, cross-referenced from the corpus frontmatter as `artifact_url`. The corpus is the prompt-ready source of truth; the artifact is the readable, shareable, series-designed presentation. One pair, two audiences — the model reads the markdown, a person reads the page.

The mapping is not one-to-one, and the exceptions are informative:

- **14 paired** — corpus and artifact both exist.
- **1 corpus without an artifact** — the J-3 addendum, folded verbatim into the host as Annex 1 rather than published separately.
- **2 artifacts without a corpus** — the two research dossiers that open the series, which are findings rather than law.

---

## Part 2 — The set as ECOSYSTEM items

The organising scheme is the butterfly. Anatomy is the taxonomy, and it does real work — position on the body encodes the volume's role.

### Host and precedence

| doc_id | Volume | Role |
| --- | --- | --- |
| `MAK-FFC` | The Four Faces Corpus (v1.1, 46 reqs) | The body, and the law. No subordinate volume relaxes a corpus MUST; where volumes appear to differ, the host governs. |
| `MAK-ELSM` | Execution Layer Sourcing Map (v1.1, 23 entries, informative) | The sourcing record — verdicts per subsystem. |
| `MAK-J3` | Guideline-Prompt Profile (v0.9-proposed, 16 GPP) | Exempt-tier reserve; folded into MAK-FFC as Annex 1. |

### The wings — the two reasoning traditions

| doc_id | Volume | Content |
| --- | --- | --- |
| `MAK-LWC` | Left Wing (v1.1, 43 reqs — FS/FC/FP/FA/FE/FX) | Fuzzy logic. Linguistic variables as first-class artifacts, μ-vectors as additive annotation, type separation enforced so degrees of meaning can never masquerade as probability. Absorbs the `MAK-DOT` research base. |
| `MAK-RWC` | Right Wing (v1.1, 42 reqs — MS/MC/MP/MA/ME/MX) | Meta-rationality. |

Both wings use a symmetrical prefix structure — Spine, Clinician, Patient, Auditor, Engines, Cross-cutting — so the same six-part frame is answered twice from two epistemologies.

### The engine plane

| doc_id | Volume | Content |
| --- | --- | --- |
| `MAK-CEC` | Compound Eyes (v1.1, 38 reqs — OM/CP/DX/QU/AD/RG) | Verdicts with stage traces, the five-signal registry. The layer the faces consume. |

### The three faces, consolidated from both wings

| doc_id | Volume | Face | Reqs |
| --- | --- | --- | --- |
| `MAK-HDC` | Head | Clinician | 30 (HW/HR/HA/HG/HT/HE) |
| `MAK-TXC` | Thorax | Patient | 28 (TW/TR/TA/TC/TL/TE) |
| `MAK-ABC` | Abdomen | Auditor | 27 (AL/AR/AG/AT/AX/AE) |

### The mouthparts — the two user interfaces

| doc_id | Volume | Content |
| --- | --- | --- |
| `MAK-PRB` | Proboscis (27 reqs — PV/PS/PC/PI/PA) | Patient UI. |
| `MAK-LBP` | Labial Palps (26 reqs — CV/CS/CC/CI/CA) | Clinician UI. |

### The legs — the stack

| doc_id | Volume | Content |
| --- | --- | --- |
| `MAK-LEG` | Legs (23 reqs — LS/L1..L6) | Six legs: frontend, backend, database, cache & queue, storage, infrastructure & deploy. Explicitly self-limiting — named technologies are a reasonable example, not a ruleset. Only the binding constraints are law; defaults may be swapped freely where bindings hold. |

### The antennae — regulatory sensing

| doc_id | Volume | Content |
| --- | --- | --- |
| `MAK-ANT` | Antennae (12 AN reqs) | Folds REG-POSTURE v1.0 verbatim as Annex 1. Read *last and always*: citation surface, precedence rules, and the open `ASSUME-REG-001..007` items pending counsel attestation. The posture assumes inclusion rather than exemption, treats glass-box as the design target, and holds J-1/J-2 as lower- and higher-class included variants. |

### Doctrine and dossiers

- `MAK-MIF` — **Mākoha in Flight** (8 beats, informative). The flight doctrine.
- **Sleep Tools Dossier** (series vol. 1) and **The Stranieri File** (series vol. 2) — artifact-only research dossiers that open the series as its research base.

---

## Reading order for prompt work

1. `MAK-FFC` (host law) → `MAK-MIF` (flight doctrine) → `MAK-LWC` + `MAK-RWC` (the wings).
2. `MAK-CEC` (engine plane) → `MAK-HDC` / `MAK-TXC` / `MAK-ABC` (the faces).
3. `MAK-PRB` / `MAK-LBP` (the UIs) → `MAK-LEG` (the stack).
4. `MAK-ANT` last and always.
