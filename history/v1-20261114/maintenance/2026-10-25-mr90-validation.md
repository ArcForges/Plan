# MR-90: stable process-table references

Implementation: [ArcForges#47](https://github.com/ArcForges/ArcForges/pull/47), pushed head `14a60d607b57d1030e90cdbc6ca74f9fd2e48574`, base `f10248e4163999b867c0e33b6da5c66935045ce6`. Merged as `266bfa60229fc191e85966ee406c84ce3a4ead55` after both exact-head required statuses passed. This existing maintenance item became a prerequisite when MR-101's affected Windows ci encountered it.

## Defect and repair

The test read NtQuerySystemInformation first, then Toolhelp, and tolerated up to five later entries absent from the earlier table. The fixed allowance did not establish which processes existed across the read. At MR-101 head c78bdd9 it failed with eight absent entries. Their exact lifetime timeline was not retained; that log alone proves neither a sampler omission nor a particular interleaving.

The repaired test captures queryable Toolhelp identities (PID plus exact creation time) before the process table. Every captured identity still running afterwards must be present, with zero omissions permitted. Newly born, exited or PID-reused processes do not become false references. The self-process reference must exist; all parent/image/start/CPU/memory/I/O assertions and the explicit System/PID 4 check remain.

Only ResourceSamplerTests.cs changes (12 insertions, 4 deletions). No product, per-field bound, suite isolation or Design change. Protected processes whose creation cannot be queried cannot supply a lifetime reference; System is still checked explicitly. This is a limit of the independent reference API, rather than a claim to observe protected-process lifetimes.

## Distinct native Windows checks

- Controlled births: one owned reference starts before the table; eight actual TestLoad processes and their console hosts start strictly afterwards and stay alive. The old assertion fails with sixteen missing later entries. The repaired comparison passes.
- Negative control: temporarily remove the actual stable reference from the sampled list while leaving it alive. The repaired Assert.Empty fails with that reference, so a real stable omission is not hidden by the birth handling.
- All diagnostic injection was removed before the final build. Owned diagnostic processes are terminated and drained through their process handles, and their marker files are removed in finally blocks.
- One initial after-control ran the previous test DLL: Copy-Item retained a source time older than the built DLL. The unchanged old assertion in the output, source variant and file timestamps established the cause. The corrected orchestration touches changed sources before incremental builds; proper after-control and negative-control results above then followed. The stale-DLL failure is retained and is not after-fix evidence.
- Locked restore, final affected Release build (0 warnings/errors) and changed-file format passed.
- Final affected Platform.Windows ci: 116 total, 115 passed, 1 documented adoption skip, 0 failed. No target test was skipped.

Logs: `C:\MyFile\Projects\dev\logs\resume-20261025-mr90` (`before-control-test.log`, `v2-after-control-test.log`, `v2-missing-control-test.log`, `v2-final-build.log`, `v2-format.log`, `v2-affected-ci.log`, `summary-v2.log`). The full one-file diff was self-reviewed under the owner's instruction to use no other model or agent; no blocking finding.

## Formal verification

Windows formal verification passed all 13 full-profile steps in 954 s at the pushed head (tree `f7f84f5e93b9f14c702f6460f643305a0f32c737`, base `f10248e4163999b867c0e33b6da5c66935045ce6`). Its summary was checked. Linux passed all 16 full-profile steps in 1132 s at the same head/tree/base; it started only after the previous MR-101 c78bdd9 leg finished successfully and drained. No competing host build/test ran. Both summaries and the live GitHub head/base, required success statuses and owner's skipped hosted jobs were checked immediately before merge.

Windows summary: `C:\MyFile\Projects\ArcForges\ArcForges\.git\arcforges-verify\logs\20261025-115921-14a60d607b57-win\summary.json`.
Linux summary: `/home/sammiller/arcforges/ArcForges/.git/arcforges-verify/logs/20261025-200219-14a60d607b57-linux/summary.json`.

After this Plan record merges, MR-101 continues in its existing PR #45, takes main and receives fresh required checks at its resulting pushed head. MR-16 remains blocked; no real credential store, orphan credential file, systemd manager termination or later feature implementation is involved.
