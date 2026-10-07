---
task: PLT.54
status: delivered
recorded: 2026-10-07
claimant: w-codex-20261006-image
epoch: 1
---

# Real parser containment implementation and observed Windows components

The production-parser hostile-input harness, explicit authenticated-release configuration and invocation cancellation repair are merged. Implementation delivery is separate from signed installed-release and full-RID acceptance. The tested native libraries contain genuine Image and PDF implementations; neither a mocked OS boundary nor the deliberately hostile first-party fixture is represented as production decoding proof.

## Source and independent review

[DesktopPlatform PR169](https://github.com/ArcForges/DesktopPlatform/pull/169), exact reviewed head `a5a0331c88da092d2cef4d7b07a211b98247fb1e`, was merged as `b2ade44372ff6c6ff8b67c19ec15d195d3a11db3`. Independent reviewer `w-codex-20261006-platform` reviewed all eleven changed paths and approved the exact source at [6031657709](https://github.com/ArcForges/DesktopPlatform/pull/169#issuecomment-6031657709). Separate agent/session review is independent despite the shared GitHub account. Existing native codecs, strict PDF admission, PLT.60 profile/process lifetime implementation and production parser factories are preserved.

The reusable harness verifies bounded PNG/TIFF/EXR metadata, RGBA8/float32 pixels and hashes, malformed/truncated input refusal, geometry budgets, stale handles, cancellation, abrupt child loss and recovery. Explicit authenticated mode requires bounded duplicate-free operator configuration with exact RID/version/source/helper hash, approved P-256 publisher keys and exact Image/Pdf manifest/profile identities. It uses genuine release trust; no unsigned fixture is promoted to publisher authority.

The nonpackable hostile fixture preloads both genuine Image/Pdf libraries through the production loader before applying the existing OS isolation and executing unchanged first-party attack scenarios. It is not registered in the production helper and does not implement a format decoder. Broker RunAsync now ends a live invocation through the existing cancellation lifecycle when its caller cancels before or during admission, preserving the original caller token and idempotent drain behavior.

## Actual component validation

Pinned SDK 10.0.400 Release compilation, scoped solution formatting and 37 ordinary component cases passed. Both admission regressions first failed against the unrepaired broker, then passed after the focused repair. Exact clean-head dependency admission passed with 62 NuGet/10 Python/314 input hashes; source provenance passed with 1125 files/25 reused targets/144 records. Production helper and separate hostile fixture win-x64 Native AOT publishes passed with zero warnings and unchanged committed source locks.

On actual Windows 11 build26300, 26 distinct scenarios passed: eleven real Image cases, four real PDF cases and eleven native-loaded hostile/lifecycle cases. Both genuine libraries were loaded before AppContainer/Job restrictions. Observations include actual pixels and hashes, bounded refusal/recovery, cancellation, abrupt process loss, parent death, token/file/environment restrictions, process spawn refusal, input-write refusal, network listener isolation, crash/hang supervision, memory limits and storage lifecycle. The UDP sender's successful send result is not itself denial evidence; the bounded parent TCP/UDP listeners observed no received data.

An initial test-DLL invocation through dotnet failed only the PDF self-parent entry because Environment.ProcessPath then selected the dotnet host without its assembly argument. That failed observation remains retained. The correct actual test apphost invocation passed all four PDF and eleven hostile cases; the previous eleven Image successes remain distinct observations. No unchanged OS suite was rerun after merging.

The actual helper SHA256 is `4f541ffca96305f6898c0a7760a9a204f85892f65179dda1ec54091a9529e7a3`; the separate hostile fixture SHA256 is `c5259497819e4be22f4c32e1d7680e4431702e3399815e624fa3ec81550af789`. Component directories contain exact copied native manifests, Image DLL `7bcdbc2765bd3fc8a09dc8d628d8f49c250466889145752d53af49240daabbcb`, PDF DLL `892eab79eb1075db7b54916b04fdfe5c8bcbf7dc4c7ebe488b08d20803d742a5`, PDFium and matching approved CRT bytes. This unsigned mixture of actual compiled inputs is not a same-source signed deployment cohort.

Raw test results, initial failure and copied-file hashes are retained in the task worktree under artifacts/plt54-production-real.trx, artifacts/plt54-native-hostile-real.trx, artifacts/evidence/plt54-production-component.json and artifacts/evidence/plt54-actual-windows-components.json. These local component receipts do not assert registry publication or external signing authority.

Exact-head [CI37576715741](https://github.com/ArcForges/DesktopPlatform/actions/runs/37576715741) passed all 22 applicable checks, including ordinary managed packaging, native production staging, source/security policies, nine AOT checks and aggregate CI. Hosted compile checks are not OS-isolation acceptance.

## Actual normal publication

Normal main [Publish NuGet37578664127](https://github.com/ArcForges/DesktopPlatform/actions/runs/37578664127) completed SUCCESS for exact merge source `b2ade44372ff6c6ff8b67c19ec15d195d3a11db3`: all24 jobs succeeded. [Publisher112657303512](https://github.com/ArcForges/DesktopPlatform/actions/runs/37578664127/job/112657303512) verified and promoted the same original candidate **1.0.0-ci.123.1**. Its retained log contains25 package push attempts,25 Created acknowledgements and25 successful push receipts between `2026-10-07T06:10:17.4932487Z` and `2026-10-07T06:10:41.4625037Z`. The actual cohort contains23 managed packages, Build.Policy and the existing Image win-x64 runtime; its additional admitted managed Pdf package is preserved. No ContentSandbox runtime or additional unbuilt RID is represented as published by this record. No public package download, extra republish or installed-consumer rerun was performed for the ledger.

## Deferred acceptance and precise owners

NAT.25 owns the actual same-release authenticated Image/Pdf/helper runtime bundle, external approved publisher authority and signing/publication handoff. PLT.54 owns execution of its authenticated-release entrypoints against that real bundle and remaining supported-RID OS observations; the current real Windows component run does not certify Linux/macOS or a signed installed binary. PLT.63 owns the remaining real macOS XPC lifecycle adapter. PLT.46 and product/release tasks retain installed-product and commercial end-to-end acceptance. There is no human-only blocker for this implementation producer; deferred signing/account or OS evidence is never replaced by a success stub.
