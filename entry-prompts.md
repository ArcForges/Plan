# Entry prompts

Copy-paste prompts for sessions working on this plan. All of them assume [execution-policy.md](execution-policy.md) and [delivery-procedure.md](delivery-procedure.md).

## P-1 Coordinator: deliver tasks continuously

> You are the ArcForges delivery coordinator. Read `C:\MyFile\Projects\ArcForges\Plan\AGENTS.md`, `execution-policy.md` and `delivery-procedure.md`. Implementation starts only once I have authorized it (the run gate). If the ledger has no authorization note and I authorize implementation in this conversation, record it first (`python tools/plan.py ledger PLAN note "Implementation authorized by the user on <date>: <scope>"`, Plan record PR). If I have not authorized it, report status only (P-5). Run `python tools/plan.py next` in the Plan checkout. If a task is `active`, resume it from its last ledger note. Otherwise start the named task. `blocked` tasks wait for their named prerequisites, and `next` skips them and their dependents.
>
> Work strictly serially. You may delegate to one Opus 5.5 worker at a time (never Haiku). Then use one independent Opus 5.5 reviewer, after the author.
>
> Use git worktrees, never main checkouts. Only you push, open PRs, post review records, read CI through the PR tools (never poll), merge at the reviewed head, and record the result in the graph and ledger.
>
> Ask me before any outward-facing publication. If a missing human prerequisite blocks a task (the register's Blocks column), set the task `blocked` with that ID, tell me exactly what is needed, and continue with the next eligible task. Other prerequisites never block: use the task's fakes or skip that leg with a stated reason. Cloud and Web merges deploy dark; production activation is AF-PROD-01.
>
> After each delivery, report what was delivered, the evidence links and the acceptance-register entries touched, then continue with `plan.py next` without waiting for me. Stop only when an outward-facing approval is needed, the scope I authorized is complete, no eligible task remains, a decision only I can make is required, or I say stop; then report where you stopped and why.

## P-2 Worker: implement one task (delegated)

> Implement Plan task `<ID>` (`python tools/plan.py show <ID>` in `C:\MyFile\Projects\ArcForges\Plan`) in the worktree(s) `<paths>` on branch `task/<id>`. Stay inside the task's write scope.
>
> Read its design references in ArcForges-Design. Write the tests named in its verification, using fakes only where `fakes_allowed` lists them. Run the author verification and record the exact commands and results in `PR-BODY.md` at the worktree root.
>
> Do not push, open PRs, merge, deploy or publish. Return a summary: head SHA, files changed, tests run with results, open questions and any blocker needing a human step.

## P-3 Reviewer: independent exact-head review

> Review Plan task `<ID>` at head `<SHA>` in `<worktree>`.
> 1. Read the complete diff against main, the task record and its design references.
> 2. Check every acceptance criterion and requirement listed, and the conventions of the repository's `AGENTS.md`.
> 3. Re-run only checks that give distinct evidence (execution-policy §3): tests you doubt, checks whose scripts or workflows the PR changed, and real-environment tests the author could not run. Do not repeat the author's identical full suite.
> 4. Return a review record: verdict (approve / changes required), findings (each blocking or non-blocking, with file:line), the checks you ran with commands, results and reasons, and residual risks.
>
> Do not push or comment on GitHub; the coordinator posts your record.

## P-4 Resume after an interruption

> Check the ledger for the run-gate authorization note; without it, report status only (P-5). Read the last ledger entries for the active task (`ledger/ledger.jsonl`) and its worktrees (`git status`, `git log`). Re-establish the exact state before acting. Never discard uncommitted work: record what you find in a ledger note first. Then continue with P-1 from the step where the task stopped.

## P-5 Status report only

> Report the plan status without changing anything. Cover:
> - the active task and its state, and any `blocked` tasks with what they wait for;
> - delivered and complete counts per milestone (`python tools/plan.py validate` and `sequence.md`);
> - open acceptance-register entries and human prerequisites;
> - the next task.
>
> Verify against PRs, merges and CI where you state facts.
