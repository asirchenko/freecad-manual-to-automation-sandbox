# FreeCAD Manual-to-Automation Sandbox

Desktop automation sandbox for the QAE Desktop Transformation program.
**Track:** Desktop — FreeCAD + Pywinauto + Pytest  
**Structure:** Appendix B from *Sandbox Desktop Testing* program document  
**Author:** Artem Sirchenko

## What this repo is

A standalone Python project for learning and building UI automation around FreeCAD:

- `framework/` — page objects, launchers, assertions (filled in Weeks 4+)
- `tests/junior/` — J1–J5 test cases (Weeks 3–9)
- `tests/middle/` — M1–M6 test cases (Weeks 13–18)
- `models/` — prepared `.FCStd` files (Week 8+)
- `baselines/` — viewport baseline images (Week 15+)
- `artifacts/` — runtime screenshots (gitignored); see [docs/ARTIFACTS.md](docs/ARTIFACTS.md)
- `week02_python/` — Python exercises (Week 2)
- `week03_python/` — Week 3 notes and pytest guide

## Python version note

| Source | Version |
|--------|---------|
| Company Portal | Python 3.14 |
| Appendix A (docx) | Python 3.11 |

Local development uses **Python 3.14** (Company Portal). CI workflow (Week 17) targets **3.11** per Appendix A. If pywinauto/FreeCAD compatibility issues arise, fallback to 3.11.

## Prerequisites

- VS Code with extensions: Python, Pylance, Python Debugger, GitLens, Error Lens, Markdown All in One
- Python 3.14 (Company Portal) or 3.11 (Appendix A fallback)
- FreeCAD (Company Portal)
- Git

## Quick start

```powershell
git clone https://github.com/asirchenko/freecad-manual-to-automation-sandbox.git
cd freecad-manual-to-automation-sandbox
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## Pulling latest changes

To update your local working copy with the latest changes:

```powershell
cd D:\Projects\freecad-manual-to-automation-sandbox
git pull origin main
```

If you have local uncommitted changes and just want to check for remote
updates without touching them:

```powershell
git fetch origin
git status
```

## Verify environment (Week 1)

```powershell
python hello.py
pytest --collect-only
pip list
```

Expected output from `hello.py`:

```
Hello from FreeCAD Manual-to-Automation Sandbox!
Week 1 environment setup — OK
```

Verified packages (Week 1):

| Package | Version |
|---------|---------|
| pytest | 9.1.1 |
| pywinauto | 0.6.9 |
| pywin32 | 312 |
| pillow | 12.2.0 |

## Run Junior tests (J1–J5)

Requires **FreeCAD** for UI tests (`test_01` … `test_03`, `test_05`). Unit and API tests run without GUI.

```powershell
venv\Scripts\activate

# Quick smoke (no GUI)
pytest tests/junior/test_00_basics.py tests/junior/test_04_tolerance_check.py -v

# Full junior suite — 23 tests
pytest tests/junior/ -v
```

Standalone scripts (from project root):

```powershell
python scripts/py_inspect_tree.py --depth 2 --backend uia
python scripts/capture_freecad_screenshot.py
```

Evidence and anti-patterns: [docs/junior/JUNIOR_EVIDENCE.md](docs/junior/JUNIOR_EVIDENCE.md), [docs/junior/ANTI_PATTERNS_REVIEW.md](docs/junior/ANTI_PATTERNS_REVIEW.md).

## Project layout

```
freecad-manual-to-automation-sandbox/
├── framework/
│   ├── app/              # FreeCAD launcher
│   ├── ui/               # Main window, dialogs, viewport
│   ├── assertions/       # Geometry and image checks
│   └── utils/            # Paths, waits
├── tests/
│   ├── conftest.py
│   ├── junior/           # test_00 … test_05
│   └── middle/           # test_01 … test_06
├── models/
├── baselines/
├── artifacts/
├── docs/
│   ├── PROGRESS.md       # Week-by-week progress log
│   ├── ARTIFACTS.md      # Files and artifacts per week
│   ├── debugging/        # Week 10 checklist + root cause docs
│   ├── junior/           # J1–J5 evidence + anti-patterns (Week 11)
│   └── ai-evidence/
├── week02_python/
├── week03_python/
├── hello.py              # Week 1 sanity check
├── pytest.ini
└── requirements.txt
```

## FreeCAD + Qt strategy

Per program **Plan.md** and Appendix B:

| Layer | Tool | Use for |
|-------|------|---------|
| UI shell | **Pywinauto** (`uia` for main window) | Launch, menus, toolbar, viewport screenshots |
| Native dialogs | **Pywinauto** (`win32` where needed) | e.g. Save As `#32770` — see `framework/ui/dialogs.py` |
| Geometry / files | **FreeCAD Python API** (`freecadcmd`) | Cubes, tolerance, `.FCStd` save when API path is required |
| Orchestration | **Pytest** + fixtures | Independent tests, setup/teardown |

**Qt caveat (program + our tests):** UIA often does not expose all Qt controls. Do not assume every menu/dialog works via `menu_select` alone — verify with Inspect/py_inspect and prefer keyboard shortcuts or win32 for native Windows dialogs.

**Debugging (Week 10):** [docs/debugging/DEBUGGING_CHECKLIST.md](docs/debugging/DEBUGGING_CHECKLIST.md) — logs in `artifacts/logs/sandbox.log`, VS Code `.vscode/launch.json`.

Official refs: [pywinauto](https://pywinauto.readthedocs.io/), [FreeCAD testing](https://freecad.github.io/DevelopersHandbook/technical/automated_testing.html). Program schedule: parent folder `Plan.md`.

## CI/CD

GitHub Actions workflow added in **Week 17**. Full FreeCAD UI tests may require a self-hosted Windows runner; smoke tests run on `windows-latest`.

## Program status

See **[docs/PROGRESS.md](docs/PROGRESS.md)** for the full week-by-week log.

| Week | Topic | Status |
|------|-------|--------|
| 1 | Environment Setup | Done |
| 2 | Python Part 1 | Done |
| 3 | Python Part 2 (pytest basics) | Done |
| 4 | Pywinauto Part 1 | Done |
| 5 | Pywinauto Part 2 | Done |
| 6 | Git Fundamentals | Done |
| 7 | Create Tests J1–J2 | Done |
| 8 | Create Tests J3–J4 | Done |
| 9 | Create Tests J5 E2E (Junior track complete) | Done |
| 10 | Debugging Tools | Done |
| 11 | Junior Consolidation | Done |

## License

Internal learning sandbox — not for public distribution unless approved by program owners.
