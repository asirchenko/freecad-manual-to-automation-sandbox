"""Week 2 — Part 4: Functions (функции)."""


def greet(name: str) -> str:
    """Return a greeting string."""
    return f"Hello, {name}!"


def is_timeout_valid(timeout_sec: int) -> bool:
    """Return True if timeout is in allowed range for UI waits."""
    return 1 <= timeout_sec <= 120


def build_artifact_path(test_name: str, extension: str = "png") -> str:
    """Build a relative artifact path for a screenshot."""
    safe_name = test_name.lower().replace(" ", "_")
    return f"artifacts/{safe_name}.{extension}"


def summarize_run(passed: int, failed: int) -> None:
    """Print a one-line test run summary."""
    total = passed + failed
    print(f"Run complete: {passed}/{total} passed, {failed} failed")


# --- Вызовы ---
print(greet("Artem"))
print(f"Timeout 30 valid: {is_timeout_valid(30)}")
print(f"Timeout 200 valid: {is_timeout_valid(200)}")
print(f"Artifact path: {build_artifact_path('Launch FreeCAD')}")
summarize_run(passed=3, failed=1)


# --- YOUR TURN ---
# Напишите функцию cube_volume(edge_mm: float) -> float
# Формула: edge ** 3
# Проверьте для edge_mm = 10.0 (ожидается 1000.0)

def cube_volume(edge_mm: float) -> float:
    return edge_mm ** 3


print(f"Cube volume (10 mm edge): {cube_volume(10.0)}")
