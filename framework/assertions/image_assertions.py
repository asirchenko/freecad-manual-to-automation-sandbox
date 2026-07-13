"""Pillow helpers for screenshot validation."""

from __future__ import annotations

from pathlib import Path

from PIL import Image


def assert_screenshot_exists(path: Path) -> None:
    assert path.exists(), f"Screenshot not found: {path}"


def assert_screenshot_not_empty(path: Path, min_size_bytes: int = 1000) -> None:
    """Verify the screenshot file exists and has a reasonable size."""
    assert_screenshot_exists(path)
    size = path.stat().st_size
    assert size >= min_size_bytes, f"Screenshot too small ({size} bytes): {path}"


def assert_screenshot_dimensions(path: Path, min_width: int = 100, min_height: int = 100) -> None:
    """Open the image with Pillow and verify width/height."""
    assert_screenshot_exists(path)
    with Image.open(path) as image:
        width, height = image.size
        assert width >= min_width, f"Screenshot width too small: {width}"
        assert height >= min_height, f"Screenshot height too small: {height}"
