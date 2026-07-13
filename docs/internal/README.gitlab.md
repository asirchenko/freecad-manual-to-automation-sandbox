# FreeCAD Manual-to-Automation Sandbox

Desktop automation sandbox for the QAE Desktop Transformation program.  
**Track:** Desktop — FreeCAD + Pywinauto + Pytest  
**Structure:** Appendix B (*Sandbox Desktop Testing*)  
**Author:** Artem Sirchenko

## Overview

Python project for UI automation around FreeCAD:

- `framework/` — launchers, page objects, assertions, config
- `tests/junior/` — J1–J5 (23 tests)
- `tests/middle/` — M1–M6 (17 tests)
- `models/` — prepared `.FCStd` test models
- `baselines/` — viewport baseline images (M5)
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

## Run tests

GUI tests need FreeCAD installed locally.

```powershell
venv\Scripts\activate

# CI smoke (no GUI)
pytest tests/junior/test_00_basics.py tests/junior/test_04_tolerance_check.py tests/middle/test_03_cad_api.py tests/middle/test_04_geometry_validation.py -v

# Full suite — 40 tests
pytest tests/ -v
```

## Test map

| Track | Tests | GUI |
|-------|-------|-----|
| Junior J1–J5 + basics | 23 | Partial |
| Middle M1–M6 | 17 | Partial |

Evidence: `docs/junior/JUNIOR_EVIDENCE.md`, `docs/middle/MIDDLE_EVIDENCE.md`

## Automation approach

| Layer | Tool | Use for |
|-------|------|---------|
| UI shell | Pywinauto (`uia`) | Launch, menus, Preferences panel, viewport |
| Native dialogs | Pywinauto (`win32`) | Save As (`#32770`) |
| Geometry / files | FreeCAD Python API | Cubes, tolerance, `.FCStd` |
| Screenshots | Pillow | File checks + baseline compare (M5) |
| Orchestration | Pytest + fixtures | Isolated tests |

## CI/CD

GitHub Actions workflow `.github/workflows/pytest.yml` runs smoke tests on push. Full UI suite runs locally — see `docs/cicd/CI_NOTES.md`.

## Debugging

`docs/debugging/DEBUGGING_CHECKLIST.md` — logs in `artifacts/logs/sandbox.log` (runtime, gitignored).

## License

Internal AMC Bridge learning sandbox.
