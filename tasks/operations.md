# ArcForges delivery task prompts — Operations, support and trust and safety

Generated from Design `docs/planning/delivery/delivery-graph.json` by `tools/delivery.py`; do not edit by hand.
Each block is self-contained. Claim a task only when `python tools/delivery.py ready` lists it, with
`python tools/delivery.py claim <TASK-ID> --worker <name>`, then follow `arcforges-implementation.md`.
Tasks are ordered by lane for reading; the order is not a schedule.

## Operations, support and trust and safety

```text
Execute ArcForges delivery task OPS.01 — Service levels and alerting.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\operations.md (anchor task-ops-01).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/ops-01 (python tools/delivery.py claim OPS.01 --worker <name>); task branch task/ops-01 in Cloud; ledger record ledger/tasks/ops-01.md.
Kind/size: service/M. Baseline: not-started.
Outcome: Service-level indicators measure user-visible success per capability group with realtime/managed-AI computed independently, error budgets are visible, and every deployed alert routes correctly and names an existing runbook.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-45.00 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\45-operations-support-and-trust-safety.md, anchor rule-wp-45.00

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

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\operations.md (anchor task-ops-02).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/ops-02 (python tools/delivery.py claim OPS.02 --worker <name>); task branch task/ops-02 in Cloud; ledger record ledger/tasks/ops-02.md.
Kind/size: service/M. Baseline: not-started.
Outcome: A shared four-severity ladder drives incident state tracked independently of production, a possible personal-data breach classifies automatically at the highest severity with the statutory notification clock as a hard deadline, and post-incident review produces runbook updates.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-45.01 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\45-operations-support-and-trust-safety.md, anchor rule-wp-45.01

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

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\operations.md (anchor task-ops-03).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/ops-03 (python tools/delivery.py claim OPS.03 --worker <name>); task branch task/ops-03 in Cloud; ledger record ledger/tasks/ops-03.md.
Kind/size: service/M. Baseline: not-started.
Outcome: Every required runbook is written with preconditions, decision points, exact steps, verification and rollback, and every runbook for an implemented owner carries at least one dated rehearsal record.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-45.02 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\45-operations-support-and-trust-safety.md, anchor rule-wp-45.02

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

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\operations.md (anchor task-ops-04).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Web (integration owner: Web integration owner, the holder of roles/integration-web).
Claim and handoff record: claims/ops-04 (python tools/delivery.py claim OPS.04 --worker <name>); task branch task/ops-04 in Web; ledger record ledger/tasks/ops-04.md.
Kind/size: service/M. Baseline: not-started.
Outcome: An independently hosted status page publishes only user-facing capability components with an explicit reviewed health-to-component mapping, survives a full Cloud outage, and publishes its emergency alternate URL in at least three places.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-45.03 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\45-operations-support-and-trust-safety.md, anchor rule-wp-45.03
- WP-45:browser-matrix-acceptance-status-page-su browser matrix acceptance; status page supported/degraded/blocked browser behavior, static no-JS readability (browser matrix acceptance; status page supported/degraded/blocked browser behavior, static no-JS readability): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\45-operations-support-and-trust-safety.md, package-level obligation
- WP-45:browser-matrix-acceptance-browser-suppor Browser matrix acceptance (browser-support.v1 supported/degraded/blocked) (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\45-operations-support-and-trust-safety.md, package-level obligation

Entry condition: adoption slice ADOPT.09.operations is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] OPS.01: capability health signals to map from
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Web:apps/site/**/status/**
Shared resources (follow the owner protocol): RES-cloud-runbooks-and-fixtures (append): One file per runbook, monitor or provider fixture; indexes are append-only; recorded provider fixtures stay test-only.
Unblocks: OPS.12

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline/staged tests: full-cloud-outage availability, per-capability mapping, vendor-name-absence scan; static no-JS readability check per browser-support.v1.
Completion evidence for the ledger: Full-cloud-outage availability test; vendor-name-absence scan (zero hits).
```

```text
Execute ArcForges delivery task OPS.05 — Operator console and support access.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\operations.md (anchor task-ops-05).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Web (integration owner: Web integration owner, the holder of roles/integration-web).
Claim and handoff record: claims/ops-05 (python tools/delivery.py claim OPS.05 --worker <name>); task branch task/ops-05 in Web; ledger record ledger/tasks/ops-05.md.
Kind/size: service/XL. Baseline: not-started.
Outcome: The operator console runs on a separate origin with a separate identity system, never in public navigation; support access is explicit, scoped, time-bounded, consented and audited; a destructive action needs a second authorised operator; and no parallel unversioned admin API exists.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-45.04 (all work except the parts mapped to OPS.13): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\45-operations-support-and-trust-safety.md, anchor rule-wp-45.04
- WP-45:operator-contract-closure-the-real-conso Operator contract closure — the real console join (operator contract closure; the real console join — wiring every generated role/method pair into the console UI): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\45-operations-support-and-trust-safety.md, package-level obligation
- WP-45:browser-matrix-acceptance-supported-degr browser matrix acceptance; supported/degraded/blocked browser behavior for the operator console's own flows (browser matrix acceptance; supported/degraded/blocked browser behavior for the operator console's own flows): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\45-operations-support-and-trust-safety.md, package-level obligation
- WP-45:browser-matrix-acceptance-browser-suppor Browser matrix acceptance (browser-support.v1 supported/degraded/blocked) (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\45-operations-support-and-trust-safety.md, package-level obligation

Entry condition: adoption slice ADOPT.09.operations is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [contract] CON.14: the OperatorService full RPC surface
- [artifact] POL.05: the kill-switch RPC implementation
Completion prerequisites (may start earlier; cannot complete before these are complete):
- [integration] COM.13: the financial-owner RPC implementations

Permitted write scope: Web:apps/app/**
Shared resources (follow the owner protocol): RES-cloud-runbooks-and-fixtures (append): One file per runbook, monitor or provider fixture; indexes are append-only; recorded provider fixtures stay test-only.; RES-contracts-schema-sources (append): Each closure task edits only its own domain proto or HTTP-schema files and adds its own sharded constraint and fixture files; shared inventories (package inventory, foundation inventory, constraint aggregate) are append-only per closure. A proto file with several contributing tasks (operator, policy/configuration) has one designated author task and the others request changes through it. The integration owner merges closure pull requests one at a time and the next author rebases and regenerates.; RES-web-app-routing (append): The application shell task owns root route registration; each surface adds its own route module and per-origin edge directory.
Unblocks: CLOUD.64, OPS.06, OPS.07, OPS.08, OPS.11, OPS.13, WEB.31

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline/staged tests: silent-impersonation negative, scope/expiry, two-operator requirement, audit-completeness, parallel-admin-API-absence assertion, every generated role/method pair (allowed and refused), double-execution-of-one-approval negative; browser-support.v1 supported/degraded/blocked behavior per P2-017 (no live E2E browser matrix in routine CI).
Completion evidence for the ledger: Silent-impersonation negative result; two-operator requirement result; full role/method matrix exercised (allowed and refused).
Notes: BR-06 ('an operator never silently becomes a user') is a headline security invariant for the whole package; the silent-impersonation negative test is worth proving early against a minimal console skeleton before building every case-type UI on top.
```

```text
Execute ArcForges delivery task OPS.06 — Break-glass.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\operations.md (anchor task-ops-06).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/ops-06 (python tools/delivery.py claim OPS.06 --worker <name>); task branch task/ops-06 in Cloud; ledger record ledger/tasks/ops-06.md.
Kind/size: service/M. Baseline: not-started.
Outcome: A distinct, alarmed emergency-access path requires justification, expires automatically, alerts immediately, requires mandatory post-hoc review, and is visible to the affected account owner.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-45.05 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\45-operations-support-and-trust-safety.md, anchor rule-wp-45.05

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

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\operations.md (anchor task-ops-07).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/ops-07 (python tools/delivery.py claim OPS.07 --worker <name>); task branch task/ops-07 in Cloud; ledger record ledger/tasks/ops-07.md.
Kind/size: service/M. Baseline: not-started.
Outcome: In-product problem reporting produces a support reference without attaching user data by default, support cases link to diagnostic references rather than content, and the case lifecycle carries defined response expectations.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-45.06 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\45-operations-support-and-trust-safety.md, anchor rule-wp-45.06

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

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\operations.md (anchor task-ops-08).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/ops-08 (python tools/delivery.py claim OPS.08 --worker <name>); task branch task/ops-08 in Cloud; ledger record ledger/tasks/ops-08.md.
Kind/size: service/L. Baseline: not-started.
Outcome: Community report intake drives a proportionate enforcement ladder with every action recorded and communicated, account enforcement states integrate with the account model, and appeals have a defined path and response expectation.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-45.07 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\45-operations-support-and-trust-safety.md, anchor rule-wp-45.07

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
```

```text
Execute ArcForges delivery task OPS.09 — Operational mail and provider drills.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\operations.md (anchor task-ops-09).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/ops-09 (python tools/delivery.py claim OPS.09 --worker <name>); task branch task/ops-09 in Cloud; ledger record ledger/tasks/ops-09.md.
Kind/size: service/M. Baseline: not-started.
Outcome: Transactional/broadcast email use the real WP-22 Postmark/SES adapters with separated streams; outage and reconciliation drills are rehearsed under a prepared secondary path; and the private security-advisory intake-through-publication process is complete with in-product containment/revocation attention.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-45.08 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\45-operations-support-and-trust-safety.md, anchor rule-wp-45.08
- WP-45:producer-prerequisites-wp45-08-must-cons Producer prerequisites (WP45.08 must consume real WP22 mail, no fixture) (producer prerequisites; consuming WP-22 real mail artifacts without deferring WP-22's own gate; package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\45-operations-support-and-trust-safety.md, package-level obligation

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
Notes: This task cannot use a mail substitute — WP-45 explicitly states runtime mail fixtures are absent and that WP-45.08 'is not the first email producer,' i.e. it must consume WP-22's real adapters from day one.
```

```text
Execute ArcForges delivery task OPS.10 — Customer push delivery and registration lifecycle.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\operations.md (anchor task-ops-10).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/ops-10 (python tools/delivery.py claim OPS.10 --worker <name>); task branch task/ops-10 in Cloud; ledger record ledger/tasks/ops-10.md.
Kind/size: service/L. Baseline: not-started.
Outcome: Notification.IPushSender sends through a typed FCM HTTP v1 credential adapter with a unique delivery-intent outbox, generation/revocation checks and the exact push.v1 profile, working against an actual isolated Firebase project with bounded, fenced recovery.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-45.09 (all work except the parts mapped to AND.26): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\45-operations-support-and-trust-safety.md, anchor rule-wp-45.09

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
Execute ArcForges delivery task OPS.11 — Package review and revocation console.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\operations.md (anchor task-ops-11).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Web (integration owner: Web integration owner, the holder of roles/integration-web).
Claim and handoff record: claims/ops-11 (python tools/delivery.py claim OPS.11 --worker <name>); task branch task/ops-11 in Web; ledger record ledger/tasks/ops-11.md.
Kind/size: service/M. Baseline: not-started.
Outcome: The operator console integrates WP-41 PackageCatalog operator methods (catalogReview/catalogRevoke) with independent operator authentication, step-up/evidence and audit, and review/revocation decisions visibly affect real signed catalog consumers.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-45.10 (all work except the parts mapped to OPS.13): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\45-operations-support-and-trust-safety.md, anchor rule-wp-45.10

Entry condition: adoption slice ADOPT.09.operations is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] EXT.06: the PackageCatalog producer's operator methods (GetCatalogSubmission etc.)
- [contract] CON.14: the catalogReview/catalogRevoke operator RPC shapes
- [artifact] OPS.05: the operator console's identity/step-up/audit shell
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Web:apps/app/**
Shared resources (follow the owner protocol): RES-contracts-schema-sources (append): Each closure task edits only its own domain proto or HTTP-schema files and adds its own sharded constraint and fixture files; shared inventories (package inventory, foundation inventory, constraint aggregate) are append-only per closure. A proto file with several contributing tasks (operator, policy/configuration) has one designated author task and the others request changes through it. The integration owner merges closure pull requests one at a time and the next author rebases and regenerates.; RES-web-app-routing (append): The application shell task owns root route registration; each surface adds its own route module and per-origin edge directory.
Unblocks: OPS.12, OPS.13

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline tests: customer/PAT denial, changed-proposal-hash, replay, revoked-package, failed-index-publication/retry.
Completion evidence for the ledger: Revocation affecting a real signed catalog consumer, with recorded operator evidence.
```

```text
Execute ArcForges delivery task OPS.12 — Owned-artifact receipt.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\operations.md (anchor task-ops-12).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/ops-12 (python tools/delivery.py claim OPS.12 --worker <name>); task branch task/ops-12 in Cloud; ledger record ledger/tasks/ops-12.md.
Kind/size: service/S. Baseline: not-started.
Outcome: The package-level owned-artifact/real-integration receipt is recorded confirming actual role/redaction/status/support-case behavior and actionable CF/R2 failure diagnostics, with no second Node/operations business host.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-45.90 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\45-operations-support-and-trust-safety.md, anchor rule-wp-45.90

Entry condition: adoption slice ADOPT.07.operations is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] OPS.11: the last domain producer's evidence to attach
- [artifact] AND.26: package task delivered
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

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Aggregation of OPS.01-11 evidence; no-second-host architecture assertion.
Completion evidence for the ledger: The owned-artifact/real-integration receipt; no-second-Node-host assertion.
```

```text
Execute ArcForges delivery task OPS.13 — Operator console exercises real financial-owner and kill-switch RPCs end to end.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\operations.md (anchor task-ops-13).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Web (integration owner: Web integration owner, the holder of roles/integration-web).
Claim and handoff record: claims/ops-13 (python tools/delivery.py claim OPS.13 --worker <name>); task branch task/ops-13 in Web; ledger record ledger/tasks/ops-13.md.
Kind/size: integration/M. Baseline: not-started.
Outcome: an authorised operator can actually grant/revoke/issueCredit/adjustCredit/refund and activate a kill switch through the console UI, not just via direct RPC test calls

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-45.04 (exercise every generated role/method pair via the actual console UI): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\45-operations-support-and-trust-safety.md, anchor rule-wp-45.04
- WP-45.10 (real operator console join): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\45-operations-support-and-trust-safety.md, anchor rule-wp-45.10

Entry condition: adoption slice ADOPT.09.operations is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] COM.13: real, delivered outcome of COM.13 (Operator financial-owner proposal/approval operations)
- [artifact] POL.05: real, delivered outcome of POL.05 (Kill switches)
- [artifact] OPS.05: real, delivered outcome of OPS.05 (Operator console and support access)
- [artifact] CON.14: real, delivered outcome of CON.14 (Operator control service (OperatorService, full §9/9.1/9.2 protocol))
- [artifact] OPS.11: real, delivered outcome of OPS.11 (Package review and revocation console)
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: 
Unblocks: COM.13

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Local real-integration run of the affected scenario in an existing environment, recorded once; offline and static checks in CI; no hosted runtime, device, browser, live-service or inference CI (P2-017).
Completion evidence for the ledger: an authorised operator can actually grant/revoke/issueCredit/adjustCredit/refund and activate a kill switch through the console UI, not just via direct RPC test calls
Notes: Merged duplicate integration or closure task formerly proposed as CON.98.
```
