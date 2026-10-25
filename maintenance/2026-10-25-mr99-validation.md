# MR-99: durable managed-attempt phases

## Scope and disposition

MR-99 repairs the managed executing-attempt paths named by the maintenance list: the fictional CREATED predecessor, missing durable
FINALIZING, and internal stop causes that could recover as RUNNING. No enum, public RPC, package or database schema migration changes.
AF-REC-01 and all later feature tasks remain unstarted. Real Windows Credential Manager cleanup, orphan credential-file operations and
real-store stress remain prohibited (MR-16). All operations and checks used the native Windows/Linux MCP hosts; no agents/models were
delegated.

The code-wide review also found the separate synthetic ADOPTED mapping gap, now open MR-105. Adoption already starts from an existing
process and has the LOST/no-exit-status semantics of architecture 04 section 10. This managed-execution repair does not claim those
separate initial/finish paths repaired. MR-105 follows MR-103 in the same maintenance section. Successful Windows adoption stays
deferred where every user process is already in a job. This is a code audit; the full source profile's existing adoption
regressions are separate coverage, without a new canonical-transition validation claim.

## Design first

[ArcForges-Design#31](https://github.com/ArcForges/ArcForges-Design/pull/31) defines local STARTING as committed launch intent before
container creation. CREATED remains a future preparation state; placement/cache features are not enabled. The first local attempt
event has no previous state. Completion evidence commits FINALIZING separately before final output/accounting/result recording;
end steps and leftover rundown may precede that evidence in the holder/unit. Fast completion can enter FINALIZING before RUNNING
was published. Direct FINISHED shortcuts require the declared spawn/policy or recovery LOST reason and effect.

STOPPING stores its pending cause and redacted detail before platform action and retains them through FINALIZING. A live phase
exposes no final AttemptResult. A legacy STOPPING row without a cause retains cancellation fallback; FINALIZING without a cause is
normal completion, never inferred cancellation. Absence of a pending stop does not imply success: exit/launch evidence still
determines the outcome. AD-0004 was amended and the generated state-machine README regenerated.

- Head: 401f6ae96e62b37edd6a0dd59db784c300e2f0f1; tree: b43f271e10c75d8075bac5630a9abc62bca5857e.
- Base: 049cf20a7da7994d849c13dab2c7ac8944c20529.
- Actual merge: 376c6e9b3b895e75ef3e486623e0b16ad931161f, before the implementation merge.
- Author: check_design.py --write compiled 25 protos, 0 errors; diff check passed.
- Exact-head Windows full profile: 3 steps/13 s, 20261025-211008-401f6ae96e62-win.
- Exact-head Linux full profile: 3 steps/45 s, 20261026-051005-401f6ae96e62-linux.
- All summary results and both required success statuses read; owner-hosted check skipped.
- [Direct self-review](https://github.com/ArcForges/ArcForges-Design/pull/31#issuecomment-6403343385), no findings. User-authorized
  direct work without another agent/model; no independent review claimed. Fresh main and PR head checked before merge.

## Implementation

[ArcForges#52](https://github.com/ArcForges/ArcForges/pull/52) uses the serialized writer for internal stop intent and a separate
FINALIZING transaction. Cancellation, pressure preemption/requeue, timeout, CPU/output/disk limits and kill_with_node shutdown share
the durable stop path. Pending stop recording is awaited before finalization. The first committed cause wins; queue/store failures
retry rather than applying the platform stop ahead of its cause, and an unrecorded shutdown result cannot be acknowledged as success.
A platform-call failure retains the durable intent for the enforcement loop's forced retry.

RecordFinished now requires the persisted FINALIZING phase. Pre-container failure also uses the common final result path, retaining
a stop that won the writer race. Finalization reads a STOPPING cause that committed immediately before its own writer turn, so the
live outcome and recovery use the same committed intent. Recovery recognizes FINALIZING and preserves the distinction between a
normal nullable cause and a legacy STOPPING cancellation fallback. Root-start evidence, measured accounting, termination guards,
five-second verification bounds, retry permission and secret-store isolation remain intact.

The model checks actual initial states with no invented predecessor and validates FINISHED reason/effect triggers, instead of
silently accepting every live-state finish. Eight trigger/effect vectors include rejected normal direct finishes and wrong effects.
A deterministic real-node exit test requires a private FINALIZING event followed by FINISHED. Three real process-crash cases on each
OS kill the actual test node after a committed timeout STOPPING, normal FINALIZING, or timeout FINALIZING. They read the fixture's
SQLite phase/cause, require no public result while live, retain the same attempt and node-gap marker, preserve the expected final
reason/effect and assert exactly one real workload start. In the STOPPING case the actual root must survive the node crash.

## Before/after and author checks

Before repair, only the new model test was added to the unchanged production source at main dec32cb8. The real Windows exit test
failed with "Local admission must not invent a prior CREATED row." (1 failed, 0 passed, test exit 2), proving that the new regression
rejects the old behavior. This failure stops before the later FINALIZING assertions and is not claimed to prove those assertions
failed separately. Log: C:\MyFile\Projects\dev\logs\mr99-before2.{out,err,test-exit,exit}.

Compile-only iterations are retained and not counted as runtime verification: mr99-before failed the xUnit2031 analyzer (use the
predicate overload of Assert.Single); mr99-after failed an ambiguous ProcessIdentity name and nullable-result access; mr99-after2
failed nullable value-type IsRunning calls. These were corrected without weakening an assertion. A temporary PowerShell patch
capture did not apply after restoring the baseline; no file was partly applied, and edits were regenerated on the Windows host from
the unchanged source. All subsequent Linux code synchronization used Git fetch/checkout, with no source files copied through agent
context.

Initial working-tree mr99-after3 completed: Release build 0 warnings/errors, model 10/10, LaunchFaultTests 18/18 and actual node-crash
phase tests 3/3. Direct review then added the writer-race handling described above; final author evidence below uses its pushed head.

Initial candidate author head: 71b367d081ade2859aac474ac3d4f5a3ca748a6e.
Tree: 391f5c6429c60bcc82e97b4d9503cd43dc7fa869.
Base: dec32cb8ab48a575d563c5e4a1b10c80fc95c486.
Both clean host worktrees checked that exact fetched head before running. Both mr99-native-author wrappers exited 0 and drained.
These are valid targeted results for 71b367d, not proof that its later full profile passed or that the new head is fully verified.

| Check | Native Windows | Native Linux |
|---|---|---|
| Restore/build | Release 0 warnings/errors; retained locked restore from baseline setup | locked restore and Release build passed |
| Model | 10 passed (8 vectors, real exit and generated real sequences) | 10 passed |
| TaskControlTests | 15 passed | 15 Windows-only skips, 0 executed; not Linux control proof |
| Host AOT | win-x64, 0 warnings/errors | linux-x64, warnings-as-errors, passed |
| Launch faults against native helper | 18 passed | 11 passed, 7 Windows-only skips |
| Native node phase crash/recovery | 3 passed | 3 passed |
| MR-100 native preemption/legacy/retry regression | 4 passed | 3 passed |
| Changed-file format and diff check | passed | passed |

Commands and complete output remain in:
- Windows C:\MyFile\Projects\dev\logs\mr99-native-author.{ps1,out,err,exit}.
- Linux /home/sammiller/arcforges/logs/mr99-native-author.{sh,out,err,exit}.

The early PR author summary's Linux TaskControl wording was clarified after reading every per-class summary:
[clarification](https://github.com/ArcForges/ArcForges/pull/52#issuecomment-6403467637). Skips are not reported as executed passes.

## First full-profile failure and cancellation receipt ordering

The full Linux profile at 71b367d failed after 136 s at linux-ci. Node.Core reported 257 passed, 47 Windows-only skips and one failure:
ACancelAfterARestartInTheMiddleOfTheLaunchOfAStartingAttemptEndsTheCommandThatStartsLate. The original assertion required the
restarted node to see a command enter after its forced stop, but it observed none. The actual result was CANCELLED/HAPPENED with an
exit-record-written SIGKILL outcome. Store-schema, publish, native tools/closed-loop, benchmarks, package, exclusive tests and startup
gate were not run. Read summary: 20261026-052053-71b367d081ad-linux. This run is not a complete Linux pass.

Diagnosis from the original test and implementation: the old synchronous Stop initiated the forced phase before CancelTask replied.
The new asynchronous stop path returned void, so the handler could reply and the fixture could release its real pending start before
the stop had armed late-start observation. Targeted standalone tests had passed because their timing did not always expose this gap.
The first direct self-review at 71b367d missed it and is superseded by the corrected validation and final-head review.

StopAsync now returns its recording/platform-initiation task. The real API handler and caller-bound cancellation await it before
replying/logging completion; shutdown awaits it as well. Internal enforcement/preemption callers deliberately schedule it and
finalization awaits the same task. No original test, late-start assertion or timeout was weakened. A new real RPC regression holds
the actual platform stop behind a fixture release file after STOPPING commits, asserts the cancel response is still incomplete and
the live result absent, releases the stop, and requires CANCELLED/HAPPENED. The fault is test-mode-only and bounded to 60 s; normal
production execution never reaches the hold. Its fixture releases it in finally.

Current corrected head: d86b89ce1a0670cfdc6b9dd3fa43260c967f9f6e; tree 9fd0e767d5f06e56647c0226b8bbf772cf84d8af.
The Linux causal negative control changed only the handler to discard StopAsync rather than await it. The new real RPC barrier test
failed explicitly with "CancelTask replied before the durable stop's platform phase began" (1 failure, test exit 2). The mutation
was restored from Git before the fixed build; the same test then passed. This is a causal negative control, not a passing baseline.

The exact-head Linux author wrapper mr99-reply-author exited 0. The original two-lane ci suite passed, including the previously
failing late-start test (Node.Core 258 passed, 47 Windows-only skips, 0 failed, 42.348 s). Host linux-x64 Native AOT passed with
warnings-as-errors. Against it: launch faults 11 passed/7 Windows-only skips, native phase/reply class 4 passed/3 Windows-only skips,
and MR-100 native recovery 3/3 passed. Changed-file format/diff passed and the worktree was clean. Negative-control logs remain in
/home/sammiller/arcforges/logs/mr99-reply-before.{out,err,test-exit}; author commands/results in mr99-reply-author.{sh,out,err,exit}.

The old-head Windows profile at 71b367d completed 13 steps/1055 s; all 13 summary results were read. Its success was retained only as
historical evidence and did not satisfy the corrected head gate. Windows final-head checks ran strictly after that job drained:
Release build 0 warnings/errors, model 10/10, TaskControl 15/15, Host win-x64 AOT 0 warnings/errors, native-helper launch faults 18/18,
native phase/reply class 4 passed/3 Linux-only skips, MR-100 native recovery 4/4, changed-file format/diff passed. The
mr99-reply-author wrapper exited 0. The final profile began only after that result, through native background process dependencies
that checked live process identity and completion records; no competing build/test and no blind failure rerun.

## Final post-push gate and records

Final head d86b89ce1a0670cfdc6b9dd3fa43260c967f9f6e; tree 9fd0e767d5f06e56647c0226b8bbf772cf84d8af; base dec32cb8ab48a575d563c5e4a1b10c80fc95c486.
Both complete native profiles ran after the push at this exact head. Every selected summary result was read and passed:

- Windows full: 13 steps/1023 s, 20261025-214217-d86b89ce1a06-win.
- Linux full: 16 steps/1183 s, 20261026-053350-d86b89ce1a06-linux.
- Both required exact-head arcforges/windows and arcforges/linux statuses were success; owner-hosted checks were skipped as configured.
- [Final direct self-review](https://github.com/ArcForges/ArcForges/pull/52#issuecomment-6403660689) covered all 8 changed files and the
  receipt-order correction/causal regression; no findings within the managed-execution repair. No independent review claimed.
- Fresh PR head/tree and source main were checked immediately before merge. Actual source merge: 47ec7aa38b3c8a7431862ad98b6c0b3c6ddcf8e5.
- Final gate comment: https://github.com/ArcForges/ArcForges/pull/52#issuecomment-6403923701.

Windows logs: C:\MyFile\Projects\dev\logs\mr99-final2.{out,err,exit}.
Linux logs: /home/sammiller/arcforges/logs/mr99-final2.{out,err,exit}.
All native jobs drained. No old-head status, partial leg, skipped test or negative control was substituted for this gate.
The maintenance row and completion ledger note were updated only after the actual source merge.

The future AF-DIST-02 acceptance now includes live FINALIZING and nullable pending stop intent across update/rollback. It remains
planned: no updater, database migration, cross-version settlement implementation or real older/newer-reader validation is claimed.
The future compatibility note and open MR-105 observation were appended only with the Plan CLI. Completion was appended through
the same CLI after the source merge; no task state was activated or rewritten.
