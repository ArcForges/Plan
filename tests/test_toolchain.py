"""Exercise exact interpreter selection with real processes and isolated pins."""
import io
from pathlib import Path
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "eng"))
import check_toolchain as toolchain  # noqa: E402


class ToolchainSelection(unittest.TestCase):
    def check(self):
        with redirect_stdout(io.StringIO()):
            return toolchain.check()

    def test_actual_interpreters_match_repository_pin(self):
        self.assertEqual(self.check(), [])

    def test_running_and_path_interpreters_both_reject_a_different_pin(self):
        with tempfile.TemporaryDirectory() as tmp:
            fixture = Path(tmp)
            (fixture / ".python-version").write_text("0.0.0\n", encoding="utf-8")
            with patch.object(toolchain, "ROOT", fixture):
                errors = self.check()
            self.assertTrue(any(error.startswith("Python ") for error in errors))
            self.assertTrue(any(error.startswith("PATH python ") for error in errors))


if __name__ == "__main__":
    unittest.main()
