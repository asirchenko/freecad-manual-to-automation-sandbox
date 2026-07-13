# Week 7 — Create Tests J1 + J2

**Deliverables:** full J1 startup verification, J2 document creation tests

## J1 — `test_01_launch_freecad.py`

| Test | Checks |
|------|--------|
| process starts | FreeCAD running |
| window visible | Main window enabled |
| window title | Contains `FreeCAD` |
| menu bar | `File` menu present |
| toolbar | `New Document` button present |
| **J1 screenshot** | `artifacts/j1_startup_screenshot.png` |

## J2 — `test_02_create_document.py`

| Test | Checks |
|------|--------|
| window title | Contains `Unnamed` after new document |
| model tree | `Unnamed` listed in TreeItem controls |
| **J2 screenshot** | `artifacts/j2_create_document_screenshot.png` |

## MainWindow API added

- `create_new_document()` — clicks toolbar **New Document**
- `get_model_tree_items()` — reads model tree labels
- `toolbar_has_button()` / `find_toolbar_button()`

## Run tests

```powershell
venv\Scripts\activate
pytest tests/junior/test_01_launch_freecad.py -v
pytest tests/junior/test_02_create_document.py -v
```

Expected: **6 + 3 = 9 passed** (local, FreeCAD required).

Fixtures `launched_freecad`, `main_window`, `document_window` live in `tests/conftest.py`.

Progress log: [docs/PROGRESS.md](../docs/PROGRESS.md)
