# AFV2-MXC-02 partial native evidence — 2026-11-17

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
