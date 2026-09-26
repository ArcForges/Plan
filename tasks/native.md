# ArcForges delivery task prompts — Native producers and probes

Generated from Design `docs/planning/delivery/delivery-graph.json` by `tools/delivery.py`; do not edit by hand.
Each block is self-contained. Claim a task only when `python tools/delivery.py ready` lists it, with
`python tools/delivery.py claim <TASK-ID> --worker <name>`, then follow `arcforges-implementation.md`.
Tasks are ordered by lane for reading; the order is not a schedule.

## Native producers and probes

```text
Execute ArcForges delivery task NAT.01 — Probe A: device tool execution under Native AOT.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\native.md (anchor task-nat-01).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/nat-01 (python tools/delivery.py claim NAT.01 --worker <name>); task branch task/nat-01 in DesktopPlatform; ledger record ledger/tasks/nat-01.md.
Kind/size: producer/M. Baseline: not-started.
Outcome: Inside a published Native AOT desktop binary, a stub ToolRequest is pulled, re-authorised locally, resolved through the generated allowlist to a CapabilityKey, decoded into a typed product request, invoked and returns an idempotent result -- with an AOT publish log showing zero diagnostics and a negative test proving no reflection-based registration/decode path compiles or exists.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-13.00 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\13-high-risk-technical-probes.md, anchor rule-wp-13.00
- WP-13:ss1-nd-05-probe-scaffolds-13-00-13-03-ar SS1/ND-05: probe scaffolds (13.00-13.03) are cleanup-or-regression-fixture; production 13.05-13.16 code is retained and maintained -- different lifecycle rules for the two groups even though both may live under similar directories (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\13-high-risk-technical-probes.md, package-level obligation

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
Notes: One of WP13's four canonical early risk proofs (package goal: 'retire the four early technical risks'). Parallel with NAT.02/03/04 (disjoint write scopes).
```

```text
Execute ArcForges delivery task NAT.02 — Probe B: block editor, store, undo and recovery.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\native.md (anchor task-nat-02).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/nat-02 (python tools/delivery.py claim NAT.02 --worker <name>); task branch task/nat-02 in DesktopPlatform; ledger record ledger/tasks/nat-02.md.
Kind/size: producer/M. Baseline: not-started.
Outcome: A minimal block editor over the local store demonstrates create/edit/reorder, undo/redo across a composite operation, and recovery from a hard process kill mid-edit that returns to the last committed boundary with uncommitted work explicitly reported as loss -- proving undo, revision, checkpoint and journal are four distinct mechanisms.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-13.01 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\13-high-risk-technical-probes.md, anchor rule-wp-13.01
- WP-13:ss1-nd-05-probe-scaffolds-13-00-13-03-ar SS1/ND-05: probe scaffolds (13.00-13.03) are cleanup-or-regression-fixture; production 13.05-13.16 code is retained and maintained -- different lifecycle rules for the two groups even though both may live under similar directories (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\13-high-risk-technical-probes.md, package-level obligation

Entry condition: adoption slice ADOPT.02.native is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] PLT.01: the real local persistence single-writer journal/checkpoint mechanism
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:benchmarks/probes/editor-store/**
Unblocks: NAT.05, NAT.30

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Kill-during-edit recovery run; undo-across-composite-operation test; explicit test that undo history is not crash recovery (QI-09)
Completion evidence for the ledger: Kill-during-edit recovery and undo-distinction results
Notes: Parallel with NAT.01/03/04.
```

```text
Execute ArcForges delivery task NAT.03 — Probe C: high-throughput acquisition over a real transport.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\native.md (anchor task-nat-03).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/nat-03 (python tools/delivery.py claim NAT.03 --worker <name>); task branch task/nat-03 in DesktopPlatform; ledger record ledger/tasks/nat-03.md.
Kind/size: producer/M. Baseline: not-started.
Outcome: Sustained acquisition from a real transport (at least one real TCP/UDP/serial configuration, not an in-memory generator, per BR-06) runs above the intended product target through a ring buffer with responsive plot downsampling; overrun is counted and timestamped, pausing the view never stops recording, and disconnect leaves an explicit gap.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-13.02 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\13-high-risk-technical-probes.md, anchor rule-wp-13.02
- WP-13:ss1-nd-05-probe-scaffolds-13-00-13-03-ar SS1/ND-05: probe scaffolds (13.00-13.03) are cleanup-or-regression-fixture; production 13.05-13.16 code is retained and maintained -- different lifecycle rules for the two groups even though both may live under similar directories (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\13-high-risk-technical-probes.md, package-level obligation

Entry condition: adoption slice ADOPT.02.native is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- none
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:benchmarks/probes/acquisition/**
Unblocks: NAT.05, NAT.30

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Sustained-throughput run with recorded rate/memory/drop counts; induced overrun; induced disconnect; pause-while-recording test
Completion evidence for the ledger: Sustained-throughput record with overrun/gap/pause results
Notes: No hard start-dependency on any other WP -- can begin immediately using a real TCP/UDP loopback or serial-over-USB pair; exotic hardware is not required for the first real-transport configuration. Parallel with NAT.01/02/04.
```

```text
Execute ArcForges delivery task NAT.04 — Probe D: native decode and audio/video synchronisation.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\native.md (anchor task-nat-04).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/nat-04 (python tools/delivery.py claim NAT.04 --worker <name>); task branch task/nat-04 in DesktopPlatform; ledger record ledger/tasks/nat-04.md.
Kind/size: producer/L. Baseline: not-started.
Outcome: Native decode through a thin C ABI shim displays one frame in the desktop shell with audio/video synchronised against a shared timeline clock; safe handles, managed-side input validation, a clean sanitiser run and a sacrificial-process crash test all pass; hardware acceleration is discovered at runtime with a proven software fallback.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-13.03 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\13-high-risk-technical-probes.md, anchor rule-wp-13.03
- WP-13:ss1-nd-05-probe-scaffolds-13-00-13-03-ar SS1/ND-05: probe scaffolds (13.00-13.03) are cleanup-or-regression-fixture; production 13.05-13.16 code is retained and maintained -- different lifecycle rules for the two groups even though both may live under similar directories (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\13-high-risk-technical-probes.md, package-level obligation

Entry condition: adoption slice ADOPT.02.native is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] PRF.01: a shape for an AOT-published desktop shell capable of hosting a display surface
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:benchmarks/probes/media/**
Shared resources (follow the owner protocol): RES-workstation-build-slot (exclusive): Exclusive per workstation for the duration of each CPU-heavy local build or test, through the workstation lock rather than a Plan lease: run the command as `python tools/delivery.py build-slot run --worker <name> --task <task> -- <command>` with the Plan repository tool, which holds the lock directory `.arcforges/build-slot` in the user profile with an owner record and heartbeat and recovers a lock whose holder stopped. Coding and review continue while a build waits; CI capacity is not limited by this rule.
Unblocks: NAT.05, NAT.30

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Frame-display run; audio/video sync measurement; sanitiser run (ASan/UBSan); sacrificial-process crash test; forced-software-path run
Completion evidence for the ledger: Frame display, synchronisation measurement, sanitiser and sacrificial-process results
Notes: GPU-accelerated path testing is necessarily per-local-machine (whatever GPU is available); the required CPU software-fallback path is universally testable. Parallel with NAT.01/02/03.
```

```text
Execute ArcForges delivery task NAT.05 — Probe evidence, licence positions, conclusions and hardware-lab inventory seed.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\native.md (anchor task-nat-05).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/nat-05 (python tools/delivery.py claim NAT.05 --worker <name>); task branch task/nat-05 in DesktopPlatform; ledger record ledger/tasks/nat-05.md.
Kind/size: producer/S. Baseline: not-started.
Outcome: Each of the four probes has a written conclusion (proved / not proved / downstream constraint / open items); every native dependency the probes introduced has a recorded licence position; the tests/HardwareLab device inventory is created (device/firmware/driver versions) -- seeding PG-08 (completed later by NAT.28/WP-13.16).

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-13.04 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\13-high-risk-technical-probes.md, anchor rule-wp-13.04

Entry condition: adoption slice ADOPT.02.native is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] NAT.01: Probe A result
- [artifact] NAT.02: Probe B result
- [artifact] NAT.03: Probe C result
- [artifact] NAT.04: Probe D result
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:eng/verification/probe-evidence/**; DesktopPlatform:tests/HardwareLab/**
Unblocks: NAT.30

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Completeness check: every probe has a recorded environment, procedure, result and conclusion
Completion evidence for the ledger: Four written probe conclusions; licence positions for probe-introduced dependencies; hardware inventory shell
Notes: Small synthesis task; not itself a risk probe.
```

```text
Execute ArcForges delivery task NAT.06 — Common native ABI: preambles, pack8 records, ownership, cancellation, bounded buffers.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\native.md (anchor task-nat-06).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/nat-06 (python tools/delivery.py claim NAT.06 --worker <name>); task branch task/nat-06 in DesktopPlatform; ledger record ledger/tasks/nat-06.md.
Kind/size: producer/L. Baseline: not-started.
Outcome: annex-06 common preambles, fixed numeric keys, pack8 records, ownership/cancellation/bounded-buffer helpers compile as C17/C++20 headers and C# layouts for all seven families; every field offset and all 17 normative sizes are asserted; wrong-size/version/null/closed-handle cases and zero-leaked-output-on-failure are proven. ArcForges.Native.Abstractions managed package (status/handle types only) is published. The five existing probe-library identities (incl. arc_metal_*) are retained unchanged.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-13.05 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\13-high-risk-technical-probes.md, anchor rule-wp-13.05
- WP-13:ss1-nd-05-probe-scaffolds-13-00-13-03-ar SS1/ND-05: probe scaffolds (13.00-13.03) are cleanup-or-regression-fixture; production 13.05-13.16 code is retained and maintained -- different lifecycle rules for the two groups even though both may live under similar directories (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\13-high-risk-technical-probes.md, package-level obligation
- WP-13:ss4-major-types-note-no-native-pointer-b SS4 major-types note: no native pointer becomes a managed domain identifier or a wire field (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\13-high-risk-technical-probes.md, package-level obligation

Entry condition: adoption slice ADOPT.02.native is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- none
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:native/shared/**; DesktopPlatform:native/*/include/arc/**; DesktopPlatform:src/Native/ArcForges.Native.Abstractions/**
Shared resources (follow the owner protocol): RES-desktopplatform-package-inventory (append): Each producer task adds its own package entry; every merge to main packs and publishes all packages at one version; consumers pin the candidate produced by the merge of the capability they need, never waiting for a package closure task; one merge queue.; RES-workstation-build-slot (exclusive): Exclusive per workstation for the duration of each CPU-heavy local build or test, through the workstation lock rather than a Plan lease: run the command as `python tools/delivery.py build-slot run --worker <name> --task <task> -- <command>` with the Plan repository tool, which holds the lock directory `.arcforges/build-slot` in the user profile with an owner record and heartbeat and recovers a lock whose holder stopped. Coding and review continue while a build waits; CI capacity is not limited by this rule.
Unblocks: NAT.07, NAT.08, NAT.09, NAT.10, NAT.11, NAT.12, NAT.13, NAT.14, NAT.15, NAT.30, NOTES.09, SLATE.15, SLATE.38

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Compile C17/C++20 headers and C# layouts on the admitted RIDs; offset/size assertions; wrong-size/version/null/closed-handle negative tests
Completion evidence for the ledger: Common ABI and deterministic failure surface: behavioral, failure and package evidence
Notes: Hard prerequisite for NAT.07-15 (artifact edges from each).
```

```text
Execute ArcForges delivery task NAT.07 — Media family: reader, probe, frame and seek (arc_media_reader_*).

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\native.md (anchor task-nat-07).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/nat-07 (python tools/delivery.py claim NAT.07 --worker <name>); task branch task/nat-07 in DesktopPlatform; ledger record ledger/tasks/nat-07.md.
Kind/size: producer/L. Baseline: not-started.
Outcome: arc_media_reader_open/stream/seek/next/close and arc_media_buffer_* implemented over the selected FFmpeg demux/decode path and the WP11 restricted helper; stream metadata, delayed frames, EOF and seek epochs preserved; every export has a behavioral oracle and bounded isolated execution.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-13.06 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\13-high-risk-technical-probes.md, anchor rule-wp-13.06
- WP-13:ss1-nd-05-probe-scaffolds-13-00-13-03-ar SS1/ND-05: probe scaffolds (13.00-13.03) are cleanup-or-regression-fixture; production 13.05-13.16 code is retained and maintained -- different lifecycle rules for the two groups even though both may live under similar directories (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\13-high-risk-technical-probes.md, package-level obligation
- WP-13:ss4-major-types-note-no-native-pointer-b SS4 major-types note: no native pointer becomes a managed domain identifier or a wire field (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\13-high-risk-technical-probes.md, package-level obligation

Entry condition: adoption slice ADOPT.02.native is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] NAT.06: compiled common ABI headers/layouts (arc_io_v1, arc_reader_options_v1, arc_frame_v1, arc_region_v1)
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:native/arcmedia-ffmpeg-abi/src/**; DesktopPlatform:native/arcmedia-ffmpeg-abi/include/**; DesktopPlatform:native/arcmedia-ffmpeg-abi/tests/**; DesktopPlatform:src/Native/ArcForges.Native.Media/**
Shared resources (follow the owner protocol): RES-desktopplatform-native-build (append): The vcpkg baseline and overlay ports change only through a dependency-admission change with licence and provenance receipts; each native family adds its own CMake targets and workflow entries; triplet or port changes are rebased and rebuilt by their author; CPU-heavy native builds use the workstation build slot.; RES-workstation-build-slot (exclusive): Exclusive per workstation for the duration of each CPU-heavy local build or test, through the workstation lock rather than a Plan lease: run the command as `python tools/delivery.py build-slot run --worker <name> --task <task> -- <command>` with the Plan repository tool, which holds the lock directory `.arcforges/build-slot` in the user profile with an owner record and heartbeat and recovers a lock whose holder stopped. Coding and review continue while a build waits; CI capacity is not limited by this rule.
Unblocks: NAT.20, NAT.30, SLATE.04, SLATE.15

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Known two-frame seek, malformed input, B-frame/drain, tiled copy, exact audio sample bounds, repeated cancel/close against the actual FFmpeg dependency build; sanitiser build for parser paths (SB-03/SB-04)
Completion evidence for the ledger: Media reader/probe/frame/seek: behavioral, failure and package evidence
Notes: Shares the arcmedia-ffmpeg-abi library/target with NAT.08 (writer/convert/resample) and NAT.09 (audio) -- see 'shared' entries. All three can be developed in parallel branches but should merge sequentially.
```

```text
Execute ArcForges delivery task NAT.08 — Media family: convert, resample and media writer.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\native.md (anchor task-nat-08).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/nat-08 (python tools/delivery.py claim NAT.08 --worker <name>); task branch task/nat-08 in DesktopPlatform; ledger record ledger/tasks/nat-08.md.
Kind/size: producer/M. Baseline: not-started.
Outcome: arc_media_video_convert, arc_media_resampler_* and arc_media_writer_* implemented with the fixed portable profiles (FFV1/PCM/WAV, MP4 MPEG4-AAC); resampler delay/PTS preserved; writer commits only after complete output/sidecars/hash.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-13.07 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\13-high-risk-technical-probes.md, anchor rule-wp-13.07
- WP-13:ss1-nd-05-probe-scaffolds-13-00-13-03-ar SS1/ND-05: probe scaffolds (13.00-13.03) are cleanup-or-regression-fixture; production 13.05-13.16 code is retained and maintained -- different lifecycle rules for the two groups even though both may live under similar directories (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\13-high-risk-technical-probes.md, package-level obligation
- WP-13:ss4-major-types-note-no-native-pointer-b SS4 major-types note: no native pointer becomes a managed domain identifier or a wire field (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\13-high-risk-technical-probes.md, package-level obligation

Entry condition: adoption slice ADOPT.02.native is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] NAT.06: compiled common ABI headers/layouts (arc_video_convert_v1, arc_audio_convert_v1, arc_writer_options_v1)
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:native/arcmedia-ffmpeg-abi/src/**; DesktopPlatform:native/arcmedia-ffmpeg-abi/include/**; DesktopPlatform:native/arcmedia-ffmpeg-abi/tests/**; DesktopPlatform:src/Native/ArcForges.Native.Media/**
Shared resources (follow the owner protocol): RES-desktopplatform-native-build (append): The vcpkg baseline and overlay ports change only through a dependency-admission change with licence and provenance receipts; each native family adds its own CMake targets and workflow entries; triplet or port changes are rebased and rebuilt by their author; CPU-heavy native builds use the workstation build slot.; RES-workstation-build-slot (exclusive): Exclusive per workstation for the duration of each CPU-heavy local build or test, through the workstation lock rather than a Plan lease: run the command as `python tools/delivery.py build-slot run --worker <name> --task <task> -- <command>` with the Plan repository tool, which holds the lock directory `.arcforges/build-slot` in the user profile with an owner record and heartbeat and recovers a lock whose holder stopped. Coding and review continue while a build waits; CI capacity is not limited by this rule.
Unblocks: NAT.20, NAT.30, SLATE.15, SLATE.19, SLATE.20, SLATE.21, SLATE.27, SLATE.28

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Independent fresh decode of FFV1/PCM/WAV and MP4 MPEG4-AAC; resample length, finish-twice, cancel/abort, disk-full corruption rejection
Completion evidence for the ledger: Convert, resample and media writer: behavioral, failure and package evidence
Notes: Does not functionally require NAT.07 (arc_media_buffer_create can construct input buffers directly per the ABI doc), only the shared-file contention noted above.
```

```text
Execute ArcForges delivery task NAT.09 — Media family: audio devices (miniaudio).

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\native.md (anchor task-nat-09).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/nat-09 (python tools/delivery.py claim NAT.09 --worker <name>); task branch task/nat-09 in DesktopPlatform; ledger record ledger/tasks/nat-09.md.
Kind/size: producer/M. Baseline: not-started.
Outcome: arc_media_audio_* implemented over miniaudio device/context/ring primitives with explicit negotiation, bounded rings, counters, disconnect/reopen; missing output device permits video-only playback with a stated reason without blocking offline export.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-13.08 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\13-high-risk-technical-probes.md, anchor rule-wp-13.08
- WP-13:ss1-nd-05-probe-scaffolds-13-00-13-03-ar SS1/ND-05: probe scaffolds (13.00-13.03) are cleanup-or-regression-fixture; production 13.05-13.16 code is retained and maintained -- different lifecycle rules for the two groups even though both may live under similar directories (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\13-high-risk-technical-probes.md, package-level obligation
- WP-13:ss4-major-types-note-no-native-pointer-b SS4 major-types note: no native pointer becomes a managed domain identifier or a wire field (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\13-high-risk-technical-probes.md, package-level obligation

Entry condition: adoption slice ADOPT.02.native is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] NAT.06: compiled common ABI headers/layouts (arc_device_options_v1, arc_device_state_v1)
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:native/arcmedia-ffmpeg-abi/src/**; DesktopPlatform:native/arcmedia-ffmpeg-abi/include/**; DesktopPlatform:native/arcmedia-ffmpeg-abi/tests/**; DesktopPlatform:src/Native/ArcForges.Native.Media/**
Shared resources (follow the owner protocol): RES-desktopplatform-native-build (append): The vcpkg baseline and overlay ports change only through a dependency-admission change with licence and provenance receipts; each native family adds its own CMake targets and workflow entries; triplet or port changes are rebased and rebuilt by their author; CPU-heavy native builds use the workstation build slot.; RES-workstation-build-slot (exclusive): Exclusive per workstation for the duration of each CPU-heavy local build or test, through the workstation lock rather than a Plan lease: run the command as `python tools/delivery.py build-slot run --worker <name> --task <task> -- <command>` with the Plan repository tool, which holds the lock directory `.arcforges/build-slot` in the user profile with an owner record and heartbeat and recovers a lock whose holder stopped. Coding and review continue while a build waits; CI capacity is not limited by this rule.
Unblocks: NAT.20, NAT.30

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Physical output/input, underflow, overflow, device loss, exclusive-use refusal, no-device video clock, offline render -- physical audio hardware is ordinary (most dev machines have one), not a scarce PG-08 lab resource
Completion evidence for the ledger: Audio devices: behavioral, failure and package evidence
Notes: Independent of NAT.07/08 functionally; shares the same target/export files.
```

```text
Execute ArcForges delivery task NAT.10 — Colour family: OCIO transforms.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\native.md (anchor task-nat-10).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/nat-10 (python tools/delivery.py claim NAT.10 --worker <name>); task branch task/nat-10 in DesktopPlatform; ledger record ledger/tasks/nat-10.md.
Kind/size: producer/M. Baseline: not-started.
Outcome: arc_color_* implemented with immutable OCIO config/processor assets and alpha-correct CPU transforms; no ambient file/network config lookup; named refusal of invalid transforms.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-13.09 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\13-high-risk-technical-probes.md, anchor rule-wp-13.09
- WP-13:ss1-nd-05-probe-scaffolds-13-00-13-03-ar SS1/ND-05: probe scaffolds (13.00-13.03) are cleanup-or-regression-fixture; production 13.05-13.16 code is retained and maintained -- different lifecycle rules for the two groups even though both may live under similar directories (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\13-high-risk-technical-probes.md, package-level obligation
- WP-13:ss4-major-types-note-no-native-pointer-b SS4 major-types note: no native pointer becomes a managed domain identifier or a wire field (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\13-high-risk-technical-probes.md, package-level obligation

Entry condition: adoption slice ADOPT.02.native is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] NAT.06: compiled common ABI headers/layouts (arc_colour_options_v1)
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:native/arcslate-color-abi/**; DesktopPlatform:src/Native/ArcForges.Native.Colour/**
Shared resources (follow the owner protocol): RES-desktopplatform-native-build (append): The vcpkg baseline and overlay ports change only through a dependency-admission change with licence and provenance receipts; each native family adds its own CMake targets and workflow entries; triplet or port changes are rebased and rebuilt by their author; CPU-heavy native builds use the workstation build slot.; RES-workstation-build-slot (exclusive): Exclusive per workstation for the duration of each CPU-heavy local build or test, through the workstation lock rather than a Plan lease: run the command as `python tools/delivery.py build-slot run --worker <name> --task <task> -- <command>` with the Plan repository tool, which holds the lock directory `.arcforges/build-slot` in the user profile with an owner record and heartbeat and recovers a lock whose holder stopped. Coding and review continue while a build waits; CI capacity is not limited by this rule.
Unblocks: NAT.21, NAT.30, SLATE.24

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Independent RGB/alpha vectors, alpha 0, unknown space, tampered bundle, preview/render agreement
Completion evidence for the ledger: Colour transforms: behavioral, failure and package evidence
Notes: Independent native library from Media -- no shared-file contention with NAT.07-09. Parallel with NAT.11/12/13/14/15.
```

```text
Execute ArcForges delivery task NAT.11 — Image family: still-image codecs (PNG/TIFF/EXR).

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\native.md (anchor task-nat-11).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/nat-11 (python tools/delivery.py claim NAT.11 --worker <name>); task branch task/nat-11 in DesktopPlatform; ledger record ledger/tasks/nat-11.md.
Kind/size: producer/M. Baseline: not-started.
Outcome: arc_image_* implemented with PNG/TIFF/EXR metadata and bounded tile reads/writes via OIIO/OpenEXR/Imath; hostile reads execute only in the WP11 helper.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-13.10 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\13-high-risk-technical-probes.md, anchor rule-wp-13.10
- WP-13:ss1-nd-05-probe-scaffolds-13-00-13-03-ar SS1/ND-05: probe scaffolds (13.00-13.03) are cleanup-or-regression-fixture; production 13.05-13.16 code is retained and maintained -- different lifecycle rules for the two groups even though both may live under similar directories (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\13-high-risk-technical-probes.md, package-level obligation
- WP-13:ss4-major-types-note-no-native-pointer-b SS4 major-types note: no native pointer becomes a managed domain identifier or a wire field (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\13-high-risk-technical-probes.md, package-level obligation

Entry condition: adoption slice ADOPT.02.native is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] NAT.06: compiled common ABI headers/layouts (arc_image_options_v1, arc_region_v1)
- [artifact] PLT.45: published ContentSandbox.Contracts/Broker/foundation Runtime.<rid>
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:native/arcslate-image-abi/**; DesktopPlatform:src/Native/ArcForges.Native.Image/**
Shared resources (follow the owner protocol): RES-desktopplatform-native-build (append): The vcpkg baseline and overlay ports change only through a dependency-admission change with licence and provenance receipts; each native family adds its own CMake targets and workflow entries; triplet or port changes are rebased and rebuilt by their author; CPU-heavy native builds use the workstation build slot.; RES-workstation-build-slot (exclusive): Exclusive per workstation for the duration of each CPU-heavy local build or test, through the workstation lock rather than a Plan lease: run the command as `python tools/delivery.py build-slot run --worker <name> --task <task> -- <command>` with the Plan repository tool, which holds the lock directory `.arcforges/build-slot` in the user profile with an owner record and heartbeat and recovers a lock whose holder stopped. Coding and review continue while a build waits; CI capacity is not limited by this rule.
Unblocks: NAT.22, NAT.30, SLATE.21

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Bit depth/metadata round trip, edge tiles, decompression bomb, failed codec, incomplete-output refusal
Completion evidence for the ledger: Still-image codecs: behavioral, failure and package evidence
Notes: Consumed by both ArcSlate (stills) and ArcNotes (attachment images) per the platform matrix SS3.2 slot table.
```

```text
Execute ArcForges delivery task NAT.12 — Otio family: OTIO0.18.1 interchange.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\native.md (anchor task-nat-12).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/nat-12 (python tools/delivery.py claim NAT.12 --worker <name>); task branch task/nat-12 in DesktopPlatform; ledger record ledger/tasks/nat-12.md.
Kind/size: producer/L. Baseline: not-started.
Outcome: arc_otio_read/write implemented under the official OTIO0.18.1 library with the selected schema allowlist and fidelity report; exact tick conversion preserved; unsupported schema/malicious path/parser-death cases reported as loss before commit, never silently.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-13.11 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\13-high-risk-technical-probes.md, anchor rule-wp-13.11
- WP-13:ss1-nd-05-probe-scaffolds-13-00-13-03-ar SS1/ND-05: probe scaffolds (13.00-13.03) are cleanup-or-regression-fixture; production 13.05-13.16 code is retained and maintained -- different lifecycle rules for the two groups even though both may live under similar directories (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\13-high-risk-technical-probes.md, package-level obligation
- WP-13:ss4-major-types-note-no-native-pointer-b SS4 major-types note: no native pointer becomes a managed domain identifier or a wire field (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\13-high-risk-technical-probes.md, package-level obligation

Entry condition: adoption slice ADOPT.02.native is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] NAT.06: compiled common ABI headers/layouts (arc_io_v1)
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:native/arcslate-otio-abi/**; DesktopPlatform:src/Native/ArcForges.Native.Otio/**
Shared resources (follow the owner protocol): RES-desktopplatform-native-build (append): The vcpkg baseline and overlay ports change only through a dependency-admission change with licence and provenance receipts; each native family adds its own CMake targets and workflow entries; triplet or port changes are rebased and rebuilt by their author; CPU-heavy native builds use the workstation build slot.; RES-workstation-build-slot (exclusive): Exclusive per workstation for the duration of each CPU-heavy local build or test, through the workstation lock rather than a Plan lease: run the command as `python tools/delivery.py build-slot run --worker <name> --task <task> -- <command>` with the Plan repository tool, which holds the lock directory `.arcforges/build-slot` in the user profile with an owner record and heartbeat and recovers a lock whose holder stopped. Coding and review continue while a build waits; CI capacity is not limited by this rule.
Unblocks: NAT.23, NAT.30, SLATE.38, SLATE.39

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Mixed/fractional rate round trip, unsupported schema, malicious path, parser death, reported loss before commit -- PG-15 evidence class
Completion evidence for the ledger: OTIO interchange: behavioral, failure and package evidence
Notes: PG-15 (OTIO bidirectional evidence, owned by the ArcSlate lane WP-39.05) consumes this task's output as its real-fixture producer.
```

```text
Execute ArcForges delivery task NAT.13 — Instruments family: serial and USB devices (NEW library).

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\native.md (anchor task-nat-13).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/nat-13 (python tools/delivery.py claim NAT.13 --worker <name>); task branch task/nat-13 in DesktopPlatform; ledger record ledger/tasks/nat-13.md.
Kind/size: producer/M. Baseline: not-started.
Outcome: A new arcinstruments-abi native library and ArcForges.Native.Instruments managed package implement arc_instruments_* over generic OS serial and explicit libusb interface/endpoint open/read/write/cancel/close; identity revalidated at open; no auto-detach of unrelated drivers, no vendor SDK.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-13.12 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\13-high-risk-technical-probes.md, anchor rule-wp-13.12
- WP-13:ss1-nd-05-probe-scaffolds-13-00-13-03-ar SS1/ND-05: probe scaffolds (13.00-13.03) are cleanup-or-regression-fixture; production 13.05-13.16 code is retained and maintained -- different lifecycle rules for the two groups even though both may live under similar directories (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\13-high-risk-technical-probes.md, package-level obligation
- WP-13:ss4-major-types-note-no-native-pointer-b SS4 major-types note: no native pointer becomes a managed domain identifier or a wire field (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\13-high-risk-technical-probes.md, package-level obligation

Entry condition: adoption slice ADOPT.02.native is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] NAT.06: compiled common ABI headers/layouts (arc_instrument_options_v1, arc_transfer_v1)
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:native/arcinstruments-abi/**; DesktopPlatform:src/Native/ArcForges.Native.Instruments/**; DesktopPlatform:native/CMakeLists.txt; DesktopPlatform:eng/packaging/packages.json
Shared resources (follow the owner protocol): RES-desktopplatform-native-build (append): The vcpkg baseline and overlay ports change only through a dependency-admission change with licence and provenance receipts; each native family adds its own CMake targets and workflow entries; triplet or port changes are rebased and rebuilt by their author; CPU-heavy native builds use the workstation build slot.; RES-desktopplatform-package-inventory (append): Each producer task adds its own package entry; every merge to main packs and publishes all packages at one version; consumers pin the candidate produced by the merge of the capability they need, never waiting for a package closure task; one merge queue.; RES-workstation-build-slot (exclusive): Exclusive per workstation for the duration of each CPU-heavy local build or test, through the workstation lock rather than a Plan lease: run the command as `python tools/delivery.py build-slot run --worker <name> --task <task> -- <command>` with the Plan repository tool, which holds the lock directory `.arcforges/build-slot` in the user profile with an owner record and heartbeat and recovers a lock whose holder stopped. Coding and review continue while a build waits; CI capacity is not limited by this rule.
Unblocks: NAT.24, NAT.30, SCOPE.04

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Enumeration, explicit interface claim, control/bulk/interrupt transfers, partial writes, cancellation callback, hot unplug, driver absence, permission denial on Tier 1 -- against the PG-08 hardware inventory for the physical-device cases
Completion evidence for the ledger: Serial and USB instruments: behavioral, failure and package evidence
Notes: Degradation-path code (enumeration, driver-absence reporting) does not require the PG-08 lab to exist; the physical hot-unplug/permission-denial matrix against a named USB device does..
```

```text
Execute ArcForges delivery task NAT.14 — Pdf family: PDFium and production parser containment in the WP11 helper (NEW library).

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\native.md (anchor task-nat-14).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/nat-14 (python tools/delivery.py claim NAT.14 --worker <name>); task branch task/nat-14 in DesktopPlatform; ledger record ledger/tasks/nat-14.md.
Kind/size: producer/L. Baseline: not-started.
Outcome: A new arcpdf-abi native library and ArcForges.Native.Pdf managed package implement arc_pdf_* over actual PDFium; PDFium and all approved parser wrappers are composed into the existing WP-11.09 ContentSandbox host using generated local gRPC controls (no second helper, no duplicate DTO owner); the next immutable ContentSandbox.Runtime.<rid> version is published; test-parser production registration is removed (hostile regression fixture retained). Contributes real evidence to PG-12 and PG-22.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-13.13 (all work except the parts mapped to PLT.54): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\13-high-risk-technical-probes.md, anchor rule-wp-13.13
- WP-13:ss1-nd-05-probe-scaffolds-13-00-13-03-ar SS1/ND-05: probe scaffolds (13.00-13.03) are cleanup-or-regression-fixture; production 13.05-13.16 code is retained and maintained -- different lifecycle rules for the two groups even though both may live under similar directories (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\13-high-risk-technical-probes.md, package-level obligation
- WP-13:ss4-major-types-note-no-native-pointer-b SS4 major-types note: no native pointer becomes a managed domain identifier or a wire field (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\13-high-risk-technical-probes.md, package-level obligation

Entry condition: adoption slice ADOPT.02.native is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] PLT.45: published ArcForges.ContentSandbox.Contracts,.Broker and the foundation Runtime.<rid> package (built around a deliberately hostile first-party TEST parser)
- [artifact] NAT.06: compiled common ABI headers/layouts (arc_pdf_page_v1)
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:native/arcpdf-abi/**; DesktopPlatform:src/Native/ArcForges.Native.Pdf/**; DesktopPlatform:src/DesktopHelpers/ArcForges.ContentSandbox/**; DesktopPlatform:native/CMakeLists.txt; DesktopPlatform:eng/packaging/packages.json
Shared resources (follow the owner protocol): RES-desktopplatform-native-build (append): The vcpkg baseline and overlay ports change only through a dependency-admission change with licence and provenance receipts; each native family adds its own CMake targets and workflow entries; triplet or port changes are rebased and rebuilt by their author; CPU-heavy native builds use the workstation build slot.; RES-desktopplatform-package-inventory (append): Each producer task adds its own package entry; every merge to main packs and publishes all packages at one version; consumers pin the candidate produced by the merge of the capability they need, never waiting for a package closure task; one merge queue.; RES-workstation-build-slot (exclusive): Exclusive per workstation for the duration of each CPU-heavy local build or test, through the workstation lock rather than a Plan lease: run the command as `python tools/delivery.py build-slot run --worker <name> --task <task> -- <command>` with the Plan repository tool, which holds the lock directory `.arcforges/build-slot` in the user profile with an owner record and heartbeat and recovers a lock whose holder stopped. Coding and review continue while a build waits; CI capacity is not limited by this rule.
Permitted substitutes (never real integration evidence): SUB-hostile-test-parser: OS-level containment mechanics only (AppContainer/Job Object, Landlock/seccomp, App-Sandbox/XPC denial, resource bounds, crash/hang/parent-death cleanup) against a deliberately hostile FIRST-PARTY test parser, not real format-parsing correctness Real producer ['NAT.14']; removed by PLT.54
Unblocks: NAT.25, NAT.30, NOTES.09, NOTES.37, PLT.45, PLT.54, SLATE.04, SLATE.16

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Packaged PDF page/text/tile fixtures, malformed/native-crash/hang and parent-death cleanup on every admitted RID; rerun of actual image/media/OTIO parser containment (not just PDF)
Completion evidence for the ledger: Actual PDF dependency and containment evidence contributing to PG-12; PG-22 runtime evidence for the real-parser leg (11.09 supplies the mechanism leg)
Notes: Highest residual security-relevant risk of the seven native families (hostile content inside a real isolation boundary) -- flagged as an early risk proof even though it is scheduled after NAT.06, unlike WP13's four canonical probes.
```

```text
Execute ArcForges delivery task NAT.15 — Graphics family: portable CPU surface and optional OS backends (NEW library).

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\native.md (anchor task-nat-15).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/nat-15 (python tools/delivery.py claim NAT.15 --worker <name>); task branch task/nat-15 in DesktopPlatform; ledger record ledger/tasks/nat-15.md.
Kind/size: producer/M. Baseline: not-started.
Outcome: A new arcgraphics-abi native library and ArcForges.Native.Graphics managed package implement ArcGraphicsNative CPU surface/upload/present/fence/device-loss behavior on all admitted RIDs; the existing arcgraphics-metal-abi probe ABI is preserved unchanged as a private optional backend, not claimed as functional acceleration by itself.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-13.14 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\13-high-risk-technical-probes.md, anchor rule-wp-13.14
- WP-13:ss1-nd-05-probe-scaffolds-13-00-13-03-ar SS1/ND-05: probe scaffolds (13.00-13.03) are cleanup-or-regression-fixture; production 13.05-13.16 code is retained and maintained -- different lifecycle rules for the two groups even though both may live under similar directories (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\13-high-risk-technical-probes.md, package-level obligation
- WP-13:ss4-major-types-note-no-native-pointer-b SS4 major-types note: no native pointer becomes a managed domain identifier or a wire field (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\13-high-risk-technical-probes.md, package-level obligation

Entry condition: adoption slice ADOPT.02.native is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] NAT.06: compiled common ABI headers/layouts (arc_surface_options_v1, arc_region_v1)
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:native/arcgraphics-abi/**; DesktopPlatform:src/Native/ArcForges.Native.Graphics/**; DesktopPlatform:native/CMakeLists.txt; DesktopPlatform:eng/packaging/packages.json
Shared resources (follow the owner protocol): RES-desktopplatform-native-build (append): The vcpkg baseline and overlay ports change only through a dependency-admission change with licence and provenance receipts; each native family adds its own CMake targets and workflow entries; triplet or port changes are rebased and rebuilt by their author; CPU-heavy native builds use the workstation build slot.; RES-desktopplatform-package-inventory (append): Each producer task adds its own package entry; every merge to main packs and publishes all packages at one version; consumers pin the candidate produced by the merge of the capability they need, never waiting for a package closure task; one merge queue.; RES-workstation-build-slot (exclusive): Exclusive per workstation for the duration of each CPU-heavy local build or test, through the workstation lock rather than a Plan lease: run the command as `python tools/delivery.py build-slot run --worker <name> --task <task> -- <command>` with the Plan repository tool, which holds the lock directory `.arcforges/build-slot` in the user profile with an owner record and heartbeat and recovers a lock whose holder stopped. Coding and review continue while a build waits; CI capacity is not limited by this rule.
Unblocks: NAT.26, NAT.30, SLATE.19, SLATE.22, SLATE.25

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): CPU display/readback, ownership and fence lifetime, device loss and forced software path; each advertised accelerator exercised with its actual driver where locally available
Completion evidence for the ledger: Portable graphics and optional OS backends: behavioral, failure and package evidence
Notes: Consumed by both ArcSlate (preview surface) and ArcScope (live-view surface).
```

```text
Execute ArcForges delivery task NAT.20 — Media package production: all 6 RIDs.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\native.md (anchor task-nat-20).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/nat-20 (python tools/delivery.py claim NAT.20 --worker <name>); task branch task/nat-20 in DesktopPlatform; ledger record ledger/tasks/nat-20.md.
Kind/size: producer/M. Baseline: not-started.
Outcome: ArcForges.Native.Media.Runtime.<rid> published for win-x64, win-arm64, osx-arm64, osx-x64, linux-x64, linux-arm64 with matched tested bytes, headers/import libraries, native manifests and complete dependency closures; isolated clean-cache C17 and C# AOT consumers pass on each admitted RID.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-13.15 (ArcForges.Native.Media + Runtime.<rid> only): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\13-high-risk-technical-probes.md, anchor rule-wp-13.15
- WP-13:producer-artifacts-and-integration-md-wp producer-artifacts-and-integration.md WP13 row: 'Probe-only 1.0, missing functional export or dependency prevents completion' (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\13-high-risk-technical-probes.md, package-level obligation

Entry condition: adoption slice ADOPT.02.native is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] NAT.07: complete arc_media_reader_* export set
- [artifact] NAT.08: complete arc_media_writer_*/convert/resample export set
- [artifact] NAT.09: complete arc_media_audio_* export set
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:src/Native/ArcForges.Native.Media.Runtime.win-arm64/**; DesktopPlatform:src/Native/ArcForges.Native.Media.Runtime.osx-arm64/**; DesktopPlatform:src/Native/ArcForges.Native.Media.Runtime.osx-x64/**; DesktopPlatform:src/Native/ArcForges.Native.Media.Runtime.linux-x64/**; DesktopPlatform:src/Native/ArcForges.Native.Media.Runtime.linux-arm64/**; DesktopPlatform:eng/packaging/packages.json
Shared resources (follow the owner protocol): RES-desktopplatform-native-build (append): The vcpkg baseline and overlay ports change only through a dependency-admission change with licence and provenance receipts; each native family adds its own CMake targets and workflow entries; triplet or port changes are rebased and rebuilt by their author; CPU-heavy native builds use the workstation build slot.; RES-desktopplatform-package-inventory (append): Each producer task adds its own package entry; every merge to main packs and publishes all packages at one version; consumers pin the candidate produced by the merge of the capability they need, never waiting for a package closure task; one merge queue.; RES-workstation-build-slot (exclusive): Exclusive per workstation for the duration of each CPU-heavy local build or test, through the workstation lock rather than a Plan lease: run the command as `python tools/delivery.py build-slot run --worker <name> --task <task> -- <command>` with the Plan repository tool, which holds the lock directory `.arcforges/build-slot` in the user profile with an owner record and heartbeat and recovers a lock whose holder stopped. Coding and review continue while a build waits; CI capacity is not limited by this rule.
Unblocks: NAT.28, NAT.30

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Clean-cache C17 and C# AOT consumers per RID; missing/transitive/wrong-RID library, hash collision, absent export, revoked artifact, source-unavailable negatives
Completion evidence for the ledger: Immutable native package production: behavioral, failure and package evidence (Media slice)
Notes: Win-x64 leg can start as soon as NAT.07-09 land; win-arm64/osx-arm64/osx-x64/linux-x64/linux-arm64 legs are independent of each other and could be sub-split further if the integration owner wants finer parallelism (Tier-1 RIDs win-x64/osx-arm64/linux-x64 vs Tier-2 win-arm64/osx-x64/linux-arm64).
```

```text
Execute ArcForges delivery task NAT.21 — Colour package production: all 6 RIDs.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\native.md (anchor task-nat-21).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/nat-21 (python tools/delivery.py claim NAT.21 --worker <name>); task branch task/nat-21 in DesktopPlatform; ledger record ledger/tasks/nat-21.md.
Kind/size: producer/S. Baseline: not-started.
Outcome: ArcForges.Native.Colour.Runtime.<rid> published for all 6 RIDs with matched tested bytes/headers/manifests/dependency closures.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-13.15 (ArcForges.Native.Colour + Runtime.<rid> only): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\13-high-risk-technical-probes.md, anchor rule-wp-13.15
- WP-13:producer-artifacts-and-integration-md-wp producer-artifacts-and-integration.md WP13 row: 'Probe-only 1.0, missing functional export or dependency prevents completion' (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\13-high-risk-technical-probes.md, package-level obligation

Entry condition: adoption slice ADOPT.02.native is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] NAT.10: complete arc_color_* export set
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:src/Native/ArcForges.Native.Colour.Runtime.win-arm64/**; DesktopPlatform:src/Native/ArcForges.Native.Colour.Runtime.osx-arm64/**; DesktopPlatform:src/Native/ArcForges.Native.Colour.Runtime.osx-x64/**; DesktopPlatform:src/Native/ArcForges.Native.Colour.Runtime.linux-x64/**; DesktopPlatform:src/Native/ArcForges.Native.Colour.Runtime.linux-arm64/**; DesktopPlatform:eng/packaging/packages.json
Shared resources (follow the owner protocol): RES-desktopplatform-native-build (append): The vcpkg baseline and overlay ports change only through a dependency-admission change with licence and provenance receipts; each native family adds its own CMake targets and workflow entries; triplet or port changes are rebased and rebuilt by their author; CPU-heavy native builds use the workstation build slot.; RES-desktopplatform-package-inventory (append): Each producer task adds its own package entry; every merge to main packs and publishes all packages at one version; consumers pin the candidate produced by the merge of the capability they need, never waiting for a package closure task; one merge queue.; RES-workstation-build-slot (exclusive): Exclusive per workstation for the duration of each CPU-heavy local build or test, through the workstation lock rather than a Plan lease: run the command as `python tools/delivery.py build-slot run --worker <name> --task <task> -- <command>` with the Plan repository tool, which holds the lock directory `.arcforges/build-slot` in the user profile with an owner record and heartbeat and recovers a lock whose holder stopped. Coding and review continue while a build waits; CI capacity is not limited by this rule.
Unblocks: NAT.28, NAT.30

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Clean-cache C17/C# AOT consumers per RID; same negative matrix as NAT.20
Completion evidence for the ledger: Immutable native package production: behavioral, failure and package evidence (Colour slice)
Notes: Independent of NAT.20/22-26 (different package identity, disjoint writes except the shared allowlist/vcpkg pin).
```

```text
Execute ArcForges delivery task NAT.22 — Image package production: all 6 RIDs.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\native.md (anchor task-nat-22).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/nat-22 (python tools/delivery.py claim NAT.22 --worker <name>); task branch task/nat-22 in DesktopPlatform; ledger record ledger/tasks/nat-22.md.
Kind/size: producer/S. Baseline: not-started.
Outcome: ArcForges.Native.Image.Runtime.<rid> published for all 6 RIDs with matched tested bytes/headers/manifests/dependency closures.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-13.15 (ArcForges.Native.Image + Runtime.<rid> only): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\13-high-risk-technical-probes.md, anchor rule-wp-13.15
- WP-13:producer-artifacts-and-integration-md-wp producer-artifacts-and-integration.md WP13 row: 'Probe-only 1.0, missing functional export or dependency prevents completion' (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\13-high-risk-technical-probes.md, package-level obligation

Entry condition: adoption slice ADOPT.02.native is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] NAT.11: complete arc_image_* export set
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:src/Native/ArcForges.Native.Image.Runtime.win-arm64/**; DesktopPlatform:src/Native/ArcForges.Native.Image.Runtime.osx-arm64/**; DesktopPlatform:src/Native/ArcForges.Native.Image.Runtime.osx-x64/**; DesktopPlatform:src/Native/ArcForges.Native.Image.Runtime.linux-x64/**; DesktopPlatform:src/Native/ArcForges.Native.Image.Runtime.linux-arm64/**; DesktopPlatform:eng/packaging/packages.json
Shared resources (follow the owner protocol): RES-desktopplatform-native-build (append): The vcpkg baseline and overlay ports change only through a dependency-admission change with licence and provenance receipts; each native family adds its own CMake targets and workflow entries; triplet or port changes are rebased and rebuilt by their author; CPU-heavy native builds use the workstation build slot.; RES-desktopplatform-package-inventory (append): Each producer task adds its own package entry; every merge to main packs and publishes all packages at one version; consumers pin the candidate produced by the merge of the capability they need, never waiting for a package closure task; one merge queue.; RES-workstation-build-slot (exclusive): Exclusive per workstation for the duration of each CPU-heavy local build or test, through the workstation lock rather than a Plan lease: run the command as `python tools/delivery.py build-slot run --worker <name> --task <task> -- <command>` with the Plan repository tool, which holds the lock directory `.arcforges/build-slot` in the user profile with an owner record and heartbeat and recovers a lock whose holder stopped. Coding and review continue while a build waits; CI capacity is not limited by this rule.
Unblocks: NAT.28, NAT.30

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Clean-cache C17/C# AOT consumers per RID; same negative matrix as NAT.20
Completion evidence for the ledger: Immutable native package production: behavioral, failure and package evidence (Image slice)
Notes: Independent of the other packaging tasks.
```

```text
Execute ArcForges delivery task NAT.23 — Otio package production: all 6 RIDs.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\native.md (anchor task-nat-23).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/nat-23 (python tools/delivery.py claim NAT.23 --worker <name>); task branch task/nat-23 in DesktopPlatform; ledger record ledger/tasks/nat-23.md.
Kind/size: producer/S. Baseline: not-started.
Outcome: ArcForges.Native.Otio.Runtime.<rid> published for all 6 RIDs with matched tested bytes/headers/manifests/dependency closures.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-13.15 (ArcForges.Native.Otio + Runtime.<rid> only): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\13-high-risk-technical-probes.md, anchor rule-wp-13.15
- WP-13:producer-artifacts-and-integration-md-wp producer-artifacts-and-integration.md WP13 row: 'Probe-only 1.0, missing functional export or dependency prevents completion' (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\13-high-risk-technical-probes.md, package-level obligation

Entry condition: adoption slice ADOPT.02.native is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] NAT.12: complete arc_otio_* export set
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:src/Native/ArcForges.Native.Otio.Runtime.win-arm64/**; DesktopPlatform:src/Native/ArcForges.Native.Otio.Runtime.osx-arm64/**; DesktopPlatform:src/Native/ArcForges.Native.Otio.Runtime.osx-x64/**; DesktopPlatform:src/Native/ArcForges.Native.Otio.Runtime.linux-x64/**; DesktopPlatform:src/Native/ArcForges.Native.Otio.Runtime.linux-arm64/**; DesktopPlatform:eng/packaging/packages.json
Shared resources (follow the owner protocol): RES-desktopplatform-native-build (append): The vcpkg baseline and overlay ports change only through a dependency-admission change with licence and provenance receipts; each native family adds its own CMake targets and workflow entries; triplet or port changes are rebased and rebuilt by their author; CPU-heavy native builds use the workstation build slot.; RES-desktopplatform-package-inventory (append): Each producer task adds its own package entry; every merge to main packs and publishes all packages at one version; consumers pin the candidate produced by the merge of the capability they need, never waiting for a package closure task; one merge queue.; RES-workstation-build-slot (exclusive): Exclusive per workstation for the duration of each CPU-heavy local build or test, through the workstation lock rather than a Plan lease: run the command as `python tools/delivery.py build-slot run --worker <name> --task <task> -- <command>` with the Plan repository tool, which holds the lock directory `.arcforges/build-slot` in the user profile with an owner record and heartbeat and recovers a lock whose holder stopped. Coding and review continue while a build waits; CI capacity is not limited by this rule.
Unblocks: NAT.28, NAT.30

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Clean-cache C17/C# AOT consumers per RID; same negative matrix as NAT.20
Completion evidence for the ledger: Immutable native package production: behavioral, failure and package evidence (Otio slice)
Notes: Independent of the other packaging tasks.
```

```text
Execute ArcForges delivery task NAT.24 — Instruments package production: all 6 RIDs.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\native.md (anchor task-nat-24).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/nat-24 (python tools/delivery.py claim NAT.24 --worker <name>); task branch task/nat-24 in DesktopPlatform; ledger record ledger/tasks/nat-24.md.
Kind/size: producer/S. Baseline: not-started.
Outcome: ArcForges.Native.Instruments.Runtime.<rid> published for all 6 RIDs.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-13.15 (ArcForges.Native.Instruments + Runtime.<rid> only): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\13-high-risk-technical-probes.md, anchor rule-wp-13.15
- WP-13:producer-artifacts-and-integration-md-wp producer-artifacts-and-integration.md WP13 row: 'Probe-only 1.0, missing functional export or dependency prevents completion' (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\13-high-risk-technical-probes.md, package-level obligation

Entry condition: adoption slice ADOPT.02.native is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] NAT.13: complete arc_instruments_* export set
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:src/Native/ArcForges.Native.Instruments.Runtime.*/**; DesktopPlatform:eng/packaging/packages.json
Shared resources (follow the owner protocol): RES-desktopplatform-native-build (append): The vcpkg baseline and overlay ports change only through a dependency-admission change with licence and provenance receipts; each native family adds its own CMake targets and workflow entries; triplet or port changes are rebased and rebuilt by their author; CPU-heavy native builds use the workstation build slot.; RES-desktopplatform-package-inventory (append): Each producer task adds its own package entry; every merge to main packs and publishes all packages at one version; consumers pin the candidate produced by the merge of the capability they need, never waiting for a package closure task; one merge queue.; RES-workstation-build-slot (exclusive): Exclusive per workstation for the duration of each CPU-heavy local build or test, through the workstation lock rather than a Plan lease: run the command as `python tools/delivery.py build-slot run --worker <name> --task <task> -- <command>` with the Plan repository tool, which holds the lock directory `.arcforges/build-slot` in the user profile with an owner record and heartbeat and recovers a lock whose holder stopped. Coding and review continue while a build waits; CI capacity is not limited by this rule.
Unblocks: NAT.28, NAT.30, SCOPE.11

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Clean-cache C17/C# AOT consumers per RID; same negative matrix as NAT.20
Completion evidence for the ledger: Immutable native package production: behavioral, failure and package evidence (Instruments slice)
Notes: First RID (win-x64) is the realistic starting point given libusb Windows support is best-understood; other RIDs follow.
```

```text
Execute ArcForges delivery task NAT.25 — Pdf package production: all 6 RIDs + ContentSandbox Runtime.<rid> composition.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\native.md (anchor task-nat-25).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/nat-25 (python tools/delivery.py claim NAT.25 --worker <name>); task branch task/nat-25 in DesktopPlatform; ledger record ledger/tasks/nat-25.md.
Kind/size: producer/M. Baseline: not-started.
Outcome: ArcForges.Native.Pdf.Runtime.<rid> published for all 6 RIDs; the composed ContentSandbox.Runtime.<rid> (real parser closure) is rebuilt/signed once and published as the next immutable version per admitted RID.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-13.15 (ArcForges.Native.Pdf + Runtime.<rid>, plus the ContentSandbox.Runtime.<rid> republication from 13.13): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\13-high-risk-technical-probes.md, anchor rule-wp-13.15
- WP-13:producer-artifacts-and-integration-md-wp producer-artifacts-and-integration.md WP13 row: 'Probe-only 1.0, missing functional export or dependency prevents completion' (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\13-high-risk-technical-probes.md, package-level obligation

Entry condition: adoption slice ADOPT.02.native is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] NAT.14: complete arc_pdf_* export set and the composed ContentSandbox parser registration
- [artifact] PLT.45: the WP11-owned host/broker/launcher mechanics stay the versioning authority for ContentSandbox.Runtime identity
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:src/Native/ArcForges.Native.Pdf.Runtime.*/**; DesktopPlatform:src/DesktopHelpers/ArcForges.ContentSandbox/**; DesktopPlatform:eng/packaging/packages.json
Shared resources (follow the owner protocol): RES-desktopplatform-native-build (append): The vcpkg baseline and overlay ports change only through a dependency-admission change with licence and provenance receipts; each native family adds its own CMake targets and workflow entries; triplet or port changes are rebased and rebuilt by their author; CPU-heavy native builds use the workstation build slot.; RES-desktopplatform-package-inventory (append): Each producer task adds its own package entry; every merge to main packs and publishes all packages at one version; consumers pin the candidate produced by the merge of the capability they need, never waiting for a package closure task; one merge queue.; RES-workstation-build-slot (exclusive): Exclusive per workstation for the duration of each CPU-heavy local build or test, through the workstation lock rather than a Plan lease: run the command as `python tools/delivery.py build-slot run --worker <name> --task <task> -- <command>` with the Plan repository tool, which holds the lock directory `.arcforges/build-slot` in the user profile with an owner record and heartbeat and recovers a lock whose holder stopped. Coding and review continue while a build waits; CI capacity is not limited by this rule.
Unblocks: NAT.28, NAT.30, NOTES.37

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Clean-cache C17/C# AOT consumers per RID; PG-22 hostile-parser containment re-run at package level (not just source level)
Completion evidence for the ledger: Immutable native package production: behavioral, failure and package evidence (Pdf slice); PG-12 contribution
Notes: Depends on NAT.14 landing first (unlike the other packaging tasks, this one also republishes the shared ContentSandbox helper, so it is more tightly sequenced).
```

```text
Execute ArcForges delivery task NAT.26 — Graphics package production: all 6 RIDs.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\native.md (anchor task-nat-26).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/nat-26 (python tools/delivery.py claim NAT.26 --worker <name>); task branch task/nat-26 in DesktopPlatform; ledger record ledger/tasks/nat-26.md.
Kind/size: producer/S. Baseline: not-started.
Outcome: ArcForges.Native.Graphics.Runtime.<rid> published for all 6 RIDs, CPU path mandatory everywhere, optional accelerators labelled per RID.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-13.15 (ArcForges.Native.Graphics + Runtime.<rid> only): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\13-high-risk-technical-probes.md, anchor rule-wp-13.15
- WP-13:producer-artifacts-and-integration-md-wp producer-artifacts-and-integration.md WP13 row: 'Probe-only 1.0, missing functional export or dependency prevents completion' (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\13-high-risk-technical-probes.md, package-level obligation

Entry condition: adoption slice ADOPT.02.native is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] NAT.15: complete arc_graphics_* export set
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: DesktopPlatform:src/Native/ArcForges.Native.Graphics.Runtime.*/**; DesktopPlatform:eng/packaging/packages.json
Shared resources (follow the owner protocol): RES-desktopplatform-native-build (append): The vcpkg baseline and overlay ports change only through a dependency-admission change with licence and provenance receipts; each native family adds its own CMake targets and workflow entries; triplet or port changes are rebased and rebuilt by their author; CPU-heavy native builds use the workstation build slot.; RES-desktopplatform-package-inventory (append): Each producer task adds its own package entry; every merge to main packs and publishes all packages at one version; consumers pin the candidate produced by the merge of the capability they need, never waiting for a package closure task; one merge queue.; RES-workstation-build-slot (exclusive): Exclusive per workstation for the duration of each CPU-heavy local build or test, through the workstation lock rather than a Plan lease: run the command as `python tools/delivery.py build-slot run --worker <name> --task <task> -- <command>` with the Plan repository tool, which holds the lock directory `.arcforges/build-slot` in the user profile with an owner record and heartbeat and recovers a lock whose holder stopped. Coding and review continue while a build waits; CI capacity is not limited by this rule.
Unblocks: NAT.28, NAT.30

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Clean-cache C17/C# AOT consumers per RID; forced-software-path verified on every RID even where an accelerator is also present
Completion evidence for the ledger: Immutable native package production: behavioral, failure and package evidence (Graphics slice)
Notes: Independent of the other packaging tasks.
```

```text
Execute ArcForges delivery task NAT.28 — Dependency adoption receipts and hardware-lab closure.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\native.md (anchor task-nat-28).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/nat-28 (python tools/delivery.py claim NAT.28 --worker <name>); task branch task/nat-28 in DesktopPlatform; ledger record ledger/tasks/nat-28.md.
Kind/size: producer/M. Baseline: not-started.
Outcome: AD01-AD08 recorded for FFmpeg, miniaudio, OCIO, OIIO, OpenEXR, Imath, OTIO, libusb, PDFium and every shipped transitive dependency; the hardware-lab inventory (serial/audio/GPU plus an actual USB device with vendor/product identity, explicit interface/endpoint, firmware and driver versions) is completed; SBOM/licence/source and enabled-feature lists matched to actual packaged files.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-13.16 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\13-high-risk-technical-probes.md, anchor rule-wp-13.16

Entry condition: adoption slice ADOPT.02.native is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] NAT.20: Media package closure (FFmpeg/miniaudio/libusb positions)
- [artifact] NAT.21: Colour package closure (OCIO position)
- [artifact] NAT.22: Image package closure (OIIO/OpenEXR/Imath positions)
- [artifact] NAT.23: Otio package closure (OTIO position)
- [artifact] NAT.24: Instruments package closure (libusb position, physical USB device)
- [artifact] NAT.25: Pdf package closure (PDFium position)
- [artifact] NAT.26: Graphics package closure
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

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\native.md (anchor task-nat-29).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/nat-29 (python tools/delivery.py claim NAT.29 --worker <name>); task branch task/nat-29 in DesktopPlatform; ledger record ledger/tasks/nat-29.md.
Kind/size: integration/M. Baseline: not-started.
Outcome: Actual candidate NuGet restore/native loading and desktop AOT; C# AOT gRPC/gRPC-Web plus selected auth/storage/SQL adapters; Kotlin/Jetpack Compose generated-client calls; React client calls; a minimal deployed CF<->reachable C#<->R2 chain -- a bounded foundation probe, explicitly not the full WP-52 Cloud Harness

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-06.90 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\06-aot-jit-and-wasm-publish-proof.md, anchor rule-wp-06.90

Entry condition: adoption slice ADOPT.02.native is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] PRF.01: real, delivered outcome of PRF.01 (ArcNotes desktop Native AOT package proof)
- [artifact] PRF.02: real, delivered outcome of PRF.02 (ArcScope desktop Native AOT package proof)
- [artifact] PRF.03: real, delivered outcome of PRF.03 (ArcSlate desktop Native AOT package proof)
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

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\native.md (anchor task-nat-30).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\DesktopPlatform (integration owner: DesktopPlatform integration owner, the holder of roles/integration-desktopplatform).
Claim and handoff record: claims/nat-30 (python tools/delivery.py claim NAT.30 --worker <name>); task branch task/nat-30 in DesktopPlatform; ledger record ledger/tasks/nat-30.md.
Kind/size: integration/M. Baseline: not-started.
Outcome: Decode/seek/drain, encode->independent decode, image tiles, colour, OTIO, PDF, instruments, graphics CPU/fallback, cancel/lifetime/hostile-helper vectors and missing-DLL/wrong-RID negative consumers, all against actual WP07 to WP12 mechanisms (persistence, local RPC, shell, ContentSandbox, telemetry) -- probe-only exports never pass; this is the gate WP14/WP33/WP36 consumers wait behind

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-13.90 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\13-high-risk-technical-probes.md, anchor rule-wp-13.90

Entry condition: adoption slice ADOPT.02.native is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] NAT.06: real, delivered outcome of NAT.06 (Common native ABI: preambles, pack8 records, ownership, cancellation, bounded buffers)
- [artifact] NAT.07: real, delivered outcome of NAT.07 (Media family: reader, probe, frame and seek (arc_media_reader_*))
- [artifact] NAT.08: real, delivered outcome of NAT.08 (Media family: convert, resample and media writer)
- [artifact] NAT.09: real, delivered outcome of NAT.09 (Media family: audio devices (miniaudio))
- [artifact] NAT.10: real, delivered outcome of NAT.10 (Colour family: OCIO transforms)
- [artifact] NAT.11: real, delivered outcome of NAT.11 (Image family: still-image codecs (PNG/TIFF/EXR))
- [artifact] NAT.12: real, delivered outcome of NAT.12 (Otio family: OTIO0.18.1 interchange)
- [artifact] NAT.13: real, delivered outcome of NAT.13 (Instruments family: serial and USB devices (NEW library))
- [artifact] NAT.14: real, delivered outcome of NAT.14 (Pdf family: PDFium and production parser containment in the WP11 helper (NEW library))
- [artifact] NAT.15: real, delivered outcome of NAT.15 (Graphics family: portable CPU surface and optional OS backends (NEW library))
- [artifact] NAT.20: real, delivered outcome of NAT.20 (Media package production: all 6 RIDs)
- [artifact] NAT.21: real, delivered outcome of NAT.21 (Colour package production: all 6 RIDs)
- [artifact] NAT.22: real, delivered outcome of NAT.22 (Image package production: all 6 RIDs)
- [artifact] NAT.23: real, delivered outcome of NAT.23 (Otio package production: all 6 RIDs)
- [artifact] NAT.24: real, delivered outcome of NAT.24 (Instruments package production: all 6 RIDs)
- [artifact] NAT.25: real, delivered outcome of NAT.25 (Pdf package production: all 6 RIDs + ContentSandbox Runtime.<rid> composition)
- [artifact] NAT.26: real, delivered outcome of NAT.26 (Graphics package production: all 6 RIDs)
- [artifact] NAT.28: real, delivered outcome of NAT.28 (Dependency adoption receipts and hardware-lab closure)
- [artifact] NAT.01: package task delivered
- [artifact] NAT.02: package task delivered
- [artifact] NAT.03: package task delivered
- [artifact] NAT.04: package task delivered
- [artifact] NAT.05: package task delivered
- [artifact] PLT.54: package task delivered
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: 

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Local real-integration run of the affected scenario in an existing environment, recorded once; offline and static checks in CI; no hosted runtime, device, browser, live-service or inference CI (P2-017).
Completion evidence for the ledger: Decode/seek/drain, encode->independent decode, image tiles, colour, OTIO, PDF, instruments, graphics CPU/fallback, cancel/lifetime/hostile-helper vectors and missing-DLL/wrong-RID negative consumers, all against actual WP07 to WP12 mechanisms (persistence, local RPC, shell, ContentSandbox, telemetry) -- probe-only exports never pass; this is the gate WP14/WP33/WP36 consumers wait behind
```
