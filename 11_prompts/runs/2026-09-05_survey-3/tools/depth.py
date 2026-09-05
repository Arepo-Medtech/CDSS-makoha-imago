"""depth.py — directory depth census over in-scope files. Threshold 4 (architect's; v1.0 Layer 1)."""
import json, sys, collections; sys.path.insert(0, __file__.rsplit('/',1)[0]); import scope
fs = scope.files(); hist = collections.Counter(f.count('/') for f in fs)
over = [f for f in fs if f.count('/') > 4]
print(json.dumps({"tool":"depth.py","files":len(fs),"histogram":{str(k):hist[k] for k in sorted(hist)},"threshold":4,"exceeding":over,"at_threshold":[f for f in fs if f.count('/')==4][:5]+(["…"] if hist[4]>5 else [])},indent=1))
