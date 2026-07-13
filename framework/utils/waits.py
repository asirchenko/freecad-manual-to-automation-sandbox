"""Synchronization helpers — polling instead of fixed sleeps."""

from __future__ import annotations

import time
from collections.abc import Callable
from typing import TypeVar

T = TypeVar("T")


def wait_until(
    condition: Callable[[], bool],
    timeout_sec: float = 30.0,
    poll_interval_sec: float = 0.5,
    error_message: str = "Condition not met before timeout",
) -> None:
    """Poll condition until it returns True or timeout is reached."""
    deadline = time.time() + timeout_sec
    while time.time() < deadline:
        if condition():
            return
        time.sleep(poll_interval_sec)
    raise TimeoutError(error_message)


def wait_for_value(
    supplier: Callable[[], T],
    timeout_sec: float = 30.0,
    poll_interval_sec: float = 0.5,
    error_message: str = "Value not available before timeout",
) -> T:
    """Poll supplier until it returns without raising, then return the value."""
    deadline = time.time() + timeout_sec
    last_error: Exception | None = None

    while time.time() < deadline:
        try:
            return supplier()
        except Exception as exc:  # noqa: BLE001 — UI connect retries may raise varied errors
            last_error = exc
            time.sleep(poll_interval_sec)

    if last_error is not None:
        raise TimeoutError(f"{error_message}: {last_error}") from last_error
    raise TimeoutError(error_message)
