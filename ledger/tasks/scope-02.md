---
task: SCOPE.02
status: complete
recorded: 2026-09-28
claimant: af-20260928-c04
epoch: 1
---

# Exact time and channel domain

## Evidence

- **Implementation.** ArcScope [PR #19](https://github.com/ArcForges/ArcScope/pull/19) added the canonical internal `ArcForges.ArcScope.Domain` time and channel models plus tests in the existing `ArcForges.ArcScope.Tests` project. The exact reviewed head was `e3f71ef4c6968428e9f2ae957c1d5a5d63f981dd`, based on `3051416605f50efcd5f429b26680ad255c0a2052`; independent exact-head clean review [5341967445](https://github.com/ArcForges/ArcScope/pull/19#pullrequestreview-5341967445). Squash-merged as `3762518843f3379d4d0c17135ae2a893866c8df7`.
- **WP-33.03 acceptance.** The model preserves reduced exact rates and time-domain identity; duration/time conversions reject non-integral or overflowing results rather than round; cross-source alignment is explicit and anchored by recorded source/reference observations; signals enforce strictly increasing timestamps while preserving irregular spacing; and discrete typed events remain distinct from sampled signals. Focused tests cover normalization/invalid rates, precision and overflow, alignment and nonrepresentable cross-domain conversions, ordering/irregular gaps, and typed values/events.
- **Validation.** With pinned .NET SDK 10.0.401, exact-head locked restore passed; Release solution build passed with 0 warnings and 0 errors; the existing ArcScope test project passed 117/117; `dotnet format --verify-no-changes` passed. Hosted PR CI [run 36453378512](https://github.com/ArcForges/ArcScope/actions/runs/36453378512) passed every applicable check; release jobs were correctly skipped for a PR. Post-merge main CI [run 36455002479](https://github.com/ArcForges/ArcScope/actions/runs/36455002479) completed successfully on merge commit `3762518843f3379d4d0c17135ae2a893866c8df7`, including all three Native AOT targets, `Verify`, publication, and publication verification.
- **Published candidate.** Main-push run 36455002479 published [ArcScope `v0.1.0-ci.43.1`](https://github.com/ArcForges/ArcScope/releases/tag/v0.1.0-ci.43.1), a non-draft prerelease at `2026-09-28T17:04:05Z`. GitHub release/tag metadata identifies the exact source merge commit above and lists the three Windows/Linux archives, their three `.sha256` sidecars, and `arcscope-verification.tar.gz`. This records provider metadata only; no release payload was downloaded or re-hashed.
- **Scope and untested coverage.** The change adds no Contracts dependency, public Signal/EventRecord wire contract, serializer, or runtime transport behavior. Signal/EventRecord serialization remains with its producer task; this task makes no wire-compatibility claim. The packaged application was not launched; GUI, live-service, hardware, and macOS behavior/artifacts are not claimed or tested. No dependency version or third-party package closure changed.
- **Closure.** SCOPE.02 has no completion prerequisites. Its exact time/channel domain outcome and required evidence are satisfied. The Plan ledger PR review/merge identity is retained by this ledger PR and the final SCOPE.02 claim record.
