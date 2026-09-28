# ArcForges delivery task prompts — Extension platform and integrations

Generated from Design `docs/planning/delivery/delivery-graph.json` by `tools/delivery.py`; do not edit by hand.
Each block is self-contained. Claim a task only when `python tools/delivery.py ready` lists it, with
`python tools/delivery.py claim <TASK-ID> --worker <name>`, then follow `arcforges-implementation.md`.
Tasks are ordered by lane for reading; the order is not a schedule.

## Extension platform and integrations

```text
Execute ArcForges delivery task EXT.00 — Extension host process and supervision.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\extensions.md (anchor task-ext-00).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/ext-00 (python tools/delivery.py claim EXT.00 --worker <name>); task branch task/ext-00 in DesktopPlatform; ledger record ledger/tasks/ext-00.md.
Kind/size: producer/L. Baseline: not-started.
Outcome: Per-installation extension processes start on demand and stop when idle inside the package-specific OS isolation profile; resource limits are enforced by termination, crashes trigger backoff restart then quarantine, in-flight invocations fail typed, and no ambient credential is inherited.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-41.00 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\41-extension-platform-and-integrations.md, anchor rule-wp-41.00

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

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\extensions.md (anchor task-ext-01).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/ext-01 (python tools/delivery.py claim EXT.01 --worker <name>); task branch task/ext-01 in DesktopPlatform; ledger record ledger/tasks/ext-01.md.
Kind/size: producer/M. Baseline: not-started.
Outcome: Identity is verified against the installed manifest before any contribution is invoked; more than one protocol version is negotiated during a migration window; impersonation and reserved-namespace claims are refused with a clean explanation.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-41.01 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\41-extension-platform-and-integrations.md, anchor rule-wp-41.01

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

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\extensions.md (anchor task-ext-02).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Contracts (integration owner: Contracts integration owner, the holder of roles/integration-contracts).
Claim and handoff record: claims/ext-02 (python tools/delivery.py claim EXT.02 --worker <name>); task branch task/ext-02 in Contracts; ledger record ledger/tasks/ext-02.md.
Kind/size: producer/L. Baseline: not-started.
Outcome: The typed extension-point layer exists as ordinary versioned contracts and the dynamic layer as the closed, AOT-safe StructuredValue/ValueSchema model with bidirectional validation; a repository policy test proves StructuredValue never appears in a first-party domain or product contract, and the host still publishes AOT cleanly.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-41.02 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\41-extension-platform-and-integrations.md, anchor rule-wp-41.02

Entry condition: adoption slice ADOPT.03.extensions is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [contract] CON.05: the published foundation/value-model proto types this layer extends
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Contracts:public/proto/arcforges/extensions/v1/**; Contracts:public/proto/constraints/ext-02-dual-capability.json (only EXT.02-authored new messages); Contracts:public/proto/constraints.json (regenerated from the EXT.02-owned shard; preserve all other shards); Contracts:.gitleaks.toml (only exact-path-and-digest generic-api-key exceptions for the six observed input-hash lines described below); Contracts:tests/StructureTests/ExtensionBoundaryCases.cs (negative containment test for StructuredValue in first-party domain/product contracts); Contracts:tests/StructureTests/Fixtures/structured-value-first-party-domain.proto (task-owned negative test fixture only); Contracts:tests/StructureTests/Program.cs (register exactly ExtensionBoundaryCases.Run(root) in the existing console runner only); Contracts:tests/tooling/test_dependency_admission.py (only positive and negative tests for the task's exact path-plus-digest Gitleaks exception boundary); DesktopPlatform:Directory.Packages.props (only pin the existing ArcForges.Contracts.PublicApi and ArcForges.Sdk.Contracts packages to the exact candidates published by this task's Contracts stage); DesktopPlatform:DesktopPlatform.slnx (only register the task-owned product, Tests and AotProbe projects); DesktopPlatform:.github/workflows/package-validation.yml (only build, test and AOT-compile steps for this task's projects); DesktopPlatform:src/Extensions/ArcForges.Extensions.Contracts/** (product plus nested Tests/AotProbe only); DesktopPlatform:eng/policy/architecture-projects.json (task-owned project rows only); DesktopPlatform:eng/policy/architecture-contract-tests.json (task-owned public-API-to-actual-test rows only); DesktopPlatform:eng/policy/dependency-policy.json and eng/policy/dependency-reviews/ext-02-r1.json (task-owned inputs and immutable admission receipt only; record the exact PublicApi and Sdk.Contracts candidates from the same Contracts merge, preserve all other coordinates/versions and the existing transitive, xunit and TestSdk closure); DesktopPlatform:eng/policy/licence-boundary.json (task-owned project/test classifications only); DesktopPlatform:eng/policy/runtime-ownership.json (task-owned extension project row only); DesktopPlatform:eng/policy/reconciliation/active-projects.json, eng/policy/reconciliation/project-updates.json and eng/policy/reconciliation/source.json (task-owned active project/update/source rows only; preserve history); DesktopPlatform:eng/provenance/files.json (task-owned source, test, AotProbe and generated project-input classifications only); DesktopPlatform:artifacts/evidence/** (task-owned WP-41.02 evidence only)
Shared resources (follow the owner protocol): RES-contracts-schema-sources (append): Each schema closure task edits only its own domain proto or HTTP-schema files and adds its own sharded constraint and fixture files. Schema-closure tasks and Contracts policy tasks that touch package/access/provenance/dependency input registries share this append/rebase protocol: append only task-owned rows and successor receipts to package, compiled access/hash, foundation, operation, constraint, provenance source/output, binding, and dependency-review inventories; preserve prior history and never rewrite another task's rows. Refresh dependency input hashes only for the task-owned closure; do not expand dependency versions or closure. Public Kotlin/Dokka successors are exclusively governed by RES-contracts-dokka-profile. A proto file with several contributing tasks (operator, policy/configuration) has one designated author task and the others request changes through it. Each serialized merge is followed by a rebase and regeneration before integration of the next task.; RES-desktopplatform-build-config (append): Solution/project lists, central package versions and CI job lists are appended by the task that adds a project, dependency or job; dependency additions follow the dependency-admission policy with a reviewed receipt; lock files are regenerated after rebase and never hand-merged; the integration owner resolves ordering conflicts at merge.; RES-desktopplatform-policy-data (append): Generated policy data is regenerated from its pinned source and never hand-edited; the reason-code registry is append-only with stable codes; each task adds its own test classes and evidence rows.; RES-contract-consumer-pins (append): A consumer task updates the pin it needs through a reviewed dependency change to the exact published candidate containing its closure; no consumer pins an unpublished closure or references Contracts source.
Unblocks: EXT.03, EXT.04, EXT.08, EXT.90, SCOPE.25

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Contracts stage: authored constraint-shard and aggregate checks, generated-shape and fixture checks, and applicable schema/structure tests. Only after that Contracts merge publishes both task candidates, Desktop stage pins the exact ArcForges.Contracts.PublicApi and ArcForges.Sdk.Contracts packages from the same merge and builds/tests the product and nested tests against those packages (never Contracts source); verify value-model coverage per type, bidirectional validation and executable first-party containment rejection. The nested AotProbe must AOT-compile with the platform present under P2-017; compilation only, with no hosted/runtime execution. Keep the pinned Gitleaks scan enabled. Its generic-api-key exception may match only the six observed lines/four unique verified public input SHA256 values in eng/policy/dependency-policy.json and eng/policy/dependency-reviews/ext-02-r1.json, requiring the exact path and digest on the same line (AND); tests must cover exact positives and reject a changed digest, another path, and any unrelated 64-hex value. Do not allow generic 64-hex patterns, whole-file or commit suppressions, scanner/workflow/rule-algorithm changes, or new dependencies.
Completion evidence for the ledger: Contracts source/generation/test results and both exact published package identities, versions and content hashes; Desktop exact two-package pins, locked restore/build/test results, executable containment negative, and native AOT compile result; pinned Gitleaks results and positive/negative exact exception-boundary tests.
Notes: WP-41 Sec.1 names the AOT-vs-dynamic-value tension as 'the platform's hardest design problem' -- narrow early risk proof. The first-party containment test must execute and reject StructuredValue in first-party domain/product contract source, not merely retain a textual fixture; Program.cs may only register ExtensionBoundaryCases.Run(root), without runner refactoring, other registrations, or execution-order/exit-semantics changes. The fixture and test are task-owned evidence. This is a staged cross-repository task: finish and merge the Contracts proto/owned constraint shard/tests first, then consume only the exact ArcForges.Contracts.PublicApi and ArcForges.Sdk.Contracts candidates published by that same Contracts merge before starting the Desktop consumer stage; never reference unpublished Contracts source. Contracts package ownership is fixed: PublicApi supplies the existing StructuredValue/CapabilityArguments/CapabilityResult types, while Sdk.Contracts owns the generated ValueSchema types from extensions.proto; do not duplicate ValueSchema locally or move extensions.proto into PublicApi. No new package ID or package ecosystem is introduced: the only added dependency identities are these two already-existing NuGet package IDs at their exact task-produced candidate versions; preserve every other coordinate/version and the existing transitive, xunit and TestSdk closure unchanged. Desktop changes are confined to the exact project/configuration/policy/evidence paths listed above, with task-owned additive rows and immutable receipt; no runtime, security, schema, generator, package-identity or unrelated algorithm changes are authorized. The root constraints aggregate is regenerated through the existing generator from only the new EXT.02 shard; do not alter extensions.json, the generator, its manifest or other shards/messages.
```

```text
Execute ArcForges delivery task EXT.03 — Declarative UI and settings contribution.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\extensions.md (anchor task-ext-03).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/ext-03 (python tools/delivery.py claim EXT.03 --worker <name>); task branch task/ext-03 in DesktopPlatform; ledger record ledger/tasks/ext-03.md.
Kind/size: producer/M. Baseline: not-started.
Outcome: Panel declarations from a closed, versioned element vocabulary render with first-party controls; settings schemas are declarative; secret fields yield references only; extension-contributed surfaces are visibly attributed.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-41.03 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\41-extension-platform-and-integrations.md, anchor rule-wp-41.03

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

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\extensions.md (anchor task-ext-04).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Contracts (integration owner: Contracts integration owner, the holder of roles/integration-contracts).
Claim and handoff record: claims/ext-04 (python tools/delivery.py claim EXT.04 --worker <name>); task branch task/ext-04 in Contracts; ledger record ledger/tasks/ext-04.md.
Kind/size: producer/M. Baseline: not-started.
Outcome: manifest.v1/workflow.v1/panel.v1 validators exist from published Contracts, and package installation moves only through the immutable staged states (acquired/verified/staged/awaitingConsent/active/disabled/quarantined/removed) with no state that resets an effect fence.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-41.04 (manifest.v1/workflow.v1/panel.v1 validators and the immutable staged install/update/drain/migration/revocation/rollback state machine): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\41-extension-platform-and-integrations.md, anchor rule-wp-41.04

Entry condition: adoption slice ADOPT.03.extensions is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] EXT.02: the closed value model workflow.v1 nodes are typed against
- [artifact] CON.16: WP-03 fixture signing/catalog keys (catalog/index/revocation/update/realm schemas + independent signed vectors)
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Contracts:public/proto/arcforges/extensions/v1/**; DesktopPlatform:src/Extensions/ArcForges.Extensions.Packaging/Lifecycle/**
Shared resources (follow the owner protocol): RES-contracts-schema-sources (append): Each schema closure task edits only its own domain proto or HTTP-schema files and adds its own sharded constraint and fixture files. Schema-closure tasks and Contracts policy tasks that touch package/access/provenance/dependency input registries share this append/rebase protocol: append only task-owned rows and successor receipts to package, compiled access/hash, foundation, operation, constraint, provenance source/output, binding, and dependency-review inventories; preserve prior history and never rewrite another task's rows. Refresh dependency input hashes only for the task-owned closure; do not expand dependency versions or closure. Public Kotlin/Dokka successors are exclusively governed by RES-contracts-dokka-profile. A proto file with several contributing tasks (operator, policy/configuration) has one designated author task and the others request changes through it. Each serialized merge is followed by a rebase and regeneration before integration of the next task.
Permitted substitutes (never real integration evidence): SUB-signed-format-fixture-keys: signature/hash verification mechanics, expired/revoked/unknown-key refusal, malformed/rollback/mixed-shard handling Real producer ['UPD.07']; removed by REL.11
Unblocks: EXT.05, EXT.90

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Archive traversal/size/signature tests, DAG bounds (maxItems<=100, nesting<=2, 256 expanded steps), increased-permission re-consent, active-old-job, private-state rollback incompatibility, unknown-effect tests -- all offline against fixture-signed archives.
Completion evidence for the ledger: Lifecycle matrix, re-consent, uninstall and revoke results (part).
```

```text
Execute ArcForges delivery task EXT.05 — Six contribution-kind runtime wiring.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\extensions.md (anchor task-ext-05).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/ext-05 (python tools/delivery.py claim EXT.05 --worker <name>); task branch task/ext-05 in DesktopPlatform; ledger record ledger/tasks/ext-05.md.
Kind/size: producer/L. Baseline: not-started.
Outcome: Each of the six contribution kinds registers and executes through the lifecycle engine and the dual capability boundary; a running task freezes the package version it started with (BR-10); uninstall never cascade-deletes professional resources the extension created (BR-11).

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-41.04 (the six package contribution kinds (skill/template/workflow/mcp/connector/extension) runtime registration and execution wiring): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\41-extension-platform-and-integrations.md, anchor rule-wp-41.04

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

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\extensions.md (anchor task-ext-06).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/ext-06 (python tools/delivery.py claim EXT.06 --worker <name>); task branch task/ext-06 in Cloud; ledger record ledger/tasks/ext-06.md.
Kind/size: producer/L. Baseline: not-started.
Outcome: Cloud PackageCatalog accepts immutable submissions with DNS publisher verification, holds review-state/revocation authority and produces a signed static index; only OperatorService (not the console or the Extensions implementation) writes PackageCatalog tables.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-41.05 (Cloud PackageCatalog producer: DNS publisher verification, immutable submissions, review-state/revocation authority, signed static index): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\41-extension-platform-and-integrations.md, anchor rule-wp-41.05
- WP-41:packagecatalog-ownership-paragraph-sec-5 PackageCatalog ownership paragraph (Sec.5-6 boundary): OperatorService is sole authenticator/caller; neither Extensions Runtime nor console writes PackageCatalog tables (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\41-extension-platform-and-integrations.md, package-level obligation

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

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\extensions.md (anchor task-ext-07).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/ext-07 (python tools/delivery.py claim EXT.07 --worker <name>); task branch task/ext-07 in DesktopPlatform; ledger record ledger/tasks/ext-07.md.
Kind/size: producer/M. Baseline: not-started.
Outcome: Desktop and CLI consume the signed static index and PackageCatalog methods to install/update packages, with correct offline behavior when the catalog is unreachable.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-41.05 (desktop/CLI catalog consumers): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\41-extension-platform-and-integrations.md, anchor rule-wp-41.05

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

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\extensions.md (anchor task-ext-08).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Contracts (integration owner: Contracts integration owner, the holder of roles/integration-contracts).
Claim and handoff record: claims/ext-08 (python tools/delivery.py claim EXT.08 --worker <name>); task branch task/ext-08 in Contracts; ledger record ledger/tasks/ext-08.md.
Kind/size: producer/M. Baseline: not-started.
Outcome: The SDK, validators and tool-payload projections generate from authored public proto; the CLI uses eligible publisher PAT and catalog/resource methods; validate matches host install checks; no generated schema is inferred from C# reflection.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-41.06 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\41-extension-platform-and-integrations.md, anchor rule-wp-41.06
- WP-41:sec-8-gate-item-8-mcp-vocabulary-mapping Sec.8 gate item 8: MCP vocabulary mapping + SDK version pin -- VG-02 (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\41-extension-platform-and-integrations.md, package-level obligation

Entry condition: adoption slice ADOPT.03.extensions is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] EXT.02: the published extension protocol/value-model proto to generate from
- [artifact] CLOUD.16: publisher PAT issuance
Completion prerequisites (may start earlier; cannot complete before these are complete):
- [integration] EXT.06: the real Cloud PackageCatalog submit endpoint

Permitted write scope: Contracts:src/SDK/ArcForges.SDK.*/**; Contracts:src/SDK/ArcForges.Cli/**
Shared resources (follow the owner protocol): RES-contracts-schema-sources (append): Each schema closure task edits only its own domain proto or HTTP-schema files and adds its own sharded constraint and fixture files. Schema-closure tasks and Contracts policy tasks that touch package/access/provenance/dependency input registries share this append/rebase protocol: append only task-owned rows and successor receipts to package, compiled access/hash, foundation, operation, constraint, provenance source/output, binding, and dependency-review inventories; preserve prior history and never rewrite another task's rows. Refresh dependency input hashes only for the task-owned closure; do not expand dependency versions or closure. Public Kotlin/Dokka successors are exclusively governed by RES-contracts-dokka-profile. A proto file with several contributing tasks (operator, policy/configuration) has one designated author task and the others request changes through it. Each serialized merge is followed by a rebase and regeneration before integration of the next task.
Unblocks: EXT.90

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Independent SDK consumer test, manifest/tag compatibility, PAT scope tests, generated-vs-reflection negative test -- offline codegen tests.
Completion evidence for the ledger: Generator, validate-parity and first-party build results.
```

```text
Execute ArcForges delivery task EXT.09 — Local MCP stdio behind the owned connector child.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\extensions.md (anchor task-ext-09).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/ext-09 (python tools/delivery.py claim EXT.09 --worker <name>); task branch task/ext-09 in DesktopPlatform; ledger record ledger/tasks/ext-09.md.
Kind/size: producer/M. Baseline: not-started.
Outcome: Local MCP servers run stdio behind an owned connector child process; only that child speaks ArcForges gRPC; origin/scope changes invalidate consent; no browser/Android local subprocess exists; child crash/lease recovery works.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-41.07 (local MCP stdio placement behind the owned connector child process): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\41-extension-platform-and-integrations.md, anchor rule-wp-41.07
- WP-41:sec-8-gate-item-8-mcp-vocabulary-mapping Sec.8 gate item 8: MCP vocabulary mapping + SDK version pin -- VG-02 (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\41-extension-platform-and-integrations.md, package-level obligation

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

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\extensions.md (anchor task-ext-10).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\AI (integration owner: AI integration owner, the holder of roles/integration-ai).
Claim and handoff record: claims/ext-10 (python tools/delivery.py claim EXT.10 --worker <name>); task branch task/ext-10 in AI; ledger record ledger/tasks/ext-10.md.
Kind/size: producer/M. Baseline: not-started.
Outcome: Cloud-placed MCP connections route HTTP through the AI Worker adapter only; standard MCP protocol is preserved; each connection has one placement/secret owner and exact failure/egress behavior; MCP content is treated as untrusted data.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-41.07 (Cloud MCP HTTP placement through the AI Worker adapter): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\41-extension-platform-and-integrations.md, anchor rule-wp-41.07
- WP-41:sec-8-gate-item-8-mcp-vocabulary-mapping Sec.8 gate item 8: MCP vocabulary mapping + SDK version pin -- VG-02 (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\41-extension-platform-and-integrations.md, package-level obligation

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

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\extensions.md (anchor task-ext-90).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/ext-90 (python tools/delivery.py claim EXT.90 --worker <name>); task branch task/ext-90 in DesktopPlatform; ledger record ledger/tasks/ext-90.md.
Kind/size: producer/M. Baseline: not-started.
Outcome: SDK/protocol, desktop host/runtime and Cloud registry ownership are verified split correctly; standard MCP transports and out-of-process extensions are preserved; no external-agent delegation or in-process third-party plugin exists anywhere; VG-02 and PG-09 close.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-41.90 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\41-extension-platform-and-integrations.md, anchor rule-wp-41.90
- WP-41:sec-8-gate-item-9-extension-protocol-con Sec.8 gate item 9: extension protocol conformance suite -- PG-09 (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\41-extension-platform-and-integrations.md, package-level obligation

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
