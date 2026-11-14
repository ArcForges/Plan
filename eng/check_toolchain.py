"""Require the same pinned interpreter for the runner, steps and hosted CI."""
import json
from pathlib import Path
import platform
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parent.parent


def check() -> list[str]:
    expected = (ROOT / ".python-version").read_text(encoding="utf-8").strip()
    actual = platform.python_version()
    errors = []
    if actual != expected:
        errors.append(f"Python {actual} at {sys.executable}; expected {expected}")
    selected = shutil.which("python")
    if not selected:
        return errors + ["python must be on PATH"]
    result = subprocess.run([selected, "--version"], capture_output=True, text=True, check=False)
    if result.returncode or result.stdout.strip() != f"Python {expected}":
        errors.append(f"PATH python at {selected} does not select {expected}")
    print(json.dumps({"python": actual, "python_executable": sys.executable,
                      "path_python": selected, "expected_python": expected}, ensure_ascii=True))
    return errors


def main() -> int:
    errors = check()
    for error in errors:
        print("toolchain mismatch: " + error, file=sys.stderr)
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
