#!/usr/bin/env python3
"""Rebuild the drawings and assembly packs listed in drawings.toml.

Each manifest entry is a STEP file plus its title block; nothing else is applied. For each
drawing this writes a minimal Spec holding the title block, then runs the stock
`draftwright render` (the PDF) and `draftwright review` (problems and lint) on it.
Packs use `draftwright pack` with only the GA title block set.
Run with no arguments to rebuild everything, or name entries to rebuild a subset.
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
PACK_SPEC_SCHEMA = "draftwright.pack-spec/1"


def load_manifest(path: Path) -> dict:
    data = tomllib.loads(path.read_text())
    names = [d["name"] for kind in ("drawing", "pack") for d in data.get(kind, [])]
    duplicates = {n for n in names if names.count(n) > 1}
    if duplicates:
        raise SystemExit(f"duplicate drawing/pack names in {path.name}: {sorted(duplicates)}")
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


def pack_summary(report: dict) -> dict:
    """Count groups, not quantities; include row errors alongside severity findings."""
    rows = report.get("rows", [])
    findings = list(report.get("findings", []))
    findings.extend(report.get("general_assembly", {}).get("problems", []))
    for row in rows:
        findings.extend(row.get("problems", []))
    severity = Counter(f.get("severity") for f in findings)
    failed_parts = sum(row.get("error") is not None for row in rows)
    return {
        "groups": len(rows),
        "made": sum(row.get("supply") == "make" for row in rows),
        "bought": sum(row.get("supply") == "buy" for row in rows),
        "sheets": report.get("pages", 0),
        "failed_parts": failed_parts,
        "ga_failed": any(f.get("code") == "pack_ga_failed" for f in findings),
        "errors": severity["error"] + failed_parts,
        "warnings": severity["warning"],
        "infos": severity["info"],
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
    kind = entry["kind"]
    step = ROOT / entry["step"]
    if not step.is_file():
        raise SystemExit(f"{name}: missing STEP file {entry['step']}")
    out_dir = out_root / name
    if out_dir.exists():
        shutil.rmtree(out_dir)
    out_dir.mkdir(parents=True)
    spec = out_dir / f"{name}.{kind}.json"
    intent = spec_for(entry)
    if kind == "pack":
        intent = {"schema": PACK_SPEC_SCHEMA, "ga": {"drawing": intent}}
    spec.write_text(json.dumps(intent, indent=2) + "\n")

    print(f"==> {name}: {entry['step']}", flush=True)
    record = {"kind": kind, "name": name, "step": entry["step"], "title": entry.get("title")}
    if kind == "pack":
        completed, _ = run_json(
            [cli, "pack", str(step), "--spec", str(spec), "-o", str(out_dir),
             "--formats", "pdf,csv,json"]
        )
        # Keep every surviving output, even when the CLI or an individual sheet fails.
        for source, target in (("pack.pdf", f"{name}.pdf"),
                               ("pack.csv", f"{name}.csv"),
                               ("pack.json", f"{name}.report.json")):
            path = out_dir / source
            if path.is_file():
                path.rename(out_dir / target)
            elif completed:
                print(f"    pack failed: missing {source}")
                completed = False
        report_path = out_dir / f"{name}.report.json"
        if report_path.is_file():
            report = json.loads(report_path.read_text())
            record["pack"] = pack_summary(report)
            for row in report.get("rows", []):
                if row.get("error") is not None:
                    print(f"    failed part {row['key']}: {json.dumps(row['error'])}")
            for finding in report.get("findings", []):
                if finding.get("code") == "pack_ga_failed":
                    print(f"    failed GA: {finding['message']}")
        record["files"] = sorted(p.name for p in out_dir.iterdir())
        record["ok"] = completed
        return record

    rendered, _ = run_json(
        [cli, "render", str(step), "--spec", str(spec), "-o", str(out_dir / name),
         "--formats", ",".join(formats)]
    )
    reviewed, review = run_json([cli, "review", str(step), "--spec", str(spec)])
    if reviewed:
        review.pop("svg", None)  # the drawing itself is the PDF beside it
        (out_dir / f"{name}.review.json").write_text(json.dumps(review, indent=1) + "\n")
        record["review"] = review_summary(review)
    record["files"] = sorted(p.name for p in out_dir.iterdir())
    record["ok"] = rendered and reviewed
    return record


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("names", nargs="*", help="drawings or packs to build (default: all)")
    parser.add_argument("--manifest", type=Path, default=MANIFEST)
    parser.add_argument("--out-root", type=Path, default=OUT_ROOT)
    parser.add_argument("--cli", default="draftwright", help="draftwright executable")
    parser.add_argument("--list", action="store_true", help="list drawing and pack names and exit")
    opts = parser.parse_args()

    manifest = load_manifest(opts.manifest)
    drawings = [dict(entry, kind=kind) for kind in ("drawing", "pack")
                for entry in manifest.get(kind, [])]
    formats = list(manifest.get("formats", ["pdf"]))
    if opts.list:
        for entry in drawings:
            print(entry["name"])
        return 0

    if opts.names:
        known = {entry["name"] for entry in drawings}
        unknown = sorted(set(opts.names) - known)
        if unknown:
            raise SystemExit(f"unknown drawing(s) or pack(s): {unknown}; known: {sorted(known)}")
        drawings = [entry for entry in drawings if entry["name"] in opts.names]

    version = manifest["draftwright"]
    print(f"draftwright {version}: building {len(drawings)} drawing(s)/pack(s)", flush=True)
    results = [build(entry, formats, opts.cli, opts.out_root) for entry in drawings]

    index_path = opts.out_root / "index.json"
    index = {"draftwright": version, "drawings": []}
    if index_path.is_file() and opts.names:
        # A partial rebuild keeps the entries it did not touch.
        previous = json.loads(index_path.read_text())
        rebuilt = {r["name"] for r in results}
        index["drawings"] = [d for d in previous.get("drawings", []) if d["name"] not in rebuilt]
        for record in index["drawings"]:
            record.setdefault("kind", "drawing")  # indexes written before packs existed
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
        if "pack" in r:
            summary = r["pack"]
            detail = (f", {summary['groups']} groups ({summary['made']} made/{summary['bought']} bought), "
                      f"{summary['sheets']} sheets, {summary['failed_parts']} failed parts, "
                      f"GA {'failed' if summary['ga_failed'] else 'ok'}, "
                      f"{summary['errors']}E/{summary['warnings']}W/{summary['infos']}I")
        print(f"{'ok  ' if r['ok'] else 'FAIL'} {r['name']}: {len(r['files'])} file(s){detail}")
    if failed:
        print(f"failed: {', '.join(failed)}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
