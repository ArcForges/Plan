# MR-100: STOPPING cause and retry rules across a node crash

Date: 2026-10-25. Design: [ArcForges-Design#29](https://github.com/ArcForges/ArcForges-Design/pull/29) and [#30](https://github.com/ArcForges/ArcForges-Design/pull/30).
Implementation: [ArcForges#51](https://github.com/ArcForges/ArcForges/pull/51).

## Dependency and scope

MR-100 precedes MR-99: persisting additional STOPPING paths without restoring their cause would classify those stops as cancellations
after restart. The MR-99 worktree was created cleanly from source main 6caf418 but remains unmodified; its state-machine reconciliation
continues only after this cause repair and its Plan records finish. No later feature task was activated.

Design merged first as `c58c228fa160c34e91c126e1408c02a2e4efb478`, reviewed head
`154dafc7c6b3ef7768271f6121fb1a82c6f51cb5`, tree `eb8c255197e154101fd8370c0e2a3007c449f942`,
base `64e7c99459d25b2e247471f4fad26b0baf51fdb9`. The two-file, 12-line clarification specifies pending stop cause/detail in the
existing attempt.termination_reason/detail columns, atomic with STOPPING. Pending intent is not a final AttemptResult; the contract
publishes result only at FINISHED, after finalization writes the actual outcome (including TERMINATION_INCOMPLETE when applicable).
Recovery continues the forced stop with its known cause/detail and existing retry rules. Legacy null-cause STOPPING rows retain the
previous cancellation fallback; the node does not parse human text to invent a preemption or permission to retry. SQL schema/version,
proto and state transitions are unchanged; no migration or backfill.

Design author: locked proto-toolchain restore; check_design.py --require-protoc --compile (25 files, generated C# zero warnings,
zero errors; 63 node and 13 cloud tables loaded), 44 tool tests (20 existing Windows skips), git diff --check passed.
Complete final-head summaries/all results were read: native Windows full 3 steps/15 s, Linux full 3 steps/46 s, same head/tree/base.
Summaries under Design/.git/arcforges-verify/logs: `20261025-182125-154dafc7c6b3-win`, `20261026-022121-154dafc7c6b3-linux`.
Direct two-file self-review by OpenAI Codex alone, comment 6401398737, no blocking finding. Both required successes, owner-skipped
hosted check, freshly fetched main/head/base and mergeability were checked before merging.

## Implementation

Initial pushed head `6b4e8c471ec0f6c2902504518b117ebbc7231ef6`, tree `7dc8c5d2cb4017f3a7a3389f9c17140e1f3a396c`,
base `6caf418af3eba19a5d4d7989e8ed11476b67736b`.
Preempt, pressure Requeue and cancellation write cause/detail with their existing STOPPING update, restricted to the same live predecessor
states, without overwriting an already-stopping row. Recovery recognizes STOPPING even when reason is non-null, restores its cause and
detail, and preserves the legacy cancellation fallback. The admission-registration handoff reads the same stored intent.
TaskRecords reads detail in its internal row view and publishes Attempt.result only at FINISHED. Finalization and AD-0006 still decide
the final outcome and retry permission; storing PREEMPTED does not make an unasserted class retryable. No package, SQL schema or RPC change.

A test-only hold-preempt-before-stop fault, gated by ExecutionFaults.FromEnvironment(testMode), holds the first preemption before its
platform stop. The real-node tests wait for committed STOPPING, confirm no public final result and that the actual command is alive,
restore their node's pressure policy, kill only that node, and confirm its root remains alive under the holder/unit. Recovery then must
finish the old attempt with node_gap/HAPPENED and the known cause. An asserted idempotent task must start a distinct second attempt
with two real workload start markers. An unasserted task must remain failed with one attempt and no retry. A legacy case clears only
the cause in that fixture's temporary row, retains the preemption text, and requires CANCELLED with no retry.

Windows covers Critical preemption and Pressure requeue; Linux covers Critical preemption. Both use real samplers with only that node's
policy thresholds changed, no fake sampler, allocator or machine-wide pressure manipulation. Every entry point has exclusive and
DisableParallelization traits. The fixtures use --test-mode isolated secret stores and clean up their own nodes, attempts and units;
no real Credential Manager access, orphan credential operation, user-manager termination, pkill -f or daemon-reload.

## Before, diagnostics and after

Before the cause fix, with only the test-mode hold seam and new tests added to product main 6caf418, Windows had 3 failures/1 pass,
zero skips: the Critical retryable/unasserted and Pressure retryable cases expected PREEMPTED but recovered CANCELLED; the legacy control
passed. Root survival across the actual crash was asserted before this failure. The first two builds failed before runtime on a
ProcessIdentity name collision and nullable-value handling; these provide no runtime before evidence. Both were fixed structurally,
without suppression or assertion removal. Logs mr100-before*, actual runtime before run mr100-before3 (4 cases, about 35 s, exit 2).

The first after run restored every cause, but two retryable cases timed out waiting for QUEUED (2 passed/2 failed, exit 2).
Diagnostics showed RETRY_WAIT with an asserted caller class and a scheduled PREEMPTED retry, then a real second RUNNING attempt.
The test had assumed ParallelismMode.DISABLED paused admission: Design 03 section 4 and queue.proto define it as FIXED 1, allowing a
retry to start once its predecessor finishes. One diagnostic case passed and a four-case diagnostic run still failed once because
QUEUED is transient. A diagnostic build also caught xUnit1069 (explicit cancellation-token use was missing in the temporary diagnostic
entry point); no test ran in that build. These failed/partial/diagnostic runs are retained, never counted as complete author success.

The final test removes that incorrect queue-control assumption and verifies the stronger observable result: a distinct second running
attempt and second actual command start, retaining denial/legacy controls and the original 90 s bound. Temporary diagnostics were removed
before the pushed commit. State traces are retained as mr100-retry-state-critical.txt and mr100-retry-state-pressure.txt in Windows dev logs.
This is a test setup correction supported by the existing contract; no admission/parallelism policy was changed by MR-100.

Initial cause-repair Windows author (mr100-after2): full Release build/analyzers zero warnings/errors, crash cases 4/4, LaunchFault 18/18,
TaskControl 15/15, lifecycle model 1/1, repository isolation policy 2/2; changed-file format, format verify and git diff --check passed.
Host Native AOT published with zero warnings/errors; all four crash cases passed again against the actual native node (mr100-aot).
Initial cause-repair Linux author (mr100-author): locked restore, full Release build/analyzers zero warnings/errors, crash cases 3/3, LaunchFault
11 passed/7 Windows skips, lifecycle model 1/1, isolation policy 2/2, changed-file format verify; host Native AOT zero warnings/errors,
and all three crash cases passed again against the actual native node. Both author wrappers exited 0; hosts were drained before formal legs.

Author commands through native MCP, each background job with its own stdout/stderr/exit marker:

```text
dotnet restore ArcForges.slnx --locked-mode
dotnet build ArcForges.slnx -c Release --no-restore
dotnet test --project tests/ArcForges.ClosedLoop.Tests -c Release --no-build --filter-method '*APreemptedAttemptKeepsItsCauseAndRetryRulesAfterACrashOnWindows' --minimum-expected-tests 4 --parallel none --output Detailed
dotnet test --project tests/ArcForges.ClosedLoop.Tests -c Release --no-build --filter-method '*APreemptedAttemptKeepsItsCauseAndRetryRulesAfterACrashOnLinux' --minimum-expected-tests 3 --parallel none --output Detailed
dotnet test --project tests/ArcForges.Node.Core.Tests -c Release --no-build --filter-class ArcForges.Node.Core.Tests.LaunchFaultTests --output Detailed
```

The corresponding TaskControlTests class ran on Windows; TaskLifecycleModelTests and repository TestIsolationPolicyTests ran on both.
Windows format used dotnet format ArcForges.slnx --no-restore --include <five changed C# files>, then --verify-no-changes; Linux used
--verify-no-changes directly. Windows MSVC Developer PowerShell used eng/publish.ps1 -RuntimeIdentifier win-x64 -Component @('host').
Linux used dotnet publish src/ArcForges.Host -c Release -r linux-x64 -o artifacts/publish/linux-x64/host -warnaserror -tl:off
'-clp:Summary;ForceNoAlign' -p:TrimmerSingleWarn=false. ARCFORGES_HOST_PATH then selected each host's own published native node for the
same new closed-loop methods. These are actual native-node crash/recovery tests, distinct from in-process-node helper tests.

## Final host profiles and merge

Initial five-file direct self-review by OpenAI Codex alone at6b4e8c4, comment 6401742995, found no blocking diff issue.
No independent model or agent reviewer is claimed.
The first Linux full leg at this head failed at linux-ci: 136 s overall, Node.Core 247 passed/47 skips/2 failures in the existing
MR-95 recovered CPU-limit cases (during gap and after recovery), at final Usage.CpuTimeMs >= 1500. Both already had the expected
CPU_TIME_EXCEEDED outcome. Later schema/AOT/native/exclusive/startup steps were unrun; this is failed/incomplete, not a merge pass.
The Linux author checks and Windows formal leg remain distinct. A diagnostic-only Linux worktree records enforcement CPU, exit-record
cgroup/counters and unchanged assertion evidence; the first standalone 296-case Node.Core diagnostic passed 249/47 skips, so it does
not explain or erase the original full-CI failure. The complete two-lane CI diagnostic reproduced both cases: enforcement read
2244/1937 ms, while exit.json had recorded_by=unit with 249/131 ms; the exit-record helper had not written its record. That run also
failed a launch-cancel bound (10.14 s > 5 s), lifecycle model (systemd start timed out), and watchdog restart (45.8 s > 45 s).
These remain failed diagnostic evidence, not formal status.

A deterministic real-unit regression then held a real end step after its command exited and invoked the same late forced phase.
Before the repair it failed: five helper/step processes were killed and the end step never reached its completion marker (4.56 s,
mr100-end-before). The repair leaves systemd's bounded control helpers alone when the root has exited; otherwise it snapshots actual
member identities and kills the same processes, main last. A timed-out FreezeUnit is directly thawed in finally too, so a manager
spawn never depends on a successful D-Bus reply to be released. No configured CPU threshold is substituted for measured usage.
The unchanged regression passed after the repair in 650 ms with an exit-record result and normal exit code. Diagnostic-only CPU
logging/files were archived outside the source tree and removed.

The first Windows full leg also failed: 1130 s overall, win-exclusive-native's new retryable Critical case timed out waiting for the
second marker; startup gate unrun. The second real attempt was already RUNNING. The test used File.ReadAllLines during marker polling;
a native file-sharing probe proves this denies HoldScenario's append open, whereas the existing TestNode.ReadShared helper permits it.
Polling now uses that helper. All four actual native-node cases passed again (32 s, mr100-marker-after), with both starts, denial/legacy
controls, the same 90 s bound and no assertion weakened. First-leg source comments 6401815189 and 6402032068 retain both failed statuses.
At this diagnostic stage fresh complete profiles on the eventual final pushed head were still required.
Intermediate pushed head `9aad2686f3c7d7d7c0675cd4cf7d8a324038f4da`, tree `f4aff565de52219d512991d5547de9abb472ef9d`,
same base 6caf418. Seven changed files, 318 insertions/33 deletions. Intermediate direct self-review comment 6402107567 covers every file,
including validating the root identity after each member scan to exclude a newly started helper if the root exits during the scan.
The earlier 770003b Windows leg was already running when that final review improvement was made; its result belongs only to that
superseded head and was drained before the final Windows profile.

Additional author logs mr100-stop-author: Linux platform 83/83 JIT and 83/83 actual native host; complete two-lane ci passed including
Node.Core 249 passed/47 Windows skips; Host Native AOT zero warnings/errors; native crash cases 3/3. The wrapper then failed only
changed-file format at two missing final newlines introduced by MCP text synchronization. No source runtime failure in that run,
but its exit 2 is not called a complete author pass. The newline transfer was corrected explicitly and the final after-scan identity
guard receives fresh author verification (mr100-stop-author2).
Windows mr100-followup-format: full Release build/analyzers zero warnings/errors, changed-file formatting/verification and diff check
passed; native marker-corrected crash cases remain 4/4. The later identity guard is Linux-only and receives its native checks there.

mr100-stop-author2 exited 0: final after-scan guard compiled with zero warnings/errors; Linux platform83/83, LaunchFault11 passed/
7 Windows skips, Host Native AOT zero warnings/errors, native end-step regression1/1, actual native crash3/3, changed-file format
verification/diff check. A comparison to the pushed source also caught the MCP display of one old Unicode environment-test string
being transferred as mojibake; that transfer-only change was removed using the exact Git commit. No encoding change is in the PR.

The superseded 770003b Windows formal failed at win-ci; later steps unrun. Existing MR-102 positive control
ASuccessfulRootStillWaitsForItsProcessToRunDownOnWindows reached SUCCEEDED after the held successful root was released, but its end-step
marker was empty (line107). The explicit zero exit/empty job/held run-down/absence-of-early-end-step guards had passed. A temporary
end-step-result instrumented two-lane Windows CI then passed (Node.Core263/33 skips), so this diagnostic alone does not explain or
erase the formal failure. A subsequent native job-admission probe checked the test's deliberate TerminateJobObject setup; its results follow below;
no blind formal rerun. Source discussion 6402139807.

Windows superseded formal summary 770003b: tree9961f8e99a48afc00f80f3153065e6e21cef2bef, same base6caf418, 104 s total;
restore/base-host/build passed, ci failed in88.5 s, all later steps unrun. Log directory20261025-192253-770003bfa154-win.
Native admission probes then distinguished the setup: with EXIT_PROCESS held, the test-terminated empty job returned
ERROR_ACCESS_DENIED to a suspended new member, before and after an empty-job reset. Only after full root run-down and empty reset did
that same probe admit a new member; the actual end step then reported success (mr100-root-probe5,1/1). The first individual-process
variant omitted terminate access; the next showed already-exiting members still reject individual termination. Both only emptied after
the debug hold's30 s automatic release, so neither is valid positive root-hold evidence. One probe build used the wrong fixture-helper
namespace and ran no tests. All logs retained; no blind formal retry.

The final test changes only release setup, after all original negative guards passed: suspend this fixture's holder, release the exact
root, await its complete run-down, reset the now-empty job, then resume the holder in finally. Zero exit, empty job, held root, two seconds
without end steps/exit.json, task RUNNING, final SUCCEEDED and actual end-step marker assertions/bounds all remain. Temporary product
instrumentation and probe processes were removed before commit. Source comment6402243301 records the evidence; new Windows author
CI/native/format checks subsequently passed on this code.

Intermediate pushed head `eb7b208b5bb7cf0246f892ac1e819f0506f4ff60`, tree `6ff28dc8e6cd20cd54b83b2ca6284597572bd7f9`,
same base6caf418; eight files333 insertions/35 deletions. No formal Linux leg ran on770003b or9aad268.
Windows final root-fixture author (mr100-root-author) exited0: Release build0 warnings/errors, full two-lane ci passed
(Node.Core263/33 skips), native-helper LaunchFault18/18, actual native-node crash4/4, changed-file format/diff-check passed.

A further direct review found the initial Linux preservation early return too broad: remaining workload descendants must still die
when the main command has exited. The eb7b208 Linux full profile did pass16/1172 s at its own tree/base (all results read, summary20261026-033916-eb7b208b5bb7-linux); no Windows formal leg ran
at that intermediate head, and this later demonstrated gap prevents using its pass for the final candidate. The source follow-up uses systemd control identity before/after the process snapshot, protects the bounded control tree,
and signals only remaining workload identities; a failed-freeze path also rechecks after direct thaw. The real-unit regression now has
a second variant with a real descendant proven alive when the main root has exited and the end step is held. That descendant must die
within the original5 s bound before releasing the end step; no controls or workload-zero assertion are weakened.

Required Design follow-up [Design#30](https://github.com/ArcForges/ArcForges-Design/pull/30): head
`a498bb53f6de4b8e05bde2626f43bba20c1393b1`, tree`bbf7bb4cce5df36126592f4d79b5c36ef7dd6713`, basec58c228.
One-file4 insertions/3 deletions in04 section6 clarifies workload/control boundary, late-stop cleanup, timeout-thaw and the original5 s
workload-zero verification. No state/schema/proto/package/migration change. Final author locked proto restore/check_design compiled25/
generated C#0 warnings/0 errors;44 tool tests with20 Windows skips;diff-check. Direct whole-diff self-review6402359722, no blocking finding.
Windows full3 steps/12 s passed, summary20261025-194854-a498bb53f6de-win; all summary results read. At that point its Linux leg waited for the existing source
formal job to drain, with no competing build/test; the completed result and merge follow below. Source discussion6402359956 records the required follow-up; no implementation merge
before Design#30. The Windows follow-up compile/changed-file format/verify/diff-check exited0 (mr100-control-compile).

The real-leftover baseline at intermediate eb7b208 plus the new test had1 pass/1 fail,0 skips: the descendant was proven alive after
root exit and remained alive5 s after the forced phase while the real end step stayed held. Cleanup then released the step and drained
the unit;11.45 s total, mr100-leftover-before exit2, build0 warnings/errors. After the control-tree fix both variants passed in621/629 ms;
the leftover case killed2 workload processes while preserving the held control tree, normal exit0 and recorded_by=exit-record.

Final candidate `c146ddebb8ce912d375ef5facd505d00525dba6b`, tree`6e9977f679f505c8b1ac4520a12ea5986e36406a`,
same base6caf418, eight files441 insertions/35 deletions. Source discussion6402506035 records the baseline.
Windows mr100-c146-author exited0 at the clean pushed head: Release build/analyzers0 warnings/errors, Host Native AOT0 warnings/errors,
native-helper LaunchFault18/18, actual native-node crash4/4, changed-file format verify/diff check.
Linux mr100-control-after exited0: the two real stop regressions2/2, platform84/84 JIT(serial,62.4 s), complete two-lane ci passed
(Node.Core249/47 Windows skips,43 s; platform78/78; closed-loop25/19 platform skips,69.7 s), Host Native AOT0 warnings/errors,
platform84/84 with native helpers(serial,53.4 s), actual native-node crash3/3,format verify/diff check. Its working source was compared
byte-for-byte to c146dde after fetching; the patch was archived outside the repo and the worktree checked out cleanly at that commit.
Those Linux author binaries came from matching working source before clean checkout, and are not final-head formal artifact evidence.

Complete final eight-file direct self-review after authors found no remaining blocking issue; final source profiles ran independently
after each host's author jobs drained. No other model/agent or independent reviewer. Final direct self-review comment6402619710; no remaining blocking issue.
Design#30 merged first as `049cf20a7da7994d849c13dab2c7ac8944c20529`. Linux full3/38 s, summary
20261026-040343-a498bb53f6de-linux, all results read with identical head/tree/base; both required statuses success and owner-hosted check
skipped. Fresh native fetch/main/head/mergeability confirmed before exact-head merge; final gate6402541626. Windows Plan context
was refreshed cleanly to049cf20; both final Plan host profiles must still fetch current Design main before their run/merge.
Complete final-head native profiles passed: Windows full13 steps/1051 s; Linux full16 steps/1168 s. All summary results were read at c146ddebb8ce912d375ef5facd505d00525dba6b, tree6e9977f679f505c8b1ac4520a12ea5986e36406a, base6caf418af3eba19a5d4d7989e8ed11476b67736b. Summaries: Windows 20261025-201054-c146ddebb8ce-win; Linux 20261026-041247-c146ddebb8ce-linux. Both required exact-head statuses were success; owner-hosted checks were skipped. Fresh main/head/base/mergeability and the unchanged eight-file direct review6402619710 were checked before merge; final gate comment6402924959. No older-head success was reused.
ArcForges#51 merged as `dec32cb8ab48a575d563c5e4a1b10c80fc95c486`, after both Design dependencies had merged.

Both native hosts retain their own full profiles and step logs under ArcForges/.git/arcforges-verify/logs; no binary moved between hosts.
Windows author/diagnostic/profile logs: C:\MyFile\Projects\dev\logs\mr100-* (stdout, stderr and exit markers; root/control/c146 follow-ups included).
Linux author/diagnostic/profile logs: /home/sammiller/arcforges/logs/mr100-*; each native full summary stays in its repository's .git/arcforges-verify/logs.

## Disposition and future compatibility

MR-100 is fixed; the maintenance row and AF-EXEC-02 CLI ledger note record the final merge/head and both complete profiles. MR-95 and MR-102 retain their earlier valid results with links to these helper/fixture follow-ups. Future AF-DIST-02 stays planned.
AF-DIST-02 remains planned, with explicit supported-version update/rollback acceptance for pending STOPPING cause/detail semantics:
preserve the interpretation and retry rules, or settle with the compatible node first. An unknown legacy cause is not reconstructed
from human-readable detail. No updater, migration, backfill or cross-version validation is implemented or claimed here.
MR-99 state persistence is next; its clean worktree is retained. MR-16 remains blocked and its recovery proposal retained.
