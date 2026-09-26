# ArcForges delivery task prompts — ArcSlate

Generated from Design `docs/planning/delivery/delivery-graph.json` by `tools/delivery.py`; do not edit by hand.
Each block is self-contained. Claim a task only when `python tools/delivery.py ready` lists it, with
`python tools/delivery.py claim <TASK-ID> --worker <name>`, then follow `arcforges-implementation.md`.
Tasks are ordered by lane for reading; the order is not a schedule.

## ArcSlate

```text
Execute ArcForges delivery task SLATE.01 — Exact time model: canonical ticks, rational rates, frame/sample time, half-open ranges.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\arcslate.md (anchor task-slate-01).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\ArcSlate (integration owner: ArcSlate integration owner, the holder of roles/integration-arcslate).
Claim and handoff record: claims/slate-01 (python tools/delivery.py claim SLATE.01 --worker <name>); task branch task/slate-01 in ArcSlate; ledger record ledger/tasks/slate-01.md.
Kind/size: feature/M. Baseline: not-started.
Outcome: RationalRate, FrameTime, SampleTime, TimeRange and the 705,600,000 Hz tick domain exist with exact frame<->tick and sample<->tick round-trip on every supported rate, half-open range algebra (BO-01), and the five enumerated rounding sites (RP-02) as the only places a position rounds; a policy test asserts no other code path rounds.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-36.01 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\36-arcslate-project-and-timeline.md, anchor rule-wp-36.01

Entry condition: adoption slice ADOPT.06.arcslate is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- none
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: ArcSlate:src/ArcForges.ArcSlate.Domain/Time/**; ArcSlate:tests/ArcForges.ArcSlate.Tests.Unit/Time/**
Unblocks: SLATE.02, SLATE.03, SLATE.06, SLATE.14, SLATE.17, SLATE.20, SLATE.29, SLATE.38

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline unit tests only: NTSC/audio/negative/source-inexact/ties-even/half-open/overflow vectors per WP-36.01; no runtime/device dependency; AOT-compatible pure C#.
Completion evidence for the ledger: Per-rate round-trip table (frame->tick->frame, sample->tick->sample), long-sequence drift measurement showing zero drift, boundary-sample fixture proving no duplicated/missing sample at a cut.
Notes: No cross-area start blocker: this is pure C# arithmetic against a frozen architecture-23 spec (§3, §3.10 OB-01..05) and the frozen slate.edit.v1/keyframe profile (26§4). It needs no persistence, no UI, no native ABI and no published Contracts wire type to begin. It is the least-blocked, most-parallelizable task in the whole area and should start immediately alongside repository bootstrap for the other lanes.
```

```text
Execute ArcForges delivery task SLATE.02 — Project and sequence domain model.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\arcslate.md (anchor task-slate-02).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\ArcSlate (integration owner: ArcSlate integration owner, the holder of roles/integration-arcslate).
Claim and handoff record: claims/slate-02 (python tools/delivery.py claim SLATE.02 --worker <name>); task branch task/slate-02 in ArcSlate; ledger record ledger/tasks/slate-02.md.
Kind/size: feature/M. Baseline: not-started.
Outcome: Project (multi-sequence container) and Sequence (playable/renderable composition with its own SequenceSettings snapshot and output grids) exist as structurally distinct types over one shared MediaLibrary; Project != Sequence != media folder is asserted structurally.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-36.00 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\36-arcslate-project-and-timeline.md, anchor rule-wp-36.00

Entry condition: adoption slice ADOPT.06.arcslate is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] SLATE.01: RationalRate/TimeRange types for SequenceSettings video/audio output grids
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: ArcSlate:src/ArcForges.ArcSlate.Domain/Project/**; ArcSlate:src/ArcForges.ArcSlate.Domain/Sequence/**
Shared resources (follow the owner protocol): RES-arcslate-build-config (append): Solution/project lists, central package versions and CI job lists are appended by the task that adds a project, dependency or job; dependency additions follow the dependency-admission policy with a reviewed receipt; lock files are regenerated after rebase and never hand-merged; the integration owner resolves ordering conflicts at merge.
Unblocks: SLATE.05, SLATE.06, SLATE.10

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline unit tests: multi-sequence-over-one-library assertion, project/sequence/folder distinction test.
Completion evidence for the ledger: Multi-sequence project fixture; structural-distinction test results.
```

```text
Execute ArcForges delivery task SLATE.03 — Media asset/stream/metadata domain model and content-based relink algorithm.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\arcslate.md (anchor task-slate-03).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\ArcSlate (integration owner: ArcSlate integration owner, the holder of roles/integration-arcslate).
Claim and handoff record: claims/slate-03 (python tools/delivery.py claim SLATE.03 --worker <name>); task branch task/slate-03 in ArcSlate; ledger record ledger/tasks/slate-03.md.
Kind/size: feature/M. Baseline: not-started.
Outcome: MediaAsset (stable logical identity, never a file path), MediaMetadata (streams/codecs/dimensions/rate/duration/colour/timecode/channel layout), MediaAvailability, and a relink algorithm that verifies asset identity/size/content-hash/metadata before reusing an origin hash all exist as pure domain types with no native type present.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-36.02 (domain types (MediaAsset/MediaStream/MediaMetadata/MediaAvailability) and the relink-by-content-hash algorithm; excludes the real native read/probe adapter): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\36-arcslate-project-and-timeline.md, anchor rule-wp-36.02

Entry condition: adoption slice ADOPT.06.arcslate is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] SLATE.01: source-stream time base rational types for MediaMetadata.rate/duration
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: ArcSlate:src/ArcForges.ArcSlate.Domain/Media/**
Unblocks: SLATE.04, SLATE.05, SLATE.06, SLATE.21, SLATE.24, SLATE.36

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline unit tests: offline-open structure/edit-decision preservation, relink verification and mismatch reporting, per-device-location-one-logical-asset test, structural no-native-type test.
Completion evidence for the ledger: Offline-open fixture; relink match/mismatch vectors; multi-device-location-one-asset fixture.
Notes: Deliberately split from the native read adapter (SLATE.04): everything here is pure domain logic testable against synthetic MediaMetadata, matching WP-36.02's own text that WP-37 (full playback) is explicitly NOT an undeclared prerequisite for this step.
```

```text
Execute ArcForges delivery task SLATE.04 — Native media metadata/probe read adapter (real import path).

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\arcslate.md (anchor task-slate-04).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\ArcSlate (integration owner: ArcSlate integration owner, the holder of roles/integration-arcslate).
Claim and handoff record: claims/slate-04 (python tools/delivery.py claim SLATE.04 --worker <name>); task branch task/slate-04 in ArcSlate; ledger record ledger/tasks/slate-04.md.
Kind/size: feature/L. Baseline: not-started.
Outcome: Importing a real media file populates MediaMetadata through the owned arc_media_probe ABI running behind the ContentSandbox boundary; malformed metadata and a child crash both preserve the native project (structure and edit decisions intact); content-origin is captured on import per the frozen carrier schema.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-36.02 (the real metadata/read adapter using the approved owned ABI and ContentSandbox, and the content-origin carrier/propagation/failure vectors recorded in this substep's evidence row): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\36-arcslate-project-and-timeline.md, anchor rule-wp-36.02
- WP-36:content-origin-carrier-propagation-failu Content-origin carrier/propagation/failure vectors (WP-36.02 required evidence addition; §8 additional completion requirement) (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\36-arcslate-project-and-timeline.md, package-level obligation

Entry condition: adoption slice ADOPT.06.arcslate is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] NAT.07: published arc_media_probe / arc_media_reader_stream export in the ArcForges.Native.Media package (managed MediaProbe wrapper)
- [artifact] SLATE.03: MediaAsset/MediaMetadata domain types to populate
Completion prerequisites (may start earlier; cannot complete before these are complete):
- [integration] NAT.14: production ContentSandbox.Runtime.<rid> parser composition (hostile-media containment)

Permitted write scope: ArcSlate:src/ArcForges.ArcSlate.Infrastructure/Media/ProbeAdapter/**
Permitted substitutes (never real integration evidence): SUB-media-probe-fixture: domain/library/editing/timeline logic against synthetic but schema-conformant metadata only; never hostile-input containment or real decode fidelity Real producer ['NAT.07']; removed by SLATE.15
Unblocks: SLATE.05, SLATE.14, SLATE.15, SLATE.35, SLATE.36

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Local only; sacrificial-process/child-crash test requires the WP-13.13 sandbox on the existing environment; offline unit tests against the fixture substitute are the default CI path per P2-017 (no live hostile-parsing CI).
Completion evidence for the ledger: Malformed-metadata-preserves-project run; child-crash-preserves-project run; content-origin carrier/propagation/failure vectors with payload and manifest hashes (WP-36.02 required evidence addition).
```

```text
Execute ArcForges delivery task SLATE.05 — Media library: bins, reference-in-place import, background analysis.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\arcslate.md (anchor task-slate-05).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\ArcSlate (integration owner: ArcSlate integration owner, the holder of roles/integration-arcslate).
Claim and handoff record: claims/slate-05 (python tools/delivery.py claim SLATE.05 --worker <name>); task branch task/slate-05 in ArcSlate; ledger record ledger/tasks/slate-05.md.
Kind/size: feature/M. Baseline: not-started.
Outcome: Bins organise assets; import defaults to reference-in-place and completes without waiting for background analysis/caches; an indexing failure never fails the import (the asset still exists, degraded and retryable).

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-36.03 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\36-arcslate-project-and-timeline.md, anchor rule-wp-36.03

Entry condition: adoption slice ADOPT.06.arcslate is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] SLATE.02: Project/MediaLibrary container
- [artifact] SLATE.03: MediaAsset identity
Completion prerequisites (may start earlier; cannot complete before these are complete):
- [integration] SLATE.04: real probe-populated metadata for a fully real import, as opposed to import against the SUB-media-probe-fixture

Permitted write scope: ArcSlate:src/ArcForges.ArcSlate.Domain/Media/Bin/**; ArcSlate:src/ArcForges.ArcSlate.Application/Import/**
Unblocks: SLATE.14, SLATE.35, SLATE.36

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline unit tests: import-completion-timing test, failed-indexing-still-imports test, large-library performance measurement (local, once).
Completion evidence for the ledger: Import timing results; indexing-failure-does-not-fail-import result.
```

```text
Execute ArcForges delivery task SLATE.06 — Timeline structural model: tracks, items, clips, transitions, markers.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\arcslate.md (anchor task-slate-06).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\ArcSlate (integration owner: ArcSlate integration owner, the holder of roles/integration-arcslate).
Claim and handoff record: claims/slate-06 (python tools/delivery.py claim SLATE.06 --worker <name>); task branch task/slate-06 in ArcSlate; ledger record ledger/tasks/slate-06.md.
Kind/size: feature/L. Baseline: not-started.
Outcome: Role-typed Track, TimelineItem, Clip (in/out points referencing a MediaAsset, never a file path), Transition and Marker/RangeMarker exist; one asset supports unlimited independent clip instances; track ordering/enable/lock/solo exist.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-36.04 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\36-arcslate-project-and-timeline.md, anchor rule-wp-36.04

Entry condition: adoption slice ADOPT.06.arcslate is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] SLATE.02: Sequence to hold tracks
- [artifact] SLATE.03: MediaAsset reference type
- [artifact] SLATE.01: TimeRange for clip in/out and timeline placement
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: ArcSlate:src/ArcForges.ArcSlate.Domain/Timeline/**
Shared resources (follow the owner protocol): RES-arcslate-build-config (append): Solution/project lists, central package versions and CI job lists are appended by the task that adds a project, dependency or job; dependency additions follow the dependency-admission policy with a reviewed receipt; lock files are regenerated after rebase and never hand-merged; the integration owner resolves ordering conflicts at merge.
Unblocks: SLATE.07, SLATE.10, SLATE.12, SLATE.18, SLATE.26, SLATE.29, SLATE.34, SLATE.38

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline unit tests: many-clips-one-asset independence, track operation coverage, structural no-file-path-in-clip test.
Completion evidence for the ledger: Many-clips-one-asset fixture; no-path structural test result.
```

```text
Execute ArcForges delivery task SLATE.07 — Edit command pipeline and placement operations.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\arcslate.md (anchor task-slate-07).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\ArcSlate (integration owner: ArcSlate integration owner, the holder of roles/integration-arcslate).
Claim and handoff record: claims/slate-07 (python tools/delivery.py claim SLATE.07 --worker <name>); task branch task/slate-07 in ArcSlate; ledger record ledger/tasks/slate-07.md.
Kind/size: feature/XL. Baseline: not-started.
Outcome: TimelineCommand infrastructure exists (expand link/group scope, validate locks/handles/overlaps/bounds, commit one undoable transaction, failure changes nothing, caller-supplied IDs replay identically) together with the placement-operation family, each exact per its declared semantics (e.g. Overwrite trims/splits only the target track interval; RippleDelete processes disjoint intervals latest-first so shift occurs once).

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-36.05 (the shared validate->expand-affected-set->one-transaction command pipeline, plus Insert/Overwrite/Move/Trim(in/out)/Split/Delete/Lift/RippleDelete/Extract/Duplicate exactly per slate.edit.v1 (26-product-behavior-profiles.md §4)): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\36-arcslate-project-and-timeline.md, anchor rule-wp-36.05

Entry condition: adoption slice ADOPT.06.arcslate is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] SLATE.06: Track/TimelineItem/Clip model to operate on
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: ArcSlate:src/ArcForges.ArcSlate.Timeline/**; ArcSlate:src/ArcForges.ArcSlate.Application/Editing/**
Shared resources (follow the owner protocol): RES-arcslate-registries (append): Each feature registers its own commands and capabilities through its module; registry files are append-only.; RES-contracts-schema-sources (append): Each closure task edits only its own domain proto or HTTP-schema files and adds its own sharded constraint and fixture files; shared inventories (package inventory, foundation inventory, constraint aggregate) are append-only per closure. A proto file with several contributing tasks (operator, policy/configuration) has one designated author task and the others request changes through it. The integration owner merges closure pull requests one at a time and the next author rebases and regenerates.
Unblocks: SLATE.08, SLATE.09, SLATE.33

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline unit tests: independent operation examples, collision/source-handle tests, undo/restart vectors, per-command exactness on its own grid (video frame-precise, audio sample-precise, TG-03).
Completion evidence for the ledger: Per-operation exactness and non-destructiveness results; one-transaction-or-nothing failure vectors.
Notes: Sized XL deliberately: 10 commands sharing one pipeline is one coherent reviewable outcome (the pipeline's affected-set/validation/transaction contract), not ten unrelated features; splitting further would fragment review of the shared contract.
```

```text
Execute ArcForges delivery task SLATE.08 — Relationship and retiming edit operations.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\arcslate.md (anchor task-slate-08).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\ArcSlate (integration owner: ArcSlate integration owner, the holder of roles/integration-arcslate).
Claim and handoff record: claims/slate-08 (python tools/delivery.py claim SLATE.08 --worker <name>); task branch task/slate-08 in ArcSlate; ledger record ledger/tasks/slate-08.md.
Kind/size: feature/L. Baseline: not-started.
Outcome: The remaining TL-06 operations exist on the same command pipeline: Roll adjusts a shared cut with both source handles; Slide trims outer neighbours to keep the combined boundary fixed; Link!=shared-identity is enforced; RetimeCurve composes rationals and projects once at the decode boundary with a reported inexact mapping; Snap converts pointer tolerance to ticks once and previews before commit.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-36.05 (RippleTrim/Roll/Slip/Slide/Group-Ungroup/Link-Unlink/Enable-Disable/ReorderTracks/Transition(create-delete)/Snap/Retime+RetimeCurve/ripple-marker-scope exactly per slate.edit.v1): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\36-arcslate-project-and-timeline.md, anchor rule-wp-36.05

Entry condition: adoption slice ADOPT.06.arcslate is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] SLATE.07: the shared command pipeline (validate/affected-set/transaction) and the placement operations these compose with (e.g. Roll needs two adjacent clips already placed)
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: ArcSlate:src/ArcForges.ArcSlate.Timeline/**
Shared resources (follow the owner protocol): RES-arcslate-registries (append): Each feature registers its own commands and capabilities through its module; registry files are append-only.; RES-contracts-schema-sources (append): Each closure task edits only its own domain proto or HTTP-schema files and adds its own sharded constraint and fixture files; shared inventories (package inventory, foundation inventory, constraint aggregate) are append-only per closure. A proto file with several contributing tasks (operator, policy/configuration) has one designated author task and the others request changes through it. The integration owner merges closure pull requests one at a time and the next author rebases and regenerates.
Unblocks: SLATE.12, SLATE.33

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline unit tests: reverse/freeze retime, linked-track refusal, collision/source-handle vectors, snap tie-priority (playhead>marker>clip>grid>earlier-tick).
Completion evidence for the ledger: Per-operation exactness results; retime no-drift-across-a-chain-of-speed-changes vector (TV-06).
```

```text
Execute ArcForges delivery task SLATE.09 — Undo/redo stack and composite command grouping.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\arcslate.md (anchor task-slate-09).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\ArcSlate (integration owner: ArcSlate integration owner, the holder of roles/integration-arcslate).
Claim and handoff record: claims/slate-09 (python tools/delivery.py claim SLATE.09 --worker <name>); task branch task/slate-09 in ArcSlate; ledger record ledger/tasks/slate-09.md.
Kind/size: feature/M. Baseline: not-started.
Outcome: Every edit command produces one undo transaction; a complex multi-command user gesture groups into one composite undo step; undo is demonstrably a different mechanism from checkpoint and crash recovery.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-36.06 (undo/redo as a distinct mechanism from checkpoint/recovery: composite operation grouping, explicit commit-boundary (a transient drag/preview is never a committed command)): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\36-arcslate-project-and-timeline.md, anchor rule-wp-36.06

Entry condition: adoption slice ADOPT.06.arcslate is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] SLATE.07: the command pipeline's one-transaction-per-command contract
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: ArcSlate:src/ArcForges.ArcSlate.Application/Undo/**
Unblocks: SLATE.11, SLATE.26

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline unit tests: undo-across-composite-operations, undo-is-not-recovery distinction test.
Completion evidence for the ledger: Composite-undo fixture; three-mechanism distinction test contribution (paired with SLATE.11's checkpoint/recovery evidence).
```

```text
Execute ArcForges delivery task SLATE.10 — Project persistence and store infrastructure (V1 migration baseline).

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\arcslate.md (anchor task-slate-10).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\ArcSlate (integration owner: ArcSlate integration owner, the holder of roles/integration-arcslate).
Claim and handoff record: claims/slate-10 (python tools/delivery.py claim SLATE.10 --worker <name>); task branch task/slate-10 in ArcSlate; ledger record ledger/tasks/slate-10.md.
Kind/size: feature/M. Baseline: not-started.
Outcome: ArcSlate.Infrastructure persists Project/Sequence/Timeline/MediaLibrary through the platform's single write path; fixtures/formats/arcslate/v1/ exists as the V1 project fixture; the storage schema version equals the highest applied migration.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-36:database-impact-arcslate-project-store-a Database impact: ArcSlate project store and its V1 migration baseline (§6) (package-level: §6 Impacts row "Database: the ArcSlate project store and its V1 migration baseline"; §4 ArcSlate.Infrastructure project store/media index/migration set; package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\36-arcslate-project-and-timeline.md, package-level obligation

Entry condition: adoption slice ADOPT.06.arcslate is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] PLT.01: published store abstraction with the single transactional write path (validate->authorize->begin->apply->journal->advance revision->commit->notify)
- [artifact] PLT.04: published migration runner (numbered, transactional-per-step, idempotent, resumable)
- [artifact] SLATE.02: Project/Sequence domain types to persist
- [artifact] SLATE.06: Timeline/Track/Clip domain types to persist
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: ArcSlate:src/ArcForges.ArcSlate.Infrastructure/Store/**; ArcSlate:fixtures/formats/arcslate/v1/**
Shared resources (follow the owner protocol): RES-arcslate-migrations (append): Numbered migrations are allocated at merge by the integration owner (a rebase renumbers pending migrations); each migration is forward-only with its recovery and downgrade-refusal tests; no task edits a merged migration.
Unblocks: SLATE.11, SLATE.26, SLATE.37

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline unit tests only; no live database service.
Completion evidence for the ledger: Migration-forward-from-V1 fixture result.
```

```text
Execute ArcForges delivery task SLATE.11 — Project checkpoints, crash recovery and project-version migration.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\arcslate.md (anchor task-slate-11).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\ArcSlate (integration owner: ArcSlate integration owner, the holder of roles/integration-arcslate).
Claim and handoff record: claims/slate-11 (python tools/delivery.py claim SLATE.11 --worker <name>); task branch task/slate-11 in ArcSlate; ledger record ledger/tasks/slate-11.md.
Kind/size: feature/L. Baseline: not-started.
Outcome: A checkpoint is an explicit user action distinct from both undo and autosave; a kill mid-edit recovers to the last committed boundary and reports what was lost; a prior-version project migrates forward with semantic (not merely structural) preservation.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-36.06 (project checkpoints as an explicit user mechanism distinct from undo; crash recovery to the last committed boundary with explicit loss reporting; migration from prior project versions with semantic preservation): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\36-arcslate-project-and-timeline.md, anchor rule-wp-36.06

Entry condition: adoption slice ADOPT.06.arcslate is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] PLT.02: published append-only journal with durable-before-acknowledged commits
- [artifact] PLT.03: published snapshot/recovery mechanism with typed outcomes (clean / recovered-with-loss / unrecoverable-with-evidence)
- [artifact] SLATE.09: the undo mechanism this task must remain distinct from
- [artifact] SLATE.10: the project store to checkpoint/recover
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: ArcSlate:src/ArcForges.ArcSlate.Application/Recovery/**
Shared resources (follow the owner protocol): RES-arcslate-migrations (append): Numbered migrations are allocated at merge by the integration owner (a rebase renumbers pending migrations); each migration is forward-only with its recovery and downgrade-refusal tests; no task edits a merged migration.
Unblocks: SLATE.14

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline unit tests: kill-during-edit recovery run (local process-kill simulation), migration semantic-comparison test.
Completion evidence for the ledger: Kill-during-edit recovery result; three-mechanism distinction result; migration semantic-preservation comparison.
```

```text
Execute ArcForges delivery task SLATE.12 — Slate.project.v1/graph.v1 wire projection: bins, generators, nesting, adjustment, title/subtitle, cycle rejection.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\arcslate.md (anchor task-slate-12).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\ArcSlate (integration owner: ArcSlate integration owner, the holder of roles/integration-arcslate).
Claim and handoff record: claims/slate-12 (python tools/delivery.py claim SLATE.12 --worker <name>); task branch task/slate-12 in ArcSlate; ledger record ledger/tasks/slate-12.md.
Kind/size: feature/L. Baseline: not-started.
Outcome: The full slate.project.v1/graph.v1 wire projection round-trips metadata-only (no media bytes) with every edit and Offline Media preserved; nested-sequence and graph cycles are rejected; an unknown imported effect definition is retained and stays inert rather than silently activated.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-36:unlabelled-final-review-closure-complete Unlabelled final-review closure: complete slate.project.v1/graph.v1 model, generators/nesting/adjustment/title/subtitle, cycle rejection, unknown-effect inert (the unlabelled final-review closure paragraph: "Implement the complete slate.project.v1/graph.v1 model: bins, exact sequence video/audio/colour config, track roles, generators/nesting/adjustment/title/subtitle, graph definition/instance identity and keyframe time scope. Metadata-only cross-device round-trip preserves every edit with Offline Media. Reject graph/nesting cycles and preserve unknown imported effects inert."; package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\36-arcslate-project-and-timeline.md, package-level obligation

Entry condition: adoption slice ADOPT.06.arcslate is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] SLATE.06: Timeline/Track/TimelineItem structural model to project
- [artifact] SLATE.08: nested-sequence and adjustment-layer semantics from the edit operation set
- [contract] CON.06: published slate.project.v1 / slate.graph.v1 generated records in ArcForges.Contracts.LocalRpc.Slate (wire keys per 26-product-behavior-profiles.md §4: transform/crop/opacity/colourAdjustment/audioGain/pan/composite/audioMix, generated-source keys colour/gradient/counter/testPattern/title)
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: ArcSlate:src/ArcForges.ArcSlate.Infrastructure/Wire/**
Shared resources (follow the owner protocol): RES-contracts-schema-sources (append): Each closure task edits only its own domain proto or HTTP-schema files and adds its own sharded constraint and fixture files; shared inventories (package inventory, foundation inventory, constraint aggregate) are append-only per closure. A proto file with several contributing tasks (operator, policy/configuration) has one designated author task and the others request changes through it. The integration owner merges closure pull requests one at a time and the next author rebases and regenerates.
Unblocks: SLATE.14, SLATE.42

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline unit tests: metadata-only cross-device round-trip fixture, cycle-rejection negative test, unknown-effect-preserved-inert test.
Completion evidence for the ledger: Round-trip-with-Offline-Media fixture; cycle-rejection vectors; unknown-effect inertness proof.
```

```text
Execute ArcForges delivery task SLATE.13 — ArcSlate reference-coverage drift check (maintenance).

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\arcslate.md (anchor task-slate-13).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\ArcSlate (integration owner: ArcSlate integration owner, the holder of roles/integration-arcslate).
Claim and handoff record: claims/slate-13 (python tools/delivery.py claim SLATE.13 --worker <name>); task branch task/slate-13 in Design; ledger record ledger/tasks/slate-13.md.
Kind/size: acceptance/S. Baseline: not-started.
Outcome: ArcVideo (caf5651) and ArcVideoFoundation (139eeca) are re-diffed against their bound commits; changed rows are reassessed, newly introduced upstream material gets a disposition (mapped or excluded, never auto-adopted), and the licence position is re-confirmed.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-36.07 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\36-arcslate-project-and-timeline.md, anchor rule-wp-36.07

Entry condition: adoption slice ADOPT.06.arcslate is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- none
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Design:docs/assurance/reference-coverage/arcslate-arcvideo.md
Unblocks: SLATE.14

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Design-stage comparison only; no build/test involved. Reads two reference repositories read-only (never executed, per MT-04).
Completion evidence for the ledger: Drift report: changed-file list with row reassessment, new-material list with disposition, licence re-verification statement.
Notes: Not blocked by anything else in this area and touches no ArcSlate source; can run in parallel with all other SLATE tasks. Its only real prerequisite is that the two reference repositories (C:\MyFile\ArcForges\ArcVideo, C:\MyFile\ArcForges\ArcVideoFoundation per the matrix's local paths) remain available read-only.
```

```text
Execute ArcForges delivery task SLATE.14 — Closure: owned-artifact and real-integration receipt.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\arcslate.md (anchor task-slate-14).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\ArcSlate (integration owner: ArcSlate integration owner, the holder of roles/integration-arcslate).
Claim and handoff record: claims/slate-14 (python tools/delivery.py claim SLATE.14 --worker <name>); task branch task/slate-14 in ArcSlate; ledger record ledger/tasks/slate-14.md.
Kind/size: acceptance/S. Baseline: not-started.
Outcome: One recorded receipt (source commit, candidate hashes, actual runtime/OS/provider, scenario, result, real-versus-fixture status per field) demonstrates that the exact timeline/edit/recovery fixtures from SLATE.01-12 remain valid and that no package or wire boundary rounds a frame/time value.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-36.90 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\36-arcslate-project-and-timeline.md, anchor rule-wp-36.90

Entry condition: adoption slice ADOPT.06.arcslate is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] SLATE.01: all WP-36 tasks complete
- [artifact] SLATE.11: all WP-36 tasks complete
- [artifact] SLATE.12: all WP-36 tasks complete
- [artifact] SLATE.13: drift report exists
- [artifact] SLATE.04: package task delivered
- [artifact] SLATE.05: package task delivered
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: ArcSlate:docs/evidence/wp36-90-receipt.md
Unblocks: REL.03

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Re-run of SLATE.01-12's existing offline unit suites plus a policy test that no rounding site outside RP-02's five exists.
Completion evidence for the ledger: The consolidated receipt itself.
```

```text
Execute ArcForges delivery task SLATE.15 — Native media boundary consumption (ArcSlate.Media wrapper and safety suite).

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\arcslate.md (anchor task-slate-15).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\ArcSlate (integration owner: ArcSlate integration owner, the holder of roles/integration-arcslate).
Claim and handoff record: claims/slate-15 (python tools/delivery.py claim SLATE.15 --worker <name>); task branch task/slate-15 in ArcSlate; ledger record ledger/tasks/slate-15.md.
Kind/size: feature/L. Baseline: not-started.
Outcome: ArcSlate.Media consumes the exact published ArcForges.Native.Media/.Colour/.Image/.Otio/.Graphics packages with managed input validation, safe handles and a sacrificial-process integration suite; sanitiser builds run in CI; every native dependency's licence position is recorded; no native type escapes the media layer. Satisfies PG-03 for ArcSlate.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-37.00 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\37-arcslate-playback-and-processing.md, anchor rule-wp-37.00

Entry condition: adoption slice ADOPT.06.arcslate is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] NAT.06: the compiled common ABI/preamble/pack-8 record layer all family wrappers build on
- [artifact] NAT.07: published functional arc_media_reader_*/probe exports in ArcForges.Native.Media (beyond the current 3-function version/build/error probe)
- [artifact] NAT.08: published arc_media_writer_*/convert/resample exports
- [artifact] SLATE.04: native media metadata and probe adapter
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: ArcSlate:src/ArcForges.ArcSlate.Media/**; ArcSlate:src/ArcForges.ArcSlate.Native/**
Shared resources (follow the owner protocol): RES-arcslate-build-config (append): Solution/project lists, central package versions and CI job lists are appended by the task that adds a project, dependency or job; dependency additions follow the dependency-admission policy with a reviewed receipt; lock files are regenerated after rebase and never hand-merged; the integration owner resolves ordering conflicts at merge.; RES-workstation-build-slot (exclusive): Exclusive per workstation for the duration of each CPU-heavy local build or test, through the workstation lock rather than a Plan lease: run the command as `python tools/delivery.py build-slot run --worker <name> --task <task> -- <command>` with the Plan repository tool, which holds the lock directory `.arcforges/build-slot` in the user profile with an owner record and heartbeat and recovers a lock whose holder stopped. Coding and review continue while a build waits; CI capacity is not limited by this rule.
Permitted substitutes (never real integration evidence): SUB-no-op-media-adapter: wiring/composition only, never decode/codec correctness Real producer ['NAT.07', 'NAT.08']; removed by SLATE.23
Unblocks: SLATE.16, SLATE.19, SLATE.23

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): ABI conformance and version-mismatch rejection tests, ownership/handle-lifetime tests, sanitiser runs, sacrificial-process crash tests, domain-purity test -- all local, once, per P2-017 (no hosted native CI).
Completion evidence for the ledger: ABI version-negotiation result; leak-free handle-lifetime proof; clean sanitiser run; sacrificial-process crash-containment result; PG-03 licence-position record.
Notes: First real ArcSlate-side exercise of the native P/Invoke boundary; WP-13.03 (Probe D) already proved decode+sync feasibility in isolation, but this task is where ArcSlate's own AOT-published, sanitiser-clean, sacrificial-process-tested consumption is proven for the first time. A failure here (ABI mismatch, handle leak, AOT trimming of a marshalled type) invalidates SLATE.16 through SLATE.31.
```

```text
Execute ArcForges delivery task SLATE.16 — Decode and pooled buffers.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\arcslate.md (anchor task-slate-16).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\ArcSlate (integration owner: ArcSlate integration owner, the holder of roles/integration-arcslate).
Claim and handoff record: claims/slate-16 (python tools/delivery.py claim SLATE.16 --worker <name>); task branch task/slate-16 in ArcSlate; ledger record ledger/tasks/slate-16.md.
Kind/size: feature/L. Baseline: not-started.
Outcome: Demux and decode run through the boundary into pooled buffers; buffers return on every path including failure; pool exhaustion is measured and surfaced; hardware acceleration is discovered at runtime with a proven software fallback whose output matches within declared tolerance.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-37.01 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\37-arcslate-playback-and-processing.md, anchor rule-wp-37.01

Entry condition: adoption slice ADOPT.06.arcslate is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] SLATE.15: the ABI boundary/wrapper this decode path calls through
Completion prerequisites (may start earlier; cannot complete before these are complete):
- [integration] NAT.14: production ContentSandbox.Runtime.<rid> parser composition

Permitted write scope: ArcSlate:src/ArcForges.ArcSlate.Media/Decode/**
Shared resources (follow the owner protocol): RES-arcslate-golden-media (append): Golden media and reference outputs are added per task with provenance; they are never regenerated to make a test pass; large media follows the repository storage policy.; RES-workstation-build-slot (exclusive): Exclusive per workstation for the duration of each CPU-heavy local build or test, through the workstation lock rather than a Plan lease: run the command as `python tools/delivery.py build-slot run --worker <name> --task <task> -- <command>` with the Plan repository tool, which holds the lock directory `.arcforges/build-slot` in the user profile with an owner record and heartbeat and recovers a lock whose holder stopped. Coding and review continue while a build waits; CI capacity is not limited by this rule.
Unblocks: SLATE.17, SLATE.20, SLATE.21, SLATE.30

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Long-run buffer accounting, pool-exhaustion behaviour, forced-software-path equivalence, decode-capability disclosure -- local, once, on the existing environment.
Completion evidence for the ledger: Buffer-leak-free soak result; pool-exhaustion surfaced result; software-vs-hardware equivalence-within-tolerance result; PG-22 hostile-input containment result.
Notes: PG-22 anchor for ArcSlate: this is where hostile-media containment is proven for the whole product, not merely for PDF/Notes.
```

```text
Execute ArcForges delivery task SLATE.17 — Playback engine, clock and scheduler.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\arcslate.md (anchor task-slate-17).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\ArcSlate (integration owner: ArcSlate integration owner, the holder of roles/integration-arcslate).
Claim and handoff record: claims/slate-17 (python tools/delivery.py claim SLATE.17 --worker <name>); task branch task/slate-17 in ArcSlate; ledger record ledger/tasks/slate-17.md.
Kind/size: feature/L. Baseline: not-started.
Outcome: The playback engine is driven by the timeline clock, decoupled from editing so an edit invalidates and re-requests incrementally without stalling playback; frames may drop but the audio/timeline clock stays correct; playback quality state (realtime/reduced/proxy/dropping/requires-render) is computed and visible.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-37.02 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\37-arcslate-playback-and-processing.md, anchor rule-wp-37.02

Entry condition: adoption slice ADOPT.06.arcslate is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] SLATE.16: decoded frames/audio buffers to schedule
- [artifact] SLATE.01: the exact tick/grid time model
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: ArcSlate:src/ArcForges.ArcSlate.Playback/**
Unblocks: SLATE.22

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Edit-during-playback tests, A/V synchronisation measurement under induced load, long-playback drift test, quality-state coverage -- local, once.
Completion evidence for the ledger: Sync-under-load measurement; long-run drift measurement (must show zero); quality-state coverage matrix.
Notes: This is where WP-13.03's (Probe D) isolated decode+sync proof becomes a real, editable-while-playing product runtime under load -- the specific risk ND-04 in implementation-sequence.md names ('ArcSlate does not meet... synchronisation... problems for the first time at work package 36'). A narrow A/V-sync-under-load spike is worth running before building the full quality-state UI on top.
```

```text
Execute ArcForges delivery task SLATE.18 — Processing graph and keyframe engine (pure evaluation).

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\arcslate.md (anchor task-slate-18).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\ArcSlate (integration owner: ArcSlate integration owner, the holder of roles/integration-arcslate).
Claim and handoff record: claims/slate-18 (python tools/delivery.py claim SLATE.18 --worker <name>); task branch task/slate-18 in ArcSlate; ledger record ledger/tasks/slate-18.md.
Kind/size: feature/L. Baseline: not-started.
Outcome: A typed acyclic ProcessingGraph evaluates per node kind with typed, non-arbitrarily-connectable ports; EffectDefinition and EffectInstance are distinct; keyframe time is pinned to its declared clip-local-or-sequence scope and never silently switches, including across a clip move; bezier evaluation uses the exact cubic-Hermite tangent contract.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-37.03 (graph topology/ports/EffectDefinition-vs-Instance/keyframe-scope/curve-evaluation engine, including the built-in definitions and formulas of 26-product-behavior-profiles.md §5 (transform/crop/opacity/colourAdjustment/audioGain/pan, hold/linear/bezier keyframe evaluation, RetimeCurve); excludes execution of any node that requires a native pixel/sample operation): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\37-arcslate-playback-and-processing.md, anchor rule-wp-37.03

Entry condition: adoption slice ADOPT.06.arcslate is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] SLATE.06: TimelineItem/Clip/Track to attach graphs and adjustment layers to
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: ArcSlate:src/ArcForges.ArcSlate.Processing/**
Shared resources (follow the owner protocol): RES-arcslate-build-config (append): Solution/project lists, central package versions and CI job lists are appended by the task that adds a project, dependency or job; dependency additions follow the dependency-admission policy with a reviewed receipt; lock files are regenerated after rebase and never hand-merged; the integration owner resolves ordering conflicts at merge.
Unblocks: SLATE.19, SLATE.20, SLATE.23, SLATE.24

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Offline unit tests: per-node-kind evaluation correctness, keyframe-scope-across-a-clip-move test, definition-vs-instance distinction test, adjustment-layer ordering test.
Completion evidence for the ledger: Per-node-kind evaluation results; keyframe-scope-never-switches result.
```

```text
Execute ArcForges delivery task SLATE.19 — Native-backed processing nodes (convert, scale, transform, colour-adjustment execution).

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\arcslate.md (anchor task-slate-19).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\ArcSlate (integration owner: ArcSlate integration owner, the holder of roles/integration-arcslate).
Claim and handoff record: claims/slate-19 (python tools/delivery.py claim SLATE.19 --worker <name>); task branch task/slate-19 in ArcSlate; ledger record ledger/tasks/slate-19.md.
Kind/size: feature/M. Baseline: not-started.
Outcome: Transform/crop/composite/generated-source nodes actually produce pixel output through the native convert path when evaluated, matching the CPU reference formulas within the declared 1e-5 tolerance; the CPU graph definition remains the oracle for any optional GPU acceleration.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-37.03 (execution of graph nodes that require a real pixel/sample operation (video convert/scale/transform), and generated media (colour/gradient/counter/test-pattern/title per 26§5)): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\37-arcslate-playback-and-processing.md, anchor rule-wp-37.03

Entry condition: adoption slice ADOPT.06.arcslate is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] SLATE.18: the graph/port/keyframe engine these nodes plug into
- [artifact] SLATE.15: the ABI boundary
- [artifact] NAT.08: published arc_media_video_convert export
- [artifact] NAT.15: published ArcGraphicsNative CPU surface
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: ArcSlate:src/ArcForges.ArcSlate.Processing/NativeNodes/**
Shared resources (follow the owner protocol): RES-workstation-build-slot (exclusive): Exclusive per workstation for the duration of each CPU-heavy local build or test, through the workstation lock rather than a Plan lease: run the command as `python tools/delivery.py build-slot run --worker <name> --task <task> -- <command>` with the Plan repository tool, which holds the lock directory `.arcforges/build-slot` in the user profile with an owner record and heartbeat and recovers a lock whose holder stopped. Coding and review continue while a build waits; CI capacity is not limited by this rule.
Unblocks: SLATE.23, SLATE.25, SLATE.28

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Reference-vector comparison at 1e-5 per-channel tolerance before quantisation; identity-operation exactness check.
Completion evidence for the ledger: Per-formula reference-vector results (exposure/contrast/saturation/composite/crop/transform).
```

```text
Execute ArcForges delivery task SLATE.20 — Audio processing chain and sample-accurate mixing.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\arcslate.md (anchor task-slate-20).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\ArcSlate (integration owner: ArcSlate integration owner, the holder of roles/integration-arcslate).
Claim and handoff record: claims/slate-20 (python tools/delivery.py claim SLATE.20 --worker <name>); task branch task/slate-20 in ArcSlate; ledger record ledger/tasks/slate-20.md.
Kind/size: feature/XL. Baseline: not-started.
Outcome: Per-non-overlapping-track-cut sample ownership is assigned (never rounded) per BO-02, all track/transition contributions are summed once at each output index (BO-02/BO-03), filter/resampler padding primes DSP without being emitted independently, and gain/pan/dissolve/crossfade use the exact formulas of 26§5 (10^(dB/20) gain, equal-power pan/crossfade). Satisfies the PG-20 per-track-cut-ownership evidence for ArcSlate.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-37.04 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\37-arcslate-playback-and-processing.md, anchor rule-wp-37.04

Entry condition: adoption slice ADOPT.06.arcslate is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] SLATE.01: the sample grid and half-open range algebra this mixing rule is defined over
- [artifact] SLATE.18: the processing graph's audio-buffer port type and node composition
- [artifact] SLATE.16: decoded audio buffers to mix
- [artifact] NAT.08: published resampler push/drain exports with retained delay
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: ArcSlate:src/ArcForges.ArcSlate.Audio/**
Shared resources (follow the owner protocol): RES-arcslate-golden-media (append): Golden media and reference outputs are added per task with provenance; they are never regenerated to make a test pass; large media follows the repository storage policy.; RES-workstation-build-slot (exclusive): Exclusive per workstation for the duration of each CPU-heavy local build or test, through the workstation lock rather than a Plan lease: run the command as `python tools/delivery.py build-slot run --worker <name> --task <task> -- <command>` with the Plan repository tool, which holds the lock directory `.arcforges/build-slot` in the user profile with an owner record and heartbeat and recovers a lock whose holder stopped. Coding and review continue while a build waits; CI capacity is not limited by this rule.
Unblocks: SLATE.23, SLATE.28

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Two-mixed-tracks/dissolve/track-gap/resampler-priming/NTSC-frame-one-boundary vectors, each asserting exactly one mixed output sample at index k; mixing-against-reference-output test; sync-under-load test with video.
Completion evidence for the ledger: The TV-08 fixture (a cut at frame 1 of 30000/1001 fps @ 48 kHz emits sample 1601 exactly once and 1602 exactly once); mixing-vs-reference results.
Notes: The design doc devotes a full worked example (23-simulator-and-interchange.md §3.4) to exactly the boundary-duplication defect this task must avoid (directional outward rounding on both sides of a cut double-emits the boundary sample). This is a subtle, easy-to-get-wrong correctness area that also anchors PG-20; worth a narrow proof against the TV-08 fixture before building the full mixing/gain-staging UI on top.
```

```text
Execute ArcForges delivery task SLATE.21 — Proxies and derived caches.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\arcslate.md (anchor task-slate-21).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\ArcSlate (integration owner: ArcSlate integration owner, the holder of roles/integration-arcslate).
Claim and handoff record: claims/slate-21 (python tools/delivery.py claim SLATE.21 --worker <name>); task branch task/slate-21 in ArcSlate; ledger record ledger/tasks/slate-21.md.
Kind/size: feature/L. Baseline: not-started.
Outcome: Proxy generation/policy per project and per asset, plus render/thumbnail/waveform caches, all exist as derived stores; a clip never knows which representation is in use; deleting every cache leaves the project fully intact; render output is identical with proxies enabled and disabled.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-37.05 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\37-arcslate-playback-and-processing.md, anchor rule-wp-37.05

Entry condition: adoption slice ADOPT.06.arcslate is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] SLATE.03: MediaAsset identity for cache keys
- [artifact] SLATE.16: decode to generate proxy/thumbnail source frames
- [artifact] NAT.08: published media writer to encode proxy media
- [artifact] NAT.11: published still-image codec export (PNG) for thumbnails
- [artifact] PLT.07: published derived-store abstraction with rebuild semantics and storage-pressure eviction
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: ArcSlate:src/ArcForges.ArcSlate.Infrastructure/DerivedCaches/**
Shared resources (follow the owner protocol): RES-arcslate-migrations (append): Numbered migrations are allocated at merge by the integration owner (a rebase renumbers pending migrations); each migration is forward-only with its recovery and downgrade-refusal tests; no task edits a merged migration.
Unblocks: SLATE.23

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Proxy-equivalence test (output identical with proxies on/off), delete-all-caches-and-rebuild test, clip-ignorance structural test, cache eviction under storage pressure -- local, once.
Completion evidence for the ledger: Proxy-on/off output-identity result; delete-all-caches-leaves-project-intact result.
```

```text
Execute ArcForges delivery task SLATE.22 — Viewer: source and sequence, professional transport.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\arcslate.md (anchor task-slate-22).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\ArcSlate (integration owner: ArcSlate integration owner, the holder of roles/integration-arcslate).
Claim and handoff record: claims/slate-22 (python tools/delivery.py claim SLATE.22 --worker <name>); task branch task/slate-22 in ArcSlate; ledger record ledger/tasks/slate-22.md.
Kind/size: feature/M. Baseline: not-started.
Outcome: Source and sequence viewers exist with play/pause/frame-step/shuttle/in-out-marking/go-to-timecode/loop/rate, fully keyboard-operable, with playback quality state visible.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-37.06 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\37-arcslate-playback-and-processing.md, anchor rule-wp-37.06

Entry condition: adoption slice ADOPT.06.arcslate is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] SLATE.17: the playback engine/clock/quality-state this viewer displays and controls
- [artifact] NAT.15: published ArcGraphicsNative presentable-surface exports
- [artifact] PLT.27: published windows/panels/layout foundation
- [artifact] PLT.28: published command system
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: ArcSlate:src/ArcForges.ArcSlate.Presentation/Viewer/**; ArcSlate:src/ArcForges.ArcSlate.Desktop/Viewer/**
Unblocks: PLT.56, SLATE.23

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Transport coverage, frame-accuracy-at-step-boundary assertions, keyboard-only operation test.
Completion evidence for the ledger: Frame-accurate transport results; keyboard-only operability result.
```

```text
Execute ArcForges delivery task SLATE.23 — Closure: owned-artifact and real-integration receipt.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\arcslate.md (anchor task-slate-23).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\ArcSlate (integration owner: ArcSlate integration owner, the holder of roles/integration-arcslate).
Claim and handoff record: claims/slate-23 (python tools/delivery.py claim SLATE.23 --worker <name>); task branch task/slate-23 in ArcSlate; ledger record ledger/tasks/slate-23.md.
Kind/size: acceptance/S. Baseline: not-started.
Outcome: A clean AOT package consumer plus representative decode, synchronisation, cancellation, damaged-input and native dependency loading pass on every supported RID; the receipt records exact artifacts and real-versus-fixture status per field.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-37.90 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\37-arcslate-playback-and-processing.md, anchor rule-wp-37.90
- WP-37:unlabelled-final-review-closure-consume Unlabelled final-review closure: consume actual Platform media packages, portable baseline codec/graph/audio-grid verification, unsupported-capability-cannot-be-advertised, font/colour/source identity affects render snapshot (the unlabelled final-review closure paragraph: consume actual Platform media packages, test portable baseline render codecs/graph-source semantics/audio-grid mixing together, confirm unsupported native capabilities cannot be advertised, and that font/colour/source identity affects the render snapshot (the last clause is jointly satisfied here and at SLATE.26); package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\37-arcslate-playback-and-processing.md, package-level obligation

Entry condition: adoption slice ADOPT.06.arcslate is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] SLATE.15: all WP-37 tasks complete
- [artifact] SLATE.22: all WP-37 tasks complete
- [artifact] SLATE.18: package task delivered
- [artifact] SLATE.19: package task delivered
- [artifact] SLATE.20: package task delivered
- [artifact] SLATE.21: package task delivered
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: ArcSlate:docs/evidence/wp37-90-receipt.md
Unblocks: REL.03

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Clean AOT publish + representative decode/sync/cancellation/damaged-input/dependency-loading run on every admitted RID, local, once.
Completion evidence for the ledger: The consolidated receipt.
```

```text
Execute ArcForges delivery task SLATE.24 — Colour management: input interpretation, working config, display/export transform separation.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\arcslate.md (anchor task-slate-24).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\ArcSlate (integration owner: ArcSlate integration owner, the holder of roles/integration-arcslate).
Claim and handoff record: claims/slate-24 (python tools/delivery.py claim SLATE.24 --worker <name>); task branch task/slate-24 in ArcSlate; ledger record ledger/tasks/slate-24.md.
Kind/size: feature/L. Baseline: not-started.
Outcome: Per-asset input colour metadata with a non-destructive override, a project/sequence working colour configuration, and strictly separate viewer-display and export transforms all exist; the colour domain holds only semantic configuration, with the OCIO backend fully behind an infrastructure interface.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-38.00 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\38-arcslate-render-and-colour.md, anchor rule-wp-38.00

Entry condition: adoption slice ADOPT.06.arcslate is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] SLATE.18: the processing graph's colour-data port type
- [artifact] SLATE.03: MediaAsset input colour metadata
- [artifact] NAT.10: published arc_color_config_open/arc_color_processor_create/arc_color_apply exports (immutable OCIO config/processor)
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: ArcSlate:src/ArcForges.ArcSlate.Color/**
Shared resources (follow the owner protocol): RES-arcslate-build-config (append): Solution/project lists, central package versions and CI job lists are appended by the task that adds a project, dependency or job; dependency additions follow the dependency-admission policy with a reviewed receipt; lock files are regenerated after rebase and never hand-merged; the integration owner resolves ordering conflicts at merge.; RES-workstation-build-slot (exclusive): Exclusive per workstation for the duration of each CPU-heavy local build or test, through the workstation lock rather than a Plan lease: run the command as `python tools/delivery.py build-slot run --worker <name> --task <task> -- <command>` with the Plan repository tool, which holds the lock directory `.arcforges/build-slot` in the user profile with an owner record and heartbeat and recovers a lock whose holder stopped. Coding and review continue while a build waits; CI capacity is not limited by this rule.
Unblocks: SLATE.27, SLATE.32

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Round-trip colour tests against reference values, override-non-destructiveness assertion, display-transform-never-alters-export test, domain-purity test on the colour model.
Completion evidence for the ledger: Round-trip colour results; display/export separation proof; domain-purity result.
```

```text
Execute ArcForges delivery task SLATE.25 — Video scopes (waveform, vectorscope, histogram, parade).

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\arcslate.md (anchor task-slate-25).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\ArcSlate (integration owner: ArcSlate integration owner, the holder of roles/integration-arcslate).
Claim and handoff record: claims/slate-25 (python tools/delivery.py claim SLATE.25 --worker <name>); task branch task/slate-25 in ArcSlate; ledger record ledger/tasks/slate-25.md.
Kind/size: feature/M. Baseline: not-started.
Outcome: Waveform/vectorscope/histogram/parade all read correctly against reference signals as derived views over the current frame or range, each stating its measurement point in the pipeline explicitly.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-38.01 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\38-arcslate-render-and-colour.md, anchor rule-wp-38.01

Entry condition: adoption slice ADOPT.06.arcslate is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] SLATE.19: processed frame buffers to measure
- [artifact] NAT.15: published graphics CPU surface
- [artifact] PLT.27: published panel foundation
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: ArcSlate:src/ArcForges.ArcSlate.Visualization/**
Unblocks: SLATE.32

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Reference-signal tests per scope, measurement-point disclosure assertion, performance test at playback rate.
Completion evidence for the ledger: Per-scope reference-signal results.
```

```text
Execute ArcForges delivery task SLATE.26 — Render planning and immutable snapshot binding.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\arcslate.md (anchor task-slate-26).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\ArcSlate (integration owner: ArcSlate integration owner, the holder of roles/integration-arcslate).
Claim and handoff record: claims/slate-26 (python tools/delivery.py claim SLATE.26 --worker <name>); task branch task/slate-26 in ArcSlate; ledger record ledger/tasks/slate-26.md.
Kind/size: feature/M. Baseline: not-started.
Outcome: A RenderRequest captures sequence/range/preset/destination/options and binds an immutable project+sequence revision snapshot including font/colour/source-hash identities; editing during a render never affects that running render; proxy render is opt-in and recorded in output metadata.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-38.02 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\38-arcslate-render-and-colour.md, anchor rule-wp-38.02
- WP-37:final-review-closure-clause-font-colour final-review closure clause: font/colour/source identity affects the render snapshot (the snapshot-binding half; the native-package-consumption half is SLATE.23) (final-review closure clause: font/colour/source identity affects the render snapshot (the snapshot-binding half; the native-package-consumption half is SLATE.23)): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\37-arcslate-playback-and-processing.md, package-level obligation
- WP-37:unlabelled-final-review-closure-consume Unlabelled final-review closure: consume actual Platform media packages, portable baseline codec/graph/audio-grid verification, unsupported-capability-cannot-be-advertised, font/colour/source identity affects render snapshot (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\37-arcslate-playback-and-processing.md, package-level obligation

Entry condition: adoption slice ADOPT.06.arcslate is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] SLATE.06: the timeline structure to snapshot
- [artifact] SLATE.09: the undo/revision concept this snapshot binds to
- [artifact] SLATE.10: the project store, to read a committed revision
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: ArcSlate:src/ArcForges.ArcSlate.Rendering/Planning/**; ArcSlate:src/ArcForges.ArcSlate.Domain/Render/**
Unblocks: SLATE.28, SLATE.39

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Edit-during-render test asserting output is unaffected; snapshot-binding assertion; proxy-render disclosure test.
Completion evidence for the ledger: Edit-during-render-unaffected result; snapshot-binding proof.
```

```text
Execute ArcForges delivery task SLATE.27 — Export presets and encoding validation.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\arcslate.md (anchor task-slate-27).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\ArcSlate (integration owner: ArcSlate integration owner, the holder of roles/integration-arcslate).
Claim and handoff record: claims/slate-27 (python tools/delivery.py claim SLATE.27 --worker <name>); task branch task/slate-27 in ArcSlate; ledger record ledger/tasks/slate-27.md.
Kind/size: feature/M. Baseline: not-started.
Outcome: Reusable ExportPresets cover container/codec/rate/resolution/colour-output/audio configuration; an invalid combination is refused before a ProductJob starts, never failing mid-render; the three portable baseline profiles (matroska-ffv1-pcm, wav-pcm, mp4-mpeg4-aac) validate exactly per the declared bounds (even dimensions 16-8192, sequence-representable rate, etc.).

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-38.04 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\38-arcslate-render-and-colour.md, anchor rule-wp-38.04

Entry condition: adoption slice ADOPT.06.arcslate is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] SLATE.24: colour-output configuration the preset references
- [artifact] NAT.08: the exact three writer profile identities (matroska-ffv1-pcm/wav-pcm/mp4-mpeg4-aac)
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: ArcSlate:src/ArcForges.ArcSlate.Domain/Render/ExportPreset.cs; ArcSlate:src/ArcForges.ArcSlate.Rendering/Encoding/**
Shared resources (follow the owner protocol): RES-arcslate-golden-media (append): Golden media and reference outputs are added per task with provenance; they are never regenerated to make a test pass; large media follows the repository storage policy.; RES-arcslate-migrations (append): Numbered migrations are allocated at merge by the integration owner (a rebase renumbers pending migrations); each migration is forward-only with its recovery and downgrade-refusal tests; no task edits a merged migration.; RES-workstation-build-slot (exclusive): Exclusive per workstation for the duration of each CPU-heavy local build or test, through the workstation lock rather than a Plan lease: run the command as `python tools/delivery.py build-slot run --worker <name> --task <task> -- <command>` with the Plan repository tool, which holds the lock directory `.arcforges/build-slot` in the user profile with an owner record and heartbeat and recovers a lock whose holder stopped. Coding and review continue while a build waits; CI capacity is not limited by this rule.
Unblocks: SLATE.28, SLATE.31

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Preset validation negative tests; encode conformance tests per preset against golden fixtures with declared tolerance; metadata-correctness check on output files.
Completion evidence for the ledger: Invalid-preset-refused-before-start results; per-preset conformance results.
```

```text
Execute ArcForges delivery task SLATE.28 — Render execution engine and atomic export (native Product Job).

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\arcslate.md (anchor task-slate-28).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\ArcSlate (integration owner: ArcSlate integration owner, the holder of roles/integration-arcslate).
Claim and handoff record: claims/slate-28 (python tools/delivery.py claim SLATE.28 --worker <name>); task branch task/slate-28 in ArcSlate; ledger record ledger/tasks/slate-28.md.
Kind/size: feature/XL. Baseline: not-started.
Outcome: Render runs as a native Product Job (progress, pause, resume, cancellation) owned and recovered by ArcSlate, never entering task.task or consuming AI capacity; output writes to a temporary target and commits atomically so a crash/cancel/missing marker never exposes a complete-looking file; a long render survives machine sleep and resumes where the platform permits.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-38.03 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\38-arcslate-render-and-colour.md, anchor rule-wp-38.03
- WP-38:security-impact-output-paths-validated-n Security impact: output paths validated, no arbitrary write location (§6) (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\38-arcslate-render-and-colour.md, package-level obligation
- WP-38:additional-completion-requirement-conten Additional completion requirement: content-origin vectors on render/subtitle output paths, including unknown input and failed publication (§8) (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\38-arcslate-render-and-colour.md, package-level obligation

Entry condition: adoption slice ADOPT.06.arcslate is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] SLATE.26: the render plan/snapshot this executes
- [artifact] SLATE.27: the validated export preset
- [artifact] SLATE.19: the native-backed graph evaluator to produce pixels
- [artifact] SLATE.20: sample-accurate mixing for the rendered audio track
- [artifact] NAT.08: published writer open/write/finish/abort with commit-only-after-complete semantics
- [artifact] EXE.01: the published native ProductJob engine (ProductJobId/ProductJobRecord/JobStep/JobAttempt/ExecutionState/Checkpoint/CompensationAction/ApprovalGate/ResourcePermit/ProgressReport/ExecutionOutcome/ExecutionTrace)
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: ArcSlate:src/ArcForges.ArcSlate.Rendering/Execution/**
Shared resources (follow the owner protocol): RES-arcslate-build-config (append): Solution/project lists, central package versions and CI job lists are appended by the task that adds a project, dependency or job; dependency additions follow the dependency-admission policy with a reviewed receipt; lock files are regenerated after rebase and never hand-merged; the integration owner resolves ordering conflicts at merge.; RES-arcslate-golden-media (append): Golden media and reference outputs are added per task with provenance; they are never regenerated to make a test pass; large media follows the repository storage policy.; RES-workstation-build-slot (exclusive): Exclusive per workstation for the duration of each CPU-heavy local build or test, through the workstation lock rather than a Plan lease: run the command as `python tools/delivery.py build-slot run --worker <name> --task <task> -- <command>` with the Plan repository tool, which holds the lock directory `.arcforges/build-slot` in the user profile with an owner record and heartbeat and recovers a lock whose holder stopped. Coding and review continue while a build waits; CI capacity is not limited by this rule.
Unblocks: SLATE.31, SLATE.33

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Cancellation and failure tests asserting no complete-looking partial file; long-render soak; sleep-and-resume test; disk-full test -- local, once, on the existing environment.
Completion evidence for the ledger: No-complete-looking-partial-file results; soak survival result; sleep/resume result.
Notes: WP-38's own dependency header lists only 'Upstream: 37', omitting WP-16 even though WP-38.03's body text explicitly requires WP-16's Product Job lifecycle.
```

```text
Execute ArcForges delivery task SLATE.29 — Subtitles and captions: authored tracks, SRT/WebVTT import/export.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\arcslate.md (anchor task-slate-29).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\ArcSlate (integration owner: ArcSlate integration owner, the holder of roles/integration-arcslate).
Claim and handoff record: claims/slate-29 (python tools/delivery.py claim SLATE.29 --worker <name>); task branch task/slate-29 in ArcSlate; ledger record ledger/tasks/slate-29.md.
Kind/size: feature/M. Baseline: not-started.
Outcome: SubtitleTrack/SubtitleCue exist as an independent track role (never a text-overlay effect); imported millisecond timestamps convert exactly to ticks; export rounds each endpoint once to nearest millisecond (ties-to-even) and reports maximum endpoint error and any collapsed-cue extension/refusal; exported files carry the content-origin carrier/sidecar.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-38.05 (authored subtitles and SRT/WebVTT import/export: exact canonical ticks, declared nearest-ms bounded loss on export (<=0.5ms), explicit collapsed-interval handling, retained sidecar/origin): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\38-arcslate-render-and-colour.md, anchor rule-wp-38.05
- WP-38:additional-completion-requirement-conten Additional completion requirement: content-origin vectors on render/subtitle output paths, including unknown input and failed publication (§8) (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\38-arcslate-render-and-colour.md, package-level obligation
- WP-38:unlabelled-final-review-closure-srt-webv Unlabelled final-review closure: SRT/WebVTT preview/import/export plus local extraction ProductJob/TranscriptRecord adoption (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\38-arcslate-render-and-colour.md, package-level obligation

Entry condition: adoption slice ADOPT.06.arcslate is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] SLATE.06: the track-role model subtitle tracks are a role of
- [artifact] SLATE.01: the tick<->millisecond conversion boundary
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: ArcSlate:src/ArcForges.ArcSlate.Subtitles/**
Shared resources (follow the owner protocol): RES-arcslate-migrations (append): Numbered migrations are allocated at merge by the integration owner (a rebase renumbers pending migrations); each migration is forward-only with its recovery and downgrade-refusal tests; no task edits a merged migration.; RES-contracts-schema-sources (append): Each closure task edits only its own domain proto or HTTP-schema files and adds its own sharded constraint and fixture files; shared inventories (package inventory, foundation inventory, constraint aggregate) are append-only per closure. A proto file with several contributing tasks (operator, policy/configuration) has one designated author task and the others request changes through it. The integration owner merges closure pull requests one at a time and the next author rebases and regenerates.
Unblocks: SLATE.30, SLATE.32

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Independent sub-ms/negative/out-of-range/overlap/collapse vectors and a round-trip fidelity report; no blanket byte/time identity claim for lossy standard formats.
Completion evidence for the ledger: Round-trip fidelity report per format; <=0.5ms max-endpoint-error result.
```

```text
Execute ArcForges delivery task SLATE.30 — Local transcription extraction ProductJob and TranscriptRecord adoption.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\arcslate.md (anchor task-slate-30).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\ArcSlate (integration owner: ArcSlate integration owner, the holder of roles/integration-arcslate).
Claim and handoff record: claims/slate-30 (python tools/delivery.py claim SLATE.30 --worker <name>); task branch task/slate-30 in ArcSlate; ledger record ledger/tasks/slate-30.md.
Kind/size: feature/L. Baseline: not-started.
Outcome: A local isolated ProductJob freezes the selected sequence revision/range, extracts mono PCM16 WAV in <=30s/1MiB chunks, and records exact sample counts/hashes/conform mapping without auto-uploading; adoption previews derived segments as authored subtitle cues, binds NativeContentRev, requires explicit partial-output acceptance where applicable, and commits one undoable edit carrying AI content-origin.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-38.05 (the final-review closure clause: local extraction ProductJob and TranscriptRecord review/adoption under expectedNative/undo/origin (slate.transcribe.v1)): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\38-arcslate-render-and-colour.md, anchor rule-wp-38.05
- WP-38:additional-completion-requirement-conten Additional completion requirement: content-origin vectors on render/subtitle output paths, including unknown input and failed publication (§8) (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\38-arcslate-render-and-colour.md, package-level obligation
- WP-38:unlabelled-final-review-closure-srt-webv Unlabelled final-review closure: SRT/WebVTT preview/import/export plus local extraction ProductJob/TranscriptRecord adoption (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\38-arcslate-render-and-colour.md, package-level obligation

Entry condition: adoption slice ADOPT.06.arcslate is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] SLATE.29: the SubtitleTrack/Cue model adoption writes into
- [artifact] SLATE.16: decode to extract PCM audio
- [artifact] EXE.01: the native ProductJob engine (local isolated job)
Completion prerequisites (may start earlier; cannot complete before these are complete):
- [integration] HAR.91: real Cloud Workers AI whisper-large-v3-turbo output reconciled end to end

Permitted write scope: ArcSlate:src/ArcForges.ArcSlate.Application/Transcription/**
Shared resources (follow the owner protocol): RES-contracts-schema-sources (append): Each closure task edits only its own domain proto or HTTP-schema files and adds its own sharded constraint and fixture files; shared inventories (package inventory, foundation inventory, constraint aggregate) are append-only per closure. A proto file with several contributing tasks (operator, policy/configuration) has one designated author task and the others request changes through it. The integration owner merges closure pull requests one at a time and the next author rebases and regenerates.
Permitted substitutes (never real integration evidence): SUB-slate-asr-fixture: chunking, extraction-artifact hashing, adoption preview/undo/content-origin logic only -- never real ASR accuracy, real budget/metering or real provider failure modes Real producer ['AIR.09']; removed by HAR.91
Unblocks: HAR.91, SLATE.32

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Local extraction/adoption tests against the SUB-slate-asr-fixture only; no live AI dispatch in this task's own CI (that belongs to WP-43/WP-52 under P2-017's no-real-inference-CI rule).
Completion evidence for the ledger: Extraction-artifact exact-sample-count/hash result; adoption-commits-one-undoable-edit result; partial-output-acceptance result.
```

```text
Execute ArcForges delivery task SLATE.31 — Golden output stability corpus.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\arcslate.md (anchor task-slate-31).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\ArcSlate (integration owner: ArcSlate integration owner, the holder of roles/integration-arcslate).
Claim and handoff record: claims/slate-31 (python tools/delivery.py claim SLATE.31 --worker <name>); task branch task/slate-31 in ArcSlate; ledger record ledger/tasks/slate-31.md.
Kind/size: feature/M. Baseline: not-started.
Outcome: A golden fixture corpus with declared tolerances covers every supported export preset; a codec or backend update that changes output beyond tolerance fails the build and requires a recorded decision.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-38.06 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\38-arcslate-render-and-colour.md, anchor rule-wp-38.06

Entry condition: adoption slice ADOPT.06.arcslate is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] SLATE.28: real render execution to produce the corpus outputs
- [artifact] SLATE.27: every supported preset to cover
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: ArcSlate:fixtures/media/golden/**
Shared resources (follow the owner protocol): RES-arcslate-golden-media (append): Golden media and reference outputs are added per task with provenance; they are never regenerated to make a test pass; large media follows the repository storage policy.; RES-workstation-build-slot (exclusive): Exclusive per workstation for the duration of each CPU-heavy local build or test, through the workstation lock rather than a Plan lease: run the command as `python tools/delivery.py build-slot run --worker <name> --task <task> -- <command>` with the Plan repository tool, which holds the lock directory `.arcforges/build-slot` in the user profile with an owner record and heartbeat and recovers a lock whose holder stopped. Coding and review continue while a build waits; CI capacity is not limited by this rule.
Unblocks: SLATE.32

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Golden comparison across the corpus; a deliberate-change negative test asserting the gate fires -- local, once.
Completion evidence for the ledger: Full-corpus comparison result; negative-gate-fires proof.
Notes: Golden media fixture acquisition/licensing is a cross-cutting logistical risk: SLATE.16 (decode), SLATE.20 (audio mixing), SLATE.27/28 (encode conformance) and SLATE.38/39 (OTIO round-trip) all need real, licence-clear test media before their own real-integration evidence can be recorded, not only this task.
```

```text
Execute ArcForges delivery task SLATE.32 — Closure: owned-artifact and real-integration receipt.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\arcslate.md (anchor task-slate-32).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\ArcSlate (integration owner: ArcSlate integration owner, the holder of roles/integration-arcslate).
Claim and handoff record: claims/slate-32 (python tools/delivery.py claim SLATE.32 --worker <name>); task branch task/slate-32 in ArcSlate; ledger record ledger/tasks/slate-32.md.
Kind/size: acceptance/S. Baseline: not-started.
Outcome: Independent render/range/colour/output checks and cancel/failure/atomic-publish recovery pass, with the receipt confirming no CF Harness or AI budget is required for native render execution.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-38.90 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\38-arcslate-render-and-colour.md, anchor rule-wp-38.90

Entry condition: adoption slice ADOPT.06.arcslate is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] SLATE.24: all WP-38 tasks complete
- [artifact] SLATE.31: all WP-38 tasks complete
- [artifact] HAR.91: package task delivered
- [artifact] SLATE.25: package task delivered
- [artifact] SLATE.29: package task delivered
- [artifact] SLATE.30: package task delivered
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: ArcSlate:docs/evidence/wp38-90-receipt.md
Unblocks: REL.03

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Consolidated re-run of SLATE.24-31's suites, local, once.
Completion evidence for the ledger: The consolidated receipt.
```

```text
Execute ArcForges delivery task SLATE.33 — Capability surface: query, edit, render and export capabilities.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\arcslate.md (anchor task-slate-33).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\ArcSlate (integration owner: ArcSlate integration owner, the holder of roles/integration-arcslate).
Claim and handoff record: claims/slate-33 (python tools/delivery.py claim SLATE.33 --worker <name>); task branch task/slate-33 in ArcSlate; ledger record ledger/tasks/slate-33.md.
Kind/size: feature/L. Baseline: not-started.
Outcome: Query capabilities (projects/sequences/tracks/clips/markers/media/transcripts/render-state), edit capabilities (semantic timeline operations, marker/subtitle operations, effect application) and render/export capabilities (ProductJobHandle-returning) are all registered, each declaring risk/side-effect-class/reversibility/approval-posture with owner-side validation; the contract is provably frozen only after timeline/command/undo semantics stabilised.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-39.00 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\39-arcslate-integration-and-portability.md, anchor rule-wp-39.00

Entry condition: adoption slice ADOPT.06.arcslate is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] SLATE.07: the stable semantic edit-command set to expose
- [artifact] SLATE.08: the remaining edit-command set
- [artifact] SLATE.28: render execution to expose as a capability returning a ProductJobHandle
Completion prerequisites (may start earlier; cannot complete before these are complete):
- [integration] DEV.03: published owner reauthorization (Device.Runtime invoking typed in-process product handlers after grant/resource/revision/egress checks)

Permitted write scope: ArcSlate:src/ArcForges.ArcSlate.AssistantIntegration/**
Shared resources (follow the owner protocol): RES-arcslate-build-config (append): Solution/project lists, central package versions and CI job lists are appended by the task that adds a project, dependency or job; dependency additions follow the dependency-admission policy with a reviewed receipt; lock files are regenerated after rebase and never hand-merged; the integration owner resolves ordering conflicts at merge.; RES-arcslate-registries (append): Each feature registers its own commands and capabilities through its module; registry files are append-only.
Unblocks: SLATE.40

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Descriptor validation, owner-side refusal test, idempotency-per-write-capability test, stability assertion (contract frozen only after semantics stabilised).
Completion evidence for the ledger: Risk/approval-posture declaration coverage; owner-side-validation-always proof.
Notes: This is the REAL landing point for WP-26 (Application Presence and One-Application Tool Bridge), not WP-36. WP-36's header lists 07/10/13/26 as upstream, but nothing in WP-36.00-36.07's actual scope (project/timeline/media domain model) touches remote application presence or the tool bridge; WP-26's substeps (ApplicationService, ToolRequest queue, owner reauthorization, remote approval) are about exposing an already-running desktop instance to Cloud-driven remote invocation, which is exactly WP-39.00's capability-surface scope.
```

```text
Execute ArcForges delivery task SLATE.34 — Bounded context provision.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\arcslate.md (anchor task-slate-34).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\ArcSlate (integration owner: ArcSlate integration owner, the holder of roles/integration-arcslate).
Claim and handoff record: claims/slate-34 (python tools/delivery.py claim SLATE.34 --worker <name>); task branch task/slate-34 in ArcSlate; ledger record ledger/tasks/slate-34.md.
Kind/size: feature/M. Baseline: not-started.
Outcome: Context providers expose sequence structure, markers, selected ranges, timecodes and metadata; raw media structurally cannot enter a context payload; oversized context is refused explicitly and visibly.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-39.01 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\39-arcslate-integration-and-portability.md, anchor rule-wp-39.01

Entry condition: adoption slice ADOPT.06.arcslate is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] SLATE.06: the timeline structure to project into context
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: ArcSlate:src/ArcForges.ArcSlate.AssistantIntegration/Context/**
Shared resources (follow the owner protocol): RES-arcslate-registries (append): Each feature registers its own commands and capabilities through its module; registry files are append-only.
Unblocks: SLATE.40

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Structural test asserting media data cannot enter a context payload (type-level, not merely a runtime check); bounding and visibility tests.
Completion evidence for the ledger: Media-cannot-enter-context structural proof; oversized-context-refused result.
```

```text
Execute ArcForges delivery task SLATE.35 — Collect, consolidate and the portable project package.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\arcslate.md (anchor task-slate-35).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\ArcSlate (integration owner: ArcSlate integration owner, the holder of roles/integration-arcslate).
Claim and handoff record: claims/slate-35 (python tools/delivery.py claim SLATE.35 --worker <name>); task branch task/slate-35 in ArcSlate; ledger record ledger/tasks/slate-35.md.
Kind/size: feature/L. Baseline: not-started.
Outcome: Collect/Consolidate gathers external media into a managed portable form on request, reports exactly what was gathered/skipped and why, never destroys originals; the portable package (project data plus managed media) re-imports with equivalence.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-39.02 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\39-arcslate-integration-and-portability.md, anchor rule-wp-39.02
- WP-39:security-impact-media-path-handling-no-p Security impact: media path handling, no path leakage through references (§6) (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\39-arcslate-integration-and-portability.md, package-level obligation

Entry condition: adoption slice ADOPT.06.arcslate is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] SLATE.04: the real relink/asset-resolution adapter
- [artifact] SLATE.05: the media library to enumerate
- [artifact] PLT.06: published chunked verifiable large-append store
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: ArcSlate:src/ArcForges.ArcSlate.ImportExport/CollectConsolidate/**
Unblocks: SLATE.42

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Collect with mixed available/offline media, originals-untouched assertion, package round-trip equivalence, large-project performance measurement -- local, once.
Completion evidence for the ledger: Originals-untouched result; round-trip equivalence result; honest skipped-item report.
```

```text
Execute ArcForges delivery task SLATE.36 — Cross-device resolution and relink.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\arcslate.md (anchor task-slate-36).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\ArcSlate (integration owner: ArcSlate integration owner, the holder of roles/integration-arcslate).
Claim and handoff record: claims/slate-36 (python tools/delivery.py claim SLATE.36 --worker <name>); task branch task/slate-36 in ArcSlate; ledger record ledger/tasks/slate-36.md.
Kind/size: feature/M. Baseline: not-started.
Outcome: MediaResolutionStrategy resolves per-device asset locations; the relink workflow handles moved/renamed/partially-available media; a project opens with all media offline and relinks without altering any edit decision.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-39.03 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\39-arcslate-integration-and-portability.md, anchor rule-wp-39.03
- WP-39:security-impact-media-path-handling-no-p Security impact: media path handling, no path leakage through references (§6) (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\39-arcslate-integration-and-portability.md, package-level obligation

Entry condition: adoption slice ADOPT.06.arcslate is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] SLATE.03: the content-based relink algorithm
- [artifact] SLATE.04: the real read adapter to re-verify content hash on relink
- [artifact] SLATE.05: the media library
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: ArcSlate:src/ArcForges.ArcSlate.Application/Relink/**
Shared resources (follow the owner protocol): RES-arcslate-migrations (append): Numbered migrations are allocated at merge by the integration owner (a rebase renumbers pending migrations); each migration is forward-only with its recovery and downgrade-refusal tests; no task edits a merged migration.
Unblocks: SLATE.40

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Open-with-all-offline test, relink-after-path-change test, partial-relink test, edit-decisions-survive-every-relink-path test.
Completion evidence for the ledger: Offline-open-and-full-relink result; edit-decision-preservation proof.
```

```text
Execute ArcForges delivery task SLATE.37 — Cloud sync scope declaration.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\arcslate.md (anchor task-slate-37).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\ArcSlate (integration owner: ArcSlate integration owner, the holder of roles/integration-arcslate).
Claim and handoff record: claims/slate-37 (python tools/delivery.py claim SLATE.37 --worker <name>); task branch task/slate-37 in ArcSlate; ledger record ledger/tasks/slate-37.md.
Kind/size: feature/M. Baseline: not-started.
Outcome: Project data/sequences/markers/presets/metadata sync by default; heavyweight media follows an explicit escalation policy, never swept in by enabling sync; derived data (proxies/caches/analysis) never syncs as authority; big media never traverses the application runtime.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-39.04 (all work except the parts mapped to SLATE.42): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\39-arcslate-integration-and-portability.md, anchor rule-wp-39.04

Entry condition: adoption slice ADOPT.06.arcslate is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] SLATE.10: the project store to declare a sync scope over
- [contract] CON.09: published SyncService/ResourceService records for project-metadata sync scopes
Completion prerequisites (may start earlier; cannot complete before these are complete):
- [integration] SLATE.42: real multi-device project convergence against the deployed Cloud sync engine

Permitted write scope: ArcSlate:src/ArcForges.ArcSlate.CloudClient/**
Shared resources (follow the owner protocol): RES-arcslate-migrations (append): Numbered migrations are allocated at merge by the integration owner (a rebase renumbers pending migrations); each migration is forward-only with its recovery and downgrade-refusal tests; no task edits a merged migration.
Unblocks: SLATE.42

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Enable-sync test asserting no heavyweight media transferred implicitly; derived-data-exclusion assertion; application-service-no-body assertion (the app runtime itself never carries big media) -- local, once, against WP-25's real environment where available.
Completion evidence for the ledger: No-implicit-heavy-media-transfer result; derived-data-never-syncs-as-authority result.
```

```text
Execute ArcForges delivery task SLATE.38 — OTIO interchange: import.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\arcslate.md (anchor task-slate-38).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\ArcSlate (integration owner: ArcSlate integration owner, the holder of roles/integration-arcslate).
Claim and handoff record: claims/slate-38 (python tools/delivery.py claim SLATE.38 --worker <name>); task branch task/slate-38 in ArcSlate; ledger record ledger/tasks/slate-38.md.
Kind/size: feature/L. Baseline: not-started.
Outcome: Importing a real.otio file (through the pinned official library, behind the narrow C ABI, no adapters/plug-ins/executable content) decodes each finite double via its exact binary rational, normalises only within one ULP of a declared standard rate, stages the result with a fidelity report the user reviews or cancels, and never silently drops timeline structure.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-39.05 (import direction: OB-01..OB-05 numeric boundary, staged-before-commit import creating ArcSlate-owned canonical objects with provenance, item-level retained/approximated/omitted dispositions, media relink for Offline Media): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\39-arcslate-integration-and-portability.md, anchor rule-wp-39.05
- WP-39:completion-gate-item-6-every-claimed-int Completion gate item 6: every claimed interchange version has a fixture and states fidelity before writing -- satisfies PG-07 for ArcSlate (§8) (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\39-arcslate-integration-and-portability.md, package-level obligation

Entry condition: adoption slice ADOPT.06.arcslate is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] SLATE.06: the timeline structural model import populates
- [artifact] SLATE.01: the canonical tick domain the OB-01..05 numeric boundary converts into
- [artifact] NAT.06: the common ABI layer
- [artifact] NAT.12: published arc_otio_read export (official OTIO0.18.1 read/upgrade under the schema allowlist)
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: ArcSlate:src/ArcForges.ArcSlate.ImportExport/Otio/Import/**
Shared resources (follow the owner protocol): RES-arcslate-build-config (append): Solution/project lists, central package versions and CI job lists are appended by the task that adds a project, dependency or job; dependency additions follow the dependency-admission policy with a reviewed receipt; lock files are regenerated after rebase and never hand-merged; the integration owner resolves ordering conflicts at merge.; RES-arcslate-golden-media (append): Golden media and reference outputs are added per task with provenance; they are never regenerated to make a test pass; large media follows the repository storage policy.; RES-contracts-schema-sources (append): Each closure task edits only its own domain proto or HTTP-schema files and adds its own sharded constraint and fixture files; shared inventories (package inventory, foundation inventory, constraint aggregate) are append-only per closure. A proto file with several contributing tasks (operator, policy/configuration) has one designated author task and the others request changes through it. The integration owner merges closure pull requests one at a time and the next author rebases and regenerates.; RES-workstation-build-slot (exclusive): Exclusive per workstation for the duration of each CPU-heavy local build or test, through the workstation lock rather than a Plan lease: run the command as `python tools/delivery.py build-slot run --worker <name> --task <task> -- <command>` with the Plan repository tool, which holds the lock directory `.arcforges/build-slot` in the user profile with an owner record and heartbeat and recovers a lock whose holder stopped. Coding and review continue while a build waits; CI capacity is not limited by this rule.
Unblocks: SLATE.39

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Finite/nonfinite/large/fractional-value vectors, standard-30000/1001-vs-decimal-29.97 vector, metadata-stripped-external-file vector -- against real fixtures and the pinned official library, local, once.
Completion evidence for the ledger: Per-vector numeric-boundary results; no-silent-frame-shift proof; malicious-path-denied and malformed-input-rejected-before-commit results.
Notes: OB-01..OB-05's exact-binary-rational-decode-then-normalise-only-within-one-ULP rule is intricate and gates PG-15/PG-20/PG-03 simultaneously. A narrow numeric-adapter proof (the finite/NaN/overflow/ULP vectors alone, before building the full staged-import/fidelity-report UI) is worth doing first, since a wrong approach here invalidates broad downstream evidence, matching the same class of risk the design doc's own worked example (23-simulator-and-interchange.md §3.10) calls out.
```

```text
Execute ArcForges delivery task SLATE.39 — OTIO interchange: export.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\arcslate.md (anchor task-slate-39).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\ArcSlate (integration owner: ArcSlate integration owner, the holder of roles/integration-arcslate).
Claim and handoff record: claims/slate-39 (python tools/delivery.py claim SLATE.39 --worker <name>); task branch task/slate-39 in ArcSlate; ledger record ledger/tasks/slate-39.md.
Kind/size: feature/M. Baseline: not-started.
Outcome: Export binds a committed sequence revision (reusing the same immutable-snapshot pattern as render), writes to a temporary destination, and publishes atomically after validation; failure/cancellation leaves the project and any existing destination untouched; reports exclude unselected absolute paths and secrets.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-39.05 (export direction: binds a committed sequence revision, writes a temporary destination and publishes atomically, item-level dispositions for everything outside the supported subset): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\39-arcslate-integration-and-portability.md, anchor rule-wp-39.05
- WP-39:completion-gate-item-6-every-claimed-int Completion gate item 6: every claimed interchange version has a fixture and states fidelity before writing -- satisfies PG-07 for ArcSlate (§8) (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\39-arcslate-integration-and-portability.md, package-level obligation

Entry condition: adoption slice ADOPT.06.arcslate is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] SLATE.38: the shared OB-01..05 numeric adapter and FidelityEntry plumbing
- [artifact] SLATE.26: the committed-revision-snapshot pattern
- [artifact] NAT.12: published arc_otio_write export
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: ArcSlate:src/ArcForges.ArcSlate.ImportExport/Otio/Export/**
Shared resources (follow the owner protocol): RES-arcslate-golden-media (append): Golden media and reference outputs are added per task with provenance; they are never regenerated to make a test pass; large media follows the repository storage policy.; RES-contracts-schema-sources (append): Each closure task edits only its own domain proto or HTTP-schema files and adds its own sharded constraint and fixture files; shared inventories (package inventory, foundation inventory, constraint aggregate) are append-only per closure. A proto file with several contributing tasks (operator, policy/configuration) has one designated author task and the others request changes through it. The integration owner merges closure pull requests one at a time and the next author rebases and regenerates.; RES-workstation-build-slot (exclusive): Exclusive per workstation for the duration of each CPU-heavy local build or test, through the workstation lock rather than a Plan lease: run the command as `python tools/delivery.py build-slot run --worker <name> --task <task> -- <command>` with the Plan repository tool, which holds the lock directory `.arcforges/build-slot` in the user profile with an owner record and heartbeat and recovers a lock whose holder stopped. Coding and review continue while a build waits; CI capacity is not limited by this rule.
Unblocks: SLATE.40

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Mixed/fractional-rate round trip, gaps/stack ordering, repeated-media-retains-placement, missing-references-become-relinkable-Offline-Media, supported-dissolves/markers, unsupported-feature-reports, export-cancellation-leaves-project-untouched -- against real fixtures and the pinned official library, local, once.
Completion evidence for the ledger: Both-directions-against-real-fixtures result (paired with SLATE.38); semantic-round-trip (meaning/references, not bytes/internal-IDs) result; cancellation-leaves-nothing-touched result. Together with SLATE.38, satisfies PG-15, contributes to PG-20 and PG-03 (OTIO bridge licence/provenance), and PG-07 for ArcSlate.
```

```text
Execute ArcForges delivery task SLATE.40 — Closure: owned-artifact and real-integration receipt.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\arcslate.md (anchor task-slate-40).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\ArcSlate (integration owner: ArcSlate integration owner, the holder of roles/integration-arcslate).
Claim and handoff record: claims/slate-40 (python tools/delivery.py claim SLATE.40 --worker <name>); task branch task/slate-40 in ArcSlate; ledger record ledger/tasks/slate-40.md.
Kind/size: acceptance/S. Baseline: not-started.
Outcome: OTIO round-trip/projection and relocation fixtures, the package boundary, explicit R2 upload and missing-external-reference behaviour are all recorded with real artifacts and provider identity; the receipt confirms no DTO version-skew can truncate a native project before sync.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-39.90 (full): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\39-arcslate-integration-and-portability.md, anchor rule-wp-39.90
- WP-39:unlabelled-final-review-closure-cloud-da Unlabelled final-review closure: Cloud data-model round-trip of complete Slate metadata/archive, managed asset uploads, exact grids, graph scopes, fonts/colour, ASR references, anti-truncation (the unlabelled final-review closure paragraph: Cloud data-model round-trip of complete Slate metadata/archive with originals absent, explicit managed asset uploads, exact grids, graph scopes, titles/subtitles/fonts/colour and ASR source/artifact references; an older DTO cannot truncate the native project before sync; package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\39-arcslate-integration-and-portability.md, package-level obligation

Entry condition: adoption slice ADOPT.06.arcslate is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] SLATE.33: all WP-39 tasks complete
- [artifact] SLATE.39: all WP-39 tasks complete
- [artifact] SLATE.34: package task delivered
- [artifact] SLATE.36: package task delivered
Completion prerequisites (may start earlier; cannot complete before these are complete):
- [integration] SLATE.42: real Cloud replica round-trip of complete Slate project metadata/archive against WP-25's deployed store

Permitted write scope: ArcSlate:docs/evidence/wp39-90-receipt.md
Unblocks: REL.03

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Consolidated re-run of SLATE.33-39's suites plus the real Cloud round-trip, local/available-environment, once.
Completion evidence for the ledger: The consolidated receipt; DTO-version-skew-cannot-truncate-project proof.
```

```text
Execute ArcForges delivery task SLATE.42 — Real multi-device ArcSlate project convergence against the deployed Cloud sync engine.

Task record: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\lanes\arcslate.md (anchor task-slate-42).
Delivery rules: C:\MyFile\Projects\ArcForges-Design-B\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan-B\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\ArcSlate (integration owner: ArcSlate integration owner, the holder of roles/integration-arcslate). Also touches: Cloud.
Claim and handoff record: claims/slate-42 (python tools/delivery.py claim SLATE.42 --worker <name>); task branch task/slate-42 in ArcSlate; ledger record ledger/tasks/slate-42.md.
Kind/size: integration/M. Baseline: not-started.
Outcome: Two devices editing/opening the same ArcSlate project through the real Cloud sync engine converge correctly, with heavyweight media never implicitly transferred and derived data never syncing as authority.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-39.04 (testing requirement: 'multi-device project convergence'): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\39-arcslate-integration-and-portability.md, anchor rule-wp-39.04
- WP-39:unlabelled-final-review-closure-paragrap unlabelled final-review closure paragraph (01-cloud-data-model.md structural-move-and-complete-media-replica-constraints) (unlabelled final-review closure paragraph (01-cloud-data-model.md structural-move-and-complete-media-replica-constraints)): C:\MyFile\Projects\ArcForges-Design-B\docs\planning\work-packages\39-arcslate-integration-and-portability.md, package-level obligation

Entry condition: adoption slice ADOPT.06.arcslate is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] SLATE.37: real, delivered outcome of SLATE.37 (Cloud sync scope declaration)
- [artifact] CLOUD.39: real, delivered outcome of CLOUD.39 (Guarded publication and convergent bootstrap)
- [artifact] CLOUD.44: real, delivered outcome of CLOUD.44 (Multi-device convergence harness)
- [artifact] SLATE.12: real, delivered outcome of SLATE.12 (Slate.project.v1/graph.v1 wire projection: bins, generators, nesting, adjustment, title/subtitle, cycle rejection)
- [artifact] SLATE.35: real, delivered outcome of SLATE.35 (Collect, consolidate and the portable project package)
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: 
Unblocks: SLATE.37, SLATE.40

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Local real-integration run of the affected scenario in an existing environment, recorded once; offline and static checks in CI; no hosted runtime, device, browser, live-service or inference CI (P2-017).
Completion evidence for the ledger: Two devices editing/opening the same ArcSlate project through the real Cloud sync engine converge correctly, with heavyweight media never implicitly transferred and derived data never syncing as authority.
Notes: Merged duplicate integration or closure task formerly proposed as SLATE.43.
```
