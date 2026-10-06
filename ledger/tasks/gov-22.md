---
task: GOV.22
status: complete
recorded: 2026-10-06
claimant: w-codex-20261006-identity
epoch: 1
---

# Cloud devtool sharp security admission successor

Complete implementation, review, CI, normal production deployment and publication. This record does not claim whole-system commercial acceptance or provider authentication acceptance.

## Change and admitted dependency closure

- [GHSA-wq5f-xc86-pv6w](https://github.com/advisories/GHSA-wq5f-xc86-pv6w), published 2026-10-06, affected the locked Sharp 0.35.4 devtool transitive dependency. The exact nested `miniflare` → `sharp` 0.35.5 override patches it; Wrangler remains 4.143.1 and Miniflare remains 5.20260926.1-alpha. No broad automatic upgrade or audit suppression occurred.
- The actual lock successor changes 27 existing entries, including Sharp's optional platform packages and libvips 1.3.3 → 1.3.4; no lock entries were added or removed, and licence expressions remain unchanged. The actual installation and licence files informed the admission, rather than a hash-only refresh.
- Immutable release profile `cloud-release-r37`, admission `gov-22-r1`, and artifact records `gov-22-cloud-runtime-notices-r1` and `gov-22-cloud-worker-bundle-r1` supersede their active predecessors, preserving every historical record. The profile owns source commit `6b7999fe7ee47d3801efe10b5ab4c3ce5efd5a5d`. The Worker inputs and bundle identity are unchanged; the image input successor changes the actual lock hash. Production runtime/provider dependency coordinates, source behavior, schema, routes, and permissions were not changed by this fix.
- Source scope and execution authority came from merged Design `3c1453e` and Plan `e7462c014d25919a06ef2fd2f31168652b3c96d4`. The dependency-admission obligation is WP-02.05; the launcher's erroneous WP-05.06 mapping is corrected by the separately reviewed planning successor. No specification-integrity obligation is weakened.

## Independent review and integration

- Claim epoch 1: `w-codex-20261006-identity`, latest source-review checkpoint `claims/gov-22` at `6a0f7e2338bb2a69bb9a1d9ea2e5d3c7ea89480e`.
- Cloud [PR #65](https://github.com/ArcForges/Cloud/pull/65) at independently approved exact head `ba889b9fece22ef7a4f7df90c8f138159fa3a764`; review by distinct worker `w-codex-20261006-pat` in [approval receipt](https://github.com/ArcForges/Cloud/pull/65#issuecomment-6021508166). The review approved source and admission, with CI/deployment retained as delivery gates.
- Merged using the held `integration:Cloud` epoch 1 role, receipt `bccd31d29c00`, fenced to the reviewed head. Merge `14f7bbe0c0fcd5f9ab2749dfbc1ff0374ba9ddb3` at 2026-10-06T17:20:15Z. Worktrees and task branches are retained.

## Validation evidence

Claimant-reported local validation on Windows, Node 24.21.0, through the workstation build slot where applicable:

- Actual `npm ci --ignore-scripts`: 49 packages installed, 50 audited; `npm audit --audit-level=high`: zero vulnerabilities. `npm ls` confirms the exact override under the unchanged Wrangler/Miniflare coordinates.
- `npm run check`: 754 tests passed, no skips or failures; storage-plan/migration, dependency/licence/provenance, naming, formatting, lint and type checks passed. `npm run test:artifact`: 10 passed; actual locked Wrangler dry-run bundle matched the prior admitted Worker. Local legal-image fixtures are not evidence of a real container build or OS isolation.
- Latest-head hosted [PR CI 37501504578](https://github.com/ArcForges/Cloud/actions/runs/37501504578): source on Windows and Ubuntu, dependency audit/review, architecture policy, all four CodeQL jobs, real Native AOT container image inspection and Worker build, and Verify passed. Deployment was appropriately skipped on the PR.
- Hosted [main CI 37502761761](https://github.com/ArcForges/Cloud/actions/runs/37502761761) on the exact merge: all applicable source/security/image/Verify jobs and normal production deployment passed. Proof deployment was not requested.

## Actual production delivery and publication

- Deployment receipt: revision `14f7bbe0c0fcd5f9ab2749dfbc1ff0374ba9ddb3`, version `0.1.0-ci.246.1`, deployed 2026-10-06T17:29:18.194Z, base `https://arcforges.com/api`. Provider-reported Worker version `babe1ff1-98ac-4c34-a0a8-58eae5da0aaa`; existing route `arcforges.com/api/*` remains attached. Container application `a0322dd7-048e-435c-bb15-116e6878b104` retains its `lite` configuration. Checked-in production configuration retains `workers_dev: false` and disabled preview URLs; this task changed neither.
- Image ID `sha256:c7057a507d1030e8343b3bea24a1eb91b71c5ad126533072028796ff3d940414`; deployed image digest `sha256:e809c6bcc312c87a83ceacd1287124d2e49088d0905fdebf51537b4780816a2e`. Migration gate reports `not-applicable`: production declares no D1 database, so no production data migration occurred.
- Published [cloud-0.1.0-ci.246.1](https://github.com/ArcForges/Cloud/releases/tag/cloud-0.1.0-ci.246.1), target the exact merge. The release includes the actual candidate tarball (14,105,624 bytes, SHA-256 `7d1f89e5141519236df10d74e10f2ab8eab9322392bc5414b02a348c974010ca`) and deployment receipt (431 bytes, SHA-256 `c9ce904d72a150dbe5eee05eaa914a80064fc78e038335a4bdfe17e8bf3a96e0`). Hosted evidence artifact `cloudflare-evidence-37502761761-1`, ID 11430368537, preserves the deployment and migration receipts.
- Claimant-observed after deployment: read-only `GET https://arcforges.com/api/healthz` returned HTTP 200 and `nativeAot: true`, exact merge, release `0.1.0-ci.246.1`, and build ID `37502761761.1`. No local credentials or secret values were read or printed.

## Remaining checks and owners

No remaining implementation or human-only blocker for GOV.22. No acceptance test was replaced with a mock. Full Identity/provider/OS/commercial-series acceptance belongs to the corresponding implementation and acceptance tasks; it is outside this security successor's obligation. Future devtool advisories remain owned by the normal dependency-admission mechanism.
