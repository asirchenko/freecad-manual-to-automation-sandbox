# Artifacts and Files by Week

Consolidated registry of **repo files** and **runtime artifacts** added per program week.

| Document | Role |
|----------|------|
| [PROGRESS.md](PROGRESS.md) | Week status, deliverables checklist, verify commands |
| [ARTIFACTS.md](ARTIFACTS.md) | This file — paths, git tracking, produced-by |
| `weekXX_*/README.md` | Single-week guide and file map |

**Update rule:** when a week is completed, add its section here and link any new artifact paths from tests or scripts.

---

## Git tracking policy

| Location | In git? | Notes |
|----------|---------|-------|
| `artifacts/week01/**` | Yes | Week 1 required evidence |
| `artifacts/**/*.png` | No | Runtime screenshots (`.gitignore`) |
| `artifacts/**/*.FCStd` | No | Runtime saves from tests/scripts |
| `models/*.FCStd` | Yes | Prepared test models (Week 8+) |
| `baselines/` | Yes (when added) | Baseline images — Week 15+ |
| `docs/git-evidence/` | Yes | Week 6 Git task outputs |

Runtime artifacts are created locally when you run tests or scripts. Paths below are **expected outputs**, not guaranteed to exist until you run the verify commands in [PROGRESS.md](PROGRESS.md).

---

## Master artifact index

| Path | Week | Produced by | In git |
|------|------|-------------|--------|
| `artifacts/week01/freecad_running.png` | 1 | `scripts/capture_freecad_screenshot.py` | Yes |
| `artifacts/startup_viewport_week5.png` | 5 | Week 5 screenshot test (superseded by J1 in Week 7) | No |
| `artifacts/j1_startup_screenshot.png` | 7 | `test_j1_startup_screenshot` | No |
| `artifacts/j2_create_document_screenshot.png` | 7 | `test_j2_create_document_screenshot` | No |
| `artifacts/j3_viewport_sample_box.png` | 8 | `test_j3_viewport_screenshot_with_pillow` | No |
| `artifacts/j5_e2e_geometry.FCStd` | 9 | `test_j5_e2e_junior_flow` (API) | No |
| `artifacts/j5_e2e_saved.FCStd` | 9 | `test_j5_e2e_junior_flow` (API) | No |
| `artifacts/j5_e2e_viewport.png` | 9 | `test_j5_e2e_junior_flow` (UI) | No |
| `models/sample_box.FCStd` | 8 | `scripts/create_sample_box.py` | Yes |
| `docs/git-evidence/task02_git_branch.txt` | 6 | `git branch` | Yes |
| `docs/git-evidence/task03_git_log.txt` | 6 | `git log --oneline` | Yes |
| `docs/git-evidence/task05_pr_link.txt` | 6 | PR creation | Yes |

### Dev / debug outputs (not program deliverables)

| Path | Produced by |
|------|-------------|
| `artifacts/debug_save_as.FCStd` | `scripts/debug_save_as_dialog.py` |
| `artifacts/ui_save_test.FCStd` | Manual / Save As UI verification |
| `artifacts/logs/sandbox.log` | 10 | pytest / framework logging (`logging_config.py`) | No |

---

## Week 1 — Environment Setup

### Repo files added

| Path | Purpose |
|------|---------|
| `pytest.ini` | Pytest config |
| `requirements.txt` | Python dependencies |
| `hello.py` | Sanity check script |
| `.gitignore` | venv, cache, artifact rules |
| `framework/` | Package scaffold (stub modules) |
| `tests/junior/`, `tests/middle/` | Test directory layout |
| `artifacts/.gitkeep`, `baselines/.gitkeep` | Placeholder dirs |
| `docs/ai-evidence/.gitkeep` | Week 18 evidence placeholder |
| `scripts/capture_freecad_screenshot.py` | Week 1 FreeCAD screenshot |

### Artifacts

| Path | In git |
|------|--------|
| `artifacts/week01/freecad_running.png` | Yes |

---

## Week 2 — Python Part 1

### Repo files added

| Path | Purpose |
|------|---------|
| `week02_python/01_variables.py` | Variables exercise |
| `week02_python/02_conditions.py` | Conditions exercise |
| `week02_python/03_loops.py` | Loops exercise |
| `week02_python/04_functions.py` | Functions exercise |
| `week02_python/05_practice.py` | Practice exercise |
| `week02_python/run_all.py` | Run all exercises |
| `week02_python/README.md` | Week guide |

### Artifacts

None (console output only).

---

## Week 3 — Python Part 2

### Repo files added

| Path | Purpose |
|------|---------|
| `framework/utils/basics.py` | Lists, dict, exception helpers |
| `tests/junior/test_00_basics.py` | 7 pytest unit tests |
| `week03_python/README.md` | Week guide |
| `pytest.ini` | Added `pythonpath = .` |

### Artifacts

None.

---

## Week 4 — Pywinauto Part 1

### Repo files added

| Path | Purpose |
|------|---------|
| `framework/app/freecad_launcher.py` | Launch / connect / close FreeCAD |
| `framework/utils/paths.py` | `artifact_path`, `model_path` |
| `framework/utils/waits.py` | `wait_until`, `wait_for_value` |
| `tests/conftest.py` | `freecad_app` fixture |
| `tests/junior/test_01_launch_freecad.py` | 3 startup UI tests |
| `week04_pywinauto/README.md` | Week guide |

### Artifacts

None (no screenshot tests yet).

---

## Week 5 — Pywinauto Part 2

### Repo files added

| Path | Purpose |
|------|---------|
| `framework/ui/main_window.py` | Page object: menus, toolbar, tree |
| `framework/ui/viewport.py` | Screenshot capture to `artifacts/` |
| `framework/ui/dialogs.py` | Dialog helpers (OK dismiss; Save As added later) |
| `framework/assertions/image_assertions.py` | Pillow file checks |
| `tests/junior/test_01_launch_freecad.py` | Extended (+ menu bar, screenshot tests) |
| `week05_pywinauto/README.md` | Week guide |

### Artifacts

| Path | Test / script | In git |
|------|---------------|--------|
| `artifacts/startup_viewport_week5.png` | Week 5 screenshot test | No |

---

## Week 6 — Git Fundamentals

### Repo files added

| Path | Purpose |
|------|---------|
| `week06_git/README.md` | 7-task Git guide |
| `week06_git/conflict_demo.txt` | Merge conflict lab |
| `week06_git/MERGE_CONFLICT_RESOLVED.md` | Conflict resolution notes |
| `docs/git-evidence/README.md` | Evidence naming guide |
| `docs/git-evidence/task02_git_branch.txt` | Task 2 output |
| `docs/git-evidence/task03_git_log.txt` | Task 3 output |
| `docs/git-evidence/task05_pr_link.txt` | PR #1 link |
| `docs/git-evidence/PR_BODY_WEEK06.md` | PR description draft |

### Git outputs (not in `artifacts/`)

| Item | Value |
|------|-------|
| Feature branch | `feature/week06-git-fundamentals` |
| Pull request | [#1](https://github.com/asirchenko/freecad-manual-to-automation-sandbox/pull/1) |

### Suggested screenshots (optional, `docs/git-evidence/`)

`task01_clone_vscode.png`, `task04_remote_branch.png`, `task06_review_reply.png`, `task07_conflict_resolved.png`

---

## Week 7 — Create Tests J1 + J2

### Repo files added / changed

| Path | Purpose |
|------|---------|
| `tests/junior/test_01_launch_freecad.py` | J1 — 6 tests + startup screenshot |
| `tests/junior/test_02_create_document.py` | J2 — 3 tests |
| `tests/conftest.py` | `launched_freecad`, `main_window`, `document_window` |
| `framework/ui/main_window.py` | `create_new_document`, `get_model_tree_items` |
| `week07_tests/README.md` | Week guide |

### Artifacts

| Path | Test | In git |
|------|------|--------|
| `artifacts/j1_startup_screenshot.png` | `test_j1_startup_screenshot` | No |
| `artifacts/j2_create_document_screenshot.png` | `test_j2_create_document_screenshot` | No |

---

## Week 8 — Create Tests J3 + J4

### Repo files added

| Path | Purpose |
|------|---------|
| `models/sample_box.FCStd` | 10 mm cube test model |
| `scripts/create_sample_box.py` | Generate `sample_box.FCStd` |
| `framework/app/freecad_api.py` | Headless `freecadcmd` runner |
| `framework/assertions/geometry_assertions.py` | Tolerance assertions |
| `framework/app/freecad_launcher.py` | `launch(open_path=...)` |
| `tests/junior/test_03_viewport_screenshot.py` | J3 — 3 tests |
| `tests/junior/test_04_tolerance_check.py` | J4 — 3 tests (no file artifacts) |
| `tests/conftest.py` | `model_window` fixture |
| `week08_tests/README.md` | Week guide |

### Artifacts

| Path | Test / script | In git |
|------|---------------|--------|
| `models/sample_box.FCStd` | `create_sample_box.py` | Yes |
| `artifacts/j3_viewport_sample_box.png` | `test_j3_viewport_screenshot_with_pillow` | No |

---

## Week 9 — Create Tests J5 E2E

### Repo files added / changed

| Path | Purpose |
|------|---------|
| `tests/junior/test_05_e2e_junior.py` | J5 E2E flow |
| `framework/app/freecad_api.py` | `create_box_and_save`, `save_document_copy` |
| `framework/ui/dialogs.py` | `save_document_as` (win32 Save As — post-J5 fix) |
| `framework/ui/main_window.py` | `save_document_as` wrapper |
| `week09_tests/README.md` | Week guide |

### Artifacts

| Path | Step | In git |
|------|------|--------|
| `artifacts/j5_e2e_geometry.FCStd` | API create + save | No |
| `artifacts/j5_e2e_viewport.png` | UI viewport screenshot | No |
| `artifacts/j5_e2e_saved.FCStd` | API save copy | No |

---

## Week 10 — Debugging Tools

### Repo files added

| Path | Purpose |
|------|---------|
| `docs/debugging/DEBUGGING_CHECKLIST.md` | 7-step debugging workflow (docx 6.3) |
| `docs/debugging/save-as-root-cause.md` | Root cause doc — Save As UIA vs win32 |
| `framework/utils/logging_config.py` | Console + file logging |
| `framework/utils/ui_inspect.py` | Control tree dump helpers |
| `scripts/py_inspect_tree.py` | CLI UI inspection while FreeCAD runs |
| `scripts/_bootstrap.py` | Project root on sys.path for standalone scripts |
| `.vscode/launch.json` | VS Code pytest / script debug configs |
| `week10_debugging/README.md` | Week guide |

### Repo files changed

| Path | Change |
|------|--------|
| `framework/app/freecad_launcher.py` | Launch/close log lines |
| `framework/ui/dialogs.py` | Save As step logging |
| `tests/conftest.py` | Session autouse `setup_logging()` |
| `pytest.ini` | `log_cli_level` for optional `--log-cli-level` |

### Artifacts

| Path | Produced by | In git |
|------|-------------|--------|
| `artifacts/logs/sandbox.log` | pytest session / framework modules | No |

---

## Week 11 — Junior Consolidation

### Repo files added

| Path | Purpose |
|------|---------|
| `docs/junior/JUNIOR_EVIDENCE.md` | J1–J5 evidence package |
| `docs/junior/ANTI_PATTERNS_REVIEW.md` | Anti-patterns self-review |
| `docs/junior/PR_BODY_WEEK11.md` | PR template |
| `week11_consolidation/README.md` | Week guide |

### Repo files changed

| Path | Change |
|------|--------|
| `README.md` | Junior run instructions, doc index, status |

### Artifacts

None (documentation week).

---

## Weeks 12+

Add a new section when each week starts. Planned locations:

| Week | Expected additions |
|------|-------------------|
| 12 | SME Junior review on PR |
| 15 (M5) | `baselines/*.png` |
| 17 | `.github/workflows/pytest.yml` |
| 18 | `docs/ai-evidence/` |

---

## Quick verify — regenerate runtime artifacts

```powershell
cd freecad-manual-to-automation-sandbox
venv\Scripts\activate

# Week 1 evidence
python scripts/capture_freecad_screenshot.py

# Week 8 model (if missing)
& "C:\Program Files\FreeCAD 1.1\bin\freecadcmd.exe" scripts/create_sample_box.py

# Junior tests (creates screenshots + J5 .FCStd files)
pytest tests/junior/ -v
```
