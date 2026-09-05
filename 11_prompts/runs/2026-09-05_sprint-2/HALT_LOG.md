# HALT_LOG — sprint-2 (2026-09-05)

| # | When | What halted | Type | Resolution |
|---|---|---|---|---|
| H-1 | task extraction | first regex over the posture task tables returned 59 of 60 rows (`TASK-REG-020` "ARTG inclusion." is shorter than the length filter) | TOOL-DEFECT | filter replaced by a header-row exclusion; 60/60 parsed; census pasted in REG-TASK-OWNERS §3 |
| H-2 | REG-TASK-OWNERS | US and EU tasks have no DR step or RUN in EXEC-1 (which covers AU and NZ) | SCOPE | recorded as "not in EXEC-1 RUN-0..4 (V3 / later)" rather than inventing a run; stated in §1 |
| H-3 | REG-TASK-OWNERS | `TASK-REG-014` owner role is "Operations owner" (DEPLOY-1.1 DR-4); MET-2.2 §1 names no operations owner | DECISION-PENDING | cell reads `[NEEDS DEFINITION — DEC-23 extension]`; 7 such cells in total (DEC-07, DEC-19, DEC-23 ext) |
| H-4 | REPO-MAP v3 | `cdss-compiler` has no prefix in the ratified PFX set {FAB, UIP, UIC, GPP}; Arch §14.5 cites it as EN-3/CP | ID-GAP | PFX cell reads `[PENDING-ENUMERATION]`; no prefix minted |
| H-5 | MET-5 | §13.7 cadence sentence is on Arch l.481, not l.482 as first written | CITATION | corrected before commit (sed; verified by `sed -n 481p`) |
| H-6 | GLOSSARY | census line said 37 rows; grep gave 39 (38 + header); R25 row cited Arch l.449 (a table separator) | CITATION | corrected to 38 / l.450 before commit |
| H-7 | ledger2.py | first pass read frontmatter from files it had not yet written (FileNotFoundError) | TOOL-DEFECT | guard added ("generated this pass"); fixed-point loop converges in 2–3 iterations; byte counts quoted = disk (pasted below) |
| H-8 | HARDEN-1.2 D-1 | 13 "Manifest owner" and 46 "Corpus owner" cells cannot resolve — MET-2.2 §1 names neither role | DECISION-PENDING | left as HARDEN-1.1 wrote them; counted in D-1 foot |
| H-9 | DEPLOY-1.2 | RTO/RPO targets and the L5 drill protocol are values the infrastructure owner has not given | EXECUTABLE-AFTER-INPUT | not written; MET-4.1 G-09 says "still owed" |
| H-10 | schemas.py | system python3 lacks `jsonschema`; CI installs it | TOOL-ENV | run with the sprint-1 venv interpreter; output pasted in RUN-REPORT |
| H-11 | mermaid | `.github/audit/mermaid/` has no node_modules locally (CI installs) | TOOL-ENV | sprint-1 `tools/mermaid/parse.mjs` used (mermaid 10.9.8); 22/22 PASS pasted in INDEX-09.1 §3 and raw/mermaid_parse.json |

Byte-count fixed point (ledger2.py, final run): quoted = disk for HARDEN-1.2 (76468), HARDEN-3.2 (86892), 00_inventory_v1.3.txt (24257), INDEX-09.1 (4155), GLOSSARY.md (11410).
