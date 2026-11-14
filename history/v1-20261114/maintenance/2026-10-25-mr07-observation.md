# MR-07: unresolved StopNode exit 75

Date: 2026-10-25. Disposition: **deferred validation / unresolved observation**, AR-20. No runtime repair is claimed.

## Historical evidence

[ArcForges#12](https://github.com/ArcForges/ArcForges/pull/12) and
[its review record](https://github.com/ArcForges/ArcForges/pull/12#issuecomment-6223420516) retain the original
Windows supervisor-test failure: node stop exited 75 with "No node listens on the pipe".
The review records 528 targeted stops and more than 20 concurrent iterations without another occurrence.
Those historical Windows/WSL experiments were not resumed and are not counted as current native-host validation.

The wait-ready defect found during that investigation returned before READY and explained INTERNAL, not the pipe-missing
exit 75. MR-06's typed startup-state refusal likewise does not establish a cause or repair for MR-07.

## Current source and retained logs

Current source main 5eaee92 was fetched and inspected. TestNode.StopNodeAsync still executes node stop --verbose and
fails with the descriptor's process/liveness, supervisor last 60 lines and node last 40 lines.
Cli.MutateAsync preserves transport retry traces and the command ID. NodeConnector maps Windows error 2 to
EndpointFailure.NotRunning with the reported message. The two original supervisor scenarios and their assertions remain.

A read-only audit of retained Windows formal logs completed at 2026-10-25T16:01:48Z:
- 76 run directories inventoried; 53 eligible Windows summaries supplied 197 relevant log files.
- File names: win-ci.log, win-closed-loop-native.log, win-exclusive.log, win-exclusive-native.log.
- Summary range: 2026-10-22T09:12:32Z through 2026-10-25T15:47:17Z.
- 47 successful summaries; 6 failed/incomplete summaries, which are not counted as passes.
- No read errors, no exact pipe-missing message and no failed outcome for either named original supervisor test.
- This is coverage of existing log files, not 53 fresh validations, 197 stop operations or proof that every failed/incomplete run
  reached the original scenarios. The old original raw capture was not found in the targeted local log-name inventory.

Audit script/output remain at C:/MyFile/Projects/dev/logs/resume-20261025-mr07/ (audit.py, audit.json, audit.out).
Audit JSON SHA-256: 8b6a6aa57aa903da2334b5fc40be62deabdf7c02e04bfeb6ba03d2313d10cfba.

The latest complete runtime profile remains exact head 8fe744ffee80f24b59f835af60ba43e4a5163391, merged as
5eaee92a4a964469bad41dad28dad9787b7552cf: Windows 13 steps/963 s, Linux 16 steps/1129 s.
That is revision-specific evidence already recorded for MR-06, not a new MR-07 runtime run or a root-cause proof.

## Remaining obligation

AR-20 retains a native Windows capture/reproduction procedure under AF-NODE-01 and a closure rule requiring a proven
cause and discriminating regression/repair with required final-head checks where applicable. Non-recurrence alone cannot
close it. The venue exists; no human provisioning or task block is created. Existing diagnostic assertions, retries and
timeouts stay intact, and no new stress batch or runtime code change was made for this observation review.

Later feature tasks stay unstarted. MR-16 remains blocked with its recovery proposal; real credential-store cleanup/stress,
LAN/cloud MCP and database migrations remain outside this work.
