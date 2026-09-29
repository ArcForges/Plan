# ArcForges delivery task prompts — Runtime proofs

Generated from Design `docs/planning/delivery/delivery-graph.json` by `tools/delivery.py`; do not edit by hand.
Each block is self-contained. Claim a task only when `python tools/delivery.py ready` lists it, with
`python tools/delivery.py claim <TASK-ID> --worker <name>`, then follow `arcforges-implementation.md`.
Tasks are ordered by lane for reading; the order is not a schedule.

## Runtime proofs

```text
Execute ArcForges delivery task PRF.02 — ArcScope desktop Native AOT package proof.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\runtime-proofs.md (anchor task-prf-02).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\ArcScope (integration owner: ArcScope integration owner, the holder of roles/integration-arcscope).
Claim and handoff record: claims/prf-02 (python tools/delivery.py claim PRF.02 --worker <name>); task branch task/prf-02 in ArcScope; ledger record ledger/tasks/prf-02.md.
Kind/size: proof/M. Baseline: not-started.
Outcome: ArcForges.ArcScope publishes self-contained Native AOT per Tier-1/Tier-2 RID, launches without a machine runtime, loads real native libraries and passes existing ABI smoke vectors; wired into continuous main-branch CI.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-06.00 (ArcScope host only): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\06-aot-jit-and-wasm-publish-proof.md, anchor rule-wp-06.00
- WP-06:ss8-completion-gate-item-9-br-06-every-p SS8 completion gate item 9 / BR-06: every proof runs continuously on main-branch builds, not once (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\06-aot-jit-and-wasm-publish-proof.md, package-level obligation

Entry condition: adoption slice ADOPT.05.runtime-proofs is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [contract] CON.91: ArcForges.Contracts.Foundation/LocalRpc.Scope published package
- [artifact] FND.01: Foundation/Application.Abstractions identity/error primitives
Completion prerequisites (may start earlier; cannot complete before these are complete):
- [integration] APP.01: published minimal Assistant.Abstractions host ports over the actual PLT.17 application composition
- [integration] PLT.11: real parent-owned private child registration over PLT.09 transport and PLT.10 endpoint identity

Permitted write scope: ArcScope:src/ArcForges.ArcScope/**; ArcScope:ArcScope.slnx
Shared resources (follow the owner protocol): RES-desktopplatform-native-build (append): The vcpkg baseline and overlay ports change only through a dependency-admission change with licence and provenance receipts; each native family adds its own CMake targets and workflow entries; triplet or port changes are rebased and rebuilt by their author; CPU-heavy native builds use the workstation build slot.; RES-product-solutions (append): Solution/project lists, central package versions and CI job lists are appended by the task that adds a project, dependency or job; dependency additions follow the dependency-admission policy with a reviewed receipt; lock files are regenerated after rebase and never hand-merged; the integration owner resolves ordering conflicts at merge.; RES-workstation-build-slot (exclusive): Exclusive per workstation for the duration of each CPU-heavy local build or test, through the workstation lock rather than a Plan lease: run the command as `python tools/delivery.py build-slot run --worker <name> --task <task> -- <command>` with the Plan repository tool, which holds the lock directory `.arcforges/build-slot` in the user profile with an owner record and heartbeat and recovers a lock whose holder stopped. Coding and review continue while a build waits; CI capacity is not limited by this rule.
Unblocks: NAT.29, PLT.26, PLT.34, UPD.08

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Windows/Linux local Native AOT publish with zero trim/AOT/single-file diagnostics; real per-RID launch and ABI smoke vectors; no macOS CI
Completion evidence for the ledger: Per-RID AOT publish log with zero-diagnostic assertion; smoke-vector pass log; continuous main-branch CI run reference; final completion additionally requires exact APP.01/PLT.11 candidate identities and actual embedded host/private child-channel acceptance, with fixture and untested coverage explicitly distinguished
Notes: Stage delivery as the real minimal ArcScope Native AOT host consuming existing immutable Foundation/Application.Abstractions primitives, generated contracts and admitted native packages, with zero-diagnostic compilation and applicable native ABI evidence. Preserve the full WP-06.00 embedded assistant composition and private child-channel obligations as this task own completion acceptance after APP.01 (including PLT.17) and PLT.11 (including PLT.09/10) are complete. Consume those exact published candidates and record actual host composition/channel evidence before completion; neither future full assistant/Harness implementation nor an acceptance-only package closure is an early producer. Fixtures remain named boundary evidence only. Keep the ledger delivered while required real producers or completion acceptance are pending; no downstream task claim or implementation is authorized by this repair. The existing optional local runtime/environment policy remains unchanged: missing optional infrastructure is not a provisioning task, and unobserved evidence is never reported as passed.
```

```text
Execute ArcForges delivery task PRF.04 — Local RPC under AOT: bidirectional named-pipe/UDS probe processes.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\runtime-proofs.md (anchor task-prf-04).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/prf-04 (python tools/delivery.py claim PRF.04 --worker <name>); task branch task/prf-04 in DesktopPlatform; ledger record ledger/tasks/prf-04.md.
Kind/size: proof/L. Baseline: not-started.
Outcome: Two published AOT desktop probe processes complete LocalBootstrap over Kestrel HTTP/2 named-pipe (Windows) / UDS (Linux/macOS), authenticate same-user peers, register both endpoint directions, invoke generated services, cancel, disconnect and reattach; malformed-input/unauthorized-peer/bounded-resource negative tests pass.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-06.01 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\06-aot-jit-and-wasm-publish-proof.md, anchor rule-wp-06.01
- WP-06:ss8-completion-gate-item-9-br-06-every-p SS8 completion gate item 9 / BR-06: every proof runs continuously on main-branch builds, not once (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\06-aot-jit-and-wasm-publish-proof.md, package-level obligation

Entry condition: adoption slice ADOPT.02.runtime-proofs is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [contract] CON.05: local RPC generated server/client codegen (LocalBootstrap, ConnectCallback surface)
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:tests/LocalRpcAotTests/**; DesktopPlatform:eng/verification/**; DesktopPlatform:Directory.Packages.props; DesktopPlatform:DesktopPlatform.slnx; DesktopPlatform:.github/workflows/package-validation.yml (existing compile/AOT path only); DesktopPlatform:eng/policy/dependency-policy.json; DesktopPlatform:eng/policy/dependency-reviews/prf-04-r1.json; DesktopPlatform:eng/provenance/files.json
Shared resources (follow the owner protocol): RES-workstation-build-slot (exclusive): Exclusive per workstation for the duration of each CPU-heavy local build or test, through the workstation lock rather than a Plan lease: run the command as `python tools/delivery.py build-slot run --worker <name> --task <task> -- <command>` with the Plan repository tool, which holds the lock directory `.arcforges/build-slot` in the user profile with an owner record and heartbeat and recovers a lock whose holder stopped. Coding and review continue while a build waits; CI capacity is not limited by this rule.; RES-desktopplatform-build-config (append): Solution/project lists, central package versions and CI job lists are appended by the task that adds a project, dependency or job; dependency additions follow the dependency-admission policy with a reviewed receipt; lock files are regenerated after rebase and never hand-merged; the integration owner resolves ordering conflicts at merge.; RES-desktopplatform-policy-data (append): Generated policy data is regenerated from its pinned source and never hand-edited; the reason-code registry is append-only with stable codes; each task adds its own test classes and evidence rows.
Unblocks: APP.03, NAT.01, NAT.29, PLT.09

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Actual Windows/Linux/macOS(local opt-in) process-to-process runs; no in-memory or TCP substitute (explicit design prohibition); malformed input, unauthorized peer, bounded resource tests
Completion evidence for the ledger: Cross-process AOT RPC integration results satisfying VG-04
Notes: Directly closes VG-04. Independent of PRF.02 (uses its own dedicated probe processes, not the product hosts). Keep dependency admission limited to the existing reviewed Grpc.AspNetCore.Server 2.83.0 and Grpc.Net.Client 2.84.0 candidates plus the CON.05 candidate; use the BCL NamedPipe stream API with no new NamedPipes package and no hosted execution. Directory.Packages.props, solution/workflow and dependency-policy/review/provenance edits are append/rebase-only under RES-desktopplatform-build-config and RES-desktopplatform-policy-data; merge after current GOV.14 main, never overwrite or rederive GOV.14 bindings.
```

```text
Execute ArcForges delivery task PRF.05 — Generated gRPC-Web under AOT against deployed Worker/Container ingress.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\runtime-proofs.md (anchor task-prf-05).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/prf-05 (python tools/delivery.py claim PRF.05 --worker <name>); task branch task/prf-05 in DesktopPlatform; ledger record ledger/tasks/prf-05.md.
Kind/size: proof/M. Baseline: not-started.
Outcome: A published AOT desktop probe calls the real generated binary gRPC-Web client against actual deployed Worker/Container ingress, proving headers, trailers, cancellation, scoped errors and exact primitives; F-026 closes on this artifact.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-06.02 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\06-aot-jit-and-wasm-publish-proof.md, anchor rule-wp-06.02
- WP-06:ss8-completion-gate-item-9-br-06-every-p SS8 completion gate item 9 / BR-06: every proof runs continuously on main-branch builds, not once (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\06-aot-jit-and-wasm-publish-proof.md, package-level obligation

Entry condition: adoption slice ADOPT.02.runtime-proofs is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [contract] CON.92: ArcForges.Sdk.Client / generated gRPC-Web client, AOT-clean per accepted WP03.02 evidence
- [artifact] PRF.07: a deployed Worker/Container ingress endpoint (from WP-06.04)
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:tests/ReleaseArtifactTests/**; DesktopPlatform:eng/verification/**; DesktopPlatform:DesktopPlatform.slnx (append only tests/ReleaseArtifactTests/GrpcWeb/GrpcWebAotProbe.csproj); DesktopPlatform:Directory.Packages.props (append only Grpc.Net.Client.Web 2.84.0; preserve every existing coordinate/version); DesktopPlatform:tests/ReleaseArtifactTests/GrpcWeb/GrpcWebAotProbe.csproj and packages.lock.json; DesktopPlatform:.github/workflows/package-validation.yml (append only one exact locked Native AOT publish-only job for this project on pull requests and main builds; no runtime execution or live endpoint); DesktopPlatform:eng/policy/dependency-policy.json (only task-owned project/lock/pin input hashes and active review binding); DesktopPlatform:eng/policy/dependency-reviews/prf-05-r1.json (new immutable successor only when the existing gate requires one); DesktopPlatform:eng/policy/licence-boundary.json (append only this project as kind=msbuild); DesktopPlatform:eng/policy/runtime-ownership.json (append only this project as test-or-build-tool); DesktopPlatform:eng/policy/reconciliation/active-projects.json (append only this project row bound to its exact post-rebase blob); DesktopPlatform:eng/policy/architecture-projects.json (append only this project as Test, owner DesktopPlatform, empty module, production=false, aot=false); DesktopPlatform:eng/provenance/files.json (append only firstParty rows for task-owned files)
Shared resources (follow the owner protocol): RES-desktopplatform-build-config (append): Solution/project lists, central package versions and CI job lists are appended by the task that adds a project, dependency or job; dependency additions follow the dependency-admission policy with a reviewed receipt; lock files are regenerated after rebase and never hand-merged; the integration owner resolves ordering conflicts at merge.; RES-desktopplatform-policy-data (append): Generated policy data is regenerated from its pinned source and never hand-edited; the reason-code registry is append-only with stable codes; each task adds its own test classes and evidence rows.; RES-workstation-build-slot (exclusive): Exclusive per workstation for the duration of each CPU-heavy local build or test, through the workstation lock rather than a Plan lease: run the command as `python tools/delivery.py build-slot run --worker <name> --task <task> -- <command>` with the Plan repository tool, which holds the lock directory `.arcforges/build-slot` in the user profile with an owner record and heartbeat and recovers a lock whose holder stopped. Coding and review continue while a build waits; CI capacity is not limited by this rule.; RES-cloud-deployment (read): Bindings are added by the owning module task in its own section, and the Cloud integration owner resolves ordering conflicts at merge. Any task that runs against the deployed test environment holds the lease `leases/res-cloud-deployment` for that live run only, whatever mode it declares for its binding edits; production deployment belongs to release tasks.
Unblocks: AST.11, NAT.29

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Real AOT client round trip against the deployed Worker/Container; scope/permission, wrong or stale target, loss/retry, and expiry cases are local opt-in only under P2-017. CI performs a locked Native AOT publish-only check on pull requests and every main build; it never connects to the live deployment, reads deployment secrets, or executes the probe.
Completion evidence for the ledger: AOT publish result and exact pull-request/main workflow run; local deployed-provider round-trip and dependency-graph/negative build-test results for the typed client; F-026 closure evidence
Notes: Start-depends on PRF.07 (same area) for the deployed ingress target, with the existing CON.92 prerequisite unchanged. The public Worker is binary gRPC-Web, so PRF.05/06 share exactly one direct Grpc.Net.Client.Web 2.84.0 pin alongside the already-pinned Grpc.Net.Client 2.84.0; whichever task first reaches the serialized DesktopPlatform build-config merge appends that sole entry, and the other only reuses it. The exact locked closure and Apache-2.0 package licence are recorded in immutable task receipts; no other dependency coordinate/version changes. This task's project is `tests/ReleaseArtifactTests/GrpcWeb/GrpcWebAotProbe.csproj`; its solution/build-config/policy/provenance bindings are append-only. The probe is a non-packable test tool, not a release package. The workflow job compiles/publishes only and is not live-service evidence. Hold `leases/res-cloud-deployment` only during the local live round trip; the secret scanner/configuration is unchanged and no secret or credential-looking value may be committed or emitted.
```

```text
Execute ArcForges delivery task PRF.06 — Realtime (EventService.Watch/Poll) under AOT.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\runtime-proofs.md (anchor task-prf-06).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/prf-06 (python tools/delivery.py claim PRF.06 --worker <name>); task branch task/prf-06 in DesktopPlatform; ledger record ledger/tasks/prf-06.md.
Kind/size: proof/M. Baseline: not-started.
Outcome: A published AOT desktop probe proves EventService.Watch and output server streams plus Poll/readOutput recovery from annex 10 against actual Worker/Container/DO, including drop/expire/revoke and recovery through authoritative reads; no SignalR dependency, no claimed hint durability beyond what is proven.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-06.03 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\06-aot-jit-and-wasm-publish-proof.md, anchor rule-wp-06.03
- WP-06:ss8-completion-gate-item-9-br-06-every-p SS8 completion gate item 9 / BR-06: every proof runs continuously on main-branch builds, not once (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\06-aot-jit-and-wasm-publish-proof.md, package-level obligation

Entry condition: adoption slice ADOPT.02.runtime-proofs is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] PRF.07: deployed Worker/Container/DO providing EventService.Watch
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:tests/ReleaseArtifactTests/**; DesktopPlatform:eng/verification/**; DesktopPlatform:DesktopPlatform.slnx (append only tests/ReleaseArtifactTests/Realtime/RealtimeAotProbe.csproj); DesktopPlatform:Directory.Packages.props (append only the single exact Grpc.Net.Client.Web 2.84.0 pin if not yet present; otherwise reuse it, with no other coordinate/version changes); DesktopPlatform:tests/ReleaseArtifactTests/Realtime/RealtimeAotProbe.csproj and packages.lock.json; DesktopPlatform:.github/workflows/package-validation.yml (append only one exact locked Native AOT publish-only job for this project on pull requests and main builds; no runtime execution or live endpoint); DesktopPlatform:eng/policy/dependency-policy.json (only task-owned project/lock/pin input hashes and active review binding); DesktopPlatform:eng/policy/dependency-reviews/prf-06-r1.json (new immutable successor only when the existing gate requires one); DesktopPlatform:eng/policy/licence-boundary.json (append only this project as kind=msbuild); DesktopPlatform:eng/policy/runtime-ownership.json (append only this project as test-or-build-tool); DesktopPlatform:eng/policy/reconciliation/active-projects.json (append only this project row bound to its exact post-rebase blob); DesktopPlatform:eng/policy/architecture-projects.json (append only this project as Test, owner DesktopPlatform, empty module, production=false, aot=false); DesktopPlatform:eng/provenance/files.json (append only firstParty rows for task-owned files)
Shared resources (follow the owner protocol): RES-desktopplatform-build-config (append): Solution/project lists, central package versions and CI job lists are appended by the task that adds a project, dependency or job; dependency additions follow the dependency-admission policy with a reviewed receipt; lock files are regenerated after rebase and never hand-merged; the integration owner resolves ordering conflicts at merge.; RES-desktopplatform-policy-data (append): Generated policy data is regenerated from its pinned source and never hand-edited; the reason-code registry is append-only with stable codes; each task adds its own test classes and evidence rows.; RES-workstation-build-slot (exclusive): Exclusive per workstation for the duration of each CPU-heavy local build or test, through the workstation lock rather than a Plan lease: run the command as `python tools/delivery.py build-slot run --worker <name> --task <task> -- <command>` with the Plan repository tool, which holds the lock directory `.arcforges/build-slot` in the user profile with an owner record and heartbeat and recovers a lock whose holder stopped. Coding and review continue while a build waits; CI capacity is not limited by this rule.; RES-cloud-deployment (read): Bindings are added by the owning module task in its own section, and the Cloud integration owner resolves ordering conflicts at merge. Any task that runs against the deployed test environment holds the lease `leases/res-cloud-deployment` for that live run only, whatever mode it declares for its binding edits; production deployment belongs to release tasks.
Unblocks: NAT.29

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Real AOT EventService.Watch/output-stream and Poll/readOutput recovery against the deployed Worker/Container/DO; scope/permission, stale target, loss/retry, expiry and revoke cases are local opt-in only under P2-017. CI performs a locked Native AOT publish-only check on pull requests and every main build; it never connects to the live deployment, reads deployment secrets, or executes the probe.
Completion evidence for the ledger: Exact pull-request/main AOT publish result plus local deployed-provider realtime reconnection, Poll/readOutput recovery and authorization results
Notes: Runs after PRF.07 stands up DO/Worker; the existing PRF.07 start prerequisite is unchanged. Its runtime behavior is independent of PRF.04/05, but it shares their append-only transport/build configuration where applicable. Use only the single exact Grpc.Net.Client.Web 2.84.0 pin described by PRF.05; if this task reaches the serialized build-config merge first, append that sole entry, otherwise reuse it. The exact locked closure and Apache-2.0 package licence must be recorded in this task's immutable receipt; do not change any other dependency coordinate/version. This task's project is `tests/ReleaseArtifactTests/Realtime/RealtimeAotProbe.csproj`. Keep AOT publish evidence separate from the required local live-service proof. The project and policy/provenance rows are append-only under the declared build-config/policy-data resources; this probe is non-packable and does not alter package inventory. Hold `leases/res-cloud-deployment` only for the local live run. Do not add Gitleaks allowlists or change secret-scan behavior; no secret or credential-looking value is committed or emitted.
```

```text
Execute ArcForges delivery task PRF.07 — Cloudflare Native AOT host + D1 + DO/Queue/R2 foundation proof.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\runtime-proofs.md (anchor task-prf-07).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/prf-07 (python tools/delivery.py claim PRF.07 --worker <name>); task branch task/prf-07 in Cloud; ledger record ledger/tasks/prf-07.md.
Kind/size: proof/XL. Baseline: not-started.
Outcome: ArcForges.Cloud.Host publishes/deploys as a Linux x64 Native AOT container with the real private Worker D1 binding, DO/Queue/R2 foundation, rollback on guard failure, exact 64-bit/decimal handling, session/CSRF/revoke and bounded checkpoint/restart; zero trim/AOT diagnostics; VG-06 is supported (not yet closed platform-wide, since VG-06 is also maintained by WP-21.00/WP-50.04).

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-06.04 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\06-aot-jit-and-wasm-publish-proof.md, anchor rule-wp-06.04
- WP-06:ss8-completion-gate-item-9-br-06-every-p SS8 completion gate item 9 / BR-06: every proof runs continuously on main-branch builds, not once (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\06-aot-jit-and-wasm-publish-proof.md, package-level obligation

Entry condition: adoption slice ADOPT.07.runtime-proofs is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [contract] CON.92: Published Contracts serialization posture, exact-value vectors and existing CloudInternal package boundary
- [contract] CON.07: Native/browser authentication exception and identity/session schemas
- [contract] CON.15: Generated private D1 ExecutePlan request/reply schema
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Cloud:src/ArcForges.Cloud/**; Cloud:eng/verification/**; Cloud:worker/**; Cloud:wrangler.json; Cloud:Dockerfile; Cloud:Directory.Packages.props; Cloud:package.json; Cloud:package-lock.json; Cloud:tests/ArcForges.Cloud.Tests/**; Cloud:tests/worker/**; Cloud:eng/policy/dependency-reviews/**; Cloud:eng/provenance/**; Cloud:tooling/project.ts; Cloud:tooling/cloudflare.ts; Cloud:.github/workflows/ci.yml; Cloud:docs/prf-07-*.md
Shared resources (follow the owner protocol): RES-workstation-build-slot (exclusive): Exclusive per workstation for the duration of each CPU-heavy local build or test, through the workstation lock rather than a Plan lease: run the command as `python tools/delivery.py build-slot run --worker <name> --task <task> -- <command>` with the Plan repository tool, which holds the lock directory `.arcforges/build-slot` in the user profile with an owner record and heartbeat and recovers a lock whose holder stopped. Coding and review continue while a build waits; CI capacity is not limited by this rule.; RES-cloud-deployment (append): Bindings are added by the owning module task in its own section, and the Cloud integration owner resolves ordering conflicts at merge. Any task that runs against the deployed test environment holds the lease `leases/res-cloud-deployment` for that live run only, whatever mode it declares for its binding edits; production deployment belongs to release tasks.; RES-cloud-host-composition (append): Each module registers through its own module entry point and route fragment; the host composition only lists modules; route and binding conflicts are resolved by the integration owner at merge.; RES-cloud-leased-singletons (append): Each publication watermark, Durable Object alarm namespace and R2 prefix has exactly one owning module task; others use its published port; names are reserved in the binding plan before first use.; RES-cloud-storage-plans (regenerate): Each module owns its own plan directory; the plan-manifest hash is regenerated by the author after rebase and checked in CI.
Permitted substitutes (never real integration evidence): SUB-signed-format-fixture-keys: signature/hash verification mechanics, expired/revoked/unknown-key refusal, malformed/rollback/mixed-shard handling Real producer ['UPD.07']; removed by REL.11
Unblocks: CLOUD.25, NAT.29, PRF.05, PRF.06, PRF.08, PRF.10

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Native AOT compilation required; real-adapter runtime verification is scoped local opt-in per V-03/P2-017; no EF/dynamic ORM/ASP.NET Session/CookieAuthenticationHandler; chiseled Ubuntu image, non-root, read-only root
Completion evidence for the ledger: Cloud image build, pipeline order and integration results; VG-06 supporting evidence
Notes: This is the foundation every other Cloud-touching PRF task (05, 06, 08, 10) depends on.
```

```text
Execute ArcForges delivery task PRF.08 — React production build and generated TS SDK proof.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\runtime-proofs.md (anchor task-prf-08).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Web (integration owner: Web integration owner, the holder of roles/integration-web).
Claim and handoff record: claims/prf-08 (python tools/delivery.py claim PRF.08 --worker <name>); task branch task/prf-08 in Web; ledger record ledger/tasks/prf-08.md.
Kind/size: proof/L. Baseline: not-started.
Outcome: Minimal Account/Chat production React profiles build from Web root locks using the exact released generated gRPC-Web SDK, call the real AOT Cloud probe through same-origin routing/cookie/CSRF, exercise exact values/typed failures/cancellation and CF authenticated presentation; asset/interaction budgets measured; esproj and portable npm entry points proven. Contributes the foundation slice of PG-23 only.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-06.05 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\06-aot-jit-and-wasm-publish-proof.md, anchor rule-wp-06.05
- WP-06:ss8-completion-gate-item-9-br-06-every-p SS8 completion gate item 9 / BR-06: every proof runs continuously on main-branch builds, not once (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\06-aot-jit-and-wasm-publish-proof.md, package-level obligation

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

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\runtime-proofs.md (anchor task-prf-09).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/prf-09 (python tools/delivery.py claim PRF.09 --worker <name>); task branch task/prf-09 in DesktopPlatform; ledger record ledger/tasks/prf-09.md.
Kind/size: proof/S. Baseline: not-started.
Outcome: The process for admitting a third-party UI control into an AOT deliverable is documented and exercised once against a real candidate control published AOT with zero diagnostics; schedules VG-03 for WP10.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-06.06 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\06-aot-jit-and-wasm-publish-proof.md, anchor rule-wp-06.06
- WP-06:ss8-completion-gate-item-9-br-06-every-p SS8 completion gate item 9 / BR-06: every proof runs continuously on main-branch builds, not once (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\06-aot-jit-and-wasm-publish-proof.md, package-level obligation

Entry condition: adoption slice ADOPT.02.runtime-proofs is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [design] PLT.34: a candidate third-party control the desktop shell actually intends to use
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:eng/verification/probe-evidence/**; DesktopPlatform:.github/workflows/package-validation.yml (one separate Windows aot-probe job only); DesktopPlatform:eng/policy/dependency-policy.json (only the three probe input hashes, exact four build-only locked coordinates, successor receipt pointer, and active review summary exactly equal to the new immutable successor review listed in notes); DesktopPlatform:eng/policy/dependency-reviews/prf-09-r1.json (new immutable full successor, chained from the then-current receipt at serialized integration); DesktopPlatform:eng/policy/licence-boundary.json (append only the probe project as kind=msbuild); DesktopPlatform:eng/policy/runtime-ownership.json (append only the probe csproj to the DesktopPlatform owner projects as role=test-or-build-tool; preserve every other owner, project and field); DesktopPlatform:eng/policy/reconciliation/active-projects.json (append only the probe csproj row bound to its exact post-rebase git blob SHA; preserve the existing pinned roster); DesktopPlatform:eng/policy/architecture-projects.json (append only the exact probe path as role=BuildTool, owner=DesktopPlatform, module empty, production=false, aot=false); DesktopPlatform:tests/ArchitectureTests/EvaluatedPolicyTests.cs (exact probe-only default-solution selection exclusion and fail-closed drift tests; preserve all other BuildTool selection); DesktopPlatform:eng/provenance/files.json (append only the seven exact PRF.09 firstParty rows listed in notes; preserve every prior row/classification); DesktopPlatform:docs/third-party-control-admission.md (scope the no-Avalonia-use claim to production/shipped shell and disclose the isolated verification-only probe)
Shared resources (follow the owner protocol): RES-desktopplatform-build-config (append): Solution/project lists, central package versions and CI job lists are appended by the task that adds a project, dependency or job; dependency additions follow the dependency-admission policy with a reviewed receipt; lock files are regenerated after rebase and never hand-merged; the integration owner resolves ordering conflicts at merge.; RES-desktopplatform-policy-data (append): Generated policy data is regenerated from its pinned source and never hand-edited; the reason-code registry is append-only with stable codes; each task adds its own test classes and evidence rows.
Unblocks: NAT.29

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): First-candidate Windows x64 Native AOT publish with zero warnings/errors; locked restore and the same win-x64 publish gate run in package-validation PR and every main-build call under WP-06 BR-06. The existing EvaluatedPolicyTests gate must prove the probe is the sole exact default-solution exclusion and reject missing/duplicate rows, path/owner/role/module/production/aot drift, accidental solution inclusion, and owned/classified inventory drift, while preserving selection of every other BuildTool row. No executable or GUI run.
Completion evidence for the ledger: First-candidate publish log and exact-head PR/main workflow runs for the locked aot-probe job; no runtime/GUI or package-adoption claim.
Notes: Low coupling; can run independent of PRF.02-08. Formally schedules VG-03 to WP10, not itself. The verification-only probe is not product adoption, a production dependency, or a release package. Its project must explicitly declare PackageLicenseExpression AGPL-3.0-only; inherited LicenceBoundary classification remains unchanged. The exact package-validation.yml support is a separate aot-probe job on windows-latest using the repository-pinned checkout and setup-dotnet actions, global-json-file global.json, cache enabled with **/packages.lock.json, locked restore of eng/verification/probe-evidence/Prf09.TableViewProbe.csproj, then dotnet publish eng/verification/probe-evidence/Prf09.TableViewProbe.csproj --no-restore -c Release -r win-x64 --verbosity minimal. The job must not execute the binary, run GUI/UI behavior, upload an artifact, or alter product packaging/dependencies/locks/other workflow jobs. The dependency-policy successor adds only input hashes for eng/verification/probe-evidence/Directory.Packages.props, Prf09.TableViewProbe.csproj, and packages.lock.json, and only these build-only locked NuGet coordinates: avalonia/12.1.3, avalonia.buildservices/11.3.2, avalonia.remote.protocol/12.1.3, microcom.runtime/0.11.6. Create eng/policy/dependency-reviews/prf-09-r1.json as a full immutable successor chained from the then-current receipt after rebase; preserve all earlier receipts and admission history. Set dependency-policy.json reviewReceipt to that successor and replace only its active review object with the byte-equivalent review object from that successor so the existing active-receipt gate remains truthful; no unrelated dependency-policy field may change. Append to eng/policy/licence-boundary.json only the probe csproj with kind msbuild. Append only the probe csproj to the DesktopPlatform projects in eng/policy/runtime-ownership.json with role test-or-build-tool, preserving every other owner, project, role and field; this is the necessary gate-support classification for the same verification-only project, not product adoption, a production dependency, runtime selection, runtime authority, a host, or a package. Append only the probe csproj row to eng/policy/reconciliation/active-projects.json, binding its exact post-rebase git blob SHA and preserving the existing pinned roster; no current/source/historical snapshots or project-updates, solution edits or reference-baseline changes. The only architecture-projects addition is the exact probe row at eng/verification/probe-evidence/Prf09.TableViewProbe.csproj as role=BuildTool, owner=DesktopPlatform, module empty, production=false, aot=false. The existing EvaluatedPolicyTests must permit only this exact probe-only exclusion from default-solution selection; path, owner, role, module, production, AOT, solution inclusion, or owned/classified inventory drift fails closed, and all other BuildTool rows remain selected. This narrowly reconciles the existing test invariant that runtime-owned .csproj entries equal classified architecture-project rows and all other classifications are selected by the default solution; it is not a solution, runtime-ownership, production or product-adoption change. The CI evidence is hosted run 36414100059/job108903421150. Append these seven exact firstParty rows to eng/provenance/files.json, preserving every existing classification: eng/verification/probe-evidence/Directory.Packages.props, eng/verification/probe-evidence/Prf09.TableViewProbe.csproj, eng/verification/probe-evidence/Program.cs, eng/verification/probe-evidence/packages.lock.json, eng/verification/probe-evidence/README.md, eng/verification/probe-evidence/prf-09-publish.log, and eng/policy/dependency-reviews/prf-09-r1.json. Correct docs/third-party-control-admission.md only to state that the production/shipped shell has no Avalonia adoption, reference, or runtime usage and to disclose this isolated verification-only probe. No package-inventory append applies because this build-only probe is not a DesktopPlatform release package; no contract-access, package release allowlist, provenance artifact receipt, Gitleaks config, or other support path is authorized. DesktopPlatform has no dedicated provenance/source-inventory shared resource; exact policy/test/provenance additions use the existing RES-desktopplatform-policy-data append, while RES-desktopplatform-build-config covers only the existing workflow append.
```

```text
Execute ArcForges delivery task PRF.10 — Android Kotlin/Jetpack Compose gRPC-Web and CF proof.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\runtime-proofs.md (anchor task-prf-10).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Mobile (integration owner: Mobile integration owner, the holder of roles/integration-mobile).
Claim and handoff record: claims/prf-10 (python tools/delivery.py claim PRF.10 --worker <name>); task branch task/prf-10 in Mobile; ledger record ledger/tasks/prf-10.md.
Kind/size: proof/L. Baseline: not-started.
Outcome: A Kotlin Android release build consumes the actual Maven Connect Kotlin gRPC-Web client, exercises unary/server-stream/trailers/cancel/Keystore against real Worker/Container/D1/DO/R2 foundation; the compatible actual toolchain is pinned after proof. Closes VG-07 and the first-artifact leg of F-023 (already CLOSED for the inspected android-0.1.0-ci.14.1 replacement per the gates register, but reopens on dependency/resource change).

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-06.07 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\06-aot-jit-and-wasm-publish-proof.md, anchor rule-wp-06.07
- WP-06:ss8-completion-gate-item-9-br-06-every-p SS8 completion gate item 9 / BR-06: every proof runs continuously on main-branch builds, not once (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\06-aot-jit-and-wasm-publish-proof.md, package-level obligation

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
