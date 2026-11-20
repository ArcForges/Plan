# AFV2-WEB-01 native Dashboard evidence

## Delivery

[Web PR 61](https://github.com/ArcForges/Web/pull/61) delivered the responsive Blazor Overview and device registry, current same-origin Center browser authority, exact enrollment detail, locally scoped Run availability and passkey-confirmed device revocation. The former Account, Chat and Hello probe implementations moved to test fixtures. Existing signed Contracts 1.0.0-ci.481.1 packages supply the browser and typed V2 wire shapes.

The reviewed GitHub head was `18958ccaf45b4d90af9e08099db4c0c49eb9311a`, tree `7d14c3d8a920e00693379bf5b8e9a0167049f781`. The Web merge was `2e3c6df8c481d59867fbc3a56c0180aa009ac467` with that same tree. Windows and H-22 separately fetched the exact head and used the existing `eng/verify.py run-and-report` entry point.

| Host | Stock result | Raw report under the Web Git verification log directory | SHA-256 |
|---|---:|---|---|
| Windows deku | 12/12 | `20261121-032224-18958ccaf45b-win/summary.json` | `7932d41508b675df77869fce69c00f382b9471ba5eb0270c6425ae13339baf85` |
| Linux H-22 | 17/17 | `20261121-032227-18958ccaf45b-linux/summary.json` | `d0f7b3a64d492d5c0f16344a255c1844940fad4680fe15cd1f930baaf85302d5` |

The independent source review covered the actual head and maintained its previously qualified source and authority boundaries. The main push [CI run 44802148565](https://github.com/ArcForges/Web/actions/runs/44802148565) completed successfully. GitHub retained the sealed Site candidate as artifact 14662190152 and the verified profile bundle as artifact 14662041416. The deployed-site and coupled prerelease steps were skipped, and the latest published tag remained `web-0.1.0-ci.186.1`. The original run-result JSON has SHA-256 `2cd8dd8d07f84c6b5274ebf3b8bf6f92e15a6f3224c5f8439cd7fd42bb73ae3a`.

## Native journey and authority

Windows local opt-in Chromium used the exact published Web archive `a11e88565f33546edbd2b294ed4b6b0a8d46d1c6a105df7992c7adb3309d8e1a`, Center `9b8796eac760982d9814f371b820b736ddd945c4`, PostgreSQL 18.7 and installed Node source `215125cffbab6737a71a540006dc6b2e56d4ca1a`. The browser supplied an isolated virtual authenticator as test input. The Center performed the real passkey verification and database decisions, and the installed Node enforced the real owner-local grant.

The exact Windows browser journey passed with no overlay. It verified sign-in and empty registry, installed Node enrollment, three real device list reads, three real device detail reads and two real scoped Run reads. The same Node became offline and rejoined. The browser discarded the former Run result and required an explicit renewed scope before showing the second genuine empty result. At 390 CSS pixels the page fit horizontally. Enter on the skip link focused the main landmark, and Escape from the revoke confirmation returned focus to its trigger.

The two real typed Device/Revoke attempts carried the same device, revision, command and request correlation. The first required passkey confirmation and recorded no effect. The second returned the revoked device after Center verified the passkey. PostgreSQL recorded one command receipt and one audit effect. The installed Node retained its private-data digest and the test Sandbox still had no Runs. The browser and supervised Center, PostgreSQL and Node processes drained at teardown.

The separate H-22 native API witness used the same Web head with real Center, PostgreSQL and the qualified installed Linux Node. It verified a fresh empty device registry, live device presence, a genuine empty scoped Run list, the typed offline refusal and the same scope after the Node rejoined. Chromium was used on Windows. The finished self-host route and distribution qualification remain with DIST-01.

| Evidence | Location | SHA-256 |
|---|---|---|
| Exact Windows browser/Center/Node receipt | `C:/MyFile/Projects/ArcForges/Cloud/.git/arcforges-verify/cache/center02-pg-18.7-win/web01-native-browser-14d03c8c732344b58653808dfa68bc3a/dashboard/receipt.json` | `bfd02c5f90a1b39974718d1214d77d6e1443c94c6e24ef4f6a0873de4ec061fe` |
| Windows browser phase log | `C:/MyFile/Projects/ArcForges/Cloud/.git/arcforges-verify/cache/center02-pg-18.7-win/web01-native-browser-14d03c8c732344b58653808dfa68bc3a/dashboard/browser-phases.log` | `c3f0f18b0f6910faafd625fa935e19b443cca1168ec70229e248f9113e69f1bc` |
| Exact H-22 native API receipt | `/home/sammiller/arcforges/ArcForges/.git/arcforges-verify/launches/web01-api-18958ccaf45b-linux/receipt.json` | `a8351e417b17c88f228ec41b5e76c36906f57a9d5050e91aa1abecc723029b02` |

## Application package and reviewed baseline

[Design PR 85](https://github.com/ArcForges/ArcForges-Design/pull/85) and [Plan PR 262](https://github.com/ArcForges/Plan/pull/262) scoped the separate current Dashboard budget. At the exact fully rooted Web source `e80c58fb6d01d1a1405d7e15f7dc753dc726a996`, H-22 .NET 11.0.100 stock release mode measured 62 requests, 776 shell bytes, 2,417 CSS gzip bytes, 130,237 initial JS gzip bytes, 4,254,961 initial WASM gzip bytes, 905,126 initial data gzip bytes, 238 other gzip bytes and 5,292,979 total gzip bytes. The raw metric SHA-256 was `78f1f654e9d4c18591d034e8ecd4abbc2632b7cf1e724b78aa6b712131310556`.

The current budget preserves six earlier ceilings and the 10% rule, with reviewed WASM and total ceilings of 4,680,457 and 5,822,276 bytes. The old Account/Chat budget, existing profile verifier, 24 MiB raw admission, security headers and historical release bytes remained intact. The stock H-22 control accepted the exact measured candidate and refused a private synthetic over-limit WASM sample at 4,705,762 bytes. Positive and refusal logs are in `web01-budget-controls.rDAQnZLI` with SHA-256 `7d1fd0d0cf40d5a12318bda7a8049d2fa9452f8cd90e48583a91539885d88c1a` and `7c6e54ffb4754d4c7a9488bf3c291c2e6974a15d4282298b3fef52e6ac3561be`.

The previously released static Site artifacts remain distinct from the locally routed compiled Dashboard. The existing Cloud proof archive verifier was used for byte and format compatibility. DIST-01 owns finished Dashboard route admission in the self-host distribution, and WEB-04 owns broad interaction and accessibility qualification.

## Preserved diagnostics

The original two-host exact `021d83a` checks exposed ten generated lockfiles without their required final LF. The source and all original receipts remain available. Later exact heads also exposed missing full-trim component metadata, excess current WASM gzip versus the earlier probe benchmark, a keyboard skip that failed to focus the content landmark, and a missing correlation identifier refused by the real typed Run API before effect. Corrected only the demonstrated flaws. Authored Windows diagnostics retained both successful renderer checks and original failure traces in the Web verification directory. Real scoped Run empty, offline and rejoined states are covered only by their corresponding positive native receipts.

The exact R9 browser archive exposed a separate full-trim issue during the actual WebAuthn call after Center supplied a valid passkey challenge. The original private phase log `web01-revoke-diagnostic-browser-fe985950234641e08c9052eab32db5ee/dashboard/browser-phases.log` under the Windows Cloud verification cache has SHA-256 `224b28b7f7f78dae30bcc9b2b079dd721d3182927a32d5d620849c820d64020b`. It recorded the managed JSON exception before any assertion reached the Center. R10 used the same single fingerprinted browser module with string-only interop, retained the full trim mode and verified the actual native passkey and durable effect. The Windows candidate archive and H-22 stock candidate `d5e9a9d1c4776962b08d22c209891ff4e9c3c7fdfd2dfa53181acefc85937e65` are retained under their Web Git verification directories.

AR-05 remains open. The preserved FILE-02 H-22 refusal establishes pre-effect safety for the current Linux storage profile. FILE-02's required native positive deletion and interrupted recovery still require a supported exact-directory guard. WEB-02 and the rest of the dependency chain remain gated by FILE-02.
