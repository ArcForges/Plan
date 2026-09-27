# ArcForges delivery task prompts — Foundation values

Generated from Design `docs/planning/delivery/delivery-graph.json` by `tools/delivery.py`; do not edit by hand.
Each block is self-contained. Claim a task only when `python tools/delivery.py ready` lists it, with
`python tools/delivery.py claim <TASK-ID> --worker <name>`, then follow `arcforges-implementation.md`.
Tasks are ordered by lane for reading; the order is not a schedule.

## Foundation values

```text
Execute ArcForges delivery task FND.01 — Core identity and version-axis value-type skeleton.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\foundation.md (anchor task-fnd-01).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/fnd-01 (python tools/delivery.py claim FND.01 --worker <name>); task branch task/fnd-01 in DesktopPlatform; ledger record ledger/tasks/fnd-01.md.
Kind/size: producer/S. Baseline: not-started.
Outcome: ArcForges.Foundation exposes the UUID/revision/enum/error primitive types (registry-04 exact values) with generation and validation, adapting Contracts.Foundation wire types rather than redefining them.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-04.00 (all work except the parts mapped to FND.07): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\04-identity-error-and-versioning-primitives.md, anchor rule-wp-04.00

Entry condition: adoption slice ADOPT.02.foundation is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [contract] CON.91: ArcForges.Contracts.Foundation package: canonical UUID/Decimal/Rational/exact-value wire types and codecs
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:src/BuildingBlocks/ArcForges.Foundation/**; DesktopPlatform:eng/packaging/packages.json (owned producer package admission only); DesktopPlatform:eng/version-sources.json (owned producer source declarations only); DesktopPlatform:eng/policy/dependency-policy.json (owned producer/test dependency admission); DesktopPlatform:eng/policy/dependency-reviews/** (new immutable admission receipts); DesktopPlatform:eng/policy/licence-boundary.json (owned producer/test project registration); DesktopPlatform:eng/policy/reconciliation/project-updates.json (owned producer/test project registration); DesktopPlatform:eng/policy/reconciliation/source.json (owned producer source inventory); DesktopPlatform:eng/provenance/** (new owned-source receipts and generated inventory; preserve historical reused-file records); DesktopPlatform:eng/policy/runtime-ownership.json (owned producer/test project registration); DesktopPlatform:eng/policy/reconciliation/active-projects.json (owned active project registration; preserve historical frozen inventories); DesktopPlatform:eng/packaging/packages.py (exact external published dependency pins distinct from same-candidate owned packages); DesktopPlatform:eng/packaging/test_packages.py (external pin positive/negative fixtures); DesktopPlatform:README.md (current Foundation/Application package production claims only); DesktopPlatform:docs/compliance/third-party-license-register.md (exact admitted Contracts/Protobuf dependencies for owned producer packages)
Shared resources (follow the owner protocol): RES-desktopplatform-build-config (append): Solution/project lists, central package versions and CI job lists are appended by the task that adds a project, dependency or job; dependency additions follow the dependency-admission policy with a reviewed receipt; lock files are regenerated after rebase and never hand-merged; the integration owner resolves ordering conflicts at merge.; RES-desktopplatform-package-inventory (append): Each producer task adds its own package entry; every merge to main packs and publishes all packages at one version; consumers pin the candidate produced by the merge of the capability they need, never waiting for a package closure task; one merge queue.; RES-desktopplatform-policy-data (append): Generated policy data is regenerated from its pinned source and never hand-edited; the reason-code registry is append-only with stable codes; each task adds its own test classes and evidence rows.
Unblocks: APP.01, FND.07, PLT.17, PLT.36, PLT.47, PRF.02

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): P2-017 scope: Windows/Linux build + offline unit tests, compile-negative tests for identifier/axis confusion, no macOS/hosted-runtime/device CI.
Completion evidence for the ledger: Compile-negative suite result for identifier and axis confusion; round-trip vectors for absent/default/unknown values.
```

```text
Execute ArcForges delivery task FND.02 — Execution identity, idempotency and Application.Abstractions ports.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\foundation.md (anchor task-fnd-02).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/fnd-02 (python tools/delivery.py claim FND.02 --worker <name>); task branch task/fnd-02 in DesktopPlatform; ledger record ledger/tasks/fnd-02.md.
Kind/size: producer/S. Baseline: not-started.
Outcome: Immutable CommandId/InvocationId/AttemptId/RunId, canonical hash, Outcome<T> with typed failure/cancellation distinction, and Application.Abstractions cancellation/lifecycle ports exist as storage-free, memory-fixture-tested types.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-04.01 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\04-identity-error-and-versioning-primitives.md, anchor rule-wp-04.01

Entry condition: adoption slice ADOPT.02.foundation is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [contract] CON.91: Contracts.Foundation exact-value/identity wire types
Completion prerequisites (may start earlier; cannot complete before these are complete):
- [integration] PLT.01: durable single-effect/receipt proof against real persistence

Permitted write scope: DesktopPlatform:src/BuildingBlocks/ArcForges.Foundation/**; DesktopPlatform:src/BuildingBlocks/ArcForges.Application.Abstractions/**; DesktopPlatform:eng/packaging/packages.json (owned producer package admission only); DesktopPlatform:eng/version-sources.json (owned producer source declarations only); DesktopPlatform:eng/policy/dependency-policy.json (owned producer/test dependency admission); DesktopPlatform:eng/policy/dependency-reviews/** (new immutable admission receipts); DesktopPlatform:eng/policy/licence-boundary.json (owned producer/test project registration); DesktopPlatform:eng/policy/reconciliation/project-updates.json (owned producer/test project registration); DesktopPlatform:eng/policy/reconciliation/source.json (owned producer source inventory); DesktopPlatform:eng/provenance/** (new owned-source receipts and generated inventory; preserve historical reused-file records); DesktopPlatform:eng/policy/runtime-ownership.json (owned producer/test project registration); DesktopPlatform:eng/policy/reconciliation/active-projects.json (owned active project registration; preserve historical frozen inventories); DesktopPlatform:eng/packaging/packages.py (exact external published dependency pins distinct from same-candidate owned packages); DesktopPlatform:eng/packaging/test_packages.py (external pin positive/negative fixtures); DesktopPlatform:README.md (current Foundation/Application package production claims only); DesktopPlatform:docs/compliance/third-party-license-register.md (exact admitted Contracts/Protobuf dependencies for owned producer packages)
Shared resources (follow the owner protocol): RES-desktopplatform-build-config (append): Solution/project lists, central package versions and CI job lists are appended by the task that adds a project, dependency or job; dependency additions follow the dependency-admission policy with a reviewed receipt; lock files are regenerated after rebase and never hand-merged; the integration owner resolves ordering conflicts at merge.; RES-desktopplatform-package-inventory (append): Each producer task adds its own package entry; every merge to main packs and publishes all packages at one version; consumers pin the candidate produced by the merge of the capability they need, never waiting for a package closure task; one merge queue.; RES-desktopplatform-policy-data (append): Generated policy data is regenerated from its pinned source and never hand-edited; the reason-code registry is append-only with stable codes; each task adds its own test classes and evidence rows.
Unblocks: APP.04, EXE.01, FND.07, PLT.01, PLT.02, PLT.06, PLT.14

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline unit tests only: independent ID/hash/exact-value and state/retry algebra tests using memory-only fixtures; no storage adapter in scope.
Completion evidence for the ledger: Storage-free command/attempt/effect identity vectors under duplication.
```

```text
Execute ArcForges delivery task FND.03 — Revision and sequence types.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\foundation.md (anchor task-fnd-03).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/fnd-03 (python tools/delivery.py claim FND.03 --worker <name>); task branch task/fnd-03 in DesktopPlatform; ledger record ledger/tasks/fnd-03.md.
Kind/size: producer/S. Baseline: not-started.
Outcome: Revision (per-object monotonic, optimistic-concurrency comparable) and SequenceNumber (per-channel, gap-detecting) exist as non-interchangeable types with a compile-negative test proving they cannot be compared.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-04.02 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\04-identity-error-and-versioning-primitives.md, anchor rule-wp-04.02

Entry condition: adoption slice ADOPT.02.foundation is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [contract] CON.91: Contracts.Foundation revision/sequence wire primitives
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:src/BuildingBlocks/ArcForges.Foundation/**; DesktopPlatform:eng/packaging/packages.json (owned producer package admission only); DesktopPlatform:eng/version-sources.json (owned producer source declarations only); DesktopPlatform:eng/policy/dependency-policy.json (owned producer/test dependency admission); DesktopPlatform:eng/policy/dependency-reviews/** (new immutable admission receipts); DesktopPlatform:eng/policy/licence-boundary.json (owned producer/test project registration); DesktopPlatform:eng/policy/reconciliation/project-updates.json (owned producer/test project registration); DesktopPlatform:eng/policy/reconciliation/source.json (owned producer source inventory); DesktopPlatform:eng/provenance/** (new owned-source receipts and generated inventory; preserve historical reused-file records); DesktopPlatform:eng/policy/runtime-ownership.json (owned producer/test project registration); DesktopPlatform:eng/policy/reconciliation/active-projects.json (owned active project registration; preserve historical frozen inventories)
Shared resources (follow the owner protocol): RES-desktopplatform-build-config (append): Solution/project lists, central package versions and CI job lists are appended by the task that adds a project, dependency or job; dependency additions follow the dependency-admission policy with a reviewed receipt; lock files are regenerated after rebase and never hand-merged; the integration owner resolves ordering conflicts at merge.; RES-desktopplatform-package-inventory (append): Each producer task adds its own package entry; every merge to main packs and publishes all packages at one version; consumers pin the candidate produced by the merge of the capability they need, never waiting for a package closure task; one merge queue.; RES-desktopplatform-policy-data (append): Generated policy data is regenerated from its pinned source and never hand-edited; the reason-code registry is append-only with stable codes; each task adds its own test classes and evidence rows.
Unblocks: APP.04, EXE.01, FND.07, PLT.01, PLT.02

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline unit tests: optimistic concurrency conflict tests, sequence gap detection, compile-negative revision/sequence comparison test.
Completion evidence for the ledger: Optimistic concurrency and sequence gap test results.
```

```text
Execute ArcForges delivery task FND.04 — Clock abstraction and canonical time handling.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\foundation.md (anchor task-fnd-04).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/fnd-04 (python tools/delivery.py claim FND.04 --worker <name>); task branch task/fnd-04 in DesktopPlatform; ledger record ledger/tasks/fnd-04.md.
Kind/size: producer/S. Baseline: not-started.
Outcome: A clock abstraction provides wall-clock Instant and MonotonicTimestamp as distinct types; storage is canonical (instant plus originating zone where meaningful), presentation is localised, durations always use monotonic time.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-04.03 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\04-identity-error-and-versioning-primitives.md, anchor rule-wp-04.03

Entry condition: adoption slice ADOPT.02.foundation is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- none
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:src/BuildingBlocks/ArcForges.Foundation/**; DesktopPlatform:eng/packaging/packages.json (owned producer package admission only); DesktopPlatform:eng/version-sources.json (owned producer source declarations only); DesktopPlatform:eng/policy/dependency-policy.json (owned producer/test dependency admission); DesktopPlatform:eng/policy/dependency-reviews/** (new immutable admission receipts); DesktopPlatform:eng/policy/licence-boundary.json (owned producer/test project registration); DesktopPlatform:eng/policy/reconciliation/project-updates.json (owned producer/test project registration); DesktopPlatform:eng/policy/reconciliation/source.json (owned producer source inventory); DesktopPlatform:eng/provenance/** (new owned-source receipts and generated inventory; preserve historical reused-file records); DesktopPlatform:eng/policy/runtime-ownership.json (owned producer/test project registration); DesktopPlatform:eng/policy/reconciliation/active-projects.json (owned active project registration; preserve historical frozen inventories)
Shared resources (follow the owner protocol): RES-desktopplatform-build-config (append): Solution/project lists, central package versions and CI job lists are appended by the task that adds a project, dependency or job; dependency additions follow the dependency-admission policy with a reviewed receipt; lock files are regenerated after rebase and never hand-merged; the integration owner resolves ordering conflicts at merge.; RES-desktopplatform-package-inventory (append): Each producer task adds its own package entry; every merge to main packs and publishes all packages at one version; consumers pin the candidate produced by the merge of the capability they need, never waiting for a package closure task; one merge queue.; RES-desktopplatform-policy-data (append): Generated policy data is regenerated from its pinned source and never hand-edited; the reason-code registry is append-only with stable codes; each task adds its own test classes and evidence rows.
Unblocks: FND.07

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline unit tests: locale-change test asserting stored values unchanged, duration test asserting monotonic time used, DST boundary test for scheduled operations. Deterministic testing enabled by the clock abstraction itself.
Completion evidence for the ledger: Locale, time-zone and daylight-saving test results.
```

```text
Execute ArcForges delivery task FND.05 — Reason-code registry and Outcome result model.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\foundation.md (anchor task-fnd-05).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/fnd-05 (python tools/delivery.py claim FND.05 --worker <name>); task branch task/fnd-05 in DesktopPlatform; ledger record ledger/tasks/fnd-05.md.
Kind/size: producer/M. Baseline: not-started.
Outcome: A single generated reason-code registry (eng/policy/reason-codes.json, generated from source) exists with category, retryability, effect-certainty and message-key per code; Outcome<T> distinguishes success, typed failure and cancellation.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-04.04 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\04-identity-error-and-versioning-primitives.md, anchor rule-wp-04.04

Entry condition: adoption slice ADOPT.02.foundation is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [contract] CON.91: Contracts error/reason-code wire schema
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:src/BuildingBlocks/ArcForges.Foundation/**; DesktopPlatform:eng/policy/reason-codes.json; DesktopPlatform:eng/packaging/packages.json (owned producer package admission only); DesktopPlatform:eng/version-sources.json (owned producer source declarations only); DesktopPlatform:eng/policy/dependency-policy.json (owned producer/test dependency admission); DesktopPlatform:eng/policy/dependency-reviews/** (new immutable admission receipts); DesktopPlatform:eng/policy/licence-boundary.json (owned producer/test project registration); DesktopPlatform:eng/policy/reconciliation/project-updates.json (owned producer/test project registration); DesktopPlatform:eng/policy/reconciliation/source.json (owned producer source inventory); DesktopPlatform:eng/provenance/** (new owned-source receipts and generated inventory; preserve historical reused-file records); DesktopPlatform:eng/policy/runtime-ownership.json (owned producer/test project registration); DesktopPlatform:eng/policy/reconciliation/active-projects.json (owned active project registration; preserve historical frozen inventories)
Shared resources (follow the owner protocol): RES-desktopplatform-policy-data (append): Generated policy data is regenerated from its pinned source and never hand-edited; the reason-code registry is append-only with stable codes; each task adds its own test classes and evidence rows.; RES-desktopplatform-build-config (append): Solution/project lists, central package versions and CI job lists are appended by the task that adds a project, dependency or job; dependency additions follow the dependency-admission policy with a reviewed receipt; lock files are regenerated after rebase and never hand-merged; the integration owner resolves ordering conflicts at merge.; RES-desktopplatform-package-inventory (append): Each producer task adds its own package entry; every merge to main packs and publishes all packages at one version; consumers pin the candidate produced by the merge of the capability they need, never waiting for a package closure task; one merge queue.
Unblocks: FND.07, PLT.01, PLT.31, PLT.49, UPD.01, UPD.06

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline unit tests: registry completeness test, every failure path returns a registered code, cancellation never conflated with failure.
Completion evidence for the ledger: Reason-code registry with a completeness report.
```

```text
Execute ArcForges delivery task FND.06 — Version axis value types.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\foundation.md (anchor task-fnd-06).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/fnd-06 (python tools/delivery.py claim FND.06 --worker <name>); task branch task/fnd-06 in DesktopPlatform; ledger record ledger/tasks/fnd-06.md.
Kind/size: producer/S. Baseline: not-started.
Outcome: Each of the nine version axes (AppVersion, ContractSet, CapabilityVersion, NativeFormatVersion, StorageSchemaVersion, NativeAbiVersion, PolicySchemaVersion, ExtensionProtocolVersion, PackageVersion) is a distinct value type with parsing, comparison, range semantics and compile-time cross-assignment prevention.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-04.05 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\04-identity-error-and-versioning-primitives.md, anchor rule-wp-04.05

Entry condition: adoption slice ADOPT.02.foundation is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- none
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:src/BuildingBlocks/ArcForges.Foundation/**; DesktopPlatform:eng/packaging/packages.json (owned producer package admission only); DesktopPlatform:eng/version-sources.json (owned producer source declarations only); DesktopPlatform:eng/policy/dependency-policy.json (owned producer/test dependency admission); DesktopPlatform:eng/policy/dependency-reviews/** (new immutable admission receipts); DesktopPlatform:eng/policy/licence-boundary.json (owned producer/test project registration); DesktopPlatform:eng/policy/reconciliation/project-updates.json (owned producer/test project registration); DesktopPlatform:eng/policy/reconciliation/source.json (owned producer source inventory); DesktopPlatform:eng/provenance/** (new owned-source receipts and generated inventory; preserve historical reused-file records); DesktopPlatform:eng/policy/runtime-ownership.json (owned producer/test project registration); DesktopPlatform:eng/policy/reconciliation/active-projects.json (owned active project registration; preserve historical frozen inventories)
Shared resources (follow the owner protocol): RES-desktopplatform-build-config (append): Solution/project lists, central package versions and CI job lists are appended by the task that adds a project, dependency or job; dependency additions follow the dependency-admission policy with a reviewed receipt; lock files are regenerated after rebase and never hand-merged; the integration owner resolves ordering conflicts at merge.; RES-desktopplatform-package-inventory (append): Each producer task adds its own package entry; every merge to main packs and publishes all packages at one version; consumers pin the candidate produced by the merge of the capability they need, never waiting for a package closure task; one merge queue.; RES-desktopplatform-policy-data (append): Generated policy data is regenerated from its pinned source and never hand-edited; the reason-code registry is append-only with stable codes; each task adds its own test classes and evidence rows.
Unblocks: FND.07, PLT.04

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline unit tests: compile-negative tests per axis pair, range comparison tests including open/partial ranges.
Completion evidence for the ledger: Compile-negative test suite for axis confusion.
```

```text
Execute ArcForges delivery task FND.07 — Publish Foundation/Application.Abstractions and verify cross-language round trips.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\foundation.md (anchor task-fnd-07).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/fnd-07 (python tools/delivery.py claim FND.07 --worker <name>); task branch task/fnd-07 in DesktopPlatform; ledger record ledger/tasks/fnd-07.md.
Kind/size: acceptance/S. Baseline: not-started.
Outcome: ArcForges.Foundation and ArcForges.Application.Abstractions are packed, admitted to eng/packaging/packages.json, published from a main-branch candidate, and independently consumed to prove C#/TS round trips (values outside JS safe integers, absence/unknown values, duplicate commands, unknown effects) against Contracts' generated TS/Kotlin projections.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-04.90 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\04-identity-error-and-versioning-primitives.md, anchor rule-wp-04.90
- WP-04.00 (first real external consumption of Contracts.Foundation): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\04-identity-error-and-versioning-primitives.md, anchor rule-wp-04.00
- WP-04:typescript-kotlin-primitive-projection-o TypeScript/Kotlin primitive projection of registry-04 exact-value rules (UUID canonical ordering, TS bigint/Decimal, JSON exceptions) (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\04-identity-error-and-versioning-primitives.md, package-level obligation

Entry condition: adoption slice ADOPT.02.foundation is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] FND.01: identity/exact-value types
- [artifact] FND.02: execution identity/idempotency types
- [artifact] FND.03: revision/sequence types
- [artifact] FND.04: clock abstraction
- [artifact] FND.05: reason-code registry
- [artifact] FND.06: version axis types
- [artifact] CON.91: real, delivered outcome of CON.91 (WP03.01 — foundation contract types (accepted, historical))
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:eng/packaging/packages.json; DesktopPlatform:eng/version-sources.json; DesktopPlatform:eng/acceptance/foundation/** (exact published C#/TS producer-consumer offline fixtures, runner and receipt; no installed-consumer CI); DesktopPlatform:eng/policy/dependency-policy.json (owned dev-only acceptance dependencies); DesktopPlatform:eng/policy/dependency-reviews/** (new immutable acceptance dependency receipts); DesktopPlatform:eng/policy/licence-boundary.json (owned acceptance project registration); DesktopPlatform:eng/provenance/** (owned acceptance inventory and new receipts; preserve historical records); DesktopPlatform:eng/policy/runtime-ownership.json (owned acceptance project registration); DesktopPlatform:eng/policy/reconciliation/active-projects.json (owned acceptance project registration); DesktopPlatform:eng/policy/reconciliation/source.json (owned acceptance source inventory); DesktopPlatform:eng/dependency_policy.py (only exact existing Foundation/Application.Abstractions 1.0.0-ci.29.1 AGPL package/publisher admission for the owned acceptance runner, and its exact npm manifest/lock input bindings); DesktopPlatform:eng/test_dependency_policy.py (owned exact admission positive and wrong package/version/publisher/licence/source/hash negatives); DesktopPlatform:eng/runtime_ownership.py (only eng/acceptance/foundation/package.json as a local test/build tool; no production npm runtime); DesktopPlatform:eng/test_runtime_ownership.py (exact acceptance path/owner positive and adjacent path/owner negatives)
Shared resources (follow the owner protocol): RES-desktopplatform-build-config (append): Solution/project lists, central package versions and CI job lists are appended by the task that adds a project, dependency or job; dependency additions follow the dependency-admission policy with a reviewed receipt; lock files are regenerated after rebase and never hand-merged; the integration owner resolves ordering conflicts at merge.; RES-desktopplatform-package-inventory (append): Each producer task adds its own package entry; every merge to main packs and publishes all packages at one version; consumers pin the candidate produced by the merge of the capability they need, never waiting for a package closure task; one merge queue.; RES-desktopplatform-policy-data (append): Generated policy data is regenerated from its pinned source and never hand-edited; the reason-code registry is append-only with stable codes; each task adds its own test classes and evidence rows.

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): P2-017: pack once (whole-repo shared candidate version per the publish-nuget/pr-gate workflows), offline packages.py verify, no hosted runtime execution; cross-language vector tests run as local/offline unit tests against Contracts' committed fixtures, not live services.
Completion evidence for the ledger: Owned artifact and real-integration receipt: source commit, producer version, candidate hashes, real-versus-fixture status per the WP-04.90 template.
Notes: Merged duplicate integration or closure task formerly proposed as CON.93. The existing policy rejects this repository own AGPL Foundation/Application.Abstractions packages and any DesktopPlatform npm project; the current acceptance task may repair only those precise admission boundaries. Permit AGPL-3.0-only solely for arcforges.foundation/1.0.0-ci.29.1 and arcforges.application.abstractions/1.0.0-ci.29.1 with immutable locked hashes, exact NuGet source URLs, DesktopPlatform publisher identity and source commit ace60538849047184954baed09fb05ec7676d367 verified from existing publication/nuspec evidence. Preserve all other licence refusals, candidate/receipt history checks and independent review. Bind eng/acceptance/foundation/package.json and package-lock.json as exact dependency input hashes; retain their locked Contracts proto/fixtures 1.0.0-ci.113.1 and protobuf 2.15.0 closure, not a general npm admission expansion. The exact npm project is a local-only test/build tool, never a product runtime or CI installed-consumer execution. Negative tests must reject changed package/version/publisher/source/licence/hash and any other DesktopPlatform npm path. This is explicit source-policy repair under the existing FND.07 claim, not inferred supporting-file authority or permission to add other dependencies.
```
