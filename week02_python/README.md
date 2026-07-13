# Week 2 — Python Part 1

**Topics:** variables, conditions, loops, functions  
**Goal:** Core Python before pytest and pywinauto (Weeks 3–4).

## How to run

```powershell
cd freecad-manual-to-automation-sandbox
venv\Scripts\activate
python week02_python/01_variables.py
python week02_python/02_conditions.py
python week02_python/03_loops.py
python week02_python/04_functions.py
python week02_python/05_practice.py
```

Or run everything at once:

```powershell
python week02_python/run_all.py
```

## Files

| File | Topic | What you learn |
|------|-------|----------------|
| `01_variables.py` | Variables | str, int, float, bool, f-strings |
| `02_conditions.py` | Conditions | if / elif / else, comparisons, logic |
| `03_loops.py` | Loops | for, while, break, range |
| `04_functions.py` | Functions | def, return, parameters, type hints |
| `05_practice.py` | Practice | Mini smoke-check scenario |
| `run_all.py` | Runner | Executes all exercises in order |

## Hands-on practice

Each file ends with a `# YOUR TURN` block. Change the code and run again.  
Ask in Cursor if anything is unclear, e.g. "explain line X in 02_conditions.py".

## Link to automation

Examples use familiar concepts: app name, FreeCAD path, test status, timeout.  
This makes the jump to Week 4 (`freecad_launcher.py`) easier.

## Week 2 checklist

- [ ] Ran all 5 files without errors
- [ ] Understand the difference between `=` and `==`
- [ ] Can write a simple function with `return`
- [ ] Completed at least one YOUR TURN block

## Next week

**Week 3:** lists, dict, exceptions, modules → `tests/junior/test_00_basics.py` (3+ pytest tests).

Full progress log: [docs/PROGRESS.md](../docs/PROGRESS.md)
