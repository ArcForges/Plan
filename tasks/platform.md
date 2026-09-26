# ArcForges delivery task prompts — Desktop platform mechanisms

Generated from Design `docs/planning/delivery/delivery-graph.json` by `tools/delivery.py`; do not edit by hand.
Each block is self-contained. Claim a task only when `python tools/delivery.py ready` lists it, with
`python tools/delivery.py claim <TASK-ID> --worker <name>`, then follow `arcforges-implementation.md`.
Tasks are ordered by lane for reading; the order is not a schedule.

## Desktop platform mechanisms

```text
Execute ArcForges delivery task PLT.01 — Store abstraction and the single transactional write path.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\platform.md (anchor task-plt-01).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/plt-01 (python tools/delivery.py claim PLT.01 --worker <name>); task branch task/plt-01 in DesktopPlatform; ledger record ledger/tasks/plt-01.md.
Kind/size: producer/L. Baseline: not-started.
Outcome: IStore/CommitUnit/WriteCommand exist with the eight-step write path (validate, authorize, begin commit unit, apply, journal, advance revision, enqueue outbox, commit, notify) implemented exactly once; persistence types never cross the repository boundary; a policy test proves no alternative write path exists.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-07.00 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\07-local-persistence-foundation.md, anchor rule-wp-07.00
- WP-07:content-origin-carrier-projection-commit Content-origin carrier projection committed atomically with payload in the same owner transaction/journal boundary (SS2 required design input) (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\07-local-persistence-foundation.md, package-level obligation

Entry condition: adoption slice ADOPT.02.platform is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] FND.02: CommandId/effect-certainty types
- [artifact] FND.03: Revision type
- [artifact] FND.05: reason-code registry
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:src/BuildingBlocks/ArcForges.Persistence.Sqlite/**
Shared resources (follow the owner protocol): RES-desktopplatform-build-config (append): Solution/project lists, central package versions and CI job lists are appended by the task that adds a project, dependency or job; dependency additions follow the dependency-admission policy with a reviewed receipt; lock files are regenerated after rebase and never hand-merged; the integration owner resolves ordering conflicts at merge.
Unblocks: CLOUD.38, FND.02, NAT.02, NOTES.01, NOTES.02, PLT.05, PLT.07, PLT.08, PLT.39, PLT.43, PLT.44, SCOPE.01, SLATE.10

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline unit + integration tests against a real local SQLite file (no external service): policy test asserting no alternative write path, concurrency tests for serialised writes/concurrent reads, boundary test that no storage type appears in an application signature. AOT/trim diagnostics build-breaking since this library is IsAotCompatible.
Completion evidence for the ledger: Single-write-path policy test result.
Notes: Interface-first decoupling recommended: define IJournalWriter/IJournalReader here as the seam PLT.02 implements, so PLT.01 and PLT.02 can be authored in parallel PRs against the same interface rather than serially.
```

```text
Execute ArcForges delivery task PLT.02 — Append-only journal with durability and bounded truncation.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\platform.md (anchor task-plt-02).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/plt-02 (python tools/delivery.py claim PLT.02 --worker <name>); task branch task/plt-02 in DesktopPlatform; ledger record ledger/tasks/plt-02.md.
Kind/size: producer/M. Baseline: not-started.
Outcome: JournalEntry records every commit with enough information to replay; journal writes are durable before a commit is acknowledged; growth is bounded by snapshot policy and truncation is safe under concurrent read.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-07.01 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\07-local-persistence-foundation.md, anchor rule-wp-07.01

Entry condition: adoption slice ADOPT.02.platform is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] FND.02: CommandId type
- [artifact] FND.03: Revision/Sequence types
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:src/BuildingBlocks/ArcForges.Persistence.Sqlite/**
Shared resources (follow the owner protocol): RES-assistant-store-schema (append): Numbered migrations are allocated at merge by the integration owner (a rebase renumbers pending migrations); each migration is forward-only with its recovery and downgrade-refusal tests; no task edits a merged migration.
Unblocks: NOTES.11, PLT.03, PLT.08, SLATE.11

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline tests: durability test using a simulated process kill between journal write and commit acknowledgement (in-process fault injection, not a real OS-level crash - that remains local opt-in); replay test; truncation-under-read test.
Completion evidence for the ledger: Durability and replay results.
```

```text
Execute ArcForges delivery task PLT.03 — Snapshot and crash/corruption recovery.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\platform.md (anchor task-plt-03).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/plt-03 (python tools/delivery.py claim PLT.03 --worker <name>); task branch task/plt-03 in DesktopPlatform; ledger record ledger/tasks/plt-03.md.
Kind/size: producer/L. Baseline: not-started.
Outcome: Snapshots are policy-triggered, self-describing and verifiable; recovery selects the latest verifiable snapshot and replays the journal forward to typed outcomes (clean, recovered-with-loss, unrecoverable-with-preserved-evidence); native crash and safe-start paths are handled.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-07.02 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\07-local-persistence-foundation.md, anchor rule-wp-07.02

Entry condition: adoption slice ADOPT.02.platform is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] PLT.02: journal append/replay implementation
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:src/BuildingBlocks/ArcForges.Persistence.Sqlite/**
Shared resources (follow the owner protocol): RES-desktopplatform-policy-data (append): Generated policy data is regenerated from its pinned source and never hand-edited; the reason-code registry is append-only with stable codes; each task adds its own test classes and evidence rows.
Unblocks: NOTES.11, PLT.08, SLATE.11

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline tests: full recovery matrix (clean shutdown, hard kill, kill during snapshot, kill during migration, corrupted snapshot, corrupted journal tail, disk-full during write) using simulated fault injection; native-crash/safe-start scenarios beyond process-level simulation are local opt-in only.
Completion evidence for the ledger: Full recovery matrix with a named outcome per case.
Notes: This is one of the two narrowest, highest-value early risk proofs in the whole platform area (with PLT.45 content-helper isolation): if crash recovery has a hidden defect, every downstream product's data-loss guarantees are invalid. Recommend starting this in the same wave as PLT.01/02, not deferred.
```

```text
Execute ArcForges delivery task PLT.04 — Migration runner.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\platform.md (anchor task-plt-04).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/plt-04 (python tools/delivery.py claim PLT.04 --worker <name>); task branch task/plt-04 in DesktopPlatform; ledger record ledger/tasks/plt-04.md.
Kind/size: producer/M. Baseline: not-started.
Outcome: Numbered migrations run through a transactional-per-step, idempotent, resumable-after-interruption runner; StorageSchemaVersion equals the highest applied migration; downgrade is either an explicit reverse migration or a clean refusal.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-07.03 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\07-local-persistence-foundation.md, anchor rule-wp-07.03

Entry condition: adoption slice ADOPT.02.platform is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] FND.06: StorageSchemaVersion axis type
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:src/BuildingBlocks/ArcForges.Persistence.Sqlite/**; DesktopPlatform:fixtures/formats/**
Shared resources (follow the owner protocol): RES-desktopplatform-fixtures (append): Fixtures are added per task in their own directory; golden files are never regenerated to make a test pass.
Unblocks: NOTES.11, PLT.08, PLT.29, SLATE.10, UPD.04

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline tests: forward migration from every historical version fixture, interruption/resume, refusal test for unsupported downgrade, golden-fixture semantic comparison (QI-07).
Completion evidence for the ledger: Migration results against every historical fixture plus semantic comparison.
```

```text
Execute ArcForges delivery task PLT.05 — Managed resource store (content-addressed blobs).

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\platform.md (anchor task-plt-05).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/plt-05 (python tools/delivery.py claim PLT.05 --worker <name>); task branch task/plt-05 in DesktopPlatform; ledger record ledger/tasks/plt-05.md.
Kind/size: producer/M. Baseline: not-started.
Outcome: Content-addressed storage with identity-to-location resolution, integrity verification on read, reference counting derived from a referrer table, and a GC path that never deletes a referenced object even after a crash mid-operation.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-07.04 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\07-local-persistence-foundation.md, anchor rule-wp-07.04

Entry condition: adoption slice ADOPT.02.platform is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] PLT.01: store abstraction's write-path pattern
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:src/BuildingBlocks/ArcForges.Persistence.Resources/**
Shared resources (follow the owner protocol): RES-desktopplatform-build-config (append): Solution/project lists, central package versions and CI job lists are appended by the task that adds a project, dependency or job; dependency additions follow the dependency-admission policy with a reviewed receipt; lock files are regenerated after rebase and never hand-merged; the integration owner resolves ordering conflicts at merge.
Unblocks: NOTES.08, PLT.08, PLT.22

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline tests: integrity verification on read, reference-counting test including crash between reference and store, garbage-collection safety test.
Completion evidence for the ledger: Integrity, reference-counting and garbage-collection safety results.
```

```text
Execute ArcForges delivery task PLT.06 — Large append store for high-rate chunked data.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\platform.md (anchor task-plt-06).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/plt-06 (python tools/delivery.py claim PLT.06 --worker <name>); task branch task/plt-06 in DesktopPlatform; ledger record ledger/tasks/plt-06.md.
Kind/size: producer/M. Baseline: not-started.
Outcome: A chunked, verifiable append store outside the relational working store, with per-chunk checksums, an explicit end marker, and honest truncation: a crash mid-append yields a verifiable prefix plus a recorded loss, never a silently short file.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-07.05 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\07-local-persistence-foundation.md, anchor rule-wp-07.05

Entry condition: adoption slice ADOPT.02.platform is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] FND.02: execution/effect-certainty types for loss records
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:src/BuildingBlocks/ArcForges.Persistence.Resources/**
Shared resources (follow the owner protocol): RES-assistant-store-schema (append): Numbered migrations are allocated at merge by the integration owner (a rebase renumbers pending migrations); each migration is forward-only with its recovery and downgrade-refusal tests; no task edits a merged migration.
Unblocks: PLT.08, SCOPE.07, SLATE.35

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline tests: append-under-kill at chunk boundaries and mid-chunk, verification of recovered prefix, loss-record assertion.
Completion evidence for the ledger: Append-under-kill results with loss records.
```

```text
Execute ArcForges delivery task PLT.07 — Derived-store abstraction and storage-pressure model.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\platform.md (anchor task-plt-07).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/plt-07 (python tools/delivery.py claim PLT.07 --worker <name>); task branch task/plt-07 in DesktopPlatform; ledger record ledger/tasks/plt-07.md.
Kind/size: producer/S. Baseline: not-started.
Outcome: A DerivedStore abstraction with declared rebuild semantics (every derived store deletable/rebuildable from canonical data) and a StoragePressureState model whose eviction policy only ever touches derived data.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-07.06 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\07-local-persistence-foundation.md, anchor rule-wp-07.06

Entry condition: adoption slice ADOPT.02.platform is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] PLT.01: store abstraction boundary
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:src/BuildingBlocks/ArcForges.Persistence.Derived/**
Shared resources (follow the owner protocol): RES-desktopplatform-build-config (append): Solution/project lists, central package versions and CI job lists are appended by the task that adds a project, dependency or job; dependency additions follow the dependency-admission policy with a reviewed receipt; lock files are regenerated after rebase and never hand-merged; the integration owner resolves ordering conflicts at merge.
Unblocks: NOTES.15, PLT.08, SLATE.21

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline tests: delete-and-rebuild test per derived-store kind, eviction test asserting canonical data is never evicted.
Completion evidence for the ledger: Rebuild and eviction results.
```

```text
Execute ArcForges delivery task PLT.08 — Publish Persistence packages and verify real integration.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\platform.md (anchor task-plt-08).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/plt-08 (python tools/delivery.py claim PLT.08 --worker <name>); task branch task/plt-08 in DesktopPlatform; ledger record ledger/tasks/plt-08.md.
Kind/size: acceptance/S. Baseline: not-started.
Outcome: ArcForges.Persistence.Sqlite,.Persistence.Resources and.Persistence.Derived are packed, admitted to the publication allowlist, published, and independently consumed; package consumption is shown not to centralise product data ownership.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-07.90 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\07-local-persistence-foundation.md, anchor rule-wp-07.90

Entry condition: adoption slice ADOPT.02.platform is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] PLT.01: write path
- [artifact] PLT.02: journal
- [artifact] PLT.03: snapshot/recovery
- [artifact] PLT.04: migration runner
- [artifact] PLT.05: resource store
- [artifact] PLT.06: append store
- [artifact] PLT.07: derived store/pressure
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:eng/packaging/packages.json; DesktopPlatform:eng/version-sources.json
Shared resources (follow the owner protocol): RES-desktopplatform-build-config (append): Solution/project lists, central package versions and CI job lists are appended by the task that adds a project, dependency or job; dependency additions follow the dependency-admission policy with a reviewed receipt; lock files are regenerated after rebase and never hand-merged; the integration owner resolves ordering conflicts at merge.; RES-desktopplatform-package-inventory (append): Each producer task adds its own package entry; every merge to main packs and publishes all packages at one version; consumers pin the candidate produced by the merge of the capability they need, never waiting for a package closure task; one merge queue.

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): P2-017: offline packages.py verify plus policy tests; real crash/hardware-level recovery evidence beyond simulated kills is local opt-in, recorded separately.
Completion evidence for the ledger: Owned artifact and real-integration receipt per the WP-07.90 template.
```

```text
Execute ArcForges delivery task PLT.09 — Local gRPC transport and framing over Named Pipe/UDS.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\platform.md (anchor task-plt-09).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/plt-09 (python tools/delivery.py claim PLT.09 --worker <name>); task branch task/plt-09 in DesktopPlatform; ledger record ledger/tasks/plt-09.md.
Kind/size: producer/L. Baseline: not-started.
Outcome: Generated gRPC over HTTP/2 runs on Windows Named Pipe/Unix domain socket between parent and owned helper/extension children via a custom Kestrel IConnectionListenerFactory and ConnectCallback client, with explicit registration, AOT-safe serialization, and zero local TCP listener.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-08.00 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\08-local-ipc-and-registration.md, anchor rule-wp-08.00
- WP-08:no-product-listener-global-discovery-str No product listener/global discovery - structural constraint on every substep, most directly tested by transport/registration (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\08-local-ipc-and-registration.md, package-level obligation

Entry condition: adoption slice ADOPT.02.platform is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] PRF.04: proven AOT gRPC-over-OS-stream pattern from the two real helper-probe processes
- [contract] CON.04: ArcForges.Contracts.LocalRpc.Platform/.Sandbox generated proto services
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:src/BuildingBlocks/ArcForges.LocalRpc/**
Shared resources (follow the owner protocol): RES-desktopplatform-build-config (append): Solution/project lists, central package versions and CI job lists are appended by the task that adds a project, dependency or job; dependency additions follow the dependency-admission policy with a reviewed receipt; lock files are regenerated after rebase and never hand-merged; the integration owner resolves ordering conflicts at merge.; RES-desktopplatform-policy-data (append): Generated policy data is regenerated from its pinned source and never hand-edited; the reason-code registry is append-only with stable codes; each task adds its own test classes and evidence rows.
Unblocks: NAT.01, PLT.10, PLT.13, PLT.14, PLT.15, PLT.16, PLT.45

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): CI uses targeted deterministic offline framing and authentication fixtures. Actual Named Pipe/Unix domain socket behavior, malformed-frame handling, wrong-user denial and the absence of a local TCP listener are checked locally once when the existing environment supports the affected behavior and the change requires it; fixture evidence never substitutes for actual OS-stream evidence. Do not execute real IPC integration in CI or provision an environment solely for validation.
Completion evidence for the ledger: Actual OS streams, malformed frames, wrong-user denial and no local TCP listener.
Notes: This is the WP-level edge most worth re-examining: the old header lists WP08 upstream as '06 and 07'. WP-07 (Persistence) is NOT a real start need for any WP08 substep - WP-04.01's own gate explicitly defers durable command/receipt storage to WP07/21/52, meaning WP08's in-flight idempotency stays memory-only; nothing in WP-08.00-08.06 touches SQLite. Recommend dropping the 07->08 start edge entirely; it appears to be inherited phase-grouping (both are 'Phase A/B foundation') rather than a genuine code dependency.
```

```text
Execute ArcForges delivery task PLT.10 — Parent-owned endpoint identity.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\platform.md (anchor task-plt-10).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/plt-10 (python tools/delivery.py claim PLT.10 --worker <name>); task branch task/plt-10 in DesktopPlatform; ledger record ledger/tasks/plt-10.md.
Kind/size: producer/M. Baseline: not-started.
Outcome: Parent launch descriptor fixes endpoint, process/build/protocol identity, nonce and epoch; owner-only endpoint files are created/removed atomically; a stale descriptor never authorizes a child.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-08.01 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\08-local-ipc-and-registration.md, anchor rule-wp-08.01

Entry condition: adoption slice ADOPT.02.platform is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] PLT.09: transport/framing
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:src/BuildingBlocks/ArcForges.LocalRpc/**
Unblocks: PLT.11, PLT.16, PLT.38

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline/local tests: concurrent launch, stale descriptor, forged nonce/build, parent-death cleanup.
Completion evidence for the ledger: Concurrent launch, stale descriptor, forged nonce/build and parent-death cleanup results.
```

```text
Execute ArcForges delivery task PLT.11 — Child registration lifecycle.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\platform.md (anchor task-plt-11).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/plt-11 (python tools/delivery.py claim PLT.11 --worker <name>); task branch task/plt-11 in DesktopPlatform; ledger record ledger/tasks/plt-11.md.
Kind/size: producer/M. Baseline: not-started.
Outcome: LocalBootstrap authentication with 30s lease/10s renewal, epoch fencing and restartable restricted launch; expired/stale children cannot call; parent restart requires fresh grants.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-08.02 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\08-local-ipc-and-registration.md, anchor rule-wp-08.02
- WP-08:no-product-listener-global-discovery-str No product listener/global discovery - structural constraint on every substep, most directly tested by transport/registration (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\08-local-ipc-and-registration.md, package-level obligation

Entry condition: adoption slice ADOPT.02.platform is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] PLT.10: endpoint identity
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:src/BuildingBlocks/ArcForges.LocalRpc/**
Unblocks: PLT.12, PLT.16

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline/local tests: expired/stale child cannot call, parent restart requires fresh grants.
Completion evidence for the ledger: Expired/stale child cannot call; parent restart requires fresh grants.
```

```text
Execute ArcForges delivery task PLT.12 — Static routing and version refusal.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\platform.md (anchor task-plt-12).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/plt-12 (python tools/delivery.py claim PLT.12 --worker <name>); task branch task/plt-12 in DesktopPlatform; ledger record ledger/tasks/plt-12.md.
Kind/size: producer/S. Baseline: not-started.
Outcome: Resolves only explicitly launched children and their declared generated services; rejects unsupported version/capability; never selects an installed product as fallback.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-08.03 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\08-local-ipc-and-registration.md, anchor rule-wp-08.03

Entry condition: adoption slice ADOPT.02.platform is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] PLT.11: registration lifecycle
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:src/BuildingBlocks/ArcForges.LocalRpc/**
Unblocks: PLT.16

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline tests: version mismatch and unregistered service refusal.
Completion evidence for the ledger: Version mismatch and unregistered service refusal.
```

```text
Execute ArcForges delivery task PLT.13 — Bounds and concurrency.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\platform.md (anchor task-plt-13).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/plt-13 (python tools/delivery.py claim PLT.13 --worker <name>); task branch task/plt-13 in DesktopPlatform; ledger record ledger/tasks/plt-13.md.
Kind/size: producer/M. Baseline: not-started.
Outcome: 16 active/64 queued bounded calls, deadlines and parent-owned callback channels; no recursive saturated callback lane.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-08.04 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\08-local-ipc-and-registration.md, anchor rule-wp-08.04

Entry condition: adoption slice ADOPT.02.platform is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] PLT.09: transport
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:src/BuildingBlocks/ArcForges.LocalRpc/**
Unblocks: PLT.16

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline tests: queue/memory bound, fairness, timeout and typed overload.
Completion evidence for the ledger: Queue/memory bound, fairness, timeout and typed overload.
```

```text
Execute ArcForges delivery task PLT.14 — Disconnect, cancel and retry semantics.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\platform.md (anchor task-plt-14).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/plt-14 (python tools/delivery.py claim PLT.14 --worker <name>); task branch task/plt-14 in DesktopPlatform; ledger record ledger/tasks/plt-14.md.
Kind/size: producer/M. Baseline: not-started.
Outcome: Effect certainty, stable command/receipt identity and cancellation are preserved across helper crashes; replay only when explicitly allowed; kill before/after commit and lost-ack scenarios resolve to typed unknown-effect outcomes, in-memory only (durable receipts remain WP07/21/52 territory per WP-04.01's own gate).

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-08.05 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\08-local-ipc-and-registration.md, anchor rule-wp-08.05

Entry condition: adoption slice ADOPT.02.platform is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] PLT.09: transport
- [artifact] FND.02: effect-certainty/Outcome types
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:src/BuildingBlocks/ArcForges.LocalRpc/**
Unblocks: PLT.16

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline/local tests: kill before/after commit, lost ack and unknown effect.
Completion evidence for the ledger: Kill before/after commit, lost ack and unknown effect.
```

```text
Execute ArcForges delivery task PLT.15 — Brokered large data over the sandbox boundary.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\platform.md (anchor task-plt-15).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/plt-15 (python tools/delivery.py claim PLT.15 --worker <name>); task branch task/plt-15 in DesktopPlatform; ledger record ledger/tasks/plt-15.md.
Kind/size: producer/M. Baseline: not-started.
Outcome: Bounded verified chunks over annex-09 sandbox resources/buffers, parent-authorized only; no direct product-to-product transfer ticket.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-08.06 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\08-local-ipc-and-registration.md, anchor rule-wp-08.06

Entry condition: adoption slice ADOPT.02.platform is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] PLT.09: transport
- [contract] CON.04: ContentSandboxService/slot-grant wire shapes in contracts/09-local-grpc-and-sandbox.md
Completion prerequisites (may start earlier; cannot complete before these are complete):
- [integration] PLT.45: the real ContentSandbox helper actually using these brokered buffers

Permitted write scope: DesktopPlatform:src/BuildingBlocks/ArcForges.LocalRpc/**
Unblocks: PLT.16, PLT.24, PLT.45

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline/local tests: wrong resource grant, range/hash/expiry/cancel and orphan cleanup.
Completion evidence for the ledger: Wrong resource grant, range/hash/expiry/cancel and orphan cleanup.
```

```text
Execute ArcForges delivery task PLT.16 — Publish LocalRpc package and verify real integration.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\platform.md (anchor task-plt-16).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/plt-16 (python tools/delivery.py claim PLT.16 --worker <name>); task branch task/plt-16 in DesktopPlatform; ledger record ledger/tasks/plt-16.md.
Kind/size: acceptance/S. Baseline: not-started.
Outcome: ArcForges.LocalRpc is packed, admitted, published, and independently consumed; all owned actions/schemas/public interfaces and tests are complete with applicable UX acceptance ledger rows recorded.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-08.90 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\08-local-ipc-and-registration.md, anchor rule-wp-08.90

Entry condition: adoption slice ADOPT.02.platform is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] PLT.09: transport
- [artifact] PLT.10: endpoint identity
- [artifact] PLT.11: registration
- [artifact] PLT.12: routing
- [artifact] PLT.13: bounds
- [artifact] PLT.14: cancel/retry
- [artifact] PLT.15: brokered data
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:eng/packaging/packages.json
Shared resources (follow the owner protocol): RES-desktopplatform-package-inventory (append): Each producer task adds its own package entry; every merge to main packs and publishes all packages at one version; consumers pin the candidate produced by the merge of the capability they need, never waiting for a package closure task; one merge queue.

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): P2-017: offline verify plus policy tests; real multi-process OS-stream evidence beyond the repo's own build-machine tests is local opt-in.
Completion evidence for the ledger: Exact artifact/consumer and applicable UX acceptance ledger.
```

```text
Execute ArcForges delivery task PLT.17 — Application identity and in-process composition.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\platform.md (anchor task-plt-17).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/plt-17 (python tools/delivery.py claim PLT.17 --worker <name>); task branch task/plt-17 in DesktopPlatform; ledger record ledger/tasks/plt-17.md.
Kind/size: producer/S. Baseline: not-started.
Outcome: AppIdentity/InstallationIdentity/InstanceIdentity bound to each application composition root; two products on one device keep separate sessions/history/capabilities; forged/missing target refuses; no running-product registry or shared Hub.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-09.00 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\09-capability-contribution-and-resource-model.md, anchor rule-wp-09.00

Entry condition: adoption slice ADOPT.02.platform is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [contract] CON.91: descriptor contract types (App/Installation/Instance identity wire shapes)
- [artifact] FND.01: identity primitive types
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:src/BuildingBlocks/ArcForges.Capabilities/**
Shared resources (follow the owner protocol): RES-desktopplatform-build-config (append): Solution/project lists, central package versions and CI job lists are appended by the task that adds a project, dependency or job; dependency additions follow the dependency-admission policy with a reviewed receipt; lock files are regenerated after rebase and never hand-merged; the integration owner resolves ordering conflicts at merge.
Unblocks: APP.01, EXE.01, PLT.18, PLT.19, PLT.21, PLT.22, PLT.25

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline unit tests: two-product separation, forged/missing target refusal.
Completion evidence for the ledger: Identity lifecycle matrix.
Notes: The old header lists WP09 upstream as '03, 08'. Reading contracts/02-local-rpc-operations.md closely: product capability ports (ICapabilityProvider etc.) are IN-PROCESS typed calls; only helper/extension children use the WP-08 Named Pipe/UDS transport. WP-09.00-09.06 (identity, registration, selection, availability, context, resources, navigation/health) do not need WP-08 at all. Recommend narrowing the 08->09 edge to apply only where PLT.24 (invocation pipeline) routes to an admitted child - see PLT.24's own start edges.
```

```text
Execute ArcForges delivery task PLT.18 — Static contribution registration.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\platform.md (anchor task-plt-18).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/plt-18 (python tools/delivery.py claim PLT.18 --worker <name>); task branch task/plt-18 in DesktopPlatform; ledger record ledger/tasks/plt-18.md.
Kind/size: producer/M. Baseline: not-started.
Outcome: Capability/context/artifact/lifecycle/deep-link handlers register inside the owning process through generated descriptors and explicit composition; duplicate IDs, wrong owner, unavailable child, undeclared tool schema and cross-product registration all refuse; registration is idempotent and survives restart.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-09.01 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\09-capability-contribution-and-resource-model.md, anchor rule-wp-09.01
- WP-09:contribution-registration-state-durable Contribution/registration state durable across restarts (SS6 impacts) (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\09-capability-contribution-and-resource-model.md, package-level obligation

Entry condition: adoption slice ADOPT.02.platform is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] PLT.17: application identity/composition root
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:src/BuildingBlocks/ArcForges.Contributions/**
Unblocks: NAT.01, NOTES.12, PLT.25

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline tests: duplicate IDs, wrong owner, unavailable child, undeclared tool schema, cross-product registration refusal; registration survives a simulated restart against the persistence layer PLT.01/PLT.05 provide.
Completion evidence for the ledger: Registration idempotency and namespace refusal results.
```

```text
Execute ArcForges delivery task PLT.19 — Capability registry and selection.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\platform.md (anchor task-plt-19).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/plt-19 (python tools/delivery.py claim PLT.19 --worker <name>); task branch task/plt-19 in DesktopPlatform; ledger record ledger/tasks/plt-19.md.
Kind/size: producer/L. Baseline: not-started.
Outcome: The wire CapabilityDescriptor/OperationBinding/effect/locus/context/cancellation schema is implemented with a complete initial first-party binding matrix; enumerated bindings are validated against declared Contracts methods; unsupported major, inconsistent pureRead/write classification, readiness mismatch and ambiguous target all reject.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-09.02 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\09-capability-contribution-and-resource-model.md, anchor rule-wp-09.02

Entry condition: adoption slice ADOPT.02.platform is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] PLT.17: identity/composition
- [contract] CON.91: CapabilityDescriptor/OperationBinding wire schema
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:src/BuildingBlocks/ArcForges.Capabilities/**
Unblocks: EXT.00, PLT.20, PLT.24, PLT.25, PLT.37

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline tests: enumerate expected bindings, reject missing/extra methods/unsupported major/inconsistent classification/readiness mismatch/ambiguous target.
Completion evidence for the ledger: Selection priority, determinism and explainability results.
```

```text
Execute ArcForges delivery task PLT.20 — Actions and availability.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\platform.md (anchor task-plt-20).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/plt-20 (python tools/delivery.py claim PLT.20 --worker <name>); task branch task/plt-20 in DesktopPlatform; ledger record ledger/tasks/plt-20.md.
Kind/size: producer/M. Baseline: not-started.
Outcome: Actions are computed from capabilities plus current context, side-effect free, cheap enough for UI enumeration; unavailability always yields a typed reason across permission/entitlement/health/context/version causes.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-09.03 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\09-capability-contribution-and-resource-model.md, anchor rule-wp-09.03

Entry condition: adoption slice ADOPT.02.platform is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] PLT.19: capability registry
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:src/BuildingBlocks/ArcForges.Capabilities/**
Unblocks: PLT.24, PLT.25, PLT.28

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline tests: availability tests across permission/entitlement/health/context/version reasons; purity test asserting no side effect.
Completion evidence for the ledger: Availability reason matrix and purity assertion.
```

```text
Execute ArcForges delivery task PLT.21 — Context providers and freezing.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\platform.md (anchor task-plt-21).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/plt-21 (python tools/delivery.py claim PLT.21 --worker <name>); task branch task/plt-21 in DesktopPlatform; ledger record ledger/tasks/plt-21.md.
Kind/size: producer/M. Baseline: not-started.
Outcome: Context providers contribute typed context; at invocation the context is frozen into an immutable snapshot carried with the invocation; a later live-context change never affects an in-flight invocation; oversized context is refused explicitly.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-09.04 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\09-capability-contribution-and-resource-model.md, anchor rule-wp-09.04

Entry condition: adoption slice ADOPT.02.platform is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] PLT.17: identity/composition
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:src/BuildingBlocks/ArcForges.Capabilities/**
Unblocks: APP.06, PLT.24, PLT.25, PLT.42

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline tests: mutation-during-invocation test asserting frozen snapshot used; size-bounding test asserting oversized context is refused rather than truncated.
Completion evidence for the ledger: Context freezing and size-bound results.
```

```text
Execute ArcForges delivery task PLT.22 — Resources and artifacts resolution.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\platform.md (anchor task-plt-22).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/plt-22 (python tools/delivery.py claim PLT.22 --worker <name>); task branch task/plt-22 in DesktopPlatform; ledger record ledger/tasks/plt-22.md.
Kind/size: producer/M. Baseline: not-started.
Outcome: Resource resolution from reference to access honours ownership and floating-versus-pinned distinction; artifact handlers register per kind; a reference never carries a path/pointer/handle; resolution re-checks permission at access time.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-09.05 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\09-capability-contribution-and-resource-model.md, anchor rule-wp-09.05

Entry condition: adoption slice ADOPT.02.platform is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] PLT.05: managed resource store's identity-to-location resolution
- [artifact] PLT.17: identity/composition
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:src/BuildingBlocks/ArcForges.Capabilities/**
Unblocks: APP.06, PLT.23, PLT.25

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline tests: resolution across owner-present/owner-absent/permission-denied/version-pinned cases; structural test that a reference cannot carry a path.
Completion evidence for the ledger: Resource resolution matrix and structural path prohibition.
```

```text
Execute ArcForges delivery task PLT.23 — Own navigation, hints and health.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\platform.md (anchor task-plt-23).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/plt-23 (python tools/delivery.py claim PLT.23 --worker <name>); task branch task/plt-23 in DesktopPlatform; ledger record ledger/tasks/plt-23.md.
Kind/size: producer/M. Baseline: not-started.
Outcome: Artifact opens and deep links route to the owning application handler; bounded in-process state hints cause authoritative rereads; invalid ownership, missing content, expired child cursor, restart and duplicate hint all recover without launching another product.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-09.06 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\09-capability-contribution-and-resource-model.md, anchor rule-wp-09.06

Entry condition: adoption slice ADOPT.02.platform is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] PLT.22: resource/artifact resolution
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:src/BuildingBlocks/ArcForges.Capabilities/**
Unblocks: PLT.25, PLT.51

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline tests: invalid ownership, missing content, expired child cursor, restart, duplicate hint recovery.
Completion evidence for the ledger: Deep-link hostile-input, event and health results.
```

```text
Execute ArcForges delivery task PLT.24 — Invocation pipeline.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\platform.md (anchor task-plt-24).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/plt-24 (python tools/delivery.py claim PLT.24 --worker <name>); task branch task/plt-24 in DesktopPlatform; ledger record ledger/tasks/plt-24.md.
Kind/size: producer/L. Baseline: not-started.
Outcome: The end-to-end path resolve -> check availability -> freeze context -> authorize -> invoke -> validate result -> record is the ONLY route to a capability; every failure maps to the closed semantic error set; every invocation is traced.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-09.07 (all work except the parts mapped to PLT.57): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\09-capability-contribution-and-resource-model.md, anchor rule-wp-09.07

Entry condition: adoption slice ADOPT.02.platform is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] PLT.19: capability registry/selection
- [artifact] PLT.20: availability
- [artifact] PLT.21: context freezing
Completion prerequisites (may start earlier; cannot complete before these are complete):
- [integration] PLT.15: real LocalRpc brokered routing for the subset of invocations that target an admitted helper/extension child

Permitted write scope: DesktopPlatform:src/BuildingBlocks/ArcForges.Capabilities/**
Shared resources (follow the owner protocol): RES-desktopplatform-policy-data (append): Generated policy data is regenerated from its pinned source and never hand-edited; the reason-code registry is append-only with stable codes; each task adds its own test classes and evidence rows.
Unblocks: APP.02, PLT.25, PLT.57

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline tests: policy test asserting no bypass route exists; error-mapping tests for every semantic error; tracing test.
Completion evidence for the ledger: Pipeline bypass-prohibition, error-mapping and tracing results.
```

```text
Execute ArcForges delivery task PLT.25 — Publish Capabilities/Contributions packages and verify real integration.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\platform.md (anchor task-plt-25).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/plt-25 (python tools/delivery.py claim PLT.25 --worker <name>); task branch task/plt-25 in DesktopPlatform; ledger record ledger/tasks/plt-25.md.
Kind/size: acceptance/S. Baseline: not-started.
Outcome: ArcForges.Capabilities (and the Contributions internals it packages) is packed, admitted, published, and independently consumed; owner refuses invalid/stale invocations and opaque references do not grant access.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-09.90 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\09-capability-contribution-and-resource-model.md, anchor rule-wp-09.90

Entry condition: adoption slice ADOPT.02.platform is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] PLT.17: identity/composition
- [artifact] PLT.18: contribution registration
- [artifact] PLT.19: registry/selection
- [artifact] PLT.20: actions/availability
- [artifact] PLT.21: context freezing
- [artifact] PLT.22: resources/artifacts
- [artifact] PLT.23: navigation/health
- [artifact] PLT.24: invocation pipeline
- [artifact] PLT.57: package task delivered
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:eng/packaging/packages.json; DesktopPlatform:eng/version-sources.json
Shared resources (follow the owner protocol): RES-desktopplatform-build-config (append): Solution/project lists, central package versions and CI job lists are appended by the task that adds a project, dependency or job; dependency additions follow the dependency-admission policy with a reviewed receipt; lock files are regenerated after rebase and never hand-merged; the integration owner resolves ordering conflicts at merge.; RES-desktopplatform-package-inventory (append): Each producer task adds its own package entry; every merge to main packs and publishes all packages at one version; consumers pin the candidate produced by the merge of the capability they need, never waiting for a package closure task; one merge queue.

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): P2-017: offline verify/policy tests; real cross-product UI acceptance is deferred to product WPs (14/18/33/36) that actually consume this package.
Completion evidence for the ledger: Owned artifact and real-integration receipt per the WP-09.90 template.
```

```text
Execute ArcForges delivery task PLT.26 — Token system and theming.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\platform.md (anchor task-plt-26).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/plt-26 (python tools/delivery.py claim PLT.26 --worker <name>); task branch task/plt-26 in DesktopPlatform; ledger record ledger/tasks/plt-26.md.
Kind/size: producer/M. Baseline: not-started.
Outcome: Semantic tokens for colour/typography/spacing/radius/elevation/motion with light/dark/high-contrast themes and first-class density modes; no component references a raw literal.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-10.00 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\10-design-system-and-desktop-shell.md, anchor rule-wp-10.00
- WP-10:reconciliation-of-the-five-legacy-src-bu Reconciliation of the five legacy src/BuildingBlocks/ArcForges.Desktop.{Experience,Graphics,Preview,RichContent,Text} scaffold projects per WP-01.02 into DesignSystem/Shell (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\10-design-system-and-desktop-shell.md, package-level obligation

Entry condition: adoption slice ADOPT.02.platform is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] PRF.01: a proven Avalonia Native AOT publish with zero trim/AOT diagnostics
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:src/DesignSystem/ArcForges.DesignSystem/**
Shared resources (follow the owner protocol): RES-desktopplatform-build-config (append): Solution/project lists, central package versions and CI job lists are appended by the task that adds a project, dependency or job; dependency additions follow the dependency-admission policy with a reviewed receipt; lock files are regenerated after rebase and never hand-merged; the integration owner resolves ordering conflicts at merge.
Unblocks: NOTES.03, NOTES.04, PLT.27, PLT.29, PLT.31, PLT.35

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline tests: policy test asserting no raw colour/size literal in component code; contrast tests across every theme; density snapshot suite. Real AOT publish-with-zero-diagnostics evidence is local opt-in, recorded at PLT.34/PLT.35.
Completion evidence for the ledger: Raw-literal policy result and contrast reports per theme.
```

```text
Execute ArcForges delivery task PLT.27 — Windows, panels and layout.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\platform.md (anchor task-plt-27).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/plt-27 (python tools/delivery.py claim PLT.27 --worker <name>); task branch task/plt-27 in DesktopPlatform; ledger record ledger/tasks/plt-27.md.
Kind/size: producer/L. Baseline: not-started.
Outcome: Multi-window-per-instance window model, dockable/collapsible panel host, device-local layout persistence resilient to a missing panel or changed screen configuration.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-10.01 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\10-design-system-and-desktop-shell.md, anchor rule-wp-10.01
- WP-10:reconciliation-of-the-five-legacy-src-bu Reconciliation of the five legacy src/BuildingBlocks/ArcForges.Desktop.{Experience,Graphics,Preview,RichContent,Text} scaffold projects per WP-01.02 into DesignSystem/Shell (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\10-design-system-and-desktop-shell.md, package-level obligation

Entry condition: adoption slice ADOPT.02.platform is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] PLT.26: token system
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:src/DesignSystem/ArcForges.Desktop.Shell/**
Shared resources (follow the owner protocol): RES-desktopplatform-build-config (append): Solution/project lists, central package versions and CI job lists are appended by the task that adds a project, dependency or job; dependency additions follow the dependency-admission policy with a reviewed receipt; lock files are regenerated after rebase and never hand-merged; the integration owner resolves ordering conflicts at merge.
Unblocks: NOTES.03, NOTES.04, NOTES.05, PLT.28, PLT.30, PLT.33, PLT.35, SLATE.22, SLATE.25

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline tests: restore tests across missing panel, changed display arrangement, corrupted layout state; device-local assertion.
Completion evidence for the ledger: Layout restore matrix.
```

```text
Execute ArcForges delivery task PLT.28 — Command system.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\platform.md (anchor task-plt-28).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/plt-28 (python tools/delivery.py claim PLT.28 --worker <name>); task branch task/plt-28 in DesktopPlatform; ledger record ledger/tasks/plt-28.md.
Kind/size: producer/M. Baseline: not-started.
Outcome: Command registry with availability, shortcut binding, command palette and conflict detection; command availability is computed from the same evaluation the capability model uses so command and capability never disagree.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-10.02 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\10-design-system-and-desktop-shell.md, anchor rule-wp-10.02

Entry condition: adoption slice ADOPT.02.platform is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] PLT.27: window/panel host
- [artifact] PLT.20: capability availability evaluation (WP-09.03)
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:src/DesignSystem/ArcForges.Desktop.Shell/**
Unblocks: PLT.32, PLT.35, SLATE.22

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline tests: shortcut conflict detection; availability agreement tests against the capability model; palette search relevance tests.
Completion evidence for the ledger: Shortcut conflict and availability agreement results.
Notes: The old WP-10 header claims upstream '06, 09' for the whole package. Only this substep genuinely needs WP-09; PLT.26/27/29/30/31/32/33/34 do not.
```

```text
Execute ArcForges delivery task PLT.29 — Scoped settings.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\platform.md (anchor task-plt-29).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/plt-29 (python tools/delivery.py claim PLT.29 --worker <name>); task branch task/plt-29 in DesktopPlatform; ledger record ledger/tasks/plt-29.md.
Kind/size: producer/M. Baseline: not-started.
Outcome: Fixed scope resolution (application/workspace/device/instance), typed schemas, migration on schema change, explainable effective value; device-scoped settings never sync.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-10.03 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\10-design-system-and-desktop-shell.md, anchor rule-wp-10.03

Entry condition: adoption slice ADOPT.02.platform is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] PLT.26: token/theming groundwork
- [artifact] PLT.04: migration runner pattern (WP-07.03)
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:src/DesignSystem/ArcForges.Desktop.Shell/**
Unblocks: PLT.35

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline tests: resolution order tests across every scope combination; explainability tests; migration test.
Completion evidence for the ledger: Settings resolution and explainability results.
```

```text
Execute ArcForges delivery task PLT.30 — Attention and notification model.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\platform.md (anchor task-plt-30).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/plt-30 (python tools/delivery.py claim PLT.30 --worker <name>); task branch task/plt-30 in DesktopPlatform; ledger record ledger/tasks/plt-30.md.
Kind/size: producer/M. Baseline: not-started.
Outcome: Attention items classified by durability; a durable item (pending approval, failed task) persists until resolved regardless of a missed transient notification; lock-screen/system-notification content is non-sensitive by default.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-10.04 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\10-design-system-and-desktop-shell.md, anchor rule-wp-10.04

Entry condition: adoption slice ADOPT.02.platform is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] PLT.27: window/panel host
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:src/DesignSystem/ArcForges.Desktop.Shell/**
Unblocks: PLT.35

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline tests: missed-notification test asserting durable state survives; sensitivity test on notification content.
Completion evidence for the ledger: Missed-notification durability result.
```

```text
Execute ArcForges delivery task PLT.31 — Error presentation.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\platform.md (anchor task-plt-31).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/plt-31 (python tools/delivery.py claim PLT.31 --worker <name>); task branch task/plt-31 in DesktopPlatform; ledger record ledger/tasks/plt-31.md.
Kind/size: producer/S. Baseline: not-started.
Outcome: Errors are presented from the reason-code registry with a human-readable statement, retry guidance and a support reference identifier; a raw exception message never reaches the user.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-10.05 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\10-design-system-and-desktop-shell.md, anchor rule-wp-10.05

Entry condition: adoption slice ADOPT.02.platform is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] PLT.26: token system
- [artifact] FND.05: reason-code registry
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:src/DesignSystem/ArcForges.Desktop.Shell/**
Unblocks: PLT.35, PLT.52

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline tests: no raw exception text displayed; coverage that every registered reason code has a message.
Completion evidence for the ledger: Raw-exception prohibition and reason-code coverage.
```

```text
Execute ArcForges delivery task PLT.32 — Lifecycle, menus and shutdown.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\platform.md (anchor task-plt-32).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/plt-32 (python tools/delivery.py claim PLT.32 --worker <name>); task branch task/plt-32 in DesktopPlatform; ledger record ledger/tasks/plt-32.md.
Kind/size: producer/M. Baseline: not-started.
Outcome: Start-up sequence within budget; single-instance routing; shutdown prompts stating consequences when work is running/unsaved; menu contribution from the command registry.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-10.06 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\10-design-system-and-desktop-shell.md, anchor rule-wp-10.06

Entry condition: adoption slice ADOPT.02.platform is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] PLT.28: command registry
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:src/DesignSystem/ArcForges.Desktop.Shell/**
Unblocks: APP.07, PLT.35, SCOPE.09, UPD.03

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline tests: startup budget measurement per product host (local perf harness, not hosted CI); shutdown-during-work test; single-instance routing test.
Completion evidence for the ledger: Startup budget measurements and shutdown-during-work result.
```

```text
Execute ArcForges delivery task PLT.33 — Accessibility and localisation baseline.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\platform.md (anchor task-plt-33).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/plt-33 (python tools/delivery.py claim PLT.33 --worker <name>); task branch task/plt-33 in DesktopPlatform; ledger record ledger/tasks/plt-33.md.
Kind/size: producer/L. Baseline: not-started.
Outcome: Every shell surface carries assistive-technology semantics, correct focus order and keyboard reachability; all strings externalised; RTL layout supported structurally.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-10.07 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\10-design-system-and-desktop-shell.md, anchor rule-wp-10.07

Entry condition: adoption slice ADOPT.02.platform is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] PLT.27: window/panel/layout
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:src/DesignSystem/ArcForges.Desktop.Shell/**; DesktopPlatform:tests/DesktopUiTests/**
Shared resources (follow the owner protocol): RES-desktopplatform-build-config (append): Solution/project lists, central package versions and CI job lists are appended by the task that adds a project, dependency or job; dependency additions follow the dependency-admission policy with a reviewed receipt; lock files are regenerated after rebase and never hand-merged; the integration owner resolves ordering conflicts at merge.
Unblocks: PLT.35

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline automated accessibility checks plus pseudo-localisation pass and RTL layout pass run in CI; the dated manual assistive-technology verification is explicit local opt-in per P2-017 (device/GUI testing is excluded from hosted CI).
Completion evidence for the ledger: Accessibility automated plus dated manual record; pseudo-localisation report.
```

```text
Execute ArcForges delivery task PLT.34 — Third-party control admission.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\platform.md (anchor task-plt-34).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/plt-34 (python tools/delivery.py claim PLT.34 --worker <name>); task branch task/plt-34 in DesktopPlatform; ledger record ledger/tasks/plt-34.md.
Kind/size: producer/M. Baseline: not-started.
Outcome: Every third-party control the shell uses passes a real AOT publish proof with zero diagnostics before adoption, with a recorded licence position per control.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-10.08 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\10-design-system-and-desktop-shell.md, anchor rule-wp-10.08

Entry condition: adoption slice ADOPT.02.platform is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] PRF.01: the established AOT-publish-with-zero-diagnostics harness/process
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:src/DesignSystem/**; DesktopPlatform:docs/**
Unblocks: PLT.35, PRF.09

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Per-control real AOT publish proof - genuinely requires local/CI compilation (Windows/Linux AOT publish IS in the retained CI scope per P2-017), so this can run in CI unlike device/GUI checks.
Completion evidence for the ledger: Per-control AOT proofs and licence records.
```

```text
Execute ArcForges delivery task PLT.35 — Publish DesignSystem/Shell packages and verify real integration.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\platform.md (anchor task-plt-35).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/plt-35 (python tools/delivery.py claim PLT.35 --worker <name>); task branch task/plt-35 in DesktopPlatform; ledger record ledger/tasks/plt-35.md.
Kind/size: acceptance/S. Baseline: not-started.
Outcome: ArcForges.DesignSystem and ArcForges.Desktop.Shell are packed, admitted, published, and independently consumed; each app is shown to restore only the packages/mechanisms it needs.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-10.90 (all work except the parts mapped to PLT.56): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\10-design-system-and-desktop-shell.md, anchor rule-wp-10.90

Entry condition: adoption slice ADOPT.02.platform is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] PLT.26: tokens
- [artifact] PLT.27: windows/panels
- [artifact] PLT.28: commands
- [artifact] PLT.29: settings
- [artifact] PLT.30: attention
- [artifact] PLT.31: error presentation
- [artifact] PLT.32: lifecycle/menus
- [artifact] PLT.33: a11y/l10n
- [artifact] PLT.34: control admission
Completion prerequisites (may start earlier; cannot complete before these are complete):
- [integration] PLT.56: ArcNotes actually composing the shell for its own product UI

Permitted write scope: DesktopPlatform:eng/packaging/packages.json
Shared resources (follow the owner protocol): RES-desktopplatform-package-inventory (append): Each producer task adds its own package entry; every merge to main packs and publishes all packages at one version; consumers pin the candidate produced by the merge of the capability they need, never waiting for a package closure task; one merge queue.
Unblocks: PLT.56

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): P2-017: offline verify/policy tests plus the retained AOT-publish gate.
Completion evidence for the ledger: Owned artifact and real-integration receipt per WP-10.90.
```

```text
Execute ArcForges delivery task PLT.36 — Principals and the actor chain.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\platform.md (anchor task-plt-36).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/plt-36 (python tools/delivery.py claim PLT.36 --worker <name>); task branch task/plt-36 in DesktopPlatform; ledger record ledger/tasks/plt-36.md.
Kind/size: producer/M. Baseline: not-started.
Outcome: Every operation carries a complete actor chain (human principal, device, installation, session, any acting agent/extension) constructed once at the entry point and flowing through every layer without reconstruction; no operation reaches an enforcement point without it.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-11.00 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\11-security-foundation.md, anchor rule-wp-11.00

Entry condition: adoption slice ADOPT.02.platform is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] FND.01: identity primitive types
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:src/BuildingBlocks/ArcForges.Security/**
Unblocks: PLT.38, PLT.40, PLT.44, PLT.46

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline unit tests: propagation test asserting the chain survives every hop including queue/process boundaries; completeness test.
Completion evidence for the ledger: Actor chain propagation and completeness results.
```

```text
Execute ArcForges delivery task PLT.37 — Risk model and classification.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\platform.md (anchor task-plt-37).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/plt-37 (python tools/delivery.py claim PLT.37 --worker <name>); task branch task/plt-37 in DesktopPlatform; ledger record ledger/tasks/plt-37.md.
Kind/size: producer/M. Baseline: not-started.
Outcome: R0 to R4 with runtime modifiers; every capability declares a base risk; modifiers raise it based on scope/target/reversibility/egress/actor kind; effective risk is computed, explainable and monotonic (never lowered).

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-11.01 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\11-security-foundation.md, anchor rule-wp-11.01

Entry condition: adoption slice ADOPT.02.platform is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] PLT.19: CapabilityDescriptor carrying risk level/trust requirement/side-effect class (WP-09.02)
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:src/BuildingBlocks/ArcForges.Security/**
Unblocks: PLT.38, PLT.39, PLT.46

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline unit tests: classification tests across every modifier combination; monotonicity test.
Completion evidence for the ledger: Risk classification and monotonicity matrix.
```

```text
Execute ArcForges delivery task PLT.38 — Decision pipeline and the four enforcement points.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\platform.md (anchor task-plt-38).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/plt-38 (python tools/delivery.py claim PLT.38 --worker <name>); task branch task/plt-38 in DesktopPlatform; ledger record ledger/tasks/plt-38.md.
Kind/size: producer/L. Baseline: not-started.
Outcome: The fourteen-step decision pipeline implemented once and invoked at each of the four enforcement points (caller pre-check, transport boundary, service-side decision, owner-side final validation always last); every step produces a typed outcome; a refusal names the failing step and reason code; the pipeline is unbypassable.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-11.02 (all work except the parts mapped to PLT.57): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\11-security-foundation.md, anchor rule-wp-11.02

Entry condition: adoption slice ADOPT.02.platform is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] PLT.36: actor chain
- [artifact] PLT.37: risk model
- [artifact] PLT.10: LocalRpc session handshake (WP-08.01/08.02)
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:src/BuildingBlocks/ArcForges.Security/**; DesktopPlatform:src/BuildingBlocks/ArcForges.Capabilities/**
Shared resources (follow the owner protocol): RES-assistant-store-schema (append): Numbered migrations are allocated at merge by the integration owner (a rebase renumbers pending migrations); each migration is forward-only with its recovery and downgrade-refusal tests; no task edits a merged migration.; RES-desktopplatform-policy-data (append): Generated policy data is regenerated from its pinned source and never hand-edited; the reason-code registry is append-only with stable codes; each task adds its own test classes and evidence rows.
Unblocks: APP.02, GOV.16, PLT.41, PLT.43, PLT.46, PLT.57

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline unit tests: step-coverage test asserting every step runs; refusal matrix producing a distinct reason code per failing step; bypass test.
Completion evidence for the ledger: Pipeline bypass, step-coverage and refusal matrix.
```

```text
Execute ArcForges delivery task PLT.39 — Approval, steering and step-up.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\platform.md (anchor task-plt-39).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/plt-39 (python tools/delivery.py claim PLT.39 --worker <name>); task branch task/plt-39 in DesktopPlatform; ledger record ledger/tasks/plt-39.md.
Kind/size: producer/L. Baseline: not-started.
Outcome: Approval requests with bounded lifetime, durable pending state and explicit outcome; steering adjusts a running operation without granting authority; step-up challenges for enumerated sensitive operations; local presence required for the highest risk class, biometric app-unlock never substituting.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-11.03 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\11-security-foundation.md, anchor rule-wp-11.03

Entry condition: adoption slice ADOPT.02.platform is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] PLT.37: risk model
- [artifact] PLT.01: durable persistence for the approval object
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:src/BuildingBlocks/ArcForges.Security/**
Unblocks: APP.05, AST.12, DEV.06, EXE.06, PLT.46

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline tests: approval expiry, duplicate-approval, approval-after-cancel tests; steering-cannot-escalate test; biometric-does-not-satisfy-step-up test. Real OS biometric/local-presence hardware evidence is local opt-in.
Completion evidence for the ledger: Approval, steering and step-up results.
```

```text
Execute ArcForges delivery task PLT.40 — Per-application secrets and session isolation.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\platform.md (anchor task-plt-40).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/plt-40 (python tools/delivery.py claim PLT.40 --worker <name>); task branch task/plt-40 in DesktopPlatform; ledger record ledger/tasks/plt-40.md.
Kind/size: producer/L. Baseline: not-started.
Outcome: Platform secure storage/broker primitives scoped to realm/account/product/installation with no cross-product SSO endpoint; SecretRef Use != Reveal; connector child grants are foreground/definition-bound and cannot export raw secrets; own sign-out leaves other apps/local data intact.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-11.04 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\11-security-foundation.md, anchor rule-wp-11.04
- WP-11:application-credential-boundary-shared-s Application credential boundary: shared security packages use the caller application/installation storage namespace; deny sibling credential reads; no device-SSO signing broker (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\11-security-foundation.md, package-level obligation

Entry condition: adoption slice ADOPT.02.platform is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] PLT.36: actor chain
Completion prerequisites (may start earlier; cannot complete before these are complete):
- [integration] CLOUD.18: real Cloud authentication

Permitted write scope: DesktopPlatform:src/BuildingBlocks/ArcForges.Security.Secrets/**
Shared resources (follow the owner protocol): RES-desktopplatform-build-config (append): Solution/project lists, central package versions and CI job lists are appended by the task that adds a project, dependency or job; dependency additions follow the dependency-admission policy with a reviewed receipt; lock files are regenerated after rebase and never hand-merged; the integration owner resolves ordering conflicts at merge.
Unblocks: CLOUD.18, PLT.46, PLT.49, UPD.01

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline tests where possible; real OS secure-storage round trips (Windows Credential Manager/keychain/keystore) are local opt-in per platform, recorded separately from CI.
Completion evidence for the ledger: Secret structural prohibitions and platform round-trip results.
```

```text
Execute ArcForges delivery task PLT.41 — Egress control.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\platform.md (anchor task-plt-41).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/plt-41 (python tools/delivery.py claim PLT.41 --worker <name>); task branch task/plt-41 in DesktopPlatform; ledger record ledger/tasks/plt-41.md.
Kind/size: producer/M. Baseline: not-started.
Outcome: Every outbound data transfer is its own egress decision, distinct from read access, recording data class/destination/authority; a denied egress produces a typed refusal and every egress is audited.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-11.05 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\11-security-foundation.md, anchor rule-wp-11.05

Entry condition: adoption slice ADOPT.02.platform is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] PLT.38: decision pipeline
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:src/BuildingBlocks/ArcForges.Security/**
Unblocks: APP.06, PLT.46

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline tests: matrix asserting read access alone never authorizes egress; destination allowlist tests; audit assertion.
Completion evidence for the ledger: Egress authorization matrix and audit assertions.
```

```text
Execute ArcForges delivery task PLT.42 — Instruction provenance.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\platform.md (anchor task-plt-42).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/plt-42 (python tools/delivery.py claim PLT.42 --worker <name>); task branch task/plt-42 in DesktopPlatform; ledger record ledger/tasks/plt-42.md.
Kind/size: producer/L. Baseline: not-started.
Outcome: Every input that can carry instructions (model output, extension output, retrieved content, imported documents, deep links, catalog metadata) is marked with its provenance; untrusted provenance can be processed but never gains authority to trigger an operation unapproved.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-11.06 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\11-security-foundation.md, anchor rule-wp-11.06

Entry condition: adoption slice ADOPT.02.platform is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] PLT.21: context freezing (WP-09.04)
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:src/BuildingBlocks/ArcForges.Security/**
Unblocks: AST.05, PLT.46

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline tests: injection corpus asserting untrusted content cannot cause an unapproved operation; marking-completeness test over every input path.
Completion evidence for the ledger: Injection corpus results and marking coverage.
```

```text
Execute ArcForges delivery task PLT.43 — Capability leases and trust.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\platform.md (anchor task-plt-43).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/plt-43 (python tools/delivery.py claim PLT.43 --worker <name>); task branch task/plt-43 in DesktopPlatform; ledger record ledger/tasks/plt-43.md.
Kind/size: producer/M. Baseline: not-started.
Outcome: A delegation creates a lease with scope/expiry/revocation, enforced at use not only at issue; typed trust levels evaluated at defined points; trust never substitutes for permission.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-11.07 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\11-security-foundation.md, anchor rule-wp-11.07

Entry condition: adoption slice ADOPT.02.platform is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] PLT.38: decision pipeline
- [artifact] PLT.01: durable persistence for lease state
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:src/BuildingBlocks/ArcForges.Security/**
Unblocks: DEV.03, PLT.46

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline tests: lease expiry-at-use, revocation-mid-operation, scope-escalation-attempt tests; trust-never-grants-permission test.
Completion evidence for the ledger: Lease expiry, revocation and trust-separation results.
```

```text
Execute ArcForges delivery task PLT.44 — Append-only audit subsystem.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\platform.md (anchor task-plt-44).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/plt-44 (python tools/delivery.py claim PLT.44 --worker <name>); task branch task/plt-44 in DesktopPlatform; ledger record ledger/tasks/plt-44.md.
Kind/size: producer/M. Baseline: not-started.
Outcome: Append-only audit append/query with a dedicated policy-retention maintenance authority; ordinary roles cannot UPDATE/DELETE; audited retention purge removes only expired unheld partitions under declared policy; complete separation from telemetry.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-11.08 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\11-security-foundation.md, anchor rule-wp-11.08

Entry condition: adoption slice ADOPT.02.platform is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] PLT.36: actor chain
- [artifact] PLT.01: persistence write path
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:src/BuildingBlocks/ArcForges.Security.Audit/**
Shared resources (follow the owner protocol): RES-desktopplatform-build-config (append): Solution/project lists, central package versions and CI job lists are appended by the task that adds a project, dependency or job; dependency additions follow the dependency-admission policy with a reviewed receipt; lock files are regenerated after rebase and never hand-merged; the integration owner resolves ordering conflicts at merge.
Unblocks: PLT.46

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline tests: reject ordinary UPDATE/DELETE and forged retention role; approved expiry purge; legal hold; complete security events; telemetry separation test (also exercised jointly with PLT.49's redaction/separation evidence).
Completion evidence for the ledger: Audit immutability, completeness and separation results.
```

```text
Execute ArcForges delivery task PLT.45 — Content helper and OS-enforced isolation (ContentSandbox host).

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\platform.md (anchor task-plt-45).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/plt-45 (python tools/delivery.py claim PLT.45 --worker <name>); task branch task/plt-45 in DesktopPlatform; ledger record ledger/tasks/plt-45.md.
Kind/size: producer/XL. Baseline: not-started.
Outcome: The first-party C# Native AOT ContentSandbox, generated gRPC broker/control bindings and all restricted RID launch profiles (Windows AppContainer+Job Object, Linux Landlock+seccomp, macOS App-Sandbox+XPC handoff) are built and solely owned here; ContentSandbox.Contracts/.Broker and the foundation Runtime.<rid> are published before WP13 consumes them; OS containment is proven with a deliberately hostile first-party test parser. Production PDF/image/media/OTIO libraries are WP13's job, never an upstream input here.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-11.09 (full; production ContentSandbox helper, real transport): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\11-security-foundation.md, anchor rule-wp-11.09
- WP-11:local-grpc-closure-ss7-own-actual-signed Local gRPC closure (SS7): own actual signed restricted gRPC helper, launch-secret/OS-descriptor allowlist, hostile-fixture containment, private-copy/digest validation, ConnectorBroker security boundary (real connector providers are WP41) (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\11-security-foundation.md, package-level obligation

Entry condition: adoption slice ADOPT.02.platform is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] PLT.15: LocalRpc brokered large-data mechanism (WP-08.06)
- [artifact] PLT.09: LocalRpc transport/restricted launch identity (WP-08.00/08.01)
- [contract] CON.04: ArcForges.Contracts.LocalRpc.Sandbox generated ContentSandboxService/session/grant schema
Completion prerequisites (may start earlier; cannot complete before these are complete):
- [integration] NAT.14: production PDF/image/media/OTIO parser composition rebuilt and signed on top of this same helper

Permitted write scope: DesktopPlatform:src/DesktopHelpers/ArcForges.ContentSandbox.Broker/**; DesktopPlatform:src/DesktopHelpers/ArcForges.ContentSandbox.Contracts/**; DesktopPlatform:src/DesktopHelpers/ArcForges.ContentSandbox/**
Shared resources (follow the owner protocol): RES-desktopplatform-policy-data (append): Generated policy data is regenerated from its pinned source and never hand-edited; the reason-code registry is append-only with stable codes; each task adds its own test classes and evidence rows.
Permitted substitutes (never real integration evidence): SUB-hostile-test-parser: OS-level containment mechanics only (AppContainer/Job Object, Landlock/seccomp, App-Sandbox/XPC denial, resource bounds, crash/hang/parent-death cleanup) against a deliberately hostile FIRST-PARTY test parser, not real format-parsing correctness Real producer ['NAT.14']; removed by PLT.54
Unblocks: EXT.00, NAT.11, NAT.14, NAT.25, NOTES.09, NOTES.37, PLT.15, PLT.46, PLT.54

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): P2-017 CRITICAL NUANCE: static/offline unit and policy tests run in CI, but the actual required evidence - real OS containment (AppContainer/Job Object denial, Landlock/seccomp denial, App-Sandbox/XPC denial, native crash/hang/memory-exhaustion/parent-death cleanup) - is device/OS-level execution that P2-017 explicitly excludes from hosted CI ('no macOS CI; no CI for... desktop GUI... sandbox execution'). This evidence MUST be recorded as local opt-in runs on each supported RID, per the ci-and-local-validation-policy.md and the architecture 24 rule 'a mocked launcher or same-user unrestricted child satisfies this gate: never'.
Completion evidence for the ledger: Real child attempts at product-DB/token reads, outbound TCP/UDP/loopback, sibling-process access, spawn escape, oversized output; OS denial, resource bounds and parent-death cleanup on every supported RID.
Notes: This is the single highest-stakes early risk proof in the desktop platform foundation: PG-22 explicitly states a mocked launcher or unrestricted same-user child cannot close the gate, and the failure mode (hostile parsing escaping containment) would invalidate downstream trust in every product that later touches untrusted content (Notes PDF, Slate media/OTIO, extensions). Recommend prioritising this alongside PLT.03 (persistence recovery). Merged duplicate integration or closure task formerly proposed as CON.96.
```

```text
Execute ArcForges delivery task PLT.46 — Publish Security packages and verify real integration.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\platform.md (anchor task-plt-46).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/plt-46 (python tools/delivery.py claim PLT.46 --worker <name>); task branch task/plt-46 in DesktopPlatform; ledger record ledger/tasks/plt-46.md.
Kind/size: acceptance/M. Baseline: not-started.
Outcome: ArcForges.Security,.Security.Secrets and.Security.Audit are packed, admitted, published and independently consumed; the signed parent-bound helper and OS broker are packaged with only this stage's dependencies and the test-only parser fixture, no dependency back on WP13.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-11.90 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\11-security-foundation.md, anchor rule-wp-11.90

Entry condition: adoption slice ADOPT.02.platform is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] PLT.36: actor chain
- [artifact] PLT.37: risk model
- [artifact] PLT.38: decision pipeline
- [artifact] PLT.39: approval/step-up
- [artifact] PLT.40: secrets/session isolation
- [artifact] PLT.41: egress control
- [artifact] PLT.42: instruction provenance
- [artifact] PLT.43: leases/trust
- [artifact] PLT.44: audit
- [artifact] PLT.45: content helper isolation
- [artifact] PLT.54: package task delivered
- [artifact] PLT.57: package task delivered
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:eng/packaging/packages.json
Shared resources (follow the owner protocol): RES-desktopplatform-package-inventory (append): Each producer task adds its own package entry; every merge to main packs and publishes all packages at one version; consumers pin the candidate produced by the merge of the capability they need, never waiting for a package closure task; one merge queue.

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): P2-017: offline verify/policy tests in CI; the real OS-isolation matrix (PLT.45's evidence) is local opt-in, recorded and cross-referenced here rather than re-run.
Completion evidence for the ledger: Cross-boundary owner refusal, stale approval/revocation, secrets/redaction and real OS-isolation tests per WP-11.90.
```

```text
Execute ArcForges delivery task PLT.47 — Emission and required dimensions.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\platform.md (anchor task-plt-47).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/plt-47 (python tools/delivery.py claim PLT.47 --worker <name>); task branch task/plt-47 in DesktopPlatform; ledger record ledger/tasks/plt-47.md.
Kind/size: producer/M. Baseline: not-started.
Outcome: A single emission surface for metrics/traces/structured logs with the required dimension set attached automatically from ambient context; a present dimension is always attached, an absent one omitted rather than defaulted; build identifier and instance identity are on every signal.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-12.00 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\12-observability-foundation.md, anchor rule-wp-12.00

Entry condition: adoption slice ADOPT.02.platform is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] FND.01: identity primitive types (instance identity, build id)
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:src/BuildingBlocks/ArcForges.Observability/**
Unblocks: PLT.48, PLT.53, UPD.06

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline tests: dimension-coverage test across representative operations; absent-dimension-omitted test.
Completion evidence for the ledger: Dimension coverage report.
```

```text
Execute ArcForges delivery task PLT.48 — Correlation and causation propagation.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\platform.md (anchor task-plt-48).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/plt-48 (python tools/delivery.py claim PLT.48 --worker <name>); task branch task/plt-48 in DesktopPlatform; ledger record ledger/tasks/plt-48.md.
Kind/size: producer/M. Baseline: not-started.
Outcome: Correlation created at the originating edge or accepted from a validated client value, propagated across HTTP/queue/worker/realtime/provider calls once, in shared infrastructure; causation records which operation caused which; a user-visible task/run identifier resolves to its trace.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-12.01 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\12-observability-foundation.md, anchor rule-wp-12.01

Entry condition: adoption slice ADOPT.02.platform is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] PLT.47: emission surface
Completion prerequisites (may start earlier; cannot complete before these are complete):
- [integration] CLOUD.01: a real Cloud hop to prove the full HTTP/queue/worker/realtime/provider chain

Permitted write scope: DesktopPlatform:src/BuildingBlocks/ArcForges.Observability/**
Unblocks: PLT.53

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline tests: synthetic end-to-end action producing one connected trace across available local hop kinds; resolution test from task identifier to trace; validation test rejecting malformed client-supplied correlation.
Completion evidence for the ledger: A single connected trace across every available hop kind.
```

```text
Execute ArcForges delivery task PLT.49 — Redaction by construction.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\platform.md (anchor task-plt-49).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/plt-49 (python tools/delivery.py claim PLT.49 --worker <name>); task branch task/plt-49 in DesktopPlatform; ledger record ledger/tasks/plt-49.md.
Kind/size: producer/L. Baseline: not-started.
Outcome: Secret-bearing and content types have no logging representation; a scrubbing processor removes known-sensitive header/field names as a second line of defence; URLs recorded as route templates plus identifiers; exception messages mapped to reason codes before export.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-12.02 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\12-observability-foundation.md, anchor rule-wp-12.02
- WP-12:eng-policy-telemetry-policy-json-creatio eng/policy/telemetry-policy.json creation: dimension allowlist, metric label allowlist, sampling and retention configuration (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\12-observability-foundation.md, package-level obligation

Entry condition: adoption slice ADOPT.02.platform is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] PLT.40: SecretRef type with no accessible string representation
- [artifact] FND.05: reason-code registry
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:src/BuildingBlocks/ArcForges.Observability/**; DesktopPlatform:eng/policy/telemetry-policy.json
Unblocks: PLT.50, PLT.52, PLT.53

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline tests: marker values injected as headers/tokens/prompts/note-content/file-paths must never appear in exported signals; structural test that content types cannot be logged. This is exactly PG-05's own evidence requirement, run offline against a local test exporter, not a live telemetry backend.
Completion evidence for the ledger: Marker-injection redaction report, zero findings - satisfies PG-05.
```

```text
Execute ArcForges delivery task PLT.50 — Cardinality and sampling.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\platform.md (anchor task-plt-50).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/plt-50 (python tools/delivery.py claim PLT.50 --worker <name>); task branch task/plt-50 in DesktopPlatform; ledger record ledger/tasks/plt-50.md.
Kind/size: producer/M. Baseline: not-started.
Outcome: Metric labels and bounded trace policy enforced from observability architecture SS13: head sample plus bounded diagnostic buffer, error/slow promotion only for spans still retained, explicit overflow/loss counters; unsampled mandatory error facts remain redacted under consent.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-12.03 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\12-observability-foundation.md, anchor rule-wp-12.03
- WP-12:eng-policy-telemetry-policy-json-creatio eng/policy/telemetry-policy.json creation: dimension allowlist, metric label allowlist, sampling and retention configuration (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\12-observability-foundation.md, package-level obligation

Entry condition: adoption slice ADOPT.02.platform is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] PLT.49: redaction processor
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:src/BuildingBlocks/ArcForges.Observability/**; DesktopPlatform:eng/policy/telemetry-policy.json
Unblocks: PLT.53

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline tests: cardinality negative fixture, sampled/unsampled error, slow-span buffer expiry, overflow and disabled-consent tests.
Completion evidence for the ledger: Cardinality negative fixture and sampling retention results.
```

```text
Execute ArcForges delivery task PLT.51 — Health probes.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\platform.md (anchor task-plt-51).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/plt-51 (python tools/delivery.py claim PLT.51 --worker <name>); task branch task/plt-51 in DesktopPlatform; ledger record ledger/tasks/plt-51.md.
Kind/size: producer/S. Baseline: not-started.
Outcome: Liveness, readiness and capability health as three distinct probe kinds; readiness fails closed on a missing required dependency; capability health uses the five health dimensions (reachable, ready, healthy, degraded, capacity) shared with the contract model.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-12.04 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\12-observability-foundation.md, anchor rule-wp-12.04

Entry condition: adoption slice ADOPT.02.platform is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] PLT.23: HealthDimension type (WP-09.06)
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:src/BuildingBlocks/ArcForges.Observability/**
Unblocks: PLT.53

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline tests: dependency-outage test asserting readiness fails closed; capability-health test reflecting simulated degradation.
Completion evidence for the ledger: Health probe fail-closed and degradation results.
```

```text
Execute ArcForges delivery task PLT.52 — Desktop diagnostics and consent.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\platform.md (anchor task-plt-52).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/plt-52 (python tools/delivery.py claim PLT.52 --worker <name>); task branch task/plt-52 in DesktopPlatform; ledger record ledger/tasks/plt-52.md.
Kind/size: producer/L. Baseline: not-started.
Outcome: Local diagnostics always available without upload; three tiers (minimal always-on local, user-approved report, time-bounded self-disabling verbose session visible while active); a report is generated, shown in full, sent only after approval; no memory dump by default; consent is revocable and stops collection immediately and locally.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-12.05 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\12-observability-foundation.md, anchor rule-wp-12.05

Entry condition: adoption slice ADOPT.02.platform is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] PLT.31: error presentation shell surface (WP-10.05)
- [artifact] PLT.49: redaction
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:src/BuildingBlocks/ArcForges.Observability.Desktop/**
Shared resources (follow the owner protocol): RES-desktopplatform-build-config (append): Solution/project lists, central package versions and CI job lists are appended by the task that adds a project, dependency or job; dependency additions follow the dependency-admission policy with a reviewed receipt; lock files are regenerated after rebase and never hand-merged; the integration owner resolves ordering conflicts at merge.
Unblocks: PLT.53

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline tests: consent-absent test asserting no signal leaves the device; crash test asserting no automatic upload; verbose-session expiry test; revocation test. All runnable as local simulated-consent-state tests, no live telemetry backend needed.
Completion evidence for the ledger: Consent-absent, crash-approval, verbose-expiry and revocation results.
```

```text
Execute ArcForges delivery task PLT.53 — Publish Observability packages and verify real integration.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\platform.md (anchor task-plt-53).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/plt-53 (python tools/delivery.py claim PLT.53 --worker <name>); task branch task/plt-53 in DesktopPlatform; ledger record ledger/tasks/plt-53.md.
Kind/size: acceptance/S. Baseline: not-started.
Outcome: ArcForges.Observability and.Observability.Desktop are packed, admitted, published and independently consumed; a trace can join one request across owners without logging prompts/credentials/unbounded payloads; health distinguishes backend/CF/model/R2 failures once those exist.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-12.90 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\12-observability-foundation.md, anchor rule-wp-12.90

Entry condition: adoption slice ADOPT.02.platform is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] PLT.47: emission/dimensions
- [artifact] PLT.48: correlation/causation
- [artifact] PLT.49: redaction
- [artifact] PLT.50: cardinality/sampling
- [artifact] PLT.51: health probes
- [artifact] PLT.52: diagnostics/consent
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:eng/packaging/packages.json
Shared resources (follow the owner protocol): RES-desktopplatform-package-inventory (append): Each producer task adds its own package entry; every merge to main packs and publishes all packages at one version; consumers pin the candidate produced by the merge of the capability they need, never waiting for a package closure task; one merge queue.

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): P2-017: offline verify/policy tests; Cloud-side hop evidence deferred per PLT.48's complete edge.
Completion evidence for the ledger: Owned artifact and real-integration receipt per WP-12.90.
```

```text
Execute ArcForges delivery task PLT.54 — Real hostile-input containment proof with production parser libraries loaded in ContentSandbox.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\platform.md (anchor task-plt-54).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/plt-54 (python tools/delivery.py claim PLT.54 --worker <name>); task branch task/plt-54 in DesktopPlatform; ledger record ledger/tasks/plt-54.md.
Kind/size: integration/M. Baseline: not-started.
Outcome: that PG-12/PG-22's OS isolation mechanics (proven against a first-party hostile test parser in PLT.45) hold once real PDFium/FFmpeg/OpenImageIO/OpenColorIO/OTIO composition is loaded into the same helper by WP-13.13 ; this is the point where the SUB-hostile-test-parser substitute is actually replaced.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-11.09 (containment mechanics re-verified against the real parser closure): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\11-security-foundation.md, anchor rule-wp-11.09
- WP-13.13 (production parser composition and its own containment evidence): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\13-high-risk-technical-probes.md, anchor rule-wp-13.13

Entry condition: adoption slice ADOPT.02.platform is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] PLT.45: real, delivered outcome of PLT.45 (Content helper and OS-enforced isolation (ContentSandbox host))
- [artifact] NAT.14: real, delivered outcome of NAT.14 (Pdf family: PDFium and production parser containment in the WP11 helper (NEW library))
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: 
Unblocks: NAT.30, PLT.46

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Local real-integration run of the affected scenario in an existing environment, recorded once; offline and static checks in CI; no hosted runtime, device, browser, live-service or inference CI (P2-017).
Completion evidence for the ledger: that PG-12/PG-22's OS isolation mechanics (proven against a first-party hostile test parser in PLT.45) hold once real PDFium/FFmpeg/OpenImageIO/OpenColorIO/OTIO composition is loaded into the same helper by WP-13.13 ; this is the point where the SUB-hostile-test-parser substitute is actually replaced.
```

```text
Execute ArcForges delivery task PLT.56 — Three professional products compose the shared DesignSystem/Shell without divergence.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\platform.md (anchor task-plt-56).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/plt-56 (python tools/delivery.py claim PLT.56 --worker <name>); task branch task/plt-56 in DesktopPlatform; ledger record ledger/tasks/plt-56.md.
Kind/size: integration/M. Baseline: not-started.
Outcome: that ArcNotes, ArcScope and ArcSlate each restore only the shell packages/mechanisms they need, feel like one family (shared tokens/commands/settings/attention/error presentation), and that no product had to depend on another to render its own UI (BR-02 of WP10).

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-10.90 (the multi-product consumption evidence beyond a single clean package-only diagnostic): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\10-design-system-and-desktop-shell.md, anchor rule-wp-10.90

Entry condition: adoption slice ADOPT.02.platform is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] PLT.35: real, delivered outcome of PLT.35 (Publish DesignSystem/Shell packages and verify real integration)
- [artifact] NOTES.03: real, delivered outcome of NOTES.03 (Editor interaction: caret, selection, IME composition, markdown-friendly input)
- [artifact] SCOPE.09: real, delivered outcome of SCOPE.09 (Long-running capture in the shell)
- [artifact] SLATE.22: real, delivered outcome of SLATE.22 (Viewer: source and sequence, professional transport)
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: 
Unblocks: PLT.35

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Local real-integration run of the affected scenario in an existing environment, recorded once; offline and static checks in CI; no hosted runtime, device, browser, live-service or inference CI (P2-017).
Completion evidence for the ledger: that ArcNotes, ArcScope and ArcSlate each restore only the shell packages/mechanisms they need, feel like one family (shared tokens/commands/settings/attention/error presentation), and that no product had to depend on another to render its own UI (BR-02 of WP10).
```

```text
Execute ArcForges delivery task PLT.57 — End-to-end capability invocation with real security enforcement inside one product.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\platform.md (anchor task-plt-57).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/plt-57 (python tools/delivery.py claim PLT.57 --worker <name>); task branch task/plt-57 in DesktopPlatform; ledger record ledger/tasks/plt-57.md.
Kind/size: integration/M. Baseline: not-started.
Outcome: that the WP-09.07 invocation pipeline's 'authorize' step, wired to the real WP-11.02 decision pipeline, actually gates a real product capability end to end (resolve -> availability -> freeze -> authorize -> invoke -> validate -> record -> audit), closing the IAuthorizer interface seam both PLT.24 and PLT.38 are built against.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-09.07 (real authorize-step integration): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\09-capability-contribution-and-resource-model.md, anchor rule-wp-09.07
- WP-11.02 (real invocation-pipeline attachment): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\11-security-foundation.md, anchor rule-wp-11.02

Entry condition: adoption slice ADOPT.02.platform is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] PLT.24: real, delivered outcome of PLT.24 (Invocation pipeline)
- [artifact] PLT.38: real, delivered outcome of PLT.38 (Decision pipeline and the four enforcement points)
- [artifact] APP.01: real, delivered outcome of APP.01 (Assistant.Abstractions host ports and application identity)
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: 
Unblocks: PLT.25, PLT.46

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Local real-integration run of the affected scenario in an existing environment, recorded once; offline and static checks in CI; no hosted runtime, device, browser, live-service or inference CI (P2-017).
Completion evidence for the ledger: that the WP-09.07 invocation pipeline's 'authorize' step, wired to the real WP-11.02 decision pipeline, actually gates a real product capability end to end (resolve -> availability -> freeze -> authorize -> invoke -> validate -> record -> audit), closing the IAuthorizer interface seam both PLT.24 and PLT.38 are built against.
```
