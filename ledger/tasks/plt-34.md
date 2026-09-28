---
task: PLT.34
status: complete
recorded: 2026-09-28
claimant: af-20260928-p04
epoch: 1
---

# Third-party control admission

## Evidence

- Implementation and admission record: [DesktopPlatform PR #80](https://github.com/ArcForges/DesktopPlatform/pull/80), reviewed head `d12171931459ce3ce4ec8745756ea5534ea28c05`, independently reviewed without findings by `platform_capabilities` at [review comment 5863858775](https://github.com/ArcForges/DesktopPlatform/pull/80#issuecomment-5863858775), merged as `606e8336a18946551966174b5747f9ff7f5b7eb7`. The merged document records the per-control licence/admission boundary and the current source search; it does not introduce runtime or dependency changes.
- WP-10.08 (full): the current DesktopPlatform shell consumes no third-party Avalonia control packages. The proposed Avalonia `TableView` candidate is explicitly NOT ADMITTED pending PRF.09's real consumer/AOT proof. No AOT proof for that proposed candidate is claimed; no third-party control is adopted without its zero-diagnostic proof and licence position. The Avalonia 12.1.3 MIT grant is distinguished from ArcForges' package-boundary policy.
- Latest-head PR gate [run 36380529918](https://github.com/ArcForges/DesktopPlatform/actions/runs/36380529918) passed on the reviewed head. The normal post-merge [Publish NuGet run 36381143738](https://github.com/ArcForges/DesktopPlatform/actions/runs/36381143738) completed successfully for source `606e8336a18946551966174b5747f9ff7f5b7eb7`, build `36381143738.1`. Publisher job `108798455407` rechecked the immutable candidate before OIDC and published the same verified bytes; all eight NuGet pushes succeeded.
- Publication receipt: existing managed packages `ArcForges.Build.Policy`, `ArcForges.Native.Abstractions`, `ArcForges.Native.Image`, `ArcForges.Native.Image.Runtime.win-x64`, `ArcForges.Foundation`, `ArcForges.Application.Abstractions`, `ArcForges.Capabilities`, and `ArcForges.Persistence.Sqlite`, version `1.0.0-ci.37.1`. Candidate artifact `nuget-candidate-36381143738-1` / artifact `10952314680`, digest `sha256:b5a3b16413068a3530d767ac59e929ef46988a4a975a6bc189b9ff1e3240f471`; its manifest contains the source identity and SHA-256 for every package plus the native artifact. The publisher log records each upload as created at NuGet.org. This routine main publication is not a TableView package or consumer acceptance claim.
- Validation: `git diff --check` and the applicable pre-commit hooks passed on the documentation change; PR CI passed all retained checks, including provenance/runtime/licence/reconciliation, managed packing, Windows native and aggregate CI. No real consumer AOT proof, installed-consumer test, or use of the proposed TableView is claimed; PRF.09 owns the candidate's actual AOT proof. There are no completion prerequisites remaining.
- Substitutes still in use: none. The proposed TableView remains not admitted until PRF.09 evidence exists.
