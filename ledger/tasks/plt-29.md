---
task: PLT.29
status: complete
recorded: 2026-09-29
claimant: af-20260928-p02
epoch: 1
---

# Scoped settings

## Evidence

- Implementation: DesktopPlatform [PR #102](https://github.com/ArcForges/DesktopPlatform/pull/102), independently reviewed clean at exact head `1b98b30c2999a88a802fa0670baecfdeba13b9c0` (COMMENTED review [5352591268](https://github.com/ArcForges/DesktopPlatform/pull/102#pullrequestreview-5352591268)) over base `690e5ea5029b284a349fc9e51ba5807302866a5d`; merged as `20a447c45447f06280cc16f0f6ba5867f141bd6a`. The merge has the expected first parent and its tree exactly matches the reviewed head tree `00a01bb5146de5db9e4995d1bd35b8d941261ed5`.
- PLT.29 implements application/workspace/device/instance scope resolution, typed settings definitions, explainable winning values, schema migration and atomic local persistence; device- and instance-scoped values are excluded from the synchronization projection. The six ordinary public APIs are bound to three task-owned direct `[Fact]` tests in the RP-10 registry.
- Obligations satisfied: WP-10.03 (full). Start prerequisites PLT.26 and PLT.04 were complete. Completion prerequisite PLT.27 is complete (Plan ledger #159 merged as `1fa49d7378faea2af5e7336a89485a05061a19cd`); no completion prerequisites remain open.
- Exact-head hosted PR gate [run 36567351007](https://github.com/ArcForges/DesktopPlatform/actions/runs/36567351007) completed successfully with all 15 checks green, including secret scan, architecture/RP-10, native, Windows/Linux Local RPC AOT compile, Avalonia AOT compile-only probe, pack and aggregate CI.
- Local validation at the final source candidate: pinned .NET SDK 10.0.400 locked solution restore and format verification passed; Release solution build passed with 0 warnings/errors; Desktop Shell tests passed 21/21; Python tooling tests passed 47/47; provenance and `git diff --check` passed. Local ArchitectureTests were 99/100: the sole failure was the unrelated Build.Policy generated-source reconstruction defect (CS8795 in unchanged DesignSystem generated partials). No bypass or product finding was added; the exact-head hosted architecture/RP-10 gate passed.
- Normal post-merge [Publish NuGet run 36568773736](https://github.com/ArcForges/DesktopPlatform/actions/runs/36568773736) completed successfully with all 17 jobs green for source merge `20a447c45447f06280cc16f0f6ba5867f141bd6a`. It verified and published version `1.0.0-ci.62.1` for all ten admitted package IDs. The retained same-run candidate artifact is `nuget-candidate-36568773736-1` (artifact ID `11034065431`, 5,663,945 bytes, archive SHA-256 `178d9af5820d9cc1fbdcd6a30e16ce637ec40debffdc301dba0e519f405984ff`). Its manifest SHA-256 is `916bacdb3417674b0f0d5a38bfa6e6f05a87523880b0aab4f7fa7ade5815def4`; the manifest binds build `36568773736.1`, source `20a447c45447f06280cc16f0f6ba5867f141bd6a`, `dirty=false`, and the following package hashes. The publisher reverified the candidate manifest and all ten package bytes before upload. The retained internal candidate was read once to capture its manifest; no public NuGet package payloads were downloaded.

  | NuGet package | Version | Manifest package SHA-256 | Public index |
  |---|---|---|---|
  | ArcForges.Build.Policy | 1.0.0-ci.62.1 | `513b2e936a5ff112507c141c132568ac341da7cebb7bfdb3e1fb2be23004ed50` | [index](https://api.nuget.org/v3-flatcontainer/arcforges.build.policy/index.json) |
  | ArcForges.Native.Abstractions | 1.0.0-ci.62.1 | `f0cb1d4ad0cc5475503ebe4a09355d07147e94832d4a240e6337dbe633c03c04` | [index](https://api.nuget.org/v3-flatcontainer/arcforges.native.abstractions/index.json) |
  | ArcForges.Native.Image | 1.0.0-ci.62.1 | `411cdccfd9145c12fd18a0523fc7396a0ec2108aaa26deca419cb074d9ef3a14` | [index](https://api.nuget.org/v3-flatcontainer/arcforges.native.image/index.json) |
  | ArcForges.Native.Image.Runtime.win-x64 | 1.0.0-ci.62.1 | `ee39c56603da47bd170a012f34c34c462c7e8e8e302abfe62fdbecc621e3a28f` | [index](https://api.nuget.org/v3-flatcontainer/arcforges.native.image.runtime.win-x64/index.json) |
  | ArcForges.Foundation | 1.0.0-ci.62.1 | `47c1508094da7a32d2190dff1d69a5e2777cdab8fb78e09e7d2d9475f3368310` | [index](https://api.nuget.org/v3-flatcontainer/arcforges.foundation/index.json) |
  | ArcForges.Application.Abstractions | 1.0.0-ci.62.1 | `aa5831b09ed37f3ba7a91d66f131334fff06ea7629dc46d9e08a9d1008da3d81` | [index](https://api.nuget.org/v3-flatcontainer/arcforges.application.abstractions/index.json) |
  | ArcForges.Capabilities | 1.0.0-ci.62.1 | `ff37f5b7463a39555e3f126c1bce97fc503390e7e5c3148b91fbc15b7fc8fc77` | [index](https://api.nuget.org/v3-flatcontainer/arcforges.capabilities/index.json) |
  | ArcForges.Persistence.Sqlite | 1.0.0-ci.62.1 | `ab0204d138a176342b12edc3a2daaa0c91419009b086a18b1952d16086d9add9` | [index](https://api.nuget.org/v3-flatcontainer/arcforges.persistence.sqlite/index.json) |
  | ArcForges.Persistence.Resources | 1.0.0-ci.62.1 | `a696b329fe86a9fb28436aea2243b0594bf9b27fd60a9f4aea08c28dfd1dd898` | [index](https://api.nuget.org/v3-flatcontainer/arcforges.persistence.resources/index.json) |
  | ArcForges.Persistence.Derived | 1.0.0-ci.62.1 | `9c8e72f0d6b8737881b49e86b1946147034cd64a93e9a92c06bdba7509ebd99b` | [index](https://api.nuget.org/v3-flatcontainer/arcforges.persistence.derived/index.json) |

- Independent read-only NuGet v3 flat-container index checks confirmed version `1.0.0-ci.62.1` visible for all ten manifest package IDs at `2026-09-29T13:06:30Z`. These checks read only each exact package `index.json`; no public package payloads were downloaded.
- Substitutes still in use and their removing tasks: None introduced or relied on by PLT.29.
- Untested coverage: No GUI, installed-consumer, device, macOS, browser E2E, live-service or inference validation is claimed; these are outside the offline PLT.29 acceptance and restricted by P2-017.
- Remaining completion prerequisites and next action: None. PLT.27 is complete and PLT.29 has no other completion prerequisites.
