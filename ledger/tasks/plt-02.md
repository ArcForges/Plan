---
task: PLT.02
status: delivered
recorded: 2026-09-28
claimant: w-20260927-ai-lane
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

## Remaining acceptance

PLT.03 remains the explicit completion prerequisite established by Design PR91 merge `e384301467dd9dd695b54d8ffe236f4bf1a7af38` and Plan PR62 merge `34f50a51ac349c9bb4e005103b9ab34755865aba`. Full PLT.02 completion requires the real durable verified snapshot producer and its repeated bounded snapshot/truncate/replay acceptance. No PLT.03 work was started in this session.

Ledger review and merge identity are retained by this ledger PR and the task claim history.
