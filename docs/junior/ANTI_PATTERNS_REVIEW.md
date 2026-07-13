# Junior Track — Anti-Patterns Self-Review

**Week 11** — consolidation checklist against program guidance (*Sandbox Desktop Testing* docx + Plan.md).

Review date: program Week 11 (Sep 8–14, 2026).

| # | Anti-pattern | Status | Notes |
|---|--------------|--------|-------|
| 1 | **Hard sleeps in tests** instead of sync helpers | Pass | Tests use `wait_until` / `wait_for_value` in `framework/utils/waits.py`. Fixed delays only in UI layer (dialogs/viewport) where Qt needs settle time — not in test bodies. |
| 2 | **Tests depend on run order** | Pass | Each test file uses fixtures with explicit setup/teardown. J5 is one self-contained flow; no cross-file state. |
| 3 | **Geometry checks via UI clicks only** | Pass | J4 + J5 use `freecadcmd` / `FreeCADApiRunner`. UI covers launch, tree, viewport screenshot per Plan.md split. |
| 4 | **No teardown — FreeCAD left running** | Pass | `freecad_app`, `launched_freecad`, `model_window`, J5 `finally: launcher.close()`. |
| 5 | **Fragile paths** hard-coded in tests | Pass | `framework/utils/paths.py` — `artifact_path`, `model_path`, `PROJECT_ROOT`. |
| 6 | **Raw locators in every test** | Pass | Page objects: `MainWindow`, `Viewport`, `DialogHelper`, `FreeCADLauncher`. |
| 7 | **`menu_select` on Qt without fallback** | Pass (with note) | File menu uses click + keyboard shortcuts; Save As uses `Ctrl+Shift+S` + win32 `#32770`. See [save-as-root-cause.md](../debugging/save-as-root-cause.md). |
| 8 | **Secrets or credentials in repo** | Pass | `.gitignore` blocks `.env`, passwords; no creds committed. |
| 9 | **Empty or vague assert messages** | Pass | Assertions include context (`Missing artifact`, `Model tree should not be empty`, etc.). |
| 10 | **Appendix B layout violated** | Pass | `framework/`, `tests/junior/test_00…05`, `models/`, stubs in `tests/middle/` for Weeks 13+. |
| 11 | **Debug scripts without import path fix** | Pass | `scripts/_bootstrap.py` adds project root for standalone runs. |
| 12 | **Undocumented empirical claims as official docs** | Pass | Week 9–10 docs label *observed in our tests* vs official pywinauto/FreeCAD refs. |

## Follow-ups (Middle track — not blockers for Junior)

| Item | Target week |
|------|-------------|
| Replace remaining fixed sleeps in `dialogs.py` / `viewport.py` with waits where possible | Week 16 (M2 stability) |
| Baseline image compare (not just file-exists Pillow checks) | Week 15 (M5) |
| CI workflow for smoke tests | Week 17 |
| Optional: J5 UI Save As step using `DialogHelper.save_document_as` | Future / Middle |

## Sign-off

Junior track **J1–J5** meets program anti-pattern review for consolidation PR.

Reviewer: Artem Sirchenko (self-review, Week 11).
