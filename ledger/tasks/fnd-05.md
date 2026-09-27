---
task: FND.05
status: complete
recorded: 2026-09-27
claimant: w-20260927-web-lane
epoch: 1
---

# Reason registry and Outcome

- Implementation: [DesktopPlatform PR65](https://github.com/ArcForges/DesktopPlatform/pull/65), final reviewed source `ca7a56daf80e86d7b7fa070931c3f179ecb5d441`, merge `ace60538849047184954baed09fb05ec7676d367`. Independent [final exact-head review](https://github.com/ArcForges/DesktopPlatform/pull/65#issuecomment-5859360792) retains the preceding full source review and bounded fixes.
- Outcome: WP04.04: generated44-code reason registry carries category/retryability/effect-certainty/message keys. Sealed Outcome distinguishes success, typed failure and cancellation; unknown reason/effect inputs fail closed for automatic action. Registry completeness/generation and cancellation distinction tests pass.
- Validation: all12 retained [PR checks](https://github.com/ArcForges/DesktopPlatform/actions/runs/36346503976) passed, including Windows native staging and Linux managed compilation,47 Foundation offline tests, registry generation, real package verification and all policy/security gates. Local Windows SDK10.0.401 was invoked explicitly with ignored compatibility targets preserving the10.0.11 ILLink/ILCompiler tool inputs; exact repository SDK10.0.400 remained unchanged and authoritative in CI. Full solution locked restore,15 admission tests and9 external dependency guard tests pass.
- Package boundaries: Foundation pins external `ArcForges.Contracts.Foundation/1.0.0-ci.113.1`; Application.Abstractions depends on same-candidate Foundation and the same external Contracts pin promoted by central transitive pinning. Actual local nupkg metadata for both producers passed the strict dependency-set check; no new package version was substituted. Current admission records33 NuGet/10 Python dependencies and200 inputs, preserving historical receipts. The immutable predecessor is `gov17-gov18-r2` at `111a935e98a6666ec1dd965b095bcb8b95d9b80a`.
- Untested boundaries: no device/browser/live-service/inference/runtime benchmark or installed-consumer CI is claimed. FND.07 owns published cross-language acceptance; PLT.01 owns durable real-store receipts. No product schema, database adapter or provider integration is implied by these producer tests.
- Ledger review and merge identity are retained by this ledger PR and task claim history.
- Publication: [normal main run36347078380](https://github.com/ArcForges/DesktopPlatform/actions/runs/36347078380) completed successfully, including candidate verification, OIDC authentication and NuGet publication of the same verified bytes. Both owned coordinates use `1.0.0-ci.29.1` from merge `ace60538849047184954baed09fb05ec7676d367`. No tag or verification-only republish was created.
- Original candidate receipt: `nuget-candidate-36347078380-1`, GitHub artifact10941456614, archive digest `sha256:e3757f7136b5deccc1d145311db81fba763b1d3348fdfae89bd6b9e6bdf09976`. Its manifest records `ArcForges.Foundation` package SHA256 `c373e7eb8d9e8a1232fb5de06c68b74f50a1f42bde2155eb92ee59980581ab51` and `ArcForges.Application.Abstractions` SHA256 `2f2ef1494db6927b2d7b724c6b59c0685c1a2520d62a24827af30296110c0306`; build identity is `36347078380.1`, source dirty=false. This original CI artifact was retrieved once for the receipt and retained acceptance inputs; no public package bytes were repeatedly downloaded or re-compared. The successful same-run publish job is the registry transfer receipt.
