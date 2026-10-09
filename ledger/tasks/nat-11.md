---
task: NAT.11
status: complete
recorded: 2026-10-09
claimant: w-deku-20261008-nat-11
epoch: 1
---

# Image family: still-image codecs (PNG/TIFF/EXR)

## Evidence

- Implementation: DesktopPlatform PR [#175](https://github.com/ArcForges/DesktopPlatform/pull/175) was reviewed and merged at head `a68092e2c9def5d2ddb4a69bf607f3421a4bf815` as `c8280488a1203a5c0160bebeba48ae5f20443f9c` on `main`, with `--merge --match-head-commit`. The integration role `integration:DesktopPlatform` was held by `w-deku-20261008-coord`.
  - The independent reviewer session `w-deku-20261008-rev-nat-11` reviewed the change.
    - Round 1 at `7ac75362` had two material findings: the managed `ReadRegionAsync` could cancel after a successful native read, and `arc_image_open` wrote metadata before the handle was registered.
    - Round 2 approved `9061e47d`.
    - Each later commit got a delta review:
      - `e8dff231`, one clang-format hunk from the repository-hooks job;
      - `df3cf780`, the OpenImageIO `limits:imagesize_MB` pin;
      - `0097442f`, the GOV.18 active-project blob re-pin;
      - `71a2aec8`, the ABI 1.1 export set in packaging;
      - `a68092e2`, the native binding owner map and RP-10 contract-test map.
    - Hosted run 37892380137 at `0097442f` found the packaging export-set failure. The delta review of `0097442f` confirmed it from that log and did not approve it, so no approval comment exists for `0097442f`.
    - The `a68092e2` review approved once the ADP-07 binding was recorded in the PR and the handoff.
  - All sessions ran under one GitHub account, and the approvals are PR comments, not GitHub review events. Independence is by session only.
- Planning authority:
  - the NAT.11 record, as repaired by Design PRs [#343](https://github.com/ArcForges/ArcForges-Design/pull/343) (Annex 06 image clarification and the D5 writes), [#344](https://github.com/ArcForges/ArcForges-Design/pull/344) (write split) and [#345](https://github.com/ArcForges/ArcForges-Design/pull/345) (path rows);
  - the coordinator decisions D1 to D12, plus straight alpha and the packaging check.
- Outcome:
  - `arc_image_open`, `arc_image_read` and `arc_image_close` are implemented in `native/arcimage-abi` (logical library ArcImageNative, ABI 1.1) over OpenImageIO 3.1.14.0 with OpenEXR and Imath. They provide PNG, TIFF and EXR metadata and bounded tiled and region reads, straight alpha (byte-exact 8-bit PNG and TIFF RGBA), the output format selected at open, raster-order coverage, cancellation at tile boundaries, bounded handles, decompression-bomb refusal before allocation, and CORRUPT and unsupported-format refusal.
  - OpenImageIO's `limits:imagesize_MB` is pinned to the shim's bounds (131072 MiB), so the size authority does not depend on host memory.
  - The managed binding `ArcForges.Native.Image` provides `ImageReader`, a SafeHandle owning the generation token, typed options and results, `IAsyncDisposable`, and a completion step that refuses missing coverage. It builds with warnings as errors under the IsAotCompatible (trim and AOT) analyzers. Analyzer-level evidence is the only AOT evidence: see the untested coverage.
  - Deviation from D4, recorded in the review: the rgba8 bit-depth mapping uses the shim's own clamp and round-to-nearest, not OpenImageIO `convert_type`. The observable semantics match D4 (clamp to [0,1], round to nearest, exact 8-bit round trips), and the tests pass.
  - Size pin note: on hosts below 128 GiB, OpenImageIO's open-time parsing now admits larger declared headers before the shim's own checks. This is the same exposure large hosts already had. Containment was NAT.31's, which is now out of scope.
- **ADP-07 supporting-file bindings**, outside the NAT.11 writes list (D5 authorised only `eng/packaging/native_consumer.py` among the packaging files), recorded in the PR body and the claim handoff: `eng/packaging/native.py`, `eng/packaging/packages.py`, `tests/ArchitectureTests/RepositoryPolicyTests.cs` and `eng/policy/architecture-contract-tests.json`. They hold append-only rows for the ABI 1.1 exports, the single binding owner and the RP-10 contract-test map, and add no exemption. No dependency receipt binds their hashes.
- Candidate identity (D7):
  - Main-push [Publish NuGet run 37917316227](https://github.com/ArcForges/DesktopPlatform/actions/runs/37917316227) (run 130, attempt 1) on `c8280488` succeeded and published the DesktopPlatform cohort `1.0.0-ci.130.1`.
  - Its publish job log shows 17 'Your package was pushed' lines, including `ArcForges.Native.Image.1.0.0-ci.130.1` and `ArcForges.Native.Image.Runtime.win-x64.1.0.0-ci.130.1`.
  - Package hashes and registry receipts were not captured. This is the provider status, and nothing was downloaded.
- Dependency receipt: `eng/policy/dependency-reviews/nat-11-r1.json`, chained from `gov-30-r1`, names the reviewer and reviewedOn 2026-10-09. Its `maintenanceAssessment` text still says the review is pending; that sentence is stale, and the approval is recorded in the PR #175 comments. Committed receipts are not rewritten.
- `delivery.py check` reports, among its warnings, an unordered write overlap between NAT.11 and APP.07 on `eng/provenance/files.json` in DesktopPlatform. The provenance rows are append-only; this is noted for APP.07.
- Validation actually performed:
  - **Hosted PR gate [run 37913132381](https://github.com/ArcForges/DesktopPlatform/actions/runs/37913132381) at `a68092e2`:** 22 of 22 checks passed, including `native / native-win-x64` (configure, build, CTest with the CI filter, stage), `managed-packages / pack` (platform validation, architecture tests, invariant accounting, pack and PackageGuards), every policy job, secret-scan, repository-hooks, stage-integration and the AOT compile jobs.
  - **Earlier hosted failures**, each diagnosed from the log and fixed, never rerun blindly:
    - run 37889757342 at `e8dff231`: `codec.limits_bomb`, because OpenImageIO's host-memory default limit applied;
    - run 37892380137 at `0097442f`: the packaging export set;
    - run 37895016174 at `71a2aec8`: the architecture binding owner and RP-10. The invariant-accounting "Malformed TRX" was downstream of the RP-10 message.
  - **Local, on Windows through the workstation build slot:**
    - win-x64 shim-static configure, build and install with `/W4 /WX` and zero warnings; CTest with the CI filter, 37 of 37; the codec executable, 374 checks;
    - NativeAbiLayout 3/3 and NativeAbi functional 16/16;
    - managed builds under the pinned SDK 10.0.400 with 0 warnings, and `dotnet format`;
    - every test suite of the managed-packages platform validation (architecture 134/135; the one failure reads hosted-only evidence) and invariant accounting;
    - AOT compile-only publishes for win-x64, and for linux-x64 in WSL Debian;
    - gitleaks at the pinned digest (from the image already in WSL Docker): 422 commits, no leaks;
    - pre-commit;
    - every policy job and its unit suites.
- Obligations: WP-13.10 (full), with package-level contributions to WP-13 ss1 and ss4.
- Substitutes still in use: none introduced or removed by this task.

## Scope (2026-10-09)

Under the user's scope correction of 2026-10-09 (planning repair P2-026), NAT.11 was finished as an in-progress DesktopPlatform delivery under the DesktopPlatform exception: review, CI, merge and publication closeout, and then it stops.

- NAT.11 is not an ArcScope prerequisite.
- The production containment of hostile image reads in the ContentSandbox helper (NAT.31, PLT.54) and the other-RID packages (NAT.22, NAT.25) are out of scope under P2-026. They are not completed.
- The outcome clause "hostile reads execute only in the WP11 helper" was recorded under decision D1 as the NAT.31 and PLT.54 residual. With those tasks out of scope, the residual is out of scope, not delivered.

## Untested coverage (stated expressly)

- **linux-x64 native build:** not run. Under D8 it is a local WSL2 opt-in, and WSL lacks cmake, ninja and libtool, which are user installs. win-x64 is the required leg and the CI authority.
- **Packaging stage, pack and PackageGuards:** not run locally, because the reviewed owned CMake 4.3.3 and Ninja 1.13.1 are not installed. Hosted CI ran and passed them.
- **NativeAbi functional suite:** a local opt-in; hosted CI filters on NativeAbiLayout.
- **Native AOT consumer publish of `ArcForges.Native.Image`:** not run, locally or hosted. None of the hosted AOT compile jobs names it. Only the IsAotCompatible analyzers ran, with 0 warnings.
