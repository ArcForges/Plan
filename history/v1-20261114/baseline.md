# Baseline (2026-10-12)

The state the flagship plan starts from. Tasks pin or build on these. A task that finds a different state records the difference in its PR before relying on it.

## 1. Repositories (main heads)

| Repository | Head | Notes |
|---|---|---|
| ArcForges/ArcForges | `966f062` | Initial commit (AGPL-3.0 licence only). AF-REPO-01 creates the structure. |
| ArcForges/ArcForges-Design | (this planning PR) | Design authority |
| ArcForges/Plan | (this planning PR) | Plan authority |
| ArcForges/Contracts | `b774c322` | Latest published cohort **1.0.0-ci.370.1** (from `b774c322`; CON.43) |
| ArcForges/DesktopPlatform | `60309ec9` | Latest published cohort **1.0.0-ci.133.1** (PLT.45/PLT.33, DP #178) |
| ArcForges/Cloud | `92ba1dc9` | CLOUD.72 deployed (deploy run 38102843509) |
| ArcForges/Web | `dd0a5de3` | Deployed 0.1.0-ci.119.1 (PRF.11) |
| ArcForges/Mobile | `6702e281` | MAUI foundation (AND.40) |
| ArcForges/ArcScope | `485c8d6d` | Retained; pre-release 0.1.0-ci.68.1 |
| ArcForges/ArcSlate, ArcNotes | `569785a`, `2839da6` | Retained |
| ArcForges/AI | `70f8b22` | Read-only history |
| ArcForges-Design-Parallel, Plan-Parallel | `64173614`, `5ccbb392` | Frozen history ([legacy-disposition](history/legacy-disposition.md)) |

## 2. Never admit

- Contracts `1.0.0-ci.350.1` and DesktopPlatform Build.Policy `1.0.0-ci.124.1` (rolled back).
- Any first-party version whose publishing commit is not an ancestor of its producer's main.

## 3. Workstation

From ArcForges-Design `docs/verification/platform-capabilities.md`.

| Item | Value |
|---|---|
| Windows | Windows 11 Pro for Workstations build 26300; 18 logical processors (hybrid); 31.5 GB RAM (L-01) |
| WSL | WSL 3.0.1.0, kernel 6.18, Debian 13 with systemd 257, cgroup v2, user manager delegation of cpu, memory and pids (L-02..L-07). Transient user units proven (L-13). Mirrored networking (L-12). Dated workstation facts: since 2026-10-21 WSL Debian is no longer the Linux verification venue (ArcForges-Design AD-0018 §5). |
| .NET | SDK 10.0.401 (Windows); 10.0.400 under `~/.dotnet` in WSL (not on PATH; dated, see the WSL row) |
| Python | 3.14.7 |
| Node | 24.21.0, npm 11.19.0 (repositories that use them) |
| protoc | Grpc.Tools 2.84.0 (NuGet cache) |
| Tools on Windows | Rust (rustup), CMake, Ninja, sccache, Node LTS, git, gh, winget, Scoop; Visual Studio 18 instance (no `cl.exe` on PATH); no ccache or FASTBuild (L-10) |
| Tools in WSL | gcc, g++, clang, git, Docker CLI, npm, Python 3. No cargo, CMake, Ninja, sccache, ccache or Avahi (L-11); dated, see the WSL row. |
| Linux verification venue | The Linux MCP host, through the Linux MCP server (ArcForges-Design AD-0019; H-22, not provisioned yet). Never local WSL, and no agent's own sandbox; until H-22 no Linux leg can be recorded (AD-0019 §8), so no `arcforges/linux` status can be reported and no PR can merge (AD-0020). *Dated (AD-0018, kept as history):* the Claude Code Cloud Linux environment, an Ubuntu 24.04 container with .NET SDK 10.0.401 from the Microsoft SDK image and Docker; it has no systemd user manager, so it ran the portable checks only. Real-OS Linux tests (systemd units, cgroups) need the Linux MCP host; installs on it are the user's (H-11). |

## 4. Accounts and access

Existing access only. npm and Maven through the existing OIDC publishing. No new accounts are created by agents. Signing custody, store accounts, payment and Firebase are human prerequisites ([acceptance-register.md](acceptance-register.md) §2).
