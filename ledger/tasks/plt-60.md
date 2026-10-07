---
task: PLT.60
status: complete
recorded: 2026-10-07
claimant: w-codex-20261006-security
epoch: 1
---

# Actual helper isolation and resource-lifetime producer

This completes the independently useful Windows profile/process lifetime and Linux signal-filter implementation producer. Original PLT.45/PLT.54/PLT.46 and NAT.25 packaged, signing, combined parser and full OS acceptance remain separate. No mocked lifecycle result is represented as actual isolation.

## Source and independent review

[DesktopPlatform PR157](https://github.com/ArcForges/DesktopPlatform/pull/157) was fenced merged at final head `0aa1d3c512457fd4868693f143c3878af0edded4` as `4eba06b6fe396f2b21002f0926b4098da83e2092`. Reviewed merged Design259/Plan360 authority admits actual pending lifetime records and original-process confirmed exit; reopened named Job state alone cannot prove a prior process exited.

Independent reviewer `w-codex-20261006-governance` approved complete substantive source `e073837f5b4e4d4c3a4f07cb505fa0dca9c123d3` at [6025049755](https://github.com/ArcForges/DesktopPlatform/pull/157#issuecomment-6025049755), and final accepted-parent metadata successor at [6026795449](https://github.com/ArcForges/DesktopPlatform/pull/157#issuecomment-6026795449). Separate agent/session review is independent despite the shared GitHub account. Review found that truncating the pending record before writing active state could falsely leave an empty reusable slot while a created child remained alive. The corrected transition preserves nonempty flushed pending evidence through every write cut, flushes the complete active bytes before truncation, and quarantines partial/malformed records. Actual-file cut/reopen negatives cover the fix. All twelve owned behavioral/test/import/isolation-documentation blobs remained identical across the later accepted-parent metadata unions; accepted immutable records, locks, pins, package identities and scanner boundaries were preserved.

## Production behavior

- Eight canonical per-user/profile slots use crash-releasing kernel locks independent of caller-selected coordination directories. A test/runtime override is additional coordination, never profile reuse authority. Windows Userenv supplies the actual SID-owned profile storage location; successful profile deletion also requires actual storage absence before reuse. Cleanup does not recursively delete guessed paths.
- A durable pending record is flushed before process creation. CreateProcess receives the existing atomic JOB_LIST attribute. Before Resume, active state binds actual process ID, creation time and verified AppContainer SID. The retained original kernel process handle must prove exit before profile deletion or reuse. Recovery validates the persisted process instance; unknown, pending, malformed or unverifiable evidence quarantines the slot. Foreign/reused PIDs are never killed. Named Job accounting is supplemental only: an actual probe observed a newly reopened empty Job while the original child was still alive.
- One shared disposal operation attempts process/job termination, owned resources and bounded diagnostics despite faults or cancellation. A canceled/faulted exit observation is not exit proof. Unconfirmed exit returns typed resource-unavailable failure and retains a quarantined lease with an owned continuation until actual exit is confirmed. Foreign callbacks have bounded invocation budgets; the implementation does not pretend it can forcibly stop arbitrary foreign code.
- The Linux seccomp filter permits tgkill only for the exact positive own process ID with the high argument word zero. Both x64 and arm64 filter-interpreter regressions exercise low/high-word mismatches. These are component tests, not observed Linux kernel isolation.

## Tests and current CI

Pinned SDK10.0.400 local locked Release build and formatting passed with zero warnings/errors. Final substantive Windows lifetime components passed12/12; the helper suite passed175 with15 explicitly skipped OS opt-ins. Earlier unchanged actual Windows AOT fixture observations cover fresh-profile privacy, current-SID recovery, access violation/deadline supervision and parent loss. These retained observations were not rerun for metadata-only successors and do not certify packaged combined Image/Pdf or other-OS behavior. Actual-file pending-to-active write cuts, two-directory exclusivity, cancellation/failure cleanup and concurrent disposal exercise genuine components; unavailable dependency seams alone are faked.

Final exact-head [CI37541920350](https://github.com/ArcForges/DesktopPlatform/actions/runs/37541920350) passed all22 applicable checks, including [aggregate112541752266](https://github.com/ArcForges/DesktopPlatform/actions/runs/37541920350/job/112541752266). Source/admission/provenance/reference/runtime/secret gates and actual hosted ordinary/AOT compilation checks passed. No new project, package, dependency receipt or source lock was admitted by PLT.60.

## Actual normal publication

Normal main [Publish NuGet37545726637](https://github.com/ArcForges/DesktopPlatform/actions/runs/37545726637) for exact merge source `4eba06b6fe396f2b21002f0926b4098da83e2092` completed SUCCESS: all24 jobs succeeded. [Publisher112553489514](https://github.com/ArcForges/DesktopPlatform/actions/runs/37545726637/job/112553489514) reverified and pushed the same actual existing cohort **1.0.0-ci.116.1**, containing22 managed packages, Build.Policy and the existing Image win-x64 runtime. Retained publisher logs contain24 Created and24 successful push receipts from `2026-10-06T23:32:22.8227707Z` through `23:32:39.6392212Z`. No NuGet binary download, extra republish or installed-product acceptance was performed for this ledger.

## Deferred acceptance and owners

PLT.45/PLT.54/PLT.46 and APP.03 retain full Windows/Linux/macOS isolation, actual published combined parser composition and commercial product acceptance. NAT.22/NAT.25 retain actual RID producer, authenticated runtime and signed helper delivery. Unknown same-boot crash cuts remain fail-closed quarantine rather than guessed reuse; actual operator/kernel evidence is required to recover an unverifiable profile safely. PLT.63 owns the missing real macOS XPC lifecycle adapter. These deferred checks do not leave unfinished PLT.60 implementation or require a user login for this producer.
