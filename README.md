# ArcForges V2 delivery plan

This is the sole current task graph for the general CLI sandbox, resource management, optional Go Center and Blazor remote dashboard product defined by [Design AD-0022](https://github.com/ArcForges/ArcForges-Design/blob/main/docs/decisions/AD-0022-cli-sandbox-platform-pivot.md).

**40 current tasks, beginning with the documents-first dependency upgrade AFV2-ENV-01.** [sequence.md](sequence.md) is generated from [delivery-graph.json](delivery-graph.json). Each task includes exact repository/module scope, removals, design/API references, tests, Windows/Linux evidence, migration, rollback, independent review and completion criteria. `python tools/plan.py show AFV2-ENV-01` prints the first task.

Read [execution policy](execution-policy.md), [delivery procedure](delivery-procedure.md), [acceptance register](acceptance-register.md), [baseline](baseline.md), and [Codex handoff](codex-handoff.md) before implementation. The ledger records authorization of the original 39 tasks and the added upgrade task. Review and merge the AD-0023 Design/Plan amendment before starting AFV2-ENV-01; preserve the parked BASE-01 work.

All 63 earlier tasks leave the current sequence. Their 11 delivered, 8 complete, 36 planned and 8 superseded facts are preserved byte-for-byte with their ledger under the [frozen-baseline notice](history/v1-20261114-notice.md). Never resume that graph, and never count its completion as V2 delivery.

## Validation and merge order

```sh
python tools/plan.py sequence --write
python tools/plan.py validate --design <ArcForges-Design-worktree>
python <ArcForges-Design-worktree>/tools/check_design.py --plan delivery-graph.json
python -m unittest discover -s tests -v
```

These author diagnostics do not replace required native host verification. One complete Design PR merges first; then both Plan host legs verify the exact Plan head against the new Design main. The unchanged `arcforges/windows`/`arcforges/linux` gates and independent review remain mandatory. Candidate branches and paired static checks are not a claim that main or the product is already V2.

The [Design review record](https://github.com/ArcForges/ArcForges-Design/blob/main/docs/verification/v2-review.md) preserves the original V2 review. Design #66 and Plan #98/#99 are merged; the dependency-policy amendment still requires its own final-head independent review and native verification in Design-first order.
