# AI adoption facts

ADOPT.08 repository record, prepared by AI integration owner `w-20260927-ai-lane` (role epoch 2). Governing authorities: Design P2-018 and ADP-01 through ADP-10; frozen Design `722e85641c8afb765dafcab5bc0e84d5a22d5a3c`.

## Frozen source and publication

AI main is `31f734d7b8aece5f1c87cfda9d5c6ce420bcfc40`, matching the clean inspected primary. [Retarget PR 22](https://github.com/ArcForges/AI/pull/22) was independently reviewed at `cdb1264bc4d89ab9014c3795f53e28256e54f4b8` and merged to that frozen head. Open PRs: none at baseline and adoption inspection. The baseline retains main and task/adopt-01 branch identities; no unpublished branch is counted as completed behavior.

[CI run 36334249591](https://github.com/ArcForges/AI/actions/runs/36334249591) passed its applicable source/offline, security, CodeQL, candidate, Verify, deployment and Verify deployment gates. The [original deployment receipt job](https://github.com/ArcForges/AI/actions/runs/36334249591/job/108662189499) and [verification job](https://github.com/ArcForges/AI/actions/runs/36334249591/job/108662252958) identify the build-once deployment. [Candidate ai-0.1.0-ci.68.1](https://github.com/ArcForges/AI/releases/tag/ai-0.1.0-ci.68.1) targets this source. Original asset identifiers are ai-worker.zip `593330244`, candidate.json `593330242`, deployment.json `593330246`; no bytes were fetched. These already recorded receipts are reused from the [frozen baseline](baseline.md#ai), not repeated publication verification.

## Actual layout, identities and pins

- One private npm workspace `@arcforges/ai`, AGPL-3.0-only, with `package.json` and committed `package-lock.json`. It produces a deployable Worker/Workflow candidate, not a published npm library.
- Worker and Workflow names `arcforges-ai-hello`; entry `src/index.ts`, class `HelloAgentWorkflow`, binding `HELLO_AGENT`, direct `AI` binding and `CF_VERSION` native version metadata. workers.dev and preview URLs are disabled; no public route is configured. Preserve these bootstrap identities until a scoped implementation migration is reviewed.
- Runtime sources: `src/index.ts`, `hello.ts`, `model.ts`, `model-diagnostics.ts`, `deployment.ts`, plus generated `env.generated.d.ts`. Existing tests are hello/model/diagnostics and explicit opt-in Workflow fixtures. No `src/workflows`, `src/providers`, `src/inference`, `src/streams`, `src/mcp`, `tests/ArchitectureTests`, `tests/provider-fixtures` or OwnApp integration tree exists.
- Runtime package pins: `@arcforges/proto` `1.0.0-ci.44.1`, `@bufbuild/protobuf` `2.15.0`. The older exact Contracts pin is a bootstrap input; each future generated-client consumer must adopt its required published closure through reviewed manifest/lock and admission changes, never sibling imports or copied DTOs.
- Toolchain: Node `24.21.0`, npm `11.19.0`, TypeScript `7.0.2`, Wrangler `4.135.0`, Workers types `5.20260918.1`, Vitest `4.1.11`, Cloudflare plugin `1.1.13`, Biome `2.5.14`, Prettier `3.9.8` and Node types `26.6.1`. No upgrade is performed by adoption.
- Existing policy roots: `eng/policy/licence-boundary.json`, dependency-policy/reuse-policy data and admission review; `eng/provenance/files.json`, records, artifact profiles and release provenance. These retain bounded WP02 checks, not the complete GOV.10 rule suite.
- New modules bind to this existing TypeScript workspace. Future module/inventory/lock changes belong to their implementation task. Workflow entry and route pins follow RES-ai-workflow-and-routes; configuration sections follow RES-private-configuration; architecture fixture registration follows RES-architecture-tests. No new project/package rename is implied by planned paths.

## Retained CI and evidence limits

`.github/workflows/ci.yml` is the retained workflow: Linux Source and offline units (binding freshness, project/licence/provenance policy, format, lint, typecheck, pure units and tooling); Repository security (audit, actionlint and secret scan); CodeQL JavaScript/TypeScript and Actions; PR-only Dependency review; Build candidate; Verify; main-only Deploy Cloudflare of the same candidate and Verify deployment. No macOS, hosted Workflow/inference, live probe, browser/device or installed-consumer gate is present. CI provider completion is not runtime acceptance.

`docs/validation.md` and `docs/evidence/*2026-09-14.json` retain bounded real Hello model/Workflow and deployment-admission observations. They explicitly do not prove production authorization, accounting, streaming, R2, load or full Harness behavior. Mock steps and historic model responses are not reused as current product acceptance. The preserved source inventory, PR/CI receipts and obligation definitions were read; no new product build or runtime verification was performed.

## Combined classification

All 12 tasks are gaps; none is inherited or closed. Their full remaining outcome, bound write scope and prerequisites are recorded individually in the slices below. GOV.10 remains a gap despite useful WP02 scaffolding because the mapped independent full rule suite does not exist. No D-001 conflict or AI-owned retired-family source cleanup is identified. Cleanup in Contracts/DesktopPlatform remains with its explicit owners and is not certified here.

| Task | Classification | Slice |
|---|---|---|
| AIR.00 | gap | [ADOPT.08.ai-routing](../tasks/adopt-08-ai-routing.md) |
| AIR.05 | gap | [ADOPT.08.ai-routing](../tasks/adopt-08-ai-routing.md) |
| AIR.07 | gap | [ADOPT.08.ai-routing](../tasks/adopt-08-ai-routing.md) |
| AIR.08 | gap | [ADOPT.08.ai-routing](../tasks/adopt-08-ai-routing.md) |
| EXT.10 | gap | [ADOPT.08.extensions](../tasks/adopt-08-extensions.md) |
| GOV.10 | gap | [ADOPT.08.governance](../tasks/adopt-08-governance.md) |
| HAR.00 | gap | [ADOPT.08.harness](../tasks/adopt-08-harness.md) |
| HAR.01 | gap | [ADOPT.08.harness](../tasks/adopt-08-harness.md) |
| HAR.02 | gap | [ADOPT.08.harness](../tasks/adopt-08-harness.md) |
| HAR.03 | gap | [ADOPT.08.harness](../tasks/adopt-08-harness.md) |
| HAR.05 | gap | [ADOPT.08.harness](../tasks/adopt-08-harness.md) |
| HAR.90 | gap | [ADOPT.08.harness](../tasks/adopt-08-harness.md) |
