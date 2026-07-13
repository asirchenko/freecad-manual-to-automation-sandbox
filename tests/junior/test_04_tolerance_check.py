"""J4 — Geometry and tolerance check via FreeCAD API."""

from __future__ import annotations

from framework.app.freecad_api import FreeCADApiRunner
from framework.assertions.geometry_assertions import assert_box_dimensions

EDGE_MM = 10.0
ABS_TOLERANCE_MM = 0.01


def test_create_box_via_freecad_api() -> None:
    runner = FreeCADApiRunner()
    x_len, y_len, z_len = runner.create_box_bounding_box(EDGE_MM, EDGE_MM, EDGE_MM)

    assert x_len > 0
    assert y_len > 0
    assert z_len > 0


def test_box_dimensions_within_tolerance() -> None:
    runner = FreeCADApiRunner()
    x_len, y_len, z_len = runner.create_box_bounding_box(EDGE_MM, EDGE_MM, EDGE_MM)

    assert_box_dimensions(
        x_len,
        y_len,
        z_len,
        EDGE_MM,
        EDGE_MM,
        EDGE_MM,
        abs_tolerance=ABS_TOLERANCE_MM,
    )


def test_box_dimensions_are_equal_edges() -> None:
    runner = FreeCADApiRunner()
    x_len, y_len, z_len = runner.create_box_bounding_box(EDGE_MM, EDGE_MM, EDGE_MM)

    assert abs(x_len - y_len) <= ABS_TOLERANCE_MM
    assert abs(y_len - z_len) <= ABS_TOLERANCE_MM
