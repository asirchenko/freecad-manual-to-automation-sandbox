"""Tolerance-based geometry checks for CAD validation."""

from __future__ import annotations

import math


def assert_dimension_close(
    actual: float,
    expected: float,
    *,
    abs_tolerance: float = 0.01,
    rel_tolerance: float = 1e-6,
    label: str = "dimension",
) -> None:
    assert math.isclose(
        actual,
        expected,
        rel_tol=rel_tolerance,
        abs_tol=abs_tolerance,
    ), f"{label}: expected {expected}, got {actual} (tol={abs_tolerance})"


def assert_box_dimensions(
    x_length: float,
    y_length: float,
    z_length: float,
    expected_x: float,
    expected_y: float,
    expected_z: float,
    *,
    abs_tolerance: float = 0.01,
) -> None:
    assert_dimension_close(x_length, expected_x, abs_tolerance=abs_tolerance, label="X length")
    assert_dimension_close(y_length, expected_y, abs_tolerance=abs_tolerance, label="Y length")
    assert_dimension_close(z_length, expected_z, abs_tolerance=abs_tolerance, label="Z length")
