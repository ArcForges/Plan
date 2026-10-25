# MR-102: stopped Windows root process run-down

Date: 2026-10-25. Source PR: [ArcForges#48](https://github.com/ArcForges/ArcForges/pull/48).
Reviewed source head: `95f5ea2cb60f9c0c8fefa5c11ab5d367a1a72395`.
Tree: `7a990364a4f100799473b301fe1e00127ed3b002`.
Base: `e79f837986c0c88a428826ed71813936200b2f38`.
Merged as `3990e07be8cc1ad4494bc73fe2013ba36acc6b80` after both required exact-head checks passed.

## Repair and review

The root's unbounded process-handle wait delayed the durable exit record after a forced job termination.
The root now shares the guarded process wait with launch/end steps. It checks every 250 ms; steps retain
their 50 ms interval. Only a known final nonzero exit status plus zero active child-job processes permits early
completion. Zero, STILL_ACTIVE, unreadable status and failed accounting queries keep waiting for the process handle.
Checking status first avoids job accounting queries while a command is running.

The node owns the job's single completion port, including after recovery (AD-0005 Windows sections 3–4).
The holder also needs to observe limit stops while the node is down. Four checks per second were chosen instead
of introducing another IPC lifetime and recovery protocol. This does add periodic wakeups to a long-running root.
A controlled real-holder CPU observation reported 0.000 ms increments over 30.012 s for the original wait and over
30.017 s for the new wait, at the host's process-time resolution. It establishes no measurable cost in those
samples; it does not establish zero overhead.

OpenAI Codex authored and reviewed the complete two-file diff directly, without other models or agents, under
the owner's explicit instruction. Review covered root/step ordering, exit-code guards, handle lifetime, accounting,
holder acknowledgement and node recovery against Design 04 sections 3,6,9 and AD-0005 Windows sections 3–4.
No blocking findings; exact-head review comment: 6398991351. MR-103's end-step budget remains a separate open repair.

## Regression evidence and earlier failures

The final forced-root test waits for the actual command's ready marker and a recorded RUNNING attempt, attaches a
debugger to that root, and holds its EXIT_PROCESS event. The command ignores CTRL_BREAK and has zero cancel grace,
so the forced phase must give it exit code 1. The task must end within the existing 5 s standard while that process
object remains unsignaled, with a durable exit record, empty job, CANCELLED/HAPPENED and no leftovers. Only after
those assertions does the test release the debugger and await the exact process object's run-down before cleanup.

The final test on the original implementation failed: still RUNNING after the 10 s failure-path wait
(`baseline-final-test.log`). With the repair, the whole 12-test LaunchFault class passed three times, and the
forced-root terminal observations were 415, 446 and 311 ms. Against the zero-warning Native AOT host, the entire
class passed 12/12, with root stop 267 ms.

The success test holds a real root's zero exit event, empties the remaining console job, explicitly confirms its exit
code is still 0 and the job has zero active processes, and requires both the end step and exit record to wait for
process-object completion. Removing only the zero-code guard fails this test with a premature exit record
(`zero-mutant.log`). This negative control is not a product pass. Temporary probe/mutant source was restored
byte-for-byte and rebuilt before final author validation.

Earlier development failures are retained, never counted as passes:
- Initial test compilation found a missing IdText import and xUnit cancellation-token analyzer references; corrected.
- An exploratory root without a break handler exited on CTRL_BREAK (0xC000013A), so it did not prove forced termination.
- An ordinary nonzero exit left console members active while debug-held; the empty-job guard correctly kept waiting.
  That exploratory case made an invalid empty-job assumption; the final forced test instead asserts exit 1 and zero members.
- An int/uint assertion compilation mismatch was corrected without changing its required zero value.
- Two transient Windows MCP 502 responses occurred during diagnostics. The saved script and completed result were inspected
  on recovery before any further launch; the background run was not duplicated.

## Final author checks

Logs and scripts stay on the Windows host under
`C:\MyFile\Projects\dev\logs\resume-20261025-mr102\`.

- `dotnet restore ArcForges.slnx --locked-mode`: passed.
- `dotnet format ArcForges.slnx --no-restore --verify-no-changes --include src/ArcForges.Node.Platform.Windows/AttemptRunner.cs tests/ArcForges.Node.Core.Tests/LaunchFaultTests.RootRundown.cs`: passed.
- `dotnet build ArcForges.slnx -c Release --no-restore`: passed, zero warnings/errors.
- `dotnet test --project tests/ArcForges.Node.Core.Tests -c Release --no-build --filter-class ArcForges.Node.Core.Tests.LaunchFaultTests --minimum-expected-tests 12 --output Detailed`, three runs: 12/12 each.
- TaskControl and EscapedTermination classes: 17 total, 16 passed, 1 Linux-only skip, no failures.
- Windows platform ci filters: 116 total, 115 passed, 1 existing adoption skip, no failures.
- `eng/publish.ps1 -RuntimeIdentifier win-x64 -Component host` in the Visual Studio developer environment: Native AOT with zero warnings.
- Entire LaunchFault class with `ARCFORGES_HOST_PATH` set to that native host: 12/12.
- Temporary HolderTests probe restored, source whitespace check passed, final worktree clean after commit.

## Required host checks

Both legs started after pushing the reviewed head, with no other build/test running on either host. Each fetched
that commit and ran `python eng/verify.py run-and-report` through its MCP. Both complete summaries and every step result
were inspected: same head, tree and base above, full profiles, all results successful.

| Host | Steps | Seconds | Summary |
|---|---:|---:|---|
| Windows | 13 | 963 | `ArcForges/.git/arcforges-verify/logs/20261025-143828-95f5ea2cb60f-win/summary.json` |
| Linux | 16 | 1132 | `ArcForges/.git/arcforges-verify/logs/20261025-223822-95f5ea2cb60f-linux/summary.json` |

The formal Node.Core ci suite had 256 passed/33 platform skips on Windows and 244 passed/45 platform skips on Linux,
zero failures on each. Both legs also completed all AOT publishes, native tools/closed loop, schema checks, JIT and
native exclusive suites, benchmarks, packaging and startup comparisons; Linux additionally passed the real-OS,
format and secret-scan steps.

Before merge, current main e79f837, exact PR head, mergeability, both required success statuses and the owner's
skipped hosted jobs were checked. No status was copied or posted manually. A transient Windows MCP 502 on a
progress read recovered; the original formal run continued to completion and was not restarted.

MR-103 stays open. MR-16 stays blocked with its recovery proposal, and no real credential-store cleanup/stress,
later feature activation, LAN/cloud MCP or database migration was performed.
