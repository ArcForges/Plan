# ArcForges delivery task prompts — ArcScope

Generated from Design `docs/planning/delivery/delivery-graph.json` by `tools/delivery.py`; do not edit by hand.
Each block is self-contained. Claim a task only when `python tools/delivery.py ready` lists it, with
`python tools/delivery.py claim <TASK-ID> --worker <name>`, then follow `arcforges-implementation.md`.
Tasks are ordered by lane for reading; the order is not a schedule.

## ArcScope

```text
Execute ArcForges delivery task SCOPE.01 — DataSource/SourceAdapter contract, connection profiles and lease/busy exclusivity.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\arcscope.md (anchor task-scope-01).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\ArcScope (integration owner: ArcScope integration owner, the holder of roles/integration-arcscope).
Claim and handoff record: claims/scope-01 (python tools/delivery.py claim SCOPE.01 --worker <name>); task branch task/scope-01 in ArcScope; ledger record ledger/tasks/scope-01.md.
Kind/size: feature/M. Baseline: not-started.
Outcome: A single adapter contract (DataSource/SourceAdapter/Connection) exists with persisted, reusable connection profiles; editing a profile never rewrites a historical session's recorded configuration; a second claimant on the same source is refused with a busy state.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-33.00 (shared adapter contract; ConnectionProfile storage/reuse; EffectiveConfigurationSnapshot immutability on profile edit; lease/busy exclusivity model (BR-01..BR-06, BR-09)): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\33-arcscope-acquisition-and-session.md, anchor rule-wp-33.00

Entry condition: adoption slice ADOPT.05.arcscope is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] PLT.01: published store abstraction with the single write path (for ArcScope's own profile/session store)
- [contract] CON.91: published Contracts records for capture/session identifiers referenced by ConnectionProfile
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: ArcScope:src/ArcScope/ArcScope.Domain/**; ArcScope:src/ArcScope/ArcScope.Acquisition/Adapters/Contract/**; ArcScope:tests/ArcScopePipelineTests/Adapters/**
Shared resources (follow the owner protocol): RES-arcscope-migrations (append): Numbered migrations are allocated at merge by the integration owner (a rebase renumbers pending migrations); each migration is forward-only with its recovery and downgrade-refusal tests; no task edits a merged migration.
Unblocks: SCOPE.03, SCOPE.04, SCOPE.05, SCOPE.08, SCOPE.11, SIM.06

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): offline unit/integration tests only (profile-edit immutability test, exclusivity test with two claimants); no live Cloud or hardware required at this stage
Completion evidence for the ledger: adapter-contract conformance tests, profile immutability test, exclusivity busy-state test
Notes: Foundational; SCOPE.03 (network/replay adapters) and SCOPE.04 (serial/USB adapters) both implement this contract and can proceed in parallel once it lands.
```

```text
Execute ArcForges delivery task SCOPE.02 — Channel, signal, event and time model.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\arcscope.md (anchor task-scope-02).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\ArcScope (integration owner: ArcScope integration owner, the holder of roles/integration-arcscope).
Claim and handoff record: claims/scope-02 (python tools/delivery.py claim SCOPE.02 --worker <name>); task branch task/scope-02 in ArcScope; ledger record ledger/tasks/scope-02.md.
Kind/size: feature/M. Baseline: not-started.
Outcome: A precise time model spanning signal samples and discrete events with exact rate representation, explicit conversion between domains, and explicit recorded alignment between sources.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-33.03 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\33-arcscope-acquisition-and-session.md, anchor rule-wp-33.03

Entry condition: adoption slice ADOPT.05.arcscope is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [contract] CON.91: published numeric/time wire types (rate, timestamp, duration) Channel/Signal/EventRecord must serialise as
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: ArcScope:src/ArcScope/ArcScope.Domain/Time/**; ArcScope:src/ArcScope/ArcScope.Domain/Channels/**; ArcScope:tests/ArcScopePipelineTests/TimeModel/**
Unblocks: SCOPE.05, SCOPE.06, SCOPE.11, SCOPE.12, SCOPE.14

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): offline unit tests: precision across rate domains, alignment with two sources, conversion exactness — pure math, no external environment
Completion evidence for the ledger: precision/alignment/conversion test results
Notes: Pure domain/math task with no native or Cloud dependency; runs fully in parallel with SCOPE.01 (different files, same repo) — a clean simultaneous-execution example.
```

```text
Execute ArcForges delivery task SCOPE.03 — Network and file-replay source adapters (TCP, UDP, file stream).

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\arcscope.md (anchor task-scope-03).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\ArcScope (integration owner: ArcScope integration owner, the holder of roles/integration-arcscope).
Claim and handoff record: claims/scope-03 (python tools/delivery.py claim SCOPE.03 --worker <name>); task branch task/scope-03 in ArcScope; ledger record ledger/tasks/scope-03.md.
Kind/size: feature/M. Baseline: not-started.
Outcome: TCP, UDP and file-stream-replay adapters work over real transports (pure managed sockets/file I/O), pass connect/disconnect/reconnect tests, and share SCOPE.01's profile and exclusivity model.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-33.00 (TCP/UDP/file-replay concrete adapters over the shared contract; real-transport connect/disconnect/reconnect tests): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\33-arcscope-acquisition-and-session.md, anchor rule-wp-33.00

Entry condition: adoption slice ADOPT.05.arcscope is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] SCOPE.01: DataSource/SourceAdapter contract and connection profile model
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: ArcScope:src/ArcScope/ArcScope.Acquisition/Adapters/Network/**; ArcScope:src/ArcScope/ArcScope.Acquisition/Adapters/FileReplay/**; ArcScope:tests/ArcScopePipelineTests/Adapters/Network/**
Unblocks: SCOPE.05, SCOPE.11

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): real-transport tests using.NET Socket/TcpListener/UdpClient loopback and local files — no native dependency, no emulator/CI restriction applies; proportionate under P2-017
Completion evidence for the ledger: per-adapter real-transport connect/disconnect/reconnect results
Notes: This is the implementation-sequence.md §3 'must be real early' item: real serial/TCP/UDP transports must not be mocked.
```

```text
Execute ArcForges delivery task SCOPE.04 — Serial and USB instrument adapters.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\arcscope.md (anchor task-scope-04).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\ArcScope (integration owner: ArcScope integration owner, the holder of roles/integration-arcscope).
Claim and handoff record: claims/scope-04 (python tools/delivery.py claim SCOPE.04 --worker <name>); task branch task/scope-04 in ArcScope; ledger record ledger/tasks/scope-04.md.
Kind/size: feature/M. Baseline: not-started.
Outcome: Serial and USB adapters work over real hardware transports via the native ArcInstruments ABI, enumerate/open/transfer/cancel correctly, refuse busy/permission conflicts per Tier-1 RID, and record a hot-unplug as an explicit capture gap.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-33.00 (serial/USB concrete adapters over the shared contract): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\33-arcscope-acquisition-and-session.md, anchor rule-wp-33.00
- WP-33.90 (generic-USB-V1 body text (enumeration, explicit interface/endpoint open, control/bulk/interrupt transfers, partial writes, cancellation, driver/permission/busy refusal per Tier 1 RID; no automatic kernel-driver detach; hot unplug records an explicit capture gap) — this text sits orphaned between WP-33 §6 and §7 in the source doc with no substep id of its own; folded here since it is entirely about the serial/USB adapter, not §33.90's own verify-and-integration content): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\33-arcscope-acquisition-and-session.md, anchor rule-wp-33.90
- WP-33:orphaned-generic-usb-is-v1-body-text-enu orphaned 'Generic USB is V1' body text (enumeration/open/transfer/cancel/refusal per Tier-1 RID, no auto kernel-driver detach, hot-unplug=explicit gap) sitting between §6 Impacts and §7 Tests with no substep id (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\33-arcscope-acquisition-and-session.md, package-level obligation

Entry condition: adoption slice ADOPT.05.arcscope is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] SCOPE.01: DataSource/SourceAdapter contract and connection profile model
- [artifact] NAT.13: published ArcInstrumentsNative package (arc_instruments_* ABI) — at minimum its fixture/simulated-hardware tier build
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: ArcScope:src/ArcScope/ArcScope.Acquisition/Adapters/Instruments/**; ArcScope: src/ArcScope/ArcScope.Native/**; ArcScope:tests/ArcScopePipelineTests/Adapters/Instruments/**
Permitted substitutes (never real integration evidence): SUB-scope-instruments-fixture: adapter enumerate/open/transfer/cancel/error-path logic against a simulated-hardware build only Real producer ['NAT.13', 'NAT.24']; removed by SCOPE.11
Unblocks: SCOPE.11

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): fixture/simulated-hardware unit tests at this task's own gate; real per-RID hardware acceptance deferred to SCOPE.11/PG-08 per P2-017 (no device/hardware CI)
Completion evidence for the ledger: enumeration/open/transfer/cancel/refusal results against fixture tier now; real-hardware receipt at SCOPE.11
Notes: This is the one WP-33.00 sub-path that genuinely needs a WP13 native family, and only WP-13.12 (not the whole WP13 package). It is the correct place to attach PG-08's per-RID USB acceptance text, which the source document places oddly (orphaned paragraph after WP-33 §6, before §7) with no substep id.
```

```text
Execute ArcForges delivery task SCOPE.05 — Acquisition pipeline: bounded loop, ring buffer, backpressure and overrun accounting.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\arcscope.md (anchor task-scope-05).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\ArcScope (integration owner: ArcScope integration owner, the holder of roles/integration-arcscope).
Claim and handoff record: claims/scope-05 (python tools/delivery.py claim SCOPE.05 --worker <name>); task branch task/scope-05 in ArcScope; ledger record ledger/tasks/scope-05.md.
Kind/size: feature/L. Baseline: not-started.
Outcome: A bounded, timestamped acquisition loop with explicit backpressure sustains throughput above the product target with bounded memory; every overrun is counted, timestamped and recorded; hardware timestamps are preserved where available and the timing source/uncertainty is recorded otherwise.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-33.01 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\33-arcscope-acquisition-and-session.md, anchor rule-wp-33.01

Entry condition: adoption slice ADOPT.05.arcscope is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] SCOPE.01: source adapter contract
- [artifact] SCOPE.02: time/channel model
- [artifact] SCOPE.03: at least one real concrete adapter (network) to drive throughput/overrun tests
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: ArcScope:src/ArcScope/ArcScope.Acquisition/Pipeline/**; ArcScope:tests/ArcScopePipelineTests/Throughput/**
Unblocks: SCOPE.06, SCOPE.11, SCOPE.13

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): sustained-throughput runs with recorded rate/memory/drop counts; induced overrun; timing-source assertions — local, offline, repeatable
Completion evidence for the ledger: throughput/memory/overrun/timing-source results
Notes: WP-13.02 ('Probe C: high-throughput acquisition', the native and runtime-proof lanes/WP13) is a near-identical early risk proof of the same ring-buffer/throughput/overrun approach, done earlier and cheaper. It validates the approach but ships no reusable package (BR-10 keeps the real loop in C# here regardless) — treated as an informative precedent, not a start edge.
```

```text
Execute ArcForges delivery task SCOPE.06 — Session and capture lifecycle: segments, gaps and live observation.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\arcscope.md (anchor task-scope-06).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\ArcScope (integration owner: ArcScope integration owner, the holder of roles/integration-arcscope).
Claim and handoff record: claims/scope-06 (python tools/delivery.py claim SCOPE.06 --worker <name>); task branch task/scope-06 in ArcScope; ledger record ledger/tasks/scope-06.md.
Kind/size: feature/L. Baseline: not-started.
Outcome: The session/capture lifecycle (armed, running, paused, stopped, finalised, interrupted) is correct; captures are sequences of segments plus explicit gaps; pausing the view never stops recording; a disconnect produces an explicit gap rather than a truncated capture.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-33.02 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\33-arcscope-acquisition-and-session.md, anchor rule-wp-33.02

Entry condition: adoption slice ADOPT.05.arcscope is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] SCOPE.05: acquisition pipeline and rolling buffer
- [artifact] SCOPE.02: time/channel model
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: ArcScope:src/ArcScope/ArcScope.Domain/Session/**; ArcScope:src/ArcScope/ArcScope.Domain/Capture/**; ArcScope:tests/ArcScopePipelineTests/Lifecycle/**
Shared resources (follow the owner protocol): RES-arcscope-migrations (append): Numbered migrations are allocated at merge by the integration owner (a rebase renumbers pending migrations); each migration is forward-only with its recovery and downgrade-refusal tests; no task edits a merged migration.
Unblocks: SCOPE.07, SCOPE.09, SCOPE.11, SCOPE.12, SCOPE.13, SCOPE.14, SCOPE.15, SCOPE.17, SCOPE.20, SCOPE.22

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): lifecycle coverage including interruption; pause-view-while-recording test; segment/gap integrity after disconnect — offline
Completion evidence for the ledger: lifecycle, pause-view and gap-integrity results
```

```text
Execute ArcForges delivery task SCOPE.07 — Durable capture writer, chunked verifiable store and crash recovery.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\arcscope.md (anchor task-scope-07).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\ArcScope (integration owner: ArcScope integration owner, the holder of roles/integration-arcscope).
Claim and handoff record: claims/scope-07 (python tools/delivery.py claim SCOPE.07 --worker <name>); task branch task/scope-07 in ArcScope; ledger record ledger/tasks/scope-07.md.
Kind/size: feature/L. Baseline: not-started.
Outcome: Raw capture is written to the chunked verifiable store with per-chunk checksums and an explicit end marker; a finalised capture is structurally immutable; a crash mid-capture recovers to the last committed boundary with an honest end marker and recorded loss.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-33.04 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\33-arcscope-acquisition-and-session.md, anchor rule-wp-33.04

Entry condition: adoption slice ADOPT.05.arcscope is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] SCOPE.06: session/capture lifecycle types
- [artifact] PLT.06: published chunked/large-append verifiable store primitive
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: ArcScope:src/ArcScope/ArcScope.Recording/**; ArcScope:src/ArcScope/ArcScope.Infrastructure/CaptureStore/**; ArcScope:tests/ArcScopePipelineTests/DurableCapture/**
Unblocks: SCOPE.08, SCOPE.11, SCOPE.23, SCOPE.24, SCOPE.25

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): kill-during-capture at chunk boundaries and mid-chunk; recovered-prefix verification; immutability test — offline, deterministic fault injection, no live environment needed
Completion evidence for the ledger: crash-recovery prefix verification and immutability results
Notes: WP-07.05 is named precisely (not 'whole WP07') because WP-07.00/.03 (store abstraction, migrations) are consumed earlier by SCOPE.01/06 for ordinary relational state, while raw capture specifically needs the large-append/chunked primitive.
```

```text
Execute ArcForges delivery task SCOPE.08 — Replay as a source (capture-level).

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\arcscope.md (anchor task-scope-08).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\ArcScope (integration owner: ArcScope integration owner, the holder of roles/integration-arcscope).
Claim and handoff record: claims/scope-08 (python tools/delivery.py claim SCOPE.08 --worker <name>); task branch task/scope-08 in ArcScope; ledger record ledger/tasks/scope-08.md.
Kind/size: feature/M. Baseline: not-started.
Outcome: Replay of a recorded, finalised capture feeds the same pipeline as a labelled ReplaySource, always recording its origin, and never presents device-only fields as measured.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-33.05 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\33-arcscope-acquisition-and-session.md, anchor rule-wp-33.05

Entry condition: adoption slice ADOPT.05.arcscope is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] SCOPE.07: durable, finalised captures to replay
- [artifact] SCOPE.01: source adapter contract
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: ArcScope:src/ArcScope/ArcScope.Acquisition/Adapters/Replay/**; ArcScope:tests/ArcScopePipelineTests/Replay/**
Unblocks: SCOPE.11

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): replay-equivalence test against a recorded capture; labelling assertion; negative test for absent device-only fields
Completion evidence for the ledger: replay equivalence and labelling results
Notes: This is WP-34's repeatable source (SD-09): once this task lands, WP-34's reproducibility/analysis tasks can develop and verify against real recorded+replayed captures without any Cloud simulator.
```

```text
Execute ArcForges delivery task SCOPE.09 — Long-running capture in the shell.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\arcscope.md (anchor task-scope-09).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\ArcScope (integration owner: ArcScope integration owner, the holder of roles/integration-arcscope).
Claim and handoff record: claims/scope-09 (python tools/delivery.py claim SCOPE.09 --worker <name>); task branch task/scope-09 in ArcScope; ledger record ledger/tasks/scope-09.md.
Kind/size: feature/S. Baseline: not-started.
Outcome: Recording state is permanently visible; closing a window during capture always asks with consequences stated, never silently stopping or continuing; background capture persists only while genuine work is active.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-33.06 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\33-arcscope-acquisition-and-session.md, anchor rule-wp-33.06

Entry condition: adoption slice ADOPT.05.arcscope is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] SCOPE.06: capture lifecycle (running/interrupted states) to bind the shell prompt to
- [artifact] PLT.32: published generic shell lifecycle/shutdown-prompt mechanism
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: ArcScope:src/ArcScope/ArcScope.Presentation/**; ArcScope:src/ArcScope/ArcScope.Desktop/CaptureLifecycle/**
Unblocks: PLT.56, SCOPE.11

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): window-close-during-capture prompt test; background-residency test; visibility assertion — desktop-GUI-adjacent, kept to the offline/local tier per P2-017 (no desktop GUI CI; local manual/scripted verification)
Completion evidence for the ledger: window-close, background and visibility results
Notes: The old upstream edge WP-33<-26 (remote action/tool bridge) does not apply here or anywhere else in WP33: WP-26 is about remote-triggered tool execution on a running instance (durable target queue, owner reauth, remote approval), and none of WP-33.00-33.07's substep bodies mention it..
```

```text
Execute ArcForges delivery task SCOPE.10 — Reference drift check against Serial-Studio 639daafb.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\arcscope.md (anchor task-scope-10).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\ArcScope (integration owner: ArcScope integration owner, the holder of roles/integration-arcscope).
Claim and handoff record: claims/scope-10 (python tools/delivery.py claim SCOPE.10 --worker <name>); task branch task/scope-10 in Design; ledger record ledger/tasks/scope-10.md.
Kind/size: feature/S. Baseline: not-started.
Outcome: A drift report exists comparing the reference against the bound commit, covering changed rows, newly introduced upstream material (mapped to an existing requirement or recorded as an accepted exclusion) and licence re-verification; every changed/new item carries a disposition.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-33.07 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\33-arcscope-acquisition-and-session.md, anchor rule-wp-33.07

Entry condition: adoption slice ADOPT.05.arcscope is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- none
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Design:docs/assurance/reference-coverage/arcscope-serial-studio.md
Shared resources (follow the owner protocol): RES-design-evidence (append): Receipts and gate records are separate files per task or gate; indexes are appended; historical records are not rewritten.
Unblocks: SCOPE.11

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): a completeness check that every changed/new item has a disposition; no code build required
Completion evidence for the ledger: drift report: changed rows, newly introduced material with assessment, licence comparison
Notes: Has no real code dependency on any other SCOPE task; can run at any time, though it is most useful shortly before SCOPE.11/WP-33.90 closes so any licence correction lands before the package gate.
```

```text
Execute ArcForges delivery task SCOPE.11 — Owned-artifact verification and real hardware integration.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\arcscope.md (anchor task-scope-11).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\ArcScope (integration owner: ArcScope integration owner, the holder of roles/integration-arcscope).
Claim and handoff record: claims/scope-11 (python tools/delivery.py claim SCOPE.11 --worker <name>); task branch task/scope-11 in ArcScope; ledger record ledger/tasks/scope-11.md.
Kind/size: feature/M. Baseline: not-started.
Outcome: The WP-33 candidate closes: real packaged hardware-path and throughput/overrun/recovery acceptance recorded, no automatic upload of raw acquisition data, PG-08 and PG-03 evidence recorded for every producer this package owns.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-33.90 (full (excluding the generic-USB-V1 body text folded into SCOPE.04)): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\33-arcscope-acquisition-and-session.md, anchor rule-wp-33.90
- WP-33:p2-010-required-behavior-and-closure-sec P2-010 required-behavior-and-closure section (acquisition.source/framing/trigger profiles, gap/loss/durable-capture manifests, all accepted serial/network/file/USB sources) (P2-010 required-behavior-and-closure section: acquisition.source/framing/trigger profiles, gap/loss/durable-capture manifests, all accepted serial/network/file/USB sources, independent positive/negative vectors, actual owner integration): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\33-arcscope-acquisition-and-session.md, package-level obligation

Entry condition: adoption slice ADOPT.05.arcscope is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] SCOPE.01: all WP33 tasks complete to assemble
- [artifact] SCOPE.02: as above
- [artifact] SCOPE.03: as above
- [artifact] SCOPE.04: as above
- [artifact] SCOPE.05: as above
- [artifact] SCOPE.06: as above
- [artifact] SCOPE.07: as above
- [artifact] SCOPE.08: as above
- [artifact] SCOPE.09: as above
- [artifact] SCOPE.10: drift report disposition (must be clean or corrected per D-001 before dependent work continues)
- [artifact] NAT.24: published Instruments runtime packages
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: ArcScope:docs/wp-33-integration-receipt.md
Unblocks: REL.02

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): real packaged hardware-path and throughput/overrun/recovery acceptance; offline-acceptance-matrix rows (fresh shell, hydrated outage, unavailable content, signout, restart) where applicable; no macOS CI, no device/emulator CI per P2-017 — evidence is recorded from local/lab runs
Completion evidence for the ledger: owned-artifact and real-integration receipt: source commit, producer version, candidate hashes, actual runtime/OS/device/provider, scenario, result, limitations, real-vs-fixture status
```

```text
Execute ArcForges delivery task SCOPE.12 — Visualisation: virtualised rendering, downsampling, cursors and markers.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\arcscope.md (anchor task-scope-12).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\ArcScope (integration owner: ArcScope integration owner, the holder of roles/integration-arcscope).
Claim and handoff record: claims/scope-12 (python tools/delivery.py claim SCOPE.12 --worker <name>); task branch task/scope-12 in ArcScope; ledger record ledger/tasks/scope-12.md.
Kind/size: feature/L. Baseline: not-started.
Outcome: Time-series and event visualisation meets the responsiveness budget at corpus scale with virtualised rendering and downsampling; the display explicitly discloses when it is downsampled; cursor readings are exact regardless of display resolution.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-34.00 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\34-arcscope-analysis-and-reporting.md, anchor rule-wp-34.00

Entry condition: adoption slice ADOPT.05.arcscope is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] SCOPE.02: time/channel model
- [artifact] SCOPE.06: session/capture to visualise
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: ArcScope:src/ArcScope/ArcScope.Visualization/**; ArcScope:tests/ArcScopePipelineTests/Visualization/**
Unblocks: SCOPE.19

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): scale-corpus interaction measurements; downsampling-disclosure assertion; downsampled-vs-full-resolution cursor correctness — desktop rendering kept to local/offline tier per P2-017
Completion evidence for the ledger: responsiveness, disclosure and cursor-exactness results
Notes: RESOLVED FINDING, not an edge: the assignment hint suggested this might need the WP-13.14 Graphics native family (arc_graphics_* ABI). Checked 12-native-interop-and-media.md (the ArcScope native-interop authority, §8) directly: zero mentions of Graphics; its native surface is device/transport/high-rate acquisition primitives only. The Graphics native family's real consumer is ArcSlate (per the native and runtime-proof lanes' own contracts note: 'used by ArcSlate mainly'). ArcScope already carries Avalonia (Skia-based managed rendering, see ArcScope third-party/Avalonia.LICENSE.txt), which is sufficient for plotting/downsampling in pure C#.
```

```text
Execute ArcForges delivery task SCOPE.13 — Triggers with pre/post windows.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\arcscope.md (anchor task-scope-13).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\ArcScope (integration owner: ArcScope integration owner, the holder of roles/integration-arcscope).
Claim and handoff record: claims/scope-13 (python tools/delivery.py claim SCOPE.13 --worker <name>); task branch task/scope-13 in ArcScope; ledger record ledger/tasks/scope-13.md.
Kind/size: feature/M. Baseline: not-started.
Outcome: Triggers control capture and mark significant time events with exact pre- and post-trigger windows served by the rolling buffer; samples are provably unmodified; trigger storms are bounded.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-34.01 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\34-arcscope-analysis-and-reporting.md, anchor rule-wp-34.01

Entry condition: adoption slice ADOPT.05.arcscope is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] SCOPE.05: rolling buffer
- [artifact] SCOPE.06: capture lifecycle
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: ArcScope:src/ArcScope/ArcScope.Domain/Triggers/**; ArcScope:tests/ArcScopePipelineTests/Triggers/**
Unblocks: SCOPE.19

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): pre/post-window correctness; data-immutability assertion; trigger-storm bound test — offline
Completion evidence for the ledger: trigger window, immutability and storm-bound results
```

```text
Execute ArcForges delivery task SCOPE.14 — Measurements: scope.measurement.v1.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\arcscope.md (anchor task-scope-14).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\ArcScope (integration owner: ArcScope integration owner, the holder of roles/integration-arcscope).
Claim and handoff record: claims/scope-14 (python tools/delivery.py claim SCOPE.14 --worker <name>); task branch task/scope-14 in ArcScope; ledger record ledger/tasks/scope-14.md.
Kind/size: feature/L. Baseline: not-started.
Outcome: Every measurement family in scope.measurement.v1 reproduces under its recorded profile/configuration within the declared numerical tolerance, with units and precision stated; independent reference values (including the Pearson r=1/r=-1 vectors and constant-input-unavailable case) pass.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-34.02 (full, including the required-design-implementation text: every basic family via declared population/sample-weighted formulas, half-open input selection, calibrated units, coverage/status rules, recorded pulse thresholds/interpolation, independent statistical hand-calculation and digital/analog/gap vectors): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\34-arcscope-analysis-and-reporting.md, anchor rule-wp-34.02
- WP-34:orphaned-6-7-body-text-pearson-independe orphaned §6/§7 body text: 'Pearson independent vectors: x=[1,2,3], y=[2,4,6] gives r=1; y=[3,2,1] gives r=-1. Constant input is unavailable; preserve the declared lag and overlap rules' — a concrete correlation-family acceptance vector with no substep id of its own (orphaned §6/§7 body text: 'Pearson independent vectors: x=[1,2,3], y=[2,4,6] gives r=1; y=[3,2,1] gives r=-1. Constant input is unavailable; preserve the declared lag and overlap rules' — a concrete correlation-family acceptance vector with no substep id of its own; package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\34-arcscope-analysis-and-reporting.md, package-level obligation
- WP-34:8-additional-completion-requirement-ever §8 additional completion requirement: every basic family has its formula/status oracle; reproduction uses the defined tolerance rather than an undefined byte-equality claim (§8 additional completion requirement: every basic family has its formula/status oracle; reproduction uses the defined tolerance rather than an undefined byte-equality claim; package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\34-arcscope-analysis-and-reporting.md, package-level obligation

Entry condition: adoption slice ADOPT.05.arcscope is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [contract] CON.91: the published scope.measurement.v1 profile (families, formulas, units, coverage/status rules) in Contracts
- [artifact] SCOPE.02: time/channel model
- [artifact] SCOPE.06: capture/configuration snapshot
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: ArcScope:src/ArcScope/ArcScope.Analysis/Measurements/**; ArcScope:tests/ArcScopePipelineTests/Measurements/**
Unblocks: SCOPE.16, SCOPE.18, SCOPE.19, SCOPE.21, SCOPE.24, SIM.06, SIM.09

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): reference-value tests per measurement kind; unit-handling test; reproduction-from-recorded-configuration test — offline, deterministic tolerance-based comparison
Completion evidence for the ledger: measurement reference and reproduction results, including the Pearson vectors
```

```text
Execute ArcForges delivery task SCOPE.15 — Decoder framework and first-party protocol decoders.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\arcscope.md (anchor task-scope-15).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\ArcScope (integration owner: ArcScope integration owner, the holder of roles/integration-arcscope).
Claim and handoff record: claims/scope-15 (python tools/delivery.py claim SCOPE.15 --worker <name>); task branch task/scope-15 in ArcScope; ledger record ledger/tasks/scope-15.md.
Kind/size: feature/M. Baseline: not-started.
Outcome: A versioned decoder framework produces structured events (never raw channel data); malformed frames, checksum failures and unknown fields are surfaced with counts/locations; no decoder has a device-write path.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-34.03 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\34-arcscope-analysis-and-reporting.md, anchor rule-wp-34.03

Entry condition: adoption slice ADOPT.05.arcscope is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] SCOPE.06: capture/channel data to decode
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: ArcScope:src/ArcScope/ArcScope.Decoders/**; ArcScope:tests/ArcScopePipelineTests/Decoders/**
Unblocks: SCOPE.16, SCOPE.18, SCOPE.19, SCOPE.21

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): per-decoder fixture corpora including malformed input; error-visibility assertion; structural no-device-write test — offline
Completion evidence for the ledger: per-decoder fixtures, error visibility and no-write assertion
Notes: Independent of SCOPE.14 (measurements); the two can proceed in parallel. Decoder scope (UART/I2C/SPI) is fixed by the already-frozen analysis.v1 profile in architecture doc 26-product-behavior-profiles.md — note this is the ARCHITECTURE document numbered 26, unrelated to WP-26 (Remote action and tool bridge); no start edge needed since the design is already frozen, not missing.
```

```text
Execute ArcForges delivery task SCOPE.16 — Analysis definitions and recipes as native ProductJobs.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\arcscope.md (anchor task-scope-16).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\ArcScope (integration owner: ArcScope integration owner, the holder of roles/integration-arcscope).
Claim and handoff record: claims/scope-16 (python tools/delivery.py claim SCOPE.16 --worker <name>); task branch task/scope-16 in ArcScope; ledger record ledger/tasks/scope-16.md.
Kind/size: feature/L. Baseline: not-started.
Outcome: Versioned analysis definitions compose into recipes; results are derived data reconstructable from evidence plus configuration; long analyses run as long-running product jobs with progress and cancellation; deleting and rebuilding all results matches the profile oracle within tolerance; historical results record their definition version.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-34.04 (full, including the required-design-implementation text: same profile through native ProductJobs over a frozen committed source; persist request/config hashes, resolved levels, per-family quality; delete-and-rebuild must match the profile oracle within tolerance): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\34-arcscope-analysis-and-reporting.md, anchor rule-wp-34.04

Entry condition: adoption slice ADOPT.05.arcscope is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] SCOPE.14: measurements
- [artifact] SCOPE.15: decoders
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: ArcScope:src/ArcScope/ArcScope.Analysis/Recipes/**; ArcScope:tests/ArcScopePipelineTests/Analysis/**
Unblocks: SCOPE.18, SCOPE.19, SCOPE.21

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): reconstruction test deleting all results and rebuilding; long-analysis cancellation; version-change test — offline
Completion evidence for the ledger: result reconstruction and version-recording results
Notes: 'Native ProductJobs' reads as ArcScope's own in-process long-running Task/CancellationToken job pattern ('under their product owner'), not a shared cross-repo service; DesktopPlatform already carries a BuildingBlocks ArcForges.Application.Abstractions package this can reuse. Not modelled as a hard external artifact edge — checked WP-08 specifically and ruled it out: WP-08 is local IPC/process registration, not a job-execution abstraction.
```

```text
Execute ArcForges delivery task SCOPE.17 — Annotations, findings and session/capture comparison.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\arcscope.md (anchor task-scope-17).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\ArcScope (integration owner: ArcScope integration owner, the holder of roles/integration-arcscope).
Claim and handoff record: claims/scope-17 (python tools/delivery.py claim SCOPE.17 --worker <name>); task branch task/scope-17 in ArcScope; ledger record ledger/tasks/scope-17.md.
Kind/size: feature/M. Baseline: not-started.
Outcome: Annotations and findings exist as authored content with identity and history, never written into raw capture; session-to-session and capture-to-capture comparison states its alignment explicitly.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-34.05 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\34-arcscope-analysis-and-reporting.md, anchor rule-wp-34.05

Entry condition: adoption slice ADOPT.05.arcscope is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] SCOPE.06: session/capture to annotate/compare
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: ArcScope:src/ArcScope/ArcScope.Domain/Annotations/**; ArcScope:tests/ArcScopePipelineTests/Annotations/**
Unblocks: SCOPE.18, SCOPE.19, SCOPE.22

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): structural raw-capture-untouched test; comparison correctness with deliberate misalignment; finding history tests — offline
Completion evidence for the ledger: raw-capture immutability and comparison alignment results
Notes: Independent of SCOPE.14/15/16 (measurements/decoders/recipes); can run in parallel with them.
```

```text
Execute ArcForges delivery task SCOPE.18 — Reports and reproducibility.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\arcscope.md (anchor task-scope-18).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\ArcScope (integration owner: ArcScope integration owner, the holder of roles/integration-arcscope).
Claim and handoff record: claims/scope-18 (python tools/delivery.py claim SCOPE.18 --worker <name>); task branch task/scope-18 in ArcScope; ledger record ledger/tasks/scope-18.md.
Kind/size: feature/L. Baseline: not-started.
Outcome: Reports compose analyses, measurements, findings and visualisations into a portable exported form; every element traces to session, capture, time range, configuration snapshot, decoder version and analysis version; regenerating from recorded sources produces equivalent results.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-34.06 (full, including both required-design-implementation paragraphs: report/UI/offline-recomputation comparison with rendering/rounding never changing the stored numeric result; report-section origin plus enclosing union; deterministic measurement beside AI narrative never relabelled): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\34-arcscope-analysis-and-reporting.md, anchor rule-wp-34.06
- WP-34:8-additional-completion-requirement-ever §8 additional completion requirement: every basic family has its formula/status oracle; reproduction uses the defined tolerance rather than an undefined byte-equality claim (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\34-arcscope-analysis-and-reporting.md, package-level obligation

Entry condition: adoption slice ADOPT.05.arcscope is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] SCOPE.14: measurements
- [artifact] SCOPE.15: decoders
- [artifact] SCOPE.16: analysis results
- [artifact] SCOPE.17: annotations/findings
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: ArcScope:src/ArcScope/ArcScope.Reporting/**; ArcScope:tests/ArcScopePipelineTests/Reports/**
Unblocks: SCOPE.19, SCOPE.22, SIM.09

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): traceability completeness test; regeneration-equivalence test; export fidelity check; content-origin carrier vectors including unknown input and failed publication — offline
Completion evidence for the ledger: traceability completeness and regeneration equivalence results; carrier/propagation/failure vectors with payload and manifest hashes
Notes: Content-origin behavior (requirements/07-security-privacy-and-trust.md) and the carrier schema (requirements/13-data-formats-and-portability.md) are named as frozen design inputs fixed before this package — already satisfied, not a start edge; implement per spec without choosing a different marking mechanism.
```

```text
Execute ArcForges delivery task SCOPE.19 — Owned-artifact verification and real integration.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\arcscope.md (anchor task-scope-19).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\ArcScope (integration owner: ArcScope integration owner, the holder of roles/integration-arcscope).
Claim and handoff record: claims/scope-19 (python tools/delivery.py claim SCOPE.19 --worker <name>); task branch task/scope-19 in ArcScope; ledger record ledger/tasks/scope-19.md.
Kind/size: feature/M. Baseline: not-started.
Outcome: The WP-34 candidate closes: scope.measurement.v1 independent expected results, invalid/status cases and reporting references pass; native acceleration does not redefine the result; PG-08 hardware-based measurement/analysis evidence is recorded.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-34.90 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\34-arcscope-analysis-and-reporting.md, anchor rule-wp-34.90
- WP-34:p2-010-required-behavior-and-closure-sec P2-010 required-behavior-and-closure section (every remaining spectrum/correlation/threshold/event-pattern/decoder analysis profile in architecture 26) (P2-010 required-behavior-and-closure section: every remaining spectrum/correlation/threshold/event-pattern/decoder analysis profile in architecture 26, independent numeric and gap/error vectors): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\34-arcscope-analysis-and-reporting.md, package-level obligation

Entry condition: adoption slice ADOPT.05.arcscope is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] SCOPE.12: all WP34 tasks complete to assemble
- [artifact] SCOPE.13: as above
- [artifact] SCOPE.14: as above
- [artifact] SCOPE.15: as above
- [artifact] SCOPE.16: as above
- [artifact] SCOPE.17: as above
- [artifact] SCOPE.18: as above
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: ArcScope:docs/wp-34-integration-receipt.md
Unblocks: REL.02

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): scope.measurement.v1 independent expected results, invalid/status cases and reporting references; proportionate under P2-017
Completion evidence for the ledger: owned-artifact and real-integration receipt
Notes: Confirms the design's explicit non-edge: WP-34 does not wait on WP-51 (the Cloud simulator); reproducibility is verified via SCOPE.08 replay.
```

```text
Execute ArcForges delivery task SCOPE.20 — ArcChat capability surface for ArcScope.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\arcscope.md (anchor task-scope-20).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\ArcScope (integration owner: ArcScope integration owner, the holder of roles/integration-arcscope).
Claim and handoff record: claims/scope-20 (python tools/delivery.py claim SCOPE.20 --worker <name>); task branch task/scope-20 in ArcScope; ledger record ledger/tasks/scope-20.md.
Kind/size: feature/M. Baseline: not-started.
Outcome: Query, analysis, authoring and operational capabilities are declared, each with risk level, permission requirement and approval posture; start/stop capture are treated as real-side-effect operations, not read-only conveniences.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-35.00 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\35-arcscope-integration-and-sync.md, anchor rule-wp-35.00

Entry condition: adoption slice ADOPT.05.arcscope is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] SCOPE.06: session/capture/channel/signal/event domain objects the query capabilities expose
- [contract] CON.02: the generic capability descriptor shape (risk level, permission requirement, approval posture) established by the Hub/minimal-provider-slice pattern
Completion prerequisites (may start earlier; cannot complete before these are complete):
- [integration] AST.12: real ArcChat security/approval surface actually enforcing these descriptors end to end

Permitted write scope: ArcScope:src/ArcScope/ArcScope.AssistantIntegration/**; ArcScope:tests/ArcScopePipelineTests/Capabilities/**
Unblocks: SCOPE.25, SCOPE.26

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): descriptor validation per capability; owner-side refusal tests; operational-capability risk assertion — offline
Completion evidence for the ledger: capability descriptor and refusal results
Notes: The old WP33<-26 edge does not transfer here either: WP-26 is the remote *execution* bridge, which would consume these capability descriptors as a downstream caller, not produce anything WP-35.00 needs to start.
```

```text
Execute ArcForges delivery task SCOPE.21 — Bounded context provision for AI.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\arcscope.md (anchor task-scope-21).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\ArcScope (integration owner: ArcScope integration owner, the holder of roles/integration-arcscope).
Claim and handoff record: claims/scope-21 (python tools/delivery.py claim SCOPE.21 --worker <name>); task branch task/scope-21 in ArcScope; ledger record ledger/tasks/scope-21.md.
Kind/size: feature/M. Baseline: not-started.
Outcome: ArcScope contributes structured results (measurements, analysis outputs, decoded event summaries, selected ranges) as bounded context; raw capture structurally cannot enter a context payload; oversized context is refused explicitly.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-35.01 (full, including required-design-implementation text: project measurement values with profile, immutable source/configuration binding, counts, coverage and status into bounded context/report references; unknown-profile and insufficient results are never silently rendered as numeric zero): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\35-arcscope-integration-and-sync.md, anchor rule-wp-35.01
- WP-35:4-content-origin-content-unit-binding-ob §4 content-origin/content-unit binding obligation applying broadly to WP35's changed files (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\35-arcscope-integration-and-sync.md, package-level obligation

Entry condition: adoption slice ADOPT.05.arcscope is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] SCOPE.14: measurements
- [artifact] SCOPE.16: analysis results
- [artifact] SCOPE.15: decoders
Completion prerequisites (may start earlier; cannot complete before these are complete):
- [integration] AST.15: real ArcChat 'Ask ArcChat' consumption of the bounded context reference

Permitted write scope: ArcScope:src/ArcScope/ArcScope.Application/Context/**; ArcScope:tests/ArcScopePipelineTests/Context/**
Unblocks: SCOPE.26

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): structural test asserting raw capture cannot enter a context payload; bounding test; visibility test — offline
Completion evidence for the ledger: structural raw-capture exclusion and bounding results
```

```text
Execute ArcForges delivery task SCOPE.22 — Cloud sync scope (metadata, not raw capture).

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\arcscope.md (anchor task-scope-22).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\ArcScope (integration owner: ArcScope integration owner, the holder of roles/integration-arcscope).
Claim and handoff record: claims/scope-22 (python tools/delivery.py claim SCOPE.22 --worker <name>); task branch task/scope-22 in ArcScope; ledger record ledger/tasks/scope-22.md.
Kind/size: feature/M. Baseline: not-started.
Outcome: The ArcScope sync scope excludes raw capture by default and includes metadata, analysis, annotations, findings, reports and configurations; enabling project sync transfers no raw capture bytes; the policy is visible per project and per session; the included scope converges across devices.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-35.02 (all work except the parts mapped to SCOPE.27): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\35-arcscope-integration-and-sync.md, anchor rule-wp-35.02

Entry condition: adoption slice ADOPT.05.arcscope is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] SCOPE.06: session metadata
- [artifact] SCOPE.18: reports
- [artifact] SCOPE.17: annotations/findings
Completion prerequisites (may start earlier; cannot complete before these are complete):
- [integration] SCOPE.27: real ArcScope metadata sync against deployed Cloud

Permitted write scope: ArcScope:src/ArcScope/ArcScope.CloudClient/SyncScope/**; ArcScope:tests/SyncConflictTests/ArcScope/**
Permitted substitutes (never real integration evidence): SUB-scope-sync-fixture: client-side scope-mapping/exclusion logic only Real producer ['CLOUD.39']; removed by SCOPE.27
Unblocks: SCOPE.26, SCOPE.27

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): enable-sync test asserting no raw bytes transferred; policy-visibility test; convergence test across devices for included scope — early development against a contract-bound sync fixture, real convergence at WP-35.90
Completion evidence for the ledger: no-raw-bytes sync assertion and convergence results
```

```text
Execute ArcForges delivery task SCOPE.23 — Explicit per-session raw capture upload.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\arcscope.md (anchor task-scope-23).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\ArcScope (integration owner: ArcScope integration owner, the holder of roles/integration-arcscope).
Claim and handoff record: claims/scope-23 (python tools/delivery.py claim SCOPE.23 --worker <name>); task branch task/scope-23 in ArcScope; ledger record ledger/tasks/scope-23.md.
Kind/size: feature/M. Baseline: not-started.
Outcome: Raw upload is an explicit per-session act with size/destination/consequence stated, using the chunked upload path with resumption and verification; no automatic trigger path exists anywhere (not from AI, not from enabling sync).

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-35.03 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\35-arcscope-integration-and-sync.md, anchor rule-wp-35.03

Entry condition: adoption slice ADOPT.05.arcscope is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] SCOPE.07: durable capture to upload
- [artifact] CLOUD.42: published blob lifecycle mechanism (chunked upload, resumption, verification)
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: ArcScope:src/ArcScope/ArcScope.CloudClient/RawUpload/**; ArcScope:tests/SyncConflictTests/ArcScope/RawUpload/**
Unblocks: SCOPE.26

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): explicit-upload flow test; negative test for no automatic trigger path; resumption and verification tests on a large capture
Completion evidence for the ledger: explicit upload, no-auto-trigger and resumption results
```

```text
Execute ArcForges delivery task SCOPE.24 — Import, export and format fixtures.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\arcscope.md (anchor task-scope-24).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\ArcScope (integration owner: ArcScope integration owner, the holder of roles/integration-arcscope).
Claim and handoff record: claims/scope-24 (python tools/delivery.py claim SCOPE.24 --worker <name>); task branch task/scope-24 in ArcScope; ledger record ledger/tasks/scope-24.md.
Kind/size: feature/L. Baseline: not-started.
Outcome: Native full-fidelity bundle export/import round-trips with equivalence; tabular export carries explicit precision warnings; import enters the unified session model with a recorded origin (never disguised as a live device); every claimed import version has a fixture — satisfying PG-07 for ArcScope.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-35.04 (full, including required-design-implementation text: native bundles preserve origin, measurement profile/configuration and simulator provenance separately; CSV/JSON/report export publishes required sidecars atomically; structured context carries selected origins and measurement quality, never raw capture): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\35-arcscope-integration-and-sync.md, anchor rule-wp-35.04
- WP-35:4-content-origin-content-unit-binding-ob §4 content-origin/content-unit binding obligation applying broadly to WP35's changed files (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\35-arcscope-integration-and-sync.md, package-level obligation
- WP-35:8-additional-completion-requirements-mea §8 additional completion requirements (measurement meaning/numerical profile survives portability; content-origin carrier vectors) (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\35-arcscope-integration-and-sync.md, package-level obligation

Entry condition: adoption slice ADOPT.05.arcscope is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] SCOPE.07: durable capture format to bundle/export
- [artifact] SCOPE.14: measurement profile/configuration to carry in the bundle
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: ArcScope:src/ArcScope/ArcScope.ImportExport/**; ArcScope:fixtures/formats/arcscope/**; ArcScope:tests/ArcScopePipelineTests/ImportExport/**
Shared resources (follow the owner protocol): RES-arcscope-format-fixtures (append): Fixtures are added per task under its own subdirectory; manifests are append-only.
Unblocks: SCOPE.26, SIM.06, SIM.09

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): bundle round-trip equivalence; precision-warning assertions; origin-recording test; fixture coverage for every claimed version — offline
Completion evidence for the ledger: bundle round-trip, precision warnings, origin and fixture coverage
Notes: This task also carries the bundle-side half of WP-51's 'simulator provenance separately' requirement — SIM.06 (ArcScope-side simulator ingestion) depends on this task so simulated captures round-trip through the same bundle format with their synthetic labelling intact.
```

```text
Execute ArcForges delivery task SCOPE.25 — Extension boundary: no third-party raw-capture write path.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\arcscope.md (anchor task-scope-25).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\ArcScope (integration owner: ArcScope integration owner, the holder of roles/integration-arcscope).
Claim and handoff record: claims/scope-25 (python tools/delivery.py claim SCOPE.25 --worker <name>); task branch task/scope-25 in ArcScope; ledger record ledger/tasks/scope-25.md.
Kind/size: feature/S. Baseline: not-started.
Outcome: No extension-reachable path can write raw capture; extension access to ArcScope is through capabilities with owner-side validation only.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-35.05 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\35-arcscope-integration-and-sync.md, anchor rule-wp-35.05

Entry condition: adoption slice ADOPT.05.arcscope is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] SCOPE.20: capability surface
- [artifact] SCOPE.07: raw capture write path to assert exclusion against
- [artifact] EXT.02: published dual capability boundary mechanism
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: ArcScope:src/ArcScope/ArcScope.AssistantIntegration/ExtensionBoundary/**; ArcScope:tests/ArcScopePipelineTests/ExtensionBoundary/**
Unblocks: SCOPE.26

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): structural test asserting no extension-reachable raw-write path exists; owner-side refusal test from an extension caller — offline
Completion evidence for the ledger: extension no-write structural results
```

```text
Execute ArcForges delivery task SCOPE.26 — Owned-artifact verification and real integration.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\arcscope.md (anchor task-scope-26).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\ArcScope (integration owner: ArcScope integration owner, the holder of roles/integration-arcscope).
Claim and handoff record: claims/scope-26 (python tools/delivery.py claim SCOPE.26 --worker <name>); task branch task/scope-26 in ArcScope; ledger record ledger/tasks/scope-26.md.
Kind/size: feature/M. Baseline: not-started.
Outcome: The WP-35 candidate closes: metadata sync and explicit-upload behavior remain distinct; context/report data retain measurement identity and ownership across real service calls; PG-03 licence/provenance evidence recorded.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-35.90 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\35-arcscope-integration-and-sync.md, anchor rule-wp-35.90

Entry condition: adoption slice ADOPT.05.arcscope is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] SCOPE.20: all WP35 tasks complete to assemble
- [artifact] SCOPE.21: as above
- [artifact] SCOPE.22: as above
- [artifact] SCOPE.23: as above
- [artifact] SCOPE.24: as above
- [artifact] SCOPE.25: as above
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: ArcScope:docs/wp-35-integration-receipt.md
Unblocks: REL.02

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): metadata sync and explicit-upload behavior remain distinct; context/report data retain measurement identity across real service calls — real Cloud integration exercised here, not at earlier SCOPE tasks
Completion evidence for the ledger: owned-artifact and real-integration receipt
```

```text
Execute ArcForges delivery task SCOPE.27 — Real ArcScope metadata sync against the deployed Cloud sync engine.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\arcscope.md (anchor task-scope-27).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\ArcScope (integration owner: ArcScope integration owner, the holder of roles/integration-arcscope). Also touches: Cloud.
Claim and handoff record: claims/scope-27 (python tools/delivery.py claim SCOPE.27 --worker <name>); task branch task/scope-27 in ArcScope; ledger record ledger/tasks/scope-27.md.
Kind/size: integration/M. Baseline: not-started.
Outcome: ArcScope session and capture metadata sync scopes converge across devices against the deployed Cloud sync engine, replacing the contract-bound sync substitute; raw captures stay local unless explicitly uploaded.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-35.02 (real-integration evidence: metadata sync scope converges against deployed Cloud authority): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\35-arcscope-integration-and-sync.md, anchor rule-wp-35.02

Entry condition: adoption slice ADOPT.05.arcscope is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] SCOPE.22: ArcScope Cloud sync scope declaration and client
- [artifact] CLOUD.39: deployed guarded publication and convergent bootstrap
- [artifact] CLOUD.44: multi-device convergence harness
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: ArcScope:tests/ArcScope.Tests.Integration/Sync/**
Unblocks: SCOPE.22

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Local real-integration run against a deployed test environment, recorded once; offline checks in CI; no hosted live-service CI (P2-017).
Completion evidence for the ledger: Candidate identities, deployed environment identity, convergence scenario results and untested coverage.
Notes: Added during consolidation so the ArcScope sync substitute has a named replacing task.
```
