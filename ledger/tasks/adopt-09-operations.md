---
task: ADOPT.09.operations
status: complete
recorded: 2026-09-27
claimant: w-20260927-web-lane
epoch: 1
---

# Web operations adoption

## Review basis and evidence

Reviewed frozen Web `b0a6d7e1552d0a28f6abc30978cc25b7da3a8461` against Design `722e85641c8afb765dafcab5bc0e84d5a22d5a3c`; [baseline](../adoption/baseline.md#web) records PR #19, exact-head peer approval, green retained PR checks, successful main CI [36334763241](https://github.com/ArcForges/Web/actions/runs/36334763241), candidate `web-0.1.0-ci.62.1` and original Cloudflare receipt. No open Web PR existed at review. [Repository facts](../adoption/Web.md) give the shared source inventory and pin bindings.

Evidence keys refer to this frozen source, not future implementation:

- E1: `README.md`, `apps/app/README.md`, `apps/site/app/routes.ts`, `apps/site/react-router.config.ts`: only home/Hello/Cloud-Hello routes, `ssr: false`, three prerenders; Account/Chat/operator are absent.
- E2: `packages/ui/src/index.tsx` and styles: bootstrap Shell/Button/Arrow, not complete owned consumer states.
- E3: `tooling/project.ts` policy, `tooling/licence-boundary.ts`, `tooling/dependency-policy.ts`, `eng/policy`, `tests/unit/licence-boundary.test.ts`, `tests/unit/lock-provenance.test.ts` and `tests/provenance`: existing licence/pin/lock/provenance controls, not the full architecture rule matrix.
- E4: `.github/workflows/ci.yml`, `tooling/cloudflare.ts`, `docs/validation.md`, baseline CI/provider receipt: one static candidate and deployment pipeline, not Account/Chat or commercial/browser acceptance.

The reviewer compared each task outcome, mapped obligation parts (including tests and completion gates), write scope and evidence against source and accepted receipts. No task is inherited as complete. Every gap retains its full mapped obligation, tests and acceptance evidence; the table summarizes the missing outcome and does not narrow it. Historical four-product wording is superseded by P2-020's ArcScope family; no source contradiction requiring D-001 was found. Existing scaffolds are reusable inputs only.

Validation was read-only source, receipt and obligation review plus the Plan ledger check. No build, package download, browser/device/live-service/inference or runtime check was run. Existing browser and provider probes do not certify future flows. Browser matrix, accessibility, performance, real session/business and commercial acceptance remain untested for the missing outcomes, under P2-017. Graph prerequisites still govern every opened task; an unavailable optional environment is not a new provisioning prerequisite.

## Classifications

| Task | Classification | Obligation parts reviewed | Evidence | Bound write scope and remaining scope | Conflicts / blockers |
|---|---|---|---|---|---|
| OPS.04 | gap | WP-45.03 (full); WP-45:browser-matrix-acceptance-status-page-su (browser matrix acceptance; status page supported/degraded/blocked browser behavior, static no-JS readability); WP-45:browser-matrix-acceptance-browser-suppor (package-level obligation contribution) | E1 | Web:apps/site/**/status/**. Remaining: An independently hosted status page publishes only user-facing capability components with an explicit reviewed health-to-component mapping, survives a full Cloud outage, and publishes its emergency alternate URL in at least three places. | None in adoption; normal graph prerequisites apply. |
| OPS.05 | gap | WP-45.04 (all work except the parts mapped to OPS.13); WP-45:operator-contract-closure-the-real-conso (operator contract closure; the real console join — wiring every generated role/method pair into the console UI); WP-45:browser-matrix-acceptance-supported-degr (browser matrix acceptance; supported/degraded/blocked browser behavior for the operator console's own flows); WP-45:browser-matrix-acceptance-browser-suppor (package-level obligation contribution) | E1 | Web:apps/app/**. Remaining: The operator console runs on a separate origin with a separate identity system, never in public navigation; support access is explicit, scoped, time-bounded, consented and audited; a destructive action needs a second authorised operator; and no parallel unversioned admin API exists. | None in adoption; normal graph prerequisites apply. |
| OPS.11 | gap | WP-45.10 (all work except the parts mapped to OPS.13) | E1 | Web:apps/app/**. Remaining: The operator console integrates WP-41 PackageCatalog operator methods (catalogReview/catalogRevoke) with independent operator authentication, step-up/evidence and audit, and review/revocation decisions visibly affect real signed catalog consumers. | None in adoption; normal graph prerequisites apply. |
| OPS.13 | gap | WP-45.04 (exercise every generated role/method pair via the actual console UI); WP-45.10 (real operator console join) | E1 | Task prompt has no write scope; bind integration evidence to owning apps/app feature and tests or Design acceptance record before edits, without enlarging implementation scope. Remaining: an authorised operator can actually grant/revoke/issueCredit/adjustCredit/refund and activate a kill switch through the console UI, not just via direct RPC test calls | No design contradiction; integration-only task has no declared source write scope. Before any source edit its claimant must obtain a reviewed scope binding/planning repair; evidence-only work stays within the ledger. |

## Review and ledger provenance

This ledger-only bundle is branch `task/adopt-09`; its PR, exact reviewed head and merge commit are recorded by the durable claim histories for ADOPT.09 and each slice. No implementation publication is produced. Source evidence and original receipt identities above remain immutable. No removed-product source cleanup is performed or certified.
