---
doc_id: MET-2.2
title: "MET-2.2 — Decision Register Delta: nine decisions closed by owner ruling; roles named to accounts; closure-evidence column; DEC-23 accepted; DEC-24..26 proposed"
version: "1.0"
date: "2026-09-05"
status: "Added. Additive delta to MET-2 and MET-2.1 per the MET-1.1 pattern; neither is edited. Read MET-2 through MET-2.1 through this file. Where a row here states a State, it governs over the same row in MET-2 / MET-2.1."
supersedes: "nothing — MET-2 v1.0 and MET-2.1 preserved verbatim beside this file"
applies_to: "01_north-star-and-transformation/MET-2_conflict_and_decision_register.md; 01_north-star-and-transformation/MET-2.1_decision_register_delta.md; 01_north-star-and-transformation/MET-4_gap_analysis_and_roadmap.md (G-09 narrowed)"
change_policy: "Additive delta. Closures recorded here were ruled by their owners on 2026-09-05 (§0); the delta author drafted the wording and made one delegated naming ruling (DEC-13). No ASSUME-*, gate or posture is closed by this file."
ruled_by: "Kenny-bytes (Founder; Programme lead; Architecture owner per §1) — rulings given 2026-09-05 in the Claude Code session that produced this file, in answer to the survey-3 Queue §c HUMAN-ONLY rows QI-0167..QI-0174"
req_prefixes: [C, DEC]
minted_here: "C-17; DEC-24, DEC-25, DEC-26 (proposed rows); DEC-23 accepted as a register row from the A-004 proposal — 5 new rows"
req_count: 5
id_families: "C: C-01..C-17 (17 rows, home MET-2 / MET-2.1 / this file) · DEC: DEC-01..DEC-26 (26 rows, 23 minted + 3 proposed, home MET-2 / MET-2.1 / this file; aliases DEC-G1..G4 = DEC-13..16, SD-01..05 = DEC-17..21) · G: G-01..G-11 (11 rows, home MET-4)"
---

# MET-2.2 — Decision closures

## 0. Provenance and delta-reading rule

The survey-3 run (`11_prompts/runs/2026-09-05_survey-3/IMPECCABILITY_QUEUE.md` §c) placed eight
rows in the HUMAN-ONLY bin: QI-0170 (DEC-22), QI-0169 (DEC-10/DEC-11), QI-0167 (DEC-02), QI-0168
(DEC-09), QI-0171 (G-09 / proposed DEC-23), QI-0173 (DEC-13/DEC-14), QI-0172 (DEC-08), QI-0174
(DEC-01). On 2026-09-05 the owner walked the eight rows and ruled on each. This file is the register
record of those rulings. It adds the closure-evidence column the Queue asked for (QI-0019), declares
the C / DEC / G families (QI-0023), and names roles to GitHub accounts for the first time (§1).

Read MET-2 v1.0, then MET-2.1, then this file. A decision not listed in §2 keeps the State it has in
MET-2 / MET-2.1. Nothing here closes an `ASSUME-*`, a `GATE-*` or a regulatory posture: those close
only by their own owners and evidence (REG-POSTURE v1.2 §0.4; AGENTS.md law 4).

## 1. Named roles

Roles in every MET-2 owner cell resolve to accounts as follows. All four accounts are members of the
`Arepo-Medtech` GitHub organisation; logins are written in the casing GitHub returns (§8, check 5). The
order is the owner's stated order of seniority.

| Rank | Account | Roles held | Named by | Named on |
|---|---|---|---|---|
| 1 | Kenny-bytes | Founder (programme) · Programme lead · Architecture owner · MT2 operator (DEC-10) · default repository owner (DEC-09) | Owner ruling (Rows 4 and 6; DEC-10 per §Assumptions) | 2026-09-05 |
| 2 | kendo-Jones | Regulatory owner (G-09 / DEC-23) | Owner ruling (Row 6, seniority order) | 2026-09-05 |
| 3 | Ken-nough | Infrastructure owner (G-09 / DEC-23) | Owner ruling (Row 6, seniority order) | 2026-09-05 |
| 4 | Ken-E-Gee | Security owner (G-09 / DEC-23) | Owner ruling (Row 6, seniority order) | 2026-09-05 |

Not named by this file: Corpus owner / corpus custodian (DEC-05, DEC-12), Counsel (external),
Clinical review, Advisor, Product. Their cells keep `[NEEDS DEFINITION]` where MET-2 has it.

## 2. Decision register — full table with closure evidence

State column governs. "Closes on" is the evidence that closes (or closed) the row.

| DEC | Decision (short) | Owner (§1) | Closes on | Closed on | State |
|---|---|---|---|---|---|
| DEC-01 | Ratify C-01 relabel portfolio-wide; regenerate derived artifacts once | Regulatory + Architecture owners | Owner ratification (this file §3.9). `ASSUME-REG-002` (counsel) is a separate item and stays OPEN in REG-POSTURE until the owner records the attestation date | 2026-09-05 | **Closed — ratified.** Regeneration of derived artifacts is EXECUTABLE-NOW (IMAGO-3 v4: 09_diagrams/register_topology_v4.mermaid and 09_diagrams/cdss_diagrams_v4.html, owed) |
| DEC-02 | Ratify R29 + R30 into Arch §12.2; schemas in 05_ | Architecture owner | Owner ratification (§3.4) | 2026-09-05 | **Closed — ratified.** R29 and R30 are real registers |
| DEC-03 | Rule C-03 substrate (Bedrock ⟷ Baseten) | Infrastructure + Regulatory owners | GATE-001 / TASK-REG-009 | — | Open (MET-2) |
| DEC-04 | Rule C-05 ledger substrate; registers-as-views | Architecture owner | fabric v0 design | — | Open (MET-2) |
| DEC-05 | Ratify or defer FZ-1..6 | Corpus owner + clinical review | fuzzy entry | — | Open (MET-2) |
| DEC-06 | Ratify MAK-J3 from v0.9 / retirement (C-14 reframe) | Counsel + product | GPP first release | — | Open (MET-2 / MET-2.1) |
| DEC-07 | Patient-surface scope | Counsel + product | GATE-000 | — | Open (MET-2) |
| DEC-08 | IMPL rename ratification; Observer cadence | Architecture owner | Owner ratification (§3.6) | 2026-09-05 | **Closed — both ratified** (IMPL rename; quarterly Observer cadence from L4) |
| DEC-09 | New repo owners + namespace prefixes {FAB, UIP, UIC, GPP} | Programme lead (Kenny-bytes) | Owner ruling (§3.5) | 2026-09-05 | **Closed.** Owners named; prefixes ratified into Arch §13.3 (§14.4 Proposed → ratified) |
| DEC-10 | Name the MT2 operator | Programme lead | Owner ruling (§3.2; §Assumptions) | 2026-09-05 | **Closed.** Operator = Kenny-bytes |
| DEC-11 | Accept C-11 row-zero reconciliation rule | MT2 operator | Operator acceptance (§3.3) | 2026-09-05 | **Closed — accepted** |
| DEC-12 | HeyDoc corpus-seed intake; below-README inventory (G-08) | Corpus custodian | corpus seeding | — | Open (MET-2) |
| DEC-13 (=DEC-G1) | MAK-GOV namespace & doc_id | Architecture owner (delegated to delta author: naming only) | Delegated ruling (§3.7) | 2026-09-05 | **Closed.** doc_id `MAK-GOV` permanent; G-family internal IDs stand; not J-series |
| DEC-14 (=DEC-G2) | Ship the non-device Governance Layer as first revenue | Founder + advisor | Owner ruling (§3.8) | 2026-09-05 | **Closed for build scope.** Built to finish and held release-ready; commercial timing is outside this register and gates no build task |
| DEC-15 (=DEC-G3) | NDG-3 latency floor value | Regulatory + product | Sprint V1-S0 | — | Open (MET-2.1) |
| DEC-16 (=DEC-G4) | cdss-governance repo split | Architecture owner | V1-S1 | — | Open (MET-2.1) |
| DEC-17 (=SD-01) | V1 use case | Founder + advisor | RUN-0, week 1–2 | — | Open (MET-2.1) |
| DEC-18 (=SD-02) | V2 clinical domain | Clinical + regulatory | checkpoint month 4 | — | Provisionally resolved: respiratory (MET-2.1) |
| DEC-19 (=SD-03) | NZ sponsor structure | Founder + NZ counsel | NZ-GATE-0 | — | Open (MET-2.1) |
| DEC-20 (=SD-04) | V2 supplies Australia pre-ARTG, or NZ-only | Founder + counsel | before V2-S3b | — | Open (MET-2.1) |
| DEC-21 (=SD-05) | Governance Layer namespace/repo | Architecture owner | namespace component merged into DEC-13 (MET-2.1 alias law); repo component rides DEC-16 | 2026-09-05 (namespace only) | **Namespace component closed with DEC-13; repo component Open with DEC-16** |
| DEC-22 | Adopt EXEC-1 precedence (EX-1) and the run map (EX-5) | Founder (programme) | Owner adoption (§3.1) | 2026-09-05 | **Closed — adopted.** The 10_ layer v1.2 set is the working set |
| DEC-23 | Name regulatory, infrastructure and security owners; set RTO/RPO; approve the L5 multi-region DR drill protocol (from G-09; proposed in A-004) | Founder (names) → Infrastructure owner (values) | Names: owner ruling (§3.10). Values: infrastructure owner records RTO/RPO and the drill protocol in a DEPLOY-1.2 delta | 2026-09-05 (names) | **Accepted as a register row. Names closed; RTO/RPO values and drill protocol Open (Ken-nough)** |
| DEC-24 | doc_id supersession rule (survey-3 QI-0001) | Architecture owner | ruling on §5 draft | — | **Proposed — Open** |
| DEC-25 | R25 label: "Build Evidence & Assumptions Ledger" vs "property runs" (BSQ-0602 / QI-0029) | Architecture owner | ruling on §5 draft | — | **Proposed — Open** |
| DEC-26 | Namespace alias laws: W-n, RG, CC (QI-0030 / QI-0024 / QI-0025) | Architecture owner | ruling on §5 draft | — | **Proposed — Open** |

Census: DEC rows 26 = 23 minted (DEC-01..23) + 3 proposed (DEC-24..26). Closed by this file: 9
(DEC-01, 02, 08, 09, 10, 11, 13, 14, 22) + DEC-21 namespace component + DEC-23 names. Open: 14
(DEC-03..07, 12, 15..17, 19, 20, 24..26) + DEC-18 provisional + DEC-21 repo component + DEC-23 values.

## 3. Rulings in full

### 3.1 DEC-22 — EXEC-1 precedence and run map adopted
EX-1 (sequencing precedence of the 10_ layer over MET-4's roadmap, volume phasing tables and
DEPLOY-1) and EX-5 (every phase name resolves to a RUN row; the hardening pass is not rescheduled)
are adopted. The working set is REG-POSTURE v1.2, REG-SPRINT v1.0 read through REG-SPRINT-1.1 and
1.2, and EXEC-1. Content authority is unchanged (EX-1 second sentence). Consequence: RUN-0 may
start; DEPLOY-1.1 and IMAGO-4 v2 are in force; every timeline cell in the MET-4.1 and
REG-TASK-OWNERS drafts (Queue §c.1) is filled from the run map as fact.

### 3.2 DEC-10 — MT2 operator named
The MT2 operator, who receives the consolidated blocker report (MT2 directive §6, §7(2)), is
Kenny-bytes. Consequence: the 41 `[NEEDS DEFINITION]` cells that read "MT2 operator" in HARDEN-1.1 /
HARDEN-3.1 resolve to this name in the HARDEN-1.2 / HARDEN-3.2 delta; PROMPT-HARDEN may be launched
once row zero (W0, T-000) is run by the operator. This file writes no R29 row (AGENTS.md law 5).

### 3.3 DEC-11 — C-11 row-zero reconciliation rule accepted
The operator accepts MET-2 C-11 as ruled: row zero installs the whole skills pack, confirms the
live inventory against the directive's §2.2 list at install time, records any delta verbatim, and
halts the pass if the two cannot be reconciled.

### 3.4 DEC-02 — R29 and R30 ratified as real registers
R29 Hardening Coverage Ledger and R30 Regulatory Posture Register are ratified into Arch §12.2 as
registers, not proposals. Their schemas (`05_registers-and-contracts/`) move to `cdss-spine`
on the schema move; until then the 05_ files are the schema of record. Consequence: register home
for every T-nnn task and R29 row is R29; for every R30.3 row, R30; the six `PENDING-REGISTER-HOME`
placeholders in scope resolve accordingly in their owning files' next delta. Arch §12.2 is retained
unedited; this ruling is recorded here and carried into the next Architecture successor.

### 3.5 DEC-09 — repository owners and namespace prefixes
Owner of every repository in REPO-MAP v2 (14 existing; proposed `cdss-fabric`, `cdss-compiler`,
`cdss-ui-clinician`, `cdss-ui-patient`, `cdss-integration`; the GPP channel) is Kenny-bytes as
Programme lead. The eligible owner pool for any later per-repository delegation is the four accounts
of §1. The PFX set of Arch §13.3 gains {FAB, UIP, UIC, GPP}: §14.4 moves from Proposed to ratified.
Consequence: the 98 repo-owner and 22 component-owner placeholder cells resolve in HARDEN-1.2;
REPO-MAP v3 carries an owner column; the cdss-compiler primer (BSQ-0391) is unblocked on this
decision (it remains dependent on DEC-13, now also closed).

### 3.6 DEC-08 — carry-over ratifications
The IMPL rename (Implementer Contract; MET-1 §"Build-execution layer") is ratified as the
operational and documentary name. The Observer's cadence beyond per-level exits is quarterly from
L4, as MET-1 proposed. Consequence: the cadence text in Arch §13.7, GOV-1 and OPS-1 now cites a
ratified position; a wording delta is owed where those files say "proposed".

### 3.7 DEC-13 — MAK-GOV namespace (delegated naming ruling)
The owner delegated this ruling to the delta author as a naming-convention matter. Ruling: the
doc_id `MAK-GOV` is permanent; "Addendum G" remains its display title; the internal families
`NDG-n`, `GATE-Gn`, `T-Gnn`, `SG-V1-n` stand; `DEC-G1..G4` remain aliases of DEC-13..16 under the
MET-2.1 alias law. MAK-GOV is not a J-series member. Grounds: (a) tracked files in nine folders outside run
directories already cite `MAK-GOV` (command and pasted output in §8, check 4); (b) `MAK-<TLA>` is the corpus volume
convention; (c) MAK-GOV's own `naming_note` states the J-series denotes regulatory fork branches and
that it is not a J-1/J-2 alternative, and J-3 is under retirement (DEC-06). Consequence: the MAK-GOV
integration delta (BSQ-0707) and the NDG verification cells are unblocked; the MAK-GOV frontmatter
`naming_note` is superseded by this ruling and is corrected in the volume's next version by the
corpus owner (nothing under 03_/10_ is edited here).

### 3.8 DEC-14 — Governance Layer: build to finish
The Governance Layer is built to completion as a sprint deliverable and held release-ready. It is
established (C-15) as a non-patient-facing artifact usable as a reduced-function subset app. Whether
and when it ships as first revenue is a commercial and partnership matter that this register does not
gate and that gates no build task. The MET-2.1 trigger `SG-V1-0` remains the trigger for the
regulatory attestation the commercial step would need; it is not a build gate.

### 3.9 DEC-01 — C-01 relabel ratified
The C-01 relabel (exempt-CDSS posture replaced by the classified posture, applied through the
deprecation notices listed in MET-2 C-01) is ratified portfolio-wide by the Regulatory and
Architecture owners. Derived artifacts are to be regenerated once: IMAGO-3 v4, as
09_diagrams/register_topology_v4.mermaid and 09_diagrams/cdss_diagrams_v4.html (successors to the v3
files; EXECUTABLE-NOW; owed). `ASSUME-REG-002` (counsel attestation that the CDSS exemption
is unavailable) is a separate register item owned by AU regulatory counsel; it stays OPEN in
REG-POSTURE v1.2 until the owner records the attestation date. The owner has stated they will record
it when it arrives. See C-17.

### 3.10 DEC-23 — accepted; owners named; values open
DEC-23 (proposed in 00_MANIFEST A-004 from G-09) is accepted as a register row. Names: regulatory
owner kendo-Jones, infrastructure owner Ken-nough, security owner Ken-E-Gee (§1). RTO and RPO
targets, the L5 multi-region DR drill protocol and the commercial thresholds of G-09 are not set by
this file; the infrastructure owner records them in a DEPLOY-1.2 delta, and G-09 in MET-4 is thereby
narrowed (owners named; values pending) in MET-4.1.

## 4. New conflict

| # | Conflict | Handling |
|---|---|---|
| C-17 | REG-POSTURE v1.2 §3.1 (l.473): "DEC-01 (relabel portfolio-wide) remains Open; closes only on `ASSUME-REG-002`" ⟷ this file: DEC-01 closed by owner ratification 2026-09-05 with `ASSUME-REG-002` still OPEN | **Dated divergence, recorded.** The decision register governs the state of a DEC; REG-POSTURE governs the state of an ASSUME. DEC-01 is Closed; `ASSUME-REG-002` is OPEN; GATE-000 is unchanged. REG-POSTURE's sentence reads as superseded on the DEC-01 clause only, to be carried into REG-POSTURE's next version by its owner |

Census: C rows 17 = 12 (MET-2) + 4 (MET-2.1) + 1 (this file).

## 5. Proposed decisions DEC-24..26 — drafted law text, Open

Drafted by survey-3 (`QI.jsonl` rows QI-0001, QI-0029, QI-0030, QI-0024, QI-0025). Each becomes
law only by the Architecture owner's ruling recorded in a later delta.

- **DEC-24 — doc_id supersession rule.** "Superseded versions keep their doc_id and MUST carry
  `supersedes:`; a citation of a versioned file MUST name the version (README 'How to cite' already
  requires the commit)."
- **DEC-25 — R25 label.** One label in Arch §12.2 is authoritative ("Build Evidence & Assumptions
  Ledger"); "property runs" (Primer A A10 / IMAGO-3) becomes its alias; IMAGO-3 v4 carries the
  authoritative label.
- **DEC-26 — namespace alias laws.** (a) Unqualified `W-n` means HARDEN-3 (the pass); FOLD-1 steps
  are cited `FOLD-1 W-n` or `FW-n`. (b) `RG-nn` (two-digit) = research gap, home RESEARCH-1.n;
  `RG-n` (one-digit) = MAK-CEC requirement, home MAK-CEC; citations use the padded form; new research
  gaps mint as `RGAP-`. (c) `CC-n` in 04_/05_/06_ and HARDEN rows = HARDEN-2 class bar; MAK-LBP `CC-n`
  resolves only inside 03_; the R29 schema `class` enum spells the bars `HCC-n` on ratification. The
  corpus is untouched in every case.

## 6. Consequential work this file creates (new files only; sprint-2)

| Owed file | Fills | From |
|---|---|---|
| HARDEN-1.2 and HARDEN-3.2 deltas under 04_hardening/ (owed, not yet written) | 98 repo-owner + 41 operator + 22 component + 15 regulatory owner cells; ledger rows for every file since A-005 | DEC-09, DEC-10, DEC-23; A-005..A-009 debt |
| MET-4.1 gap register delta under 01_north-star-and-transformation/ (owed) | owner · DEC · RUN/gate · exit evidence · register home per G; G-09 narrowed | Queue QI-0018; DEC-22, DEC-23 |
| REPO-MAP v3 under 06_repositories/ (owed) | owner column | DEC-09 |
| REG-TASK-OWNERS companion under 10_regulatory-execution/ (owed) | task · owner · evidence · R30.3 row | Queue QI-0020; DEC-22, DEC-23 |
| DEPLOY-1.2 delta under 07_deployment-and-operations/ (owed) | RTO/RPO; L5 DR drill protocol | DEC-23 values (Ken-nough) |
| 09_diagrams/register_topology_v4.mermaid and 09_diagrams/cdss_diagrams_v4.html (IMAGO-3 v4 successors to the v3 files; owed, written without backticks) | regenerated derived artifacts; R29/R30 ratified; R25 label once DEC-25 rules | DEC-01, DEC-02 |
| Wording deltas: Arch §13.7 / GOV-1 / OPS-1 cadence; Arch §12.2 R29/R30 and §14.4 status | "proposed" → ratified | DEC-02, DEC-08, DEC-09 |

## 7. What this file did not do

Closed no `ASSUME-*`, no `GATE-*`, no posture; wrote no R29 row; launched no pass; edited nothing
under 00_–11_ other than by this new file and the appended manifest amendment (A-009). DEC-03..07,
DEC-12, DEC-15..17, DEC-19, DEC-20 keep their MET-2 / MET-2.1 State. DEC-24..26 are proposed only.
Ledger debt: this file has no HARDEN-1.1 row or HARDEN-3.1 task; it joins the A-005..A-008 debt.

## 8. Self-audit (run 2026-09-05 on the PR branch; commands pasted, outputs quoted)

1. **Append-only** — `python3 .github/audit/append_only.py origin/main` (run after the final edit of both changed files; CI job "Mechanical audit" on PR #15: pass) →
```
00_MANIFEST.md: appended 6887 bytes; prefix preserved (sha256 6867157e3d4c)
append-only: 2 changed paths, 2 permitted, 0 violations
```
2. **References** — `python3 .github/audit/refcheck.py 00_MANIFEST.md 01_north-star-and-transformation/MET-2.2_decision_closures_delta.md` → `dead in-repo paths: 0; unresolved anchors: 0`. Owed future files in §6 are written without backticks so they are not read as references.
3. **Census parity (§2)** — `grep -c '^| DEC-'` → 26 rows; `grep -o '^| DEC-[0-9]*' | sort -u | wc -l` → 26 distinct ids = DEC-01..26 · `grep -c '^| DEC-.*\*\*Closed'` → 9 closed rows (DEC-01, 02, 08, 09, 10, 11, 13, 14, 22) · `grep -c '^| C-17'` → 1. C census 12 + 4 + 1 = 17; DEC census 23 minted + 3 proposed = 26; both agree with the frontmatter `req_prefixes` (C, DEC — the families this file mints into; G is cited, not minted) and `id_families`.
4. **DEC-13 ground (a)** — `git ls-files | grep -v '^11_prompts/runs/' | xargs grep -l 'MAK-GOV' | wc -l` → 37 tracked files (this file and the manifest included); by top-level folder:
```
1 .github
   1 00_MANIFEST.md
   2 01_north-star-and-transformation
   2 04_hardening
   3 05_registers-and-contracts
   1 07_deployment-and-operations
   1 08_research
   9 10_regulatory-execution
  16 11_prompts
   1 README.md
```
5. **Account logins (§1)** — `gh api orgs/Arepo-Medtech/members -q '.[].login'` →
```
Ken-E-Gee
Ken-nough
kendo-Jones
Kenny-bytes
```
6. **Frontmatter** — `python3 .github/audit/frontmatter_census.py` → core-field gaps for this file: none; `files minting requirement blocks without req_prefix: 0`.

## Assumptions (one)

- **DEC-10 name.** The owner ruled "closes as per the suggested responses" without naming the
  operator. This file names Kenny-bytes, the Programme lead who receives the consolidated blocker
  report under MT2 §6. If a different account is intended, a one-row delta (MET-2.3) re-names it.
