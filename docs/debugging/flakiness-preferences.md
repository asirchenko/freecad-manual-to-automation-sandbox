# Preferences Dialog Stability (M2)

## Context

Week 16 — replace hard waits with state checks; prove Preferences open/close is stable across 5 runs.

## Approach

- `PreferencesDialog.wait_visible()` uses `wait_until()` on dialog presence
- `click_cancel()` waits until dialog is gone before the next iteration
- Test parametrized 5 times via `DEFAULT_CONFIG.stability_run_count`

## Root cause addressed

Early prototypes used fixed `time.sleep(2)` after menu clicks. Under load, FreeCAD menus could still be animating, causing intermittent "dialog not open" failures.

## Fix

- Poll for dialog window via UIA `Desktop.windows()`
- Explicit timeout from `framework/config.py` (`SANDBOX_DIALOG_TIMEOUT` env override)

## Verify

```powershell
pytest tests/middle/test_02_dialog_stability.py -v
```

Expected: **5 passed** (one parametrized test × 5 runs).
