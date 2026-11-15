# Codex handoff — ArcForges V2

## Current task — AFV2-BASE-01 active

Owner resumed BASE-01 on 2026-11-16. ENV remains complete; AR-13 stays PASS.
The owner clarified that the reconnect stop rule is **three consecutive failed
attempts in one outage**, reset by a successful reconnect. The previous
cumulative stop was the coordinator’s incorrect interpretation, not evidence of
a VPS failure. Its original ledger facts and draft checkpoint remain historical.
Windows work and native checks now use the current machine’s local directory
directly under the owner’s latest instruction. H-22 Linux still uses its MCP.

Current fetched main baselines: Plan 2b8b4809ae13a01ce7b9a665f4b5aea1777a98a6;
Design 4472ea5a110a3c15c8beeeed14627e44b37103d0;
ArcForges 200d2d25b1b40093c3af278993145a92bbf82a78;
Cloud d422d7718307f39903de49ee673105a3d0db6b9d;
Contracts 2b525ad3d79f404d705e4abe8c30bf4bf477d0a6.
All retained upgrade results and applied SQL remain unchanged. No deployment.

### Worktrees, heads and evidence

Windows product task worktrees are under each repository’s
.worktree/afv2-base-01-resume on task/afv2-base-01-resume.
The untouched original .worktree/afv2-base-01 drafts remain preserved.
Plan continuation is Plan/.worktree/afv2-base-01-continue on
plan/afv2-base-01-continue, based on actual remote checkpoint 2cff1b3.
Earlier local Plan resume worktree remains at 1dfcce7; its equivalent tree was
published as 2cff1b3 without resetting local work. Linux Plan primary’s dirty
history remains preserved; never use it as a clean task worktree.

| Repository | Candidate / PR | Actual evidence |
|---|---|---|
| ArcForges | 77459503f24df7fff6cb7c13908abed0f6692434 / PR85 | Node Windows author tests 12 OK (one Linux-only expected skip); Linux native fixtures 12/12, no skips; 107-entry module/subasset map |
| Cloud | e66c610e27d5ad0ba13a6487fb0a7b1b5d4d7f5d / PR158 | Real PostgreSQL inventory tests 8/8 at fdc1b282 (same Python source; later commits docs/provenance only); final full profiles running |
| Contracts | f173cf4124541f33b7b6366fe7b264733a0d6077 / PR139 | 5 temporary-Git tests; 10-repository committed input report: 215 references / 60 central declarations; final Linux full profile running |
| Plan | PR110, this continuation | Resume semantics and exact-path correction for mandatory provenance metadata; independent review/full native gates pending |

The module map covers all ArcForges/Cloud/Web/Contracts/DesktopPlatform projects
and 40 Go package/command roots, with owners/consumers/retirement gates. No V1
executor, applied SQL, published package or independent product was removed.
BASE-01’s Cloud/Contracts allowlists add only eng/provenance/files.json: their
existing mandatory provenance checks require classifying the new original
preflight files. No provenance validator/policy/reused record is changed.

Linux PostgreSQL test command was python eng/v2-migration/test_preflight.py in
Cloud/.worktree/afv2-base-01-resume at fdc1b2820e3efed5eedb9a30b18812b7ceb74997.
The prior uncertain background command never started: log/process probes were
absent. The direct bounded run completed all eight tests and removed its fixture.
This is inventory-fixture proof, not guarded CENTER-01 migration/authority or
schema11 deployment admission. All deployment reports remain unknown.

### Current checks and next action

Unchanged eng/verify.py run-and-report runs from independently fetched exact SHA
worktrees on each host. Windows local sessions: Cloud 23556, Node 66138.
Linux detached verification launch PIDs: Cloud old-head rerun 2696842,
Contracts final 2708140, Node final 2711473. Root logs are under
/home/sammiller/arcforges/logs/afv2-base01-*-verify*.txt; authoritative receipts
are each repository’s .git/arcforges-verify/logs/. Inspect summaries before
claiming a pass; these processes may have finished by the time of handoff.
Linux Node fixture log: logs/afv2-base01-node-fixtures.txt.

Cloud’s first full attempts failed because historical Go1.27.3 was not selected.
Use ARCFORGES_CTR06_BRIDGE_GO pointing at the preserved native dev/go/go1.27.3/go/bin/go
(or go.exe), while current Center remains Go1.27.4. Security producer needs the
existing ARCFORGES_CTR06_SECURITY_GO_ARCHIVE under
tmp/af-ctr-06-scratch/go1274-provision-<platform>-amd64-20261111/.
No install, PATH/global setting or verifier was changed. The unchanged native
bridge check passed after the selector correction. The old dce3615 Linux rerun
may still finish; final Cloud e66c610e requires its own new run.

Next: finish independent nonauthor review and required exact-head profiles,
fix actual failures only, and merge PR110’s bounded metadata scope correction
before product PRs. Check the final actual main/status/review identities. Then
record BASE-01 delivery/completion and all merge/publication results in a final
Plan checkpoint, with both Plan hosts bound to actual Design main. Do not start
another product task before BASE-01 completes. H-03 remains a later destructive
admission prerequisite, not a read-only code blocker. No current task is claimed
delivered/complete yet. Public activation still requires PROD-01 approval.

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
