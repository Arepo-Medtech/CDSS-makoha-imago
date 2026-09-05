---
applyTo: "0[0-9]_*/**"
---
Every pre-existing file in these folders is retained. Changes arrive only as new files — a delta (`NAME-1.1_…_delta.md` with `applies_to`, `supersedes: nothing`, D-n rows), a companion, or a new version beside the old — plus an appended amendment in `00_MANIFEST.md`. New files carry YAML frontmatter with `doc_id`, `title`, `version`, `date`, `status` (stating what is and is NOT claimed), and `req_prefix`/`req_count` when they mint IDs, and end with an ID census and a self-audit whose outputs are pasted. Review against the four layers in `.github/copilot-instructions.md`; report with the Severity / Target Asset / Observed / Target / Remediation template.
