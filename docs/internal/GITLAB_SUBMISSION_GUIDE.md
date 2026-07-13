# GitLab SME Submission Guide (Weeks 1–18)

**Audience:** CloudCode agent on the AMC Bridge work laptop  
**Author:** Artem Sirchenko  
**Purpose:** Submit the sandbox to the assigned GitLab repo as **18 sequential Merge Requests** — one per program week (Weeks 1–18).

**Workflow policy:** **100% manual.** No GitHub Actions sync, no GitLab mirror jobs, no scheduled pulls. Artem (or CloudCode on his instruction) runs every `git pull`, file copy, commit, push, and MR creation by hand in VS Code / terminal.

---

## 1. Two repositories — two roles

| Repo | URL pattern | Role |
|------|-------------|------|
| **GitHub (lab archive)** | `https://github.com/asirchenko/freecad-manual-to-automation-sandbox` | Full project: learning guides, progress logs, Cursor metadata. **Source of truth for file content.** |
| **GitLab (SME submission)** | `https://gitlab.amcbridge.com/<group>/<assigned-sandbox>.git` | Assigned AMC repo. **Only official deliverables.** SME reviews MRs here. |

### 1.1 What is NOT used (automation disabled)

| Automation | Status | Why |
|------------|--------|-----|
| `.github/workflows/gitlab-mirror-sync.yml` | **Do not run / ignore** | Squashes to one commit on GitLab `main`; no week-by-week MR history for SME |
| Self-hosted GitHub Actions runner on AMC laptop | **Not required** | Submission is manual push to GitLab only |
| GitLab Pull Mirroring from GitHub | **Not available** | Premium feature; was never an option |
| Auto `git pull` on a schedule | **Not used** | Artem pulls lab updates manually when ready |

SME submission = **manual** `git clone` / `git pull` (lab) → **manual** file copy → **manual** `git commit` + `git push` (GitLab) → **manual** MR in GitLab UI.

Replace `<assigned-sandbox>` with the actual path SME provided (e.g. `asirchenko/freecad-manual-to-automation-sandbox` or a team-assigned name).

---

## 2. Prerequisites (AMC laptop)

- Git configured with Artem's AMC identity (name/email used at work)
- Access to assigned GitLab repo (Maintainer or Developer + MR rights)
- Python 3.14 (Company Portal) or 3.11 fallback
- FreeCAD 1.1.x installed
- Network access to `gitlab.amcbridge.com`

```powershell
git --version
python --version
& "C:\Program Files\FreeCAD 1.1\bin\freecadcmd.exe" --version
```

---

## 3. Initial setup (run once, manually)

### 3.1 Clone both repos (one-time)

```powershell
# Lab archive — source for file copies (GitHub)
git clone https://github.com/asirchenko/freecad-manual-to-automation-sandbox.git C:\work\sandbox-lab
cd C:\work\sandbox-lab
git checkout main

# Assigned GitLab repo — submission target (SME)
git clone https://gitlab.amcbridge.com/<group>/<assigned-sandbox>.git C:\work\sandbox-gitlab
cd C:\work\sandbox-gitlab
```

Set `$LAB = "C:\work\sandbox-lab"` and `$GL = "C:\work\sandbox-gitlab"` if helpful.

**Later updates (manual only):** when Artem has pushed new work to GitHub from another machine, run on AMC:

```powershell
cd C:\work\sandbox-lab
git fetch origin
git pull origin main
```

Do this **only when Artem asks** — not on a timer or via any automation.

### 3.2 Verify lab archive (after manual pull)

```powershell
cd C:\work\sandbox-lab
git log --oneline -5
git rev-parse --short HEAD
pytest tests/junior/ --collect-only
pytest tests/junior/ -v
```

Expected:

- HEAD is **`649ef49` or later** (GUI test fixes — see section 4.6)
- Junior tests `test_00` … `test_05` collect successfully
- `models/sample_box.FCStd` exists
- Full suite: **40 passed** — 23 junior + 17 middle (~2–3 min with FreeCAD GUI tests)

---

## 4. Global rules

### 4.1 What NEVER goes to GitLab

Copy **none** of these paths into any MR:

```
.cursor/
.kilo/
docs/PROGRESS.md
docs/ARTIFACTS.md
docs/internal/                    # this guide — GitHub only
week03_python/
week04_pywinauto/
week05_pywinauto/
week06_git/README.md
week06_git/MERGE_CONFLICT_RESOLVED.md
week07_tests/
week08_tests/
week09_tests/
week10_debugging/
week11_consolidation/
week12_junior_review/
week13_middle/
week14_middle/
week15_middle/
week16_middle/
week17_cicd/
week18_final/
docs/git-evidence/PR_BODY_WEEK06.md
docs/git-evidence/README.md
docs/junior/PR_BODY_WEEK11.md
scripts/debug_save_as_dialog.py
scripts/debug_save_as_dialog2.py
.github/                           # until Week 17 (CI/CD)
artifacts/**/*.FCStd               # runtime outputs
artifacts/ui_save_test.FCStd
```

### 4.2 Commit message style (GitLab)

Use neutral, professional messages. **No** `week07:` prefixes, **no** references to PROGRESS/Plan/Cursor/AI.

| Bad | Good |
|-----|------|
| `week08: add J3/J4 tests` | `Add viewport screenshot and tolerance tests` |
| `Mark Week 10 complete in PROGRESS` | `Add debugging checklist and Save As logging` |
| `Junior consolidation evidence` | `Update README and add junior evidence summary` |

### 4.3 MR description template

Keep each MR body to 3–6 lines:

```markdown
## Summary
- <1–3 bullets: what code/tests/docs were added>

## Testing
<exact pytest or script command>
Requires FreeCAD for GUI tests (if applicable).
```

No links to `Plan.md`, `PROGRESS.md`, Cursor, or GitHub lab repo.

### 4.4 MR timing (match program schedule)

Submit **one MR per calendar week** so SME sees a natural pace. Target merge dates:

| MR | Program dates | Suggested submit |
|----|---------------|------------------|
| Week 1 | Jun 30 – Jul 6 | ASAP after setup |
| Week 2 | Jul 7 – 13 | +1 week |
| Week 3 | Jul 14 – 20 | +1 week |
| Week 4 | Jul 21 – 27 | +1 week |
| Week 5 | Jul 28 – Aug 3 | +1 week |
| Week 6 | Aug 4 – 10 | +1 week |
| Week 7 | Aug 11 – 17 | +1 week |
| Week 8 | Aug 18 – 24 | +1 week |
| Week 9 | Aug 25 – 31 | +1 week |
| Week 10 | Sep 1 – 7 | +1 week |
| Week 11 | Sep 8 – 14 | +1 week |

Wait for SME merge (or at least acknowledgment) before opening the next MR when possible.

### 4.5 Pre-MR checklist

Before every `git push`:

- [ ] No paths from the exclusion list (section 4.1)
- [ ] No Cyrillic / Russian text in committed files
- [ ] No `Co-authored-by: Cursor` or similar in commit messages
- [ ] `pytest` for this week's tests passes locally
- [ ] `git status` is clean after commit
- [ ] Copied files match **post-fix lab state** (section 4.6) when the week touches GUI/viewport/logging

### 4.6 Critical GUI fixes (lab commit `649ef49`)

The lab repo includes fixes that are **required** for a green junior suite. Always copy the
**current `main`** versions of affected files — do not use older per-week git snapshots for these paths.

| File | Fix |
|------|-----|
| `framework/ui/dialogs.py` | `DialogHelper.__init__` — `main_window` optional (conftest calls `DialogHelper(launcher.app)`) |
| `framework/ui/main_window.py` | Manual `select_menu()` (no `menu_select`); `find_tree_item()`; `show_tree_item()` for headless models |
| `framework/ui/viewport.py` | `fit_all` / `set_front_view` via `View->Standard Views` menus, not keyboard `type_keys` |
| `framework/utils/logging_config.py` | `_sandbox_logging_configured` flag — pytest no longer blocks `sandbox.log` |
| `scripts/create_sample_box.py` | Output path relative to script, not a hardcoded machine path |
| `tests/junior/test_03_viewport_screenshot.py` | Calls `show_tree_item("box")` before screenshot |
| `tests/junior/test_05_e2e_junior.py` | Calls `show_tree_item("Cube")` before viewport capture |
| `.gitignore` | Includes `artifacts/**/*.FCBak` |

**Why `show_tree_item` matters:** models created via `freecadcmd` open without a GuiDocument and stay
hidden in the tree. J3/J5 screenshots are empty without making the object visible first.

**Neutral commit message if bundling fixes into Week 8/9 MR:**

```
Fix menu navigation and hidden model visibility for viewport tests
```

---

## 5. Copy helper (PowerShell)

Use this to copy files from lab to GitLab working tree:

```powershell
function Copy-WeekFiles {
    param(
        [string]$LabRoot,
        [string]$GitLabRoot,
        [string[]]$RelativePaths
    )
    foreach ($rel in $RelativePaths) {
        $src = Join-Path $LabRoot $rel
        $dst = Join-Path $GitLabRoot $rel
        if (-not (Test-Path $src)) {
            Write-Warning "Missing in lab: $rel"
            continue
        }
        $dstDir = Split-Path $dst -Parent
        if ($dstDir -and -not (Test-Path $dstDir)) {
            New-Item -ItemType Directory -Path $dstDir -Force | Out-Null
        }
        Copy-Item -Path $src -Destination $dst -Recurse -Force
        Write-Host "Copied: $rel"
    }
}
```

---

## 6. Week-by-week manifest

Each MR is **cumulative**: it contains everything from prior weeks plus this week's additions. After SME merges MR N, branch Week N+1 from updated `main`.

For each week below:

1. **Manually** `git checkout main && git pull` in `$GL` (GitLab repo only)
2. **Manually** `git checkout -b <branch-name>`
3. **Manually** copy files listed under **Include** from `$LAB` (use `Copy-WeekFiles` or VS Code / Explorer)
4. Run **Verify**
5. **Manually** `git add` → `git commit` → `git push` → create MR in GitLab UI

---

### Week 1 — Environment Setup

| Field | Value |
|-------|-------|
| **Branch** | `feature/week01-environment-setup` |
| **MR title** | `Week 1: Environment setup and project scaffold` |
| **Commit message** | `Add project scaffold, dependencies, and environment evidence` |

**Include (copy from lab):**

```
README.md                          # use shortened version — see section 7 (Week 1 stub)
requirements.txt
pytest.ini
.gitignore
hello.py
framework/__init__.py
framework/app/__init__.py
framework/app/freecad_launcher.py  # Week 1 stub only — if full launcher exists, use Week 4 copy instead; for Week 1 MR use scaffold stubs from earliest commit OR omit launcher implementation and keep stubs
framework/ui/__init__.py
framework/ui/main_window.py        # stubs
framework/ui/dialogs.py            # stubs
framework/ui/viewport.py           # stubs
framework/assertions/__init__.py
framework/assertions/geometry_assertions.py  # stubs
framework/assertions/image_assertions.py   # stubs
framework/utils/__init__.py
framework/utils/paths.py           # stubs
framework/utils/waits.py             # stubs
tests/__init__.py                  # if exists
tests/junior/__init__.py           # if exists
tests/middle/__init__.py           # if exists
tests/middle/test_01_preferences.py  # stubs
tests/middle/test_02_dialog_stability.py
tests/middle/test_03_cad_api.py
tests/middle/test_04_geometry_validation.py
tests/middle/test_05_deterministic_viewport.py
tests/middle/test_06_e2e_middle.py
models/.gitkeep
baselines/.gitkeep
artifacts/.gitkeep
artifacts/week01/freecad_running.png
scripts/capture_freecad_screenshot.py
docs/ai-evidence/.gitkeep
```

**Note:** Week 1 `framework/*.py` files may be stubs. If the lab repo only has the final combined code, for Week 1 MR copy **stub versions** from git history:

```powershell
cd C:\work\sandbox-lab
git show c47b8eb:framework/app/freecad_launcher.py   # inspect Week 1 scaffold commit
```

If stub extraction is too complex, include minimal stubs (empty classes / `pass`) matching Appendix B layout — SME expects scaffold, not full launcher yet.

**Verify:**

```powershell
cd C:\work\sandbox-gitlab
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python hello.py
pytest --collect-only
```

**MR body:**

```markdown
## Summary
- Added Appendix B project scaffold (framework, tests, models, baselines, artifacts)
- Added requirements, pytest config, hello.py sanity check
- Added Week 1 environment evidence screenshot

## Testing
python hello.py
pytest --collect-only
```

---

### Week 2 — Python Part 1

| Field | Value |
|-------|-------|
| **Branch** | `feature/week02-python-fundamentals` |
| **MR title** | `Week 2: Python fundamentals exercises` |
| **Commit message** | `Add Python Part 1 exercises` |

**Include:**

```
week02_python/01_variables.py
week02_python/02_conditions.py
week02_python/03_loops.py
week02_python/04_functions.py
week02_python/05_practice.py
week02_python/run_all.py
week02_python/README.md
```

**Verify:**

```powershell
python week02_python/run_all.py
```

---

### Week 3 — Python Part 2

| Field | Value |
|-------|-------|
| **Branch** | `feature/week03-pytest-basics` |
| **MR title** | `Week 3: Pytest basics and framework helpers` |
| **Commit message** | `Add pytest basics and framework helper module` |

**Include:**

```
framework/utils/basics.py
tests/junior/test_00_basics.py
pytest.ini                    # must include pythonpath = .
```

**Verify:**

```powershell
pytest tests/junior/test_00_basics.py -v
```

---

### Week 4 — Pywinauto Part 1

| Field | Value |
|-------|-------|
| **Branch** | `feature/week04-freecad-launcher` |
| **MR title** | `Week 4: FreeCAD launcher and startup fixture` |
| **Commit message** | `Add FreeCAD launcher and pytest fixture` |

**Include:**

```
framework/app/freecad_launcher.py
framework/utils/paths.py
framework/utils/waits.py
tests/conftest.py
tests/junior/test_01_launch_freecad.py
```

Use the **Week 4 version** of `test_01` (3 startup tests, no menu/screenshot tests yet). If only the final file exists in lab, copy from lab commit `65f0190` or remove Week 5+ tests manually so only launch tests remain.

**Verify:**

```powershell
pytest tests/junior/test_01_launch_freecad.py -v
```

---

### Week 5 — Pywinauto Part 2

| Field | Value |
|-------|-------|
| **Branch** | `feature/week05-ui-page-objects` |
| **MR title** | `Week 5: UI page objects and viewport capture` |
| **Commit message** | `Add UI page objects and viewport screenshot checks` |

**Include:**

```
framework/ui/main_window.py             # final: manual select_menu() — section 4.6
framework/ui/viewport.py                # final: menu-based view helpers — section 4.6
framework/ui/dialogs.py
framework/assertions/image_assertions.py
tests/junior/test_01_launch_freecad.py    # full Week 5 version with menu + screenshot tests
```

**Verify:**

```powershell
pytest tests/junior/test_01_launch_freecad.py -v
```

---

### Week 6 — Git Fundamentals

| Field | Value |
|-------|-------|
| **Branch** | `feature/week06-git-fundamentals` |
| **MR title** | `Week 6: Git fundamentals evidence` |
| **Commit message** | `Add Git task evidence and merge conflict demo` |

**Include:**

```
week06_git/conflict_demo.txt
docs/git-evidence/task02_git_branch.txt
docs/git-evidence/task03_git_log.txt
docs/git-evidence/task05_pr_link.txt
```

Update `task05_pr_link.txt` to point to **this GitLab MR** after creation (or the actual MR URL for Week 6).

**Verify:** Files exist and are readable. No pytest required.

**MR body:**

```markdown
## Summary
- Added Git branch and log evidence (tasks 2–3)
- Added merge conflict demo file (task 7)
- PR link recorded in docs/git-evidence

## Testing
Manual review of docs/git-evidence/*.txt
```

---

### Week 7 — J1 + J2

| Field | Value |
|-------|-------|
| **Branch** | `feature/week07-j1-j2-tests` |
| **MR title** | `Week 7: Startup and document creation tests (J1, J2)` |
| **Commit message** | `Add J1 startup and J2 document creation tests` |

**Include:**

```
tests/junior/test_01_launch_freecad.py    # J1 full — 6 tests
tests/junior/test_02_create_document.py
tests/conftest.py                         # launched_freecad, main_window, document_window fixtures
framework/ui/main_window.py               # create_new_document, get_model_tree_items
framework/ui/dialogs.py                   # optional main_window — required for DialogHelper(launcher.app)
```

**Verify:**

```powershell
pytest tests/junior/test_01_launch_freecad.py tests/junior/test_02_create_document.py -v
```

---

### Week 8 — J3 + J4

| Field | Value |
|-------|-------|
| **Branch** | `feature/week08-j3-j4-tests` |
| **MR title** | `Week 8: Viewport screenshot and tolerance tests (J3, J4)` |
| **Commit message** | `Add viewport screenshot and geometry tolerance tests` |

**Include:**

```
models/sample_box.FCStd
scripts/create_sample_box.py              # relative output path — section 4.6
framework/app/freecad_api.py
framework/assertions/geometry_assertions.py
framework/app/freecad_launcher.py         # open_path support
framework/ui/main_window.py               # find_tree_item, show_tree_item — section 4.6
framework/ui/viewport.py                  # menu-based prepare_for_screenshot — section 4.6
tests/junior/test_03_viewport_screenshot.py   # includes show_tree_item("box")
tests/junior/test_04_tolerance_check.py
tests/conftest.py                         # model_window fixture
```

**Verify:**

```powershell
pytest tests/junior/test_03_viewport_screenshot.py tests/junior/test_04_tolerance_check.py -v
```

---

### Week 9 — J5 E2E

| Field | Value |
|-------|-------|
| **Branch** | `feature/week09-j5-e2e` |
| **MR title** | `Week 9: Junior E2E test (J5)` |
| **Commit message** | `Add junior end-to-end workflow test` |

**Include:**

```
tests/junior/test_05_e2e_junior.py        # includes show_tree_item("Cube") — section 4.6
framework/app/freecad_api.py              # create_box_and_save, save_document_copy
framework/ui/dialogs.py                   # save_document_as (win32); optional main_window
framework/ui/main_window.py             # save_document_as wrapper; show_tree_item
framework/ui/viewport.py                  # if not already from Week 8
```

**Verify:**

```powershell
pytest tests/junior/test_05_e2e_junior.py -v
```

---

### Week 10 — Debugging Tools

| Field | Value |
|-------|-------|
| **Branch** | `feature/week10-debugging-tools` |
| **MR title** | `Week 10: Debugging tools and Save As fix` |
| **Commit message** | `Add debugging checklist, logging, and UI inspection helpers` |

**Include:**

```
docs/debugging/DEBUGGING_CHECKLIST.md
docs/debugging/save-as-root-cause.md
framework/utils/logging_config.py         # _sandbox_logging_configured flag — section 4.6
framework/utils/ui_inspect.py
scripts/_bootstrap.py
scripts/py_inspect_tree.py
.vscode/launch.json
framework/app/freecad_launcher.py         # logging lines only (full file)
framework/ui/dialogs.py                   # logging lines (full file)
tests/conftest.py                         # setup_logging autouse
pytest.ini                                # log_cli_level
```

**Verify:**

```powershell
pytest tests/junior/test_00_basics.py -v
python scripts/py_inspect_tree.py --help
```

---

### Week 11 — Junior Consolidation

| Field | Value |
|-------|-------|
| **Branch** | `feature/week11-junior-consolidation` |
| **MR title** | `Week 11: Junior consolidation and documentation` |
| **Commit message** | `Update README and add junior evidence package` |

**Include:**

```
README.md                                 # use docs/internal/README.gitlab.md → copy as README.md
docs/junior/JUNIOR_EVIDENCE.md
docs/junior/ANTI_PATTERNS_REVIEW.md
```

**Verify:**

```powershell
pytest tests/junior/ -v
# Expected: 23 passed in ~50–90s (FreeCAD GUI required)
```

After Week 11 MR merges, the GitLab repo should match lab `main` at `649ef49+` for all framework/test paths.

---

## 7. GitLab README

For Week 1 and Week 11, use the clean README at:

```
docs/internal/README.gitlab.md   (in lab repo)
```

Copy it to `README.md` in the GitLab repo. It has no references to PROGRESS, ARTIFACTS, Cursor, or internal guides.

---

## 8. End-to-end workflow (manual — CloudCode)

Execute weeks in order. Adjust `$GL` and `$LAB` paths. **Every step is manual** — no CI, no mirror, no background sync.

```powershell
$LAB = "C:\work\sandbox-lab"
$GL  = "C:\work\sandbox-gitlab"

# Optional: refresh lab from GitHub (only when Artem says lab was updated)
# cd $LAB; git fetch origin; git pull origin main

# Example: Week 7
cd $GL
git checkout main
git pull origin main          # GitLab main — manual
git checkout -b feature/week07-j1-j2-tests

Copy-WeekFiles -LabRoot $LAB -GitLabRoot $GL -RelativePaths @(
    "tests/junior/test_01_launch_freecad.py",
    "tests/junior/test_02_create_document.py",
    "tests/conftest.py",
    "framework/ui/main_window.py"
)

cd $GL
venv\Scripts\activate
pytest tests/junior/test_01_launch_freecad.py tests/junior/test_02_create_document.py -v

git add tests/junior/test_01_launch_freecad.py tests/junior/test_02_create_document.py tests/conftest.py framework/ui/main_window.py
git commit -m "Add J1 startup and J2 document creation tests"
git push -u origin feature/week07-j1-j2-tests
```

Then open GitLab → **Create merge request** → assign to SME (Ievhenii Kadenchuk) → paste MR body from section 6.

Repeat for Weeks 1–11 following the schedule in section 4.4.

---

## 9. SME notification template

After each MR is created, Artem sends:

```
Hi Ievhenii,

Week [N] — [topic] — ready for review.

GitLab MR: [URL]

What was done:
- [bullet 1]
- [bullet 2]

Tests: [command]

Thanks,
Artem
```

---

## 10. Troubleshooting

| Problem | Action |
|---------|--------|
| Week 4/5 `test_01` has too many tests | Check out file from specific lab commit (`65f0190` = Week 4, `ecd4d6b` = Week 5) |
| `TypeError: DialogHelper.__init__()` missing `main_window` | Copy post-fix `framework/ui/dialogs.py` from lab `main` (section 4.6) |
| J3/J5 screenshots show empty viewport | Ensure `show_tree_item()` in test + `main_window.py` from section 4.6 |
| `IndexError` in `menu_select` | Use final `main_window.select_menu()` — manual menu clicks (section 4.6) |
| `artifacts/logs/sandbox.log` empty under pytest | Copy post-fix `framework/utils/logging_config.py` (section 4.6) |
| FreeCAD not found | Set path in `freecad_launcher.py` or install from Company Portal |
| GitLab push denied | Check token / SSH key and branch protection rules |
| Accidentally copied `docs/PROGRESS.md` | `git reset`, remove file, recommit |
| MR diff too large | Expected for cumulative weeks — MR title/body must explain scope |
| Full junior suite not 23 passed | Manually `git pull` in `$LAB`; rerun `pytest tests/junior/ -v` |
| Full project not 40 passed | `pytest tests/ -v` locally; Middle GUI tests need FreeCAD |
| Lab repo out of date on AMC | Artem pushes GitHub from home → then manually `git pull` in `C:\work\sandbox-lab` on AMC |

---

## 11. Weeks 12–18 (Middle track + final)

Same rules as Weeks 1–11: **manual** copy from `$LAB`, cumulative MRs, no lab-only paths (section 4.1).

### Week 12 — Junior SME Review

| Field | Value |
|-------|-------|
| **Branch** | `feature/week12-junior-signoff` |
| **MR title** | `Week 12: Junior track ready for SME sign-off` |
| **Commit message** | `Confirm junior evidence package for SME review` |

**Include:** no new code required if Weeks 1–11 merged. Optional touch-up:

```
docs/junior/JUNIOR_EVIDENCE.md
docs/junior/ANTI_PATTERNS_REVIEW.md
README.md                                 # final from README.gitlab.md if not done in Week 11
```

**Verify:** `pytest tests/junior/ -v` → 23 passed.

**MR body:** Request SME sign-off on Junior track; link evidence docs.

---

### Week 13 — M1 Preferences

| Field | Value |
|-------|-------|
| **Branch** | `feature/week13-m1-preferences` |
| **MR title** | `Week 13: Preferences dialog tests (M1)` |
| **Commit message** | `Add Preferences panel tests and page object` |

**Include:**

```
framework/ui/preferences.py               # in-window panel on FreeCAD 1.1 — not Windows Settings
tests/middle/test_01_preferences.py
```

**Note:** FreeCAD 1.1 opens Preferences **inside the main window** (Edit → Preferences). Do not search desktop windows titled "Settings" — that opens Windows OS Settings.

**Verify:** `pytest tests/middle/test_01_preferences.py -v`

---

### Week 14 — M3 CAD API

| Field | Value |
|-------|-------|
| **Branch** | `feature/week14-m3-cad-api` |
| **MR title** | `Week 14: CAD API geometry tests (M3)` |
| **Commit message** | `Add middle CAD API tests and saved model` |

**Include:**

```
framework/app/freecad_api.py              # read_bounding_box_from_model, create_box_in_document
tests/middle/test_03_cad_api.py
models/middle_api_box.FCStd
```

**Verify:** `pytest tests/middle/test_03_cad_api.py -v`

---

### Week 15 — M4 Geometry + M5 Baselines

| Field | Value |
|-------|-------|
| **Branch** | `feature/week15-m4-m5-viewport` |
| **MR title** | `Week 15: Geometry validation and viewport baselines (M4, M5)` |
| **Commit message** | `Add geometry validation and baseline screenshot compare` |

**Include:**

```
framework/assertions/geometry_assertions.py   # assert_volume_close
framework/assertions/image_assertions.py      # assert_image_matches_baseline, image_diff_ratio
tests/middle/test_04_geometry_validation.py
tests/middle/test_05_deterministic_viewport.py
baselines/viewport_sample_box_front.png
```

**Verify:**

```powershell
pytest tests/middle/test_04_geometry_validation.py tests/middle/test_05_deterministic_viewport.py -v
```

If baseline missing on AMC laptop (first time only):

```powershell
$env:GENERATE_BASELINE = "1"
pytest tests/middle/test_05_deterministic_viewport.py::test_viewport_matches_baseline -v
git add baselines/viewport_sample_box_front.png
```

---

### Week 16 — M2 Dialog Stability

| Field | Value |
|-------|-------|
| **Branch** | `feature/week16-m2-stability` |
| **MR title** | `Week 16: Preferences dialog stability (M2)` |
| **Commit message** | `Add five-run Preferences stability test` |

**Include:**

```
framework/config.py                       # stability_run_count, baseline_max_diff_ratio
tests/middle/test_02_dialog_stability.py
docs/debugging/flakiness-preferences.md
```

**Verify:** `pytest tests/middle/test_02_dialog_stability.py -v` → 5 passed

---

### Week 17 — Config + CI/CD

| Field | Value |
|-------|-------|
| **Branch** | `feature/week17-cicd` |
| **MR title** | `Week 17: Project config and CI smoke workflow` |
| **Commit message** | `Add sandbox config and GitHub Actions smoke tests` |

**Include:**

```
framework/config.py
.github/workflows/pytest.yml              # smoke job only — NOT gitlab-mirror-sync.yml
docs/cicd/CI_NOTES.md
```

**Do NOT include:** `.github/workflows/gitlab-mirror-sync.yml`, `.github/GITLAB_SYNC_GUIDE.md` (lab automation only).

**Verify:**

```powershell
pytest tests/junior/test_00_basics.py tests/middle/test_03_cad_api.py -v
```

Push to GitHub and attach green Actions run screenshot to MR (or run workflow on GitLab if mirrored).

---

### Week 18 — M6 E2E + AI Evidence

| Field | Value |
|-------|-------|
| **Branch** | `feature/week18-middle-e2e-ai` |
| **MR title** | `Week 18: Middle E2E and AI-assisted engineering evidence` |
| **Commit message** | `Add middle E2E test and AI evidence package` |

**Include:**

```
tests/middle/test_06_e2e_middle.py
docs/middle/MIDDLE_EVIDENCE.md
docs/ai-evidence/README.md
docs/ai-evidence/AI-J1-test-scenario.md
docs/ai-evidence/AI-J2-helper-review.md
docs/ai-evidence/AI-J3-code-explanation.md
docs/ai-evidence/AI-J4-failure-analysis.md
README.md                                 # final README.gitlab.md — middle + CI sections
```

**Verify:**

```powershell
pytest tests/ -v
```

Expected: **40 passed** (23 junior + 17 middle).

---

## 12. MR schedule Weeks 12–18

| MR | Program dates | Suggested submit |
|----|---------------|------------------|
| Week 12 | Sep 15 – 21 | After Week 11 SME merge |
| Week 13 | Sep 22 – 28 | +1 week |
| Week 14 | Sep 29 – Oct 5 | +1 week |
| Week 15 | Oct 6 – 12 | +1 week |
| Week 16 | Oct 13 – 19 | +1 week |
| Week 17 | Oct 20 – 26 | +1 week |
| Week 18 | Oct 27 – Nov 2 | +1 week (program soft deadline Nov 1) |

---

## 13. Program complete

After Week 18 MR merges:

- Final evidence: `docs/junior/JUNIOR_EVIDENCE.md` + `docs/middle/MIDDLE_EVIDENCE.md` + `docs/ai-evidence/`
- Full local verify: `pytest tests/ -v` → 40 passed
- SME final review on GitLab `main`

---

*This file is for internal/lab use only. Do not copy to the GitLab submission repo.*
