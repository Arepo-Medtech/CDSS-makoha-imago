# The PRIMERs — Briefing

**Source:** `ECOSYSTEM/makoha-imago-v1.2/02_cdss-stack-augmented`
**Scope:** 13 lettered primers (0, A–L) plus `harness_ml_primer.md`, alongside four non-primer companions.

---

## Part 1 — What a primer is

*Ecosystem-agnostic. Hand this half to anyone unfamiliar with the project.*

A primer is a **single-component specification written to be built in isolation and assembled later**. One component, one document, fixed skeleton. It is not a design doc, not a README, and not an ADR — it sits above code and below architecture, and its job is to let an engineer who knows nothing about the rest of the system build their piece correctly and hand it over without a negotiation.

Every primer carries the same eleven-part structure, which is where most of its value sits:

| Section | Answers |
| --- | --- |
| **X1 What this is** | One paragraph. The component's identity and defining property. |
| **X2 Scope** | Explicit **in scope** and **out of scope**. The out-of-scope list names the neighbouring component that owns each excluded thing. |
| **X3 Breadth and depth** | How much content is required to be real, not a demo. |
| **X4 Building in a silo** | What can be built with no dependencies on anything else. |
| **X5 Folding it in** | The integration contract — what it consumes, what it emits. |
| **X6 Definition of done** | Release-gating criteria, per release. |
| **X7 Internal operations diagram** | The component's own mechanics. |
| **X8 Execution layer** | Build steps. |
| **Topology annotations** | Where it runs (production) and which ledgers it writes to (register). |
| **X9 Build execution extension** | Version-scoped build detail. |
| **X10 Hardening annex** | Additive later-version binding, appended without editing prior text. |

Two structural conventions do the heavy lifting:

**A shared epigraph with a per-document position clause.** Every primer opens with the identical statement of the system's governing doctrine, then one sentence naming *this component's position within it*. Same constitution, different seat. A reader can open any primer cold and know where they are.

**Additive-only revision.** Later passes append annexes rather than editing what came before. The document's history is legible; nothing silently changes underfoot.

The result is a set that composes. Because scope boundaries are stated from both sides — each primer names what it doesn't do and who does — the seams are declared rather than discovered during integration.

---

## Part 2 — The primers as ECOSYSTEM items

**Primer 0 — Ecosystem Explainer.** The front door, and structurally different from the rest: charter-exempt, no build blocks, no obligations. Plain-language cast list, one worked consultation end to end, a glossary of house vocabulary, and reading paths by role (engineer / clinician advisor / regulator / investor). Everything else assumes it has been read.

The twelve lettered primers group into four bands.

### The spine — what computes and what releases

| | Component | Position |
| --- | --- | --- |
| **A** | Bayesian engine | The principal probabilistic proposer. Reconstructible arithmetic: prior → LR → posterior, logged per step. Deliberately not a learned model. |
| **B** | Evidence library | Every number the engine computes over, tiered E1/E2/E3. Data and governance, never a service. |
| **D** | Content registry | The spine made concrete. Signed fragments, five arithmetic gates. Nothing generative writes to it; nothing renders except from it. |
| **E** | Graph RAG | The most sophisticated selector in the system, and still only a selector. Traversal returns pointers; the registry verifies. |

### The three attachments that raise the spec

| | Component | Position |
| --- | --- | --- |
| **F** | Conformal wrapper | Converts posteriors into guaranteed-coverage sets. Bought with held-out data, not model quality. |
| **G** | Corruption engine | The in-house saboteur. Guaranteed-wrong material with labels true by construction; gates must catch 100% of the safety class. |
| **H** | Lumos pathway | A programme, not a codebase. NSW GP-to-outcome linkage — the only Australian asset that can settle whether the posteriors match reality. Also the one item engineering effort cannot compress. |

### The lattices — governance running across everything

| | Component | Position |
| --- | --- | --- |
| **I** | Living evaluation | Six regenerating mechanisms replacing frozen regression, plus the incident ledger as the sanctioned exception. |
| **J** | Model governance | The passport office. No card, no deployment; no model verifies anything whose errors it shares. |
| **K** | LLM augmentation | Twenty behind-the-scenes points, three classes, no classification impact. |
| **L** | Runtime LLM | The frontier, available only under full device posture. Explicitly framed as *what classification buys*. |

### Independent instrument

| | Component | Position |
| --- | --- | --- |
| **C** | Casebundle corpus | The firewalled exam. Value is entirely that nothing under test has learned from it; the firewall is structural, enforced by credentials rather than policy. |

### Companion (primer-named, harness-scoped)

**Harness ML primer** — the offline workshop where the learned artifacts live. Its models propose and test; none release.

---

## Non-primer files in the same folder

- `architecture_and_integration.md` — repos, maturity levels, register topology
- `cdss_complete_stack.md` — the consolidated spec (291 KB)
- `grounding_and_weak_supervision.md`
- `ecosystem_integration_report.md`
- `cdss_diagrams.html`
- `variant_1b_deterministic_coder.md` and `variant_2_ml_coder_runtime.md` — the two coder-fork options corresponding to the J-1 / J-2 decision
