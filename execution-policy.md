# Execution policy (serial)

Authority: ArcForges-Design [AD-0014](https://github.com/ArcForges/ArcForges-Design/blob/main/docs/decisions/AD-0014-delivery-method.md) and [AD-0016](https://github.com/ArcForges/ArcForges-Design/blob/main/docs/decisions/AD-0016-local-first-verification.md) (local-first verification). This policy replaces every earlier Plan-Parallel policy (`execution-policy.md`, `single-task-command.md`, `arcforges-implementation.md`, the build slot and claims and leases), which are history only.

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
| Author | Targeted and affected tests, affected real Windows and Linux tests, build and AOT publish of affected components, format and analyzers. May run `python eng/verify.py run` on a host before handing over (a local check; it reports nothing). Records exact commands and results in the PR. | Skips tests it changed or that cover changed code |
| Independent reviewer (one session, after the author) | Reads the complete diff at the exact head against the task's design references and acceptance criteria. Re-runs only what gives distinct evidence: a doubted test, a check whose script or workflow the PR changed, or a real-environment test the author could not run. | Repeats the author's identical full suite on the same unchanged head |
| Host verification after the push ([AD-0020](https://github.com/ArcForges/ArcForges-Design/blob/main/docs/decisions/AD-0020-post-push-verification-and-required-checks.md)) | The repository's CI-equivalent profile at the pushed head, one leg on each host (`python eng/verify.py run-and-report`: the native Windows leg and the native Linux leg, §5), reported as the commit statuses `arcforges/windows` and `arcforges/linux` that the `main` rulesets require for every PR | Bypassed, weakened or skipped; a step that could not run is never reported as passed; a status is never posted by hand |
| Hosted CI, external PRs | The repository's full CI for every other author, Dependabot included: the merge gate for platform-independent checks | GUI, device, browser-E2E, live-service or inference jobs |
| Coordinator | Push, PR, running `run-and-report` on each host for the head, review record, reading the required statuses and, for external PRs, CI, merge at the reviewed head, publication or deployment check, graph state and ledger | Duplicates any of the above |

- **Host verification after the coordinator's push** ([AD-0020](https://github.com/ArcForges/ArcForges-Design/blob/main/docs/decisions/AD-0020-post-push-verification-and-required-checks.md)). After pushing a head, the coordinator runs `python eng/verify.py run-and-report` on each host the repository's step table uses, through its MCP server, in a worktree at that commit fetched from GitHub (`AGENTS.md` rule 6). If a leg fails, the coordinator returns the failure (step, last log lines, log path) to the worker, or fixes a coordinator-side cause such as a stale fetch, pushes again and verifies the new head. It never posts a status by hand, never changes a ruleset or required check to get a PR merged, and never disables or edits the verification scripts to get a change through. *Before 2026-10-22 this was the pre-push hook at the coordinator's push.*
- **Task records.** A task's `verification.hosted_ci` names the CI-equivalent checks of each touched repository. For the owner's PRs they are met by that repository's host verification (the required statuses); for external PRs by its hosted CI as well.
- **Re-review** after fixes covers only the delta, unless the delta changes build or test infrastructure.
- **Fakes** are allowed only where a task lists them (`fakes_allowed`). They stand in for an unavailable external environment (other machines, Cloudflare, Paddle, Google Play, FCM, AI-client internals), never for the behaviour under test.

## 4. Publication, merge and deployment

- **Coordinator only.** The coordinator pushes branches, opens PRs, posts review records and merges. Auto-merge is never enabled unless the user asks.
- **Merge gate** ([AD-0016](https://github.com/ArcForges/ArcForges-Design/blob/main/docs/decisions/AD-0016-local-first-verification.md) as amended by [AD-0020](https://github.com/ArcForges/ArcForges-Design/blob/main/docs/decisions/AD-0020-post-push-verification-and-required-checks.md)). Merges happen at the reviewed head when:
  - **every PR:** the commit statuses its repository's `main` ruleset requires (`arcforges/windows`, `arcforges/linux`) report success for that head, which GitHub enforces with no bypass, and the independent review approved;
  - **owner PRs** (author `deku2026`): GitHub shows the hosted validation jobs as skipped;
  - **external PRs** (any other author, Dependabot included): full hosted CI also passed at that head. A maintainer reads the diff before any host verifies it.
- **Reading CI.** The coordinator reads the required statuses and, for external PRs, CI through the app's PR tools, and never polls them in loops.
- **After a merge.** A main push runs only delivery: publication and deployment workflows, including gates that a publication embeds in its evidence (AD-0016 §2). It runs no separate validation, and the next task does not wait for a main CI run.
- **Production changes** happen only through main-push deploys of the repositories' guarded scripts.
  - Cloudflare only through repository scripts; `workers.dev` and previews stay off.
  - **Dark deploys.** Cloud and Web merges deploy with the flagship surfaces disabled (Design 10 §8). Implementation delivery never waits for production key material, domains, provisioning or publication approval.
  - **Production activation** is task AF-PROD-01: it needs the user's approval and the production prerequisites, and enables the surfaces one at a time.
  - Outward-facing changes need the user's explicit approval before they become visible: publication of the public site and web profiles (AF-PROD-01), store listings, and publication to package managers and plugin marketplaces (winget, Scoop, apt repositories, plugin marketplaces; AR-13). First-party package cohorts published through a repository's main-push publishing are ordinary delivery.
- **Published versions** are never unpublished, deprecated or deleted.
  - Never pin or admit Contracts `1.0.0-ci.350.1` or DesktopPlatform Build.Policy `1.0.0-ci.124.1`.
  - Never admit a first-party version whose publishing commit is not an ancestor of its producer's main.
- **Dependabot PRs** are never touched: no merge, close, comment or rebase.
- **Plan record PRs.** A Plan PR that changes only task states, evidence and ledger lines (as written by `plan.py`) needs no independent review: the coordinator checks the diff, pushes it, verifies the head on both hosts (the required statuses) and merges. Any other Plan change (graph content, policy, tools) is reviewed like a task.
- **Merge order between Design and Plan.** The Plan's verification (the host verification for every PR, Plan CI also for external PRs) validates the graph against ArcForges-Design `main` and runs the design's traceability cross-check (`check_design.py --plan`). A change that touches both merges the **Design PR first**, then verifies the Plan PR's head again on both hosts against the new Design main (`python eng/verify.py run-and-report`, which replaces the earlier statuses of that commit) and merges it. A status does not record which Design main it checked, so the coordinator re-verifies the Plan head after every Design merge that its PR depends on. If the Plan head needs the unmerged Design change, its legs fail until the Design PR merges.

## 5. Safety and environment

- **Secrets.** Never read or print secrets.
- **Network and settings.** No proxy or network changes. The coordinator never changes repository security settings (H-12), with two exceptions: the required status checks of the conditional CI (AD-0016 §2), which it may change only as the user authorized on 2026-10-16: "If existing required checks must be adjusted to support this conditional workflow, make the smallest appropriate changes."; and the `main` rulesets that require the host statuses (AD-0020 §6), which the user authorized on 2026-10-22 for that migration. Neither is ever changed to get a PR merged.
- **Failures.**
  - Diagnose before any rerun.
  - Retry ordinary transient failures with bounded backoff.
  - Inspect remote state before retrying any write.
- **Platforms.** Verification is MCP-first and runs on native machines, never through WSL ([AD-0018](https://github.com/ArcForges/ArcForges-Design/blob/main/docs/decisions/AD-0018-native-platforms-without-wsl-integration.md) §5 as amended by [AD-0019](https://github.com/ArcForges/ArcForges-Design/blob/main/docs/decisions/AD-0019-mcp-first-verification.md)): the Windows leg on the owner's Windows workstation through the Windows MCP server, the Linux leg on the Linux MCP host through the Linux MCP server (H-22). Both are standard MCP servers that Claude Code and Codex share. Each host fetches the pushed commit from GitHub and reports its leg as a commit status (AD-0020). Local WSL is never used, not even as a fallback, and need not be installed. If an MCP server is unavailable, verification stops and the status stays missing, so the PR cannot merge; nothing is skipped or bypassed (AD-0019 §5). Installs on those hosts are the user's (H-11). There is no SSH, and macOS is out of scope.
- **CI scope.** No device, GUI, browser, live-service or inference CI. Those runs are local opt-in, or deferred to the acceptance register.

## 6. Dogfooding

After AF-EXEC-01 (and fully after AF-SCHED-01), delivery sessions should run heavy local commands through ArcForges (`arcforges run …`) and record that in evidence. This is evidence, not a precondition.
