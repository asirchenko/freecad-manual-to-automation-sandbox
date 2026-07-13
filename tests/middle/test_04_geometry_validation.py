"""M4 — Geometry validation from prepared model — Week 15."""

from __future__ import annotations

import math

from framework.app.freecad_api import FreeCADApiRunner
from framework.assertions.geometry_assertions import assert_box_dimensions, assert_volume_close
from framework.utils.paths import model_path

EDGE_MM = 10.0
TOLERANCE = 0.01


def test_sample_box_bounding_box_dimensions() -> None:
    runner = FreeCADApiRunner()
    path = model_path("sample_box.FCStd")
    assert path.exists(), f"Missing prepared model: {path}"

    x_len, y_len, z_len = runner.read_bounding_box_from_model(path)
    assert_box_dimensions(x_len, y_len, z_len, EDGE_MM, EDGE_MM, EDGE_MM, abs_tolerance=TOLERANCE)


def test_sample_box_volume_is_cube() -> None:
    runner = FreeCADApiRunner()
    x_len, y_len, z_len = runner.read_bounding_box_from_model(model_path("sample_box.FCStd"))
    volume = x_len * y_len * z_len
    expected = EDGE_MM ** 3
    assert_volume_close(volume, expected, abs_tolerance=0.5)


def test_all_box_edges_equal_within_tolerance() -> None:
    runner = FreeCADApiRunner()
    x_len, y_len, z_len = runner.read_bounding_box_from_model(model_path("sample_box.FCStd"))
    assert math.isclose(x_len, y_len, abs_tol=TOLERANCE)
    assert math.isclose(y_len, z_len, abs_tol=TOLERANCE)
