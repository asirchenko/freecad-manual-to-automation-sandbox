# Week 3 — Python Part 2

**Topics:** lists, dict, exceptions, modules, pytest  
**Deliverable:** `tests/junior/test_00_basics.py` (3+ tests)

## Concepts

| Topic | Where | Example |
|-------|-------|---------|
| Lists | `parse_menu_path`, `merge_tags` | `["File", "New"]` |
| Dict | `get_launch_config`, `filter_passed` | `config["timeout_sec"]` |
| Exceptions | `safe_int` + `pytest.raises` | invalid string → `ValueError` |
| Modules | `framework/utils/basics.py` | `from framework.utils.basics import ...` |
| Pytest | `tests/junior/test_00_basics.py` | classes, `assert`, `pytest.raises` |

## Run tests

```powershell
cd freecad-manual-to-automation-sandbox
venv\Scripts\activate
pytest tests/junior/test_00_basics.py -v
```

Expected: **7 passed**.

## File map

- `framework/utils/basics.py` — reusable helpers (module import practice)
- `tests/junior/test_00_basics.py` — pytest tests grouped by topic

## Try it yourself

1. Add a new helper in `basics.py`, e.g. `count_failures(results)`.
2. Add a test in `test_00_basics.py` for that helper.
3. Run pytest and confirm green.

## Next week

**Week 4:** Pywinauto — `framework/app/freecad_launcher.py` and `freecad_app` fixture in `conftest.py`.

Progress log: [docs/PROGRESS.md](../docs/PROGRESS.md)
