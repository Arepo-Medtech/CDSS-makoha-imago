"""style_census.py — per HTML page: distinct hex colours, px/rem values, font-family declarations, media queries; cross-page intersection = implied token set."""
import re, json, sys, os, collections; sys.path.insert(0, __file__.rsplit('/',1)[0]); import scope
pages = scope.html_files(); rows=[]; colour_pages=collections.Counter(); size_pages=collections.Counter(); font_pages=collections.Counter()
for p in pages:
    t=open(p,encoding='utf-8',errors='replace').read()
    hexes=set(h.lower() for h in re.findall(r'#(?:[0-9a-fA-F]{3}){1,2}\b',t))
    sizes=set(re.findall(r'\b\d*\.?\d+(?:px|rem)\b',t))
    fonts=set(m.strip().split(',')[0].strip('\'" ') for m in re.findall(r'font-family\s*:\s*([^;}{]+)',t))
    mq=len(re.findall(r'@media',t)); ext=len(re.findall(r'<link[^>]+rel=["\']stylesheet',t)); styleblocks=len(re.findall(r'<style',t))
    rows.append({"page":p,"bytes":os.path.getsize(p),"hex_colours":len(hexes),"px_rem_values":len(sizes),"font_families":sorted(fonts),"media_queries":mq,"external_stylesheets":ext,"style_blocks":styleblocks,"hex_list":sorted(hexes)})
    for h in hexes: colour_pages[h]+=1
    for s in sizes: size_pages[s]+=1
    for f in fonts: font_pages[f]+=1
N=len(pages); k=max(1,round(N*0.4))  # implied token = used by >= 40% of pages [ASSESSOR-PROPOSED]
implied={"threshold_pages":k,"colours":sorted([h for h,c in colour_pages.items() if c>=k]),"sizes":sorted([s for s,c in size_pages.items() if c>=k],key=lambda x:float(re.match(r'[\d.]+',x).group())),"fonts":[f for f,c in font_pages.items() if c>=k]}
for r in rows: r["drift_colours_not_in_implied"]=len([h for h in r["hex_list"] if h not in implied["colours"]]); del r["hex_list"]
print(json.dumps({"tool":"style_census.py","pages":N,"rows":rows,"implied_token_set":implied},indent=1))
