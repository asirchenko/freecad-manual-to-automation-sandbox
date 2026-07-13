"""Create models/sample_box.FCStd — run once via freecadcmd."""

from pathlib import Path

import FreeCAD as App
import Part

OUTPUT = Path(__file__).resolve().parents[1] / "models" / "sample_box.FCStd"

doc = App.newDocument("SampleBox")
box = Part.makeBox(10.0, 10.0, 10.0)
feature = doc.addObject("Part::Feature", "Box")
feature.Shape = box
doc.recompute()
doc.saveAs(str(OUTPUT))
App.closeDocument(doc.Name)
print(f"Saved: {OUTPUT}")
