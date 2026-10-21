# SPDX-License-Identifier: Apache-2.0
"""Tests of the shared verification core (eng/verify.py, the same file in every ArcForges repository).

Each test builds a throwaway repository with its own origin and step table and drives eng/verify.py as the hook does.
Only the Linux host runs here (the Windows leg is checked for being required, imported and refused); the tests are
skipped on other operating systems.
"""
from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
import tempfile
import time
import unittest
from pathlib import Path

CORE = Path(__file__).resolve().parent.parent / "eng" / "verify.py"

TABLE = '''REPOSITORY = "CoreTest-{name}"
FINGERPRINT = {{"linux": {{"bash": "bash --version | head -n 1"}}}}
def select_profile(changed): return "full"
STEPS = [
{steps}
]
'''


def run(argv: list[str], cwd: Path, stdin: str = "", env: dict[str, str] | None = None) -> subprocess.CompletedProcess:
    return subprocess.run(argv, cwd=cwd, input=stdin, capture_output=True, text=True, timeout=300,
                          env=dict(os.environ, **(env or {})))


@unittest.skipUnless(sys.platform.startswith("linux") and shutil.which("setsid") and shutil.which("timeout"),
                     "the Linux host of the verification core")
class VerifyCore(unittest.TestCase):
    def setUp(self) -> None:
        self.root = Path(tempfile.mkdtemp(prefix="verify-core-"))
        self.home = self.root / "home"
        self.home.mkdir()
        self.env = {"HOME": str(self.home), "GIT_CONFIG_GLOBAL": str(self.root / "gitconfig"),
                    "GIT_CONFIG_NOSYSTEM": "1"}
        (self.root / "gitconfig").write_text("[user]\n\temail = t@example.invalid\n\tname = t\n"
                                             "[init]\n\tdefaultBranch = main\n", encoding="utf-8")
        self.counter = 0

    def tearDown(self) -> None:
        shutil.rmtree(self.root, ignore_errors=True)

    def git(self, cwd: Path, *args: str) -> str:
        result = run(["git", *args], cwd, env=self.env)
        self.assertEqual(result.returncode, 0, result.stderr)
        return result.stdout.strip()

    def repository(self, steps: str, name: str = "a") -> Path:
        """A clone with an origin whose main holds the core and the table, and a feature commit on top."""
        self.counter += 1
        origin = self.root / f"origin-{name}-{self.counter}.git"
        self.git(self.root, "init", "-q", "--bare", str(origin))
        work = self.root / f"work-{name}-{self.counter}"
        self.git(self.root, "clone", "-q", str(origin), str(work))
        (work / "eng").mkdir()
        shutil.copy(CORE, work / "eng" / "verify.py")
        (work / "eng" / "verify_steps.py").write_text(TABLE.format(name=name, steps=steps), encoding="utf-8")
        (work / "a.txt").write_text("base\n", encoding="utf-8")
        self.git(work, "add", "-A")
        self.git(work, "commit", "-qm", "base")
        self.git(work, "push", "-q", "origin", "HEAD:main")
        self.git(work, "checkout", "-q", "-b", "feature")
        (work / "a.txt").write_text("change\n", encoding="utf-8")
        self.git(work, "commit", "-qam", "change")
        return work

    def verify(self, work: Path, *args: str, stdin: str = "") -> subprocess.CompletedProcess:
        return run([sys.executable, "eng/verify.py", *args], work, stdin=stdin, env=self.env)

    def pre_push(self, work: Path) -> subprocess.CompletedProcess:
        sha = self.git(work, "rev-parse", "HEAD")
        return self.verify(work, "pre-push", "origin", stdin=f"refs/heads/feature {sha} refs/heads/feature {'0' * 40}\n")

    def records(self, work: Path, host: str) -> list[Path]:
        return sorted((work / ".git" / "arcforges-verify").glob(f"leg-{host}-*.json"))

    def test_the_linux_leg_runs_natively_in_its_own_clone_and_is_reused(self) -> None:
        work = self.repository('Step("linux-a", "linux", "test \\"$PWD\\" = \\"$HOME/.cache/arcforges-verify/CoreTest-a\\" '
                               '&& test \\"$(git rev-parse HEAD)\\" = {sha} && test -z \\"$(git status --porcelain)\\" '
                               '&& echo $ARCFORGES_VERIFY-$X", timeout=60, env={"X": "y"})')
        first = self.verify(work, "run")
        self.assertEqual(first.returncode, 0, first.stdout + first.stderr)
        self.assertIn("arcforges-verify: LEG PASS", first.stdout)
        self.assertIn("arcforges-verify: PASS", first.stdout)
        [record] = self.records(work, "linux")
        data = json.loads(record.read_text(encoding="utf-8"))
        self.assertEqual(data["origin"], "local")
        self.assertEqual(data["sha"], self.git(work, "rev-parse", "HEAD"))
        log = Path(data["logs"]) / "linux-a.log"
        self.assertIn("1-y", log.read_text(encoding="utf-8"))
        self.assertTrue(data["results"][0]["log_sha256"])
        self.assertTrue((self.home / ".cache" / "arcforges-verify" / "CoreTest-a" / ".git").is_dir())
        second = self.verify(work, "run")
        self.assertIn("already passed", second.stdout)
        self.assertNotIn("LEG PASS", second.stdout)

    def test_a_missing_windows_leg_rejects_the_push(self) -> None:
        work = self.repository('Step("linux-a", "linux", "true", timeout=60),\n'
                               'Step("win-a", "win", ["cmd", "/c", "exit 0"], timeout=60)')
        run_result = self.verify(work, "run")
        self.assertEqual(run_result.returncode, 0, run_result.stderr)
        self.assertIn("arcforges-verify: INCOMPLETE", run_result.stdout)
        self.assertNotIn("arcforges-verify: PASS", run_result.stdout)
        push = self.pre_push(work)
        self.assertEqual(push.returncode, 1)
        self.assertIn("the win leg", push.stderr)
        self.assertIn("push rejected", push.stderr)

    def test_a_failed_step_fails_the_leg_and_records_nothing(self) -> None:
        work = self.repository('Step("linux-ok", "linux", "true", timeout=60),\n'
                               'Step("linux-bad", "linux", "echo broken; exit 3", timeout=60, lane="other")')
        result = self.verify(work, "run")
        self.assertEqual(result.returncode, 1)
        self.assertIn("linux-bad (exit code 3)", result.stderr)
        self.assertIn("broken", result.stdout)
        self.assertEqual(self.records(work, "linux"), [])
        self.assertEqual(self.pre_push(work).returncode, 1)

    def test_a_timed_out_step_is_stopped_with_its_children(self) -> None:
        marker = self.root / "child.pid"
        work = self.repository(f'Step("linux-slow", "linux", "sleep 300 & echo $! > {marker}; wait", timeout=3)')
        started = time.monotonic()
        result = self.verify(work, "run")
        self.assertEqual(result.returncode, 1)
        self.assertIn("timed out after 3s", result.stderr)
        self.assertLess(time.monotonic() - started, 120)
        child = int(marker.read_text().strip())
        time.sleep(1)
        self.assertFalse(Path(f"/proc/{child}").exists() and "sleep" in Path(f"/proc/{child}/cmdline").read_text(errors="replace"),
                         "the step's child process survived the timeout")

    def test_a_record_from_another_machine_is_imported_after_checking_it(self) -> None:
        steps = 'Step("linux-a", "linux", "true", timeout=60)'
        here = self.repository(steps, name="shared")
        there = self.root / "there"
        self.git(self.root, "clone", "-q", str(next(self.root.glob("origin-shared-*.git"))), str(there))
        self.git(there, "fetch", "-q", str(here), "feature")
        self.git(there, "checkout", "-q", "-B", "feature", "FETCH_HEAD")
        self.assertEqual(self.verify(there, "run").returncode, 0)
        [record] = self.records(there, "linux")
        copy = self.root / "record.json"
        shutil.copy(record, copy)
        imported = self.verify(here, "import", str(copy))
        self.assertEqual(imported.returncode, 0, imported.stderr)
        self.assertIn("arcforges-verify: IMPORTED", imported.stdout)
        push = self.pre_push(here)
        self.assertEqual(push.returncode, 0, push.stderr)
        self.assertIn("(imported,", push.stdout)
        self.assertNotIn("LEG PASS", push.stdout)

    def test_a_record_that_does_not_match_the_commit_is_refused(self) -> None:
        steps = 'Step("linux-a", "linux", "true", timeout=60)'
        work = self.repository(steps)
        self.assertEqual(self.verify(work, "run").returncode, 0)
        [record] = self.records(work, "linux")
        original = json.loads(record.read_text(encoding="utf-8"))
        record.unlink()
        forged = [
            ("tree", dict(original, tree="0" * 40)),
            ("profile", dict(original, profile="docs")),
            ("results", dict(original, results=[dict(original["results"][0], ok=False)])),
            ("results", dict(original, results=[])),
            ("steps", dict(original, steps=["linux-a", "linux-extra"])),
            ("digest", dict(original, digest="0" * 64)),
            ("context", dict(original, context={"design-main": "0" * 40})),
        ]
        for field, data in forged:
            path = self.root / f"forged-{field}.json"
            path.write_text(json.dumps(data), encoding="utf-8")
            result = self.verify(work, "import", str(path))
            self.assertEqual(result.returncode, 1, field)
            self.assertIn(field, result.stderr)
        unknown = self.root / "unknown-commit.json"
        unknown.write_text(json.dumps(dict(original, sha="1" * 40)), encoding="utf-8")
        self.assertIn("not in this clone", self.verify(work, "import", str(unknown)).stderr)
        self.assertEqual(self.records(work, "linux"), [], "no forged record was accepted")

    def test_a_windows_record_satisfies_the_windows_leg(self) -> None:
        work = self.repository('Step("linux-a", "linux", "true", timeout=60),\n'
                               'Step("win-a", "win", ["cmd", "/c", "exit 0"], timeout=60)')
        self.assertEqual(self.verify(work, "run").returncode, 0)
        [linux] = self.records(work, "linux")
        data = json.loads(linux.read_text(encoding="utf-8"))
        # The record eng/verify.py writes on Windows for this commit; the import recomputes and compares every field.
        script = ("import importlib.util; spec = importlib.util.spec_from_file_location('core', 'eng/verify.py'); "
                  "core = importlib.util.module_from_spec(spec); "
                  "import sys; sys.modules['core'] = core; spec.loader.exec_module(core); "
                  "print(core.target(core.Repository(), 'HEAD', 'origin').legs['win'].key)")
        computed = run([sys.executable, "-c", script], work, env=self.env)
        self.assertEqual(computed.returncode, 0, computed.stderr)
        full_key = computed.stdout.strip().splitlines()[-1]
        win = dict(data, host="win", key=full_key, steps=["win-a"], machine="WINBOX", tools={"python": "3.14"},
                   results=[{"step": "win-a", "ok": True, "seconds": 0.1, "reason": "", "log_sha256": "x"}])
        path = self.root / "win.json"
        path.write_text(json.dumps(win), encoding="utf-8")
        self.assertEqual(self.verify(work, "import", str(path)).returncode, 0)
        push = self.pre_push(work)
        self.assertEqual(push.returncode, 0, push.stderr)
        self.assertIn("win@WINBOX (imported", push.stdout)


if __name__ == "__main__":
    unittest.main()
