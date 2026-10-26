# MR-13: retained backups exclude sealed task input

## Scope and authority

MR-13 confirmed that pre-migration backups kept decryptable task_secret values after both live-store purge paths. The maintenance
list permits either removing values from all retained backups or excluding them from backups. This repair selects exclusion:
new copies are sanitized before publish; older retained copies are sanitized on store open before migration/startup. Failure
to sanitize any retained copy refuses the open. Task records, nonsecret data, presence-only names and store_meta schema version
are retained. A backup restore requires new submission for sealed inputs, including values still available in the live store.
The live store's retention and the node data key are unchanged.

[Design#33](https://github.com/ArcForges/ArcForges-Design/pull/33) merged first as
6358f94ebf32f4e2968d591413d86f5e2939decc. Reviewed head 029fc26067a26a0d4e9a92cb99ca857363cd6682, tree
d2a106cfee32753d702104db2e4e5fc0bb90a407, base 772435e591339a0c94ec34832bbebe5b94094a57.
AD-0006, execution, startup, distribution and node-store documentation agree on this retention policy and its restore consequence.

Design author checks: zero errors, protoc 25 files, both SQL schemas, 47 tool tests with 20 Windows platform skips, diff clean.
Final native Windows full 3 steps/25 s (20261026-000524-029fc26067a2-win); Linux 3 steps/46 s
(20261026-080520-029fc26067a2-linux). All six results, both wrapper exit records 0 and both exact-head required success statuses
were read, owner-hosted check skipped. Fresh main/head/tree checked before merge.
[Direct self-review](https://github.com/ArcForges/ArcForges-Design/pull/33#issuecomment-6405254475);
[final gate](https://github.com/ArcForges/ArcForges-Design/pull/33#issuecomment-6405277250).

## Real before-fix proof

Source test-only head ebc2b951cff881ab85173ca7ccef85d16c7b61c0, tree 4ebdbb06f88f0dc009b1bf7f2090496f19b1c376,
kept production unchanged at main 54e0809d7386f1ec24c39cd4ec1a4fc90f35177a. Both native hosts fetched through Git.

- Windows locked restore/Release build passed, zero warnings/errors, build 19.89 s. Five actual regressions failed, zero skips,
  test exit 2, 3.317 s.
- Linux locked restore/Release build passed, zero warnings/errors, build 15.57 s. Five actual regressions failed, zero skips,
  test exit 2, 0.878 s.
- Four cases restored a real SQLite backup with the original isolated key backend still available, and found the input Available
  instead of Unavailable: new copies with small and overflow-sized payloads, and three legacy retained copies after immediate
  and retention-based live purges. The live purge itself passed its unavailable assertion before the legacy restore failed.
- The fifth case found that a corrupt retained backup did not refuse the open. The unexpected successful open was disposed.
- Both wrappers captured the expected test failures and exited 0; these are before-fix evidence, never a successful regression
  or complete profile. No formal profile ran on either intermediate test-only head.

The AES-GCM, SQLite files, backup copy and restored store are real. Only the external key backend is isolated, as required by
the secret-store test policy. Tests use synthetic input and their own temporary roots, verify key cleanup through the isolated
backend, and never call a real OS secret store or inspect/delete credential or orphan-credential files.
They also require nonsecret records/names/schema preservation, unchanged live input availability, no migration, backup integrity,
absence of sampled old ciphertext bytes, and refusal without damaging live input. An unrelated file is retained untouched.

Before logs: Windows C:\MyFile\Projects\dev\logs\mr13-before.{ps1,out,err,test-exit,exit};
Linux /home/sammiller/arcforges/logs/mr13-before.{sh,out,err,test-exit,exit}.

## Diagnosed author iteration

The first fixed working-tree Windows author attempt passed formatting but failed compilation with CS0111: an added
StoreBackupException(string, Exception) duplicated the existing constructor. The duplicate addition was removed; the existing
constructor is reused. No regression or AOT checks ran in that failed attempt. This was a compile-only failure, not a passed
profile or weakened test. Logs: C:\MyFile\Projects\dev\logs\mr13-author.{ps1,out,err,exit} (exit 2).

## Author and final evidence

[ArcForges#55](https://github.com/ArcForges/ArcForges/pull/55) merged as 448e28dc247fb4234607cc4e811f3723f53e9b31.
Final reviewed head: fcd99c085bb8b5bba44e4be4cb43d97fc147979e.
Tree: 5517871c08c62ec72e659a37ddf014cadc51caa3.
Base: 54e0809d7386f1ec24c39cd4ec1a4fc90f35177a.
Four files: backup sanitization, its store-open hook, reuse of the existing tombstone and real backup/restore regressions.

New copies are sanitized before rename/publish. Store open processes every retained backup before startup or any existing
migration path. The copy uses secure_delete, DELETE journal mode and VACUUM, then integrity_check. Existing schemas are not
migrated or expanded. The original task secret rows in the live store remain usable until their own purge; key operations and
retention policy are unchanged. Older copies with no task_secret table are not given a new table. Copy failures retain the
underlying error and refuse the open. Named backup retention remains three.

Windows author working tree was byte-identical to this final head: changed-file format/diff and Release build passed with
zero warnings/errors (10.77 s); new regressions 5/5, no skips, 3.780 s. Full affected store project: 95 total, 93 passed,
2 platform skips, 8.052 s. Skips: Linux Secret Service selection and Unix directory modes. Host and Bench win-x64 Native AOT
both published with zero warnings/errors; mr13-author2 exited 0.

Linux fetched the exact final head: Release build zero warnings/errors, new regressions 5/5, no skips, 0.880 s. Full affected
store project: 95 total, 92 passed, 3 platform skips, 3.013 s (two Windows mapped-file behaviors and the Windows-only
Credential Manager denial guard). Host and Bench linux-x64 Native AOT both published with zero warnings/errors; changed-file
format/diff passed and worktree clean; mr13-after exited 0. Both author jobs drained before either complete final profile.
These author tests exercise the managed store on each native host; AOT publish validates the affected components. A broader
native executable backup-runtime claim is not inferred.

[Author evidence](https://github.com/ArcForges/ArcForges/pull/55#issuecomment-6405463572).
[Exact-head direct self-review](https://github.com/ArcForges/ArcForges/pull/55#issuecomment-6405463805): all four files against
the merged Design, no findings. No identical full suite was repeated for review.
Author logs: Windows C:\MyFile\Projects\dev\logs\mr13-author2.{ps1,out,err,exit};
Linux /home/sammiller/arcforges/logs/mr13-after.{sh,out,err,exit}.

Both complete post-push native profiles passed at the final reviewed head:

- Windows full: 13 steps/1135 s, 20261026-002302-fcd99c085bb8-win.
- Linux full: 16 steps/1355 s, 20261026-082255-fcd99c085bb8-linux.
- Every selected summary result read and passed, including JIT/native exclusive suites and startup gates.
- Both required exact-head arcforges/windows and arcforges/linux statuses success; owner-hosted checks skipped as configured.
- Fresh PR head/tree and source main/base checked immediately before merge.
- [Final merge gate](https://github.com/ArcForges/ArcForges/pull/55#issuecomment-6405736718).

Formal logs: Windows C:\MyFile\Projects\dev\logs\mr13-final.{out,err,exit};
Linux /home/sammiller/arcforges/logs/mr13-final.{out,err,exit}. Both native runners exited 0 and drained, with no competing
build/test. No earlier head, expected failure, partial run, skip or relaxed assertion substituted for these gates.
Only after the actual source merge, the maintenance list was updated and the owning AF-NODE-02 ledger note was appended
through the Plan CLI. Task states and later feature activation remain unchanged.

The implementation uses existing tables and tombstones. No new or deployed database schema migration, enum/RPC/package change,
real credential-store operation, node-key deletion/rotation or orphan credential-file operation is included. MR-16 remains blocked.
MR-14's live-store page/WAL erasure is the next separate item. No user manager shutdown, daemon-reload, pkill -f, LAN/cloud MCP
or AF-REC-01/later feature activation. All work/review by OpenAI Codex alone; no other model/agent or independent review claimed.
