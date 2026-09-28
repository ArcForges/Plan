---
task: PLT.42
status: complete
recorded: 2026-09-28
claimant: af-20260928-g02
epoch: 1
---

## Evidence

- Pull requests (implementation, documentation, ledger), each with its reviewed head commit and merge commit:
  - DesktopPlatform PR [#91](https://github.com/ArcForges/DesktopPlatform/pull/91): reviewed head `c123ed25b6c019c78338baf5417dca146905b9d1`, base `a2c36acfef24e3cbbc1b44ec0a013114b0aec38b`, merged as `213424c4944e7ed208ef21f3493068fcc26c7210`. Independent scoped exact-head clean review: [review 5342532447](https://github.com/ArcForges/DesktopPlatform/pull/91#pullrequestreview-5342532447).
- Published candidate identities (package, version, hash, registry receipt) and the CI and publication runs:
  - Normal Publish NuGet run [36460394855](https://github.com/ArcForges/DesktopPlatform/actions/runs/36460394855) completed successfully on source `213424c4944e7ed208ef21f3493068fcc26c7210`; candidate CI and OIDC publisher both succeeded. Candidate artifact `nuget-candidate-36460394855-1`, artifact ID `10987147230`, size `5,552,044` bytes, SHA-256 `a1fcba17f5742c1708c87e585fc6a1575e4b0a8b39415c0efb31707ad72d31d0`.
  - Publisher verified and pushed all eight allowlisted packages at version `1.0.0-ci.50.1`: `ArcForges.Build.Policy`, `ArcForges.Native.Abstractions`, `ArcForges.Native.Image`, `ArcForges.Native.Image.Runtime.win-x64`, `ArcForges.Foundation`, `ArcForges.Application.Abstractions`, `ArcForges.Capabilities`, and `ArcForges.Persistence.Sqlite`. By `2026-09-28T18:06:55Z`, all eight public NuGet flat-container indexes listed the exact version; package payloads were not downloaded.
  - These eight packages are the repository-level release allowlist evidence, not a direct PLT.42 package. `ArcForges.Security.csproj` inherits `<IsPackable>false</IsPackable>` from `Directory.Build.props` and `ArcForges.Security` is absent from `eng/packaging/packages.json`; PLT.42 did not publish or admit a Security package. PLT.46 owns the later Security package admission, publication, and independent-consumer acceptance.
- Obligations satisfied (substep or package obligation and part):
  - WP-11.06 (full): instruction-bearing inputs carry immutable origin/source/content provenance; all six origins remain explicitly untrusted, provenance cannot grant operation authority, and snapshots preserve and validate provenance across boundaries. Added injection, completeness, tampering, and bounded-encoding regressions.
- Validation actually performed (CI checks, local runtime checks with environment identity):
  - Exact-head PR run [36458819651](https://github.com/ArcForges/DesktopPlatform/actions/runs/36458819651) completed successfully with all 15 checks green, including Security architecture/RP-10 policy, native Windows, managed package pack, Linux/Windows Local RPC AOT, TableView AOT, and aggregate CI.
  - Local exact-candidate Security.Tests: 28 passed, 0 failed, 0 skipped; Security and Security.Tests formatting verification passed. Provenance gate passed (546 files/140 records); dependency policy passed (51 NuGet, 10 Python, 238 inputs); licence boundary passed (40 projects); JSON parse and `git diff --check` passed.
  - The two approved local focused EPT attempts did not reach the RP-10 assertion: the first child process resolved SDK 10.0.401 instead of pinned 10.0.400; after process-local SDK path correction, the narrowly restored project lacked full-graph Build.Policy `project.assets.json`. The hosted managed-packages pack gate on run 36458819651 performed full locked solution restore and passed platform-ownership tests; these local preparation failures are not reported as test failures or green evidence.
  - Post-merge Publish NuGet run 36460394855 completed successfully (17 jobs); candidate gates, OIDC exchange, and all eight package pushes succeeded.
- Substitutes still in use and their removing tasks: No substitute implementation or temporary authority was introduced or relied on by PLT.42.
- Untested coverage: No hosted runtime/device/GUI/browser/live-service/inference/installed-consumer validation was performed; such validation is excluded by the task's P2-017 boundary. The offline injection, marking, security, packaging, and current-head CI acceptance criteria passed as recorded above.
- Remaining completion prerequisites and next action (delivered only): None; the task has no completion prerequisites.
