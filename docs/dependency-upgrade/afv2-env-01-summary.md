<!-- SPDX-License-Identifier: Apache-2.0 -->
# AFV2-ENV-01 completion

**ENV is complete; AR-13 is PASS; all original 39 tasks remain planned.**
All seven repositories have completed the necessary toolchain upgrade and
applicable native verification, merge and ordinary delivery recorded below.
This round ends with this completion record.

Scope: retain completed upgrades and finish necessary .NET/C#, Go, TypeScript
and supporting toolchains with applicable local/CI parity. Keep normal locked
build/test/AOT/analyzer/security/source checks. Compatible existing dependencies
and producer cohorts may remain; no new transitive-version research, special
upstream-tag qualification or per-version approval loop is required.

## Repository records

| Repository | PR | Tested / candidate head | Merge | Required native result |
|---|---|---|---|---|
| ArcForges-Design | [71](https://github.com/ArcForges/ArcForges-Design/pull/71) | `4e80ab88f0fe2894213b61d05bda981acbf8aa8a` | `4472ea5a110a3c15c8beeeed14627e44b37103d0` | Windows 4/4; Linux 4/4 |
| Plan | [108](https://github.com/ArcForges/Plan/pull/108) | `108949da73493213782dc9a7c9825ce1aaa9af61` | `557cfc12861a0778f41e7be25a151efce43105cc` | Windows 5/5; Linux 5/5 |
| DesktopPlatform | [217](https://github.com/ArcForges/DesktopPlatform/pull/217) | `40762012e530e76eeb16d9fa31c043b32631f061` | `6e109ef5d01855158c7ae3a63cd42c98db2647f3` | Windows 18/18; Linux 25/25 |
| Web | [59](https://github.com/ArcForges/Web/pull/59) | `8eddb2e74cd23044db381af49eb3fe4bb22dd45a` | `69be85d95ea412cc027597ffd0d990bf0e28e50f` | Windows 12/12; Linux 17/17 |
| Contracts | [138](https://github.com/ArcForges/Contracts/pull/138) | `db455a51630667413fb363cba9f439376442a7a4` | `2b525ad3d79f404d705e4abe8c30bf4bf477d0a6` | Required single Linux profile 21/21 |
| ArcForges | [84](https://github.com/ArcForges/ArcForges/pull/84) | `136670a04d34bb45822fa2908229190d25f479ae` | `200d2d25b1b40093c3af278993145a92bbf82a78` | Windows 15/15; Linux 21/21 |
| Cloud | [157](https://github.com/ArcForges/Cloud/pull/157) | `7d2d18b6e29157df98b5a63dbb6efe2977f6c632` | `d422d7718307f39903de49ee673105a3d0db6b9d` | Windows 10/10; Linux 18/18 |

Cloud #157 passed at `7d2d18b6e29157df98b5a63dbb6efe2977f6c632`, tree
`25acb398c655d2b1d4e91ea39ccb23daa3470aec`. Receipts are
`20261115-184205-7d2d18b6e291-win` and `20261115-184203-7d2d18b6e291-linux`.
Both required statuses succeeded before merge.

ArcForges #84's tree is `572dbbe7298a8345e3b7b8ff97201a52d88930ee`; receipts are
`20261115-171816-136670a04d34-win` and `20261115-173443-136670a04d34-linux`.
Both primary checkouts were fast-forwarded. No main-push publication applies.
Contracts' tree is `61cef44cad40c8aeda87330f5a2783349693b594`, with required receipt
`20261115-172040-db455a516306-linux`; both primaries were fast-forwarded.

## Ordinary publication and delivery

- DesktopPlatform [run 43693457102](https://github.com/ArcForges/DesktopPlatform/actions/runs/43693457102)
  passed all 29 jobs and published all 21 NuGet packages at `1.0.0-ci.151.1`.
- Contracts [run 43699575709](https://github.com/ArcForges/Contracts/actions/runs/43699575709)
  at its recorded merge succeeded for candidate, NuGet, npm and Go tag publication.
  Security/Verify were skipped under their original conditions. Logs confirm 17
  NuGet packages and `@arcforges/ai-internal` at `1.0.0-ci.463.1`; tag
  `go/v1.0.0-ci.463.1` was created on that merge and resolved through Go proxy and
  sumdb on the first attempt. Compatible consumers may retain 450.1; likewise the
  earlier DesktopPlatform 150.1 cohort remains valid when compatible.
- Web [run 43694865856](https://github.com/ArcForges/Web/actions/runs/43694865856)
  succeeded for candidate and existing guarded main-push delivery, recording
  `web-0.1.0-ci.186.1`, Version ID `95d6ff5a-fd2c-4e74-8794-77486d6e722c` and
  `No targets deployed for arcforges-web`. Public targets remain unmounted.
  Earlier [Web #57](https://github.com/ArcForges/Web/pull/57) is preserved history;
  #59 is the final accepted npm CI repair. Both Web primaries were fast-forwarded.

- Cloud [run 43706393820](https://github.com/ArcForges/Cloud/actions/runs/43706393820) at merge `d422d7718307f39903de49ee673105a3d0db6b9d`
  completed with conclusion `skipped` under its pre-existing guards. All 18 hosted jobs were skipped: ordinary main-push candidates and deployment were already disabled before ENV. No publication or deployment was attempted. The required native Linux profile built and verified candidate 0.1.0-local.1794739798362 (image sha256:aeb1e68ce06a1a119f0f61ae44c7a29e8fc312c9a3bbdbc0473d664f6f95edfe). Both Cloud primary checkouts were fast-forwarded to the merge.

## Selected language tools and local/CI selection

This table reuses existing selected versions and verified local roots. This
documentation edit performed no upstream-version search or host probe; the
coordinator's actual new default-shell result is recorded below. Apply each tool
only where the repository uses it; historical fixtures keep their recorded pins.

| Tool | Selected version | Current Windows MCP shell selection | Previously recorded H-22 selection | Committed CI selection |
|---|---|---|---|---|
| .NET / C# | SDK `11.0.100`, current projects C# `15` | `C:/Users/J7Rdm/scoop/apps/dotnet-sdk/current/dotnet.exe`; SDK/MSBuild roots verified against `global.json` | `/home/sammiller/.local/share/arcforges/toolchains/dotnet-11.0.100`; explicit `DOTNET_ROOT` and child selection | `actions/setup-dotnet` uses `global.json`; current `Directory.Build.props` selects C# 15 / net11 where applicable |
| Go | `1.27.4` | `C:/MyFile/Projects/dev/go/go1.27.4/go/bin/go.exe` | `/home/sammiller/dev/go/go1.27.4/go/bin/go` | Current `go/toolchain.json` / `center/toolchain.json` and `actions/setup-go` `1.27.4`, or the repository's existing pinned installer; local execution uses `GOTOOLCHAIN=local` |
| TypeScript | `7.0.2` | Repository-local `node_modules/typescript/bin/tsc`, restored from `package-lock.json` | Same repository-local locked CLI for the platform | Exact `typescript: 7.0.2` declaration and lock; `npm ci --ignore-scripts` selects the repository CLI |
| Node / npm | `26.13.1` / `12.2.2` | `C:/MyFile/Projects/dev/arcforges-toolchains/node-v26.13.1-win-x64`; npm in that Node installation | `/home/sammiller/.local/share/arcforges/toolchains/node-v26.13.1-linux-x64`; npm in that Node installation | `actions/setup-node` reads `.node-version`; current workflows install and verify npm 12.2.2 inside the selected Node prefix before `npm ci` |
| Python | `3.15.2` | `C:/MyFile/Projects/dev/arcforges-toolchains/python/cpython-3.15.2-windows-x86_64-none/python.exe` | `/home/sammiller/.local/bin/python` selects the managed 3.15.2 installation under `/home/sammiller/.local/share/arcforges/toolchains/python/` | `actions/setup-python` reads `.python-version`; invoking and PATH interpreters are checked by `eng/check_toolchain.py` |

The coordinator completed Windows User-level default selection while preserving
the old installations. The original MCP process still had SDK 10.0.403,
Node 26.13.0/npm 12.0.2, Python 3.14.7 and no Go. Four existing language roots
were prepended to User PATH, Scoop 11 `DOTNET_ROOT` retained, and the fixed User
`MSBuildSDKsPath` override removed. Both Windows PowerShell and PowerShell
`CurrentUserAllHosts` profiles only dot-source
`C:/MyFile/Projects/dev/arcforges-toolchains/activate-language-tools.ps1`.
The new MCP default shell was actually tested at SDK 11.0.100, Go 1.27.4,
Node 26.13.1, npm 12.2.2 and Python 3.15.2. Backup:
`tmp/afv2-env-01/windows-language-selection-backup/user-environment.json`.
Machine environment, execution/security policy and old installations were not
changed. Linux `.profile` selection had already been completed. This host
selection is supported by the completed repository profiles recorded above.

Existing source records include the [Cloud selection inventory](https://github.com/ArcForges/Cloud/blob/d422d7718307f39903de49ee673105a3d0db6b9d/docs/dependency-upgrade/afv2-env-01-current.json),
[Web inventory](https://github.com/ArcForges/Web/blob/69be85d95ea412cc027597ffd0d990bf0e28e50f/docs/dependency-upgrade/current.json)
and [Plan's own Python/CI inventory](current.json). Host-local preflight and formal
profile records retain actual executable/SDK roots and lock fingerprints. Current
hosted runner labels are explicit venues (including Ubuntu 26.04 and Windows 2025);
H-22's native OS is a separate venue. Matching tools does not claim identical OSes.

## Preserved recovery and deferred work

Earlier H-22 OOM/ENOSPC interrupted verification. Only 172 temporary Cloud
`artifacts/sealed-tool-*` extracted copies were removed, freeing 20.310 GiB;
archives, evidence and logs were preserved. The existing `user@1000` service was
started and restored `cpu`/`memory`/`pids` without configuration changes.
Subsequent completed results are the exact receipts above; recovery or partial
attempts do not count as profile success.

Visual Studio 18.12 installation completed with exit 3010; reboot remains pending
and is not performed in this round. Installed LLVM/GNU and their historical
receipts remain. The optional broader native r5 worktree is parked unchanged,
not extra completion work. BASE-01 WIP remains preserved in the
[handoff](../../codex-handoff.md#preserved-base-01-checkpoint).

The coordinator recorded all repository PRs, merges and ordinary publication
through `plan.py`, closed AR-13, and recorded ENV delivered then complete.
The original 39 tasks remain planned; BASE-01 and optional native WIP are preserved.
This round stops here.
