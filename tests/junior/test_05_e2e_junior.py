"""J5 — Junior E2E: launch, document, API geometry, viewport, save, verify artifacts."""

from __future__ import annotations

from pathlib import Path

from framework.app.freecad_api import FreeCADApiRunner
from framework.app.freecad_launcher import FreeCADLauncher
from framework.assertions.geometry_assertions import assert_box_dimensions
from framework.assertions.image_assertions import (
    assert_screenshot_dimensions,
    assert_screenshot_not_empty,
)
from framework.ui.dialogs import DialogHelper
from framework.ui.main_window import MainWindow
from framework.ui.viewport import Viewport
from framework.utils.paths import artifact_path

EDGE_MM = 10.0
ABS_TOLERANCE_MM = 0.01
MIN_FCSTD_BYTES = 1000


def test_j5_e2e_junior_flow() -> None:
    """Full junior flow in one independent test."""
    geometry_path = artifact_path("j5_e2e_geometry", extension="FCStd")
    saved_path = artifact_path("j5_e2e_saved", extension="FCStd")
    screenshot_path = artifact_path("j5_e2e_viewport", extension="png")

    # --- Geometry (API) + validation ---
    api = FreeCADApiRunner()
    x_len, y_len, z_len = api.create_box_and_save(
        geometry_path,
        EDGE_MM,
        EDGE_MM,
        EDGE_MM,
    )
    assert_box_dimensions(
        x_len,
        y_len,
        z_len,
        EDGE_MM,
        EDGE_MM,
        EDGE_MM,
        abs_tolerance=ABS_TOLERANCE_MM,
    )
    assert geometry_path.exists()
    assert geometry_path.stat().st_size >= MIN_FCSTD_BYTES

    # --- Launch + open document (UI) ---
    launcher = FreeCADLauncher()
    launcher.launch(open_path=geometry_path)
    try:
        DialogHelper(launcher.app).dismiss_ok_dialog_if_present()
        main = MainWindow(launcher.get_main_window())
        main.wait_ready()

        assert main.window.is_visible()
        assert "FreeCAD" in main.title
        tree_items = main.get_model_tree_items()
        assert tree_items, "Model tree should not be empty after opening geometry document"
        assert any("cube" in item.lower() for item in tree_items)

        # --- Viewport + screenshot ---
        viewport = Viewport(main)
        viewport.prepare_for_screenshot()
        captured = viewport.capture_to_file("j5_e2e_viewport")
        assert captured == screenshot_path
        assert_screenshot_not_empty(screenshot_path)
        assert_screenshot_dimensions(screenshot_path)

        # --- Save copy (API — UI Save As is unreliable on Qt/FreeCAD) ---
        api.save_document_copy(geometry_path, saved_path)
        assert saved_path.exists()
        assert saved_path.stat().st_size >= MIN_FCSTD_BYTES

        # --- Verify all artifacts ---
        for artifact in (geometry_path, saved_path, screenshot_path):
            assert artifact.exists(), f"Missing artifact: {artifact}"
            assert artifact.stat().st_size > 0
    finally:
        launcher.close()
