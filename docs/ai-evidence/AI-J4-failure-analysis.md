# AI-J4 — Failure Analysis

## Problem

Junior GUI tests failed with `TypeError: DialogHelper.__init__() missing 1 required positional argument: 'main_window'`.

Screenshots from J3/J5 showed an empty viewport despite a loaded model.

## AI recommendation

1. Make `main_window` optional in `DialogHelper` for dismiss-only use in fixtures.
2. For empty viewport — check object visibility in the model tree before capture.

## Diagnosis

| Symptom | Root cause |
|---------|--------------|
| TypeError in conftest | `DialogHelper(launcher.app)` called with one argument after signature required two |
| Empty viewport | Headless FCStd objects default to hidden in GUI |

## Fix applied

- `dialogs.py` — optional `main_window`, guard on menu methods
- `main_window.py` — `show_tree_item()` via context menu
- `viewport.py` — menu-based view orientation instead of ignored keyboard shortcuts

## Verification

```powershell
pytest tests/junior/ -v
pytest tests/middle/test_05_deterministic_viewport.py -v
```

Commit: `649ef49` (lab repo)
