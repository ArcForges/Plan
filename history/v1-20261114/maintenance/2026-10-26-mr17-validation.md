# MR-17: Windows node-gap memory-notification evidence, 2026-10-26

MR-17 is fixed. [Design#36](https://github.com/ArcForges/ArcForges-Design/pull/36) merged first as
9da4127003a90842ddafeb03a6f07e7c5877f34c. [ArcForges#57](https://github.com/ArcForges/ArcForges/pull/57) merged as
852d23d8b4daca78cef509cb7a6925b18795b6b1, reviewed head92235c31a30d7434a3abe78c09083c3bd507bf9e,
tree8013bd2effc7df38b2c14000b073f2a5f643ccd0, base5fa2ad5fe77bef791b96db11129b3851fe55c940.

## Diagnosed defect and repair

A final live violation query is not durable history. If a different notification/accounting query runs after an allocator
released its memory, the holder can later see no job_memory even though the attempt crossed its enabled notification
threshold while the node was down. Existing fallback compares peak only with the higher hard commit cap, so a peak
between notification and hard thresholds is missed and recovery reports EXITED on a nonzero exit.

JobObject now queries the actual job's enabled notification threshold (zero when disabled). At exit the holder compares
its existing durable peak with that threshold and adds the existing job_memory marker on a strict crossing. The original
hard-limit fallback and Outcome's nonzero-exit guard remain; exit0 is still EXITED. No new polling loop, enforcement action,
enum/RPC/package/schema/migration or data-key/credential operation. QUERY rights/interop types already exist.
Design AD-0005 and04 section7 specify the node-gap rule and same-user guardrail. Evidence is a notification crossing,
not proof of an allocation refused by a hard cap. MR-18's correlated/nested-limit classification/detail questions stay separate.

## Discriminating native Windows before/after

Three test-only stages keep production unchanged from5fa2ad5:
- 110d67cbc20690d4abc756ec8c461cd5bdbeff6b:4/4 pass with unread notifications still retained. This did not reproduce the defect.
- eee443d4d83904e1297829720edd05a093a74f3b:5/5 pass; a query while allocation continued could be followed by another notification.
  For example one query saw168570880 bytes but the eventual peak was220999680. These are retained diagnostic iterations,
  not discriminating failure evidence and not a repaired-code validation.
- 9ec49397236f7f792778d111688121fa7c1504fa (treefc5e0391c77801991e89a0ad81401eb20a9bde9d): a second conditional gate
  confirms the allocator process exited before the observer queries and before the root exits. Release build0 warnings/errors
  in11.87 s; testexit2 with2 failed recovery reasons (expected MEMORY_LIMIT, actual EXITED) and3 controls passed,
  no skips,13.413 s; outer wrapper0/drained. No fixture-precondition failure was counted as the defect.

The two failed cases had peaks307466240 and221958144 bytes, notification thresholds268435456 and167772160, hard
cap402653184. Both peaks were far below the original hard fallback; the changed-limit peak was below the startup
notification value. Post-release queries reported68698112/68698112 and64135168/64200704 bytes; flags and exit-record
job_memory were empty. The controls retained EXITED for zero exit or no crossing, and MEMORY_LIMIT when a notification
had not been consumed. Original bounds/assertions were retained in the fixed tests.

The final5-case regression uses real in-process NodeHost stop/restart across generations, native jobs/holders, actual
committed allocation, real queries, file gates and durable exit records. Only external key storage is isolated under the
test policy. It deliberately avoids relying on allocation refusal: a controlled nonzero command exit plus threshold
evidence exercises the specified normalization. No fake samples/events/exceptions or fixed timing releases.
The new test is isolation=exclusive with DisableParallelization and runs with parallel none.
The AOT variant uses the published holder; the node remains in-process. No new standalone native-node crash claim.

## Final-head author evidence

| Check | Native Windows | Native Linux |
|---|---|---|
| Format, Release build, analyzers | pass,0 warnings/errors;13.21 s build | pass,0 warnings/errors;15.64 s build |
| New node-gap regression | JIT5/5,no skips14.204 s; AOT holder5/5,no skips14.094 s | Windows-only behavior; no inferred Windows pass |
| Affected TaskControl class |15/15,no skips77.887 s | unchanged Linux behavior |
| Affected JobTests class |8/8,no skips15.263 s | Windows-only behavior |
| Repository guards |72/72,no skips3.130 s |72/72,no skips0.982 s |
| Pure format/protocol tests | covered by full profiles |14/14,no skips0.628 s |
| Host Native AOT publish |0 warnings/errors42.22 s |0 warnings/errors48.56 s |
| Final format/diff/clean checkout, author wrapper |pass,exit0 |pass,exit0 |

Exact scripts/logs: C:/MyFile/Projects/dev/logs/mr17-before{,2,3}.ps1/.out/.err/.exit,
mr17-author.ps1/.out/.err/.exit; Linux /home/sammiller/arcforges/logs/mr17-author.sh/.out/.err/.exit.
The affected Windows mixed classes were run alone for their exclusive/memory-sensitive methods; no repository
parallelism setting changed. Existing keys/fixtures clean up only their own isolated temporary data.

## Final pushed-head gates and direct review

Design headcd2ed1367d9479eaf70dab78bf20cd5b291e9045, treee0fab623ef594f531e9bc5293fc0309b4113eb10:
complete native Windows3 steps/12 s and Linux3 steps/45 s passed. All six results, runner exits0 and required exact-head
statuses were read with fresh main/head/tree before merge. [Design review/gate](https://github.com/ArcForges/ArcForges-Design/pull/36#issuecomment-6407178689).
Design summary IDs:20261026-025257-cd2ed1367d94-win and20261026-105249-cd2ed1367d94-linux.

Source final head92235c31a30d7434a3abe78c09083c3bd507bf9e: complete native Windows13 steps/1163 s and
Linux16 steps/1364 s passed. All29 results, both wrapper exits0 and engine-reported exact-head success
statuses were read; owner-hosted checks skipped as expected. No competing same-host build/test, altered assertion/step/hook,
old-head pass or partial run substituted. Windows summary20261026-030042-92235c31a30d-win;
Linux summary20261026-105858-92235c31a30d-linux. Both hosts use native MCP, no SSH/WSL/container substitute.

[Author evidence](https://github.com/ArcForges/ArcForges/pull/57#issuecomment-6407264108),
[direct self-review](https://github.com/ArcForges/ArcForges/pull/57#issuecomment-6407264417),
[final source gate](https://github.com/ArcForges/ArcForges/pull/57#issuecomment-6407498149). Full three-file review checked actual job threshold/rights, strict crossing,
disabled threshold, unchanged zero-exit/hard fallback, real released-memory and changed-threshold preconditions.
OpenAI Codex alone under explicit user instruction; no independent reviewer or other agent/model claimed.

Only after actual source merge, update MR-17 to fixed and append the owning AF-EXEC-01 note through Plan CLI.
No task-state/later-feature activation. MR-16 remains blocked; MR-07,MR-11,MR-15 remain deferred/unresolved.
After MR-17:36 disposed,65 open,3 deferred,1 blocked of105,69 unresolved total. Report those counts and continue MR-18.
