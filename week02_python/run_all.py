"""Run all Week 2 Python exercises in order."""

from pathlib import Path
import runpy

FILES = [
    "01_variables.py",
    "02_conditions.py",
    "03_loops.py",
    "04_functions.py",
    "05_practice.py",
]


def main() -> None:
    base = Path(__file__).parent
    for filename in FILES:
        print("=" * 60)
        print(f"Running {filename}")
        print("=" * 60)
        runpy.run_path(str(base / filename), run_name="__main__")
        print()


if __name__ == "__main__":
    main()
