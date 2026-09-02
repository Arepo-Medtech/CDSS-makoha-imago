---
doc_id: REG-R30.2
title: "R30.2 — Regulatory Posture Register seed delta (jurisdiction set: AU v1.2, NZ v1.1, US v1.0, EU v1.0)"
version: 1.0
date: "2026-09-02"
status: "Added. Additive seed rows over REG-R30 schema+seed and R30.1; neither earlier file is edited. Same row fields; same write law (external attestations only for ASSUME closures)."
---

# R30.2 — Seed delta

**Scope extension:** R30's `reg_id` enum extends additively with the two new jurisdiction
namespaces — `US-FIND-*`, `US-OBL-*`, `US-STD-*`, `US-REG-*`, `US-ASSUME-*`, `US-TASK-*`,
`US-GATE-*`, `US-WATCH-*`, `US-Q-*`, `US-SRC-*` and `EU-FIND-*`, `EU-OBL-*`, `EU-STD-*`,
`EU-LAW-*`, `EU-ASSUME-*`, `EU-TASK-*`, `EU-GATE-*`, `EU-WATCH-*`, `EU-Q-*`, `EU-SRC-*` —
plus `NZ-STD-*` and `NZ-GATE-*` (the latter formalises v1.0's prose gates), and `STD-*`
for Australia (present in REG-POSTURE since v1.0; never in the R30 enum — formalised here).

A new optional row field is added: `jurisdiction` ∈ {AU, NZ, US, EU}. Rows seeded before
this delta are AU unless their prefix is `NZ-`.

**New rows (verbatim statuses at source, 2026-09-02):**

- **AU (REG-POSTURE v1.2):** REG-FIND-012..013 OPEN (013 medium confidence — accessory
  question) · ASSUME-REG-009 OPEN (AU counsel; blocks MAK-GOV GATE-G0 / SG-V1-0, **not**
  GATE-000) · OBL-015 standing · STD-001..013 editions pinned (no status change) ·
  STD-014..026 standing, each tagged [recommendation] with confidence · TASK-REG-023..024
  not started · KTX-013..014 OPEN (vendor-stated, written confirmation pending) ·
  WATCH-REG-008 annually + at GATE-004 · Q-REG-010..011 open · SRC-REG-015..020 recorded
  (017 vendor correspondence; 019 author's analysis). **Closes survey-2 BSQ-0001:**
  REG-FIND-013 and TASK-REG-023 now defined; ASSUME-REG-009 and Q-REG-010 (seeded in
  R30.1 without a document home) now homed.
- **NZ (REG-NZ v1.1):** NZ-FIND-010..012 OPEN · NZ-OBL-011..013 standing · NZ-STD-001..026
  standing (014..026 [recommendation]) · NZ-GATE-000..002 not passed (rename of prose
  NZ-GATE-0/1/2; the v1.0 seed row names are aliases) · NZ-TASK-009..010 not started ·
  NZ-WATCH-004 semi-annually, 005 annually · NZ-Q-005..006 open · NZ-SRC-006..013 recorded.
  **Homed:** NZ-Q-004 (from REG-SPRINT-1.1 D-2) and NZ-ASSUME-005 (from EXEC-1 EX-7) —
  both were register rows without a document definition until this version.
- **US (REG-US v1.0):** US-FIND-001..016 OPEN (003 medium — Jan 2026 CDS revision unread;
  011 partly draft guidance) · US-OBL-001..014 standing · US-STD-001..027 standing
  (recognition status to confirm against the FDA database, US-WATCH-004) · US-REG-001..017
  recorded (003, 009, 011, 013, 015, 016 flagged [currency: verify]) · US-ASSUME-001..006
  OPEN · US-GATE-000..003 not passed · US-TASK-001..013 not started (001..004 are "now"
  tasks that run during the NZ/AU build) · US-WATCH-001..007 · US-Q-001..006 open ·
  US-SRC-001..019 recorded.
- **EU (REG-EU v1.0):** EU-FIND-001..016 OPEN (009 application date uncertain — Digital
  Omnibus; 014 medium) · EU-OBL-001..016 standing · EU-STD-001..027 standing
  (harmonisation status to confirm against the OJ list, EU-WATCH-004) · EU-LAW-001..014
  recorded (001, 007, 008, 009, 012 flagged [currency: verify]) · EU-ASSUME-001..006 OPEN ·
  EU-GATE-000..003 not passed · EU-TASK-001..013 not started (001..004 "now" tasks) ·
  EU-WATCH-001..007 · EU-Q-001..006 open · EU-SRC-001..014 recorded.

**Cross-joins added:**
- Shared-stack alignment: `STD-nnn` ↔ `NZ-STD-nnn` ↔ `US-STD-nnn` ↔ `EU-STD-nnn` for
  nnn = 001..026 name the same standard in every jurisdiction; a change to one row's
  edition is a change to all four (replete-standalone divergence rule).
- Clinical evidence transfer: NZ-ASSUME-004 ↔ US-ASSUME-004 ↔ EU-ASSUME-004 ↔ AU GATE-003 —
  one ISO 14155 programme, three admissibility attestations.
- Records: OBL-015 ↔ NZ-OBL-012 ↔ US-OBL-002/US-ASSUME-003 ↔ EU-OBL-015 — one Part 11-capable
  record set.
- Governance Layer non-device status: ASSUME-REG-009 ↔ NZ-Q-003 ↔ US-ASSUME-006 ↔
  EU-ASSUME-006 ↔ MAK-GOV GATE-G0.
- QMS certification route: TASK-REG-024 / Q-REG-011 ↔ US-TASK-008 / US-Q-005 ↔ EU-ASSUME-003.
- Pre-deployment functional-change control: REG-FIND-011 ↔ NZ-OBL-013 ↔ US-FIND-010 (PCCP)
  ↔ EU-OBL-011.
- Jurisdiction sequence: TASK-REG-022 / Q-REG-008 governs the `sequence_position` field
  declared in REG-NZ, REG-US and REG-EU frontmatter.

**Status-vocabulary note:** all four documents use the REG-POSTURE §0.4 vocabulary and the
§0.7 R30 crosswalk unchanged.
