#!/usr/bin/env python3
"""Rebuild the drawings listed in drawings.toml with the installed draftwright CLI.

Each manifest entry is a STEP file plus its title block; nothing else is applied. For each
drawing this writes a minimal Spec holding the title block, then runs the stock
`draftwright render` (the PDF) and `draftwright review` (problems and lint) on it.
Run with no arguments to rebuild everything, or name drawings to rebuild a subset.
"""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
import tomllib
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent
MANIFEST = ROOT / "drawings.toml"
OUT_ROOT = ROOT / "drawings"
SPEC_SCHEMA = "draftwright.spec/2"


def load_manifest(path: Path) -> dict:
    data = tomllib.loads(path.read_text())
    names = [d["name"] for d in data.get("drawing", [])]
    duplicates = {n for n in names if names.count(n) > 1}
    if duplicates:
        raise SystemExit(f"duplicate drawing names in {path.name}: {sorted(duplicates)}")
    if "draftwright" not in data:
        raise SystemExit(f"{path.name} must name the draftwright release tag")
    return data


def spec_for(entry: dict) -> dict:
    title = {k: entry[k] for k in ("title", "number") if k in entry}
    return {"schema": SPEC_SCHEMA, "sheet": {"title": title}}


def review_summary(review: dict) -> dict:
    """The headline numbers of a review, so a draftwright bump shows up as an index.json diff."""
    findings = review.get("problems", []) + review.get("lint", [])
    severity = Counter(f.get("severity") for f in findings)
    impacts = {k: v["findings"] for k, v in review.get("summary", {}).get("impacts", {}).items()}
    return {
        "errors": severity["error"],
        "warnings": severity["warning"],
        "infos": severity["info"],
        "impacts": dict(sorted(impacts.items())),
    }


def run_json(cmd: list[str]) -> tuple[bool, dict]:
    result = subprocess.run(cmd, capture_output=True, text=True)
    try:
        doc = json.loads(result.stdout) if result.stdout.strip() else {}
    except json.JSONDecodeError:
        doc = {}
    ok = result.returncode == 0 and doc.get("ok", True) is not False
    if not ok:
        error = doc.get("error") or result.stderr.strip() or f"exit {result.returncode}"
        print(f"    {cmd[1]} failed: {json.dumps(error) if isinstance(error, dict) else error}")
    return ok, doc


def build(entry: dict, formats: list[str], cli: str, out_root: Path) -> dict:
    name = entry["name"]
    step = ROOT / entry["step"]
    if not step.is_file():
        raise SystemExit(f"{name}: missing STEP file {entry['step']}")
    out_dir = out_root / name
    if out_dir.exists():
        shutil.rmtree(out_dir)
    out_dir.mkdir(parents=True)
    spec = out_dir / f"{name}.drawing.json"
    spec.write_text(json.dumps(spec_for(entry), indent=2) + "\n")

    print(f"==> {name}: {entry['step']}", flush=True)
    rendered, _ = run_json(
        [cli, "render", str(step), "--spec", str(spec), "-o", str(out_dir / name),
         "--formats", ",".join(formats)]
    )
    reviewed, review = run_json([cli, "review", str(step), "--spec", str(spec)])
    record = {"name": name, "step": entry["step"], "title": entry.get("title")}
    if reviewed:
        review.pop("svg", None)  # the drawing itself is the PDF beside it
        (out_dir / f"{name}.review.json").write_text(json.dumps(review, indent=1) + "\n")
        record["review"] = review_summary(review)
    record["files"] = sorted(p.name for p in out_dir.iterdir())
    record["ok"] = rendered and reviewed
    return record


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("names", nargs="*", help="drawings to build (default: all)")
    parser.add_argument("--manifest", type=Path, default=MANIFEST)
    parser.add_argument("--out-root", type=Path, default=OUT_ROOT)
    parser.add_argument("--cli", default="draftwright", help="draftwright executable")
    parser.add_argument("--list", action="store_true", help="list drawing names and exit")
    opts = parser.parse_args()

    manifest = load_manifest(opts.manifest)
    drawings = manifest.get("drawing", [])
    formats = list(manifest.get("formats", ["pdf"]))
    if opts.list:
        for entry in drawings:
            print(entry["name"])
        return 0

    if opts.names:
        known = {entry["name"] for entry in drawings}
        unknown = sorted(set(opts.names) - known)
        if unknown:
            raise SystemExit(f"unknown drawing(s): {unknown}; known: {sorted(known)}")
        drawings = [entry for entry in drawings if entry["name"] in opts.names]

    version = manifest["draftwright"]
    print(f"draftwright {version}: building {len(drawings)} drawing(s)", flush=True)
    results = [build(entry, formats, opts.cli, opts.out_root) for entry in drawings]

    index_path = opts.out_root / "index.json"
    index = {"draftwright": version, "drawings": []}
    if index_path.is_file() and opts.names:
        # A partial rebuild keeps the entries it did not touch.
        previous = json.loads(index_path.read_text())
        rebuilt = {r["name"] for r in results}
        index["drawings"] = [d for d in previous.get("drawings", []) if d["name"] not in rebuilt]
    index["drawings"] = sorted(
        index["drawings"] + [{k: v for k, v in r.items() if k != "ok"} for r in results],
        key=lambda d: d["name"],
    )
    opts.out_root.mkdir(parents=True, exist_ok=True)
    index_path.write_text(json.dumps(index, indent=2) + "\n")

    failed = [r["name"] for r in results if not r["ok"]]
    for r in results:
        summary = r.get("review")
        detail = f", review {summary['errors']}E/{summary['warnings']}W/{summary['infos']}I" if summary else ""
        print(f"{'ok  ' if r['ok'] else 'FAIL'} {r['name']}: {len(r['files'])} file(s){detail}")
    if failed:
        print(f"failed: {', '.join(failed)}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
