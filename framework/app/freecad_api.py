"""Run FreeCAD Python scripts via freecadcmd (headless CAD API)."""

from __future__ import annotations

import subprocess
import textwrap
from pathlib import Path

DEFAULT_FREECAD_CMD = Path(r"C:\Program Files\FreeCAD 1.1\bin\freecadcmd.exe")


class FreeCADApiRunner:
    """Execute FreeCAD API code outside the GUI process."""

    def __init__(self, freecadcmd_path: Path | str = DEFAULT_FREECAD_CMD) -> None:
        self.freecadcmd_path = Path(freecadcmd_path)

    def run_script(self, script: str) -> str:
        if not self.freecadcmd_path.exists():
            raise FileNotFoundError(f"freecadcmd not found: {self.freecadcmd_path}")

        wrapped = textwrap.dedent(script).strip()
        result = subprocess.run(
            [str(self.freecadcmd_path), "-c", wrapped],
            capture_output=True,
            text=True,
            check=False,
        )
        if result.returncode != 0:
            raise RuntimeError(
                f"freecadcmd failed ({result.returncode}): {result.stderr or result.stdout}"
            )
        return result.stdout

    def create_box_bounding_box(self, length: float, width: float, height: float) -> tuple[float, float, float]:
        """Create a box via Part.makeBox and return bounding-box dimensions."""
        script = f"""
import FreeCAD as App
import Part

doc = App.newDocument("BoxDoc")
shape = Part.makeBox({length}, {width}, {height})
obj = doc.addObject("Part::Feature", "Cube")
obj.Shape = shape
doc.recompute()
bb = obj.Shape.BoundBox
print(bb.XLength)
print(bb.YLength)
print(bb.ZLength)
App.closeDocument(doc.Name)
"""
        output = self.run_script(script)
        lines = [line.strip() for line in output.splitlines() if line.strip()]
        numeric = [line for line in lines if _is_float(line)]
        if len(numeric) < 3:
            raise RuntimeError(f"Unexpected freecadcmd output: {output!r}")
        return float(numeric[-3]), float(numeric[-2]), float(numeric[-1])

    def create_box_and_save(
        self,
        output_path: Path | str,
        length: float,
        width: float,
        height: float,
    ) -> tuple[float, float, float]:
        """Create a box, save as .FCStd, and return bounding-box dimensions."""
        path = Path(output_path).resolve()
        path.parent.mkdir(parents=True, exist_ok=True)
        path_posix = str(path).replace("\\", "/")

        script = f"""
import FreeCAD as App
import Part

doc = App.newDocument("E2EDoc")
shape = Part.makeBox({length}, {width}, {height})
obj = doc.addObject("Part::Feature", "Cube")
obj.Shape = shape
doc.recompute()
bb = obj.Shape.BoundBox
doc.saveAs(r"{path_posix}")
print(bb.XLength)
print(bb.YLength)
print(bb.ZLength)
App.closeDocument(doc.Name)
"""
        output = self.run_script(script)
        if not path.exists():
            raise RuntimeError(f"Expected saved document at {path}")

        lines = [line.strip() for line in output.splitlines() if line.strip()]
        numeric = [line for line in lines if _is_float(line)]
        if len(numeric) < 3:
            raise RuntimeError(f"Unexpected freecadcmd output: {output!r}")
        return float(numeric[-3]), float(numeric[-2]), float(numeric[-1])

    def save_document_copy(self, source_path: Path | str, dest_path: Path | str) -> None:
        """Load an FCStd file and save a copy to a new path."""
        source = Path(source_path).resolve()
        dest = Path(dest_path).resolve()
        dest.parent.mkdir(parents=True, exist_ok=True)
        source_posix = str(source).replace("\\", "/")
        dest_posix = str(dest).replace("\\", "/")

        script = f"""
import FreeCAD as App

doc = App.openDocument(r"{source_posix}")
doc.saveAs(r"{dest_posix}")
App.closeDocument(doc.Name)
"""
        self.run_script(script)
        if not dest.exists():
            raise RuntimeError(f"Expected saved copy at {dest}")

    def read_bounding_box_from_model(self, model_path: Path | str) -> tuple[float, float, float]:
        """Open an FCStd file and return the first Part feature bounding box."""
        path = Path(model_path).resolve()
        if not path.exists():
            raise FileNotFoundError(f"Model not found: {path}")
        path_posix = str(path).replace("\\", "/")

        script = f"""
import FreeCAD as App

doc = App.openDocument(r"{path_posix}")
obj = doc.Objects[0]
bb = obj.Shape.BoundBox
print(bb.XLength)
print(bb.YLength)
print(bb.ZLength)
App.closeDocument(doc.Name)
"""
        output = self.run_script(script)
        lines = [line.strip() for line in output.splitlines() if line.strip()]
        numeric = [line for line in lines if _is_float(line)]
        if len(numeric) < 3:
            raise RuntimeError(f"Unexpected freecadcmd output: {output!r}")
        return float(numeric[-3]), float(numeric[-2]), float(numeric[-1])

    def create_box_in_document(
        self,
        output_path: Path | str,
        length: float,
        width: float,
        height: float,
        *,
        object_name: str = "MiddleBox",
    ) -> tuple[float, float, float]:
        """Create a box in a new document and save (M3)."""
        return self.create_box_and_save(output_path, length, width, height)


def _is_float(value: str) -> bool:
    try:
        float(value)
        return True
    except ValueError:
        return False
