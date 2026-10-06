---
task: NAT.11
status: delivered
recorded: 2026-10-06
claimant: w-codex-20261006-image
epoch: 1
---

# Production PNG/TIFF/EXR implementation and actual win-x64 publication

The complete still-image native implementation, internal managed binding and production helper composition are merged and published. Implementation delivery is distinct from full packaged-RID, installed-helper and OS containment acceptance. No scripted parser, mock or unexecuted RID is represented as production runtime evidence.

## Source and independent review

[DesktopPlatform PR151](https://github.com/ArcForges/DesktopPlatform/pull/151) final reviewed head `2a3985475151551e37cecd2bfade72d60e93d926` was merged as `57d0e995c1efda621f308b0ac9b94d6a057ff7b6` at `2026-10-06T22:04:40Z`. Accepted NAT.15, PLT.59, PLT.33 and GOV.24 implementations, every accepted receipt and all existing package identities are preserved.

The actual C++ Image implementation exposes the closed six-export ABI1.1, preserving all three historical preambles and C17 layouts. PNG/TIFF/EXR factories are bound directly to the pinned static OpenImageIO/OpenEXR/Imath graph. Metadata retains native precision, image/subimage/mip geometry and alpha/transfer semantics. Region decoding supports unaligned, repeated and backward tiles, bounded scratch/staged output and explicit conversion-loss reporting. Generation handles, a finite 64-slot table, cancellation/deadlines, short/error callbacks, malformed/nonfinite geometry and stale/double-close refusal are implemented. C++ callback reentry and concurrent native borrows refuse rather than blocking into a callback deadlock.

The managed reader owns the native/input/cancellation lifetime with one reserved or active borrow. It refuses parallel borrowing before scheduling, fences every active image callback across readers, drains close once, and releases reservations even when caller-owned MemoryManager span acquisition throws. All eight parsing types are internal, with only the existing helper/test friend access. The nonfriend compiler regression returns actual CS0122 for each parsing type; historical typed ImageAbi diagnostics remain public and compatible.

ProductionParserProfile creates the actual NativeImageParser and preloads/admit-checks both Image and accepted strict PDFium libraries before OS restriction. The helper image parser composes the real internal reader, validates geometry/pixel transfer/precision and obeys host cancellation and resource bounds. Existing parent supervision and broker authorization are preserved. Actual helper composition, codec implementation, managed package activation, exact Image6/PDF8 registry/staging/minor contracts and architecture inventory are implemented; no success stub or fake decoder is registered in production.

Independent substantive review by observability found cross-reader callback deadlock/queued borrowing and exceptional MemoryManager reservation release defects; each was fixed with actual loaded-codec regressions. The substantive core approval is [core approval](https://github.com/ArcForges/DesktopPlatform/pull/151#issuecomment-6022601371), internal-boundary [boundary approval](https://github.com/ArcForges/DesktopPlatform/pull/151#issuecomment-6023529180), accepted-parent successor [accepted-parent approval](https://github.com/ArcForges/DesktopPlatform/pull/151#issuecomment-6023979481), PLT59 integration [PLT59 approval](https://github.com/ArcForges/DesktopPlatform/pull/151#issuecomment-6025866036), and latest GOV24 delta [final approval](https://github.com/ArcForges/DesktopPlatform/pull/151#issuecomment-6026072237). Review is independent by separate agent/session despite the shared GitHub account. Own codec/reader/helper/test bytes are unchanged across the final integration successors; accepted legal/receipt history is preserved. Each private unaccepted NI candidate receipt was archived before its authorized reseal; no accepted receipt was rewritten.

Actual local evidence retained: real PNG16, TIFF16 uncompressed/ZIP/LZMA/multipage/associated alpha and EXRhalf/five-mip precision, tiles, padding, conversion, malformed/nonfinite input, failed/short I/O, cancellation/deadlines, callback/concurrent BUSY and 64-slot/stale/double-close cases. Actual loaded native reader tests cover asynchronous lifecycle, callback close, cross-reader refusal, caller memory exceptions and subsequent normal read/close. The helper suite passed 189 tests with nine explicit opt-in OS checks skipped. Actual SDK10.0.400 win-x64 Native AOT helper compilation/publish had zero warnings/errors. Scripted native-reader tests demonstrate only the helper/broker component composition, not real OS isolation. Actual later ARM Image6 cross-compilation is retained under NAT22 as a component prerequisite, not a published or executed ARM package.

Final narrow checks passed: dependency admission62 NuGet/10 Python/289 inputs, source provenance1055 files/144 records, four closed Image ABI inventory tests, and14 affected metadata/registry/external/Assistant324 guards. Generated helper locks were restored with the pinned SDK after the accepted PLT59 rebase; the GOV24 successor changes no restore inputs or generated lock bytes. Exact-head hosted CI37536237910 completed SUCCESS at 2026-10-06T21:58:15Z; all 22 applicable jobs passed. Managed pack passed ContentSandbox185/185 with 17 explicitly skipped OS/loaded-native opt-ins and general Platform878/878 with 23 explicit OS opt-ins skipped; these CI skips are not runtime acceptance. PR native-stage artifact11446796941 is5,575,109 bytes with provider digest sha256:d4250651d413ee1df7fca77b61dd63c88da718ab9fac2ff42fd42cbac52d87a0 and source2a398547, not a main publication. The prior b26 CI native/policy/all nine AOT jobs succeeded, but its remaining package job was canceled when the mandatory accepted GOV24 rechain replaced that candidate; it is not final CI evidence.

## Actual normal publication and producer handoff

The normal [Publish NuGet run37538249908](https://github.com/ArcForges/DesktopPlatform/actions/runs/37538249908) completed SUCCESS at `2026-10-06T22:35:49Z`, with all 24 jobs successful at exact merged source `57d0e995`. The [publish job112535306859](https://github.com/ArcForges/DesktopPlatform/actions/runs/37538249908/job/112535306859) completed the source/allowlist/contents/hash recheck before authentication, exchanged GitHub OIDC identity, and pushed the same verified candidate bytes. All24 packages at `1.0.0-ci.113.1` received actual NuGet Created acknowledgements between `22:35:26Z` and `22:35:45Z`; no manual republish or installation was performed.

The source-bound candidate artifact `nuget-candidate-37538249908-1`, ID11449140712, is 6,635,951 bytes with provider digest `sha256:2cdc0015e8e1db3a5ca81da8c3eb59107982761a5a417c33aca4446efb0d4b73`. Its canonical manifest SHA-256 is `884597d690807fc52496714ad2d9eb414a60674142207d000d747bd4824ce3b6`, exact clean CI identity `37538249908.1`, source `57d0e995`, version `1.0.0-ci.113.1`. One authenticated workflow-artifact acquisition for the delivery receipt verified all 24 extracted package hashes against that manifest. This was source-bound delivery evidence, not routine public-feed download/install revalidation. The embedded Image DLL in the actual Runtime package matches the independently verified producer DLL hash below.

The real main native artifact `native-stage-37538249908-1`, ID11447619610, is 5,575,115 bytes with provider digest `sha256:1fce825f1d339a344b963c22db776d37e4dc5b0b1b57d79553bf326dc8810298`, created `2026-10-06T22:24:44Z`. It was acquired once as NAT.22's mandatory actual producer prerequisite and verified using the retained exact-source `57d0e995` checkout: native source/build/package-set/inventory verifier passed all 191 Image runtime material files and every extracted file hash. The approved common inspector observed PE32+/x86_64, identity `ArcImageNative.dll`, exactly the six callable Image exports, no forwarded/data/unnamed exports, actual ABI1.1 and embedded clean source/build identity. Actual DLL SHA-256 is `56c041b2ad8f766562c33617f54d8a6cb3c63b121d51382227d8b035d4694858`; the staged artifact manifest bound by the candidate has SHA-256 `703823238ca782346bacfa46ffd2a76317d43f6bab3c2a40edde812b31c50b36`. Original licence, vcpkg source/recipe and compiler redistributable material remain in the complete inventory. Provider compressed archive digests are remotely observed metadata, not independently recomputed ZIP digests. No upstream re-download was performed.

Published allowlisted package SHA-256 values below come from the exact source-bound manifest verified by the successful normal publisher; every row has version `1.0.0-ci.113.1` and its actual Created acknowledgement.

| Package | SHA-256 |
| --- | --- |
| ArcForges.Build.Policy | `40c94417a8e4f8b490cf3266151210215d17b0c8e48193fdb3b7058476448fe0` |
| ArcForges.Native.Abstractions | `66903aed327c812dca1cdf795ee63ede8da5c816651021e086643232f0a3fc66` |
| ArcForges.Native.Image | `f3339c48608706a8f931704f0ba68f57606af7d5add70ec21524d856147609ca` |
| ArcForges.Native.Image.Runtime.win-x64 | `2818babcf7f1a309438551f545650156c4d41d8ec994c866088a7134343acf5e` |
| ArcForges.Foundation | `3a4ed976d5dd80123349be86784eb22f3086d139d87b3f618d32d4c7375e3f2d` |
| ArcForges.Application.Abstractions | `4eaccd7d3d78a566fbe16da6553dbd5c4fdd97710c828b5c8f7d0608812f2c44` |
| ArcForges.Assistant.Abstractions | `b6330b873f90aa2da2817e7537466be7d1939ab0c499976f6360598bb0ff0c6a` |
| ArcForges.Capabilities | `98fa7afea0ff947f17bfa182f6a14ce14ad73d4ab84431303bbe245a8f927e97` |
| ArcForges.Persistence.Sqlite | `83f6f6c5a9cb08fca92263e1df9eee5edcc14a4f3aa3ed6e6a734a833f23cb9b` |
| ArcForges.Persistence.Resources | `8b4c482e7c015a231f028e566865a2b0fb8621f7021033407f9b9a1715a0c5e6` |
| ArcForges.Persistence.Derived | `0cf6b2c14179c46d40d81f26d613ddd09c90d7f9b996734510cebe82199a0041` |
| ArcForges.DesignSystem | `7107c4f97598b69544c406833182e50acda57c2a812d3e27951fd66150ad384b` |
| ArcForges.Desktop.Shell | `5e446019f1f61d5a3f729da69087cbb8206e50636f1c21b26ffd2a9ae5f33c2d` |
| ArcForges.Observability | `1ecccf40164c90a0e48e617914ea2b22e42bbeeae53835072ff2568842073c9e` |
| ArcForges.Observability.Desktop | `4c438de7a710b81e72a79208d1c7e215f5917ba0c4278077b1e94c58a20bbeed` |
| ArcForges.LocalRpc | `44bca5aff37dd65da3101979a074faa36c2be6ebf9c6ac6c845cbb4e54515ff4` |
| ArcForges.Contributions | `706aded9239c2d8384aee6709d48197caa1047282670b3ac363995aa0252cb21` |
| ArcForges.Security | `0087dd175142e768ab869f937fd72ea89986f8cbc64dc02fa824459d5c4106f0` |
| ArcForges.Security.Secrets | `f9b601d4cbba0bc9fded85823eda5a0a825397a5fe7332b743ebe6a35dbff37f` |
| ArcForges.Security.Audit | `0c73b07a3fc462cca264ba191650ca2e8bf26f2188b783bc5d19bd29a887d33c` |
| ArcForges.Security.LocalRpcBoundary | `d9caab975845b0e17bb0a24a5b93f5d813d7a682ae72e476ec5861019855c2ca` |
| ArcForges.Security.CapabilityEnforcement | `91a5e479b02edc3dcc08813781e5d1dd14c18819737d9a3969cf2df7528ced38` |
| ArcForges.ContentSandbox.Contracts | `a398e3f5d5e3be8fccf64e606f4ff5bb413a1928448f8d56a87342748425eb38` |
| ArcForges.ContentSandbox.Broker | `a5fd3aa8a4ea7f9ed0ecbcf7c58bfe89034d4d428d512e5accf832083a0009ce` |

## Obligations and deferred acceptance

The implementation delivers WP-13.10 production still-image decode and helper composition, retains the WP-13 cleanup/regression versus maintained production distinction, and preserves the major-type boundary: native generation handles/pointers remain private implementation state and never become managed domain IDs or wire fields. Applicable real component, error, cancellation, concurrency, lifecycle and source/admission/CI checks are recorded above. Image parsing types are internal and hostile product parsing routes through the existing ContentSandbox broker/helper boundary.

NAT.22 owns the complete portable Image producer/stager/contracts and actual built RID publication; NAT.25 owns authenticated native loader/publisher trust, Pdf runtime activation and signed production ContentSandbox Runtime composition. PLT.54 owns the combined actual packaged Image/Pdf containment diagnostics; PLT.45/46 and product integration own installed, all-RID and whole-series acceptance. NI's source/ordinary tests and actual win-x64 publication are delivered; Mac/Linux/ARM runtime execution, installed signed helper, hard OS isolation/resource enforcement, combined real parser acceptance and whole-series business-flow acceptance remain explicitly deferred to those owners. The planning graph currently lists no explicit NAT.11 completion prerequisite; that does not convert the unperformed task acceptance into proof. A future completion follow-up must append actual acceptance evidence, not merely upstream delivery status.

No substitute decoder or success stub remains in production Image composition. Scripted broker/parser fixtures and unavailable-OS opt-in skips remain diagnostic evidence only. No human-only blocker remains for this delivered Image implementation; unavailable actual native hosts or signing/runtime composition affect only their owned acceptance/delivery work and do not justify stopping independent implementation.
