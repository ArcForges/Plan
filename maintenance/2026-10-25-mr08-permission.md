# MR-08: the delivered adopted-task permission gate

Disposition: resolved in the delivered local permission gate; the future remote transport's integration obligation is assigned to
AF-CLD-05. That task stays planned. No remote entry point, LAN or cloud implementation is introduced.

## Current evidence

ArcForges main `5eaee92a4a964469bad41dad28dad9787b7552cf` was freshly fetched. In
`TaskServiceHandler.TaskGate`, cancelling an ADOPTED task selects `PermissionMatrix.ProcessTerminate` before the ordinary task-owner
rule. This branch was introduced by `cd0bb00a` (AF-SEC-01), an ancestor of current main, and was delivered by
[ArcForges#31](https://github.com/ArcForges/ArcForges/pull/31), merge `2180053`, also confirmed as an ancestor.

`PermissionMatrix` assigns `process.terminate` no remote command kind and returns DENY for REMOTE. A REMOTE override can only deny.
`ApiCommands.GateAsync` admits an approval only for an APPROVAL verdict; an approval cannot bypass DENY. The gate runs before the
idempotent cancellation and its post-commit stop. Terminal or missing tasks make no change; `EnsureStillSettled` detects a revived
task and rechecks the gate. A recorded-command replay may only replay, and does not issue another stop.

`GateAndReplayTests.AnApprovedCancelOfAnAdoptedTaskIsAuditedAsProcessTerminate` covers the adopted-task branch, approval and audit
using a recorded adoption whose container is already gone. `PermissionTests.TheDefaultMatrixDecidesPerOrigin` independently
asserts the REMOTE deny for `process.terminate`; the override test rejects an allow override. These existing tests were included in
the successful native Windows and Linux Node.Core CI lanes at reviewed head `8fe744ffee80f24b59f835af60ba43e4a5163391`
([ArcForges#49](https://github.com/ArcForges/ArcForges/pull/49), merged as the current main). Their code and gate are unchanged here.
This is retained existing coverage, not a new runtime verification or a successful live adoption/remote cancellation test.

## Remaining future obligation

The delivered connection caller comes from a local client session; the other caller construction restores an approval's requester.
There is no delivered remote transport before AF-CLD-04/05. AF-CLD-05 already owns REMOTE enforcement, but its acceptance lacked this
case. Its record now requires a signed REMOTE cancel_task against a nonterminal ADOPTED task to be denied as process.terminate
before any stop, with the adopted process still running and a denied audit record. Medium risk, step-up and approval must not bypass
that deny. This must be tested through the real remote-to-node path when the task is implemented; it is not claimed as proven now.

The original suspicion that ordinary remote task cancellation could directly bypass the delivered ADOPTED gate is resolved by the
existing branch. Future transport enforcement remains an explicit planned acceptance requirement, without activating the task.
