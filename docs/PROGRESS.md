# Program Progress

Week-by-week log for the QAE Desktop sandbox (Artem Sirchenko).

**Schedule reference:** parent folder `Plan.md` and *Sandbox Desktop Testing* program document.  
**Files and artifacts registry:** [ARTIFACTS.md](ARTIFACTS.md)

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

**Status:** Done  
**Dates:** Aug 4 – 10, 2026 (program)

### Deliverables

- [x] Feature branch `feature/week06-git-fundamentals`
- [x] Meaningful commits for Weeks 2–5 work
- [x] Push to remote GitHub
- [x] Pull Request [#1](https://github.com/asirchenko/freecad-manual-to-automation-sandbox/pull/1)
- [x] Merge conflict lab (`week06_git/conflict_demo.txt`) — resolved
- [x] `week06_git/README.md` — 7-task guide
- [x] `docs/git-evidence/` — branch log, commit log, PR link
- [ ] Task 6: SME review feedback (pending real review on PR)

### What was done

| Task | Result |
|------|--------|
| 1 Clone | Repo already cloned; structure in Appendix B layout |
| 2 Branch | `feature/week06-git-fundamentals` |
| 3 Commits | Separate commits per week + Week 6 docs |
| 4 Push | Branch on `origin` |
| 5 PR | https://github.com/asirchenko/freecad-manual-to-automation-sandbox/pull/1 |
| 6 Review | Awaiting SME comments on PR |
| 7 Conflict | `add/add` on `conflict_demo.txt` — resolved, see `MERGE_CONFLICT_RESOLVED.md` |

### How to verify

```powershell
git branch
git log --oneline -10
git remote show origin
gh pr view 1
```

### Notes

- Program assigns AMC Bridge GHE; this repo uses GitHub mirror `asirchenko/freecad-manual-to-automation-sandbox`
- Task 6 completes when SME reviews PR #1

---

## Week 7 — Create Tests Part 1 (J1 + J2)

**Status:** Done  
**Dates:** Aug 11 – 17, 2026 (program)

### Deliverables

- [x] J1 full startup verification in `test_01_launch_freecad.py` (6 tests)
- [x] J1 startup screenshot `artifacts/j1_startup_screenshot.png`
- [x] J2 `test_02_create_document.py` (3 tests)
- [x] J2 screenshot `artifacts/j2_create_document_screenshot.png`
- [x] `MainWindow.create_new_document()` and `get_model_tree_items()`
- [x] Shared UI fixtures moved to `tests/conftest.py`
- [x] `week07_tests/README.md`

### What was done

- J1: process, window, menu bar, toolbar `New Document`, startup screenshot with Pillow checks
- J2: create document via toolbar, verify `Unnamed` in title and model tree, screenshot
- Document creation uses toolbar button (reliable under UIA; File menu less stable on Qt)

### How to verify

```powershell
venv\Scripts\activate
pytest tests/junior/test_01_launch_freecad.py -v
pytest tests/junior/test_02_create_document.py -v
```

Expected: 6 + 3 = 9 passed (~17s, FreeCAD required).

### Notes

- Screenshots saved to `artifacts/` (gitignored except `week01/`)

---

## Week 8 — Create Tests Part 2 (J3 + J4)

**Status:** Done  
**Dates:** Aug 18 – 24, 2026 (program)

### Deliverables

- [x] `models/sample_box.FCStd` (10 mm cube)
- [x] `scripts/create_sample_box.py`
- [x] `test_03_viewport_screenshot.py` (3 tests)
- [x] `test_04_tolerance_check.py` (3 tests)
- [x] `framework/app/freecad_api.py` — headless `freecadcmd` runner
- [x] `framework/assertions/geometry_assertions.py`
- [x] Viewport: fit all, front view, model screenshot
- [x] `week08_tests/README.md`

### What was done

- J3: launch FreeCAD with `sample_box.FCStd`, verify tree, viewport shortcuts, Pillow screenshot
- J4: create cube via `Part.makeBox` in freecadcmd, tolerance checks with `math.isclose`
- `FreeCADLauncher.launch(open_path=...)` opens prepared models reliably (UI File dialog avoided)

### How to verify

```powershell
pytest tests/junior/test_03_viewport_screenshot.py -v
pytest tests/junior/test_04_tolerance_check.py -v
```

Expected: 3 + 3 = 6 passed.

### Notes

- J4 runs without GUI (~2.5s); J3 needs local FreeCAD (~10s)

---

## Week 9 — Create Tests Part 3 (J5 E2E)

**Status:** Done  
**Dates:** Aug 25 – 31, 2026 (program)

### Deliverables

- [x] `test_05_e2e_junior.py` — `test_j5_e2e_junior_flow`
- [x] `FreeCADApiRunner.create_box_and_save()` and `save_document_copy()`
- [x] Artifacts: `j5_e2e_geometry.FCStd`, `j5_e2e_saved.FCStd`, `j5_e2e_viewport.png`
- [x] `week09_tests/README.md`

### What was done

Single E2E test: API geometry + validation → UI launch/open → model tree check → viewport screenshot → API save copy → verify all artifacts.

### How to verify

```powershell
pytest tests/junior/test_05_e2e_junior.py -v
```

Expected: 1 passed (~15s).

### Notes

- UI Save As is flaky on Qt; save step uses freecadcmd (documented in week09 README)
- **Junior track J1–J5 complete**

---

## Week 10 — Debugging Tools

**Status:** Done  
**Dates:** Sep 1 – 7, 2026 (program)

### Deliverables

- [x] `docs/debugging/DEBUGGING_CHECKLIST.md` — 7-step workflow (docx 6.3)
- [x] `docs/debugging/save-as-root-cause.md` — root cause doc + fix (Save As / UIA vs win32)
- [x] `framework/utils/logging_config.py` — file + console logging
- [x] `framework/utils/ui_inspect.py` — control tree helpers
- [x] `scripts/py_inspect_tree.py` — py_inspect CLI
- [x] `.vscode/launch.json` — pytest and script debug configs
- [x] Logging wired in `freecad_launcher.py`, `dialogs.py`, `conftest.py`
- [x] `week10_debugging/README.md`

### What was done

- Documented debugging checklist: assertion → locator → trace → screenshots → env → test isolation
- Root cause write-up for Save As: UIA does not expose `#32770` dialog; fix uses win32 + `Ctrl+Shift+S`
- Added `artifacts/logs/sandbox.log` output via session autouse fixture in `conftest.py`
- VS Code launch configs for stepping through tests and `py_inspect_tree.py`

### How to verify

```powershell
venv\Scripts\activate
pytest tests/junior/test_00_basics.py -v
pytest tests/junior/test_01_launch_freecad.py -v -s --log-cli-level=INFO
python scripts/py_inspect_tree.py --depth 1 --backend uia
```

Expected: basics pass; UI test logs show `framework.app.freecad_launcher` lines; log file created under `artifacts/logs/`.

### Notes

- `py_inspect_tree.py` requires local FreeCAD (interactive — press Enter to close)
- Save As fix was implemented during Week 9; Week 10 documents the debugging process formally
- `scripts/_bootstrap.py` fixes `ModuleNotFoundError: framework` when running scripts directly

---

## Week 11 — Junior Consolidation

**Status:** Done  
**Dates:** Sep 8 – 14, 2026 (program)

### Deliverables

- [x] `docs/junior/JUNIOR_EVIDENCE.md` — J1–J5 evidence package
- [x] `docs/junior/ANTI_PATTERNS_REVIEW.md` — self-review (12 items, all pass)
- [x] `docs/junior/PR_BODY_WEEK11.md` — PR template «Junior cleanup»
- [x] `README.md` — Junior run instructions, doc links, removed Draft
- [x] `week11_consolidation/README.md`
- [ ] GitHub PR «Junior cleanup» (open when ready)

### What was done

- Consolidated Junior documentation: evidence index, anti-patterns sign-off, test run matrix (23 tests)
- README polish: how to run full junior suite, script notes, `docs/junior/` in layout

### How to verify

```powershell
venv\Scripts\activate
pytest tests/junior/test_00_basics.py tests/junior/test_04_tolerance_check.py -v
pytest tests/junior/ -v
```

Expected: 10 + 23 passed (23 total when running full suite once).

### Notes

- Week 12: SME review on Junior PR
- Middle track stubs remain in `tests/middle/` for Week 13+

---

## Week 12 — Junior SME Review

**Status:** Done  
**Deliverables:** SME sign-off checklist in `week12_junior_review/README.md`; junior evidence unchanged from Week 11.

---

## Weeks 13–18 — Middle Track

**Status:** Done  

| Week | Deliverables |
|------|--------------|
| 13 | `framework/ui/preferences.py`, `test_01_preferences.py` (M1) |
| 14 | `test_03_cad_api.py`, `models/middle_api_box.FCStd` (M3) |
| 15 | `test_04`, `test_05`, `baselines/viewport_sample_box_front.png`, baseline compare in `image_assertions.py` (M4, M5) |
| 16 | `test_02_dialog_stability.py`, `flakiness-preferences.md` (M2) |
| 17 | `framework/config.py`, `.github/workflows/pytest.yml`, `docs/cicd/CI_NOTES.md` |
| 18 | `test_06_e2e_middle.py`, `docs/ai-evidence/`, `docs/middle/MIDDLE_EVIDENCE.md` |

---

## Weeks 12–20

| Week | Topic | Status |
|------|-------|--------|
| 12 | Junior SME Review | Done (docs ready) |
| 13 | M1 Preferences | Done |
| 14 | M3 CAD API | Done |
| 15 | M4 Geometry + M5 Baselines | Done |
| 16 | M2 Dialog Stability | Done |
| 17 | Config + CI/CD | Done |
| 18 | M6 E2E + AI Evidence | Done |

### Week 18 verify (full program)

```powershell
pytest tests/ -v
```

Expected: **40 passed** (23 junior + 17 middle).

See `Plan.md` in the parent Sandbox folder for schedule reference.
