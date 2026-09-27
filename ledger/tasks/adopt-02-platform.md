---
task: ADOPT.02.platform
status: complete
recorded: 2026-09-27
claimant: w-20260927-platform
epoch: 1
---

# Desktop platform adoption

## Authority, scope and method

DesktopPlatform integration owner `w-20260927-dgov` (role epoch 2) assigned this slice review to `w-20260927-platform`. Reviewed the 55 platform tasks against Design `722e85641c8afb765dafcab5bc0e84d5a22d5a3c`, their WP07-WP12 obligations and PLT.54/57 integration parts, and the [frozen baseline](../adoption/baseline.md#desktopplatform). DesktopPlatform source is frozen at `e5ce94221c13d0014781a760c0865b942350be4d`. The frozen and current open-PR inventories contain no platform implementation PR. This slice changes only the Plan ledger.

Plan before editing: inspect frozen tracked source/tests and package inventory; compare each task outcome and evidence requirement; bind every write scope to retained or missing projects; classify each task separately; run the ledger consistency check; obtain peer review at the exact head and merge through the Plan integration owner. No product execution or publication verification cycle is needed.

## Evidence references and scope bindings

All source references below resolve at the frozen DesktopPlatform commit, not an unmerged working tree.

- **S**: `src/BuildingBlocks/ArcForges.Persistence.Sqlite/AssemblyPlaceholder.cs`, its project and README contain only the named scaffold; no IStore, journal, snapshot or migration implementation. `Persistence.Resources` and `Persistence.Derived` do not exist. The new projects retain those planned names; Sqlite retains its existing project/namespace. No SQLite dependency is admitted yet.
- **L**: tracked `src/BuildingBlocks` inventory contains no `ArcForges.LocalRpc` project. Add the named project for the private parent/helper transport; do not repurpose product RPC or native ABI probes.
- **C**: tracked inventory contains no `ArcForges.Capabilities` or `ArcForges.Contributions` project. Add the exact named mechanism projects; the existing `Application.Abstractions` placeholder is not a capability registry.
- **U**: `src/DesignSystem` is absent. Five retained `ArcForges.Desktop.{Experience,Graphics,Preview,RichContent,Text}` projects each contain only `AssemblyPlaceholder.cs`, project, lock and README. PLT.26/27 must explicitly reconcile these scaffolds under their mapped WP10 obligation, preserving accepted/package identities; they are no implemented shell/token behavior to inherit.
- **Q**: `src/BuildingBlocks/ArcForges.Security/AssemblyPlaceholder.cs` and its README explicitly describe an unpublished scaffold. `Security.Secrets` and `Security.Audit` are absent. Retain the Security namespace; add the named missing projects without inventing a shared product session.
- **H**: `src/DesktopHelpers/ArcForges.ContentSandbox/Program.cs` only prints Hello World. Broker and Contracts helper projects are absent. Existing native version/build/error probes provide no restricted parser containment or production transport evidence. Retain the helper identity and add the named private projects.
- **O**: `src/BuildingBlocks/ArcForges.Observability/AssemblyPlaceholder.cs` is the only implementation in that project; `Observability.Desktop` and `eng/policy/telemetry-policy.json` are absent. Retain Observability namespace and add only the planned desktop project/policy.
- **P**: `eng/packaging/packages.json` lists only Build.Policy and nine native ABI/runtime identities. No Persistence, LocalRpc, Capabilities, DesignSystem/Shell, Security or Observability capability is admitted or published. Existing candidate `1.0.0-ci.27.1` and original successful [publication run](https://github.com/ArcForges/DesktopPlatform/actions/runs/36334843593) are reused from ADOPT.01; their success certifies no PLT outcome.
- **T**: tracked tests contain architecture/build-identity/repository policy and native skeleton/oracle tests only. No task-specific PLT behavior or integration receipts exist. Add targeted validation under each task's declared scope and shared-resource protocol; a needed scope expansion must be reviewed before editing.

All new project additions require explicit solution/project inventory, central dependency admission where needed, regenerated locks and package admission only when behavior is delivered, under the declared shared-resource protocols. This is remaining task work, not inherited behavior. No package, installation identity or immutable publication is renamed by adoption.

## Per-task classification

Every row is **gap**: the full named obligation part, outcome and required evidence remain open. Evidence codes refer to the concrete frozen inputs above. Bound paths are repository-relative in DesktopPlatform. Start blockers below are the task's declared prerequisite IDs, not added lane barriers; evaluate their current merged states before claiming. There are no unresolved implementation conflicts raised by this slice. Missing implementations are gaps, not conflicts. A missing optional runtime environment must be recorded honestly by the implementing task.

| Task / remaining behavior | Classification / evidence | Bound write scope | Remaining acceptance evidence | Start prerequisite IDs |
|---|---|---|---|---|
| PLT.01: Store abstraction and the single transactional write path | gap; S/P/T | src/BuildingBlocks/ArcForges.Persistence.Sqlite/** | Single-write-path policy test result. | FND.02, FND.03, FND.05 |
| PLT.02: Append-only journal with durability and bounded truncation | gap; S/P/T | src/BuildingBlocks/ArcForges.Persistence.Sqlite/** | Durability and replay results. | FND.02, FND.03 |
| PLT.03: Snapshot and crash/corruption recovery | gap; S/P/T | src/BuildingBlocks/ArcForges.Persistence.Sqlite/** | Full recovery matrix with a named outcome per case. | PLT.02 |
| PLT.04: Migration runner | gap; S/P/T | src/BuildingBlocks/ArcForges.Persistence.Sqlite/**; fixtures/formats/** | Migration results against every historical fixture plus semantic comparison. | FND.06 |
| PLT.05: Managed resource store (content-addressed blobs) | gap; S/P/T | src/BuildingBlocks/ArcForges.Persistence.Resources/** | Integrity, reference-counting and garbage-collection safety results. | PLT.01 |
| PLT.06: Large append store for high-rate chunked data | gap; S/P/T | src/BuildingBlocks/ArcForges.Persistence.Resources/** | Append-under-kill results with loss records. | FND.02 |
| PLT.07: Derived-store abstraction and storage-pressure model | gap; S/P/T | src/BuildingBlocks/ArcForges.Persistence.Derived/** | Rebuild and eviction results. | PLT.01 |
| PLT.08: Publish Persistence packages and verify real integration | gap; S/P/T | eng/packaging/packages.json; eng/version-sources.json | Owned artifact and real-integration receipt per the WP-07.90 template. | PLT.01, PLT.02, PLT.03, PLT.04, PLT.05, PLT.06, PLT.07 |
| PLT.09: Local gRPC transport and framing over Named Pipe/UDS | gap; L/P/T | src/BuildingBlocks/ArcForges.LocalRpc/** | Actual OS streams, malformed frames, wrong-user denial and no local TCP listener. | PRF.04, CON.04 |
| PLT.10: Parent-owned endpoint identity | gap; L/P/T | src/BuildingBlocks/ArcForges.LocalRpc/** | Concurrent launch, stale descriptor, forged nonce/build and parent-death cleanup results. | PLT.09 |
| PLT.11: Child registration lifecycle | gap; L/P/T | src/BuildingBlocks/ArcForges.LocalRpc/** | Expired/stale child cannot call; parent restart requires fresh grants. | PLT.10 |
| PLT.12: Static routing and version refusal | gap; L/P/T | src/BuildingBlocks/ArcForges.LocalRpc/** | Version mismatch and unregistered service refusal. | PLT.11 |
| PLT.13: Bounds and concurrency | gap; L/P/T | src/BuildingBlocks/ArcForges.LocalRpc/** | Queue/memory bound, fairness, timeout and typed overload. | PLT.09 |
| PLT.14: Disconnect, cancel and retry semantics | gap; L/P/T | src/BuildingBlocks/ArcForges.LocalRpc/** | Kill before/after commit, lost ack and unknown effect. | PLT.09, FND.02 |
| PLT.15: Brokered large data over the sandbox boundary | gap; L/P/T | src/BuildingBlocks/ArcForges.LocalRpc/** | Wrong resource grant, range/hash/expiry/cancel and orphan cleanup. | PLT.09, CON.04 |
| PLT.16: Publish LocalRpc package and verify real integration | gap; L/P/T | eng/packaging/packages.json | Exact artifact/consumer and applicable UX acceptance ledger. | PLT.09, PLT.10, PLT.11, PLT.12, PLT.13, PLT.14, PLT.15 |
| PLT.17: Application identity and in-process composition | gap; C/P/T | src/BuildingBlocks/ArcForges.Capabilities/** | Identity lifecycle matrix. | CON.91, FND.01 |
| PLT.18: Static contribution registration | gap; C/P/T | src/BuildingBlocks/ArcForges.Contributions/** | Registration idempotency and namespace refusal results. | PLT.17 |
| PLT.19: Capability registry and selection | gap; C/P/T | src/BuildingBlocks/ArcForges.Capabilities/** | Selection priority, determinism and explainability results. | PLT.17, CON.91 |
| PLT.20: Actions and availability | gap; C/P/T | src/BuildingBlocks/ArcForges.Capabilities/** | Availability reason matrix and purity assertion. | PLT.19 |
| PLT.21: Context providers and freezing | gap; C/P/T | src/BuildingBlocks/ArcForges.Capabilities/** | Context freezing and size-bound results. | PLT.17 |
| PLT.22: Resources and artifacts resolution | gap; C/P/T | src/BuildingBlocks/ArcForges.Capabilities/** | Resource resolution matrix and structural path prohibition. | PLT.05, PLT.17 |
| PLT.23: Own navigation, hints and health | gap; C/P/T | src/BuildingBlocks/ArcForges.Capabilities/** | Deep-link hostile-input, event and health results. | PLT.22 |
| PLT.24: Invocation pipeline | gap; C/P/T | src/BuildingBlocks/ArcForges.Capabilities/** | Pipeline bypass-prohibition, error-mapping and tracing results. | PLT.19, PLT.20, PLT.21 |
| PLT.25: Publish Capabilities/Contributions packages and verify real integration | gap; C/P/T | eng/packaging/packages.json; eng/version-sources.json | Owned artifact and real-integration receipt per the WP-09.90 template. | PLT.17, PLT.18, PLT.19, PLT.20, PLT.21, PLT.22, PLT.23, PLT.24, PLT.57 |
| PLT.26: Token system and theming | gap; U/P/T | src/DesignSystem/ArcForges.DesignSystem/** | Raw-literal policy result and contrast reports per theme. | PRF.02 |
| PLT.27: Windows, panels and layout | gap; U/P/T | src/DesignSystem/ArcForges.Desktop.Shell/** | Layout restore matrix. | PLT.26 |
| PLT.28: Command system | gap; U/P/T | src/DesignSystem/ArcForges.Desktop.Shell/** | Shortcut conflict and availability agreement results. | PLT.27, PLT.20 |
| PLT.29: Scoped settings | gap; U/P/T | src/DesignSystem/ArcForges.Desktop.Shell/** | Settings resolution and explainability results. | PLT.26, PLT.04 |
| PLT.30: Attention and notification model | gap; U/P/T | src/DesignSystem/ArcForges.Desktop.Shell/** | Missed-notification durability result. | PLT.27 |
| PLT.31: Error presentation | gap; U/P/T | src/DesignSystem/ArcForges.Desktop.Shell/** | Raw-exception prohibition and reason-code coverage. | PLT.26, FND.05 |
| PLT.32: Lifecycle, menus and shutdown | gap; U/P/T | src/DesignSystem/ArcForges.Desktop.Shell/** | Startup budget measurements and shutdown-during-work result. | PLT.28 |
| PLT.33: Accessibility and localisation baseline | gap; U/P/T | src/DesignSystem/ArcForges.Desktop.Shell/**; tests/DesktopUiTests/** | Accessibility automated plus dated manual record; pseudo-localisation report. | PLT.27 |
| PLT.34: Third-party control admission | gap; U/P/T | src/DesignSystem/**; docs/** | Per-control AOT proofs and licence records. | PRF.02 |
| PLT.35: Publish DesignSystem/Shell packages and verify real integration | gap; U/P/T | eng/packaging/packages.json | Owned artifact and real-integration receipt per WP-10.90. | PLT.26, PLT.27, PLT.28, PLT.29, PLT.30, PLT.31, PLT.32, PLT.33, PLT.34 |
| PLT.36: Principals and the actor chain | gap; Q/P/T | src/BuildingBlocks/ArcForges.Security/** | Actor chain propagation and completeness results. | FND.01 |
| PLT.37: Risk model and classification | gap; Q/P/T | src/BuildingBlocks/ArcForges.Security/** | Risk classification and monotonicity matrix. | PLT.19 |
| PLT.38: Decision pipeline and the four enforcement points | gap; Q/P/T | src/BuildingBlocks/ArcForges.Security/**; src/BuildingBlocks/ArcForges.Capabilities/** | Pipeline bypass, step-coverage and refusal matrix. | PLT.36, PLT.37, PLT.10 |
| PLT.39: Approval, steering and step-up | gap; Q/P/T | src/BuildingBlocks/ArcForges.Security/** | Approval, steering and step-up results. | PLT.37, PLT.01 |
| PLT.40: Per-application secrets and session isolation | gap; Q/P/T | src/BuildingBlocks/ArcForges.Security.Secrets/** | Secret structural prohibitions and platform round-trip results. | PLT.36 |
| PLT.41: Egress control | gap; Q/P/T | src/BuildingBlocks/ArcForges.Security/** | Egress authorization matrix and audit assertions. | PLT.38 |
| PLT.42: Instruction provenance | gap; Q/P/T | src/BuildingBlocks/ArcForges.Security/** | Injection corpus results and marking coverage. | PLT.21 |
| PLT.43: Capability leases and trust | gap; Q/P/T | src/BuildingBlocks/ArcForges.Security/** | Lease expiry, revocation and trust-separation results. | PLT.38, PLT.01 |
| PLT.44: Append-only audit subsystem | gap; Q/P/T | src/BuildingBlocks/ArcForges.Security.Audit/** | Audit immutability, completeness and separation results. | PLT.36, PLT.01 |
| PLT.45: Content helper and OS-enforced isolation (ContentSandbox host) | gap; H/Q/P/T | src/DesktopHelpers/ArcForges.ContentSandbox.Broker/**; src/DesktopHelpers/ArcForges.ContentSandbox.Contracts/**; src/DesktopHelpers/ArcForges.ContentSandbox/** | Real child attempts at product-DB/token reads, outbound TCP/UDP/loopback, sibling-process access, spawn escape, oversized output; OS denial, resource bounds and parent-death cleanup on every supported RID. | PLT.15, PLT.09, CON.04 |
| PLT.46: Publish Security packages and verify real integration | gap; Q/P/T | eng/packaging/packages.json | Cross-boundary owner refusal, stale approval/revocation, secrets/redaction and real OS-isolation tests per WP-11.90. | PLT.36, PLT.37, PLT.38, PLT.39, PLT.40, PLT.41, PLT.42, PLT.43, PLT.44, PLT.45, PLT.54, PLT.57 |
| PLT.47: Emission and required dimensions | gap; O/P/T | src/BuildingBlocks/ArcForges.Observability/** | Dimension coverage report. | FND.01 |
| PLT.48: Correlation and causation propagation | gap; O/P/T | src/BuildingBlocks/ArcForges.Observability/** | A single connected trace across every available hop kind. | PLT.47 |
| PLT.49: Redaction by construction | gap; O/P/T | src/BuildingBlocks/ArcForges.Observability/**; eng/policy/telemetry-policy.json | Marker-injection redaction report, zero findings - satisfies PG-05. | PLT.40, FND.05 |
| PLT.50: Cardinality and sampling | gap; O/P/T | src/BuildingBlocks/ArcForges.Observability/**; eng/policy/telemetry-policy.json | Cardinality negative fixture and sampling retention results. | PLT.49 |
| PLT.51: Health probes | gap; O/P/T | src/BuildingBlocks/ArcForges.Observability/** | Health probe fail-closed and degradation results. | PLT.23 |
| PLT.52: Desktop diagnostics and consent | gap; O/P/T | src/BuildingBlocks/ArcForges.Observability.Desktop/** | Consent-absent, crash-approval, verbose-expiry and revocation results. | PLT.31, PLT.49 |
| PLT.53: Publish Observability packages and verify real integration | gap; O/P/T | eng/packaging/packages.json | Owned artifact and real-integration receipt per WP-12.90. | PLT.47, PLT.48, PLT.49, PLT.50, PLT.51, PLT.52 |
| PLT.54: Real hostile-input containment proof with production parser libraries loaded in ContentSandbox | gap; H/T | Evidence-only integration task; graph declares no source write scope. Resolve any required source edit through planning first. | that PG-12/PG-22's OS isolation mechanics (proven against a first-party hostile test parser in PLT.45) hold once real PDFium/OpenImageIO composition is loaded into the same helper by WP-13.13 ; this is the point where the SUB-hostile-test-parser substitute is actually replaced. | PLT.45, NAT.14 |
| PLT.57: End-to-end capability invocation with real security enforcement inside one product | gap; C/Q/T | Evidence-only integration task; graph declares no source write scope. Resolve any required source edit through planning first. | that the WP-09.07 invocation pipeline's 'authorize' step, wired to the real WP-11.02 decision pipeline, actually gates a real product capability end to end (resolve -> availability -> freeze -> authorize -> invoke -> validate -> record -> audit), closing the IAuthorizer interface seam both PLT.24 and PLT.38 are built against. | PLT.24, PLT.38, APP.01 |

## Completion and limits

Result: 55 gaps; zero inherited, inherited-with-adjustment or conflicting tasks. No inherited task records are created. Merging this record opens these 55 tasks only subject to their own dependencies; it does not complete any PLT implementation. PLT.54 still needs NAT.14 and PLT.57 still needs APP.01, which are outside the current launcher's implementation selection and are not silently added.

Retired native family bindings and legacy policy export remain cleanup owned by GOV.17/GOV.18 under ADP-10; their existing publication is not PLT capability evidence. This slice neither changes nor certifies that cleanup.

Validation: frozen tracked inventory/source inspection, mapped task outcome/obligation/evidence comparison, package inventory and existing baseline receipt reuse, plus `delivery.py check` with explicit Plan worktree and Design roots. No product builds, package downloads, public-byte checks, installed consumers, GUI/runtime, OS containment or live-service checks ran. All platform behavior remains untested until its implementation task supplies evidence. No substitutes are newly introduced or certified here.

Ledger PR review/merge metadata is recorded in the claim and the PR at its exact head; this record makes no self-referential future commit claim.
