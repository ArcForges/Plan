# ArcForges delivery task prompts — Native producers and probes

Generated from Design `docs/planning/delivery/delivery-graph.json` by `tools/delivery.py`; do not edit by hand.
Each block is self-contained. Claim a task only when `python tools/delivery.py ready` lists it, with
`python tools/delivery.py claim <TASK-ID> --worker <name>`, then follow `arcforges-implementation.md`.
Tasks are ordered by lane for reading; the order is not a schedule.

## Native producers and probes

```text
Execute ArcForges delivery task NAT.01 — Probe A: device tool execution under Native AOT.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\native.md (anchor task-nat-01).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/nat-01 (python tools/delivery.py claim NAT.01 --worker <name>); task branch task/nat-01 in DesktopPlatform; ledger record ledger/tasks/nat-01.md.
Kind/size: producer/M. Baseline: not-started.
Outcome: Inside a published Native AOT desktop binary, a stub ToolRequest is pulled, re-authorised locally, resolved through the generated allowlist to a CapabilityKey, decoded into a typed product request, invoked and returns an idempotent result -- with an AOT publish log showing zero diagnostics and a negative test proving no reflection-based registration/decode path compiles or exists.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-13.00 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\13-high-risk-technical-probes.md, anchor rule-wp-13.00
- WP-13:ss1-nd-05-probe-scaffolds-13-00-13-03-ar SS1/ND-05: probe scaffolds (13.00-13.03) are cleanup-or-regression-fixture; production 13.05-13.16 code is retained and maintained -- different lifecycle rules for the two groups even though both may live under similar directories (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\13-high-risk-technical-probes.md, package-level obligation

Entry condition: adoption slice ADOPT.02.native is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] PLT.18: generated CapabilityKey allowlist and static registration mechanism (Capabilities package)
- [artifact] PLT.09: local RPC structured-argument decode path (DP-02 boundary dispatch assembly)
- [artifact] PRF.04: a working pattern for AOT desktop <-> AOT desktop local RPC (from WP-06.01)
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:benchmarks/probes/agent-aot/**
Unblocks: APP.03, NAT.05, NAT.30

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): AOT publish log zero diagnostics; end-to-end ToolRequest->decode->typed invocation->result run inside the published binary; containment test confirming the structured value type appears only in the boundary dispatch assembly
Completion evidence for the ledger: AOT publish log and in-binary device tool request decode/execute trace; explicit note that the model loop itself is NOT probed here (it is the CF Workflow, LS-02/V-03)
Notes: One of WP13's two canonical early risk proofs (package goal: 'retire the early technical risks'). Parallel with NAT.03 (disjoint write scopes).
```

```text
Execute ArcForges delivery task NAT.03 — Probe C: high-throughput acquisition over a real transport.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\native.md (anchor task-nat-03).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/nat-03 (python tools/delivery.py claim NAT.03 --worker <name>); task branch task/nat-03 in DesktopPlatform; ledger record ledger/tasks/nat-03.md.
Kind/size: producer/M. Baseline: not-started.
Outcome: Sustained acquisition from a real transport (at least one real TCP/UDP/serial configuration, not an in-memory generator, per BR-06) runs above the intended product target through a ring buffer with responsive plot downsampling; overrun is counted and timestamped, pausing the view never stops recording, and disconnect leaves an explicit gap.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-13.02 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\13-high-risk-technical-probes.md, anchor rule-wp-13.02
- WP-13:ss1-nd-05-probe-scaffolds-13-00-13-03-ar SS1/ND-05: probe scaffolds (13.00-13.03) are cleanup-or-regression-fixture; production 13.05-13.16 code is retained and maintained -- different lifecycle rules for the two groups even though both may live under similar directories (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\13-high-risk-technical-probes.md, package-level obligation

Entry condition: adoption slice ADOPT.02.native is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- none
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:benchmarks/probes/acquisition/**; DesktopPlatform:eng/runtime_ownership.py (classify only the exact task-owned benchmarks/probes/acquisition/AcquisitionProbe.csproj path as test-or-build-tool); DesktopPlatform:eng/test_runtime_ownership.py (positive exact-path assertion and rejection fixtures for lookalike or any other benchmarks path)
Shared resources (follow the owner protocol): RES-desktopplatform-policy-data (append): Generated policy data is regenerated from its pinned source and never hand-edited; the reason-code registry is append-only with stable codes; each task adds its own test classes and evidence rows.
Unblocks: NAT.05, NAT.30

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Run a single-channel probe at 1,000,000 scalar samples/second over real localhost TCP sustained for at least 10 seconds using a fixed-capacity ring buffer; record achieved rate, buffer capacity/memory and drop/overrun counts. Also induce and record overrun, disconnect/gap and pause-while-recording behavior.
Completion evidence for the ledger: Sustained-throughput record with overrun/gap/pause results
Notes: No hard start-dependency on any other WP -- can begin immediately using a real TCP/UDP loopback or serial-over-USB pair; exotic hardware is not required for the first real-transport configuration. For this bounded probe, use one channel at 1,000,000 scalar samples/second over real localhost TCP for at least 10 seconds with a fixed-capacity ring buffer and record actual rate, memory/capacity and dropped/overrun samples. This probe-only measurement is not a shipping SLA, marketing claim or downstream performance target; existing overrun counting/timestamping, explicit disconnect gap, pause-with-recording and responsive plot-downsampling obligations remain unchanged. Parallel with NAT.01. The scoped runtime-ownership support admits only the full exact path benchmarks/probes/acquisition/AcquisitionProbe.csproj as test-or-build-tool, with a positive exact-path assertion and rejection of lookalike and other benchmarks paths. It does not authorize a general benchmarks prefix, another path exception, runtime/schema/security algorithm expansion, or any source outside eng/runtime_ownership.py and eng/test_runtime_ownership.py.
```

```text
Execute ArcForges delivery task NAT.05 — Probe evidence, licence positions, conclusions and hardware-lab inventory seed.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\native.md (anchor task-nat-05).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/nat-05 (python tools/delivery.py claim NAT.05 --worker <name>); task branch task/nat-05 in DesktopPlatform; ledger record ledger/tasks/nat-05.md.
Kind/size: producer/S. Baseline: not-started.
Outcome: Each of the two retained probes (A and C) has a written conclusion (proved / not proved / downstream constraint / open items); every native dependency the probes introduced has a recorded licence position; the tests/HardwareLab device inventory is created (device/firmware/driver versions) -- seeding PG-08 (completed later by NAT.28/WP-13.16).

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-13.04 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\13-high-risk-technical-probes.md, anchor rule-wp-13.04

Entry condition: adoption slice ADOPT.02.native is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] NAT.01: Probe A result
- [artifact] NAT.03: Probe C result
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:eng/verification/probe-evidence/**; DesktopPlatform:tests/HardwareLab/**
Unblocks: NAT.30

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Completeness check: every probe has a recorded environment, procedure, result and conclusion
Completion evidence for the ledger: Two written probe conclusions; licence positions for probe-introduced dependencies; hardware inventory shell
Notes: Small synthesis task; not itself a risk probe.
```

```text
Execute ArcForges delivery task NAT.06 — Common native ABI: preambles, pack8 records, ownership, cancellation, bounded buffers.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\native.md (anchor task-nat-06).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/nat-06 (python tools/delivery.py claim NAT.06 --worker <name>); task branch task/nat-06 in DesktopPlatform; ledger record ledger/tasks/nat-06.md.
Kind/size: producer/L. Baseline: not-started.
Outcome: annex-06 common preambles, fixed numeric keys, pack8 records, ownership/cancellation/bounded-buffer helpers compile as C17/C++20 headers and C# layouts for the retained still-image, instrument and PDF families; every field offset and all 17 normative sizes are asserted; wrong-size/version/null/closed-handle cases and zero-leaked-output-on-failure are proven. ArcForges.Native.Abstractions managed package (status/handle types only) is published. The existing arc_image_* probe-library identity is retained unchanged; retired families are removed by GOV.17 before this task starts.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-13.05 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\13-high-risk-technical-probes.md, anchor rule-wp-13.05
- WP-13:ss1-nd-05-probe-scaffolds-13-00-13-03-ar SS1/ND-05: probe scaffolds (13.00-13.03) are cleanup-or-regression-fixture; production 13.05-13.16 code is retained and maintained -- different lifecycle rules for the two groups even though both may live under similar directories (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\13-high-risk-technical-probes.md, package-level obligation
- WP-13:ss4-major-types-note-no-native-pointer-b SS4 major-types note: no native pointer becomes a managed domain identifier or a wire field (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\13-high-risk-technical-probes.md, package-level obligation

Entry condition: adoption slice ADOPT.02.native is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] GOV.17: retired native families removed and the still-image shim moved
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:native/shared/**; DesktopPlatform:native/CMakeLists.txt (register only the exact NAT.06 C17/C++20 common-ABI test targets below); DesktopPlatform:native/shared/tests/arc_native_abi_c17_layout.c (retained shim-static test source only; CTest target arc_native_abi_c17_layout_tests); DesktopPlatform:native/shared/tests/arc_native_abi_cpp20_tests.cpp (retained shim-static test source only; target arc_native_abi_cpp20_tests); DesktopPlatform:native/*/include/arc/**; DesktopPlatform:src/Native/ArcForges.Native.Abstractions/**; DesktopPlatform:tests/NativeAbiTests/ArcForges.Tests.NativeAbiTests.csproj (add only a ProjectReference to the existing Native.Abstractions project; no PackageReference); DesktopPlatform:tests/NativeAbiTests/CommonAbiLayoutTests.cs (existing Windows x64 test project only); DesktopPlatform:.github/workflows/native-abi.yml (on Windows x64 run only the two exact CTest targets and `dotnet test tests/NativeAbiTests/ArcForges.Tests.NativeAbiTests.csproj --filter Category=NativeAbiLayout --no-restore`; this filter runs only common-layout tests and excludes the existing image runtime smoke); DesktopPlatform:eng/provenance/files.json (append only the three exact new test-source rows above)
Shared resources (follow the owner protocol): RES-desktopplatform-package-inventory (append): Each producer task adds its own package entry; every merge to main packs and publishes all packages at one version; consumers pin the candidate produced by the merge of the capability they need, never waiting for a package closure task; one merge queue.; RES-desktopplatform-native-build (append): The vcpkg baseline and overlay ports change only through a dependency-admission change with licence and provenance receipts; each native family adds its own CMake targets and workflow entries; triplet or port changes are rebased and rebuilt by their author; CPU-heavy native builds use the workstation build slot. PLT.39 may append only a narrowly scoped transport compatibility change to eng/native_provenance.py and offline tests in tests/tooling/test_native_provenance.py: after the verified cache-hit path, pass urllib.request.Request(url, headers={"User-Agent": "ArcForges/1.0 (+https://github.com/ArcForges/DesktopPlatform)"}) only when the complete requested URL equals https://visualstudio.microsoft.com/wp-content/uploads/2025/10/Visual_Studio_2026-License-Community_ENU.docx or https://visualstudio.microsoft.com/wp-content/uploads/2025/10/Visual-C-V14-License-Redistributable_and_Runtime_ENU.docx; preserve all other URL behavior, pinned URLs/hashes, TLS, timeout, redirects, cache, digest verification, temporary cleanup and atomic promotion, with no retries, dependency, workflow or runner changes. The DesktopPlatform integration owner serializes this shared helper append.; RES-desktopplatform-policy-data (append): Generated policy data is regenerated from its pinned source and never hand-edited; the reason-code registry is append-only with stable codes; each task adds its own test classes and evidence rows.; RES-workstation-build-slot (exclusive): Exclusive per workstation for the duration of each CPU-heavy local build or test, through the workstation lock rather than a Plan lease: run the command as `python tools/delivery.py build-slot run --worker <name> --task <task> -- <command>` with the Plan repository tool, which holds the lock directory `.arcforges/build-slot` in the user profile with an owner record and heartbeat and recovers a lock whose holder stopped. Coding and review continue while a build waits; CI capacity is not limited by this rule.
Unblocks: NAT.11, NAT.13, NAT.14, NAT.30

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): On the admitted RIDs compile the common headers and run only CTest targets arc_native_abi_c17_layout_tests (C17) and arc_native_abi_cpp20_tests (C++20), both retained shim-static; on Windows x64 run only `dotnet test tests/NativeAbiTests/ArcForges.Tests.NativeAbiTests.csproj --filter Category=NativeAbiLayout --no-restore`, excluding the existing image runtime smoke. Assert all field offsets and 17 normative sizes, wrong-size/version/null/closed-handle failures, and zero outputs on failure.
Completion evidence for the ledger: Common ABI and deterministic failure surface: behavioral, failure and package evidence
Notes: Hard prerequisite for NAT.11, NAT.13 and NAT.14 (artifact edges from each). NAT.06 alone registers native/shared/tests/arc_native_abi_c17_layout.c as CTest target arc_native_abi_c17_layout_tests and native/shared/tests/arc_native_abi_cpp20_tests.cpp as target arc_native_abi_cpp20_tests in native/CMakeLists.txt; both tests and targets are retained shim-static only. The existing tests/NativeAbiTests/ArcForges.Tests.NativeAbiTests.csproj gains only a ProjectReference to the existing Native.Abstractions project; CommonAbiLayoutTests.cs uses that project. On Windows x64 native-abi.yml runs only `dotnet test tests/NativeAbiTests/ArcForges.Tests.NativeAbiTests.csproj --filter Category=NativeAbiLayout --no-restore`, so the existing image runtime smoke is excluded. Do not create a project, add a PackageReference or change package identity, or authorize other workflow behavior. Append only these three new test-source rows to eng/provenance/files.json. Preserve the 17 normative size/offset checks and wrong-size, version, null, closed-handle, and zero-output-on-failure cases. No native family implementation, library identity, package identity or dependency expansion is authorized; runtime/policy input binding changes are limited to exact ADP-07 current rows necessary for these files.
```

```text
Execute ArcForges delivery task NAT.11 — Image family: still-image codecs (PNG/TIFF/EXR).

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\native.md (anchor task-nat-11).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/nat-11 (python tools/delivery.py claim NAT.11 --worker <name>); task branch task/nat-11 in DesktopPlatform; ledger record ledger/tasks/nat-11.md.
Kind/size: producer/M. Baseline: not-started.
Outcome: arc_image_* implemented with PNG/TIFF/EXR metadata and bounded tile reads via OIIO/OpenEXR/Imath; hostile reads execute only in the WP11 helper.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-13.10 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\13-high-risk-technical-probes.md, anchor rule-wp-13.10
- WP-13:ss1-nd-05-probe-scaffolds-13-00-13-03-ar SS1/ND-05: probe scaffolds (13.00-13.03) are cleanup-or-regression-fixture; production 13.05-13.16 code is retained and maintained -- different lifecycle rules for the two groups even though both may live under similar directories (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\13-high-risk-technical-probes.md, package-level obligation
- WP-13:ss4-major-types-note-no-native-pointer-b SS4 major-types note: no native pointer becomes a managed domain identifier or a wire field (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\13-high-risk-technical-probes.md, package-level obligation

Entry condition: adoption slice ADOPT.02.native is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] NAT.06: compiled common ABI headers/layouts (arc_image_options_v1, arc_region_v1)
- [artifact] PLT.45: published ContentSandbox.Contracts/Broker/foundation Runtime.<rid>
- [artifact] GOV.17: the still-image shim at native/arcimage-abi under the ArcImageNative logical library
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:native/arcimage-abi/**; DesktopPlatform:src/Native/ArcForges.Native.Image/**
Shared resources (follow the owner protocol): RES-desktopplatform-native-build (append): The vcpkg baseline and overlay ports change only through a dependency-admission change with licence and provenance receipts; each native family adds its own CMake targets and workflow entries; triplet or port changes are rebased and rebuilt by their author; CPU-heavy native builds use the workstation build slot. PLT.39 may append only a narrowly scoped transport compatibility change to eng/native_provenance.py and offline tests in tests/tooling/test_native_provenance.py: after the verified cache-hit path, pass urllib.request.Request(url, headers={"User-Agent": "ArcForges/1.0 (+https://github.com/ArcForges/DesktopPlatform)"}) only when the complete requested URL equals https://visualstudio.microsoft.com/wp-content/uploads/2025/10/Visual_Studio_2026-License-Community_ENU.docx or https://visualstudio.microsoft.com/wp-content/uploads/2025/10/Visual-C-V14-License-Redistributable_and_Runtime_ENU.docx; preserve all other URL behavior, pinned URLs/hashes, TLS, timeout, redirects, cache, digest verification, temporary cleanup and atomic promotion, with no retries, dependency, workflow or runner changes. The DesktopPlatform integration owner serializes this shared helper append.; RES-workstation-build-slot (exclusive): Exclusive per workstation for the duration of each CPU-heavy local build or test, through the workstation lock rather than a Plan lease: run the command as `python tools/delivery.py build-slot run --worker <name> --task <task> -- <command>` with the Plan repository tool, which holds the lock directory `.arcforges/build-slot` in the user profile with an owner record and heartbeat and recovers a lock whose holder stopped. Coding and review continue while a build waits; CI capacity is not limited by this rule.
Unblocks: NAT.22, NAT.30

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Bit depth/metadata round trip, edge tiles, decompression bomb, failed codec, incomplete-output refusal
Completion evidence for the ledger: Still-image codecs: behavioral, failure and package evidence
Notes: Consumed by the assistant image previews through the ContentSandbox per the platform matrix SS3.2 slot table.
```

```text
Execute ArcForges delivery task NAT.13 — Instruments family: serial and USB devices (NEW library).

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\native.md (anchor task-nat-13).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/nat-13 (python tools/delivery.py claim NAT.13 --worker <name>); task branch task/nat-13 in DesktopPlatform; ledger record ledger/tasks/nat-13.md.
Kind/size: producer/M. Baseline: not-started.
Outcome: A new arcinstruments-abi native library and ArcForges.Native.Instruments managed package implement arc_instruments_* over generic OS serial and explicit libusb interface/endpoint open/read/write/cancel/close; identity revalidated at open; no auto-detach of unrelated drivers, no vendor SDK.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-13.12 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\13-high-risk-technical-probes.md, anchor rule-wp-13.12
- WP-13:ss1-nd-05-probe-scaffolds-13-00-13-03-ar SS1/ND-05: probe scaffolds (13.00-13.03) are cleanup-or-regression-fixture; production 13.05-13.16 code is retained and maintained -- different lifecycle rules for the two groups even though both may live under similar directories (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\13-high-risk-technical-probes.md, package-level obligation
- WP-13:ss4-major-types-note-no-native-pointer-b SS4 major-types note: no native pointer becomes a managed domain identifier or a wire field (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\13-high-risk-technical-probes.md, package-level obligation

Entry condition: adoption slice ADOPT.02.native is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] NAT.06: compiled common ABI headers/layouts (arc_instrument_options_v1, arc_transfer_v1)
- [artifact] GOV.17: retired native families removed and the still-image shim moved
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:native/arcinstruments-abi/**; DesktopPlatform:src/Native/ArcForges.Native.Instruments/**; DesktopPlatform:native/CMakeLists.txt; DesktopPlatform:eng/packaging/packages.json
Shared resources (follow the owner protocol): RES-desktopplatform-native-build (append): The vcpkg baseline and overlay ports change only through a dependency-admission change with licence and provenance receipts; each native family adds its own CMake targets and workflow entries; triplet or port changes are rebased and rebuilt by their author; CPU-heavy native builds use the workstation build slot. PLT.39 may append only a narrowly scoped transport compatibility change to eng/native_provenance.py and offline tests in tests/tooling/test_native_provenance.py: after the verified cache-hit path, pass urllib.request.Request(url, headers={"User-Agent": "ArcForges/1.0 (+https://github.com/ArcForges/DesktopPlatform)"}) only when the complete requested URL equals https://visualstudio.microsoft.com/wp-content/uploads/2025/10/Visual_Studio_2026-License-Community_ENU.docx or https://visualstudio.microsoft.com/wp-content/uploads/2025/10/Visual-C-V14-License-Redistributable_and_Runtime_ENU.docx; preserve all other URL behavior, pinned URLs/hashes, TLS, timeout, redirects, cache, digest verification, temporary cleanup and atomic promotion, with no retries, dependency, workflow or runner changes. The DesktopPlatform integration owner serializes this shared helper append.; RES-desktopplatform-package-inventory (append): Each producer task adds its own package entry; every merge to main packs and publishes all packages at one version; consumers pin the candidate produced by the merge of the capability they need, never waiting for a package closure task; one merge queue.; RES-workstation-build-slot (exclusive): Exclusive per workstation for the duration of each CPU-heavy local build or test, through the workstation lock rather than a Plan lease: run the command as `python tools/delivery.py build-slot run --worker <name> --task <task> -- <command>` with the Plan repository tool, which holds the lock directory `.arcforges/build-slot` in the user profile with an owner record and heartbeat and recovers a lock whose holder stopped. Coding and review continue while a build waits; CI capacity is not limited by this rule.
Unblocks: NAT.24, NAT.30, SCOPE.04

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Enumeration, explicit interface claim, control/bulk/interrupt transfers, partial writes, cancellation callback, hot unplug, driver absence, permission denial on Tier 1 -- against the PG-08 hardware inventory for the physical-device cases
Completion evidence for the ledger: Serial and USB instruments: behavioral, failure and package evidence
Notes: Degradation-path code (enumeration, driver-absence reporting) does not require the PG-08 lab to exist; the physical hot-unplug/permission-denial matrix against a named USB device does..
```

```text
Execute ArcForges delivery task NAT.14 — Pdf family: arcpdf-abi export set, ArcForges.Native.Pdf binding and production parser composition seam in the WP11 helper (NEW library; real PDFium is NAT.15).

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\native.md (anchor task-nat-14).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/nat-14 (python tools/delivery.py claim NAT.14 --worker <name>); task branch task/nat-14 in DesktopPlatform; ledger record ledger/tasks/nat-14.md.
Kind/size: producer/L. Baseline: not-started.
Outcome: A new arcpdf-abi native library implements the complete arc_pdf_* export set (open, page_info, render, text, close) with the handle table, limits, cancellation, bounded buffers and text/geometry encoding over a PDF-backend interface; the non-packable ArcForges.Native.Pdf managed binding is added (it is not packable until NAT.25 and NAT.15 admit it); and the production parser composition is added to the existing WP-11.09 ContentSandbox host using generated local gRPC controls (no second helper, no duplicate DTO owner): a PDF parser wrapper over arc_pdf_*, the production parser profile registered, the native library pre-loaded before the OS profile is applied, hostile-PDF failure, limits and containment tests against a test-only fake PDF backend, test-parser production registration removed and the hostile regression fixture retained. The real PDFium (chromium/8044) backend is NOT part of this task: the fake backend is test-only and must never be registered in a release composition, and no ContentSandbox.Runtime.<rid> version is published here. The real PDFium build and binding, real-parser containment acceptance and the next immutable ContentSandbox.Runtime.<rid> input are NAT.15.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-13.13 (composition, interfaces, limits and fake-backend containment tests; excludes the real PDFium build/binding and real-parser containment acceptance (NAT.15) and the parts mapped to PLT.54): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\13-high-risk-technical-probes.md, anchor rule-wp-13.13
- WP-13:ss1-nd-05-probe-scaffolds-13-00-13-03-ar SS1/ND-05: probe scaffolds (13.00-13.03) are cleanup-or-regression-fixture; production 13.05-13.16 code is retained and maintained -- different lifecycle rules for the two groups even though both may live under similar directories (package-level obligation contribution (interface-level part: probe scaffolds retired or kept as regression fixtures for the PDF family seam; the real-library part is NAT.15)): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\13-high-risk-technical-probes.md, package-level obligation
- WP-13:ss4-major-types-note-no-native-pointer-b SS4 major-types note: no native pointer becomes a managed domain identifier or a wire field (package-level obligation contribution (interface-level part: major-types note and no native pointer crossing the ABI for the PDF family; the real-library part is NAT.15)): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\13-high-risk-technical-probes.md, package-level obligation

Entry condition: adoption slice ADOPT.02.native is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] PLT.45: published ArcForges.ContentSandbox.Contracts,.Broker and the foundation Runtime.<rid> package (built around a deliberately hostile first-party TEST parser)
- [artifact] NAT.06: compiled common ABI headers/layouts (arc_pdf_page_v1)
- [artifact] GOV.17: retired native families removed and the still-image shim moved
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:native/arcpdf-abi/**; DesktopPlatform:src/Native/ArcForges.Native.Pdf/**; DesktopPlatform:src/DesktopHelpers/ArcForges.ContentSandbox/**; DesktopPlatform:native/CMakeLists.txt; DesktopPlatform:.github/workflows/native-abi.yml (extend only the CTest -R filter with the NAT.14 arcpdf test targets arcpdf_abi_engine_tests and arcpdf_abi_unsupported_tests; no other workflow behavior); DesktopPlatform:eng/provenance/files.json (append only rows for the new NAT.14 source files)
Shared resources (follow the owner protocol): RES-desktopplatform-native-build (append): The vcpkg baseline and overlay ports change only through a dependency-admission change with licence and provenance receipts; each native family adds its own CMake targets and workflow entries; triplet or port changes are rebased and rebuilt by their author; CPU-heavy native builds use the workstation build slot. PLT.39 may append only a narrowly scoped transport compatibility change to eng/native_provenance.py and offline tests in tests/tooling/test_native_provenance.py: after the verified cache-hit path, pass urllib.request.Request(url, headers={"User-Agent": "ArcForges/1.0 (+https://github.com/ArcForges/DesktopPlatform)"}) only when the complete requested URL equals https://visualstudio.microsoft.com/wp-content/uploads/2025/10/Visual_Studio_2026-License-Community_ENU.docx or https://visualstudio.microsoft.com/wp-content/uploads/2025/10/Visual-C-V14-License-Redistributable_and_Runtime_ENU.docx; preserve all other URL behavior, pinned URLs/hashes, TLS, timeout, redirects, cache, digest verification, temporary cleanup and atomic promotion, with no retries, dependency, workflow or runner changes. The DesktopPlatform integration owner serializes this shared helper append.; RES-workstation-build-slot (exclusive): Exclusive per workstation for the duration of each CPU-heavy local build or test, through the workstation lock rather than a Plan lease: run the command as `python tools/delivery.py build-slot run --worker <name> --task <task> -- <command>` with the Plan repository tool, which holds the lock directory `.arcforges/build-slot` in the user profile with an owner record and heartbeat and recovers a lock whose holder stopped. Coding and review continue while a build waits; CI capacity is not limited by this rule.; RES-desktopplatform-policy-data (append): Generated policy data is regenerated from its pinned source and never hand-edited; the reason-code registry is append-only with stable codes; each task adds its own test classes and evidence rows.
Permitted substitutes (never real integration evidence): SUB-hostile-test-parser: OS-level containment mechanics only (AppContainer/Job Object, Landlock/seccomp, App-Sandbox/XPC denial, resource bounds, crash/hang/parent-death cleanup) against a deliberately hostile FIRST-PARTY test parser, not real format-parsing correctness Real producer ['NAT.15']; removed by PLT.54
Unblocks: NAT.15, NAT.30

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline unit and ABI tests for every arc_pdf_* export (handle table, limits, cancellation, bounded buffers, text/geometry encoding, malformed arguments) and Windows/Linux compilation; hostile-PDF failure, limit and containment tests through the production parser composition against the test-only fake backend, including a check that the fake backend and the test parser are not registered in a production composition; no real PDFium, packaged-RID containment or native-crash evidence is claimed here (NAT.15).
Completion evidence for the ledger: arcpdf-abi export-set, ABI-layout and limit test results; the PDF parser composition in the ContentSandbox host with fake-backend failure/limit/containment test results and the production-registration negative test; explicit statement that the real PDFium dependency, PG-12 real-library evidence and PG-22 real-parser runtime evidence are NAT.15, not this task.
Notes: Planning repair (split of NAT.14, claim NAT.14 epoch 1): architecture/01 builds PDFium from verified chromium/8044 source in a Platform isolated profile, but DesktopPlatform has no PDFium source, binary or dependency-admission receipt, no vcpkg port exists and policy forbids public downloads and toolchain installs, so the real library cannot be obtained by any admitted path. This task keeps everything deliverable without it: the complete arc_pdf_* export set over a PDF-backend interface, the non-packable ArcForges.Native.Pdf binding, and the production parser composition in the existing WP-11.09 ContentSandbox host with hostile-PDF failure, limit and containment tests against a test-only fake backend. The fake backend is test-only and is never registered in a release composition (a test asserts this); the production parser profile registers the arc_pdf_* wrapper only. This task adds no package inventory entry (eng/packaging/packages.json waits for a real PDFium, NAT.15/NAT.25) and publishes no ContentSandbox.Runtime.<rid> version. Delivering this task does not satisfy PG-12/PG-22 real-parser evidence: NAT.15 (real PDFium admission, binding and containment acceptance) and then PLT.54 and NAT.25 follow. Hard prerequisite for NAT.15. Layout and bindings: the helper and test code lives under src/DesktopHelpers/ArcForges.ContentSandbox/** and src/Native/ArcForges.Native.Pdf/** (tests/** is not added to the write scope). The one-line InternalsVisibleTo(ArcForges.Native.Pdf) in src/Native/ArcForges.Native.Abstractions/NativeAbi.cs is added as an ADP-07 supporting binding, recorded here and not a widening of the write scope. CI wiring is limited to extending the CTest -R filter in native-abi.yml with arcpdf_abi_engine_tests and arcpdf_abi_unsupported_tests, and provenance is limited to files.json rows for the new source files.
```

```text
Execute ArcForges delivery task NAT.15 — Pdf family: real PDFium (chromium/8044) build admission, binding and real-parser containment acceptance.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\native.md (anchor task-nat-15).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/nat-15 (python tools/delivery.py claim NAT.15 --worker <name>); task branch task/nat-15 in DesktopPlatform; ledger record ledger/tasks/nat-15.md.
Kind/size: producer/L. Baseline: not-started.
Outcome: PDFium built from verified chromium/8044 source (or an equivalently admitted build provenance) in a Platform isolated profile, admitted through the DesktopPlatform dependency admission (provenance, licence and SBOM receipts) and bound behind the arc_pdf_* backend interface delivered by NAT.14, replacing the test-only fake backend; ArcForges.Native.Pdf and the PDF parser composition in the existing WP-11.09 ContentSandbox host run over actual PDFium (no second helper, no duplicate DTO owner); the packaged PDF page/text/tile fixtures, malformed, native-crash, hang and parent-death cleanup cases pass against the real library on every admitted RID; the actual image-parser containment is rerun; and the composition input for the next immutable ContentSandbox.Runtime.<rid> version is produced (published by NAT.25). Contributes real evidence to PG-12 and PG-22.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-13.13 (the real PDFium (chromium/8044) build and binding, the packaged PDF page/text/tile fixtures, malformed/native-crash/hang and parent-death cleanup against the real library on every admitted RID, rerun of the actual image-parser containment, and the next immutable ContentSandbox.Runtime.<rid> composition input; the composition, interfaces, limits and fake-backend tests are NAT.14): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\13-high-risk-technical-probes.md, anchor rule-wp-13.13
- WP-13:ss1-nd-05-probe-scaffolds-13-00-13-03-ar SS1/ND-05: probe scaffolds (13.00-13.03) are cleanup-or-regression-fixture; production 13.05-13.16 code is retained and maintained -- different lifecycle rules for the two groups even though both may live under similar directories (package-level obligation contribution (real-library part: probe scaffolds retired against the real PDFium build; the interface-level part is NAT.14)): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\13-high-risk-technical-probes.md, package-level obligation
- WP-13:ss4-major-types-note-no-native-pointer-b SS4 major-types note: no native pointer becomes a managed domain identifier or a wire field (package-level obligation contribution (real-library part: major-types note verified against the real PDFium binding; the interface-level part is NAT.14)): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\13-high-risk-technical-probes.md, package-level obligation

Entry condition: adoption slice ADOPT.02.native is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] NAT.14: arc_pdf_* export set over the PDF-backend interface, the non-packable ArcForges.Native.Pdf binding and the production parser composition seam in the ContentSandbox host
- [artifact] PLT.45: published ArcForges.ContentSandbox.Contracts,.Broker and the foundation Runtime.<rid> package (built around a deliberately hostile first-party TEST parser)
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:native/arcpdf-abi/**; DesktopPlatform:src/Native/ArcForges.Native.Pdf/**; DesktopPlatform:src/DesktopHelpers/ArcForges.ContentSandbox/**; DesktopPlatform:native/CMakeLists.txt; DesktopPlatform:eng/packaging/packages.json; DesktopPlatform:eng/native/vcpkg/** (only the PDFium admission inputs: overlay port or build profile and triplet entries for the chromium/8044 build); DesktopPlatform:eng/provenance/** (only the PDFium source/build provenance records, artifact-profile successor and files.json rows); DesktopPlatform:eng/policy/dependency-policy.json (only the PDFium admission entry and the exact input hashes it refreshes; point reviewReceipt to the NAT.15 successor); DesktopPlatform:eng/policy/dependency-reviews/** (only the new immutable NAT.15 receipt successor chained from the receipt active on main at merge); DesktopPlatform:third-party/** (only the PDFium licence and notice texts); DesktopPlatform:eng/native_provenance.py (only the changes the PDFium build inputs require); DesktopPlatform:eng/test_native_provenance.py (matching tests for the native_provenance.py change)
Shared resources (follow the owner protocol): RES-desktopplatform-native-build (append): The vcpkg baseline and overlay ports change only through a dependency-admission change with licence and provenance receipts; each native family adds its own CMake targets and workflow entries; triplet or port changes are rebased and rebuilt by their author; CPU-heavy native builds use the workstation build slot. PLT.39 may append only a narrowly scoped transport compatibility change to eng/native_provenance.py and offline tests in tests/tooling/test_native_provenance.py: after the verified cache-hit path, pass urllib.request.Request(url, headers={"User-Agent": "ArcForges/1.0 (+https://github.com/ArcForges/DesktopPlatform)"}) only when the complete requested URL equals https://visualstudio.microsoft.com/wp-content/uploads/2025/10/Visual_Studio_2026-License-Community_ENU.docx or https://visualstudio.microsoft.com/wp-content/uploads/2025/10/Visual-C-V14-License-Redistributable_and_Runtime_ENU.docx; preserve all other URL behavior, pinned URLs/hashes, TLS, timeout, redirects, cache, digest verification, temporary cleanup and atomic promotion, with no retries, dependency, workflow or runner changes. The DesktopPlatform integration owner serializes this shared helper append.; RES-desktopplatform-package-inventory (append): Each producer task adds its own package entry; every merge to main packs and publishes all packages at one version; consumers pin the candidate produced by the merge of the capability they need, never waiting for a package closure task; one merge queue.; RES-desktopplatform-policy-data (append): Generated policy data is regenerated from its pinned source and never hand-edited; the reason-code registry is append-only with stable codes; each task adds its own test classes and evidence rows.; RES-workstation-build-slot (exclusive): Exclusive per workstation for the duration of each CPU-heavy local build or test, through the workstation lock rather than a Plan lease: run the command as `python tools/delivery.py build-slot run --worker <name> --task <task> -- <command>` with the Plan repository tool, which holds the lock directory `.arcforges/build-slot` in the user profile with an owner record and heartbeat and recovers a lock whose holder stopped. Coding and review continue while a build waits; CI capacity is not limited by this rule.
Permitted substitutes (never real integration evidence): SUB-hostile-test-parser: OS-level containment mechanics only (AppContainer/Job Object, Landlock/seccomp, App-Sandbox/XPC denial, resource bounds, crash/hang/parent-death cleanup) against a deliberately hostile FIRST-PARTY test parser, not real format-parsing correctness Real producer ['NAT.15']; removed by PLT.54
Unblocks: NAT.25, NAT.30, PLT.45, PLT.54

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Packaged PDF page/text/tile fixtures, malformed/native-crash/hang and parent-death cleanup against the real PDFium library on every admitted RID; rerun of actual image parser containment (not just PDF); the dependency-admission, provenance and licence checks for the PDFium build run in CI as offline/static checks (no public download or toolchain install in CI or locally beyond what the admission records); no real-library evidence is claimed for a RID that was not run.
Completion evidence for the ledger: Actual PDF dependency and containment evidence contributing to PG-12; PG-22 runtime evidence for the real-parser leg (11.09 supplies the mechanism leg); PDFium admission receipts (source/build provenance, licence, SBOM).
Notes: Created by the planning repair that split NAT.14 (claim NAT.14 epoch 1). Blocking prerequisite: an admitted way to obtain and build PDFium chromium/8044 here -- verified source or build provenance, licence and SBOM receipts, and a build toolchain -- which is a Platform dependency admission change (Design architecture/01 requires verified chromium/8044 source built in a Platform isolated profile; policy forbids public downloads and toolchain installs outside admitted paths). Until that admission exists this task cannot start in practice and must be recorded blocked with that exact missing input rather than satisfied with the fake backend; the fake backend from NAT.14 is test-only and must never be registered in a release composition. Highest residual security-relevant risk of the seven native families (hostile content inside a real isolation boundary) -- flagged as an early risk proof even though it is scheduled after NAT.06. This task owns the real-library PDF obligations of WP-13.13 and the real-library halves of the two WP-13 package-level contributions that NAT.14 carries at interface level; PLT.54 re-verifies the containment mechanics against the real parser closure and NAT.25 packages it. No ContentSandbox.Runtime.<rid> is published here; NAT.25 publishes the next immutable version from this composition input.
```

```text
Execute ArcForges delivery task NAT.22 — Image package production: all 6 RIDs.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\native.md (anchor task-nat-22).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/nat-22 (python tools/delivery.py claim NAT.22 --worker <name>); task branch task/nat-22 in DesktopPlatform; ledger record ledger/tasks/nat-22.md.
Kind/size: producer/S. Baseline: not-started.
Outcome: ArcForges.Native.Image.Runtime.<rid> published for all 6 RIDs with matched tested bytes/headers/manifests/dependency closures.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-13.15 (ArcForges.Native.Image + Runtime.<rid> only): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\13-high-risk-technical-probes.md, anchor rule-wp-13.15
- WP-13:producer-artifacts-and-integration-md-wp producer-artifacts-and-integration.md WP13 row: 'Probe-only 1.0, missing functional export or dependency prevents completion' (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\13-high-risk-technical-probes.md, package-level obligation

Entry condition: adoption slice ADOPT.02.native is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] NAT.11: complete arc_image_* export set
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:src/Native/ArcForges.Native.Image.Runtime.win-arm64/**; DesktopPlatform:src/Native/ArcForges.Native.Image.Runtime.osx-arm64/**; DesktopPlatform:src/Native/ArcForges.Native.Image.Runtime.osx-x64/**; DesktopPlatform:src/Native/ArcForges.Native.Image.Runtime.linux-x64/**; DesktopPlatform:src/Native/ArcForges.Native.Image.Runtime.linux-arm64/**; DesktopPlatform:eng/packaging/packages.json
Shared resources (follow the owner protocol): RES-desktopplatform-native-build (append): The vcpkg baseline and overlay ports change only through a dependency-admission change with licence and provenance receipts; each native family adds its own CMake targets and workflow entries; triplet or port changes are rebased and rebuilt by their author; CPU-heavy native builds use the workstation build slot. PLT.39 may append only a narrowly scoped transport compatibility change to eng/native_provenance.py and offline tests in tests/tooling/test_native_provenance.py: after the verified cache-hit path, pass urllib.request.Request(url, headers={"User-Agent": "ArcForges/1.0 (+https://github.com/ArcForges/DesktopPlatform)"}) only when the complete requested URL equals https://visualstudio.microsoft.com/wp-content/uploads/2025/10/Visual_Studio_2026-License-Community_ENU.docx or https://visualstudio.microsoft.com/wp-content/uploads/2025/10/Visual-C-V14-License-Redistributable_and_Runtime_ENU.docx; preserve all other URL behavior, pinned URLs/hashes, TLS, timeout, redirects, cache, digest verification, temporary cleanup and atomic promotion, with no retries, dependency, workflow or runner changes. The DesktopPlatform integration owner serializes this shared helper append.; RES-desktopplatform-package-inventory (append): Each producer task adds its own package entry; every merge to main packs and publishes all packages at one version; consumers pin the candidate produced by the merge of the capability they need, never waiting for a package closure task; one merge queue.; RES-workstation-build-slot (exclusive): Exclusive per workstation for the duration of each CPU-heavy local build or test, through the workstation lock rather than a Plan lease: run the command as `python tools/delivery.py build-slot run --worker <name> --task <task> -- <command>` with the Plan repository tool, which holds the lock directory `.arcforges/build-slot` in the user profile with an owner record and heartbeat and recovers a lock whose holder stopped. Coding and review continue while a build waits; CI capacity is not limited by this rule.
Unblocks: NAT.28, NAT.30

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Clean-cache C17/C# AOT consumers per RID; missing/transitive/wrong-RID library, hash collision, absent export, revoked artifact, source-unavailable negatives
Completion evidence for the ledger: Immutable native package production: behavioral, failure and package evidence (Image slice)
Notes: Independent of the other packaging tasks.
```

```text
Execute ArcForges delivery task NAT.24 — Instruments package production: all 6 RIDs.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\native.md (anchor task-nat-24).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/nat-24 (python tools/delivery.py claim NAT.24 --worker <name>); task branch task/nat-24 in DesktopPlatform; ledger record ledger/tasks/nat-24.md.
Kind/size: producer/S. Baseline: not-started.
Outcome: ArcForges.Native.Instruments.Runtime.<rid> published for all 6 RIDs.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-13.15 (ArcForges.Native.Instruments + Runtime.<rid> only): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\13-high-risk-technical-probes.md, anchor rule-wp-13.15
- WP-13:producer-artifacts-and-integration-md-wp producer-artifacts-and-integration.md WP13 row: 'Probe-only 1.0, missing functional export or dependency prevents completion' (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\13-high-risk-technical-probes.md, package-level obligation

Entry condition: adoption slice ADOPT.02.native is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] NAT.13: complete arc_instruments_* export set
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:src/Native/ArcForges.Native.Instruments.Runtime.*/**; DesktopPlatform:eng/packaging/packages.json
Shared resources (follow the owner protocol): RES-desktopplatform-native-build (append): The vcpkg baseline and overlay ports change only through a dependency-admission change with licence and provenance receipts; each native family adds its own CMake targets and workflow entries; triplet or port changes are rebased and rebuilt by their author; CPU-heavy native builds use the workstation build slot. PLT.39 may append only a narrowly scoped transport compatibility change to eng/native_provenance.py and offline tests in tests/tooling/test_native_provenance.py: after the verified cache-hit path, pass urllib.request.Request(url, headers={"User-Agent": "ArcForges/1.0 (+https://github.com/ArcForges/DesktopPlatform)"}) only when the complete requested URL equals https://visualstudio.microsoft.com/wp-content/uploads/2025/10/Visual_Studio_2026-License-Community_ENU.docx or https://visualstudio.microsoft.com/wp-content/uploads/2025/10/Visual-C-V14-License-Redistributable_and_Runtime_ENU.docx; preserve all other URL behavior, pinned URLs/hashes, TLS, timeout, redirects, cache, digest verification, temporary cleanup and atomic promotion, with no retries, dependency, workflow or runner changes. The DesktopPlatform integration owner serializes this shared helper append.; RES-desktopplatform-package-inventory (append): Each producer task adds its own package entry; every merge to main packs and publishes all packages at one version; consumers pin the candidate produced by the merge of the capability they need, never waiting for a package closure task; one merge queue.; RES-workstation-build-slot (exclusive): Exclusive per workstation for the duration of each CPU-heavy local build or test, through the workstation lock rather than a Plan lease: run the command as `python tools/delivery.py build-slot run --worker <name> --task <task> -- <command>` with the Plan repository tool, which holds the lock directory `.arcforges/build-slot` in the user profile with an owner record and heartbeat and recovers a lock whose holder stopped. Coding and review continue while a build waits; CI capacity is not limited by this rule.
Unblocks: NAT.28, NAT.30, SCOPE.11

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Clean-cache C17/C# AOT consumers per RID; missing/transitive/wrong-RID library, hash collision, absent export, revoked artifact, source-unavailable negatives
Completion evidence for the ledger: Immutable native package production: behavioral, failure and package evidence (Instruments slice)
Notes: First RID (win-x64) is the realistic starting point given libusb Windows support is best-understood; other RIDs follow.
```

```text
Execute ArcForges delivery task NAT.25 — Pdf package production: all 6 RIDs + ContentSandbox Runtime.<rid> composition.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\native.md (anchor task-nat-25).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/nat-25 (python tools/delivery.py claim NAT.25 --worker <name>); task branch task/nat-25 in DesktopPlatform; ledger record ledger/tasks/nat-25.md.
Kind/size: producer/M. Baseline: not-started.
Outcome: ArcForges.Native.Pdf.Runtime.<rid> published for all 6 RIDs; the composed ContentSandbox.Runtime.<rid> (real parser closure) is rebuilt/signed once and published as the next immutable version per admitted RID.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-13.15 (ArcForges.Native.Pdf + Runtime.<rid>, plus the ContentSandbox.Runtime.<rid> republication from 13.13): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\13-high-risk-technical-probes.md, anchor rule-wp-13.15
- WP-13:producer-artifacts-and-integration-md-wp producer-artifacts-and-integration.md WP13 row: 'Probe-only 1.0, missing functional export or dependency prevents completion' (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\13-high-risk-technical-probes.md, package-level obligation

Entry condition: adoption slice ADOPT.02.native is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] NAT.15: the real PDFium backend and binding behind the complete arc_pdf_* export set, and the composition input for the production ContentSandbox parser registration
- [artifact] PLT.45: the WP11-owned host/broker/launcher mechanics stay the versioning authority for ContentSandbox.Runtime identity
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:src/Native/ArcForges.Native.Pdf.Runtime.*/**; DesktopPlatform:src/DesktopHelpers/ArcForges.ContentSandbox/**; DesktopPlatform:eng/packaging/packages.json
Shared resources (follow the owner protocol): RES-desktopplatform-native-build (append): The vcpkg baseline and overlay ports change only through a dependency-admission change with licence and provenance receipts; each native family adds its own CMake targets and workflow entries; triplet or port changes are rebased and rebuilt by their author; CPU-heavy native builds use the workstation build slot. PLT.39 may append only a narrowly scoped transport compatibility change to eng/native_provenance.py and offline tests in tests/tooling/test_native_provenance.py: after the verified cache-hit path, pass urllib.request.Request(url, headers={"User-Agent": "ArcForges/1.0 (+https://github.com/ArcForges/DesktopPlatform)"}) only when the complete requested URL equals https://visualstudio.microsoft.com/wp-content/uploads/2025/10/Visual_Studio_2026-License-Community_ENU.docx or https://visualstudio.microsoft.com/wp-content/uploads/2025/10/Visual-C-V14-License-Redistributable_and_Runtime_ENU.docx; preserve all other URL behavior, pinned URLs/hashes, TLS, timeout, redirects, cache, digest verification, temporary cleanup and atomic promotion, with no retries, dependency, workflow or runner changes. The DesktopPlatform integration owner serializes this shared helper append.; RES-desktopplatform-package-inventory (append): Each producer task adds its own package entry; every merge to main packs and publishes all packages at one version; consumers pin the candidate produced by the merge of the capability they need, never waiting for a package closure task; one merge queue.; RES-workstation-build-slot (exclusive): Exclusive per workstation for the duration of each CPU-heavy local build or test, through the workstation lock rather than a Plan lease: run the command as `python tools/delivery.py build-slot run --worker <name> --task <task> -- <command>` with the Plan repository tool, which holds the lock directory `.arcforges/build-slot` in the user profile with an owner record and heartbeat and recovers a lock whose holder stopped. Coding and review continue while a build waits; CI capacity is not limited by this rule.
Unblocks: NAT.28, NAT.30

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Clean-cache C17/C# AOT consumers per RID; PG-22 hostile-parser containment re-run at package level (not just source level)
Completion evidence for the ledger: Immutable native package production: behavioral, failure and package evidence (Pdf slice); PG-12 contribution
Notes: Depends on NAT.14 landing first (unlike the other packaging tasks, this one also republishes the shared ContentSandbox helper, so it is more tightly sequenced).
```

```text
Execute ArcForges delivery task NAT.28 — Dependency adoption receipts and hardware-lab closure.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\native.md (anchor task-nat-28).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/nat-28 (python tools/delivery.py claim NAT.28 --worker <name>); task branch task/nat-28 in DesktopPlatform; ledger record ledger/tasks/nat-28.md.
Kind/size: producer/M. Baseline: not-started.
Outcome: AD01-AD08 recorded for OIIO, OpenEXR, Imath, libusb, PDFium and every shipped transitive dependency; the hardware-lab inventory (serial plus an actual USB device with vendor/product identity, explicit interface/endpoint, firmware and driver versions) is completed; SBOM/licence/source and enabled-feature lists matched to actual packaged files.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-13.16 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\13-high-risk-technical-probes.md, anchor rule-wp-13.16

Entry condition: adoption slice ADOPT.02.native is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] NAT.22: Image package closure (OIIO/OpenEXR/Imath positions)
- [artifact] NAT.24: Instruments package closure (libusb position, physical USB device)
- [artifact] NAT.25: Pdf package closure (PDFium position)
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:tests/HardwareLab/**; DesktopPlatform:eng/provenance/**; DesktopPlatform:eng/policy/dependency-reviews/**
Unblocks: NAT.30

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Match SBOM/license/source and enabled-feature lists to actual packaged files; bind every physical result and each simulated absence to its evidence class
Completion evidence for the ledger: Dependency adoption and hardware receipts: behavioral, failure and package evidence; PG-03 and PG-08 contributions covering the complete shipped graph and physical fixtures
Notes: This is where PG-08 is genuinely CLOSED (not merely seeded); requires a real labelled USB device to exist. Everything else in this task (SBOM/licence matching, non-USB inventory) can proceed without exotic hardware.
```

```text
Execute ArcForges delivery task NAT.29 — Verify the owned WP06 artifact set and real cross-runtime integration.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\native.md (anchor task-nat-29).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/nat-29 (python tools/delivery.py claim NAT.29 --worker <name>); task branch task/nat-29 in DesktopPlatform; ledger record ledger/tasks/nat-29.md.
Kind/size: integration/M. Baseline: not-started.
Outcome: Actual candidate NuGet restore/native loading and desktop AOT; C# AOT gRPC/gRPC-Web plus selected auth/storage/SQL adapters; Kotlin/Jetpack Compose generated-client calls; React client calls; a minimal deployed CF<->reachable C#<->R2 chain -- a bounded foundation probe, explicitly not the full WP-52 Cloud Harness

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-06.90 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\06-aot-jit-and-wasm-publish-proof.md, anchor rule-wp-06.90

Entry condition: adoption slice ADOPT.02.native is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] PRF.02: real, delivered outcome of PRF.02 (ArcScope desktop Native AOT package proof)
- [artifact] PRF.04: real, delivered outcome of PRF.04 (Local RPC under AOT: bidirectional named-pipe/UDS probe processes)
- [artifact] PRF.05: real, delivered outcome of PRF.05 (Generated gRPC-Web under AOT against deployed Worker/Container ingress)
- [artifact] PRF.06: real, delivered outcome of PRF.06 (Realtime (EventService.Watch/Poll) under AOT)
- [artifact] PRF.07: real, delivered outcome of PRF.07 (Cloudflare Native AOT host + D1 + DO/Queue/R2 foundation proof)
- [artifact] PRF.08: real, delivered outcome of PRF.08 (React production build and generated TS SDK proof)
- [artifact] PRF.09: real, delivered outcome of PRF.09 (Third-party control AOT admission gate and first candidate)
- [artifact] PRF.10: real, delivered outcome of PRF.10 (Android Kotlin/Jetpack Compose gRPC-Web and CF proof)
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: 

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Local real-integration run of the affected scenario in an existing environment, recorded once; offline and static checks in CI; no hosted runtime, device, browser, live-service or inference CI (P2-017).
Completion evidence for the ledger: Actual candidate NuGet restore/native loading and desktop AOT; C# AOT gRPC/gRPC-Web plus selected auth/storage/SQL adapters; Kotlin/Jetpack Compose generated-client calls; React client calls; a minimal deployed CF<->reachable C#<->R2 chain -- a bounded foundation probe, explicitly not the full WP-52 Cloud Harness
```

```text
Execute ArcForges delivery task NAT.30 — Verify the complete native producer set as one immutable candidate.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\native.md (anchor task-nat-30).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/nat-30 (python tools/delivery.py claim NAT.30 --worker <name>); task branch task/nat-30 in DesktopPlatform; ledger record ledger/tasks/nat-30.md.
Kind/size: integration/M. Baseline: not-started.
Outcome: Image tiles, PDF, instruments, cancel/lifetime/hostile-helper vectors and missing-DLL/wrong-RID negative consumers, all against actual WP07 to WP12 mechanisms (persistence, local RPC, shell, ContentSandbox, telemetry) -- probe-only exports never pass; this is the gate WP14/WP33 consumers wait behind

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-13.90 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\13-high-risk-technical-probes.md, anchor rule-wp-13.90

Entry condition: adoption slice ADOPT.02.native is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] NAT.06: real, delivered outcome of NAT.06 (Common native ABI: preambles, pack8 records, ownership, cancellation, bounded buffers)
- [artifact] NAT.11: real, delivered outcome of NAT.11 (Image family: still-image codecs (PNG/TIFF/EXR))
- [artifact] NAT.13: real, delivered outcome of NAT.13 (Instruments family: serial and USB devices (NEW library))
- [artifact] NAT.14: real, delivered outcome of NAT.14 (Pdf family: arcpdf-abi export set, ArcForges.Native.Pdf binding and production parser composition seam in the WP11 helper)
- [artifact] NAT.15: real, delivered outcome of NAT.15 (Pdf family: real PDFium (chromium/8044) build admission, binding and real-parser containment acceptance)
- [artifact] NAT.22: real, delivered outcome of NAT.22 (Image package production: all 6 RIDs)
- [artifact] NAT.24: real, delivered outcome of NAT.24 (Instruments package production: all 6 RIDs)
- [artifact] NAT.25: real, delivered outcome of NAT.25 (Pdf package production: all 6 RIDs + ContentSandbox Runtime.<rid> composition)
- [artifact] NAT.28: real, delivered outcome of NAT.28 (Dependency adoption receipts and hardware-lab closure)
- [artifact] NAT.01: package task delivered
- [artifact] NAT.03: package task delivered
- [artifact] NAT.05: package task delivered
- [artifact] PLT.54: package task delivered
- [artifact] GOV.17: the producer set without the retired native families
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: 

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Local real-integration run of the affected scenario in an existing environment, recorded once; offline and static checks in CI; no hosted runtime, device, browser, live-service or inference CI (P2-017).
Completion evidence for the ledger: Image tiles, PDF, instruments, cancel/lifetime/hostile-helper vectors and missing-DLL/wrong-RID negative consumers, all against actual WP07 to WP12 mechanisms (persistence, local RPC, shell, ContentSandbox, telemetry) -- probe-only exports never pass; this is the gate WP14/WP33 consumers wait behind
```
