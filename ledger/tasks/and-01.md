---
task: AND.01
status: delivered
recorded: 2026-10-09
claimant: w-deku-20261008-and-01
epoch: 1
---

# Android production identity and .NET MAUI toolchain pins

## Evidence

- Implementation: Mobile PR [#22](https://github.com/ArcForges/Mobile/pull/22) was reviewed and merged at head `c22298fb9f6b1ffc2b6401e9fde177a8a65df4ab` as `35fdfa63b8f757670246130133b18ee6e0fe5968` on `main` (`--merge --match-head-commit`, integration role `integration:Mobile` held by `w-deku-20261008-coord`).
  - Head `c22298fb` merges Mobile main `685a4772`, the maintenance PR [#23](https://github.com/ArcForges/Mobile/pull/23) that admitted Gradle 9.8.1, Kotlin 2.4.21 and Spotless 8.10.4 after their upstream releases turned lint red.
- Review: independent reviewer session `w-deku-20261008-rev-and-01`.
  - Round 1 at `8c53752`: the lock admission was bound to CRLF bytes.
  - Round 2 at `08e8d02`: notice obligations were ungated, and the workload admission was missing.
  - Round 3 at `380a123`: the write scope, runtime-shaped application source, and Contracts `1.0.0-ci.350.1` from a rolled-back commit.
  - Round 4 approved at `c48eb7c`. The deltas `8eef355`, `e18e156` and `90ae491` were then verified.
  - The first hosted run at `90ae491` failed the Gradle gates `:verifyMobilePolicy` and `:app:verifyAndroidLicences`. The cause was the .NET project row in the Gradle-read `licence-boundary.json`. Fix `8cd770a` was approved after all gates passed, and merge head `c22298fb` was approved.
  - The approvals are PR comments from one GitHub account, so independence is by session only.
- Planning authority: [P2-021](https://github.com/ArcForges/ArcForges-Design/blob/main/docs/decisions/phase-2-specification-decisions.md#rule-p2-021) item 3. The write scope, the rolled-back candidate rule, the Linux identity-build deferral to AND.40 and the AND.22 ordering come from Design PR [#342](https://github.com/ArcForges/ArcForges-Design/pull/342) (merge `c84f8b2f9f5ac41de322598d80893d8f261d8a57`) with Plan PR [#458](https://github.com/ArcForges/Plan/pull/458) (merge `47dd08c7b6907e7aca948fbe76d181050f566772`).
- Outcome (see `docs/maui-toolchain.md` at `35fdfa63`):
  - **Identity:** applicationId `com.arcforges.mobile`, with namespace and source root `ArcForges.Mobile`. The reinstall guidance from the development prerelease `io.github.arcforges.mobile` is in `docs/releasing.md`: reinstall, with no data migration. The persistent release signing identity (cert SHA-256 `7a8b3b14…`) is kept.
  - **Pinned candidate tuple:**
    - SDK 10.0.400 with `rollForward: disable`;
    - `net10.0-android` only, with `UseMonoRuntime=true`;
    - workloads `android` 36.1.69 and `maui-android` 10.0.20;
    - `Microsoft.Maui.Controls` 10.0.20 and a central `Microsoft.NET.ILLink.Tasks` 10.0.11;
    - NuGet locked restore from nuget.org only (117 locked packages);
    - target API 36.1 (coordinator D-016 decision) and minimum API 26.
  - **Admission:** `nuget-admission.json`, `workload-admission.json` and `dotnet-toolchain.json`; the inventory receipts `maui-identity-inventory-r1` to `r3` (r3 is active at the AND.01 head and names the reviewer); and `eng/policy/dotnet-licence-boundary.json` for the .NET project.
  - **Contracts:** `ArcForges.Contracts.PublicApi` and `Foundation` at `1.0.0-ci.324.1`, published from Contracts main `330e46bd` by run 37388554007. Compile-only generated-client compatibility evidence is `Compatibility/ContractsClientCompatibility.cs`.
  - **Identity-only project:** no permission, no launchable activity and no UI.
  - **Gate:** `eng/maui_identity.py` checks the tuple, the admissions, the file shape, the namespace, and the APK badging and certificate.
  - **Kotlin baseline:** unchanged until AND.40.
- Candidate identity: none for the MAUI project. AND.01 publishes no MAUI candidate; the first MAUI release-build proof is AND.40's CI, then PRF.12. The main-push CI on `35fdfa63` builds the unchanged Kotlin baseline.
- Obligations: WP-30.00 (all work except the parts mapped to AND.04) and the WP-30 Apache-2.0 boundary contribution, delivered on candidate pins. Completion waits for the items below.
- Validation actually performed:
  - **Hosted PR CI at `c22298fb`:** every check passed. That covers Build on ubuntu-latest and windows-latest, Verify, CodeQL for actions, java-kotlin and python, dependency review and secret scan.
  - **Windows identity builds, recorded in `docs/maui-toolchain.md`:**
    - SDK 10.0.401, because the pinned MAUI workloads are installed only under that SDK root;
    - JDK 21 (Temurin 21.0.11) and Android platform 36.1 / build-tools 36.1.0;
    - a locked restore into a clean NuGet folder;
    - Debug (0 warnings) and Release with R8 (2 SDK advisory warnings);
    - `maui_identity --apk` on both APKs: `com.arcforges.mobile`, minSdk 26, targetSdk 36, one signer, no INTERNET permission, no launchable activity, debug-signed.
  - **Reviewer at merge head `c22298fb`:**
    - the full ci.yml Gradle set, including `:app:lintRelease` with no suppression, and forced test reruns;
    - `mobile.py check` and `bytecode`, `eng/tests` (133), `maui_identity`, `licences projects`, `dependency_policy` and `check_provenance --owner Mobile`.
- Substitutes still in use: none.
- Remaining completion prerequisites and next action (delivered):
  - The P2-024 deferral: the hosted Linux CI run of the identity-only build (Debug and Release, locked restore) that AND.40 adds. A failed Linux build reopens AND.01.
  - PRF.12, the MAUI Android release proof of the exact tuple. This is the completion edge.
  - The F-023 closure for the actual MAUI distribution closure, and the notice deferrals listed in `docs/maui-toolchain.md` (Glide BSD-2, Google.Protobuf, Grpc.Core.Api, the workload-pack licences). Both are owned by AND.40 before the first MAUI release candidate.

## Untested coverage (stated expressly)

- The committed SDK 10.0.400 pin has never built the MAUI project. Its first build is the AND.40 CI run.
- No Linux build has been run.
- No persistent-key (`--release`) signature has been proven on a MAUI APK.
- Mono AOT, the 16 KB alignment check, device install and App Link fixture-key tests are not run. They belong to AND.40 and PRF.12.
- The `Microsoft.Maui.*` nupkg SHA-512 values were checked against the nuget.org catalog only for `Microsoft.Maui.Controls`. The clean locked restore matched every lock contentHash.
- The prerelease transitive `Xamarin.AndroidX.Security.SecurityCrypto` 1.1.0.4-alpha07 is in the admitted closure. AND.40 must confirm it is needed before any release candidate.
- The local JDK was 21.0.11, against the 21.0.12 pin.
