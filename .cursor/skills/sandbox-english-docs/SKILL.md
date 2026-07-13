---
name: sandbox-english-docs
description: >-
  Enforces English-only documentation and weekly progress updates for the
  FreeCAD sandbox project. Use when writing or editing README, docs/, comments
  in markdown, week summaries, SME messages, or when a week is completed.
---

# Sandbox Documentation Standards

## Language rule

**All project documentation must be written exclusively in English.**

This applies to:

- `README.md` and any `README.md` in subfolders
- `docs/` (including `PROGRESS.md`, `ai-evidence/`)
- Markdown files, docstrings in `.md` context, PR descriptions
- Code comments that explain workflow or learning goals (prefer English)
- Commit messages for this repo

**Not in scope:** casual chat with the user (any language), `Plan.md` in the parent Sandbox folder (personal plan, may stay Russian).

If existing docs are not in English, translate them when touched or when closing a week.

## Weekly progress tracking

After **each completed week**, update progress in **two places**:

1. **`docs/PROGRESS.md`** — canonical detailed log (required)
2. **`README.md`** — short "Program status" table with current week only (required)

### When to update

Update at the end of a week when:

- Deliverables for that week exist in the repo
- Exercises or tests run successfully
- The user says a week is done, or work for that week is committed

### `docs/PROGRESS.md` — what to add per week

For each week, append or update a section with:

```markdown
## Week N — [Topic]

**Status:** Done | In progress | Pending  
**Dates:** [program dates from Plan.md if known]

### Deliverables
- [ ] item 1
- [x] item 2

### What was done
- Bullet summary of files, features, evidence

### How to verify
\`\`\`powershell
# commands to reproduce
\`\`\`

### Notes
- Blockers, SME feedback, version quirks
```

Keep completed weeks unchanged except for corrections. Do not delete history.

### `README.md` — program status table

Keep a compact table (max one row per week group or current focus):

```markdown
## Program status

See [docs/PROGRESS.md](docs/PROGRESS.md) for the full week-by-week log.

| Week | Topic | Status |
|------|-------|--------|
| 1 | Environment Setup | Done |
| 2 | Python Part 1 | In progress |
```

Update statuses only; link to `PROGRESS.md` for details.

## End-of-week checklist

Copy and complete when closing a week:

```
Week N close-out:
- [ ] All new/changed docs are in English
- [ ] docs/PROGRESS.md updated (deliverables, verify steps, notes)
- [ ] README.md program status table updated
- [ ] Subfolder README (if any) in English
- [ ] No secrets in committed files
```

## File map

| File | Role |
|------|------|
| `docs/PROGRESS.md` | Full weekly log — primary tracking document |
| `README.md` | Entry point + short status + links |
| `week02_python/README.md` | Week-specific instructions (English) |
| `Plan.md` (parent folder) | Personal schedule — not repo documentation |

## Examples

**Good** — PROGRESS entry:

```markdown
## Week 2 — Python Part 1

**Status:** Done

### Deliverables
- [x] `week02_python/` exercises (variables, conditions, loops, functions)
- [x] `week02_python/README.md`

### How to verify
python week02_python/run_all.py
```

**Bad** — Russian in repo docs:

```markdown
## Week 2 — основы Python
Создайте переменную...
```

**Bad** — status only in chat, not in repo:

Week 2 finished but `PROGRESS.md` not updated.

## Agent behavior

When working on this sandbox:

1. Write new documentation in English by default.
2. After week work, propose or apply `PROGRESS.md` + `README.md` updates.
3. If user completes a week in chat, update tracking docs without being asked again.
4. Prefer `docs/PROGRESS.md` for detail; keep `README.md` scannable.
