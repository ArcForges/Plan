---
task: PLT.22
status: complete
recorded: 2026-09-28
claimant: af-20260928-p04
epoch: 1
---

## Evidence

- Implementation PR [#92](https://github.com/ArcForges/DesktopPlatform/pull/92) was independently reviewed clean at exact head `9e112d06d2a40754d6077d3c1d00a06ad8f6fe3d` by review 5345024574 and merged as `fe48620d57a8d18f7b10d831bfa76b43227fb5d8` over base `19635a2dd205184fd89b7e7992ab24228cf23021`. The primary checkout was fast-forwarded to that merge commit.
- The final source PR gate [run 36487402155](https://github.com/ArcForges/DesktopPlatform/actions/runs/36487402155) completed successfully with all 15 checks green, including the Architecture policy gate.
- PLT.22 implements the full [WP-09.05](https://github.com/ArcForges/ArcForges-Design/blob/main/docs/planning/work-packages/09-capability-contribution-and-resource-model.md#rule-wp-09.05) obligation: resource resolution distinguishes owner-present/absent, permission denial, floating references and immutable pinned references; every access rechecks current permission; per-kind artifact handlers resolve only opaque references; and references structurally cannot carry paths, pointers or handles. Pinned versions require a canonical lowercase SHA-256; a present BlobRef requires a matching digest, and invalid pins fail closed before authorization/access callbacks.
- Targeted local validation on the final source head passed: pinned .NET SDK 10.0.400 locked restore, production/test format verification, 25/25 Capabilities tests, dependency policy (51 dependencies / 238 inputs), provenance (554 files / 140 records; NOTICE unchanged), and `git diff --check`. The local filtered RP-10 ProjectGraph attempt stopped before policy assertions on unrelated Native.Image generated-implementation errors; this is not claimed as a local pass. The hosted Architecture gate passed on the exact final head.
- The normal post-merge [Publish NuGet run 36488732948](https://github.com/ArcForges/DesktopPlatform/actions/runs/36488732948) succeeded on source commit `fe48620d57a8d18f7b10d831bfa76b43227fb5d8`; publisher job 109154671158 completed successfully. Its immutable candidate was version `1.0.0-ci.52.1`, artifact `nuget-candidate-36488732948-1` (artifact ID `11000186896`, 5,567,585 bytes, archive SHA-256 `79406dbe431abf130c516d54735dda363d14633bfb5835e278462ababa18cbaf`). The manifest SHA-256 is `acfdcde4d66507080ad0f31a080e1ebc9254d1c6becc509168ab909343e76d76`; `native-artifact.json` SHA-256 is `d4b0d74e0ee558c82f6c510dcc775c11b1ddc2325f55ebd22e3475e6b797b3e7`. The manifest binds the candidate to source commit `fe48620d57a8d18f7b10d831bfa76b43227fb5d8` and build `36488732948.1`. The publisher's `packages.py verify` succeeded, and all eight extracted package file hashes independently matched the manifest:

  | NuGet package | Version | Package SHA-256 | Public index |
  |---|---|---|---|
  | ArcForges.Build.Policy | 1.0.0-ci.52.1 | `229646e28c1a3a2f19344c98a4bb32a719b1382f56616b12a1d89114a9ddc58c` | [index](https://api.nuget.org/v3-flatcontainer/arcforges.build.policy/index.json) |
  | ArcForges.Native.Abstractions | 1.0.0-ci.52.1 | `ece161cc99a0cd048b6ea1f36e98080e348de42b56c405fefc9d08ac5035d5ff` | [index](https://api.nuget.org/v3-flatcontainer/arcforges.native.abstractions/index.json) |
  | ArcForges.Native.Image | 1.0.0-ci.52.1 | `c09e3aa60de4dc0dccbb1377eeb02f19c28f7cbb9e81baeb11e31a2f321d89e0` | [index](https://api.nuget.org/v3-flatcontainer/arcforges.native.image/index.json) |
  | ArcForges.Native.Image.Runtime.win-x64 | 1.0.0-ci.52.1 | `1eeb01a82e4ab3dd7ea42be08c47990d08bbef44c29153331a8d5af207c97ba4` | [index](https://api.nuget.org/v3-flatcontainer/arcforges.native.image.runtime.win-x64/index.json) |
  | ArcForges.Foundation | 1.0.0-ci.52.1 | `a4c6deb9c6503fe22e2e2e8061062e72b3987e6e0210365d7147ff0972d7c855` | [index](https://api.nuget.org/v3-flatcontainer/arcforges.foundation/index.json) |
  | ArcForges.Application.Abstractions | 1.0.0-ci.52.1 | `c5a7cde92eee31789a59600d168bec7289a30db4fb8cd60c979321a31eea42e5` | [index](https://api.nuget.org/v3-flatcontainer/arcforges.application.abstractions/index.json) |
  | ArcForges.Capabilities | 1.0.0-ci.52.1 | `43e39d60e57ff2fc8acb20969097ae74aa49900e62498b62fb8284648cdacd0f` | [index](https://api.nuget.org/v3-flatcontainer/arcforges.capabilities/index.json) |
  | ArcForges.Persistence.Sqlite | 1.0.0-ci.52.1 | `f3938d61645d029272e6a971fed5e213a220c0fa3465cd817668223f195013fb` | [index](https://api.nuget.org/v3-flatcontainer/arcforges.persistence.sqlite/index.json) |

- NuGet publisher logs report successful pushes for all eight packages; an independent flat-container index check confirmed `1.0.0-ci.52.1` visible for all eight IDs at 2026-09-28 22:01 UTC. No public package payloads were downloaded.
- **Obligations satisfied:** WP-09.05, full — resource owner/permission/version resolution matrix and structural prohibition on location-bearing references.
- **Substitutes still in use and removing tasks:** None claimed for this task. WP-09.90 package/real-integration acceptance remains separately owned by PLT.25 and is not implied by this publication.
- **Untested coverage:** No GUI, installed-package consumer, cross-process product integration, or platform-specific runtime was exercised; these are outside WP-09.05's offline contract acceptance and no result is claimed for them.
- **Remaining completion prerequisites and next action:** None. The Design record lists no PLT.22 completion prerequisites.
