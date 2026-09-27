---
task: ADOPT.07.device-bridge
status: complete
recorded: 2026-09-27
claimant: w-20260927-cloud-lane
epoch: 1
---

# Adopt Cloud: Application presence and tool bridge

## Inputs and source comparison

Cloud integration owner w-20260927-cloud-lane, role epoch 2, reviewed the [frozen Cloud baseline](../adoption/baseline.md#cloud), source `60c5c4288b126c81a09fa5d1944671e9acb87495`, generated task outcomes/obligation parts, and the corresponding WP requirements/tests/gates. No open Cloud PR existed at the freeze.

No Presence or ToolBridge implementation, target queue, attempt-result store or approval authority exists.

The complete tracked source inventory is summarized in [Cloud repository facts](../adoption/Cloud.md). Bootstrap build/dependency/provenance checks and deployment receipts remain valid for their original scope, but do not satisfy these missing outcomes. Each row retains the full named task outcome as remaining work, including its mapped tests and completion gates.

## Classifications

| Task | Classification | Bound write scope | Remaining scope | Evidence / conflicts / blockers |
|---|---|---|---|---|
| DEV.01 | gap | Planned additions: Cloud:src/ArcForges.Cloud/Presence/** | ApplicationService.List/Heartbeat/Disconnect implemented with DO projection of D1 installation authority; separate app rows per device; 30s expiry/10s renewal, restarted epoch, app-offline-without-device-wide-false-availability proven. | Frozen source lacks this outcome. Normal graph prerequisites apply; no implementation conflict found. |
| DEV.02 | gap | Planned additions: Cloud:src/ArcForges.Cloud/ToolBridge/** | ToolRequest freezes product/device/installation and current instance epoch; commands/receipts remain in D1. Another application cannot claim; duplicate/lost ack/expiry and per-owner budget proven. | Frozen source lacks this outcome. Normal graph prerequisites apply; no implementation conflict found. |
| DEV.04 | gap | Planned additions: Cloud:src/ArcForges.Cloud/ToolBridge/** | Bridge request/result persisted in D1 using full ApplicationTarget and (toolRequestId,attemptId,commandId) plus result hash; multiple tool requests per attempt both persist; identical replay returns its own receipt; changed result hash refuses; stale epoch and cross-application delivery rejected. | Frozen source lacks this outcome. Normal graph prerequisites apply; no implementation conflict found. |
| DEV.06 | gap | Planned additions: Cloud:src/ArcForges.Cloud/ToolBridge/** | One-target approvals, sensitive local-presence requirements and ordinary steering bounds preserved; mobile biometric cannot substitute for target presence; stale approval fails. | Frozen source lacks this outcome. Normal graph prerequisites apply; no implementation conflict found. |
| DEV.07 | gap | Planned additions: Cloud:src/ArcForges.Cloud/ToolBridge/** | Explicit offline queue expiry/reconciliation; changing the selected app cannot retarget queued work. Disconnect/revoke/reinstall proven with no silent alternate product/device selection. | Frozen source lacks this outcome. Normal graph prerequisites apply; no implementation conflict found. |
| DEV.08 | gap | Planned additions: Cloud:src/ArcForges.Cloud/ToolBridge/** | Cloud-only steps may run without a desktop; every device step in one execution remains in the frozen product scope. Own-app multi-tool workflow passes; cross-product capability absent/future. | Frozen source lacks this outcome. Normal graph prerequisites apply; no implementation conflict found. |
| DEV.09 | gap | Planned additions: Cloud:artifacts/evidence/** | WP26 built/packed once from a clean environment across both repositories; all applicable UX acceptance groups recorded; failure/recovery and the real boundaries above proven; no later-provider fixture closes a real WP26 gate. | Frozen source lacks this outcome. Normal graph prerequisites apply; no implementation conflict found. |
| DEV.12 | gap | No source writes declared; integrate real prerequisite outputs and record evidence under the existing task procedure. | BI-03: the Cloud attempt row and the desktop command_log genuinely agree under concurrent/duplicate/lost-ack delivery, not just each side's own unit tests | Frozen source lacks this outcome. Normal graph prerequisites apply; no implementation conflict found. |
| DEV.13 | gap | No source writes declared; integrate real prerequisite outputs and record evidence under the existing task procedure. | an actual Cloud-planned Agent Task step (not a scripted ToolRequest) reaches a real desktop, is locally re-authorized, executed and its result accepted -- the real integration producer-artifacts.md names as closing WP26's remaining fixture-content gap | Frozen source lacks this outcome. Normal graph prerequisites apply; no implementation conflict found. |

## Scope binding and validation

Existing source is `src/ArcForges.Cloud` (assembly/namespace ArcForges.Cloud), with tests under `tests/ArcForges.Cloud.Tests`, worker code under `worker`, tooling under `tooling`, and policy/provenance under `eng`. Logical `src/Cloud/ArcForges.Cloud.Host` and `src/ArcForges.Cloud.Host` bind to the existing host, preserving its identity. Module/Storage/PublicApi/Jobs directories in the rows are absent planned additions beneath Cloud, not permissions to rename the bootstrap or copy another repository. New projects, dependency locks, root registration and workflow changes require explicit scope/resource reconciliation before implementation; this ledger itself grants no additional writes. Empty-write integration tasks remain evidence joins and cannot implement missing producers.

No task is inherited; no inherited task record is created. The slice opens exactly its listed tasks under their normal prerequisites and does not authorize execution outside the selected launcher scope. No new substitute is registered or accepted; no runtime/product gate closes. Removed-product cleanup remains with CON.23/GOV.17/GOV.18, outside these ledger edits.

Validation: source inventory, task/obligation and frozen receipt review, plus explicit-root Plan consistency check. No build, runtime/provider test, artifact download or publication recheck. Untested coverage is every missing outcome and its real integration/acceptance cases. Ledger PR, independent exact-head approval and merge commits are preserved in the PR and claim audit trail.
