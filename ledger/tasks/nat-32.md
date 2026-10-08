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
  - All sessions ran under one GitHub account, and the approvals are PR comments, not GitHub review events. Independence is by session only.
- Planning authority:
  - Decision [P2-022](https://github.com/ArcForges/ArcForges-Design/blob/main/docs/decisions/phase-2-specification-decisions.md#rule-p2-022), from Design PR #333.
  - The task record repair in Design PR [#341](https://github.com/ArcForges/ArcForges-Design/pull/341), merge `318e49735ffb1453d7bd63e0589ed1b6c34d0dc0`, with Plan PR [#457](https://github.com/ArcForges/Plan/pull/457), merge `9667e91d65cbf3ba7e41f6216a9c7068c2f7a379`. The repair states that the RPC behaviour is unchanged (P2-022 item 3) and that no retired-artifact registration is made. It also adds the stage-integration clock-test fix to the write scope.
- Outcome: the PDF engine is removed. That covers `native/arcpdf-abi`, `src/Native/ArcForges.Native.Pdf`, `NativePdfParser`, `PdfTextPager`, `IPdfParser`, `PdfPageText` and `CreatePdfParser`, with their tests, plus the common-ABI `arc_pdf_*` block, its signature pins and layout asserts, and the CMake, CTest filter, slnx, policy, provenance and reconciliation rows of the PDF targets.
  - The five ContentSandbox PDF RPCs keep the published schema: `sandbox.proto` and the `local-sandbox-1.0.0-ci.287.1` pin are unchanged.
  - Their server behaviour is unchanged. Each PDF call is first gated on a live session (`PdfCallIsLive`); a call outside a live session or with a malformed request or document id answers `validation.invalid_request`. In a live session, OpenPdf answers `resource.parser_failed` through an explicit return, GetPdfPage, ExtractPdfText and RenderPdfTile answer `state.not_found`, and ClosePdf returns its idempotent receipt. No `UNIMPLEMENTED` answer is introduced. Four closed-refusal tests assert the codes of OpenPdf, GetPdfPage, ExtractPdfText and RenderPdfTile, and one test asserts the ClosePdf receipt and its `validation.invalid_request` answer for malformed input.
  - The successor dependency receipt `eng/policy/dependency-reviews/nat-32-r1.json` is chained from `nat-14-r1`. The NuGet closure (60 coordinates) and the Python closure (10) are unchanged.
- **Retired, not completed.** PDF parsing, PDF rendering, in-app PDF preview and AI PDF reading are retired under P2-022, not delivered. PG-12 is retired through its contribution text; NAT.32 does not satisfy PG-12. This record is the retirement record. No `eng/provenance/retired-artifacts.json` entry is made, because the retired PDF material was first-party and never packaged (coordinator adjudication, brief section 10).
- Candidate identity: main-push [Publish NuGet run 37827053904](https://github.com/ArcForges/DesktopPlatform/actions/runs/37827053904) (run 127, attempt 1) on `e0f2e563` succeeded and published the DesktopPlatform cohort `1.0.0-ci.127.1`. Its publish job log shows 17 'Your package was pushed' lines, including ArcForges.Native.Abstractions, ArcForges.Native.Image, ArcForges.LocalRpc and ArcForges.Build.Policy, and no ArcForges.Native.Pdf package. Package hashes and registry receipts were not captured; this is the provider status and nothing was downloaded. The run's preflight history check passed against `f833de34`.
- Compatibility result: the Contracts repository is not changed by NAT.32, and no Contracts pull request references it. On Contracts main `330e46bd`, [CI run 37725260719](https://github.com/ArcForges/Contracts/actions/runs/37725260719) (2026-10-08, job 'Build candidate', success) ran `eng/check_compatibility.py --window`. For `local-sandbox-1.0.0-ci.287.1` its report shows identical pinned and current definitions (102 messages, 9 enums, 1 service, 2 files) and 0 errors, and 0 errors in both exchange directions (previous-client/current-server and current-client/minimum-server, 121 samples each). The whole report has `errors: []`. `sandbox.proto` itself last changed in Contracts commit `2f0a51b` (2026-09-27), the pin `eng/compatibility/local-sandbox-1.0.0-ci.287.1.binpb` last changed in `88a1988` (2026-10-02, CON.17), and NAT.32 touches no Contracts file, so the schema and the pin are unchanged.
- Obligations: NAT.32 contributes to `WP-13:ss4-major-types-note-no-native-pointer-b` by removing the PDF native types, and satisfies no obligation in full. It does not carry the WP-13.13 PDF family obligation forward: that obligation is retired by P2-022, and the NAT.15 successor split hands the still-image composition to NAT.31.
- Validation actually performed:
  - **Hosted PR gate run [37810668914](https://github.com/ArcForges/DesktopPlatform/actions/runs/37810668914) at `c39ab65c`:** 22 of 22 checks passed, including the policy, provenance, reconciliation, licence, runtime, secret-scan, stage-integration, native and managed-package jobs and the AOT compile jobs.
  - **Earlier hosted failure:** at `5cec0b5c` (run 37809098095), `stage-integration` failed, and the aggregate `ci` gate failed at 16:41:18Z. Run 37810668914, created at 16:40:43Z for the next push, had already superseded the run (pr-gate concurrency cancels in-progress runs of the same ref) and cancelled its still-running `managed-packages / pack` at 16:40:56Z. The cause was a date-dependent test: `test_snapshot_building_is_deterministic` built its snapshot with the real clock and evaluated it at the fixed 2026-10-05. It was diagnosed from the log and fixed in `c39ab65c`, not rerun blindly.
  - **WSL2 Debian 13 (kernel 6.18), SDK 10.0.400, on a Linux-native copy (P2-024):** solution `restore --locked-mode`, a Release build with warnings as errors (the reviewer's full-solution rerun used a python3 shim and its result was not read; the hosted build jobs passed), ContentSandbox tests (98 passed, 9 opt-in OS checks skipped), NativeAbiLayout tests (3 passed), and the Native AOT publish of the helper for linux-x64.
  - **Windows SDK 10.0.401 through an uncommitted global.json adapter:** solution build, ContentSandbox tests and NativeAbiLayout tests. The Windows Native AOT build of the helper is covered by the hosted 'managed-packages / Content helper AOT compile (win-x64)' job, which passed at `c39ab65c`; it was not published locally.
  - **Python suites:** dependency policy (22), reconciliation (8), licence boundary (12), runtime ownership (26), reference baselines (13), design policy (21), architecture evidence (11) and build identity (6). The `dependency_policy`, `check_provenance` (974 files, 140 records), `reconciliation` (321 directories), `reference_baselines` and `design_policy` checks also pass.
- Substitutes still in use: none introduced or removed by this task.

## Untested coverage (stated expressly)

- The native CMake/CTest set was not run locally, because the vcpkg tree is absent on this workstation. Hosted `native-win-x64` passed.
- `licence_boundary.py` and `runtime_ownership.py --evaluate-managed` were not run locally on Windows, because SDK 10.0.400 is not installed there. Hosted CI is authoritative and passed.
- `check_compatibility` was not run locally for this task; the result cited above is the Contracts main CI run at the unchanged Contracts head.
- The refusal tests prove that no parser is reached structurally, because no PDF parser type remains; they do not instrument parser construction.
