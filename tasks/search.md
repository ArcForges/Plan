# ArcForges delivery task prompts — Knowledge search and retrieval

Generated from Design `docs/planning/delivery/delivery-graph.json` by `tools/delivery.py`; do not edit by hand.
Each block is self-contained. Claim a task only when `python tools/delivery.py ready` lists it, with
`python tools/delivery.py claim <TASK-ID> --worker <name>`, then follow `arcforges-implementation.md`.
Tasks are ordered by lane for reading; the order is not a schedule.

## Knowledge search and retrieval

```text
Execute ArcForges delivery task SRCH.00 — Source admission and registration for search.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\search.md (anchor task-srch-00).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/srch-00 (python tools/delivery.py claim SRCH.00 --worker <name>); task branch task/srch-00 in Cloud; ledger record ledger/tasks/srch-00.md.
Kind/size: service/M. Baseline: not-started.
Outcome: Own-product content, explicitly selected uploads and authorized web sources are admitted into the search source registry with origin/egress and consent recorded; other-product, other-realm and private resources are rejected before any index write.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-40.00 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\40-knowledge-search-and-retrieval.md, anchor rule-wp-40.00

Entry condition: adoption slice ADOPT.07.search is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [contract] CON.10: published SourceRecord/ContentOrigin typed record (origin, consent, egress) in Contracts public schema
- [artifact] CLOUD.37: durable resource identity/revision for synced product content
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Cloud:src/Cloud/ArcForges.Cloud.Modules.Retrieval/Sources/**; Cloud:tests/Cloud.Tests.Integration/Retrieval/Sources/**
Shared resources (follow the owner protocol): RES-cloud-host-composition (append): Each module registers through its own module entry point and route fragment; the host composition only lists modules; route and binding conflicts are resolved by the integration owner at merge.
Permitted substitutes (never real integration evidence): SUB-web-search-fixture: source admission's origin/consent/rejection logic for web sources without a funded external call Real producer ['AIR.06']; removed by SRCH.06
Unblocks: HAR.01, SRCH.01

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline unit + Cloud integration tests against the real D1 schema in an ephemeral test host; no live web fetch in CI (P2-017 forbids live-service CI) -- the web-source path is exercised through the fixture web-search response only.
Completion evidence for the ledger: Rejection-before-snippet test matrix (other-product/realm/private), consent/origin record contents, source registration receipt.
Notes: WP-40 has no explicit section 4 project/file table (unlike WP-41, WP-43 and WP-52); the Cloud module path above follows the Cloud module layout convention and is not stated in WP-40 itself.
```

```text
Execute ArcForges delivery task SRCH.01 — Scoped derived index production (D1 FTS + Vectorize).

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\search.md (anchor task-srch-01).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/srch-01 (python tools/delivery.py claim SRCH.01 --worker <name>); task branch task/srch-01 in Cloud; ledger record ledger/tasks/srch-01.md.
Kind/size: service/L. Baseline: not-started.
Outcome: D1 FTS scoped queries and per-workspace Vectorize namespaces are produced with mandatory realm/product/model-generation filters, source revision/policy checks, rebuild pointers, tombstone reconciliation and dimensional-change isolation (separate index, atomic reader switch, rollback window).

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-40.01 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\40-knowledge-search-and-retrieval.md, anchor rule-wp-40.01

Entry condition: adoption slice ADOPT.07.search is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] SRCH.00: admitted source registry entries to index
- [contract] CON.10: the data-model retrieval_chunk projection key (sourceId, sourceRev, embeddingModelId, embeddingProfileVersion, chunkHash) as a published schema
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Cloud:src/Cloud/ArcForges.Cloud.Modules.Retrieval/Indexing/**
Shared resources (follow the owner protocol): RES-ai-workflow-and-routes (append): The Workflow entry is owned by the turn-loop task; other Harness tasks add steps through their own modules; the route-pin table changes only with a policy snapshot. Any task that runs against the AI deployment environment holds the lease `leases/res-ai-workflow-and-routes` for that live run only.; RES-cloud-host-composition (append): Each module registers through its own module entry point and route fragment; the host composition only lists modules; route and binding conflicts are resolved by the integration owner at merge.
Permitted substitutes (never real integration evidence): SUB-embedding-rerank-fixture: index-write correctness (namespace scoping, filters, tombstones, dimension-change isolation) independent of real model variance Real producer ['AIR.00']; removed by SRCH.06
Unblocks: SRCH.02, SRCH.05, SRCH.06

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline unit tests for index math with fixture vectors; D1/Vectorize behavior exercised against local/emulated CF bindings per P2-017 (no live CF in ordinary CI); L-16 index/namespace footprint measured locally.
Completion evidence for the ledger: Cross-product/tenant isolation before topK, stale deletion, unavailable canonical owner, lexical fallback, L-16 footprint measurement.
```

```text
Execute ArcForges delivery task SRCH.02 — Hybrid retrieval, RRF fusion and budgets.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\search.md (anchor task-srch-02).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/srch-02 (python tools/delivery.py claim SRCH.02 --worker <name>); task branch task/srch-02 in Cloud; ledger record ledger/tasks/srch-02.md.
Kind/size: service/L. Baseline: not-started.
Outcome: Lexical (D1 FTS) and semantic (Vectorize) candidates are fused with RRF(x)=sum(1/(60+rank_i(x))), exact-match priority preserved, the Notes scalar comparator never reordered by vector score, and RetrievalBudget defaults (candidates 200/500, evidence 20/100, contextTokens 8192/24000, perSource 5/20, graphDepth 1/3) enforced.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-40.02 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\40-knowledge-search-and-retrieval.md, anchor rule-wp-40.02

Entry condition: adoption slice ADOPT.07.search is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] SRCH.01: scoped derived index to query against
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Cloud:src/Cloud/ArcForges.Cloud.Modules.Retrieval/Ranking/**
Shared resources (follow the owner protocol): RES-ai-workflow-and-routes (append): The Workflow entry is owned by the turn-loop task; other Harness tasks add steps through their own modules; the route-pin table changes only with a policy snapshot. Any task that runs against the AI deployment environment holds the lease `leases/res-ai-workflow-and-routes` for that live run only.; RES-cloud-host-composition (append): Each module registers through its own module entry point and route fragment; the host composition only lists modules; route and binding conflicts are resolved by the integration owner at merge.
Permitted substitutes (never real integration evidence): SUB-embedding-rerank-fixture: index-write correctness (namespace scoping, filters, tombstones, dimension-change isolation) independent of real model variance Real producer ['AIR.00']; removed by SRCH.06
Unblocks: SRCH.03, SRCH.06

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline unit tests: budget bounds, multilingual/no-match/partial queries, exact decimal vector comparison against fixture vectors.
Completion evidence for the ledger: Budget-bound test matrix; multilingual/no-match/partial results; decimal-vector exactness.
```

```text
Execute ArcForges delivery task SRCH.03 — Current permission recheck at query time.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\search.md (anchor task-srch-03).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/srch-03 (python tools/delivery.py claim SRCH.03 --worker <name>); task branch task/srch-03 in Cloud; ledger record ledger/tasks/srch-03.md.
Kind/size: service/S. Baseline: not-started.
Outcome: Source owner permission and revision are rechecked after candidate retrieval and before any count/snippet/citation is returned; revocation during a query and a stale index can never expose content.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-40.03 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\40-knowledge-search-and-retrieval.md, anchor rule-wp-40.03

Entry condition: adoption slice ADOPT.07.search is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] SRCH.02: ranked candidate list to filter
- [artifact] CLOUD.11: live owner/grant permission check API
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Cloud:src/Cloud/ArcForges.Cloud.Modules.Retrieval/PermissionRecheck/**
Unblocks: SRCH.04, SRCH.90

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline integration test with a revocation injected mid-query and a deliberately stale index row.
Completion evidence for the ledger: Revocation-during-query and stale-index-cannot-expose-content test results.
```

```text
Execute ArcForges delivery task SRCH.04 — Evidence and citations.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\search.md (anchor task-srch-04).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/srch-04 (python tools/delivery.py claim SRCH.04 --worker <name>); task branch task/srch-04 in Cloud; ledger record ledger/tasks/srch-04.md.
Kind/size: service/M. Baseline: not-started.
Outcome: Retrieval results retain source kind, immutable reference, anchor, uncertainty/completeness and measurement/media precision; stale or missing sources are labelled and no citation is ever fabricated.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-40.04 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\40-knowledge-search-and-retrieval.md, anchor rule-wp-40.04

Entry condition: adoption slice ADOPT.07.search is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] SRCH.03: permission-rechecked candidates
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Cloud:src/Cloud/ArcForges.Cloud.Modules.Retrieval/Citations/**
Unblocks: SRCH.90

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline unit tests for stale/missing source labelling and anti-fabrication assertions.
Completion evidence for the ledger: Stale/missing source label tests; no-fabricated-citation assertion.
```

```text
Execute ArcForges delivery task SRCH.05 — Privacy partitioning and cache isolation.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\search.md (anchor task-srch-05).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/srch-05 (python tools/delivery.py claim SRCH.05 --worker <name>); task branch task/srch-05 in Cloud; ledger record ledger/tasks/srch-05.md.
Kind/size: service/M. Baseline: not-started.
Outcome: Cache, history and context are partitioned by product/profile per RI-01..03 (workspace+principal key, no cross-workspace reuse); temporary/local Cloud-processing content never enters Cloud search.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-40.05 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\40-knowledge-search-and-retrieval.md, anchor rule-wp-40.05

Entry condition: adoption slice ADOPT.07.search is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] SRCH.01: index/cache tables to partition
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Cloud:src/Cloud/ArcForges.Cloud.Modules.Retrieval/Privacy/**
Shared resources (follow the owner protocol): RES-cloud-host-composition (append): Each module registers through its own module entry point and route fragment; the host composition only lists modules; route and binding conflicts are resolved by the integration owner at merge.
Unblocks: SRCH.90

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline marker test, cross-app/account leakage test, purge test.
Completion evidence for the ledger: Marker test, cross-app/account leakage and purge results.
```

```text
Execute ArcForges delivery task SRCH.06 — Real Cloud query path (fixture-to-real swap).

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\search.md (anchor task-srch-06).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/srch-06 (python tools/delivery.py claim SRCH.06 --worker <name>); task branch task/srch-06 in Cloud; ledger record ledger/tasks/srch-06.md.
Kind/size: integration/M. Baseline: not-started.
Outcome: The retrieval path runs against real Workers AI embeddings/reranker and real D1/Vectorize with C# owner filtering; SUB-embedding-rerank-fixture is retired from the query path, and explicit lexical-only degradation is proven when the semantic path is unavailable.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-40.06 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\40-knowledge-search-and-retrieval.md, anchor rule-wp-40.06

Entry condition: adoption slice ADOPT.07.search is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] AIR.00: deployed Workers AI embed/rerank adapter (real, not fixture)
- [artifact] POL.08: active policy/config snapshot naming the admitted embedding/rerank model generation
- [artifact] SRCH.01: scoped derived index production
- [artifact] SRCH.02: hybrid retrieval and budgets
- [artifact] AIR.06: the real operator-funded web-search dispatch capability
Completion prerequisites (may start earlier; cannot complete before these are complete):
- [integration] SRCH.90: index capacity acceptance evidence

Permitted write scope: Cloud:src/Cloud/ArcForges.Cloud.Modules.Retrieval/Indexing/**; Cloud:src/Cloud/ArcForges.Cloud.Modules.Retrieval/Ranking/**
Shared resources (follow the owner protocol): RES-ai-workflow-and-routes (append): The Workflow entry is owned by the turn-loop task; other Harness tasks add steps through their own modules; the route-pin table changes only with a policy snapshot. Any task that runs against the AI deployment environment holds the lease `leases/res-ai-workflow-and-routes` for that live run only.; RES-private-configuration (append): Each owning task adds its own configuration section; activation is a signed publication by the policy lane; no task edits another section.
Unblocks: SRCH.90

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Real compatible client/owner/index version test against deployed CF bindings (credentialed candidate gate, not ordinary CI, per P2-017's 'no real AI inference in CI'); explicit lexical-only degradation test.
Completion evidence for the ledger: Real compatible client/owner/index versions; explicit lexical-only degradation.
```

```text
Execute ArcForges delivery task SRCH.90 — Owned artifacts, real integration and index capacity acceptance.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\search.md (anchor task-srch-90).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/srch-90 (python tools/delivery.py claim SRCH.90 --worker <name>); task branch task/srch-90 in Cloud; ledger record ledger/tasks/srch-90.md.
Kind/size: service/M. Baseline: not-started.
Outcome: Every SRCH substep is built/packed once and consumed as exact candidate bytes from a clean environment; model04 launch-capacity.v1 account/realm vector and namespace budgets are enforced with reservation, old/new index overlap, tombstone reconciliation, threshold refusal before new paid admission, and rebuild pausing/recovery all proven.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-40.90 (full, including index capacity acceptance): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\40-knowledge-search-and-retrieval.md, anchor rule-wp-40.90

Entry condition: adoption slice ADOPT.07.search is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] SRCH.06: real query path evidence
- [artifact] SRCH.03: package task delivered
- [artifact] SRCH.04: package task delivered
- [artifact] SRCH.05: package task delivered
Completion prerequisites (may start earlier; cannot complete before these are complete):
- [integration] POL.02: launch-capacity.v1 signed configuration snapshot

Permitted write scope: Cloud:tests/Cloud.Tests.Integration/Retrieval/**
Shared resources (follow the owner protocol): RES-private-configuration (append): Each owning task adds its own configuration section; activation is a signed publication by the policy lane; no task edits another section.
Unblocks: REL.06, SRCH.06

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Package/contract/owner/version compatibility and failure/recovery tests; P2-017 proportionate (no live paid-provider CI loop; capacity thresholds tested against recorded/replayable fixtures where the real CF budget document is unavailable in CI).
Completion evidence for the ledger: Index capacity acceptance ledger: reservations, overlap, tombstone reconciliation, threshold refusal, rebuild pause/recovery.
Notes: WP-40 Sec.9 names 50/52 as downstream consumers of this released artifact; not a completion blocker for SRCH.90 itself. Contributes to PG-26 (launch capacity envelope) as one of its producers.
```
