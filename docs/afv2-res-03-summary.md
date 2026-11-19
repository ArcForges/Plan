# AFV2-RES-03 resource admission and pressure response

## Implemented scope

Sandbox Core coordinates Node and Sandbox concurrency, native hard resource grants, and measured resident memory reservations before releasing a V2 Run. A request that cannot fit receives a durable `budget_unavailable` result with the applicable `ArcError.State.Reason`. Replaying the same request preserves the decision and its effect certainty. The numeric admission proof stays in the private native receipts.

The coordinator uses a fresh resource frame to divide available CPU between active Sandboxes and Runs by weight, within their configured ceilings. A prospective admission can reduce an incumbent’s CPU grant in the same native scope. The coordinator verifies the native readback before confirming the combined reservation and releasing the new Run. Subsequent rebalances use the confirmed reservation as their baseline and apply hysteresis.

Sustained critical memory pressure can request a bounded Stop through the existing owner after checking the Run’s policy and eligibility. The coordinator waits for verified native drain and a fresh inventory without that Run before selecting another victim. The pressure termination reason is recorded when the native owner confirms the scope is empty. Linux retains its cgroup hard memory limit and verified Stop path. Optional live `memory.high` control is unavailable on the qualified H-22 path because a write on the verified kernel can block in synchronous reclaim. This task carries forward the existing MXC profile qualification and egress evidence boundaries.

## Exact delivery

Node PR107 merged at `8584ef28c2666d8d809cbe842b006889b36b9e0a`. The merge tree `2dc78a7d02ce2c6e93cd89a3a642b0f86a6b6c86` matches independent review and native verification of `96ce91e7d561c45068e5ec54dad779d587abc365`. Each designated host fetched the exact PR head independently and ran the unchanged full profile with evidence collection enabled for every step. Both required GitHub statuses succeeded. [Node PR107](https://github.com/ArcForges/ArcForges/pull/107)

| Host | Full profile | Installed package | Original summary and SHA-256 |
| --- | --- | --- | --- |
| Windows deku | 15/15 in 2908 seconds | 14/14, zero skips, 93 files | `20261120-030545-96ce91e7d561-win/summary.json`, `469ae9da324236471571da00b35cce064a4ed0c61f2370c0290a9d72220dd428` |
| Linux H-22 | 20/20 in 2427 seconds | 14/14, zero skips, 88 files | `20261120-030610-96ce91e7d561-linux/summary.json`, `65e90721177c3900eee1c6dd7881b4c52c7346e1b2fc43b19358889cd632f117` |

Paths in this section are relative to the corresponding Node repository’s `.git/arcforges-verify/logs/` directory. Both profiles ran the native closed-loop suite, the verified installed MXC package, both exclusive suites and the startup comparison.

| Host | Verified archive SHA-256 | MXC manifest SHA-256 | Package log and SHA-256 |
| --- | --- | --- | --- |
| Windows deku | `6974b24d10e433bd3b8d8e645018dfbc29b83023fa2a406633b4b3734f13b40f` | `e48fbe86e837ae38f2a73cdbeae8e03604861970ba5ee6c3dddf2f69cc8a6997` | `20261120-030545-96ce91e7d561-win/win-package.log`, `21f8c43eb82520a57a39786d67ada7826282ee425ac6f27e7bf215f929e18833` |
| Linux H-22 | `9cc45ed2b6360ad0ddc74208a5e8fcea39064034606c145b0b2d627a2cd0f9ea` | `d8d93ba3c2565f45b415443e7603260a0de96a095b3c2c6439237adce36e2e2b` | `20261120-030610-96ce91e7d561-linux/linux-package.log`, `61ec7c437626b44645ad24ce49a595c7fe842b4cc44bb895e16f87f45fbd5d6f` |

The installed tests exercised concurrent Start refusal and durable replay, separate resident reservations, incumbent reduction before a new Run starts, native weighted CPU recovery, and verified drain after the single authorized pressure Stop. The nonpreemptible peer remained running, and a new admission after recovery required a fresh intent. The full profiles passed the inherited restart cases with original process exit observed before reusing the Node instance.

These are verified development archives. No public release or activation was performed.


## Initial native qualification

Both hosts installed the build from Node commit `daad97027ace6263e717a50ec06e68ee9db53cff`, tree `512990aa2fc01b81462359684b250eb3413d7adc`. The paths below are relative to `.git/arcforges-verify/launches/` in each host’s Node repository.

| Host | Installed native checks | Original log | SHA-256 |
| --- | --- | --- | --- |
| Windows `deku` | 13/14 passed, 0 skipped | `res03-author-daad97027ace-win/native.log` | `b41c18febbefcdbd9d7c83c20bf5fdacb7d8c659d773cb1b42a774e97f18a43f` |
| Linux H-22 | 10/14 passed, 0 skipped | `res03-author-daad97027ace-linux/native.log` | `3c9e429039687f28cd48827337ea51c1187fccc64f6482cf1270e79058576bb1` |

- The parallel Starts test compared the full durable refusal across calls on both hosts. The recorded mismatch was the per-call `error.correlationId`. The command, owner epoch, aggregate, refusal reason, `FAILED` state, `DID_NOT_HAPPEN` effect, retry disposition, and timestamp agreed. The repaired assertion checks each returned correlation against its own request and compares the remaining durable fields across the original call, replay, and reconciliation.
- The H-22 pressure test observed `stopped` where it expected `pressure_preempted`. The source correction recognizes both `stopped` and `user_stop` when a pressure Stop is already recorded and the native exit confirms an empty scope.
- The H-22 continuity test’s initial boundary observation read a `cpu.max` quota of `585300` against the expected `620000`, equivalent to 5,853m and 6,200m at a 100,000 μs period. The 347m difference was below the host’s 400m hysteresis threshold. Source review found the scheduler could use a measured startup budget as its baseline before it had established the confirmed active reservation. The log does not establish which sample occurred before or after admission. The correction anchors the first cohort at the confirmed reservation and preserves a later confirmed increase as a baseline for reductions.
- The H-22 Pipes test observed `terminal_ack_unavailable` at explicit EOF, which leaves delivery `UNKNOWN`. A timing race with payload exit is plausible. The same installed product and test passed the isolated Pipes case 1/1 with zero skips. Its log is `res03-pipes-daad97027ace-linux.bCbNMr/run.log`, SHA-256 `2eb3a9b6d93c1bd30c9ea14331e6735dbb7d16f645e1bd8c9b65edfa8e592a43`.

## Isolated admission evidence

Both hosts repeated `InstalledParallelStartsReserveOneSlotAndNeverQueueTheRefusedRun` with the corrected test fixture blob `8e816748e09ea526179b49ae756d8d555c0b458e` and the unchanged installed `daad97027ace` product. Each run passed 1/1 with zero skips. The tests recorded 128 MiB reserved and 64 MiB of measured resident admission headroom when a separate 128 MiB request was refused. The native hard grant was 128 MiB. Each host also read back the same incumbent’s reduced CPU grant before confirming a separate explicit grant.

| Host | Verified incumbent and separate grants | Isolated log | SHA-256 |
| --- | --- | --- | --- |
| Windows `deku` | Incumbent 400m → 299m, separate 99m grant | `res03-author-daad97027ace-win/corrected-admission-fixture.log` | `05e066f40eceb02e47c7e76eb00053ac672c7b97d79c042854252f8c9d3f803e` |
| Linux H-22 | Incumbent 400m → 300m, separate 100m grant | `res03-admission-fixture-daad97027ace-linux.ehfds9/native.log` | `a563b1eb5891dd21191860799c1b8f2a5d81dcb032aeecb4e6aa419e3fd79a46` |

## Second native qualification

Node candidate `48640048ba42148d3361d5dc7f32e016bac221f1`, tree `8e7dac0c67b12f898c583913f535163fc7eb6104`, incorporates the per-call association assertion and both source corrections. It received independent source review and passed 28 focused local tests. [Node PR107](https://github.com/ArcForges/ArcForges/pull/107)

| Host | Installed native checks | Original log | Log SHA-256 | Installed archive SHA-256 |
| --- | --- | --- | --- | --- |
| Windows `deku` | 14/14 passed, 0 skipped | `res03-author-48640048ba42-win/native.log` | `5200d6d9ea4f48a8b1db3a855b45b409569ab2449af046b9d73fd1cf0305ae1a` | `32d97b8b974cc6d2b980fad0354f399955d87471405143d26f77f4281edb7f5e` |
| Linux H-22 | 11/14 passed, 0 skipped | `res03-author-48640048ba42-linux/native.log` | `650642872d2c754672ddaca8a798b8b1a8cde2a5e2da21d84f10029ebcae2515` | `4ef9ebf91581f86fcfa726880f64315b6503d5c016e7f9aecdde451c15441bd3` |

- The original H-22 pressure test measured 6.842 s from the fixture’s independent physical pressure detector to Stop, exceeding its 4.25–6.25 s assertion. That interval included the time for Node to observe Critical and the persistence window after observation. The corrected fixture checks both intervals separately.
- The full H-22 Pipes test again received `terminal_ack_unavailable` at explicit EOF. The exact build retains delivery uncertainty. The two full-run errors and the isolated success remain distinct observations.
- The H-22 continuity test read a live 5,604m CPU grant while its assertion still used the 6,200m startup grant. The 596m reduction exceeded the host’s 400m hysteresis threshold, which is 5% of host CPU capacity. The live reduction is permitted and remains enforced by the native scope. The fixture needs separate assertions for immutable startup proof and current authorized native limits, along with existing owned identity, survival, and drain checks.

Plan PR190 scoped only the two existing installed-test files for continuity and explicit EOF. It merged as `a9a4509b7a5b09e8bde488e764086dba1716d25b` after Plan validation passed 5/5 on both hosts against the same Design revision. The original required checks and evidence remain applicable. [Plan PR190](https://github.com/ArcForges/Plan/pull/190)

## Isolated pressure evidence

Both hosts passed the pressure case 1/1 with zero skips using pressure-only test fixture blob `9151fc1a00ac4c7ec1afd9152a599b9f9d79b8c2` and their unchanged installed `48640048ba42` product. The fixture bounds the independent detector-to-first-raw interval at 3 s. It separately requires 4.25–6.25 s from the contiguous raw Critical transition to effective Critical and to the authorized Stop. Node’s pressure log records transitions. An intervening noncritical raw transition resets the persistence anchor. The effective transition and Stop must identify the same scheduler sample.

| Host | Physical crossing → raw Critical | Raw → effective Critical | Raw → Stop | Isolated log | SHA-256 |
| --- | --- | --- | --- | --- | --- |
| Windows `deku` | 247 ms, sample 13 | 4,988 ms, sample 18 | 5,210 ms, sample 18 | `res03-author-48640048ba42-win/corrected-pressure-fixture.log` | `04d8d12b66f0fa85cac9c730a588c29fb9e03e78d37edce24f86b2523fc3daa3` |
| Linux H-22 | 1,713 ms, sample 17 | 4,995 ms, sample 22 | 5,169 ms, sample 22 | `res03-pressure-fixture-48640048ba42-linux.kffMsV/native.log` | `efc8ef101ae199e7b0b5b2570efa4638c9b80395f93050827431005f9f8d36e7` |

Both isolated runs confirmed one verified native drain with the durable `pressure_preempted` termination reason. Both peer Runs survived the pressure event.

## Isolated recovery and EOF evidence

Both hosts passed the continuity and maximum binary Pipes cases 2/2 with zero skips. The overlay changed only the test fixtures and used the same installed `48640048ba42` product archives recorded above.

| Host | Isolated log | SHA-256 |
| --- | --- | --- |
| Windows `deku` | `res03-author-48640048ba42-win/tracked-recovery-eof-overlay.log` | `9c97efac287801c4e405dcd48752e6a244ac9f870b6d77f821d806fa71bafd05` |
| Linux H-22 | `res03-inherited-fixture-48640048ba42-linux.w86fqF/native.log` | `2303a16e845437874007da97d0a5893a01b40c0e4addc388ac734d986053caa7` |

The Linux continuity fixture verified the immutable launch identity and a 6,200m authorized ceiling. It read 5,263m with a 100,000 μs period on the same held cgroup. The quota and hard memory limit agreed with Node’s effective readback. The older owner and child remained verifiable through client disconnect and Node loss, and the Run drained as expected. The 5,263m proof carried `native_readback_confirmed`, which identifies the observed grant without asserting a later weighted update.

The Linux Pipes fixture held the payload scope open after native EOF until the client collected its acknowledgement. It confirmed explicit EOF, an exact 65,536-byte binary echo, a verified empty native scope, and an original exit code of 0. Windows passed the same byte and EOF checks using the existing echo payload.

## Frozen source for formal validation

The independently approved Node PR107 head is `efa8cbf33619f27eeb906d27ca5915722012a1f4`, tree `8768746616f9e1c055ad80e9cd5d094b4850822f`, with parent `48640048ba42148d3361d5dc7f32e016bac221f1`. The change from that parent is limited to the three existing test fixtures below. The full PR changes 22 scoped paths relative to the RES-02 baseline. [Node PR107](https://github.com/ArcForges/ArcForges/pull/107)

| Fixture in `tests/ArcForges.ClosedLoop.Tests/` | Git blob |
| --- | --- |
| `MxcRunServiceTests.cs` | `ad8fee9171e59509e82702f5f512ab35cfd1dcfc` |
| `PressureMxcRunServiceTests.cs` | `9151fc1a00ac4c7ec1afd9152a599b9f9d79b8c2` |
| `TerminalMxcRunServiceTests.cs` | `f520ba65bb6db673c96d33578b8abec8d64b122a` |

## First H-22 formal attempt

The first H-22 formal run of `efa8cbf33619` reported failure at `linux-closed-loop-native`. Thirteen of the 20 profile steps had passed and six later steps remained unrun. The native step reported 44 passed, one failed, and 19 skipped. The original results are retained under the H-22 Node repository’s `.git/arcforges-verify/` directory.

| Receipt | SHA-256 |
| --- | --- |
| `logs/20261120-024045-efa8cbf33619-linux/summary.json` | `0baecb8bd524587af3867fccf434a7576a5c7b54314435c3bcd12e24abb78ef7` |
| `logs/20261120-024045-efa8cbf33619-linux/linux-closed-loop-native.log` | `26b13b5fa901741beeeee59982a4be6dadc153c56a00976764919d39b0c8737c` |

The inherited `LinuxWorkerInterruptionHostTests.StoppedOwnedNodeCannotResumeAnExpiredWorkerAndPartialEffectRemainsUnknown` case failed before the second raw Node process became ready. The previous process logged `node.stopped`. The next process exited with code 3 before a readiness descriptor appeared. The CLI Stop command waits for the socket to stop responding. Node can still be closing SQLite and releasing the single-instance lock after the socket stops. The exit code maps to `AlreadyRunning` in the unchanged Node startup path. An overlapping lock interval is the source-based diagnosis. The failed start retained no new Node stderr to confirm the specific lock refusal. The inherited fixture, NodeHost, and single-instance implementation are unchanged in this candidate.

The unchanged case passed an isolated retest with the actual AOT binaries from the same source, 1/1 with zero skips in 17.260 s. It observed the worker’s SIGKILL, preserved the partial effect as `UNKNOWN`, and verified the alias hold after restart. The retest log is `launches/res03-native-worker-efa8cbf33619-linux.OEXLa4/native.log`, SHA-256 `e6073f2396b0e8bd376b5cc0a2a1ac3acd39507fa05934c7237cdd0357ec13cc`.

## Windows formal attempt and H-22 full retry

The Windows formal run of `efa8cbf33619` passed nine steps and failed `win-closed-loop-native`, leaving five steps unrun. The failing step reported 42 passed, one failed, and 21 skipped. The inherited `PlanRemovalInputAuditHostTests.SignedRealHostReadsAndReplaysTheOriginalInputObservation` case saw the original endpoint stop and the second raw Node process exit with code 3 before publishing a new descriptor. The previous Node logged `node.stopped`. This reproduces the same observed stop-to-restart ordering as on H-22 in a separate inherited test.

The stock H-22 profile ran again at `efa8cbf33619` with `--keep-going` and reproduced the worker fixture’s exit 3 before readiness. It also completed the installed native package suite with 14/14 passed and zero skips. The archive SHA-256 was `ec68abd202003dfa1480ff588ae14f243dbda187d87e7ed93be3cafa8e69b602` and the MXC manifest SHA-256 was `925ad812d8923d838b5e8de7362858104ff4a4215a83ec41a64fb2f52323bb7a`. After the scope review and package drain, the coordinator gracefully stopped this retry’s reporter. The exclusive step had started and was interrupted. The reporter posted `arcforges/linux` as incomplete with `KeyboardInterrupt`. The stopped retry has no final summary and the installed package pass is only one profile step.

| Host | Receipt under `.git/arcforges-verify/` | SHA-256 |
| --- | --- | --- |
| Windows `deku` | `logs/20261120-024044-efa8cbf33619-win/summary.json` | `3851a9715c250308af96f9acb3509ada4b27eaacb2e208c356fd0177ea61583a` |
| Windows `deku` | `logs/20261120-024044-efa8cbf33619-win/win-closed-loop-native.log` | `029bcb017f61fe8ff996624f718c26480ae2c72ec10dca95b12c20e349010520` |
| Linux H-22 | `logs/20261120-025242-efa8cbf33619-linux/linux-closed-loop-native.log` | `acbe88855b2916683848121ef44cc41f91445a2cde65524aa7fc06ddb45dfa0c` |
| Linux H-22 | `logs/20261120-025242-efa8cbf33619-linux/linux-package.log` | `74e9ea0af2a61f2d43e7d929721e97c3bc9320a62b411a366b0bd31990bedd79` |
| Linux H-22 | `launches/verify-res03-efa8cbf33619-linux-retry/reporter.log` | `74c14a385837d12fc8286f64a5c1b0f41770b9afb92d0de8af0f740af1ebbe71` |

Plan PR191 scopes the two exact restart fixtures. The proposed change waits up to 15 s for the already-held original Node process to exit successfully before making the single fresh Start. The signed input audit, replay, partial `UNKNOWN` effect, and cleanup checks remain required. Plan verification was underway when this evidence was recorded. [Plan PR191](https://github.com/ArcForges/Plan/pull/191)

## Restart fixture scope and cleanup

Plan PR191 head `0ef7d71e7e62328496ab3ea366bd880c6602cf43` passed 5/5 on both hosts against Design `6aa869670f8e1acbe8578d5ed231f3e4c17d1c3e` and merged as `55fb2657ff1c520afe48b9e01efed45305767b57`. [Plan PR191](https://github.com/ArcForges/Plan/pull/191)

| Host | Plan receipt under `.git/arcforges-verify/logs/` | SHA-256 |
| --- | --- | --- |
| Windows `deku` | `20261120-030040-0ef7d71e7e62-win/summary.json` | `1943190760fa57f23637c4d5fc5adc1d66767f34443c11af758249bba29a9cad` |
| Linux H-22 | `20261120-030301-0ef7d71e7e62-linux/summary.json` | `69079650ecd6706c38df12e4dd633fd5c1309b0b30ccf2d4850b6bbdcd8799f0` |

The interrupted H-22 retry had left its owned JIT exclusive session and detached fixture attempt units. The coordinator confirmed their ownership and drained them. The final receipts show no remaining session processes. The inspected units were inactive with no main PID or populated cgroup, and none of the original owned processes remained.

| Node cleanup receipt under `.git/arcforges-verify/launches/` | SHA-256 |
| --- | --- |
| `verify-res03-efa8cbf33619-linux-retry/exclusive-drain.log` | `1dfc236d132c37145b143ef65ba9d7b0c6329861ffa3c5c4205cfc970a0bf0ef` |
| `verify-res03-efa8cbf33619-linux-retry/exclusive-units-drain.log` | `45abd8f1cd68638fdc42039d12a572b4b58bcec1902efdd969ece263a24b5020` |

## Isolated restart evidence and latest reviewed source

Each corrected fixture passed 1/1 with zero skips against the unchanged `efa8cbf33619` formal AOT binaries. Each confirmed the original Node exited with code 0 before starting a fresh one. Windows continued to verify the signed audit and replay the original input observation across restart. H-22 observed the original worker’s SIGKILL, preserved the real partial effect as `UNKNOWN`, and verified the alias hold after restart.

| Host | Node evidence under `.git/arcforges-verify/launches/` | SHA-256 |
| --- | --- | --- |
| Windows `deku` | `verify-res03-efa8cbf33619-win/owned-exit-audit-fixture.log` | `99fe552573a972753ee305da45fd634e5897a7b8f4427d600ded9b165bf0c831` |
| Linux H-22 | `res03-worker-fixture-efa8cbf33619-linux.YHdqXW/native.log` | `e10d21aab6add09e6e78bd42ea132004c8981c9042be4fc1730e1711b59fa1ef` |

The latest independently reviewed Node PR107 head is `96ce91e7d561c45068e5ec54dad779d587abc365`, tree `2dc78a7d02ce2c6e93cd89a3a642b0f86a6b6c86`. Its parent is `efa8cbf33619f27eeb906d27ca5915722012a1f4` and the only changes from that parent are the two scoped fixtures below. The cumulative diff from RES-02 covers 24 scoped paths. [Node PR107](https://github.com/ArcForges/ArcForges/pull/107)

| Fixture in `tests/ArcForges.ClosedLoop.Tests/` | Git blob |
| --- | --- |
| `LinuxWorkerInterruptionHostTests.cs` | `535d69569501b58a63b63b281335bac0849bb175` |
| `PlanRemovalInputAuditHostTests.cs` | `6a7277002fa36b9b209c447c89c6bbdcd8e80053` |
