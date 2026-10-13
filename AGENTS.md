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
6. **Standing constraints.**
   - Never read or print secrets.
   - Cloudflare only through repository scripts; `workers.dev` and previews off.
   - Production changes only through main-push deploys.
   - No proxy or network changes.
   - Diagnose before rerunning; bounded backoff; inspect remote state before retrying a write.
   - Never unpublish, deprecate or delete a version; never pin or admit the rolled-back versions.
   - Dependabot PRs untouched.
   - No macOS, device, GUI, browser, live or inference CI.
   - WSL2 Debian for Linux tests, with installs by the user. No SSH.
   - The coordinator does not change repository security settings.
   - Never poll CI; use the PR tools.
   - Never enable auto-merge unless the user asks.
7. **Commits and PRs.** Commit messages end with `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`. PR bodies end with `🤖 Generated with [Claude Code](https://claude.com/claude-code)`.
8. **Run gate and continuous execution.** No implementation starts until the user authorizes it; the authorization is recorded as a ledger `note` (execution policy §1.5), and without that record a session only reports status. Once authorized, deliver eligible tasks one at a time and continue with `plan.py next` after each delivery, without asking to continue (execution policy §1.5).
9. **Stop points.** Stop and ask the user before outward-facing publication, when no eligible task remains, when a decision only the user can make is required, or when the user says stop. When a human prerequisite (H-*) whose **Blocks** column in the acceptance register names this task is missing, set the task `blocked` with that ID (`plan.py set-state <id> blocked --blocked-by H-xx --reason ...`), tell the user exactly what is needed, and continue with `plan.py next`, which skips blocked tasks and their dependents. Prerequisites that block only `complete`, or nothing, never block the task. Production prerequisites block only AF-PROD-01, because Cloud and Web tasks deploy dark.
