# Week 6 — Git Fundamentals

**Program reference:** docx 5.3 Junior Stage 2 — seven Git tasks  
**Repo:** `freecad-manual-to-automation-sandbox` (GitHub / GHE assigned sandbox)

## Branch naming (team convention)

```
feature/<short-description>
```

Example for this week: `feature/week06-git-fundamentals`

## Task checklist

| # | Task | Command / action | Evidence |
|---|------|------------------|----------|
| 1 | Clone repo, open in VS Code | `git clone <url>`, `code .` | Project tree screenshot |
| 2 | Create feature branch | `git checkout -b feature/week06-git-fundamentals` | `git branch` output |
| 3 | Commit with meaningful messages | `git add`, `git commit -m "..."` | `git log --oneline` |
| 4 | Push to remote | `git push -u origin <branch>` | Branch on remote |
| 5 | Open Pull Request | GitHub/GHE UI or `gh pr create` | PR URL |
| 6 | Address review feedback | Update code, push, re-request review | Updated PR / comments |
| 7 | Pull main, resolve merge conflict | `git merge main` or `git pull origin main` | Resolved file + merge commit |

Evidence folder: [docs/git-evidence/](../docs/git-evidence/)

---

## Task 1 — Clone and open

```powershell
git clone https://github.com/asirchenko/freecad-manual-to-automation-sandbox.git
cd freecad-manual-to-automation-sandbox
code .
```

Verify remotes:

```powershell
git remote -v
```

---

## Task 2 — Feature branch

Always branch from updated `main`:

```powershell
git checkout main
git pull origin main
git checkout -b feature/week06-git-fundamentals
git branch
```

---

## Task 3 — Meaningful commits

**Good commit message format:**

```
Add Week 4 FreeCAD launcher and startup pytest fixture

- FreeCADLauncher connects via pywinauto UIA
- freecad_app fixture for tests
```

**Avoid:** `fix`, `update`, `changes`, `wip` without context.

Example sequence for Weeks 2–5:

```powershell
git add week02_python/
git commit -m "Add Week 2 Python Part 1 exercises"

git add framework/utils/basics.py tests/junior/test_00_basics.py week03_python/ pytest.ini
git commit -m "Add Week 3 pytest basics and framework helpers"

git add framework/app/ framework/utils/paths.py framework/utils/waits.py tests/conftest.py tests/junior/test_01_launch_freecad.py week04_pywinauto/
git commit -m "Add Week 4 FreeCAD launcher and UI startup tests"

git add framework/ui/ framework/assertions/image_assertions.py week05_pywinauto/
git commit -m "Add Week 5 UI page objects and viewport screenshot tests"
```

---

## Task 4 — Push

```powershell
git push -u origin feature/week06-git-fundamentals
```

Confirm on remote: repository → Branches.

---

## Task 5 — Pull Request

**PR title example:** `Week 2–5: Python fundamentals and Pywinauto startup tests`

**PR body template:**

```markdown
## Summary
- Week 2: Python exercises (variables, conditions, loops, functions)
- Week 3: pytest basics (7 unit tests)
- Week 4: FreeCAD launcher + startup UI tests
- Week 5: MainWindow page object, viewport capture, Pillow checks

## Testing
- pytest tests/junior/test_00_basics.py -v  → 7 passed
- pytest tests/junior/test_01_launch_freecad.py -v  → 5 passed (local, FreeCAD required)

## Outcome
Sandbox progress Weeks 2–5 ready for SME review.
```

CLI:

```powershell
gh pr create --title "Week 2-5: Python and Pywinauto fundamentals" --body-file docs/git-evidence/PR_BODY_WEEK06.md
```

---

## Task 6 — Review feedback

When SME comments on the PR:

1. Read each comment
2. Checkout the PR branch
3. Fix code or docs
4. Commit with reference: `Address review: clarify menu bar selection in MainWindow`
5. Push — PR updates automatically
6. Reply in PR thread what you changed

---

## Task 7 — Merge conflict lab

Practice conflict on file `week06_git/conflict_demo.txt` (does not affect production code).

### Step A — conflicting commits

```powershell
# On feature branch — first version
git checkout feature/week06-git-fundamentals
echo "Feature: sandbox progress note" > week06_git/conflict_demo.txt
git add week06_git/conflict_demo.txt
git commit -m "week06: add conflict demo on feature branch"

# Simulate main moving forward
git branch lab/main-update main
git checkout lab/main-update
echo "Main: updated program note" > week06_git/conflict_demo.txt
git add week06_git/conflict_demo.txt
git commit -m "week06: add conflicting update on main"

# Merge into feature → conflict
git checkout feature/week06-git-fundamentals
git merge lab/main-update
```

### Step B — resolve

Open `week06_git/conflict_demo.txt`, remove conflict markers, keep both lines:

```
Main: updated program note
Feature: sandbox progress note
```

```powershell
git add week06_git/conflict_demo.txt
git commit -m "week06: resolve merge conflict in conflict_demo.txt"
git branch -d lab/main-update
```

### Step C — evidence

- Screenshot of conflict markers in VS Code (before resolve)
- Screenshot or copy of resolved file
- `git log --oneline -5` showing merge commit

---

## Security

- Never commit passwords, tokens, or `Git Password.txt`
- Use Git credential manager or SSH for GHE
- `.gitignore` blocks `*password*`, `*credentials*`, `.env`

## Next week

**Week 7:** J1 + J2 — full startup and document creation tests.

Progress log: [docs/PROGRESS.md](../docs/PROGRESS.md)
