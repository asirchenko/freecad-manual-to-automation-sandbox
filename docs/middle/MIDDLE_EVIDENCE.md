# Middle Track — Evidence Package (M1–M6)

Checklist for Week 18 consolidation and SME review.

## Test files

| Task | File | Tests | GUI required |
|------|------|-------|--------------|
| M1 | `test_01_preferences.py` | 3 | Yes |
| M2 | `test_02_dialog_stability.py` | 5 | Yes |
| M3 | `test_03_cad_api.py` | 3 | No |
| M4 | `test_04_geometry_validation.py` | 3 | No |
| M5 | `test_05_deterministic_viewport.py` | 2 | Yes |
| M6 | `test_06_e2e_middle.py` | 1 | Yes |

**Total:** 17 middle tests.

## Run commands

```powershell
# API / geometry only (no GUI)
pytest tests/middle/test_03_cad_api.py tests/middle/test_04_geometry_validation.py -v

# Full middle suite
pytest tests/middle/ -v

# Full project
pytest tests/ -v
```

## Key artifacts

| Path | Task |
|------|------|
| `models/middle_api_box.FCStd` | M3 |
| `baselines/viewport_sample_box_front.png` | M5 |
| `.github/workflows/pytest.yml` | Week 17 CI |
| `docs/ai-evidence/` | Week 18 AI tasks |

## CI

Cloud smoke job runs non-GUI tests only. See `docs/cicd/CI_NOTES.md`.
