"""readability.py — prose-only readability per authored .md: strips YAML frontmatter, fenced code, tables, HTML comments, backtick spans, headings, list markers;
computes average sentence length (words) and Flesch–Kincaid grade = 0.39*(words/sentences) + 11.8*(syllables/words) − 15.59 (Kincaid et al. 1975).
Syllables: heuristic vowel-group count (no dictionary) — stated so the number is reproducible, not authoritative. Tool: this script, Python 3.9."""
import re, json, sys; sys.path.insert(0, __file__.rsplit('/',1)[0]); import scope
def prose(t):
    t=re.sub(r'\A---\n.*?\n---\n','',t,flags=re.S); t=re.sub(r'```.*?```','',t,flags=re.S); t=re.sub(r'<!--.*?-->','',t,flags=re.S)
    t='\n'.join(l for l in t.split('\n') if not l.lstrip().startswith('|') and not l.lstrip().startswith('#'))
    t=re.sub(r'`[^`]*`','',t); t=re.sub(r'^\s*[-*>]\s+','',t,flags=re.M); t=re.sub(r'\[([^\]]*)\]\([^)]*\)',r'\1',t); t=re.sub(r'[*_]{1,3}','',t)
    return t
def syl(w):
    w=w.lower(); w=re.sub(r'[^a-z]','',w)
    if not w: return 0
    g=len(re.findall(r'[aeiouy]+',w)); 
    if w.endswith('e') and not w.endswith(('le','ee')) and g>1: g-=1
    return max(1,g)
rows=[]
for f in scope.md_files():
    p=prose(open(f,encoding='utf-8',errors='replace').read())
    sents=[s for s in re.split(r'(?<=[.!?])\s+(?=[A-Z"“(\[])',p) if len(s.split())>=3]
    words=[w for s in sents for w in s.split()]
    if len(words)<50: rows.append({"file":f,"prose_words":len(words),"note":"<50 prose words — not scored"}); continue
    asl=len(words)/len(sents); spw=sum(syl(w) for w in words)/len(words); fk=0.39*asl+11.8*spw-15.59
    rows.append({"file":f,"prose_words":len(words),"sentences":len(sents),"avg_sentence_len":round(asl,1),"fk_grade":round(fk,1)})
scored=[r for r in rows if 'fk_grade' in r]; import statistics as st
print(json.dumps({"tool":"readability.py","formula":"FK grade = 0.39*ASL + 11.8*ASW - 15.59; prose only","files":len(rows),"scored":len(scored),
 "median_asl":round(st.median(r['avg_sentence_len'] for r in scored),1),"median_fk":round(st.median(r['fk_grade'] for r in scored),1),
 "thresholds_[ASSESSOR-PROPOSED]":{"asl_max":35,"fk_max":14},
 "rows":sorted(rows,key=lambda r:-r.get('avg_sentence_len',0))},indent=1))
