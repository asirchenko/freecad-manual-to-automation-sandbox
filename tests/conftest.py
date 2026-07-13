"""Shared pytest fixtures."""

from __future__ import annotations

from collections.abc import Iterator

import pytest

from framework.app.freecad_launcher import FreeCADLauncher
from framework.ui.dialogs import DialogHelper
from framework.ui.main_window import MainWindow
from framework.utils.logging_config import setup_logging


@pytest.fixture(scope="session", autouse=True)
def _configure_test_logging() -> None:
    """Write framework logs to artifacts/logs/sandbox.log during test runs."""
    setup_logging()


@pytest.fixture
def freecad_app() -> Iterator[FreeCADLauncher]:
    """Launch FreeCAD before a test and close it afterward."""
    launcher = FreeCADLauncher()
    launcher.launch()
    yield launcher
    launcher.close()


@pytest.fixture(scope="module")
def launched_freecad() -> Iterator[FreeCADLauncher]:
    """Launch FreeCAD once per test module (UI tests)."""
    launcher = FreeCADLauncher()
    launcher.launch()
    DialogHelper(launcher.app).dismiss_ok_dialog_if_present()
    yield launcher
    launcher.close()


@pytest.fixture(scope="module")
def main_window(launched_freecad: FreeCADLauncher) -> MainWindow:
    window = launched_freecad.get_main_window()
    main = MainWindow(window)
    main.wait_ready()
    return main


@pytest.fixture(scope="module")
def document_window(main_window: MainWindow) -> MainWindow:
    """Main window with a new document created."""
    main_window.create_new_document()
    return main_window


@pytest.fixture(scope="module")
def model_window() -> Iterator[MainWindow]:
    """Launch FreeCAD with sample_box.FCStd loaded."""
    from framework.utils.paths import model_path

    launcher = FreeCADLauncher()
    launcher.launch(open_path=model_path("sample_box.FCStd"))
    DialogHelper(launcher.app).dismiss_ok_dialog_if_present()
    window = launcher.get_main_window()
    main = MainWindow(window)
    main.wait_ready()
    yield main
    launcher.close()
