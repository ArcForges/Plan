# ArcForges delivery task prompts — Contracts schema closures

Generated from Design `docs/planning/delivery/delivery-graph.json` by `tools/delivery.py`; do not edit by hand.
Each block is self-contained. Claim a task only when `python tools/delivery.py ready` lists it, with
`python tools/delivery.py claim <TASK-ID> --worker <name>`, then follow `arcforges-implementation.md`.
Tasks are ordered by lane for reading; the order is not a schedule.

## Contracts schema closures

```text
Execute ArcForges delivery task CON.01 — Shard contended eng inventory/constraint files by domain; fix one-owner merge protocol.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\contracts.md (anchor task-con-01).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Contracts (integration owner: Contracts integration owner, the holder of roles/integration-contracts).
Claim and handoff record: claims/con-01 (python tools/delivery.py claim CON.01 --worker <name>); task branch task/con-01 in Contracts; ledger record ledger/tasks/con-01.md.
Kind/size: governance/S. Baseline: not-started.
Outcome: public/proto/constraints.json and internal/proto/constraints.json are split into small per-domain shard files (mirroring the already-proven fixtures/public/wp03-NN.json pattern) merged by eng/contracts.py; eng/contract-packages.json and eng/foundation-inventory.json gain a documented append protocol; a short CONTRIBUTING note fixes the single Contracts integration owner who serially merges CON.* branches.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- P2-018 (contention reduction that lets Contracts closures be authored concurrently): C:\MyFile\Projects\ArcForges-Design-B\docs\decisions\phase-2-specification-decisions.md, anchor rule-p2-018

Entry condition: adoption slice ADOPT.03.contracts is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- none
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Contracts:eng/contracts.py; Contracts:public/proto/constraints/**; Contracts:internal/proto/constraints/**; Contracts:CONTRIBUTING.md
Shared resources (follow the owner protocol): RES-contracts-generated-baseline (regenerate): Never hand-edited or hand-merged: after rebasing, the author regenerates with the pinned generator and commits the result; CI rejects drift between schemas, descriptors and generated output.; RES-contracts-publication (append): Every merge to main publishes all Contracts packages at one allocated candidate version (Maven main as SNAPSHOT under the publication-channel profile); the integration owner keeps a single merge queue so publications stay ordered; no tag, republication or replacement version is created for verification.; RES-contracts-schema-sources (append): Each closure task edits only its own domain proto or HTTP-schema files and adds its own sharded constraint and fixture files; shared inventories (package inventory, foundation inventory, constraint aggregate) are append-only per closure. A proto file with several contributing tasks (operator, policy/configuration) has one designated author task and the others request changes through it. The integration owner merges closure pull requests one at a time and the next author rebases and regenerates.
Unblocks: CON.19

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): offline: eng/contracts.py generate --check round-trips the sharded constraints back to the same effective merged content; existing eng/check_foundation.py and check_serialization.py pass unchanged.
Completion evidence for the ledger: eng/contracts.py generate --check clean; diff shows only file-layout change, zero constraint-content change.
Notes: Optional enabler: without it, closure pull requests edit the same constraint files and are merged one at a time with rebase-and-regenerate by the Contracts integration owner, which remains the fallback protocol.
```

```text
Execute ArcForges delivery task CON.02 — Capability/action/context/version/health descriptor records + immutable oversized-body reference (EncodedBodyRef).

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\contracts.md (anchor task-con-02).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Contracts (integration owner: Contracts integration owner, the holder of roles/integration-contracts).
Claim and handoff record: claims/con-02 (python tools/delivery.py claim CON.02 --worker <name>); task branch task/con-02 in Contracts; ledger record ledger/tasks/con-02.md.
Kind/size: contract/M. Baseline: not-started.
Outcome: CapabilityDescriptor, ActionDescriptor, ContextProvider/ContextDescriptor, CompatibilityDescriptor/ContractVersion/FeatureSet and HealthSnapshot/InstancePresence/InstanceHealth/InstanceReadiness records (architecture 02-contracts-and-protocols.md §4/5/6/11/12 domain model) are generated in Foundation or PublicApi as appropriate, plus EncodedBodyRef (registry04 §4) wired into every ResponseMeta.value oneof tag-4 read projection; independent positive/negative fixtures cover descriptor shape and the >4MiB large-read-projection envelope (messageType/descriptorHash/byteLength/snapshotToken/ResourceVersionRef SHA256 check before decode).

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-03.03 (capability/action/context/version/health descriptor records only, plus EncodedBodyRef (the immutable oversized-body reference form); excludes the Sync mutation allowlist and cross-owner/wrong-revision/opaque-object/forbidden-path negative vectors, which are CON.03): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\03-contract-foundation-and-licence-split.md, anchor rule-wp-03.03

Entry condition: adoption slice ADOPT.03.contracts is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [contract] CON.91: published Foundation ResourceRef/ResourceVersionRef/ArtifactRef (already generated) as the base EncodedBodyRef.resource field type
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Contracts:public/proto/arcforges/foundation/v1/foundation.proto; Contracts:public/proto/constraints/foundation-descriptors.json; Contracts:fixtures/public/con-02-descriptors.json
Shared resources (follow the owner protocol): RES-contracts-generated-baseline (regenerate): Never hand-edited or hand-merged: after rebasing, the author regenerates with the pinned generator and commits the result; CI rejects drift between schemas, descriptors and generated output.; RES-contracts-publication (append): Every merge to main publishes all Contracts packages at one allocated candidate version (Maven main as SNAPSHOT under the publication-channel profile); the integration owner keeps a single merge queue so publications stay ordered; no tag, republication or replacement version is created for verification.; RES-contracts-schema-sources (append): Each closure task edits only its own domain proto or HTTP-schema files and adds its own sharded constraint and fixture files; shared inventories (package inventory, foundation inventory, constraint aggregate) are append-only per closure. A proto file with several contributing tasks (operator, policy/configuration) has one designated author task and the others request changes through it. The integration owner merges closure pull requests one at a time and the next author rebases and regenerates.
Unblocks: APP.01, CON.03, CON.06, CON.10, CON.19, CON.20, CON.21, CON.22, SCOPE.20

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): offline unit tests for descriptor round-trip (C#/TS), decode-limit fixtures (exact 64MiB boundary and 64MiB+1 refusal) reusing WP03.02's WireLimits constants, deterministic regeneration, generated-header/import checks; no macOS/device/live-service CI per P2-017.
Completion evidence for the ledger: Independent fixture file con-02-descriptors.json; C#/TS conformance report; descriptor baseline diff.
Notes: This is the 'descriptor' half of WP-03.03. Small and foundational: many later domain tasks (CON.06 in-process ports, CON.10 task/chat tool binding) reference CapabilityDescriptor for tool metadata, so this should land early even though nothing strictly blocks it from running in parallel with CON.03-CON.05.
```

```text
Execute ArcForges delivery task CON.03 — Resource/Sync owner-body admission: closed Sync mutation allowlist + cross-owner/wrong-revision/opaque-object/forbidden-path negatives.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\contracts.md (anchor task-con-03).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Contracts (integration owner: Contracts integration owner, the holder of roles/integration-contracts).
Claim and handoff record: claims/con-03 (python tools/delivery.py claim CON.03 --worker <name>); task branch task/con-03 in Contracts; ledger record ledger/tasks/con-03.md.
Kind/size: contract/M. Baseline: not-started.
Outcome: A generated/schema-derived validator enforces that Sync (registry04 §10) accepts client-origin writes only for NotebookBody/NotesDocument/PropertyDefinition/SavedViewRecord/TagRecord and authorized ScopeMetadata/SlateMetadata (AggregateBody's Cloud-writable subset), refusing TaskSnapshot/AutomationView/ConversationBody/AgentProfile/SkillRecord/ChatProjectRecord/MemoryRecord/PreferenceRecord as client writes (Cloud-authored-only); externalBody indirection resolves to the same allowlist before validation. Independent negative vectors cover cross-owner reference, wrong-revision precondition, opaque/unknown AggregateBody variant, and forbidden-path (non-allowlisted body kind) attempts, plus compatible unknown-response preservation.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-03.03 (the Sync mutation allowlist and oversized-body admission negative-vector half; ResourceRef/ResourceVersionRef/BlobRef schema itself is already done (CON.91/WP-03.01)): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\03-contract-foundation-and-licence-split.md, anchor rule-wp-03.03

Entry condition: adoption slice ADOPT.03.contracts is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [contract] CON.02: EncodedBodyRef record
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Contracts:public/proto/arcforges/publicapi/v1/content.proto; Contracts:fixtures/public/con-03-sync-allowlist.json
Shared resources (follow the owner protocol): RES-contracts-generated-baseline (regenerate): Never hand-edited or hand-merged: after rebasing, the author regenerates with the pinned generator and commits the result; CI rejects drift between schemas, descriptors and generated output.; RES-contracts-publication (append): Every merge to main publishes all Contracts packages at one allocated candidate version (Maven main as SNAPSHOT under the publication-channel profile); the integration owner keeps a single merge queue so publications stay ordered; no tag, republication or replacement version is created for verification.; RES-contracts-schema-sources (append): Each closure task edits only its own domain proto or HTTP-schema files and adds its own sharded constraint and fixture files; shared inventories (package inventory, foundation inventory, constraint aggregate) are append-only per closure. A proto file with several contributing tasks (operator, policy/configuration) has one designated author task and the others request changes through it. The integration owner merges closure pull requests one at a time and the next author rebases and regenerates.
Unblocks: CLOUD.37, CON.09, CON.19, NOTES.02

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): offline positive/negative fixture suite (C#/TS); schema-level validator only (no owner authorization, persistence or transaction — those stay with WP-07/WP-21 per CA rules).
Completion evidence for the ledger: fixtures/public/con-03-sync-allowlist.json with named negative cases; validator unit test report.
Notes: Deliberately scoped narrower than 'author SyncService.* RPC methods' (that's CON.09, part of the huge WP-03.05 business-operation registry). CON.03 is only the shared-record ADMISSION RULE that CON.09's SyncService.pushChange/pushBatch and WP-21's real D1 sync both must obey — keeping it separate lets WP-21 pin an early closure (CON.03) without waiting for the full SyncService RPC surface (CON.09).
```

```text
Execute ArcForges delivery task CON.04 — ContentSandbox service schema (24 methods: session/slot/media/image/PDF/OTIO).

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\contracts.md (anchor task-con-04).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Contracts (integration owner: Contracts integration owner, the holder of roles/integration-contracts).
Claim and handoff record: claims/con-04 (python tools/delivery.py claim CON.04 --worker <name>); task branch task/con-04 in Contracts; ledger record ledger/tasks/con-04.md.
Kind/size: contract/L. Baseline: not-started.
Outcome: internal/proto/arcforges/local/sandbox/v1/sandbox.proto has the complete ContentSandboxService with all 24 methods, generated into ArcForges.Contracts.LocalRpc.Sandbox; wrong-child-direction/removed-method/cross-product-registration negative fixtures pass; policy test asserts every method carries the generated service/descriptor identity (CA rule).

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-03.04 (ContentSandboxService only, from annex 09 §§2-6 (OpenSession/RenewSession/GrantSlot/AckBuffer/ProbeMedia/OpenMediaReader/ReadMediaFrame/SeekMedia/CopyVideoFrame/CopyAudioFrame/CloseFrame/CloseReader/OpenImage/GetImageInfo/ReadImageTile/CloseImage/OpenPdf/GetPdfPage/ExtractPdfText/RenderPdfTile/ClosePdf/ReadOtio/WriteOtio/OtioReadChunk/CancelSession/CloseSession = 24 methods)): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\03-contract-foundation-and-licence-split.md, anchor rule-wp-03.04
- WP-03:7-evidence-local-grpc-closure-complete-l §7 evidence: Local gRPC closure — complete.LocalRpc.Platform/.Sandbox typed parser/connector/hint/bootstrap methods before consumers (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\03-contract-foundation-and-licence-split.md, package-level obligation

Entry condition: adoption slice ADOPT.03.contracts is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- none
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Contracts:internal/proto/arcforges/local/sandbox/v1/sandbox.proto; Contracts:src/internal/dotnet/ArcForges.Contracts.LocalRpc.Sandbox/**; Contracts:fixtures/internal/con-04-content-sandbox.json
Shared resources (follow the owner protocol): RES-contracts-generated-baseline (regenerate): Never hand-edited or hand-merged: after rebasing, the author regenerates with the pinned generator and commits the result; CI rejects drift between schemas, descriptors and generated output.; RES-contracts-publication (append): Every merge to main publishes all Contracts packages at one allocated candidate version (Maven main as SNAPSHOT under the publication-channel profile); the integration owner keeps a single merge queue so publications stay ordered; no tag, republication or replacement version is created for verification.; RES-contracts-schema-sources (append): Each closure task edits only its own domain proto or HTTP-schema files and adds its own sharded constraint and fixture files; shared inventories (package inventory, foundation inventory, constraint aggregate) are append-only per closure. A proto file with several contributing tasks (operator, policy/configuration) has one designated author task and the others request changes through it. The integration owner merges closure pull requests one at a time and the next author rebases and regenerates.
Unblocks: CON.19, PLT.09, PLT.15, PLT.45

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): offline: wrong-direction/removed-method/parent-death/cross-product-registration negative fixtures (per annex09 §6 required test list); policy test for generated service/descriptor identity; no real helper process, no live parser (that is WP-11/WP-13).
Completion evidence for the ledger: fixtures/internal/con-04-content-sandbox.json; RPC policy test report.
Notes: The single biggest service in the whole registry (24 methods). Independently implementable in parallel with CON.05/CON.06 — different proto file (sandbox/v1 vs platform/v1), different owning package (.LocalRpc.Sandbox vs.LocalRpc.Platform/.Chat/.Notes/.Scope/.Slate).
```

```text
Execute ArcForges delivery task CON.05 — Extension/Connector/LocalBootstrap service schema (annex09 helper closure minus ContentSandbox).

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\contracts.md (anchor task-con-05).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Contracts (integration owner: Contracts integration owner, the holder of roles/integration-contracts).
Claim and handoff record: claims/con-05 (python tools/delivery.py claim CON.05 --worker <name>); task branch task/con-05 in Contracts; ledger record ledger/tasks/con-05.md.
Kind/size: contract/M. Baseline: not-started.
Outcome: Public ExtensionHostService gains Handshake/Invoke/Stop (Handshake already partially scoped by extensions.proto's ExtensionLease); internal LocalBootstrapService (platform/v1) and ConnectorBroker are generated with the exact bootstrap transcript (HMAC-SHA256 challenge/confirm, one-use 32-byte secret) and connector state machine from annex09 §§2,6; IHubRegistry/IHubRouting/DeviceSsoBrokerService names are reserved in a retirement manifest and asserted absent from active service registration by a structural test.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-03.04 (ExtensionHostService (remaining Handshake/Invoke/Stop; RenewLease already done), ILocalBootstrap (Challenge/Confirm/Renew), IConnectorBroker (ListDefinitions/ListConnections/BeginConnection/CompleteConnection/GetConnection/RevokeConnection); reserve removed Hub/SSO/transfer names (IHubRegistry/IHubRouting/DeviceSsoBrokerService) without registering them): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\03-contract-foundation-and-licence-split.md, anchor rule-wp-03.04
- WP-03:7-evidence-local-grpc-closure-complete-l §7 evidence: Local gRPC closure — complete.LocalRpc.Platform/.Sandbox typed parser/connector/hint/bootstrap methods before consumers (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\03-contract-foundation-and-licence-split.md, package-level obligation

Entry condition: adoption slice ADOPT.03.contracts is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- none
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Contracts:public/proto/arcforges/extensions/v1/extensions.proto; Contracts:internal/proto/arcforges/local/platform/v1/platform.proto; Contracts:fixtures/internal/con-05-extension-connector-bootstrap.json
Shared resources (follow the owner protocol): RES-contracts-generated-baseline (regenerate): Never hand-edited or hand-merged: after rebasing, the author regenerates with the pinned generator and commits the result; CI rejects drift between schemas, descriptors and generated output.; RES-contracts-publication (append): Every merge to main publishes all Contracts packages at one allocated candidate version (Maven main as SNAPSHOT under the publication-channel profile); the integration owner keeps a single merge queue so publications stay ordered; no tag, republication or replacement version is created for verification.; RES-contracts-schema-sources (append): Each closure task edits only its own domain proto or HTTP-schema files and adds its own sharded constraint and fixture files; shared inventories (package inventory, foundation inventory, constraint aggregate) are append-only per closure. A proto file with several contributing tasks (operator, policy/configuration) has one designated author task and the others request changes through it. The integration owner merges closure pull requests one at a time and the next author rebases and regenerates.
Unblocks: CON.19, EXT.02, PRF.04

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): offline: replayed/cross-connection confirm, expired nonce, wrong child direction/role negative fixtures (annex09 §2/§6); structural test asserting Hub/SSO registration absence; no live OS pipe/socket (that is WP-06/WP-08/WP-09/WP-11).
Completion evidence for the ledger: fixtures/internal/con-05-extension-connector-bootstrap.json; retirement-manifest structural test report.
Notes: Independent of CON.04 (different proto files/packages).
```

```text
Execute ArcForges delivery task CON.06 — Product in-process port completion: INotesOperations/IScopeOperations/ISlateOperations/IChatOperations + infra ports.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\contracts.md (anchor task-con-06).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Contracts (integration owner: Contracts integration owner, the holder of roles/integration-contracts).
Claim and handoff record: claims/con-06 (python tools/delivery.py claim CON.06 --worker <name>); task branch task/con-06 in Contracts; ledger record ledger/tasks/con-06.md.
Kind/size: contract/L. Baseline: not-started.
Outcome: Every method in manifest11's 'in-process' scope class (ICapabilityProvider, IContextProvider, IArtifactHandler, IResourceAccess, IProductLifecycle, IDeepLinkTarget, INotesOperations [26 methods], IScopeOperations [13], ISlateOperations [19], IChatOperations [8]) is generated as a typed request/result pair per registry04 §6, with product-port packages containing only in-process records (no listener/gRPC registration) and a policy test proving that.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-03.04 (the 'Product interfaces use generated records and static in-process adapters' half — full method surface for the four product-port packages plus ICapabilityProvider/IContextProvider/IArtifactHandler/IResourceAccess/IProductLifecycle/IDeepLinkTarget): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\03-contract-foundation-and-licence-split.md, anchor rule-wp-03.04
- WP-03:p2-010-required-behavior-and-closure-sou P2-010 required behavior and closure (source KnowledgePolicy/Patch/View, typed one-use overrides, Notes run/atom/table-cell positions, complete initial owner/profile records) (P2-010 required behavior: source KnowledgePolicy/Patch/View and typed one-use overrides (source.getPolicy/setPolicy/clearPolicy, source.createConsent/revokeConsent) fall inside IChatOperations/context-provider scope; stable Notes run/atom/table-cell positions (NotesTextPosition already exists in content.proto from WP03.01 — this task only needs to verify no gap remains for table-cell addressing); package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\03-contract-foundation-and-licence-split.md, package-level obligation

Entry condition: adoption slice ADOPT.03.contracts is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [contract] CON.02: CapabilityDescriptor/ContextDescriptor shapes
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Contracts:internal/proto/arcforges/local/chat/v1/chat.proto; Contracts:internal/proto/arcforges/local/notes/v1/notes.proto; Contracts:internal/proto/arcforges/local/scope/v1/scope.proto; Contracts:internal/proto/arcforges/local/slate/v1/slate.proto; Contracts:fixtures/internal/con-06-product-ports.json
Shared resources (follow the owner protocol): RES-contracts-generated-baseline (regenerate): Never hand-edited or hand-merged: after rebasing, the author regenerates with the pinned generator and commits the result; CI rejects drift between schemas, descriptors and generated output.; RES-contracts-publication (append): Every merge to main publishes all Contracts packages at one allocated candidate version (Maven main as SNAPSHOT under the publication-channel profile); the integration owner keeps a single merge queue so publications stay ordered; no tag, republication or replacement version is created for verification.; RES-contracts-schema-sources (append): Each closure task edits only its own domain proto or HTTP-schema files and adds its own sharded constraint and fixture files; shared inventories (package inventory, foundation inventory, constraint aggregate) are append-only per closure. A proto file with several contributing tasks (operator, policy/configuration) has one designated author task and the others request changes through it. The integration owner merges closure pull requests one at a time and the next author rebases and regenerates.
Unblocks: CON.19, SLATE.12

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): offline: policy test asserting no product gRPC listener/registration exists; positive/negative fixtures for representative methods per product (full behavioral testing stays with each product's own WP1x/3x).
Completion evidence for the ledger: fixtures/internal/con-06-product-ports.json; in-process-only policy test report.
Notes: Four independent product sub-surfaces (Notes/Scope/Slate/Chat) that could in principle be four separate tasks; kept as one task because they share the same infra-port dependency (ICapabilityProvider etc.) and are individually S-to-M sized — splitting further would violate the 'do not create one task per trivial item' guidance. A future re-split by product is reasonable if a product-area team wants to own its own port slice.
```

```text
Execute ArcForges delivery task CON.07 — Identity/session/device operation registry + native-auth and browser HTTP exceptions.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\contracts.md (anchor task-con-07).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Contracts (integration owner: Contracts integration owner, the holder of roles/integration-contracts).
Claim and handoff record: claims/con-07 (python tools/delivery.py claim CON.07 --worker <name>); task branch task/con-07 in Contracts; ledger record ledger/tasks/con-07.md.
Kind/size: contract/L. Baseline: not-started.
Outcome: IdentityService/WorkspaceService/DeviceService are generated with all listed operations, exact request/response field tags, and the eight authorization fields exported per operation; GET /session/v1/native/authorize, POST /session/v1/native/token and the four /session/v1 browser routes have generated strict-JSON exception schemas (reusing WP03.02's JsonSerializerContext posture); independent fixtures cover the identity journeys table in contracts07 §1 (account creation, email/passkey/OIDC login, recovery, step-up, refresh, logout, PAT).

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-03.05 (IdentityService (29 ops)/WorkspaceService (4)/DeviceService (6) from registry04 §5, plus contracts07 §1 native PKCE token endpoint and the four /session/v1 browser routes as declared JSON exceptions): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\03-contract-foundation-and-licence-split.md, anchor rule-wp-03.05

Entry condition: adoption slice ADOPT.03.contracts is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- none
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Contracts:public/proto/arcforges/publicapi/v1/identity.proto; Contracts:public/http/v1/schema.json; Contracts:fixtures/public/con-07-identity.json
Shared resources (follow the owner protocol): RES-contracts-generated-baseline (regenerate): Never hand-edited or hand-merged: after rebasing, the author regenerates with the pinned generator and commits the result; CI rejects drift between schemas, descriptors and generated output.; RES-contracts-publication (append): Every merge to main publishes all Contracts packages at one allocated candidate version (Maven main as SNAPSHOT under the publication-channel profile); the integration owner keeps a single merge queue so publications stay ordered; no tag, republication or replacement version is created for verification.; RES-contracts-schema-sources (append): Each closure task edits only its own domain proto or HTTP-schema files and adds its own sharded constraint and fixture files; shared inventories (package inventory, foundation inventory, constraint aggregate) are append-only per closure. A proto file with several contributing tasks (operator, policy/configuration) has one designated author task and the others request changes through it. The integration owner merges closure pull requests one at a time and the next author rebases and regenerates.
Unblocks: AND.04, CLOUD.20, CON.19, WEB.10

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): offline positive/negative vectors per contracts07 §1 table (used/expired proof never replays, bad proof same bounded denial shape, wrong PKCE verifier never consumes valid code, etc.); no live provider, no real email/passkey ceremony (WP-22 owns that).
Completion evidence for the ledger: fixtures/public/con-07-identity.json; C#/TS/Kotlin conformance report.
Notes: Largest single domain in the public registry by operation count. WP-22 (Identity/Workspace/Device, owned by the Cloud lane) is the direct downstream consumer and is the one WP explicitly still gated behind the OLD 'whole WP03' edge in implementation-sequence.md §9 (22 depends on 11,21; 21 depends on 03,05,12) — this task is what actually unblocks WP-22's real work, not WP-03.05 as a monolith.
```

```text
Execute ArcForges delivery task CON.08 — Entitlement/commerce operation registry.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\contracts.md (anchor task-con-08).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Contracts (integration owner: Contracts integration owner, the holder of roles/integration-contracts).
Claim and handoff record: claims/con-08 (python tools/delivery.py claim CON.08 --worker <name>); task branch task/con-08 in Contracts; ledger record ledger/tasks/con-08.md.
Kind/size: contract/M. Baseline: not-started.
Outcome: EntitlementService/CommerceService generated with all listed operations and exact fields; every operation is tagged compatibility-class=frozen per CC-04; independent fixtures cover the closed condition set's entitlement.*/commerce.* error rows.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-03.05 (EntitlementService (6 ops) + CommerceService (~14 ops) from registry04 §5, all declared 'frozen' compatibility class per catalogue00 CC-04): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\03-contract-foundation-and-licence-split.md, anchor rule-wp-03.05

Entry condition: adoption slice ADOPT.03.contracts is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- none
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Contracts:public/proto/arcforges/publicapi/v1/commerce.proto; Contracts:fixtures/public/con-08-entitlement-commerce.json
Shared resources (follow the owner protocol): RES-contracts-generated-baseline (regenerate): Never hand-edited or hand-merged: after rebasing, the author regenerates with the pinned generator and commits the result; CI rejects drift between schemas, descriptors and generated output.; RES-contracts-publication (append): Every merge to main publishes all Contracts packages at one allocated candidate version (Maven main as SNAPSHOT under the publication-channel profile); the integration owner keeps a single merge queue so publications stay ordered; no tag, republication or replacement version is created for verification.; RES-contracts-schema-sources (append): Each closure task edits only its own domain proto or HTTP-schema files and adds its own sharded constraint and fixture files; shared inventories (package inventory, foundation inventory, constraint aggregate) are append-only per closure. A proto file with several contributing tasks (operator, policy/configuration) has one designated author task and the others request changes through it. The integration owner merges closure pull requests one at a time and the next author rebases and regenerates.
Unblocks: CON.19, WEB.14

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): offline positive/negative vectors; frozen-class compatibility baseline entries so any future field addition here fails the diff gate without an explicit new version (this is deliberate — financial operations must never silently gain an additive field).
Completion evidence for the ledger: fixtures/public/con-08-entitlement-commerce.json.
Notes: Independent of every other CON.0x domain task. Needed to start by WP-42 (commerce/entitlement/credits, the commerce, policy and operations lanes).
```

```text
Execute ArcForges delivery task CON.09 — Sync/resource-transfer/objects operation registry + realm-transfer.v1.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\contracts.md (anchor task-con-09).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Contracts (integration owner: Contracts integration owner, the holder of roles/integration-contracts).
Claim and handoff record: claims/con-09 (python tools/delivery.py claim CON.09 --worker <name>); task branch task/con-09 in Contracts; ledger record ledger/tasks/con-09.md.
Kind/size: contract/L. Baseline: not-started.
Outcome: SyncService/ResourceService/TransferService generated with all listed operations; SyncService.pushChange/pushBatch enforce CON.03's mutation allowlist at the schema-validator boundary; realm-transfer.v1's included/excluded-roots manifest and chunked-batch (<=100 roots) semantics are schema-encoded per contracts07 §5.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-03.05 (SyncService (~10 ops incl. listScopes/pullChanges/pushChange/pushBatch/getAggregate/listConflicts/resolveConflict/requestFullResync/getBootstrapPage), ResourceService transfer ops (beginUpload/completeUpload/getDownloadTicket/getMetadata/release/getUploadStatus/renewUploadTicket), TransferService (realm-transfer.v1: requestExport/previewImport/commitImport/get/list/cancel) from registry04 §5 and contracts07 §5): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\03-contract-foundation-and-licence-split.md, anchor rule-wp-03.05

Entry condition: adoption slice ADOPT.03.contracts is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [contract] CON.03: the closed Sync mutation allowlist validator
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Contracts:public/proto/arcforges/publicapi/v1/sync.proto; Contracts:public/proto/arcforges/publicapi/v1/transfer.proto; Contracts:fixtures/public/con-09-sync-transfer.json
Shared resources (follow the owner protocol): RES-contracts-generated-baseline (regenerate): Never hand-edited or hand-merged: after rebasing, the author regenerates with the pinned generator and commits the result; CI rejects drift between schemas, descriptors and generated output.; RES-contracts-publication (append): Every merge to main publishes all Contracts packages at one allocated candidate version (Maven main as SNAPSHOT under the publication-channel profile); the integration owner keeps a single merge queue so publications stay ordered; no tag, republication or replacement version is created for verification.; RES-contracts-schema-sources (append): Each closure task edits only its own domain proto or HTTP-schema files and adds its own sharded constraint and fixture files; shared inventories (package inventory, foundation inventory, constraint aggregate) are append-only per closure. A proto file with several contributing tasks (operator, policy/configuration) has one designated author task and the others request changes through it. The integration owner merges closure pull requests one at a time and the next author rebases and regenerates.
Unblocks: CLOUD.37, CON.19, SLATE.37

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): offline positive/negative vectors incl. stale revision -> preserved conflict proposal, absent-hash-never-promotes, expired-pin-blocks-adoption; no real D1/R2 (WP-21/WP-25 own that).
Completion evidence for the ledger: fixtures/public/con-09-sync-transfer.json.
Notes: WP-21 (Cloud D1/sync engine, the Cloud lane) is the direct consumer that most needs this + CON.03 to start; it does NOT need CON.07/08/10-16.
```

```text
Execute ArcForges delivery task CON.10 — Task/approval/bridge/chat/agent/automation/search operation registry + ai-internal package.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\contracts.md (anchor task-con-10).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Contracts (integration owner: Contracts integration owner, the holder of roles/integration-contracts).
Claim and handoff record: claims/con-10 (python tools/delivery.py claim CON.10 --worker <name>); task branch task/con-10 in Contracts; ledger record ledger/tasks/con-10.md.
Kind/size: contract/L. Baseline: not-started.
Outcome: All listed public services generated with exact fields and eight authorization fields; @arcforges/ai-internal and CloudInternal gain the ~15 internal/ai/v1 HTTP port schemas (authorize/claim/renew/reconcile/context/model-intent/model-outcome/settle/prepare-tools/cloud-tool/wait/finalize/stream-state/late-outcome + the inference-job family) from contracts05 §3/§8 as closed JSON records with CommitReceipt-style semantics.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-03.05 (TaskService(~9)/ApprovalService(2)/BridgeService(3)/public ChatOperationsService(~25)/AgentService(3)/AutomationService(9)/search.query from registry04 §5, plus internal/ai-http/v1 schema.json (ai-internal npm/CloudInternal package) for the C#<->AI-Worker internal HTTP ports in contracts05 §3): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\03-contract-foundation-and-licence-split.md, anchor rule-wp-03.05
- WP-03:p2-010-required-behavior-and-closure-sou P2-010 required behavior and closure (source KnowledgePolicy/Patch/View, typed one-use overrides, Notes run/atom/table-cell positions, complete initial owner/profile records) (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\03-contract-foundation-and-licence-split.md, package-level obligation

Entry condition: adoption slice ADOPT.03.contracts is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [contract] CON.02: CapabilityDescriptor
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Contracts:public/proto/arcforges/publicapi/v1/chat.proto; Contracts:internal/ai-http/v1/schema.json; Contracts:fixtures/public/con-10-chat-task-agent.json; Contracts:fixtures/internal/con-10-ai-internal.json
Shared resources (follow the owner protocol): RES-contracts-generated-baseline (regenerate): Never hand-edited or hand-merged: after rebasing, the author regenerates with the pinned generator and commits the result; CI rejects drift between schemas, descriptors and generated output.; RES-contracts-publication (append): Every merge to main publishes all Contracts packages at one allocated candidate version (Maven main as SNAPSHOT under the publication-channel profile); the integration owner keeps a single merge queue so publications stay ordered; no tag, republication or replacement version is created for verification.; RES-contracts-schema-sources (append): Each closure task edits only its own domain proto or HTTP-schema files and adds its own sharded constraint and fixture files; shared inventories (package inventory, foundation inventory, constraint aggregate) are append-only per closure. A proto file with several contributing tasks (operator, policy/configuration) has one designated author task and the others request changes through it. The integration owner merges closure pull requests one at a time and the next author rebases and regenerates.
Unblocks: AIR.00, AST.11, AST.14, CON.11, CON.19, DEV.02, DEV.04, HAR.00, HAR.02, SRCH.00, SRCH.01

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): offline positive/negative vectors for ChatTurn/AgentTask journeys per contracts07 §2 table; ai-internal codecs reuse WP03.02's strict-JSON posture; no live CF Worker (WP-52 owns that).
Completion evidence for the ledger: fixtures/public/con-10-chat-task-agent.json + fixtures/internal/con-10-ai-internal.json.
Notes: Second-largest domain task. WP-15/16/17 (ArcChat core/execution/independent-core, the assistant lanes) are the direct consumers; WP-52 (Cloud Harness, the AI lanes) needs both this and CON.11.
```

```text
Execute ArcForges delivery task CON.11 — Application/history/execution/events operations (annex10's 13 additions) + EventService.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\contracts.md (anchor task-con-11).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Contracts (integration owner: Contracts integration owner, the holder of roles/integration-contracts).
Claim and handoff record: claims/con-11 (python tools/delivery.py claim CON.11 --worker <name>); task branch task/con-11 in Contracts; ledger record ledger/tasks/con-11.md.
Kind/size: contract/M. Baseline: not-started.
Outcome: ApplicationService/HistoryService/ExecutionService/EventService generated with all 13+1 operations, RequestMeta.applicationScope(8)/historyMode(11) and ToolRequest.targetApplication(16) appended without renumbering existing fields; the 17 EventService.Poll hint payloads (sync.changed through config.revisionActivated) generated from one event registry; binary server-streaming frames validated at 32KiB/frame; reserved future Hub/DeviceSso methods verified absent from active registration.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-03.05 (the annex10 13 new operations (ApplicationService.List/Heartbeat/Disconnect, HistoryService.BeginImport/FinalizeImport/GetImport/CancelImport, ExecutionService.StartTransientTurn/ReadOutput/WatchOutput/AcknowledgeOutput/PurgeTransient, EventService.Watch) plus EventService.Poll's 17 hint payloads (CA-12) and StreamFrame/OutputChunk/StreamPosition/StreamReset server-streaming framing): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\03-contract-foundation-and-licence-split.md, anchor rule-wp-03.05
- WP-03:current-application-and-stream-contract Current application and stream contract completeness (annex10+manifest11, explicitly required before 03 completion) ('Current application and stream contract completeness' package-level obligation — explicitly required before 03 completion, not a.90-deferred item): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\03-contract-foundation-and-licence-split.md, package-level obligation

Entry condition: adoption slice ADOPT.03.contracts is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [contract] CON.10: TaskSnapshot/ChatTurnProgress shapes for ExecutionProgress's oneof
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Contracts:public/proto/arcforges/publicapi/v1/application.proto; Contracts:public/proto/arcforges/events/v1/events.proto; Contracts:fixtures/public/con-11-application-streams.json
Shared resources (follow the owner protocol): RES-contracts-generated-baseline (regenerate): Never hand-edited or hand-merged: after rebasing, the author regenerates with the pinned generator and commits the result; CI rejects drift between schemas, descriptors and generated output.; RES-contracts-publication (append): Every merge to main publishes all Contracts packages at one allocated candidate version (Maven main as SNAPSHOT under the publication-channel profile); the integration owner keeps a single merge queue so publications stay ordered; no tag, republication or replacement version is created for verification.; RES-contracts-schema-sources (append): Each closure task edits only its own domain proto or HTTP-schema files and adds its own sharded constraint and fixture files; shared inventories (package inventory, foundation inventory, constraint aggregate) are append-only per closure. A proto file with several contributing tasks (operator, policy/configuration) has one designated author task and the others request changes through it. The integration owner merges closure pull requests one at a time and the next author rebases and regenerates.
Unblocks: AND.04, AND.05, AST.01, AST.07, CLOUD.29, CON.15, CON.19, DEV.01, HAR.01

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): offline: binary unary/stream frame fixtures, scope/presence/unknown-field vectors, contract fixtures with mismatched resource owner/forged target/stale epoch per annex10 §6; no live gRPC-Web transport (WP-06/23/24/30 own that).
Completion evidence for the ledger: fixtures/public/con-11-application-streams.json.
Notes: Directly required by WP-24 (realtime/reliable events) and WP-26 (device bridge), both the Cloud lane; also the substep the WP03 text is most emphatic about ('required before 03 completion, not a.90 design task').
```

```text
Execute ArcForges delivery task CON.12 — Extension and policy schemas: manifest.v1/workflow.v1/panel.v1/policy body.v1/configuration.v1.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\contracts.md (anchor task-con-12).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Contracts (integration owner: Contracts integration owner, the holder of roles/integration-contracts).
Claim and handoff record: claims/con-12 (python tools/delivery.py claim CON.12 --worker <name>); task branch task/con-12 in Contracts; ledger record ledger/tasks/con-12.md.
Kind/size: contract/M. Baseline: not-started.
Outcome: The five contracts08 schema families are authored as closed JSON schemas (manifest.v1/workflow.v1/panel.v1 under public/http or a dedicated extensions schema path; policy body.v1 and configuration.v1 under public/http and internal/ai-http respectively) with generated C#/TS validators; independent vectors cover malformed archive, permission expansion, revoke-during-work, private-schema-rollback-refusal and the deterministic bucket-assignment hash vectors from contracts08 §5.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-03.05 (extension/policy schemas named in WP-03 §4's projects table ('Selected CF/auth/provider HTTP exceptions') and contracts08 in full:.arcpkg manifest.v1, workflow.v1 DAG, panel.v1 declarative UI, PolicyBundle body.v1, internal ConfigurationDocument (20 sections)): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\03-contract-foundation-and-licence-split.md, anchor rule-wp-03.05

Entry condition: adoption slice ADOPT.03.contracts is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- none
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Contracts:public/http/v1/schema.json; Contracts:internal/ai-http/v1/schema.json; Contracts:fixtures/public/con-12-extension-policy.json
Shared resources (follow the owner protocol): RES-contracts-generated-baseline (regenerate): Never hand-edited or hand-merged: after rebasing, the author regenerates with the pinned generator and commits the result; CI rejects drift between schemas, descriptors and generated output.; RES-contracts-publication (append): Every merge to main publishes all Contracts packages at one allocated candidate version (Maven main as SNAPSHOT under the publication-channel profile); the integration owner keeps a single merge queue so publications stay ordered; no tag, republication or replacement version is created for verification.; RES-contracts-schema-sources (append): Each closure task edits only its own domain proto or HTTP-schema files and adds its own sharded constraint and fixture files; shared inventories (package inventory, foundation inventory, constraint aggregate) are append-only per closure. A proto file with several contributing tasks (operator, policy/configuration) has one designated author task and the others request changes through it. The integration owner merges closure pull requests one at a time and the next author rebases and regenerates.
Unblocks: CON.19, POL.02, POL.09

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): offline vectors per contracts08 (allocation-0/10000 boundary bucket tests, lower-value-dominates capacity limit test, invalid commercial credential blocks activation); no live broker/OS profile (WP-09/WP-11/WP-41/WP-44 own that).
Completion evidence for the ledger: fixtures/public/con-12-extension-policy.json.
Notes: Needed to start by WP-41 (extensions) and WP-44 (policy/configuration), both currently blocked on the whole-WP03 edge in the old serial graph.
```

```text
Execute ArcForges delivery task CON.13 — Package catalog operation registry (CatalogService).

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\contracts.md (anchor task-con-13).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Contracts (integration owner: Contracts integration owner, the holder of roles/integration-contracts).
Claim and handoff record: claims/con-13 (python tools/delivery.py claim CON.13 --worker <name>); task branch task/con-13 in Contracts; ledger record ledger/tasks/con-13.md.
Kind/size: contract/S. Baseline: not-started.
Outcome: arcforges.catalog.v1 generated with the 7 public CatalogService operations and their records; DNS TXT publisher-verification challenge format and the PAT-eligible subset (catalog.search/getPackage/listVersions/submitVersion/getSubmission per catalogue00's PAT allowlist) are schema-encoded.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-03.05 (the public CatalogService (search/getPackage/listVersions/registerPublisher/verifyPublisher/submitVersion/getSubmission, 7 ops) and PublisherView/CatalogPackageView/CatalogVersionView/CatalogSubmissionView/CatalogReviewDecision records from registry04 §4/§5): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\03-contract-foundation-and-licence-split.md, anchor rule-wp-03.05

Entry condition: adoption slice ADOPT.03.contracts is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- none
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Contracts:public/proto/arcforges/catalog/v1/catalog.proto; Contracts:fixtures/public/con-13-package-catalog.json
Shared resources (follow the owner protocol): RES-contracts-generated-baseline (regenerate): Never hand-edited or hand-merged: after rebasing, the author regenerates with the pinned generator and commits the result; CI rejects drift between schemas, descriptors and generated output.; RES-contracts-publication (append): Every merge to main publishes all Contracts packages at one allocated candidate version (Maven main as SNAPSHOT under the publication-channel profile); the integration owner keeps a single merge queue so publications stay ordered; no tag, republication or replacement version is created for verification.; RES-contracts-schema-sources (append): Each closure task edits only its own domain proto or HTTP-schema files and adds its own sharded constraint and fixture files; shared inventories (package inventory, foundation inventory, constraint aggregate) are append-only per closure. A proto file with several contributing tasks (operator, policy/configuration) has one designated author task and the others request changes through it. The integration owner merges closure pull requests one at a time and the next author rebases and regenerates.
Unblocks: CON.14, CON.19

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): offline vectors for the catalogue00 PAT-allowlist assertion and submission-integrity checks (matching ID/version/digest/license).
Completion evidence for the ledger: fixtures/public/con-13-package-catalog.json.
Notes: Small and self-contained.
```

```text
Execute ArcForges delivery task CON.14 — Operator control service (OperatorService, full §9/9.1/9.2 protocol).

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\contracts.md (anchor task-con-14).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Contracts (integration owner: Contracts integration owner, the holder of roles/integration-contracts).
Claim and handoff record: claims/con-14 (python tools/delivery.py claim CON.14 --worker <name>); task branch task/con-14 in Contracts; ledger record ledger/tasks/con-14.md.
Kind/size: contract/L. Baseline: not-started.
Outcome: internal/proto/arcforges/operator/v1/operator.proto generated with all 29 OperatorService methods (ListCases through catalog.review/catalog.revoke), OperatorCallContext(tag100)/OperatorProposalRef(tag101) appended per method, and the typed propose/approve/execute protocol (§9.2) with its 9 mutation-variant table rows (grant/revokeGrant/issueCredit/adjustCredit/refund/catalogReview/catalogRevoke/appeal/kill); independent negative vectors cover distinct-approver violation, stale hash/revision/configuration, role revocation, expiry, concurrent consumption and lost receipt; no direct SQL or public-SDK import of operator schema.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-03.05 (OperatorService's ~29 methods with all eight authorization fields and the OC-03 role matrix): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\03-contract-foundation-and-licence-split.md, anchor rule-wp-03.05
- WP-03:operator-contract-closure-package-level 'Operator contract closure' package-level obligation — schema and negative vectors only; WP-23 owns real identity/dispatch, WP-42 financial owners, WP-44 config/policy owners, WP-45 the console join ('Operator contract closure' package-level obligation — schema and negative vectors only; WP-23 owns real identity/dispatch, WP-42 financial owners, WP-44 config/policy owners, WP-45 the console join; package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\03-contract-foundation-and-licence-split.md, package-level obligation

Entry condition: adoption slice ADOPT.03.contracts is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [contract] CON.13: CatalogSubmissionView/CatalogVersionView
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Contracts:internal/proto/arcforges/operator/v1/operator.proto; Contracts:src/internal/dotnet/ArcForges.Contracts.CloudInternal/**; Contracts:src/internal/ts/operator-client/src/**; Contracts:fixtures/internal/con-14-operator.json
Shared resources (follow the owner protocol): RES-contracts-generated-baseline (regenerate): Never hand-edited or hand-merged: after rebasing, the author regenerates with the pinned generator and commits the result; CI rejects drift between schemas, descriptors and generated output.; RES-contracts-publication (append): Every merge to main publishes all Contracts packages at one allocated candidate version (Maven main as SNAPSHOT under the publication-channel profile); the integration owner keeps a single merge queue so publications stay ordered; no tag, republication or replacement version is created for verification.; RES-contracts-schema-sources (append): Each closure task edits only its own domain proto or HTTP-schema files and adds its own sharded constraint and fixture files; shared inventories (package inventory, foundation inventory, constraint aggregate) are append-only per closure. A proto file with several contributing tasks (operator, policy/configuration) has one designated author task and the others request changes through it. The integration owner merges closure pull requests one at a time and the next author rebases and regenerates.
Unblocks: COM.13, CON.19, OPS.05, OPS.11, OPS.13, POL.05

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): offline negative vectors per registry04 §9.1/§9.2 (public customer/PAT/agent access refuses; distinct approver enforced; stale hash/revision fails); no live Entra OIDC session (WP-06/WP-45 own that).
Completion evidence for the ledger: fixtures/internal/con-14-operator.json.
Notes: @arcforges/operator-client package already exists as an empty-ish scaffold (WP03.00); this task is what actually fills it. WP-45 (operations console, the commerce, policy and operations lanes) is the direct consumer.
```

```text
Execute ArcForges delivery task CON.15 — Cloudflare-internal HTTP bindings (AI Worker <-> C# ports beyond ai-internal's chat/task family).

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\contracts.md (anchor task-con-15).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Contracts (integration owner: Contracts integration owner, the holder of roles/integration-contracts).
Claim and handoff record: claims/con-15 (python tools/delivery.py claim CON.15 --worker <name>); task branch task/con-15 in Contracts; ledger record ledger/tasks/con-15.md.
Kind/size: contract/M. Baseline: not-started.
Outcome: The remaining ~15 contracts05 internal HTTP ports and their records are generated as closed JSON schemas in internal/ai-http/v1/schema.json (or a dedicated internal/cf-http/v1 if the CON.10 file is already large), reusing WP03.02's strict-JSON posture; independent vectors cover duplicate dispatch, lease takeover, R2 part mismatch and stale-epoch rejection per contracts05 §7's injection list (schema-level only — no live Worker).

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-03.90 ('Private CF binding/event definitions' input — the remaining contracts05 ports not already covered by CON.10 (ai-internal): /internal/objects/v1/* (authorize/part-receipt/verification/job-grant/job-authorize), /internal/ai/v1/dispatch|control|delete (Worker-side), inference-job family (embedding/rerank), and CfDeletionTarget/CfDeletionReceipt/SessionBinding/BackupManifest records): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\03-contract-foundation-and-licence-split.md, anchor rule-wp-03.90

Entry condition: adoption slice ADOPT.03.contracts is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [contract] CON.11: ExecutionOwner/StreamPosition shapes
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Contracts:internal/ai-http/v1/schema.json; Contracts:fixtures/internal/con-15-cf-internal.json
Shared resources (follow the owner protocol): RES-contracts-generated-baseline (regenerate): Never hand-edited or hand-merged: after rebasing, the author regenerates with the pinned generator and commits the result; CI rejects drift between schemas, descriptors and generated output.; RES-contracts-publication (append): Every merge to main publishes all Contracts packages at one allocated candidate version (Maven main as SNAPSHOT under the publication-channel profile); the integration owner keeps a single merge queue so publications stay ordered; no tag, republication or replacement version is created for verification.; RES-contracts-schema-sources (append): Each closure task edits only its own domain proto or HTTP-schema files and adds its own sharded constraint and fixture files; shared inventories (package inventory, foundation inventory, constraint aggregate) are append-only per closure. A proto file with several contributing tasks (operator, policy/configuration) has one designated author task and the others request changes through it. The integration owner merges closure pull requests one at a time and the next author rebases and regenerates.
Unblocks: CON.19, EXT.10, HAR.00

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): offline vectors only; explicitly NOT a live-Worker/D1/R2 test (that is WP-06 minimal probe and WP-52 real Harness per the producer matrix's WP03 row: 'Owner handlers are deliberately absent; codec/validator fixtures prove schema only').
Completion evidence for the ledger: fixtures/internal/con-15-cf-internal.json.
Notes: Consumed by WP-21 (D1 execution lease), WP-25 (R2/object lifecycle), WP-52 (Harness) — all the Cloud lane/the AI lanes. This is schema-only; the actual Worker deployment is explicitly out of WP03 scope (WP03 §1 'Out of scope:... The cloud endpoint implementations (23)').
```

```text
Execute ArcForges delivery task CON.16 — Signed catalog/update/realm formats (catalog-index.v1, catalog-revocations.v1, android-update.v1, realm.v1).

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\contracts.md (anchor task-con-16).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Contracts (integration owner: Contracts integration owner, the holder of roles/integration-contracts).
Claim and handoff record: claims/con-16 (python tools/delivery.py claim CON.16 --worker <name>); task branch task/con-16 in Contracts; ledger record ledger/tasks/con-16.md.
Kind/size: contract/M. Baseline: not-started.
Outcome: The four signed-format schemas are authored under public/http (or a dedicated signed-formats path) with canonical signing-vector fixtures and a deterministic fixture-only trust root (Ed25519, distinct from any production key); malformed/expired/rollback/mixed-shard negative vectors exist per WP-03.07's gate; android-update.v1 matches registry04's tail-section field list exactly (packageId/channel/versionName/versionCode-as-string/minSdk/minSupportedVersionCode/apkUrl/sha256/size/signingCertificateSha256/releaseNotesUrl/publishedAt, expiry<=7 days).

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-03.07 (full — publish catalog-index.v1, catalog-revocations.v1, android-update.v1 and realm.v1 schemas, canonical signing vectors and separate fixture trust roots; production keys are explicitly WP-53 output, not a WP-03 input): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\03-contract-foundation-and-licence-split.md, anchor rule-wp-03.07

Entry condition: adoption slice ADOPT.03.contracts is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- none
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Contracts:public/http/v1/signed-formats.schema.json; Contracts:fixtures/public/con-16-signed-formats.json
Shared resources (follow the owner protocol): RES-contracts-generated-baseline (regenerate): Never hand-edited or hand-merged: after rebasing, the author regenerates with the pinned generator and commits the result; CI rejects drift between schemas, descriptors and generated output.; RES-contracts-publication (append): Every merge to main publishes all Contracts packages at one allocated candidate version (Maven main as SNAPSHOT under the publication-channel profile); the integration owner keeps a single merge queue so publications stay ordered; no tag, republication or replacement version is created for verification.; RES-contracts-schema-sources (append): Each closure task edits only its own domain proto or HTTP-schema files and adds its own sharded constraint and fixture files; shared inventories (package inventory, foundation inventory, constraint aggregate) are append-only per closure. A proto file with several contributing tasks (operator, policy/configuration) has one designated author task and the others request changes through it. The integration owner merges closure pull requests one at a time and the next author rebases and regenerates.
Permitted substitutes (never real integration evidence): SUB-signed-format-fixture-keys: signature/hash verification mechanics, expired/revoked/unknown-key refusal, malformed/rollback/mixed-shard handling Real producer ['UPD.07']; removed by REL.11
Unblocks: AND.20, CON.19, EXT.04, EXT.06, UPD.07

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): offline signature/hash verification vectors; no real key custody, no live distribution (WP-32/WP-41/WP-53 own those).
Completion evidence for the ledger: fixtures/public/con-16-signed-formats.json with named trust-root fixture and its provenance note ('fixture only, never production').
Notes: Fully independent of every other CON.0x task (self-contained format definitions). Gate explicitly states 'WP32/WP41 can implement complete consumers with deterministic fixture keys and named later production replacement' — this is the textbook named-scaffolding pattern from implementation-sequence.md §3.1.
```

```text
Execute ArcForges delivery task CON.17 — Cross-language compatibility window + canonical semantic hash.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\contracts.md (anchor task-con-17).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Contracts (integration owner: Contracts integration owner, the holder of roles/integration-contracts).
Claim and handoff record: claims/con-17 (python tools/delivery.py claim CON.17 --worker <name>); task branch task/con-17 in Contracts; ledger record ledger/tasks/con-17.md.
Kind/size: contract/M. Baseline: not-started.
Outcome: A canonical-semantic-hash implementation (per registry04 §2's exact algorithm: sorted ASCII property names, canonical integer/decimal strings, NFC where required) exists in C#/TS with shared golden vectors; a compatibility-matrix test harness runs previous-published-client-assembly against current server and current client against a pinned minimum-server descriptor set, both directions; deliberate deletion/tag-reuse/type-change mutations are injected and must fail the baseline-diff gate before publication.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-03.06 (full — wire bigint/decimal-coefficient-scale/oneof-presence/unknown-field/additive-response-evolution profile; canonical semantic hash distinct from wire byte hash; independent versioning of descriptors from applications; supported-window enforcement (previous-client/current-server and current-client/minimum-server matrices); deletion/tag-reuse/type-change failure tests): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\03-contract-foundation-and-licence-split.md, anchor rule-wp-03.06

Entry condition: adoption slice ADOPT.03.contracts is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [contract] CON.92: already-published Foundation/PublicApi as the 'previous stable' fixture
Completion prerequisites (may start earlier; cannot complete before these are complete):
- [integration] CON.18: full coverage of the compatibility matrix against every later-added service (CON.07-CON.16)

Permitted write scope: Contracts:eng/check_compatibility.py; Contracts:tests/tooling/test_compatibility_matrix.py; Contracts:fixtures/public/con-17-compat-hash.json
Shared resources (follow the owner protocol): RES-contracts-generated-baseline (regenerate): Never hand-edited or hand-merged: after rebasing, the author regenerates with the pinned generator and commits the result; CI rejects drift between schemas, descriptors and generated output.; RES-contracts-publication (append): Every merge to main publishes all Contracts packages at one allocated candidate version (Maven main as SNAPSHOT under the publication-channel profile); the integration owner keeps a single merge queue so publications stay ordered; no tag, republication or replacement version is created for verification.; RES-contracts-schema-sources (append): Each closure task edits only its own domain proto or HTTP-schema files and adds its own sharded constraint and fixture files; shared inventories (package inventory, foundation inventory, constraint aggregate) are append-only per closure. A proto file with several contributing tasks (operator, policy/configuration) has one designated author task and the others request changes through it. The integration owner merges closure pull requests one at a time and the next author rebases and regenerates.
Unblocks: CON.19

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): offline: golden semantic-hash vectors (order-independent, explicit-null-sensitive per registry04 §2's exact examples); deliberate-break injection tests; no live multi-version deployment (that is WP-23.06's real bidirectional test).
Completion evidence for the ledger: fixtures/public/con-17-compat-hash.json; compatibility-matrix CI job report.
Notes: Marked early_risk_proof=true: getting the canonical semantic hash algorithm right (vs. wire byte hash) early is exactly the kind of narrow risk proof that should stay early, because every later domain task's fixtures implicitly depend on hash determinism, and a late discovery of a hash-algorithm bug would invalidate many already-published fixture files.
```

```text
Execute ArcForges delivery task CON.18 — Operation-scope manifest + authorization-reachability matrix generator.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\contracts.md (anchor task-con-18).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Contracts (integration owner: Contracts integration owner, the holder of roles/integration-contracts).
Claim and handoff record: claims/con-18 (python tools/delivery.py claim CON.18 --worker <name>); task branch task/con-18 in Contracts; ledger record ledger/tasks/con-18.md.
Kind/size: contract/S. Baseline: not-started.
Outcome: A generator/policy-test tool reads manifest11's ~380-row scope-class table as its oracle, cross-references every currently-registered service method's exported eight authorization fields (capability/risk/approval/stepUp/localPresence/egress/patEligible/actorKinds), and fails the build on any unclassified, ambiguous, or nonexistent-idempotency-example method, or any tool reachability of a human-only approval/credential/commerce/policy method.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-03:7-evidence-operation-by-actor-reachabili §7 evidence: operation-by-actor reachability matrix (AZ-04) for public/local/operator/CF/exception bindings (§7 evidence requirement: 'Generate an operation-by-actor reachability matrix for every public/local/operator/CF/exception binding under catalogue 00 AZ-04, with all seven effective authorization fields and source profile. Fail unclassified/ambiguous fields...'; package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\03-contract-foundation-and-licence-split.md, package-level obligation

Entry condition: adoption slice ADOPT.03.contracts is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- none
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Contracts:eng/check_operation_scope.py; Contracts:eng/operation-scope-manifest.json
Shared resources (follow the owner protocol): RES-contracts-generated-baseline (regenerate): Never hand-edited or hand-merged: after rebasing, the author regenerates with the pinned generator and commits the result; CI rejects drift between schemas, descriptors and generated output.; RES-contracts-publication (append): Every merge to main publishes all Contracts packages at one allocated candidate version (Maven main as SNAPSHOT under the publication-channel profile); the integration owner keeps a single merge queue so publications stay ordered; no tag, republication or replacement version is created for verification.; RES-contracts-schema-sources (append): Each closure task edits only its own domain proto or HTTP-schema files and adds its own sharded constraint and fixture files; shared inventories (package inventory, foundation inventory, constraint aggregate) are append-only per closure. A proto file with several contributing tasks (operator, policy/configuration) has one designated author task and the others request changes through it. The integration owner merges closure pull requests one at a time and the next author rebases and regenerates.
Unblocks: CON.17, CON.19, GOV.16

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): offline: the tool itself is tested against the current (mostly 'pending') state and against synthetic unclassified/ambiguous fixtures that must fail.
Completion evidence for the ledger: eng/operation-scope-manifest.json plus its policy-test pass/fail report.
Notes: Small and foundational — should land early so every CON.07-CON.16 domain task can self-check against it as it lands, rather than everything being checked only at the very end (CON.19).
```

```text
Execute ArcForges delivery task CON.19 — WP03.90 — verify the owned Contracts artifact and its real (non-consumer) integration.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\contracts.md (anchor task-con-19).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Contracts (integration owner: Contracts integration owner, the holder of roles/integration-contracts).
Claim and handoff record: claims/con-19 (python tools/delivery.py claim CON.19 --worker <name>); task branch task/con-19 in Contracts; ledger record ledger/tasks/con-19.md.
Kind/size: contract/M. Baseline: not-started.
Outcome: Deterministic generation, compatibility/reserved-field checks (CON.17's harness), Apache closure, and independent precise-value/error/profile vectors all pass across the complete CON.02-CON.18 closure; all three generated client ecosystems (NuGet, npm, Maven/Kotlin) restore the actual published candidate artifacts in isolated consumer tests; the WP-03.90 completion receipt records exact artifact identities and real-vs-fixture status per obligation.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-03.90 (all work except the parts mapped to CON.15): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\03-contract-foundation-and-licence-split.md, anchor rule-wp-03.90
- WP-03:8-completion-gate-6-items-p2-009-vg-04-f §8 completion gate (6 items) + P2-009/VG-04/F-026 scoped gate contributions (§8 completion gate items 1-6 and the P2-009/VG-04/F-026 gate contributions; package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\03-contract-foundation-and-licence-split.md, package-level obligation

Entry condition: adoption slice ADOPT.03.contracts is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [contract] CON.02: all CON.02-CON.18 tasks complete and published
- [contract] CON.18: full operation-scope manifest with zero pending rows
- [artifact] CON.03: closure published
- [artifact] CON.04: closure published
- [artifact] CON.05: closure published
- [artifact] CON.06: closure published
- [artifact] CON.07: closure published
- [artifact] CON.08: closure published
- [artifact] CON.09: closure published
- [artifact] CON.10: closure published
- [artifact] CON.11: closure published
- [artifact] CON.12: closure published
- [artifact] CON.13: closure published
- [artifact] CON.14: closure published
- [artifact] CON.15: closure published
- [artifact] CON.16: closure published
- [artifact] CON.17: closure published
- [artifact] CON.20: closure published
- [artifact] CON.21: closure published
- [artifact] CON.22: closure published
- [artifact] CON.01: package task delivered
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Contracts:docs/wp03-90-verification.md; Contracts:artifacts/contracts/**
Shared resources (follow the owner protocol): RES-contracts-generated-baseline (regenerate): Never hand-edited or hand-merged: after rebasing, the author regenerates with the pinned generator and commits the result; CI rejects drift between schemas, descriptors and generated output.; RES-contracts-publication (append): Every merge to main publishes all Contracts packages at one allocated candidate version (Maven main as SNAPSHOT under the publication-channel profile); the integration owner keeps a single merge queue so publications stay ordered; no tag, republication or replacement version is created for verification.; RES-contracts-schema-sources (append): Each closure task edits only its own domain proto or HTTP-schema files and adds its own sharded constraint and fixture files; shared inventories (package inventory, foundation inventory, constraint aggregate) are append-only per closure. A proto file with several contributing tasks (operator, policy/configuration) has one designated author task and the others request changes through it. The integration owner merges closure pull requests one at a time and the next author rebases and regenerates.

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): the full P2-017-scoped suite: deterministic regen, all isolated NuGet/npm/Maven consumer restore-and-compile tests, descriptor baseline diff clean, Apache boundary clean; explicitly NOT live-service/device/macOS per P2-017 — 'no missing owner decision deferred to consumer coding' per the producer matrix's WP03 acceptance row.
Completion evidence for the ledger: WP-03.90 completion receipt: source commit, producer release, candidate hashes, actual runtime/OS/provider identity tested, scenario, result, limitations, real-versus-fixture status per obligation (matching the format of the WP03.00/01/02 receipts already on file).
Notes: This is WP03's own closure, NOT waiting for WP-04/05/06/09/21/23/30 to build real consumers — per producer-artifacts-and-integration.md's WP03 row, WP03's own acceptance is schema/fixture/candidate-restore evidence only ('Owner handlers are deliberately absent'). Real cross-repo integration is separate IM.* proposals below.
```

```text
Execute ArcForges delivery task CON.20 — Notes public operation registry.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\contracts.md (anchor task-con-20).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Contracts (integration owner: Contracts integration owner, the holder of roles/integration-contracts).
Claim and handoff record: claims/con-20 (python tools/delivery.py claim CON.20 --worker <name>); task branch task/con-20 in Contracts; ledger record ledger/tasks/con-20.md.
Kind/size: contract/M. Baseline: not-started.
Outcome: NotesService is generated with all notes.* operations (notebooks, folders, documents, revisions, checkpoints, restore and requestExport), exact fields, authorization profiles and independent vectors in C#, TypeScript and Kotlin.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-03.05 (notes.* operations (17), their records, eight authorization fields and vectors): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\03-contract-foundation-and-licence-split.md, anchor rule-wp-03.05

Entry condition: adoption slice ADOPT.03.contracts is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [contract] CON.02: capability/action/context/resource descriptor and oversized-body reference records
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Contracts:public/proto/arcforges/*/v1/**; Contracts:fixtures/public/con-{i}-*.json; Contracts:src/public/**/Generated/**
Shared resources (follow the owner protocol): RES-contracts-generated-baseline (regenerate): Never hand-edited or hand-merged: after rebasing, the author regenerates with the pinned generator and commits the result; CI rejects drift between schemas, descriptors and generated output.; RES-contracts-publication (append): Every merge to main publishes all Contracts packages at one allocated candidate version (Maven main as SNAPSHOT under the publication-channel profile); the integration owner keeps a single merge queue so publications stay ordered; no tag, republication or replacement version is created for verification.; RES-contracts-schema-sources (append): Each closure task edits only its own domain proto or HTTP-schema files and adds its own sharded constraint and fixture files; shared inventories (package inventory, foundation inventory, constraint aggregate) are append-only per closure. A proto file with several contributing tasks (operator, policy/configuration) has one designated author task and the others request changes through it. The integration owner merges closure pull requests one at a time and the next author rebases and regenerates.
Unblocks: CLOUD.37, CLOUD.45, CON.19, NOTES.20

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Deterministic regeneration, descriptor/tag/compatibility checks, closed-schema validators, independent positive and negative vectors in C#, TypeScript and Kotlin; Windows/Linux compilation and packaging only (P2-017).
Completion evidence for the ledger: Merged pull request, published Contracts candidate identity containing the closure, vector and compatibility results, and the operation-scope manifest rows flipped to verified for these operations.
Notes: Added so that every operation family in the operation-scope manifest has a closure task.
```

```text
Execute ArcForges delivery task CON.21 — Simulation operation registry.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\contracts.md (anchor task-con-21).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Contracts (integration owner: Contracts integration owner, the holder of roles/integration-contracts).
Claim and handoff record: claims/con-21 (python tools/delivery.py claim CON.21 --worker <name>); task branch task/con-21 in Contracts; ledger record ledger/tasks/con-21.md.
Kind/size: contract/M. Baseline: not-started.
Outcome: SimulationService is generated with all simulation.* operations (definitions, scenario versions, run control, segments, segment tickets and state polling), exact fields and vectors in C#, TypeScript and Kotlin.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-03.05 (simulation.* operations (12), their records, authorization fields and vectors): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\03-contract-foundation-and-licence-split.md, anchor rule-wp-03.05

Entry condition: adoption slice ADOPT.03.contracts is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [contract] CON.02: capability/action/context/resource descriptor and oversized-body reference records
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Contracts:public/proto/arcforges/*/v1/**; Contracts:fixtures/public/con-{i}-*.json; Contracts:src/public/**/Generated/**
Shared resources (follow the owner protocol): RES-contracts-generated-baseline (regenerate): Never hand-edited or hand-merged: after rebasing, the author regenerates with the pinned generator and commits the result; CI rejects drift between schemas, descriptors and generated output.; RES-contracts-publication (append): Every merge to main publishes all Contracts packages at one allocated candidate version (Maven main as SNAPSHOT under the publication-channel profile); the integration owner keeps a single merge queue so publications stay ordered; no tag, republication or replacement version is created for verification.; RES-contracts-schema-sources (append): Each closure task edits only its own domain proto or HTTP-schema files and adds its own sharded constraint and fixture files; shared inventories (package inventory, foundation inventory, constraint aggregate) are append-only per closure. A proto file with several contributing tasks (operator, policy/configuration) has one designated author task and the others request changes through it. The integration owner merges closure pull requests one at a time and the next author rebases and regenerates.
Unblocks: CON.19, SIM.01, SIM.05, SIM.06

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Deterministic regeneration, descriptor/tag/compatibility checks, closed-schema validators, independent positive and negative vectors in C#, TypeScript and Kotlin; Windows/Linux compilation and packaging only (P2-017).
Completion evidence for the ledger: Merged pull request, published Contracts candidate identity containing the closure, vector and compatibility results, and the operation-scope manifest rows flipped to verified for these operations.
Notes: Added so that every operation family in the operation-scope manifest has a closure task.
```

```text
Execute ArcForges delivery task CON.22 — Account support, notification, data, preference, policy-bundle and export-job operations.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\contracts.md (anchor task-con-22).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Contracts (integration owner: Contracts integration owner, the holder of roles/integration-contracts).
Claim and handoff record: claims/con-22 (python tools/delivery.py claim CON.22 --worker <name>); task branch task/con-22 in Contracts; ledger record ledger/tasks/con-22.md.
Kind/size: contract/M. Baseline: not-started.
Outcome: Support case, notification and push registration, data export request/state, preference, policy bundle and export-job status/cancel/download operations are generated with exact fields, authorization profiles and vectors in C#, TypeScript and Kotlin.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-03.05 (support.*, notification.*, data.*, preference.*, policy.getBundle and export.* operations (15), records and vectors): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\03-contract-foundation-and-licence-split.md, anchor rule-wp-03.05

Entry condition: adoption slice ADOPT.03.contracts is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [contract] CON.02: capability/action/context/resource descriptor and oversized-body reference records
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Contracts:public/proto/arcforges/*/v1/**; Contracts:fixtures/public/con-{i}-*.json; Contracts:src/public/**/Generated/**
Shared resources (follow the owner protocol): RES-contracts-generated-baseline (regenerate): Never hand-edited or hand-merged: after rebasing, the author regenerates with the pinned generator and commits the result; CI rejects drift between schemas, descriptors and generated output.; RES-contracts-publication (append): Every merge to main publishes all Contracts packages at one allocated candidate version (Maven main as SNAPSHOT under the publication-channel profile); the integration owner keeps a single merge queue so publications stay ordered; no tag, republication or replacement version is created for verification.; RES-contracts-schema-sources (append): Each closure task edits only its own domain proto or HTTP-schema files and adds its own sharded constraint and fixture files; shared inventories (package inventory, foundation inventory, constraint aggregate) are append-only per closure. A proto file with several contributing tasks (operator, policy/configuration) has one designated author task and the others request changes through it. The integration owner merges closure pull requests one at a time and the next author rebases and regenerates.
Unblocks: AND.12, CLOUD.45, CON.19, OPS.07, OPS.10, POL.09, WEB.15

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Deterministic regeneration, descriptor/tag/compatibility checks, closed-schema validators, independent positive and negative vectors in C#, TypeScript and Kotlin; Windows/Linux compilation and packaging only (P2-017).
Completion evidence for the ledger: Merged pull request, published Contracts candidate identity containing the closure, vector and compatibility results, and the operation-scope manifest rows flipped to verified for these operations.
Notes: Added so that every operation family in the operation-scope manifest has a closure task.
```

```text
Execute ArcForges delivery task CON.90 — WP03.00 — split project structure (accepted, historical).

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\contracts.md (anchor task-con-90).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Contracts (integration owner: Contracts integration owner, the holder of roles/integration-contracts).
Claim and handoff record: claims/con-90 (python tools/delivery.py claim CON.90 --worker <name>); task branch task/con-90 in Contracts; ledger record ledger/tasks/con-90.md.
Kind/size: contract/M. Baseline: accepted.
Outcome: 22 package identities (14 NuGet/5 npm/3 Maven) exist as real source-bearing projects with generators wired; native-grpc-only contracts-client retired from new publication.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-03.00 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\03-contract-foundation-and-licence-split.md, anchor rule-wp-03.00

Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- none
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Contracts:eng/contract-packages.json; Contracts:src/**; Contracts:public/**; Contracts:internal/**
Shared resources (follow the owner protocol): RES-contracts-generated-baseline (regenerate): Never hand-edited or hand-merged: after rebasing, the author regenerates with the pinned generator and commits the result; CI rejects drift between schemas, descriptors and generated output.; RES-contracts-publication (append): Every merge to main publishes all Contracts packages at one allocated candidate version (Maven main as SNAPSHOT under the publication-channel profile); the integration owner keeps a single merge queue so publications stay ordered; no tag, republication or replacement version is created for verification.; RES-contracts-schema-sources (append): Each closure task edits only its own domain proto or HTTP-schema files and adds its own sharded constraint and fixture files; shared inventories (package inventory, foundation inventory, constraint aggregate) are append-only per closure. A proto file with several contributing tasks (operator, policy/configuration) has one designated author task and the others request changes through it. The integration owner merges closure pull requests one at a time and the next author rebases and regenerates.
Unblocks: GOV.05, PRF.10

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): accepted; see docs/assurance/wp03-00-implementation-evidence.md
Completion evidence for the ledger: Contracts PR33/34/35 merged; accepted source 30ddcad2bcb3634e089abb5e29d6c9ce05d38386; published 1.0.0-ci.86.1
Notes: Historical record only, not new work.
```

```text
Execute ArcForges delivery task CON.91 — WP03.01 — foundation contract types (accepted, historical).

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\contracts.md (anchor task-con-91).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Contracts (integration owner: Contracts integration owner, the holder of roles/integration-contracts).
Claim and handoff record: claims/con-91 (python tools/delivery.py claim CON.91 --worker <name>); task branch task/con-91 in Contracts; ledger record ledger/tasks/con-91.md.
Kind/size: contract/L. Baseline: accepted.
Outcome: 148 records (32 Foundation incl. ResourceRef/ResourceVersionRef/BlobRef/ArtifactRef/ContentOrigin, 116 PublicApi incl. all 16 AggregateBody branches) generated with safe value wrappers; 476 C#/TS conformance cases pass.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-03.01 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\03-contract-foundation-and-licence-split.md, anchor rule-wp-03.01

Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- none
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Contracts:public/proto/arcforges/foundation/v1/**; Contracts:public/proto/arcforges/publicapi/v1/content.proto
Shared resources (follow the owner protocol): RES-contracts-generated-baseline (regenerate): Never hand-edited or hand-merged: after rebasing, the author regenerates with the pinned generator and commits the result; CI rejects drift between schemas, descriptors and generated output.; RES-contracts-publication (append): Every merge to main publishes all Contracts packages at one allocated candidate version (Maven main as SNAPSHOT under the publication-channel profile); the integration owner keeps a single merge queue so publications stay ordered; no tag, republication or replacement version is created for verification.; RES-contracts-schema-sources (append): Each closure task edits only its own domain proto or HTTP-schema files and adds its own sharded constraint and fixture files; shared inventories (package inventory, foundation inventory, constraint aggregate) are append-only per closure. A proto file with several contributing tasks (operator, policy/configuration) has one designated author task and the others request changes through it. The integration owner merges closure pull requests one at a time and the next author rebases and regenerates.
Unblocks: AST.01, CLOUD.01, CLOUD.21, CLOUD.23, CLOUD.37, CON.02, FND.01, FND.02, FND.03, FND.05, FND.07, NOTES.01, NOTES.02, NOTES.07, NOTES.12, NOTES.18, NOTES.20, NOTES.23, NOTES.24, PLT.17, PLT.19, PRF.01, PRF.02, PRF.03, SCOPE.01, SCOPE.02, SCOPE.14

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): accepted; see docs/assurance/wp03-01-implementation-evidence.md
Completion evidence for the ledger: Contracts PR36 merged as 4b8134eaf8a4174922d6378da003ed390b85a94a; published 1.0.0-ci.89.1
Notes: Historical record. IMPORTANT: this substep's dependency-closure side effect already generated ResourceRef/ResourceVersionRef/BlobRef/ArtifactRef — WP03.03 does not need to invent these, only add capability/action/context/health descriptors, the Sync mutation allowlist validator, and EncodedBodyRef (still absent).
```

```text
Execute ArcForges delivery task CON.92 — WP03.02 — serialization posture (accepted, historical).

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\contracts.md (anchor task-con-92).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Contracts (integration owner: Contracts integration owner, the holder of roles/integration-contracts).
Claim and handoff record: claims/con-92 (python tools/delivery.py claim CON.92 --worker <name>); task branch task/con-92 in Contracts; ledger record ledger/tasks/con-92.md.
Kind/size: contract/M. Baseline: accepted.
Outcome: Google.Protobuf/protobuf-es are the only business serializers; decode limits (4MiB/256KiB/32KiB/64MiB), strict HTTP-exception JSON codecs, explicit service catalogues, forbidden-serializer policy gate and a test-only Native AOT probe (13 libraries, Linux CI + Windows local) all pass.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-03.02 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\03-contract-foundation-and-licence-split.md, anchor rule-wp-03.02

Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- none
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Contracts:eng/check_serialization.py; Contracts:tests/public/SerializationProbe/**
Shared resources (follow the owner protocol): RES-contracts-generated-baseline (regenerate): Never hand-edited or hand-merged: after rebasing, the author regenerates with the pinned generator and commits the result; CI rejects drift between schemas, descriptors and generated output.; RES-contracts-publication (append): Every merge to main publishes all Contracts packages at one allocated candidate version (Maven main as SNAPSHOT under the publication-channel profile); the integration owner keeps a single merge queue so publications stay ordered; no tag, republication or replacement version is created for verification.; RES-contracts-schema-sources (append): Each closure task edits only its own domain proto or HTTP-schema files and adds its own sharded constraint and fixture files; shared inventories (package inventory, foundation inventory, constraint aggregate) are append-only per closure. A proto file with several contributing tasks (operator, policy/configuration) has one designated author task and the others request changes through it. The integration owner merges closure pull requests one at a time and the next author rebases and regenerates.
Unblocks: CON.17, PRF.05, PRF.07, PRF.08

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): accepted; see docs/assurance/wp03-02-implementation-evidence.md
Completion evidence for the ledger: Contracts PR37 merged as e6c4a77f3ba48d70de4bf524623985b29278c784 (= current HEAD); published 1.0.0-ci.92.1
Notes: This is Contracts' current HEAD. Every task below starts from this baseline. Both the Contracts repo's own docs/wp03-02-serialization.md and Design's evidence doc independently state '03.03 is next and has not started' — and no artifact anywhere (git log --all, all.worktree dirs, gh pr list --state all, fixtures/ directory contents, proto message/service inventory) contradicts that..
```
