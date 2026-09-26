# ArcForges delivery task prompts — Family governance and policy tests

Generated from Design `docs/planning/delivery/delivery-graph.json` by `tools/delivery.py`; do not edit by hand.
Each block is self-contained. Claim a task only when `python tools/delivery.py ready` lists it, with
`python tools/delivery.py claim <TASK-ID> --worker <name>`, then follow `arcforges-implementation.md`.
Tasks are ordered by lane for reading; the order is not a schedule.

## Family governance and policy tests

```text
Execute ArcForges delivery task GOV.01 — Specification, naming, licence-boundary and provenance freeze (WP00, accepted).

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\governance.md (anchor task-gov-01).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/gov-01 (python tools/delivery.py claim GOV.01 --worker <name>); task branch task/gov-01 in DesktopPlatform; ledger record ledger/tasks/gov-01.md.
Kind/size: governance/XL. Baseline: accepted.
Outcome: WP00's naming/licence/provenance freeze is accepted across all nine implementation repositories: product-names.json, exported glossary/invariant policy data, per-project SPDX licence boundaries, a working provenance process and five registered Reference Coverage Matrices are in place, scanned clean, and enforced in CI.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-00.00 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\00-specification-naming-and-rights-freeze.md, anchor rule-wp-00.00
- WP-00.01 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\00-specification-naming-and-rights-freeze.md, anchor rule-wp-00.01
- WP-00.02 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\00-specification-naming-and-rights-freeze.md, anchor rule-wp-00.02
- WP-00.03 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\00-specification-naming-and-rights-freeze.md, anchor rule-wp-00.03
- WP-00.04 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\00-specification-naming-and-rights-freeze.md, anchor rule-wp-00.04
- WP-00.05 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\00-specification-naming-and-rights-freeze.md, anchor rule-wp-00.05
- WP-00.90 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\00-specification-naming-and-rights-freeze.md, anchor rule-wp-00.90

Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- none
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Contracts:eng/policy/product-names.json; DesktopPlatform:eng/policy/glossary-terms.json; DesktopPlatform:eng/policy/invariants.json; DesktopPlatform:eng/policy/reference-baselines.json; *:NOTICE.md; *:LICENSE; *:Directory.Build.props
Shared resources (follow the owner protocol): RES-desktopplatform-policy-data (append): Generated policy data is regenerated from its pinned source and never hand-edited; the reason-code registry is append-only with stable codes; each task adds its own test classes and evidence rows.
Unblocks: GOV.02, GOV.04, GOV.11, GOV.14

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Design-repo-pinned exporter (DesktopPlatform/eng/design_policy.py) verified against an immutable, clean pinned Design commit; nine-repository offline forbidden-term scanner in Contracts CI; no macOS/device/live-service runtime, per P2-017.
Completion evidence for the ledger: docs/assurance/wp00-03-implementation-evidence.md, wp00-04-implementation-evidence.md, wp00-05-implementation-evidence.md, wp00-stage-acceptance.md, wp00-stage-acceptance.json (file names only, via ls; bodies not read per assignment).
Notes: Executed across all nine implementation repositories plus Contracts' product-names.json; represented as one accepted task for the whole closed package rather than one task per substep, per the assignment's 'small number of GOV tasks' instruction.
```

```text
Execute ArcForges delivery task GOV.02 — Repository reconciliation and target layout (WP01, accepted).

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\governance.md (anchor task-gov-02).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/gov-02 (python tools/delivery.py claim GOV.02 --worker <name>); task branch task/gov-02 in DesktopPlatform; ledger record ledger/tasks/gov-02.md.
Kind/size: governance/XL. Baseline: accepted.
Outcome: WP01 reconciliation is accepted: nine-repository disposition inventory executed against ede43db, the Contracts public/internal Apache-2.0 split assigned, the shared-foundation boundary reviewed, native surface dispositions executed (OTIO admitted, MDF excluded), all eighteen test families mapped, bounded reconciliation applied with a green Notes build, and Cloud's 21 domain owners recorded.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-01.00 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\01-repository-reconciliation-and-target-layout.md, anchor rule-wp-01.00
- WP-01.01 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\01-repository-reconciliation-and-target-layout.md, anchor rule-wp-01.01
- WP-01.02 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\01-repository-reconciliation-and-target-layout.md, anchor rule-wp-01.02
- WP-01.03 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\01-repository-reconciliation-and-target-layout.md, anchor rule-wp-01.03
- WP-01.04 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\01-repository-reconciliation-and-target-layout.md, anchor rule-wp-01.04
- WP-01.05 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\01-repository-reconciliation-and-target-layout.md, anchor rule-wp-01.05
- WP-01.90 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\01-repository-reconciliation-and-target-layout.md, anchor rule-wp-01.90
- WP-01:cloud-module-layout-acceptance-map-17-hi Cloud module layout acceptance - map 17 historical scaffold names to the 21 declared domain owners in WP21; Cloud owns the Native AOT Container host and Worker bindings, AI owns the sole Workflow Harness; empty module projects are not created during reconciliation (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\01-repository-reconciliation-and-target-layout.md, package-level obligation

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

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\governance.md (anchor task-gov-03).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/gov-03 (python tools/delivery.py claim GOV.03 --worker <name>); task branch task/gov-03 in DesktopPlatform; ledger record ledger/tasks/gov-03.md.
Kind/size: governance/XL. Baseline: accepted.
Outcome: WP02 build governance is accepted: pinned/locked toolchains in all nine owners, warnings-as-errors with an empty authored-code waiver list, a complete AOT/trim declaration sweep with zero unassigned diagnostics, verified runtime/directory boundaries, all nine version axes producible, and dependency-admission policy encoded as data.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-02.00 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\02-build-governance-and-analyzer-policy.md, anchor rule-wp-02.00
- WP-02.01 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\02-build-governance-and-analyzer-policy.md, anchor rule-wp-02.01
- WP-02.02 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\02-build-governance-and-analyzer-policy.md, anchor rule-wp-02.02
- WP-02.03 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\02-build-governance-and-analyzer-policy.md, anchor rule-wp-02.03
- WP-02.04 (full, under P2-017): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\02-build-governance-and-analyzer-policy.md, anchor rule-wp-02.04
- WP-02.05 (full, under P2-017): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\02-build-governance-and-analyzer-policy.md, anchor rule-wp-02.05
- WP-02.90 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\02-build-governance-and-analyzer-policy.md, anchor rule-wp-02.90

Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] GOV.02: WP01's settled project set and dispositions (GOV.02)
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: *:global.json; *:Directory.Build.props/.targets; *:Directory.Packages.props; *:packages.lock.json; DesktopPlatform:eng/build/desktop-aot.props; Cloud:eng/build/cloud-aot.props; Mobile:gradle/*; Web:package.json,package-lock.json,.node-version,.npmrc,ArcForges.Web.esproj; Contracts:eng/build/contracts.props; *:.editorconfig; DesktopPlatform:eng/policy/dependency-policy.json
Shared resources (follow the owner protocol): RES-desktopplatform-policy-data (append): Generated policy data is regenerated from its pinned source and never hand-edited; the reason-code registry is append-only with stable codes; each task adds its own test classes and evidence rows.
Unblocks: GOV.04, GOV.11, GOV.12, NOTES.21, REL.06, WEB.01, WEB.08

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Clean-machine locked restores, warnings-as-errors full-solution build, complete AOT/trim diagnostic sweep, per P2-017 reduced CI for 02.04/02.05 (no new macOS/device/download runtime).
Completion evidence for the ledger: docs/assurance/wp02-00-implementation-evidence.md/.json, wp02-00-toolchain-profile.md, wp02-01-diagnostic-profile.md, wp02-01-implementation-evidence.md/.json, wp02-02-aot-sweep-evidence.md/.json, wp02-03-runtime-boundary-evidence.md/.json, wp02-03-runtime-boundary-profile.md, wp02-04-implementation-evidence.md/.json, wp02-04-version-identity-profile.md, wp02-05-dependency-policy-profile.md, wp02-05-implementation-evidence.md/.json, wp02-stage-acceptance.md/.json (file names only, via ls; bodies not read).
Notes: VG-08 (framework upgrade re-verification) is explicitly recurring: WP02.05's evidence closes the first instance only; every future dependency/framework upgrade re-triggers VG-08 outside this task's own closure.
```

```text
Execute ArcForges delivery task GOV.04 — Shared architecture/repository policy-test engine and DesktopPlatform enforcement.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\governance.md (anchor task-gov-04).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/gov-04 (python tools/delivery.py claim GOV.04 --worker <name>); task branch task/gov-04 in DesktopPlatform; ledger record ledger/tasks/gov-04.md.
Kind/size: governance/L. Baseline: not-started.
Outcome: A reusable AT-01..14/RP-01..10 rule engine, project-graph reader, fixture compiler and banned-symbol scanner extend DesktopPlatform's existing 5-method RepositoryPolicyTests.cs baseline (WP01.04) to the full rule set, are published for the other eight repositories to reuse, and DesktopPlatform's own project graph is fully enforced with one positive and one failing negative fixture per rule.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-05.00 (build the reusable AT-01..14/RP-01..10 rule engine and project-graph reader; apply it to DesktopPlatform's own layering/reference-direction rules): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\05-architecture-and-repository-policy-tests.md, anchor rule-wp-05.00
- WP-05.01 (licence-boundary rule implementation in the shared engine; DesktopPlatform's own licence-boundary enforcement): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\05-architecture-and-repository-policy-tests.md, anchor rule-wp-05.01
- WP-05.04 (banned-symbol scanner mechanism in the shared engine; DesktopPlatform's own banned-API fixtures): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\05-architecture-and-repository-policy-tests.md, anchor rule-wp-05.04
- WP-05.02 (wire the existing WP00.00 forbidden-term scanner into DesktopPlatform's own PR build as a failing policy test): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\05-architecture-and-repository-policy-tests.md, anchor rule-wp-05.02

Entry condition: adoption slice ADOPT.02.governance is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] GOV.03: a build that fails on warnings/AOT diagnostics (GOV.03)
- [artifact] GOV.01: exported glossary-terms.json/invariants.json policy data (GOV.01)
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:tests/ArchitectureTests/**; DesktopPlatform:eng/policy/exceptions.json
Shared resources (follow the owner protocol): RES-architecture-tests (append): Each repository policy task owns its suite; rule additions are append-only.; RES-desktopplatform-policy-data (append): Generated policy data is regenerated from its pinned source and never hand-edited; the reason-code registry is append-only with stable codes; each task adds its own test classes and evidence rows.
Unblocks: GOV.05, GOV.06, GOV.07, GOV.08, GOV.09, GOV.10, GOV.12, GOV.13, GOV.15

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline unit/analyzer-style project-graph assertions, one positive and one failing negative fixture per rule, runs in PR CI; no macOS/device/live runtime per P2-017.
Completion evidence for the ledger: Full AT-01..14/RP-01..10 rule table with pass/fail fixture pairs; banned-symbol detection results per category (reflection on AOT paths, dynamic codegen, blocking waits on async paths, direct provider SDK calls outside adapters, secret/content logging, float money arithmetic, raw pointer fields).
Notes: This is the shared-tooling half of WP05's own binding statement: 'Repositories: Each repository; shared tooling in Platform/Contracts.'
```

```text
Execute ArcForges delivery task GOV.05 — Contracts policy tests and contract/serialization policy engine.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\governance.md (anchor task-gov-05).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Contracts (integration owner: Contracts integration owner, the holder of roles/integration-contracts).
Claim and handoff record: claims/gov-05 (python tools/delivery.py claim GOV.05 --worker <name>); task branch task/gov-05 in Contracts; ledger record ledger/tasks/gov-05.md.
Kind/size: governance/L. Baseline: not-started.
Outcome: Contracts enforces its own layering/licence/banned-API rules using GOV.04's shared engine, and implements the contract/serialization policy engine that makes VG-04's policy-test half enforceable and that GOV.06-GOV.12 reuse for their own generated-client checks.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-05.03 (full: build the contract/serialization policy engine (generated-from-proto DTO check, explicit JSON metadata for HTTP exceptions, no reflection-based serializer reachable, every local RPC contract interface carries the generated service/descriptor identity, generated artifacts match the committed baseline) and apply it to Contracts itself): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\05-architecture-and-repository-policy-tests.md, anchor rule-wp-05.03
- WP-05.00 (Contracts layering: contract projects reference only contract projects and the foundation): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\05-architecture-and-repository-policy-tests.md, anchor rule-wp-05.00
- WP-05.01 (Contracts licence-boundary enforcement (public/internal Apache-2.0 split from WP01.01)): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\05-architecture-and-repository-policy-tests.md, anchor rule-wp-05.01
- WP-05.02 (wire the forbidden-term scanner into Contracts' own PR build as a failing policy test): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\05-architecture-and-repository-policy-tests.md, anchor rule-wp-05.02
- WP-05.04 (Contracts banned-API fixtures): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\05-architecture-and-repository-policy-tests.md, anchor rule-wp-05.04

Entry condition: adoption slice ADOPT.03.governance is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] GOV.04: published shared AT-*/RP-* rule engine, fixture compiler and project-graph reader
- [contract] CON.90: Contracts' public/internal Apache-2.0 project split and generated proto baseline
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Contracts:tests/ArchitectureTests/**; Contracts:eng/policy/exceptions.json
Shared resources (follow the owner protocol): RES-architecture-tests (append): Each repository policy task owns its suite; rule additions are append-only.
Unblocks: GOV.06, GOV.07, GOV.08, GOV.09, GOV.10, GOV.15

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline unit tests, negative fixtures per assertion, PR CI; no live-service runtime per P2-017.
Completion evidence for the ledger: Contract/serialization policy results with negative fixtures per assertion; Contracts' own layering/licence/banned-API results.
Notes: WP05's own §8 completion-gate text states this substep 'makes VG-04's policy-test half enforceable' - a second VG-04 contributor not listed in the README's deferred-gate table (which names only 03.04/06.01).
```

```text
Execute ArcForges delivery task GOV.06 — ArcNotes policy tests.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\governance.md (anchor task-gov-06).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\ArcNotes (integration owner: ArcNotes integration owner, the holder of roles/integration-arcnotes).
Claim and handoff record: claims/gov-06 (python tools/delivery.py claim GOV.06 --worker <name>); task branch task/gov-06 in ArcNotes; ledger record ledger/tasks/gov-06.md.
Kind/size: governance/S. Baseline: not-started.
Outcome: ArcNotes enforces its own layering/licence/naming/banned-API/contract-consumption rules independently, using GOV.04's shared engine and GOV.05's contract-policy helpers, with positive and failing-negative fixtures for each rule.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-05.00 (ArcNotes slice: layering/reference-direction fixtures): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\05-architecture-and-repository-policy-tests.md, anchor rule-wp-05.00
- WP-05.01 (ArcNotes slice: licence boundary + dependency allowlist): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\05-architecture-and-repository-policy-tests.md, anchor rule-wp-05.01
- WP-05.02 (wire the forbidden-term scanner into ArcNotes' own PR build): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\05-architecture-and-repository-policy-tests.md, anchor rule-wp-05.02
- WP-05.03 (ArcNotes' generated-client consumption checks (RPC interface carries generated descriptor identity)): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\05-architecture-and-repository-policy-tests.md, anchor rule-wp-05.03
- WP-05.04 (ArcNotes banned-API fixtures): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\05-architecture-and-repository-policy-tests.md, anchor rule-wp-05.04

Entry condition: adoption slice ADOPT.04.governance is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] GOV.04: published shared rule engine
- [artifact] GOV.05: contract/serialization policy helpers for generated-client checks
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: ArcNotes:tests/ArchitectureTests/**; ArcNotes:eng/policy/exceptions.json
Shared resources (follow the owner protocol): RES-architecture-tests (append): Each repository policy task owns its suite; rule additions are append-only.
Unblocks: GOV.15

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline unit tests, negative fixtures, PR CI; per P2-017 no live/device runtime.
Completion evidence for the ledger: Per-rule pass/fail fixture table for ArcNotes' project graph.
Notes: Runs against whatever ArcNotes source exists at Phase-A execution time (largely bootstrap); WP05's own model is fixture-driven so this does not need ArcNotes' product work (WP18/19/28) to have landed first.
```

```text
Execute ArcForges delivery task GOV.07 — ArcScope policy tests.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\governance.md (anchor task-gov-07).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\ArcScope (integration owner: ArcScope integration owner, the holder of roles/integration-arcscope).
Claim and handoff record: claims/gov-07 (python tools/delivery.py claim GOV.07 --worker <name>); task branch task/gov-07 in ArcScope; ledger record ledger/tasks/gov-07.md.
Kind/size: governance/S. Baseline: not-started.
Outcome: ArcScope enforces its own layering/licence/naming/banned-API/contract-consumption rules independently.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-05.00 (ArcScope slice): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\05-architecture-and-repository-policy-tests.md, anchor rule-wp-05.00
- WP-05.01 (ArcScope slice): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\05-architecture-and-repository-policy-tests.md, anchor rule-wp-05.01
- WP-05.02 (wire the forbidden-term scanner into ArcScope's own PR build): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\05-architecture-and-repository-policy-tests.md, anchor rule-wp-05.02
- WP-05.03 (ArcScope's generated-client consumption checks): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\05-architecture-and-repository-policy-tests.md, anchor rule-wp-05.03
- WP-05.04 (ArcScope banned-API fixtures): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\05-architecture-and-repository-policy-tests.md, anchor rule-wp-05.04

Entry condition: adoption slice ADOPT.05.governance is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] GOV.04: published shared rule engine
- [artifact] GOV.05: contract/serialization policy helpers
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: ArcScope:tests/ArchitectureTests/**; ArcScope:eng/policy/exceptions.json
Shared resources (follow the owner protocol): RES-architecture-tests (append): Each repository policy task owns its suite; rule additions are append-only.
Unblocks: GOV.15

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline unit tests, negative fixtures, PR CI; per P2-017.
Completion evidence for the ledger: Per-rule pass/fail fixture table for ArcScope's project graph.
Notes: Fixture-driven; does not require ArcScope's own product work (WP33 to WP35) to have landed.
```

```text
Execute ArcForges delivery task GOV.08 — ArcSlate policy tests.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\governance.md (anchor task-gov-08).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\ArcSlate (integration owner: ArcSlate integration owner, the holder of roles/integration-arcslate).
Claim and handoff record: claims/gov-08 (python tools/delivery.py claim GOV.08 --worker <name>); task branch task/gov-08 in ArcSlate; ledger record ledger/tasks/gov-08.md.
Kind/size: governance/S. Baseline: not-started.
Outcome: ArcSlate enforces its own layering/licence/naming/banned-API/contract-consumption rules independently.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-05.00 (ArcSlate slice): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\05-architecture-and-repository-policy-tests.md, anchor rule-wp-05.00
- WP-05.01 (ArcSlate slice): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\05-architecture-and-repository-policy-tests.md, anchor rule-wp-05.01
- WP-05.02 (wire the forbidden-term scanner into ArcSlate's own PR build): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\05-architecture-and-repository-policy-tests.md, anchor rule-wp-05.02
- WP-05.03 (ArcSlate's generated-client consumption checks): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\05-architecture-and-repository-policy-tests.md, anchor rule-wp-05.03
- WP-05.04 (ArcSlate banned-API fixtures): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\05-architecture-and-repository-policy-tests.md, anchor rule-wp-05.04

Entry condition: adoption slice ADOPT.06.governance is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] GOV.04: published shared rule engine
- [artifact] GOV.05: contract/serialization policy helpers
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: ArcSlate:tests/ArchitectureTests/**; ArcSlate:eng/policy/exceptions.json
Shared resources (follow the owner protocol): RES-architecture-tests (append): Each repository policy task owns its suite; rule additions are append-only.
Unblocks: GOV.15

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline unit tests, negative fixtures, PR CI; per P2-017.
Completion evidence for the ledger: Per-rule pass/fail fixture table for ArcSlate's project graph.
Notes: Fixture-driven; does not require ArcSlate's own product work (WP36 to WP39) to have landed. Native admission rules (official OTIO, MDF exclusion) from WP01.03 are checkable here.
```

```text
Execute ArcForges delivery task GOV.09 — Cloud policy tests.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\governance.md (anchor task-gov-09).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/gov-09 (python tools/delivery.py claim GOV.09 --worker <name>); task branch task/gov-09 in Cloud; ledger record ledger/tasks/gov-09.md.
Kind/size: governance/M. Baseline: not-started.
Outcome: Cloud enforces its own layering/licence/naming/banned-API/contract-consumption rules independently, with extra weight on AOT-path banned APIs given BR-07's zero-trim/AOT-diagnostic requirement.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-05.00 (Cloud slice): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\05-architecture-and-repository-policy-tests.md, anchor rule-wp-05.00
- WP-05.01 (Cloud slice): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\05-architecture-and-repository-policy-tests.md, anchor rule-wp-05.01
- WP-05.02 (wire the forbidden-term scanner into Cloud's own PR build): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\05-architecture-and-repository-policy-tests.md, anchor rule-wp-05.02
- WP-05.03 (Cloud's own generated public API/RPC descriptor checks): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\05-architecture-and-repository-policy-tests.md, anchor rule-wp-05.03
- WP-05.04 (Cloud banned-API fixtures, weighted toward AOT-path reflection/dynamic-codegen since Cloud is the Native AOT host): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\05-architecture-and-repository-policy-tests.md, anchor rule-wp-05.04

Entry condition: adoption slice ADOPT.07.governance is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] GOV.04: published shared rule engine
- [artifact] GOV.05: contract/serialization policy helpers
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Cloud:tests/ArchitectureTests/**; Cloud:eng/policy/exceptions.json
Shared resources (follow the owner protocol): RES-architecture-tests (append): Each repository policy task owns its suite; rule additions are append-only.
Unblocks: GOV.15

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline unit tests, negative fixtures, PR CI; per P2-017 (Cloud's real AOT publish proof is WP06/WP21, not claimed here).
Completion evidence for the ledger: Per-rule pass/fail fixture table for Cloud's project graph.
Notes: Fixture-driven; does not require Cloud's own product work (WP21 to WP26) to have landed.
```

```text
Execute ArcForges delivery task GOV.10 — AI (Workflow Harness) policy tests.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\governance.md (anchor task-gov-10).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\AI (integration owner: AI integration owner, the holder of roles/integration-ai).
Claim and handoff record: claims/gov-10 (python tools/delivery.py claim GOV.10 --worker <name>); task branch task/gov-10 in AI; ledger record ledger/tasks/gov-10.md.
Kind/size: governance/S. Baseline: not-started.
Outcome: AI enforces its own layering/licence/naming/banned-API/contract-consumption rules independently as the sole owner of the Workflow Harness (per WP01's Cloud/AI module split).

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-05.00 (AI slice): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\05-architecture-and-repository-policy-tests.md, anchor rule-wp-05.00
- WP-05.01 (AI slice): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\05-architecture-and-repository-policy-tests.md, anchor rule-wp-05.01
- WP-05.02 (wire the forbidden-term scanner into AI's own PR build): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\05-architecture-and-repository-policy-tests.md, anchor rule-wp-05.02
- WP-05.03 (AI's generated-client consumption checks): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\05-architecture-and-repository-policy-tests.md, anchor rule-wp-05.03
- WP-05.04 (AI banned-API fixtures): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\05-architecture-and-repository-policy-tests.md, anchor rule-wp-05.04

Entry condition: adoption slice ADOPT.08.governance is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] GOV.04: published shared rule engine
- [artifact] GOV.05: contract/serialization policy helpers
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: AI:tests/ArchitectureTests/**; AI:eng/policy/exceptions.json
Shared resources (follow the owner protocol): RES-architecture-tests (append): Each repository policy task owns its suite; rule additions are append-only.
Unblocks: GOV.15

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline unit tests, negative fixtures, PR CI; per P2-017.
Completion evidence for the ledger: Per-rule pass/fail fixture table for AI's project graph.
Notes: Fixture-driven; does not require AI's own product work (WP40 to WP43, WP52) to have landed.
```

```text
Execute ArcForges delivery task GOV.11 — Web policy tests (Node/TS mechanism).

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\governance.md (anchor task-gov-11).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Web (integration owner: Web integration owner, the holder of roles/integration-web).
Claim and handoff record: claims/gov-11 (python tools/delivery.py claim GOV.11 --worker <name>); task branch task/gov-11 in Web; ledger record ledger/tasks/gov-11.md.
Kind/size: governance/M. Baseline: not-started.
Outcome: Node/TS import and dependency policy checks enforce one Web workspace/lock, exact Node/npm/generator pins, SDK-to-UI licence separation, generated wire types only, no private/server/local-RPC imports, desktop JS/DOM prohibition scoped to desktop graphs, no obsolete Blazor target in the active Web graph, no esproj in portable managed references, no implicit npm install or production dev/HMR server, and no TS fixtures/test helpers in the release route graph - each with a passing and a failing negative example.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-05.01 (Web slice: SDK-to-UI licence separation): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\05-architecture-and-repository-policy-tests.md, anchor rule-wp-05.01
- WP-05.02 (wire the forbidden-term scanner into Web's own PR build): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\05-architecture-and-repository-policy-tests.md, anchor rule-wp-05.02
- WP-05.04 (Web banned dependency/route fixtures): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\05-architecture-and-repository-policy-tests.md, anchor rule-wp-05.04
- WP-05:web-repository-and-architecture-assertio Web repository and architecture assertions (unlabeled paragraph after WP-05.06): Node/TS import and dependency checks - one Web workspace/lock, exact Node/npm/generator pins, SDK-to-UI licence separation, generated wire types only, no private/server/local-RPC imports, desktop JS/DOM prohibition scoped to desktop graphs, no obsolete Blazor target, no esproj in portable managed references, no implicit npm install or production dev/HMR server, no TS fixtures/test helpers in the release route graph (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\05-architecture-and-repository-policy-tests.md, package-level obligation

Entry condition: adoption slice ADOPT.09.governance is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] GOV.03: the one Node/npm workspace and Windows esproj adapter (GOV.03)
- [artifact] GOV.01: licence boundary declarations (mobile-only/public-SDK Apache set)
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Web:eng/policy/**; Web:.eslintrc*/lint-config for architecture rules
Shared resources (follow the owner protocol): RES-architecture-tests (append): Each repository policy task owns its suite; rule additions are append-only.
Unblocks: GOV.15

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Node/npm-based static import-rule checks, offline, PR CI; no browser/E2E runtime here - that is WP-06.05/WP-50.06, per P2-017.
Completion evidence for the ledger: Per-rule pass/fail fixture table for the Web import/dependency graph.
Notes: Owns the unlabeled 'Web repository and architecture assertions' package obligation from WP05 (no WP-05.MM anchor); see package_obligations. Mechanism is necessarily separate code from GOV.04's.NET engine.
```

```text
Execute ArcForges delivery task GOV.12 — Mobile policy tests (Gradle/Kotlin mechanism).

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\governance.md (anchor task-gov-12).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Mobile (integration owner: Mobile integration owner, the holder of roles/integration-mobile).
Claim and handoff record: claims/gov-12 (python tools/delivery.py claim GOV.12 --worker <name>); task branch task/gov-12 in Mobile; ledger record ledger/tasks/gov-12.md.
Kind/size: governance/M. Baseline: not-started.
Outcome: Mobile enforces its own layering/licence/naming/banned-API rules independently via a Gradle-native mechanism (dependency verification plus lint/Detekt-style rules) that consumes the same rule DATA as the other repos, not GOV.04's.NET test library directly.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-05.00 (Mobile slice, via Gradle dependency-graph verification rather than the.NET engine): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\05-architecture-and-repository-policy-tests.md, anchor rule-wp-05.00
- WP-05.01 (Mobile slice: licence boundary + dependency allowlist over Gradle dependencies): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\05-architecture-and-repository-policy-tests.md, anchor rule-wp-05.01
- WP-05.02 (wire the forbidden-term scanner into Mobile's own PR build): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\05-architecture-and-repository-policy-tests.md, anchor rule-wp-05.02
- WP-05.04 (Mobile banned-API fixtures): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\05-architecture-and-repository-policy-tests.md, anchor rule-wp-05.04

Entry condition: adoption slice ADOPT.10.governance is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] GOV.03: pinned JDK 21/Kotlin/Compose/AGP toolchain (GOV.03)
- [artifact] GOV.04: the rule DATA (forbidden-term list, licence-boundary declarations, banned-API categories) as portable JSON, not the.NET engine itself
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Mobile:gradle/policy/**; Mobile:eng/policy/exceptions.json
Shared resources (follow the owner protocol): RES-architecture-tests (append): Each repository policy task owns its suite; rule additions are append-only.
Unblocks: GOV.15

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline Gradle-time checks, negative fixtures, PR CI; no device/emulator runtime here, per P2-017 (that is WP06.07/WP30/WP32).
Completion evidence for the ledger: Per-rule pass/fail fixture table for Mobile's Gradle dependency graph.
Notes: F-023 (mobile provenance) and VG-07 (Android runtime posture) are separately scheduled at WP06.07/WP30/WP32 and are not this task's concern.
```

```text
Execute ArcForges delivery task GOV.13 — Invariant enforcement accounting report.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\governance.md (anchor task-gov-13).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/gov-13 (python tools/delivery.py claim GOV.13 --worker <name>); task branch task/gov-13 in DesktopPlatform; ledger record ledger/tasks/gov-13.md.
Kind/size: governance/M. Baseline: not-started.
Outcome: A build-produced report classifies all 429 catalogued invariants as enforced-and-passing / enforced-and-failing / not-yet-implemented, every classification derived from an actual test-run result, without re-deriving the design-stage mapping (PG-06, already closed) and without itself closing PG-11.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-05.05 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\05-architecture-and-repository-policy-tests.md, anchor rule-wp-05.05

Entry condition: adoption slice ADOPT.02.governance is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] GOV.04: at least one owning package's real policy-test run to classify (DesktopPlatform's own AT-*/RP-* results)
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:eng/accounting/invariant-report.py or equivalent; DesktopPlatform:artifacts/evidence/invariant-accounting.json
Unblocks: GOV.15

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Report generation reads real CI test-run results only; offline; re-run as each owning package lands enforcement (not a one-time close), per P2-017's 'runtime checks local, affected-scope, once, existing environment only' spirit.
Completion evidence for the ledger: 429-row accounting table, every row classified from a real result.
Notes: Will read as mostly 'not yet implemented' immediately after WP05 since most of the 429 invariants are owned by packages far downstream (WP06...WP53, per invariant-coverage.md's ownerCell). PG-11 stays open per-invariant in its OWNING package; GOV.13 never closes PG-11 or PG-06 itself - it only reports.
```

```text
Execute ArcForges delivery task GOV.14 — Specification integrity checks over the Design repository.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\governance.md (anchor task-gov-14).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/gov-14 (python tools/delivery.py claim GOV.14 --worker <name>); task branch task/gov-14 in DesktopPlatform; ledger record ledger/tasks/gov-14.md.
Kind/size: governance/M. Baseline: not-started.
Outcome: Checks run against the current Design repository and produce zero findings: every internal link resolves; every cited requirement/architecture rule/decision/verification finding/gate identifier exists; no superseded name appears as current outside docs/deprecated-inputs/; every Phase 1 decision is cited by at least one Phase 2 document or its non-applicability is stated; the work-package dependency graph is acyclic with every referenced package existing; and the decision-coverage check passes.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-05.06 (full: six checks over docs/ in ArcForges-Design, plus the 23+8-row Phase-1/Phase-2 decision-coverage check against traceability-matrix.md): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\05-architecture-and-repository-policy-tests.md, anchor rule-wp-05.06
- P2-018 (delivery-graph validation replacing the retired package-level graph check): C:\MyFile\Projects\ArcForges-Design-B\docs\decisions\phase-2-specification-decisions.md, anchor rule-p2-018

Entry condition: adoption slice ADOPT.02.governance is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] GOV.01: the citation/anchor index and continuing drift check installed by GOV.01 (PG-21)
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:eng/design_policy.py; DesktopPlatform:eng/design_corpus.py; DesktopPlatform:eng/design_graph.py; DesktopPlatform:eng/test_design_policy.py
Shared resources (follow the owner protocol): RES-desktopplatform-policy-data (append): Generated policy data is regenerated from its pinned source and never hand-edited; the reason-code registry is append-only with stable codes; each task adds its own test classes and evidence rows.
Unblocks: GOV.15

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline documentation-only checks against a pinned, clean Design commit fetched in isolation (no Design program or repository hook is run); zero findings required; PR CI.
Completion evidence for the ledger: Zero-findings report across all six checks plus the decision-coverage check.
Notes: Implements the delivery-graph validation required by the design policy export specification under P2-018, replacing the retired package-graph and serial-order check; a precondition for moving the pinned Design commit (adoption stage section 5).
```

```text
Execute ArcForges delivery task GOV.15 — WP05 stage integration verification.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\governance.md (anchor task-gov-15).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/gov-15 (python tools/delivery.py claim GOV.15 --worker <name>); task branch task/gov-15 in DesktopPlatform; ledger record ledger/tasks/gov-15.md.
Kind/size: integration/M. Baseline: not-started.
Outcome: Each of the nine repositories enforces its own boundary independently, and a cross-repository integration graph - reading each repository's published package/dependency metadata rather than cloning every reference or product repository - detects a forbidden transitive edge; both the architecture/repository-policy suite and the specification-integrity suite run in the pull-request pipeline and a violation fails the build.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-05.90 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\05-architecture-and-repository-policy-tests.md, anchor rule-wp-05.90

Entry condition: adoption slice ADOPT.02.governance is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] GOV.04: DesktopPlatform's own policy suite green
- [artifact] GOV.05: Contracts' own policy suite green
- [artifact] GOV.06: ArcNotes' own policy suite green
- [artifact] GOV.07: ArcScope's own policy suite green
- [artifact] GOV.08: ArcSlate's own policy suite green
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

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\governance.md (anchor task-gov-16).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Contracts (integration owner: Contracts integration owner, the holder of roles/integration-contracts).
Claim and handoff record: claims/gov-16 (python tools/delivery.py claim GOV.16 --worker <name>); task branch task/gov-16 in Contracts; ledger record ledger/tasks/gov-16.md.
Kind/size: governance/M. Baseline: not-started.
Outcome: A build-produced reachability matrix classifies every public/local/operator/CF/exception operation binding under catalogue 00 against all seven AZ-04 authorization fields, failing on unclassified/ambiguous fields, impossible idempotency claims, public imports of local schema, and tool reachability of human-only approval/credential/commerce/policy methods, including hostile actor-chain fixtures; separately, the owner/deployment identity chain is asserted so automation loses authorization when its owner loses permission/service eligibility even with an otherwise-valid process credential, and no customer service-principal or Organization authority is introduced.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-05:section-7-operation-by-actor-az-04-autho Section 7 operation-by-actor AZ-04 authorization reachability matrix (public/local/operator/CF/exception bindings, hostile actor-chain fixtures, resource/context/connector egress denials) and section 8 'Identity boundary evidence' (owner/deployment identity chain; automation loses authorization when its owner loses eligibility) - both unlabeled, no WP-05.MM anchor (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\05-architecture-and-repository-policy-tests.md, package-level obligation

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
