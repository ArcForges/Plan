---
task: PLT.27
status: complete
recorded: 2026-09-29
claimant: af-20260928-p04
epoch: 1
---

# Windows, panels and layout

## Evidence

- Implementation: DesktopPlatform [PR #99](https://github.com/ArcForges/DesktopPlatform/pull/99), independently reviewed clean at exact head `5ed600b6be5109c9b58518f77cf5c372e5d40e78` by p03 (COMMENTED review `PRR_kwDOT2OO9M8AAAABPu0R1Q`), based on `d0f6665f929019326d0b8555ae129bfdc35cb63c`. It was squash-merged as `bec79e69ecef70b41233b71cc8436d58d1694920`; the merge has the reviewed head's tree and the expected base as its sole parent.
- PLT.27 delivers the per-instance multi-window model, dockable/collapsible panel host, and device-local layout persistence that restores resiliently across missing panels and changed display arrangements. The offline restore matrix covers missing/renamed panels, topology changes, corrupt/truncated state, duplicate windows and interrupted writes. The task-owned Shell remains non-packable; package activation remains with PLT.35.
- Obligations satisfied: WP-10.01 (full); WP-10 legacy scaffold reconciliation contribution under WP-01.02. The normal shared policy, project, reconciliation and provenance gates validate the registered Shell projects and implementation. No PLT.35 package activation or package inventory change is claimed.
- Exact-head hosted PR gate [run 36551018275](https://github.com/ArcForges/DesktopPlatform/actions/runs/36551018275) completed successfully with all 15 checks green, including the Architecture policy and managed-packages pack gates. The final workflow-only correction keeps the Shell 12-test suite in the pack job with failure propagation while excluding it from the invariant accountant's closed seven-suite TRX set; the accounting checker and registration audit were unchanged.
- Local validation: on implementation head `37fbd4c24547853f239cd5f66b0abca1fe09ab83` before the final workflow-only change, pinned .NET SDK 10.0.400 locked restore and full format verification passed; full Release solution rebuild passed with 0 warnings/errors; Shell tests passed 12/12; dependency policy, provenance, reconciliation, licence and runtime-ownership checks passed. ArchitectureTests passed 99/99 with only `ActualDesktopProjectsSatisfyTheSharedArchitecturePolicy` excluded because its local evidence fixture requires hosted naming/secret and native-configure receipts; that integrated evaluator passed in the final exact-head hosted gate. On final head `5ed600b6`, Shell tests passed 12/12 without emitting a TRX into the invariant-accounting directory, accounting tests passed 10/10, and `git diff --check` passed.
- Normal post-merge [Publish NuGet run 36552171922](https://github.com/ArcForges/DesktopPlatform/actions/runs/36552171922) completed successfully on source `bec79e69ecef70b41233b71cc8436d58d1694920` with all 17 jobs green (including preflight). It produced version `1.0.0-ci.60.1` and immutable candidate `nuget-candidate-36552171922-1` (artifact ID `11025059964`, 5,664,069 bytes, archive SHA-256 `df6a8f8eb9495948d8a8bf4268842e334419a93fde129c671a8cf0de210900b2`). The manifest binds source `bec79e69ecef70b41233b71cc8436d58d1694920`, build `36552171922.1`, and the ten package hashes below; the downloaded candidate members matched the manifest.

  | NuGet package | Version | Package SHA-256 | Public index |
  |---|---|---|---|
  | ArcForges.Build.Policy | 1.0.0-ci.60.1 | `4baed25fc40444fb1ef6071d4113e4876166f067505aab8974a21f1dba845d83` | [index](https://api.nuget.org/v3-flatcontainer/arcforges.build.policy/index.json) |
  | ArcForges.Native.Abstractions | 1.0.0-ci.60.1 | `f8c7a520fc388779b1b93fb54bc7c8e4fc12d2db6018b3ae38d8a64ea83e6670` | [index](https://api.nuget.org/v3-flatcontainer/arcforges.native.abstractions/index.json) |
  | ArcForges.Native.Image | 1.0.0-ci.60.1 | `2989bc44b7a626d9fb2dae9fe9f8aa53cd21524c466c788ec2586e24a12d1904` | [index](https://api.nuget.org/v3-flatcontainer/arcforges.native.image/index.json) |
  | ArcForges.Native.Image.Runtime.win-x64 | 1.0.0-ci.60.1 | `7a58209effaeeedd21ec3fe5d0c2f4c563de1e93aaff3d2f40c1ff8a40c14c92` | [index](https://api.nuget.org/v3-flatcontainer/arcforges.native.image.runtime.win-x64/index.json) |
  | ArcForges.Foundation | 1.0.0-ci.60.1 | `04ceb68b0a39a0ab5579750152e459049036da4b5b952a159533ca2af3213ae4` | [index](https://api.nuget.org/v3-flatcontainer/arcforges.foundation/index.json) |
  | ArcForges.Application.Abstractions | 1.0.0-ci.60.1 | `cc0a547639e2bd895d6b7e34f3bca7e4a91ebbeccaacf0a758c1afaa20187341` | [index](https://api.nuget.org/v3-flatcontainer/arcforges.application.abstractions/index.json) |
  | ArcForges.Capabilities | 1.0.0-ci.60.1 | `0e7827a140247bbc08e0c7e2ba71b1dfafac241bc5fc35e62c1a07d98e69a82c` | [index](https://api.nuget.org/v3-flatcontainer/arcforges.capabilities/index.json) |
  | ArcForges.Persistence.Sqlite | 1.0.0-ci.60.1 | `9af70eb185651a9d4beaa46b214df2c09ac62044833edbba5bd0ab334879b1d3` | [index](https://api.nuget.org/v3-flatcontainer/arcforges.persistence.sqlite/index.json) |
  | ArcForges.Persistence.Resources | 1.0.0-ci.60.1 | `eff78d570e3530a16bd12aebc83ea445b3d59d64da95c9a6fcd38b45a8969e02` | [index](https://api.nuget.org/v3-flatcontainer/arcforges.persistence.resources/index.json) |
  | ArcForges.Persistence.Derived | 1.0.0-ci.60.1 | `77661535a7940182e8b4e3006919b6e766b9b6cdcd08ab685ff0fc4e7fc917e6` | [index](https://api.nuget.org/v3-flatcontainer/arcforges.persistence.derived/index.json) |

- An independent NuGet v3 flat-container index check at 2026-09-29 10:19 UTC confirmed `1.0.0-ci.60.1` visible for all ten package IDs. This visibility check used index metadata only; it did not download public package payloads.
- Untested coverage: no GUI, installed-consumer, or cross-process product runtime acceptance is claimed; none is required by WP-10.01. PLT.27 has no remaining completion prerequisites.
