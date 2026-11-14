# MR-15: historical sealed-input loss remains unresolved

Date: 2026-10-26. Disposition: deferred validation / unresolved observation, AR-22. No runtime repair or real-store
validation pass is claimed. The owner resumed the authorized maintenance list after MR-14 and requested remaining
counts after every completed item; this record supersedes the temporary stop instruction in the earlier handoff.

## Historical evidence and changed test venue

[ArcForges#12](https://github.com/ArcForges/ArcForges/pull/12), historical head f5c622d94b145d3d62aad1884f8db4ae983f8467,
records one Windows ci failure while Windows and WSL ci ran concurrently, iteration 4 of 10:
CrashConsistencyTests.AStoreKilledDuringWritesReopensConsistent(420) found all 20 sampled sealed values UNAVAILABLE.
It does not record which key-load or authentication failure occurred. Commit c358e2d added UnavailableReason to the
assertion afterwards. The PR review comment does not add a cause or original raw diagnostic.

At that historical head, TestSecretStores.Select on Windows selected the real Credential Manager; the benchmark also
used that selection. Commit 6978b0c5cf4723ca562907dda7d300fb1c53caf8 (2026-10-18) moved both the writer and the
reopening crash test to NodeSecretStores.ForTestDataRoot, a private file-backed isolated key store. Production still uses
its selected backend. This change isolates routine tests; it does not establish or repair the historical real-store cause.
The old concurrent Windows/WSL run was not resumed. Current verification uses only native MCP hosts, never WSL.

## Read-only retained-log audit

Windows MCP audit at 2026-10-26T02:25:06.595092+00:00:
- 88 formal run directories, 86 readable summaries: 70 explicitly win and 16 legacy summaries without a host field.
  75 summaries say success and 11 say otherwise; failed/incomplete or host-unspecified records are not fresh native passes.
- 1,940 retained text log files, 11,920,238 bytes; no read errors or size-limit skips. Limits: 32 MiB per file, 512 MiB total.
- Scope: ArcForges .git/arcforges-verify/logs step logs, registered source worktrees' artifacts/test-logs, and
  C:/MyFile/Projects/dev/logs plus its immediate child log directories. No credential-store/data-root/key-file content.
- Summary timestamps span 2026-10-22T09:12:32Z through 2026-10-26T02:10:17Z. These runs postdate the original observation.
- Exactly six explicit case mentions/outcomes: acknowledgements 25,160,420 in mr13-author2.out and mr14-author.out;
  all six passed. Neither failed-case markers nor nearby unavailable diagnostic candidates were found in those mentions.
- The original raw failure was not found in this bounded scope. This does not assert that it exists nowhere.
  Many retained formal logs summarize projects without individual passed-case names; file/run counts are not test counts
  or proof that each run reached the original scenario.
- The first audit matched the current test-output format; a second audit also inspected every CrashConsistencyTests
  mention for alternate failure markers/nearby unavailable context. Both are read-only, not fresh crash/stress batches.

Scripts/output: C:/MyFile/Projects/dev/logs/mr15-audit.py/.ps1/.out/.err/.exit, mr15-audit2-edit.py,
mr15-audit2.py/.out/.err, mr15-audit2-inspect.exit and the two JSON manifests.
Final audit JSON SHA-256: ba16cbe71de88665228e807460632a52c1915591f5d42fe36d28e6cd96f8c0c4.
Initial audit JSON SHA-256: 3be003d79b601c7f8928495bfdf40488a486e114e9a30d71705daf7891f53cb4.

## Current evidence and diagnostic boundary

Fetched source main 5fa2ad5fe77bef791b96db11129b3851fe55c940 has the same tree
852d5472ff079f9df9debe57a1a3329f8bc0faf9 as reviewed head 0d261bbe1d48f3c1e9848c15f32a26132cf030da.
The MR-14 complete native profiles already passed at that exact code tree: Windows13/1148 s, Linux16/1364 s.
MR-14 author full Store tests passed Windows95/97 (2 platform skips) and Linux94/97 (3), with crash cases25/160/420
explicitly passed on each host. Linux retained mr14-author.out contains those three results too.
This is existing isolated-backend evidence, not a new MR-15 reproduction or real Credential Manager validation.

CrashConsistencyTests still demands every sampled sealed value be available after kill/reopen and prints
UnavailableReason on failure. TaskSecrets/NodeDataKeyRing distinguish a missing/unrecorded/unreadable/wrong-length key,
a changed backend, purge and AES-GCM authentication mismatch. No assertion, timeout, retry policy, key generation,
read-back policy or guard was weakened or changed. No source/Design/runtime patch was justified by this audit.
All 20 being unavailable alone cannot choose between the failure categories or prove a lost key write.

## Remaining obligation and authorization

AR-22 records a closure rule requiring a proven cause and discriminating regression/repair where applicable; more
isolated passing runs cannot close it. Capture an existing or naturally recurring failure's nonsecret diagnostic before
any retry/reset, identify the exact binary/commit/backend/isolation mode and preserve the original output. Do not print
key or environment values. No new OS-store call, listing, read-back, opt-in, tier run, cleanup or stress is authorized.
MR-16 remains blocked with its recovery proposal; no original real-store stress is repeated. Any future real-store
experiment needs separate explicit owner authorization and an approved isolated venue; none is proposed for execution now.
This entry blocks no other maintenance task and changes no delivery state. AF-NODE-02 owns its record.

Maintenance counts after this disposition: 105 total, 35 disposed, 66 open, 3 deferred-validation items
(MR-07/AR-20, MR-11/AR-21, MR-15/AR-22), 1 blocked (MR-16): 70 still unresolved in total.
Next eligible maintenance item is MR-17; skip MR-16 under its existing block. AF-REC-01/later features remain unstarted.
All analysis and direct record review are by OpenAI Codex alone under the owner's no-other-model/agent instruction.
