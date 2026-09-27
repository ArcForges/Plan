---
task: ADOPT.07.search
status: complete
recorded: 2026-09-27
claimant: w-20260927-cloud-lane
epoch: 1
---

# Adopt Cloud: Knowledge search and retrieval

## Inputs and source comparison

Cloud integration owner w-20260927-cloud-lane, role epoch 2, reviewed the [frozen Cloud baseline](../adoption/baseline.md#cloud), source `60c5c4288b126c81a09fa5d1944671e9acb87495`, generated task outcomes/obligation parts, and the corresponding WP requirements/tests/gates. No open Cloud PR existed at the freeze.

No Retrieval/Search source admission, index, ranking, permission recheck, citations, cache or real supplier path exists.

The complete tracked source inventory is summarized in [Cloud repository facts](../adoption/Cloud.md). Bootstrap build/dependency/provenance checks and deployment receipts remain valid for their original scope, but do not satisfy these missing outcomes. Each row retains the full named task outcome as remaining work, including its mapped tests and completion gates.

## Classifications

| Task | Classification | Bound write scope | Remaining scope | Evidence / conflicts / blockers |
|---|---|---|---|---|
| SRCH.00 | gap | Planned additions: Cloud:src/Cloud/ArcForges.Cloud.Modules.Retrieval/Sources/**; Cloud:tests/Cloud.Tests.Integration/Retrieval/Sources/** | Own-product content, explicitly selected uploads and authorized web sources are admitted into the search source registry with origin/egress and consent recorded; other-product, other-realm and private resources are rejected before any index write. | Frozen source lacks this outcome. Normal graph prerequisites apply; no implementation conflict found. |
| SRCH.01 | gap | Planned additions: Cloud:src/Cloud/ArcForges.Cloud.Modules.Retrieval/Indexing/** | D1 FTS scoped queries and per-workspace Vectorize namespaces are produced with mandatory realm/product/model-generation filters, source revision/policy checks, rebuild pointers, tombstone reconciliation and dimensional-change isolation (separate index, atomic reader switch, rollback window). | Frozen source lacks this outcome. Normal graph prerequisites apply; no implementation conflict found. |
| SRCH.02 | gap | Planned additions: Cloud:src/Cloud/ArcForges.Cloud.Modules.Retrieval/Ranking/** | Lexical (D1 FTS) and semantic (Vectorize) candidates are fused with RRF(x)=sum(1/(60+rank_i(x))), exact-match priority preserved, and RetrievalBudget defaults (candidates 200/500, evidence 20/100, contextTokens 8192/24000, perSource 5/20, graphDepth 1/3) enforced. | Frozen source lacks this outcome. Normal graph prerequisites apply; no implementation conflict found. |
| SRCH.03 | gap | Planned additions: Cloud:src/Cloud/ArcForges.Cloud.Modules.Retrieval/PermissionRecheck/** | Source owner permission and revision are rechecked after candidate retrieval and before any count/snippet/citation is returned; revocation during a query and a stale index can never expose content. | Frozen source lacks this outcome. Normal graph prerequisites apply; no implementation conflict found. |
| SRCH.04 | gap | Planned additions: Cloud:src/Cloud/ArcForges.Cloud.Modules.Retrieval/Citations/** | Retrieval results retain source kind, immutable reference, anchor, uncertainty/completeness and measurement precision; stale or missing sources are labelled and no citation is ever fabricated. | Frozen source lacks this outcome. Normal graph prerequisites apply; no implementation conflict found. |
| SRCH.05 | gap | Planned additions: Cloud:src/Cloud/ArcForges.Cloud.Modules.Retrieval/Privacy/** | Cache, history and context are partitioned by product/profile per RI-01..03 (workspace+principal key, no cross-workspace reuse); temporary/local Cloud-processing content never enters Cloud search. | Frozen source lacks this outcome. Normal graph prerequisites apply; no implementation conflict found. |
| SRCH.06 | gap | Planned additions: Cloud:src/Cloud/ArcForges.Cloud.Modules.Retrieval/Indexing/**; Cloud:src/Cloud/ArcForges.Cloud.Modules.Retrieval/Ranking/** | The retrieval path runs against real Workers AI embeddings/reranker and real D1/Vectorize with C# owner filtering; SUB-embedding-rerank-fixture is retired from the query path, and explicit lexical-only degradation is proven when the semantic path is unavailable. | Frozen source lacks this outcome. Normal graph prerequisites apply; no implementation conflict found. |
| SRCH.90 | gap | Planned additions: Cloud:tests/Cloud.Tests.Integration/Retrieval/** | Every SRCH substep is built/packed once and consumed as exact candidate bytes from a clean environment; model04 launch-capacity.v1 account/realm vector and namespace budgets are enforced with reservation, old/new index overlap, tombstone reconciliation, threshold refusal before new paid admission, and rebuild pausing/recovery all proven. | Frozen source lacks this outcome. Normal graph prerequisites apply; no implementation conflict found. |

## Scope binding and validation

Existing source is `src/ArcForges.Cloud` (assembly/namespace ArcForges.Cloud), with tests under `tests/ArcForges.Cloud.Tests`, worker code under `worker`, tooling under `tooling`, and policy/provenance under `eng`. Logical `src/Cloud/ArcForges.Cloud.Host` and `src/ArcForges.Cloud.Host` bind to the existing host, preserving its identity. Module/Storage/PublicApi/Jobs directories in the rows are absent planned additions beneath Cloud, not permissions to rename the bootstrap or copy another repository. New projects, dependency locks, root registration and workflow changes require explicit scope/resource reconciliation before implementation; this ledger itself grants no additional writes. Empty-write integration tasks remain evidence joins and cannot implement missing producers.

No task is inherited; no inherited task record is created. The slice opens exactly its listed tasks under their normal prerequisites and does not authorize execution outside the selected launcher scope. No new substitute is registered or accepted; no runtime/product gate closes. Removed-product cleanup remains with CON.23/GOV.17/GOV.18, outside these ledger edits.

Validation: source inventory, task/obligation and frozen receipt review, plus explicit-root Plan consistency check. No build, runtime/provider test, artifact download or publication recheck. Untested coverage is every missing outcome and its real integration/acceptance cases. Ledger PR, independent exact-head approval and merge commits are preserved in the PR and claim audit trail.
