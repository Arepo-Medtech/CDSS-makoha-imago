#!/usr/bin/env python3
"""Validator for the four jurisdiction posture documents.
Checks: ID pattern; each ID defined exactly once (first cell of a table row, backticked);
range endpoints contiguous 000/001..max; every TASK row names a GATE; every FIND row names a SRC;
every referenced ID is defined somewhere in the same doc; shared-stack numbering alignment.
"""
import re, sys, collections

DOCS = {
    "AU": ("REG-POSTURE_v1.2.md", r"(REG-FIND|REG-KEEP|ASSUME-REG|OBL|STD|FORK-REG|GATE|TASK-REG|KTX|WATCH-REG|Q-REG|SRC-REG)"),
    "NZ": ("REG-NZ_v1.1.md", r"NZ-(FIND|OBL|STD|ASSUME|TASK|GATE|WATCH|Q|SRC)"),
    "US": ("REG-US_v1.0.md", r"US-(FIND|OBL|STD|REG|ASSUME|TASK|GATE|WATCH|Q|SRC)"),
    "EU": ("REG-EU_v1.0.md", r"EU-(FIND|OBL|STD|LAW|ASSUME|TASK|GATE|WATCH|Q|SRC)"),
}
GATE_OF = {"AU": "GATE", "NZ": "NZ-GATE", "US": "US-GATE", "EU": "EU-GATE"}
TASK_OF = {"AU": "TASK-REG", "NZ": "NZ-TASK", "US": "US-TASK", "EU": "EU-TASK"}
FIND_OF = {"AU": "REG-FIND", "NZ": "NZ-FIND", "US": "US-FIND", "EU": "EU-FIND"}
SRC_OF = {"AU": "SRC-REG", "NZ": "NZ-SRC", "US": "US-SRC", "EU": "EU-SRC"}

fail = 0
stacks = {}
for j, (fn, fam) in DOCS.items():
    text = open(fn, encoding="utf-8").read()
    idpat = re.compile(r"`(" + fam + r"-[0-9]{3})`")
    all_ids = set(m.group(1) for m in idpat.finditer(text))
    # definitions: table rows whose first cell is a backticked ID (optionally followed by bold tag)
    defs = collections.Counter()
    for line in text.splitlines():
        m = re.match(r"^\|\s*`(" + fam + r"-[0-9]{3})`\s*(\*\*\[[^\]]*\]\*\*\s*)?\|", line)
        if m:
            defs[m.group(1)] += 1
    # exclude §6.7 note rows in AU (they carry ' note' suffix so won't match) -- ok
    dup = [k for k, v in defs.items() if v > 1]
    undefined = sorted(i for i in all_ids if i not in defs)
    print(f"== {j} {fn}: {len(all_ids)} distinct IDs referenced, {len(defs)} defined")
    if dup:
        fail += 1; print("  DUP definitions:", dup)
    if undefined:
        fail += 1; print("  REFERENCED BUT UNDEFINED:", undefined)
    # families and ranges
    byfam = collections.defaultdict(list)
    for i in defs:
        f, n = i.rsplit("-", 1); byfam[f].append(int(n))
    for f, nums in sorted(byfam.items()):
        nums.sort(); lo = 0 if "GATE" in f else 1
        expect = list(range(lo, nums[-1] + 1))
        gap = sorted(set(expect) - set(nums))
        flag = "" if not gap else f"  GAP {gap}"
        if gap: fail += 1
        print(f"  {f}: {len(nums)} defined, {lo:03d}-{nums[-1]:03d}{flag}")
        if f.endswith("STD") or f == "STD":
            stacks[j] = byfam[f]
    # TASK rows name a gate; FIND rows name a SRC
    rows = collections.defaultdict(list)
    for line in text.splitlines():
        m = re.match(r"^\|\s*`(" + fam + r"-[0-9]{3})`\s*(\*\*\[[^\]]*\]\*\*\s*)?\|", line)
        if m: rows[m.group(1)].append(line)
    for i, ls in rows.items():
        if i.startswith(TASK_OF[j] + "-") and not any(GATE_OF[j] + "-" in l for l in ls):
            fail += 1; print("  TASK without gate:", i)
        if i.startswith(FIND_OF[j] + "-") and not any(SRC_OF[j] + "-" in l for l in ls):
            fail += 1; print("  FIND without source:", i)
    # standalone rule: no 'see REG-POSTURE' style deferral in non-AU docs
    if j != "AU":
        for n, line in enumerate(text.splitlines(), 1):
            if re.search(r"see REG-POSTURE|see the Australian posture for|refer to REG-POSTURE", line) and not re.search(r"REPLETE-STANDALONE|No reference|No \"see", line):
                fail += 1; print(f"  STANDALONE VIOLATION line {n}: {line[:90]}")

# shared stack alignment 001..026
base = set(range(1, 27))
for j, nums in stacks.items():
    missing = sorted(base - set(nums))
    if missing:
        fail += 1; print(f"STACK MISALIGNED {j}: missing {missing}")
print("\nRESULT:", "PASS" if fail == 0 else f"FAIL ({fail} issues)")
sys.exit(1 if fail else 0)
