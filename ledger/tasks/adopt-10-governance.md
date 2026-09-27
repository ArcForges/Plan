---
task: ADOPT.10.governance
status: complete
recorded: 2026-09-27
claimant: w-20260927-mobile-lane
epoch: 1
---

## Evidence and scope

Reviewed against frozen Mobile source `3267f6c4bbf7a51bde26512cba5895a64502d802` and Design `722e85641c8afb765dafcab5bc0e84d5a22d5a3c`. [Repository facts and evidence E1-E3](../adoption/Mobile.md) bind every row to the source inventory, retained CI and original receipts. No post-baseline source change or open Mobile PR was found at review. The exact task prompts and linked WP obligations were compared with the source; all mapped obligation parts remain open unless explicitly stated otherwise.

This slice changes only the ledger (ADP-10). No task is classified inherited; no inherited task record is created. Existing bootstrap machinery stands only where the row says inherited with adjustment. A gap may have a Hello scaffold but lacks its required outcome. No D-001 conflict is raised: documented development identity/shared composition are migration inputs already owned by AND.01, not a production design decision. No retired-product cleanup is assigned to Mobile.

## Classification

| Task and obligations | Classification | Source evidence | Bound write scope | Remaining scope | Conflicts / blockers |
|---|---|---|---|---|---|
| GOV.12: WP-05.00 (Mobile slice, via Gradle dependency-graph verification rather than the.NET engine); WP-05.01 (Mobile slice: licence boundary + dependency allowlist over Gradle dependencies); WP-05.02 (wire the forbidden-term scanner into Mobile's own PR build); WP-05.04 (Mobile banned-API fixtures) | inherited with adjustment | build.gradle.kts, eng/licences.gradle.kts, eng/policy/**, eng/tests/**: bootstrap dependency/licence enforcement; gradle/policy absent; E1/E2. | Mobile:gradle/policy/**; Mobile:eng/policy/exceptions.json. Existing paths remain; absent core/feature/gradle-policy/release paths are planned additions, not renames. | Retain locked dependency verification, SPDX/boundary declarations and existing licence/admission/provenance fixtures; add Gradle-native layering, forbidden-term and banned-API enforcement using GOV.04 portable rule DATA, owned expiring exceptions and per-rule positive/negative fixture evidence wired into PR checks. | No adoption conflict. Start: GOV.03, GOV.04; completion: none. See authoritative ready for current satisfaction. |

## Validation and boundaries

Reviewed source, retained CI results and existing receipts only. No new build, artifact download, device/emulator, installed-consumer, runtime or live-service test was run. Physical-device, real CF foundation, streaming/Keystore, companion recovery, FCM and store acceptance remain untested here. Existing historical observations are not current candidate acceptance. No substitute was introduced or used to close a gate.

Ledger PR review/merge identities are recorded in the current epoch claim and immutable merged PR history; this file cannot contain its own future merge SHA. All task dependency conditions remain in force after this slice opens its lane.
