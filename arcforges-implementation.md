# ArcForges implementation

## Current task

```text
Implement ArcForges Substep 02.05 — Dependency policy.

Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\02-build-governance-and-analyzer-policy.md
Owning section: WP-02.05; anchor: rule-wp-02.05.
Scope: this substep, its nested sections, and applicable package-wide obligations.
Required upstream work packages: WP-01.
Earlier substeps in this work package: 02.00, 02.01, 02.02, 02.03, 02.04. Verify their required stage evidence.

Related formal documents; resolve the relevant rules and follow their references:
- C:\MyFile\Projects\ArcForges-Design\docs\architecture\14-build-packaging-and-release.md
- C:\MyFile\Projects\ArcForges-Design\docs\architecture\21-platform-and-dependency-matrix.md
- C:\MyFile\Projects\ArcForges-Design\docs\architecture\25-web-toolchain-and-sdk.md
- C:\MyFile\Projects\ArcForges-Design\docs\requirements\12-quality-and-compatibility-contract.md
```


## Project background

ArcForges is a family of commercially operable applications and shared services. ArcNotes provides knowledge management, ArcScope instrument acquisition and analysis, and ArcSlate media production. These are independent Avalonia/C# desktop applications. Each owns its application state, conversations, storage and server session, and embeds reusable assistant UI and mechanisms published by DesktopPlatform. ArcChat is the assistant/companion feature name, not a fourth desktop executable or a shared application hub.

Nine independent repositories integrate immutable published artifacts. DesktopPlatform provides shared managed mechanisms, Avalonia UI packages, native C ABI wrappers and RID runtimes; product domain behavior remains with its product owner. Contracts owns authored proto and generates C# NuGet, TypeScript npm and Kotlin Maven packages. Public business clients use binary gRPC-Web, with the explicit authentication, object-transfer and provider protocol exceptions defined by Design.

The C# Native AOT business host runs in Cloudflare Containers behind Workers. D1 owns authoritative business data, Durable Objects coordinate, and R2 stores objects. The sole AI Harness runs in Cloudflare Workflows with Workers AI. Mobile uses Kotlin/Jetpack Compose for Android; Web uses React/TypeScript for Site, Account, Chat and Operations. Applications have independent sessions without sibling Device SSO. Private parent-owned helpers/extensions alone use the specified gRPC over Named Pipes/UDS. Cross-product collaboration is future-only.

The goal is the complete accepted commercial product: usable client workflows, correct contracts and transactions, permissions, failure recovery, real integration, distribution, support and commercial operation. Existing Hello World scaffolds and published probes are migration inputs; they do not prove completed product behavior.

## Authoritative material and source locations

Formal Design: C:\MyFile\Projects\ArcForges-Design.

Read its applicable repository instructions and current decisions. The planning entry points are docs/planning/README.md, docs/planning/implementation-sequence.md, docs/planning/work-packages/README.md and docs/planning/producer-artifacts-and-integration.md. Concrete behavior is defined across docs/requirements, docs/architecture (including contracts and data-model), docs/experience and docs/assurance. Current accepted amendments govern older text; filenames and historical inventories do not override them. Deprecated-input bodies are excluded from implementation reading.

Implementation repositories are under C:\MyFile\Projects\ArcForges: DesktopPlatform, Contracts, ArcNotes, ArcScope, ArcSlate, Cloud, AI, Web and Mobile. Each is a separate Git repository. Determine which owners this substep actually changes from the formal layout, package registry and work package.

Read-only reference sources are C:\MyFile\Projects\AionUi, C:\MyFile\Projects\AFFiNE, C:\MyFile\Projects\siyuan, C:\MyFile\Projects\Serial-Studio, C:\MyFile\Projects\ArcVideo and C:\MyFile\Projects\ArcVideoFoundation. Start with their completed matrices under Design's docs/assurance/reference-coverage and inspect the relevant source or drift only. Respect per-file licenses, provenance and excluded subtrees; a rewrite does not erase upstream obligations. C:\MyFile\Projects\StartArcForges is a packaged-artifact layout/notice reference only: do not execute, unpack or reverse engineer its binaries. Reference features do not create additional product requirements.

## Execution and validation policy

This policy governs both implementation profiles and every task block. It follows [Design P2-017](https://github.com/ArcForges/ArcForges-Design/blob/main/docs/decisions/phase-2-specification-decisions.md#rule-p2-017) and the [CI/local policy](https://github.com/ArcForges/ArcForges-Design/blob/main/docs/assurance/ci-and-local-validation-policy.md).

## Collect, plan and implement

Use Current task as the execution entry point. The user's latest instructions determine whether to start, continue to subsequent numbered substeps, or stop; this document neither authorizes starting work by itself nor imposes a mandatory stop after one substep. Inspect actual roots, remotes, branches, dirty state, worktrees, related PRs, current Design and invoked workflow scripts. Finish research and decisions, then establish one complete ordered plan before editing. Repair conflicting authoritative documentation before dependent implementation. Preserve product behavior, package IDs, signing continuity, immutable releases and unrelated work.

Use a retained Git worktree for every change. Append commits to an existing related open PR; otherwise create a new worktree/PR. Do not reopen closed PRs or modify unrelated dependency PRs. Prefix PR titles with the work package and substep, such as `[WP02 · SubStep 02.04]`.

One coordinator owns dependency order, review and merging. Independent repositories may use subagents with non-overlapping ownership. Serialize CPU-heavy local builds/tests and reuse existing caches. Routine decisions and authorized merging require no renewed approval.

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

## Review and merge

Review each complete PR and fix findings. Merge documentation-only PRs with no CI after review. Automatically merge source PRs after all retained applicable latest-head CI succeeds. Remove obsolete runtime/macOS job references rather than adding fake passing gates. Do not bypass retained build/security/signing failures.

Post-merge verification is limited to the expected merge commit, required build/publication/deployment job result and clean fast-forward primary update. Do not start another public-download/hash/install/device/browser/runtime cycle. Keep branches and worktrees, protect credentials and report actual results and material untested coverage. Deployment success is not a live test, and compilation is not physical-device or full commercial acceptance.
