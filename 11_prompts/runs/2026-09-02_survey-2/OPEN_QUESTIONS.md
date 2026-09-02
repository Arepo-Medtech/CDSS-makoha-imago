# OPEN_QUESTIONS — run 2026-09-02_survey-2

## Placeholders left unresolved
1. `{{RUN_DATE}}` — resolved by the executor to `2026-09-02` (today). Confirm, or rename the run directory (the only path that embeds it).

## Ambiguities in PROMPT-SURVEY-2 interpreted by the executor (with the interpretation)
2. "Fan-out is permitted in Phase 2" — executed single-context (no sub-agents) because the work runs on the linked machine through one shell; nothing in the outputs depends on this. Interpretation recorded; no change needed.
3. `folder` enum has no value for findings whose artifact lives outside 04_–10_ (00_MANIFEST, 11_ prompts, 06_ pointer for a 05_ item). Interpretation: filed under the target folder the finding *serves*, with the out-of-scope path in `artifact_path`/`evidence` (per `<scope>`). Rows: BSQ-0004, 0103, 0393, 0395, 0408, 0605, 0702, 0708, 0715.
4. "at least one row per item + applicable chain link" — for 06_ the 90 skeleton files each got a row (MT2 §3); chain links got folder-level rows. Interpretation: presence rows for chain links that are PRESENT were folded into the ASSESSMENT §2 table rather than duplicated as PRESENT-CONFORMANT rows (folder-level PRESENT links: 00_MANIFEST row ×7, honesty ×7, HARDEN rows where present). If the operator wants one row per PRESENT chain link too, add 21 PRESENT rows — no verdict changes.
5. P-D-06 Contents threshold (15 KB / >6 parts) and the byte-count seeds: both `[ASSESSOR-PROPOSED]`; the P-line applies to 2 target files (REG-POSTURE, MAK-GOV).
6. The prompt's `known_state` said 06_ has 93 files — it has 91 excluding `.DS_Store` (CENSUS §9). No row filed against the prompt; recorded here.
7. The prompt lists `date` as a core frontmatter field; four 10_ files use `date_issued`. Treated as a variant (CENSUS §9). If the operator wants strict field names, four P-D-01 FAIL rows follow (weight 1).

## Questions for the operator
8. Should the seven INDEX files be one build item or seven? The specs are written per folder so they can be built in the §d order and ratified piecemeal; a single session could build all seven in one pass — say which.
9. HARDEN-1.1 / HARDEN-3.1 are pre-ratification seed deltas (A-001 precedent). Confirm the architecture owner accepts seed deltas before DEC-02 closes; if not, both rows move to EXECUTABLE-AFTER-DECISION (DEC-02) and every INDEX cites "ABSENT until ratification" in its HARDEN columns.
10. R30 status mapping (BSQ-0208): which enum value should a *standing obligation* (OBL-*) and a *watch cadence* row take — `OPEN`, or a new register-only value the way `ARMED`/`passed` are register-only? Regulatory owner's call; the row-form seed ships with `source_status_verbatim` until then.
11. BSQ-0602 — is R25 "Build Evidence & Assumptions Ledger" (Arch §12.2) or "property runs" (Primer A A10; IMAGO-3)? If the primer layer is right, Arch §12.2 needs an annex note, not the diagram.
12. BSQ-0711 — rename FOLD-1 W1–W5 (FW-1..5) via a FOLD-1.1 delta, or accept the bare-W ambiguity? Architecture owner.
13. Who receives this hand-back — the MT2 operator (DEC-10, unnamed), the manifest owner (unnamed), or the founder? Every `owner` field in the queue carries the role; persons remain `[NEEDS DEFINITION]` per DEC-09/DEC-10/G-09.
14. May the operator delete `tools/mermaid/node_modules/` (77 MB, run-local tooling, `.gitignore`d)? This session could not delete on the mounted folder.
15. Should PROMPT-P0 be run next (BSQ-0702 — counsel packets, the longest lead) before any build item here? This run recommends yes (§h), but sequencing across prompts is the founder's call under DEC-22.
