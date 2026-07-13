"""Helpers to dump UI control trees (pywinauto / Inspect-style debugging)."""

from __future__ import annotations

from collections.abc import Iterable
from typing import Any

from pywinauto import Desktop


def _safe_text(value: str | None) -> str:
    if not value:
        return ""
    return value.encode("ascii", errors="replace").decode("ascii")


def format_control_line(wrapper: Any, index: int) -> str:
    """One-line summary of a pywinauto wrapper."""
    try:
        title = _safe_text(wrapper.window_text())
        class_name = wrapper.class_name()
        control_type = getattr(wrapper, "element_info", None)
        ctype = control_type.control_type if control_type else "?"
        return f"[{index}] {ctype!r} class={class_name!r} title={title!r}"
    except Exception as exc:
        return f"[{index}] <unreadable: {exc}>"


def print_descendants(
    root: Any,
    *,
    max_depth: int = 3,
    control_type: str | None = None,
    label: str = "control tree",
) -> None:
    """Print a shallow descendant tree for locator debugging."""
    print(f"\n=== {label} (max_depth={max_depth}) ===")

    def walk(node: Any, depth: int) -> None:
        if depth > max_depth:
            return
        indent = "  " * depth
        try:
            title = _safe_text(node.window_text())
            class_name = node.class_name()
            ctype = node.element_info.control_type
            if control_type is None or ctype == control_type:
                print(f"{indent}{ctype!r} class={class_name!r} title={title!r}")
        except Exception as exc:
            print(f"{indent}<error: {exc}>")
            return

        if depth == max_depth:
            return
        try:
            for child in node.children():
                walk(child, depth + 1)
        except Exception:
            return

    walk(root, 0)


def list_top_windows(backend: str = "uia", *, control_type: str | None = None) -> list[str]:
    """List visible top-level window titles for the given backend."""
    lines: list[str] = []
    desktop = Desktop(backend=backend)
    windows: Iterable[Any] = (
        desktop.windows(control_type=control_type) if control_type else desktop.windows()
    )
    for index, window in enumerate(windows):
        lines.append(format_control_line(window, index))
    return lines


def print_top_windows(backend: str = "uia", *, label: str | None = None) -> None:
    """Print top-level windows to stdout."""
    title = label or f"top windows ({backend})"
    print(f"\n=== {title} ===")
    for line in list_top_windows(backend=backend):
        print(f"  {line}")
