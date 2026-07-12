"""Week 2 — Part 2: Conditions (условия)."""

test_status = "failed"
error_message = "Main window not found"

# --- if / else ---
if test_status == "passed":
    print("Test OK - continue suite")
else:
    print(f"Test failed: {error_message}")

# --- if / elif / else ---
exit_code = 1

if exit_code == 0:
    result = "success"
elif exit_code == 1:
    result = "assertion error"
else:
    result = "unknown error"

print(f"Exit code {exit_code} -> {result}")

# --- Сравнения и логика ---
timeout_sec = 45
window_visible = True

if timeout_sec >= 30 and window_visible:
    print("Ready to capture screenshot")
else:
    print("Not ready yet")

# --- Проверка вхождения строки (полезно для заголовков окон) ---
window_title = "FreeCAD 1.1.1 - Start"

if "FreeCAD" in window_title:
    print("Correct application window")
else:
    print("Unexpected window")

# --- YOUR TURN ---
# Напишите условие: если app_version начинается с "1.", вывести "Supported major version"
app_version = "1.1.1"

if app_version.startswith("1."):
    print("Supported major version")
