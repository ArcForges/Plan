# ArcForges delivery task prompts — Family governance and policy tests

Generated from Design `docs/planning/delivery/delivery-graph.json` by `tools/delivery.py`; do not edit by hand.
Each block is self-contained. Claim a task only when `python tools/delivery.py ready` lists it, with
`python tools/delivery.py claim <TASK-ID> --worker <name>`, then follow `arcforges-implementation.md`.
Tasks are ordered by lane for reading; the order is not a schedule.

## Family governance and policy tests

```text
Execute ArcForges delivery task GOV.01 — Specification, naming, licence-boundary and provenance freeze (WP00, accepted).

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\governance.md (anchor task-gov-01).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/gov-01 (python tools/delivery.py claim GOV.01 --worker <name>); task branch task/gov-01 in DesktopPlatform; ledger record ledger/tasks/gov-01.md.
Kind/size: governance/XL. Baseline: accepted.
Outcome: WP00's naming/licence/provenance freeze is accepted across the seven implementation repositories: product-names.json, exported glossary/invariant policy data, per-project SPDX licence boundaries, a working provenance process and five registered Reference Coverage Matrices are in place, scanned clean, and enforced in CI.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-00.00 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\00-specification-naming-and-rights-freeze.md, anchor rule-wp-00.00
- WP-00.01 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\00-specification-naming-and-rights-freeze.md, anchor rule-wp-00.01
- WP-00.02 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\00-specification-naming-and-rights-freeze.md, anchor rule-wp-00.02
- WP-00.03 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\00-specification-naming-and-rights-freeze.md, anchor rule-wp-00.03
- WP-00.04 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\00-specification-naming-and-rights-freeze.md, anchor rule-wp-00.04
- WP-00.05 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\00-specification-naming-and-rights-freeze.md, anchor rule-wp-00.05
- WP-00.90 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\00-specification-naming-and-rights-freeze.md, anchor rule-wp-00.90

Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- none
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Contracts:eng/policy/product-names.json; DesktopPlatform:eng/policy/glossary-terms.json; DesktopPlatform:eng/policy/invariants.json; DesktopPlatform:eng/policy/reference-baselines.json; *:NOTICE.md; *:LICENSE; *:Directory.Build.props
Shared resources (follow the owner protocol): RES-desktopplatform-policy-data (append): Generated policy data is regenerated from its pinned source and never hand-edited; the reason-code registry is append-only with stable codes; each task adds its own test classes and evidence rows.
Unblocks: CON.23, GOV.02, GOV.04, GOV.11, GOV.14

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Design-repo-pinned exporter (DesktopPlatform/eng/design_policy.py) verified against an immutable, clean pinned Design commit; offline forbidden-term scanner over the implementation repositories in Contracts CI; no macOS/device/live-service runtime, per P2-017.
Completion evidence for the ledger: docs/assurance/wp00-03-implementation-evidence.md, wp00-04-implementation-evidence.md, wp00-05-implementation-evidence.md, wp00-stage-acceptance.md, wp00-stage-acceptance.json (file names only, via ls; bodies not read per assignment).
Notes: Executed across the seven implementation repositories plus Contracts' product-names.json; represented as one accepted task for the whole closed package rather than one task per substep, per the assignment's 'small number of GOV tasks' instruction.
```

```text
Execute ArcForges delivery task GOV.02 — Repository reconciliation and target layout (WP01, accepted).

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\governance.md (anchor task-gov-02).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/gov-02 (python tools/delivery.py claim GOV.02 --worker <name>); task branch task/gov-02 in DesktopPlatform; ledger record ledger/tasks/gov-02.md.
Kind/size: governance/XL. Baseline: accepted.
Outcome: WP01 reconciliation is accepted: seven-repository disposition inventory executed against ede43db, the Contracts public/internal Apache-2.0 split assigned, the shared-foundation boundary reviewed, native surface dispositions executed (MDF excluded), all eighteen test families mapped, bounded reconciliation applied, and Cloud's 19 domain owners recorded.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-01.00 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\01-repository-reconciliation-and-target-layout.md, anchor rule-wp-01.00
- WP-01.01 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\01-repository-reconciliation-and-target-layout.md, anchor rule-wp-01.01
- WP-01.02 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\01-repository-reconciliation-and-target-layout.md, anchor rule-wp-01.02
- WP-01.03 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\01-repository-reconciliation-and-target-layout.md, anchor rule-wp-01.03
- WP-01.04 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\01-repository-reconciliation-and-target-layout.md, anchor rule-wp-01.04
- WP-01.05 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\01-repository-reconciliation-and-target-layout.md, anchor rule-wp-01.05
- WP-01.90 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\01-repository-reconciliation-and-target-layout.md, anchor rule-wp-01.90
- WP-01:cloud-module-layout-acceptance-map-17-hi Cloud module layout acceptance - map 17 historical scaffold names to the 21 declared domain owners in WP21; Cloud owns the Native AOT Container host and Worker bindings, AI owns the sole Workflow Harness; empty module projects are not created during reconciliation (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\01-repository-reconciliation-and-target-layout.md, package-level obligation

Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] GOV.01: WP00's naming/licence freeze closed (GOV.01)
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: *:every .csproj disposition; Contracts:src/Contracts/; *:native/; *:eng/policy/reconciliation/
Unblocks: GOV.03

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Clean-checkout builds with no sibling source, licence/reference-direction checks, offline; per P2-017 no macOS/device runtime.
Completion evidence for the ledger: docs/assurance/wp01-00-implementation-evidence.md/.json, wp01-00-inventory-policy.md, wp01-01-contract-access-policy.md, wp01-01-implementation-evidence.md/.json, wp01-02-foundation-review.md/.json, wp01-03-native-reconciliation-policy.md, wp01-03-native-reconciliation.md/.json, wp01-04-test-family-map.md/.json, wp01-05-bounded-reconciliation.md/.json, wp01-stage-acceptance.md/.json (file names only, via ls; bodies not read).
Notes: Also closes the unlabeled 'Cloud module layout acceptance' package obligation (17 historical scaffold names -> 21 declared WP21 domain owners); see package_obligations.
```

```text
Execute ArcForges delivery task GOV.03 — Build governance, packaging policy and analyzers (WP02, accepted).

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\governance.md (anchor task-gov-03).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/gov-03 (python tools/delivery.py claim GOV.03 --worker <name>); task branch task/gov-03 in DesktopPlatform; ledger record ledger/tasks/gov-03.md.
Kind/size: governance/XL. Baseline: accepted.
Outcome: WP02 build governance is accepted: pinned/locked toolchains in all seven owners, warnings-as-errors with an empty authored-code waiver list, a complete AOT/trim declaration sweep with zero unassigned diagnostics, verified runtime/directory boundaries, all nine version axes producible, and dependency-admission policy encoded as data.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-02.00 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\02-build-governance-and-analyzer-policy.md, anchor rule-wp-02.00
- WP-02.01 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\02-build-governance-and-analyzer-policy.md, anchor rule-wp-02.01
- WP-02.02 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\02-build-governance-and-analyzer-policy.md, anchor rule-wp-02.02
- WP-02.03 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\02-build-governance-and-analyzer-policy.md, anchor rule-wp-02.03
- WP-02.04 (full, under P2-017): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\02-build-governance-and-analyzer-policy.md, anchor rule-wp-02.04
- WP-02.05 (full, under P2-017): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\02-build-governance-and-analyzer-policy.md, anchor rule-wp-02.05
- WP-02.90 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\02-build-governance-and-analyzer-policy.md, anchor rule-wp-02.90

Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] GOV.02: WP01's settled project set and dispositions (GOV.02)
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: *:global.json; *:Directory.Build.props/.targets; *:Directory.Packages.props; *:packages.lock.json; DesktopPlatform:eng/build/desktop-aot.props; Cloud:eng/build/cloud-aot.props; Mobile:gradle/*; Web:package.json,package-lock.json,.node-version,.npmrc,ArcForges.Web.esproj; Contracts:eng/build/contracts.props; *:.editorconfig; DesktopPlatform:eng/policy/dependency-policy.json
Shared resources (follow the owner protocol): RES-desktopplatform-policy-data (append): Generated policy data is regenerated from its pinned source and never hand-edited; the reason-code registry is append-only with stable codes; each task adds its own test classes and evidence rows.
Unblocks: GOV.04, GOV.11, GOV.12, REL.06, WEB.01, WEB.08

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Clean-machine locked restores, warnings-as-errors full-solution build, complete AOT/trim diagnostic sweep, per P2-017 reduced CI for 02.04/02.05 (no new macOS/device/download runtime).
Completion evidence for the ledger: docs/assurance/wp02-00-implementation-evidence.md/.json, wp02-00-toolchain-profile.md, wp02-01-diagnostic-profile.md, wp02-01-implementation-evidence.md/.json, wp02-02-aot-sweep-evidence.md/.json, wp02-03-runtime-boundary-evidence.md/.json, wp02-03-runtime-boundary-profile.md, wp02-04-implementation-evidence.md/.json, wp02-04-version-identity-profile.md, wp02-05-dependency-policy-profile.md, wp02-05-implementation-evidence.md/.json, wp02-stage-acceptance.md/.json (file names only, via ls; bodies not read).
Notes: VG-08 (framework upgrade re-verification) is explicitly recurring: WP02.05's evidence closes the first instance only; every future dependency/framework upgrade re-triggers VG-08 outside this task's own closure.
```

```text
Execute ArcForges delivery task GOV.04 — Shared architecture/repository policy-test engine and DesktopPlatform enforcement.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\governance.md (anchor task-gov-04).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/gov-04 (python tools/delivery.py claim GOV.04 --worker <name>); task branch task/gov-04 in DesktopPlatform; ledger record ledger/tasks/gov-04.md.
Kind/size: governance/L. Baseline: not-started.
Outcome: A reusable AT-01..14/RP-01..10 rule engine, project-graph reader, fixture compiler and banned-symbol scanner extend DesktopPlatform's existing 5-method RepositoryPolicyTests.cs baseline (WP01.04) to the full rule set, are published for the other six repositories to reuse, and DesktopPlatform's own project graph is fully enforced with one positive and one failing negative fixture per rule.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-05.00 (build the reusable AT-01..14/RP-01..10 rule engine and project-graph reader; apply it to DesktopPlatform's own layering/reference-direction rules): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\05-architecture-and-repository-policy-tests.md, anchor rule-wp-05.00
- WP-05.01 (licence-boundary rule implementation in the shared engine; DesktopPlatform's own licence-boundary enforcement): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\05-architecture-and-repository-policy-tests.md, anchor rule-wp-05.01
- WP-05.04 (banned-symbol scanner mechanism in the shared engine; DesktopPlatform's own banned-API fixtures): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\05-architecture-and-repository-policy-tests.md, anchor rule-wp-05.04
- WP-05.02 (wire the existing WP00.00 forbidden-term scanner into DesktopPlatform's own PR build as a failing policy test): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\05-architecture-and-repository-policy-tests.md, anchor rule-wp-05.02

Entry condition: adoption slice ADOPT.02.governance is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] GOV.03: a build that fails on warnings/AOT diagnostics (GOV.03)
- [artifact] GOV.01: exported glossary-terms.json/invariants.json policy data (GOV.01)
- [artifact] GOV.18: policy data reduced to the retained repositories
- [artifact] CON.23: Immutable canonical naming policy/scanner build-time candidate asset
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:src/Build/ArcForges.Build.Policy/Architecture/** (single shared C# policy engine, project graph, fixture compiler, banned-symbol scanner and explicit opt-in source-link props); DesktopPlatform:src/Build/ArcForges.Build.Policy/ArcForges.Build.Policy.csproj (package the same engine source as tools/architecture build-only assets; preserve existing default behavior and package identity); DesktopPlatform:src/Build/ArcForges.Build.Policy/README.md (owned opt-in test/build-only engine contract); DesktopPlatform:tests/ArchitectureTests/**; DesktopPlatform:eng/policy/exceptions.json; DesktopPlatform:Directory.Packages.props (exact canonical naming-tool package pin); DesktopPlatform:eng/policy/dependency-policy.json (canonical naming-tool admission); DesktopPlatform:eng/policy/dependency-reviews/** (new immutable naming-tool admission receipt); DesktopPlatform:eng/provenance/** (owned naming-tool inventory and new receipts; preserve historical records)
Shared resources (follow the owner protocol): RES-architecture-tests (append): Each repository policy task owns its suite; rule additions are append-only.; RES-desktopplatform-policy-data (append): Generated policy data is regenerated from its pinned source and never hand-edited; the reason-code registry is append-only with stable codes; each task adds its own test classes and evidence rows.; RES-desktopplatform-build-config (append): Solution/project lists, central package versions and CI job lists are appended by the task that adds a project, dependency or job; dependency additions follow the dependency-admission policy with a reviewed receipt; lock files are regenerated after rebase and never hand-merged; the integration owner resolves ordering conflicts at merge.
Unblocks: GOV.05, GOV.06, GOV.07, GOV.09, GOV.12, GOV.13, GOV.15

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline unit/analyzer-style project-graph assertions, one positive and one failing negative fixture per rule, runs in PR CI; no macOS/device/live runtime per P2-017.
Completion evidence for the ledger: Full AT-01..14/RP-01..10 rule table with pass/fail fixture pairs; banned-symbol detection results per category (reflection on AOT paths, dynamic codegen, blocking waits on async paths, direct provider SDK calls outside adapters, secret/content logging, float money arithmetic, raw pointer fields).
Notes: The existing ArcForges.Build.Policy package publishes one C# engine source under tools/architecture, linked explicitly into offline consumer policy tests through ArchitecturePolicy.props. DesktopPlatform ArchitectureTests exercise that same producer source; no copied Python engine, new package identity, implicit default hook or product runtime dependency. Preserve existing AGPL/build-only and PrivateAssets boundaries. The already pinned SDK Roslyn assemblies may serve the offline fixture compiler under existing dependency admission; do not introduce a new NuGet dependency or provision another SDK. Necessary existing project/packaging/lock/inventory/provenance bindings follow ADP-07 with exact paths and evidence recorded before editing. This is the shared-tooling half of WP05's own binding statement: 'Repositories: Each repository; shared tooling in Platform/Contracts.'
```

```text
Execute ArcForges delivery task GOV.05 — Contracts policy tests and contract/serialization policy engine.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\governance.md (anchor task-gov-05).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Contracts (integration owner: Contracts integration owner, the holder of roles/integration-contracts).
Claim and handoff record: claims/gov-05 (python tools/delivery.py claim GOV.05 --worker <name>); task branch task/gov-05 in Contracts; ledger record ledger/tasks/gov-05.md.
Kind/size: governance/L. Baseline: not-started.
Outcome: Contracts enforces its own layering/licence/banned-API rules using GOV.04's shared engine, and implements the contract/serialization policy engine that makes VG-04's policy-test half enforceable and that GOV.07 and GOV.09-GOV.12 reuse for their own generated-client checks.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-05.03 (full: build the contract/serialization policy engine (generated-from-proto DTO check, explicit JSON metadata for HTTP exceptions, no reflection-based serializer reachable, every local RPC contract interface carries the generated service/descriptor identity, generated artifacts match the committed baseline) and apply it to Contracts itself): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\05-architecture-and-repository-policy-tests.md, anchor rule-wp-05.03
- WP-05.00 (Contracts layering: contract projects reference only contract projects and the foundation): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\05-architecture-and-repository-policy-tests.md, anchor rule-wp-05.00
- WP-05.01 (Contracts licence-boundary enforcement (public/internal Apache-2.0 split from WP01.01)): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\05-architecture-and-repository-policy-tests.md, anchor rule-wp-05.01
- WP-05.02 (wire the forbidden-term scanner into Contracts' own PR build as a failing policy test): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\05-architecture-and-repository-policy-tests.md, anchor rule-wp-05.02
- WP-05.04 (Contracts banned-API fixtures): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\05-architecture-and-repository-policy-tests.md, anchor rule-wp-05.04

Entry condition: adoption slice ADOPT.03.governance is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] GOV.04: published shared AT-*/RP-* rule engine, fixture compiler and project-graph reader
- [contract] CON.90: Contracts' public/internal Apache-2.0 project split and generated proto baseline
- [artifact] CON.23: retired Contracts elements removed and reserved
- [artifact] GOV.06: the published ArcForges.Build.Policy candidate whose ProjectGraph reconstruction includes pinned-SDK generated sources and whose generated-type recognition accepts protoc and schema-generator output
Completion prerequisites (may start earlier; cannot complete before these are complete):
- [integration] GOV.06: the published ArcForges.Build.Policy candidate whose ProjectGraph reconstruction includes pinned-SDK generated sources

Permitted write scope: Contracts:tests/ArchitectureTests/**; Contracts:eng/policy/exceptions.json; Contracts:ArcForges.Contracts.slnx; Contracts:eng/contracts.py; Contracts:.github/workflows/security.yml (wire the hosted architecture-policy gate into the existing secrets job only, after the unchanged Gitleaks step: pinned setup-dotnet/setup-python, locked restore, Release build, python eng/check_naming.py --report artifacts/evidence/naming.json, then ArchitectureTests --hosted, in the order the gate verifies; no change to the Gitleaks command, history scope, allowlist, permissions, action pins of existing steps, other jobs, thresholds or continue-on-error/if-always behavior); Contracts:Directory.Packages.props; Contracts:tests/ArchitectureTests/packages.lock.json; Contracts:eng/policy/dependency-policy.json; Contracts:eng/policy/dependency-reviews/gov-05-*.json; Contracts:eng/policy/contract-access.json (only the existing buildInputs["Directory.Packages.props"] normalized SHA256 binding for this task's central Build.Policy pin); Contracts:.gitleaks.toml (support-only exact receipt false-positive allowlist for rule generic-api-key); Contracts:eng/policy/licence-boundary.json; Contracts:eng/provenance/files.json; Contracts:eng/dependency_admission.py; Contracts:tests/tooling/test_dependency_admission.py; Contracts:eng/check_licences.py; Contracts:tests/tooling/test_licence_boundary.py
Shared resources (follow the owner protocol): RES-architecture-tests (append): Each repository policy task owns its suite; rule additions are append-only.; RES-contracts-schema-sources (append): Each schema closure task edits only its own domain proto or HTTP-schema files and adds its own sharded constraint and fixture files. Schema-closure tasks and Contracts policy tasks that touch package/access/provenance/dependency input registries share this append/rebase protocol: append only task-owned rows and successor receipts to package, compiled access/hash, foundation, operation, constraint, provenance source/output, binding, and dependency-review inventories; preserve prior history and never rewrite another task's rows. Refresh dependency input hashes only for the task-owned closure; do not expand dependency versions or closure except for the two exact task-specific exceptions below. One narrow exception applies only to CON.14: it may add the single ArcForges.Contracts.CloudInternal → existing ArcForges.Contracts.PublicApi package/project edge required for generated OperatorService imports to resolve to their canonical owner, implemented only by one ProjectReference in the CloudInternal csproj, its existing packages.lock.json, and the CloudInternal dependency row in eng/contract-packages.json. This expands only CloudInternal's package-specific closure to include the existing PublicApi package and its existing same-version transitive realization; the lock may add the PublicApi project and already-pinned Grpc.Core.Api 2.84.0, while existing Foundation and Google.Protobuf 3.36.1 entries retain their versions and hashes. The exception permits only the matching exact input-hash refreshes and immutable con-14-r1 successor chained from active con-22-r1. Preserve the aggregate dependency coordinate/version set, package IDs and licences, every other package's dependency usage/closure, Foundation/PublicApi ownership, all prior receipt history, and the PublicApi 1.0.0-ci.113.1 PreviousClient-only fixture classification. A second, CON.11-only exception permits only the already-authorized Events → PublicApi and CloudInternal → Events/PublicApi project references to realize in Events and CloudInternal as the corresponding first-party Project lock entries plus the exact centrally pinned Grpc.Core.Api CentralTransitive row: requested [2.84.0, ), resolved 2.84.0, contentHash p2SOMl6q/GZ4/5MLkgboC/z55g4zKUEruRn/g46QgppjQBVnsLZVBU/9VO7n60ll38G3Eo8Zu9b7x+W01GKFVg==. Only the five existing consumer lockfiles tests/StructureTests/packages.lock.json, tests/public/SerializationProbe/packages.lock.json, src/public/dotnet/ArcForges.Sdk.Client/packages.lock.json, src/public/dotnet/ArcForges.Cli/packages.lock.json, and src/public/dotnet/ArcForges.Contracts.Validation/packages.lock.json may add ArcForges.Contracts.PublicApi [1.0.0-ci.0.0, ) to the existing ArcForges.Contracts.Events Project.dependencies field, exactly as SDK restore requires. In only tests/StructureTests/packages.lock.json and tests/public/SerializationProbe/packages.lock.json, SDK restore may also add ArcForges.Contracts.Events and ArcForges.Contracts.PublicApi [1.0.0-ci.0.0, ) to the existing ArcForges.Contracts.CloudInternal Project.dependencies field, exactly as the already-authorized CloudInternal -> Events/PublicApi project references require; no other field, package/project entry, project dependency, target framework, version, hash, or consumer behavior changes. This exception permits only these matching task-owned lock/policy input-hash refreshes and the immutable con-11-r1 successor, and preserves the aggregate coordinate/version/licence union, all other package usage/closures, existing Foundation, Google.Protobuf and Microsoft.NET.ILLink.Tasks rows, previous receipt history, package identities and the PreviousClient-only fixture classification. No direct package reference, PrivateAssets or asset override, other coordinate/version/hash, project, lock row, licence exception or dependency algorithm change is authorized; all other tasks retain the no-closure-expansion rule. Public Kotlin/Dokka successors are exclusively governed by RES-contracts-dokka-profile. A proto file with several contributing tasks (operator, policy/configuration) has one designated author task and the others request changes through it. Each serialized merge is followed by a rebase and regeneration before integration of the next task.
Unblocks: GOV.07, GOV.09, GOV.15

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline unit tests, negative fixtures per assertion, PR CI; no live-service runtime per P2-017.
Completion evidence for the ledger: Contract/serialization policy results with negative fixtures per assertion; Contracts' own layering/licence/banned-API results.
Notes: WP05's own §8 completion-gate text states this substep 'makes VG-04's policy-test half enforceable' - a second VG-04 contributor not listed in the README's deferred-gate table (which names only 03.04/06.01). The narrowly required ArcForges.Build.Policy 1.0.0-ci.31.1 AGPL admission permits a direct PackageReference only from Contracts tests/ArchitectureTests, with PrivateAssets=all, for architecture-test/build use. Regression negatives must reject this exact package from every other project or package closure, including product/runtime and generated-public-package closures; do not broaden the exception. This task may update only the existing buildInputs["Directory.Packages.props"] SHA256 in eng/policy/contract-access.json to the independently recomputed LF-normalized SHA256 of the final Directory.Packages.props at the reviewed head after the authorized central Build.Policy pin (the pin is the exact candidate published by GOV.06; no literal digest is recorded here because the file and its digest move whenever main's central pins change, and the worker and the reviewer each recompute it at the head under review); do not alter contract access, package graph, categories, schema, or checker. Refresh only the matching dependency-policy.inputHashes["eng/policy/contract-access.json"] and current active dependency-policy.review.inputHashes["eng/policy/contract-access.json"] entries to the independently recomputed final LF-normalized contract-access.json SHA256 at the reviewed head required by dependency admission (the literal previously recorded in this task, fcd8b5a1..., is stale: the exact-head recovery of PR 71 recomputed 27c315c3... and current main differs again); both current entries must remain identical under the retained admission invariant, and no coordinate, project, historical receipt, other review field or other input binding may change. For the support-only .gitleaks.toml addition, allow only rule generic-api-key, exact containing paths AND complete JSON key/value lines for that final recomputed contract-access.json digest in eng/policy/dependency-policy.json and for the exact four review.inputHashes tuples in eng/policy/dependency-reviews/gov-05-r1.json: eng/policy/contract-access.json -> that final recomputed digest (observed pre-repair value c339d391aeb89aabb9a5b503f152436905048c4855a72065fc4bc85712252ea7); eng/provenance/records/dokka-combokeys-licence-r1.json -> 75219d61672002f0bb242fed0fd93a0886f07d944e0b9e1b1f72132f59df1b41; eng/provenance/records/dokka-object-keys-licence-r1.json -> 55621ecc7032745ca46e56d13133dc22a3bd808d80966d737427b5d6fc5bd096; src/public/dotnet/ArcForges.Contracts.PublicApi/ArcForges.Contracts.PublicApi.csproj -> 986b7a97734cd5d0630e548da897869de322a112c087c2d0df6a0bfc98b8784c. Use exactly that one final recomputed digest in dependency-policy, gov-05-r1 and both exact allowlist path bindings; recompute it and the three other digests (which this repair re-verified unchanged at Contracts main and at PR 71's head) again at the final reviewed head and have the reviewer independently confirm every allowlisted line against it; any rebase that changes Directory.Packages.props or contract-access.json changes it and requires re-recording; no inferred replacement is authorized. Keep the other three exact tuples bound to these values and preserve the historical CON.06 block unchanged. No wildcard receipt/path entries, source allowlist, other rule, threshold, scan scope, command, workflow or history change; do not change receipt format or bypass the parser/scanner. Shared Contracts solution, policy and provenance edits rebase and merge one-at-a-time under the Contracts integration owner after exact-head review.

Planning repair 2026-10-04. (1) Generated wire types: the AT-12 findings recorded for PR 71 come from the shared engine and are repaired by GOV.06, now a start prerequisite; do not stamp attributes in Contracts generators and do not hide AT-12 with an exception row. Pin the exact GOV.06 candidate through this task's own reviewed successor receipt (a version change of the existing ArcForges.Build.Policy identity inside the existing admission restrictions; no other coordinate). (2) RP-03 decision: the Apache-boundary tests/ArchitectureTests host references the AGPL ArcForges.Build.Policy package that this task's own admission permits (direct reference from this one project only, PrivateAssets=all, IsPackable=false, build/test use). Design docs/architecture/01-solution-and-project-layout.md section 4.1 fixes Contracts as Apache with Apache-2.0 and forbids relabelling the host or the licence, and LB-06 forbids silent exceptions, so this reviewed planning change records the resolution: exactly one row in eng/policy/exceptions.json using the engine's exception fields (rule RP-03, path tests/ArchitectureTests/ArcForges.Contracts.ArchitectureTests.csproj, owner Contracts, reason naming this admission and its restrictions, expires no later than 2027-04-04). The engine already rejects wildcard rules and paths, a non-owner and an expired row (it throws), and matches rule plus exact path only. Renewal path: before expiry, a reviewed Contracts pull request that changes only that row's expires date, with Architecture Owner approval recorded on the pull request and the admission unchanged, or removal of the row by a successor that moves the engine host out of the Apache closure; otherwise the gate fails closed at expiry. The row waives nothing else: the regression negatives still reject the package from every other project and package closure, and no other path or rule may be added. (3) Hosted wiring: the implemented gate verifies that the secrets job of .github/workflows/security.yml runs the pinned build, canonical naming report and ArchitectureTests --hosted after the unchanged Gitleaks step, so that file is now in write scope for that wiring only; PR 71's passing security checks do not exercise a gate that is not wired. No other change to security.yml is authorized.
```

```text
Execute ArcForges delivery task GOV.06 — Build.Policy generated-source reconstruction and generated-type recognition repair.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\governance.md (anchor task-gov-06).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/gov-06 (python tools/delivery.py claim GOV.06 --worker <name>); task branch task/gov-06 in DesktopPlatform; ledger record ledger/tasks/gov-06.md.
Kind/size: governance/M. Baseline: not-started.
Outcome: The existing ArcForges.Build.Policy ProjectGraph reader materializes a selected project's sources through the pinned SDK's actual compiler/source-generator pipeline before semantic reconstruction; generated source participates in compilation diagnostics, and a GeneratedRegex partial regression passes. The normal DesktopPlatform merge publishes the fixed candidate under the existing ArcForges.Build.Policy package identity. The same normal merge also repairs the engine's generated-type test: the private generated-type recognition in PolicyEngine (used by the AT-11 generated-interface check and the AT-12 wire-type check) accepts, in addition to today's class-level GeneratedCode attribute from protoc, Google.Protobuf, grpc_csharp_plugin or ArcForges.SchemaGenerator, a type declared in a syntax tree whose leading header comment contains <auto-generated (the Roslyn generated-code convention), with nested types following their container. Positive and negative regressions pass: an attributed type and a header-marked type are recognised; an authored type without either, and a type whose file mentions <auto-generated only in a non-leading comment, are still rejected; a recognised type that has no schema binding or whose schema hash differs still fails AT-12.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-05.00 (DesktopPlatform project-graph repair: run the pinned SDK compiler and configured source generators before semantic reconstruction, include generated sources in fail-closed diagnostics, and prove GeneratedRegex partial-method reconstruction): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\05-architecture-and-repository-policy-tests.md, anchor rule-wp-05.00
- WP-05.03 (shared-engine generated-type recognition: the AT-11 interface-identity and AT-12 wire-type checks must recognise real protoc output and schema-generator output (a type declared in a source file with a leading <auto-generated header comment), so Contracts' generated-from-proto DTO check and the other consumers' generated-client checks can pass over actual generated shapes): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\05-architecture-and-repository-policy-tests.md, anchor rule-wp-05.03

Entry condition: adoption slice ADOPT.02.governance is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] GOV.04: the published shared ProjectGraph reader and architecture-policy package
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:src/Build/ArcForges.Build.Policy/Architecture/ProjectGraph.cs (ReadCompilation source materialization and semantic reconstruction only); DesktopPlatform:src/Build/ArcForges.Build.Policy/Architecture/PolicyEngine.cs (the private generated-type recognition used by AT-11/AT-12 only; no other rule, rule identifier, message, threshold or exception-handling change); DesktopPlatform:tests/ArchitectureTests/GeneratedSourceReconstructionTests.cs (GeneratedRegex partial-method regression only); DesktopPlatform:tests/ArchitectureTests/GeneratedTypeRecognitionTests.cs (positive and negative generated-type recognition regressions over in-memory compilations only); DesktopPlatform:eng/provenance/files.json (append only the exact first-party regression source paths of the new test files); DesktopPlatform:eng/policy/dependency-policy.json (only exact active-input hashes/review binding required by the existing dependency/provenance gates; no dependency or closure changes); DesktopPlatform:eng/policy/dependency-reviews/gov-06-r1.json (new immutable successor only if an existing registered input changes; chain from the exact then-active receipt, preserve history and the full admitted closure)
Shared resources (follow the owner protocol): RES-architecture-tests (append): Each repository policy task owns its suite; rule additions are append-only.; RES-desktopplatform-policy-data (append): Generated policy data is regenerated from its pinned source and never hand-edited; the reason-code registry is append-only with stable codes; each task adds its own test classes and evidence rows.; RES-desktopplatform-package-inventory (read): Each producer task adds its own package entry; every merge to main packs and publishes all packages at one version; consumers pin the candidate produced by the merge of the capability they need, never waiting for a package closure task; one merge queue.
Unblocks: GOV.05, GOV.07, GOV.09

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Pinned SDK 10.0.400 locked restore and applicable Release build; ArchitectureTests GeneratedRegex regression must show SDK-produced partial implementation in the reconstructed compilation and keep compiler diagnostics fail-closed; all existing DesktopPlatform PR CI and package-validation checks pass. The normal DesktopPlatform integration merge publishes the next candidate under the same ArcForges.Build.Policy package identity.
Completion evidence for the ledger: Exact-head local and hosted results for the GeneratedRegex regression and retained policy suite; exact source commit and successful publication receipt identifying the new ArcForges.Build.Policy candidate from the normal DesktopPlatform main merge.
Notes: GOV.06 is a post-adoption planning repair introduced 2026-09-28; its implementation was not covered by the 2026-09-27 ADOPT.02.governance nine-task classification and is a gap, not inherited work. Do not claim GOV.06 until the accompanying Plan change adds a separate Post-adoption adjustment classification for GOV.06 as gap to ledger/tasks/adopt-02-governance.md; preserve that record's status, recorded date, epoch and nine frozen classifications verbatim. This follows DLV-22's later-adoption-adjustment process; do not reopen or rewrite the completed slice, create another adoption task, or add a GOV.06 start prerequisite. Since the 2026-10-04 planning repair GOV.06 is a start (artifact) prerequisite of GOV.05, GOV.07 and GOV.09 and remains a GOV.05 completion prerequisite: their hosted full-graph gates cannot pass, and their pins cannot be reviewed, without the published candidate. It does not invalidate GOV.05's earlier claim record. The 2026-10-04 scope extension is recorded as a further Post-adoption adjustment in ledger/tasks/adopt-02-governance.md; GOV.06 is not claimable until that Plan change also merges. Use the pinned SDK's actual compiler and configured source-generator pipeline to materialize outputs for every selected project before semantic reconstruction. Preserve full-project coverage and fail-closed compilation diagnostics. Do not filter diagnostics, skip projects, synthesize or bypass compiler/generator outputs in the consumer, introduce another scanner/CI mechanism, create a package ID, add a runtime or other dependency, change the SDK/toolchain, or expand package/dependency closure. Preserve the existing ArcForges.Build.Policy package identity and payload topology; do not edit its package inventory entry or consumer pin here. Preserve prior dependency/provenance receipts immutably and create a successor only when an existing gate requires one for an exact task-owned input change. After reviewed DesktopPlatform integration and its normal package publication, GOV.05, GOV.07 and GOV.09 each separately pin the exact published candidate through their own reviewed successors.

Generated-type recognition (added 2026-10-04, evidence): the hosted full-graph run recorded in Contracts PR 71 reports 1843 AT-12 findings across ten contract projects at Contracts main 4047930 because PolicyEngine.Generated (about line 341 of src/Build/ArcForges.Build.Policy/Architecture/PolicyEngine.cs) accepts only a class-level GeneratedCode attribute. Inspected Contracts sources show why that is too narrow: protoc output (for example src/internal/dotnet/ArcForges.Contracts.CloudInternal/Generated/Proto/Operator.cs) stamps GeneratedCode on members while its reflection and gRPC static classes carry no attribute at all, and schema-generated shapes (Generated/Shapes/*.g.cs, Generated/Services/*.g.cs) carry none; every one of those files begins with a leading <auto-generated header comment. Header recognition is therefore the single mechanism that covers messages, enums, reflection, gRPC and schema-generated classes, so no separate member-stamp or IMessage-shape heuristic is added (an authored class could imitate it). Require positive and negative regressions as in the outcome, keep the existing attribute path, keep AT-12's other conditions (a WireTypes binding and a matching schema SHA256) and AT-11's other conditions unchanged, and note that the broadened test also governs AT-11's generated-interface identity check. Do not hide the findings with a role change, exception row, per-project waiver, Contracts-side attribute stamping, diagnostic filtering or generator changes. Do not edit the package inventory entry or any consumer pin here.
```

```text
Execute ArcForges delivery task GOV.07 — ArcScope policy tests.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\governance.md (anchor task-gov-07).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\ArcScope (integration owner: ArcScope integration owner, the holder of roles/integration-arcscope).
Claim and handoff record: claims/gov-07 (python tools/delivery.py claim GOV.07 --worker <name>); task branch task/gov-07 in ArcScope; ledger record ledger/tasks/gov-07.md.
Kind/size: governance/S. Baseline: not-started.
Outcome: ArcScope enforces its own layering/licence/naming/banned-API/contract-consumption rules independently.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-05.00 (ArcScope slice): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\05-architecture-and-repository-policy-tests.md, anchor rule-wp-05.00
- WP-05.01 (ArcScope slice): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\05-architecture-and-repository-policy-tests.md, anchor rule-wp-05.01
- WP-05.02 (wire the forbidden-term scanner into ArcScope's own PR build): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\05-architecture-and-repository-policy-tests.md, anchor rule-wp-05.02
- WP-05.03 (ArcScope's generated-client consumption checks): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\05-architecture-and-repository-policy-tests.md, anchor rule-wp-05.03
- WP-05.04 (ArcScope banned-API fixtures): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\05-architecture-and-repository-policy-tests.md, anchor rule-wp-05.04

Entry condition: adoption slice ADOPT.05.governance is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] GOV.04: published shared rule engine
- [artifact] GOV.05: contract/serialization policy helpers
- [artifact] GOV.06: the published ArcForges.Build.Policy candidate carrying generated-source reconstruction and generated-type recognition
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: ArcScope:tests/ArchitectureTests/**; ArcScope:eng/policy/exceptions.json; ArcScope:ArcScope.slnx (add the new host project only); ArcScope:Directory.Packages.props (the exact ArcForges.Build.Policy pin moved to the published GOV.06 candidate, and the exact published ArcForges.Contracts.Validation candidate that carries the CON.23 build-only naming tools only if the naming scan is wired through it; no other coordinate, runtime or version change); ArcScope:tests/ArchitectureTests/packages.lock.json; ArcScope:src/ArcForges.ArcScope.Domain/packages.lock.json, ArcScope:src/ArcForges.ArcScope.Core/packages.lock.json, ArcScope:src/ArcForges.ArcScope/packages.lock.json, ArcScope:tests/ArcForges.ArcScope.Tests/packages.lock.json, ArcScope:eng/ArcForges.Repository/packages.lock.json (regenerated only for the central pin change); ArcScope:eng/policy/dependency-policy.json; ArcScope:eng/policy/dependency-review.json (the existing active review, updated for the exact task-owned input and coordinate changes; preserve history); ArcScope:eng/policy/licence-boundary.json (the host project row); ArcScope:eng/provenance/files.json; ArcScope:eng/provenance/records/gov-07-*.json (new immutable successors only where an existing record binds an input this task changes); ArcScope:.github/workflows/ci.yml (wire the host build, the forbidden-term scan and the policy run into the existing pull-request job; no new platform, scheduled or manual workflow, no weakened or removed check)
Shared resources (follow the owner protocol): RES-architecture-tests (append): Each repository policy task owns its suite; rule additions are append-only.; RES-product-solutions (append): Solution/project lists, central package versions and CI job lists are appended by the task that adds a project, dependency or job; dependency additions follow the dependency-admission policy with a reviewed receipt; lock files are regenerated after rebase and never hand-merged; the integration owner resolves ordering conflicts at merge.
Unblocks: GOV.15

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline unit tests, negative fixtures, PR CI; per P2-017.
Completion evidence for the ledger: Per-rule pass/fail fixture table for ArcScope's project graph.
Notes: Fixture-driven; does not require ArcScope's own product work (WP33 to WP35) to have landed. Write scope extended by the 2026-10-04 governance-chain planning repair: adding the host project needs the solution entry, the exact ArcForges.Build.Policy pin move (ArcScope pins 1.0.0-ci.20.1, which predates GOV.04's engine candidate 1.0.0-ci.31.1 and GOV.06's repair), every project lock the central pin changes (Directory.Build.props gives every project the package reference), dependency and provenance bindings, the licence inventory row and CI wiring. ArcScope is AGPL-3.0-only, so the host needs no RP-03 exception and none may be added. No security-scanner, gitleaks or secret-scan configuration change is authorized; if a new receipt digest line triggers the secret scan, that needs its own narrow planning repair. The pin cannot move before GOV.06's candidate is published.
```

```text
Execute ArcForges delivery task GOV.09 — Cloud policy tests.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\governance.md (anchor task-gov-09).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/gov-09 (python tools/delivery.py claim GOV.09 --worker <name>); task branch task/gov-09 in Cloud; ledger record ledger/tasks/gov-09.md.
Kind/size: governance/M. Baseline: not-started.
Outcome: Cloud enforces its own layering/licence/naming/banned-API/contract-consumption rules independently, with extra weight on AOT-path banned APIs given BR-07's zero-trim/AOT-diagnostic requirement.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-05.00 (Cloud slice): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\05-architecture-and-repository-policy-tests.md, anchor rule-wp-05.00
- WP-05.01 (Cloud slice): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\05-architecture-and-repository-policy-tests.md, anchor rule-wp-05.01
- WP-05.02 (wire the forbidden-term scanner into Cloud's own PR build): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\05-architecture-and-repository-policy-tests.md, anchor rule-wp-05.02
- WP-05.03 (Cloud's own generated public API/RPC descriptor checks): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\05-architecture-and-repository-policy-tests.md, anchor rule-wp-05.03
- WP-05.04 (Cloud banned-API fixtures, weighted toward AOT-path reflection/dynamic-codegen since Cloud is the Native AOT host): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\05-architecture-and-repository-policy-tests.md, anchor rule-wp-05.04

Entry condition: adoption slice ADOPT.07.governance is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] GOV.04: published shared rule engine
- [artifact] GOV.05: contract/serialization policy helpers
- [artifact] GOV.06: the published ArcForges.Build.Policy candidate carrying generated-source reconstruction and generated-type recognition
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Cloud:tests/ArchitectureTests/**; Cloud:eng/policy/exceptions.json; Cloud:Cloud.slnx (add the new host project only); Cloud:Directory.Packages.props (the exact ArcForges.Build.Policy pin moved to the published GOV.06 candidate; no other coordinate, runtime or version change); Cloud:tests/ArchitectureTests/packages.lock.json; Cloud:src/ArcForges.Cloud/packages.lock.json, Cloud:tests/ArcForges.Cloud.Tests/packages.lock.json, Cloud:tests/ArcForges.Cloud.Consumer/packages.lock.json (regenerated only for the central pin change); Cloud:eng/policy/dependency-policy.json; Cloud:eng/policy/dependency-reviews/gov-09-*.json (new immutable successor chained from the then-active receipt); Cloud:eng/policy/licence-boundary.json (the host project row); Cloud:eng/provenance/files.json; Cloud:eng/provenance/records/gov-09-*.json (new immutable successors only where an existing record binds an input this task changes); Cloud:eng/policy/naming-candidate.json (exact published @arcforges/proto naming-tool identity and asset hashes, as in Web); Cloud:tooling/project.ts (wire the forbidden-term scan into the existing check gate only); Cloud:package.json (a policy script and the exact already-locked @arcforges/proto devDependency; no version change); Cloud:package-lock.json (reflect that manifest change only); Cloud:.github/workflows/ci.yml (wire the host build and policy run into the existing pull-request job; no new platform, scheduled or manual workflow, no weakened or removed check)
Shared resources (follow the owner protocol): RES-architecture-tests (append): Each repository policy task owns its suite; rule additions are append-only.
Unblocks: GOV.15

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline unit tests, negative fixtures, PR CI; per P2-017 (Cloud's real AOT publish proof is WP06/WP21, not claimed here).
Completion evidence for the ledger: Per-rule pass/fail fixture table for Cloud's project graph.
Notes: Fixture-driven; does not require Cloud's own product work (WP21 to WP26) to have landed. Write scope extended by the 2026-10-04 governance-chain planning repair for the same supporting set as ArcScope's GOV.07 (host solution entry, exact ArcForges.Build.Policy pin move from 1.0.0-ci.21.1, every project lock that pin changes, dependency and provenance bindings, licence row, CI wiring), plus the naming-scan wiring. Cloud is AGPL-3.0-only, so the host needs no RP-03 exception and none may be added. Scope boundary: the engine and fixture scope is the C# project graph (src/ArcForges.Cloud and its tests). The worker/ TypeScript tree is NOT given a TS import or route policy by this task (the unlabeled WP-05 Node/TS assertion paragraph is mapped to GOV.11 only); it is covered only by the repository-wide forbidden-term scan wired through tooling/project.ts and by the existing licence, dependency and provenance tooling. A Cloud worker import policy, if wanted, needs its own planning change. No security-scanner, gitleaks or secret-scan configuration change is authorized. The pin cannot move before GOV.06's candidate is published.
```

```text
Execute ArcForges delivery task GOV.10 — AI (Workflow Harness) policy tests.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\governance.md (anchor task-gov-10).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\AI (integration owner: AI integration owner, the holder of roles/integration-ai).
Claim and handoff record: claims/gov-10 (python tools/delivery.py claim GOV.10 --worker <name>); task branch task/gov-10 in AI; ledger record ledger/tasks/gov-10.md.
Kind/size: governance/S. Baseline: not-started.
Outcome: AI enforces its own layering/licence/naming/banned-API/contract-consumption rules independently as the sole owner of the Workflow Harness (per WP01's Cloud/AI module split).

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-05.00 (AI slice): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\05-architecture-and-repository-policy-tests.md, anchor rule-wp-05.00
- WP-05.01 (AI slice): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\05-architecture-and-repository-policy-tests.md, anchor rule-wp-05.01
- WP-05.02 (wire the forbidden-term scanner into AI's own PR build): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\05-architecture-and-repository-policy-tests.md, anchor rule-wp-05.02
- WP-05.03 (AI's generated-client consumption checks): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\05-architecture-and-repository-policy-tests.md, anchor rule-wp-05.03
- WP-05.04 (AI banned-API fixtures): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\05-architecture-and-repository-policy-tests.md, anchor rule-wp-05.04

Entry condition: adoption slice ADOPT.08.governance is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] CON.23: Immutable canonical naming policy/scanner build-time candidate asset
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: AI:tests/ArchitectureTests/**; AI:eng/policy/** (owned Node/TypeScript policy sources and offline fixtures, exceptions.json, naming-candidate.json); AI:eng/provenance/** (owned policy source inventory and new receipts; preserve historical records); AI:package.json (policy scripts and the exact published @arcforges/proto naming-tool candidate pin); AI:package-lock.json (regenerate exact naming-tool candidate lock); AI:eng/project.mjs (wire owned policy checks into the existing check gate); AI:vitest.config.ts, AI:tsconfig.tools.json (include the owned policy sources and tests only); AI:eng/policy/dependency-policy.json, AI:eng/policy/dependency-reviews/** (immutable naming-tool pin admission receipt and exact input bindings); AI:eng/build-identity.mjs, AI:eng/tests/build-identity.test.mjs, AI:eng/version-sources.json (read the published @arcforges/proto build-identity ContractSet, whose subjects declare their own schema versions and one or several schema sources, instead of the retired single-schema source receipt field; cross-check it against the installed source receipt and the exact package pin; add focused positive and negative tests; no other behavior change; the reused cloud-build-identity-r1 record is superseded by an immutable successor under AI:eng/provenance/**); AI:eng/tests/release-provenance.test.mjs (update only the expected parsed and emitted input counts of the actual candidate to the reviewed ai-worker-r8 profile); AI:tests/tsconfig.json (exclude tests/ArchitectureTests from the Workers-typed test project; the owned suite is type-checked by tsconfig.tools.json with Node types; no other change); AI:README.md, AI:docs/development.md (state the new exact @arcforges/proto pin where the toolchain table names it; no other change); AI:.gitleaks.toml (extend only the existing generic-api-key allowlist path pattern from ai-worker-r[1234567] to ai-worker-r[12345678], and its description, so that the single existing whole-line api_pb.js digest repeated by the immutable ai-worker-r8 profile is accepted exactly as for r1 to r7; no other rule, path, regex, digest or scanner behavior)
Shared resources (follow the owner protocol): RES-architecture-tests (append): Each repository policy task owns its suite; rule additions are append-only.
Unblocks: GOV.15

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline unit tests, negative fixtures, PR CI; per P2-017.
Completion evidence for the ledger: Per-rule pass/fail fixture table for AI's project graph.
Notes: Fixture-driven; does not require AI's own product work (WP40 to WP43, WP52) to have landed. Rebound by the 2026-10-04 governance-chain planning repair: AI is a pure Node/TypeScript repository with no .NET project and no ArcForges.Build.Policy reference, so GOV.04's C# engine and GOV.05's Contracts-hosted policy engine cannot run there and the GOV.04 and GOV.05 start edges are replaced by the CON.23 artifact edge for the published naming scanner. Mirror GOV.11's mechanism (Node/TS static import and dependency policy over the real Git inventory, with passing and failing negative fixtures): mechanism is necessarily separate code from GOV.04's .NET engine, as GOV.11 records. Layering, licence boundary, generated-client consumption (generated wire types from the pinned @arcforges/proto only, no handwritten codec) and banned-API fixtures are implemented in that Node/TS mechanism; WP-05.02 consumes the published naming scanner and policy with exact producer, source and asset identity checked before execution, never a sibling checkout or copied rule. The pin of the naming-tool candidate is the only dependency version change. No security-scanner, gitleaks or secret-scan configuration change is authorized (AI's .gitleaks.toml is not in scope); if a new receipt digest line triggers the secret scan, that needs its own narrow planning repair. Offline only; no Workers AI or live run. Write scope extended by the 2026-10-04 GOV.10 planning repair after the pin move was found to need supporting bindings the previous repair did not list. (1) The published @arcforges/proto 1.0.0-ci.287.1 source receipt no longer carries the single schema field that eng/build-identity.mjs reads for the ContractSet axis, and every published candidate that carries the naming tools (CON.23 introduced them at 1.0.0-ci.129.1) has the same shape, so no naming-tool candidate can be pinned unless the build identity reads the producer's own published build-identity, as Web GOV.11 did: each subject keeps its own schema version and may name one or several schema sources, and the producer owner, clean source, exact package pin, complete schema-source hash set and descriptor hashes are cross-checked against the installed source receipt; focused positive and negative tests are added and the reused cloud-build-identity-r1 record gets an immutable successor. (2) The eng/tests/release-provenance.test.mjs counts follow the reviewed ai-worker-r8 profile (the emitted Worker bytes and source-map membership are unchanged; the parsed closure grows by 23 modules of the same package that are not emitted). (3) tests/tsconfig.json excludes the owned suite, which needs Node types and TypeScript import extensions that the Workers-typed test project does not provide. (4) The two documents that name the pin are updated. (5) Secret-scan support, the narrow planning repair that the preceding sentence about the secret scan requires (same class as the merged r7 admission): the immutable ai-worker-r8 profile necessarily repeats the one public digest line of protobuf 2.15.0 api_pb.js that the existing allowlist accepts for r1 to r7 by exact path pattern and exact whole line; only that path pattern is extended to r8, and the unchanged regex line still accepts nothing else. This authorizes no other .gitleaks.toml change, no new rule or allowlist, no scanner, workflow or baseline change and no change to any other repository's configuration. Passing pinned full-history secret-scan evidence on the GOV.10 head is required.
```

```text
Execute ArcForges delivery task GOV.11 — Web policy tests (Node/TS mechanism).

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\governance.md (anchor task-gov-11).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Web (integration owner: Web integration owner, the holder of roles/integration-web).
Claim and handoff record: claims/gov-11 (python tools/delivery.py claim GOV.11 --worker <name>); task branch task/gov-11 in Web; ledger record ledger/tasks/gov-11.md.
Kind/size: governance/M. Baseline: not-started.
Outcome: Node/TS import and dependency policy checks enforce one Web workspace/lock, exact Node/npm/generator pins, SDK-to-UI licence separation, generated wire types only, no private/server/local-RPC imports, desktop JS/DOM prohibition scoped to desktop graphs, no obsolete Blazor target in the active Web graph, no esproj in portable managed references, no implicit npm install or production dev/HMR server, and no TS fixtures/test helpers in the release route graph - each with a passing and a failing negative example.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-05.01 (Web slice: SDK-to-UI licence separation): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\05-architecture-and-repository-policy-tests.md, anchor rule-wp-05.01
- WP-05.02 (wire the forbidden-term scanner into Web's own PR build): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\05-architecture-and-repository-policy-tests.md, anchor rule-wp-05.02
- WP-05.04 (Web banned dependency/route fixtures): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\05-architecture-and-repository-policy-tests.md, anchor rule-wp-05.04
- WP-05:web-repository-and-architecture-assertio Web repository and architecture assertions (unlabeled paragraph after WP-05.06): Node/TS import and dependency checks - one Web workspace/lock, exact Node/npm/generator pins, SDK-to-UI licence separation, generated wire types only, no private/server/local-RPC imports, desktop JS/DOM prohibition scoped to desktop graphs, no obsolete Blazor target, no esproj in portable managed references, no implicit npm install or production dev/HMR server, no TS fixtures/test helpers in the release route graph (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\05-architecture-and-repository-policy-tests.md, package-level obligation

Entry condition: adoption slice ADOPT.09.governance is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] GOV.03: the one Node/npm workspace and Windows esproj adapter (GOV.03)
- [artifact] GOV.01: licence boundary declarations (mobile-only/public-SDK Apache set)
- [artifact] CON.23: Immutable canonical naming policy/scanner build-time candidate asset
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Web:apps/site/app/cloud-hello.ts (remove obsolete explicit useBinaryFormat option for the pinned SDK that internally requires binary; no transport behavior change); Web:tests/unit/contracts.test.ts (same pinned SDK option adaptation only; retain binary transport assertions); Web:eng/policy/**; Web:.eslintrc*/lint-config for architecture rules; Web:tooling/project.ts (wire owned policy checks into existing PR gate); Web:tests/unit/** (offline policy positive/negative fixtures); Web:eng/provenance/** (owned policy source inventory and new receipts; preserve historical records); Web:apps/site/package.json (exact published naming-tool candidate pin and required existing SDK lockstep); Web:package-lock.json (regenerate exact naming-tool candidate lock); Web:eng/policy/dependency-reviews/** (immutable naming-tool pin admission receipt); Web:.gitleaks.toml (extend the existing anchored browser-resources-r1 through r6 path selection to r7 only for its eight actually observed public source-hash rows, reusing the unchanged five exact key/hash regexes, generic-api-key rule and AND condition; no new hash, rule, broad path or future receipt exemption)
Shared resources (follow the owner protocol): RES-architecture-tests (append): Each repository policy task owns its suite; rule additions are append-only.; RES-web-build-config (append): Solution/project lists, central package versions and CI job lists are appended by the task that adds a project, dependency or job; dependency additions follow the dependency-admission policy with a reviewed receipt; lock files are regenerated after rebase and never hand-merged; the integration owner resolves ordering conflicts at merge.
Unblocks: GOV.15, WEB.01

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Node/npm-based static import-rule checks, offline, PR CI; no browser/E2E runtime here - that is WP-06.05/WP-50.06, per P2-017.
Completion evidence for the ledger: Per-rule pass/fail fixture table for the Web import/dependency graph.
Notes: Owns the unlabeled 'Web repository and architecture assertions' package obligation from WP05 (no WP-05.MM anchor); see package_obligations. Mechanism is necessarily separate code from GOV.04's.NET engine. The r7 public-digest support requires independently verifying all eight observed key/hash rows against r6 and their public inputs; six distinct digest values and all existing narrow matching conditions remain unchanged. This is explicit security-exception scope, not ADP.07 metadata support. A previously pushed exception change is not retroactive approval: preserve that history and require this authority, independent exact-head review and retained CI before merging the product PR.
```

```text
Execute ArcForges delivery task GOV.12 — Mobile policy tests (Gradle/Kotlin mechanism).

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\governance.md (anchor task-gov-12).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Mobile (integration owner: Mobile integration owner, the holder of roles/integration-mobile).
Claim and handoff record: claims/gov-12 (python tools/delivery.py claim GOV.12 --worker <name>); task branch task/gov-12 in Mobile; ledger record ledger/tasks/gov-12.md.
Kind/size: governance/M. Baseline: not-started.
Outcome: DesktopPlatform owns and publishes a portable, schema-versioned catalog of the seven canonical BAN-* categories with the BannedSymbolScanner that consumes and validates it. Mobile enforces its own layering/licence/naming/banned-API rules independently via a Gradle-native mechanism (dependency verification plus lint/Detekt-style rules), pinning and copying the exact packaged catalog with version, source commit and SHA plus parity tests; it consumes the same data, not GOV.04's .NET test library. The catalog contains no repository-specific paths or status.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-05.00 (Mobile slice, via Gradle dependency-graph verification rather than the.NET engine): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\05-architecture-and-repository-policy-tests.md, anchor rule-wp-05.00
- WP-05.01 (Mobile slice: licence boundary + dependency allowlist over Gradle dependencies): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\05-architecture-and-repository-policy-tests.md, anchor rule-wp-05.01
- WP-05.02 (wire the forbidden-term scanner into Mobile's own PR build): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\05-architecture-and-repository-policy-tests.md, anchor rule-wp-05.02
- WP-05.04 (Mobile banned-API fixtures): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\05-architecture-and-repository-policy-tests.md, anchor rule-wp-05.04

Entry condition: adoption slice ADOPT.10.governance is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] GOV.03: pinned JDK 21/Kotlin/Compose/AGP toolchain (GOV.03)
- [artifact] GOV.04: the rule DATA (forbidden-term list, licence-boundary declarations, banned-API categories) as portable JSON, not the.NET engine itself
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Mobile:gradle/policy/**; Mobile:eng/policy/exceptions.json; Mobile:build.gradle.kts (apply owned Gradle-native policy and formatter target only); DesktopPlatform:src/Build/ArcForges.Build.Policy/Architecture/banned-api-categories.json; DesktopPlatform:src/Build/ArcForges.Build.Policy/ArcForges.Build.Policy.csproj; DesktopPlatform:src/Build/ArcForges.Build.Policy/Architecture/BannedSymbolScanner.cs; DesktopPlatform:tests/ArchitectureTests/SharedPolicyTests.cs; DesktopPlatform:eng/provenance/files.json; DesktopPlatform:eng/packaging/packages.json (append only ArcForges.Build.Policy.requiredFiles entry tools/architecture/banned-api-categories.json; preserve package ID, project, kind, dependencies and version; no second package)
Shared resources (follow the owner protocol): RES-architecture-tests (append): Each repository policy task owns its suite; rule additions are append-only.; RES-mobile-build-config (append): The module skeleton task registers all modules once and holds the lease `leases/res-mobile-build-config` while it restructures the build; later tasks edit only their module; catalog entries are appended and locks regenerated after rebase; dependency additions carry admission receipts.; RES-desktopplatform-policy-data (append): Generated policy data is regenerated from its pinned source and never hand-edited; the reason-code registry is append-only with stable codes; each task adds its own test classes and evidence rows.; RES-desktopplatform-build-config (append): Solution/project lists, central package versions and CI job lists are appended by the task that adds a project, dependency or job; dependency additions follow the dependency-admission policy with a reviewed receipt; lock files are regenerated after rebase and never hand-merged; the integration owner resolves ordering conflicts at merge.; RES-desktopplatform-package-inventory (append): Each producer task adds its own package entry; every merge to main packs and publishes all packages at one version; consumers pin the candidate produced by the merge of the capability they need, never waiting for a package closure task; one merge queue.
Unblocks: GOV.15

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline Gradle-time checks, negative fixtures, PR CI; no device/emulator runtime here, per P2-017 (that is WP06.07/WP30/WP32).
Completion evidence for the ledger: Per-rule pass/fail fixture table for Mobile's Gradle dependency graph.
Notes: Deliver two exact-head PRs under the single GOV.12 claim: independently review, CI and merge the DesktopPlatform catalog/scanner producer first, publish its existing package identity, then pin that exact immutable candidate in Mobile and run its parity checks. Preserve provenance and package/source digests across the handoff. No second catalog authority or per-repository path/status fields. F-023 (mobile provenance) and VG-07 (Android runtime posture) are separately scheduled at WP06.07/WP30/WP32 and are not this task's concern.
```

```text
Execute ArcForges delivery task GOV.13 — Invariant enforcement accounting report.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\governance.md (anchor task-gov-13).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/gov-13 (python tools/delivery.py claim GOV.13 --worker <name>); task branch task/gov-13 in DesktopPlatform; ledger record ledger/tasks/gov-13.md.
Kind/size: governance/M. Baseline: not-started.
Outcome: A build-produced report emits each current catalog ID exactly once and classifies each invariant as enforced-and-passing, enforced-and-failing or not-yet-implemented. Only enforced-* classifications derive from actual registered test outcomes; not-yet-implemented requires a complete catalog and owner-registration scan confirming zero registered cases, never a missing or skipped run. Do not re-derive the design-stage mapping (PG-06, already closed) or close PG-11.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-05.05 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\05-architecture-and-repository-policy-tests.md, anchor rule-wp-05.05

Entry condition: adoption slice ADOPT.02.governance is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] GOV.04: at least one owning package's real policy-test run to classify (DesktopPlatform's own AT-*/RP-* results)
- [artifact] GOV.18: the invariant export regenerated from this Design repository
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:eng/accounting/invariant-test-cases.json; DesktopPlatform:eng/accounting/**; DesktopPlatform:.github/workflows/package-validation.yml; DesktopPlatform:eng/provenance/files.json
Shared resources (follow the owner protocol): RES-desktopplatform-policy-data (append): Generated policy data is regenerated from its pinned source and never hand-edited; the reason-code registry is append-only with stable codes; each task adds its own test classes and evidence rows.; RES-desktopplatform-build-config (append): Solution/project lists, central package versions and CI job lists are appended by the task that adds a project, dependency or job; dependency additions follow the dependency-admission policy with a reviewed receipt; lock files are regenerated after rebase and never hand-merged; the integration owner resolves ordering conflicts at merge.
Unblocks: GOV.15

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Define and test a normalized cross-owner result-input schema under eng/accounting/** with invariant ID, stable case ID, outcome, repository, source commit, CI run and attempt. The durable invariant-test-cases.json roster declares expected case IDs; DesktopPlatform CI converts all six unique TRX files to the schema, and future owner receipts use the same contract. A mapped test failure is failing and all accepted registered case outcomes passed is passing. Not-yet-implemented is allowed only when a complete catalog and owner-registration scan proves the expected-case roster has zero cases for that invariant. Missing declared result set or expected case; skipped/inconclusive result; malformed or incomplete TRX; duplicate/unknown IDs; or source/repository/run/attempt provenance mismatch fails closed. Reruns consume accepted owner run receipts; never claim another repository implemented an invariant without its receipt. Offline checks and PR CI; repeat as owners land enforcement, per P2-017.
Completion evidence for the ledger: Current-catalogue-complete accounting report and six normalized CI result inputs, uploaded with TRX as generated ignored artifacts; the ledger receipt records source SHA, run identity, artifact URL and digest.
Notes: Will read as mostly 'not yet implemented' immediately after WP05 since most current invariants are owned by packages far downstream (WP06...WP53, per invariant-coverage.md's ownerCell). PG-11 stays open per-invariant in its OWNING package; GOV.13 never closes PG-11 or PG-06 itself - it only reports. `artifacts/evidence/test-results/**` and `artifacts/evidence/invariant-accounting.json` are generated ignored CI artifacts, uploaded together and never checked in. Future owners append stable invariant-to-case registrations in the normalized input schema; each report rerun consumes accepted owner run receipts, bound to the exact source SHA, CI run and attempt, and never claims another repository's coverage without that evidence.
```

```text
Execute ArcForges delivery task GOV.14 — Specification integrity checks over the Design repository.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\governance.md (anchor task-gov-14).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/gov-14 (python tools/delivery.py claim GOV.14 --worker <name>); task branch task/gov-14 in DesktopPlatform; ledger record ledger/tasks/gov-14.md.
Kind/size: governance/M. Baseline: not-started.
Outcome: Checks run against the current Design repository and produce zero findings: every internal link resolves; every cited requirement/architecture rule/decision/verification finding/gate identifier exists; no superseded name appears as current outside docs/deprecated-inputs/; every Phase 1 decision is cited by at least one Phase 2 document or its non-applicability is stated; the delivery graph has satisfiable prerequisites, current generated views and complete obligation coverage; and the decision-coverage check passes.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-05.06 (full: six checks over docs/ in ArcForges-Design, plus semantic coverage of the 22 retained Phase 1 rows, seven retained initial Phase 2 rows and twelve current closure groups; trace retired decisions through P2-019 without recreating removed obligations): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\05-architecture-and-repository-policy-tests.md, anchor rule-wp-05.06

Entry condition: adoption slice ADOPT.02.governance is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] GOV.01: the citation/anchor index and continuing drift check installed by GOV.01 (PG-21)
- [artifact] GOV.18: the design-policy export re-pinned to this Design repository
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:eng/design_policy.py; DesktopPlatform:eng/design_corpus.py; DesktopPlatform:eng/design_graph.py; DesktopPlatform:eng/test_design_policy.py; Contracts:eng/policy/product-names.json (GOV.14 supporting producer data only: update design.commit and the sole DesktopPlatform eng/policy/glossary-terms.json derivedDeclaration.designCommit from 7aa84e69ad6808461b34181de261fab03bede076 to ec1a1e7400683a6f971693cf84c8480183b4b6c5; retain sourceSha256 9041df86987324c25446dc3a5cfbfbabd6b6df1ea20381135a8caf84f98e44d4 and declarationSha256 bdbdfcdc7e77fec492890159747cfffe4996181090af8818322064ae897ee023 unchanged; no other policy or scanner change); DesktopPlatform:eng/policy/naming-package.json (strictly pin the normally published immutable Contracts naming-tool candidate carrying this exact GOV.14 source-identity registration; retain package identity and exact content/source proof); DesktopPlatform:eng/policy/dependency-policy.json (current input binding and admission of that exact existing naming-tool candidate only; no unrelated dependency change); DesktopPlatform:eng/policy/dependency-reviews/gov-14-naming-r4.json (new immutable successor for that exact naming-tool candidate; preserve all prior receipts)
Shared resources (follow the owner protocol): RES-desktopplatform-policy-data (append): Generated policy data is regenerated from its pinned source and never hand-edited; the reason-code registry is append-only with stable codes; each task adds its own test classes and evidence rows.
Unblocks: GOV.15

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline documentation-only checks against a pinned, clean Design commit fetched in isolation (no Design program or repository hook is run); zero findings required; PR CI.
Completion evidence for the ledger: Zero-findings report across all six checks plus the decision-coverage check.
Notes: Extends the corpus and decision-coverage checks after GOV.18 has migrated the retired graph validator and re-pinned the export. Reuse that migration evidence; this broader integrity task is not a prerequisite for the initial repin. Current coverage follows the effective reduced-family authority: 22 of the original 23 Phase 1 decisions, seven of the initial eight Phase 2 decisions and twelve current closure groups. Historical acceptance totals remain historical, later amendment records remain traceable, and retirement is accounted through P2-019. Test semantic row identity, successor and producer/consumer mappings, not count equality alone. The actual GOV.14 Design export remains pinned to ec1a1e7400683a6f971693cf84c8480183b4b6c5; this supporting scope change does not chase later Design commits. The existing 1.0.0-ci.129.1 naming candidate registers the old source identity and therefore cannot validate that export, even though the glossary source and declaration bytes are unchanged. Under the real GOV.14 claim, contribute the exact Contracts registration data change through its integration owner, independent review, retained CI and normal immutable package publication, then consume that same produced candidate in DesktopPlatform. Do not reopen completed CON.23, copy sibling sources, republish old versions, weaken exact registration, broaden exceptions or modify naming/scanner algorithms. The Contracts producer change needs only those two policy fields: existing package staging copies and verifies the policy bytes, and no access/dependency/provenance input binding changes are required. The explicit DesktopPlatform candidate upgrade is not inferred from ADP.07.
```

```text
Execute ArcForges delivery task GOV.15 — WP05 stage integration verification.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\governance.md (anchor task-gov-15).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/gov-15 (python tools/delivery.py claim GOV.15 --worker <name>); task branch task/gov-15 in DesktopPlatform; ledger record ledger/tasks/gov-15.md.
Kind/size: integration/M. Baseline: not-started.
Outcome: Each of the seven implementation repositories enforces its own boundary independently, and a cross-repository integration graph - reading each repository's published package/dependency metadata rather than cloning every reference or product repository - detects a forbidden transitive edge; both the architecture/repository-policy suite and the specification-integrity suite run in the pull-request pipeline and a violation fails the build.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-05.90 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\05-architecture-and-repository-policy-tests.md, anchor rule-wp-05.90

Entry condition: adoption slice ADOPT.02.governance is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] GOV.04: DesktopPlatform's own policy suite green
- [artifact] GOV.05: Contracts' own policy suite green
- [artifact] GOV.07: ArcScope's own policy suite green
- [artifact] GOV.09: Cloud's own policy suite green
- [artifact] GOV.10: AI's own policy suite green
- [artifact] GOV.11: Web's own policy suite green
- [artifact] GOV.12: Mobile's own policy suite green
- [artifact] GOV.13: the invariant accounting report existing and complete
- [artifact] GOV.14: the specification-integrity suite green
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:eng/**; Design:docs/assurance/wp05-90-*.md, wp05-stage-acceptance.md/.json
Shared resources (follow the owner protocol): RES-design-evidence (append): Receipts and gate records are separate files per task or gate; indexes are appended; historical records are not rewritten.

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Reads published package manifests only (no full clone of every repository); offline; PR CI.
Completion evidence for the ledger: Stage-acceptance receipt joining all eleven preceding GOV.04-14 substeps' real results.
Notes: Terminal task for WP05. WP06 and WP21 depend on this as their own external artifact prerequisite (README downstream index: 05 -> 06, 21).
```

```text
Execute ArcForges delivery task GOV.16 — Operation-catalogue authorization reachability matrix and identity boundary evidence.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\governance.md (anchor task-gov-16).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Contracts (integration owner: Contracts integration owner, the holder of roles/integration-contracts).
Claim and handoff record: claims/gov-16 (python tools/delivery.py claim GOV.16 --worker <name>); task branch task/gov-16 in Contracts; ledger record ledger/tasks/gov-16.md.
Kind/size: governance/M. Baseline: not-started.
Outcome: A build-produced reachability matrix classifies every public/local/operator/CF/exception operation binding under catalogue 00 against all seven AZ-04 authorization fields, failing on unclassified/ambiguous fields, impossible idempotency claims, public imports of local schema, and tool reachability of human-only approval/credential/commerce/policy methods, including hostile actor-chain fixtures; separately, the owner/deployment identity chain is asserted so automation loses authorization when its owner loses permission/service eligibility even with an otherwise-valid process credential, and no customer service-principal or Organization authority is introduced.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-05:section-7-operation-by-actor-az-04-autho Section 7 operation-by-actor AZ-04 authorization reachability matrix (public/local/operator/CF/exception bindings, hostile actor-chain fixtures, resource/context/connector egress denials) and section 8 'Identity boundary evidence' (owner/deployment identity chain; automation loses authorization when its owner loses eligibility) - both unlabeled, no WP-05.MM anchor (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\05-architecture-and-repository-policy-tests.md, package-level obligation

Entry condition: adoption slice ADOPT.03.governance is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [contract] CON.18: generated catalogue 00 (operation-catalogue.md) AZ-04 authorization-field descriptors
Completion prerequisites (may start earlier; cannot complete before these are complete):
- [integration] CLOUD.11: identity/workspace/device/session bindings
- [integration] PLT.38: the owner/deployment identity chain mechanism (the platform lane security foundation)

Permitted write scope: Contracts:tests/AuthorizationPolicyTests/**

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Static/offline policy tests over each repository's DECLARED authorization metadata (generated attributes/descriptors), not live-system penetration testing, per P2-017.
Completion evidence for the ledger: Reachability matrix with all seven AZ-04 fields classified per binding, plus identity-boundary assertion results.
Notes: Covers two WP05 package-level obligations that carry no WP-05.MM anchor (the section 7 paragraph before the evidence table, and the section 8 'Identity boundary evidence' paragraph); see package_obligations. Genuinely cross-repository in subject matter (Contracts defines the catalogue; Cloud/DesktopPlatform implement the actual bindings) but modeled as a Contracts-owned static check over declared metadata, consistent with P2-017.
```

```text
Execute ArcForges delivery task GOV.17 — Retire the native families outside the product family and move the still-image shim.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\governance.md (anchor task-gov-17).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/gov-17 (python tools/delivery.py claim GOV.17 --worker <name>); task branch task/gov-17 in DesktopPlatform; ledger record ledger/tasks/gov-17.md.
Kind/size: governance/M. Baseline: not-started.
Outcome: The Media, Colour and Otio native families and the macOS Metal graphics probe leave DesktopPlatform - ABI directories, overlays, managed and runtime projects, oracle tests, solution entries and package registrations - and no further versions of them are published; the still-image shim moves to native/arcimage-abi under the logical library ArcImageNative while its published arc_image_* symbols stay unchanged; provenance records of reused files stay unchanged. Packaging guards, local opt-in consumer fixtures and examples use retained producers, preserving applicable integrity and RID checks.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- P2-019 (retirement of the accepted DesktopPlatform native families, projects, packages and tests whose only consumers left the family; the neutral identity of the still-image shim): C:\MyFile\Projects\ArcForges-Design\docs\decisions\phase-2-specification-decisions.md, anchor rule-p2-019
- P2-020 (source cleanup of the alignment sequence (ADP-10); blocks only the tasks that edit the retired bindings): C:\MyFile\Projects\ArcForges-Design\docs\decisions\phase-2-specification-decisions.md, anchor rule-p2-020

Entry condition: adoption slice ADOPT.02.governance is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- none
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:native/* (retired family directories and the moved still-image directory); DesktopPlatform:native/CMakeLists.txt; DesktopPlatform:src/Native/* (retired family projects and the still-image logical library name); DesktopPlatform:tests/NativeAbiTests/**; DesktopPlatform:win.slnx; DesktopPlatform:DesktopPlatform.slnx (retired native project entries only); DesktopPlatform:eng/packaging/packages.json; DesktopPlatform:docs/native-reconciliation.md; DesktopPlatform:README.md; DesktopPlatform:docs/native-package-release.md; DesktopPlatform:src/BuildingBlocks/ArcForges.NativeInterop/README.md; DesktopPlatform:tests/ArchitectureTests/** (retired native library map); DesktopPlatform:eng/packaging/test_packages.py; DesktopPlatform:eng/packaging/native_consumer.py; DesktopPlatform:eng/packaging/README.md; DesktopPlatform:.github/workflows/native-abi.yml (retired owned-family build inputs only; retain dependencies of retained image/PDF/instrument families); DesktopPlatform:CMakePresets.json (retired build targets only); DesktopPlatform:deploy/README.md (current retained-family build/install inventory); DesktopPlatform:eng/packaging/native.py; DesktopPlatform:eng/native/vcpkg/ports/opentimelineio/** (retired overlay only); DesktopPlatform:eng/native_provenance.py; DesktopPlatform:tests/tooling/test_native_provenance.py; DesktopPlatform:eng/provenance/files.json; DesktopPlatform:eng/provenance/NOTICE.txt; DesktopPlatform:eng/provenance/artifact-profiles/native-win-x64-r4.json (new immutable successor); DesktopPlatform:eng/provenance/records/native-*-r4.json (new immutable successors; preserve historical records); DesktopPlatform:eng/check_provenance.py (validate explicit retirement of previously registered artifact targets only); DesktopPlatform:tests/tooling/test_provenance.py (retirement rejection fixtures); DesktopPlatform:eng/provenance/retired-artifacts.json (exact former project/package/kind targets with retirement authority; reject active or unregistered targets); DesktopPlatform:eng/provenance/records/contracts-provenance-tools-r2.json (new immutable tool successor; preserve previous record); DesktopPlatform:CMakeLists.txt (reject retired native build profiles); DesktopPlatform:docs/provenance.md (current retained native profile inventory; preserve historical evidence)
Shared resources (follow the owner protocol): RES-desktopplatform-package-inventory (append): Each producer task adds its own package entry; every merge to main packs and publishes all packages at one version; consumers pin the candidate produced by the merge of the capability they need, never waiting for a package closure task; one merge queue.; RES-desktopplatform-native-build (append): The vcpkg baseline and overlay ports change only through a dependency-admission change with licence and provenance receipts; each native family adds its own CMake targets and workflow entries; triplet or port changes are rebased and rebuilt by their author; CPU-heavy native builds use the workstation build slot. PLT.39 may append only a narrowly scoped transport compatibility change to eng/native_provenance.py and offline tests in tests/tooling/test_native_provenance.py: after the verified cache-hit path, pass urllib.request.Request(url, headers={"User-Agent": "ArcForges/1.0 (+https://github.com/ArcForges/DesktopPlatform)"}) only when the complete requested URL equals https://visualstudio.microsoft.com/wp-content/uploads/2025/10/Visual_Studio_2026-License-Community_ENU.docx or https://visualstudio.microsoft.com/wp-content/uploads/2025/10/Visual-C-V14-License-Redistributable_and_Runtime_ENU.docx; preserve all other URL behavior, pinned URLs/hashes, TLS, timeout, redirects, cache, digest verification, temporary cleanup and atomic promotion, with no retries, dependency, workflow or runner changes. The DesktopPlatform integration owner serializes this shared helper append.; RES-desktopplatform-build-config (append): Solution/project lists, central package versions and CI job lists are appended by the task that adds a project, dependency or job; dependency additions follow the dependency-admission policy with a reviewed receipt; lock files are regenerated after rebase and never hand-merged; the integration owner resolves ordering conflicts at merge.; RES-workstation-build-slot (exclusive): Exclusive per workstation for the duration of each CPU-heavy local build or test, through the workstation lock rather than a Plan lease: run the command as `python tools/delivery.py build-slot run --worker <name> --task <task> -- <command>` with the Plan repository tool, which holds the lock directory `.arcforges/build-slot` in the user profile with an owner record and heartbeat and recovers a lock whose holder stopped. Coding and review continue while a build waits; CI capacity is not limited by this rule.; RES-architecture-tests (append): Each repository policy task owns its suite; rule additions are append-only.
Unblocks: NAT.06, NAT.11, NAT.13, NAT.14, NAT.30

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): offline: native CMake/solution/package-inventory consistency, retained packaging guard tests and a scan for active retired-family bindings outside provenance history. Retain necessary Windows native compilation and packaging checks; run affected consumer behavior locally only when the existing environment supports it and the change requires it (P2-017), never as CI. Acceptance: source, solution, packaging, tests and current documentation contain only retained families, guards no longer select Media packages, and still-image consumers resolve ArcImageNative.
Completion evidence for the ledger: Retirement diff; native build and package-consumer results for the retained families; the moved still-image shim with unchanged exported symbols.
Notes: Independent of the retained native families; NAT.11 starts on the moved still-image directory and NAT.30 verifies the retained producer set. GOV.18 carries the policy-data half, so neither waits on the other.
```

```text
Execute ArcForges delivery task GOV.18 — Reduce the DesktopPlatform policy data and re-pin the design-policy export.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\governance.md (anchor task-gov-18).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/gov-18 (python tools/delivery.py claim GOV.18 --worker <name>); task branch task/gov-18 in DesktopPlatform; ledger record ledger/tasks/gov-18.md.
Kind/size: governance/M. Baseline: not-started.
Outcome: Runtime-ownership, licence-boundary and reconciliation policy data drop the retired repositories and families. In the same reviewed change, the retired serial-graph validator and exporter migrate to the delivery graph, including graph-derived active invariant owners, before the design-policy export is re-pinned to this Design repository and glossary-terms.json and invariants.json are regenerated. Provenance records of reused files stay unchanged.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- P2-019 (retirement of the accepted DesktopPlatform policy data that names repositories or families outside the family; the design-policy export re-pinned to this Design repository): C:\MyFile\Projects\ArcForges-Design\docs\decisions\phase-2-specification-decisions.md, anchor rule-p2-019
- P2-020 (source cleanup of the alignment sequence (ADP-10); blocks only the tasks that edit the retired bindings): C:\MyFile\Projects\ArcForges-Design\docs\decisions\phase-2-specification-decisions.md, anchor rule-p2-020
- P2-018 (delivery-graph validation replacing the retired package-level graph check): C:\MyFile\Projects\ArcForges-Design\docs\decisions\phase-2-specification-decisions.md, anchor rule-p2-018

Entry condition: adoption slice ADOPT.02.governance is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] CON.23: Published canonical naming data/scanner build-time candidate
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:eng/policy/**; DesktopPlatform:docs/design-policy.md; DesktopPlatform:eng/runtime_ownership.py; DesktopPlatform:eng/licence_boundary.py; DesktopPlatform:eng/reference_baselines.py; DesktopPlatform:eng/reconciliation.py; DesktopPlatform:eng/test_runtime_ownership.py; DesktopPlatform:eng/test_licence_boundary.py; DesktopPlatform:eng/test_design_policy.py; DesktopPlatform:tests/ArchitectureTests/** (retired repository owners); DesktopPlatform:eng/design_graph.py; DesktopPlatform:eng/design_policy.py; DesktopPlatform:eng/provenance/** (new same-owner tool reuse receipt and source inventory only; existing reused-file provenance remains unchanged); DesktopPlatform:NOTICE.md (generated provenance notice only); DesktopPlatform:eng/test_reference_baselines.py; DesktopPlatform:eng/test_reconciliation.py; DesktopPlatform:AGENTS.md; DesktopPlatform:docs/runtime-ownership.md; DesktopPlatform:docs/licence-boundary.md; DesktopPlatform:docs/reference-baselines.md; DesktopPlatform:docs/reconciliation-inventory.md; DesktopPlatform:Directory.Packages.props (exact canonical naming-tool package pin); DesktopPlatform:eng/policy/dependency-policy.json (canonical naming-tool admission); DesktopPlatform:eng/policy/dependency-reviews/** (new immutable naming-tool admission receipt); DesktopPlatform:eng/provenance/** (owned naming-tool inventory and new receipts; preserve historical records)
Shared resources (follow the owner protocol): RES-desktopplatform-policy-data (append): Generated policy data is regenerated from its pinned source and never hand-edited; the reason-code registry is append-only with stable codes; each task adds its own test classes and evidence rows.; RES-architecture-tests (append): Each repository policy task owns its suite; rule additions are append-only.; RES-desktopplatform-build-config (append): Solution/project lists, central package versions and CI job lists are appended by the task that adds a project, dependency or job; dependency additions follow the dependency-admission policy with a reviewed receipt; lock files are regenerated after rebase and never hand-merged; the integration owner resolves ordering conflicts at merge.
Unblocks: CON.23, GOV.04, GOV.13, GOV.14

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): offline: delivery-graph and exporter tests, including invalid prerequisite/obligation/active-owner rejection fixtures; architecture and runtime-ownership tests; fresh exporter comparison against the reviewed repinned Design commit; no live retired bindings outside provenance. Acceptance: the graph-validator migration and repin pass together without waiting for GOV.14, policy tools name only the retained repositories and references, and the design-policy check passes against the new pin.
Completion evidence for the ledger: Reviewed graph-validator/exporter migration and negative-fixture results; repinned Design commit and policy-source identities; exporter comparison and policy-test results.
Notes: Performs the narrow checker migration needed to repin within this cleanup task. GOV.13 and GOV.14 consume the resulting export; GOV.14 retains the broader specification-integrity audit. CON.23 completes after its forbidden-alias declaration is re-exported.
```
