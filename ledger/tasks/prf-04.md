---
task: PRF.04
status: delivered
recorded: 2026-09-28
claimant: af-20260928-p02
epoch: 1
---

# Local RPC under AOT: bidirectional named-pipe/UDS probe processes

## Evidence

- Implementation PR: [DesktopPlatform #84](https://github.com/ArcForges/DesktopPlatform/pull/84), reviewed head `af093eecdd58f279a7e010658825b632f822ca05`, merge `0514461b80dc0f5b81078937633cab861c7da48e`. Independent exact-head review by `platform_ui`: [comment #5866522597](https://github.com/ArcForges/DesktopPlatform/pull/84#issuecomment-5866522597), no source/scope/documentation findings. The review explicitly leaves macOS runtime acceptance outstanding.
- The exact-head PR gate [run 36398786705](https://github.com/ArcForges/DesktopPlatform/actions/runs/36398786705) passed all checks, including aggregate CI, native-win-x64, Linux/Windows Local RPC Native AOT compile, package validation, policies, provenance, reconciliation, reference checks, secret scan, and repository hooks.
- Normal main publication [run 36400330513](https://github.com/ArcForges/DesktopPlatform/actions/runs/36400330513) completed successfully on merge `0514461b80dc0f5b81078937633cab861c7da48e`, including candidate CI and publication of the same verified repository bytes. PRF.04 adds a non-packable test host and produced no task-owned NuGet package.
- WP-06.01 contribution delivered: the published `win-x64` Native AOT probe ran two real processes over HTTP/2 named pipes (`CurrentUserOnly`) on Windows. It verified bidirectional generated Challenge/Confirm, OS-observed PID plus instance/installation/launch binding, same-user spoof refusal, disconnect and retained-owner-session reattach, malformed-input refusal followed by valid same-channel recovery, cancellation, bounded messages, and concurrent/fenced/expiry lease behavior. The repeated post-Darwin run passed: owner PID `25284`, restarted peer PID `27756`, fresh B2 instance/launch tuple accepted.
- Darwin source support: both Unix-socket client and accepted-server identity paths dispatch through an AOT-safe `getsockopt(SOL_LOCAL, LOCAL_PEERPID)` backend; Linux retains `SO_PEERCRED`. The pure selector check passed in managed and published Windows Native AOT modes for Linux and macOS dispatch plus ambiguous/unsupported fail-closed cases. Apple API constants are documented against the [Apple XNU header](https://raw.githubusercontent.com/apple-oss-distributions/xnu/main/bsd/sys/un.h#L81-L89). This selector check is not an actual macOS socket/runtime test.
- Continuous-proof contribution: the existing main workflow retains Linux/Windows Local RPC AOT compilation and package/static gates; the merge publication run passed those checks. No hosted runtime test was added.
- Local validation used pinned SDK 10.0.400 and the workstation build-slot: locked restore, format verification, Release build (0 warnings/errors), Win-x64 Native AOT publish and runtime probe passed. Dependency policy passed for 47 NuGet coordinates/225 inputs; all 16 dependency-policy tests, reconciliation (7 owners, 67 projects, 166 historical entries, 326 directories, 7 native records), provenance (499 tracked files), and `git diff --check` passed. No package or lock files changed.
- Untested coverage: actual Linux and macOS process-to-process runtime runs were not performed on this Windows host. In particular, Darwin `LOCAL_PEERPID` has not been exercised on a real macOS host. No Mac environment was installed, provisioned, simulated, or claimed; macOS hosted CI remains prohibited.
- Scope boundary/substitutes: this is a non-packable test probe, not a product Local RPC host, restricted launcher, inherited-descriptor proof, or production lease service. Production transport/endpoint identity and private-child integration remain in their owner tasks.
- Remaining completion prerequisites: capture the required actual macOS local-opt-in two-process run (and any remaining Linux local runtime evidence) on existing target hosts; complete graph prerequisites [APP.01](https://github.com/ArcForges/ArcForges-Design/blob/main/docs/planning/delivery/lanes/app-composition.md#task-app-01) and [PLT.11](https://github.com/ArcForges/ArcForges-Design/blob/main/docs/planning/delivery/lanes/platform.md#task-plt-11). Until then PRF.04 is `delivered`, not `complete`.
