---
task: CLOUD.71
status: complete
recorded: 2026-10-06
claimant: w-c20261006-cloud71b
epoch: 2
---

# Serve the built Web profiles from the proof origin (WP-06.05, deployed same-origin hosting)

Complete.

- **First delivery** (epoch 1, worker `w-c20261006-cloud71`). It merged and deployed the hosting and observed both profiles served from `https://proof.arcforges.com` next to `/api` and `/session/v1`. PRF.08's live script never completed, because the proof Containers answered 503 and timed out. The record was `delivered`.
- **Completion follow-up** (epoch 2, worker `w-c20261006-cloud71b`, section [Completion follow-up](#completion-follow-up-epoch-2-2026-10-06)). It found two defects and fixed both through reviewed changes:
  - The proof Container application kept a single instance for its two named Containers. The ceiling was raised from 2 to 4, and a new read-only observation shows the provider's view of the application.
  - The proof host renewed a session with the configured thirty-minute idle window instead of the session's own window. A renewal now keeps the session's own window.
- **Result.** One unmodified run of the live script on the served pages then passed all 17 of its scenarios. Its interaction timings are recorded, and Web #32 added the interaction budgets derived from them.
- **Completion prerequisites.** CLOUD.71 has none.

Reasons and the mapping to the acceptance are in [Obligation status and the judgment of `complete`](#obligation-status-and-the-judgment-of-complete).

How to read this record:

- **Job-log-observed** means visible in GitHub runs and job logs.
- **Claimant-reported** means taken from the claimant's own local or live runs (Windows 11, Node 24.21.0), which a reviewer cannot re-observe. The evidence files named below stay outside the repository, identified by their SHA-256.
- **Reviewers.**
  - The code reviewers are `r-c20261006-cloud71-code` and `-code2` to `-code4`, and `r-c20261006-cloud71-web2` and `-web3`.
  - The planning reviewers include `r-c20261006-cloud71-scope2` and `-scope3`.
  - They are separate worker identities on the same GitHub account as the claimants, so independence is by worker identity only.
- **Epoch-1 sections.** The sections marked epoch 1 are the first delivery's record. They are kept as history, and the follow-up supersedes them where it says otherwise.

## Evidence of the first delivery (epoch 1; history, superseded where the follow-up says otherwise)

- **Planning repair** (found while implementing, see "What the first delivery found"): ArcForges-Design [#251](https://github.com/ArcForges/ArcForges-Design/pull/251) (merge `be0ae1e746c43fe4d941909fff0d95b156637357`, approved head `be0f1b810149ba2d17fe01058c1e96668ab93c52`, comment 6006136007) and Plan [#338](https://github.com/ArcForges/Plan/pull/338) (merge `c9a994d1dbe51c4921b69e76e06c74e74bdd3826`, approved head `3b8732c39ee93b252706e43dac6d33bab667a281`, comment 6006136627). They add the per-profile router base, the carriage steps of the bundle in Web's `ci.yml`, the Web tests and `eng/verification/proof-cloudflare.ts` (deploy function only) to the write scope.
- **Web half.** Web [#30](https://github.com/ArcForges/Web/pull/30), merge `d5ebdd19f200afe3a21d7c27a9cca31d1dc45a21` at the approved head `34d41cc00ab8eccc4119b667b38795627ad0b7fd` (comment 6006371963), through the Web integration role. Per-profile router base `/account/` and `/chat/`; `npm run build:profiles` also writes one deterministic ustar bundle; a main-push-only upload and download step and one extra asset on the existing release step; the live script gained `PROOF_PAGES=served`. Main-push run [37393760121](https://github.com/ArcForges/Web/actions/runs/37393760121) on `d5ebdd1` succeeded (job-log-observed) and created release `web-0.1.0-ci.90.1` with asset `web-profiles-67956d7f4b3d2909625585ca68f19f3f8a9ea27a5a08958659b9d9841871f996.tar` (523,776 bytes, the provider-reported asset digest equals the name). The claimant had built the same bundle on Windows before the merge and got the same digest, so the Windows and hosted Linux builds were byte-identical.
- **Cloud half.** Cloud [#61](https://github.com/ArcForges/Cloud/pull/61), merge `b5ff291cfd0a479fe9cb5fc03b8d0a32ffbc125e` at the approved head `b01ff51f3240f1e1648706a9740b65304adccf0a` (comment 6007674722), through the Cloud integration role. `env.proof.assets` with `run_worker_first` for `/api/*`, `/session/v1/*` and `/proof/v1/*`; the pinned bundle (`web-0.1.0-ci.90.1`, the digest above); strict verification and staging in `eng/verification/proof-deploy.ts` and `proof-cloudflare.ts`; 18 offline tests in `tests/worker/proof-assets.test.ts`; receipt `cloud-71-r1`. Review history: head `04751c1` not approved (comment 6007298911: the documentation promised a not-observed list that did not exist), `aff7d17` not approved (comment 6007486676: the reference check missed slash-separated attributes), `b01ff51` approved. CodeQL `js/bad-tag-filter` flagged the first script-tag pattern twice and was fixed in two commits; one intermediate push had a broken test string and failed Source on Ubuntu, corrected in the next commit. Hosted CI on the approved head: Source on both operating systems, audit, dependency review, four CodeQL jobs, Native AOT image and Worker build and Verify.
- **Main-push run** [37401254836](https://github.com/ArcForges/Cloud/actions/runs/37401254836) on `b5ff291` (job-log-observed): all jobs succeeded including `Deploy Cloudflare` (production). The production Worker's configuration still carries the proof `assets` block only inside `env.proof`; production deployed without change.
- **Proof deployment** (job-log-observed; lease `RES-cloud-deployment` epoch 19 held by the claimant for the live phase and released with a note): manual dispatch `proof=deploy` on main, run [37402155825](https://github.com/ArcForges/Cloud/actions/runs/37402155825) on `b5ff291`: all jobs succeeded. In its log: the gated migration step passed; "Profile bundle web-0.1.0-ci.90.1 67956d7f…: 14 files verified and staged as the proof assets"; wrangler read 17 files from the assets directory and uploaded 13 new assets (273.10 KiB, 46.41 KiB gzip); the Worker deployed on custom domain `proof.arcforges.com`; the provider receipts passed (workers.dev and preview URLs disabled for the proof Worker, `proof.arcforges.com` serves `arcforges-cloud-proof`, the production route `arcforges.com/api/*` still serves `arcforges-cloud`, no proof Worker route on the zone). No secret was read or printed by the claimant.
- **Served pages observed live** (claimant-reported, one Playwright Chromium session and plain HTTP probes against `https://proof.arcforges.com` right after the deployment, under the lease): `/account/` and `/chat/` answered HTTP 200 with the per-profile `Content-Security-Policy` header from the bundle's `_headers` (starting `default-src 'self'; script-src 'self' 'sha256-…`), `x-content-type-options: nosniff`, `x-frame-options: DENY` and `cache-control: public, no-cache, no-transform`; each page's bytes equalled the page of the local build of the same source (digest-checked); no console error and no CSP violation in either page; the Account page, loaded from the deployed origin, rendered its anonymous presentation ("You are not signed in.") from a real same-origin `GET /session/v1/bootstrap` on the same origin (one page load, 45 s allowance; the first bootstrap after idle took about 25 s). The script's own route assertions (the origin root is not a page, an unsigned `/proof/v1/readiness` is refused by the Worker with a non-HTML 4xx, an unknown profile path is not a page) passed in each run before it aborted; its observation row was not written because the run aborted later.
- **What did not work live** (claimant-reported). The Chat page loaded, but its one greeting did not render: "The server did not answer in time." (the profile's ten second deadline). Plain probes then showed the Hello route answering 200 in 1 to 11 s with occasional 503 after 2 to 6 s, and the session route answering 503 after about 28 s for the first request after an idle period and 200 afterwards (with stretches of consecutive 503s of about 28 s each). That is the Containers library's start-wait behaviour (a start that outlasts about 28 s), the same flapping the PRF.08 and CLOUD.08 records describe; the cause was not confirmed here. `node apps/app/scripts/proof-run.ts` (`PROOF_PAGES=served`) therefore did not complete: runs 1 to 4 (unmodified, after the deployment; run 3 after a pre-warm of both routes with plain probes) each aborted at the first anonymous bootstrap that follows the script's warm-up (HTTP 503, kind `unavailable`); run 5 used an uncommitted local harness change (a clean-pass warm-up and a ten second keep-alive of both routes) and aborted in the warm-up of the Hello route (the profile's ten second deadline against the observed 1 to 11 s). The local change was discarded; nothing of it is merged. No evidence file was written, no interaction timing exists and `apps/app/interaction-budgets.json` does not exist.
- **Disclosures.** The live script was run five times, not once, and each abort was diagnosed from plain status probes before the next run; every run and probe was made while holding the lease and sent no session handle or secret anywhere (the operator key is read only by the script and was never printed). Plain anonymous probes (a bootstrap GET and a hand-framed Hello POST) were sent from the workstation to diagnose, and the two routes were pre-warmed that way once. The lease was released with a note after the last run.
- **Obligations.** WP-06.05, the deployed same-origin hosting part: the hosting is satisfied and observed (pages served from the proof origin with their policy, Worker-first routes, no workers.dev). Its exercise with the live script (real session, cookie and CSRF round trip from the built profiles in a browser, Chat round trip, session expiry and cancellation on the real path) is **not** satisfied.
- **Substitutes still in use.** The PRF.08 forwarder mode (`PROOF_PAGES=forwarded`) remains as an explicit fallback of the script; the served mode is the default and was never run to completion.

## What the first delivery found (epoch 1)

- The unchanged PRF.08 pages have router base `/` and rendered "Page not found" when copied under `/account/` (observed once in local Chromium). Each profile is now built with its own router base; the JavaScript and stylesheet chunks are byte-identical to the root builds and only the prerendered page moved. This is why the Web half touched `apps/app/react-router.config.ts`, which the original scope did not name (repaired through Design #251 and Plan #338).
- The Web sealed candidate verifies an exact file set, so the bundle cannot ride in it; it is carried as its own artifact and release asset.

## Accepted gaps of the bundle verifier

Recorded from the reviewer's non-blocking notes on `b01ff51` (the code stays as approved): comments are not modelled by the start-tag tokenizer (a tag inside an HTML comment is tokenized and checked, which is stricter, never looser); `xlink:href`, `srcdoc` and `imagesrcset` attributes are not checked; an `&amp;` in a query string of a `src` or `href` value fails closed (the real bundle has none). Also accepted and documented in `docs/prf-07-foundation-proof.md`: CSS `url()` values other than `@import`, URLs a script builds at run time and inline event-handler attributes, all of which the policy itself blocks.

## Untested coverage at the first delivery (epoch 1; history, superseded where the follow-up says otherwise)

- The live script's browser stages (authenticated Account presentation from a real session, sign out in the browser, session expiry in the browser, Chat in the browser, cancellation on the real path) and every interaction timing; the Chat greeting never rendered.
- Cloudflare behaviour of `_headers` beyond the three header names and the policy prefix observed above; `Cache-Control` on `/assets/*` was not read.
- Linux, macOS, Firefox and WebKit runs of the served pages; accessibility and visual review.
- Whether a same-origin GET without an `Origin` header passes the session edge was observed only for the anonymous bootstrap (it did).

## Completion follow-up (epoch 2, 2026-10-06)

Worker `w-c20261006-cloud71b`, claim epoch 2 (claimed 03:43:19Z). The directive: diagnose and fix the cause of the failed live verification, not by longer timeouts, pre-warming, keep-alive requests or weaker assertions; then run the targeted verification once and record it. All times below are UTC on 2026-10-06.

### Diagnosis (claimant-reported)

**Probe run.** One probe run under `RES-cloud-deployment` epoch 20, from 03:48:55Z to 04:08:10Z, with evidence `cloud-71-diagnosis-probes-2026-10-06T034855Z.json`. It showed that the two named instances of the proof Container application never ran at the same time. `hello` serves `/api`; `foundation` serves `/session/v1` and the operator surface.

**Refusals.** While one instance held a container, every start of the other was refused for as long as the holder stayed active.

- In one case the holder was in continuous use for about six minutes (03:50:15Z to 03:56:20Z). The 9.5 minutes from the first foundation refusal to the next foundation answer include the probe's own 130 s idle gap.
- The refused instance started within 2 to 14 s after the holder's 60 s idle stop.
- **Foundation refusals:** 16, each an empty 503 with `Retry-After: 2`, after 29.6 to 34.8 s. That is the start wait of the Containers library.
- **Refused Hello calls** ended within the Worker's own deadline:
  - 9 × 504 `RPC deadline exceeded.` on `/api/healthz` after 15.29 to 15.92 s (the route's 15 s bound);
  - 5 × gRPC status 4 on `SayHello` after 10.86 to 11.21 s (the 10 s bound);
  - earlier, 7 × the classified 503 `Cloud container is temporarily unavailable.` with `Retry-After: 2`, after 0.70 to 14.30 s.
- **Cold starts.** The recurring "cold" Hello start of about 76 s (75,997 and 75,988 ms) is the 60 s idle stop plus one `/api/healthz` attempt. A start with a free instance took 2.15 to 14.42 s (first successes of 2,152, 2,478, 4,318, 10,125 and 14,419 ms in the probe file).

**CPU is not the cause.** A local win-x64 Native AOT build of `b01ff51`, run through the build slot (evidence `cloud-71-diagnosis-local-cpu.json`), showed:
- start to first `/healthz` took 31 to 63 ms of CPU;
- requests were below timer resolution;
- there was no slowdown under a 1/16-core job cap.

So the `lite` instance type (1/16 vCPU, 256 MiB) is not the cause.

**The origin root.** `GET /` on the proof origin answers 404 `Unknown API method.` (evidence `cloud-71-diagnosis-root-check.json`). This is the Worker's deny-by-default answer: intended, and unchanged.

### Planning repairs

Two repairs, each a Design and Plan pair approved before the work it allowed (DLV-34; no obligation or acceptance removed).

**Capacity and observation.**
- **ArcForges-Design [#252](https://github.com/ArcForges/ArcForges-Design/pull/252):** merge `3c8d5b148e92188ec8cd7b1c47a27456d3dcd54f` at the approved head `e7bc422da1e18e4fc2ab163d7055efa79f8d27d5` (comment 6009434602). The first head, `9d7cf7f`, was not approved (comment 6009380985): placement constraints were unusable without an out-of-scope key-set test, so placement left the scope.
- **Plan [#341](https://github.com/ArcForges/Plan/pull/341):** merge `e7eebbfe36a0877bb9f6a9ec2c254cb95e66caa8` at the approved head `cb1a965c4374e7f021836ee130901ab5e39bce50` (comment 6009435045). The first head, `b58d557`, was not approved (comment 6009381431).
- **Scope gained:**
  - the `env.proof` container ceiling (`max_instances`);
  - the read-only `proof=observe` choice of the manual dispatch, with its function, tests and script;
  - the pin of the proof ceiling;
  - the matching documentation.
- **Reviewer:** `r-c20261006-cloud71-scope2`.

**Session renewal.**
- **ArcForges-Design [#253](https://github.com/ArcForges/ArcForges-Design/pull/253):** merge `4b4858fcc49df97f8b5d50ee5451c2042b20c483` at the approved head `515b6f4581ccc5bcf4c9fecf9480acea2a3fccca` (comment 6010810146).
- **Plan [#342](https://github.com/ArcForges/Plan/pull/342):** merge `d5a3952e17b642186226b352e5c6b5987759e082` at the approved head `91cad197a61a3a9675a7d326c206f4252908cabc` (comment 6010810747).
- **Scope gained:** the renewal path (`TouchAsync`) of `src/ArcForges.Cloud/Foundation/SessionService.cs`, its tests and its documentation.
- **Why this fix:** the coordinator chose it over changing the live assertion, which would have weakened it.
- **Reviewer:** `r-c20261006-cloud71-scope3`.

### Pull requests and merges (job-log-observed)

Every merge below went through the repository's integration role, with `--match-head-commit` at the approved head. "Promotion" in the last column means the production Worker received only the new image: `instance_type` lite and `max_instances` 1 were unchanged, workers.dev and preview URLs stayed off, and the route `arcforges.com/api/*` stayed the same.

| Pull request | Approved head (review comment) | Merge | Hosted CI | Main-push run |
| --- | --- | --- | --- | --- |
| Cloud [#62](https://github.com/ArcForges/Cloud/pull/62): read-only `proof=observe`, `env.proof` `max_instances` 2 → 4, ceiling pin, docs, receipt `cloud-71-r2` | `cc749decb8b60f4673a570ae8a7aa24cd3592dcd` (6009936287, `r-c20261006-cloud71-code2`) | `99617b84c331cc76ff76ad47c102125fc99c564a` | 37415939215 | 37418446762: promotion of `ci.227.1`; production Worker `020835ce-1d16-4933-9419-4c50491e8ce0` |
| Cloud [#63](https://github.com/ArcForges/Cloud/pull/63): the renewal keeps the session's own idle window; release profile `cloud-release-r36`, records `cloud-71-cloud-runtime-notices-r1` and `cloud-71-cloud-worker-bundle-r1`, NOTICE, receipt `cloud-71-r3` | `a8dfe63fc2aa138138492c58d3ae1897a9bac5bd` (6011766216, `r-c20261006-cloud71-code3`). Head `eeba417` was not approved (6011556953): no test caught a renewal that read the clock twice. | `c59f91c5c3d366ac6f98de1afdce050aaec4c1f9` | 37426676599 (`eeba417`), 37430523674 | 37431846044: promotion of `ci.239.1`; production Worker `a55da8f2-ecd9-4aae-a8d8-c593486bedf1` |
| Cloud [#64](https://github.com/ArcForges/Cloud/pull/64): observe test gaps from the #62 review, 503 diagnosis wording, post-run record | `a8550dfa9ef8843f453e29b9de88ee11522ab799` (6013133823, `r-c20261006-cloud71-code4`). Head `37e70da` was not approved (6012811825): the fifteen second bound holds for `/api/healthz` only. | `3d304ef3fcf1a8cb7800939405f86e85a5ef9467` | 37436335442 (`37e70da`), 37439677211 | 37441726724: promotion of `ci.244.1`; production Worker `c7a0cfc1-fb80-48c2-8b32-9bd53af59ca6` |
| Web [#32](https://github.com/ArcForges/Web/pull/32): `apps/app/interaction-budgets.json`, the served-profile run record in `docs/prf-08-profile-proof.md`, one inventory row (ADP-07) | `9c8d5c4bc1beadb9d9a130f497cca3845158476b` (6013457092, `r-c20261006-cloud71-web3`). Content approved first at `4cab0ce` (6012789467, `r-c20261006-cloud71-web2`), then rebased with no change. | `016d1239288a0eeb8b81f0cae973088def742635` | 37435449219 (`4cab0ce`): failed only at `npm audit` (GHSA-68fv-2mgg-jv7q in `source-map-js` 1.2.1, lock not changed by #32); 37443052005 | 37444111952: Web site deploy and prerelease `web-0.1.0-ci.100.1` |

The `source-map-js` admission that unblocked Web #32 is Web #33 (worker `w-c20261006-webdep`, merge `ab5da29`). It is not part of this task.

**New idle-renewal tests** (Cloud #63; existing tests unchanged):
- `SessionServiceTests`:
  - `ARenewalKeepsTheSessionsOwnShortIdleWindow`
  - `ADefaultSessionRenewsWithTheConfiguredThirtyMinutesExactlyAsBefore`
  - `TheAbsoluteExpiryStillCapsARenewalOfAShortWindow`
  - `AStoredWindowLongerThanTheConfiguredOneCannotLengthenARenewal`
  - `AZeroOrNegativeStoredWindowFailsClosedAndIsNeverRenewed`
  - `InterleavedRenewalsOfOneSessionKeepAConsistentPairOfLastSeenAndIdleExpiry`
  - `ARenewalReadsTheClockOnceForLastSeenTheGuardAndTheNewExpiry`
- `FoundationHostTests`:
  - `ARenewingBootstrapKeepsTheSessionsShortIdleWindowSoIdlenessIsStillRefusedOnBootstrapAndLogout`

**Mutation checks** (claimant-reported, through the build slot):
- **Cloud #63:**
  - the old renewal rule fails three of the new tests;
  - removing the clamp or the guard fails two;
  - each of the three two-clock-read mutations (new expiry, last seen, guard) fails the stepping-clock test.
- **Cloud #64:** each of these mutants fails the observe test:
  - exempting observe from the main-branch check;
  - a deploy condition widened to observe or to access;
  - `!= 'none'`;
  - `contains(fromJSON(...))` or a negated condition, each with a misleading step comment.

### Deployments, observations and live runs

**Ground rules.**
- Every live step held `RES-cloud-deployment`, and each lease was released with a note.
- CI ran only the dispatches named here. A `proof=observe` dispatch only reads the provider's records of the proof Container application.
- No step touched production.
- From 05:35:59Z on, no request was sent to the proof origin outside the steps in this table. The earlier diagnosis run of lease epoch 20 is described under Diagnosis, and its requests are listed under Disclosures.

**How to read the table.**
- **Evidence:** the claimant-reported rows name their evidence file, and the job-log-observed rows name their run.
- **Receipts:** the four receipts are:
  - workers.dev and preview URLs disabled for the proof Worker;
  - `proof.arcforges.com` serves `arcforges-cloud-proof`;
  - `arcforges.com/api/*` still serves `arcforges-cloud`;
  - no proof route on the zone.

| When (UTC) | Step | Result |
| --- | --- | --- |
| 05:35:59–05:36:39 (lease epoch 21) | Requests before the change: one anonymous `/api/healthz`, then one anonymous bootstrap | Hello 200 in 2.7 s. The bootstrap was refused (503, `Retry-After: 2`) after 34.0 s while Hello held the only instance. |
| 05:36:30 | observe [37419346539](https://github.com/ArcForges/Cloud/actions/runs/37419346539), before the change | `max_instances` 2 but `instances` 1. The one instance (`d038d2e3`, version 10, cmh02) served `hello`; `foundation` was assigned without an instance. Rollouts v6 to v10 each had one instance. The status endpoint answered 404, and the Workers Logs query was not permitted (HTTP 403). |
| after the observation | `proof=deploy` [37419568073](https://github.com/ArcForges/Cloud/actions/runs/37419568073) of `99617b8` | All jobs succeeded. The migration gate passed with nothing to apply. Bundle `web-0.1.0-ci.90.1` `67956d7f…` was verified and staged (14 files). `max_instances` went from 2 to 4. Proof Worker `66cd245b-9bd1-4380-9743-cf14657896de`. All four receipts PASS. |
| 05:49:35 | observe [37420442070](https://github.com/ArcForges/Cloud/actions/runs/37420442070), after the change | Version 11, `max_instances` 4, `instances` 4, health healthy 4. The rollout created at 05:47:59Z had completed. |
| 05:50:28–05:52:06 | Concurrency window 1 | Both cold starts happened in the same second (bootstrap 2.57 s, healthz 2.63 s). Then 15 rounds of `/api/healthz`, `SayHello` and bootstrap over 95.4 s. 47 of 47 answers were 200, warm-up included. |
| 05:56:57 | observe [37420557204](https://github.com/ArcForges/Cloud/actions/runs/37420557204) | Dispatched at the start of window 1, but it queued behind the previous run in the main concurrency group and ran after the window. Four healthy instances; both Durable Objects released at 05:53:11Z. |
| 06:03:34–06:04:40 | Concurrency window 2, with observe [37421694302](https://github.com/ArcForges/Cloud/actions/runs/37421694302) inside it (06:03:58) | 32 of 32 answers were 200. At the same moment the observation lists `hello` on `d03b5135` (yyz04) and `foundation` on `d0392d5f` (ewr05), both version 11. |
| 06:12:59–06:13:48 (lease epoch 22) | Live run 1 of the follow-up, on the deployment of 37419568073, started after an 8 min 24 s idle gap | **Failed** at the Account idle-expiry stage: the deployed logout answered 200, not 401. The proof host had renewed the session with the configured thirty-minute window. The script had reached that assertion, so every earlier stage passed. The Chat stage did not run, and no results file was written, because the script writes it only at the end. Evidence: `cloud-71-live-run-2026-10-06T061259Z.txt`. |
| 07:58:46 to 08:06:06 (lease epoch 23) | `proof=deploy` [37433072095](https://github.com/ArcForges/Cloud/actions/runs/37433072095) of `c59f91c` (deploy job 112170518191, 08:05:20–08:06:06) | All jobs succeeded. The migration gate passed with nothing to apply; the access probes passed. Image `ci.240.1` `sha256:e64bb000…`. The same bundle `67956d7f…` was verified and staged (14 files). Only the image changed in the application; the ceiling stayed 4. Proof Worker `6951f4d7-4209-438f-813c-950e4e336143`. All four receipts PASS. Evidence excerpt: `cloud-71-deploy-37433072095.txt`. |
| 08:10:19 | observe [37434302367](https://github.com/ArcForges/Cloud/actions/runs/37434302367) | Version 12 with image `e64bb000`, `max_instances` 4, `instances` 4, healthy 4. Rollout `0c6679b6` (08:06:01Z, target version 12) had completed. No instances were listed: neither `hello` nor `foundation` held an instance. Their last assignment changes were at 06:14:23Z and 06:14:58Z. |
| 08:11:03–08:12:15 | Live run 2, on the deployment of 37433072095 | **Passed every scenario** (next section). Exit 3 (`PARTIAL`) only because `apps/app/interaction-budgets.json` did not exist yet. |

### The passing live run (claimant-reported)

**Script and start state.**
- The script: Web `apps/app/scripts/proof-run.ts` exactly as merged at Web `d5ebdd1`, with the served pages (the default `PROOF_PAGES`), on pinned Node 24.21.0, from a Windows 11 workstation over the public internet.
- It started cold, about two hours after the last request to the proof origin, which was the 06:13Z run, and five minutes after the rollout.
- Nothing else reached the proof origin before or during it: no pre-warm, keep-alive or other request.
- Evidence: the console output `cloud-71-live-run-2026-10-06T081103Z.txt` and the results file `cloud-71-proof-run-2026-10-06T081103Z.json`. Neither holds a secret, cookie or session handle.

**The 17 observations, all on the deployed origin:**
- **Origin routes:** the root 404, an unsigned `/proof/v1` request 401 from the Worker (no content type), an unknown profile path 404.
- **Warm-up from cold, not budgeted:** the session route (foundation Container) gave its first success after 3,371 ms, and the chat route (Hello Container) after 1,522 ms.
- **The profiles' own clients from Node:**
  - an anonymous bootstrap;
  - an issued session's real C# bootstrap body, parsed by the generated codec: one workspace, exact uint64 recovery generation `0`, and a CSRF token equal to the issued one;
  - a wrong CSRF token and a wrong Origin forbidden, and a missing cookie unauthenticated, with the session still alive afterwards;
  - logout receipt `happened`, a second logout unauthenticated, and the bootstrap anonymous afterwards;
  - cancellation of an in-flight bootstrap;
  - a Hello greeting, a Unicode name, an empty name `rejected`, and 257 code units `limit`.
- **Account page in Chromium:**
  - `/account/` returned HTTP 200 with the profile policy (`connect-src 'self'`, no unsafe inline), nosniff and frame denial;
  - the page and its 7 initial resources equal the local build's bytes;
  - the anonymous presentation, and the authenticated presentation from an issued session (exact uint64 `0`);
  - five sign-outs, each with logout 200, the cookie cleared by the server, and the bootstrap anonymous afterwards;
  - idle expiry: a session issued with an eight second idle window, the page loaded, eleven seconds idle, then sign out. The deployed logout answered 401, and the page showed the ended session with no alert.
- **Chat page in Chromium:**
  - `/chat/` returned HTTP 200 with its policy and the build's bytes (7 initial resources);
  - five greetings, a Unicode name, `rejected` and `limit`, with every gRPC-Web call answered HTTP 200;
  - cancellation of a request the deployed host was still answering: shown as cancelled, and the answer that arrived later was not shown;
  - no console error or CSP violation.

**Interaction timings.** Five warm samples each, measured from the user action to the rendered result:

| Interaction | Min / median / max (ms) | Budget ceilings, median / max (ms), Web #32 |
| --- | --- | --- |
| `account.read` | 1,015 / 1,034 / 1,043 | 1,138 / 1,148 |
| `account.signout` | 836 / 846 / 857 | 931 / 943 |
| `chat.greeting` | 858 / 863 / 1,367 | 950 / 1,504 |

**How the ceilings were set.**
- Each ceiling is the measured value plus 10 percent (the TH-01 regression line), rounded up to the next millisecond, with `minimumSamples` 5.
- Design defines no interaction ceiling, so these are regression guards, not product budgets.
- No run has been checked against them yet. The script ran before the file existed, and that is why it reported `PARTIAL`.

### Cause model the observations support

**Model (b): a single prepared instance.**
- With `max_instances` 2 the provider counted and kept one instance for the application (`instances` 1), and the two names took turns on it.
- It was not (a), a stopped instance still counted. The count was 1 of 2, and no other instance, stopped or of an older rollout, held the second slot. The provider's derived state reads `stopped` even for instances in use (both in-use instances in 37421694302), so that state alone does not mean stale.
- It was not (c), instances left by an earlier rollout: rollouts v6 to v10 each had one instance.
- With `max_instances` 4 the application keeps four prepared instances and served both names at once. The evidence is observe 37421694302, both concurrency windows, and the passing run's cold warm-ups of 3.4 s and 1.5 s.

**The second defect** was independent of capacity. The renewing bootstrap gave a short-window proof session the configured thirty minutes. The PRF.07 record states this as a limit; it is now annotated there.

### Evidence files (claimant-reported, `~/.arcforges/proof-evidence/`)

| SHA-256 | File |
| --- | --- |
| `b46e9a9c151aa7592a951b313055fc8444d2899f5204ec37dfb8cd1110ce1c8d` | `cloud-71-diagnosis-probes-2026-10-06T034855Z.json` |
| `13408b88b530b8425d8f7db998aac12d175ac380415ff852359780ba0dcb2ed8` | `cloud-71-diagnosis-local-cpu.json` |
| `60d9b707b21dd924b5bad5529db848b2c2b5f1d21b659a2e9aa8c76d46a0d588` | `cloud-71-diagnosis-root-check.json` |
| `0393a70935a407d6f6441dc8ae6c2cff8af10d5964924b1bafed49cdab1d9d82` | `cloud-71-before-2026-10-06T053559Z.json` |
| `0756748eedd3c7cecbe9f618e8c3da1baa75ef8fe7981db0a223687170dba5a3` | `cloud-71-observe-before-37419346539.txt` |
| `3c57941cf08272ee75cd947e364679bea74d1ec16756b7b3e7dff5a852e27fdf` | `cloud-71-observe-after-deploy-37420442070.txt` |
| `d654d6e71ab90f76298b812432861c05c4f045c06755ba8813ec04ef52d5b06b` | `cloud-71-concurrency-2026-10-06T055028Z.json` |
| `8cc0890f265ada000be162fe1a10da89967be1a0ed9d404cdbb52d0f42d04efc` | `cloud-71-observe-after-concurrency-37420557204.txt` |
| `4455b1e083c02c637c161b4f69b9b7448e01bf2dc9edef7c681def59e3b0316e` | `cloud-71-concurrency-2026-10-06T060334Z.json` |
| `2e50e1ee4917a942f8f4703c7d152ee20d74121089ef34458005edde690e5bb4` | `cloud-71-observe-during-concurrency-37421694302.txt` |
| `f3a4d055594b150536daf28e996243f0f9ddacd4408628b1231235ccc2a36af9` | `cloud-71-live-run-2026-10-06T061259Z.txt` |
| `83a4579b42e949e1b328b31def9e6434e803ef4dbfa63224663d0bf69b505a5c` | `cloud-71-deploy-37433072095.txt` (job log excerpt; the registry account path is replaced by `<account>`) |
| `a387d37e9548c4eb1916587dd34bea5768b6dbb33f9ebc0f72ffe8554a211653` | `cloud-71-observe-after-redeploy-37434302367.txt` |
| `7995ec7905d2da72b2e99a99ed90d29e215ef600ff085cb9ce6058fd707b65bf` | `cloud-71-live-run-2026-10-06T081103Z.txt` |
| `bfc47c13e476ea1cff2a4d7684237e8aafb324e59cb5c7fe43371e65436fab17` | `cloud-71-proof-run-2026-10-06T081103Z.json` |

### Obligation status and the judgment of `complete`

CLOUD.71 has no completion prerequisite, so `complete` rests only on its own outcome and validation. Each part of the outcome:

**The two profiles are served byte for byte** by the proof Worker on `/account/` and `/chat/` of `proof.arcforges.com`, next to `/api`, `/session/v1` and `/proof/v1`, which the Worker answers first.
- In the passing run, each page and its 7 initial resources equalled the local build.
- The root and an unknown profile path answered 404, and an unsigned `/proof/v1` request got the Worker's 401.
- `/api` and `/session/v1` answered the profiles' own clients and pages.
- workers.dev and preview URLs stay disabled: the receipts of all three proof deployments say so.

**The bytes come from the immutable digest-named bundle** that the Web main-push build published (release `web-0.1.0-ci.90.1`, digest `67956d7f…`). The manual `proof=deploy` job downloaded, verified and staged it in 37402155825, 37419568073 and 37433072095 ("14 files verified and staged"). Nothing was rebuilt.

**The responses carry the profile Content-Security-Policy:** the served policy of each page equals the one derived from the build.

**Per-profile router base:** Web #30, in the epoch-1 evidence.

**Production configuration and the Web apex Custom Domain are untouched.**
- Every production deployment was the standard main-push promotion of a new image, with `max_instances` 1 unchanged.
- The receipts show `arcforges.com/api/*` still serving `arcforges-cloud`.
- No change touched Web's apex domain.

**Headroom for both named instances to run at the same time,** with a read-only observation of the ceiling and instances before and after the deployment:
- the ceiling is 4;
- the observations before and after are 37419346539 and 37420442070, plus 37434302367 after the redeploy;
- both names ran at once (37421694302), and both concurrency windows passed.

**Exercised once with PRF.08's live script on the served profiles, under the lease, with the result recorded:** live run 2 above.
- All 17 scenarios passed, and its observations and timings are recorded here and in Web `docs/prf-08-profile-proof.md`.
- The interaction budgets it produced were added by Web #32.
- Its `PARTIAL` exit only reports that the budgets file did not exist yet.

**Validation** (P2-017):
- offline tests of route precedence, digest verification and headers (Cloud #61) and of the read-only observation (Cloud #62 and #64);
- one observation before and one after the deployment, the concurrency check and the live run, all under the lease and recorded here;
- no pull-request job received a secret or ran a live service.

**WP-06.05, the deployed same-origin hosting part,** is satisfied: in a real browser the page, `/api` and `/session/v1` shared one origin, cookie and CSRF boundary on a deployed Cloudflare.

**Attempts.** The task asks for one run recorded once. This record lists every attempt:
- five aborted runs in epoch 1;
- in this follow-up, one failed run and one passing run.

Each earlier failure has its cause recorded and fixed; the passing run is the recorded result.

### Disclosures

- **User-ordered stop.** At the user's order the coordinator cancelled run 37421694302, which was complete by 06:06:37Z. Its observe job had already succeeded at 06:04:00Z; Verify of that run failed only because the cancelled jobs did not run. Lease epoch 21 was released at 06:11Z. Nothing was dispatched or sent until the user authorised the follow-up to continue.
- **Requests from the workstation outside the live runs.** All were sent under the lease.
  - The diagnosis run (epoch 20) sent anonymous `/api/healthz`, `SayHello` and bootstrap requests. It also sent:
    - three operator-signed `POST /proof/v1/readiness` requests, at 03:48:55Z (200), 03:56:11Z (503) and 04:08:02Z (503), signed with the operator key loaded through Cloud's own `eng/verification/proof-operator.ts`;
    - one anonymous `GET /`, at 04:03:28Z (the root check).
  - The requests before the change and both concurrency windows sent anonymous `/api/healthz`, `SayHello` and bootstrap requests.
  - Neither live run of this follow-up was preceded or accompanied by a pre-warm, keep-alive or any other request.
- **Secrets.** No secret, token, cookie, session handle or account-private value was printed or written. The operator key was read only by the repository's own scripts.

### Follow-ups and notes (not part of this task's acceptance)

- **TH-02 (interaction budgets).**
  - The ceilings come from one run of five samples, from one workstation, with the Container locations of that run not observed. Earlier observations placed the instances in cmh02, yyz04 and ewr05.
  - The max ceilings are the most sensitive to noise. The results file keeps only the minimum, median and maximum of each interaction, and for `chat.greeting` these are 858, 863 and 1,367 ms, so its maximum lies far above its median.
  - A single over-ceiling result must be sampled again before it counts as a regression (Design TH-02: a regression gate needs repeated sampling, never a single-machine fluctuation).
- **For the Architecture Owner (CLOUD.10, PG-26; no production change).**
  - The launch profile's Container allocation (Design `docs/architecture/data-model/04-d1-execution-profile.md`) uses four fixed named slots per realm with `max_instances=4` as the global deployment ceiling. That leaves no headroom between the names and the ceiling, and the profile says only real L-16 measurements can prove sufficiency.
  - On the proof application, a ceiling of 2 for two named instances behaved as one usable instance: the provider counted and kept one instance, and the other name was refused for as long as the holder stayed active. A ceiling of 4 for two names gave four instances, serving both at once.
  - The launch profile therefore cannot assume that the provider prepares as many instances as the ceiling allows.
  - CLOUD.10's launch-capacity acceptance and L-16 should measure the four named slots at `max_instances=4` before relying on a ceiling equal to the slot count. The measurement should include a slot that restarts while the others are active.
  - Production keeps `max_instances` 1 for its single Hello instance.
- **Observation paging** (Cloud #62 review, note 3). The observation reads instances as one page of 100 and does not check `result_info.next_page_token`. Wrangler's default page is 25, and no maximum is documented. This does not matter at a ceiling of 4, and a refused page size fails closed.
- **Logs permission wording** (Cloud #62 review, note 4). The documented permission of the telemetry query is Workers Observability Write. "May query Workers Logs" therefore means the token holds that write-class permission; a dry query still persists nothing. The token was refused (HTTP 403).
- **Cloud docs figure.** The merged Cloud `docs/prf-07-foundation-proof.md` says a start with a free instance took 1.6 to 14 seconds. The probe file gives 2.15 to 14.42 s (see Diagnosis), so a later touch of that document can correct the figure.
- **Web gitleaks allowlist** (owner: the Web dependency maintainer). `.gitleaks.toml` allowlists the browser-resource profiles by `browser-resources-r[123456789]\.json`. That pattern does not match a tenth revision (`r10`), so the next profile revision needs it widened.
- **Production image observation** (outside CLOUD.71; not investigated; production untouched).
  - The production deployments of main-push runs 37431846044 (about 07:55Z) and 37441726724 both list the current image of `arcforges-cloud-cloudcontainer` as `sha256:4bb6e3e3…`.
  - `4bb6e3e3…` is the `ci.227.1` image that 37418446762 promoted.
  - The first of those deployments had changed the image to `dfbc22cd…`, so the application does not appear to have stayed on the new digest.
  - The production application's rollout state was not read. The question belongs to the production release tasks.

### Untested coverage (epoch 2)

- **Platforms:** Linux, macOS, Firefox and WebKit runs of the served pages; accessibility and visual review.
- **`Cache-Control` on `/assets/*`:** not read.
- **The interaction budgets:** no run has been checked against them yet.
- **The passing run's environment:** its network path and Container locations were not observed after the run.
- **Load:** nothing beyond one browser and the two short concurrency windows, and no long-run behaviour of the four-instance pool.
- **The provider's instance count:** why the provider kept one instance at a ceiling of 2 is inferred from the observations, not from provider documentation.

## Remaining acceptance and next action (first delivery; history, superseded by the follow-up)

Repeat `node apps/app/scripts/proof-run.ts` once under `RES-cloud-deployment` when the proof Containers start reliably (the CLOUD.08 readiness surface names the Container component before a run), record the observations and interaction timings, add `apps/app/interaction-budgets.json` through a reviewed Web change, and amend this record to `complete` through a reviewed change. A harness hardening is a lead, not a decision: the warm-up could require a clean pass of both routes and keep both Containers from idling during the run (an uncommitted attempt aborted on the Hello deadline, so its value is unproven). The same completion follow-up covers the PRF.08 live round trips.
