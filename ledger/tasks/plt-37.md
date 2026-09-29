---
task: PLT.37
status: complete
recorded: 2026-09-29
claimant: af-20260928-g01
epoch: 1
---

## Evidence

- Pull requests (implementation, documentation, ledger), each with its reviewed head commit and merge commit:
  - Risk-floor clarification: Design PR [#146](https://github.com/ArcForges/ArcForges-Design/pull/146), exact reviewed head `0107c7149b814a04ada79cf4128ee4830c5c9c8d` on base `85c09c2b591f8fb282b73556ea0f3b1b9ad884a2`, merged as `9fc122a2b099656e603e20aa5ec2bd3e6333a017` after exact-head clean review 5348873381.
  - Generated Plan companion: Plan PR [#151](https://github.com/ArcForges/Plan/pull/151), exact reviewed head `1f1f2d8d69a140400f2096462ad63d7d494e8602` on base `51d98afd0b9fe26eb7752112646c9a70ca829000`, merged as `30f9e93aef4d62d8b269e7a04413b9841db7b6f7` after exact-head clean review 5348994537.
  - Implementation: DesktopPlatform PR [#98](https://github.com/ArcForges/DesktopPlatform/pull/98), exact reviewed head `3254c65eb9afba05060caa78fc60599658a58618` on base `cb01b57fbee9eca6998ae4c8dd646f0894f8c317`, merged as `d0f6665f929019326d0b8555ae129bfdc35cb63c`. Independent exact-head clean review: [review 5349599447](https://github.com/ArcForges/DesktopPlatform/pull/98#pullrequestreview-5349599447).
- Published candidate identities (package, version, hash, registry receipt) and the CI and publication runs:
  - Exact-head source CI [run 36540434135](https://github.com/ArcForges/DesktopPlatform/actions/runs/36540434135) completed successfully with all 15 checks green, including aggregate `ci`.
  - Normal main Publish NuGet [run 36542323533](https://github.com/ArcForges/DesktopPlatform/actions/runs/36542323533) completed successfully on merge/source `d0f6665f929019326d0b8555ae129bfdc35cb63c`; the publisher verified the allowlist and candidate bytes, exchanged OIDC identity, and pushed the same verified packages. Candidate artifact `nuget-candidate-36542323533-1`, artifact ID `11020984108`, size `5,664,170` bytes, SHA-256 `06ac29cff0625b15ac37ef34522059ca026edb3430dbcf9465a0e0adf9acc336`.
  - The artifact manifest binds source `d0f6665f929019326d0b8555ae129bfdc35cb63c`, run `36542323533`, version `1.0.0-ci.59.1`, and ten packages. All ten local package payload hashes matched the manifest; public NuGet flat-container indexes each listed `1.0.0-ci.59.1` when checked at `2026-09-29T09:10:32Z` (10/10; package payloads were not downloaded):
    - `ArcForges.Build.Policy` — `da49655d99d3a988ed0a6f48f208652fdb93db42d100a868378e7cee93e9868b`
    - `ArcForges.Native.Abstractions` — `d92bf0623ed7313ffaccc3a8afdd52e1817d7d5279ab7937109c4a49cd5d3fb5`
    - `ArcForges.Native.Image` — `669d343dcfb02e404132a76e31ea422a60f3d966301550b0c855de228468efbf`
    - `ArcForges.Native.Image.Runtime.win-x64` — `7e303a0bb113ff217e04072a4a06d4d9cff39c3d9580283a1db1433d66264c88`
    - `ArcForges.Foundation` — `2a3c0b9d461538300f197fce7667546cc48de2aa71e2a5ff89067e60035d691a`
    - `ArcForges.Application.Abstractions` — `83d4dd4d390f2e6b322464e3d7757925f2125edd97e9c235030e4ee4a3f606f2`
    - `ArcForges.Capabilities` — `78e7a0b624ccb1feefe76af4a32124358531ed1d65998914dc24795f5af57f7c`
    - `ArcForges.Persistence.Sqlite` — `2ac1c4dbae2ed9c4dfb9bd85a4971dcd6c6274fd10d44ffb0ff1248680e53267`
    - `ArcForges.Persistence.Resources` — `23b58c409d72948f4c941bab316f498439582f37597fa8ae065ed5d2ca89795c`
    - `ArcForges.Persistence.Derived` — `039498f651d1c8967b4764527aab92cb73f36474c3b8d19f556c5c0104b9f225`
  - `ArcForges.Security` inherits `IsPackable=false` and is absent from `eng/packaging/packages.json`; PLT.37 produced no direct package. The ten packages above are the repository's normal allowlisted publication evidence, not a PLT.37 package.
- Obligations satisfied (substep or package obligation and part):
  - WP-11.01 (full): added a closed R0–R4 risk scale and immutable runtime context; each assessment is the maximum of the descriptor's canonical baseline and active fixed modifier floors, with stable non-authorizing explanation codes. Actor floors: `None` adds none, `Agent` R2, `Extension` R3, `Automation` R2, and `InternalService` R1. Other floors: remote origin R3, bulk R2, sensitive resource R2, large data volume R2, external egress R3, irreversible effect R4, and unverified package R3. The only stricter interaction floors are `Automation + ExternalEgress` R4, `SensitiveResource + ExternalEgress` R4, and `Extension + UnverifiedPackage` R4. There are no configurable weights or hidden modifiers.
- Validation actually performed (CI checks, local runtime checks with environment identity):
  - Pinned .NET SDK 10.0.400 exact-head locked solution restore and full Release solution build with `--warnaserror` passed; build had 0 warnings and 0 errors. Full-solution `dotnet format --verify-no-changes --no-restore` passed.
  - `ArcForges.Security.Tests` passed 33/33. ArchitectureTests excluding the known `ActualDesktopProjectsSatisfyTheSharedArchitecturePolicy` reconstruction case passed 99/99; all 10 PLT.37 RP-10 direct public-API-to-`[Fact]` bindings were appended and validated. Dependency policy passed (51 dependencies/240 inputs; tests 19/19); licence boundary covered 41 projects (tests 12/12); architecture-evidence tests 11/11; build-identity tests 6/6; provenance passed (577 files/140 records against base `cb01b57`); native provenance passed (21 components, no packages); `git diff --check` was clean.
  - The classification test exhaustively assessed 640 runtime contexts (scope, target, reversibility, egress, all `ActorKind` values, remote origin, package verification, and data-volume modifiers) against all five descriptor baselines, checking exact effective risks and explanation codes. The monotonicity test verifies adding each modifier never lowers risk. Focused tests separately assert each of the three authorized R4 interaction floors exceeds both individual floors and reject malformed baselines and unknown enum values.
  - The exact focused `ActualDesktopProjectsSatisfyTheSharedArchitecturePolicy` method was attempted with `PATH` pinned to SDK 10.0.400 but failed while reconstructing the unchanged `DesignSystem.Tests` project: GeneratedRegex partials `RawColor`/`RawDimension` produced CS8795. The same failure was independently reproduced on clean DesktopPlatform main `bdf4460` with the pinned SDK, identifying the existing GOV.06 generated-source reconstruction gap; it is not presented as a PLT.37 test pass. Hosted source CI remained fully green at the exact reviewed head.
- Substitutes still in use and their removing tasks: No substitute implementation or temporary policy authority was introduced or relied on by PLT.37.
- Untested coverage: No macOS, hosted runtime, device, GUI, browser E2E, live-service, inference, or installed-consumer validation was performed; these are excluded by P2-017. The known GOV.06 source-generator reconstruction limitation is recorded above; no out-of-scope producer repair was made.
- Remaining completion prerequisites and next action (delivered only): None. PLT.37 has no completion prerequisites; source acceptance, exact-head review, hosted CI, normal publication, and public-index visibility are recorded above.
