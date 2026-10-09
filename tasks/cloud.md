# ArcForges delivery task prompts — Cloud core

Generated from Design `docs/planning/delivery/delivery-graph.json` by `tools/delivery.py`; do not edit by hand.
Each block is self-contained. Claim a task only when `python tools/delivery.py ready` lists it, with
`python tools/delivery.py claim <TASK-ID> --worker <name>`, then follow `arcforges-implementation.md`.
Tasks are ordered by lane for reading; the order is not a schedule.

## Cloud core

```text
Execute ArcForges delivery task CLOUD.01 — Ingress and host pipeline.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\cloud.md (anchor task-cloud-01).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/cloud-01 (python tools/delivery.py claim CLOUD.01 --worker <name>); task branch task/cloud-01 in Cloud; ledger record ledger/tasks/cloud-01.md.
Kind/size: service/M. Baseline: not-started.
Outcome: Worker /api routing plus the C# AOT gRPC-Web/auth/current-owner pipeline runs behind the Worker in the real Container image; no buffered stream, no direct public Container port.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-21.00 (all work except the parts mapped to CLOUD.39): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\21-cloud-host-and-persistence.md, anchor rule-wp-21.00

Entry condition: adoption slice ADOPT.07.cloud is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [contract] CON.91: published ArcForges.Contracts.PublicApi generated gRPC-Web service stubs to register the pipeline against
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Cloud:worker/index.ts; Cloud:worker/router.ts; Cloud:worker/ingress/** (new: the generalized /api route table, credential and CSRF edge checks and the frame-guarded streaming pass-through); Cloud:worker/foundation/entry.ts, Cloud:worker/foundation/container-env.ts and Cloud:worker/foundation/types.ts (only to hand the ingress route table the proof-only probe route and to forward the allowed origin; no change to a proof route, queue consumer or private handler); Cloud:wrangler.json; Cloud:Dockerfile; Cloud:.dockerignore (only admit the new nested C# source folder of the existing host project by the same append-only explicit directory rule and *.cs rule used for its other source folders; every other ignore rule is preserved); Cloud:src/ArcForges.Cloud/** (the existing Native AOT host project, which is the real layout of the planned src/ArcForges.Cloud.Host/**; the adoption rules forbid renaming it or adding a parallel project); Cloud:tests/ArcForges.Cloud.Tests/**; Cloud:tests/worker/**; Cloud:eng/verification/** (the local cross-process and explicit opt-in live scenarios of the pipeline); Cloud:package.json (the explicit test file list and the pipeline scenario scripts only; no dependency or version change); Cloud:eng/policy/dependency-policy.json and Cloud:eng/policy/dependency-reviews/cloud-01-*.json (new immutable successor chained from the then-active receipt, only because the changed bundle, manifest and source inputs are hash-bound; no coordinate, integrity value or closure entry changes); Cloud:eng/provenance/** (immutable successor release profile, Worker bundle and runtime-notice records only where an existing record binds an input this task changes, the first-party inventory files.json and the deterministic NOTICE.txt); Cloud:docs/cloud-ingress.md, Cloud:docs/deployment.md and Cloud:AGENTS.md (factual description of the ingress pipeline; the AGENTS.md Hello bullet is narrowed to what remains true)
Shared resources (follow the owner protocol): RES-cloud-deployment (append): Bindings are added by the owning module task in its own section, and the Cloud integration owner resolves ordering conflicts at merge. Any task that runs against the deployed test environment holds the lease `leases/res-cloud-deployment` for that live run only, whatever mode it declares for its binding edits; production deployment belongs to release tasks.; RES-cloud-host-composition (append): Each module registers through its own module entry point and route fragment; the host composition only lists modules; route and binding conflicts are resolved by the integration owner at merge.
Unblocks: CLOUD.02, CLOUD.05, CLOUD.08, CLOUD.09, CLOUD.10, CLOUD.19, CLOUD.39, CLOUD.42, CLOUD.69, CLOUD.70, CLOUD.84, HAR.00, HAR.40, PLT.48

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): offline unit tests for routing/validation logic; deployed-environment request/stream/cancel/CSRF/trailer path checks are opt-in local runtime evidence per docs/validation-policy.md, not hosted CI
Completion evidence for the ledger: source commit, Worker/Container image hash, deployed request/stream/cancel/CSRF/trailer scenario results, confirmation no buffered stream or direct public Container port exists
Notes: Foundation task. The Hello World router.ts already proves the deadline/cancel/body-limit/trailer mechanics at small scale (see worker/router.ts); WP21.00 generalizes this to real dispatch. Early risk: every later public call depends on this boundary being correct. Planning repair 2026-10-08 (DLV-34; P2-021; adjudication 5): the worker/index.ts and worker/router.ts transport adapter stays thin. Its TypeScript credential, CSRF and Origin edge checks are kept only under the P2-021 edge-guard rule: C# remains authoritative and enforces the same rule, their parameters and allowlists are generated from the C# source, and the Worker only refuses early (a cost control) and never grants. No user decision is needed for them. The remaining business decisions move to C# under CLOUD.84. Outcome, validation and evidence above are recorded history and are unchanged.
```

```text
Execute ArcForges delivery task CLOUD.02 — Nineteen module boundaries and D1 named-plan bridge.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\cloud.md (anchor task-cloud-02).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/cloud-02 (python tools/delivery.py claim CLOUD.02 --worker <name>); task branch task/cloud-02 in Cloud; ledger record ledger/tasks/cloud-02.md.
Kind/size: service/M. Baseline: not-started.
Outcome: The 19 module projects exist as boundaries and the D1 named-plan bridge mechanism works: C# decides business logic and asks the Worker to execute one exact named/versioned plan; the Worker executes only approved SQL, never ad hoc queries.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-21.02 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\21-cloud-host-and-persistence.md, anchor rule-wp-21.02

Entry condition: adoption slice ADOPT.07.cloud is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] CLOUD.01: the deployed ingress/host pipeline to carry the private C#<->Worker plan-execution calls
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Cloud:src/ArcForges.Cloud.Modules.*/** (one project per module, named ArcForges.Cloud.Modules.<Name> for the 19 owners of the Cloud schema map, plus ArcForges.Cloud.Modules.Abstractions for the shared boundary types; the Domain, Application and Infrastructure layers are folders and namespaces inside each project, enforced by architecture tests, instead of three projects per module); Cloud:src/ArcForges.Cloud.Storage.D1/** (new project that owns the named-plan binding mechanism; it receives, by move with namespaces preserved, the PRF.07 proof bridge now in Cloud:src/ArcForges.Cloud/Storage/** and Cloud:src/ArcForges.Cloud/Hmac/**: plan definitions, exact scalar values, executor, private request signing and the generated manifest); Cloud:storage/plans/** (the plan root and owner registry; it receives, by move, the reviewed plans now in Cloud:src/ArcForges.Cloud/Storage/Plans/**); Cloud:src/ArcForges.Cloud/** (the existing Native AOT host project, which is the real layout of the planned Cloud.Host; only the removal of the moved Storage and Hmac sources, the project references, the module catalog listing in Composition/HostModules.cs and the project file; no behavior change and no rename, per the adoption rules); Cloud:Cloud.slnx, Cloud:Dockerfile, Cloud:.dockerignore and Cloud:eng/policy/licence-boundary.json (only project membership, the restore and publish context of the new projects by the same explicit directory and *.cs rules, and the licence boundary rows; every other rule is preserved); Cloud:tests/ArcForges.Cloud.Tests/** and Cloud:tests/worker/**; Cloud:eng/verification/storage-plans.ts (the plan root, the owner and table ownership checks and the generated C# output path; the Worker dictionary format and the manifest hash algorithm are unchanged) and Cloud:package.json (the explicit test file list only; no dependency or version change); Cloud:tooling/dependency-policy.ts and Cloud:tooling/dependency-policy.test.ts (only to admit src/ArcForges.Cloud.Storage.D1/ as the second consumer root of the private generated CloudInternal records, which moved with the bridge; no new package, owner or coordinate), and Cloud:tooling/release-provenance.ts only if an existing check enumerates the host source root; Cloud:eng/policy/dependency-policy.json and Cloud:eng/policy/dependency-reviews/cloud-02-*.json (new immutable successor chained from the then-active receipt, only because the hash-bound project, lock and source inputs change; no coordinate, integrity value or closure entry changes); Cloud:eng/provenance/** (immutable successor release profile, Worker bundle and runtime-notice records only where an existing record binds an input this task changes, the first-party inventory files.json and the deterministic NOTICE.txt); Cloud:docs/storage-plans.md (new), Cloud:docs/development.md, Cloud:docs/prf-07-foundation-proof.md (path references only) and Cloud:AGENTS.md (factual description of the module projects and the plan root)
Shared resources (follow the owner protocol): RES-cloud-host-composition (append): Each module registers through its own module entry point and route fragment; the host composition only lists modules; route and binding conflicts are resolved by the integration owner at merge.; RES-cloud-storage-plans (append): Each module owns its own plan directory; the plan-manifest hash is regenerated by the author after rebase and checked in CI.
Unblocks: CLOUD.03, CLOUD.04, CLOUD.06, CLOUD.07, CLOUD.08, CLOUD.10, CLOUD.11, CLOUD.84, SIM.01

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): offline architecture/import tests (no forbidden cross-module reference), plan-hash tests, wrong-container/public-access refusal tests, AOT compile
Completion evidence for the ledger: architecture/import/plan-hash/wrong-container/public-access refusal test results, source commit and plan-manifest hash
Notes: Foundation task and the security-model proof: if the C#-decides/Worker-executes-approved-SQL-only boundary is wrong, every module built on it inherits the defect. Every module task (Identity, Sync, Resource, etc.) in this and other areas starts against this. Planning repair 2026-10-08 (DLV-34; P2-021): the TypeScript generated plan dictionary under storage/plans and eng/verification becomes data generated from the C# single source under CLOUD.84; plan authority moves to C#. Outcome, validation and evidence above are recorded history and are unchanged. Planning repair 2026-10-09 (P2-026; scope correction): reduced: the PackageCatalog boundary project, its Cloud.slnx, HostModules and licence-boundary registrations are out of scope, not completed; the delivered project is kept as history and is not deleted; the 19-owner count is labelled, not left unstated: PackageCatalog is the out nineteenth owner, and the active V1 count is 18 (P2-026, S5).
```

```text
Execute ArcForges delivery task CLOUD.03 — D1 migration runner and exact physical mapping.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\cloud.md (anchor task-cloud-03).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/cloud-03 (python tools/delivery.py claim CLOUD.03 --worker <name>); task branch task/cloud-03 in Cloud; ledger record ledger/tasks/cloud-03.md.
Kind/size: service/L. Baseline: not-started.
Outcome: Model-04's full physical manifest is implemented: migrations, typed exact bind/result adapters for D1's signed64/uint64/Decimal/JSON/FTS5 quirks, and expand/backfill/fenced-cutover migration mode support.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-21.03 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\21-cloud-host-and-persistence.md, anchor rule-wp-21.03
- WP-21:6-impacts-migration-compatibility-manife §6 Impacts -- migration/compatibility manifests include source/schema/plan/ABI/runtime versions (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\21-cloud-host-and-persistence.md, package-level obligation

Entry condition: adoption slice ADOPT.07.cloud is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] CLOUD.02: module boundary projects to attach physical tables to (physical table name = <module>_<snake_case_entity>)
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Cloud:src/ArcForges.Cloud.Storage.D1/Migrations/** (the numbered, checksum-locked D1 migrations and the append-only migration lock; RES-cloud-d1-migrations); Cloud:src/ArcForges.Cloud.Storage.D1/Physical/** (the checked-in physical manifest, its generated C# column maps, the typed exact bind/result adapters and their shared vectors); Cloud:eng/migrations/** and Cloud:eng/verification/physical-schema.ts (the migration runner with its D1 clients and sequence assignment, and the manifest validator, baseline emitter and migration-to-manifest drift check; Node tooling like eng/verification/storage-plans.ts, because migrations run from the gated deployment job and never from the Container); Cloud:tests/ArcForges.Cloud.Tests/Physical/** and Cloud:tests/ArcForges.Cloud.Tests/Vectors/physical-*.json and Cloud:tests/worker/d1-*.test.ts (adapter, manifest, migration and conformance tests, new files only); Cloud:package.json (only the new npm scripts and the new test files in the test list), Cloud:tsconfig.json (only the include of eng/migrations) and Cloud:.dockerignore (only the admission rule of the new Physical source folder, so the image build context holds the sources that compile into the host); Cloud:eng/policy/dependency-policy.json and Cloud:eng/policy/dependency-reviews/cloud-03-*.json (new immutable successor chained from the then-active receipt, only because hash-bound project and release inputs change; no coordinate, integrity value or closure entry changes); Cloud:eng/provenance/** (immutable successor release profile, Worker bundle and runtime-notice records only where an existing record binds an input this task changes, the first-party inventory files.json and the deterministic NOTICE.txt); Cloud:docs/d1-physical-schema.md (new, factual description of the manifest, the adapters, the migration runner and its modes) and Cloud:docs/storage-plans.md and Cloud:AGENTS.md (only factual pointers if the description of the storage layer changes)
Shared resources (follow the owner protocol): RES-cloud-d1-migrations (append): One global D1 migration sequence: each module task authors migrations under its module prefix; the integration owner assigns the global sequence number at merge, regenerates the plan manifest and rejects edits to merged migrations; the migrator applies in sequence with receipts.
Unblocks: CLOUD.04, CLOUD.06, CLOUD.07, CLOUD.09, CLOUD.10, CLOUD.11, CLOUD.39, CLOUD.48, CLOUD.70, CLOUD.84, COM.16

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): offline unit tests for bind/result adapters; opt-in local runtime tests against a real D1 instance for signed64/uint64/Decimal/JSON/FTS5, interrupted migration, stale backfill and compatible rollback per docs/validation-policy.md
Completion evidence for the ledger: actual D1 signed64/uint64/decimal/JSON/FTS5 conformance results, interrupted-migration/stale-backfill/rollback test results, source commit
Notes: Early risk proof: D1's real type/SQL quirks (signed 64-bit only, no native uint64/Decimal, JSON1, FTS5 behavior) affect the physical design of all 19 modules' tables. Getting the bind/result adapters wrong here would force rework across every later module task in every area that stores data in D1. Planning repair 2026-10-08 (DLV-34; P2-021; brief section 5.7): the runner's lease, epoch fence, gating and sequence decisions move to C# under CLOUD.84 (src/ArcForges.Cloud.Storage.D1/MigrationRunner), and Node only invokes wrangler. This complete record’s writes are history and are not restated; CLOUD.84 carries the move. Migration SQL, the physical manifest and the migration lock are unchanged. The outcome, validation and evidence above are unchanged by this note; the runner decisions they name are re-homed to CLOUD.84 as stated. Planning repair 2026-10-09 (P2-026; scope correction): reduced: the package_catalog physical tables, their generated column maps, typed adapters, conformance vectors and tests are out of scope, not completed; locked migrations stay as history and are not edited or deleted.
```

```text
Execute ArcForges delivery task CLOUD.04 — Receipts, outbox, inbox dedup and change archive.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\cloud.md (anchor task-cloud-04).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/cloud-04 (python tools/delivery.py claim CLOUD.04 --worker <name>); task branch task/cloud-04 in Cloud; ledger record ledger/tasks/cloud-04.md.
Kind/size: service/M. Baseline: not-started.
Outcome: Every atomic guarded write also produces its owner receipt, outbox entry and change-archive row in the same D1 batch; inbox dedup makes replay a no-op; publication is contiguous (no gaps).

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-21.04 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\21-cloud-host-and-persistence.md, anchor rule-wp-21.04

Entry condition: adoption slice ADOPT.07.cloud is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] CLOUD.02: the D1 named-plan bridge to add receipt/outbox/inbox writes inside
- [artifact] CLOUD.03: physical platform.command/outbox/inbox tables (data-model/01 §2 platform infra tables)
- [artifact] CLOUD.06: the guard table platform_command_guard, the guard statement grammar and the release statement of the shared-family engine
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Cloud:src/ArcForges.Cloud.Storage.D1/Receipts/** (the commit tail builder, the command receipt and its replay classification, the inbox dedup); Cloud:src/ArcForges.Cloud.Storage.D1/Outbox/** (outbox streams, the contiguous publisher with its guarded acknowledgement and reconciliation, attempts, dead letter and requeue) and Cloud:src/ArcForges.Cloud.Storage.D1/Archive/** (the change archive reader with its record-hash verification and the acknowledged watermark); Cloud:storage/plans/platform/** and the generated plan manifest Cloud:worker/storage/plans.generated.ts and Cloud:src/ArcForges.Cloud.Storage.D1/PlanManifest.g.cs (the platform owner's named plans over platform_ tables only: receipt and inbox reads and writes, stream state, outbox select, acknowledgement, attempt, dead letter and requeue, archive select, acknowledgement and purge, and the outbox and change-archive purge under the purge rule of model 01; the manifest hash is regenerated by the author after rebase; RES-cloud-storage-plans); Cloud:eng/verification/storage-plans.ts and the new Cloud:eng/verification/commit-tail.ts (only the commit-tail directive and its verification: a module write plan declares the canonical commit tail or the reason it has none, a plan that declares it starts with a commit-guard insert and ends with the exact canonical statements, and the one shared definition of that tail; no change to the table-ownership rule, the statement grammar or the generated output format); Cloud:src/ArcForges.Cloud.Storage.D1/Physical/manifest/platform.json, Cloud:src/ArcForges.Cloud.Storage.D1/Physical/PhysicalSchema.g.cs and Cloud:src/ArcForges.Cloud.Storage.D1/Migrations/** (only the three new platform tables of model 01 section 2, platform.sequence_stream, platform.outbox_position and platform.change_archive, as one append-only expand migration numbered at merge by the integration owner; RES-cloud-d1-migrations; the guard table platform.command_guard is CLOUD.06's and is only consumed here; no existing table, column, trigger or locked migration changes); Cloud:tests/ArcForges.Cloud.Tests/Receipts/**, Cloud:tests/ArcForges.Cloud.Tests/Outbox/**, Cloud:tests/ArcForges.Cloud.Tests/Archive/**, Cloud:tests/ArcForges.Cloud.Tests/Vectors/commit-tail*.json, Cloud:tests/worker/commit-tail*.test.ts, Cloud:tests/worker/d1-receipts*.test.ts, Cloud:tests/worker/support/** (new files only), Cloud:eng/verification/d1-receipts-local.ts (the explicit opt-in run against workerd's D1), and the minimal edits of existing tests that the new tables and plans require: the pinned table inventory counts and the per-table monotonic fixtures of Cloud:tests/ArcForges.Cloud.Tests/Physical/** and Cloud:tests/worker/d1-physical-schema.test.ts, the hard-coded next migration numbers of Cloud:tests/worker/d1-migration-runner.test.ts (now derived from the catalog), and the owner list and scope rule of Cloud:tests/worker/storage-plan-ownership.test.ts and Cloud:tests/worker/storage-plans-generator.test.ts for the platform owner's plans, and the pinned Worker bundle hash and size of Cloud:tests/worker/release-provenance.test.ts, which the regenerated plan dictionary changes; Cloud:package.json (only the new npm scripts and the new test files in the test list), Cloud:tsconfig.json (only includes of new Node files) and Cloud:.dockerignore (only the admission rule of any new Storage.D1 source folder, so the image build context holds the sources that compile into the host); Cloud:eng/policy/dependency-policy.json and Cloud:eng/policy/dependency-reviews/cloud-04-*.json (new immutable successor chained from the then-active receipt, only because hash-bound project and release inputs change; no coordinate, integrity value or closure entry changes); Cloud:eng/provenance/** (immutable successor release profile, Worker bundle and runtime-notice records only where an existing record binds an input this task changes, the first-party inventory files.json and the deterministic NOTICE.txt); Cloud:docs/d1-receipts-outbox.md (new, factual description of the commit tail, the receipts, the outbox streams, the inbox and the change archive) and Cloud:docs/storage-plans.md, Cloud:docs/d1-physical-schema.md and Cloud:AGENTS.md (only factual pointers if the description of the storage layer changes)
Shared resources (follow the owner protocol): RES-cloud-d1-migrations (append): One global D1 migration sequence: each module task authors migrations under its module prefix; the integration owner assigns the global sequence number at merge, regenerates the plan manifest and rejects edits to merged migrations; the migrator applies in sequence with receipts.; RES-cloud-storage-plans (append): Each module owns its own plan directory; the plan-manifest hash is regenerated by the author after rebase and checked in CI.
Unblocks: CLOUD.05, CLOUD.10, CLOUD.11, CLOUD.31, CLOUD.39, CLOUD.72, CLOUD.84, COM.16, SIM.04

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): offline unit tests plus opt-in local D1 runtime tests: constraint-guard failure rolls back all rows, zero-row CAS cannot publish, duplicate/lost ack reconciles
Completion evidence for the ledger: constraint-guard rollback, zero-row-CAS and duplicate/lost-ack reconciliation results
Notes: This generic outbox mechanism is distinct from (a) WP-24.04's DO wake/live-feed publisher and (b) WP-25.02's sync.change publish_seq bootstrap publisher; both consume this task's committed outbox rows but each adds its own D1-batch publication logic.. Planning repair 2026-10-05: the write scope is bound to the real Cloud layout (the commit-tail directive in the plan generator, the three new platform tables as one expand migration, the platform owner's plans, tests and the factual document), as for CLOUD.01, CLOUD.02, CLOUD.03 and COM.05. The physical tables of model 01 had no sequence and no change-archive field list, so model 01 section 2 and model 04 sections 4 and 5 now define them; the guard table is defined by the CLOUD.06 repair (platform.command_guard) and CLOUD.04 follows its guards with the commit tail and the release, which that repair's generated family plans append the same way. The module-facing exposure of the commit tail (a port in ArcForges.Cloud.Modules.Abstractions) belongs to the generic plan-execution port of COM.16; this task delivers the mechanism inside Storage.D1. The finite-job lease and fence plans over platform.job_lease are not part of WP-21.04 and are not delivered here. Planning repair 2026-10-08 (DLV-34; P2-021): plan authoring under storage/plans moves to C# under CLOUD.84. The owner receipt, commit tail and outbox contracts are unchanged. Outcome, validation and evidence above are recorded history and are unchanged.
```

```text
Execute ArcForges delivery task CLOUD.05 — Finite durable jobs (Cron, Queue and DO-alarm wake into C# endpoints).

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\cloud.md (anchor task-cloud-05).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/cloud-05 (python tools/delivery.py claim CLOUD.05 --worker <name>); task branch task/cloud-05 in Cloud; ledger record ledger/tasks/cloud-05.md.
Kind/size: service/M. Baseline: not-started.
Outcome: Perpetual hosted loops are replaced by Cron-, Queue- and Durable-Object-alarm-woken C# endpoints bounded to <=100 items/20s per job with checkpoint/receipt/lease-then-yield semantics. No Cloudflare Workflow holds job state or wakes a job in this task; each wake is a stateless forward into a C# endpoint, and C# makes every step decision. A later Workflow wake adapter needs its own reviewed record (P2-021 item 5).

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-21.01 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\21-cloud-host-and-persistence.md, anchor rule-wp-21.01

Entry condition: adoption slice ADOPT.07.cloud is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] CLOUD.01: the deployed Worker/Container ingress to attach Cron, Queue and Durable Object alarm triggers to
- [artifact] CLOUD.04: receipt/lease primitives to checkpoint job progress
- [artifact] CLOUD.69: the Cloud-side correlation seam for wake messages and job-slice calls
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Cloud:src/ArcForges.Cloud.Jobs/** (new project, not in the tree today: the C# queue/coordination and finite-job runner; registered by this task in Cloud:Cloud.slnx and Cloud:src/ArcForges.Cloud/ArcForges.Cloud.csproj, project membership and project-reference lines only); Cloud:Cloud.slnx (project membership line only; RES-cloud-host-composition); Cloud:src/ArcForges.Cloud/ArcForges.Cloud.csproj (project-reference line only; RES-cloud-host-composition); Cloud:worker/ingress/** (new thin wake shim only: Cron, Queue and alarm forwarding to the C# job endpoints; no job decision in TypeScript)
Shared resources (follow the owner protocol): RES-cloud-deployment (append): Bindings are added by the owning module task in its own section, and the Cloud integration owner resolves ordering conflicts at merge. Any task that runs against the deployed test environment holds the lease `leases/res-cloud-deployment` for that live run only, whatever mode it declares for its binding edits; production deployment belongs to release tasks.; RES-cloud-host-composition (append): Each module registers through its own module entry point and route fragment; the host composition only lists modules; route and binding conflicts are resolved by the integration owner at merge.
Unblocks: CLOUD.10, CLOUD.33, CLOUD.45, CLOUD.84, HAR.00, SIM.03

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): opt-in local runtime tests: sleep/restart, duplicate wake, delayed delivery, stale lease, paused simulator continuation
Completion evidence for the ledger: sleep/restart, duplicate-wake, delayed-delivery, stale-lease and paused-simulator-continuation results
Notes: This is the generic mechanism later background jobs plug into: WP-25.02's publisher, WP-25.06 realm-transfer jobs, WP-46 backup jobs, notification delivery retries. Planning repair 2026-10-05: job wake messages and job-slice calls carry correlationId and causationId through the CLOUD.69 seam; this task keeps them when it replaces the proof queue consumer (no new write scope). Planning repair 2026-10-08 (DLV-34; P2-021; coordinator adjudication 8): re-specified as 'Finite durable jobs (Cron, Queue and DO-alarm wake into C# endpoints)' with no Cloudflare Workflow state and no Workflow wake in this task. The job logic and its budgets (<=100 items/20s per job) are C#, and the TypeScript wake shim is the only TypeScript this task writes. Validation, evidence and the budgets are unchanged; no acceptance is removed.
```

```text
Execute ArcForges delivery task CLOUD.06 — Shared atomic family guarded-batch engine.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\cloud.md (anchor task-cloud-06).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/cloud-06 (python tools/delivery.py claim CLOUD.06 --worker <name>); task branch task/cloud-06 in Cloud; ledger record ledger/tasks/cloud-06.md.
Kind/size: service/M. Baseline: not-started.
Outcome: A reusable D1 guarded-batch engine exists that enforces the fixed SU-04 module lock order (Config->Identity->Workspace->Device->Entitlement->Commerce->Policy->Agent->Chat->Scope->Task->Search->PackageCatalog->Notification->Resource->Sync->Audit) and provides authorization/revision/policy/balance/lease guard primitives that any shared-transaction family can compose: a closed registry of families with their participant lists, a family plan grammar whose generator expands the guard primitives against the physical manifest and refuses a plan that is out of order, names a table of another participant's module or lets a module write without its own guard, the platform_command_guard table that makes a false guard roll the whole batch back, and a C# unit of work and executor that seal one family plan call, supply the command identity to every guard, and reread and recalculate with bounded jitter only under the original command. The module tasks append their own family and plans (RES-shared-transaction-families); this task ships the registry empty and no family plan.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-21.05 (generic guarded-batch engine and fixed SU-04 module lock-order enforcement only; each module's own family participant list is a separate obligation carried by that module's own task (see coverage)): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\21-cloud-host-and-persistence.md, anchor rule-wp-21.05

Entry condition: adoption slice ADOPT.07.cloud is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] CLOUD.02: the D1 named-plan bridge, since a guarded batch is executed as one named plan
- [artifact] CLOUD.03: the physical manifest and migration runner: the guard primitives are expanded against the physical columns and the guard table is one more manifest table and expand migration
Completion prerequisites (may start earlier; cannot complete before these are complete):
- [integration] CLOUD.63: at least two real module family participants exercising the engine under contention (e.g. Identity's auth/enrollment family and Sync's synced-content-mutation family)

Permitted write scope: Cloud:src/ArcForges.Cloud.Storage.D1/SharedFamilies/** (the engine: the fixed SU-04 module lock order, the family and participant types, the typed guard primitives, the unit of work that seals one family plan call and the executor with its bounded reread; internal to Storage.D1 and built on the existing IPlanExecutor, so it is not a second execution path and it carries no SQL text); Cloud:storage/plans/families.json and Cloud:storage/plans/families/** and Cloud:storage/plans/families.expanded.json (the closed registry of shared transaction families with their participant lists, the reviewed family plan files `families.<family>.<name>` and the generated listing of their expanded statements that a review reads and the C# identity check recomputes from; the registry ships empty and no family plan ships with this task, so the plan manifest hash is unchanged; a module task appends its declared family and plans; RES-shared-transaction-families, RES-cloud-storage-plans); Cloud:eng/verification/storage-plans.ts (only the family grammar: the family header and the guard directives, expansion of the five guard primitives against the physical manifest, the SU-04 order, the participant, ownership and guard-coverage rules, and the family catalog in the generated C#) and Cloud:src/ArcForges.Cloud.Storage.D1/PlanManifest.g.cs (regenerated by that tool; it gains only the family catalog and the family plan list, both empty); Cloud:src/ArcForges.Cloud.Storage.D1/Physical/manifest/platform.json and Cloud:src/ArcForges.Cloud.Storage.D1/Physical/PhysicalSchema.g.cs (regenerated) and Cloud:src/ArcForges.Cloud.Storage.D1/Migrations/** (one append-only expand migration `platform__command-guard` and its lock entry, numbered by the integration owner at merge; RES-cloud-d1-migrations): the table platform_command_guard of the guarded batch of data model 04 section 4; Cloud:eng/verification/d1-families-local.ts (new: the opt-in local run of a fixture family on workerd's D1 under Miniflare, two writers contending and a stale lease holder) and Cloud:package.json (only the new npm script and the new test files in the test list); Cloud:tests/ArcForges.Cloud.Tests/SharedFamilies/** and Cloud:tests/ArcForges.Cloud.Tests/Vectors/family-*.json and Cloud:tests/worker/family-*.test.ts and Cloud:tests/worker/support/family-*.ts (lock-order, primitive, unit-of-work and executor tests, generator tests, and the SQLite oracle that runs generated family SQL on the real migrations, new files only; and only the minimal edits of existing files that the new table and the family plans require: the table-count pins of Cloud:tests/ArcForges.Cloud.Tests/Physical/PhysicalSchemaTests.cs and Cloud:tests/worker/d1-physical-schema.test.ts, the migration sequence pins of Cloud:tests/worker/d1-migration-runner.test.ts (derived from the catalog so that a later migration does not move them), and Cloud:tests/ArcForges.Cloud.Tests/StoragePlanBoundaryTests.cs so that its owner-plan checks skip the reserved families directory and its manifest identity includes the family plan identities); Cloud:.dockerignore (only the admission rule of the new SharedFamilies source folder, so the image build context holds the sources that compile into the host); Cloud:eng/policy/dependency-policy.json and Cloud:eng/policy/dependency-reviews/cloud-06-*.json (new immutable successor chained from the then-active receipt, only because hash-bound project and release inputs change; no coordinate, integrity value or closure entry changes); Cloud:eng/provenance/** (immutable successor release profile, Worker bundle and runtime-notice records only where an existing record binds an input this task changes, the first-party inventory files.json and the deterministic NOTICE.txt); Cloud:docs/shared-families.md (new, factual description of the registry, the family grammar, the guard primitives, the lock order, the unit of work and the executor, and what each check proves and does not) and Cloud:docs/storage-plans.md and Cloud:docs/d1-physical-schema.md and Cloud:AGENTS.md (only factual pointers, and the sentence of storage-plans.md that said the ownership rule does not allow a cross-module plan)
Shared resources (follow the owner protocol): RES-shared-transaction-families (append): Adding a participant to a shared atomic family is a design change through the Architecture Owner; module tasks implement only their declared participation.; RES-cloud-storage-plans (append): Each module owns its own plan directory; the plan-manifest hash is regenerated by the author after rebase and checked in CI.; RES-cloud-d1-migrations (append): One global D1 migration sequence: each module task authors migrations under its module prefix; the integration owner assigns the global sequence number at merge, regenerates the plan manifest and rejects edits to merged migrations; the migrator applies in sequence with receipts.
Unblocks: CLOUD.04, CLOUD.07, CLOUD.10, CLOUD.11, CLOUD.13, CLOUD.39, CLOUD.42, CLOUD.46, CLOUD.63, CLOUD.72, CLOUD.84, COM.16, SIM.03

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): offline unit tests for the guard/lock-order primitives, the family generator and the C# unit of work and executor; the generated family SQL run on the real migrations in the node:sqlite oracle (guard pass and refusal, whole-batch rollback, two writers contending, a stale lease holder); opt-in local D1 runtime tests on workerd's D1: two Containers contend, stale holder cannot finalize (the provider's REST batch atomicity and live D1 stay deferred to a RES-cloud-deployment lease)
Completion evidence for the ledger: lock-order enforcement test results, contention/stale-holder test results, source commit
Notes: Every module task that participates in a named shared-transaction family (CLOUD.11/13 Identity's auth-enrollment/device-revocation families, CLOUD.39 Sync's synced-content-mutation family, CLOUD.42 Resource's upload-lifecycle family, CLOUD.53 realm-transfer family) declares a start edge on this task and fills in its own participant logic; WP-21.05 substep coverage therefore spans CLOUD.06 plus those module tasks with differing `part` text. Planning repair 2026-10-05: the plan ownership rule of CLOUD.02 forbids a cross-module plan, so the engine's write scope is bound to the real layout and includes the family registry, the family grammar of the plan generator and the platform_command_guard table that data model 04 section 4 already uses in its minimal SQL; the registry ships empty, so no participant list is decided here (SU-01) and the module tasks that declare a family append it. Support and TrustSafety have no position in the SU-04 order, so the engine refuses them as participants until the Architecture Owner extends the order. Planning repair 2026-10-08 (DLV-34; P2-021): the family guard engine described in the TypeScript storage-plan family grammar (eng/verification/storage-plans.ts) moves to C# under CLOUD.84. The SU-04 lock order and guards are unchanged. Outcome, validation and evidence above are recorded history and are unchanged. Planning repair 2026-10-09 (P2-026; scope correction): reduced: the PackageCatalog slot of the SU-04 lock order is out of scope, not completed; the relative order of the retained modules is unchanged and the delivered engine is not reverted.
```

```text
Execute ArcForges delivery task CLOUD.07 — Capacity, Container/D1 integration producer and harness.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\cloud.md (anchor task-cloud-07).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/cloud-07 (python tools/delivery.py claim CLOUD.07 --worker <name>); task branch task/cloud-07 in Cloud; ledger record ledger/tasks/cloud-07.md.
Kind/size: service/L. Baseline: not-started.
Outcome: Model-04 named plans run through guarded-batch fixtures under measured load; the primary-authorization path, route/service-binding/outbound-handler matrix, job-slice and SimulationPacer infrastructure exist; the L-16 measurement harness and a proposed capacity report are produced.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-21.06 (all work except the parts mapped to SIM.10): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\21-cloud-host-and-persistence.md, anchor rule-wp-21.06

Entry condition: adoption slice ADOPT.07.cloud is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] CLOUD.02: module boundary + plan bridge to issue guarded-batch fixture plans against
- [artifact] CLOUD.03: physical D1 schema to measure real write/read latency against
- [artifact] CLOUD.06: the guarded-batch engine, since capacity fixtures are guarded batches
Completion prerequisites (may start earlier; cannot complete before these are complete):
- [integration] CLOUD.70: the gated migration step that applies the locked migrations to the deployed D1 database

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

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\cloud.md (anchor task-cloud-08).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/cloud-08 (python tools/delivery.py claim CLOUD.08 --worker <name>); task branch task/cloud-08 in Cloud; ledger record ledger/tasks/cloud-08.md.
Kind/size: service/S. Baseline: not-started.
Outcome: Ingress/Container/D1/DO/R2/Queue health are exposed separately, and a missing binding or plan-hash mismatch fails readiness rather than allowing partial execution to appear successful; logs remain no-content.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-21.07 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\21-cloud-host-and-persistence.md, anchor rule-wp-21.07

Entry condition: adoption slice ADOPT.07.cloud is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] CLOUD.01: the deployed ingress/Container to expose readiness for
- [artifact] CLOUD.02: the plan-manifest hash to check for mismatch
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Cloud:worker/readiness/** (new: the readiness model and its closed vocabulary, the declared required binding sets per environment, the component probes, the Container start-failure classification, the report and its HTTP form; the Worker half of the real layout of the planned src/ArcForges.Cloud.Host/Readiness/**); Cloud:src/ArcForges.Cloud/Readiness/** (new: the host half, in the existing Native AOT host project, which is the real layout of the planned src/ArcForges.Cloud.Host/Readiness/**; the adoption rules forbid renaming it or adding a parallel project); Cloud:worker/foundation/proof-routes.ts (only to serve the operator readiness operation from the readiness module and to answer a Container that did not start with the classified refusal in the proof session forward), Cloud:worker/foundation/container-client.ts (only to return the reply's media type, which the classification reads), Cloud:worker/ingress/pipeline.ts (only the classified, retryable refusal of a Container that did not start; no change to routing, admission, credentials, deadlines or the frame guard), Cloud:src/ArcForges.Cloud/Foundation/FoundationOperations.cs and Cloud:src/ArcForges.Cloud/Foundation/FoundationJson.cs (only the readiness operation, which now returns the closed report from Readiness/); Cloud:tests/ArcForges.Cloud.Tests/Readiness/**, Cloud:tests/worker/readiness-*.test.ts, Cloud:tests/worker/support/readiness-*.ts and the existing tests of the files named above (only where their pinned readiness or Container-refusal behavior changes, and the expected Worker bundle figures of tests/worker/release-provenance.test.ts that a changed bundle changes); Cloud:eng/verification/** (only the readiness scenarios of the explicit opt-in local and deployed runs, and the reading of the readiness reply by the existing scenarios), Cloud:package.json (only the new test files in the test list), Cloud:tsconfig.json (only includes of new Node files) and Cloud:.dockerignore (only the admission rule of the new Readiness source folder, so the image build context holds the sources that compile into the host); Cloud:eng/policy/dependency-policy.json and Cloud:eng/policy/dependency-reviews/cloud-08-*.json (new immutable successor chained from the then-active receipt, only because the changed bundle, manifest and source inputs are hash-bound; no coordinate, integrity value or closure entry changes); Cloud:eng/provenance/** (immutable successor release profile, Worker bundle and runtime-notice records only where an existing record binds an input this task changes, the first-party inventory files.json and the deterministic NOTICE.txt); Cloud:docs/cloud-readiness.md (new, factual description of the components, the states, the reasons and what each probe does and does not prove), Cloud:docs/cloud-ingress.md and Cloud:docs/prf-07-foundation-proof.md (only factual pointers and the changed refusal) and Cloud:AGENTS.md (only a pointer)
Shared resources (follow the owner protocol): RES-cloud-deployment (append): Bindings are added by the owning module task in its own section, and the Cloud integration owner resolves ordering conflicts at merge. Any task that runs against the deployed test environment holds the lease `leases/res-cloud-deployment` for that live run only, whatever mode it declares for its binding edits; production deployment belongs to release tasks.
Unblocks: CLOUD.10, CLOUD.84, PRF.08, PRF.11

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): opt-in local runtime tests: missing binding/plan mismatch fails readiness, not successful partial execution
Completion evidence for the ledger: missing-binding and plan-mismatch readiness-failure results
Notes: Can be built in parallel with WP-22/23/24/25 once CLOUD.01/02 exist; readiness for R2/Queue/DO bindings can be checked even while those bindings are still otherwise unused stubs. Planning repair 2026-10-05: the planned src/ArcForges.Cloud.Host/Readiness/** does not exist (the Native AOT host is the existing src/ArcForges.Cloud project, which the adoption rules forbid renaming), and the readiness of the Worker, the Container, D1, the Durable Object, R2 and the Queue is partly decided in the Worker (bindings, probes, the Container's start failures), so the write scope is bound to the real layout as for CLOUD.01, CLOUD.02, CLOUD.03 and COM.05: a Worker module and a host folder, the narrow edits of the existing proof route, ingress refusal and host operation that call them, tests, the opt-in scenarios, the dependency and provenance records that hash-bind the changed inputs, and the factual document. The task adds no public production route: the production Worker keeps serving the anonymous Hello method and its health route only, so the full report is served on the operator-signed proof surface. The launch-capacity.v1 readiness timeout (model 04) is a CLOUD.10 output, so this task uses a named default of the same value, and the gated D1 migration step is CLOUD.70. Planning repair 2026-10-08 (DLV-34; P2-021): the readiness business model in worker/readiness (evaluate.ts, model.ts) moves to C# under CLOUD.84; the readiness vocabulary is generated from C# for the adapter. Outcome, validation and evidence above are recorded history and are unchanged.
```

```text
Execute ArcForges delivery task CLOUD.09 — Selfhost.v1 deployment profile.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\cloud.md (anchor task-cloud-09).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/cloud-09 (python tools/delivery.py claim CLOUD.09 --worker <name>); task branch task/cloud-09 in Cloud; ledger record ledger/tasks/cloud-09.md.
Kind/size: service/M. Baseline: not-started.
Outcome: An operator-owned Cloudflare deployment/config/realm descriptor exists for self-hosting, with default payment disabled, separate keys/identity/providers from the official realm, immutable artifacts and independent backup requirements preserved.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-21.08 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\21-cloud-host-and-persistence.md, anchor rule-wp-21.08

Entry condition: adoption slice ADOPT.07.cloud is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] CLOUD.01: a deployable Worker/Container image to define a second deployment profile for
- [artifact] CLOUD.03: the D1 physical schema/migration runner to provision a fresh realm's database
Completion prerequisites (may start earlier; cannot complete before these are complete):
- [integration] CLOUD.70: the gated migration step to provision a fresh realm's database

Permitted write scope: Cloud:docs/deployment.md; Cloud:eng/selfhost/**
Shared resources (follow the owner protocol): RES-cloud-deployment (append): Bindings are added by the owning module task in its own section, and the Cloud integration owner resolves ordering conflicts at merge. Any task that runs against the deployed test environment holds the lease `leases/res-cloud-deployment` for that live run only, whatever mode it declares for its binding edits; production deployment belongs to release tasks.
Unblocks: CLOUD.10

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): opt-in local + real Cloudflare dev-account tests: fresh development account/realm provisioning, missing binding/secret/unsupported descriptor/redirect failures, no official token acceptance
Completion evidence for the ledger: fresh provisioning, missing-binding/secret refusal, and no-official-token-acceptance results
Notes: WP-21's own completion gate states this task hands WP-46 'a runnable deployment and complete configuration inventory'; production PG-25 evidence stays external. Can run in parallel with WP-22/23/24/25 once CLOUD.01/03 exist.
```

```text
Execute ArcForges delivery task CLOUD.10 — Owned-artifact closure and launch-capacity.v1 acceptance.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\cloud.md (anchor task-cloud-10).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/cloud-10 (python tools/delivery.py claim CLOUD.10 --worker <name>); task branch task/cloud-10 in Cloud; ledger record ledger/tasks/cloud-10.md.
Kind/size: integration/M. Baseline: not-started.
Outcome: Every WP-21 substep is complete, built/packed once, and consumed as exact candidate bytes from a clean environment; launch-capacity.v1 is produced and tested (four fixed standard-2 slots, no per-account instance creation, idle sleep/wake, pre-dispatch refusal vs unknown dispatched outcome, control-slot reserve, Vectorize/R2 reservation thresholds at 60/70/80/90%).

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-21.90 (full, including the Launch configuration acceptance subsection (launch-capacity.v1, PG-26)): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\21-cloud-host-and-persistence.md, anchor rule-wp-21.90
- WP-21:6-impacts-migration-compatibility-manife §6 Impacts -- migration/compatibility manifests include source/schema/plan/ABI/runtime versions (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\21-cloud-host-and-persistence.md, package-level obligation

Entry condition: adoption slice ADOPT.07.cloud is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] CLOUD.39: package task delivered
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
- [integration] CLOUD.70: final candidate build

Permitted write scope: Cloud:artifacts/candidate/**
Shared resources (follow the owner protocol): RES-cloud-deployment (append): Bindings are added by the owning module task in its own section, and the Cloud integration owner resolves ordering conflicts at merge. Any task that runs against the deployed test environment holds the lease `leases/res-cloud-deployment` for that live run only, whatever mode it declares for its binding edits; production deployment belongs to release tasks.
Unblocks: REL.06

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): package/contract/owner/version compatibility, failure/recovery and the real boundaries above; publish/promote only the tested immutable bytes in the producer CI sequence (matches the existing candidate->verify->deploy CI job sequence)
Completion evidence for the ledger: cold-start and measured cost inputs; PG-26 explicitly cannot close on a localhost benchmark
Notes: Gate: PG-26. A localhost benchmark cannot close it per WP-21.90's own text. Planning note 2026-10-09 (P2-026; S4, S16(c)): kept with its Vectorize threshold legs, because the semantic search leg is V1; the classifier removal of those legs is not applied.
```

```text
Execute ArcForges delivery task CLOUD.11 — Core identity model (realm, user, authIdentity, single-owner workspace).

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\cloud.md (anchor task-cloud-11).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/cloud-11 (python tools/delivery.py claim CLOUD.11 --worker <name>); task branch task/cloud-11 in Cloud; ledger record ledger/tasks/cloud-11.md.
Kind/size: service/M. Baseline: not-started.
Outcome: Realm, user, authentication identity and single-owner workspace exist with ownership as a direct workspace.owner_user_id check; no membership/role/seat table exists anywhere in schema, contracts or operations.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-22.00 (all work except the parts mapped to CLOUD.20 and CLOUD.72): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\22-identity-workspace-and-device.md, anchor rule-wp-22.00

Entry condition: adoption slice ADOPT.07.cloud is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] CLOUD.02: module boundary + D1 plan bridge to implement the Identity module against
- [artifact] CLOUD.03: physical D1 schema/migration runner for identity.* tables
- [artifact] CLOUD.06: the shared atomic family engine, since core identity operations (enrollment, workspace provisioning) are shared-transaction families
- [artifact] CLOUD.04: the commit tail (receipt, outbox event and change record) that every module write plan declares
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Cloud:src/ArcForges.Cloud.Modules.Identity/Core/** (the core model in the real one-project-per-module layout: Domain, Application and Infrastructure as folders and namespaces of the existing Identity project, internal types only, plus Cloud:src/ArcForges.Cloud.Modules.Identity/IdentityModule.cs, the project file's InternalsVisibleTo item and its lock file; the Workspace single-owner provisioning has no other owning task in the graph, so the minimal workspace owner model and its provisioning statements are carried here); Cloud:storage/plans/identity/** (the reviewed named plans of the identity owner over identity_ tables, each declaring its commit tail), Cloud:storage/plans/families.json (append the `account-enrollment` family) and Cloud:storage/plans/families/account-enrollment.* (the family plan of enrollment with default workspace provisioning, statements by module: identity, workspace, platform) and the generated Cloud:storage/plans/families.expanded.json, Cloud:src/ArcForges.Cloud.Storage.D1/PlanManifest.g.cs and Cloud:worker/storage/plans.generated.ts (regenerated after rebase; RES-cloud-storage-plans, RES-shared-transaction-families); Cloud:tests/ArcForges.Cloud.Tests/Identity/** and Cloud:tests/ArcForges.Cloud.Tests/Vectors/identity-*.json and Cloud:tests/worker/identity-*.test.ts and Cloud:tests/worker/support/identity-*.ts (domain, application and structural tests, the SQLite oracle that runs the identity plans and the enrollment family on the real migrations, new files only; and only the minimal edits of existing files that the new plans and family require: the manifest-identity recomputation of Cloud:tests/ArcForges.Cloud.Tests/ExactValueTests.cs (which must skip the family plans and add their independently recomputed identities), the pinned Worker bundle hash and size of Cloud:tests/worker/release-provenance.test.ts (the plan dictionary is bundled), and Cloud:tests/worker/storage-plan-ownership.test.ts (which must skip the family plans, a shared family plan not being an owner plan), Cloud:tests/worker/storage-plans-generator.test.ts (the temporary root of its stale-output case needs the physical manifest once a family plan exists, and the realm-level identity reads are named beside the realm-level platform plans) and the layered-module list of the architecture policy host in Cloud:tests/ArchitectureTests/**); Cloud:eng/verification/storage-plans.ts (only the print width of the generated family expansion JSON, 100 like the repository's Prettier configuration: the registry shipped empty, so the generated file was never formatted, and format:check fails on the first family plan) and Cloud:eng/verification/d1-identity-local.ts (new: the opt-in local run of the identity plans and the enrollment family on workerd's D1 under Miniflare) and Cloud:package.json (only the new npm script and the new test files in the test list); Cloud:.dockerignore (only the admission rule of the new Identity source folder, if the image build context does not already admit it); Cloud:eng/policy/dependency-policy.json and Cloud:eng/policy/dependency-reviews/cloud-11-*.json (new immutable successor chained from the then-active receipt, only because hash-bound project and release inputs change; no coordinate, integrity value or closure entry changes); Cloud:eng/provenance/** (immutable successor release profile, Worker bundle and runtime-notice records only where an existing record binds an input this task changes, the first-party inventory files.json and the deterministic NOTICE.txt); Cloud:docs/identity-core.md (new, factual description of the realm, user, authentication identity and single-owner workspace model, the plans and the enrollment family, and what each check proves and does not) and Cloud:docs/storage-plans.md and Cloud:docs/shared-families.md and Cloud:AGENTS.md (only factual pointers)
Shared resources (follow the owner protocol): RES-cloud-d1-migrations (append): One global D1 migration sequence: each module task authors migrations under its module prefix; the integration owner assigns the global sequence number at merge, regenerates the plan manifest and rejects edits to merged migrations; the migrator applies in sequence with receipts.; RES-cloud-storage-plans (append): Each module owns its own plan directory; the plan-manifest hash is regenerated by the author after rebase and checked in CI.; RES-shared-transaction-families (append): Adding a participant to a shared atomic family is a design change through the Architecture Owner; module tasks implement only their declared participation.
Unblocks: CLOUD.12, CLOUD.13, CLOUD.16, CLOUD.19, CLOUD.20, CLOUD.72, CLOUD.84, GOV.16, SRCH.03

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): offline structural tests: identity-change continuity, no membership/role/invitation/seat concept anywhere, no capability treats an auth identity as a user; AOT compile
Completion evidence for the ledger: identity-continuity and structural-separation test results
Notes: First real module built on the WP-21 foundation; unlocks the rest of WP-22. Planning repair 2026-10-05: the write scope named a layout (`src/Cloud/...`) that does not exist and could not hold the plans, the family, the tests or the successor records the task needs, so it is bound to the real layout (precedents: CLOUD.03, CLOUD.06, COM.05). Decisions recorded in this repair (raised to the Architecture Owner, D-001, in the pull request): (1) a realm is deployment configuration, not a table (one D1 authority per realm, model 00 section 6.1.1; model 01 declares `realm_id` columns and no realm table), so the core model carries a realm value and every plan and rule scopes by it; (2) no task in the graph owns the Workspace module's tables, so the single-owner workspace provisioning is carried here, as the family statements of module `workspace` in the enrollment family and the minimal workspace model of the Identity core; (3) the enrollment row of the shared units of work (data model 00 section 6.1.1, rule su-01 in docs/architecture/data-model/00-data-model-overview.md: 'Authentication/enrollment completion and default workspace provisioning') lists Device, Entitlement and Notification, which belong to CLOUD.12/13/19 and the grant tasks, so the registered `account-enrollment` family declares Identity and Workspace as required participants and Device, Entitlement and Notification as conditional on the completion that creates a session, applies configured initial grants or notifies, and the later tasks append their own plans of the same family; (4) the module cannot reference the plan bridge, so the typed bridge from the module's statements to a plan call is the Abstractions-level port that COM.16 delivers; binding the Identity store port (IIdentityStore) to it, the production identifier source and the receipt reused-identifier mapping are owned by CLOUD.72 (planning repair 2026-10-05, after this task completed without a production store; CLOUD.12 starts after CLOUD.72), and this task proves the plans against the real migrations and the shared vectors instead; (5) the plans declare the commit tail that CLOUD.04 delivered, so a CLOUD.04 artifact start edge is added (CLOUD.04 is complete, so it changes no ordering). No membership, role, invitation or seat concept is added; the structural tests that forbid it are part of this task. Planning repair 2026-10-08 (DLV-34; P2-021): the identity plans under storage/plans/identity move to C# under CLOUD.84; the model, rules, service and plans are unchanged. Outcome, validation and evidence above are recorded history and are unchanged.
```

```text
Execute ArcForges delivery task CLOUD.12 — Native and browser authentication with Postmark/SES mail adapters (live delivery evidence blocked-external).

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\cloud.md (anchor task-cloud-12).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/cloud-12 (python tools/delivery.py claim CLOUD.12 --worker <name>); task branch task/cloud-12 in Cloud; ledger record ledger/tasks/cloud-12.md.
Kind/size: service/L. Baseline: not-started.
Outcome: Native authorize/token PKCE ceremony and minimal browser login UI work with passkey/email and configured self-host OIDC/password; real Postmark-primary/SES-secondary delivery and outcome adapters are delivered as real adapters, with test doubles used only inside tests; live provider delivery and recovery evidence is a blocked-external input under P2-025 that gates completion, not delivery.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-22.01 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\22-identity-workspace-and-device.md, anchor rule-wp-22.01

Entry condition: adoption slice ADOPT.07.cloud is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] CLOUD.11: the core identity/authIdentity model to attach auth methods to
- [artifact] CLOUD.72: the production Identity store and identifier source over the plan-execution port, including the account-enrollment family call and the replay mapping
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Cloud:src/Cloud/ArcForges.Cloud.Modules.Identity/Auth/**; Cloud:src/Cloud/ArcForges.Cloud.Modules.Notification/**
Permitted substitutes (never real integration evidence): SUB-postmark-ses-test-recordings: Deterministic refusal, unknown-outcome and callback regression cases only; runtime registration is forbidden and live delivery is proven by the same task. Real producer ['CLOUD.12']; removed by CLOUD.12
Unblocks: CLOUD.15, CLOUD.17, CLOUD.18, CLOUD.20, CLOUD.68, OPS.09, WEB.10

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline checks in CI (P2-017): PKCE/state/redirect/code-replay, Credential Manager/RP origin fixtures, refresh contention and revocation, and the Postmark-primary/SES-secondary delivery, recovery and prepared-secondary tests. Test doubles of the mail providers are used only inside these tests: they serve as delivery evidence only inside these tests and are never completion evidence. Completion evidence is local opt-in only: live Postmark/SES send and recovery runs and real provider identity flow results, with no hosted live-service CI (P2-017). These are blocked-external under P2-025, gate completion only, and do not gate delivery.
Completion evidence for the ledger: Delivery evidence: adapter and flow tests with test doubles inside tests only, plus the recorded external-input list (Postmark/SES sender accounts and notify-subdomain DNS, blocked-external per P2-025). Completion evidence, blocked-external until executed: real provider identity flow results and live Postmark/SES delivery and recovery results, never replaced by a stub acceptance.
Notes: Must-be-real-early per implementation-sequence §3 ('Identity, refresh/session contention and real email delivery/recovery at WP22' is explicitly listed as Must be real early, not Push-until-later). Keep this must-be-real-early placement; do not move it later. Planning repair 2026-10-05: starts after CLOUD.72, which binds the Identity store and identifier source to the plan-execution port; this task binds its own Auth and Notification stores the same way. Pattern for every module (decided by the CLOUD.72 planning repair, 2026-10-05): a module project references only the Abstractions project, so each module task binds its own live store itself, under its own Persistence folder, as an internal class written against the Abstractions plan-execution port (IModulePlanPort, COM.16) and registered in the module's own Register entry with the port created for its own descriptor (IModulePlanPortFactory.For); a call to a shared transaction family goes through the Abstractions family port that CLOUD.72 adds. No module task may leave its store unbound while declaring a service that needs one. The write scope above still names the nonexistent `src/Cloud/...` layout; its claimant binds it to the real layout (precedents: CLOUD.03, CLOUD.06, CLOUD.11). Planning repair 2026-10-08 (DLV-34; P2-025): outcome, validation and evidence are re-specified in place so the task can be delivered with real adapters and test doubles used only in tests, while completion stays blocked-external until live Postmark/SES send and recovery evidence is recorded. Acceptance is preserved, not removed or passed. The complete-edge dependents CLOUD.20, CLOUD.68 and WEB.10 inherit this completion block; their owners record it on their own records. CLOUD.15, CLOUD.17, CLOUD.18 and OPS.09 start on CLOUD.12 and need only its delivery. Planning repair 2026-10-09 (P2-026; scope correction, brief section 11 S19(c)): reduced: the official-realm password path and the official social or enterprise sign-in methods are out of scope, not completed (ID-21, ID-24, ID-26); self-host OIDC, local password and the self-host enterprise identity provider stay as operator-configured providers (ID-25, C-08).
```

```text
Execute ArcForges delivery task CLOUD.13 — Device, installation, instance and session (four distinct concepts).

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\cloud.md (anchor task-cloud-13).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/cloud-13 (python tools/delivery.py claim CLOUD.13 --worker <name>); task branch task/cloud-13 in Cloud; ledger record ledger/tasks/cloud-13.md.
Kind/size: service/M. Baseline: not-started.
Outcome: Device, installation, instance and session are four distinct concepts with four lifecycles; device identity is stable but not a hardware fingerprint; device revocation cascades to sessions and push registrations.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-22.02 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\22-identity-workspace-and-device.md, anchor rule-wp-22.02

Entry condition: adoption slice ADOPT.07.cloud is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] CLOUD.11: the core identity model a device/session attaches to
- [artifact] CLOUD.06: the shared atomic family engine, since device revocation is a named shared-transaction family
- [artifact] CLOUD.72: the Abstractions family port and the Identity production store, to execute the account-enrollment and device-revocation families and bind the Device store over the plan-execution port
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Cloud:src/Cloud/ArcForges.Cloud.Modules.Identity/Device/**
Shared resources (follow the owner protocol): RES-cloud-d1-migrations (append): One global D1 migration sequence: each module task authors migrations under its module prefix; the integration owner assigns the global sequence number at merge, regenerates the plan manifest and rejects edits to merged migrations; the migrator applies in sequence with receipts.; RES-shared-transaction-families (append): Adding a participant to a shared atomic family is a design change through the Architecture Owner; module tasks implement only their declared participation.
Unblocks: AND.07, CLOUD.14, CLOUD.15, CLOUD.19, CLOUD.20, CLOUD.21, DEV.01

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): offline structural distinction-matrix tests; revocation-cascade tests; hardware-change survival test
Completion evidence for the ledger: four-concept distinction matrix and revocation cascade results
Notes: Planning repair 2026-10-05: starts after CLOUD.72 (the family port and the plan-execution port it builds on). Pattern for every module (decided by the CLOUD.72 planning repair, 2026-10-05): a module project references only the Abstractions project, so each module task binds its own live store itself, under its own Persistence folder, as an internal class written against the Abstractions plan-execution port (IModulePlanPort, COM.16) and registered in the module's own Register entry with the port created for its own descriptor (IModulePlanPortFactory.For); a call to a shared transaction family goes through the Abstractions family port that CLOUD.72 adds. No module task may leave its store unbound while declaring a service that needs one. The write scope above still names the nonexistent `src/Cloud/...` layout; its claimant binds it to the real layout.
```

```text
Execute ArcForges delivery task CLOUD.14 — Device trust and remote gating.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\cloud.md (anchor task-cloud-14).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/cloud-14 (python tools/delivery.py claim CLOUD.14 --worker <name>); task branch task/cloud-14 in Cloud; ledger record ledger/tasks/cloud-14.md.
Kind/size: service/S. Baseline: not-started.
Outcome: Trust levels per device exist with remote access defaulting to off; raising trust requires an explicit act with step-up; remote capability is derived from trust, never from mere session possession.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-22.03 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\22-identity-workspace-and-device.md, anchor rule-wp-22.03

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

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\cloud.md (anchor task-cloud-15).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/cloud-15 (python tools/delivery.py claim CLOUD.15 --worker <name>); task branch task/cloud-15 in Cloud; ledger record ledger/tasks/cloud-15.md.
Kind/size: service/M. Baseline: not-started.
Outcome: Step-up challenges exist for the enumerated sensitive operations, bounded validity window, no app-unlock substitution; step-up state is per session and per operation class.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-22.04 (the step-up mechanism itself and coverage for Cloud/Identity-owned sensitive operations (credential change, recovery, deletion, trust elevation); full coverage across every enumerated operation in every module is completed as each owning module wires it in -- see IM.step-up-cross-product-coverage): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\22-identity-workspace-and-device.md, anchor rule-wp-22.04

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

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\cloud.md (anchor task-cloud-16).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/cloud-16 (python tools/delivery.py claim CLOUD.16 --worker <name>); task branch task/cloud-16 in Cloud; ledger record ledger/tasks/cloud-16.md.
Kind/size: service/M. Baseline: not-started.
Outcome: patEligible/scopes metadata, hash-only token storage, expiry/revocation and one-time display after step-up are implemented; the actor chain is preserved and customer tokens are denied on operator/internal/local boundaries.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-22.05 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\22-identity-workspace-and-device.md, anchor rule-wp-22.05

Entry condition: adoption slice ADOPT.07.cloud is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] CLOUD.11: the core identity model a token belongs to
- [artifact] COM.16: the generic plan-execution port, to bind the token store to D1
Completion prerequisites (may start earlier; cannot complete before these are complete):
- [integration] CLOUD.15: the step-up mechanism, since one-time PAT display happens after step-up

Permitted write scope: Cloud:src/ArcForges.Cloud.Modules.Identity/Tokens/** (the real one-project-per-module path; the Cloud tree has no src/Cloud directory)
Unblocks: CLOUD.19, CLOUD.20, CLOUD.63, EXT.06, EXT.08

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): offline enumeration of eligible/denied methods from the generated manifest; cookie+bearer conflict, scope escalation and agent-substitution negative vectors
Completion evidence for the ledger: no missing/default PAT metadata, no generic token bypass
Notes: Planning repair 2026-10-05: starts after COM.16 (the plan-execution port). Pattern for every module (decided by the CLOUD.72 planning repair, 2026-10-05): a module project references only the Abstractions project, so each module task binds its own live store itself, under its own Persistence folder, as an internal class written against the Abstractions plan-execution port (IModulePlanPort, COM.16) and registered in the module's own Register entry with the port created for its own descriptor (IModulePlanPortFactory.For); a call to a shared transaction family goes through the Abstractions family port that CLOUD.72 adds. No module task may leave its store unbound while declaring a service that needs one. The write scope above still names the nonexistent `src/Cloud/...` layout; its claimant binds it to the real layout. Planning repair 2026-10-08 (DLV-34; handoff from the CLOUD.72 review): the write path is restated for the real one-project-per-module layout (src/ArcForges.Cloud.Modules.Identity/Tokens/**); the earlier src/Cloud path does not exist in the Cloud tree. The Tokens folder does not overlap CLOUD.72's Persistence folder, IdentityModule.cs or Core folder. CLOUD.16 writes no IdentityModule.cs; if its token store must be bound in IdentityModule.cs, that file belongs to CLOUD.72 and the write must be declared with a start edge on CLOUD.72 by the CLOUD.16 owner. Outcome, validation and evidence are unchanged.
```

```text
Execute ArcForges delivery task CLOUD.17 — Recovery, account states and deletion.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\cloud.md (anchor task-cloud-17).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/cloud-17 (python tools/delivery.py claim CLOUD.17 --worker <name>); task branch task/cloud-17 in Cloud; ledger record ledger/tasks/cloud-17.md.
Kind/size: service/M. Baseline: not-started.
Outcome: Recovery flows resist modelled abuse; account states (active/restricted/suspended/pending-deletion) have defined capability; deletion has a grace period, explicit scope of what is/isn't deleted, and never touches local data.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-22.06 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\22-identity-workspace-and-device.md, anchor rule-wp-22.06

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

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\cloud.md (anchor task-cloud-18).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/cloud-18 (python tools/delivery.py claim CLOUD.18 --worker <name>); task branch task/cloud-18 in DesktopPlatform; ledger record ledger/tasks/cloud-18.md.
Kind/size: service/M. Baseline: not-started.
Outcome: System browser, per-product redirects, secure storage and installation-bound tokens are integrated into Platform client primitives; each client owns its own session, no token sharing/device SSO.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-22.07 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\22-identity-workspace-and-device.md, anchor rule-wp-22.07

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

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\cloud.md (anchor task-cloud-19).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/cloud-19 (python tools/delivery.py claim CLOUD.19 --worker <name>); task branch task/cloud-19 in Cloud; ledger record ledger/tasks/cloud-19.md.
Kind/size: service/L. Baseline: not-started.
Outcome: The same-origin browser adapter runs in the AOT host with random hashed session/preauth/CSRF records, exact Origin checks, idle/absolute expiry, lowest-trust browser installation and one-use auth flow, with explicit cookie parsing/writing (no ASP.NET Data Protection/cookie-auth middleware); the full typed account surface is wired through the same owner ports.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-22.08 (full, including the 'Required implementation and closure from the final review' paragraph (complete typed account surface: profile/email, recovery-code set, scoped PAT, credential rename, session listing, four sign-out scopes, per-installation browser authorization, remote capability policy, restricted deletion-cancel reauthentication)): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\22-identity-workspace-and-device.md, anchor rule-wp-22.08
- WP-22:browser-session-evidence-note-wp-22-08-m Browser-session evidence note (WP-22.08 must pass before WP-23 consumes its contract; a written P2-003 decision alone is insufficient) (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\22-identity-workspace-and-device.md, package-level obligation

Entry condition: adoption slice ADOPT.07.cloud is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] CLOUD.01: the AOT host pipeline to implement the /session/* routes in
- [artifact] CLOUD.11: identity core model
- [artifact] CLOUD.13: device/installation/session model, since browser sessions are the lowest-trust browser installation
Completion prerequisites (may start earlier; cannot complete before these are complete):
- [integration] CLOUD.16: PAT mechanism for the scoped-PAT account surface
- [integration] CLOUD.17: recovery/deletion mechanism for the deletion-cancel reauthentication surface

Permitted write scope: Cloud:src/Cloud/ArcForges.Cloud.Host/Session/**; Cloud:src/Contracts/Public/ArcForges.Contracts.PublicApi.Identity/**
Unblocks: AND.07, CLOUD.20, CLOUD.21, CLOUD.26, CLOUD.29, PRF.12, WEB.11, WEB.30

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): opt-in local + real D1 tests: one-use challenge, lost-login response, idle-vs-revoke race, expiry, replica failover, exact Origin/CSRF on unsafe RPC/session/stream/object operations, native-token route refusal, gRPC-Web stream authorization, two-products-one-OS-user isolation
Completion evidence for the ledger: one server-owned session authority, no JS bearer, no cross-origin reuse or session resurrection; real database/concurrency, origin/CSRF/expiry and multi-replica results
Notes: Gate: PG-23 (this task's contribution; WP-23.05 contributes the other side). Feeds WP-23 and full portal acceptance -- WP-23 cannot consume this contract until it passes; a written P2-003 decision alone is insufficient per the WP text.
```

```text
Execute ArcForges delivery task CLOUD.20 — Owned-artifact closure and real integration.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\cloud.md (anchor task-cloud-20).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/cloud-20 (python tools/delivery.py claim CLOUD.20 --worker <name>); task branch task/cloud-20 in Cloud; ledger record ledger/tasks/cloud-20.md.
Kind/size: integration/M. Baseline: not-started.
Outcome: Native/Android bearer sessions, same-origin Web opaque sessions, passkeys/recovery, workspace/device rules and authenticated CF authorization ports work end-to-end using selected AOT-compatible components; real publish-mode auth/session/CSRF/origin/rotation/revocation tests pass including stale CF requests and browser credential secrecy.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-22.90 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\22-identity-workspace-and-device.md, anchor rule-wp-22.90
- WP-22:p2-010-required-behavior-and-closure-app P2-010 required behavior and closure appendix (initial enrollment/recovery/provider/account/SSO methods wired end-to-end in client journeys) (P2-010 required behavior and closure appendix (initial enrollment/recovery/provider/account methods wired end-to-end in client journeys; the ID-26 SSO methods are out of scope under P2-026)): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\22-identity-workspace-and-device.md, package-level obligation
- WP-22.00 (real identity/session implementation): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\22-identity-workspace-and-device.md, anchor rule-wp-22.00

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
- [integration] CLOUD.72: the production Identity store and identifier source over the plan-execution port

Permitted write scope: Cloud:artifacts/candidate/**
Unblocks: REL.06

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): real publish-mode auth/session/CSRF/origin/rotation/revocation tests including stale CF requests and browser credential secrecy
Completion evidence for the ledger: owned artifact and real-integration receipt: source commit, producer version, candidate hashes, actual runtime/OS/device/provider, scenario, result, limitations, real-vs-fixture status
Notes: Merged duplicate integration or closure task formerly proposed as CON.94. Planning repair 2026-10-09 (P2-026; scope correction): reduced: the SSO methods wired end to end in the P2-010 closure appendix are out of scope, not completed (ID-26); enrollment, recovery, provider, account and passkey or email methods are retained.
```

```text
Execute ArcForges delivery task CLOUD.21 — Public endpoint mapping and validation.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\cloud.md (anchor task-cloud-21).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/cloud-21 (python tools/delivery.py claim CLOUD.21 --worker <name>); task branch task/cloud-21 in Cloud; ledger record ledger/tasks/cloud-21.md.
Kind/size: service/M. Baseline: not-started.
Outcome: Generated proto service methods are registered with exact request/reply/semantic validation from the registry; binary gRPC-Web unary calls and declared server streams go through the same owner handlers; owner mutations and the Sync allowlist are mapped exactly; no ad-hoc REST business API exists.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-23.00 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\23-public-api-and-generated-clients.md, anchor rule-wp-23.00
- WP-22:browser-session-evidence-note-wp-22-08-m Browser-session evidence note (WP-22.08 must pass before WP-23 consumes its contract; a written P2-003 decision alone is insufficient) (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\22-identity-workspace-and-device.md, package-level obligation

Entry condition: adoption slice ADOPT.07.cloud is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [contract] CON.91: the handwritten-proto-generated service/method definitions to register (D-009 authority)
- [artifact] CLOUD.13: session model and native session validation
Completion prerequisites (may start earlier; cannot complete before these are complete):
- [integration] CLOUD.19: the browser cookie-session adapter and native session validation to authenticate requests before they reach a handler

Permitted write scope: Cloud:src/Cloud/ArcForges.Cloud.PublicApi/Endpoints/**
Unblocks: AND.04, CLOUD.22, CLOUD.23, CLOUD.24, CLOUD.25, CLOUD.28, CLOUD.29, CLOUD.64, CLOUD.66, CLOUD.68, CLOUD.84, COM.13, PRF.05, PRF.08, PRF.11, PRF.12, SIM.05

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): offline + opt-in tests: each method category through native C# and browser Grpc.Net.Client.Web (binary gRPC-Web) transports, malformed/unknown request values, denied scope before handler
Completion evidence for the ledger: every selected operation has a concrete typed endpoint and owner; no ad-hoc REST business API
Notes: Planning repair 2026-10-08 (DLV-34; P2-021): the TypeScript transport check is replaced by the browser Grpc.Net.Client.Web transport tested from C#; the endpoint and owner-handler rules are unchanged.
```

```text
Execute ArcForges delivery task CLOUD.22 — Typed protocol and error mapping.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\cloud.md (anchor task-cloud-22).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/cloud-22 (python tools/delivery.py claim CLOUD.22 --worker <name>); task branch task/cloud-22 in Cloud; ledger record ledger/tasks/cloud-22.md.
Kind/size: service/M. Baseline: not-started.
Outcome: Generated ArcResult domain errors and gRPC-Web transport statuses/trailers are mapped exactly under registry 04; ProblemDetails is limited to documented HTTP exceptions.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-23.01 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\23-public-api-and-generated-clients.md, anchor rule-wp-23.01

Entry condition: adoption slice ADOPT.07.cloud is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] CLOUD.21: the endpoint registration to attach error mapping to
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Cloud:src/Cloud/ArcForges.Cloud.PublicApi/Errors/**
Unblocks: CLOUD.26, CLOUD.28, CLOUD.64, CLOUD.66, PRF.05, PRF.08, PRF.11, PRF.12

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): offline + opt-in tests: HTTP200-with-error-trailers, partial frame, 64-bit values, deadline/cancel-after-dispatch, command-receipt reconciliation
Completion evidence for the ledger: every C# client (native, browser gRPC-Web and MAUI Android) distinguishes transport uncertainty from a domain refusal
Notes: Planning repair 2026-10-08 (DLV-34; P2-021): the client-language list in the evidence is restated for C# clients: native, browser gRPC-Web (Blazor WebAssembly) and MAUI Android. The error-mapping and transport rules under registry 04 are unchanged.
```

```text
Execute ArcForges delivery task CLOUD.23 — Typed queries and revision preconditions.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\cloud.md (anchor task-cloud-23).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/cloud-23 (python tools/delivery.py claim CLOUD.23 --worker <name>); task branch task/cloud-23 in Cloud; ledger record ledger/tasks/cloud-23.md.
Kind/size: service/M. Baseline: not-started.
Outcome: Opaque scope-bound PageRequest cursors, registered typed filters and RequestMeta expected-owner-revision preconditions work; no ETag/If-Match for business RPC.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-23.02 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\23-public-api-and-generated-clients.md, anchor rule-wp-23.02

Entry condition: adoption slice ADOPT.07.cloud is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] CLOUD.21: endpoint registration to add query/cursor semantics to
- [contract] CON.91: the accepted foundation PageRequest/PageState and exact-value records
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Cloud:src/Cloud/ArcForges.Cloud.PublicApi/Queries/**
Unblocks: CLOUD.28, COM.06

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): offline + opt-in tests: wrong product/scope cursor, stale revision, page limits, unsupported filter/version, exact scalar vectors
Completion evidence for the ledger: generated clients exercise the authoritative RPC query/revision rules without REST aliases
```

```text
Execute ArcForges delivery task CLOUD.24 — Idempotency and rate limiting.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\cloud.md (anchor task-cloud-24).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/cloud-24 (python tools/delivery.py claim CLOUD.24 --worker <name>); task branch task/cloud-24 in Cloud; ledger record ledger/tasks/cloud-24.md.
Kind/size: service/M. Baseline: not-started.
Outcome: State-changing requests accept a command identity and produce exactly one effect under retry; rate limits apply per identity and per capability class with typed refusals carrying retry guidance.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-23.03 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\23-public-api-and-generated-clients.md, anchor rule-wp-23.03

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

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\cloud.md (anchor task-cloud-25).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/cloud-25 (python tools/delivery.py claim CLOUD.25 --worker <name>); task branch task/cloud-25 in Cloud; ledger record ledger/tasks/cloud-25.md.
Kind/size: service/M. Baseline: not-started.
Outcome: The complete generated upload/status/ticket/verification/owner-promotion schema and permission/error envelope is registered and exercised through declared protocol fixtures; every endpoint's real owner/fixture/replacement WP is recorded.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-23.04 (full (schema/transport/fixture boundary only; real R2 multipart behavior is WP-25.05)): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\23-public-api-and-generated-clients.md, anchor rule-wp-23.04

Entry condition: adoption slice ADOPT.07.cloud is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] CLOUD.21: endpoint registration to add resource-transport endpoints to
- [artifact] PRF.07: the minimal real R2 transport probe already proved by WP-06
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Cloud:src/Contracts/Public/ArcForges.Contracts.PublicApi.Resource/**; Cloud:fixtures/wire/publicapi/resource/**
Permitted substitutes (never real integration evidence): SUB-resource-transport-schema-fixtures: protocol/schema/permission/error envelope only, via declared fixtures -- release excludes the fixture handlers Real producer ['CLOUD.42']; removed by CLOUD.42
Unblocks: CLOUD.28, CLOUD.42

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): offline + opt-in tests: independent request/result/expiry/hash/denied-scope and encoded-body fixtures across the C# server, Blazor WebAssembly browser and MAUI Android consumers
Completion evidence for the ledger: no missing resource schema; no claim that WP-23 alone delivered Resource/R2 owner behavior
Notes: Planning repair 2026-10-08 (DLV-34; P2-021): the TypeScript and Kotlin fixture consumers are replaced by C# server, browser and MAUI consumers; the schema and fixture boundary are unchanged.
```

```text
Execute ArcForges delivery task CLOUD.26 — Generated C# clients (native and Grpc.Net.Client.Web browser) against Identity/Workspace/Device.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\cloud.md (anchor task-cloud-26).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/cloud-26 (python tools/delivery.py claim CLOUD.26 --worker <name>); task branch task/cloud-26 in Cloud; ledger record ledger/tasks/cloud-26.md.
Kind/size: service/L. Baseline: not-started.
Outcome: Released C# native, C# gRPC-Web browser (Grpc.Net.Client.Web, used by the Blazor WebAssembly profiles) and C# MAUI Android client consumers work against actual Identity/Workspace/Device endpoints with native single-flight refresh, Web cookie/CSRF/Origin handling and generation-scoped callbacks outside generated code; the MAUI Android consumer is evidenced through the PRF.12 completion edge; no TypeScript or Kotlin client is generated or released.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-23.05 (all work except the parts mapped to AND.07, WEB.30): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\23-public-api-and-generated-clients.md, anchor rule-wp-23.05

Entry condition: adoption slice ADOPT.07.cloud is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] CLOUD.19: the real browser cookie-session adapter to test the C# native and Grpc.Net.Client.Web browser clients' cookie/CSRF/Origin handling against
- [artifact] CLOUD.22: typed error mapping to test exact-value/error/header client conformance against
Completion prerequisites (may start earlier; cannot complete before these are complete):
- [integration] PRF.12: the PRF.12 MAUI Android release proof (unary, server stream, trailers, cancel and Keystore against the proof ingress) consuming the generated C# client; this carries the consumer scenario the superseded Kotlin proof PRF.10 would have covered

Permitted write scope: Cloud:src/BuildingBlocks/ArcForges.CloudClient/**; Cloud:tests/PublicApiContractTests/**
Unblocks: AND.07, CLOUD.27, CLOUD.28, PRF.12, WEB.30

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): offline + opt-in tests: independent exact-value/current-previous-major vectors, actual WP-22 session expiry/revoke/refresh, public/internal leak rejection
Completion evidence for the ledger: the C# native, C# browser gRPC-Web and C# MAUI Android client consumers work against the actual host; owner implementations replaced by WP-25/42/52 before full release
Notes: Gate: PG-23 (this task's client-side contribution; CLOUD.19 contributes the server side). Planning repair 2026-10-08 (DLV-34; P2-021): re-specified C#-first: the generated clients are C# only (native and gRPC-Web browser), per P2-021; the TypeScript and Kotlin generation is removed from this task. Validation, the single-flight refresh rules and the WP-23.05 mapping to AND.07 and WEB.30 are unchanged.
```

```text
Execute ArcForges delivery task CLOUD.27 — Compatibility window and bidirectional matrix.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\cloud.md (anchor task-cloud-27).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/cloud-27 (python tools/delivery.py claim CLOUD.27 --worker <name>); task branch task/cloud-27 in Cloud; ledger record ledger/tasks/cloud-27.md.
Kind/size: service/M. Baseline: not-started.
Outcome: The supported client window is declared with golden wire vectors per contract version; the compatibility matrix runs both directions (previous client vs current server, current client vs minimum supported server) and catches a deliberately breaking change.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-23.06 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\23-public-api-and-generated-clients.md, anchor rule-wp-23.06

Entry condition: adoption slice ADOPT.07.cloud is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] CLOUD.26: at least one released C# client kind (native, and Grpc.Net.Client.Web browser, as CLOUD.26 releases them) to build the matrix against; no TypeScript or Kotlin client is a matrix member under P2-021
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Cloud:fixtures/wire/publicapi/**; Cloud:tests/PublicApiContractTests/Compatibility/**
Unblocks: CLOUD.28

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): the bidirectional matrix; a negative test asserting a breaking change fails the matrix
Completion evidence for the ledger: bidirectional compatibility matrix passes and catches a deliberately breaking change
Notes: Planning repair 2026-10-08 (DLV-34; P2-021): the matrix's client members are the C# clients that CLOUD.26 releases (native and Grpc.Net.Client.Web browser); no TypeScript or Kotlin client is a matrix member. The supported window, golden vectors and the negative test are unchanged.
```

```text
Execute ArcForges delivery task CLOUD.28 — Owned-artifact closure and real integration.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\cloud.md (anchor task-cloud-28).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/cloud-28 (python tools/delivery.py claim CLOUD.28 --worker <name>); task branch task/cloud-28 in Cloud; ledger record ledger/tasks/cloud-28.md.
Kind/size: integration/L. Baseline: not-started.
Outcome: Real C#, browser (Blazor WebAssembly) and MAUI Android calls succeed against the AOT image with previous/current compatibility and complete operation mapping including auth, files and webhooks outside gRPC.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-23.90 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\23-public-api-and-generated-clients.md, anchor rule-wp-23.90
- WP-23:operator-contract-closure-appendix-cloud Operator contract closure appendix -- Cloud's own share: generate/implement every operation with its eight authorization fields, operator scope and OC-03 role binding, refuse public customer/PAT/agent access, verify distinct approver/stale hash/revision/configuration/role revocation/expiry/concurrent consumption/lost receipt; the financial owners (WP-42), configuration/policy owners (WP-44) and console join (WP-45) are NOT this task's obligation -- see IM.operator-contract-closure (Operator contract closure appendix -- Cloud's own share: generate/implement every operation with its eight authorization fields, operator scope and OC-03 role binding, refuse public customer/PAT/agent access, verify distinct approver/stale hash/revision/configuration/role revocation/expiry/concurrent consumption/lost receipt; the financial owners (WP-42), configuration/policy owners (WP-44) and console join (WP-45) are NOT this task's obligation -- see IM.operator-contract-closure): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\23-public-api-and-generated-clients.md, package-level obligation
- WP-23:browser-matrix-acceptance-appendix-cloud Browser matrix acceptance appendix -- Cloud's own share: prove generated transports support delayed-stream polling, refusal of unavailable required auth/step-up, safe-preview refusal, preserved pending work; WP-45/47/48/49/50's own operations/site/account/chat/production-hash evidence is NOT this task's obligation -- see IM.browser-matrix-acceptance (Browser matrix acceptance appendix -- Cloud's own share: prove generated transports support delayed-stream polling, refusal of unavailable required auth/step-up, safe-preview refusal, preserved pending work; WP-45/47/48/49/50's own operations/site/account/chat/production-hash evidence is NOT this task's obligation -- see IM.browser-matrix-acceptance): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\23-public-api-and-generated-clients.md, package-level obligation
- WP-23:operator-contract-closure-appendix-regis Operator contract closure appendix (registry04 §9 + model01 operator state; eight authorization fields, operator scope, OC-03 role binding) (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\23-public-api-and-generated-clients.md, package-level obligation
- WP-23:browser-matrix-acceptance-appendix-brows Browser matrix acceptance appendix (browser-support.v1, supported/degraded/blocked behavior for generated transports) (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\23-public-api-and-generated-clients.md, package-level obligation

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

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): real C#, browser and MAUI Android calls against the AOT image, previous/current compatibility, complete operation mapping including auth/files/webhooks outside gRPC
Completion evidence for the ledger: owned artifact and real-integration receipt per WP-23.90
Notes: Gate: PG-23 (joint with CLOUD.19/CLOUD.26). Planning repair 2026-10-08 (DLV-34; P2-021): the Kotlin consumer is replaced by the MAUI Android consumer (AND.40); the real-integration and compatibility rules are unchanged.
```

```text
Execute ArcForges delivery task CLOUD.29 — Stream connection and authentication (EventService.Watch/ExecutionService.WatchOutput shells).

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\cloud.md (anchor task-cloud-29).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/cloud-29 (python tools/delivery.py claim CLOUD.29 --worker <name>); task branch task/cloud-29 in Cloud; ledger record ledger/tasks/cloud-29.md.
Kind/size: service/M. Baseline: not-started.
Outcome: Public server-streaming shells for EventService.Watch and ExecutionService.WatchOutput exist with generated StreamFrame, re-authorizing current session/scope every 15s; real C#, browser (Blazor WebAssembly) and MAUI Android binary streams work with trailers/cancel/expiry; the browser uses binary server streaming through the .NET 10 browser streaming HttpClient, and if that is not observed in the Blazor proof (PRF.11) the grpc-web-text variant is accepted on server-stream routes only, as recorded in the wire registry; no client or bidirectional stream; no WebSocket path.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-24.00 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\24-realtime-and-reliable-events.md, anchor rule-wp-24.00

Entry condition: adoption slice ADOPT.07.cloud is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] CLOUD.21: the endpoint-mapping pattern to register server-streaming methods alongside unary ones
- [artifact] CLOUD.19: session authorization to re-check every 15s on the open stream
- [contract] CON.11: the StreamFrame/StreamPosition/ApplicationScope record definitions (contracts/10 §2)
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Cloud:src/Cloud/ArcForges.Cloud.PublicApi/Streams/**
Unblocks: AND.07, AND.40, CLOUD.30, CLOUD.34, CLOUD.36, DEV.01, DEV.14, PRF.06, PRF.12, WEB.30

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): opt-in real deployed C#, browser and MAUI Android binary stream tests: trailers/cancel/expiry, no WebSocket path, no client or bidirectional stream; if the grpc-web-text fallback is used on a browser server-stream route, the same trailers, cancel, expiry, no-WebSocket, no-client-stream and no-bidirectional-stream checks run on that text variant with equal acceptance, and its framing is recorded in the wire registry
Completion evidence for the ledger: real binary stream trailer/cancel/expiry results; and, if the text fallback is used, the same trailer/cancel/expiry and no-WebSocket/no-bidirectional results for the grpc-web-text server-stream route
Notes: Planning repair 2026-10-08 (DLV-34; P2-021): the Kotlin consumer is replaced by MAUI Android. The streaming transport follows the browser limits recorded for P2-021: unary and server streaming only; the grpc-web-text fallback applies only where the Blazor proof shows binary server streaming does not work. The stream-authorization and expiry rules are unchanged.
```

```text
Execute ArcForges delivery task CLOUD.30 — Scoped subscription (owner/product/filter/recovery-generation binding).

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\cloud.md (anchor task-cloud-30).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/cloud-30 (python tools/delivery.py claim CLOUD.30 --worker <name>); task branch task/cloud-30 in Cloud; ledger record ledger/tasks/cloud-30.md.
Kind/size: service/M. Baseline: not-started.
Outcome: The feed is bound to owner/product/filter/recovery generation, one events stream plus two output streams per foreground profile; mixed-product/unauthorized feeds are refused; account-security identifiers stay separate.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-24.01 (all work except the parts mapped to DEV.14): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\24-realtime-and-reliable-events.md, anchor rule-wp-24.01

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

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\cloud.md (anchor task-cloud-31).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/cloud-31 (python tools/delivery.py claim CLOUD.31 --worker <name>); task branch task/cloud-31 in Cloud; ledger record ledger/tasks/cloud-31.md.
Kind/size: service/M. Baseline: not-started.
Outcome: Sequence/hash/offset cursors and snapshot high-water recovery work per annex 10; the DO is a projection backed by the D1 outbox, never a second business authority.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-24.02 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\24-realtime-and-reliable-events.md, anchor rule-wp-24.02

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

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\cloud.md (anchor task-cloud-32).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/cloud-32 (python tools/delivery.py claim CLOUD.32 --worker <name>); task branch task/cloud-32 in Cloud; ledger record ledger/tasks/cloud-32.md.
Kind/size: service/S. Baseline: not-started.
Outcome: Poll/readOutput works with the same owner/cursor profile as the stream, replacing the old HTTP task-stream endpoint; a blocked stream recovers through a real unary read without inventing completion.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-24.03 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\24-realtime-and-reliable-events.md, anchor rule-wp-24.03

Entry condition: adoption slice ADOPT.07.cloud is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] CLOUD.31: cursor/gap handling to read from in the unary fallback
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Cloud:src/Cloud/ArcForges.Cloud.PublicApi/Streams/Fallback/**
Unblocks: CLOUD.36, PRF.06

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): opt-in test: blocked stream recovers through real unary read without invented completion
Completion evidence for the ledger: blocked-stream real-recovery result
Notes: AI terminal bodies (ChatTurn/Task execution output) arrive via WP-52, not this task.
```

```text
Execute ArcForges delivery task CLOUD.33 — Publication and wake (D1 outbox to bounded DO feed via Queues).

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\cloud.md (anchor task-cloud-33).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/cloud-33 (python tools/delivery.py claim CLOUD.33 --worker <name>); task branch task/cloud-33 in Cloud; ledger record ledger/tasks/cloud-33.md.
Kind/size: service/M. Baseline: not-started.
Outcome: The committed D1 outbox publishes into the bounded DO feed with wake hints delivered via Queues; contiguous watermark, no skipped commit, duplicate queue event is safe; no business ownership lives in the DO.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-24.04 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\24-realtime-and-reliable-events.md, anchor rule-wp-24.04

Entry condition: adoption slice ADOPT.07.cloud is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] CLOUD.31: the DO projection to publish into
- [artifact] CLOUD.05: the finite-durable-job/Queue wake mechanism
- [artifact] CLOUD.69: the Cloud-side correlation seam for event publication
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Cloud:src/Cloud/ArcForges.Cloud.EventFeed/Publisher/**
Shared resources (follow the owner protocol): RES-cloud-leased-singletons (append): Each publication watermark, Durable Object alarm namespace and R2 prefix has exactly one owning module task; others use its published port; names are reserved in the binding plan before first use.
Unblocks: CLOUD.35, CLOUD.36, DEV.14

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): opt-in tests: contiguous watermark, no skipped commit, duplicate queue event safe
Completion evidence for the ledger: contiguous-watermark and duplicate-safety results
Notes: Planning repair 2026-10-05: the bounded DO feed and the events it publishes carry the originating correlation (Event.correlationId, contracts 03) through the CLOUD.69 seam; this is part of this task's own acceptance and of the real realtime hop that PLT.48's correlation scenario names as a later owner (no new write scope).
```

```text
Execute ArcForges delivery task CLOUD.34 — Bounded stream lifecycle.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\cloud.md (anchor task-cloud-34).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/cloud-34 (python tools/delivery.py claim CLOUD.34 --worker <name>); task branch task/cloud-34 in Cloud; ledger record ledger/tasks/cloud-34.md.
Kind/size: service/S. Baseline: not-started.
Outcome: 5-minute stream, 15s heartbeat, 45s silence and bounded jitter/queue limits are enforced; Android background closes streams and later refetches; slow-reader overflow resets rather than growing unbounded.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-24.05 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\24-realtime-and-reliable-events.md, anchor rule-wp-24.05

Entry condition: adoption slice ADOPT.07.cloud is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] CLOUD.29: the stream shell to bound the lifecycle of
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Cloud:src/Cloud/ArcForges.Cloud.PublicApi/Streams/Lifecycle/**
Unblocks: CLOUD.35, CLOUD.36, DEV.14, PRF.06

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): opt-in test: slow reader overflow resets, no unbounded memory or hibernation-cost claim
Completion evidence for the ledger: slow-reader overflow-reset result
```

```text
Execute ArcForges delivery task CLOUD.35 — Reusable stream consumer adapters.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\cloud.md (anchor task-cloud-35).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/cloud-35 (python tools/delivery.py claim CLOUD.35 --worker <name>); task branch task/cloud-35 in Cloud; ledger record ledger/tasks/cloud-35.md.
Kind/size: service/M. Baseline: not-started.
Outcome: Platform Cloud.Client and Contracts C# stream fixtures are published with typed lifecycle states and no UI-specific transport logic.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-24.06 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\24-realtime-and-reliable-events.md, anchor rule-wp-24.06

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
Notes: Planning repair 2026-10-08 (DLV-34; P2-021): the TypeScript and Kotlin stream fixtures retire under CON.40; the C# stream fixtures and the typed lifecycle states are the published surface.
```

```text
Execute ArcForges delivery task CLOUD.36 — Owned-artifact closure and real integration (tool-result acceptance).

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\cloud.md (anchor task-cloud-36).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/cloud-36 (python tools/delivery.py claim CLOUD.36 --worker <name>); task branch task/cloud-36 in Cloud; ledger record ledger/tasks/cloud-36.md.
Kind/size: integration/M. Baseline: not-started.
Outcome: Every WP-24 substep is complete and packaged; two distinct toolRequestIds in one attempt both persist and replay correctly for both Task and ChatTurn owners; a changed result under the same (toolRequestId, attemptId, commandId) refuses.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-24.90 (full, including the Tool-result acceptance subsection (toolRequestId dedup for Task and ChatTurn owners, command.reused_identifier refusal, wire registry + TK-05 + task.tool_result binding)): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\24-realtime-and-reliable-events.md, anchor rule-wp-24.90

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
Execute ArcForges delivery task CLOUD.38 — Client outbox and conflict lineage (desktop data model).

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\cloud.md (anchor task-cloud-38).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/cloud-38 (python tools/delivery.py claim CLOUD.38 --worker <name>); task branch task/cloud-38 in DesktopPlatform; ledger record ledger/tasks/cloud-38.md.
Kind/size: service/L. Baseline: not-started.
Outcome: The single sync_outbox schema exists client-side: the existing store_content aggregate row holds its canonical acknowledged Cloud shadow in a dedicated nullable column while payload bytes remain opaque and byte-exact, alongside the pending journal, frozen batch hash/revision/range and explicit supersession lineage; a user conflict resolution appends a new local event and never edits the frozen failed batch.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-25.01 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\25-sync-engine-and-blob-lifecycle.md, anchor rule-wp-25.01

Entry condition: adoption slice ADOPT.02.cloud is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] PLT.01: the local store journal/single-writer persistence foundation
Completion prerequisites (may start earlier; cannot complete before these are complete):
- [integration] CLOUD.39: the real guarded publication/bootstrap mechanism to submit batches against for a genuine end-to-end proof

Permitted write scope: DesktopPlatform:src/BuildingBlocks/ArcForges.Sync/**; DesktopPlatform:src/BuildingBlocks/ArcForges.Persistence.Sqlite/** (only the existing single sync_outbox schema and one store_content.acknowledged_cloud_shadow BLOB NULL column under the fixed cloud-38-sync-outbox-v1 forward migration; atomic local edit/state/journal/outbox/shadow transaction; recovery and downgrade-refusal behavior; payload remains opaque and byte-exact; protected-table migration authorization is limited to this exact migration touching sync_outbox and store_content after legacy-shape validation); DesktopPlatform:tests/PersistenceTests/** (sync_outbox regressions of the persistence work package only)
Shared resources (follow the owner protocol): RES-assistant-store-schema (append): Numbered migrations are allocated at merge by the integration owner (a rebase renumbers pending migrations); each migration is forward-only with its recovery and downgrade-refusal tests; no task edits a merged migration.; RES-desktopplatform-build-config (append): Solution/project lists, central package versions and CI job lists are appended by the task that adds a project, dependency or job; dependency additions follow the dependency-admission policy with a reviewed receipt; lock files are regenerated after rebase and never hand-merged; the integration owner resolves ordering conflicts at merge.; RES-desktopplatform-policy-data (append): Generated policy data is regenerated from its pinned source and never hand-edited; the reason-code registry is append-only with stable codes; each task adds its own test classes and evidence rows.
Unblocks: CLOUD.40, CLOUD.44, CLOUD.47

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): offline + opt-in tests: edit during dispatch, conflict followed by keep-local/keep-Cloud/merge, dependent undispatched batches, crash at each resolution write, late old receipt, own-origin feed echo; migration preserves legacy payload bytes, valid and malformed projection-marker prefixes remain opaque byte-exact payloads, acknowledged shadow round-trips only through its explicit nullable column, legacy store_content shape is validated, and unrelated protected-table access is refused
Completion evidence for the ledger: every local edit has a durable outcome and exactly one live submission lineage; no conflict silently drops pending content
Notes: Cross-repo: WP-25 names this project explicitly in its own §4 table despite living in DesktopPlatform. Persistence.Sqlite scope is limited to the one existing sync_outbox schema plus one store_content.acknowledged_cloud_shadow BLOB NULL column on the existing store_content row, in the same database and atomic local edit/state/journal/outbox/shadow transaction, with the fixed cloud-38-sync-outbox-v1 forward migration, legacy-shape validation, recovery and downgrade-refusal tests; no second database, table or outbox and no unrelated Persistence changes. store_content.payload remains opaque application bytes and is never inspected for or decoded from a marker, magic prefix or hash wrapper. Only cloud-38-sync-outbox-v1 may touch the two exact protected tables sync_outbox and store_content; no generic protected-table authorization is added. PersistenceTests scope covers only WP-25.01 outbox regressions. Project/solution/workflow/inventory/support changes are exact ADP-07 bindings only: append the required project/build/test and current policy/provenance inputs without new dependencies, package identities, policy algorithms or unrelated rows. Preserve RES-assistant-store-schema's serialized migration protocol.
```

```text
Execute ArcForges delivery task CLOUD.39 — Guarded publication, convergent bootstrap and the Sync owner transaction.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\cloud.md (anchor task-cloud-39).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/cloud-39 (python tools/delivery.py claim CLOUD.39 --worker <name>); task branch task/cloud-39 in Cloud; ledger record ledger/tasks/cloud-39.md.
Kind/size: service/L. Baseline: not-started.
Outcome: Model-04's primary lower-bound W bootstrap, immutable-key pages, retention pin and replay-to-H work; the publisher guards watermark/fence/selected rows in one D1 batch; the real Sync owner transaction commits admitted ScopeProjectMetadata and ScopeMetadata owner bodies with publication, receipts and Resource/Entitlement enlistment in the same commit; real D1 clients converge without PostgreSQL snapshot/locks or lost pending work.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-25.02 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\25-sync-engine-and-blob-lifecycle.md, anchor rule-wp-25.02
- WP-21.00 (real Sync owner transaction implementation for admitted ArcScope metadata owner bodies): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\21-cloud-host-and-persistence.md, anchor rule-wp-21.00

Entry condition: adoption slice ADOPT.07.cloud is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] CLOUD.04: the generic receipts/outbox mechanism this publisher reads committed-unpublished rows from
- [artifact] CLOUD.31: WP-24's cursor/gap-handling concept, since this publisher and the realtime DO feed are related but distinct publication mechanisms consumers must not conflate
- [artifact] CLOUD.03: D1 physical mapping/migration runner for the Sync owner tables
- [artifact] CLOUD.06: the shared atomic family engine, since synced content mutation is a named shared-transaction family
- [artifact] CON.03: the closed Sync owner-body admission for ArcScope metadata
- [artifact] CON.09: the published SyncService operations
- [artifact] CLOUD.01: real, delivered outcome of CLOUD.01 (Ingress and host pipeline)
Completion prerequisites (may start earlier; cannot complete before these are complete):
- [integration] CLOUD.70: the gated migration step that applies the locked migrations to the deployed D1 database

Permitted write scope: Cloud:src/Cloud/ArcForges.Cloud.Modules.Sync/Publisher/**; Cloud:src/Cloud/ArcForges.Cloud.Modules.Sync/Transactions/**
Shared resources (follow the owner protocol): RES-cloud-leased-singletons (append): Each publication watermark, Durable Object alarm namespace and R2 prefix has exactly one owning module task; others use its published port; names are reserved in the binding plan before first use.
Unblocks: AND.07, CLOUD.10, CLOUD.38, CLOUD.40, CLOUD.41, CLOUD.43, CLOUD.47, CLOUD.68, SCOPE.27, SRCH.00

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): opt-in real-D1 tests: two-writer interleavings, commit between pages, insert below cursor, delete/tombstone, expired pin, lost acknowledgement, old/new revision application with pending edits; non-allowlisted owner body, stale sorted-root revision and cross-owner reference refusals
Completion evidence for the ledger: real D1 clients converge without PostgreSQL snapshot/locks or lost pending work
Notes: Early risk proof: this is the two-writer D1 guarded-batch algorithm underlying PG-17. Proving it under contention before WP-25.03-07 build on top avoids invalidating that downstream work. PG-17 explicitly 'consumes the publisher from package 21' (CLOUD.04/CLOUD.06) -- this task is where that consumption happens for Sync specifically, together with the real Sync owner transaction. Planning repair 2026-10-05: Pattern for every module (decided by the CLOUD.72 planning repair, 2026-10-05): a module project references only the Abstractions project, so each module task binds its own live store itself, under its own Persistence folder, as an internal class written against the Abstractions plan-execution port (IModulePlanPort, COM.16) and registered in the module's own Register entry with the port created for its own descriptor (IModulePlanPortFactory.For); a call to a shared transaction family goes through the Abstractions family port that CLOUD.72 adds. No module task may leave its store unbound while declaring a service that needs one.
```

```text
Execute ArcForges delivery task CLOUD.40 — Conflict detection and five resolution policies.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\cloud.md (anchor task-cloud-40).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/cloud-40 (python tools/delivery.py claim CLOUD.40 --worker <name>); task branch task/cloud-40 in Cloud; ledger record ledger/tasks/cloud-40.md.
Kind/size: service/M. Baseline: not-started.
Outcome: Conflicts are detected by revision, never timestamp; five policies are implemented per the architecture, chosen per scope and object kind; discarded versions remain recoverable; user-facing conflicts present both versions intelligibly.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-25.03 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\25-sync-engine-and-blob-lifecycle.md, anchor rule-wp-25.03

Entry condition: adoption slice ADOPT.07.cloud is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] CLOUD.38: the client outbox/conflict lineage to detect conflicts against
- [artifact] CLOUD.39: the guarded publication mechanism, since conflicts are detected during publication
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Cloud:src/Cloud/ArcForges.Cloud.Modules.Sync/Conflict/**
Unblocks: CLOUD.44, CLOUD.47

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): offline + opt-in tests: conflict matrix across object kinds and policies, recoverability test for every discard, user-facing presentation test
Completion evidence for the ledger: every conflict path covered, every discarded version recoverable, user-facing conflicts present both versions
```

```text
Execute ArcForges delivery task CLOUD.41 — Deletion and tombstones.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\cloud.md (anchor task-cloud-41).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/cloud-41 (python tools/delivery.py claim CLOUD.41 --worker <name>); task branch task/cloud-41 in Cloud; ledger record ledger/tasks/cloud-41.md.
Kind/size: service/M. Baseline: not-started.
Outcome: Deletion propagates through tombstones with defined retention; an offline-beyond-retention device resolves deterministically rather than silently resurrecting content; local deletion, cloud deletion and unsync are distinguished.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-25.04 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\25-sync-engine-and-blob-lifecycle.md, anchor rule-wp-25.04

Entry condition: adoption slice ADOPT.07.cloud is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] CLOUD.39: the change feed/publication mechanism to propagate tombstones through
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Cloud:src/Cloud/ArcForges.Cloud.Modules.Sync/Tombstones/**
Unblocks: CLOUD.44, CLOUD.47

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): offline + opt-in tests: offline-beyond-retention convergence, resurrection-prevention test, three-way delete-action distinction test
Completion evidence for the ledger: deleted content never silently resurrects; the three delete-like actions are distinguishable
```

```text
Execute ArcForges delivery task CLOUD.42 — Blob lifecycle (real R2 staged/verified/committed).

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\cloud.md (anchor task-cloud-42).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/cloud-42 (python tools/delivery.py claim CLOUD.42 --worker <name>); task branch task/cloud-42 in Cloud; ledger record ledger/tasks/cloud-42.md.
Kind/size: service/L. Baseline: not-started.
Outcome: Upload happens through a server-issued session, chunked and checksummed, moving Staged -> Verified -> Committed; a reference is only published after commit; orphan cleanup removes uncommitted staging without touching committed data; storage accounting is computed from committed objects.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-25.05 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\25-sync-engine-and-blob-lifecycle.md, anchor rule-wp-25.05

Entry condition: adoption slice ADOPT.07.cloud is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] CLOUD.01: the deployed Worker's R2 bucket binding and job-authorized object port (contracts/05 §9 job-grant/job-authorize)
- [artifact] CLOUD.06: the shared atomic family engine, since resource upload lifecycle is a named shared-transaction family
- [artifact] CLOUD.25: the resource transport schema this task replaces the fixture for
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Cloud:src/Cloud/ArcForges.Cloud.Modules.Resource/**
Shared resources (follow the owner protocol): RES-cloud-d1-migrations (append): One global D1 migration sequence: each module task authors migrations under its module prefix; the integration owner assigns the global sequence number at merge, regenerates the plan manifest and rejects edits to merged migrations; the migrator applies in sequence with receipts.; RES-cloud-storage-plans (append): Each module owns its own plan directory; the plan-manifest hash is regenerated by the author after rebase and checked in CI.; RES-shared-transaction-families (append): Adding a participant to a shared atomic family is a design change through the Architecture Owner; module tasks implement only their declared participation.
Unblocks: AND.07, CLOUD.43, CLOUD.44, CLOUD.45, CLOUD.46, CLOUD.47, CLOUD.48, EXT.06, SCOPE.23, SIM.04, WEB.13

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): opt-in real-R2 tests: interrupted-upload resumption, verification-failure path, orphan-cleanup safety test, accounting comparison against actual committed storage
Completion evidence for the ledger: no reference published before commit; orphan cleanup never touches committed data; accounting matches committed storage
Notes: Must-be-real-early per implementation-sequence §3 ('Object storage adapters' may be mocked only at the schema/protocol layer -- 'Upload interruption, hashing, resumption and quota' must be real). Keep this must-be-real-early placement; do not defer real R2 behind fixture evidence. Planning repair 2026-10-05: Pattern for every module (decided by the CLOUD.72 planning repair, 2026-10-05): a module project references only the Abstractions project, so each module task binds its own live store itself, under its own Persistence folder, as an internal class written against the Abstractions plan-execution port (IModulePlanPort, COM.16) and registered in the module's own Register entry with the port created for its own descriptor (IModulePlanPortFactory.For); a call to a shared transaction family goes through the Abstractions family port that CLOUD.72 adds. No module task may leave its store unbound while declaring a service that needs one.
```

```text
Execute ArcForges delivery task CLOUD.43 — Availability, protection, data-health signals and realm-transfer workflow.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\cloud.md (anchor task-cloud-43).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/cloud-43 (python tools/delivery.py claim CLOUD.43 --worker <name>); task branch task/cloud-43 in Cloud; ledger record ledger/tasks/cloud-43.md.
Kind/size: service/L. Baseline: not-started.
Outcome: Hydration/cache pause is distinguished from explicit Cloud deletion; source-consent/transient inputs and health states exist; the full realm-transfer export/preview/commit/status/cancel workflow works from client journeys; missing-object outcomes are rebuilt or verified with irrecoverable data retaining evidence and recovery/export actions.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-25.06 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\25-sync-engine-and-blob-lifecycle.md, anchor rule-wp-25.06

Entry condition: adoption slice ADOPT.07.cloud is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] CLOUD.42: the real blob lifecycle to verify object availability against
- [artifact] CLOUD.39: the sync change feed for the realm-transfer workflow's status/commit steps
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Cloud:src/Cloud/ArcForges.Cloud.Modules.Sync/Health/**; Cloud:src/Cloud/ArcForges.Cloud.Modules.Resource/RealmTransfer/**
Unblocks: CLOUD.47

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): opt-in real-R2/D1 tests: resume after 100-root batch, repeated command, missing object, partial cancellation, denied current scope, transfer credential/ledger exclusion, restore generation
Completion evidence for the ledger: no Unsync deletion of authoritative Cloud content, no empty success for irrecoverable data, no manual migration rule invented
Notes: POSSIBLE DESIGN OVERLAP: this task's 'full realm-transfer export/preview/commit/status/cancel workflow from client journeys' (WP-25.06) reads very close to WP-46.05's 'existing explicit realm export/import semantics using compatible D1 physical/schema/plan manifests' (CLOUD.53). They may be genuinely different (user-facing personal-data export vs operator-level realm-to-realm database migration) or may be the same feature described twice.
```

```text
Execute ArcForges delivery task CLOUD.44 — Multi-device convergence harness.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\cloud.md (anchor task-cloud-44).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/cloud-44 (python tools/delivery.py claim CLOUD.44 --worker <name>); task branch task/cloud-44 in Cloud; ledger record ledger/tasks/cloud-44.md.
Kind/size: integration/L. Baseline: not-started.
Outcome: Three devices editing concurrently, one offline for an extended period, converge to verifiably identical state under concurrent edits, attachments, deletions and a mid-sync crash, verified by comparison not absence of errors.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-25.07 (all work except the parts mapped to SCOPE.27): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\25-sync-engine-and-blob-lifecycle.md, anchor rule-wp-25.07

Entry condition: adoption slice ADOPT.07.cloud is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- none
Completion prerequisites (may start earlier; cannot complete before these are complete):
- [integration] CLOUD.38: real client outbox
- [integration] CLOUD.40: real conflict policies
- [integration] CLOUD.41: real tombstones
- [integration] CLOUD.42: real blob lifecycle
- [integration] SCOPE.27: a real ArcScope client syncing metadata against the deployed Cloud sync engine to run the three-device harness against

Permitted write scope: Cloud:tests/SyncConflictTests/Convergence/**
Unblocks: CLOUD.47, SCOPE.27

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): a three-device convergence harness with concurrent edits, an extended offline device, attachments, deletions and a mid-sync crash
Completion evidence for the ledger: three devices converge to verifiably identical state
Notes: Gate: PG-17 (joint with CLOUD.39). This is the full end-to-end demonstration; CLOUD.39 is where the underlying algorithm risk is retired early.
```

```text
Execute ArcForges delivery task CLOUD.45 — Real Cloud Chat export producer.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\cloud.md (anchor task-cloud-45).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/cloud-45 (python tools/delivery.py claim CLOUD.45 --worker <name>); task branch task/cloud-45 in Cloud; ledger record ledger/tasks/cloud-45.md.
Kind/size: service/L. Baseline: not-started.
Outcome: Bounded leased Cloud export jobs freeze an acknowledged revision manifest, pin history/attachment objects, generate the declared JSON/text outputs with metadata/link map and fidelity report, and publish a verified expiring download artifact; device-only pending edits are excluded.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-25.08 (all work except the parts mapped to AST.21, CLOUD.58): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\25-sync-engine-and-blob-lifecycle.md, anchor rule-wp-25.08

Entry condition: adoption slice ADOPT.07.cloud is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] CLOUD.42: real R2 staging/verification for the export bundle
- [artifact] CLOUD.05: the finite-durable-job mechanism, since exports are bounded leased jobs
- [contract] CON.22: published export and data operations
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Cloud:src/Cloud/ArcForges.Cloud.Modules.Chat/Export/**; Cloud:src/Cloud/ArcForges.Cloud.Jobs/Export/**
Unblocks: AST.21, CLOUD.47, CLOUD.58, WEB.15

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): opt-in real host/database/object-store tests: concurrent history writes, branch edits, deleted attachments, quota limit, expiry, restart, cancellation, paid-term end; compare every delivered manifest/hash and omission; scan for secrets
Completion evidence for the ledger: the Chat export path works against real Cloud authority, preserves a stable snapshot and honest fidelity, and releases pins/reservations on all terminal paths
Notes: This is the Cloud-side producer for PG-07's Cloud Chat export portion; CLOUD.58 structurally removes the WP-15.06 runtime export fixture. Planning repair 2026-10-09 (P2-026; scope correction): reduced: Markdown output of the Cloud export producer is out of scope, not completed; Cloud history export stays JSON or text plus the attachment-availability manifest (EX-01).
```

```text
Execute ArcForges delivery task CLOUD.46 — Application Cloud history and restartable import.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\cloud.md (anchor task-cloud-46).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/cloud-46 (python tools/delivery.py claim CLOUD.46 --worker <name>); task branch task/cloud-46 in Cloud; ledger record ledger/tasks/cloud-46.md.
Kind/size: service/M. Baseline: not-started.
Outcome: HistoryService.BeginImport/FinalizeImport/GetImport/CancelImport work per annex 10 with fixed product scope, verified staged archive/typed rows and atomic visibility/receipt; local-only history bodies never enter Cloud Chat or search without explicit promotion.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-25.09 (all work except the parts mapped to AST.22): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\25-sync-engine-and-blob-lifecycle.md, anchor rule-wp-25.09

Entry condition: adoption slice ADOPT.07.cloud is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] CLOUD.42: real R2 staged-archive verification for imported history bodies
- [artifact] CLOUD.06: the shared atomic family engine for atomic visibility/receipt
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Cloud:src/Cloud/ArcForges.Cloud.Modules.*/History/**
Unblocks: AST.22, CLOUD.47

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): opt-in real tests: actual archive/manifest hashes, staged object authorization, parent/branch mapping, lost finalization acknowledgement, duplicate import, source edit during promotion, quota/permission loss, expiry
Completion evidence for the ledger: clean published desktop, C# Blazor WebAssembly and MAUI Android consumers recover a real interrupted import, see no partial visible conversation, keep local/Cloud/temporary retention distinct
Notes: Replaces the HistoryService fixture consumed by WP-15/WP-17. See integration_proposals: IM.assistant-history-real-integration. Planning repair 2026-10-08 (DLV-34; P2-021): the Kotlin and TypeScript consumers are replaced by the C# desktop, Blazor WebAssembly and MAUI Android consumers; the import and retention rules are unchanged.
```

```text
Execute ArcForges delivery task CLOUD.47 — Owned-artifact closure and real integration.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\cloud.md (anchor task-cloud-47).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/cloud-47 (python tools/delivery.py claim CLOUD.47 --worker <name>); task branch task/cloud-47 in Cloud; ledger record ledger/tasks/cloud-47.md.
Kind/size: integration/M. Baseline: not-started.
Outcome: R2 is used for the existing upload admission, multipart resume, Verified pin, owner promotion, quota and release lifecycle; outbox/inbox/tombstones/conflicts/bootstrap/unknown-field behavior and export protocol are retained; three-device convergence and interrupted-upload/failed-content-commit/orphan/delete cases run against actual provider adapters.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-25.90 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\25-sync-engine-and-blob-lifecycle.md, anchor rule-wp-25.90
- WP-25:required-implementation-and-closure-from Required implementation and closure from the final review (01-cloud-data-model verification; real structural move/ack/conflict transactions, full native metadata replicas, job-authorized R2 staging/verification/promotion, quarantined old-generation client commands) (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\25-sync-engine-and-blob-lifecycle.md, package-level obligation

Entry condition: adoption slice ADOPT.07.cloud is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] AST.21: package task delivered
- [artifact] AST.22: package task delivered
- [artifact] CLOUD.58: package task delivered
- [artifact] SCOPE.27: package task delivered
Completion prerequisites (may start earlier; cannot complete before these are complete):
- [integration] CLOUD.38: final candidate
- [integration] CLOUD.39: final candidate
- [integration] CLOUD.40: final candidate
- [integration] CLOUD.41: final candidate
- [integration] CLOUD.42: final candidate
- [integration] CLOUD.43: final candidate
- [integration] CLOUD.44: final candidate
- [integration] CLOUD.45: final candidate; WP-25.08 must be represented in this task's own evidence and completion gate per the WP text, not treated as optional
- [integration] CLOUD.46: final candidate
- [integration] CLOUD.68: package task complete

Permitted write scope: Cloud:artifacts/candidate/**
Unblocks: REL.06

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): three-device convergence and interrupted-upload/failed-content-commit/orphan/delete cases against actual provider adapters
Completion evidence for the ledger: owned artifact and real-integration receipt per WP-25.90
```

```text
Execute ArcForges delivery task CLOUD.48 — D1 and independent object backup.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\cloud.md (anchor task-cloud-48).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/cloud-48 (python tools/delivery.py claim CLOUD.48 --worker <name>); task branch task/cloud-48 in Cloud; ledger record ledger/tasks/cloud-48.md.
Kind/size: service/L. Baseline: not-started.
Outcome: Model-04/backup-manifest-v1 works: matching D1 export/bookmark/base sequence, contiguous replay, verified R2 inventory and an independent S3-COMPLIANCE copy; no PostgreSQL WAL/LSN procedure; measured metadata/blob RPO and RTO pass; Time Travel alone cannot satisfy independent restore.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-46.00 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\46-backup-recovery-and-data-health.md, anchor rule-wp-46.00

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

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\cloud.md (anchor task-cloud-49).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/cloud-49 (python tools/delivery.py claim CLOUD.49 --worker <name>); task branch task/cloud-49 in Cloud; ledger record ledger/tasks/cloud-49.md.
Kind/size: service/M. Baseline: not-started.
Outcome: Base bookmark/sequence and contiguous after-image archive are verified; in-place Time Travel and fresh import/replay both use generation fences.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-46.01 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\46-backup-recovery-and-data-health.md, anchor rule-wp-46.01

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

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\cloud.md (anchor task-cloud-50).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/cloud-50 (python tools/delivery.py claim CLOUD.50 --worker <name>); task branch task/cloud-50 in Cloud; ledger record ledger/tasks/cloud-50.md.
Kind/size: service/M. Baseline: not-started.
Outcome: Old ingress/keys are fenced, D1/R2 are restored, the independent restrictive safety journal replays, credentials/leases/cursors are invalidated, external effects are reconciled; a deleted/revoked account cannot reappear and an absent attempt cannot execute twice.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-46.02 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\46-backup-recovery-and-data-health.md, anchor rule-wp-46.02

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

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\cloud.md (anchor task-cloud-51).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/cloud-51 (python tools/delivery.py claim CLOUD.51 --worker <name>); task branch task/cloud-51 in Cloud; ledger record ledger/tasks/cloud-51.md.
Kind/size: integration/M. Baseline: not-started.
Outcome: An actual Container/Worker/DO/R2/D1 restore runs using separate credentials and an immutable archive with RTO<=4h real evidence, not a SQLite/simulator-only restore.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-46.03 (Cloud-side drill: real Container/Worker/DO/R2/D1 restore using separate credentials and immutable archive, RTO<=4h. The combined AI reopen portion is a joint step with the AI lanes/the governance and release lanes -- see IM.dr-drill-combined-ai-reopen): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\46-backup-recovery-and-data-health.md, anchor rule-wp-46.03

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

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\cloud.md (anchor task-cloud-52).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/cloud-52 (python tools/delivery.py claim CLOUD.52 --worker <name>); task branch task/cloud-52 in Cloud; ledger record ledger/tasks/cloud-52.md.
Kind/size: service/S. Baseline: not-started.
Outcome: Archive watermark, capacity, canonical refs/hash/pins, derived-rebuild state and backup lag/admission state are exposed as a queryable read projection, with 4min/12min warning guards and exceeded-objective incidents made visible.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-46.04 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\46-backup-recovery-and-data-health.md, anchor rule-wp-46.04

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

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\cloud.md (anchor task-cloud-53).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/cloud-53 (python tools/delivery.py claim CLOUD.53 --worker <name>); task branch task/cloud-53 in Cloud; ledger record ledger/tasks/cloud-53.md.
Kind/size: service/M. Baseline: not-started.
Outcome: Explicit realm export/import semantics work using compatible D1 physical/schema/plan manifests; no automatic cross-DB transaction; identity/resource/history scope is preserved and unsupported mapping is refused.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-46.05 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\46-backup-recovery-and-data-health.md, anchor rule-wp-46.05

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
Notes: POSSIBLE DESIGN OVERLAP with CLOUD.43 (WP-25.06 realm-transfer workflow) -- see that task's notes. Planning repair 2026-10-05: Pattern for every module (decided by the CLOUD.72 planning repair, 2026-10-05): a module project references only the Abstractions project, so each module task binds its own live store itself, under its own Persistence folder, as an internal class written against the Abstractions plan-execution port (IModulePlanPort, COM.16) and registered in the module's own Register entry with the port created for its own descriptor (IModulePlanPortFactory.For); a call to a shared transaction family goes through the Abstractions family port that CLOUD.72 adds. No module task may leave its store unbound while declaring a service that needs one.
```

```text
Execute ArcForges delivery task CLOUD.54 — Backup release gate.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\cloud.md (anchor task-cloud-54).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/cloud-54 (python tools/delivery.py claim CLOUD.54 --worker <name>); task branch task/cloud-54 in Cloud; ledger record ledger/tasks/cloud-54.md.
Kind/size: service/S. Baseline: not-started.
Outcome: Verified independent backup and safety journal are required before paid production admission; no unverified restore, private access or mutation reopens on incomplete inventory.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-46.06 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\46-backup-recovery-and-data-health.md, anchor rule-wp-46.06

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

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\cloud.md (anchor task-cloud-55).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/cloud-55 (python tools/delivery.py claim CLOUD.55 --worker <name>); task branch task/cloud-55 in Cloud; ledger record ledger/tasks/cloud-55.md.
Kind/size: integration/M. Baseline: not-started.
Outcome: Every WP-46 substep is complete, built/packed once, and consumed as exact candidate bytes from a clean environment with all applicable UX acceptance groups recorded.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-46.90 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\46-backup-recovery-and-data-health.md, anchor rule-wp-46.90

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
Execute ArcForges delivery task CLOUD.58 — Structural removal of the Chat export runtime fixture.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\cloud.md (anchor task-cloud-58).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/cloud-58 (python tools/delivery.py claim CLOUD.58 --worker <name>); task branch task/cloud-58 in Cloud; ledger record ledger/tasks/cloud-58.md.
Kind/size: integration/M. Baseline: not-started.
Outcome: The production clients run with no fixture export producer registered; real Cloud export jobs serve the Chat export path

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-25.08 (full, joint with consumer-side structural fixture-registration removal): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\25-sync-engine-and-blob-lifecycle.md, anchor rule-wp-25.08

Entry condition: adoption slice ADOPT.07.cloud is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] CLOUD.45: real, delivered outcome of CLOUD.45 (Real Cloud Chat export producer)
- [artifact] AST.21: assistant history export consuming the real Cloud export producer
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: 
Unblocks: CLOUD.47

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Local real-integration run of the affected scenario in an existing environment, recorded once; offline and static checks in CI; no hosted runtime, device, browser, live-service or inference CI (P2-017).
Completion evidence for the ledger: The production clients run with no fixture export producer registered; real Cloud export jobs serve the Chat export path
```

```text
Execute ArcForges delivery task CLOUD.63 — Real Commerce/Entitlement participation in the shared atomic family engine.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\cloud.md (anchor task-cloud-63).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/cloud-63 (python tools/delivery.py claim CLOUD.63 --worker <name>); task branch task/cloud-63 in Cloud; ledger record ledger/tasks/cloud-63.md.
Kind/size: integration/M. Baseline: not-started.
Outcome: The 'exact credits' half of WP-21.05's own completion gate ('Two Containers contend, stale holder cannot finalize, exact credits and sync cursor safety') -- Commerce's family participation, owned by the commerce, policy and operations lanes

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-21.05 (Commerce/Entitlement family participant evidence for the shared completion gate): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\21-cloud-host-and-persistence.md, anchor rule-wp-21.05

Entry condition: adoption slice ADOPT.07.cloud is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] CLOUD.06: real, delivered outcome of CLOUD.06 (Shared atomic family guarded-batch engine)
- [artifact] CLOUD.16: real, delivered outcome of CLOUD.16 (PAT and actor authorization)
- [artifact] COM.09: real, delivered outcome of COM.09 (Ledgers and reconciliation)
- [artifact] COM.16: the real Entitlement D1 store and grant port as the Entitlement participant of the shared families
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: 
Unblocks: CLOUD.06

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Local real-integration run of the affected scenario in an existing environment, recorded once; offline and static checks in CI; no hosted runtime, device, browser, live-service or inference CI (P2-017).
Completion evidence for the ledger: The 'exact credits' half of WP-21.05's own completion gate ('Two Containers contend, stale holder cannot finalize, exact credits and sync cursor safety') -- Commerce's family participation, owned by the commerce, policy and operations lanes
```

```text
Execute ArcForges delivery task CLOUD.64 — Full operator contract closure across PublicApi, Commerce, Policy and Console.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\cloud.md (anchor task-cloud-64).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/cloud-64 (python tools/delivery.py claim CLOUD.64 --worker <name>); task branch task/cloud-64 in Cloud; ledger record ledger/tasks/cloud-64.md.
Kind/size: integration/M. Baseline: not-started.
Outcome: Every operator operation's eight authorization fields, operator scope and OC-03 role binding work end-to-end with the real financial owners (WP-42), configuration/policy owners (WP-44) and console join (WP-45)

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-23:operator-contract-closure-appendix-full Operator contract closure appendix, full cross-area join (Operator contract closure appendix, full cross-area join): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\23-public-api-and-generated-clients.md, package-level obligation

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

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\cloud.md (anchor task-cloud-66).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/cloud-66 (python tools/delivery.py claim CLOUD.66 --worker <name>); task branch task/cloud-66 in Cloud; ledger record ledger/tasks/cloud-66.md.
Kind/size: integration/M. Baseline: not-started.
Outcome: Full coverage of WP-22.04's completion gate ('every enumerated operation demands step-up') across Commerce refund/purchase operations and any other module-owned sensitive operation, not just Identity's own

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-22.04 (cross-product operation coverage beyond Identity's own operations): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\22-identity-workspace-and-device.md, anchor rule-wp-22.04

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

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\cloud.md (anchor task-cloud-67).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/cloud-67 (python tools/delivery.py claim CLOUD.67 --worker <name>); task branch task/cloud-67 in Cloud; ledger record ledger/tasks/cloud-67.md.
Kind/size: integration/M. Baseline: not-started.
Outcome: AI services genuinely reopen and function after a real Cloud DR restore, per WP-46.03's own 'then combined AI reopen at 50/52'

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-46.03 (combined AI-reopen portion): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\46-backup-recovery-and-data-health.md, anchor rule-wp-46.03

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

```text
Execute ArcForges delivery task CLOUD.68 — ArcScope library read model and companion notifications.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\cloud.md (anchor task-cloud-68).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/cloud-68 (python tools/delivery.py claim CLOUD.68 --worker <name>); task branch task/cloud-68 in Cloud; ledger record ledger/tasks/cloud-68.md.
Kind/size: service/M. Baseline: not-started.
Outcome: scope.listProjects, scope.listSessions and scope.getSession project authorized committed project/session rows from scope.synced_aggregate. Project names, revisions and commit times come from ScopeProjectMetadata; counts and paging bind a consistent authorized snapshot, with missing/deleted parents and empty projects excluded. Sync emits durable scope.reportSynced and sync.conflictNeedsDecision notifications through the existing owner transaction, idempotently on replay. No raw bytes or new authoritative table are introduced.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-25.10 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\25-sync-engine-and-blob-lifecycle.md, anchor rule-wp-25.10

Entry condition: adoption slice ADOPT.07.cloud is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [contract] CON.24: the generated ScopeService and summary records
- [artifact] CLOUD.39: the real Sync owner transaction committing ArcScope metadata
- [artifact] CLOUD.21: public endpoint registration
- [artifact] CLOUD.12: the Notification module durable rows that CLOUD.12 writes (Cloud:src/Cloud/ArcForges.Cloud.Modules.Notification/**), not live Postmark or SES mail delivery
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Cloud:src/Cloud/ArcForges.Cloud.Modules.Scope/Library/**; Cloud:src/Cloud/ArcForges.Cloud.Modules.Sync/Notifications/**
Unblocks: AND.27, CLOUD.47, WEB.32

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): offline projection, authorization and notification tests covering project rename, parent tombstones, out-of-order project/session arrival, empty projects, count changes without a project revision change, paged reads across commits and cache invalidation on either root; optional affected-scope real-D1 checks using an existing environment for these cases, minRevision, large responses and durable notification replay (P2-017).
Completion evidence for the ledger: Real D1 projection results, authorization refusals and notification receipts for a synced ArcScope workspace.
Notes: Builds as soon as the Sync owner transaction exists; durable notification rows come from the Notification module. Planning repair 2026-10-09 (P2-026; scope correction, brief section 11 S6): the complete edge to CLOUD.12 is replaced by an artifact start edge on CLOUD.12, so the read model and the WP-25 closure are not blocked by CLOUD.12's blocked-external live mail evidence.
```

```text
Execute ArcForges delivery task CLOUD.69 — Correlation acceptance and propagation across ingress, response meta and queue wake.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\cloud.md (anchor task-cloud-69).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/cloud-69 (python tools/delivery.py claim CLOUD.69 --worker <name>); task branch task/cloud-69 in Cloud; ledger record ledger/tasks/cloud-69.md.
Kind/size: service/M. Baseline: not-started.
Outcome: The deployed Cloud ingress and host carry one correlation identity per call (CR-01, CR-03, CR-06, HP-06): a RequestMeta.correlationId is read, validated as a canonical lowercase UUID and bound to the call context without ever influencing authorization or the current-owner decision, an absent value is created at the edge, a malformed value is refused with the registered validation.invalid_request code, and the identity is returned in ResponseMeta.correlationId and ArcError.correlationId of every reply the host builds. The Worker and host join it to one W3C traceparent per call, and the job wake message and the private job-slice call carry correlationId and causationId (the originating request or the previous wake event), so one synthetic call is joined across HTTP, Worker, host and queue-wake by the identifier alone. The task provides the one Cloud-side seam (a call-scoped correlation context for the host and a correlation envelope for Worker-originated queue messages) that later hop owners reuse instead of re-implementing propagation per module. It adds no realtime or provider behavior and no new wire field, header or contract meaning: a need for one is raised to the Contracts owner under PA-02.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-12.01 (the Cloud share: acceptance of a validated client correlation value or creation at the Cloud edge, and its propagation across the HTTP ingress, Worker, host, ResponseMeta/ArcError and queue-wake hops (the shared infrastructure and the desktop origin stay with PLT.48)): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\12-observability-foundation.md, anchor rule-wp-12.01

Entry condition: adoption slice ADOPT.07.cloud is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] CLOUD.01: the deployed ingress and host pipeline (RpcPolicy, RequestEnvelopeReader, IngressPipeline, Worker pipeline and the wake queue consumer) in which correlation is read, bound and returned
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Cloud:worker/ingress/** (read, validate or create the correlation identity at the edge, forward it to the host with one W3C traceparent, and return it on Worker-built refusals only through fields the wire registry already defines); Cloud:worker/foundation/queue.ts, Cloud:worker/foundation/types.ts and Cloud:worker/foundation/container-client.ts (only the job wake message correlationId/causationId metadata, its closed-key parser and its forwarding in the private job-slice call; no change to lease, fence, retry or backoff semantics); Cloud:src/ArcForges.Cloud/Ingress/** (the existing Native AOT host project, which is the real layout of the planned Cloud.Host; RequestEnvelopeReader, Caller, RpcPolicy, IngressPipeline and the proof-only PipelineProbe replies; the adoption rules forbid renaming it or adding a parallel project); Cloud:src/ArcForges.Cloud/Foundation/JobSliceService.cs and the private job-slice request handling in Cloud:src/ArcForges.Cloud/Foundation/FoundationEndpoints.cs (only to accept the wake's correlation/causation and carry them in the call context); Cloud:tests/ArcForges.Cloud.Tests/** and Cloud:tests/worker/**; Cloud:eng/verification/pipeline-scenarios.ts and Cloud:eng/verification/foundation-scenarios.ts (only added local cross-process and explicit opt-in deployed correlation scenarios: supplied, absent, malformed, error reply, queue wake; the deployed scenarios hold the lease leases/res-cloud-deployment for the live run only); Cloud:package.json (the explicit test file list and the scenario scripts only; no dependency or version change); Cloud:eng/policy/dependency-policy.json and Cloud:eng/policy/dependency-reviews/cloud-69-*.json (new immutable successor chained from the then-active receipt, only because the changed bundle, manifest and source inputs are hash-bound; no coordinate, integrity value or closure entry changes); Cloud:eng/provenance/** (immutable successor release profile, Worker bundle and runtime-notice records only where an existing record binds an input this task changes, the first-party inventory files.json and the deterministic NOTICE.txt); Cloud:docs/cloud-ingress.md and Cloud:AGENTS.md (factual description of correlation acceptance, the seam and what remains unobserved)
Shared resources (follow the owner protocol): RES-cloud-deployment (append): Bindings are added by the owning module task in its own section, and the Cloud integration owner resolves ordering conflicts at merge. Any task that runs against the deployed test environment holds the lease `leases/res-cloud-deployment` for that live run only, whatever mode it declares for its binding edits; production deployment belongs to release tasks.
Unblocks: AIR.04, CLOUD.05, CLOUD.33, CLOUD.84, PLT.48

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline unit and cross-process tests: a valid supplied identifier is echoed in ResponseMeta and ArcError and reaches the wake message and job-slice call; an absent one is created; a malformed one is refused with validation.invalid_request before any handler or authorization decision; a supplied value never changes the authorization outcome; the Worker and host share one traceparent. Explicit local opt-in deployed scenarios against the isolated proof environment, once, under the RES-cloud-deployment lease. No hosted live, device, GUI or browser run (P2-017).
Completion evidence for the ledger: Source commit, Worker bundle and image identity, local and deployed correlation scenario results with the untested hops named (realtime and provider are not exercised), and confirmation that no new wire field or header was introduced.
Notes: Planning repair 2026-10-05 (DLV-34: scope moves only; no obligation or acceptance is removed). PLT.48's completion follow-up found that its completion prerequisite CLOUD.01 delivers a pipeline that neither reads, validates, returns nor propagates a correlation identifier (no Cloud code or documentation handles RequestMeta.correlationId, ResponseMeta.correlationId, ArcError.correlationId or a traceparent; the wake message is a closed key set without correlation) and that no Cloud task owned CR-01, CR-03, CR-06 or HP-06 for the Cloud side. This task is that owner and is deliberately small: it uses only the fields already in wire registry 04 (RequestMeta tag 3, ResponseMeta tag 4, ArcError tag 6; the generated Contracts packages already carry them) and the existing private signed job-slice call. It does not add the realtime or provider hops: Event.correlationId is populated by the publication owners (CLOUD.33 and the stream owners) and a provider request identifier (CR-05) by the provider owners (AIR.04), each of which starts from this task's seam and keeps its own acceptance. The C# origin that makes the connected trace is not a Cloud or DesktopPlatform delivery task: PLT.48's completion follow-up performs it as one local opt-in consumer run outside the repository (the PLT.53 precedent) using the published ArcForges.Observability package to create the typed origin and the published generated PublicApi client to send it to the isolated proof environment, under the RES-cloud-deployment lease, and records the connected trace. The write scope of CLOUD.01 is not reopened. CLOUD.02 changes different files of the same host project (moved Storage and Hmac sources, module projects, composition listing); rebase after it merges, append to RES-cloud-host-composition only if a registration is needed (none is planned), and regenerate hash-bound provenance after the rebase. Planning repair 2026-10-08 (DLV-34; P2-021): the correlation validation in worker/ingress/correlation.ts moves to C# under CLOUD.84; the Worker only forwards correlation values. Outcome, validation and evidence above are recorded history and are unchanged.
```

```text
Execute ArcForges delivery task CLOUD.70 — Gated D1 migration deployment step and compatible-rollback flow.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\cloud.md (anchor task-cloud-70).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/cloud-70 (python tools/delivery.py claim CLOUD.70 --worker <name>); task branch task/cloud-70 in Cloud; ledger record ledger/tasks/cloud-70.md.
Kind/size: service/S. Baseline: not-started.
Outcome: Migrations reach a deployed D1 database only through one gated step of the deployment pipeline (Design D1 profile section 6: never from Container startup). The step runs the CLOUD.03 runner against the target environment's business database under the migrator lease and fence, applies the pending migrations in sequence, prints the receipts and compatibility record without any secret, applies a backfill, cutover or contract migration only when the release manifest names it for this deployment (contract only with the explicit consent flag and after its soak), and before promoting a Worker or image checks the compatible-rollback rule so that a build the read or write horizon excludes is never promoted. The step is exercised once against the proof environment under the RES-cloud-deployment lease and records its result; production receives the same step only through the existing gated main-push deployment job. It adds no schema, no runner behavior and no deployment secret to pull-request code.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-21.03 (the deployment-job application of the migration runner and its compatibility flow: a gated migration step in the existing deployment pipeline that holds the migrator lease and fence, applies the pending locked migrations in sequence with receipts, surfaces the receipts and the compatibility record in the job, orders expand, backfill, cutover and contract across deployments, and refuses an application build that the schema horizons exclude (the compatible-rollback rule); the manifest, the runner, the adapters and the conformance evidence stay with CLOUD.03): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\21-cloud-host-and-persistence.md, anchor rule-wp-21.03

Entry condition: adoption slice ADOPT.07.cloud is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] CLOUD.03: the migration runner, its REST client, the locked migration catalog and the compatible-rollback rule to run from the deployment job
- [artifact] CLOUD.01: the existing gated deployment job and the proof environment the step is added to and exercised in
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Cloud:.github/workflows/ci.yml (only one gated migration step in the existing main-push deployment job and the proof deployment job, run before the Worker or image is promoted; the pull-request jobs gain no secret and no migration step; the workflow is shared build configuration and the Cloud integration owner resolves ordering conflicts at merge); Cloud:tooling/cloudflare.ts and Cloud:eng/migrations/deploy.ts (the deployment-time caller of the runner: environment-to-database selection from the existing deployment configuration, the release manifest's migration plan, the compatible-rollback check and the receipt report; no change to the runner, the catalog, the manifest or the adapters); Cloud:tests/worker/d1-migration-deploy*.test.ts (new files only: the step against the SQLite and fake-REST oracles, the refusal of an excluded build, no secret in any output); Cloud:package.json (only the new test files in the test list and one script) and Cloud:tsconfig.json (only if a new folder needs the include); Cloud:eng/policy/dependency-policy.json and Cloud:eng/policy/dependency-reviews/cloud-70-*.json (new immutable successor chained from the then-active receipt, only because hash-bound inputs change; no coordinate, integrity value or closure entry changes); Cloud:eng/provenance/** (immutable successor records only where an existing record binds an input this task changes, the first-party inventory files.json and the deterministic NOTICE.txt); Cloud:docs/d1-migration-deployment.md (new, factual description of the gated step, its environment variables by name only, the proof-environment run and the rollback flow; docs/deployment.md stays with CLOUD.09)
Shared resources (follow the owner protocol): RES-cloud-deployment (append): Bindings are added by the owning module task in its own section, and the Cloud integration owner resolves ordering conflicts at merge. Any task that runs against the deployed test environment holds the lease `leases/res-cloud-deployment` for that live run only, whatever mode it declares for its binding edits; production deployment belongs to release tasks.
Unblocks: CLOUD.07, CLOUD.09, CLOUD.10, CLOUD.39, CLOUD.84

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): offline tests of the deployment caller against the SQLite oracle and a fake REST client (gated order, receipts printed, excluded build refused, no secret in any output, a contract refused without consent); one explicit proof-environment run under the RES-cloud-deployment lease per docs/validation-policy.md, recorded once; no pull-request job receives a secret and none runs a live service
Completion evidence for the ledger: the proof-environment run's job result and receipt report (receipt and fence values, never a secret), the refusal test results and the source commit
Notes: Planning repair 2026-10-05 (DLV-34: a new task gives work no existing scope could hold; no obligation or acceptance is removed). CLOUD.03 delivers the runner and states that no workflow step runs it; CLOUD.07 (wrangler.json and capacity), CLOUD.09 (docs/deployment.md and eng/selfhost) and CLOUD.10 (artifacts/candidate) cannot hold a .github/workflows/ci.yml edit, and only the completed PRF.07 listed it. Modules whose live acceptance runs against a deployed schema (CLOUD.07, CLOUD.09, CLOUD.10, CLOUD.39) complete after it; no task's start waits for it, so offline and local-oracle module work is not delayed. Planning repair 2026-10-08 (DLV-34; P2-021; brief section 5.7): the deployment-time decisions in eng/migrations/deploy.ts (target and database selection, release-plan reading, and the gate and excluded-build refusals) move to C# under CLOUD.84 (src/ArcForges.Cloud.Storage.D1/Deploy); the Node caller keeps argument passing only. Outcome, validation and evidence above are recorded history and are unchanged.
```

```text
Execute ArcForges delivery task CLOUD.71 — Serve the built Web profiles from the proof origin.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\cloud.md (anchor task-cloud-71).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/cloud-71 (python tools/delivery.py claim CLOUD.71 --worker <name>); task branch task/cloud-71 in Cloud; ledger record ledger/tasks/cloud-71.md.
Kind/size: service/S. Baseline: not-started.
Outcome: The two production profile builds of PRF.08 are served, byte for byte, by the proof Worker (custom domain proof.arcforges.com, workers.dev and previews stay disabled) as static assets on separate paths of the same origin that serves /api, /session/v1 and the operator-signed /proof/v1 surface, which keep going to the Worker first. The bytes come from one immutable digest-named bundle that the Web main-push build publishes; the Cloud proof deployment job (manual proof=deploy) downloads that exact asset, verifies its digest against the value pinned in the deployment manifest and binds it as the Worker's assets, so nothing is rebuilt and no Web source is read. Responses carry the profile Content-Security-Policy that PRF.08 derives. Each profile is built with its own router base, /account/ and /chat/, so that the unchanged page code runs on its own path (a profile whose router base is / answers "Page not found" on any other path); the compiled JavaScript and stylesheet chunks stay byte-identical to the root builds, only the prerendered page moves to account/index.html and chat/index.html and carries its base, and the content-hashed assets/ directories of the two builds merge into one tree in which a name with two different contents refuses the bundle. Production configuration and the Web apex Custom Domain are untouched. The proof Container application gives its two named instances (hello, which serves /api, and foundation, which serves /session/v1 and the operator surface) the headroom to run at the same time, and a read-only observation in the manual proof dispatch shows the application's configured ceiling and its instances before and after the deployment. The result is exercised once with PRF.08's live script (apps/app/scripts/proof-run.ts) pointed at the served profiles under the RES-cloud-deployment lease and the run's result is recorded.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-06.05 (the deployed same-origin hosting of the two built production profiles (Account and Chat) on the proof origin, so that the page, /api and /session/v1 share one origin, cookie and CSRF boundary on a deployed Cloudflare; the profile builds, their budgets and their offline proof stay with PRF.08): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\06-aot-jit-and-wasm-publish-proof.md, anchor rule-wp-06.05

Entry condition: adoption slice ADOPT.07.cloud is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] PRF.07: the deployed proof environment, its custom domain, its operator-signed surface and its manual deployment job
- [artifact] PRF.11: the Blazor WebAssembly Account and Chat production profile builds and their measured, deterministic output (PRF.11, successor of the React build:profiles output)
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Cloud:wrangler.json (only env.proof: the static-assets binding and the routing so that /api, /session/v1 and /proof/v1 reach the Worker first, and the instance ceiling of its one containers entry (max_instances) so that its two named instances can run at the same time; no production, no other environment and no binding, class, image, instance-type or placement change); Cloud:worker/foundation/** (only the proof route fragment, and only if the assets configuration alone cannot keep the three route families on the Worker); Cloud:.github/workflows/ci.yml and Cloud:eng/verification/proof-deploy.ts (only the manual proof deployment job: download the digest-named bundle asset, verify the pinned digest, stage it as the proof assets; no pull-request job gains a secret, a download or a live call); Cloud:.github/workflows/ci.yml (also the read-only observe choice of the same manual proof dispatch: one option of the existing proof input and its branch in the existing proof access step, which creates, changes and deploys nothing and prints no secret or token; no new job and no pull-request change); Cloud:eng/verification/proof-cloudflare.ts (only the deploy function of the same manual job, which is the real home of its code, as CLOUD.70 recorded: stage the verified bundle as the proof assets and record its digest in the proof deployment record); Cloud:eng/verification/proof-cloudflare.ts (also the read-only observe function of that dispatch and its action check: the proof Container application's configured and counted instances, every instance with its state, Durable Object name, version, location and state-change times, its rollouts, and whether the deployment token may query Workers Logs; allowlisted names, states, counts and times only, never a secret, token, environment value or log content); Cloud:tests/worker/proof-assets*.test.ts (new files only: route precedence, digest refusal, headers); Cloud:tests/worker/proof-observe*.test.ts (new files only: the observe function against a fake provider API: read-only calls, the allowlist, no token or account id in the output, a missing application and refused reads); Cloud:tests/worker/proof-deploy.test.ts (only the pin of the proof environment's container ceiling); Cloud:src/ArcForges.Cloud/Foundation/SessionService.cs (only the idle renewal of an active session, TouchAsync: it renews with the session's own idle window, the distance between its stored idle expiry and last-seen time, which issue and every renewal write together and no request supplies, never longer than the configured window and capped at the absolute expiry; issue, resolution, revocation, the default constants, the plans and the stored schema are unchanged. The foundation module is registered only in the proof environment, so production, which serves only Hello, is unchanged, and a default session keeps its thirty minute window); Cloud:tests/ArcForges.Cloud.Tests/SessionServiceTests.cs and Cloud:tests/ArcForges.Cloud.Tests/FoundationHostTests.cs (only new idle-renewal tests: a short issued window stays short after renewal, a session idle past its window is refused on bootstrap and on logout after a renewing bootstrap, a default session renews exactly as before, the absolute expiry still caps, and a stored window longer than the configured one cannot lengthen a renewal); Cloud:package.json (only the new test files in the test list and the observe:proof script); Cloud:eng/policy/dependency-policy.json and Cloud:eng/policy/dependency-reviews/cloud-71-*.json (new immutable successor chained from the then-active receipt, only because hash-bound inputs change; no coordinate or closure entry changes); Cloud:eng/provenance/** (immutable successor records only where an existing record binds an input this task changes, the first-party inventory files.json and the deterministic NOTICE.txt); Cloud:docs/prf-07-foundation-proof.md and Cloud:docs/cloud-ingress.md (factual additions and corrections about the served profiles, the proof Container capacity, the observe choice, the session idle renewal and the proof run); Cloud:docs/cloud-readiness.md (only its section on diagnosing a 503 from the proof origin: the observed one-container behaviour, the observe choice and the proof ceiling); Web:.github/workflows/ci.yml (only what carries the already built profile bundle to one immutable digest-named release asset next to the existing candidate asset: one main-push-only upload step in the candidate job, one download step in the existing main-push deployment job and the extra asset argument of its existing release step; the sealed candidate directory and its file-set verification are unchanged; no new job, runner, credential or pull-request step); Web:apps/app/scripts/** and Web:docs/prf-08-*.md (only the bundling script for that asset, the adaptation of the existing build, measurement and live scripts to the page location below, and the factual record of the served-profile run, and the interaction-budgets.json that the live run produces); Web:apps/app/react-router.config.ts (only the per-profile router base /account/ and /chat/ that lets the unchanged page code run on its own path of the proof origin); Web:tests/unit/app-profiles.test.ts and Web:tests/unit/app-bundle*.test.ts (the existing build-gate expectations for the page location and new files for the bundling script)
Shared resources (follow the owner protocol): RES-cloud-deployment (append): Bindings are added by the owning module task in its own section, and the Cloud integration owner resolves ordering conflicts at merge. Any task that runs against the deployed test environment holds the lease `leases/res-cloud-deployment` for that live run only, whatever mode it declares for its binding edits; production deployment belongs to release tasks.; RES-cloud-host-composition (append): Each module registers through its own module entry point and route fragment; the host composition only lists modules; route and binding conflicts are resolved by the integration owner at merge.
Unblocks: CLOUD.85, PRF.08, PRF.11

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): offline tests of route precedence, digest verification and headers, and of the read-only observation (read-only calls, allowlisted output, no secret); one read-only observation of the proof Container application before and one after one explicit proof-environment deployment, one check that both named instances answer within the same minute and one live run, all under the RES-cloud-deployment lease per docs/validation-policy.md and recorded once; no pull-request job receives a secret and none runs a live service
Completion evidence for the ledger: the proof deployment job result with the verified bundle digest, the observation outputs before and after the deployment and the concurrency check, the live run's output (observations and interaction timings, never a secret or a session handle) and the source commits
Notes: Planning repair 2026-10-05 (DLV-34: a new task gives work no existing scope could hold; no obligation or acceptance is removed). PRF.08's completion needs the built profiles to share an origin with the deployed ingress; the proof Worker has no assets binding and no existing Cloud or Web task owns one. WEB.30 cannot hold it because it consumes PRF.08, so an edge from PRF.08 to it would be a cycle; this task starts after PRF.08 delivers the profiles and PRF.08 completes after it. No task's start waits for it. Planning repair 2026-10-06 (DLV-34, found while implementing: the unchanged PRF.08 page, whose router base is /, rendered "Page not found" when served on /account/ in a local Chromium check, so serving the two profiles on separate paths needs the per-profile router base; the proof deployment function lives in eng/verification/proof-cloudflare.ts, which the scope did not name; and the sealed Web candidate directory verifies an exact file set, so the profile bundle cannot ride inside it and needs its own upload and download step; no obligation or acceptance is removed). Planning repair 2026-10-06, second (DLV-34, found by the completion follow-up's diagnosis): in the proof Container application (max_instances 2) only one of the two named instances, hello and foundation, ran at a time; while one held a container every start of the other was refused for as long as the holder stayed active, and the refused one started within seconds after the holder's idle stop, so the live run could not pass (the warm-up's Hello start waited for the foundation instance to sleep, and the following session call was then refused). Which platform state causes it (an instance still counted after it stopped, one usable placement, or instances left by an earlier rollout) is not readable from the existing receipts, so the scope gains a read-only observe choice of the manual proof dispatch with its function, tests and script, the env.proof container ceiling (max_instances), the pin of the proof ceiling in tests/worker/proof-deploy.test.ts and the matching documentation; placement stays out of scope (a placement field would also need the container key-set test in tests/worker/ingress-routes.test.ts), so a placement need gets its own repair. No obligation or acceptance is removed; production keeps one instance. Planning repair 2026-10-06, third (DLV-34, found by the completion follow-up's live run): with both Containers serving, the live run reached the Account page's idle-expiry stage and failed there. A session issued with the proof-only eight second idle window and renewed by the page's own bootstrap was renewed with the configured thirty minute window, so its logout answered 200 instead of 401; the PRF.07 record lists this as a limit of the proof. The live assertion stays; the proof host's renewal keeps the session's own window instead, so the scope gains that renewal path of src/ArcForges.Cloud/Foundation/SessionService.cs, its tests and the documentation of the renewal. No obligation or acceptance is removed, and production, which serves only Hello, is unchanged. Planning repair 2026-10-08 (DLV-34; P2-021; brief section 2): CLOUD.71 stays complete as history. The React profile bytes it served are superseded by the Blazor WebAssembly profiles of PRF.11 (its start edge is retargeted from PRF.08 to PRF.11 in web.json). Serving the Blazor profiles and the C# static Site from the proof origin is the approved CLOUD.85 (P2-021 section 6), which gates PRF.11. Outcome, validation and evidence above are recorded history and are unchanged. Planning repair 2026-10-09 (P2-026; scope correction): reduced: the React PRF.08 profile bytes, their build and live-script plumbing, the React Web bundling and router-base expectations, and the React interaction budgets are out of scope, not completed; the delivered history is preserved and not extended.
```

```text
Execute ArcForges delivery task CLOUD.72 — Identity production store, identifier source and enrollment family call over the plan-execution port.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\cloud.md (anchor task-cloud-72).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/cloud-72 (python tools/delivery.py claim CLOUD.72 --worker <name>); task branch task/cloud-72 in Cloud; ledger record ledger/tasks/cloud-72.md.
Kind/size: service/M. Baseline: not-started.
Outcome: The Identity module has a production store and identifier source, so its service can be resolved and served. IIdentityStore is implemented by one internal D1 store under the Identity project's own Persistence folder, written only against the Abstractions plan-execution port that COM.16 delivered (named identity plans with exact typed values; no SQL, no table name, no reference to the plan bridge); its commit variants call the named identity plans and the enrollment call executes the registered family `account-enrollment` (plan `families.account-enrollment.create-user`) through a generic family-execution port that this task adds to ArcForges.Cloud.Modules.Abstractions (outside the Identity folder, so every later family participant reuses it) and a Storage.D1 adapter that implements it over the existing shared-family engine, refusing a family or a statement contribution the calling module may not make. IIdentityIdSource is implemented with identifiers from the platform's cryptographic random generator in the canonical lower-case UUID form, so a user, credential or workspace identifier is unpredictable, and a collision is never an overwrite (the primary keys and the revision-zero guards refuse it as a whole-batch precondition and the commit retries with fresh identifiers). The receipt reused-identifier mapping that CLOUD.11 deferred is delivered: a repeated enrollment command with the same content is answered from its receipt as a replay (the service returns CreatedUser=false and the existing user, credential and workspace), a command identifier reused with different content is refused as an identifier conflict, an expired receipt is never executed as a new command, and an unknown outcome is retried only as the same command; the other plan statuses map to the service's typed refusals. The Identity service is registered by composition and resolves. No new plan, table or migration is added.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-22.00 (the production persistence and identifier binding of the core identity model: the production IIdentityStore written against the Abstractions plan-execution port (the named identity plans and the enrollment family call), the production IIdentityIdSource with unpredictable collision-safe identifiers, and the mapping of the receipt's replay and reused-identifier outcomes to the service result (a replayed enrollment answers CreatedUser=false, a reused command identifier with different content is refused); the model, rules, service, plans and family stay with CLOUD.11): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\22-identity-workspace-and-device.md, anchor rule-wp-22.00

Entry condition: adoption slice ADOPT.07.cloud is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] CLOUD.11: the core identity model, the IIdentityStore and IIdentityIdSource ports, the identity plans and the account-enrollment family with their argument builders
- [artifact] COM.16: the generic plan-execution port in the Abstractions project and the Storage.D1 ModuleBinding adapter that implements it over the signed Worker executor
- [artifact] CLOUD.06: the shared-family engine (FamilyUnitOfWork, FamilyExecutor, the closed family registry and the fixed SU-04 lock order)
- [artifact] CLOUD.04: the owner receipt store, the commit tail and the replay and reused-identifier outcomes
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Cloud:src/ArcForges.Cloud.Modules.Identity/Persistence/** (new, internal: the D1 IIdentityStore over IModulePlanPort and the account-enrollment family port, the row codecs from the plans' typed rows to the Core records, and the cryptographically random IIdentityIdSource; no SQL text, no table name, no reference to Storage.D1); Cloud:src/ArcForges.Cloud.Modules.Identity/IdentityModule.cs and Cloud:src/ArcForges.Cloud.Modules.Identity/Core/** (only the Register entry that binds the store and the identifier source with the plan port created for the module's own descriptor, and the minimal Application and Infrastructure edits the replay and reused-identifier mapping needs: the commit outcome gains the replayed and identifier-conflict results, the service answers a replayed enrollment with CreatedUser=false, and the statement builders hand their typed values to the ports; the model, the rules and the plans of CLOUD.11 are unchanged); Cloud:src/ArcForges.Cloud.Modules.Abstractions/Families/** (new and public: the generic family-execution port, a registered family id with the calling module's typed statement contributions by module, class and stable key plus the commit tail in, a typed status out that reuses the plan-execution port's status vocabulary; built from primitives only, referencing no module and no storage type; the plan-execution port of COM.16 under Abstractions/Storage/** is unchanged); Cloud:src/ArcForges.Cloud.Storage.D1/FamilyBinding/** (new folder owned by this task, no overlap with the ModuleBinding folder of COM.16 or the SharedFamilies folder of CLOUD.06: the adapter that implements the Abstractions family port over FamilyUnitOfWork and FamilyExecutor, checks that the calling module is a participant of the family and contributes only statements of its own module, with one explicit reviewed exception: the enrollment initiator also contributes the `workspace` statements, because no Workspace module project exists and CLOUD.11 carries the single-owner workspace provisioning, and maps the executor and receipt outcomes to the typed statuses); Cloud:src/ArcForges.Cloud/Composition/HostModules.cs (only the append that binds the Storage.D1 FamilyBinding adapter to the Abstractions family port, beside the COM.16 binding of the plan-execution port; RES-cloud-host-composition); Cloud:src/**/packages.lock.json and Cloud:tests/**/packages.lock.json (only project-reference entries, if the new files need any; no package coordinate or integrity value changes); Cloud:tests/ArcForges.Cloud.Tests/Identity/** and Cloud:tests/ArcForges.Cloud.Tests/Families/** and Cloud:tests/ArchitectureTests/** (new files and only the minimal edits of the CLOUD.11 tests that the new commit outcomes require: store tests through the plan-port fakes and the SQLite-oracle bridge that COM.16 added, identifier source tests, the replay, reused-identifier, expired and unknown-outcome mapping, family port contract tests, and architecture tests that Identity references only Abstractions and that the Abstractions project still references no module); Cloud:eng/verification/d1-identity-local.ts and Cloud:package.json (only the extension of the existing opt-in local workerd run and no new test file in the test list; never CI; the store and enrollment tests are C# under tests/ArcForges.Cloud.Tests/Identity/** and Families/**, per the P2-021 C#-first re-specification); Cloud:eng/policy/dependency-policy.json and Cloud:eng/policy/dependency-reviews/cloud-72-*.json (new immutable successor chained from the then-active receipt, only because hash-bound project and release inputs change; no coordinate, integrity value or closure entry changes); Cloud:eng/provenance/** (immutable successor release profile, Worker bundle and runtime-notice records only where an existing record binds an input this task changes, the first-party inventory files.json and the deterministic NOTICE.txt); Cloud:docs/identity-core.md (the stated limit that no production store exists is replaced by what this task delivers), Cloud:docs/shared-families.md and Cloud:docs/storage-plans.md and Cloud:AGENTS.md (only factual pointers)
Shared resources (follow the owner protocol): RES-cloud-host-composition (append): Each module registers through its own module entry point and route fragment; the host composition only lists modules; route and binding conflicts are resolved by the integration owner at merge.; RES-architecture-tests (append): Each repository policy task owns its suite; rule additions are append-only.
Unblocks: CLOUD.12, CLOUD.13, CLOUD.20

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline unit tests (C#): the store against the plan-port fakes and the SQLite oracle on the real migrations (every read scoped by realm, every commit variant, a refused guard commits nothing, concurrent enrollments of one credential commit once), the enrollment call through the family port to the real family plan, identifier unpredictability and format (version 4, canonical, no repeat in a large draw, a forced collision is refused whole and retried with fresh identifiers), the replay mapping (same content replays with CreatedUser=false, different content is a conflict, an expired receipt is never executed, an unknown outcome retries only the same command), the family port contract (a non-participant, a foreign statement and an unknown family are refused before the executor; the enrollment initiator's workspace statements are accepted only through the one reviewed exception recorded in writes) and the architecture tests; one explicit local opt-in run against workerd's D1 through the existing harness entry eng/verification/d1-identity-local.ts per docs/validation-policy.md, recorded once as an execution run of C#-owned plans with no TypeScript business assertion; no existing CLOUD.11 assertion is loosened, removed or made conditional (new assertions are additive; a CLOUD.11 case changes only where the new typed commit outcome replaces the value it asserts, and then the replacement is at least as strict, keeps its case and its negative, and is listed in the evidence); no hosted runtime, live-service or browser CI (P2-017).
Completion evidence for the ledger: Store, identifier-source, replay-mapping and family-port test results; the enrollment and concurrent-writer results on the oracle and the local workerd D1 run (recorded once, or recorded as untested); the architecture test results; source commit.
Notes: Planning repair 2026-10-05 (DLV-34: a new task gives work no existing scope could hold; no obligation or acceptance is removed). Design #248 decision 4 left the binding of IIdentityStore to the plan-execution port with no owner, and CLOUD.11's record lists the identifier source and the receipt reused-identifier mapping with it; nothing in the graph owned any of the three. Decisions: (1) one new small task, not an extension of CLOUD.12: CLOUD.12 is an L task whose acceptance needs external provider accounts and DNS that this binding does not, so absorbing it would hold the offline store work behind the Operations Owner, and a separate task keeps the enrollment path testable offline on the oracle and gives CLOUD.13 and later Identity tasks the same base. (2) It starts after COM.16 (the plan-execution port, delivered when merged per DLV-24) and CLOUD.11, and only CLOUD.12 and CLOUD.13 start after it (CLOUD.12 is the first live-store consumer; CLOUD.13 runs the device-revocation family and the Device participant of enrollment through the family port); CLOUD.16 gains a COM.16 edge for its own token store; CLOUD.20 completes after it. GOV.16 needs only the static metadata CLOUD.11 delivered (its edge is on CLOUD.11 and is unchanged), and no in-scope task waits for this one. (3) The COM.16 port refuses a plan whose owner is not the caller, so a shared family plan cannot pass through it; the family-execution port is therefore a new generic port in Abstractions with its own adapter folder in Storage.D1, neither of which overlaps COM.16's folders, and every later family participant (CLOUD.13, CLOUD.39, CLOUD.42, CLOUD.53, CLOUD.63) reuses it. Until the Workspace module has a project, the enrollment initiator contributes the workspace statements by one explicit adapter exception. (4) Identifiers: random version 4 UUIDs from the platform's cryptographic generator (the Entitlement store uses the same form); a replayed enrollment discards the identifiers it generated for the retry. (5) No plan, table or migration changes, so no RES-cloud-storage-plans or migration append; if the replay mapping proves to need one, that is a planning repair. Pattern for every module (decided by the CLOUD.72 planning repair, 2026-10-05): a module project references only the Abstractions project, so each module task binds its own live store itself, under its own Persistence folder, as an internal class written against the Abstractions plan-execution port (IModulePlanPort, COM.16) and registered in the module's own Register entry with the port created for its own descriptor (IModulePlanPortFactory.For); a call to a shared transaction family goes through the Abstractions family port that CLOUD.72 adds. No module task may leave its store unbound while declaring a service that needs one. Planning repair 2026-10-08 (DLV-34; P2-021): the store, identifier-source, replay and family-port tests are C# tests in tests/ArcForges.Cloud.Tests/Identity/** and Families/** with the same cases and negatives; no TypeScript store test is added, and the opt-in workerd run keeps its existing harness entry (eng/verification/d1-identity-local.ts). The reviewed 2026-10-05 workspace exception (the enrollment initiator contributes the workspace statements) stays as recorded in writes and is unchanged by this repair; no external prerequisite or new task is proposed here. No existing CLOUD.11 assertion is loosened. Outcome and evidence are otherwise unchanged.
```

```text
Execute ArcForges delivery task CLOUD.85 — Serve the Blazor WebAssembly Account and Chat profiles and the C# static Site from the proof origin.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\cloud.md (anchor task-cloud-85).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/cloud-85 (python tools/delivery.py claim CLOUD.85 --worker <name>); task branch task/cloud-85 in Cloud; ledger record ledger/tasks/cloud-85.md.
Kind/size: integration/S. Baseline: not-started.
Outcome: Serves the Blazor WebAssembly Account and Chat production profiles and the C# static Site from the proof origin next to the Cloud API. The Cloud Worker's static-assets binding (env.proof only) serves the content-hashed Blazor profile bytes of WEB.40's web-profiles-<sha256>.tar release asset and the C# Site bytes of its web-site-<sha256>.tar release asset (a deterministic tar, D2 option A), after digest verification; /api, /session/v1 and /proof/v1 keep routing to the Worker first; the profiles are served under base href / (the framework stays at the root, and the shells at /account/index.html and /chat/index.html load it) with the exact CSP token set of each surface (App profiles: script-src 'self' 'wasm-unsafe-eval' plus required hashes, never unsafe-eval or unsafe-inline, and style-src 'self'; the public Site keeps its strict set without wasm-unsafe-eval). The Worker stays a thin transport adapter: it makes no business decision and grants no access (P2-021 item 1). This is the serving path that WP-06.05 requires for PRF.11; CLOUD.71 remains complete for the React bytes.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-06.05 (partial: proof-origin serving slice (Blazor and Site bytes served same-origin with /api, /session/v1 and /proof/v1 reaching the Worker first; base href / with the shells at /account/ and /chat/). The deployed-origin proof is PRF.11's full WP-06.05 acceptance.): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\06-aot-jit-and-wasm-publish-proof.md, anchor rule-wp-06.05

Entry condition: adoption slice ADOPT.07.cloud is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] WEB.40: the Blazor WebAssembly profile projects and the C# static Site output (content-hashed bytes and their digests) built by the migration
- [artifact] CLOUD.71: the proof-origin route families (/api, /session/v1 and /proof/v1 reach the Worker first) that CLOUD.71 provides for the React bytes
- [artifact] PRF.07: a deployed Cloud AOT probe reachable same-origin through the proof origin
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Cloud:wrangler.json (env.proof static-assets binding only); Cloud:worker/foundation/** (only if the assets config cannot keep /api, /session/v1 and /proof/v1 on the Worker first); Cloud:eng/verification/proof-deploy.ts (download and digest-verify the Blazor bundle asset); Cloud:eng/verification/proof-cloudflare.ts (download and digest-verify the Blazor bundle asset); Cloud:tests/worker/proof-assets*.test.ts; Cloud:docs/prf-07-foundation-proof.md (served-profiles section and the record near line 395); Cloud:docs/cloud-ingress.md (line 176); Cloud:package.json (only the new test file names in the npm test script); Cloud:eng/provenance/files.json (inventory of changed and added first-party files); Cloud:eng/policy/dependency-policy.json (successor binding of the changed inputs); Cloud:eng/policy/dependency-reviews/cloud-85-r1.json (new immutable receipt, chained from the receipt active on main at the time of the change); Cloud:eng/provenance/artifact-profiles/cloud-release-r<N>.json (derived release profile; N is the next free profile number at the time of the change, not a fixed number); Cloud:tests/worker/proof-cloudflare.test.ts (deploy tests, needs this repair); Cloud:eng/verification/proof-site.ts (optional Site verifier, only if the Site verifier is split out of proof-deploy.ts)
Shared resources (follow the owner protocol): RES-cloud-deployment (append): Bindings are added by the owning module task in its own section, and the Cloud integration owner resolves ordering conflicts at merge. Any task that runs against the deployed test environment holds the lease `leases/res-cloud-deployment` for that live run only, whatever mode it declares for its binding edits; production deployment belongs to release tasks.
Unblocks: PRF.11

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline (CI-eligible) tests in Cloud: route precedence, with /api, /session/v1 and /proof/v1 matched ahead of static assets; digest refusal, with a changed, missing or unexpected Blazor or Site bundle digest refused before serving; the exact CSP token-set assertion on the served App-profile responses (script-src 'self' 'wasm-unsafe-eval' plus required hashes; no unsafe-eval or unsafe-inline; style-src 'self') and the strict no-wasm token set on the public Site; same-origin resolution under base href / from the served route table, with the shells at /account/ and /chat/ loading root framework paths. The deployed proof-origin run of the same checks is PRF.11's local opt-in acceptance, not a hosted CI job (P2-017).
Completion evidence for the ledger: Offline route-precedence, digest-refusal and exact CSP token-set test results in Cloud; digest record of the WEB.40 web-profiles-<sha256>.tar and web-site-<sha256>.tar release assets (the Blazor profile and Site bytes) the proof origin serves; PRF.11's deployed proof-origin same-origin and base-href record cites this task.
Notes: Planning repair 2026-10-08 (DLV-34; P2-021; brief section 6, approved ID CLOUD.85): the serving successor required by WP-06.05 for PRF.11. PRF.11 takes it as a blocking integration completion edge (addComplete in the web patch). Cloud work stays transport only: no business rule or authoritative state enters the Worker, and Node remains wrangler and verification tooling only (P2-021 item 1). Decision basis: P2-021 (decision obligations are reserved for adoption and governance tasks, so the decision is cited here rather than as an obligation). Planning repair 2026-10-09 (DLV-34; P2-026 fix6; S20(b)): the write scope now lists the paths of the phase-2 plan's P0 repair (docs/prf-07-foundation-proof.md, docs/cloud-ingress.md, package.json, eng/provenance/files.json, eng/policy/dependency-policy.json, eng/policy/dependency-reviews/cloud-85-r1.json, the next eng/provenance/artifact-profiles/cloud-release-r<N>.json numbered at the time of the change, tests/worker/proof-cloudflare.test.ts and the optional Site verifier eng/verification/proof-site.ts). The base href is / (D1) and the Site source is WEB.40's web-site-<sha256>.tar release asset (D2-A, S20(a)); those clauses are reworded in the outcome, validation, evidence and the WP-06.05 obligation part. Title, edges and the validation scope are unchanged.
```

```text
Execute ArcForges delivery task CLOUD.84 — Cloud TypeScript reduction: C# generated tables and policy, thin Worker adapters, proof code out of the production bundle.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\cloud.md (anchor task-cloud-84).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/cloud-84 (python tools/delivery.py claim CLOUD.84 --worker <name>); task branch task/cloud-84 in Cloud; ledger record ledger/tasks/cloud-84.md.
Kind/size: service/L. Baseline: not-started.
Outcome: The Cloud Worker (worker/**) contains only the thin Cloudflare platform adapter: Worker fetch entry and routing; ingress transport framing and size/time guards whose limits are generated from C#; Container, Durable Object, Queue and alarm lifecycle classes; D1 batch execution, R2, Workers AI, Vectorize and Static Assets binding facades; operator HMAC transport; and the @arcforges/ai-internal codec. The TypeScript credential, CSRF and Origin edge checks in worker/index.ts and worker/router.ts are kept only under the P2-021 edge-guard rule: C# remains authoritative and enforces the same rule, their parameters and allowlists are generated from the C# source, and the Worker only refuses early (a cost control) and never grants. The method/route table, admission constants, budgets and readiness vocabulary are generated from the C# host source into one generated TypeScript module (worker/generated/cloud-tables.ts) that a generate --check gate verifies; no hand-written copy remains and regex parsing of C# sources is removed. The decisions that move to C#, each with its destination: queue/coordination policy to the C# finite-job runner src/ArcForges.Cloud.Jobs (CLOUD.05); readiness evaluation beyond transport to src/ArcForges.Cloud/Readiness (CLOUD.08); storage-plan authority (plan authoring, the family grammar, the guard checks and the generation of PlanManifest.g.cs, storage/plans/families.expanded.json and worker/storage/plans.generated.ts) to src/ArcForges.Cloud.Storage.D1/Plans (CLOUD.02, CLOUD.04, CLOUD.06, CLOUD.11); correlation validation (worker/ingress/correlation.ts) to the existing src/ArcForges.Cloud/Ingress/Correlation.cs (CLOUD.69; the Worker only forwards correlation values); the D1 migration runner's lease, epoch fence, gating, sequence and receipt decisions to src/ArcForges.Cloud.Storage.D1/MigrationRunner (new), where the Node shim only invokes wrangler with the C#-supplied statements (brief section 5.7; eng/migrations/runner.ts, catalog.ts, sql.ts and clients.ts keep argument passing and wrangler calls only); and the deploy-time environment-to-database selection, release-plan reading and excluded-build and gate refusals (eng/migrations/deploy.ts) to the new folder src/ArcForges.Cloud.Storage.D1/Deploy. C# tests replace the TypeScript tests one-for-one with the same cases and limits in tests/ArcForges.Cloud.Tests/Reduction (new), Generation (new) and Readiness (existing), and the existing tests/ArcForges.Cloud.Tests/IngressCorrelationTests.cs. The production bundle built from the Worker entry contains no proof-only route, fixture or verification code. The Cloud package.json stops depending on the retiring @arcforges/proto and @arcforges/api-client identities; @arcforges/ai-internal is the one npm Contracts dependency. The Kotlin consumer gate (tests/kotlin-consumer and tooling/kotlin.ts) is removed after AND.40 delivers. The D1 migration runner and deployment step remain Node only as the wrangler invocation shim.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-21.00 (partial: the Worker ingress framing and size/time guards keep their limits, generated from C# (P2-021 Decisions 1 and 6), and the generated method/route table is generated from the C# endpoint registration of CLOUD.21 rather than hand-mirrored; the host pipeline behaviour is unchanged): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\21-cloud-host-and-persistence.md, anchor rule-wp-21.00

Entry condition: adoption slice ADOPT.07.cloud is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] CLOUD.01: the thin ingress adapter (worker/index.ts, router.ts, ingress) that this task keeps thin
- [artifact] CLOUD.02: the storage-plan generation that becomes data generated from C#
- [artifact] CLOUD.03: the D1 migration runner's Node wrangler shim and migration tooling delivered by CLOUD.03, whose lease, epoch fence, gating and sequence decisions move to C# in this task
- [artifact] CLOUD.04: the plan authoring that moves to C#
- [artifact] CLOUD.06: the family guard engine that moves to C#
- [artifact] CLOUD.08: the readiness business model that moves to C# and whose vocabulary is generated
- [artifact] CLOUD.11: the identity plans that move to C#
- [artifact] CLOUD.69: the correlation validation that moves to C# (the Worker only forwards)
- [artifact] CLOUD.70: the gated deployment step whose target, release-plan and refusal decisions move to C# under src/ArcForges.Cloud.Storage.D1/Deploy
- [artifact] HAR.40: the C# Harness budget and admission constants that the generated TypeScript module is generated from
Completion prerequisites (may start earlier; cannot complete before these are complete):
- [integration] CLOUD.21: the method/route table is generated from the registered C# public endpoints of CLOUD.21
- [integration] CLOUD.05: the job slice budgets (<=100 items/20s) are generated from the C# finite-job runner of CLOUD.05
- [integration] AND.40: the MAUI Android migration replaces the Kotlin consumer, so the Kotlin consumer CI gate is removed
- [integration] HAR.03: the final worker/harness Durable Object run-stream projection and the worker/index.ts entry that HAR.03 delivers; the static and bundle scans of this task run on them

Permitted write scope: Cloud:worker/index.ts (thin entry and routing; the TypeScript credential, CSRF and Origin edge checks are kept only under the P2-021 edge-guard rule: their parameters and allowlists are read from the generated module, the Worker only refuses early and never grants); Cloud:worker/router.ts (thin routing only; the same edge-guard rule as worker/index.ts); Cloud:worker/ingress/** (thin transport framing and size/time guards with limits generated from C#; the correlation validation in correlation.ts is removed and the Worker only forwards correlation values); Cloud:worker/foundation/** (thin lifecycle and binding adapters only); Cloud:worker/readiness/** (transport only; the readiness model and evaluation move to C# under src/ArcForges.Cloud/Readiness/**); Cloud:worker/storage/** (generated data and thin D1 binding adapters only: plans.generated.ts is regenerated by the C# plan generator, and execute-plan.ts, handler.ts, d1.ts, plan-types.ts and scalars.ts keep only binding and transport); Cloud:worker/private/** (thin adapter only); Cloud:worker/proof-migrations/** (proof-only code: removed from the production bundle path); Cloud:worker/harness/** (thin Durable Object projection and alarm adapters only; HAR.03 and HAR.40 own the files they add; this task completes after HAR.03); Cloud:worker/ai/** (thin ai.internal egress adapter only; HAR.40 owns the files it adds; the MCP HTTP egress route in worker/ai/mcp is out of scope, not completed (P2-026)); Cloud:worker/generated/cloud-tables.ts (new: the generated TypeScript module of the method/route table, admission constants, budgets and readiness vocabulary; produced only by the C# generator in src/ArcForges.Cloud/Generation/**, never hand-edited); Cloud:storage/plans/families.expanded.json (regenerated from the C# single source only; RES-cloud-storage-plans; plan SQL and every module's plan directory are unchanged); Cloud:src/ArcForges.Cloud.Storage.D1/Plans/** (new folder, runtime plan-authority types only, per D3 as adopted by S20(e): the typed plan model that the host and the D1 runner use, with the existing PlanDefinition.cs as the plan type; the storage-plan generator (SQL parsing, shape and table-ownership validation, family grammar and guard checks, and emission) is in Cloud:tools/ArcForges.Cloud.Generation/**, not here); Cloud:src/ArcForges.Cloud.Storage.D1/PlanManifest.g.cs (existing: regenerated by the C# generator above with the same single manifest hash; RES-cloud-storage-plans); Cloud:src/ArcForges.Cloud.Storage.D1/MigrationRunner/** (new folder: the C# D1 migration runner: global sequence check, receipts, the lease and epoch fence held in platform_schema_state, guarded batch construction, and the expand, backfill, cutover and contract gating; it reads the migrations and migrations.lock.json under Migrations/ and edits neither); Cloud:src/ArcForges.Cloud.Storage.D1/Deploy/** (new folder: the environment-to-database selection from the deployment configuration, the reading of the release migration plan, and the excluded-build and gate refusals, decided in C#; the Node caller keeps argument passing only); Cloud:src/ArcForges.Cloud/Generation/** (new folder, runtime decision types only, per D3 as adopted by S20(e): the admission constants, budgets and readiness vocabulary types that the host reads; the generator entry point that emits worker/generated/cloud-tables.ts is in Cloud:tools/ArcForges.Cloud.Generation/**, not here); Cloud:src/ArcForges.Cloud/Readiness/** (existing folder, HostReadiness.cs: readiness evaluation beyond transport); Cloud:src/ArcForges.Cloud/Ingress/Correlation.cs (existing and authoritative: changed only if a TypeScript correlation rule has no C# equivalent, and then the C# rule and its test are added here); Cloud:tests/ArcForges.Cloud.Tests/Reduction/** (new folder: C# replacements, one-for-one, for the moved queue/coordination, storage-plan, migration-runner and deploy-decision tests); Cloud:tests/ArcForges.Cloud.Tests/Generation/** (new folder: generate --check parity and the generated route, budget and vocabulary tables); Cloud:tests/ArcForges.Cloud.Tests/Readiness/** (existing folder, HostReadinessTests.cs: C# replacements for the readiness-evaluate and readiness-model tests); Cloud:tests/ArcForges.Cloud.Tests/IngressCorrelationTests.cs (existing: the C# replacement for tests/worker/ingress-correlation.test.ts); Cloud:tests/ArchitectureTests/WorkerAdapter/** (new folder: adapter-boundary and production-bundle architecture tests); Cloud:tests/ArchitectureTests/EvaluatedRepositoryGate.cs (D9 hosted gate wiring, added by the fix6 review: the WorkerAdapter scan runs from this class, which the existing ci.yml step with --filter-class ArcForges.Cloud.ArchitectureTests.EvaluatedRepositoryGate already runs; CloudRepository.cs is not added); Cloud:tests/worker/** (adapter tests kept; each business test is removed only after its C# replacement passes, including ingress-correlation.test.ts, d1-migration-runner.test.ts, d1-migration-deploy*.test.ts, storage-plans-generator.test.ts, storage-plan-ownership.test.ts, storage-plan-vectors.test.ts, readiness-evaluate.test.ts and readiness-model.test.ts); Cloud:tests/kotlin-consumer/** (removed after AND.40 delivers); Cloud:eng/verification/** except eng/verification/d1-identity-local.ts, which CLOUD.72 owns, and eng/verification/physical-schema.ts, which is Node build tooling under D4 and D5 and is not written by CLOUD.84 (proof-only and local verification drivers are removed from the production bundle path; eng/verification/storage-plans.ts is removed once the C# plan generator passes its --check gate; generation checks are kept); Cloud:eng/migrations/** (Node wrangler invocation shim only: runner, catalog, sql and clients keep argument passing and wrangler calls; the lease, fence, gating and sequence decisions are C# under src/ArcForges.Cloud.Storage.D1/MigrationRunner and the deploy decisions under src/ArcForges.Cloud.Storage.D1/Deploy); Cloud:tooling/project.ts, Cloud:tooling/build-identity.ts and Cloud:tooling/protocol.ts (remove the @arcforges/proto and @arcforges/api-client usage; the C# client is the source); Cloud:tooling/kotlin.ts (removed after AND.40 delivers); Cloud:.github/workflows/ci.yml (remove the Kotlin consumer gate step after AND.40; add the generate --check gates for worker/generated and the C# plan generator; no new hosted job); Cloud:package.json (remove the retiring @arcforges/proto and @arcforges/api-client; @arcforges/ai-internal stays); Cloud:package-lock.json (manifest change only); Cloud:tsconfig.json and Cloud:tsconfig.worker.json; Cloud:wrangler.json (production bundle without proof-only code; no binding change; RES-cloud-deployment); Cloud:eng/policy/dependency-policy.json (new immutable successor chained from the then-active receipt; ordered behind CLOUD.72 by its start edge); Cloud:eng/policy/dependency-reviews/cloud-84-*.json (new immutable successor records); Cloud:eng/provenance/records/cloud-84-*.json (new immutable successor records only, named for this task); Cloud:eng/provenance/files.json (only where an existing record binds an input this task changes; ordered behind CLOUD.02, CLOUD.03, CLOUD.04, CLOUD.06, CLOUD.70 and CLOUD.72 by start edges); Cloud:docs/cloud-readiness.md (factual update: readiness decisions now in C#), Cloud:docs/cloud-ingress.md (factual update: the adapter boundary and the edge-guard rule) and Cloud:docs/d1-migration-deployment.md (factual update of the runner and deploy decisions, now C#); Cloud:worker/proof/entry.ts (new: the separate proof Worker entry, D1); Cloud:tooling/cloudflare.ts (the proof bundle upload in deploy:proof, D1); Cloud:tools/ArcForges.Cloud.Generation/** (new non-published tool project for the C# generator entry points, D3; the published projects keep only runtime decision types)
Shared resources (follow the owner protocol): RES-cloud-deployment (append): Bindings are added by the owning module task in its own section, and the Cloud integration owner resolves ordering conflicts at merge. Any task that runs against the deployed test environment holds the lease `leases/res-cloud-deployment` for that live run only, whatever mode it declares for its binding edits; production deployment belongs to release tasks.; RES-cloud-storage-plans (append): Each module owns its own plan directory; the plan-manifest hash is regenerated by the author after rebase and checked in CI.; RES-architecture-tests (append): Each repository policy task owns its suite; rule additions are append-only.
Unblocks: CON.40

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline and static checks only (P2-017, P2-024): generate --check receipts for worker/generated/cloud-tables.ts and for the C# plan generator, which must reproduce worker/storage/plans.generated.ts, storage/plans/families.expanded.json and PlanManifest.g.cs with one manifest hash; a static scan finds no admission, budget, method-table, correlation-validation, readiness or plan-authority literal in worker/ outside the generated module; the static scan of worker/ingress/correlation.ts finds no correlation rule beyond forwarding; the edge-guard scan of worker/index.ts and worker/router.ts finds that every credential, CSRF and Origin check reads its parameters from the generated module, that it only refuses, and that C# enforces the same rule under C# tests; a bundle scan of the Worker entry finds no proof-only symbol, route, fixture or eng/verification code; each retired TypeScript test is replaced by a C# test with the same cases, negatives and limits (job slices <=100 items/20 s, body caps, readiness wait, stream lifetime, leases, migration fences and the other recorded limits), including the migration-runner cases of d1-migration-runner.test.ts (stale migrator refused, interrupted run resumed from statements_done, merged-migration checksum refusal) run by the C# runner against the SQLite oracle in tests/ArcForges.Cloud.Tests/Reduction; Native AOT host build on Windows and in WSL2 Debian; and a standing C# architecture check (P2-021 item 1, P2-026 S16(b)): tests/ArchitectureTests/WorkerAdapter scans every worker/** source file and fails on any business decision, authoritative state or business constant outside the generated module and the thin adapters; the Kotlin consumer gate is removed only after AND.40 is delivered.
Completion evidence for the ledger: generate --check receipts for worker/generated/cloud-tables.ts and for the C# plan generator outputs (worker/storage/plans.generated.ts, storage/plans/families.expanded.json, PlanManifest.g.cs); the bundle-scan receipt for the production Worker entry; the static-scan receipt for worker/ingress/correlation.ts; the edge-guard scan receipt for worker/index.ts and worker/router.ts; the one-for-one TypeScript to C# test mapping, including tests/worker/ingress-correlation.test.ts, d1-migration-runner.test.ts, d1-migration-deploy*.test.ts and the readiness and plan tests; the C# migration-runner oracle results; the commit that removes the Kotlin consumer gate after AND.40; Native AOT build results on Windows and WSL2 Debian.
Notes: Planning repair 2026-10-08 (DLV-34; P2-021; brief section 5.7 and coordinator adjudications 5 and 7): new task; no obligation or acceptance is removed. The TypeScript credential, CSRF and Origin edge checks are kept under the P2-021 edge-guard rule (C# authoritative; generated parameters; refuse only, never grant), so no user decision is needed for them. The D1 migration runner's lease, fence, gating and sequence decisions move to C# (src/ArcForges.Cloud.Storage.D1/MigrationRunner); Node only invokes wrangler. Start edges, each a composed artifact (DLV-07) or an ordering on the TypeScript surface this task reduces: CLOUD.01, CLOUD.02, CLOUD.03, CLOUD.04, CLOUD.06, CLOUD.08, CLOUD.11, CLOUD.69 and CLOUD.70 supply the delivered shapes it reduces (the package.json overlaps with these are ordered by these edges); HAR.40 supplies the C# Harness budgets and admission constants that the generated module is generated from; Shared-file overlaps covered by declared resources or start edges: wrangler.json with CLOUD.07 and HAR.40, and worker/index.ts with HAR.03 and HAR.40 (RES-cloud-deployment, append); eng/verification/d1-identity-local.ts is owned by CLOUD.72 and excluded from this task's writes. Completion edge to HAR.03 (DLV-09): the bundle and static scans of this task run against the final worker/harness adapter code that task delivers; the MCP egress route is out of scope (P2-026). CLOUD.05 supplies the budgets through its completion edge. AND.40 must not start on this task; this task completes after AND.40. Cloud package.json has no declared shared resource; the coordinator decides whether to declare one. Coordinator adjudication 2026-10-08 (P2-021 item 1): after this task Node in the Cloud repository only invokes wrangler and runs the TypeScript tests of the thin TypeScript adapters (tests/worker/**); every other TypeScript build checker or generator under tooling/** and eng/verification/** that makes a policy or business decision (provenance, licence, dependency policy, build identity, plan and table generation) is migrated to C# within this task or retired. Planning repair 2026-10-08 (DLV-34; coordinator adjudication, brief section 10): the start edge on CLOUD.72 only ordered the dependency-policy receipt chain; it is removed. The successor receipt of this task chains from the receipt active on main at merge, as every successor receipt does. Planning repair 2026-10-09 (P2-026; scope correction): reduced: the MCP HTTP egress route in worker/ai/mcp and its egress test are out of scope, not completed; the Vectorize binding facade stays (P2-026 search decision). Planning repair 2026-10-09 (DLV-34; P2-026 fix6; S20(b)): the write scope adds the separate proof entry worker/proof/entry.ts and tooling/cloudflare.ts for the proof bundle upload (D1), and the non-published generator tool project tools/ArcForges.Cloud.Generation/** (D3). The WorkerAdapter architecture test (tests/ArchitectureTests/WorkerAdapter/**) is listed, and D9's hosted gate wiring is the exact path tests/ArchitectureTests/EvaluatedRepositoryGate.cs, added by the fix6 review (the existing ci.yml step with --filter-class ArcForges.Cloud.ArchitectureTests.EvaluatedRepositoryGate runs it, so ci.yml needs no D9 edit). Node build tooling stays under S17(a) (D4), including the physical-schema generator eng/verification/physical-schema.ts (D5), which is recorded here as Node build tooling and is not written by this task. The deploy decision runs in the candidate job and is sealed into the candidate (D6), and proof-only coordination stays TypeScript in the proof bundle until CLOUD.05 (D16). Planning repair 2026-10-09 (DLV-34; P2-026 fix6 review; S20(b), S20(e)): the generator placement follows D3 as adopted by S20(e). The published-project entries src/ArcForges.Cloud/Generation/** and src/ArcForges.Cloud.Storage.D1/Plans/** are narrowed to runtime decision types, and the generator entry points (the table generator and the storage-plan generator) are in tools/ArcForges.Cloud.Generation/**. Generator code placed outside that tool project would be a deviation from D3 that needs its own review. The physical-schema generator is excluded from the eng/verification/** entry (D4, D5). The D9 gate wiring is tests/ArchitectureTests/EvaluatedRepositoryGate.cs; CloudRepository.cs is not added, because the scan needs only the repository root that CloudRepository.FindRoot already provides.
```
