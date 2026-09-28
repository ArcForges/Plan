---
task: PLT.08
status: complete
recorded: 2026-09-29
claimant: af-20260928-p02
epoch: 1
---

# Package owned local persistence capabilities

## Evidence

- Implementation: DesktopPlatform [PR #93](https://github.com/ArcForges/DesktopPlatform/pull/93), final reviewed head `d9d2c61e91acb260d6fd6db04cd1ea11ddc4d884` on base `94b3f12e802c225ac16fea4b72ceb2717214a32b`; independent exact-head COMMENTED clean review [5345662963](https://github.com/ArcForges/DesktopPlatform/pull/93#pullrequestreview-5345662963). Merged as `a3391d4440ea0fa2d16b5d0843e4191d24eb2008`.
- Scope and ownership: the nine-file change adds only the two existing Resources and Derived projects to the package allowlist and supplies their authorized pack/readme/description metadata plus narrow package-input, provenance, receipt and active-project-hash bindings. Resources retains its existing Foundation project reference and exact `ArcForges.Contracts.Foundation` pin; Derived remains dependency-free. Both preserve the existing AGPL-3.0-only metadata. No public API, schema, workflow, lock, solution, dependency coordinate/version/closure, or pack algorithm changed. The product consumer—not these shared persistence packages—owns its canonical record, schema and migration.
- Latest-head hosted PR gate [run 36494764557](https://github.com/ArcForges/DesktopPlatform/actions/runs/36494764557) completed successfully (15/15). It includes secret-scan, policy/reconciliation/provenance/reference/licence/runtime checks, native Windows, managed pack, Linux and Windows Local RPC AOT compile probes, Avalonia AOT compile probe, and aggregate CI.
- Dependency admission: immutable `plt-08-r1.json` succeeds `plt-47-r1.json`; the active receipt retains the same 51 NuGet and 10 Python dependency closure and all PLT.47 Observability inputs. The task adds no dependency. The candidate input set has 240 exact hashes. Local dependency admission and provenance validation passed on the final source head; provenance covered 564 files, 10 reused records and 140 records, with generated NOTICE SHA256 unchanged at `9fa2317d54eb0256911ab0feeec394e30429d4040616f4a1a00bfa19ad8a0cac`.
- Normal post-merge [Publish NuGet run 36496295310](https://github.com/ArcForges/DesktopPlatform/actions/runs/36496295310) completed successfully on merge commit `a3391d4440ea0fa2d16b5d0843e4191d24eb2008`. Publisher job `109178782580` authenticated through GitHub OIDC, reverified the source/allowlist/manifest, and reported successful pushes for all ten packages using the retained candidate bytes. Candidate artifact `nuget-candidate-36496295310-1`, artifact `11003443213`, is 5,645,950 bytes with API digest `sha256:3f7d1915673d69ded4d7eded01ec0ab8a1fb9a2dfa755c29e1faabbc011965d1`. Its manifest SHA256 is `d488f8f7142f8fb4b59a2a33231fbd433ca27b04a7022ff73649a06a122b9f50`; manifest source is the merge commit above, and published version is `1.0.0-ci.54.1`. `packages.py verify` confirmed all ten package archives against that exact source/version manifest.
- Published package hashes from the verified normal-publish manifest:

  | Package ID | Version | SHA256 |
  |---|---|---|
  | `ArcForges.Build.Policy` | `1.0.0-ci.54.1` | `10b6c87aa3d16c17aebd708035af5d0e3f3e0496bb080c563ebdd75db6d25abc` |
  | `ArcForges.Native.Abstractions` | `1.0.0-ci.54.1` | `c55b38b113501e42d6ce648b309ff6c417dc5f5f6fbae52ae1fef9964401c9ab` |
  | `ArcForges.Native.Image` | `1.0.0-ci.54.1` | `c57d3adaacff473bb614e4c202938cd5be0c8ba333800b2dc0fab3bc987e2be8` |
  | `ArcForges.Native.Image.Runtime.win-x64` | `1.0.0-ci.54.1` | `d16e2daa540402439b83ad0eb3cdd921af995e175582110c09e92b927da1aa21` |
  | `ArcForges.Foundation` | `1.0.0-ci.54.1` | `722c5c3b1ddd512a7b561f939896ce8b258440ffcaf3206b72dbea7a2753bbac` |
  | `ArcForges.Application.Abstractions` | `1.0.0-ci.54.1` | `0cf8db4ef88e59281c910de4b700c37ce8649bf55344b552b50e930f26ac8963` |
  | `ArcForges.Capabilities` | `1.0.0-ci.54.1` | `bc1eb34c5fc33f91fd23d7309055d1f962ef97c76db177b9f5b19f3d23a0a8c3` |
  | `ArcForges.Persistence.Sqlite` | `1.0.0-ci.54.1` | `95802aacf66c5cdbec61659f966d1733e41f368956ae60cff9e711a318fbae30` |
  | `ArcForges.Persistence.Resources` | `1.0.0-ci.54.1` | `69a5fac0eb59deedc6e41022d04a2c72f3d87046eb308e4e9bde1617238e24b5` |
  | `ArcForges.Persistence.Derived` | `1.0.0-ci.54.1` | `fa87e7e1b19baac9ca866e96bf967dac221a1efb9ca3abd423f35209aaf1a962` |

- Public availability: direct read-only GETs of the ten exact nuget.org flat-container `index.json` endpoints confirmed `1.0.0-ci.54.1` in every package index. No public package payload was downloaded for post-publication verification.
- Real-integration receipt: an isolated consumer project outside the repository consumed the retained PR-gate candidate artifact `11002952070` (5,646,194 bytes; `sha256:8ea6bf9015211e17523550ce75a0ee31b93700b0ee96192291037c48706fefd8`), version `1.0.0-ci.36494764557.1`, manifest SHA256 `c4d61a9e50c3e921a24313aa93541537669d40acd46bae96780ec89544c350da`, source candidate merge commit `fe6372d2f4926b798c392465ebff14bfc5d87257`. The consumer had no `ProjectReference`; only the exact four IDs `ArcForges.Foundation`, `ArcForges.Persistence.Sqlite`, `ArcForges.Persistence.Resources`, and `ArcForges.Persistence.Derived` mapped to the candidate directory, while all other dependencies resolved from nuget.org. It used a fresh isolated NuGet cache and locked restore; each resolved candidate `.nupkg` hash matched its manifest entry. `ArcForges.Contracts.Foundation` resolved to exact external pin `1.0.0-ci.113.1`, and `Microsoft.Data.Sqlite` to `10.0.12`.
- Exact candidate package hashes observed in that isolated consumer cache:

  | Package ID | SHA256 |
  |---|---|
  | `ArcForges.Foundation` | `ed428dc77ec1ac6353ebe61396e5b042c6453c12335f6fb042b047943041676c` |
  | `ArcForges.Persistence.Sqlite` | `074a0f350c818f13b2d2487a3a971eb247ad9d7a5fba1c26e676e703fd3ec8e6` |
  | `ArcForges.Persistence.Resources` | `7514789522e6533bb8085095c831a75398b8ccd56f087626e28e190cec2b68c2` |
  | `ArcForges.Persistence.Derived` | `697e4d1b827abfd19c27761b51c154886fdae67c43473f95984c4756df5344e4` |
- Consumer scenario/result: on Windows 10.0.26200 with .NET runtime 10.0.11, the external product-owned `ProductRecord`, schema and migration completed a SQLite round-trip; managed-resource round-trip passed; the derived store was built and evicted. Canonical SQLite SHA256 was `4f08e89126db4e87019abff217ba2931f8604cdf4e3a101cafae4818d538ee79` both before and after eviction, resource bytes were preserved, and the derived directory was removed. Transcript: `C:\Users\J7Rdm\AppData\Local\Temp\ArcForges-PLT08-FinalGate-20260928\Consumer-36490816614\consumer-run-36494764557.log`. This is a real, repository-external Windows package consumer, not a fixture-only or hosted consumer.
- Validation actually performed on the final source head: pinned .NET SDK 10.0.400 locked solution restore, full-solution format verification, and Release build (0 warnings/errors); Foundation 65/65, Resources 19 passed with 2 explicit process-kill skips, Derived 15/15, and Persistence 81/81. Dependency policy passed (51 NuGet, 10 Python, 240 inputs) and its tests 16/16; licence boundary passed for 41 projects; default reconciliation passed for 7 owners / 67 projects / 166 historical entries / 326 directories / 7 native entries; native provenance passed for 21 components; runtime ownership passed for 7 repositories. Hosted exact-head CI is the authoritative full policy/security/native/AOT/pack gate. Local Docker Gitleaks was not run under the execution policy; the hosted exact-head secret-scan passed.
- Obligations satisfied: WP-07.90 (full). The package consumer proves that publishing and consuming these persistence mechanisms does not centralize product-owned canonical records/schema/migrations. The existing persistence recovery/profile evidence remains in the PLT.01–PLT.07 producer records; this packaging task did not change those profiles or claim to repeat their recovery matrix.
- Substitutes still in use: none for the PLT.08 package-consumption boundary. The consumer uses the exact retained PR candidate packages and owns its schema/data; it is not a mocked package reference.
- Untested coverage and limits: the external consumer was run once on Windows only; no Linux/macOS runtime, hosted consumer, or hardware-level crash/recovery claim is made. These are outside this task's package-validation scope/P2-017. Normal post-publication verification used publisher receipt/manifest and ten public version indexes only; no package payload download/install/hash was performed after publication.
- Completion prerequisites and next action: none. PLT.08 is complete.
