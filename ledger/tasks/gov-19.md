---
task: GOV.19
status: complete
recorded: 2026-10-04
claimant: w-c20261004-aiwrangler
epoch: 1
---

# AI Wrangler and undici dependency admission

Complete. The task's acceptance is offline (the repository security gate and the dependency, provenance and candidate checks), and it was met on the merged main. Nothing below claims a live Cloudflare, Workflow or inference result.

## Evidence

All identities were read from GitHub and the local worktrees by the claimant `w-c20261004-aiwrangler` (epoch 1) on 2026-10-04. The independent review was written by a separate worker identity through the same GitHub account, so independence is by worker identity only.

- **Need.** AI main's unchanged lock failed `npm audit --audit-level=high` in the `Repository security` job: the published undici advisories (7.0.0 to 7.29.0) were reached through the locked `wrangler 4.135.0`, `miniflare 5.20260918.0-alpha` and `@cloudflare/vitest-plugin 1.1.13`, which pins Wrangler and Miniflare exactly. Every AI pull request, including GOV.10 (AI PR 28), was blocked. Cloud had admitted the same line as Cloud PR 32 under PRF.07.
- **Planning pair.** AI had no task covering a dependency admission, so [Design PR 214](https://github.com/ArcForges/ArcForges-Design/pull/214) (merged as `430718f`, approved at head `e40eaa1cb579bf1544803a1ff319b3d1a2ff7b97`) added GOV.19 with GOV.10 depending on it, and [Plan PR 269](https://github.com/ArcForges/Plan/pull/269) (approved at `f39771c9f37b1de6f03254c7db6f44eff915b94e`) regenerated the views and recorded the adoption adjustment. The first heads were returned for changes (missing GOV.10 start edge; GOV.10 numbering and its own `.gitleaks.toml` write).
- **Implementation.** [AI PR 29](https://github.com/ArcForges/AI/pull/29), merged as `19f52d3388366c8d66c8d75b5e9a9698a091b2fb` (merge commit) at the reviewed head `998cbf04fc14752d99a0af4953e48b423555f220`; approval [comment 5978642085](https://github.com/ArcForges/AI/pull/29#issuecomment-5978642085).
  - Versions: `wrangler` 4.135.0 to 4.143.1, `@cloudflare/vitest-plugin` 1.1.13 to 1.3.2 (the release pinning exactly Wrangler 4.143.1 and Miniflare 5.20260926.1-alpha), `@cloudflare/workers-types` 5.20260918.1 to 5.20260926.1; transitively `miniflare` 5.20260926.1-alpha, `workerd` and its five platform packages 1.20260926.1, `undici` 7.29.1 and `@cloudflare/unenv-preset` 2.16.2. Twelve lock entries changed; none added or removed. The closure equals Cloud's.
  - Records: receipt `wrangler-4-143-1-r1` (supersedes `admission-r1`), profile `ai-worker-r8`, `ai-worker-bundle-r8`, `wrangler-bindings-r3`, `files.json`, `NOTICE.txt`, README and `docs/development.md` text. The Wrangler generator commit is `d866c0922b8973b38aac0eddf1fdd86a3ac0c7bd`; the `bundle.ts`, `maybe-build-worker.ts` and `type-generation/helpers.ts` blobs and `LICENSE-MIT` equal those at the 4.135.0 commit, and `type-generation/index.ts` differs only by container_images binding emission, which AI's configuration never reaches (read through the GitHub contents API).
  - `.gitleaks.toml`: only the existing generic-api-key allowlist path pattern changed, `ai-worker-r[1234567]` to `ai-worker-r[123456789]`, plus its description. Regex, rule, scanner and workflow are unchanged. r9 is reserved for GOV.10's profile; GOV.10 must not rewrite the pattern.
  - Dependabot PR 27 (Wrangler 4.147.0, plugin 1.3.6) was not modified by this task; it is closed (state read after the merge). No other Dependabot PR was touched.
- **Hosted CI on the reviewed head** ([run 37191426908](https://github.com/ArcForges/AI/actions/runs/37191426908)): Repository security (npm audit `found 0 vulnerabilities`, the gitleaks history scan), Source and offline units, Build candidate, CodeQL, Dependency review and Verify passed; deploy jobs skipped on pull requests by design.
- **Main push** ([run 37193297497](https://github.com/ArcForges/AI/actions/runs/37193297497) on `19f52d3`): Source and offline units, Repository security, CodeQL (two), Build candidate, Verify, Deploy Cloudflare and Verify deployment succeeded (Dependency review skipped on pushes). Only provider job conclusions were read. The deployment is the standard candidate promotion; it is not a Workflow or inference test, and the Worker bytes were expected to be unchanged under r8 (not independently compared after deployment).
- **Local validation** (claimant; Node 24.21.0 and npm 11.19.0 from the repository pin, CPU-heavy runs through the build slot): `npm audit --audit-level=high` 0 vulnerabilities; `npm run check` (68 tooling tests among them), `check:dependencies` (195 dependencies, 8 inputs) and `test:artifact` (23 of 23) passed; `npm run types` left `src/env.generated.d.ts` unchanged.
- **Reviewer notes.** The reviewer cancelled its own local build-slot run after about 30 minutes of queueing, so its reproduction of the candidate build rests on hosted CI, and it did not observe the dependency-policy unit test count.

## Untested coverage

- No workerd runtime test (`test:runtime`), Workflow run, Workers AI inference or live Cloudflare check was run; the new Wrangler, Miniflare and workerd are exercised only by the offline tests, the candidate dry-run build and hosted CI.
- The Linux candidate build is evidenced only by hosted CI; no public artifact was downloaded.

## Remaining acceptance and next action

None for GOV.19. GOV.10 (AI PR 28) rebases over `19f52d3`, renumbers its profile and records to r9 and makes no `.gitleaks.toml` change.
