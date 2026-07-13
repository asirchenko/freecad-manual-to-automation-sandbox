"""Page object for the FreeCAD main window."""

from __future__ import annotations

import time
from pathlib import Path

from pywinauto import Application, Desktop
from pywinauto.application import WindowSpecification

from framework.utils.waits import wait_for_value, wait_until


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
        """Select a menu path such as 'View' or 'View->Standard Views->Fit All'.

        Clicks through each level manually instead of using pywinauto's
        built-in menu_select(), which raises IndexError against FreeCAD's
        Qt menus — likely due to the duplicate/empty MenuBar (see
        get_menu_items()).
        """
        for label in menu_path.split("->"):
            label = label.strip()
            for item in self.window.descendants(control_type="MenuItem"):
                if item.window_text() == label:
                    item.click_input()
                    break
            else:
                raise RuntimeError(f"Menu item not found: {label}")
            time.sleep(0.3)

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

    def find_tree_item(self, label: str):
        """Find a model-tree item, preferring an exact label match.

        Falls back to a substring match only if no exact match exists —
        an object like "Box" would otherwise match its parent document
        "sample_box" first.
        """
        label_lower = label.lower()
        fallback = None
        for item in self.window.descendants(control_type="TreeItem"):
            text = item.window_text()
            if not text:
                continue
            if text.lower() == label_lower:
                return item
            if fallback is None and label_lower in text.lower():
                fallback = item

        if fallback is not None:
            return fallback
        raise RuntimeError(f"Tree item not found: {label}")

    def show_tree_item(self, label: str) -> None:
        """Select a tree item and make it visible via its context menu.

        Objects created headless via freecadcmd are saved without a
        GuiDocument, so they default to hidden when opened in the GUI.
        Qt's custom-painted tree view does not respond to the "Space"
        shortcut sent via UIA, so this uses the right-click "Show
        Selection" context menu action instead.
        """
        item = self.find_tree_item(label)
        item.click_input()
        item.click_input(button="right")

        desktop = Desktop(backend="uia")

        def find_context_menu():
            for window in desktop.windows():
                try:
                    if window.element_info.class_name == "QMenu":
                        return window
                except Exception:
                    continue
            raise RuntimeError("Tree context menu not found")

        menu = wait_for_value(
            find_context_menu,
            timeout_sec=5,
            poll_interval_sec=0.2,
            error_message="Tree context menu did not appear",
        )

        for menu_item in menu.descendants(control_type="MenuItem"):
            if menu_item.window_text() == "Show Selection":
                menu_item.click_input()
                return

        raise RuntimeError("'Show Selection' not found in tree context menu")

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
