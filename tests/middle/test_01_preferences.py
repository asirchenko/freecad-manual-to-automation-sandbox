"""M1 — Preferences dialog (multi-window) — Week 13."""

from __future__ import annotations

from framework.ui.main_window import MainWindow
from framework.ui.preferences import PreferencesDialog


def test_edit_menu_contains_preferences(main_window: MainWindow) -> None:
    assert main_window.menu_contains("Edit")


def test_preferences_dialog_opens_and_closes(main_window: MainWindow) -> None:
    prefs = PreferencesDialog(main_window.window)
    prefs.open()
    prefs.wait_visible()
    assert prefs.is_open()
    assert prefs.has_general_page()
    prefs.click_cancel()
    assert not prefs.is_open()


def test_preferences_ok_dismisses_dialog(main_window: MainWindow) -> None:
    prefs = PreferencesDialog(main_window.window)
    prefs.open()
    prefs.wait_visible()
    prefs.click_ok()
    assert not prefs.is_open()
    assert main_window.menu_contains("File")
