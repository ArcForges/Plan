---
task: PLT.31
status: complete
recorded: 2026-09-29
claimant: af-20260928-p05
epoch: 1
---

# Error presentation

## Evidence

- Implementation: DesktopPlatform [PR #101](https://github.com/ArcForges/DesktopPlatform/pull/101), independently reviewed clean at exact head `26c450c2f6a4ece169a1591253b75665ff8df122` over base `bec79e69ecef70b41233b71cc8436d58d1694920` (review `5351659607`), then merged as `690e5ea5029b284a349fc9e51ba5807302866a5d`. The merge has the reviewed candidate tree and expected base as its sole parent.
- PLT.31 presents errors through the registered reason-code resources, with human-readable statements, retry guidance and support references. It does not expose raw exception messages or paths. The focused suite verifies disclosure safety and that all 44 registered reason codes have nonblank presentation text.
- Obligations satisfied: WP-10.05 (full). PLT.27's Shell project and test host were integrated before PLT.31 completion; PLT.31 has no other completion prerequisites.
- Exact-head hosted PR gate [run 36559720356](https://github.com/ArcForges/DesktopPlatform/actions/runs/36559720356) completed successfully with all 15 checks green, including native, managed-packages, secret-scan, architecture and aggregate CI gates.
- Local validation at the final source candidate: pinned .NET SDK 10.0.400 locked solution restore and format verification passed; Release solution build passed with 0 warnings/errors; focused Shell tests passed 18/18; non-incremental workflow-parity build with generated compiler files passed; provenance passed (594 files, 140 records, clean); dependency-policy tests passed 19/19; and `git diff --check` passed. Local ArchitectureTests were 99/100 because the remaining evaluator requires same-source hosted RP-01/RP-08/RP-09 and AT-09 native-configure evidence; that integrated architecture gate passed in the exact-head hosted run above. No local 100/100 ArchitectureTests result is claimed.
- Normal post-merge [Publish NuGet run 36560972770](https://github.com/ArcForges/DesktopPlatform/actions/runs/36560972770) succeeded on source merge `690e5ea5029b284a349fc9e51ba5807302866a5d`. It verified and published candidate version `1.0.0-ci.61.1` for all ten repository package IDs: `ArcForges.Build.Policy`, `ArcForges.Native.Abstractions`, `ArcForges.Native.Image`, `ArcForges.Native.Image.Runtime.win-x64`, `ArcForges.Foundation`, `ArcForges.Application.Abstractions`, `ArcForges.Capabilities`, `ArcForges.Persistence.Sqlite`, `ArcForges.Persistence.Resources`, and `ArcForges.Persistence.Derived`. Immutable candidate `nuget-candidate-36560972770-1` (artifact ID `11030471066`, 5,664,046 bytes) has archive SHA-256 `561689943f1f3e614136042303ae527ce7ea1b41d3da2a902ff5594c9ab353a5`; this is the GitHub artifact archive digest, not a package-set or manifest digest. The verified candidate manifest binds source `690e5ea5029b284a349fc9e51ba5807302866a5d` and version `1.0.0-ci.61.1`.
- Independent read-only NuGet v3 flat-container index checks confirmed the exact version `1.0.0-ci.61.1` visible for all ten package IDs at `2026-09-29T11:42Z`. These checks read index metadata only; no public package payloads were downloaded.
- Substitutes still in use and their removing tasks: None introduced or relied on by PLT.31.
- Untested coverage: No GUI, installed-consumer, cross-process product runtime, macOS, device, browser E2E, live-service or inference validation is claimed; these are excluded by P2-017 and not required for WP-10.05.
- Remaining completion prerequisites and next action: None. PLT.27 is complete, and PLT.31 has no remaining completion prerequisites.
