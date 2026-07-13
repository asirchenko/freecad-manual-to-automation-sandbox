"""Pillow helpers for screenshot validation."""

from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageChops


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


def image_diff_ratio(actual: Path, baseline: Path) -> float:
    """Return mean per-channel difference ratio in [0, 1]."""
    assert_screenshot_exists(actual)
    assert baseline.exists(), f"Baseline not found: {baseline}"

    with Image.open(actual) as actual_img, Image.open(baseline) as baseline_img:
        actual_rgb = actual_img.convert("RGB")
        baseline_rgb = baseline_img.convert("RGB")
        if actual_rgb.size != baseline_rgb.size:
            baseline_rgb = baseline_rgb.resize(actual_rgb.size)

        diff = ImageChops.difference(actual_rgb, baseline_rgb)
        histogram = diff.histogram()
        pixels = actual_img.size[0] * actual_img.size[1]
        channels = 3
        total_diff = 0.0
        for channel in range(channels):
            channel_hist = histogram[channel * 256 : (channel + 1) * 256]
            total_diff += sum(i * count for i, count in enumerate(channel_hist))
        max_diff = pixels * 255 * channels
        return total_diff / max_diff if max_diff else 0.0


def assert_image_matches_baseline(
    actual: Path,
    baseline: Path,
    *,
    max_diff_ratio: float = 0.05,
) -> None:
    """Compare screenshot to baseline (M5)."""
    ratio = image_diff_ratio(actual, baseline)
    assert ratio <= max_diff_ratio, (
        f"Screenshot differs from baseline: diff={ratio:.4f} max={max_diff_ratio} "
        f"actual={actual} baseline={baseline}"
    )


def save_as_baseline(source: Path, baseline: Path) -> None:
    """Copy a captured screenshot into baselines/ (one-time setup)."""
    assert_screenshot_exists(source)
    baseline.parent.mkdir(parents=True, exist_ok=True)
    with Image.open(source) as image:
        image.save(baseline)

