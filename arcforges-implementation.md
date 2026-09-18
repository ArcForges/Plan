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

Use one main context serially, without subagents. Follow completeness, clarity and convergence together: fulfill all accepted obligations of this substep; use the specified business, contract, data, UI and recovery rules; choose ordinary internal implementation details without reopening settled design or expanding scope.

## Collect first, then plan

Before editing, establish actual roots, remotes, branches, HEADs, dirty state and existing worktrees. Verify the accepted Design baseline against the current default branch when accessible, and read one coherent commit. Preserve unrelated work and compatible published examples, package identities, application IDs and signing continuity.

Freshly search the current formal documentation during every execution, beyond the documents named in the current task. Those entry points may be incomplete. Search the substep ID, rule IDs, operations, messages, tables, packages, screens, states and failure cases; follow outgoing references and incoming uses across requirements, decisions, architecture, contracts, data models, experience, planning and assurance. Read the concrete definitions and acceptance rules, not just an overview. Inspect the relevant implementation, tests, package configuration and source provenance.

Verify the actual prerequisites and their evidence from the owning repositories, commits, CI runs and artifact manifests. Distinguish current upstream dependencies from later integration targets. A source file, merged PR or schema fixture does not prove that a required package is published or that a real consumer works. If the formal ID, scope or dependencies have changed, resolve them against the accepted Design before depending on outdated task wording.

Check relevant changing external facts against current official sources: SDKs, provider behavior, supported versions, limits and release/store requirements. Record the date and impact; a new external default does not authorize changing an accepted design silently.

Collect all applicable obligations, gaps, conflicts, affected files and verification requirements for this substep before fixing anything. Then form one bounded implementation plan mapping each obligation to its owner, change and evidence. Routine implementation choices do not need renewed permission.

Planning-repair authority: resolve missing, ambiguous, contradictory or impractical design within the current substep while preserving frozen product direction, architecture invariants and compatibility requirements. First inspect the complete affected authoritative chain and the relevant code, tests, artifacts and evidence it names. Record the decision, rationale, ownership, downstream and compatibility impacts, and verification requirements in the authoritative Design documents; review and freeze that amendment before implementing it. Do not change requirements merely to fit existing code, tests or generated artifacts. This authority does not permit overriding frozen decisions, substituting repositories or implementing another substep. Block the affected work and request clarification only when no safe, complete, in-scope resolution exists; continue independent authorized work within this substep where possible.

## Implement the selected work

Create each new branch in an isolated worktree with git worktree add in every repository requiring changes, following its .worktree convention. Reuse a verified worktree when resuming the same task. Do not substitute git checkout or git switch for a worktree. Use explicit working directories and keep every owner's changes within its own worktree; preserve primary checkouts and reference repositories.

Execute the collected plan continuously. Follow the authored proto, ABI, schemas, authorization metadata, exact numeric/time behavior, transaction plans, UI states and recovery semantics. Change generated outputs through their owning generator/source and prescribed tracking policy.

For cross-repository integration, produce and verify the required immutable candidate before building its consumer. Consumers restore exact package versions/hashes in an isolated environment, without sibling source, submodules, unpublished project references or accidental developer-cache dependencies. Follow the prescribed build, pack, candidate-test, registry-publication, availability-verification and manifest-promotion order. Record producer and consumer identities separately; partial publication is not a complete release.

Honor the producer stage matrix. An explicitly permitted early fixture has a named later replacement owner. It cannot satisfy a currently required real transport, package, native, AOT, Cloudflare, device, browser, provider or commercial gate. Conversely, do not demand a future producer at an earlier stage that deliberately uses a fixture. Shared gates close only when their combined required evidence exists. Missing account, toolchain, hardware or credentials remain explicit blockers, not invented passes or reasons to remove accepted scope.

## Verify, review and finish

Run the substep's stated tests and completion gate, applicable parent-WP obligations, required repository checks and affected consumer verification. Test the specified failures and recovery paths using independent expectations. Keep documentation/schema/unit/fixture checks, clean packaged-consumer execution, real provider/device/runtime evidence and commercial activation distinguishable.

Review the complete change against the collected obligations, including boundaries, compatibility, permissions, data/UI/recovery behavior, package identities, tests and provenance. Fix concrete defects and repeat the affected checks; do not restart an unlimited design expansion. Keep required implementation and test evidence with its owning repository according to the work package's conventions.

Before opening a PR, complete the required implementation, local validation, self-review and locally obtainable evidence for this substep. A blocked implementation or failed required local check is not ready for a PR. If the formal plan requires evidence obtainable only through PR CI, merge or publication, identify that gate and leave it explicitly pending; do not claim full acceptance before it passes.

Commit only this substep's reviewed changes and create one new PR per changed repository, stating cross-repository dependencies and pending external gates. Do not reopen, comment on or push updates to pre-existing or closed PRs. Do not automatically merge or activate a release beyond the applicable authorization and gates. Do not place credentials or private data in source, reports or logs. If existing work already satisfies the substep, verify its current evidence instead of reimplementing it or making an empty commit.

Report the exact substep, changed owners and files, worktrees, commit/PR/artifact identities, observed verification results and any remaining blocker. State whether its required acceptance has passed or whether implementation still awaits specified evidence or integration. Documentation checks cannot establish product readiness. Stop after the selected substep.
