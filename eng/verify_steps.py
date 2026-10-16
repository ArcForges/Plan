# SPDX-License-Identifier: Apache-2.0
"""Local verification steps of the ArcForges Plan, loaded by eng/verify.py (which injects `Step`).

The steps are exactly what .github/workflows/plan.yml runs for external PRs: the plan validation against ArcForges-Design
main, the design's traceability cross-check of delivery-graph.json, and the tool tests. Like CI, the Plan is validated
against the merged Design, never an unmerged branch: the Design main commit is fetched once, by the `design-main`
fingerprint probe (so that a pass is keyed to it and is not reused after Design main moves), and each lane checks that
commit out: a detached worktree of the sibling Design clone on Windows, a Linux-native clone in WSL. Markdown is this
repository's source (plan.py validates the sequence, register and roadmap), so every change runs the full profile, on
Windows and WSL Debian concurrently. actionlint runs only when a workflow changed.
"""
import subprocess
from pathlib import Path

REPOSITORY = "Plan"


def _design_clone() -> Path:
    """The ArcForges-Design clone next to this Plan clone's main checkout (C:/MyFile/Projects/ArcForges/<name>)."""
    common = subprocess.run(["git", "rev-parse", "--path-format=absolute", "--git-common-dir"], capture_output=True,
                            text=True, check=True).stdout.strip()
    return Path(common).parent.parent / "ArcForges-Design"


def _wsl_path(path: Path) -> str:
    text = path.resolve().as_posix()
    return "/mnt/" + text[0].lower() + text[2:] if text[1:2] == ":" else text


DESIGN = _design_clone()
DESIGN_MAIN = "refs/remotes/origin/main"
WIN_DESIGN = DESIGN / ".worktree" / "_plan-verify"
WSL_DESIGN = "$HOME/.cache/arcforges-verify/Plan-design-main"

# Tool versions that key a reusable pass (the python running eng/verify.py is added by the core), and the Design main
# commit the steps validate against: this probe fetches it (a read of existing access) and prints it.
FINGERPRINT = {
    "win": {
        "python": ["python", "--version"],
        "design-main": f'git -C "{DESIGN}" fetch --quiet --no-tags origin main && '
                       f'git -C "{DESIGN}" rev-parse {DESIGN_MAIN}',
    },
    "wsl": {"python": "python --version"},
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

WSL_REFRESH = (
    f"set -euo pipefail; d={WSL_DESIGN}; mkdir -p \"$d\"; cd \"$d\"; [ -d .git ] || git init -q; "
    f"git fetch -q --no-tags {_wsl_path(DESIGN / '.git')} {DESIGN_MAIN}; "
    "git checkout -q --force --detach FETCH_HEAD; git clean -ffdq; "
    "echo \"ArcForges-Design main $(git rev-parse HEAD) at $d\""
)

TESTS = "python -m unittest discover -s tests -v"

# actionlint as pinned in the product repositories' CI, cached once in WSL; the archive is checked on every run.
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
    Step("win-design-main", "win", ["python", "-c", WIN_REFRESH, str(DESIGN), str(WIN_DESIGN), DESIGN_MAIN],
         timeout=300, env=ENV),
    Step("win-validate", "win", ["python", "tools/plan.py", "validate", "--design", str(WIN_DESIGN)], timeout=300,
         env=ENV),
    Step("win-traceability", "win", ["python", str(WIN_DESIGN / "tools" / "check_design.py"), "--plan",
                                     "delivery-graph.json"], timeout=600, env=ENV),
    Step("win-tool-tests", "win", TESTS.split(), timeout=300, env=ENV),
    Step("wsl-design-main", "wsl", WSL_REFRESH, timeout=300, env=ENV),
    Step("wsl-validate", "wsl", f"python tools/plan.py validate --design {WSL_DESIGN}", timeout=300, env=ENV),
    Step("wsl-traceability", "wsl", f"python {WSL_DESIGN}/tools/check_design.py --plan delivery-graph.json",
         timeout=600, env=ENV),
    Step("wsl-tool-tests", "wsl", TESTS, timeout=300, env=ENV),
    Step("actionlint", "wsl", ACTIONLINT, timeout=300, lane="actionlint", when=workflows_changed),
]
