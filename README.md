# dw-examples

Prebuilt [draftwright](https://github.com/pzfreo/draftwright) drawings for standard STEP
files. Every drawing here is produced by the stock `draftwright` CLI — no custom scripts,
no hand edits, no post-processing. The only thing that varies between drawings is the CLI
arguments, and those live in [`drawings.toml`](drawings.toml).

The repo starts with the five CTC parts from the NIST MBE PMI Validation and Conformance
Testing Project.

## Drawings

| Drawing | STEP input | PDF |
| --- | --- | --- |
| NIST CTC-01 | [`nist_ctc_01_asme1_ap242.stp`](steps/nist/nist_ctc_01_asme1_ap242.stp) | [`drawings/nist-ctc-01/nist-ctc-01.pdf`](drawings/nist-ctc-01/nist-ctc-01.pdf) |
| NIST CTC-02 | [`nist_ctc_02_asme1_ap242.stp`](steps/nist/nist_ctc_02_asme1_ap242.stp) | [`drawings/nist-ctc-02/nist-ctc-02.pdf`](drawings/nist-ctc-02/nist-ctc-02.pdf) |
| NIST CTC-03 | [`nist_ctc_03_asme1_ap242.stp`](steps/nist/nist_ctc_03_asme1_ap242.stp) | [`drawings/nist-ctc-03/nist-ctc-03.pdf`](drawings/nist-ctc-03/nist-ctc-03.pdf) |
| NIST CTC-04 | [`nist_ctc_04_asme1_ap242.stp`](steps/nist/nist_ctc_04_asme1_ap242.stp) | [`drawings/nist-ctc-04/nist-ctc-04.pdf`](drawings/nist-ctc-04/nist-ctc-04.pdf) |
| NIST CTC-05 | [`nist_ctc_05_asme1_ap242.stp`](steps/nist/nist_ctc_05_asme1_ap242.stp) | [`drawings/nist-ctc-05/nist-ctc-05.pdf`](drawings/nist-ctc-05/nist-ctc-05.pdf) |

Each drawing directory also holds the `.draftwright.json` report the CLI writes beside the
PDF. [`drawings/index.json`](drawings/index.json) records the draftwright version that
built the current set, the exact arguments used for each drawing, and that drawing's
headline lint numbers (status, score, error/warning counts) — so a version bump that
degrades a drawing shows up as a diff in one small file, not just as a changed PDF.

## How a drawing is defined

```toml
args = ["--format", "pdf", "--no-progress"]   # prepended to every drawing

[[drawing]]
name = "nist-ctc-01"
step = "steps/nist/nist_ctc_01_asme1_ap242.stp"
args = ["--title", "NIST CTC-01", "--number", "NIST-CTC-01"]
```

`build.py` runs `draftwright <step> --out drawings/<name>/<name> <shared args> <drawing args>`
and nothing else. To add a drawing: drop the STEP file under `steps/`, add an entry, and
run the build. To change how a drawing looks, change its arguments — `draftwright --help`
lists them all.

## Building locally

```
uv sync --frozen          # installs the pinned draftwright
uv run python build.py    # rebuild everything
uv run python build.py nist-ctc-03   # rebuild one drawing
uv run python build.py --list
```

Python is pinned to 3.12 and `draftwright` to an exact version in
[`pyproject.toml`](pyproject.toml), so a checkout reproduces the committed PDFs.

## Staying current with draftwright

1. Dependabot watches the exact `draftwright==` pin daily and opens a PR for each release.
2. The `Drawings` workflow builds all five drawings on that PR — a failure there is the
   alert that a release changed something that matters.
3. Merging the PR runs the same workflow on `main`, which rebuilds the drawings and commits
   the regenerated PDFs, so `drawings/` always reflects the pinned version.

Dependabot-triggered workflows get a read-only token, so the rebuilt PDFs are committed on
the post-merge `main` run rather than pushed into the Dependabot branch. The workflow can
also be started by hand from the Actions tab.

## Licensing

The NIST CTC STEP files are works of the U.S. federal government and are not subject to
copyright in the United States; see [`steps/nist/README.md`](steps/nist/README.md).
draftwright itself is AGPL-3.0.
