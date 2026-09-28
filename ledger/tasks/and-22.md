---
task: AND.22
status: complete
recorded: 2026-09-28
claimant: af-20260928-p04
epoch: 1
---

# Android scope statement

## Evidence

- Implementation: Mobile [PR #18](https://github.com/ArcForges/Mobile/pull/18), exact head `ab167271a24f69fc49926378f3e44c77165a92c0`, independently reviewed by g02 at that exact head ([review](https://github.com/ArcForges/Mobile/pull/18#pullrequestreview-5339410607)); merged to Mobile main as `7d3aa075c87b04e7701f79315031a3a350c5b5aa`.
- The change is limited to the already-classified `README.md`, `docs/development.md`, and `docs/releasing.md`. They state Android is the only product/release platform, identify desktop JVM preview as local development-only, and explicitly put iOS, Swift, KMP and cross-platform UI product promises outside this delivery. The platform/distribution matrix matches the existing Android APK/AAB GitHub prerelease path and does not claim Play publication. No code, Gradle, workflow, dependency, or provenance inventory changed.
- Local validation on the implementation head: `python eng/mobile.py check` passed; `python -m unittest discover -s eng/tests -v` passed 70/70; `git diff --check` passed. PR CI run [36429088081](https://github.com/ArcForges/Mobile/actions/runs/36429088081) completed successfully for all applicable checks.
- Post-merge workflow [36430588934](https://github.com/ArcForges/Mobile/actions/runs/36430588934) completed successfully on merge `7d3aa075c87b04e7701f79315031a3a350c5b5aa`: Ubuntu and Windows builds, Verify, CodeQL and secret scan passed; dependency review was skipped as expected for a push event. The normal Publish Android job succeeded.
- Publication: non-draft prerelease [Android 0.1.0-ci.56.1](https://github.com/ArcForges/Mobile/releases/tag/android-0.1.0-ci.56.1), created 2026-09-28T13:42:58Z and targeting the exact merge commit above. GitHub release metadata lists `ArcForges-0.1.0-ci.56.1.apk` (SHA-256 `fc88c012504edbe27b6dec1631029fcd2a20baad914834262eadc288309538d9`) and `ArcForges-0.1.0-ci.56.1.aab` (SHA-256 `86e643ebd88831d064b407d008192c997c61d2dbc28bc337cb9387a1dd410759`), plus the APK idsig and release/build identity, licence, source/resource provenance and checksum evidence. No artifact was downloaded or installed.
- The Mobile primary checkout was cleanly fast-forwarded to `7d3aa075c87b04e7701f79315031a3a350c5b5aa` and is clean/tracking `origin/main`.
- Obligations satisfied: [WP-32.06](https://github.com/ArcForges/ArcForges-Design/blob/main/docs/planning/work-packages/32-mobile-release-and-store-gates.md#rule-wp-32.06), full. The documentation and distribution matrix are consistent with the published Android release and do not retain unsupported iOS/platform claims. AND.22 has no completion prerequisites.
- Untested coverage: no device install or runtime exercise was performed; no Play listing/submission or iOS/desktop product delivery is claimed. These are outside this documentation-only scope.
- Remaining completion prerequisites and next action: none.
