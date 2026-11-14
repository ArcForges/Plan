# One V2 delivery task

For the AD-0023 amendment, complete Design/Plan document review, required native verification and Design-first merges before implementing upgrades. AFV2-ENV-01 then delivers the seven-repository latest-stable dependency baseline and local/CI parity; only after its acceptance may BASE-01 resume. All dependency compatibility work retains the complete checks below.

The owner-approved 2026-11-15 Contracts Go qualifications in AD-0023 retain the full selected graph, all current checks and final Windows/Linux actual-closure evidence. Merge their paired policy amendment in the same Design-first order before affected admission; no other dependency exception is implied.

1. Read [execution policy](execution-policy.md), the authorized AFV2 range, `plan.py next`, full task record, Design refs and register Blocks. A task outside the authorized range is not implied scope.
2. Fetch latest involved main branches, inspect existing PRs/worktrees and actual deployed/migration state relevant to the task. Reuse valid prior work. Create isolated task worktrees.
3. Mark the eligible task active through `plan.py set-state`; record the user's authorization and task start. State-only Plan records retain required host checks even where independent review is exempt.
4. Implement the complete vertical slice inside allowed paths, including declared old-code removal, consumers, error/recovery behavior and migration. Never leave disconnected stubs or weaken a platform guarantee.
5. Run targeted author tests and the task's native Windows/Linux scenarios. Record real results and explicit unavailable external prerequisites; do not substitute source review or mocks for mandatory platform behavior.
6. Push the final candidate. Fetch its exact SHA on each required native MCP host and run `python eng/verify.py run-and-report` in that host's worktree. A missing host blocks merge. An agent sandbox check is author diagnostic only.
7. Have an independent nonauthor reviewer inspect the complete latest diff and acceptance evidence. Fix blockers in one focused batch, review the delta and reverify the new head on required hosts. Post the truthful review record.
8. Read actual required statuses, resolved threads and external hosted CI where applicable. Merge only that reviewed up-to-date head. Do not enable auto-merge or change protections.
9. Inspect applicable main-push publication/deployment identity; record all PRs/merges/artifacts via `plan.py set-state ... delivered` and the ledger. Complete only when all completion prerequisites hold. Official activation has its separate explicit approval task.
10. Continue with the next eligible task inside the authorized range. On interruption record exact SHA/worktree/unfinished steps. On a named missing prerequisite mark blocked and continue independent authorized work; never resume old task IDs.

For paired Design/Plan amendments, Design merges first, then Plan host verification reruns against actual new Design main. Freeze and preserve historical evidence; no old task can be converted into a new delivered task.
