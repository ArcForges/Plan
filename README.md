# ArcForges Plan

The authoritative delivery plan for **ArcForges**, the flagship resource-control and execution platform. The design lives in [ArcForges/ArcForges-Design](https://github.com/ArcForges/ArcForges-Design).

| Document | Purpose |
|---|---|
| [execution-policy.md](execution-policy.md) | Serial delivery rules: one active task, distinct-evidence verification, publication and safety rules |
| [delivery-procedure.md](delivery-procedure.md) | Steps for one task, from start to delivered or complete |
| [execution-prompt.md](execution-prompt.md) | The self-contained coordinator prompt: the user pastes a range of `sequence.md` steps, and the session delivers exactly that range. The user's copy is `C:\MyFile\Projects\ArcForges\ArcForges.md`. |
| [entry-prompts.md](entry-prompts.md) | Prompts for worker, reviewer, resume and status sessions |
| [roadmap.md](roadmap.md) | The canonical roadmap: committed delivery (the graph), accepted future work (`RM-*`), exploratory ideas (`EX-*`), and how items are promoted |
| [delivery-graph.json](delivery-graph.json) | The 52 tasks (AF-*) in serial order across milestones M0–M15, with full fields, real dependencies and risks; M15 is production activation (AF-PROD-01) |
| [sequence.md](sequence.md) | Generated view of the serial sequence and states |
| [acceptance-register.md](acceptance-register.md) | Deferred real-world validation (AR-*) and human prerequisites (H-*) |
| [baseline.md](baseline.md) | Repository heads, admitted versions and workstation facts at the start |
| [ledger/](ledger/README.md) | Append-only delivery ledger |
| [history/](history/legacy-disposition.md) | Archived launchers, the legacy agent definition, and the disposition of the previous model |

## Tool

```bash
python tools/plan.py validate --design ../ArcForges-Design   # graph, sequence and register checks, cross-checked with the design
python tools/plan.py next                                     # the active task, or the next task to start
python tools/plan.py show AF-NODE-01
python tools/plan.py set-state AF-REPO-01 active
python tools/plan.py ledger AF-REPO-01 started "scaffold work begins"
python -m unittest discover -s tests -v
```

## Verification

Every pushed head is verified after the push ([AD-0020](https://github.com/ArcForges/ArcForges-Design/blob/main/docs/decisions/AD-0020-post-push-verification-and-required-checks.md); [AGENTS.md](AGENTS.md) rule 6). Each host fetches the commit from GitHub and runs what the `Plan checks` workflow runs, against ArcForges-Design `main`: the Windows host through the Windows MCP server, the Linux host through the Linux MCP server, never through local WSL ([AD-0019](https://github.com/ArcForges/ArcForges-Design/blob/main/docs/decisions/AD-0019-mcp-first-verification.md)). Each host reports the commit status `arcforges/windows` or `arcforges/linux`, and the `main` ruleset requires both before a PR can merge. The workflow runs only for external PRs, the merge queue and manual dispatch.

```bash
python eng/verify.py install          # once per clone, from the main checkout on main (removes the retired pre-push hook)
python eng/verify.py list             # the steps each host runs for a commit
python eng/verify.py run-and-report   # on a host, in a worktree at the pushed commit: verify it and report its status
python eng/verify.py run              # verify this host's leg of HEAD without reporting
```

The previous parallel plan is frozen in `ArcForges/Plan-Parallel` (main `5ccbb392`). It is never resumed ([history/legacy-disposition.md](history/legacy-disposition.md)).
