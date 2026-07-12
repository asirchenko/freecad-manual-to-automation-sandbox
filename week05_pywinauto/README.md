# Week 5 — Pywinauto Part 2

**Topics:** menus, dialogs, waits, viewport capture, Pillow validation  
**Deliverables:** `framework/ui/`, screenshot in `artifacts/`, image assertions

## What was added

| File | Role |
|------|------|
| `framework/ui/main_window.py` | Page object: menus, focus, capture |
| `framework/ui/viewport.py` | Save main-window screenshot to `artifacts/` |
| `framework/ui/dialogs.py` | Dismiss optional modal OK dialogs |
| `framework/assertions/image_assertions.py` | Pillow file size and dimension checks |
| `tests/junior/test_01_launch_freecad.py` | +2 tests (menu bar, screenshot) |

## Run tests

```powershell
venv\Scripts\activate
pytest tests/junior/test_01_launch_freecad.py -v
```

Expected: **5 passed** (one FreeCAD launch per module via `launched_freecad` fixture).

Screenshot output: `artifacts/startup_viewport_week5.png` (gitignored).

## Design notes

- FreeCAD is Qt; many child widgets are invisible to UIA. Week 5 captures the **main window** as a pragmatic viewport stand-in.
- Week 8 (J3) opens a prepared model and refines viewport behavior.
- Week 15 (M5) adds baseline comparison in `image_assertions.py`.

Progress log: [docs/PROGRESS.md](../docs/PROGRESS.md)
