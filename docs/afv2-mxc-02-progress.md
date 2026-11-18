# AFV2-MXC-02 partial native evidence — 2026-11-17

## One native Windows run covering the 59 workstation cases — 2026-11-18

[Node draft PR95](https://github.com/ArcForges/ArcForges/pull/95) now collects
the workstation cases before starting the external network peer. Previously
an unavailable peer could stop the full profile before the CLI, lifecycle
and six workstation network cases ran. The `--only local` selection runs
those groups together without starting a remote peer. Full mode retains
the original 68 case names, protocol assignments and admission checks.

The author worktree is `.worktree/afv2-mxc-02-local-qualification`.
Locked restore, Release build, formatting and `git diff --check` passed.
The native Windows worker built commit
`cb0396b3d93b9afaf0629630f2020358a353bf53` in detached worktree
`.worktree/m02-local-cb0396b`. The Native AOT publish produced zero errors
and warnings. The existing staging script verified the official Microsoft
MXC 1.0.1 distribution and all ten staged files. The worker ran the
published `--windows-profile` with a fresh work directory, manifest,
report and `--only local`.

| Artifact in `artifacts/native-cb0396b/` | SHA-256 |
|---|---|
| `local.json` | `d7708eae1ba1c11e31f5625343c38c89af3006791c13b2b588cb68edc0180eac` |
| `local.json.events.jsonl` | `b5027b61d9b5b424e6d335aaa9476b3c5058756816b153b9a3f18caedaa02a0c` |
| `stage-run.log` | `27243e7aebcdc852b7c50f57560aa15dba475f9302fa5a800b6e90f9d5a9a206` |
| Published probe | `9c64c6531f3a1fb1b5af7d5b957358b892f07fd4a58c2b029f8fb22052c655d1` |
| Stage manifest | `d085ab0dbdaba95b6038e695cbf066381e63124140ca2c7d69eb53943d85cb9f` |

Run `232a29c0a9444c28963fa1da05f0ef6a` on deku passed 59 distinct cases
in 59.851 seconds, with confirmed cleanup, observed driver Job context
and matching stage identities before and after execution. The protocol
counts were WIN01 7, WIN02 15, WIN03 9, WIN04 13 and WIN05 15.
The probe returned 2 and recorded partial qualification.

For host-loopback egress, ordinary TCP and UDP each advanced the peer's
receive and match counters from 0 to 1. With host loopback denied, both
counters stayed at 1 on each channel. The workload exit codes were 70 for
TCP and 124 for UDP. In all four inbound cases the payload listener
reported ready and default ingress was denied. With host loopback denied,
neither listener observed a request and the host received no matching
reply. With host loopback allowed, both listeners received the request and
the host matched both replies.
The six observations are retained with their SHA-256 digests in the receipt.
An independent reviewer matched all six observation and policy files to the
receipt, checked the ten stage files against the manifest and verified the
59 cases against their original protocol assignments. The reviewer traced
the source review from the earlier full PR review through both subsequent
changes, including the final three-file delta and tree
`3aeff44d353b016c9a2352262ac938b78c9f49b5`. The coordinator posted
the [independent review and native results](https://github.com/ArcForges/ArcForges/pull/95#issuecomment-6969263914)
on the draft.

Seven external WIN04 cases and two same-Run WIN06 scenarios remain open.
The previous direct-path and same-host measurements below apply to their
original locations. Read-only workstation and H-22 inventory identified
no additional controlled, independently reachable TCP/UDP peer. The
current inventory cannot establish ownership or reachability of an opaque
local virtual guest. The user identified no existing test endpoint.

The reviewer also checked the exact requests from the prior same-host IPv6
experiment against the pinned backend. Each selected request contained the
observed destination, protocol, port and exact /128, denied default egress,
denied ingress and denied host loopback. The backend derives the Internet
client capability from the nonempty egress rule. Its documented direct
egress model uses that policy shape. This rules out a missing explicit
Internet client capability in those requests. The zero-receive outcomes
do not identify the native layer responsible. See the [pinned helper
source](https://github.com/microsoft/mxc/blob/fda29ac63bc306b7f97f3b86b4b63d44f7f40cf2/src/mxc-sdk/src/backends/process_container/common/network_policy_helpers.rs#L19-L90)
and [official network model](https://github.com/microsoft/mxc/blob/fda29ac63bc306b7f97f3b86b4b63d44f7f40cf2/docs/backends/process-container/networking.md).

### Repository checks for cb0396b

Both designated hosts fetched the PR branch from GitHub, checked its exact
commit and ran `python eng/verify.py run-and-report` from detached
`.worktree/verify-mxc02-cb0396b` worktrees. Windows used the existing
English CLI setting. On H-22 the coordinator used the documented process
umask 0077 and redirected the detached reporter's output to its host-local
launch log.

Windows passed toolchain, toolchain tests, restore, base host and build.
The CI step then failed after 412.6 seconds. The other nine steps did not
run. Platform recorded 113 passes, one failure and one skip. It timed out
while waiting for the 13-process fixture to form, before the test issued
its termination request. Core recorded 743 passes, two failures and 105
skips. The 3000 ms launch-fault test observed 5.0504235 seconds against
its five-second cancellation deadline. The StopNode receipt test observed
a broken local pipe and gRPC Unavailable. GitHub received
`arcforges/windows=failure` (status 59217230792). The summary is
`20261118-120445-cb0396b3d93b-win/summary.json`, SHA-256
`bdaeafe5767b7de97d6ff61e9bcd97b10eebe8416125b495132eb36a0d496c88`.
The adjacent `win-ci.log` has SHA-256
`97f9be8c6cbe63c7d8e0bfbb6b83f9472f973d970f3fe3dd399838605410ad13`.

The new StopNode failure occurred while reading the gRPC response body.
The handler persists the receipt and signals shutdown before returning
it. The host subsequently stops the RPC service. The original log does
not establish which operation finished first. A targeted run of
`NodeServiceTests.StopNodeReturnsAReceiptAndTheNodeShutsDownCleanly`
on the same compiled Release binary passed 1/1 in 2.176 seconds with the
original timeout. The worker observed no new surviving test process or
test directory. The targeted summary is
`artifacts/stopnode-single-20261118/summary.json` in the Windows
verification worktree, SHA-256
`a1d3887bf247d9d9a59cae6dc36f65641747b42d8692e1fa0f17ca22d3a42d3a`.

H-22 passed all 20 steps in 2,087 seconds, including both exclusive suites
and the startup gate. The detached reporter posted `arcforges/linux=success`
(status 59218624276). The original receipt is
`20261118-120447-cb0396b3d93b-linux/summary.json`, SHA-256
`eb0b7da7830769532d412c59753fbb4c4379af3582e721a496b76d26dec3e2a1`.
The launch log is `launches/mxc02-cb0396b-native-01/reporter.log` under
the Git common directory's `arcforges-verify` directory.

## Native Windows diagnostic groups at 32e2ac1 — 2026-11-18

On deku, the coordinator's Windows worker rebuilt
`32e2ac1b6c9645b75f607bfc7a58bcb0d552c274` in detached Node worktree
`.worktree/m02-local-32e2ac1`. The locked Native AOT release build passed
with zero warnings and errors. The repository staging command verified the
official 1.0.1 package, release archive, signatures and ten staged files.
The executable SHA-256 is
`d33863e30358da137c014520d17eab04f310c1bae661b18615bdac69f6b1c590`
and the manifest SHA-256 is
`3e2e821b64e42406aca5e05b19718b475e43681b2e866ab8be8b5d158eaae043`.

The worker ran the published `--windows-profile` command serially, changing
only the diagnostic selection and the fresh work/report paths. The five
receipts record the same executable identity. Each records verified stage,
final identity, observed host Job context and confirmed cleanup. Each exited
2 with a partial result.

| Selection | Passed / run | Receipt SHA-256 |
|---|---:|---|
| terminal | 15/15 | `fa7b4ee6b07f7a50e3c775073050ae4790ff443f94cddd5524054e2433baddfa` |
| resource | 9/9 | `4f2b692d742f467effe6864927de920841822e6eacfd8ac1ebdb155e20eefc8b` |
| policy | 12/12 | `1bac37e3243021aaa5f5e1d22da7e84f5ca05fa096ebebfcf0ce49a2d689bc57` |
| cli | 2/2 | `b9c1298e1c5459dc3c243f82985feb6a80f5b1f0250a18319b45e18ff56f8f3f` |
| lifecycle | 15/15 | `9324ca406277473e88c7095257a03e645a4f0c414903d42ef1ea284e578a7595` |

The original receipts are `artifacts/native-32e2ac1/<selection>.json` in
that worktree, with adjacent launch records and event logs. The staging
transcript `stage-run.log` has SHA-256
`b1ae03c7f49086ca412a3f48042f30470db9bd37c7770c01419bc3a497704af9`.
These five receipts cover 53 workstation cases. The external network and
combined cases still require evidence in the full Windows receipt.

## Assigned IPv6 endpoint on the Windows host — 2026-11-18

At Node `dcd91f63a8ce96863c4f9384d66292759550175d`, a bounded diagnostic used
an existing non-loopback IPv6 address on the Windows workstation. The host
bound the test sockets to that address. Before and after the four native
cases, the host exchanged the expected bytes over TCP, UDP on the same
numeric port, and a second TCP port. Each exchange increased its own peer's
receive and match counters by exactly one. The peer saw no foreign requests.

All four requests used the pinned official executor, BaseContainer, denied
ingress and denied host loopback. Each workload recorded its network attempt.

| Transport | Default deny | Exact /128, protocol and port allowed | Peer receive/match deltas |
|---|---|---|---|
| TCP | Winsock 10013, exit 70 | Winsock 10013, exit 70 | 0/0 in both cases |
| UDP | 18 bytes sent, reply timed out, exit 124 | 18 bytes sent, reply timed out, exit 124 | 0/0 in both cases |

All four executors and observed payload processes exited. The peer sockets
closed and its thread exited. This diagnostic observed network effects and
process exit only. WIN04/06 and the full composed-Run qualification stay open.
The result applies to this endpoint and policy. The layer that rejected the
selected traffic remains undetermined.

The private report is `artifacts/mxc-02/local-v6-run-01/report.json` in the
Node worktree `.worktree/mxc02-local-v6-diagnostic`, SHA-256
`f28ba5094b075c3548bbacd53667ef24c6897e24c61ea6ca6d3b45c1b732680c`.
It records per-case policy hashes, before/after counters, process observations
and the staged executable hashes. All test traffic stayed on this workstation.
The private driver is `artifacts/mxc-02/local-v6-diagnostic.py`, SHA-256
`041e741ef5503b01e7d080bbb05dc72a34e7f175d5aa23ed91762a8ec6629850`.
It takes the assigned IPv6 address and a fresh output directory. Before
launching the first contained case it wrote `calibration.json`, SHA-256
`2d183ebf979335ca84064f369337884f3bae352ed0048a4d800312afe72ff0d3`.

The earlier local IPv4 endpoint used an RFC 1918 address. The
[pinned Microsoft network contract](https://github.com/microsoft/mxc/blob/fda29ac63bc306b7f97f3b86b4b63d44f7f40cf2/docs/backends/process-container/networking.md)
requires the bidirectional private-network capability for private traffic.
Setting `ingress.default=allow` would change the policy under test. A future
candidate for strict selected egress needs a controlled endpoint reachable
under the original ingress policy. The experiment design permits any topology
that demonstrates these effects.

## Calibration correction at Node 32e2ac1

The prior calibrator verified the echo bytes and endpoint health. Its success
path did not compare the actual peer counters before and after the exchange.
[Node PR95](https://github.com/ArcForges/ArcForges/pull/95) now retains both
snapshots and requires one receive and one match on the selected channel.
A counter read failure or a wrong delta preserves the failure and its
observations. The networking policy and I/O budget are unchanged.

The author ran a real local TCP listener, UDP on the same port and a second
TCP listener. Each passed 12 successive calibrations. A controlled extra
matching TCP request caused the counts to move from 1/0 to 2/2. The
calibrator refused the correct echo and preserved both snapshots. A disposed
endpoint preserved its original exception and cleared the previous success.
Original author log `artifacts/mxc02-calibration-test/native-loopback.log`,
SHA-256 `85c02dbcc6295cb0c0ce117524b7483325bddda918b4dafda58a6a06646b0304`,
in Node worktree `.worktree/afv2-mxc-02-peer-calibration`. Locked restore,
Release build, formatting and Windows x64 Native AOT publish passed.
A nonauthor reviewed the exact delta from `dcd91f6` through
`32e2ac1b6c9645b75f607bfc7a58bcb0d552c274` against the source and receipts.
The draft retains its open native acceptance. Independent selected-egress
success and a single 68-case composed receipt are outstanding.

The first H-22 formal run on `32e2ac1` used the SSH session default umask
`0002`. In the CloudLink suite, `ARealCliUnderARegisteredAgentRootCannotSubmitLocally`
created its temporary directory and the Unix socket server rejected the
directory's permissions at startup. The suite recorded 699 passed, one
failed and one skipped. The original formal summary is
`20261118-062427-32e2ac1b6c96-linux/summary.json`, SHA-256
`6b1d447fa1006e288431c45065c78984b751ec7a3cf5da39ee7c14ed14eb0d8e`.
The adjacent `cloudlink-original-failure.log` has SHA-256
`0ff55368cc449a5d0c5117400a9c206075498a71e5a6c7b309af7ae1806fbb3d`.
Running the exact test with the documented process umask `0077` passed 1/1
in 2.369 seconds, log `cloudlink-owner-only-targeted.log`, SHA-256
`7ec9cf5729a953c4426a62cd85207112e26c78a0fbe012e3ea222c996bb79f15`.
The full retry used that process setting and the same source. The older
`dcd91f6` pressure-test timeout has its own evidence and an unknown cause.

The retry in `20261118-063155-32e2ac1b6c96-linux` passed the CI suite and
the regular exclusive suite. After the foreground SSH session disconnected,
the reporter exited with `BrokenPipeError` and posted `error` before the
native exclusive suite, startup or summary publication. The complete
regular exclusive log has SHA-256
`c0e249adbdeb47f188bc2b605e60b34d56bf15683c50c03ffe3e5d30cc98decc`.
The next invocation runs the same command under `nohup` on H-22 with local
log redirection and umask 0077. Its launch log is
`arcforges-verify/launches/mxc02-32e2ac1-linux-detached-01/reporter.log`
under the Git common directory.

The detached H-22 run passed all 20 required steps in 1,981 seconds. Its
regular and native exclusive suites passed in 843.6 and 799.0 seconds, and
startup passed in 1.3 seconds. The source, host and result are recorded in
`20261118-065617-32e2ac1b6c96-linux/summary.json`, SHA-256
`5b7572fcd113960d0cf0333e6e59bf8f57842e95419d3e59b92aad93fb4e0168`.
The reporter posted `arcforges/linux=success` (status 59200509937) and exited.

On the first Windows `32e2ac1` run, the CI step reported three failures.
CloudLink's ahead-of-server clock test timed out waiting for its timers.
The Core priority test still saw a Running task after 60 seconds. The
3,000 ms Core cancellation case observed a command start during cancellation.
The original summary `20261118-062407-32e2ac1b6c96-win/summary.json`
has SHA-256 `4217e24991524a3146f0cfc461e91bf6ec1729868c3bffde951375a81eb568e7`.
The reporter's log directory retains both suite logs and three targeted
rerun logs. All four targeted cases passed on the same compiled binaries,
including both cancellation inputs. The reasons for the original failures
remain undetermined.

The same-head Windows full retry again stopped at `win-ci`. CloudLink
passed. Seven Windows Platform cases and one Core forced-root-stop case
failed in this run. The original summary
`20261118-063738-32e2ac1b6c96-win/summary.json` has SHA-256
`da3bf5f2b1f997d876b29754da9d7534c22c78bd24d532d720bbf074c259d57b`.

A separate diagnostic reran the original affected CI group on the same
Release binaries, with default project and in-project parallelism and
unchanged deadlines. Seven projects passed. Windows Platform reported
three failures and Core reported three. Three previously observed Windows
wait timeouts and the Core forced-stop deadline recurred. Whole-host CPU
use had 30-second medians of 88.24–88.89 percent near the observed failures.
Available physical memory stayed at or above 14,290 MiB across the run. These
measurements establish concurrent load. The cause of the timing failures
remains open. The diagnostic's `summary.json` has SHA-256
`ee160d638861fc5687f135456769faa7719f7daba92e0a8767bcd0b6e0861898`
under `.worktree/verify-mxc02-32e2ac1/artifacts/ci-suite-measured-32e2ac1`.

The same Windows Platform CI selection then ran alone with its original
in-project parallelism, trait filters and time limits. It passed 114 cases
and skipped one. The test runner reported 22.057 seconds. This result and
the concurrent 111-pass/3-fail/1-skip result localize a difference in test
conditions. They leave project contention as a possible contributor. The
standalone observation does not fulfill the repository's Windows status.
Its `summary.json` has SHA-256
`baae645bbdf9c2be02114ef3200ccebb3bde38ff6be5a8ee01d2a31c8db01ae7`
under `.worktree/verify-mxc02-32e2ac1/artifacts/windows-project-isolated-32e2ac1`.

## Earlier dcd91f6 checkpoint — 2026-11-18, after Plan160

MXC02 is blocked by existing AR-01 at Node PR95 source dcd91f63a8ce96863c4f9384d66292759550175d,
in `.worktree/afv2-mxc-02-resume`; Design main is41d25327841e6c88df639bbcb387682bd067f7a1.
The older parked-task and endpoint-decision wording below is dated history.
The owner resumed the full authorized graph. SSH only replaces Linux MCP as
transport to the same H22; it creates no extra network test, prohibition or
endpoint-approval gate. Implement the original WIN04/06 requirements.

Windows exact-head full required profile passed15/15 in2177s, including both
exclusive suites and startup. Receipt `20261118-040926-dcd91f63a8ce-win/summary.json`
SHA2567845d9fa55708176aec964e78487603ce9e27e83a5f3ee0b2a40e682df664560.
H22 full required profile failed17-pass/18-ran/20-required: the fourth protected
task in the pressure-response test did not enter Running within90s, before
pressure injection; later the whole exclusive step exhausted900s. Its two final
steps did not run. Receipt `20261118-040940-dcd91f63a8ce-linux/summary.json`
SHA256ede9129da912bb99457e46945083ece4dd699e81384e52d8b4838a105edaced6.
An unchanged targeted reproduction with bounded read-only diagnostics passed
1/1 in19.904s, including four running tasks, Critical, one preemption and Normal.
The queue was empty in all nine observations, so the original admission failure
was not reproduced and its cause remains UNKNOWN. Owned processes/units/data
were cleaned by the fixture. The same-source full Linux retry then passed20/20
in1991s, receipt `20261118-045655-dcd91f63a8ce-linux/summary.json`, SHA256
154a878b85a74ebd90515ba91f928069370de9a3481de9bced47df27c499acfd.
The reporter postedSUCCESS and exited. Both required repository profiles now
pass; neither they nor the targeted diagnostic erase the original failure or
replace the original complete Windows qualification.

The committed H22 peer is independently fetched from GitHub and controlled over
SSH. Ordinary Windows calibration has failed on the measured defaultIPv4,
existingIPv6 and socket-selected physicalIPv4 paths, with peer counters0/0 and
explicit peer cleanup confirmed. These are original failures before any contained
network case; they establish neither an SSH outage nor a sandbox policy result.
WIN04/06 and one final68-case receipt remain incomplete. No host network/proxy/
security setting changed. The [handoff](../codex-handoff.md) and draft PR95 carry
the exact stage/source/receipt identities and current diagnostic next step.

The earlier `terminal-integration-09.json` also contains the concrete local
assigned-IPv4 alternative with HostLoopback denied and exact IP/protocol/port
allowed. Ordinary peer calibration succeeded, but contained TCP returned native
10013 and UDP timed out without increasing peer counters. This rules out that
tested combination; it does not establish a universal prohibition on same-host
endpoints or add an external-peer approval requirement. Preserve those policy,
peer and payload observations rather than repeating the same unsuccessful path.

## Owner transport clarification — 2026-11-17, after PR151

The extra Windows-to-VPS direct endpoint prerequisite H-06 is retired. Code
transport and designated Linux execution use GitHub exact fetch over healthy
`ssh netcup`; stop further cross-host data probes. MXC02 is parked planned while
MXC03 continues as the sole active task. This does not turn any failed network
experiment into a pass or waive real selected-egress/full-combination acceptance.
The earlier H-06 references and measurements below describe the original
checkpoint and are retained as history, not a current port-opening request.


Full Windows qualification is not established. Source is preserved in [Node draft PR95](https://github.com/ArcForges/ArcForges/pull/95), branch `task/afv2-mxc-02`, current head `14886bffd3f66b59aa1f8fec83f0450f108e40b2`. Code checkpoint `4ca55dfc88a6d21caebbee1afd11f099b1914412` passed author compilation, targeted whitespace formatting and Native AOT publication with zero warnings; the following commit adds usage documentation. No latest-head formal Node host profiles, merge, publication or whole-profile PASS are claimed.

Node worktree: `C:/MyFile/Projects/ArcForges/ArcForges/.worktree/afv2-mxc-02`. Private original evidence is under `artifacts/mxc-02`. Official SDK/executor cohort remains 1.0.1/schema1.0.0; staged official bytes are unchanged. Design baseline is `af28dc6378d91d678870abc628362476611efa32`. Existing product launchers and all data/recovery guards remain.

## Observed author results

| Evidence | Actual result | SHA256 |
|---|---|---|
| `terminal-integration-08.json` | 43 cases:28 pass/15 fail; original failures retained | `6768d99f62dc1a135114f428723c6fe09f4072f615bca2aeaba57ccb08d51472` |
| `terminal-integration-09.json` | 50 cases:45 pass/5 fail; terminal and resource cases pass, remaining failures still recorded | `a6542249d1e042d9fb9fc8cd754a8dc5a0d11182c4bdf29896a816f4c7260e1e` |
| `policy-integration-10.json` | 12/12 policy/filesystem/refusal cases pass; diagnostic slice, not full admission | `253004c0a282026d5d53ce753c78a2a4a18f41602f8eb78c3505f31e69a235e7` |
| `lifecycle-integration-11.json` | 14/14 owner/client-loss, phase, root-exit, cleanup-failure and persistence cases pass; diagnostic slice | `2d197ca86b87b27a03190abf178465234edcc39031dfd6faed2d63dc06c76ddf` |
| `network-integration-14.json` | Peer ready, but ordinary Windows host calibration fails at TCP exchange with external accepted/matched counts0; no payload case ran | `ae1cc3f91df3401da6bfaba25cb925ad68623358b90b136fad2bef693e591bd9` |
| `peer-selfcheck-h22.json` | Same peer script on designated H-22 successfully exchanges TCP, alternate-port TCP and UDP; actual counters1 each, acknowledged cleanup and exit0 | `615d482d9bdaf7e87a523c0b8eebe8acdd67759f5d3d081e5c5683a0ba057055` |
| `peer-windows-data-path-measurement.json` | Separate15s ordinary-host timing diagnostic: virtual-interface TCP connect completes around15ms, receive times out, peer accepted/matched counts remain0; acknowledged cleanup | `b6709795ebc13693af444cba40a76aa96c11eb7cfd9a6499581ca67b50ef1c2e` |

Different probe revisions produced these slices; they are not one final qualification receipt. H-22 independently fetched source `f75d4de31425bfc19ff334bb5ddfaf41c4f2ff9a` into `.worktree/mxc02-f75d4de-author`, performed locked restore and compiled the shared probe with zero warnings. This author compile is not a required commit status or Windows-native evidence.

## Fixed causes and remaining condition

The five original Windows `0xc0000142` popups came from disabling Win32k for the AOT fixture. The explicit accepted UI policy now allows it while retaining the configured clipboard/injection restrictions. A process-local error mode preserves real native failures without desktop dialogs; no machine setting changed. Later native runs did not reproduce those popups.

Redirected-parent standard-handle inheritance required null standard handles with `STARTF_USESTDHANDLES` for actual ConPTY initialization. Bounded fixture observations prevent terminal redraw from destroying test records; they never become trusted backend state. Cooperative ETX is classified honestly as handler exit, native Ctrl exit or deadline escalation, rather than assuming universal graceful exit.

The remaining `conhost.exe` in lifecycle10 was identified by held process identity and native membership. `CREATE_NO_WINDOW` had still attached a hidden owner console. A detached background owner removes that console while retaining the separate workload ConPTY and before-resume Job assignment. Lifecycle11 proves the original owner-only and final-empty conditions without weakening them.

Network12/13 exposed an incorrect test-helper assumption: the existing SSH control connection reaches an IPv6 loopback address, which is not the VPS data endpoint. Read-only route/address discovery now binds the peer to its unique assigned global IPv4. Network14 then establishes a separate ordinary-host data-path limitation before any MXC payload is attempted. Native H-22 self-calibration passes. Windows uses the existing Mihomo route; no relevant connection log was found, so the drop cannot be attributed to a particular component. No proxy, route, firewall or security setting was changed. H-06 records only this narrow prerequisite; it does not block native builds or Linux qualification.

## Continuation

Preserve the draft, private original reports and unqualified profile. Do not merge or label the full task complete using these partial results. Once a reachable controlled data path is available, run network-only diagnostics, the required same-run combinations, and one final complete receipt. Then obtain independent final-head review and unchanged Windows/Linux host reports before ordinary merge. All future features follow the diagnostics-from-first-implementation instruction merged in Plan PR150.

## Latest resumption evidence — 2026-11-18

Node PR95 candidate57decb6315f7d0cdfaf7652a760092d6848e6161 has a reviewed
immediate-Job observation gate (no blanket rejection of inherited Jobs), atomic
final receipt publication, and a real log-sink failure test in the existing
lifecycle case. Its Native AOT build passed without warnings/errors.
`lifecycle-resume-02.json` passed15/15 with all cleanup confirmed; diagnostic
exit2 remains partial, not qualification. SHA256:
9936bf35f63b88c95d5f8905a0e2358274e95f70cdb0356c7e29db8e00cc7e28.
The log failure retained original HResult-2147024816, disqualified its negative
result and still completed native Stop/shutdown/empty-scope verification.

Earlier candidate8765ddb's `network-resume-01` passed8/13 only: HostLoopbackallow
allowed all five intended fine-egress denies. ReceiptSHA256
2bf9a3f162155c2b68651fc046a229a8eefcb14c82426a86f32f5e3b430e7565.
Strict policy-resume-02 passed12/12 as a partial diagnostic, SHA256
53fe08b9626fd0dbb244922fbf015458a280859279eb6d5e7cc0b5e65da18339.
No full profile or current-source merge gate is claimed. An independent-network
peer decision remains pending under the earlier stop on cross-host data probes;
GitHub/ssh netcup control and native host checks remain healthy and authorized.
The handoff names exact worktrees, stage and next action. Historical facts above
remain unchanged; H-06 has since been retired, as the current register records.
