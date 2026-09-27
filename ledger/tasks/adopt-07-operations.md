---
task: ADOPT.07.operations
status: complete
recorded: 2026-09-27
claimant: w-20260927-cloud-lane
epoch: 1
---

# Adopt Cloud: Operations, support and trust and safety

## Inputs and source comparison

Cloud integration owner w-20260927-cloud-lane, role epoch 2, reviewed the [frozen Cloud baseline](../adoption/baseline.md#cloud), source `60c5c4288b126c81a09fa5d1944671e9acb87495`, generated task outcomes/obligation parts, and the corresponding WP requirements/tests/gates. No open Cloud PR existed at the freeze.

No monitoring/runbook suite, Support/TrustSafety module or Notification mail/push adapters exist. Deployment instructions and health are not operational acceptance.

The complete tracked source inventory is summarized in [Cloud repository facts](../adoption/Cloud.md). Bootstrap build/dependency/provenance checks and deployment receipts remain valid for their original scope, but do not satisfy these missing outcomes. Each row retains the full named task outcome as remaining work, including its mapped tests and completion gates.

## Classifications

| Task | Classification | Bound write scope | Remaining scope | Evidence / conflicts / blockers |
|---|---|---|---|---|
| OPS.01 | gap | Planned additions: Cloud:deploy/monitoring/** | Service-level indicators measure user-visible success per capability group with realtime/managed-AI computed independently, error budgets are visible, and every deployed alert routes correctly and names an existing runbook. | Frozen source lacks this outcome. Normal graph prerequisites apply; no implementation conflict found. |
| OPS.02 | gap | Planned additions: Cloud:src/Cloud/ArcForges.Cloud.Modules.Support/**/Incidents/** | A shared four-severity ladder drives incident state tracked independently of production, a possible personal-data breach classifies automatically at the highest severity with the statutory notification clock as a hard deadline, and post-incident review produces runbook updates. | Frozen source lacks this outcome. Normal graph prerequisites apply; no implementation conflict found. |
| OPS.03 | gap | Planned additions: Cloud:docs/runbooks/** | Every required runbook is written with preconditions, decision points, exact steps, verification and rollback, and every runbook for an implemented owner carries at least one dated rehearsal record. | Frozen source lacks this outcome. Normal graph prerequisites apply; no implementation conflict found. |
| OPS.06 | gap | Planned additions: Cloud:src/Cloud/ArcForges.Cloud.Modules.Support/**/BreakGlass/** | A distinct, alarmed emergency-access path requires justification, expires automatically, alerts immediately, requires mandatory post-hoc review, and is visible to the affected account owner. | Frozen source lacks this outcome. Normal graph prerequisites apply; no implementation conflict found. |
| OPS.07 | gap | Planned additions: Cloud:src/Cloud/ArcForges.Cloud.Modules.Support/**/Cases/** | In-product problem reporting produces a support reference without attaching user data by default, support cases link to diagnostic references rather than content, and the case lifecycle carries defined response expectations. | Frozen source lacks this outcome. Normal graph prerequisites apply; no implementation conflict found. |
| OPS.08 | gap | Planned additions: Cloud:src/Cloud/ArcForges.Cloud.Modules.TrustSafety/** | Community report intake drives a proportionate enforcement ladder with every action recorded and communicated, account enforcement states integrate with the account model, and appeals have a defined path and response expectation. | Frozen source lacks this outcome. Normal graph prerequisites apply; no implementation conflict found. |
| OPS.09 | gap | Planned additions: Cloud:src/Cloud/ArcForges.Cloud.Modules.Notification/**; Cloud:src/Cloud/ArcForges.Cloud.Modules.TrustSafety/**/Advisories/** | Transactional/broadcast email use the real WP-22 Postmark/SES adapters with separated streams; outage and reconciliation drills are rehearsed under a prepared secondary path; and the private security-advisory intake-through-publication process is complete with in-product containment/revocation attention. | Frozen source lacks this outcome. Normal graph prerequisites apply; no implementation conflict found. |
| OPS.10 | gap | Planned additions: Cloud:src/Cloud/ArcForges.Cloud.Modules.Notification/**/Push/** | Notification.IPushSender sends through a typed FCM HTTP v1 credential adapter with a unique delivery-intent outbox, generation/revocation checks and the exact push.v1 profile, working against an actual isolated Firebase project with bounded, fenced recovery. | Frozen source lacks this outcome. Normal graph prerequisites apply; no implementation conflict found. |
| OPS.12 | gap | Planned additions: Cloud:eng/provenance/records/** | The package-level owned-artifact/real-integration receipt is recorded confirming actual role/redaction/status/support-case behavior and actionable CF/R2 failure diagnostics, with no second Node/operations business host. | Frozen source lacks this outcome. Normal graph prerequisites apply; no implementation conflict found. |

## Scope binding and validation

Existing source is `src/ArcForges.Cloud` (assembly/namespace ArcForges.Cloud), with tests under `tests/ArcForges.Cloud.Tests`, worker code under `worker`, tooling under `tooling`, and policy/provenance under `eng`. Logical `src/Cloud/ArcForges.Cloud.Host` and `src/ArcForges.Cloud.Host` bind to the existing host, preserving its identity. Module/Storage/PublicApi/Jobs directories in the rows are absent planned additions beneath Cloud, not permissions to rename the bootstrap or copy another repository. New projects, dependency locks, root registration and workflow changes require explicit scope/resource reconciliation before implementation; this ledger itself grants no additional writes. Empty-write integration tasks remain evidence joins and cannot implement missing producers.

No task is inherited; no inherited task record is created. The slice opens exactly its listed tasks under their normal prerequisites and does not authorize execution outside the selected launcher scope. No new substitute is registered or accepted; no runtime/product gate closes. Removed-product cleanup remains with CON.23/GOV.17/GOV.18, outside these ledger edits.

Validation: source inventory, task/obligation and frozen receipt review, plus explicit-root Plan consistency check. No build, runtime/provider test, artifact download or publication recheck. Untested coverage is every missing outcome and its real integration/acceptance cases. Ledger PR, independent exact-head approval and merge commits are preserved in the PR and claim audit trail.
