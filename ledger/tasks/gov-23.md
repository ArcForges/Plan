---
task: GOV.23
status: complete
recorded: 2026-10-06
claimant: w-codex-20261006-audit
epoch: 1
---

# Desktop CI virtualenv security admission successor

The narrow security implementation, immutable admission, independently approved source, all applicable CI and actual normal main publication are delivered. GOV.23 has no completion prerequisites. No whole-system commercial or OS acceptance is claimed.

## Exact implementation and prerequisite repair

The original [Dependabot PR116](https://github.com/ArcForges/DesktopPlatform/pull/116), commit `57801a0e67799b6d695f0bdc2428e5ec31f09341`, remains unchanged. Its virtualenv 21.5.1 to 21.7.13 patch was cherry-picked with original authorship and source receipt. The exact actual 21.7.13 wheel requires python-discovery >=1.6; the existing 1.4.3 requirement is incompatible. The minimum verified 1.6.0 requires only filelock >=3.15.4, satisfied by the existing 3.29.5. Only these two Python coordinates change; the other eight Python coordinates, all 60 NuGet coordinates and pinned Python 3.14.7/.NET SDK 10.0.400/native toolchains are preserved.

Primary [GHSA-p58f-9548-mpm2](https://github.com/pypa/virtualenv/security/advisories/GHSA-p58f-9548-mpm2) describes activation-script path injection fixed by 21.7.13. Current provider alerts observed before merge were three high and one medium, all on this same manifest: p58f <=21.7.12 patched21.7.13; x78j and 94p9 <=21.7.11 patched21.7.12; 9h9j <=21.7.10 patched21.7.11. The chosen pin satisfies all four observed patched-version bounds. After source integration, the actual provider API marked all four state=fixed at 2026-10-06T19:30:20Z/19:30:21Z; none was dismissed or suppressed.

The actual original [repository-hooks failure](https://github.com/ArcForges/DesktopPlatform/actions/runs/36912180246/job/110537264414) was pip ResolutionImpossible for the discovery mismatch; its separate [license failure](https://github.com/ArcForges/DesktopPlatform/actions/runs/36912180246/job/110537264366) refused changed inputs without admission. Old failure summaries were corrected using completed provider logs. Reviewed merged authority Design257 `e4ec7c979a1af7135999094672d02a5eb55b2472` and Plan352 `7972e1e84466b67285e6b07702ac2a4d68c257a7` expressly admit the exact two-pin minimum and unchanged unrelated closure.

## Actual legal and immutable admission

Both actual bounded wheel downloads were size/SHA-256 verified once against primary PyPI; complete METADATA and MIT LICENSE bytes were inspected. Upstream immutable LICENSE bytes match the wheels. Two new reference-only provenance records import no code, wheel or legal text into product packages and make no cryptographic wheel-to-source attestation claim. The full legal/closure/upgrade checklist is retained in the new gov-23-r1 receipt.

The final candidate is based on actual NAT.15 merge `24feb447955e131bcfbf3483d295af913d15d629`; its receipt chains from used nat-15-r1 with 289 complete actual input hashes. Every used historical receipt and accepted native/legal/NOTICE record remains unchanged. The prior reviewed candidate is preserved under local archive/gov-23-reviewed-7102bf5. Rebase conflicts were resolved only by retaining the accepted parent policy/inventory and appending the exact owned minimum successor.

## Independent review and actual verification

Distinct reviewer `w-codex-20261006-governance` approved initial 7102bf56 at [source approval](https://github.com/ArcForges/DesktopPlatform/pull/155#issuecomment-6023527503), then final clean pushed `b97a48232e2141f6ac8a43807c676202a50433d1` at [exact successor approval](https://github.com/ArcForges/DesktopPlatform/pull/155#issuecomment-6023615764). Requirements, focused tests, documentation and both reference-only records are byte-identical across the accepted-parent rebase. Independence is by distinct agent/session; GitHub authentication is shared. Claim epoch1 binds exact head and reviewed head b97 at claims/gov-23 checkpoint35c4a2d84ad0 (later actual merge handoff e26e216a1073).

Actual component checks: 25 admission/history tests passed on the final candidate, including old/missing/mutated/extra distribution and immutable-history negatives. Twelve license-boundary tests passed on the unchanged component. Current final dependency gate60NuGet/10Python/289inputs and clean provenance1040files/25reused/144records passed. NOTICE matches the accepted parent's a44d34ed digest. Metadata requirements were evaluated against actual pinned Python3.14.7 and all active dependency bounds passed.

Prior 7102 [hosted repository-hooks job](https://github.com/ArcForges/DesktopPlatform/actions/runs/37516217051/job/112449661025) actually installed the complete require-hashes closure, including virtualenv21.7.13 and python-discovery1.6.0. That is historical implementation evidence, never final b97 CI authority. Final b97 [PR workflow37516983878](https://github.com/ArcForges/DesktopPlatform/actions/runs/37516983878) completed SUCCESS with all22 applicable jobs passing. Its actual [repository-hooks job112452905345](https://github.com/ArcForges/DesktopPlatform/actions/runs/37516983878/job/112452905345) again installed the complete require-hashes closure with exact two new versions and eight preserved pins. This current-head result is distinct from prior7102 evidence. Root fenced source merge71b6df2db828bc859cca6934ed66aac9b525b5c7 occurred2026-10-06T19:29:13Z; normal main [Publish37519330950](https://github.com/ArcForges/DesktopPlatform/actions/runs/37519330950) completed SUCCESS with all 24 jobs for that exact source. Actual [publisher job112466799116](https://github.com/ArcForges/DesktopPlatform/actions/runs/37519330950/job/112466799116) independently rechecked the same source-bound 17-package candidate and completed at 2026-10-06T19:45:04Z. Its completed provider log records version `1.0.0-ci.109.1`, each package receiving Created and Your package was pushed between 19:44:45Z and 19:45:00Z. This is normal production publication evidence, not allocation-only success. No published binaries were downloaded or reinstalled to verify delivery.

A transient claim-ref push refusal was diagnosed by re-reading the unchanged owned epoch and remote record before one bounded retry; the successor update then succeeded. No successful write was repeated blindly. Source branches, worktrees, existing routes and data remain preserved.

## Delivery gates and remaining boundaries

Final applicable CI, exact fenced source merge and actual normal main publication are satisfied. This sole ledger record requires independent exact-head review and fenced Plan integration before the claim becomes complete. This narrow CI-tooling security task has no remaining implementation, completion prerequisite, substitute or human-only blocker. Actual product/OS/commercial acceptance remains with the corresponding producer/consumer acceptance tasks; none is inferred from metadata, source approval or mocked behavior.
