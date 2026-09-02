---
doc_id: RESEARCH-1
title: "Research report — supplied vs newly-found vs proposed sources"
version: "1.0"
date: "2026-09-01"
---
# 1. Supplied sources (in the uploaded material; not re-verified this pass unless noted)
The entire evidence base of the two stacks: the CDSS primers' clinical/regulatory citations; MAK-ELSM's 23 individually-verified repo rows (verification dates recorded per row in the volume, e.g. 30 Aug 2026 for the fuzzy repos); MAK-DOT's literature base; REG-POSTURE's SRC-REG-001..004 (TGA guidance incl. the 7 Oct 2025 exemption rewrite; standards matrix); MAK-MIF's CWW/Z-number/neuro-symbolic bibliographies. These remain authoritative in their owning volumes; this pass cites, never restates.

# 2. Newly-found / newly-verified this pass (fetches on 1 Sep 2026)
| Source | Finding | Feeds |
|---|---|---|
| github.com/Arepo-Medtech/Makoha (README depth) | "HeyDoc — AI Doctor Grounding Infrastructure", build 2026-06-23; 5-step grounding pipeline; two-store case architecture (00–02 / 10–13); pharm firewall (doses only in pharm-check); T0–T5 tiers with 3× under-triage weighting; 9 trunks; first clinician-reviewed case SPEC-CARD-04-00001; Amplify present; 747 commits; below-README contents uninventoried | MET-1 §4.1 dispositions; C10 seed intake; G-08/DEC-12 |
| demo.makoha.ai (surface) | session-gated "Working DEMO Surfaces"; educational-tool disclaimer; "conversations are processed via third-party AI providers" | C-10 positioning escalation |
| github.com/addyosmani/agent-skills (README, releases, docs, CLAUDE.md/AGENTS.md) | live and active; "25 skills total — 24 lifecycle + using-agent-skills meta"; release 0.6.4 ships an in-repo three-tier skill eval framework + Codex support + supply-chain hardening; per-skill install gap confirmed and tracked at issue #361; personas-don't-invoke-personas rule confirmed in AGENTS.md | Row zero; C-11/C-12; DEC-11; HARDEN-1 row 0 |

# 3. Research gaps (open; no findings fabricated)
| Gap | What's needed | Who |
|---|---|---|
| RG-01 | HeyDoc below-README clone inventory (schemas, trunk prompts, MCP servers — salvage assessment) | DEC-12 executor |
| RG-02 | Counsel reading of the two MAK-J3 ⚑ flags (verbatim dose tables; values elicitation-display) | AU counsel |
| RG-03 | Baseten Sydney dedicated terms in writing (ASSUME-REG-004) | Baseten |
| RG-04 | immudb BUSL redistribution terms if C-05 ruling prefers it over the Aurora pattern | Legal |
| RG-05 | Conformal-for-LLM literature watch before any L-capability qualifier claim (MAK-ELSM §05: "track it; do not ship ahead of it") | cdss-conformal owner |
| RG-06 | WATCH-REG-002: TGA AI-enabled-SaMD guidance (applies from 5 Feb 2026) read against the intended-purpose statement once TASK-REG-001 exists | Regulatory owner |

# 4. Proposed sources (named in supplied material as future engagements — not yet consulted)
Stranieri (GAAM formalization collaboration — MAK-ELSM's highest-leverage de-risk); NSW Health / Lumos custodian (or Danish Health Data Authority per H10 contingency); Ketryx (tier/validation package); pilot practices (MoUs, ASSUME-SPINE-001).
