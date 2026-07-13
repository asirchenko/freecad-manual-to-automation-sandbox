# AI-J1 — Test Scenario Generation

## Prompt (summary)

> Review the Middle track plan (M1–M6). Propose pytest scenarios for Preferences dialog stability and viewport baseline comparison. Identify gaps in the current junior suite that middle tests should cover.

## AI response (summary)

- Suggested parametrized open/close loop for M2 (5 runs)
- Recommended baseline image under `baselines/` with Pillow diff ratio threshold
- Flagged missing multi-window handling for Preferences vs main window

## Accepted

| Recommendation | Implementation |
|----------------|----------------|
| 5-run stability parametrization | `test_02_dialog_stability.py` + `DEFAULT_CONFIG.stability_run_count` |
| Baseline compare with max diff ratio | `assert_image_matches_baseline()` in `image_assertions.py` |

## Rejected

| Recommendation | Reason |
|----------------|--------|
| Compare screenshots pixel-exact (zero tolerance) | FreeCAD viewport rendering varies slightly; use 5% diff ratio instead |

## Decision

Implemented state-based waits and ratio-based baseline compare — aligns with docx anti-patterns (no hard sleeps, no exact pixel equality).
