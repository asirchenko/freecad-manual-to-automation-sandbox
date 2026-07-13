"""Print FreeCAD UI control trees — Week 10 py_inspect / Inspect workflow."""

from __future__ import annotations

import _bootstrap  # noqa: F401 — project root on sys.path before framework imports

import argparse

from framework.app.freecad_launcher import FreeCADLauncher
from framework.ui.main_window import MainWindow
from framework.utils.logging_config import setup_logging
from framework.utils.paths import model_path
from framework.utils.ui_inspect import print_descendants, print_top_windows

setup_logging()


def main() -> None:
    parser = argparse.ArgumentParser(description="Dump FreeCAD UI trees for locator debugging.")
    parser.add_argument(
        "--model",
        default="sample_box.FCStd",
        help="Optional model under models/ to open on launch",
    )
    parser.add_argument("--depth", type=int, default=2, help="Max descendant depth")
    parser.add_argument(
        "--backend",
        choices=("uia", "win32", "both"),
        default="both",
        help="Which Desktop backend to list",
    )
    args = parser.parse_args()

    launcher = FreeCADLauncher()
    try:
        open_path = model_path(args.model) if args.model else None
        launcher.launch(open_path=open_path)
        main = MainWindow(launcher.get_main_window())
        main.wait_ready()

        if args.backend in {"uia", "both"}:
            print_top_windows("uia", label="UIA top windows")
            print_descendants(main.window, max_depth=args.depth, label="FreeCAD main window (UIA)")

        if args.backend in {"win32", "both"}:
            print_top_windows("win32", label="win32 top windows")

        input("\nPress Enter to close FreeCAD...")
    finally:
        launcher.close()


if __name__ == "__main__":
    main()
