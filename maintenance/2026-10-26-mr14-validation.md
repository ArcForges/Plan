# MR-14: live SQLite sealed-value erasure, 2026-10-26

MR-14 is fixed. Design#34 merged first as 3df9db7946e9af6fd1e43f97216adfc44fd55507.
The additional direct-review finding in the common idempotency summaries was resolved in
[Design#35](https://github.com/ArcForges/ArcForges-Design/pull/35), merge 2d9995e78c4aa0f6327371ab0b5639857718da5c,
reviewed head f45a6f2deae5d02a0256b4a5fa7f57ab1fc9cb41, tree 1e93ab47a607ee7f4ccdafe57b8659b8a911da2f.
Its complete native Windows 3 steps/26 s and Linux 3 steps/45 s
passed before implementation merge; all results and both required statuses were read. AD-0004 and contracts README
now distinguish the stored logical outcome from the transient known-HAPPENED checkpoint error on replay, without
replacing dedup bytes or repeating deletion. No source/profile input changed; the source checks use the same final head.
ArcForges#56 merged as 5fa2ad5fe77bef791b96db11129b3851fe55c940, reviewed head 0d261bbe1d48f3c1e9848c15f32a26132cf030da,
tree 852d5472ff079f9df9debe57a1a3329f8bc0faf9, base 448e28dc247fb4234607cc4e811f3723f53e9b31.

- [Design#34](https://github.com/ArcForges/ArcForges-Design/pull/34), [design review](https://github.com/ArcForges/ArcForges-Design/pull/34#issuecomment-6405954167), [gate](https://github.com/ArcForges/ArcForges-Design/pull/34#issuecomment-6405967642).
- [ArcForges#56](https://github.com/ArcForges/ArcForges/pull/56), [author evidence](https://github.com/ArcForges/ArcForges/pull/56#issuecomment-6406450264), [direct review](https://github.com/ArcForges/ArcForges/pull/56#issuecomment-6406450558).
- Final source gate: https://github.com/ArcForges/ArcForges/pull/56#issuecomment-6406691491.

## Diagnosis and repair

The original secure_delete=ON pragma was already present. The confirmed gap was post-commit checkpoint handling:
manual PurgeTaskRecord did not checkpoint at all, so it acknowledged success with old ciphertext still present in the
main database/WAL. A retention purge attempted a checkpoint only when it changed rows; a held older read snapshot
could block it, and the next pass changed zero rows and never retried physical erasure.

Manual purge now attempts a truncating checkpoint after the command and its logical dedup response commit, including
identical-command replay. A busy checkpoint or SQLite exception produces the existing INTERNAL/internal error with
known effect HAPPENED and AFTER_TIME advice. It never implies rollback or overwrites the stored logical result:
ApiCommands parses the stored bytes into a new response before this post-commit step. Release the reader and replay
the identical command to reattempt the checkpoint. A refused logical outcome does not take this path.

PurgeDue attempts a checkpoint on every pass, including zero newly purged rows. This retains retry across a restart
without a new marker, schema or migration. The returned count is logical purges, not a physical-erasure completion flag.
A long read snapshot can retain old sealed bytes until a checkpoint succeeds; housekeeping uses its existing 10-minute
interval. This is live SQLite-file erasure, without a device/filesystem/external-copy guarantee. MR-13 backup exclusion
stays separate. No key rotation/deletion, real OS-store operation or restricted credential-file operation is introduced.

## Real before/after evidence

Test-only baseline dcb10d0ae8e5ce97e45080b64815457c13286420 (tree 703ab467a901a2abe1147280da37639c36749ccf)
has unchanged production from 448e28d. Both native hosts built Release with zero warnings/errors: Windows 13.68 s,
Linux 9.88 s. Each host then had 2 retention failures (0 skips) and 4 own-platform RPC failures (4 opposite-platform
skips), test exit 2, both wrappers drained with exit 0. The retention failure found old ciphertext after a zero-new-row
pass; unblocked manual purge found ciphertext after success; held-reader manual purge incorrectly returned success.

The initial test-only 1cb7c38a36a771845399d82c5966eb017cefca25 had four compile/analyzer errors: the test used the
wrong sealed-input type and omitted direct cancellation-token references. Neither regression suite nor AOT ran there.
These errors were corrected before the actual failing baseline. They are not product failures or validation passes.

At the fixed head (Linux author working tree byte-identical; Windows clean fetched head):

| Check | Native Windows | Native Linux |
|---|---|---|
| Changed-file format and Release build | pass, 0 warnings/errors; build 13.22 s | pass, 0 warnings/errors; build 3.89 s |
| New retention regressions | 2/2, no skips, 13.877 s | 2/2, no skips, 10.783 s |
| New real-RPC purge regressions | 4 passed/4 Linux skips, 10.192 s | 4 passed/4 Windows skips, 7.215 s |
| Full affected Store project | 95 passed/2 platform skips of 97, 13.611 s | 94 passed/3 platform skips of 97, 10.712 s |
| Existing affected TaskService class | 9/9, no skips, 5.512 s | Windows-only class; no new Linux execution claim |
| Host and Bench Native AOT publish | both pass, 0 warnings/errors | both pass, 0 warnings/errors |
| Diff and author wrapper | clean, exit 0 | clean, exit 0 |

Windows Store skips are the Linux-only directory-mode/Secret Service selection cases; Linux skips are two Windows
mapped-file cases and the Windows Credential Manager denial guard. These are platform skips, never real-store passes.
The new tests use real SQLite/GCM, real old read snapshots and real native attempts through a real RPC node. They
first checkpoint the original cipher into the main DB and prove it is present, then look for three 16-byte fragments
across main/WAL after cleanup. Payloads cover small cells and overflow/free-list pages (Store: 32 and 131072 characters;
RPC: 32 and 8192). They assert known committed error effect, unavailable logical values, identical-ID replay, no new due
row, integrity and unchanged schema. Only the external key backend is isolated; every fixture deletes its own isolated
keys and checks for leaks. New RPC tests run the node in-process; AOT publication/full native profiles are separate
evidence, not a new standalone Native AOT purge-runtime claim. No injected I/O failure was tested.

Author commands: changed-file dotnet format, dotnet build ArcForges.slnx -c Release --no-restore, dotnet test --project
tests/ArcForges.Node.Store.Tests --filter-class ArcForges.Node.Store.Tests.SecretPageErasureTests -c Release --no-build,
the analogous PurgeSecretErasureTests class in Node.Core.Tests, the full Store project, the Windows TaskServiceTests
class, and affected Host/Bench AOT publishes (Windows eng/publish.ps1 with the two-element component array in the
installed MSVC environment; Linux python3 eng/verify_linux.py publish host,bench). Exact commands, durations and exits
are retained in mr14-before2 and mr14-author scripts/logs on each host. The original mr14-before compile-only logs remain.

## Final pushed-head merge gates

Both legs ran python eng/verify.py run-and-report, at the exact head/tree above. All results and engine-reported required
statuses were read before merge; the owner-hosted checks were skipped as expected. No competing build/test ran on the
same host. Direct self-review by OpenAI Codex under the explicit single-model/no-agent instruction left no unresolved issues;
no independent reviewer or other model/agent is claimed. No assertions, bounds, hooks or required checks were weakened.

| Repository | Windows | Linux |
|---|---|---|
| Design, head bebad6a2e5f83d7c39d34229e2168dd31c97a5be | full 3 steps/15 s, all pass | full 3 steps/34 s, all pass |
| Design follow-up, head f45a6f2deae5d02a0256b4a5fa7f57ab1fc9cb41 | full 3 steps/26 s, all pass | full 3 steps/45 s, all pass |
| ArcForges, head 0d261bbe1d48f3c1e9848c15f32a26132cf030da | full 13 steps/1148 s, all pass | full 16 steps/1364 s, all pass |

Source summary IDs: Windows 20261026-015108-0d261bbe1d48-win; Linux 20261026-091249-0d261bbe1d48-linux.
Design summary IDs: Windows 20261026-010658-bebad6a2e5f8-win; Linux 20261026-090652-bebad6a2e5f8-linux.
Design follow-up summary IDs: Windows 20261026-021046-f45a6f2deae5-win; Linux 20261026-095744-f45a6f2deae5-linux.
Windows full summary: C:/MyFile/Projects/ArcForges/ArcForges/.git/arcforges-verify/logs/20261026-015108-0d261bbe1d48-win/summary.json.
Linux full summary: /home/sammiller/arcforges/ArcForges/.git/arcforges-verify/logs/20261026-091249-0d261bbe1d48-linux/summary.json.
Wrapper logs: C:/MyFile/Projects/dev/logs/mr14-*.out/.err/.exit and /home/sammiller/arcforges/logs/mr14-*.out/.err/.exit.

## Record and stopping point

The maintenance list is updated to fixed; one AF-NODE-02 completion note is appended through tools/plan.py ledger
after the implementation merge. No delivery-graph state changes or later feature activation.
The owner subsequently asked to finish MR-14 and stop to adjust context to 872000. This supersedes automatic continuation:
MR-15 is next and remains unstarted. MR-16 remains blocked. List totals after MR-14: 35 disposed, 67 open,
2 deferred-validation items (MR-07/AR-20 and MR-11/AR-21), 1 blocked item (MR-16), 105 total.
See [current handoff](2026-10-26-handoff.md); refresh all refs, host processes and MCP tools on any later resumption.
