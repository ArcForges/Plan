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

The previous parallel plan is frozen in `ArcForges/Plan-Parallel` (main `5ccbb392`). It is never resumed ([history/legacy-disposition.md](history/legacy-disposition.md)).
