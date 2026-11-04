# Specs set by an AI

The drawings in `drawings/` are built from a Spec holding only the title block: Draftwright's
defaults, with no design intent. The `-ai` drawings use the same STEP files with a Spec an AI set
the way the product is meant to be used: from Draftwright's own analysis, plan and review, with
no hand-drawing. They show what an agent can already fix through the Spec, and what it can't.

How each Spec was made (Draftwright v0.2.9):
1. `draftwright analyse` and `plan` for the part's feature and dimension ids.
2. Fill what the review asks for (`general_tolerance_missing` → `sheet/title/tolerance`).
3. Locate hole patterns from the part's edges with baseline `dimension_schemes` (`from: min`).
   Observed on the mounting plate: setting `origin` alone did not change how its holes were
   located; the baseline schemes did.
4. `review_loop.py`: review, apply the review's own `fix` operations that move a dimension,
   repeat. Fixes that change the sheet (`sheet/`, `sheets/`: size, scale, sheet count) are left
   out: taken blindly they shrink the part to 1:2 on A4. The sheet was then set by hand to 1:1 on
   A3 (mounting plate, enclosure). The loop stops when the fixes change nothing or bring back a
   Spec already tried: on the mounting plate they flip the slot width's label above and below.

The Specs name some dimensions by Draftwright's generated ids (`d:scheme:holes-y/…`), which are
those of v0.2.9; a Draftwright bump may need them set again.

| Part | Fixed through the Spec | New in the review | Not fixable through the Spec yet |
|---|---|---|---|
| Mounting plate | holes located from the left and bottom edges; general tolerance; the radius leaders | the 8 (slot) extension line crosses a ⌀5.5 hole; the 4× ⌀5.5 callout runs past its view's area | |
| Electronics enclosure base | holes located from the edges (15/85, 10/60); the 50 and 35 drawn once; general tolerance; section-arrow overlaps | the stepped-detail view has no room at 1:1 on A3 | |
| L bracket | general tolerance; four extension lines through the ⌀6 holes | | the ⌀6 holes called 8 deep in an 8 mm plate: the review flags `hole_bottom_unknown`, but no Spec field sets a hole's depth or "through" (queued in Draftwright) |
| Angle bracket | see below | | see below |
| Stepped shaft with keyway | see below | | see below |

The spring in the shock-absorber pack (simplified coil with a data table) needs Draftwright
work and has no `-ai` version yet.

## Angle bracket: best effort with authored dimensions

| STEP | Baseline | AI best effort | Spec |
|---|---|---|---|
| [`angle-bracket.step`](../steps/text-to-cad/angle-bracket.step) | [PDF](../drawings/t2c-angle-bracket/t2c-angle-bracket.pdf) | [PDF](../drawings/t2c-angle-bracket-ai/t2c-angle-bracket-ai.pdf) | [`t2c-angle-bracket-ai.spec.json`](t2c-angle-bracket-ai.spec.json) |

Unlike the three above, this goes past the review's own fixes: an agent read the part as a designer
would, and authored the dimensions from `Analysis.edge_ink.references`.

- **Baseline:** 75.381, 93.072 and 38.641 are by-products of the projection; the flange's length
  and thickness and the ⌀10 hole's position are not stated.
- **AI:** base 80, flange 40, thickness 8 on each, 120°, ⌀10 at 25 along the flange and 25 across;
  100 and 38.6 become references; 75.381 and 93.072 go; 1:1 on A4; no readability findings. Each
  value matches the [model source](https://github.com/amywork777/text-to-cad-upstream/blob/85d8fdbfb467ebd7e22994fe8bcd86afa6626ed3/models/examples/src/angle_bracket.py)
  (`BASE_LENGTH`, `TAB_HEIGHT`, `TAB_HOLE_HEIGHT`, `THICKNESS`), and lint remeasures authored values.
- **The review does not show this.** Baseline 4 warnings, 3 incomplete; AI 4 warnings, 4 incomplete.
  All 4 are issues 2 and 3 below. The review's counts can't be the measure of progress here.
- **Choices not from the source:** ISO 2768-m is assumed, as on the other `-ai` drawings. The
  material comes from the model source, not the STEP. The ⌀10 is measured from the far edge
  (issue 4). Nobody has judged this drawing fit to manufacture from.

### Issues found (v0.2.9)

Each was reproduced against the release binary with this Spec. Filed as: 1 already open as
[draftwright-rust#232](https://github.com/pzfreo/draftwright-rust/issues/232) and [draftwright-rust#278](https://github.com/pzfreo/draftwright-rust/issues/278); 2 [draftwright-rust#293](https://github.com/pzfreo/draftwright-rust/issues/293); 3 [draftwright-rust#300](https://github.com/pzfreo/draftwright-rust/issues/300); 4 [draftwright-rust#294](https://github.com/pzfreo/draftwright-rust/issues/294); 5 [draftwright-rust#295](https://github.com/pzfreo/draftwright-rust/issues/295); 6 [draftwright-rust#296](https://github.com/pzfreo/draftwright-rust/issues/296); 7 [draftwright-rust#297](https://github.com/pzfreo/draftwright-rust/issues/297); 8 and 9 [draftwright-rust#298](https://github.com/pzfreo/draftwright-rust/issues/298); 10–13 [draftwright-rust#299](https://github.com/pzfreo/draftwright-rust/issues/299).

**Stops the drawing being right**

1. **No auxiliary view.** `views` takes only `front`, `plan`, `side`, `iso`, `section_aa` and
   details (`views/aux_flange` is refused). The flange and its ⌀10 hole are never shown true; the
   ⌀10 is called out on an ellipse. The model source itself expects an auxiliary view here. Wanted:
   a view square to a named face or feature, carrying dimensions.
2. **An inclined hole's location can't be satisfied.** `feature_not_dimensioned` and
   `feature_not_located` stay although 25 and 25 locate it. Lint asks for `location.length.z`, but:
   an authored `along: z` is refused ("no unique z station"), `along: true` to the base is refused
   (the supports intersect), and `note_satisfies` refuses the role lint itself names ("not a
   measurement role of f:hole:2"). Nothing clears it, and the offered fix names a view that can't
   exist. Wanted: lint credits authored dimensions on the feature's axis.
3. **Lint doesn't follow an oblique chain.** `unrecognised_defining_geometry` wants the shoulders at
   35.381 and 53.072, which 80, 8, 40 and 120° already fix. It clears only by printing (75.381) and
   (93.072), the noise this drawing removes, so they stay out and the warnings stay.
4. **K6 compares spans, not what they locate.** The ⌀10's 25 from the near edge is refused as a
   duplicate of the ⌀8's. Following the message (edit the ⌀8's dimension) would leave the ⌀10
   unlocated. Workaround: measure from the far edge, a true but arbitrary choice.

**Makes it harder for an agent**

5. **Automatic sheet disagrees with an explicit one.** With no `sheet.size`/`scale` this Spec gets
   A4 1:2 at 22% fill (target 60–85%), reporting 2 hard findings for A4 1:1. Asking for A4 1:1 gives
   no such findings.
6. **Explicit lanes run off the sheet with paper to spare.** Lane 1 left of the front view gave
   `annotation_off_sheet` with the sheet's middle empty. Workaround: carry that dimension on the
   side view.
7. **References are hashes with no role.** Each `edge_ink.references` record gives geometry only, so
   finding "the flange's outer bend edge" took a coordinate-matching script. Only `axis:f:hole:2`
   names a feature.
8. **Discovery from the release alone.** The macOS arm64 archive holds the `draftwright` binary, LICENSE and README: no
   `draftwright-mcp`, no Spec schema, no `docs/model.md` (read here from the git tag). `--help` and
   `--version` are errors, and `serve` has no schema or options operation. `item_options` and
   `spec_schema` are documented for MCP; MCP was not built or tried for this drawing.
9. **Offsets are blind from the CLI.** A pinned callout's `offset` is relative to its automatic tip.
   `Session::callout_offset` returns that tip, but no CLI command does, so `[14, 12]` came from
   trial and viewing the render.

**Small**

10. Ids carry values (`step_position.length.x75_381`), so omitting one is tied to that geometry.
11. `general_tolerance_missing`'s fix also sets `keep_layout`, `size`, `scale` and `sheets/max`: a
    title-block fix freezes the sheet.
12. `nominal_rounded` still reports (38.6), a reference with its precision set on purpose.
13. A detail around the ⌀10 is refused with "needs its source view and room for its crop", which
    doesn't say which, and a detail wouldn't show it true anyway.

## Stepped shaft with keyway: best effort with authored dimensions

| STEP | Baseline | AI best effort | Spec |
|---|---|---|---|
| [`stepped-shaft-keyway.step`](../steps/text-to-cad/stepped-shaft-keyway.step) | [PDF](../drawings/t2c-stepped-shaft-keyway/t2c-stepped-shaft-keyway.pdf) | [PDF](../drawings/t2c-stepped-shaft-keyway-ai/t2c-stepped-shaft-keyway-ai.pdf) | [`t2c-stepped-shaft-keyway-ai.spec.json`](t2c-stepped-shaft-keyway-ai.spec.json) |

- **Baseline:** the keyway's centre is located with a 60 and with a 15 from a tangent to the ⌀30;
  the shoulders are 30 and 90; its depth is only "3 MAX DEEP".
- **AI:** the keyway starts 40 from the end, as the [model source](https://github.com/amywork777/text-to-cad-upstream/blob/85d8fdbfb467ebd7e22994fe8bcd86afa6626ed3/models/examples/src/stepped_shaft_keyway.py)
  defines it, and is noted `CENTRED ON AXIS`; the shoulders are 30 and 60, the source's lengths; the
  floor is (12) from the axis as a reference; material from the source. No readability findings.
- **Review:** baseline 1 warning (decision: no tolerance); AI 1 warning (incomplete: lint wants the
  keyway's location at its centre, issue 2). The count again doesn't show the change.
- **Choices not from the source:** ISO 2768-m is assumed. The source names a chromium-molybdenum
  alloy steel without a grade. No fit is stated on the keyway, as the source gives none. Nobody has
  judged this drawing fit to manufacture from.

### Issues found (v0.2.9)

Each was reproduced against the release binary with this Spec.

1. **No section through a keyway** ([draftwright-rust#304](https://github.com/pzfreo/draftwright-rust/issues/304)). `section_aa` needs a z-axis hole, a half section a part
   turned whole, and an enlarged detail is refused on this A4 sheet (it's accepted on A2). The
   depth shows only in hidden lines.
2. **Lint doesn't credit authored pocket dimensions** ([draftwright-rust#301](https://github.com/pzfreo/draftwright-rust/issues/301)). A location from the keyway's end
   stays reported as missing, and so do an authored width and length replacing the callout.
3. **"3 MAX DEEP" reads like a limit** ([draftwright-rust#305](https://github.com/pzfreo/draftwright-rust/issues/305)), and by design the wording can't be changed. A
   dimension of 27 across the shaft isn't possible, as a cylinder's far side has nothing to
   reference, so (12) from the axis stands in.
4. **A centred keyway is located from a tangent** ([draftwright-rust#302](https://github.com/pzfreo/draftwright-rust/issues/302)), and `origin` can't name the axis. A
   note with `note_satisfies` was the route that worked.
5. **Smaller** ([draftwright-rust#303](https://github.com/pzfreo/draftwright-rust/issues/303)): no keyway fit classes (N9 is refused); the plan view is dropped under
   authored dimensions until `views/plan` is set.
