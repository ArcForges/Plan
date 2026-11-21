# AFV2-WEB-03 development evidence

[Design PR89](https://github.com/ArcForges/ArcForges-Design/pull/89) merged as `d06e9346cdefc643cb3ba580d501ae45e68694b0`. [Plan PR276](https://github.com/ArcForges/Plan/pull/276) merged as `9aba69e66e8f974b74e0a7e225dabdad482d7d6b`. Design passed 4/4 and Plan passed 5/5 on each designated host. The Plan checks used actual merged Design main.

## Development scope

The Dashboard provides security, account and subscription views using the shipped Center routes. It presents scoped security facts and original command reconciliation, and uses the same-origin Center recovery and lifecycle pages for protected proof, confirmation and export. Self-host mode reads only actual capability decisions and directs the user to operator limits. Official mode displays server quotes, checkout and renewal state and bounds actions to the selected account and original identifiers.

The 13 focused tests use real Blazor views and production typed transport with scripted responses. They cover signed-out and expired sessions, exact profile retry and conflict, pending deletion and the Center proof handoff, missed session revoke replies, stale and unavailable credential views, read-only grant limits, disabled commerce in self-host and closed official sales, read-only renewal reconciliation, and the purchase and checkout request sequence. A mismatched checkout response never exposes the supplied link or creates another purchase. Tests neither visit a provider nor run an integrated browser journey.

## Packaging diagnosis

The initial Windows preflight used the pinned SDK with the prebuilt WASM runtime. It measured 5,154,963 WASM gzip bytes against the unchanged limit of 4,680,457. Narrow fixed RPC descriptors alone still measured 5,139,131 bytes and the diagnostic archive was 27,446,784 bytes against the offline origin's unchanged 24 MiB maximum.

Linked metadata traced two non-payload diagnostic presentation paths into the full protobuf descriptor graph. Replacing only the Dashboard's linked `JsonFormatter.ToDiagnosticString` and `RepeatedField<T>.ToString` implementations with an explicit unavailable message eliminated that graph. The app continues to use the published generated clients, protobuf encoders and response parsing. An isolated comparison proved that substituting `MapField<TKey,TValue>.ToString` as well had no effect on the resulting bytes.

The isolated Windows optimization experiment used generated clients and the two publish-only diagnostic substitutions. It measured 62 primary resources, 4,396,809 WASM gzip bytes, 5,435,730 total gzip bytes and a checked archive of 23,826,432 bytes, SHA-256 `1c02edb9b72fe275d342d53152040934c64256c2fad8b758928e76553357a759`. The coordinator's separate integrated Windows preflight measured 4,396,682 WASM gzip bytes and 5,435,596 total gzip bytes. Published packages, profile limits and verification entry points retain their inputs. The required Windows and H-22 repository checks provide the merge evidence.

The first pushed head `0f25ad7e8133a62e8c718a79721ce8007f558cb6` passed the Windows profile 12/12. The report is `20261121-142627-0f25ad7e8133-win/summary.json`, SHA-256 `907f4733c7e3e253929d6d583f3857d3eddcc116aaef8352a952b7903196bc30`. H-22 passed compile, test and publish. The original source gate then rejected the changed App project hash because its active dependency review still named the earlier hash. The refusal remains in `20261121-142630-0f25ad7e8133-linux/summary.json`, SHA-256 `cbbd2154c5dc0a0d4e0560d1eaafa83e8c99d6a04803d39e0a3c676e8fb78741`.

[Plan PR277](https://github.com/ArcForges/Plan/pull/277) merged as `9c6675bd63c62f7c08423c46f2b655c3509983b4` after both 5/5 host checks. The reviewed successor receipt binds the exact App project and diagnostic XML inputs. It preserves the previous review records and uses the same locked dependency versions, published package evidence and dependency scanner.

## Exact native and static results

The independently reviewed [Web PR63](https://github.com/ArcForges/Web/pull/63) head is `bdc900d93e618fa41df11b9a0d44293c6c685691` with tree `6613247c7405823ae1fc4fc8f711c8f79524c372`. Web main merged as `9b8ae6a954e3a8166a1d756037bcdda64a4e851d` with the same tree.

Windows deku fetched the same head from GitHub and passed 12/12 steps with the unchanged repository profile. The App suite passed 155/155 with zero skips. The raw report `20261121-143154-bdc900d93e61-win/summary.json` in the Web Git verification log directory has SHA-256 `3f739966543b3ca8d0ba67cf37365c8128191bf1faea7a0e97278e224138bb3e`.

H-22 fetched the head from GitHub and passed 16/16 steps with the unchanged `python eng/verify.py run-and-report` profile. The App suite passed 155/155 with zero skips. The original summary `20261121-143156-bdc900d93e61-linux/summary.json` in the Web Git verification log directory has SHA-256 `419d21141eeef9edf5198a7f5218cc4b74be343c19aaef3dcd3694643ec4ccfe`.

The stock H-22 candidate passed all eight original package dimensions. It measured 62 primary resources, 776 HTML bytes, 2,467 CSS gzip bytes, 131,075 JS gzip bytes, 4,396,372 WASM gzip bytes, 905,126 data gzip bytes, 238 other gzip bytes and 5,435,278 total gzip bytes. The verified local archive contains 187 members and is 23,824,896 bytes with SHA-256 `9d612aecb98c5c4ec54200d1812250f0ca9cde80e835d4056cf9eb1d19e0d41a`. The H-22 verification worktree then passed both existing `node --test tests/browser/dashboard-origin.test.ts` cases against that exact tar path and digest, covering the added account and security routes, cache and CSP rules, and damaged archive rejection. This test serves requests in process and starts no browser.

The coordinator captured the exact H-22 supplemental stdout in the Windows Web Git verification directory as `web03-static-bdc900d.txt`, SHA-256 `40516aff81d8439b675ed83d3031d7c90b009ded7ecc9764a7d8dc7fa6a9f4c0`.

## Merged-main candidate

[Web CI run 44876273133](https://github.com/ArcForges/Web/actions/runs/44876273133) succeeded at the exact merge. GitHub retained the sealed candidate (artifact `14696002688`, ZIP SHA-256 `85d8685dc5de5d7d057a06446a079fa1ffebcc3f19e2fddf0716091dca910425`) and verified profile (artifact `14696032672`, ZIP SHA-256 `9d795eeb7fdfe74366bac4ca77573f4bf8e67d40128ed40258977b265f1fcf3d`). The Cloudflare deploy job and its coupled prerelease were skipped.

## Remaining qualification

The staged tests do not establish new browser-to-Center, PostgreSQL, account, payment or native Node effects. The prior ID-01 and HOST-02 receipts retain their original scope. WEB-04 and ACC-02 retain integrated browser and business qualification under AR-12. Public provider and deployment acceptance remains under AR-10 and PROD-01.
