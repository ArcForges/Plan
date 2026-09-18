# ArcForges implementation

## Current task

```text
Implement ArcForges Substep 00.00 — Product and naming freeze.

Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\00-specification-naming-and-rights-freeze.md
Owning section: WP-00.00; anchor: rule-wp-00.00.
Scope: this substep, its nested sections, and applicable package-wide obligations.
Required upstream work packages: none.

Related formal documents; resolve the relevant rules and follow their references:
- C:\MyFile\Projects\ArcForges-Design\docs\requirements\00-product-scope-and-portfolio.md
- C:\MyFile\Projects\ArcForges-Design\docs\requirements\01-normative-glossary-and-invariants.md
- C:\MyFile\Projects\ArcForges-Design\docs\architecture\27-platform-projects-and-application-assistants.md
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

## Execution boundaries

Implement only the current owning substep, including its nested sections. Read the whole parent work package so its inputs, rules, non-goals, impacts, tests, completion gates and appended amendments are not missed. Apply the provisions relevant to this substep; do not implement siblings or later work packages. A .90 substep verifies its assembled stage and does not authorize postponing earlier required behavior until then.

Use one main context serially, without subagents. Follow completeness, clarity and convergence together: fulfill the accepted obligations of this substep and make necessary design and implementation decisions yourself, based on verified facts and the goal of a complete, commercially operable product. Preserve explicit user constraints, compatibility and scope. Do not interrupt for routine decisions or approvals, or stop after planning, implementation or PR creation; review, CI fixes and merging are already authorized.

## Collect first, then plan

Before editing, establish actual roots, remotes, branches, HEADs, dirty state and existing worktrees. Verify the accepted Design baseline against the current default branch when accessible, and read one coherent commit. Preserve unrelated work and compatible published examples, package identities, application IDs and signing continuity.

Freshly search the current formal documentation during every execution, beyond the documents named in the current task. Those entry points may be incomplete. Search the substep ID, rule IDs, operations, messages, tables, packages, screens, states and failure cases; follow outgoing references and incoming uses across requirements, decisions, architecture, contracts, data models, experience, planning and assurance. Read the concrete definitions and acceptance rules, not just an overview. Inspect the relevant implementation, tests, package configuration and source provenance.

Verify the actual prerequisites and their evidence from the owning repositories, commits, CI runs and artifact manifests. Distinguish current upstream dependencies from later integration targets. A source file, merged PR or schema fixture does not prove that a required package is published or that a real consumer works. If the formal ID, scope or dependencies have changed, resolve them against the accepted Design before depending on outdated task wording.

Check relevant changing external facts against current official sources: SDKs, provider behavior, supported versions, limits and release/store requirements. Record the date and impact; a new external default does not authorize changing an accepted design silently.

Collect all applicable obligations, gaps, conflicts, affected files and verification requirements for this substep before fixing anything. Then form one bounded implementation plan mapping each obligation to its owner, change and evidence. Routine implementation choices do not need renewed permission.

Planning-repair authority: resolve missing, ambiguous, contradictory or impractical design within the current substep. Before deciding, inspect the complete affected authoritative chain and its relevant code, tests, artifacts, runtime/provider facts and evidence. Choose the resolution that fulfills the accepted commercial-product goals and explicit user constraints; record the decision, rationale, ownership, downstream and compatibility impacts, and verification requirements in the authoritative Design documents. Review and merge that documentation PR using the rules below before implementing dependent changes. Do not change requirements merely to fit existing code, tests or generated artifacts, remove accepted scope to manufacture completion, substitute repositories or begin another substep.

## Implement the selected work

Create each new branch in an isolated worktree with git worktree add in every repository requiring changes, following its .worktree convention. Reuse a verified worktree when resuming the same task. Do not substitute git checkout or git switch for a worktree. Use explicit working directories and keep every owner's changes within its own worktree; preserve primary checkouts and reference repositories.

Execute the collected plan continuously. Follow the authored proto, ABI, schemas, authorization metadata, exact numeric/time behavior, transaction plans, UI states and recovery semantics. Change generated outputs through their owning generator/source and prescribed tracking policy.

For cross-repository integration, produce and verify the required immutable candidate before building its consumer. Consumers restore exact package versions/hashes in an isolated environment, without sibling source, submodules, unpublished project references or accidental developer-cache dependencies. Follow the prescribed build, pack, candidate-test, registry-publication, availability-verification and manifest-promotion order. Record producer and consumer identities separately; partial publication is not a complete release.

Honor the producer stage matrix. An explicitly permitted early fixture has a named later replacement owner. It cannot satisfy a currently required real transport, package, native, AOT, Cloudflare, device, browser, provider or commercial gate. Conversely, do not demand a future producer at an earlier stage that deliberately uses a fixture. Shared gates close only when their combined required evidence exists. Investigate and repair setup or access failures using available tools and permissions; continue all independent work while resolving dependencies. If an externally controlled account, credential, device or service remains unavailable after feasible remedies, report the exact missing prerequisite and evidence without inventing a pass or removing accepted scope.

## Verify, review and finish

Run the substep's stated tests and completion gate, applicable parent-WP obligations, required repository checks and affected consumer verification. Wherever the available environment permits, run real end-to-end tests across the affected application, service and package boundaries, including specified failures and recovery paths, using independent expectations. Keep documentation/schema/unit/fixture checks, clean packaged-consumer execution, real provider/device/runtime evidence and commercial activation distinguishable.

Review the complete change against the collected obligations, including boundaries, compatibility, permissions, data/UI/recovery behavior, package identities, tests and provenance. Fix concrete defects and repeat the affected checks; do not restart an unlimited design expansion. Keep required implementation and test evidence with its owning repository according to the work package's conventions.

Before opening each PR, complete the documentation or implementation it owns, self-review and the locally executable checks required at that stage. A failed required local check must be fixed first. Evidence that requires PR CI, merge or publication remains explicitly pending until verified; it must not prevent the prerequisite PR from progressing through the required sequence.

Commit only this substep's changes and create the necessary scoped PRs, stating cross-repository dependencies and pending gates. Review every PR's complete diff before merging. Fix review and CI findings in this task's open PRs, repeat affected checks and review the final changes. Do not modify unrelated PRs or reopen closed PRs. If existing work already satisfies the substep, verify its current evidence instead of making empty commits or PRs.

Merge automatically in dependency order once required merge conditions are satisfied, without requesting confirmation. For documentation-only PRs with no configured CI, merge after review. For every other PR, wait for all applicable CI checks to succeed on the latest head; code changes without CI require appropriate CI before merging. Diagnose and fix failures instead of stopping, disabling checks or bypassing protections. Keep branches and worktrees after merging.

Continue through applicable post-merge publication, availability and integration checks; verify the actual merged commits and artifacts. Fix failures within this substep, using a new scoped PR when the previous one is already merged. Do not stop at a decision, repairable environment issue, pending CI or merge boundary. Do not place credentials or private data in source, reports or logs.

Report the exact substep, changed owners and files, retained worktrees and branches, merged commit/PR/artifact identities, observed verification results and any genuinely unavailable external prerequisite. State which acceptance gates actually passed and which remain unverified; documentation checks and merged PRs cannot establish product readiness. Finish only after completing the authorized workflow and all independently achievable work for this substep; do not begin the next substep.
