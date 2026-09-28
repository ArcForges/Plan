---
task: NAT.06
status: complete
recorded: 2026-09-28
claimant: af-20260928-c02
epoch: 1
---

# Common native ABI layouts

## Evidence

- Implementation: DesktopPlatform [PR #90](https://github.com/ArcForges/DesktopPlatform/pull/90), exact reviewed head `e046bd5590974ae5b4689f2eede6fd37d4d99470`, independently reviewed clean by af-20260928-p03 at [review 5342997524](https://github.com/ArcForges/DesktopPlatform/pull/90#pullrequestreview-5342997524), merged from base `213424c4944e7ed208ef21f3493068fcc26c7210` as `19635a2dd205184fd89b7e7992ab24228cf23021`.
- Outcome: Added the common C17/C++20 and C# ABI preambles, fixed-width keys, pack-8 POD layouts, ownership/cancellation/bounded-buffer helpers and deterministic failure semantics. Assertions cover all 17 normative sizes (7 frozen PODs, 8 ABI 1.1 records, status and bool scalar widths) plus a separate 8-byte `arc_handle_t` width invariant. The retained ABI 1.0 image probe identity/signatures and minor remain unchanged. Added the exact 14 Annex 06 ABI 1.1 family declarations (6 instruments, 3 functional image, 5 PDF) with compile-time C17/C++20 signature checks only; no family bodies, new library targets, functional exports or package identities were introduced. Managed abstractions contain status/handle and common layout declarations only.
- Published candidate: [Publish NuGet run 36466017180](https://github.com/ArcForges/DesktopPlatform/actions/runs/36466017180) completed successfully for source merge `19635a2dd205184fd89b7e7992ab24228cf23021`. The verified release was `1.0.0-ci.51.1`; all eight registered packages were verified and pushed: `ArcForges.Build.Policy`, `ArcForges.Native.Abstractions`, `ArcForges.Native.Image`, `ArcForges.Native.Image.Runtime.win-x64`, `ArcForges.Foundation`, `ArcForges.Application.Abstractions`, `ArcForges.Capabilities` and `ArcForges.Persistence.Sqlite`. Candidate artifact `nuget-candidate-36466017180-1` (artifact ID `10990085091`, size 5,558,026 bytes) has archive SHA-256 `a1be55808048a4bde3227fc051a46d1bfaac7dab408df01fd5f69d0b7ec121f5`. The package publication is repository-wide; NAT.06 changes no package inventory or identity.
- Registry visibility: On 2026-09-28, index-only checks confirmed that the exact `1.0.0-ci.51.1` version is listed in the public NuGet flat-container index for all eight package IDs above. No package payloads were downloaded.
- Validation at final exact head: [PR gate run 36464520754](https://github.com/ArcForges/DesktopPlatform/actions/runs/36464520754) passed all 14 checks, including repository hooks, all policy/security gates, Windows native configure/build/CTest/package staging, managed package validation, Windows/Linux Local RPC AOT compile probes, Avalonia AOT compile probe, and aggregate CI. The earlier full run 36463385688 also passed on the preceding formatting-only head; the transient hosted native-source HTTP 403 did not recur.
- Independent local validation with pinned .NET SDK 10.0.400: locked restore, formatting and filtered `NativeAbiLayout` tests passed (3/3); development dependency audit passed with 51 NuGet and 10 Python packages across 238 inputs, dependency-policy tests 16/16; native provenance and IDE licence evaluation passed; reconciliation passed with tests 8/8; runtime-ownership tests 25/25; source provenance passed (550 files/140 records); `git diff --check` passed. Local CMake/CTest/native package staging could not run because this host lacks the pinned `VCPKG_ROOT`/toolchain; the exact-head hosted Windows native job ran and passed those gates.
- Obligations satisfied: WP-13.05 (full), including common ABI declarations/layouts, field offsets, 17 normative sizes, deterministic wrong-size/version/null/closed-handle behavior and zero outputs on failure. Package-level WP-13 probe-scaffold lifecycle contribution is satisfied by keeping the new ABI tests retained shim-static and isolated from runtime/package activation. WP-13 major-types note is preserved: no native pointer is used as a managed domain identifier or wire field.
- Substitutes still in use: none introduced or relied on.
- Untested coverage: No instruments, functional image or PDF family implementation/library body, device/hardware runtime, hosted runtime/device test, installed-consumer behavior or product acquisition capability is claimed; these remain outside NAT.06's common ABI/layout scope and later native-family tasks.
- Remaining completion prerequisites: none in the merged Design graph.

The source claim, exact-head review, CI, merge, publication and index evidence are retained in `claims/nat-06` and the DesktopPlatform integration-role history.
