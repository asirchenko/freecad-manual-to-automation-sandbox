"""Project root and artifact path helpers."""

from __future__ import annotations

from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
ARTIFACTS_DIR = PROJECT_ROOT / "artifacts"
MODELS_DIR = PROJECT_ROOT / "models"
BASELINES_DIR = PROJECT_ROOT / "baselines"


def artifact_path(name: str, extension: str = "png") -> Path:
    """Return a path under artifacts/ and ensure the directory exists."""
    ARTIFACTS_DIR.mkdir(parents=True, exist_ok=True)
    return ARTIFACTS_DIR / f"{name}.{extension}"


def model_path(filename: str) -> Path:
    """Return path to a prepared model in models/."""
    return MODELS_DIR / filename
