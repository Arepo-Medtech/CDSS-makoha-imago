---
doc_id: WAYS-OF-WORKING
title: "Mākoha — Ways of Working"
date: "2026-09-10"
status: "Proposed. Drafted by Claude agent (MAK-5); pending Ken Lee's review and edit in Confluence before the task is closed."
produced_by: "claude/MAK-5/ways-of-working-page — MAK-5"
sources:
  - "CDSS_AI_AGENT_CUSTOM_INSTRUCTIONS.md (Codex output, 3 Sep 2026)"
  - "CDSS_AI_SDLC_KNOWLEDGE_CORPUS.md (Codex output, 3 Sep 2026)"
  - "REG-POSTURE v1.2 §6.6 — ecosystem boundary"
  - "MAK-ANT AN-5 — mapping-by-reference doctrine"
  - "CDSS_Makoha README.md — rules of the road"
  - "CDSS_Makoha .github/pull_request_template.md — tier field"
  - "CDSS_Makoha .github/CODEOWNERS — gate rule for tier A3+"
---

# Mākoha — Ways of Working

> **Rule.** This page explains; it is not a design output.
> Nothing stated here constitutes a controlled document, a design control, a regulatory
> commitment, or a requirement. Controlled content lives in Imago (design record),
> Jira MAK (work record) and Ketryx (design controls). This page points at those
> sources; it never replaces them.
> **Ken: please review and edit this page directly in Confluence, then close MAK-5.**

---

## 1. The five systems and what each one owns

| System | What it owns | What it does NOT own |
|---|---|---|
| **Imago** ([CDSS-makoha-imago](https://github.com/Arepo-Medtech/CDSS-makoha-imago)) | Design record: architecture, regulatory posture, research corpus, hardening plan, register schemas. Cite by stable ID at a commit; never copy or restate. | Work items, code, approvals, narratives. |
| **Jira MAK** (arepo-tech.atlassian.net) | Controlled work record: every task, bug, change item and decision trail that moves through the programme. The task is the unit of controlled work. | Design artefacts, code, approvals, explanations. |
| **Ketryx** | Design controls, risk file, traceability V-model, human release approvals. Only a named human can apply a Ketryx signature; the AI has no approve/sign capability. | Work scheduling, code, design record, narrative. |
| **GitHub** ([CDSS_Makoha](https://github.com/Arepo-Medtech/CDSS_Makoha)) | Engineering record: code, tests, build definitions, CI evidence, agent sessions. Every branch and PR carries a MAK key linking it to Jira and Ketryx. | Controlled work items, design artefacts, approvals. |
| **Confluence** (Makoha space) | Narrative for humans: intended purpose, corpus map, decision index, architecture overview, this page. Explains the work; is never a design output. | Anything that creates a regulatory obligation. |

---

## 2. Authority order

When sources conflict, apply this order — highest authority first:

1. **MAK-FFC v1.1** (Mākoha Four Faces Corpus) — host law; governs the fabric architecture.
2. **REG-POSTURE v1.2** (ADVISORY\_ONLY) — canonical regulatory posture; counsel attestation required before any commitment.
3. **Imago corpus** (`00_MANIFEST.md` precedence; AGENTS.md laws 1–7) — the append-only design record.
4. **Jira MAK** — the controlled work record; the task is the controlled unit.
5. **Ketryx** — design controls; operates under the external QMS (REG-POSTURE §6.6).
6. **GitHub** — engineering record; provides the evidence artefacts Ketryx consumes.
7. **Confluence** — explanation only; lower precedence than all of the above.

*Source: REG-POSTURE v1.2 §6.6 ecosystem boundary; AGENTS.md law 2; OPS-1 §3–4.*

---

## 3. Source labels

Every artefact in the ecosystem carries an implicit label. Use these labels to read a document correctly:

| Label | What it means | Examples |
|---|---|---|
| **canonical** | The authoritative source; other systems cite it, never copy it. | Imago design corpus files (`00_`–`11_`), REG-POSTURE v1.2, MAK-FFC volumes. |
| **controlled** | Lives in a system with a regulated change trail; changes require a human decision record. | Jira MAK work items, Ketryx design controls and risk rows, signed release artefacts. |
| **derived** | Created from a canonical or controlled source; must stay in sync by reference (AN-5 mapping-by-reference doctrine — IDs are cited, content is never copied). | CDSS_Makoha code, CI evidence artefacts, Ketryx traceability rows derived from Jira items. |
| **transient** | Useful now; not a design record; may be edited or deleted without a change trail. | Agent draft outputs, Confluence pages, PR descriptions, session logs, Nimbalyst previews. |

> **Cardinal rule.** Nothing on a Confluence page is a design output.
> A Confluence page is **transient**: it explains a decision, it does not make one.
> If you find yourself writing something in Confluence that should be binding — stop,
> open a Jira task, and let it land in Imago or Ketryx instead.

---

## 4. Agent risk tiers (A0–A5)

Every agent contribution to CDSS\_Makoha carries a tier declared in the PR template.
The tier determines which human gate must be passed before the PR may be merged.

| Tier | Scope | Human gate | Gate owner |
|---|---|---|---|
| **A0** | Non-clinical tooling only — documentation, CI scaffolding, repository structure, test fixtures with no clinical logic. No path to a clinical output. | Owner review of PR description. | Kenny-bytes (Architecture owner) |
| **A1** | Non-clinical engineering — build infrastructure, data-pipeline plumbing, synthetic-only test datasets. Indirect relationship to clinical outputs. | Owner review + passing CI. | Kenny-bytes |
| **A2** | Deterministic clinical logic — arithmetic, rule engines, register schemas, conformal wrappers. No learned parameters; output is reproducible and inspectable. Aligns with J-1 posture. | Named engineering reviewer approval in GitHub. | Kenny-bytes (Architecture owner) |
| **A3** | ML-contributing — components that propose or influence a clinical output (e.g. Bayesian engine updates, model configuration changes, LLM prompt changes that reach clinical inference). | Named clinical or safety reviewer approval in addition to engineering. Every path in the repository requires at least this gate (CODEOWNERS rule). | kendo-Jones (Regulatory owner) |
| **A4** | Patient-facing outputs — any component whose output can reach a patient surface or influence a clinician decision rendered to a patient. Blocked on GATE-002 (no identifiable patient data before this gate). | Named clinical reviewer **and** named safety reviewer approval; evidence artefact recorded. | kendo-Jones + Ken-E-Gee (Security/Safety owner) |
| **A5** | Regulated release gate — a version entering the Ketryx controlled release pipeline. Only arithmetic releases (doctrine: "ML proposes and tests; only arithmetic releases"). Requires Ketryx human e-signature; AI has no approve/sign capability. | Ketryx human release signature; IEC 62304 evidence bundle; GATE-003 passed. | kendo-Jones (Regulatory owner), with Architecture owner sign-off |

> Agents open draft PRs only. A named human reviews and merges. `main` is protected.
> If the tier is uncertain, declare the higher tier and flag it for human resolution.

---

## 5. The working loop

One complete unit of work follows this path:

```
Jira MAK space
  └─ Open a Task (MAK-nnn)
       │
       ▼
  Agent drafts in a branch (CDSS_Makoha or Imago)
  ├─ Branch name includes the MAK key: claude/MAK-nnn/short-slug
  ├─ PR opened as draft; tier declared; MAK key in title
  └─ For Confluence narrative: agent commits PAGENAME.md to Imago
       │
       ▼
  GitHub → Confluence connector (confluence-mirror.yml)
  └─ Creates / updates one Confluence page per committed .md file
       │
       ▼
  Human reviews in Confluence (for narrative) or GitHub (for code)
  ├─ Edit in place in Confluence — the page is transient; edit freely
  ├─ Comment or request changes in GitHub PR for code changes
  └─ Merge PR once gate requirements are satisfied for the tier
       │
       ▼
  Close the Jira Task (MAK-nnn)
  └─ Evidence artefact named (DONE-WITH-EVIDENCE, REG-POSTURE §0.4)
```

**Short form:** open a Task → agent drafts → connector mirrors → review in Confluence, edit in place → close the Task.

---

## 6. What this page is — and is not

| This page IS | This page is NOT |
|---|---|
| An orientation guide for anyone joining the programme. | A design document or controlled record. |
| A pointer to the five systems and their authority order. | A requirement, obligation, or regulatory commitment. |
| A quick reference for the tier table and working loop. | Authoritative on the tier definitions — those live in `CDSS_AI_AGENT_CUSTOM_INSTRUCTIONS.md`. |
| Editable directly in Confluence by Ken Lee (or any team member). | Subject to the Imago append-only law — this page is transient. |

---

*Sources: `CDSS_AI_AGENT_CUSTOM_INSTRUCTIONS.md` and `CDSS_AI_SDLC_KNOWLEDGE_CORPUS.md` (Codex outputs, 3 Sep 2026); `REG-POSTURE v1.2 §6.6` ecosystem boundary ([Imago `73460b3`](https://github.com/Arepo-Medtech/CDSS-makoha-imago/blob/73460b3/10_regulatory-execution/REG-POSTURE_v1.2.md#66-ecosystem-boundary)); MAK-ANT AN-5 mapping-by-reference doctrine; `CDSS_Makoha` [README](https://github.com/Arepo-Medtech/CDSS_Makoha/blob/main/README.md), [PR template](https://github.com/Arepo-Medtech/CDSS_Makoha/blob/main/.github/pull_request_template.md), [CODEOWNERS](https://github.com/Arepo-Medtech/CDSS_Makoha/blob/main/.github/CODEOWNERS).*

*Agent contribution: drafted by Claude (Fable 5.1); human owner Ken Lee.*
