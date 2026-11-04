# dw-examples

Prebuilt [draftwright](https://github.com/pzfreo/draftwright-rust) drawings and assembly packs
for public STEP files. Every drawing here is produced by the stock `draftwright` CLI from
[draftwright-rust](https://github.com/pzfreo/draftwright-rust): no custom scripts, no hand edits,
no post-processing. Most drawings set only a title block, in [`drawings.toml`](drawings.toml).
The [AI best-effort drawings](#ai-best-effort-drawings) also use a Spec from [`specs/`](specs/README.md).

The current set is built by draftwright **v0.2.9**. The drawings are unreviewed output, shown
as draftwright draws them, including its mistakes: features are recognised automatically and
some are missed or misread. Each drawing's `.review.json` lists the problems draftwright found
in it; each assembly pack has a `.report.json` with per-part findings and failures.

## Drawings

53 drawings and three assembly packs from six sources: 44 baselines, listed below, and nine
[AI best-effort versions](#ai-best-effort-drawings) of the text-to-cad parts. See [Licensing](#licensing) for where
each STEP file comes from and the terms it is shared under.

### NIST MBE PMI test parts (AP242 with semantic PMI)

| Drawing | STEP input | PDF |
| --- | --- | --- |
| NIST CTC-01 | [`nist_ctc_01_asme1_ap242.stp`](steps/nist/nist_ctc_01_asme1_ap242.stp) | [`nist-ctc-01.pdf`](drawings/nist-ctc-01/nist-ctc-01.pdf) |
| NIST CTC-02 | [`nist_ctc_02_asme1_ap242.stp`](steps/nist/nist_ctc_02_asme1_ap242.stp) | [`nist-ctc-02.pdf`](drawings/nist-ctc-02/nist-ctc-02.pdf) |
| NIST CTC-03 | [`nist_ctc_03_asme1_ap242.stp`](steps/nist/nist_ctc_03_asme1_ap242.stp) | [`nist-ctc-03.pdf`](drawings/nist-ctc-03/nist-ctc-03.pdf) |
| NIST CTC-04 | [`nist_ctc_04_asme1_ap242.stp`](steps/nist/nist_ctc_04_asme1_ap242.stp) | [`nist-ctc-04.pdf`](drawings/nist-ctc-04/nist-ctc-04.pdf) |
| NIST CTC-05 | [`nist_ctc_05_asme1_ap242.stp`](steps/nist/nist_ctc_05_asme1_ap242.stp) | [`nist-ctc-05.pdf`](drawings/nist-ctc-05/nist-ctc-05.pdf) |
| NIST FTC-06 | [`nist_ftc_06_asme1_ap242-e2.stp`](steps/nist/nist_ftc_06_asme1_ap242-e2.stp) | [`nist-ftc-06.pdf`](drawings/nist-ftc-06/nist-ftc-06.pdf) |
| NIST FTC-07 | [`nist_ftc_07_asme1_ap242-e2.stp`](steps/nist/nist_ftc_07_asme1_ap242-e2.stp) | [`nist-ftc-07.pdf`](drawings/nist-ftc-07/nist-ftc-07.pdf) |
| NIST FTC-08 | [`nist_ftc_08_asme1_ap242-e2.stp`](steps/nist/nist_ftc_08_asme1_ap242-e2.stp) | [`nist-ftc-08.pdf`](drawings/nist-ftc-08/nist-ftc-08.pdf) |
| NIST FTC-10 | [`nist_ftc_10_asme1_ap242-e2.stp`](steps/nist/nist_ftc_10_asme1_ap242-e2.stp) | [`nist-ftc-10.pdf`](drawings/nist-ftc-10/nist-ftc-10.pdf) |
| NIST FTC-11 | [`nist_ftc_11_asme1_ap242-e3.stp`](steps/nist/nist_ftc_11_asme1_ap242-e3.stp) | [`nist-ftc-11.pdf`](drawings/nist-ftc-11/nist-ftc-11.pdf) |
| NIST STC-06 | [`nist_stc_06_asme1_ap242-e3.stp`](steps/nist/nist_stc_06_asme1_ap242-e3.stp) | [`nist-stc-06.pdf`](drawings/nist-stc-06/nist-stc-06.pdf) |
| NIST STC-07 | [`nist_stc_07_asme1_ap242-e3.stp`](steps/nist/nist_stc_07_asme1_ap242-e3.stp) | [`nist-stc-07.pdf`](drawings/nist-stc-07/nist-stc-07.pdf) |
| NIST STC-08 | [`nist_stc_08_asme1_ap242-e3.stp`](steps/nist/nist_stc_08_asme1_ap242-e3.stp) | [`nist-stc-08.pdf`](drawings/nist-stc-08/nist-stc-08.pdf) |
| NIST STC-09 | [`nist_stc_09_asme1_ap242-e4.stp`](steps/nist/nist_stc_09_asme1_ap242-e4.stp) | [`nist-stc-09.pdf`](drawings/nist-stc-09/nist-stc-09.pdf) |
| NIST STC-10 | [`nist_stc_10_asme1_ap242-e2.stp`](steps/nist/nist_stc_10_asme1_ap242-e2.stp) | [`nist-stc-10.pdf`](drawings/nist-stc-10/nist-stc-10.pdf) |

### FreeCAD parts library

| Drawing | STEP input | PDF |
| --- | --- | --- |
| NEMA 17 mount bracket | [`nema17-mount-bracket.step`](steps/freecad/nema17-mount-bracket.step) | [`nema17-mount-bracket.pdf`](drawings/nema17-mount-bracket/nema17-mount-bracket.pdf) |
| 608ZZ ball bearing | [`bearing-608zz.step`](steps/freecad/bearing-608zz.step) | [`bearing-608zz.pdf`](drawings/bearing-608zz/bearing-608zz.pdf) |
| LM10UU linear bearing | [`bearing-lm10uu.step`](steps/freecad/bearing-lm10uu.step) | [`bearing-lm10uu.pdf`](drawings/bearing-lm10uu/bearing-lm10uu.pdf) |
| Sprocket ANSI simplex 1/2x1/4 z08 | [`sprocket-iso606-z08.step`](steps/freecad/sprocket-iso606-z08.step) | [`sprocket-iso606-z08.pdf`](drawings/sprocket-iso606-z08/sprocket-iso606-z08.pdf) |
| Hirth joint D20x8 T16x60 | [`hirth-joint.step`](steps/freecad/hirth-joint.step) | [`hirth-joint.pdf`](drawings/hirth-joint/hirth-joint.pdf) |
| DIN 471 M10 retaining ring | [`retaining-ring-din471-m10.step`](steps/freecad/retaining-ring-din471-m10.step) | [`retaining-ring-din471-m10.pdf`](drawings/retaining-ring-din471-m10/retaining-ring-din471-m10.pdf) |
| M3 x 12 hex standoff | [`hex-standoff-m3.step`](steps/freecad/hex-standoff-m3.step) | [`hex-standoff-m3.pdf`](drawings/hex-standoff-m3/hex-standoff-m3.pdf) |
| 2020 V-slot extrusion x 50 | [`vslot-2020x50.step`](steps/freecad/vslot-2020x50.step) | [`vslot-2020x50.pdf`](drawings/vslot-2020x50/vslot-2020x50.pdf) |
| 2020 corner bracket | [`corner-bracket-2020.step`](steps/freecad/corner-bracket-2020.step) | [`corner-bracket-2020.pdf`](drawings/corner-bracket-2020/corner-bracket-2020.pdf) |
| Gantry plate 20 mm V-slot | [`gantry-plate.step`](steps/freecad/gantry-plate.step) | [`gantry-plate.pdf`](drawings/gantry-plate/gantry-plate.pdf) |
| L joining plate, 5 holes | [`l-plate-5-holes.step`](steps/freecad/l-plate-5-holes.step) | [`l-plate-5-holes.pdf`](drawings/l-plate-5-holes/l-plate-5-holes.pdf) |
| LM8UU linear bearing | [`lm8uu.step`](steps/freecad/lm8uu.step) | [`lm8uu.pdf`](drawings/lm8uu/lm8uu.pdf) |
| SHF08 shaft support | [`shf08.step`](steps/freecad/shf08.step) | [`shf08.pdf`](drawings/shf08/shf08.pdf) |
| SK08 shaft support | [`sk08.step`](steps/freecad/sk08.step) | [`sk08.pdf`](drawings/sk08/sk08.pdf) |
| T8 housing bracket | [`t8-housing-bracket.step`](steps/freecad/t8-housing-bracket.step) | [`t8-housing-bracket.pdf`](drawings/t8-housing-bracket/t8-housing-bracket.pdf) |
| T8 flange nut | [`t8-flange-nut.step`](steps/freecad/t8-flange-nut.step) | [`t8-flange-nut.pdf`](drawings/t8-flange-nut/t8-flange-nut.pdf) |
| V-slot 20x20 x 100 | [`vslot-20x20-100.step`](steps/freecad/vslot-20x20-100.step) | [`vslot-20x20-100.pdf`](drawings/vslot-20x20-100/vslot-20x20-100.pdf) |
| GT2 pulley | [`gt2-pulley.stp`](steps/freecad/gt2-pulley.stp) | [`gt2-pulley.pdf`](drawings/gt2-pulley/gt2-pulley.pdf) |

### build123d

| Drawing | STEP input | PDF |
| --- | --- | --- |
| NEMA 17 bracket | [`nema-17-bracket.step`](steps/build123d/nema-17-bracket.step) | [`nema17-bracket.pdf`](drawings/nema17-bracket/nema17-bracket.pdf) |

### Open CASCADE Technology

| Drawing | STEP input | PDF |
| --- | --- | --- |
| Link rods | [`linkrods.step`](steps/occt/linkrods.step) | [`linkrods.pdf`](drawings/linkrods/linkrods.pdf) |

### text-to-cad

| Drawing | STEP input | PDF |
| --- | --- | --- |
| Angle bracket | [`angle-bracket.step`](steps/text-to-cad/angle-bracket.step) | [`t2c-angle-bracket.pdf`](drawings/t2c-angle-bracket/t2c-angle-bracket.pdf) |
| Circular flange | [`circular-flange.step`](steps/text-to-cad/circular-flange.step) | [`t2c-circular-flange.pdf`](drawings/t2c-circular-flange/t2c-circular-flange.pdf) |
| Electronics enclosure base | [`electronics-enclosure-base.step`](steps/text-to-cad/electronics-enclosure-base.step) | [`t2c-electronics-enclosure-base.pdf`](drawings/t2c-electronics-enclosure-base/t2c-electronics-enclosure-base.pdf) |
| Guide bar | [`guide-bar.step`](steps/text-to-cad/guide-bar.step) | [`t2c-guide-bar.pdf`](drawings/t2c-guide-bar/t2c-guide-bar.pdf) |
| L bracket | [`l-bracket.step`](steps/text-to-cad/l-bracket.step) | [`t2c-l-bracket.pdf`](drawings/t2c-l-bracket/t2c-l-bracket.pdf) |
| Mounting plate | [`mounting-plate.step`](steps/text-to-cad/mounting-plate.step) | [`t2c-mounting-plate.pdf`](drawings/t2c-mounting-plate/t2c-mounting-plate.pdf) |
| Perforated plate | [`perforated-plate.step`](steps/text-to-cad/perforated-plate.step) | [`t2c-perforated-plate.pdf`](drawings/t2c-perforated-plate/t2c-perforated-plate.pdf) |
| Pivot mount plate | [`pivot-mount-plate.step`](steps/text-to-cad/pivot-mount-plate.step) | [`t2c-pivot-mount-plate.pdf`](drawings/t2c-pivot-mount-plate/t2c-pivot-mount-plate.pdf) |
| Stepped shaft with keyway | [`stepped-shaft-keyway.step`](steps/text-to-cad/stepped-shaft-keyway.step) | [`t2c-stepped-shaft-keyway.pdf`](drawings/t2c-stepped-shaft-keyway/t2c-stepped-shaft-keyway.pdf) |

## AI best-effort drawings

Nine text-to-cad parts are drawn twice from the same STEP file, to show what an agent can add
through a Spec and what it can't:

- **Baseline** (`t2c-<part>`): the title block alone, so everything else is draftwright's default.
- **AI best effort** (`t2c-<part>-ai`): a Spec an AI wrote using draftwright's analysis, plan and
  review, with no hand-drawing and no edits to the output.

The first three parts below mostly apply the review's own fixes, with
[`review_loop.py`](specs/review_loop.py). The other six go further: an agent read the part as a
designer would and authored dimensions to match its model source.

Review is findings by impact: incomplete / decision / readability / advisory.

| Part | Drawings | Sheet | Review | What changed, and what's still missing |
| --- | --- | --- | --- | --- |
| Mounting plate | [Baseline](drawings/t2c-mounting-plate/t2c-mounting-plate.pdf) · [AI](drawings/t2c-mounting-plate-ai/t2c-mounting-plate-ai.pdf) · [Spec](specs/t2c-mounting-plate-ai.spec.json) | A4 1:1 → A3 1:1 | 0/1/2/1 → 0/0/1/3 | Holes located from the left and bottom edges; radius leaders tidied. The review's own fixes also added a crossing line and an overrun callout. |
| Electronics enclosure base | [Baseline](drawings/t2c-electronics-enclosure-base/t2c-electronics-enclosure-base.pdf) · [AI](drawings/t2c-electronics-enclosure-base-ai/t2c-electronics-enclosure-base-ai.pdf) · [Spec](specs/t2c-electronics-enclosure-base-ai.spec.json) | A4 1:2 → A3 1:1 | 1/1/2/3 → 1/0/1/2 | Holes located from the edges; the 50 and 35 drawn once; section arrows clear. The stepped detail has no room at 1:1 on A3. |
| L bracket | [Baseline](drawings/t2c-l-bracket/t2c-l-bracket.pdf) · [AI](drawings/t2c-l-bracket-ai/t2c-l-bracket-ai.pdf) · [Spec](specs/t2c-l-bracket-ai.spec.json) | A4 1:2 → A4 1:2 | 0/1/1/10 → 0/0/1/6 | Four extension lines moved off the ⌀6 holes. The holes are still called 8 deep in an 8 mm plate; no Spec field can fix that. |
| Angle bracket | [Baseline](drawings/t2c-angle-bracket/t2c-angle-bracket.pdf) · [AI](drawings/t2c-angle-bracket-ai/t2c-angle-bracket-ai.pdf) · [Spec](specs/t2c-angle-bracket-ai.spec.json) | A4 1:1 → A4 1:1 | 3/1/0/3 → 4/0/0/3 | Projection by-products (75.381, 93.072) replaced by the designer's 80, 40, 8 and 120°; the ⌀10 hole located. No auxiliary view is possible, so the flange is never shown true. |
| Stepped shaft with keyway | [Baseline](drawings/t2c-stepped-shaft-keyway/t2c-stepped-shaft-keyway.pdf) · [AI](drawings/t2c-stepped-shaft-keyway-ai/t2c-stepped-shaft-keyway-ai.pdf) · [Spec](specs/t2c-stepped-shaft-keyway-ai.spec.json) | A4 1:1 → A4 1:1 | 0/1/0/1 → 1/0/0/1 | Keyway located from the shaft's end instead of a tangent; shoulders as 30 and 60; floor as a reference. No section through the keyway is possible. |
| Circular flange | [Baseline](drawings/t2c-circular-flange/t2c-circular-flange.pdf) · [AI](drawings/t2c-circular-flange-ai/t2c-circular-flange-ai.pdf) · [Spec](specs/t2c-circular-flange-ai.spec.json) | A4 1:1 → A4 1:1 | 2/1/1/1 → 2/0/0/1 | ⌀30 leader moved off its centre line. The baseline's sizes were already right, so this is the smallest change. |
| Guide bar | [Baseline](drawings/t2c-guide-bar/t2c-guide-bar.pdf) · [AI](drawings/t2c-guide-bar-ai/t2c-guide-bar-ai.pdf) · [Spec](specs/t2c-guide-bar-ai.spec.json) | A4 1:5 → A3 1:2 | 0/1/1/1 → 1/0/0/1 | Larger scale; holes 20 from each end of the bar; 600 + 30 instead of 600 and 630. No broken view is possible, and the overall length had to go. |
| Perforated plate | [Baseline](drawings/t2c-perforated-plate/t2c-perforated-plate.pdf) · [AI](drawings/t2c-perforated-plate-ai/t2c-perforated-plate-ai.pdf) · [Spec](specs/t2c-perforated-plate-ai.spec.json) | A4 1:2 → A3 1:1 | 0/1/0/3 → 0/0/0/1 | Hole table replaces crowded dimensions; the ⌀6 rows now have a stated distance from the edge; the slot has its own location. |
| Pivot mount plate | [Baseline](drawings/t2c-pivot-mount-plate/t2c-pivot-mount-plate.pdf) · [AI](drawings/t2c-pivot-mount-plate-ai/t2c-pivot-mount-plate-ai.pdf) · [Spec](specs/t2c-pivot-mount-plate-ai.spec.json) | A4 1:1 → A4 1:1 | 0/1/1/2 → 0/0/0/1 | Holes 12 from the edges, as the source defines them; datums A, B and C; leaders and labels clear. |

How to read the comparison:

- **The review count isn't the measure of progress.** The angle bracket, stepped shaft and guide bar
  each gain an `incomplete` finding, because lint doesn't credit the authored dimensions that make
  those drawings better. Nor does a quiet review prove a drawing complete: on the perforated plate,
  adding the hole table left the slot unlocated, no finding mentioned it, and only the render showed it.
- **Decision findings clear because a tolerance was assumed.** Every AI drawing states ISO 2768-m,
  which is an assumption, not something in the STEP file or the model source.
- **The last six parts had a model source to read.** Their design dimensions and material come from
  it, not from the STEP file. An agent given only a STEP file couldn't recover that intent.
- **None of these has been judged fit to manufacture from.** Like the rest of this repository, they
  are unreviewed output. The pivot mount plate's bushing bore, for example, has no fit stated because
  the source gives none.

[`specs/README.md`](specs/README.md) has the detail for each part, including the choices not taken
from the source and the draftwright issues each one raised.

## Assemblies

| Assembly | STEP input | Pack PDF | Parts list CSV |
| --- | --- | --- | --- |
| Gramil marking gauge | [`gramil-assembly.step`](steps/gramil/gramil-assembly.step) | [Pack PDF](drawings/gramil-pack/gramil-pack.pdf) | [Parts list CSV](drawings/gramil-pack/gramil-pack.csv) |
| Motorcycle shock absorber | [`motorcycle-shock-absorber.step`](steps/text-to-cad/motorcycle-shock-absorber.step) | [Pack PDF](drawings/t2c-motorcycle-shock-absorber-pack/t2c-motorcycle-shock-absorber-pack.pdf) | [Parts list CSV](drawings/t2c-motorcycle-shock-absorber-pack/t2c-motorcycle-shock-absorber-pack.csv) |
| Pivot mount plate assembly | [`pivot-mount-plate.step`](steps/text-to-cad/pivot-mount-plate.step) | [Pack PDF](drawings/t2c-pivot-mount-plate-pack/t2c-pivot-mount-plate-pack.pdf) | [Parts list CSV](drawings/t2c-pivot-mount-plate-pack/t2c-pivot-mount-plate-pack.csv) |

A pack starts with a general assembly (GA) sheet with item balloons and a parts list,
then sheets for each distinct made part. Bought parts stay in the list without part sheets.
Material, BOM part numbers and supplier are blank because these STEP files carry no BOM data;
product names and any product-key references come from STEP, and make/buy is inferred by
stock draftwright. These are unreviewed outputs, including any mistakes.

## Output files

Each pack directory holds `<name>.pdf`, `<name>.csv`, `<name>.pack.json` (the minimal GA
title-block Spec), and `<name>.report.json` (the stock pack report). If a GA or part sheet
fails, the surviving outputs and the report are kept. A completed CLI invocation still counts
as a successful build; failed parts and GA failures are printed and recorded in the index.

Each drawing directory holds:

- `<name>.pdf`, the drawing;
- `<name>.drawing.json`, the draftwright Spec it was drawn from (only the title block is set,
  and everything else is draftwright's default, except on the AI best-effort drawings);
- `<name>.review.json`, the output of `draftwright review` without the SVG: its problems,
  lint and summary.

[`drawings/index.json`](drawings/index.json) records the draftwright tag that built the current
set. Entries have `kind: "drawing"` or `kind: "pack"`. Drawings record headline review
numbers (errors, warnings, infos, and findings by impact). Packs record group counts
(made/bought, rather than quantities), sheets, failed parts and GA status, plus error,
warning and info totals from pack findings, GA problems and part problems; each part error
also counts as an error. A version bump therefore shows up in one small file as well as PDFs.

## How a drawing is defined

```toml
draftwright = "v0.2.9"   # the draftwright-rust release tag that builds every drawing
formats = ["pdf"]

[[drawing]]
name = "nist-ctc-01"
step = "steps/nist/nist_ctc_01_asme1_ap242.stp"
title = "NIST CTC-01"
number = "NIST-CTC-01"

[[pack]]
name = "gramil-pack"
step = "steps/gramil/gramil-assembly.step"
title = "Gramil"
number = "GRM-00"
```

For each `[[drawing]]` entry `build.py` writes `drawings/<name>/<name>.drawing.json`, a Spec
holding only the title block, or the file an optional `spec` key names with the title block added,
then runs

```
draftwright render <step> --spec <spec> -o drawings/<name>/<name> --formats pdf
draftwright review <step> --spec <spec>
```

For each `[[pack]]` entry it writes `drawings/<name>/<name>.pack.json`, using schema
`draftwright.pack-spec/1` and setting only `ga.drawing.sheet.title`, then runs:

```
draftwright pack <step> --spec <spec> -o drawings/<name> --formats pdf,csv,json
```

The stock `pack.pdf`, `pack.csv` and `pack.json` outputs are renamed to `<name>.pdf`,
`<name>.csv` and `<name>.report.json`. The manifest's `formats` setting applies to drawings;
packs always request all three formats. Names must be unique across drawings and packs.
To add either: drop the STEP file under `steps/`, record its source and licence in that
folder's README, add an entry, and run the build.

## Building locally

Use the [draftwright-rust release](https://github.com/pzfreo/draftwright-rust/releases/tag/v0.2.9)
matching the tag in `drawings.toml`, and verify the archive against its `.sha256` asset.
Pass the extracted binary with `--cli` if another draftwright is on PATH (the Python
package is a different CLI). Alternatively, build from the pinned tag; the repository
pins its Rust toolchain:

```
git clone --depth 1 --branch v0.2.9 https://github.com/pzfreo/draftwright-rust
(cd draftwright-rust && cargo install --locked --path . --bin draftwright)
python3 build.py                 # rebuild everything (Python 3.11 or later)
python3 build.py nist-ctc-03     # rebuild one drawing
python3 build.py gramil-pack     # rebuild one assembly pack
python3 build.py --list
python3 build.py --cli /path/to/draftwright   # use a CLI that is not on PATH
```

## Staying current with draftwright

1. To move to a new draftwright-rust release, change `draftwright` in `drawings.toml` in a PR.
2. The `Drawings` workflow builds the CLI from that tag (cached per tag) and builds every
   drawing and pack on the PR; a failure there is the alert that a release changed something
   that matters. The built drawings are attached to the run as an artifact.
3. The workflow commits the rebuilt `drawings/` to the PR branch, so the PDFs and
   `index.json` diff can be reviewed in the PR, and merging puts them on `main` as they are.
   (PRs from forks only build; their drawings are rebuilt by running the workflow by hand.)
4. `main` does not rebuild on merge. To rebuild everything on `main`, run the `Drawings`
   workflow by hand (Actions → Drawings → Run workflow).

## Licensing

The STEP files are redistributed unmodified, except the text-to-cad parts, which are STEP exports
of its Python models; each source folder's README records the original location, commit and
SHA-256 of every file.

- [`steps/nist`](steps/nist/README.md): works of the U.S. federal government, not subject to
  copyright in the United States.
- [`steps/freecad`](steps/freecad/README.md): from the FreeCAD parts library, under
  [CC-BY-3.0](steps/freecad/LICENSE-CC-BY-3.0.txt), each copyright its named author. The gantry
  plate and the V-slot 20x20 profile incorporate OpenBuilds designs and are also under CC BY-SA
  4.0. The drawings of these parts are adaptations shared under the same terms and attribution.
- [`steps/build123d`](steps/build123d/README.md): from the build123d documentation, under the
  [Apache License 2.0](steps/build123d/LICENSE).
- [`steps/occt`](steps/occt/README.md): from Open CASCADE Technology's sample data, under the
  [GNU LGPL 2.1](steps/occt/LICENSE_LGPL_21.txt) with the
  [Open CASCADE exception](steps/occt/OCCT_LGPL_EXCEPTION.txt).
- [`steps/text-to-cad`](steps/text-to-cad/README.md): STEP exports of
  [text-to-cad](https://github.com/earthtojake/text-to-cad)'s example and assembly models,
  copyright Thompson Labs LLC, under the [MIT License](steps/text-to-cad/LICENSE).
- [`steps/gramil`](steps/gramil/README.md): Gramil marking gauge, copyright Paul Fremantle,
  under the [Open Community License v1 (OCL v1)](steps/gramil/LICENSE). The pack is shared
  under the same terms.

draftwright itself is AGPL-3.0.
