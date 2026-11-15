# Codex handoff — ArcForges V2

## Current checkpoint — BASE-01 resumed, stopped on host transport failures

The owner resumed the existing V2 authorization on 2026-11-16 (Asia/Shanghai).
This round works only on AFV2-BASE-01. ENV remains complete and AR-13 PASS;
BASE-01 is now **blocked by H-02**, with 38 other product tasks still planned.
The prior upgrade-round stop below is historical and was superseded by this
resumption. No product task is delivered by this checkpoint.

Baselines fetched from GitHub: Plan `2b8b4809ae13a01ce7b9a665f4b5aea1777a98a6`,
Design `4472ea5a110a3c15c8beeeed14627e44b37103d0`,
ArcForges `200d2d25b1b40093c3af278993145a92bbf82a78`,
Cloud `d422d7718307f39903de49ee673105a3d0db6b9d`,
Contracts `2b525ad3d79f404d705e4abe8c30bf4bf477d0a6`.

Both designated MCP hosts executed real identity/workspace/tool probes. Windows
was DEKU / deku\\j7rdm / Windows 10.0.26300, workspace
`C:/MyFile/Projects/ArcForges`; Linux was v2202601329473427941 / sammiller /
Debian kernel 6.12.63+deb13-amd64, `/home/sammiller/arcforges`, with a running user
manager and cgroup2fs. These probes are not required verification statuses.
Linux Plan primary's existing dirty staged/unstaged history was preserved.

Three Linux MCP shell invocations returned transport send/HTTP errors for
`https://linux-mcp.arcforges.com/mcp`, interspersed with successful reconnects.
After the third error the coordinator stopped under the owner's explicit
three-failure rule. No further native invocation is permitted in this stopped
round. Windows Git HTTPS also reported intermittent schannel handshake failures;
no network/TLS/proxy/security setting was changed.

### Saved work and exact identities

All Windows task worktrees are `<workspace>/<repo>/.worktree/afv2-base-01-resume`,
branch `task/afv2-base-01-resume` (Plan uses `plan/afv2-base-01-resume`). Original
parked `.worktree/afv2-base-01` drafts were copied, never reset or overwritten.

| Repository | Commit / remote state | Contents |
|---|---|---|
| ArcForges | local `6f6436db7ddd4df6211c539870959e779cafafc6`; HTTPS push failed | Read-only Node preflight, 12 tests, operator/backup/cutover/rollback instructions |
| Cloud | pushed `dce36152a21e19cb64b94b8837b21bfc9f63200f`; [draft PR158](https://github.com/ArcForges/Cloud/pull/158) | Read-only PG preflight, real disposable PostgreSQL test script, use/evidence boundaries |
| Contracts | local `9fd2b8e384198db983f7b9e230614cd070f93474`; HTTPS push failed | Committed-input consumer scanner, 5 tests, instructions, `observed-20261116.json` |
| Plan | this checkpoint branch; exact publication identity in its PR | Authorization, active→blocked facts, generated sequence and this handoff |

Author diagnostic `python -m unittest discover -s eng/v2-migration -v` in the
Windows ArcForges task worktree: 12 tests, OK, 1 expected Linux-only rename skip.
It exercised real temporary SQLite files/locks/WAL/unknown-journal cases; this is
not MCP `run-and-report` evidence. The draft's source-size bound now precedes
hashing; schema drift is unknown. Contracts' 5 temporary-Git tests passed; actual
10-repository scan observed 215 references and 60 central declarations, with exact
HEADs/input hashes and independent/shared consumers protected. It does not
evaluate conditional MSBuild or prove installations/runtime compatibility.
Cloud scripts passed syntax compilation only. No PostgreSQL result was observed.

Linux independently fetched Cloud `fdc1b2820e3efed5eedb9a30b18812b7ceb74997`
(parent of documentation head) into
`/home/sammiller/arcforges/Cloud/.worktree/afv2-base-01-resume`.
The attempted background command was
`nohup python eng/v2-migration/test_preflight.py > /home/sammiller/arcforges/logs/afv2-base-01-pg.txt 2>&1 < /dev/null &`.
Its transport failed; **whether it started is unknown**. On resume inspect that
log and only the owned `eng/v2-migration/test_preflight.py` process/container
(`arcforges-center-v2-preflight-*`) before restarting. Never kill unrelated
processes/containers. No formal host profile or CI was deliberately started.
No required status, independent final review, merge, publication, migration or
deployment is claimed. Cloud draft PR hosted skips are not acceptance.

Untracked `eng/v2-migration/__pycache__/` may exist in both Windows product
worktrees; these are Python author-check artifacts, excluded from commits.
The per-module machine-readable disposition map was not completed before stop.
No Design file was changed; its pinned historical audit remains unchanged.

### Next action on a later authorized resume

1. Recheck designated MCP connectivity (same three-failure stop rule), inspect
   uncertain PG process/log, fetch actual main and compare the saved exact heads.
2. Publish the preserved Node/Contracts commits if still local; retain any
   supplemental connector-publication identities recorded with this checkpoint.
3. Complete the source-pinned per-module disposition/owner/consumer map within
   ArcForges `docs/v2-migration/**`, reconciling upgraded main with the immutable
   Design audit. Do not widen retirement or edit applied SQL.
4. Run Windows and Linux Node fixtures and Linux PostgreSQL fixtures; fix actual
   failures, obtain independent nonauthor full-final-head review, then exact
   pushed-head required profiles through each designated MCP. None has run yet.
5. Merge only when every BASE-01 item and required repository gate is met;
   record actual merges/evidence through plan.py and Plan native checks. H-03
   still blocks later destructive admission, not read-only preflight code.

## Prior completed upgrade round — historical stopping point

**ENV is complete, AR-13 is PASS, and the original 39 tasks remain planned.**
This upgrade round is finished; do not start BASE-01, MXC-01
or another task. The original authorization remains in the ledger for a later
resumed round. Public activation retains its separate explicit approval.

Current authority is AD-0022/schema3 and the owner's AD-0023 clarification merged
through [Design #71](https://github.com/ArcForges/ArcForges-Design/pull/71) and
[Plan #108](https://github.com/ArcForges/Plan/pull/108). Preserve completed upgrades
and finish necessary .NET/C#, Go, TypeScript and supporting tools with local/CI
parity. Compatible locked dependencies and published producer cohorts may remain.
Keep normal build/test/AOT/analyzer/security/provenance and required native gates;
do not restart per-dependency freshness research, special upstream-metadata/tag
qualification, additional per-version approval or the optional broader native r5.
Independent Mobile/AI/ArcScope/ArcSlate/ArcNotes remain protected consumers.

## Completed ENV delivery

All seven repositories are delivered. Cloud [#157](https://github.com/ArcForges/Cloud/pull/157)
merged as `d422d7718307f39903de49ee673105a3d0db6b9d` after Windows 10/10 and Linux 18/18
at `7d2d18b6e29157df98b5a63dbb6efe2977f6c632`. Its
[main CI run](https://github.com/ArcForges/Cloud/actions/runs/43706393820) completed as `skipped` under the pre-existing guards. All 18 hosted jobs were skipped: ordinary main-push candidates and deployment were already disabled before ENV. No publication or deployment was attempted. The required native Linux profile built and verified candidate 0.1.0-local.1794739798362 (image sha256:aeb1e68ce06a1a119f0f61ae44c7a29e8fc312c9a3bbdbc0473d664f6f95edfe). Both Cloud primary checkouts were fast-forwarded to the merge.

The [ENV summary](docs/dependency-upgrade/afv2-env-01-summary.md) is the single
table of tested heads, merges, required totals and publication links. In particular:

- [ArcForges #84](https://github.com/ArcForges/ArcForges/pull/84) merged
  `200d2d25b1b40093c3af278993145a92bbf82a78` after Windows 15/15 and Linux 21/21
  at `136670a04d34bb45822fa2908229190d25f479ae`; there is no main-push publication.
- [Contracts #138](https://github.com/ArcForges/Contracts/pull/138) merged
  `2b525ad3d79f404d705e4abe8c30bf4bf477d0a6` after its required single Linux 21/21.
  Ordinary [run463](https://github.com/ArcForges/Contracts/actions/runs/43699575709)
  published 17 NuGet packages, internal npm and the Go tag at `1.0.0-ci.463.1`;
  Go proxy/sumdb resolution succeeded. Compatible consumers may retain 450.1.
- DesktopPlatform's [ordinary publication](https://github.com/ArcForges/DesktopPlatform/actions/runs/43693457102)
  completed all 29 jobs and 21 NuGet packages at `1.0.0-ci.151.1`; compatible 150.1 remains valid.
- Web's [final CI/delivery](https://github.com/ArcForges/Web/actions/runs/43694865856)
  succeeded at merge `69be85d95ea412cc027597ffd0d990bf0e28e50f`, recording
  `web-0.1.0-ci.186.1`; `No targets deployed for arcforges-web` keeps public targets unmounted.

The coordinator recorded ENV delivered then complete through `plan.py` and
closed AR-13 with actual evidence. This state/evidence record retains the required
Plan Windows/Linux checks against actual Design main. Preserve the pre-existing
dirty Linux Plan primary and use isolated worktrees.

## Tool selection and preserved host work

Selected necessary versions are SDK 11.0.100 / C# 15, Go 1.27.4, TypeScript 7.0.2,
Node 26.13.1 / npm 12.2.2 and Python 3.15.2 where used. The
[selection table](docs/dependency-upgrade/afv2-env-01-summary.md#selected-language-tools-and-localci-selection)
records actual local roots and committed CI selectors. The new Windows MCP
default shell was measured at these executable versions; Linux `.profile`
selection was completed earlier. Windows User PATH/profile selection uses
`C:/MyFile/Projects/dev/arcforges-toolchains/activate-language-tools.ps1`, retains
Scoop 11 `DOTNET_ROOT` and removes the fixed User `MSBuildSDKsPath` override.
User environment backup is `tmp/afv2-env-01/windows-language-selection-backup/user-environment.json`.
Machine environment, execution/security policy and old installations were unchanged.

Visual Studio 18.12 installation completed with exit 3010; do not reboot in this round.
Private LLVM 23.1.5 / GNU 2.47 (actual banner 2.47.20260726) and their receipts remain.
The optional broader native r5 WIP in `DesktopPlatform/.worktree/afv2-env-01-native`
is preserved unchanged, not an outstanding mainstream-toolchain requirement.
Earlier OOM/ENOSPC recovery removed only 172 temporary Cloud sealed-tool copies
(20.310 GiB), preserved archives/evidence/logs, and restarted the existing user
manager without configuration changes. It is history, not a current profile pass.

Earlier tooling/managed slices and failed-candidate investigations remain in Git,
the [ledger](ledger/ledger.jsonl), linked PRs and each host's own
`.git/arcforges-verify/logs/`. For example, the
[old bootstrap publication failure](https://github.com/ArcForges/DesktopPlatform/actions/runs/43615837618)
and later [150.1 publication](https://github.com/ArcForges/DesktopPlatform/actions/runs/43678526078)
retain their original outcomes. Do not rerun them or rewrite historical receipts.

## Preserved BASE-01 checkpoint

BASE-01 is parked planned, not delivered. Preserve these uncommitted files on Windows under `C:/MyFile/Projects/ArcForges/`:

- `ArcForges/.worktree/afv2-base-01/eng/v2-migration/preflight.py` and `test_preflight.py`; base `10f692224f94916cfc93fbad971f80ec340c5edf`.
- `Cloud/.worktree/afv2-base-01/eng/v2-migration/preflight.py`; base `6df33c525fcbc20495e46c9c4c011086146da796`.
- `Contracts/.worktree/afv2-base-01` remains unmodified at `de3dba76266e89654be9b4d29d097d525a281c6a`.

The earlier Node author diagnostic had 11 tests OK with one Windows condition skipped; the latest protected-fd/in-memory SQLite snapshot and failure-classification changes are untested. Cloud is an untested draft. Consumer scanning, module map, documentation and PostgreSQL fixtures remain unfinished. No product commit, PR or native acceptance exists for this checkpoint. On a later resumed BASE-01 round, reconcile these worktrees with actual upgraded main and run affected checks; do not count the old author diagnostic as current acceptance.

## Product and verification boundaries

The subsequent product remains the general CLI Sandbox/Run platform with official
stable MXC, real terminals/resources/data safety, free offline local CLI, optional
self-hosted Go Center/Blazor management, and subscription-gated official hosting.
No product MCP/AI/Task-DAG/cache platform or desktop/mobile client is introduced.
Preserve Node schema 15 and Center schema 10/11 guards; mandatory composed P1/runtime
qualification and destructive-migration prerequisites remain future task work.

Use native Windows MCP at `C:/MyFile/Projects/ArcForges/` and H-22 Linux MCP at
`/home/sammiller/arcforges/`; fetch exact candidates independently. Never use
substitute hosts, copied receipts, bypasses or network/security changes. Report in
Simplified Chinese. This round is complete; resume product work only in a later round.
