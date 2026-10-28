# Agent instructions: ArcForges Plan

Read [execution-policy.md](execution-policy.md) and [delivery-procedure.md](delivery-procedure.md) before doing anything. They are binding.

1. **Strictly serial.**
   - One `active` task; `python tools/plan.py next` names it.
   - One delegated worker or reviewer at a time, without a required provider or model.
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
6. **Verification** ([AD-0016](https://github.com/ArcForges/ArcForges-Design/blob/main/docs/decisions/AD-0016-local-first-verification.md) as amended by [AD-0020](https://github.com/ArcForges/ArcForges-Design/blob/main/docs/decisions/AD-0020-post-push-verification-and-required-checks.md); hosts [AD-0019](https://github.com/ArcForges/ArcForges-Design/blob/main/docs/decisions/AD-0019-mcp-first-verification.md); every active repository, whose own `AGENTS.md` names its steps). Push → Fetch → Local verification → Report status → Required checks → Review → Merge.
   - **Merge gate.** Every PR into `main`, whoever wrote it, needs two things at its head commit:
     - the commit statuses its repository's `main` ruleset requires: `arcforges/windows` and `arcforges/linux`, or only `arcforges/linux` where the step table has no Windows steps (Contracts);
     - the independent review.

     The rulesets have no bypass actors and require the branch to be up to date with `main`. External PRs (anyone else, Dependabot included) also run the full hosted CI (`Verify` where required). A maintainer reads an external diff before any host verifies `refs/pull/<n>/head`, because the host runs that code (execution policy §3, §4).
   - **Push** the branch to GitHub; nothing is verified before a push. There is no pre-push hook. `python eng/verify.py install`, once per clone from the main checkout on `main`, installs the lightweight hooks where a repository has them (`pre-commit`) and removes the retired pre-push hook. It uses no `core.hooksPath`: it removes any, and refuses while one remains elsewhere.
   - **Two hosts.** Each step runs on one host, `win` (native Windows) or `linux` (native Linux), and `eng/verify.py` runs only the leg of its host's own operating system, never through WSL or a remote shell.
     - The Windows host is the owner's Windows 11 workstation, reached through the Windows MCP server.
     - The Linux host is the Linux MCP host (H-22: native Linux with a systemd user manager and cgroups v2 delegation), reached through the Linux MCP server.

     Both are standard MCP servers, the same for Claude Code and Codex; their client configuration and credentials stay outside the repositories. Local WSL is never a venue, not even as a fallback, and an agent's own sandbox is not a verification host (AD-0019).
   - **Fetch and verify on each host.** In the host's clone of the repository, fetch the pushed commit from GitHub and run the command in a worktree at it:

     ```
     git fetch origin <branch>
     git worktree add --detach .worktree/verify-<sha> <sha>
     cd .worktree/verify-<sha>
     python eng/verify.py run-and-report
     ```

     No Git bundle, record or other file travels between the hosts or through an agent's context.
   - **What runs.** The repository's CI-equivalent steps from `eng/verify_steps.py`, selected by the profile of the paths changed since the merge base with `main`. They run in `.worktree/_verify` on Windows and in a Linux-native clone on Linux. In the Plan, each leg runs:
     - `python tools/plan.py validate --design <Design>`;
     - `python <Design>/tools/check_design.py --plan delivery-graph.json`;
     - `python -m unittest discover -s tests -v`;
     - `actionlint` when `.github/workflows/**` changed.

     `<Design>` is ArcForges-Design `origin/main`, fetched when the leg starts. `python eng/verify.py list` shows each host's steps; `python eng/verify.py run` runs the leg without reporting.
   - **Report status.** The command reports `arcforges/windows` or `arcforges/linux` on that exact commit:
     - `pending` when it starts;
     - `success` only when every step of the leg ran and passed (or, where the step table selects no steps for this host, success saying so);
     - `failure` when a step failed, `error` when the leg could not complete.

     It exits non-zero unless it reported success. Every new push needs both hosts again. The host reports with `ARCFORGES_STATUS_TOKEN` when set (a token limited to commit statuses), otherwise with its own `gh` login; never print or copy either.
   - **Stop rule.** If the Linux (or Windows) MCP server is unavailable, unreachable or its host lacks a prerequisite, stop and report the exact failure: the status stays missing and the PR cannot merge. Never skip, mock or weaken a step, or run the leg elsewhere (local WSL or an agent's own sandbox included) (AD-0019 §5).
   - **Failures.** A failed, timed-out or unrunnable step (a missing tool) reports `failure` and prints the step, the last log lines and the log path; the logs and a `summary.json` stay on the host. Read the log, fix the cause, push, verify again.
   - **Statuses and rulesets.** A status is reported only by `python eng/verify.py run-and-report` on the host it names, at the commit it verified. Never post, edit or copy an `arcforges/*` status by hand (for example with `gh api …/statuses`). Never change a ruleset, branch protection or required check to get a PR merged.
   - AI agents must never use `git push --no-verify` to bypass required validation. They must also never disable, remove, modify, or otherwise circumvent the hooks or required checks merely to get a change through.
   - If validation fails, investigate and fix the underlying issue.
   - If a required local test cannot run, do not silently skip it or claim successful verification.
   - Changing `eng/verify*.py`, `.githooks/` or the rulesets as reviewed engineering work is allowed; changing them to get a change through is not.
7. **Efficient execution** (every repository; implementation repositories add only their concrete commands).
   - Run long commands in the background and wait for their completion notification. No sleep loops, fixed delays or CI polling.
   - Restore and build once, then use `--no-restore` and `--no-build`. Keep builds incremental and reuse existing caches (NuGet, npm, compiler caches); never clean or clear them without a cause.
   - While iterating, run the affected suites only. The full profile runs once per pushed head, on each host (rule 6); `python eng/verify.py run` checks a leg on its host without reporting.
   - Format only the changed files while iterating (`dotnet format --include <files>`); the full check runs in the host verification (rule 6).
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
   - The coordinator does not change repository security settings. The first exception is the required status checks of the conditional CI ([AD-0016](https://github.com/ArcForges/ArcForges-Design/blob/main/docs/decisions/AD-0016-local-first-verification.md) §2), which the coordinator may change only as the user authorized on 2026-10-16: "If existing required checks must be adjusted to support this conditional workflow, make the smallest appropriate changes." The second is the `main` rulesets that require the host statuses (AD-0020 §6), which the user authorized on 2026-10-22 for that migration. Neither is ever changed to get a PR merged.
   - Read hosted CI (external PRs) with the PR tools; never poll it.
   - Never enable auto-merge unless the user asks.
9. **Commits and PRs.** Any commit co-author trailer or PR footer must identify the actual contributors and tools used.
10. **Run gate and continuous execution.** No implementation starts until the user authorizes it with the execution prompt ([execution-prompt.md](execution-prompt.md)) and a pasted range of `sequence.md` steps. The range is the authorized scope and is recorded as a ledger `note` (execution policy §1.5). Deliver the eligible tasks of the range one at a time, without asking to continue, and never start a task outside the range.
11. **Stop points.** Stop and ask the user before outward-facing publication, when the authorized range is complete, when no eligible task remains in it, when a task outside the range is active, when no independent reviewer is available, when a decision only the user can make is required, or when the user says stop. When a human prerequisite (H-*) whose **Blocks** column in the acceptance register names a task is missing, set the task `blocked` with that ID (`plan.py set-state <id> blocked --blocked-by H-xx --reason ...`), tell the user exactly what is needed, and continue with the next eligible task of the range; blocked tasks and their dependents are skipped. Prerequisites that block only `complete`, or nothing, never block the task. Production prerequisites block only AF-PROD-01, because Cloud and Web tasks deploy dark.
12. **Roadmap.** [roadmap.md](roadmap.md) is the only backlog for work that is not committed delivery. Never implement a roadmap item; promotion to tasks follows roadmap.md §4.
