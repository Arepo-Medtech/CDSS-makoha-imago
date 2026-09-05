# OPEN_QUESTIONS — sprint-1 (2026-09-05)

## Interpretive calls made by the executor (alternative rejected; where recorded)
1. **A-004 appended by the sprint**, not left as proposed text. README "How to change it" step 3 names the appended manifest amendment as the repository's change mechanism and the owner requested the sprint. Alternative (PROPOSED_AMENDMENTS-only) rejected as leaving the queue open. Prefix preservation proven in RUN-REPORT.
2. **Row-form seed named R30.3**, not "REG-R30.2_row-form_seed.jsonl" as BSQ-0202 wrote, because R30.2 landed under A-003 as a delta. Same for the Contents companion: built over **v1.2** (BSQ-0705 said v1.1) and PROMPT-FOLD-1 folds **v1.2** (REG-POSTURE §12.5).
3. **Run-directory files are out of ledger scope** (HARDEN-1.1 scope rule) — they are evidence, not instruction-bearing artifacts. If the MT2 operator wants run directories hardened, add a scope line in a HARDEN-1.2 delta.
4. **Repository files (.gitignore, .github/**, README.md, 00_inventory.txt) are in ledger scope** as CC-5/CC-8 (MT2 §3 "every document in the portfolio"). Alternative (exclude non-authored files) rejected; the classing rule is recorded in HARDEN-1.1.
5. **Rows 60–71 retained ids** assigned to the first twelve of the 21 collapsed artifacts in v1.0's own order; remaining nine take new ids. Alternative (retire 60–71 and re-mint all 21) rejected — BSQ-0104 says "v1.0 row ids retained".
6. **HARDEN-3 W4 "sixteen"** read as HARDEN-1 rows 11–26 (A–L, 1b, 2, harness, grounding); Arch / Primer 0 / integration report take T-046..048 (DEF-006). Alternative (drop three from W4) rejected — every artifact needs a task.
7. **W8 T-100..107** assigned to REPO-MAP, DEPLOY-1/2, OPS-1, GOV-1, SEC-1, RESEARCH-1, RESEARCH-1.1 (05_ originals stay in W1; 05_ regulatory seed deltas join W3 with T-021). Alternative (double-cover 05_ in W1 and W8) rejected — the survey flagged the double coverage as unreconciled.
8. **R30 status crosswalk**: 'standing', 'recorded', 'proposed-normative', 'in force on DEC-22' and cadence words → `OPEN` + `mapping_pending: true`; 'not started' / 'not passed' / 'open' → `OPEN` (§0.4 "OPEN — not started"; `passed` register-only). No ASSUME status touched.
9. **KTX-001..012 rows** carry `source_status_verbatim: none stated at source` (REG-POSTURE §6 states configuration decisions without a status word) and `definition_shape: prose` for the legacy-shape ids §12.2 check 2 lists.
10. **PROMPT-P0 partial run**: only Phase 2 items 1–2 executed (those BSQ-0702 names); Phase 1 (row zero install) and items 3–8 not run — they install software / are gated on DEC-10/DEC-11 or are separate tasks. Directory named `_primer-0` per BSQ-0702.
11. **SEC-2 encryption in transit** recorded as a gap ([NEEDS DEFINITION]) because neither Arch §11 nor SEC-1 states it; nothing was invented to fill the cell.
12. **CI stub for cdss-corpus not added** — intentionally minimal per REPO-MAP skeleton index (firewall); the six stubs cover the trees the survey named.

## Questions for the owner
13. Merge the PR (`sprint-1-build-spec-queue` → `main`) — the Confluence mirror then creates one Imago page per new file and folder. Confirm the mirror's page count expectation (~45 new pages) is acceptable.
14. DEC-22 (adopt EXEC-1 precedence and the run map): every sequencing artifact built this sprint (DEPLOY-1.1, IMAGO-4 v2) is *in force* only on this decision. Founder.
15. DEC-10 / DEC-11 / DEC-02 / DEC-09: PROMPT-HARDEN cannot run, R29 cannot open, and no schema can MOVE to cdss-spine until these close. Programme lead / architecture owner.
16. Regulatory owner (G-09): name the person; rule the R30 status mapping (BSQ-0208); commission FOLD-1 via PROMPT-FOLD-1; dispatch the counsel packets (with the founder).
17. Architecture owner: R25 label ruling (BSQ-0602); FOLD-1 W-namespace rename (BSQ-0711); DEC-13 namespace for MAK-GOV (unblocks BSQ-0707 and BSQ-0391).
18. Should `11_prompts/runs/2026-09-02_survey-2/tools/mermaid/node_modules/` (77 MB, gitignored, if still on the ECOSYSTEM working copy) be deleted? Not present in this clone.
19. The repository flipped to **public** on GitHub at 05:25 UTC on 5 Sep 2026 (it was private at the session start). If unintended, revert before merging: the PR adds counsel-facing packet text (by reference only, no licensed content) and intended-purpose drafts.
