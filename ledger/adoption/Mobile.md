# Mobile adoption repository record

Recorded 2026-09-27 by Mobile integration owner `w-20260927-mobile-lane` (role epoch 2), for ADOPT.10 and its four independently claimed slices (each epoch 1).

## Frozen source and evidence

- **E1 — source:** frozen main `3267f6c4bbf7a51bde26512cba5895a64502d802`; [source tree](https://github.com/ArcForges/Mobile/tree/3267f6c4bbf7a51bde26512cba5895a64502d802). The primary checkout is clean at this commit; no open Mobile PR at review. Frozen remote branches are main and `task/adopt-01` at `7c8e100f20991e912a45a8bc44d75782218ee2a6`. No later source change is included.
- **E2 — reviewed CI/publication:** [frozen baseline](baseline.md#mobile), [Mobile PR #15](https://github.com/ArcForges/Mobile/pull/15), reviewed head `7c8e100f20991e912a45a8bc44d75782218ee2a6`, [peer approval](https://github.com/ArcForges/Mobile/pull/15#issuecomment-5857861119), merge equal to E1. Retained [PR CI 36334917935](https://github.com/ArcForges/Mobile/actions/runs/36334917935) passed. [Main run 36335468538](https://github.com/ArcForges/Mobile/actions/runs/36335468538) and [signing/publication job](https://github.com/ArcForges/Mobile/actions/runs/36335468538/job/108666576568) succeeded for [android-0.1.0-ci.49.1](https://github.com/ArcForges/Mobile/releases/tag/android-0.1.0-ci.49.1). Reuse these original receipts; no artifact bytes were downloaded or republished for adoption.
- **E3 — bounded historical evidence:** Design [F-023 and VG-07 register](https://github.com/ArcForges/ArcForges-Design/blob/722e85641c8afb765dafcab5bc0e84d5a22d5a3c/docs/assurance/open-gates-register.md) closes F-023 only for inspected `android-0.1.0-ci.14.1`; VG-07 remains open. Mobile `docs/validation.md` records historical bootstrap/emulator observations and explicitly disclaims physical-device, Play and production-backend acceptance. These do not establish current full companion behavior.

## Layout, identities and pins

The only included Gradle modules are `:app` and `:shared`. `app/src/main/kotlin/io/github/arcforges/mobile/` contains MainActivity, BuildInformation and CloudHelloClient. The shared common sources contain the greeting state/UI, with an optional JVM desktop preview. Contrary to a shorthand description of shared as preview-only, `app/build.gradle.kts` actually has `implementation(project(":shared"))`: shared code is presently in the Android graph. AND.01 owns reconciling this documented bootstrap with the final module plan; adoption does not remove or rename it.

Release identity and namespace are `io.github.arcforges.mobile`; debug adds `.debug`. AND.01 owns migration to `com.arcforges.mobile` and reinstall guidance. No production identity or signing identity is changed by adoption. Kotlin/Java target JVM 21; Gradle 9.8.0, AGP 9.4.1, Kotlin 2.4.20, Compose 1.12.1, Connect Kotlin 0.9.0, Spotless 8.10.3; compile/target API 37, build-tools 37.0.0, minimum API 26. Exact versions, checksums and platform-specific preview locks remain in the catalog, wrapper, verification metadata and lockfiles.

Contracts consumer pin is `io.github.arcforges:contracts-connect-client:1.0.0-ci.60.1` (and its contracts-proto dependency), from Maven Central; this is deliberately recorded separately from the newer producer baseline. Later consumer tasks move pins only through reviewed exact candidate consumption. There are no local producer source dependencies. The repository publishes Android APK/AAB prereleases, not Maven libraries or desktop/iOS products. The protected `android-release` environment signs the original candidate with its persistent identity. `docs/releasing.md` says Play publishing is future setup; AAB publication is not Play submission.

Existing governance lives under `eng/policy`, `eng/provenance`, `eng/tests`, `eng/licences.gradle.kts` and the Gradle build files. It includes dependency admission, SPDX boundaries, checksum verification, notices, source/resource provenance and release identity checks. `core/*`, `feature/*`, `gradle/policy` and `eng/release` do not exist. Planned scopes bind to additions under these roots after prerequisites, never implied renames of accepted packages. Integration tasks with empty write scopes produce evidence, not unowned source changes.

## Retained workflow inventory and shared resources

- `.github/workflows/ci.yml`: Windows/Linux compilation, exact dependency restore, Spotless, shared offline tests, app test compilation, release lint, APK/AAB packaging and bytecode verification. Linux alone runs repository/tooling checks, workflow validation and stages the candidate. `Verify` joins build/security; main alone signs and publishes. App transport tests are compiled, not represented as runtime passes.
- `.github/workflows/security.yml`: PR dependency review, redacted secret scan and CodeQL Python/actions/java-kotlin (including its pinned Kotlin-compatible tool bundle). No macOS, emulator/device, GUI, hosted service or public-install CI gate.
- Shared build configuration follows `RES-mobile-build-config`: AND.02 owns exclusive module registration; later catalog additions are append-only and locks regenerate after rebase. `RES-architecture-tests` is append-only per repository suite. Heavy local work uses the workstation build slot. Signing/device/provider leases are taken only by the relevant task for an actual phase, not held for adoption.

## Combined classification

The four linked records classify all 30 tasks exactly once: 8 inherited with adjustment, 22 gaps, zero inherited and zero conflicting. The existing bootstrap is preserved; no source task is closed by this review. All mapped tests and acceptance remain as stated in the slice rows. No AND task was claimed or implemented by this adoption bundle.

| Task | Classification | Slice record |
|---|---|---|
| AND.01 | inherited with adjustment | [ADOPT.10.android](../tasks/adopt-10-android.md) |
| AND.02 | gap | [ADOPT.10.android](../tasks/adopt-10-android.md) |
| AND.03 | gap | [ADOPT.10.android](../tasks/adopt-10-android.md) |
| AND.04 | inherited with adjustment | [ADOPT.10.android](../tasks/adopt-10-android.md) |
| AND.05 | gap | [ADOPT.10.android](../tasks/adopt-10-android.md) |
| AND.06 | gap | [ADOPT.10.android](../tasks/adopt-10-android.md) |
| AND.07 | gap | [ADOPT.10.android](../tasks/adopt-10-android.md) |
| AND.08 | gap | [ADOPT.10.android](../tasks/adopt-10-android.md) |
| AND.09 | gap | [ADOPT.10.android](../tasks/adopt-10-android.md) |
| AND.10 | gap | [ADOPT.10.android](../tasks/adopt-10-android.md) |
| AND.11 | gap | [ADOPT.10.android](../tasks/adopt-10-android.md) |
| AND.12 | gap | [ADOPT.10.android](../tasks/adopt-10-android.md) |
| AND.13 | gap | [ADOPT.10.android](../tasks/adopt-10-android.md) |
| AND.14 | inherited with adjustment | [ADOPT.10.android](../tasks/adopt-10-android.md) |
| AND.15 | gap | [ADOPT.10.android](../tasks/adopt-10-android.md) |
| AND.16 | inherited with adjustment | [ADOPT.10.android](../tasks/adopt-10-android.md) |
| AND.17 | gap | [ADOPT.10.android](../tasks/adopt-10-android.md) |
| AND.18 | inherited with adjustment | [ADOPT.10.android](../tasks/adopt-10-android.md) |
| AND.19 | gap | [ADOPT.10.android](../tasks/adopt-10-android.md) |
| AND.20 | gap | [ADOPT.10.android](../tasks/adopt-10-android.md) |
| AND.21 | gap | [ADOPT.10.android](../tasks/adopt-10-android.md) |
| AND.22 | inherited with adjustment | [ADOPT.10.android](../tasks/adopt-10-android.md) |
| AND.23 | gap | [ADOPT.10.android](../tasks/adopt-10-android.md) |
| AND.24 | gap | [ADOPT.10.android](../tasks/adopt-10-android.md) |
| AND.25 | gap | [ADOPT.10.android](../tasks/adopt-10-android.md) |
| AND.26 | gap | [ADOPT.10.android](../tasks/adopt-10-android.md) |
| AND.27 | gap | [ADOPT.10.android](../tasks/adopt-10-android.md) |
| GOV.12 | inherited with adjustment | [ADOPT.10.governance](../tasks/adopt-10-governance.md) |
| REL.04 | gap | [ADOPT.10.release](../tasks/adopt-10-release.md) |
| PRF.10 | inherited with adjustment | [ADOPT.10.runtime-proofs](../tasks/adopt-10-runtime-proofs.md) |
