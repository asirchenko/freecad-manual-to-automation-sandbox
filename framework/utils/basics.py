"""Week 3 helpers — lists, dicts, and exceptions for pytest basics."""

from __future__ import annotations


def parse_menu_path(path: str) -> list[str]:
    """Split a menu breadcrumb like 'File > New' into parts."""
    return [part.strip() for part in path.split(">")]


def get_launch_config() -> dict[str, str | int]:
    """Return a default launch configuration for UI tests."""
    return {
        "app_name": "FreeCAD",
        "exe_path": r"C:\Program Files\FreeCAD 1.1\bin\freecad.exe",
        "timeout_sec": 30,
        "backend": "uia",
    }


def safe_int(value: str) -> int:
    """Convert a string to int; raise ValueError with a clear message on failure."""
    try:
        return int(value)
    except ValueError as exc:
        raise ValueError(f"Cannot convert '{value}' to int") from exc


def filter_passed(results: list[dict[str, str]]) -> list[dict[str, str]]:
    """Return only results where status is 'passed'."""
    return [item for item in results if item.get("status") == "passed"]


def merge_tags(*tag_groups: list[str]) -> list[str]:
    """Merge tag lists without duplicates, preserving order."""
    seen: set[str] = set()
    merged: list[str] = []
    for group in tag_groups:
        for tag in group:
            if tag not in seen:
                seen.add(tag)
                merged.append(tag)
    return merged
