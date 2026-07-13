"""M3 — CAD API geometry script — Week 14."""

from __future__ import annotations

from framework.app.freecad_api import FreeCADApiRunner
from framework.assertions.geometry_assertions import assert_box_dimensions
from framework.utils.paths import MODELS_DIR, model_path

EDGE_MM = 12.0
TOLERANCE = 0.01
MIDDLE_MODEL = "middle_api_box.FCStd"


def test_create_box_via_api_and_save() -> None:
    runner = FreeCADApiRunner()
    output = model_path(MIDDLE_MODEL)
    x_len, y_len, z_len = runner.create_box_in_document(output, EDGE_MM, EDGE_MM, EDGE_MM)

    assert output.exists()
    assert output.stat().st_size > 100
    assert_box_dimensions(x_len, y_len, z_len, EDGE_MM, EDGE_MM, EDGE_MM, abs_tolerance=TOLERANCE)


def test_saved_model_bounding_box_matches() -> None:
    path = model_path(MIDDLE_MODEL)
    if not path.exists():
        runner = FreeCADApiRunner()
        runner.create_box_in_document(path, EDGE_MM, EDGE_MM, EDGE_MM)

    runner = FreeCADApiRunner()
    x_len, y_len, z_len = runner.read_bounding_box_from_model(path)
    assert_box_dimensions(x_len, y_len, z_len, EDGE_MM, EDGE_MM, EDGE_MM, abs_tolerance=TOLERANCE)


def test_models_directory_contains_middle_api_box() -> None:
    assert MODELS_DIR.exists()
    assert model_path(MIDDLE_MODEL).exists()
