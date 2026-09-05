# Regulatory task tables — depth read

Target: `10_regulatory-execution/REG-POSTURE_v1.2.md §7 (+ REG-NZ §8, REG-US, REG-EU)`

- **Read:** section reads (files 47–96 KB; chunk boundaries: REG-POSTURE l.868–945, l.955–970, l.1046–1120)
- **Eight-property lens (MT2 §1):** exit+evidence: §0.4 vocabulary defines DONE-WITH-EVIDENCE but the evidence artifact is not named per task
- **Naive-executor read:** TACIT: which owner role executes TASK-REG-005 (Jira) is knowable only via DEPLOY-1.1 DR-3 — a naive executor of RUN-1 would not find it in the posture
- **Sibling consistency:** REG-POSTURE §7 vs EXEC-1 RUN table: RUN-1 cites TASK-REG-005/006/007 exactly as §7 Phase 1 — consistent
- **Delivery quality (placeholders):** none
- **Row changes:** WARNING confirmed; confidence 80→85
