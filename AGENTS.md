# Agent instructions: ArcForges Plan

Read [execution-policy.md](execution-policy.md) and [delivery-procedure.md](delivery-procedure.md) before doing anything. They are binding.

1. **Strictly serial.**
   - One `active` task; `python tools/plan.py next` names it.
   - One delegated worker or reviewer at a time, Opus 5.5 only, never Haiku.
   - No build slot, no claims, no leases.
2. **Never resume history.** Nothing from Plan-Parallel, the old launcher or old claims is resumed ([history/legacy-disposition.md](history/legacy-disposition.md)).
3. **Worktrees.** Work in worktrees (`<repo>/.worktree/<key>`), never in main checkouts. This applies to the Plan too: `plan/<topic>` branches in `.worktree/`.
4. **Records.**
   - The coordinator alone updates graph states and the ledger, through `tools/plan.py`.
   - `sequence.md` is generated; never edit it by hand.
   - `python tools/plan.py validate --design <ArcForges-Design root>` must pass before any Plan PR.
5. **Verification.** Distinct evidence only (execution policy §3).
   - Fakes are allowed only where a task lists them.
   - Real-world validation that cannot run now goes to the acceptance register and is never reported as proven.
6. **Local verification** ([AD-0016](https://github.com/ArcForges/ArcForges-Design/blob/main/docs/decisions/AD-0016-local-first-verification.md), topology [AD-0018](https://github.com/ArcForges/ArcForges-Design/blob/main/docs/decisions/AD-0018-native-platforms-without-wsl-integration.md) §5 as amended by [AD-0019](https://github.com/ArcForges/ArcForges-Design/blob/main/docs/decisions/AD-0019-mcp-first-verification.md); every active repository, whose own `AGENTS.md` names its steps).
   - **Merge gate.** The owner's (`deku2026`) PRs: the pre-push verification at the pushed head, whose `arcforges-verify: PASS` line and each leg's `LEG PASS` line the coordinator quotes in the PR, plus the independent review; hosted validation is skipped for them. External PRs (anyone else, Dependabot included): full hosted CI plus review, and no hook is required (execution policy §3, §4).
   - **Install** once per clone, from the main checkout on `main`: `python eng/verify.py install` copies `.githooks/*` into the clone's common hooks directory and makes them executable (Git skips a non-executable hook with only a hint), so every worktree runs them. It uses no `core.hooksPath`: it removes any, including per-worktree values left by older scripts, and refuses while one remains elsewhere. Re-run it when `.githooks/` changes, and once in a Linux or macOS clone installed by an earlier `eng/verify.py`, whose hooks it left non-executable. A push from a worktree whose commit has no `eng/verify.py` is rejected; rebase it onto `main`.
   - **Two legs on two machines.** Each step runs on one host, `win` (native Windows) or `linux` (native Linux). `eng/verify.py` runs only the leg of the machine's own operating system, never through WSL or a remote shell: the Windows leg on the owner's Windows 11 workstation, through the Windows MCP server, in an isolated worktree at the exact commit; the Linux leg on the Linux MCP host (H-22: native Linux with a systemd user manager and cgroups v2 delegation), through the Linux MCP server, in a Linux-native clone at the exact commit. Both are standard MCP servers, the same for Claude Code and Codex; their client configuration and credentials stay outside the repositories. Local WSL is never a venue, not even as a fallback, and need not be installed; an agent's own sandbox is not a Linux verification host (AD-0019). Until the Linux MCP server exists (H-22), no Linux leg can be recorded and every push is rejected; there is no transition venue (AD-0019 §8).
   - **Stop rule.** If the Linux (or Windows) MCP server is unavailable, unreachable or its host lacks a prerequisite, stop verification and report the exact failure: the leg has no record, so the push stays rejected. Never skip, mock or weaken a step, run the leg elsewhere (local WSL or an agent's own sandbox included), write a record by hand, or bypass the hook (AD-0019 §5).
   - **What it runs.** Each pushed commit, never the working tree, in `.worktree/_verify` (Windows) or a Linux-native clone (Linux): the repository's CI-equivalent steps from `eng/verify_steps.py`. Commits already in `origin/main` are skipped. In the Plan: `python tools/plan.py validate --design <Design>`, `python <Design>/tools/check_design.py --plan delivery-graph.json` and `python -m unittest discover -s tests -v`, where `<Design>` is ArcForges-Design `origin/main`, fetched by the hook (as CI checks out Design main); plus `actionlint` when `.github/workflows/**` changed.
   - `python eng/verify.py list` shows the steps and each leg's state; `python eng/verify.py run` verifies this machine's leg of `HEAD` now and records it, keyed by the tree, the merge base, the step set, the scripts and the table's context (in the Plan, the Design main commit); a local record is reused while the tool versions are unchanged.
   - **The other leg.** Check out the exact commit on the other machine in a worktree of its clone (a commit not yet on GitHub travels as a Git bundle: `git bundle create <file> HEAD --not origin/main` here, `git fetch <file> HEAD` and `git worktree add --detach .worktree/<key> FETCH_HEAD` there), run `python eng/verify.py run` there, and accept its record here with `python eng/verify.py import <record>`, which recomputes the key and refuses any mismatch or any step that did not pass. A push needs a passed or imported record of every leg of every pushed commit.
   - **Failures.** A failed, timed-out or unrunnable step (a missing tool) or a missing leg record rejects the push and prints the step, the last log lines and the log path. Read the log, fix the cause, push again.
   - AI agents must never use `git push --no-verify` to bypass required validation. They must also never disable, remove, modify, or otherwise circumvent the hooks merely to allow a push.
   - Only `python eng/verify.py import` brings in another machine's leg, and only the record that `python eng/verify.py run` wrote on that machine at the exact commit: writing, editing or reusing a pass record by hand is circumventing the hooks.
   - If validation fails, investigate and fix the underlying issue.
   - If a required local test cannot run, do not silently skip it or claim successful verification.
   - Changing `eng/verify*.py` or `.githooks/` as reviewed engineering work is allowed; changing them to get a push through is not.
7. **Efficient execution** (every repository; implementation repositories add only their concrete commands).
   - Run long commands in the background and wait for their completion notification. No sleep loops, fixed delays or CI polling.
   - Restore and build once, then use `--no-restore` and `--no-build`. Keep builds incremental and reuse existing caches (NuGet, npm, compiler caches); never clean or clear them without a cause.
   - While iterating, run the affected suites only. The full profile runs once, through the hook; running `python eng/verify.py run` before handover lets the push reuse it.
   - Format only the changed files while iterating (`dotnet format --include <files>`); the full check runs in the hook.
   - Within one task, run independent work in parallel with the repository's bounded defaults: test projects, AOT components, the lanes of a leg, and the Windows and Linux legs on their two machines. Never add `-m:1`, `--max-parallel-threads 1` or serial collections without a measured reason.
   - Reviewers add a worktree to the existing clone (`git worktree add`) instead of cloning, and re-run only distinct evidence.
   - Measure before restricting parallelism or resources, and record the measurement.
   - This is parallelism inside one task. Delivery stays strictly serial (rule 1): no parallel tasks and no extra agents.
8. **Standing constraints.**
   - Never read or print secrets.
   - Cloudflare only through repository scripts; `workers.dev` and previews off.
   - Production changes only through main-push deploys.
   - No proxy or network changes.
   - Diagnose before rerunning; bounded backoff; inspect remote state before retrying a write.
   - Never unpublish, deprecate or delete a version; never pin or admit the rolled-back versions.
   - Dependabot PRs untouched.
   - No macOS, device, GUI, browser, live or inference CI.
   - Linux tests on the Linux MCP host and Windows tests on the native Windows workstation, each through its MCP server (rule 6); installs on both are the user's. No local WSL, not even as a fallback. No SSH.
   - The coordinator does not change repository security settings. The one exception is the required status checks of the conditional CI ([AD-0016](https://github.com/ArcForges/ArcForges-Design/blob/main/docs/decisions/AD-0016-local-first-verification.md) §2), which the coordinator may change only as the user authorized on 2026-10-16: "If existing required checks must be adjusted to support this conditional workflow, make the smallest appropriate changes."
   - Read hosted CI (external PRs) with the PR tools; never poll it.
   - Never enable auto-merge unless the user asks.
9. **Commits and PRs.** Commit messages end with `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`. PR bodies end with `🤖 Generated with [Claude Code](https://claude.com/claude-code)`.
10. **Run gate and continuous execution.** No implementation starts until the user authorizes it with the execution prompt ([execution-prompt.md](execution-prompt.md)) and a pasted range of `sequence.md` steps. The range is the authorized scope and is recorded as a ledger `note` (execution policy §1.5). Deliver the eligible tasks of the range one at a time, without asking to continue, and never start a task outside the range.
11. **Stop points.** Stop and ask the user before outward-facing publication, when the authorized range is complete, when no eligible task remains in it, when a task outside the range is active, when no confirmed Opus 5.5 reviewer is available, when a decision only the user can make is required, or when the user says stop. When a human prerequisite (H-*) whose **Blocks** column in the acceptance register names a task is missing, set the task `blocked` with that ID (`plan.py set-state <id> blocked --blocked-by H-xx --reason ...`), tell the user exactly what is needed, and continue with the next eligible task of the range; blocked tasks and their dependents are skipped. Prerequisites that block only `complete`, or nothing, never block the task. Production prerequisites block only AF-PROD-01, because Cloud and Web tasks deploy dark.
12. **Roadmap.** [roadmap.md](roadmap.md) is the only backlog for work that is not committed delivery. Never implement a roadmap item; promotion to tasks follows roadmap.md §4.
