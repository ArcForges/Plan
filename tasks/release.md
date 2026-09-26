# ArcForges delivery task prompts — Release readiness and family release

Generated from Design `docs/planning/delivery/delivery-graph.json` by `tools/delivery.py`; do not edit by hand.
Each block is self-contained. Claim a task only when `python tools/delivery.py ready` lists it, with
`python tools/delivery.py claim <TASK-ID> --worker <name>`, then follow `arcforges-implementation.md`.
Tasks are ordered by lane for reading; the order is not a schedule.

## Release readiness and family release

```text
Execute ArcForges delivery task REL.01 — ArcNotes desktop release readiness.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\release.md (anchor task-rel-01).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\ArcNotes (integration owner: ArcNotes integration owner, the holder of roles/integration-arcnotes).
Claim and handoff record: claims/rel-01 (python tools/delivery.py claim REL.01 --worker <name>); task branch task/rel-01 in ArcNotes; ledger record ledger/tasks/rel-01.md.
Kind/size: release/L. Baseline: not-started.
Outcome: ArcNotes' desktop release candidate passes the complete update matrix on all three platforms against a candidate/staging feed, and carries a complete licence/SBOM/provenance/NOTICE record for REL.07 to roll up.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-50.02 (ArcNotes' own complete update matrix (fresh install, upgrade, two-version upgrade, downgrade protection, rollback, interrupted download, interrupted install, corrupted-artifact rejection, update during a long task, update with documents open, uninstall preserving user data, channel switch both ways, blocked bad version) on Windows/macOS/Linux): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\50-full-platform-production-release.md, anchor rule-wp-50.02
- WP-50.01 (ArcNotes' own licence inventory, SBOM, provenance attestation and verified NOTICE): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\50-full-platform-production-release.md, anchor rule-wp-50.01

Entry condition: adoption slice ADOPT.04.release is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [release] NOTES.32: ArcNotes feature-complete release candidate
- [artifact] UPD.08: the published ArcForges.Update package/client (the platform lane UPD area)
- [release] NOTES.14: ArcNotes document core accepted
- [release] NOTES.22: ArcNotes search and portability accepted
Completion prerequisites (may start earlier; cannot complete before these are complete):
- [integration] REL.10: production feed/signing cutover pointing at this proven candidate

Permitted write scope: ArcNotes:eng/release/**; Design:docs/assurance/wp50-02-arcnotes-*.md
Shared resources (follow the owner protocol): RES-production-release-trust (append): Changed only by release tasks, once per promoted candidate; test-signed feeds and fixture roots stay separate from production.
Permitted substitutes (never real integration evidence): SUB-desktop-candidate-feed: the update matrix (fresh install/upgrade/rollback/etc.) works against a correctly-shaped feed Real producer ['UPD.07']; removed by REL.10
Unblocks: REL.07, REL.10, REL.11

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Local opt-in runtime observation per platform under P2-017/ci-and-local-validation-policy.md; no macOS CI - an independently produced macOS installer has its own local build/signing evidence; Windows/Linux installers promote their original CI-produced candidates, never rebuilt.
Completion evidence for the ledger: Full update-matrix results table per platform; licence/SBOM/provenance/NOTICE closure report for the ArcNotes artifact.
Notes: Analogous tasks exist for ArcScope (REL.02) and ArcSlate (REL.03); all three can run in parallel once their own product WP and WP53 are ready.
```

```text
Execute ArcForges delivery task REL.02 — ArcScope desktop release readiness.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\release.md (anchor task-rel-02).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\ArcScope (integration owner: ArcScope integration owner, the holder of roles/integration-arcscope).
Claim and handoff record: claims/rel-02 (python tools/delivery.py claim REL.02 --worker <name>); task branch task/rel-02 in ArcScope; ledger record ledger/tasks/rel-02.md.
Kind/size: release/L. Baseline: not-started.
Outcome: ArcScope's desktop release candidate passes the complete update matrix on all three platforms against a candidate/staging feed, and carries a complete licence/SBOM/provenance/NOTICE record for REL.07 to roll up.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-50.02 (ArcScope's own complete update matrix on Windows/macOS/Linux): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\50-full-platform-production-release.md, anchor rule-wp-50.02
- WP-50.01 (ArcScope's own licence inventory, SBOM, provenance attestation and verified NOTICE): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\50-full-platform-production-release.md, anchor rule-wp-50.01

Entry condition: adoption slice ADOPT.05.release is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [release] SCOPE.26: ArcScope feature-complete release candidate
- [artifact] UPD.08: the published ArcForges.Update package/client (the platform lane UPD area)
- [release] SCOPE.11: ArcScope acquisition package accepted
- [release] SCOPE.19: ArcScope analysis package accepted
Completion prerequisites (may start earlier; cannot complete before these are complete):
- [integration] REL.10: production feed/signing cutover pointing at this proven candidate

Permitted write scope: ArcScope:eng/release/**; Design:docs/assurance/wp50-02-arcscope-*.md
Shared resources (follow the owner protocol): RES-production-release-trust (append): Changed only by release tasks, once per promoted candidate; test-signed feeds and fixture roots stay separate from production.
Permitted substitutes (never real integration evidence): SUB-desktop-candidate-feed: the update matrix (fresh install/upgrade/rollback/etc.) works against a correctly-shaped feed Real producer ['UPD.07']; removed by REL.10
Unblocks: REL.07, REL.10, REL.11

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Local opt-in runtime observation per platform under P2-017; no macOS CI.
Completion evidence for the ledger: Full update-matrix results table per platform; licence/SBOM/provenance/NOTICE closure report for the ArcScope artifact.
Notes: Parallel sibling of REL.01/REL.03.
```

```text
Execute ArcForges delivery task REL.03 — ArcSlate desktop release readiness.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\release.md (anchor task-rel-03).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\ArcSlate (integration owner: ArcSlate integration owner, the holder of roles/integration-arcslate).
Claim and handoff record: claims/rel-03 (python tools/delivery.py claim REL.03 --worker <name>); task branch task/rel-03 in ArcSlate; ledger record ledger/tasks/rel-03.md.
Kind/size: release/L. Baseline: not-started.
Outcome: ArcSlate's desktop release candidate passes the complete update matrix on all three platforms against a candidate/staging feed, and carries a complete licence/SBOM/provenance/NOTICE record for REL.07 to roll up.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-50.02 (ArcSlate's own complete update matrix on Windows/macOS/Linux): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\50-full-platform-production-release.md, anchor rule-wp-50.02
- WP-50.01 (ArcSlate's own licence inventory, SBOM, provenance attestation and verified NOTICE): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\50-full-platform-production-release.md, anchor rule-wp-50.01

Entry condition: adoption slice ADOPT.06.release is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [release] SLATE.40: ArcSlate feature-complete release candidate
- [artifact] UPD.08: the published ArcForges.Update package/client (the platform lane UPD area)
- [release] SLATE.14: ArcSlate obligation package accepted
- [release] SLATE.23: ArcSlate obligation package accepted
- [release] SLATE.32: ArcSlate obligation package accepted
Completion prerequisites (may start earlier; cannot complete before these are complete):
- [integration] REL.10: production feed/signing cutover pointing at this proven candidate

Permitted write scope: ArcSlate:eng/release/**; Design:docs/assurance/wp50-02-arcslate-*.md
Shared resources (follow the owner protocol): RES-production-release-trust (append): Changed only by release tasks, once per promoted candidate; test-signed feeds and fixture roots stay separate from production.
Permitted substitutes (never real integration evidence): SUB-desktop-candidate-feed: the update matrix (fresh install/upgrade/rollback/etc.) works against a correctly-shaped feed Real producer ['UPD.07']; removed by REL.10
Unblocks: REL.07, REL.10, REL.11

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Local opt-in runtime observation per platform under P2-017; no macOS CI.
Completion evidence for the ledger: Full update-matrix results table per platform; licence/SBOM/provenance/NOTICE closure report for the ArcSlate artifact.
Notes: Parallel sibling of REL.01/REL.02.
```

```text
Execute ArcForges delivery task REL.04 — Android release readiness.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\release.md (anchor task-rel-04).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Mobile (integration owner: Mobile integration owner, the holder of roles/integration-mobile).
Claim and handoff record: claims/rel-04 (python tools/delivery.py claim REL.04 --worker <name>); task branch task/rel-04 in Mobile; ledger record ledger/tasks/rel-04.md.
Kind/size: release/M. Baseline: not-started.
Outcome: The Android artifact is submitted and live with every mobile gate closed and the store listing consistent with the consumption-only posture; post-release install and update are verified from the store channel.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-50.03 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\50-full-platform-production-release.md, anchor rule-wp-50.03
- WP-50.01 (Android's own licence inventory, SBOM, provenance attestation and verified NOTICE): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\50-full-platform-production-release.md, anchor rule-wp-50.01

Entry condition: adoption slice ADOPT.10.release is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [release] AND.23: every mobile gate satisfied (the Web and Android lanes AND area: signing, distribution, store gates)
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Mobile:eng/release/**; Design:docs/assurance/wp50-03-android-*.md
Unblocks: REL.07, REL.11

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Post-release store-channel install/update verification, listing-consistency check; no emulator/device CI per P2-017 (real device evidence is WP06.07/WP30/WP32).
Completion evidence for the ledger: Store install/update verification results; listing-consistency check.
Notes: F-023 final closure and VG-13 (store category fit) are WP32's own gates, consumed here rather than produced.
```

```text
Execute ArcForges delivery task REL.05 — Web outputs release readiness.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\release.md (anchor task-rel-05).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Web (integration owner: Web integration owner, the holder of roles/integration-web).
Claim and handoff record: claims/rel-05 (python tools/delivery.py claim REL.05 --worker <name>); task branch task/rel-05 in Web; ledger record ledger/tasks/rel-05.md.
Kind/size: release/L. Baseline: not-started.
Outcome: Site/Account/Chat build once through the pinned Node/npm pipeline after current released proto-descriptor/C#/TS compatibility checks, promote the same artifacts with manifest and safe runtime-config schema, deploy atomically with per-origin edge routing/opaque cookie/CSRF policy/CSP, preserve old hashed chunks for the compatibility window, and roll back headers/assets/config coherently, while keeping production Node servers and esproj/npm installs out of Cloud runtime; the full browser-support.v1 matrix passes for supported/degraded/blocked behavior.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-50.06 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\50-full-platform-production-release.md, anchor rule-wp-50.06
- WP-50.01 (Web's own npm SBOM/provenance and CLI evidence): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\50-full-platform-production-release.md, anchor rule-wp-50.01
- WP-50:browser-matrix-acceptance-unlabeled-para Browser matrix acceptance (unlabeled paragraph after WP-50.90): browser-support.v1 against the exact release artifact/OS/browser patches, supported/degraded/blocked flows including delayed-stream polling, refusal of unavailable required auth/step-up, safe-preview refusal, preserved pending work; no-JS static-site readability; joins WP23/45/47/48/49 production hashes with real browser evidence - a Playwright WebKit run alone does not claim Safari/OS authenticator proof (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\50-full-platform-production-release.md, package-level obligation

Entry condition: adoption slice ADOPT.09.release is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [release] WEB.26: ArcChat Web Companion complete (the Web and Android lanes WEB area)
- [release] WEB.09: Static Public Site complete (the Web and Android lanes WEB area)
- [release] WEB.18: Account Portal complete (the Web and Android lanes WEB area)
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Web:eng/release/**; Design:docs/assurance/wp50-06-web-*.md
Unblocks: REL.07, REL.11

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Production asset/real C# integration in the supported browser matrix; public no-script content, auth/CSRF/expiry/replica revocation, paid-checkout return, Task recovery; visual/accessibility/performance budgets; atomic switch/rollback, cached-client/chunk failure, route-fallback/API-error separation; npm SBOM/provenance and Windows/CLI evidence; no fixture-only substitution; real-browser evidence per browser-support.v1, not Playwright-WebKit-only for Safari/OS-authenticator claims.
Completion evidence for the ledger: PG-23 combined production release/rollback evidence; browser-matrix acceptance results.
Notes: Owns the unlabeled 'Browser matrix acceptance' package obligation appended after WP-50.90; see package_obligations. Joins WP23/45/47/48/49 production hashes with real browser evidence per that paragraph.
```

```text
Execute ArcForges delivery task REL.06 — Cloud/AI production readiness (deployment, migration, backup, self-host).

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\release.md (anchor task-rel-06).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/rel-06 (python tools/delivery.py claim REL.06 --worker <name>); task branch task/rel-06 in Cloud; ledger record ledger/tasks/rel-06.md.
Kind/size: release/XL. Baseline: not-started.
Outcome: Cloud is deployed from a promoted, never-rebuilt artifact with rehearsed migration/rollback, proven backup/restore, a live status page with emergency alternate URL, and the approved/measured capacity envelope plus independently operated self-host deployment evidence required for L-16/PG-25/PG-26, on a genuine Native AOT publish.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-50.04 (production deployment from a promoted artifact; expand/contract migration and compatible rollback rehearsed; backup verified with proven restore; upgrade/rollback rehearsed; L-01..L-16 evidence except the game-day exercise itself (REL.09); status page live with emergency alternate URL; approved/measured capacity envelope and independently operated self-host deployment (PG-25/26)): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\50-full-platform-production-release.md, anchor rule-wp-50.04
- WP-50.01 (Cloud/AI's own licence inventory, SBOM, provenance attestation and verified NOTICE): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\50-full-platform-production-release.md, anchor rule-wp-50.01

Entry condition: adoption slice ADOPT.07.release is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [release] CLOUD.51: D1/R2 disaster-recovery mechanism complete
- [release] AIR.90: Workers AI routing/metering complete (the AI lanes AIR area)
- [artifact] GOV.03: Cloud's Native AOT build posture (GOV.03)
- [release] CLOUD.10: Cloud host closure and launch-capacity acceptance
- [release] CLOUD.20: obligation package accepted
- [release] CLOUD.28: obligation package accepted
- [release] CLOUD.36: obligation package accepted
- [release] CLOUD.47: obligation package accepted
- [release] CLOUD.55: obligation package accepted
- [release] COM.15: obligation package accepted
- [release] POL.10: obligation package accepted
- [release] OPS.12: obligation package accepted
- [release] SRCH.90: obligation package accepted
- [release] EXT.90: obligation package accepted
- [release] HAR.90: obligation package accepted
- [release] SIM.08: obligation package accepted
Completion prerequisites (may start earlier; cannot complete before these are complete):
- [integration] REL.09: the combined disaster drill actually exercised against this deployed production topology

Permitted write scope: Cloud:eng/release/**; Cloud:deploy/production/**; Design:docs/assurance/wp50-04-cloud-*.md
Unblocks: REL.07, REL.09, REL.11

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Production-shaped migration/rollback rehearsal against real Cloudflare topology; archived launch-capacity.v1 hash, actual standard-2 allocation/four global slots/ten-minute sleep, warm/cold/burst/fallback-read workload, D1/Vectorize/R2 dimensions and provider prices; explicit Product/Operations approval required for L-16/PG-26 - not markable complete from document checks alone.
Completion evidence for the ledger: Per-gate go-live evidence L-01..L-16 (except the drill); backup/restore proof; self-host deployment evidence.
Notes: The game-day exercise itself is split out to REL.09 per the assignment's explicit 'combined disaster drill' bucket.
```

```text
Execute ArcForges delivery task REL.07 — Contracts/SDK release audit (licence, SBOM, provenance rollup).

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\release.md (anchor task-rel-07).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Contracts (integration owner: Contracts integration owner, the holder of roles/integration-contracts).
Claim and handoff record: claims/rel-07 (python tools/delivery.py claim REL.07 --worker <name>); task branch task/rel-07 in Contracts; ledger record ledger/tasks/rel-07.md.
Kind/size: acceptance/M. Baseline: not-started.
Outcome: Every shipped artifact across every surface has a licence inventory, SBOM, provenance attestation and verified NOTICE, and every reused item has a completed provenance record, rolled into one closure report.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-50.01 (the audit mechanism (licence inventory, SBOM, provenance attestation, NOTICE-generation verification per artifact, copied-content audit) plus Contracts/public-SDK's own candidate audit and the cross-artifact provenance-completeness rollup): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\50-full-platform-production-release.md, anchor rule-wp-50.01

Entry condition: adoption slice ADOPT.03.release is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] REL.01: ArcNotes' own licence/SBOM/provenance/NOTICE evidence row
- [artifact] REL.02: ArcScope's own licence/SBOM/provenance/NOTICE evidence row
- [artifact] REL.03: ArcSlate's own licence/SBOM/provenance/NOTICE evidence row
- [artifact] REL.04: Android's own licence/SBOM/provenance/NOTICE evidence row
- [artifact] REL.05: Web's own licence/SBOM/provenance/NOTICE evidence row
- [artifact] REL.06: Cloud/AI's own licence/SBOM/provenance/NOTICE evidence row
- [artifact] REL.08: the commercial surface's own licence/SBOM/provenance/NOTICE evidence row
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Contracts:eng/release-audit/**; Design:docs/assurance/wp50-01-audit-*.md
Unblocks: REL.11

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline document/metadata rollup; no new build or download beyond what each surface already produced, per P2-017.
Completion evidence for the ledger: Closure report per artifact; NOTICE verification; provenance-completeness check across every recorded reuse.
Notes: Distributed-responsibility pattern: each surface task produces its OWN artifact's evidence as part of its own completion (WP50.01's per-artifact language); REL.07 owns the audit mechanism and the cross-artifact completeness rollup, mirroring GOV.13's role for PG-11/invariant accounting.
```

```text
Execute ArcForges delivery task REL.08 — Commercial activation.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\release.md (anchor task-rel-08).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/rel-08 (python tools/delivery.py claim REL.08 --worker <name>); task branch task/rel-08 in Cloud; ledger record ledger/tasks/rel-08.md.
Kind/size: release/L. Baseline: not-started.
Outcome: Account portal and checkout run in production; official pricing is published only after entitlement, refunds, webhook idempotency and a RECEIVED payout are all proven - until then the public statement is 'technical integration complete'; the regional route remains disabled unless its own gates are met.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-50.05 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\50-full-platform-production-release.md, anchor rule-wp-50.05

Entry condition: adoption slice ADOPT.07.release is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [release] COM.15: Commerce, Entitlement and Credits complete (the commerce, policy and operations lanes COM area)
- [release] POL.10: Dynamic Policy and Configuration Control Plane complete (the commerce, policy and operations lanes POL area)
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Cloud:eng/release/commercial/**; Design:docs/assurance/wp50-05-commercial-*.md
Unblocks: REL.07, REL.11

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Full commercial gate evidence set from WP42; configuration assertion on the regional route; a received payout is required, not merely a successful test transaction, per BR-05.
Completion evidence for the ledger: Commercial gate evidence set including the received payout; regional-route configuration assertion.
Notes: VG-10/VG-11/VG-12 (supplier onboarding, payout eligibility, regional enablement) are WP42's own gates, consumed here rather than produced.
```

```text
Execute ArcForges delivery task REL.09 — Combined disaster drill and operational readiness confirmation.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\release.md (anchor task-rel-09).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/rel-09 (python tools/delivery.py claim REL.09 --worker <name>); task branch task/rel-09 in Cloud; ledger record ledger/tasks/rel-09.md.
Kind/size: release/L. Baseline: not-started.
Outcome: A game-day exercise across the full severity ladder runs against the real deployed production topology with recorded evidence for every go-live gate; every alert maps to a rehearsed runbook, on-call is in place, and support/enforcement/appeal paths are operable.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-50.04 (the game-day exercise across the severity ladder against the real production topology only (the rest of 50.04 is REL.06)): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\50-full-platform-production-release.md, anchor rule-wp-50.04
- WP-50.07 (full: alerting live and mapped to rehearsed runbooks, on-call arrangement in place, incident process exercised, support entry points live, enforcement/appeal paths operable, advisory process rehearsed): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\50-full-platform-production-release.md, anchor rule-wp-50.07

Entry condition: adoption slice ADOPT.07.release is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] REL.06: Cloud deployed to the real production topology
- [release] OPS.12: rehearsed runbooks and PG-04 closure (the commerce, policy and operations lanes OPS area)
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Cloud:eng/release/game-day/**; Design:docs/assurance/wp50-04-gameday-*.md, wp50-07-operational-readiness-*.md
Unblocks: REL.06, REL.11

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): A real exercise across the severity ladder against real production topology; alert-to-runbook completeness assertion; on-call verification; support-path end-to-end test; local/opt-in per P2-017, no synthetic-only substitution.
Completion evidence for the ledger: Game-day record with per-gate go-live evidence; alert-to-runbook, on-call and support-path results.
Notes: Named explicitly in the assignment as its own bucket ('combined disaster drill'); folds WP50.07 in alongside WP50.04's game-day portion since both are evidence of the same severity-ladder incident-response exercise.
```

```text
Execute ArcForges delivery task REL.10 — Production update feed and signing switch.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\release.md (anchor task-rel-10).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/rel-10 (python tools/delivery.py claim REL.10 --worker <name>); task branch task/rel-10 in DesktopPlatform; ledger record ledger/tasks/rel-10.md.
Kind/size: release/M. Baseline: not-started.
Outcome: The production update feed is populated with hashes/compatibility ranges/minimum versions for all three desktop products across Windows/macOS/Linux, store and package-manager listings point at the corresponding signed installer, and a blocked bad version is refused by both the feed and compatibility policy.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-50.02 (the shared production update-feed population (hashes, compatibility ranges, minimum versions) and code-signing/publication-pointer cutover only; per-product update-matrix testing is REL.01/REL.02/REL.03): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\50-full-platform-production-release.md, anchor rule-wp-50.02

Entry condition: adoption slice ADOPT.02.release is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] REL.01: ArcNotes' own update matrix proven on all three platforms
- [artifact] REL.02: ArcScope's own update matrix proven
- [artifact] REL.03: ArcSlate's own update matrix proven
- [artifact] UPD.01: the update client/channel mechanism and feed schema (the platform lane UPD area)
- [artifact] UPD.07: production catalog and Android distribution trust
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:eng/packaging/release/**
Shared resources (follow the owner protocol): RES-production-release-trust (append): Changed only by release tasks, once per promoted candidate; test-signed feeds and fixture roots stay separate from production.
Unblocks: REL.01, REL.02, REL.03, REL.11, UPD.08

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Blocked-bad-version refusal test against both feed and compatibility policy; no rebuild - promotes the exact already-proven candidate per BR-01; per P2-017 local/opt-in observation only.
Completion evidence for the ledger: Feed population record; signed-installer listing consistency; blocked-bad-version refusal evidence.
Notes: Production feed hosting and signing-key invocation follow the updater lane design; key custody is the Release Engineering Owner.
```

```text
Execute ArcForges delivery task REL.11 — Family release readiness audit and honest statement.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\release.md (anchor task-rel-11).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/rel-11 (python tools/delivery.py claim REL.11 --worker <name>); task branch task/rel-11 in DesktopPlatform; ledger record ledger/tasks/rel-11.md.
Kind/size: release/L. Baseline: not-started.
Outcome: Every gate in release-gates.md is evaluated for every surface with a named, resolvable evidence artifact; every still-open gate's blocking consequence is stated; no cross-system failure row in architecture/20-cross-system-lifecycles.md lacks a run test; every public claim is backed by gate evidence, iOS is explicitly stated as outside current scope, and nothing incomplete is presented as complete.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-50.00 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\50-full-platform-production-release.md, anchor rule-wp-50.00
- WP-50.08 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\50-full-platform-production-release.md, anchor rule-wp-50.08
- WP-50.90 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\50-full-platform-production-release.md, anchor rule-wp-50.90

Entry condition: adoption slice ADOPT.02.release is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [release] REL.01: ArcNotes desktop release readiness complete
- [release] REL.02: ArcScope desktop release readiness complete
- [release] REL.03: ArcSlate desktop release readiness complete
- [release] REL.04: Android release readiness complete
- [release] REL.05: Web outputs release readiness complete
- [release] REL.06: Cloud/AI production readiness complete
- [release] REL.07: Contracts/SDK release audit complete
- [release] REL.08: commercial activation complete
- [release] REL.09: combined disaster drill and operational readiness confirmed
- [release] REL.10: production feed/signing switch complete
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Design:docs/assurance/wp50-00-readiness-audit.md, wp50-08-honest-statement.md, wp50-stage-acceptance.md/.json; DesktopPlatform:eng/release/**
Shared resources (follow the owner protocol): RES-design-evidence (append): Receipts and gate records are separate files per task or gate; indexes are appended; historical records are not rewritten.

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Gate-coverage report asserting no gate is unevaluated; evidence-resolution check asserting every claimed evidence artifact exists; cross-system failure-row coverage check; claim audit comparing every required feature and owner WP to real gate receipts and public claims; per P2-017 no new runtime beyond what each surface already produced.
Completion evidence for the ledger: Gate-coverage report; claim audit; WP50 stage-acceptance receipt joining REL.01-10.
Notes: Terminal task for the entire 51-package sequence (WP50 has no downstream). BR-01/BR-02/BR-03/BR-04 (build once, no partial pass, no waiving integrity/security/licence/regulatory gates, nothing incomplete presented as complete) all bind here directly.
```
