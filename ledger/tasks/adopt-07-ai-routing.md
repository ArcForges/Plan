---
task: ADOPT.07.ai-routing
status: complete
recorded: 2026-09-27
claimant: w-20260927-cloud-lane
epoch: 1
---

# Adopt Cloud: Workers AI routing and metering

## Inputs and source comparison

Cloud integration owner w-20260927-cloud-lane, role epoch 2, reviewed the [frozen Cloud baseline](../adoption/baseline.md#cloud), source `60c5c4288b126c81a09fa5d1944671e9acb87495`, generated task outcomes/obligation parts, and the corresponding WP requirements/tests/gates. No open Cloud PR existed at the freeze.

No Agent tariff, metering, supplier routing or settlement source exists; the Worker imports only the Container router.

The complete tracked source inventory is summarized in [Cloud repository facts](../adoption/Cloud.md). Bootstrap build/dependency/provenance checks and deployment receipts remain valid for their original scope, but do not satisfy these missing outcomes. Each row retains the full named task outcome as remaining work, including its mapped tests and completion gates.

## Classifications

| Task | Classification | Bound write scope | Remaining scope | Evidence / conflicts / blockers |
|---|---|---|---|---|
| AIR.01 | gap | Planned additions: Cloud:src/Cloud/ArcForges.Cloud.Modules.Agent/Tariffs/** | Versioned tariffs with effective dates and the full cost-dimension set exist; each run locks a tariff snapshot at start; a historical charge is reconstructible from its locked snapshot; image-context units are metered separately from text units. | Frozen source lacks this outcome. Normal graph prerequisites apply; no implementation conflict found. |
| AIR.02 | gap | Planned additions: Cloud:src/Cloud/ArcForges.Cloud.Modules.Agent/Metering/** | C# reservation/intent commits before CF I/O, outcome receipt precedes settlement, attempt usage revisions are immutable; interactive runs and bounded inference jobs are both covered with stable attempt identity, supplier exposure, Run customer total and exact credit lots; unknown usage follows the deadline/liability ladder, never an automatic resend. | Frozen source lacks this outcome. Normal graph prerequisites apply; no implementation conflict found. |
| AIR.03 | gap | Planned additions: Cloud:src/Cloud/ArcForges.Cloud.Modules.Agent/Routing/** | Only the Workers AI binding and explicit admitted catalogue route calls, with no AI Gateway/multiprovider bypass/fallback; self-host uses operator-owned credentials/funding with payment disabled by default; no silent substitution or credit crossing between official/self-host realms. | Frozen source lacks this outcome. Normal graph prerequisites apply; no implementation conflict found. |
| AIR.04 | gap | Planned additions: Cloud:src/Cloud/ArcForges.Cloud.Modules.Agent/InteractionRecords/** | A provider interaction record exists per call, separate from execution/capability/audit traces, carrying no content beyond policy; cost transparency surfaces show what a run cost and why. | Frozen source lacks this outcome. Normal graph prerequisites apply; no implementation conflict found. |
| AIR.06 | gap | Planned additions: Cloud:src/Cloud/ArcForges.Cloud.Modules.Agent/Metering/UncertainOutcome/** | Supplier intent/exposure and customer settlement are proven independent: Brave search is operator-funded while processing results is customer inference; a crash before/after dispatch, an unknown deadline, and late usage after a closed no-later-debit window are all handled without an automatic model retry. | Frozen source lacks this outcome. Normal graph prerequisites apply; no implementation conflict found. |
| AIR.90 | gap | Planned additions: Cloud:tests/Cloud.Tests.Integration/AiMetering/** | All AIR deliverables assemble under the selected repository/package/runtime/protocol authorities with the frozen Workers AI model subset, capability matrix, normalization and known/unknown usage contract proven; Gateway is confirmed not a required dependency. | Frozen source lacks this outcome. Normal graph prerequisites apply; no implementation conflict found. |

## Scope binding and validation

Existing source is `src/ArcForges.Cloud` (assembly/namespace ArcForges.Cloud), with tests under `tests/ArcForges.Cloud.Tests`, worker code under `worker`, tooling under `tooling`, and policy/provenance under `eng`. Logical `src/Cloud/ArcForges.Cloud.Host` and `src/ArcForges.Cloud.Host` bind to the existing host, preserving its identity. Module/Storage/PublicApi/Jobs directories in the rows are absent planned additions beneath Cloud, not permissions to rename the bootstrap or copy another repository. New projects, dependency locks, root registration and workflow changes require explicit scope/resource reconciliation before implementation; this ledger itself grants no additional writes. Empty-write integration tasks remain evidence joins and cannot implement missing producers.

No task is inherited; no inherited task record is created. The slice opens exactly its listed tasks under their normal prerequisites and does not authorize execution outside the selected launcher scope. No new substitute is registered or accepted; no runtime/product gate closes. Removed-product cleanup remains with CON.23/GOV.17/GOV.18, outside these ledger edits.

Validation: source inventory, task/obligation and frozen receipt review, plus explicit-root Plan consistency check. No build, runtime/provider test, artifact download or publication recheck. Untested coverage is every missing outcome and its real integration/acceptance cases. Ledger PR, independent exact-head approval and merge commits are preserved in the PR and claim audit trail.
