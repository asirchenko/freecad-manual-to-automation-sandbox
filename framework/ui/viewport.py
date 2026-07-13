"""Viewport actions and screenshots."""

from __future__ import annotations

from pathlib import Path

from framework.ui.main_window import MainWindow
from framework.utils.paths import artifact_path


class Viewport:
    """Viewport helpers — menu navigation when Qt shortcuts are not exposed via UIA."""

    def __init__(self, main_window: MainWindow) -> None:
        self.main_window = main_window

    def fit_all(self) -> None:
        """View -> Standard Views -> Fit All."""
        self.main_window.wait_ready()
        self.main_window.select_menu("View->Standard Views->Fit All")

    def set_front_view(self) -> None:
        """View -> Standard Views -> 1 Front."""
        self.main_window.select_menu("View->Standard Views->1 Front")

    def prepare_for_screenshot(self) -> None:
        """Apply a consistent view before capturing."""
        self.fit_all()
        self.set_front_view()
        self.fit_all()

    def capture_to_file(self, name: str, extension: str = "png") -> Path:
        """Capture the main window and save it under artifacts/."""
        self.main_window.wait_ready()
        output = artifact_path(name, extension=extension)
        image = self.main_window.capture_image()
        image.save(output)
        return output

    def capture_model_view(self, name: str) -> Path:
        """Fit view and capture a model screenshot."""
        self.prepare_for_screenshot()
        return self.capture_to_file(name)
