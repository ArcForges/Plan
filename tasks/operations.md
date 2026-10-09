# ArcForges delivery task prompts — Operations, support and trust and safety

Generated from Design `docs/planning/delivery/delivery-graph.json` by `tools/delivery.py`; do not edit by hand.
Each block is self-contained. Claim a task only when `python tools/delivery.py ready` lists it, with
`python tools/delivery.py claim <TASK-ID> --worker <name>`, then follow `arcforges-implementation.md`.
Tasks are ordered by lane for reading; the order is not a schedule.

## Operations, support and trust and safety

```text
Execute ArcForges delivery task OPS.01 — Service levels and alerting.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\operations.md (anchor task-ops-01).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/ops-01 (python tools/delivery.py claim OPS.01 --worker <name>); task branch task/ops-01 in Cloud; ledger record ledger/tasks/ops-01.md.
Kind/size: service/M. Baseline: not-started.
Outcome: Service-level indicators measure user-visible success per capability group with realtime/managed-AI computed independently, error budgets are visible, and every deployed alert routes correctly and names an existing runbook.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-45.00 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\45-operations-support-and-trust-safety.md, anchor rule-wp-45.00

Entry condition: adoption slice ADOPT.07.operations is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- none
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Cloud:deploy/monitoring/**
Shared resources (follow the owner protocol): RES-cloud-runbooks-and-fixtures (append): One file per runbook, monitor or provider fixture; indexes are append-only; recorded provider fixtures stay test-only.
Unblocks: OPS.02, OPS.04, OPS.12

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline tests: indicator correctness against synthetic failures, dependency-attribution, alert-routing, alert-to-runbook completeness assertion.
Completion evidence for the ledger: Alert-to-runbook completeness assertion (every deployed alert names an existing runbook).
```

```text
Execute ArcForges delivery task OPS.02 — Incident process.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\operations.md (anchor task-ops-02).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/ops-02 (python tools/delivery.py claim OPS.02 --worker <name>); task branch task/ops-02 in Cloud; ledger record ledger/tasks/ops-02.md.
Kind/size: service/M. Baseline: not-started.
Outcome: A shared four-severity ladder drives incident state tracked independently of production, a possible personal-data breach classifies automatically at the highest severity with the statutory notification clock as a hard deadline, and post-incident review produces runbook updates.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-45.01 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\45-operations-support-and-trust-safety.md, anchor rule-wp-45.01

Entry condition: adoption slice ADOPT.07.operations is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] OPS.01: alert routing to trigger incidents from
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Cloud:src/Cloud/ArcForges.Cloud.Modules.Support/**/Incidents/**
Unblocks: OPS.03, OPS.09, OPS.12

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline tests: severity-classification exercise, independence assertion for the incident system, breach-classification test.
Completion evidence for the ledger: Breach-classification-automatic-highest-severity test result.
```

```text
Execute ArcForges delivery task OPS.03 — Runbooks and rehearsal.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\operations.md (anchor task-ops-03).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/ops-03 (python tools/delivery.py claim OPS.03 --worker <name>); task branch task/ops-03 in Cloud; ledger record ledger/tasks/ops-03.md.
Kind/size: service/M. Baseline: not-started.
Outcome: Every required runbook is written with preconditions, decision points, exact steps, verification and rollback, and every runbook for an implemented owner carries at least one dated rehearsal record.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-45.02 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\45-operations-support-and-trust-safety.md, anchor rule-wp-45.02

Entry condition: adoption slice ADOPT.07.operations is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] OPS.02: the incident process the runbooks are executed within
Completion prerequisites (may start earlier; cannot complete before these are complete):
- [integration] CLOUD.51: the DR drill programme's runbooks
- [integration] HAR.04: Cloud Harness provider-failure/effect-certainty procedures

Permitted write scope: Cloud:docs/runbooks/**
Shared resources (follow the owner protocol): RES-cloud-runbooks-and-fixtures (append): One file per runbook, monitor or provider fixture; indexes are append-only; recorded provider fixtures stay test-only.
Unblocks: OPS.12

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Completeness check against the required runbook set (docs/requirements/products/arcforges-cloud.md §9.1); a dated rehearsal record per runbook, executed under existing environment per P2-017 (no new infra spun up for the rehearsal itself).
Completion evidence for the ledger: Completeness check result; dated rehearsal record per implemented-owner runbook; explicit pending markers for DR/CF cases awaiting WP-46/WP-52.
Notes: Contributes to PG-04 (runbook rehearsal, Operations Owner, currently OPEN per open-gates-register.md).
```

```text
Execute ArcForges delivery task OPS.04 — Status page.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\operations.md (anchor task-ops-04).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Web (integration owner: Web integration owner, the holder of roles/integration-web).
Claim and handoff record: claims/ops-04 (python tools/delivery.py claim OPS.04 --worker <name>); task branch task/ops-04 in Web; ledger record ledger/tasks/ops-04.md.
Kind/size: service/M. Baseline: not-started.
Outcome: An independently hosted status page publishes only user-facing capability components with an explicit reviewed health-to-component mapping, survives a full Cloud outage, and publishes its emergency alternate URL in at least three places.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-45.03 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\45-operations-support-and-trust-safety.md, anchor rule-wp-45.03
- WP-45:browser-matrix-acceptance-status-page-su browser matrix acceptance; status page supported/degraded/blocked browser behavior, static no-JS readability (browser matrix acceptance; status page supported/degraded/blocked browser behavior, static no-JS readability): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\45-operations-support-and-trust-safety.md, package-level obligation
- WP-45:browser-matrix-acceptance-browser-suppor Browser matrix acceptance (browser-support.v1 supported/degraded/blocked) (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\45-operations-support-and-trust-safety.md, package-level obligation

Entry condition: adoption slice ADOPT.09.operations is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] OPS.01: capability health signals to map from
- [artifact] WEB.01: the C# static generator and locale/URL inventory that the status route is generated through
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Web:src/ArcForges.Web.Site/**/status/**
Shared resources (follow the owner protocol): RES-cloud-runbooks-and-fixtures (append): One file per runbook, monitor or provider fixture; indexes are append-only; recorded provider fixtures stay test-only.
Unblocks: OPS.12

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline/staged tests: full-cloud-outage availability, per-capability mapping, vendor-name-absence scan; static no-JS readability check per browser-support.v1.
Completion evidence for the ledger: Full-cloud-outage availability test; vendor-name-absence scan (zero hits).
Notes: Planning repair 2026-10-08 (DLV-34; P2-021): The output path moves from the React apps/site tree (which WEB.01 and WEB.40 replace) to the C# static generator (ArcForges.Web.Site). Its full-cloud-outage, per-capability mapping, vendor-name-absence and no-JS readability criteria are unchanged. OPS.04 stays held until WEB.01 delivers.
```

```text
Execute ArcForges delivery task OPS.05 — Operator console and support access.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\operations.md (anchor task-ops-05).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Web (integration owner: Web integration owner, the holder of roles/integration-web).
Claim and handoff record: claims/ops-05 (python tools/delivery.py claim OPS.05 --worker <name>); task branch task/ops-05 in Web; ledger record ledger/tasks/ops-05.md.
Kind/size: service/XL. Baseline: not-started.
Outcome: The operator console runs on a separate origin with a separate identity system, never in public navigation; support access is explicit, scoped, time-bounded, consented and audited; a destructive action needs a second authorised operator; and no parallel unversioned admin API exists.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-45.04 (all work except the parts mapped to OPS.13): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\45-operations-support-and-trust-safety.md, anchor rule-wp-45.04
- WP-45:operator-contract-closure-the-real-conso Operator contract closure — the real console join (operator contract closure; the real console join — wiring every generated role/method pair into the console UI): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\45-operations-support-and-trust-safety.md, package-level obligation
- WP-45:browser-matrix-acceptance-supported-degr browser matrix acceptance; supported/degraded/blocked browser behavior for the operator console's own flows (browser matrix acceptance; supported/degraded/blocked browser behavior for the operator console's own flows): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\45-operations-support-and-trust-safety.md, package-level obligation
- WP-45:browser-matrix-acceptance-browser-suppor Browser matrix acceptance (browser-support.v1 supported/degraded/blocked) (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\45-operations-support-and-trust-safety.md, package-level obligation

Entry condition: adoption slice ADOPT.09.operations is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [contract] CON.14: the OperatorService full RPC surface
- [artifact] POL.05: the kill-switch RPC implementation
- [artifact] WEB.40: the Operations profile skeleton (ArcForges.Web.Operations, separate origin and identity configuration) and the C# policy suite
Completion prerequisites (may start earlier; cannot complete before these are complete):
- [integration] COM.13: the financial-owner RPC implementations

Permitted write scope: Web:src/ArcForges.Web.Operations/**; Web:tests/ArcForges.Web.Operations.Tests/**
Shared resources (follow the owner protocol): RES-cloud-runbooks-and-fixtures (append): One file per runbook, monitor or provider fixture; indexes are append-only; recorded provider fixtures stay test-only.; RES-contracts-schema-sources (append): Each schema closure task edits only its own domain proto or HTTP-schema files and adds its own sharded constraint and fixture files. Schema-closure tasks and Contracts policy tasks that touch package/access/provenance/dependency input registries share this append/rebase protocol: append only task-owned rows and successor receipts to package, compiled access/hash, foundation, operation, constraint, provenance source/output, binding, and dependency-review inventories; preserve prior history and never rewrite another task's rows. Refresh dependency input hashes only for the task-owned closure; do not expand dependency versions or closure except for the two exact task-specific exceptions below. One narrow exception applies only to CON.14: it may add the single ArcForges.Contracts.CloudInternal → existing ArcForges.Contracts.PublicApi package/project edge required for generated OperatorService imports to resolve to their canonical owner, implemented only by one ProjectReference in the CloudInternal csproj, its existing packages.lock.json, and the CloudInternal dependency row in eng/contract-packages.json. This expands only CloudInternal's package-specific closure to include the existing PublicApi package and its existing same-version transitive realization; the lock may add the PublicApi project and already-pinned Grpc.Core.Api 2.84.0, while existing Foundation and Google.Protobuf 3.36.1 entries retain their versions and hashes. The exception permits only the matching exact input-hash refreshes and immutable con-14-r1 successor chained from active con-22-r1. Preserve the aggregate dependency coordinate/version set, package IDs and licences, every other package's dependency usage/closure, Foundation/PublicApi ownership, all prior receipt history, and the PublicApi 1.0.0-ci.113.1 PreviousClient-only fixture classification. A second, CON.11-only exception permits only the already-authorized Events → PublicApi and CloudInternal → Events/PublicApi project references to realize in Events and CloudInternal as the corresponding first-party Project lock entries plus the exact centrally pinned Grpc.Core.Api CentralTransitive row: requested [2.84.0, ), resolved 2.84.0, contentHash p2SOMl6q/GZ4/5MLkgboC/z55g4zKUEruRn/g46QgppjQBVnsLZVBU/9VO7n60ll38G3Eo8Zu9b7x+W01GKFVg==. Only the five existing consumer lockfiles tests/StructureTests/packages.lock.json, tests/public/SerializationProbe/packages.lock.json, src/public/dotnet/ArcForges.Sdk.Client/packages.lock.json, src/public/dotnet/ArcForges.Cli/packages.lock.json, and src/public/dotnet/ArcForges.Contracts.Validation/packages.lock.json may add ArcForges.Contracts.PublicApi [1.0.0-ci.0.0, ) to the existing ArcForges.Contracts.Events Project.dependencies field, exactly as SDK restore requires. In only tests/StructureTests/packages.lock.json and tests/public/SerializationProbe/packages.lock.json, SDK restore may also add ArcForges.Contracts.Events and ArcForges.Contracts.PublicApi [1.0.0-ci.0.0, ) to the existing ArcForges.Contracts.CloudInternal Project.dependencies field, exactly as the already-authorized CloudInternal -> Events/PublicApi project references require; no other field, package/project entry, project dependency, target framework, version, hash, or consumer behavior changes. This exception permits only these matching task-owned lock/policy input-hash refreshes and the immutable con-11-r1 successor, and preserves the aggregate coordinate/version/licence union, all other package usage/closures, existing Foundation, Google.Protobuf and Microsoft.NET.ILLink.Tasks rows, previous receipt history, package identities and the PreviousClient-only fixture classification. No direct package reference, PrivateAssets or asset override, other coordinate/version/hash, project, lock row, licence exception or dependency algorithm change is authorized; all other tasks retain the no-closure-expansion rule. Public Kotlin/Dokka successors are exclusively governed by RES-contracts-dokka-profile. A proto file with several contributing tasks (operator, policy/configuration) has one designated author task and the others request changes through it. Each serialized merge is followed by a rebase and regeneration before integration of the next task.; RES-web-app-routing (append): The application shell task owns root route registration; each surface adds its own route module and per-origin edge directory.
Unblocks: CLOUD.64, OPS.06, OPS.07, OPS.08, OPS.11, OPS.13, WEB.31

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline/staged tests: silent-impersonation negative, scope/expiry, two-operator requirement, audit-completeness, parallel-admin-API-absence assertion, every generated role/method pair of the retained operator contract (allowed and refused; catalog pairs are out of scope, P2-026), double-execution-of-one-approval negative; browser-support.v1 supported/degraded/blocked behavior per P2-017 (no live E2E browser matrix in routine CI).
Completion evidence for the ledger: Silent-impersonation negative result; two-operator requirement result; full retained-contract role/method matrix exercised (allowed and refused).
Notes: BR-06 ('an operator never silently becomes a user') is a headline security invariant for the whole package; the silent-impersonation negative test is worth proving early against a minimal console skeleton before building every case-type UI on top. Planning repair 2026-10-08 (DLV-34; P2-021): The operator console is the standalone Blazor WebAssembly Operations profile (P2-021 item 2) on its own origin and identity, not part of the Account or Chat bundles. Its writes move from the React apps/app tree to ArcForges.Web.Operations, whose skeleton WEB.40 creates. The silent-impersonation, two-operator, audit, scope/expiry and role/method criteria are unchanged. Tests are xUnit and bUnit; browser-support.v1 checks stay local opt-in per P2-017. Planning repair 2026-10-09 (P2-026; scope correction): reduced: the PackageCatalog and catalog operator methods and their role/method pairs, the package-review feature folder and its tests in ArcForges.Web.Operations, and catalog scope in the operator role matrix are out of scope, not completed.
```

```text
Execute ArcForges delivery task OPS.06 — Break-glass.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\operations.md (anchor task-ops-06).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/ops-06 (python tools/delivery.py claim OPS.06 --worker <name>); task branch task/ops-06 in Cloud; ledger record ledger/tasks/ops-06.md.
Kind/size: service/M. Baseline: not-started.
Outcome: A distinct, alarmed emergency-access path requires justification, expires automatically, alerts immediately, requires mandatory post-hoc review, and is visible to the affected account owner.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-45.05 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\45-operations-support-and-trust-safety.md, anchor rule-wp-45.05

Entry condition: adoption slice ADOPT.07.operations is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] OPS.05: the operator identity/audit infrastructure
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Cloud:src/Cloud/ArcForges.Cloud.Modules.Support/**/BreakGlass/**
Shared resources (follow the owner protocol): RES-cloud-runbooks-and-fixtures (append): One file per runbook, monitor or provider fixture; indexes are append-only; recorded provider fixtures stay test-only.
Unblocks: OPS.12

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline tests: activation alerting, expiry enforcement, review-requirement, owner-visibility.
Completion evidence for the ledger: Expiry-enforcement test; owner-visibility test.
```

```text
Execute ArcForges delivery task OPS.07 — Support cases and in-product reporting.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\operations.md (anchor task-ops-07).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/ops-07 (python tools/delivery.py claim OPS.07 --worker <name>); task branch task/ops-07 in Cloud; ledger record ledger/tasks/ops-07.md.
Kind/size: service/M. Baseline: not-started.
Outcome: In-product problem reporting produces a support reference without attaching user data by default, support cases link to diagnostic references rather than content, and the case lifecycle carries defined response expectations.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-45.06 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\45-operations-support-and-trust-safety.md, anchor rule-wp-45.06

Entry condition: adoption slice ADOPT.07.operations is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] OPS.05: operator case-handling surface
- [contract] CON.22: published support operations
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Cloud:src/Cloud/ArcForges.Cloud.Modules.Support/**/Cases/**
Unblocks: OPS.08, OPS.12

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline tests: no-data-by-default assertion, reference-resolution, lifecycle.
Completion evidence for the ledger: No-data-by-default assertion result.
```

```text
Execute ArcForges delivery task OPS.08 — Trust and safety.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\operations.md (anchor task-ops-08).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/ops-08 (python tools/delivery.py claim OPS.08 --worker <name>); task branch task/ops-08 in Cloud; ledger record ledger/tasks/ops-08.md.
Kind/size: service/L. Baseline: not-started.
Outcome: Account-level enforcement (community report intake for public ecosystem objects is out of scope, P2-026) drives a proportionate enforcement ladder with every action recorded and communicated, account enforcement states integrate with the account model, and appeals have a defined path and response expectation.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-45.07 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\45-operations-support-and-trust-safety.md, anchor rule-wp-45.07

Entry condition: adoption slice ADOPT.07.operations is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] OPS.07: the support case/reference model
- [artifact] OPS.05: operator audit infrastructure
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Cloud:src/Cloud/ArcForges.Cloud.Modules.TrustSafety/**
Unblocks: OPS.12

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline tests: ladder-progression, communication-completeness, appeal-path, enforcement-audit.
Completion evidence for the ledger: Ladder-progression test; appeal-path test.
Notes: Planning repair 2026-10-09 (P2-026; scope correction): reduced: community report intake and the Community Report to Investigation to Enforcement chain for public ecosystem objects, the community-report case type on OPS.07 reference resolution, and package-version enforcement and binary security-revocation appeals (AP-04) are out of scope, not completed.
```

```text
Execute ArcForges delivery task OPS.09 — Operational mail and provider drills.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\operations.md (anchor task-ops-09).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/ops-09 (python tools/delivery.py claim OPS.09 --worker <name>); task branch task/ops-09 in Cloud; ledger record ledger/tasks/ops-09.md.
Kind/size: service/M. Baseline: not-started.
Outcome: Transactional/broadcast email use the real WP-22 Postmark/SES adapters with separated streams; outage and reconciliation drills are rehearsed under a prepared secondary path; and the first-party private security-advisory intake-through-publication process is complete (third-party package advisories and in-product package containment or revocation attention are out of scope, P2-026).

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-45.08 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\45-operations-support-and-trust-safety.md, anchor rule-wp-45.08
- WP-45:producer-prerequisites-wp45-08-must-cons Producer prerequisites (WP45.08 must consume real WP22 mail, no fixture) (producer prerequisites; consuming WP-22 real mail artifacts without deferring WP-22's own gate; package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\45-operations-support-and-trust-safety.md, package-level obligation

Entry condition: adoption slice ADOPT.07.operations is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] CLOUD.12: native/browser authentication's real Postmark/SES adapters
- [artifact] OPS.02: the incident process
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Cloud:src/Cloud/ArcForges.Cloud.Modules.Notification/**; Cloud:src/Cloud/ArcForges.Cloud.Modules.TrustSafety/**/Advisories/**
Shared resources (follow the owner protocol): RES-cloud-runbooks-and-fixtures (append): One file per runbook, monitor or provider fixture; indexes are append-only; recorded provider fixtures stay test-only.
Unblocks: OPS.10, OPS.12

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline tests where possible (spoofed/replayed callback, bounced/complained suppression, content-redaction) plus recorded live-provider drill evidence (unknown send, DNS readiness, independent status/incident during a real Cloud outage) kept outside routine CI per P2-017.
Completion evidence for the ledger: Live operational evidence and rollback-contact record; signed advisory authenticity and affected-version-matching results; no disclosure before approved publication.
Notes: This task cannot use a mail substitute — WP-45 explicitly states runtime mail fixtures are absent and that WP-45.08 'is not the first email producer,' i.e. it must consume WP-22's real adapters from day one. Planning repair 2026-10-09 (P2-026; scope correction): reduced: publisher-facing advisories for vulnerabilities in third-party packages (SR-12) and in-product package containment and revocation attention (I-442) are out of scope, not completed; only the first-party advisory process remains.
```

```text
Execute ArcForges delivery task OPS.10 — Customer push delivery and registration lifecycle.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\operations.md (anchor task-ops-10).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/ops-10 (python tools/delivery.py claim OPS.10 --worker <name>); task branch task/ops-10 in Cloud; ledger record ledger/tasks/ops-10.md.
Kind/size: service/L. Baseline: not-started.
Outcome: Notification.IPushSender sends through a typed FCM HTTP v1 credential adapter with a unique delivery-intent outbox, generation/revocation checks and the exact push.v1 profile, working against an actual isolated Firebase project with bounded, fenced recovery.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-45.09 (all work except the parts mapped to AND.26): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\45-operations-support-and-trust-safety.md, anchor rule-wp-45.09

Entry condition: adoption slice ADOPT.07.operations is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] OPS.09: the Notification module's adapter pattern and outbox convention
- [contract] CON.22: published notification operations including push registration
Completion prerequisites (may start earlier; cannot complete before these are complete):
- [integration] AND.26: physical Android device receipt, no-GMS and permission evidence

Permitted write scope: Cloud:src/Cloud/ArcForges.Cloud.Modules.Notification/**/Push/**
Permitted substitutes (never real integration evidence): SUB-fcm-recorded-responses: Sender error, retry and token-invalidation handling only; live sending is proven by the same task and physical receipt by the Android integration task. Real producer ['OPS.10']; removed by AND.26
Unblocks: AND.26, OPS.12

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Live isolated Firebase project send (kept outside routine CI per P2-017, real service) plus offline tests for token-rotation race, crash-after-acceptance duplicates, TTL expiry, revoke-before-send, no-secret-logging.
Completion evidence for the ledger: Recorded invalid-token/payload/project/rate-limit responses; no-secret-logging scan.
Notes: Named as required-real-early scaffolding in implementation-sequence §3.1 (recorded FCM WP45.09 to WP32 proves device receipt) — unlike payment/mail, no fixture stands in for the server-side send itself; it is real against an isolated Firebase project from the start.
```

```text
Execute ArcForges delivery task OPS.12 — Owned-artifact receipt.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\operations.md (anchor task-ops-12).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/ops-12 (python tools/delivery.py claim OPS.12 --worker <name>); task branch task/ops-12 in Cloud; ledger record ledger/tasks/ops-12.md.
Kind/size: service/S. Baseline: not-started.
Outcome: The package-level owned-artifact/real-integration receipt is recorded confirming actual role/redaction/status/support-case behavior and actionable CF/R2 failure diagnostics, with no second Node/operations business host.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-45.90 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\45-operations-support-and-trust-safety.md, anchor rule-wp-45.90

Entry condition: adoption slice ADOPT.07.operations is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] OPS.01: package task delivered
- [artifact] OPS.02: package task delivered
- [artifact] OPS.03: package task delivered
- [artifact] OPS.04: package task delivered
- [artifact] OPS.06: package task delivered
- [artifact] OPS.07: package task delivered
- [artifact] OPS.08: package task delivered
- [artifact] OPS.09: package task delivered
- [artifact] OPS.10: package task delivered
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Cloud:eng/provenance/records/**
Unblocks: REL.06, REL.09

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Aggregation of OPS.01-10 evidence; no-second-host architecture assertion.
Completion evidence for the ledger: The owned-artifact/real-integration receipt; no-second-Node-host assertion.
Notes: Planning repair 2026-10-09 (P2-026; scope correction): reduced: the receipt aggregates OPS.01-10 only (OPS.11 is out of scope); the physical-device FCM receipt (AND.26) gates the Android release (REL.04), not this receipt.
```

```text
Execute ArcForges delivery task OPS.13 — Operator console exercises real financial-owner and kill-switch RPCs end to end.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\operations.md (anchor task-ops-13).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Web (integration owner: Web integration owner, the holder of roles/integration-web).
Claim and handoff record: claims/ops-13 (python tools/delivery.py claim OPS.13 --worker <name>); task branch task/ops-13 in Web; ledger record ledger/tasks/ops-13.md.
Kind/size: integration/M. Baseline: not-started.
Outcome: an authorised operator can actually grant/revoke/issueCredit/adjustCredit/refund and activate a kill switch through the console UI, not just via direct RPC test calls

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-45.04 (exercise every generated role/method pair via the actual console UI): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\45-operations-support-and-trust-safety.md, anchor rule-wp-45.04
- WP-45.10 (real operator console join): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\45-operations-support-and-trust-safety.md, anchor rule-wp-45.10

Entry condition: adoption slice ADOPT.09.operations is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] COM.13: real, delivered outcome of COM.13 (Operator financial-owner proposal/approval operations)
- [artifact] POL.05: real, delivered outcome of POL.05 (Kill switches)
- [artifact] OPS.05: real, delivered outcome of OPS.05 (Operator console and support access)
- [artifact] CON.14: real, delivered outcome of CON.14 (Operator control service (OperatorService, full §9/9.1/9.2 protocol))
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: 
Unblocks: COM.13

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Local real-integration run of the affected scenario in an existing environment, recorded once; offline and static checks in CI; no hosted runtime, device, browser, live-service or inference CI (P2-017).
Completion evidence for the ledger: an authorised operator can actually grant/revoke/issueCredit/adjustCredit/refund and activate a kill switch through the console UI, not just via direct RPC test calls
Notes: Merged duplicate integration or closure task formerly proposed as CON.98. Planning repair 2026-10-08 (DLV-34; P2-021): The console this task exercises is the Blazor Operations profile (OPS.05, WEB.40). The end-to-end RPC and kill-switch criteria are stack-neutral and unchanged; OPS.13 has no writes of its own. Planning repair 2026-10-09 (P2-026; scope correction): reduced: the WP-45.10 real operator console join for package review (catalogReview and catalogRevoke through the console) is out of scope, not completed; the OPS.11 start edge is removed.
```

### Out of scope

Excluded from the active plan. No prompt is issued and these tasks are never claimable; their decision, note and ledger status are listed here.

| Task | Title | Decision | Mode | Note | Ledger status |
|---|---|---|---|---|---|
| OPS.11 | Package review and revocation console | P2-026 | excluded | Out of scope, not completed: no concrete necessary ArcScope consumer; the package review and revocation console depends on the excluded PackageCatalog and catalog ecosystem, which are post-V1 (P2-026 S5). | no record |
