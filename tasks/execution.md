# ArcForges delivery task prompts — Execution engine

Generated from Design `docs/planning/delivery/delivery-graph.json` by `tools/delivery.py`; do not edit by hand.
Each block is self-contained. Claim a task only when `python tools/delivery.py ready` lists it, with
`python tools/delivery.py claim <TASK-ID> --worker <name>`, then follow `arcforges-implementation.md`.
Tasks are ordered by lane for reading; the order is not a schedule.

## Execution engine

```text
Execute ArcForges delivery task EXE.01 — Execution chain and its persistence (ProductJob engine core).

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\execution.md (anchor task-exe-01).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/exe-01 (python tools/delivery.py claim EXE.01 --worker <name>); task branch task/exe-01 in DesktopPlatform; ledger record ledger/tasks/exe-01.md.
Kind/size: producer/L. Baseline: not-started.
Outcome: The full ProductJob/JobStep/JobAttempt chain with distinct types and lifecycles, persisted durably at every state transition; invalid transitions rejected; state survives process termination.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-16.00 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\16-unified-execution-engine.md, anchor rule-wp-16.00
- WP-16:tool-result-acceptance-paragraph-between Tool-result acceptance paragraph (between §5 and §6): two distinct toolRequestIds in one attempt both persist and each replay returns its own original receipt; a changed result under the same (toolRequestId,attemptId,commandId) refuses with command.reused_identifier; lost acknowledgement never allocates a fresh command or drops the second result. Bound to the wire registry, TK-05 and task.tool_result -- the same key WP-26.03 uses. (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\16-unified-execution-engine.md, package-level obligation

Entry condition: adoption slice ADOPT.02.execution is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] APP.01: published product/profile identity (ApplicationScope) from Assistant.Abstractions
- [artifact] FND.02: published execution identity and idempotency records
- [artifact] FND.03: published revision and sequence records
- [artifact] PLT.17: real application identity and in-process composition
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:src/BuildingBlocks/ArcForges.Execution/**; DesktopPlatform:src/BuildingBlocks/ArcForges.Execution.Persistence/**; DesktopPlatform:tests/ExecutionEngineTests/**
Shared resources (follow the owner protocol): RES-assistant-store-schema (append): Numbered migrations are allocated at merge by the integration owner (a rebase renumbers pending migrations); each migration is forward-only with its recovery and downgrade-refusal tests; no task edits a merged migration.; RES-desktopplatform-build-config (append): Solution/project lists, central package versions and CI job lists are appended by the task that adds a project, dependency or job; dependency additions follow the dependency-admission policy with a reviewed receipt; lock files are regenerated after rebase and never hand-merged; the integration owner resolves ordering conflicts at merge.
Unblocks: AST.10, AST.13, DEV.05, EXE.02, EXE.03, EXE.04, EXE.05, EXE.06, EXE.07, EXE.08, EXE.09, SLATE.28, SLATE.30

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline unit tests: state-machine invalid-transition rejection, kill-at-every-transition-point durability; no live environment.
Completion evidence for the ledger: State-machine coverage report, kill-at-transition recovery log.
Notes: Narrow early-risk proof: kill-at-any-transition durability underlies WP16.03-07, WP17.03 Task Centre and the vocabulary WP52 reuses. A defect here invalidates checkpoint/compensation/concurrency work built on top.
```

```text
Execute ArcForges delivery task EXE.02 — Lifecycle states and reason facets.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\execution.md (anchor task-exe-02).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/exe-02 (python tools/delivery.py claim EXE.02 --worker <name>); task branch task/exe-02 in DesktopPlatform; ledger record ledger/tasks/exe-02.md.
Kind/size: producer/S. Baseline: not-started.
Outcome: Every reachable state carries a reason facet (waiting for approval, waiting for a resource, blocked on limit, paused, retrying) that reaches the UI; never a bare state alone.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-16.01 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\16-unified-execution-engine.md, anchor rule-wp-16.01

Entry condition: adoption slice ADOPT.02.execution is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] EXE.01: the real state machine to attach reason facets to
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:src/BuildingBlocks/ArcForges.Execution/**
Unblocks: EXE.09

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline coverage test (every reachable state has a facet) plus a presentation test that the reason reaches the UI layer.
Completion evidence for the ledger: Reason-facet coverage report.
```

```text
Execute ArcForges delivery task EXE.03 — Failure classification and retry.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\execution.md (anchor task-exe-03).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/exe-03 (python tools/delivery.py claim EXE.03 --worker <name>); task branch task/exe-03 in DesktopPlatform; ledger record ledger/tasks/exe-03.md.
Kind/size: producer/M. Baseline: not-started.
Outcome: Failures classify into transient/permanent/refused/cancelled/unknown-effect with effect certainty; an unknown-effect failure on a non-idempotent operation never auto-retries.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-16.02 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\16-unified-execution-engine.md, anchor rule-wp-16.02

Entry condition: adoption slice ADOPT.02.execution is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] EXE.01: the real state machine to classify failures against
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:src/BuildingBlocks/ArcForges.Execution/**
Unblocks: EXE.09

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline classification matrix test; negative test for non-idempotent unknown-effect auto-retry.
Completion evidence for the ledger: Classification matrix, no-auto-retry proof.
Notes: Shares vocabulary only (not implementation) with the Cloud AgentTask failure model in requirements/05 (WP-52); no cross-repo dependency.
```

```text
Execute ArcForges delivery task EXE.04 — Child tasks and ownership.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\execution.md (anchor task-exe-04).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/exe-04 (python tools/delivery.py claim EXE.04 --worker <name>); task branch task/exe-04 in DesktopPlatform; ledger record ledger/tasks/exe-04.md.
Kind/size: producer/M. Baseline: not-started.
Outcome: A task may spawn children with their own lifecycle/budget/cancellation relationship; cancelling a parent cancels children, a failed child does not necessarily fail its parent, ownership is uniform across the tree.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-16.03 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\16-unified-execution-engine.md, anchor rule-wp-16.03

Entry condition: adoption slice ADOPT.02.execution is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] EXE.01: the real state machine and persistence to attach child relationships to
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:src/BuildingBlocks/ArcForges.Execution/**
Shared resources (follow the owner protocol): RES-assistant-store-schema (append): Numbered migrations are allocated at merge by the integration owner (a rebase renumbers pending migrations); each migration is forward-only with its recovery and downgrade-refusal tests; no task edits a merged migration.
Unblocks: EXE.09

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline tests: cancellation propagation, child-failure isolation, ownership assertion across the tree.
Completion evidence for the ledger: Cancellation/isolation/ownership test results.
```

```text
Execute ArcForges delivery task EXE.05 — Checkpoints and compensation.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\execution.md (anchor task-exe-05).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/exe-05 (python tools/delivery.py claim EXE.05 --worker <name>); task branch task/exe-05 in DesktopPlatform; ledger record ledger/tasks/exe-05.md.
Kind/size: producer/M. Baseline: not-started.
Outcome: Checkpoints capture resumable state at declared boundaries; compensation actions run in reverse order on abort; an undeclared irreversible effect fails validation.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-16.04 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\16-unified-execution-engine.md, anchor rule-wp-16.04
- WP-16:tool-result-acceptance-paragraph-between Tool-result acceptance paragraph (between §5 and §6): two distinct toolRequestIds in one attempt both persist and each replay returns its own original receipt; a changed result under the same (toolRequestId,attemptId,commandId) refuses with command.reused_identifier; lost acknowledgement never allocates a fresh command or drops the second result. Bound to the wire registry, TK-05 and task.tool_result -- the same key WP-26.03 uses. (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\16-unified-execution-engine.md, package-level obligation

Entry condition: adoption slice ADOPT.02.execution is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] EXE.01: the real durable state machine to checkpoint
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:src/BuildingBlocks/ArcForges.Execution/**
Shared resources (follow the owner protocol): RES-assistant-store-schema (append): Numbered migrations are allocated at merge by the integration owner (a rebase renumbers pending migrations); each migration is forward-only with its recovery and downgrade-refusal tests; no task edits a merged migration.
Unblocks: AST.13, EXE.09

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline tests: resume-from-checkpoint after kill, compensation-on-abort ordering, undeclared-irreversible validation failure.
Completion evidence for the ledger: Resume and compensation-ordering test results.
Notes: Same (toolRequestId,attemptId,commandId) dedup key referenced by the WP16 'Tool-result acceptance' package-level obligation shared with DEV.04/DEV.05 -- see package_obligations.
```

```text
Execute ArcForges delivery task EXE.06 — Approval, steering and budget integration.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\execution.md (anchor task-exe-06).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/exe-06 (python tools/delivery.py claim EXE.06 --worker <name>); task branch task/exe-06 in DesktopPlatform; ledger record ledger/tasks/exe-06.md.
Kind/size: producer/M. Baseline: not-started.
Outcome: Approval gates pause a task durably until resolved/expired; steering adjusts a running task without granting authority; local resource permits (CPU/memory/disk/queue) are acquired before and released after a bounded job step, with no monetary accounting.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-16.05 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\16-unified-execution-engine.md, anchor rule-wp-16.05

Entry condition: adoption slice ADOPT.02.execution is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] EXE.01: the real durable state machine to pause/resume
- [artifact] PLT.39: published approval/steering/step-up mechanism
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:src/BuildingBlocks/ArcForges.Execution/**; DesktopPlatform:src/BuildingBlocks/ArcForges.Execution.Budget/**
Shared resources (follow the owner protocol): RES-assistant-store-schema (append): Numbered migrations are allocated at merge by the integration owner (a rebase renumbers pending migrations); each migration is forward-only with its recovery and downgrade-refusal tests; no task edits a merged migration.
Unblocks: EXE.09

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline tests: approval-pause across restart, steering-grants-nothing, resource-permit acquisition/release, bounded queue/memory exhaustion.
Completion evidence for the ledger: Approval/steering/budget test results.
Notes: BR-07: local resource permits only, D-020 monetary accounting explicitly absent here (Cloud-owned).
```

```text
Execute ArcForges delivery task EXE.07 — Progress, outcome and trace.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\execution.md (anchor task-exe-07).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/exe-07 (python tools/delivery.py claim EXE.07 --worker <name>); task branch task/exe-07 in DesktopPlatform; ledger record ledger/tasks/exe-07.md.
Kind/size: producer/M. Baseline: not-started.
Outcome: Progress is a separate best-effort channel; outcome is durable fact; execution trace, capability trace and audit stay separate (provider-interaction records stay Cloud-only); a user-visible task identifier resolves to its execution trace. Losing all progress never affects the recorded outcome.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-16.06 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\16-unified-execution-engine.md, anchor rule-wp-16.06

Entry condition: adoption slice ADOPT.02.execution is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] EXE.01: the real durable state machine to record outcome against
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:src/BuildingBlocks/ArcForges.Execution/**
Unblocks: EXE.09

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline tests: progress-loss-never-affects-outcome, task-id-to-trace resolution, trace-system separation.
Completion evidence for the ledger: Conflation-test result, trace-resolution result, trace-separation result; payload/manifest hashes with content-origin carrier per WP16 §7 addition.
Notes: Content-origin behavior/carrier schema (requirements/07, requirements/13) is a frozen design input already decided, not a blocking producer task.
```

```text
Execute ArcForges delivery task EXE.08 — Concurrency, loops and storms.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\execution.md (anchor task-exe-08).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/exe-08 (python tools/delivery.py claim EXE.08 --worker <name>); task branch task/exe-08 in DesktopPlatform; ledger record ledger/tasks/exe-08.md.
Kind/size: producer/M. Baseline: not-started.
Outcome: Per-product and per-device/resource concurrency limits; loop detection preventing plan re-entry into the same step; storm protection preventing automation cascade; each limit produces a typed, explained refusal rather than silent unbounded queuing.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-16.07 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\16-unified-execution-engine.md, anchor rule-wp-16.07

Entry condition: adoption slice ADOPT.02.execution is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] EXE.01: the real state machine and job tree to bound
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:src/BuildingBlocks/ArcForges.Execution/**
Unblocks: EXE.09

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline tests: loop-injection, cascade-injection, saturation with explained refusal.
Completion evidence for the ledger: Loop/cascade/saturation test results.
Notes: Storm/cascade protection here is the native counterpart engine-level guard; the durable Cloud trigger scheduler itself is WP-52.06 (see AST.14 substitute).
```

```text
Execute ArcForges delivery task EXE.09 — Owned-artifact receipt and real integration.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\execution.md (anchor task-exe-09).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/exe-09 (python tools/delivery.py claim EXE.09 --worker <name>); task branch task/exe-09 in DesktopPlatform; ledger record ledger/tasks/exe-09.md.
Kind/size: acceptance/M. Baseline: not-started.
Outcome: ProductJob-only responsibility preserved (no local model loop, no Cloud budget/Task ownership in the shared engine); shared execution vocabulary/package references, dispatch/error profiles and cancellation updated; pending later owners (WP-52) and their closing gates recorded.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-16.90 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\16-unified-execution-engine.md, anchor rule-wp-16.90
- WP-16:6-impacts-row-compatibility-task-contrac §6 Impacts row 'Compatibility: Task contract versioning for later cloud and mobile surfaces' (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\16-unified-execution-engine.md, package-level obligation

Entry condition: adoption slice ADOPT.02.execution is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] EXE.01: completed WP-16.00
- [artifact] EXE.02: completed WP-16.01
- [artifact] EXE.03: completed WP-16.02
- [artifact] EXE.04: completed WP-16.03
- [artifact] EXE.05: completed WP-16.04
- [artifact] EXE.06: completed WP-16.05
- [artifact] EXE.07: completed WP-16.06
- [artifact] EXE.08: completed WP-16.07
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:artifacts/evidence/**
Shared resources (follow the owner protocol): RES-desktopplatform-policy-data (append): Generated policy data is regenerated from its pinned source and never hand-edited; the reason-code registry is append-only with stable codes; each task adds its own test classes and evidence rows.
Unblocks: AST.17

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Architecture-evidence review confirming no local model loop/Cloud budget ownership; P2-017 scope only.
Completion evidence for the ledger: Source commit, producer version, candidate hashes, real-vs-fixture status (none expected for WP16 itself), task-contract versioning note for later Cloud/mobile surfaces.
Notes: Provides ProductJobRef, the surface WP-52's Cloud Task consumes in the OTHER direction (CT-01..07); WP16 does not depend on WP52, WP52 depends on this.
```
