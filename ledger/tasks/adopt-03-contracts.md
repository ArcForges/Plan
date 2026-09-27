---
task: ADOPT.03.contracts
status: complete
recorded: 2026-09-27
claimant: w-20260927-contracts-lane
epoch: 1
---

# Contracts schema adoption

## Evidence and ordered review

Reviewed the frozen [ADOPT.01 baseline](../adoption/baseline.md#contracts), then the task outcomes, mapped WP03 obligations, accepted receipts, source inventories, authored schemas and fixture inventory before recording classifications. This ledger-only review does not perform source cleanup or accept future product behavior.

- Frozen Contracts source: `b10b2f6f316bf0c007e00632c5442fc102ebbe6e`; Design authority: `722e85641c8afb765dafcab5bc0e84d5a22d5a3c`.
- [Frozen source inventory](https://github.com/ArcForges/Contracts/tree/b10b2f6f316bf0c007e00632c5442fc102ebbe6e): authored services are only HelloService.SayHello and ExtensionHostService.RenewLease. No descriptor closure, EncodedBodyRef, ScopeProjectMetadata, complete operation catalogue or con-* vectors exists. Public/internal constraint files remain monolithic. HTTP schemas supply PartReceipt, inventory and CommitReceipt seeds only.
- Accepted receipts at the Design authority: [WP03.00](https://github.com/ArcForges/ArcForges-Design/blob/722e85641c8afb765dafcab5bc0e84d5a22d5a3c/docs/assurance/wp03-00-implementation-evidence.md), [WP03.01](https://github.com/ArcForges/ArcForges-Design/blob/722e85641c8afb765dafcab5bc0e84d5a22d5a3c/docs/assurance/wp03-01-implementation-evidence.md), [WP03.02](https://github.com/ArcForges/ArcForges-Design/blob/722e85641c8afb765dafcab5bc0e84d5a22d5a3c/docs/assurance/wp03-02-implementation-evidence.md). Their individual inherited records are [CON.90](con-90.md), [CON.91](con-91.md), [CON.92](con-92.md).
- Frozen main [CI 36334951174](https://github.com/ArcForges/Contracts/actions/runs/36334951174) and [Security 36334951206](https://github.com/ArcForges/Contracts/actions/runs/36334951206) succeeded. Baseline retains original registry receipts for all 14 NuGet / five npm packages at `1.0.0-ci.113.1`, three Maven coordinates through `1.0.0-SNAPSHOT`, bound to that source and original candidate. Mutable Maven label alone is not an immutable pin.
- Intervening commits after accepted serialization contain instruction alignment and dependency updates, not later contract closures. No open PR existed at freeze; unmerged branches do not count as accepted work.

## Actual layout and classifications

Paths below are relative to Contracts. Generated bindings use existing owners in `eng/contract-packages.json`: `src/public/dotnet`, `src/internal/dotnet`, `src/public/ts/{proto,api-client,contract-fixtures}`, `src/internal/ts/{ai-internal,operator-client}` and `src/public/kotlin`. New schema/project/lock/inventory additions must follow the task's declared write scope and generator ownership; these bindings do not expand that scope or authorize package renames. Every row cites the frozen source inventory above; inherited rows additionally cite their own accepted receipt. All remaining outcomes retain their exact task obligation, vector and evidence requirements.

|Task|Classification|Bound authored scope / existing evidence|Remaining scope|
|---|---|---|---|
|CON.01|gap|eng/contracts.py; existing public/proto/constraints.json and internal/proto/constraints.json; new constraints/** and CONTRIBUTING.md|Shard effective constraints unchanged after CON.23; generation support and append/merge protocol evidence.|
|CON.02|gap|public/proto/arcforges/foundation/v1/foundation.proto; new descriptor shard and fixtures/public/con-02-descriptors.json|All descriptors, EncodedBodyRef, decode boundary and independent vectors. Reuse CON.91 reference types.|
|CON.03|gap|public/proto/arcforges/publicapi/v1/content.proto; constraints; new con-03 vectors|ScopeProjectMetadata, additive carrier, closed Sync admission and all named negatives; existing AggregateBody is scaffolding, not admission proof.|
|CON.04|gap|internal/proto/arcforges/local/sandbox/v1/sandbox.proto; existing LocalRpc.Sandbox package; new fixtures/internal/con-04-content-sandbox.json|Complete15 methods and direction/identity/registration negatives.|
|CON.05|inherited with adjustment|public/proto/arcforges/extensions/v1/extensions.proto already has accepted RenewLease; internal/proto/arcforges/local/platform/v1/platform.proto|Remaining ExtensionHost methods, bootstrap/connector closure, reserved removed names and con-05 negatives; RenewLease reuse does not accept full helper semantics.|
|CON.06|gap|internal/proto/arcforges/local/{chat,scope}/v1/*.proto; existing LocalRpc.Chat/Scope packages|Full in-process ports and infrastructure ports, knowledge policy/consent boundaries, con-06 vectors. Existing seed values do not satisfy outcome.|
|CON.07|gap|new public/proto/arcforges/publicapi/v1/identity.proto; existing public/http/v1/schema.json|Identity/workspace/device full operation closure, native auth/browser exceptions and three-language vectors.|
|CON.08|gap|new public/proto/arcforges/publicapi/v1/commerce.proto|Entitlement/commerce closure and con-08 vectors.|
|CON.09|gap|new public/proto/arcforges/publicapi/v1/{sync,transfer}.proto|Sync/resource/object/realm transfer operations and vectors; wait CON.03.|
|CON.10|gap|new public/proto/arcforges/publicapi/v1/chat.proto; existing internal/ai-http/v1/schema.json|Task/approval/bridge/chat/agent/automation/search and AI internal closure, knowledge policy, positive/negative vectors.|
|CON.11|gap|new public/proto/arcforges/publicapi/v1/application.proto; existing events/v1/events.proto|13 additions, EventService Poll/Watch and typed stream/hint vectors.|
|CON.12|gap|existing public/http/v1/schema.json and internal/ai-http/v1/schema.json|Complete manifest/workflow/panel/policy/configuration20 sections and vectors; receipt schemas do not prove these formats.|
|CON.13|gap|new public/proto/arcforges/catalog/v1/catalog.proto|7 Catalog operations, records and vectors.|
|CON.14|gap|existing internal/proto/arcforges/operator/v1/operator.proto; CloudInternal and operator-client owners|Full OperatorService, authorization fields/role matrix and negatives; no authored service exists.|
|CON.15|gap|existing internal/ai-http/v1/schema.json|Remaining objects/AI/inference/deletion/session/backup HTTP ports and vectors; preserve CON.10 ownership.|
|CON.16|gap|new public/http/v1/signed-formats.schema.json and con-16 vectors|Four signed formats, canonical vectors and fixture-only trust roots.|
|CON.17|gap|new eng/check_compatibility.py, tests/tooling/test_compatibility_matrix.py, con-17 vectors|Supported-version matrix and canonical semantic hash; reuse exact values/unknown-field codec but accepted codecs are not compatibility-window evidence.|
|CON.18|gap|new eng/check_operation_scope.py and eng/operation-scope-manifest.json|Reachability generator and complete authorization classification with fail-closed policy tests.|
|CON.19|gap|new docs/wp03-90-verification.md; artifacts/contracts/**|Full owned producer stage closure and six completion gates, excluding CON.15; do not infer stage completion from existing package publication.|
|CON.21|gap|new simulation schema under public/proto/arcforges/publicapi/v1; existing package owner|13 simulation operations incl. paginated authorized listRuns, vectors and verified manifest rows.|
|CON.22|gap|new account/support/notification schemas under public/proto/arcforges/publicapi/v1; existing package owner|15 selected operations, authorization, vectors and verified manifest rows.|
|CON.23|inherited with adjustment|eng/policy/product-names.json; foundation/content protos; internal/local/{notes,slate}; corresponding LocalRpc packages; actual inventories, constraints, fixtures, solution and generated owners|Retire outside-family names/packages/types with exact wire reservations; preserve immutable historical packages. Known planned retirement under ADP-10/P2-019/P2-020, not a new architecture conflict. GOV.18 required for completion binding.|
|CON.24|gap|new public/proto/arcforges/publicapi/v1/scope.proto; content.proto summaries only|ScopeService3 read operations and summaries from CON.03 metadata, authorized snapshot/count/pagination vectors and generated3-language evidence.|
|CON.90|inherited|eng/contract-packages.json; source-bearing public/internal project split; accepted WP03.00 receipt|None within accepted historical boundary; subsequent retirements owned solely by CON.23.|
|CON.91|inherited|foundation.proto/content.proto; foundation inventory/baseline; wp03-01 vectors; accepted receipt|None within accepted historical boundary; descriptors/Sync/ScopeProjectMetadata remain CON.02/03, retirement CON.23.|
|CON.92|inherited|eng/check_serialization.py; tests/public/SerializationProbe; generated strict codecs and service catalogues; wp03-02 vectors|None within accepted historical boundary; real AOT generated-client call remains PRF owner, not inherited.|


## Conflicts, blockers and validation boundary

No unresolved architecture conflict was found. Outside-family Notes/Slate bindings are retired pending CON.23 under ADP-10/P2-019/P2-020. Their continued presence is an approved migration input, not completed cleanup; exact wire reservations and immutable publications must be preserved. CON.23 completion waits for GOV.18's forbidden-alias re-export. Every other task keeps its graph prerequisites; this record creates no repository-wide barrier.

Only CON.90–CON.92 are inherited, each with its own record. CON.05 and CON.23 retain concrete adjustments and receive no inherited completion record. The other 21 nonhistorical tasks are gaps. The 23 open tasks become eligible according to their individual prerequisites after this slice merges.

Validation: inspected merged source, accepted receipt evidence, actual schema/service and fixture inventories, and history; ledger consistency checked with explicit Plan worktree and current Design roots. No new build, runtime, consumer, package download, hash-audit, device, browser, live-service or inference cycle. Historical C#/TS and AOT evidence is reused only within its accepted scope; Kotlin compilation is not three-language behavioral conformance. No substitute proves an owner or commercial scenario.

The ledger PR's exact reviewed head and merge commit are retained in the ADOPT.03.contracts claim and PR review/merge history; no implementation PR is produced by this slice.
