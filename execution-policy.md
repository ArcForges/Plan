# Execution policy (serial)

Authority: ArcForges-Design [AD-0014](https://github.com/ArcForges/ArcForges-Design/blob/main/docs/decisions/AD-0014-delivery-method.md). This policy replaces every earlier Plan-Parallel policy (`execution-policy.md`, `single-task-command.md`, `arcforges-implementation.md`, the build slot and claims and leases), which are history only.

## 1. One task at a time

1. Exactly one task in [delivery-graph.json](delivery-graph.json) may be `active`. `python tools/plan.py next` names it, or names the next task to start.
2. The next task to start is the first `planned` task in serial order whose dependencies are `delivered`, `complete` or `superseded`. The order in the graph is the order of work. Do not reorder, skip or start tasks early.
3. **Delegation.**
   - A coordinator session may delegate to **one** worker or reviewer at a time, using **Opus 5.5** only. Never Haiku.
   - No parallel research, implementation or review workstreams.
   - A delegate works only in its task's worktree and never pushes, posts, merges or deploys. The coordinator does those (§4).
4. **No build slot.** There is no workstation lock and no "retry for a slot". Long checks run once, in the background when practical, and their results are read rather than polled in loops.

## 2. Task states

| State | Meaning | Set by |
|---|---|---|
| `planned` | Not started | — |
| `active` | Being implemented | Coordinator, when work starts (`plan.py set-state <id> active` plus a ledger `started` record) |
| `delivered` | Merged at the reviewed head, published or deployed where applicable, and its own development-stage acceptance met | Coordinator, after merge and publication checks (`--merge REPO@SHA`) |
| `complete` | Delivered, and every completion prerequisite holds, including the real-environment evidence possible now. Deferred real-world validation is recorded in the acceptance register. | Coordinator |
| `superseded` | Replaced by a design decision (with reason) | Coordinator, with a ledger record |

A task that cannot finish because a human step is missing completes everything else, records the exact pending step in [acceptance-register.md](acceptance-register.md), and the plan continues with the next task.

## 3. Verification responsibilities (distinct evidence only)

| Role | Runs | Never |
|---|---|---|
| Author | Targeted and affected tests, affected real Windows/WSL2 tests, build and AOT publish of affected components, format and analyzers. Records exact commands and results in the PR. | Skips tests it changed or that cover changed code |
| Independent reviewer (one session, after the author) | Reads the complete diff at the exact head against the task's design references and acceptance criteria. Re-runs only what gives distinct evidence: a doubted test, a check whose script or workflow the PR changed, or a real-environment test the author could not run. | Repeats the author's identical full suite on the same unchanged head |
| Hosted CI | The repository's CI: the merge gate for platform-independent checks | GUI, device, browser-E2E, live-service or inference jobs |
| Coordinator | Push, PR, review record, CI result reading, merge at the reviewed head, publication or deployment check, graph state and ledger | Duplicates any of the above |

- **Re-review** after fixes covers only the delta, unless the delta changes build or test infrastructure.
- **Fakes** are allowed only where a task lists them (`fakes_allowed`). They stand in for an unavailable external environment (other machines, Cloudflare, Paddle, Google Play, FCM, AI-client internals), never for the behaviour under test.

## 4. Publication, merge and deployment

- **Coordinator only.** The coordinator pushes branches, opens PRs, posts review records and merges. Merges happen at the reviewed head after hosted CI passes. Auto-merge is never enabled unless the user asks.
- **Reading CI.** The coordinator reads CI through the app's PR tools and never polls CI in loops.
- **Production changes** happen only through main-push deploys of the repositories' guarded scripts.
  - Cloudflare only through repository scripts; `workers.dev` and previews stay off.
  - Outward-facing changes (public site content, store listings, package-manager or plugin publication) need the user's explicit approval before merge or publish.
- **Published versions** are never unpublished, deprecated or deleted.
  - Never pin or admit Contracts `1.0.0-ci.350.1` or DesktopPlatform Build.Policy `1.0.0-ci.124.1`.
  - Never admit a first-party version whose publishing commit is not an ancestor of its producer's main.
- **Dependabot PRs** are never touched: no merge, close, comment or rebase.

## 5. Safety and environment

- **Secrets.** Never read or print secrets.
- **Network and settings.** No proxy or network changes. The coordinator never changes repository security settings (H-12).
- **Failures.**
  - Diagnose before any rerun.
  - Retry ordinary transient failures with bounded backoff.
  - Inspect remote state before retrying any write.
- **Platforms.** WSL2 Debian is the Linux test environment; installs inside it are the user's (H-11). There is no SSH, and macOS is out of scope.
- **CI scope.** No device, GUI, browser, live-service or inference CI. Those runs are local opt-in, or deferred to the acceptance register.

## 6. Dogfooding

After AF-EXEC-01 (and fully after AF-SCHED-01), delivery sessions should run heavy local commands through ArcForges (`arcforges run …`) and record that in evidence. This is evidence, not a precondition.
