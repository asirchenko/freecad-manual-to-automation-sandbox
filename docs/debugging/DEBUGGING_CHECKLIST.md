# Debugging Workflow Checklist

Program reference: *Sandbox Desktop Testing* docx section **6.3**.

Use this order when a UI or API test fails. Do not skip steps.

| Step | Question | Tools / where to look |
|------|----------|----------------------|
| 1 | **Assertion message** — what exactly failed? | pytest `-v --tb=long`; read the assert line and message |
| 2 | **Locator correctness** — is the control ID/title/class still valid? | Inspect.exe, `scripts/py_inspect_tree.py`, `framework/utils/ui_inspect.py` |
| 3 | **Trace details** — full stack and framework logs? | `artifacts/logs/sandbox.log`; pytest `--log-cli-level=DEBUG` |
| 4 | **Screenshots / videos** — visual state at failure? | `artifacts/*.png`; add `viewport.capture_to_file()` before assert |
| 5 | **Network / requests** — external calls involved? | Usually N/A for FreeCAD desktop; check if test uses HTTP |
| 6 | **Test data / environment** — model file, FreeCAD path, Qt backend? | `models/`, `FreeCADLauncher` exe path, UIA vs win32 |
| 7 | **Prior test state** — order dependency or shared fixture? | pytest fixtures scope; run failing test alone with `-k` |

## Quick commands

```powershell
cd freecad-manual-to-automation-sandbox
venv\Scripts\activate

# Single test with long traceback
pytest tests/junior/test_02_create_document.py -v --tb=long -k j2

# Console logs from framework
pytest tests/junior/test_01_launch_freecad.py -v -s --log-cli-level=INFO

# Dump control tree while FreeCAD is open
python scripts/py_inspect_tree.py --depth 2 --backend both

# VS Code: Run and Debug -> "Pytest: current file"
```

## Inspect.exe (Windows SDK)

1. Start FreeCAD and reach the UI state you need to automate.
2. Run **Inspect.exe** (Windows SDK) or **Accessibility Insights**.
3. Hover the target control — note **Name**, **ControlType**, **ClassName**, **AutomationId**.
4. Compare with pywinauto locator in code (`child_window`, `descendants`, keyboard shortcut).
5. If UIA shows nothing for a Qt widget, try **win32** backend (see [save-as-root-cause.md](save-as-root-cause.md)).

## pywinauto print_control_identifiers

```python
main_window.print_control_identifiers(depth=2)
```

Equivalent helper: `framework.utils.ui_inspect.print_descendants(root, max_depth=2)`.

## Logging

- Framework modules log to **`artifacts/logs/sandbox.log`** when `setup_logging()` runs (pytest session in `conftest.py`).
- Log lines include module name: `framework.app.freecad_launcher`, `framework.ui.dialogs`, etc.

## VS Code debugger

`.vscode/launch.json` includes:

- **Pytest: current file** — breakpoint in test or framework code
- **Pytest: junior tests** — full junior suite
- **Script: py_inspect_tree** — step through tree dump script

Set breakpoints in `framework/ui/main_window.py` or `tests/conftest.py` to inspect fixture state.

## Document the fix

After root cause is found, write a short doc under `docs/debugging/` using the checklist sections.  
Example: [save-as-root-cause.md](save-as-root-cause.md).
