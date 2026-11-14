# Codex handoff â€” ArcForges V2

Continue from current GitHub main and the ledger. The owner authorized the original 39 AFV2 tasks and subsequently added all-dependency upgrades with local/CI parity, explicitly requiring document review and merge first. Public activation still needs its separate concrete approval.

## Current authority and document order

Design #66 merged as `7952aa9fbf54613e8c1b078ead797b6f0444f7a7`; Plan #98 merged as `27fe4278d3b30b418619c4369860ddb573caace4` and start-record #99 as `f5fdaabd10a63a5b60d1dce903475b1be2d51b1a`. They established AD-0022/schema3 and the original implementation authorization. Do not redo that completed migration.

The documents-first amendment is complete: Design [#67](https://github.com/ArcForges/ArcForges-Design/pull/67) merged as `8241e59d97ae216d829b7ea0019c5b16dacafa96`, then Plan [#100](https://github.com/ArcForges/Plan/pull/100) as `32b397b975e90a6f1c7e62061dc6b072677b7cdf`. Both received independent review and full exact-head native Windows/Linux verification; the Plan summaries recorded that actual Design main. They add AD-0023, R-DEP-001 and AFV2-ENV-01. Plan [#101](https://github.com/ArcForges/Plan/pull/101), merged as `fca5c7c2aa918cecab684898e46d18a764966080`, records ENV active. Do not repeat the document stage or restart the task.

## Authorized next work

The graph has 40 tasks and AFV2-ENV-01 is active. The original 39-ID authorization remains in the ledger; the added ENV authorization is recorded separately. Read AGENTS, execution-policy, delivery-procedure, acceptance-register and each complete task record. Continue ENV, then use `python tools/plan.py next` to resume eligible tasks serially. BASE-01 and MXC-01 both depend on the upgrade. Keep isolated task worktrees, independent nonauthor review and every required native profile; never bypass statuses, hooks, protections or failed safety checks.

ENV covers ArcForges, Cloud, Web, Contracts, shared DesktopPlatform, ArcForges-Design and Plan: all current tools/runtimes/SDKs, Actions/images, direct business dependencies and resolved transitive dependencies. Check latest upstream stable versions during implementation, pin exact identities and make local/CI resolution match. Include major upgrades and necessary compatibility repairs. Preserve immutable historical artifacts, published versions and applied SQL. Independent Mobile/AI/ArcScope/ArcSlate/ArcNotes are protected consumers, outside blanket upgrade scope. Public deployment/activation is not part of ENV.

## ENV implementation checkpoint

Two tooling slices have merged; **ENV is not delivered or complete**:

| Repository | PR / final tested head | Merge | Required native evidence |
|---|---|---|---|
| ArcForges-Design | [#68](https://github.com/ArcForges/ArcForges-Design/pull/68), `c32f428418c54d01a3611bf5e3e902cf08909996` | `1a46a08e525b073afd86ff8c046f9b09a691eb1b` | Windows 4/4, Linux 5/5; full receipts `20261114-232318-c32f428418c5-win` / `20261114-232318-c32f428418c5-linux` |
| Plan | [#102](https://github.com/ArcForges/Plan/pull/102), `0f0c1f2de895c97f2b8793e9fa2737b1e222f9d8` | `fcac9fd47fe7bed278ed8f170dbaa7ec30e6a85d` | Windows 5/5, Linux 6/6; full receipts `20261114-233007-0f0c1f2de895-win` / `20261114-233006-0f0c1f2de895-linux` |

Both final heads received independent nonauthor review. Plan's two summaries record Design main `1a46a08e525b073afd86ff8c046f9b09a691eb1b`, rechecked against GitHub before merge. Each receipt remains under its own host's repository `.git/arcforges-verify/logs/`; none was transferred between hosts. Hosted PR workflows were skipped under the configured owner policy. See each repository's `docs/dependency-upgrade/current.json` for exact admitted pins and sources. Design now binds protoc/plugin/includes to its restored lock; both repositories reject invoking/PATH Python mismatches, and Design also checks selected SDK/MSBuild roots. The actionlint configuration adds only the official Ubuntu 26.04 label absent from stable actionlint's vocabulary.

Continue with the shared producers. DesktopPlatform's published Build.Policy currently restricts consumers to C# 14; a narrow compatibility bootstrap is being prepared in `DesktopPlatform/.worktree/afv2-env-01` on `task/afv2-env-01`. It must retain existing consumers while admitting C# 15 with a suitable SDK. It still requires ordinary complete DesktopPlatform native gates, independent review, main merge and publication of the normal full package cohort. There is no standalone unverified policy-package publication route. Then upgrade Contracts, finish DesktopPlatform's managed/native closure, and admit their exact new cohorts into ArcForges, Cloud and Web. Remaining five repository worktrees are `.worktree/afv2-env-01`; no unmerged implementation is accepted by this checkpoint.

The Windows scratch inventory is `C:/MyFile/Projects/ArcForges/tmp/afv2-env-01/inventory.json` with `inventory-summary.md`. It inventories source and locks, including historical references; it does not prove every row is current or upgraded. Official-registry observations are a separate scratch research step, not dependency admission. Review actual restored closures, successor major module paths, licences/provenance, current native profiles and protected consumers. Preserve old native receipts and bridge identities; do not refresh their hashes to disguise a new toolchain.

Authorized side-by-side tool installs exist under `C:/MyFile/Projects/dev/arcforges-toolchains/` and `/home/sammiller/.local/share/arcforges/toolchains/` (Python 3.15.2, Node 26.13.1, npm 12.2.2, uv 0.13.8). Windows Design verification selected SDK 11.0.100 from the existing Scoop SDK root and removed only the conflicting process-local `MSBuildSDKsPath`; the user's older `.dotnet` SDKs remain. Linux `.dotnet` now also contains SDK 11.0.100 while retaining older SDKs, and `~/.local/bin/python` selects the installed 3.15.2. Install/source hashes and the prior Linux Python selection are recorded in each host's own `tmp/afv2-env-01/` receipts. No proxy/security settings were changed. Remaining repository/tool selections still need migration and verification; these installs are not evidence of complete local/CI parity across all seven repositories.

Clean Windows Plan/Design primaries and Linux Design were fast-forwarded to these merges. The pre-existing dirty Linux Plan primary was preserved; use fresh verification/task worktrees there.

## Preserved BASE-01 checkpoint

BASE-01 is parked planned, not delivered. Preserve these uncommitted files on Windows under `C:/MyFile/Projects/ArcForges/`:

- `ArcForges/.worktree/afv2-base-01/eng/v2-migration/preflight.py` and `test_preflight.py`; base `10f692224f94916cfc93fbad971f80ec340c5edf`.
- `Cloud/.worktree/afv2-base-01/eng/v2-migration/preflight.py`; base `6df33c525fcbc20495e46c9c4c011086146da796`.
- `Contracts/.worktree/afv2-base-01` remains unmodified at `de3dba76266e89654be9b4d29d097d525a281c6a`.

The earlier Node author diagnostic had 11 tests OK with one Windows condition skipped; the latest protected-fd/in-memory SQLite snapshot and failure-classification changes are untested. Cloud is an untested draft. Consumer scanning, module map, documentation and PostgreSQL fixtures remain unfinished. No product commit, PR or native acceptance exists for this checkpoint. After ENV, reconcile these worktrees with actual upgraded main and run affected checks; do not count the old author diagnostic as current acceptance.

## Product and acceptance boundaries

Deliver the general CLI Sandbox/Run platform with official stable MXC, genuine terminals, preserved intelligent resource management, private persistent data, free offline local CLI, optional free self-hosted Go Center and Blazor management. Only official hosted access is subscription-gated. No product MCP/AI/Task DAG/cache platform/desktop or mobile client; never copy/fork MXC or silently use an uncontained process.

Both composed native profiles need real P1 qualification before executor replacement. Changed upstream versions require relevant source/artifact requalification; dated research is not a new runtime pass. Preserve Node schema15 and Center schema10/11 safeguards and unresolved effects. H-03 blocks destructive admission, not read-only preflight code. Prices/provider/legal/domain settings remain owner inputs, and AFV2-PROD-01 needs separate explicit outward-facing activation approval.

Use the Windows MCP at `C:/MyFile/Projects/ArcForges/` and H-22 Linux MCP at `/home/sammiller/arcforges/`. Fetch independently from GitHub; never substitute WSL/SSH/scratch or transfer verification receipts. Preserve existing dirty primary checkouts. Record exact heads, worktrees and unfinished steps on interruption. Report in Simplified Chinese and continue only within the authorized graph.
