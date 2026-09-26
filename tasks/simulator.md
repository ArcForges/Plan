# ArcForges delivery task prompts — ArcScope Cloud simulator

Generated from Design `docs/planning/delivery/delivery-graph.json` by `tools/delivery.py`; do not edit by hand.
Each block is self-contained. Claim a task only when `python tools/delivery.py ready` lists it, with
`python tools/delivery.py claim <TASK-ID> --worker <name>`, then follow `arcforges-implementation.md`.
Tasks are ordered by lane for reading; the order is not a schedule.

## ArcScope Cloud simulator

```text
Execute ArcForges delivery task SIM.01 — Simulation definitions, immutable scenario versions and bounded AST evaluator.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\simulator.md (anchor task-sim-01).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/sim-01 (python tools/delivery.py claim SIM.01 --worker <name>); task branch task/sim-01 in Cloud; ledger record ledger/tasks/sim-01.md.
Kind/size: service/L. Baseline: not-started.
Outcome: Definitions and immutable scenario versions exist; the channel schema (stable ids, value types, units, rate, timestamp semantics) and the V1 generator set (constant, sine, square, triangle, sawtooth, seeded noise, seeded random walk, pulse, step sequence, CSV replay) are defined; the bounded AST (constants, time/tick, channel references, arithmetic, comparison, conditionals, allowlisted numeric functions) validates acyclic dependencies and depth/node-count/per-tick-operation bounds before admission, with no scripting/dynamic compilation/reflection/file access/networking possible.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-51.00 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\51-arcscope-cloud-simulator.md, anchor rule-wp-51.00

Entry condition: adoption slice ADOPT.07.simulator is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] CLOUD.02: the module-boundary pattern the other 20 Cloud modules follow ('Twenty-one module boundaries')
- [contract] CON.21: published SimulationService definition and scenario-version records
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Cloud:src/Cloud/ArcForges.Cloud.Modules.Scope/Definitions/**; Cloud:src/Cloud/ArcForges.Cloud.Modules.Scope/Ast/**; Cloud:tests/Cloud.Tests.Integration/Scope/Ast/**
Shared resources (follow the owner protocol): RES-cloud-d1-migrations (append): One global D1 migration sequence: each module task authors migrations under its module prefix; the integration owner assigns the global sequence number at merge, regenerates the plan manifest and rejects edits to merged migrations; the migrator applies in sequence with receipts.
Unblocks: SIM.02, SIM.08, SIM.10

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): malformed-AST corpus rejected before any side effect; cyclic-dependency case; each bound exceeded; definition-edit-does-not-affect-existing-runs test; CSV replay with bounded parse report; URL-fetch/host-file-read/cross-workspace-reference each denied — pure in-process unit tests, no D1/R2/host needed yet
Completion evidence for the ledger: AST bounds, cyclic-dependency and sandbox-denial results
Notes: Per producer-artifacts-and-integration.md's WP51 row, this and SIM.02 are exactly the permitted early substitute tier: independent fixed generator vectors, built and proven BEFORE any real D1/R2 integration. The initial simulator execution profile (architecture/23-simulator-and-interchange.md §6, af-sim.v1: generator formulas, RNG spec, AST depth/node/eval limits, duration/batch/concurrency/queue/memory bounds) is already frozen design, not a start edge — implemented directly.
```

```text
Execute ArcForges delivery task SIM.02 — Deterministic generators, seeded RNG and fault profiles (algorithmic determinism).

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\simulator.md (anchor task-sim-02).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/sim-02 (python tools/delivery.py claim SIM.02 --worker <name>); task branch task/sim-02 in Cloud; ledger record ledger/tasks/sim-02.md.
Kind/size: service/L. Baseline: not-started.
Outcome: Same seed and profile produce identical canonical hashes; a changed seed produces different data; every injected fault carries provenance/counters and is exactly positioned; RNG streams are provably independent across channels and fault sources.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-51.01 (the pure-algorithmic half: fixed logical ticks driving canonical data; independently seeded RNG per channel and per fault source; the execution profile pinning numeric/RNG/generator/encoding versions; fault profiles (latency, jitter, drop, duplicate, reorder, disconnect, malformed frame, outlier) at explicit logical boundaries with provenance and counters; same-seed-same-hash and changed-seed-different-data tests; exact fault positions; one channel's RNG not perturbing another's): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\51-arcscope-cloud-simulator.md, anchor rule-wp-51.01

Entry condition: adoption slice ADOPT.07.simulator is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] SIM.01: definitions, channel schema and AST evaluator
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Cloud:src/Cloud/ArcForges.Cloud.Modules.Scope/Generators/**; Cloud:src/Cloud/ArcForges.Cloud.Modules.Scope/Faults/**; Cloud:tests/Cloud.Tests.Integration/Scope/Generators/**
Unblocks: SIM.03, SIM.08

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): pure in-process determinism tests (hash equality, seed sensitivity, fault-position exactness, RNG-stream independence) — no host/D1/R2 needed for this half
Completion evidence for the ledger: determinism and fault-position results (algorithmic tier)
Notes: WP-51.01's remaining requirement — identical hashes under real-time vs accelerated pacing, and the SimulationPacer state-diagram/wake/retry/cold-start exercise plus 24h pacing/cost recording — needs the real SimulationPacer and is carried as part of SIM.03's obligations/testing instead, since it cannot be exercised before that component exists. See SIM.03.
```

```text
Execute ArcForges delivery task SIM.03 — Fenced slices and SimulationPacer (DO alarm coordinator, bounded Container segments, D1 checkpoint/fence).

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\simulator.md (anchor task-sim-03).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/sim-03 (python tools/delivery.py claim SIM.03 --worker <name>); task branch task/sim-03 in Cloud; ledger record ledger/tasks/sim-03.md.
Kind/size: service/XL. Baseline: not-started.
Outcome: Deterministic committed samples and restart recovery pass under real DO alarm delivery, Container execution and D1 checkpoint/fence; the proposed 5s latency is measured and recorded, never claimed as hard real time; every SimulationPacer state-diagram race (duplicate alarm, exhausted retry, sleeping Container, pause/cancel race, duplicate segment, delayed catch-up, accelerated mode) passes.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-51.02 (full: architecture-23 DO alarm integration owner plus bounded Container segments, D1 checkpoint/fence/next_due_at, minutely rescue scan; default 1s and 0.25-10s segment bounds; no permanent hosted-service loop): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\51-arcscope-cloud-simulator.md, anchor rule-wp-51.02
- WP-51.01 (the real-host half: identical hashes under real-time and accelerated pacing; exercise the SimulationPacer state diagram (duplicate/delayed alarm, exhausted automatic retries plus Cron rescue, Container cold start, pause/resume, epoch loss); record 24-hour run cost, alarm/Container/Queue counts and end-to-end pacing distribution against the proposed 5-second target, no hard real-time claim): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\51-arcscope-cloud-simulator.md, anchor rule-wp-51.01
- WP-51:slice-recovery-acceptance-body-text-betw 'Slice recovery acceptance' body text (between §5 and §6, no substep id): kill the real Container before D1 publication, after the guarded segment/checkpoint/outbox batch, and before/after alarm scheduling; race a duplicate alarm with Cron rescue; assert one committed segment per run/range, deterministic continuation, no lost next-due intent, rejection of stale fences; alarm delivery itself may repeat; use the bounded mechanism in architecture 23 §1.2, never interactive BEGIN/COMMIT or an in-memory continuation loop ('Slice recovery acceptance' body text (between §5 and §6, no substep id): kill the real Container before D1 publication, after the guarded segment/checkpoint/outbox batch, and before/after alarm scheduling; race a duplicate alarm with Cron rescue; assert one committed segment per run/range, deterministic continuation, no lost next-due intent, rejection of stale fences; alarm delivery itself may repeat; use the bounded mechanism in architecture 23 §1.2, never interactive BEGIN/COMMIT or an in-memory continuation loop; package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\51-arcscope-cloud-simulator.md, package-level obligation

Entry condition: adoption slice ADOPT.07.simulator is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] SIM.02: deterministic generators/faults
- [artifact] CLOUD.05: published finite-durable-jobs mechanism (DO alarm scheduling, the generic durable-job abstraction a SimulationRun specialises per WP-51 BR-01)
- [artifact] CLOUD.06: published shared atomic families and claims mechanism (lease fencing)
- [artifact] CLOUD.07: published capacity and Container/D1 integration producer mechanism
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Cloud:src/Cloud/ArcForges.Cloud.BackgroundJobs/SimulationPacer/**; Cloud:tests/Cloud.Tests.Integration/Scope/Pacer/**
Shared resources (follow the owner protocol): RES-cloud-leased-singletons (append): Each publication watermark, Durable Object alarm namespace and R2 prefix has exactly one owning module task; others use its published port; names are reserved in the binding plan before first use.
Unblocks: SIM.04, SIM.07, SIM.08

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): at-least-once alarm, exhausted retry, sleeping Container, pause/cancel race, duplicate segment, delayed catch-up, accelerated mode, and the full slice-recovery Container-kill matrix — this genuinely needs a real (local/dev) Cloud host+D1+Container environment, kept to local/affected-scope per P2-017, not hosted CI
Completion evidence for the ledger: replica contention, fenced takeover, bounded-batch and slice-recovery results; determinism/pacing-equality/fault-position results carried over from WP-51.01's real-host half
Notes: This is the highest-complexity task in the whole area (XL): it is the first place WP51 genuinely needs the real Cloud host, and it deliberately folds in WP-51.01's real-pacing half plus the WP51-level 'Slice recovery acceptance' paragraph, none of which can be honestly tested before SimulationPacer itself exists.
```

```text
Execute ArcForges delivery task SIM.04 — Canonical publication, checkpoints and recovery.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\simulator.md (anchor task-sim-04).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/sim-04 (python tools/delivery.py claim SIM.04 --worker <name>); task branch task/sim-04 in Cloud; ledger record ledger/tasks/sim-04.md.
Kind/size: service/L. Baseline: not-started.
Outcome: Canonical batches are written as immutable objects; manifest entries carry run/profile identity, sequence, logical range, count, encoding, byte length and hash; the manifest row is the commit point with the checkpoint advanced in the same transaction; incomplete objects are invisible and swept; recovery produces byte-identical remaining canonical data across pause/resume, host loss and lease takeover; real Entitlement/Scope/Resource quota is reserved and the current monotonic lease fence is verified in every commit.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-51.03 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\51-arcscope-cloud-simulator.md, anchor rule-wp-51.03

Entry condition: adoption slice ADOPT.07.simulator is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] SIM.03: fenced execution producing ticks to publish
- [artifact] CLOUD.42: published blob lifecycle mechanism (immutable object write, incomplete-object sweep)
- [artifact] CLOUD.04: published receipts/outbox/archive transactional-commit pattern
- [artifact] COM.07: published quota/usage/storage accounting mechanism
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Cloud:src/Cloud/ArcForges.Cloud.Modules.Scope/Publication/**; Cloud:tests/Cloud.Tests.Integration/Scope/Publication/**
Shared resources (follow the owner protocol): RES-cloud-d1-migrations (append): One global D1 migration sequence: each module task authors migrations under its module prefix; the integration owner assigns the global sequence number at merge, regenerates the plan manifest and rejects edits to merged migrations; the migrator applies in sequence with receipts.; RES-cloud-leased-singletons (append): Each publication watermark, Durable Object alarm namespace and R2 prefix has exactly one owning module task; others use its published port; names are reserved in the binding plan before first use.
Unblocks: SIM.05, SIM.08

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): stale-holder-resumes-after-takeover; cancellation racing segment promotion and quota release; pause/resume producing same remaining data; host loss/takeover producing no duplicate/no missing range; crash-between-object-write-and-manifest-commit leaving a swept invisible object; committed manifest row never referencing an unverified object — real local Cloud host/D1/R2 environment, local/affected-scope per P2-017
Completion evidence for the ledger: recovery equality across pause, host loss and takeover
```

```text
Execute ArcForges delivery task SIM.05 — Cloud-side simulation.* operations, manifest listing and segment fetch.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\simulator.md (anchor task-sim-05).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/sim-05 (python tools/delivery.py claim SIM.05 --worker <name>); task branch task/sim-05 in Cloud; ledger record ledger/tasks/sim-05.md.
Kind/size: service/M. Baseline: not-started.
Outcome: The eleven simulation.* operations are durable, idempotent and expected-state; a client can list authorised manifests and fetch segments resumably with hash verification; state polling works with realtime disabled.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-51.04 (the Cloud API half: the eleven simulation.* operations as durable, idempotent, expected-state commands; authorised manifest listing; resumable hash-verifiable segment fetch over HTTP or object storage; revision-/cursor-based state polling): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\51-arcscope-cloud-simulator.md, anchor rule-wp-51.04

Entry condition: adoption slice ADOPT.07.simulator is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] SIM.04: published manifests/checkpoints to expose
- [artifact] CLOUD.21: published endpoint mapping and validation pattern
- [artifact] CLOUD.24: published idempotency and rate-limiting mechanism
- [contract] CON.21: published SimulationService operations
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Cloud:src/Cloud/ArcForges.Cloud.PublicApi/Scope/**; Cloud:tests/Cloud.Tests.Integration/Scope/Api/**
Shared resources (follow the owner protocol): RES-cloud-leased-singletons (append): Each publication watermark, Durable Object alarm namespace and R2 prefix has exactly one owning module task; others use its published port; names are reserved in the binding plan before first use.
Unblocks: SIM.06, SIM.08, SIM.09

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): duplicate/stale/out-of-order commands; terminal-run resists resurrection; hash-mismatched segment rejected; reconnect-with-realtime-disabled proves polling is a complete authoritative fallback — real local Cloud host per P2-017
Completion evidence for the ledger: command idempotency and realtime-disabled fallback results (Cloud-side)
```

```text
Execute ArcForges delivery task SIM.06 — ArcScope-side simulated DataSource and native ingestion.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\simulator.md (anchor task-sim-06).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\ArcScope (integration owner: ArcScope integration owner, the holder of roles/integration-arcscope).
Claim and handoff record: claims/sim-06 (python tools/delivery.py claim SIM.06 --worker <name>); task branch task/sim-06 in ArcScope; ledger record ledger/tasks/sim-06.md.
Kind/size: service/L. Baseline: not-started.
Outcome: A SimulatedDataSource adapter feeds the ordinary ArcScope acquisition pipeline; simulated data is usable in every normal ArcScope workflow (session, capture, decoder, measurement, report) while remaining labelled synthetic everywhere, including through export/copy; with realtime disabled, a client reaches the same state via the polling fallback.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-51.04 (the ArcScope consumer half: feed retained canonical simulator output through the existing Scope measurement/replay consumer using its recorded profile and configuration; simulation labels remain synthetic, separate from AI origin; recompute statistical/pulse fixtures without changing measurement meaning or treating simulation as hardware evidence; ArcScope's clearly synthetic DataSource feeding the normal acquisition pipeline; seed and profile provenance surviving export and copy; simulated data flowing through session/capture/decoder/measurement/report unchanged; synthetic labelling surviving export): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\51-arcscope-cloud-simulator.md, anchor rule-wp-51.04
- WP-51:7-required-evidence-addition-canonical-s §7 required evidence addition (canonical simulator replay retains measurement profile and synthetic provenance) (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\51-arcscope-cloud-simulator.md, package-level obligation

Entry condition: adoption slice ADOPT.05.simulator is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] SIM.05: Cloud-side simulation.* operations and segment fetch
- [contract] CON.21: published generated C# SimulationService client and records
- [artifact] SCOPE.01: the DataSource/SourceAdapter contract
- [artifact] SCOPE.14: the real measurement/replay consumer
- [artifact] SCOPE.24: import/export bundle format with simulator-provenance fields
Completion prerequisites (may start earlier; cannot complete before these are complete):
- [integration] SIM.09: the end-to-end real AOT simulation -> R2 -> native ingest/measurement/report proof

Permitted write scope: ArcScope:src/ArcScope/ArcScope.Acquisition/Adapters/Simulation/**; ArcScope:src/ArcScope/ArcScope.Desktop/Simulation/**; ArcScope:tests/ArcScope.Tests.Integration/Simulation/**
Shared resources (follow the owner protocol): RES-arcscope-format-fixtures (append): Fixtures are added per task under its own subdirectory; manifests are append-only.; RES-cloud-leased-singletons (append): Each publication watermark, Durable Object alarm namespace and R2 prefix has exactly one owning module task; others use its published port; names are reserved in the binding plan before first use.
Unblocks: SIM.08, SIM.09

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): simulated data flowing through session/capture/decoder/measurement/report unchanged; synthetic labelling surviving export; realtime-disabled polling fallback proof
Completion evidence for the ledger: native ingestion and synthetic-labelling results
```

```text
Execute ArcForges delivery task SIM.07 — Limits, entitlement and lifecycle.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\simulator.md (anchor task-sim-07).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/sim-07 (python tools/delivery.py claim SIM.07 --worker <name>); task branch task/sim-07 in Cloud; ledger record ledger/tasks/sim-07.md.
Kind/size: service/L. Baseline: not-started.
Outcome: Deployment policy bounds (channels, rates, duration, AST work, per-workspace/global concurrency, queue/wait time, storage, egress, retention) are enforced before and during execution with capacity reservation; service-entitlement gating is independent of AI credits; term expiry/suspension stops generation at a durable boundary as canceled with reason; a 24-hour bounded-resource soak holds within bounds.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-51.05 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\51-arcscope-cloud-simulator.md, anchor rule-wp-51.05

Entry condition: adoption slice ADOPT.07.simulator is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] SIM.03: real execution loop to enforce limits against
- [artifact] COM.05: published entitlement resolver
- [artifact] COM.07: published quota/usage/storage accounting
- [artifact] COM.12: published service term/replenishing capacity mechanism
- [artifact] POL.03: published compiled hard limits mechanism
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Cloud:src/Cloud/ArcForges.Cloud.Modules.Scope/Limits/**; Cloud:tests/Cloud.Tests.Integration/Scope/Limits/**
Shared resources (follow the owner protocol): RES-cloud-leased-singletons (append): Each publication watermark, Durable Object alarm namespace and R2 prefix has exactly one owning module task; others use its published port; names are reserved in the binding plan before first use.
Unblocks: SIM.08

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): quota exhaustion before side effects; cross-workspace denial; term expiring mid-run; suspension mid-run; storage exhaustion; retention pass with active readers; partial-cancellation reporting partial; 24-hour bounded-resource soak — real local Cloud host, local/affected-scope per P2-017 (the 24h soak is the one long-running exception explicitly required by this substep)
Completion evidence for the ledger: limit enforcement, entitlement, expiry and 24-hour soak results
```

```text
Execute ArcForges delivery task SIM.08 — Owned-artifact verification and real integration.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\simulator.md (anchor task-sim-08).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/sim-08 (python tools/delivery.py claim SIM.08 --worker <name>); task branch task/sim-08 in Cloud; ledger record ledger/tasks/sim-08.md.
Kind/size: service/M. Baseline: not-started.
Outcome: Real AOT simulation -> R2 verified publication -> ArcScope ingest/measurement proves deterministic results and failure recovery, with no Workers AI dependency or AI debit; PG-14b evidence recorded, including the 24-hour soak.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-51.90 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\51-arcscope-cloud-simulator.md, anchor rule-wp-51.90
- WP-51:8-additional-completion-requirement-the §8 additional completion requirement: the simulator remains an optional later source for already-defined measurement semantics, never a prerequisite for the earlier replay-based analysis package (confirms WP-34 does not wait on WP-51) (§8 additional completion requirement: the simulator remains an optional later source for already-defined measurement semantics, never a prerequisite for the earlier replay-based analysis package (confirms WP-34 does not wait on WP-51)): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\51-arcscope-cloud-simulator.md, package-level obligation

Entry condition: adoption slice ADOPT.07.simulator is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] SIM.01: all SIM tasks complete to assemble
- [artifact] SIM.02: as above
- [artifact] SIM.03: as above
- [artifact] SIM.04: as above
- [artifact] SIM.05: as above
- [artifact] SIM.06: as above
- [artifact] SIM.07: as above
Completion prerequisites (may start earlier; cannot complete before these are complete):
- [integration] SIM.09: completed end-to-end proof

Permitted write scope: Cloud:docs/wp-51-integration-receipt.md
Unblocks: REL.06

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): real AOT simulation -> R2 verified publication -> ArcScope ingest/measurement; no Workers AI dependency; proportionate under P2-017 given this is explicitly a real-service/real-storage/real-native-adapter gate (PG-14b text: 'preview/test fakes are insufficient')
Completion evidence for the ledger: owned-artifact and real-integration receipt covering the full SIM-01..SIM-20 acceptance list
Notes: WP-51 executes in Phase J specifically because it needs WP-42/WP-44's real commercial admission, unlike the desktop-only WP33/34 (Phase H). This ordering is already correct in the source design; nothing to change here.
```

```text
Execute ArcForges delivery task SIM.09 — Real Cloud->R2->ArcScope-native simulator closure: hash/timebase/provenance proof against WP34 measurement/report and WP35 import/portability.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\simulator.md (anchor task-sim-09).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/sim-09 (python tools/delivery.py claim SIM.09 --worker <name>); task branch task/sim-09 in Cloud; ledger record ledger/tasks/sim-09.md.
Kind/size: integration/M. Baseline: not-started.
Outcome: A real generated simulation run, published through real R2-verified segments, ingested by ArcScope's real (non-simulator) measurement/report/import-export consumers, with hash/timebase/provenance checked end to end and stale grant/fence attempts refused. No simulator fixture stands in for a hardware claim anywhere in this chain.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-51.04 (final-review closure paragraph: real service-authorized R2 segments; consume WP34 measurement/report and WP35 import/portability outputs; Cloud->R2->native hash/timebase/provenance check; stale grant/fence refusal): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\51-arcscope-cloud-simulator.md, anchor rule-wp-51.04
- WP-51:required-implementation-and-closure-from 'Required implementation and closure from the final review' paragraph (real service-authorized R2 segments; consume WP34 measurement/report and WP35 import/portability outputs; Cloud->R2->native hash/timebase/provenance check; stale grant/fence refusal) (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\51-arcscope-cloud-simulator.md, package-level obligation

Entry condition: adoption slice ADOPT.07.simulator is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] SIM.05: real, delivered outcome of SIM.05 (Cloud-side simulation.* operations, manifest listing and segment fetch)
- [artifact] SIM.06: real, delivered outcome of SIM.06 (ArcScope-side simulated DataSource and native ingestion)
- [artifact] SCOPE.14: real, delivered outcome of SCOPE.14 (Measurements: scope.measurement.v1)
- [artifact] SCOPE.18: real, delivered outcome of SCOPE.18 (Reports and reproducibility)
- [artifact] SCOPE.24: real, delivered outcome of SCOPE.24 (Import, export and format fixtures)
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: 
Unblocks: SIM.06, SIM.08

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Local real-integration run of the affected scenario in an existing environment, recorded once; offline and static checks in CI; no hosted runtime, device, browser, live-service or inference CI (P2-017).
Completion evidence for the ledger: A real generated simulation run, published through real R2-verified segments, ingested by ArcScope's real (non-simulator) measurement/report/import-export consumers, with hash/timebase/provenance checked end to end and stale grant/fence attempts refused. No simulator fixture stands in for a hardware claim anywhere in this chain.
```

```text
Execute ArcForges delivery task SIM.10 — Real ArcScope simulator admission against deployed capacity/SimulationPacer.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\simulator.md (anchor task-sim-10).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/sim-10 (python tools/delivery.py claim SIM.10 --worker <name>); task branch task/sim-10 in Cloud; ledger record ledger/tasks/sim-10.md.
Kind/size: integration/M. Baseline: not-started.
Outcome: Simulator admission and SimulationPacer DO infrastructure work against the real deployed capacity harness, not a local-only simulation

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-21.06 (SimulationPacer real-consumer integration): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\21-cloud-host-and-persistence.md, anchor rule-wp-21.06

Entry condition: adoption slice ADOPT.07.simulator is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] CLOUD.07: real, delivered outcome of CLOUD.07 (Capacity, Container/D1 integration producer and harness)
- [artifact] SIM.01: real, delivered outcome of SIM.01 (Simulation definitions, immutable scenario versions and bounded AST evaluator)
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: 
Unblocks: CLOUD.10

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Local real-integration run of the affected scenario in an existing environment, recorded once; offline and static checks in CI; no hosted runtime, device, browser, live-service or inference CI (P2-017).
Completion evidence for the ledger: Simulator admission and SimulationPacer DO infrastructure work against the real deployed capacity harness, not a local-only simulation
```
