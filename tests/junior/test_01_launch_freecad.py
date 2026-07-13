"""J1 — Startup verification: launch, UI elements, startup screenshot."""

from __future__ import annotations

from framework.app.freecad_launcher import FreeCADLauncher
from framework.assertions.image_assertions import (
    assert_screenshot_dimensions,
    assert_screenshot_not_empty,
)
from framework.ui.main_window import MainWindow
from framework.ui.viewport import Viewport


def test_freecad_process_starts(launched_freecad: FreeCADLauncher) -> None:
    assert launched_freecad.is_running
    assert launched_freecad.app is not None


def test_freecad_main_window_is_visible(main_window: MainWindow) -> None:
    assert main_window.window.is_visible()
    assert main_window.window.is_enabled()


def test_freecad_window_title(main_window: MainWindow) -> None:
    assert "FreeCAD" in main_window.title


def test_main_window_menu_bar_has_file(main_window: MainWindow) -> None:
    menus = main_window.get_menu_items()
    assert menus, "Expected at least one top-level menu item"
    assert main_window.menu_contains("File")


def test_startup_toolbar_has_new_document(main_window: MainWindow) -> None:
    assert main_window.toolbar_has_button("New Document")


def test_j1_startup_screenshot(main_window: MainWindow) -> None:
    viewport = Viewport(main_window)
    screenshot_path = viewport.capture_to_file("j1_startup_screenshot")

    assert_screenshot_not_empty(screenshot_path)
    assert_screenshot_dimensions(screenshot_path)
