"""M5 — Deterministic viewport + baseline compare — Week 15."""

from __future__ import annotations

import os

from framework.assertions.image_assertions import (
    assert_image_matches_baseline,
    assert_screenshot_not_empty,
    save_as_baseline,
)
from framework.config import DEFAULT_CONFIG, baseline_path
from framework.ui.main_window import MainWindow
from framework.ui.viewport import Viewport

BASELINE_NAME = "viewport_sample_box_front"
CAPTURE_NAME = "m5_viewport_compare"


def test_deterministic_viewport_capture(model_window: MainWindow) -> None:
    model_window.show_tree_item("box")
    viewport = Viewport(model_window)
    viewport.prepare_for_screenshot()
    screenshot = viewport.capture_model_view(CAPTURE_NAME)
    assert_screenshot_not_empty(screenshot)


def test_viewport_matches_baseline(model_window: MainWindow) -> None:
    baseline = baseline_path(BASELINE_NAME)
    model_window.show_tree_item("box")
    viewport = Viewport(model_window)
    viewport.prepare_for_screenshot()
    actual = viewport.capture_model_view(CAPTURE_NAME)

    if os.getenv("GENERATE_BASELINE") == "1" or not baseline.exists():
        save_as_baseline(actual, baseline)

    assert baseline.exists(), (
        f"Baseline missing: {baseline}. Run once with GENERATE_BASELINE=1 to create it."
    )
    assert_image_matches_baseline(
        actual,
        baseline,
        max_diff_ratio=DEFAULT_CONFIG.baseline_max_diff_ratio,
    )
