# FreeCAD Manual-to-Automation Sandbox

Desktop automation sandbox for the QAE Desktop Transformation program.  
**Track:** Desktop — FreeCAD + Pywinauto + Pytest  
**Structure:** Appendix B (*Sandbox Desktop Testing*)  
**Author:** Artem Sirchenko

## Overview

Python project for UI automation around FreeCAD:

- `framework/` — launchers, page objects, assertions
- `tests/junior/` — J1–J5 test cases
- `tests/middle/` — M1–M6 placeholders (Middle track)
- `models/` — prepared `.FCStd` test models
- `baselines/` — viewport baseline images (Middle track)
- `artifacts/` — runtime screenshots (gitignored except `artifacts/week01/`)

## Prerequisites

- VS Code with extensions: Python, Pylance, Python Debugger, GitLens, Error Lens, Markdown All in One
- Python 3.14 (Company Portal) or 3.11 (Appendix A fallback)
- FreeCAD 1.1.x (Company Portal)
- Git

## Quick start

```powershell
git clone <gitlab-repo-url>
cd <repo-folder>
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python hello.py
pytest --collect-only
```

## Run Junior tests

GUI tests need a local FreeCAD install. Unit and API tests run without GUI.

```powershell
venv\Scripts\activate

# Smoke (no GUI)
pytest tests/junior/test_00_basics.py tests/junior/test_04_tolerance_check.py -v

# Full junior suite — 23 tests
pytest tests/junior/ -v
```

## Junior test map

| Task | File | Tests | GUI |
|------|------|-------|-----|
| — | `test_00_basics.py` | 7 | No |
| J1 | `test_01_launch_freecad.py` | 6 | Yes |
| J2 | `test_02_create_document.py` | 3 | Yes |
| J3 | `test_03_viewport_screenshot.py` | 3 | Yes |
| J4 | `test_04_tolerance_check.py` | 3 | No |
| J5 | `test_05_e2e_junior.py` | 1 | Partial |

Evidence summary: `docs/junior/JUNIOR_EVIDENCE.md`  
Anti-patterns review: `docs/junior/ANTI_PATTERNS_REVIEW.md`

## FreeCAD automation approach

| Layer | Tool | Use for |
|-------|------|---------|
| UI shell | Pywinauto (`uia`) | Launch, menus, viewport screenshots |
| Native dialogs | Pywinauto (`win32`) | Save As and other `#32770` dialogs |
| Geometry / files | FreeCAD Python API (`freecadcmd`) | Cubes, tolerance, `.FCStd` |
| Orchestration | Pytest + fixtures | Test isolation, setup/teardown |

Qt controls are not always visible to UIA. Verify with Inspect or `scripts/py_inspect_tree.py` before assuming menu-only automation works.

## Debugging

See `docs/debugging/DEBUGGING_CHECKLIST.md`. Logs: `artifacts/logs/sandbox.log` (runtime, gitignored).

## License

Internal AMC Bridge learning sandbox.
