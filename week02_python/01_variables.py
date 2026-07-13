"""Week 2 — Part 1: Variables."""

# --- Strings (str) ---
app_name = "FreeCAD"
workbench = "Part Design"
message = f"Launching {app_name} with {workbench} workbench"
print(message)

# --- Numbers (int, float) ---
startup_timeout_sec = 30
cube_size_mm = 10.0
print(f"Timeout: {startup_timeout_sec}s, cube edge: {cube_size_mm} mm")

# --- Booleans (bool) ---
is_running = False
is_running = True
print(f"FreeCAD running: {is_running}")

# --- Constants by convention (Python allows reassignment; we treat these as fixed) ---
FREECAD_EXE = r"C:\Program Files\FreeCAD 1.1\bin\freecad.exe"
print(f"Path: {FREECAD_EXE}")

# --- Reassignment ---
test_status = "pending"
test_status = "passed"
print(f"Test status: {test_status}")

# --- YOUR TURN ---
# 1. Create a variable author with your name.
# 2. Create a variable week_number = 2.
# 3. Print an f-string: "Week 2 — author: <name>"

author = "Artem Sirchenko"
week_number = 2
print(f"Week {week_number} - author: {author}")
