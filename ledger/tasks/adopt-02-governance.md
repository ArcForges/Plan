---
task: ADOPT.02.governance
status: complete
recorded: 2026-09-27
claimant: w-20260927-dgov
epoch: 1
---

# DesktopPlatform governance adoption

Reviewer: `w-20260927-dgov`, DesktopPlatform integration owner epoch 2. Review covers all nine tasks in the slice against their outcomes, mapped WP00/WP01/WP02/WP05 obligations and P2-018/P2-019/P2-020. Ordered plan: inspect frozen authorities and accepted receipt inventory; bind each task to actual source; classify all nine; record accepted tasks separately; run ledger consistency check; obtain exact-head peer review and Plan integration. Adoption changes only this ledger.

## Classification and bound scope

| Task | Classification | Evidence and actual source binding | Remaining scope and blockers |
|---|---|---|---|
| GOV.01 | inherited | [Own record](gov-01.md); accepted WP00 receipts; existing glossary/invariant exports, reference registration, licence/provenance policy and Contracts naming policy. | None for accepted retained-family baseline; new policy-data cleanup belongs to GOV.18. |
| GOV.02 | inherited | [Own record](gov-02.md); accepted WP01 receipts; `eng/policy/reconciliation/*`, `eng/reconciliation.py`, solutions, native/source dispositions and five-method `tests/ArchitectureTests/RepositoryPolicyTests.cs`. | None for accepted reconciliation; retired families remain explicit GOV.17/GOV.18 cleanup. |
| GOV.03 | inherited | [Own record](gov-03.md); accepted WP02 receipts; locked build roots, AOT/trim declarations, dependency admission, runtime ownership, package/version tools and green frozen CI/publication. | None for first acceptance; recurring framework/dependency changes require new admission. |
| GOV.04 | inherited with adjustment | Five existing `RepositoryPolicyTests.cs` methods check solution ownership, local references, native ownership, explicit publication and source licences. Existing Python policy tools remain useful. Bound additions: `tests/ArchitectureTests/**` and `eng/policy/exceptions.json`. | Full reusable AT-01..14/RP-01..10 engine, project-graph reader, fixture compiler, banned-category scanner, forbidden-term integration and pass/fail pair per rule are absent; add actual reusable producer/package integration through a scoped planning repair if required beyond declared paths. Start waits for GOV.18. No full engine inheritance. |
| GOV.13 | gap | `eng/accounting/invariant-report.py` and actual test-derived accounting output do not exist; `eng/policy/invariants.json` is planned-only export, not implementation evidence. Bind to `eng/accounting/` and `artifacts/evidence/invariant-accounting.json`. | Implement accounting from real GOV.04 results and GOV.18 export; preserve retired invariant identities and never count them as satisfied obligations. Starts after GOV.04/GOV.18. |
| GOV.14 | inherited with adjustment | `eng/design_policy.py`, `eng/design_corpus.py`, `eng/design_graph.py`, `eng/test_design_policy.py` exist and verify their old pinned corpus; pin `5322d698a1b650a52a5a139d986dd85b00b48581` does not establish current Design integrity. | After GOV.18 migration, close all current corpus/link/citation/decision-coverage checks with zero findings, extending these files. Known Design citation repairs coordinate through ADOPT.11; no acceptance is inferred from old pin or planning observations. |
| GOV.15 | gap | No current WP05 stage acceptance or seven-owner policy graph integration exists. Bind to `eng/**` and new Design `docs/assurance/wp05-90-*` / `wp05-stage-acceptance.*`. | Join real policy results from GOV.04/.05/.07/.09/.10/.11/.12/.13/.14 and published metadata; no source cloning or bootstrap substitution closes this gate. |
| GOV.17 | gap | `native/CMakeLists.txt` still includes Media/colour/OTIO/graphics; `src/Native` and `eng/packaging/packages.json` still publish retired families. Still-image shim remains `native/arcslate-image-abi` and managed imports use `ArcSlateImageNative`. | Apply approved P2-019/P2-020 cleanup across native directories, solution, retained packaging guards, ABI tests and current docs; move image to `native/arcimage-abi`, use `ArcImageNative`, retain exported `arcimage_*` symbols, immutable package history and provenance. No extra design conflict: ADP-10 already authorizes this change. |
| GOV.18 | gap | Existing policy JSON retains removed owners/families; `eng/design_graph.py` validates serial package tables/order and `eng/design_policy.py` derives active owners from that graph. `docs/design-policy.md` still points to B and GOV.14 for migration. | Reduce live runtime/licence/reconciliation/reference policy and corresponding tools/tests; migrate to delivery-graph validation and active owners, negative fixtures, then reviewed Design repin and regenerated exports in one change. Correct current guidance to GOV.18; preserve provenance/history. No source edits in adoption. |

## Findings, execution readiness and validation

P2-019/P2-020 and ADP-10 already decide retired bindings, so they are scheduled adjustments rather than unresolved architecture conflicts. No new D-001 conflict was found. GOV.17 and GOV.18 become immediately eligible after this record merges; other tasks retain their exact graph prerequisites. No global adoption barrier is added. Cross-repository naming declaration re-export belongs to CON.23 after GOV.18, not this slice. GOV.04's reusable publication integration must stay within a reviewed scope (its present write scope is test/data only).

The record deliberately does not rewrite deprecated evidence or claim 429 current obligations are all implemented. Old counts, five historical reference registrations and superseded owners are historical evidence; current graph/retirement authority controls future work. All three inherited tasks have separate records in this PR.

Validation: frozen-source and accepted-receipt filename review; source-layout review; Plan ledger consistency check with explicit retained Plan/current Design roots. No product builds, public downloads or runtime verification. Exact reviewed/merge heads are recorded on the claim and PR history, since embedding the future merge SHA would change the reviewed head.

## Evidence and limits

Frozen source: DesktopPlatform `e5ce94221c13d0014781a760c0865b942350be4d`; Design `722e85641c8afb765dafcab5bc0e84d5a22d5a3c`. See [baseline](../adoption/baseline.md#desktopplatform) for independently reviewed PR #64, retained green CI and original publication run 36334843593 (NuGet candidate `1.0.0-ci.27.1`). No open PR existed at freeze. Review uses the graph's explicit accepted-baseline designation and named accepted receipts; historical receipt bodies were not reread, as the task evidence fields direct. Source inventory and current instructions were inspected, without rebuilding or downloading artifacts.

The accepted historical work is inherited only for retained-family obligations under P2-019. Removed-product obligations are retired, not satisfied. GOV.17/GOV.18 own source cleanup separately; inheritance does not certify their cleanup or product functionality. No new runtime, device, GUI, browser, live-service, inference or installed-consumer result is asserted. Existing receipts retain their historical coverage; no substitutes introduced. Recurring dependency/framework admission remains required for future changes.
