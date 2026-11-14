# MR-06: StopNode before readiness

Date: 2026-10-25. Design: [ArcForges-Design#27](https://github.com/ArcForges/ArcForges-Design/pull/27).
Implementation: [ArcForges#49](https://github.com/ArcForges/ArcForges/pull/49).

## Design dependency

Design merged first as `c36bf89ed5b4f47dc09a2e40ee2c7b82c96788c8`, reviewed head
`bf86fc6db1857161e6bf825f34202b2067b7339b`, tree `a827f2a2dcb2baea790d8cfe318fd913ba359ba1`,
base `8ec57350dc3e38858282c0d484f6de0b3fba85ff`.
It retains SM-NODE's READY/DEGRADED acceptance states and specifies the existing STATE/invalid_state convention
(NEVER, DID_NOT_HAPPEN, current state and readiness reason) for a reachable API in STARTING/RECOVERING.
Startup continues, with no deferred stop; the caller may issue a new command after readiness.
The proto's annotations were updated and api-catalogue.md regenerated with check_design.py --write.
No wire field or lifecycle transition was added.

Complete exact-head Design summaries and all results were read before merge, with live main/head/base,
both required success statuses, mergeability and owner-skipped hosted check:
- Windows: full 3 steps/21 s, logs `Design/.git/arcforges-verify/logs/20261025-152145-bf86fc6db185-win`.
- Linux: full 3 steps/43 s, logs `Design/.git/arcforges-verify/logs/20261025-232142-bf86fc6db185-linux`.

Author locked proto-toolchain restore, require-protoc design checks (25 proto files compiled, zero errors) and
44 tool tests passed (20 existing Windows skips). Complete Design diff self-reviewed directly by OpenAI Codex
under the owner's no-delegation instruction, no blocking findings; comment 6399467139.

## Implementation and regression

Reviewed head `8fe744ffee80f24b59f835af60ba43e4a5163391`, tree
`e843cc316959074d956d78202a6c0e2c4dd5171f`, base
`3990e07be8cc1ad4494bc73fe2013ba36acc6b80`.
Implementation merged as `5eaee92a4a964469bad41dad28dad9787b7552cf` after both final-head host checks passed.

StopNode now checks STARTING/RECOVERING inside the serialized idempotent writer, alongside lifecycle transitions.
It returns the catalogued error, which is saved as that command ID's outcome, before any stop transition/event/request.
Only a successful value response calls RequestStop. Permission checks still run before this action.

An internal BeforeReady callback lets an in-process component test hold the actual node while the real API listens
in RECOVERING. The executable never sets it. This is a scheduling hold, not a simulated lifecycle, RPC or store.
The test releases it in finally and observes the runtime stop token. STARTING normally has no listening endpoint;
a native connection in that state is not claimed, and both explicit startup states use the same handler guard.

The final test on the unmodified handler failed: expected State, actual Internal (`before-test.log`).
After the repair, it requires STATE/invalid_state, DID_NOT_HAPPEN, NEVER and RECOVERING details; no stop token/state
change; continued READY/DEGRADED startup; an identical saved error when the same command is replayed after readiness;
a new successful stop with HAPPENED and clean exit; and no api.command.failed log event.
No existing assertion or timeout was weakened.

## Author validation

Windows logs/scripts: `C:\MyFile\Projects\dev\logs\resume-20261025-mr06\`.

- Locked solution restore and Release solution build: passed, zero warnings/errors.
- Changed-file format and final verify-no-changes, plus whitespace checks: passed.
- Entire NodeServiceTests class three times: 14/14 each; the new real-RPC regression passed in each.
- PermissionTests and UnitTests: 81/81.
- Native AOT win-x64 host in the Visual Studio developer environment: zero warnings.
- Native host WaitReadyReturnsOnlyOnceTheNodeIsReady closed-loop test: 1/1.
  This checks native readiness and normal stop; the controlled refusal/replay test runs in-process over the real RPC.

Complete five-file implementation diff and surrounding startup/lifecycle/dedup/permission/shutdown paths were
self-reviewed directly at the final head, under the owner's instruction. No blocking findings.

## Required implementation checks

Both native hosts fetched the pushed reviewed commit and ran their full run-and-report profiles through MCP,
with no other build/test running on either host. Both complete summaries and every result were inspected:
same head/tree/base above, full profiles, every required step successful.

| Host | Steps | Seconds | Summary |
|---|---:|---:|---|
| Windows | 13 | 963 | `ArcForges/.git/arcforges-verify/logs/20261025-153113-8fe744ffee80-win/summary.json` |
| Linux | 16 | 1129 | `ArcForges/.git/arcforges-verify/logs/20261025-233108-8fe744ffee80-linux/summary.json` |

The formal Node.Core ci suites had 257 passed/33 platform skips on Windows and 245 passed/45 platform skips on Linux,
zero failures. The common regression is included in that suite on both native operating systems. Both profiles also
passed all AOT publishes, native tools/closed loop, schema checks, JIT and native exclusive suites, benchmarks,
packaging and startup comparisons; Linux additionally passed real-OS, format and secret-scan checks.

Immediately before merge, source main 3990e07, exact PR head, required success statuses, mergeability and owner-skipped
hosted jobs were checked. No status was copied or posted manually. Full implementation self-review: comment 6399586091.

MR-16 remains blocked with its recovery proposal. Later feature tasks, real credential-store cleanup/stress,
LAN/cloud MCP and database migrations remain outside this maintenance work.
