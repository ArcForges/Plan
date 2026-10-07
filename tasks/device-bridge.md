# ArcForges delivery task prompts — Application presence and tool bridge

Generated from Design `docs/planning/delivery/delivery-graph.json` by `tools/delivery.py`; do not edit by hand.
Each block is self-contained. Claim a task only when `python tools/delivery.py ready` lists it, with
`python tools/delivery.py claim <TASK-ID> --worker <name>`, then follow `arcforges-implementation.md`.
Tasks are ordered by lane for reading; the order is not a schedule.

## Application presence and tool bridge

```text
Execute ArcForges delivery task DEV.01 — Application presence (ApplicationService List/Heartbeat/Disconnect).

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\device-bridge.md (anchor task-dev-01).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/dev-01 (python tools/delivery.py claim DEV.01 --worker <name>); task branch task/dev-01 in Cloud; ledger record ledger/tasks/dev-01.md.
Kind/size: service/M. Baseline: not-started.
Outcome: ApplicationService.List/Heartbeat/Disconnect implemented with DO projection of D1 installation authority; separate app rows per device; 30s expiry/10s renewal, restarted epoch, app-offline-without-device-wide-false-availability proven.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-26.00 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\26-remote-action-and-tool-bridge.md, anchor rule-wp-26.00

Entry condition: adoption slice ADOPT.07.device-bridge is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [contract] CON.11: published ApplicationService.List/Heartbeat/Disconnect wire definitions
- [artifact] CLOUD.72: actual owner-bound module read/plan port and existing Devices/Workspace factories
- [artifact] CLOUD.75: actual configured realm/recovery authority
Completion prerequisites (may start earlier; cannot complete before these are complete):
- [integration] CLOUD.13: actual D1 device/installation/session durable authority and typed instance-target authorization
- [integration] CLOUD.29: real Durable-Object-backed connection/authentication substrate
- [integration] CLOUD.11: actual single-owner workspace/Identity source
- [integration] CLOUD.21: actual signed host/Worker production storage executor
- [integration] CON.31: actual published344.1 owned generated storage/public validation and mandatory peer closure

Permitted write scope: Cloud:src/ArcForges.Cloud.Modules.Devices/Presence/** and DevicesModule.cs (real bounded presence core, current owner adapters and actual registration only); Cloud:src/ArcForges.Cloud.Modules.Abstractions/Devices/ApplicationPresencePort.cs (closed neutral owner/read/control ports and typed failures; no duplicated published Application DTO); Cloud:src/ArcForges.Cloud.Modules.Workspace/Presence/** and WorkspaceModule.cs and src/ArcForges.Cloud.Modules.Abstractions/Workspace/ApplicationPresenceWorkspacePort.cs (ONLY real single-owner current active personal workspace read authority; reuse existing workspace-load/by-owner plans, no membership table/foreign SQL); Cloud:src/ArcForges.Cloud/Composition/ApplicationPresenceModule.cs and HostModules.cs (append only lazy actual presence registration; absent producer typed unavailable and existing health unchanged); Cloud:src/ArcForges.Cloud/Infrastructure/WorkerPresenceClient.cs and PublicApi/Application/** (actual bounded generated Application List/Heartbeat/Disconnect ingress/current credential resolution and signed private presence bridge only); Cloud:worker/presence/model.ts and durable.ts and handler.ts and environment.ts (actual SQLite ApplicationPresenceCoordinator monotone owner epoch/lease/idempotency and closed HMAC bridge; no D1 device.presence table); Cloud:worker/index.ts (exact class export and closed virtual presence.internal private routing/environment registration only); Cloud:wrangler.json (append only APPLICATION_PRESENCE SQLite DO binding/migration presence-v1 and exact actual environment entries; preserve existing migrations, routes/workers_dev=false/data); Cloud:storage/plans/device/presence-*.sql and storage/plans/workspace/workspace-load.sql and workspace-by-owner.sql (only actual owner read facts if needed, retain current schemas/identity; no foreign Identity/Workspace SQL); Cloud:src/ArcForges.Cloud.Storage.D1/PlanManifest.g.cs and worker/storage/plans.generated.ts (sole coordinated actual owned read union regeneration only); Cloud:tests/ArcForges.Cloud.Tests/Presence/** and tests/worker/application-presence*.test.ts (actual current owner, durable SQLite DO epoch/lease/receipt/recovery/overflow/cancel and generated ingress tests); Cloud:package.json (append only owned application-presence offline test command entries, no tools/dependencies/locks changes); Cloud:tests/ArchitectureTests/** (only actual owned API/layer/producer bindings, preserve all shape/no-authored-wire guards); Cloud:eng/policy/dependency-policy.json and eng/policy/dependency-reviews/dev-01-*.json and eng/provenance/** (only actual evaluated input/firstParty/immutable Worker/legal/source successor, no guessed producer pins); Cloud:tests/worker/release-provenance.test.ts (only actual owned sealed Worker SHA/bytes successor, preserve all historical/legal/refusal tests); Cloud:.dockerignore (exact actual owned source inclusion only); Cloud:docs/application-presence.md (full owner/epoch/lease/replay and actual component/publication evidence); Cloud:src/ArcForges.Cloud.Modules.Devices/DevicesModule.cs (exact existing presence factory registration only; preserve all actual Devices readers/participants/signatures/queries); Cloud:Directory.Packages.props and src/ArcForges.Cloud/ArcForges.Cloud.csproj and src/ArcForges.Cloud/packages.lock.json and tests/ArcForges.Cloud.Tests/packages.lock.json and tests/ArcForges.Cloud.Consumer/packages.lock.json and tests/ArchitectureTests/packages.lock.json and eng/policy/licence-boundary.json (ONLY actual published ArcForges.Contracts.Validation 1.0.0-ci.287.1 generated Application shape-validation host closure and actually affected generated lock/legal/input bindings; no cohort/tool upgrade, source refs or warning suppression); Cloud:src/ArcForges.Cloud/Ingress/RpcPolicy.cs and IngressPipeline.cs (ONLY immutable trusted Session-policy CredentialProviderKey and exact keyed current-credential selection; missing declared keyed provider typedUnavailable/no global fallback, null preserves Foundation behavior and all denial/framing/current-owner/correlation gates); Cloud:worker/ingress/routes.ts (only three actual ApplicationService.List/Heartbeat/Disconnect rows, unarySessionMeta65536frame/<=15000ms, explicit presence namespace; coordinate sole shared union writer); Cloud:tests/worker/ingress-routes.test.ts (only genuine three Application routes/key/meta/namespace/cap parity and old default/unknown/proof preservation)
Shared resources (follow the owner protocol): RES-cloud-d1-migrations (append): One global D1 migration sequence: each module task authors migrations under its module prefix; the integration owner assigns the global sequence number at merge, regenerates the plan manifest and rejects edits to merged migrations; the migrator applies in sequence with receipts.; RES-cloud-policy-inputs (append): Append only task-owned source/test bindings and immutable successor receipts. Rebase before integration; regenerate actual input hashes and plan manifests; chain from the receipt active on main; preserve all prior versions and records. This protocol admits no unreviewed coordinate, permission or runtime behavior changes.; RES-cloud-host-composition (append): Each module registers through its own module entry point and route fragment; the host composition only lists modules; route and binding conflicts are resolved by the integration owner at merge.; RES-contract-consumer-pins (append): A consumer task updates the pin it needs through a reviewed dependency change to the exact published candidate containing its closure; no consumer pins an unpublished closure or references Contracts source.
Unblocks: APP.03, DEV.02, DEV.09, DEV.14

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline/local Worker+DO test harness only (per P2-017, no hosted live-service CI): expiry/renewal timers, restarted epoch, offline-without-false-availability.
Completion evidence for the ledger: Expiry/renewal timer test results, restarted-epoch test, per-device-row isolation proof.
Notes: Exact Cloud-side project path for the WP21 to WP26 service split is not yet established in-repo; glob is a reasonable placeholder pending that layout decision (the Cloud lane / WP22 to WP23 territory).

2026-10-06 narrow production addendum (docs/decisions/production-delivery-addendum-2026-10-06.md). CLOUD.13 supplies actual durable device/installation/session authority plus typed instance-target authorization. ApplicationPresenceDO instanceEpoch/presence stays DEV.01-owned, never a fictitious D1 instance-presence prerequisite or reverse cycle.

2026-10-07 actual application registration producer (docs/decisions/application-presence-epoch-and-progressive-production-2026-10-07.md) supersedes the placeholder path and whole13/29 implementation-start gates only. Platform UI is sole DEV01 producer. Full current13/11/75/21 and29 realtime composition remain mandatory completion; standalone durable SQLite DO/core/owned reader components advance now. No random epoch, D1 presence/membership table, ActorRef/User alias, permissive port or constructor-created authority. Durable uint64 owner counter survives lease expiry/eviction; heartbeat30s/renew10s, current one personal active workspace, nonrevoked session/device/install and actual product authority every public operation.

2026-10-07 stable installation owner/validation binding (docs/decisions/application-presence-stable-owner-and-validation-2026-10-07.md): private DO key SHA256 of canonical realm/device/install/product JSON array, retained immutable user/personal-workspace fence and monotone counter across recovery; exact existing DevicesModule.cs append. Consume only actual published Contracts.Validation287.1 with its same-cohort closure and method-specific generated validators. All existing current permission/replay/timing/completion obligations remain.

P2-049 2026-10-07 exact keyed current-credential ingress (docs/decisions/application-presence-keyed-ingress-2026-10-07.md): ApplicationPresenceModule owns one fixed key for three real published Application routes only, never global verifier replacement or caller-selected provider. Actual C13 raw credential/configured Origin/CSRF/current personal-owner checks before admission and fresh final core disclosure; missing producer unavailable. Exact two existing ingress supports preserve all unrelated policies/operation obligations; no rich shared authority DTO or HAR key admission. Public current-session composition support is precisely docs/decisions/current-session-public-host-and-codec-composition-2026-10-07.md. Only six generated unary methods are first activated with genuine keyed raw request authority and exact owner namespaces. No fictitious browserActivity/logout RPC, native RevokeSession relabel, default Foundation origin or active authentication facade from component types. Actual CON31 344.1 peer/codec closure is required; CON39 browser logout original-command publication is separate.
```

```text
Execute ArcForges delivery task DEV.02 — Durable target queue.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\device-bridge.md (anchor task-dev-02).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/dev-02 (python tools/delivery.py claim DEV.02 --worker <name>); task branch task/dev-02 in Cloud; ledger record ledger/tasks/dev-02.md.
Kind/size: service/M. Baseline: not-started.
Outcome: ToolRequest freezes product/device/installation and current instance epoch; commands/receipts remain in D1. Another application cannot claim; duplicate/lost ack/expiry and per-owner budget proven.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-26.01 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\26-remote-action-and-tool-bridge.md, anchor rule-wp-26.01

Entry condition: adoption slice ADOPT.07.device-bridge is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] DEV.01: the real installation/epoch projection to freeze against
- [contract] CON.10: published ToolRequest wire shape (contracts/03 §5.1 fields)
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Cloud:src/ArcForges.Cloud/ToolBridge/**
Shared resources (follow the owner protocol): RES-cloud-d1-migrations (append): One global D1 migration sequence: each module task authors migrations under its module prefix; the integration owner assigns the global sequence number at merge, regenerates the plan manifest and rejects edits to merged migrations; the migrator applies in sequence with receipts.; RES-cloud-policy-inputs (append): Append only task-owned source/test bindings and immutable successor receipts. Rebase before integration; regenerate actual input hashes and plan manifests; chain from the receipt active on main; preserve all prior versions and records. This protocol admits no unreviewed coordinate, permission or runtime behavior changes.
Unblocks: AND.25, DEV.04, DEV.06, DEV.07, DEV.08, DEV.09, DEV.13, DEV.14, WEB.28

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline/local Worker+D1 test harness: another-app-cannot-claim, duplicate/lost-ack/expiry, per-owner budget.
Completion evidence for the ledger: Claim-isolation, duplicate/lost-ack, expiry and budget test results.
```

```text
Execute ArcForges delivery task DEV.03 — Owner reauthorization (Device.Runtime local re-authorization).

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\device-bridge.md (anchor task-dev-03).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/dev-03 (python tools/delivery.py claim DEV.03 --worker <name>); task branch task/dev-03 in DesktopPlatform; ledger record ledger/tasks/dev-03.md.
Kind/size: service/M. Baseline: not-started.
Outcome: Device.Runtime invokes registered typed in-process product handlers after current grant/resource/revision/egress checks; no local product RPC, shared database or delegation through a shared integration owner.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-26.02 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\26-remote-action-and-tool-bridge.md, anchor rule-wp-26.02

Entry condition: adoption slice ADOPT.02.device-bridge is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] AST.11: the Device.Runtime project skeleton and typed dispatch adapter interfaces built as the 17.01 fixture boundary
- [artifact] APP.05: the exact WP-14.04 owner approval/authorization enforcement point
- [artifact] PLT.43: published capability leases and trust verification
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:src/BuildingBlocks/ArcForges.Communication.DeviceRuntime/**
Unblocks: AND.25, DEV.05, DEV.06, DEV.09, DEV.13, DEV.14, WEB.28

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline unit tests: no local product RPC/shared database/integration owner delegation.
Completion evidence for the ledger: Negative tests proving no RPC/shared-database/integration owner path exists.
```

```text
Execute ArcForges delivery task DEV.04 — Execution and result deduplication -- Cloud D1 attempt/result store.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\device-bridge.md (anchor task-dev-04).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/dev-04 (python tools/delivery.py claim DEV.04 --worker <name>); task branch task/dev-04 in Cloud; ledger record ledger/tasks/dev-04.md.
Kind/size: service/M. Baseline: not-started.
Outcome: Bridge request/result persisted in D1 using full ApplicationTarget and (toolRequestId,attemptId,commandId) plus result hash; multiple tool requests per attempt both persist; identical replay returns its own receipt; changed result hash refuses; stale epoch and cross-application delivery rejected.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-26.03 (Cloud-side D1 attempt-row persistence, hash dedup and cross-application delivery guard): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\26-remote-action-and-tool-bridge.md, anchor rule-wp-26.03
- WP-16:tool-result-acceptance-paragraph-between Tool-result acceptance paragraph (between §5 and §6): two distinct toolRequestIds in one attempt both persist and each replay returns its own original receipt; a changed result under the same (toolRequestId,attemptId,commandId) refuses with command.reused_identifier; lost acknowledgement never allocates a fresh command or drops the second result. Bound to the wire registry, TK-05 and task.tool_result -- the same key WP-26.03 uses. (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\16-unified-execution-engine.md, package-level obligation

Entry condition: adoption slice ADOPT.07.device-bridge is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] DEV.02: the real durable target queue to attach results to
- [contract] CON.10: published (toolRequestId,attemptId,commandId)+hash wire shape, TK-05, task.tool_result
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Cloud:src/ArcForges.Cloud/ToolBridge/**
Shared resources (follow the owner protocol): RES-cloud-d1-migrations (append): One global D1 migration sequence: each module task authors migrations under its module prefix; the integration owner assigns the global sequence number at merge, regenerates the plan manifest and rejects edits to merged migrations; the migrator applies in sequence with receipts.; RES-cloud-policy-inputs (append): Append only task-owned source/test bindings and immutable successor receipts. Rebase before integration; regenerate actual input hashes and plan manifests; chain from the receipt active on main; preserve all prior versions and records. This protocol admits no unreviewed coordinate, permission or runtime behavior changes.
Unblocks: DEV.09, DEV.12, DEV.13, DEV.14

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline/local D1 test harness: multi-request-per-attempt, identical replay, changed-hash refusal, stale epoch, cross-application delivery rejection.
Completion evidence for the ledger: Dedup/replay/hash-mismatch/stale-epoch test results.
Notes: Split from WP-26.03 by repo; see DEV.05 for the desktop-side half and IM.tool-bridge-dedup-agreement for the cross-repo proof.
```

```text
Execute ArcForges delivery task DEV.05 — Execution and result deduplication -- Desktop command_log agreement.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\device-bridge.md (anchor task-dev-05).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/dev-05 (python tools/delivery.py claim DEV.05 --worker <name>); task branch task/dev-05 in DesktopPlatform; ledger record ledger/tasks/dev-05.md.
Kind/size: service/M. Baseline: not-started.
Outcome: Owner handler's normal in-process validation records the same (toolRequestId,attemptId,commandId) plus result hash into a local command_log; agrees with the Cloud attempt row (BI-03); duplicate delivery and uncertain external effect handled locally.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-26.03 (Desktop command_log persistence and (toolRequestId,attemptId,commandId) agreement with the Cloud attempt row): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\26-remote-action-and-tool-bridge.md, anchor rule-wp-26.03
- WP-16:tool-result-acceptance-paragraph-between Tool-result acceptance paragraph (between §5 and §6): two distinct toolRequestIds in one attempt both persist and each replay returns its own original receipt; a changed result under the same (toolRequestId,attemptId,commandId) refuses with command.reused_identifier; lost acknowledgement never allocates a fresh command or drops the second result. Bound to the wire registry, TK-05 and task.tool_result -- the same key WP-26.03 uses. (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\16-unified-execution-engine.md, package-level obligation

Entry condition: adoption slice ADOPT.02.device-bridge is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] DEV.03: the real owner-reauthorization call site to log results from
- [artifact] EXE.01: the execution-persistence project to extend with the command_log table, rather than a parallel store
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:src/BuildingBlocks/ArcForges.Execution.Persistence/**; DesktopPlatform:src/BuildingBlocks/ArcForges.Communication.DeviceRuntime/**
Shared resources (follow the owner protocol): RES-assistant-store-schema (append): Numbered migrations are allocated at merge by the integration owner (a rebase renumbers pending migrations); each migration is forward-only with its recovery and downgrade-refusal tests; no task edits a merged migration.
Unblocks: DEV.09, DEV.12, DEV.13, DEV.14

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline unit tests: duplicate delivery, uncertain external effect, local/Cloud key agreement using a contract-bound fixture for the Cloud side.
Completion evidence for the ledger: Duplicate-delivery and uncertain-effect test results; local-vs-fixture-Cloud key agreement proof.
Notes: Real cross-repo agreement (this store vs the actual Cloud D1 row) is proven by IM.tool-bridge-dedup-agreement, not by this task alone.
```

```text
Execute ArcForges delivery task DEV.06 — Remote approval and steering.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\device-bridge.md (anchor task-dev-06).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/dev-06 (python tools/delivery.py claim DEV.06 --worker <name>); task branch task/dev-06 in Cloud; ledger record ledger/tasks/dev-06.md.
Kind/size: service/M. Baseline: not-started.
Outcome: One-target approvals, sensitive local-presence requirements and ordinary steering bounds preserved; mobile biometric cannot substitute for target presence; stale approval fails.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-26.04 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\26-remote-action-and-tool-bridge.md, anchor rule-wp-26.04

Entry condition: adoption slice ADOPT.07.device-bridge is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] DEV.02: the real durable target queue to gate with approval
- [artifact] DEV.03: the real desktop local-presence enforcement to require
- [artifact] PLT.39: published approval/steering/step-up mechanism
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Cloud:src/ArcForges.Cloud/ToolBridge/**
Shared resources (follow the owner protocol): RES-cloud-d1-migrations (append): One global D1 migration sequence: each module task authors migrations under its module prefix; the integration owner assigns the global sequence number at merge, regenerates the plan manifest and rejects edits to merged migrations; the migrator applies in sequence with receipts.; RES-cloud-policy-inputs (append): Append only task-owned source/test bindings and immutable successor receipts. Rebase before integration; regenerate actual input hashes and plan manifests; chain from the receipt active on main; preserve all prior versions and records. This protocol admits no unreviewed coordinate, permission or runtime behavior changes.
Unblocks: AND.25, DEV.09, DEV.13, WEB.28

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline/local test harness: mobile-biometric-cannot-substitute, stale-approval-fails.
Completion evidence for the ledger: Biometric-substitution-refusal and stale-approval test results.
```

```text
Execute ArcForges delivery task DEV.07 — Offline expiry and recovery.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\device-bridge.md (anchor task-dev-07).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/dev-07 (python tools/delivery.py claim DEV.07 --worker <name>); task branch task/dev-07 in Cloud; ledger record ledger/tasks/dev-07.md.
Kind/size: service/S. Baseline: not-started.
Outcome: Explicit offline queue expiry/reconciliation; changing the selected app cannot retarget queued work. Disconnect/revoke/reinstall proven with no silent alternate product/device selection.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-26.05 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\26-remote-action-and-tool-bridge.md, anchor rule-wp-26.05

Entry condition: adoption slice ADOPT.07.device-bridge is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] DEV.02: the real durable target queue to expire/reconcile
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Cloud:src/ArcForges.Cloud/ToolBridge/**
Shared resources (follow the owner protocol): RES-cloud-d1-migrations (append): One global D1 migration sequence: each module task authors migrations under its module prefix; the integration owner assigns the global sequence number at merge, regenerates the plan manifest and rejects edits to merged migrations; the migrator applies in sequence with receipts.; RES-cloud-policy-inputs (append): Append only task-owned source/test bindings and immutable successor receipts. Rebase before integration; regenerate actual input hashes and plan manifests; chain from the receipt active on main; preserve all prior versions and records. This protocol admits no unreviewed coordinate, permission or runtime behavior changes.
Unblocks: AND.25, DEV.09, WEB.28

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline/local test harness: disconnect/revoke/reinstall, no silent retarget.
Completion evidence for the ledger: Disconnect/revoke/reinstall test results.
```

```text
Execute ArcForges delivery task DEV.08 — Frozen application locality.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\device-bridge.md (anchor task-dev-08).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/dev-08 (python tools/delivery.py claim DEV.08 --worker <name>); task branch task/dev-08 in Cloud; ledger record ledger/tasks/dev-08.md.
Kind/size: service/S. Baseline: not-started.
Outcome: Cloud-only steps may run without a desktop; every device step in one execution remains in the frozen product scope. Own-app multi-tool workflow passes; cross-product capability absent/future.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-26.06 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\26-remote-action-and-tool-bridge.md, anchor rule-wp-26.06

Entry condition: adoption slice ADOPT.07.device-bridge is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] DEV.02: the real durable target queue whose ApplicationTarget freeze this enforces
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Cloud:src/ArcForges.Cloud/ToolBridge/**
Shared resources (follow the owner protocol): RES-cloud-d1-migrations (append): One global D1 migration sequence: each module task authors migrations under its module prefix; the integration owner assigns the global sequence number at merge, regenerates the plan manifest and rejects edits to merged migrations; the migrator applies in sequence with receipts.; RES-cloud-policy-inputs (append): Append only task-owned source/test bindings and immutable successor receipts. Rebase before integration; regenerate actual input hashes and plan manifests; chain from the receipt active on main; preserve all prior versions and records. This protocol admits no unreviewed coordinate, permission or runtime behavior changes.
Unblocks: DEV.09, HAR.05

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline/local test harness: own-app multi-tool workflow, cross-product-absent assertion.
Completion evidence for the ledger: Multi-tool workflow and cross-product-absence test results.
```

```text
Execute ArcForges delivery task DEV.09 — Owned-artifact receipt and real integration.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\device-bridge.md (anchor task-dev-09).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/dev-09 (python tools/delivery.py claim DEV.09 --worker <name>); task branch task/dev-09 in Cloud; ledger record ledger/tasks/dev-09.md.
Kind/size: acceptance/M. Baseline: not-started.
Outcome: WP26 built/packed once from a clean environment across both repositories; all applicable UX acceptance groups recorded; failure/recovery and the real boundaries above proven; no later-provider fixture closes a real WP26 gate.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-26.90 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\26-remote-action-and-tool-bridge.md, anchor rule-wp-26.90

Entry condition: adoption slice ADOPT.07.device-bridge is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] DEV.01: completed WP-26.00
- [artifact] DEV.02: completed WP-26.01
- [artifact] DEV.03: completed WP-26.02
- [artifact] DEV.04: completed WP-26.03 Cloud half
- [artifact] DEV.05: completed WP-26.03 Desktop half
- [artifact] DEV.06: completed WP-26.04
- [artifact] DEV.07: completed WP-26.05
- [artifact] DEV.08: completed WP-26.06
- [artifact] DEV.12: package task delivered
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Cloud:artifacts/evidence/**
Shared resources (follow the owner protocol): RES-cloud-policy-inputs (append): Append only task-owned source/test bindings and immutable successor receipts. Rebase before integration; regenerate actual input hashes and plan manifests; chain from the receipt active on main; preserve all prior versions and records. This protocol admits no unreviewed coordinate, permission or runtime behavior changes.

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Clean-environment build/pack across both repos; P2-017 scope only (no live-service CI); real cross-repo dedup agreement proven per IM.tool-bridge-dedup-agreement.
Completion evidence for the ledger: Source commits (both repos), artifact versions/hashes, environment, UX-D/E rows, real-boundary test results.
Notes: Own capabilities are real here (device-tool-path mechanics are 'must be real early' per implementation-sequence §3); the CONTENT of tool requests (model-driven planning) stays fixture/scripted until WP-52 -- see IM.agent-driven-device-tool-use for that separate real-scenario proof.
```

```text
Execute ArcForges delivery task DEV.12 — Cross-repo (toolRequestId,attemptId,commandId) agreement between Cloud D1 and Desktop command_log.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\device-bridge.md (anchor task-dev-12).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/dev-12 (python tools/delivery.py claim DEV.12 --worker <name>); task branch task/dev-12 in Cloud; ledger record ledger/tasks/dev-12.md.
Kind/size: integration/M. Baseline: not-started.
Outcome: BI-03: the Cloud attempt row and the desktop command_log genuinely agree under concurrent/duplicate/lost-ack delivery, not just each side's own unit tests

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-26.03 (cross-repo agreement proof beyond each side's own unit coverage): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\26-remote-action-and-tool-bridge.md, anchor rule-wp-26.03

Entry condition: adoption slice ADOPT.07.device-bridge is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] DEV.04: real, delivered outcome of DEV.04 (Execution and result deduplication -- Cloud D1 attempt/result store)
- [artifact] DEV.05: real, delivered outcome of DEV.05 (Execution and result deduplication -- Desktop command_log agreement)
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: 
Unblocks: AND.25, CLOUD.36, DEV.09, DEV.13, DEV.14, WEB.28

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Local real-integration run of the affected scenario in an existing environment, recorded once; offline and static checks in CI; no hosted runtime, device, browser, live-service or inference CI (P2-017).
Completion evidence for the ledger: BI-03: the Cloud attempt row and the desktop command_log genuinely agree under concurrent/duplicate/lost-ack delivery, not just each side's own unit tests
```

```text
Execute ArcForges delivery task DEV.13 — Real Harness-planned tool request flowing through the real device bridge end-to-end.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\device-bridge.md (anchor task-dev-13).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/dev-13 (python tools/delivery.py claim DEV.13 --worker <name>); task branch task/dev-13 in Cloud; ledger record ledger/tasks/dev-13.md.
Kind/size: integration/M. Baseline: not-started.
Outcome: an actual Cloud-planned Agent Task step (not a scripted ToolRequest) reaches a real desktop, is locally re-authorized, executed and its result accepted -- the real integration producer-artifacts.md names as closing WP26's remaining fixture-content gap

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-52.05 (all work except the parts mapped to AST.19, HAR.05): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\52-cloud-harness.md, anchor rule-wp-52.05

Entry condition: adoption slice ADOPT.07.device-bridge is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] AST.19: real, delivered outcome of AST.19 (Real Cloud Harness turn loop replacing the fixture turn endpoint)
- [artifact] HAR.02: real Harness approval and tool-dispatch path
- [artifact] DEV.02: the real durable target queue
- [artifact] DEV.03: real owner reauthorization on the desktop
- [artifact] DEV.04: real Cloud attempt and result deduplication
- [artifact] DEV.05: real desktop command_log agreement
- [artifact] DEV.06: real remote approval and steering
- [artifact] DEV.12: the cross-repository (toolRequestId, attemptId, commandId) agreement
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: 
Unblocks: HAR.05

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Local real-integration run of the affected scenario in an existing environment, recorded once; offline and static checks in CI; no hosted runtime, device, browser, live-service or inference CI (P2-017).
Completion evidence for the ledger: an actual Cloud-planned Agent Task step (not a scripted ToolRequest) reaches a real desktop, is locally re-authorized, executed and its result accepted -- the real integration producer-artifacts.md names as closing WP26's remaining fixture-content gap
```

```text
Execute ArcForges delivery task DEV.14 — Real device tool bridge over the deployed realtime transport.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\device-bridge.md (anchor task-dev-14).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform). Also touches: Cloud.
Claim and handoff record: claims/dev-14 (python tools/delivery.py claim DEV.14 --worker <name>); task branch task/dev-14 in DesktopPlatform; ledger record ledger/tasks/dev-14.md.
Kind/size: integration/M. Baseline: not-started.
Outcome: The device tool path (pull, local re-authorisation, generated decode, typed invocation, idempotent result) works over the real deployed stream transport -- this is explicitly must-be-real-early per implementation-sequence §3, owned jointly with the assistant lanes WP-26

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-24.01 (device-targeted feed real integration): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\24-realtime-and-reliable-events.md, anchor rule-wp-24.01

Entry condition: adoption slice ADOPT.02.device-bridge is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] CLOUD.29: real, delivered outcome of CLOUD.29 (Stream connection and authentication (EventService.Watch/ExecutionService.WatchOutput shells))
- [artifact] CLOUD.30: real, delivered outcome of CLOUD.30 (Scoped subscription (owner/product/filter/recovery-generation binding))
- [artifact] CLOUD.31: real, delivered outcome of CLOUD.31 (Cursor and gap handling (DO projection backed by D1 outbox))
- [artifact] CLOUD.33: real, delivered outcome of CLOUD.33 (Publication and wake (D1 outbox to bounded DO feed via Queues))
- [artifact] CLOUD.34: real, delivered outcome of CLOUD.34 (Bounded stream lifecycle)
- [artifact] AST.11: assistant Cloud client and device runtime
- [artifact] DEV.01: real application presence
- [artifact] DEV.02: the real durable target queue
- [artifact] DEV.03: real owner reauthorization on the desktop
- [artifact] DEV.04: real Cloud attempt and result deduplication
- [artifact] DEV.05: real desktop command_log agreement
- [artifact] DEV.12: the cross-repository (toolRequestId, attemptId, commandId) agreement
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: 
Unblocks: CLOUD.36

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Local real-integration run of the affected scenario in an existing environment, recorded once; offline and static checks in CI; no hosted runtime, device, browser, live-service or inference CI (P2-017).
Completion evidence for the ledger: The device tool path (pull, local re-authorisation, generated decode, typed invocation, idempotent result) works over the real deployed stream transport -- this is explicitly must-be-real-early per implementation-sequence §3, owned jointly with the assistant lanes WP-26
```
