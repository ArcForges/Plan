---
task: PLT.02
status: complete
recorded: 2026-09-28
claimant: af-20260928-p01
epoch: 1
---

# Transactional journal stage

## Evidence

- Implementation: [DesktopPlatform PR71](https://github.com/ArcForges/DesktopPlatform/pull/71), bundled with PLT.01 and PLT.04. Final reviewed head `98d9c5ca96f400d45d1e9bc9a146781e64d00837`, independent mobile approval [5860838788](https://github.com/ArcForges/DesktopPlatform/pull/71#issuecomment-5860838788), following the complete source review and bounded corrections. Implementation merge `48a3ef4fcb5e356d4a50d0317f93a1cb1f314b6e`. Publication: normal main [run36359293616](https://github.com/ArcForges/DesktopPlatform/actions/runs/36359293616) succeeded at source `48a3ef4fcb5e356d4a50d0317f93a1cb1f314b6e`. `ArcForges.Persistence.Sqlite/1.0.0-ci.33.1` is among the eight successful pushes in publisher job `108734304036`. Original provider candidate `nuget-candidate-36359293616-1`, artifact `10944818667`, has archive digest `sha256:ca330cca4b1a395534d4609266e7aacf8af47501059adf4664431e39b7ddf225`. This is provider metadata; no artifact bytes were downloaded for revalidation. Primary clean fast-forward was confirmed; no post-merge runtime cycle ran.
- WP-07.01 journal stage: immutable checksummed replay records contain typed previous/next versions, command/actor/correlation/causation/time and replay payload or durable reference. Journal order is distinct from nullable per-aggregate local edit identity. Append and durable high watermark participate in the owner's transaction.
- Replay refuses gaps, missing committed tail, malformed records, changed size accounting and checksum corruption. Count/size pressure refuses an append rather than deleting unverified history; time pressure requests snapshot work. Truncation requires a verified-boundary interface and respects active SQLite read snapshots.
- Actual local file tests cover commit/reopen versus injected failure after append, replay, corruption, local identity independence, capacity and truncation under read. The final affected Windows x64 SQLite suite passed 47/47 cases, zero failed or skipped, in Release using existing SDK10.0.401 through the workstation build slot after final integration onto cdd16cf5ed8b505779facf8bb55f18d95ba7cdcd. Local log: artifacts/persistence-final-test.log. All 12 retained exact-head checks passed in [run36358863088](https://github.com/ArcForges/DesktopPlatform/actions/runs/36358863088), including exact SDK10.0.400 Linux compilation/packaging/offline tests and Windows native staging.
- Substitute: NamedSnapshotFixture implements only the explicitly named PLT.03 seam. It is not a real durable snapshot producer and does not prove repeated snapshot/truncate/replay operation at bounded size.
- Untested: OS crash/power loss, network/removable filesystem and device/product consumers. No prohibited hosted runtime or installed-consumer execution was added.

## Completion follow-up — 2026-09-28

- PLT.03 is complete in [its ledger](plt-03.md): DesktopPlatform PR [#81](https://github.com/ArcForges/DesktopPlatform/pull/81) merged at `e60348bb39c6bc383980b524271a7fe10d953abb`, with exact-head independent review and hosted run [36392074287](https://github.com/ArcForges/DesktopPlatform/actions/runs/36392074287) terminal success (12/12). Normal publication run [36393746622](https://github.com/ArcForges/DesktopPlatform/actions/runs/36393746622) succeeded and all eight published package indexes were verified.
- Real snapshot/truncation acceptance was added in DesktopPlatform PR [#85](https://github.com/ArcForges/DesktopPlatform/pull/85): `RepeatedRealSnapshotsBoundJournalAndSnapshotGrowthThenRestoreAndReplayTheTail` exercises repeated durable snapshot, bounded journal/snapshot growth, restore and journal-tail replay; `RealSnapshotTruncationPreservesAnActiveReadersJournalView` exercises truncation while an active SQLite reader retains its journal view.
- Pinned .NET SDK 10.0.400 `PersistenceTests` focused suite passed 81/81. The source PR exact head `4f1df9cf61dbecd0fa82a84708f3fceadb7f06bd` received independent exact-head CLEAN review [5867860268](https://github.com/ArcForges/DesktopPlatform/pull/85#issuecomment-5867860268); hosted run [36407016787](https://github.com/ArcForges/DesktopPlatform/actions/runs/36407016787) completed terminal SUCCESS (13/13). PR #85 merged at `eb272b0893d42417e9255ab5ba17adc9337ffd69`.
- Normal post-merge publication run [36408861604](https://github.com/ArcForges/DesktopPlatform/actions/runs/36408861604) succeeded on that merge. Candidate `nuget-candidate-36408861604-1`, artifact `10963427563`, size `5,543,468` bytes, SHA-256 `14795c562cd09b8c155a1bd1f56932081730aea43b5fb81583fcaf4aae82c191`; publisher OIDC validation and all eight package pushes succeeded for `1.0.0-ci.43.1`. Independent index verification confirmed all eight public flat-container indexes list that version; no package bytes were downloaded.
- The earlier `NamedSnapshotFixture` remains only historical delivery-stage evidence; completion is based on the real producer and acceptance above. The validation scope remains offline/process-level as specified; this does not claim OS power-loss, removable-filesystem, hosted-runtime, or installed-consumer evidence.

Ledger review and merge identity are retained by this ledger PR and the task claim history.
