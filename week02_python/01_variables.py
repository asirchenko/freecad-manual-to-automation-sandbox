"""Week 2 — Part 1: Variables (переменные)."""

# --- Строки (str) ---
app_name = "FreeCAD"
workbench = "Part Design"
message = f"Launching {app_name} with {workbench} workbench"
print(message)

# --- Числа (int, float) ---
startup_timeout_sec = 30
cube_size_mm = 10.0
print(f"Timeout: {startup_timeout_sec}s, cube edge: {cube_size_mm} mm")

# --- Логические значения (bool) ---
is_running = False
is_running = True
print(f"FreeCAD running: {is_running}")

# --- Константы по смыслу (Python не запрещает менять, но мы договариваемся не менять) ---
FREECAD_EXE = r"C:\Program Files\FreeCAD 1.1\bin\freecad.exe"
print(f"Path: {FREECAD_EXE}")

# --- Переименование / переприсваивание ---
test_status = "pending"
test_status = "passed"
print(f"Test status: {test_status}")

# --- YOUR TURN ---
# 1. Создайте переменную author со своим именем.
# 2. Создайте переменную week_number = 2.
# 3. Выведите f-string: "Week 2 — author: <имя>"

author = "Artem Sirchenko"
week_number = 2
print(f"Week {week_number} - author: {author}")
