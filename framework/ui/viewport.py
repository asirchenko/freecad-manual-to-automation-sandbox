"""Viewport capture helpers — full window capture when Qt child controls are hidden."""

from __future__ import annotations

from pathlib import Path

from framework.ui.main_window import MainWindow
from framework.utils.paths import artifact_path


class Viewport:
    """Capture screenshots from the main window area."""

    def __init__(self, main_window: MainWindow) -> None:
        self.main_window = main_window

    def capture_to_file(self, name: str, extension: str = "png") -> Path:
        """Capture the current main window and save it under artifacts/."""
        self.main_window.wait_ready()
        output = artifact_path(name, extension=extension)
        image = self.main_window.capture_image()
        image.save(output)
        return output
