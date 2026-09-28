---
task: SCOPE.10
status: complete
recorded: 2026-09-28
claimant: af-20260928-p05
epoch: 1
---

# Serial-Studio reference drift check

## Evidence

- **Adoption and scope.** ADOPT.05.arcscope is complete and records SCOPE.10 as inherited with adjustment: the pinned 31-row reference matrix already existed, while the current changed/new-material and licence drift check remained outstanding. SCOPE.10 has no completion prerequisites and no D-001 conflict. Its sole authorized output is the Design drift report; the task does not require product code or a package publication.
- **Documentation PR.** Design [PR #112](https://github.com/ArcForges/ArcForges-Design/pull/112) added the SCOPE.10 drift report. The exact reviewed head was `977e102318bb6a5d3549dd8488864a203569da6d`, based on Design main `ff8854085eb9c3e00a5163728d9ceed6f15dec9d`; independent exact-head review [5339885408](https://github.com/ArcForges/ArcForges-Design/pull/112#pullrequestreview-5339885408) was COMMENTED clean. The PR merged as `3701bde466571ab2df620752fb0c9d58041ad0d5`; that merge has the expected base/head parents. Design had no configured PR checks.
- **WP-33.07 acceptance.** The report at [`docs/assurance/reference-coverage/arcscope-serial-studio.md`](https://github.com/ArcForges/ArcForges-Design/blob/3701bde466571ab2df620752fb0c9d58041ad0d5/docs/assurance/reference-coverage/arcscope-serial-studio.md) keeps §§1–7 explicitly historical and bound to Serial-Studio `639daafb2fe7d324c3b2d5583d2514c8c470676f`. Its separate §8 comparison binds current upstream to `2e6ee11350c1ab619ff41e758c1861864325cf3f` and records 5,270 changed path records as drift locators, not behavioral proof. Sections 8.1 and 8.4 disposition all 31 baseline row families; §8.3 maps or excludes all 20 current/new material groups; §8.2 re-reads the current licence and REUSE position. No ArcScope requirement is added, and all assessed current material remains Reference Only or Drop.
- **Licence and authorship boundary.** The report distinguishes the historical GPL-3.0-only/commercial baseline from current per-file/REUSE licensing, current EULA and trademark material, and the current commercial-source boundary. It notes that the latest upstream change adds `app/rcc/sounds/**` to the existing first-party asset annotation; the miniaudio `MIT-0 OR Unlicense` declaration predates that change. It makes no legal-validity determination and grants no reuse rights. No Pro implementation was read; no packaged binary or sound asset was opened, run, or played.
- **Validation performed.** The task's completeness check passed: 31 baseline row families and 20 §8.3 disposition groups are accounted for. `git diff --check` passed on the PR and merged range; the merged Design diff contains only the authorized report. Explicit-root `delivery.py check` passed after merge against Design main `3701bde466571ab2df620752fb0c9d58041ad0d5` and Plan main `4a4247cf4231dfd2461eaaae4fc6595fc444e52d`: 437 tasks, 50 adoption slices, 99 current views, 0 warnings, ledger valid. No code build or runtime check was required or claimed.
- **Substitutes and untested coverage.** SCOPE.10 introduced no implementation substitute or product behavior. Upstream path names and public help are reported only at their stated evidence level; upstream implementation behavior, Pro source, packaged binary behavior, sound playback, and legal validity are not claimed or verified.
- **Closure.** WP-33.07's full drift-report obligation is satisfied. SCOPE.10 has no remaining completion prerequisite or follow-up acceptance. SCOPE.11 remains a separate task with its own hardware and integration evidence; this record closes only SCOPE.10.
