# AFV2-WEB-02 development evidence

The owner chose sufficient mock coverage before integrated browser acceptance. [Design PR88](https://github.com/ArcForges/ArcForges-Design/pull/88) merged as `a80a0b83066d69f1f3a7e7c9dd26acd980f498d0`. [Plan PR274](https://github.com/ArcForges/Plan/pull/274) merged as `8ba0b5777362337ad642ed7fdcc2eebbf21dd7fd`. Design passed 4/4 and Plan passed 5/5 on each designated host, with the Plan checks recorded against actual merged Design main.

## Scope and deterministic checks

[Web PR62](https://github.com/ArcForges/Web/pull/62) implements the Sandbox, Run, resource and regular-file transfer views using the published typed Center routes. Browser control uses an exact local grant and captures the original command, owner epoch and applicable revision before sending. Read-only reconciliation reports the returned effect. Sandbox deletion preview and complete configuration editing remain available through the owner-local Node CLI. Remote resource policy changes are limited to tightening an existing confirmed Run throttle overlay.

The adjusted candidate `0500aa6524dd5d5abf4fbbcd6a9fea03ae1d8890`, tree `27c3a4952b0934243e4af4cd22a0a720a051d0a2`, passed independent review. Web PR62 merged as `6d090f2dab401eb393ebf18aea6f49043675c5eb` with the same tree. The reviewed source and test scope covers grant-scoped Sandbox observation, bounded request size, accepted and compacted creation receipts, launch and stop, exact original uncertainty reconciliation, escaped bounded output, resource compare-and-set, and export retention with explicit release.

Windows development ran `dotnet test tests/ArcForges.Web.App.Tests/ArcForges.Web.App.Tests.csproj --no-restore -c Release`. The complete App suite passed 142/142 with zero skips, including 15 focused typed mock cases. Fixtures use production generated request construction and actual Blazor components with deterministic responses and wire failures. They exercise missing owner epoch, cancellation of late device responses, the closed route map, rejected oversize requests, operation reconciliation, stale and unavailable controls, ordered argument arrays, escaped output and retention gaps, typed provisioning and resource conflicts, and download followed by separate snapshot closure.

An earlier isolated App suite had 141 passes and one failure. Its strict JavaScript interop inventory still expected only the two previously approved importers. The final check admits the additional importer for verified downloads, checks the actual shared module's content identity, and retains the existing Content Security Policy.

## Original build failure and correction

The first pushed head `be108822cf1713363b8d054cb30d5e475a21b9c8` passed Windows 12/12. H-22 reached its final candidate step after build and tests, then refused 69 published primary resources against the limit of 62. The unchanged measurement function showed CSS at 2,498 gzip bytes against the limit of 2,469. All six other dimensions met the existing limits. The original Windows and H-22 `summary.json` digests are `cc9c3a5e52b303583f152417b28fab10d93a2b7d966e0a3bc24ae04ce154491e` and `9a01d2f207558581f87e3ab61b57aa1d35fc09c92bc7ac9279e9148fd71e2f1f` respectively, under the corresponding Web Git verification log directories.

The linked assembly comparison found six new TypeConverter-related assemblies retained by two enum-valued Razor selectors. An explicit choice for each valid value preserves both selectors and uses the existing string binding path. The download function now shares the existing content-addressed browser module with lifecycle and passkeys, removing the extra script. Shared styles cover the previously duplicated rules. The two budget files, verifier and 10% rule remain unchanged.

## Exact native and static results

Windows deku independently fetched the adjusted head from GitHub and passed all 12 steps of `python eng/verify.py run-and-report`. The App suite passed 142/142 with zero skips. The raw report `20261121-140745-0500aa6524dd-win/summary.json` in the Web Git verification log directory has SHA-256 `05cd8422a273cec9bba85a894ee1ef9567c99f04539be9052023f8546e521674`.

H-22 fetched the adjusted head from GitHub and passed all 16 steps of `python eng/verify.py run-and-report`. The App suite passed 142/142 with zero skips. The raw report `20261121-140747-0500aa6524dd-linux/summary.json` in the Web Git verification log directory has SHA-256 `db1042b8f13b1007b8a82ffb3ba0ccd7d3f011abc1cb61e124bc73cebbbbce9e`.

The H-22 candidate passed all eight unchanged metrics. The measured primary resource count was 62, HTML 776 bytes, CSS 2,467 gzip bytes, JS 131,076 gzip bytes, WASM 4,358,280 gzip bytes, data 905,126 gzip bytes, other 238 gzip bytes, and total 5,397,187 gzip bytes.

The stock verifier accepted the 187-member profile archive with SHA-256 `27b1e5fed3a1ec82be6ed9d4a3f287d41a51e10c65b7c76778b640254af07ba1` and size 23,719,936 bytes. The same H-22 worktree ran `node --test tests/browser/dashboard-origin.test.ts` with the archive path and SHA-256. Both offline cases passed, covering the exact nested Dashboard routes, CSP and cache handling, and rejection of altered archive bytes. No browser process was started.

The coordinator's exact supplemental measurement and offline test outputs are retained as `web02-coordinator-observations.txt` alongside the Windows final summary with SHA-256 `ff6c1a68dad90d5a173236001515afff1c448ed56cdbca02f65d983d6cc49f08`.

## Merged-main candidate

The exact merged tree completed [Web CI run 44874344286](https://github.com/ArcForges/Web/actions/runs/44874344286) successfully. GitHub retained the sealed candidate (artifact `14695600805`, ZIP SHA-256 `dca59f7680d5939136fa34d6c84be392f0dcef8c47ec468d82563e9a76e4b00e`) and the verified profile bundle (artifact `14695003782`, ZIP SHA-256 `4a43bfb7d8da8f226f00a87b7ec4d86e712a90b05da0a3498ceea3e4ebd6b275`). The Cloudflare deploy job and its coupled prerelease were skipped.

## Remaining qualification

The integrated browser, Center, PostgreSQL and native Node effect scenarios remain unverified in this stage. The later qualification remains under WEB-04, ACC-02 and AR-12. Earlier native CENTER-03, CENTER-04 and FILE-02 evidence keeps its original scope. The protected Linux FILE-02 native qualification remains open under AR-05 and F-FILE-01.
