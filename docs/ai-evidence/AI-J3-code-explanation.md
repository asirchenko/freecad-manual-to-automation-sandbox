# AI-J3 — Code Explanation (own words)

## Subject

`MainWindow.show_tree_item()` — why it exists and how it works.

## Explanation

FreeCAD models created with `freecadcmd` are saved without GUI visibility flags. When the same file opens in the desktop app, the Part feature can exist in the tree but stay hidden, so viewport screenshots look empty.

The helper:

1. Finds the tree item by exact label first (avoids matching the document name).
2. Right-clicks to open Qt's context menu (Space via UIA did not toggle visibility).
3. Clicks **Show Selection** on the `QMenu` window found through `Desktop(backend="uia")`.

This is a workflow outcome fix — not just checking that a button exists.

## Related tests

- J3: `show_tree_item("box")`
- M5/M6: same pattern before viewport capture

## Reference

`framework/ui/main_window.py` — `show_tree_item`, `find_tree_item`
