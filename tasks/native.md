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
Completion evidence for the ledger: AOT publish log and in-binary device tool request decode/execute trace; explicit note that the model loop itself is NOT probed here (it is the C# Harness of P2-021 item 5, with Workers AI reached through the thin ai.internal adapter)
Notes: One of WP13's two canonical early risk proofs (package goal: 'retire the early technical risks'). Parallel with NAT.03 (disjoint write scopes). Planning repair 2026-10-08 (DLV-34; P2-021): the evidence note names the C# Harness instead of the Cloudflare Workflow as the model loop that this probe does not cover. The probe itself is unchanged.
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
Outcome: Each of the two retained probes (A and C) keeps a recorded result as verification evidence only (no written conclusion record is a product dependency); every native dependency the probes introduced has a recorded licence position; the tests/HardwareLab device inventory is created (device/firmware/driver versions) -- seeding PG-08 (completed later by NAT.28/WP-13.16).

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

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Completeness check: every probe has a recorded environment, procedure and result
Completion evidence for the ledger: Two probe result records kept as verification evidence only; licence positions for probe-introduced dependencies; hardware inventory shell
Notes: Small synthesis task; not itself a risk probe. Planning repair 2026-10-09 (P2-026; scope correction, brief section 11 S19(c)): reduced: written probe-conclusion records as a product dependency and licence positions for PDF-only dependencies are out of scope, not completed.
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
Unblocks: NAT.11, NAT.13, NAT.14, NAT.30, NAT.32

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): On the admitted RIDs compile the common headers and run only CTest targets arc_native_abi_c17_layout_tests (C17) and arc_native_abi_cpp20_tests (C++20), both retained shim-static; on Windows x64 run only `dotnet test tests/NativeAbiTests/ArcForges.Tests.NativeAbiTests.csproj --filter Category=NativeAbiLayout --no-restore`, excluding the existing image runtime smoke. Assert all field offsets and 17 normative sizes, wrong-size/version/null/closed-handle failures, and zero outputs on failure.
Completion evidence for the ledger: Common ABI and deterministic failure surface: behavioral, failure and package evidence
Notes: Hard prerequisite for NAT.11, NAT.13 and NAT.14 (artifact edges from each). NAT.06 alone registers native/shared/tests/arc_native_abi_c17_layout.c as CTest target arc_native_abi_c17_layout_tests and native/shared/tests/arc_native_abi_cpp20_tests.cpp as target arc_native_abi_cpp20_tests in native/CMakeLists.txt; both tests and targets are retained shim-static only. The existing tests/NativeAbiTests/ArcForges.Tests.NativeAbiTests.csproj gains only a ProjectReference to the existing Native.Abstractions project; CommonAbiLayoutTests.cs uses that project. On Windows x64 native-abi.yml runs only `dotnet test tests/NativeAbiTests/ArcForges.Tests.NativeAbiTests.csproj --filter Category=NativeAbiLayout --no-restore`, so the existing image runtime smoke is excluded. Do not create a project, add a PackageReference or change package identity, or authorize other workflow behavior. Append only these three new test-source rows to eng/provenance/files.json. Preserve the 17 normative size/offset checks and wrong-size, version, null, closed-handle, and zero-output-on-failure cases. No native family implementation, library identity, package identity or dependency expansion is authorized; runtime/policy input binding changes are limited to exact ADP-07 current rows necessary for these files. Planning repair 2026-10-08 (DLV-34; P2-022): the PDF family named in this delivered outcome is retired. The arc_pdf_* block and its signature pins in the common ABI, and the NativePdfPageV1 entry, are removed by the NAT.32 deletion change, which is chained as a successor receipt. The still-image, instrument and ABI families are unchanged. The delivered outcome, validation and evidence are history and are not changed by this note. Planning repair 2026-10-09 (P2-026; scope correction): reduced: the PDF family ABI (arc_pdf_* block and its signature pins) is out of scope, not completed; the delivered text is history.
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
Execute ArcForges delivery task NAT.24 — Instruments package production: three supported RIDs (win-x64, win-arm64, linux-x64).

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\native.md (anchor task-nat-24).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/nat-24 (python tools/delivery.py claim NAT.24 --worker <name>); task branch task/nat-24 in DesktopPlatform; ledger record ledger/tasks/nat-24.md.
Kind/size: producer/S. Baseline: not-started.
Outcome: ArcForges.Native.Instruments.Runtime.<rid> published for the three supported desktop RIDs (win-x64, win-arm64, linux-x64); osx-x64 and osx-arm64 are outside the delivery scope (P2-023).

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-13.15 (ArcForges.Native.Instruments + Runtime.<rid> only): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\13-high-risk-technical-probes.md, anchor rule-wp-13.15
- WP-13:producer-artifacts-and-integration-md-wp producer-artifacts-and-integration.md WP13 row: 'Probe-only 1.0, missing functional export or dependency prevents completion' (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\13-high-risk-technical-probes.md, package-level obligation

Entry condition: adoption slice ADOPT.02.native is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] NAT.13: complete arc_instruments_* export set
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:src/Native/ArcForges.Native.Instruments.Runtime.win-x64/** (new folder; no Instruments runtime folder exists yet); DesktopPlatform:src/Native/ArcForges.Native.Instruments.Runtime.win-arm64/** (new folder); DesktopPlatform:src/Native/ArcForges.Native.Instruments.Runtime.linux-x64/** (new folder); DesktopPlatform:eng/packaging/packages.json
Shared resources (follow the owner protocol): RES-desktopplatform-native-build (append): The vcpkg baseline and overlay ports change only through a dependency-admission change with licence and provenance receipts; each native family adds its own CMake targets and workflow entries; triplet or port changes are rebased and rebuilt by their author; CPU-heavy native builds use the workstation build slot. PLT.39 may append only a narrowly scoped transport compatibility change to eng/native_provenance.py and offline tests in tests/tooling/test_native_provenance.py: after the verified cache-hit path, pass urllib.request.Request(url, headers={"User-Agent": "ArcForges/1.0 (+https://github.com/ArcForges/DesktopPlatform)"}) only when the complete requested URL equals https://visualstudio.microsoft.com/wp-content/uploads/2025/10/Visual_Studio_2026-License-Community_ENU.docx or https://visualstudio.microsoft.com/wp-content/uploads/2025/10/Visual-C-V14-License-Redistributable_and_Runtime_ENU.docx; preserve all other URL behavior, pinned URLs/hashes, TLS, timeout, redirects, cache, digest verification, temporary cleanup and atomic promotion, with no retries, dependency, workflow or runner changes. The DesktopPlatform integration owner serializes this shared helper append.; RES-desktopplatform-package-inventory (append): Each producer task adds its own package entry; every merge to main packs and publishes all packages at one version; consumers pin the candidate produced by the merge of the capability they need, never waiting for a package closure task; one merge queue.; RES-workstation-build-slot (exclusive): Exclusive per workstation for the duration of each CPU-heavy local build or test, through the workstation lock rather than a Plan lease: run the command as `python tools/delivery.py build-slot run --worker <name> --task <task> -- <command>` with the Plan repository tool, which holds the lock directory `.arcforges/build-slot` in the user profile with an owner record and heartbeat and recovers a lock whose holder stopped. Coding and review continue while a build waits; CI capacity is not limited by this rule.
Unblocks: NAT.28, NAT.30, SCOPE.11

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Clean-cache C17/C# AOT consumers per RID; missing/transitive/wrong-RID library, hash collision, absent export, revoked artifact, source-unavailable negatives
Completion evidence for the ledger: Immutable native package production: behavioral, failure and package evidence (Instruments slice)
Notes: First RID (win-x64) is the realistic starting point given libusb Windows support is best-understood; other RIDs follow. Planning repair 2026-10-08 (DLV-34; P2-023; coordinator RID adjudication 2026-10-08): macOS is outside the delivery scope; no osx RID, macOS artifact, signing or notarisation is part of this task. The desktop RID set is win-x64, win-arm64 and linux-x64. The osx RIDs remain listed in eng/build/desktop-rids.props, the CMake presets and the osx lock sections until GOV.30 completes; this task produces no osx runtime. The existing first-RID note is unchanged.
```

```text
Execute ArcForges delivery task NAT.28 — Dependency adoption receipts and hardware-lab closure.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\native.md (anchor task-nat-28).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/nat-28 (python tools/delivery.py claim NAT.28 --worker <name>); task branch task/nat-28 in DesktopPlatform; ledger record ledger/tasks/nat-28.md.
Kind/size: producer/M. Baseline: not-started.
Outcome: AD01-AD08 recorded for libusb and every shipped transitive dependency (PDFium is not shipped: PDF parsing is retired under P2-022); the hardware-lab inventory (serial plus an actual USB device with vendor/product identity, explicit interface/endpoint, firmware and driver versions) is completed; SBOM/licence/source and enabled-feature lists matched to actual packaged files.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-13.16 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\13-high-risk-technical-probes.md, anchor rule-wp-13.16

Entry condition: adoption slice ADOPT.02.native is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] NAT.24: Instruments package closure (libusb position, physical USB device)
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:tests/HardwareLab/**; DesktopPlatform:eng/provenance/**; DesktopPlatform:eng/policy/dependency-reviews/**
Shared resources (follow the owner protocol): RES-desktopplatform-policy-data (append): Generated policy data is regenerated from its pinned source and never hand-edited; the reason-code registry is append-only with stable codes; each task adds its own test classes and evidence rows.
Unblocks: NAT.30

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Match SBOM/license/source and enabled-feature lists to actual packaged files; bind every physical result and each simulated absence to its evidence class
Completion evidence for the ledger: Dependency adoption and hardware receipts: behavioral, failure and package evidence; PG-03 and PG-08 contributions covering the complete shipped graph and physical fixtures
Notes: This is where PG-08 is genuinely CLOSED (not merely seeded); requires a real labelled USB device to exist. Everything else in this task (SBOM/licence matching, non-USB inventory) can proceed without exotic hardware. Planning repair 2026-10-08 (DLV-34; P2-022): PDFium is removed from the AD01-AD08 scope because PDF parsing is retired and PDFium is not shipped. PG-03, PG-08 and the hardware-lab closure are unchanged. NAT.28 writes eng/provenance/** and eng/policy/dependency-reviews/** and declares RES-desktopplatform-policy-data (append), the existing shared resource that covers provenance and dependency-review files and that PLT.46 and PLT.54 also declare, so those writes are serialised by the resource protocol. Its start on NAT.25, which now starts after PLT.54 (DLV-11), also orders it after PLT.54's provenance rows. Planning repair 2026-10-09 (P2-026; scope correction): reduced: OIIO, OpenEXR and Imath adoption receipts and the image-package closure are out of scope, not completed; libusb and instrument receipts remain.
```

```text
Execute ArcForges delivery task NAT.29 — Verify the owned WP06 artifact set and real cross-runtime integration.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\native.md (anchor task-nat-29).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/nat-29 (python tools/delivery.py claim NAT.29 --worker <name>); task branch task/nat-29 in DesktopPlatform; ledger record ledger/tasks/nat-29.md.
Kind/size: integration/M. Baseline: not-started.
Outcome: Actual candidate NuGet restore/native loading and desktop AOT; C# AOT gRPC/gRPC-Web plus selected auth/storage/SQL adapters; .NET MAUI Android calls through the generated C# Contracts client; Blazor WebAssembly calls through the generated C# Contracts client; a minimal deployed CF<->reachable C#<->R2 chain -- a bounded foundation probe, explicitly not the full WP-52 Cloud Harness

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-06.90 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\06-aot-jit-and-wasm-publish-proof.md, anchor rule-wp-06.90

Entry condition: adoption slice ADOPT.02.native is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] PRF.02: real, delivered outcome of PRF.02 (ArcScope desktop Native AOT package proof)
- [artifact] PRF.04: real, delivered outcome of PRF.04 (Local RPC under AOT: bidirectional named-pipe/UDS probe processes)
- [artifact] PRF.05: real, delivered outcome of PRF.05 (Generated gRPC-Web under AOT against deployed Worker/Container ingress)
- [artifact] PRF.06: real, delivered outcome of PRF.06 (Realtime (EventService.Watch/Poll) under AOT)
- [artifact] PRF.07: real, delivered outcome of PRF.07 (Cloudflare Native AOT host + D1 + DO/Queue/R2 foundation proof)
- [artifact] PRF.11: real, delivered outcome of PRF.11 (Blazor WebAssembly production build and generated C# SDK proof against deployed ingress)
- [artifact] PRF.12: real, delivered outcome of PRF.12 (MAUI Android release proof)
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: 

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Local real-integration run of the affected scenario in an existing environment, recorded once; offline and static checks in CI; no hosted runtime, device, browser, live-service or inference CI (P2-017).
Completion evidence for the ledger: Actual candidate NuGet restore/native loading and desktop AOT; C# AOT gRPC/gRPC-Web plus selected auth/storage/SQL adapters; .NET MAUI Android calls through the generated C# Contracts client; Blazor WebAssembly calls through the generated C# Contracts client; a minimal deployed CF<->reachable C#<->R2 chain -- a bounded foundation probe, explicitly not the full WP-52 Cloud Harness
Notes: Planning repair 2026-10-08 (DLV-34; P2-021): the Kotlin/Jetpack Compose and React client calls of this probe become .NET MAUI Android and Blazor WebAssembly calls through the generated C# Contracts client; the start edges move to PRF.11 and PRF.12. No acceptance is removed.
```

```text
Execute ArcForges delivery task NAT.30 — Verify the complete native producer set as one immutable candidate.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\native.md (anchor task-nat-30).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/nat-30 (python tools/delivery.py claim NAT.30 --worker <name>); task branch task/nat-30 in DesktopPlatform; ledger record ledger/tasks/nat-30.md.
Kind/size: integration/M. Baseline: not-started.
Outcome: Instruments, cancel/lifetime/hostile-helper vectors and missing-DLL/wrong-RID negative consumers, all against actual WP07 to WP12 mechanisms (persistence, local RPC, shell, ContentSandbox, telemetry) -- probe-only exports never pass; this is the gate WP14/WP33 consumers wait behind

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-13.90 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\13-high-risk-technical-probes.md, anchor rule-wp-13.90

Entry condition: adoption slice ADOPT.02.native is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] NAT.06: real, delivered outcome of NAT.06 (Common native ABI: preambles, pack8 records, ownership, cancellation, bounded buffers)
- [artifact] NAT.13: real, delivered outcome of NAT.13 (Instruments family: serial and USB devices (NEW library))
- [artifact] NAT.24: real, delivered outcome of NAT.24 (Instruments package production for the non-macOS desktop RIDs)
- [artifact] NAT.28: real, delivered outcome of NAT.28 (Dependency adoption receipts and hardware-lab closure)
- [artifact] NAT.01: package task delivered
- [artifact] NAT.03: package task delivered
- [artifact] NAT.05: package task delivered
- [artifact] GOV.17: the producer set without the retired native families
- [artifact] GOV.30: the osx-free desktop RID set: osx-x64 and osx-arm64 removed from eng/build/desktop-rids.props, the CMake osx presets and the osx lock sections (GOV.30)
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: 
Unblocks: REL.02

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Local real-integration run of the affected scenario in an existing environment, recorded once; offline and static checks in CI; no hosted runtime, device, browser, live-service or inference CI (P2-017).
Completion evidence for the ledger: Candidate verification records: instrument, cancel/lifetime and hostile-helper vector results and missing-DLL/wrong-RID negative consumer results, each run against the actual WP07 to WP12 mechanisms (persistence, local RPC, shell, ContentSandbox, telemetry); probe-only export results, which never pass.
Notes: Planning repair 2026-10-08 (DLV-34; P2-022): the PDF family is removed from the candidate. The start edges from superseded NAT.15 and from NAT.14 are retargeted to NAT.31 (still-image composition) and NAT.32 (PDF retirement, whose closed-refusal and no-PDF-parser checks are part of the candidate outcome). The start edges to NAT.01, NAT.03, NAT.05, NAT.06, NAT.11, NAT.13, NAT.28 and GOV.17 keep their task IDs and are not changed by this patch. The start edges to NAT.22, NAT.24, NAT.25 and PLT.54 keep their task IDs; their own task records carry the RID and image-only changes. Planning repair 2026-10-08 (DLV-34; P2-023): GOV.30 removes osx-x64 and osx-arm64 from eng/build/desktop-rids.props, the CMake osx presets and the osx lock sections, and depends only on GOV.18 (no CON.40 edge). The start edge on GOV.30 added here therefore holds no CON.40 wait. This integration verifies the non-macOS desktop RIDs (win-x64, win-arm64 and linux-x64); linux-arm64 is not a desktop RID (coordinator decision, 2026-10-08). Planning repair 2026-10-08 (DLV-34; P2-022 item 3; coordinator adjudication, brief section 10): the PDF RPC wording follows the repaired NAT.32 record; no new refusal is introduced. Planning repair 2026-10-09 (P2-026; scope correction): reduced: image-tile verification and EXR and TIFF writer and codec-breadth vectors are out of scope, not completed; the start edges to NAT.11, NAT.22, NAT.25, NAT.31, NAT.32 and PLT.54 are removed. Planning review 2026-10-09 (P2-026; S8): the PDF clauses are removed from the outcome and the evidence. The five PDF RPC closed-refusal results and the no-PDF-parser check belong to the out-of-scope NAT.32 and are not validated here (user rule 2). NAT.30 keeps only its instrument (libusb) and common-ABI legs.
```

### Out of scope

Excluded from the active plan. No prompt is issued and these tasks are never claimable; their decision, note and ledger status are listed here.

| Task | Title | Decision | Mode | Note | Ledger status |
|---|---|---|---|---|---|
| NAT.11 | Image family: still-image codecs (PNG/TIFF/EXR) | P2-026 | closeout | finished under the DesktopPlatform exception (P2-026); never an ArcScope prerequisite | complete |
| NAT.14 | Pdf family: arcpdf-abi export set, ArcForges.Native.Pdf binding and production parser composition seam in the WP11 helper (NEW library; real PDFium is NAT.15) | P2-026 | excluded | PDF engine composition and binding have no retained ArcScope consumer after P2-022; delivered history kept, out of scope, not completed (P2-026) | complete |
| NAT.15 | Pdf family: real PDFium (chromium/8044) build admission, binding and real-parser containment acceptance | P2-026 | excluded | PDF production parser superseded under P2-022 and has no V1 consumer; out of scope, not completed (P2-026) | superseded |
| NAT.22 | Image package production: three supported RIDs (win-x64, win-arm64, linux-x64) | P2-026 | excluded | the in-app still-image decode is out of V1 (P2-026 S1 and S8: metadata cards only, no decode), so this image runtime package has no ArcScope consumer; out of scope, not completed | no record |
| NAT.25 | ContentSandbox Runtime.<rid> republication from the still-image composition (three supported RIDs; PDF package retired) | P2-026 | excluded | the ContentSandbox still-image runtime republication serves only the in-app still-image decode, which is out of V1 (P2-026 S1 and S8); out of scope, not completed | no record |
| NAT.31 | Still-image composition: production still-image parsers (NAT.11 family) composed into the ContentSandbox helper, with real containment re-run | P2-026 | excluded | composing still-image parsers into the ContentSandbox helper serves only the in-app decoded thumbnail, which is out of V1 (P2-026 S1 and S8); out of scope, not completed | no record |
| NAT.32 | PDF engine retirement: remove native/arcpdf-abi, ArcForges.Native.Pdf and the helper PDF parser path | P2-026 | excluded | PDF engine retirement is delivered history under P2-022 (the ledger records NAT.32 complete, DesktopPlatform PR 172 merged at e0f2e563); no further NAT.32 work is in the active plan (P2-026 S2) | complete |
