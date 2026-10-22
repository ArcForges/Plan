# SPDX-License-Identifier: Apache-2.0
"""Local verification steps of the ArcForges Plan, loaded by eng/verify.py (which injects `Step`).

The steps are exactly what .github/workflows/plan.yml runs for external PRs: the plan validation against
ArcForges-Design main, the design's traceability cross-check of delivery-graph.json, and the tool tests. Like CI, the
Plan is validated against the merged Design, never an unmerged branch: the Design main commit is fetched and resolved
once when this table loads (DESIGN_SHA) and recorded as CONTEXT in each leg's summary (a status does not record it, so a
Plan head is verified again before its merge whenever Design main has moved; execution policy §4), and each leg checks out exactly that commit: a
detached worktree of the sibling Design clone on Windows, a clone fetched from the sibling Design clone on Linux.
Markdown is this repository's source (plan.py validates the sequence, register and roadmap), so every change runs the
full profile: the Windows leg on native Windows and the Linux leg on native Linux, each on its own host after the push
and reported as the commit statuses arcforges/windows and arcforges/linux (eng/verify.py; AGENTS.md rule 6).
actionlint runs only when a workflow changed.
"""
import shlex
import subprocess
from pathlib import Path

REPOSITORY = "Plan"


def _design_clone() -> Path:
    """The ArcForges-Design clone next to this Plan clone's main checkout (<projects>/ArcForges-Design)."""
    common = subprocess.run(["git", "rev-parse", "--path-format=absolute", "--git-common-dir"], capture_output=True,
                            text=True, check=True).stdout.strip()
    return Path(common).parent.parent / "ArcForges-Design"


DESIGN = _design_clone()
DESIGN_MAIN = "refs/remotes/origin/main"


def _design_main() -> str:
    """Fetches ArcForges-Design main (a read of existing access) once and returns its commit, which every step uses and
    each leg's summary records. A failed fetch fails verification."""
    try:
        subprocess.run(["git", "-C", str(DESIGN), "fetch", "--quiet", "--no-tags", "origin", "main"], check=True)
        return subprocess.run(["git", "-C", str(DESIGN), "rev-parse", f"{DESIGN_MAIN}^{{commit}}"], capture_output=True,
                              text=True, check=True).stdout.strip()
    except (subprocess.CalledProcessError, OSError) as error:
        raise RuntimeError(f"cannot fetch ArcForges-Design main in {DESIGN}: {error}; check "
                         "network access to GitHub and that clone, then verify again") from error


DESIGN_SHA = _design_main()
WIN_DESIGN = DESIGN / ".worktree" / "_plan-verify"
LINUX_DESIGN = "$HOME/.cache/arcforges-verify/Plan-design-main"

# The Design main commit every leg validates against (DESIGN_SHA, resolved once above), recorded in each leg's summary.
CONTEXT = {"design-main": DESIGN_SHA}

# Tool versions recorded in each leg's summary (the python running eng/verify.py is added by the core).
FINGERPRINT = {
    "win": {"python": ["python", "--version"]},
    "linux": {"python": "python --version"},
}

# The environment of plan.yml.
ENV = {"CI": "true", "PYTHONUTF8": "1"}

# Checks out the fetched Design main in a detached worktree of the Design clone (created on first use) and removes
# untracked files.
WIN_REFRESH = """
import subprocess, sys
from pathlib import Path
clone, tree, ref = Path(sys.argv[1]), Path(sys.argv[2]), sys.argv[3]
def git(*args, cwd):
    subprocess.run(['git', *args], cwd=cwd, check=True)
if (tree / '.git').exists():
    git('checkout', '--quiet', '--force', '--detach', ref, cwd=tree)
else:
    git('worktree', 'prune', cwd=clone)
    git('worktree', 'add', '--quiet', '--force', '--detach', str(tree), ref, cwd=clone)
git('clean', '-ffdq', cwd=tree)
head = subprocess.run(['git', 'rev-parse', 'HEAD'], cwd=tree, check=True, capture_output=True, text=True).stdout
print('ArcForges-Design main', head.strip(), 'at', tree)
"""

LINUX_REFRESH = (
    # A shallow Design clone would leave this clone incomplete without an error (as in eng/verify.py prepare_linux).
    f"set -euo pipefail; test \"$(git -C {shlex.quote(DESIGN.as_posix())} rev-parse --is-shallow-repository)\" = false "
    f"|| {{ echo \"the ArcForges-Design clone {DESIGN.as_posix()} is shallow; run git fetch --unshallow there\" >&2; exit 1; }}; "
    f"d={LINUX_DESIGN}; mkdir -p \"$d\"; cd \"$d\"; [ -d .git ] || git init -q; "
    f"git fetch -q --no-tags {shlex.quote((DESIGN / '.git').as_posix())} {DESIGN_MAIN}; "
    f"test \"$(git rev-parse FETCH_HEAD)\" = {DESIGN_SHA} || {{ echo \"ArcForges-Design main moved during "
    f"verification (expected {DESIGN_SHA}, got $(git rev-parse FETCH_HEAD)); run again\" >&2; exit 1; }}; "
    "git checkout -q --force --detach FETCH_HEAD; git clean -ffdq; "
    "echo \"ArcForges-Design main $(git rev-parse HEAD) at $d\""
)

TESTS = "python -m unittest discover -s tests -v"

# actionlint as pinned in the product repositories' CI, cached once on the Linux host; the archive is checked on every
# run.
ACTIONLINT = (
    "set -euo pipefail; v=1.7.12; "
    "sum=8aca8db96f1b94770f1b0d72b6dddcb1ebb8123cb3712530b08cc387b349a3d8; "
    "d=\"$HOME/.cache/arcforges-verify/tools\"; t=\"$d/actionlint_${v}_linux_amd64.tar.gz\"; mkdir -p \"$d\"; "
    "if [ ! -f \"$t\" ]; then "
    "curl --fail --silent --show-error --location --output \"$t.part\" "
    "\"https://github.com/rhysd/actionlint/releases/download/v${v}/actionlint_${v}_linux_amd64.tar.gz\"; "
    "echo \"$sum  $t.part\" | sha256sum --check --quiet; mv \"$t.part\" \"$t\"; fi; "
    "echo \"$sum  $t\" | sha256sum --check --quiet; "
    "mkdir -p \"$d/actionlint-$v\"; tar -xzf \"$t\" -C \"$d/actionlint-$v\" actionlint; "
    "\"$d/actionlint-$v/actionlint\""
)


def workflows_changed(changed: list[str]) -> bool:
    return any(path.startswith(".github/workflows/") for path in changed)


def select_profile(changed: list[str]) -> str:
    return "full"


STEPS = [
    Step("win-design-main", "win", ["python", "-c", WIN_REFRESH, str(DESIGN), str(WIN_DESIGN), DESIGN_SHA],
         timeout=300, env=ENV),
    Step("win-validate", "win", ["python", "tools/plan.py", "validate", "--design", str(WIN_DESIGN)], timeout=300,
         env=ENV),
    Step("win-traceability", "win", ["python", str(WIN_DESIGN / "tools" / "check_design.py"), "--plan",
                                     "delivery-graph.json"], timeout=600, env=ENV),
    Step("win-tool-tests", "win", TESTS.split(), timeout=300, env=ENV),
    Step("linux-design-main", "linux", LINUX_REFRESH, timeout=300, env=ENV),
    Step("linux-validate", "linux", f"python tools/plan.py validate --design {LINUX_DESIGN}", timeout=300, env=ENV),
    Step("linux-traceability", "linux", f"python {LINUX_DESIGN}/tools/check_design.py --plan delivery-graph.json",
         timeout=600, env=ENV),
    Step("linux-tool-tests", "linux", TESTS, timeout=300, env=ENV),
    Step("actionlint", "linux", ACTIONLINT, timeout=300, lane="actionlint", when=workflows_changed),
]
