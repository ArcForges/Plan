---
task: OPS.01
status: complete
recorded: 2026-09-28
claimant: af-20260928-ops01-pui
epoch: 1
---

# Service levels and alerting

## Evidence

- Implementation: Cloud [PR #23](https://github.com/ArcForges/Cloud/pull/23), reviewed exact head `7ebf2993a5c766cfc84a1af85bb2c2986017d08c` by c01 ([exact-head review](https://github.com/ArcForges/Cloud/pull/23#pullrequestreview-5338606960)); merged at `44d0a22de705a265b9dcee70f4d689df6e248238`. The exact-head PR CI run [36421246633](https://github.com/ArcForges/Cloud/actions/runs/36421246633) completed successfully.
- The delivery adds capability-group user-visible SLI objectives and bounded indicator calculations; realtime and managed-AI availability and error budgets are computed independently. It defines the 11 enumerated page-worthy alerts with page/ticket/dashboard routing, and gives every page alert a linked, indexed existing response runbook. Alert-to-runbook and routing completeness are checked offline, including negative cases. The alert/runbook files follow the `RES-cloud-runbooks-and-fixtures` append protocol; the scoped runbooks do not claim OPS.03's broader rehearsal acceptance.
- Full local `npm run check` passed on the exact implementation head, including the pinned toolchain and dependency, licence, provenance, format, lint, typecheck and test gates; `npm test` passed 72/72, including all nine OPS.01 monitoring tests. `git diff --check` passed and dependency closure and lockfiles were unchanged.
- Normal post-merge Cloud workflow [36422780088](https://github.com/ArcForges/Cloud/actions/runs/36422780088) completed successfully on merge `44d0a22de705a265b9dcee70f4d689df6e248238`. Applicable repository/policy checks, Ubuntu source checks, Windows managed compile/licence, Native AOT image and Worker candidate, Verify, and CodeQL succeeded. The Cloudflare deploy job succeeded; dependency-review was skipped as expected for the push event.
- Publication and deployment receipt: prerelease [Cloud 0.1.0-ci.68.1](https://github.com/ArcForges/Cloud/releases/tag/cloud-0.1.0-ci.68.1), tag `cloud-0.1.0-ci.68.1`, published 2026-09-28T12:39:09Z. The release's `deployment.json` records revision `44d0a22de705a265b9dcee70f4d689df6e248238`, version `0.1.0-ci.68.1`, image ID `sha256:073ca8e631cf1a5c292ca51669bd793753a5b87dd89001a4a3539c8a24511d4c`, image digest `registry.cloudflare.com/85a6bb957ba952261f6d177217ca9919/arcforges-cloud@sha256:3ffc37d3057873e2409bed9fb5a668efae18fac71f2fca0c1e9c7b64331ac834`, base URL `https://arcforges.com/api`, and deployedAt `2026-09-28T12:39:05.315Z`. The workflow retained deployment evidence as artifact `cloudflare-evidence-36422780088-1` (artifact ID `10969644822`); release assets include `deployment.json` (SHA-256 `c40846a481996096e479c14f14b8e1c5fad6bb6428e857fc4d77bb580e6cc06d`) and the published Cloud tarball (SHA-256 `143917400afdec81968190d2e8477176648d9ff453678957dabd6f59a254c1dd`).
- Obligations satisfied: [WP-45.00](https://github.com/ArcForges/ArcForges-Design/blob/main/docs/planning/work-packages/45-operations-support-and-trust-safety.md#rule-wp-45.00), full. Completion evidence is the offline alert-to-runbook completeness assertion and the successful deployed candidate publication above. OPS.01 has no completion prerequisites.
- Substitutes still in use: none recorded.
- Untested coverage: no live provider-outage injection or historical production telemetry window was exercised; the task's required synthetic-failure, dependency-attribution, routing and completeness validation is offline. No OPS.03 runbook rehearsal is claimed.
- Remaining completion prerequisites and next action: none.
