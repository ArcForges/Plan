# ArcForges implementation — remote edition

## How to use this edition

This is the portable counterpart of [the local edition](https://github.com/ArcForges/Plan/blob/main/arcforges-implementation.md). Repository identities are HTTPS GitHub URLs; workspace locations are chosen by the execution environment. Use it from a local machine or a remote coding environment. Public source access does not by itself provide command execution, GitHub write access, deployment credentials or hardware; use the capabilities actually available and report any required capability that is genuinely unavailable.

To execute the current task, give the coding agent this command:

```text
Read https://github.com/ArcForges/Plan/blob/main/arcforges-implementation-remote.md completely and follow it to complete only its Current task. Use its remote repository map and pinned reference revisions. Collect first, plan, implement, review each PR, wait for applicable CI, merge and finish required post-merge verification. Keep branches and worktrees, then stop.
```

For another single task, use one block from [list-remote.md](https://github.com/ArcForges/Plan/blob/main/list-remote.md). An explicitly supplied block replaces only the Current task below for that run; all other instructions in this profile still apply. Reading the list does not authorize executing the whole list.

Choose a writable workspace. This bootstrap is for a fresh workspace; reuse existing checkouts only after verifying their origins, branches and dirty state:

```sh
git clone https://github.com/ArcForges/Plan.git Plan
git clone https://github.com/ArcForges/ArcForges-Design.git ArcForges-Design
git -C ArcForges-Design fetch origin main
git -C ArcForges-Design rev-parse origin/main
```

Resolve the current Design default branch once to a full commit, and read every formal document for the task at that same commit. GitHub `blob/main` links are discovery entry points: replace `main` with the resolved commit when reading a coherent snapshot. If a reviewed Design repair is merged, explicitly advance that snapshot before dependent implementation. Clone only the implementation owners and references needed for the selected task. Within a checkout, repository-relative paths are valid; machine-specific paths found in historical documents are location aliases, not required filesystem layouts.

## Current task

```text
Complete ArcForges Substep 02.04 - Version axis plumbing, with the explicitly authorized repository-wide CI and validation reduction.

Owning document: https://github.com/ArcForges/ArcForges-Design/blob/main/docs/planning/work-packages/02-build-governance-and-analyzer-policy.md
Owning section: WP-02.04; anchor: rule-wp-02.04.
Execution authority: Design P2-017 and docs/assurance/ci-and-local-validation-policy.md.
Scope: all nine implementation repositories, Design and Plan; append to the existing related Mobile PR, create retained worktrees/PRs for other owners, remove obsolete automated gates and correct active documentation.
Preserve upstream evidence; do not rerun historical runtime/public-download checks.
Stop after this task. Do not begin WP02.05.
```

## Project background

ArcForges is a family of commercially operable applications and shared services. ArcNotes provides knowledge management, ArcScope instrument acquisition and analysis, and ArcSlate media production. These are independent Avalonia/C# desktop applications. Each owns its application state, conversations, storage and server session, and embeds reusable assistant UI and mechanisms published by DesktopPlatform. ArcChat is the assistant/companion feature name, not a fourth desktop executable or a shared application hub.

Nine independent repositories integrate immutable published artifacts. DesktopPlatform provides shared managed mechanisms, Avalonia UI packages, native C ABI wrappers and RID runtimes; product domain behavior remains with its product owner. Contracts owns authored proto and generates C# NuGet, TypeScript npm and Kotlin Maven packages. Public business clients use binary gRPC-Web, with the explicit authentication, object-transfer and provider protocol exceptions defined by Design.

The C# Native AOT business host runs in Cloudflare Containers behind Workers. D1 owns authoritative business data, Durable Objects coordinate, and R2 stores objects. The sole AI Harness runs in Cloudflare Workflows with Workers AI. Mobile uses Kotlin/Jetpack Compose for Android; Web uses React/TypeScript for Site, Account, Chat and Operations. Applications have independent sessions without sibling Device SSO. Private parent-owned helpers/extensions alone use the specified gRPC over Named Pipes/UDS. Cross-product collaboration is future-only.

The goal is the complete accepted commercial product: usable client workflows, correct contracts and transactions, permissions, failure recovery, real integration, distribution, support and commercial operation. Existing Hello World scaffolds and published probes are migration inputs; they do not prove completed product behavior.

## Authoritative material and remote repositories

Formal Design: [ArcForges-Design](https://github.com/ArcForges/ArcForges-Design), default branch `main`. The default-branch commit verified on 2026-09-20 was `db2f060e0720af5483f23c6cf8a55a14101e1142`; this is an observation, not a permanent replacement for the required fresh baseline check.

Read its applicable repository instructions and current decisions. Planning entry points:

- https://github.com/ArcForges/ArcForges-Design/blob/main/docs/planning/README.md
- https://github.com/ArcForges/ArcForges-Design/blob/main/docs/planning/implementation-sequence.md
- https://github.com/ArcForges/ArcForges-Design/blob/main/docs/planning/work-packages/README.md
- https://github.com/ArcForges/ArcForges-Design/blob/main/docs/planning/producer-artifacts-and-integration.md

Concrete behavior is defined across [requirements](https://github.com/ArcForges/ArcForges-Design/tree/main/docs/requirements), [architecture](https://github.com/ArcForges/ArcForges-Design/tree/main/docs/architecture), [contracts](https://github.com/ArcForges/ArcForges-Design/tree/main/docs/architecture/contracts), [data models](https://github.com/ArcForges/ArcForges-Design/tree/main/docs/architecture/data-model), [experience](https://github.com/ArcForges/ArcForges-Design/tree/main/docs/experience), [assurance](https://github.com/ArcForges/ArcForges-Design/tree/main/docs/assurance). Current accepted amendments govern older text; filenames and historical inventories do not override them. Deprecated-input bodies are excluded from implementation reading.

Each implementation owner is a separate repository. Their current default branch is `main`; verify the actual remote before each run. Determine which owners the substep changes from the formal layout, package registry and work package.

| Owner | Repository / HTTPS clone URL |
|---|---|
| DesktopPlatform | https://github.com/ArcForges/DesktopPlatform.git |
| Contracts | https://github.com/ArcForges/Contracts.git |
| ArcNotes | https://github.com/ArcForges/ArcNotes.git |
| ArcScope | https://github.com/ArcForges/ArcScope.git |
| ArcSlate | https://github.com/ArcForges/ArcSlate.git |
| Cloud | https://github.com/ArcForges/Cloud.git |
| AI | https://github.com/ArcForges/AI.git |
| Web | https://github.com/ArcForges/Web.git |
| Mobile | https://github.com/ArcForges/Mobile.git |

### Read-only reference revisions

Start with the completed [reference matrices](https://github.com/ArcForges/ArcForges-Design/blob/main/docs/assurance/reference-coverage/README.md), then inspect only the relevant source or drift. The following published references were verified on 2026-09-20 against the original local committed HEADs and the matrix baselines. Use the full commit as identity; tags and branches are readable labels and must still resolve to the recorded commit.

| Reference | Remote source at the exact commit | Published tag or branch | Original local branch label |
|---|---|---|---|
| AionUi | https://github.com/iOfficeAI/AionUi/tree/29c9271a59484e4696778cb80164f705245a6186 | tag `v2.1.35` | `Branch_v2.1.35` |
| AFFiNE | https://github.com/toeverything/AFFiNE/tree/81df4751a367f2795bc0d165586650dbe8db73d6 | tag `v0.27.2` | `Branch_v0.27.2` |
| SiYuan | https://github.com/siyuan-note/siyuan/tree/eef10568384e2e7cf547adb029ae46a72e43c287 | tag `v3.7.3` | `Branch_v3.7.3` |
| Serial-Studio | https://github.com/Serial-Studio/Serial-Studio/tree/639daafb2fe7d324c3b2d5583d2514c8c470676f | tag `v4.0.3` | `Branch_v4.0.3` |
| ArcVideo | https://github.com/ArcForges/ArcVideo/tree/caf56513278703adec0c2933ec235bb864d72e31 | branch `reference-baseline`; no tag | `main` |
| ArcVideoFoundation | https://github.com/ArcForges/ArcVideoFoundation/tree/139eecaaa79dbad743a146f174a9c89a66ed594b | branch `reference-baseline`; no tag | `main` |

The `Branch_v...` names above are local convenience labels, not upstream branch names to clone. For example, a fresh AionUi reference checkout uses its published tag, then verifies HEAD against the full commit above:

```sh
git clone --branch v2.1.35 --single-branch https://github.com/iOfficeAI/AionUi.git AionUi
git -C AionUi rev-parse HEAD
```

ArcVideo and ArcVideoFoundation publish the original source history unchanged on their default `reference-baseline` branches, preserving its GPL-3.0 licence. Their separately initialized `main` branches contain only the new repository initialization and are not the source baselines. The original AionUi, ArcVideo and ArcVideoFoundation working trees have uncommitted local edits; those edits are not part of the published commits or tag snapshots and must not be silently assumed by a remote execution.

Respect per-file licences, provenance and excluded subtrees; a rewrite does not erase upstream obligations. Public repository visibility does not mean every subtree has the same reuse rights. The retired ArcChat initialization repository is not an implementation owner or a required checkout. Reference features do not create additional product requirements.

StartArcForges is a historical packaged-output tree, not a Git repository. Its publicly available reviewed evidence is [the distribution reference matrix](https://github.com/ArcForges/ArcForges-Design/blob/main/docs/assurance/reference-coverage/distribution-startarcforges.md). No public mirror, branch, tag or commit of the original packaged tree has been verified. Consume the existing matrix as planning evidence; if the selected task requires new direct inspection of that tree, report access to those exact packaged outputs as an unavailable prerequisite rather than inventing a source URL or claiming the matrix is the original artifact. Do not execute, unpack or reverse engineer those binaries.

## Execution and validation policy

This policy governs both implementation profiles and every task block. It follows [Design P2-017](https://github.com/ArcForges/ArcForges-Design/blob/main/docs/decisions/phase-2-specification-decisions.md#rule-p2-017) and the [CI/local policy](https://github.com/ArcForges/ArcForges-Design/blob/main/docs/assurance/ci-and-local-validation-policy.md).

## Collect, plan and implement

Complete only the Current task and its explicitly authorized cross-repository repair. Inspect actual roots, remotes, branches, dirty state, worktrees, related PRs, current Design and invoked workflow scripts. Finish research and decisions, then establish one complete ordered plan before editing. Repair conflicting authoritative documentation before dependent implementation. Preserve product behavior, package IDs, signing continuity, immutable releases and unrelated work.

Use a retained Git worktree for every change. Append commits to an existing related open PR; otherwise create a new worktree/PR. Do not reopen closed PRs or modify unrelated dependency PRs. Prefix PR titles with the work package and substep, such as `[WP02 · SubStep 02.04]`.

One coordinator owns dependency order, review and merging. Independent repositories may use subagents with non-overlapping ownership. Serialize CPU-heavy local builds/tests and reuse existing caches. Routine decisions and authorized merging require no renewed approval. Do not begin another numbered substep.

## Validation restrictions

- No macOS CI job, runner or matrix, including self-hosted, scheduled and manual workflows. Local macOS source support may remain; never claim an unproduced macOS artifact or unobserved platform result.
- No hosted physical-device/emulator, desktop GUI, browser E2E, live service/RPC, real inference/Workflow, installed-package consumer or public-release install/upgrade tests. Remove hidden default check/build/publish invocations and obsolete artifact/status dependencies.
- Retain necessary Windows/Linux compilation, Native AOT compilation, packaging, static/format/type/lint checks, targeted offline unit tests and non-duplicated security. Do not multiply identical checks across platforms without a platform-specific requirement.
- Runtime/E2E checks are explicit local opt-in only for affected behavior supported by the existing environment. Run once; repeat only for a new change or concrete unresolved finding. Record untested coverage without inventing success or turning an optional missing environment into a new provisioning task.
- Do not install/reinstall vcpkg, SDKs, emulators or toolchains solely to expand validation. Git hooks must not silently restore/build/test on every commit/push.
- No routine public package/archive/image/site downloads, repeated member/hash comparison or consumer execution. Retain lockfile integrity, required signing/licence/provenance checks and one necessary identity/integrity check at an actual publication handoff. Additional downloads require a concrete integrity/publication defect or explicit user request.
- Promote the original candidate. Use provider upload/deployment receipts and status/coordinate metadata; no public-byte polling. Maven main uses SNAPSHOT, and formal Central publication requires a deliberate tag.
- Do not create tags, republish, re-sign or allocate replacement versions solely for verification. Diagnose failures before rerunning; no blind retries.
- Documentation-only edits require consistency/link review, not product builds or runtime tests. Keep AGENTS, active docs, workflow dependencies and actual release inventories synchronized. Preserve historical evidence as history, not as a rerun mandate.

## Network and resources

Use the normal network path. Do not configure proxy 7890 or another proxy. On a failed network operation, stop and report the exact operation rather than changing networking or repeatedly retrying. Do not invoke wsl.exe or WSL wrappers; use a directly available WSL terminal only if necessary. Parallelize independent source work, not competing heavy local builds.

## Review, merge and stop

Review each complete PR and fix findings. Merge documentation-only PRs with no CI after review. Automatically merge source PRs after all retained applicable latest-head CI succeeds. Remove obsolete runtime/macOS job references rather than adding fake passing gates. Do not bypass retained build/security/signing failures.

Post-merge verification is limited to the expected merge commit, required build/publication/deployment job result and clean fast-forward primary update. Do not start another public-download/hash/install/device/browser/runtime cycle. Keep branches and worktrees, protect credentials and report actual results and material untested coverage. Deployment success is not a live test, and compilation is not physical-device or full commercial acceptance. Stop after the authorized task.

## Maintaining the two editions

When advancing the plan, keep the local and remote Current task synchronized. Preserve the same task IDs, ordering, dependencies and scope in list.md and list-remote.md. Changes to execution rules apply to both profiles; the remote edition additionally owns its repository map, published reference identities and environment-neutral bootstrap.
