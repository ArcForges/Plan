# MR-103: one bounded end-step budget on both native platforms

## Repair scope

[ArcForges#53](https://github.com/ArcForges/ArcForges/pull/53) repairs end-step timeout selection in the Windows holder, Linux ExecStop
and Linux observe-only child path. All three previously passed a negative timeout through to their process wait. In particular -1
selected an infinite wait; zero and other negative values could instead kill a step before it ran. The maintenance-list observation
named Windows; the code audit found the same defect in both Linux paths, repaired in this item.

The existing authority is architecture 04 section 3 at Design main 376c6e9b3b895e75ef3e486623e0b16ad931161f: end steps share a
ten-second budget, their failure does not change the root result, then leftover cleanup and exit recording follow. No Design change
is needed. A nonpositive per-step timeout now uses the remaining total budget; a positive value is still capped by that remainder.
The budget is not restarted for each step. Launch-step timeout behavior and all other termination/accounting guards remain intact.
No public schema/RPC/package change, database migration, later feature, LAN/cloud MCP, real credential-store or orphan-file operation.

## Real before/after regressions

The Windows holder and Linux unit/direct cases each run a real first end step that consumes four seconds. A second real step has
TimeoutMs -1, 0, -2 or 30000 and runs long enough to exceed the shared budget if it is not capped. A third sentinel must never start
after the budget is consumed. The regression requires the second step to start, exit recording within twelve seconds of observing
the first step (the real ten-second budget plus two seconds for scheduling/recording), at least eight seconds elapsed, unchanged
successful root exit, no launch failure and no sentinel. Unit stop records must show timed_out, timed_out, skipped.

The four seconds spent first make a wrongly restarted ten-second budget fail the twelve-second total bound. These are timing-sensitive
exclusive tests with actual processes/jobs or user units; no fake clock, process, sampler or platform substitutes for the behavior.
The Linux direct case uses the existing unreachable-manager-address fault to select real observe-only children, without stopping or
altering the user's actual manager. Its before-fix fifteen-second children finish and are reaped in fixture cleanup; completion is
awaited before disposal. On Windows thread rundown is separately drained after the bounded exit record (MR-101). Fixture cleanup is
limited to its own attempts/slice; no user-manager shutdown, daemon-reload or pkill -f.

Before repair:
- Windows production source was unchanged at main 47ec7aa38b3c8a7431862ad98b6c0b3c6ddcf8e5. Locked restore/Release build passed.
  The new four cases reported 3 failures/1 pass, test exit 2, 33.684 s. The -1 case had no exit record within its total bound; 0/-2
  produced no second-step marker. The long positive control passed at 10.210 s. Wrapper captured that expected failure and exited 0.
- Linux fetched the test-only head 8ab02278f66fd38c4974fa6b12be3baa56c40c2d, with unchanged production source. Locked restore/Release
  build passed. Eight cases reported 6 failures/2 positive-control passes, no skips, test exit 2, 73.420 s. Each path reproduced all
  three nonpositive defects. Direct -1 finished cleanup naturally after about 19 s; the unit's separate stop timeout bounded its
  before-fix failure at about 15.6 s. That external unit timeout was not the required shared ten-second budget.
- Both before wrappers drained. Logs: Windows C:\MyFile\Projects\dev\logs\mr103-before.{ps1,out,err,test-exit,exit};
  Linux /home/sammiller/arcforges/logs/mr103-before.{sh,out,err,test-exit,exit}. Test-only intermediate heads ran no formal profile.

After repair:
- Initial Windows working-tree Release build, format and HolderTests passed 9/9 in 49.389 s. All four new cases completed at
  10.191-10.220 s, preserving the root result and blocking the sentinel. This is author evidence, not a post-push full profile.
- At the pushed head below, Windows Host win-x64 Native AOT published with zero warnings/errors; HolderTests 9/9 and native-helper
  LaunchFaultTests 18/18 passed. Changed-file format/diff passed, and mr103-native-author exited 0.
- Linux full affected platform project passed 92/92 JIT in 144.510 s, with no skips. Host linux-x64 Native AOT published with
  warnings-as-errors, then the same project passed 92/92 against native helpers in 137.412 s, no skips. All eight new unit/direct
  cases passed in each run. Format/diff passed, worktree clean, mr103-after exited 0.
- The direct budget loop executes in the real parent test process; its command launch uses the selected real helper. The unit
  ExecStop and Windows holder run their real helper roles. A native-node direct-budget claim is not inferred from this coverage.
- Linux synchronization uses Git fetch/checkout only; no source file or verification artifact is copied between hosts through agent
  context. Author commands/results: Windows C:\MyFile\Projects\dev\logs\mr103-native-author.{ps1,out,err,exit};
  Linux /home/sammiller/arcforges/logs/mr103-after.{sh,out,err,exit}.

## Commit, author checks and final gate

Final reviewed head: 0b11e1c97081dc6c1cb4baf8065015bb3038f79f.
Tree: 153aee3c889f4942fe3d89938d8e8657c2f2b617.
Base: 47ec7aa38b3c8a7431862ad98b6c0b3c6ddcf8e5.
Five files: three timeout-selection repairs and two real regression test files.

[Author evidence](https://github.com/ArcForges/ArcForges/pull/53#issuecomment-6404412089) records both hosts and before-fix failures.
[Direct self-review](https://github.com/ArcForges/ArcForges/pull/53#issuecomment-6404412350) covers all five files, the three repaired
paths and real regression/cleanup behavior against existing Design; no findings. No independent review claimed.

Both full native profiles completed on the final pushed head, after the relevant host's author jobs drained:

- Windows full: 13 steps/1140 s, 20261025-223721-0b11e1c97081-win.
- Linux full: 16 steps/1357 s, 20261026-064114-0b11e1c97081-linux.
- Every selected result was read and passed, including JIT/native exclusive suites and startup gates.
- Both required exact-head arcforges/windows and arcforges/linux statuses were success; owner-hosted checks were skipped as configured.
- Fresh PR head/tree and source main/base were checked immediately before merge; actual source merge 4990f63f33bcf36855e184e4e8c4d3b8d7bde003.
- [Final gate](https://github.com/ArcForges/ArcForges/pull/53#issuecomment-6404647803); exact-head direct self-review above.

Windows full logs: C:\MyFile\Projects\dev\logs\mr103-final.{out,err,exit}.
Linux full logs: /home/sammiller/arcforges/logs/mr103-final.{out,err,exit}.
Both native runners exited 0 and drained; no competing build/test, older-head status, expected failure, partial run or skip was used
as the final gate. Maintenance-list status and the completion note were updated only after the source merge; the ledger note was
appended through the Plan CLI, with no task-state activation.

MR-16 remains blocked. AF-REC-01 and later feature tasks remain unstarted. MR-105 is the next maintenance follow-up after this item,
before continuing the list. No other model or agent was used; any review is direct self-review under the user's explicit instruction.
