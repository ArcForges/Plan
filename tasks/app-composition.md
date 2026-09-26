# ArcForges delivery task prompts — Application composition

Generated from Design `docs/planning/delivery/delivery-graph.json` by `tools/delivery.py`; do not edit by hand.
Each block is self-contained. Claim a task only when `python tools/delivery.py ready` lists it, with
`python tools/delivery.py claim <TASK-ID> --worker <name>`, then follow `arcforges-implementation.md`.
Tasks are ordered by lane for reading; the order is not a schedule.

## Application composition

```text
Execute ArcForges delivery task APP.01 — Assistant.Abstractions host ports and application identity.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\app-composition.md (anchor task-app-01).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/app-01 (python tools/delivery.py claim APP.01 --worker <name>); task branch task/app-01 in DesktopPlatform; ledger record ledger/tasks/app-01.md.
Kind/size: producer/M. Baseline: not-started.
Outcome: Assistant.Abstractions published with IHostContext/IHostActions/IHostResources/IHostNavigation/IHostLifecycle/IHostPlatformServices, product/profile identity and lifetime; two independent application identities cannot share stores/registration.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-14.00 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\14-hub-and-minimal-provider-slice.md, anchor rule-wp-14.00

Entry condition: adoption slice ADOPT.02.app-composition is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [contract] CON.02: published capability/resource contract records (descriptor/risk/context shapes)
- [artifact] PLT.17: real ArcForges.Application.Abstractions (application identity and in-process composition), not the current placeholder assembly
- [artifact] FND.01: real ArcForges.Foundation identity/error/version primitives, not the current placeholder assembly
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:src/BuildingBlocks/ArcForges.Assistant.Abstractions/**; DesktopPlatform:tests/AssistantAbstractionsTests/**
Shared resources (follow the owner protocol): RES-desktopplatform-build-config (append): Solution/project lists, central package versions and CI job lists are appended by the task that adds a project, dependency or job; dependency additions follow the dependency-admission policy with a reviewed receipt; lock files are regenerated after rebase and never hand-merged; the integration owner resolves ordering conflicts at merge.
Unblocks: APP.02, APP.03, APP.05, APP.06, APP.07, APP.08, AST.01, EXE.01, NOTES.03, PLT.57

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline unit tests only (two identities/no shared store); Native AOT compile check; no live Cloud/device in CI per P2-017.
Completion evidence for the ledger: Source commit, Assistant.Abstractions package version/hash, two-identity isolation test results.
Notes: Root of the whole area's dependency graph; every other WP14 to WP17/26 desktop task starts from this package.
```

```text
Execute ArcForges delivery task APP.02 — Minimal ArcNotes application services (read/create/append).

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\app-composition.md (anchor task-app-02).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\ArcNotes (integration owner: ArcNotes integration owner, the holder of roles/integration-arcnotes).
Claim and handoff record: claims/app-02 (python tools/delivery.py claim APP.02 --worker <name>); task branch task/app-02 in ArcNotes; ledger record ledger/tasks/app-02.md.
Kind/size: producer/M. Baseline: not-started.
Outcome: Real read/create/append document commands through typed application handlers and local persistence, with descriptor/risk/context validation and one write path shared by UI and own-app capability invocation. Professional document completion remains WP18.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-14.01 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\14-hub-and-minimal-provider-slice.md, anchor rule-wp-14.01

Entry condition: adoption slice ADOPT.04.app-composition is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] APP.01: published Assistant.Abstractions host ports and product identity
- [artifact] PLT.24: real ICapabilityProvider.InvokeAsync invocation pipeline (owner-side decode/validate)
- [artifact] PLT.38: published security decision pipeline enforcement point
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: ArcNotes:src/ArcForges.ArcNotes.Application/**; ArcNotes:src/ArcForges.ArcNotes.Infrastructure/**; ArcNotes:tests/**
Unblocks: APP.03, APP.04, APP.08

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline unit tests (descriptor/risk/context validation, one write path); no live Cloud in CI.
Completion evidence for the ledger: Source commit, command receipt samples, validation-failure cases.
Notes: This is the ONLY product-repo work in WP14 to WP17/26; full ArcNotes document model is WP18, not here.
```

```text
Execute ArcForges delivery task APP.03 — Clean Native AOT package-consumer composition for ArcNotes.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\app-composition.md (anchor task-app-03).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\ArcNotes (integration owner: ArcNotes integration owner, the holder of roles/integration-arcnotes).
Claim and handoff record: claims/app-03 (python tools/delivery.py claim APP.03 --worker <name>); task branch task/app-03 in ArcNotes; ledger record ledger/tasks/app-03.md.
Kind/size: producer/S. Baseline: not-started.
Outcome: A clean Native AOT ArcNotes consumer built purely from published Platform/Contracts packages and in-process typed host ports; no source reference or local-RPC product loop. Package-only restore, publish/run, command/cancel/result and owner refusal proven.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-14.02 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\14-hub-and-minimal-provider-slice.md, anchor rule-wp-14.02

Entry condition: adoption slice ADOPT.04.app-composition is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] APP.01: published Assistant.Abstractions package (not project reference)
- [artifact] APP.02: published ArcNotes application-services package surface
- [artifact] PRF.04: proven Local RPC under Native AOT pattern
- [artifact] NAT.01: confirmed Native AOT device-tool/capability-invocation feasibility from the high-risk probe
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: ArcNotes:src/ArcForges.ArcNotes/**; ArcNotes:packaging/**
Unblocks: APP.08, HAR.05

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Native AOT publish/run in CI (package-only restore), offline command/cancel/result tests; no installed-package or public-release install/upgrade CI per P2-017.
Completion evidence for the ledger: AOT publish log, package hash manifest, command/cancel/result and owner-refusal test results.
Notes: Narrow early-risk proof: first real evidence that the whole Assistant.Abstractions/host-port composition model survives Native AOT package-only consumption for an actual product. Failure here invalidates the composition model assumed by WP15 to WP17.
```

```text
Execute ArcForges delivery task APP.04 — Idempotency and revision against the real store.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\app-composition.md (anchor task-app-04).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/app-04 (python tools/delivery.py claim APP.04 --worker <name>); task branch task/app-04 in DesktopPlatform; ledger record ledger/tasks/app-04.md.
Kind/size: producer/S. Baseline: not-started.
Outcome: Command receipt and expected local revision exercised against the real store; draft/conflict behavior and unknown-outcome classification preserved under duplicate command, stale revision and process-kill-around-commit.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-14.03 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\14-hub-and-minimal-provider-slice.md, anchor rule-wp-14.03

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

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\app-composition.md (anchor task-app-05).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/app-05 (python tools/delivery.py claim APP.05 --worker <name>); task branch task/app-05 in DesktopPlatform; ledger record ledger/tasks/app-05.md.
Kind/size: producer/M. Baseline: not-started.
Outcome: Expiry/modified-input/revocation cannot bypass owner checks.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-14.04 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\14-hub-and-minimal-provider-slice.md, anchor rule-wp-14.04

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

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\app-composition.md (anchor task-app-06).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/app-06 (python tools/delivery.py claim APP.06 --worker <name>); task branch task/app-06 in DesktopPlatform; ledger record ledger/tasks/app-06.md.
Kind/size: producer/M. Baseline: not-started.
Outcome: Own-app resource references frozen at selection time, preview opened through the product port, egress enforced separately, provenance preserved. Selection changes after freeze, missing resource, denied export and bounded artifact all handled.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-14.05 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\14-hub-and-minimal-provider-slice.md, anchor rule-wp-14.05

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

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\app-composition.md (anchor task-app-07).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/app-07 (python tools/delivery.py claim APP.07 --worker <name>); task branch task/app-07 in DesktopPlatform; ledger record ledger/tasks/app-07.md.
Kind/size: producer/S. Baseline: not-started.
Outcome: Launch/save works with Cloud unavailable and the assistant view closed; views dispose independently from services; two windows with different drafts and independent app crash lose no canonical data.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-14.06 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\14-hub-and-minimal-provider-slice.md, anchor rule-wp-14.06

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

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\app-composition.md (anchor task-app-08).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/app-08 (python tools/delivery.py claim APP.08 --worker <name>); task branch task/app-08 in DesktopPlatform; ledger record ledger/tasks/app-08.md.
Kind/size: acceptance/M. Baseline: not-started.
Outcome: WP14 built/packed once from a clean environment; all applicable UX acceptance groups recorded; package/contract/owner/version compatibility and failure/recovery evidence attached; no later-provider fixture used to close a real WP14 gate.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-14.90 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\14-hub-and-minimal-provider-slice.md, anchor rule-wp-14.90

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
