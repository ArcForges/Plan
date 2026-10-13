# Delivery procedure (one task)

Follow [execution-policy.md](execution-policy.md). These steps take one task from `planned` to `delivered` or `complete`.

## 1. Start

1. `python tools/plan.py next` names the task. `python tools/plan.py show <id>` prints its full record.
2. **Read** the task's design references in ArcForges-Design, its requirements and its acceptance criteria. Check the open acceptance-register entries and human prerequisites the task lists.
3. **Mark it active.**
   - `python tools/plan.py set-state <id> active`
   - `python tools/plan.py ledger <id> started "<one line>"`
   - Commit to a Plan branch `plan/<id>-start`, then PR and merge. State-only record PRs need no independent review (policy §4): the coordinator checks the diff and Plan CI, then merges.
4. **Create a worktree** per repository in the task's write scope: `<repo>/.worktree/<id-lower>` on branch `task/<id-lower>`, from the repository's current main. Never work in a main checkout.

## 2. Implement

1. Stay inside the task's `repositories[].paths` write scope. A needed change outside it is either a new task proposal (stop and record it) or an explicit scope note in the PR when trivial.
   - **Package files.** A task that pins, adds or updates a package may also change the repository's central package file (`Directory.Packages.props`), its lock files and its dependency admission records.
2. Follow each repository's `AGENTS.md`: locked restores, dependency admission records for new packages, analyzers, AOT settings.
3. Build vertically. The task's user-visible outcome works end to end. Do not leave disconnected interface shells.
4. Write tests at the layers named in ArcForges-Design `docs/architecture/16-testing-strategy.md`. Use fakes only where `fakes_allowed` lists them.
5. Run heavy local commands through ArcForges once AF-EXEC-01 is delivered (dogfooding, §6 of the policy).

## 3. Author verification

Run exactly what the task's `verification.author` names. Record in the PR body:
- the commands, with the result of each;
- the environments covered (Windows real, WSL2 real);
- which acceptance criterion each test proves;
- benchmarks for measured paths;
- acceptance-register entries prepared or advanced.

## 4. Review

1. The coordinator pushes the branch and opens the PR. The PR body ends with `🤖 Generated with [Claude Code](https://claude.com/claude-code)`, and commits end with `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`.
2. **One independent reviewer** (Opus 5.5, a fresh session) reviews the exact head:
   - the full diff against the design references and acceptance criteria;
   - distinct checks only (policy §3).

   The reviewer writes a review record with findings, each marked blocking or non-blocking, and lists the checks run with their reasons.
3. The author fixes blocking findings. Re-review covers only the delta.
4. The coordinator posts the review record on the PR.

## 5. Merge and publish

1. Hosted CI must pass at the reviewed head. The coordinator reads the results with the PR tools.
2. **Merge** at the reviewed head (no auto-merge). Outward-facing changes need the user's approval first (policy §4).
3. **Verify the publication or deployment.**
   - **Packages:** the cohort on main, and admission rules respected.
   - **Deploys:** the guarded main-push deploy succeeded.
   - Record the identifiers.
4. **Record.**
   - `python tools/plan.py set-state <id> delivered --pr <url> --merge <Repo>@<sha> [--publication "<cohort or deploy id>"]`
   - `python tools/plan.py ledger <id> delivered "<summary>"`
   - Plan PR, then merge.
5. **Complete.** When every completion prerequisite holds, including real-environment evidence possible now, run `set-state <id> complete` and add a ledger record. Deferred real-world items stay in the acceptance register.
6. **Continue.** Report the delivery and go back to §1 with `python tools/plan.py next` (execution policy §1.5). Stop only at a stop point: an outward-facing approval, no eligible task, a decision only the user can make, or the user's instruction.

## 6. Interruptions

- **Stopped work.** Leave the worktree and branch in place, and record the exact state (head, uncommitted files, next step) in a ledger `note`. Never discard work.
- **Resuming.** A later session resumes from that record. Do not restart from scratch if the record is usable.
- **Blockers.** A blocker needing a human step goes into the acceptance register (or as an H item), with its **Blocks** column. When it blocks the task, the coordinator sets the task `blocked` (`python tools/plan.py set-state <id> blocked --blocked-by H-xx --reason "…"`), records it in the ledger, tells the user exactly what is needed, and continues with `python tools/plan.py next`, which skips the blocked task and its dependents.
- **Production activation.** Cloud and Web tasks deploy dark on merge (Design 10 §8), so no production prerequisite blocks an implementation merge. AF-PROD-01 activates the surfaces with the user's approval. Ask the user for H-05, H-06, H-09, H-10, H-16 and H-20 when AF-ACC-01 starts, so that activation is not held up.
