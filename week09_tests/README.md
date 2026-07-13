# Week 9 — J5 Junior E2E

**Deliverable:** `tests/junior/test_05_e2e_junior.py` — one full-flow test

## Flow (`test_j5_e2e_junior_flow`)

| Step | Layer | Action |
|------|-------|--------|
| 1 | API | Create 10 mm cube, save `artifacts/j5_e2e_geometry.FCStd` |
| 2 | API | Validate bounding box tolerance |
| 3 | UI | Launch FreeCAD with geometry document |
| 4 | UI | Verify window + model tree (`Cube`) |
| 5 | UI | Viewport fit/front + screenshot `j5_e2e_viewport.png` |
| 6 | API | Save copy to `artifacts/j5_e2e_saved.FCStd` |
| 7 | Assert | All artifacts exist and are non-empty |

## Design note — Save step (aligned with program strategy)

Per **Plan.md** (Qt + split automation): Pywinauto handles UI shell; FreeCAD API handles geometry and file operations when needed.

**Save in J5** uses `freecadcmd` (`save_document_copy`) — matches the program's API layer for reliable file I/O.

### Save As via UI — observed in our tests (not an official pywinauto/FreeCAD claim)

- `menu_select('File->Save As')` on FreeCAD raised COM / UIA errors in our environment.
- UIA `Desktop` did not list the Save dialog; the native dialog **`Save FreeCAD Document`** (win32 class `#32770`) appears after **`Ctrl+Shift+S`**.
- UI Save As is implemented in `framework/ui/dialogs.py` (`DialogHelper.save_document_as`) for reuse in later tests.

References: [pywinauto Getting Started](https://pywinauto.readthedocs.io/en/latest/getting_started.html) (Qt5 via `uia`, backends are separate); [FreeCAD testing handbook](https://freecad.github.io/DevelopersHandbook/technical/automated_testing.html) (unittest / `freecadcmd`, no pywinauto GUI guide).

## Run

```powershell
venv\Scripts\activate
pytest tests/junior/test_05_e2e_junior.py -v
```

Expected: **1 passed** (~15–25s, FreeCAD GUI required for UI steps).

Progress log: [docs/PROGRESS.md](../docs/PROGRESS.md)
