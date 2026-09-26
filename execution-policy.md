# Execution and validation policy

This policy governs every delivery task and the adoption stage. It follows [Design P2-017](https://github.com/ArcForges/ArcForges-Design-B/blob/main/docs/decisions/phase-2-specification-decisions.md#rule-p2-017), the [CI/local policy](https://github.com/ArcForges/ArcForges-Design-B/blob/main/docs/assurance/ci-and-local-validation-policy.md) and the [delivery model](https://github.com/ArcForges/ArcForges-Design-B/blob/main/docs/planning/delivery/README.md) of [P2-018](https://github.com/ArcForges/ArcForges-Design-B/blob/main/docs/decisions/phase-2-specification-decisions.md#rule-p2-018).

## Collect, plan and implement

There is no single Current task. A worker selects a ready task or adoption slice with `python tools/delivery.py ready`, which reads only the merged graph, ledger and claims, claims it atomically with `python tools/delivery.py claim` as described in [arcforges-implementation.md](arcforges-implementation.md), records its handoff checkpoints on the claim, and owns it until it is delivered or complete, released or taken over. Any number of workers may run at once on different tasks, including different tasks in the same repository. The implementation baseline is complete through WP03.02; WP03.03 has not started. The user's latest instructions determine whether to start, continue or stop; this document neither authorizes starting work by itself nor imposes a stop after one task.

Inspect actual roots, remotes, branches, dirty state, worktrees, related PRs, current Design and invoked workflow scripts. Finish research and decisions, then establish one complete ordered plan before editing. Repair conflicting authoritative documentation before dependent implementation. Preserve product behavior, package IDs, signing continuity, immutable releases and unrelated work.

Use a retained Git worktree for every change, on branch `task/<key>` (the task ID in lower case with dots replaced by hyphens, such as `task/con-07`). Append commits to the task's open PR; otherwise create a new worktree/PR. Do not reopen closed PRs or modify unrelated dependency PRs. Prefix PR titles with the task identifier, such as `[CON.07]`, and keep it in the merge or squash commit title; a bundle of compatible ready tasks lists each identifier, and planning changes use `[P2-018]` or the affected task identifiers.

Coordination is at the narrowest boundary: each repository's integration owner (the session holding `roles/integration-<repository>`) decides merge order among ready PRs, merges only at the reviewed head of the claimant at the current claim epoch and applies the shared-resource protocols; exclusive phases are held through short leases released before waiting; the Architecture Owner decides contract and planning changes; the Release Engineering Owner runs release tasks. Coordination state lives in claim, lease and role records, pull requests and the ledger, never only in a conversation. Run CPU-heavy local builds/tests one at a time per workstation through the build slot and reuse existing caches. Routine decisions and authorized merging require no renewed approval.

## Validation restrictions

- No macOS CI job, runner or matrix, including self-hosted, scheduled and manual workflows. Local macOS source support may remain; never claim an unproduced macOS artifact or unobserved platform result.
- No hosted physical-device/emulator, desktop GUI, browser E2E, live service/RPC, real inference/Workflow, installed-package consumer or public-release install/upgrade tests. Remove hidden default check/build/publish invocations and obsolete artifact/status dependencies.
- Retain necessary Windows/Linux compilation, Native AOT compilation, packaging, static/format/type/lint checks, targeted offline unit tests and non-duplicated security. Do not multiply identical checks across platforms without a platform-specific requirement.
- Runtime/E2E checks are explicit local opt-in only for affected behavior supported by the existing environment. Run once; repeat only for a new change or concrete unresolved finding. Record untested coverage without inventing success or turning an optional missing environment into a new provisioning task.
- Do not install/reinstall vcpkg, SDKs, emulators or toolchains solely to expand validation. Git hooks must not silently restore/build/test on every commit/push.
- No routine public package/archive/image/site downloads, repeated member/hash comparison or consumer execution. Retain lockfile integrity, required signing/licence/provenance checks and one necessary identity/integrity check at an actual publication handoff. Additional downloads require a concrete integrity/publication defect or explicit user request.
- Promote the original candidate. Use provider upload/deployment receipts and status/coordinate metadata; no public-byte polling. Maven main uses SNAPSHOT, and formal Central publication requires a deliberate tag.
- Do not create tags, republish, re-sign or allocate replacement versions solely for verification. Diagnose failures before rerunning; no blind retries.
- Documentation-only edits require consistency/link review without an additional local product-build or runtime-test cycle. Code repositories still run their existing applicable CI for documentation-only PRs. Keep AGENTS, active docs, workflow dependencies and actual release inventories synchronized. Preserve historical evidence as history, not as a rerun mandate.

## Network and resources

Use the normal network path. On a failed network operation, stop and report the exact operation rather than changing networking or repeatedly retrying. Do not invoke wsl.exe or WSL wrappers; use a directly available WSL terminal only if necessary. Parallelize independent tasks, not competing heavy local builds.

## Review and merge

Review each complete PR and fix findings. Documentation repositories that have no CI merge directly after review. In code repositories, every PR, including documentation-only changes, must run the existing applicable CI and may merge automatically only after all retained latest-head checks succeed. Do not skip configured checks or weaken branch protection to merge documentation changes. Remove obsolete runtime/macOS job references rather than adding fake passing gates. Do not bypass retained build/security/signing failures.

Post-merge verification is limited to the expected merge commit, required build/publication/deployment job result and clean fast-forward primary update. Do not start another public-download/hash/install/device/browser/runtime cycle. Keep branches and worktrees, protect credentials and report actual results and material untested coverage. Deployment success is not a live test, and compilation is not physical-device or full commercial acceptance.
