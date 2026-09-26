# ArcForges implementation

## Execution state

There is no single Current task. Implementation is a set of delivery tasks with typed prerequisites, and any number of workers execute different ready tasks at the same time. The authoritative rules are the Design [delivery model](https://github.com/ArcForges/ArcForges-Design-B/blob/main/docs/planning/delivery/README.md) (decision P2-018); this document is the operating procedure, and [single-task-command.md](single-task-command.md) holds the entry prompts that start a worker, a coordinator, an integration owner or a resumption.

- **Historical baseline:** when this procedure was introduced, implementation was complete through WP03.02. WP00, WP01, WP02 and WP03.00–03.02 are accepted (tasks `GOV.01`–`GOV.03`, `CON.90`–`CON.92`) and are to be recorded as inherited by adoption. WP03.03 had not started; its closures are the tasks `CON.02` and `CON.03`.
- **Progress:** determine it only from the authoritative state below, never from this document. When this procedure was written the adoption stage had not run and the only ready task was `ADOPT.01` (freeze the adoption baseline). It opens 58 adoption slices, one per repository and lane (`ADOPT.NN.<lane>`); each recorded slice opens the tasks of its own lane in its own repository, independently of every other slice. The repository records `ADOPT.02`–`ADOPT.10` close after their slices; `ADOPT.11` reconciles Design and Plan.
- **Find work:** `python tools/delivery.py ready`. The [task list](list.md) indexes every task and adoption slice; each lane file under [`tasks/`](tasks/) holds one self-contained prompt per task and slice.

## Project background

ArcForges is a family of commercially operable applications and shared services. ArcNotes provides knowledge management, ArcScope instrument acquisition and analysis, and ArcSlate media production. These are independent Avalonia/C# desktop applications. Each owns its application state, conversations, storage and server session, and embeds reusable assistant UI and mechanisms published by DesktopPlatform. ArcChat is the assistant/companion feature name, not a fourth desktop executable or a shared application hub.

Nine independent repositories integrate immutable published artifacts. DesktopPlatform provides shared managed mechanisms, Avalonia UI packages, native C ABI wrappers and RID runtimes; product domain behavior remains with its product owner. Contracts owns authored proto and generates C# NuGet, TypeScript npm and Kotlin Maven packages. Public business clients use binary gRPC-Web, with the explicit authentication, object-transfer and provider protocol exceptions defined by Design.

The C# Native AOT business host runs in Cloudflare Containers behind Workers. D1 owns authoritative business data, Durable Objects coordinate, and R2 stores objects. The sole AI Harness runs in Cloudflare Workflows with Workers AI. Mobile uses Kotlin/Jetpack Compose for Android; Web uses React/TypeScript for Site, Account, Chat and Operations. Applications have independent sessions without sibling Device SSO. Private parent-owned helpers/extensions alone use the specified gRPC over Named Pipes/UDS. Cross-product collaboration is future-only.

The goal is the complete accepted commercial product: usable client workflows, correct contracts and transactions, permissions, failure recovery, real integration, distribution, support and commercial operation. Existing Hello World scaffolds and published probes are migration inputs; they do not prove completed product behavior.

## Authoritative material and source locations

Formal Design: `C:\MyFile\Projects\ArcForges-Design-B`. Read its repository instructions and current decisions. The planning entry points are `docs/planning/delivery/README.md` (delivery model), the task records in `docs/planning/delivery/lanes/`, `docs/planning/README.md`, `docs/planning/implementation-sequence.md` (principles and mock policy) and `docs/planning/producer-artifacts-and-integration.md`. Work packages in `docs/planning/work-packages/` are the obligation catalogue: a task's obligations link to the substeps whose "what must be fully done", testing requirements and completion gates it must satisfy. Concrete behavior is defined across `docs/requirements`, `docs/architecture` (including `contracts` and `data-model`), `docs/experience` and `docs/assurance`. Current accepted amendments govern older text; filenames and historical inventories do not override them. Deprecated-input bodies are excluded from implementation reading.

Implementation repositories are under `C:\MyFile\Projects\ArcForges`: DesktopPlatform, Contracts, ArcNotes, ArcScope, ArcSlate, Cloud, AI, Web and Mobile. Each is a separate Git repository; a task names its one owning repository and any other repository it touches.

Read-only reference sources are `C:\MyFile\Projects\AionUi`, `AFFiNE`, `siyuan`, `Serial-Studio`, `ArcVideo` and `ArcVideoFoundation`. Start with their completed matrices under Design's `docs/assurance/reference-coverage` and inspect the relevant source or drift only. Respect per-file licences, provenance and excluded subtrees; a rewrite does not erase upstream obligations. `C:\MyFile\Projects\StartArcForges` is a packaged-artifact layout/notice reference only: do not execute, unpack or reverse engineer its binaries. Reference features do not create additional product requirements.

The retired serial task list remains in Git history (`list.md` at commit `0fa610d`) as traceability only; it is not an execution entry.

## Authoritative state and the delivery tool

Run the tool by its absolute path from any directory, in Git Bash or PowerShell: `python C:\MyFile\Projects\Plan-B\tools\delivery.py <command>` (keep the Plan primary checkout fast-forwarded so the tool itself is current). The current directory never selects the Plan or Design checkout the tool reads. Execution commands read no working tree, only the **authoritative state**: the merged `main` of Design and Plan and the Plan record branches, fetched on every call into a private ref namespace, so concurrent workers never move a ref another worker has read. Unmerged commits and uncommitted edits in any checkout, including your own, never count; `ready --local --plan <Plan worktree> --design <Design worktree>` shows such an unreviewed state of the named working trees for review and is never a basis for claiming.

The tool fails closed. An invalid graph or ledger authorizes no work. An invalid claim, lease or role record keeps its item unavailable until a reviewed fix repairs it. A claim that changed concurrently writes nothing (exit 2). A failed network operation stops with the exact operation (exit 3): report it and stop.

| Command | Purpose |
|---|---|
| `ready [--lane L] [--repo R] [--json]` | Tasks and slices that may be claimed now, with resume or recovery notes, and completion follow-ups |
| `status [--worker W] [--repo R] [--json]` | Every claim, lease and role with holder, lease and handoff; delivered tasks still waiting; vacant integration roles; the local build slot |
| `show <ID> [--json]` | One record with its history, and the task's ledger and start-rule state |
| `claim <ID> --worker W` | Claim a ready task or slice, a completion follow-up, a lease (`RES-...` with `--task`) or a role (`integration:<Repository>`) |
| `update <ID> --worker W --epoch N ...` | Renew and record handoff checkpoints; set `blocked`, `delivered` or `complete` |
| `release <ID> --worker W --epoch N --note ...` | Voluntary handoff, or the end of a lease or role |
| `build-slot run --worker W --task T -- <command>` | Run one CPU-heavy local build or test under the workstation lock |
| `check --plan P --design D`, `generate --plan P --design D` | Validate, or regenerate, the graph, views and ledger of the named Plan and Design working trees for planning and ledger pull requests; always name both ([Planning and ledger changes](#planning-and-ledger-changes)) |

**Keys.** Every ID has one key, in lower case with dots replaced by hyphens (`CON.02` → `con-02`, `ADOPT.03.contracts` → `adopt-03-contracts`). It names the claim `claims/<key>`, the task branch `task/<key>` and the ledger record `ledger/tasks/<key>.md`. Never use the dotted ID in a branch or file name: Git for Windows cannot store names such as `con.02`.

## Planning and ledger changes

`check` and `generate` read and write only the working trees named by `--plan` and `--design`. Their defaults ignore the current directory: `--plan` defaults to the checkout holding the copy of the tool that runs, so `C:\MyFile\Projects\Plan-B\tools\delivery.py` uses the Plan primary checkout, and `--design` defaults to `ArcForges-Design-B` beside the Plan primary checkout (or `ARCFORGES_DESIGN` when set). Run that way from a worktree, `check` validates the primary checkouts and can pass while your worktree holds a stale view. Always name both roots:

- **Planning change:** edit the Design graph in a retained Design worktree, then run `python C:\MyFile\Projects\Plan-B\tools\delivery.py generate --plan <Plan worktree> --design <Design worktree>` and `check` with the same roots. `generate` rewrites every view in both trees.
- **Ledger-only change:** `python C:\MyFile\Projects\Plan-B\tools\delivery.py check --plan <Plan worktree> --design C:\MyFile\Projects\ArcForges-Design-B`, with the Design primary checkout fast-forwarded to current `main`; `check` only reads it.
- **Change to `tools/delivery.py`:** run the worktree's own copy, `python <Plan worktree>\tools\delivery.py`, with the same explicit roots.

Never run `generate` against a primary checkout, and never edit a primary checkout.

## Sessions and roles

Every session chooses a **worker name** unique to that session (for example `w-<host>-<yyyymmdd>-<n>`) and uses it for every claim, lease, role and review it makes. Coordination state lives only in claim, lease and role records, pull requests and the ledger ([DLV-40](https://github.com/ArcForges/ArcForges-Design-B/blob/main/docs/planning/delivery/README.md#rule-dlv-40), [DLV-42](https://github.com/ArcForges/ArcForges-Design-B/blob/main/docs/planning/delivery/README.md#rule-dlv-42)); never keep it only in a conversation.

- **Worker.** Implements one claimed task or bundle at a time. While that task waits on review, CI or a merge queue it may review another pull request, take a vacant integration role, claim a completion follow-up or claim another ready task, keeping every claim it holds renewed with a current handoff record. It resumes its own claims first (`status --worker W`) and then takes new work until the user's instruction ends.
- **Reviewer.** A session other than the task's claimant when one is available; a worker operating alone reviews its own complete diff and says so. The review comment on the pull request names the exact head commit it approved.
- **Integration owner.** One session per repository holds `roles/integration-<repository>` (`claim integration:<Repository> --worker W`). It merges approved pull requests of that repository, applies the shared-resource protocols, confirms publication and keeps `main` green. Any worker may assume a vacant role to merge approved pull requests and release it with a note when done; a busy repository may keep a dedicated owner that renews the role while it works. `status` shows every holder and every vacant role.
- **Coordinator** (optional). Maintains capacity: starts workers up to the requested number (separate sessions, or subagents when the user asks for them), replaces workers that stop, directs idle workers to completion follow-ups, reviews and vacant integration roles, and reports. It holds no state of its own, so any session replaces it by running `status`.

**Selecting work.** Take, in this order: your own live claims and pull requests; completion follow-ups; released tasks that carry a handoff (continue them, never restart them); ready tasks on the [critical path](https://github.com/ArcForges/ArcForges-Design-B/blob/main/docs/planning/delivery/schedule-analysis.md) or that unblock the most work; review requests and vacant integration roles with approved pull requests. Stay within the scope the user gave (tasks, lanes or repositories). If nothing is available, report what the ready set waits on (`show <ID>` names the unsatisfied prerequisites) and stop rather than invent work.

## Claiming

1. Run `ready`, choose, then `python tools/delivery.py claim <TASK-ID> --worker W`. The tool re-reads the exact claim commit, verifies the start rule (or the follow-up rule) from the authoritative state, writes the next record as a compare-and-swap on that commit and verifies the result; if anyone moved the claim meanwhile, nothing is written.
   - No claim yet: epoch 1.
   - Released: the next epoch, keeping the earlier handoff. Continue its branch and pull request.
   - Delivered, with every completion prerequisite complete: a completion follow-up at the next epoch (see [Completing a task](#completing-a-task)).
   - Held with a live lease, complete, or invalid: not available.
   - Lease expired more than one hour ago: recovery only, under [Interruption, handoff and recovery](#interruption-handoff-and-recovery), with `--takeover --reason "<the checks you made>"`.
2. Note the epoch the tool prints. Every later `update` and `release` names it, and the tool refuses any change unless the record's tip names you at that epoch.
3. Before the first edit, look for an existing `task/<key>` branch and open pull requests titled with the task ID, even if the record lists none, and continue them.

## Durable handoff

The claim record carries the handoff ([DLV-40](https://github.com/ArcForges/ArcForges-Design-B/blob/main/docs/planning/delivery/README.md#rule-dlv-40)): repository, task branch, worktree path (host-specific, informational), pull requests, last pushed head, reviewed commit, merge commits, `done` and `next` actions, validation performed, blocker and note. Record it with `update`, which also renews the lease (24 hours by default), at every checkpoint:

| Checkpoint | Record with `update <ID> --worker W --epoch N` |
|---|---|
| First commit pushed to `task/<key>` (push early; work-in-progress commits are fine) | `--head <SHA> --worktree <path> --done ... --next ...` |
| Pull request opened or updated for review | `--pr <URL> --head <SHA> --next "await review"` |
| Review approved | `--reviewed <SHA>` |
| Merged | `--merge <merge SHA> --next "confirm publication" --next "record the ledger"` |
| Publication receipt and ledger pull request | `--pr <ledger PR URL> --validation ...` |
| Blocked, or unblocked | `--state blocked --blocker "<concrete missing input>"`, or `--state claimed` (clears the blocker) |
| Before stopping, pausing or running out of context | push the branch, then `--done ... --next ...`, or `release` |

Renew at least once a day while you hold a claim. Push before recording: an unpushed local worktree is lost to every other worker.

## Executing a task

- Take the task's self-contained prompt from its lane file under `tasks/`. Read the task record, every obligation it links, the prerequisite tasks' published outputs and the applicable repository instructions. Verify relevant facts, finish research and decisions, then establish one complete ordered plan before editing. Repair conflicting authoritative documentation through a Design pull request before dependent implementation.
- Work in a retained Git worktree of the owning repository (for example `<repository>\.worktree\<key>`) on branch `task/<key>`. Title pull requests `[<TASK-ID>] <summary>` and put in the body the link to the task record and one claim line per task: `Claim: <TASK-ID> epoch <N> (<worker>)`. Append to the task's open pull request rather than creating a parallel one. Several ready tasks with compatible scopes may share one pull request titled `[<TASK-ID>, <TASK-ID>] <summary>`; each keeps its own claim, handoff record, ledger record and evidence, and a bundle never waits for a task that is not ready (DLV-38).
- Before implementing a non-adoption task, read its merged adoption-slice classification and any later adoption adjustments. Reuse inherited evidence; for inherited-with-adjustment work, implement the recorded remaining scope. An unresolved conflict or blocker stops only the affected task: record it in the claim and follow D-001 for a design conflict. Dependency readiness does not clear these findings or authorize bypassing them.
- Before the first edit, bind the task's planned write scope to the repository's actual project and namespace layout; never rename existing packages or installation identities to match a planned path (ADP-07). Stay inside the task's write scope. Touch a declared shared resource only through its owner protocol (generated baselines are regenerated after rebase, migrations are numbered at merge, registries are appended). An undeclared conflict discovered at merge is resolved by the repository integration owner and recorded as a planning change if it will recur.
- Consume producers only through published candidates: update the exact pin you need through a reviewed dependency change. Use only the substitutes the task lists; never register a substitute in a release composition.
- Preserve product behavior, package IDs, signing continuity, immutable releases and unrelated work. Claiming a task never changes runtime authority: one canonical writer per store, module-owned Cloud tables and guarded cross-owner transactions stay as designed (DLV-39). A genuine architecture conflict stops the task and is raised (D-001); the claim records the blocked state.
- If a delivered producer you pinned changes incompatibly, revalidate only the changed scope and move your pin through a reviewed change; your inputs are never rewritten while you work (DLV-36).
- Run every CPU-heavy local build or test through the workstation build slot ([Leases, roles and the workstation build slot](#leases-roles-and-the-workstation-build-slot)).

## Review, merge and fencing

1. The claimant requests review with a pull request comment and records `--next "await review"`.
2. The reviewer reviews the complete diff at one head commit and comments `Reviewed <full SHA> for [<TASK-ID>] epoch <N>: approved`, or lists findings. The claimant fixes findings and requests review of the new head, and records the approved commit with `--reviewed <SHA>`.
3. The integration owner (the holder of `roles/integration-<repository>`; claim `integration:<Repository>` if it is vacant) confirms before merging:
   - `show <TASK-ID>`: state `claimed`, the claimant and epoch of the pull request's claim line, and `reviewed` equal to the pull request's head commit;
   - every retained applicable check on that head is green (repositories without CI merge after review);
   - the shared-resource protocols are applied (rebase and regenerate baselines, allocate migration numbers, append registries).
4. Merge only at the reviewed head, with a title that keeps the task IDs: `gh pr merge <N> --merge --match-head-commit <reviewed SHA> --subject "[<TASK-ID>] <summary> (#<N>)"` (a squash-merging repository uses `--squash` with the same subject). A head that moved after the review is reviewed again, never merged; commits pushed by an earlier epoch are reviewed by the current claimant first.
5. The claimant records `--merge <merge SHA>`. The integration owner confirms the required post-merge job results and publication receipt, then releases the role with a note describing the queue, or keeps it while it keeps merging.

## Completing a task

1. Confirm the producer candidate's publication receipt where the task publishes one.
2. Open a Plan pull request titled `[<TASK-ID>] Record <summary>` that adds `ledger/tasks/<key>.md` in the [ledger format](ledger/README.md): `delivered` while a completion prerequisite is open, otherwise `complete`. Several records may share one pull request, each with its own file. Review it, run `python C:\MyFile\Projects\Plan-B\tools\delivery.py check --plan <Plan worktree> --design C:\MyFile\Projects\ArcForges-Design-B` with the Design primary checkout at current `main` ([Planning and ledger changes](#planning-and-ledger-changes)), and merge it through the Plan integration role (Plan has no CI).
3. After the ledger pull request merges, record `update <ID> --worker W --epoch N --state delivered` or `--state complete`; the tool refuses until the merged ledger says so. A delivered task has no owner while it waits, so take other work.
4. **Completion follow-up** ([DLV-41](https://github.com/ArcForges/ArcForges-Design-B/blob/main/docs/planning/delivery/README.md#rule-dlv-41)): when `ready` lists a delivered task under completion follow-ups, any worker claims it (the next epoch), performs the task's own remaining acceptance for the scenarios its completion prerequisites name, amends the existing ledger record in place (`status: complete`, new evidence appended) through a reviewed pull request, and records `--state complete`. Upstream completion alone is not the task's acceptance.
5. Package and gate acceptance records go to Design `docs/assurance` when a package closure or gate task completes.

## Interruption, handoff and recovery

- **Your own interruption:** run `status --worker W` and continue each live claim, lease and role from its record, branch and pull request.
- **Voluntary handoff:** push the branch, then `release <ID> --worker W --epoch N --note "handoff: <why>" --next ...`. Another worker re-claims at once (the next epoch), reviews the earlier commits and continues the same branch and pull request. Push nothing more after releasing.
- **Recovery of an expired claim** (its worker or coordinator disappeared): `ready` and `status` show it. Take over only when the lease expired more than one hour ago, the branch and pull request show no activity since then, and a release request comment on the pull request, where one exists, has gone unanswered for at least one hour. Then `claim <ID> --worker W --takeover --reason "<those checks>"`, review the earlier commits, and continue the same branch and pull request. Leases and roles are recovered the same way, without the pull request checks.
- **Merged but not yet recorded:** the record shows the merge commits and next actions (publication confirmation, ledger); the successor continues from there and never re-implements.
- **Interrupted before any push:** only the record's notes survive; the successor redoes the unpushed part from them.
- **Blocked:** record the concrete missing input. A missing prerequisite or design gap becomes a planning change (edit the Design graph, run `generate` and `check` with both roots named as in [Planning and ledger changes](#planning-and-ledger-changes), merge the Design and Plan pull requests); an architecture conflict is raised under D-001. If you stop while blocked, release the claim with the blocker kept in the record so the next worker sees it.
- **Superseded:** if a planning change supersedes a claimed task, release it naming the superseding task; the ledger records it as superseded.

## Leases, roles and the workstation build slot

- **Exclusive phases** ([DLV-11](https://github.com/ArcForges/ArcForges-Design-B/blob/main/docs/planning/delivery/README.md#rule-dlv-11), [DLV-37](https://github.com/ArcForges/ArcForges-Design-B/blob/main/docs/planning/delivery/README.md#rule-dlv-37)): a resource protocol that names an exclusive phase binds every task entering it. Today these are live runs against the deployed Cloud test environment (`RES-cloud-deployment`) or the AI deployment environment (`RES-ai-workflow-and-routes`), and the Android module-skeleton restructuring (`RES-mobile-build-config`). Take the lease only for that phase with `claim <RES-ID> --worker W --task <TASK-ID>` (you must hold the task's claim) and release it with `release <RES-ID> --worker W --epoch N --note ...` as soon as the phase ends, before waiting on review, CI or a producer. Acquire several leases in ascending resource-ID order and release all of them if one cannot be acquired. `append`, `regenerate` and `read` modes need no lease: follow the [shared-resource protocols](https://github.com/ArcForges/ArcForges-Design-B/blob/main/docs/planning/delivery/shared-resources.md).
- **Integration roles** are claimed, renewed and released the same way (see [Review, merge and fencing](#review-merge-and-fencing)).
- **Workstation build slot** ([DLV-31](https://github.com/ArcForges/ArcForges-Design-B/blob/main/docs/planning/delivery/README.md#rule-dlv-31)): run every CPU-heavy local build or test as `python C:\MyFile\Projects\Plan-B\tools\delivery.py build-slot run --worker W --task <TASK-ID> -- <command>`. A batch file in the current directory may be named directly (for example `-- gradlew.bat build`): the tool runs it through `cmd /c` by its full path, because this workstation does not search the current directory for commands (`NoDefaultCurrentDirectoryInExePath`). Run a shell script through `-- bash -lc "<script>"`. The tool holds the lock directory `%USERPROFILE%\.arcforges\build-slot` with an owner record and a heartbeat, waits while another build runs (keep coding or reviewing meanwhile), recovers a lock whose holder stopped, and releases it when the command ends. `build-slot status` shows the holder.

## Execution and validation policy

This policy governs every task and the adoption stage. It follows Design P2-017 and the CI/local validation policy, as amended in coordination wording by P2-018.

- No macOS CI job, runner or matrix, including self-hosted, scheduled and manual workflows. Local macOS source support may remain; never claim an unproduced macOS artifact or unobserved platform result.
- No hosted physical-device/emulator, desktop GUI, browser E2E, live service/RPC, real inference/Workflow, installed-package consumer or public-release install/upgrade tests. Remove hidden default check/build/publish invocations and obsolete artifact/status dependencies.
- Retain necessary Windows/Linux compilation, Native AOT compilation, packaging, static/format/type/lint checks, targeted offline unit tests and non-duplicated security. Do not multiply identical checks across platforms without a platform-specific requirement.
- Runtime/E2E checks are explicit local opt-in only for affected behavior supported by the existing environment. Run once; repeat only for a new change or concrete unresolved finding. Record untested coverage without inventing success or turning an optional missing environment into a new provisioning task.
- Do not install/reinstall vcpkg, SDKs, emulators or toolchains solely to expand validation. Git hooks must not silently restore/build/test on every commit/push.
- No routine public package/archive/image/site downloads, repeated member/hash comparison or consumer execution. Retain lockfile integrity, required signing/licence/provenance checks and one necessary identity/integrity check at an actual publication handoff. Additional downloads require a concrete integrity/publication defect or explicit user request.
- Promote the original candidate. Use provider upload/deployment receipts and status/coordinate metadata; no public-byte polling. Maven main uses SNAPSHOT, and formal Central publication requires a deliberate tag.
- Do not create tags, republish, re-sign or allocate replacement versions solely for verification. Diagnose failures before rerunning; no blind retries.
- Documentation-only edits require consistency/link review without an additional local product-build or runtime-test cycle. Code repositories still run their existing applicable CI for documentation-only PRs. Keep AGENTS, active docs, workflow dependencies and actual release inventories synchronized. Preserve historical evidence as history, not as a rerun mandate.

## Network and resources

Use the normal network connection. On a failed network operation, stop and report the exact operation rather than changing networking or repeatedly retrying. Do not invoke wsl.exe or WSL wrappers; use a directly available WSL terminal only if necessary. Run at most one CPU-heavy local build or test per workstation at a time, through the build slot, and reuse existing caches; coding and review continue in parallel.

## Review and merge

Review each complete PR and fix findings. Documentation repositories that have no CI merge directly after review. In code repositories, every PR, including documentation-only changes, must run the existing applicable CI and may merge only after all retained latest-head checks succeed. Do not skip configured checks or weaken branch protection to merge documentation changes. Remove obsolete runtime/macOS job references rather than adding fake passing gates. Do not bypass retained build/security/signing failures.

Post-merge verification is limited to the expected merge commit, required build/publication/deployment job result and clean fast-forward primary update. Do not start another public-download/hash/install/device/browser/runtime cycle. Keep branches and worktrees, protect credentials and report actual results and material untested coverage. Deployment success is not a live test, and compilation is not physical-device or full commercial acceptance.
