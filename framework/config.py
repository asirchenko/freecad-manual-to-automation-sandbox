"""Sandbox configuration — timeouts and paths (Week 17)."""

from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path

from framework.utils.paths import BASELINES_DIR, PROJECT_ROOT


@dataclass(frozen=True)
class SandboxConfig:
    """Central settings for tests and framework helpers."""

    project_root: Path = PROJECT_ROOT
    default_ui_timeout_sec: float = 30.0
    dialog_timeout_sec: float = 10.0
    stability_run_count: int = 5
    baseline_max_diff_ratio: float = 0.05
    freecad_cmd: Path = Path(r"C:\Program Files\FreeCAD 1.1\bin\freecadcmd.exe")

    @classmethod
    def from_env(cls) -> SandboxConfig:
        """Build config from optional environment overrides."""
        return cls(
            default_ui_timeout_sec=float(os.getenv("SANDBOX_UI_TIMEOUT", "30")),
            dialog_timeout_sec=float(os.getenv("SANDBOX_DIALOG_TIMEOUT", "10")),
            stability_run_count=int(os.getenv("SANDBOX_STABILITY_RUNS", "5")),
            baseline_max_diff_ratio=float(os.getenv("SANDBOX_BASELINE_MAX_DIFF", "0.05")),
            freecad_cmd=Path(os.getenv("FREECAD_CMD", str(cls.freecad_cmd))),
        )


def baseline_path(name: str, extension: str = "png") -> Path:
    """Return a path under baselines/."""
    BASELINES_DIR.mkdir(parents=True, exist_ok=True)
    return BASELINES_DIR / f"{name}.{extension}"


DEFAULT_CONFIG = SandboxConfig.from_env()
