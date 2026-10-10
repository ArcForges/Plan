---
task: PRF.11
status: delivered
recorded: 2026-10-10
claimant: w-deku-20261009-prf-11
epoch: 1
---

# Blazor WebAssembly production build and generated C# SDK proof against deployed ingress

## Evidence

- Implementation, in one Web pull request (brief S20(d), S25, S27(b), S28, S36 and S37):
  - Web [PR #39](https://github.com/ArcForges/Web/pull/39), "[PRF.11] Blazor WebAssembly production build and generated C# SDK proof (offline units and local live run)", head branch `task/prf-11`, was reviewed and merged at head `7c668b8748a715bf2f2492867fc68b74b1814b5c` as `dd0a5de3e625086189a2e7d0fc3f3f4b70013178` on `main` at 2026-10-10T01:45:42Z. The merge commit message is "Merge pull request #39 from ArcForges/task/prf-11", verified with `gh api`. The merge ran under the `integration:Web` role, which the coordinator reports as held by `w-deku-20261008-coord` at epoch 2 after a recovery takeover of the coordinator's own expired role. That role fact is coordinator-reported and is not visible in the PR text.
  - The first delivery's offline units U1 to U9 (brief S20(d)) are the content of that merge. The record in Web `docs/prf-11-profile-proof.md` at `dd0a5de3` is the proof record for them.
- Review trail (Web PR #39). The PR has one comment, [6092259125](https://github.com/ArcForges/Web/pull/39#issuecomment-6092259125) (2026-10-10T01:37:44Z), and no GitHub review events. It records `approved` for `7c668b8` as an independent exact-head review by the session `w-deku-20261008-rev-prf-11`. Approvals are comments under one GitHub account, so independence is by session only, as the coordinator's rules define.
  - r1 found the material `base-uri 'none'` defect in the profile CSP, reproduced in Chrome 156. It was escalated and ruled S36 (brief section 11), and it was fixed in Web [PR #38](https://github.com/ArcForges/Web/pull/38), merged at `049f6a58583c2b88ed03232d7d18bb975c428a95`. The fix is the WEB.40 completion follow-up, recorded in `ledger/tasks/web-40.md`.
  - r2 found the status wording, which was fixed.
  - The head `2643127` was approved with six non-blocking notes. The approving comment states this; the PR has no separate comment for that head.
  - The live round at `7c668b8` addressed the six notes. The budget ceilings are restored to the WEB.40 values, byte-identical to `c5a5f2e`.
  - The reviewer's re-run at `7c668b8` is reported in the approving comment and is not re-run by this author: Tooling 56, Site 76 with 1 skip, Ui 15, App 96, Operations 6, Policy 108; format; Release builds with 0 warnings; publish; budgets pass; the twice-built candidate is identical and verifies; the bundle (175 members) verifies; npm test 94; audit 0. The reviewer's mutation checks (the explicit send bound, the framing kind assertion) are in the same comment.
- Post-merge proof-origin preconditions (read-only `GET` by this author on 2026-10-10): `https://proof.arcforges.com/account/` and `/chat/` return 200 with the exact profile policy, which ends `base-uri 'self'; frame-ancestors 'none'; form-action 'none'`. `/` returns the Site policy with `base-uri 'none'`. Each shell body has one `<base href="/" />` and loads `_framework/blazor.webassembly.js` from the root. These follow the CLOUD.85 completion-follow-up redeploy, observed in the CLOUD.85 record.
- Local opt-in live run against `https://proof.arcforges.com/` (claimant-reported; one local run on one host, 2026-10-10; not a CI result; the reviewer re-ran it with the same result):
  - Browser: Google Chrome 156.0.8078.12, driven by Microsoft.Playwright 1.62.0 through `ExecutablePath`. No browser was downloaded.
  - Command: `dotnet test tests/browser/ArcForges.Web.Browser.Tests/ArcForges.Web.Browser.Tests.csproj -c Release --filter "FullyQualifiedName~LivePrf11Specs"` at Web `31888e1`, the code head of the gate chain and the live run. The commits after it change no gated input. Result: 4 total, 2 passed, 0 failed, 2 skipped, 14.97 s.
  - Requests were GET only, to the two shells, the root framework path and the two pages in the browser. No credential, form or write request was sent.
  - Passed, `TheShellsAreServedOnTheProofOriginWithRootBaseAndTheExactPolicy` (HTTP): the exact profile policy on both responses, one `<base href="/">` in each shell, and `/_framework/blazor.webassembly.js` returns 200 at the root.
  - Passed, `TheShellsLoadInTheInstalledBrowserWithNoContentSecurityPolicyViolation` (in browser): 0 CSP violations reported on `/account/` and `/chat/`, and the heading in `#app h1` appeared within 60 s on both. The same-origin result of this spec is inferred from the render; the spec records no request trace.
  - Skipped, `TheAnonymousGreetingRoundTripsOnTheDeployedIngress` and `TheGreetingInteractionResponsivenessIsCapturedForTheRebaseline`. Both are blocked on CLOUD.21 and CLOUD.22 and are not proven. No interaction timing is captured or claimed.
- Hosted runs in `ArcForges/Web` for the merge head (job conclusions read with `gh run view`, no secret printed):
  - Main-push CI run [38014418588](https://github.com/ArcForges/Web/actions/runs/38014418588) on `dd0a5de3` (created 2026-10-10T01:45:44Z, updated 2026-10-10T01:52:52Z). It completed with conclusion `success`. Every job succeeded except Dependency review, which was skipped: Dependency audit and repository checks, both Source jobs, both C# restore, build, test and publish jobs, the CodeQL jobs, Build and verify the C# static candidate and profile bundle, Verify, and Deploy Cloudflare.
  - Its Deploy Cloudflare job logged `Candidate verified: 0.1.0-ci.119.1 dd0a5de3e625086189a2e7d0fc3f3f4b70013178 (20 members)` and `Current Version ID: 18a9af95-db62-43fc-bd00-22f252c8f5fe`. That deploy is the production Web Worker, not the proof origin.
  - Release `web-0.1.0-ci.119.1` (prerelease, not a draft, published 2026-10-10T01:52:48Z, target `dd0a5de3`) carries `web-profiles-c70088c50d88ce7d181f32d1f0cf65000b3d2a1127448f99dbb1b8ce6940cb95.tar` (18671616 bytes), the Account and Chat profile bundle, and `web-site-d73e069eb5ec8b59bbffbd58f415b6a65ab5f9b5939b231da7bf1a00f9d98803.tar` (26112 bytes), the C# public Site. Read with `gh release view`; not downloaded here. Cloud does not pin this release. The proof origin serves release `web-0.1.0-ci.117.1` (the CLOUD.85 pins), so the live run above tested the 117.1 bytes, not the 119.1 bytes of this merge.
- Hosted docs and proof record: Web `docs/prf-11-profile-proof.md` at `dd0a5de3` cites CLOUD.85 as the PRF.11 deployed proof-origin same-origin and base-href record (line 309). The CLOUD.85 record cites this proof for the same purpose.

## Blocked items and next actions

The completion edges CLOUD.21 and CLOUD.22 are not complete. Neither has a ledger record: CLOUD.21 waits on CLOUD.13, and CLOUD.22 waits on CLOUD.21. Completion stays blocked on both (S20(d)). The status stays `delivered`.

1. **CLOUD.21 (not started).** Next action: deliver CLOUD.21 (the real generated public methods on the deployed gRPC-Web ingress). Then set `ARCFORGES_PRF11_CLOUD_READY=1` and re-run `LivePrf11Specs`.
2. **CLOUD.22 (not started).** Next action: deliver CLOUD.22 (the ArcResult and gRPC-Web status and trailer mapping). Then run the typed-failure, cancellation-after-dispatch, and session, CSRF and logout receipt checks on the deployed origin, following the manual steps in `docs/prf-11-runbook.md`.
3. **Greeting round trip and interaction responsiveness (skipped specs).** Next action: after items 1 and 2, run the two skipped specs in the local opt-in run and record their results. The AL-06 interaction re-baseline stays pending under this task.
4. **Exact int64, uint64 and decimal calls, typed failures, cancellation after dispatch, session, CSRF and logout receipt on the deployed origin.** Not attempted, because the runbook makes these manual and authenticated. Next action: the runbook steps, after items 1 and 2.
5. **Server-stream transport decision.** The binary `application/grpc-web+proto` stream was not observed, and the decision stays open. Next action: observe the stream on the deployed ingress after items 1 and 2, and record the framing variant (brief section 5.12 requires the observed behaviour before completion).
6. **Startup time and the RunAOTCompilation benchmark.** Not measured, because no `wasm-tools` workload is installed. Next action: install the workload or measure locally, and record the result by a reviewed AL-06 re-baseline, never silently.
7. **Interaction and startup budgets.** The re-baseline of the `interactionBudgets` in `eng/policy/profile-budgets.json` stays pending. Next action: measure after item 3, then record the re-baseline.
8. **Linux-affected checks (P2-024).** Not run by the claimant. Next action: run them once in WSL2 Debian on a Linux-native filesystem, or record the hosted Linux runs for `dd0a5de3` as the evidence and say so.
9. **`npm run policy`.** It stops at the local Node pin (local Node 24.20 against the 24.21 pin). Next action: run it on Node 24.21, or rely on the hosted Source job, which the reviewer treats as authoritative.

## Coordinator rulings applied

- S20(d): PRF.11 is delivered on its offline units, and completion waits on CLOUD.21 and CLOUD.22.
- S25: the reviewer fields are ratified by the approval of `w-deku-20261008-rev-prf-11`.
- S27(b): the Account and Chat shells are served at `/account/` and `/chat/` under base href `"/"` (CLOUD.85 D1), with the framework at the root.
- S28(i): the successor of the WEB.40 app-proof row is PRF.11, whose outcome is the Blazor production build and proof gates. The WEB.40 follow-ups are recorded in `ledger/tasks/web-40.md`.
- S36: the profile CSP `base-uri` is `'self'`. The fix is Web PR #38, merged at `049f6a58`, and the CLOUD.85 verifier follow-up is Cloud PR #82, merged at `3c59ce34`.
- S37: the profile stylesheets are plain CSS. The fix is in Web PR #38.

## Untested coverage (stated expressly)

- **Everything blocked on CLOUD.21 and CLOUD.22** (items 1 to 5 above): the greeting round trip, the exact-value calls, typed failures, cancellation, session, CSRF and logout, the INP capture, and the binary stream on the deployed origin. None of them is recorded as passed or deferred.
- **Startup time and the AOT benchmark** (items 6 and 7): not measured.
- **Bundle served by the proof origin.** The live run ran against the release `web-0.1.0-ci.117.1` bytes that the proof origin serves. The merge head's release `web-0.1.0-ci.119.1` (profile bundle `c70088c5…`, 18671616 bytes) is not pinned by Cloud and is not deployed to the proof origin, so the live run does not test it. Next action: a reviewed Cloud pin move and proof redeploy under the `RES-cloud-deployment` lease, if the proof origin should serve the merge head's bundle, followed by a re-run of the live specs.
- **The live run** is one local run by the claimant, on one host. The second live spec's same-origin result is inferred from the render, and the spec records no request trace.
- **`npm run policy`** stops at the local Node pin (item 9).
- **Hosted-only steps.** The main-push CI run for `dd0a5de3` and its release are reported in the Evidence section above. This author did not re-run any hosted job, and no hosted job ran locally.
- **Reviewer-reported gate figures** at `7c668b8` were not re-run by this author.
