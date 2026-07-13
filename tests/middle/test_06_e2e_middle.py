"""M6 — Middle E2E integration — Week 18."""

from __future__ import annotations

from pathlib import Path

from framework.app.freecad_api import FreeCADApiRunner
from framework.app.freecad_launcher import FreeCADLauncher
from framework.assertions.geometry_assertions import assert_box_dimensions
from framework.assertions.image_assertions import assert_screenshot_not_empty
from framework.ui.main_window import MainWindow
from framework.ui.preferences import PreferencesDialog
from framework.ui.viewport import Viewport
from framework.utils.paths import artifact_path, model_path

EDGE_MM = 10.0
TOLERANCE = 0.01


def test_m6_middle_e2e_flow() -> None:
    """Launch -> preferences smoke -> open model -> geometry check -> viewport -> save."""
    runner = FreeCADApiRunner()
    geometry_path = artifact_path("m6_e2e_geometry", "FCStd")
    saved_copy = artifact_path("m6_e2e_saved", "FCStd")

    runner.create_box_and_save(geometry_path, EDGE_MM, EDGE_MM, EDGE_MM)
    assert geometry_path.exists()

    launcher = FreeCADLauncher()
    launcher.launch(open_path=geometry_path)
    try:
        from framework.ui.dialogs import DialogHelper

        DialogHelper(launcher.app).dismiss_ok_dialog_if_present()
        window = launcher.get_main_window()
        main = MainWindow(window)
        main.wait_ready()

        prefs = PreferencesDialog(main.window)
        prefs.open()
        prefs.wait_visible()
        prefs.click_cancel()

        main.show_tree_item("Cube")
        x_len, y_len, z_len = runner.read_bounding_box_from_model(geometry_path)
        assert_box_dimensions(x_len, y_len, z_len, EDGE_MM, EDGE_MM, EDGE_MM, abs_tolerance=TOLERANCE)

        viewport = Viewport(main)
        viewport.prepare_for_screenshot()
        screenshot = viewport.capture_to_file("m6_e2e_viewport")
        assert_screenshot_not_empty(screenshot)

        runner.save_document_copy(geometry_path, saved_copy)
        assert saved_copy.exists()
        assert Path(saved_copy).stat().st_size > 100
    finally:
        launcher.close()
