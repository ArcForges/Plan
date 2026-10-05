---
task: CLOUD.08
status: complete
recorded: 2026-10-05
claimant: w-c20261005-cloud08
epoch: 1
---

# Failure isolation and readiness surface (WP-21.07)

Complete against its own acceptance. The task has no completion prerequisite (`complete: []`). The acceptance, quoted from the task record:

- **Outcome:** "Ingress/Container/D1/DO/R2/Queue health are exposed separately, and a missing binding or plan-hash mismatch fails readiness rather than allowing partial execution to appear successful; logs remain no-content."
- **WP-21.07 testing requirement:** "Missing binding/plan mismatch fails readiness, not successful partial execution."
- **Completion evidence asked for:** missing-binding and plan-mismatch readiness-failure results.

How to read this record: **observed** means visible on GitHub (pull requests, review comments, merge commits, workflow runs and job logs). **Claimant-reported** means taken from local runs by the claimant (Windows 11, Node 24.20.0 which is off the pinned 24.21.0, so the local `toolchain` check cannot run and hosted CI covers it; .NET 10.0.401) or from evidence files outside the repository, which a reviewer cannot re-observe. The reviewer `r-c20261005-cloud08-code` is a separate worker identity on the same GitHub account as the claimant, so independence is by worker identity only.

## Evidence

- **Planning pair** (write scope bound to the real layout: the planned `src/ArcForges.Cloud.Host/Readiness/**` does not exist, the host is the existing `src/ArcForges.Cloud` project): ArcForges-Design [#246](https://github.com/ArcForges/ArcForges-Design/pull/246) (merge `3c8b132762d98ac540535a9772c2f97e79240ab7`) and Plan [#323](https://github.com/ArcForges/Plan/pull/323) (merge `b7379091f5441607a2fd018e9e31c554bb944868`), both approved at their heads and merged through the integration roles after mechanical merge-forwards of main (diffs posted on the PRs).
- **Implementation.** Cloud [PR 50](https://github.com/ArcForges/Cloud/pull/50), merged as `0f4cdcebd99420c042db5f5bd88d35f813689bd2` at the reviewed head `d2c98936dee7efea9e8af8ce4e5ae0e65b1ac341` (observed: approval comment 5998251907). The first review of `5f66ad7` was not approved: one low/medium finding (a stream aborted by the 15 second cold-start timer was given `Retry-After: 2` although the call may have reached a slow running Container); fixed by dropping the hint on that path, with a test for the slow-first-byte case. The head was also rebased after CLOUD.06 merged (profile r31, receipt `cloud-08-r1` superseding `cloud-06-r1`).
- **What was built.**
  - Worker module `worker/readiness/`: six components (ingress, Container, D1, Durable Object, R2, Queue) with a closed state and reason vocabulary and an evidence level (`probed` or `bound`). The whole is ready only when every required component is ready or not required (a test enumerates all 6^6 state combinations). A missing or wrongly shaped binding or key, a plan-manifest mismatch (checked by the Worker and by the host) and a recovery-generation mismatch are `misconfigured`. `unknown` never counts as ready.
  - Host `src/ArcForges.Cloud/Readiness/HostReadiness.cs`: D1 readiness runs the named plan once and classifies the failure (plan hash, recovery generation, refused signature, schema version, outage).
  - Operator-signed proof `POST /proof/v1/readiness` returns the report: 200 when ready, otherwise 503 with `Retry-After: 2` only for starting or unavailable. Each component check is bounded at eight seconds; nothing is retried, replayed or written. No production route is added.
  - The ingress and proof session forward answer a Container the platform could not start (the Containers library's own plain-text 503, 500 or 429, pinned by a test against the locked library) with the fixed text and `Retry-After: 2`; every other non-200 and every thrown error stays a 503 without guidance.
  - No-content logs: one closed line per readiness call; tests check the report and the line against secret values.
  - `docs/cloud-readiness.md`.
- **Hosted CI on the reviewed head** (observed, run [37335146719](https://github.com/ArcForges/Cloud/actions/runs/37335146719); the failed jobs were re-run once after CLOUD.04's branch, whose reseal commit `4c5da4b` had put one leak into the shared all-branch history scan, was cleaned): Source ubuntu and windows, dependency audit and secret scan, dependency review, four CodeQL jobs, Native AOT image and Worker build, Verify all succeeded. Main-push run [37338209319](https://github.com/ArcForges/Cloud/actions/runs/37338209319): all jobs including `Deploy Cloudflare` (production) succeeded; production serves the anonymous Hello method only, so this is a deployment result, not a readiness observation.
- **Local evidence** (claimant-reported): `npm test` 604 of 604, `dotnet test --solution Cloud.slnx` 771 of 771 (including the architecture gate on a clean tree), `dotnet format`, biome, prettier, tsc, dependency policy, provenance, licence, `test:artifact` on the real Wrangler bundle. 25 deliberate mutants (19 Worker, 6 host), all killed by a failing test (host mutants checked for compile errors, none).
- **Missing binding and plan mismatch, real runtime** (claimant-reported, opt-in `npm run test:foundation:local`, once, real C# host as a Release apphost, not Native AOT, behind the real Worker modules in workerd with local D1, R2, Durable Object and Queue emulation; evidence file `artifacts/foundation-local/foundation-local-evidence.json` SHA-256 `8620cb94f2208383c1afa3610689e81fcf2678b90079f4a93ec0769aee58a67f`, not in the repository; run on an earlier head that differs from the merged one by one guard in `evaluate.ts` with its own unit test and by the provenance records): 20 of 20 scenarios passed, including `readiness` (all six components ready, Queue `bound`) and `readiness-failures`: with `OBJECTS` dropped for one request the report is `misconfigured` with `r2: binding_missing` naming `OBJECTS` and the other five components ready; with the bridge presenting another plan-manifest hash to the real host the report is `misconfigured` with `d1: plan_hash_mismatch` and the Container still ready; with both faults removed it is ready again.
- **Deployed proof observation** (lease `RES-cloud-deployment` held at epoch 17 for the run and released; claimant-reported unless stated). Dispatch `proof=deploy` on main `0f4cdce`: run [37339503124](https://github.com/ArcForges/Cloud/actions/runs/37339503124) succeeded (observed: Proof Cloudflare access and resources and Deploy Cloudflare proof environment succeeded; production deploy skipped). Then `npm run test:foundation:live` against `https://proof.arcforges.com` once, 2026-10-05T16:27:35Z to 16:33:30Z, from a detached worktree at `0f4cdce` (operator-signed local key, never printed; Node 24.20.0 off the pinned version): **all 22 scenarios passed**, including `deployed-revision` (Worker, Hello and the restarted foundation instance all reported `0f4cdce`, 151 s), `readiness` (every component `ready`: ingress and queue evidence `bound`, container 236 ms, Durable Object 18 ms, R2 180 ms, D1 `ready`, manifest hash equal), and `exact-values` (3.7 s, the first write after the stop and restart that `deployed-revision` performs). Evidence file `~/.arcforges/proof-evidence/cloud-08-live-evidence.json` SHA-256 `82374ebeaca92f30d6c31e0f2955baafc0ce7d61b6132f756d997627c7d75330`, checked for session handles and secrets before hashing (the only matches are scenario labels).
- **Provenance and receipt.** Receipt `cloud-08-r1` (chained after `cloud-06-r1`, no coordinate or closure change), release profile `cloud-release-r31`, records `cloud-08-cloud-worker-bundle-r1` and `cloud-08-cloud-runtime-notices-r1`; Worker bundle 209,480 bytes, SHA-256 `ecbed698efa4f37c638ef7880366890309245563941d16d56e968df6f7dce26c`. CLOUD.04 (#51) also claimed r31 while open: whichever merged second had to reseal; this PR merged first.
- **Substitutes still in use.** None added.

## The two live leads (explained, not reproduced)

Neither is an acceptance item of this task.

1. **Proof `foundation` Container answering 503 on every request while Hello answered 200** (PRF.08 live run, 2026-10-05). Anonymous probes at 14:19 UTC returned HTTP 503 after about 31 seconds from `/session/v1/bootstrap` with the body `There is no Container instance available at this time.` followed by the library's note about the maximum concurrent instance count and provisioning, and `/api/healthz` answered 200 in 1.7 seconds. That text is the Containers library's own answer when the platform could not provide an instance for that Durable Object (neither the Worker's empty refusal nor the host's JSON). Whether it was the instance limit (`max_instances` is 2 in the proof environment, Hello plus foundation, and a stopped instance may still count), provisioning or platform capacity could not be told from outside, and no credential, lease or redeploy was used for the diagnosis. After the proof redeploy above, `/session/v1/bootstrap` answered 200 within 3 seconds and the live run passed; the redeploy therefore cleared the condition, but its cause was not observed and the redeploy is not a diagnosis.
2. **`unknown_outcome` on the first write after a restart** (CLOUD.01 live run 1). Explained: the Worker's eight second deadline or the host's ten second bound running out (both pinned by tests), a stall rather than a failure. The deployed run above passed the same scenario after a stop and restart; the stall has not been reproduced and its platform cause stays an inference from timing.

## Untested coverage and known gaps

- The readiness failures (missing binding, plan mismatch) were observed in the local cross-process run, not on Cloudflare; the deployed run observed only the all-ready report. A deployed fault injection would need a deliberately broken deployment.
- The Queue component proves the binding only (evidence `bound`), not delivery; delivery is observed by the separate `queue-retry-dlq` scenario.
- Production serves no readiness route, so no production readiness was observed.
- The Native AOT host was not run locally; the local cross-process run used a Release apphost (hosted CI builds the AOT image and the deployed run executed it).
- Linux and macOS runtime of the host, and any repeated measurement of the first write after a restart (how often the stall happens), were not observed.
- A bounded Container start inside the Container class that refuses before forwarding with an exact `didNotHappen` effect, and the launch-capacity.v1 `readinessTimeoutMs` value, belong with the launch configuration (CLOUD.10); the library's own start wait (about 8 s to acquire an instance plus up to 20 s for the port) still applies inside the Durable Object.
- A stream aborted at the cold-start bound carries no retry guidance by design.

## Next actions

None owed by this task.
