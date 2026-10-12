ARCFORGES PARALLEL DELIVERY LAUNCHER


=== SCOPE BEGIN ===

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

=== SCOPE END ===

1. SCOPE
- The scope is every task or slice ID in the first column of a table row in SCOPE, plus any ID standing alone on a line.
- Ignore headings, header rows, prerequisite columns and all other text.
- Derive this ID list once and pass it to every subagent.
- Apply the scope filter only to delivery task and slice selection. Keep relevant integration roles, resource leases and build-slot status visible, and allow claiming and managing those required for in-scope work.
- Report any ID that T show rejects; never guess. No delivery task or adoption slice outside the list is claimed or executed.

2. AUTHORITY AND STATE
- This launcher authorizes executing the scope to completion. Routine decisions and authorized merges need no renewed approval. Later user instructions override the launcher.
- WP03.02 is only the historical baseline. Current progress comes solely from:
  - the authoritative state T reads (merged Design-B and Plan-B main, plus the claims/*, leases/* and roles/* branches);
  - pull requests;
  - the ledger.
  It never comes from documents, this launcher or unmerged work.
- Run one coordinator per scope at a time. The coordinator keeps no state of its own. Pasting this launcher again after the previous coordinator has ended resumes the batch from T status.

3. TOOL TARGETING (every session)
- T = python C:\MyFile\Projects\Plan-B\tools\delivery.py, the copy in the Plan-B primary checkout. Whatever the current directory:
  - its default --plan is that primary checkout;
  - its default --design is the primary C:\MyFile\Projects\ArcForges-Design-B (or $ARCFORGES_DESIGN).
- Commands that use no working tree may keep the defaults: ready, status, show, claim, update, release and build-slot. They work only on the remote record branches and the workstation lock.
- The coordinator keeps both primary checkouts clean and fast-forwarded, so that T is current.
- check and generate read or write working trees, so always name both roots:
    T generate --plan <Plan worktree> --design <Design worktree>
    T check --plan <Plan worktree> --design <Design worktree>
- For a ledger-only Plan change, --design may be the Design primary at current main, because check only reads.
- Before merging a Plan PR, the integration owner runs that check in its own retained Plan worktree, on the reviewed head merged uncommitted onto current main.
- A change to tools\delivery.py itself runs its own worktree copy of the tool, with the same explicit roots.
- Never run generate against a primary checkout, and never edit a primary checkout.
- This makes explicit the procedure's instruction to "run check and generate from a Plan worktree".

4. READING (in proportion to responsibility)
- Coordinator reads:
  - the SCOPE;
  - Plan-B arcforges-implementation.md, execution-policy.md and single-task-command.md;
  - Design docs\planning\delivery\README.md sections 5 and 6 (DLV-22 to DLV-42).
  It does not read task prompts, list.md, lane files or source.
- Every subagent reads arcforges-implementation.md and execution-policy.md (its entry prompt requires both), plus the launcher sections it is given.
- Worker, for each claimed item:
  - only that item's prompt block (search C:\MyFile\Projects\Plan-B\tasks\*.md for the ID);
  - its task record and the obligations it links;
  - the published outputs of its prerequisites;
  - the AGENTS.md of each repository it edits;
  - for ADOPT items, also Design docs\planning\delivery\adoption.md.
- Reviewer, for each PR: the diff, the item's prompt block and task record, and the obligations, rules and repository instructions the diff touches.
- Integration owner, for each repository:
  - its AGENTS.md and retained CI;
  - the shared-resource protocols that name the repository (Design docs\planning\delivery\shared-resources.md);
  - for Plan, also ledger\README.md.
- No subagent reads list.md or whole lane files.

5. COORDINATOR LOOP
a. Run T status and T ready --json. Select delivery tasks and slices only from the scope ID list, while retaining relevant integration-role, resource-lease and build-slot state. ready never lists accepted, complete, inherited or superseded items.
b. Run at most 10 background general-purpose subagents at once, fewer when the runtime allows fewer. Launch them without runtime worktree isolation; they create their own retained worktrees.
   Allocate by current demand, with no fixed quotas and no waves:
   - workers for claimable scope items (ready, completion follow-ups, released or resumable);
   - reviewers for PRs awaiting review;
   - an integration owner for each repository with approved PRs waiting (one session may hold several roles).
   Start a subagent as soon as there is work for it, and never one with nothing to do. Only real prerequisites and resource locks (leases, roles, the build slot) order the work.
c. Name each subagent w-<host>-<yyyymmdd>-<token>-<n>. Choose <token> at random, once per coordinator. No two live sessions share a name.
d. Build each prompt:
   - start from the matching entry prompt in single-task-command.md (Worker, Resume or Integration owner), or from section 7 for a reviewer;
   - fill in the name and the scope ID list;
   - append sections 3, 4, 6 and 9 verbatim, and section 8 as well when the scope contains ADOPT IDs.
e. When a subagent returns, read its report and T status.
   - Resume its live claims, leases and roles under the same name with the Resume prompt: at once if it returned for lack of context, otherwise as soon as they need action.
   - Check its PRs with gh pr view, and resume it when a PR has an approval, findings or a merge.
   - After a coordinator restart, resume the previous batch's names the same way.
   - Take over other workers' claims only under the procedure's recovery rules.
f. Re-check T status and ready:
   - whenever a subagent returns;
   - every few minutes while capacity is free and merges are pending;
   - otherwise about every 15 minutes.
   Never poll in a tight loop.
g. Stop when no subagent holds unfinished work and every scope ID is one of:
   - complete, inherited or superseded in the merged ledger;
   - accepted baseline ("Baseline: accepted" in its prompt block);
   - blocked with a concrete recorded blocker;
   - waiting only on prerequisites outside the scope (per T show).
   First, have a worker correct any active guidance the batch made stale, in one reviewed [P2-018] Plan PR. After adoption this includes the Plan-B AGENTS.md sentence "The adoption stage is defined but has not been executed". Then give the section 10 report.

6. SUBAGENT RULES
These are additions to arcforges-implementation.md, which governs claiming, handoff, execution, review, merge, completion, follow-ups, recovery, leases and the build slot.
- Scope and order:
  - Execute only scope tasks and slices, in the procedure's selection order.
  - Keep relevant integration-role, resource-lease and build-slot state visible; claim and manage the roles and leases required for in-scope work.
  - Take an item as soon as ready lists it. No table order, section boundary or unrelated item is a barrier.
  - Execute in-scope prerequisites as they become ready.
  - Report an unmet out-of-scope or external prerequisite (DLV-12) with T show output, and never execute it.
- Planning: research each item in proportion to it, then plan it completely before editing it. There is no global research phase.
- Conventions:
  - Commit messages end with "Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>".
  - PR bodies end with "🤖 Generated with [Claude Code](https://claude.com/claude-code)".
  - Create PRs with gh pr create --body-file <file>.
  - Review comments use the procedure's format followed by "(reviewer <name>)", because every session posts from the same GitHub account.
- Waiting and returning:
  - Your own live claims count as available work. While they await review, CI or merge, take other available work or check them sparingly.
  - Return only when nothing in scope is available to you, or when your context runs low.
  - Before returning, push, then record update --done/--next (or release with a handoff note).
  - Then report your name and, for each ID: epoch, state, PRs, head, reviewed and merge SHAs, next actions, validation performed and blockers.
- Lock errors:
  - A git error naming a local lock file ("...lock': File exists", "cannot lock ref") comes from concurrent local commands, not the network, even when T exits with code 3.
  - Wait for the other command, then repeat once.
  - Every other failed network operation follows section 9.

7. REVIEWER PROMPT
Act as ArcForges reviewer <name> for the scope IDs given. Repeatedly take in-scope PRs whose claim record lists "await review" (T status --json). Review the complete diff at one head against the item's prompt block and task record, the applicable DLV and ADP rules, and section 9. Post either the approval comment (one line per ID in a bundle) or concrete findings. Review each new head again. Never edit, claim or merge. Return a report when nothing awaits review.

8. ADOPT ITEMS (only for IDs beginning "ADOPT.")
- Slices and repository records review each product repository at the head frozen in ledger/adoption/baseline.md, and never edit a product repository.
- An item whose write scope includes its own ledger record (slices, and ADOPT.02 to ADOPT.10) adds that record in its own PR. There is no separate ledger PR.
- Roles (adoption.md section 2):
  - The workers you start are the assigned adoption reviewers of the slices they claim.
  - ADOPT.02 to ADOPT.10, and their follow-ups, belong to the repository's integration owner. Claim the vacant integration:<Repository> role before the item, and release it with a note afterwards.
  - If another session holds that role, leave the item to it.
- Conflicts and adjustments:
  - A task classified as conflicting is recorded in its slice row and raised under D-001 for a user decision. The slice still completes.
  - An adjustment that fits no existing task becomes a planning change, linked from the record. The record does not wait for it.

9. POLICY REMINDER (restates execution-policy.md and the user's standing rules; weakens nothing)
- CI:
  - No macOS job, runner or matrix: hosted, self-hosted, scheduled or manual.
  - No CI for physical devices, Android emulators, desktop GUI, browser E2E, live services, real AI inference, installed-package consumers or public-release install or upgrade.
  - Keep only necessary Windows/Linux compilation, Native AOT, packaging, static checks, targeted offline unit tests and non-duplicated security checks.
  - Never claim an unproduced macOS or platform result.
- Local validation:
  - Run local runtime or E2E tests only when the existing environment supports them and the change requires them. Test the affected behavior once; repeat only after a new change or for a concrete unresolved finding.
  - Never install or reinstall vcpkg, SDKs, emulators or toolchains to expand validation. Use existing tools and caches.
  - No Git hooks that build or test.
  - One CPU-heavy local build or test per workstation, through the build slot.
- Artifacts and publication:
  - No routine downloads of published packages, archives, images or website assets.
  - No repeated archive extraction, member comparison, hash recomputation or consumer reruns against the same candidate.
  - Keep lockfile integrity, required signing, provenance and licence checks, and one necessary publication-candidate identity check.
  - Anything more needs a concrete integrity or publication defect, or an explicit user request.
  - Promote the original candidate, using provider receipts.
  - Never create tags, republish, re-sign or allocate replacement versions just to verify.
- Documentation and failures:
  - Documentation-only changes get review and document consistency checks, not product builds or runtime tests. Configured CI still runs.
  - Never rerun a failed job blindly: diagnose and fix its specific cause.
  - Keep AGENTS.md, authoritative design documents, workflow dependencies and release-asset expectations consistent with these rules.
  - Repair conflicting authoritative documentation before dependent work.
  - Record removed platform coverage honestly. Never claim tests or artifacts that no longer exist.
- Preservation:
  - Preserve product behavior, package and installation identities, signing continuity, immutable releases and unrelated work.
  - Fix concrete findings without repeatedly expanding scope.
- Network:
  - Use the normal network path only: no proxy 7890 and no network changes.
  - On a failed network operation, report the exact operation and stop without retrying.
  - The coordinator then starts nothing new, has running subagents stop after their current step, and reports.
  - Never invoke wsl.exe or WSL wrappers. If WSL is necessary, use a directly available WSL terminal.
- Review and merge:
  - Review every PR and fix its findings.
  - A repository without CI merges after review. Otherwise, merge only after every applicable CI check passes on the reviewed head, documentation-only changes included.
  - Never skip CI or weaken branch protection.
  - Post-merge verification is limited to three things: the expected merge commit, the required build, publication or deployment job result, and a clean fast-forward of the primary checkout. Start no further download, hash-audit, installation or runtime-test cycle.
- Repositories and credentials:
  - A Git worktree for every change. Keep branches and worktrees.
  - Work only in Plan-B, ArcForges-Design-B and the nine repositories under C:\MyFile\Projects\ArcForges.
  - Never print or commit credentials.
- Reporting: report verified results and material untested coverage accurately. Deployment success is not a live test, and compilation is not device or commercial acceptance.

10. FINAL REPORT (coordinator)
- Completed: each ID with its final ledger status, and its PRs with their reviewed heads and merge commits.
- Blocked or unfinished: each ID with its concrete blocker or unmet prerequisite, its holder and its next action.
- CI, publication and deployment job outcomes required and observed, plus required jobs that did not run.
- Remaining acceptance: delivered items awaiting completion prerequisites, D-001 conflicts awaiting a decision, and open planning changes.
- For ADOPT slices: the classification counts, and the tasks each slice opened.
- Material untested coverage.
