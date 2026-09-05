#!/usr/bin/env python3
"""Sprint-2 seal: refresh byte quotes in A-010 and RUN-REPORT §3 from 00_inventory_v1.3.txt, write CHECKSUMS_AFTER/CHANGED, paste the proof into RUN-REPORT §5. Run after tools/ledger2.py has reached its fixed point. No shell."""
import re, os, hashlib, subprocess
R='11_prompts/runs/2026-09-05_sprint-2'
inv={l.split(' ',1)[1].strip():int(l.split(' ',1)[0]) for l in open('00_inventory_v1.3.txt') if not l.startswith('#')}
m='00_MANIFEST.md'; s=open(m,encoding='utf-8').read(); i=s.index('# 16. Amendment A-010'); base,a=s[:i],s[i:]
def fix(mm):
    name=mm.group(1); c=[p for p in inv if p.endswith('/'+name) or p==name]
    return f'`{name}` ({inv[c[0]]:,})' if len(c)==1 else mm.group(0)
a=re.sub(r'`([^`/]+)` \((\d[\d,]*)\)',fix,a); a=re.sub(r'`tokens\.css` \((\d[\d,]*):',lambda mm:f'`tokens.css` ({inv["09_diagrams/tokens.css"]:,}:',a)
open(m,'w',encoding='utf-8').write(base+a)
rep=open(R+'/RUN-REPORT.md',encoding='utf-8').read()
newfiles=[l.split('\t')[1] for l in subprocess.check_output(['git','diff','--name-status','--cached','origin/main']).decode().split('\n') if l.startswith('A\t') and not l.split('\t')[1].startswith('11_prompts/runs/')]
files='\n'.join(f'| `{p}` | {inv[p]:,} |' for p in newfiles)
rep=re.sub(r'(\| path \| bytes \|\n\|---\|---\|\n)(?:\| `[^\n]*\n)+', lambda mm: mm.group(1)+files+'\n', rep)
rep=re.sub(r'`09_diagrams/tokens\.css` \(\d+ B:',f'`09_diagrams/tokens.css` ({inv["09_diagrams/tokens.css"]} B:',rep)
# checksums
out=[]
for root,dirs,fs in os.walk('.'):
    dirs[:]=[d for d in dirs if d not in ('.git','node_modules','.venv') and not (root=='./11_prompts/runs' and d=='2026-09-05_sprint-2') and not root.endswith('/tools') or d!='mermaid']
    for f in fs:
        p=os.path.join(root,f)
        if f=='.DS_Store' or p.startswith('./'+R) or '/node_modules/' in p or '/.venv/' in p or '/tools/mermaid/' in p: continue
        out.append((p,hashlib.sha256(open(p,'rb').read()).hexdigest()))
out.sort(); open(R+'/CHECKSUMS_AFTER.txt','w').write(''.join(f'{h}  {p}\n' for p,h in out))
b={l.split('  ',1)[1].strip():l.split('  ',1)[0] for l in open(R+'/CHECKSUMS_BEFORE.txt')}; a2=dict((p,h) for p,h in out)
changed=[p for p in b if p in a2 and a2[p]!=b[p]]; removed=[p for p in b if p not in a2]; added=[p for p in a2 if p not in b]
basem=subprocess.run(['git','show','origin/main:00_MANIFEST.md'],capture_output=True).stdout; head=open('00_MANIFEST.md','rb').read()
proof=f"CHECKSUMS_BEFORE.txt: {len(b)} files (main 21b9675, before any write)\nCHECKSUMS_AFTER.txt:  {len(a2)} files\npre-existing files whose hash changed: {len(changed)}\n"+''.join(f"< {b[p]}  {p}\n" for p in changed)+f"pre-existing files removed: {len(removed)} {removed}\nfiles added (outside this run directory): {len(added)}\n00_MANIFEST.md prefix check: head.startswith(main:00_MANIFEST.md) = {head.startswith(basem)}; appended {len(head)-len(basem)} bytes; sha256(main:00_MANIFEST.md) = {hashlib.sha256(basem).hexdigest()}\nREADME.md, AGENTS.md: root governance files outside the 00_–11_ law; README +1 table row, AGENTS.md one 'How work lands' sentence (H-12)"
open(R+'/CHECKSUMS_CHANGED.txt','w').write(proof)
rep=re.sub(r'```\nCHECKSUMS_BEFORE\.txt:.*?\n```',lambda mm:'```\n'+proof+'\n```',rep,flags=re.S); open(R+'/RUN-REPORT.md','w',encoding='utf-8').write(rep)
print(proof)
