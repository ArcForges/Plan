# ArcForges delivery task prompts — Embedded assistant

Generated from Design `docs/planning/delivery/delivery-graph.json` by `tools/delivery.py`; do not edit by hand.
Each block is self-contained. Claim a task only when `python tools/delivery.py ready` lists it, with
`python tools/delivery.py claim <TASK-ID> --worker <name>`, then follow `arcforges-implementation.md`.
Tasks are ordered by lane for reading; the order is not a schedule.

## Embedded assistant

```text
Execute ArcForges delivery task AST.01 — Single application history store (model 05 schema).

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\assistant.md (anchor task-ast-01).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/ast-01 (python tools/delivery.py claim AST.01 --worker <name>); task branch task/ast-01 in DesktopPlatform; ledger record ledger/tasks/ast-01.md.
Kind/size: producer/L. Baseline: not-started.
Outcome: Assistant.Persistence.Sqlite implements the full data-model-05 schema (assistant_conversation/branch/message/draft/turn/receipt/outbox/history_import/attachment/project/conversation_project/profile/skill/context/task_projection/compaction), migrations and typed payloads, plus Android logical-schema fixtures. Competing model-02 conversation tables retired.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-15.00 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\15-arcchat-conversation-core.md, anchor rule-wp-15.00

Entry condition: adoption slice ADOPT.02.assistant is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] APP.01: published Assistant.Abstractions product/profile identity
- [contract] CON.91: published Foundation contract types (identity/error/revision)
- [contract] CON.11: complete generated package/schema gate output
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:src/BuildingBlocks/ArcForges.Assistant.Core/**; DesktopPlatform:src/BuildingBlocks/ArcForges.Assistant.Persistence.Sqlite/**; DesktopPlatform:tests/AssistantCoreTests/**
Shared resources (follow the owner protocol): RES-assistant-store-schema (append): Numbered migrations are allocated at merge by the integration owner (a rebase renumbers pending migrations); each migration is forward-only with its recovery and downgrade-refusal tests; no task edits a merged migration.; RES-desktopplatform-build-config (append): Solution/project lists, central package versions and CI job lists are appended by the task that adds a project, dependency or job; dependency additions follow the dependency-admission policy with a reviewed receipt; lock files are regenerated after rebase and never hand-merged; the integration owner resolves ordering conflicts at merge.
Unblocks: AST.02, AST.03, AST.04, AST.05, AST.06, AST.07, AST.08, AST.09, AST.10, AST.11, AST.22

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline unit tests: DDL with foreign keys, migrations, disk-full, branch fork, concurrent-window stale revision, duplicate terminal frame, interrupted send; no live environment.
Completion evidence for the ledger: Schema/migration hash, transaction-kill and disk-full test results, one-store-per-application-profile proof.
Notes: Foundation for all other WP15 substeps and for WP16/17's reuse of conversation identities; a schema mistake here invalidates branches, attachments, projects, skills, search and export simultaneously, so it should land and stabilize early.
```

```text
Execute ArcForges delivery task AST.02 — Branches and window drafts.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\assistant.md (anchor task-ast-02).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/ast-02 (python tools/delivery.py claim AST.02 --worker <name>); task branch task/ast-02 in DesktopPlatform; ledger record ledger/tasks/ast-02.md.
Kind/size: producer/M. Baseline: not-started.
Outcome: Immutable ancestry and fork-at-message; per-window draft revisions with a shared committed service within one application. Concurrent windows, draft preserved during another send, parent/child isolation proven.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-15.01 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\15-arcchat-conversation-core.md, anchor rule-wp-15.01

Entry condition: adoption slice ADOPT.02.assistant is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] AST.01: the real history store's branch/message tables
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:src/BuildingBlocks/ArcForges.Assistant.Core/**
Shared resources (follow the owner protocol): RES-assistant-store-schema (append): Numbered migrations are allocated at merge by the integration owner (a rebase renumbers pending migrations); each migration is forward-only with its recovery and downgrade-refusal tests; no task edits a merged migration.
Unblocks: AST.09, AST.10

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline unit tests: concurrent windows, draft preserved during another send, parent/child isolation.
Completion evidence for the ledger: Concurrent-window and fork-isolation test results.
```

```text
Execute ArcForges delivery task AST.03 — Attachments and provenance.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\assistant.md (anchor task-ast-03).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/ast-03 (python tools/delivery.py claim AST.03 --worker <name>); task branch task/ast-03 in DesktopPlatform; ledger record ledger/tasks/ast-03.md.
Kind/size: producer/M. Baseline: not-started.
Outcome: Typed local refs, authorized file staging/preview, resource ownership and explicit egress; attachment selection is never treated as upload consent. Missing/hostile file, lost URI/path grant, source labels, quota and temporary exclusion covered.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-15.02 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\15-arcchat-conversation-core.md, anchor rule-wp-15.02

Entry condition: adoption slice ADOPT.02.assistant is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] AST.01: the real history store's attachment table
- [artifact] APP.06: the real WP-14.05 context/artifact freeze and preview port
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:src/BuildingBlocks/ArcForges.Assistant.Core/**
Shared resources (follow the owner protocol): RES-assistant-store-schema (append): Numbered migrations are allocated at merge by the integration owner (a rebase renumbers pending migrations); each migration is forward-only with its recovery and downgrade-refusal tests; no task edits a merged migration.
Unblocks: AST.09

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline unit tests: missing/hostile file, lost URI/path grant, quota, temporary exclusion.
Completion evidence for the ledger: Attachment provenance and egress-consent test results.
```

```text
Execute ArcForges delivery task AST.04 — Projects and profiles.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\assistant.md (anchor task-ast-04).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/ast-04 (python tools/delivery.py claim AST.04 --worker <name>); task branch task/ast-04 in DesktopPlatform; ledger record ledger/tasks/ast-04.md.
Kind/size: producer/S. Baseline: not-started.
Outcome: Accepted project/instruction/profile CRUD, validation, immutable per-execution snapshots and application partitioning; conflict/revision handling and profile change cannot alter an active execution.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-15.03 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\15-arcchat-conversation-core.md, anchor rule-wp-15.03

Entry condition: adoption slice ADOPT.02.assistant is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] AST.01: the real history store's project/profile tables
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:src/BuildingBlocks/ArcForges.Assistant.Core/**
Shared resources (follow the owner protocol): RES-assistant-store-schema (append): Numbered migrations are allocated at merge by the integration owner (a rebase renumbers pending migrations); each migration is forward-only with its recovery and downgrade-refusal tests; no task edits a merged migration.
Unblocks: AST.09, AST.10

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline unit tests: conflict/revision, active-execution immutability.
Completion evidence for the ledger: Immutable-snapshot-during-active-execution test results.
```

```text
Execute ArcForges delivery task AST.05 — Skills.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\assistant.md (anchor task-ast-05).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/ast-05 (python tools/delivery.py claim AST.05 --worker <name>); task branch task/ast-05 in DesktopPlatform; ledger record ledger/tasks/ast-05.md.
Kind/size: producer/S. Baseline: not-started.
Outcome: Accepted skill/version/permission metadata and selection, without installing an external agent or granting authority from content; untrusted instructions remain content, cross-app source denied.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-15.04 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\15-arcchat-conversation-core.md, anchor rule-wp-15.04

Entry condition: adoption slice ADOPT.02.assistant is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] AST.01: the real history store's skill table
- [artifact] PLT.42: published instruction provenance mechanism
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:src/BuildingBlocks/ArcForges.Assistant.Core/**
Shared resources (follow the owner protocol): RES-assistant-store-schema (append): Numbered migrations are allocated at merge by the integration owner (a rebase renumbers pending migrations); each migration is forward-only with its recovery and downgrade-refusal tests; no task edits a merged migration.
Unblocks: AST.09, AST.10

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline unit tests: untrusted-instruction and cross-app-source-denied cases.
Completion evidence for the ledger: Skill selection/provenance test results.
```

```text
Execute ArcForges delivery task AST.06 — Local search.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\assistant.md (anchor task-ast-06).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/ast-06 (python tools/delivery.py claim AST.06 --worker <name>); task branch task/ast-06 in DesktopPlatform; ledger record ledger/tasks/ast-06.md.
Kind/size: producer/M. Baseline: not-started.
Outcome: Indexes only committed non-deleted normal history in the owning partition, with exact citations/branches and a rebuildable index; delete/rebuild, partial index and no temporary/other-app leak proven.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-15.05 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\15-arcchat-conversation-core.md, anchor rule-wp-15.05

Entry condition: adoption slice ADOPT.02.assistant is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] AST.01: the real committed-message store to index
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:src/BuildingBlocks/ArcForges.Assistant.Core/**
Unblocks: AST.09, AST.10

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline unit tests: delete/rebuild, partial index, isolation leak checks.
Completion evidence for the ledger: Rebuild and isolation-leak test results.
```

```text
Execute ArcForges delivery task AST.07 — Local history export and import (assistant-history.v1).

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\assistant.md (anchor task-ast-07).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/ast-07 (python tools/delivery.py claim AST.07 --worker <name>); task branch task/ast-07 in DesktopPlatform; ledger record ledger/tasks/ast-07.md.
Kind/size: producer/M. Baseline: not-started.
Outcome: Produces/consumes assistant-history.v1 from committed local snapshots, preserving branch/message/resource provenance and missing-resource reports; import remaps identities. Complete offline without Cloud, implicit upload or mode conversion. Cloud promotion itself remains WP-25.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-15.06 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\15-arcchat-conversation-core.md, anchor rule-wp-15.06

Entry condition: adoption slice ADOPT.02.assistant is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] AST.01: the real committed history store to export from
- [contract] CON.11: published assistant-history.v1 format definition
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:src/BuildingBlocks/ArcForges.Assistant.Core/**
Shared resources (follow the owner protocol): RES-assistant-store-schema (append): Numbered migrations are allocated at merge by the integration owner (a rebase renumbers pending migrations); each migration is forward-only with its recovery and downgrade-refusal tests; no task edits a merged migration.
Permitted substitutes (never real integration evidence): SUB-assistant-history-fixture: local offline export/import round-trip, malformed/hash/foreign-reference handling, branch-cycle and cancel-import handling only -- no Cloud upload Real producer ['CLOUD.45']; removed by AST.21
Unblocks: AST.09, AST.10, AST.15, AST.21

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline full round-trip tests: malformed/hash/foreign references, draft exclusion, branch cycles, canceled import; no Cloud in CI.
Completion evidence for the ledger: Round-trip hash manifests, malformed/cycle/cancel test results, named-fixture manifest entry for this substitute.
Notes: One of the four named scaffolding rows in implementation-sequence.md §3.1 (shared with ArcNotes' own WP-19.05, not mine). See integration_proposals IM.history-export-cloud-promotion.
```

```text
Execute ArcForges delivery task AST.08 — Reference and package proof (AionUi evidence, clean-app package consumption).

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\assistant.md (anchor task-ast-08).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/ast-08 (python tools/delivery.py claim AST.08 --worker <name>); task branch task/ast-08 in DesktopPlatform; ledger record ledger/tasks/ast-08.md.
Kind/size: producer/S. Baseline: not-started.
Outcome: AionUi component evidence/provenance recorded; the actual candidate Assistant.Core/Assistant.Persistence.Sqlite package consumed from a clean test application with no reference runtime or imported agent scope.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-15.07 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\15-arcchat-conversation-core.md, anchor rule-wp-15.07

Entry condition: adoption slice ADOPT.02.assistant is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] AST.01: published Assistant.Core/Assistant.Persistence.Sqlite candidate packages
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:tests/AssistantCoreTests/**
Unblocks: AST.09

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Package-only restore in a clean test app; offline behavior tests; exact package hash recorded.
Completion evidence for the ledger: Package hash manifest, AionUi reference-coverage citation (arcchat-aionui.md, no reused code), clean-app test results.
```

```text
Execute ArcForges delivery task AST.09 — Owned-artifact receipt and UX acceptance.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\assistant.md (anchor task-ast-09).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/ast-09 (python tools/delivery.py claim AST.09 --worker <name>); task branch task/ast-09 in DesktopPlatform; ledger record ledger/tasks/ast-09.md.
Kind/size: acceptance/M. Baseline: not-started.
Outcome: WP15 built/packed once from a clean environment; all applicable UX acceptance groups recorded; package/contract/owner/version compatibility and failure/recovery evidence attached; no later-provider fixture closes a real WP15 gate.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-15.90 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\15-arcchat-conversation-core.md, anchor rule-wp-15.90

Entry condition: adoption slice ADOPT.02.assistant is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] AST.01: completed WP-15.00
- [artifact] AST.02: completed WP-15.01
- [artifact] AST.03: completed WP-15.02
- [artifact] AST.04: completed WP-15.03
- [artifact] AST.05: completed WP-15.04
- [artifact] AST.06: completed WP-15.05
- [artifact] AST.07: completed WP-15.06
- [artifact] AST.08: completed WP-15.07
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:artifacts/evidence/**
Shared resources (follow the owner protocol): RES-desktopplatform-policy-data (append): Generated policy data is regenerated from its pinned source and never hand-edited; the reason-code registry is append-only with stable codes; each task adds its own test classes and evidence rows.

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Build/pack once; UX-C history ledger rows recorded; P2-017 scope only.
Completion evidence for the ledger: Source commit, package versions/hashes, UX-C rows, named-fixture manifest (assistant-history.v1 export fixture).
```

```text
Execute ArcForges delivery task AST.10 — Complete assistant navigation shell.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\assistant.md (anchor task-ast-10).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/ast-10 (python tools/delivery.py claim AST.10 --worker <name>); task branch task/ast-10 in DesktopPlatform; ledger record ledger/tasks/ast-10.md.
Kind/size: producer/L. Baseline: not-started.
Outcome: All AS01 to AS13 docked/floating/expanded surfaces are reachable through the architecture-27 AssistantHost API; the same composition code works independently in each product. All actions reachable at minimum size; window/draft/account/keyboard/accessibility matrix passes.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-17.00 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\17-arcchat-independent-core.md, anchor rule-wp-17.00

Entry condition: adoption slice ADOPT.02.assistant is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] EXE.01: the real execution chain to surface job state in navigation
- [artifact] AST.01: the real application history store the shell hosts
- [artifact] AST.02: real branches and window drafts to navigate
- [artifact] AST.04: real projects and profiles to navigate
- [artifact] AST.05: real skills to navigate
- [artifact] AST.06: real local search to surface
- [artifact] AST.07: real local history export and import to surface
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:src/BuildingBlocks/ArcForges.Assistant.Avalonia/**; DesktopPlatform:samples/AssistantHost/**
Shared resources (follow the owner protocol): RES-desktopplatform-build-config (append): Solution/project lists, central package versions and CI job lists are appended by the task that adds a project, dependency or job; dependency additions follow the dependency-admission policy with a reviewed receipt; lock files are regenerated after rebase and never hand-merged; the integration owner resolves ordering conflicts at merge.
Unblocks: AST.12, AST.13, AST.14, AST.15, AST.16, AST.17

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline UI tests: minimum-size reachability, window/draft/account/keyboard/accessibility matrix; no live Cloud in CI.
Completion evidence for the ledger: Reachability matrix results, accessibility pass, source commit.
Notes: This is the navigation shell/chrome only; deeper per-surface behavior (security, task centre, automation, history, preview) is separately owned by AST.12-16 and composed into this shell.
```

```text
Execute ArcForges delivery task AST.11 — Cloud client and device runtime (fixture turn endpoint boundary).

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\assistant.md (anchor task-ast-11).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/ast-11 (python tools/delivery.py claim AST.11 --worker <name>); task branch task/ast-11 in DesktopPlatform; ledger record ledger/tasks/ast-11.md.
Kind/size: producer/L. Baseline: not-started.
Outcome: Reusable Cloud.Client (session/event/output/upload) and Device.Runtime (own-app registration/presence, pull/claim/result, typed dispatch adapter) implemented against generated gRPC-Web contracts; own-app typed dispatch adapters work end-to-end in-process. Named future-owner fixtures stand in for WP-23 through WP-26 and WP-52 until those exist.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-17.01 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\17-arcchat-independent-core.md, anchor rule-wp-17.01

Entry condition: adoption slice ADOPT.02.assistant is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [contract] CON.10: published generated C#/TypeScript/Kotlin gRPC-Web client stubs and numbered wire registry
- [artifact] PRF.05: proven generated gRPC-Web under Native AOT pattern
- [artifact] AST.01: the history store assistant_turn and assistant_outbox records the Cloud client writes into
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:src/BuildingBlocks/ArcForges.Communication.CloudClient/**; DesktopPlatform:src/BuildingBlocks/ArcForges.Communication.DeviceRuntime/**
Shared resources (follow the owner protocol): RES-desktopplatform-build-config (append): Solution/project lists, central package versions and CI job lists are appended by the task that adds a project, dependency or job; dependency additions follow the dependency-admission policy with a reviewed receipt; lock files are regenerated after rebase and never hand-merged; the integration owner resolves ordering conflicts at merge.
Permitted substitutes (never real integration evidence): SUB-device-runtime-loopback: in-process typed dispatch/decode/local-reauthorization mechanics only, no real cross-device delivery Real producer ['DEV.01', 'DEV.02']; removed by DEV.14; SUB-fixture-turn-endpoint: client-side session/event/output/upload handling, typed state transitions, reconnection -- runs no model/planner/admission/metering itself Real producer ['HAR.00', 'HAR.02', 'HAR.03']; removed by HAR.05
Unblocks: AST.13, AST.17, AST.19, DEV.03, DEV.14, HAR.05

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline tests against generated gRPC-Web calls/typed states with an explicit named-fixture manifest; no live Cloud in CI per P2-017.
Completion evidence for the ledger: Fixture manifest naming each replacement producer (WP-23..26, WP-52), typed-state test results.
Notes: This is the DesktopPlatform half of the WP26 dual-repo split: Device.Runtime's project skeleton is built here and extended (not duplicated) by DEV.03/DEV.05.
```

```text
Execute ArcForges delivery task AST.12 — Security and approval surface.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\assistant.md (anchor task-ast-12).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/ast-12 (python tools/delivery.py claim AST.12 --worker <name>); task branch task/ast-12 in DesktopPlatform; ledger record ledger/tasks/ast-12.md.
Kind/size: producer/M. Baseline: not-started.
Outcome: AS06/11/12 implemented with actor/target/context/egress/cost/expiry and local-presence escalation; no persistent allow-all or cross-product grant, stale approval refused.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-17.02 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\17-arcchat-independent-core.md, anchor rule-wp-17.02

Entry condition: adoption slice ADOPT.02.assistant is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] AST.10: the navigation shell to compose this surface into
- [artifact] APP.05: the exact WP-14.04 owner approval enforcement point
- [artifact] PLT.39: published approval/steering/step-up mechanism
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:src/BuildingBlocks/ArcForges.Assistant.Avalonia/**
Unblocks: AST.17, SCOPE.20

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline tests: no persistent allow-all/cross-product grant, stale approval refused.
Completion evidence for the ledger: Allow-all/cross-product/stale-approval negative test results.
```

```text
Execute ArcForges delivery task AST.13 — Task centre.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\assistant.md (anchor task-ast-13).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/ast-13 (python tools/delivery.py claim AST.13 --worker <name>); task branch task/ast-13 in DesktopPlatform; ledger record ledger/tasks/ast-13.md.
Kind/size: producer/M. Baseline: not-started.
Outcome: Task timeline, tools, artifacts, cancellation/steering and ProductJob links with effect certainty; canceled/interrupted/unknown/complete distinguishable, closing the view does not cancel.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-17.03 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\17-arcchat-independent-core.md, anchor rule-wp-17.03

Entry condition: adoption slice ADOPT.02.assistant is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] AST.10: the navigation shell to compose this surface into
- [artifact] EXE.01: the real execution chain (ProductJobRecord/JobAttempt) to link to
- [artifact] EXE.05: real checkpoint/compensation state for display
- [artifact] AST.11: the Cloud client's TaskRef/output stream for the Cloud Agent Task side of the timeline
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:src/BuildingBlocks/ArcForges.Assistant.Avalonia/**
Unblocks: AST.17

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline tests: canceled/interrupted/unknown/complete distinguishability, close-does-not-cancel.
Completion evidence for the ledger: State-distinguishability and close-behavior test results.
```

```text
Execute ArcForges delivery task AST.14 — Automation client (automation fixture state transitions).

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\assistant.md (anchor task-ast-14).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/ast-14 (python tools/delivery.py claim AST.14 --worker <name>); task branch task/ast-14 in DesktopPlatform; ledger record ledger/tasks/ast-14.md.
Kind/size: producer/M. Baseline: not-started.
Outcome: Existing Cloud-owned rule/occurrence UI implemented: schedule/timezone/target/budget and action availability; offline edits remain drafts and never imply local scheduling.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-17.04 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\17-arcchat-independent-core.md, anchor rule-wp-17.04

Entry condition: adoption slice ADOPT.02.assistant is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] AST.10: the navigation shell to compose this surface into
- [contract] CON.10: published Cloud-owned rule/occurrence record shapes
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:src/BuildingBlocks/ArcForges.Assistant.Avalonia/**
Permitted substitutes (never real integration evidence): SUB-automation-fixture: client rendering of schedule/timezone/target/budget and action availability, offline-draft handling only Real producer ['HAR.06']; removed by HAR.06
Unblocks: AST.17, AST.20

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline tests: offline edits remain drafts; no live scheduler in CI.
Completion evidence for the ledger: Named-fixture manifest entry, offline-draft test results.
Notes: Second of the four named scaffolding rows in implementation-sequence.md §3.1.
```

```text
Execute ArcForges delivery task AST.15 — History and AI admission (local/cloud/temporary modes).

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\assistant.md (anchor task-ast-15).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/ast-15 (python tools/delivery.py claim AST.15 --worker <name>); task branch task/ast-15 in DesktopPlatform; ledger record ledger/tasks/ast-15.md.
Kind/size: producer/M. Baseline: not-started.
Outcome: Local/cloud/temporary disclosure, mode selection, Cloud promotion/copy UI and real local lifecycle implemented, with named Cloud fixtures for the promotion target; no implicit upload; denied-admission/credit-consent and transient-output-recovery states covered.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-17.05 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\17-arcchat-independent-core.md, anchor rule-wp-17.05

Entry condition: adoption slice ADOPT.02.assistant is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] AST.10: the navigation shell to compose this surface into
- [artifact] AST.07: the real assistant-history.v1 local export/import surface
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:src/BuildingBlocks/ArcForges.Assistant.Cloud/**
Permitted substitutes (never real integration evidence): SUB-history-admission-fixture: local mode selection/disclosure/promotion UI and denied-admission/credit-consent gating only, no real upload Real producer ['CLOUD.46']; removed by AST.22; SUB-stubbed-provider-path: early client/UI development against a scripted AI response only Real producer ['AIR.00']; removed by AIR.08
Unblocks: AIR.08, AST.17, AST.22, HAR.03, SCOPE.21

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline tests: no implicit upload, denied admission/credit consent, transient output recovery states; no live Cloud in CI.
Completion evidence for the ledger: Named-fixture manifest entry, admission/consent/recovery test results.
Notes: See integration_proposals IM.cloud-history-admission for the real WP-25.09 receiver proof.
```

```text
Execute ArcForges delivery task AST.16 — Preview and host context.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\assistant.md (anchor task-ast-16).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/ast-16 (python tools/delivery.py claim AST.16 --worker <name>); task branch task/ast-16 in DesktopPlatform; ledger record ledger/tasks/ast-16.md.
Kind/size: producer/M. Baseline: not-started.
Outcome: AS03/08 own-app selection/preview/navigation implemented using the frozen WP-14.05 host ports, with safe fallback for unsupported native preview; no live-selection mutation, no another-product destination, citations/resources keep ownership.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-17.06 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\17-arcchat-independent-core.md, anchor rule-wp-17.06

Entry condition: adoption slice ADOPT.02.assistant is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] AST.10: the navigation shell to compose this surface into
- [artifact] APP.06: the exact frozen WP-14.05 context/artifact preview port
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:src/BuildingBlocks/ArcForges.Assistant.Avalonia/**
Unblocks: AST.17

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline tests: no live-selection mutation, no cross-product destination, citation/resource ownership preserved.
Completion evidence for the ledger: Selection-mutation and ownership test results.
```

```text
Execute ArcForges delivery task AST.17 — Complete package acceptance (Assistant.Avalonia/Core/Sqlite/Cloud).

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\assistant.md (anchor task-ast-17).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/ast-17 (python tools/delivery.py claim AST.17 --worker <name>); task branch task/ast-17 in DesktopPlatform; ledger record ledger/tasks/ast-17.md.
Kind/size: acceptance/L. Baseline: not-started.
Outcome: Assistant.Avalonia/Core/Sqlite/Cloud candidates published; a clean Native AOT host consumes only required packages; every accepted assistant capability is mapped; UX-A/B/C/H pass locally; real Cloud/AI fixtures remain explicit and close only at WP-26/WP-52.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-17.07 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\17-arcchat-independent-core.md, anchor rule-wp-17.07

Entry condition: adoption slice ADOPT.02.assistant is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] AST.10: completed WP-17.00
- [artifact] AST.11: completed WP-17.01
- [artifact] AST.12: completed WP-17.02
- [artifact] AST.13: completed WP-17.03
- [artifact] AST.14: completed WP-17.04
- [artifact] AST.15: completed WP-17.05
- [artifact] AST.16: completed WP-17.06
Completion prerequisites (may start earlier; cannot complete before these are complete):
- [integration] APP.08: WP-14 acceptance complete
- [integration] EXE.09: WP-16 acceptance complete

Permitted write scope: DesktopPlatform:samples/AssistantHost/**; DesktopPlatform:artifacts/evidence/**
Shared resources (follow the owner protocol): RES-desktopplatform-build-config (append): Solution/project lists, central package versions and CI job lists are appended by the task that adds a project, dependency or job; dependency additions follow the dependency-admission policy with a reviewed receipt; lock files are regenerated after rebase and never hand-merged; the integration owner resolves ordering conflicts at merge.; RES-desktopplatform-policy-data (append): Generated policy data is regenerated from its pinned source and never hand-edited; the reason-code registry is append-only with stable codes; each task adds its own test classes and evidence rows.
Unblocks: AST.18

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Clean-environment AOT publish/run of the sample host; UX-A/B/C/H ledger rows recorded locally; real Cloud/AI fixtures explicitly named, not closed here; P2-017 scope only.
Completion evidence for the ledger: Package set versions/hashes, clean-host run log, UX-A/B/C/H rows, consolidated named-fixture manifest.
```

```text
Execute ArcForges delivery task AST.18 — Owned-artifact receipt and real integration.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\assistant.md (anchor task-ast-18).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/ast-18 (python tools/delivery.py claim AST.18 --worker <name>); task branch task/ast-18 in DesktopPlatform; ledger record ledger/tasks/ast-18.md.
Kind/size: acceptance/M. Baseline: not-started.
Outcome: WP17 built/packed once from a clean environment; all applicable UX acceptance groups recorded; later external evidence (WP-26/WP-41/WP-52) remains explicitly named, not fabricated.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-17.90 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\17-arcchat-independent-core.md, anchor rule-wp-17.90

Entry condition: adoption slice ADOPT.02.assistant is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] AST.17: completed WP-17.07 package acceptance
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:artifacts/evidence/**
Shared resources (follow the owner protocol): RES-desktopplatform-policy-data (append): Generated policy data is regenerated from its pinned source and never hand-edited; the reason-code registry is append-only with stable codes; each task adds its own test classes and evidence rows.

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): P2-017 scope only; no macOS/E2E/live-service CI.
Completion evidence for the ledger: Source commit, artifact versions/hashes, environment, UX ledger rows, named-fixture list for WP-26/41/52.
Notes: Two orphaned substep anchors (rule-wp-17.08, rule-wp-17.09) exist in the WP17 doc with no substep content and no entry in substeps.json --; not modeled as tasks.
```

```text
Execute ArcForges delivery task AST.19 — Real Cloud Harness turn loop replacing the fixture turn endpoint.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\assistant.md (anchor task-ast-19).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/ast-19 (python tools/delivery.py claim AST.19 --worker <name>); task branch task/ast-19 in DesktopPlatform; ledger record ledger/tasks/ast-19.md.
Kind/size: integration/M. Baseline: not-started.
Outcome: HV-09 structural test 'no client runs a model loop' plus a live streamed turn against the deployed Harness, deleting the fixture turn endpoint structurally

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-52.05 (all work except the parts mapped to DEV.13, HAR.05): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\52-cloud-harness.md, anchor rule-wp-52.05

Entry condition: adoption slice ADOPT.02.assistant is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] AST.11: real, delivered outcome of AST.11 (Cloud client and device runtime (fixture turn endpoint boundary))
- [artifact] HAR.00: real Harness turn loop
- [artifact] HAR.03: real generated streaming and durable output
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: 
Unblocks: DEV.13, HAR.05

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Local real-integration run of the affected scenario in an existing environment, recorded once; offline and static checks in CI; no hosted runtime, device, browser, live-service or inference CI (P2-017).
Completion evidence for the ledger: HV-09 structural test 'no client runs a model loop' plus a live streamed turn against the deployed Harness, deleting the fixture turn endpoint structurally
```

```text
Execute ArcForges delivery task AST.20 — Real durable Cloud automation scheduler replacing the automation fixture.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\assistant.md (anchor task-ast-20).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/ast-20 (python tools/delivery.py claim AST.20 --worker <name>); task branch task/ast-20 in DesktopPlatform; ledger record ledger/tasks/ast-20.md.
Kind/size: integration/M. Baseline: not-started.
Outcome: a live scheduled occurrence executes and cascades with storm protection, observed end-to-end from the AST.14 client

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-52.06 (all work except the parts mapped to HAR.06, HAR.91): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\52-cloud-harness.md, anchor rule-wp-52.06

Entry condition: adoption slice ADOPT.02.assistant is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] AST.14: real, delivered outcome of AST.14 (Automation client (automation fixture state transitions))
- [artifact] HAR.06: real, delivered outcome of HAR.06 (Durable Cloud automation, scheduling and automation-fixture removal)
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: 
Unblocks: HAR.06

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Local real-integration run of the affected scenario in an existing environment, recorded once; offline and static checks in CI; no hosted runtime, device, browser, live-service or inference CI (P2-017).
Completion evidence for the ledger: a live scheduled occurrence executes and cascades with storm protection, observed end-to-end from the AST.14 client
```

```text
Execute ArcForges delivery task AST.21 — Real Cloud Notes/Chat export producer replacing the local assistant-history.v1 fixture.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\assistant.md (anchor task-ast-21).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform). Also touches: Cloud.
Claim and handoff record: claims/ast-21 (python tools/delivery.py claim AST.21 --worker <name>); task branch task/ast-21 in DesktopPlatform; ledger record ledger/tasks/ast-21.md.
Kind/size: integration/M. Baseline: not-started.
Outcome: a real deployed Cloud export/snapshot job round-trips the same assistant-history.v1 archive that AST.07's offline fixture produces, for both ArcChat and ArcNotes history

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-25.08 (all work except the parts mapped to CLOUD.45, CLOUD.58, NOTES.33): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\25-sync-engine-and-blob-lifecycle.md, anchor rule-wp-25.08

Entry condition: adoption slice ADOPT.02.assistant is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] AST.07: real, delivered outcome of AST.07 (Local history export and import (assistant-history.v1))
- [artifact] CLOUD.45: real, delivered outcome of CLOUD.45 (Real Cloud Notes and Chat export producers)
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: 
Unblocks: CLOUD.47, CLOUD.58

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Local real-integration run of the affected scenario in an existing environment, recorded once; offline and static checks in CI; no hosted runtime, device, browser, live-service or inference CI (P2-017).
Completion evidence for the ledger: a real deployed Cloud export/snapshot job round-trips the same assistant-history.v1 archive that AST.07's offline fixture produces, for both ArcChat and ArcNotes history
```

```text
Execute ArcForges delivery task AST.22 — Real Cloud application-history restartable import receiving promoted local history.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\assistant.md (anchor task-ast-22).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform). Also touches: Cloud.
Claim and handoff record: claims/ast-22 (python tools/delivery.py claim AST.22 --worker <name>); task branch task/ast-22 in DesktopPlatform; ledger record ledger/tasks/ast-22.md.
Kind/size: integration/M. Baseline: not-started.
Outcome: AST.15's Cloud promotion/copy UI successfully drives a real restartable import, including lost-finalize-ack, changed-local-history and account-switch recovery

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-25.09 (full; consumer-side real integration): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\25-sync-engine-and-blob-lifecycle.md, anchor rule-wp-25.09

Entry condition: adoption slice ADOPT.02.assistant is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] AST.15: real, delivered outcome of AST.15 (History and AI admission (local/cloud/temporary modes))
- [artifact] CLOUD.46: real, delivered outcome of CLOUD.46 (Application Cloud history and restartable import)
- [artifact] AST.01: real, delivered outcome of AST.01 (Single application history store (model 05 schema))
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: 
Unblocks: CLOUD.47

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Local real-integration run of the affected scenario in an existing environment, recorded once; offline and static checks in CI; no hosted runtime, device, browser, live-service or inference CI (P2-017).
Completion evidence for the ledger: AST.15's Cloud promotion/copy UI successfully drives a real restartable import, including lost-finalize-ack, changed-local-history and account-switch recovery
Notes: Merged duplicate integration or closure task formerly proposed as CLOUD.57.
```
