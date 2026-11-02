"""An AI-style loop on a Draftwright spec: review, apply the review's own fix ops, repeat.

Usage: loop.py <draftwright> <step> <spec.json> <rounds>  (the spec is updated in place)
"""
import json, subprocess, sys
from collections import Counter

dw, step, path, rounds = sys.argv[1], sys.argv[2], sys.argv[3], int(sys.argv[4])

def put(doc, pointer, value):
    keys = [k.replace("~1", "/").replace("~0", "~") for k in pointer.split("/")]
    for k in keys[:-1]:
        doc = doc.setdefault(k, {})
    doc[keys[-1]] = value

for n in range(rounds + 1):
    review = json.loads(subprocess.run([dw, "review", step, "--spec", path], capture_output=True, text=True).stdout)
    found = review.get("problems", []) + review.get("lint", [])
    print(f"round {n}: {dict(Counter(f['code'] for f in found))}")
    # Judgement: take a fix that moves a dimension; leave the sheet (size, scale) as it is.
    fixes = [op for f in found for op in (f.get("fix") or []) if isinstance(op, dict) and not op["path"].startswith("sheet/")]
    if n == rounds or not fixes:
        break
    spec = json.load(open(path))
    for op in fixes:
        if op.get("op") == "set":
            put(spec, op["path"], op["value"])
    json.dump(spec, open(path, "w"), indent=1)
