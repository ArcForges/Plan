# ArcForges delivery task prompts — Application composition

Generated from Design `docs/planning/delivery/delivery-graph.json` by `tools/delivery.py`; do not edit by hand.
Each block is self-contained. Claim a task only when `python tools/delivery.py ready` lists it, with
`python tools/delivery.py claim <TASK-ID> --worker <name>`, then follow `arcforges-implementation.md`.
Tasks are ordered by lane for reading; the order is not a schedule.

## Application composition

```text
Execute ArcForges delivery task APP.01 — Assistant.Abstractions host ports and application identity.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\app-composition.md (anchor task-app-01).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/app-01 (python tools/delivery.py claim APP.01 --worker <name>); task branch task/app-01 in DesktopPlatform; ledger record ledger/tasks/app-01.md.
Kind/size: producer/M. Baseline: not-started.
Outcome: Assistant.Abstractions published with IHostContext/IHostActions/IHostResources/IHostNavigation/IHostLifecycle/IHostPlatformServices, product/profile identity and lifetime; two independent application identities cannot share stores/registration.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-14.00 (Host-port signatures, product/profile identity and lifetime, and two-identity unit isolation only; APP.08 owns the WP-14.00 minimal real-integration sample.): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\14-hub-and-minimal-provider-slice.md, anchor rule-wp-14.00

Entry condition: adoption slice ADOPT.02.app-composition is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [contract] CON.02: published capability/resource contract records (descriptor/risk/context shapes)
- [artifact] PLT.17: delivered ArcForges.Capabilities application identity and explicit in-process composition pattern
- [artifact] FND.02: published ArcForges.Application.Abstractions cancellation and lifecycle ports
- [artifact] FND.01: published ArcForges.Foundation identity/error/version primitives
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:src/BuildingBlocks/ArcForges.Assistant.Abstractions/**; DesktopPlatform:tests/AssistantAbstractionsTests/**; DesktopPlatform:DesktopPlatform.slnx (register APP.01 producer and its test project only); DesktopPlatform:.github/workflows/package-validation.yml (run the APP.01 test project only); DesktopPlatform:eng/packaging/packages.json (APP.01 package entry and Architecture 27 owned-package edges only); DesktopPlatform:eng/version-sources.json (APP.01 package source declaration only); DesktopPlatform:eng/policy/dependency-policy.json (APP.01 production/test project registrations for the exact Architecture 27 dependency edges only); DesktopPlatform:eng/policy/dependency-reviews/app-01-*.json (new immutable APP.01 successor only for already-admitted dependency identities, if required; no new dependency or version); DesktopPlatform:eng/policy/licence-boundary.json (APP.01 production/test project registrations only); DesktopPlatform:eng/policy/reconciliation/project-updates.json (APP.01 project registrations only); DesktopPlatform:eng/policy/reconciliation/source.json (APP.01 source inventory only); DesktopPlatform:eng/policy/reconciliation/active-projects.json (APP.01 active project registrations only; preserve frozen inventories); DesktopPlatform:eng/policy/runtime-ownership.json (APP.01 project classifications only); DesktopPlatform:eng/policy/architecture-projects.json (append exactly the APP.01 producer as role=Abstractions with production=true and aot=true, and its test project as role=Test with production=false and aot=false; preserve every other row and field); DesktopPlatform:eng/provenance/files.json (APP.01 owned-source inventory rows only); DesktopPlatform:eng/provenance/records/assistant-abstractions-*.json (new immutable APP.01 source/package receipts only; preserve all prior records); DesktopPlatform:eng/packaging/packages.py (exact existing external dependency pins in the APP.01 package closure only; add no package ID or version); DesktopPlatform:eng/packaging/test_packages.py (APP.01-owned positive/negative checks for those exact existing pins only); DesktopPlatform:README.md (current APP.01 package production claim only); DesktopPlatform:docs/compliance/third-party-license-register.md (APP.01 package binding to already-admitted external dependencies only); DesktopPlatform:Directory.Packages.props (append only ArcForges.Assistant.Abstractions and AssistantAbstractionsTests to the existing ArcForges.Contracts.Foundation 1.0.0-ci.216.1 MSBuildProjectName selector; preserve the 1.0.0-ci.113.1 default); DesktopPlatform:eng/policy/architecture-contract-tests.json (append only exact APP.01 public API-to-focused-test bindings in the AssistantAbstractionsTests project)
Shared resources (follow the owner protocol): RES-desktopplatform-build-config (append): Solution/project lists, central package versions and CI job lists are appended by the task that adds a project, dependency or job; dependency additions follow the dependency-admission policy with a reviewed receipt; lock files are regenerated after rebase and never hand-merged; the integration owner resolves ordering conflicts at merge.; RES-desktopplatform-package-inventory (append): Each producer task adds its own package entry; every merge to main packs and publishes all packages at one version; consumers pin the candidate produced by the merge of the capability they need, never waiting for a package closure task; one merge queue.; RES-desktopplatform-policy-data (append): Generated policy data is regenerated from its pinned source and never hand-edited; the reason-code registry is append-only with stable codes; each task adds its own test classes and evidence rows.; RES-architecture-tests (append): Each repository policy task owns its suite; rule additions are append-only.
Unblocks: APP.02, APP.03, APP.05, APP.06, APP.07, APP.08, AST.01, EXE.01, PLT.57, PRF.02

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline unit tests only (two identities/no shared store); Native AOT compile check; no live Cloud/device in CI per P2-017.
Completion evidence for the ledger: Source commit, Assistant.Abstractions package version/hash, two-identity isolation test results.
Notes: Root of the whole area's dependency graph; every other WP14 to WP17/26 desktop task starts from this package. FND.02 is the real ArcForges.Application.Abstractions producer; PLT.17 provides only the ArcForges.Capabilities application-identity/composition pattern. Keep Architecture 27's Assistant.Abstractions direct dependency table exactly Foundation plus Application.Abstractions; do not add a direct ArcForges.Capabilities dependency. CON.02 remains a host-port shape prerequisite and does not authorize another dependency edge. Register only APP.01's package, producer/test projects, and provenance/reconciliation rows, using already-admitted dependency identities and exact existing version pins; do not add package IDs, pins, versions, dependency owners, or expand the package closure. Append this producer's package entry and build-config project/CI rows; after rebase regenerate lock files and never hand-merge them. Write-scope repair 2026-10-04 (w-c20261004-app01): Directory.Packages.props and eng/policy/architecture-contract-tests.json are append-only supporting bindings for the APP.01 producer and test projects (central transitive pinning rejects restore of a project that reaches ArcForges.Foundation under the 1.0.0-ci.113.1 default; RP-10 requires a [Fact] binding for every public API method of the Abstractions project). They add no dependency, package ID, version or pin.
```

```text
Execute ArcForges delivery task APP.02 — Minimal ArcScope application services (read/create/append annotations).

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\app-composition.md (anchor task-app-02).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\ArcScope (integration owner: ArcScope integration owner, the holder of roles/integration-arcscope).
Claim and handoff record: claims/app-02 (python tools/delivery.py claim APP.02 --worker <name>); task branch task/app-02 in ArcScope; ledger record ledger/tasks/app-02.md.
Kind/size: producer/M. Baseline: not-started.
Outcome: Real read/create/append annotation commands through typed application handlers and local persistence, with descriptor/risk/context validation and one write path shared by UI and own-app capability invocation. Professional ArcScope completion remains WP33-WP35.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-14.01 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\14-hub-and-minimal-provider-slice.md, anchor rule-wp-14.01

Entry condition: adoption slice ADOPT.05.app-composition is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] APP.01: published Assistant.Abstractions host ports and product identity
- [artifact] PLT.24: real ICapabilityProvider.InvokeAsync invocation pipeline (owner-side decode/validate)
- [artifact] PLT.38: published security decision pipeline enforcement point
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: ArcScope:src/ArcForges.ArcScope.Application/**; ArcScope:src/ArcForges.ArcScope.Infrastructure/**; ArcScope:tests/**
Unblocks: APP.03, APP.04, APP.08

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline unit tests (descriptor/risk/context validation, one write path); no live Cloud in CI.
Completion evidence for the ledger: Source commit, command receipt samples, validation-failure cases.
Notes: This is the ONLY product-repo work in WP14 to WP17/26; professional ArcScope completion is WP33-WP35, not here.
```

```text
Execute ArcForges delivery task APP.03 — Clean Native AOT package-consumer composition for ArcScope.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\app-composition.md (anchor task-app-03).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\ArcScope (integration owner: ArcScope integration owner, the holder of roles/integration-arcscope).
Claim and handoff record: claims/app-03 (python tools/delivery.py claim APP.03 --worker <name>); task branch task/app-03 in ArcScope; ledger record ledger/tasks/app-03.md.
Kind/size: producer/M. Baseline: not-started.
Outcome: A clean Native AOT ArcScope consumer built purely from published Platform/Contracts packages (including the ArcForges.Security.Audit and ArcForges.Security.CapabilityEnforcement packages admitted by PLT.46) and in-process typed host ports; no source or project reference and no local-RPC product loop. Package-only restore, publish/run, command/cancel/result and owner refusal proven. The ArcScope product host (ArcForges.ArcScope) composes every capability binding through CapabilityEnforcementGate.Enforce, with the security and egress audit sinks and the lease event sink writing to ArcForges.Security.Audit, and applies the egress-to-audit mapping decision recorded in ledger plt-44.md (Design architecture/08 EG-06 to EG-09). A binding built without Enforce is not allowed in the host.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-14.02 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\14-hub-and-minimal-provider-slice.md, anchor rule-wp-14.02

Entry condition: adoption slice ADOPT.05.app-composition is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] APP.01: published Assistant.Abstractions package (not project reference)
- [artifact] APP.02: published ArcScope application-services surface
- [artifact] PRF.04: proven Local RPC under Native AOT pattern
- [artifact] NAT.01: confirmed Native AOT device-tool/capability-invocation feasibility from the high-risk probe
- [artifact] PLT.44: delivered ArcForges.Security.Audit: the durable AuditStore, EgressAuditSink, CapabilityLeaseEventAuditSink and the AuditRetentionRunner (ledger plt-44.md)
- [artifact] PLT.24: delivered CapabilityInvocationPipeline (invocation pipeline) that CapabilityEnforcementGate wraps
- [artifact] PLT.38: delivered decision pipeline and the four enforcement points that CapabilityEnforcementGate.AuthorizeAsync runs
Completion prerequisites (may start earlier; cannot complete before these are complete):
- [integration] PLT.46: published ArcForges.Security.Audit and ArcForges.Security.CapabilityEnforcement packages admitted and published by PLT.46 (the CapabilityEnforcement package requires the PLT.46 IsPackable repair)

Permitted write scope: ArcScope:src/ArcForges.ArcScope/**; ArcScope:packaging/**; ArcScope:Directory.Packages.props (append only the central version rows that the host package references need for ArcForges.Security.Audit and ArcForges.Security.CapabilityEnforcement)
Unblocks: APP.08, HAR.05, PLT.57

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Native AOT publish/run in CI (package-only restore), offline command/cancel/result tests; no installed-package or public-release install/upgrade CI per P2-017. Product host acceptance (Planning repair 2026-10-08, DLV-34; P2-021, PLT.57 completion): offline tests in CI prove that every capability binding in the host goes through CapabilityEnforcementGate.Enforce and that the audit sinks write to the audit store; one real local opt-in run of the host composition gates one real capability end to end and reads its audit events back, recorded once (no hosted runtime, device or live-service CI, P2-017).
Completion evidence for the ledger: AOT publish log, package hash manifest, command/cancel/result and owner-refusal test results. Host composition test results and the one local opt-in run record for the PLT.57 completion acceptance.
Notes: Narrow early-risk proof: first real evidence that the whole Assistant.Abstractions/host-port composition model survives Native AOT package-only consumption for an actual product. Failure here invalidates the composition model assumed by WP15 to WP17. Planning repair 2026-10-08 (DLV-34; P2-021): the PLT.57 completion acceptance is carried here, because no other patch owned APP.03. Size moves from S to M for the host composition. Route (packaging, not reference; the coordinator must approve it, because it adds the CapabilityEnforcement project to the PLT.46 packaging scope): ArcScope consumes ArcForges.Security.Audit and ArcForges.Security.CapabilityEnforcement as published NuGet packages admitted by PLT.46 (start edge added here). The CapabilityEnforcement project is non-packable at PLT.57 (delivered record), so PLT.46 must make it packable under its IsPackable repair. A project reference to the non-packable project is refused by this task package-only rule. The outcome above names these packages, so it no longer forbids the chosen route.
```

```text
Execute ArcForges delivery task APP.04 — Idempotency and revision against the real store.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\app-composition.md (anchor task-app-04).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/app-04 (python tools/delivery.py claim APP.04 --worker <name>); task branch task/app-04 in DesktopPlatform; ledger record ledger/tasks/app-04.md.
Kind/size: producer/S. Baseline: not-started.
Outcome: Command receipt and expected local revision exercised against the real store; draft/conflict behavior and unknown-outcome classification preserved under duplicate command, stale revision and process-kill-around-commit.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-14.03 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\14-hub-and-minimal-provider-slice.md, anchor rule-wp-14.03

Entry condition: adoption slice ADOPT.02.app-composition is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] APP.02: real local persistence write path to kill/duplicate against
- [artifact] FND.02: published execution identity and idempotency records (command identity)
- [artifact] FND.03: published revision and sequence records
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:src/BuildingBlocks/ArcForges.Assistant.Abstractions/**; DesktopPlatform:tests/AssistantAbstractionsTests/**
Unblocks: APP.08

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline unit/process-kill tests (duplicate command, stale revision, kill-around-commit); no live environment.
Completion evidence for the ledger: Kill-around-commit recovery log, duplicate/stale-revision test results.
Notes: Shares vocabulary (command identity, revision) with WP16 execution engine (EXE.01) but is the host-port-level idempotency check, not the ProductJob engine itself.
```

```text
Execute ArcForges delivery task APP.05 — Approval at the owner.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\app-composition.md (anchor task-app-05).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/app-05 (python tools/delivery.py claim APP.05 --worker <name>); task branch task/app-05 in DesktopPlatform; ledger record ledger/tasks/app-05.md.
Kind/size: producer/M. Baseline: not-started.
Outcome: Expiry/modified-input/revocation cannot bypass owner checks.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-14.04 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\14-hub-and-minimal-provider-slice.md, anchor rule-wp-14.04

Entry condition: adoption slice ADOPT.02.app-composition is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] APP.01: published host ports to render the approval surface through
- [artifact] PLT.39: published approval/steering/step-up mechanism
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:src/BuildingBlocks/ArcForges.Assistant.Abstractions/**; DesktopPlatform:tests/AssistantAbstractionsTests/**
Unblocks: APP.08, AST.12, DEV.03

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline unit tests: expiry, modified-input, revocation cannot bypass owner checks.
Completion evidence for the ledger: Expiry/modified-input/revocation test results tied to a real approval record.
Notes: contracts/02-local-rpc-operations.md confirms InvokeAsync performs owner-side final validation under WP-14.04 AND WP-26.02 -- this is the SAME enforcement mechanism DEV.03 (26.02) re-invokes at the device-bridge call site, not a duplicate.
```

```text
Execute ArcForges delivery task APP.06 — Context and artifact integration.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\app-composition.md (anchor task-app-06).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/app-06 (python tools/delivery.py claim APP.06 --worker <name>); task branch task/app-06 in DesktopPlatform; ledger record ledger/tasks/app-06.md.
Kind/size: producer/M. Baseline: not-started.
Outcome: Own-app resource references frozen at selection time, preview opened through the product port, egress enforced separately, provenance preserved. Selection changes after freeze, missing resource, denied export and bounded artifact all handled.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-14.05 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\14-hub-and-minimal-provider-slice.md, anchor rule-wp-14.05

Entry condition: adoption slice ADOPT.02.app-composition is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] APP.01: published IContextProvider/IArtifactHandler/IResourceAccess host port shapes
- [artifact] PLT.21: real context providers and freezing implementation
- [artifact] PLT.22: real resources-and-artifacts implementation
- [artifact] PLT.41: published egress control mechanism
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:src/BuildingBlocks/ArcForges.Assistant.Abstractions/**; DesktopPlatform:tests/AssistantAbstractionsTests/**
Unblocks: APP.08, AST.03, AST.16

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline unit tests: selection-after-freeze, missing resource, denied export, bounded artifact size.
Completion evidence for the ledger: Freeze/preview/egress test results with provenance trace samples.
Notes: AST.03 (15.02 attachments) and AST.16 (17.06 preview/host context) both reuse this exact freeze+preview port rather than duplicating it.
```

```text
Execute ArcForges delivery task APP.07 — Independent lifecycle.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\app-composition.md (anchor task-app-07).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/app-07 (python tools/delivery.py claim APP.07 --worker <name>); task branch task/app-07 in DesktopPlatform; ledger record ledger/tasks/app-07.md.
Kind/size: producer/S. Baseline: not-started.
Outcome: Launch/save works with Cloud unavailable and the assistant view closed; views dispose independently from services; two windows with different drafts and independent app crash lose no canonical data.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-14.06 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\14-hub-and-minimal-provider-slice.md, anchor rule-wp-14.06

Entry condition: adoption slice ADOPT.02.app-composition is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] APP.01: published IHostLifecycle port
- [artifact] PLT.32: published lifecycle/menus/shutdown shell pattern
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:src/BuildingBlocks/ArcForges.Assistant.Abstractions/**; DesktopPlatform:tests/AssistantAbstractionsTests/**; DesktopPlatform:eng/policy/architecture-contract-tests.json (append only exact APP.07 public API-to-focused-test bindings in the AssistantAbstractionsTests project); DesktopPlatform:eng/provenance/files.json (APP.07 owned-source inventory rows for the new source and test files only)
Shared resources (follow the owner protocol): RES-architecture-tests (append): Each repository policy task owns its suite; rule additions are append-only.
Unblocks: APP.08

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline unit/process tests: two windows/different drafts, independent crash, no data loss; no live-environment CI.
Completion evidence for the ledger: Two-window and crash-recovery test results.
Notes: Write-scope repair 2026-10-05 (w-c20261005-app07): eng/policy/architecture-contract-tests.json and eng/provenance/files.json are append-only supporting bindings for the new Assistant.Abstractions lifecycle source and tests (RP-10 requires a [Fact] binding for every public API method of the Abstractions project; the provenance inventory lists every owned source file). They add no dependency, package ID, version, project or pin. The task composes no Shell, Capabilities or Persistence.Sqlite (APP.08 owns the real sample); its tests use test-only ports for the local draft store, Cloud link and canonical data.
```

```text
Execute ArcForges delivery task APP.08 — Owned-artifact receipt and UX acceptance.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\app-composition.md (anchor task-app-08).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/app-08 (python tools/delivery.py claim APP.08 --worker <name>); task branch task/app-08 in DesktopPlatform; ledger record ledger/tasks/app-08.md.
Kind/size: acceptance/M. Baseline: not-started.
Outcome: A minimal, runnable WP14 integration sample composes the host ports with real ArcForges.Capabilities, ArcForges.Desktop.Shell and ArcForges.Persistence.Sqlite, and demonstrates product/profile identity, lifecycle and isolated local-store use; WP14 is built/packed once from a clean environment with all applicable UX acceptance groups and package/contract/owner/version compatibility and failure/recovery evidence recorded. No later-provider fixture closes a real WP14 gate.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-14.00 (Minimal real-integration sample only: compose the WP-14 host ports with real ArcForges.Capabilities, ArcForges.Desktop.Shell and ArcForges.Persistence.Sqlite; no fakes or stand-ins.): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\14-hub-and-minimal-provider-slice.md, anchor rule-wp-14.00
- WP-14.90 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\14-hub-and-minimal-provider-slice.md, anchor rule-wp-14.90

Entry condition: adoption slice ADOPT.02.app-composition is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] APP.01: published WP-14.00 host-port signatures and product/profile identity/lifetime
- [artifact] APP.02: completed WP-14.01
- [artifact] APP.03: completed WP-14.02
- [artifact] APP.04: completed WP-14.03
- [artifact] APP.05: completed WP-14.04
- [artifact] APP.06: completed WP-14.05
- [artifact] APP.07: completed WP-14.06
- [artifact] PLT.17: real ArcForges.Capabilities application identity and composition root
- [artifact] PLT.27: real ArcForges.Desktop.Shell project and window/panel host
- [artifact] PLT.01: real single-write-path Persistence.Sqlite store
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:samples/AssistantHost/** (minimal runnable sample only; its packages.lock.json is generated from existing approved dependency identities); DesktopPlatform:DesktopPlatform.slnx (register only the APP.08 sample); DesktopPlatform:.github/workflows/package-validation.yml (build/run only the sample in the existing validation flow; no new job, matrix or deployment); DesktopPlatform:eng/policy/architecture-projects.json (append only the sample project classification); DesktopPlatform:eng/policy/runtime-ownership.json (append only the sample's non-production ownership classification); DesktopPlatform:eng/policy/licence-boundary.json (append only the sample project classification); DesktopPlatform:eng/policy/reconciliation/active-projects.json (append only the sample project); DesktopPlatform:eng/policy/reconciliation/project-updates.json (append only the sample project registration); DesktopPlatform:eng/policy/reconciliation/source.json (append only the sample source inventory); DesktopPlatform:eng/provenance/files.json (classify only the task-owned sample source and project/lock inputs); DesktopPlatform:eng/policy/dependency-policy.json (only exact sample project/lock input bindings for already-admitted dependency identities); DesktopPlatform:eng/policy/dependency-reviews/app-08-r1.json (immutable sample admission receipt only if required by the existing dependency gate; no dependency identity, version or closure changes); DesktopPlatform:artifacts/evidence/**
Shared resources (follow the owner protocol): RES-desktopplatform-build-config (append): Solution/project lists, central package versions and CI job lists are appended by the task that adds a project, dependency or job; dependency additions follow the dependency-admission policy with a reviewed receipt; lock files are regenerated after rebase and never hand-merged; the integration owner resolves ordering conflicts at merge.; RES-desktopplatform-policy-data (append): Generated policy data is regenerated from its pinned source and never hand-edited; the reason-code registry is append-only with stable codes; each task adds its own test classes and evidence rows.
Unblocks: AST.17

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Build and run the real minimal sample in the existing package-validation flow under P2-017, alongside the single WP14 CI build/pack producing the immutable candidate; record UX-A/B ledger rows per experience/03. No hosted E2E or live-service CI (P2-017); macOS is outside the delivery scope per P2-023.
Completion evidence for the ledger: Source commit, package/artifact versions and hashes, environment, UX-A/B acceptance rows, named later-fixture list (none expected for WP14 itself).
Notes: APP.01 owns only WP-14.00 host-port signatures, product/profile identity and lifetime, and two-identity unit isolation; APP.08 owns WP-14.00's minimal real-integration sample plus WP-14.90 acceptance. The sample composes existing host ports with real ArcForges.Capabilities, ArcForges.Desktop.Shell and ArcForges.Persistence.Sqlite; it must not use fakes or fixture stand-ins, implement full AssistantHost UI (WP-17), add a package identity, or require PLT.35. Register only the sample project/build/run path and its exact existing-policy, reconciliation, provenance and lock bindings; preserve all package identities and dependency versions/closure. Shared build-config and policy-data updates are append-only.
```
