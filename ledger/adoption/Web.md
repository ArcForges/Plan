# Web repository adoption

Frozen Web main: `b0a6d7e1552d0a28f6abc30978cc25b7da3a8461`; Design `722e85641c8afb765dafcab5bc0e84d5a22d5a3c`. Integration owner for this review: `w-20260927-web-lane`, integration:Web epoch 2. The exact source, instruction PR, review and publication receipts are in [ADOPT.01 baseline](baseline.md#web). No open Web PR was present at review. Retained `task/adopt-01` is historical evidence, not unfinished product implementation.

## Actual inventory and scope binding

- One npm workspace/lock (`package.json`, `package-lock.json`): private AGPL identities `@arcforges/web-workspace`, `@arcforges/web-site`, `@arcforges/web-ui`. Members are `apps/site` and `packages/ui`; `apps/app` contains only its boundary README. Preserve these names; planned `src/Web/ArcForges.Web.App` binds to future `apps/app`, not a rename.
- Exact toolchain: Node `24.21.0`, npm `11.19.0`; TypeScript `7.0.2`, React `19.3.0`, Router `8.4.0`, Vite `8.3.0`, Tailwind `4.3.3`, Wrangler `4.135.0`. `apps/site` pins `@arcforges/api-client` and `@arcforges/proto` at `1.0.0-ci.44.1`. No root contract-fixtures dependency exists. Move exact consumer pins only when the implementing task consumes a published producer; adoption performs no pin updates.
- `apps/site/app/routes.ts` registers home/hello/cloud-hello and the router config prerenders those only with SSR disabled. No locale/documentation/version inventory, Account/Chat or operator implementation exists.
- Shared UI is `packages/ui/src/index.tsx` plus CSS. Root route registration and profile composition must follow the owning shell task; surfaces add scoped modules. New workspace/lock entries, origin edge directories and public-config schemas are explicit future additions, not present evidence.
- Build/policy/source tooling is `tooling/**`, declarations `eng/policy/**`, provenance inventory `eng/provenance/**`, tests `tests/unit`, `tests/provenance`, `tooling/dependency-policy.test.ts`. Formatter/linter are Prettier/Biome. Bind GOV.11 architecture lint additions to these existing mechanisms and `eng/policy`; do not rename packages to the planned paths or install ESLint merely because a scope mentions lint-config.
- Windows adapter is root `ArcForges.Web.esproj`, `win.slnx`, `Directory.Build.targets`. Deployment is `worker/index.js`, `wrangler.json`, `tooling/cloudflare.ts`; Account/Chat `deploy/edge` profiles do not yet exist. Cloud owns `/api/*`; Web is not a second business host.
- Shared protocols: append required workspace, lock, CI and budget entries; regenerate the single lock after rebase, never hand-merge it. Shared UI additions belong to WEB.08; surface callers coordinate with that owner. Contract pins use RES-contract-consumer-pins. Root routes and composition follow their owning tasks.

## Retained CI and publication

`.github/workflows/ci.yml` retains Linux Node source/static/offline checks; Windows evaluated esproj declarations; dependency audit, actionlint and secret scan; PR dependency review; CodeQL JavaScript/TypeScript and Actions; one Linux static candidate; Verify; main-only Cloudflare deployment. No macOS, browser/device/live-service or inference CI is introduced. Local browser scripts are opt-in only.

Baseline main CI 36334763241 succeeded and published `web-0.1.0-ci.62.1`, Cloudflare version `4f9bd451-88de-483b-95a9-a95cf1846ea2`; original receipt artifact `10936629029`. These are static bootstrap build/deployment facts, not runtime or product acceptance. Private workspaces are not published npm libraries. No receipt downloads, product builds or runtime tests were repeated.

## Combined classification

Forty tasks: 39 gaps, one inherited with adjustment (GOV.11), zero inherited completions, zero conflicting classifications. Source cleanup remains owned by CON.23/GOV.17/GOV.18 in their repositories. Blank source scopes in integration-only tasks require an explicit reviewed binding before source changes and do not grant arbitrary write authority. No manual login or adoption environment blocker exists.

| Task | Classification | Slice record |
|---|---|---|
| GOV.11 | inherited with adjustment | [ADOPT.09.governance](../tasks/adopt-09-governance.md) |
| OPS.04 | gap | [ADOPT.09.operations](../tasks/adopt-09-operations.md) |
| OPS.05 | gap | [ADOPT.09.operations](../tasks/adopt-09-operations.md) |
| OPS.11 | gap | [ADOPT.09.operations](../tasks/adopt-09-operations.md) |
| OPS.13 | gap | [ADOPT.09.operations](../tasks/adopt-09-operations.md) |
| REL.05 | gap | [ADOPT.09.release](../tasks/adopt-09-release.md) |
| PRF.08 | gap | [ADOPT.09.runtime-proofs](../tasks/adopt-09-runtime-proofs.md) |
| WEB.01 | gap | [ADOPT.09.web](../tasks/adopt-09-web.md) |
| WEB.02 | gap | [ADOPT.09.web](../tasks/adopt-09-web.md) |
| WEB.03 | gap | [ADOPT.09.web](../tasks/adopt-09-web.md) |
| WEB.04 | gap | [ADOPT.09.web](../tasks/adopt-09-web.md) |
| WEB.05 | gap | [ADOPT.09.web](../tasks/adopt-09-web.md) |
| WEB.06 | gap | [ADOPT.09.web](../tasks/adopt-09-web.md) |
| WEB.07 | gap | [ADOPT.09.web](../tasks/adopt-09-web.md) |
| WEB.08 | gap | [ADOPT.09.web](../tasks/adopt-09-web.md) |
| WEB.09 | gap | [ADOPT.09.web](../tasks/adopt-09-web.md) |
| WEB.10 | gap | [ADOPT.09.web](../tasks/adopt-09-web.md) |
| WEB.11 | gap | [ADOPT.09.web](../tasks/adopt-09-web.md) |
| WEB.12 | gap | [ADOPT.09.web](../tasks/adopt-09-web.md) |
| WEB.13 | gap | [ADOPT.09.web](../tasks/adopt-09-web.md) |
| WEB.14 | gap | [ADOPT.09.web](../tasks/adopt-09-web.md) |
| WEB.15 | gap | [ADOPT.09.web](../tasks/adopt-09-web.md) |
| WEB.16 | gap | [ADOPT.09.web](../tasks/adopt-09-web.md) |
| WEB.17 | gap | [ADOPT.09.web](../tasks/adopt-09-web.md) |
| WEB.18 | gap | [ADOPT.09.web](../tasks/adopt-09-web.md) |
| WEB.19 | gap | [ADOPT.09.web](../tasks/adopt-09-web.md) |
| WEB.20 | gap | [ADOPT.09.web](../tasks/adopt-09-web.md) |
| WEB.21 | gap | [ADOPT.09.web](../tasks/adopt-09-web.md) |
| WEB.22 | gap | [ADOPT.09.web](../tasks/adopt-09-web.md) |
| WEB.23 | gap | [ADOPT.09.web](../tasks/adopt-09-web.md) |
| WEB.24 | gap | [ADOPT.09.web](../tasks/adopt-09-web.md) |
| WEB.25 | gap | [ADOPT.09.web](../tasks/adopt-09-web.md) |
| WEB.26 | gap | [ADOPT.09.web](../tasks/adopt-09-web.md) |
| WEB.27 | gap | [ADOPT.09.web](../tasks/adopt-09-web.md) |
| WEB.28 | gap | [ADOPT.09.web](../tasks/adopt-09-web.md) |
| WEB.29 | gap | [ADOPT.09.web](../tasks/adopt-09-web.md) |
| WEB.30 | gap | [ADOPT.09.web](../tasks/adopt-09-web.md) |
| WEB.31 | gap | [ADOPT.09.web](../tasks/adopt-09-web.md) |
| WEB.32 | gap | [ADOPT.09.web](../tasks/adopt-09-web.md) |
| WEB.33 | gap | [ADOPT.09.web](../tasks/adopt-09-web.md) |
