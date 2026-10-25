# MR-105: kind-guarded synthetic adoption lifecycle

## Scope and authority

MR-99 repaired launched attempts. MR-105 reconciles the separate synthetic ADOPTED task/attempt lifecycle already described in
architecture 04 section 10 and adds the missing cancellation journal event. Adoption creates one already-running attempt;
it does not launch a command or collect a parent exit status. It cannot be queued, paused, preempted or retried.

[Design#32](https://github.com/ArcForges/ArcForges-Design/pull/32) merged first as
772435e591339a0c94ec34832bbebe5b94094a57. Reviewed head f3b43e34f2d5c0e568a73d5c507e16eaf0a13518, tree
a5b4442f27c7ec69e17eaa3d3f0df14268d271fc, base 376c6e9b3b895e75ef3e486623e0b16ad931161f.

The canonical machines now guard initial RUNNING by ADOPTED kind. Ordinary task/attempt initial states and managed FINALIZING
requirements remain intact. Cancellation records and journals RUNNING -> STOPPING, then FINISHED CANCELLED/HAPPENED once the
container is empty. Natural disappearance ends LOST/UNKNOWN, as does missing-container/changed-boot recovery of a live adoption.
Neither path invents an exit code or managed finalization work. The generated reference renders initial guards; checker regressions
reject incomplete, extra and empty declared guards. Architecture 04 and AD-0004 were amended.

Design author generation/check passed with protoc (25 files), both SQL schemas, 19 state machines and zero errors; 47 tool tests
passed with 20 Windows platform skips; diff clean. Final native full Windows: 3 steps/24 s,
20261025-231335-f3b43e34f2d5-win. Linux: 3 steps/46 s, 20261026-071331-f3b43e34f2d5-linux.
All six results and both exact-head required success statuses were read, owner-hosted check skipped as configured, runners exited 0.
Fresh main/head/tree checked before merge. [Direct self-review](https://github.com/ArcForges/ArcForges-Design/pull/32#issuecomment-6404743228)
and [final gate](https://github.com/ArcForges/ArcForges-Design/pull/32#issuecomment-6404753124).

## Before-fix evidence

Test-only source head f010977e2d0ccd165ecdae3f326ed314ae823766, tree bd2be394db55bf77e6dbaf18edb3fed5ff8d7ba7,
keeps production code unchanged at main 4990f63f33bcf36855e184e4e8c4d3b8d7bde003. Linux fetched it through Git into its native
worktree. Locked restore and Release build passed, zero warnings/errors, build 15.21 s. One real cancellation regression ran
with no skips and failed as expected in 2.117 s (test exit 2): the FINISHED event reports previous STOPPING, while the real journal
last reported RUNNING. The cancel command had persisted STOPPING but never emitted its event. The wrapper captured that expected
failure and exited 0; it is not a successful regression or complete profile.

The regression adopts its own same-user TestLoad process, runs a separate ordinary task in the same real journal, issues two
cancels and checks result reason/effect, one attempt, no exit code, exactly one STOPPING event, initial events without previous
states, sequence/revision continuity and no adopted FINALIZING. Existing natural-disappearance and missing-container-after-restart
tests also feed their actual events through the same kind-guarded model. Fixture cleanup stays within its own node/units/processes.
No fake process, clock or event stream substitutes for this behavior.

Before logs: /home/sammiller/arcforges/logs/mr105-before.{sh,out,err,test-exit,exit}. No formal profile ran on the test-only head.

## Diagnosed intermediate check

Candidate 864531c0351f26f21565991ca96005e5d65a2c55 contained the production fix. Its Linux affected adoption class reported
3 passes/1 failure, no skips, 2.232 s: the cancel regression now passed, while the newly added restart-event check incorrectly
reused an API cursor from an older stream generation. EventJournal.Open deliberately increments generation on a node restart;
ListEvents correctly requires reset. The corrected test asserts that reset, reads the actual persisted TASKS journal spanning
both generations, and retains all state/result/sequence/revision assertions. No production behavior or bound was weakened.

The Windows full leg had been started before the Linux affected author result. It was interrupted once the candidate became
obsolete: a host-local control helper verified the exact runner command/process tree and all members of its private console,
then delivered one Ctrl+C. The verification engine performed its own step cleanup and reported arcforges/windows error
(KeyboardInterrupt), not success; the outer wrapper's interrupted execution produced no exit record. A fresh process inventory
confirmed no old runner or build/test workload remained before new author work started. The first control-helper attempt
returned exit 1 without captured diagnostics and had no observed effect; the second used file diagnostics, exact console membership and one recorded
delivery. No arbitrary process, system manager or global process-name kill was used.

Intermediate author logs: /home/sammiller/arcforges/logs/mr105-after.{sh,out,err,exit} (exit 2).
Obsolete Windows formal logs: C:\MyFile\Projects\dev\logs\mr105-final.{out,err}; these are interrupted, incomplete evidence.
Final profiles must run afresh on the corrected pushed head.

## Author and final source evidence

[ArcForges#54](https://github.com/ArcForges/ArcForges/pull/54) merged as 54e0809d7386f1ec24c39cd4ec1a4fc90f35177a.
Final reviewed head: 3c16d263d22cd2777dbba6f72f852a1fa0811f4d.
Tree: 140798f0d9d717c15964e213a051674a41819d29.
Base: 4990f63f33bcf36855e184e4e8c4d3b8d7bde003.
Three files: one missing production journal event and two actual lifecycle regression/model files.

Final-head Windows author checks passed: Release build with zero warnings/errors, changed-file format/diff, model 18/18 JIT
and 18/18 native-helper, task control 15/15, Host win-x64 Native AOT zero warnings/errors. Each adoption run executed 0/4:
three WMI-created candidates were already in a job and one test is Linux-only. These four skips in each mode are explicitly
not successful Windows adoption evidence; AR-19 remains Open and now includes the cancellation/journal procedure.

Final-head Linux affected adoption class passed 4/4 JIT in 2.264 s and 4/4 native-helper in 2.388 s, no skips. The lifecycle
model passed 18/18 JIT in 5.102 s and 18/18 native-helper in 4.977 s. Release build and Host linux-x64 Native AOT had zero
warnings/errors; format/diff passed and worktree clean. The corrected restart test asserts API reset and validates actual
persisted events across both generations. All real before/after, continuity, reason/effect and cleanup assertions remain.
The node in these author tests runs in the test process; native-helper mode uses the actual native launch helper for the
ordinary task sharing the journal. A full native-node adoption runtime claim is not inferred from that author coverage.

Author logs: Windows C:\MyFile\Projects\dev\logs\mr105-author2.{ps1,out,err,exit};
Linux /home/sammiller/arcforges/logs/mr105-after2.{sh,out,err,exit}. Both author wrappers exited 0 and drained.
[Author evidence](https://github.com/ArcForges/ArcForges/pull/54#issuecomment-6404895324).
[Final exact-head direct self-review](https://github.com/ArcForges/ArcForges/pull/54#issuecomment-6404895644):
all three files and the generation-correction delta checked against the merged Design; no findings.

Both complete native post-push profiles passed on this final head:

- Windows full: 13 steps/1109 s, 20261025-232921-3c16d263d22c-win.
- Linux full: 16 steps/1356 s, 20261026-072914-3c16d263d22c-linux.
- Every selected result was read and passed, including JIT/native exclusive suites and startup gates.
- Both required exact-head arcforges/windows and arcforges/linux statuses were success; owner-hosted checks skipped as configured.
- Fresh main/base, PR head and tree checked immediately before merge.
- [Final merge gate](https://github.com/ArcForges/ArcForges/pull/54#issuecomment-6405126852).

Final formal logs: Windows C:\MyFile\Projects\dev\logs\mr105-final2.{out,err,exit};
Linux /home/sammiller/arcforges/logs/mr105-final2.{out,err,exit}. Both runners exited 0 and drained; no competing build/test
or old candidate/partial run/skip substituted for these complete profiles. After the actual source merge, the list and CLI
ledger completion were recorded. Windows successful adoption remains deferred, no task or future feature was activated.

No enum/RPC/package/schema change or database migration. No real credential-store or orphan-file operation; MR-16 remains blocked.
No user systemd manager termination, daemon-reload or pkill -f. AF-REC-01 and later feature tasks remain unstarted; no LAN/cloud MCP.
All work and review are by OpenAI Codex alone under the user's explicit instruction; no independent review is claimed.
