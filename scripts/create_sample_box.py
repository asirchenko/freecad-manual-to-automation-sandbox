"""Create models/sample_box.FCStd — run once via freecadcmd."""

import FreeCAD as App
import Part

OUTPUT = r"c:\!!!PROJECT\Cursor Projects\Sandbox\freecad-manual-to-automation-sandbox\models\sample_box.FCStd"

doc = App.newDocument("SampleBox")
box = Part.makeBox(10.0, 10.0, 10.0)
feature = doc.addObject("Part::Feature", "Box")
feature.Shape = box
doc.recompute()
doc.saveAs(OUTPUT)
App.closeDocument(doc.Name)
print(f"Saved: {OUTPUT}")
