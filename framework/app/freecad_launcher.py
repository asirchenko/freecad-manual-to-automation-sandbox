"""Launch and connect to FreeCAD via pywinauto."""

from __future__ import annotations

import subprocess
from pathlib import Path

from pywinauto import Application
from pywinauto.application import WindowSpecification
from pywinauto.findwindows import ElementNotFoundError

from framework.utils.logging_config import get_logger
from framework.utils.waits import wait_for_value

logger = get_logger(__name__)

DEFAULT_FREECAD_EXE = Path(r"C:\Program Files\FreeCAD 1.1\bin\freecad.exe")
DEFAULT_STARTUP_TIMEOUT_SEC = 90


class FreeCADLauncher:
    """Start FreeCAD, attach with UIA backend, and expose the main window."""

    def __init__(
        self,
        exe_path: Path | str = DEFAULT_FREECAD_EXE,
        startup_timeout_sec: float = DEFAULT_STARTUP_TIMEOUT_SEC,
    ) -> None:
        self.exe_path = Path(exe_path)
        self.startup_timeout_sec = startup_timeout_sec
        self._process: subprocess.Popen[str] | None = None
        self._app: Application | None = None

    @property
    def app(self) -> Application:
        if self._app is None:
            raise RuntimeError("FreeCAD is not running. Call launch() first.")
        return self._app

    @property
    def is_running(self) -> bool:
        return self._app is not None and self._process is not None

    def launch(self, open_path: Path | str | None = None) -> Application:
        """Start FreeCAD and connect pywinauto to the process."""
        if self.is_running:
            return self.app

        if not self.exe_path.exists():
            raise FileNotFoundError(f"FreeCAD executable not found: {self.exe_path}")

        command = [str(self.exe_path)]
        if open_path is not None:
            model = Path(open_path)
            if not model.exists():
                raise FileNotFoundError(f"Model file not found: {model}")
            command.append(str(model))

        self._process = subprocess.Popen(command)
        logger.info("Started FreeCAD pid=%s open_path=%s", self._process.pid, open_path)

        def connect_to_process() -> Application:
            if self._process is None:
                raise RuntimeError("FreeCAD process was not started")
            try:
                return Application(backend="uia").connect(process=self._process.pid, timeout=5)
            except ElementNotFoundError as exc:
                raise RuntimeError("FreeCAD UI not ready yet") from exc

        self._app = wait_for_value(
            connect_to_process,
            timeout_sec=self.startup_timeout_sec,
            poll_interval_sec=2.0,
            error_message="FreeCAD window did not appear",
        )
        logger.info("Connected to FreeCAD via UIA backend")
        return self._app

    def get_main_window(self) -> WindowSpecification:
        """Return the top-level FreeCAD window and wait until it is visible."""
        window = self.app.top_window()
        window.wait("visible", timeout=30)
        return window

    def close(self) -> None:
        """Close FreeCAD and release pywinauto resources."""
        if self._app is not None:
            try:
                self._app.kill()
            except Exception:
                if self._process is not None:
                    self._process.kill()
        elif self._process is not None:
            self._process.kill()

        self._app = None
        self._process = None
        logger.info("FreeCAD process closed")
