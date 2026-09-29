---
task: PLT.30
status: complete
recorded: 2026-09-29
claimant: af-20260928-a01
epoch: 1
---

# Attention and notification model

## Evidence

- Implementation: DesktopPlatform [PR #103](https://github.com/ArcForges/DesktopPlatform/pull/103), independently reviewed clean at exact head `be221455ef44014c428db7a57e8e4f0f7c6a39a8` over base `5a71fc4ba059c0768d13dbc5e911cd36f6096b9f` (P05 COMMENTED review [5353177498](https://github.com/ArcForges/DesktopPlatform/pull/103#pullrequestreview-5353177498)); squash-merged as `45815417e30e294d05d898a18b6986f642f81401`. The merge has the expected base as its sole parent, and its tree `3ab69e601a5518dfd245a68a6bcf3f2c95223b6b` exactly matches the reviewed source head tree.
- PLT.30 delivers a framework-neutral attention model: durable items remain in the snapshot until resolved even when best-effort transient notification delivery is missed; transient items are not retained. Sensitive system-notification content is generic unless preview consent is explicit. Generic title/body are loaded through the existing Shell resources using `CurrentUICulture`; missing resources fail closed. The model does not claim a concrete OS notification adapter or UI integration.
- Obligations satisfied: WP-10.04 (full). Entry conditions were satisfied: ADOPT.02.platform is complete and PLT.27's window/panel host is integrated (`bec79e69ecef70b41233b71cc8436d58d1694920`). PLT.30 has no completion prerequisites.
- Exact-head hosted PR gate [run 36572809931](https://github.com/ArcForges/DesktopPlatform/actions/runs/36572809931) completed successfully, 15/15 checks green, including secret scan, native, managed-packages/AOT, policy and aggregate CI.
- Local validation on the final source head: pinned .NET SDK 10.0.400; locked full-solution restore and `dotnet format` verification passed; Release solution build passed with 0 warnings/errors; Shell tests passed 25/25; dependency policy passed (51 dependencies/244 inputs); reconciliation passed (7 owners/67 projects/166 historical); provenance passed (602 files/140 records, clean); and `git diff --check` passed. ArchitectureTests ran 99/100; the only local aggregate-evidence failure was the workstation's absent hosted-context RP-01/RP-08/RP-09 evidence and AT-09 same-source native configure receipt. There was no RP-10 finding; the exact-head hosted architecture gate passed.
- Normal post-merge [Publish NuGet run 36575682868](https://github.com/ArcForges/DesktopPlatform/actions/runs/36575682868) completed successfully with all 17 jobs green on merge `45815417e30e294d05d898a18b6986f642f81401`. It verified and published version `1.0.0-ci.64.1` for all ten admitted NuGet packages. The retained same-run candidate artifact is [nuget-candidate-36575682868-1](https://github.com/ArcForges/DesktopPlatform/actions/runs/36575682868/artifacts/11037917170), artifact ID `11037917170`, 5,675,309 bytes, GitHub artifact archive SHA-256 `6da10f471457a7157806a021075d4b2407012fe3c187b83e7dc71d7d7c4c687a`. This is the artifact archive digest, not an individual package-content digest. The publisher log verified 10 packages and bound the candidate to source merge `45815417e30e294d05d898a18b6986f642f81401` before pushing the same verified bytes.
- Independent read-only NuGet v3 flat-container index checks at `2026-09-29T13:48:10Z` confirmed `1.0.0-ci.64.1` visible for all ten candidate package IDs. These checks read index metadata only; no public package payloads were downloaded.

  | NuGet package | Version | Public index |
  |---|---|---|
  | ArcForges.Build.Policy | 1.0.0-ci.64.1 | [index](https://api.nuget.org/v3-flatcontainer/arcforges.build.policy/index.json) |
  | ArcForges.Native.Abstractions | 1.0.0-ci.64.1 | [index](https://api.nuget.org/v3-flatcontainer/arcforges.native.abstractions/index.json) |
  | ArcForges.Native.Image | 1.0.0-ci.64.1 | [index](https://api.nuget.org/v3-flatcontainer/arcforges.native.image/index.json) |
  | ArcForges.Native.Image.Runtime.win-x64 | 1.0.0-ci.64.1 | [index](https://api.nuget.org/v3-flatcontainer/arcforges.native.image.runtime.win-x64/index.json) |
  | ArcForges.Foundation | 1.0.0-ci.64.1 | [index](https://api.nuget.org/v3-flatcontainer/arcforges.foundation/index.json) |
  | ArcForges.Application.Abstractions | 1.0.0-ci.64.1 | [index](https://api.nuget.org/v3-flatcontainer/arcforges.application.abstractions/index.json) |
  | ArcForges.Capabilities | 1.0.0-ci.64.1 | [index](https://api.nuget.org/v3-flatcontainer/arcforges.capabilities/index.json) |
  | ArcForges.Persistence.Sqlite | 1.0.0-ci.64.1 | [index](https://api.nuget.org/v3-flatcontainer/arcforges.persistence.sqlite/index.json) |
  | ArcForges.Persistence.Resources | 1.0.0-ci.64.1 | [index](https://api.nuget.org/v3-flatcontainer/arcforges.persistence.resources/index.json) |
  | ArcForges.Persistence.Derived | 1.0.0-ci.64.1 | [index](https://api.nuget.org/v3-flatcontainer/arcforges.persistence.derived/index.json) |

- Substitutes still in use and their removing tasks: None introduced or relied on by PLT.30.
- Untested coverage: No GUI, installed-consumer, real OS notification delivery, lock-screen rendering, device, live-service, browser E2E or inference validation is claimed; these are outside the offline PLT.30 acceptance and restricted by P2-017.
- Remaining completion prerequisites and next action: None. PLT.27 is complete and PLT.30 has no other completion prerequisites.
