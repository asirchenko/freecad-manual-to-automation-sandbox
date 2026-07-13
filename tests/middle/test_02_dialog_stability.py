"""M2 — Dialog stability (5 stable open/close cycles) — Week 16."""

from __future__ import annotations

import pytest

from framework.config import DEFAULT_CONFIG
from framework.ui.main_window import MainWindow
from framework.ui.preferences import PreferencesDialog


@pytest.mark.parametrize("run_index", range(DEFAULT_CONFIG.stability_run_count))
def test_preferences_open_close_stable(main_window: MainWindow, run_index: int) -> None:
    """Open and close Preferences five times without hard-coded long sleeps."""
    prefs = PreferencesDialog(main_window.window)
    prefs.open()
    prefs.wait_visible(timeout_sec=DEFAULT_CONFIG.dialog_timeout_sec)
    assert prefs.is_open(), f"Run {run_index + 1}: dialog not open"
    prefs.click_cancel()
    assert not prefs.is_open(), f"Run {run_index + 1}: dialog still open"
