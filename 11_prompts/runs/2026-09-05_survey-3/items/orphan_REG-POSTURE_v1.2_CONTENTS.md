# Orphan candidate — REG-POSTURE_v1.2_CONTENTS.md

Target: `10_regulatory-execution/REG-POSTURE_v1.2_CONTENTS.md`

- **Read:** full read of the candidate (all < 60 KB) + grep of doc_id/basename/short title across every non-index, non-ledger file
- **Eight-property lens (MT2 §1):** MT2 §1(6) cross-reference integrity: the file's own outbound references resolve (refcheck 0 dead)
- **Naive-executor read:** a naive executor opening INDEX-05/INDEX-10/PROMPT-SERIES finds the file only through the index row — TACIT: which base document it accompanies is stated in its own frontmatter (`applies_to`/`companion_to`), not in the base
- **Sibling consistency:** none (no contradicting position)
- **Delivery quality (placeholders):** no unregistered placeholders in the candidate
- **Row changes:** row QI-0011 → state OPEN; confidence 80; calibrated_weight 2
