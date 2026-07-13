"""Logging setup for framework modules and pytest runs."""

from __future__ import annotations

import logging
import sys
from pathlib import Path

from framework.utils.paths import PROJECT_ROOT

LOG_DIR = PROJECT_ROOT / "artifacts" / "logs"
DEFAULT_LOG_FILE = LOG_DIR / "sandbox.log"


def setup_logging(
    level: int = logging.INFO,
    log_file: Path | None = DEFAULT_LOG_FILE,
    logger_name: str | None = None,
) -> logging.Logger:
    """Configure console + optional file logging for sandbox debugging."""
    target = logging.getLogger(logger_name) if logger_name else logging.getLogger()
    if target.handlers:
        return target

    target.setLevel(level)
    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
        datefmt="%H:%M:%S",
    )

    console = logging.StreamHandler(sys.stdout)
    console.setLevel(level)
    console.setFormatter(formatter)
    target.addHandler(console)

    if log_file is not None:
        log_file.parent.mkdir(parents=True, exist_ok=True)
        file_handler = logging.FileHandler(log_file, encoding="utf-8")
        file_handler.setLevel(level)
        file_handler.setFormatter(formatter)
        target.addHandler(file_handler)

    target.propagate = False
    return target


def get_logger(name: str) -> logging.Logger:
    """Return a named logger under the framework namespace."""
    return logging.getLogger(name)
