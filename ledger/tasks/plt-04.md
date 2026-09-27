---
task: PLT.04
status: complete
recorded: 2026-09-28
claimant: w-20260927-platform
epoch: 1
---

# Numbered SQLite migration runner

## Outcome and obligation

WP-07.03 is implemented in ArcForges.Persistence.Sqlite: immutable numbered MigrationStep/Plan definitions, complete applied-history and checksum verification, schema-exclusive execution with one transaction per step, atomic history/sys_meta updates, resumable failure and explicit downgrade refusal. The public SqliteStore exposes its migration runner; product owners supply their own migration plans and keep their own stores.

Implementation is bundled in DesktopPlatform PR71 [PLT.01, PLT.02, PLT.04]. Earlier PR69 is closed as superseded; its authored commits and retained task/plt-04 worktree remain preserved. Final reviewed head `98d9c5ca96f400d45d1e9bc9a146781e64d00837`; independent mobile approval [5860838788](https://github.com/ArcForges/DesktopPlatform/pull/71#issuecomment-5860838788). Implementation merge `48a3ef4fcb5e356d4a50d0317f93a1cb1f314b6e`. Publication: normal main [run36359293616](https://github.com/ArcForges/DesktopPlatform/actions/runs/36359293616) succeeded at source `48a3ef4fcb5e356d4a50d0317f93a1cb1f314b6e`. `ArcForges.Persistence.Sqlite/1.0.0-ci.33.1` is among the eight successful pushes in publisher job `108734304036`. Original provider candidate `nuget-candidate-36359293616-1`, artifact `10944818667`, has archive digest `sha256:ca330cca4b1a395534d4609266e7aacf8af47501059adf4664431e39b7ddf225`. This is provider metadata; no artifact bytes were downloaded for revalidation. Primary clean fast-forward was confirmed; no post-merge runtime cycle ran.

## Evidence

- Actual existing Windows x64 SDK10.0.401 direct adapter Release build and offline SQLite suite: 47 passed, zero failed or skipped, including 16 migration cases. This ran through the workstation build slot; pinned SDK10.0.400 remains retained CI authority. The affected suite was rerun after the shared-core bounded origin-collection and retained-origin validation fixes and passed all 47 cases in 6.024s; the 16 migration cases remain unchanged.
- Every synthetic historical database version (1, 2, 3) is persisted and reopened, migrated to version 3, and compared against committed semantic golden rows including Unicode content and defaulted origin. Repeating the same plan creates no duplicate history or data.
- A failing second step rolls back its data/history while retaining successful prior steps; reopening resumes from the durable highest applied version. Unsupported downgrade, changed applied-step checksum and inconsistent schema metadata refuse without partial mutation.
- Owner-authored SQL cannot commit/rollback/savepoint or mutate protected mechanism history/metadata. Temporary trigger and temporary-table shadow vectors refuse and roll back the current step. Shared SQLite authorizer support is owned by PLT.01, with the one audited internal CA2100 sink authorized by Design PR91 and Plan PR62.
- Public SqliteStore migration API persists its version on reopen and does not append business journal entries. Definitions are copied and immutable; duplicate numbers/identities and invalid versions are refused.
- Six exact SQLite dependency nuspecs and full generated lock closure are bound in the immutable PLT.01/02/04 receipt; existing historical receipts are retained. Dependency admission, licence/runtime/provenance and reconciliation static checks passed before final integration. All 12 retained exact-head checks passed in [run36358863088](https://github.com/ArcForges/DesktopPlatform/actions/runs/36358863088). Publication: normal main [run36359293616](https://github.com/ArcForges/DesktopPlatform/actions/runs/36359293616) succeeded at source `48a3ef4fcb5e356d4a50d0317f93a1cb1f314b6e`. `ArcForges.Persistence.Sqlite/1.0.0-ci.33.1` is among the eight successful pushes in publisher job `108734304036`. Original provider candidate `nuget-candidate-36359293616-1`, artifact `10944818667`, has archive digest `sha256:ca330cca4b1a395534d4609266e7aacf8af47501059adf4664431e39b7ddf225`. This is provider metadata; no artifact bytes were downloaded for revalidation. Primary clean fast-forward was confirmed; no post-merge runtime cycle ran.

## Scope and limits

The committed fixture is mechanism-owned synthetic historical data, not a product schema or a substitute for future product compatibility acceptance. No physical-device, GUI, live-service, installed-consumer, native AOT executable execution, process-kill, or product snapshot/recovery run is claimed. The actual SQLite file tests demonstrate transaction failure rollback and reopen/resume; they do not claim power-loss hardware testing.

No completion prerequisite remains for PLT.04. PLT.02 separately retains its PLT.03 actual snapshot acceptance prerequisite; this ledger does not close it. Ledger review and merge identity are retained by this ledger PR and the task claim history.

