"""Week 4–5 — Startup verification, menus, and viewport capture."""

from __future__ import annotations

from collections.abc import Iterator

import pytest

from framework.app.freecad_launcher import FreeCADLauncher
from framework.assertions.image_assertions import (
    assert_screenshot_dimensions,
    assert_screenshot_not_empty,
)
from framework.ui.dialogs import DialogHelper
from framework.ui.main_window import MainWindow
from framework.ui.viewport import Viewport


@pytest.fixture(scope="module")
def launched_freecad() -> Iterator[FreeCADLauncher]:
    """Launch FreeCAD once for all tests in this module."""
    launcher = FreeCADLauncher()
    launcher.launch()
    dialog_helper = DialogHelper(launcher.app)
    dialog_helper.dismiss_ok_dialog_if_present()
    yield launcher
    launcher.close()


@pytest.fixture(scope="module")
def main_window(launched_freecad: FreeCADLauncher) -> MainWindow:
    window = launched_freecad.get_main_window()
    main = MainWindow(window)
    main.wait_ready()
    return main


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


def test_capture_main_window_screenshot(main_window: MainWindow) -> None:
    viewport = Viewport(main_window)
    screenshot_path = viewport.capture_to_file("startup_viewport_week5")

    assert_screenshot_not_empty(screenshot_path)
    assert_screenshot_dimensions(screenshot_path)
