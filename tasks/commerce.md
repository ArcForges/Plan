# ArcForges delivery task prompts — Commerce, entitlement and credits

Generated from Design `docs/planning/delivery/delivery-graph.json` by `tools/delivery.py`; do not edit by hand.
Each block is self-contained. Claim a task only when `python tools/delivery.py ready` lists it, with
`python tools/delivery.py claim <TASK-ID> --worker <name>`, then follow `arcforges-implementation.md`.
Tasks are ordered by lane for reading; the order is not a schedule.

## Commerce, entitlement and credits

```text
Execute ArcForges delivery task COM.01 — Provider adapter boundary.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\commerce.md (anchor task-com-01).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/com-01 (python tools/delivery.py claim COM.01 --worker <name>); task branch task/com-01 in Cloud; ledger record ledger/tasks/com-01.md.
Kind/size: service/S. Baseline: not-started.
Outcome: A provider-agnostic adapter boundary exists in Billing with a typed capability description; no provider type/identifier/webhook shape appears outside it, enforced by an architecture test.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-42.00 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\42-commerce-entitlement-and-credits.md, anchor rule-wp-42.00

Entry condition: adoption slice ADOPT.07.commerce is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- none
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Cloud:src/Cloud/ArcForges.Cloud.Modules.Billing/**/Adapter/**; Cloud:tests/CloudIntegrationTests/Commerce/Adapter/**
Permitted substitutes (never real integration evidence): SUB-provider-adapter-fixture: containment (no provider type leaks) and capability-driven branching in isolation Real producer ['COM.14']; removed by COM.14
Unblocks: COM.03, COM.04

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline architecture test (dependency-direction scan) + unit tests under P2-017; no live provider network calls in CI.
Completion evidence for the ledger: Architecture-test pass log naming the forbidden-leakage scan; capability-driven behavior test results for at least one absent capability.
```

```text
Execute ArcForges delivery task COM.02 — Catalogue and versioned policy.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\commerce.md (anchor task-com-02).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/com-02 (python tools/delivery.py claim COM.02 --worker <name>); task branch task/com-02 in Cloud; ledger record ledger/tasks/com-02.md.
Kind/size: service/M. Baseline: not-started.
Outcome: Offers, prices and policy versions exist as effective-dated policy data with no commercial figure compiled into code, and historical orders are immune to later price changes.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-42.01 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\42-commerce-entitlement-and-credits.md, anchor rule-wp-42.01

Entry condition: adoption slice ADOPT.07.commerce is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- none
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Cloud:src/Cloud/ArcForges.Cloud.Modules.Catalog/**
Permitted substitutes (never real integration evidence): SUB-commercial-figure-proposal: Proposed figures exercise the configured paths only; approval under D-020 and commercial activation are release evidence. Real producer ['REL.08']; removed by REL.08
Unblocks: COM.03

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline unit tests: retroactivity negative test, policy-version resolution test, static scan asserting no commercial constant compiled into code (P2-017 static-check class).
Completion evidence for the ledger: Retroactivity negative test result; compiled-constant scan result (zero hits).
```

```text
Execute ArcForges delivery task COM.03 — Purchase pipeline.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\commerce.md (anchor task-com-03).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/com-03 (python tools/delivery.py claim COM.03 --worker <name>); task branch task/com-03 in Cloud; ledger record ledger/tasks/com-03.md.
Kind/size: service/L. Baseline: not-started.
Outcome: Purchase intent is the idempotency anchor for hosted checkout; one intent yields at most one order, a forged redirect grants nothing, and every checkout attempt carries complete internal metadata with no payment-instrument field anywhere in ArcForges.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-42.02 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\42-commerce-entitlement-and-credits.md, anchor rule-wp-42.02

Entry condition: adoption slice ADOPT.07.commerce is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] COM.01: provider adapter's hosted-checkout port and capability description
- [artifact] COM.02: Offer/Price/PriceVersion read model
- [artifact] CLOUD.24: public API idempotency-key/rate-limiting primitive
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Cloud:src/Cloud/ArcForges.Cloud.Modules.Billing/**/Purchase/**; Cloud:src/Contracts/Public/ArcForges.Contracts.PublicApi.Commerce/**
Shared resources (follow the owner protocol): RES-contract-consumer-pins (append): A consumer task updates the pin it needs through a reviewed dependency change to the exact published candidate containing its closure; no consumer pins an unpublished closure or references Contracts source.
Permitted substitutes (never real integration evidence): SUB-hosted-checkout-sandbox: internal metadata completeness and redirect-forgery rejection against a scripted/sandbox redirect Real producer ['COM.14']; removed by REL.08
Unblocks: COM.04, COM.09, COM.11, COM.14

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline unit/integration tests: double-submission, redirect-forgery negative, metadata-completeness, expired-attempt reconciliation; no live Paddle calls in CI (sandbox calls stay in manual/scheduled acceptance per P2-017).
Completion evidence for the ledger: Double-submission test producing exactly one order; redirect-forgery negative result; metadata-completeness assertion.
```

```text
Execute ArcForges delivery task COM.04 — Provider event inbox.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\commerce.md (anchor task-com-04).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/com-04 (python tools/delivery.py claim COM.04 --worker <name>); task branch task/com-04 in Cloud; ledger record ledger/tasks/com-04.md.
Kind/size: service/L. Baseline: not-started.
Outcome: Every provider event is persisted before processing, signature-verified, deduplicated, and processed through the fixed eight-step verification chain, with quarantine and alerting for unprocessable events and idempotent full-inbox replay.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-42.03 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\42-commerce-entitlement-and-credits.md, anchor rule-wp-42.03

Entry condition: adoption slice ADOPT.07.commerce is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] COM.01: adapter signature-verification capability and typed event shape
- [artifact] COM.03: CheckoutAttempt/Order identifiers to correlate events against
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Cloud:src/Cloud/ArcForges.Cloud.Modules.Billing/**/Inbox/**; Cloud:fixtures/provider/**
Shared resources (follow the owner protocol): RES-cloud-runbooks-and-fixtures (append): One file per runbook, monitor or provider fixture; indexes are append-only; recorded provider fixtures stay test-only.; RES-contract-consumer-pins (append): A consumer task updates the pin it needs through a reviewed dependency change to the exact published candidate containing its closure; no consumer pins an unpublished closure or references Contracts source.
Permitted substitutes (never real integration evidence): SUB-provider-event-fixtures: Recorded provider events drive inbox, idempotency and reconciliation tests; recorded cases remain regression inputs after live ingestion replaces runtime registration. Real producer ['COM.14']; removed by COM.14
Unblocks: COM.09, COM.11, COM.14

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline unit tests: duplicate, out-of-order, unsigned, unknown-product, replay, backlog-alert, convergence-from-point-in-time; deterministic fixture replay only, no live provider calls.
Completion evidence for the ledger: Convergence test reproducing identical commercial state from inbox replay; backlog alert firing test.
Notes: Webhook idempotency/ordering/signature correctness is named by SQ-08 as one of the two things that must be real before pricing is published; get this right before building ledgers/reconciliation on top.
```

```text
Execute ArcForges delivery task COM.05 — Entitlement resolver.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\commerce.md (anchor task-com-05).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/com-05 (python tools/delivery.py claim COM.05 --worker <name>); task branch task/com-05 in Cloud; ledger record ledger/tasks/com-05.md.
Kind/size: service/L. Baseline: not-started.
Outcome: Immutable grants and revocations resolve deterministically into an entitlement snapshot with a per-capability reason and version, and rebuilding the snapshot from its grants/revocations always reproduces the stored snapshot.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-42.04 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\42-commerce-entitlement-and-credits.md, anchor rule-wp-42.04

Entry condition: adoption slice ADOPT.07.commerce is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- none
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Cloud:src/Cloud/ArcForges.Cloud.Modules.Entitlement/**/Resolver/**
Shared resources (follow the owner protocol): RES-cloud-host-composition (append): Each module registers through its own module entry point and route fragment; the host composition only lists modules; route and binding conflicts are resolved by the integration owner at merge.
Unblocks: COM.06, COM.07, COM.08, COM.10, COM.11, COM.13, COM.14, HAR.06, POL.04, SIM.07

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline unit tests: rebuild-equivalence over fixture accounts, reason-coverage, combination matrix over the four entitlement kinds, clock-determinism against an injected time source.
Completion evidence for the ledger: Rebuild-equivalence test result (snapshot-from-scratch equals stored snapshot) across fixture accounts.
Notes: BR-06 rebuild-equivalence is the core commerce invariant; COM.06/07/08/10/12 all read this resolver's snapshot, so its correctness gates a large share of downstream work.
```

```text
Execute ArcForges delivery task COM.06 — Distribution and enforcement.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\commerce.md (anchor task-com-06).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/com-06 (python tools/delivery.py claim COM.06 --worker <name>); task branch task/com-06 in Cloud; ledger record ledger/tasks/com-06.md.
Kind/size: service/M. Baseline: not-started.
Outcome: Entitlement is distributed with its version for client caching, realtime notification is only a refresh hint, offline staleness is bounded, all cost-bearing enforcement happens server-side, and losing entitlement never deletes local data.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-42.05 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\42-commerce-entitlement-and-credits.md, anchor rule-wp-42.05

Entry condition: adoption slice ADOPT.07.commerce is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] COM.05: EntitlementSnapshot + EntitlementVersion
- [artifact] CLOUD.23: typed-query/revision-precondition pattern
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Cloud:src/Cloud/ArcForges.Cloud.Modules.Entitlement/**/Distribution/**; Cloud:src/Cloud/ArcForges.Cloud.Modules.Entitlement/**/Enforcement/**
Shared resources (follow the owner protocol): RES-cloud-host-composition (append): Each module registers through its own module entry point and route fragment; the host composition only lists modules; route and binding conflicts are resolved by the integration owner at merge.; RES-contract-consumer-pins (append): A consumer task updates the pin it needs through a reviewed dependency change to the exact published candidate containing its closure; no consumer pins an unpublished closure or references Contracts source.
Unblocks: COM.15

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline tests: hint-not-authority, offline-staleness behavior, client-bypass negative, local-data-survival.
Completion evidence for the ledger: Client-bypass negative test result; local-data-survival result.
```

```text
Execute ArcForges delivery task COM.07 — Quota, usage and storage accounting.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\commerce.md (anchor task-com-07).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/com-07 (python tools/delivery.py claim COM.07 --worker <name>); task branch task/com-07 in Cloud; ledger record ledger/tasks/com-07.md.
Kind/size: service/L. Baseline: not-started.
Outcome: Quota (limit) and usage (measurement) live in separate stores keyed to the entitlement period, storage accounting matches committed objects exactly, and an exceeded quota produces a typed, explained refusal.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-42.06 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\42-commerce-entitlement-and-credits.md, anchor rule-wp-42.06

Entry condition: adoption slice ADOPT.07.commerce is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] CLOUD.07: the published capacity/quota kernel (Capacity and Container/D1 integration producer)
- [artifact] COM.05: versioned entitlement grants
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Cloud:src/Cloud/ArcForges.Cloud.Modules.Entitlement/**/Quota/**
Shared resources (follow the owner protocol): RES-cloud-host-composition (append): Each module registers through its own module entry point and route fragment; the host composition only lists modules; route and binding conflicts are resolved by the integration owner at merge.
Unblocks: COM.15, SIM.04, SIM.07

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline tests: race admissions, quota downgrade, repeated cancellation, GC timeout, period rollover with held old-period use, boundary-reset, accounting-vs-committed-storage comparison, refusal-message.
Completion evidence for the ledger: Accounting comparison result against actual committed storage; boundary-reset test result.
```

```text
Execute ArcForges delivery task COM.08 — Credits.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\commerce.md (anchor task-com-08).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/com-08 (python tools/delivery.py claim COM.08 --worker <name>); task branch task/com-08 in Cloud; ledger record ledger/tasks/com-08.md.
Kind/size: service/L. Baseline: not-started.
Outcome: Purchased (no-expiry) and compensation (disclosed-expiry) credit lots exist in integer micro-credits with funding order capacity to compensation to purchased, single-reservation-spans-both-pools accounting, reservation-expiry sweeping and a hard stop at zero with no floating point anywhere in the path.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-42.07 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\42-commerce-entitlement-and-credits.md, anchor rule-wp-42.07

Entry condition: adoption slice ADOPT.07.commerce is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] COM.05: entitlement kind determination (which grant authorises which credit class)
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Cloud:src/Cloud/ArcForges.Cloud.Modules.Entitlement/**/Credits/**
Shared resources (follow the owner protocol): RES-cloud-host-composition (append): Each module registers through its own module entry point and route fragment; the host composition only lists modules; route and binding conflicts are resolved by the integration owner at merge.
Unblocks: AIR.02, COM.12, COM.13

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline tests: lot-ordering matrix, concurrency (no-overdraft), reservation-expiry sweep, hard-stop, refund-hold, fixed-precision policy scan (no floating point).
Completion evidence for the ledger: Concurrency test showing no overdraft under concurrent reservation; fixed-precision scan result.
```

```text
Execute ArcForges delivery task COM.09 — Ledgers and reconciliation.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\commerce.md (anchor task-com-09).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/com-09 (python tools/delivery.py claim COM.09 --worker <name>); task branch task/com-09 in Cloud; ledger record ledger/tasks/com-09.md.
Kind/size: service/L. Baseline: not-started.
Outcome: The three ledgers exist as separate append-only stores with scheduled two-way provider reconciliation expressing repairs as new typed records, never edits, and divergence above threshold alerts.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-42.08 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\42-commerce-entitlement-and-credits.md, anchor rule-wp-42.08
- WP-42:p2-010-required-behavior-and-closure-thr P2-010 required behavior and closure; three ledgers with unresolved holds through their existing deadline (P2-010 required behavior and closure; three ledgers with unresolved holds through their existing deadline): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\42-commerce-entitlement-and-credits.md, package-level obligation
- WP-42:p2-010-required-behavior-and-closure P2-010 required behavior and closure (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\42-commerce-entitlement-and-credits.md, package-level obligation

Entry condition: adoption slice ADOPT.07.commerce is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] COM.03: Order/Payment records
- [artifact] COM.04: verified ProviderEvent stream
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Cloud:src/Cloud/ArcForges.Cloud.Modules.Billing/**/Ledgers/**; Cloud:src/Cloud/ArcForges.Cloud.Modules.Billing/**/Reconciliation/**
Shared resources (follow the owner protocol): RES-cloud-runbooks-and-fixtures (append): One file per runbook, monitor or provider fixture; indexes are append-only; recorded provider fixtures stay test-only.
Unblocks: CLOUD.63, COM.10, COM.14

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline tests: dropped-webhook repair, duplicated-order repair, provider-side-change repair, immutability (history cannot be edited), ledger-separation.
Completion evidence for the ledger: Dropped-webhook repair test recovering correct state without editing history; ledger-separation test.
```

```text
Execute ArcForges delivery task COM.10 — Refunds, disputes and evidence.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\commerce.md (anchor task-com-10).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/com-10 (python tools/delivery.py claim COM.10 --worker <name>); task branch task/com-10 in Cloud; ledger record ledger/tasks/com-10.md.
Kind/size: service/M. Baseline: not-started.
Outcome: A refund verifiably rolls entitlement back, dispute records are tracked, and a commercial evidence export covering order/payment/event/entitlement-history/usage for a period is complete, reproducible and free of payment-instrument data.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-42.09 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\42-commerce-entitlement-and-credits.md, anchor rule-wp-42.09

Entry condition: adoption slice ADOPT.07.commerce is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] COM.05: entitlement rollback path
- [artifact] COM.09: ledger entries to export
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Cloud:src/Cloud/ArcForges.Cloud.Modules.Billing/**/Refunds/**
Shared resources (follow the owner protocol): RES-cloud-runbooks-and-fixtures (append): One file per runbook, monitor or provider fixture; indexes are append-only; recorded provider fixtures stay test-only.
Unblocks: CLOUD.66, COM.13, COM.14

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline tests: refund-with-rollback, evidence completeness/reproducibility, payment-data-absence scan.
Completion evidence for the ledger: Refund-with-rollback test result; payment-instrument-absence scan (zero hits) on the evidence export.
```

```text
Execute ArcForges delivery task COM.11 — Service term interval model.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\commerce.md (anchor task-com-11).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/com-11 (python tools/delivery.py claim COM.11 --worker <name>); task branch task/com-11 in Cloud; ledger record ledger/tasks/com-11.md.
Kind/size: service/L. Baseline: not-started.
Outcome: entitlement.service_term exists as an interval keyed on (kind, period_ref) with subscription_ref stable across renewals, a renewal always creating a new period_ref row, a replayed provider event extending nothing twice, and a plan change superseding rather than editing.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-42.11 (service_term interval model keyed on (kind, period_ref); the three separated identities (subscription_ref stable / period_ref per paid interval / provider-event dedup in commerce.provider_event); union-of-overlap effective term; plan-change supersede. Capacity bucket/refill/reservation half split to COM.12.): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\42-commerce-entitlement-and-credits.md, anchor rule-wp-42.11

Entry condition: adoption slice ADOPT.07.commerce is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] COM.03: paid period identifiers (checkout/order confirmation producing a period_ref-worthy paid interval)
- [artifact] COM.05: offer assignment and entitlement kind
- [artifact] COM.04: deduplicated ProviderEvent stream
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Cloud:src/Cloud/ArcForges.Cloud.Modules.Entitlement/**/ServiceTerm/**
Shared resources (follow the owner protocol): RES-cloud-host-composition (append): Each module registers through its own module entry point and route fragment; the host composition only lists modules; route and binding conflicts are resolved by the integration owner at merge.
Unblocks: COM.12

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline tests: renewal creating a second term row without violating the (kind,period_ref) key, replayed event creating nothing, plan change superseding not editing, overlap/genuine-gap union-of-interval tests.
Completion evidence for the ledger: Renewal-without-key-violation test; replay-creates-nothing test; supersede-not-edit test.
```

```text
Execute ArcForges delivery task COM.12 — Replenishing capacity bucket, refill and admission.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\commerce.md (anchor task-com-12).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/com-12 (python tools/delivery.py claim COM.12 --worker <name>); task branch task/com-12 in Cloud; ledger record ledger/tasks/com-12.md.
Kind/size: service/XL. Baseline: not-started.
Outcome: The capacity bucket refills by a per-period saturating accrual independent of evaluation frequency, backed by a monotonic durable watermark and exact rational carry, never claws back on a ceiling reduction, initialises exactly once per contiguous run, and admission is atomic with the service-term check first, committing before dispatch.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-42.11 (entitlement.capacity_bucket refill algorithm (§7.2), capacity_policy_period history, capacity_reservation with three funding sources, idempotent once-per-contiguous-run initialisation, and atomic admission with the service-term check first): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\42-commerce-entitlement-and-credits.md, anchor rule-wp-42.11

Entry condition: adoption slice ADOPT.07.commerce is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] COM.11: service_term interval and (kind,period_ref) rows
- [artifact] COM.08: CreditReservation reserve/settle/release primitive
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Cloud:src/Cloud/ArcForges.Cloud.Modules.Entitlement/**/Capacity/**
Shared resources (follow the owner protocol): RES-cloud-host-composition (append): Each module registers through its own module entry point and route fragment; the host composition only lists modules; route and binding conflicts are resolved by the integration owner at merge.
Unblocks: AIR.02, COM.14, HAR.02, SIM.07

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline deterministic tests only (no wall-clock sleep): full-hold-then-consume-then-read fixture, fractional saturation, changed plan, overlap, genuine gap, unchanged renewal, grandfathered above-ceiling balance, the CT-13 refill fixture (identical result whether refill runs once or a thousand times over an interval containing a ceiling raise, reduction and rate change, asserting 11 at t=11), clock rollback/restart/reconnect/second-device/racing-replica watermark tests, ceiling-reduction-preserves-held-funding test, ledger-unit-separation test (customerCredit carries micro-credits with no currency; the other two carry money with currency; no query sums them).
Completion evidence for the ledger: The CT-13 refill fixture result exactly (11 at t=11, not 21 or 12); watermark non-rewind evidence across restart/second-device/racing-replica; ceiling-reduction-preserves-funding result.
Notes: The single most algorithmically risky unit in this area (§7.2 saturating accrual with exact rational carry); named as the PG-13/PG-16 producer that must close before WP-42.10 despite its higher substep number. Consider a narrow property-based-test spike on the refill function ahead of the full admission integration.
```

```text
Execute ArcForges delivery task COM.13 — Operator financial-owner proposal/approval operations.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\commerce.md (anchor task-com-13).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/com-13 (python tools/delivery.py claim COM.13 --worker <name>); task branch task/com-13 in Cloud; ledger record ledger/tasks/com-13.md.
Kind/size: service/L. Baseline: not-started.
Outcome: The financial-owner operator RPCs (grant/revokeGrant/issueCredit/adjustCredit/refund) are implemented exactly once against the registry04 §9 typed proposal/approval protocol with all eight authorization fields, refusing public customer/PAT/agent access, and one approved proposal cannot execute twice.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-42:operator-contract-closure-financial-owne Operator contract closure — financial owners (grant/revokeGrant/issueCredit/adjustCredit/refund) (operator contract closure; financial-owner RPC implementations: grant, revokeGrant, issueCredit, adjustCredit, refund): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\42-commerce-entitlement-and-credits.md, package-level obligation

Entry condition: adoption slice ADOPT.07.commerce is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [contract] CON.14: the OperatorService full RPC surface (ProposeAction/ApproveAction/execute, grant/revokeGrant/issueCredit/adjustCredit/refund message shapes, eight authorization fields, negative vectors) per registry04 §9
- [artifact] CLOUD.21: real identity/dispatch conformance for operator calls
- [artifact] COM.05: grant/revocation model
- [artifact] COM.08: credit lot issue/adjust primitives
- [artifact] COM.10: refund/rollback path
Completion prerequisites (may start earlier; cannot complete before these are complete):
- [integration] OPS.13: the operator console UI actually calling these RPCs end-to-end

Permitted write scope: Cloud:src/Cloud/ArcForges.Cloud.Modules.Billing/**/Operator/**; Cloud:src/Cloud/ArcForges.Cloud.Modules.Entitlement/**/Operator/**
Shared resources (follow the owner protocol): RES-cloud-host-composition (append): Each module registers through its own module entry point and route fragment; the host composition only lists modules; route and binding conflicts are resolved by the integration owner at merge.; RES-contracts-schema-sources (append): Each closure task edits only its own domain proto or HTTP-schema files and adds its own sharded constraint and fixture files; shared inventories (package inventory, foundation inventory, constraint aggregate) are append-only per closure. A proto file with several contributing tasks (operator, policy/configuration) has one designated author task and the others request changes through it. The integration owner merges closure pull requests one at a time and the next author rebases and regenerates.
Unblocks: CLOUD.64, OPS.05, OPS.13

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline tests: distinct approver, stale hash/revision/configuration, role revocation, expiry, concurrent consumption, lost receipt, double-execution-of-one-approval, no-direct-SQL/public-SDK-import architecture test.
Completion evidence for the ledger: Double-execution negative result (one approved proposal cannot execute twice); public-customer/PAT/agent refusal result for every method.
```

```text
Execute ArcForges delivery task COM.14 — Technical commerce closure and live-gate staging.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\commerce.md (anchor task-com-14).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/com-14 (python tools/delivery.py claim COM.14 --worker <name>); task branch task/com-14 in Cloud; ledger record ledger/tasks/com-14.md.
Kind/size: service/L. Baseline: not-started.
Outcome: Deterministic provider normalization and the full sandbox lifecycle are proven with synthetic and Paddle/Payoneer-sandbox vectors, SubscriptionState exactly matches requirements-04, plan changes start next term without proration, and the live-payment/payout/refund/merchant gates are explicitly preserved as pending for WP50.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-42.10 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\42-commerce-entitlement-and-credits.md, anchor rule-wp-42.10
- WP-42:p2-010-required-behavior-and-closure P2-010 required behavior and closure (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\42-commerce-entitlement-and-credits.md, package-level obligation

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
Shared resources (follow the owner protocol): RES-cloud-runbooks-and-fixtures (append): One file per runbook, monitor or provider fixture; indexes are append-only; recorded provider fixtures stay test-only.
Unblocks: COM.15, WEB.14, WEB.29

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Recorded Paddle/Payoneer sandbox scenario vectors (no-term, cancellation, lost result, unknown exposure, future-effective changes) plus synthetic fixtures; per P2-017 this acceptance-level sandbox evidence stays outside routine CI (manual/scheduled), while regression-level assertions stay in offline CI.
Completion evidence for the ledger: Full synthetic/sandbox ledger vector results; activation checklist document handed to WP48/WP50; explicit statement that VG-10/VG-11/VG-12/L-30 remain open.
Notes: Completion explicitly does not require WP48 (account portal) or WP50 (real go-live); this task closes the technical/test-mode gate only (PG-10) and stages the activation checklist. Real checkout/payout evidence and VG-10/VG-11/VG-12/L-30 stay with WP50 per WP-42 §8.11. Retires SUB-provider-event-fixtures and SUB-hosted-checkout-sandbox.
```

```text
Execute ArcForges delivery task COM.15 — Owned-artifact receipt and closure.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\commerce.md (anchor task-com-15).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/com-15 (python tools/delivery.py claim COM.15 --worker <name>); task branch task/com-15 in Cloud; ledger record ledger/tasks/com-15.md.
Kind/size: service/S. Baseline: not-started.
Outcome: The package-level owned-artifact/real-integration receipt is recorded (source commit, producer version, candidate hashes, actual runtime/provider, scenario, result, real-vs-fixture status) and the P2-010 active-Pass/subscription-exclusivity and ledger-hold-deadline vectors pass.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-42.90 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\42-commerce-entitlement-and-credits.md, anchor rule-wp-42.90
- WP-42:p2-010-required-behavior-and-closure-act P2-010 required behavior and closure; active Pass/subscription mutual exclusion, no immediate proration, exact renewal/reset periods (P2-010 required behavior and closure; active Pass/subscription mutual exclusion, no immediate proration, exact renewal/reset periods): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\42-commerce-entitlement-and-credits.md, package-level obligation
- WP-42:p2-010-required-behavior-and-closure P2-010 required behavior and closure (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\42-commerce-entitlement-and-credits.md, package-level obligation

Entry condition: adoption slice ADOPT.07.commerce is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] COM.14: technical commerce closure results to attach to the receipt
- [artifact] COM.06: package task delivered
- [artifact] COM.07: package task delivered
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Cloud:eng/provenance/records/**
Unblocks: REL.06, REL.08

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Aggregation only: existing concurrent admission/idempotent settlement/reversal/storage-accounting cases re-asserted at the candidate closure; no new test logic.
Completion evidence for the ledger: The owned-artifact/real-integration receipt itself, with inapplicable fields explicitly marked.
```
