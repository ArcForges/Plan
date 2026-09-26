# ArcForges delivery task prompts — Android companion

Generated from Design `docs/planning/delivery/delivery-graph.json` by `tools/delivery.py`; do not edit by hand.
Each block is self-contained. Claim a task only when `python tools/delivery.py ready` lists it, with
`python tools/delivery.py claim <TASK-ID> --worker <name>`, then follow `arcforges-implementation.md`.
Tasks are ordered by lane for reading; the order is not a schedule.

## Android companion

```text
Execute ArcForges delivery task AND.01 — Android production identity and stable toolchain reconciliation.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\android.md (anchor task-and-01).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Mobile (integration owner: Mobile integration owner, the holder of roles/integration-mobile).
Claim and handoff record: claims/and-01 (python tools/delivery.py claim AND.01 --worker <name>); task branch task/and-01 in Mobile; ledger record ledger/tasks/and-01.md.
Kind/size: producer/M. Baseline: not-started.
Outcome: com.arcforges.mobile applicationId/namespace/source packages adopted, and a mutually compatible stable JDK21/AGP/Kotlin/Compose/Gradle tuple is pinned with wrapper checksums, version-catalog locks and generated-client compatibility evidence.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-30.00 (all work except the parts mapped to AND.04): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\30-mobile-shared-architecture.md, anchor rule-wp-30.00
- WP-30:3-binding-rules-apache-2-0-boundary-no-g §3 binding rules: Apache-2.0 boundary, no GPL-family implementation, immutable producer artifacts (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\30-mobile-shared-architecture.md, package-level obligation

Entry condition: adoption slice ADOPT.10.android is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] PRF.10: immutable toolchain compatibility manifest (exact AGP/Kotlin/Compose/Gradle versions proven together on a real release build)
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Mobile:app/build.gradle.kts; Mobile:app/src/main/AndroidManifest.xml; Mobile:app/src/main/kotlin/**; Mobile:gradle/libs.versions.toml; Mobile:gradle/locks/**; Mobile:gradle/verification-metadata.xml; Mobile:gradle/wrapper/gradle-wrapper.properties; Mobile:eng/policy/**; Mobile:eng/provenance/**
Shared resources (follow the owner protocol): RES-mobile-build-config (append): The module skeleton task registers all modules once and holds the lease `leases/res-mobile-build-config` while it restructures the build; later tasks edit only their module; catalog entries are appended and locks regenerated after rebase; dependency additions carry admission receipts.
Unblocks: AND.02, AND.04

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Windows/Linux full build, dependency-verification metadata check, package/certificate inspection under P2-017; device install and App Link fixture-key tests are local opt-in, not CI gates
Completion evidence for the ledger: Exact pinned tuple + wrapper checksums + regenerated locks; F-023 re-run showing closure holds after the identity change
Notes: Must also decide the KMP shared/ preview module's fate: arch-27's module map (core/*, feature/*) has no KMP target, so shared/ stays a dev-only convenience outside the shipped app graph, never a second production plan (per WP30 §4).
```

```text
Execute ArcForges delivery task AND.02 — Real Android module graph and AN01-AN25 route/state contracts.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\android.md (anchor task-and-02).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Mobile (integration owner: Mobile integration owner, the holder of roles/integration-mobile).
Claim and handoff record: claims/and-02 (python tools/delivery.py claim AND.02 --worker <name>); task branch task/and-02 in Mobile; ledger record ledger/tasks/and-02.md.
Kind/size: producer/L. Baseline: not-started.
Outcome: The arch-27 module set (app, core/domain, core/data, core/network, core/security, core/designsystem, feature/home, feature/chat, feature/tasks, feature/library, feature/settings) exists as enforced Gradle modules with typed AN01-AN25 navigation/state contracts; features depend only on typed core ports.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-30.01 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\30-mobile-shared-architecture.md, anchor rule-wp-30.01

Entry condition: adoption slice ADOPT.10.android is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] AND.01: renamed applicationId/namespace and pinned toolchain
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Mobile:settings.gradle.kts; Mobile:build.gradle.kts; Mobile:core/domain/**; Mobile:core/data/**; Mobile:core/network/**; Mobile:core/security/**; Mobile:core/designsystem/**; Mobile:feature/home/**; Mobile:feature/chat/**; Mobile:feature/tasks/**; Mobile:feature/library/**; Mobile:feature/settings/**
Shared resources (follow the owner protocol): RES-mobile-build-config (exclusive): The module skeleton task registers all modules once and holds the lease `leases/res-mobile-build-config` while it restructures the build; later tasks edit only their module; catalog entries are appended and locks regenerated after rebase; dependency additions carry admission receipts.
Unblocks: AND.03, AND.04, AND.05

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Architecture/import boundary tests (no React Native/iOS/AGPL imports, no cross-module leakage) as offline static checks; targeted offline unit tests per module
Completion evidence for the ledger: Module dependency graph report showing one-way core<-feature<-app dependencies; route ID inventory matching AN01-AN25
```

```text
Execute ArcForges delivery task AND.03 — Android runtime and OS adapters (Compose, Credential Manager, Keystore wrapper, WorkManager, FCM registration, SAF/MediaStore).

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\android.md (anchor task-and-03).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Mobile (integration owner: Mobile integration owner, the holder of roles/integration-mobile).
Claim and handoff record: claims/and-03 (python tools/delivery.py claim AND.03 --worker <name>); task branch task/and-03 in Mobile; ledger record ledger/tasks/and-03.md.
Kind/size: feature/L. Baseline: not-started.
Outcome: arm64 release / x64 emulator adapters for Compose, Credential Manager/passkey fallback, Keystore, WorkManager, FCM with non-GMS fallback, and SAF/MediaStore/FileProvider exist in core/security, core/data and core/network, with no unsafe fallback path.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-30.02 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\30-mobile-shared-architecture.md, anchor rule-wp-30.02

Entry condition: adoption slice ADOPT.10.android is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] AND.02: core/security, core/data, core/network module shells
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Mobile:core/security/**; Mobile:core/data/**; Mobile:core/network/**
Shared resources (follow the owner protocol): RES-mobile-build-config (append): The module skeleton task registers all modules once and holds the lease `leases/res-mobile-build-config` while it restructures the build; later tasks edit only their module; catalog entries are appended and locks regenerated after rebase; dependency additions carry admission receipts.
Unblocks: AND.06, AND.07, AND.08, AND.12

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Targeted offline unit tests for adapter contracts; install-on-real-device, permission-refusal, process-death and missing-Play-services scenarios are local opt-in under P2-017, not CI
Completion evidence for the ledger: Adapter test matrix (permission refusal, process death, missing Play services, callback after account switch) with device identity recorded for local runs
Notes: Can proceed in parallel with AND.04 (core/network gRPC client) and AND.05 (Room, core/data) once AND.02's skeleton lands; they touch different files within shared modules so should be sequenced as short-lived parallel PRs, not serialized.
```

```text
Execute ArcForges delivery task AND.04 — Published gRPC-Web contract consumption (Connect Kotlin client, binary framing, session/stream/retry adapters).

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\android.md (anchor task-and-04).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Mobile (integration owner: Mobile integration owner, the holder of roles/integration-mobile).
Claim and handoff record: claims/and-04 (python tools/delivery.py claim AND.04 --worker <name>); task branch task/and-04 in Mobile; ledger record ledger/tasks/and-04.md.
Kind/size: feature/M. Baseline: not-started.
Outcome: core/network wraps the pinned contracts-proto/contracts-connect-client Maven artifacts behind typed session/stream/retry/exact-value adapters, explicitly selecting binary gRPC-Web.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-30.03 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\30-mobile-shared-architecture.md, anchor rule-wp-30.03
- WP-30.00 (Kotlin Android foundation real package consumption): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\30-mobile-shared-architecture.md, anchor rule-wp-30.00

Entry condition: adoption slice ADOPT.10.android is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] AND.02: core/network module shell
- [contract] CON.07: io.github.arcforges:contracts-proto / contracts-connect-client Maven coordinates
- [contract] CON.11: published ApplicationService/HistoryService/EventService Kotlin Connect clients
- [artifact] AND.01: real, delivered outcome of AND.01 (Android production identity and stable toolchain reconciliation)
Completion prerequisites (may start earlier; cannot complete before these are complete):
- [integration] CLOUD.21: publicly deployed Cloud host serving the generated business RPC surface

Permitted write scope: Mobile:core/network/**
Shared resources (follow the owner protocol): RES-mobile-build-config (append): The module skeleton task registers all modules once and holds the lease `leases/res-mobile-build-config` while it restructures the build; later tasks edit only their module; catalog entries are appended and locks regenerated after rebase; dependency additions carry admission receipts.
Unblocks: AND.07, AND.08, AND.09, AND.10, AND.11, AND.12

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Targeted offline codec/adapter unit tests; real device/service calls against a deployed Cloud host are local opt-in evidence, not a CI gate (matches CloudHelloClient's existing pattern)
Completion evidence for the ledger: Real packaged Maven consumer + service/device call evidence with exact hashes/versions/device identity
Notes: Merged duplicate integration or closure task formerly proposed as CON.97.
```

```text
Execute ArcForges delivery task AND.05 — Room history, drafts, outbox and receipts.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\android.md (anchor task-and-05).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Mobile (integration owner: Mobile integration owner, the holder of roles/integration-mobile).
Claim and handoff record: claims/and-05 (python tools/delivery.py claim AND.05 --worker <name>); task branch task/and-05 in Mobile; ledger record ledger/tasks/and-05.md.
Kind/size: feature/L. Baseline: not-started.
Outcome: Room schemas (local_schema, scope_partition, projection, draft, outbox, transfer, cursor, preferences) implement per-profile partitions with a durable, bounded, never-silently-evicted outbox; local canonical history is not evictable cache.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-30.04 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\30-mobile-shared-architecture.md, anchor rule-wp-30.04

Entry condition: adoption slice ADOPT.10.android is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] AND.02: core/data module shell
- [contract] CON.11: model-05-equivalent typed records for projections/receipts
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Mobile:core/data/**
Shared resources (follow the owner protocol): RES-mobile-build-config (append): The module skeleton task registers all modules once and holds the lease `leases/res-mobile-build-config` while it restructures the build; later tasks edit only their module; catalog entries are appended and locks regenerated after rebase; dependency additions carry admission receipts.
Unblocks: AND.07, AND.08, AND.09, AND.10, AND.11

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline Room migration/instrumented-on-emulator-or-device tests for crash recovery, capacity refusal and atomic outbox writes; local opt-in for real-device runs under P2-017
Completion evidence for the ledger: Migration test results; outbox capacity-refusal and awaitingReconciliation replay tests; no silent eviction of draft/outbox rows
Notes: Fully local; remote Task/AI content reconciled through this store may use named fixtures until WP31/52 per the producer matrix ("Task/AI fixture allowed only until 31+52"), but the store/journal/outbox mechanics themselves must be real now.
```

```text
Execute ArcForges delivery task AND.06 — Secure per-account lifecycle: Keystore encryption, no-backup policy, purge/quarantine, deep-link validation.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\android.md (anchor task-and-06).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Mobile (integration owner: Mobile integration owner, the holder of roles/integration-mobile).
Claim and handoff record: claims/and-06 (python tools/delivery.py claim AND.06 --worker <name>); task branch task/and-06 in Mobile; ledger record ledger/tasks/and-06.md.
Kind/size: feature/M. Baseline: not-started.
Outcome: Per-account Keystore-encrypted secret/pending-store policy, session/logout/revoke purge vs unsent-work quarantine/export, same-generation deep-link validation and current-foreground consent are implemented in core/security.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-30.05 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\30-mobile-shared-architecture.md, anchor rule-wp-30.05

Entry condition: adoption slice ADOPT.10.android is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] AND.03: Keystore/Credential Manager adapter wrapper
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Mobile:core/security/**
Unblocks: AND.07, AND.08, AND.12

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline unit tests for encryption/purge/quarantine logic; device-restore-without-key, logout-while-requests-run, deep-link-spoof and secret-scan-of-release-logs are local opt-in under P2-017
Completion evidence for the ledger: Secret scan of release logs/backup showing no credential leakage; device restore and logout-while-in-flight scenario results
```

```text
Execute ArcForges delivery task AND.07 — Foundation integration evidence: real candidate against deployed 22/23/24/25.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\android.md (anchor task-and-07).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Mobile (integration owner: Mobile integration owner, the holder of roles/integration-mobile).
Claim and handoff record: claims/and-07 (python tools/delivery.py claim AND.07 --worker <name>); task branch task/and-07 in Mobile; ledger record ledger/tasks/and-07.md.
Kind/size: integration/M. Baseline: not-started.
Outcome: A candidate APK is built, installed clean and exercises real sign-in/hydration/upload/reconnect on a physical device against actually deployed Cloud identity/API/realtime/sync; any Task/AI fixtures still present are named and confirmed compiled out of production before WP31.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-30.90 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\30-mobile-shared-architecture.md, anchor rule-wp-30.90
- WP-23.05 (Android real-consumer integration beyond the WP-06 probe): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\23-public-api-and-generated-clients.md, anchor rule-wp-23.05

Entry condition: adoption slice ADOPT.10.android is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] AND.03: OS adapters complete
- [artifact] AND.04: gRPC-Web client complete
- [artifact] AND.05: Room store complete
- [artifact] AND.06: secure lifecycle complete
- [artifact] CLOUD.13: deployed identity/session service
- [artifact] CLOUD.42: deployed R2/sync/hydration
- [artifact] CLOUD.39: deployed guarded publication and convergent bootstrap
- [artifact] CLOUD.18: real, delivered outcome of CLOUD.18 (Independent native session integration (Platform client primitives))
- [artifact] CLOUD.19: real, delivered outcome of CLOUD.19 (Browser cookie-session adapter and full account-surface closure)
- [artifact] CLOUD.26: real, delivered outcome of CLOUD.26 (Generated C#/TypeScript/Kotlin clients against Identity/Workspace/Device)
- [artifact] CLOUD.29: real, delivered outcome of CLOUD.29 (Stream connection and authentication (EventService.Watch/ExecutionService.WatchOutput shells))
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Mobile:app/**
Unblocks: AND.08, AND.09, AND.10, AND.11, AND.12, CLOUD.28

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Clean-cache restore/build/install on a real device is local opt-in evidence per P2-017; CI only runs the offline/static portion
Completion evidence for the ledger: Owned-artifact-and-real-integration receipt: source commit, producer versions, candidate hashes, actual device identity, scenario, result, real-vs-fixture status per field
Notes: Merged duplicate integration or closure task formerly proposed as CLOUD.60.
```

```text
Execute ArcForges delivery task AND.08 — Authentication, Home and workspace (AN01-AN06).

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\android.md (anchor task-and-08).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Mobile (integration owner: Mobile integration owner, the holder of roles/integration-mobile).
Claim and handoff record: claims/and-08 (python tools/delivery.py claim AND.08 --worker <name>); task branch task/and-08 in Mobile; ledger record ledger/tasks/and-08.md.
Kind/size: feature/L. Baseline: not-started.
Outcome: System authentication, five-destination navigation and per-device application selection are complete with real Cloud identity/presence and explicit history disclosure.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-31.00 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\31-arcchat-mobile-android.md, anchor rule-wp-31.00

Entry condition: adoption slice ADOPT.10.android is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] AND.03: the real Android foundation module AND.03 this feature is built on
- [artifact] AND.04: the real Android foundation module AND.04 this feature is built on
- [artifact] AND.05: the real Android foundation module AND.05 this feature is built on
- [artifact] AND.06: the real Android foundation module AND.06 this feature is built on
Completion prerequisites (may start earlier; cannot complete before these are complete):
- [integration] AND.07: foundation candidate proven against the deployed Cloud services

Permitted write scope: Mobile:feature/home/**; Mobile:app/**
Unblocks: AND.13, AND.14, AND.15, AND.19

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Instrumented UI tests offline where feasible; scope/permission, wrong/stale target, loss/retry and expiry scenarios against real WP22/23 are local opt-in
Completion evidence for the ledger: Full account/attention path walkthrough against real Cloud endpoints
Notes: Does not need WP26 (remote bridge), WP45 (push sender) or WP52 (Harness) to start or complete — only WP30's own foundation and the already-deployed WP22/23. Demonstrates that not all Android features wait on the complete Harness.
```

```text
Execute ArcForges delivery task AND.09 — Conversations and context (AN07-AN10/15/16).

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\android.md (anchor task-and-09).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Mobile (integration owner: Mobile integration owner, the holder of roles/integration-mobile).
Claim and handoff record: claims/and-09 (python tools/delivery.py claim AND.09 --worker <name>); task branch task/and-09 in Mobile; ledger record ledger/tasks/and-09.md.
Kind/size: feature/L. Baseline: not-started.
Outcome: Native composer/IME/branch/context, history modes/promotion and real binary output streams work end-to-end for own-application scope, with no desktop local-history access.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-31.01 (all work except the parts mapped to AND.24): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\31-arcchat-mobile-android.md, anchor rule-wp-31.01

Entry condition: adoption slice ADOPT.10.android is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] AND.04: the real Android foundation module AND.04 this feature is built on
- [artifact] AND.05: the real Android foundation module AND.05 this feature is built on
Completion prerequisites (may start earlier; cannot complete before these are complete):
- [integration] AND.24: real CF Harness admission/generation/tool loop
- [integration] AND.07: foundation candidate proven against the deployed Cloud services

Permitted write scope: Mobile:feature/chat/**
Permitted substitutes (never real integration evidence): SUB-fixture-turn-endpoint: client-side session/event/output/upload handling, typed state transitions, reconnection -- runs no model/planner/admission/metering itself Real producer ['HAR.00', 'HAR.02', 'HAR.03']; removed by HAR.05
Unblocks: AND.13, AND.14, AND.15, AND.19, AND.24

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline stream-codec/cursor unit tests; real-device streaming/reconnect scenarios against the deployed (fixture-backed until WP52.05) endpoint are local opt-in
Completion evidence for the ledger: History/pending-input/stream/final-message consistency under every declared recovery outcome
```

```text
Execute ArcForges delivery task AND.10 — Tasks, approvals and automation (AN11-AN13/19/25).

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\android.md (anchor task-and-10).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Mobile (integration owner: Mobile integration owner, the holder of roles/integration-mobile).
Claim and handoff record: claims/and-10 (python tools/delivery.py claim AND.10 --worker <name>); task branch task/and-10 in Mobile; ledger record ledger/tasks/and-10.md.
Kind/size: feature/L. Baseline: not-started.
Outcome: Task/approval/automation surfaces enforce action, risk, credit-consent and consumption-only rules with one real owner outcome/settlement per command.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-31.02 (all work except the parts mapped to AND.24, AND.25): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\31-arcchat-mobile-android.md, anchor rule-wp-31.02

Entry condition: adoption slice ADOPT.10.android is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] AND.04: the real Android foundation module AND.04 this feature is built on
- [artifact] AND.05: the real Android foundation module AND.05 this feature is built on
Completion prerequisites (may start earlier; cannot complete before these are complete):
- [integration] AND.25: real device bridge with lease/current-grant/unknown-effect reconciliation
- [integration] AND.24: real Harness planning/tool-proposal loop
- [integration] AND.07: foundation candidate proven against the deployed Cloud services

Permitted write scope: Mobile:feature/tasks/**
Permitted substitutes (never real integration evidence): SUB-automation-fixture: client rendering of schedule/timezone/target/budget and action availability, offline-draft handling only Real producer ['HAR.06']; removed by HAR.06
Unblocks: AND.13, AND.14, AND.15, AND.19, AND.24, AND.25

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline idempotency/state-machine unit tests; real bridge/Harness/commerce scenarios are local opt-in against deployed services
Completion evidence for the ledger: One real owner outcome/settlement per command; no broad implicit grant or hidden background write
```

```text
Execute ArcForges delivery task AND.11 — Library and resources (AN14-AN18/22).

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\android.md (anchor task-and-11).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Mobile (integration owner: Mobile integration owner, the holder of roles/integration-mobile).
Claim and handoff record: claims/and-11 (python tools/delivery.py claim AND.11 --worker <name>); task branch task/and-11 in Mobile; ledger record ledger/tasks/and-11.md.
Kind/size: feature/M. Baseline: not-started.
Outcome: Native preview/import/export/transfer flows handle missing/denied/unsupported states with correct local/cloud copy and deletion semantics.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-31.03 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\31-arcchat-mobile-android.md, anchor rule-wp-31.03

Entry condition: adoption slice ADOPT.10.android is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] AND.04: the real Android foundation module AND.04 this feature is built on
- [artifact] AND.05: the real Android foundation module AND.05 this feature is built on
Completion prerequisites (may start earlier; cannot complete before these are complete):
- [integration] AND.07: foundation candidate proven against the deployed Cloud services

Permitted write scope: Mobile:feature/library/**
Unblocks: AND.13, AND.15, AND.19

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline transfer-journal unit tests; resumable-upload/hash-mismatch/process-death-during-transfer scenarios are local opt-in on real devices
Completion evidence for the ledger: No unavailable bytes represented as empty success; resumable journal survives process death
Notes: Independent of WP26/WP45/WP52 — can complete in parallel with AND.09/AND.10 once the foundation (AND.07) lands.
```

```text
Execute ArcForges delivery task AND.12 — Presence, push, links and settings (AN20-AN24).

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\android.md (anchor task-and-12).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Mobile (integration owner: Mobile integration owner, the holder of roles/integration-mobile).
Claim and handoff record: claims/and-12 (python tools/delivery.py claim AND.12 --worker <name>); task branch task/and-12 in Mobile; ledger record ledger/tasks/and-12.md.
Kind/size: feature/M. Baseline: not-started.
Outcome: Presence/push/deep-link/settings surfaces stay usable through declared polling/notification fallback, with no purchase/store billing surface and no exposure of a revoked resource on background reconnect.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-31.04 (all work except the parts mapped to AND.26): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\31-arcchat-mobile-android.md, anchor rule-wp-31.04
- WP-31:pg-24-completion-gate-paragraph-physical PG-24 completion-gate paragraph: physical arm64 push/Doze/background evidence (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\31-arcchat-mobile-android.md, package-level obligation

Entry condition: adoption slice ADOPT.10.android is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [contract] CON.22: published notification.registerPush and unregisterPush
- [artifact] AND.03: the real Android foundation module AND.03 this feature is built on
- [artifact] AND.04: the real Android foundation module AND.04 this feature is built on
- [artifact] AND.06: the real Android foundation module AND.06 this feature is built on
Completion prerequisites (may start earlier; cannot complete before these are complete):
- [integration] AND.26: live FCM sender adapter with a project-bound credential
- [integration] AND.07: foundation candidate proven against the deployed Cloud services

Permitted write scope: Mobile:feature/settings/**; Mobile:core/network/**
Shared resources (follow the owner protocol): RES-mobile-build-config (append): The module skeleton task registers all modules once and holds the lease `leases/res-mobile-build-config` while it restructures the build; later tasks edit only their module; catalog entries are appended and locks regenerated after rebase; dependency additions carry admission receipts.
Unblocks: AND.13, AND.15, AND.19, AND.26

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline notification-dedup/registration unit tests; physical-device push receipt, Doze/background behavior and no-GMS fallback are local opt-in per PG-24
Completion evidence for the ledger: Physical device receipt of a real push; denied-permission and no-GMS durable-polling fallback observed
```

```text
Execute ArcForges delivery task AND.13 — Native interaction and recovery: full experience-02 device matrix.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\android.md (anchor task-and-13).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Mobile (integration owner: Mobile integration owner, the holder of roles/integration-mobile).
Claim and handoff record: claims/and-13 (python tools/delivery.py claim AND.13 --worker <name>); task branch task/and-13 in Mobile; ledger record ledger/tasks/and-13.md.
Kind/size: integration/L. Baseline: not-started.
Outcome: The complete phone/tablet/back/IME/TalkBack/large-text/process-death/account-switch/denied-permission/no-GMS matrix from experience 02 passes against real services on a release APK, preserving typed effect uncertainty and drafts.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-31.05 (all work except the parts mapped to AND.25): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\31-arcchat-mobile-android.md, anchor rule-wp-31.05

Entry condition: adoption slice ADOPT.10.android is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] AND.08: auth/home built
- [artifact] AND.09: chat built
- [artifact] AND.10: tasks built
- [artifact] AND.11: library built
- [artifact] AND.12: settings/push built
Completion prerequisites (may start earlier; cannot complete before these are complete):
- [integration] AND.24: real Harness evidence
- [integration] AND.25: real bridge evidence

Permitted write scope: Mobile:app/src/androidTest/**
Unblocks: AND.15, AND.25

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Physical low/mid-tier arm64 device matrix (1000 messages, 4 MiB answer, rotation, process kill during send/refresh/upload, denied push, airplane/reconnect, account switch, expired approval, revoked source) is local opt-in under P2-017
Completion evidence for the ledger: Per-scenario pass/fail with device identity and TalkBack/IME/large-text results
```

```text
Execute ArcForges delivery task AND.14 — Scope and licence enforcement audit.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\android.md (anchor task-and-14).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Mobile (integration owner: Mobile integration owner, the holder of roles/integration-mobile).
Claim and handoff record: claims/and-14 (python tools/delivery.py claim AND.14 --worker <name>); task branch task/and-14 in Mobile; ledger record ledger/tasks/and-14.md.
Kind/size: acceptance/S. Baseline: not-started.
Outcome: Full companion requirements, consumption-only restrictions, public-Maven-only imports, and absence of desktop secrets/device-local paths/excluded professional-editing surfaces are verified with complete provenance.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-31.06 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\31-arcchat-mobile-android.md, anchor rule-wp-31.06
- WP-30:3-binding-rules-apache-2-0-boundary-no-g §3 binding rules: Apache-2.0 boundary, no GPL-family implementation, immutable producer artifacts (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\30-mobile-shared-architecture.md, package-level obligation

Entry condition: adoption slice ADOPT.10.android is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] AND.08: features exist to audit
- [artifact] AND.09: features exist to audit
- [artifact] AND.10: features exist to audit
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Mobile:eng/policy/**; Mobile:eng/provenance/**
Shared resources (follow the owner protocol): RES-mobile-build-config (append): The module skeleton task registers all modules once and holds the lease `leases/res-mobile-build-config` while it restructures the build; later tasks edit only their module; catalog entries are appended and locks regenerated after rebase; dependency additions carry admission receipts.
Unblocks: AND.15

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Package content/dependency/privacy static checks plus full surface-action inventory cross-check, offline
Completion evidence for the ledger: Complete surface/action inventory cross-check with no unaccepted third-party provenance
```

```text
Execute ArcForges delivery task AND.15 — Complete companion acceptance.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\android.md (anchor task-and-15).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Mobile (integration owner: Mobile integration owner, the holder of roles/integration-mobile).
Claim and handoff record: claims/and-15 (python tools/delivery.py claim AND.15 --worker <name>); task branch task/and-15 in Mobile; ledger record ledger/tasks/and-15.md.
Kind/size: integration/M. Baseline: not-started.
Outcome: A signed candidate joins real 31.00-31.06 evidence with producer manifests and the full compatible 52/26/25/42/45 integration manifest, verified through injected-failure scenarios with exact device/OS/server/worker/package identities.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-31.90 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\31-arcchat-mobile-android.md, anchor rule-wp-31.90
- WP-31:pg-24-completion-gate-paragraph-physical PG-24 completion-gate paragraph: physical arm64 push/Doze/background evidence (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\31-arcchat-mobile-android.md, package-level obligation

Entry condition: adoption slice ADOPT.10.android is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] AND.08: all WP31 substep tasks complete
- [artifact] AND.09: all WP31 substep tasks complete
- [artifact] AND.10: all WP31 substep tasks complete
- [artifact] AND.11: all WP31 substep tasks complete
- [artifact] AND.12: all WP31 substep tasks complete
- [artifact] AND.13: all WP31 substep tasks complete
- [artifact] AND.14: all WP31 substep tasks complete
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Mobile:app/**
Unblocks: AND.16

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Full physical-device release scenarios and injected failure matrix, local opt-in under P2-017
Completion evidence for the ledger: Owned-artifact-and-real-integration receipt joining all producer manifests; distribution/store activation explicitly deferred to WP32
```

```text
Execute ArcForges delivery task AND.16 — Signed Android release artifacts (AAB + direct APK).

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\android.md (anchor task-and-16).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Mobile (integration owner: Mobile integration owner, the holder of roles/integration-mobile).
Claim and handoff record: claims/and-16 (python tools/delivery.py claim AND.16 --worker <name>); task branch task/and-16 in Mobile; ledger record ledger/tasks/and-16.md.
Kind/size: release/S. Baseline: not-started.
Outcome: AAB (Play) and a separately signed direct APK build automatically from reviewed main with monotonic versionCode, immutable provenance and tested WP03 update-schema compatibility.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-32.00 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\32-mobile-release-and-store-gates.md, anchor rule-wp-32.00

Entry condition: adoption slice ADOPT.10.android is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] AND.15: companion acceptance complete
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Mobile:.github/workflows/ci.yml; Mobile:eng/mobile.py
Shared resources (follow the owner protocol): RES-android-signing-and-store (append): Used only by release tasks through protected CI environments; no task creates replacement keys or listings.
Unblocks: AND.17, AND.18, AND.21

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Actual signature/package/R8/runtime and version-monotonicity checks; clean device install/upgrade is local opt-in
Completion evidence for the ledger: Signed AAB/APK with recorded provenance and monotonic versionCode
```

```text
Execute ArcForges delivery task AND.17 — Release runtime inspection.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\android.md (anchor task-and-17).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Mobile (integration owner: Mobile integration owner, the holder of roles/integration-mobile).
Claim and handoff record: claims/and-17 (python tools/delivery.py claim AND.17 --worker <name>); task branch task/and-17 in Mobile; ledger record ledger/tasks/and-17.md.
Kind/size: acceptance/S. Baseline: not-started.
Outcome: Kotlin/ART, Compose/public grpc-lite closure, min/target API, arm64 assets, R8 rules and required permissions are verified on the actual signed APK/AAB, not source inspection.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-32.01 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\32-mobile-release-and-store-gates.md, anchor rule-wp-32.01

Entry condition: adoption slice ADOPT.10.android is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] AND.16: signed candidate
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Mobile:eng/mobile.py
Unblocks: AND.23

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Install without development server/toolchain; startup/identity/RPC/notifications/lifecycle release tests are local opt-in
Completion evidence for the ledger: VG-07 evidence: real Kotlin/ART release artifact inspection, not debug-only or source-only proof
```

```text
Execute ArcForges delivery task AND.18 — Dependency and source rights closure (final artifact).

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\android.md (anchor task-and-18).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Mobile (integration owner: Mobile integration owner, the holder of roles/integration-mobile).
Claim and handoff record: claims/and-18 (python tools/delivery.py claim AND.18 --worker <name>); task branch task/and-18 in Mobile; ledger record ledger/tasks/and-18.md.
Kind/size: acceptance/S. Baseline: not-started.
Outcome: Direct/transitive Gradle/plugin/runtime/asset closure, licences, provenance and reproducible SBOM/NOTICE are audited against the final companion candidate; public schema/tooling Apache origin and independently original app implementation are verified.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-32.02 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\32-mobile-release-and-store-gates.md, anchor rule-wp-32.02

Entry condition: adoption slice ADOPT.10.android is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] AND.16: signed candidate
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Mobile:eng/policy/**; Mobile:eng/provenance/**; Mobile:third-party/**
Shared resources (follow the owner protocol): RES-mobile-build-config (append): The module skeleton task registers all modules once and holds the lease `leases/res-mobile-build-config` while it restructures the build; later tasks edit only their module; catalog entries are appended and locks regenerated after rebase; dependency additions carry admission receipts.
Unblocks: AND.23

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Forbidden-licence fixture, unpinned/dynamic dependency and changed-checksum rejection tests, offline
Completion evidence for the ledger: F-023 re-closure for the final companion candidate (binary inventory matches candidate)
```

```text
Execute ArcForges delivery task AND.19 — Consumption-only enforcement.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\android.md (anchor task-and-19).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Mobile (integration owner: Mobile integration owner, the holder of roles/integration-mobile).
Claim and handoff record: claims/and-19 (python tools/delivery.py claim AND.19 --worker <name>); task branch task/and-19 in Mobile; ledger record ledger/tasks/and-19.md.
Kind/size: acceptance/M. Baseline: not-started.
Outcome: Absence of purchase buttons/embedded checkout/store billing/external purchase CTAs/licence-key unlock is enforced by static route/dependency checks and exercised across every state including expired subscription and exhausted credits.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-32.03 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\32-mobile-release-and-store-gates.md, anchor rule-wp-32.03

Entry condition: adoption slice ADOPT.10.android is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] AND.08: every authentication and Home state to audit
- [artifact] AND.09: every conversation state to audit
- [artifact] AND.10: every task, approval and automation state to audit
- [artifact] AND.11: every library and resource state to audit
- [artifact] AND.12: every presence, push, link and settings state to audit
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Mobile:eng/policy/**
Unblocks: AND.23

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Static route/dependency checks (MC-01..MC-06 build-time/CI assertions) plus all-state UX tests, offline where feasible
Completion evidence for the ledger: VG-13 evidence: no build path can display a purchase CTA or accept a licence key
```

```text
Execute ArcForges delivery task AND.20 — Play and direct-channel signed update client.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\android.md (anchor task-and-20).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Mobile (integration owner: Mobile integration owner, the holder of roles/integration-mobile).
Claim and handoff record: claims/and-20 (python tools/delivery.py claim AND.20 --worker <name>); task branch task/and-20 in Mobile; ledger record ledger/tasks/and-20.md.
Kind/size: feature/M. Baseline: not-started.
Outcome: arch-11 channel behavior and a notify-only signed update client are complete, consuming WP03's format/fixture keys now; channel-switch export/reinstall guidance is explicit.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-32.04 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\32-mobile-release-and-store-gates.md, anchor rule-wp-32.04

Entry condition: adoption slice ADOPT.10.android is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [contract] CON.16: android-update.v1 feed format and fixture signing keys
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Mobile:core/network/**; Mobile:feature/settings/**
Shared resources (follow the owner protocol): RES-mobile-build-config (append): The module skeleton task registers all modules once and holds the lease `leases/res-mobile-build-config` while it restructures the build; later tasks edit only their module; catalog entries are appended and locks regenerated after rebase; dependency additions carry admission receipts.
Unblocks: AND.23

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Expired/rollback/wrong-certificate/URL/hash and offline-stale-feed tests, offline where feasible
Completion evidence for the ledger: Play primary + direct APK flow complete with no silent install
Notes: Explicitly does NOT wait on WP53 (production feed/signing) — WP-32.04's own text states WP53's replacement is verified at WP50, not a backward input to this task.
```

```text
Execute ArcForges delivery task AND.21 — Physical device and recovery gates.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\android.md (anchor task-and-21).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Mobile (integration owner: Mobile integration owner, the holder of roles/integration-mobile).
Claim and handoff record: claims/and-21 (python tools/delivery.py claim AND.21 --worker <name>); task branch task/and-21 in Mobile; ledger record ledger/tasks/and-21.md.
Kind/size: integration/L. Baseline: not-started.
Outcome: Full companion runs on minimum-supported and current physical-device profiles across weak/offline network, permission denial, no-GMS, key-loss/backup-restore, process kill and OS background limits; forward-rescue release with a higher versionCode is proven (Android never downgrades as routine rollback).

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-32.05 (all work except the parts mapped to AND.26): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\32-mobile-release-and-store-gates.md, anchor rule-wp-32.05

Entry condition: adoption slice ADOPT.10.android is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] AND.16: signed candidate
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Mobile:eng/mobile.py
Unblocks: AND.23, AND.26

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Actual local/server unknown-effect replay, encrypted draft/outbox retention through upgrade, signing-key recovery rehearsal — all local opt-in under P2-017
Completion evidence for the ledger: All mandatory scenarios pass; material device limits disclosed; no pending user work lost
```

```text
Execute ArcForges delivery task AND.22 — Android scope statement.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\android.md (anchor task-and-22).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Mobile (integration owner: Mobile integration owner, the holder of roles/integration-mobile).
Claim and handoff record: claims/and-22 (python tools/delivery.py claim AND.22 --worker <name>); task branch task/and-22 in Mobile; ledger record ledger/tasks/and-22.md.
Kind/size: acceptance/S. Baseline: not-started.
Outcome: Documentation and store/release/readme/platform matrices state Android-only scope; iOS/Swift/KMP/cross-platform UI are recorded as outside this delivery with no false retained-iOS claim.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-32.06 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\32-mobile-release-and-store-gates.md, anchor rule-wp-32.06

Entry condition: adoption slice ADOPT.10.android is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- none
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Mobile:README.md; Mobile:docs/**
Unblocks: AND.23

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Store/release/readme/platform matrix cross-check against the signed Android artifact, offline
Completion evidence for the ledger: No false retained-iOS deliverable or unsupported platform claim
Notes: Small and independent; can land in the same PR series as AND.18 or AND.19 for convenience without being merged into them as one task.
```

```text
Execute ArcForges delivery task AND.23 — Distribution acceptance.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\android.md (anchor task-and-23).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Mobile (integration owner: Mobile integration owner, the holder of roles/integration-mobile).
Claim and handoff record: claims/and-23 (python tools/delivery.py claim AND.23 --worker <name>); task branch task/and-23 in Mobile; ledger record ledger/tasks/and-23.md.
Kind/size: release/M. Baseline: not-started.
Outcome: The exact signed APK/AAB, manifest/hash/versionCode/certificate identity, compatible server/Contracts release and all gate receipts are archived and published through the automatic main graph; a clean-device download verifies signature/hash and exercises actual services.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-32.90 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\32-mobile-release-and-store-gates.md, anchor rule-wp-32.90
- WP-32:pg-24-completion-gate-paragraph-recheck PG-24 completion-gate paragraph (recheck on distributed artifact) (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\32-mobile-release-and-store-gates.md, package-level obligation

Entry condition: adoption slice ADOPT.10.android is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] AND.17: release runtime inspection passed
- [artifact] AND.18: dependency rights closed
- [artifact] AND.19: consumption-only verified
- [artifact] AND.20: update client complete
- [artifact] AND.21: device/recovery gates passed
- [artifact] AND.22: scope statement complete
Completion prerequisites (may start earlier; cannot complete before these are complete):
- [integration] AND.26: live FCM sender + physical receipt rechecked on the distributed artifact

Permitted write scope: Mobile:eng/mobile.py
Shared resources (follow the owner protocol): RES-android-signing-and-store (append): Used only by release tasks through protected CI environments; no task creates replacement keys or listings.
Unblocks: AND.26, REL.04

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Download public candidate in a clean device path, verify signature/hash, exercise actual services — local opt-in
Completion evidence for the ledger: Distribution complete only with real receipts; VG-13 store-submission confirmation
```

```text
Execute ArcForges delivery task AND.24 — Real CF Harness generation/tool loop observed end to end on Android.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\android.md (anchor task-and-24).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Mobile (integration owner: Mobile integration owner, the holder of roles/integration-mobile).
Claim and handoff record: claims/and-24 (python tools/delivery.py claim AND.24 --worker <name>); task branch task/and-24 in Mobile; ledger record ledger/tasks/and-24.md.
Kind/size: integration/M. Baseline: not-started.
Outcome: real admitted generation, tool proposal and automation execution replace the contract-bound fixture turn endpoint on a physical device

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-31.01 (real-integration closure): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\31-arcchat-mobile-android.md, anchor rule-wp-31.01
- WP-31.02 (real-integration closure): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\31-arcchat-mobile-android.md, anchor rule-wp-31.02

Entry condition: adoption slice ADOPT.10.android is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] AND.09: real, delivered outcome of AND.09 (Conversations and context (AN07-AN10/15/16))
- [artifact] AND.10: real, delivered outcome of AND.10 (Tasks, approvals and automation (AN11-AN13/19/25))
- [artifact] HAR.00: real, delivered outcome of HAR.00 (Turn loop, tool batching and bounds (RunWorkflow core))
- [artifact] HAR.03: real generated streaming and durable output
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: 
Unblocks: AND.09, AND.10, AND.13, HAR.05, HAR.06

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Local real-integration run of the affected scenario in an existing environment, recorded once; offline and static checks in CI; no hosted runtime, device, browser, live-service or inference CI (P2-017).
Completion evidence for the ledger: real admitted generation, tool proposal and automation execution replace the contract-bound fixture turn endpoint on a physical device
```

```text
Execute ArcForges delivery task AND.25 — Real desktop tool dispatch and unknown-effect reconciliation from Android.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\android.md (anchor task-and-25).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Mobile (integration owner: Mobile integration owner, the holder of roles/integration-mobile).
Claim and handoff record: claims/and-25 (python tools/delivery.py claim AND.25 --worker <name>); task branch task/and-25 in Mobile; ledger record ledger/tasks/and-25.md.
Kind/size: integration/M. Baseline: not-started.
Outcome: an Android-initiated remote task actually reaches a desktop through the durable bridge with correct lease/grant/reconciliation semantics

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-31.02 (device-dispatch closure): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\31-arcchat-mobile-android.md, anchor rule-wp-31.02
- WP-31.05 (real-52/26 evidence): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\31-arcchat-mobile-android.md, anchor rule-wp-31.05

Entry condition: adoption slice ADOPT.10.android is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] AND.10: real, delivered outcome of AND.10 (Tasks, approvals and automation (AN11-AN13/19/25))
- [artifact] AND.13: real, delivered outcome of AND.13 (Native interaction and recovery: full experience-02 device matrix)
- [artifact] DEV.02: the real durable target queue
- [artifact] DEV.03: real owner reauthorization on the desktop
- [artifact] DEV.06: real remote approval and steering
- [artifact] DEV.07: real offline expiry and unknown-effect recovery
- [artifact] DEV.12: the cross-repository (toolRequestId, attemptId, commandId) agreement
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: 
Unblocks: AND.10, AND.13

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Local real-integration run of the affected scenario in an existing environment, recorded once; offline and static checks in CI; no hosted runtime, device, browser, live-service or inference CI (P2-017).
Completion evidence for the ledger: an Android-initiated remote task actually reaches a desktop through the durable bridge with correct lease/grant/reconciliation semantics
```

```text
Execute ArcForges delivery task AND.26 — Real FCM sending and physical Android receipt.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\android.md (anchor task-and-26).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Mobile (integration owner: Mobile integration owner, the holder of roles/integration-mobile).
Claim and handoff record: claims/and-26 (python tools/delivery.py claim AND.26 --worker <name>); task branch task/and-26 in Mobile; ledger record ledger/tasks/and-26.md.
Kind/size: integration/M. Baseline: not-started.
Outcome: PG-24: a project-bound FCM credential actually sends and a physical arm64 device actually receives, including duplicate/rotation/revocation and denied-permission/no-GMS recovery

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-31.04 (physical receipt closure): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\31-arcchat-mobile-android.md, anchor rule-wp-31.04
- WP-32:pg-24-completion-gate-paragraph-recheck PG-24 completion-gate paragraph (recheck on distributed artifact) (PG-24 closure): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\32-mobile-release-and-store-gates.md, package-level obligation
- WP-45.09 (device-delivery half): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\45-operations-support-and-trust-safety.md, anchor rule-wp-45.09
- WP-32.05 (physical/no-GMS/permission evidence half): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\32-mobile-release-and-store-gates.md, anchor rule-wp-32.05

Entry condition: adoption slice ADOPT.10.android is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] AND.12: real, delivered outcome of AND.12 (Presence, push, links and settings (AN20-AN24))
- [artifact] AND.23: real, delivered outcome of AND.23 (Distribution acceptance)
- [artifact] OPS.10: real, delivered outcome of OPS.10 (Customer push delivery and registration lifecycle)
- [artifact] AND.21: real, delivered outcome of AND.21 (Physical device and recovery gates)
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: 
Unblocks: AND.12, AND.23, OPS.10, OPS.12

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Local real-integration run of the affected scenario in an existing environment, recorded once; offline and static checks in CI; no hosted runtime, device, browser, live-service or inference CI (P2-017).
Completion evidence for the ledger: PG-24: a project-bound FCM credential actually sends and a physical arm64 device actually receives, including duplicate/rotation/revocation and denied-permission/no-GMS recovery
Notes: Merged duplicate integration or closure task formerly proposed as COM.17.
```
