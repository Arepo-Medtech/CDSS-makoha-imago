# 05_registers-and-contracts — FIRST REQUIREMENTS (queue order)

1. `[5] [P-D-14] [DECISION]` Homes and owners of every 05_ artifact depend on DEC-02 + DEC-09 (BSQ-0209) — evidence: pointer stub "On DEC-02+DEC-09 ratification the draft MOVES here"; MET-2 both Open — blocks: W1; L1 register check; code freeze — remedy: **HUMAN-ONLY: DEC-02 (Architecture owner), DEC-09 (Programme lead [NEEDS DEFINITION])**.
2. `[4] [P-D-09] [SCHEMA]` No JSON Schema for GenericArgument/ActualArgument/Deviation; no RRI test spec (BSQ-0205) — evidence: one .md contract file; CC-7 requires "jsonschema validation runs" — blocks: W1 T-001..003; PROMPT-A/E/F L1 exits — remedy: write `CONTRACT-ARG-1.schema.json`, `CONTRACT-DEV-1.schema.json`, `CONTRACT-RRI-1_render-invariance_test-spec.md` with ≥2 example instances each and recorded validator output.
3. `[4] [P-D-08] [REGISTER]` R30 has no JSON Schema and no row-form seed (BSQ-0202) — evidence: `ls 05_* | grep -i r30` → two .md; CC-4 check "R30 schema validation" unrunnable — blocks: W1 T-005, W3 T-021, RUN-0 exit row (EX-10) — remedy: write `REG-R30.schema.json` + `REG-R30.2_row-form_seed.jsonl` (crosswalked status + `source_status_verbatim`; ASSUME rows stay OPEN).
4. `[3] [P-F-02] [INDEX]` No folder index/briefing (BSQ-0201) — remedy: write `05_registers-and-contracts/INDEX.md` (briefing §, file table with doc_ids carried, HARDEN row/task, skeleton home, DEC gate, reading rule R30→R30.1, honesty, self-audit).
5. `[3] [P-F-08] [SEED]` REG-R30.1 has no HARDEN-1 row and no HARDEN-3 task (BSQ-0203, BSQ-0204) — remedy: rows/tasks added in HARDEN-1.1 / HARDEN-3.1 (04_ queue items).
6. `[3] [P-D-09] [SCHEMA]` REG-R29.schema.json has no example instance; md twin omits `blocker` (BSQ-0206) — remedy: `REG-R29.examples.jsonl` + `REG-R29.1_schema_twin_delta.md` with recorded validation.
7. `[3] [P-D-10] [SEED]` R30/R30.1 statuses are verbatim source words, not the declared enum; 'standing'/cadences have no crosswalk value (BSQ-0208) — remedy: **EXECUTABLE-AFTER-DECISION** — regulatory owner rules the mapping; then normalise in the row-form seed (item 3).

Dismissed: BSQ-0210 (per-schema pointer stubs — README suffices until DEC-02).

Folder parity verdict (provisional): **BELOW-PARITY** — P-D-01 FAIL ×3 (version/date), P-D-08/09 ABSENT ×5, P-D-10 FAIL ×2; chain: INDEX/BRIEFING ABSENT, SKELETON PARTIAL, HARDEN coverage PARTIAL.
