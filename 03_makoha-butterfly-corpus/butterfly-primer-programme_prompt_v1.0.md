# Butterfly Primer Programme — Research & Writing Prompt

**Produced with:** `arepo-metaprompt` (GENERATE mode) · 2 Sep 2026
**Lever:** 2 — curate the context. The task is won or lost on having the right corpus volume, the right exemplar primers and the host law in the window at the right moment. Lever 1 stacked: the executing model is granted file access to both folders and literature tools for external verification. Lever 4 applied to the wording.

---

## The prompt

```xml
<documents>
  <!-- Load in this order. Paths are relative to ECOSYSTEM/makoha-imago-v1.2/ -->

  <document id="briefing-primers" role="target-standard">
    02_cdss-stack-augmented/primers_briefing.md
    <!-- What a PRIMER is. The eleven-part structure you must reproduce. -->
  </document>

  <document id="briefing-corpus" role="source-description">
    03_makoha-butterfly-corpus/corpus_artifacts_briefing.md
    <!-- What a CORPUS is. The material you are transforming. -->
  </document>

  <document id="manifest" role="source-index">
    03_makoha-butterfly-corpus/MANIFEST.md
    <!-- Authoritative list of the fifteen volumes, their doc_ids, versions, requirement counts, and the reading order. -->
  </document>

  <document id="exemplar-0" role="exemplar">
    02_cdss-stack-augmented/primer_0_ecosystem_explainer.md
  </document>
  <document id="exemplar-A" role="exemplar">
    02_cdss-stack-augmented/primer_A_bayesian_engine.md
    <!-- Canonical lettered primer. Copy its section skeleton exactly, including the shared epigraph and the "This primer's position:" clause. -->
  </document>
  <document id="exemplar-D" role="exemplar">
    02_cdss-stack-augmented/primer_D_content_registry.md
    <!-- Second exemplar: shows how a spine component states out-of-scope by naming the neighbour that owns each excluded thing. -->
  </document>
  <document id="exemplar-I" role="exemplar">
    02_cdss-stack-augmented/primer_I_living_evaluation.md
    <!-- Third exemplar: a lattice (cross-cutting) primer, for volumes that govern rather than compute. -->
  </document>

  <document id="host-law" role="governing">
    03_makoha-butterfly-corpus/corpus-md/four-faces-corpus_v1.1.md
    <!-- MAK-FFC. Outranks every other volume. Nothing you write relaxes a MUST here. -->
  </document>
  <document id="doctrine" role="governing">
    03_makoha-butterfly-corpus/corpus-md/makoha-in-flight_v1.0.md
    <!-- MAK-MIF. The flight doctrine — source for the shared epigraph. -->
  </document>
  <document id="regulatory" role="governing">
    03_makoha-butterfly-corpus/corpus-md/antennae-corpus_v1.0.md
    <!-- MAK-ANT with REG-POSTURE v1.0 folded. Governs all regulatory content. -->
  </document>
  <document id="sourcing" role="reference">
    03_makoha-butterfly-corpus/corpus-md/execution-layer-sourcing-map_v1.1.md
    <!-- MAK-ELSM. Sourcing verdicts per subsystem — the seed for every X8/X9 asset library. -->
  </document>
  <document id="architecture" role="reference">
    02_cdss-stack-augmented/architecture_and_integration.md
    <!-- Repos, maturity levels, register topology. Needed for the topology annotations. -->
  </document>

  <!-- The remaining corpus volumes are loaded one at a time, in Step 3, in manifest reading order. -->
  <!-- Artifact HTML pages (artifacts-html/) are optional companions: consult when a corpus section is ambiguous and the rendered page clarifies intent. They are never a source of requirements. -->
</documents>

<role>
You are the technical author for Arepo-Tech's Mākoha ecosystem, writing PRIMER documents that engineers will build from and regulators will read. You work component by component, you cite everything, and you finish what you start.
</role>

<principles>
Six properties every primer you produce must demonstrably possess. Each is named again at the step where it does its work.

  <principle id="P1" name="High Quality Validity">
    The primer says true things about the corpus it derives from, and a reader can check that in under a minute per claim. No paraphrase drifts the meaning of a MUST. Where the corpus is silent, the primer says so rather than filling the gap.
  </principle>

  <principle id="P2" name="Strategically Researched">
    Research is aimed, not exhaustive for its own sake. Before searching, name what the primer needs to know that the corpus does not already say — usually: does this asset still exist, is this standard current, does this neighbouring primer already own this concern. Then go and find out. Record what was searched, what was found, and the retrieval date.
  </principle>

  <principle id="P3" name="Reliable Provenancing">
    Every statement in the primer traces to one of four sources, named inline: a corpus requirement ID (e.g. FS-3), a section of an existing 02_ primer (e.g. Primer D §D2), an ELSM entry, or an external source with URL and retrieval date. A statement with no trace is removed or marked {{UNSOURCED — operator to confirm}}.
  </principle>

  <principle id="P4" name="Construct Validity">
    Three axes, checked separately.
    Internal — the primer is self-consistent: scope-in matches the requirement IDs it claims; scope-out names who owns each exclusion; the definition of done is satisfiable by the execution layer described.
    Ecosystem-wide — the primer contradicts nothing in MAK-FFC, nothing in the 02_ primer set it touches, and nothing in REG-POSTURE v1.0. Where a corpus volume and a 02_ primer appear to conflict, the host law governs and the conflict is reported, never silently resolved.
    External — every technology, standard, repository and regulatory position the primer relies on is verified against the outside world, with currency checked. Named standards are confirmed to exist and to be the version cited.
  </principle>

  <principle id="P5" name="Exhaustive Library of Execution Layer Assets">
    Sections X8 and X9 map every requirement ID in the primer's scope to at least one concrete asset — a repository, library, standard, dataset, service, or an explicit "no existing asset; build" entry. Seed from the corpus volume's own execution sourcing annex and MAK-ELSM; verify each asset is live (last release date, licence, maintenance signal); mark dead or archived assets as such and propose a replacement or a build. An asset library with unverified entries is not exhaustive, it is long.
  </principle>

  <principle id="P6" name="Reliable Deliverable on Execution">
    Every primer ships complete on the first pass: all eleven sections present, the ID census reconciled to the corpus, the self-audit checks run and passing, the file written to {{OUTPUT_DIR}} under the agreed name, and a one-line changelog entry. A primer that stops at "draft — to be completed" has not been delivered.
  </principle>
</principles>

<instructions>

<step n="0" name="Orient">
Read briefing-primers, briefing-corpus and manifest in full. Read exemplar-A end to end and note the exact section skeleton: X1 What this is · X2 Scope · X3 Breadth and depth · X4 Building in a silo · X5 Folding it in · X6 Definition of done · X7 Internal operations diagram · X8 Execution layer · Production topology annotation · Register topology annotation · X9 Build Execution Extension · X10 Metamorphosis & Hardening Annex. Note the shared epigraph block quote and the per-primer "This primer's position:" sentence inside it. This skeleton is the contract. You do not vary it.
</step>

<step n="1" name="Derive the shared epigraph">
The 02_ primers open with one governing sentence — "ML proposes and tests; only arithmetic releases" — followed by the three spine attachments and the two lattices. The butterfly needs its own equivalent, derived from MAK-FFC's Thesis and Part 2 (the shared spine) and MAK-MIF's eight beats.

Draft it once. It must: state the butterfly's governing doctrine in one sentence; name the host (MAK-FFC) and the governing regulatory posture (REG-POSTURE via MAK-ANT); and leave a slot for the per-primer position clause.

<clarification_gate id="CG-1">
Present the drafted epigraph to the operator with a one-line rationale trace to the MAK-FFC and MAK-MIF passages it derives from. Ask for confirmation or edits before writing any primer, because this text is replicated verbatim across every primer in the set and a later change means touching all of them. Offer the draft as the default so "confirmed" is a complete answer.
</clarification_gate>
</step>

<step n="2" name="Map corpus volumes to primers">
The mapping is not one-to-one. A primer specifies a buildable component; a corpus volume specifies a law. Some volumes are informative (MAK-ELSM, MAK-MIF, MAK-DOT), one is folded into another (MAK-J3 into MAK-FFC Annex 1), and the host itself (MAK-FFC) may map better to an architecture document than to a component primer.

Produce a mapping table with one row per manifest entry: doc_id → proposed primer (name, or "no primer — reason", or "folds into primer X §Y") → the requirement prefixes that primer will own → the 02_ primers it borders. Work from the corpus briefing's anatomy bands (host, wings, engine plane, faces, mouthparts, legs, antennae, doctrine).

Default proposals, for the operator to accept or amend:
- MAK-LWC → a Fuzzy Spine primer (owns FS/FC/FP/FA/FE/FX)
- MAK-RWC → a Meta-Rationality primer (owns MS/MC/MP/MA/ME/MX)
- MAK-CEC → an Engines primer (owns OM/CP/DX/QU/AD/RG)
- MAK-HDC / MAK-TXC / MAK-ABC → three Face primers
- MAK-PRB / MAK-LBP → two UI primers
- MAK-LEG → a Stack primer (bindings as the definition of done; defaults as X8 assets)
- MAK-ANT → a Regulatory Sensing primer (AN duties; REG-POSTURE cited, not reproduced)
- MAK-FFC → no component primer; feeds the epigraph and the ecosystem-wide validity checks of every other primer
- MAK-ELSM, MAK-MIF, MAK-DOT → no primer; reference sources for X8/X9 and for the epigraph
- MAK-J3 → no separate primer; its GPP requirements land in whichever primer owns EN-3 / the guideline-compiler path, marked provisional at v0.9

<clarification_gate id="CG-2">
Present the mapping table and ask the operator to confirm, amend, or strike rows. Also ask: (a) the naming scheme for the new primers — default is `primer_<MAK-doc_id>_<slug>.md`, e.g. `primer_LWC_fuzzy_spine.md`, chosen so the file name preserves traceability to its source volume and cannot be confused with the 02_ lettered set; (b) the output directory — default {{OUTPUT_DIR}}; (c) whether a Primer 0-equivalent for the butterfly is wanted at the end of the run — default yes, written last, charter-exempt like its 02_ counterpart. Offer all three defaults so "defaults" is a complete answer.
</clarification_gate>
</step>

<step n="3" name="Write the primers, one at a time, in manifest reading order">
Follow the manifest's reading order for prompt work, skipping rows mapped to "no primer". For each volume:

  <substep n="3a" name="Load and extract">
  Load the corpus volume. Extract, into a working table: every requirement ID with its RFC-2119 level and one-line statement; the volume's subordinate_to, builds_from, absorbs, folds_in and governed_by; the Part that carries its execution sourcing annex, if any. This table is the spine of P1 and P3 — every primer sentence will point back into it.
  </substep>

  <substep n="3b" name="Draft the eleven sections">
  Write in exemplar-A's skeleton. Section by section:

  X1 What this is — one paragraph, the component's identity and its defining property, phrased in the corpus's own terms. The defining property is usually the volume's Thesis restated as a property the built thing has.

  X2 Scope — in-scope as the requirement prefixes this primer owns, each with a one-line gloss. Out-of-scope as a list where every excluded concern names the primer that owns it — a 02_ primer or another butterfly primer from the CG-2 map. This is where P4 (ecosystem-wide) is built in, not bolted on.

  X3 Breadth and depth — how much content is required for the component to be real. Derive from the corpus's requirement count, its Part 1 foundations, and any explicit coverage statements.

  X4 Building in a silo — what can be built with no dependency on any other primer's output. Be concrete: name the inputs that can be mocked and the interfaces that can be stubbed.

  X5 Folding it in — the integration contract: what this component consumes (from which primer, by which interface), what it emits (to which primer). Every edge here must have a matching edge in the neighbouring primer's X5 or X2 — check the 02_ primers you border and record the check.

  X6 Definition of done — release-gating criteria per release, derived from the corpus MUSTs that are testable and from the volume's own self-audit checks. Where MAK-LEG-style bindings apply, the bindings are the definition of done and the defaults are not.

  X7 Internal operations diagram — a Mermaid flowchart of the component's own mechanics, in the style of exemplar-A §A7. Nodes are named in the corpus's vocabulary.

  X8 Execution layer — this is where P5 lives. Seed from the volume's execution sourcing annex and MAK-ELSM. For every requirement ID in scope, at least one asset row: asset name · type (repo / library / standard / dataset / service / build) · what it satisfies (requirement IDs) · licence · last release or currency date · verification method and date · verdict (adopt / adapt / build / dead-replace). Verify each externally (P2, P4-external). Do not carry forward an ELSM verdict without re-checking it — sourcing rots.

  Production topology annotation — where the component runs, per architecture §topology. Register topology annotation — which of the 28 registers it writes to, per architecture §12.

  X9 Build Execution Extension — version-scoped build detail in the form the 02_ primers use at their §-9.

  X10 Metamorphosis & Hardening Annex — for a first-version primer this is the additive-revision commitment and the fabric-binding statement, following exemplar-A §A10's form. Do not invent hardening content that has no corpus source.
  </substep>

  <substep n="3c" name="Run the three validity checks">
  Internal (P4-i): every requirement ID in the working table appears in exactly one of X2/X6/X8; scope-out names an owner for every exclusion; X6 is satisfiable by X8.
  Ecosystem-wide (P4-e): no sentence contradicts MAK-FFC; every X5 edge has a counterpart in the bordering primer; regulatory statements cite REG-POSTURE IDs and do not restate them. Where a conflict is found between this volume and a 02_ primer, write it up as a finding in the primer's X10 with both citations — host law governs, and the operator decides.
  External (P4-x): every standard, repository and regulatory position in X8 carries a verification date within this run. Named standards confirmed to exist at the cited version; where a revision is in progress, say so.
  </substep>

  <substep n="3d" name="Reconcile and self-audit">
  Append the ID census: declared requirement count from the corpus frontmatter vs. IDs actually mapped in this primer; any gap named. Append the self-audit checks in the corpus's own style (numbered, each a yes/no the reader can verify), and record the result of running them. Add an Assumptions & confidence block: what you assumed where the corpus was silent, and how confident you are in each X8 verdict.
  </substep>

  <substep n="3e" name="Deliver">
  Write the file to {{OUTPUT_DIR}} under the CG-2 name. Add one changelog line. Report to the operator in five lines: file written; requirement IDs mapped / declared; assets verified / total; validity findings (count, with the most consequential named); open questions. Then proceed to the next volume without waiting, unless a finding in 3c requires an operator ruling — in which case ask once, with a proposed default, and continue with the next volume while waiting.
  </substep>
</step>

<step n="4" name="Close the set">
If CG-2 confirmed a Primer 0-equivalent: write it last, from the delivered primers, in exemplar-0's form — cast list, one worked flow end to end, glossary of house vocabulary, reading paths by role, one Mermaid picture. Charter-exempt: no build blocks, no obligations.

Then produce the run report: the mapping table as executed; a cross-primer edge check (every X5 emit has a matching consume); the consolidated findings list from all 3c passes; the consolidated open-questions list; and the asset library totals (verified / adapt / build / dead-replace).
</step>

</instructions>

<clarification_protocol>
Ask only at the named gates (CG-1, CG-2) and when a 3c finding needs a ruling. Batch questions. Every question carries a proposed default so a one-word answer is complete. Anything else that is unknown becomes a {{PLACEHOLDER}} in the primer and a line in that primer's open-questions list — do not stall a volume on a question you can answer with a placeholder.
</clarification_protocol>

<examples>

<example name="epigraph-with-position-clause" from="exemplar-A">
> **Architecture spine.** The project's spine is the deterministic-release doctrine plus the signed content registry: *ML proposes and tests; only arithmetic releases.* Three spine attachments raise the spec: … This primer's position: the principal probabilistic proposer. …

Your butterfly epigraph follows this shape exactly: doctrine sentence in italics · the governing structures named · "This primer's position:" · one sentence.
</example>

<example name="scope-out-naming-the-owner" from="exemplar-D">
**Out of scope:** deciding *which* fragment is relevant (Graph RAG/engine selection); authoring clinical content de novo (fragments derive from licensed authoritative sources under their terms); diagnosis-side evidence (library territory).

Every exclusion names its owner in parentheses. Reproduce this. An exclusion with no owner is a seam nobody has claimed.
</example>

<example name="requirement-to-section-mapping">
| Req ID | Level | Lands in | Trace |
|---|---|---|---|
| FS-1 | MUST | X2 in-scope; X6 (FML serialisation is a release gate) | MAK-LWC Part 2 |
| FS-3 | MUST | X6 (validator rejects mixed types) | MAK-LWC Part 2; A1 |
| FS-5 | MUST | X5 (decoder → codebook interface) | MAK-LWC Part 2 |
</example>

<example name="x8-asset-row">
| Asset | Type | Satisfies | Licence | Currency | Verified | Verdict |
|---|---|---|---|---|---|---|
| IEEE 1855-2016 (FML) | standard | FS-1 | IEEE | 2016; revision under discussion (StandICT) | ieeexplore.ieee.org/document/7479441 · 2026-09-02 | adopt; monitor revision |
| JFML | library (Java) | FS-1 serialisation | GPL (verify) | {{last release — verify}} | uco.es/JFML · 2026-09-02 | adapt or build Python equivalent |
</example>

<example name="clarification-question-with-default">
CG-2 (b) — Output directory. Default: `ECOSYSTEM/makoha-imago-v1.2/04_butterfly-primers/`. Rationale: keeps the new set out of 02_ so the lettered primers stay a closed set, and out of 03_ so source and derivative aren't interleaved. Reply "default" to accept.
</example>

<example name="validity-finding">
**P4-e finding, MAK-HDC → Primer D.** MAK-HDC HR-4 requires the Clinician Face to render a fragment's *verification tier* as a graded chip. Primer D §D2 places tier as an input to the gate chain, not a rendered field. Not a contradiction — D governs *release*, HDC governs *display of what was released* — but the X5 edge must carry tier from D's serving API to HDC's renderer, and D's §D8 does not currently list tier in the response schema. Recorded in Head primer X10; operator to confirm whether Primer D's schema is extended or HDC narrows.
</example>

</examples>

<output_format>
Per primer: the complete markdown file in exemplar-A's skeleton, written to disk, followed by the five-line delivery report in chat.
At set close: the run report as a single markdown document written to {{OUTPUT_DIR}}/RUN-REPORT.md.
Every file carries YAML frontmatter in the corpus style: doc_id (new namespace, e.g. PRM-LWC), title, version 1.0, date, series, status, derived_from (the corpus doc_id and version), companions, change_policy.
</output_format>
```

---

## Evidence pack

Facts this prompt depends on, with source and verification.

| Claim | Source | Verified | Grade |
| --- | --- | --- | --- |
| The 02_ primers share an eleven-section skeleton (X1–X10 plus two topology annotations) and an identical opening epigraph with a per-primer position clause | Direct read of `primer_A`, `_B`, `_C`, `_D`, `_E`, `_F` headings and openers; `primers_briefing.md` | 2026-09-02, device read | Primary document |
| Primer 0 is charter-exempt from build-execution blocks | `primer_0_ecosystem_explainer.md` MET-1 annex comment: "Primer 0 is charter-exempt from build-execution blocks (Arch §13.9)" | 2026-09-02 | Primary document |
| Corpus volumes use RFC 2119, stable IDs, requirement blocks with inline rationale trace, ID census and self-audit appendices | Direct read of `four-faces`, `left-wing`, `head`, `antennae`, `legs` frontmatter and headings; FS-1..6 block sample | 2026-09-02 | Primary document |
| MAK-FFC is the host; no subordinate volume relaxes a corpus MUST; consolidation volumes never retire source requirements | `MANIFEST.md` "Precedence in one paragraph"; `subordinate_to` fields | 2026-09-02 | Primary document |
| Mapping is not 1:1 — 15 corpus files, 16 artifacts; MAK-J3 has no artifact (folded); two dossiers have no corpus | `MANIFEST.md` table; directory listing | 2026-09-02 | Primary document |
| Corpus volumes carry their own execution sourcing annex (LWC Part 9, HDC Part 8) and MAK-ELSM is the sourcing record | Headings read; LWC changelog v1.1 | 2026-09-02 | Primary document |
| The architecture has 28 registers ("if it is not in a register, it did not happen") | `primer_0` §5 and glossary | 2026-09-02 | Primary document |
| IEEE 1855-2016 Fuzzy Markup Language exists as cited in FS-1; a revision is under discussion | [IEEE Xplore 7479441](https://ieeexplore.ieee.org/document/7479441/); [Wikipedia IEEE 1855](https://en.wikipedia.org/wiki/IEEE_1855); [StandICT revision discussion](https://standict.eu/discussion-groups/artificial-intelligence/267/revision-ieee-1855-standard-fuzzy-markup-language); [JFML](http://www.uco.es/JFML/) | 2026-09-02, web | Standards body + secondary |

**Gap noted:** MAK-RWC, MAK-CEC, MAK-TXC, MAK-ABC, MAK-PRB, MAK-LBP were characterised from the manifest and briefing, not read in full. The prompt instructs the executing model to load each in full at 3a; nothing in the prompt depends on their internal content beyond what the manifest declares.

---

## Open questions

Placeholders left in the prompt, for the operator:

1. `{{OUTPUT_DIR}}` — where do the new primers land? Proposed default: `04_butterfly-primers/`.
2. Naming scheme — proposed default `primer_<MAK-doc_id>_<slug>.md`. Alternative: continue the letter sequence M onward. The default was chosen because letters would imply the butterfly primers are peers in the same closed set as 0/A–L, and the doc_id form preserves traceability to source.
3. Primer 0-equivalent for the butterfly — wanted? Default yes.
4. New primer doc_id namespace — proposed `PRM-<MAK-suffix>` (e.g. PRM-LWC). Confirm or supply.
5. MAK-J3 at v0.9-proposed — treat its GPP requirements as provisional in whichever primer absorbs them, or hold them out until J3 ratifies? Default: include, marked provisional.

---

## Eval pack

| # | Case | Input | Pass criterion |
| --- | --- | --- | --- |
| 1 | Happy path | MAK-LWC v1.1 | Primer has all 11 sections in exemplar-A order; ID census shows 43/43 FS–FX mapped; every X8 row has a verification date; file written |
| 2 | Informative volume | MAK-ELSM | At CG-2 the model proposes "no primer — reference source for X8/X9" rather than fabricating a component |
| 3 | Folded volume | MAK-J3 v0.9 | GPP requirements land in the primer owning the guideline-compiler path, each marked provisional; not a standalone primer unless operator overrides |
| 4 | Epigraph gate | Start of run | Model drafts the epigraph with rationale trace to MAK-FFC/MAK-MIF and stops at CG-1 before writing any primer |
| 5 | Ecosystem conflict | A corpus MUST that appears to contradict a 02_ primer section | Reported as a P4-e finding in X10 with both citations; host law stated as governing; not silently harmonised; run continues |
| 6 | Dead asset | An ELSM or annex repo that is archived or has no release in 18+ months | X8 verdict is `dead-replace` or `build`, with the check date; verdict not carried forward from ELSM unexamined |
| 7 | Sequencing | Model reaches MAK-HDC | MAK-CEC primer already delivered (manifest order: engine plane before faces) |
| 8 | Census mismatch | Primer maps 41 of 43 declared IDs | Self-audit check fails and names the two missing IDs; delivery report shows 41/43, not "complete" |
| 9 | Evidence doesn't support | A named standard in X8 cannot be located externally | Row marked `{{UNVERIFIED}}` with search record; not asserted as adopt |
| 10 | No stall | Operator does not answer a 3c ruling request | Model proceeds to the next volume, ruling logged in open questions |

**Rubric:** each case is pass/fail on the stated criterion. Cases 1, 5, 6 and 8 are the load-bearing four — a run that fails any of them has not met P1, P4 or P5 regardless of the rest.

**Expected failure mode:** the model writes fluent X3/X4 prose that reads well but isn't traceable — filling "breadth and depth" from general knowledge rather than from the corpus's requirement count and Part 1. Mitigation is already in the prompt (P3 removes or flags untraced statements); if evals show it, tighten 3b to require an inline trace per paragraph, not per section.

---

## Design notes

- **Two clarification gates, not a running dialogue.** The brief permits clarification; the skill's stance forbids stalling. Resolved by naming exactly two gates before writing starts (epigraph, mapping) plus a ruling protocol for genuine conflicts, with defaults on every question so a one-word answer is complete. Everything else is placeholder-and-continue.
- **The mapping gate is the substantive design decision.** "Each corpus → its corresponding primer" reads as 1:1; the source isn't. Three volumes are informative, one is folded, and the host is a constitution rather than a component. Forcing 15 primers would produce five hollow ones. The prompt front-loads a proposed map with a rationale per row so the operator decides once.
- **X8 verifies, it doesn't inherit.** MAK-ELSM is v1.1 dated before this run; sourcing verdicts rot. The prompt requires each asset re-checked with a date, and models the row format with a live example (IEEE 1855, revision in progress). This is where "Strategically Researched" and "Exhaustive Library" are the same instruction.
- **Filed-item note, once:** the brief says "and any associated artefact document if useful." The prompt demotes artifacts to disambiguation aids and bars them as a source of requirements, because the corpus frontmatter declares itself the source of truth and the artifact its presentation. If the operator wants artifacts elevated, strike the comment in `<documents>`.
- **First thing to change if evals fail:** if case 5 or 6 fails, the model is treating ELSM and the 02_ primers as authorities rather than inputs. Move the P4/P5 checks from 3c into 3b so they run during drafting rather than after.
