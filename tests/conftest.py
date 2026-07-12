"""Shared pytest fixtures."""

from __future__ import annotations

from collections.abc import Iterator

import pytest

from framework.app.freecad_launcher import FreeCADLauncher


@pytest.fixture
def freecad_app() -> Iterator[FreeCADLauncher]:
    """Launch FreeCAD before a test and close it afterward."""
    launcher = FreeCADLauncher()
    launcher.launch()
    yield launcher
    launcher.close()
