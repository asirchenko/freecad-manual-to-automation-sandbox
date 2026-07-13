# Junior Track — Evidence Package (J1–J5)

Checklist for Week 11 consolidation and Week 12 SME review.

## Test files

| Task | File | Tests | GUI required |
|------|------|-------|--------------|
| — | `test_00_basics.py` | 7 | No |
| J1 | `test_01_launch_freecad.py` | 6 | Yes |
| J2 | `test_02_create_document.py` | 3 | Yes |
| J3 | `test_03_viewport_screenshot.py` | 3 | Yes |
| J4 | `test_04_tolerance_check.py` | 3 | No |
| J5 | `test_05_e2e_junior.py` | 1 | Yes (partial API) |

**Total:** 23 junior tests.

## Run all Junior tests

```powershell
cd freecad-manual-to-automation-sandbox
venv\Scripts\activate

# Unit + API (no FreeCAD GUI)
pytest tests/junior/test_00_basics.py tests/junior/test_04_tolerance_check.py -v

# Full junior suite (FreeCAD GUI required)
pytest tests/junior/ -v
```

Expected: **23 passed** (~1–2 min with GUI tests).

## Artifacts produced by tests

| Artifact | Test | In git |
|----------|------|--------|
| `artifacts/j1_startup_screenshot.png` | J1 | No |
| `artifacts/j2_create_document_screenshot.png` | J2 | No |
| `artifacts/j3_viewport_sample_box.png` | J3 | No |
| `artifacts/j5_e2e_geometry.FCStd` | J5 | No |
| `artifacts/j5_e2e_viewport.png` | J5 | No |
| `artifacts/j5_e2e_saved.FCStd` | J5 | No |

Prepared model: `models/sample_box.FCStd` (in git).

Full registry: [docs/ARTIFACTS.md](../ARTIFACTS.md).

## Framework modules used

| Module | Role |
|--------|------|
| `framework/app/freecad_launcher.py` | UI launch, open model |
| `framework/app/freecad_api.py` | Headless geometry + save |
| `framework/ui/main_window.py` | Menus, toolbar, model tree |
| `framework/ui/viewport.py` | Screenshots |
| `framework/ui/dialogs.py` | OK dismiss, Save As (win32) |
| `framework/assertions/image_assertions.py` | Pillow checks |
| `framework/assertions/geometry_assertions.py` | Tolerance checks |
| `framework/utils/waits.py` | Sync helpers |
| `tests/conftest.py` | Shared fixtures |

## Documentation index

| Doc | Purpose |
|-----|---------|
| [README.md](../../README.md) | Entry point, quick start, strategy |
| [docs/PROGRESS.md](../PROGRESS.md) | Week-by-week log |
| [docs/ARTIFACTS.md](../ARTIFACTS.md) | Files and artifacts per week |
| [docs/debugging/DEBUGGING_CHECKLIST.md](../debugging/DEBUGGING_CHECKLIST.md) | Week 10 debugging |
| [docs/junior/ANTI_PATTERNS_REVIEW.md](ANTI_PATTERNS_REVIEW.md) | Week 11 self-review |

## Week 1 evidence (still in git)

- `artifacts/week01/freecad_running.png`
