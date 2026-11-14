# Agent instructions — ArcForges V2 Plan

Read [execution-policy.md](execution-policy.md), [delivery-procedure.md](delivery-procedure.md), [acceptance-register.md](acceptance-register.md) and the exact current task before delivery. Design AD-0022, the AD-0023 dependency policy and this schema3 graph are current authority. Frozen history is evidence only.

## Scope and records

1. Work in `.worktree/<key>` on `plan/<topic>` branches, never in a primary main checkout. Product implementations use their own task worktrees.
2. One active authorized AFV2 task at a time. The coordinator owns graph states/ledger through `tools/plan.py`. `sequence.md` is generated. Do not start product implementation from this design migration alone; record the exact user-authorized range first.
3. Every task has real dependencies, allowed module paths, removals, migration, rollback, native checks, independent review and observable completion. A superseded task is not a satisfied dependency. Preserve interrupted work and exact next step.
4. The previous 63-task graph and ledger are immutable in history; never rewrite completed facts or reuse their completion as V2 evidence. All new tasks initially planned. No old AI/MCP/cache/Task runtime or unrelated app becomes current scope.
5. Run `python tools/plan.py validate --design <Design>` and the reciprocal Design traceability checker. Native Windows/Linux source facts, future experiments and external activation prerequisites remain distinct. Keep all published package versions and applied migration bytes immutable; protect shared consumers.

## Required verification and review — unchanged gates

6. Every PR into main needs the repository's required host statuses at its exact latest head and independent nonauthor review. The Plan requires both `arcforges/windows` and `arcforges/linux`; rulesets have no bypass actors and require the branch up to date with main. External PRs also pass configured full hosted CI. Read untrusted external diffs before a host executes them.
7. Push first. On each designated host, fetch that exact branch/SHA from GitHub, create a worktree and run `python eng/verify.py run-and-report`. The command alone reports pending/success/failure/error. It must run all steps and succeed before success is claimed. Never post/copy/edit statuses by hand.
8. Windows verification runs on the owner's native Windows workstation through its Windows MCP server. Linux runs on the H-22 native Linux host through its Linux MCP server with real systemd user manager/cgroupv2 delegation. An agent sandbox, local WSL, SSH, remote-shell replacement or other machine is not a verification host. Hosts fetch independently; no bundles or receipts travel between hosts. Prerequisite installs are the owner's.
9. Plan host profiles include exact invoking/PATH Python selection via `python eng/check_toolchain.py`, `python tools/plan.py validate --design <Design>`, `python <Design>/tools/check_design.py --plan delivery-graph.json`, all tooling unittests, and actionlint when workflows change. `<Design>` is freshly fetched Design origin/main. `eng/verify.py list` describes exact steps; it is not permission to skip any. Local author diagnostics are not these statuses.
10. Missing/unreachable host or prerequisite means the status stays missing and that PR cannot merge. Report the concrete limitation and preserve completed reviewable work. Never weaken a check, disable/remove hooks, use `git push --no-verify`, change protection/rulesets/permissions, substitute mocks or forge review to get a merge. Verification-tool engineering changes require reviewed justification, never a bypass motive.
11. Independent review covers complete final head and acceptance; fixes get delta review and a new head needs fresh host checks. Graph/policy/tool changes require review. State/evidence/ledger-only Plan PRs retain the coordinator-check exception, but still need both required host statuses.
12. Design merges first. Then rerun Plan native legs against actual new Design main. Before every Plan merge, current Design main must equal the `design-main` recorded in both host summaries; otherwise rerun both legs. A Plan status does not encode its Design baseline. Never enable auto-merge unless explicitly requested.

## Standing engineering constraints

13. Never read/print secrets. No proxy/network/security setting changes. Keep Dependabot PRs untouched. Never unpublish/deprecate/delete published versions; never admit rolled-back Contracts 1.0.0-ci.350.1 or Build.Policy 1.0.0-ci.124.1 or a version not descended from producer main.
14. Cloudflare only through repository guarded scripts; previews and workers.dev off; production changes only through guarded main-push deploys. Unconfigured official surfaces stay dark. Public activation and release-channel publication require the concrete approval/prerequisites in AFV2-PROD-01. Do not reuse historical external bootstrap authority.
15. Keep existing Windows/Linux build, packaging, offline/unit/static and necessary security checks. No macOS/device/GUI/browser/live-service/inference CI. Explicit manual runtime/browser acceptance uses approved local venues, not new hosted jobs.
16. Run long work in the background with bounded output; no busy sleep/poll loops. Restore/build once per unchanged input and use incremental/no-restore/no-build where applicable. Reviewers rerun distinct disputed/changed evidence only. Measure before resource throttles; never clean caches without cause.
17. Use actual contributor/tool identity in commits/PRs. Stop when the authorized range completes, on an unsatisfied merge gate, a real owner-only decision, or user stop. A blocked task can be preserved while independent authorized tasks continue. Do not invent requirements after agreed acceptance.
