"""An AI-style loop on a Draftwright Spec: review, apply the review's own fixes that move a
dimension, repeat until they change nothing, or bring back a Spec already tried (the
review's fixes can undo each other), or the round limit.

Usage: review_loop.py <draftwright> <step> <spec.json> <rounds>  (the Spec is updated in place)

Fixes that change the sheet (``sheet/``, ``sheets/``: size, scale, sheet count) are left out:
taken blindly they shrink the part (1:2 on A4 for the mounting plate). Set the sheet yourself.
"""
import json, subprocess, sys
from collections import Counter

dw, step, path, rounds = sys.argv[1], sys.argv[2], sys.argv[3], int(sys.argv[4])


def put(doc, pointer, value):
    keys = [k.replace("~1", "/").replace("~0", "~") for k in pointer.strip("/").split("/")]
    for k in keys[:-1]:
        doc = doc.setdefault(k, {})
    doc[keys[-1]] = value


def review():
    run = subprocess.run([dw, "review", step, "--spec", path], capture_output=True, text=True)
    out = json.loads(run.stdout or "{}")
    if "error" in out:
        raise SystemExit(f"review failed: {out['error']}")
    return out.get("problems", []) + out.get("lint", [])


seen = [json.load(open(path))]
for n in range(rounds + 1):
    found = review()
    print(f"round {n}: {dict(Counter(f['code'] for f in found))}")
    fixes = [op for f in found for op in (f.get("fix") or [])
             if isinstance(op, dict) and op.get("op") == "set" and "path" in op
             and not op["path"].startswith(("sheet/", "sheets/"))]
    if n == rounds or not fixes:
        break
    before = json.load(open(path))
    spec = json.loads(json.dumps(before))
    for op in fixes:
        put(spec, op["path"], op["value"])
    if spec == before:
        print("the review's fixes change nothing: stopping")
        break
    if spec in seen:
        print("the review's fixes bring back a Spec already tried: stopping")
        break
    seen.append(spec)
    json.dump(spec, open(path, "w"), indent=1)
    open(path, "a").write("\n")
