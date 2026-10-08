---
task: GOV.32
status: complete
recorded: 2026-10-08
claimant: w-deku-20261008-gov-32
epoch: 1
---

# Remove the ContentSandbox macOS launch-profile code and keep the typed fail-closed refusal

## Evidence

- Implementation: DesktopPlatform PR [#173](https://github.com/ArcForges/DesktopPlatform/pull/173) was reviewed and merged at head `45343a42609cc16b319493134bf1d27b122ab18d` as `6f21d73e0ef6953138ff264ced195fde3b28fe93` on `main` (`--merge --match-head-commit`, integration role `integration:DesktopPlatform` held by `w-deku-20261008-coord`).
  - Independent reviewer session `w-deku-20261008-rev-gov-32` reviewed it in two rounds. Round 1 verified it by inspection, but its validation could not run, because the PATH `dotnet` lacked the pinned SDK 10.0.400. Round 2 approved it with the full validation listed below.
  - The approvals are PR comments from one GitHub account, so independence is by session only.
- Planning authority: [P2-023](https://github.com/ArcForges/ArcForges-Design/blob/main/docs/decisions/phase-2-specification-decisions.md#rule-p2-023) item 4. The task was created by Design PR [#341](https://github.com/ArcForges/ArcForges-Design/pull/341) (merge `318e49735ffb1453d7bd63e0589ed1b6c34d0dc0`) with Plan PR [#457](https://github.com/ArcForges/Plan/pull/457) (merge `9667e91d65cbf3ba7e41f6216a9c7068c2f7a379`).
- Outcome:
  - **Deleted:** the declarative entitlements input `src/DesktopHelpers/ArcForges.ContentSandbox/macos/ArcForges.ContentSandbox.entitlements`, with its `eng/provenance/files.json` row.
  - **Refusal:** `ProfileEnforcement.ThisPlatform` is now a nullable `ContentSandboxProfileKind?` that is null on every OS other than Windows and Linux. `HelperEntry` compares the frame profile with it unchanged, so every launch frame there, including one carrying the reserved `MacOsAppSandboxXpc`, exits with the isolation-unavailable code (70) before any resource or parser is reached.
  - **Tests:** `Tests/MacProfileTests.cs` is refusal-only. It proves the broker refusal, that the reserved value stays at wire value 3, that the Windows (1) and Linux (2) kinds are unchanged, and that a helper given a `MacOsAppSandboxXpc` frame exits 70. The `Tests/ContractFacadeTests.cs` refusal check covers every non-Windows, non-Linux OS.
  - **Docs:** the README macOS lines and the doc comments of the reserved enum value state that macOS is not supported.
  - **Unchanged:** the Windows and Linux branches. The broker's typed fail-closed macOS refusal (`ContentSandboxLauncher.cs`) is unchanged and was not edited.
- Candidate identity: main-push [Publish NuGet run 37846186616](https://github.com/ArcForges/DesktopPlatform/actions/runs/37846186616) (run 128, attempt 1) on `6f21d73e` succeeded, with preflight passing. It published the DesktopPlatform cohort `1.0.0-ci.128.1`; its publish job log shows 17 'Your package was pushed' lines. Package hashes and registry receipts were not captured. This is the provider status, and nothing was downloaded.
- Obligations: P2-023 (governance obligation). The macOS App-Sandbox and XPC launch-profile deliverable is removed from the ContentSandbox code. The typed fail-closed refusal and the wire-stable enum value stay.
- Validation actually performed:
  - **Hosted PR gate on `45343a42`:** 22 of 22 checks passed, including the policy, provenance, reconciliation, licence, runtime, secret-scan, stage-integration, native and managed-package jobs and the Content helper AOT compile jobs.
  - **Reviewer, Windows, SDK 10.0.400** (from `C:\Users\J7Rdm\.dotnet`, first on PATH with `DOTNET_ROOT`): ContentSandbox tests restored `--locked-mode` and built with warnings as errors (0 warnings, 0 errors). Tests: 110 total, 101 passed, 0 failed, 9 skipped.
  - **Reviewer, WSL2 Debian 13, SDK 10.0.400, Linux-native clone (P2-024):** the same restore and build, with the same test totals.
  - **Python gates:** design policy, dependency policy, licence boundary (`--evaluate-managed` and `--evaluate-ide`), reference baselines, runtime ownership, architecture naming evidence, reconciliation, provenance, native provenance and stage-integration verify all pass, as do the `eng` (119), `tests/tooling` (51), `stage_integration` (47) and `accounting` (10) unit suites.
  - **Static scan:** no App-Sandbox, XPC or entitlements profile code remains outside the reserved enum value, the launcher refusal and the docs and tests that state macOS is unsupported.
- Substitutes still in use: none introduced or removed.

## Untested coverage (stated expressly)

- The 9 opt-in OS isolation tests (`OsIsolationTests`, which need `ARCFORGES_CONTENTSANDBOX_OS=1` and a published hostile fixture) were skipped on both platforms. The change does not touch the Windows or Linux containment branches.
- The `eng/packaging` unit suite needs the pack output, so 13 of its 25 tests error locally without it. Hosted package-validation packs first and passed.
- No macOS run exists or is claimed (P2-017, P2-023).
- `ContentSandboxLauncher.ProbeProfile()` on macOS still reports the reserved value as an unavailable profile, with a reason text describing the removed bundle/XPC handoff. The refusal is correct, but the wording is outside this task's write scope. It is carried as a non-blocking note.
