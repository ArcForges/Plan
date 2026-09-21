# Execution and validation policy

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
