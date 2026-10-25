# MR-104: admission policy revision guard

Discovered during MR-101 continuation. Implementation: [ArcForges#46](https://github.com/ArcForges/ArcForges/pull/46), pushed head `9a776dd2fe4adac16db45897621c26dee7b74698`, based on `8146392993a5aec6215b0c38e7c27ef426a77b55`.

## Defect and scope

An admission pass could capture policy settings, then read tasks submitted after a newer policy committed. Attempt creation checked QUEUED state but not the policy revision that produced its decision. The obsolete pass could bypass a committed GLOBAL or SESSION DISABLED limit.

The immutable settings snapshot now carries the existing policy revision. The serialized attempt-creation transaction compares it with the current `policy_document.revision` before any attempt/task mutation. A mismatch leaves the task queued, refreshes policy outside the transaction and kicks another pass. No schema, contract or database migration is introduced. This restores Design 03 section 4 / R-EXE-013.

## Controlled reproduction and author checks

The real-node tests pause a pass after settings capture, commit DISABLED, submit two workloads, resume that pass and hold its successor. The obsolete pass must admit neither task. The following current pass must serialize their actual process windows. SQLite, command processing, RPC and native process containment are real; the internal hook controls only the interleaving.

- Before fix: both Windows cases fail, Expected QUEUED / Actual RUNNING. Failure-path release and drain leave no processes behind.
- After fix: both Windows cases pass (2 Linux-only cases skipped on Windows).
- Affected AdmissionEngineTests, PolicyRulesTests, QueuePolicyServiceTests and AdmissionPolicyRaceTests: 33 total, 31 passed, 2 Linux-only skips, 0 failed.
- Locked restore, Release build and changed-file format passed; build has 0 warnings and 0 errors.

Author logs: `C:\MyFile\Projects\dev\logs\resume-20261025-mr104\` (`before-tests.log`, `after-tests.log`, `affected-tests.log`, `after-build.log`, `format.log`). Initial analyzer errors in the local draft were corrected before commit and retained separately.

## Formal verification and merge

Merged as `f10248e4163999b867c0e33b6da5c66935045ce6` after both exact-head required statuses passed. Windows passed all 13 full-profile steps in 976 s; Linux passed all 16 in 1131 s. Both summaries report tree `291b24ba279c5854c4701ff154f42fd8bfa333a5` and base `8146392993a5aec6215b0c38e7c27ef426a77b55`. GitHub head, required statuses and the owner's skipped hosted jobs were checked immediately before merge. No competing build/test leg ran on either host.

Windows summary directory: `C:\MyFile\Projects\ArcForges\ArcForges\.git\arcforges-verify\logs\20261025-111849-9a776dd2fe4a-win`.
Linux summary directory: `/home/sammiller/arcforges/ArcForges/.git/arcforges-verify/logs/20261025-191842-9a776dd2fe4a-linux`.

The complete four-file implementation diff was self-reviewed under the owner's explicit instruction to use no other models or agents. Revision publication, serialized writes, outside-transaction refresh, failure cleanup and AOT constraints were checked. No blocking findings were identified.

The deterministic stale-policy bug is proven. Its contribution to every historical MR-101 scheduler timing/fairness observation remains unproven. MR-101 still needs main merged into its existing PR and both native legs at the resulting pushed head. No old status can satisfy that new commit. MR-16 remains blocked and later features remain unstarted.
