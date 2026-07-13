"""Debug Save As dialog detection in FreeCAD."""

from __future__ import annotations

import _bootstrap  # noqa: F401 — project root on sys.path before framework imports

import time
from pathlib import Path

from pywinauto import Application, Desktop

from framework.app.freecad_launcher import FreeCADLauncher
from framework.ui.main_window import MainWindow
from framework.utils.paths import model_path

OUTPUT = Path(__file__).resolve().parents[1] / "artifacts" / "debug_save_as.FCStd"


def click_file_submenu(main: MainWindow, submenu_text: str) -> None:
    """Open File menu by click (avoids menu_select COM issues)."""
    menu_bars = main.window.descendants(control_type="MenuBar")
    file_item = None
    for bar in menu_bars:
        for item in bar.children(control_type="MenuItem"):
            if item.window_text().lower() == "file":
                file_item = item
                break
    if file_item is None:
        raise RuntimeError("File menu item not found")

    file_item.click_input()
    time.sleep(0.5)

    for item in Desktop(backend="uia").windows(control_type="MenuItem"):
        text = item.window_text()
        if submenu_text.lower() in text.lower():
            print(f"Clicking submenu: {repr(text)}")
            item.click_input()
            return

    raise RuntimeError(f"Submenu not found: {submenu_text}")


def list_top_windows(label: str) -> None:
    print(f"\n=== Top windows ({label}) ===")
    for win in Desktop(backend="uia").windows():
        try:
            title = win.window_text()
            if title.strip():
                safe = title.encode("ascii", errors="replace").decode("ascii")
                print(f"  {safe!r} | class={win.class_name()}")
        except Exception:
            pass


def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    if OUTPUT.exists():
        OUTPUT.unlink()

    launcher = FreeCADLauncher()
    launcher.launch(open_path=model_path("sample_box.FCStd"))
    main = MainWindow(launcher.get_main_window())
    main.wait_ready()
    list_top_windows("before Save As")

    try:
        click_file_submenu(main, "Save As")
    except Exception as exc:
        print(f"File->Save As click failed: {exc}")
        main.set_focus()
        main.window.type_keys("%f")  # Alt+F
        time.sleep(0.5)
        main.window.type_keys("a")

    time.sleep(3)
    list_top_windows("after Save As trigger")

    # Try multiple dialog patterns
    patterns = [
        ".*Save.*",
        ".*save.*",
        ".*As.*",
        ".*sample_box.*",
    ]
    for pattern in patterns:
        try:
            dlg = Desktop(backend="uia").window(title_re=pattern, visible_only=True)
            if dlg.exists(timeout=1):
                print(f"MATCH uia pattern {pattern!r}: {dlg.window_text()!r}")
        except Exception as exc:
            print(f"No uia match {pattern!r}: {exc}")

    try:
        dlg = Desktop(backend="win32").window(title_re=".*Save.*")
        if dlg.exists(timeout=1):
            print(f"MATCH win32: {dlg.window_text()!r}")
    except Exception as exc:
        print(f"No win32 match: {exc}")

    # Enumerate all dialogs
    print("\n=== All Window controls ===")
    for win in Desktop(backend="uia").windows(control_type="Window"):
        t = win.window_text()
        if t and t != main.title:
            print(f"  Window: {repr(t)}")

    launcher.close()


if __name__ == "__main__":
    main()
