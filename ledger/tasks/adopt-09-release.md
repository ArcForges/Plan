---
task: ADOPT.09.release
status: complete
recorded: 2026-09-27
claimant: w-20260927-web-lane
epoch: 1
---

# Web release adoption

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
| REL.05 | gap | WP-50.06 (full); WP-50.01 (Web's own npm SBOM/provenance and CLI evidence); WP-50:browser-matrix-acceptance-unlabeled-para (package-level obligation contribution) | E1, E4 | Web:eng/release/**; Design:docs/assurance/wp50-06-web-*.md. Remaining: Site/Account/Chat build once through the pinned Node/npm pipeline after current released proto-descriptor/C#/TS compatibility checks, promote the same artifacts with manifest and safe runtime-config schema, deploy atomically with per-origin edge routing/opaque cookie/CSRF policy/CSP, preserve old hashed chunks for the compatibility window, and roll back headers/assets/config coherently, while keeping production Node servers and esproj/npm installs out of Cloud runtime; the full browser-support.v1 matrix passes for supported/degraded/blocked behavior. | None in adoption; normal graph prerequisites apply. |

## Review and ledger provenance

This ledger-only bundle is branch `task/adopt-09`; its PR, exact reviewed head and merge commit are recorded by the durable claim histories for ADOPT.09 and each slice. No implementation publication is produced. Source evidence and original receipt identities above remain immutable. No removed-product source cleanup is performed or certified.
