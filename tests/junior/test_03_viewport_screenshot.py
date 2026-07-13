"""J3 — Viewport screenshot with prepared model sample_box.FCStd."""

from __future__ import annotations

from framework.assertions.image_assertions import (
    assert_screenshot_dimensions,
    assert_screenshot_not_empty,
)
from framework.ui.main_window import MainWindow
from framework.ui.viewport import Viewport


def test_sample_box_loaded_in_title(model_window: MainWindow) -> None:
    assert "sample_box" in model_window.title.lower()


def test_sample_box_visible_in_model_tree(model_window: MainWindow) -> None:
    tree_items = model_window.get_model_tree_items()
    assert any("sample_box" in item.lower() for item in tree_items)
    assert any("box" in item.lower() for item in tree_items)


def test_j3_viewport_screenshot_with_pillow(model_window: MainWindow) -> None:
    model_window.show_tree_item("box")

    viewport = Viewport(model_window)
    screenshot_path = viewport.capture_model_view("j3_viewport_sample_box")

    assert_screenshot_not_empty(screenshot_path)
    assert_screenshot_dimensions(screenshot_path, min_width=200, min_height=200)
