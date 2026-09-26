# ArcForges delivery task prompts — Cloud core

Generated from Design `docs/planning/delivery/delivery-graph.json` by `tools/delivery.py`; do not edit by hand.
Each block is self-contained. Claim a task only when `python tools/delivery.py ready` lists it, with
`python tools/delivery.py claim <TASK-ID> --worker <name>`, then follow `arcforges-implementation.md`.
Tasks are ordered by lane for reading; the order is not a schedule.

## Cloud core

```text
Execute ArcForges delivery task CLOUD.01 — Ingress and host pipeline.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\cloud.md (anchor task-cloud-01).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/cloud-01 (python tools/delivery.py claim CLOUD.01 --worker <name>); task branch task/cloud-01 in Cloud; ledger record ledger/tasks/cloud-01.md.
Kind/size: service/M. Baseline: not-started.
Outcome: Worker /api routing plus the C# AOT gRPC-Web/auth/current-owner pipeline runs behind the Worker in the real Container image; no buffered stream, no direct public Container port.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-21.00 (all work except the parts mapped to CLOUD.37): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\21-cloud-host-and-persistence.md, anchor rule-wp-21.00

Entry condition: adoption slice ADOPT.07.cloud is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [contract] CON.91: published ArcForges.Contracts.PublicApi generated gRPC-Web service stubs to register the pipeline against
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Cloud:worker/index.ts; Cloud:worker/router.ts; Cloud:wrangler.json; Cloud:src/ArcForges.Cloud.Host/**; Cloud:Dockerfile
Shared resources (follow the owner protocol): RES-cloud-deployment (append): Bindings are added by the owning module task in its own section, and the Cloud integration owner resolves ordering conflicts at merge. Any task that runs against the deployed test environment holds the lease `leases/res-cloud-deployment` for that live run only, whatever mode it declares for its binding edits; production deployment belongs to release tasks.
Unblocks: CLOUD.02, CLOUD.05, CLOUD.08, CLOUD.09, CLOUD.10, CLOUD.19, CLOUD.37, CLOUD.42, HAR.00, PLT.48

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): offline unit tests for routing/validation logic; deployed-environment request/stream/cancel/CSRF/trailer path checks are opt-in local runtime evidence per docs/validation-policy.md, not hosted CI
Completion evidence for the ledger: source commit, Worker/Container image hash, deployed request/stream/cancel/CSRF/trailer scenario results, confirmation no buffered stream or direct public Container port exists
Notes: Foundation task. The Hello World router.ts already proves the deadline/cancel/body-limit/trailer mechanics at small scale (see worker/router.ts); WP21.00 generalizes this to real dispatch. Early risk: every later public call depends on this boundary being correct.
```

```text
Execute ArcForges delivery task CLOUD.02 — Twenty-one module boundaries and D1 named-plan bridge.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\cloud.md (anchor task-cloud-02).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/cloud-02 (python tools/delivery.py claim CLOUD.02 --worker <name>); task branch task/cloud-02 in Cloud; ledger record ledger/tasks/cloud-02.md.
Kind/size: service/M. Baseline: not-started.
Outcome: The 21 module projects exist as boundaries and the D1 named-plan bridge mechanism works: C# decides business logic and asks the Worker to execute one exact named/versioned plan; the Worker executes only approved SQL, never ad hoc queries.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-21.02 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\21-cloud-host-and-persistence.md, anchor rule-wp-21.02

Entry condition: adoption slice ADOPT.07.cloud is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] CLOUD.01: the deployed ingress/host pipeline to carry the private C#<->Worker plan-execution calls
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Cloud:src/ArcForges.Cloud.Modules.*/**; Cloud:src/ArcForges.Cloud.Storage.D1/**; Cloud:storage/plans/**
Shared resources (follow the owner protocol): RES-cloud-storage-plans (append): Each module owns its own plan directory; the plan-manifest hash is regenerated by the author after rebase and checked in CI.
Unblocks: CLOUD.03, CLOUD.04, CLOUD.06, CLOUD.07, CLOUD.08, CLOUD.10, CLOUD.11, SIM.01

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): offline architecture/import tests (no forbidden cross-module reference), plan-hash tests, wrong-container/public-access refusal tests, AOT compile
Completion evidence for the ledger: architecture/import/plan-hash/wrong-container/public-access refusal test results, source commit and plan-manifest hash
Notes: Foundation task and the security-model proof: if the C#-decides/Worker-executes-approved-SQL-only boundary is wrong, every module built on it inherits the defect. Every module task (Identity, Sync, Resource, etc.) in this and other areas starts against this.
```

```text
Execute ArcForges delivery task CLOUD.03 — D1 migration runner and exact physical mapping.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\cloud.md (anchor task-cloud-03).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/cloud-03 (python tools/delivery.py claim CLOUD.03 --worker <name>); task branch task/cloud-03 in Cloud; ledger record ledger/tasks/cloud-03.md.
Kind/size: service/L. Baseline: not-started.
Outcome: Model-04's full physical manifest is implemented: migrations, typed exact bind/result adapters for D1's signed64/uint64/Decimal/JSON/FTS5 quirks, and expand/backfill/fenced-cutover migration mode support.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-21.03 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\21-cloud-host-and-persistence.md, anchor rule-wp-21.03
- WP-21:6-impacts-migration-compatibility-manife §6 Impacts -- migration/compatibility manifests include source/schema/plan/ABI/runtime versions (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\21-cloud-host-and-persistence.md, package-level obligation

Entry condition: adoption slice ADOPT.07.cloud is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] CLOUD.02: module boundary projects to attach physical tables to (physical table name = <module>_<snake_case_entity>)
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Cloud:src/ArcForges.Cloud.Storage.D1/Migrations/**; Cloud:src/ArcForges.Cloud.Storage.D1/Physical/**
Shared resources (follow the owner protocol): RES-cloud-d1-migrations (append): One global D1 migration sequence: each module task authors migrations under its module prefix; the integration owner assigns the global sequence number at merge, regenerates the plan manifest and rejects edits to merged migrations; the migrator applies in sequence with receipts.
Unblocks: CLOUD.04, CLOUD.07, CLOUD.09, CLOUD.10, CLOUD.11, CLOUD.37, CLOUD.48

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): offline unit tests for bind/result adapters; opt-in local runtime tests against a real D1 instance for signed64/uint64/Decimal/JSON/FTS5, interrupted migration, stale backfill and compatible rollback per docs/validation-policy.md
Completion evidence for the ledger: actual D1 signed64/uint64/decimal/JSON/FTS5 conformance results, interrupted-migration/stale-backfill/rollback test results, source commit
Notes: Early risk proof: D1's real type/SQL quirks (signed 64-bit only, no native uint64/Decimal, JSON1, FTS5 behavior) affect the physical design of all 21 modules' tables. Getting the bind/result adapters wrong here would force rework across every later module task in every area that stores data in D1.
```

```text
Execute ArcForges delivery task CLOUD.04 — Receipts, outbox, inbox dedup and change archive.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\cloud.md (anchor task-cloud-04).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/cloud-04 (python tools/delivery.py claim CLOUD.04 --worker <name>); task branch task/cloud-04 in Cloud; ledger record ledger/tasks/cloud-04.md.
Kind/size: service/M. Baseline: not-started.
Outcome: Every atomic guarded write also produces its owner receipt, outbox entry and change-archive row in the same D1 batch; inbox dedup makes replay a no-op; publication is contiguous (no gaps).

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-21.04 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\21-cloud-host-and-persistence.md, anchor rule-wp-21.04

Entry condition: adoption slice ADOPT.07.cloud is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] CLOUD.02: the D1 named-plan bridge to add receipt/outbox/inbox writes inside
- [artifact] CLOUD.03: physical platform.command/outbox/inbox tables (data-model/01 §2 platform infra tables)
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Cloud:src/ArcForges.Cloud.Storage.D1/Receipts/**; Cloud:src/ArcForges.Cloud.Storage.D1/Outbox/**
Unblocks: CLOUD.05, CLOUD.10, CLOUD.31, CLOUD.39, SIM.04

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): offline unit tests plus opt-in local D1 runtime tests: constraint-guard failure rolls back all rows, zero-row CAS cannot publish, duplicate/lost ack reconciles
Completion evidence for the ledger: constraint-guard rollback, zero-row-CAS and duplicate/lost-ack reconciliation results
Notes: This generic outbox mechanism is distinct from (a) WP-24.04's DO wake/live-feed publisher and (b) WP-25.02's sync.change publish_seq bootstrap publisher; both consume this task's committed outbox rows but each adds its own D1-batch publication logic..
```

```text
Execute ArcForges delivery task CLOUD.05 — Finite durable jobs (Cron/Queue/Workflow-woken endpoints).

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\cloud.md (anchor task-cloud-05).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/cloud-05 (python tools/delivery.py claim CLOUD.05 --worker <name>); task branch task/cloud-05 in Cloud; ledger record ledger/tasks/cloud-05.md.
Kind/size: service/M. Baseline: not-started.
Outcome: Perpetual hosted loops are replaced by Cron/Queue/Workflow-woken C# endpoints bounded to <=100 items/20s per job with checkpoint/receipt/lease-then-yield semantics.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-21.01 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\21-cloud-host-and-persistence.md, anchor rule-wp-21.01

Entry condition: adoption slice ADOPT.07.cloud is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] CLOUD.01: the deployed Worker/Container ingress to attach Cron/Queue/Workflow triggers to
- [artifact] CLOUD.04: receipt/lease primitives to checkpoint job progress
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Cloud:src/ArcForges.Cloud.Jobs/**
Shared resources (follow the owner protocol): RES-cloud-deployment (append): Bindings are added by the owning module task in its own section, and the Cloud integration owner resolves ordering conflicts at merge. Any task that runs against the deployed test environment holds the lease `leases/res-cloud-deployment` for that live run only, whatever mode it declares for its binding edits; production deployment belongs to release tasks.
Unblocks: CLOUD.10, CLOUD.33, CLOUD.45, HAR.00, SIM.03

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): opt-in local runtime tests: sleep/restart, duplicate wake, delayed delivery, stale lease, paused simulator continuation
Completion evidence for the ledger: sleep/restart, duplicate-wake, delayed-delivery, stale-lease and paused-simulator-continuation results
Notes: This is the generic mechanism later background jobs plug into: WP-25.02's publisher, WP-25.06 realm-transfer jobs, WP-46 backup jobs, notification delivery retries.
```

```text
Execute ArcForges delivery task CLOUD.06 — Shared atomic family guarded-batch engine.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\cloud.md (anchor task-cloud-06).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/cloud-06 (python tools/delivery.py claim CLOUD.06 --worker <name>); task branch task/cloud-06 in Cloud; ledger record ledger/tasks/cloud-06.md.
Kind/size: service/M. Baseline: not-started.
Outcome: A reusable D1 guarded-batch executor exists that enforces the fixed SU-04 module lock order (Config->Identity->Workspace->Device->Entitlement->Commerce->Policy->Agent->Chat->Notes->Scope->Slate->Task->Search->PackageCatalog->Notification->Resource->Sync->Audit) and provides authorization/revision/policy/balance/lease guard primitives that any shared-transaction family can compose.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-21.05 (generic guarded-batch engine and fixed SU-04 module lock-order enforcement only; each module's own family participant list is a separate obligation carried by that module's own task (see coverage)): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\21-cloud-host-and-persistence.md, anchor rule-wp-21.05

Entry condition: adoption slice ADOPT.07.cloud is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] CLOUD.02: the D1 named-plan bridge, since a guarded batch is executed as one named plan
Completion prerequisites (may start earlier; cannot complete before these are complete):
- [integration] CLOUD.63: at least two real module family participants exercising the engine under contention (e.g. Identity's auth/enrollment family and Notes/Sync's synced-content-mutation family)

Permitted write scope: Cloud:src/ArcForges.Cloud.Storage.D1/SharedFamilies/**
Shared resources (follow the owner protocol): RES-shared-transaction-families (append): Adding a participant to a shared atomic family is a design change through the Architecture Owner; module tasks implement only their declared participation.
Unblocks: CLOUD.07, CLOUD.10, CLOUD.11, CLOUD.13, CLOUD.37, CLOUD.42, CLOUD.46, CLOUD.63, SIM.03

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): offline unit tests for the guard/lock-order primitives; opt-in local D1 runtime tests: two Containers contend, stale holder cannot finalize
Completion evidence for the ledger: lock-order enforcement test results, contention/stale-holder test results, source commit
Notes: Every module task that participates in a named shared-transaction family (CLOUD.11/13 Identity's auth-enrollment/device-revocation families, CLOUD.37/38 Notes' synced-content-mutation family, CLOUD.42 Resource's upload-lifecycle family, CLOUD.53 realm-transfer family) declares a start edge on this task and fills in its own participant logic; WP-21.05 substep coverage therefore spans CLOUD.06 plus those module tasks with differing `part` text.
```

```text
Execute ArcForges delivery task CLOUD.07 — Capacity, Container/D1 integration producer and harness.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\cloud.md (anchor task-cloud-07).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/cloud-07 (python tools/delivery.py claim CLOUD.07 --worker <name>); task branch task/cloud-07 in Cloud; ledger record ledger/tasks/cloud-07.md.
Kind/size: service/L. Baseline: not-started.
Outcome: Model-04 named plans run through guarded-batch fixtures under measured load; the primary-authorization path, route/service-binding/outbound-handler matrix, job-slice and SimulationPacer infrastructure exist; the L-16 measurement harness and a proposed capacity report are produced.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-21.06 (all work except the parts mapped to SIM.10): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\21-cloud-host-and-persistence.md, anchor rule-wp-21.06

Entry condition: adoption slice ADOPT.07.cloud is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] CLOUD.02: module boundary + plan bridge to issue guarded-batch fixture plans against
- [artifact] CLOUD.03: physical D1 schema to measure real write/read latency against
- [artifact] CLOUD.06: the guarded-batch engine, since capacity fixtures are guarded batches
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Cloud:src/ArcForges.Cloud.Capacity/**; Cloud:wrangler.json
Shared resources (follow the owner protocol): RES-cloud-deployment (append): Bindings are added by the owning module task in its own section, and the Cloud integration owner resolves ordering conflicts at merge. Any task that runs against the deployed test environment holds the lease `leases/res-cloud-deployment` for that live run only, whatever mode it declares for its binding edits; production deployment belongs to release tasks.
Permitted substitutes (never real integration evidence): SUB-guarded-batch-capacity-fixtures: capacity/latency/contention envelope under synthetic load only, never business correctness Real producer ['CLOUD.47', 'COM.15']; removed by REL.06
Unblocks: CLOUD.10, COM.07, SIM.03, SIM.10

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): opt-in local + real-deployed D1 rollback/duplicate/competing-writer/cold-start tests; public/internal denial, blocked egress, forged service headers, stream-limit and headroom measurement
Completion evidence for the ledger: L-16 measurement harness output, proposed capacity report, real D1 rollback/duplicate/competing-writer/cold-start results, public/internal denial and forged-header refusal results
Notes: Can proceed in parallel with WP-22/23/24/25 module work once CLOUD.01-04/06 exist, because it uses its own guarded-batch fixtures rather than waiting for real module business logic.
```

```text
Execute ArcForges delivery task CLOUD.08 — Failure isolation and readiness surface.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\cloud.md (anchor task-cloud-08).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/cloud-08 (python tools/delivery.py claim CLOUD.08 --worker <name>); task branch task/cloud-08 in Cloud; ledger record ledger/tasks/cloud-08.md.
Kind/size: service/S. Baseline: not-started.
Outcome: Ingress/Container/D1/DO/R2/Queue health are exposed separately, and a missing binding or plan-hash mismatch fails readiness rather than allowing partial execution to appear successful; logs remain no-content.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-21.07 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\21-cloud-host-and-persistence.md, anchor rule-wp-21.07

Entry condition: adoption slice ADOPT.07.cloud is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] CLOUD.01: the deployed ingress/Container to expose readiness for
- [artifact] CLOUD.02: the plan-manifest hash to check for mismatch
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Cloud:src/ArcForges.Cloud.Host/Readiness/**
Unblocks: CLOUD.10

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): opt-in local runtime tests: missing binding/plan mismatch fails readiness, not successful partial execution
Completion evidence for the ledger: missing-binding and plan-mismatch readiness-failure results
Notes: Can be built in parallel with WP-22/23/24/25 once CLOUD.01/02 exist; readiness for R2/Queue/DO bindings can be checked even while those bindings are still otherwise unused stubs.
```

```text
Execute ArcForges delivery task CLOUD.09 — Selfhost.v1 deployment profile.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\cloud.md (anchor task-cloud-09).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/cloud-09 (python tools/delivery.py claim CLOUD.09 --worker <name>); task branch task/cloud-09 in Cloud; ledger record ledger/tasks/cloud-09.md.
Kind/size: service/M. Baseline: not-started.
Outcome: An operator-owned Cloudflare deployment/config/realm descriptor exists for self-hosting, with default payment disabled, separate keys/identity/providers from the official realm, immutable artifacts and independent backup requirements preserved.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-21.08 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\21-cloud-host-and-persistence.md, anchor rule-wp-21.08

Entry condition: adoption slice ADOPT.07.cloud is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] CLOUD.01: a deployable Worker/Container image to define a second deployment profile for
- [artifact] CLOUD.03: the D1 physical schema/migration runner to provision a fresh realm's database
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Cloud:docs/deployment.md; Cloud:eng/selfhost/**
Shared resources (follow the owner protocol): RES-cloud-deployment (append): Bindings are added by the owning module task in its own section, and the Cloud integration owner resolves ordering conflicts at merge. Any task that runs against the deployed test environment holds the lease `leases/res-cloud-deployment` for that live run only, whatever mode it declares for its binding edits; production deployment belongs to release tasks.
Unblocks: CLOUD.10

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): opt-in local + real Cloudflare dev-account tests: fresh development account/realm provisioning, missing binding/secret/unsupported descriptor/redirect failures, no official token acceptance
Completion evidence for the ledger: fresh provisioning, missing-binding/secret refusal, and no-official-token-acceptance results
Notes: WP-21's own completion gate states this task hands WP-46 'a runnable deployment and complete configuration inventory'; production PG-25 evidence stays external. Can run in parallel with WP-22/23/24/25 once CLOUD.01/03 exist.
```

```text
Execute ArcForges delivery task CLOUD.10 — Owned-artifact closure and launch-capacity.v1 acceptance.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\cloud.md (anchor task-cloud-10).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/cloud-10 (python tools/delivery.py claim CLOUD.10 --worker <name>); task branch task/cloud-10 in Cloud; ledger record ledger/tasks/cloud-10.md.
Kind/size: integration/M. Baseline: not-started.
Outcome: Every WP-21 substep is complete, built/packed once, and consumed as exact candidate bytes from a clean environment; launch-capacity.v1 is produced and tested (four fixed standard-2 slots, no per-account instance creation, idle sleep/wake, pre-dispatch refusal vs unknown dispatched outcome, control-slot reserve, Vectorize/R2 reservation thresholds at 60/70/80/90%).

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-21.90 (full, including the Launch configuration acceptance subsection (launch-capacity.v1, PG-26)): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\21-cloud-host-and-persistence.md, anchor rule-wp-21.90
- WP-21:6-impacts-migration-compatibility-manife §6 Impacts -- migration/compatibility manifests include source/schema/plan/ABI/runtime versions (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\21-cloud-host-and-persistence.md, package-level obligation

Entry condition: adoption slice ADOPT.07.cloud is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] CLOUD.37: package task delivered
- [artifact] SIM.10: package task delivered
Completion prerequisites (may start earlier; cannot complete before these are complete):
- [integration] CLOUD.01: final candidate build
- [integration] CLOUD.02: final candidate build
- [integration] CLOUD.03: final candidate build
- [integration] CLOUD.04: final candidate build
- [integration] CLOUD.05: final candidate build
- [integration] CLOUD.06: final candidate build
- [integration] CLOUD.07: final candidate build
- [integration] CLOUD.08: final candidate build
- [integration] CLOUD.09: final candidate build

Permitted write scope: Cloud:artifacts/candidate/**
Shared resources (follow the owner protocol): RES-cloud-deployment (append): Bindings are added by the owning module task in its own section, and the Cloud integration owner resolves ordering conflicts at merge. Any task that runs against the deployed test environment holds the lease `leases/res-cloud-deployment` for that live run only, whatever mode it declares for its binding edits; production deployment belongs to release tasks.
Unblocks: REL.06

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): package/contract/owner/version compatibility, failure/recovery and the real boundaries above; publish/promote only the tested immutable bytes in the producer CI sequence (matches the existing candidate->verify->deploy CI job sequence)
Completion evidence for the ledger: cold-start and measured cost inputs; PG-26 explicitly cannot close on a localhost benchmark
Notes: Gate: PG-26. A localhost benchmark cannot close it per WP-21.90's own text.
```

```text
Execute ArcForges delivery task CLOUD.11 — Core identity model (realm, user, authIdentity, single-owner workspace).

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\cloud.md (anchor task-cloud-11).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/cloud-11 (python tools/delivery.py claim CLOUD.11 --worker <name>); task branch task/cloud-11 in Cloud; ledger record ledger/tasks/cloud-11.md.
Kind/size: service/M. Baseline: not-started.
Outcome: Realm, user, authentication identity and single-owner workspace exist with ownership as a direct workspace.owner_user_id check; no membership/role/seat table exists anywhere in schema, contracts or operations.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-22.00 (all work except the parts mapped to CLOUD.20): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\22-identity-workspace-and-device.md, anchor rule-wp-22.00

Entry condition: adoption slice ADOPT.07.cloud is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] CLOUD.02: module boundary + D1 plan bridge to implement the Identity module against
- [artifact] CLOUD.03: physical D1 schema/migration runner for identity.* tables
- [artifact] CLOUD.06: the shared atomic family engine, since core identity operations (enrollment, workspace provisioning) are shared-transaction families
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Cloud:src/Cloud/ArcForges.Cloud.Modules.Identity/Core/**
Shared resources (follow the owner protocol): RES-cloud-d1-migrations (append): One global D1 migration sequence: each module task authors migrations under its module prefix; the integration owner assigns the global sequence number at merge, regenerates the plan manifest and rejects edits to merged migrations; the migrator applies in sequence with receipts.; RES-cloud-storage-plans (append): Each module owns its own plan directory; the plan-manifest hash is regenerated by the author after rebase and checked in CI.; RES-shared-transaction-families (append): Adding a participant to a shared atomic family is a design change through the Architecture Owner; module tasks implement only their declared participation.
Unblocks: CLOUD.12, CLOUD.13, CLOUD.16, CLOUD.19, CLOUD.20, GOV.16, SRCH.03

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): offline structural tests: identity-change continuity, no membership/role/invitation/seat concept anywhere, no capability treats an auth identity as a user; AOT compile
Completion evidence for the ledger: identity-continuity and structural-separation test results
Notes: First real module built on the WP-21 foundation; unlocks the rest of WP-22.
```

```text
Execute ArcForges delivery task CLOUD.12 — Native and browser authentication with real Postmark/SES mail delivery.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\cloud.md (anchor task-cloud-12).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/cloud-12 (python tools/delivery.py claim CLOUD.12 --worker <name>); task branch task/cloud-12 in Cloud; ledger record ledger/tasks/cloud-12.md.
Kind/size: service/L. Baseline: not-started.
Outcome: Native authorize/token PKCE ceremony and minimal browser login UI work with passkey/email and configured self-host OIDC/password; real Postmark-primary/SES-secondary delivery and outcome adapters exist and prove live delivery/recovery, not a stub.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-22.01 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\22-identity-workspace-and-device.md, anchor rule-wp-22.01

Entry condition: adoption slice ADOPT.07.cloud is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] CLOUD.11: the core identity/authIdentity model to attach auth methods to
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Cloud:src/Cloud/ArcForges.Cloud.Modules.Identity/Auth/**; Cloud:src/Cloud/ArcForges.Cloud.Modules.Notification/**
Permitted substitutes (never real integration evidence): SUB-postmark-ses-test-recordings: Deterministic refusal, unknown-outcome and callback regression cases only; runtime registration is forbidden and live delivery is proven by the same task. Real producer ['CLOUD.12']; removed by CLOUD.12
Unblocks: CLOUD.15, CLOUD.17, CLOUD.18, CLOUD.20, OPS.09, WEB.10

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): actual email delivery/recovery and prepared-secondary tests; PKCE/state/redirect/code-replay, Credential Manager/RP origin fixtures, refresh contention and revocation -- real provider evidence, no CI hosted live-service run (per P2-017, this stays local opt-in)
Completion evidence for the ledger: real provider identity flow results; required accounts/DNS recorded as external inputs, never replaced by a stub acceptance
Notes: Must-be-real-early per implementation-sequence §3 ('Identity, refresh/session contention and real email delivery/recovery at WP22' is explicitly listed as Must be real early, not Push-until-later). Keep this must-be-real-early placement; do not move it later.
```

```text
Execute ArcForges delivery task CLOUD.13 — Device, installation, instance and session (four distinct concepts).

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\cloud.md (anchor task-cloud-13).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/cloud-13 (python tools/delivery.py claim CLOUD.13 --worker <name>); task branch task/cloud-13 in Cloud; ledger record ledger/tasks/cloud-13.md.
Kind/size: service/M. Baseline: not-started.
Outcome: Device, installation, instance and session are four distinct concepts with four lifecycles; device identity is stable but not a hardware fingerprint; device revocation cascades to sessions and push registrations.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-22.02 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\22-identity-workspace-and-device.md, anchor rule-wp-22.02

Entry condition: adoption slice ADOPT.07.cloud is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] CLOUD.11: the core identity model a device/session attaches to
- [artifact] CLOUD.06: the shared atomic family engine, since device revocation is a named shared-transaction family
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Cloud:src/Cloud/ArcForges.Cloud.Modules.Identity/Device/**
Shared resources (follow the owner protocol): RES-cloud-d1-migrations (append): One global D1 migration sequence: each module task authors migrations under its module prefix; the integration owner assigns the global sequence number at merge, regenerates the plan manifest and rejects edits to merged migrations; the migrator applies in sequence with receipts.; RES-shared-transaction-families (append): Adding a participant to a shared atomic family is a design change through the Architecture Owner; module tasks implement only their declared participation.
Unblocks: AND.07, CLOUD.14, CLOUD.15, CLOUD.19, CLOUD.20, CLOUD.21, DEV.01

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): offline structural distinction-matrix tests; revocation-cascade tests; hardware-change survival test
Completion evidence for the ledger: four-concept distinction matrix and revocation cascade results
```

```text
Execute ArcForges delivery task CLOUD.14 — Device trust and remote gating.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\cloud.md (anchor task-cloud-14).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/cloud-14 (python tools/delivery.py claim CLOUD.14 --worker <name>); task branch task/cloud-14 in Cloud; ledger record ledger/tasks/cloud-14.md.
Kind/size: service/S. Baseline: not-started.
Outcome: Trust levels per device exist with remote access defaulting to off; raising trust requires an explicit act with step-up; remote capability is derived from trust, never from mere session possession.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-22.03 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\22-identity-workspace-and-device.md, anchor rule-wp-22.03

Entry condition: adoption slice ADOPT.07.cloud is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] CLOUD.13: the device/session model to attach trust levels to
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Cloud:src/Cloud/ArcForges.Cloud.Modules.Identity/Trust/**
Unblocks: CLOUD.20

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): offline default-off assertion, trust-elevation-requires-step-up test, session-alone-insufficient test
Completion evidence for the ledger: default-off and session-insufficiency results
```

```text
Execute ArcForges delivery task CLOUD.15 — Step-up challenges for sensitive operations.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\cloud.md (anchor task-cloud-15).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/cloud-15 (python tools/delivery.py claim CLOUD.15 --worker <name>); task branch task/cloud-15 in Cloud; ledger record ledger/tasks/cloud-15.md.
Kind/size: service/M. Baseline: not-started.
Outcome: Step-up challenges exist for the enumerated sensitive operations, bounded validity window, no app-unlock substitution; step-up state is per session and per operation class.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-22.04 (the step-up mechanism itself and coverage for Cloud/Identity-owned sensitive operations (credential change, recovery, deletion, trust elevation); full coverage across every enumerated operation in every module is completed as each owning module wires it in -- see IM.step-up-cross-product-coverage): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\22-identity-workspace-and-device.md, anchor rule-wp-22.04

Entry condition: adoption slice ADOPT.07.cloud is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] CLOUD.12: real authentication methods to re-assert during a step-up challenge
- [artifact] CLOUD.13: the session model to scope step-up state to
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Cloud:src/Cloud/ArcForges.Cloud.Modules.Identity/StepUp/**
Unblocks: CLOUD.16, CLOUD.20, CLOUD.66

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): offline coverage-enumeration test, window-expiry test, app-unlock-does-not-substitute negative test
Completion evidence for the ledger: step-up coverage, expiry and non-substitution results
Notes: Aggregate-gate risk: WP-22.04's completion gate says 'every enumerated operation demands step-up', but the full enumeration spans Commerce (WP-42), PublicApi (WP-23) and client apps outside this area. This task delivers the mechanism plus Identity's own operations; see integration_proposals for the cross-product completion.
```

```text
Execute ArcForges delivery task CLOUD.16 — PAT and actor authorization.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\cloud.md (anchor task-cloud-16).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/cloud-16 (python tools/delivery.py claim CLOUD.16 --worker <name>); task branch task/cloud-16 in Cloud; ledger record ledger/tasks/cloud-16.md.
Kind/size: service/M. Baseline: not-started.
Outcome: patEligible/scopes metadata, hash-only token storage, expiry/revocation and one-time display after step-up are implemented; the actor chain is preserved and customer tokens are denied on operator/internal/local boundaries.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-22.05 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\22-identity-workspace-and-device.md, anchor rule-wp-22.05

Entry condition: adoption slice ADOPT.07.cloud is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] CLOUD.11: the core identity model a token belongs to
Completion prerequisites (may start earlier; cannot complete before these are complete):
- [integration] CLOUD.15: the step-up mechanism, since one-time PAT display happens after step-up

Permitted write scope: Cloud:src/Cloud/ArcForges.Cloud.Modules.Identity/Tokens/**
Unblocks: CLOUD.19, CLOUD.20, CLOUD.63, EXT.06, EXT.08

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): offline enumeration of eligible/denied methods from the generated manifest; cookie+bearer conflict, scope escalation and agent-substitution negative vectors
Completion evidence for the ledger: no missing/default PAT metadata, no generic token bypass
```

```text
Execute ArcForges delivery task CLOUD.17 — Recovery, account states and deletion.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\cloud.md (anchor task-cloud-17).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/cloud-17 (python tools/delivery.py claim CLOUD.17 --worker <name>); task branch task/cloud-17 in Cloud; ledger record ledger/tasks/cloud-17.md.
Kind/size: service/M. Baseline: not-started.
Outcome: Recovery flows resist modelled abuse; account states (active/restricted/suspended/pending-deletion) have defined capability; deletion has a grace period, explicit scope of what is/isn't deleted, and never touches local data.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-22.06 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\22-identity-workspace-and-device.md, anchor rule-wp-22.06

Entry condition: adoption slice ADOPT.07.cloud is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] CLOUD.12: real auth methods (passkey/email/OIDC) to build recovery flows on
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Cloud:src/Cloud/ArcForges.Cloud.Modules.Identity/Recovery/**
Unblocks: CLOUD.19, CLOUD.20, CLOUD.50

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): offline recovery-abuse tests, state-transition capability matrix, deletion-preserves-local-data test
Completion evidence for the ledger: recovery abuse-resistance, state matrix and deletion results
```

```text
Execute ArcForges delivery task CLOUD.18 — Independent native session integration (Platform client primitives).

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\cloud.md (anchor task-cloud-18).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/cloud-18 (python tools/delivery.py claim CLOUD.18 --worker <name>); task branch task/cloud-18 in DesktopPlatform; ledger record ledger/tasks/cloud-18.md.
Kind/size: service/M. Baseline: not-started.
Outcome: System browser, per-product redirects, secure storage and installation-bound tokens are integrated into Platform client primitives; each client owns its own session, no token sharing/device SSO.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-22.07 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\22-identity-workspace-and-device.md, anchor rule-wp-22.07

Entry condition: adoption slice ADOPT.02.cloud is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] CLOUD.12: the real native PKCE ceremony endpoints to integrate against
- [artifact] PLT.40: the local security foundation's secure storage primitive
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:src/BuildingBlocks/ArcForges.Security/**
Shared resources (follow the owner protocol): RES-assistant-store-schema (append): Numbered migrations are allocated at merge by the integration owner (a rebase renumbers pending migrations); each migration is forward-only with its recovery and downgrade-refusal tests; no task edits a merged migration.
Unblocks: AND.07, CLOUD.20, PLT.40

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): offline + opt-in local tests: separate product sign-in/sign-out, canceled/lost callback, wrong state/realm, expired code, device revoke, local history preservation
Completion evidence for the ledger: per-client session isolation results
Notes: Cross-repo: owned by WP-22 but lives in DesktopPlatform.
```

```text
Execute ArcForges delivery task CLOUD.19 — Browser cookie-session adapter and full account-surface closure.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\cloud.md (anchor task-cloud-19).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/cloud-19 (python tools/delivery.py claim CLOUD.19 --worker <name>); task branch task/cloud-19 in Cloud; ledger record ledger/tasks/cloud-19.md.
Kind/size: service/L. Baseline: not-started.
Outcome: The same-origin browser adapter runs in the AOT host with random hashed session/preauth/CSRF records, exact Origin checks, idle/absolute expiry, lowest-trust browser installation and one-use auth flow, with explicit cookie parsing/writing (no ASP.NET Data Protection/cookie-auth middleware); the full typed account surface is wired through the same owner ports.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-22.08 (full, including the 'Required implementation and closure from the final review' paragraph (complete typed account surface: profile/email, recovery-code set, scoped PAT, credential rename, session listing, four sign-out scopes, per-installation browser authorization, remote capability policy, restricted deletion-cancel reauthentication)): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\22-identity-workspace-and-device.md, anchor rule-wp-22.08
- WP-22:browser-session-evidence-note-wp-22-08-m Browser-session evidence note (WP-22.08 must pass before WP-23 consumes its contract; a written P2-003 decision alone is insufficient) (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\22-identity-workspace-and-device.md, package-level obligation

Entry condition: adoption slice ADOPT.07.cloud is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] CLOUD.01: the AOT host pipeline to implement the /session/* routes in
- [artifact] CLOUD.11: identity core model
- [artifact] CLOUD.13: device/installation/session model, since browser sessions are the lowest-trust browser installation
Completion prerequisites (may start earlier; cannot complete before these are complete):
- [integration] CLOUD.16: PAT mechanism for the scoped-PAT account surface
- [integration] CLOUD.17: recovery/deletion mechanism for the deletion-cancel reauthentication surface

Permitted write scope: Cloud:src/Cloud/ArcForges.Cloud.Host/Session/**; Cloud:src/Contracts/Public/ArcForges.Contracts.PublicApi.Identity/**
Unblocks: AND.07, CLOUD.20, CLOUD.21, CLOUD.26, CLOUD.29, WEB.11, WEB.30

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): opt-in local + real D1 tests: one-use challenge, lost-login response, idle-vs-revoke race, expiry, replica failover, exact Origin/CSRF on unsafe RPC/session/stream/object operations, native-token route refusal, gRPC-Web stream authorization, two-products-one-OS-user isolation
Completion evidence for the ledger: one server-owned session authority, no JS bearer, no cross-origin reuse or session resurrection; real database/concurrency, origin/CSRF/expiry and multi-replica results
Notes: Gate: PG-23 (this task's contribution; WP-23.05 contributes the other side). Feeds WP-23 and full portal acceptance -- WP-23 cannot consume this contract until it passes; a written P2-003 decision alone is insufficient per the WP text.
```

```text
Execute ArcForges delivery task CLOUD.20 — Owned-artifact closure and real integration.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\cloud.md (anchor task-cloud-20).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/cloud-20 (python tools/delivery.py claim CLOUD.20 --worker <name>); task branch task/cloud-20 in Cloud; ledger record ledger/tasks/cloud-20.md.
Kind/size: integration/M. Baseline: not-started.
Outcome: Native/Android bearer sessions, same-origin Web opaque sessions, passkeys/recovery, workspace/device rules and authenticated CF authorization ports work end-to-end using selected AOT-compatible components; real publish-mode auth/session/CSRF/origin/rotation/revocation tests pass including stale CF requests and browser credential secrecy.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-22.90 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\22-identity-workspace-and-device.md, anchor rule-wp-22.90
- WP-22:p2-010-required-behavior-and-closure-app P2-010 required behavior and closure appendix (initial enrollment/recovery/provider/account/SSO methods wired end-to-end in client journeys) (P2-010 required behavior and closure appendix (initial enrollment/recovery/provider/account/SSO methods wired end-to-end in client journeys)): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\22-identity-workspace-and-device.md, package-level obligation
- WP-22.00 (real identity/session implementation): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\22-identity-workspace-and-device.md, anchor rule-wp-22.00

Entry condition: adoption slice ADOPT.07.cloud is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] CON.07: real, delivered outcome of CON.07 (Identity/session/device operation registry + native-auth and browser HTTP exceptions)
- [artifact] CLOUD.11: real, delivered outcome of CLOUD.11 (Core identity model (realm, user, authIdentity, single-owner workspace))
- [artifact] CLOUD.66: package task delivered
Completion prerequisites (may start earlier; cannot complete before these are complete):
- [integration] CLOUD.12: final candidate
- [integration] CLOUD.13: final candidate
- [integration] CLOUD.14: final candidate
- [integration] CLOUD.15: final candidate
- [integration] CLOUD.16: final candidate
- [integration] CLOUD.17: final candidate
- [integration] CLOUD.18: final candidate
- [integration] CLOUD.19: final candidate

Permitted write scope: Cloud:artifacts/candidate/**
Unblocks: REL.06

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): real publish-mode auth/session/CSRF/origin/rotation/revocation tests including stale CF requests and browser credential secrecy
Completion evidence for the ledger: owned artifact and real-integration receipt: source commit, producer version, candidate hashes, actual runtime/OS/device/provider, scenario, result, limitations, real-vs-fixture status
Notes: Merged duplicate integration or closure task formerly proposed as CON.94.
```

```text
Execute ArcForges delivery task CLOUD.21 — Public endpoint mapping and validation.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\cloud.md (anchor task-cloud-21).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/cloud-21 (python tools/delivery.py claim CLOUD.21 --worker <name>); task branch task/cloud-21 in Cloud; ledger record ledger/tasks/cloud-21.md.
Kind/size: service/M. Baseline: not-started.
Outcome: Generated proto service methods are registered with exact request/reply/semantic validation from the registry; binary gRPC-Web unary calls and declared server streams go through the same owner handlers; owner mutations and the Sync allowlist are mapped exactly; no ad-hoc REST business API exists.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-23.00 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\23-public-api-and-generated-clients.md, anchor rule-wp-23.00
- WP-22:browser-session-evidence-note-wp-22-08-m Browser-session evidence note (WP-22.08 must pass before WP-23 consumes its contract; a written P2-003 decision alone is insufficient) (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\22-identity-workspace-and-device.md, package-level obligation

Entry condition: adoption slice ADOPT.07.cloud is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [contract] CON.91: the handwritten-proto-generated service/method definitions to register (D-009 authority)
- [artifact] CLOUD.13: session model and native session validation
Completion prerequisites (may start earlier; cannot complete before these are complete):
- [integration] CLOUD.19: the browser cookie-session adapter and native session validation to authenticate requests before they reach a handler

Permitted write scope: Cloud:src/Cloud/ArcForges.Cloud.PublicApi/Endpoints/**
Unblocks: AND.04, CLOUD.22, CLOUD.23, CLOUD.24, CLOUD.25, CLOUD.28, CLOUD.29, CLOUD.64, CLOUD.66, COM.13, SIM.05

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): offline + opt-in tests: each method category through native and TS transport, malformed/unknown request values, denied scope before handler
Completion evidence for the ledger: every selected operation has a concrete typed endpoint and owner; no ad-hoc REST business API
```

```text
Execute ArcForges delivery task CLOUD.22 — Typed protocol and error mapping.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\cloud.md (anchor task-cloud-22).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/cloud-22 (python tools/delivery.py claim CLOUD.22 --worker <name>); task branch task/cloud-22 in Cloud; ledger record ledger/tasks/cloud-22.md.
Kind/size: service/M. Baseline: not-started.
Outcome: Generated ArcResult domain errors and gRPC-Web transport statuses/trailers are mapped exactly under registry 04; ProblemDetails is limited to documented HTTP exceptions.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-23.01 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\23-public-api-and-generated-clients.md, anchor rule-wp-23.01

Entry condition: adoption slice ADOPT.07.cloud is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] CLOUD.21: the endpoint registration to attach error mapping to
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Cloud:src/Cloud/ArcForges.Cloud.PublicApi/Errors/**
Unblocks: CLOUD.26, CLOUD.28, CLOUD.64, CLOUD.66

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): offline + opt-in tests: HTTP200-with-error-trailers, partial frame, 64-bit values, deadline/cancel-after-dispatch, command-receipt reconciliation
Completion evidence for the ledger: every C#/TS/Kotlin client distinguishes transport uncertainty from a domain refusal
```

```text
Execute ArcForges delivery task CLOUD.23 — Typed queries and revision preconditions.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\cloud.md (anchor task-cloud-23).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/cloud-23 (python tools/delivery.py claim CLOUD.23 --worker <name>); task branch task/cloud-23 in Cloud; ledger record ledger/tasks/cloud-23.md.
Kind/size: service/M. Baseline: not-started.
Outcome: Opaque scope-bound PageRequest cursors, registered typed filters and RequestMeta expected-owner-revision preconditions work; no ETag/If-Match for business RPC.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-23.02 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\23-public-api-and-generated-clients.md, anchor rule-wp-23.02

Entry condition: adoption slice ADOPT.07.cloud is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] CLOUD.21: endpoint registration to add query/cursor semantics to
- [contract] CON.91: the frozen notes.scalar.v1 query profile definition
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Cloud:src/Cloud/ArcForges.Cloud.PublicApi/Queries/**
Unblocks: CLOUD.28, COM.06

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): offline + opt-in tests: wrong product/scope cursor, stale revision, page limits, unsupported filter/version, exact scalar vectors
Completion evidence for the ledger: generated clients exercise the authoritative RPC query/revision rules without REST aliases
```

```text
Execute ArcForges delivery task CLOUD.24 — Idempotency and rate limiting.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\cloud.md (anchor task-cloud-24).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/cloud-24 (python tools/delivery.py claim CLOUD.24 --worker <name>); task branch task/cloud-24 in Cloud; ledger record ledger/tasks/cloud-24.md.
Kind/size: service/M. Baseline: not-started.
Outcome: State-changing requests accept a command identity and produce exactly one effect under retry; rate limits apply per identity and per capability class with typed refusals carrying retry guidance.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-23.03 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\23-public-api-and-generated-clients.md, anchor rule-wp-23.03

Entry condition: adoption slice ADOPT.07.cloud is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] CLOUD.21: endpoint registration to enforce idempotency/rate limits on
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Cloud:src/Cloud/ArcForges.Cloud.PublicApi/Idempotency/**
Unblocks: CLOUD.28, COM.03, SIM.05

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): offline + opt-in tests: retry-produces-one-effect at the API boundary, rate-limit tests per class, actionable-guidance test
Completion evidence for the ledger: one command produces one effect at the API boundary; rate limiting refuses with actionable guidance
```

```text
Execute ArcForges delivery task CLOUD.25 — Resource transport schema and future-owner boundary.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\cloud.md (anchor task-cloud-25).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/cloud-25 (python tools/delivery.py claim CLOUD.25 --worker <name>); task branch task/cloud-25 in Cloud; ledger record ledger/tasks/cloud-25.md.
Kind/size: service/M. Baseline: not-started.
Outcome: The complete generated upload/status/ticket/verification/owner-promotion schema and permission/error envelope is registered and exercised through declared protocol fixtures; every endpoint's real owner/fixture/replacement WP is recorded.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-23.04 (full (schema/transport/fixture boundary only; real R2 multipart behavior is WP-25.05)): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\23-public-api-and-generated-clients.md, anchor rule-wp-23.04

Entry condition: adoption slice ADOPT.07.cloud is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] CLOUD.21: endpoint registration to add resource-transport endpoints to
- [artifact] PRF.07: the minimal real R2 transport probe already proved by WP-06
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Cloud:src/Contracts/Public/ArcForges.Contracts.PublicApi.Resource/**; Cloud:fixtures/wire/publicapi/resource/**
Permitted substitutes (never real integration evidence): SUB-resource-transport-schema-fixtures: protocol/schema/permission/error envelope only, via declared fixtures -- release excludes the fixture handlers Real producer ['CLOUD.42']; removed by CLOUD.42
Unblocks: CLOUD.28, CLOUD.42

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): offline + opt-in tests: independent request/result/expiry/hash/denied-scope and encoded-body fixtures across C#/TS/Kotlin
Completion evidence for the ledger: no missing resource schema; no claim that WP-23 alone delivered Resource/R2 owner behavior
```

```text
Execute ArcForges delivery task CLOUD.26 — Generated C#/TypeScript/Kotlin clients against Identity/Workspace/Device.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\cloud.md (anchor task-cloud-26).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/cloud-26 (python tools/delivery.py claim CLOUD.26 --worker <name>); task branch task/cloud-26 in Cloud; ledger record ledger/tasks/cloud-26.md.
Kind/size: service/L. Baseline: not-started.
Outcome: Released C# native, TypeScript gRPC-Web and Kotlin native clients work against actual Identity/Workspace/Device endpoints with native single-flight refresh, Web cookie/CSRF/Origin handling and generation-scoped callbacks outside generated code.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-23.05 (all work except the parts mapped to AND.07, WEB.30): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\23-public-api-and-generated-clients.md, anchor rule-wp-23.05

Entry condition: adoption slice ADOPT.07.cloud is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] CLOUD.19: the real browser cookie-session adapter to test the TS client's cookie/CSRF/Origin handling against
- [artifact] CLOUD.22: typed error mapping to test exact-value/error/header client conformance against
- [artifact] PRF.10: the WP-06 Android probe artifact, explicitly named as the substitute for the future complete Android app
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Cloud:src/BuildingBlocks/ArcForges.CloudClient/**; Cloud:tests/PublicApiContractTests/**
Unblocks: AND.07, CLOUD.27, CLOUD.28, WEB.30

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): offline + opt-in tests: independent exact-value/current-previous-major vectors, actual WP-22 session expiry/revoke/refresh, public/internal leak rejection
Completion evidence for the ledger: three ecosystem clients work against the actual host; owner implementations replaced by WP-25/42/52 before full release
Notes: Gate: PG-23 (this task's client-side contribution; CLOUD.19 contributes the server side).
```

```text
Execute ArcForges delivery task CLOUD.27 — Compatibility window and bidirectional matrix.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\cloud.md (anchor task-cloud-27).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/cloud-27 (python tools/delivery.py claim CLOUD.27 --worker <name>); task branch task/cloud-27 in Cloud; ledger record ledger/tasks/cloud-27.md.
Kind/size: service/M. Baseline: not-started.
Outcome: The supported client window is declared with golden wire vectors per contract version; the compatibility matrix runs both directions (previous client vs current server, current client vs minimum supported server) and catches a deliberately breaking change.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-23.06 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\23-public-api-and-generated-clients.md, anchor rule-wp-23.06

Entry condition: adoption slice ADOPT.07.cloud is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] CLOUD.26: at least one generated client per language to build the matrix against
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Cloud:fixtures/wire/publicapi/**; Cloud:tests/PublicApiContractTests/Compatibility/**
Unblocks: CLOUD.28

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): the bidirectional matrix; a negative test asserting a breaking change fails the matrix
Completion evidence for the ledger: bidirectional compatibility matrix passes and catches a deliberately breaking change
```

```text
Execute ArcForges delivery task CLOUD.28 — Owned-artifact closure and real integration.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\cloud.md (anchor task-cloud-28).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/cloud-28 (python tools/delivery.py claim CLOUD.28 --worker <name>); task branch task/cloud-28 in Cloud; ledger record ledger/tasks/cloud-28.md.
Kind/size: integration/L. Baseline: not-started.
Outcome: Real C#/browser/Kotlin calls succeed against the AOT image with previous/current compatibility and complete operation mapping including auth, files and webhooks outside gRPC.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-23.90 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\23-public-api-and-generated-clients.md, anchor rule-wp-23.90
- WP-23:operator-contract-closure-appendix-cloud Operator contract closure appendix -- Cloud's own share: generate/implement every operation with its eight authorization fields, operator scope and OC-03 role binding, refuse public customer/PAT/agent access, verify distinct approver/stale hash/revision/configuration/role revocation/expiry/concurrent consumption/lost receipt; the financial owners (WP-42), configuration/policy owners (WP-44) and console join (WP-45) are NOT this task's obligation -- see IM.operator-contract-closure (Operator contract closure appendix -- Cloud's own share: generate/implement every operation with its eight authorization fields, operator scope and OC-03 role binding, refuse public customer/PAT/agent access, verify distinct approver/stale hash/revision/configuration/role revocation/expiry/concurrent consumption/lost receipt; the financial owners (WP-42), configuration/policy owners (WP-44) and console join (WP-45) are NOT this task's obligation -- see IM.operator-contract-closure): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\23-public-api-and-generated-clients.md, package-level obligation
- WP-23:browser-matrix-acceptance-appendix-cloud Browser matrix acceptance appendix -- Cloud's own share: prove generated transports support delayed-stream polling, refusal of unavailable required auth/step-up, safe-preview refusal, preserved pending work; WP-45/47/48/49/50's own operations/site/account/chat/production-hash evidence is NOT this task's obligation -- see IM.browser-matrix-acceptance (Browser matrix acceptance appendix -- Cloud's own share: prove generated transports support delayed-stream polling, refusal of unavailable required auth/step-up, safe-preview refusal, preserved pending work; WP-45/47/48/49/50's own operations/site/account/chat/production-hash evidence is NOT this task's obligation -- see IM.browser-matrix-acceptance): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\23-public-api-and-generated-clients.md, package-level obligation
- WP-23:operator-contract-closure-appendix-regis Operator contract closure appendix (registry04 §9 + model01 operator state; eight authorization fields, operator scope, OC-03 role binding) (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\23-public-api-and-generated-clients.md, package-level obligation
- WP-23:browser-matrix-acceptance-appendix-brows Browser matrix acceptance appendix (browser-support.v1, supported/degraded/blocked behavior for generated transports) (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\23-public-api-and-generated-clients.md, package-level obligation

Entry condition: adoption slice ADOPT.07.cloud is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] AND.07: package task delivered
- [artifact] WEB.30: package task delivered
Completion prerequisites (may start earlier; cannot complete before these are complete):
- [integration] CLOUD.21: final candidate
- [integration] CLOUD.22: final candidate
- [integration] CLOUD.23: final candidate
- [integration] CLOUD.24: final candidate
- [integration] CLOUD.25: final candidate
- [integration] CLOUD.26: final candidate
- [integration] CLOUD.27: final candidate

Permitted write scope: Cloud:artifacts/candidate/**
Unblocks: CLOUD.64, REL.06, WEB.31

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): real C#/browser/Kotlin calls against the AOT image, previous/current compatibility, complete operation mapping including auth/files/webhooks outside gRPC
Completion evidence for the ledger: owned artifact and real-integration receipt per WP-23.90
Notes: Gate: PG-23 (joint with CLOUD.19/CLOUD.26).
```

```text
Execute ArcForges delivery task CLOUD.29 — Stream connection and authentication (EventService.Watch/ExecutionService.WatchOutput shells).

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\cloud.md (anchor task-cloud-29).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/cloud-29 (python tools/delivery.py claim CLOUD.29 --worker <name>); task branch task/cloud-29 in Cloud; ledger record ledger/tasks/cloud-29.md.
Kind/size: service/M. Baseline: not-started.
Outcome: Public server-streaming shells for EventService.Watch and ExecutionService.WatchOutput exist with generated StreamFrame, re-authorizing current session/scope every 15s; real C#/browser/Kotlin binary streams work with trailers/cancel/expiry; no WebSocket path.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-24.00 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\24-realtime-and-reliable-events.md, anchor rule-wp-24.00

Entry condition: adoption slice ADOPT.07.cloud is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] CLOUD.21: the endpoint-mapping pattern to register server-streaming methods alongside unary ones
- [artifact] CLOUD.19: session authorization to re-check every 15s on the open stream
- [contract] CON.11: the StreamFrame/StreamPosition/ApplicationScope record definitions (contracts/10 §2)
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Cloud:src/Cloud/ArcForges.Cloud.PublicApi/Streams/**
Unblocks: AND.07, CLOUD.30, CLOUD.34, CLOUD.36, DEV.01, DEV.14, WEB.30

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): opt-in real deployed C#/browser/Kotlin binary stream tests: trailers/cancel/expiry, no WebSocket path
Completion evidence for the ledger: real binary stream trailer/cancel/expiry results
```

```text
Execute ArcForges delivery task CLOUD.30 — Scoped subscription (owner/product/filter/recovery-generation binding).

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\cloud.md (anchor task-cloud-30).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/cloud-30 (python tools/delivery.py claim CLOUD.30 --worker <name>); task branch task/cloud-30 in Cloud; ledger record ledger/tasks/cloud-30.md.
Kind/size: service/M. Baseline: not-started.
Outcome: The feed is bound to owner/product/filter/recovery generation, one events stream plus two output streams per foreground profile; mixed-product/unauthorized feeds are refused; account-security identifiers stay separate.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-24.01 (all work except the parts mapped to DEV.14): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\24-realtime-and-reliable-events.md, anchor rule-wp-24.01

Entry condition: adoption slice ADOPT.07.cloud is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] CLOUD.29: the stream connection/auth shell to bind scope onto
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Cloud:src/Cloud/ArcForges.Cloud.PublicApi/Streams/Scope/**
Unblocks: CLOUD.31, CLOUD.36, DEV.14

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): opt-in tests: mixed-product/unauthorized feed refused
Completion evidence for the ledger: mixed-product/unauthorized refusal and account-security-identifier separation results
```

```text
Execute ArcForges delivery task CLOUD.31 — Cursor and gap handling (DO projection backed by D1 outbox).

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\cloud.md (anchor task-cloud-31).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/cloud-31 (python tools/delivery.py claim CLOUD.31 --worker <name>); task branch task/cloud-31 in Cloud; ledger record ledger/tasks/cloud-31.md.
Kind/size: service/M. Baseline: not-started.
Outcome: Sequence/hash/offset cursors and snapshot high-water recovery work per annex 10; the DO is a projection backed by the D1 outbox, never a second business authority.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-24.02 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\24-realtime-and-reliable-events.md, anchor rule-wp-24.02

Entry condition: adoption slice ADOPT.07.cloud is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] CLOUD.30: scoped subscription to attach cursor semantics to
- [artifact] CLOUD.04: the committed D1 outbox to project from
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Cloud:src/Cloud/ArcForges.Cloud.EventFeed/**
Unblocks: CLOUD.32, CLOUD.33, CLOUD.36, CLOUD.39, DEV.14

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): opt-in tests: duplicate/conflicting frames, expired cursor, deleted DO, revision replay
Completion evidence for the ledger: duplicate/conflicting-frame, expired-cursor, deleted-DO and revision-replay results
```

```text
Execute ArcForges delivery task CLOUD.32 — Durable unary fallback (Poll/readOutput).

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\cloud.md (anchor task-cloud-32).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/cloud-32 (python tools/delivery.py claim CLOUD.32 --worker <name>); task branch task/cloud-32 in Cloud; ledger record ledger/tasks/cloud-32.md.
Kind/size: service/S. Baseline: not-started.
Outcome: Poll/readOutput works with the same owner/cursor profile as the stream, replacing the old HTTP task-stream endpoint; a blocked stream recovers through a real unary read without inventing completion.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-24.03 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\24-realtime-and-reliable-events.md, anchor rule-wp-24.03

Entry condition: adoption slice ADOPT.07.cloud is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] CLOUD.31: cursor/gap handling to read from in the unary fallback
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Cloud:src/Cloud/ArcForges.Cloud.PublicApi/Streams/Fallback/**
Unblocks: CLOUD.36

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): opt-in test: blocked stream recovers through real unary read without invented completion
Completion evidence for the ledger: blocked-stream real-recovery result
Notes: AI terminal bodies (ChatTurn/Task execution output) arrive via WP-52, not this task.
```

```text
Execute ArcForges delivery task CLOUD.33 — Publication and wake (D1 outbox to bounded DO feed via Queues).

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\cloud.md (anchor task-cloud-33).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/cloud-33 (python tools/delivery.py claim CLOUD.33 --worker <name>); task branch task/cloud-33 in Cloud; ledger record ledger/tasks/cloud-33.md.
Kind/size: service/M. Baseline: not-started.
Outcome: The committed D1 outbox publishes into the bounded DO feed with wake hints delivered via Queues; contiguous watermark, no skipped commit, duplicate queue event is safe; no business ownership lives in the DO.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-24.04 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\24-realtime-and-reliable-events.md, anchor rule-wp-24.04

Entry condition: adoption slice ADOPT.07.cloud is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] CLOUD.31: the DO projection to publish into
- [artifact] CLOUD.05: the finite-durable-job/Queue wake mechanism
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Cloud:src/Cloud/ArcForges.Cloud.EventFeed/Publisher/**
Shared resources (follow the owner protocol): RES-cloud-leased-singletons (append): Each publication watermark, Durable Object alarm namespace and R2 prefix has exactly one owning module task; others use its published port; names are reserved in the binding plan before first use.
Unblocks: CLOUD.35, CLOUD.36, DEV.14

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): opt-in tests: contiguous watermark, no skipped commit, duplicate queue event safe
Completion evidence for the ledger: contiguous-watermark and duplicate-safety results
```

```text
Execute ArcForges delivery task CLOUD.34 — Bounded stream lifecycle.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\cloud.md (anchor task-cloud-34).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/cloud-34 (python tools/delivery.py claim CLOUD.34 --worker <name>); task branch task/cloud-34 in Cloud; ledger record ledger/tasks/cloud-34.md.
Kind/size: service/S. Baseline: not-started.
Outcome: 5-minute stream, 15s heartbeat, 45s silence and bounded jitter/queue limits are enforced; Android background closes streams and later refetches; slow-reader overflow resets rather than growing unbounded.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-24.05 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\24-realtime-and-reliable-events.md, anchor rule-wp-24.05

Entry condition: adoption slice ADOPT.07.cloud is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] CLOUD.29: the stream shell to bound the lifecycle of
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Cloud:src/Cloud/ArcForges.Cloud.PublicApi/Streams/Lifecycle/**
Unblocks: CLOUD.35, CLOUD.36, DEV.14

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): opt-in test: slow reader overflow resets, no unbounded memory or hibernation-cost claim
Completion evidence for the ledger: slow-reader overflow-reset result
```

```text
Execute ArcForges delivery task CLOUD.35 — Reusable stream consumer adapters.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\cloud.md (anchor task-cloud-35).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/cloud-35 (python tools/delivery.py claim CLOUD.35 --worker <name>); task branch task/cloud-35 in Cloud; ledger record ledger/tasks/cloud-35.md.
Kind/size: service/M. Baseline: not-started.
Outcome: Platform Cloud.Client and Contracts TS/Kotlin stream fixtures are published with typed lifecycle states and no UI-specific transport logic.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-24.06 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\24-realtime-and-reliable-events.md, anchor rule-wp-24.06

Entry condition: adoption slice ADOPT.07.cloud is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] CLOUD.33: the real publication/wake mechanism to expose through the reusable adapter
- [artifact] CLOUD.34: bounded lifecycle semantics to expose as typed lifecycle states
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:src/BuildingBlocks/ArcForges.CloudClient/Streams/**; Cloud:fixtures/wire/streams/**
Shared resources (follow the owner protocol): RES-assistant-store-schema (append): Numbered migrations are allocated at merge by the integration owner (a rebase renumbers pending migrations); each migration is forward-only with its recovery and downgrade-refusal tests; no task edits a merged migration.
Unblocks: CLOUD.36

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): opt-in tests: clean generated-client consumers and real deployed C# ownership paths
Completion evidence for the ledger: clean-consumer and real-ownership-path results
```

```text
Execute ArcForges delivery task CLOUD.36 — Owned-artifact closure and real integration (tool-result acceptance).

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\cloud.md (anchor task-cloud-36).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/cloud-36 (python tools/delivery.py claim CLOUD.36 --worker <name>); task branch task/cloud-36 in Cloud; ledger record ledger/tasks/cloud-36.md.
Kind/size: integration/M. Baseline: not-started.
Outcome: Every WP-24 substep is complete and packaged; two distinct toolRequestIds in one attempt both persist and replay correctly for both Task and ChatTurn owners; a changed result under the same (toolRequestId, attemptId, commandId) refuses.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-24.90 (full, including the Tool-result acceptance subsection (toolRequestId dedup for Task and ChatTurn owners, command.reused_identifier refusal, wire registry + TK-05 + task.tool_result binding)): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\24-realtime-and-reliable-events.md, anchor rule-wp-24.90

Entry condition: adoption slice ADOPT.07.cloud is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] DEV.14: package task delivered
Completion prerequisites (may start earlier; cannot complete before these are complete):
- [integration] CLOUD.29: final candidate
- [integration] CLOUD.30: final candidate
- [integration] CLOUD.31: final candidate
- [integration] CLOUD.32: final candidate
- [integration] CLOUD.33: final candidate
- [integration] CLOUD.34: final candidate
- [integration] CLOUD.35: final candidate
- [integration] DEV.12: a real Task owner to exercise the tool-result dedup vector against

Permitted write scope: Cloud:artifacts/candidate/**
Unblocks: REL.06

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): package/contract/owner/version compatibility, failure/recovery, real boundaries
Completion evidence for the ledger: owned artifact and real-integration receipt per WP-24.90
```

```text
Execute ArcForges delivery task CLOUD.37 — Cloud Notes authority and sync scopes.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\cloud.md (anchor task-cloud-37).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/cloud-37 (python tools/delivery.py claim CLOUD.37 --worker <name>); task branch task/cloud-37 in Cloud; ledger record ledger/tasks/cloud-37.md.
Kind/size: service/L. Baseline: not-started.
Outcome: The canonical notes schema (notebook-owned folders, document-owned blocks/values, tags, property definitions, saved views, immutable revisions, checkpoints, derived backlinks) exists with typed folder/document/history operations and sorted-root revision checks; Cloud validates the same typed operations as the local domain.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-25.00 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\25-sync-engine-and-blob-lifecycle.md, anchor rule-wp-25.00
- WP-21.00 (real Sync owner transaction implementation): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\21-cloud-host-and-persistence.md, anchor rule-wp-21.00

Entry condition: adoption slice ADOPT.07.cloud is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] CLOUD.03: D1 physical mapping/migration runner for notes.* tables
- [artifact] CLOUD.06: the shared atomic family engine, since synced content mutation is a named shared-transaction family
- [contract] CON.91: published Notes owner-body records (documents, blocks, properties) in the foundation closure
- [contract] CON.20: published NotesService operations
- [artifact] CON.03: real, delivered outcome of CON.03 (Resource/Sync owner-body admission: closed Sync mutation allowlist + cross-owner/wrong-revision/opaque-object/forbidden-path negatives)
- [artifact] CON.09: real, delivered outcome of CON.09 (Sync/resource-transfer/objects operation registry + realm-transfer.v1)
- [artifact] CLOUD.01: real, delivered outcome of CLOUD.01 (Ingress and host pipeline)
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Cloud:src/Cloud/ArcForges.Cloud.Modules.Notes/**
Shared resources (follow the owner protocol): RES-cloud-d1-migrations (append): One global D1 migration sequence: each module task authors migrations under its module prefix; the integration owner assigns the global sequence number at merge, regenerates the plan manifest and rejects edits to merged migrations; the migrator applies in sequence with receipts.; RES-cloud-storage-plans (append): Each module owns its own plan directory; the plan-manifest hash is regenerated by the author after rebase and checked in CI.; RES-shared-transaction-families (append): Adding a participant to a shared atomic family is a design change through the Architecture Owner; module tasks implement only their declared participation.
Unblocks: CLOUD.10, CLOUD.39, CLOUD.45, CLOUD.47, NOTES.01, NOTES.34, NOTES.35, SRCH.00

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): offline + opt-in real-D1 tests: folder cycle/reorder/reparent, cross-notebook move with stable document IDs, concurrent move/delete, ancestor trash/restore, stale revisions, immutable history, revision/attachment pins; verify generated API/SQLite projections against real D1
Completion evidence for the ledger: one complete server authority model and hierarchy, executable operations, history and resource ownership; no client required to create authoritative schema or assign Cloud revisions
Notes: Merged duplicate integration or closure task formerly proposed as CON.95.
```

```text
Execute ArcForges delivery task CLOUD.38 — Client outbox and conflict lineage (desktop data model).

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\cloud.md (anchor task-cloud-38).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/cloud-38 (python tools/delivery.py claim CLOUD.38 --worker <name>); task branch task/cloud-38 in DesktopPlatform; ledger record ledger/tasks/cloud-38.md.
Kind/size: service/L. Baseline: not-started.
Outcome: The single sync_outbox schema exists client-side: acked shadow plus pending journal, frozen batch hash/revision/range, explicit supersession lineage; a user conflict resolution appends a new local event and never edits the frozen failed batch.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-25.01 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\25-sync-engine-and-blob-lifecycle.md, anchor rule-wp-25.01

Entry condition: adoption slice ADOPT.02.cloud is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] PLT.01: the local store journal/single-writer persistence foundation
Completion prerequisites (may start earlier; cannot complete before these are complete):
- [integration] CLOUD.39: the real guarded publication/bootstrap mechanism to submit batches against for a genuine end-to-end proof

Permitted write scope: DesktopPlatform:src/BuildingBlocks/ArcForges.Sync/**
Shared resources (follow the owner protocol): RES-assistant-store-schema (append): Numbered migrations are allocated at merge by the integration owner (a rebase renumbers pending migrations); each migration is forward-only with its recovery and downgrade-refusal tests; no task edits a merged migration.
Unblocks: CLOUD.40, CLOUD.44, CLOUD.47, NOTES.35

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): offline + opt-in tests: edit during dispatch, conflict followed by keep-local/keep-Cloud/merge, dependent undispatched batches, crash at each resolution write, late old receipt, own-origin feed echo
Completion evidence for the ledger: every local edit has a durable outcome and exactly one live submission lineage; no conflict silently drops pending content
Notes: Cross-repo: WP-25 names this project explicitly in its own §4 table despite living in DesktopPlatform.
```

```text
Execute ArcForges delivery task CLOUD.39 — Guarded publication and convergent bootstrap.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\cloud.md (anchor task-cloud-39).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/cloud-39 (python tools/delivery.py claim CLOUD.39 --worker <name>); task branch task/cloud-39 in Cloud; ledger record ledger/tasks/cloud-39.md.
Kind/size: service/L. Baseline: not-started.
Outcome: Model-04's primary lower-bound W bootstrap, immutable-key pages, retention pin and replay-to-H work; the publisher guards watermark/fence/selected rows in one D1 batch; real D1 clients converge without PostgreSQL snapshot/locks or lost pending work.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-25.02 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\25-sync-engine-and-blob-lifecycle.md, anchor rule-wp-25.02

Entry condition: adoption slice ADOPT.07.cloud is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] CLOUD.37: the canonical notes schema to publish changes from
- [artifact] CLOUD.04: the generic receipts/outbox mechanism this publisher reads committed-unpublished rows from
- [artifact] CLOUD.31: WP-24's cursor/gap-handling concept, since this publisher and the realtime DO feed are related but distinct publication mechanisms consumers must not conflate
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Cloud:src/Cloud/ArcForges.Cloud.Modules.Sync/Publisher/**
Shared resources (follow the owner protocol): RES-cloud-leased-singletons (append): Each publication watermark, Durable Object alarm namespace and R2 prefix has exactly one owning module task; others use its published port; names are reserved in the binding plan before first use.
Unblocks: AND.07, CLOUD.38, CLOUD.40, CLOUD.41, CLOUD.43, CLOUD.47, NOTES.35, SCOPE.27, SLATE.42

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): opt-in real-D1 tests: two-writer interleavings, commit between pages, insert below cursor, delete/tombstone, expired pin, lost acknowledgement, old/new revision application with pending edits
Completion evidence for the ledger: real D1 clients converge without PostgreSQL snapshot/locks or lost pending work
Notes: Early risk proof: this is the two-writer D1 guarded-batch algorithm underlying PG-17. Proving it under contention before WP-25.03-07 build on top avoids invalidating that downstream work. PG-17 explicitly 'consumes the publisher from package 21' (CLOUD.04/CLOUD.06) -- this task is where that consumption happens for Notes/Sync specifically.
```

```text
Execute ArcForges delivery task CLOUD.40 — Conflict detection and five resolution policies.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\cloud.md (anchor task-cloud-40).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/cloud-40 (python tools/delivery.py claim CLOUD.40 --worker <name>); task branch task/cloud-40 in Cloud; ledger record ledger/tasks/cloud-40.md.
Kind/size: service/M. Baseline: not-started.
Outcome: Conflicts are detected by revision, never timestamp; five policies are implemented per the architecture, chosen per scope and object kind; discarded versions remain recoverable; user-facing conflicts present both versions intelligibly.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-25.03 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\25-sync-engine-and-blob-lifecycle.md, anchor rule-wp-25.03

Entry condition: adoption slice ADOPT.07.cloud is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] CLOUD.38: the client outbox/conflict lineage to detect conflicts against
- [artifact] CLOUD.39: the guarded publication mechanism, since conflicts are detected during publication
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Cloud:src/Cloud/ArcForges.Cloud.Modules.Sync/Conflict/**
Unblocks: CLOUD.44, CLOUD.47, NOTES.35

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): offline + opt-in tests: conflict matrix across object kinds and policies, recoverability test for every discard, user-facing presentation test
Completion evidence for the ledger: every conflict path covered, every discarded version recoverable, user-facing conflicts present both versions
```

```text
Execute ArcForges delivery task CLOUD.41 — Deletion and tombstones.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\cloud.md (anchor task-cloud-41).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/cloud-41 (python tools/delivery.py claim CLOUD.41 --worker <name>); task branch task/cloud-41 in Cloud; ledger record ledger/tasks/cloud-41.md.
Kind/size: service/M. Baseline: not-started.
Outcome: Deletion propagates through tombstones with defined retention; an offline-beyond-retention device resolves deterministically rather than silently resurrecting content; local deletion, cloud deletion and unsync are distinguished.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-25.04 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\25-sync-engine-and-blob-lifecycle.md, anchor rule-wp-25.04

Entry condition: adoption slice ADOPT.07.cloud is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] CLOUD.39: the change feed/publication mechanism to propagate tombstones through
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Cloud:src/Cloud/ArcForges.Cloud.Modules.Sync/Tombstones/**
Unblocks: CLOUD.44, CLOUD.47, NOTES.35

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): offline + opt-in tests: offline-beyond-retention convergence, resurrection-prevention test, three-way delete-action distinction test
Completion evidence for the ledger: deleted content never silently resurrects; the three delete-like actions are distinguishable
```

```text
Execute ArcForges delivery task CLOUD.42 — Blob lifecycle (real R2 staged/verified/committed).

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\cloud.md (anchor task-cloud-42).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/cloud-42 (python tools/delivery.py claim CLOUD.42 --worker <name>); task branch task/cloud-42 in Cloud; ledger record ledger/tasks/cloud-42.md.
Kind/size: service/L. Baseline: not-started.
Outcome: Upload happens through a server-issued session, chunked and checksummed, moving Staged -> Verified -> Committed; a reference is only published after commit; orphan cleanup removes uncommitted staging without touching committed data; storage accounting is computed from committed objects.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-25.05 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\25-sync-engine-and-blob-lifecycle.md, anchor rule-wp-25.05

Entry condition: adoption slice ADOPT.07.cloud is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] CLOUD.01: the deployed Worker's R2 bucket binding and job-authorized object port (contracts/05 §9 job-grant/job-authorize)
- [artifact] CLOUD.06: the shared atomic family engine, since resource upload lifecycle is a named shared-transaction family
- [artifact] CLOUD.25: the resource transport schema this task replaces the fixture for
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Cloud:src/Cloud/ArcForges.Cloud.Modules.Resource/**
Shared resources (follow the owner protocol): RES-cloud-d1-migrations (append): One global D1 migration sequence: each module task authors migrations under its module prefix; the integration owner assigns the global sequence number at merge, regenerates the plan manifest and rejects edits to merged migrations; the migrator applies in sequence with receipts.; RES-cloud-storage-plans (append): Each module owns its own plan directory; the plan-manifest hash is regenerated by the author after rebase and checked in CI.; RES-shared-transaction-families (append): Adding a participant to a shared atomic family is a design change through the Architecture Owner; module tasks implement only their declared participation.
Unblocks: AND.07, CLOUD.43, CLOUD.44, CLOUD.45, CLOUD.46, CLOUD.47, CLOUD.48, EXT.06, NOTES.35, SCOPE.23, SIM.04, WEB.13

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): opt-in real-R2 tests: interrupted-upload resumption, verification-failure path, orphan-cleanup safety test, accounting comparison against actual committed storage
Completion evidence for the ledger: no reference published before commit; orphan cleanup never touches committed data; accounting matches committed storage
Notes: Must-be-real-early per implementation-sequence §3 ('Object storage adapters' may be mocked only at the schema/protocol layer -- 'Upload interruption, hashing, resumption and quota' must be real). Keep this must-be-real-early placement; do not defer real R2 behind fixture evidence.
```

```text
Execute ArcForges delivery task CLOUD.43 — Availability, protection, data-health signals and realm-transfer workflow.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\cloud.md (anchor task-cloud-43).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/cloud-43 (python tools/delivery.py claim CLOUD.43 --worker <name>); task branch task/cloud-43 in Cloud; ledger record ledger/tasks/cloud-43.md.
Kind/size: service/L. Baseline: not-started.
Outcome: Hydration/cache pause is distinguished from explicit Cloud deletion; source-consent/transient inputs and health states exist; the full realm-transfer export/preview/commit/status/cancel workflow works from client journeys; missing-object outcomes are rebuilt or verified with irrecoverable data retaining evidence and recovery/export actions.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-25.06 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\25-sync-engine-and-blob-lifecycle.md, anchor rule-wp-25.06

Entry condition: adoption slice ADOPT.07.cloud is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] CLOUD.42: the real blob lifecycle to verify object availability against
- [artifact] CLOUD.39: the sync change feed for the realm-transfer workflow's status/commit steps
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Cloud:src/Cloud/ArcForges.Cloud.Modules.Sync/Health/**; Cloud:src/Cloud/ArcForges.Cloud.Modules.Resource/RealmTransfer/**
Unblocks: CLOUD.47

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): opt-in real-R2/D1 tests: resume after 100-root batch, repeated command, missing object, partial cancellation, denied current scope, transfer credential/ledger exclusion, restore generation
Completion evidence for the ledger: no Unsync deletion of authoritative Notes/Chat, no empty success for irrecoverable data, no manual migration rule invented
Notes: POSSIBLE DESIGN OVERLAP: this task's 'full realm-transfer export/preview/commit/status/cancel workflow from client journeys' (WP-25.06) reads very close to WP-46.05's 'existing explicit realm export/import semantics using compatible D1 physical/schema/plan manifests' (CLOUD.53). They may be genuinely different (user-facing personal-data export vs operator-level realm-to-realm database migration) or may be the same feature described twice.
```

```text
Execute ArcForges delivery task CLOUD.44 — Multi-device convergence harness.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\cloud.md (anchor task-cloud-44).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/cloud-44 (python tools/delivery.py claim CLOUD.44 --worker <name>); task branch task/cloud-44 in Cloud; ledger record ledger/tasks/cloud-44.md.
Kind/size: integration/L. Baseline: not-started.
Outcome: Three devices editing concurrently, one offline for an extended period, converge to verifiably identical state under concurrent edits, attachments, deletions and a mid-sync crash, verified by comparison not absence of errors.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-25.07 (all work except the parts mapped to NOTES.35): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\25-sync-engine-and-blob-lifecycle.md, anchor rule-wp-25.07

Entry condition: adoption slice ADOPT.07.cloud is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- none
Completion prerequisites (may start earlier; cannot complete before these are complete):
- [integration] CLOUD.38: real client outbox
- [integration] CLOUD.40: real conflict policies
- [integration] CLOUD.41: real tombstones
- [integration] CLOUD.42: real blob lifecycle
- [integration] NOTES.37: a real ArcNotes client to run the three-device harness against

Permitted write scope: Cloud:tests/SyncConflictTests/Convergence/**
Unblocks: CLOUD.47, NOTES.35, SCOPE.27, SLATE.42

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): a three-device convergence harness with concurrent edits, an extended offline device, attachments, deletions and a mid-sync crash
Completion evidence for the ledger: three devices converge to verifiably identical state
Notes: Gate: PG-17 (joint with CLOUD.39). This is the full end-to-end demonstration; CLOUD.39 is where the underlying algorithm risk is retired early.
```

```text
Execute ArcForges delivery task CLOUD.45 — Real Cloud Notes and Chat export producers.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\cloud.md (anchor task-cloud-45).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/cloud-45 (python tools/delivery.py claim CLOUD.45 --worker <name>); task branch task/cloud-45 in Cloud; ledger record ledger/tasks/cloud-45.md.
Kind/size: service/L. Baseline: not-started.
Outcome: Bounded leased Cloud export jobs freeze an acknowledged revision manifest, pin content/history/attachment objects, generate Markdown/JSON/text outputs with metadata/link map and fidelity report, and publish a verified expiring download artifact; device-only pending edits are excluded.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-25.08 (all work except the parts mapped to AST.21, CLOUD.58, NOTES.33): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\25-sync-engine-and-blob-lifecycle.md, anchor rule-wp-25.08

Entry condition: adoption slice ADOPT.07.cloud is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] CLOUD.37: the canonical notes schema to snapshot for export
- [artifact] CLOUD.42: real R2 staging/verification for the export bundle
- [artifact] CLOUD.05: the finite-durable-job mechanism, since exports are bounded leased jobs
- [contract] CON.20: published notes.requestExport records
- [contract] CON.22: published export and data operations
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Cloud:src/Cloud/ArcForges.Cloud.Modules.Notes/Export/**; Cloud:src/Cloud/ArcForges.Cloud.Jobs/Export/**
Unblocks: AST.21, CLOUD.47, CLOUD.58, NOTES.20, NOTES.33, WEB.15

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): opt-in real host/database/object-store tests: concurrent edits, notebook moves, deleted attachments, quota limit, expiry, restart, cancellation, paid-term end; compare every delivered manifest/hash and omission; scan for secrets
Completion evidence for the ledger: both export exit paths work against real Cloud authority, preserve a stable snapshot and honest fidelity, release pins/reservations on all terminal paths
Notes: This is the CLOUD-side producer for PG-07's Notes/Chat portion. See integration_proposals: IM.notes-chat-export-fixture-removal, which structurally asserts removal of the WP-15.06/WP-19.05 fixture endpoints owned by the assistant lanes/the ArcNotes lane.
```

```text
Execute ArcForges delivery task CLOUD.46 — Application Cloud history and restartable import.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\cloud.md (anchor task-cloud-46).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/cloud-46 (python tools/delivery.py claim CLOUD.46 --worker <name>); task branch task/cloud-46 in Cloud; ledger record ledger/tasks/cloud-46.md.
Kind/size: service/M. Baseline: not-started.
Outcome: HistoryService.BeginImport/FinalizeImport/GetImport/CancelImport work per annex 10 with fixed product scope, verified staged archive/typed rows and atomic visibility/receipt; local-only history bodies never enter Cloud Chat or search without explicit promotion.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-25.09 (all work except the parts mapped to AST.22): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\25-sync-engine-and-blob-lifecycle.md, anchor rule-wp-25.09

Entry condition: adoption slice ADOPT.07.cloud is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] CLOUD.42: real R2 staged-archive verification for imported history bodies
- [artifact] CLOUD.06: the shared atomic family engine for atomic visibility/receipt
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Cloud:src/Cloud/ArcForges.Cloud.Modules.*/History/**
Unblocks: AST.22, CLOUD.47

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): opt-in real tests: actual archive/manifest hashes, staged object authorization, parent/branch mapping, lost finalization acknowledgement, duplicate import, source edit during promotion, quota/permission loss, expiry
Completion evidence for the ledger: clean published desktop/Kotlin/TS consumers recover a real interrupted import, see no partial visible conversation, keep local/Cloud/temporary retention distinct
Notes: Replaces the HistoryService fixture consumed by WP-15/WP-17. See integration_proposals: IM.assistant-history-real-integration.
```

```text
Execute ArcForges delivery task CLOUD.47 — Owned-artifact closure and real integration.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\cloud.md (anchor task-cloud-47).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/cloud-47 (python tools/delivery.py claim CLOUD.47 --worker <name>); task branch task/cloud-47 in Cloud; ledger record ledger/tasks/cloud-47.md.
Kind/size: integration/M. Baseline: not-started.
Outcome: R2 is used for the existing upload admission, multipart resume, Verified pin, owner promotion, quota and release lifecycle; outbox/inbox/tombstones/conflicts/bootstrap/unknown-field behavior and export protocol are retained; three-device convergence and interrupted-upload/failed-content-commit/orphan/delete cases run against actual provider adapters.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-25.90 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\25-sync-engine-and-blob-lifecycle.md, anchor rule-wp-25.90
- WP-25:required-implementation-and-closure-from Required implementation and closure from the final review (01-cloud-data-model verification; real structural move/ack/conflict transactions, full native metadata replicas, job-authorized R2 staging/verification/promotion, quarantined old-generation client commands) (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\25-sync-engine-and-blob-lifecycle.md, package-level obligation

Entry condition: adoption slice ADOPT.07.cloud is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] AST.21: package task delivered
- [artifact] AST.22: package task delivered
- [artifact] CLOUD.58: package task delivered
- [artifact] NOTES.33: package task delivered
- [artifact] NOTES.35: package task delivered
Completion prerequisites (may start earlier; cannot complete before these are complete):
- [integration] CLOUD.37: final candidate
- [integration] CLOUD.38: final candidate
- [integration] CLOUD.39: final candidate
- [integration] CLOUD.40: final candidate
- [integration] CLOUD.41: final candidate
- [integration] CLOUD.42: final candidate
- [integration] CLOUD.43: final candidate
- [integration] CLOUD.44: final candidate
- [integration] CLOUD.45: final candidate; WP-25.08 must be represented in this task's own evidence and completion gate per the WP text, not treated as optional
- [integration] CLOUD.46: final candidate

Permitted write scope: Cloud:artifacts/candidate/**
Unblocks: REL.06

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): three-device convergence and interrupted-upload/failed-content-commit/orphan/delete cases against actual provider adapters
Completion evidence for the ledger: owned artifact and real-integration receipt per WP-25.90
```

```text
Execute ArcForges delivery task CLOUD.48 — D1 and independent object backup.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\cloud.md (anchor task-cloud-48).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/cloud-48 (python tools/delivery.py claim CLOUD.48 --worker <name>); task branch task/cloud-48 in Cloud; ledger record ledger/tasks/cloud-48.md.
Kind/size: service/L. Baseline: not-started.
Outcome: Model-04/backup-manifest-v1 works: matching D1 export/bookmark/base sequence, contiguous replay, verified R2 inventory and an independent S3-COMPLIANCE copy; no PostgreSQL WAL/LSN procedure; measured metadata/blob RPO and RTO pass; Time Travel alone cannot satisfy independent restore.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-46.00 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\46-backup-recovery-and-data-health.md, anchor rule-wp-46.00

Entry condition: adoption slice ADOPT.07.cloud is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] CLOUD.03: the D1 physical schema/migration runner to export a matching bookmark/base sequence for
- [artifact] CLOUD.42: real committed R2 objects to inventory and copy independently
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Cloud:src/Cloud/ArcForges.Cloud.Backup/**
Shared resources (follow the owner protocol): RES-cloud-d1-migrations (append): One global D1 migration sequence: each module task authors migrations under its module prefix; the integration owner assigns the global sequence number at merge, regenerates the plan manifest and rejects edits to merged migrations; the migrator applies in sequence with receipts.
Unblocks: CLOUD.49, CLOUD.52, CLOUD.53, CLOUD.54, CLOUD.55

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): opt-in real tests: fresh database import, missing replay gap/hash/key, restrictive journal replay, session/generation reset, reconciled unknown effects; include selfhost.v1 account
Completion evidence for the ledger: measured metadata/blob RPO and RTO; Time Travel alone cannot satisfy independent restore
```

```text
Execute ArcForges delivery task CLOUD.49 — Point-in-time and fresh restore.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\cloud.md (anchor task-cloud-49).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/cloud-49 (python tools/delivery.py claim CLOUD.49 --worker <name>); task branch task/cloud-49 in Cloud; ledger record ledger/tasks/cloud-49.md.
Kind/size: service/M. Baseline: not-started.
Outcome: Base bookmark/sequence and contiguous after-image archive are verified; in-place Time Travel and fresh import/replay both use generation fences.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-46.01 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\46-backup-recovery-and-data-health.md, anchor rule-wp-46.01

Entry condition: adoption slice ADOPT.07.cloud is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] CLOUD.48: the backup manifest/archive to restore from
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Cloud:src/Cloud/ArcForges.Cloud.Backup/Restore/**
Unblocks: CLOUD.50, CLOUD.55

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): opt-in real tests: missing archive/object, partial export, unsafe reopen refusal
Completion evidence for the ledger: missing-archive/object and unsafe-reopen refusal results
```

```text
Execute ArcForges delivery task CLOUD.50 — Fresh environment rebuild.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\cloud.md (anchor task-cloud-50).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/cloud-50 (python tools/delivery.py claim CLOUD.50 --worker <name>); task branch task/cloud-50 in Cloud; ledger record ledger/tasks/cloud-50.md.
Kind/size: service/M. Baseline: not-started.
Outcome: Old ingress/keys are fenced, D1/R2 are restored, the independent restrictive safety journal replays, credentials/leases/cursors are invalidated, external effects are reconciled; a deleted/revoked account cannot reappear and an absent attempt cannot execute twice.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-46.02 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\46-backup-recovery-and-data-health.md, anchor rule-wp-46.02

Entry condition: adoption slice ADOPT.07.cloud is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] CLOUD.49: point-in-time restore to rebuild from
- [artifact] CLOUD.17: the recovery/account-states/deletion model, since a deleted/revoked account must not reappear after rebuild
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Cloud:src/Cloud/ArcForges.Cloud.Backup/Rebuild/**
Unblocks: CLOUD.51, CLOUD.55

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): opt-in real tests: deleted/revoked account cannot reappear, absent attempt cannot execute twice
Completion evidence for the ledger: deleted-account and absent-attempt-no-double-execution results
```

```text
Execute ArcForges delivery task CLOUD.51 — Disaster-recovery drill programme.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\cloud.md (anchor task-cloud-51).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/cloud-51 (python tools/delivery.py claim CLOUD.51 --worker <name>); task branch task/cloud-51 in Cloud; ledger record ledger/tasks/cloud-51.md.
Kind/size: integration/M. Baseline: not-started.
Outcome: An actual Container/Worker/DO/R2/D1 restore runs using separate credentials and an immutable archive with RTO<=4h real evidence, not a SQLite/simulator-only restore.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-46.03 (Cloud-side drill: real Container/Worker/DO/R2/D1 restore using separate credentials and immutable archive, RTO<=4h. The combined AI reopen portion is a joint step with the AI lanes/the governance and release lanes -- see IM.dr-drill-combined-ai-reopen): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\46-backup-recovery-and-data-health.md, anchor rule-wp-46.03

Entry condition: adoption slice ADOPT.07.cloud is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] CLOUD.50: the fresh environment rebuild mechanism to drill
Completion prerequisites (may start earlier; cannot complete before these are complete):
- [integration] CLOUD.67: AI reopen after the Cloud-side restore, per WP-46's own text 'then combined AI reopen at 50/52'

Permitted write scope: Cloud:tests/DrillTests/**
Unblocks: CLOUD.55, CLOUD.67, OPS.03, REL.06

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): RTO<=4h with real evidence, not SQLite/simulator-only restore
Completion evidence for the ledger: real RTO<=4h evidence
```

```text
Execute ArcForges delivery task CLOUD.52 — Data health read projection.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\cloud.md (anchor task-cloud-52).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/cloud-52 (python tools/delivery.py claim CLOUD.52 --worker <name>); task branch task/cloud-52 in Cloud; ledger record ledger/tasks/cloud-52.md.
Kind/size: service/S. Baseline: not-started.
Outcome: Archive watermark, capacity, canonical refs/hash/pins, derived-rebuild state and backup lag/admission state are exposed as a queryable read projection, with 4min/12min warning guards and exceeded-objective incidents made visible.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-46.04 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\46-backup-recovery-and-data-health.md, anchor rule-wp-46.04

Entry condition: adoption slice ADOPT.07.cloud is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] CLOUD.48: the real D1/object backup mechanism producing watermark/lag/inventory numbers to project
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Cloud:src/Cloud/ArcForges.Cloud.Modules.*/DataHealth/**
Unblocks: CLOUD.55, WEB.13

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): opt-in tests: 4min/12min warning guard, exceeded-objective incident visible
Completion evidence for the ledger: warning-guard and exceeded-objective-visibility results
Notes: DELIBERATELY separable from CLOUD.49/50/51 (point-in-time restore, fresh rebuild, drill programme): this task's start edge is only on CLOUD.48 (real backup producing real numbers), not on the full restore/rebuild/drill machinery. This lets the Account portal (WP-48, the Web and Android lanes) consume the data-health projection without waiting for all of WP-46's recovery work to close -- per this area's assignment, keep this separation explicit and do not fold CLOUD.52 into a bundled WP-46 restore task.
```

```text
Execute ArcForges delivery task CLOUD.53 — Export and realm migration.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\cloud.md (anchor task-cloud-53).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/cloud-53 (python tools/delivery.py claim CLOUD.53 --worker <name>); task branch task/cloud-53 in Cloud; ledger record ledger/tasks/cloud-53.md.
Kind/size: service/M. Baseline: not-started.
Outcome: Explicit realm export/import semantics work using compatible D1 physical/schema/plan manifests; no automatic cross-DB transaction; identity/resource/history scope is preserved and unsupported mapping is refused.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-46.05 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\46-backup-recovery-and-data-health.md, anchor rule-wp-46.05

Entry condition: adoption slice ADOPT.07.cloud is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] CLOUD.48: the backup manifest format to reuse for realm export/import
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Cloud:src/Cloud/ArcForges.Cloud.Backup/RealmMigration/**
Shared resources (follow the owner protocol): RES-shared-transaction-families (append): Adding a participant to a shared atomic family is a design change through the Architecture Owner; module tasks implement only their declared participation.
Unblocks: CLOUD.55

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): opt-in real tests: identity/resource/history scope preserved, unsupported mapping refused
Completion evidence for the ledger: scope-preservation and unsupported-mapping-refusal results
Notes: POSSIBLE DESIGN OVERLAP with CLOUD.43 (WP-25.06 realm-transfer workflow) -- see that task's notes.
```

```text
Execute ArcForges delivery task CLOUD.54 — Backup release gate.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\cloud.md (anchor task-cloud-54).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/cloud-54 (python tools/delivery.py claim CLOUD.54 --worker <name>); task branch task/cloud-54 in Cloud; ledger record ledger/tasks/cloud-54.md.
Kind/size: service/S. Baseline: not-started.
Outcome: Verified independent backup and safety journal are required before paid production admission; no unverified restore, private access or mutation reopens on incomplete inventory.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-46.06 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\46-backup-recovery-and-data-health.md, anchor rule-wp-46.06

Entry condition: adoption slice ADOPT.07.cloud is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] CLOUD.48: the independent backup/safety-journal mechanism this gate checks the completeness of
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Cloud:src/Cloud/ArcForges.Cloud.Backup/ReleaseGate/**
Unblocks: CLOUD.55

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): opt-in tests: no unverified restore, private access or mutation reopens on incomplete inventory
Completion evidence for the ledger: incomplete-inventory refusal results
```

```text
Execute ArcForges delivery task CLOUD.55 — Owned-artifact closure and real integration.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\cloud.md (anchor task-cloud-55).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/cloud-55 (python tools/delivery.py claim CLOUD.55 --worker <name>); task branch task/cloud-55 in Cloud; ledger record ledger/tasks/cloud-55.md.
Kind/size: integration/M. Baseline: not-started.
Outcome: Every WP-46 substep is complete, built/packed once, and consumed as exact candidate bytes from a clean environment with all applicable UX acceptance groups recorded.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-46.90 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\46-backup-recovery-and-data-health.md, anchor rule-wp-46.90

Entry condition: adoption slice ADOPT.07.cloud is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- none
Completion prerequisites (may start earlier; cannot complete before these are complete):
- [integration] CLOUD.48: final candidate
- [integration] CLOUD.49: final candidate
- [integration] CLOUD.50: final candidate
- [integration] CLOUD.51: final candidate
- [integration] CLOUD.52: final candidate
- [integration] CLOUD.53: final candidate
- [integration] CLOUD.54: final candidate

Permitted write scope: Cloud:artifacts/candidate/**
Unblocks: REL.06

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): package/contract/owner/version compatibility, failure/recovery, real boundaries
Completion evidence for the ledger: owned artifact and real-integration receipt per WP-46.90
```

```text
Execute ArcForges delivery task CLOUD.58 — Structural removal of the Notes/Chat export runtime fixtures.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\cloud.md (anchor task-cloud-58).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/cloud-58 (python tools/delivery.py claim CLOUD.58 --worker <name>); task branch task/cloud-58 in Cloud; ledger record ledger/tasks/cloud-58.md.
Kind/size: integration/M. Baseline: not-started.
Outcome: Both production clients run with no fixture export producer registered; real Cloud export jobs serve both paths

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-25.08 (full, joint with consumer-side structural fixture-registration removal): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\25-sync-engine-and-blob-lifecycle.md, anchor rule-wp-25.08

Entry condition: adoption slice ADOPT.07.cloud is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] CLOUD.45: real, delivered outcome of CLOUD.45 (Real Cloud Notes and Chat export producers)
- [artifact] NOTES.33: real, delivered outcome of NOTES.33 (Real Cloud Notes export join replaces the / fixture endpoint)
- [artifact] AST.21: assistant history export consuming the real Cloud export producer
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: 
Unblocks: CLOUD.47

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Local real-integration run of the affected scenario in an existing environment, recorded once; offline and static checks in CI; no hosted runtime, device, browser, live-service or inference CI (P2-017).
Completion evidence for the ledger: Both production clients run with no fixture export producer registered; real Cloud export jobs serve both paths
```

```text
Execute ArcForges delivery task CLOUD.63 — Real Commerce/Entitlement participation in the shared atomic family engine.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\cloud.md (anchor task-cloud-63).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/cloud-63 (python tools/delivery.py claim CLOUD.63 --worker <name>); task branch task/cloud-63 in Cloud; ledger record ledger/tasks/cloud-63.md.
Kind/size: integration/M. Baseline: not-started.
Outcome: The 'exact credits' half of WP-21.05's own completion gate ('Two Containers contend, stale holder cannot finalize, exact credits and sync cursor safety') -- Commerce's family participation, owned by the commerce, policy and operations lanes

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-21.05 (Commerce/Entitlement family participant evidence for the shared completion gate): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\21-cloud-host-and-persistence.md, anchor rule-wp-21.05

Entry condition: adoption slice ADOPT.07.cloud is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] CLOUD.06: real, delivered outcome of CLOUD.06 (Shared atomic family guarded-batch engine)
- [artifact] CLOUD.16: real, delivered outcome of CLOUD.16 (PAT and actor authorization)
- [artifact] COM.09: real, delivered outcome of COM.09 (Ledgers and reconciliation)
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: 
Unblocks: CLOUD.06

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Local real-integration run of the affected scenario in an existing environment, recorded once; offline and static checks in CI; no hosted runtime, device, browser, live-service or inference CI (P2-017).
Completion evidence for the ledger: The 'exact credits' half of WP-21.05's own completion gate ('Two Containers contend, stale holder cannot finalize, exact credits and sync cursor safety') -- Commerce's family participation, owned by the commerce, policy and operations lanes
```

```text
Execute ArcForges delivery task CLOUD.64 — Full operator contract closure across PublicApi, Commerce, Policy and Console.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\cloud.md (anchor task-cloud-64).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/cloud-64 (python tools/delivery.py claim CLOUD.64 --worker <name>); task branch task/cloud-64 in Cloud; ledger record ledger/tasks/cloud-64.md.
Kind/size: integration/M. Baseline: not-started.
Outcome: Every operator operation's eight authorization fields, operator scope and OC-03 role binding work end-to-end with the real financial owners (WP-42), configuration/policy owners (WP-44) and console join (WP-45)

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-23:operator-contract-closure-appendix-full Operator contract closure appendix, full cross-area join (Operator contract closure appendix, full cross-area join): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\23-public-api-and-generated-clients.md, package-level obligation

Entry condition: adoption slice ADOPT.07.cloud is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] COM.13: real, delivered outcome of COM.13 (Operator financial-owner proposal/approval operations)
- [artifact] POL.05: real, delivered outcome of POL.05 (Kill switches)
- [artifact] OPS.05: real, delivered outcome of OPS.05 (Operator console and support access)
- [artifact] CLOUD.21: real public endpoint mapping for the operator operations
- [artifact] CLOUD.22: real typed protocol and error mapping
Completion prerequisites (may start earlier; cannot complete before these are complete):
- [integration] CLOUD.28: the WP-23 operator contract closure accepted

Permitted write scope: 

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Local real-integration run of the affected scenario in an existing environment, recorded once; offline and static checks in CI; no hosted runtime, device, browser, live-service or inference CI (P2-017).
Completion evidence for the ledger: Every operator operation's eight authorization fields, operator scope and OC-03 role binding work end-to-end with the real financial owners (WP-42), configuration/policy owners (WP-44) and console join (WP-45)
```

```text
Execute ArcForges delivery task CLOUD.66 — Every enumerated sensitive operation wired to the step-up mechanism.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\cloud.md (anchor task-cloud-66).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/cloud-66 (python tools/delivery.py claim CLOUD.66 --worker <name>); task branch task/cloud-66 in Cloud; ledger record ledger/tasks/cloud-66.md.
Kind/size: integration/M. Baseline: not-started.
Outcome: Full coverage of WP-22.04's completion gate ('every enumerated operation demands step-up') across Commerce refund/purchase operations and any other module-owned sensitive operation, not just Identity's own

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-22.04 (cross-product operation coverage beyond Identity's own operations): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\22-identity-workspace-and-device.md, anchor rule-wp-22.04

Entry condition: adoption slice ADOPT.07.cloud is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] CLOUD.15: real, delivered outcome of CLOUD.15 (Step-up challenges for sensitive operations)
- [artifact] COM.10: real, delivered outcome of COM.10 (Refunds, disputes and evidence)
- [artifact] CLOUD.21: real public endpoint mapping for the sensitive operations
- [artifact] CLOUD.22: real typed protocol and error mapping that returns step-up challenges
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: 
Unblocks: CLOUD.20

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Local real-integration run of the affected scenario in an existing environment, recorded once; offline and static checks in CI; no hosted runtime, device, browser, live-service or inference CI (P2-017).
Completion evidence for the ledger: Full coverage of WP-22.04's completion gate ('every enumerated operation demands step-up') across Commerce refund/purchase operations and any other module-owned sensitive operation, not just Identity's own
```

```text
Execute ArcForges delivery task CLOUD.67 — Combined AI reopen after Cloud disaster-recovery restore.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\cloud.md (anchor task-cloud-67).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/cloud-67 (python tools/delivery.py claim CLOUD.67 --worker <name>); task branch task/cloud-67 in Cloud; ledger record ledger/tasks/cloud-67.md.
Kind/size: integration/M. Baseline: not-started.
Outcome: AI services genuinely reopen and function after a real Cloud DR restore, per WP-46.03's own 'then combined AI reopen at 50/52'

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-46.03 (combined AI-reopen portion): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\46-backup-recovery-and-data-health.md, anchor rule-wp-46.03

Entry condition: adoption slice ADOPT.07.cloud is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] CLOUD.51: real, delivered outcome of CLOUD.51 (Disaster-recovery drill programme)
- [artifact] HAR.00: the real Harness turn loop to reopen
- [artifact] HAR.02: real approval, cancellation and crash recovery
- [artifact] HAR.03: real generated streaming and durable output
- [artifact] AIR.00: real Workers AI provider adapters
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: 
Unblocks: CLOUD.51

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Local real-integration run of the affected scenario in an existing environment, recorded once; offline and static checks in CI; no hosted runtime, device, browser, live-service or inference CI (P2-017).
Completion evidence for the ledger: AI services genuinely reopen and function after a real Cloud DR restore, per WP-46.03's own 'then combined AI reopen at 50/52'
```
