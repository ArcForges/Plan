# AFV2-MXC-02 partial native evidence — 2026-11-17

## Current status — 2026-11-18, after Plan160

MXC02 is active at Node PR95 source dcd91f63a8ce96863c4f9384d66292759550175d,
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
were cleaned by the fixture. A same-source full Linux retry follows; the targeted
pass does not replace the required profile or erase its original failure.

The committed H22 peer is independently fetched from GitHub and controlled over
SSH. Ordinary Windows calibration has failed on the measured defaultIPv4,
existingIPv6 and socket-selected physicalIPv4 paths, with peer counters0/0 and
explicit peer cleanup confirmed. These are original failures before any contained
network case; they establish neither an SSH outage nor a sandbox policy result.
WIN04/06 and one final68-case receipt remain incomplete. No host network/proxy/
security setting changed. The [handoff](../codex-handoff.md) and draft PR95 carry
the exact stage/source/receipt identities and current diagnostic next step.

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
