# ArcForges delivery task prompts — Extension platform and integrations

Generated from Design `docs/planning/delivery/delivery-graph.json` by `tools/delivery.py`; do not edit by hand.
Each block is self-contained. Claim a task only when `python tools/delivery.py ready` lists it, with
`python tools/delivery.py claim <TASK-ID> --worker <name>`, then follow `arcforges-implementation.md`.
Tasks are ordered by lane for reading; the order is not a schedule.

## Extension platform and integrations

```text
Execute ArcForges delivery task EXT.00 — Extension host process and supervision.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\extensions.md (anchor task-ext-00).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/ext-00 (python tools/delivery.py claim EXT.00 --worker <name>); task branch task/ext-00 in DesktopPlatform; ledger record ledger/tasks/ext-00.md.
Kind/size: producer/L. Baseline: not-started.
Outcome: Per-installation extension processes start on demand and stop when idle inside the package-specific OS isolation profile; resource limits are enforced by termination, crashes trigger backoff restart then quarantine, in-flight invocations fail typed, and no ambient credential is inherited.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-41.00 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\41-extension-platform-and-integrations.md, anchor rule-wp-41.00

Entry condition: adoption slice ADOPT.02.extensions is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] PLT.45: the OS-level process isolation / ContentSandbox primitives (broker grants, syscall restriction)
- [contract] PLT.19: the typed capability/resource contribution model
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:src/Extensions/ArcForges.Extensions.Runtime/Host/**
Unblocks: EXT.01, EXT.09, EXT.90

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Hostile-package tests against product DB/token paths, network, sibling-package and process APIs on the real target OS per platform (Windows primary; no macOS CI per P2-017); crash/hang/memory-exhaustion/unbounded-output tests; quarantine behaviour; credential-absence assertion. No device/emulator CI -- these run as local/affected-scope checks per P2-017.
Completion evidence for the ledger: Hostile-process behaviour and credential-absence results (PG-22).
Notes: Narrow early risk proof: if real OS-level sandboxing cannot reach PG-22's bar on the target platforms, the whole out-of-process extension model needs redesign.
```

```text
Execute ArcForges delivery task EXT.01 — Handshake and protocol versioning.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\extensions.md (anchor task-ext-01).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/ext-01 (python tools/delivery.py claim EXT.01 --worker <name>); task branch task/ext-01 in DesktopPlatform; ledger record ledger/tasks/ext-01.md.
Kind/size: producer/M. Baseline: not-started.
Outcome: Identity is verified against the installed manifest before any contribution is invoked; more than one protocol version is negotiated during a migration window; impersonation and reserved-namespace claims are refused with a clean explanation.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-41.01 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\41-extension-platform-and-integrations.md, anchor rule-wp-41.01

Entry condition: adoption slice ADOPT.02.extensions is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] EXT.00: a running extension process to handshake with
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:src/Extensions/ArcForges.Extensions.Runtime/Handshake/**
Unblocks: EXT.90

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Impersonation and reserved-namespace negative tests; version-negotiation matrix including refusal -- offline/local, no live device needed.
Completion evidence for the ledger: Impersonation, namespace and negotiation results.
```

```text
Execute ArcForges delivery task EXT.02 — Dual capability boundary (typed layer + closed dynamic value model).

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\extensions.md (anchor task-ext-02).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Contracts (integration owner: Contracts integration owner, the holder of roles/integration-contracts).
Claim and handoff record: claims/ext-02 (python tools/delivery.py claim EXT.02 --worker <name>); task branch task/ext-02 in Contracts; ledger record ledger/tasks/ext-02.md.
Kind/size: producer/L. Baseline: not-started.
Outcome: The typed extension-point layer exists as ordinary versioned contracts and the dynamic layer as the closed, AOT-safe StructuredValue/ValueSchema model with bidirectional validation; a repository policy test proves StructuredValue never appears in a first-party domain or product contract, and the host still publishes AOT cleanly.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-41.02 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\41-extension-platform-and-integrations.md, anchor rule-wp-41.02

Entry condition: adoption slice ADOPT.03.extensions is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [contract] CON.05: the published foundation/value-model proto types this layer extends
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Contracts:public/proto/arcforges/extensions/v1/**; DesktopPlatform:src/Extensions/ArcForges.Extensions.Contracts/**
Shared resources (follow the owner protocol): RES-contracts-schema-sources (append): Each closure task edits only its own domain proto or HTTP-schema files and adds its own sharded constraint and fixture files; shared inventories (package inventory, foundation inventory, constraint aggregate) are append-only per closure. A proto file with several contributing tasks (operator, policy/configuration) has one designated author task and the others request changes through it. The integration owner merges closure pull requests one at a time and the next author rebases and regenerates.
Unblocks: EXT.03, EXT.04, EXT.08, EXT.90, SCOPE.25

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Value-model coverage per type; bidirectional validation tests; containment policy test with a negative fixture; an AOT publish with the platform present (native AOT compile check, permitted under P2-017).
Completion evidence for the ledger: Value-model, validation, containment and AOT results.
Notes: WP-41 Sec.1 names the AOT-vs-dynamic-value tension as 'the platform's hardest design problem' -- narrow early risk proof.
```

```text
Execute ArcForges delivery task EXT.03 — Declarative UI and settings contribution.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\extensions.md (anchor task-ext-03).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/ext-03 (python tools/delivery.py claim EXT.03 --worker <name>); task branch task/ext-03 in DesktopPlatform; ledger record ledger/tasks/ext-03.md.
Kind/size: producer/M. Baseline: not-started.
Outcome: Panel declarations from a closed, versioned element vocabulary render with first-party controls; settings schemas are declarative; secret fields yield references only; extension-contributed surfaces are visibly attributed.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-41.03 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\41-extension-platform-and-integrations.md, anchor rule-wp-41.03

Entry condition: adoption slice ADOPT.02.extensions is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] EXT.02: the closed StructuredValue/panel.v1 schema
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:src/Extensions/ArcForges.Extensions.Runtime/DeclarativeUi/**
Unblocks: EXT.90

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Vocabulary coverage tests; negative test for raw markup/script rejection; secret-field test; attribution test -- all offline UI-layer tests.
Completion evidence for the ledger: Vocabulary, markup-rejection, secret and attribution results.
```

```text
Execute ArcForges delivery task EXT.04 — Package manifest/workflow/panel validators and lifecycle state machine.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\extensions.md (anchor task-ext-04).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Contracts (integration owner: Contracts integration owner, the holder of roles/integration-contracts).
Claim and handoff record: claims/ext-04 (python tools/delivery.py claim EXT.04 --worker <name>); task branch task/ext-04 in Contracts; ledger record ledger/tasks/ext-04.md.
Kind/size: producer/M. Baseline: not-started.
Outcome: manifest.v1/workflow.v1/panel.v1 validators exist from published Contracts, and package installation moves only through the immutable staged states (acquired/verified/staged/awaitingConsent/active/disabled/quarantined/removed) with no state that resets an effect fence.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-41.04 (manifest.v1/workflow.v1/panel.v1 validators and the immutable staged install/update/drain/migration/revocation/rollback state machine): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\41-extension-platform-and-integrations.md, anchor rule-wp-41.04

Entry condition: adoption slice ADOPT.03.extensions is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] EXT.02: the closed value model workflow.v1 nodes are typed against
- [artifact] CON.16: WP-03 fixture signing/catalog keys (catalog/index/revocation/update/realm schemas + independent signed vectors)
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Contracts:public/proto/arcforges/extensions/v1/**; DesktopPlatform:src/Extensions/ArcForges.Extensions.Packaging/Lifecycle/**
Shared resources (follow the owner protocol): RES-contracts-schema-sources (append): Each closure task edits only its own domain proto or HTTP-schema files and adds its own sharded constraint and fixture files; shared inventories (package inventory, foundation inventory, constraint aggregate) are append-only per closure. A proto file with several contributing tasks (operator, policy/configuration) has one designated author task and the others request changes through it. The integration owner merges closure pull requests one at a time and the next author rebases and regenerates.
Permitted substitutes (never real integration evidence): SUB-signed-format-fixture-keys: signature/hash verification mechanics, expired/revoked/unknown-key refusal, malformed/rollback/mixed-shard handling Real producer ['UPD.07']; removed by REL.11
Unblocks: EXT.05, EXT.90

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Archive traversal/size/signature tests, DAG bounds (maxItems<=100, nesting<=2, 256 expanded steps), increased-permission re-consent, active-old-job, private-state rollback incompatibility, unknown-effect tests -- all offline against fixture-signed archives.
Completion evidence for the ledger: Lifecycle matrix, re-consent, uninstall and revoke results (part).
```

```text
Execute ArcForges delivery task EXT.05 — Six contribution-kind runtime wiring.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\extensions.md (anchor task-ext-05).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/ext-05 (python tools/delivery.py claim EXT.05 --worker <name>); task branch task/ext-05 in DesktopPlatform; ledger record ledger/tasks/ext-05.md.
Kind/size: producer/L. Baseline: not-started.
Outcome: Each of the six contribution kinds registers and executes through the lifecycle engine and the dual capability boundary; a running task freezes the package version it started with (BR-10); uninstall never cascade-deletes professional resources the extension created (BR-11).

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-41.04 (the six package contribution kinds (skill/template/workflow/mcp/connector/extension) runtime registration and execution wiring): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\41-extension-platform-and-integrations.md, anchor rule-wp-41.04

Entry condition: adoption slice ADOPT.02.extensions is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] EXT.04: the lifecycle state machine to register kinds into
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:src/Extensions/ArcForges.Extensions.Registry/Contributions/**
Unblocks: EXT.90

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Per-kind lifecycle tests; version-freeze-during-running-task test; uninstall-preserves-resources test -- offline.
Completion evidence for the ledger: Lifecycle matrix, re-consent, uninstall and revoke results (remainder).
```

```text
Execute ArcForges delivery task EXT.06 — Cloud PackageCatalog producer.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\extensions.md (anchor task-ext-06).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/ext-06 (python tools/delivery.py claim EXT.06 --worker <name>); task branch task/ext-06 in Cloud; ledger record ledger/tasks/ext-06.md.
Kind/size: producer/L. Baseline: not-started.
Outcome: Cloud PackageCatalog accepts immutable submissions with DNS publisher verification, holds review-state/revocation authority and produces a signed static index; only OperatorService (not the console or the Extensions implementation) writes PackageCatalog tables.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-41.05 (Cloud PackageCatalog producer: DNS publisher verification, immutable submissions, review-state/revocation authority, signed static index): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\41-extension-platform-and-integrations.md, anchor rule-wp-41.05
- WP-41:packagecatalog-ownership-paragraph-sec-5 PackageCatalog ownership paragraph (Sec.5-6 boundary): OperatorService is sole authenticator/caller; neither Extensions Runtime nor console writes PackageCatalog tables (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\41-extension-platform-and-integrations.md, package-level obligation

Entry condition: adoption slice ADOPT.07.extensions is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] CLOUD.16: publisher identity/PAT and operator authentication
- [artifact] CLOUD.42: durable blob storage for submitted package archives
- [artifact] CON.16: WP-03 fixture catalog/index/revocation/update/realm schemas and signed vectors
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Cloud:src/Modules/PackageCatalog/PackageCatalog.Domain/**; Cloud:src/Modules/PackageCatalog/PackageCatalog.Application/**; Cloud:src/Modules/PackageCatalog/PackageCatalog.Infrastructure/**
Shared resources (follow the owner protocol): RES-cloud-host-composition (append): Each module registers through its own module entry point and route fragment; the host composition only lists modules; route and binding conflicts are resolved by the integration owner at merge.
Unblocks: EXT.07, EXT.08, EXT.90, OPS.11

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Owner/PAT/operator separation, duplicate-version conflict, invalid archive, review/revoke replay, signed-index rollback/expiry, offline installed-package behavior -- Cloud integration tests against ephemeral D1, no live DNS/public network in CI.
Completion evidence for the ledger: Hostile catalog and unreachable-catalog results.
```

```text
Execute ArcForges delivery task EXT.07 — Desktop and CLI catalog consumers.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\extensions.md (anchor task-ext-07).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/ext-07 (python tools/delivery.py claim EXT.07 --worker <name>); task branch task/ext-07 in DesktopPlatform; ledger record ledger/tasks/ext-07.md.
Kind/size: producer/M. Baseline: not-started.
Outcome: Desktop and CLI consume the signed static index and PackageCatalog methods to install/update packages, with correct offline behavior when the catalog is unreachable.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-41.05 (desktop/CLI catalog consumers): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\41-extension-platform-and-integrations.md, anchor rule-wp-41.05

Entry condition: adoption slice ADOPT.02.extensions is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] EXT.06: the real signed static index format and PackageCatalog API
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:src/Extensions/ArcForges.Extensions.Registry/CatalogClient/**
Unblocks: EXT.90

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Catalog-unavailable-never-disables-installed-packages test; signed-index rollback/expiry consumption test -- offline.
Completion evidence for the ledger: Hostile catalog and unreachable-catalog results (consumer half).
Notes: WP-45 (the commerce, policy and operations lanes OPS review console) is a downstream consumer of these same EXT.06/07 methods -- noted for integration owner cross-check, not a completion blocker here.
```

```text
Execute ArcForges delivery task EXT.08 — Public SDK and CLI.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\extensions.md (anchor task-ext-08).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Contracts (integration owner: Contracts integration owner, the holder of roles/integration-contracts).
Claim and handoff record: claims/ext-08 (python tools/delivery.py claim EXT.08 --worker <name>); task branch task/ext-08 in Contracts; ledger record ledger/tasks/ext-08.md.
Kind/size: producer/M. Baseline: not-started.
Outcome: The SDK, validators and tool-payload projections generate from authored public proto; the CLI uses eligible publisher PAT and catalog/resource methods; validate matches host install checks; no generated schema is inferred from C# reflection.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-41.06 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\41-extension-platform-and-integrations.md, anchor rule-wp-41.06
- WP-41:sec-8-gate-item-8-mcp-vocabulary-mapping Sec.8 gate item 8: MCP vocabulary mapping + SDK version pin -- VG-02 (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\41-extension-platform-and-integrations.md, package-level obligation

Entry condition: adoption slice ADOPT.03.extensions is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] EXT.02: the published extension protocol/value-model proto to generate from
- [artifact] CLOUD.16: publisher PAT issuance
Completion prerequisites (may start earlier; cannot complete before these are complete):
- [integration] EXT.06: the real Cloud PackageCatalog submit endpoint

Permitted write scope: Contracts:src/SDK/ArcForges.SDK.*/**; Contracts:src/SDK/ArcForges.Cli/**
Shared resources (follow the owner protocol): RES-contracts-schema-sources (append): Each closure task edits only its own domain proto or HTTP-schema files and adds its own sharded constraint and fixture files; shared inventories (package inventory, foundation inventory, constraint aggregate) are append-only per closure. A proto file with several contributing tasks (operator, policy/configuration) has one designated author task and the others request changes through it. The integration owner merges closure pull requests one at a time and the next author rebases and regenerates.
Unblocks: EXT.90

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Independent SDK consumer test, manifest/tag compatibility, PAT scope tests, generated-vs-reflection negative test -- offline codegen tests.
Completion evidence for the ledger: Generator, validate-parity and first-party build results.
```

```text
Execute ArcForges delivery task EXT.09 — Local MCP stdio behind the owned connector child.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\extensions.md (anchor task-ext-09).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/ext-09 (python tools/delivery.py claim EXT.09 --worker <name>); task branch task/ext-09 in DesktopPlatform; ledger record ledger/tasks/ext-09.md.
Kind/size: producer/M. Baseline: not-started.
Outcome: Local MCP servers run stdio behind an owned connector child process; only that child speaks ArcForges gRPC; origin/scope changes invalidate consent; no browser/Android local subprocess exists; child crash/lease recovery works.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-41.07 (local MCP stdio placement behind the owned connector child process): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\41-extension-platform-and-integrations.md, anchor rule-wp-41.07
- WP-41:sec-8-gate-item-8-mcp-vocabulary-mapping Sec.8 gate item 8: MCP vocabulary mapping + SDK version pin -- VG-02 (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\41-extension-platform-and-integrations.md, package-level obligation

Entry condition: adoption slice ADOPT.02.extensions is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] EXT.00: the extension host's process supervision primitives
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:src/Communication/Mcp/**
Unblocks: EXT.90

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Origin/scope-change consent invalidation test; no-unrestricted-AI-fetch test; child crash/lease recovery test -- offline/local process tests.
Completion evidence for the ledger: MCP mapping record, connector secret and no-delegation structural results (local half).
```

```text
Execute ArcForges delivery task EXT.10 — Cloud MCP HTTP through the AI Worker adapter.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\extensions.md (anchor task-ext-10).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\AI (integration owner: AI integration owner, the holder of roles/integration-ai).
Claim and handoff record: claims/ext-10 (python tools/delivery.py claim EXT.10 --worker <name>); task branch task/ext-10 in AI; ledger record ledger/tasks/ext-10.md.
Kind/size: producer/M. Baseline: not-started.
Outcome: Cloud-placed MCP connections route HTTP through the AI Worker adapter only; standard MCP protocol is preserved; each connection has one placement/secret owner and exact failure/egress behavior; MCP content is treated as untrusted data.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-41.07 (Cloud MCP HTTP placement through the AI Worker adapter): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\41-extension-platform-and-integrations.md, anchor rule-wp-41.07
- WP-41:sec-8-gate-item-8-mcp-vocabulary-mapping Sec.8 gate item 8: MCP vocabulary mapping + SDK version pin -- VG-02 (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\41-extension-platform-and-integrations.md, package-level obligation

Entry condition: adoption slice ADOPT.08.extensions is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [contract] CON.15: the internal AI HTTP port surface to attach an MCP adapter route to
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: AI:src/mcp/**
Unblocks: EXT.90

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Standard-MCP-transport preservation test; secret-as-reference test; egress-control test -- offline against a local MCP fixture server, no live external MCP endpoint in CI.
Completion evidence for the ledger: MCP mapping record, connector secret and no-delegation structural results (Cloud half).
```

```text
Execute ArcForges delivery task EXT.90 — Verify owned artifact and real integration (extension platform).

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\extensions.md (anchor task-ext-90).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/ext-90 (python tools/delivery.py claim EXT.90 --worker <name>); task branch task/ext-90 in DesktopPlatform; ledger record ledger/tasks/ext-90.md.
Kind/size: producer/M. Baseline: not-started.
Outcome: SDK/protocol, desktop host/runtime and Cloud registry ownership are verified split correctly; standard MCP transports and out-of-process extensions are preserved; no external-agent delegation or in-process third-party plugin exists anywhere; VG-02 and PG-09 close.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-41.90 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\41-extension-platform-and-integrations.md, anchor rule-wp-41.90
- WP-41:sec-8-gate-item-9-extension-protocol-con Sec.8 gate item 9: extension protocol conformance suite -- PG-09 (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\41-extension-platform-and-integrations.md, package-level obligation

Entry condition: adoption slice ADOPT.02.extensions is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] EXT.00: all prior EXT tasks complete (EXT.00-EXT.10)
- [artifact] EXT.01: package task delivered
- [artifact] EXT.02: package task delivered
- [artifact] EXT.03: package task delivered
- [artifact] EXT.04: package task delivered
- [artifact] EXT.05: package task delivered
- [artifact] EXT.06: package task delivered
- [artifact] EXT.07: package task delivered
- [artifact] EXT.08: package task delivered
- [artifact] EXT.09: package task delivered
- [artifact] EXT.10: package task delivered
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:tests/McpAotTests/**; DesktopPlatform:tests/ExtensionPlatformTests/**
Unblocks: REL.06

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): SDK licence/protocol compatibility, capability checks, hostile-extension/process isolation and owner execution tests; local gRPC closure suite (extension host<->child real generated gRPC roles, ConnectorBroker consent/secret rotation/revocation, forged-identity/direct-SSO-access denial).
Completion evidence for the ledger: Owned artifact and real-integration receipt; PG-09 protocol conformance suite pass; VG-02 MCP vocabulary mapping + SDK version pin record.
```
