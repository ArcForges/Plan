# ArcForges delivery task list

Generated from Design `docs/planning/delivery/delivery-graph.json` by `tools/delivery.py`; do not edit by hand.
There is no Current task. Any number of workers execute different ready tasks at the same time.
This list is an index for reading and selection; its order is not a schedule. `python tools/delivery.py ready`
lists what may be claimed now from the merged graph, ledger and claims. Each task's self-contained prompt is in
the lane file linked from its section, and `arcforges-implementation.md` is the procedure.

Tasks: 529 in 27 lanes, plus 58 adoption slices listed in the adoption section.

## Adoption stage — [prompts](tasks/adoption.md)

| Task | Repository | Size | Start prerequisites | Title |
|---|---|---|---|---|
| ADOPT.01 | Plan | S | — | Freeze the adoption baseline |
| ADOPT.02 | DesktopPlatform | S | ADOPT.01 | Adopt DesktopPlatform |
| ADOPT.03 | Contracts | S | ADOPT.01 | Adopt Contracts |
| ADOPT.04 | ArcNotes | S | ADOPT.01 | Adopt ArcNotes |
| ADOPT.05 | ArcScope | S | ADOPT.01 | Adopt ArcScope |
| ADOPT.06 | ArcSlate | S | ADOPT.01 | Adopt ArcSlate |
| ADOPT.07 | Cloud | S | ADOPT.01 | Adopt Cloud |
| ADOPT.08 | AI | S | ADOPT.01 | Adopt AI |
| ADOPT.09 | Web | S | ADOPT.01 | Adopt Web |
| ADOPT.10 | Mobile | S | ADOPT.01 | Adopt Mobile |
| ADOPT.11 | Design | S | ADOPT.01 | Reconcile Design and Plan documentation for adoption |

### Adoption slices

| Slice | Repository | Size | Start prerequisites | Title (tasks it opens) |
|---|---|---|---|---|
| ADOPT.02.app-composition | DesktopPlatform | S | ADOPT.01 | Adopt DesktopPlatform: Application composition (6) |
| ADOPT.02.assistant | DesktopPlatform | S | ADOPT.01 | Adopt DesktopPlatform: Embedded assistant (22) |
| ADOPT.02.cloud | DesktopPlatform | S | ADOPT.01 | Adopt DesktopPlatform: Cloud core (2) |
| ADOPT.02.device-bridge | DesktopPlatform | S | ADOPT.01 | Adopt DesktopPlatform: Application presence and tool bridge (3) |
| ADOPT.02.execution | DesktopPlatform | S | ADOPT.01 | Adopt DesktopPlatform: Execution engine (9) |
| ADOPT.02.extensions | DesktopPlatform | S | ADOPT.01 | Adopt DesktopPlatform: Extension platform and integrations (7) |
| ADOPT.02.foundation | DesktopPlatform | S | ADOPT.01 | Adopt DesktopPlatform: Foundation values (7) |
| ADOPT.02.governance | DesktopPlatform | S | ADOPT.01 | Adopt DesktopPlatform: Family governance and policy tests (4) |
| ADOPT.02.native | DesktopPlatform | S | ADOPT.01 | Adopt DesktopPlatform: Native producers and probes (25) |
| ADOPT.02.platform | DesktopPlatform | S | ADOPT.01 | Adopt DesktopPlatform: Desktop platform mechanisms (56) |
| ADOPT.02.policy | DesktopPlatform | S | ADOPT.01 | Adopt DesktopPlatform: Dynamic policy and configuration (1) |
| ADOPT.02.release | DesktopPlatform | S | ADOPT.01 | Adopt DesktopPlatform: Release readiness and family release (2) |
| ADOPT.02.runtime-proofs | DesktopPlatform | S | ADOPT.01 | Adopt DesktopPlatform: Runtime proofs (4) |
| ADOPT.02.updater | DesktopPlatform | S | ADOPT.01 | Adopt DesktopPlatform: Desktop distribution and update (8) |
| ADOPT.03.contracts | Contracts | S | ADOPT.01 | Adopt Contracts: Contracts schema closures (22) |
| ADOPT.03.extensions | Contracts | S | ADOPT.01 | Adopt Contracts: Extension platform and integrations (3) |
| ADOPT.03.governance | Contracts | S | ADOPT.01 | Adopt Contracts: Family governance and policy tests (2) |
| ADOPT.03.release | Contracts | S | ADOPT.01 | Adopt Contracts: Release readiness and family release (1) |
| ADOPT.04.app-composition | ArcNotes | S | ADOPT.01 | Adopt ArcNotes: Application composition (2) |
| ADOPT.04.arcnotes | ArcNotes | S | ADOPT.01 | Adopt ArcNotes: ArcNotes (35) |
| ADOPT.04.governance | ArcNotes | S | ADOPT.01 | Adopt ArcNotes: Family governance and policy tests (1) |
| ADOPT.04.release | ArcNotes | S | ADOPT.01 | Adopt ArcNotes: Release readiness and family release (1) |
| ADOPT.04.runtime-proofs | ArcNotes | S | ADOPT.01 | Adopt ArcNotes: Runtime proofs (1) |
| ADOPT.05.arcscope | ArcScope | S | ADOPT.01 | Adopt ArcScope: ArcScope (27) |
| ADOPT.05.governance | ArcScope | S | ADOPT.01 | Adopt ArcScope: Family governance and policy tests (1) |
| ADOPT.05.release | ArcScope | S | ADOPT.01 | Adopt ArcScope: Release readiness and family release (1) |
| ADOPT.05.runtime-proofs | ArcScope | S | ADOPT.01 | Adopt ArcScope: Runtime proofs (1) |
| ADOPT.05.simulator | ArcScope | S | ADOPT.01 | Adopt ArcScope: ArcScope Cloud simulator (1) |
| ADOPT.06.arcslate | ArcSlate | S | ADOPT.01 | Adopt ArcSlate: ArcSlate (41) |
| ADOPT.06.governance | ArcSlate | S | ADOPT.01 | Adopt ArcSlate: Family governance and policy tests (1) |
| ADOPT.06.release | ArcSlate | S | ADOPT.01 | Adopt ArcSlate: Release readiness and family release (1) |
| ADOPT.06.runtime-proofs | ArcSlate | S | ADOPT.01 | Adopt ArcSlate: Runtime proofs (1) |
| ADOPT.07.ai-routing | Cloud | S | ADOPT.01 | Adopt Cloud: Workers AI routing and metering (6) |
| ADOPT.07.cloud | Cloud | S | ADOPT.01 | Adopt Cloud: Cloud core (58) |
| ADOPT.07.commerce | Cloud | S | ADOPT.01 | Adopt Cloud: Commerce, entitlement and credits (15) |
| ADOPT.07.device-bridge | Cloud | S | ADOPT.01 | Adopt Cloud: Application presence and tool bridge (9) |
| ADOPT.07.extensions | Cloud | S | ADOPT.01 | Adopt Cloud: Extension platform and integrations (1) |
| ADOPT.07.governance | Cloud | S | ADOPT.01 | Adopt Cloud: Family governance and policy tests (1) |
| ADOPT.07.harness | Cloud | S | ADOPT.01 | Adopt Cloud: Cloud Harness (2) |
| ADOPT.07.operations | Cloud | S | ADOPT.01 | Adopt Cloud: Operations, support and trust and safety (9) |
| ADOPT.07.policy | Cloud | S | ADOPT.01 | Adopt Cloud: Dynamic policy and configuration (10) |
| ADOPT.07.release | Cloud | S | ADOPT.01 | Adopt Cloud: Release readiness and family release (3) |
| ADOPT.07.runtime-proofs | Cloud | S | ADOPT.01 | Adopt Cloud: Runtime proofs (1) |
| ADOPT.07.search | Cloud | S | ADOPT.01 | Adopt Cloud: Knowledge search and retrieval (8) |
| ADOPT.07.simulator | Cloud | S | ADOPT.01 | Adopt Cloud: ArcScope Cloud simulator (9) |
| ADOPT.08.ai-routing | AI | S | ADOPT.01 | Adopt AI: Workers AI routing and metering (5) |
| ADOPT.08.extensions | AI | S | ADOPT.01 | Adopt AI: Extension platform and integrations (1) |
| ADOPT.08.governance | AI | S | ADOPT.01 | Adopt AI: Family governance and policy tests (1) |
| ADOPT.08.harness | AI | S | ADOPT.01 | Adopt AI: Cloud Harness (7) |
| ADOPT.09.governance | Web | S | ADOPT.01 | Adopt Web: Family governance and policy tests (1) |
| ADOPT.09.operations | Web | S | ADOPT.01 | Adopt Web: Operations, support and trust and safety (4) |
| ADOPT.09.release | Web | S | ADOPT.01 | Adopt Web: Release readiness and family release (1) |
| ADOPT.09.runtime-proofs | Web | S | ADOPT.01 | Adopt Web: Runtime proofs (1) |
| ADOPT.09.web | Web | S | ADOPT.01 | Adopt Web: Web (31) |
| ADOPT.10.android | Mobile | S | ADOPT.01 | Adopt Mobile: Android companion (26) |
| ADOPT.10.governance | Mobile | S | ADOPT.01 | Adopt Mobile: Family governance and policy tests (1) |
| ADOPT.10.release | Mobile | S | ADOPT.01 | Adopt Mobile: Release readiness and family release (1) |
| ADOPT.10.runtime-proofs | Mobile | S | ADOPT.01 | Adopt Mobile: Runtime proofs (1) |

## Family governance and policy tests — [prompts](tasks/governance.md)

| Task | Repository | Size | Start prerequisites | Title |
|---|---|---|---|---|
| GOV.01 | DesktopPlatform | XL | — | Specification, naming, licence-boundary and provenance freeze (WP00, accepted) |
| GOV.02 | DesktopPlatform | XL | GOV.01 | Repository reconciliation and target layout (WP01, accepted) |
| GOV.03 | DesktopPlatform | XL | GOV.02 | Build governance, packaging policy and analyzers (WP02, accepted) |
| GOV.04 | DesktopPlatform | L | GOV.03, GOV.01, ADOPT.02.governance (adoption) | Shared architecture/repository policy-test engine and DesktopPlatform enforcement |
| GOV.05 | Contracts | L | GOV.04, CON.90, ADOPT.03.governance (adoption) | Contracts policy tests and contract/serialization policy engine |
| GOV.06 | ArcNotes | S | GOV.04, GOV.05, ADOPT.04.governance (adoption) | ArcNotes policy tests |
| GOV.07 | ArcScope | S | GOV.04, GOV.05, ADOPT.05.governance (adoption) | ArcScope policy tests |
| GOV.08 | ArcSlate | S | GOV.04, GOV.05, ADOPT.06.governance (adoption) | ArcSlate policy tests |
| GOV.09 | Cloud | M | GOV.04, GOV.05, ADOPT.07.governance (adoption) | Cloud policy tests |
| GOV.10 | AI | S | GOV.04, GOV.05, ADOPT.08.governance (adoption) | AI (Workflow Harness) policy tests |
| GOV.11 | Web | M | GOV.03, GOV.01, ADOPT.09.governance (adoption) | Web policy tests (Node/TS mechanism) |
| GOV.12 | Mobile | M | GOV.03, GOV.04, ADOPT.10.governance (adoption) | Mobile policy tests (Gradle/Kotlin mechanism) |
| GOV.13 | DesktopPlatform | M | GOV.04, ADOPT.02.governance (adoption) | Invariant enforcement accounting report |
| GOV.14 | DesktopPlatform | M | GOV.01, ADOPT.02.governance (adoption) | Specification integrity checks over the Design repository |
| GOV.15 | DesktopPlatform | M | GOV.04, GOV.05, GOV.06, GOV.07, GOV.08, GOV.09, GOV.10, GOV.11, GOV.12, GOV.13, GOV.14, ADOPT.02.governance (adoption) | WP05 stage integration verification |
| GOV.16 | Contracts | M | CON.18, ADOPT.03.governance (adoption) | Operation-catalogue authorization reachability matrix and identity boundary evidence |

## Contracts schema closures — [prompts](tasks/contracts.md)

| Task | Repository | Size | Start prerequisites | Title |
|---|---|---|---|---|
| CON.01 | Contracts | S | ADOPT.03.contracts (adoption) | Shard contended eng inventory/constraint files by domain; fix one-owner merge protocol |
| CON.02 | Contracts | M | CON.91, ADOPT.03.contracts (adoption) | Capability/action/context/version/health descriptor records + immutable oversized-body reference (EncodedBodyRef) |
| CON.03 | Contracts | M | CON.02, ADOPT.03.contracts (adoption) | Resource/Sync owner-body admission: closed Sync mutation allowlist + cross-owner/wrong-revision/opaque-object/forbidden-path negatives |
| CON.04 | Contracts | L | ADOPT.03.contracts (adoption) | ContentSandbox service schema (24 methods: session/slot/media/image/PDF/OTIO) |
| CON.05 | Contracts | M | ADOPT.03.contracts (adoption) | Extension/Connector/LocalBootstrap service schema (annex09 helper closure minus ContentSandbox) |
| CON.06 | Contracts | L | CON.02, ADOPT.03.contracts (adoption) | Product in-process port completion: INotesOperations/IScopeOperations/ISlateOperations/IChatOperations + infra ports |
| CON.07 | Contracts | L | ADOPT.03.contracts (adoption) | Identity/session/device operation registry + native-auth and browser HTTP exceptions |
| CON.08 | Contracts | M | ADOPT.03.contracts (adoption) | Entitlement/commerce operation registry |
| CON.09 | Contracts | L | CON.03, ADOPT.03.contracts (adoption) | Sync/resource-transfer/objects operation registry + realm-transfer.v1 |
| CON.10 | Contracts | L | CON.02, ADOPT.03.contracts (adoption) | Task/approval/bridge/chat/agent/automation/search operation registry + ai-internal package |
| CON.11 | Contracts | M | CON.10, ADOPT.03.contracts (adoption) | Application/history/execution/events operations (annex10's 13 additions) + EventService |
| CON.12 | Contracts | M | ADOPT.03.contracts (adoption) | Extension and policy schemas: manifest.v1/workflow.v1/panel.v1/policy body.v1/configuration.v1 |
| CON.13 | Contracts | S | ADOPT.03.contracts (adoption) | Package catalog operation registry (CatalogService) |
| CON.14 | Contracts | L | CON.13, ADOPT.03.contracts (adoption) | Operator control service (OperatorService, full §9/9.1/9.2 protocol) |
| CON.15 | Contracts | M | CON.11, ADOPT.03.contracts (adoption) | Cloudflare-internal HTTP bindings (AI Worker <-> C# ports beyond ai-internal's chat/task family) |
| CON.16 | Contracts | M | ADOPT.03.contracts (adoption) | Signed catalog/update/realm formats (catalog-index.v1, catalog-revocations.v1, android-update.v1, realm.v1) |
| CON.17 | Contracts | M | CON.92, ADOPT.03.contracts (adoption) | Cross-language compatibility window + canonical semantic hash |
| CON.18 | Contracts | S | ADOPT.03.contracts (adoption) | Operation-scope manifest + authorization-reachability matrix generator |
| CON.19 | Contracts | M | CON.02, CON.18, CON.03, CON.04, CON.05, CON.06, CON.07, CON.08, CON.09, CON.10, CON.11, CON.12, CON.13, CON.14, CON.15, CON.16, CON.17, CON.20, CON.21, CON.22, CON.01, ADOPT.03.contracts (adoption) | WP03.90 — verify the owned Contracts artifact and its real (non-consumer) integration |
| CON.20 | Contracts | M | CON.02, ADOPT.03.contracts (adoption) | Notes public operation registry |
| CON.21 | Contracts | M | CON.02, ADOPT.03.contracts (adoption) | Simulation operation registry |
| CON.22 | Contracts | M | CON.02, ADOPT.03.contracts (adoption) | Account support, notification, data, preference, policy-bundle and export-job operations |
| CON.90 | Contracts | M | — | WP03.00 — split project structure (accepted, historical) |
| CON.91 | Contracts | L | — | WP03.01 — foundation contract types (accepted, historical) |
| CON.92 | Contracts | M | — | WP03.02 — serialization posture (accepted, historical) |

## Foundation values — [prompts](tasks/foundation.md)

| Task | Repository | Size | Start prerequisites | Title |
|---|---|---|---|---|
| FND.01 | DesktopPlatform | S | CON.91, ADOPT.02.foundation (adoption) | Core identity and version-axis value-type skeleton |
| FND.02 | DesktopPlatform | S | CON.91, ADOPT.02.foundation (adoption) | Execution identity, idempotency and Application.Abstractions ports |
| FND.03 | DesktopPlatform | S | CON.91, ADOPT.02.foundation (adoption) | Revision and sequence types |
| FND.04 | DesktopPlatform | S | ADOPT.02.foundation (adoption) | Clock abstraction and canonical time handling |
| FND.05 | DesktopPlatform | M | CON.91, ADOPT.02.foundation (adoption) | Reason-code registry and Outcome result model |
| FND.06 | DesktopPlatform | S | ADOPT.02.foundation (adoption) | Version axis value types |
| FND.07 | DesktopPlatform | S | FND.01, FND.02, FND.03, FND.04, FND.05, FND.06, CON.91, ADOPT.02.foundation (adoption) | Publish Foundation/Application.Abstractions and verify cross-language round trips |

## Runtime proofs — [prompts](tasks/runtime-proofs.md)

| Task | Repository | Size | Start prerequisites | Title |
|---|---|---|---|---|
| PRF.01 | ArcNotes | M | CON.91, FND.01, ADOPT.04.runtime-proofs (adoption) | ArcNotes desktop Native AOT package proof |
| PRF.02 | ArcScope | M | CON.91, FND.01, ADOPT.05.runtime-proofs (adoption) | ArcScope desktop Native AOT package proof |
| PRF.03 | ArcSlate | M | CON.91, FND.01, ADOPT.06.runtime-proofs (adoption) | ArcSlate desktop Native AOT package proof |
| PRF.04 | DesktopPlatform | L | CON.05, ADOPT.02.runtime-proofs (adoption) | Local RPC under AOT: bidirectional named-pipe/UDS probe processes |
| PRF.05 | DesktopPlatform | M | CON.92, PRF.07, ADOPT.02.runtime-proofs (adoption) | Generated gRPC-Web under AOT against deployed Worker/Container ingress |
| PRF.06 | DesktopPlatform | M | PRF.07, ADOPT.02.runtime-proofs (adoption) | Realtime (EventService.Watch/Poll) under AOT |
| PRF.07 | Cloud | XL | CON.92, ADOPT.07.runtime-proofs (adoption) | Cloudflare Native AOT host + D1 + DO/Queue/R2 foundation proof |
| PRF.08 | Web | L | CON.92, PRF.07, ADOPT.09.runtime-proofs (adoption) | React production build and generated TS SDK proof |
| PRF.09 | DesktopPlatform | S | PLT.34, ADOPT.02.runtime-proofs (adoption) | Third-party control AOT admission gate and first candidate |
| PRF.10 | Mobile | L | CON.90, PRF.07, ADOPT.10.runtime-proofs (adoption) | Android Kotlin/Jetpack Compose gRPC-Web and CF proof |

## Desktop platform mechanisms — [prompts](tasks/platform.md)

| Task | Repository | Size | Start prerequisites | Title |
|---|---|---|---|---|
| PLT.01 | DesktopPlatform | L | FND.02, FND.03, FND.05, ADOPT.02.platform (adoption) | Store abstraction and the single transactional write path |
| PLT.02 | DesktopPlatform | M | FND.02, FND.03, ADOPT.02.platform (adoption) | Append-only journal with durability and bounded truncation |
| PLT.03 | DesktopPlatform | L | PLT.02, ADOPT.02.platform (adoption) | Snapshot and crash/corruption recovery |
| PLT.04 | DesktopPlatform | M | FND.06, ADOPT.02.platform (adoption) | Migration runner |
| PLT.05 | DesktopPlatform | M | PLT.01, ADOPT.02.platform (adoption) | Managed resource store (content-addressed blobs) |
| PLT.06 | DesktopPlatform | M | FND.02, ADOPT.02.platform (adoption) | Large append store for high-rate chunked data |
| PLT.07 | DesktopPlatform | S | PLT.01, ADOPT.02.platform (adoption) | Derived-store abstraction and storage-pressure model |
| PLT.08 | DesktopPlatform | S | PLT.01, PLT.02, PLT.03, PLT.04, PLT.05, PLT.06, PLT.07, ADOPT.02.platform (adoption) | Publish Persistence packages and verify real integration |
| PLT.09 | DesktopPlatform | L | PRF.04, CON.04, ADOPT.02.platform (adoption) | Local gRPC transport and framing over Named Pipe/UDS |
| PLT.10 | DesktopPlatform | M | PLT.09, ADOPT.02.platform (adoption) | Parent-owned endpoint identity |
| PLT.11 | DesktopPlatform | M | PLT.10, ADOPT.02.platform (adoption) | Child registration lifecycle |
| PLT.12 | DesktopPlatform | S | PLT.11, ADOPT.02.platform (adoption) | Static routing and version refusal |
| PLT.13 | DesktopPlatform | M | PLT.09, ADOPT.02.platform (adoption) | Bounds and concurrency |
| PLT.14 | DesktopPlatform | M | PLT.09, FND.02, ADOPT.02.platform (adoption) | Disconnect, cancel and retry semantics |
| PLT.15 | DesktopPlatform | M | PLT.09, CON.04, ADOPT.02.platform (adoption) | Brokered large data over the sandbox boundary |
| PLT.16 | DesktopPlatform | S | PLT.09, PLT.10, PLT.11, PLT.12, PLT.13, PLT.14, PLT.15, ADOPT.02.platform (adoption) | Publish LocalRpc package and verify real integration |
| PLT.17 | DesktopPlatform | S | CON.91, FND.01, ADOPT.02.platform (adoption) | Application identity and in-process composition |
| PLT.18 | DesktopPlatform | M | PLT.17, ADOPT.02.platform (adoption) | Static contribution registration |
| PLT.19 | DesktopPlatform | L | PLT.17, CON.91, ADOPT.02.platform (adoption) | Capability registry and selection |
| PLT.20 | DesktopPlatform | M | PLT.19, ADOPT.02.platform (adoption) | Actions and availability |
| PLT.21 | DesktopPlatform | M | PLT.17, ADOPT.02.platform (adoption) | Context providers and freezing |
| PLT.22 | DesktopPlatform | M | PLT.05, PLT.17, ADOPT.02.platform (adoption) | Resources and artifacts resolution |
| PLT.23 | DesktopPlatform | M | PLT.22, ADOPT.02.platform (adoption) | Own navigation, hints and health |
| PLT.24 | DesktopPlatform | L | PLT.19, PLT.20, PLT.21, ADOPT.02.platform (adoption) | Invocation pipeline |
| PLT.25 | DesktopPlatform | S | PLT.17, PLT.18, PLT.19, PLT.20, PLT.21, PLT.22, PLT.23, PLT.24, PLT.57, ADOPT.02.platform (adoption) | Publish Capabilities/Contributions packages and verify real integration |
| PLT.26 | DesktopPlatform | M | PRF.01, ADOPT.02.platform (adoption) | Token system and theming |
| PLT.27 | DesktopPlatform | L | PLT.26, ADOPT.02.platform (adoption) | Windows, panels and layout |
| PLT.28 | DesktopPlatform | M | PLT.27, PLT.20, ADOPT.02.platform (adoption) | Command system |
| PLT.29 | DesktopPlatform | M | PLT.26, PLT.04, ADOPT.02.platform (adoption) | Scoped settings |
| PLT.30 | DesktopPlatform | M | PLT.27, ADOPT.02.platform (adoption) | Attention and notification model |
| PLT.31 | DesktopPlatform | S | PLT.26, FND.05, ADOPT.02.platform (adoption) | Error presentation |
| PLT.32 | DesktopPlatform | M | PLT.28, ADOPT.02.platform (adoption) | Lifecycle, menus and shutdown |
| PLT.33 | DesktopPlatform | L | PLT.27, ADOPT.02.platform (adoption) | Accessibility and localisation baseline |
| PLT.34 | DesktopPlatform | M | PRF.01, ADOPT.02.platform (adoption) | Third-party control admission |
| PLT.35 | DesktopPlatform | S | PLT.26, PLT.27, PLT.28, PLT.29, PLT.30, PLT.31, PLT.32, PLT.33, PLT.34, ADOPT.02.platform (adoption) | Publish DesignSystem/Shell packages and verify real integration |
| PLT.36 | DesktopPlatform | M | FND.01, ADOPT.02.platform (adoption) | Principals and the actor chain |
| PLT.37 | DesktopPlatform | M | PLT.19, ADOPT.02.platform (adoption) | Risk model and classification |
| PLT.38 | DesktopPlatform | L | PLT.36, PLT.37, PLT.10, ADOPT.02.platform (adoption) | Decision pipeline and the four enforcement points |
| PLT.39 | DesktopPlatform | L | PLT.37, PLT.01, ADOPT.02.platform (adoption) | Approval, steering and step-up |
| PLT.40 | DesktopPlatform | L | PLT.36, ADOPT.02.platform (adoption) | Per-application secrets and session isolation |
| PLT.41 | DesktopPlatform | M | PLT.38, ADOPT.02.platform (adoption) | Egress control |
| PLT.42 | DesktopPlatform | L | PLT.21, ADOPT.02.platform (adoption) | Instruction provenance |
| PLT.43 | DesktopPlatform | M | PLT.38, PLT.01, ADOPT.02.platform (adoption) | Capability leases and trust |
| PLT.44 | DesktopPlatform | M | PLT.36, PLT.01, ADOPT.02.platform (adoption) | Append-only audit subsystem |
| PLT.45 | DesktopPlatform | XL | PLT.15, PLT.09, CON.04, ADOPT.02.platform (adoption) | Content helper and OS-enforced isolation (ContentSandbox host) |
| PLT.46 | DesktopPlatform | M | PLT.36, PLT.37, PLT.38, PLT.39, PLT.40, PLT.41, PLT.42, PLT.43, PLT.44, PLT.45, PLT.54, PLT.57, ADOPT.02.platform (adoption) | Publish Security packages and verify real integration |
| PLT.47 | DesktopPlatform | M | FND.01, ADOPT.02.platform (adoption) | Emission and required dimensions |
| PLT.48 | DesktopPlatform | M | PLT.47, ADOPT.02.platform (adoption) | Correlation and causation propagation |
| PLT.49 | DesktopPlatform | L | PLT.40, FND.05, ADOPT.02.platform (adoption) | Redaction by construction |
| PLT.50 | DesktopPlatform | M | PLT.49, ADOPT.02.platform (adoption) | Cardinality and sampling |
| PLT.51 | DesktopPlatform | S | PLT.23, ADOPT.02.platform (adoption) | Health probes |
| PLT.52 | DesktopPlatform | L | PLT.31, PLT.49, ADOPT.02.platform (adoption) | Desktop diagnostics and consent |
| PLT.53 | DesktopPlatform | S | PLT.47, PLT.48, PLT.49, PLT.50, PLT.51, PLT.52, ADOPT.02.platform (adoption) | Publish Observability packages and verify real integration |
| PLT.54 | DesktopPlatform | M | PLT.45, NAT.14, ADOPT.02.platform (adoption) | Real hostile-input containment proof with production parser libraries loaded in ContentSandbox |
| PLT.56 | DesktopPlatform | M | PLT.35, NOTES.03, SCOPE.09, SLATE.22, ADOPT.02.platform (adoption) | Three professional products compose the shared DesignSystem/Shell without divergence |
| PLT.57 | DesktopPlatform | M | PLT.24, PLT.38, APP.01, ADOPT.02.platform (adoption) | End-to-end capability invocation with real security enforcement inside one product |

## Native producers and probes — [prompts](tasks/native.md)

| Task | Repository | Size | Start prerequisites | Title |
|---|---|---|---|---|
| NAT.01 | DesktopPlatform | M | PLT.18, PLT.09, PRF.04, ADOPT.02.native (adoption) | Probe A: device tool execution under Native AOT |
| NAT.02 | DesktopPlatform | M | PLT.01, ADOPT.02.native (adoption) | Probe B: block editor, store, undo and recovery |
| NAT.03 | DesktopPlatform | M | ADOPT.02.native (adoption) | Probe C: high-throughput acquisition over a real transport |
| NAT.04 | DesktopPlatform | L | PRF.01, ADOPT.02.native (adoption) | Probe D: native decode and audio/video synchronisation |
| NAT.05 | DesktopPlatform | S | NAT.01, NAT.02, NAT.03, NAT.04, ADOPT.02.native (adoption) | Probe evidence, licence positions, conclusions and hardware-lab inventory seed |
| NAT.06 | DesktopPlatform | L | ADOPT.02.native (adoption) | Common native ABI: preambles, pack8 records, ownership, cancellation, bounded buffers |
| NAT.07 | DesktopPlatform | L | NAT.06, ADOPT.02.native (adoption) | Media family: reader, probe, frame and seek (arc_media_reader_*) |
| NAT.08 | DesktopPlatform | M | NAT.06, ADOPT.02.native (adoption) | Media family: convert, resample and media writer |
| NAT.09 | DesktopPlatform | M | NAT.06, ADOPT.02.native (adoption) | Media family: audio devices (miniaudio) |
| NAT.10 | DesktopPlatform | M | NAT.06, ADOPT.02.native (adoption) | Colour family: OCIO transforms |
| NAT.11 | DesktopPlatform | M | NAT.06, PLT.45, ADOPT.02.native (adoption) | Image family: still-image codecs (PNG/TIFF/EXR) |
| NAT.12 | DesktopPlatform | L | NAT.06, ADOPT.02.native (adoption) | Otio family: OTIO0.18.1 interchange |
| NAT.13 | DesktopPlatform | M | NAT.06, ADOPT.02.native (adoption) | Instruments family: serial and USB devices (NEW library) |
| NAT.14 | DesktopPlatform | L | PLT.45, NAT.06, ADOPT.02.native (adoption) | Pdf family: PDFium and production parser containment in the WP11 helper (NEW library) |
| NAT.15 | DesktopPlatform | M | NAT.06, ADOPT.02.native (adoption) | Graphics family: portable CPU surface and optional OS backends (NEW library) |
| NAT.20 | DesktopPlatform | M | NAT.07, NAT.08, NAT.09, ADOPT.02.native (adoption) | Media package production: all 6 RIDs |
| NAT.21 | DesktopPlatform | S | NAT.10, ADOPT.02.native (adoption) | Colour package production: all 6 RIDs |
| NAT.22 | DesktopPlatform | S | NAT.11, ADOPT.02.native (adoption) | Image package production: all 6 RIDs |
| NAT.23 | DesktopPlatform | S | NAT.12, ADOPT.02.native (adoption) | Otio package production: all 6 RIDs |
| NAT.24 | DesktopPlatform | S | NAT.13, ADOPT.02.native (adoption) | Instruments package production: all 6 RIDs |
| NAT.25 | DesktopPlatform | M | NAT.14, PLT.45, ADOPT.02.native (adoption) | Pdf package production: all 6 RIDs + ContentSandbox Runtime.<rid> composition |
| NAT.26 | DesktopPlatform | S | NAT.15, ADOPT.02.native (adoption) | Graphics package production: all 6 RIDs |
| NAT.28 | DesktopPlatform | M | NAT.20, NAT.21, NAT.22, NAT.23, NAT.24, NAT.25, NAT.26, ADOPT.02.native (adoption) | Dependency adoption receipts and hardware-lab closure |
| NAT.29 | DesktopPlatform | M | PRF.01, PRF.02, PRF.03, PRF.04, PRF.05, PRF.06, PRF.07, PRF.08, PRF.09, PRF.10, ADOPT.02.native (adoption) | Verify the owned WP06 artifact set and real cross-runtime integration |
| NAT.30 | DesktopPlatform | M | NAT.06, NAT.07, NAT.08, NAT.09, NAT.10, NAT.11, NAT.12, NAT.13, NAT.14, NAT.15, NAT.20, NAT.21, NAT.22, NAT.23, NAT.24, NAT.25, NAT.26, NAT.28, NAT.01, NAT.02, NAT.03, NAT.04, NAT.05, PLT.54, ADOPT.02.native (adoption) | Verify the complete native producer set as one immutable candidate |

## Application composition — [prompts](tasks/app-composition.md)

| Task | Repository | Size | Start prerequisites | Title |
|---|---|---|---|---|
| APP.01 | DesktopPlatform | M | CON.02, PLT.17, FND.01, ADOPT.02.app-composition (adoption) | Assistant.Abstractions host ports and application identity |
| APP.02 | ArcNotes | M | APP.01, PLT.24, PLT.38, ADOPT.04.app-composition (adoption) | Minimal ArcNotes application services (read/create/append) |
| APP.03 | ArcNotes | S | APP.01, APP.02, PRF.04, NAT.01, ADOPT.04.app-composition (adoption) | Clean Native AOT package-consumer composition for ArcNotes |
| APP.04 | DesktopPlatform | S | APP.02, FND.02, FND.03, ADOPT.02.app-composition (adoption) | Idempotency and revision against the real store |
| APP.05 | DesktopPlatform | M | APP.01, PLT.39, ADOPT.02.app-composition (adoption) | Approval at the owner |
| APP.06 | DesktopPlatform | M | APP.01, PLT.21, PLT.22, PLT.41, ADOPT.02.app-composition (adoption) | Context and artifact integration |
| APP.07 | DesktopPlatform | S | APP.01, PLT.32, ADOPT.02.app-composition (adoption) | Independent lifecycle |
| APP.08 | DesktopPlatform | M | APP.01, APP.02, APP.03, APP.04, APP.05, APP.06, APP.07, ADOPT.02.app-composition (adoption) | Owned-artifact receipt and UX acceptance |

## Embedded assistant — [prompts](tasks/assistant.md)

| Task | Repository | Size | Start prerequisites | Title |
|---|---|---|---|---|
| AST.01 | DesktopPlatform | L | APP.01, CON.91, CON.11, ADOPT.02.assistant (adoption) | Single application history store (model 05 schema) |
| AST.02 | DesktopPlatform | M | AST.01, ADOPT.02.assistant (adoption) | Branches and window drafts |
| AST.03 | DesktopPlatform | M | AST.01, APP.06, ADOPT.02.assistant (adoption) | Attachments and provenance |
| AST.04 | DesktopPlatform | S | AST.01, ADOPT.02.assistant (adoption) | Projects and profiles |
| AST.05 | DesktopPlatform | S | AST.01, PLT.42, ADOPT.02.assistant (adoption) | Skills |
| AST.06 | DesktopPlatform | M | AST.01, ADOPT.02.assistant (adoption) | Local search |
| AST.07 | DesktopPlatform | M | AST.01, CON.11, ADOPT.02.assistant (adoption) | Local history export and import (assistant-history.v1) |
| AST.08 | DesktopPlatform | S | AST.01, ADOPT.02.assistant (adoption) | Reference and package proof (AionUi evidence, clean-app package consumption) |
| AST.09 | DesktopPlatform | M | AST.01, AST.02, AST.03, AST.04, AST.05, AST.06, AST.07, AST.08, ADOPT.02.assistant (adoption) | Owned-artifact receipt and UX acceptance |
| AST.10 | DesktopPlatform | L | EXE.01, AST.01, AST.02, AST.04, AST.05, AST.06, AST.07, ADOPT.02.assistant (adoption) | Complete assistant navigation shell |
| AST.11 | DesktopPlatform | L | CON.10, PRF.05, AST.01, ADOPT.02.assistant (adoption) | Cloud client and device runtime (fixture turn endpoint boundary) |
| AST.12 | DesktopPlatform | M | AST.10, APP.05, PLT.39, ADOPT.02.assistant (adoption) | Security and approval surface |
| AST.13 | DesktopPlatform | M | AST.10, EXE.01, EXE.05, AST.11, ADOPT.02.assistant (adoption) | Task centre |
| AST.14 | DesktopPlatform | M | AST.10, CON.10, ADOPT.02.assistant (adoption) | Automation client (automation fixture state transitions) |
| AST.15 | DesktopPlatform | M | AST.10, AST.07, ADOPT.02.assistant (adoption) | History and AI admission (local/cloud/temporary modes) |
| AST.16 | DesktopPlatform | M | AST.10, APP.06, ADOPT.02.assistant (adoption) | Preview and host context |
| AST.17 | DesktopPlatform | L | AST.10, AST.11, AST.12, AST.13, AST.14, AST.15, AST.16, ADOPT.02.assistant (adoption) | Complete package acceptance (Assistant.Avalonia/Core/Sqlite/Cloud) |
| AST.18 | DesktopPlatform | M | AST.17, ADOPT.02.assistant (adoption) | Owned-artifact receipt and real integration |
| AST.19 | DesktopPlatform | M | AST.11, HAR.00, HAR.03, ADOPT.02.assistant (adoption) | Real Cloud Harness turn loop replacing the fixture turn endpoint |
| AST.20 | DesktopPlatform | M | AST.14, HAR.06, ADOPT.02.assistant (adoption) | Real durable Cloud automation scheduler replacing the automation fixture |
| AST.21 | DesktopPlatform | M | AST.07, CLOUD.45, ADOPT.02.assistant (adoption) | Real Cloud Notes/Chat export producer replacing the local assistant-history.v1 fixture |
| AST.22 | DesktopPlatform | M | AST.15, CLOUD.46, AST.01, ADOPT.02.assistant (adoption) | Real Cloud application-history restartable import receiving promoted local history |

## Execution engine — [prompts](tasks/execution.md)

| Task | Repository | Size | Start prerequisites | Title |
|---|---|---|---|---|
| EXE.01 | DesktopPlatform | L | APP.01, FND.02, FND.03, PLT.17, ADOPT.02.execution (adoption) | Execution chain and its persistence (ProductJob engine core) |
| EXE.02 | DesktopPlatform | S | EXE.01, ADOPT.02.execution (adoption) | Lifecycle states and reason facets |
| EXE.03 | DesktopPlatform | M | EXE.01, ADOPT.02.execution (adoption) | Failure classification and retry |
| EXE.04 | DesktopPlatform | M | EXE.01, ADOPT.02.execution (adoption) | Child tasks and ownership |
| EXE.05 | DesktopPlatform | M | EXE.01, ADOPT.02.execution (adoption) | Checkpoints and compensation |
| EXE.06 | DesktopPlatform | M | EXE.01, PLT.39, ADOPT.02.execution (adoption) | Approval, steering and budget integration |
| EXE.07 | DesktopPlatform | M | EXE.01, ADOPT.02.execution (adoption) | Progress, outcome and trace |
| EXE.08 | DesktopPlatform | M | EXE.01, ADOPT.02.execution (adoption) | Concurrency, loops and storms |
| EXE.09 | DesktopPlatform | M | EXE.01, EXE.02, EXE.03, EXE.04, EXE.05, EXE.06, EXE.07, EXE.08, ADOPT.02.execution (adoption) | Owned-artifact receipt and real integration |

## Application presence and tool bridge — [prompts](tasks/device-bridge.md)

| Task | Repository | Size | Start prerequisites | Title |
|---|---|---|---|---|
| DEV.01 | Cloud | M | CLOUD.13, CLOUD.29, CON.11, ADOPT.07.device-bridge (adoption) | Application presence (ApplicationService List/Heartbeat/Disconnect) |
| DEV.02 | Cloud | M | DEV.01, CON.10, ADOPT.07.device-bridge (adoption) | Durable target queue |
| DEV.03 | DesktopPlatform | M | AST.11, APP.05, PLT.43, ADOPT.02.device-bridge (adoption) | Owner reauthorization (Device.Runtime local re-authorization) |
| DEV.04 | Cloud | M | DEV.02, CON.10, ADOPT.07.device-bridge (adoption) | Execution and result deduplication -- Cloud D1 attempt/result store |
| DEV.05 | DesktopPlatform | M | DEV.03, EXE.01, ADOPT.02.device-bridge (adoption) | Execution and result deduplication -- Desktop command_log agreement |
| DEV.06 | Cloud | M | DEV.02, DEV.03, PLT.39, ADOPT.07.device-bridge (adoption) | Remote approval and steering |
| DEV.07 | Cloud | S | DEV.02, ADOPT.07.device-bridge (adoption) | Offline expiry and recovery |
| DEV.08 | Cloud | S | DEV.02, ADOPT.07.device-bridge (adoption) | Frozen application locality |
| DEV.09 | Cloud | M | DEV.01, DEV.02, DEV.03, DEV.04, DEV.05, DEV.06, DEV.07, DEV.08, DEV.12, ADOPT.07.device-bridge (adoption) | Owned-artifact receipt and real integration |
| DEV.12 | Cloud | M | DEV.04, DEV.05, ADOPT.07.device-bridge (adoption) | Cross-repo (toolRequestId,attemptId,commandId) agreement between Cloud D1 and Desktop command_log |
| DEV.13 | Cloud | M | AST.19, HAR.02, DEV.02, DEV.03, DEV.04, DEV.05, DEV.06, DEV.12, ADOPT.07.device-bridge (adoption) | Real Harness-planned tool request flowing through the real device bridge end-to-end |
| DEV.14 | DesktopPlatform | M | CLOUD.29, CLOUD.30, CLOUD.31, CLOUD.33, CLOUD.34, AST.11, DEV.01, DEV.02, DEV.03, DEV.04, DEV.05, DEV.12, ADOPT.02.device-bridge (adoption) | Real device tool bridge over the deployed realtime transport |

## ArcNotes — [prompts](tasks/arcnotes.md)

| Task | Repository | Size | Start prerequisites | Title |
|---|---|---|---|---|
| NOTES.01 | ArcNotes | M | PLT.01, CON.91, ADOPT.04.arcnotes (adoption) | Notebook/folder hierarchy, document placement and structural commands |
| NOTES.02 | ArcNotes | XL | PLT.01, CON.91, CON.03, ADOPT.04.arcnotes (adoption) | Block/inline content model, EditTransaction engine, kind conversions and clipboard |
| NOTES.03 | ArcNotes | L | PLT.27, APP.01, PLT.26, ADOPT.04.arcnotes (adoption) | Editor interaction: caret, selection, IME composition, markdown-friendly input |
| NOTES.04 | ArcNotes | L | PLT.26, PLT.27, ADOPT.04.arcnotes (adoption) | Virtualised block layout, measurement caching and scroll anchoring |
| NOTES.05 | ArcNotes | L | PLT.27, ADOPT.04.arcnotes (adoption) | Rich content kinds: code highlighting, math rendering (notes.math.v1), table interaction |
| NOTES.06 | ArcNotes | M | NOTES.01, NOTES.02, ADOPT.04.arcnotes (adoption) | Links, backlinks and outline over the canonical block store |
| NOTES.07 | ArcNotes | M | NOTES.01, CON.91, ADOPT.04.arcnotes (adoption) | Document-level typed properties and tags (basic) |
| NOTES.08 | ArcNotes | M | PLT.05, NOTES.02, ADOPT.04.arcnotes (adoption) | Managed and external attachments (non-PDF): storage, availability, preview levels 1-2 |
| NOTES.09 | ArcNotes | L | PLT.45, NAT.06, ADOPT.04.arcnotes (adoption) | PDF in-product viewer, page anchors and native parser isolation |
| NOTES.10 | ArcNotes | L | NOTES.02, ADOPT.04.arcnotes (adoption) | Undo, history, checkpoint and trash as four distinct mechanisms |
| NOTES.11 | ArcNotes | M | PLT.02, PLT.03, PLT.04, ADOPT.04.arcnotes (adoption) | Crash recovery and upgrade/downgrade migration |
| NOTES.12 | ArcNotes | M | PLT.18, CON.91, ADOPT.04.arcnotes (adoption) | ArcNotes capability surface registration |
| NOTES.13 | ArcNotes | S | ADOPT.04.arcnotes (adoption) | ArcNotes reference-matrix drift check (AFFiNE/SiYuan) |
| NOTES.14 | ArcNotes | M | NOTES.01, NOTES.02, NOTES.03, NOTES.04, NOTES.05, NOTES.06, NOTES.07, NOTES.08, NOTES.09, NOTES.10, NOTES.11, NOTES.12, NOTES.13, ADOPT.04.arcnotes (adoption) | Owned-artifact and real-integration verification |
| NOTES.15 | ArcNotes | L | NOTES.02, PLT.07, ADOPT.04.arcnotes (adoption) | Local full-text index over hydrated content |
| NOTES.16 | ArcNotes | M | NOTES.15, NOTES.07, ADOPT.04.arcnotes (adoption) | Query, ranking and permission over the local index |
| NOTES.17 | ArcNotes | M | NOTES.15, ADOPT.04.arcnotes (adoption) | Citation anchors |
| NOTES.18 | ArcNotes | M | NOTES.16, NOTES.07, CON.91, ADOPT.04.arcnotes (adoption) | Saved views (list projection only) |
| NOTES.19 | ArcNotes | L | NOTES.01, NOTES.02, NOTES.06, ADOPT.04.arcnotes (adoption) | Non-destructive Markdown/plain-text import (incl. Obsidian-style folders) |
| NOTES.20 | ArcNotes | L | NOTES.01, CON.91, CON.20, ADOPT.04.arcnotes (adoption) | Cloud Notes export client and its named fixture endpoint |
| NOTES.21 | ArcNotes | S | GOV.03, ADOPT.04.arcnotes (adoption) | Repository-projection prohibition (structural assertion) |
| NOTES.22 | ArcNotes | M | NOTES.15, NOTES.16, NOTES.17, NOTES.18, NOTES.19, NOTES.20, NOTES.21, ADOPT.04.arcnotes (adoption) | Owned-artifact and real-integration verification |
| NOTES.23 | ArcNotes | M | NOTES.07, CON.91, ADOPT.04.arcnotes (adoption) | Typed property schemas: full bounded scalar set |
| NOTES.24 | ArcNotes | L | NOTES.23, NOTES.16, CON.91, ADOPT.04.arcnotes (adoption) | Query model: local evaluator and notes.scalar.v1 conformance fixtures |
| NOTES.26 | ArcNotes | L | NOTES.24, NOTES.18, ADOPT.04.arcnotes (adoption) | View kinds: list and table projections |
| NOTES.27 | ArcNotes | M | NOTES.26, NOTES.02, ADOPT.04.arcnotes (adoption) | Editing through a view |
| NOTES.28 | ArcNotes | S | NOTES.23, ADOPT.04.arcnotes (adoption) | Lightness preservation for plain notes |
| NOTES.29 | ArcNotes | M | NOTES.11, NOTES.23, NOTES.26, ADOPT.04.arcnotes (adoption) | Supported-schema migration for property/view data (local) |
| NOTES.30 | ArcNotes | S | NOTES.20, NOTES.23, NOTES.26, ADOPT.04.arcnotes (adoption) | Cloud export fidelity for property/view metadata |
| NOTES.31 | ArcNotes | M | NOTES.26, NOTES.04, ADOPT.04.arcnotes (adoption) | Scale: large collections, many properties, large result sets |
| NOTES.32 | ArcNotes | M | NOTES.23, NOTES.24, NOTES.26, NOTES.27, NOTES.28, NOTES.29, NOTES.31, ADOPT.04.arcnotes (adoption) | Owned-artifact and real-integration verification |
| NOTES.33 | ArcNotes | M | NOTES.20, NOTES.30, CLOUD.45, ADOPT.04.arcnotes (adoption) | Real Cloud Notes export join replaces the / fixture endpoint |
| NOTES.34 | ArcNotes | M | NOTES.24, CLOUD.37, ADOPT.04.arcnotes (adoption) | Cross-evaluator conformance of notes.scalar.v1 between the native cache and the real Cloud query evaluator |
| NOTES.35 | ArcNotes | M | NOTES.01, NOTES.02, NOTES.10, CLOUD.44, CLOUD.37, CLOUD.38, CLOUD.39, CLOUD.40, CLOUD.41, CLOUD.42, ADOPT.04.arcnotes (adoption) | ArcNotes participates in the three-device convergence harness |
| NOTES.37 | ArcNotes | M | PLT.45, NAT.14, NOTES.09, NAT.25, ADOPT.04.arcnotes (adoption) | ArcNotes PDF attachment viewer against the real ContentSandbox |

## ArcScope — [prompts](tasks/arcscope.md)

| Task | Repository | Size | Start prerequisites | Title |
|---|---|---|---|---|
| SCOPE.01 | ArcScope | M | PLT.01, CON.91, ADOPT.05.arcscope (adoption) | DataSource/SourceAdapter contract, connection profiles and lease/busy exclusivity |
| SCOPE.02 | ArcScope | M | CON.91, ADOPT.05.arcscope (adoption) | Channel, signal, event and time model |
| SCOPE.03 | ArcScope | M | SCOPE.01, ADOPT.05.arcscope (adoption) | Network and file-replay source adapters (TCP, UDP, file stream) |
| SCOPE.04 | ArcScope | M | SCOPE.01, NAT.13, ADOPT.05.arcscope (adoption) | Serial and USB instrument adapters |
| SCOPE.05 | ArcScope | L | SCOPE.01, SCOPE.02, SCOPE.03, ADOPT.05.arcscope (adoption) | Acquisition pipeline: bounded loop, ring buffer, backpressure and overrun accounting |
| SCOPE.06 | ArcScope | L | SCOPE.05, SCOPE.02, ADOPT.05.arcscope (adoption) | Session and capture lifecycle: segments, gaps and live observation |
| SCOPE.07 | ArcScope | L | SCOPE.06, PLT.06, ADOPT.05.arcscope (adoption) | Durable capture writer, chunked verifiable store and crash recovery |
| SCOPE.08 | ArcScope | M | SCOPE.07, SCOPE.01, ADOPT.05.arcscope (adoption) | Replay as a source (capture-level) |
| SCOPE.09 | ArcScope | S | SCOPE.06, PLT.32, ADOPT.05.arcscope (adoption) | Long-running capture in the shell |
| SCOPE.10 | ArcScope | S | ADOPT.05.arcscope (adoption) | Reference drift check against Serial-Studio 639daafb |
| SCOPE.11 | ArcScope | M | SCOPE.01, SCOPE.02, SCOPE.03, SCOPE.04, SCOPE.05, SCOPE.06, SCOPE.07, SCOPE.08, SCOPE.09, SCOPE.10, NAT.24, ADOPT.05.arcscope (adoption) | Owned-artifact verification and real hardware integration |
| SCOPE.12 | ArcScope | L | SCOPE.02, SCOPE.06, ADOPT.05.arcscope (adoption) | Visualisation: virtualised rendering, downsampling, cursors and markers |
| SCOPE.13 | ArcScope | M | SCOPE.05, SCOPE.06, ADOPT.05.arcscope (adoption) | Triggers with pre/post windows |
| SCOPE.14 | ArcScope | L | CON.91, SCOPE.02, SCOPE.06, ADOPT.05.arcscope (adoption) | Measurements: scope.measurement.v1 |
| SCOPE.15 | ArcScope | M | SCOPE.06, ADOPT.05.arcscope (adoption) | Decoder framework and first-party protocol decoders |
| SCOPE.16 | ArcScope | L | SCOPE.14, SCOPE.15, ADOPT.05.arcscope (adoption) | Analysis definitions and recipes as native ProductJobs |
| SCOPE.17 | ArcScope | M | SCOPE.06, ADOPT.05.arcscope (adoption) | Annotations, findings and session/capture comparison |
| SCOPE.18 | ArcScope | L | SCOPE.14, SCOPE.15, SCOPE.16, SCOPE.17, ADOPT.05.arcscope (adoption) | Reports and reproducibility |
| SCOPE.19 | ArcScope | M | SCOPE.12, SCOPE.13, SCOPE.14, SCOPE.15, SCOPE.16, SCOPE.17, SCOPE.18, ADOPT.05.arcscope (adoption) | Owned-artifact verification and real integration |
| SCOPE.20 | ArcScope | M | SCOPE.06, CON.02, ADOPT.05.arcscope (adoption) | ArcChat capability surface for ArcScope |
| SCOPE.21 | ArcScope | M | SCOPE.14, SCOPE.16, SCOPE.15, ADOPT.05.arcscope (adoption) | Bounded context provision for AI |
| SCOPE.22 | ArcScope | M | SCOPE.06, SCOPE.18, SCOPE.17, ADOPT.05.arcscope (adoption) | Cloud sync scope (metadata, not raw capture) |
| SCOPE.23 | ArcScope | M | SCOPE.07, CLOUD.42, ADOPT.05.arcscope (adoption) | Explicit per-session raw capture upload |
| SCOPE.24 | ArcScope | L | SCOPE.07, SCOPE.14, ADOPT.05.arcscope (adoption) | Import, export and format fixtures |
| SCOPE.25 | ArcScope | S | SCOPE.20, SCOPE.07, EXT.02, ADOPT.05.arcscope (adoption) | Extension boundary: no third-party raw-capture write path |
| SCOPE.26 | ArcScope | M | SCOPE.20, SCOPE.21, SCOPE.22, SCOPE.23, SCOPE.24, SCOPE.25, ADOPT.05.arcscope (adoption) | Owned-artifact verification and real integration |
| SCOPE.27 | ArcScope | M | SCOPE.22, CLOUD.39, CLOUD.44, ADOPT.05.arcscope (adoption) | Real ArcScope metadata sync against the deployed Cloud sync engine |

## ArcScope Cloud simulator — [prompts](tasks/simulator.md)

| Task | Repository | Size | Start prerequisites | Title |
|---|---|---|---|---|
| SIM.01 | Cloud | L | CLOUD.02, CON.21, ADOPT.07.simulator (adoption) | Simulation definitions, immutable scenario versions and bounded AST evaluator |
| SIM.02 | Cloud | L | SIM.01, ADOPT.07.simulator (adoption) | Deterministic generators, seeded RNG and fault profiles (algorithmic determinism) |
| SIM.03 | Cloud | XL | SIM.02, CLOUD.05, CLOUD.06, CLOUD.07, ADOPT.07.simulator (adoption) | Fenced slices and SimulationPacer (DO alarm coordinator, bounded Container segments, D1 checkpoint/fence) |
| SIM.04 | Cloud | L | SIM.03, CLOUD.42, CLOUD.04, COM.07, ADOPT.07.simulator (adoption) | Canonical publication, checkpoints and recovery |
| SIM.05 | Cloud | M | SIM.04, CLOUD.21, CLOUD.24, CON.21, ADOPT.07.simulator (adoption) | Cloud-side simulation.* operations, manifest listing and segment fetch |
| SIM.06 | ArcScope | L | SIM.05, CON.21, SCOPE.01, SCOPE.14, SCOPE.24, ADOPT.05.simulator (adoption) | ArcScope-side simulated DataSource and native ingestion |
| SIM.07 | Cloud | L | SIM.03, COM.05, COM.07, COM.12, POL.03, ADOPT.07.simulator (adoption) | Limits, entitlement and lifecycle |
| SIM.08 | Cloud | M | SIM.01, SIM.02, SIM.03, SIM.04, SIM.05, SIM.06, SIM.07, ADOPT.07.simulator (adoption) | Owned-artifact verification and real integration |
| SIM.09 | Cloud | M | SIM.05, SIM.06, SCOPE.14, SCOPE.18, SCOPE.24, ADOPT.07.simulator (adoption) | Real Cloud->R2->ArcScope-native simulator closure: hash/timebase/provenance proof against WP34 measurement/report and WP35 import/portability |
| SIM.10 | Cloud | M | CLOUD.07, SIM.01, ADOPT.07.simulator (adoption) | Real ArcScope simulator admission against deployed capacity/SimulationPacer |

## ArcSlate — [prompts](tasks/arcslate.md)

| Task | Repository | Size | Start prerequisites | Title |
|---|---|---|---|---|
| SLATE.01 | ArcSlate | M | ADOPT.06.arcslate (adoption) | Exact time model: canonical ticks, rational rates, frame/sample time, half-open ranges |
| SLATE.02 | ArcSlate | M | SLATE.01, ADOPT.06.arcslate (adoption) | Project and sequence domain model |
| SLATE.03 | ArcSlate | M | SLATE.01, ADOPT.06.arcslate (adoption) | Media asset/stream/metadata domain model and content-based relink algorithm |
| SLATE.04 | ArcSlate | L | NAT.07, SLATE.03, ADOPT.06.arcslate (adoption) | Native media metadata/probe read adapter (real import path) |
| SLATE.05 | ArcSlate | M | SLATE.02, SLATE.03, ADOPT.06.arcslate (adoption) | Media library: bins, reference-in-place import, background analysis |
| SLATE.06 | ArcSlate | L | SLATE.02, SLATE.03, SLATE.01, ADOPT.06.arcslate (adoption) | Timeline structural model: tracks, items, clips, transitions, markers |
| SLATE.07 | ArcSlate | XL | SLATE.06, ADOPT.06.arcslate (adoption) | Edit command pipeline and placement operations |
| SLATE.08 | ArcSlate | L | SLATE.07, ADOPT.06.arcslate (adoption) | Relationship and retiming edit operations |
| SLATE.09 | ArcSlate | M | SLATE.07, ADOPT.06.arcslate (adoption) | Undo/redo stack and composite command grouping |
| SLATE.10 | ArcSlate | M | PLT.01, PLT.04, SLATE.02, SLATE.06, ADOPT.06.arcslate (adoption) | Project persistence and store infrastructure (V1 migration baseline) |
| SLATE.11 | ArcSlate | L | PLT.02, PLT.03, SLATE.09, SLATE.10, ADOPT.06.arcslate (adoption) | Project checkpoints, crash recovery and project-version migration |
| SLATE.12 | ArcSlate | L | SLATE.06, SLATE.08, CON.06, ADOPT.06.arcslate (adoption) | Slate.project.v1/graph.v1 wire projection: bins, generators, nesting, adjustment, title/subtitle, cycle rejection |
| SLATE.13 | ArcSlate | S | ADOPT.06.arcslate (adoption) | ArcSlate reference-coverage drift check (maintenance) |
| SLATE.14 | ArcSlate | S | SLATE.01, SLATE.11, SLATE.12, SLATE.13, SLATE.04, SLATE.05, ADOPT.06.arcslate (adoption) | Closure: owned-artifact and real-integration receipt |
| SLATE.15 | ArcSlate | L | NAT.06, NAT.07, NAT.08, SLATE.04, ADOPT.06.arcslate (adoption) | Native media boundary consumption (ArcSlate.Media wrapper and safety suite) |
| SLATE.16 | ArcSlate | L | SLATE.15, ADOPT.06.arcslate (adoption) | Decode and pooled buffers |
| SLATE.17 | ArcSlate | L | SLATE.16, SLATE.01, ADOPT.06.arcslate (adoption) | Playback engine, clock and scheduler |
| SLATE.18 | ArcSlate | L | SLATE.06, ADOPT.06.arcslate (adoption) | Processing graph and keyframe engine (pure evaluation) |
| SLATE.19 | ArcSlate | M | SLATE.18, SLATE.15, NAT.08, NAT.15, ADOPT.06.arcslate (adoption) | Native-backed processing nodes (convert, scale, transform, colour-adjustment execution) |
| SLATE.20 | ArcSlate | XL | SLATE.01, SLATE.18, SLATE.16, NAT.08, ADOPT.06.arcslate (adoption) | Audio processing chain and sample-accurate mixing |
| SLATE.21 | ArcSlate | L | SLATE.03, SLATE.16, NAT.08, NAT.11, PLT.07, ADOPT.06.arcslate (adoption) | Proxies and derived caches |
| SLATE.22 | ArcSlate | M | SLATE.17, NAT.15, PLT.27, PLT.28, ADOPT.06.arcslate (adoption) | Viewer: source and sequence, professional transport |
| SLATE.23 | ArcSlate | S | SLATE.15, SLATE.22, SLATE.18, SLATE.19, SLATE.20, SLATE.21, ADOPT.06.arcslate (adoption) | Closure: owned-artifact and real-integration receipt |
| SLATE.24 | ArcSlate | L | SLATE.18, SLATE.03, NAT.10, ADOPT.06.arcslate (adoption) | Colour management: input interpretation, working config, display/export transform separation |
| SLATE.25 | ArcSlate | M | SLATE.19, NAT.15, PLT.27, ADOPT.06.arcslate (adoption) | Video scopes (waveform, vectorscope, histogram, parade) |
| SLATE.26 | ArcSlate | M | SLATE.06, SLATE.09, SLATE.10, ADOPT.06.arcslate (adoption) | Render planning and immutable snapshot binding |
| SLATE.27 | ArcSlate | M | SLATE.24, NAT.08, ADOPT.06.arcslate (adoption) | Export presets and encoding validation |
| SLATE.28 | ArcSlate | XL | SLATE.26, SLATE.27, SLATE.19, SLATE.20, NAT.08, EXE.01, ADOPT.06.arcslate (adoption) | Render execution engine and atomic export (native Product Job) |
| SLATE.29 | ArcSlate | M | SLATE.06, SLATE.01, ADOPT.06.arcslate (adoption) | Subtitles and captions: authored tracks, SRT/WebVTT import/export |
| SLATE.30 | ArcSlate | L | SLATE.29, SLATE.16, EXE.01, ADOPT.06.arcslate (adoption) | Local transcription extraction ProductJob and TranscriptRecord adoption |
| SLATE.31 | ArcSlate | M | SLATE.28, SLATE.27, ADOPT.06.arcslate (adoption) | Golden output stability corpus |
| SLATE.32 | ArcSlate | S | SLATE.24, SLATE.31, HAR.91, SLATE.25, SLATE.29, SLATE.30, ADOPT.06.arcslate (adoption) | Closure: owned-artifact and real-integration receipt |
| SLATE.33 | ArcSlate | L | SLATE.07, SLATE.08, SLATE.28, ADOPT.06.arcslate (adoption) | Capability surface: query, edit, render and export capabilities |
| SLATE.34 | ArcSlate | M | SLATE.06, ADOPT.06.arcslate (adoption) | Bounded context provision |
| SLATE.35 | ArcSlate | L | SLATE.04, SLATE.05, PLT.06, ADOPT.06.arcslate (adoption) | Collect, consolidate and the portable project package |
| SLATE.36 | ArcSlate | M | SLATE.03, SLATE.04, SLATE.05, ADOPT.06.arcslate (adoption) | Cross-device resolution and relink |
| SLATE.37 | ArcSlate | M | SLATE.10, CON.09, ADOPT.06.arcslate (adoption) | Cloud sync scope declaration |
| SLATE.38 | ArcSlate | L | SLATE.06, SLATE.01, NAT.06, NAT.12, ADOPT.06.arcslate (adoption) | OTIO interchange: import |
| SLATE.39 | ArcSlate | M | SLATE.38, SLATE.26, NAT.12, ADOPT.06.arcslate (adoption) | OTIO interchange: export |
| SLATE.40 | ArcSlate | S | SLATE.33, SLATE.39, SLATE.34, SLATE.36, ADOPT.06.arcslate (adoption) | Closure: owned-artifact and real-integration receipt |
| SLATE.42 | ArcSlate | M | SLATE.37, CLOUD.39, CLOUD.44, SLATE.12, SLATE.35, ADOPT.06.arcslate (adoption) | Real multi-device ArcSlate project convergence against the deployed Cloud sync engine |

## Cloud core — [prompts](tasks/cloud.md)

| Task | Repository | Size | Start prerequisites | Title |
|---|---|---|---|---|
| CLOUD.01 | Cloud | M | CON.91, ADOPT.07.cloud (adoption) | Ingress and host pipeline |
| CLOUD.02 | Cloud | M | CLOUD.01, ADOPT.07.cloud (adoption) | Twenty-one module boundaries and D1 named-plan bridge |
| CLOUD.03 | Cloud | L | CLOUD.02, ADOPT.07.cloud (adoption) | D1 migration runner and exact physical mapping |
| CLOUD.04 | Cloud | M | CLOUD.02, CLOUD.03, ADOPT.07.cloud (adoption) | Receipts, outbox, inbox dedup and change archive |
| CLOUD.05 | Cloud | M | CLOUD.01, CLOUD.04, ADOPT.07.cloud (adoption) | Finite durable jobs (Cron/Queue/Workflow-woken endpoints) |
| CLOUD.06 | Cloud | M | CLOUD.02, ADOPT.07.cloud (adoption) | Shared atomic family guarded-batch engine |
| CLOUD.07 | Cloud | L | CLOUD.02, CLOUD.03, CLOUD.06, ADOPT.07.cloud (adoption) | Capacity, Container/D1 integration producer and harness |
| CLOUD.08 | Cloud | S | CLOUD.01, CLOUD.02, ADOPT.07.cloud (adoption) | Failure isolation and readiness surface |
| CLOUD.09 | Cloud | M | CLOUD.01, CLOUD.03, ADOPT.07.cloud (adoption) | Selfhost.v1 deployment profile |
| CLOUD.10 | Cloud | M | CLOUD.37, SIM.10, ADOPT.07.cloud (adoption) | Owned-artifact closure and launch-capacity.v1 acceptance |
| CLOUD.11 | Cloud | M | CLOUD.02, CLOUD.03, CLOUD.06, ADOPT.07.cloud (adoption) | Core identity model (realm, user, authIdentity, single-owner workspace) |
| CLOUD.12 | Cloud | L | CLOUD.11, ADOPT.07.cloud (adoption) | Native and browser authentication with real Postmark/SES mail delivery |
| CLOUD.13 | Cloud | M | CLOUD.11, CLOUD.06, ADOPT.07.cloud (adoption) | Device, installation, instance and session (four distinct concepts) |
| CLOUD.14 | Cloud | S | CLOUD.13, ADOPT.07.cloud (adoption) | Device trust and remote gating |
| CLOUD.15 | Cloud | M | CLOUD.12, CLOUD.13, ADOPT.07.cloud (adoption) | Step-up challenges for sensitive operations |
| CLOUD.16 | Cloud | M | CLOUD.11, ADOPT.07.cloud (adoption) | PAT and actor authorization |
| CLOUD.17 | Cloud | M | CLOUD.12, ADOPT.07.cloud (adoption) | Recovery, account states and deletion |
| CLOUD.18 | DesktopPlatform | M | CLOUD.12, PLT.40, ADOPT.02.cloud (adoption) | Independent native session integration (Platform client primitives) |
| CLOUD.19 | Cloud | L | CLOUD.01, CLOUD.11, CLOUD.13, ADOPT.07.cloud (adoption) | Browser cookie-session adapter and full account-surface closure |
| CLOUD.20 | Cloud | M | CON.07, CLOUD.11, CLOUD.66, ADOPT.07.cloud (adoption) | Owned-artifact closure and real integration |
| CLOUD.21 | Cloud | M | CON.91, CLOUD.13, ADOPT.07.cloud (adoption) | Public endpoint mapping and validation |
| CLOUD.22 | Cloud | M | CLOUD.21, ADOPT.07.cloud (adoption) | Typed protocol and error mapping |
| CLOUD.23 | Cloud | M | CLOUD.21, CON.91, ADOPT.07.cloud (adoption) | Typed queries and revision preconditions |
| CLOUD.24 | Cloud | M | CLOUD.21, ADOPT.07.cloud (adoption) | Idempotency and rate limiting |
| CLOUD.25 | Cloud | M | CLOUD.21, PRF.07, ADOPT.07.cloud (adoption) | Resource transport schema and future-owner boundary |
| CLOUD.26 | Cloud | L | CLOUD.19, CLOUD.22, PRF.10, ADOPT.07.cloud (adoption) | Generated C#/TypeScript/Kotlin clients against Identity/Workspace/Device |
| CLOUD.27 | Cloud | M | CLOUD.26, ADOPT.07.cloud (adoption) | Compatibility window and bidirectional matrix |
| CLOUD.28 | Cloud | L | AND.07, WEB.30, ADOPT.07.cloud (adoption) | Owned-artifact closure and real integration |
| CLOUD.29 | Cloud | M | CLOUD.21, CLOUD.19, CON.11, ADOPT.07.cloud (adoption) | Stream connection and authentication (EventService.Watch/ExecutionService.WatchOutput shells) |
| CLOUD.30 | Cloud | M | CLOUD.29, ADOPT.07.cloud (adoption) | Scoped subscription (owner/product/filter/recovery-generation binding) |
| CLOUD.31 | Cloud | M | CLOUD.30, CLOUD.04, ADOPT.07.cloud (adoption) | Cursor and gap handling (DO projection backed by D1 outbox) |
| CLOUD.32 | Cloud | S | CLOUD.31, ADOPT.07.cloud (adoption) | Durable unary fallback (Poll/readOutput) |
| CLOUD.33 | Cloud | M | CLOUD.31, CLOUD.05, ADOPT.07.cloud (adoption) | Publication and wake (D1 outbox to bounded DO feed via Queues) |
| CLOUD.34 | Cloud | S | CLOUD.29, ADOPT.07.cloud (adoption) | Bounded stream lifecycle |
| CLOUD.35 | Cloud | M | CLOUD.33, CLOUD.34, ADOPT.07.cloud (adoption) | Reusable stream consumer adapters |
| CLOUD.36 | Cloud | M | DEV.14, ADOPT.07.cloud (adoption) | Owned-artifact closure and real integration (tool-result acceptance) |
| CLOUD.37 | Cloud | L | CLOUD.03, CLOUD.06, CON.91, CON.20, CON.03, CON.09, CLOUD.01, ADOPT.07.cloud (adoption) | Cloud Notes authority and sync scopes |
| CLOUD.38 | DesktopPlatform | L | PLT.01, ADOPT.02.cloud (adoption) | Client outbox and conflict lineage (desktop data model) |
| CLOUD.39 | Cloud | L | CLOUD.37, CLOUD.04, CLOUD.31, ADOPT.07.cloud (adoption) | Guarded publication and convergent bootstrap |
| CLOUD.40 | Cloud | M | CLOUD.38, CLOUD.39, ADOPT.07.cloud (adoption) | Conflict detection and five resolution policies |
| CLOUD.41 | Cloud | M | CLOUD.39, ADOPT.07.cloud (adoption) | Deletion and tombstones |
| CLOUD.42 | Cloud | L | CLOUD.01, CLOUD.06, CLOUD.25, ADOPT.07.cloud (adoption) | Blob lifecycle (real R2 staged/verified/committed) |
| CLOUD.43 | Cloud | L | CLOUD.42, CLOUD.39, ADOPT.07.cloud (adoption) | Availability, protection, data-health signals and realm-transfer workflow |
| CLOUD.44 | Cloud | L | ADOPT.07.cloud (adoption) | Multi-device convergence harness |
| CLOUD.45 | Cloud | L | CLOUD.37, CLOUD.42, CLOUD.05, CON.20, CON.22, ADOPT.07.cloud (adoption) | Real Cloud Notes and Chat export producers |
| CLOUD.46 | Cloud | M | CLOUD.42, CLOUD.06, ADOPT.07.cloud (adoption) | Application Cloud history and restartable import |
| CLOUD.47 | Cloud | M | AST.21, AST.22, CLOUD.58, NOTES.33, NOTES.35, ADOPT.07.cloud (adoption) | Owned-artifact closure and real integration |
| CLOUD.48 | Cloud | L | CLOUD.03, CLOUD.42, ADOPT.07.cloud (adoption) | D1 and independent object backup |
| CLOUD.49 | Cloud | M | CLOUD.48, ADOPT.07.cloud (adoption) | Point-in-time and fresh restore |
| CLOUD.50 | Cloud | M | CLOUD.49, CLOUD.17, ADOPT.07.cloud (adoption) | Fresh environment rebuild |
| CLOUD.51 | Cloud | M | CLOUD.50, ADOPT.07.cloud (adoption) | Disaster-recovery drill programme |
| CLOUD.52 | Cloud | S | CLOUD.48, ADOPT.07.cloud (adoption) | Data health read projection |
| CLOUD.53 | Cloud | M | CLOUD.48, ADOPT.07.cloud (adoption) | Export and realm migration |
| CLOUD.54 | Cloud | S | CLOUD.48, ADOPT.07.cloud (adoption) | Backup release gate |
| CLOUD.55 | Cloud | M | ADOPT.07.cloud (adoption) | Owned-artifact closure and real integration |
| CLOUD.58 | Cloud | M | CLOUD.45, NOTES.33, AST.21, ADOPT.07.cloud (adoption) | Structural removal of the Notes/Chat export runtime fixtures |
| CLOUD.63 | Cloud | M | CLOUD.06, CLOUD.16, COM.09, ADOPT.07.cloud (adoption) | Real Commerce/Entitlement participation in the shared atomic family engine |
| CLOUD.64 | Cloud | M | COM.13, POL.05, OPS.05, CLOUD.21, CLOUD.22, ADOPT.07.cloud (adoption) | Full operator contract closure across PublicApi, Commerce, Policy and Console |
| CLOUD.66 | Cloud | M | CLOUD.15, COM.10, CLOUD.21, CLOUD.22, ADOPT.07.cloud (adoption) | Every enumerated sensitive operation wired to the step-up mechanism |
| CLOUD.67 | Cloud | M | CLOUD.51, HAR.00, HAR.02, HAR.03, AIR.00, ADOPT.07.cloud (adoption) | Combined AI reopen after Cloud disaster-recovery restore |

## Commerce, entitlement and credits — [prompts](tasks/commerce.md)

| Task | Repository | Size | Start prerequisites | Title |
|---|---|---|---|---|
| COM.01 | Cloud | S | ADOPT.07.commerce (adoption) | Provider adapter boundary |
| COM.02 | Cloud | M | ADOPT.07.commerce (adoption) | Catalogue and versioned policy |
| COM.03 | Cloud | L | COM.01, COM.02, CLOUD.24, ADOPT.07.commerce (adoption) | Purchase pipeline |
| COM.04 | Cloud | L | COM.01, COM.03, ADOPT.07.commerce (adoption) | Provider event inbox |
| COM.05 | Cloud | L | ADOPT.07.commerce (adoption) | Entitlement resolver |
| COM.06 | Cloud | M | COM.05, CLOUD.23, ADOPT.07.commerce (adoption) | Distribution and enforcement |
| COM.07 | Cloud | L | CLOUD.07, COM.05, ADOPT.07.commerce (adoption) | Quota, usage and storage accounting |
| COM.08 | Cloud | L | COM.05, ADOPT.07.commerce (adoption) | Credits |
| COM.09 | Cloud | L | COM.03, COM.04, ADOPT.07.commerce (adoption) | Ledgers and reconciliation |
| COM.10 | Cloud | M | COM.05, COM.09, ADOPT.07.commerce (adoption) | Refunds, disputes and evidence |
| COM.11 | Cloud | L | COM.03, COM.05, COM.04, ADOPT.07.commerce (adoption) | Service term interval model |
| COM.12 | Cloud | XL | COM.11, COM.08, ADOPT.07.commerce (adoption) | Replenishing capacity bucket, refill and admission |
| COM.13 | Cloud | L | CON.14, CLOUD.21, COM.05, COM.08, COM.10, ADOPT.07.commerce (adoption) | Operator financial-owner proposal/approval operations |
| COM.14 | Cloud | L | COM.12, COM.03, COM.04, COM.05, COM.09, COM.10, ADOPT.07.commerce (adoption) | Technical commerce closure and live-gate staging |
| COM.15 | Cloud | S | COM.14, COM.06, COM.07, ADOPT.07.commerce (adoption) | Owned-artifact receipt and closure |

## Dynamic policy and configuration — [prompts](tasks/policy.md)

| Task | Repository | Size | Start prerequisites | Title |
|---|---|---|---|---|
| POL.01 | Cloud | S | ADOPT.07.policy (adoption) | The four boundaries |
| POL.02 | Cloud | L | CON.12, POL.01, ADOPT.07.policy (adoption) | Schema-constrained configuration |
| POL.03 | Cloud | M | POL.02, ADOPT.07.policy (adoption) | Compiled hard limits |
| POL.04 | Cloud | L | POL.01, POL.02, COM.05, ADOPT.07.policy (adoption) | Features, flags and deterministic rollout |
| POL.05 | Cloud | M | POL.02, CON.14, ADOPT.07.policy (adoption) | Kill switches |
| POL.06 | Cloud | M | POL.02, ADOPT.07.policy (adoption) | Scoped resolution and explainability (server side) |
| POL.07 | Cloud | M | POL.02, ADOPT.07.policy (adoption) | Compatibility policy |
| POL.08 | Cloud | M | POL.02, ADOPT.07.policy (adoption) | Publication, staleness and last-known-good (server side) |
| POL.09 | DesktopPlatform | L | POL.04, CON.12, CON.22, ADOPT.02.policy (adoption) | Client-side policy resolution library (native/AOT) |
| POL.10 | Cloud | S | POL.09, POL.03, POL.05, POL.06, POL.07, ADOPT.07.policy (adoption) | Owned-artifact receipt |
| POL.11 | Cloud | M | POL.08, POL.09, ADOPT.07.policy (adoption) | First real publish-then-resolve round trip from Cloud Policy authority to the DesktopPlatform client library |

## Operations, support and trust and safety — [prompts](tasks/operations.md)

| Task | Repository | Size | Start prerequisites | Title |
|---|---|---|---|---|
| OPS.01 | Cloud | M | ADOPT.07.operations (adoption) | Service levels and alerting |
| OPS.02 | Cloud | M | OPS.01, ADOPT.07.operations (adoption) | Incident process |
| OPS.03 | Cloud | M | OPS.02, ADOPT.07.operations (adoption) | Runbooks and rehearsal |
| OPS.04 | Web | M | OPS.01, ADOPT.09.operations (adoption) | Status page |
| OPS.05 | Web | XL | CON.14, POL.05, ADOPT.09.operations (adoption) | Operator console and support access |
| OPS.06 | Cloud | M | OPS.05, ADOPT.07.operations (adoption) | Break-glass |
| OPS.07 | Cloud | M | OPS.05, CON.22, ADOPT.07.operations (adoption) | Support cases and in-product reporting |
| OPS.08 | Cloud | L | OPS.07, OPS.05, ADOPT.07.operations (adoption) | Trust and safety |
| OPS.09 | Cloud | M | CLOUD.12, OPS.02, ADOPT.07.operations (adoption) | Operational mail and provider drills |
| OPS.10 | Cloud | L | OPS.09, CON.22, ADOPT.07.operations (adoption) | Customer push delivery and registration lifecycle |
| OPS.11 | Web | M | EXT.06, CON.14, OPS.05, ADOPT.09.operations (adoption) | Package review and revocation console |
| OPS.12 | Cloud | S | OPS.11, AND.26, OPS.01, OPS.02, OPS.03, OPS.04, OPS.06, OPS.07, OPS.08, OPS.09, OPS.10, ADOPT.07.operations (adoption) | Owned-artifact receipt |
| OPS.13 | Web | M | COM.13, POL.05, OPS.05, CON.14, OPS.11, ADOPT.09.operations (adoption) | Operator console exercises real financial-owner and kill-switch RPCs end to end |

## Knowledge search and retrieval — [prompts](tasks/search.md)

| Task | Repository | Size | Start prerequisites | Title |
|---|---|---|---|---|
| SRCH.00 | Cloud | M | CON.10, CLOUD.37, ADOPT.07.search (adoption) | Source admission and registration for search |
| SRCH.01 | Cloud | L | SRCH.00, CON.10, ADOPT.07.search (adoption) | Scoped derived index production (D1 FTS + Vectorize) |
| SRCH.02 | Cloud | L | SRCH.01, ADOPT.07.search (adoption) | Hybrid retrieval, RRF fusion and budgets |
| SRCH.03 | Cloud | S | SRCH.02, CLOUD.11, ADOPT.07.search (adoption) | Current permission recheck at query time |
| SRCH.04 | Cloud | M | SRCH.03, ADOPT.07.search (adoption) | Evidence and citations |
| SRCH.05 | Cloud | M | SRCH.01, ADOPT.07.search (adoption) | Privacy partitioning and cache isolation |
| SRCH.06 | Cloud | M | AIR.00, POL.08, SRCH.01, SRCH.02, AIR.06, ADOPT.07.search (adoption) | Real Cloud query path (fixture-to-real swap) |
| SRCH.90 | Cloud | M | SRCH.06, SRCH.03, SRCH.04, SRCH.05, ADOPT.07.search (adoption) | Owned artifacts, real integration and index capacity acceptance |

## Extension platform and integrations — [prompts](tasks/extensions.md)

| Task | Repository | Size | Start prerequisites | Title |
|---|---|---|---|---|
| EXT.00 | DesktopPlatform | L | PLT.45, PLT.19, ADOPT.02.extensions (adoption) | Extension host process and supervision |
| EXT.01 | DesktopPlatform | M | EXT.00, ADOPT.02.extensions (adoption) | Handshake and protocol versioning |
| EXT.02 | Contracts | L | CON.05, ADOPT.03.extensions (adoption) | Dual capability boundary (typed layer + closed dynamic value model) |
| EXT.03 | DesktopPlatform | M | EXT.02, ADOPT.02.extensions (adoption) | Declarative UI and settings contribution |
| EXT.04 | Contracts | M | EXT.02, CON.16, ADOPT.03.extensions (adoption) | Package manifest/workflow/panel validators and lifecycle state machine |
| EXT.05 | DesktopPlatform | L | EXT.04, ADOPT.02.extensions (adoption) | Six contribution-kind runtime wiring |
| EXT.06 | Cloud | L | CLOUD.16, CLOUD.42, CON.16, ADOPT.07.extensions (adoption) | Cloud PackageCatalog producer |
| EXT.07 | DesktopPlatform | M | EXT.06, ADOPT.02.extensions (adoption) | Desktop and CLI catalog consumers |
| EXT.08 | Contracts | M | EXT.02, CLOUD.16, ADOPT.03.extensions (adoption) | Public SDK and CLI |
| EXT.09 | DesktopPlatform | M | EXT.00, ADOPT.02.extensions (adoption) | Local MCP stdio behind the owned connector child |
| EXT.10 | AI | M | CON.15, ADOPT.08.extensions (adoption) | Cloud MCP HTTP through the AI Worker adapter |
| EXT.90 | DesktopPlatform | M | EXT.00, EXT.01, EXT.02, EXT.03, EXT.04, EXT.05, EXT.06, EXT.07, EXT.08, EXT.09, EXT.10, ADOPT.02.extensions (adoption) | Verify owned artifact and real integration (extension platform) |

## Workers AI routing and metering — [prompts](tasks/ai-routing.md)

| Task | Repository | Size | Start prerequisites | Title |
|---|---|---|---|---|
| AIR.00 | AI | L | CON.10, POL.08, ADOPT.08.ai-routing (adoption) | Provider adapters and routing (Workers AI) |
| AIR.01 | Cloud | M | POL.02, ADOPT.07.ai-routing (adoption) | Tariffs and cost dimensions |
| AIR.02 | Cloud | L | COM.08, AIR.00, ADOPT.07.ai-routing (adoption) | Metering and settlement |
| AIR.03 | Cloud | M | AIR.00, ADOPT.07.ai-routing (adoption) | Selected supplier and realm routing (no BYOK) |
| AIR.04 | Cloud | M | AIR.02, ADOPT.07.ai-routing (adoption) | Provider interaction records, redaction and cost transparency |
| AIR.05 | AI | M | AIR.00, ADOPT.08.ai-routing (adoption) | Content-origin marking at the provider generation boundary |
| AIR.06 | Cloud | M | AIR.02, ADOPT.07.ai-routing (adoption) | Funding and uncertain-outcome proof |
| AIR.07 | AI | M | AIR.00, ADOPT.08.ai-routing (adoption) | Provider test-environment coverage |
| AIR.08 | AI | L | AIR.00, AIR.02, AST.15, ADOPT.08.ai-routing (adoption) | Real-provider metering evidence and stubbed-path removal |
| AIR.09 | AI | M | AIR.00, ADOPT.08.ai-routing (adoption) | ASR/Whisper capability closure and inference-late-outcome reconciliation |
| AIR.90 | Cloud | M | AIR.08, AIR.01, AIR.03, AIR.04, AIR.05, AIR.06, AIR.07, AIR.09, ADOPT.07.ai-routing (adoption) | Verify owned artifact and real integration (AI routing and metering) |

## Cloud Harness — [prompts](tasks/harness.md)

| Task | Repository | Size | Start prerequisites | Title |
|---|---|---|---|---|
| HAR.00 | AI | XL | CLOUD.01, CON.15, CON.10, CLOUD.05, ADOPT.08.harness (adoption) | Turn loop, tool batching and bounds (RunWorkflow core) |
| HAR.01 | AI | L | HAR.00, CON.11, ADOPT.08.harness (adoption) | Context assembly and compaction |
| HAR.02 | AI | L | HAR.00, CON.10, ADOPT.08.harness (adoption) | Approval, cancellation and crash recovery |
| HAR.03 | AI | L | HAR.00, AIR.05, ADOPT.08.harness (adoption) | Generated streaming and durable output |
| HAR.04 | Cloud | M | HAR.00, AIR.06, ADOPT.07.harness (adoption) | Provider failure and effect-certainty classification |
| HAR.05 | AI | XL | HAR.00, HAR.01, HAR.02, HAR.03, HAR.04, AST.11, DEV.08, AST.19, DEV.13, AND.24, WEB.27, AIR.00, NOTES.12, APP.03, ADOPT.08.harness (adoption) | Own-application execution proof and fixture turn-endpoint removal |
| HAR.06 | Cloud | L | HAR.00, HAR.04, COM.05, ADOPT.07.harness (adoption) | Durable Cloud automation, scheduling and automation-fixture removal |
| HAR.90 | AI | M | HAR.05, HAR.06, HAR.91, ADOPT.08.harness (adoption) | Verify owned artifact and real integration (Harness) |
| HAR.91 | AI | M | HAR.06, AIR.09, SLATE.30, AIR.08, ADOPT.08.harness (adoption) | Paid Slate transcription end-to-end adoption |

## Android companion — [prompts](tasks/android.md)

| Task | Repository | Size | Start prerequisites | Title |
|---|---|---|---|---|
| AND.01 | Mobile | M | PRF.10, ADOPT.10.android (adoption) | Android production identity and stable toolchain reconciliation |
| AND.02 | Mobile | L | AND.01, ADOPT.10.android (adoption) | Real Android module graph and AN01-AN25 route/state contracts |
| AND.03 | Mobile | L | AND.02, ADOPT.10.android (adoption) | Android runtime and OS adapters (Compose, Credential Manager, Keystore wrapper, WorkManager, FCM registration, SAF/MediaStore) |
| AND.04 | Mobile | M | AND.02, CON.07, CON.11, AND.01, ADOPT.10.android (adoption) | Published gRPC-Web contract consumption (Connect Kotlin client, binary framing, session/stream/retry adapters) |
| AND.05 | Mobile | L | AND.02, CON.11, ADOPT.10.android (adoption) | Room history, drafts, outbox and receipts |
| AND.06 | Mobile | M | AND.03, ADOPT.10.android (adoption) | Secure per-account lifecycle: Keystore encryption, no-backup policy, purge/quarantine, deep-link validation |
| AND.07 | Mobile | M | AND.03, AND.04, AND.05, AND.06, CLOUD.13, CLOUD.42, CLOUD.39, CLOUD.18, CLOUD.19, CLOUD.26, CLOUD.29, ADOPT.10.android (adoption) | Foundation integration evidence: real candidate against deployed 22/23/24/25 |
| AND.08 | Mobile | L | AND.03, AND.04, AND.05, AND.06, ADOPT.10.android (adoption) | Authentication, Home and workspace (AN01-AN06) |
| AND.09 | Mobile | L | AND.04, AND.05, ADOPT.10.android (adoption) | Conversations and context (AN07-AN10/15/16) |
| AND.10 | Mobile | L | AND.04, AND.05, ADOPT.10.android (adoption) | Tasks, approvals and automation (AN11-AN13/19/25) |
| AND.11 | Mobile | M | AND.04, AND.05, ADOPT.10.android (adoption) | Library and resources (AN14-AN18/22) |
| AND.12 | Mobile | M | CON.22, AND.03, AND.04, AND.06, ADOPT.10.android (adoption) | Presence, push, links and settings (AN20-AN24) |
| AND.13 | Mobile | L | AND.08, AND.09, AND.10, AND.11, AND.12, ADOPT.10.android (adoption) | Native interaction and recovery: full experience-02 device matrix |
| AND.14 | Mobile | S | AND.08, AND.09, AND.10, ADOPT.10.android (adoption) | Scope and licence enforcement audit |
| AND.15 | Mobile | M | AND.08, AND.09, AND.10, AND.11, AND.12, AND.13, AND.14, ADOPT.10.android (adoption) | Complete companion acceptance |
| AND.16 | Mobile | S | AND.15, ADOPT.10.android (adoption) | Signed Android release artifacts (AAB + direct APK) |
| AND.17 | Mobile | S | AND.16, ADOPT.10.android (adoption) | Release runtime inspection |
| AND.18 | Mobile | S | AND.16, ADOPT.10.android (adoption) | Dependency and source rights closure (final artifact) |
| AND.19 | Mobile | M | AND.08, AND.09, AND.10, AND.11, AND.12, ADOPT.10.android (adoption) | Consumption-only enforcement |
| AND.20 | Mobile | M | CON.16, ADOPT.10.android (adoption) | Play and direct-channel signed update client |
| AND.21 | Mobile | L | AND.16, ADOPT.10.android (adoption) | Physical device and recovery gates |
| AND.22 | Mobile | S | ADOPT.10.android (adoption) | Android scope statement |
| AND.23 | Mobile | M | AND.17, AND.18, AND.19, AND.20, AND.21, AND.22, ADOPT.10.android (adoption) | Distribution acceptance |
| AND.24 | Mobile | M | AND.09, AND.10, HAR.00, HAR.03, ADOPT.10.android (adoption) | Real CF Harness generation/tool loop observed end to end on Android |
| AND.25 | Mobile | M | AND.10, AND.13, DEV.02, DEV.03, DEV.06, DEV.07, DEV.12, ADOPT.10.android (adoption) | Real desktop tool dispatch and unknown-effect reconciliation from Android |
| AND.26 | Mobile | M | AND.12, AND.23, OPS.10, AND.21, ADOPT.10.android (adoption) | Real FCM sending and physical Android receipt |

## Web — [prompts](tasks/web.md)

| Task | Repository | Size | Start prerequisites | Title |
|---|---|---|---|---|
| WEB.01 | Web | L | GOV.03, ADOPT.09.web (adoption) | React static generation and determinism engine |
| WEB.02 | Web | M | WEB.01, ADOPT.09.web (adoption) | Versioned public content and pricing inputs (catalogue.json) |
| WEB.03 | Web | M | WEB.01, ADOPT.09.web (adoption) | Rendering and performance |
| WEB.04 | Web | M | WEB.01, ADOPT.09.web (adoption) | Internationalisation |
| WEB.05 | Web | M | WEB.01, ADOPT.09.web (adoption) | Documentation, downloads and legal surfaces |
| WEB.06 | Web | S | WEB.01, ADOPT.09.web (adoption) | Accessibility and analytics |
| WEB.07 | Web | S | WEB.01, ADOPT.09.web (adoption) | Independence and atomic deployment |
| WEB.08 | Web | L | GOV.03, ADOPT.09.web (adoption) | Owned consumer design system (packages/ui) |
| WEB.09 | Web | S | WEB.02, WEB.03, WEB.04, WEB.05, WEB.06, WEB.07, WEB.08, ADOPT.09.web (adoption) | Verify the owned Site artifact and real integration |
| WEB.10 | Web | XL | WEB.08, CON.07, ADOPT.09.web (adoption) | Account shell: route graph, deployment-profile selection, generated-SDK wiring |
| WEB.11 | Web | L | CLOUD.19, WEB.10, ADOPT.09.web (adoption) | Real browser session and step-up acceptance |
| WEB.12 | Web | M | WEB.11, ADOPT.09.web (adoption) | Account and security surfaces |
| WEB.13 | Web | M | WEB.10, ADOPT.09.web (adoption) | Workspace, storage and usage |
| WEB.14 | Web | L | WEB.10, CON.08, ADOPT.09.web (adoption) | Subscription, capacity, credits and hosted checkout |
| WEB.15 | Web | M | WEB.10, CON.22, ADOPT.09.web (adoption) | Data export and deletion |
| WEB.16 | Web | M | WEB.10, ADOPT.09.web (adoption) | Origin security and performance (account) |
| WEB.17 | Web | M | WEB.12, WEB.13, WEB.14, WEB.15, ADOPT.09.web (adoption) | Offline, degradation and accessibility (account) |
| WEB.18 | Web | M | WEB.11, WEB.12, WEB.13, WEB.14, WEB.15, WEB.16, WEB.17, WEB.29, ADOPT.09.web (adoption) | Verify the owned Account artifact and real integration |
| WEB.19 | Web | L | WEB.08, WEB.10, ADOPT.09.web (adoption) | Chat shell: route composition and design-system integration |
| WEB.20 | Web | L | WEB.19, ADOPT.09.web (adoption) | Conversation and generated output streams |
| WEB.21 | Web | L | WEB.19, ADOPT.09.web (adoption) | Tasks, approval and steering |
| WEB.22 | Web | M | WEB.19, ADOPT.09.web (adoption) | Artifacts and sandboxing |
| WEB.23 | Web | M | WEB.19, ADOPT.09.web (adoption) | One-application remote control |
| WEB.24 | Web | M | WEB.20, WEB.21, WEB.22, WEB.23, ADOPT.09.web (adoption) | Offline, degradation and accessibility (chat) |
| WEB.25 | Web | S | WEB.19, ADOPT.09.web (adoption) | Performance budgets (chat) |
| WEB.26 | Web | M | WEB.20, WEB.21, WEB.22, WEB.23, WEB.24, WEB.25, ADOPT.09.web (adoption) | Verify the owned Chat artifact and real integration |
| WEB.27 | Web | M | WEB.20, WEB.21, HAR.00, HAR.03, ADOPT.09.web (adoption) | Real CF Harness generation/tool loop observed end to end in the browser |
| WEB.28 | Web | M | WEB.21, WEB.23, DEV.02, DEV.03, DEV.06, DEV.07, DEV.12, ADOPT.09.web (adoption) | Real desktop tool dispatch from the browser companion |
| WEB.29 | Web | M | WEB.14, COM.14, POL.08, ADOPT.09.web (adoption) | Real commerce/policy provider evidence for the account portal |
| WEB.30 | Web | M | CLOUD.19, CLOUD.26, CLOUD.29, WEB.07, WEB.14, WEB.19, PRF.08, ADOPT.09.web (adoption) | Real React Web client against deployed browser session/PublicApi/realtime |
| WEB.31 | Web | M | OPS.05, WEB.07, WEB.14, WEB.19, WEB.30, ADOPT.09.web (adoption) | Full browser-support.v1 matrix across all Web-facing outputs |

## Desktop distribution and update — [prompts](tasks/updater.md)

| Task | Repository | Size | Start prerequisites | Title |
|---|---|---|---|---|
| UPD.01 | DesktopPlatform | M | PLT.40, FND.05, ADOPT.02.updater (adoption) | Signed feed and applicable-target selection |
| UPD.02 | DesktopPlatform | L | UPD.01, ADOPT.02.updater (adoption) | Background download and staging |
| UPD.03 | DesktopPlatform | L | UPD.02, PLT.32, ADOPT.02.updater (adoption) | Safe apply and atomic activation |
| UPD.04 | DesktopPlatform | L | UPD.03, PLT.04, ADOPT.02.updater (adoption) | Rollback and migration interlock |
| UPD.05 | DesktopPlatform | M | UPD.01, ADOPT.02.updater (adoption) | Channels, staged rollout and security updates |
| UPD.06 | DesktopPlatform | S | PLT.47, FND.05, ADOPT.02.updater (adoption) | Diagnostics and preserving data on uninstall |
| UPD.07 | DesktopPlatform | M | UPD.01, CON.16, ADOPT.02.updater (adoption) | Production catalog and Android distribution trust |
| UPD.08 | DesktopPlatform | M | UPD.01, UPD.02, UPD.03, UPD.04, UPD.05, UPD.06, UPD.07, PRF.01, POL.09, ADOPT.02.updater (adoption) | Publish ArcForges.Update and verify the complete lifecycle |

## Release readiness and family release — [prompts](tasks/release.md)

| Task | Repository | Size | Start prerequisites | Title |
|---|---|---|---|---|
| REL.01 | ArcNotes | L | NOTES.32, UPD.08, NOTES.14, NOTES.22, ADOPT.04.release (adoption) | ArcNotes desktop release readiness |
| REL.02 | ArcScope | L | SCOPE.26, UPD.08, SCOPE.11, SCOPE.19, ADOPT.05.release (adoption) | ArcScope desktop release readiness |
| REL.03 | ArcSlate | L | SLATE.40, UPD.08, SLATE.14, SLATE.23, SLATE.32, ADOPT.06.release (adoption) | ArcSlate desktop release readiness |
| REL.04 | Mobile | M | AND.23, ADOPT.10.release (adoption) | Android release readiness |
| REL.05 | Web | L | WEB.26, WEB.09, WEB.18, ADOPT.09.release (adoption) | Web outputs release readiness |
| REL.06 | Cloud | XL | CLOUD.51, AIR.90, GOV.03, CLOUD.10, CLOUD.20, CLOUD.28, CLOUD.36, CLOUD.47, CLOUD.55, COM.15, POL.10, OPS.12, SRCH.90, EXT.90, HAR.90, SIM.08, ADOPT.07.release (adoption) | Cloud/AI production readiness (deployment, migration, backup, self-host) |
| REL.07 | Contracts | M | REL.01, REL.02, REL.03, REL.04, REL.05, REL.06, REL.08, ADOPT.03.release (adoption) | Contracts/SDK release audit (licence, SBOM, provenance rollup) |
| REL.08 | Cloud | L | COM.15, POL.10, ADOPT.07.release (adoption) | Commercial activation |
| REL.09 | Cloud | L | REL.06, OPS.12, ADOPT.07.release (adoption) | Combined disaster drill and operational readiness confirmation |
| REL.10 | DesktopPlatform | M | REL.01, REL.02, REL.03, UPD.01, UPD.07, ADOPT.02.release (adoption) | Production update feed and signing switch |
| REL.11 | DesktopPlatform | L | REL.01, REL.02, REL.03, REL.04, REL.05, REL.06, REL.07, REL.08, REL.09, REL.10, ADOPT.02.release (adoption) | Family release readiness audit and honest statement |
