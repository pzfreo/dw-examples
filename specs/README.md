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

The spring in the shock-absorber pack (simplified coil with a data table) needs Draftwright
work and has no `-ai` version yet.
