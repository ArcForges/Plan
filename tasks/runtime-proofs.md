# ArcForges delivery task prompts — Runtime proofs

Generated from Design `docs/planning/delivery/delivery-graph.json` by `tools/delivery.py`; do not edit by hand.
Each block is self-contained. Claim a task only when `python tools/delivery.py ready` lists it, with
`python tools/delivery.py claim <TASK-ID> --worker <name>`, then follow `arcforges-implementation.md`.
Tasks are ordered by lane for reading; the order is not a schedule.

## Runtime proofs

```text
Execute ArcForges delivery task PRF.01 — ArcNotes desktop Native AOT package proof.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\runtime-proofs.md (anchor task-prf-01).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\ArcNotes (integration owner: ArcNotes integration owner, the holder of roles/integration-arcnotes).
Claim and handoff record: claims/prf-01 (python tools/delivery.py claim PRF.01 --worker <name>); task branch task/prf-01 in ArcNotes; ledger record ledger/tasks/prf-01.md.
Kind/size: proof/M. Baseline: not-started.
Outcome: ArcForges.ArcNotes publishes self-contained Native AOT per Tier-1/Tier-2 RID, launches without a machine runtime, loads real native libraries and passes existing ABI smoke vectors with no reflection/sibling-source fallback; wired into continuous main-branch CI (BR-06).

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-06.00 (ArcNotes host only): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\06-aot-jit-and-wasm-publish-proof.md, anchor rule-wp-06.00
- WP-06:ss8-completion-gate-item-9-br-06-every-p SS8 completion gate item 9 / BR-06: every proof runs continuously on main-branch builds, not once (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\06-aot-jit-and-wasm-publish-proof.md, package-level obligation

Entry condition: adoption slice ADOPT.04.runtime-proofs is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [contract] CON.91: ArcForges.Contracts.Foundation/LocalRpc.Notes published package
- [artifact] FND.01: Foundation/Application.Abstractions identity/error primitives
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: ArcNotes:src/ArcForges.ArcNotes/**; ArcNotes:ArcNotes.slnx
Shared resources (follow the owner protocol): RES-arcnotes-build-config (append): Solution/project lists, central package versions and CI job lists are appended by the task that adds a project, dependency or job; dependency additions follow the dependency-admission policy with a reviewed receipt; lock files are regenerated after rebase and never hand-merged; the integration owner resolves ordering conflicts at merge.; RES-desktopplatform-native-build (append): The vcpkg baseline and overlay ports change only through a dependency-admission change with licence and provenance receipts; each native family adds its own CMake targets and workflow entries; triplet or port changes are rebased and rebuilt by their author; CPU-heavy native builds use the workstation build slot.; RES-product-solutions (append): Solution/project lists, central package versions and CI job lists are appended by the task that adds a project, dependency or job; dependency additions follow the dependency-admission policy with a reviewed receipt; lock files are regenerated after rebase and never hand-merged; the integration owner resolves ordering conflicts at merge.; RES-workstation-build-slot (exclusive): Exclusive per workstation for the duration of each CPU-heavy local build or test, through the workstation lock rather than a Plan lease: run the command as `python tools/delivery.py build-slot run --worker <name> --task <task> -- <command>` with the Plan repository tool, which holds the lock directory `.arcforges/build-slot` in the user profile with an owner record and heartbeat and recovers a lock whose holder stopped. Coding and review continue while a build waits; CI capacity is not limited by this rule.
Unblocks: NAT.04, NAT.29, PLT.26, PLT.34, UPD.08

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Windows/Linux local Native AOT publish with zero trim/AOT/single-file diagnostics (BR-04); real per-RID launch and ABI smoke vectors; no macOS CI (P2-017), local-opt-in macOS only
Completion evidence for the ledger: Per-RID AOT publish log with zero-diagnostic assertion; smoke-vector pass log; continuous main-branch CI run reference
Notes: Runs in parallel with PRF.02/PRF.03 (different repos, no shared write scope).
```

```text
Execute ArcForges delivery task PRF.02 — ArcScope desktop Native AOT package proof.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\runtime-proofs.md (anchor task-prf-02).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\ArcScope (integration owner: ArcScope integration owner, the holder of roles/integration-arcscope).
Claim and handoff record: claims/prf-02 (python tools/delivery.py claim PRF.02 --worker <name>); task branch task/prf-02 in ArcScope; ledger record ledger/tasks/prf-02.md.
Kind/size: proof/M. Baseline: not-started.
Outcome: ArcForges.ArcScope publishes self-contained Native AOT per Tier-1/Tier-2 RID, launches without a machine runtime, loads real native libraries and passes existing ABI smoke vectors; wired into continuous main-branch CI.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-06.00 (ArcScope host only): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\06-aot-jit-and-wasm-publish-proof.md, anchor rule-wp-06.00
- WP-06:ss8-completion-gate-item-9-br-06-every-p SS8 completion gate item 9 / BR-06: every proof runs continuously on main-branch builds, not once (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\06-aot-jit-and-wasm-publish-proof.md, package-level obligation

Entry condition: adoption slice ADOPT.05.runtime-proofs is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [contract] CON.91: ArcForges.Contracts.Foundation/LocalRpc.Scope published package
- [artifact] FND.01: Foundation/Application.Abstractions identity/error primitives
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: ArcScope:src/ArcForges.ArcScope/**; ArcScope:ArcScope.slnx
Shared resources (follow the owner protocol): RES-desktopplatform-native-build (append): The vcpkg baseline and overlay ports change only through a dependency-admission change with licence and provenance receipts; each native family adds its own CMake targets and workflow entries; triplet or port changes are rebased and rebuilt by their author; CPU-heavy native builds use the workstation build slot.; RES-product-solutions (append): Solution/project lists, central package versions and CI job lists are appended by the task that adds a project, dependency or job; dependency additions follow the dependency-admission policy with a reviewed receipt; lock files are regenerated after rebase and never hand-merged; the integration owner resolves ordering conflicts at merge.; RES-workstation-build-slot (exclusive): Exclusive per workstation for the duration of each CPU-heavy local build or test, through the workstation lock rather than a Plan lease: run the command as `python tools/delivery.py build-slot run --worker <name> --task <task> -- <command>` with the Plan repository tool, which holds the lock directory `.arcforges/build-slot` in the user profile with an owner record and heartbeat and recovers a lock whose holder stopped. Coding and review continue while a build waits; CI capacity is not limited by this rule.
Unblocks: NAT.29

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Windows/Linux local Native AOT publish with zero trim/AOT/single-file diagnostics; real per-RID launch and ABI smoke vectors; no macOS CI
Completion evidence for the ledger: Per-RID AOT publish log with zero-diagnostic assertion; smoke-vector pass log; continuous main-branch CI run reference
Notes: Runs in parallel with PRF.01/PRF.03.
```

```text
Execute ArcForges delivery task PRF.03 — ArcSlate desktop Native AOT package proof.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\runtime-proofs.md (anchor task-prf-03).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\ArcSlate (integration owner: ArcSlate integration owner, the holder of roles/integration-arcslate).
Claim and handoff record: claims/prf-03 (python tools/delivery.py claim PRF.03 --worker <name>); task branch task/prf-03 in ArcSlate; ledger record ledger/tasks/prf-03.md.
Kind/size: proof/M. Baseline: not-started.
Outcome: ArcForges.ArcSlate publishes self-contained Native AOT per Tier-1/Tier-2 RID, launches without a machine runtime, loads real native libraries and passes existing ABI smoke vectors; wired into continuous main-branch CI.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-06.00 (ArcSlate host only): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\06-aot-jit-and-wasm-publish-proof.md, anchor rule-wp-06.00
- WP-06:ss8-completion-gate-item-9-br-06-every-p SS8 completion gate item 9 / BR-06: every proof runs continuously on main-branch builds, not once (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\06-aot-jit-and-wasm-publish-proof.md, package-level obligation

Entry condition: adoption slice ADOPT.06.runtime-proofs is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [contract] CON.91: ArcForges.Contracts.Foundation/LocalRpc.Slate published package
- [artifact] FND.01: Foundation/Application.Abstractions identity/error primitives
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: ArcSlate:src/ArcForges.ArcSlate/**; ArcSlate:ArcSlate.slnx
Shared resources (follow the owner protocol): RES-desktopplatform-native-build (append): The vcpkg baseline and overlay ports change only through a dependency-admission change with licence and provenance receipts; each native family adds its own CMake targets and workflow entries; triplet or port changes are rebased and rebuilt by their author; CPU-heavy native builds use the workstation build slot.; RES-product-solutions (append): Solution/project lists, central package versions and CI job lists are appended by the task that adds a project, dependency or job; dependency additions follow the dependency-admission policy with a reviewed receipt; lock files are regenerated after rebase and never hand-merged; the integration owner resolves ordering conflicts at merge.; RES-workstation-build-slot (exclusive): Exclusive per workstation for the duration of each CPU-heavy local build or test, through the workstation lock rather than a Plan lease: run the command as `python tools/delivery.py build-slot run --worker <name> --task <task> -- <command>` with the Plan repository tool, which holds the lock directory `.arcforges/build-slot` in the user profile with an owner record and heartbeat and recovers a lock whose holder stopped. Coding and review continue while a build waits; CI capacity is not limited by this rule.
Unblocks: NAT.29

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Windows/Linux local Native AOT publish with zero trim/AOT/single-file diagnostics; real per-RID launch and ABI smoke vectors; no macOS CI
Completion evidence for the ledger: Per-RID AOT publish log with zero-diagnostic assertion; smoke-vector pass log; continuous main-branch CI run reference
Notes: Runs in parallel with PRF.01/PRF.02.
```

```text
Execute ArcForges delivery task PRF.04 — Local RPC under AOT: bidirectional named-pipe/UDS probe processes.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\runtime-proofs.md (anchor task-prf-04).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/prf-04 (python tools/delivery.py claim PRF.04 --worker <name>); task branch task/prf-04 in DesktopPlatform; ledger record ledger/tasks/prf-04.md.
Kind/size: proof/L. Baseline: not-started.
Outcome: Two published AOT desktop probe processes complete LocalBootstrap over Kestrel HTTP/2 named-pipe (Windows) / UDS (Linux/macOS), authenticate same-user peers, register both endpoint directions, invoke generated services, cancel, disconnect and reattach; malformed-input/unauthorized-peer/bounded-resource negative tests pass.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-06.01 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\06-aot-jit-and-wasm-publish-proof.md, anchor rule-wp-06.01
- WP-06:ss8-completion-gate-item-9-br-06-every-p SS8 completion gate item 9 / BR-06: every proof runs continuously on main-branch builds, not once (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\06-aot-jit-and-wasm-publish-proof.md, package-level obligation

Entry condition: adoption slice ADOPT.02.runtime-proofs is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [contract] CON.05: local RPC generated server/client codegen (LocalBootstrap, ConnectCallback surface)
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:tests/LocalRpcAotTests/**; DesktopPlatform:eng/verification/**
Shared resources (follow the owner protocol): RES-workstation-build-slot (exclusive): Exclusive per workstation for the duration of each CPU-heavy local build or test, through the workstation lock rather than a Plan lease: run the command as `python tools/delivery.py build-slot run --worker <name> --task <task> -- <command>` with the Plan repository tool, which holds the lock directory `.arcforges/build-slot` in the user profile with an owner record and heartbeat and recovers a lock whose holder stopped. Coding and review continue while a build waits; CI capacity is not limited by this rule.
Unblocks: APP.03, NAT.01, NAT.29, PLT.09

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Actual Windows/Linux/macOS(local opt-in) process-to-process runs; no in-memory or TCP substitute (explicit design prohibition); malformed input, unauthorized peer, bounded resource tests
Completion evidence for the ledger: Cross-process AOT RPC integration results satisfying VG-04
Notes: Directly closes VG-04. Independent of PRF.01-03 (uses its own dedicated probe processes, not the product hosts).
```

```text
Execute ArcForges delivery task PRF.05 — Generated gRPC-Web under AOT against deployed Worker/Container ingress.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\runtime-proofs.md (anchor task-prf-05).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/prf-05 (python tools/delivery.py claim PRF.05 --worker <name>); task branch task/prf-05 in DesktopPlatform; ledger record ledger/tasks/prf-05.md.
Kind/size: proof/M. Baseline: not-started.
Outcome: A published AOT desktop probe calls the real generated binary gRPC-Web client against actual deployed Worker/Container ingress, proving headers, trailers, cancellation, scoped errors and exact primitives; F-026 closes on this artifact.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-06.02 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\06-aot-jit-and-wasm-publish-proof.md, anchor rule-wp-06.02
- WP-06:ss8-completion-gate-item-9-br-06-every-p SS8 completion gate item 9 / BR-06: every proof runs continuously on main-branch builds, not once (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\06-aot-jit-and-wasm-publish-proof.md, package-level obligation

Entry condition: adoption slice ADOPT.02.runtime-proofs is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [contract] CON.92: ArcForges.Sdk.Client / generated gRPC-Web client, AOT-clean per accepted WP03.02 evidence
- [artifact] PRF.07: a deployed Worker/Container ingress endpoint (from WP-06.04)
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:tests/ReleaseArtifactTests/**; DesktopPlatform:eng/verification/**
Unblocks: AST.11, NAT.29

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Production browser-equivalent round trip against real AOT host + deployed CF; scope/permission, wrong/stale target, loss/retry, expiry cases; local opt-in only, not hosted CI
Completion evidence for the ledger: Dependency-graph and negative build-test results for the typed client; F-026 closure evidence
Notes: Start-depends on PRF.07 (same area) for the deployed ingress target.
```

```text
Execute ArcForges delivery task PRF.06 — Realtime (EventService.Watch/Poll) under AOT.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\runtime-proofs.md (anchor task-prf-06).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/prf-06 (python tools/delivery.py claim PRF.06 --worker <name>); task branch task/prf-06 in DesktopPlatform; ledger record ledger/tasks/prf-06.md.
Kind/size: proof/M. Baseline: not-started.
Outcome: A published AOT desktop probe proves EventService.Watch and output server streams plus Poll/readOutput recovery from annex 10 against actual Worker/Container/DO, including drop/expire/revoke and recovery through authoritative reads; no SignalR dependency, no claimed hint durability beyond what is proven.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-06.03 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\06-aot-jit-and-wasm-publish-proof.md, anchor rule-wp-06.03
- WP-06:ss8-completion-gate-item-9-br-06-every-p SS8 completion gate item 9 / BR-06: every proof runs continuously on main-branch builds, not once (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\06-aot-jit-and-wasm-publish-proof.md, package-level obligation

Entry condition: adoption slice ADOPT.02.runtime-proofs is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] PRF.07: deployed Worker/Container/DO providing EventService.Watch
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:tests/ReleaseArtifactTests/**; DesktopPlatform:eng/verification/**
Unblocks: NAT.29

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Real deployed DO/Worker realtime round trip; scope/permission, stale target, loss/retry, expiry cases; local opt-in only
Completion evidence for the ledger: AOT realtime reconnection results
Notes: Runs after PRF.07 stands up DO/Worker; independent of PRF.04/05 otherwise.
```

```text
Execute ArcForges delivery task PRF.07 — Cloudflare Native AOT host + D1 + DO/Queue/R2 foundation proof.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\runtime-proofs.md (anchor task-prf-07).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/prf-07 (python tools/delivery.py claim PRF.07 --worker <name>); task branch task/prf-07 in Cloud; ledger record ledger/tasks/prf-07.md.
Kind/size: proof/XL. Baseline: not-started.
Outcome: ArcForges.Cloud.Host publishes/deploys as a Linux x64 Native AOT container with the real private Worker D1 binding, DO/Queue/R2 foundation, rollback on guard failure, exact 64-bit/decimal handling, session/CSRF/revoke and bounded checkpoint/restart; zero trim/AOT diagnostics; VG-06 is supported (not yet closed platform-wide, since VG-06 is also maintained by WP-21.00/WP-50.04).

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-06.04 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\06-aot-jit-and-wasm-publish-proof.md, anchor rule-wp-06.04
- WP-06:ss8-completion-gate-item-9-br-06-every-p SS8 completion gate item 9 / BR-06: every proof runs continuously on main-branch builds, not once (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\06-aot-jit-and-wasm-publish-proof.md, package-level obligation

Entry condition: adoption slice ADOPT.07.runtime-proofs is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [contract] CON.92: ArcForges.Contracts.CloudInternal, native auth exception/catalog/index/revocation/realm schemas and independent signed vectors (fixture keys per WP02/06)
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Cloud:src/Cloud/ArcForges.Cloud.Host/**; Cloud:eng/verification/**
Shared resources (follow the owner protocol): RES-workstation-build-slot (exclusive): Exclusive per workstation for the duration of each CPU-heavy local build or test, through the workstation lock rather than a Plan lease: run the command as `python tools/delivery.py build-slot run --worker <name> --task <task> -- <command>` with the Plan repository tool, which holds the lock directory `.arcforges/build-slot` in the user profile with an owner record and heartbeat and recovers a lock whose holder stopped. Coding and review continue while a build waits; CI capacity is not limited by this rule.
Permitted substitutes (never real integration evidence): SUB-signed-format-fixture-keys: signature/hash verification mechanics, expired/revoked/unknown-key refusal, malformed/rollback/mixed-shard handling Real producer ['UPD.07']; removed by REL.11
Unblocks: CLOUD.25, NAT.29, PRF.05, PRF.06, PRF.08, PRF.10

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Native AOT compilation required; real-adapter runtime verification is scoped local opt-in per V-03/P2-017; no EF/dynamic ORM/ASP.NET Session/CookieAuthenticationHandler; chiseled Ubuntu image, non-root, read-only root
Completion evidence for the ledger: Cloud image build, pipeline order and integration results; VG-06 supporting evidence
Notes: This is the foundation every other Cloud-touching PRF task (05, 06, 08, 10) depends on.
```

```text
Execute ArcForges delivery task PRF.08 — React production build and generated TS SDK proof.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\runtime-proofs.md (anchor task-prf-08).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Web (integration owner: Web integration owner, the holder of roles/integration-web).
Claim and handoff record: claims/prf-08 (python tools/delivery.py claim PRF.08 --worker <name>); task branch task/prf-08 in Web; ledger record ledger/tasks/prf-08.md.
Kind/size: proof/L. Baseline: not-started.
Outcome: Minimal Account/Chat production React profiles build from Web root locks using the exact released generated gRPC-Web SDK, call the real AOT Cloud probe through same-origin routing/cookie/CSRF, exercise exact values/typed failures/cancellation and CF authenticated presentation; asset/interaction budgets measured; esproj and portable npm entry points proven. Contributes the foundation slice of PG-23 only.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-06.05 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\06-aot-jit-and-wasm-publish-proof.md, anchor rule-wp-06.05
- WP-06:ss8-completion-gate-item-9-br-06-every-p SS8 completion gate item 9 / BR-06: every proof runs continuously on main-branch builds, not once (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\06-aot-jit-and-wasm-publish-proof.md, package-level obligation

Entry condition: adoption slice ADOPT.09.runtime-proofs is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [contract] CON.92: @arcforges/api-client generated TS gRPC-Web client, AOT-irrelevant but descriptor/compat-checked
- [artifact] PRF.07: a deployed Cloud AOT probe reachable same-origin through CF
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Web:src/Web/ArcForges.Web.App/**; Web:apps/**
Permitted substitutes (never real integration evidence): SUB-web-msw-fixtures: Generated-contract request and response shapes in the browser only; MSW handlers stay test-only and are excluded from release bundles. Real producer ['CLOUD.19', 'CLOUD.21']; removed by WEB.30
Unblocks: NAT.29, WEB.30

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Production Node/npm build, no dev server; browser/CSP/visual/bundle-budget checks; malformed frame/status and session-expiry cases; Windows win.slnx/esproj + portable npm entry points
Completion evidence for the ledger: Production Web build, load and bundle baseline; PG-23 foundation contribution
Notes: Lower novel-technology risk than the native/AOT proofs (React/Node toolchain is well understood); still a required PG-23 contribution.
```

```text
Execute ArcForges delivery task PRF.09 — Third-party control AOT admission gate and first candidate.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\runtime-proofs.md (anchor task-prf-09).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/prf-09 (python tools/delivery.py claim PRF.09 --worker <name>); task branch task/prf-09 in DesktopPlatform; ledger record ledger/tasks/prf-09.md.
Kind/size: proof/S. Baseline: not-started.
Outcome: The process for admitting a third-party UI control into an AOT deliverable is documented and exercised once against a real candidate control published AOT with zero diagnostics; schedules VG-03 for WP10.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-06.06 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\06-aot-jit-and-wasm-publish-proof.md, anchor rule-wp-06.06
- WP-06:ss8-completion-gate-item-9-br-06-every-p SS8 completion gate item 9 / BR-06: every proof runs continuously on main-branch builds, not once (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\06-aot-jit-and-wasm-publish-proof.md, package-level obligation

Entry condition: adoption slice ADOPT.02.runtime-proofs is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [design] PLT.34: a candidate third-party control the desktop shell actually intends to use
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:eng/verification/probe-evidence/**
Unblocks: NAT.29

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Single probe-host AOT publish with zero diagnostics for the first candidate
Completion evidence for the ledger: Probe publish log for the first candidate
Notes: Low coupling; can run independent of PRF.01-08. Formally schedules VG-03 to WP10, not itself.
```

```text
Execute ArcForges delivery task PRF.10 — Android Kotlin/Jetpack Compose gRPC-Web and CF proof.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\runtime-proofs.md (anchor task-prf-10).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Mobile (integration owner: Mobile integration owner, the holder of roles/integration-mobile).
Claim and handoff record: claims/prf-10 (python tools/delivery.py claim PRF.10 --worker <name>); task branch task/prf-10 in Mobile; ledger record ledger/tasks/prf-10.md.
Kind/size: proof/L. Baseline: not-started.
Outcome: A Kotlin Android release build consumes the actual Maven Connect Kotlin gRPC-Web client, exercises unary/server-stream/trailers/cancel/Keystore against real Worker/Container/D1/DO/R2 foundation; the compatible actual toolchain is pinned after proof. Closes VG-07 and the first-artifact leg of F-023 (already CLOSED for the inspected android-0.1.0-ci.14.1 replacement per the gates register, but reopens on dependency/resource change).

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-06.07 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\06-aot-jit-and-wasm-publish-proof.md, anchor rule-wp-06.07
- WP-06:ss8-completion-gate-item-9-br-06-every-p SS8 completion gate item 9 / BR-06: every proof runs continuously on main-branch builds, not once (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\06-aot-jit-and-wasm-publish-proof.md, package-level obligation

Entry condition: adoption slice ADOPT.10.runtime-proofs is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [contract] CON.90: io.github.arcforges:contracts-connect-client Maven artifact (public schema only, Connect Kotlin generated client)
- [artifact] PRF.07: deployed Worker/Container/D1/DO/R2 foundation
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Mobile:app/**; Mobile:gradle/**
Shared resources (follow the owner protocol): RES-workstation-build-slot (exclusive): Exclusive per workstation for the duration of each CPU-heavy local build or test, through the workstation lock rather than a Plan lease: run the command as `python tools/delivery.py build-slot run --worker <name> --task <task> -- <command>` with the Plan repository tool, which holds the lock directory `.arcforges/build-slot` in the user profile with an owner record and heartbeat and recovers a lock whose holder stopped. Coding and review continue while a build waits; CI capacity is not limited by this rule.
Unblocks: AND.01, CLOUD.26, NAT.29

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Actual device/service/native-adapter tests; scope/permission, wrong/stale target, loss/retry, expiry cases; CI builds the release artifact, device checks are local opt-in under P2-017
Completion evidence for the ledger: Pre-artifact Apache closure and Android/device/native/CF proof
Notes: Different runtime family (Kotlin/JVM) from the rest of WP06 -- genuine independent risk axis.
```
