# CI/CD Notes (Week 17)

## Workflow

File: `.github/workflows/pytest.yml`

| Job | Runner | What runs |
|-----|--------|-----------|
| `smoke` | `windows-latest` | Junior unit/API + Middle API/geometry tests (no GUI) |

## Local vs CI

| Test group | Local (FreeCAD installed) | GitHub Actions cloud |
|------------|---------------------------|----------------------|
| `test_00_basics`, `test_04`, M3, M4 | Yes | Yes |
| Junior GUI (J1–J3, J5) | Yes | No — needs FreeCAD GUI |
| Middle GUI (M1, M2, M5, M6) | Yes | No — needs FreeCAD GUI |

Full UI suite on AMC laptop:

```powershell
venv\Scripts\activate
pytest tests/ -v
```

## Reading pipeline logs

1. GitHub → Actions → **Desktop Sandbox Tests**
2. Open the failed job → expand the pytest step
3. Distinguish:
   - **Test failure** — assertion or test code issue
   - **Environment** — missing FreeCAD, wrong Python path
   - **Infra** — runner timeout, checkout failure

## Evidence for SME

Attach a screenshot of a green `smoke` workflow run. Note in the MR that UI tests are verified locally.
