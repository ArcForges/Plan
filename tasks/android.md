# ArcForges delivery task prompts — Android companion

Generated from Design `docs/planning/delivery/delivery-graph.json` by `tools/delivery.py`; do not edit by hand.
Each block is self-contained. Claim a task only when `python tools/delivery.py ready` lists it, with
`python tools/delivery.py claim <TASK-ID> --worker <name>`, then follow `arcforges-implementation.md`.
Tasks are ordered by lane for reading; the order is not a schedule.

## Android companion

```text
Execute ArcForges delivery task AND.01 — Android production identity and .NET MAUI toolchain pins.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\android.md (anchor task-and-01).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Mobile (integration owner: Mobile integration owner, the holder of roles/integration-mobile).
Claim and handoff record: claims/and-01 (python tools/delivery.py claim AND.01 --worker <name>); task branch task/and-01 in Mobile; ledger record ledger/tasks/and-01.md.
Kind/size: producer/M. Baseline: not-started.
Outcome: com.arcforges.mobile applicationId, namespace and source packages adopted, with reinstall guidance from the development prerelease io.github.arcforges.mobile recorded in docs/releasing.md (reinstall with no data migration; the prerelease holds no production user data); the persistent android-release signing identity is kept (cert SHA256 7a8b3b14...); and a mutually compatible .NET 10 LTS SDK, Android workload, MAUI and NuGet tuple is pinned as candidate pins with global.json, central package versions (Directory.Packages.props), packages.lock.json locks, SDK and workload integrity pins and dependency-admission records, plus generated-client compatibility evidence (the NuGet Contracts client restores and builds against the candidate tuple). Every Mobile project targets net10.0-android only (P2-021.3), with UseMonoRuntime=true set explicitly; platform-neutral domain and feature projects (AND.02) contain no Android or platform API references but use the same single target. The exact tuple is not proven by this task: the first release-build proof is AND.40's CI gate, and PRF.12 proves the tuple on the device before this task completes.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-30.00 (all work except the parts mapped to AND.04): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\30-mobile-shared-architecture.md, anchor rule-wp-30.00
- WP-30:3-binding-rules-apache-2-0-boundary-no-g §3 binding rules: Apache-2.0 boundary, no GPL-family implementation, immutable producer artifacts (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\30-mobile-shared-architecture.md, package-level obligation

Entry condition: adoption slice ADOPT.10.android is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- none
Completion prerequisites (may start earlier; cannot complete before these are complete):
- [integration] PRF.12: the MAUI Android release proof recording the exact compatible .NET 10 / Android workload / NuGet tuple

Permitted write scope: Mobile:global.json; Mobile:Directory.Build.props; Mobile:Directory.Packages.props; Mobile:NuGet.config; Mobile:eng/policy/**; Mobile:eng/provenance/**; Mobile:eng/build_identity.py; Mobile:eng/version-sources.json; Mobile:src/ArcForges.Mobile/** (the identity-only project: its csproj, packages.lock.json, the Android manifest with no permission and no launchable activity, and only the compile-only sources the identity build and the generated-client compatibility evidence need; no runtime behaviour, because AND.40 owns the app); Mobile:docs/releasing.md (the reinstall guidance from io.github.arcforges.mobile only); Mobile:docs/maui-toolchain.md (new: the pinned tuple, the integrity pins and the identity-build evidence); Mobile:docs/licence-boundary.md (the Contracts NuGet admission entry and the MAUI-closure licence notes only); Mobile:eng/maui_identity.py (new identity, tuple and admission gate) and Mobile:eng/tests/test_maui_identity.py (its offline tests); Mobile:eng/mobile.py (wire the identity gate, and the exact-path final-newline exemption of the identity project lock, only); Mobile:eng/licences.py (extend the existing licence audit to the identity project csproj only); Mobile:.gitignore (bin/ and obj/ of the identity project only)
Shared resources (follow the owner protocol): RES-mobile-build-config (append): AND.01 pins the candidate .NET tuple (global.json, Directory.Build.props, Directory.Packages.props, NuGet.config and the identity project) and appends to this resource. AND.40 holds the exclusive lease `leases/res-mobile-build-config` for the Gradle-to-.NET restructure of the solution, lock files and policy data; AND.02 then registers the .NET project set under the same exclusive lease. Later tasks edit only their own project, append package versions to Directory.Packages.props, and regenerate packages.lock.json after rebase; dependency additions carry admission receipts.
Unblocks: AND.02, AND.04, AND.22, AND.40

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Windows full build of the identity-only project with locked restore (packages.lock.json content hashes), NuGet audit and dependency-verification check, and the same Linux full build in the hosted Linux CI job that AND.40 adds (P2-024 limitation: the local WSL2 Debian distribution has no JDK or Android SDK and installing them needs the user; owner AND.40, trigger its Linux CI job; AND.01 is not complete before that Linux build passes); F-023-class licence and provenance closure re-run for the pinned MAUI closure; package-identity and certificate inspection of the built manifest under P2-017. The MAUI app release build and its Mono AOT, trimming, R8 and 16 KB checks are an explicit transfer to AND.40 (CI) and PRF.12 (candidate proof), so the Windows and Linux build acceptance is not narrowed here; device install and App Link fixture-key tests are local opt-in, not CI gates.
Completion evidence for the ledger: Exact pinned tuple in global.json, Directory.Packages.props and packages.lock.json; SDK and workload integrity pins (exact SDK version with rollForward pinned, exact workload manifest versions, packages.lock.json content hashes in place of the former Gradle wrapper checksum); admission records for each new NuGet or workload dependency; built manifest showing applicationId com.arcforges.mobile; reinstall guidance recorded in docs/releasing.md; F-023 re-run showing the closure holds for the MAUI dependency set (the android-0.1.0-ci.14.1 closure does not carry over and reopens on this dependency change); no AGPL DesktopPlatform package in the closure.
Notes: Must also decide the KMP shared/ preview module's fate: arch-27's module map (core/*, feature/*) has no KMP target, so shared/ stays a dev-only convenience outside the shipped app graph, never a second production plan (per WP30 §4). Planning repair 2026-10-08 (DLV-34; P2-021): Kotlin/AGP/Compose/Gradle tuple replaced by the .NET 10 LTS SDK, Android workload and NuGet candidate pins (P2-021.3); applicationId decision taken from P2-021.3 and IRD-23 (com.arcforges.mobile, reinstall from io.github.arcforges.mobile documented in docs/releasing.md with no data migration). Source packages are adopted as well as applicationId and namespace. Identity-only Windows and Linux build acceptance restored; the MAUI release-build proof transfers explicitly to AND.40 (CI) and PRF.12 (device proof). Start edge on the superseded PRF.10 removed; the exact-tuple proof is a completion edge on PRF.12, not a start gate. Dropped on purpose: the optional development preview in the KMP shared/ module (desktopMain, labelled development-only; AGENTS.md:3) retires with the Kotlin/KMP modules under AND.40, with no replacement preview; the development-only status is restated in AND.22. No acceptance removed. Planning repair 2026-10-08 (DLV-34; coordinator adjudication, brief section 10): the write scope is completed with the paths the outcome already requires (docs/releasing.md for the reinstall guidance; the identity-only project sources, manifest and lock; the identity gate and its tests; the toolchain and licence documentation; the bin/obj ignore). The identity project carries no runtime behaviour: no permission, no launchable activity, only compile-only sources. First-party Contracts packages are admitted only from a candidate published from a commit on the current Contracts main (Contracts main 330e46bd, which the 2026-10-07 baseline rollback kept, published 1.0.0-ci.324.1 on 2026-10-05); 1.0.0-ci.350.1 was published from rolled-back commit 74c298c9 and is not admitted. No obligation or acceptance changes.
```

```text
Execute ArcForges delivery task AND.02 — Real MAUI module graph and AN01-AN28 route/state contracts.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\android.md (anchor task-and-02).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Mobile (integration owner: Mobile integration owner, the holder of roles/integration-mobile).
Claim and handoff record: claims/and-02 (python tools/delivery.py claim AND.02 --worker <name>); task branch task/and-02 in Mobile; ledger record ledger/tasks/and-02.md.
Kind/size: producer/L. Baseline: not-started.
Outcome: The arch-27 module set (app, core/domain, core/data, core/network, core/security, core/designsystem, feature/home, feature/chat, feature/tasks, feature/library, feature/scope, feature/settings) exists as enforced .NET projects, every one targeting net10.0-android only (P2-021.3): the app is the MAUI project; the domain and feature projects are platform-neutral in code (no Android or platform API reference, enforced by architecture tests) and carry the same single target. Typed AN01-AN28 Shell/navigation and state contracts exist, and features depend only on typed core ports. No iOS, Mac Catalyst, macOS or other platform target exists.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-30.01 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\30-mobile-shared-architecture.md, anchor rule-wp-30.01

Entry condition: adoption slice ADOPT.10.android is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] AND.01: renamed applicationId/namespace and pinned toolchain
- [artifact] AND.40: the MAUI app project, Hello transport and CI created by AND.40
- [artifact] PRF.12: the MAUI Android release proof of the candidate app, Hello transport and release pipeline on the device or emulator
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Mobile:src/ArcForges.Mobile/**; Mobile:src/core/ArcForges.Mobile.Domain/**; Mobile:src/core/ArcForges.Mobile.Data/**; Mobile:src/core/ArcForges.Mobile.Network/**; Mobile:src/core/ArcForges.Mobile.Security/**; Mobile:src/core/ArcForges.Mobile.DesignSystem/**; Mobile:src/features/ArcForges.Mobile.Home/**; Mobile:src/features/ArcForges.Mobile.Chat/**; Mobile:src/features/ArcForges.Mobile.Tasks/**; Mobile:src/features/ArcForges.Mobile.Library/**; Mobile:src/features/ArcForges.Mobile.Scope/**; Mobile:src/features/ArcForges.Mobile.Settings/**; Mobile:ArcForges.Mobile.slnx; Mobile:tests/ArcForges.Mobile.Tests/**
Shared resources (follow the owner protocol): RES-mobile-build-config (exclusive): AND.01 pins the candidate .NET tuple (global.json, Directory.Build.props, Directory.Packages.props, NuGet.config and the identity project) and appends to this resource. AND.40 holds the exclusive lease `leases/res-mobile-build-config` for the Gradle-to-.NET restructure of the solution, lock files and policy data; AND.02 then registers the .NET project set under the same exclusive lease. Later tasks edit only their own project, append package versions to Directory.Packages.props, and regenerate packages.lock.json after rebase; dependency additions carry admission receipts.
Unblocks: AND.03, AND.04, AND.05, AND.20

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Architecture and import-boundary tests (no React Native, iOS, macOS or AGPL package references, no cross-module leakage, one-way core<-feature<-app) as offline xUnit architecture tests run in CI; targeted offline unit tests per project.
Completion evidence for the ledger: Project reference graph report showing one-way core<-feature<-app dependencies; route ID inventory matching AN01-AN28; zero iOS or macOS target frameworks.
Notes: Planning repair 2026-10-08 (DLV-34; P2-021): arch-27 Gradle module set becomes .NET project set with the same one-way rule; KMP shared/ dev module retires with AND.40. Acceptance unchanged.
```

```text
Execute ArcForges delivery task AND.03 — Android runtime and OS adapters (MAUI, Credential Manager, Keystore wrapper, WorkManager, FCM registration, SAF/MediaStore).

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\android.md (anchor task-and-03).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Mobile (integration owner: Mobile integration owner, the holder of roles/integration-mobile).
Claim and handoff record: claims/and-03 (python tools/delivery.py claim AND.03 --worker <name>); task branch task/and-03 in Mobile; ledger record ledger/tasks/and-03.md.
Kind/size: feature/L. Baseline: not-started.
Outcome: arm64 release and x64 emulator adapters for Credential Manager/passkey fallback, Keystore, WorkManager, FCM with non-GMS fallback, and SAF/MediaStore/FileProvider exist in ArcForges.Mobile.Security, ArcForges.Mobile.Data and ArcForges.Mobile.Network, bound through admitted .NET for Android (AndroidX and Google/OS) bindings, with no unsafe fallback path.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-30.02 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\30-mobile-shared-architecture.md, anchor rule-wp-30.02

Entry condition: adoption slice ADOPT.10.android is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] AND.02: core/security, core/data, core/network module shells
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Mobile:src/core/ArcForges.Mobile.Security/**; Mobile:src/core/ArcForges.Mobile.Data/**; Mobile:src/core/ArcForges.Mobile.Network/**; Mobile:tests/ArcForges.Mobile.Tests/**
Shared resources (follow the owner protocol): RES-mobile-build-config (append): AND.01 pins the candidate .NET tuple (global.json, Directory.Build.props, Directory.Packages.props, NuGet.config and the identity project) and appends to this resource. AND.40 holds the exclusive lease `leases/res-mobile-build-config` for the Gradle-to-.NET restructure of the solution, lock files and policy data; AND.02 then registers the .NET project set under the same exclusive lease. Later tasks edit only their own project, append package versions to Directory.Packages.props, and regenerate packages.lock.json after rebase; dependency additions carry admission receipts.
Unblocks: AND.06, AND.07, AND.08, AND.12

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Targeted offline xUnit tests for adapter contracts in CI; install-on-real-device, permission-refusal, process-death and missing-Play-services scenarios are local opt-in under P2-017, not CI.
Completion evidence for the ledger: Adapter test matrix (permission refusal, process death, missing Play services, callback after account switch) with device identity recorded for local runs
Notes: Can proceed in parallel with AND.04 (core/network gRPC client) and AND.05 (Room, core/data) once AND.02's skeleton lands; they touch different files within shared modules so should be sequenced as short-lived parallel PRs, not serialized. Planning repair 2026-10-08 (DLV-34; P2-021): Compose and Kotlin references replaced by MAUI and .NET Android bindings (admitted per binding); paths moved to the C# projects; the xUnit adapter tests land in tests/ArcForges.Mobile.Tests, which is added to writes. Acceptance unchanged.
```

```text
Execute ArcForges delivery task AND.04 — Published gRPC-Web contract consumption (Grpc.Net.Client.Web C# client from the NuGet Contracts packages, binary framing, session/stream/retry adapters).

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\android.md (anchor task-and-04).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Mobile (integration owner: Mobile integration owner, the holder of roles/integration-mobile).
Claim and handoff record: claims/and-04 (python tools/delivery.py claim AND.04 --worker <name>); task branch task/and-04 in Mobile; ledger record ledger/tasks/and-04.md.
Kind/size: feature/M. Baseline: not-started.
Outcome: ArcForges.Mobile.Network wraps the NuGet Contracts client surface behind typed session/stream/retry/exact-value adapters, explicitly selecting binary gRPC-Web through Grpc.Net.Client.Web; the observed GrpcWebMode and server-stream media type are recorded by PRF.12 together with the fallback decision. Exact values stay exact: int64 and uint64 use C# long and ulong, decimal values use decimal, and no value passes through floating point.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-30.03 (full contract consumption through the NuGet Grpc.Net.Client.Web client (Connect-Kotlin client retired)): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\30-mobile-shared-architecture.md, anchor rule-wp-30.03
- WP-30.00 (MAUI real package consumption of the NuGet Contracts clients): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\30-mobile-shared-architecture.md, anchor rule-wp-30.00

Entry condition: adoption slice ADOPT.10.android is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] AND.02: core/network module shell
- [contract] CON.07: the NuGet Contracts packages (ArcForges.Contracts.PublicApi and the Contracts generated C# client surface) for identity, session and native-auth types
- [contract] CON.11: the generated C# ApplicationService, HistoryService and EventService clients in the NuGet Contracts packages
- [artifact] AND.01: delivered AND.01 identity and candidate .NET MAUI toolchain pins (the exact tuple is proven by PRF.12 before AND.01 completes)
- [artifact] AND.40: the MAUI Hello transport and streaming consumer rules built by AND.40
Completion prerequisites (may start earlier; cannot complete before these are complete):
- [integration] CLOUD.21: publicly deployed Cloud host serving the generated business RPC surface

Permitted write scope: Mobile:src/core/ArcForges.Mobile.Network/**; Mobile:tests/ArcForges.Mobile.Tests/**
Shared resources (follow the owner protocol): RES-mobile-build-config (append): AND.01 pins the candidate .NET tuple (global.json, Directory.Build.props, Directory.Packages.props, NuGet.config and the identity project) and appends to this resource. AND.40 holds the exclusive lease `leases/res-mobile-build-config` for the Gradle-to-.NET restructure of the solution, lock files and policy data; AND.02 then registers the .NET project set under the same exclusive lease. Later tasks edit only their own project, append package versions to Directory.Packages.props, and regenerate packages.lock.json after rebase; dependency additions carry admission receipts.
Unblocks: AND.07, AND.08, AND.09, AND.10, AND.11, AND.12

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Targeted offline xUnit codec and adapter tests in CI (binary framing, exact int64/uint64/decimal values, grpc-timeout header format, no cookies, no redirects, no connection retry); real device or service calls against a deployed Cloud host are local opt-in evidence, not a CI gate (same pattern as the MAUI Hello client built by AND.40).
Completion evidence for the ledger: Real NuGet-package consumer and service/device call evidence with exact package versions, hashes and device identity.
Notes: Merged duplicate integration or closure task formerly proposed as CON.97. Planning repair 2026-10-08 (DLV-34; P2-021): Connect-Kotlin client replaced by Grpc.Net.Client.Web (C#, binary gRPC-Web selected explicitly). Maven edges replaced by NuGet Contracts edges. Open items on the NuGet streaming methods are recorded in PRF.12. Acceptance unchanged; exact-value rule stated explicitly.
```

```text
Execute ArcForges delivery task AND.05 — SQLite history, drafts, outbox and receipts (versioned migrations through an admitted Apache-2.0 SQLite binding).

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\android.md (anchor task-and-05).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Mobile (integration owner: Mobile integration owner, the holder of roles/integration-mobile).
Claim and handoff record: claims/and-05 (python tools/delivery.py claim AND.05 --worker <name>); task branch task/and-05 in Mobile; ledger record ledger/tasks/and-05.md.
Kind/size: feature/L. Baseline: not-started.
Outcome: SQLite schemas (local_schema, scope_partition, projection, draft, outbox, transfer, cursor, preferences), versioned with forward-only SQLite migrations through an admitted Apache-2.0 .NET SQLite binding, implement per-profile partitions with a durable, bounded, never-silently-evicted outbox; local canonical history is not evictable cache.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-30.04 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\30-mobile-shared-architecture.md, anchor rule-wp-30.04

Entry condition: adoption slice ADOPT.10.android is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] AND.02: core/data module shell
- [contract] CON.11: model-05-equivalent typed records for projections/receipts
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Mobile:src/core/ArcForges.Mobile.Data/**; Mobile:tests/ArcForges.Mobile.Tests/**
Shared resources (follow the owner protocol): RES-mobile-build-config (append): AND.01 pins the candidate .NET tuple (global.json, Directory.Build.props, Directory.Packages.props, NuGet.config and the identity project) and appends to this resource. AND.40 holds the exclusive lease `leases/res-mobile-build-config` for the Gradle-to-.NET restructure of the solution, lock files and policy data; AND.02 then registers the .NET project set under the same exclusive lease. Later tasks edit only their own project, append package versions to Directory.Packages.props, and regenerate packages.lock.json after rebase; dependency additions carry admission receipts.
Unblocks: AND.07, AND.08, AND.09, AND.10, AND.11

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline SQLite migration tests in CI: every schema version migrates forward; crash-recovery, capacity-refusal and atomic outbox writes run against a file-backed database; the SQLite binding is admitted under dependency admission with its licence and native-library provenance closure (Apache-2.0 required by P2-021.3). Instrumented runs on the emulator or a device are local opt-in under P2-017.
Completion evidence for the ledger: Migration test results for every schema version; outbox capacity-refusal and awaitingReconciliation replay tests; no silent eviction of draft or outbox rows.
Notes: Fully local; remote Task/AI content reconciled through this store may use named fixtures until WP31/52 per the producer matrix ("Task/AI fixture allowed only until 31+52"), but the store/journal/outbox mechanics themselves must be real now. Planning repair 2026-10-08 (DLV-34; P2-021): Room is replaced by SQLite with versioned migrations (the coordinator translation for the MAUI stack). The binding must be Apache-2.0 under P2-021.3 and is admitted by dependency admission; if no Apache-2.0 SQLite binding is admitted, the AndroidX Room binding is the fallback and needs a coordinator decision (openQuestions). Durability, bounds and no-eviction rules unchanged.
```

```text
Execute ArcForges delivery task AND.06 — Secure per-account lifecycle: Keystore encryption, no-backup policy, purge/quarantine, deep-link validation.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\android.md (anchor task-and-06).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Mobile (integration owner: Mobile integration owner, the holder of roles/integration-mobile).
Claim and handoff record: claims/and-06 (python tools/delivery.py claim AND.06 --worker <name>); task branch task/and-06 in Mobile; ledger record ledger/tasks/and-06.md.
Kind/size: feature/M. Baseline: not-started.
Outcome: Per-account Keystore-encrypted secret and pending-store policy (Android Keystore through the .NET binding), session, logout and revoke purge vs unsent-work quarantine or export, same-generation deep-link validation and current-foreground consent are implemented in ArcForges.Mobile.Security. Reinstall path: the io.github.arcforges.mobile development prerelease (Kotlin-era Keystore data) has no MAUI migration helper and holds no production user data, so the path to com.arcforges.mobile is reinstall guidance in docs/releasing.md with no data migration. Upgrades within com.arcforges.mobile keep the migration, quarantine and retention rules of AND.21, including no pending user work lost.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-30.05 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\30-mobile-shared-architecture.md, anchor rule-wp-30.05

Entry condition: adoption slice ADOPT.10.android is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] AND.03: Keystore/Credential Manager adapter wrapper
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Mobile:src/core/ArcForges.Mobile.Security/**
Unblocks: AND.07, AND.08, AND.12

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline unit tests for encryption/purge/quarantine logic; device-restore-without-key, logout-while-requests-run, deep-link-spoof and secret-scan-of-release-logs are local opt-in under P2-017. The io.github reinstall guidance in docs/releasing.md (no data migration) is checked offline in CI by the AND.40 policy suite.
Completion evidence for the ledger: Secret scan of release logs/backup showing no credential leakage; device restore and logout-while-in-flight scenario results; the docs/releasing.md reinstall-guidance check result for io.github.arcforges.mobile (no data migration).
Notes: Planning repair 2026-10-08 (DLV-34; P2-021): Paths moved to ArcForges.Mobile.Security. The io.github reinstall guidance (no data migration; development prerelease, no production user data) is recorded by AND.40 in docs/releasing.md; see the outcome, validation and evidence. Acceptance otherwise unchanged.
```

```text
Execute ArcForges delivery task AND.07 — Foundation integration evidence: real candidate against deployed 22/23/24/25.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\android.md (anchor task-and-07).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Mobile (integration owner: Mobile integration owner, the holder of roles/integration-mobile).
Claim and handoff record: claims/and-07 (python tools/delivery.py claim AND.07 --worker <name>); task branch task/and-07 in Mobile; ledger record ledger/tasks/and-07.md.
Kind/size: integration/M. Baseline: not-started.
Outcome: A candidate APK is built, installed clean and exercises real sign-in/hydration/upload/reconnect on a physical device against actually deployed Cloud identity/API/realtime/sync; any Task/AI fixtures still present are named and confirmed compiled out of production before WP31.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-30.90 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\30-mobile-shared-architecture.md, anchor rule-wp-30.90
- WP-23.05 (Android real-consumer integration beyond the WP-06 probe): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\23-public-api-and-generated-clients.md, anchor rule-wp-23.05

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
- [artifact] CLOUD.26: real, delivered outcome of CLOUD.26 (generated NuGet C# clients against Identity/Workspace/Device)
- [artifact] CLOUD.29: real, delivered outcome of CLOUD.29 (Stream connection and authentication (EventService.Watch/ExecutionService.WatchOutput shells))
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Mobile:src/ArcForges.Mobile/**
Unblocks: AND.08, AND.09, AND.10, AND.11, AND.12, CLOUD.28

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Clean-cache restore/build/install on a real device is local opt-in evidence per P2-017; CI only runs the offline/static portion
Completion evidence for the ledger: Owned-artifact-and-real-integration receipt: source commit, producer versions, candidate hashes, actual device identity, scenario, result, real-vs-fixture status per field
Notes: Merged duplicate integration or closure task formerly proposed as CLOUD.60. Planning repair 2026-10-08 (DLV-34; P2-021): Writes moved to the MAUI app project; the Kotlin candidate becomes a MAUI candidate under AND.40. Real-device and fixture-retirement acceptance unchanged.
```

```text
Execute ArcForges delivery task AND.08 — Authentication, Home and workspace (AN01-AN06).

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\android.md (anchor task-and-08).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Mobile (integration owner: Mobile integration owner, the holder of roles/integration-mobile).
Claim and handoff record: claims/and-08 (python tools/delivery.py claim AND.08 --worker <name>); task branch task/and-08 in Mobile; ledger record ledger/tasks/and-08.md.
Kind/size: feature/L. Baseline: not-started.
Outcome: System authentication, five-destination navigation and per-device application selection are complete with real Cloud identity/presence and explicit history disclosure.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-31.00 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\31-arcchat-mobile-android.md, anchor rule-wp-31.00

Entry condition: adoption slice ADOPT.10.android is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] AND.03: the real Android foundation module AND.03 this feature is built on
- [artifact] AND.04: the real Android foundation module AND.04 this feature is built on
- [artifact] AND.05: the real Android foundation module AND.05 this feature is built on
- [artifact] AND.06: the real Android foundation module AND.06 this feature is built on
Completion prerequisites (may start earlier; cannot complete before these are complete):
- [integration] AND.07: foundation candidate proven against the deployed Cloud services
- [integration] AND.13: the UI-level suite (five-destination Shell navigation, back and state restore, UI assertions) in the net10.0-android device test project

Permitted write scope: Mobile:src/features/ArcForges.Mobile.Home/**; Mobile:src/ArcForges.Mobile/**; Mobile:tests/ArcForges.Mobile.Tests/**
Unblocks: AND.13, AND.14, AND.15, AND.19

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline xUnit view-model and Shell navigation tests in CI where feasible; the UI-level suite the instrumented tests covered (five-destination Shell navigation, back and state restore, UI assertions) runs in the net10.0-android device test project owned by AND.13 as local opt-in under P2-017; scope/permission, wrong or stale target, loss/retry and expiry scenarios against real WP22/23 are local opt-in.
Completion evidence for the ledger: Full account/attention path walkthrough against real Cloud endpoints
Notes: Does not need WP26 (remote bridge), WP45 (push sender) or WP52 (Harness) to start or complete — only WP30's own foundation and the already-deployed WP22/23. Demonstrates that not all Android features wait on the complete Harness. Planning repair 2026-10-08 (DLV-34; P2-021): Five-destination navigation is MAUI Shell instead of Compose navigation. Instrumented UI tests become offline view-model and Shell navigation tests in tests/ArcForges.Mobile.Tests (added to writes) where feasible, and the UI-level suite moves to the AND.13 net10.0-android device test project. AND.08 completes on AND.13 (typed edge), so no UI-level coverage is removed. Acceptance unchanged.
```

```text
Execute ArcForges delivery task AND.09 — Conversations and context (AN07-AN10/15/16).

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\android.md (anchor task-and-09).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Mobile (integration owner: Mobile integration owner, the holder of roles/integration-mobile).
Claim and handoff record: claims/and-09 (python tools/delivery.py claim AND.09 --worker <name>); task branch task/and-09 in Mobile; ledger record ledger/tasks/and-09.md.
Kind/size: feature/L. Baseline: not-started.
Outcome: Native composer/IME/branch/context, history modes/promotion and real binary output streams work end-to-end for own-application scope, with no desktop local-history access.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-31.01 (all work except the parts mapped to AND.24): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\31-arcchat-mobile-android.md, anchor rule-wp-31.01

Entry condition: adoption slice ADOPT.10.android is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] AND.04: the real Android foundation module AND.04 this feature is built on
- [artifact] AND.05: the real Android foundation module AND.05 this feature is built on
Completion prerequisites (may start earlier; cannot complete before these are complete):
- [integration] AND.24: real CF Harness admission/generation/tool loop
- [integration] AND.07: foundation candidate proven against the deployed Cloud services

Permitted write scope: Mobile:src/features/ArcForges.Mobile.Chat/**
Permitted substitutes (never real integration evidence): SUB-fixture-turn-endpoint: client-side session/event/output/upload handling, typed state transitions, reconnection -- runs no model/planner/admission/metering itself Real producer ['HAR.00', 'HAR.02', 'HAR.03']; removed by HAR.05
Unblocks: AND.13, AND.14, AND.15, AND.19, AND.24

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline stream-codec/cursor unit tests; real-device streaming/reconnect scenarios against the deployed (fixture-backed until WP52.05) endpoint are local opt-in
Completion evidence for the ledger: History/pending-input/stream/final-message consistency under every declared recovery outcome
Notes: Planning repair 2026-10-08 (DLV-34; P2-021): Composer, IME and stream surfaces become MAUI controls on the same stream and cursor semantics; writes moved to the C# feature project. Acceptance unchanged.
```

```text
Execute ArcForges delivery task AND.10 — Tasks, approvals and automation (AN11-AN13/19/25).

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\android.md (anchor task-and-10).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Mobile (integration owner: Mobile integration owner, the holder of roles/integration-mobile).
Claim and handoff record: claims/and-10 (python tools/delivery.py claim AND.10 --worker <name>); task branch task/and-10 in Mobile; ledger record ledger/tasks/and-10.md.
Kind/size: feature/L. Baseline: not-started.
Outcome: Task/approval/automation surfaces enforce action, risk, credit-consent and consumption-only rules with one real owner outcome/settlement per command.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-31.02 (all work except the parts mapped to AND.24, AND.25): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\31-arcchat-mobile-android.md, anchor rule-wp-31.02

Entry condition: adoption slice ADOPT.10.android is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] AND.04: the real Android foundation module AND.04 this feature is built on
- [artifact] AND.05: the real Android foundation module AND.05 this feature is built on
Completion prerequisites (may start earlier; cannot complete before these are complete):
- [integration] AND.25: real device bridge with lease/current-grant/unknown-effect reconciliation
- [integration] AND.24: real Harness planning/tool-proposal loop
- [integration] AND.07: foundation candidate proven against the deployed Cloud services

Permitted write scope: Mobile:src/features/ArcForges.Mobile.Tasks/**
Permitted substitutes (never real integration evidence): SUB-automation-fixture: client rendering of schedule/timezone/target/budget and action availability, offline-draft handling only Real producer ['HAR.06']; removed by HAR.06
Unblocks: AND.13, AND.14, AND.15, AND.19, AND.24, AND.25

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline idempotency/state-machine unit tests; real bridge/Harness/commerce scenarios are local opt-in against deployed services
Completion evidence for the ledger: One real owner outcome/settlement per command; no broad implicit grant or hidden background write
Notes: Planning repair 2026-10-08 (DLV-34; P2-021): Task, approval and automation UI port to MAUI; idempotency state machine unchanged. Writes moved to the C# feature project. Acceptance unchanged.
```

```text
Execute ArcForges delivery task AND.11 — Library and resources (AN14-AN18/22).

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\android.md (anchor task-and-11).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Mobile (integration owner: Mobile integration owner, the holder of roles/integration-mobile).
Claim and handoff record: claims/and-11 (python tools/delivery.py claim AND.11 --worker <name>); task branch task/and-11 in Mobile; ledger record ledger/tasks/and-11.md.
Kind/size: feature/M. Baseline: not-started.
Outcome: Native preview/import/export/transfer flows handle missing/denied/unsupported states with correct local/cloud copy and deletion semantics.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-31.03 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\31-arcchat-mobile-android.md, anchor rule-wp-31.03

Entry condition: adoption slice ADOPT.10.android is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] AND.04: the real Android foundation module AND.04 this feature is built on
- [artifact] AND.05: the real Android foundation module AND.05 this feature is built on
Completion prerequisites (may start earlier; cannot complete before these are complete):
- [integration] AND.07: foundation candidate proven against the deployed Cloud services

Permitted write scope: Mobile:src/features/ArcForges.Mobile.Library/**
Unblocks: AND.13, AND.15, AND.19, AND.27

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline transfer-journal unit tests; resumable-upload/hash-mismatch/process-death-during-transfer scenarios are local opt-in on real devices
Completion evidence for the ledger: No unavailable bytes represented as empty success; resumable journal survives process death
Notes: Independent of WP26/WP45/WP52 — can complete in parallel with AND.09/AND.10 once the foundation (AND.07) lands. Planning repair 2026-10-08 (DLV-34; P2-021): Library preview, import, export and transfer flows port to MAUI with SAF/MediaStore equivalents. Writes moved to the C# feature project. Acceptance unchanged.
```

```text
Execute ArcForges delivery task AND.12 — Presence, push, links and settings (AN20-AN24).

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\android.md (anchor task-and-12).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Mobile (integration owner: Mobile integration owner, the holder of roles/integration-mobile).
Claim and handoff record: claims/and-12 (python tools/delivery.py claim AND.12 --worker <name>); task branch task/and-12 in Mobile; ledger record ledger/tasks/and-12.md.
Kind/size: feature/M. Baseline: not-started.
Outcome: Presence/push/deep-link/settings surfaces stay usable through declared polling/notification fallback, with no purchase/store billing surface and no exposure of a revoked resource on background reconnect.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-31.04 (all work except the parts mapped to AND.26): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\31-arcchat-mobile-android.md, anchor rule-wp-31.04
- WP-31:pg-24-completion-gate-paragraph-physical PG-24 completion-gate paragraph: physical arm64 push/Doze/background evidence (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\31-arcchat-mobile-android.md, package-level obligation

Entry condition: adoption slice ADOPT.10.android is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [contract] CON.22: published notification.registerPush and unregisterPush
- [artifact] AND.03: the real Android foundation module AND.03 this feature is built on
- [artifact] AND.04: the real Android foundation module AND.04 this feature is built on
- [artifact] AND.06: the real Android foundation module AND.06 this feature is built on
Completion prerequisites (may start earlier; cannot complete before these are complete):
- [integration] AND.26: live FCM sender adapter with a project-bound credential
- [integration] AND.07: foundation candidate proven against the deployed Cloud services

Permitted write scope: Mobile:src/features/ArcForges.Mobile.Settings/**; Mobile:src/core/ArcForges.Mobile.Network/**
Shared resources (follow the owner protocol): RES-mobile-build-config (append): AND.01 pins the candidate .NET tuple (global.json, Directory.Build.props, Directory.Packages.props, NuGet.config and the identity project) and appends to this resource. AND.40 holds the exclusive lease `leases/res-mobile-build-config` for the Gradle-to-.NET restructure of the solution, lock files and policy data; AND.02 then registers the .NET project set under the same exclusive lease. Later tasks edit only their own project, append package versions to Directory.Packages.props, and regenerate packages.lock.json after rebase; dependency additions carry admission receipts.
Unblocks: AND.13, AND.15, AND.19, AND.26

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline notification-dedup/registration unit tests; physical-device push receipt, Doze/background behavior and no-GMS fallback are local opt-in per PG-24
Completion evidence for the ledger: Physical device receipt of a real push; denied-permission and no-GMS durable-polling fallback observed
Notes: Planning repair 2026-10-08 (DLV-34; P2-021): Push registration uses the .NET Firebase binding and the no-GMS polling fallback is retained; writes moved to the C# projects. Acceptance unchanged.
```

```text
Execute ArcForges delivery task AND.13 — Native interaction and recovery: full experience-02 device matrix.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\android.md (anchor task-and-13).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Mobile (integration owner: Mobile integration owner, the holder of roles/integration-mobile).
Claim and handoff record: claims/and-13 (python tools/delivery.py claim AND.13 --worker <name>); task branch task/and-13 in Mobile; ledger record ledger/tasks/and-13.md.
Kind/size: integration/L. Baseline: not-started.
Outcome: The complete phone/tablet/back/IME/TalkBack/large-text/process-death/account-switch/denied-permission/no-GMS matrix from experience 02 passes against real services on a release APK, preserving typed effect uncertainty and drafts.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-31.05 (all work except the parts mapped to AND.25): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\31-arcchat-mobile-android.md, anchor rule-wp-31.05

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

Permitted write scope: Mobile:tests/ArcForges.Mobile.DeviceTests/**
Unblocks: AND.08, AND.15, AND.19, AND.25

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Physical low/mid-tier arm64 device matrix (1000 messages, 4 MiB answer, rotation, process kill during send/refresh/upload, denied push, airplane/reconnect, account switch, expired approval, revoked source) is local opt-in under P2-017
Completion evidence for the ledger: Per-scenario pass/fail with device identity and TalkBack/IME/large-text results
Notes: Planning repair 2026-10-08 (DLV-34; P2-021): The androidTest Kotlin matrix moves to a net10.0-android device test project (local opt-in). The matrix itself and TalkBack, IME and large-text criteria are unchanged.
```

```text
Execute ArcForges delivery task AND.14 — Scope and licence enforcement audit.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\android.md (anchor task-and-14).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Mobile (integration owner: Mobile integration owner, the holder of roles/integration-mobile).
Claim and handoff record: claims/and-14 (python tools/delivery.py claim AND.14 --worker <name>); task branch task/and-14 in Mobile; ledger record ledger/tasks/and-14.md.
Kind/size: acceptance/S. Baseline: not-started.
Outcome: Full companion requirements, consumption-only restrictions, public-NuGet-only imports, and absence of desktop secrets, device-local paths and excluded professional-editing surfaces are verified with complete provenance.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-31.06 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\31-arcchat-mobile-android.md, anchor rule-wp-31.06
- WP-30:3-binding-rules-apache-2-0-boundary-no-g §3 binding rules: Apache-2.0 boundary, no GPL-family implementation, immutable producer artifacts (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\30-mobile-shared-architecture.md, package-level obligation

Entry condition: adoption slice ADOPT.10.android is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] AND.08: features exist to audit
- [artifact] AND.09: features exist to audit
- [artifact] AND.10: features exist to audit
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Mobile:eng/policy/**; Mobile:eng/provenance/**
Shared resources (follow the owner protocol): RES-mobile-build-config (append): AND.01 pins the candidate .NET tuple (global.json, Directory.Build.props, Directory.Packages.props, NuGet.config and the identity project) and appends to this resource. AND.40 holds the exclusive lease `leases/res-mobile-build-config` for the Gradle-to-.NET restructure of the solution, lock files and policy data; AND.02 then registers the .NET project set under the same exclusive lease. Later tasks edit only their own project, append package versions to Directory.Packages.props, and regenerate packages.lock.json after rebase; dependency additions carry admission receipts.
Unblocks: AND.15

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Package content/dependency/privacy static checks plus full surface-action inventory cross-check, offline
Completion evidence for the ledger: Complete surface/action inventory cross-check with no unaccepted third-party provenance
Notes: Planning repair 2026-10-08 (DLV-34; P2-021): Gradle-based inventory becomes NuGet/MSBuild inventory; the public-Maven-only import criterion becomes public-NuGet-only. Acceptance unchanged.
```

```text
Execute ArcForges delivery task AND.15 — Complete companion acceptance.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\android.md (anchor task-and-15).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Mobile (integration owner: Mobile integration owner, the holder of roles/integration-mobile).
Claim and handoff record: claims/and-15 (python tools/delivery.py claim AND.15 --worker <name>); task branch task/and-15 in Mobile; ledger record ledger/tasks/and-15.md.
Kind/size: integration/M. Baseline: not-started.
Outcome: A signed candidate joins real 31.00-31.06 evidence with producer manifests and the full compatible 52/26/25/42/45 integration manifest, verified through injected-failure scenarios with exact device/OS/server/worker/package identities.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-31.90 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\31-arcchat-mobile-android.md, anchor rule-wp-31.90
- WP-31:pg-24-completion-gate-paragraph-physical PG-24 completion-gate paragraph: physical arm64 push/Doze/background evidence (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\31-arcchat-mobile-android.md, package-level obligation

Entry condition: adoption slice ADOPT.10.android is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] AND.08: all WP31 substep tasks complete
- [artifact] AND.09: all WP31 substep tasks complete
- [artifact] AND.10: all WP31 substep tasks complete
- [artifact] AND.11: all WP31 substep tasks complete
- [artifact] AND.12: all WP31 substep tasks complete
- [artifact] AND.13: all WP31 substep tasks complete
- [artifact] AND.14: all WP31 substep tasks complete
- [artifact] AND.27: package task delivered
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Mobile:src/ArcForges.Mobile/**
Unblocks: AND.16

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Full physical-device release scenarios and injected failure matrix, local opt-in under P2-017
Completion evidence for the ledger: Owned-artifact-and-real-integration receipt joining all producer manifests; distribution/store activation explicitly deferred to WP32
Notes: Planning repair 2026-10-08 (DLV-34; P2-021): Final join of the MAUI companion; writes moved to the MAUI app project. Acceptance unchanged.
```

```text
Execute ArcForges delivery task AND.16 — Signed Android release artifacts (AAB + direct APK).

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\android.md (anchor task-and-16).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Mobile (integration owner: Mobile integration owner, the holder of roles/integration-mobile).
Claim and handoff record: claims/and-16 (python tools/delivery.py claim AND.16 --worker <name>); task branch task/and-16 in Mobile; ledger record ledger/tasks/and-16.md.
Kind/size: release/S. Baseline: not-started.
Outcome: AAB (Play) and a separately signed direct APK build automatically from reviewed main as MAUI outputs, with monotonic versionCode within applicationId com.arcforges.mobile, immutable provenance and tested WP03 update-schema compatibility.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-32.00 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\32-mobile-release-and-store-gates.md, anchor rule-wp-32.00

Entry condition: adoption slice ADOPT.10.android is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] AND.15: companion acceptance complete
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Mobile:.github/workflows/ci.yml; Mobile:eng/mobile.py; Mobile:eng/published.py
Shared resources (follow the owner protocol): RES-android-signing-and-store (append): Used only by release tasks through protected CI environments; no task creates replacement keys or listings.
Unblocks: AND.17, AND.18, AND.21

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Actual signature/package/R8/runtime and version-monotonicity checks; clean device install/upgrade is local opt-in
Completion evidence for the ledger: Signed AAB and APK with recorded provenance; monotonic versionCode for com.arcforges.mobile; reinstall guidance from io.github.arcforges.mobile recorded in docs/releasing.md with no data migration.
Notes: Planning repair 2026-10-08 (DLV-34; P2-021): The signing pipeline and persistent certificate are kept. The upgrade check in eng/published.py is re-based on the com.arcforges.mobile identity; the io.github line stays immutable history. Acceptance unchanged.
```

```text
Execute ArcForges delivery task AND.17 — Release runtime inspection.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\android.md (anchor task-and-17).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Mobile (integration owner: Mobile integration owner, the holder of roles/integration-mobile).
Claim and handoff record: claims/and-17 (python tools/delivery.py claim AND.17 --worker <name>); task branch task/and-17 in Mobile; ledger record ledger/tasks/and-17.md.
Kind/size: acceptance/S. Baseline: not-started.
Outcome: Mono and ART runtime, the .NET for Android closure (no Kotlin, Compose or Connect-Kotlin residue), min and target API (26 and 37), arm64 assets with 16 KB alignment, trimming and R8 rules (AndroidLinkTool=r8), and required permissions are verified on the actual signed APK/AAB, not source inspection.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-32.01 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\32-mobile-release-and-store-gates.md, anchor rule-wp-32.01

Entry condition: adoption slice ADOPT.10.android is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] AND.16: signed candidate
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Mobile:eng/mobile.py
Unblocks: AND.23

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Install without development server/toolchain; startup/identity/RPC/notifications/lifecycle release tests are local opt-in
Completion evidence for the ledger: VG-07 evidence: real Mono and ART release artifact inspection, not debug-only or source-only proof.
Notes: Planning repair 2026-10-08 (DLV-34; P2-021): Kotlin/ART and Compose/grpc-lite inspection rewritten to the Mono/AOT and .NET closure with the same release checks (min/target API, arm64, R8, permissions, no debug-only proof). Rewording, not weakening.
```

```text
Execute ArcForges delivery task AND.18 — Dependency and source rights closure (final artifact).

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\android.md (anchor task-and-18).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Mobile (integration owner: Mobile integration owner, the holder of roles/integration-mobile).
Claim and handoff record: claims/and-18 (python tools/delivery.py claim AND.18 --worker <name>); task branch task/and-18 in Mobile; ledger record ledger/tasks/and-18.md.
Kind/size: acceptance/S. Baseline: not-started.
Outcome: Direct and transitive NuGet, MSBuild, workload, runtime and asset closure, licences, provenance and reproducible SBOM and NOTICE are audited against the final companion candidate, including F-023-class re-closure of the MAUI closure (the android-0.1.0-ci.14.1 closure does not carry over); public schema and tooling Apache origin and independently original app implementation are verified.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-32.02 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\32-mobile-release-and-store-gates.md, anchor rule-wp-32.02

Entry condition: adoption slice ADOPT.10.android is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] AND.16: signed candidate
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Mobile:eng/policy/**; Mobile:eng/provenance/**; Mobile:third-party/**
Shared resources (follow the owner protocol): RES-mobile-build-config (append): AND.01 pins the candidate .NET tuple (global.json, Directory.Build.props, Directory.Packages.props, NuGet.config and the identity project) and appends to this resource. AND.40 holds the exclusive lease `leases/res-mobile-build-config` for the Gradle-to-.NET restructure of the solution, lock files and policy data; AND.02 then registers the .NET project set under the same exclusive lease. Later tasks edit only their own project, append package versions to Directory.Packages.props, and regenerate packages.lock.json after rebase; dependency additions carry admission receipts.
Unblocks: AND.23

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Forbidden-licence fixture, unpinned or dynamic dependency and changed-checksum rejection tests, plus a fixture that rejects any AGPL DesktopPlatform package in the app closure and any PDF parser or renderer package (PDFium or a PDF rendering binding) under P2-022; offline.
Completion evidence for the ledger: F-023 re-closure for the final MAUI companion candidate (NuGet and MSBuild binary inventory matches the candidate; the closure reopened by the dependency change and is re-proven).
Notes: Planning repair 2026-10-08 (DLV-34; P2-021): Gradle and plugin closure becomes NuGet/MSBuild closure; the AGPL exclusion (P2-021.3) is an explicit fixture, and the PDF parser and renderer exclusion (P2-022) is added to the same fixture. Acceptance unchanged.
```

```text
Execute ArcForges delivery task AND.19 — Consumption-only enforcement.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\android.md (anchor task-and-19).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Mobile (integration owner: Mobile integration owner, the holder of roles/integration-mobile).
Claim and handoff record: claims/and-19 (python tools/delivery.py claim AND.19 --worker <name>); task branch task/and-19 in Mobile; ledger record ledger/tasks/and-19.md.
Kind/size: acceptance/M. Baseline: not-started.
Outcome: Absence of purchase buttons/embedded checkout/store billing/external purchase CTAs/licence-key unlock is enforced by static route/dependency checks and exercised across every state including expired subscription and exhausted credits.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-32.03 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\32-mobile-release-and-store-gates.md, anchor rule-wp-32.03

Entry condition: adoption slice ADOPT.10.android is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] AND.08: every authentication and Home state to audit
- [artifact] AND.09: every conversation state to audit
- [artifact] AND.10: every task, approval and automation state to audit
- [artifact] AND.11: every library and resource state to audit
- [artifact] AND.12: every presence, push, link and settings state to audit
Completion prerequisites (may start earlier; cannot complete before these are complete):
- [integration] AND.13: the rendered-state UX tests run in the net10.0-android device test project

Permitted write scope: Mobile:eng/policy/**; Mobile:tests/ArcForges.Mobile.Tests/**
Unblocks: AND.23

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Static route and dependency checks (MC-01..MC-06 build-time and CI assertions, as C# analyzers or xUnit architecture tests) plus all-state UX tests, offline where feasible; UX states that need a rendered MAUI page run in the AND.13 device test project as local opt-in.
Completion evidence for the ledger: VG-13 evidence: no build path can display a purchase CTA or accept a licence key
Notes: Planning repair 2026-10-08 (DLV-34; P2-021): Static checks move from Gradle to C# analyzers or architecture tests in tests/ArcForges.Mobile.Tests (added to writes); rendered-state UX tests run in the AND.13 device test project, and AND.19 completes on AND.13 (typed edge). Acceptance unchanged.
```

```text
Execute ArcForges delivery task AND.20 — Play and direct-channel signed update client.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\android.md (anchor task-and-20).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Mobile (integration owner: Mobile integration owner, the holder of roles/integration-mobile).
Claim and handoff record: claims/and-20 (python tools/delivery.py claim AND.20 --worker <name>); task branch task/and-20 in Mobile; ledger record ledger/tasks/and-20.md.
Kind/size: feature/M. Baseline: not-started.
Outcome: arch-11 channel behavior and a notify-only signed update client are complete, consuming WP03's format/fixture keys now; channel-switch export/reinstall guidance is explicit.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-32.04 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\32-mobile-release-and-store-gates.md, anchor rule-wp-32.04

Entry condition: adoption slice ADOPT.10.android is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [contract] CON.16: android-update.v1 feed format and fixture signing keys
- [artifact] AND.02: registered core/network and feature/settings module shells from android-module-boundaries
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Mobile:src/core/ArcForges.Mobile.Network/**; Mobile:src/features/ArcForges.Mobile.Settings/**
Shared resources (follow the owner protocol): RES-mobile-build-config (append): AND.01 pins the candidate .NET tuple (global.json, Directory.Build.props, Directory.Packages.props, NuGet.config and the identity project) and appends to this resource. AND.40 holds the exclusive lease `leases/res-mobile-build-config` for the Gradle-to-.NET restructure of the solution, lock files and policy data; AND.02 then registers the .NET project set under the same exclusive lease. Later tasks edit only their own project, append package versions to Directory.Packages.props, and regenerate packages.lock.json after rebase; dependency additions carry admission receipts.
Unblocks: AND.23

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Expired/rollback/wrong-certificate/URL/hash and offline-stale-feed tests, offline where feasible
Completion evidence for the ledger: Play primary + direct APK flow complete with no silent install
Notes: Explicitly does NOT wait on WP53 (production feed/signing) — WP-32.04's own text states WP53's replacement is verified at WP50, not a backward input to this task. Planning repair 2026-10-08 (DLV-34; P2-021): Notify-only update client ported to C# on the same android-update.v1 feed rules. Writes moved to the C# projects. Acceptance unchanged.
```

```text
Execute ArcForges delivery task AND.21 — Physical device and recovery gates.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\android.md (anchor task-and-21).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Mobile (integration owner: Mobile integration owner, the holder of roles/integration-mobile).
Claim and handoff record: claims/and-21 (python tools/delivery.py claim AND.21 --worker <name>); task branch task/and-21 in Mobile; ledger record ledger/tasks/and-21.md.
Kind/size: integration/L. Baseline: not-started.
Outcome: Full companion runs on minimum-supported and current physical-device profiles across weak/offline network, permission denial, no-GMS, key-loss/backup-restore, process kill and OS background limits; forward-rescue release with a higher versionCode is proven (Android never downgrades as routine rollback).

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-32.05 (all work except the parts mapped to AND.26): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\32-mobile-release-and-store-gates.md, anchor rule-wp-32.05

Entry condition: adoption slice ADOPT.10.android is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] AND.16: signed candidate
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Mobile:eng/mobile.py
Unblocks: AND.23, AND.26

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Actual local/server unknown-effect replay, encrypted draft/outbox retention through upgrade, signing-key recovery rehearsal — all local opt-in under P2-017
Completion evidence for the ledger: All mandatory scenarios pass; material device limits disclosed; no pending user work lost
Notes: Planning repair 2026-10-08 (DLV-34; P2-021): Device and recovery gates unchanged; they run against the MAUI signed candidate instead of the Kotlin candidate.
```

```text
Execute ArcForges delivery task AND.22 — Android scope statement.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\android.md (anchor task-and-22).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Mobile (integration owner: Mobile integration owner, the holder of roles/integration-mobile).
Claim and handoff record: claims/and-22 (python tools/delivery.py claim AND.22 --worker <name>); task branch task/and-22 in Mobile; ledger record ledger/tasks/and-22.md.
Kind/size: acceptance/S. Baseline: not-started.
Outcome: Documentation and store/release/readme/platform matrices state Android-only scope; iOS/Swift/KMP/cross-platform UI are recorded as outside this delivery with no false retained-iOS claim.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-32.06 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\32-mobile-release-and-store-gates.md, anchor rule-wp-32.06

Entry condition: adoption slice ADOPT.10.android is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] AND.01: the AND.01 Mobile documentation (docs/releasing.md reinstall guidance, docs/maui-toolchain.md, docs/licence-boundary.md) merged
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Mobile:README.md; Mobile:docs/**
Unblocks: AND.23

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Store/release/readme/platform matrix cross-check against the signed Android artifact, offline
Completion evidence for the ledger: No false retained-iOS deliverable or unsupported platform claim
Notes: Small and independent; can land in the same PR series as AND.18 or AND.19 for convenience without being merged into them as one task. Planning repair 2026-10-08 (DLV-34; P2-021): Successor AND.40 retires the Kotlin wording in README.md and docs (README KMP row, docs/development.md, docs/releasing.md). The development-only desktop preview in shared/ (desktopMain; AGENTS.md:3 forbids any desktop product) retires with the KMP module. The AND.40 README and AGENTS.md restate the Android-only scope, the no-desktop, no-iOS and no-macOS product statement, and the development-only qualifier for any local tooling; none of these is dropped. Planning repair 2026-10-08 (DLV-34; coordinator adjudication, brief section 10): start edge on AND.01 orders the shared Mobile docs writes.
```

```text
Execute ArcForges delivery task AND.23 — Distribution acceptance.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\android.md (anchor task-and-23).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Mobile (integration owner: Mobile integration owner, the holder of roles/integration-mobile).
Claim and handoff record: claims/and-23 (python tools/delivery.py claim AND.23 --worker <name>); task branch task/and-23 in Mobile; ledger record ledger/tasks/and-23.md.
Kind/size: release/M. Baseline: not-started.
Outcome: The exact signed APK/AAB, manifest/hash/versionCode/certificate identity, compatible server/Contracts release and all gate receipts are archived and published through the automatic main graph; a clean-device download verifies signature/hash and exercises actual services.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-32.90 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\32-mobile-release-and-store-gates.md, anchor rule-wp-32.90
- WP-32:pg-24-completion-gate-paragraph-recheck PG-24 completion-gate paragraph (recheck on distributed artifact) (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\32-mobile-release-and-store-gates.md, package-level obligation

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
Notes: Planning repair 2026-10-08 (DLV-34; P2-021): Distribution receipts bind to the MAUI signed APK and AAB (com.arcforges.mobile). Acceptance unchanged.
```

```text
Execute ArcForges delivery task AND.24 — Real CF Harness generation/tool loop observed end to end on Android.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\android.md (anchor task-and-24).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Mobile (integration owner: Mobile integration owner, the holder of roles/integration-mobile).
Claim and handoff record: claims/and-24 (python tools/delivery.py claim AND.24 --worker <name>); task branch task/and-24 in Mobile; ledger record ledger/tasks/and-24.md.
Kind/size: integration/M. Baseline: not-started.
Outcome: real admitted generation, tool proposal and automation execution replace the contract-bound fixture turn endpoint on a physical device

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-31.01 (real-integration closure): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\31-arcchat-mobile-android.md, anchor rule-wp-31.01
- WP-31.02 (real-integration closure): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\31-arcchat-mobile-android.md, anchor rule-wp-31.02

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
Notes: Planning repair 2026-10-08 (DLV-34; P2-021): Real Harness integration unchanged; the Android client is the MAUI app. Start edges to AI-lane tasks are re-homed to Cloud under P2-021.5, not renumbered here.
```

```text
Execute ArcForges delivery task AND.25 — Real desktop tool dispatch and unknown-effect reconciliation from Android.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\android.md (anchor task-and-25).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Mobile (integration owner: Mobile integration owner, the holder of roles/integration-mobile).
Claim and handoff record: claims/and-25 (python tools/delivery.py claim AND.25 --worker <name>); task branch task/and-25 in Mobile; ledger record ledger/tasks/and-25.md.
Kind/size: integration/M. Baseline: not-started.
Outcome: an Android-initiated remote task actually reaches a desktop through the durable bridge with correct lease/grant/reconciliation semantics

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-31.02 (device-dispatch closure): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\31-arcchat-mobile-android.md, anchor rule-wp-31.02
- WP-31.05 (real-52/26 evidence): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\31-arcchat-mobile-android.md, anchor rule-wp-31.05

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
Notes: Planning repair 2026-10-08 (DLV-34; P2-021): Real desktop dispatch unchanged; stack-neutral. Acceptance unchanged.
```

```text
Execute ArcForges delivery task AND.26 — Real FCM sending and physical Android receipt.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\android.md (anchor task-and-26).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Mobile (integration owner: Mobile integration owner, the holder of roles/integration-mobile).
Claim and handoff record: claims/and-26 (python tools/delivery.py claim AND.26 --worker <name>); task branch task/and-26 in Mobile; ledger record ledger/tasks/and-26.md.
Kind/size: integration/M. Baseline: not-started.
Outcome: PG-24: a project-bound FCM credential actually sends and a physical arm64 device actually receives, including duplicate/rotation/revocation and denied-permission/no-GMS recovery

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-31.04 (physical receipt closure): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\31-arcchat-mobile-android.md, anchor rule-wp-31.04
- WP-32:pg-24-completion-gate-paragraph-recheck PG-24 completion-gate paragraph (recheck on distributed artifact) (PG-24 closure): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\32-mobile-release-and-store-gates.md, package-level obligation
- WP-45.09 (device-delivery half): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\45-operations-support-and-trust-safety.md, anchor rule-wp-45.09
- WP-32.05 (physical/no-GMS/permission evidence half): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\32-mobile-release-and-store-gates.md, anchor rule-wp-32.05

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
Notes: Merged duplicate integration or closure task formerly proposed as COM.17. Planning repair 2026-10-08 (DLV-34; P2-021): Physical FCM receipt unchanged; the receipt side uses the .NET Firebase binding. Acceptance unchanged.
```

```text
Execute ArcForges delivery task AND.27 — ArcScope library, reports and simulation runs on Android.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\android.md (anchor task-and-27).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Mobile (integration owner: Mobile integration owner, the holder of roles/integration-mobile).
Claim and handoff record: claims/and-27 (python tools/delivery.py claim AND.27 --worker <name>); task branch task/and-27 in Mobile; ledger record ledger/tasks/and-27.md.
Kind/size: feature/L. Baseline: not-started.
Outcome: AN14 and AN26-AN28: the read-only ArcScope library, session and report views with provenance and stored chart snapshots, report sharing through the system share sheet, simulation run status with cancel, and the ArcScope notification kinds opening their objects. A fresh installation discovers runs with simulation.listRuns before reading details or cancelling. The AN27 static PDF preview is retired under P2-022 and replaced by download or share of the exported bundle and an Android ACTION_VIEW intent to the system PDF viewer for arcscope.report.pdf.v1. The app embeds no PDF parser or renderer, and generic PDF attachments remain opaque files.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-31.07 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\31-arcchat-mobile-android.md, anchor rule-wp-31.07

Entry condition: adoption slice ADOPT.10.android is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] AND.11: the Library route and resource preview surfaces
- [contract] CON.24: the generated library operations
- [contract] CON.21: the generated simulation operations
Completion prerequisites (may start earlier; cannot complete before these are complete):
- [integration] CLOUD.68: the deployed library read model
- [integration] SIM.05: the deployed simulation operations
- [integration] SCOPE.22: the delivered desktop project/session and report publication adapter

Permitted write scope: Mobile:src/features/ArcForges.Mobile.Scope/**
Unblocks: AND.15

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Local real-integration run of the affected scenario in an existing environment, recorded once; offline and static checks in CI; no hosted runtime, device, browser, live-service or inference CI (P2-017). PDF disposition check (P2-022): the ACTION_VIEW hand-off of arcscope.report.pdf.v1 to the system viewer is exercised in the local run, and the AND.18 closure fixture and AND.19 architecture tests reject any PDF parser or renderer package in the app closure.
Completion evidence for the ledger: A report synced from ArcScope desktop found, read and shared on Android; a Cloud simulation run followed to its terminal state; revocation, unavailable-artifact and raw-data-local cases. Run discovery after reinstall or on another authorized device; no remembered run ID required. PDF disposition evidence: the exported report opened through ACTION_VIEW in a system viewer on the device, and the closure listing shows no PDF renderer.
Notes: Planning repair 2026-10-08 (DLV-34; P2-021): ArcScope library, report and simulation views port to MAUI; system share sheet and notification behaviours use MAUI platform equivalents. Writes moved to the C# feature project. The AN27 static PDF preview is retired under P2-022.2 (download or share of the bundle, and an Android ACTION_VIEW hand-off to the system viewer); the other acceptance is unchanged.
```

```text
Execute ArcForges delivery task AND.40 — MAUI migration of the existing Mobile app: Hello client, streaming consumer rules, Keystore probe, CI, signing and C# policy (Kotlin, KMP and Gradle retired).

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\android.md (anchor task-and-40).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Mobile (integration owner: Mobile integration owner, the holder of roles/integration-mobile).
Claim and handoff record: claims/and-40 (python tools/delivery.py claim AND.40 --worker <name>); task branch task/and-40 in Mobile; ledger record ledger/tasks/and-40.md.
Kind/size: producer/L. Baseline: not-started.
Outcome: Mobile is a .NET MAUI Android app (net10.0-android only, Mono runtime with AOT for release, UseMonoRuntime=true explicit, applicationId com.arcforges.mobile, persistent android-release signing identity cert SHA256 7a8b3b14...). Its Hello client uses Grpc.Net.Client.Web selecting binary gRPC-Web, with the transport rules carried over from the retired Kotlin client (the GrpcWebMode and server-stream media type are not settled here: they are observed and recorded by PRF.12 together with the fallback decision): no cookies, no redirects, no connection retry, deadline no more than 5 s, 10 s call timeout, the grpc-timeout header in the same format, and the 1..256 name rule. Its streaming consumer keeps frames in order, requires exactly one OK trailer (a missing trailer is DATA_LOSS), stays bounded, and closes the stream on cancellation even when the caller is cancelled (NonCancellable close). A Keystore probe reports the platform security level without claiming hardware backing. CI on Windows and Linux compiles and executes the offline unit tests; the signed candidate and prerelease pipeline use the persistent identity in the protected android-release environment only. GOV.12's Gradle policy is replaced by a C# policy suite that keeps its layering, licence, naming and banned-API categories: the seven canonical BAN-* categories are enforced by Mobile-owned Apache-2.0 rules with negative fixtures, authored from the Design requirement text. Under P2-021.3 Mobile never consumes an AGPL-3.0-only DesktopPlatform package: no copy, port or consumption of the DesktopPlatform banned-symbol catalog and no ArcForges.Build.Policy package is part of the MAUI closure. Mobile's build-only consumption of ArcForges.Build.Policy 1.0.0-ci.40.1 recorded under GOV.12 (PR17, merged 34c64e0) ends in this task, which reverses, for Mobile, the GOV.12 single-canonical-producer receipt (history retained). The Kotlin app, KMP shared module and Gradle build retire in the same change that makes the MAUI candidate pass the offline checks.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-30.03 (Hello client transport and streaming consumer rules only (binary gRPC-Web, deadlines, no cookies, no redirects, no retry, exactly one OK trailer); full contract consumption stays in AND.04): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\30-mobile-shared-architecture.md, anchor rule-wp-30.03
- WP-05.00 (GOV.12 successor: Mobile policy suite in C#): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\05-architecture-and-repository-policy-tests.md, anchor rule-wp-05.00
- WP-05.01 (GOV.12 successor: licence boundary and dependency allowlist over NuGet): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\05-architecture-and-repository-policy-tests.md, anchor rule-wp-05.01
- WP-05.02 (GOV.12 successor: forbidden-term scanner in the Mobile PR build): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\05-architecture-and-repository-policy-tests.md, anchor rule-wp-05.02
- WP-05.04 (GOV.12 successor: Mobile banned-API fixtures): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\05-architecture-and-repository-policy-tests.md, anchor rule-wp-05.04

Entry condition: adoption slice ADOPT.10.android is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] AND.01: the com.arcforges.mobile identity and the pinned .NET 10 / Android workload / NuGet tuple
Completion prerequisites (may start earlier; cannot complete before these are complete):
- [integration] CON.11: the generated C# EventService Watch and Poll operations and the ApplicationService operations that CON.11 publishes in the NuGet Contracts packages (events.proto and application.proto)
- [integration] CLOUD.29: the deployed stream connection and authentication (EventService.Watch shell) that the streaming consumer rules are checked against

Permitted write scope: Mobile:src/ArcForges.Mobile/**; Mobile:src/core/ArcForges.Mobile.Network/**; Mobile:src/core/ArcForges.Mobile.Security/**; Mobile:tests/ArcForges.Mobile.Tests/**; Mobile:tests/ArcForges.Mobile.Policy/**; Mobile:ArcForges.Mobile.slnx; Mobile:global.json; Mobile:Directory.Build.props; Mobile:Directory.Packages.props; Mobile:NuGet.config; Mobile:.github/workflows/ci.yml; Mobile:.github/workflows/security.yml; Mobile:.gitleaks.toml; Mobile:eng/mobile.py; Mobile:eng/published.py; Mobile:eng/policy/**; Mobile:README.md; Mobile:AGENTS.md; Mobile:docs/**; Mobile:app/**; Mobile:shared/**; Mobile:gradle/**; Mobile:build.gradle.kts; Mobile:settings.gradle.kts; Mobile:settings-gradle.lockfile; Mobile:gradle.properties; Mobile:gradlew; Mobile:gradlew.bat; Mobile:.java-version; Mobile:eng/licences.gradle.kts
Shared resources (follow the owner protocol): RES-mobile-build-config (exclusive): AND.01 pins the candidate .NET tuple (global.json, Directory.Build.props, Directory.Packages.props, NuGet.config and the identity project) and appends to this resource. AND.40 holds the exclusive lease `leases/res-mobile-build-config` for the Gradle-to-.NET restructure of the solution, lock files and policy data; AND.02 then registers the .NET project set under the same exclusive lease. Later tasks edit only their own project, append package versions to Directory.Packages.props, and regenerate packages.lock.json after rebase; dependency additions carry admission receipts.; RES-android-signing-and-store (append): Used only by release tasks through protected CI environments; no task creates replacement keys or listings.
Unblocks: AND.02, AND.04, CLOUD.84, CON.40, PRF.12

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline on Windows and Linux CI only (compile, offline xUnit and policy tests, actionlint, gitleaks, existing eng/*.py tests): restore with locked packages (packages.lock.json), NuGet audit and dependency-admission and provenance records for every package in the closure (Apache-2.0 only; no AGPL DesktopPlatform package and no ArcForges.Build.Policy reference); net10.0-android Release build with Mono AOT, trimming and R8 (AndroidLinkTool=r8), which is the first proof of the AND.01 candidate tuple (a failure reopens AND.01); the Hello transport suite (no cookies, no redirects, no retry, deadline cap 5 s, call timeout 10 s, grpc-timeout format, binary gRPC-Web selected through the configured GrpcWebMode with the configured media type asserted, the observed unary and server-stream mode left to PRF.12, 1..256 name rule) and the streaming suite (ordered frames then one OK trailer; an error trailer after frames keeps the frames and status; a missing trailer is DATA_LOSS; deadline mid-stream keeps frames and gives DEADLINE_EXCEEDED; cancel releases the stream) against loopback fixtures; C# policy tests (layering, licence boundary, forbidden terms, the seven BAN-* categories as Mobile-owned rules) with negative fixtures; F-023-class closure re-proof (licence, provenance, SBOM and NOTICE) for the MAUI closure on the candidate; a NuGet closure check that rejects an unadmitted or unpinned package. Signing and prerelease publication run only in the protected android-release environment on main. Emulator and device runs are local opt-in under P2-017, not CI. The Gradle, Kotlin and KMP retirement lands only with a candidate that passes these offline checks.
Completion evidence for the ledger: Offline CI run identifiers for the Windows and Linux builds with executed test counts; transport and streaming test matrix results (including the configured media-type assertion; observed unary and server-stream values are PRF.12 evidence); Keystore probe output recording the reported security level (software level is not hardware evidence); policy suite results with negative fixtures; NuGet admission and provenance records for the closure; a closure listing showing no ArcForges.Build.Policy and no AGPL DesktopPlatform package; F-023-class closure re-proof for the MAUI candidate (licence, provenance, SBOM and NOTICE); a retirement receipt listing every removed Kotlin, KMP, Gradle and ArcForges.Build.Policy consumer path; signed candidate hash and applicationId and certificate SHA256 verification (7a8b3b14...); reinstall guidance from io.github.arcforges.mobile recorded in docs/releasing.md with no data migration.
Notes: Planning repair 2026-10-08 (DLV-34; P2-021): new C#-first successor of the Kotlin Android foundation, of GOV.12 (Gradle policy) and of the Android CI and signing surfaces. Published Kotlin prereleases stay immutable history; nothing here unpublishes, deletes or re-signs them. No start edge on CON.07: the Hello.V1 surface the transport uses is already published in the ArcForges.Contracts.PublicApi NuGet package (Contracts repo evidence), and the transport, streaming consumer and Keystore probe use none of CON.07's identity, session or native-auth types; AND.04 keeps its CON.07 edge for those. CON.11 and CLOUD.29 are completion edges, not start edges: the loopback fixtures are test-only characterisation of the EventService stream shape, not a substitute, and the published client and the real stream producer confirm it before AND.40 completes.
```
