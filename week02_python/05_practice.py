"""Week 2 — Part 5: Combined practice (mini scenario)."""

from __future__ import annotations


def evaluate_test(step_name: str, success: bool) -> str:
    if success:
        return f"[PASS] {step_name}"
    return f"[FAIL] {step_name}"


def run_junior_smoke_check() -> None:
    """Simulate a tiny test flow without real FreeCAD."""
    app_name = "FreeCAD"
    timeout_sec = 30
    steps = [
        ("Launch application", True),
        ("Wait for main window", True),
        ("Create new document", False),
    ]

    print(f"Smoke check for {app_name} (timeout {timeout_sec}s)\n")

    failed = 0
    for step_name, success in steps:
        line = evaluate_test(step_name, success)
        print(line)
        if not success:
            failed += 1

    print()
    if failed == 0:
        print("Result: ALL PASSED")
    else:
        print(f"Result: {failed} step(s) failed - investigate logs and screenshots")


if __name__ == "__main__":
    run_junior_smoke_check()
