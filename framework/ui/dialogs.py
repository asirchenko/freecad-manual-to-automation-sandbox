"""Optional dialogs — Save As, OK dismiss, etc."""

from __future__ import annotations

import time
from pathlib import Path

from pywinauto import Application
from pywinauto.application import WindowSpecification
from pywinauto.keyboard import send_keys

from framework.utils.logging_config import get_logger
from framework.utils.waits import wait_until

logger = get_logger(__name__)


class DialogHelper:
    """Detect and interact with FreeCAD modal dialogs."""

    SAVE_AS_TITLE = "Save FreeCAD Document"

    def __init__(self, app: Application, main_window: WindowSpecification) -> None:
        self.app = app
        self.main_window = main_window
        self._win32_app: Application | None = None

    def _win32(self) -> Application:
        if self._win32_app is None:
            pid = self.app.process
            self._win32_app = Application(backend="win32").connect(process=pid)
        return self._win32_app

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

    def open_file_menu(self) -> None:
        """Open the File menu via UIA (Qt-safe)."""
        for menu_bar in self.main_window.descendants(control_type="MenuBar"):
            items = [
                item.window_text()
                for item in menu_bar.children(control_type="MenuItem")
                if item.window_text()
            ]
            if len(items) <= 5:
                continue
            for item in menu_bar.children(control_type="MenuItem"):
                if item.window_text().lower() == "file":
                    item.click_input()
                    time.sleep(0.5)
                    return
        raise RuntimeError("File menu not found")

    def click_file_submenu(self, label_contains: str) -> None:
        """Click a File submenu entry such as 'Save As'."""
        label_lower = label_contains.lower()
        wait_until(
            lambda: any(
                label_lower in (item.window_text() or "").lower()
                for item in self.main_window.descendants(control_type="MenuItem")
            ),
            timeout_sec=5,
            error_message=f"File menu did not expand for: {label_contains}",
        )
        for item in self.main_window.descendants(control_type="MenuItem"):
            text = item.window_text()
            if text and label_lower in text.lower():
                item.click_input()
                time.sleep(0.5)
                return
        raise RuntimeError(f"File submenu not found: {label_contains}")

    def open_save_as_dialog(self) -> None:
        """Open Save As — Ctrl+Shift+S (reliable); File menu as fallback."""
        self.main_window.set_focus()
        send_keys("^+s")
        time.sleep(1)

        try:
            self.wait_save_as_dialog(timeout_sec=3)
            return
        except TimeoutError:
            pass

        self.open_file_menu()
        self.click_file_submenu("save as")

    def wait_save_as_dialog(self, timeout_sec: float = 10.0):
        """Return the native Save As dialog (win32 #32770 — not visible via UIA)."""
        deadline = time.time() + timeout_sec
        last_error: Exception | None = None

        while time.time() < deadline:
            try:
                for dialog in self._win32().windows(title=self.SAVE_AS_TITLE):
                    if dialog.class_name() != "#32770":
                        continue
                    buttons = [
                        btn.window_text()
                        for btn in dialog.descendants(class_name="Button")
                    ]
                    if any("save" in label.lower() for label in buttons):
                        return dialog
            except Exception as exc:
                last_error = exc
            time.sleep(0.3)

        if last_error:
            raise TimeoutError(f"Save As dialog not found: {last_error}") from last_error
        raise TimeoutError(
            f"Save As dialog '{self.SAVE_AS_TITLE}' (#32770) not found. "
            "Use win32 backend — UIA/Desktop does not expose this Qt dialog."
        )

    def _set_save_filename(self, dialog, path: Path) -> None:
        """Set the file name in the standard Windows Save dialog."""
        for edit in dialog.descendants(class_name="Edit"):
            if edit.is_visible() and edit.is_enabled():
                edit.set_edit_text(str(path))
                return

        combos = dialog.descendants(class_name="ComboBox")
        for combo in combos:
            try:
                combo.child_window(class_name="Edit").set_edit_text(str(path))
                return
            except Exception:
                continue

        raise RuntimeError("No filename field found in Save As dialog")

    def save_document_as(self, output_path: Path | str) -> Path:
        """Save As via UI (Ctrl+Shift+S + win32 dialog)."""
        path = Path(output_path).resolve()
        path.parent.mkdir(parents=True, exist_ok=True)

        self.open_save_as_dialog()
        dialog = self.wait_save_as_dialog()
        logger.info("Save As dialog found: class=%s", dialog.class_name())
        self._set_save_filename(dialog, path)

        time.sleep(0.3)
        for button in dialog.descendants(class_name="Button"):
            label = button.window_text().lower().strip()
            if label in {"save", "&save"}:
                button.click_input()
                break
        else:
            raise RuntimeError("Save button not found in Save As dialog")

        wait_until(lambda: path.exists(), timeout_sec=15, error_message=f"File not saved: {path}")
        logger.info("Document saved via UI: %s (%s bytes)", path, path.stat().st_size)
        return path
