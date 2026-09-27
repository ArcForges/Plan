---
task: ADOPT.07.policy
status: complete
recorded: 2026-09-27
claimant: w-20260927-cloud-lane
epoch: 1
---

# Adopt Cloud: Dynamic policy and configuration

## Inputs and source comparison

Cloud integration owner w-20260927-cloud-lane, role epoch 2, reviewed the [frozen Cloud baseline](../adoption/baseline.md#cloud), source `60c5c4288b126c81a09fa5d1944671e9acb87495`, generated task outcomes/obligation parts, and the corresponding WP requirements/tests/gates. No open Cloud PR existed at the freeze.

No Configuration or Policy business module, bundle activation, hard-limit/rollout/kill-switch or publication/recovery implementation exists.

The complete tracked source inventory is summarized in [Cloud repository facts](../adoption/Cloud.md). Bootstrap build/dependency/provenance checks and deployment receipts remain valid for their original scope, but do not satisfy these missing outcomes. Each row retains the full named task outcome as remaining work, including its mapped tests and completion gates.

## Classifications

| Task | Classification | Bound write scope | Remaining scope | Evidence / conflicts / blockers |
|---|---|---|---|---|
| POL.01 | gap | Planned additions: Cloud:src/Cloud/ArcForges.Cloud.Modules.Policy/**/Boundaries/** | Policy, entitlement, user settings, health and the data plane are kept structurally distinct with an architecture test asserting no policy type reaches an entitlement decision, each boundary backed by a failing negative fixture. | Frozen source lacks this outcome. Normal graph prerequisites apply; no implementation conflict found. |
| POL.02 | gap | Planned additions: Cloud:src/Cloud/ArcForges.Cloud.Modules.Configuration/** | policy.body.v1 and configuration.v1 bundles validate exactly against their schema (key/type/scope/limit/cross-reference), an invalid bundle is rejected wholesale, and activation is a dry-run proposal with dual approval and compare-and-swap. | Frozen source lacks this outcome. Normal graph prerequisites apply; no implementation conflict found. |
| POL.03 | gap | Planned additions: Cloud:src/Cloud/ArcForges.Cloud.Modules.Policy/**/HardLimits/** | Safety-critical limits are compiled and authoritative; remote policy may only tighten them, and any attempt to loosen one is rejected and recorded. | Frozen source lacks this outcome. Normal graph prerequisites apply; no implementation conflict found. |
| POL.04 | gap | Planned additions: Cloud:src/Cloud/ArcForges.Cloud.Modules.Policy/**/Rollout/** | Deterministic target/percent hashing, exclusion groups and sticky experiment allocation select the same result for the same stable subject/version across languages, and rollout cannot grant commercial or security authority. | Frozen source lacks this outcome. Normal graph prerequisites apply; no implementation conflict found. |
| POL.05 | gap | Planned additions: Cloud:src/Cloud/ArcForges.Cloud.Modules.Policy/**/KillSwitch/** | All four kill-switch modes propagate promptly with a defined blast radius, a mandatory reason, a user-visible explanation and a complete audit record, and are reversible. | Frozen source lacks this outcome. Normal graph prerequisites apply; no implementation conflict found. |
| POL.06 | gap | Planned additions: Cloud:src/Cloud/ArcForges.Cloud.Modules.Policy/**/Resolution/** | Policy resolves across application, workspace, device and installation scopes in a fixed order, and the server can state which scope and bundle produced any effective value. | Frozen source lacks this outcome. Normal graph prerequisites apply; no implementation conflict found. |
| POL.07 | gap | Planned additions: Cloud:src/Cloud/ArcForges.Cloud.Modules.Policy/**/Compatibility/** | Compatibility rules express supported client windows and blocked version ranges; a bad version is blockable without affecting neighbours, and a minimum-version requirement is never enforced before its grace period elapses. | Frozen source lacks this outcome. Normal graph prerequisites apply; no implementation conflict found. |
| POL.08 | gap | Planned additions: Cloud:src/Cloud/ArcForges.Cloud.Modules.Policy/**/Publication/** | Bundles publish with versioning and audit, and the server-side staleness/application-timing contract is defined so a change is never applied in a way that produces inconsistent behaviour mid-operation. | Frozen source lacks this outcome. Normal graph prerequisites apply; no implementation conflict found. |
| POL.10 | gap | Planned additions: Cloud:eng/provenance/records/** | The package-level owned-artifact/real-integration receipt is recorded confirming every CF run and effect uses the required policy version and stale/disallowed models or revoked permission fail deterministically without client-side policy becoming authority. | Frozen source lacks this outcome. Normal graph prerequisites apply; no implementation conflict found. |
| POL.11 | gap | No source writes declared; integrate real prerequisite outputs and record evidence under the existing task procedure. | a genuinely published bundle is fetched, cached, and correctly falls back to last-known-good on a later real staleness condition, not just against POL.09's local fixture | Frozen source lacks this outcome. Normal graph prerequisites apply; no implementation conflict found. |

## Scope binding and validation

Existing source is `src/ArcForges.Cloud` (assembly/namespace ArcForges.Cloud), with tests under `tests/ArcForges.Cloud.Tests`, worker code under `worker`, tooling under `tooling`, and policy/provenance under `eng`. Logical `src/Cloud/ArcForges.Cloud.Host` and `src/ArcForges.Cloud.Host` bind to the existing host, preserving its identity. Module/Storage/PublicApi/Jobs directories in the rows are absent planned additions beneath Cloud, not permissions to rename the bootstrap or copy another repository. New projects, dependency locks, root registration and workflow changes require explicit scope/resource reconciliation before implementation; this ledger itself grants no additional writes. Empty-write integration tasks remain evidence joins and cannot implement missing producers.

No task is inherited; no inherited task record is created. The slice opens exactly its listed tasks under their normal prerequisites and does not authorize execution outside the selected launcher scope. No new substitute is registered or accepted; no runtime/product gate closes. Removed-product cleanup remains with CON.23/GOV.17/GOV.18, outside these ledger edits.

Validation: source inventory, task/obligation and frozen receipt review, plus explicit-root Plan consistency check. No build, runtime/provider test, artifact download or publication recheck. Untested coverage is every missing outcome and its real integration/acceptance cases. Ledger PR, independent exact-head approval and merge commits are preserved in the PR and claim audit trail.
