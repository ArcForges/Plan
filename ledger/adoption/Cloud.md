# Cloud repository adoption facts

Frozen source: `60c5c4288b126c81a09fa5d1944671e9acb87495`; Design authority: `722e85641c8afb765dafcab5bc0e84d5a22d5a3c`. Reviewed by Cloud integration owner `w-20260927-cloud-lane` (role epoch 2). [ADOPT.01 baseline](baseline.md#cloud) holds the exact branch/PR/publication snapshot. No open Cloud PR at freeze; retained task/adopt-01 is the reviewed instruction branch, not unfinished product implementation.

## Source, identities and receipts

- Host: `src/ArcForges.Cloud/ArcForges.Cloud.csproj`, assembly/namespace `ArcForges.Cloud`; only Program, HelloEndpoint, BuildIdentity and HealthStatus source. Preserve identity when binding planned host paths. `Cloud.slnx`, Directory.Build.props/targets and Directory.Packages.props are shared roots.
- Worker: `worker/index.ts` and `worker/router.ts`; `wrangler.json` declares one `CloudContainer` DO, max_instances 1, lite instance, Hello rate limiter and arcforges.com/api route. No D1, Queue or R2 binding. The anonymous bootstrap route is a migration input, not the completed production routing graph.
- Tests: `tests/ArcForges.Cloud.Tests`, C# and Kotlin Hello consumers, and `tests/worker`; fixtures cover bootstrap routing/deadline/build identity/licence/provenance. No ArchitectureTests project or product module/transaction tests.
- Tooling: `tooling/project.ts`, cloudflare/build-identity/protocol/process/dependency-policy/licence/provenance/release tools. `eng/policy` and `eng/provenance` retain policy and immutable provenance revisions; `third-party` retains notices. No business storage/migrations/plans, BackgroundJobs or module implementation exists.
- Exact frozen producer pins: ArcForges.Build.Policy `1.0.0-ci.21.1`, ArcForges.Contracts.PublicApi and npm @arcforges/api-client `1.0.0-ci.74.1`. Current baseline producers are newer; consumers must update only the exact required published closure through reviewed pin/lock/admission changes, never adjacent source. The Kotlin Hello consumer pins `io.github.arcforges:contracts-connect-client:1.0.0-ci.42.1`; this is a separate historical probe pin, not proof of a matched current three-language closure. The npm workspace is private and does not publish a library.
- `Dockerfile` builds Linux x64 Native AOT with pinned .NET SDK 10.0.401 noble-aot and runtime-deps 10.0.12 noble-chiseled images, runs as APP_UID and preserves build identity/notices. No second host is needed. This is compilation/package posture, not authenticated provider acceptance.
- Instruction [PR22](https://github.com/ArcForges/Cloud/pull/22): reviewed `4f37ac16ec70ca421bc227c0c448fb424e5df53f`, merged at the frozen source. Eleven retained PR checks passed. [Main CI36335115598](https://github.com/ArcForges/Cloud/actions/runs/36335115598) and deployment succeeded. Candidate `cloud-0.1.0-ci.66.1`, original deployment receipt asset593358358, are recorded in the frozen baseline; no bytes re-downloaded.

## Retained CI and shared boundaries

The sole workflow `.github/workflows/ci.yml` retains Windows/Linux managed/source checks, Linux npm formatting/lint/type/offline tests, Kotlin compilation, dependency review/audit, licence/provenance, actionlint/gitleaks, C#/JavaScript CodeQL, Linux AOT container/Worker candidate, Verify and main candidate promotion/deployment. PR code receives no deployment secrets. Runtime commands are explicit local opt-in and are not evidence from this adoption review. No macOS/device/browser/live-inference CI is introduced.

Cloud integration ownership orders host registration, bindings, namespace reservations, plan-manifest regeneration and global migration numbering. A live test deployment phase requires RES-cloud-deployment's short exclusive lease; source work does not hold it while waiting. Product modules keep their own storage/plan ownership. Root dependency, project, provenance and workflow additions need scope binding before implementation; slices do not silently widen authority.

## Combined classifications

All 132 mapped Cloud tasks are gaps: bootstrap mechanisms are reusable inputs, but no task's full outcome and acceptance exists. None is inherited or retired as a completed product capability. Individual rows below are incorporated from the slice records; each record preserves bound scopes, complete remaining outcomes and limitations. ADOPT.07 is a review completion, not completion of these 132 tasks.

| Slice | Tasks | Classification |
|---|---:|---|
| [ADOPT.07.ai-routing](../tasks/adopt-07-ai-routing.md) | 6 | gap: AIR.01, AIR.02, AIR.03, AIR.04, AIR.06, AIR.90 |
| [ADOPT.07.cloud](../tasks/adopt-07-cloud.md) | 58 | gap: CLOUD.01, CLOUD.02, CLOUD.03, CLOUD.04, CLOUD.05, CLOUD.06, CLOUD.07, CLOUD.08, CLOUD.09, CLOUD.10, CLOUD.11, CLOUD.12, CLOUD.13, CLOUD.14, CLOUD.15, CLOUD.16, CLOUD.17, CLOUD.19, CLOUD.20, CLOUD.21, CLOUD.22, CLOUD.23, CLOUD.24, CLOUD.25, CLOUD.26, CLOUD.27, CLOUD.28, CLOUD.29, CLOUD.30, CLOUD.31, CLOUD.32, CLOUD.33, CLOUD.34, CLOUD.35, CLOUD.36, CLOUD.39, CLOUD.40, CLOUD.41, CLOUD.42, CLOUD.43, CLOUD.44, CLOUD.45, CLOUD.46, CLOUD.47, CLOUD.48, CLOUD.49, CLOUD.50, CLOUD.51, CLOUD.52, CLOUD.53, CLOUD.54, CLOUD.55, CLOUD.58, CLOUD.63, CLOUD.64, CLOUD.66, CLOUD.67, CLOUD.68 |
| [ADOPT.07.commerce](../tasks/adopt-07-commerce.md) | 15 | gap: COM.01, COM.02, COM.03, COM.04, COM.05, COM.06, COM.07, COM.08, COM.09, COM.10, COM.11, COM.12, COM.13, COM.14, COM.15 |
| [ADOPT.07.device-bridge](../tasks/adopt-07-device-bridge.md) | 9 | gap: DEV.01, DEV.02, DEV.04, DEV.06, DEV.07, DEV.08, DEV.09, DEV.12, DEV.13 |
| [ADOPT.07.extensions](../tasks/adopt-07-extensions.md) | 1 | gap: EXT.06 |
| [ADOPT.07.governance](../tasks/adopt-07-governance.md) | 1 | gap: GOV.09 |
| [ADOPT.07.harness](../tasks/adopt-07-harness.md) | 2 | gap: HAR.04, HAR.06 |
| [ADOPT.07.operations](../tasks/adopt-07-operations.md) | 9 | gap: OPS.01, OPS.02, OPS.03, OPS.06, OPS.07, OPS.08, OPS.09, OPS.10, OPS.12 |
| [ADOPT.07.policy](../tasks/adopt-07-policy.md) | 10 | gap: POL.01, POL.02, POL.03, POL.04, POL.05, POL.06, POL.07, POL.08, POL.10, POL.11 |
| [ADOPT.07.release](../tasks/adopt-07-release.md) | 3 | gap: REL.06, REL.08, REL.09 |
| [ADOPT.07.runtime-proofs](../tasks/adopt-07-runtime-proofs.md) | 1 | gap: PRF.07 |
| [ADOPT.07.search](../tasks/adopt-07-search.md) | 8 | gap: SRCH.00, SRCH.01, SRCH.02, SRCH.03, SRCH.04, SRCH.05, SRCH.06, SRCH.90 |
| [ADOPT.07.simulator](../tasks/adopt-07-simulator.md) | 9 | gap: SIM.01, SIM.02, SIM.03, SIM.04, SIM.05, SIM.07, SIM.08, SIM.09, SIM.10 |

## Findings and limits

PRF.07 requires a reviewed graph/write-scope repair before adding private Worker bindings and associated registries; its slice records that fence. CON.92 proves serialization posture, not later native/browser auth exception schemas, so implementation must resolve that producer edge before claiming their availability. Other tasks retain graph prerequisites and any row-specific path issue; absence of optional runtime environments never authorizes provisioning or a false completion.

Adoption used frozen source, task/obligation and original CI/provider evidence only. No new build, runtime, service, device/browser or artifact-download verification was run. No new substitutes or cleanup were introduced. Exact ledger PR review/merge evidence is preserved in the task claims and PR audit trail.

