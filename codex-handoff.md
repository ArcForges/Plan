# Codex handoff — ArcForges V2

## Current checkpoint — AFV2-BASE-01 complete

The owner resumed V2 implementation on 2026-11-16. This round delivered only
BASE-01, after ENV; no second product task started. ENV and AR-13 remain complete /
PASS. The graph now has two complete tasks and38 planned, none active. Stop this
round after the final Plan evidence PR; the next eligible task is BASE-02.

Plan baseline for this evidence is main246bb8d92c106202cb2e45123093db436c4ca2a7
(merged PR112). Design remains4472ea5a110a3c15c8beeeed14627e44b37103d0; no normative
Design change was required. This evidence branch is plan/afv2-base-01-complete in
Plan/.worktree/afv2-base-01-complete, [PR113](https://github.com/ArcForges/Plan/pull/113).
Its own exact-head Windows/Linux gates and merge remain mandatory before this
checkpoint reaches main; final receipts/statuses/review are linked on that PR.

### Delivered source and ordinary delivery

| Repository | Tested head | Actual merge / PR | Required native result |
|---|---|---|---|
| ArcForges | 2c4607cab05967fdd316ebfed5ffea4087fa3f13 | de361dbb189baa3ecfb1389fbaf682191d68766a / [85](https://github.com/ArcForges/ArcForges/pull/85) | Windows15/15, H-22 Linux20/20 |
| Cloud | a498b4c48e5d2e0a13ee10b14f9ae4426cb13b80 | f4708b36fd799025ad7d6fa9e5845e4558e492b3 / [158](https://github.com/ArcForges/Cloud/pull/158) | Windows10/10, H-22 Linux17/17 |
| Contracts | f173cf4124541f33b7b6366fe7b264733a0d6077 | 69f3041ab4c6bcee1677d0587aaebbbf54cb98bb / [139](https://github.com/ArcForges/Contracts/pull/139) | Required single H-22 Linux20/20 |

All product final heads passed independent nonauthor review by OpenAI Codex agent
/root/base_review. Its map-owner findings were repaired and delta reviewed. The
final Node change adds only exclusive/DisableParallelization attributes to one
existing timing-sensitive test; the method body and1s latency assertion remain.
Actual strict/no-bypass rules and final statuses were checked before each merge.

Contracts [ordinary CI43772758290](https://github.com/ArcForges/Contracts/actions/runs/43772758290)
succeeded, publishing17 NuGet packages, internal npm and Go tag1.0.0-ci.467.1.
Compatible existing consumer cohorts remain valid. Cloud [main CI43774372219](https://github.com/ArcForges/Cloud/actions/runs/43774372219)
completed skipped (all18 jobs) under unchanged migration guards: no deployment or
publication. Node has no main-push publication path; no merge-triggered run was
observed. Native verification packages below are local outputs, not a release.

### Acceptance and limits

Read-only preflights distinguish fresh, Node15, Center10/11 and unknown/newer;
source state is never migrated or initialized. Node holds native read protection
and inspects an in-memory SQLite snapshot without source sidecars. Center uses a
single read-only repeatable-read PostgreSQL transaction. Reports expose aggregate
metadata only. Unresolved/active/locked/unknown inputs remain fail-closed;
contraction is always denied. Optional binary hashes do not prove provenance,
and actual deployment/authority remain unknown.

The107-entry module/subasset map covers146 C# projects and40 Go roots, actual
owners/consumers and pinned-audit drift. The fixed-HEAD consumer snapshot covers
10 repositories,215 references and60 central declarations; SHA256
1b20e70b5a4c24e1758fdbf596f09b25e65ae8749e510fddfe6b10306950f8e8.
Independent products and shared DesktopPlatform ContentSandbox v1 are protected.
No executor, runtime route, applied SQL or published bytes were removed/rewritten.
Backup, drain, restore, cutover and rollback prerequisites and later owner tasks
are in ArcForges docs/v2-migration/README.md and the two companion tool READMEs.

Node author fixtures: Windows12 total, one expected Linux-only rename skip;
H-22 Linux12/12, no skips. Cloud H-22 PostgreSQL inventory8/8 used real disposable
PostgreSQL/source DDL and removed its fixture container. Contracts input tests5/5
use temporary Git repositories, not runtime doubles. Final native socket test1/1
on each host preceded full gates. PostgreSQL inventory fixtures do not prove the
guarded CENTER-01 upgrade, schema11 deployment or security/provider authority.
H-03 still gates later destructive admission, and AR-01..12 remain unqualified.
There was no production backup/restore/migration, deployment or public activation.

### Exact receipts and native artifact identities

Each host independently fetched the exact SHA from GitHub into an isolated
worktree and ran unchanged `python eng/verify.py run-and-report`. Full summaries
were read, every result ok=true. Receipts stay on their originating hosts under
<repo>/.git/arcforges-verify/logs/ (Windows roots C:/MyFile/Projects/ArcForges,
Linux roots /home/sammiller/arcforges):

- Node:20261116-075439-2c4607cab059-win (2215s),
  20261116-073919-2c4607cab059-linux (2004s), same tree
  31b85b3b8d1a15be615c9ca75f5a95fb133dc429.
- Cloud:20261116-071745-a498b4c48e5d-win and
  20261116-070913-a498b4c48e5d-linux, same tree
  a05ad1946fe380661186b25fa02f8f394ab2d830.
- Contracts:20261116-065050-f173cf412454-linux, tree
  2469c712dcd9dc5879306df054ee6521be8007fe.
- Prior Plan scope PR110: b5bc9953a7945e9cf9df54d510731e75406e4e3c,
  dual5/5, merge7da363a8b781d13903e8bab88e90f5e230a96e94;
  PR111:d90bcd79544c296b7ab61b5d9d87f1fa577cabc3, dual5/5,
  merge7c8aeea55f27c06763cf3eded2abbcb79099dbc9;
  PR112:01564acfe4bd14590fa0db948c1e9c229d26a730, dual5/5,
  receipts20261116-075030-01564acfe4bd-win/20261116-075023-01564acfe4bd-linux,
  merge246bb8d92c106202cb2e45123093db436c4ca2a7.
  All bind actual Design4472ea5a; no Design mutation or validator bypass.

Native Node host SHA256: Windows
1fa9838d3ab163cea2b02dc571fecf4df3db095e4a8d63ae1f9fec45e9b5aef8;
Linux2c8e988b54e6578b1bbe15d359302c6f6ffe28e68d08cdb17c2727e341f7911a.
Local package SHA256: Windows zip
8f4dc7dac090f032dce1f183a9e6e60854523dd7d9729acf188c867491e1d3b3;
Linux tar.gz c57f8272a17a95806124df72b3441a5b7bbc0fc189a44e35c65eefc9fa2812d0.
Paths are artifacts/publish/<rid>/host/arcforges[.exe] and
artifacts/packages/arcforges-desktop-<rid>.<zip|tar.gz> in the native verifier's
checkout (Windows ArcForges/.worktree/_verify, Linux
/home/sammiller/.cache/arcforges-verify/ArcForges).
Cloud local candidate0.1.0-local.1794784677743 image
sha256:b351e73fbb63fc368035244f25185ac1a196700a5a016400ff45205ba36fbfa2.

### Preserved work and exact next step

No BASE-01 verification process remains running. Prior Windows session85689 and
H-22 PID2852179 ended successfully. No Cloud/Contracts CI remains pending.
Windows product author worktrees <repo>/.worktree/afv2-base-01-resume remain on
task/afv2-base-01-resume at the tested heads above. Node and Cloud each have only
untracked eng/v2-migration/__pycache__/ generated by tests; Contracts is clean.
Untouched ArcForges/Cloud .worktree/afv2-base-01 still contain their original
untracked eng/v2-migration drafts. Cloud/.worktree/cloud-deploy-ci-python retains
its independent uncommitted eng/verification/test_ctr06_bridge_assets.py fix;
do not mix it into V2. Earlier Plan worktrees are preserved.
Linux Plan primary still has its pre-existing staged/unstaged historical edits
(including graph, ledger, policy, tooling and maintenance paths); do not reset or
reuse it for authoring. Use independent worktrees. No unrelated product changed.

The owner permits current-machine local Windows access in place of unstable
Windows MCP; designated H-22 Linux MCP is required. Three consecutive failed
reconnect attempts within one outage stop work; successful calls reset the count.
The earlier cumulative stop was a coordinator interpretation error. Subsequent
H-22 identity, fixture and full-profile calls succeeded. Transport failures alone
do not establish VPS failure. No network/proxy/security settings changed.
Windows verifier needs only process-local DOTNET_CLI_UI_LANGUAGE=en-US and
VSLANG=1033 so unchanged publish scripts can read English zero-warning summaries.
Cloud's existing bridge selectors remain in the ledger/previous checkpoint; no
tool installation or general toolchain upgrade was reopened.

Failure history remains append-only in ledger/ledger.jsonl: prior77459503
resource timeouts and48aac4ed CI timing failures were not reused as final proof.
The latter caused only the standing single-test isolation repair admitted by
PR112. Cloud's narrow public-digest scan exceptions bind exact receipt file and
two exact public key/value lines with positive/negative controls; no rule disabled.
Immutable r1 was retained and input-only r2 used; all131 package coordinates and
locks remain unchanged. Final normal scans and admission checks passed.

After final Plan PR113 merge, fetch latest main/Design and run
`python tools/plan.py next`: it returns AFV2-BASE-02. Read its full definition and
current allowed paths before starting; it is planned, not active. This round
stops at BASE-01 completion. Public rollout still requires PROD-01's separate
concrete approval. Historical sections below describe their dated stopping points
and do not override this checkpoint.

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
