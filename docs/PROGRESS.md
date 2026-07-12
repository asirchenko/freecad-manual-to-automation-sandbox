# Program Progress

Week-by-week log for the QAE Desktop sandbox (Artem Sirchenko).

**Schedule reference:** parent folder `Plan.md` and *Sandbox Desktop Testing* program document.

---

## Week 1 — Environment Setup

**Status:** Done  
**Dates:** Jun 30 – Jul 6, 2026 (program)

### Deliverables

- [x] Appendix B project scaffold (`framework/`, `tests/`, `pytest.ini`, `requirements.txt`)
- [x] Python venv with pytest, pywinauto, pillow
- [x] VS Code extensions (Python, Pylance, Python Debugger, GitLens, Error Lens, Markdown All in One)
- [x] FreeCAD 1.1.1 installed and verified
- [x] `hello.py` sanity check
- [x] Week 1 evidence: `artifacts/week01/freecad_running.png`

### What was done

- Created full Appendix B directory structure with stub modules for future weeks
- Configured `.gitignore` to track `artifacts/week01/` while ignoring runtime screenshots
- Added `scripts/capture_freecad_screenshot.py` for FreeCAD window capture
- Verified: Python 3.14.3, FreeCAD 1.1.1, venv packages installed

### How to verify

```powershell
cd freecad-manual-to-automation-sandbox
venv\Scripts\activate
python hello.py
pytest --collect-only
& "C:\Program Files\FreeCAD 1.1\bin\freecadcmd.exe" --version
```

### Notes

- SME email for Week 1 not sent; evidence kept in git
- Global `python` may not be on PATH; use `venv\Scripts\python.exe`

---

## Week 2 — Python Part 1

**Status:** Done  
**Dates:** Jul 7 – 13, 2026 (program)

### Deliverables

- [x] `week02_python/` exercises (variables, conditions, loops, functions)
- [x] `week02_python/README.md`
- [x] `week02_python/run_all.py`

### What was done

- Added runnable exercises for variables, conditions, loops, and functions
- Examples use automation context (FreeCAD, timeouts, test status, artifact paths)

### How to verify

```powershell
venv\Scripts\activate
python week02_python/run_all.py
```

---

## Week 3 — Python Part 2

**Status:** Done  
**Dates:** Jul 14 – 20, 2026 (program)

### Deliverables

- [x] `framework/utils/basics.py` (lists, dict, exceptions)
- [x] `tests/junior/test_00_basics.py` (7 pytest tests)
- [x] `week03_python/README.md`
- [x] `pytest.ini` — `pythonpath = .` for framework imports

### What was done

- Added helper module `framework/utils/basics.py` with list/dict/exception utilities
- Wrote 7 pytest tests grouped by topic: lists, dict, exceptions, modules
- Tests import from `framework` the same way later UI tests will

### How to verify

```powershell
venv\Scripts\activate
pytest tests/junior/test_00_basics.py -v
```

### Notes

- First real pytest suite in the project; all tests are unit-level (no FreeCAD yet)

---

## Week 4 — Pywinauto Part 1

**Status:** Done  
**Dates:** Jul 21 – 27, 2026 (program)

### Deliverables

- [x] `framework/app/freecad_launcher.py`
- [x] `framework/utils/paths.py`
- [x] `framework/utils/waits.py`
- [x] `tests/conftest.py` with `freecad_app` fixture
- [x] `tests/junior/test_01_launch_freecad.py` (3 UI tests)
- [x] `week04_pywinauto/README.md`

### What was done

- `FreeCADLauncher` starts FreeCAD, connects via pywinauto UIA, exposes main window
- `freecad_app` fixture launches before test and kills process after test
- Three startup checks: process running, window visible/enabled, title contains "FreeCAD"

### How to verify

```powershell
venv\Scripts\activate
pytest tests/junior/test_01_launch_freecad.py -v
```

### Notes

- UI tests are local-only (FreeCAD GUI required); ~20s total runtime
- Startup screenshot deferred to Week 7 (full J1)

---

## Week 5 — Pywinauto Part 2

**Status:** Done  
**Dates:** Jul 28 – Aug 3, 2026 (program)

### Deliverables

- [x] `framework/ui/main_window.py` — page object, menu bar access
- [x] `framework/ui/viewport.py` — screenshot to `artifacts/`
- [x] `framework/ui/dialogs.py` — optional OK dialog dismiss
- [x] `framework/assertions/image_assertions.py` — Pillow size/dimension checks
- [x] Extended `tests/junior/test_01_launch_freecad.py` (5 tests, module-scoped launch)
- [x] `week05_pywinauto/README.md`

### What was done

- MainWindow reads menu items from the correct UIA MenuBar (FreeCAD has two bars)
- Viewport saves `artifacts/startup_viewport_week5.png`
- Pillow asserts file exists, min size, and dimensions
- Module fixture `launched_freecad` — one FreeCAD launch for all tests in the file (~7s)

### How to verify

```powershell
venv\Scripts\activate
pytest tests/junior/test_01_launch_freecad.py -v
```

### Notes

- Qt child viewport controls remain limited under UIA; main-window capture is the Week 5 approach
- Baseline compare deferred to Week 15 (M5)

---

## Week 6 — Git Fundamentals

**Status:** Pending  
**Dates:** Aug 4 – 10, 2026

### Deliverables

- [ ] Clone assigned GHE repo, feature branch, PR, merge conflict exercise

---

## Weeks 7–20

See `Plan.md` in the parent Sandbox folder for the full schedule.  
Update this file when each week is started or completed.

| Week | Topic | Status |
|------|-------|--------|
| 4 | Pywinauto Part 1 | Done |
| 5 | Pywinauto Part 2 | Done |
| 6 | Git Fundamentals | Pending |
| 7–9 | Create Tests J1–J5 | Pending |
| 10 | Debugging Tools | Pending |
| 11–12 | Junior consolidation & review | Pending |
| 13–18 | Middle track M1–M6 + CI/CD + AI | Pending |
