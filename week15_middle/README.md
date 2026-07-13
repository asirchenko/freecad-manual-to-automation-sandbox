# Week 15 — M4 Geometry + M5 Baselines

**Deliverables:** `test_04_geometry_validation.py`, `test_05_deterministic_viewport.py`, `baselines/viewport_sample_box_front.png`

```powershell
pytest tests/middle/test_04_geometry_validation.py tests/middle/test_05_deterministic_viewport.py -v
```

Generate baseline once:

```powershell
$env:GENERATE_BASELINE="1"
pytest tests/middle/test_05_deterministic_viewport.py::test_viewport_matches_baseline -v
```
