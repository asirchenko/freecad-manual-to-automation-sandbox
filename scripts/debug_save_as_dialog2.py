"""Debug Save As - search inside FreeCAD main window (modal Qt dialog)."""

from __future__ import annotations

import _bootstrap  # noqa: F401 — project root on sys.path before framework imports

import time
from pathlib import Path

from pywinauto import Desktop

from framework.app.freecad_launcher import FreeCADLauncher
from framework.ui.main_window import MainWindow
from framework.utils.paths import model_path


def safe_print(text: str) -> None:
    print(text.encode("ascii", errors="replace").decode("ascii"))


def open_file_menu_and_list(main: MainWindow) -> None:
    for bar in main.window.descendants(control_type="MenuBar"):
        for item in bar.children(control_type="MenuItem"):
            if item.window_text().lower() == "file":
                item.click_input()
                time.sleep(0.8)
                safe_print("--- File submenu items ---")
                for mi in Desktop(backend="uia").windows(control_type="MenuItem"):
                    t = mi.window_text()
                    if t:
                        safe_print(f"  menu: {t!r}")
                return


def click_save_as_from_menu(main: MainWindow) -> None:
    for bar in main.window.descendants(control_type="MenuBar"):
        for item in bar.children(control_type="MenuItem"):
            if item.window_text().lower() == "file":
                item.click_input()
                time.sleep(0.8)
                break

    for mi in Desktop(backend="uia").windows(control_type="MenuItem"):
        t = mi.window_text()
        if t and "save" in t.lower() and "as" in t.lower():
            safe_print(f"Clicking: {t!r}")
            mi.click_input()
            return
    raise RuntimeError("Save As menu item not found")


def dump_dialog_candidates(main: MainWindow, label: str) -> None:
    safe_print(f"\n=== Dialog candidates ({label}) ===")
    for ctrl_type in ["Window", "Pane", "Dialog", "Custom"]:
        items = main.window.descendants(control_type=ctrl_type)
        for item in items:
            try:
                t = item.window_text()
                cn = item.class_name()
                if t or cn in ("#32770", "Qt5QWindowIcon", "Qt653QWindowIcon"):
                    safe_print(f"  [{ctrl_type}] {t!r} class={cn}")
            except Exception:
                pass

    # win32 child dialogs
    try:
        app_win32 = main.window.wrapper_object()
        safe_print("win32 children count: " + str(len(app_win32.children())))
    except Exception as exc:
        safe_print(f"win32: {exc}")


def main() -> None:
    launcher = FreeCADLauncher()
    launcher.launch(open_path=model_path("sample_box.FCStd"))
    main = MainWindow(launcher.get_main_window())
    main.wait_ready()

    open_file_menu_and_list(main)
    time.sleep(1)

    # reopen and click Save As
    click_save_as_from_menu(main)
    time.sleep(2)

    dump_dialog_candidates(main, "after Save As")
    list_top_windows()

    launcher.close()


def list_top_windows() -> None:
    safe_print("\n=== Top-level windows with Save/As/sample ===")
    for win in Desktop(backend="uia").windows():
        t = win.window_text()
        if any(k in t.lower() for k in ("save", "as", "sample", "freecad")):
            safe_print(f"  {t!r} | {win.class_name()}")


if __name__ == "__main__":
    main()
