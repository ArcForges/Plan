# Delivery procedure (one task)

Follow [execution-policy.md](execution-policy.md). These steps take one task from `planned` to `delivered` or `complete`.

## 1. Start

1. The task is the next eligible task of the authorized range (execution policy §1.2 and §1.5; `python tools/plan.py next` names the first eligible task overall, which may lie outside the range). `python tools/plan.py show <id>` prints its full record.
2. **Read** the task's design references in ArcForges-Design, its requirements and its acceptance criteria. Check the open acceptance-register entries and human prerequisites the task lists.
3. **Mark it active.**
   - `python tools/plan.py set-state <id> active`
   - `python tools/plan.py ledger <id> started "<one line>"`
   - Commit to a Plan branch `plan/<id>-start`, then PR and merge. State-only record PRs need no independent review (policy §4): the coordinator checks the diff, pushes it, verifies the head on both hosts (`AGENTS.md` rule 6) and merges once the required statuses pass.
4. **Create a worktree** per repository in the task's write scope: `<repo>/.worktree/<id-lower>` on branch `task/<id-lower>`, from `origin/main` after `git fetch`. Never work in a main checkout.

## 2. Implement

1. Stay inside the task's `repositories[].paths` write scope.
   - **Repairs.** A defect in delivered code that prevents this task's acceptance is repaired within the task: in its PR with a scope note when it is small and inside the write paths, otherwise in a separate repair PR in the owning repository, reviewed like a task and recorded in the task's evidence (execution policy §1.6).
   - **The task's own needs.** Small changes outside the write paths that the task's own specified scope needs (for example solution entries, wiring, or view models for its pages) go into its PR with a scope note. A larger one first widens the task record through a reviewed Plan PR.
   - **New scope.** Behaviour that no task specifies is a new task proposal: record it in the ledger, report it and do not build it.
   - **Package files.** A task that pins, adds or updates a package may also change the repository's central package file (`Directory.Packages.props`), its lock files and its dependency admission records.
2. Follow each repository's `AGENTS.md`: locked restores, dependency admission records for new packages, analyzers, AOT settings.
3. Build vertically. The task's user-visible outcome works end to end. Do not leave disconnected interface shells.
4. Write tests at the layers named in ArcForges-Design `docs/architecture/16-testing-strategy.md`. Use fakes only where `fakes_allowed` lists them.
5. Run heavy local commands through ArcForges once AF-EXEC-01 is delivered (dogfooding, §6 of the policy).

## 3. Author verification

Run exactly what the task's `verification.author` names: the affected suites while iterating (`AGENTS.md`, Efficient execution). Before handing over, the author may run `python eng/verify.py run` on a host (a local check that reports nothing). Record in the PR body:
- the commands, with the result of each;
- the environments covered (native Windows real, native Linux real);
- which acceptance criterion each test proves;
- benchmarks for measured paths;
- acceptance-register entries prepared or advanced.

## 4. Review

1. The coordinator pushes the branch and opens the PR, then runs `python eng/verify.py run-and-report` on each host for the head ([AD-0020](https://github.com/ArcForges/ArcForges-Design/blob/main/docs/decisions/AD-0020-post-push-verification-and-required-checks.md); `AGENTS.md` rule 6). The hosts report `arcforges/windows` and `arcforges/linux` on the commit, which the `main` ruleset requires. A failure goes back to the author (or the coordinator fixes a coordinator-side cause), and the fixed branch is pushed and verified again. A status is never posted by hand (policy §3). Any commit co-author trailer or PR footer must identify the actual contributors and tools used.
2. **One independent reviewer** (a fresh session) reviews the exact head:
   - the full diff against the design references and acceptance criteria;
   - distinct checks only (policy §3).

   The reviewer writes a review record with findings, each marked blocking or non-blocking, and lists the checks run with their reasons.
3. The author fixes blocking findings. The coordinator pushes the fixed head and verifies it on both hosts (a new head has no statuses). Re-review covers only the delta.
4. The coordinator posts the review record on the PR.

## 5. Merge and publish

1. The merge gate holds at the reviewed head (policy §4):
   - **every PR:** the required statuses (`arcforges/windows`, `arcforges/linux`) report success for that head, and the review approved; GitHub refuses the merge otherwise;
   - **external PRs**: hosted CI also passed at that head (read with the PR tools, never polled).
2. **Merge** at the reviewed head (no auto-merge). Outward-facing changes need the user's approval first (policy §4).
3. **Verify the publication or deployment.** Delivery workflows run on the main push; it runs no separate validation, and the next task does not wait for a main CI run.
   - **Packages:** the cohort on main, and admission rules respected.
   - **Deploys:** the guarded main-push deploy succeeded.
   - Record the identifiers.
4. **Record.**
   - `python tools/plan.py set-state <id> delivered --pr <url> --merge <Repo>@<sha> [--publication "<cohort or deploy id>"]`; a multi-repository task repeats `--pr`, `--merge` and `--publication` once per PR, repository and publication
   - `python tools/plan.py ledger <id> delivered "<summary>"`
   - Plan PR, then merge.
5. **Complete.** When every completion prerequisite holds, including real-environment evidence possible now, run `set-state <id> complete` and add a ledger record. Deferred real-world items stay in the acceptance register.
6. **Continue.** Report the delivery and go back to §1 with the next eligible task of the authorized range (execution policy §1.5). Stop only at a stop point: an outward-facing approval, the authorized scope complete, no eligible task, a decision only the user can make, or the user's instruction.

## 6. Interruptions

- **Stopped work.** Leave the worktree and branch in place, and record the exact state (head, uncommitted files, next step) in a ledger `note`. Never discard work.
- **Resuming.** A later session resumes from that record. Do not restart from scratch if the record is usable.
- **Unresolved failures without a human step** (for example an external outage beyond bounded retries): return the task to `planned` (`python tools/plan.py set-state <id> planned --reason "…"`) with the ledger note above, so the single active slot is free, and continue with tasks that do not depend on it.
- **A task outside the authorized range is active:** report it and stop. Resuming, parking or finishing it is the user's decision.
- **Blockers.** A blocker needing a human step goes into the acceptance register (or as an H item), with its **Blocks** column. When it blocks the task, the coordinator sets the task `blocked` (`python tools/plan.py set-state <id> blocked --blocked-by H-xx --reason "…"`), records it in the ledger, tells the user exactly what is needed, and continues with the next eligible task of the authorized range; the blocked task and its dependents are skipped.
- **Production activation.** Cloud and Web tasks deploy dark on merge (Design 10 §8), so no production prerequisite blocks an implementation merge. AF-PROD-01 activates the surfaces with the user's approval. Ask the user for the core items H-05, H-06, H-09, H-16, H-19 and H-20, and for H-01, H-02, H-03, H-07 and H-10 for the other surfaces, when AF-ACC-01 starts, so that activation is not held up.
