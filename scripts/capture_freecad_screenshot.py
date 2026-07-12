"""Capture FreeCAD main window screenshot for Week 1 evidence."""

from __future__ import annotations

import subprocess
import time
from pathlib import Path

from pywinauto import Application
from pywinauto.findwindows import ElementNotFoundError

FREECAD_EXE = Path(r"C:\Program Files\FreeCAD 1.1\bin\freecad.exe")
OUTPUT = Path(__file__).resolve().parents[1] / "artifacts" / "week01" / "freecad_running.png"
STARTUP_TIMEOUT = 90


def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)

    process = subprocess.Popen([str(FREECAD_EXE)])
    deadline = time.time() + STARTUP_TIMEOUT
    app = None

    while time.time() < deadline:
        try:
            app = Application(backend="uia").connect(process=process.pid, timeout=5)
            break
        except ElementNotFoundError:
            time.sleep(2)

    if app is None:
        raise RuntimeError("FreeCAD window did not appear within timeout")

    window = app.top_window()
    window.wait("visible", timeout=30)
    window.set_focus()
    time.sleep(3)

    window.capture_as_image().save(OUTPUT)
    print(f"Screenshot saved: {OUTPUT}")


if __name__ == "__main__":
    main()
