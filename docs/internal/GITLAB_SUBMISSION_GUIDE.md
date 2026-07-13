# GitLab SME Submission Guide (Weeks 1–11)

**Audience:** CloudCode agent on the AMC Bridge work laptop  
**Author:** Artem Sirchenko  
**Purpose:** Submit the sandbox to the assigned GitLab repo as **11 sequential Merge Requests** — one per program week. Each MR must look like normal VS Code + Copilot work, not an AI-assisted learning archive.

---

## 1. Two repositories — two roles

| Repo | URL pattern | Role |
|------|-------------|------|
| **GitHub (lab archive)** | `https://github.com/asirchenko/freecad-manual-to-automation-sandbox` | Full project: learning guides, progress logs, Cursor metadata. **Source of truth for file content.** |
| **GitLab (SME submission)** | `https://gitlab.amcbridge.com/<group>/<assigned-sandbox>.git` | Assigned AMC repo. **Only official deliverables.** SME reviews MRs here. |

**Do NOT** use the GitHub Actions `gitlab-mirror-sync` workflow for SME submission. That workflow squashes everything into a single neutral commit on `main` and strips `.github/`. SME expects **feature branches + MRs with reviewable history**.

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

## 3. Initial setup (run once)

### 3.1 Clone both repos

```powershell
# Lab archive (read-only source)
git clone https://github.com/asirchenko/freecad-manual-to-automation-sandbox.git C:\work\sandbox-lab
cd C:\work\sandbox-lab
git checkout main
git pull

# Assigned GitLab repo (submission target)
git clone https://gitlab.amcbridge.com/<group>/<assigned-sandbox>.git C:\work\sandbox-gitlab
cd C:\work\sandbox-gitlab
```

Set `$LAB  = "C:\work\sandbox-lab"` and `$GL   = "C:\work\sandbox-gitlab"` in your session if helpful.

### 3.2 Verify lab archive has Weeks 1–11

```powershell
cd C:\work\sandbox-lab
git log --oneline -15
pytest tests/junior/ --collect-only
```

Expected: junior tests `test_00` … `test_05` collect successfully; `models/sample_box.FCStd` exists.

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

1. `git checkout main && git pull`
2. `git checkout -b <branch-name>`
3. Copy files listed under **Include**
4. Run **Verify**
5. `git add` only included paths → commit → push → create MR

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
framework/ui/main_window.py
framework/ui/viewport.py
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
scripts/create_sample_box.py
framework/app/freecad_api.py
framework/assertions/geometry_assertions.py
framework/app/freecad_launcher.py         # open_path support
tests/junior/test_03_viewport_screenshot.py
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
tests/junior/test_05_e2e_junior.py
framework/app/freecad_api.py              # create_box_and_save, save_document_copy
framework/ui/dialogs.py                   # save_document_as (win32)
framework/ui/main_window.py               # save_document_as wrapper
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
framework/utils/logging_config.py
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
# Expected: 23 passed (FreeCAD required for GUI tests)
```

---

## 7. GitLab README

For Week 1 and Week 11, use the clean README at:

```
docs/internal/README.gitlab.md   (in lab repo)
```

Copy it to `README.md` in the GitLab repo. It has no references to PROGRESS, ARTIFACTS, Cursor, or internal guides.

---

## 8. End-to-end workflow script (CloudCode)

Execute weeks in order. Adjust `$GL` and `$LAB` paths.

```powershell
$LAB = "C:\work\sandbox-lab"
$GL  = "C:\work\sandbox-gitlab"

# Example: Week 7
cd $GL
git checkout main
git pull origin main
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
| FreeCAD not found | Set path in `freecad_launcher.py` or install from Company Portal |
| GitLab push denied | Check token / SSH key and branch protection rules |
| Accidentally copied `docs/PROGRESS.md` | `git reset`, remove file, recommit |
| MR diff too large | Expected for cumulative weeks — MR title/body must explain scope |

---

## 11. After Week 11

- Week 12: SME review and sign-off on final Junior state
- Weeks 13+: Middle track — continue in GitHub lab, submit to GitLab using the same pattern (new sections to be added to this guide)

---

*This file is for internal/lab use only. Do not copy to the GitLab submission repo.*
