# Merge conflict resolution — Week 6 Task 7

**File:** `week06_git/conflict_demo.txt`  
**Branches:** `feature/week06-git-fundamentals` ← `lab/main-update` (simulated main)

## Conflict type

`add/add` — both branches added the same file with different content.

## Resolution

Kept both lines (main first, then feature):

```
Main: updated program note
Feature: sandbox progress note
```

## Commands used

```powershell
git merge lab/main-update
# edit conflict_demo.txt — remove <<<<<<< ======= >>>>>>> markers
git add week06_git/conflict_demo.txt
git commit -m "week06: resolve merge conflict in conflict_demo.txt"
git branch -d lab/main-update
```

## Evidence

- Conflict markers visible in VS Code before save
- Merge commit in `git log --oneline`
