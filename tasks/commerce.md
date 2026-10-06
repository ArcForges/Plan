# ArcForges delivery task prompts — Commerce, entitlement and credits

Generated from Design `docs/planning/delivery/delivery-graph.json` by `tools/delivery.py`; do not edit by hand.
Each block is self-contained. Claim a task only when `python tools/delivery.py ready` lists it, with
`python tools/delivery.py claim <TASK-ID> --worker <name>`, then follow `arcforges-implementation.md`.
Tasks are ordered by lane for reading; the order is not a schedule.

## Commerce, entitlement and credits

```text
Execute ArcForges delivery task COM.01 — Provider adapter boundary.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\commerce.md (anchor task-com-01).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/com-01 (python tools/delivery.py claim COM.01 --worker <name>); task branch task/com-01 in Cloud; ledger record ledger/tasks/com-01.md.
Kind/size: service/S. Baseline: not-started.
Outcome: A provider-neutral typed boundary in the actual Commerce module and a complete production Paddle HTTP/signature/event adapter implement the current selected provider capabilities; no provider identifier/payload leaks outside the adapter. Unsupported provider capabilities refuse explicitly; ambiguous mutations return an unknown outcome and are never blindly retried. Commerce owners retain durable mutation fencing.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-42.00 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\42-commerce-entitlement-and-credits.md, anchor rule-wp-42.00

Entry condition: adoption slice ADOPT.07.commerce is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- none
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Cloud:src/ArcForges.Cloud.Modules.Commerce/Adapters/**; Cloud:tests/ArcForges.Cloud.Tests/Commerce/Adapter/**; Cloud:tests/ArchitectureTests/EvaluatedRepositoryGate.cs (exact provider API/tests only); Cloud:eng/provenance/** (owned first-party/input successors); Cloud:eng/policy/** (only exact owned source/admission bindings and immutable receipt successors); Cloud:docs/commerce-provider-adapter.md; Cloud:.dockerignore (owned Commerce Adapters source inclusion only)
Shared resources (follow the owner protocol): RES-cloud-policy-inputs (append): Append only task-owned source/test bindings and immutable successor receipts. Rebase before integration; regenerate actual input hashes and plan manifests; chain from the receipt active on main; preserve all prior versions and records. This protocol admits no unreviewed coordinate, permission or runtime behavior changes.; RES-architecture-tests (append): Each repository policy task owns its suite; rule additions are append-only.
Permitted substitutes (never real integration evidence): SUB-provider-adapter-fixture: containment (no provider type leaks) and capability-driven branching in isolation Real producer ['COM.14']; removed by COM.14
Unblocks: CLOUD.74, COM.03, COM.04

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline architecture test (dependency-direction scan) + unit tests under P2-017; no live provider network calls in CI.
Completion evidence for the ledger: Architecture-test pass log naming the forbidden-leakage scan; capability-driven behavior test results for at least one absent capability.
Notes: 

2026-10-06 production-delivery repair (docs/decisions/production-delivery-2026-10-06.md). This amendment governs conflicting historical scope notes; preserve completed evidence, immutable history and package identities. Paddle is already the D-005 selected provider. Caller-injected HTTP/clock/key custody, raw-body signature freshness/rotation, neutral typed events and actual query/checkout/refund/subscription adapters are implementation scope, not an interface-only boundary. No invented provider idempotency header or method capability; merchant-account acceptance is distinct and does not delay component implementation.

2026-10-06 verified production follow-up (docs/decisions/production-delivery-followup-2026-10-06.md). This scoped amendment governs conflicting older path/model notes; preserve closed records, package identities and immutable history. EV-01/EI-01/EI-08 retain only an allowlisted lossless business/financial projection with exact original raw-byte SHA256/size and immutable verification receipt bound to canonical projection digest, stable verification key version, signature time and verification time. Bounded original bytes exist only ephemerally during signature verification. Durable quarantine/audit/export cannot contain instrument, credentials or arbitrary provider fields. Processing/replay validates integrity-protected projection, never claims original-signature reverification of redacted bytes; provider refetch/reconciliation has independent verified authority. Unknown/malformed events retain digest/size and safe refusal metadata only.
```

```text
Execute ArcForges delivery task COM.02 — Catalogue and versioned policy.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\commerce.md (anchor task-com-02).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/com-02 (python tools/delivery.py claim COM.02 --worker <name>); task branch task/com-02 in Cloud; ledger record ledger/tasks/com-02.md.
Kind/size: service/M. Baseline: not-started.
Outcome: Offers, prices and policy versions exist as effective-dated policy data with no commercial figure compiled into code, and historical orders are immune to later price changes.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-42.01 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\42-commerce-entitlement-and-credits.md, anchor rule-wp-42.01

Entry condition: adoption slice ADOPT.07.commerce is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] COM.16: actual Abstractions plan port over signed D1
Completion prerequisites (may start earlier; cannot complete before these are complete):
- [integration] POL.02: dual-approved active configuration source with canonical revision/hash/publisher evidence

Permitted write scope: Cloud:src/ArcForges.Cloud.Modules.Commerce/Catalogue/**; Cloud:src/ArcForges.Cloud.Modules.Commerce/CommerceModule.cs; Cloud:src/ArcForges.Cloud.Modules.Commerce/ArcForges.Cloud.Modules.Commerce.csproj (existing test friend binding only); Cloud:src/ArcForges.Cloud.Modules.Abstractions/Commerce/** (verified catalogue configuration projection); Cloud:storage/plans/commerce/catalogue-*.sql; Cloud:src/ArcForges.Cloud.Storage.D1/PlanManifest.g.cs (regenerate only); Cloud:tests/ArcForges.Cloud.Tests/Commerce/Catalogue/**; Cloud:tests/worker/catalogue*.test.ts; Cloud:tests/ArchitectureTests/CloudRepository.cs (Commerce layer registration); Cloud:tests/ArchitectureTests/EvaluatedRepositoryGate.cs (exact catalogue API/tests); Cloud:package.json (offline owned test-list append); Cloud:eng/policy/** (owned input/immutable admission successors only); Cloud:eng/provenance/** (owned input successors only); Cloud:docs/commerce-catalogue.md; Cloud:.dockerignore (owned Catalogue/Abstractions Commerce source inclusion only); Cloud:worker/storage/plans.generated.ts (regenerate only)
Shared resources (follow the owner protocol): RES-cloud-policy-inputs (append): Append only task-owned source/test bindings and immutable successor receipts. Rebase before integration; regenerate actual input hashes and plan manifests; chain from the receipt active on main; preserve all prior versions and records. This protocol admits no unreviewed coordinate, permission or runtime behavior changes.; RES-cloud-storage-plans (append): Each module owns its own plan directory; the plan-manifest hash is regenerated by the author after rebase and checked in CI.; RES-architecture-tests (append): Each repository policy task owns its suite; rule additions are append-only.
Permitted substitutes (never real integration evidence): SUB-commercial-figure-proposal: Proposed figures exercise the configured paths only; approval under D-020 and commercial activation are release evidence. Real producer ['REL.08']; removed by REL.08
Unblocks: COM.03

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline unit tests: retroactivity negative test, policy-version resolution test, static scan asserting no commercial constant compiled into code (P2-017 static-check class).
Completion evidence for the ledger: Retroactivity negative test result; compiled-constant scan result (zero hits).
Notes: 

2026-10-06 production-delivery repair (docs/decisions/production-delivery-2026-10-06.md). This amendment governs conflicting historical scope notes; preserve completed evidence, immutable history and package identities. Binds the actual Commerce owner, not the unrelated PackageCatalog. Immutable price rows use append-only supersession: starts_at and version strictly increase; the newest effective started version supersedes earlier open rows, and an expired newest version does not fall back to a superseded old price. Historical exact-version reads retain old amount/currency and structural offer kind/scope/term-profile. No compiled commercial figures, default currency or new table; regional mapping comes from approved configuration. Publication requires exact canonical content/revision/hash, trusted publisher and distinct dual approval from POL.02; no source is silently trusted. All feasible authorization/replay/concurrency/persistence tests run against actual catalogue and named-plan components.
```

```text
Execute ArcForges delivery task COM.03 — Purchase pipeline.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\commerce.md (anchor task-com-03).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/com-03 (python tools/delivery.py claim COM.03 --worker <name>); task branch task/com-03 in Cloud; ledger record ledger/tasks/com-03.md.
Kind/size: service/L. Baseline: not-started.
Outcome: Purchase intent is the idempotency anchor for hosted checkout; one intent yields at most one order, a forged redirect grants nothing, and every checkout attempt carries complete internal metadata with no payment-instrument field anywhere in ArcForges.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-42.02 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\42-commerce-entitlement-and-credits.md, anchor rule-wp-42.02

Entry condition: adoption slice ADOPT.07.commerce is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] COM.01: provider adapter's hosted-checkout port and capability description
- [artifact] COM.02: Offer/Price/PriceVersion read model
- [artifact] CLOUD.24: public API idempotency-key/rate-limiting primitive
- [artifact] CLOUD.74: actual restricted provider outbound transport
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Cloud:src/ArcForges.Cloud.Modules.Commerce/**/Purchase/**; Cloud:src/ArcForges.Cloud/PublicApi/Commerce/**; Cloud:tests/ArcForges.Cloud.Tests/** (task-owned component tests only); Cloud:tests/worker/** (task-owned actual storage/adapter tests only); Cloud:tests/ArchitectureTests/** (exact owned API/layer bindings only); Cloud:eng/policy/dependency-policy.json (actual changed-input binding to a new immutable reviewed receipt); Cloud:eng/policy/dependency-reviews/com-03-*.json; Cloud:eng/provenance/** (only owned first-party and immutable input successors); Cloud:docs/com-03-implementation.md; Cloud:storage/plans/** (only task-owned module/family plans, preserve owner declarations); Cloud:src/ArcForges.Cloud.Storage.D1/PlanManifest.g.cs (regenerate only); Cloud:worker/storage/plans.generated.ts (regenerate only); Cloud:src/ArcForges.Cloud.Modules.Abstractions/** (task-owned primitive production cross-owner ports, no duplicate wire schemas); Cloud:src/ArcForges.Cloud/Composition/** (append only real task-owned service/owner registration); Cloud:.dockerignore (task-owned source inclusion only); Cloud:src/ArcForges.Cloud.Storage.D1/Migrations/pending/** (new Commerce-prefixed additive migrations only; sequence allocated at merge); Cloud:src/ArcForges.Cloud.Storage.D1/Physical/manifest/commerce.json (owned Commerce schema manifest only); Cloud:src/ArcForges.Cloud.Modules.Commerce/** (only own purchase/inbox/ledger behavior, preserve Adapters/Catalogue owners); Cloud:src/ArcForges.Cloud.Storage.D1/Physical/PhysicalSchema.g.cs (regenerate only)
Shared resources (follow the owner protocol): RES-contract-consumer-pins (append): A consumer task updates the pin it needs through a reviewed dependency change to the exact published candidate containing its closure; no consumer pins an unpublished closure or references Contracts source.; RES-cloud-policy-inputs (append): Append only task-owned source/test bindings and immutable successor receipts. Rebase before integration; regenerate actual input hashes and plan manifests; chain from the receipt active on main; preserve all prior versions and records. This protocol admits no unreviewed coordinate, permission or runtime behavior changes.; RES-cloud-storage-plans (append): Each module owns its own plan directory; the plan-manifest hash is regenerated by the author after rebase and checked in CI.; RES-cloud-host-composition (append): Each module registers through its own module entry point and route fragment; the host composition only lists modules; route and binding conflicts are resolved by the integration owner at merge.; RES-cloud-d1-migrations (append): One global D1 migration sequence: each module task authors migrations under its module prefix; the integration owner assigns the global sequence number at merge, regenerates the plan manifest and rejects edits to merged migrations; the migrator applies in sequence with receipts.
Permitted substitutes (never real integration evidence): SUB-hosted-checkout-sandbox: internal metadata completeness and redirect-forgery rejection against a scripted/sandbox redirect Real producer ['COM.14']; removed by REL.08
Unblocks: COM.04, COM.09, COM.11, COM.14

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline unit/integration tests: double-submission, redirect-forgery negative, metadata-completeness, expired-attempt reconciliation; no live Paddle calls in CI (sandbox calls stay in manual/scheduled acceptance per P2-017).
Completion evidence for the ledger: Double-submission test producing exactly one order; redirect-forgery negative result; metadata-completeness assertion.
Notes: 

2026-10-06 production-delivery repair (docs/decisions/production-delivery-2026-10-06.md). This amendment governs conflicting historical scope notes; preserve completed evidence, immutable history and package identities. Logical source paths are bound to actual existing projects, preserving namespace/package identities. New production behavior requires full contracts, logic, persistent adapters and feasible composition tests; unavailable provider/OS endpoints may be faked in component tests but never become deployed or commercial evidence. Root dependency/admission/lock changes require the exact published producer and a reviewed successor, not hash-only refresh.
```

```text
Execute ArcForges delivery task COM.04 — Provider event inbox.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\commerce.md (anchor task-com-04).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/com-04 (python tools/delivery.py claim COM.04 --worker <name>); task branch task/com-04 in Cloud; ledger record ledger/tasks/com-04.md.
Kind/size: service/L. Baseline: not-started.
Outcome: Every provider event is persisted before processing, signature-verified, deduplicated, and processed through the fixed eight-step verification chain, with quarantine and alerting for unprocessable events and idempotent full-inbox replay.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-42.03 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\42-commerce-entitlement-and-credits.md, anchor rule-wp-42.03

Entry condition: adoption slice ADOPT.07.commerce is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] COM.01: adapter signature-verification capability and typed event shape
- [artifact] COM.03: CheckoutAttempt/Order identifiers to correlate events against
- [artifact] COM.16: the published IssueGrant and RevokeGrant port and the durable Entitlement store behind it
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Cloud:src/ArcForges.Cloud.Modules.Commerce/**/Inbox/**; Cloud:fixtures/provider/**; Cloud:tests/ArcForges.Cloud.Tests/** (task-owned component tests only); Cloud:tests/worker/** (task-owned actual storage/adapter tests only); Cloud:tests/ArchitectureTests/** (exact owned API/layer bindings only); Cloud:eng/policy/dependency-policy.json (actual changed-input binding to a new immutable reviewed receipt); Cloud:eng/policy/dependency-reviews/com-04-*.json; Cloud:eng/provenance/** (only owned first-party and immutable input successors); Cloud:docs/com-04-implementation.md; Cloud:storage/plans/** (only task-owned module/family plans, preserve owner declarations); Cloud:src/ArcForges.Cloud.Storage.D1/PlanManifest.g.cs (regenerate only); Cloud:worker/storage/plans.generated.ts (regenerate only); Cloud:src/ArcForges.Cloud.Modules.Abstractions/** (task-owned primitive production cross-owner ports, no duplicate wire schemas); Cloud:src/ArcForges.Cloud/Composition/** (append only real task-owned service/owner registration); Cloud:.dockerignore (task-owned source inclusion only); Cloud:src/ArcForges.Cloud.Storage.D1/Migrations/pending/** (new Commerce-prefixed additive migrations only; sequence allocated at merge); Cloud:src/ArcForges.Cloud.Storage.D1/Physical/manifest/commerce.json (owned Commerce schema manifest only); Cloud:src/ArcForges.Cloud.Modules.Commerce/** (only own purchase/inbox/ledger behavior, preserve Adapters/Catalogue owners); Cloud:src/ArcForges.Cloud.Storage.D1/Physical/PhysicalSchema.g.cs (regenerate only)
Shared resources (follow the owner protocol): RES-cloud-runbooks-and-fixtures (append): One file per runbook, monitor or provider fixture; indexes are append-only; recorded provider fixtures stay test-only.; RES-contract-consumer-pins (append): A consumer task updates the pin it needs through a reviewed dependency change to the exact published candidate containing its closure; no consumer pins an unpublished closure or references Contracts source.; RES-cloud-policy-inputs (append): Append only task-owned source/test bindings and immutable successor receipts. Rebase before integration; regenerate actual input hashes and plan manifests; chain from the receipt active on main; preserve all prior versions and records. This protocol admits no unreviewed coordinate, permission or runtime behavior changes.; RES-cloud-storage-plans (append): Each module owns its own plan directory; the plan-manifest hash is regenerated by the author after rebase and checked in CI.; RES-cloud-host-composition (append): Each module registers through its own module entry point and route fragment; the host composition only lists modules; route and binding conflicts are resolved by the integration owner at merge.; RES-cloud-d1-migrations (append): One global D1 migration sequence: each module task authors migrations under its module prefix; the integration owner assigns the global sequence number at merge, regenerates the plan manifest and rejects edits to merged migrations; the migrator applies in sequence with receipts.
Permitted substitutes (never real integration evidence): SUB-provider-event-fixtures: Recorded provider events drive inbox, idempotency and reconciliation tests; recorded cases remain regression inputs after live ingestion replaces runtime registration. Real producer ['COM.14']; removed by COM.14
Unblocks: COM.09, COM.11, COM.14

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline unit tests: duplicate, out-of-order, unsigned, unknown-product, replay, backlog-alert, convergence-from-point-in-time; deterministic fixture replay only, no live provider calls.
Completion evidence for the ledger: Convergence test reproducing identical commercial state from inbox replay; backlog alert firing test.
Notes: Webhook idempotency/ordering/signature correctness is named by SQ-08 as one of the two things that must be real before pricing is published; get this right before building ledgers/reconciliation on top.

2026-10-06 production-delivery repair (docs/decisions/production-delivery-2026-10-06.md). This amendment governs conflicting historical scope notes; preserve completed evidence, immutable history and package identities. Logical source paths are bound to actual existing projects, preserving namespace/package identities. New production behavior requires full contracts, logic, persistent adapters and feasible composition tests; unavailable provider/OS endpoints may be faked in component tests but never become deployed or commercial evidence. Root dependency/admission/lock changes require the exact published producer and a reviewed successor, not hash-only refresh.

2026-10-06 verified production follow-up (docs/decisions/production-delivery-followup-2026-10-06.md). This scoped amendment governs conflicting older path/model notes; preserve closed records, package identities and immutable history. EV-01/EI-01/EI-08 retain only an allowlisted lossless business/financial projection with exact original raw-byte SHA256/size and immutable verification receipt bound to canonical projection digest, stable verification key version, signature time and verification time. Bounded original bytes exist only ephemerally during signature verification. Durable quarantine/audit/export cannot contain instrument, credentials or arbitrary provider fields. Processing/replay validates integrity-protected projection, never claims original-signature reverification of redacted bytes; provider refetch/reconciliation has independent verified authority. Unknown/malformed events retain digest/size and safe refusal metadata only.
```

```text
Execute ArcForges delivery task COM.05 — Entitlement resolver.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\commerce.md (anchor task-com-05).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/com-05 (python tools/delivery.py claim COM.05 --worker <name>); task branch task/com-05 in Cloud; ledger record ledger/tasks/com-05.md.
Kind/size: service/L. Baseline: not-started.
Outcome: Immutable grants and revocations resolve deterministically into an entitlement snapshot with a per-capability reason and version, and rebuilding the snapshot from its grants/revocations always reproduces the stored snapshot.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-42.04 (the grant and revocation model, the resolver and the snapshot with per-capability reasons and version, with rebuild equivalence proven over the resolver's store port (the Commerce-facing grant interface in the shared Abstractions project, the GR-05 reason on the grant row, and the durable D1 store with its atomic snapshot commit are mapped to COM.16)): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\42-commerce-entitlement-and-credits.md, anchor rule-wp-42.04

Entry condition: adoption slice ADOPT.07.commerce is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- none
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Cloud:src/ArcForges.Cloud.Modules.Entitlement/Resolver/** (the real layout of the planned src/Cloud/ArcForges.Cloud.Modules.Entitlement/**/Resolver/**: the one Entitlement project CLOUD.02 creates, whose Domain, Application and Infrastructure layers are folders and namespaces; the resolver and the grant and revocation model are folders inside it); Cloud:src/ArcForges.Cloud.Modules.Entitlement/EntitlementModule.cs and Cloud:src/ArcForges.Cloud.Modules.Entitlement/ArcForges.Cloud.Modules.Entitlement.csproj (only the module's own Register entry point listing the resolver services, and InternalsVisibleTo for the existing test assembly so that no public method needs a public-API-to-test mapping; no package, reference or behavior change); Cloud:tests/ArcForges.Cloud.Tests/Entitlement/** and Cloud:tests/ArchitectureTests/** (resolver tests in the existing test projects; the architecture tests only for the reviewed project role and layering binding of the Entitlement project); Cloud:eng/policy/dependency-policy.json and Cloud:eng/policy/dependency-reviews/com-05-*.json (new immutable successor chained from the then-active receipt, only because hash-bound project and release inputs change; no coordinate, integrity value or closure entry changes); Cloud:eng/provenance/** (immutable successor release profile, Worker bundle and runtime-notice records only where an existing record binds an input this task changes, the first-party inventory files.json and the deterministic NOTICE.txt); Cloud:docs/entitlement-resolver.md (new, factual description of the resolver and its fixtures) and Cloud:AGENTS.md (only if the module description changes)
Shared resources (follow the owner protocol): RES-cloud-host-composition (append): Each module registers through its own module entry point and route fragment; the host composition only lists modules; route and binding conflicts are resolved by the integration owner at merge.; RES-cloud-policy-inputs (append): Append only task-owned source/test bindings and immutable successor receipts. Rebase before integration; regenerate actual input hashes and plan manifests; chain from the receipt active on main; preserve all prior versions and records. This protocol admits no unreviewed coordinate, permission or runtime behavior changes.
Unblocks: COM.06, COM.07, COM.08, COM.10, COM.11, COM.13, COM.14, COM.16, HAR.06, PLT.20, POL.04, SIM.07

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline unit tests: rebuild-equivalence over fixture accounts, reason-coverage, combination matrix over the four entitlement kinds, clock-determinism against an injected time source.
Completion evidence for the ledger: Rebuild-equivalence test result (snapshot-from-scratch equals stored snapshot) across fixture accounts.
Notes: BR-06 rebuild-equivalence is the core commerce invariant; COM.06/07/08/10/12 all read this resolver's snapshot, so its correctness gates a large share of downstream work.
```

```text
Execute ArcForges delivery task COM.06 — Distribution and enforcement.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\commerce.md (anchor task-com-06).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/com-06 (python tools/delivery.py claim COM.06 --worker <name>); task branch task/com-06 in Cloud; ledger record ledger/tasks/com-06.md.
Kind/size: service/M. Baseline: not-started.
Outcome: Entitlement is distributed with its version for client caching, realtime notification is only a refresh hint, offline staleness is bounded, all cost-bearing enforcement happens server-side, and losing entitlement never deletes local data.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-42.05 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\42-commerce-entitlement-and-credits.md, anchor rule-wp-42.05

Entry condition: adoption slice ADOPT.07.commerce is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] COM.05: EntitlementSnapshot + EntitlementVersion
- [artifact] CLOUD.23: typed-query/revision-precondition pattern
- [artifact] COM.16: the durable Entitlement store that holds the stored snapshot with its EntitlementVersion
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Cloud:src/ArcForges.Cloud.Modules.Entitlement/**/Distribution/**; Cloud:src/ArcForges.Cloud.Modules.Entitlement/**/Enforcement/**; Cloud:tests/ArcForges.Cloud.Tests/** (task-owned component tests only); Cloud:tests/worker/** (task-owned actual storage/adapter tests only); Cloud:tests/ArchitectureTests/** (exact owned API/layer bindings only); Cloud:eng/policy/dependency-policy.json (actual changed-input binding to a new immutable reviewed receipt); Cloud:eng/policy/dependency-reviews/com-06-*.json; Cloud:eng/provenance/** (only owned first-party and immutable input successors); Cloud:docs/com-06-implementation.md; Cloud:storage/plans/** (only task-owned module/family plans, preserve owner declarations); Cloud:src/ArcForges.Cloud.Storage.D1/PlanManifest.g.cs (regenerate only); Cloud:worker/storage/plans.generated.ts (regenerate only); Cloud:src/ArcForges.Cloud.Modules.Abstractions/** (task-owned primitive production cross-owner ports, no duplicate wire schemas); Cloud:src/ArcForges.Cloud/Composition/** (append only real task-owned service/owner registration); Cloud:.dockerignore (task-owned source inclusion only)
Shared resources (follow the owner protocol): RES-cloud-host-composition (append): Each module registers through its own module entry point and route fragment; the host composition only lists modules; route and binding conflicts are resolved by the integration owner at merge.; RES-contract-consumer-pins (append): A consumer task updates the pin it needs through a reviewed dependency change to the exact published candidate containing its closure; no consumer pins an unpublished closure or references Contracts source.; RES-cloud-policy-inputs (append): Append only task-owned source/test bindings and immutable successor receipts. Rebase before integration; regenerate actual input hashes and plan manifests; chain from the receipt active on main; preserve all prior versions and records. This protocol admits no unreviewed coordinate, permission or runtime behavior changes.; RES-cloud-storage-plans (append): Each module owns its own plan directory; the plan-manifest hash is regenerated by the author after rebase and checked in CI.
Unblocks: COM.15, PLT.20

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline tests: hint-not-authority, offline-staleness behavior, client-bypass negative, local-data-survival.
Completion evidence for the ledger: Client-bypass negative test result; local-data-survival result.
Notes: 

2026-10-06 production-delivery repair (docs/decisions/production-delivery-2026-10-06.md). This amendment governs conflicting historical scope notes; preserve completed evidence, immutable history and package identities. Logical source paths are bound to actual existing projects, preserving namespace/package identities. New production behavior requires full contracts, logic, persistent adapters and feasible composition tests; unavailable provider/OS endpoints may be faked in component tests but never become deployed or commercial evidence. Root dependency/admission/lock changes require the exact published producer and a reviewed successor, not hash-only refresh.
```

```text
Execute ArcForges delivery task COM.07 — Quota, usage and storage accounting.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\commerce.md (anchor task-com-07).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/com-07 (python tools/delivery.py claim COM.07 --worker <name>); task branch task/com-07 in Cloud; ledger record ledger/tasks/com-07.md.
Kind/size: service/L. Baseline: not-started.
Outcome: Quota (limit) and usage (measurement) live in separate stores keyed to the entitlement period, storage accounting matches committed objects exactly, and an exceeded quota produces a typed, explained refusal.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-42.06 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\42-commerce-entitlement-and-credits.md, anchor rule-wp-42.06

Entry condition: adoption slice ADOPT.07.commerce is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] CLOUD.07: the published capacity/quota kernel (Capacity and Container/D1 integration producer)
- [artifact] COM.05: versioned entitlement grants
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Cloud:src/Cloud/ArcForges.Cloud.Modules.Entitlement/**/Quota/**
Shared resources (follow the owner protocol): RES-cloud-host-composition (append): Each module registers through its own module entry point and route fragment; the host composition only lists modules; route and binding conflicts are resolved by the integration owner at merge.; RES-cloud-policy-inputs (append): Append only task-owned source/test bindings and immutable successor receipts. Rebase before integration; regenerate actual input hashes and plan manifests; chain from the receipt active on main; preserve all prior versions and records. This protocol admits no unreviewed coordinate, permission or runtime behavior changes.
Unblocks: COM.15, SIM.04, SIM.07

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline tests: race admissions, quota downgrade, repeated cancellation, GC timeout, period rollover with held old-period use, boundary-reset, accounting-vs-committed-storage comparison, refusal-message.
Completion evidence for the ledger: Accounting comparison result against actual committed storage; boundary-reset test result.
```

```text
Execute ArcForges delivery task COM.08 — Credits.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\commerce.md (anchor task-com-08).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/com-08 (python tools/delivery.py claim COM.08 --worker <name>); task branch task/com-08 in Cloud; ledger record ledger/tasks/com-08.md.
Kind/size: service/L. Baseline: not-started.
Outcome: Purchased (no-expiry) and compensation (disclosed-expiry) credit lots exist in integer micro-credits with funding order capacity to compensation to purchased, single-reservation-spans-both-pools accounting, reservation-expiry sweeping and a hard stop at zero with no floating point anywhere in the path.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-42.07 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\42-commerce-entitlement-and-credits.md, anchor rule-wp-42.07

Entry condition: adoption slice ADOPT.07.commerce is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] COM.05: entitlement kind determination (which grant authorises which credit class)
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Cloud:src/Cloud/ArcForges.Cloud.Modules.Entitlement/**/Credits/**
Shared resources (follow the owner protocol): RES-cloud-host-composition (append): Each module registers through its own module entry point and route fragment; the host composition only lists modules; route and binding conflicts are resolved by the integration owner at merge.; RES-cloud-policy-inputs (append): Append only task-owned source/test bindings and immutable successor receipts. Rebase before integration; regenerate actual input hashes and plan manifests; chain from the receipt active on main; preserve all prior versions and records. This protocol admits no unreviewed coordinate, permission or runtime behavior changes.
Unblocks: AIR.02, COM.12, COM.13

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline tests: lot-ordering matrix, concurrency (no-overdraft), reservation-expiry sweep, hard-stop, refund-hold, fixed-precision policy scan (no floating point).
Completion evidence for the ledger: Concurrency test showing no overdraft under concurrent reservation; fixed-precision scan result.
```

```text
Execute ArcForges delivery task COM.09 — Ledgers and reconciliation.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\commerce.md (anchor task-com-09).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/com-09 (python tools/delivery.py claim COM.09 --worker <name>); task branch task/com-09 in Cloud; ledger record ledger/tasks/com-09.md.
Kind/size: service/L. Baseline: not-started.
Outcome: The three ledgers exist as separate append-only stores with scheduled two-way provider reconciliation expressing repairs as new typed records, never edits, and divergence above threshold alerts.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-42.08 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\42-commerce-entitlement-and-credits.md, anchor rule-wp-42.08
- WP-42:p2-010-required-behavior-and-closure-thr P2-010 required behavior and closure; three ledgers with unresolved holds through their existing deadline (P2-010 required behavior and closure; three ledgers with unresolved holds through their existing deadline): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\42-commerce-entitlement-and-credits.md, package-level obligation
- WP-42:p2-010-required-behavior-and-closure P2-010 required behavior and closure (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\42-commerce-entitlement-and-credits.md, package-level obligation

Entry condition: adoption slice ADOPT.07.commerce is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] COM.03: Order/Payment records
- [artifact] COM.04: verified ProviderEvent stream
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Cloud:src/ArcForges.Cloud.Modules.Commerce/**/Ledgers/**; Cloud:src/ArcForges.Cloud.Modules.Commerce/**/Reconciliation/**; Cloud:tests/ArcForges.Cloud.Tests/** (task-owned component tests only); Cloud:tests/worker/** (task-owned actual storage/adapter tests only); Cloud:tests/ArchitectureTests/** (exact owned API/layer bindings only); Cloud:eng/policy/dependency-policy.json (actual changed-input binding to a new immutable reviewed receipt); Cloud:eng/policy/dependency-reviews/com-09-*.json; Cloud:eng/provenance/** (only owned first-party and immutable input successors); Cloud:docs/com-09-implementation.md; Cloud:storage/plans/** (only task-owned module/family plans, preserve owner declarations); Cloud:src/ArcForges.Cloud.Storage.D1/PlanManifest.g.cs (regenerate only); Cloud:worker/storage/plans.generated.ts (regenerate only); Cloud:src/ArcForges.Cloud.Modules.Abstractions/** (task-owned primitive production cross-owner ports, no duplicate wire schemas); Cloud:src/ArcForges.Cloud/Composition/** (append only real task-owned service/owner registration); Cloud:.dockerignore (task-owned source inclusion only); Cloud:src/ArcForges.Cloud.Storage.D1/Migrations/pending/** (new Commerce-prefixed additive migrations only; sequence allocated at merge); Cloud:src/ArcForges.Cloud.Storage.D1/Physical/manifest/commerce.json (owned Commerce schema manifest only); Cloud:src/ArcForges.Cloud.Modules.Commerce/** (only own purchase/inbox/ledger behavior, preserve Adapters/Catalogue owners); Cloud:src/ArcForges.Cloud.Storage.D1/Physical/PhysicalSchema.g.cs (regenerate only)
Shared resources (follow the owner protocol): RES-cloud-runbooks-and-fixtures (append): One file per runbook, monitor or provider fixture; indexes are append-only; recorded provider fixtures stay test-only.; RES-cloud-policy-inputs (append): Append only task-owned source/test bindings and immutable successor receipts. Rebase before integration; regenerate actual input hashes and plan manifests; chain from the receipt active on main; preserve all prior versions and records. This protocol admits no unreviewed coordinate, permission or runtime behavior changes.; RES-cloud-storage-plans (append): Each module owns its own plan directory; the plan-manifest hash is regenerated by the author after rebase and checked in CI.; RES-cloud-host-composition (append): Each module registers through its own module entry point and route fragment; the host composition only lists modules; route and binding conflicts are resolved by the integration owner at merge.; RES-cloud-d1-migrations (append): One global D1 migration sequence: each module task authors migrations under its module prefix; the integration owner assigns the global sequence number at merge, regenerates the plan manifest and rejects edits to merged migrations; the migrator applies in sequence with receipts.
Unblocks: CLOUD.63, COM.10, COM.14

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline tests: dropped-webhook repair, duplicated-order repair, provider-side-change repair, immutability (history cannot be edited), ledger-separation.
Completion evidence for the ledger: Dropped-webhook repair test recovering correct state without editing history; ledger-separation test.
Notes: 

2026-10-06 production-delivery repair (docs/decisions/production-delivery-2026-10-06.md). This amendment governs conflicting historical scope notes; preserve completed evidence, immutable history and package identities. Logical source paths are bound to actual existing projects, preserving namespace/package identities. New production behavior requires full contracts, logic, persistent adapters and feasible composition tests; unavailable provider/OS endpoints may be faked in component tests but never become deployed or commercial evidence. Root dependency/admission/lock changes require the exact published producer and a reviewed successor, not hash-only refresh.
```

```text
Execute ArcForges delivery task COM.10 — Refunds, disputes and evidence.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\commerce.md (anchor task-com-10).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/com-10 (python tools/delivery.py claim COM.10 --worker <name>); task branch task/com-10 in Cloud; ledger record ledger/tasks/com-10.md.
Kind/size: service/M. Baseline: not-started.
Outcome: A refund verifiably rolls entitlement back, dispute records are tracked, and a commercial evidence export covering order/payment/event/entitlement-history/usage for a period is complete, reproducible and free of payment-instrument data.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-42.09 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\42-commerce-entitlement-and-credits.md, anchor rule-wp-42.09

Entry condition: adoption slice ADOPT.07.commerce is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] COM.05: entitlement rollback path
- [artifact] COM.09: ledger entries to export
- [artifact] COM.16: the RevokeGrant side of the published grant port
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Cloud:src/Cloud/ArcForges.Cloud.Modules.Billing/**/Refunds/**
Shared resources (follow the owner protocol): RES-cloud-runbooks-and-fixtures (append): One file per runbook, monitor or provider fixture; indexes are append-only; recorded provider fixtures stay test-only.; RES-cloud-policy-inputs (append): Append only task-owned source/test bindings and immutable successor receipts. Rebase before integration; regenerate actual input hashes and plan manifests; chain from the receipt active on main; preserve all prior versions and records. This protocol admits no unreviewed coordinate, permission or runtime behavior changes.
Unblocks: CLOUD.66, COM.13, COM.14

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline tests: refund-with-rollback, evidence completeness/reproducibility, payment-data-absence scan.
Completion evidence for the ledger: Refund-with-rollback test result; payment-instrument-absence scan (zero hits) on the evidence export.
```

```text
Execute ArcForges delivery task COM.11 — Service term interval model.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\commerce.md (anchor task-com-11).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/com-11 (python tools/delivery.py claim COM.11 --worker <name>); task branch task/com-11 in Cloud; ledger record ledger/tasks/com-11.md.
Kind/size: service/L. Baseline: not-started.
Outcome: entitlement.service_term exists as an interval keyed on (kind, period_ref) with subscription_ref stable across renewals, a renewal always creating a new period_ref row, a replayed provider event extending nothing twice, and a plan change superseding rather than editing.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-42.11 (service_term interval model keyed on (kind, period_ref); the three separated identities (subscription_ref stable / period_ref per paid interval / provider-event dedup in commerce.provider_event); union-of-overlap effective term; plan-change supersede. Capacity bucket/refill/reservation half split to COM.12.): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\42-commerce-entitlement-and-credits.md, anchor rule-wp-42.11

Entry condition: adoption slice ADOPT.07.commerce is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] COM.03: paid period identifiers (checkout/order confirmation producing a period_ref-worthy paid interval)
- [artifact] COM.05: offer assignment and entitlement kind
- [artifact] COM.04: deduplicated ProviderEvent stream
- [artifact] COM.16: the widened append path of the durable Entitlement store for service terms and term actions, with its D1 plans
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Cloud:src/Cloud/ArcForges.Cloud.Modules.Entitlement/**/ServiceTerm/**
Shared resources (follow the owner protocol): RES-cloud-host-composition (append): Each module registers through its own module entry point and route fragment; the host composition only lists modules; route and binding conflicts are resolved by the integration owner at merge.; RES-cloud-policy-inputs (append): Append only task-owned source/test bindings and immutable successor receipts. Rebase before integration; regenerate actual input hashes and plan manifests; chain from the receipt active on main; preserve all prior versions and records. This protocol admits no unreviewed coordinate, permission or runtime behavior changes.
Unblocks: COM.12

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline tests: renewal creating a second term row without violating the (kind,period_ref) key, replayed event creating nothing, plan change superseding not editing, overlap/genuine-gap union-of-interval tests.
Completion evidence for the ledger: Renewal-without-key-violation test; replay-creates-nothing test; supersede-not-edit test.
```

```text
Execute ArcForges delivery task COM.12 — Replenishing capacity bucket, refill and admission.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\commerce.md (anchor task-com-12).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/com-12 (python tools/delivery.py claim COM.12 --worker <name>); task branch task/com-12 in Cloud; ledger record ledger/tasks/com-12.md.
Kind/size: service/XL. Baseline: not-started.
Outcome: The capacity bucket refills by a per-period saturating accrual independent of evaluation frequency, backed by a monotonic durable watermark and exact rational carry, never claws back on a ceiling reduction, initialises exactly once per contiguous run, and admission is atomic with the service-term check first, committing before dispatch.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-42.11 (entitlement.capacity_bucket refill algorithm (§7.2), capacity_policy_period history, capacity_reservation with three funding sources, idempotent once-per-contiguous-run initialisation, and atomic admission with the service-term check first): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\42-commerce-entitlement-and-credits.md, anchor rule-wp-42.11

Entry condition: adoption slice ADOPT.07.commerce is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] COM.11: service_term interval and (kind,period_ref) rows
- [artifact] COM.08: CreditReservation reserve/settle/release primitive
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Cloud:src/Cloud/ArcForges.Cloud.Modules.Entitlement/**/Capacity/**
Shared resources (follow the owner protocol): RES-cloud-host-composition (append): Each module registers through its own module entry point and route fragment; the host composition only lists modules; route and binding conflicts are resolved by the integration owner at merge.; RES-cloud-policy-inputs (append): Append only task-owned source/test bindings and immutable successor receipts. Rebase before integration; regenerate actual input hashes and plan manifests; chain from the receipt active on main; preserve all prior versions and records. This protocol admits no unreviewed coordinate, permission or runtime behavior changes.
Unblocks: AIR.02, COM.14, HAR.02, SIM.07

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline deterministic tests only (no wall-clock sleep): full-hold-then-consume-then-read fixture, fractional saturation, changed plan, overlap, genuine gap, unchanged renewal, grandfathered above-ceiling balance, the CT-13 refill fixture (identical result whether refill runs once or a thousand times over an interval containing a ceiling raise, reduction and rate change, asserting 11 at t=11), clock rollback/restart/reconnect/second-device/racing-replica watermark tests, ceiling-reduction-preserves-held-funding test, ledger-unit-separation test (customerCredit carries micro-credits with no currency; the other two carry money with currency; no query sums them).
Completion evidence for the ledger: The CT-13 refill fixture result exactly (11 at t=11, not 21 or 12); watermark non-rewind evidence across restart/second-device/racing-replica; ceiling-reduction-preserves-funding result.
Notes: The single most algorithmically risky unit in this area (§7.2 saturating accrual with exact rational carry); named as the PG-13/PG-16 producer that must close before WP-42.10 despite its higher substep number. Consider a narrow property-based-test spike on the refill function ahead of the full admission integration.
```

```text
Execute ArcForges delivery task COM.13 — Operator financial-owner proposal/approval operations.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\commerce.md (anchor task-com-13).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/com-13 (python tools/delivery.py claim COM.13 --worker <name>); task branch task/com-13 in Cloud; ledger record ledger/tasks/com-13.md.
Kind/size: service/L. Baseline: not-started.
Outcome: The financial-owner operator RPCs (grant/revokeGrant/issueCredit/adjustCredit/refund) are implemented exactly once against the registry04 §9 typed proposal/approval protocol with all eight authorization fields, refusing public customer/PAT/agent access, and one approved proposal cannot execute twice.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-42:operator-contract-closure-financial-owne Operator contract closure — financial owners (grant/revokeGrant/issueCredit/adjustCredit/refund) (operator contract closure; financial-owner RPC implementations: grant, revokeGrant, issueCredit, adjustCredit, refund): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\42-commerce-entitlement-and-credits.md, package-level obligation

Entry condition: adoption slice ADOPT.07.commerce is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [contract] CON.14: the OperatorService full RPC surface (ProposeAction/ApproveAction/execute, grant/revokeGrant/issueCredit/adjustCredit/refund message shapes, eight authorization fields, negative vectors) per registry04 §9
- [artifact] CLOUD.21: real identity/dispatch conformance for operator calls
- [artifact] COM.05: grant/revocation model
- [artifact] COM.08: credit lot issue/adjust primitives
- [artifact] COM.10: refund/rollback path
- [artifact] COM.16: the IssueGrant and RevokeGrant port carrying the GR-05 reason
Completion prerequisites (may start earlier; cannot complete before these are complete):
- [integration] OPS.13: the operator console UI actually calling these RPCs end-to-end

Permitted write scope: Cloud:src/Cloud/ArcForges.Cloud.Modules.Billing/**/Operator/**; Cloud:src/Cloud/ArcForges.Cloud.Modules.Entitlement/**/Operator/**
Shared resources (follow the owner protocol): RES-cloud-host-composition (append): Each module registers through its own module entry point and route fragment; the host composition only lists modules; route and binding conflicts are resolved by the integration owner at merge.; RES-contracts-schema-sources (append): Each schema closure task edits only its own domain proto or HTTP-schema files and adds its own sharded constraint and fixture files. Schema-closure tasks and Contracts policy tasks that touch package/access/provenance/dependency input registries share this append/rebase protocol: append only task-owned rows and successor receipts to package, compiled access/hash, foundation, operation, constraint, provenance source/output, binding, and dependency-review inventories; preserve prior history and never rewrite another task's rows. Refresh dependency input hashes only for the task-owned closure; do not expand dependency versions or closure except for the two exact task-specific exceptions below. One narrow exception applies only to CON.14: it may add the single ArcForges.Contracts.CloudInternal → existing ArcForges.Contracts.PublicApi package/project edge required for generated OperatorService imports to resolve to their canonical owner, implemented only by one ProjectReference in the CloudInternal csproj, its existing packages.lock.json, and the CloudInternal dependency row in eng/contract-packages.json. This expands only CloudInternal's package-specific closure to include the existing PublicApi package and its existing same-version transitive realization; the lock may add the PublicApi project and already-pinned Grpc.Core.Api 2.84.0, while existing Foundation and Google.Protobuf 3.36.1 entries retain their versions and hashes. The exception permits only the matching exact input-hash refreshes and immutable con-14-r1 successor chained from active con-22-r1. Preserve the aggregate dependency coordinate/version set, package IDs and licences, every other package's dependency usage/closure, Foundation/PublicApi ownership, all prior receipt history, and the PublicApi 1.0.0-ci.113.1 PreviousClient-only fixture classification. A second, CON.11-only exception permits only the already-authorized Events → PublicApi and CloudInternal → Events/PublicApi project references to realize in Events and CloudInternal as the corresponding first-party Project lock entries plus the exact centrally pinned Grpc.Core.Api CentralTransitive row: requested [2.84.0, ), resolved 2.84.0, contentHash p2SOMl6q/GZ4/5MLkgboC/z55g4zKUEruRn/g46QgppjQBVnsLZVBU/9VO7n60ll38G3Eo8Zu9b7x+W01GKFVg==. Only the five existing consumer lockfiles tests/StructureTests/packages.lock.json, tests/public/SerializationProbe/packages.lock.json, src/public/dotnet/ArcForges.Sdk.Client/packages.lock.json, src/public/dotnet/ArcForges.Cli/packages.lock.json, and src/public/dotnet/ArcForges.Contracts.Validation/packages.lock.json may add ArcForges.Contracts.PublicApi [1.0.0-ci.0.0, ) to the existing ArcForges.Contracts.Events Project.dependencies field, exactly as SDK restore requires. In only tests/StructureTests/packages.lock.json and tests/public/SerializationProbe/packages.lock.json, SDK restore may also add ArcForges.Contracts.Events and ArcForges.Contracts.PublicApi [1.0.0-ci.0.0, ) to the existing ArcForges.Contracts.CloudInternal Project.dependencies field, exactly as the already-authorized CloudInternal -> Events/PublicApi project references require; no other field, package/project entry, project dependency, target framework, version, hash, or consumer behavior changes. This exception permits only these matching task-owned lock/policy input-hash refreshes and the immutable con-11-r1 successor, and preserves the aggregate coordinate/version/licence union, all other package usage/closures, existing Foundation, Google.Protobuf and Microsoft.NET.ILLink.Tasks rows, previous receipt history, package identities and the PreviousClient-only fixture classification. No direct package reference, PrivateAssets or asset override, other coordinate/version/hash, project, lock row, licence exception or dependency algorithm change is authorized; all other tasks retain the no-closure-expansion rule. Public Kotlin/Dokka successors are exclusively governed by RES-contracts-dokka-profile. A proto file with several contributing tasks (operator, policy/configuration) has one designated author task and the others request changes through it. Each serialized merge is followed by a rebase and regeneration before integration of the next task.; RES-cloud-policy-inputs (append): Append only task-owned source/test bindings and immutable successor receipts. Rebase before integration; regenerate actual input hashes and plan manifests; chain from the receipt active on main; preserve all prior versions and records. This protocol admits no unreviewed coordinate, permission or runtime behavior changes.
Unblocks: CLOUD.64, OPS.05, OPS.13

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline tests: distinct approver, stale hash/revision/configuration, role revocation, expiry, concurrent consumption, lost receipt, double-execution-of-one-approval, no-direct-SQL/public-SDK-import architecture test.
Completion evidence for the ledger: Double-execution negative result (one approved proposal cannot execute twice); public-customer/PAT/agent refusal result for every method.
```

```text
Execute ArcForges delivery task COM.14 — Technical commerce closure and live-gate staging.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\commerce.md (anchor task-com-14).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/com-14 (python tools/delivery.py claim COM.14 --worker <name>); task branch task/com-14 in Cloud; ledger record ledger/tasks/com-14.md.
Kind/size: service/L. Baseline: not-started.
Outcome: Deterministic provider normalization and the full sandbox lifecycle are proven with synthetic and Paddle/Payoneer-sandbox vectors, SubscriptionState exactly matches requirements-04, plan changes start next term without proration, and the live-payment/payout/refund/merchant gates are explicitly preserved as pending for WP50.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-42.10 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\42-commerce-entitlement-and-credits.md, anchor rule-wp-42.10
- WP-42:p2-010-required-behavior-and-closure P2-010 required behavior and closure (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\42-commerce-entitlement-and-credits.md, package-level obligation

Entry condition: adoption slice ADOPT.07.commerce is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] COM.12: passing durable term/capacity/refill state (WP-42.11 evidence)
- [artifact] COM.03: purchase pipeline end to end
- [artifact] COM.04: event inbox end to end
- [artifact] COM.05: entitlement resolver end to end
- [artifact] COM.09: ledgers and reconciliation end to end
- [artifact] COM.10: refund path end to end
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Cloud:tests/CloudIntegrationTests/Commerce/**; Cloud:src/Cloud/ArcForges.Cloud.Modules.Billing/**
Shared resources (follow the owner protocol): RES-cloud-runbooks-and-fixtures (append): One file per runbook, monitor or provider fixture; indexes are append-only; recorded provider fixtures stay test-only.; RES-cloud-policy-inputs (append): Append only task-owned source/test bindings and immutable successor receipts. Rebase before integration; regenerate actual input hashes and plan manifests; chain from the receipt active on main; preserve all prior versions and records. This protocol admits no unreviewed coordinate, permission or runtime behavior changes.
Unblocks: COM.15, WEB.14, WEB.29

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Recorded Paddle/Payoneer sandbox scenario vectors (no-term, cancellation, lost result, unknown exposure, future-effective changes) plus synthetic fixtures; per P2-017 this acceptance-level sandbox evidence stays outside routine CI (manual/scheduled), while regression-level assertions stay in offline CI.
Completion evidence for the ledger: Full synthetic/sandbox ledger vector results; activation checklist document handed to WP48/WP50; explicit statement that VG-10/VG-11/VG-12/L-30 remain open.
Notes: Completion explicitly does not require WP48 (account portal) or WP50 (real go-live); this task closes the technical/test-mode gate only (PG-10) and stages the activation checklist. Real checkout/payout evidence and VG-10/VG-11/VG-12/L-30 stay with WP50 per WP-42 §8.11. Retires SUB-provider-event-fixtures and SUB-hosted-checkout-sandbox.
```

```text
Execute ArcForges delivery task COM.15 — Owned-artifact receipt and closure.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\commerce.md (anchor task-com-15).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/com-15 (python tools/delivery.py claim COM.15 --worker <name>); task branch task/com-15 in Cloud; ledger record ledger/tasks/com-15.md.
Kind/size: service/S. Baseline: not-started.
Outcome: The package-level owned-artifact/real-integration receipt is recorded (source commit, producer version, candidate hashes, actual runtime/provider, scenario, result, real-vs-fixture status) and the P2-010 active-Pass/subscription-exclusivity and ledger-hold-deadline vectors pass.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-42.90 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\42-commerce-entitlement-and-credits.md, anchor rule-wp-42.90
- WP-42:p2-010-required-behavior-and-closure-act P2-010 required behavior and closure; active Pass/subscription mutual exclusion, no immediate proration, exact renewal/reset periods (P2-010 required behavior and closure; active Pass/subscription mutual exclusion, no immediate proration, exact renewal/reset periods): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\42-commerce-entitlement-and-credits.md, package-level obligation
- WP-42:p2-010-required-behavior-and-closure P2-010 required behavior and closure (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\42-commerce-entitlement-and-credits.md, package-level obligation

Entry condition: adoption slice ADOPT.07.commerce is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] COM.14: technical commerce closure results to attach to the receipt
- [artifact] COM.06: package task delivered
- [artifact] COM.07: package task delivered
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Cloud:eng/provenance/records/**
Shared resources (follow the owner protocol): RES-cloud-policy-inputs (append): Append only task-owned source/test bindings and immutable successor receipts. Rebase before integration; regenerate actual input hashes and plan manifests; chain from the receipt active on main; preserve all prior versions and records. This protocol admits no unreviewed coordinate, permission or runtime behavior changes.
Unblocks: REL.06, REL.08

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Aggregation only: existing concurrent admission/idempotent settlement/reversal/storage-accounting cases re-asserted at the candidate closure; no new test logic.
Completion evidence for the ledger: The owned-artifact/real-integration receipt itself, with inapplicable fields explicitly marked.
```

```text
Execute ArcForges delivery task COM.16 — Entitlement grant port and durable Entitlement store.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\commerce.md (anchor task-com-16).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/com-16 (python tools/delivery.py claim COM.16 --worker <name>); task branch task/com-16 in Cloud; ledger record ledger/tasks/com-16.md.
Kind/size: service/L. Baseline: not-started.
Outcome: Commerce, the operator path and the refund path reach Entitlement only through one published IssueGrant/RevokeGrant port that lives in ArcForges.Cloud.Modules.Abstractions and is implemented by the Entitlement module (EO-03, MD-03), so no module references Entitlement internals or writes its tables; an administrative, compensation or migration grant carries its reason on the grant row (GR-05); and the Entitlement module has its production D1 store: grants, revocations, service terms, term actions, definitions activations, workspace status facts and the derived snapshot (the whole resolver output) are appended and replaced in one guarded named plan under the workspace revision together with the owner receipt and notification outbox row, so a grant or term never exists without the snapshot and EntitlementVersion that reflect it, a stale writer commits nothing, and the snapshot rebuilt from the D1-stored records equals the stored snapshot. The Entitlement store reaches D1 only through a generic plan-execution port that this task creates in ArcForges.Cloud.Modules.Abstractions (outside the Entitlement folder, so every later module reuses it) and a Storage.D1 adapter that implements it over the signed Worker executor; an Entitlement plan names only entitlement_ and platform_ tables. The port commits on its own; joining the same grant statements to the enumerated purchase unit of work is the Entitlement participation of CLOUD.63.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-42.04 (the Commerce-facing grant interface (EO-03: IssueGrant and RevokeGrant as a public port in the shared Abstractions project, implemented by the Entitlement module), the GR-05 reason carried on the grant row, and the durable D1 Entitlement store: grants, revocations, service terms and term actions committed atomically with the snapshot and its EntitlementVersion under one guarded plan, with rebuild equivalence over D1-stored records (the resolver, its rules and its in-memory-store rebuild equivalence are COM.05)): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\42-commerce-entitlement-and-credits.md, anchor rule-wp-42.04

Entry condition: adoption slice ADOPT.07.commerce is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] COM.05: the grant and revocation model, the EntitlementService admission rules and the IEntitlementStore port contract
- [artifact] CLOUD.03: the physical entitlement tables (grant with its reason column, revocation, revision, snapshot, service_term and service_term_action), their append-only triggers and the typed bind/result adapters
- [artifact] CLOUD.04: the owner receipt and notification outbox rows of a guarded write
- [artifact] CLOUD.06: the guarded-batch executor and its revision guard primitive with the SU-04 module order
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Cloud:src/ArcForges.Cloud.Modules.Abstractions/Entitlement/** (new and public: the IssueGrant and RevokeGrant port with its request, result and refusal types, built from primitives only and referencing no module and no Entitlement internal type; cross-module ports belong to this shared boundary project (architecture 01 section 5, MD-03); no change to IModuleBoundary or ModuleDescriptor; the generic plan-execution port is not part of this folder: see Abstractions/Storage/**); Cloud:src/ArcForges.Cloud.Modules.Abstractions/Storage/** (new and public: the generic plan-execution port, a named plan id with exact typed parameters in, typed rows or a typed refusal out, that a module project may use because a module references only this project and never the storage layer; it names no table, no SQL and no module; CLOUD.02 published none, and CLOUD.04 and CLOUD.06 write only inside Storage.D1 and so cannot publish one); Cloud:src/ArcForges.Cloud.Storage.D1/ModuleBinding/** and Cloud:src/ArcForges.Cloud.Storage.D1/ArcForges.Cloud.Storage.D1.csproj (new folder owned by this task, no overlap with the Migrations, Physical, Receipts, Outbox or SharedFamilies folders of CLOUD.03, CLOUD.04 and CLOUD.06: the adapter that implements the Abstractions plan-execution port over the existing signed Worker executor and refuses a plan id whose owner is not the caller's module descriptor; the project file only for the project reference to Abstractions; later module tasks reuse the adapter and add nothing here); Cloud:src/ArcForges.Cloud.Modules.Entitlement/** except Resolver/Domain (the port adapter over EntitlementService that carries the reason, the widened EntitlementAppend that also carries service terms and term actions, the D1 IEntitlementStore under Persistence/** written against the Abstractions plan-execution port, and the module's own Register entry listing them; the resolver rules, rebuild semantics and admission rules of COM.05 are unchanged); Cloud:storage/plans/entitlement/** and the generated plan manifest in Cloud:src/ArcForges.Cloud.Storage.D1/PlanManifest.g.cs (the Entitlement module's named plans as owner entitlement, naming only entitlement_ and platform_ tables (CM-01 to CM-03); the manifest hash is regenerated by the author after rebase; RES-cloud-storage-plans); Cloud:src/ArcForges.Cloud.Storage.D1/Migrations/** (one append-only expand migration under Migrations/pending that creates the three new entitlement tables with their append-only triggers and any index the plans need; numbered at merge by the integration owner; RES-cloud-d1-migrations); Cloud:src/ArcForges.Cloud.Storage.D1/Physical/manifest/entitlement.json and Cloud:src/ArcForges.Cloud.Storage.D1/Physical/PhysicalSchema.g.cs (the Entitlement module's own manifest file, only the three new tables with their inline enum, and the regenerated column maps, hash and migration identity; no other owner's manifest changes; RES-cloud-d1-migrations); Cloud:worker/storage/plans.generated.ts, Cloud:tests/worker/**, Cloud:eng/verification/d1-entitlement-local.ts and the script entry for it in Cloud:package.json (the regenerated Worker plan dictionary; the Entitlement plan and migration tests on the SQLite oracle and the counts and pins the physical-schema tests assert for the three new tables; the explicit local opt-in run on workerd's D1 for the atomic commit and the concurrent writers, never CI); Cloud:src/**/packages.lock.json and Cloud:tests/**/packages.lock.json (only the project-reference entries that the new Storage.D1 reference to the Abstractions project adds; no package coordinate or integrity value changes); Cloud:docs/d1-physical-schema.md, Cloud:docs/d1-receipts-outbox.md and Cloud:CONTRIBUTING.md (only the table counts, the stated limit that no module owns a tail-carrying plan yet, and the opt-in local command this task changes); Cloud:src/ArcForges.Cloud/Composition/HostModules.cs (only the append that binds the Storage.D1 ModuleBinding adapter to the Abstractions plan-execution port, and the Entitlement store to the Entitlement port, by composition; RES-cloud-host-composition); Cloud:tests/ArcForges.Cloud.Tests/Entitlement/** and Cloud:tests/ArchitectureTests/** (port contract tests and store tests; the architecture tests only to assert that Commerce reaches Entitlement only through the Abstractions port and that the Abstractions project references no module); Cloud:eng/policy/dependency-policy.json and Cloud:eng/policy/dependency-reviews/com-16-*.json (new immutable successor chained from the then-active receipt, only because hash-bound project and release inputs change; no coordinate, integrity value or closure entry changes); Cloud:eng/provenance/** (immutable successor release profile, Worker bundle and runtime-notice records only where an existing record binds an input this task changes, the first-party inventory files.json and the deterministic NOTICE.txt); Cloud:docs/entitlement-resolver.md (the port, the reason column and the store replace the stated limits it records), Cloud:docs/storage-plans.md (the entitlement owner) and Cloud:AGENTS.md (only if the module description changes)
Shared resources (follow the owner protocol): RES-cloud-host-composition (append): Each module registers through its own module entry point and route fragment; the host composition only lists modules; route and binding conflicts are resolved by the integration owner at merge.; RES-cloud-storage-plans (append): Each module owns its own plan directory; the plan-manifest hash is regenerated by the author after rebase and checked in CI.; RES-cloud-d1-migrations (append): One global D1 migration sequence: each module task authors migrations under its module prefix; the integration owner assigns the global sequence number at merge, regenerates the plan manifest and rejects edits to merged migrations; the migrator applies in sequence with receipts.; RES-cloud-policy-inputs (append): Append only task-owned source/test bindings and immutable successor receipts. Rebase before integration; regenerate actual input hashes and plan manifests; chain from the receipt active on main; preserve all prior versions and records. This protocol admits no unreviewed coordinate, permission or runtime behavior changes.
Unblocks: CLOUD.16, CLOUD.21, CLOUD.63, CLOUD.72, COM.02, COM.04, COM.06, COM.10, COM.11, COM.13

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline unit tests: port contract (idempotent replay by source reference, stale-version refusal, reason required for administrative, compensation and migration grants, no Entitlement type crosses the port), store tests through the plan-bridge fakes and the physical column map (atomic append and snapshot replace, a stale revision commits nothing, concurrent writers, append-only enforcement, reason round trip), rebuild equivalence over D1-stored fixture records, architecture tests for the Commerce-to-Entitlement path; opt-in local runtime run against a real D1 instance for the atomic commit and the concurrent-writer case per docs/validation-policy.md; no hosted runtime, live-service or browser CI (P2-017).
Completion evidence for the ledger: Port contract and architecture test results; the D1 atomic-commit, stale-revision and concurrent-writer results (the local D1 run recorded once, or recorded as untested); rebuild-equivalence result over D1-stored records; reason round-trip result; source commit.
Notes: Added by the COM.05 review finding that nothing owned the EO-03 port, the GR-05 reason column or the D1 IEntitlementStore. Decisions: the port type lives in Abstractions (Commerce cannot reference the Entitlement project); the reason column is a model 01 correction made by the planning pair that added this task and is mapped by the CLOUD.03 manifest; the D1 store is the Entitlement module's own persistence (module owners own their plans, architecture 01 section 5), not CLOUD.63, which joins the same statements to the shared families once Commerce exists. Plan execution: a module project references only Abstractions (docs/storage-plans.md), so this task creates the generic plan-execution port in Abstractions/Storage/** and its adapter in Storage.D1/ModuleBinding/**, and an Entitlement plan may name only entitlement_ and platform_ tables. Revision guard: the per-workspace revision COM.05's port commits under is held in the new Entitlement-owned table entitlement.revision (model 01, added by the planning pair that added this task), never in a workspace_ table, and every Entitlement commit guards and increments it in the same batch. The persistence of the workspace status facts, feature releases and definitions activations that COM.05's record set reads is settled by the planning pair that amended model 01 for COM.16 (never decided in code, D-001, ADP-07): three new append-only Entitlement-owned records, entitlement.definitions_activation, entitlement.workspace_status_fact and entitlement.feature_release, so the whole record set of a snapshot lives in entitlement_ tables; workspace.state and the commerce.subscription fields stay owned by their modules, only the Entitlement module appends to the three records, and trust and safety (status facts) and configuration (feature releases) reach it through ports their own tasks add, so COM.16 stores, reads and tests the records and publishes no port for them. The entitlement.snapshot row holds the whole resolver output (model 01 gives the shapes of its three json columns), so rebuild equivalence is a comparison of the stored row with a rebuild from the stored records. Revision fence: the guard reads an absent entitlement.revision row as revision 0 and the first commit of a workspace creates the row with an insert that cannot overwrite an existing one, so two concurrent first commits cannot both succeed. The service terms and term actions a later owner appends (COM.11) travel through the same widened append as complete rows, so a term row and its action carry every column of model 01.
```
