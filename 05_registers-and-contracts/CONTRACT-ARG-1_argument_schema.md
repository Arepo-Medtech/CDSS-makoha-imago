---
doc_id: CONTRACT-ARG-1
title: "ActualArgument / GenericArgument / linkage — spine contract"
status: "Proposed. Home on ratification: cdss-spine (contracts live here once, versioned; never duplicated — Arch §10). A change is a spine PR that visibly breaks consumers."
grounding: "Field set is MAK-FFC Part 2's canonical argument object, verbatim in intent; supplier mapping per MET-1 §5.1."
---
**GenericArgument** (knowledge-plane, versioned, ratified): `ga_id` · `ga_version` · `warrant_type` (guideline-rule | bayesian-likelihood | ratified-local) · `warrant_content` (CQL/ELM ref or LR-structure ref) · `backing_refs[]` (library row IDs w/ tier) · `release_thresholds` (crisp, ratified — FZ-3 discipline even pre-ratification) · `profile` (default | GPP — GPP builds accept warrant_type guideline-rule only, GPP-9) · `lineage` (jurisdiction/supersession for SPINE-6 pluralism).

**ActualArgument** (per encounter, append-only): `arg_id` · `claim` {type (whitelisted per profile), content, verbatim_fragment_refs[]} · `grounds[]` {coded_finding, provenance, capture_context} · `warrant` {ga_id, ga_version, applicability} · `backing[]` (resolved rows: tier/source/currency) · `qualifier` {posterior_set, conformal_set, coverage_stated} — **required (SPINE-2)** · `rebuttals[]` {source: corruption|contraindication-prune|DetectedIssue|unresolved-conflict, content} — **required non-empty when findings exist (SPINE-2)** · `evaluation` {gate_results[5], override_state, contract_assertions, evaluator_version} · `pins` {lockfile pin-set = version_stamp} (SPINE-5) · `render_projections[]` {face, register} (SPINE-3 — projections derived, disposable, rebuildable: SPINE-9).

**Deviation** (CONTRACT-DEV-1, same file family): `dev_id` · `arg_id` · `reason_taxonomy_code` · `free_text` · `severity_tier` · `author_identity` · `timestamp` — never blocked except deterministic safety classes (SPINE-8).

**Render-invariance contract (CONTRACT-RRI-1):** for any argument A and faces f1,f2: content-set(render(A,f1)) ≡ content-set(render(A,f2)) up to compression/ordering; add/remove/reweight ⇒ test failure (SPINE-3); applies to LLM narration identically (L10).
