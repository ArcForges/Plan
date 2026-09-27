---
task: ADOPT.07.harness
status: complete
recorded: 2026-09-27
claimant: w-20260927-cloud-lane
epoch: 1
---

# Adopt Cloud: Cloud Harness

## Inputs and source comparison

Cloud integration owner w-20260927-cloud-lane, role epoch 2, reviewed the [frozen Cloud baseline](../adoption/baseline.md#cloud), source `60c5c4288b126c81a09fa5d1944671e9acb87495`, generated task outcomes/obligation parts, and the corresponding WP requirements/tests/gates. No open Cloud PR existed at the freeze.

No Task effect-certainty classifier, automation definition/occurrence store or real Workflow dispatch source exists. Cloud has no model loop to inherit.

The complete tracked source inventory is summarized in [Cloud repository facts](../adoption/Cloud.md). Bootstrap build/dependency/provenance checks and deployment receipts remain valid for their original scope, but do not satisfy these missing outcomes. Each row retains the full named task outcome as remaining work, including its mapped tests and completion gates.

## Classifications

| Task | Classification | Bound write scope | Remaining scope | Evidence / conflicts / blockers |
|---|---|---|---|---|
| HAR.04 | gap | Planned additions: Cloud:src/Cloud/ArcForges.Cloud.Modules.Task/EffectCertainty/** | Failure classification keys on whether dispatch occurred, never on whether bytes returned; the unknown path releases customer holds at the reconciliation deadline while retaining supplier liability; no failure path silently resolves unknown to didNotHappen, and no dispatched request is retried automatically. | Frozen source lacks this outcome. Normal graph prerequisites apply; no implementation conflict found. |
| HAR.06 | gap | Planned additions: Cloud:src/Cloud/ArcForges.Cloud.Modules.Task/Automation/** | Automation definition/version, trigger schedule/event cursor, occurrence dedup and grant/budget snapshot live in C# Task-owned tables; bounded leased jobs dispatch the same RunWorkflow identity through the existing outbox; disabled/revoked automation stops future occurrences; the labelled WP-17 automation fixture is removed. | Frozen source lacks this outcome. Normal graph prerequisites apply; no implementation conflict found. |

## Scope binding and validation

Existing source is `src/ArcForges.Cloud` (assembly/namespace ArcForges.Cloud), with tests under `tests/ArcForges.Cloud.Tests`, worker code under `worker`, tooling under `tooling`, and policy/provenance under `eng`. Logical `src/Cloud/ArcForges.Cloud.Host` and `src/ArcForges.Cloud.Host` bind to the existing host, preserving its identity. Module/Storage/PublicApi/Jobs directories in the rows are absent planned additions beneath Cloud, not permissions to rename the bootstrap or copy another repository. New projects, dependency locks, root registration and workflow changes require explicit scope/resource reconciliation before implementation; this ledger itself grants no additional writes. Empty-write integration tasks remain evidence joins and cannot implement missing producers.

No task is inherited; no inherited task record is created. The slice opens exactly its listed tasks under their normal prerequisites and does not authorize execution outside the selected launcher scope. No new substitute is registered or accepted; no runtime/product gate closes. Removed-product cleanup remains with CON.23/GOV.17/GOV.18, outside these ledger edits.

Validation: source inventory, task/obligation and frozen receipt review, plus explicit-root Plan consistency check. No build, runtime/provider test, artifact download or publication recheck. Untested coverage is every missing outcome and its real integration/acceptance cases. Ledger PR, independent exact-head approval and merge commits are preserved in the PR and claim audit trail.
