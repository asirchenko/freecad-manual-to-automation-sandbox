"""J2 — Document creation: new document, model tree, screenshot."""

from __future__ import annotations

from framework.assertions.image_assertions import (
    assert_screenshot_dimensions,
    assert_screenshot_not_empty,
)
from framework.ui.main_window import MainWindow
from framework.ui.viewport import Viewport


def test_create_document_updates_window_title(document_window: MainWindow) -> None:
    assert "Unnamed" in document_window.title


def test_document_appears_in_model_tree(document_window: MainWindow) -> None:
    tree_items = document_window.get_model_tree_items()
    assert tree_items, "Model tree should list at least one item"
    assert any("Unnamed" in item for item in tree_items)


def test_j2_create_document_screenshot(document_window: MainWindow) -> None:
    viewport = Viewport(document_window)
    screenshot_path = viewport.capture_to_file("j2_create_document_screenshot")

    assert_screenshot_not_empty(screenshot_path)
    assert_screenshot_dimensions(screenshot_path)
