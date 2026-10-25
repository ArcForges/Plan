# MR-101 continuation evidence, 2026-10-25

Current pushed head: `364fd53ac9f66dc93426c6d531154895948f33c6`, existing [ArcForges#45](https://github.com/ArcForges/ArcForges/pull/45). Merge is pending. Linux formal verification passed at this head; Windows formal verification has not started because the loaded author validation remains interrupted.

The owner instructed this Codex session to analyze, implement and review directly, without other models or agents. That session instruction supersedes the delegation and independent Opus review requirement for this continuation. Existing review records remain historical evidence; the new delta is self-reviewed and attributed to OpenAI Codex.

## Recovery and preserved evidence

The new Windows MCP and the Linux MCP both connected. The old `resume-mr101-diagnose.ps1` had actually run and exited 0, but its log ends with the former MCP outage and no `MR101-DIAGNOSIS.md` was written. Its build/test lanes had drained; live process inspection found no leftover test or build work before diagnosis. No old diagnostic model session was resumed.

The following evidence was re-read at `c60c351`, and retained with that exact revision:

| Evidence | Result |
|---|---|
| Locked restore | exit 0 |
| Release build | 0 warnings, 0 errors |
| Changed-file format | exit 0 |
| 10 independent LaunchFaultTests class runs | 10/10 tests passed in every run; no skips |
| Debugger-held test in every independent run | task ended before step run-down; held-step cancel 159–249 ms |
| Existing Linux formal leg | all 16 steps passed in 1115 s; summary SHA and GitHub status confirmed |

Original Windows logs: `C:\MyFile\Projects\dev\logs\mr101-c60-*`.
Linux summary: `/home/sammiller/arcforges/ArcForges/.git/arcforges-verify/logs/20261025-125417-c60c351e2f29-linux/summary.json`.

The original loaded batch is **not a complete successful validation**. Although all ten target class logs passed (run 5 was also checked), its Node.Core lane failed the 30 s scheduler assertion at 37.1769528 s and ceased, leaving only partial three-lane coverage. The original CPU sampler was invalid.

The second loaded batch executed **no target test**. Its AOT lane rejected component `t`. PowerShell variables are case-insensitive: assigning the split array back to typed `$Components` through `$components` converted it to a string, and indexing returned one character. The continuation uses a separately named, explicitly typed `[string[]]$componentNames`; every lane stops on its first failure.

## Scheduler diagnosis

Temporary instrumentation captured submit, admission, root-start, TestLoad start/end markers and the final task record. It was removed byte-for-byte before the final code was built or committed. No scheduler behavior or 30 s assertion changed.

At `c60c351`: 20 single-test runs alone and 20 beside looping Node.Core ci, ClosedLoop ci and AOT publish all passed. Both test lanes completed two passing ci runs.

| Segment | Alone (ms) | Loaded (ms) |
|---|---:|---:|
| Submitted task record to admission | 19.9–25.4 | 26.4–71.4 |
| Admission to recorded root start | 148.5–166.0 | 185.3–712.5 |
| Recorded root start to workload marker | 33.9–41.4 | 41.2–13454.3 |
| Workload | 104–119 | 104–1639 |
| Workload end marker to final record | 81.6–101.3 | 107.4–12984.1 |

The slowest loaded sample took 27.3219 s; its admission took 36.85 ms. The delay was after admission, including 13.45 s before the workload marker and 12.98 s after its end marker. These samples do not show an infeasible task blocking feasible admission.

The task has no launch or end steps and exits normally with code 0. It does not enter MR-101's changed step wait; its root-handle wait is unchanged. The original failing sample's timeline was not retained, so its exact cause remains **unproven**. The new evidence supports execution/run-down delay under extra host load, not a claim that the original timeout is fixed. MR-102 remains the separate forced-root-stop repair, with the normal-exit guard intact. The scheduler timing observation remains watched.

Logs and metric extraction: `C:\MyFile\Projects\dev\logs\resume-20261025-mr101\scheduler-*`, `metrics.py`, `scheduler-metrics.json`.

## Fresh Native AOT load exposed cleanup synchronization

Before the new delta, a fresh worktree ensured a real host ILC compile rather than only incremental publishes. The first target class run at `c60c351` failed fixture cleanup: the 30 s launch-step theory cancelled successfully in 339 ms, but the terminated step still held its working directory beyond the fixture's retries. Node.Core ci and ClosedLoop ci passed; the AOT host publish passed in 79.1 s. The target stopped at this first failure and all three lanes drained.

The test-only `364fd53` delta:

- captures the Windows step by PID and creation time before cancellation, using its ready marker and an identity-checked query/synchronize handle;
- retains the task state, result, no-root, no-command and 5 s cancellation assertions;
- waits for that exact process object to become signaled after those assertions and before fixture cleanup;
- verifies deterministically that the debugger-held cleanup wait remains pending before release and completes only after run-down;
- leaves the shared fixture's leftover checks and all product code unchanged.

The targeted class at the final delta passed: 10 tests, 0 failed, 0 skipped. Release build and changed-file format passed. An initial compile issue and a wrong marker precondition in the local draft were diagnosed and corrected before commit; their failure logs are retained.

## Final-head gate

The final head passed its own 10 independent class runs. Linux formal verification passed all 16 steps in 1124 s at tree `e11a871c5b6e986f74ea3152c473f2374b799ec9`, base `8146392`; the GitHub status was checked. The earlier revision's statuses were not copied.

Clean final-head four-stream load stopped after a Node.Core scheduler overrun of 36.1068481 s. A subsequent temporarily instrumented whole-ci diagnostic passed ten target class runs and its load lanes, then restored the source; it remains diagnostic evidence. To match the formal leg's three streams, integrated validation runs the target class inside Node.Core ci beside ClosedLoop ci and AOT publish, and emits per-test CTRF JSON. Runs 1–6 passed all 283 tests (LaunchFault 10/10 each). Run 7 failed `TwoSessionsShareAdmissionsEquallyOnWindows` (64.2% running-time share) and `ParallelismDisabledPerScopeRunsOneAtATimeOnWindows` (SESSION marker overlap), while LaunchFault passed 10/10. The first-failure guard stopped and drained all lanes. This is not a complete successful loaded validation; Windows formal verification never started.

Investigation established a separate stale-policy admission bug through controlled interleavings: both GLOBAL and SESSION DISABLED limits committed after a pass captured settings can be bypassed when that pass later reads new queued work. Both cases fail on main (expected QUEUED, actual RUNNING), then pass with a transaction-time revision guard. This is prerequisite **MR-104**, [ArcForges#46](https://github.com/ArcForges/ArcForges/pull/46), at `9a776dd2fe4adac16db45897621c26dee7b74698`. It merged as `f10248e4163999b867c0e33b6da5c66935045ce6` after full Windows (13 steps/976 s) and Linux (16 steps/1131 s) verification; see the [MR-104 record](2026-10-25-mr104-validation.md). Its contribution to every historical scheduler observation remains unproven. After its Plan record merges, MR-101 must merge main and verify its new pushed head on both hosts; the current Linux status is not reusable for a new head.

Windows runner: `resume-20261025-mr101/final-364fd53.ps1`, with first-failure guards. It performs author checks, drains its load lanes, checks the host is idle, then invokes `python eng/verify.py run-and-report`.
Linux runner: `/home/sammiller/arcforges/logs/resume-mr101-364fd53-verify.sh`, fetched from GitHub at the final head.

No real Windows Credential Manager cleanup, orphan credential-file operation or real-store stress was performed. MR-16 stays blocked, and AF-REC-01 and later features remain unstarted.
