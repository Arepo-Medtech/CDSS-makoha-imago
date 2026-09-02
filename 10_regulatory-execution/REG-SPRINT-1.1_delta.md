---
doc_id: REG-SPRINT-1.1
title: "Mākoha — Sprint Plan Delta (v1.0 → v1.1)"
version: 1.1-delta
status: DRAFT
authority: ADVISORY_ONLY
date_issued: 2026-09-01
applies_to: REG-SPRINT v1.0 (makoha_sprint_plan_v1_v2_v3.md)
change_policy: "Additive delta per the MET-1.1 pattern. v1.0 text stands except where a delta row names it."
---

# Sprint Plan Delta v1.0 → v1.1

Five amendments from cold review. The first three are material.

---

## D-1 — V1 build decoupled from counsel: 12 weeks → ~9

**Error in v1.0:** `V1-S1` (build) was scheduled weeks 4–8, serialized behind
`SG-V1-0` (counsel attests non-device). But counsel gates **shipping**, not
**building**. Building the read model on synthetic pharmacy data creates no
regulatory exposure whatsoever.

**Amendment:** `V1-S1` starts week 1, parallel with `V1-S0`. Only `V1-S2`
(real site, real data) waits on `SG-V1-0`.

Revised V1 timeline:

| Sprint | Weeks | Gate |
|---|---|---|
| `V1-S0` classification | 1–4 | `SG-V1-0` |
| `V1-S1` build (synthetic) | 1–6 | `SG-V1-1` |
| `V1-S2` foothold | 5–9 | `SG-V1-2` |

Risk accepted: if counsel refuses non-device status at week 4, up to four weeks of
build is stranded. Bounded, and smaller than it looks — the components are the
abdomen face's existing specification (AL/AR/AX), which V2/V3 need regardless.
Revenue target moves from week 12 to week 9–10.

---

## D-2 — WAND notification split from first supply; new counsel question

**Gap in v1.0:** `V2-S3` bundled notification and first commercial supply into one
milestone. Under the adopted working assumption — the Medical Products Bill carries
transition provisions for already-notified devices — the grandfather position likely
attaches to **notification**, not to commercial traction. Those are separable events.

**Amendment:** `V2-S3` splits:

| ID | Milestone | Trigger |
|---|---|---|
| `V2-S3a` | WAND notification | The earliest lawful point after `SG-V2-2` (technical file complete, post-market system live) |
| `V2-S3b` | First commercial site | Commercial readiness, independently |

`V2-S3a` becomes the Bill-clock milestone; `V2-S3b` becomes the revenue milestone.
Under the working assumption, `V2-S3a` is the one racing the window — pull it as
early as the file permits, even if the first site is months behind it.

**New counsel question `NZ-Q-004`:** what is the earliest lawful point at which
Mākoha can be notified to WAND, what obligations attach to a notified-but-not-yet-
supplied device, and — the sharp version — is the transition likely to protect
*notified* or *supplied* devices? Goes into the single counsel engagement; it is the
question the entire working assumption hangs on, and v1.0 never actually asked it.

Discipline unchanged: `SG-V2-2` still gates `V2-S3a` absolutely. Notifying without a
producible file is the shortcut that converts the NZ position into an ARTG liability.

---

## D-3 — `SD-02` resolved provisionally: the domain is respiratory

**Hidden serial dependency in v1.0:** `SD-02` (V2 clinical domain) waits on V1's
guideline-gap analytics — but V1 produces real data at weeks 8–12, which is exactly
when `V2-S1` (domain build) is scheduled to start. As written, either V2 slips a
month-plus or the domain gets picked blind.

**Amendment:** name a provisional domain now, with a cheap reversal point. And the
corpus has already voted: the evaluation corpus, the casebundle pipeline and its
transformation tooling are built around **respiratory presentations** — it is the
domain where the differential library, the case bundles and the eval machinery are
furthest along. It also fits every `SD-02` criterion: high prevalence in the pharmacy
wedge, published instruments available for the reviewable-basis argument (CURB-65,
Centor, Wells), and red-flag/commission-trap structure already encoded in the case
work.

| Field | Value |
|---|---|
| `SD-02` status | **Provisionally resolved: respiratory presentations in community pharmacy scope** |
| Confirmation point | Month 4 — V1 gap analytics either confirm or contradict |
| Reversal cost at month 4 | Low: `V2-S1` is one month in, mostly library work that transfers partially |
| Reversal cost at month 7 | High — which is why the checkpoint is dated |

This converts a blocking decision into a dated checkpoint, and `V2-S1` starts on
schedule.

---

## D-4 — Corporate track rows (from the advisor's letter, missing from v1.0)

Two items with zero regulatory content and real calendar value, added as a parallel
corporate track — owner: founder + accountant/R&D specialist, not counsel:

| ID | Item | Timing |
|---|---|---|
| `V1-C1` | Confirm Arepo registration timing against the 10-year R&D incentive window running from inception; first question to the R&D specialist | Weeks 1–2 |
| `V1-C2` | ESIC qualification assessment scheduled **before** the wholesale round opens, per the advisor's sequencing | Before round |

Also one funding-contingent watch: Ketryx free-tier eligibility caps at $2M funding.
If the wholesale round closes during V2, tier upgrade becomes a round-budget line,
not a surprise — fold into `Q-REG-006`.

---

## D-5 — Register homes for the new ID families

v1.0 minted `SD-*`, `SG-*`, `V1/V2/V3-*` without naming where they live. Per house
law: `SD-*` rows enter the MET-2 decision table alongside DEC-*; `SG-*` gates and the
sprint tasks enter R30 with the same status vocabulary as REG-POSTURE §0.4; the
carrier-map re-run (AN-5) picks up both at the next MAK-ANT fold. `NZ-Q-004` joins
the REG-NZ question register.

---

## Net effect

| Metric | v1.0 | v1.1 |
|---|---|---|
| V1 revenue target | week 12 | week 9–10 |
| V2 grandfather milestone | month 12–14, coupled to commercial launch | earliest point after file completion, decoupled |
| `SD-02` | open, hidden serial dependency | provisionally resolved, dated checkpoint month 4 |
| Counsel questions in the single engagement | 4 | 5 (`NZ-Q-004` added) |

The plan's structure, gates and discipline are unchanged. The deltas remove two
self-inflicted delays and ask the one question the working assumption depends on.
