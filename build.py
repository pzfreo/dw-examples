#!/usr/bin/env python3
"""Rebuild the drawings listed in drawings.toml with the installed draftwright CLI.

Each manifest entry is a STEP file plus CLI arguments; nothing else is applied.
Run with no arguments to rebuild everything, or name drawings to rebuild a subset.
"""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parent
MANIFEST = ROOT / "drawings.toml"
OUT_ROOT = ROOT / "drawings"


def load_manifest(path: Path) -> tuple[list[str], list[dict]]:
    data = tomllib.loads(path.read_text())
    common = list(data.get("args", []))
    drawings = data.get("drawing", [])
    names = [d["name"] for d in drawings]
    duplicates = {n for n in names if names.count(n) > 1}
    if duplicates:
        raise SystemExit(f"duplicate drawing names in {path.name}: {sorted(duplicates)}")
    return common, drawings


def draftwright_version(cli: str) -> str:
    out = subprocess.run([cli, "--version"], capture_output=True, text=True, check=True)
    return out.stdout.strip().split()[-1]


def report_summary(out_dir: Path, name: str) -> dict | None:
    """Pull the headline lint numbers out of the CLI's JSON sidecar, if it wrote one."""
    sidecar = out_dir / f"{name}.draftwright.json"
    if not sidecar.is_file():
        return None
    try:
        report = json.loads(sidecar.read_text())
        lint = report["lint"]
    except (json.JSONDecodeError, KeyError, OSError):
        return None
    return {
        "status": report.get("status"),
        "passed": lint.get("passed"),
        "score": round(float(lint["score"]), 4) if lint.get("score") is not None else None,
        "errors": lint.get("errors"),
        "warnings": lint.get("warnings"),
        "infos": lint.get("infos"),
    }


def build(entry: dict, common: list[str], cli: str, out_root: Path) -> dict:
    name = entry["name"]
    step = ROOT / entry["step"]
    if not step.is_file():
        raise SystemExit(f"{name}: missing STEP file {entry['step']}")
    out_dir = out_root / name
    if out_dir.exists():
        shutil.rmtree(out_dir)
    out_dir.mkdir(parents=True)
    args = common + list(entry.get("args", []))
    cmd = [cli, str(step), "--out", str(out_dir / name), *args]
    print(f"==> {name}: {' '.join(cmd[1:])}", flush=True)
    result = subprocess.run(cmd)
    files = sorted(p.name for p in out_dir.iterdir()) if out_dir.exists() else []
    record = {
        "name": name,
        "step": entry["step"],
        "args": args,
        "files": files,
        "ok": result.returncode == 0,
    }
    summary = report_summary(out_dir, name)
    if summary is not None:
        # Recorded so a draftwright bump shows any quality regression as an index.json diff.
        record["report"] = summary
    return record


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("names", nargs="*", help="drawings to build (default: all)")
    parser.add_argument("--manifest", type=Path, default=MANIFEST)
    parser.add_argument("--out-root", type=Path, default=OUT_ROOT)
    parser.add_argument("--cli", default="draftwright", help="draftwright executable")
    parser.add_argument("--list", action="store_true", help="list drawing names and exit")
    opts = parser.parse_args()

    common, drawings = load_manifest(opts.manifest)
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

    version = draftwright_version(opts.cli)
    print(f"draftwright {version}: building {len(drawings)} drawing(s)", flush=True)

    results = [build(entry, common, opts.cli, opts.out_root) for entry in drawings]

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
        summary = r.get("report") or {}
        detail = ""
        if summary:
            detail = (
                f", lint {summary['errors']}E/{summary['warnings']}W"
                f" score {summary['score']}"
            )
        print(f"{'ok  ' if r['ok'] else 'FAIL'} {r['name']}: {len(r['files'])} file(s){detail}")
    if failed:
        print(f"failed: {', '.join(failed)}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
