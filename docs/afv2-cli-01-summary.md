# AFV2-CLI-01 offline CLI evidence

Node PR 109 merged at f8b500dd299d1738e2f9c9daef3f674c519aa15e. Its tree
6cc53cd03d47d4f33f74d16227a105fcee02fe40 is identical to the independently
reviewed head 3adb905a324eae76b29c9053273c00ee53b37d70. Both designated hosts
reported success at that head. The main push had no publication workflow.

The CLI uses the current user's authenticated local Node to create, configure,
rename, repair, list and inspect Sandboxes, and to start, inspect, list and stop
Runs. Resource reads, usage streams and policy changes use ResourceService.
The Node service handles grants and inspection of the original durable command.
The fixed service bootstrap supplies Node start and shutdown. Doctor combines
the typed handshake, a resource snapshot and an optional owned Sandbox view.

Run Start preserves the exact argument boundary after the delimiter and prints
the accepted Run identity. Mutations print the original command ID and owner
epoch. Start also prints the selected revision and resolved terminal mode.
Receipt inspection retains the original namespace across a restart or
compaction. Stop reconciliation polls the original command. The installed
package exposes explicit local administration and the carried compatibility
operations documented by their owning tasks.

## Replacement proof before retirement

Node PR 109 preview commit e29765e53f9b1b27aafea27b2eb0e6c5babff02b
had tree c61ab52b969755049fbba1fba9ed525c54621451. Both designated hosts fetched
that exact head independently and ran the same installed positive CLI cases.
The fixtures exercised the actual extracted Native AOT Host and the bundled
official MXC 1.0.1 profile. Both case names and their outcome are preserved in
each raw log.

| Host | Cases | Package SHA-256 | Raw log SHA-256 |
| --- | --- | --- | --- |
| Windows deku | 2/2, zero skips | e4367825ce026f5853a6f1fcfc835403263968d2f81ca76b68ecc4e49e0884fb | cbc5ac30ea3bbf3aac9dc6fcb68931f2524a1a0b82a22312c107abf570d05968 |
| Linux H-22 | 2/2, zero skips | 82fd241a8c92130b977a28c3a8c935b420ea4359fb260b6a749fb39e6d894361 | 9ad5fb546c05335866687968eec82d739884daf761220fbebc64bf4a8e52a8bb |

The Windows raw path is
.git/arcforges-verify/launches/cli01-author-e29765e53f9b-win/native.log
in the Node repository on deku. The H-22 equivalent directory ends in
cli01-author-e29765e53f9b-linux. The owner-private H-22 launch used umask 0077.

The offline case exercised explicit argv, a path with spaces, a real isolated
payload, resource usage and set, a resource admission refusal, native Stop,
protected Sandbox repair, and an original Start receipt across compaction
and restart. The grant case first observed the unenrolled refusal and then
used the existing isolated enrollment input to reach the real grant operations.

After those results, the e7571296e77214b6c2bcbbc07cf7c2719047f53a candidate
removed the old execution parser and source from the product CLI. Its tree
is 342786e8274120901047e3dd0f1e57ab4ba5a4c1. The carried V1 subprocess and
native terminal regression client is test-only. It connects to the same
candidate Node through its isolated test binding. The V2 package tests
continue to call the actual product Host.

## Development checks

The Windows locked solution build passed with zero warnings and errors.
The source and launcher guard checks passed 125/125. The Client checks passed
228/228 after exercising an old option at the running command's argument
boundary. The Windows carried routed CLI suite passed 65 with seven tests
reserved for Linux PTY. The first formatter run found a resource request
initializer layout issue. The corrected whitespace check passed.

Build diagnostics initially identified a JSON array overload incompatible
with Native AOT and a missing test namespace. The correction uses a typed
JSON node and the existing Node key-store import. Independent review of the
exact post-cut head confirmed the released command registrations, original
receipt handling and test-only compatibility boundary.

## Installation completion recheck

H-22 selected the full required profile for e757129. Its installation package
checks passed 34 of 35, including the exact native Stop timeout, original
receipt reconciliation and the two installed positive CLI cases. The sole
failure was the completion test. Its launcher put the mandatory test-mode
flag after the line that System.CommandLine uses as the completion query.
The exact installed binary independently returned an empty suggestion list
with that order. The normal shell invocation and the test-mode flag before
the query both returned 36 suggestions including sandbox. Tasks, queue and
jobs were absent.

The Linux e757129 summary is
.git/arcforges-verify/logs/20261120-071918-e7571296e772-linux/summary.json
with SHA-256 3caa96f0b5c2c81dc54e79331c96cd7f92b197e966a379c1c53ad17e7aed3876.
The package log SHA-256 is
8525260502f3585dc14b1ed3eed57ce073a45df4e9833a489f406253b277a26a.
The package archive was retained in the corresponding launch directory with
SHA-256 57e2279ead10833b7dc0fecd057fe73277fcb87b3cf85f88eb672bf37f61733a.
The exact Windows e757129 run passed the CI and schema steps before it was
superseded during the AOT build phase. Its partial reporter and supersession
record remain in the matching launch directory.

The independently reviewed 3adb905a324eae76b29c9053273c00ee53b37d70 candidate
has tree 6cc53cd03d47d4f33f74d16227a105fcee02fe40. The one-line delta moves
the test-mode flag before the query. The full native profiles were restarted
from this exact head, preserving the test process guard and the same package
checks.

## Windows prior regressions at the corrected head

The first Windows package check for 3adb905 passed 33 of 35, including all
three new CLI cases, with zero skips. Two carried tests had source blobs
identical to the base. TerminalLoss exercised supervisor loss and verified the
old acknowledgment outcome. During teardown the Run revision changed between
Inspect and the guarded Stop. Node returned revision_mismatch before accepting
the cleanup request. The log establishes the conflict and leaves the new
Run revision and state unobserved.

The weighted CPU test reached the second initial Start before it launched
its planned unmanaged load. Core refused that request with budget_unavailable
and node_cpu_grant_unavailable. The test checked its native CPU sample before
creating the Sandboxes and starting the first Run. The second Start rechecked
the current sample and existing charge. The earlier log preserved the
refusal reason. The exact requested and available values for that observation
remain unknown.

The Windows 3adb905 first summary is
.git/arcforges-verify/logs/20261120-073555-3adb905a324e-win/summary.json
with SHA-256 3220e2d3a4d4b0df350370853a31715bdb30b2db6879d73f19dedac5554d9497.
The package log SHA-256 is
4bdf8e7efa374e0981f78677c0f3c123c5dc787b5a44a7cae4c596e6f44df91f.
The original archive was preserved with SHA-256
a3bf78422b83db556440311590f6fe7ae64fd5a7bcb10cb6fb2d8b625d949b37.

A focused recheck used that exact installed package, the same test assembly
and the matching native workload helper. It ran both terminal-loss cases
and the weighted CPU case serially. All three passed with zero skips.
The reduced native budget was 400 millicores. The two readbacks were 99
and 299 millicores, and the independent host probe took 35 milliseconds.
The focused log SHA-256 is
85baffd05091e392947c181d5f9583dd3bd11c84431578b493d144f12d57912b.
Windows restarted the full profile at the unchanged 3adb905 head.

## H-22 exact final profile

The native Linux host passed all 20 required checks at 3adb905 in 2498
seconds, including 35 installed cases with zero skips. The archived
installation contains the product and official runtime assets. The private
legacy CLI fixture is absent from that archive. The installed cases prove
the expected completion results, refusal of retired commands, signed-out
local management, original receipt recovery and genuine grant effects under
the isolated enrollment input.

| H-22 artifact | SHA-256 |
| --- | --- |
| 20261120-073520-3adb905a324e-linux/summary.json | 686d44d4ec26c2da1ed716a3f5bf6a4953b234e4158effdcdb66c2870eea27fa |
| linux-package.log | 9283efeae1bcbd66dfcc02a3b53b6afc3c2656b4e740d301653392c1d6d0b8ac |
| arcforges-linux-x64.tar.gz | 210a5bdfd37e3bc3a17341edbbb1b87ba5c645f55c617e83073cf5122ea86fb9 |
| Official MXC stage manifest | bafd7c2339f2388579cd125c70ef1338a2e80ae1043d04613ce5c2588c5b83f6 |

## Windows exact final profile

The full-profile retry at the same 3adb905 head passed all 15 required checks
in 2837 seconds, including 35 installed cases with zero skips. The package
check included the previously failed terminal and weighted CPU cases. The
preserved Windows archive excludes the private test client.

| Windows artifact | SHA-256 |
| --- | --- |
| 20261120-080212-3adb905a324e-win/summary.json | efa1a3e6564987b7d2a5b9bc1c9574a0502fd917e774e259f4670fd53a5a514f |
| 20261120-080212-3adb905a324e-win/win-package.log | f8bf8d4116d53ac668b217762e7abfcea7b3bd686259bf0fa5c2941c2c98e22a |
| arcforges-win-x64.zip | 0a78db580f76cbbada2f0ff51fcd090416b076060522be367a514e30cc3adb00 |
| Official MXC stage manifest | da9eca96d32a7bd476fdc0e503c915cb459e4ed6169facf525b5b07e12ff9102 |

Official subscription expiry remains unverified. ACC-01 already calls for the
installed local journey during subscription expiry. ACC-02 already calls for
the integrated official entitlement expiry case with the real Center and
Node. The installed proofs here cover signed-out local use and the explicitly
scoped existing enrollment fixture. Public activation is governed by PROD-01.

See [Node PR 109](https://github.com/ArcForges/ArcForges/pull/109),
[Plan PR 199](https://github.com/ArcForges/Plan/pull/199), and
[Plan PR 200](https://github.com/ArcForges/Plan/pull/200).
