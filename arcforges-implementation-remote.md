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
Implement ArcForges Substep 00.04 — Register the completed reference matrices as versioned planning inputs.

Owning document: https://github.com/ArcForges/ArcForges-Design/blob/main/docs/planning/work-packages/00-specification-naming-and-rights-freeze.md
Owning section: WP-00.04; anchor: rule-wp-00.04.
Scope: this substep, its nested sections, and applicable package-wide obligations.
Required upstream work packages: none.
Earlier substeps in this work package: 00.00, 00.01, 00.02, 00.03. Verify their required stage evidence.

Related formal documents; resolve the relevant rules and follow their references:
- https://github.com/ArcForges/ArcForges-Design/blob/main/docs/requirements/00-product-scope-and-portfolio.md
- https://github.com/ArcForges/ArcForges-Design/blob/main/docs/requirements/01-normative-glossary-and-invariants.md
- https://github.com/ArcForges/ArcForges-Design/blob/main/docs/architecture/27-platform-projects-and-application-assistants.md
- https://github.com/ArcForges/ArcForges-Design/blob/main/docs/assurance/reference-coverage-and-provenance.md
- https://github.com/ArcForges/ArcForges-Design/blob/main/docs/assurance/open-gates-register.md
- https://github.com/ArcForges/ArcForges-Design/blob/main/docs/assurance/reference-coverage/README.md
- https://github.com/ArcForges/ArcForges-Design/blob/main/docs/decisions/phase-1-foundation-decisions.md
- https://github.com/ArcForges/ArcForges-Design/blob/main/docs/decisions/phase-2-specification-decisions.md
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

## Execution boundaries

Implement only the current owning substep, including its nested sections. Read the whole parent work package so its inputs, rules, non-goals, impacts, tests, completion gates and appended amendments are not missed. Apply the provisions relevant to this substep; do not implement siblings or later work packages. A .90 substep verifies its assembled stage and does not authorize postponing earlier required behavior until then.

Use one main context serially, without subagents. Follow completeness, clarity and convergence together: fulfill the accepted obligations of this substep and make necessary design and implementation decisions yourself, based on verified facts and the goal of a complete, commercially operable product. Preserve explicit user constraints, compatibility and scope. Do not interrupt for routine decisions or approvals, or stop after planning, implementation or PR creation; review, CI fixes and merging are already authorized.

## Collect first, then plan

Map every repository identity above to an actual checkout in the current environment. Verify an existing origin before fetching; clone missing owners from their HTTPS URLs. Resolve relative document references inside the corresponding repository at the selected coherent commit. Preserve the same scope and evidence requirements in local and remote execution.

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

## Maintaining the two editions

When advancing the plan, keep the local and remote Current task synchronized. Preserve the same task IDs, ordering, dependencies and scope in list.md and list-remote.md. Changes to execution rules apply to both profiles; the remote edition additionally owns its repository map, published reference identities and environment-neutral bootstrap.
