"""FreeCAD Preferences panel (M1, M2) — embedded in main window on FreeCAD 1.1."""

from __future__ import annotations

from pywinauto.application import WindowSpecification
from pywinauto.keyboard import send_keys

from framework.ui.main_window import MainWindow
from framework.utils.waits import wait_until

# Buttons that appear on the in-window Preferences page (FreeCAD 1.1.1).
_PREFERENCES_MARKERS = {"Import Configuration", "Revert", "Reset"}


class PreferencesDialog:
    """Page object for Edit -> Preferences (in-window panel, not a separate dialog)."""

    def __init__(self, main_window: WindowSpecification) -> None:
        self.main_window = main_window

    def _main(self) -> MainWindow:
        return MainWindow(self.main_window)

    def _button_labels(self) -> set[str]:
        return {
            (button.window_text() or "").strip()
            for button in self.main_window.descendants(control_type="Button")
            if button.window_text()
        }

    def is_open(self) -> bool:
        labels = self._button_labels()
        return bool(labels.intersection(_PREFERENCES_MARKERS))

    def open(self) -> None:
        main = self._main()
        main.wait_ready()
        main.select_menu("Edit->Preferences")
        wait_until(self.is_open, timeout_sec=15, error_message="Preferences panel did not open")

    def wait_visible(self, timeout_sec: float = 10.0) -> None:
        wait_until(self.is_open, timeout_sec=timeout_sec, error_message="Preferences panel not visible")

    def has_general_page(self) -> bool:
        """General page is the default when Preferences opens."""
        for control_type in ("TreeItem", "Text", "ListItem"):
            for item in self.main_window.descendants(control_type=control_type):
                text = (item.window_text() or "").lower()
                if "general" in text:
                    return True
        return self.is_open()

    def _click_button(self, *names: str) -> None:
        targets = {name.lower() for name in names}
        for button in self.main_window.descendants(control_type="Button"):
            label = (button.window_text() or "").lower().strip()
            if label in targets:
                button.click_input()
                return
        raise RuntimeError(f"Button not found on Preferences panel: {names}")

    def click_ok(self) -> None:
        self._click_button("ok")
        wait_until(lambda: not self.is_open(), timeout_sec=10, error_message="Preferences panel did not close")

    def click_cancel(self) -> None:
        try:
            self._click_button("cancel")
        except RuntimeError:
            self.main_window.set_focus()
            send_keys("{ESC}")
        wait_until(lambda: not self.is_open(), timeout_sec=10, error_message="Preferences panel did not close")

    def close(self) -> None:
        if self.is_open():
            self.click_cancel()
