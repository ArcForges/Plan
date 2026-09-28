---
task: PLT.06
status: complete
recorded: 2026-09-28
claimant: w-20260927-dother
epoch: 1
---

# Verifiable large append store

- Implementation: DesktopPlatform PR70. Final reviewed head `ed8b3ca96653f9290d0b7b9ddc513235f5c1bbdc`; independent approval [5861187941](https://github.com/ArcForges/DesktopPlatform/pull/70#issuecomment-5861187941). Source merge `d1fb6d0af306ec3553729dc7e46e16de1d414b28` after all12 retained checks passed in [CI36361608440](https://github.com/ArcForges/DesktopPlatform/actions/runs/36361608440). Original publication succeeded as recorded below.
- Outcome: nonpackable ArcForges.Persistence.Resources owns a bounded append-only capture format outside SQLite. A 64-byte header contains magic/version/kind/sequence/payload length plus SHA-256 over the first header half and payload. Frames are bounded to 4 MiB and scans to one million frames.
- Durable behavior: chunk, segment map and typed gap acknowledgements follow Flush(true). Segment GUIDs map ordered slices of committed chunks; range reads verify touched frames. Seal rejects later appends, and a failed write faults the writer. A writer lock serializes operations.
- Recovery: read-only snapshots retain the verified prefix and validate semantic maps. Missing seals or damage produce typed unknown-certainty loss. A durable sidecar binds the full raw capture digest and observed/verified lengths; unique pending files are flushed before atomic final publication. Existing mismatched evidence is refused. Original capture bytes are never rewritten or resealed.
- Verification: default offline suite has 14 cases, 12 passed and 2 explicit opt-in child diagnostics skipped. Both actual child-kill diagnostics previously passed. Exhaustive independent offsets cover all 231 truncated captures, verified-prefix range reads, persisted loss and original-evidence immutability. Checksum, invalid map/gap, sealing, range and receipt cases passed.
- Support: owned library/test projects and existing offline workflow; runtime/licence/project reconciliation; ten ordinary public API mappings to real test methods; unchanged third-party dependency versions; successor admission/provenance inventories preserve previous records. Package acceptance remains PLT.08.
- Shared policy: GOV.04 array-return scanner repair was independently reviewed and merged through PR72. Actual Resources project graph completes without semantic findings; local missing hosted naming/secret/native receipts remain CI gates. All final owning CI gates passed as recorded above.
- Limits: no SQLite schema/migration, installed-consumer acceptance, device or production deployment claimed. Worktrees and source evidence are retained.

- Final baseline: merged authoritative PLT17, PLT07 and FND07 main761d7c9801b5ced005fd2a5266a1f38fca827044. Own admission successor preserves the final FND07 receipt and inherited41 NuGet/10 Python closure,218 inputs. Locked restore/full solution build passed with zero warnings/errors; immutable-snapshot reconciliation passed. Atomic CreateNew writer exclusion is asserted on all platforms; arbitrary deny-write sharing is an additional Windows check and Unix filesystem callers retain access-control responsibility.

- Original normal publication [36362107425](https://github.com/ArcForges/DesktopPlatform/actions/runs/36362107425) succeeded at source `d1fb6d0af306ec3553729dc7e46e16de1d414b28`. [Publisher108742459309](https://github.com/ArcForges/DesktopPlatform/actions/runs/36362107425/job/108742459309) verified and pushed all eight existing package coordinates at `1.0.0-ci.35.1`. Resources remains nonpackable; no Resources package publication is claimed. Original candidate `nuget-candidate-36362107425-1`, artifact10945469047, provider digest `sha256:a52ea608de836f330d2972c3164e20e958d9f26e578bbb102a6ef39d2df2b48b`. Integrator confirmed a clean primary fast-forward. Only original job/provider metadata was observed; no public-byte download or installed-consumer rerun occurred.
- Final ledger review/merge identities remain in the claim and Plan PR history. No implementation or publication prerequisite remains.
