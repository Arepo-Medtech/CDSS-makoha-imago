# 10_regulatory-execution — ASSESSMENT (Phase 2)

Census: 7 files, 121,972 B. Read: EXEC-1 (full), FOLD-1 (full), REG-SPRINT-1.1 (D-1 full + D-2..D-5 headings/tables), REG-SPRINT v1.0 (headings + sprint tables), REG-NZ (frontmatter, §6–§8 full, headings), MAK-GOV (frontmatter, headings, §4 head, §5 full), REG-POSTURE v1.1 (frontmatter, §0.4, §0.7, §12 full, headings). Seven files, seven separate judgements (law 7).

## 1. Discovery and labels
| Item | Bytes | Label(s) | Why | Load-bearing? |
|---|---|---|---|---|
| `EXEC-1_execution_directive.md` | 11,180 | DIRECTIVE | "Normative for sequencing and precedence"; EX-1..10; RUN-0..4 | crit 2 — governs sequencing portfolio-wide (EX-1) |
| `REG-POSTURE_v1.1.md` | 60,793 | REGULATORY (canonical posture; ADVISORY_ONLY) | EX-3 canonical; mints 12 ID families, 120 IDs | crit 2 — counsel attachment (EX-6); R30 source; GATE-000 |
| `REG-NZ_v1.0.md` | 13,194 | REGULATORY (jurisdiction brief) | 7 NZ-* families | crit 2 — NZ packet; NZ-GATE-0 |
| `MAK-GOV_addendum-g_v0.9.md` | 17,124 | REGULATORY + build target (proposed-normative) | NDG-1..14; classification argument | crit 2 — DEC-14 first revenue; SG-V1-0 |
| `REG-SPRINT_v1.0.md` | 10,741 | WORKLIST / PLAN (run plan) | three-version plan; V*/SG-*/SD-* | crit 2 — EX-1 gives its ordering precedence (via 1.1) |
| `REG-SPRINT-1.1_delta.md` | 6,141 | DELTA | D-1..D-5 | crit 2 |
| `FOLD-1_antennae_fold_worklist.md` | 2,799 | WORKLIST | W1–W5 fold of MAK-ANT v1.1 | crit 2 — closes C-13 (EX-3 divergence); output is a 03_ corpus file (CORPUS-OWNER) |

## 2. Presence pass — folder chain
| Link | Applicability | PRESENT / ABSENT | Evidence |
|---|---|---|---|
| P-F-01 BRIEFING | APPLIES (directive, posture, brief, addendum, plan, delta, worklist — 4+ classes; the *layer* concept is explained only in EXEC-1's preamble) | PARTIAL → fold into INDEX | EXEC-1 l.16–24 preamble |
| P-F-02 INDEX | APPLIES | PARTIAL — EXEC-1 Part 4 "Integration ledger" lists 6/7 files (+ MET-2.1, R30.1, A-002) with Type only | EXEC-1 Part 4 |
| P-F-03 corpus-grade | APPLIES | §3–4 | — |
| P-F-04 PRIMER / runbook | APPLIES — RUN-0..4 and EX-8's week-one board are executable programmes; EXEC-1 states contents + exits but not steps/owners/evidence per item beyond EX-10's "lands as a register row" | ABSENT — **however PROMPT-P0 already specifies RUN-0's executor-doable items** (counsel packet assembly, DRAFT_TASK-REG-001, DRAFT_T-G01, P0 board) | `grep -n 'counsel_packet_AU' 11_prompts/PROMPT-P0_primer0_launch.md` → l.78, l.103 |
| P-F-05 LAUNCH PROMPT | APPLIES — RUN-0 items (PROMPT-P0 ✓ exists, not run); FOLD-1 W1–W5 (Claude-executable, CORPUS-OWNER ratifies) — no prompt; MAK-GOV G0–G2 build (NDG) — no prompt (DEC-14) | PARTIAL | `ls 11_prompts | grep -i 'fold\|gov\|reg-exec'` → PROMPT-PRM-ANT only (MAK-ANT primer) |
| P-F-06 ARTIFACT-HTML | APPLIES to REG-POSTURE v1.1, MAK-GOV, REG-NZ (counsel-facing, EX-6) | ABSENT — `artifacts-html/antennae-corpus.html` renders MAK-ANT v1.0 (REG-POSTURE v1.0 folded), not v1.1 | `ls 03_*/artifacts-html | grep -i 'posture\|gov\|nz'` → antennae-corpus.html only |
| P-F-07 SKELETON home | APPLIES to MAK-GOV (build target → `cdss-governance`, DEC-16) | PARTIAL — governance skeleton has README + MANIFEST; no Governance-Layer/NDG directory; MAK-GOV §5 says REPO-MAP should reclassify cdss-governance "from register home to releasable repository" — not done | `grep -n NDG 06_repositories/REPO-MAP_v2.md` → 0 |
| P-F-08 HARDEN rows/tasks | APPLIES (law-grade; EX-5 puts 10_ in the W11 sweep) | **ABSENT ×7 rows, ×7 tasks** | `grep -c '10_\|EXEC-1\|REG-POSTURE_v1.1\|MAK-GOV\|REG-NZ\|REG-SPRINT\|FOLD-1' 04_hardening/HARDEN-1*` → 0; HARDEN-3 → 0 |
| P-F-09 00_MANIFEST row | APPLIES | PRESENT (§8: 7 = 7) | CENSUS §1 |
| P-F-10 honesty | APPLIES | PRESENT — every file carries `authority: ADVISORY_ONLY` or an honesty status; 00_MANIFEST §8 honesty lines cover the layer; **one claim not evidenced by the tree**: "Counsel packets drafted, not sent" — no packet artifact exists (`grep -rln -i 'counsel packet'` → EX-6 spec, REG-POSTURE, PRM-ANT, PROMPT-P0 spec, 00_MANIFEST only) | — |

## 3. Presence pass — document contract
| P-line | EXEC-1 | REG-POSTURE v1.1 | REG-NZ | MAK-GOV | REG-SPRINT v1.0 | REG-SPRINT-1.1 | FOLD-1 |
|---|---|---|---|---|---|---|---|
| P-D-01 core | PRESENT | PRESENT (`date_issued` variant; no `date`) | PRESENT (variant) | PRESENT | PRESENT (variant) | PRESENT (variant) | PRESENT |
| P-D-02 honest status | PRESENT | PRESENT (DRAFT; ADVISORY_ONLY; attestation_required) | PRESENT | PRESENT (proposed-normative-draft; dual authority) | PRESENT (DRAFT) | PRESENT | PRESENT ("Worklist only") |
| P-D-03 precedence/authority | PRESENT (subordinate_to ×3; EX-1) | PRESENT (authority; supersedes; wrapped_by; blocks) | PRESENT (companion_to; authority) | PRESENT (subordinate_to ×3; supersedes_role_of) | PRESENT (authority) — **no read-through-1.1 declaration in the base** | PRESENT (applies_to; change_policy) | PRESENT (status; AN-5) |
| P-D-04 req declaration | PRESENT (EX/10) | PARTIAL — `id_prefixes` ×12 declared; counts in §12.1 not frontmatter | PARTIAL — `id_prefixes` ×7; **no counts anywhere** | PRESENT (NDG/14) | **ABSENT** — mints V1-S0..S2, V2-S0..S3b, V2-E1..E5, V1-C1..C2, SG-V*, SD-01..05 with no declaration | PRESENT-ish (D-1..D-5 named; no count field) | PARTIAL — W1–W5 (no count; **W-ids collide with HARDEN-3 W0–W11 namespace**) |
| P-D-05 requirement blocks / sourced rows | PRESENT (10 blocks, Statement + Rationale trace) | PASS-variant — ID tables with `source`/SRC-REG columns (advisory register form; 0 'Rationale trace' lines) | PASS-variant — NZ-FIND rows cite NZ-SRC; **0 Rationale trace** | PRESENT (14 NDG blocks) | PARTIAL — sprint tables (ID · content · weeks · gate), no source column | PRESENT (each D-n: Error/Amendment/Risk) | PARTIAL (steps; sources inline) |
| P-D-06 Contents (>15 KB) | N/A (11 KB) | **ABSENT** (60,793 B; 13 §§ + appendices; `grep -c '^## Contents'` → 0) | N/A (13 KB) | **ABSENT** (17 KB; 6 parts) | N/A | N/A | N/A |
| P-D-07 traceability | PRESENT | PRESENT (§11 Sources; SRC-REG) | PRESENT (§8 Sources + confidence note) | PRESENT (§2 argument cites MAK-ABC/FFC; §5 ledger) | PARTIAL (no sources section) | PRESENT (advisor's letter; REG-NZ) | PRESENT |
| P-D-08 ID census = count | PRESENT (Part 5 item 1: 10) | PRESENT (§12.1: 120 IDs, 12 families, Δ v1.0) | **ABSENT** | **ABSENT** (14 blocks countable; no census section) | **ABSENT** | PRESENT-ish (five amendments = D-1..D-5 ✓) | **ABSENT** |
| P-D-09 self-audit | PRESENT (Part 5, 8 checks, PASS each) | PRESENT (§12.2, 10 checks; §12.3 known gaps) | **ABSENT** | **ABSENT** | **ABSENT** | **ABSENT** | PARTIAL (W5 seal checks defined, not run) |
| P-D-10 owner + closed-enum status per row | RUN rows: exits ✓, owner ✗ | rows: status from §0.4 ✓ (check 7 PASS); attesting party ✓ | rows: Party ✓ Status OPEN ✓ | NDG blocks: level ✓; DEC-G rows: Owner ✓ Timing ✓ | rows: gate ✓, owner ✗, status ✗ | D rows ✓ | steps: owner at file level ✓ |
| P-D-11 delta discipline | PRESENT (EX-2 declares REG-SPRINT read-through) | PRESENT (§A amendment log v1.0→v1.1; supersedes) | N/A (no delta) — **but NZ-Q-004 was minted in REG-SPRINT-1.1 D-2 / R30.1, not in REG-NZ §6** | N/A | base silent (EX-2 carries it) | PRESENT (applies_to; change_policy; D-1..D-5) | N/A |
| P-D-12 placeholders | none | `[NEEDS DEFINITION]` owner ↔ G-09 ✓ (§12.3) | none | none | none | none | owner ↔ G-09 ✓ |
| P-D-14 owner | ABSENT (Founder implied via DEC-22) | ABSENT (§12.3 states it — G-09) | ABSENT | ABSENT (DEC-G owners named per decision) | ABSENT | ABSENT | PRESENT (`owner:` field, [NEEDS DEFINITION]) |
| P-D-15 execution fields | RUN rows: contents + exits ✓; no steps/failure per item (directive, not runbook) | §7 sequenced plan (phases/gates) | §5 sequenced actions | §4 sprint plan G0–G2 | sprint tables | D rows | W1–W5 steps; W4 "record the check output"; W5 seal; **no on_fail** |
| P-D-16 xrefs | PASS (Part 5 item 3) | PASS (checks 2/4/6/9) | PASS | **FAIL** — REG-FIND-013, TASK-REG-023 (BSQ-0001) | PASS (SG/V ids defined in-table) | PASS | PASS |

## 4. Measurement pass — REGULATORY / WORKLIST / DELTA floors
| Item | Contract line | PASS/FAIL | Evidence |
|---|---|---|---|
| REG-POSTURE | every OPEN item names attesting party and blocked gate | PASS (§12.2 checks 3, 5) | §12.2 |
| REG-POSTURE | no ASSUME closed internally | PASS (check 8 vacuous — zero closed) | §12.2 |
| REG-POSTURE | WATCH cadences | PASS (§10; WATCH-REG-001..007) | §12.1 |
| REG-POSTURE | canonical-vs-annex divergence listed, dated, owned | PASS (EX-3; C-13; FOLD-1 W5 closes; owner [NEEDS DEFINITION] — G-09) | MET-2.1 C-13 |
| REG-POSTURE | P-D-06 Contents | FAIL (60 KB, no Contents) | grep |
| REG-NZ | OPEN items name party + gate | PARTIAL — Party ✓; blocked gate not per row (NZ-GATE-0 named in §5) | §6 |
| REG-NZ | WATCH cadences | PASS (NZ-WATCH-001..003) | §7 |
| REG-NZ | census/self-audit; NZ-Q-004 | FAIL — no census; NZ-Q-004 (the "highest-value" transition question per EX-6/D-2) absent from §6 | grep NZ-Q-004 → 0 |
| MAK-GOV | requirement blocks + census + self-audit | PARTIAL — 14 NDG blocks ✓; no census/self-audit; Contents absent | grep |
| MAK-GOV | §5 integration ledger executed | **STALE** — of 10 declared integrations, 2 exist (MET-2 rows → MET-2.1 ✓; R30 seed → R30.1 ✓); not done: abdomen/four-faces/antennae annexes (CORPUS-OWNER; AN-5 re-run), REG-POSTURE v1.2 (REG-FIND-013/TASK-REG-023 dangling), MET-4 gap row ("non-device classification unattested" — `grep -c non-device MET-4` → 0), REPO-MAP reclassification (`grep NDG REPO-MAP` → 0), DEPLOY-2 NDG-5/NDG-7 criteria (0), MAK-J3 retirement notice (blocked DEC-06) | MAK-GOV §5 table |
| REG-SPRINT (via 1.1) | WORKLIST: one task per artifact; dependency order with reason; class/skills/exit | PASS-variant — sprint rows with weeks + gates; reasons in prose; owner/status absent | tables |
| REG-SPRINT-1.1 | DELTA: base + version; D-n; base read-through | PASS (applies_to; D-1..D-5; EX-2 declares read-through) | frontmatter |
| FOLD-1 | WORKLIST: steps; exit; owner | PASS-variant — W1–W5; W5 seal; owner [NEEDS DEFINITION]; **on_fail absent; W-namespace collides with HARDEN-3** | text |
| EXEC-1 | DIRECTIVE: eight properties on itself; precedence; RFC 2119 | PASS (Part 5 self-audit; EX-1; normative_language) | Part 5 |
| ALL | status honest against the tree | PASS except "Counsel packets drafted" (00_MANIFEST §8) — no packet artifact; PROMPT-P0 (unrun) is where it would be produced | grep |

## 5. Chain confirmation
CHAIN.md 10_ confirmed; corrections: P-F-04/05 PARTIAL via PROMPT-P0 (exists, unrun); MAK-GOV §5 integration ledger 2/10 executed.

## 6. Weighting summary
Queue (≥3): BSQ-0701 INDEX-10 · BSQ-0702 counsel packet artifacts (run PROMPT-P0 Phase 2) · BSQ-0703 HARDEN-1 rows ×7 · BSQ-0704 HARDEN-3 tasks ×7 · BSQ-0705 REG-POSTURE Contents/companion · BSQ-0706 REG-NZ-1.1 delta (census, NZ-Q-004, self-audit) · BSQ-0707 MAK-GOV integration status + census (after DEC-13/14) · BSQ-0708 PROMPT-FOLD-1 · BSQ-0709 REG-SPRINT census companion · BSQ-0712..0714 DECISION-PENDING (DEC-22; DEC-13/14/16/17; DEC-06). Below: BSQ-0710 html twins (2), BSQ-0711 W-namespace collision (2), BSQ-0715 "drafted" contradiction (2, ESCALATED), PRESENT rows ×7.

## 7. Validation
rows=22 invalid=0 valid=22
