# MR-95: recovered command start clocks and limits

Date: 2026-10-25. Design: [ArcForges-Design#28](https://github.com/ArcForges/ArcForges-Design/pull/28).
Implementation: [ArcForges#50](https://github.com/ArcForges/ArcForges/pull/50).

## Design dependency

Design merged first as `64e7c99459d25b2e247471f4fad26b0baf51fdb9`, reviewed head
`1683367cf3ba7cc0377e17c5e3cc981d61a48722`, tree `ebe9b24d3111a696ec63da161fb939edcc5b244d`,
base `c36bf89ed5b4f47dc09a2e40ee2c7b82c96788c8`. Architecture 04 section 3 specifies additive Windows
`logs/<attempt>/started.json` (schema 1, attempt ID, root PID plus exact creation FILETIME, UTC resume time), written
atomically by the holder after the actual command resumes, before its best-effort live report. Launch steps never produce it.
Absent, incomplete, invalid or wrong-attempt evidence does not identify a root. Linux uses the existing unit/main-root state.
The recovered STARTING attempt writes its known command start into existing columns, and timeout/CPU polling resumes without
a fresh budget; elapsed downtime and cumulative container CPU still count. This does not claim polling enforcement while the node is down.
No SQL or RPC schema change, migration, new IPC, updater or task activation.

Complete exact-head Design summaries/all results, both required statuses, live main/head/base and owner-skipped hosted check were read:
Windows full 3 steps/17 s (`20261025-170442-1683367cf3ba-win`); Linux full 3 steps/46 s
(`20261026-010440-1683367cf3ba-linux`). Author locked proto-toolchain restore, require-protoc check (25 proto files compiled,
zero errors), generated C# build (zero warnings), and 44 tool tests (20 existing Windows skips) passed.
Direct self-review by OpenAI Codex alone, comment 6400564752; no independent reviewer claimed under the owner's instruction.

## Implementation and regression

Final pushed head `265342e91fe69a53d263dce1eb013af7871af9fd`, tree `07fd93e4c67b33ec9a7d9a047c52bcf5186de4b6`,
base `5eaee92a4a964469bad41dad28dad9787b7552cf`.
The Windows holder records only the resumed command, and a reopened handle reads validated evidence; a new job member could
be another launch step, so it cannot set the command clock. Linux refresh now fills a previously unknown root from unit state.
The supervisor starts recovered timing once that root is known, keeps the original UTC start, and persists existing root/start fields.
An evidence-file I/O/access failure cannot abandon an already resumed root: the live report continues and a node warning names
unavailable durable evidence without logging arguments or environment values.

Four real-process cases cover timeout/CPU limits with the root starting during the node gap or after recovery.
They assert STARTING/no clock while held, the persisted start on the correct side of recovery, known root, node_gap,
HAPPENED, and eventual TIMED_OUT/CPU_TIME_EXCEEDED (including CPU accounting).
A Windows two-step case proves a new launch-step process after recovery cannot start the command clock.
A Windows blocked temporary-file case proves evidence-write failure still yields a supervised TIMED_OUT live root and warning.
Format tests check exact schema-1 names, identity/time round-trip, and absent/torn/wrong-attempt/unknown-schema/invalid evidence.
Fixtures use actual jobs/units and processes, fixed launch-step fault providers, isolated node secret stores and explicit cancellation;
no real Credential Manager store, orphan credentials, Linux user-manager termination, daemon-reload or broad process kill.

Before the product change, the first author build exposed CA1416 in a test helper lambda (no runtime evidence); the guarded foreach
fix built cleanly. Then all four recovery cases failed against unchanged product code, each waiting for the recovered start to persist.
Before command: `dotnet test --project tests/ArcForges.Node.Core.Tests -c Release --no-build --filter-method '*ARecoveredStartKeepsItsTimeoutAndCpuTimeLimit' --minimum-expected-tests 4 --output Detailed`.
After the product change, Windows Release build/analyzers and changed-file format passed; LaunchFault 18/18, TaskControl 15/15,
Windows platform suite 120 passed/1 documented skip: the WMI-created adoption target was already in a job (refusal asserted),
so outside-every-job adoption could not be demonstrated on this host. Host Native AOT published with zero warnings and LaunchFault 18/18 with
ARCFORGES_HOST_PATH selecting that native holder/helper; the node in these tests remains in process.
The first Windows author wrapper ended after its passing tests on an erroneous nonexistent eng/aot.py help path.
The corrected AOT job used the actual eng/publish.ps1 -RuntimeIdentifier win-x64 -Component @('host') and passed.

The initial Linux author run at 5d80985 failed two gap-start cases before recovery (9 passed, 7 platform skips, 2 failed).
The observer incorrectly compared the full executable name to /proc/<pid>/comm; a native probe confirmed comm=arcforges-testl
while /proc/<pid>/exe resolved to the full arcforges-testload path. The follow-up changes only that observer to resolve the unit
MainPID's executable and moves cleanup around early offline failures; assertions and bounds are unchanged. One failed fixture
reported its owned attempt unit still active, then its cleanup drained it; later read-back confirmed inactive/dead and no root.
The first follow-up launch compound timed out during build; logs stopped, no exit marker or surviving job/test remained.
That incomplete run is retained as mr95-author2; the corrected standalone background launch is mr95-author3, with distinct logs.
The corrected Linux author run at final head passed locked restore, full Release build/analyzers (zero warnings/errors),
changed-file format, LaunchFault 11 passed/7 Windows skips (all four new portable cases executed), Linux platform 82/82,
format tests 14/14, and host Native AOT with zero warnings/errors. LaunchFault with the native holder/helper again passed
11/7 skips. TaskControl is Windows-only: all 15 Linux rows skipped, providing no Linux execution evidence. Final author exit 0;
no leftover assertion or competing native test/build was present before the complete final-head Linux formal leg started.

Author commands (run through native MCP, with each job writing its own stdout/stderr/exit marker):

```text
dotnet restore ArcForges.slnx --locked-mode
dotnet build ArcForges.slnx -c Release --no-restore
dotnet test --project tests/ArcForges.Node.Core.Tests -c Release --no-build --filter-class ArcForges.Node.Core.Tests.LaunchFaultTests --output Detailed
dotnet test --project tests/ArcForges.Node.Core.Tests -c Release --no-build --filter-class ArcForges.Node.Core.Tests.TaskControlTests --output Detailed
dotnet test --project tests/ArcForges.Node.Platform.Windows.Tests -c Release --no-build
dotnet test --project tests/ArcForges.Node.Platform.Linux.Tests -c Release --no-build
dotnet test --project tests/ArcForges.Node.Platform.Windows.Tests -c Release --no-build --filter-class ArcForges.Node.Platform.Windows.Tests.FormatTests
dotnet format ArcForges.slnx --no-restore --verify-no-changes --include <changed C# files>
```

Each platform suite runs on its native host; the portable format class also ran on Linux. Windows AOT uses the installed MSVC
Developer PowerShell (VS 2026 18.10.1) and `eng/publish.ps1 -RuntimeIdentifier win-x64 -Component @('host')`.
Linux AOT uses `dotnet publish src/ArcForges.Host -c Release -r linux-x64 -o artifacts/publish/linux-x64/host -warnaserror -tl:off '-clp:Summary;ForceNoAlign' -p:TrimmerSingleWarn=false`.
Both then re-run LaunchFault with ARCFORGES_HOST_PATH set to their own published native host. This selects native helper roles;
these author nodes remain in process, distinct from the formal full profile's closed-loop native executable tests.

## Final post-push verification and merge

The Windows full leg already running at superseded head 5d80985 was allowed to drain. Its result is retained and cannot satisfy
the final head's gate. After its successful completion and host drain, the final Windows author check passed full Release build
(zero warnings/errors), LaunchFault 18/18 and changed-file format; its own exit marker is 0. Only then did the final-head full leg start.
The superseded Windows leg passed all 13 selected results in 965 s at 5d80985, matching its tree e1fdfe382aad and base 5eaee92;
summary `20261025-173103-5d80985b54dc-win/summary.json`. It drained before final-head author/formal checks began;
its required status remains attached only to that older commit.
Final-head Linux full verification passed all 16 selected results in 1128 s, matching head 265342e, tree 07fd93e and base 5eaee92;
summary `20261026-013801-265342e91fe6-linux/summary.json` under ArcForges/.git/arcforges-verify/logs. Every result was read,
including real-OS, secret scan, format/build, CI tests, AOT, native tools/closed loop, package, both exclusive suites and startup gate.
The wrapper exited 0, required status was reported, and the verification worktree was clean with no native test process remaining.
Final-head Windows full verification passed all 13 selected results in 948 s with the same head/tree/base; summary
`20261025-174835-265342e91fe6-win/summary.json` under ArcForges/.git/arcforges-verify/logs. Every selected result was read,
including CI tests, AOT, native tools/closed loop, package, both exclusive suites and startup gate; wrapper exit 0 and clean verification tree.
Complete nine-file direct self-review at final head by OpenAI Codex alone, comment 6400937846, found no blocking diff issue.
No independent reviewer is claimed. Freshly fetched source main/head/base and Design main, both exact-head required success statuses,
mergeability and owner-skipped hosted checks were checked before merge (final-gate comment 6401216341).
ArcForges#50 merged as `6caf418af3eba19a5d4d7989e8ed11476b67736b`. No other source worktree or existing modification was discarded.

Both native hosts retain their own step logs and summaries; no artifact was transferred between hosts. Windows author logs are
C:\MyFile\Projects\dev\logs\mr95-before*, mr95-after*, mr95-author*, mr95-aot*, mr95-final*;
Linux logs are /home/sammiller/arcforges/logs/mr95-author*, mr95-image-diagnosis.out and mr95-final*.

## Remaining obligation

A live older Windows holder that lacks started.json is not backfilled by this repair. AF-DIST-02, still planned, now explicitly
requires preserving known command-start/limit evidence or settling STARTING before a transparent cross-version upgrade, with
real both-platform gap/post-recovery timeout and CPU-limit update acceptance. No cross-version update is claimed verified.
Plan CLI ledger notes on AF-EXEC-02 record the current-version repair and exact verification/merges; AF-DIST-02 records
the future cross-version obligation, still planned. The MR-12 publication follow-up is recorded separately on AF-DP-01 and in its
validation report; consumer adoption MR-43 and real cross-integrity validation AR-21 remain separate.
