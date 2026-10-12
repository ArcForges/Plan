ARCFORGES PARALLEL DELIVERY LAUNCHER

Act as the coordinator and, once the user resumes feature work (see the run gate below), execute the selected scope. Maximize useful parallelism toward the complete commercially operable ArcScope system. This authorizes subagents, scoped implementation, necessary documentation repairs, PR creation, review and merging under the current execution rules. Make routine decisions autonomously.

Replace only the SCOPE block for another batch. It may contain any combination of sections, rows, task/slice IDs or generated task prompt blocks copied from the current Plan. The prefilled selection preserves the source launcher's six categories, refreshed from the current list.

Run gate (added 2026-10-10 by the phase-2 wrap-up): the user's instruction of 2026-10-09 (brief section 0b) stops the migration after phase 2, including its reviews, CI, merges, publication, deployment and validation, and allows no feature work until the user resumes it. Phase 2 is complete (2026-10-10): P2-026 (a decision record, merged through Design #346/#347/#348 and Plan #467/#469/#475) and WEB.40, AND.40, HAR.40, CLOUD.85, PRF.11, CLOUD.84 and CON.40 (merged, published or deployed, and recorded in the merged ledger) are done. CLOUD.85 is complete; the other tasks are delivered, with completion follow-ups or prerequisites still open (WEB.40 and HAR.40 are ready to complete). CON.40 is delivered, not complete: Contracts #97 merged as 56158219 (--match-head-commit 15d94d97), main-push CI 38074767207 published 1.0.0-ci.363.1 (12 NuGet packages and @arcforges/ai-internal only; no retired identity published, nothing unpublished), ledger Plan #477 5e3c53e6; its completion waits on WEB.40, AND.40 and CLOUD.84 being complete. No claim, lease or integration role is held, and no work runs, under this launcher or the continuation prompt (C:\MyFile\Projects\Gap\ArcForges-Continuation-Prompt-2026-10-10-Opus.md), until the user resumes. The SCOPE block below is the selected remaining work (21 rows; 310 in-scope tasks are not complete in total). Do not run it before the user resumes feature work. Until then, this run gate takes precedence over sections 3 and 7.

=== SCOPE BEGIN ===

## Adoption stage — [prompts](tasks/adoption.md)

| Task | Repository | Size | Start prerequisites | Title |
|---|---|---|---|---|

_No open rows at 2026-10-10: every task in this table is complete, inherited, superseded or out of scope._


### Adoption slices

| Slice | Repository | Size | Start prerequisites | Title (tasks it opens) |
|---|---|---|---|---|

_No open rows at 2026-10-10: every task in this table is complete, inherited, superseded or out of scope._


## Family governance and policy tests — [prompts](tasks/governance.md)

| Task | Repository | Size | Start prerequisites | Title |
|---|---|---|---|---|

_No open rows at 2026-10-10: every task in this table is complete, inherited, superseded or out of scope._


## Contracts schema closures — [prompts](tasks/contracts.md)

| Task | Repository | Size | Start prerequisites | Title |
|---|---|---|---|---|

_No open feature rows at 2026-10-10. CON.40 (C#-only SDK standardization) was phase 2 and is delivered (Contracts #97, Plan #477); it is not a row of this launcher. Its completion waits on WEB.40, AND.40 and CLOUD.84 being complete._


## Foundation values — [prompts](tasks/foundation.md)

| Task | Repository | Size | Start prerequisites | Title |
|---|---|---|---|---|

_No open rows at 2026-10-10: every task in this table is complete, inherited, superseded or out of scope._


## Runtime proofs — [prompts](tasks/runtime-proofs.md)

| Task | Repository | Size | Start prerequisites | Title |
|---|---|---|---|---|
| PRF.02 | ArcScope | M | CON.91, FND.01, PLT.11, ADOPT.05.runtime-proofs (adoption) | ArcScope desktop Native AOT package proof |
| PRF.04 | DesktopPlatform | L | CON.05, ADOPT.02.runtime-proofs (adoption) | Local RPC under AOT: bidirectional named-pipe/UDS probe processes |
| PRF.05 | DesktopPlatform | M | CON.92, PRF.07, ADOPT.02.runtime-proofs (adoption) | Generated gRPC-Web under AOT against deployed Worker/Container ingress |
| PRF.06 | DesktopPlatform | M | PRF.07, CON.11, ADOPT.02.runtime-proofs (adoption) | Realtime (EventService.Watch/Poll) under AOT |
| PRF.11 | Web | L | CON.92, WEB.40, PRF.07, CON.07, ADOPT.09.runtime-proofs (adoption) | Blazor WebAssembly production build and generated C# SDK proof against deployed ingress |
| PRF.12 | Mobile | L | AND.40, PRF.07, CLOUD.26, ADOPT.10.runtime-proofs (adoption) | MAUI Android release proof: Mono AOT release, trimming and R8, 16 KB alignment, signing, unary, server stream, trailers, cancel and Keystore against the proof ingress |


## Desktop platform mechanisms — [prompts](tasks/platform.md)

| Task | Repository | Size | Start prerequisites | Title |
|---|---|---|---|---|
| PLT.09 | DesktopPlatform | L | PRF.04, CON.04, ADOPT.02.platform (adoption) | Local gRPC transport and framing over Named Pipe/UDS |
| PLT.10 | DesktopPlatform | M | PLT.09, ADOPT.02.platform (adoption) | Parent-owned endpoint identity |
| PLT.11 | DesktopPlatform | M | PLT.10, ADOPT.02.platform (adoption) | Child registration lifecycle |
| PLT.15 | DesktopPlatform | M | PLT.09, CON.04, PLT.13, ADOPT.02.platform (adoption) | Brokered large data over the sandbox boundary |
| PLT.20 | DesktopPlatform | M | PLT.19, ADOPT.02.platform (adoption) | Actions and availability |
| PLT.24 | DesktopPlatform | L | PLT.19, PLT.20, PLT.21, ADOPT.02.platform (adoption) | Invocation pipeline |
| PLT.32 | DesktopPlatform | M | PLT.28, ADOPT.02.platform (adoption) | Lifecycle, menus and shutdown |
| PLT.33 | DesktopPlatform | L | PLT.27, ADOPT.02.platform (adoption) | Accessibility and localisation baseline |
| PLT.35 | DesktopPlatform | S | PLT.26, PLT.27, PLT.28, PLT.29, PLT.30, PLT.31, PLT.32, PLT.33, PLT.34 (out of scope; history edge), ADOPT.02.platform (adoption) | Publish DesignSystem/Shell packages and verify real integration |
| PLT.40 | DesktopPlatform | L | PLT.36, ADOPT.02.platform (adoption) | Per-application secrets and session isolation |
| PLT.44 | DesktopPlatform | M | PLT.36, PLT.01, FND.04, ADOPT.02.platform (adoption) | Append-only audit subsystem |
| PLT.45 | DesktopPlatform | XL | PLT.15, PLT.09, PLT.10, CON.04, ADOPT.02.platform (adoption) | Content helper and OS-enforced isolation (ContentSandbox host) |
| PLT.46 | DesktopPlatform | M | PLT.36, PLT.37, PLT.38, PLT.39, PLT.40, PLT.41, PLT.42, PLT.43, PLT.44, PLT.45, PLT.57, ADOPT.02.platform (adoption) | Publish Security packages and verify real integration |
| PLT.53 | DesktopPlatform | S | PLT.47, PLT.48, PLT.49, PLT.50, PLT.51, PLT.52, ADOPT.02.platform (adoption) | Publish Observability packages and verify real integration |
| PLT.57 | DesktopPlatform | M | PLT.24, PLT.38, APP.01, PLT.44, ADOPT.02.platform (adoption) | End-to-end capability invocation with real security enforcement inside one product |

=== SCOPE END ===

1. AUTHORITIES AND TOOL
P = C:\MyFile\Projects\Plan
D = C:\MyFile\Projects\ArcForges-Design
T = python -I C:\MyFile\Projects\Plan\tools\delivery.py
T is command shorthand: expand it before executing, and replace P/D with their full paths.

Read P\arcforges-implementation.md and P\execution-policy.md completely, P\single-task-command.md, and D\docs\planning\delivery\README.md. These govern the run; copied scope text selects work but never overrides current contracts, prerequisites, write scopes or policies. Read each edited repository's AGENTS.md. Resolve copied tasks/... links relative to P.

Make repository changes only in this documentation pair and the seven retained implementation repositories under C:\MyFile\Projects\ArcForges: DesktopPlatform, Contracts, ArcScope, Cloud, AI, Web and Mobile. Read declared reference sources when task obligations require them. ArcScope is the current product; preserve its gRPC-Web and helper-only LocalRpc mechanisms. Shared agent orchestration is C# (Cloud Harness, HAR.40), with TypeScript limited to thin Cloudflare adapters (C#-first, 2026-10-08). Current progress comes from merged Design/Plan main, record branches, PRs and the ledger. WP03.02 is historical evidence; never infer that WP03.03 or adoption has completed.

Keep clean primary checkouts fast-forwarded. Run T status --json and T ready --json with explicit --plan P --design D. Use the same roots for show, claim, update and release, avoiding environment/default-root drift. For planning changes, generate and check always name both retained worktree roots; ledger-only check may read D at current main. Run an edited delivery.py from its own worktree. Never generate into or edit a primary checkout. The local build-slot command needs no repository-root flags.

2. RESOLVE THE SCOPE
Deduplicate the selected task and slice IDs. In tables, use only the first column; in generated task prompts, use only the primary task/slice ID; accept explicit ID-only lines or lists. Headings and IDs appearing only in prerequisites, titles, obligations or explanatory text add no work. Validate IDs against the current graph. Report unknown/retired IDs without guessing replacements; continue valid selections. An empty selection never means all tasks.

Keep that target set for this run and pass it to every worker. Claim no out-of-scope delivery task or adoption slice. Required reviews, integration roles, resource leases, ledger records and narrowly necessary planning repairs are part of completing selected work. Report unmet out-of-scope prerequisites rather than silently adding them. Table order and section order are not execution barriers.

3. PLAN, DISPATCH AND KEEP CAPACITY BUSY
First resolve scope and current state, then establish one batch plan covering dependencies, delegation, validation and merging. Each claimant researches its own task and establishes a complete task plan before editing; independent tasks research and execute concurrently.

Use up to 10 concurrent subagents, or fewer if the runtime supports fewer or less useful work is ready. Every subagent (worker, fixer, reviewer, integration helper) runs on Opus 5.5, never Haiku 5.5 (user directive of 2026-10-10, brief section 0c); the main agent coordinates and decides. Count workers, reviewers and integration owners within that limit. Use actual concurrent agents where available and report a runtime limit accurately. Allocate capacity dynamically; do not create fixed waves or reserve idle roles. Multiple tasks in the same repository may run concurrently in separate retained worktrees under the declared shared-resource protocols.

Give each live session a unique worker name. Delegate with the matching Worker, Resume or Integration owner entry from P\single-task-command.md, plus the selected IDs and these launcher rules. Each worker reads its exact task prompt, linked obligations, prerequisite evidence and applicable adoption classification. The coordinator may inspect anything needed to resolve a blocker; no repeated whole-corpus reading is required.

Resume this batch's work first, then take ready completion follow-ups and ready tasks that unblock others. Schedule reviews and merges promptly. Workers obtain their own atomic claims through T before editing; dispatch is not ownership. Keep only one active claimant per task. Use required resource leases briefly and the repository integration role for merges. Run CPU-heavy local builds/tests one at a time through T build-slot run; other coding, research and review continue.

Refresh status/readiness after meaningful completions, merges, releases or blockers; wait with backoff for running work instead of polling tightly. Refill available capacity immediately. A task awaiting review, CI, publication or merge does not stop unrelated work. Resume or replace idle/returned workers using durable handoffs; do not stop merely because the ready list is temporarily empty while this batch can still advance.

4. EXECUTION, REVIEW AND DURABLE COMPLETION
Use a retained Git worktree for every repository change and preserve branches/worktrees. Follow the task/<key> naming, PR title IDs and claim lines required by the procedure. The coordinator creates PR bodies with --body-file. Do not hardcode another model's authorship or tool branding.

Record local branches, heads, validation, blockers and next actions in the claim at each checkpoint; after the coordinator publishes a branch, record its PR, reviewed head and merge commit. Keep leases renewed. Workers and execution agents edit and commit LOCALLY only. Before a worker returns, it commits locally and updates or releases its claim with a usable handoff. The coordinator pushes branches, opens PRs, posts review records and merges (brief section 8; subagent publication protocol). A restarted coordinator reconstructs work from records and PRs. Reuse a worker identity only for verified resumption with no other live holder; otherwise use the documented release/takeover rules. Never steal a live claim or treat a worker's silence as release.

Have another available session review each complete PR at its exact head. If only one session is available, perform and disclose self-review. Record approval or findings using the procedure's review format and reviewer identity. Fix findings and review changed heads. The integration owner verifies the current claim epoch, approved head and applicable checks, then merges with --match-head-commit and a title retaining the task IDs. Required CI must pass even for documentation-only PRs; repositories without CI merge after review. Apply shared-resource protocols at integration. Check combined Plan ledger changes against current main in a retained integration worktree; any changed PR head requires review again.

Confirm required publication/deployment results, merge the Plan ledger record, then update the claim state. A merged implementation PR or an accepted-baseline label is not task completion. Use delivered while completion prerequisites remain; perform and record the task's remaining acceptance when it becomes a completion follow-up. Only merged complete/inherited/superseded ledger records close a scope item. Keep progress guidance factual, with only necessary scoped documentation repairs.

5. ADOPTION AND EARLY CLEANUP
For ADOPT items, read D\docs\planning\delivery\adoption.md. ADOPT.01 first retargets the seven repositories' instructions through reviewed PRs and applicable CI, then freezes their baseline. Independent slices can proceed as soon as that record is merged; no whole-repository or whole-stage barrier is added.

Slices review their frozen inputs and change only the Plan ledger. Every inherited task receives its own inherited record, including accepted-baseline tasks. Record adjustments/conflicts and resolve them under the current decision process within the user's authorization; routine choices need no renewed approval. Repository adoption records follow the specified integration-owner rules.

CON.23, GOV.17 and GOV.18 are complete and are not in this selection, so this launcher owes no ADP-10 source cleanup for them. Ledger-only adoption does not perform or certify that cleanup. A later selection that names them must follow ADP-10. Preserve immutable published versions, provenance and required wire reservations; the approved retirement/migration exception does not authorize unrelated renaming. Unrelated lanes continue independently.

6. VALIDATION AND FAILURE POLICY
Follow execution-policy.md in full, including:

- No macOS CI, or CI for devices/emulators, desktop GUI, browser E2E, live services, real inference, installed-package consumers or public-release installation/upgrade. Retain necessary Windows/Linux compilation, AOT, packaging, static checks, targeted offline tests and non-duplicated security checks.
- Platform decisions in force (P2-022, P2-023 and P2-024, 2026-10-08 and 2026-10-09): macOS is outside the delivery scope and is never claimed. Linux runtime checks run in the local WSL2 Debian distribution through PowerShell, on a Linux-native filesystem; toolchain installs inside WSL are performed by the user. Never SSH to remote hosts. Where the local toolchain differs from CI (for example Node 24.20 versus the 24.21 pin, or the SDK 10.0.401 locked restore), hosted CI is the authority and the local gap is recorded. The native PDF preview is retired and recorded as retired, never completed. Business logic is C# (C#-first); TypeScript is limited to thin Cloudflare adapters, and no Kotlin or TypeScript business logic is added.
- Local runtime/E2E checks require affected behavior and an existing suitable environment. Run once; repeat only after a relevant change or unresolved finding. No validation-driven vcpkg/SDK/emulator/toolchain installation, hidden build/test hooks or duplicate heavy builds.
- No routine public artifact downloads, repeated archive/hash/consumer audits, or verification-only tags, republication, re-signing or replacement versions. Retain locks, required signing/provenance/licences and one necessary publication-candidate identity check; promote the original candidate using provider receipts.
- Documentation-only changes need review and consistency checks, without extra product builds/runtime tests. Diagnose failed checks before a targeted rerun. Keep authoritative docs, AGENTS, workflow dependencies and release inventories consistent; report absent coverage honestly.
- Use normal networking. Diagnose a network failure before any retry. Retry ordinary or transient failures with bounded backoff, and inspect remote state before retrying a write that may have succeeded. On a PERSISTENT network failure, report the exact operation and error, stop network operations for that work, and continue independent work. Never change network or proxy configuration. Never expose credentials. This follows the user directive of 2026-10-08 (brief section 0, "Diagnose and retry ordinary failures"), which supersedes the older report-and-stop, no-retry rule for ordinary failures.
- Post-merge verification is limited to the expected merge commit, required build/publication/deployment job result and a clean fast-forward of the primary checkout. No new artifact-download, installation, hash-audit or runtime cycle.

7. STOPPING AND FINAL REVIEW
Continue until every valid selected item is closed in the merged ledger, or all remaining items have concrete blockers/out-of-scope prerequisites and no owned work, pending review/CI/publication/merge or ready follow-up can advance them. An unrelated blocker does not stop progress. If manual action or unavailable authority is indispensable, identify it and continue independent work. A persistent network failure stops only the network operations of the affected work, as section 6 states. Never label blocked or delivered items complete.

Before returning, review the batch's final records for missing PRs, publication results, ledger updates, stale claims and unresolved findings. Correct omissions within scope. Release unnecessary roles/leases and preserve a resumable handoff for unfinished work.

Report briefly: completed IDs and ledger states; PR links and reviewed/merge commits; delivered, blocked, invalid or waiting IDs with exact prerequisites, holders and next actions; required CI/publication/deployment outcomes; material untested coverage. For adoption, include classifications and newly opened tasks, distinguishing completed review from future source cleanup. Do not claim measured parallel speedups or commercial acceptance without evidence.
