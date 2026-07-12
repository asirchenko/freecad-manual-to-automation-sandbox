"""Week 3 — Python Part 2: lists, dict, exceptions, modules (pytest)."""

import pytest

from framework.utils.basics import (
    filter_passed,
    get_launch_config,
    merge_tags,
    parse_menu_path,
    safe_int,
)


class TestLists:
    """List operations used in test data and menu paths."""

    def test_parse_menu_path_splits_parts(self) -> None:
        parts = parse_menu_path("File > New > Document")
        assert parts == ["File", "New", "Document"]
        assert len(parts) == 3

    def test_merge_tags_removes_duplicates(self) -> None:
        junior = ["smoke", "junior"]
        launch = ["junior", "freecad"]
        assert merge_tags(junior, launch) == ["smoke", "junior", "freecad"]


class TestDict:
    """Dictionary lookups for config and test metadata."""

    def test_launch_config_has_required_keys(self) -> None:
        config = get_launch_config()
        assert config["app_name"] == "FreeCAD"
        assert config["backend"] == "uia"
        assert config["timeout_sec"] >= 1

    def test_filter_passed_keeps_only_passed_results(self) -> None:
        results = [
            {"name": "launch", "status": "passed"},
            {"name": "dialog", "status": "failed"},
            {"name": "screenshot", "status": "passed"},
        ]
        passed = filter_passed(results)
        assert len(passed) == 2
        assert all(item["status"] == "passed" for item in passed)


class TestExceptions:
    """Explicit error handling before real UI failures."""

    def test_safe_int_accepts_numeric_string(self) -> None:
        assert safe_int("42") == 42

    def test_safe_int_rejects_invalid_string(self) -> None:
        with pytest.raises(ValueError, match="Cannot convert 'abc' to int"):
            safe_int("abc")


class TestModules:
    """Import project modules the same way tests will in later weeks."""

    def test_basics_module_exports_helpers(self) -> None:
        from framework.utils import basics

        assert callable(basics.parse_menu_path)
        assert callable(basics.get_launch_config)
        assert basics.parse_menu_path("View > Fit All") == ["View", "Fit All"]
