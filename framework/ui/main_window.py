"""Page object for the FreeCAD main window."""

from __future__ import annotations

from pathlib import Path

from pywinauto import Application
from pywinauto.application import WindowSpecification

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
        self.window.menu_select(menu_path)

    def find_toolbar_button(self, label: str):
        """Find a toolbar button by its visible label."""
        for button in self.window.descendants(control_type="Button"):
            if button.window_text() == label:
                return button
        raise RuntimeError(f"Toolbar button not found: {label}")

    def toolbar_has_button(self, label: str) -> bool:
        try:
            self.find_toolbar_button(label)
            return True
        except RuntimeError:
            return False

    def create_new_document(self, timeout_sec: float = 30.0) -> None:
        """Create a new document via the standard toolbar button."""
        self.wait_ready()
        if "Unnamed" in self.title:
            return

        self.find_toolbar_button("New Document").click_input()
        wait_until(
            lambda: "Unnamed" in self.title,
            timeout_sec=timeout_sec,
            error_message="New document did not appear in window title",
        )

    def get_model_tree_items(self) -> list[str]:
        """Return visible labels from the model tree (TreeItem controls)."""
        return [
            item.window_text()
            for item in self.window.descendants(control_type="TreeItem")
            if item.window_text()
        ]

    def has_open_document(self) -> bool:
        return "Unnamed" in self.title or bool(self.get_model_tree_items())

    def set_focus(self) -> None:
        self.window.set_focus()

    def capture_image(self):
        """Capture the main window as a PIL Image."""
        self.set_focus()
        return self.window.capture_as_image()

    def save_document_as(self, output_path: Path | str, app: Application) -> Path:
        """Save the active document via File -> Save As (UI)."""
        from framework.ui.dialogs import DialogHelper

        helper = DialogHelper(app, self.window)
        return helper.save_document_as(Path(output_path))
