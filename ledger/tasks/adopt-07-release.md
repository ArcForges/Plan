---
task: ADOPT.07.release
status: complete
recorded: 2026-09-27
claimant: w-20260927-cloud-lane
epoch: 1
---

# Adopt Cloud: Release readiness and family release

## Inputs and source comparison

Cloud integration owner w-20260927-cloud-lane, role epoch 2, reviewed the [frozen Cloud baseline](../adoption/baseline.md#cloud), source `60c5c4288b126c81a09fa5d1944671e9acb87495`, generated task outcomes/obligation parts, and the corresponding WP requirements/tests/gates. No open Cloud PR existed at the freeze.

The bootstrap candidate deploys successfully, but production capacity, migration, backup, self-host, commercial activation and disaster/on-call evidence do not exist.

The complete tracked source inventory is summarized in [Cloud repository facts](../adoption/Cloud.md). Bootstrap build/dependency/provenance checks and deployment receipts remain valid for their original scope, but do not satisfy these missing outcomes. Each row retains the full named task outcome as remaining work, including its mapped tests and completion gates.

## Classifications

| Task | Classification | Bound write scope | Remaining scope | Evidence / conflicts / blockers |
|---|---|---|---|---|
| REL.06 | gap | Planned additions: Cloud:eng/release/**; Cloud:deploy/production/**; Design:docs/assurance/wp50-04-cloud-*.md | Cloud is deployed from a promoted, never-rebuilt artifact with rehearsed migration/rollback, proven backup/restore, a live status page with emergency alternate URL, and the approved/measured capacity envelope plus independently operated self-host deployment evidence required for L-16/PG-25/PG-26, on a genuine Native AOT publish. | Frozen source lacks this outcome. Normal graph prerequisites apply; no implementation conflict found. |
| REL.08 | gap | Planned additions: Cloud:eng/release/commercial/**; Design:docs/assurance/wp50-05-commercial-*.md | Account portal and checkout run in production; official pricing is published only after entitlement, refunds, webhook idempotency and a RECEIVED payout are all proven - until then the public statement is 'technical integration complete'; the regional route remains disabled unless its own gates are met. | Frozen source lacks this outcome. Normal graph prerequisites apply; no implementation conflict found. |
| REL.09 | gap | Planned additions: Cloud:eng/release/game-day/**; Design:docs/assurance/wp50-04-gameday-*.md, wp50-07-operational-readiness-*.md | A game-day exercise across the full severity ladder runs against the real deployed production topology with recorded evidence for every go-live gate; every alert maps to a rehearsed runbook, on-call is in place, and support/enforcement/appeal paths are operable. | Frozen source lacks this outcome. Normal graph prerequisites apply; no implementation conflict found. |

## Scope binding and validation

Existing source is `src/ArcForges.Cloud` (assembly/namespace ArcForges.Cloud), with tests under `tests/ArcForges.Cloud.Tests`, worker code under `worker`, tooling under `tooling`, and policy/provenance under `eng`. Logical `src/Cloud/ArcForges.Cloud.Host` and `src/ArcForges.Cloud.Host` bind to the existing host, preserving its identity. Module/Storage/PublicApi/Jobs directories in the rows are absent planned additions beneath Cloud, not permissions to rename the bootstrap or copy another repository. New projects, dependency locks, root registration and workflow changes require explicit scope/resource reconciliation before implementation; this ledger itself grants no additional writes. Empty-write integration tasks remain evidence joins and cannot implement missing producers.

No task is inherited; no inherited task record is created. The slice opens exactly its listed tasks under their normal prerequisites and does not authorize execution outside the selected launcher scope. No new substitute is registered or accepted; no runtime/product gate closes. Removed-product cleanup remains with CON.23/GOV.17/GOV.18, outside these ledger edits.

Validation: source inventory, task/obligation and frozen receipt review, plus explicit-root Plan consistency check. No build, runtime/provider test, artifact download or publication recheck. Untested coverage is every missing outcome and its real integration/acceptance cases. Ledger PR, independent exact-head approval and merge commits are preserved in the PR and claim audit trail.
