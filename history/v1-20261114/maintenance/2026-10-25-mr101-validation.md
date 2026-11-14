# MR-101 continuation evidence, 2026-10-25

Reviewed and merged PR head: `8c1c06c081221e36723fd2cc16d4bfec4098b8a5`, existing [ArcForges#45](https://github.com/ArcForges/ArcForges/pull/45), based on MR-104/MR-90 main `266bfa6` plus the test readiness delta below. Merged as `866b0b7f3695cdbca8eebfd5ebe20566805d4330` after complete author validation and both exact-head formal legs passed: Windows 13 steps/932 s, Linux 16 steps/1130 s. Both summaries and the live GitHub merge gate were checked before merge. The prior 54ac6e0 Linux leg completed and remains old-head evidence. Earlier checkpoint evidence remains tied to its own revision and cannot satisfy the new head.

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

## The 364fd53 checkpoint

The 364fd53 checkpoint passed its own 10 independent class runs. Linux formal verification passed all 16 steps in 1124 s at tree `e11a871c5b6e986f74ea3152c473f2374b799ec9`, base `8146392`; the GitHub status was checked. The earlier revision's statuses were not copied.

Clean four-stream load at 364fd53 stopped after a Node.Core scheduler overrun of 36.1068481 s. A subsequent temporarily instrumented whole-ci diagnostic passed ten target class runs and its load lanes, then restored the source; it remains diagnostic evidence. To match the formal leg's three streams, integrated validation runs the target class inside Node.Core ci beside ClosedLoop ci and AOT publish, and emits per-test CTRF JSON. Runs 1–6 passed all 283 tests (LaunchFault 10/10 each). Run 7 failed `TwoSessionsShareAdmissionsEquallyOnWindows` (64.2% running-time share) and `ParallelismDisabledPerScopeRunsOneAtATimeOnWindows` (SESSION marker overlap), while LaunchFault passed 10/10. The first-failure guard stopped and drained all lanes. This is not a complete successful loaded validation; Windows formal verification never started.

Investigation established a separate stale-policy admission bug through controlled interleavings: both GLOBAL and SESSION DISABLED limits committed after a pass captured settings can be bypassed when that pass later reads new queued work. Both cases fail on main (expected QUEUED, actual RUNNING), then pass with a transaction-time revision guard. This is prerequisite **MR-104**, [ArcForges#46](https://github.com/ArcForges/ArcForges/pull/46), at `9a776dd2fe4adac16db45897621c26dee7b74698`. It merged as `f10248e4163999b867c0e33b6da5c66935045ce6` after full Windows (13 steps/976 s) and Linux (16 steps/1131 s) verification; see the [MR-104 record](2026-10-25-mr104-validation.md). Its contribution to every historical scheduler observation remains unproven. After its Plan record merges, MR-101 must merge main and verify its new pushed head on both hosts; the current Linux status is not reusable for a new head.

Windows runner: `resume-20261025-mr101/final-364fd53.ps1`, with first-failure guards. It performs author checks, drains its load lanes, checks the host is idle, then invokes `python eng/verify.py run-and-report`.
Linux runner: `/home/sammiller/arcforges/logs/resume-mr101-364fd53-verify.sh`, fetched from GitHub at the final head.

No real Windows Credential Manager cleanup, orphan credential-file operation or real-store stress was performed. MR-16 stays blocked, and AF-REC-01 and later features remain unstarted.


## Fresh head after MR-104

The existing branch merged main without conflicts and pushed `c78bdd95621c3f33494f6dcfe6807929b0ba83ea`. The delta from `364fd53` is the already reviewed MR-104 prerequisite; the PR diff against current main remains AttemptRunner.cs and LaunchFaultTests.cs. Existing untracked PR-BODY.md was preserved.

At this head, Windows locked restore, changed-file format and the Release solution build passed (0 warnings, 0 errors). Two author-script attempts selected zero tests: the native runner's `-class` syntax was used with MTP, first with a short class name and then a full name. Both stopped with minimum-expected-tests exit 5 before load or formal verification. Local MTP help identified `--filter-class`; test discovery then confirmed exactly 10 LaunchFault tests. The corrected script reuses the unchanged head's successful build and preserves both failed script logs. No test assertion or product code changed.

Windows orchestrator for the c78bdd9 checkpoint: `C:\MyFile\Projects\dev\logs\resume-20261025-mr101\integrated-c78bdd9-v3.ps1`, logs `final-c78bdd9-v3`. It requires 10 standalone class runs, affected classes and Platform.Windows ci, then 10 complete Node.Core ci runs with per-test CTRF evidence beside ClosedLoop ci and fresh-worktree AOT publishing. All lanes must drain successfully before the formal Windows leg starts. Linux formal runner: `/home/sammiller/arcforges/logs/resume-mr101-c78bdd9-verify.log`. Results and the subsequent interruption are recorded below.

At c78bdd9, the corrected Windows runner completed all 10 standalone classes (10 passed, 0 skipped each) and EscapedTermination/TaskControl (17 total, 16 passed, 1 Linux-only skip). Platform.Windows ci then stopped: 116 total, 114 passed, 1 failed, 1 documented adoption skip. The failure is existing MR-90, `ResourceSamplerTests.TheTableMatchesToolhelpAndTheProcessApi`: 8 Toolhelp entries absent from an earlier process-table snapshot exceeded its fixed tolerance of 5. No loaded batch or formal Windows leg started. The exact birth/death timeline of those eight entries is not available, so the live failure alone does not prove a sampler omission or a particular lifetime interleaving.

MR-101 is parked while MR-90 is repaired separately as a verification prerequisite. The existing c78bdd9 Linux leg is allowed to drain without a competing test/build; its result will remain evidence only for that commit. MR-90's controlled reproduction creates 8 workloads strictly after the table read and reproduces the old false failure. The repair compares exact process identities captured before the table and still running afterwards with zero omission tolerance. After MR-90 merges and its Plan record is complete, MR-101 must take main and receive fresh required host checks again.

The c78bdd9 Linux formal leg subsequently passed all 16 full-profile steps in 1134 s, tree `8fdfbc573c8b8f8bf5a5ee93aea43c0992b65e18`, base `f10248e4163999b867c0e33b6da5c66935045ce6`. Its summary was checked and the host reported success; the user manager remained running. Logs: `/home/sammiller/arcforges/ArcForges/.git/arcforges-verify/logs/20261025-194208-c78bdd95621c-linux`. No competing Linux build/test ran. This remains c78bdd9-only evidence and will not be reused after the MR-90 main merge.

MR-90 subsequently merged as `266bfa60229fc191e85966ee406c84ce3a4ead55` after both final-head formal legs passed; see the [MR-90 record](2026-10-25-mr90-validation.md). The next MR-101 action, after the Plan record merges, is to take live main and verify its resulting new pushed head. No extra MR-101 source change was made while its prerequisite was being repaired.

## Fresh head after MR-90

After MR-90's Plan#50 record merged (`83df1cf`), the existing branch took live main `266bfa60229fc191e85966ee406c84ce3a4ead55` without conflicts and pushed `54ac6e01e98fcae216f425d77dd59e27b475d380`. Its delta from c78bdd9 is the reviewed MR-90 test repair; the PR diff against main remains exactly AttemptRunner.cs and LaunchFaultTests.cs. Untracked PR-BODY.md remains preserved.

New-head Windows locked restore, changed-file format and Release solution build passed (0 warnings/errors, build 23.61 s). Runner `C:\MyFile\Projects\dev\logs\resume-20261025-mr101\integrated-54ac6e0.ps1`, logs `final-54ac6e0`, uses the confirmed MTP full-class filters, protects existing logs, checks the source/head before and after author validation, and retains typed AOT component arrays. It requires ten standalone target classes, affected classes and Platform.Windows ci, then ten full Node.Core ci runs containing the target class (minimum 287 tests) beside ClosedLoop ci and fresh-worktree AOT publish. First failure stops the batch; every lane must drain before the formal Windows leg starts.

Linux formal runner: `/home/sammiller/arcforges/logs/resume-mr101-54ac6e0-verify.log`, fetched from GitHub at 54ac6e0. Linux formal verification is in progress. Formal Windows verification has not started and its status is not yet reported at this head. None of the c78bdd9 or earlier results is reused for this commit.

## Recovered-launch test readiness, 8c1c06c

At 54ac6e0, standalone class run 1 passed; run 2 stopped with 9 passed/1 failed/0 skipped before load or formal Windows verification. The existing `AProcessEnteringAfterTheRecoveredForcedPhaseIsTerminatedWhenTheStartCompletedBeforeItOnWindows` waited 60 s but did not establish that its second step had left the job. Other cancellation cases passed, including the debugger-held regression at 298 ms. This is not a complete successful author batch.

Code inspection found a missing test precondition: reopened Started completes on job entry, while AttemptRunner creates the step suspended, assigns it to the jobs and only then resumes it. Suspending its holder immediately on Started can prevent that Resume. An independent real stopping-job probe confirmed completed Started for the exact PID/creation while the child remained CREATE_SUSPENDED with no workload marker; its marker appeared after Resume (1 passed, 0 skipped). The original failing thread state was not retained, so the probe establishes the race the old test failed to exclude, rather than a captured timeline of that failure. [Microsoft's creation-flag contract](https://learn.microsoft.com/en-us/windows/win32/procthread/process-creation-flags) specifies that the primary thread does not run until ResumeThread.

The probe temporarily changed JobTests.cs, then restored its original bytes and rebuilt the original project; entry-restored.diff is empty. Logs: `entry-probe-test.log`, `entry-probe-build.log`, `entry-restored-build.log`, `entry-probe.exit` (0), under `resume-20261025-mr101`.

The bounded test-only fix in the existing PR (8c1c06c; 11 insertions/1 deletion) waits for the second step's actual start marker before suspending its holder. The absent go2 file still holds that step before the command. A new assertion requires the readiness precondition. All original empty-job, cancellation, phase-count, no-late-command and timing assertions remain. Target test and full LaunchFault class passed (1/1 and 10/10, no skips); build/format passed with 0 warnings/errors. The complete delta was self-reviewed directly; no blocking finding. No product file changed in this delta.

Fresh runner: `integrated-8c1c06c.ps1`, logs `final-8c1c06c`. Complete Windows author validation is now the common prerequisite of both new-head formal legs. author.exit=0 is written only after every standalone/affected/loaded check passed, all lanes drained and final source/head checks passed; only then does Windows formal start and Linux formal may be launched. The prior 54ac6e0 Linux leg is not restarted or reused.

The prior 54ac6e0 Linux leg completed all 16 steps in 1131 s, tree `cade993bc5eb129b59ae7249c8d21817d83df6f2`, base `266bfa60229fc191e85966ee406c84ce3a4ead55`; summary SHA/results were checked. One subsequent Linux MCP log read had a transient transport error; a bounded read-only retry recovered the existing completed log, without restarting verification. Its status remains old-head evidence only.

At 8c1c06c the Windows runner completed all 10 standalone classes, the affected classes and Platform.Windows ci, then entered its three-stream loaded batch. The first four full Node.Core ci runs passed (287 total each; target class 10/10 each). Fresh-worktree AOT host publish passed with 0 warnings in 153.2 s beside the tests. These are partial batch results; complete author success and formal host verification are not yet established.

## Complete author validation at 8c1c06c

The full guarded batch passed and drained before formal verification. `author.exit` and `done.exit` are 0, final-source.diff is empty, and the head was rechecked. Audited evidence is saved in `final-8c1c06c/audited-author-evidence.json`.

| Check | Result |
|---|---|
| Locked restore / changed-file format / Release solution build | passed; build 0 warnings/errors, 12.59 s |
| 10 standalone LaunchFault class runs | each 10 passed, 0 failed, 0 skipped |
| EscapedTermination + TaskControl | 17 total, 16 passed, 1 Linux-only skip, 0 failed |
| Platform.Windows ci | 116 total, 115 passed, 1 documented adoption skip, 0 failed |
| 10 integrated Node.Core ci runs beside ClosedLoop and AOT | each 287 total, 254 passed, 33 platform skips, 0 failed; target class 10/10 each, 100/100 total |
| ClosedLoop load lane | 8 complete runs, each 44 total, 31 passed, 13 platform skips, 0 failed; drained exit 0 |
| AOT lane | all five component names exercised, first fresh host publish 153.2 s with 0 warnings; lane drained exit 0 |

CTRF records confirm 10 passes each for the watched infeasible, fairness and parallelism tests and the repaired recovered-launch precondition test. The infeasible method's complete duration ranged 6322-27074 ms (includes fixture/setup; this is not its internal stopwatch). No timing bound changed. The original failing samples still lack a retained exact timeline and are not retrospectively reported as fixed by these passes.

Formal Windows started at 12:57:46 UTC only after author success/drain. Linux started afterwards, after confirming author.exit=0 and the previous Linux exit=0; its user manager was running and no test/workload processes remained before launch. Both legs fetch the exact pushed head. Windows summary directory: `C:\MyFile\Projects\ArcForges\ArcForges\.git\arcforges-verify\logs\20261025-125754-8c1c06c08122-win`. Linux summary directory: `/home/sammiller/arcforges/ArcForges/.git/arcforges-verify/logs/20261025-210005-8c1c06c08122-linux`. Final formal results and GitHub required-status inspection are pending.

The 8c1c06c Windows formal leg completed all 13 full-profile steps in 932 s, tree `bfd8bbb17a9913652c388a53c0fe2fc57892e48c`, base `266bfa60229fc191e85966ee406c84ce3a4ead55`; every summary result and the SHA were checked, windows-verify.exit=0, and the host reported success. Linux formal verification and the final GitHub merge-gate inspection remain pending.

## Final formal gate and merge

Linux completed all 16 full-profile steps in 1130 s at 8c1c06c, matching the Windows summary's tree `bfd8bbb17a9913652c388a53c0fe2fc57892e48c` and base `266bfa60229fc191e85966ee406c84ce3a4ead55`. Every result, step count and exact SHA were checked. Both native host commands returned 0 and reported success; no competing build/test ran on either host during its formal leg.

Immediately before merge, GitHub reported head 8c1c06c, base 266bfa6, mergeable=true, both required statuses success, and owner-hosted jobs skipped as specified. The final complete two-file diff (358 insertions/5 deletions) was self-reviewed directly under the owner's no-other-model/agent instruction; no blocking findings. Existing #45 merged as `866b0b7f3695cdbca8eebfd5ebe20566805d4330`.

The repair restores launch-step stop latency and preserves normal-zero-exit resource lifetime. Test cleanup and recovered-launch readiness synchronize actual resource/process states while retaining all original task and timing assertions. Earlier interrupted/failed checkpoints remain above and were never counted as complete final-head validation. MR-102 (root wait) and MR-103 (end-step budget) remain separate. After this Plan record merges, continue MR-04 with Design#25 before ArcForges#44, then MR-102 and maintenance priorities. MR-16 stays blocked; recovery proposal retained, later features unstarted.
