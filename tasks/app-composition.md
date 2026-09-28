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
- WP-14.00 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\14-hub-and-minimal-provider-slice.md, anchor rule-wp-14.00

Entry condition: adoption slice ADOPT.02.app-composition is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [contract] CON.02: published capability/resource contract records (descriptor/risk/context shapes)
- [artifact] PLT.17: delivered ArcForges.Capabilities application identity and explicit in-process composition pattern
- [artifact] FND.02: published ArcForges.Application.Abstractions cancellation and lifecycle ports
- [artifact] FND.01: published ArcForges.Foundation identity/error/version primitives
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:src/BuildingBlocks/ArcForges.Assistant.Abstractions/**; DesktopPlatform:tests/AssistantAbstractionsTests/**; DesktopPlatform:DesktopPlatform.slnx (register APP.01 producer and its test project only); DesktopPlatform:.github/workflows/package-validation.yml (run the APP.01 test project only); DesktopPlatform:eng/packaging/packages.json (APP.01 package entry and Architecture 27 owned-package edges only); DesktopPlatform:eng/version-sources.json (APP.01 package source declaration only); DesktopPlatform:eng/policy/dependency-policy.json (APP.01 production/test project registrations for the exact Architecture 27 dependency edges only); DesktopPlatform:eng/policy/dependency-reviews/app-01-*.json (new immutable APP.01 successor only for already-admitted dependency identities, if required; no new dependency or version); DesktopPlatform:eng/policy/licence-boundary.json (APP.01 production/test project registrations only); DesktopPlatform:eng/policy/reconciliation/project-updates.json (APP.01 project registrations only); DesktopPlatform:eng/policy/reconciliation/source.json (APP.01 source inventory only); DesktopPlatform:eng/policy/reconciliation/active-projects.json (APP.01 active project registrations only; preserve frozen inventories); DesktopPlatform:eng/policy/runtime-ownership.json (APP.01 project classifications only); DesktopPlatform:eng/provenance/files.json (APP.01 owned-source inventory rows only); DesktopPlatform:eng/provenance/records/assistant-abstractions-*.json (new immutable APP.01 source/package receipts only; preserve all prior records); DesktopPlatform:eng/packaging/packages.py (exact existing external dependency pins in the APP.01 package closure only; add no package ID or version); DesktopPlatform:eng/packaging/test_packages.py (APP.01-owned positive/negative checks for those exact existing pins only); DesktopPlatform:README.md (current APP.01 package production claim only); DesktopPlatform:docs/compliance/third-party-license-register.md (APP.01 package binding to already-admitted external dependencies only)
Shared resources (follow the owner protocol): RES-desktopplatform-build-config (append): Solution/project lists, central package versions and CI job lists are appended by the task that adds a project, dependency or job; dependency additions follow the dependency-admission policy with a reviewed receipt; lock files are regenerated after rebase and never hand-merged; the integration owner resolves ordering conflicts at merge.; RES-desktopplatform-package-inventory (append): Each producer task adds its own package entry; every merge to main packs and publishes all packages at one version; consumers pin the candidate produced by the merge of the capability they need, never waiting for a package closure task; one merge queue.; RES-desktopplatform-policy-data (append): Generated policy data is regenerated from its pinned source and never hand-edited; the reason-code registry is append-only with stable codes; each task adds its own test classes and evidence rows.
Unblocks: APP.02, APP.03, APP.05, APP.06, APP.07, APP.08, AST.01, EXE.01, PLT.57, PRF.02

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline unit tests only (two identities/no shared store); Native AOT compile check; no live Cloud/device in CI per P2-017.
Completion evidence for the ledger: Source commit, Assistant.Abstractions package version/hash, two-identity isolation test results.
Notes: Root of the whole area's dependency graph; every other WP14 to WP17/26 desktop task starts from this package. FND.02 is the real ArcForges.Application.Abstractions producer; PLT.17 provides only the ArcForges.Capabilities application-identity/composition pattern. Keep Architecture 27's Assistant.Abstractions direct dependency table exactly Foundation plus Application.Abstractions; do not add a direct ArcForges.Capabilities dependency. CON.02 remains a host-port shape prerequisite and does not authorize another dependency edge. Register only APP.01's package, producer/test projects, and provenance/reconciliation rows, using already-admitted dependency identities and exact existing version pins; do not add package IDs, pins, versions, dependency owners, or expand the package closure. Append this producer's package entry and build-config project/CI rows; after rebase regenerate lock files and never hand-merge them.
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
Kind/size: producer/S. Baseline: not-started.
Outcome: A clean Native AOT ArcScope consumer built purely from published Platform/Contracts packages and in-process typed host ports; no source reference or local-RPC product loop. Package-only restore, publish/run, command/cancel/result and owner refusal proven.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-14.02 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\14-hub-and-minimal-provider-slice.md, anchor rule-wp-14.02

Entry condition: adoption slice ADOPT.05.app-composition is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] APP.01: published Assistant.Abstractions package (not project reference)
- [artifact] APP.02: published ArcScope application-services surface
- [artifact] PRF.04: proven Local RPC under Native AOT pattern
- [artifact] NAT.01: confirmed Native AOT device-tool/capability-invocation feasibility from the high-risk probe
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: ArcScope:src/ArcForges.ArcScope/**; ArcScope:packaging/**
Unblocks: APP.08, HAR.05

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Native AOT publish/run in CI (package-only restore), offline command/cancel/result tests; no installed-package or public-release install/upgrade CI per P2-017.
Completion evidence for the ledger: AOT publish log, package hash manifest, command/cancel/result and owner-refusal test results.
Notes: Narrow early-risk proof: first real evidence that the whole Assistant.Abstractions/host-port composition model survives Native AOT package-only consumption for an actual product. Failure here invalidates the composition model assumed by WP15 to WP17.
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

Permitted write scope: DesktopPlatform:src/BuildingBlocks/ArcForges.Assistant.Abstractions/**; DesktopPlatform:tests/AssistantAbstractionsTests/**
Unblocks: APP.08

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline unit/process tests: two windows/different drafts, independent crash, no data loss; no live-environment CI.
Completion evidence for the ledger: Two-window and crash-recovery test results.
```

```text
Execute ArcForges delivery task APP.08 — Owned-artifact receipt and UX acceptance.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\app-composition.md (anchor task-app-08).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/app-08 (python tools/delivery.py claim APP.08 --worker <name>); task branch task/app-08 in DesktopPlatform; ledger record ledger/tasks/app-08.md.
Kind/size: acceptance/M. Baseline: not-started.
Outcome: WP14 built/packed once from a clean environment; all applicable UX acceptance groups recorded; package/contract/owner/version compatibility and failure/recovery evidence attached; no later-provider fixture used to close a real WP14 gate.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-14.90 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\14-hub-and-minimal-provider-slice.md, anchor rule-wp-14.90

Entry condition: adoption slice ADOPT.02.app-composition is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] APP.01: completed WP-14.00
- [artifact] APP.02: completed WP-14.01
- [artifact] APP.03: completed WP-14.02
- [artifact] APP.04: completed WP-14.03
- [artifact] APP.05: completed WP-14.04
- [artifact] APP.06: completed WP-14.05
- [artifact] APP.07: completed WP-14.06
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:artifacts/evidence/**
Shared resources (follow the owner protocol): RES-desktopplatform-policy-data (append): Generated policy data is regenerated from its pinned source and never hand-edited; the reason-code registry is append-only with stable codes; each task adds its own test classes and evidence rows.
Unblocks: AST.17

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Build/pack once in CI producing the immutable candidate; UX-A/B ledger rows recorded per experience/03; P2-017 scope only (no macOS/E2E/live-service CI).
Completion evidence for the ledger: Source commit, package/artifact versions and hashes, environment, UX-A/B acceptance rows, named later-fixture list (none expected for WP14 itself).
```
