"""Optional dialogs that may appear around the main window."""

from __future__ import annotations

from pywinauto import Application

from framework.utils.waits import wait_until


class DialogHelper:
    """Detect and dismiss common modal dialogs."""

    def __init__(self, app: Application) -> None:
        self.app = app

    def has_modal_dialog(self) -> bool:
        try:
            dialog = self.app.window(control_type="Window", found_index=1)
            return dialog.exists(timeout=0.5)
        except Exception:
            return False

    def dismiss_ok_dialog_if_present(self) -> bool:
        """Click OK on a simple modal dialog when it exists."""
        if not self.has_modal_dialog():
            return False

        try:
            dialog = self.app.top_window()
            ok_button = dialog.child_window(title="OK", control_type="Button")
            if ok_button.exists(timeout=1):
                ok_button.click_input()
                wait_until(lambda: not self.has_modal_dialog(), timeout_sec=5)
                return True
        except Exception:
            return False
        return False
