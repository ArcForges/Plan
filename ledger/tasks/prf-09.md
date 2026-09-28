---
task: PRF.09
status: complete
recorded: 2026-09-28
claimant: af-20260928-c04
epoch: 1
---

# Third-party control AOT admission gate and first candidate

## Evidence

- Implementation: [DesktopPlatform PR #86](https://github.com/ArcForges/DesktopPlatform/pull/86), exact reviewed head `8456789654544b21439e8507c66f3b2296476f65` on base `784f238c4c01590e8de6fe5e1472ed79b70ac222`; independent exact-head clean review [5339326090](https://github.com/ArcForges/DesktopPlatform/pull/86#pullrequestreview-5339326090). Squash-merged as `9e3cff458fbef1ce4326c5d8141e478ac9d11b6b`.
- The task admits Avalonia `TableView` 12.1.3 only as an isolated verification `BuildTool`, non-production and non-AOT. A separate Windows `aot-probe` job performs locked restore and `win-x64` Native AOT publish with minimal verbosity on PR and main builds; it never runs the executable or GUI and does not change product package allowlists. The fail-closed architecture matrix permits only this exact probe exclusion from default-solution selection and rejects path/classification drift or accidental inclusion.
- Local proof on source revision `0af8d140896cea353706a49a56c9952f4b5bbd3d` used pinned .NET SDK 10.0.400; locked restore and clean `win-x64` Native AOT publish passed, invoking ILC and LinkNative with 0 warnings and 0 errors. Captured log: `eng/verification/probe-evidence/prf-09-publish.log`; executable SHA-256 `B13B6401CA36A1E93F1A3C800B8CDE1062B0DB871934FAC7495DEE5349264D26`. The executable was not run.
- Exact-head hosted PR gate [run 36425378091](https://github.com/ArcForges/DesktopPlatform/actions/runs/36425378091) completed with 15/15 checks green. Independent focused probe guard tests passed 11/11 and the positive exact-selection case passed 1/1. Local verification also passed dependency policy (51 NuGet coordinates/232 inputs), provenance (523 files/140 records), evaluated licence boundary (37 projects), reconciliation (7 owners/67 projects/166 historical), runtime ownership (7 repositories), formatter verification, Release solution build (0 warnings/errors), ArchitectureTests (99/99 after rebuilding at the exact head), and `git diff --check`.
- Main publication: [Publish NuGet run 36429161576](https://github.com/ArcForges/DesktopPlatform/actions/runs/36429161576) completed successfully on merge commit `9e3cff458fbef1ce4326c5d8141e478ac9d11b6b`; all candidate and policy gates, aggregate CI, OIDC exchange, publisher, and all eight verified-byte pushes succeeded. Candidate `nuget-candidate-36429161576-1` is artifact `10972719911`, 5,552,082 bytes, archive digest `sha256:7c63ed380df99b33d889d7a911e182ed8e309a3a14cf321e4b25f4c50fe477ac`. It published version `1.0.0-ci.46.1` for `ArcForges.Build.Policy`, `ArcForges.Native.Abstractions`, `ArcForges.Native.Image`, `ArcForges.Native.Image.Runtime.win-x64`, `ArcForges.Foundation`, `ArcForges.Application.Abstractions`, `ArcForges.Capabilities`, and `ArcForges.Persistence.Sqlite`. Public NuGet flat-container index GETs confirmed the exact version for all eight IDs. A targeted retrieval of `ArcForges.Foundation` confirmed embedded build identity run `36429161576` and source commit `9e3cff458fbef1ce4326c5d8141e478ac9d11b6b`; no additional package-byte polling is claimed.
- Completion prerequisites: none remain. No shipped Avalonia dependency, product adoption, runtime execution, or GUI behavior is claimed; the probe is verification-only. The task schedules VG-03 for WP10 but is not itself the VG-03 acceptance.
- Plan ledger PR review/merge identity is retained by this ledger PR and the final PRF.09 claim record.
