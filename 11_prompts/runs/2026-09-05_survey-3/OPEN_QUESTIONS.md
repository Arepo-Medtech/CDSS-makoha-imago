# OPEN_QUESTIONS — survey-3 (2026-09-05)

## Interpretive calls made (alternative rejected; rows affected)
1. **Scope = 271 files** (`git ls-files` minus `.github/`, `.claude/`, `.impeccable/`, run dirs, dotfiles). Alternative: include `.github/` as design assets — rejected; they are tooling (AGENTS.md "Mechanical checks"), read as evidence only. Rows affected: none filed against `.github/`.
2. **Baseline for attribution = b810db0** (3.1 D-3 default). Alternative: `main` at run start (99e47f3) — rejected because A-005..A-007 would then be "pre-existing" and the one NEW-SINCE-BASELINE readability row (3.2) would vanish.
3. **Readability primary threshold ASL ≤ 35, FK reported** (QUALITY_STANDARD policy). Alternative FK ≤ 14 would move 70 files into READABILITY-DENSE, including every corpus volume. Rows affected: 9 filed vs 70.
4. **Implied HTML token set = values on ≥ 40 % of pages (8/19).** Alternative ≥ 50 % (10/19) gives the same 28 colours (the 16 corpus pages agree exactly); alternative "any page" would make the diagram palette part of the set and hide the drift. Rows affected: 2 STYLE-DRIFT either way.
5. **Skeleton stubs exempt from Q-D-02.** Alternative: 90 ORPHAN rows — rejected (the primer names the tree; INDEX-06 §3 is the parent). Rows affected: 90 not filed; 1 PRESENT note.
6. **Prefix collisions are Layer 3 (TAXONOMY-CONFLICT), not Layer 2 padding slips.** `RG` and `CC` are two requirement-bearing families each; an alias law is the remedy, corpus untouched.
7. **Sequential run** (no sub-agents) — H-1.
8. **Confidence scoring performed by the same writer after the row was written**, against the tool output and (for hand rows) the quoted lines. Alternative: a separate scorer model per row (deep-review's headless pattern) — not available in-session; every score states what a read would add.
9. **Phase 3 deep-read set** = every CRITICAL and WARNING target (1 + 18 rows → 14 distinct files) — full read for files < 60 KB, section reads recorded for REG-POSTURE v1.2 (96 KB) and HARDEN-3.1 (134 KB).

## Questions for the owner
10. **Thresholds** (law 15): accept ASL ≤ 35 / FK-reported; implied-set 40 %; CRITICAL-presentation confidence ≥ 80; entry ≥ 60 — or supply the programme's own.
11. **doc_id supersession rule** (QI-0001): superseded versions keep `doc_id` + `supersedes:` (current practice) or take `REG-POSTURE-v1.1`? Architecture owner; proposed DEC-24.
12. **R25 label** (BSQ-0602) and **W-namespace** (BSQ-0711): two rulings the Architecture owner owes; the run drafts alias laws, it does not choose.
13. **GLOSSARY.md**: build from the draft in QI-0027 (Architecture owner ratifies), or keep Primer 0 §9/§11 as the only glossary and fix the §-anchor in MET-2.2 only?
14. **Prefix collisions RG / CC**: alias law (drafted) or a rename of the *newer* family (RESEARCH-1 gaps → RGAP-; HARDEN-2 class bars stay CC- because 275 ledger rows cite them)? Architecture owner + Corpus owner.
15. **MET-4.1 / MET-2.2 / REG-TASK-OWNERS / SEC-2.1 / RESEARCH-1.2 / tokens.css+v4**: the EXECUTABLE-NOW set for sprint-2 — confirm the order in §c or reorder.
16. **Ledger debt**: HARDEN-1.2 / HARDEN-3.2 rows for every file created since A-005 (governance files, 3.1, 3.2, this run's proposals) — one delta, owed by the MT2 operator (DEC-10) or the manifest owner?
17. **00_inventory.txt**: retire with a successor header ("v1.1 build snapshot, 2026-09-01; tracked tree authoritative") or regenerate as `00_inventory_v1.3.txt` on the next amendment?
18. **Who receives this Queue** — v1.0 open question 7 unchanged (programme lead DEC-09, MT2 operator DEC-10, or the founder); persons remain [NEEDS DEFINITION].
