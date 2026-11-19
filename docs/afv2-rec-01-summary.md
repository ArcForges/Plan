# AFV2-REC-01 native ownership and recovery verification

## Reviewed candidate

The independently reviewed Node PR108 head is `648fb7c0c9b2cefec03939e257b0e37734059b78`, tree `452bddb6405a47f46bd31e46dab05100df2a3dda`. The Node baseline is `8584ef28c2666d8d809cbe842b006889b36b9e0a`. The Plan comparison is `41fb9aa40ab8a057ee1bb5bbee43aa69c8372b85` and the Design comparison is `6aa869670f8e1acbe8578d5ed231f3e4c17d1c3e`. [Node PR108](https://github.com/ArcForges/ArcForges/pull/108)

## Formal verification and merge receipts

Each host fetched the exact PR head from GitHub into a separate native worktree and ran `python eng/verify.py run-and-report --rev 648fb7c0c9b2cefec03939e257b0e37734059b78`. H-22 used its native systemd user manager, cgroup v2 and PTY under the designated account. Private H-22 receipts used `umask 0077`.

| Host | Required profile result | Installed MXC result | Original summary, package log, and artifact identities |
| --- | --- | --- | --- |
| Windows `deku` | 15/15 passed in 2906 s | 32/32 passed, zero skips | `20261120-055727-648fb7c0c9b2-win/summary.json` SHA-256 `60681ab060fc552ece60d8699404c93bdd2e7a4e39968d03754c9b7f185f2e10`. `win-package.log` in the same directory SHA-256 `e3ce6a99d43c778e62dbde91ee4cd1c13afa0dccffc8ab013d2e6bf82c0ece76`. Product ZIP `406ca2c6e3f40a4ed23de42dc35d260c883a0092daa2baf2aa77f4209d891646`. MXC manifest `94c1d89d0e5c00a18cba983d8ee9a8157286b076dddb82557e30a1ea5472d5f3`. |
| Linux H-22 | 20/20 passed in 2465 s | 32/32 passed, zero skips | `20261120-055824-648fb7c0c9b2-linux/summary.json` SHA-256 `7565002f5d9b704f9d02313b9662859fa72e8fa9df96ef285a2dc451cc28509a`. `linux-package.log` in the same directory SHA-256 `59aeabd87d821690d65a1707d6c9860e32dede2c19ba9ae830f8a583ed17e9aa`. Product archive `33a8a2eadc18a72dddfa9b2fd60b89be4a0caf89561396ef50d206b86e940086`. MXC manifest `91d4d7248898891d9dda2c5f225ecb5ab20930d118e723df97e6fd375f529be4`. |

GitHub received `arcforges/windows` and `arcforges/linux` success for the exact reviewed head. An expected-head merge of Node PR108 produced `1b9bdb5288964ff763cd3f7da6260bdf39742466` with the same independently reviewed tree `452bddb6405a47f46bd31e46dab05100df2a3dda`. The merged change is development delivery. The merged commit had no GitHub Actions publication run at verification. Public activation remains scoped to PROD-01.

After the H-22 formal reporter exited successfully, the distinct manager re-execution case passed 1/1 with zero skips against the exact same verified archive and compiled tests under the repository’s exclusive lock. It used the package and manager test opt-ins and the exact `InstalledRecoveryKeepsOriginalRunThroughUserManagerReexec` selector. The original service invocation and cgroup, supervisor and payload identities were unchanged. The same Node completed a new native Run, then stopped the original Run and verified its scope was empty. The raw log is `rec01-manager-final-648fb7c0c9b2-linux/native.log` under Node `.git/arcforges-verify/launches/`, SHA-256 `28df8294cb4f1a3635d7ed21ab025961f81b4b57382c8d594a2632b0b1aa32ff`.

The first formal candidate `08008fe` failed both legs in the same carried architecture test. `TheRunControlSocketsUseAuthenticatedLocalPeers` still expected the former source spelling of the Linux address helper. Windows recorded five passed, one failed and nine not run. H-22 recorded ten passed, one failed and nine not run. Neither leg reached its installed package stage. Plan PR196 scoped the exact existing fixture so it could continue to check a single AF_UNIX socket, the private descriptor address, peer birth and image before handshake, and now explicitly check both original connection and rebind. [Plan PR196](https://github.com/ArcForges/Plan/pull/196)

| Original formal result | Relative to Node `.git/arcforges-verify/logs/` | SHA-256 of summary | SHA-256 of failed CI log |
| --- | --- | --- | --- |
| Windows `08008fe` | `20261120-043001-08008fe05fa5-win` | `5603b4a1734227d9d8e55cd2c70bec0a8499447a17c88c7bf521fda362de987b` | `c29227189c52a247812153b5032ace8b1a6a13cf6795986514819b1518e20fac` |
| H-22 `08008fe` | `20261120-043002-08008fe05fa5-linux` | `ba32ba4d934dc7082732a3c4a7cb7d9ac91433efb7b968daf164a6fa929f8ee7` | `42263de498e7c0da8bd7323a4550ec8aa291107618dbb6ef63a6bab7858e609d` |

## Implemented scope

Node startup reconciles nonterminal Runs before readiness. Rebind verifies the retained Run, launch, boot, process birth, supervisor image, and native scope identities, then advances the control generation. The original supervisor retains its native Job or cgroup, hard resource controls, and output cursors. Rebind invalidates terminal writer leases and acknowledgement authority. The original Start is never activated again. A pending Stop keeps its original command, reason, and deadline. Terminal registration requires a verified native drain or a durable witness that preparation never began. The Stop effect can remain `UNKNOWN` even after independently verified drain. Ownership uncertainty retains `RECOVERY_REQUIRED` and blocks conflicting use.

Schema 17 appends the Run and Stop recovery witnesses to the preserved migration history. `GetOperation` reads the exact original owner epoch and command, including compacted identity and retained `UNKNOWN`, through a single read-only projection. The durable authority accounts for reserved Stop and grant revocation capacity separately from new nonsafety effects. Coherent restore verifies outside authority and refuses an older database missing later admitted command history. An empty Store stays without a V2 owner epoch after startup recovery and operation lookup.

Local `Configure.repair_error` requires the exact owned root, current revision, and no active use or unresolved effects. `Delete.resume_command_id` authorizes a distinct successor against the original journal, root, and quarantine phase. `GetOperation` can still observe the original unresolved receipt. FILE-02 owns the native destructive stages and client integration. V1 Task and Attempt paths remain available to their existing consumers until qualified migration cutover.

## Installed author results

These are exact author checkpoints on the native development hosts. Log paths are relative to each host’s Node `.git/arcforges-verify/launches/` directory.

| Node source and tree | Host | Installed result | Original log | SHA-256 |
| --- | --- | --- | --- | --- |
| `92330eafe642fbc451b0b0b5ac1292e39a13badb`, `ae7ce98bbb6d1eeeb018147775e5f34edbec8c07` | Windows `deku` | 0/24 passed, zero skips | `rec01-author-92330eafe642-win/native.log` | `98f2831020501ae3cd8bf50be7c8a9e1f5663de3e9589098a9131180965823e9` |
| Same initial source | Linux H-22 | 15/24 passed, zero skips | `rec01-author-92330eafe642-linux/native.log` | `11b650a1aecde030650c7b832214fd09bf1ca9ed01f21ba32fd43d4f947598e1` |
| `d5c2e4cc185a97414cce7cd682d752dd2e539c6e`, `343f365cb37ccaabe17afab5cfaa3752fbabafe3` | Windows `deku` | 23/24 passed, zero skips | `rec01-author-d5c2e4cc185a-win/native.log` | `1c5b354d3f216662bcb1a52e4eb8d541dd1e59d5088a7386008fb1e0cda48e57` |
| Same corrected source | Linux H-22 | 24/24 passed, zero skips | `rec01-author-d5c2e4cc185a-linux/native.log` | `688c364e81ef20c0f1e3aab5a212045cb3c4ee68e7113af31db7d91a28292feb` |
| `22075ac0d6eb96142b2e1b7dd3ff2f583dbb7278`, `6f07d23a0b7abba885502f22158214c730232f09` | Windows `deku` | 30/32 passed, zero skips | `rec01-author-22075ac0d6eb-win/native.log` | `0db92004c9db8d9259e7fa9adea779ac885d4bd111fb3a142b4bd3aa396f2292` |
| Same expanded source | Linux H-22 | 30/32 passed, zero skips. Separate manager test reached same-owner re-execution evidence, then failed before the probe Run. | `rec01-author-22075ac0d6eb-linux/native.log` | `cc2d27a8589428c9b4345bfb1161df3769c25ebd1655e953a13230e325219cfb` |

- The first Windows cohort repeatedly observed `EntryPointNotFoundException` when the Job handle comparison bound to the wrong DLL on the workstation. The source changed `CompareObjectHandles` from `kernel32.dll` to the observed `KernelBase.dll` entry point. Dependent lifecycle, terminal, and receipt checks failed with it. The prepared-owner fixture also needed the exact trusted-image/ACL arrangement and an xUnit runner invocation supported by the deployed runner. The original log retains the `unknown option: --filter-method` refusal.
- Eight of the nine initial H-22 failures were boot identity fixture comparisons between the raw Linux boot UUID and the persisted boot UUID plus machine witness. The remaining failure saw seven occupied ordinary slots where the saturation scenario expected eight. The correction isolates the actual durable Configure admission and settlement, so an ordinary committed edit fills the intended slot while preserving already-promised Stop and revoke capacity.
- The corrected Windows cohort’s remaining failure compared a mixed-separator fixture image path with the canonical path read from Windows. `08008fe` normalizes that one test path. The targeted fixture passed 1/1 with zero skips against the unchanged `d5c2e4c` installed product. Its log is `rec01-integrated-retest-win/breakaway-normalized-native-d5c2e4c.log`, SHA-256 `4b949e33e2d53ad6503a397024ab98d52c096e6c2a0c41fb0ce786eb55f92ab9`.
- The expanded author suites each failed the two interrupted Start checks that compared the complete operation error envelope using separate query correlation IDs. Both original identities and effect outcomes agreed. The revised fixture repeats one exact query and retains full operation equality. The initial H-22 manager re-execution witness retained the original invocation, main process birth and cgroup after real reexec. The subsequent probe failed when its Sandbox reused the same display name, so no fresh probe or final original Stop evidence was accepted from this attempt.
- Independent review found that two terminal recovery tests opened the crashed store with the writer before the first true restart. The amended tests verify the missing clean-shutdown marker and hash the original signed observation through read-only access before startup. After the actual restarted Node stops, they authenticate the original observation and compare its bytes. Their earlier success is retained as diagnostic evidence for the earlier test design.

Both hosts independently used the pinned Microsoft MXC 1.0.1 binary archive, SHA-256 `0e832239454ba7fcd338ff56218a287eef4c0a01c1484084b869f55feff8abe9`. The archives in this table are the resulting product packages. The manifest digests identify the staged official MXC compositions.

| Node author source | Host | Package archive SHA-256 | Staged MXC manifest SHA-256 |
| --- | --- | --- | --- |
| `92330ea` | Windows | `b78864a22f2d5dce1862c58843d8fb2f2ddcf2862fb16feda64b78d6429d5e9c` | `0aab67d0b39d15c962616e5576d4d7241cfb1ed3e7320bf86d9a1aad36c0f5f1` |
| `92330ea` | H-22 | `52eb683c9b14f0cd277fa15b80d3a684b573b79182b3e0e01c94b52fd541449f` | `35b16151c24885fa28d48cb631f27c3b10222ebb01134565911de8be11d93faf` |
| `d5c2e4c` | Windows | `c908717ad7bc933ea9db045522f343fdb7cb78163bde34c4433fb24e192beeca` | `f208bb51ccfe34141427c8f3dbc81ed86d9c509203645ea814955724a4cff048` |
| `d5c2e4c` | H-22 | `1484cbd95da57565425d987a6b39ee7e5a81955dd332a06d708491669184fd16` | `b5fa00824c03a93ee3590739a59467d43c0e025e344908a91fc155f257e33094` |
| `22075ac` | Windows | `0a9f573849d61608a3f04aef959d09607e1efccde54f1731c3b33f0f49b0335b` | `785429ab9c606b74f61307b3db8d7156f495aa098f59af43299173dc5610070c` |
| `22075ac` | H-22 | `c1bc90e62ae1fc7a48dc5247e4870d7eb3451936bc2ca694c7734b0b76ef6fc7` | `8053c154cfd975f66d4576931a25d8dacd7ed82e76747e60c838187164059f24` |

The `648fb7c` fixture-only delta was run against the previously verified `22075ac` packages before the exact full verification. The focused repeat passed 5/5 on Windows and 6/6 on H-22, each with zero skips. The log directories below are under Node `.git/arcforges-verify/launches/` on their own hosts.

| Targeted native result | Original log | SHA-256 |
| --- | --- | --- |
| Windows Start handoff 3/3 | `rec01-retarget-648fb7c0c9b2-win/InstalledRecoveryNeverReleasesAnInterruptedStartHandoff.log` | `33be405b06f603cfddd3d8f38a6396dfa8a81491e6bd73c21563c49cb49f19d0` |
| Windows worker final 1/1 | `rec01-retarget-648fb7c0c9b2-win/InstalledRecoveryRetainsTheOriginalEffectWhenTheWorkerFinalPrecedesNodeCommit.log` | `0775ca6b1a3e78dd1ccfdf520c92e12bd10ff7bcad98852b54bffaa11bbd91f8` |
| Windows root and descendant 1/1 | `rec01-retarget-648fb7c0c9b2-win/InstalledRecoveryVerifiesTheOriginalScopeWhenItsRootExitsWithADescendant.log` | `7d2b93f09337becd6c3a1a760266eaeae8ca2675a1d15076bfd987f35f735747` |
| H-22 Start handoff, worker final, root and descendant, user manager re-execution 6/6 | `rec01-retarget-648fb7c0c9b2-linux/native.log` | `94f7613ffda945de72ababb94d8ba04672e6a53950405462d705814e077165c4` |

| Windows author checks | Result | Original log and SHA-256 |
| --- | --- | --- |
| Store suite | 170 passed, two Linux-only skips, exit 0 | `rec01-integrated-retest-win/store-applicable-win.log`, `0806bbce09d7a12c3944a27ca1240991a6fbf76bc878609ef54a4fae66a55485` |
| Focused Core recovery | 7/7 passed, zero skips | `rec01-integrated-retest-win/core-recovery.log`, `db4fc426627c0c4cd156892445b263b34d5710c7303139fdb52b0dbc4d2f4f1b` |
| Sandbox registry and remote grant behavior after atomic Configure | 19/19 passed, zero skips | Windows isolated author transcript `b5aefe`, no separate log file |

Before REC-01 timing checks on H-22, two remaining native units from ended, failed RES-03 author runs were matched to their original executable, PID and creation records, invocation, and cgroup. Both exact units stopped and their originally held cgroup entries were removed. The prior failed author reports remain intact. The clearance receipt is `rec01-old-res03-drain.e57AkF/units.log`, SHA-256 `bb0a70b6fa2c00b5dda8f5b0a8d4c8352a1bf39d8348a7e282b1c1f9d42789af`.

## Native evidence and limits

- The installed restart scenarios kill Node while the exact owner and payload are alive. They check new control generation, unchanged Run and launch identity, live hard limits, compacted Start replay, and Stop of the original scope. An interrupted Stop keeps the original deadline and receipt. A parallel stale-identity fixture keeps an unrelated process alive through recovery and confirms unresolved effects survive ordinary retention and restart.
- Windows tests exercise the same owned native Job through duplicated handle rebind, refuse a child’s attempt to leave the Job, and require native drain. If both original Job holders are lost, an independently observed exit of the test processes can coexist with a product `RECOVERY_REQUIRED` state because the original Job is unavailable for verification. Linux tests stop the exact original transient unit and verify its cgroup. The opt-in H-22 case also re-executes the real user manager, confirms the same invocation, held cgroup and original process births, completes a fresh Run from the same Node, then stops and drains the original scope.
- The installed Node is killed before the Start receipt, after durable admission before native preparation, and after authenticated native owner binding before release. The fixtures retain each actual admitted identity and verify zero payload in all three windows. A separate prepared-owner test exercises authenticated Stop before `Activate`, yielding signed `NOT_STARTED`, consumed handoff, an independently empty native scope, and no numeric exit.
- Additional cases kill the Node after release dispatch, between durable Stop intent and signal, after forced Stop dispatch with a verified native final still uncommitted, and while an original final exists before Node reconciliation. In each, independently retained native observations and durable identity are compared before accepting an effect or retaining `UNKNOWN`. The background descendant case witnessed an admitted child in the original scope before root exit. In the observed Windows and H-22 rematches, the native child was no longer live after root completion and the original scope drained. The exact terminal fallback remains conservative when the scope can no longer be reacquired.
- The reboot cases substitute prior-boot witnesses and verify the native reconciliation branch, no fabricated numeric exit, no second payload, and no signal to the unrelated process. No physical host reboot was performed. Terminal cases verify new writer authority, no replay or durable input records, and continuation from an original output cursor with a retained-range gap.
- The saturation scenario uses a real live native Run, persisted active grant, the local handlers, and the actual SQLite and protected-key history. It checks ordinary refusal, reserved Stop and revocation, exact `UNKNOWN` observation, a coherent restore, and startup refusal for a stale database paired with current authority. Enrollment setup uses the bounded existing fixture input. No external provider or selected external egress observation is inferred from this test.
