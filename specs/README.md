# Specs set by an AI

The drawings in `drawings/` are built from a Spec holding only the title block: Draftwright's
defaults, with no design intent. The `-ai` drawings use the same STEP files with a Spec an AI set
the way the product is meant to be used: from Draftwright's own analysis, plan and review, with
no hand-drawing. They show what an agent can already fix through the Spec, and what it can't.

How each Spec was made (Draftwright v0.2.9):
1. `draftwright analyse` and `plan` for the part's feature and dimension ids.
2. Fill what the review asks for (`general_tolerance_missing` → `sheet/title/tolerance`).
3. Locate hole patterns from the part's edges with baseline `dimension_schemes` (`from: min`).
   Setting `origin` alone does not change how a pattern is located.
4. `review_loop.py`: review, apply the review's own `fix` operations that move a dimension,
   repeat. Fixes that change the sheet (size, scale) were left out: taken blindly they shrink
   the part to 1:2 on A4. The sheet was then set by hand to 1:1 on A3.

| Part | Fixed through the Spec | Not fixable through the Spec yet |
|---|---|---|
| Mounting plate | holes located from the left and bottom edges; general tolerance | |
| Electronics enclosure base | holes located from the edges (15/85, 10/60); the 50 and 35 drawn once; general tolerance | |
| L bracket | general tolerance | the ⌀6 holes called 8 deep in an 8 mm plate: the review flags `hole_bottom_unknown`, but no Spec field sets a hole's depth or "through" (queued in Draftwright) |

The spring in the shock-absorber pack (simplified coil with a data table) needs Draftwright
work and has no `-ai` version yet.
