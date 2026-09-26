# ArcForges delivery task prompts — Dynamic policy and configuration

Generated from Design `docs/planning/delivery/delivery-graph.json` by `tools/delivery.py`; do not edit by hand.
Each block is self-contained. Claim a task only when `python tools/delivery.py ready` lists it, with
`python tools/delivery.py claim <TASK-ID> --worker <name>`, then follow `arcforges-implementation.md`.
Tasks are ordered by lane for reading; the order is not a schedule.

## Dynamic policy and configuration

```text
Execute ArcForges delivery task POL.01 — The four boundaries.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\policy.md (anchor task-pol-01).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/pol-01 (python tools/delivery.py claim POL.01 --worker <name>); task branch task/pol-01 in Cloud; ledger record ledger/tasks/pol-01.md.
Kind/size: service/S. Baseline: not-started.
Outcome: Policy, entitlement, user settings, health and the data plane are kept structurally distinct with an architecture test asserting no policy type reaches an entitlement decision, each boundary backed by a failing negative fixture.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-44.00 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\44-dynamic-policy-and-configuration.md, anchor rule-wp-44.00

Entry condition: adoption slice ADOPT.07.policy is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- none
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Cloud:src/Cloud/ArcForges.Cloud.Modules.Policy/**/Boundaries/**
Unblocks: POL.02, POL.04

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline architecture test (assembly/namespace dependency scan) plus four negative fixtures.
Completion evidence for the ledger: Four boundary negative-fixture results plus the architecture-test pass log.
Notes: Cheap structural invariant that every other Policy task must respect; wrong here silently corrupts POL.02-09.
```

```text
Execute ArcForges delivery task POL.02 — Schema-constrained configuration.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\policy.md (anchor task-pol-02).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/pol-02 (python tools/delivery.py claim POL.02 --worker <name>); task branch task/pol-02 in Cloud; ledger record ledger/tasks/pol-02.md.
Kind/size: service/L. Baseline: not-started.
Outcome: policy.body.v1 and configuration.v1 bundles validate exactly against their schema (key/type/scope/limit/cross-reference), an invalid bundle is rejected wholesale, and activation is a dry-run proposal with dual approval and compare-and-swap.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-44.01 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\44-dynamic-policy-and-configuration.md, anchor rule-wp-44.01
- WP-44:operator-contract-closure-configuration Operator contract closure — configuration/policy owners (operator contract closure; configuration/policy owner: dry-run proposal/dual-approval/activation CAS as the typed proposal protocol): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\44-dynamic-policy-and-configuration.md, package-level obligation

Entry condition: adoption slice ADOPT.07.policy is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [contract] CON.12: policy.body.v1 and configuration.v1 published message schemas per architecture/contracts/08 §4/§6
- [artifact] POL.01: boundary markers
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Cloud:src/Cloud/ArcForges.Cloud.Modules.Configuration/**
Shared resources (follow the owner protocol): RES-contracts-schema-sources (append): Each closure task edits only its own domain proto or HTTP-schema files and adds its own sharded constraint and fixture files; shared inventories (package inventory, foundation inventory, constraint aggregate) are append-only per closure. A proto file with several contributing tasks (operator, policy/configuration) has one designated author task and the others request changes through it. The integration owner merges closure pull requests one at a time and the next author rebases and regenerates.
Unblocks: AIR.01, POL.03, POL.04, POL.05, POL.06, POL.07, POL.08, SRCH.90, WEB.14

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline tests: unknown key/field/version, invalid commercial route, secret-in-body, conflicting rule priority, stale parent, mixed-replica version, rollback; AOT-publish check.
Completion evidence for the ledger: Atomic-rejection test (no partial apply); AOT-clean publish result.
```

```text
Execute ArcForges delivery task POL.03 — Compiled hard limits.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\policy.md (anchor task-pol-03).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/pol-03 (python tools/delivery.py claim POL.03 --worker <name>); task branch task/pol-03 in Cloud; ledger record ledger/tasks/pol-03.md.
Kind/size: service/M. Baseline: not-started.
Outcome: Safety-critical limits are compiled and authoritative; remote policy may only tighten them, and any attempt to loosen one is rejected and recorded.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-44.02 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\44-dynamic-policy-and-configuration.md, anchor rule-wp-44.02

Entry condition: adoption slice ADOPT.07.policy is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] POL.02: the activation validation pipeline
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Cloud:src/Cloud/ArcForges.Cloud.Modules.Policy/**/HardLimits/**
Shared resources (follow the owner protocol): RES-contracts-schema-sources (append): Each closure task edits only its own domain proto or HTTP-schema files and adds its own sharded constraint and fixture files; shared inventories (package inventory, foundation inventory, constraint aggregate) are append-only per closure. A proto file with several contributing tasks (operator, policy/configuration) has one designated author task and the others request changes through it. The integration owner merges closure pull requests one at a time and the next author rebases and regenerates.
Unblocks: POL.10, SIM.07

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline tests: per-hard-limit loosening-rejection, tightening-acceptance, audit assertion on rejection.
Completion evidence for the ledger: Loosening-rejection test per compiled hard limit, with audit record.
Notes: Security-critical invariant (BR-03); cheap to verify in isolation before building rollout/kill-switch machinery that also touches these limits.
```

```text
Execute ArcForges delivery task POL.04 — Features, flags and deterministic rollout.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\policy.md (anchor task-pol-04).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/pol-04 (python tools/delivery.py claim POL.04 --worker <name>); task branch task/pol-04 in Cloud; ledger record ledger/tasks/pol-04.md.
Kind/size: service/L. Baseline: not-started.
Outcome: Deterministic target/percent hashing, exclusion groups and sticky experiment allocation select the same result for the same stable subject/version across languages, and rollout cannot grant commercial or security authority.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-44.03 (server-side flag/rollout definition, publication and byte/hash/bucket algorithm; on-device execution split to POL.09): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\44-dynamic-policy-and-configuration.md, anchor rule-wp-44.03

Entry condition: adoption slice ADOPT.07.policy is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] POL.01: boundary enforcement
- [artifact] POL.02: schema/activation pipeline
- [artifact] COM.05: explicit-setting/entitlement priority ordering
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Cloud:src/Cloud/ArcForges.Cloud.Modules.Policy/**/Rollout/**
Shared resources (follow the owner protocol): RES-contracts-schema-sources (append): Each closure task edits only its own domain proto or HTTP-schema files and adds its own sharded constraint and fixture files; shared inventories (package inventory, foundation inventory, constraint aggregate) are append-only per closure. A proto file with several contributing tasks (operator, policy/configuration) has one designated author task and the others request changes through it. The integration owner merges closure pull requests one at a time and the next author rebases and regenerates.
Unblocks: POL.09

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline tests: independent byte/hash/bucket vectors, boundary 0/9999, holdout, overlapping exclusion group, account/device change, cached signed bundle expiry.
Completion evidence for the ledger: Cross-language hash/bucket vector match; boundary 0/9999 test.
```

```text
Execute ArcForges delivery task POL.05 — Kill switches.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\policy.md (anchor task-pol-05).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/pol-05 (python tools/delivery.py claim POL.05 --worker <name>); task branch task/pol-05 in Cloud; ledger record ledger/tasks/pol-05.md.
Kind/size: service/M. Baseline: not-started.
Outcome: All four kill-switch modes propagate promptly with a defined blast radius, a mandatory reason, a user-visible explanation and a complete audit record, and are reversible.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-44.04 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\44-dynamic-policy-and-configuration.md, anchor rule-wp-44.04
- WP-44:operator-contract-closure-the-kill-typed operator contract closure; the 'kill' typed operator RPC (operator contract closure; the 'kill' typed operator RPC): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\44-dynamic-policy-and-configuration.md, package-level obligation
- WP-44:operator-contract-closure-configuration Operator contract closure — configuration/policy owners (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\44-dynamic-policy-and-configuration.md, package-level obligation

Entry condition: adoption slice ADOPT.07.policy is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] POL.02: activation CAS pipeline
- [contract] CON.14: the 'kill' operator RPC shape per registry04 §9.2
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Cloud:src/Cloud/ArcForges.Cloud.Modules.Policy/**/KillSwitch/**
Shared resources (follow the owner protocol): RES-contracts-schema-sources (append): Each closure task edits only its own domain proto or HTTP-schema files and adds its own sharded constraint and fixture files; shared inventories (package inventory, foundation inventory, constraint aggregate) are append-only per closure. A proto file with several contributing tasks (operator, policy/configuration) has one designated author task and the others request changes through it. The integration owner merges closure pull requests one at a time and the next author rebases and regenerates.
Unblocks: CLOUD.64, OPS.05, OPS.13, POL.10

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline tests: per-mode activation/propagation, user-visibility, audit-completeness, reversal.
Completion evidence for the ledger: Per-mode propagation test with user-visible reason and complete audit record.
```

```text
Execute ArcForges delivery task POL.06 — Scoped resolution and explainability (server side).

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\policy.md (anchor task-pol-06).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/pol-06 (python tools/delivery.py claim POL.06 --worker <name>); task branch task/pol-06 in Cloud; ledger record ledger/tasks/pol-06.md.
Kind/size: service/M. Baseline: not-started.
Outcome: Policy resolves across application, workspace, device and installation scopes in a fixed order, and the server can state which scope and bundle produced any effective value.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-44.05 (server-side resolution across application/workspace/device/installation scopes with fixed order, and the explainability endpoint/data; client-side consumption split to POL.09): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\44-dynamic-policy-and-configuration.md, anchor rule-wp-44.05

Entry condition: adoption slice ADOPT.07.policy is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] POL.02: published, validated bundles to resolve over
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Cloud:src/Cloud/ArcForges.Cloud.Modules.Policy/**/Resolution/**
Unblocks: POL.10

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline tests: resolution-order matrix, explainability per scope, workspace-policy override.
Completion evidence for the ledger: Resolution-order matrix result; explainability-per-scope result.
```

```text
Execute ArcForges delivery task POL.07 — Compatibility policy.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\policy.md (anchor task-pol-07).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/pol-07 (python tools/delivery.py claim POL.07 --worker <name>); task branch task/pol-07 in Cloud; ledger record ledger/tasks/pol-07.md.
Kind/size: service/M. Baseline: not-started.
Outcome: Compatibility rules express supported client windows and blocked version ranges; a bad version is blockable without affecting neighbours, and a minimum-version requirement is never enforced before its grace period elapses.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-44.06 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\44-dynamic-policy-and-configuration.md, anchor rule-wp-44.06

Entry condition: adoption slice ADOPT.07.policy is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] POL.02: schema/activation pipeline
Completion prerequisites (may start earlier; cannot complete before these are complete):
- [integration] UPD.08: the update feed actually stopping an offer for a blocked version

Permitted write scope: Cloud:src/Cloud/ArcForges.Cloud.Modules.Policy/**/Compatibility/**
Unblocks: POL.10

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline tests: range-blocking precision, grace-period enforcement; update-feed integration test stays with the WP-53 consumer per P2-017 (no cross-repo E2E in this task's CI).
Completion evidence for the ledger: Range-blocking precision test; grace-period enforcement test.
```

```text
Execute ArcForges delivery task POL.08 — Publication, staleness and last-known-good (server side).

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\policy.md (anchor task-pol-08).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/pol-08 (python tools/delivery.py claim POL.08 --worker <name>); task branch task/pol-08 in Cloud; ledger record ledger/tasks/pol-08.md.
Kind/size: service/M. Baseline: not-started.
Outcome: Bundles publish with versioning and audit, and the server-side staleness/application-timing contract is defined so a change is never applied in a way that produces inconsistent behaviour mid-operation.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-44.07 (bundle publication with versioning and audit; server-side staleness signalling; the application-timing contract clients must honour. Client caching/fallback/mid-operation behaviour split to POL.09): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\44-dynamic-policy-and-configuration.md, anchor rule-wp-44.07

Entry condition: adoption slice ADOPT.07.policy is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] POL.02: validated bundle to publish
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Cloud:src/Cloud/ArcForges.Cloud.Modules.Policy/**/Publication/**
Unblocks: AIR.00, POL.09, POL.11, SRCH.06, WEB.29

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline tests: publication audit, staleness-signal correctness.
Completion evidence for the ledger: Publication audit test.
```

```text
Execute ArcForges delivery task POL.09 — Client-side policy resolution library (native/AOT).

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\policy.md (anchor task-pol-09).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/pol-09 (python tools/delivery.py claim POL.09 --worker <name>); task branch task/pol-09 in DesktopPlatform; ledger record ledger/tasks/pol-09.md.
Kind/size: service/L. Baseline: not-started.
Outcome: A single ArcForges.Policy building block resolves, caches, and explains policy identically under Native AOT, falling back from staleness to last-known-good to compiled defaults with the staleness state always visible, and a change never takes effect mid-operation inconsistently.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-44.05 (client-side consumption of scoped resolution/explainability): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\44-dynamic-policy-and-configuration.md, anchor rule-wp-44.05
- WP-44.07 (client caching, staleness threshold, fallback to last-known-good then compiled defaults, staleness visible, mid-operation application timing): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\44-dynamic-policy-and-configuration.md, anchor rule-wp-44.07
- WP-44.03 (client execution of the deterministic rollout hash so the same subject/version selects the same result on-device): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\44-dynamic-policy-and-configuration.md, anchor rule-wp-44.03

Entry condition: adoption slice ADOPT.02.policy is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] POL.04: the deterministic rollout hashing algorithm specification
- [contract] CON.12: policy.body.v1/configuration.v1 generated client-side (C#) types
- [contract] CON.22: published policy.getBundle
Completion prerequisites (may start earlier; cannot complete before these are complete):
- [integration] POL.11: a genuinely published bundle fetched and cached by this library, with staleness fallback proven against the deployed Cloud policy service
- [integration] POL.08: real server-side publication and staleness signal complete

Permitted write scope: DesktopPlatform:src/BuildingBlocks/ArcForges.Policy/**
Shared resources (follow the owner protocol): RES-contracts-schema-sources (append): Each closure task edits only its own domain proto or HTTP-schema files and adds its own sharded constraint and fixture files; shared inventories (package inventory, foundation inventory, constraint aggregate) are append-only per closure. A proto file with several contributing tasks (operator, policy/configuration) has one designated author task and the others request changes through it. The integration owner merges closure pull requests one at a time and the next author rebases and regenerates.
Permitted substitutes (never real integration evidence): SUB-lkg-compiled-defaults-seed: the fallback chain mechanics in isolation before any bundle has ever been published in a live environment Real producer ['POL.08']; removed by POL.11
Unblocks: POL.10, POL.11, UPD.05, UPD.08

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline unit tests: staleness-fallback-chain, mid-operation-application, offline-extended, AOT publish/trim check (this module must publish cleanly under Native AOT per P2-017's AOT compile class).
Completion evidence for the ledger: Fallback-chain-to-compiled-defaults test; AOT-clean publish result.
Notes: Cross-repo: WP-44 is planned under the commerce, policy and operations lanes but this substep's implementation path lives in the DesktopPlatform repo per WP-44 §4's own file table. The React/Web browser binding is NOT built here — WP-44's downstream list omits 47/49 and includes 48, so the browser-side resolver is expected to be built by the Web and Android lanes (WP-48) consuming this task's published algorithm/contract, not duplicated here.
```

```text
Execute ArcForges delivery task POL.10 — Owned-artifact receipt.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\policy.md (anchor task-pol-10).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/pol-10 (python tools/delivery.py claim POL.10 --worker <name>); task branch task/pol-10 in Cloud; ledger record ledger/tasks/pol-10.md.
Kind/size: service/S. Baseline: not-started.
Outcome: The package-level owned-artifact/real-integration receipt is recorded confirming every CF run and effect uses the required policy version and stale/disallowed models or revoked permission fail deterministically without client-side policy becoming authority.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-44.90 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\44-dynamic-policy-and-configuration.md, anchor rule-wp-44.90

Entry condition: adoption slice ADOPT.07.policy is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] POL.09: client resolution evidence to attach
- [artifact] POL.03: package task delivered
- [artifact] POL.05: package task delivered
- [artifact] POL.06: package task delivered
- [artifact] POL.07: package task delivered
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Cloud:eng/provenance/records/**
Unblocks: REL.06, REL.08

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Aggregation of POL.01-09 evidence at the candidate closure.
Completion evidence for the ledger: The owned-artifact/real-integration receipt.
```

```text
Execute ArcForges delivery task POL.11 — First real publish-then-resolve round trip from Cloud Policy authority to the DesktopPlatform client library.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\policy.md (anchor task-pol-11).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/pol-11 (python tools/delivery.py claim POL.11 --worker <name>); task branch task/pol-11 in Cloud; ledger record ledger/tasks/pol-11.md.
Kind/size: integration/M. Baseline: not-started.
Outcome: a genuinely published bundle is fetched, cached, and correctly falls back to last-known-good on a later real staleness condition, not just against POL.09's local fixture

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-44.07 (real fallback chain against a deployed publication endpoint): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\44-dynamic-policy-and-configuration.md, anchor rule-wp-44.07

Entry condition: adoption slice ADOPT.07.policy is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] POL.08: real, delivered outcome of POL.08 (Publication, staleness and last-known-good (server side))
- [artifact] POL.09: real, delivered outcome of POL.09 (Client-side policy resolution library (native/AOT))
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: 
Unblocks: POL.09

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Local real-integration run of the affected scenario in an existing environment, recorded once; offline and static checks in CI; no hosted runtime, device, browser, live-service or inference CI (P2-017).
Completion evidence for the ledger: a genuinely published bundle is fetched, cached, and correctly falls back to last-known-good on a later real staleness condition, not just against POL.09's local fixture
```
