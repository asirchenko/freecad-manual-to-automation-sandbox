# Week 10 — Debugging Tools

**Topics:** Inspect.exe, py_inspect, logging, VS Code debugger, debugging checklist  
**Deliverables:** root cause doc + fix, logging utilities, debug scripts

## What was added

| Path | Purpose |
|------|---------|
| `docs/debugging/DEBUGGING_CHECKLIST.md` | 7-step workflow (docx 6.3) |
| `docs/debugging/save-as-root-cause.md` | Root cause analysis — Save As / UIA vs win32 |
| `framework/utils/logging_config.py` | Console + file logging setup |
| `framework/utils/ui_inspect.py` | Control tree dump helpers |
| `scripts/py_inspect_tree.py` | CLI to inspect FreeCAD UI |
| `.vscode/launch.json` | Pytest and script debug configurations |

## Debugging workflow (summary)

1. Read the **assertion message** (`pytest --tb=long`)
2. Verify **locators** with Inspect.exe or `py_inspect_tree.py`
3. Check **logs** in `artifacts/logs/sandbox.log`
4. Capture **screenshots** under `artifacts/` if UI state is unclear
5. Confirm **environment** (FreeCAD path, model file, UIA vs win32)
6. Run the **failing test alone** (`pytest -k test_name`) to rule out order deps
7. Document fix in `docs/debugging/`

Full checklist: [docs/debugging/DEBUGGING_CHECKLIST.md](../docs/debugging/DEBUGGING_CHECKLIST.md)

## Run

**Working directory:** project root `freecad-manual-to-automation-sandbox` (you are already there if the prompt shows that path — do not `cd` into it twice).

```powershell
venv\Scripts\activate
python scripts/py_inspect_tree.py --depth 2 --backend both
```

# Tests with logging visible
pytest tests/junior/test_01_launch_freecad.py -v -s --log-cli-level=INFO

# VS Code: F5 -> "Pytest: current file" (breakpoint in test or framework)
```

Log file (after pytest or framework use): `artifacts/logs/sandbox.log`

## Root cause case study

Save As automation failure during Junior track — documented and fixed:

- [docs/debugging/save-as-root-cause.md](../docs/debugging/save-as-root-cause.md)
- Fix in `framework/ui/dialogs.py`

## Next week

**Week 11:** Junior consolidation — cleanup, README, anti-patterns review.

Progress: [docs/PROGRESS.md](../docs/PROGRESS.md)  
Artifacts: [docs/ARTIFACTS.md](../docs/ARTIFACTS.md)
