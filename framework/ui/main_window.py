"""Page object for the FreeCAD main window."""

from __future__ import annotations

from pywinauto.application import WindowSpecification
from pywinauto.timings import Timings

from framework.utils.waits import wait_until


class MainWindow:
    """Wraps the top-level FreeCAD window and exposes menu actions."""

    def __init__(self, window: WindowSpecification) -> None:
        self.window = window

    @property
    def title(self) -> str:
        return self.window.window_text()

    def wait_ready(self, timeout_sec: float = 30.0) -> None:
        """Wait until the main window is visible and ready for interaction."""
        self.window.wait("visible", timeout=timeout_sec)
        wait_until(
            lambda: self.window.is_enabled(),
            timeout_sec=timeout_sec,
            error_message="Main window did not become enabled",
        )

    def get_menu_items(self) -> list[str]:
        """Return top-level menu names from the menu bar."""
        menu_bars = self.window.descendants(control_type="MenuBar")
        if not menu_bars:
            return []

        best_items: list[str] = []
        for menu_bar in menu_bars:
            items = [
                item.window_text()
                for item in menu_bar.children(control_type="MenuItem")
                if item.window_text()
            ]
            if len(items) > len(best_items):
                best_items = items

        return best_items

    def menu_contains(self, menu_name: str) -> bool:
        menu_name_lower = menu_name.lower()
        return any(item.lower() == menu_name_lower for item in self.get_menu_items())

    def select_menu(self, menu_path: str) -> None:
        """Select a menu path such as 'View' or 'View->Standard views'."""
        Timings.after_menuwait = 1
        self.window.menu_select(menu_path)

    def set_focus(self) -> None:
        self.window.set_focus()

    def capture_image(self):
        """Capture the main window as a PIL Image."""
        self.set_focus()
        return self.window.capture_as_image()
