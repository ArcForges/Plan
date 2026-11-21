# AFV2-WEB-04 development evidence

[Design PR90](https://github.com/ArcForges/ArcForges-Design/pull/90) merged as `b213cdb619a05ac8ddd3a866411e58f121a892d2` after both designated hosts passed 4/4 checks. [Plan PR279](https://github.com/ArcForges/Plan/pull/279) merged as `fcb1422a399a2b3548aa833e493008e6d6bbe0b9` after both hosts passed 5/5 against that Design main. The recorded development scope uses typed mocks and local intercepted rendering.

## Application checks

[Web PR64](https://github.com/ArcForges/Web/pull/64) final candidate `ff932b6b082584deb4897837ea462566b1c05209` has tree `0abcb9dbf7db9df71c42e8ca26b2a5168b96e11b`. The independent nonauthor review covered all 28 final changed paths and closed findings for late mutation replies, overlapping device rechecks and stale checkout links. Review of the two successors confirmed that the product code and browser fixture still match `7d805f9e0d3f75b3cf1815da44752b6fec3883c9` exactly.

The local Release App suite passed 165/165 with zero skips. Ten added cases exercise keyboard interaction in destructive confirmations, overlapping rechecks, same-session command reconciliation, old Node epoch responses, interrupted output and checkout recovery. The transport fixture holds a Stop response through a bootstrap failure while the original token remains live. A new Stop sends zero requests, the late original acknowledgement remains uncertain, and the restored exact session reads the original outcome without replay. The initial combined run exposed two fixture timing races and a missing stylesheet token. The fixtures now wait for the loaded views, and the stylesheet retains the original root font token and value.

Both initial native runs rejected `7d805f9e0d3f75b3cf1815da44752b6fec3883c9` for fixture whitespace. The original summaries remain in the Web Git verification log directories. Windows `20261121-144952-7d805f9e0d3f-win/summary.json` has SHA-256 `dc41c5075b8d33f022f2a104f7753aa1426e514fe5b7b9ca19f4cc4308da0883`. H-22 `20261121-144954-7d805f9e0d3f-linux/summary.json` has SHA-256 `49512044550c658d25854da2a67bc28443b9a1acb4e6c2b8a1420c67252e852c`. The App test project's full formatter and Release suite passed locally after correcting the fixtures.

Windows passed 12/12 at `a02a6479b48bb98b90a5a6ad36e8d02a2bc509be`, including 165/165 App tests. Its report is `20261121-145152-a02a6479b48b-win/summary.json`, SHA-256 `72e6d8d69b0f6b3e491a176fd204d729edc7f9bf1d3e51fb82c77df96d8dcd91`. For the same candidate, H-22 passed format and build and then passed 164/165 App tests. The lost export reply fixture waited for a pending action to render and could click it before it became enabled. The failure also reproduced in targeted runs on H-22 and the workstation. The H-22 report is `20261121-145134-a02a6479b48b-linux/summary.json`, SHA-256 `5a7484e6896caf678e39ad4ce96c40e6f892ca081bbd534a574d2dfbe7f978bd`. The repaired fixture awaits submission and the enabled controls. It keeps the original download, lease and release checks and verifies exactly one original-result query. The repaired case passed six consecutive targeted workstation runs with the existing timeout.

## Local visual mock

Chrome 157.0.8103.79 passed 4/4 on local assets built from `7d805f9e0d3f75b3cf1815da44752b6fec3883c9`, at 320×760, 390×844, 1280×900 and 1440×900. The final candidate retains the exact App and browser-test input files. The tests exercise keyboard navigation, menu Escape and focus return, the skip link, horizontal document fit, light and dark themes, reduced motion and axe. The shell uses a scripted signed-out bootstrap answer. Requests are intercepted in process, with unexpected requests aborted and counted as failures. The fixture opens no listening service and uses no real Center, Node or provider.

The Windows Web Git verification directory retains `web04-mock-7d805f9e0d3f/browser.log`, SHA-256 `aa2e21a7d7aba0f28ed0fc279207817207ea0e3d88c13f995b23eb3067edcef0`, and four matching screenshots. A separate synthetic stylesheet check on Chrome passed 14 viewport and theme combinations, including local overflow for tables that retain all columns. The same directory preserves `stylesheet-light.json` with SHA-256 `55c7d5e013be96ee6d0309c86d9fe2fffada2c3cca56a3b44ee1e108bee3262d` and `stylesheet-dark.json` with SHA-256 `4d0608a35671601de9921580dadf04f0421456925b0a01876eafcf1cbeec9689`. The local App publish passed the stock profile limits, with CSS at 2,462 gzip bytes against a 2,469-byte limit. The initial Playwright run without an explicit executable could not find its cached Chromium revision. The passing run selects the existing workstation Chrome installation.

## Exact native and archive results

Windows deku fetched `ff932b6b082584deb4897837ea462566b1c05209` from GitHub and passed 12/12 with the unchanged repository profile. The App suite passed 165/165 with zero skips. The raw report `20261121-145538-ff932b6b0825-win/summary.json` in the Web Git verification log directory has SHA-256 `7bba90eb2fe8ed043eb8f77bc6d65da6f6c4c3b318d6ead977f63b31e3e78a4f`.

H-22 fetched `ff932b6b082584deb4897837ea462566b1c05209` from GitHub and passed the unchanged repository profile, 16/16. The App suite passed 165/165 with zero skips. The native report `20261121-145510-ff932b6b0825-linux/summary.json` in the Web Git verification log directory has SHA-256 `9be9d360cb7e341b95d0eea6ba8a22ddee550b9c11cf15679d33eac21716cea4`.

The H-22 candidate passed all eight stock package dimensions with 62 primary requests, 776 HTML bytes, 2,462 CSS gzip bytes, 131,074 JS gzip bytes, 4,401,724 WASM gzip bytes, 905,126 data gzip bytes, 238 other gzip bytes and 5,440,624 total gzip bytes. Its verified archive measured 23,851,008 bytes and has SHA-256 `1bedf2012eea23f646efe47f2891e6fdf75b3aab3d3800e79f2a6e2e0e77ac3c`. Both offline static-origin tests passed against that exact archive. H-22 retains the supplemental `web04-static-ff932b6.txt` in the Web Git verification directory, SHA-256 `dbba6de20bef945fa682b12ae6cecc932cec824b6cf9590b536d3873be426bd6`.

## Merged-main candidate

[Web PR64](https://github.com/ArcForges/Web/pull/64) merged as `d517bc45fc50e3143a25c7987726f37a24a4999b` with the same reviewed tree.

[Web CI run 44878070038](https://github.com/ArcForges/Web/actions/runs/44878070038) succeeded at the exact merge. GitHub retained the sealed candidate, artifact `14697146396` with ZIP SHA-256 `e7ddd522396380e0d5ceee69ffa7b52d4409e0b3930edaaac42f9830040e42e3`, and the verified profile, artifact `14697136647` with ZIP SHA-256 `40c0c282a11e7be71b67266e9f0f8d5b534759476644f3ce7dae1b067b5df600`. The Cloudflare deploy job and its coupled prerelease were skipped.

## Remaining qualification

F-WEB-01 and AR-09 remain open for the connected workspace, manual assistive checks and recovery qualification required for task completion. ACC-02 retains integrated browser and business acceptance. The existing authenticated and native receipts keep their recorded scope.
