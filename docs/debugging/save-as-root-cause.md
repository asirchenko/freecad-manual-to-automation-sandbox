# Root Cause: Save As Dialog Not Found (UIA)

**Week:** 10 — Debugging Tools  
**Symptom:** pywinauto could not automate File → Save As; J5 initially used API-only save.  
**Fix:** `framework/ui/dialogs.py` — `Ctrl+Shift+S` + win32 `#32770` dialog  
**Status:** Fixed and verified (`artifacts/ui_save_test.FCStd` in local runs)

---

## 1. Assertion / error message

Typical failures:

```
TimeoutError: Save As dialog 'Save FreeCAD Document' (#32770) not found.
```

```
pywinauto timings.TimeoutError  # menu_select('File->Save As')
COMError  # UIA menu_select on Qt menu bar
```

The test or script expected a Save dialog handle; UIA `Desktop` listed no matching window.

---

## 2. Locator correctness

| Approach | Result |
|----------|--------|
| `main_window.menu_select('File->Save As')` | COM / UIA errors on FreeCAD Qt menus |
| `Desktop(backend='uia').window(title_re='.*Save.*')` | No match — dialog not exposed under UIA |
| `Desktop(backend='win32').window(title='Save FreeCAD Document')` | Multiple windows with same title |
| **win32 class `#32770`** with Save button | **Correct** native Save dialog |

**Inspect / py_inspect findings:**

- Dialog title: `Save FreeCAD Document`
- Class: `#32770` (standard Windows file dialog)
- Empty Qt wrapper window may share the title — filter by class and `&Save` button

**Working locators:** see `DialogHelper.wait_save_as_dialog()` and `save_document_as()` in `framework/ui/dialogs.py`.

---

## 3. Trace details

Debug script: `scripts/debug_save_as_dialog.py`

Steps recorded:

1. Launch with `sample_box.FCStd`
2. List UIA top windows before/after Save As trigger
3. Try File menu click path vs keyboard

Logs written to console; Week 10 adds `artifacts/logs/sandbox.log` for framework modules.

Key trace insight: failure was at **dialog discovery**, not at filename entry or save click.

---

## 4. Screenshots / visual evidence

- Viewport screenshots (`artifacts/j5_e2e_viewport.png`) confirmed main window state was correct.
- Save As dialog is a **separate native window** — main window screenshot does not include dialog controls.
- Manual observation: dialog **does appear** for the user; automation backend was wrong.

---

## 5. Network / requests

Not applicable — local desktop UI only.

---

## 6. Test data / environment state

| Factor | Impact |
|--------|--------|
| FreeCAD 1.1.1 + Qt | Menus partially visible under UIA; native dialogs use win32 |
| Dual MenuBar in FreeCAD | Must pick bar with most items (already fixed in Week 5) |
| Keyboard shortcut | `Ctrl+Shift+S` opens Save As reliably vs menu COM path |
| Backend separation | `Application(backend='uia')` and `Application(backend='win32')` on same PID |

---

## 7. Dependency on prior test state

- Save As debugging used **fresh launch** with `sample_box.FCStd` — no ordering dependency.
- J5 E2E used API save to avoid flaky UI step; UI path is now available for future tests.

---

## Fix summary

1. Open Save As via **`Ctrl+Shift+S`** (primary) or File menu click (fallback).
2. Connect **win32** backend to the same FreeCAD PID.
3. Wait for `#32770` dialog titled `Save FreeCAD Document` with a **Save** button.
4. Set filename via `Edit` / `ComboBox` child; click `&Save`.
5. `wait_until` for output file on disk.

**Program alignment:** UI layer (pywinauto) + API layer (`freecadcmd`) split from Plan.md — J5 may keep API save; UI Save As is implemented for M-track and future tests.

---

## How to verify

```powershell
venv\Scripts\activate
python scripts/debug_save_as_dialog.py
python scripts/py_inspect_tree.py --backend win32 --depth 1
# Manual: DialogHelper.save_document_as(path) via a short script or future test
```

See also: [DEBUGGING_CHECKLIST.md](DEBUGGING_CHECKLIST.md), `week09_tests/README.md`.
