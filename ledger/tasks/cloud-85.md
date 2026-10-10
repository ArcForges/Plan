---
task: CLOUD.85
status: complete
recorded: 2026-10-09
claimant: w-deku-20261009-cloud-85
epoch: 1
---

# Serve the Blazor WebAssembly Account and Chat profiles and the C# static Site from the proof origin

## Evidence

- Implementation, in one Cloud pull request (brief S20(a), S20(c), S25, S27, S28(j), S31 and S32):
  - Cloud [PR #81](https://github.com/ArcForges/Cloud/pull/81), "[CLOUD.85] Serve the Blazor WebAssembly Account and Chat profiles and the C# static Site from the proof origin", head branch `task/cloud-85`, was reviewed and merged at head `036e4c4e21ac9cc7a1328650b9cd19fa08e6c7fd` as `3980212301349c71442cc3eb9bc9f410fbf5458d` on `main` at 2026-10-09T19:16:38Z. The merge commit has two parents, `ccf7bcdf7d8502c7db3fa644738908bf912a7f9f` (the previous main, the HAR.40 merge) and `036e4c4e`, which is consistent with the `--merge` method (verified from the commit). The `--match-head-commit 036e4c4e` flag and the `integration:Cloud` role, held by `w-deku-20261008-coord`, are coordinator-reported; neither is visible in the PR text.
  - The merge changes 11 files (2176 insertions, 406 deletions) and no path under `worker/**`. The only `wrangler.json` change is one line in the `env.proof` static-assets block: `not_found_handling` moves from `none` to `404-page` (D6). Production configuration is unchanged. No release artifact profile is added. The independent reviewer recorded at `e8cf8a04` that the `cloud-release-r37` Worker and image inputs are unchanged at the head, so no successor profile is required.
  - Dependency receipts: `eng/policy/dependency-reviews/cloud-85-r2.json` is the successor of `har-40-r14` (its `previous` and `supersedes` fields name `har-40-r14`) and is the review record that `eng/policy/dependency-policy.json` binds. Its reviewer is `w-deku-20261009-rev-cloud-85` and its decision is `approved`. `cloud-85-r1.json` (reviewer and decision as above, chained from `capacity-pacer-retire-r2`) stays as immutable history (S32(a)).

- Review trail (Cloud PR #81). The PR has one comment, [6087346419](https://github.com/ArcForges/Cloud/pull/81#issuecomment-6087346419) (2026-10-09T18:59:19Z), and no GitHub review events. It records `approved` for `036e4c4e` as an independent exact-head review by the session `w-deku-20261009-rev-cloud-85`:
  - a full review at `e8cf8a04` (U1 to U6);
  - a delta review at `c08a440a`, the merge of main with HAR.40, with receipt `cloud-85-r2` superseding `har-40-r14` (S32(a));
  - a delta review at `036e4c4e`, where `ping` is checked per entry (S32(b)).
  The comment reports the deltas' gates (npm 829, dotnet 1399 passed and 1 skipped, format, policy, provenance, licence, dependencies 18 of 18, audit 0, gitleaks 0 findings over 323 commits) and the non-blocking carried items: `srcset` is missing from the docs url-attribute list; svg `xlink:href`, inline style `url()` and `longdesc` are not covered by the verifier (S32(c), pre-existing); the live-only checks are completion evidence from the observe runs and the L3 checks; the Node toolchain pin, the Docker candidate and RP-09 were not run locally. The PR author, the approving comment and the merge are all under the one GitHub account `deku2026`. Independence is by session only, as the coordinator's rules define.

- Hosted runs. All are in `ArcForges/Cloud`. Job conclusions were read with `gh run view --json jobs`; log lines were grepped for specific results, and no secret value was printed.
  - Main CI run [37979115366](https://github.com/ArcForges/Cloud/actions/runs/37979115366) (push, head `3980212`, created 19:16:41Z, completed 19:26:07Z) succeeded: Dependency audit and repository checks, both Source jobs, the CodeQL jobs, Native AOT image and Worker build, Verify and Deploy Cloudflare. Deploy Cloudflare proof environment was skipped on the push, so the push deployed production only.
  - The deploy job published prerelease `cloud-0.1.0-ci.330.1` (target `3980212`; assets `cloud-0.1.0-ci.330.1.tar.gz`, 14216450 bytes, and `deployment.json`, 431 bytes; read with `gh release view`, not downloaded).
  - Production `https://arcforges.com/api/healthz`, read by this author on 2026-10-09, returned `revision` `3980212301349c71442cc3eb9bc9f410fbf5458d`, `artifact.version` `0.1.0-ci.330.1`, `build.buildId` `37979115366.1`, `nativeAot` true.
  - Proof observe run [37980332646](https://github.com/ArcForges/Cloud/actions/runs/37980332646) (workflow_dispatch, before the deploy) succeeded, including Proof Cloudflare access and resources. Its `observe:proof` output records the proof Container application `arcforges-cloud-proof-foundationcontainer-proof` at version 12, `max_instances` 4, image `sha256:e64bb000…`.
  - Proof deploy run [37981418458](https://github.com/ArcForges/Cloud/actions/runs/37981418458) (workflow_dispatch, under the `RES-cloud-deployment` lease, which the coordinator reports as held by `w-deku-20261009-cloud-85`, epoch 1, and now released) succeeded. Its job "Deploy Cloudflare proof environment" (113996025855) succeeded and logged:
    - `Web web-0.1.0-ci.111.1: profile bundle 4afc8f28… and Site 57357561… verified; 177 files staged as the proof assets.`
    - `Read 183 files from the assets directory`, then `Found 173 new or modified static assets` and `Success! Uploaded 173 files (3 already uploaded)`. The log does not reconcile the 177 and 183 counts.
    - `No migrations to apply!` (the gated proof D1 step).
    - `Pushed image: …arcforges-cloud:ci.332.1`, digest `sha256:68dd7042…`.
    - `Current Version ID: 745d5ec7-db42-4b10-967b-ae2a486314b4`.
    - `Proof environment deployed at https://proof.arcforges.com. This is deployment completion, not live acceptance evidence.`
    - Evidence artifact `proof-evidence-37981418458-1` uploaded (ID 11641665936).
    The proof `https://proof.arcforges.com/api/healthz`, read by this author on 2026-10-09, returned `revision` `3980212301349c71442cc3eb9bc9f410fbf5458d`, `artifact.version` `0.1.0-ci.332.1`, `build.buildId` `37981418458.1`.
  - Closing observe run [37982727325](https://github.com/ArcForges/Cloud/actions/runs/37982727325) (workflow_dispatch, after the deploy) succeeded, including Proof Cloudflare access and resources. Its `observe:proof` output records the proof Container at version 13 with image `sha256:68dd7042…`, the image the deploy pushed. The record reports this rollout and does not assess it; the CLOUD.85 write list names no container file.

- Live checks (L3), read-only `curl` by the coordinator at 2026-10-09T19:49:12Z, saved as `cloud85-l3.txt` in the coordinator's scratchpad and read by this author. These are HTTP status and header checks. They are not an in-browser WASM boot.
  - `/`, `/hello/` and `/cloud-hello/` return 200 with the Site policy `script-src 'self'`, with no WebAssembly token.
  - `/account/` and `/chat/` return 200 with `script-src 'self' 'wasm-unsafe-eval'`. Each response carries exactly one `Content-Security-Policy` header, so the inherited Site policy is not sent on the profile routes. The `/account/` body has `<base href="/"`.
  - `/favicon.svg` (image/svg+xml), `/robots.txt` (text/plain) and `/_framework/blazor.webassembly.js` (text/javascript) return 200.
  - `/no-such-page-xyz` returns 404 text/html with the Site policy, which is the `404-page` handling of D6.
  - `/api/healthz` returns 200 application/json with `Cache-Control: no-store`. `/session/v1/x` returns 404 text/plain and `/proof/v1/x` returns 401, both `no-store`. These are consistent with the Worker answering its route families ahead of assets. Header checks alone do not prove that.

- Offline validation, in Cloud (hosted Source (ubuntu-latest) job of run 37981418458, `npm run check`: `tests 829, pass 829, fail 0`; the Source (ubuntu-latest) job of main CI run 37979115366 also succeeded). The tests named below are in `tests/worker/` at the merge commit:
  - "the Worker answers every one of its own route families before any asset" (`proof-assets.test.ts` line 198): route precedence;
  - "a well-formed WEB.40 bundle verifies and a digest that is not the pin is refused first" (line 321) and "an asset that does not match its pinned digest stops the staging before anything is written" (`proof-cloudflare.test.ts` line 327): digest refusal;
  - "each profile's policy is the one its page derives, with the exact WebAssembly token set" (`proof-assets.test.ts` line 600): the App-profile CSP token set;
  - "the composed headers keep each surface's rules and unset the Site policy under the profiles" (line 1218): the `_headers` composition;
  - "the codebase, archive, ping and imagesrcset attributes refuse a foreign entry in any position" (line 821), "the two profile pages are one shell and every reference stays on the root" (line 485) and "page references are refused unless they are plain same-origin paths" (line 748): same-origin resolution under base href `/`.

- CLOUD.71 and CLOUD.85 bundle-naming coordination note (WEB.40 gap 1, S28(j)):
  - The WEB.40 release assets, in release `web-0.1.0-ci.111.1` of `ArcForges/Web` (a prerelease, not a draft, published 2026-10-09T14:40:06Z; checked with `gh release view`, by name and size only, nothing downloaded):
    - `web-profiles-4afc8f285a7a64202ce221bc4e3011a9f8b6de641d50eef0a537677e80eaef9a.tar` (18636800 bytes), the Account and Chat profile bundle;
    - `web-site-573575617dec11d2d3678bf5ccd92728190b64a79e7907e050764fd8a1d131ac.tar` (26112 bytes), the C# public Site.
  - Where CLOUD.85 pins them: `eng/verification/proof-deploy.ts` at `3980212`. `profileBundlePin` is at lines 27 to 31 (`release` at line 29, `digest` at line 30), and `profileBundleAssetName` is at line 32. `siteArchivePin` is at lines 37 to 41 (`release` at line 39, `digest` at line 40), and `siteArchiveAssetName` is at line 42. Both pins name `web-0.1.0-ci.111.1`.
  - The CLOUD.71 React pin `web-0.1.0-ci.90.1` (published 2026-10-06T00:25:52Z) is no longer referenced by Cloud source. The only occurrence in source is the negative assertion `assert(!source.includes("web-0.1.0-ci.90.1"), rel)` at `tests/worker/proof-assets.test.ts` line 313. `docs/prf-07-foundation-proof.md` line 320 names it as history. It stays as history in the Web release, which still exists.

- PRF.11 clause of the evidence: "PRF.11's deployed proof-origin same-origin and base-href record cites this task". Not met. PRF.11 has no ledger record on Plan `main` (baseline `not-started`), and its local opt-in live run against the proof origin is not recorded.

## Scope (2026-10-09)

- Delivered outcome: on the proof origin only (`env.proof`), the Cloud Worker's static-assets binding serves the WEB.40 Blazor WebAssembly Account and Chat profiles and the C# public Site, from the digest-verified release assets named above. `/api/*`, `/session/v1/*` and `/proof/v1/*` are routed to the Worker first. The profiles are served under base href `/`, with the framework at the root and the shells at `/account/` and `/chat/`. Each surface has its own CSP token set, and the Site's policy carries no WebAssembly token. The Worker has no `worker/**` change and makes no business decision.
- Production boundary: production `main` is at `3980212` and serves no assets. The only configuration change is `env.proof`, as the diff above shows.
- Gaps against the status rule. Each gap is named, with its next action.
  1. **PRF.11 record cites this task (Evidence): not met.** *Next action:* PRF.11's local opt-in live run against `proof.arcforges.com` records its same-origin and base-href results and cites CLOUD.85. Then this record is updated to `complete` in a follow-up. This is the only open clause of the CLOUD.85 record. Gaps 2 and 3 below are not open CLOUD.85 clauses: the record's validation assigns the deployed-origin browser run to PRF.11, so they are listed for traceability and close with gap 1.
  2. **D4 live check (S20(c), "verified live on the proof origin"): met at header level only.** The L3 check shows one CSP header on each profile route, and the Site policy on the Site routes. Browser-level behaviour of the composed `_headers` is PRF.11's (see Untested coverage).
  3. **Browser-level acceptance of the profiles** (in-browser WASM boot of the shells, base-href resolution in a browser, browser enforcement of the CSP token sets): the validation clause assigns the deployed-origin run to PRF.11's local opt-in acceptance. *Next action:* PRF.11, as in gap 1.
- The proof deploy's evidence artifacts (`proof-evidence-37981418458-1`) were not downloaded or read by this author. The deploy log lines above are the evidence cited.

## Untested coverage (stated expressly)

- **In-browser behaviour.** The Blazor WebAssembly boot of the Account and Chat shells on `proof.arcforges.com`, base-href resolution in a browser, and the browser's enforcement of the CSP token sets are untested here. PRF.11 owns them.
- **Live checks are headers and status codes only** (L3, `curl`). The `/chat/` base href was not captured, and the bodies of `/hello/`, `/cloud-hello/` and the 404 page were not checked.
- **`_headers` on the profile routes.** The unset-then-set behaviour is observed only as one CSP header per profile response. The composed `_headers` file as served was not fetched.
- **Route precedence** is checked by header on three paths only (`/api/healthz`, `/session/v1/x`, `/proof/v1/x`). It is not tested for every route family against live responses.
- **Shell hashes.** The served `/account/` and `/chat/` CSP headers carry no hash tokens. This record does not assert whether a hash is required; the offline test "each profile's policy must cover its own inline scripts" (in `proof-assets.test.ts`) covers the rule in Cloud.
- **Verifier coverage** (S32(c), pre-existing): svg `xlink:href`, inline style `url()` and `longdesc` are not checked. The docs url-attribute list omits `srcset`, which the verifier does check.
- **Asset counts.** The deploy log shows 177 staged, 183 read and 173 uploaded (3 already uploaded). The log does not reconcile them, and this record does not claim a reconciliation.
- **Proof container rollout.** The deploy pushed `ci.332.1` (`sha256:68dd7042…`), and the proof Container application moved from version 12 to 13 (observe runs above). The CLOUD.85 write list names no container file. The record reports the rollout and does not assess it.
- **Release contents.** The WEB.40 release assets were not downloaded by this author. Their digests were verified by the deploy job (log line above), and their sizes come from the release listing.
- **Local gates.** The npm, dotnet, policy, provenance and dependency figures in the PR comment were not re-run by this author. The hosted Source job figures are cited above. The Node 24.21 toolchain pin (local 24.20) and the Docker candidate were not run locally.
- **Independence.** All approvals, the PR and the merge are under one GitHub account (`deku2026`). Independence rests on the separate reviewer session `w-deku-20261009-rev-cloud-85`.
- **Coordinator-reported facts.** The `--match-head-commit` flag, the `integration:Cloud` role and the `RES-cloud-deployment` lease are coordinator-reported. The two-parent merge commit is verified.
- **Production.** Production serves no assets, so the static-assets behaviour is not observed in production.

## Completion follow-up (2026-10-10, epoch 2, DLV-41): S36 follow-up evidence

This section appends to the first delivery's record and does not rewrite it. The first delivery's pins to `web-0.1.0-ci.111.1` and its gaps stand as history, except where this section says otherwise. The follow-up is the CLOUD.85 part of brief section 11, S36(2): the verifier's expected profile policy uses `base-uri 'self'`, the Site expectation is unchanged, and the pins move to the corrected Web release. Claimant `w-deku-20261009-cloud-85`, epoch 2.

- **Pull request and merge** (job- and API-observed by this author; approval text read from the PR comment):
  - Cloud [PR #82](https://github.com/ArcForges/Cloud/pull/82), "[CLOUD.85] Expect base-uri 'self' for profiles and pin web-0.1.0-ci.117.1 (completion follow-up)", head branch `task/cloud-85`, was approved at head `34aa2f9c9be2a23cb14c59a5abf1f32fa0fa2230` (comment [6091077429](https://github.com/ArcForges/Cloud/pull/82#issuecomment-6091077429), 2026-10-09T23:34:58Z) and merged as `3c59ce34413c94c86ce400fd2950b6372d45abbd` on `main` at 2026-10-10T00:09:24Z. The merge commit message is "Merge pull request #82 from ArcForges/task/cloud-85".
  - The approving comment is an independent exact-head review by the session `w-deku-20261009-rev-cloud-85`. It reports 2 commits and 3 files, all inside the CLOUD.85 writes; no `wrangler.json` or production configuration change; and no `111.1` pin string left. The reviewer ran four mutation checks in a scratch copy, and each made an intended test fail. The approval and the merge are under one GitHub account, so independence rests on the session, as in the first delivery.
  - Pins on `main` at `3c59ce34`, read with `gh api` and checked by this author: `eng/verification/proof-deploy.ts` names release `web-0.1.0-ci.117.1` at line 29 (profile bundle, digest `2070acd93565eceb190f872505c85fcd6c40ef71643aff4924ba1f026ff87001`, line 30) and at line 39 (Site, digest `735374a56bce3e63dabcb0a4abaa25a1d6ae23a0890eade5c8273bf110bfb0a8`, line 40). The release is Web's `web-0.1.0-ci.117.1` (prerelease, target `049f6a58583c2b88ed03232d7d18bb975c428a95`, published 2026-10-09T23:12:27Z); its profile tar is 18636800 bytes and its Site tar is 26112 bytes. The bytes were not downloaded here.
  - The reviewer explains the Site digest change from the Web source: `SiteBuilder.SourceUrl` embeds `--source-ref $GITHUB_SHA`, and there is zero Site source diff between Web `c8588681` and `049f6a58`.
- **Offline gates in Cloud**: the approving comment reports npm test 830, dotnet test 1399 passed and 1 skipped, format, lint, typecheck, policy, provenance, licence and dependency checks, and dotnet build with 0 warnings. These are reviewer-reported; this author did not re-run them.
- **Hosted runs** (all in `ArcForges/Cloud`; job conclusions read with `gh run view --json`, log lines grepped, no secret printed):
  - Main CI run [38007806283](https://github.com/ArcForges/Cloud/actions/runs/38007806283) (push, head `3c59ce34`, created 2026-10-10T00:09:26Z) succeeded: Dependency audit and repository checks, both Source jobs, the CodeQL jobs, Native AOT image and Worker build, Verify and Deploy Cloudflare (production). Deploy Cloudflare proof environment was skipped on the push.
  - Proof observe run [38008603235](https://github.com/ArcForges/Cloud/actions/runs/38008603235) (workflow_dispatch, 2026-10-10T00:20:16Z) succeeded, including Proof Cloudflare access and resources.
  - Proof deploy run [38009326285](https://github.com/ArcForges/Cloud/actions/runs/38009326285) (workflow_dispatch, 2026-10-10T00:30:14Z) succeeded. Its job "Deploy Cloudflare proof environment" logged, in order: `Web web-0.1.0-ci.117.1: profile bundle 2070acd9… and Site 735374a5… verified`; `No migrations to apply!`; `Read 183 files from the assets directory`; `Found 15 new or modified static assets to upload`; `Success! Uploaded 15 files (161 already uploaded)`; `Pushed image: …arcforges-cloud:ci.339.1`; `Current Version ID: 0de3e45a-adbd-4eb0-ac8a-76a7dc223892`; and `Proof environment deployed at https://proof.arcforges.com. This is deployment completion, not live acceptance evidence.` The Worker version named here is the proof Worker version. The container image `ci.339.1` is a new image from this redeploy. The record reports the rollout and does not assess it, as in the first delivery.
  - Closing observe run [38010034909](https://github.com/ArcForges/Cloud/actions/runs/38010034909) (workflow_dispatch, 2026-10-10T00:40:11Z) succeeded, including Proof Cloudflare access and resources.
  - The `RES-cloud-deployment` lease facts (epoch 2, claimant `w-deku-20261009-cloud-85`, released after the run) are coordinator-reported.
- **Live checks by this author**, read-only `GET` on 2026-10-10 against `https://proof.arcforges.com`:
  - `/account/` and `/chat/` return 200 `text/html` with exactly one `Content-Security-Policy` header, with `script-src 'self' 'wasm-unsafe-eval'` and `base-uri 'self'`. Each shell carries `<base href="/" />`.
  - `/` returns 200 with the Site policy: `script-src 'self'` with no WebAssembly token, and `base-uri 'none'`.
  - `/app.css` returns 200 `text/css`. The coordinator's L3 check reported the same results; this author re-read them.
- **Browser boot check on the proof origin.** S36 and the validation clause assign the deployed-origin browser run to PRF.11's local opt-in acceptance. That run is recorded in Web `docs/prf-11-profile-proof.md` at Web `dd0a5de3` (merged 2026-10-10T01:45:42Z) and in `ledger/tasks/prf-11.md`. Its result, one local run in installed Chrome 156.0.8078.12: 4 specs, 2 passed and 2 skipped. The passed specs are the HTTP shell check (exact profile CSP, one `<base href="/">`, framework 200 at the root) and the in-browser check (0 CSP violations on `/account/` and `/chat/`, and the heading in `#app h1` rendered on both). The skipped specs are blocked on CLOUD.21 and CLOUD.22.
- **Gap status after this follow-up** (against the status rule in the first delivery's Scope section):
  1. **PRF.11 cites this task: met.** The clause is closed by the line below.
  2. **D4 live check, header level: met.** The composed headers on the profile and Site routes are observed above.
  3. **Browser-level acceptance of the profiles: met for the local run.** The shells load in Chrome 156, with no CSP violation and the app heading rendered. The same-origin result of the in-browser spec is inferred from the render, because the spec records no request trace. The greeting round trip and interaction timings belong to PRF.11 and are not CLOUD.85 clauses.
- **Closed evidence clause.** "PRF.11's deployed proof-origin same-origin and base-href record cites this task" is met. Web `docs/prf-11-profile-proof.md` at `dd0a5de3`, line 309, reads: "This record cites CLOUD.85. It is the PRF.11 deployed proof-origin same-origin and base-href record that the CLOUD.85 evidence clause requires (the S36 follow-up, Cloud #82, deployed at `3c59ce34`)."
- **Status decision.** `status: complete`. The outcome (serving under base href `/`, Worker-first routes, the exact CSP per surface), the validation (offline tests in Cloud CI; deployed-origin checks recorded by PRF.11's local opt-in run) and the evidence clause are each met, and the CLOUD.85 completion-prerequisite list is empty.

### Untested coverage after this follow-up

- The first delivery's untested coverage still stands, except where the bullets above observe the same thing. In particular, the composed `_headers` and the shell body are now observed on the proof origin, but route precedence is not tested live for every route family.
- The live browser run is one local run by the claimant. The reviewer re-ran it with the same result. It is not a CI result.
- The proof container image `ci.339.1` from this redeploy is reported and not assessed. The CLOUD.85 write list names no container file.
- Carried from the first delivery, outside phase 2: the verifier coverage gaps of S32(c). The Node 24.21 pin is not met locally (local Node 24.20); the hosted Source job is the authority.
