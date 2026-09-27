---
task: GOV.02
status: inherited
recorded: 2026-09-27
claimant: w-20260927-dgov
---

# Repository reconciliation

- Adoption: [ADOPT.02.governance](adopt-02-governance.md).
- Obligation parts satisfied: WP-01.00 through WP-01.05 and WP-01.90 (full retained-family parts), plus the mapped Cloud module-layout package obligation. Historical scaffold counts do not create current runtime modules.
- Accepted receipts in Design `docs/assurance/` at the frozen Design commit (presence verified): wp01-00-implementation-evidence.md/.json, wp01-00-inventory-policy.md, wp01-01-contract-access-policy.md, wp01-01-implementation-evidence.md/.json, wp01-02-foundation-review.md/.json, wp01-03-native-reconciliation-policy.md, wp01-03-native-reconciliation.md/.json, wp01-04-test-family-map.md/.json, wp01-05-bounded-reconciliation.md/.json and wp01-stage-acceptance.md/.json.
- Actual bound source: eng/policy/reconciliation/*, eng/reconciliation.py, docs/reconciliation-inventory.md, docs/native-reconciliation.md, tests/ArchitectureTests/RepositoryPolicyTests.cs and existing solution/project dispositions.
- Acceptance authority: the task's `baseline: accepted` and P2-018/P2-019 retain WP00-WP02 acceptance; no new acceptance audit or removed-product satisfaction is inferred.

## Evidence and limits

Frozen source: DesktopPlatform `e5ce94221c13d0014781a760c0865b942350be4d`; Design `722e85641c8afb765dafcab5bc0e84d5a22d5a3c`. See [baseline](../adoption/baseline.md#desktopplatform) for independently reviewed PR #64, retained green CI and original publication run 36334843593 (NuGet candidate `1.0.0-ci.27.1`). No open PR existed at freeze. Review uses the graph's explicit accepted-baseline designation and named accepted receipts; historical receipt bodies were not reread, as the task evidence fields direct. Source inventory and current instructions were inspected, without rebuilding or downloading artifacts.

The accepted historical work is inherited only for retained-family obligations under P2-019. Removed-product obligations are retired, not satisfied. GOV.17/GOV.18 own source cleanup separately; inheritance does not certify their cleanup or product functionality. No new runtime, device, GUI, browser, live-service, inference or installed-consumer result is asserted. Existing receipts retain their historical coverage; no substitutes introduced. Recurring dependency/framework admission remains required for future changes.
