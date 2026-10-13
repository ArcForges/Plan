# Execution policy (serial)

Authority: ArcForges-Design [AD-0014](https://github.com/ArcForges/ArcForges-Design/blob/main/docs/decisions/AD-0014-delivery-method.md). This policy replaces every earlier Plan-Parallel policy (`execution-policy.md`, `single-task-command.md`, `arcforges-implementation.md`, the build slot and claims and leases), which are history only.

## 1. One task at a time

1. Exactly one task in [delivery-graph.json](delivery-graph.json) may be `active`. `python tools/plan.py next` names it, or names the first eligible task overall. `next` does not know the authorized range: within a range, the next task is the one §1.2 defines.
2. The next task to start is the first `planned` task **of the authorized range** (§1.5) in serial order whose dependencies are `delivered`, `complete` or `superseded`. The order in the graph is the order of work. Do not reorder, skip or start tasks early. A task whose dependency lies outside the range and is not delivered is not eligible; the coordinator reports it and never implements the dependency.
   - `depends_on` lists only **real** dependencies (a task needs the other's delivered code, contracts or services). The serial order is the file order, not a dependency chain, so one blocked task holds back only the tasks that really need it.
3. **Delegation.**
   - A coordinator session may delegate to **one** worker or reviewer at a time, using **Opus 5.5** only, confirmed by the model ID the delegate reports first. Never Haiku. Without a confirmed Opus 5.5 reviewer, a task is not merged, and the coordinator stops and reports it.
   - No parallel research, implementation or review workstreams.
   - A delegate works only in its task's worktree and never pushes, posts, merges or deploys. The coordinator does those (§4).
4. **No build slot.** There is no workstation lock and no "retry for a slot". Long checks run once, in the background when practical, and their results are read rather than polled in loops.
5. **Run gate, then continuous execution** ([AD-0014](https://github.com/ArcForges/ArcForges-Design/blob/main/docs/decisions/AD-0014-delivery-method.md) §10).
   - No implementation starts until the user authorizes it. The user authorizes work by giving a session the execution prompt ([execution-prompt.md](execution-prompt.md); the user's copy is `C:\MyFile\Projects\ArcForges\ArcForges.md`) with a pasted range of [sequence.md](sequence.md) steps. That range is the authorized scope: only its tasks are delivered, in sequence order, and work ends at its last task.
   - The range's scope is the Task column of the pasted rows; IDs in *Depends on* are prerequisites, never scope. The coordinator records the authorization as a ledger note that lists every task ID in scope (`python tools/plan.py ledger PLAN note "Implementation authorized by the user on <date>: <ID>, <ID>, … (<count> tasks; sequence rows <first #>–<last #>)"`), merged with the first task's start record. A resumed session continues within the ID list of the latest authorization note. A session with neither a pasted range nor an unfinished authorized range only reports status (entry prompt P-5).
   - Within the range, the coordinator delivers eligible tasks one after another. Serial means one task at a time, not one task per session: it reports each delivery and continues with the next eligible task in the range without asking to continue. Tasks outside the range are never started, even when `plan.py next` names one.
   - A `blocked` task is skipped, not a reason to stop.
   - It stops only when an outward-facing approval is needed, the authorized scope is complete, no eligible task remains, a task outside the range is active, no confirmed Opus 5.5 reviewer is available, a decision only the user can make is required, or the user says stop. It then reports where it stopped and why.
6. **Repairs versus new scope.** A defect in delivered code, in any repository, that prevents the current task's acceptance is repaired within that task: in its PR with a scope note when it is small and inside the task's write paths, otherwise in a separate repair PR in the owning repository, reviewed like a task and recorded in the task's evidence. A repair restores specified behaviour and adds none. Small changes outside the write paths that the task's own specified scope needs (for example solution entries, wiring, or view models for its pages) go into its PR with a scope note. A larger one first widens the task record through a reviewed Plan PR. Only behaviour that no task specifies becomes a new task proposal, which the coordinator records and reports without building it.

## 2. Task states

| State | Meaning | Set by |
|---|---|---|
| `planned` | Not started, or returned after an unresolved failure; then its work stays on its branch, and the ledger note says where | — |
| `active` | Being implemented | Coordinator, when work starts (`plan.py set-state <id> active` plus a ledger `started` record) |
| `delivered` | Merged at the reviewed head, published or deployed where applicable, and its own development-stage acceptance met | Coordinator, after merge and publication checks (`--merge REPO@SHA`) |
| `complete` | Delivered, and every completion prerequisite holds, including the real-environment evidence possible now. Deferred real-world validation is recorded in the acceptance register. | Coordinator |
| `blocked` | Waiting on a human prerequisite or an acceptance-register entry (`blocked_by`), for example legal texts, production keys, or the user's approval to publish. Work done so far stays on its branch. A blocked task does not count against the single active task. | Coordinator (`plan.py set-state <id> blocked --blocked-by H-xx --reason …` plus a ledger record) |
| `superseded` | Replaced by a design decision (with reason) | Coordinator, with a ledger record |

- **Blocked tasks.** A task is set `blocked` only when a prerequisite whose **Blocks** column in the [acceptance register](acceptance-register.md) names that task is missing. Production prerequisites name only AF-PROD-01: Cloud and Web tasks deploy dark (§4). Prerequisites that block only `complete` leave the task `delivered`; the rest never block. `next` then continues with the first planned task that does not depend on it. When the prerequisite arrives, the task returns to `active` (or `planned`) and finishes.
- **Deferred validation is not a block.** A task whose remaining step is a deferred real-world validation completes its development-stage scope, records the procedure in [acceptance-register.md](acceptance-register.md) and becomes `delivered` or `complete`.

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
  - **Dark deploys.** Cloud and Web merges deploy with the flagship surfaces disabled (Design 10 §8). Implementation delivery never waits for production key material, domains, provisioning or publication approval.
  - **Production activation** is task AF-PROD-01: it needs the user's approval and the production prerequisites, and enables the surfaces one at a time.
  - Outward-facing changes need the user's explicit approval before they become visible: publication of the public site and web profiles (AF-PROD-01), store listings, and publication to package managers and plugin marketplaces (winget, Scoop, apt repositories, plugin marketplaces; AR-13). First-party package cohorts published through a repository's main-push publishing are ordinary delivery.
- **Published versions** are never unpublished, deprecated or deleted.
  - Never pin or admit Contracts `1.0.0-ci.350.1` or DesktopPlatform Build.Policy `1.0.0-ci.124.1`.
  - Never admit a first-party version whose publishing commit is not an ancestor of its producer's main.
- **Dependabot PRs** are never touched: no merge, close, comment or rebase.
- **Plan record PRs.** A Plan PR that changes only task states, evidence and ledger lines (as written by `plan.py`) needs no independent review: the coordinator checks the diff, waits for Plan CI and merges. Any other Plan change (graph content, policy, tools) is reviewed like a task.
- **Merge order between Design and Plan.** Plan CI validates the graph against ArcForges-Design `main` and runs the design's traceability cross-check (`check_design.py --plan`). A change that touches both merges the **Design PR first**, then re-runs Plan CI and merges the Plan PR.

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
