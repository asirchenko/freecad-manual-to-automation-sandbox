# FreeCAD Manual-to-Automation Sandbox (Draft)

Desktop automation sandbox for the QAE Transformation program.

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
- `artifacts/` — runtime screenshots (gitignored)
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
│   └── ai-evidence/
├── week02_python/
├── week03_python/
├── hello.py              # Week 1 sanity check
├── pytest.ini
└── requirements.txt
```

## FreeCAD + Qt strategy

FreeCAD is a Qt application. Pywinauto (`uia` backend) handles launch, menus, and dialogs. Geometry validation uses the **FreeCAD Python API**. Pytest fixtures orchestrate setup/teardown.

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

## License

Internal learning sandbox — not for public distribution unless approved by program owners.
