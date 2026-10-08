---
task: NAT.32
status: complete
recorded: 2026-10-08
claimant: w-deku-20261008-nat-32
epoch: 1
---

# PDF engine retirement: remove native/arcpdf-abi, ArcForges.Native.Pdf and the helper PDF parser path

## Evidence

- Implementation: DesktopPlatform PR [#172](https://github.com/ArcForges/DesktopPlatform/pull/172) was reviewed and merged at head `c39ab65c13450f775c8890325e2e1e533c6c1051` as `e0f2e563bfb1a134a415b4b085dab121c66d00f9` on `main` (`--merge --match-head-commit`, integration role `integration:DesktopPlatform` held by `w-deku-20261008-coord`).
  - Independent reviewer session `w-deku-20261008-rev-nat-32` reviewed the change. Round 1 at `0d4c90dd` requested changes: two stale active-project pins, a stale `arcforges.native.abstractions` lock entry and a placeholder receipt reviewer. Round 2 at `5cec0b5c` approved.
  - Verifier session `w-deku-20261008-rev-fix1-final` approved the delta to `c39ab65c`.
  - All sessions ran under one GitHub account, so independence is by session only.
- Planning authority:
  - Decision [P2-022](https://github.com/ArcForges/ArcForges-Design/blob/main/docs/decisions/phase-2-specification-decisions.md#rule-p2-022), from Design PR #333.
  - The task record repair in Design PR [#341](https://github.com/ArcForges/ArcForges-Design/pull/341), merge `318e49735ffb1453d7bd63e0589ed1b6c34d0dc0`, with Plan PR [#457](https://github.com/ArcForges/Plan/pull/457), merge `9667e91d65cbf3ba7e41f6216a9c7068c2f7a379`. The repair states that the RPC behaviour is unchanged (P2-022 item 3) and that no retired-artifact registration is made. It also adds the stage-integration clock-test fix to the write scope.
- Outcome: the PDF engine is removed. That covers `native/arcpdf-abi`, `src/Native/ArcForges.Native.Pdf`, `NativePdfParser`, `PdfTextPager`, `IPdfParser`, `PdfPageText` and `CreatePdfParser`, with their tests, plus the common-ABI `arc_pdf_*` block, its signature pins and layout asserts, and the CMake, CTest filter, slnx, policy, provenance and reconciliation rows of the PDF targets.
  - The five ContentSandbox PDF RPCs keep the published schema: `sandbox.proto` and the `local-sandbox-1.0.0-ci.287.1` pin are unchanged.
  - Their server behaviour is unchanged. OpenPdf answers `resource.parser_failed` through an explicit return, malformed calls answer `validation.invalid_request`, the other read calls answer `state.not_found`, and ClosePdf returns its idempotent receipt. No `UNIMPLEMENTED` answer is introduced, and five closed-refusal tests assert the codes.
  - The successor dependency receipt `eng/policy/dependency-reviews/nat-32-r1.json` is chained from `nat-14-r1`. The NuGet closure (60 coordinates) and the Python closure (10) are unchanged.
- **Retired, not completed.** PDF parsing, PDF rendering, in-app PDF preview and AI PDF reading are retired under P2-022, not delivered. PG-12 is retired through its contribution text; NAT.32 does not satisfy PG-12. This record is the retirement record. No `eng/provenance/retired-artifacts.json` entry is made, because the retired PDF material was first-party and never packaged (coordinator adjudication, brief section 10).
- Candidate identity: main-push [Publish NuGet run 37827053904](https://github.com/ArcForges/DesktopPlatform/actions/runs/37827053904) (run 127, attempt 1) on `e0f2e563` succeeded and published the DesktopPlatform cohort `1.0.0-ci.127.1`. This is the provider status; nothing was downloaded. Its preflight history check passed against `f833de34`.
- Obligations: this task does not carry the WP-13.13 PDF family obligation forward. That obligation is retired by P2-022, and the NAT.15 successor split hands the still-image composition to NAT.31.
- Validation actually performed:
  - **Hosted PR gate run [37810668914](https://github.com/ArcForges/DesktopPlatform/actions/runs/37810668914) at `c39ab65c`:** 22 of 22 checks passed, including the policy, provenance, reconciliation, licence, runtime, secret-scan, stage-integration, native and managed-package jobs and the AOT compile jobs.
  - **Earlier hosted failure:** at `5cec0b5c` (run 37809098095), `stage-integration` failed. The cause was a date-dependent test: `test_snapshot_building_is_deterministic` built its snapshot with the real clock and evaluated it at the fixed 2026-10-05. It was diagnosed from the log and fixed in `c39ab65c`, not rerun blindly.
  - **WSL2 Debian 13 (kernel 6.18), SDK 10.0.400, on a Linux-native copy (P2-024):** solution `restore --locked-mode`, Release build with warnings as errors, ContentSandbox tests (98 passed, 9 opt-in OS checks skipped), NativeAbiLayout tests (3 passed), and the Native AOT publish of the helper for linux-x64.
  - **Windows SDK 10.0.401 through an uncommitted global.json adapter:** solution build, ContentSandbox tests and NativeAbiLayout tests.
  - **Python suites:** dependency policy (22), reconciliation (8), licence boundary (12), runtime ownership (26), reference baselines (13), design policy (21), architecture evidence (11) and build identity (6). The `dependency_policy`, `check_provenance` (974 files, 140 records), `reconciliation` (321 directories), `reference_baselines` and `design_policy` checks also pass.
- Substitutes still in use: none introduced or removed by this task.

## Untested coverage (stated expressly)

- The native CMake/CTest set was not run locally, because the vcpkg tree is absent on this workstation. Hosted `native-win-x64` passed.
- `licence_boundary.py` and `runtime_ownership.py --evaluate-managed` were not run locally on Windows, because SDK 10.0.400 is not installed there. Hosted CI is authoritative and passed.
- `check_compatibility` was not run in the Contracts repository. The Contracts schema and the sandbox pin are unchanged.
- The refusal tests prove that no parser is reached structurally, because no PDF parser type remains; they do not instrument parser construction.
