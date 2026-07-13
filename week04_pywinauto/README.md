# Week 4 — Pywinauto Part 1

**Topics:** launch FreeCAD, pywinauto UIA backend, pytest fixture  
**Deliverables:** `freecad_launcher.py`, `conftest.py`, `test_01_launch_freecad.py`

## What was added

| File | Role |
|------|------|
| `framework/app/freecad_launcher.py` | Start/connect/close FreeCAD |
| `framework/utils/paths.py` | `artifacts/`, `models/`, `baselines/` paths |
| `framework/utils/waits.py` | `wait_until`, `wait_for_value` (no hard sleeps in tests) |
| `tests/conftest.py` | `freecad_app` fixture |
| `tests/junior/test_01_launch_freecad.py` | 3 UI startup tests |

## Run UI tests

```powershell
venv\Scripts\activate
pytest tests/junior/test_01_launch_freecad.py -v
```

Requires **FreeCAD installed locally**. Each test launches and closes FreeCAD (~15–30s per test).

## Fixture flow

```
test starts
  -> freecad_app fixture launches FreeCAD
  -> test uses launcher.get_main_window()
  -> fixture closes FreeCAD (kill process)
```

## Notes

- Backend: `uia` (Qt controls may be limited; top-level window works)
- Startup screenshot is added in Week 7 (full J1 evidence)
- These tests are **local only** until CI runner can launch FreeCAD (Week 17)

Progress log: [docs/PROGRESS.md](../docs/PROGRESS.md)
