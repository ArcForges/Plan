# ArcForges delivery task prompts — Desktop platform mechanisms

Generated from Design `docs/planning/delivery/delivery-graph.json` by `tools/delivery.py`; do not edit by hand.
Each block is self-contained. Claim a task only when `python tools/delivery.py ready` lists it, with
`python tools/delivery.py claim <TASK-ID> --worker <name>`, then follow `arcforges-implementation.md`.
Tasks are ordered by lane for reading; the order is not a schedule.

## Desktop platform mechanisms

```text
Execute ArcForges delivery task PLT.01 — Store abstraction and the single transactional write path.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\platform.md (anchor task-plt-01).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/plt-01 (python tools/delivery.py claim PLT.01 --worker <name>); task branch task/plt-01 in DesktopPlatform; ledger record ledger/tasks/plt-01.md.
Kind/size: producer/L. Baseline: not-started.
Outcome: IStore/CommitUnit/WriteCommand exist with the eight-step write path (validate, authorize, begin commit unit, apply, journal, advance revision, enqueue outbox, commit, notify) implemented exactly once; persistence types never cross the repository boundary; a policy test proves no alternative write path exists.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-07.00 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\07-local-persistence-foundation.md, anchor rule-wp-07.00
- WP-07:content-origin-carrier-projection-commit Content-origin carrier projection committed atomically with payload in the same owner transaction/journal boundary (SS2 required design input) (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\07-local-persistence-foundation.md, package-level obligation

Entry condition: adoption slice ADOPT.02.platform is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] FND.02: CommandId/effect-certainty types
- [artifact] FND.03: Revision type
- [artifact] FND.05: reason-code registry
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:src/BuildingBlocks/ArcForges.Persistence.Sqlite/**
Shared resources (follow the owner protocol): RES-desktopplatform-build-config (append): Solution/project lists, central package versions and CI job lists are appended by the task that adds a project, dependency or job; dependency additions follow the dependency-admission policy with a reviewed receipt; lock files are regenerated after rebase and never hand-merged; the integration owner resolves ordering conflicts at merge.
Unblocks: APP.08, CLOUD.38, FND.02, PLT.05, PLT.07, PLT.08, PLT.39, PLT.43, PLT.44, SCOPE.01

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline unit + integration tests against a real local SQLite file (no external service): policy test asserting no alternative write path, concurrency tests for serialised writes/concurrent reads, boundary test that no storage type appears in an application signature. AOT/trim diagnostics build-breaking since this library is IsAotCompatible.
Completion evidence for the ledger: Single-write-path policy test result.
Notes: Interface-first decoupling recommended: define IJournalWriter/IJournalReader here as the seam PLT.02 implements, so PLT.01 and PLT.02 can be authored in parallel PRs against the same interface rather than serially. Security-exception scope is limited to CA2100 on the internal SqliteReadContext.CreateCommand(string) method in src/BuildingBlocks/ArcForges.Persistence.Sqlite/Store/StoreDatabase.cs. Independent review must establish that every caller supplies literal SQL, a fixed internal identifier, or explicitly trusted owner-authored MigrationStep.Statements, with data values bound as parameters. The SQLite schema authorizer is additional defense, not a sanitizer or permission to accept untrusted SQL. A documented method-only suppression may cover this demonstrated statement-factory false positive; no file-wide, project-wide or repository-wide suppression, new caller trust, or weakened authorizer is authorized. Fix any real injection finding instead; retain targeted offline migration/journal tests and all other security diagnostics. Retain strict boundary negatives for untrusted data, forbidden schema actions and protected tables; the exemption must not extend to any other method or diagnostic.
```

```text
Execute ArcForges delivery task PLT.02 — Append-only journal with durability and bounded truncation.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\platform.md (anchor task-plt-02).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/plt-02 (python tools/delivery.py claim PLT.02 --worker <name>); task branch task/plt-02 in DesktopPlatform; ledger record ledger/tasks/plt-02.md.
Kind/size: producer/M. Baseline: not-started.
Outcome: JournalEntry records every commit with enough information to replay; journal writes are durable before a commit is acknowledged; growth is bounded by snapshot policy and truncation is safe under concurrent read.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-07.01 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\07-local-persistence-foundation.md, anchor rule-wp-07.01

Entry condition: adoption slice ADOPT.02.platform is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] FND.02: CommandId type
- [artifact] FND.03: Revision/Sequence types
Completion prerequisites (may start earlier; cannot complete before these are complete):
- [integration] PLT.03: actual durable verified snapshots and recovery integrated with journal truncation

Permitted write scope: DesktopPlatform:src/BuildingBlocks/ArcForges.Persistence.Sqlite/**
Shared resources (follow the owner protocol): RES-assistant-store-schema (append): Numbered migrations are allocated at merge by the integration owner (a rebase renumbers pending migrations); each migration is forward-only with its recovery and downgrade-refusal tests; no task edits a merged migration.
Unblocks: PLT.03, PLT.08

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline tests: durability test using a simulated process kill between journal write and commit acknowledgement (in-process fault injection, not a real OS-level crash - that remains local opt-in); replay test; truncation-under-read test.
Completion evidence for the ledger: Durability and replay results. Completion additionally records exact PLT.03 snapshot artifacts and real snapshot/truncate/replay, concurrent-read and repeated bounded-growth acceptance; fixture-only evidence supports delivery only.
Notes: Deliver the durable append/replay journal and verified-boundary truncation seam against an explicitly named snapshot fixture before the snapshot producer exists. A fixture never proves durable snapshot validity or the full bounded-growth obligation. Keep the ledger delivered while PLT.03 is pending; after that producer is complete, perform the real snapshot/truncate/replay, concurrent-read and repeated bounded-growth acceptance before completing PLT.02. Preserve every WP-07.01 obligation and PLT.03 existing artifact start edge; this staging does not authorize starting any unclaimed downstream task.
```

```text
Execute ArcForges delivery task PLT.03 — Snapshot and crash/corruption recovery.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\platform.md (anchor task-plt-03).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/plt-03 (python tools/delivery.py claim PLT.03 --worker <name>); task branch task/plt-03 in DesktopPlatform; ledger record ledger/tasks/plt-03.md.
Kind/size: producer/L. Baseline: not-started.
Outcome: Snapshots are policy-triggered, self-describing and verifiable; recovery selects the latest verifiable snapshot and replays the journal forward to typed outcomes (clean, recovered-with-loss, unrecoverable-with-preserved-evidence); native crash and safe-start paths are handled.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-07.02 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\07-local-persistence-foundation.md, anchor rule-wp-07.02

Entry condition: adoption slice ADOPT.02.platform is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] PLT.02: journal append/replay implementation
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:src/BuildingBlocks/ArcForges.Persistence.Sqlite/**
Shared resources (follow the owner protocol): RES-desktopplatform-policy-data (append): Generated policy data is regenerated from its pinned source and never hand-edited; the reason-code registry is append-only with stable codes; each task adds its own test classes and evidence rows.
Unblocks: PLT.02, PLT.08

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline tests: full recovery matrix (clean shutdown, hard kill, kill during snapshot, kill during migration, corrupted snapshot, corrupted journal tail, disk-full during write) using simulated fault injection; native-crash/safe-start scenarios beyond process-level simulation are local opt-in only.
Completion evidence for the ledger: Full recovery matrix with a named outcome per case.
Notes: This is one of the two narrowest, highest-value early risk proofs in the whole platform area (with PLT.45 content-helper isolation): if crash recovery has a hidden defect, every downstream product's data-loss guarantees are invalid. Recommend starting this in the same wave as PLT.01/02, not deferred.
```

```text
Execute ArcForges delivery task PLT.04 — Migration runner.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\platform.md (anchor task-plt-04).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/plt-04 (python tools/delivery.py claim PLT.04 --worker <name>); task branch task/plt-04 in DesktopPlatform; ledger record ledger/tasks/plt-04.md.
Kind/size: producer/M. Baseline: not-started.
Outcome: Numbered migrations run through a transactional-per-step, idempotent, resumable-after-interruption runner; StorageSchemaVersion equals the highest applied migration; downgrade is either an explicit reverse migration or a clean refusal.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-07.03 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\07-local-persistence-foundation.md, anchor rule-wp-07.03

Entry condition: adoption slice ADOPT.02.platform is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] FND.06: StorageSchemaVersion axis type
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:src/BuildingBlocks/ArcForges.Persistence.Sqlite/**; DesktopPlatform:fixtures/formats/**
Shared resources (follow the owner protocol): RES-desktopplatform-fixtures (append): Fixtures are added per task in their own directory; golden files are never regenerated to make a test pass.
Unblocks: PLT.08, PLT.29, UPD.04

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline tests: forward migration from every historical version fixture, interruption/resume, refusal test for unsupported downgrade, golden-fixture semantic comparison (QI-07).
Completion evidence for the ledger: Migration results against every historical fixture plus semantic comparison.
```

```text
Execute ArcForges delivery task PLT.05 — Managed resource store (content-addressed blobs).

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\platform.md (anchor task-plt-05).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/plt-05 (python tools/delivery.py claim PLT.05 --worker <name>); task branch task/plt-05 in DesktopPlatform; ledger record ledger/tasks/plt-05.md.
Kind/size: producer/M. Baseline: not-started.
Outcome: Content-addressed storage with identity-to-location resolution, integrity verification on read, reference counting derived from a referrer table, and a GC path that never deletes a referenced object even after a crash mid-operation.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-07.04 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\07-local-persistence-foundation.md, anchor rule-wp-07.04

Entry condition: adoption slice ADOPT.02.platform is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] PLT.01: store abstraction's write-path pattern
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:src/BuildingBlocks/ArcForges.Persistence.Resources/**
Shared resources (follow the owner protocol): RES-desktopplatform-build-config (append): Solution/project lists, central package versions and CI job lists are appended by the task that adds a project, dependency or job; dependency additions follow the dependency-admission policy with a reviewed receipt; lock files are regenerated after rebase and never hand-merged; the integration owner resolves ordering conflicts at merge.
Unblocks: PLT.08, PLT.22

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline tests: integrity verification on read, reference-counting test including crash between reference and store, garbage-collection safety test.
Completion evidence for the ledger: Integrity, reference-counting and garbage-collection safety results.
```

```text
Execute ArcForges delivery task PLT.06 — Large append store for high-rate chunked data.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\platform.md (anchor task-plt-06).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/plt-06 (python tools/delivery.py claim PLT.06 --worker <name>); task branch task/plt-06 in DesktopPlatform; ledger record ledger/tasks/plt-06.md.
Kind/size: producer/M. Baseline: not-started.
Outcome: A chunked, verifiable append store outside the relational working store, with per-chunk checksums, an explicit end marker, and honest truncation: a crash mid-append yields a verifiable prefix plus a recorded loss, never a silently short file.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-07.05 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\07-local-persistence-foundation.md, anchor rule-wp-07.05

Entry condition: adoption slice ADOPT.02.platform is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] FND.02: execution/effect-certainty types for loss records
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:src/BuildingBlocks/ArcForges.Persistence.Resources/**
Shared resources (follow the owner protocol): RES-assistant-store-schema (append): Numbered migrations are allocated at merge by the integration owner (a rebase renumbers pending migrations); each migration is forward-only with its recovery and downgrade-refusal tests; no task edits a merged migration.
Unblocks: PLT.08, SCOPE.07

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline tests: append-under-kill at chunk boundaries and mid-chunk, verification of recovered prefix, loss-record assertion.
Completion evidence for the ledger: Append-under-kill results with loss records.
```

```text
Execute ArcForges delivery task PLT.07 — Derived-store abstraction and storage-pressure model.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\platform.md (anchor task-plt-07).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/plt-07 (python tools/delivery.py claim PLT.07 --worker <name>); task branch task/plt-07 in DesktopPlatform; ledger record ledger/tasks/plt-07.md.
Kind/size: producer/S. Baseline: not-started.
Outcome: A DerivedStore abstraction with declared rebuild semantics (every derived store deletable/rebuildable from canonical data) and a StoragePressureState model whose eviction policy only ever touches derived data.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-07.06 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\07-local-persistence-foundation.md, anchor rule-wp-07.06

Entry condition: adoption slice ADOPT.02.platform is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] PLT.01: store abstraction boundary
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:src/BuildingBlocks/ArcForges.Persistence.Derived/**
Shared resources (follow the owner protocol): RES-desktopplatform-build-config (append): Solution/project lists, central package versions and CI job lists are appended by the task that adds a project, dependency or job; dependency additions follow the dependency-admission policy with a reviewed receipt; lock files are regenerated after rebase and never hand-merged; the integration owner resolves ordering conflicts at merge.
Unblocks: PLT.08

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline tests: delete-and-rebuild test per derived-store kind, eviction test asserting canonical data is never evicted.
Completion evidence for the ledger: Rebuild and eviction results.
```

```text
Execute ArcForges delivery task PLT.08 — Publish Persistence packages and verify real integration.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\platform.md (anchor task-plt-08).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/plt-08 (python tools/delivery.py claim PLT.08 --worker <name>); task branch task/plt-08 in DesktopPlatform; ledger record ledger/tasks/plt-08.md.
Kind/size: acceptance/S. Baseline: not-started.
Outcome: ArcForges.Persistence.Sqlite,.Persistence.Resources and.Persistence.Derived are packed, admitted to the publication allowlist, published, and independently consumed; package consumption is shown not to centralise product data ownership.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-07.90 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\07-local-persistence-foundation.md, anchor rule-wp-07.90

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

Permitted write scope: DesktopPlatform:eng/packaging/packages.json; DesktopPlatform:eng/version-sources.json; DesktopPlatform:src/BuildingBlocks/ArcForges.Persistence.Resources/ArcForges.Persistence.Resources.csproj; DesktopPlatform:src/BuildingBlocks/ArcForges.Persistence.Resources/README.md; DesktopPlatform:src/BuildingBlocks/ArcForges.Persistence.Derived/ArcForges.Persistence.Derived.csproj; DesktopPlatform:src/BuildingBlocks/ArcForges.Persistence.Derived/README.md
Shared resources (follow the owner protocol): RES-desktopplatform-build-config (append): Solution/project lists, central package versions and CI job lists are appended by the task that adds a project, dependency or job; dependency additions follow the dependency-admission policy with a reviewed receipt; lock files are regenerated after rebase and never hand-merged; the integration owner resolves ordering conflicts at merge.; RES-desktopplatform-package-inventory (append): Each producer task adds its own package entry; every merge to main packs and publishes all packages at one version; consumers pin the candidate produced by the merge of the capability they need, never waiting for a package closure task; one merge queue.

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): P2-017: offline packages.py verify plus policy tests; real crash/hardware-level recovery evidence beyond simulated kills is local opt-in, recorded separately.
Completion evidence for the ledger: Owned artifact and real-integration receipt per the WP-07.90 template.
Notes: PLT.08-only package activation: the outcome requires the existing Resources and Derived projects to publish as their named managed packages. The task-owned project files authorize only setting IsPackable=true, explicit existing package IDs, readme and description metadata, the existing AGPL-3.0-only licence metadata, and packaging the repository LICENSE and NOTICE; the new task-owned Derived README documents this owned mechanism. The Resources README is authorized for exactly one documentation correction: replace `This project is nonpackable; PLT.08 owns package/integration acceptance.` with `This package provides shared persistence mechanisms without centralizing product data ownership: each product owns its canonical files, schemas and domain records.`; no other Resources README content may change. Preserve public APIs, project references, exact dependency closure, versions and package identities; preserve the existing Sqlite package entry and append only the missing Resources and Derived allowlist entries. Narrow ADP-07 supporting bindings for these changes: update only the active input hashes for eng/packaging/packages.json and the two task-owned Resources/Derived csproj files in eng/policy/dependency-policy.json and the PLT.08 immutable successor at eng/policy/dependency-reviews/plt-08-r1.json; preserve the active predecessor chain and do not change any dependency coordinate, version or closure. In eng/provenance/files.json, append only the task-owned Derived README and the new immutable PLT.08 successor receipt as firstParty; leave the already-classified Resources README row unchanged, and regenerate only required NOTICE/provenance derivatives. Because the two task-owned csproj blobs change, update only their blob hashes on the two corresponding existing project rows in eng/policy/reconciliation/active-projects.json. Do not add or remove projects, edit project-updates.json or source.json, or change the reconciliation algorithm/checker. No workflow, lock, solution, project registration, architecture, licence/runtime policy row, pack algorithm, dependency/version or source API change is authorized.
```

```text
Execute ArcForges delivery task PLT.09 — Local gRPC transport and framing over Named Pipe/UDS.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\platform.md (anchor task-plt-09).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/plt-09 (python tools/delivery.py claim PLT.09 --worker <name>); task branch task/plt-09 in DesktopPlatform; ledger record ledger/tasks/plt-09.md.
Kind/size: producer/L. Baseline: not-started.
Outcome: Generated gRPC over HTTP/2 runs on Windows Named Pipe/Unix domain socket between parent and owned helper/extension children via a custom Kestrel IConnectionListenerFactory and ConnectCallback client, with explicit registration, AOT-safe serialization, and zero local TCP listener.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-08.00 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\08-local-ipc-and-registration.md, anchor rule-wp-08.00
- WP-08:no-product-listener-global-discovery-str No product listener/global discovery - structural constraint on every substep, most directly tested by transport/registration (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\08-local-ipc-and-registration.md, package-level obligation

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
Notes: This is the WP-level edge most worth re-examining: the old header lists WP08 upstream as '06 and 07'. WP-07 (Persistence) is NOT a real start need for any WP08 substep - WP-04.01's own gate explicitly defers durable command/receipt storage to WP07/21/52, meaning WP08's in-flight idempotency stays memory-only; nothing in WP-08.00-08.06 touches SQLite. Recommend dropping the 07->08 start edge entirely; it appears to be inherited phase-grouping (both are 'Phase A/B foundation') rather than a genuine code dependency. Planning repair 2026-10-08 (DLV-34; P2-025): the deferred second Windows account wrong-user denial run and the second Linux uid check are blocked-external inputs; neither is run or claimed here. The task stays delivered and its recorded evidence is unchanged.
```

```text
Execute ArcForges delivery task PLT.10 — Parent-owned endpoint identity.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\platform.md (anchor task-plt-10).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/plt-10 (python tools/delivery.py claim PLT.10 --worker <name>); task branch task/plt-10 in DesktopPlatform; ledger record ledger/tasks/plt-10.md.
Kind/size: producer/M. Baseline: not-started.
Outcome: Parent launch descriptor fixes endpoint, process/build/protocol identity, nonce and epoch; owner-only endpoint files are created/removed atomically; a stale descriptor never authorizes a child.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-08.01 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\08-local-ipc-and-registration.md, anchor rule-wp-08.01

Entry condition: adoption slice ADOPT.02.platform is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] PLT.09: transport/framing
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:src/BuildingBlocks/ArcForges.LocalRpc/**
Unblocks: PLT.11, PLT.16, PLT.38, PLT.45

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline/local tests: concurrent launch, stale descriptor, forged nonce/build, parent-death cleanup.
Completion evidence for the ledger: Concurrent launch, stale descriptor, forged nonce/build and parent-death cleanup results.
Notes: Planning repair 2026-10-08 (DLV-34; P2-025): this delivered task has no second-account or second-uid run in its recorded evidence; those checks (the wrong-user denial inherited through PLT.09) are blocked-external inputs and are not claimed here. The task stays delivered.
```

```text
Execute ArcForges delivery task PLT.11 — Child registration lifecycle.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\platform.md (anchor task-plt-11).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/plt-11 (python tools/delivery.py claim PLT.11 --worker <name>); task branch task/plt-11 in DesktopPlatform; ledger record ledger/tasks/plt-11.md.
Kind/size: producer/M. Baseline: not-started.
Outcome: LocalBootstrap authentication with 30s lease/10s renewal, epoch fencing and restartable restricted launch; expired/stale children cannot call; parent restart requires fresh grants.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-08.02 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\08-local-ipc-and-registration.md, anchor rule-wp-08.02
- WP-08:no-product-listener-global-discovery-str No product listener/global discovery - structural constraint on every substep, most directly tested by transport/registration (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\08-local-ipc-and-registration.md, package-level obligation

Entry condition: adoption slice ADOPT.02.platform is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] PLT.10: endpoint identity
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:src/BuildingBlocks/ArcForges.LocalRpc/**
Unblocks: PLT.12, PLT.16, PRF.02

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline/local tests: expired/stale child cannot call, parent restart requires fresh grants.
Completion evidence for the ledger: Expired/stale child cannot call; parent restart requires fresh grants.
Notes: Planning repair 2026-10-08 (DLV-34; P2-025): this delivered task has no second-account or second-uid run in its recorded evidence; the second Windows account and second Linux uid checks are blocked-external inputs and are not claimed here. The task stays delivered.
```

```text
Execute ArcForges delivery task PLT.12 — Static routing and version refusal.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\platform.md (anchor task-plt-12).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/plt-12 (python tools/delivery.py claim PLT.12 --worker <name>); task branch task/plt-12 in DesktopPlatform; ledger record ledger/tasks/plt-12.md.
Kind/size: producer/S. Baseline: not-started.
Outcome: Resolves only explicitly launched children and their declared generated services; rejects unsupported version/capability; never selects an installed product as fallback.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-08.03 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\08-local-ipc-and-registration.md, anchor rule-wp-08.03

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

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\platform.md (anchor task-plt-13).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/plt-13 (python tools/delivery.py claim PLT.13 --worker <name>); task branch task/plt-13 in DesktopPlatform; ledger record ledger/tasks/plt-13.md.
Kind/size: producer/M. Baseline: not-started.
Outcome: 16 active/64 queued bounded data calls, deadlines and parent-owned callback channels, plus exactly two reserved control slots outside the data-call budget for bootstrap, lease renewal, cancellation and health; all four control operations remain serviceable while data dispatch is saturated, with no recursive saturated callback lane.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-08.04 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\08-local-ipc-and-registration.md, anchor rule-wp-08.04

Entry condition: adoption slice ADOPT.02.platform is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] PLT.09: transport
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:src/BuildingBlocks/ArcForges.LocalRpc/**
Unblocks: PLT.14, PLT.15, PLT.16

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline deterministic tests: queue/memory bound, fairness, timeout and typed overload; hold the ordinary 16-active/64-queued data dispatcher at saturation and prove the exactly two reserved control slots remain outside that budget and service bootstrap, lease renewal, cancellation and health operations (each operation is exercised under saturation), without recursive callback dispatch.
Completion evidence for the ledger: Queue/memory bound, fairness, timeout and typed overload; saturated data-dispatch results proving the exactly two reserved control slots service bootstrap, lease renewal, cancellation and health.
```

```text
Execute ArcForges delivery task PLT.14 — Disconnect, cancel and retry semantics.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\platform.md (anchor task-plt-14).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/plt-14 (python tools/delivery.py claim PLT.14 --worker <name>); task branch task/plt-14 in DesktopPlatform; ledger record ledger/tasks/plt-14.md.
Kind/size: producer/M. Baseline: not-started.
Outcome: Effect certainty, stable command/receipt identity and cancellation are preserved across helper crashes; replay only when explicitly allowed; kill before/after commit and lost-ack scenarios resolve to typed unknown-effect outcomes, in-memory only (durable receipts remain WP07/21/52 territory per WP-04.01's own gate).

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-08.05 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\08-local-ipc-and-registration.md, anchor rule-wp-08.05

Entry condition: adoption slice ADOPT.02.platform is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] PLT.09: transport
- [artifact] FND.02: effect-certainty/Outcome types
- [artifact] PLT.13: two reserved cancellation/control slots under saturated bounded dispatch
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:src/BuildingBlocks/ArcForges.LocalRpc/**
Unblocks: PLT.16

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline/local tests: kill before/after commit, lost ack and unknown effect; while ordinary data dispatch is saturated, prove cancellation progresses through one of PLT.13's two reserved control slots.
Completion evidence for the ledger: Kill before/after commit, lost ack and unknown effect; cancellation succeeds under saturated data dispatch through a reserved control slot.
```

```text
Execute ArcForges delivery task PLT.15 — Brokered large data over the sandbox boundary.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\platform.md (anchor task-plt-15).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/plt-15 (python tools/delivery.py claim PLT.15 --worker <name>); task branch task/plt-15 in DesktopPlatform; ledger record ledger/tasks/plt-15.md.
Kind/size: producer/M. Baseline: not-started.
Outcome: Bounded verified chunks over annex-09 sandbox resources/buffers, parent-authorized only; no direct product-to-product transfer ticket.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-08.06 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\08-local-ipc-and-registration.md, anchor rule-wp-08.06

Entry condition: adoption slice ADOPT.02.platform is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] PLT.09: transport
- [contract] CON.04: ContentSandboxService/slot-grant wire shapes in contracts/09-local-grpc-and-sandbox.md
- [artifact] PLT.13: two reserved cancellation/control slots under saturated bounded dispatch
Completion prerequisites (may start earlier; cannot complete before these are complete):
- [integration] PLT.45: the real ContentSandbox helper actually using these brokered buffers

Permitted write scope: DesktopPlatform:src/BuildingBlocks/ArcForges.LocalRpc/**
Unblocks: PLT.16, PLT.24, PLT.45

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline/local tests: wrong resource grant, range/hash/expiry/cancel and orphan cleanup; while ordinary data dispatch is saturated, prove transfer cancellation progresses through one of PLT.13's two reserved control slots.
Completion evidence for the ledger: Wrong resource grant, range/hash/expiry/cancel and orphan cleanup; transfer cancellation succeeds under saturated data dispatch through a reserved control slot.
```

```text
Execute ArcForges delivery task PLT.16 — Publish LocalRpc package and verify real integration.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\platform.md (anchor task-plt-16).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/plt-16 (python tools/delivery.py claim PLT.16 --worker <name>); task branch task/plt-16 in DesktopPlatform; ledger record ledger/tasks/plt-16.md.
Kind/size: acceptance/S. Baseline: not-started.
Outcome: ArcForges.LocalRpc is packed, admitted, published, and independently consumed; all owned actions/schemas/public interfaces and tests are complete with applicable UX acceptance ledger rows recorded.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-08.90 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\08-local-ipc-and-registration.md, anchor rule-wp-08.90

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

Permitted write scope: DesktopPlatform:eng/packaging/packages.json; DesktopPlatform:src/BuildingBlocks/ArcForges.LocalRpc/ArcForges.LocalRpc.csproj (final IsPackable activation only: the IsPackable value changes from false to true; PackageId, PackageReadmeFile, Description, licence, the existing package and framework references, the InternalsVisibleTo item and the README/LICENSE/NOTICE pack items stay as merged; no reference, package, version, source or setting change); DesktopPlatform:src/BuildingBlocks/ArcForges.LocalRpc/README.md (factual package status, consumption and accuracy corrections only; remove the statement that the project is non-packable); DesktopPlatform:eng/policy/dependency-policy.json (refresh only the packages.json input hash and the LocalRpc project file input hash, mirrored in review.inputHashes, and point reviewReceipt to the PLT.16 successor); DesktopPlatform:eng/policy/dependency-reviews/plt-16-r1.json (new immutable PLT.16 receipt successor chained from the then-active receipt with an unchanged NuGet closure); DesktopPlatform:eng/provenance/files.json (append only the PLT.16 receipt path); DesktopPlatform:eng/policy/reconciliation/active-projects.json (update only the exact LocalRpc project blob)
Shared resources (follow the owner protocol): RES-desktopplatform-package-inventory (append): Each producer task adds its own package entry; every merge to main packs and publishes all packages at one version; consumers pin the candidate produced by the merge of the capability they need, never waiting for a package closure task; one merge queue.; RES-desktopplatform-build-config (append): Solution/project lists, central package versions and CI job lists are appended by the task that adds a project, dependency or job; dependency additions follow the dependency-admission policy with a reviewed receipt; lock files are regenerated after rebase and never hand-merged; the integration owner resolves ordering conflicts at merge.; RES-desktopplatform-policy-data (append): Generated policy data is regenerated from its pinned source and never hand-edited; the reason-code registry is append-only with stable codes; each task adds its own test classes and evidence rows.

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): P2-017: offline package and policy tests plus one independent consumer check against the exact prepublication CI candidate package. The consumer must resolve the recorded package ID/version and SHA256 from the candidate artifact through an isolated temporary package source/cache, with no project reference, sibling-source fallback or substitute package; record source commit, CI run/artifact identity, package identity/digest and consumer restore/build/run result. This existing-environment candidate check is local opt-in and performed once for the affected candidate; do not add a hosted installed-consumer test or a permanent consumer harness. Real multi-process OS-stream evidence beyond the repo's own build-machine tests remains local opt-in.
Completion evidence for the ledger: Exact CI candidate artifact/source commit and package identity/version/SHA256; independent isolated consumer restore/build/run proving it resolved only that exact candidate with no project/source fallback; package/policy checks and applicable UX acceptance ledger. Record any separately required real OS-stream run once as local opt-in evidence.
Notes: ADP-07 support is limited to the exact append-only package-inventory row in eng/packaging/packages.json and its required existing-gate bindings: refresh only that file's active input hash and the current dependency-review pointer/active review object in eng/policy/dependency-policy.json; add immutable eng/policy/dependency-reviews/plt-16-r1.json as a successor to the then-current receipt, preserving the admitted dependency coordinates, versions and closure; and append only that receipt as firstParty in eng/provenance/files.json. Use RES-desktopplatform-policy-data for these task-owned policy/provenance bindings and RES-desktopplatform-package-inventory for the package row. Do not invent or predeclare LocalRpc package dependency IDs, version ranges or closure here: derive them only from the reviewed, frozen PLT.09 project references and their separately admitted exact pins; if that frozen graph requires any unadmitted package/version change, obtain authority before changing it. Do not change projects, package locks, reconciliation, architecture classifications or test maps, licences, runtime behavior, policy algorithms or unrelated records. PLT.16 may publish/consume the progressive exact package candidate once its declared PLT.09-15 artifacts exist; it has no PLT.45 completion prerequisite. PLT.15 remains complete only after PLT.45 integrates the brokered-data mechanism. Package-activation binding (ADP-07): the planned scope listed only the catalogue and the policy bindings, which cannot activate a package. The packable-iff-listed repository policy test (RepositoryPolicyTests.PublishedProjectsAreExplicitAndContainNoPlaceholders) requires a listed project to set IsPackable and ArcForges.LocalRpc.csproj sets IsPackable false as merged by PLT.09, the dependency-admission gate binds the hash of that project file, and the reconciliation snapshot binds its blob; PLT.35 and PLT.53 had the same single-property project activation in their own write scope. The PackageId, readme, licence, description and pack items are already present from PLT.09, so the project change is the IsPackable value alone, plus the one stale README sentence that says the project is non-packable. The catalogue entry lists ArcForges.LocalRpc with kind managed, no owned dependencies (the project has no ProjectReference) and exactly the external dependencies a dotnet pack nuspec generates, which are the two PackageReference items Grpc.AspNetCore.Server and Grpc.Net.Client at their existing exact central versions (checked with packages.validate_generated_dependencies); it adds no project reference, package reference, central version or source behavior, so the locked NuGet closure keeps identical coordinates, versions and content hashes. Resource owners and protocols: RES-desktopplatform-package-inventory (append) for the catalogue entry, RES-desktopplatform-build-config (append) for the project file, RES-desktopplatform-policy-data (append) for the receipt chain, provenance row and reconciliation snapshot; regenerate or re-append after rebase and chain the receipt from the receipt active on main at merge. Not authorized: any other source file, any test, any packages.lock.json, Directory.Packages.props, workflow, .gitleaks.toml or scan allowlist (the receipt-directory group merged with PLT.44 covers the mirrored receipt lines and must not be widened; add no hash-like literal), eng/policy/architecture-projects.json, eng/policy/architecture-contract-tests.json or any other task's rows.
```

```text
Execute ArcForges delivery task PLT.17 — Application identity and in-process composition.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\platform.md (anchor task-plt-17).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/plt-17 (python tools/delivery.py claim PLT.17 --worker <name>); task branch task/plt-17 in DesktopPlatform; ledger record ledger/tasks/plt-17.md.
Kind/size: producer/S. Baseline: not-started.
Outcome: AppIdentity/InstallationIdentity/InstanceIdentity bound to each application composition root; two products on one device keep separate sessions/history/capabilities; forged/missing target refuses; no running-product registry or shared Hub.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-09.00 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\09-capability-contribution-and-resource-model.md, anchor rule-wp-09.00

Entry condition: adoption slice ADOPT.02.platform is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [contract] CON.91: descriptor contract types (App/Installation/Instance identity wire shapes)
- [artifact] FND.01: identity primitive types
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:src/BuildingBlocks/ArcForges.Capabilities/**
Shared resources (follow the owner protocol): RES-desktopplatform-build-config (append): Solution/project lists, central package versions and CI job lists are appended by the task that adds a project, dependency or job; dependency additions follow the dependency-admission policy with a reviewed receipt; lock files are regenerated after rebase and never hand-merged; the integration owner resolves ordering conflicts at merge.
Unblocks: APP.01, APP.08, EXE.01, PLT.18, PLT.19, PLT.21, PLT.22, PLT.25

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline unit tests: two-product separation, forged/missing target refusal.
Completion evidence for the ledger: Identity lifecycle matrix.
Notes: The old header lists WP09 upstream as '03, 08'. Reading contracts/02-local-rpc-operations.md closely: product capability ports (ICapabilityProvider etc.) are IN-PROCESS typed calls; only helper/extension children use the WP-08 Named Pipe/UDS transport. WP-09.00-09.06 (identity, registration, selection, availability, context, resources, navigation/health) do not need WP-08 at all. Recommend narrowing the 08->09 edge to apply only where PLT.24 (invocation pipeline) routes to an admitted child - see PLT.24's own start edges.
```

```text
Execute ArcForges delivery task PLT.18 — Static contribution registration.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\platform.md (anchor task-plt-18).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/plt-18 (python tools/delivery.py claim PLT.18 --worker <name>); task branch task/plt-18 in DesktopPlatform; ledger record ledger/tasks/plt-18.md.
Kind/size: producer/M. Baseline: not-started.
Outcome: Capability/context/artifact/lifecycle/deep-link handlers register inside the owning process through generated descriptors and explicit composition; duplicate IDs, wrong owner, unavailable child, undeclared tool schema and cross-product registration all refuse; registration is idempotent and survives restart.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-09.01 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\09-capability-contribution-and-resource-model.md, anchor rule-wp-09.01
- WP-09:contribution-registration-state-durable Contribution/registration state durable across restarts (SS6 impacts) (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\09-capability-contribution-and-resource-model.md, package-level obligation

Entry condition: adoption slice ADOPT.02.platform is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] PLT.17: application identity/composition root
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:src/BuildingBlocks/ArcForges.Contributions/**
Unblocks: NAT.01, PLT.25

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline tests: duplicate IDs, wrong owner, unavailable child, undeclared tool schema, cross-product registration refusal; registration survives a simulated restart against the persistence layer PLT.01/PLT.05 provide.
Completion evidence for the ledger: Registration idempotency and namespace refusal results.
```

```text
Execute ArcForges delivery task PLT.19 — Capability registry and selection.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\platform.md (anchor task-plt-19).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/plt-19 (python tools/delivery.py claim PLT.19 --worker <name>); task branch task/plt-19 in DesktopPlatform; ledger record ledger/tasks/plt-19.md.
Kind/size: producer/L. Baseline: not-started.
Outcome: The wire CapabilityDescriptor/OperationBinding/effect/locus/context/cancellation schema is implemented with a complete initial first-party binding matrix; enumerated bindings are validated against declared Contracts methods; unsupported major, inconsistent pureRead/write classification, readiness mismatch and ambiguous target all reject.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-09.02 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\09-capability-contribution-and-resource-model.md, anchor rule-wp-09.02

Entry condition: adoption slice ADOPT.02.platform is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] PLT.17: identity/composition
- [contract] CON.91: accepted Foundation contract profile, including ResourceRef/ResourceVersionRef/ArtifactRef
- [contract] CON.02: CapabilityDescriptor/OperationBinding wire schema
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:Directory.Packages.props; DesktopPlatform:eng/packaging/packages.json; DesktopPlatform:eng/policy/architecture-contract-tests.json; DesktopPlatform:eng/policy/dependency-policy.json; DesktopPlatform:eng/policy/dependency-reviews/plt-19-r1.json; DesktopPlatform:eng/policy/reconciliation/active-projects.json; DesktopPlatform:eng/provenance/files.json; DesktopPlatform:src/BuildingBlocks/ArcForges.Application.Abstractions/packages.lock.json; DesktopPlatform:src/BuildingBlocks/ArcForges.Capabilities/packages.lock.json; DesktopPlatform:src/BuildingBlocks/ArcForges.Capabilities/Tests/packages.lock.json; DesktopPlatform:src/BuildingBlocks/ArcForges.Contributions/packages.lock.json; DesktopPlatform:src/BuildingBlocks/ArcForges.Contributions/Tests/packages.lock.json; DesktopPlatform:src/BuildingBlocks/ArcForges.Foundation/packages.lock.json; DesktopPlatform:src/BuildingBlocks/ArcForges.Foundation/Tests/packages.lock.json; DesktopPlatform:src/BuildingBlocks/ArcForges.Observability/packages.lock.json; DesktopPlatform:src/BuildingBlocks/ArcForges.Observability/Tests/packages.lock.json; DesktopPlatform:src/BuildingBlocks/ArcForges.Persistence.Resources/packages.lock.json; DesktopPlatform:src/BuildingBlocks/ArcForges.Persistence.Resources/Tests/packages.lock.json; DesktopPlatform:src/BuildingBlocks/ArcForges.Persistence.Sqlite/packages.lock.json; DesktopPlatform:src/BuildingBlocks/ArcForges.Security/packages.lock.json; DesktopPlatform:src/BuildingBlocks/ArcForges.Security/Tests/packages.lock.json; DesktopPlatform:src/DesktopHelpers/ArcForges.ContentSandbox/packages.lock.json; DesktopPlatform:src/BuildingBlocks/ArcForges.Capabilities/**; DesktopPlatform:tests/PersistenceTests/packages.lock.json
Shared resources (follow the owner protocol): RES-desktopplatform-build-config (append): Solution/project lists, central package versions and CI job lists are appended by the task that adds a project, dependency or job; dependency additions follow the dependency-admission policy with a reviewed receipt; lock files are regenerated after rebase and never hand-merged; the integration owner resolves ordering conflicts at merge.; RES-desktopplatform-package-inventory (append): Each producer task adds its own package entry; every merge to main packs and publishes all packages at one version; consumers pin the candidate produced by the merge of the capability they need, never waiting for a package closure task; one merge queue.; RES-desktopplatform-policy-data (append): Generated policy data is regenerated from its pinned source and never hand-edited; the reason-code registry is append-only with stable codes; each task adds its own test classes and evidence rows.
Unblocks: EXT.00, PLT.20, PLT.24, PLT.25, PLT.37

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline tests: enumerate expected bindings, reject missing/extra methods/unsupported major/inconsistent classification/readiness mismatch/ambiguous target. Verify the implementation-only closed owner union: Product(AppIdentity) only for ArcScope/Companion inProcess descriptors, or CloudService(SearchService) only for the currently declared search.query publicGrpc descriptor; CloudService is static catalogue metadata and never constructs a CapabilityTarget or enters the local instance selector, while caller scope remains ApplicationScope. Force-evaluate and perform locked restore for the exact 17-project Contracts.Foundation 1.0.0-ci.216.1 consumer set; confirm all other projects retain the 1.0.0-ci.113.1 repository default, including Foundation.Acceptance. Validate generated package metadata for the five authorized package rows and restore repository-external locked consumers of ArcForges.Capabilities and ArcForges.Capabilities plus ArcForges.Persistence.Sqlite against the candidate feed with no NU1107, NU1605 or NU1608.
Completion evidence for the ledger: Selection priority, determinism and explainability results.
Notes: Keep the repository-wide ArcForges.Contracts.Foundation default at 1.0.0-ci.113.1 and authorize the exact 1.0.0-ci.216.1 central pin only for these 17 MSBuildProjectName values: LocalRpcAotTests, ArcForges.Application.Abstractions, ArcForges.Capabilities, ArcForges.Capabilities.Tests, ArcForges.ContentSandbox, ArcForges.Contributions, ArcForges.Contributions.Tests, ArcForges.Foundation, ArcForges.Foundation.Tests, ArcForges.Observability, ArcForges.Observability.Tests, ArcForges.Persistence.Resources, ArcForges.Persistence.Resources.Tests, ArcForges.Persistence.Sqlite, ArcForges.Security, ArcForges.Security.Tests, and ArcForges.Tests.PersistenceTests. Preserve Foundation.Acceptance and all other projects on the repository default; do not change the existing LocalRpcAotTests pin. In eng/packaging/packages.json, change only externalDependencies.ArcForges.Contracts.Foundation from 1.0.0-ci.113.1 to 1.0.0-ci.216.1 for the existing rows ArcForges.Foundation, ArcForges.Application.Abstractions, ArcForges.Capabilities, ArcForges.Persistence.Sqlite, and ArcForges.Persistence.Resources. Preserve each row's package ID, project, kind, owned dependencies, required files and all other fields, as well as every other package row. Only these 16 semantic lock paths may change: src/BuildingBlocks/ArcForges.Application.Abstractions/packages.lock.json; src/BuildingBlocks/ArcForges.Capabilities/packages.lock.json; src/BuildingBlocks/ArcForges.Capabilities/Tests/packages.lock.json; src/BuildingBlocks/ArcForges.Contributions/packages.lock.json; src/BuildingBlocks/ArcForges.Contributions/Tests/packages.lock.json; src/BuildingBlocks/ArcForges.Foundation/packages.lock.json; src/BuildingBlocks/ArcForges.Foundation/Tests/packages.lock.json; src/BuildingBlocks/ArcForges.Observability/packages.lock.json; src/BuildingBlocks/ArcForges.Observability/Tests/packages.lock.json; src/BuildingBlocks/ArcForges.Persistence.Resources/packages.lock.json; src/BuildingBlocks/ArcForges.Persistence.Resources/Tests/packages.lock.json; src/BuildingBlocks/ArcForges.Persistence.Sqlite/packages.lock.json; src/BuildingBlocks/ArcForges.Security/packages.lock.json; src/BuildingBlocks/ArcForges.Security/Tests/packages.lock.json; src/DesktopHelpers/ArcForges.ContentSandbox/packages.lock.json; and tests/PersistenceTests/packages.lock.json. Fourteen of these locks move from the already-admitted 113.1 coordinate to 216.1; the Capabilities and Capabilities.Tests locks may change only for the Foundation project-reference edge. LocalRpcAotTests and eng/acceptance/foundation/packages.lock.json remain unchanged, and no DesignSystem newline-only or other lockfile changes are authorized. Preserve the existing 51 NuGet coordinates and 10 Python package closure unchanged. The only permitted dependency-coordinate adjustment is the already-admitted Contracts.Foundation 1.0.0-ci.113.1 to 1.0.0-ci.216.1 selection for these exact five package rows and 17 projects; do not add or delete coordinates, change any license or package identity, or alter unrelated dependencies. Refresh dependency-policy.json and the immutable plt-19-r1 receipt only for actual task inputs, mirroring the same input hashes in review.inputHashes; chain the receipt from the active receipt at integration and do not modify historical receipts. No new project, package ID, version axis, global default pin, packaging algorithm, release mechanism, solution, workflow or licence-boundary change is authorized. The capability owner is an implementation-only closed union: Product(AppIdentity), limited to ArcScope/Companion inProcess descriptors, or CloudService(SearchService), limited to the currently declared search.query publicGrpc descriptor. Do not change wire CapabilityDescriptor, AppIdentity, ProductId or ApplicationScope. CloudService registration is static catalogue metadata only; it must not construct CapabilityTarget or enter the local instance selector, and caller scope remains the request ApplicationScope. Do not add a PublicApi dependency, package or closure edge. Planning repair 2026-10-08 (DLV-34; P2-023): the osx-* sections of this task's src/DesktopHelpers/ArcForges.ContentSandbox/packages.lock.json are retired by GOV.30 under P2-023; this task keeps its other writes.
```

```text
Execute ArcForges delivery task PLT.20 — Actions and availability.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\platform.md (anchor task-plt-20).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/plt-20 (python tools/delivery.py claim PLT.20 --worker <name>); task branch task/plt-20 in DesktopPlatform; ledger record ledger/tasks/plt-20.md.
Kind/size: producer/M. Baseline: not-started.
Outcome: Actions are computed from capabilities plus current context, side-effect free, cheap enough for UI enumeration; unavailability always yields a typed reason across permission/entitlement/health/context/version causes.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-09.03 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\09-capability-contribution-and-resource-model.md, anchor rule-wp-09.03

Entry condition: adoption slice ADOPT.02.platform is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] PLT.19: capability registry
Completion prerequisites (may start earlier; cannot complete before these are complete):
- [integration] PLT.38: Security-owner read-only permission evidence for the acting principal, exact capability and scope
- [integration] COM.05: canonical per-capability entitlement reason and version from the immutable grant/revocation resolver
- [integration] COM.06: the versioned client-distributed entitlement snapshot and bounded-staleness/refresh behavior

Permitted write scope: DesktopPlatform:src/BuildingBlocks/ArcForges.Capabilities/**; DesktopPlatform:eng/policy/architecture-contract-tests.json (append only the exact PLT.20 availability API-to-direct-test binding after source/test names are frozen); DesktopPlatform:eng/provenance/files.json (append only exact PLT.20-owned firstParty rows for source/test files within the existing task source scope, after file names are frozen)
Shared resources (follow the owner protocol): RES-architecture-tests (append): Each repository policy task owns its suite; rule additions are append-only.; RES-desktopplatform-policy-data (append): Generated policy data is regenerated from its pinned source and never hand-edited; the reason-code registry is append-only with stable codes; each task adds its own test classes and evidence rows.
Unblocks: PLT.24, PLT.25, PLT.28

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline tests: availability tests across permission/entitlement/health/context/version reasons; purity test asserting no side effect.
Completion evidence for the ledger: Availability reason matrix and purity assertion.
Notes: ADP-07 support is limited to the two exact supporting files above and append-only updates. Map `ArcResult<T>` to the delivered `ArcForges.Foundation.Errors.Outcome<T>` and `FrozenContext` to PLT.21's delivered `FrozenContextSnapshot`; preserve the exact `ValueTask<Outcome<AvailabilityResult>> ICapabilityProvider.EvaluateAvailabilityAsync(ActionKey actionKey, FrozenContextSnapshot context, CancellationToken cancellationToken = default)` signature and all nine existing result facts. Add only a Capabilities-owned immutable in-process `AvailabilityEvidenceSnapshot` supplied at provider construction by a trusted host; it is a local CLR contract, not protobuf, wire DTO, PublicApi dependency or grant. Bind one snapshot to `FrozenContextSnapshot.Owner`, provider principal/session, and finite unique action/capability/target keys; require exactly one matching record and reject missing, duplicate or mismatched keys. The host captures one fixed as-of time for each UI enumeration, computes freshness disposition before constructing the short-lived provider, and discards/rebuilds it on refresh or expiry; evaluation consumes only immutable evidence and its precomputed freshness disposition, never reads a clock or performs I/O. Permission facts must be owner-issued and preserve principal/capability/scope/constraints/lifetime; entitlement reason/version comes from COM.05/06; health/readiness/compatibility, product-version, installed and running facts require explicit trusted sources. PLT.19 `CapabilityTarget`/descriptor data does not establish distinct installed-versus-running state or product version: never infer these from an absent target or contract version. Missing, stale-at-capture, unknown or contradictory evidence must not yield `Available`; return an existing typed reason only for an explicitly established fact, otherwise `TemporarilyUnavailable`. Context applicability comes from the frozen context. Keep evaluation a pure projection over immutable inputs: `availabilityRule` keys select a finite private closed table of pure rule kinds; do not permit arbitrary caller-registered delegates, I/O, discovery, authorization, mutation or side effects. This is UX preflight only; Security rechecks at invocation and Cloud re-evaluates protected dispatch. `PolicyDisabled` requires explicit authorized input to an existing rule; do not invent a policy authority. Test expired-at-capture evidence returns `TemporarilyUnavailable` and host refresh constructs a new provider/snapshot; local tests may synthesize snapshots, but do not claim full WP-09.03 integration until the PLT.38 and COM.05/06 completion edges and real producer inputs are satisfied. Bind only the exact API to its direct PLT.20 test in RP-10 after names are frozen. Append only PLT.20-owned firstParty provenance rows within `src/BuildingBlocks/ArcForges.Capabilities/**`, preserving all rows and the RES-architecture-tests/RES-desktopplatform-policy-data append protocols. No new project, package, dependency, lock, solution, workflow, licence boundary, runtime owner, PublicApi reference, protobuf or reconciliation change is authorized; outcome, prerequisites and runtime behavior remain unchanged.
```

```text
Execute ArcForges delivery task PLT.21 — Context providers and freezing.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\platform.md (anchor task-plt-21).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/plt-21 (python tools/delivery.py claim PLT.21 --worker <name>); task branch task/plt-21 in DesktopPlatform; ledger record ledger/tasks/plt-21.md.
Kind/size: producer/M. Baseline: not-started.
Outcome: Context providers contribute typed context; at invocation the context is frozen into an immutable snapshot carried with the invocation; a later live-context change never affects an in-flight invocation; oversized context is refused explicitly.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-09.04 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\09-capability-contribution-and-resource-model.md, anchor rule-wp-09.04

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

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\platform.md (anchor task-plt-22).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/plt-22 (python tools/delivery.py claim PLT.22 --worker <name>); task branch task/plt-22 in DesktopPlatform; ledger record ledger/tasks/plt-22.md.
Kind/size: producer/M. Baseline: not-started.
Outcome: Resource resolution from reference to access honours ownership and floating-versus-pinned distinction; artifact handlers register per kind; a reference never carries a path/pointer/handle; resolution re-checks permission at access time.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-09.05 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\09-capability-contribution-and-resource-model.md, anchor rule-wp-09.05

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

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\platform.md (anchor task-plt-23).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/plt-23 (python tools/delivery.py claim PLT.23 --worker <name>); task branch task/plt-23 in DesktopPlatform; ledger record ledger/tasks/plt-23.md.
Kind/size: producer/M. Baseline: not-started.
Outcome: Artifact opens and deep links route to the owning application handler; bounded in-process state hints cause authoritative rereads; invalid ownership, missing content, expired child cursor, restart and duplicate hint all recover without launching another product.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-09.06 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\09-capability-contribution-and-resource-model.md, anchor rule-wp-09.06

Entry condition: adoption slice ADOPT.02.platform is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] PLT.22: resource/artifact resolution
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:src/BuildingBlocks/ArcForges.Capabilities/**; DesktopPlatform:eng/provenance/files.json (append only exact PLT.23-owned firstParty rows for source/test files within the task write scope); DesktopPlatform:eng/policy/architecture-contract-tests.json (append only exact PLT.23 public API to direct-test bindings)
Shared resources (follow the owner protocol): RES-architecture-tests (append): Each repository policy task owns its suite; rule additions are append-only.; RES-desktopplatform-policy-data (append): Generated policy data is regenerated from its pinned source and never hand-edited; the reason-code registry is append-only with stable codes; each task adds its own test classes and evidence rows.
Unblocks: PLT.25, PLT.51

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline tests: invalid ownership, missing content, expired child cursor, restart, duplicate hint recovery.
Completion evidence for the ledger: Deep-link hostile-input, event and health results.
Notes: HealthDimension is only the closed capability-probe aspect-key type defined by WP-09: reachable, ready, healthy, degraded and capacity. It carries no observation value or snapshot fields. These keys are not Architecture 02 §11's five independent axes (Installation, Presence, Health, Readiness, Compatibility). This clarification changes no Contracts/wire or Foundation HealthSnapshot/InstanceHealth/InstanceReadiness semantics and defines no Cloud presence/heartbeat behavior. ADP-07 support is limited to the two exact supporting paths above: append only PLT.23-owned firstParty source/test inventory rows and exact public-API-to-direct-test rows required by the existing provenance and RP-10 gates. These changes use RES-desktopplatform-policy-data, owned by the DesktopPlatform integration owner: generated policy data is regenerated from its pinned source and never hand-edited; task-owned API/test and inventory rows are additive, and each task adds its own tests/evidence. No evaluator, schema, algorithm, ReasonCode, dependency closure or unrelated policy change is authorized; task outcome, prerequisites and runtime behavior remain unchanged.
```

```text
Execute ArcForges delivery task PLT.24 — Invocation pipeline.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\platform.md (anchor task-plt-24).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/plt-24 (python tools/delivery.py claim PLT.24 --worker <name>); task branch task/plt-24 in DesktopPlatform; ledger record ledger/tasks/plt-24.md.
Kind/size: producer/L. Baseline: not-started.
Outcome: The end-to-end path resolve -> check availability -> freeze context -> authorize -> invoke -> validate result -> record is the ONLY route to a capability; every failure maps to the closed semantic error set; every invocation is traced.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-09.07 (all work except the parts mapped to PLT.57): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\09-capability-contribution-and-resource-model.md, anchor rule-wp-09.07

Entry condition: adoption slice ADOPT.02.platform is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] PLT.19: capability registry/selection
- [artifact] PLT.20: availability
- [artifact] PLT.21: context freezing
Completion prerequisites (may start earlier; cannot complete before these are complete):
- [integration] PLT.15: real LocalRpc brokered routing for the subset of invocations that target an admitted helper/extension child

Permitted write scope: DesktopPlatform:Directory.Packages.props (add one project-conditional exact ArcForges.Sdk.Contracts 1.0.0-ci.216.1 pin for ArcForges.Capabilities only); DesktopPlatform:eng/packaging/packages.json (add only the exact SDK.Contracts 216.1 external dependency to the existing Capabilities row); DesktopPlatform:eng/policy/architecture-contract-tests.json (append only actual PLT.24 public API to direct-test bindings); DesktopPlatform:eng/policy/dependency-policy.json (admit only exact closure additions and refresh task-owned inputs/active receipt); DesktopPlatform:eng/policy/dependency-reviews/plt-24-r1.json (one immutable PLT.24 successor receipt); DesktopPlatform:eng/policy/reconciliation/active-projects.json (refresh only the existing Capabilities project blob); DesktopPlatform:eng/provenance/files.json (append only task-owned firstParty source/test paths and the immutable receipt); DesktopPlatform:src/BuildingBlocks/ArcForges.Capabilities/**; DesktopPlatform:src/BuildingBlocks/ArcForges.Capabilities/packages.lock.json; DesktopPlatform:src/BuildingBlocks/ArcForges.Capabilities/Tests/packages.lock.json; DesktopPlatform:src/BuildingBlocks/ArcForges.Contributions/packages.lock.json; DesktopPlatform:src/BuildingBlocks/ArcForges.Contributions/Tests/packages.lock.json
Shared resources (follow the owner protocol): RES-desktopplatform-build-config (append): Solution/project lists, central package versions and CI job lists are appended by the task that adds a project, dependency or job; dependency additions follow the dependency-admission policy with a reviewed receipt; lock files are regenerated after rebase and never hand-merged; the integration owner resolves ordering conflicts at merge.; RES-desktopplatform-package-inventory (append): Each producer task adds its own package entry; every merge to main packs and publishes all packages at one version; consumers pin the candidate produced by the merge of the capability they need, never waiting for a package closure task; one merge queue.; RES-desktopplatform-policy-data (append): Generated policy data is regenerated from its pinned source and never hand-edited; the reason-code registry is append-only with stable codes; each task adds its own test classes and evidence rows.
Unblocks: APP.02, APP.03, PLT.25, PLT.57

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline tests: policy test asserting no bypass route exists; error-mapping tests for every semantic error; tracing test. Consume only the Invocation and FrozenContext members present in ArcForges.Sdk.Contracts 1.0.0-ci.216.1; later ValueSchema additions are outside scope and must not be referenced.
Completion evidence for the ledger: Pipeline bypass-prohibition, error-mapping and tracing results.
Notes: Generated request and context binding: the invocation request is the published Registry 04 ArcForges.Sdk.Contracts.V1.Invocation from Contracts/public/proto/arcforges/extensions/v1/extensions.proto, not a second local Invocation DTO. Use its generated FrozenContext directly with PLT.21 FrozenContextSnapshot, bound to the resolved owner InstanceIdentity and captured before asynchronous dispatch; preserve protobuf descriptor/type and the generated request's identity, evidence, arguments and expected-version oneof. Product capability calls remain in-process. Result-version semantics are defined by the local RPC contract `docs/architecture/contracts/02-local-rpc-operations.md` §3 (anchor `rule-ci-04`): the local InvocationOutcome preserves the typed owner's exact result-version meaning as Revision, NativeContentRev or NonVersioned. A successful versioned operation carries the exact owner-provided value, including an unchanged version observed by a versioned read; keep NativeContentRev native and never coerce it to Revision. A successful typed operation whose local owner result defines no single authoritative version is NonVersioned, including effectful handle results CreateConversationAsync → ConversationRef and StartAgentTurnAsync → TaskRef; absence of a result version does not imply the operation had no effect. NonVersioned has no result-version payload (field absent, not a zero/default sentinel), is not a wire enum/field or precondition, and cannot supply a version for a chained versioned write. Obtain a later version through a separate typed owner read/receipt. A mutation whose typed owner result defines a version cannot succeed without it. Expected versions on Invocation remain distinct preconditions; failure/cancellation are separate non-success outcomes. A same-CommandId retry returns the originally recorded typed outcome. Registry 04 shows the typed distinction: search.query returns items and PageState without a top-level revision; IScopeOperations.CreateAnnotation/CreateFinding return NativeContentRev; chat.AppendUserMessage's local typed operation returns Revision, even though the wire Receipt.result_revision is optional; and the local StartAgentTurn operation returns TaskRef. A wire TaskSnapshot revision is not the local typed TaskRef result version. Use the registered typed owner result, not field-name guessing or a flattened integer/string. PLT.15's current ContentSandbox child subset is the 15 methods in Registry 04 §6; session/slot/buffer/image/PDF outputs, identifiers, counts, expiry values and receipts define no owner Revision or NativeContentRev. ResponseMeta.result_rev and Receipt.result_revision are therefore absent for these current calls; no current PLT.15 NativeContentRev propagation blocker is asserted. ResourceVersionRef pins, where used, retain their own cloud/native oneof and are not operation result versions. For brokered extension-child invocation, forward the same generated Invocation through ExtensionHostServiceInvokeRequest.invocation and keep RequestMeta/LocalCallContext consistent. ResponseMeta.result_rev carries Revision only, has no NativeContentRev arm, and ToolResult has no generic result-version field; keep native revisions in their typed/native results. A future child operation that requires NativeContentRev through an invocation outcome/version chain needs separate reviewed Contracts/child-route authority; this task does not change wire fields. Use PLT.15 brokered ResourceRef transfer only where the current child route requires it. The sole dependency exception needed to consume that already-published generated request is one direct PackageReference to ArcForges.Sdk.Contracts 1.0.0-ci.216.1 in ArcForges.Capabilities.csproj, with one central PackageVersion conditional only on MSBuildProjectName ArcForges.Capabilities. In eng/packaging/packages.json add only ArcForges.Sdk.Contracts 1.0.0-ci.216.1 to externalDependencies of the existing ArcForges.Capabilities package row; do not add a direct ArcForges.Contracts.PublicApi dependency or change package identity. The exact SDK.Contracts 216.1 nuspec adds only ArcForges.Contracts.PublicApi 216.1 to the current closure; Foundation 216.1, Google.Protobuf 3.36.1 and Grpc.Core.Api 2.84.0 remain at their existing versions. Extend the existing Grpc.Core.Api 2.84.0 classification only to record runtime transitiveness through SDK.Contracts while preserving its PRF.04 build-only use. Only the Capabilities, Capabilities.Tests, Contributions and Contributions.Tests lock files may record the resulting exact transitive package graph; all other locks and the repository-wide Contracts.Foundation 113.1 default remain unchanged. The active dependency policy may add only ArcForges.Sdk.Contracts/216.1 and ArcForges.Contracts.PublicApi/216.1, refresh exact changed-input hashes and point to the immutable plt-24-r1 successor; chain that receipt to the active receipt at integration (currently plt-27-r1) without modifying historical receipts. Refresh only the existing Capabilities project blob in active-projects, and append only PLT.24-owned firstParty source/test paths and receipt plus actual API-to-direct-test RP-10 bindings. These exact updates use RES-desktopplatform-build-config, RES-desktopplatform-package-inventory and RES-desktopplatform-policy-data. Do not select SDK.Contracts 250.1 or any other version, alter unrelated package coordinates, licenses or package IDs, add projects or workflow changes, change packaging algorithms, or alter Contracts/wire schemas.
```

```text
Execute ArcForges delivery task PLT.25 — Publish Capabilities/Contributions packages and verify real integration.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\platform.md (anchor task-plt-25).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/plt-25 (python tools/delivery.py claim PLT.25 --worker <name>); task branch task/plt-25 in DesktopPlatform; ledger record ledger/tasks/plt-25.md.
Kind/size: acceptance/S. Baseline: not-started.
Outcome: ArcForges.Capabilities (and the Contributions internals it packages) is packed, admitted, published, and independently consumed by one local opt-in clean-consumer run recorded once (P2-017); owner refuses invalid/stale invocations and opaque references do not grant access.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-09.90 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\09-capability-contribution-and-resource-model.md, anchor rule-wp-09.90

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

Permitted write scope: DesktopPlatform:eng/packaging/packages.json; DesktopPlatform:eng/version-sources.json; DesktopPlatform:src/BuildingBlocks/ArcForges.Contributions/ArcForges.Contributions.csproj (final IsPackable/package activation only: set IsPackable to true; the PackageId, PackageReadmeFile, Description and README/LICENSE/NOTICE pack items already exist; no reference, package, version, source or setting change); DesktopPlatform:src/BuildingBlocks/ArcForges.Contributions/README.md (factual package status, contents, consumption and accuracy corrections only); DesktopPlatform:eng/policy/dependency-policy.json (refresh only the packages.json input hash and the Contributions project file input hash, mirrored in review.inputHashes, and point reviewReceipt to the PLT.25 successor); DesktopPlatform:eng/policy/dependency-reviews/plt-25-r1.json (new immutable PLT.25 receipt successor chained from the then-active receipt with an unchanged NuGet closure); DesktopPlatform:eng/provenance/files.json (append only the PLT.25 receipt path); DesktopPlatform:eng/policy/reconciliation/active-projects.json (update only the exact PLT.25 Contributions project blob)
Shared resources (follow the owner protocol): RES-desktopplatform-build-config (append): Solution/project lists, central package versions and CI job lists are appended by the task that adds a project, dependency or job; dependency additions follow the dependency-admission policy with a reviewed receipt; lock files are regenerated after rebase and never hand-merged; the integration owner resolves ordering conflicts at merge.; RES-desktopplatform-package-inventory (append): Each producer task adds its own package entry; every merge to main packs and publishes all packages at one version; consumers pin the candidate produced by the merge of the capability they need, never waiting for a package closure task; one merge queue.; RES-desktopplatform-policy-data (append): Generated policy data is regenerated from its pinned source and never hand-edited; the reason-code registry is append-only with stable codes; each task adds its own test classes and evidence rows.

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): P2-017: offline verify/policy tests; one local opt-in clean-consumer check of the packed ArcForges.Capabilities package (the PLT.53 precedent, Plan ledger/tasks/plt-53.md): a throwaway consumer restores only the package under test from an isolated temporary package source and the package cache, with no project reference, sibling-source fallback or substitute package, then builds and runs the invalid/stale-invocation and opaque-reference scenarios, performed once and recorded with source commit, package identity and result, stating whether the consumed bytes were the exact prepublication CI candidate or a locally packed equivalent. No hosted installed-package consumer, permanent consumer harness or repeated public download is added (P2-017). Real cross-product UI acceptance is deferred to product WPs (14/18/33/36) that actually consume this package.
Completion evidence for the ledger: Owned artifact and real-integration receipt per the WP-09.90 template, including the single recorded local opt-in clean-consumer run and its stated limits (what the consumer did not exercise, and whether it consumed the CI candidate or a locally packed equivalent).
Notes: ADP-07 binding for the package activation of one existing project (2026-10-04; DLV-34, scope moves only: no obligation, edge or acceptance is added, removed or retyped). The Outcome text says ArcForges.Capabilities packages the Contributions internals; the repository shows the opposite structure: ArcForges.Capabilities has been catalogued, packed and published since PLT.19/PLT.24 (its catalogue row, with the exact ArcForges.Sdk.Contracts 1.0.0-ci.216.1 external dependency, is already in eng/packaging/packages.json), while ArcForges.Contributions is a separate project that references ArcForges.Capabilities, so Capabilities cannot contain it, and Contributions sets IsPackable false and has no catalogue row. The task title and package acceptance (WP-09) name both. The planned scope listed only the catalogue and the version-source file, which cannot activate the second package: the packable-iff-listed repository policy test (RepositoryPolicyTests.PublishedProjectsAreExplicitAndContainNoPlaceholders) requires each listed project to set IsPackable, and the dependency-admission gate binds the hash of every project file and of packages.json. PLT.53 and PLT.16 needed and received the same activation scope. The write scope is exactly the paths listed above. The activation flips one property on an existing project whose PackageId, readme and licence/notice pack items are already present and appends one catalogue entry whose dependency list must equal the nuspec dependency set that dotnet pack generates (checked with packages.validate_generated_dependencies); it adds no project reference, package reference, central version or source behavior, so the locked NuGet closure keeps identical coordinates, versions and content hashes. No package identity beyond ArcForges.Capabilities (already published, unchanged) and ArcForges.Contributions (existing PackageId) is introduced. eng/version-sources.json is changed only if the existing PackageVersion axis cannot already enumerate the catalogue; the CapabilityVersion axis stays not-produced because neither package owns a product capability descriptor. Resource owners and protocols: RES-desktopplatform-package-inventory (append) for the catalogue entry, RES-desktopplatform-build-config (append) for the project file, and RES-desktopplatform-policy-data (append) for the receipt chain, provenance row and reconciliation snapshot; re-append after rebase and chain the receipt from the receipt active on main at merge. Not authorized: any other source file, any test, any packages.lock.json, Directory.Packages.props, workflow, .gitleaks.toml or scan allowlist, eng/policy/architecture-contract-tests.json, or any other task's rows. Real-integration verification stays within P2-017: one local opt-in consumer of the locally packed ArcForges.Capabilities and ArcForges.Contributions packages outside the repository; no installed-package consumer in CI, no GUI or browser end-to-end, no download or hash audit of published bytes. Outcome (read as: ArcForges.Capabilities and the separate ArcForges.Contributions package it was grouped with), prerequisites and completion evidence are otherwise unchanged.
```

```text
Execute ArcForges delivery task PLT.26 — Token system and theming.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\platform.md (anchor task-plt-26).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/plt-26 (python tools/delivery.py claim PLT.26 --worker <name>); task branch task/plt-26 in DesktopPlatform; ledger record ledger/tasks/plt-26.md.
Kind/size: producer/M. Baseline: not-started.
Outcome: Semantic tokens for colour/typography/spacing/radius/elevation/motion with light/dark/high-contrast themes and first-class density modes; no component references a raw literal.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-10.00 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\10-design-system-and-desktop-shell.md, anchor rule-wp-10.00
- WP-10:reconciliation-of-the-five-legacy-src-bu Reconciliation of the five legacy src/BuildingBlocks/ArcForges.Desktop.{Experience,Graphics,Preview,RichContent,Text} scaffold projects per WP-01.02 into DesignSystem/Shell (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\10-design-system-and-desktop-shell.md, package-level obligation

Entry condition: adoption slice ADOPT.02.platform is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] PRF.02: a proven Avalonia Native AOT publish with zero trim/AOT diagnostics
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:src/DesignSystem/ArcForges.DesignSystem/**
Shared resources (follow the owner protocol): RES-desktopplatform-build-config (append): Solution/project lists, central package versions and CI job lists are appended by the task that adds a project, dependency or job; dependency additions follow the dependency-admission policy with a reviewed receipt; lock files are regenerated after rebase and never hand-merged; the integration owner resolves ordering conflicts at merge.
Unblocks: PLT.27, PLT.29, PLT.31, PLT.35

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline tests: policy test asserting no raw colour/size literal in component code; contrast tests across every theme; density snapshot suite. Real AOT publish-with-zero-diagnostics evidence is local opt-in, recorded at PLT.34/PLT.35.
Completion evidence for the ledger: Raw-literal policy result and contrast reports per theme.
```

```text
Execute ArcForges delivery task PLT.27 — Windows, panels and layout.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\platform.md (anchor task-plt-27).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/plt-27 (python tools/delivery.py claim PLT.27 --worker <name>); task branch task/plt-27 in DesktopPlatform; ledger record ledger/tasks/plt-27.md.
Kind/size: producer/L. Baseline: not-started.
Outcome: Multi-window-per-instance window model, dockable/collapsible panel host, device-local layout persistence resilient to a missing panel or changed screen configuration.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-10.01 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\10-design-system-and-desktop-shell.md, anchor rule-wp-10.01
- WP-10:reconciliation-of-the-five-legacy-src-bu Reconciliation of the five legacy src/BuildingBlocks/ArcForges.Desktop.{Experience,Graphics,Preview,RichContent,Text} scaffold projects per WP-01.02 into DesignSystem/Shell (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\10-design-system-and-desktop-shell.md, package-level obligation

Entry condition: adoption slice ADOPT.02.platform is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] PLT.26: token system
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:src/DesignSystem/ArcForges.Desktop.Shell/**; DesktopPlatform:Directory.Packages.props (append only ArcForges.Desktop.Shell and ArcForges.Desktop.Shell.Tests to the existing ArcForges.Contracts.Foundation 1.0.0-ci.216.1 MSBuildProjectName selector; preserve the 1.0.0-ci.113.1 default); DesktopPlatform:eng/policy/architecture-contract-tests.json (append only exact PLT.27 public API to direct-test bindings); DesktopPlatform:eng/policy/architecture-projects.json (append only the PLT.27 Shell production and test project classifications); DesktopPlatform:eng/policy/dependency-policy.json (refresh only exact task-owned input hashes and active receipt pointer); DesktopPlatform:eng/policy/dependency-reviews/plt-27-r1.json (one immutable PLT.27 dependency receipt successor after rebase); DesktopPlatform:eng/policy/licence-boundary.json (append only exact PLT.27 Shell production and test project rows); DesktopPlatform:eng/policy/runtime-ownership.json (append only exact PLT.27 Shell production and test project rows); DesktopPlatform:eng/policy/reconciliation/active-projects.json (append only exact PLT.27 Shell project registrations); DesktopPlatform:eng/policy/reconciliation/directories.json (append only exact PLT.27 Shell directory registrations); DesktopPlatform:eng/policy/reconciliation/source.json (refresh only the exact source inventory snapshot required by the existing reconciliation gate); DesktopPlatform:eng/provenance/files.json (append only exact PLT.27-owned firstParty paths and immutable receipt)
Shared resources (follow the owner protocol): RES-desktopplatform-build-config (append): Solution/project lists, central package versions and CI job lists are appended by the task that adds a project, dependency or job; dependency additions follow the dependency-admission policy with a reviewed receipt; lock files are regenerated after rebase and never hand-merged; the integration owner resolves ordering conflicts at merge.; RES-desktopplatform-policy-data (append): Generated policy data is regenerated from its pinned source and never hand-edited; the reason-code registry is append-only with stable codes; each task adds its own test classes and evidence rows.
Unblocks: APP.08, PLT.28, PLT.29, PLT.30, PLT.31, PLT.33, PLT.35

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline tests: restore tests across missing panel, changed display arrangement, corrupted layout state; device-local assertion.
Completion evidence for the ledger: Layout restore matrix.
Notes: ADP-07 support is limited to the exact policy, reconciliation, provenance and central package configuration paths listed above, required to bind the task-owned Shell production/test projects, APIs, direct tests, source files and project locks to existing gates. The only Directory.Packages.props change authorized is to append ArcForges.Desktop.Shell and ArcForges.Desktop.Shell.Tests to the existing ArcForges.Contracts.Foundation 1.0.0-ci.216.1 MSBuildProjectName selector introduced by PLT.19. This changes only those two projects' selection from the repository-wide 1.0.0-ci.113.1 default to the already-admitted 1.0.0-ci.216.1 coordinate; preserve that default and all other selectors. Package identity, the available package coordinate/version set and aggregate dependency closure remain unchanged. The only corresponding semantic lock changes permitted are in src/DesignSystem/ArcForges.Desktop.Shell/packages.lock.json and src/DesignSystem/ArcForges.Desktop.Shell/Tests/packages.lock.json, reflecting that exact Foundation project edge; no other lockfile may change semantically. The PLT.27 dependency-policy/plt-27-r1 successor must record exactly these 19 consumers of 1.0.0-ci.216.1: LocalRpcAotTests, ArcForges.Application.Abstractions, ArcForges.Capabilities, ArcForges.Capabilities.Tests, ArcForges.ContentSandbox, ArcForges.Contributions, ArcForges.Contributions.Tests, ArcForges.Foundation, ArcForges.Foundation.Tests, ArcForges.Observability, ArcForges.Observability.Tests, ArcForges.Persistence.Resources, ArcForges.Persistence.Resources.Tests, ArcForges.Persistence.Sqlite, ArcForges.Security, ArcForges.Security.Tests, ArcForges.Tests.PersistenceTests, ArcForges.Desktop.Shell and ArcForges.Desktop.Shell.Tests. Preserve the immutable PLT.19 receipt as the PLT.27 successor's direct predecessor and the complete PLT.19 history. Append only exact task-owned rows; refresh only exact input hashes, the current immutable dependency-review successor and the existing reconciliation snapshot fields required by those paths. Preserve unrelated records, policy semantics, schemas, generators and checkers. Do not activate packages or change package inventory, package identity, available coordinate/version set, aggregate dependency closure, or PLT.35's package-activation boundary. These bindings use RES-desktopplatform-policy-data for task-owned policy/architecture/traceability entries and retain RES-desktopplatform-build-config for solution, central package selector, CI and the two project locks; no other shared resource is authorized. Task outcome, prerequisites and runtime behavior remain unchanged.
```

```text
Execute ArcForges delivery task PLT.28 — Command system.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\platform.md (anchor task-plt-28).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/plt-28 (python tools/delivery.py claim PLT.28 --worker <name>); task branch task/plt-28 in DesktopPlatform; ledger record ledger/tasks/plt-28.md.
Kind/size: producer/M. Baseline: not-started.
Outcome: Command registry with availability, shortcut binding, command palette and conflict detection; command availability is computed from the same evaluation the capability model uses so command and capability never disagree.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-10.02 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\10-design-system-and-desktop-shell.md, anchor rule-wp-10.02

Entry condition: adoption slice ADOPT.02.platform is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] PLT.27: window/panel host
- [artifact] PLT.20: capability availability evaluation (WP-09.03)
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:src/DesignSystem/ArcForges.Desktop.Shell/**; DesktopPlatform:eng/policy/dependency-policy.json (refresh exact existing Shell project/lock input hashes and active receipt pointer only); DesktopPlatform:eng/policy/dependency-reviews/plt-28-r1.json (new immutable PLT.28 successor receipt; preserve the dependency coordinate/version set and package closure); DesktopPlatform:eng/policy/reconciliation/active-projects.json (refresh only the existing Shell production csproj blob row); DesktopPlatform:eng/provenance/files.json (append only firstParty rows for the two PLT.28-owned C# source/test files and the immutable plt-28-r1 dependency receipt); DesktopPlatform:eng/policy/architecture-contract-tests.json (append only five exact PLT.28 public API-to-direct-[Fact] mappings)
Shared resources (follow the owner protocol): RES-desktopplatform-build-config (append): Solution/project lists, central package versions and CI job lists are appended by the task that adds a project, dependency or job; dependency additions follow the dependency-admission policy with a reviewed receipt; lock files are regenerated after rebase and never hand-merged; the integration owner resolves ordering conflicts at merge.; RES-desktopplatform-policy-data (append): Generated policy data is regenerated from its pinned source and never hand-edited; the reason-code registry is append-only with stable codes; each task adds its own test classes and evidence rows.; RES-architecture-tests (append): Each repository policy task owns its suite; rule additions are append-only.
Unblocks: PLT.32, PLT.35

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline tests: normalized shortcut binding resolution and conflict detection; availability agreement tests against the capability model; palette search relevance tests.
Completion evidence for the ledger: Shortcut-binding/conflict, capability-availability-agreement and palette-search-relevance results; exact Shell project/lock input binding with no package coordinate/version or closure expansion.
Notes: PLT.28 uses the existing Shell→Capabilities project edge explicitly listed by architecture 27 and delegates every command availability request to the public ICapabilityProvider evaluation; it does not copy or approximate capability rules. Shortcut binding is resolvable by normalized gesture through the task-owned in-process registry, with invocation/dispatch lifecycle remaining PLT.32 scope. ADP-07 support is limited to the exact paths above. Regenerate the two owned Shell packages.lock.json files only to represent the new internal Capabilities project edge; preserve every existing package coordinate, resolved version, content hash and unrelated row, with no non-project dependency closure change. Refresh only exact Shell project/lock input hashes and the active receipt pointer in dependency-policy; the existing Shell test csproj hash remains unchanged. The sole new immutable receipt is plt-28-r1 and must chain from the active dependency review on the final rebased base; never rewrite earlier receipts. The only reconciliation change is the existing Shell production csproj blob in active-projects.json; source.json, current/historical snapshots, project roster and other project bindings stay unchanged. Provenance adds only firstParty rows for Commands/CommandPalette.cs, Tests/CommandPaletteTests.cs and the immutable eng/policy/dependency-reviews/plt-28-r1.json receipt; preserve every existing classification. Architecture-contract-tests adds only five exact API-symbol→direct-[Fact] bindings: ArcForges.Desktop.Shell.Commands.ShellCommandPalette.TryRegister(ArcForges.Desktop.Shell.Commands.ShellCommand)→ArcForges.Desktop.Shell.Tests.CommandPaletteTests.TryRegisterRejectsDuplicateIdsAndNormalizedShortcutConflictsAtomically; ArcForges.Desktop.Shell.Commands.ShellCommandPalette.Snapshot()→ArcForges.Desktop.Shell.Tests.CommandPaletteTests.SnapshotIsStableReadOnlyAndOrderedByCommandId; ArcForges.Desktop.Shell.Commands.ShellCommandPalette.SearchPalette(string, int)→ArcForges.Desktop.Shell.Tests.CommandPaletteTests.SearchPaletteRanksRelevantMatchesDeterministicallyWithoutAvailabilityEvaluation; ArcForges.Desktop.Shell.Commands.ShellCommandPalette.EvaluateAvailabilityAsync(string, ArcForges.Capabilities.FrozenContextSnapshot, System.Threading.CancellationToken)→ArcForges.Desktop.Shell.Tests.CommandPaletteTests.AvailabilityEvaluationAgreesWithTheCanonicalCapabilityProvider; ArcForges.Desktop.Shell.Commands.ShellCommandPalette.TryResolveShortcut(ArcForges.Desktop.Shell.Commands.CommandShortcut, out ArcForges.Desktop.Shell.Commands.ShellCommand?)→ArcForges.Desktop.Shell.Tests.CommandPaletteTests.TryResolveShortcutUsesNormalizedBindingsAndRefusesUnknownGestures. Do not change Directory.Packages.props, package manifests/inventories/identity, solution/workflows, licences, runtime ownership, other project files, policy schemas/checkers/generators or package activation. The outcome and prerequisites remain unchanged.
```

```text
Execute ArcForges delivery task PLT.29 — Scoped settings.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\platform.md (anchor task-plt-29).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/plt-29 (python tools/delivery.py claim PLT.29 --worker <name>); task branch task/plt-29 in DesktopPlatform; ledger record ledger/tasks/plt-29.md.
Kind/size: producer/M. Baseline: not-started.
Outcome: Fixed scope resolution (application/workspace/device/instance), typed schemas, migration on schema change, explainable effective value; device-scoped settings never sync.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-10.03 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\10-design-system-and-desktop-shell.md, anchor rule-wp-10.03

Entry condition: adoption slice ADOPT.02.platform is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] PLT.26: token/theming groundwork
- [artifact] PLT.04: migration runner pattern (WP-07.03)
Completion prerequisites (may start earlier; cannot complete before these are complete):
- [integration] PLT.27: PLT.27 Shell project and test host are integrated

Permitted write scope: DesktopPlatform:src/DesignSystem/ArcForges.Desktop.Shell/**; DesktopPlatform:eng/policy/architecture-contract-tests.json (append only six PLT.29 public API to direct-[Fact] test bindings); DesktopPlatform:eng/provenance/files.json (append only four PLT.29 Settings first-party source/test paths)
Shared resources (follow the owner protocol): RES-desktopplatform-policy-data (append): Generated policy data is regenerated from its pinned source and never hand-edited; the reason-code registry is append-only with stable codes; each task adds its own test classes and evidence rows.; RES-architecture-tests (append): Each repository policy task owns its suite; rule additions are append-only.
Unblocks: PLT.35

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline tests: resolution order tests across every scope combination; explainability tests; migration test.
Completion evidence for the ledger: Settings resolution and explainability results.
Notes: The only supporting-file additions are six exact public ordinary API-to-direct-[Fact] bindings in eng/policy/architecture-contract-tests.json for DeviceLocalSettingsStore.CreateSyncSnapshot, DeviceLocalSettingsStore.Load, DeviceLocalSettingsStore.Save, ISettingSchema.Migrate, ScopedSettingsResolver.Resolve<T>, and SettingDefinition<T>.ToStoredValue; and four first-party provenance entries in eng/provenance/files.json for src/DesignSystem/ArcForges.Desktop.Shell/Settings/DeviceLocalSettingsStore.cs, src/DesignSystem/ArcForges.Desktop.Shell/Settings/ScopedSettings.cs, src/DesignSystem/ArcForges.Desktop.Shell/Settings/ScopedSettingsResolver.cs, and src/DesignSystem/ArcForges.Desktop.Shell/Tests/Settings/ScopedSettingsTests.cs. The six bindings target the task-owned direct [Fact] methods SynchronizationProjectionNeverIncludesDeviceOrInstanceSettings, StoreMigratesOlderValuesAtomicallyAndRefusesDowngradeWithoutChangingTheFile, and ResolutionCoversEveryScopeCombinationAndExplainsTheWinningSource. No project, csproj, solution, workflow, lock, dependency input/closure, immutable dependency-admission receipt, licence, runtime ownership, reconciliation, package inventory/identity, NOTICE, checker, or algorithm changes are in scope.
```

```text
Execute ArcForges delivery task PLT.30 — Attention and notification model.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\platform.md (anchor task-plt-30).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/plt-30 (python tools/delivery.py claim PLT.30 --worker <name>); task branch task/plt-30 in DesktopPlatform; ledger record ledger/tasks/plt-30.md.
Kind/size: producer/M. Baseline: not-started.
Outcome: Attention items classified by durability; a durable item (pending approval, failed task) persists until resolved regardless of a missed transient notification; lock-screen/system-notification content is non-sensitive by default.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-10.04 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\10-design-system-and-desktop-shell.md, anchor rule-wp-10.04

Entry condition: adoption slice ADOPT.02.platform is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] PLT.27: window/panel host
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:src/DesignSystem/ArcForges.Desktop.Shell/**; DesktopPlatform:eng/policy/architecture-contract-tests.json (append only four exact PLT.30 public ordinary API-to-direct-[Fact] bindings); DesktopPlatform:eng/provenance/files.json (append only firstParty classifications for the two PLT.30-owned Attention source and test files)
Shared resources (follow the owner protocol): RES-architecture-tests (append): Each repository policy task owns its suite; rule additions are append-only.; RES-desktopplatform-policy-data (append): Generated policy data is regenerated from its pinned source and never hand-edited; the reason-code registry is append-only with stable codes; each task adds its own test classes and evidence rows.
Unblocks: PLT.35

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline tests: missed-notification test asserting durable state survives; sensitivity test on notification content.
Completion evidence for the ledger: Missed-notification durability result.
Notes: The only supporting-file additions are four exact public ordinary API-to-direct-[Fact] bindings in eng/policy/architecture-contract-tests.json and two firstParty classifications in eng/provenance/files.json for src/DesignSystem/ArcForges.Desktop.Shell/Attention/AttentionModel.cs and src/DesignSystem/ArcForges.Desktop.Shell/Tests/AttentionModelTests.cs. Bind ArcForges.Desktop.Shell.AttentionModel.Publish(ArcForges.Desktop.Shell.AttentionItem, System.Func<ArcForges.Desktop.Shell.SystemNotificationContent, bool>?, ArcForges.Desktop.Shell.NotificationPreviewConsent), ArcForges.Desktop.Shell.AttentionModel.Snapshot(), and ArcForges.Desktop.Shell.AttentionModel.RemoveResolved(string) directly to ArcForges.Desktop.Shell.Tests.AttentionModelTests.MissedNotificationLeavesDurableAttentionUntilOwnerResolvesIt(); bind ArcForges.Desktop.Shell.AttentionModel.CreateSystemNotificationContent(ArcForges.Desktop.Shell.AttentionItem, ArcForges.Desktop.Shell.NotificationPreviewConsent) directly to ArcForges.Desktop.Shell.Tests.AttentionModelTests.SensitiveSystemNotificationUsesGenericContentUnlessPreviewConsentIsExplicit(). RES-architecture-tests and RES-desktopplatform-policy-data are append-only task-owned rows under their existing protocols. No project, csproj, solution, workflow, lock, dependency input/closure, immutable dependency-admission receipt, licence, runtime ownership, reconciliation, package inventory/identity, NOTICE, checker, algorithm, or unrelated architecture/provenance row changes are authorized. The outcome and prerequisite remain unchanged.
```

```text
Execute ArcForges delivery task PLT.31 — Error presentation.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\platform.md (anchor task-plt-31).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/plt-31 (python tools/delivery.py claim PLT.31 --worker <name>); task branch task/plt-31 in DesktopPlatform; ledger record ledger/tasks/plt-31.md.
Kind/size: producer/S. Baseline: not-started.
Outcome: Errors are presented from the reason-code registry with a human-readable statement, retry guidance and a support reference identifier; a raw exception message never reaches the user.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-10.05 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\10-design-system-and-desktop-shell.md, anchor rule-wp-10.05

Entry condition: adoption slice ADOPT.02.platform is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] PLT.26: token system
- [artifact] FND.05: reason-code registry
Completion prerequisites (may start earlier; cannot complete before these are complete):
- [integration] PLT.27: PLT.27 Shell project and test host are integrated

Permitted write scope: DesktopPlatform:src/DesignSystem/ArcForges.Desktop.Shell/**; DesktopPlatform:eng/policy/architecture-contract-tests.json (append only the exact PLT.31 ErrorPresenter.Present(TypedFailure) to direct-[Fact] test binding); DesktopPlatform:eng/provenance/files.json (append only the three PLT.31 Errors source/resource/test first-party paths)
Shared resources (follow the owner protocol): RES-desktopplatform-policy-data (append): Generated policy data is regenerated from its pinned source and never hand-edited; the reason-code registry is append-only with stable codes; each task adds its own test classes and evidence rows.; RES-architecture-tests (append): Each repository policy task owns its suite; rule additions are append-only.
Unblocks: PLT.35, PLT.52

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline tests: no raw exception text displayed; coverage that every registered reason code has a message.
Completion evidence for the ledger: Raw-exception prohibition and reason-code coverage.
Notes: The only supporting-file additions are one exact ordinary public API-to-direct-[Fact] binding in eng/policy/architecture-contract-tests.json: ArcForges.Desktop.Shell.Errors.ErrorPresenter.Present(ArcForges.Foundation.Errors.TypedFailure) maps to ArcForges.Desktop.Shell.Tests.ErrorPresentationTests.PresentationUsesOnlyRegisteredTextAndNeverEchoesExceptionDetailsOrPaths(). The only first-party provenance additions are src/DesignSystem/ArcForges.Desktop.Shell/Errors/ErrorPresentationStrings.resx, src/DesignSystem/ArcForges.Desktop.Shell/Errors/ErrorPresenter.cs, and src/DesignSystem/ArcForges.Desktop.Shell/Tests/ErrorPresentationTests.cs. No project, csproj, solution, workflow, lock, dependency input/closure, immutable dependency-admission receipt, licence, runtime ownership, reconciliation, package inventory/identity, NOTICE, checker, or algorithm changes are in scope.
```

```text
Execute ArcForges delivery task PLT.32 — Lifecycle, menus and shutdown.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\platform.md (anchor task-plt-32).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/plt-32 (python tools/delivery.py claim PLT.32 --worker <name>); task branch task/plt-32 in DesktopPlatform; ledger record ledger/tasks/plt-32.md.
Kind/size: producer/M. Baseline: not-started.
Outcome: Start-up sequence within budget; single-instance routing; shutdown prompts stating consequences when work is running/unsaved; menu contribution from the command registry.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-10.06 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\10-design-system-and-desktop-shell.md, anchor rule-wp-10.06

Entry condition: adoption slice ADOPT.02.platform is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] PLT.28: command registry
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:src/DesignSystem/ArcForges.Desktop.Shell/**; DesktopPlatform:eng/policy/architecture-contract-tests.json (append only the five exact PLT.32 public API-to-direct-[Fact] mappings listed in Notes)
Shared resources (follow the owner protocol): RES-architecture-tests (append): Each repository policy task owns its suite; rule additions are append-only.
Unblocks: APP.07, PLT.35, SCOPE.09, UPD.03

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline tests: startup budget measurement for the ArcScope host (local perf harness, not hosted CI); shutdown-during-work test; single-instance routing test.
Completion evidence for the ledger: Startup budget measurements and shutdown-during-work result.
Notes: The only supporting-file write outside Shell/** is an append-only update to eng/policy/architecture-contract-tests.json, protected by the existing RES-architecture-tests append protocol. Add exactly these five public ordinary API-to-discoverable direct-[Fact] bindings, and no others: ArcForges.Desktop.Shell.Commands.ShellCommandPalette.GetMenuContributions() -> ArcForges.Desktop.Shell.Tests.CommandPaletteTests.GetMenuContributionsUsesRegisteredCommandIdentityAndStableOrder(); ArcForges.Desktop.Shell.ShellLifecycleCoordinator.RunStartupAsync(System.Threading.CancellationToken) -> ArcForges.Desktop.Shell.Tests.ShellLayoutTests.RunStartupAsyncRunsLocalWorkBeforeBackgroundAndReturnsMeasurement(); ArcForges.Desktop.Shell.ShellLifecycleCoordinator.RouteActivationAsync(ArcForges.Desktop.Shell.ShellActivationRequest, System.Threading.CancellationToken) -> ArcForges.Desktop.Shell.Tests.ShellLayoutTests.RouteActivationAsyncForwardsSecondaryLaunchToPrimaryExactlyOnce(); ArcForges.Desktop.Shell.ShellLifecycleCoordinator.CreateShutdownPrompt(ArcForges.Desktop.Shell.ShellShutdownState) -> ArcForges.Desktop.Shell.Tests.ShellLayoutTests.CreateShutdownPromptStatesRunningAndUnsavedConsequences(); ArcForges.Desktop.Shell.ShellLifecycleCoordinator.ExecuteShutdownAsync(ArcForges.Desktop.Shell.ShellShutdownState, ArcForges.Desktop.Shell.ShellShutdownDecision, System.Threading.CancellationToken) -> ArcForges.Desktop.Shell.Tests.ShellLayoutTests.ExecuteShutdownAsyncRequiresChoiceAndRunsDrainInOrderWithoutLosingWork(). Each Fact must directly invoke its mapped public method and assert observable behavior; retain the existing RP-10 checker/schema and every pre-existing mapping. PLT.32 may report only task-local Shell lifecycle-path timing, not an ArcScope product startup result. This authority adds no producer or completion edge and does not satisfy WP-10.06's ArcScope cold-process-to-usable-workspace release-AOT P95 <=2.5s reference-hardware acceptance; do not mark the task complete until that existing product measurement is actually available. No other supporting path, algorithm, dependency, project, lock, solution, workflow, or task prerequisite/outcome is changed.
```

```text
Execute ArcForges delivery task PLT.33 — Accessibility and localisation baseline.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\platform.md (anchor task-plt-33).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/plt-33 (python tools/delivery.py claim PLT.33 --worker <name>); task branch task/plt-33 in DesktopPlatform; ledger record ledger/tasks/plt-33.md.
Kind/size: producer/L. Baseline: not-started.
Outcome: Every shell surface carries assistive-technology semantics, correct focus order and keyboard reachability; all strings externalised; RTL layout supported structurally.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-10.07 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\10-design-system-and-desktop-shell.md, anchor rule-wp-10.07

Entry condition: adoption slice ADOPT.02.platform is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] PLT.27: window/panel/layout
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:src/DesignSystem/ArcForges.Desktop.Shell/**; DesktopPlatform:tests/DesktopUiTests/**; DesktopPlatform:eng/policy/architecture-contract-tests.json (append only the fifteen exact PLT.33 public ordinary API-to-direct-[Fact] bindings listed in Notes); DesktopPlatform:eng/provenance/files.json (append only the seventeen exact PLT.33 first-party Shell source, resource and test paths listed in Notes)
Shared resources (follow the owner protocol): RES-desktopplatform-build-config (append): Solution/project lists, central package versions and CI job lists are appended by the task that adds a project, dependency or job; dependency additions follow the dependency-admission policy with a reviewed receipt; lock files are regenerated after rebase and never hand-merged; the integration owner resolves ordering conflicts at merge.; RES-desktopplatform-policy-data (append): Generated policy data is regenerated from its pinned source and never hand-edited; the reason-code registry is append-only with stable codes; each task adds its own test classes and evidence rows.; RES-architecture-tests (append): Each repository policy task owns its suite; rule additions are append-only.
Unblocks: PLT.35

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline automated accessibility checks plus pseudo-localisation pass and RTL layout pass run in CI; the dated manual assistive-technology verification is explicit local opt-in per P2-017 (device/GUI testing is excluded from hosted CI).
Completion evidence for the ledger: Accessibility automated plus dated manual record; pseudo-localisation report.
Notes: The only supporting-file additions are fifteen exact ordinary public API-to-direct-[Fact] bindings in eng/policy/architecture-contract-tests.json, each with testProject src/DesignSystem/ArcForges.Desktop.Shell/Tests/ArcForges.Desktop.Shell.Tests.csproj, and no others: ArcForges.Desktop.Shell.Localization.ShellMessageFormatter.Format(string, System.Collections.Generic.IReadOnlyDictionary<string, object?>?, System.Globalization.CultureInfo) -> ArcForges.Desktop.Shell.Tests.Localization.MessageFormatterTests.FormatSubstitutesNamedArgumentsAndSelectsPluralBranchesWithLocaleNumbers(); ArcForges.Desktop.Shell.Localization.PseudoLocaliser.Transform(string) -> ArcForges.Desktop.Shell.Tests.Localization.PseudoLocalisationTests.TransformMarksWholeMessagesAccentsLettersAndPreservesPlaceholdersAndPlurals(); ArcForges.Desktop.Shell.Localization.PseudoLocaliser.IsWholePseudoMessage(string) -> ArcForges.Desktop.Shell.Tests.Localization.PseudoLocalisationTests.TransformExpandsTextAndRejectsInvalidPatterns(); ArcForges.Desktop.Shell.Localization.ShellText.Resolve(ArcForges.Desktop.Shell.Localization.LocalizedText, System.Globalization.CultureInfo?) -> ArcForges.Desktop.Shell.Tests.Localization.PseudoLocalisationTests.ResolveFailsClosedForAnUndefinedKeyWithoutLeakingIt(); ArcForges.Desktop.Shell.Localization.ShellText.BeginPseudoLocalisation() -> ArcForges.Desktop.Shell.Tests.Localization.PseudoLocalisationTests.PseudoLocalisationIsScopedToTheExecutionFlowAndRestoresOnDispose(); ArcForges.Desktop.Shell.Localization.FlowDirections.FromCulture(System.Globalization.CultureInfo) -> ArcForges.Desktop.Shell.Tests.Localization.FlowDirectionTests.FromCultureClassifiesReadingDirection(); ArcForges.Desktop.Shell.Localization.FlowDirections.ToPhysical(ArcForges.Desktop.Shell.DockRegion, ArcForges.Desktop.Shell.Localization.FlowDirection) -> ArcForges.Desktop.Shell.Tests.Localization.FlowDirectionTests.ToPhysicalMirrorsOnlyTheLeadingAndTrailingEdgesInRightToLeft(); ArcForges.Desktop.Shell.Localization.FlowDirections.MirrorX(double, double, double) -> ArcForges.Desktop.Shell.Tests.Localization.FlowDirectionTests.MirrorXReflectsSpansExactlyAndIsItsOwnInverse(); ArcForges.Desktop.Shell.Accessibility.ShellAccessibilityAudit.Evaluate(System.Collections.Generic.IEnumerable<ArcForges.Desktop.Shell.Accessibility.ShellSurface>, System.Globalization.CultureInfo?) -> ArcForges.Desktop.Shell.Tests.Accessibility.ShellAccessibilityAuditTests.AuditReportsEachContractViolationWithItsStableRule(); ArcForges.Desktop.Shell.Accessibility.FocusNavigator.MoveNext() -> ArcForges.Desktop.Shell.Tests.Accessibility.FocusNavigatorTests.TabAndShiftTabVisitEveryTabStopInFocusOrderAndWrap(); ArcForges.Desktop.Shell.Accessibility.FocusNavigator.MovePrevious() -> ArcForges.Desktop.Shell.Tests.Accessibility.FocusNavigatorTests.TabAndShiftTabVisitEveryTabStopInFocusOrderAndWrap(); ArcForges.Desktop.Shell.Accessibility.FocusNavigator.Move(ArcForges.Desktop.Shell.Accessibility.FocusDirection) -> ArcForges.Desktop.Shell.Tests.Accessibility.FocusNavigatorTests.ArrowKeysMoveInsideARovingGroupWithoutWrappingAndKeepTheGroupAsOneTabStop(); ArcForges.Desktop.Shell.Accessibility.FocusNavigator.Activate() -> ArcForges.Desktop.Shell.Tests.Accessibility.FocusNavigatorTests.ModalSurfaceTrapsFocusAndDismissRestoresTheOriginatingElement(); ArcForges.Desktop.Shell.Accessibility.FocusNavigator.OpenModal(ArcForges.Desktop.Shell.Accessibility.ShellSurface) -> ArcForges.Desktop.Shell.Tests.Accessibility.FocusNavigatorTests.ModalSurfaceTrapsFocusAndDismissRestoresTheOriginatingElement(); ArcForges.Desktop.Shell.Accessibility.FocusNavigator.Dismiss() -> ArcForges.Desktop.Shell.Tests.Accessibility.FocusNavigatorTests.ModalSurfaceTrapsFocusAndDismissRestoresTheOriginatingElement(). Each Fact must directly invoke its mapped public method and assert observable behavior; retain the existing RP-10 checker/schema and every pre-existing mapping. The only first-party provenance additions in eng/provenance/files.json are these seventeen paths under src/DesignSystem/ArcForges.Desktop.Shell/: Accessibility/AccessibleNode.cs, Accessibility/FocusNavigator.cs, Accessibility/ShellAccessibilityAudit.cs, Accessibility/ShellSurfaceCatalog.cs, Localization/FlowDirection.cs, Localization/LocalizedText.cs, Localization/MessagePattern.cs, Localization/PseudoLocaliser.cs, Localization/ShellMessageFormatter.cs, Localization/ShellStrings.resx, Localization/ShellText.cs, Tests/Accessibility/FocusNavigatorTests.cs, Tests/Accessibility/KeyboardOnlyWorkflowTests.cs, Tests/Accessibility/ShellAccessibilityAuditTests.cs, Tests/Localization/FlowDirectionTests.cs, Tests/Localization/MessageFormatterTests.cs, Tests/Localization/PseudoLocalisationTests.cs. Existing Shell files change only to route the existing ErrorPresenter, AttentionModel and ShellLifecycleCoordinator text through the shared resolver without changing behavior, to migrate the three PLT.32 shutdown-consequence resources in Errors/ErrorPresentationStrings.resx from positional item(s) placeholders to named plural patterns (the only text change, with the PLT.32 ShellLayoutTests prompt-text helper following it), and to document dock-edge and accessibility semantics in LayoutModel.cs and README.md. No project, csproj, solution, workflow, lock, dependency input or closure, immutable dependency-admission receipt, licence, runtime ownership, reconciliation, package inventory or identity, NOTICE, checker or algorithm change is in scope, and no UI framework or third-party control is introduced or admitted (the PLT.34 admission record is unchanged). The shell remains framework-neutral, so this task delivers the accessibility, keyboard-focus, localisation, pseudo-localisation and structural right-to-left contracts and their offline automated tests inside the existing Shell nested test project. tests/DesktopUiTests is not created: its F-09 purpose (framework-hosted component and automation tests with screenshots) needs a UI adapter and a GUI host, which hosted CI excludes under P2-017. This authority does not satisfy the dated manual assistive-technology verification of WP-10.07, which needs a real UI adapter; the task ledger must record it as untested until that evidence exists.
```

```text
Execute ArcForges delivery task PLT.34 — Third-party control admission.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\platform.md (anchor task-plt-34).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/plt-34 (python tools/delivery.py claim PLT.34 --worker <name>); task branch task/plt-34 in DesktopPlatform; ledger record ledger/tasks/plt-34.md.
Kind/size: producer/M. Baseline: not-started.
Outcome: Every third-party control the shell uses passes a real AOT publish proof with zero diagnostics before adoption, with a recorded licence position per control.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-10.08 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\10-design-system-and-desktop-shell.md, anchor rule-wp-10.08

Entry condition: adoption slice ADOPT.02.platform is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] PRF.02: the established AOT-publish-with-zero-diagnostics harness/process
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:src/DesignSystem/**; DesktopPlatform:docs/**
Unblocks: PLT.35, PRF.09

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Per-control real AOT publish proof - genuinely requires local/CI compilation (Windows/Linux AOT publish IS in the retained CI scope per P2-017), so this can run in CI unlike device/GUI checks.
Completion evidence for the ledger: Per-control AOT proofs and licence records.
```

```text
Execute ArcForges delivery task PLT.35 — Publish DesignSystem/Shell packages and verify real integration.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\platform.md (anchor task-plt-35).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/plt-35 (python tools/delivery.py claim PLT.35 --worker <name>); task branch task/plt-35 in DesktopPlatform; ledger record ledger/tasks/plt-35.md.
Kind/size: acceptance/S. Baseline: not-started.
Outcome: ArcForges.DesignSystem and ArcForges.Desktop.Shell are packed, admitted, published, and independently consumed; each app is shown to restore only the packages/mechanisms it needs.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-10.90 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\10-design-system-and-desktop-shell.md, anchor rule-wp-10.90

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
- none

Permitted write scope: DesktopPlatform:eng/packaging/packages.json; DesktopPlatform:src/DesignSystem/ArcForges.DesignSystem/ArcForges.DesignSystem.csproj (final IsPackable/package activation only; PLT.26 remains non-packable); DesktopPlatform:src/DesignSystem/ArcForges.Desktop.Shell/ArcForges.Desktop.Shell.csproj (final IsPackable/package activation only; PLT.26 remains non-packable)
Shared resources (follow the owner protocol): RES-desktopplatform-package-inventory (append): Each producer task adds its own package entry; every merge to main packs and publishes all packages at one version; consumers pin the candidate produced by the merge of the capability they need, never waiting for a package closure task; one merge queue.

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): P2-017: offline verify/policy tests plus the retained AOT-publish gate.
Completion evidence for the ledger: Owned artifact and real-integration receipt per WP-10.90.
```

```text
Execute ArcForges delivery task PLT.36 — Principals and the actor chain.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\platform.md (anchor task-plt-36).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/plt-36 (python tools/delivery.py claim PLT.36 --worker <name>); task branch task/plt-36 in DesktopPlatform; ledger record ledger/tasks/plt-36.md.
Kind/size: producer/M. Baseline: not-started.
Outcome: Every operation carries a complete actor chain (human principal, device, installation, session, any acting agent/extension) constructed once at the entry point and flowing through every layer without reconstruction; no operation reaches an enforcement point without it.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-11.00 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\11-security-foundation.md, anchor rule-wp-11.00

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

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\platform.md (anchor task-plt-37).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/plt-37 (python tools/delivery.py claim PLT.37 --worker <name>); task branch task/plt-37 in DesktopPlatform; ledger record ledger/tasks/plt-37.md.
Kind/size: producer/M. Baseline: not-started.
Outcome: R0 to R4 with runtime modifiers; every capability declares a base risk; modifiers raise it based on scope/target/reversibility/egress/actor kind; effective risk is computed, explainable and monotonic (never lowered).

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-11.01 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\11-security-foundation.md, anchor rule-wp-11.01

Entry condition: adoption slice ADOPT.02.platform is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] PLT.19: CapabilityDescriptor carrying risk level/trust requirement/side-effect class (WP-09.02)
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:src/BuildingBlocks/ArcForges.Security/**; DesktopPlatform:eng/policy/architecture-contract-tests.json (append only PLT.37 direct public-API-to-[Fact] mappings from src/BuildingBlocks/ArcForges.Security/RiskModel.cs to src/BuildingBlocks/ArcForges.Security/Tests/RiskModelTests.cs); DesktopPlatform:eng/provenance/files.json (append only firstParty rows, per the adoption rules, for src/BuildingBlocks/ArcForges.Security/RiskModel.cs and src/BuildingBlocks/ArcForges.Security/Tests/RiskModelTests.cs)
Shared resources (follow the owner protocol): RES-architecture-tests (append): Each repository policy task owns its suite; rule additions are append-only.; RES-desktopplatform-policy-data (append): Generated policy data is regenerated from its pinned source and never hand-edited; the reason-code registry is append-only with stable codes; each task adds its own test classes and evidence rows.
Unblocks: PLT.38, PLT.39, PLT.46

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline unit tests exhaustively enumerate descriptor baselines R0–R4 and every runtime-modifier combination; verify effective risk equals the maximum of the baseline and active fixed floors, every active modifier is explained, adding a modifier never lowers risk, descriptor risk parsing is closed to canonical R0–R4, and the three explicit R4 interactions are covered.
Completion evidence for the ledger: Risk classification and monotonicity matrix.
Notes: Fixed minimum floors: remote origin R3; automation origin/Automation actor R2; unverified package R3; large data volume R2; external egress R3; sensitive resource R2; bulk scope R2; irreversible effect R4. Actor-kind floors: None/direct human adds no floor, InternalService R1, Agent R2, Automation R2, Extension R3. Exactly three two-factor interactions additionally require R4: Automation + external egress; sensitive resource + external egress; Extension + unverified package (the privileged-extension case). Effective risk is the maximum of the declared capability baseline and all active floors; every other combination adds no interaction floor. No configurable weights, additive scoring, third-party lowering, or implicit interactions are introduced.
```

```text
Execute ArcForges delivery task PLT.38 — Decision pipeline and the four enforcement points.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\platform.md (anchor task-plt-38).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/plt-38 (python tools/delivery.py claim PLT.38 --worker <name>); task branch task/plt-38 in DesktopPlatform; ledger record ledger/tasks/plt-38.md.
Kind/size: producer/L. Baseline: not-started.
Outcome: The fourteen-step decision pipeline implemented once and invoked at each of the four enforcement points (caller pre-check, transport boundary, service-side decision, owner-side final validation always last); every step produces a typed outcome; a refusal names the failing step and reason code; the pipeline is unbypassable.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-11.02 (all work except the parts mapped to PLT.57): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\11-security-foundation.md, anchor rule-wp-11.02

Entry condition: adoption slice ADOPT.02.platform is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] PLT.36: actor chain
- [artifact] PLT.37: risk model
- [artifact] PLT.10: LocalRpc session handshake (WP-08.01/08.02)
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:src/BuildingBlocks/ArcForges.Security/** (including the new nested non-packable production project src/BuildingBlocks/ArcForges.Security/LocalRpcBoundary/ArcForges.Security.LocalRpcBoundary.csproj with its source and packages.lock.json, and the existing nested Tests project with its lock); DesktopPlatform:src/BuildingBlocks/ArcForges.Capabilities/**; DesktopPlatform:DesktopPlatform.slnx (append only the ArcForges.Security.LocalRpcBoundary project line; the existing Security.Tests registration and CI test line already cover the tests); DesktopPlatform:Directory.Packages.props (append only ArcForges.Security.LocalRpcBoundary to the existing ArcForges.Contracts.Foundation 1.0.0-ci.216.1 MSBuildProjectName selector; preserve the 1.0.0-ci.113.1 default and every other entry); DesktopPlatform:eng/policy/architecture-contract-tests.json (append only exact PLT.38 public API-to-focused-test bindings, in the Security.Tests project); DesktopPlatform:eng/policy/architecture-projects.json (append only the ArcForges.Security.LocalRpcBoundary production project row); DesktopPlatform:eng/policy/licence-boundary.json (append only the ArcForges.Security.LocalRpcBoundary classification); DesktopPlatform:eng/policy/runtime-ownership.json (append only the ArcForges.Security.LocalRpcBoundary project role); DesktopPlatform:eng/provenance/files.json (append only PLT.38 first-party source, project, test, README, lock and immutable receipt paths); DesktopPlatform:eng/policy/reconciliation/active-projects.json (append only the ArcForges.Security.LocalRpcBoundary project path/blob row and refresh only the existing ArcForges.Security and ArcForges.Security.Tests project blobs); DesktopPlatform:eng/policy/dependency-policy.json (add only the exact PLT.38 project and lock input hashes, refresh only the Directory.Packages.props input hash and the changed Security and Security.Tests project and lock input hashes, mirrored in review.inputHashes, and point reviewReceipt to the PLT.38 successor); DesktopPlatform:eng/policy/dependency-reviews/plt-38-r1.json (new immutable PLT.38 receipt successor chained from the receipt active on main at merge, mirroring the active review and closure snapshots)
Shared resources (follow the owner protocol): RES-assistant-store-schema (append): Numbered migrations are allocated at merge by the integration owner (a rebase renumbers pending migrations); each migration is forward-only with its recovery and downgrade-refusal tests; no task edits a merged migration.; RES-desktopplatform-policy-data (append): Generated policy data is regenerated from its pinned source and never hand-edited; the reason-code registry is append-only with stable codes; each task adds its own test classes and evidence rows.; RES-desktopplatform-build-config (append): Solution/project lists, central package versions and CI job lists are appended by the task that adds a project, dependency or job; dependency additions follow the dependency-admission policy with a reviewed receipt; lock files are regenerated after rebase and never hand-merged; the integration owner resolves ordering conflicts at merge.; RES-architecture-tests (append): Each repository policy task owns its suite; rule additions are append-only.
Unblocks: APP.02, APP.03, GOV.16, PLT.20, PLT.41, PLT.43, PLT.46, PLT.57

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline unit tests: step-coverage test asserting every step runs; refusal matrix producing a distinct reason code per failing step; bypass test.
Completion evidence for the ledger: Pipeline bypass, step-coverage and refusal matrix.
Notes: The pipeline's availability-facing permission output is a read-only, immutable owner projection for a specific principal, capability and scope, preserving applicable constraints and lifetime. It is only a UI preflight; it is never a permission grant, resource authorization or substitute for owner-side final validation at invocation. Planning repair for the exact write scope. The outcome requires the transport-boundary step (enforcement point 2) to wrap the real PLT.10 LocalRpc launch verification, but ArcForges.Security is Foundation-only and must not take the ASP.NET Core framework reference and gRPC packages that ArcForges.LocalRpc brings, and ArcForges.LocalRpc is owned by the PLT.09-PLT.16 tasks and is not written here. The binding therefore lives in one new non-packable nested production project, ArcForges.Security.LocalRpcBoundary, inside the existing Security write scope: it references only ArcForges.Security and ArcForges.LocalRpc, implements the Security-owned transport-session port over the public LocalRpcLaunchAuthority, LocalRpcLaunch and LocalRpcLaunchClaim API, and adds no package, version, native code or runtime owner. The existing nested ArcForges.Security.Tests project (already in the solution and in the package-validation workflow) additionally references that project for its offline tests, so no new test project, solution entry beyond the one production line, or workflow change is needed. The only central-package change is appending the new project name to the existing ArcForges.Contracts.Foundation 1.0.0-ci.216.1 selector, exactly as PLT.40 did for its two projects, because central transitive pinning rejects restore (NU1109) of a project that reaches ArcForges.Foundation under the repository-wide 1.0.0-ci.113.1 default. The new immutable dependency receipt re-binds only the changed project, lock and Directory.Packages.props input hashes and chains from the receipt active on main at merge with an unchanged NuGet closure (every coordinate the new closures contain, including the ArcForges.LocalRpc gRPC set, is already recorded by PLT.09 and PLT.39). The Security production project stays Foundation-only: ArcForges.Security itself gains no project or package reference, and PLT.46 still owns Security package admission. The Capabilities write scope is retained but PLT.38 does not need to edit it: the real attachment of this pipeline to the invocation pipeline's authorize step is PLT.57. Not authorized: any other source file, any workflow, .gitleaks.toml or scan allowlist (the receipt-directory group merged with PLT.44 covers the mirrored Security.Secrets receipt lines and must not be widened; add no hash-like literal and no file or project name containing a Gitleaks generic-api-key keyword such as key, secret, token or auth in any hashed inventory row), eng/packaging/packages.json, tests/ArchitectureTests, any other task's rows, and any dependency, package version, closure expansion, package identity, schema or migration. Resource owners and protocols: RES-desktopplatform-build-config (append) for the solution and selector lines, RES-architecture-tests (append) for the exact public API-to-test bindings, and RES-desktopplatform-policy-data (append) for the receipt chain, provenance, reconciliation and inventory rows; regenerate locks and re-append rows after rebase and chain the receipt from the receipt active on main at merge.
```

```text
Execute ArcForges delivery task PLT.39 — Approval, steering and step-up.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\platform.md (anchor task-plt-39).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/plt-39 (python tools/delivery.py claim PLT.39 --worker <name>); task branch task/plt-39 in DesktopPlatform; ledger record ledger/tasks/plt-39.md.
Kind/size: producer/L. Baseline: not-started.
Outcome: Approval requests with bounded lifetime, durable pending state and explicit outcome; steering adjusts a running operation without granting authority; step-up challenges for enumerated sensitive operations; local presence required for the highest risk class, biometric app-unlock never substituting.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-11.03 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\11-security-foundation.md, anchor rule-wp-11.03

Entry condition: adoption slice ADOPT.02.platform is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] PLT.37: risk model
- [artifact] PLT.01: durable persistence for the approval object
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:src/BuildingBlocks/ArcForges.Security/**; DesktopPlatform:eng/policy/architecture-contract-tests.json (append only exact PLT.39 public Security API to focused Security.Tests direct-[Fact] bindings); DesktopPlatform:eng/policy/dependency-policy.json (refresh only the Security.Tests project/lock entries in inputHashes and the identical review.inputHashes; set reviewReceipt to plt-39-r1; update only review.owner, reviewer, reviewedOn, baselineCommit, maintenanceAssessment, values under the unchanged upgradeChecks keys, inputHashes and previousReceipt to mirror the PLT.39 receipt, with previousReceipt = active plt-28-r1; preserve frameworkVersions, namingToolCandidate, closures, unrelated hashes and every other policy field); DesktopPlatform:eng/policy/dependency-reviews/plt-39-r1.json (new immutable successor chained from active plt-28-r1 for the exact test-only project edge; mirror the active review and closure snapshots, preserve all package identities, coordinates, versions and prior receipts); DesktopPlatform:eng/policy/reconciliation/active-projects.json (refresh only the existing Security.Tests project blob for its test-only Persistence.Sqlite reference); DesktopPlatform:eng/provenance/files.json (append only PLT.39 first-party source/test and dependency-receipt rows); DesktopPlatform:eng/native_provenance.py (PLT.39 may pass urllib.request.Request(url, headers={"User-Agent": "ArcForges/1.0 (+https://github.com/ArcForges/DesktopPlatform)"}) only for exact full-string matches of https://visualstudio.microsoft.com/wp-content/uploads/2025/10/Visual_Studio_2026-License-Community_ENU.docx or https://visualstudio.microsoft.com/wp-content/uploads/2025/10/Visual-C-V14-License-Redistributable_and_Runtime_ENU.docx, and only after the existing verified-cache-hit return; preserve every other URL path and all URL, hash, TLS, timeout, redirect, cache, digest, temporary-file and atomic-promotion behavior); DesktopPlatform:tests/tooling/test_native_provenance.py (append only offline tests for the two exact URL/User-Agent cases, a same-host lookalike and unrelated URL remaining unchanged, verified cache-hit bypass, HTTP 403 propagation without cache promotion, and wrong-digest temporary cleanup)
Shared resources (follow the owner protocol): RES-desktopplatform-build-config (append): Solution/project lists, central package versions and CI job lists are appended by the task that adds a project, dependency or job; dependency additions follow the dependency-admission policy with a reviewed receipt; lock files are regenerated after rebase and never hand-merged; the integration owner resolves ordering conflicts at merge.; RES-desktopplatform-policy-data (append): Generated policy data is regenerated from its pinned source and never hand-edited; the reason-code registry is append-only with stable codes; each task adds its own test classes and evidence rows.; RES-architecture-tests (append): Each repository policy task owns its suite; rule additions are append-only.; RES-desktopplatform-native-build (append): The vcpkg baseline and overlay ports change only through a dependency-admission change with licence and provenance receipts; each native family adds its own CMake targets and workflow entries; triplet or port changes are rebased and rebuilt by their author; CPU-heavy native builds use the workstation build slot. PLT.39 may append only a narrowly scoped transport compatibility change to eng/native_provenance.py and offline tests in tests/tooling/test_native_provenance.py: after the verified cache-hit path, pass urllib.request.Request(url, headers={"User-Agent": "ArcForges/1.0 (+https://github.com/ArcForges/DesktopPlatform)"}) only when the complete requested URL equals https://visualstudio.microsoft.com/wp-content/uploads/2025/10/Visual_Studio_2026-License-Community_ENU.docx or https://visualstudio.microsoft.com/wp-content/uploads/2025/10/Visual-C-V14-License-Redistributable_and_Runtime_ENU.docx; preserve all other URL behavior, pinned URLs/hashes, TLS, timeout, redirects, cache, digest verification, temporary cleanup and atomic promotion, with no retries, dependency, workflow or runner changes. The DesktopPlatform integration owner serializes this shared helper append.
Unblocks: APP.05, AST.12, DEV.06, EXE.06, PLT.46

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline tests using the delivered IClock: approval expiry at the exact boundary, idempotent duplicate decisions with immutable action binding, approval-after-cancel refusal, and a test-only real SqliteStore close/reopen of a durable pending approval; steering cannot alter an approved action or grant authority; sensitive-operation step-up refuses biometric app-unlock and requires device-verified local presence at the highest risk. Real OS biometric/local-presence hardware evidence remains local opt-in. Same-store close/reopen proves process-restart persistence only, not cross-device recovery.
Completion evidence for the ledger: Typed approval-state/refusal matrix, exact expiry, SQLite close/reopen, steering, step-up and local-presence results; report OS hardware availability separately.
Notes: Security production remains Foundation-only and owns the typed durable approval-store contract; only the already-existing nested ArcForges.Security.Tests project may reference the already-existing ArcForges.Persistence.Sqlite project to test same-file pending-approval close/reopen through the existing PLT.01 write/receipt path. This test-only reference requires its own regenerated project lock and an immutable dependency-admission successor chained from the currently active plt-28-r1 receipt. Refresh only the Security.Tests project/lock entries in policy.inputHashes and its identical review.inputHashes; point reviewReceipt at plt-39-r1; update only review.owner, reviewer, reviewedOn, baselineCommit, maintenanceAssessment, values under the unchanged upgradeChecks keys, inputHashes and previousReceipt in the active mirrored review, setting previousReceipt to plt-28-r1. Preserve frameworkVersions, namingToolCandidate, all admitted closures/coordinates/versions, unrelated hashes and every other policy field; the new receipt is immutable and prior receipts remain unchanged. It adds no production dependency, package identity, package/version, project, solution/workflow membership, schema or migration. RP-10 bindings map only PLT.39 public APIs to their direct focused Security.Tests facts; provenance adds only PLT.39 first-party files and the new receipt. Bound expiry uses the existing injected IClock, never a caller-supplied timestamp. Steering remains separate and cannot alter the approved action or authority. Local presence comes from a trusted host verifier, not a caller Boolean; remote presence and biometric application-unlock do not satisfy highest-risk step-up. A same-store close/reopen test proves only local process-restart durability and must not be reported as cross-device evidence. No HAR.02 implementation or completion edge is part of PLT.39.
```

```text
Execute ArcForges delivery task PLT.40 — Per-application secrets and session isolation.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\platform.md (anchor task-plt-40).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/plt-40 (python tools/delivery.py claim PLT.40 --worker <name>); task branch task/plt-40 in DesktopPlatform; ledger record ledger/tasks/plt-40.md.
Kind/size: producer/L. Baseline: not-started.
Outcome: Platform secure storage/broker primitives scoped to realm/account/product/installation with no cross-product SSO endpoint; SecretRef Use != Reveal; connector child grants are foreground/definition-bound and cannot export raw secrets; own sign-out leaves other apps/local data intact.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-11.04 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\11-security-foundation.md, anchor rule-wp-11.04
- WP-11:application-credential-boundary-shared-s Application credential boundary: shared security packages use the caller application/installation storage namespace; deny sibling credential reads; no device-SSO signing broker (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\11-security-foundation.md, package-level obligation

Entry condition: adoption slice ADOPT.02.platform is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] PLT.36: actor chain
Completion prerequisites (may start earlier; cannot complete before these are complete):
- [integration] CLOUD.18: real Cloud authentication

Permitted write scope: DesktopPlatform:src/BuildingBlocks/ArcForges.Security.Secrets/**; DesktopPlatform:Directory.Packages.props (append only ArcForges.Security.Secrets and ArcForges.Security.Secrets.Tests to the existing ArcForges.Contracts.Foundation 1.0.0-ci.216.1 MSBuildProjectName selector; preserve the 1.0.0-ci.113.1 default); DesktopPlatform:eng/policy/architecture-contract-tests.json (append only exact PLT.40 public API-to-focused-test bindings); DesktopPlatform:eng/policy/architecture-projects.json (append only the PLT.40 production and test project rows); DesktopPlatform:tests/ArchitectureTests/RepositoryPolicyTests.cs (append only the exact PLT.40 Advapi32 LibraryImport owner/export mapping); DesktopPlatform:eng/policy/licence-boundary.json (append only the PLT.40 production and test project classifications); DesktopPlatform:eng/policy/runtime-ownership.json (append only the PLT.40 production and test project roles); DesktopPlatform:eng/provenance/files.json (append only PLT.40 first-party source, project, test, README, lock and immutable receipt paths); DesktopPlatform:eng/policy/reconciliation/active-projects.json (append only the exact PLT.40 production and test project path/blob rows); DesktopPlatform:eng/policy/dependency-policy.json (add only exact PLT.40 project and lock input hashes, refresh only the Directory.Packages.props input hash and point reviewReceipt to the PLT.40 successor); DesktopPlatform:eng/policy/dependency-reviews/plt-40-r1.json (new immutable PLT.40 receipt successor with the exact mirrored active input map); DesktopPlatform:.gitleaks.toml (add exactly two PLT.40 generic-api-key AND allowlists, each with regexTarget=line and one anchored path: dependency-policy.json has its four observed whole-line alternatives and plt-40-r1.json its two observed whole-line alternatives; do not form path-by-digest cross combinations and preserve every other rule and allowlist); DesktopPlatform:eng/test_dependency_policy.py (append only a focused test of the actual two PLT.40 Gitleaks allowlists and their exact six observed whole-line matches, rejecting swapped key/digest/path pairs, a trailing credential, unrelated 64-hex values, and any other rule)
Shared resources (follow the owner protocol): RES-desktopplatform-build-config (append): Solution/project lists, central package versions and CI job lists are appended by the task that adds a project, dependency or job; dependency additions follow the dependency-admission policy with a reviewed receipt; lock files are regenerated after rebase and never hand-merged; the integration owner resolves ordering conflicts at merge.; RES-desktopplatform-policy-data (append): Generated policy data is regenerated from its pinned source and never hand-edited; the reason-code registry is append-only with stable codes; each task adds its own test classes and evidence rows.; RES-architecture-tests (append): Each repository policy task owns its suite; rule additions are append-only.
Unblocks: CLOUD.18, PLT.46, PLT.49, UPD.01

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline tests where possible; real OS secure-storage round trips (Windows Credential Manager and the Linux keystore; no macOS Keychain adapter exists or is tested, P2-023) are local opt-in per platform, recorded separately from CI. PLT.40 scan-support validation requires the focused actual-config positive/negative test and a passing pinned full-history Gitleaks run; no other rule, workflow, scanner behavior, or finding may be suppressed.
Completion evidence for the ledger: Secret structural prohibitions, platform round-trip results, focused exact PLT.40 Gitleaks allowlist tests, and passing pinned full-history secret-scan evidence.
Notes: Narrow ADP-07 support is limited to the exact eleven additional DesktopPlatform paths listed above, plus the exact RepositoryPolicyTests.cs change authorized below. The scan-support extension authorizes exactly the six observed whole lines, in two separate path-bound groups. The dependency-policy.json group permits exactly four complete lines:     "src/BuildingBlocks/ArcForges.Security.Secrets/ArcForges.Security.Secrets.csproj": "8ff03fdcaf23b09386fac47dd5e3e4f9689a665a569137f726456c9e59a9ecef",     "src/BuildingBlocks/ArcForges.Security.Secrets/Tests/ArcForges.Security.Secrets.Tests.csproj": "d6798bbbcf980fab4467c6d831871b075e55aeef6e09c7df67c4d72cd2334120",       "src/BuildingBlocks/ArcForges.Security.Secrets/ArcForges.Security.Secrets.csproj": "8ff03fdcaf23b09386fac47dd5e3e4f9689a665a569137f726456c9e59a9ecef",       "src/BuildingBlocks/ArcForges.Security.Secrets/Tests/ArcForges.Security.Secrets.Tests.csproj": "d6798bbbcf980fab4467c6d831871b075e55aeef6e09c7df67c4d72cd2334120", The dependency-reviews/plt-40-r1.json group permits exactly the last two complete lines above. Each group has one anchored exact path, targets only generic-api-key, uses condition AND and regexTarget line, and cannot cross-combine paths and digests. A whole-line alternative is anchored exactly as the pinned scanner reports an added line: the scanner prefixes every added line after the first of a diff fragment with one newline, so each alternative accepts at most one optional leading newline and nothing else around the line, with its exact indentation. The focused test must inspect the actual config and the actual policy and receipt files, verify the four plus two matches in both line shapes, and reject swapped key/digest/path combinations, changed digests, appended credentials, unrelated 64-hex values, and other rules. No other finding, path, rule, scanner behavior, workflow, suppression, or dependency is authorized. The existing RES-desktopplatform-build-config append continues to cover only DesktopPlatform.slnx, .github/workflows/package-validation.yml and the Directory.Packages.props selector extension authorized below. RES-desktopplatform-policy-data covers task-owned policy, test-map, reconciliation, dependency-admission and provenance rows under their exact scopes. The existing source write scope contains exactly the new production and test projects, including src/BuildingBlocks/ArcForges.Security.Secrets/packages.lock.json and src/BuildingBlocks/ArcForges.Security.Secrets/Tests/packages.lock.json; regenerate these locks after rebase and preserve the existing dependency closure, coordinates and versions. architecture-contract-tests.json adds only exact public API-to-focused-test bindings; architecture-projects.json, licence-boundary.json and runtime-ownership.json add only the two task-owned project rows/classifications. The PLT.40 production project role is NativeAdapter because it owns the Windows Credential Manager LibraryImport boundary; the test project remains Test. RepositoryPolicyTests.cs may only extend the closed LibraryImport owner/export map with Advapi32.dll owned by the exact directory src/BuildingBlocks/ArcForges.Security.Secrets and exactly CredWriteW, CredReadW, CredDeleteW, and CredFree. Preserve the existing ArcImageNative three-export mapping, DllImport prohibition, LibraryImport syntax checks, duplicate detection, and exact export-set checks. This does not authorize wildcard libraries, paths, owners, or entrypoints, scanner algorithm changes, a Native project, or dependency expansion. active-projects.json adds only those projects' exact paths and git blob IDs. dependency-policy.json may add only the hashes of the two project files and two lock files to inputHashes, refresh only the Directory.Packages.props input hash and set reviewReceipt to the new plt-40-r1 successor. The successor's review.inputHashes must exactly mirror the resulting active dependency-policy inputHashes map; it is immutable and chains from the then-current receipt. No other policy field, dependency coordinate, version, closure, or admission algorithm may change. provenance/files.json appends only first-party paths for the nine task-owned source/project/test/README/lock files and the new immutable receipt. Do not change directories.json, project-updates.json or source.json, package inventory, central package version values, dependency algorithms, or unrelated rows. The only Directory.Packages.props change authorized is to append ArcForges.Security.Secrets and ArcForges.Security.Secrets.Tests to the existing ArcForges.Contracts.Foundation 1.0.0-ci.216.1 MSBuildProjectName selector introduced by PLT.19 and extended by PLT.27. Both new projects reference ArcForges.Security, whose Foundation edge already requires 1.0.0-ci.216.1, so NuGet central transitive pinning otherwise rejects restore with NU1109 against the repository-wide 1.0.0-ci.113.1 default. This changes only those two projects' selection to the already-admitted coordinate; preserve that default and every other selector. Package identity, the available coordinate/version set and the aggregate dependency closure remain unchanged, and the plt-40-r1 successor records the selector as exactly 21 consumers of 1.0.0-ci.216.1: the 19 recorded by PLT.27 plus these two projects. This extension uses RES-desktopplatform-build-config for the selector only. These bindings authorize no new runtime behavior, dependency, package identity or security semantics and do not change PLT.40's outcome, prerequisites or completion condition. Planning repair 2026-10-08 (DLV-34; P2-023): delivered record, not rewritten. The macOS Keychain round trip named in the validation is superseded by P2-023 and is not run or claimed; the Windows Credential Manager round trip and the other named secure-storage round trips remain local opt-in per platform, with Linux in local WSL2 under P2-024. The recorded outcome, validation and evidence are unchanged history and the task stays delivered. Planning repair 2026-10-08 (DLV-34; P2-023 items 1 and 4): the macOS keychain round trip is removed from the validation; the evidence is unchanged.
```

```text
Execute ArcForges delivery task PLT.41 — Egress control.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\platform.md (anchor task-plt-41).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/plt-41 (python tools/delivery.py claim PLT.41 --worker <name>); task branch task/plt-41 in DesktopPlatform; ledger record ledger/tasks/plt-41.md.
Kind/size: producer/M. Baseline: not-started.
Outcome: Every outbound data transfer is its own egress decision, distinct from read access, recording data class/destination/authority; a denied egress produces a typed refusal and every egress is audited.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-11.05 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\11-security-foundation.md, anchor rule-wp-11.05

Entry condition: adoption slice ADOPT.02.platform is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] PLT.38: decision pipeline
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:src/BuildingBlocks/ArcForges.Security/**
Unblocks: APP.06, PLT.44, PLT.46

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline tests: matrix asserting read access alone never authorizes egress; destination allowlist tests; audit assertion.
Completion evidence for the ledger: Egress authorization matrix and audit assertions.
```

```text
Execute ArcForges delivery task PLT.42 — Instruction provenance.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\platform.md (anchor task-plt-42).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/plt-42 (python tools/delivery.py claim PLT.42 --worker <name>); task branch task/plt-42 in DesktopPlatform; ledger record ledger/tasks/plt-42.md.
Kind/size: producer/L. Baseline: not-started.
Outcome: Every input that can carry instructions (model output, extension output, retrieved content, imported documents, deep links, catalog metadata) is marked with its provenance; untrusted provenance can be processed but never gains authority to trigger an operation unapproved.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-11.06 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\11-security-foundation.md, anchor rule-wp-11.06

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

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\platform.md (anchor task-plt-43).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/plt-43 (python tools/delivery.py claim PLT.43 --worker <name>); task branch task/plt-43 in DesktopPlatform; ledger record ledger/tasks/plt-43.md.
Kind/size: producer/M. Baseline: not-started.
Outcome: A delegation creates a lease with scope/expiry/revocation, enforced at use not only at issue; typed trust levels evaluated at defined points; trust never substitutes for permission.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-11.07 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\11-security-foundation.md, anchor rule-wp-11.07

Entry condition: adoption slice ADOPT.02.platform is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] PLT.38: decision pipeline
- [artifact] PLT.01: durable persistence for lease state
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:src/BuildingBlocks/ArcForges.Security/**
Unblocks: DEV.03, PLT.44, PLT.46

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline tests: lease expiry-at-use, revocation-mid-operation, scope-escalation-attempt tests; trust-never-grants-permission test.
Completion evidence for the ledger: Lease expiry, revocation and trust-separation results.
```

```text
Execute ArcForges delivery task PLT.44 — Append-only audit subsystem.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\platform.md (anchor task-plt-44).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/plt-44 (python tools/delivery.py claim PLT.44 --worker <name>); task branch task/plt-44 in DesktopPlatform; ledger record ledger/tasks/plt-44.md.
Kind/size: producer/M. Baseline: not-started.
Outcome: Append-only audit append/query with a dedicated policy-retention maintenance authority; ordinary roles cannot UPDATE/DELETE; audited retention purge removes only expired unheld partitions under declared policy; complete separation from telemetry; every real egress decision and capability-lease lifecycle event is durably audited.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-11.08 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\11-security-foundation.md, anchor rule-wp-11.08

Entry condition: adoption slice ADOPT.02.platform is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] PLT.36: actor chain
- [artifact] PLT.01: persistence write path
- [artifact] FND.04: wall Instant and monotonic timestamp
Completion prerequisites (may start earlier; cannot complete before these are complete):
- [integration] PLT.41: real allowed and denied egress-decision facts are synchronously appended to durable audit records
- [integration] PLT.43: actual capability-lease issue, revocation, expiry and task-end events reach the PLT.44 typed audit intake with their stable identity
- [integration] PLT.57: the real in-process product composition of PLT.57 passes EgressAuditSink and CapabilityLeaseEventAuditSink to the real EgressAuthority and CapabilityLeaseManager over one real AuditStore, and runs the production retention runner against that store under its declared policy

Permitted write scope: DesktopPlatform:src/BuildingBlocks/ArcForges.Security.Audit/ArcForges.Security.Audit.csproj; DesktopPlatform:src/BuildingBlocks/ArcForges.Security.Audit/AuditModels.cs; DesktopPlatform:src/BuildingBlocks/ArcForges.Security.Audit/AuditRetention.cs; DesktopPlatform:src/BuildingBlocks/ArcForges.Security.Audit/AuditStore.cs; DesktopPlatform:src/BuildingBlocks/ArcForges.Security.Audit/AuditRetentionRunner.cs; DesktopPlatform:src/BuildingBlocks/ArcForges.Security.Audit/EgressDecisionAuditAdapter.cs; DesktopPlatform:src/BuildingBlocks/ArcForges.Security.Audit/CapabilityLeaseAuditAdapter.cs; DesktopPlatform:src/BuildingBlocks/ArcForges.Security.Audit/README.md; DesktopPlatform:src/BuildingBlocks/ArcForges.Security.Audit/packages.lock.json; DesktopPlatform:src/BuildingBlocks/ArcForges.Security.Audit/Tests/ArcForges.Security.Audit.Tests.csproj; DesktopPlatform:src/BuildingBlocks/ArcForges.Security.Audit/Tests/AuditStoreTests.cs; DesktopPlatform:src/BuildingBlocks/ArcForges.Security.Audit/Tests/packages.lock.json; DesktopPlatform:DesktopPlatform.slnx; DesktopPlatform:Directory.Packages.props; DesktopPlatform:.github/workflows/package-validation.yml; DesktopPlatform:eng/policy/architecture-contract-tests.json; DesktopPlatform:eng/policy/architecture-projects.json; DesktopPlatform:eng/policy/licence-boundary.json; DesktopPlatform:eng/policy/reconciliation/active-projects.json; DesktopPlatform:eng/policy/runtime-ownership.json; DesktopPlatform:eng/provenance/files.json; DesktopPlatform:eng/policy/dependency-policy.json; DesktopPlatform:eng/policy/dependency-reviews/plt-44-r1.json; DesktopPlatform:.gitleaks.toml (append exactly one generic-api-key AND allowlist with regexTarget=line and the single anchored path pattern for any direct dependency receipt file, ^eng/policy/dependency-reviews/[A-Za-z0-9._-]+[.]json$, carrying only the two whole-line alternatives listed in Notes; no other path, rule or clause, no path-by-digest cross combination, preserve every other rule and allowlist including the PLT.40 groups); DesktopPlatform:eng/test_dependency_policy.py (append only focused tests of the actual receipt-directory Gitleaks allowlist: exactly the two whole lines accepted in any receipt file under eng/policy/dependency-reviews and in the actual receipts, rejected in other paths, swapped key/digest/path pairs, changed digests, trailing text or credentials, unrelated 64-hex values, and any other rule)
Shared resources (follow the owner protocol): RES-desktopplatform-build-config (append): Solution/project lists, central package versions and CI job lists are appended by the task that adds a project, dependency or job; dependency additions follow the dependency-admission policy with a reviewed receipt; lock files are regenerated after rebase and never hand-merged; the integration owner resolves ordering conflicts at merge.; RES-desktopplatform-policy-data (append): Generated policy data is regenerated from its pinned source and never hand-edited; the reason-code registry is append-only with stable codes; each task adds its own test classes and evidence rows.; RES-architecture-tests (append): Each repository policy task owns its suite; rule additions are append-only.
Unblocks: APP.03, PLT.46, PLT.57

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline tests: reject ordinary UPDATE/DELETE and forged retention role; approved expiry purge; legal hold; exact-boundary maintenance-capability expiry using monotonic time despite wall-clock rollback; store-stamped audit occurrence and hold/release times with no caller timestamp; the real PLT.41 EgressAuthority, through the audit-side IEgressAuditSink implementation, appends every allowed decision and every refused decision that reaches the sink to the durable store before returning (including each pre-classification refusal and each unavailable-source refusal; the AuditUnavailable refusal that the authority builds when an allowed decision could not be made durable is not written to the sink by PLT.41 as delivered, so it has no audit event and the failed Authorized write is the only trace), preserving the exact reason, the PLT.41 data-class tier or the explicit Unclassified marker, the destination class or the explicit Undetermined marker, the canonical destination identity (absent only for a malformed destination), the authority kind, reference and grant generation for an allowed decision (none for a refusal), the effective risk only when the producer supplies it (otherwise the explicit NotAssessed marker, never an inferred value), a one-way content reference fingerprint, and the correlation; a record the closed shape cannot represent, a foreign owner, a purged partition and a failing store fail closed so an allowed transfer is refused with AuditUnavailable; a late Authorized write that lands after the authority timed out and refused (the only way an Authorized event can sit beside a refusal) is accepted and tested as a valid event that authorizes nothing; typed capability-lease issue/revocation/expiry/task-end intake preserves the Guid-backed resource identity and unknown lifecycle kinds fail closed; telemetry separation test (also exercised jointly with PLT.49's redaction/separation evidence). Retention runner: a narrow public runner of the Audit project purges only expired, unheld, complete UTC months of its own store under the declared policy with no caller-chosen partition or time, skips a held month, isolates a month that fails verification without touching other months or the partition, mints a fresh single-use capability per month, refuses a maintenance chain of another owner and leaves unexpired months untouched.
Completion evidence for the ledger: Audit immutability, store-owned time/monotonic-expiry, typed egress and lease-event intake, completeness and separation results; report actual PLT.41 egress and PLT.43 lease-emission integration separately.
Notes: Time boundary: inject the delivered FND.04 IClock. The store, not callers, stamps audit occurrence and legal-hold placement/release from its wall Instant; caller-supplied event or hold timestamps are not accepted as authoritative or used to select a partition. The store evaluates retention with its own current Instant and uses the clock's monotonic timestamp/elapsed-time API exclusively for the in-process maintenance-capability TTL, so wall-clock rollback cannot revive an expired capability. The maintenance capability remains in-process, non-serializable and internally minted; no wall-clock timestamp is an authorization token. Egress boundary (Architecture Owner decision, delegated to the completion follow-up and recorded as architecture/08 EG-06 to EG-09): the audit intake is a projection of PLT.41's delivered EgressAuditRecord taken at its IEgressAuditSink, not a second decision and not an audit-owned mirror of the fact. The audit vocabulary adopts PLT.41's data-class tiers (Public, Diagnostic, WorkspaceContent, SensitiveContent, SecretMaterial) plus the explicit Unclassified marker; the earlier storage-class vocabulary was a different axis (where data lives, not how sensitive it is) and is removed from the egress detail. The destination class gains the explicit Undetermined marker and the destination identity is optional only for a malformed destination, so refusals before classification are stored as what they are. The authority is its PLT.41 kind, reference and grant generation (allowed decisions only); the Guid authority object and numeric revision the first design assumed do not exist in PLT.41 and are not fabricated. Effective risk is assessed at pipeline step 9, after the step 8 egress decision, so the egress authority cannot hold it: the event stores R0 to R4 only if a producer supplies one and otherwise the explicit NotAssessed marker (permitted for egress events only). The opaque PLT.41 resource id and revision are not a typed Guid and may be path-like, so the event stores their SHA256 content reference fingerprint instead of a resource Guid; the exact reference stays in the correlated step 14 record by command id. The specific EgressReason is stored exactly alongside the closed audit reason it maps to; the decision reason of an allowed decision derives from its real authority kind. Occurrence time is stamped by the store, not taken from the record. No content, secret value, path or free-form property bag is stored. Both allowed and denied decisions are appended synchronously before the enforcement path returns; an append failure must prevent an allowed transfer from proceeding. Security owns the sink port and must not reference the Audit project; the Audit project implements the port by referencing Security. PLT.41 is unchanged by this decision: carrying the AuditUnavailable refusal into the sink would need a PLT.41 change and is not required, because that refusal means the sink already failed. AU-04 is met jointly: the egress event carries actor chain, executor, software identity, capability, decision, reason, origin, workspace and correlation, while effective risk (when assessed) and the exact resource reference are in the correlated step 14 security audit record of the same command. Schema: the store schema version moves from 1 to 2 and a version 1 file is refused (fail closed) with no migration, because no code outside the Audit project and its tests constructs an audit store, so no version 1 file exists beyond test temporary files. The fingerprint is unsalted and is a reference, not secrecy: a low-entropy or path-like id can be guessed offline by anyone who can read the audit file. Lease boundary: PLT.43 must expose a non-empty immutable Guid-backed CapabilityLeaseId, and each issued/revoked/expired/task-ended lifecycle fact carries that same typed ID. Add only closed audit event/resource values for those four lifecycle kinds and map CapabilityLeaseId.Value directly into the Guid-valued AuditResourceReference; never stringify, hash or truncate the identity. Preserve the ID through append/query, reject unknown kinds, and do not fabricate a PLT.43 runtime or claim actual producer emission from intake-only tests. This task may be delivered with the append/query/retention store and both typed intakes complete, but it cannot be marked complete until real PLT.41 egress and PLT.43 lease lifecycle integrations satisfy both completion prerequisites. The production project sets IsPackable=true without changing package identity; The only permitted Directory.Packages.props edit adds exact conditions for MSBuildProjectName ArcForges.Security.Audit and ArcForges.Security.Audit.Tests selecting the already-admitted ArcForges.Contracts.Foundation 1.0.0-ci.216.1; preserve the default 1.0.0-ci.113.1 and every other project condition. This selects an existing admitted version and changes no package coordinate or aggregate closure. PLT.44 does not choose a PackageId, edit eng/packaging/packages.json, publish packages or claim package acceptance—PLT.46 alone admits the existing ArcForges.Security.Audit package and completes pack/publish/independent-consumer validation. Support writes are limited to the exact solution/test workflow, project/license/runtime/active-project registrations, RP-10 bindings, sorted provenance rows, dependency input map and immutable PLT.44 receipt listed above. Use only the existing Microsoft.Data.Sqlite 10.0.12 and admitted dependency closure. No new dependency, version, closure, external/wire schema change, signature/key algorithm, Security-to-Audit dependency or package identity is authorized. Scan-support extension (narrow ADP-07, same class as the merged PLT.40 allowlist, as the single durable repair): every dependency receipt chained after plt-40-r1 mirrors the existing Security.Secrets project input rows, and the pinned full-history scanner runs with fetch-depth 0 over all fetched branches, so a receipt line added on one open branch is reported by the secret-scan of every other open branch whose config does not cover it. Per-receipt groups would therefore deadlock concurrent branches. One additional .gitleaks.toml group is authorized: path pattern ^eng/policy/dependency-reviews/[A-Za-z0-9._-]+[.]json$ (a file directly in that directory, no subdirectory), targetRules generic-api-key, condition AND, regexTarget line, whose only two alternatives are these exact whole lines, shown with their indentation:      "src/BuildingBlocks/ArcForges.Security.Secrets/ArcForges.Security.Secrets.csproj": "8ff03fdcaf23b09386fac47dd5e3e4f9689a665a569137f726456c9e59a9ecef",      "src/BuildingBlocks/ArcForges.Security.Secrets/Tests/ArcForges.Security.Secrets.Tests.csproj": "d6798bbbcf980fab4467c6d831871b075e55aeef6e09c7df67c4d72cd2334120", each anchored as the scanner reports an added line (at most one optional leading newline and nothing else around the line). No other path, rule, clause, scanner behavior or workflow is authorized, no cross-combination of paths and digests, and every existing rule and allowlist, including the PLT.40 groups, is preserved. The focused eng/test_dependency_policy.py tests verify the actual config against the actual receipts: exactly the two lines are accepted in any receipt file under the directory (existing, PLT.44, PLT.09 and a hypothetical future one) and rejected in other paths, swapped key/digest/path pairs, changed digests, trailing text or credentials, unrelated 64-hex values and other rules. Passing pinned full-history secret-scan evidence on the PLT.44 head is required. Completion repair (2026-10-05, follow-up epoch 3, ledger/tasks/plt-44.md): the production retention runner is a PLT.44 deliverable in the Audit project (new AuditRetentionRunner.cs, listed in the write scope above, built and tested by the epoch 3 follow-up), and the composition of both sinks and the runner in a running product configuration is proved by the PLT.57 integration prerequisite added above, whose write scope and validation were extended for exactly that (PLT.57 notes, same date). PLT.57 starts after PLT.44 is delivered and PLT.44 completes after PLT.57 completes; this is an ordered pair, not a cycle. A real ArcScope process remains with the app-composition and ArcScope tasks and is not a PLT.44 prerequisite.
```

```text
Execute ArcForges delivery task PLT.45 — Content helper and OS-enforced isolation (ContentSandbox host).

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\platform.md (anchor task-plt-45).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/plt-45 (python tools/delivery.py claim PLT.45 --worker <name>); task branch task/plt-45 in DesktopPlatform; ledger record ledger/tasks/plt-45.md.
Kind/size: producer/XL. Baseline: not-started.
Outcome: The first-party C# Native AOT ContentSandbox, generated gRPC broker/control bindings and all restricted RID launch profiles (Windows AppContainer+Job Object, Linux Landlock+seccomp; macOS is outside the delivery scope (P2-023) and a macOS launch is refused fail-closed) are built and solely owned here; ContentSandbox.Contracts/.Broker and the foundation Runtime.<rid> are published before WP13 consumes them; OS containment is proven with a deliberately hostile first-party test parser. Production PDF/image libraries are WP13's job, never an upstream input here.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-11.09 (full; production ContentSandbox helper, real transport): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\11-security-foundation.md, anchor rule-wp-11.09
- WP-11:local-grpc-closure-ss7-own-actual-signed Local gRPC closure (SS7): own actual signed restricted gRPC helper, launch-secret/OS-descriptor allowlist, hostile-fixture containment, private-copy/digest validation, ConnectorBroker security boundary (real connector providers are WP41) (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\11-security-foundation.md, package-level obligation

Entry condition: adoption slice ADOPT.02.platform is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] PLT.15: LocalRpc brokered large-data mechanism (WP-08.06)
- [artifact] PLT.09: LocalRpc transport (WP-08.00)
- [artifact] PLT.10: restricted endpoint identity and one-use launch secret (WP-08.01)
- [contract] CON.04: ArcForges.Contracts.LocalRpc.Sandbox generated ContentSandboxService/session/grant schema
Completion prerequisites (may start earlier; cannot complete before these are complete):
- [integration] NAT.31: still-image parser composition into the ContentSandbox helper (NAT.31) as the production composition that completes this gate

Permitted write scope: DesktopPlatform:src/DesktopHelpers/ArcForges.ContentSandbox.Broker/** (the new non-packable production project ArcForges.ContentSandbox.Broker with its sources, README and packages.lock.json); DesktopPlatform:src/DesktopHelpers/ArcForges.ContentSandbox.Contracts/** (the new non-packable production project ArcForges.ContentSandbox.Contracts, the facade over the generated Sandbox bindings, with its sources, README and packages.lock.json); DesktopPlatform:src/DesktopHelpers/ArcForges.ContentSandbox/** (the existing helper project, its sources, README and lock; the nested non-packable offline and opt-in test project ArcForges.ContentSandbox/Tests/ArcForges.ContentSandbox.Tests.csproj with its lock; the nested non-packable test-only hostile-parser fixture executable ArcForges.ContentSandbox/Fixture/ArcForges.ContentSandbox.HostileFixture.csproj with its lock; and the declarative macOS entitlement input); DesktopPlatform:DesktopPlatform.slnx (append only the four new project lines: Contracts, Broker, Tests and HostileFixture); DesktopPlatform:Directory.Packages.props (append only one exact PackageVersion for ArcForges.Contracts.LocalRpc.Sandbox 1.0.0-ci.216.1, the candidate of the same Contracts source commit as the already admitted ArcForges.Contracts.LocalRpc.Platform 1.0.0-ci.216.1, and exact MSBuildProjectName conditions selecting the already admitted ArcForges.Contracts.Foundation 1.0.0-ci.216.1 for the four new projects; preserve the 1.0.0-ci.113.1 default and every other entry); DesktopPlatform:eng/policy/dependency-policy.json (add the one new nugetClosure entry for arcforges.contracts.localrpc.sandbox/1.0.0-ci.216.1 with its flat-container nuspec URL, raw nuspec SHA-256, Apache-2.0 licence, content hash and Contracts internal-publisher record; add only the exact PLT.45 project and lock input hashes, refresh only the Directory.Packages.props, existing helper project and lock input hashes, mirrored in review.inputHashes; point reviewReceipt to the PLT.45 successor); DesktopPlatform:eng/policy/dependency-reviews/plt-45-r1.json (new immutable PLT.45 receipt successor chained from the receipt active on main at merge, mirroring the active review and closure snapshots); DesktopPlatform:eng/policy/architecture-projects.json (append only the four new project rows; the existing helper row keeps its classification); DesktopPlatform:eng/policy/architecture-contract-tests.json (append only exact PLT.45 public API-to-focused-test bindings, in the ContentSandbox Tests project); DesktopPlatform:eng/policy/licence-boundary.json (append only the four new project classifications); DesktopPlatform:eng/policy/runtime-ownership.json (append only the four new project roles); DesktopPlatform:eng/policy/reconciliation/active-projects.json (append only the four new project path/blob rows and refresh only the existing helper project blob); DesktopPlatform:eng/provenance/files.json (append only PLT.45 first-party source, project, test, README, lock, entitlement and immutable receipt paths); DesktopPlatform:eng/runtime_ownership.py (classify only the exact two Contracts and Broker project paths under src/DesktopHelpers as aot-library and the test-only hostile fixture directory under the ContentSandbox helper as test-or-build-tool; every other project under src/DesktopHelpers keeps the single-host rule); DesktopPlatform:eng/test_runtime_ownership.py (positive assertions for the exact host, two libraries and fixture, and rejection fixtures for lookalike, wrong-owner and nested paths); DesktopPlatform:tests/ArchitectureTests/RepositoryPolicyTests.cs (extend only the closed native-binding owner map of ProductionNativeBindingsHaveOneCapabilityOwner: allow the two exact owner directories src/DesktopHelpers/ArcForges.ContentSandbox.Broker/Native and src/DesktopHelpers/ArcForges.ContentSandbox/Native, and replace the owner map plus the Cred-specific marshalling-flag assertions by one closed per-export table (library:entry point, owner directory, UTF-16 strings, last-error capture) that lists every existing owner and export unchanged and appends the exact exports of the two new directories; the matching expression, the one-owner-per-export check and the declaration count check are unchanged); DesktopPlatform:.github/workflows/package-validation.yml (append only the ContentSandbox offline test line in the existing test step and one compile-only Native AOT job for the helper project on win-x64 and linux-x64, modelled on the existing local-rpc-aot job; no execution of the helper, no new trigger and no macOS runner)
Shared resources (follow the owner protocol): RES-desktopplatform-policy-data (append): Generated policy data is regenerated from its pinned source and never hand-edited; the reason-code registry is append-only with stable codes; each task adds its own test classes and evidence rows.; RES-desktopplatform-build-config (append): Solution/project lists, central package versions and CI job lists are appended by the task that adds a project, dependency or job; dependency additions follow the dependency-admission policy with a reviewed receipt; lock files are regenerated after rebase and never hand-merged; the integration owner resolves ordering conflicts at merge.; RES-architecture-tests (append): Each repository policy task owns its suite; rule additions are append-only.
Permitted substitutes (never real integration evidence): SUB-hostile-test-parser: OS-level containment mechanics only (AppContainer/Job Object, Landlock/seccomp, resource bounds, crash/hang/parent-death cleanup) against a deliberately hostile FIRST-PARTY test parser, not real format-parsing correctness; macOS App-Sandbox/XPC denial is out of scope (P2-023) Real producer ['NAT.31']; removed by PLT.54
Unblocks: EXT.00, GOV.32, NAT.11, NAT.14, NAT.15, NAT.25, NAT.31, NAT.32, PLT.15, PLT.46, PLT.54

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): P2-017 CRITICAL NUANCE: static/offline unit and policy tests run in CI, but the actual required evidence - real OS containment (AppContainer/Job Object denial, Landlock/seccomp denial, native crash/hang/memory-exhaustion/parent-death cleanup) - is device/OS-level execution that P2-017 explicitly excludes from hosted CI ('no macOS CI; no CI for... desktop GUI... sandbox execution'). This evidence MUST be recorded as local opt-in runs on each supported RID, per the ci-and-local-validation-policy.md and the architecture 24 rule 'a mocked launcher or same-user unrestricted child satisfies this gate: never'.
Completion evidence for the ledger: Real child attempts at product-DB/token reads, outbound TCP/UDP/loopback, sibling-process access, spawn escape, oversized output; OS denial, resource bounds and parent-death cleanup on every supported RID.
Notes: This is the single highest-stakes early risk proof in the desktop platform foundation: PG-22 explicitly states a mocked launcher or unrestricted same-user child cannot close the gate, and the failure mode (hostile parsing escaping containment) would invalidate downstream trust in every product that later touches untrusted content (assistant image/PDF previews, extensions). Recommend prioritising this alongside PLT.03 (persistence recovery). Merged duplicate integration or closure task formerly proposed as CON.96. Planning repair for the exact write scope (DLV-34, scope moves only; outcome, prerequisites and evidence are unchanged). The outcome needs three new managed projects, an offline and opt-in test project and a test-only hostile-parser fixture executable, none of which exists, plus the supporting registrations they require. Project layout: ArcForges.ContentSandbox.Contracts is the thin facade over the generated ArcForges.Contracts.LocalRpc.Sandbox bindings (no duplicate authored or generated wire types) that maps the generated slot grant, seal and acknowledgement records onto the LocalRpc brokered-data records and fixes the launch frame shared by parent and helper; ArcForges.ContentSandbox.Broker is the parent side (restricted launch profiles, resource inventory, registration, session, brokered buffers, supervision); ArcForges.ContentSandbox is the Native AOT helper host. Dependency admission: the only new coordinate is ArcForges.Contracts.LocalRpc.Sandbox 1.0.0-ci.216.1, the published candidate of the same Contracts source commit as the already admitted ArcForges.Contracts.LocalRpc.Platform 1.0.0-ci.216.1 (CON.04 merged and published it); its nuspec dependencies (ArcForges.Contracts.Foundation 1.0.0-ci.216.1, Google.Protobuf 3.36.1, Grpc.Core.Api 2.84.0) are already admitted, so the closure gains this one coordinate and nothing else, and ArcForges.Contracts.LocalRpc.Platform stays the bootstrap contract. PLT.15 and ArcForges.LocalRpc could not prove the real cancel-through-contract and slot-record mapping for lack of this package, so admitting it is part of this task's outcome. No other package, version, native library, vcpkg port or signing identity is added. Native bindings: the process launch profiles need operating-system calls that the managed libraries do not expose (Windows AppContainer, Job Object and handle-list process creation; Linux descriptor-restricted process creation, Landlock, seccomp, no_new_privs and resource limits). They are LibraryImport declarations in exactly two directories (the Broker Native directory for the parent launch and the helper Native directory for self-enforcement and mapping), each export unique, none exposed publicly, and the closed native-binding owner test is extended only to list those exact owners and exports. Runtime ownership: eng/runtime_ownership.py treats every project under src/DesktopHelpers as the one runtime host, so the two new libraries and the fixture need exact-path classification there (found by hosted CI runtime-policy) and the matching unit test. Out of scope here: eng/packaging/packages.json and every package identity (PLT.46 admits the packages), .gitleaks.toml and scan allowlists (add no hash-like literal and no file or project name containing a Gitleaks generic-api-key keyword such as key, secret, token or auth in any hashed inventory row), production PDF and image parsers (NAT.14), the macOS XPC activation shim and signing (it needs a signed sandboxed bundle this repository cannot build or run here; the macOS profile is a typed fail-closed refusal until it exists), and any other task's rows. Resource owners and protocols: RES-desktopplatform-build-config (append) for the solution, selector and workflow lines, RES-architecture-tests (append) for the exact public API-to-test bindings and the native-binding owner map, and RES-desktopplatform-policy-data (append) for the receipt chain, provenance, reconciliation and inventory rows; regenerate locks and re-append rows after rebase and chain the receipt from the receipt active on main at merge. Planning repair 2026-10-08 (DLV-34; P2-022): the completion edge moves from NAT.15 (superseded) to NAT.31 (still-image parser composition into this helper). The gate quoted in the completion edge's why text is amended by P2-022 for the still-image family: NAT.31 is a reverse dependency of this stage, which that gate did not allow, so the edge is a P2-022 change and not a reopening of the delivered outcome. PDF parsing is retired by NAT.32, so no PDF parser composition completes this task. The delivered outcome, writes, validation and evidence are history and are not changed by this note. Planning repair 2026-10-08 (DLV-34; P2-023): macOS is outside the delivery scope. The macOS App-Sandbox and XPC deliverables named in this delivered task (the App-Sandbox+XPC launch profile, the App-Sandbox/XPC denial evidence and the declarative macOS entitlement input) are removed from active scope; no macOS artifact, signing or validation is claimed. The Linux and Windows containment mechanics and the shared cross-platform code (Unix socket paths) are unchanged. The delivered outcome, writes, validation and evidence are history and are not changed by this note. Planning repair 2026-10-08 (DLV-34; P2-023 item 4): the macOS App-Sandbox+XPC profile is removed from the outcome and validation; the supported RIDs for the completion evidence are Windows and Linux, with Linux observed in local WSL2 under P2-024. The delivered writes are history; the declarative macOS entitlement input is removed by GOV.32.
```

```text
Execute ArcForges delivery task PLT.46 — Publish Security packages and verify real integration.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\platform.md (anchor task-plt-46).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/plt-46 (python tools/delivery.py claim PLT.46 --worker <name>); task branch task/plt-46 in DesktopPlatform; ledger record ledger/tasks/plt-46.md.
Kind/size: acceptance/M. Baseline: not-started.
Outcome: ArcForges.Security, .Security.Secrets, .Security.Audit and .Security.CapabilityEnforcement are packed, admitted, published and independently consumed; the signed parent-bound helper and OS broker are packaged with only this stage's dependencies and the test-only parser fixture, no dependency back on WP13.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-11.90 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\11-security-foundation.md, anchor rule-wp-11.90

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

Permitted write scope: DesktopPlatform:eng/packaging/packages.json (package rows for the four packable projects only); DesktopPlatform:src/BuildingBlocks/ArcForges.Security/ArcForges.Security.csproj (IsPackable true only); DesktopPlatform:src/BuildingBlocks/ArcForges.Security.Audit/ArcForges.Security.Audit.csproj (IsPackable true only); DesktopPlatform:src/BuildingBlocks/ArcForges.Security.Secrets/ArcForges.Security.Secrets.csproj (IsPackable false changed to true only); DesktopPlatform:src/BuildingBlocks/ArcForges.Security/CapabilityEnforcement/ArcForges.Security.CapabilityEnforcement.csproj (IsPackable false changed to true only; the nested project is created by PLT.57, which PLT.46 starts on); DesktopPlatform:eng/policy/architecture-projects.json (ADP-07 supporting rows for the four packable projects only); DesktopPlatform:eng/policy/reconciliation/active-projects.json (refresh the four csproj blob rows only); DesktopPlatform:eng/provenance/files.json (refresh the four csproj rows only); DesktopPlatform:eng/policy/dependency-reviews/** (new immutable PLT.46 receipt successor chained from the receipt active on main at merge)
Shared resources (follow the owner protocol): RES-desktopplatform-package-inventory (append): Each producer task adds its own package entry; every merge to main packs and publishes all packages at one version; consumers pin the candidate produced by the merge of the capability they need, never waiting for a package closure task; one merge queue.; RES-desktopplatform-policy-data (append): Generated policy data is regenerated from its pinned source and never hand-edited; the reason-code registry is append-only with stable codes; each task adds its own test classes and evidence rows.
Unblocks: APP.03

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): P2-017: offline verify/policy tests in CI; the real OS-isolation matrix (PLT.45's evidence) is local opt-in, recorded and cross-referenced here rather than re-run.
Completion evidence for the ledger: Cross-boundary owner refusal, stale approval/revocation, secrets/redaction and real OS-isolation tests per WP-11.90.
Notes: Planning repair 2026-10-08 (DLV-34; P2-021 packaging decisions 1 and 4; coordinator adjudication 13): the write scope gains the IsPackable repair for four projects: ArcForges.Security, ArcForges.Security.Audit, ArcForges.Security.Secrets and ArcForges.Security.CapabilityEnforcement. ArcForges.Security.CapabilityEnforcement is the project APP.03 consumes as a published package for PLT.57's product-host acceptance, so APP.03's start on PLT.46 depends on it. IsPackable defaults to false through Directory.Build.props, ArcForges.Security.Secrets sets it false explicitly and CapabilityEnforcement is false today. The write scope adds the ADP-07 supporting rows, the reconciliation and provenance rows for those four csproj files and a new PLT.46 receipt; RES-desktopplatform-policy-data is declared because it holds the architecture-projects and active-projects rows written here. The outcome now names the four packed packages (the delivered-wording rule does not apply: PLT.46 has no ledger record). Validation and evidence are unchanged, including the test-only parser fixture wording. No macOS deliverable is named.
```

```text
Execute ArcForges delivery task PLT.47 — Emission and required dimensions.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\platform.md (anchor task-plt-47).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/plt-47 (python tools/delivery.py claim PLT.47 --worker <name>); task branch task/plt-47 in DesktopPlatform; ledger record ledger/tasks/plt-47.md.
Kind/size: producer/M. Baseline: not-started.
Outcome: A single emission surface for metrics/traces/structured logs with the required dimension set attached automatically from ambient context; a present dimension is always attached, an absent one omitted rather than defaulted; build identifier and instance identity are on every signal.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-12.00 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\12-observability-foundation.md, anchor rule-wp-12.00

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

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\platform.md (anchor task-plt-48).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/plt-48 (python tools/delivery.py claim PLT.48 --worker <name>); task branch task/plt-48 in DesktopPlatform; ledger record ledger/tasks/plt-48.md.
Kind/size: producer/M. Baseline: not-started.
Outcome: Correlation created at the originating edge or accepted from a validated client value, propagated across HTTP/queue/worker/realtime/provider calls once, in shared infrastructure; causation records which operation caused which; a user-visible task/run identifier resolves to its trace.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-12.01 (the shared telemetry infrastructure and the originating edge: validated typed correlation created or accepted at the origin, propagation across the local hop kinds, causation, task/run resolution (the Cloud ingress, host, ResponseMeta/ArcError and queue-wake share is mapped to CLOUD.69)): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\12-observability-foundation.md, anchor rule-wp-12.01

Entry condition: adoption slice ADOPT.02.platform is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] PLT.47: emission surface
Completion prerequisites (may start earlier; cannot complete before these are complete):
- [integration] CLOUD.01: a real Cloud hop to prove the full HTTP/queue/worker/realtime/provider chain
- [integration] CLOUD.69: the Cloud-side correlation acceptance and propagation across ingress, host, ResponseMeta/ArcError and queue wake, observable in the isolated proof environment

Permitted write scope: DesktopPlatform:src/BuildingBlocks/ArcForges.Observability/**; DesktopPlatform:eng/policy/architecture-contract-tests.json (append only exact PLT.48 public API-to-test bindings for the existing Observability test project); DesktopPlatform:eng/provenance/files.json (append only first-party paths for new PLT.48 source and test files)
Shared resources (follow the owner protocol): RES-desktopplatform-policy-data (append): Generated policy data is regenerated from its pinned source and never hand-edited; the reason-code registry is append-only with stable codes; each task adds its own test classes and evidence rows.; RES-architecture-tests (append): Each repository policy task owns its suite; rule additions are append-only.
Unblocks: PLT.53

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline tests: synthetic end-to-end action producing one connected trace across available local hop kinds; resolution test from task identifier to trace; validation test rejecting malformed client-supplied correlation.
Completion evidence for the ledger: A single connected trace across every available hop kind.
Notes: Planning repair 2026-10-05 (DLV-34, DLV-41; scope moves only; no obligation or acceptance removed). The completion edge CLOUD.01 alone could never be satisfied by an observation: CLOUD.01 delivered the ingress without any correlation handling, and no Cloud task owned it. CLOUD.69 now owns the Cloud share (HTTP, Worker, host, ResponseMeta/ArcError, queue wake). The completion follow-up, after CLOUD.01 and CLOUD.69 are complete, performs the task's own remaining acceptance as one local opt-in run (P2-017, the PLT.53 precedent): a throwaway consumer outside the repository restores only the published ArcForges.Observability and generated PublicApi packages, creates the typed origin with CorrelationPropagation.BeginOrigin, sends it in RequestMeta.correlationId to the isolated proof environment under the RES-cloud-deployment lease, and records that the identifier returns in ResponseMeta/ArcError and the wake path and that the task identifier resolves to the connected local trace. The evidence says 'every available hop kind': the realtime hop and the outbound provider hop have no Cloud producer yet, are not claimed, and are recorded as pending later owners with their closing gates (WP-12.90 staged integration): CLOUD.33 (event publication, Event.correlationId) and AIR.04 (provider request identifier, CR-05) start from the CLOUD.69 seam and keep that propagation in their own acceptance. PLT.48 write scope is unchanged.
```

```text
Execute ArcForges delivery task PLT.49 — Redaction by construction.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\platform.md (anchor task-plt-49).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/plt-49 (python tools/delivery.py claim PLT.49 --worker <name>); task branch task/plt-49 in DesktopPlatform; ledger record ledger/tasks/plt-49.md.
Kind/size: producer/L. Baseline: not-started.
Outcome: Secret-bearing and content types have no logging representation; a scrubbing processor removes known-sensitive header/field names as a second line of defence; URLs recorded as route templates plus identifiers; exception messages mapped to reason codes before export.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-12.02 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\12-observability-foundation.md, anchor rule-wp-12.02
- WP-12:eng-policy-telemetry-policy-json-creatio eng/policy/telemetry-policy.json creation: dimension allowlist, metric label allowlist, sampling and retention configuration (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\12-observability-foundation.md, package-level obligation

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

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\platform.md (anchor task-plt-50).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/plt-50 (python tools/delivery.py claim PLT.50 --worker <name>); task branch task/plt-50 in DesktopPlatform; ledger record ledger/tasks/plt-50.md.
Kind/size: producer/M. Baseline: not-started.
Outcome: Metric labels and bounded trace policy enforced from observability architecture SS13: head sample plus bounded diagnostic buffer, error/slow promotion only for spans still retained, explicit overflow/loss counters; unsampled mandatory error facts remain redacted under consent.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-12.03 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\12-observability-foundation.md, anchor rule-wp-12.03
- WP-12:eng-policy-telemetry-policy-json-creatio eng/policy/telemetry-policy.json creation: dimension allowlist, metric label allowlist, sampling and retention configuration (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\12-observability-foundation.md, package-level obligation

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

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\platform.md (anchor task-plt-51).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/plt-51 (python tools/delivery.py claim PLT.51 --worker <name>); task branch task/plt-51 in DesktopPlatform; ledger record ledger/tasks/plt-51.md.
Kind/size: producer/S. Baseline: not-started.
Outcome: Liveness, readiness and capability health as three distinct probe kinds; readiness fails closed on a missing required dependency; capability health uses the five health dimensions (reachable, ready, healthy, degraded, capacity) shared with the contract model.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-12.04 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\12-observability-foundation.md, anchor rule-wp-12.04

Entry condition: adoption slice ADOPT.02.platform is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] PLT.23: HealthDimension type (WP-09.06)
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:src/BuildingBlocks/ArcForges.Observability/**; DesktopPlatform:eng/policy/architecture-contract-tests.json (append only the exact PLT.51 public HealthProbe API-to-direct-test bindings listed below); DesktopPlatform:eng/policy/dependency-policy.json (refresh only task-owned Observability input hashes and active receipt pointer); DesktopPlatform:eng/policy/dependency-reviews/plt-51-r1.json (one immutable PLT.51 dependency receipt successor); DesktopPlatform:eng/policy/reconciliation/active-projects.json (refresh only the existing Observability project blob); DesktopPlatform:eng/provenance/files.json (append only HealthProbe.cs and the PLT.51 immutable receipt as firstParty)
Shared resources (follow the owner protocol): RES-desktopplatform-build-config (append): Solution/project lists, central package versions and CI job lists are appended by the task that adds a project, dependency or job; dependency additions follow the dependency-admission policy with a reviewed receipt; lock files are regenerated after rebase and never hand-merged; the integration owner resolves ordering conflicts at merge.; RES-architecture-tests (append): Each repository policy task owns its suite; rule additions are append-only.; RES-desktopplatform-policy-data (append): Generated policy data is regenerated from its pinned source and never hand-edited; the reason-code registry is append-only with stable codes; each task adds its own test classes and evidence rows.
Unblocks: PLT.53

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline tests: dependency-outage test asserting readiness fails closed; capability-health test reflecting simulated degradation.
Completion evidence for the ledger: Health probe fail-closed and degradation results.
Notes: Consume PLT.23's HealthDimension only as the same closed capability-probe aspect-key type defined by WP-09: reachable, ready, healthy, degraded and capacity. It carries no observation value or snapshot fields and is distinct from Architecture 02 §11's five independent axes (Installation, Presence, Health, Readiness, Compatibility). This clarification changes no Contracts/wire or Foundation HealthSnapshot/InstanceHealth/InstanceReadiness semantics and defines no Cloud presence/heartbeat behavior. The three probe kinds must be exposed through a package-consumable public HealthProbe surface; an internal/IVT-only implementation is insufficient because there is no existing public facade or consumer call chain. ADP-07 support is limited to the five exact existing-gate paths listed above: append only the three HealthProbe public API-to-direct-[Fact] bindings to architecture-contract-tests.json; refresh only hashes for task-owned Observability project/lock inputs that actually change and the active dependency receipt pointer; add immutable plt-51-r1.json as a successor to the then-current receipt, preserving dependency coordinates, versions and aggregate closure; update only the existing Observability project row's exact csproj blob in active-projects.json; and append only HealthProbe.cs and the new receipt as firstParty provenance. The exact RP-10 rows are: ArcForges.Observability.HealthProbe.CheckLiveness() -> ArcForges.Observability.Tests.SignalEmitterTests.LivenessProbeDoesNotClaimReadinessOrCapabilityHealth(); ArcForges.Observability.HealthProbe.CheckReadiness(System.Collections.Generic.IEnumerable<string>, System.Collections.Generic.IEnumerable<ArcForges.Observability.RequiredDependencyObservation>) -> ArcForges.Observability.Tests.SignalEmitterTests.ReadinessFailsClosedForEveryMissingRequiredDependency(); ArcForges.Observability.HealthProbe.EvaluateCapabilityHealth(System.Collections.Generic.IEnumerable<ArcForges.Observability.HealthDimensionObservation>) -> ArcForges.Observability.Tests.SignalEmitterTests.CapabilityHealthUsesAllFiveSharedDimensionsAndReflectsSimulatedDegradation(). The same-repository project reference to PLT.23's Capabilities type adds no external package, package identity, version, runtime package closure or package-inventory entry. Use RES-desktopplatform-build-config for the task-owned Observability project configuration and its locks, regenerated after rebase; use RES-architecture-tests for the append-only RP-10 rows and RES-desktopplatform-policy-data for the exact dependency receipt, policy hash/pointer, reconciliation blob and provenance append. Do not change packages.json, central package versions, solution/workflow, project classification, licence boundary, policy algorithms, any other architecture/API-test mapping, unrelated records or any other task's scope. Outcome, prerequisites and runtime behavior remain unchanged.
```

```text
Execute ArcForges delivery task PLT.52 — Desktop diagnostics and consent.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\platform.md (anchor task-plt-52).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/plt-52 (python tools/delivery.py claim PLT.52 --worker <name>); task branch task/plt-52 in DesktopPlatform; ledger record ledger/tasks/plt-52.md.
Kind/size: producer/L. Baseline: not-started.
Outcome: Local diagnostics always available without upload; three tiers (minimal always-on local, user-approved report, time-bounded self-disabling verbose session visible while active); a report is generated, shown in full, sent only after approval; no memory dump by default; consent is revocable and stops collection immediately and locally.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-12.05 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\12-observability-foundation.md, anchor rule-wp-12.05

Entry condition: adoption slice ADOPT.02.platform is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] PLT.31: error presentation shell surface (WP-10.05)
- [artifact] PLT.49: redaction
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:src/BuildingBlocks/ArcForges.Observability.Desktop/**; DesktopPlatform:DesktopPlatform.slnx (append the two new project entries); DesktopPlatform:.github/workflows/package-validation.yml (append one dotnet test step for the new test project beside the existing Observability step; no other job, step or workflow); DesktopPlatform:Directory.Packages.props (append exactly two MSBuildProjectName conditions for ArcForges.Observability.Desktop and ArcForges.Observability.Desktop.Tests selecting the already-admitted ArcForges.Contracts.Foundation 1.0.0-ci.216.1; preserve the default 1.0.0-ci.113.1 and every other condition); DesktopPlatform:eng/policy/architecture-contract-tests.json (append only the twenty exact PLT.52 public API-to-direct-[Fact] bindings listed in Notes); DesktopPlatform:eng/policy/architecture-projects.json (append only the two PLT.52 production and test project rows); DesktopPlatform:eng/policy/licence-boundary.json (append only the two PLT.52 project classifications); DesktopPlatform:eng/policy/runtime-ownership.json (add only the two PLT.52 project roles); DesktopPlatform:eng/policy/reconciliation/active-projects.json (append only the two exact PLT.52 path/blob rows); DesktopPlatform:eng/provenance/files.json (add only PLT.52 first-party source, project, test, README, lock and immutable receipt paths); DesktopPlatform:eng/policy/dependency-policy.json (add only the exact PLT.52 project and lock input hashes, refresh only the Directory.Packages.props input hash and point reviewReceipt to the PLT.52 successor); DesktopPlatform:eng/policy/dependency-reviews/plt-52-r1.json (new immutable PLT.52 receipt successor chained from the then-active receipt with the exact mirrored active input map)
Shared resources (follow the owner protocol): RES-desktopplatform-build-config (append): Solution/project lists, central package versions and CI job lists are appended by the task that adds a project, dependency or job; dependency additions follow the dependency-admission policy with a reviewed receipt; lock files are regenerated after rebase and never hand-merged; the integration owner resolves ordering conflicts at merge.; RES-desktopplatform-policy-data (append): Generated policy data is regenerated from its pinned source and never hand-edited; the reason-code registry is append-only with stable codes; each task adds its own test classes and evidence rows.; RES-architecture-tests (append): Each repository policy task owns its suite; rule additions are append-only.
Unblocks: PLT.53

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline tests: consent-absent test asserting no signal leaves the device; crash test asserting no automatic upload; verbose-session expiry test; revocation test. All runnable as local simulated-consent-state tests, no live telemetry backend needed.
Completion evidence for the ledger: Consent-absent, crash-approval, verbose-expiry and revocation results.
Notes: ADP-07 binding for a project that does not yet exist; it grants no new runtime behavior, dependency owner, package coordinate or version, package identity, security suppression or policy algorithm. The source scope is exactly the new production and test projects under src/BuildingBlocks/ArcForges.Observability.Desktop/**, including both packages.lock.json files, regenerated after rebase and never hand-merged. Support writes are limited to the exact paths listed above, under RES-desktopplatform-build-config (solution, workflow, central-version selector), RES-architecture-tests (append-only RP-10 rows) and RES-desktopplatform-policy-data (classification, ownership, reconciliation, provenance and dependency-admission rows). The production project references only ArcForges.Observability and ArcForges.Foundation and no package. The central-version selector is needed because the Foundation edge of ArcForges.Observability requires ArcForges.Contracts.Foundation 1.0.0-ci.216.1 and central transitive pinning otherwise rejects restore against the 1.0.0-ci.113.1 default; the plt-52-r1 successor records the selector with exactly two more consumers than the then-active receipt and an unchanged NuGet closure. Classification: the production project is role Foundation (AOT-compatible, no product-internal dependency, no UI reference) and the test project role Test; both are AGPL msbuild projects. The exact RP-10 rows are: ArcForges.Observability.Desktop.ConsentGatedTelemetry.Export(System.Diagnostics.Activity) -> ArcForges.Observability.Desktop.Tests.ConsentTests.GrantedConsentSendsEventsAndSpansAndRevocationStopsThemAtOnce(); ArcForges.Observability.Desktop.ConsentGatedTelemetry.Write(ArcForges.Observability.StructuredSignal) -> ArcForges.Observability.Desktop.Tests.ConsentTests.GrantedConsentSendsEventsAndSpansAndRevocationStopsThemAtOnce(); ArcForges.Observability.Desktop.IClientTelemetryTransport.Send(ArcForges.Observability.ScrubbedSpan) -> ArcForges.Observability.Desktop.Tests.ConsentTests.GrantedConsentSendsEventsAndSpansAndRevocationStopsThemAtOnce(); ArcForges.Observability.Desktop.IClientTelemetryTransport.Send(ArcForges.Observability.StructuredSignal) -> ArcForges.Observability.Desktop.Tests.ConsentTests.GrantedConsentSendsEventsAndSpansAndRevocationStopsThemAtOnce(); ArcForges.Observability.Desktop.TelemetryConsent.Grant() -> ArcForges.Observability.Desktop.Tests.ConsentTests.GrantedConsentSendsEventsAndSpansAndRevocationStopsThemAtOnce(); ArcForges.Observability.Desktop.TelemetryConsent.Revoke() -> ArcForges.Observability.Desktop.Tests.ConsentTests.RevocationWaitsForASendInProgressAndNoSendStartsAfterItReturns(); ArcForges.Observability.Desktop.DesktopDiagnostics.CreateTelemetry(ArcForges.Observability.Desktop.IClientTelemetryTransport) -> ArcForges.Observability.Desktop.Tests.ConsentTests.ConsentAbsentSendsNoSignalOffTheDeviceYetLocalDiagnosticsStillRecord(); ArcForges.Observability.Desktop.DesktopDiagnostics.Open(ArcForges.Observability.Desktop.DesktopDiagnosticsOptions) -> ArcForges.Observability.Desktop.Tests.LocalStoreTests.TheLocalViewIsBoundedAndOrderedOldestFirstAndOptionsAreValidated(); ArcForges.Observability.Desktop.DesktopDiagnostics.ReadRecent(int) -> ArcForges.Observability.Desktop.Tests.LocalStoreTests.TheLocalViewIsBoundedAndOrderedOldestFirstAndOptionsAreValidated(); ArcForges.Observability.Desktop.DesktopDiagnostics.Dispose() -> ArcForges.Observability.Desktop.Tests.VerboseSessionTests.DisposingTheDiagnosticsEndsAVerboseSessionAndRefusesANewOne(); ArcForges.Observability.Desktop.VerboseDiagnosticSession.Start(System.TimeSpan) -> ArcForges.Observability.Desktop.Tests.VerboseSessionTests.AVerboseSessionKeepsDetailLocallyOnlyWhileActiveAndEndsOnItsOwn(); ArcForges.Observability.Desktop.VerboseDiagnosticSession.Stop() -> ArcForges.Observability.Desktop.Tests.VerboseSessionTests.AVerboseSessionIsBoundedStoppableAndNeverEnablesUpload(); ArcForges.Observability.Desktop.DesktopDiagnostics.CreateReport(ArcForges.Observability.Desktop.DiagnosticReportOptions?) -> ArcForges.Observability.Desktop.Tests.ReportTests.AReportIsGeneratedShownInFullAndSentOnlyAfterApproval(); ArcForges.Observability.Desktop.DiagnosticReportDraft.Preview() -> ArcForges.Observability.Desktop.Tests.ReportTests.AReportIsGeneratedShownInFullAndSentOnlyAfterApproval(); ArcForges.Observability.Desktop.DiagnosticReportDraft.Approve() -> ArcForges.Observability.Desktop.Tests.ReportTests.AReportIsGeneratedShownInFullAndSentOnlyAfterApproval(); ArcForges.Observability.Desktop.ApprovedDiagnosticReport.SendAsync(ArcForges.Observability.Desktop.IDiagnosticReportUploader, System.Threading.CancellationToken) -> ArcForges.Observability.Desktop.Tests.ReportTests.AReportIsGeneratedShownInFullAndSentOnlyAfterApproval(); ArcForges.Observability.Desktop.IDiagnosticReportUploader.UploadAsync(ArcForges.Observability.Desktop.DiagnosticReportUpload, System.Threading.CancellationToken) -> ArcForges.Observability.Desktop.Tests.ReportTests.AReportIsGeneratedShownInFullAndSentOnlyAfterApproval(); ArcForges.Observability.Desktop.DesktopDiagnostics.RecordCrash(System.Exception) -> ArcForges.Observability.Desktop.Tests.ReportTests.ACrashIsKeptLocallyNeverUploadedAutomaticallyAndSentOnlyAfterApproval(); ArcForges.Observability.Desktop.DesktopDiagnostics.TryGetPendingCrashReport(ArcForges.Observability.Desktop.DiagnosticReportOptions?) -> ArcForges.Observability.Desktop.Tests.ReportTests.ACrashIsKeptLocallyNeverUploadedAutomaticallyAndSentOnlyAfterApproval(); ArcForges.Observability.Desktop.DesktopDiagnostics.DismissPendingCrashReport() -> ArcForges.Observability.Desktop.Tests.ReportTests.ADismissedCrashReportIsDiscardedWithoutAnythingBeingSent(). Boundaries: the project must not reference the Shell, DesignSystem or any UI project; it exposes presentation-neutral state and registered reason-code failures that the PLT.31 error presentation and the shell consent surface consume. It holds no uploader and no telemetry transport: both are supplied per use, and neither is invoked except through the consent-gated sink while consent is granted, or for a report the user previewed and approved. Not authorized: eng/packaging/packages.json or any package identity (PLT.53 owns admission and publication), eng/policy/telemetry-policy.json, .gitleaks.toml or any scan allowlist (the receipt-directory group merged with PLT.44 covers the mirrored receipt lines and must not be widened; add no hash-like literal to tests), or any other task's rows. Outcome, prerequisites and completion evidence are unchanged.
```

```text
Execute ArcForges delivery task PLT.53 — Publish Observability packages and verify real integration.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\platform.md (anchor task-plt-53).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/plt-53 (python tools/delivery.py claim PLT.53 --worker <name>); task branch task/plt-53 in DesktopPlatform; ledger record ledger/tasks/plt-53.md.
Kind/size: acceptance/S. Baseline: not-started.
Outcome: ArcForges.Observability and.Observability.Desktop are packed, admitted, published and independently consumed; a trace can join one request across owners without logging prompts/credentials/unbounded payloads; health distinguishes backend/CF/model/R2 failures once those exist.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-12.90 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\12-observability-foundation.md, anchor rule-wp-12.90

Entry condition: adoption slice ADOPT.02.platform is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] PLT.47: emission/dimensions
- [artifact] PLT.48: correlation/causation
- [artifact] PLT.49: redaction
- [artifact] PLT.50: cardinality/sampling
- [artifact] PLT.51: health probes
- [artifact] PLT.52: diagnostics/consent
Completion prerequisites (may start earlier; cannot complete before these are complete):
- [integration] PLT.48: PLT.48 completion, including the real Cloud HTTP/queue/worker/realtime/provider hop

Permitted write scope: DesktopPlatform:eng/packaging/packages.json; DesktopPlatform:src/BuildingBlocks/ArcForges.Observability/ArcForges.Observability.csproj (final IsPackable/package activation only: IsPackable, PackageId, PackageReadmeFile, Description and the README/LICENSE/NOTICE pack items, mirroring ArcForges.Capabilities; no reference, package, version, source or setting change); DesktopPlatform:src/BuildingBlocks/ArcForges.Observability.Desktop/ArcForges.Observability.Desktop.csproj (final IsPackable/package activation only, as for ArcForges.Observability; the existing InternalsVisibleTo item stays as merged); DesktopPlatform:src/BuildingBlocks/ArcForges.Observability/AssemblyPlaceholder.cs (delete only: the existing PublishedProjectsAreExplicitAndContainNoPlaceholders gate refuses a packable project directory containing a *Placeholder.cs file, and nothing references the type); DesktopPlatform:src/BuildingBlocks/ArcForges.Observability/README.md (factual package status, contents, consumption and accuracy corrections only); DesktopPlatform:src/BuildingBlocks/ArcForges.Observability.Desktop/README.md (factual package status, contents, consumption and accuracy corrections only); DesktopPlatform:eng/policy/dependency-policy.json (refresh only the packages.json input hash and the two project file input hashes, mirrored in review.inputHashes, and point reviewReceipt to the PLT.53 successor); DesktopPlatform:eng/policy/dependency-reviews/plt-53-r1.json (new immutable PLT.53 receipt successor chained from the then-active receipt with an unchanged NuGet closure); DesktopPlatform:eng/provenance/files.json (append only the PLT.53 receipt path and remove only the deleted placeholder path); DesktopPlatform:eng/policy/reconciliation/active-projects.json (update only the two exact PLT.53 project blobs)
Shared resources (follow the owner protocol): RES-desktopplatform-package-inventory (append): Each producer task adds its own package entry; every merge to main packs and publishes all packages at one version; consumers pin the candidate produced by the merge of the capability they need, never waiting for a package closure task; one merge queue.; RES-desktopplatform-build-config (append): Solution/project lists, central package versions and CI job lists are appended by the task that adds a project, dependency or job; dependency additions follow the dependency-admission policy with a reviewed receipt; lock files are regenerated after rebase and never hand-merged; the integration owner resolves ordering conflicts at merge.; RES-desktopplatform-policy-data (append): Generated policy data is regenerated from its pinned source and never hand-edited; the reason-code registry is append-only with stable codes; each task adds its own test classes and evidence rows.

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): P2-017: offline verify/policy tests; Cloud-side hop evidence deferred per PLT.48's complete edge.
Completion evidence for the ledger: Owned artifact and real-integration receipt per WP-12.90.
Notes: ADP-07 binding for the package activation of two existing projects; it grants no new runtime behavior, dependency owner, package coordinate or version, security suppression or policy algorithm, and no package identity beyond the two the Outcome names (ArcForges.Observability and ArcForges.Observability.Desktop). The planned scope listed only the catalogue, which cannot activate a package: the packable-iff-listed repository policy test (RepositoryPolicyTests.PublishedProjectsAreExplicitAndContainNoPlaceholders) requires each listed project to set IsPackable and to contain no *Placeholder.cs file, and the dependency-admission gate binds the hash of every project file and of packages.json. PLT.35 had its two project files in its own write scope (final IsPackable/package activation only); PLT.53 needs the same. The write scope is exactly the paths listed above. The activation sets IsPackable and package metadata on the two production projects and appends two catalogue entries whose dependency lists must equal the nuspec dependency set that dotnet pack generates (checked with packages.validate_generated_dependencies); it adds no project reference, package reference, central version or source behavior, so the locked NuGet closure keeps identical coordinates, versions and content hashes. The only source change is the deletion of the unreferenced public ArcForges.Observability.AssemblyPlaceholder type. The InternalsVisibleTo declarations for the two test assemblies, the internal null-by-default TelemetryConsent.BeforeGrantCommit test hook and the name shared by ArcForges.Observability.TelemetryConsent and ArcForges.Observability.Desktop.TelemetryConsent (fixed by merged RP-10 rows) are not changed by this task; PLT.53 re-confirms and records them as published-surface facts and documents them in the two READMEs. Resource owners and protocols: RES-desktopplatform-package-inventory (append) for the catalogue entries, RES-desktopplatform-build-config (append) for the project files, and RES-desktopplatform-policy-data (append) for the receipt chain, provenance row and reconciliation snapshot; regenerate or re-append after rebase and chain the receipt from the receipt active on main at merge. Not authorized: any other source file, any test, any packages.lock.json, Directory.Packages.props, workflow, .gitleaks.toml or scan allowlist (the receipt-directory group merged with PLT.44 covers the mirrored receipt lines and must not be widened; add no hash-like literal), eng/policy/telemetry-policy.json, eng/policy/architecture-contract-tests.json, any exporter or telemetry transport, or any other task's rows. Real-integration verification stays within P2-017: one local opt-in consumer of the locally packed packages outside the repository; no installed-package consumer in CI, no GUI or browser end-to-end, no download or hash audit of published bytes. Outcome, prerequisites and completion evidence are unchanged: the Cloud-side cross-owner hop remains the PLT.48 completion edge.
```

```text
Execute ArcForges delivery task PLT.54 — Real hostile-input containment proof with the production still-image parser libraries loaded in ContentSandbox (PDF retired).

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\platform.md (anchor task-plt-54).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/plt-54 (python tools/delivery.py claim PLT.54 --worker <name>); task branch task/plt-54 in DesktopPlatform; ledger record ledger/tasks/plt-54.md.
Kind/size: integration/M. Baseline: not-started.
Outcome: that PG-22's OS isolation mechanics (proven against a first-party hostile test parser in PLT.45) hold once the production still-image parser libraries (the NAT.11 family, composed into the same helper by NAT.31) are loaded; PDF parsing is retired (P2-022) and has no containment leg here; this is the point where the SUB-hostile-test-parser substitute is replaced for the image family.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-11.09 (containment mechanics re-verified against the real still-image parser closure (PDF containment retired, P2-022)): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\11-security-foundation.md, anchor rule-wp-11.09
- WP-13.13 (image-family production parser containment evidence through the still-image composition from NAT.31; the PDF containment leg is retired (P2-022) and not claimed): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\13-high-risk-technical-probes.md, anchor rule-wp-13.13

Entry condition: adoption slice ADOPT.02.platform is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] PLT.45: real, delivered outcome of PLT.45 (Content helper and OS-enforced isolation (ContentSandbox host))
- [artifact] NAT.31: still-image parser composition (NAT.11 family) loaded into the ContentSandbox helper (NAT.31)
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:src/DesktopHelpers/ArcForges.ContentSandbox/Tests/RealImageParserContainmentTests.cs (new; real still-image parser containment cases through the production composition inside the restricted helper); DesktopPlatform:src/DesktopHelpers/ArcForges.ContentSandbox/Tests/OsIsolationTests.cs (existing; append real image-parser cases only); DesktopPlatform:src/DesktopHelpers/ArcForges.ContentSandbox/Tests/HostileHelperTests.cs (existing; append real image hostile-input cases only); DesktopPlatform:src/DesktopHelpers/ArcForges.ContentSandbox/Tests/Images/** (new packaged valid and malformed still-image fixtures; no PDF fixtures); DesktopPlatform:src/DesktopHelpers/ArcForges.ContentSandbox/Tests/ArcForges.ContentSandbox.Tests.csproj (content entries for Tests/Images/** only); DesktopPlatform:eng/provenance/files.json (append only the new test-file and fixture rows)
Shared resources (follow the owner protocol): RES-desktopplatform-policy-data (append): Generated policy data is regenerated from its pinned source and never hand-edited; the reason-code registry is append-only with stable codes; each task adds its own test classes and evidence rows.
Unblocks: NAT.25, NAT.30, PLT.46

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Local real-integration run of the affected scenario in an existing environment, recorded once per admitted RID: Windows locally, and the Linux leg in the local WSL2 Debian distribution via wsl.exe -d Debian on a Linux-native filesystem with the distro, kernel, SDK and toolchain recorded (P2-024); offline and static checks in CI; no hosted runtime, device, browser, live-service or inference CI (P2-017).
Completion evidence for the ledger: PG-22 real-parser containment evidence for the still-image family: the OS isolation mechanics proven in PLT.45 (AppContainer/Job Object and Landlock/seccomp denial, resource bounds, parent-death cleanup) hold with the real image parser libraries loaded into the same helper. Every PLT.45 category is re-run against the real libraries: product-DB/token reads, outbound TCP/UDP/loopback, sibling-process access, spawn escape, oversized output, native crash, hang, memory exhaustion and parent-death cleanup, plus malformed-input cases; recorded per admitted RID (Linux leg in WSL2 Debian, P2-024). No PDF evidence.
Notes: Planning repair 2026-10-08 (DLV-34; P2-022): image-only (PDF retired). The start edge from superseded NAT.15 is retargeted to NAT.31, so the start set is PLT.45 and NAT.31 as P2-022 specifies. The write scope was empty before this repair. It now lists the new real-image test file and fixtures plus the two existing helper test files OsIsolationTests.cs and HostileHelperTests.cs (both present under DesktopPlatform src/DesktopHelpers/ArcForges.ContentSandbox/Tests). The research audit does not list these files; they are derived from the repository layout and PLT.45's hostile-containment scope. The evidence covers the full PLT.45 category set, not only the PG-22 subset. PLT.54 writes the ContentSandbox tree and eng/provenance/files.json, so NAT.25 starts after PLT.54 (DLV-11).
```

```text
Execute ArcForges delivery task PLT.57 — End-to-end capability invocation with real security enforcement inside one product.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\platform.md (anchor task-plt-57).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/plt-57 (python tools/delivery.py claim PLT.57 --worker <name>); task branch task/plt-57 in DesktopPlatform; ledger record ledger/tasks/plt-57.md.
Kind/size: integration/M. Baseline: not-started.
Outcome: that the WP-09.07 invocation pipeline's 'authorize' step, wired to the real WP-11.02 decision pipeline, actually gates a real product capability end to end (resolve -> availability -> freeze -> authorize -> invoke -> validate -> record -> audit), closing the IAuthorizer interface seam both PLT.24 and PLT.38 are built against.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-09.07 (real authorize-step integration): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\09-capability-contribution-and-resource-model.md, anchor rule-wp-09.07
- WP-11.02 (real invocation-pipeline attachment): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\11-security-foundation.md, anchor rule-wp-11.02

Entry condition: adoption slice ADOPT.02.platform is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] PLT.24: real, delivered outcome of PLT.24 (Invocation pipeline)
- [artifact] PLT.38: real, delivered outcome of PLT.38 (Decision pipeline and the four enforcement points)
- [artifact] APP.01: real, delivered outcome of APP.01 (Assistant.Abstractions host ports and application identity)
- [artifact] PLT.44: delivered ArcForges.Security.Audit: the durable store, EgressAuditSink, CapabilityLeaseEventAuditSink and the retention runner
Completion prerequisites (may start earlier; cannot complete before these are complete):
- [integration] APP.03: a real ArcScope product host composes every capability binding through CapabilityEnforcementGate.Enforce with the audit store connected (the security and egress audit sinks and the lease event sink writing to ArcForges.Security.Audit), and the egress-to-audit mapping decision recorded in ledger plt-44.md (Design architecture/08 EG-06 to EG-09) is applied in that host

Permitted write scope: DesktopPlatform:src/BuildingBlocks/ArcForges.Security/CapabilityEnforcement/** (the new nested non-packable production project ArcForges.Security.CapabilityEnforcement with ArcForges.Security.CapabilityEnforcement.csproj, its source and packages.lock.json: the real CapabilityInvocationAuthorization adapter over the Security decision pipeline); DesktopPlatform:src/BuildingBlocks/ArcForges.Security/ArcForges.Security.csproj (add only the Compile Remove of the nested CapabilityEnforcement source, exactly as the existing LocalRpcBoundary entry; no reference, package, version or setting change); DesktopPlatform:src/BuildingBlocks/ArcForges.Security/Tests/** (new offline tests for the adapter and the end-to-end invocation scenario including the audit composition, and in ArcForges.Security.Tests.csproj only the ProjectReferences to the new project and to ArcForges.Security.Audit, with the existing nested Tests lock regenerated); DesktopPlatform:src/BuildingBlocks/ArcForges.Security/README.md (factual status of the new nested project only); DesktopPlatform:DesktopPlatform.slnx (append only the ArcForges.Security.CapabilityEnforcement project line; the existing Security.Tests registration and CI test line already cover the tests); DesktopPlatform:Directory.Packages.props (append only ArcForges.Security.CapabilityEnforcement to the existing ArcForges.Contracts.Foundation 1.0.0-ci.216.1 MSBuildProjectName selector; preserve the 1.0.0-ci.113.1 default and every other entry); DesktopPlatform:eng/policy/architecture-contract-tests.json (append only exact PLT.57 public API-to-focused-test bindings, in the Security.Tests project); DesktopPlatform:eng/policy/architecture-projects.json (append only the ArcForges.Security.CapabilityEnforcement production project row); DesktopPlatform:eng/policy/licence-boundary.json (append only the ArcForges.Security.CapabilityEnforcement classification); DesktopPlatform:eng/policy/runtime-ownership.json (append only the ArcForges.Security.CapabilityEnforcement project role); DesktopPlatform:eng/provenance/files.json (append only PLT.57 first-party source, project, test, README, lock and immutable receipt paths); DesktopPlatform:eng/policy/reconciliation/active-projects.json (append only the ArcForges.Security.CapabilityEnforcement project path/blob row and refresh only the existing ArcForges.Security and ArcForges.Security.Tests project blobs); DesktopPlatform:eng/policy/dependency-policy.json (add only the exact PLT.57 project and lock input hashes, refresh only the Directory.Packages.props input hash and the changed Security and Security.Tests project and lock input hashes, mirrored in review.inputHashes, and point reviewReceipt to the PLT.57 successor); DesktopPlatform:eng/policy/dependency-reviews/plt-57-r1.json (new immutable PLT.57 receipt successor chained from the receipt active on main at merge, mirroring the active review and closure snapshots)
Shared resources (follow the owner protocol): RES-desktopplatform-build-config (append): Solution/project lists, central package versions and CI job lists are appended by the task that adds a project, dependency or job; dependency additions follow the dependency-admission policy with a reviewed receipt; lock files are regenerated after rebase and never hand-merged; the integration owner resolves ordering conflicts at merge.; RES-architecture-tests (append): Each repository policy task owns its suite; rule additions are append-only.; RES-desktopplatform-policy-data (append): Generated policy data is regenerated from its pinned source and never hand-edited; the reason-code registry is append-only with stable codes; each task adds its own test classes and evidence rows.
Unblocks: PLT.25, PLT.44, PLT.46

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Local real-integration run of the affected scenario in an existing environment, recorded once; offline and static checks in CI; no hosted runtime, device, browser, live-service or inference CI (P2-017). Audit composition (2026-10-05 repair): the end-to-end scenario composes one real AuditStore, the real EgressAuditSink and CapabilityLeaseEventAuditSink, the real EgressAuthority and CapabilityLeaseManager and the PLT.44 retention runner, drives an allowed and a refused egress, an issued, revoked, expired and task-ended lease and a purge of an expired month, and reads every event back from the store; a failing store refuses the allowed transfer and the lease issue.
Completion evidence for the ledger: that the WP-09.07 invocation pipeline's 'authorize' step, wired to the real WP-11.02 decision pipeline, actually gates a real product capability end to end (resolve -> availability -> freeze -> authorize -> invoke -> validate -> record -> audit), closing the IAuthorizer interface seam both PLT.24 and PLT.38 are built against.
Notes: Planning repair for the exact write scope (2026-10-04; DLV-34, scope moves only: no obligation, edge or acceptance is added, removed or retyped). The task had an empty write scope, but the outcome needs real code: the seam that PLT.24 built against is the CapabilityInvocationAuthorization delegate of ArcForges.Capabilities.InvocationPipeline (the 'IAuthorizer' of the outcome text is this seam; no type of that name exists), and PLT.38 delivered SecurityDecisionPipeline in ArcForges.Security. Neither project can host the adapter: ArcForges.Security is Foundation-only and must not reference the packable ArcForges.Capabilities (and its Sdk.Contracts package), and ArcForges.Capabilities is packable and cannot reference the non-packable Security, whose package admission PLT.46 owns. The adapter therefore lives in one new non-packable nested production project, ArcForges.Security.CapabilityEnforcement, inside the Security directory exactly as PLT.38 placed ArcForges.Security.LocalRpcBoundary (Design PR 205, Plan PR 242, Plan ledger/tasks/plt-38.md): it references only ArcForges.Security and ArcForges.Capabilities, produces the CapabilityInvocationAuthorization delegate backed by the real decision pipeline (resolve, availability, freeze, authorize, invoke, validate, record, audit stay in the Capabilities pipeline; the adapter supplies only the authorize step and maps the typed security decision to the pipeline's outcome without weakening owner-side final validation), and adds no package, version, native code, runtime owner or wire schema. The existing nested ArcForges.Security.Tests project (already in the solution and the package-validation workflow) references it for the offline tests, so no new test project, workflow or solution entry beyond the one production line is needed. Registered in the same policy files and under the same ADP-07 protocol as PLT.38 and APP.01 (solution, central-package selector, architecture-projects, licence-boundary, runtime-ownership, active-projects, provenance, dependency-policy and one new immutable receipt chained from the receipt active on main at merge). The only central-package change is appending the new project name to the existing ArcForges.Contracts.Foundation 1.0.0-ci.216.1 selector, as PLT.38 did, because central transitive pinning rejects restore of a project reaching ArcForges.Foundation under the 1.0.0-ci.113.1 default. The receipt re-binds only the changed project, lock and Directory.Packages.props input hashes with an unchanged NuGet closure (every coordinate the new closure contains is already recorded; the claimant verifies this by restoring the exact planned shape and comparing the lock to the recorded closure before editing, and stops for a planning repair if a coordinate is new). Package admission stays with PLT.46 (Security) and PLT.25 (Capabilities); this task adds no package. The APP.01 start edge is ordering only: the bound scope never references the APP.01 project. Not authorized: any other source file (including ArcForges.Capabilities and the ArcForges.Security sources delivered by PLT.38), any workflow, .gitleaks.toml or scan allowlist (add no hash-like literal and no file or project name containing a Gitleaks generic-api-key keyword such as key, secret, token or auth in any hashed inventory row; the project, directory and every file name under it must avoid those keywords, which is why the project is named CapabilityEnforcement and its source files must not be named for authorization; the claimant confirms with the pinned scanner evidence), eng/packaging/packages.json, tests/ArchitectureTests, any other task's rows, and any dependency, package version, closure expansion, package identity, schema or migration. The real permission, policy, trust and egress sources that the pipeline ports need are injected by the hosting product; this task proves the attachment and the unbypassable ordering with the real PLT.24 and PLT.38 implementations and records, honestly, which ports were test composition and what remains for a real product host. Resource owners and protocols: RES-desktopplatform-build-config (append) for the solution and selector lines, RES-architecture-tests (append) for the exact public API-to-test bindings, and RES-desktopplatform-policy-data (append) for the receipt chain, provenance, reconciliation and inventory rows; regenerate locks and re-append rows after rebase and chain the receipt from the receipt active on main at merge. Planning repair (2026-10-05, DLV-34; unlike the 2026-10-04 scope move above, this one adds acceptance): the PLT.57 completion follow-up gains the audit composition named in the validation text and the start edge on PLT.44, and PLT.44 gains a completion prerequisite on this task (PLT.44 notes and ledger/tasks/plt-44.md). The Security tests project may reference ArcForges.Security.Audit only as a ProjectReference (Audit already references Security, never the reverse, so there is no cycle; the Security.Tests lock and the dependency-policy input hashes it changes are in the dependency-policy scope above, the closure is unchanged because Microsoft.Data.Sqlite is already in that project lock, and the claimant stops for a planning repair if a coordinate is new). No file of ArcForges.Security.Audit is changed by this task; the retention runner is built by the PLT.44 follow-up. This composition is the strongest running configuration the repository can host before an ArcScope process exists; a real product process and the owner-side final validation of a real product capability remain acceptance of the app-composition and ArcScope tasks, and the follow-up must state exactly which parts were test composition. Planning repair 2026-10-08 (DLV-34; P2-021): completion edge to APP.03 (the ArcScope product composition task) added so the shipped product host, not only the in-process scenario, composes every capability binding through CapabilityEnforcementGate.Enforce with the audit store connected and applies the egress-to-audit mapping decision of ledger plt-44.md. The APP.03 acceptance carrying this need is set in this patch. APP.03 consumes the audit store and the gate as published packages: ArcForges.Security.Audit and ArcForges.Security.CapabilityEnforcement, admitted and published by PLT.46 (packaging route; the CapabilityEnforcement project is non-packable at this delivered record, and its packability is the PLT.46 repair, not an edit to this record). Outcome, validation and evidence of PLT.57 are unchanged. Ledger plt-57.md records the status delivered. Planning repair 2026-10-08 (DLV-34; P2-021, coordinator adjudication on the real product host): a completion edge to APP.03 is added, so the real ArcScope product host that composes every capability binding through CapabilityEnforcementGate.Enforce with the audit store connected is part of this task’s completion; this supersedes any earlier note that says no edge changed.
```
