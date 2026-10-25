# MR-12: LocalRpc named-pipe user ownership

The producer repair is [DesktopPlatform#200](https://github.com/ArcForges/DesktopPlatform/pull/200), reviewed head
`66ffbc7c6ec38dfa52e0f909df48f9122ffe1668`, tree `46768fc94d3f45383f8d008d1e433aebd5b47cb2`,
base `49e2dbe9dcb0d268e16cbeca237f5f4284d50b9a`.

## Repair and scope

The client previously used PipeOptions.CurrentUserOnly, which checks the token's default owner rather than its user SID. An elevated
token's default owner can be BUILTIN\Administrators, so it refuses a service pipe owned by the same user's SID. The connected server
handle's owner is now checked against WindowsIdentity.User before returning a stream to HTTP/2. Foreign users, group owners and
missing SIDs fail closed. A query or refusal failure disposes the pipe and remains a pre-stream LocalRpcConnectException; no request
bytes have been sent. No new public API, dependency or native import was added.

A parent-child listener previously also relied on the token's default owner. It now explicitly sets the user-SID owner and protected
user-only DACL on every instance, retaining FirstPipeInstance. This prevents the stricter client from refusing an elevated parent's
own listener. Service-mode ACLs, remote rejection and peer-resolution policy are unchanged. The raw ACL probes no longer apply a
second, different default-owner check; their server access-list/owner assertions remain. Current README and wrong-user procedures
name the explicit user-SID rule. No current Design contract change was required: the existing same-user boundary is restored.

The newly authored test file is explicitly classified as first-party in the existing provenance inventory. No reused record, historical
receipt, policy, pin, dependency admission or verification script was changed. ArcForges's use of a new producer version is separate
MR-43; this repair does not claim consumer adoption.

## Author evidence, native Windows through MCP

- Locked affected restore; Release build with zero warnings/errors; changed-file format verification.
- LocalRpcPipeOwnershipTests: 4/4. SID input cases deny foreign/group/SYSTEM/null values. Real parent-child and service listeners each
  carry bytes over three instances after the user owner check; a default-owner pipe is accepted only when that owner is the user.
- Existing parent-child and service ACL checks: 2/2, unchanged assertions.
- NamedPipeCarriesGeneratedCallsAndSurvivesMalformedFramesOnTheRealOsStream: 1/1 using real pipes and generated RPC calls.
- Routine LocalRpc suite: 947 passed, 57 documented platform/local-opt-in skips, zero failures (1004 total).
- Locked restores and Native AOT publish of LocalRpcAotTests and LocalRpcServiceAotTests passed without warnings. The native service
  probe then passed real Windows named-pipe, same-process peer identity, raised deadline and stream-lane/heartbeat checks.

These runs used a token whose default owner equals its user SID. The elevated default-owner branch and an actual ordinary-node /
elevated-client pair were not exercised. SID input cases are unit coverage, not substitute OS tokens or proof of cross-user denial.
AR-21 retains the real cross-integrity procedure and now names the producer's four-test class in each user-provided token. AR-02
second-account isolation remains separate. There was no elevation or real credential-store operation.

## Failures diagnosed and retained

The first author build failed CA2000 after adding token lifetime in the pipe-transfer method. Keeping that lifetime inside the
owner-query helper resolved the warning; the analyzer remains enabled. The successful Release build above followed that source fix.

At initial pushed head `16b33c0b6d16a17027c3f78c023ba2a8fd192df5`, Linux provenance-policy failed on the missing new-test inventory
entry (21 s leg), and Windows native-stage reached the same assertion (61 s leg). Both retained summaries are failed/incomplete;
subsequent steps did not pass. Exact tracked-minus-classified comparison found only the new test file, which the follow-up registered.
No runtime source changed after its author checks. Both final-head formal legs were started after the old leg on that host had ended;
the residual Linux dotnet processes were reusable MSBuild workers, not another build/test run. No old status was reused.

A transient Windows MCP transport error during record preparation was recovered by a read-only log/branch inspection: the branch
creation had not happened and the background verification continued. No test or verifier was re-launched for that tool error.

Author logs: Windows `C:\MyFile\Projects\dev\logs\mr12-author*` and `mr12-extra*`; first failed formal wrappers `mr12-formal*`,
final wrappers `mr12-final*`. Both hosts retain their own summary and step logs; no build artifacts were moved between hosts.

## Final post-push verification and merge

Both hosts fetched the final head above and ran their own complete profile through native MCP using `python eng/verify.py run-and-report`:
Windows 17/17 steps, 532 s; Linux 24/24 steps, 406 s. Every selected result passed, with matching head/tree/base. Formal LocalRpc totals
were Windows 947 passed / 57 documented skips (1004 total), Linux 946 passed / 53 documented skips (999 total; platform-specific theory
rows), zero failures. Windows verified all 21 candidate packages at local-only version 1.0.0-ci.1.1; that is not a public NuGet version.

Summaries retained on their own hosts under DesktopPlatform/.git/arcforges-verify/logs:
- Windows: `20261025-163937-66ffbc7c6ec3-win/summary.json`.
- Linux: `20261026-003932-66ffbc7c6ec3-linux/summary.json` (the host's local date had advanced to October 26).

Complete summaries/all selected results, live exact-head required success statuses, owner-skipped hosted checks, head/base and freshly
fetched main were read before merging. Full nine-file direct self-review by OpenAI Codex alone, comment 6400304577, had no blocking
finding; no independent reviewer is claimed under the owner's no-other-model/no-agent instruction.
DesktopPlatform#200 merged as `e02ebe455d4fe2c06b19dabc0f3179a43ab21aa6`; its clean primary checkout was fast-forwarded and the repair
branch/worktree retained. No work in other repositories was discarded.

The normal main-push [Publish NuGet run 40213555173](https://github.com/ArcForges/DesktopPlatform/actions/runs/40213555173) was observed
in progress at merge commit e02ebe4, run 148/attempt 1, started 2026-10-25T16:49:54Z. Publication is not yet claimed successful here.
MR-43 must use a successfully published producer cohort with the normal admission evidence; no package was reinstalled or downloaded
for post-publication verification. AF-DP-01 remains delivered, with AR-21's remaining real cross-integrity validation linked.
