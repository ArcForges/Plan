---
task: ADOPT.07.governance
status: complete
recorded: 2026-09-27
claimant: w-20260927-cloud-lane
epoch: 1
---

# Adopt Cloud: Family governance and policy tests

## Inputs and source comparison

Cloud integration owner w-20260927-cloud-lane, role epoch 2, reviewed the [frozen Cloud baseline](../adoption/baseline.md#cloud), source `60c5c4288b126c81a09fa5d1944671e9acb87495`, generated task outcomes/obligation parts, and the corresponding WP requirements/tests/gates. No open Cloud PR existed at the freeze.

Existing dependency/licence/provenance checks and Build.Policy are reusable bootstrap inputs. There is no ArchitectureTests project or shared-engine per-rule positive/negative fixture suite for the full WP05 Cloud scope.

The complete tracked source inventory is summarized in [Cloud repository facts](../adoption/Cloud.md). Bootstrap build/dependency/provenance checks and deployment receipts remain valid for their original scope, but do not satisfy these missing outcomes. Each row retains the full named task outcome as remaining work, including its mapped tests and completion gates.

## Classifications

| Task | Classification | Bound write scope | Remaining scope | Evidence / conflicts / blockers |
|---|---|---|---|---|
| GOV.09 | gap | Planned additions: Cloud:tests/ArchitectureTests/**; Cloud:eng/policy/exceptions.json | Cloud enforces its own layering/licence/naming/banned-API/contract-consumption rules independently, with extra weight on AOT-path banned APIs given BR-07's zero-trim/AOT-diagnostic requirement. | Frozen source lacks this outcome. Normal graph prerequisites apply; no implementation conflict found. |

## Scope binding and validation

Existing source is `src/ArcForges.Cloud` (assembly/namespace ArcForges.Cloud), with tests under `tests/ArcForges.Cloud.Tests`, worker code under `worker`, tooling under `tooling`, and policy/provenance under `eng`. Logical `src/Cloud/ArcForges.Cloud.Host` and `src/ArcForges.Cloud.Host` bind to the existing host, preserving its identity. Module/Storage/PublicApi/Jobs directories in the rows are absent planned additions beneath Cloud, not permissions to rename the bootstrap or copy another repository. New projects, dependency locks, root registration and workflow changes require explicit scope/resource reconciliation before implementation; this ledger itself grants no additional writes. Empty-write integration tasks remain evidence joins and cannot implement missing producers.

No task is inherited; no inherited task record is created. The slice opens exactly its listed tasks under their normal prerequisites and does not authorize execution outside the selected launcher scope. No new substitute is registered or accepted; no runtime/product gate closes. Removed-product cleanup remains with CON.23/GOV.17/GOV.18, outside these ledger edits.

Validation: source inventory, task/obligation and frozen receipt review, plus explicit-root Plan consistency check. No build, runtime/provider test, artifact download or publication recheck. Untested coverage is every missing outcome and its real integration/acceptance cases. Ledger PR, independent exact-head approval and merge commits are preserved in the PR and claim audit trail.

## Post-adoption adjustment (2026-10-04)

This is a later adoption adjustment under DLV-22, introduced by the Design governance-chain planning repair [PR 210](https://github.com/ArcForges/ArcForges-Design/pull/210) (Design source head `68827a21b4525660d4f6d2b88c965433ca0dbef6`; the merge commit is retained in the pull request history, since embedding it would change the reviewed head). It does not reopen or replace this completed slice: the front matter, status, recorded date, claimant, epoch and every frozen classification above are unchanged.

| Task | Classification | Evidence and actual source binding | Remaining scope and blockers |
|---|---|---|---|
| GOV.09 | gap (classification unchanged) | Cloud main `1a001ea`: `Directory.Build.props` gives every project a `PrivateAssets=all` ArcForges.Build.Policy reference; `Directory.Packages.props` pins `1.0.0-ci.21.1`, which predates GOV.04's engine candidate; the solution is `Cloud.slnx`; dependency receipts live in `eng/policy/dependency-reviews/`; three projects carry locks; `@arcforges/proto 1.0.0-ci.287.1` is already locked. | The explicit scope and resource reconciliation this record required before implementation is now in the graph: solution entry, exact Build.Policy pin move to the published GOV.06 candidate with the three project locks it changes, dependency policy and a new immutable receipt, licence row, provenance, naming-scan wiring (`eng/policy/naming-candidate.json`, `tooling/project.ts`, `package.json`, `package-lock.json`) and CI wiring. GOV.06 is a new start prerequisite. The engine scope is the C# project graph; the `worker/` TypeScript tree gets no import policy from GOV.09, only the repository-wide naming scan and existing tooling. Cloud is AGPL, so no RP-03 exception. No security-scanner configuration change is authorized. |

## Production prerequisite adjustment, 2026-10-06

GOV.22 is not-started, not inherited: independently admitted exact Cloud devtool sharp security fix for the newly published high advisory. Existing slice approval applies; implementation/audit/CI/receipt evidence is required.
