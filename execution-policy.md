# V2 execution policy

Authority: Design AD-0022 and retained AD-0014/0016/0018/0019/0020. The previous task/product policy is frozen history. This policy keeps serial delivery, independent review, required native verification and security gates while replacing the current product/task graph.

## 1. Authorization and ordering

The owner added [Design AD-0023](https://github.com/ArcForges/ArcForges-Design/blob/main/docs/decisions/AD-0023-current-dependency-baseline.md): first review, verify and merge the Design/Plan policy amendment; only then start AFV2-ENV-01. Upgrade all current tools, CI Actions/images and direct/transitive business dependencies across ArcForges, Cloud, Web, Contracts, DesktopPlatform, ArcForges-Design and Plan to the latest upstream stable releases, including major versions, with local/CI parity. Concrete versions are selected and locked during implementation, not during document approval. BASE-01 is parked with preserved work; both former roots depend on ENV delivery. Later tasks keep this policy for dependencies they add or change.

Use a dated official-source inventory with exact versions, hashes/digests, lockfiles and resolved executable paths; platform-specific artifacts and CI/native OS venues remain explicit. An incompatible latest stable dependency requires repair or an unresolved blocker, not an unreported older-version exception. The user authorizes prerequisite tool installations on the designated hosts for this task, superseding the generic owner-install prerequisite within this scope. Preserve old installations for rollback/historical reproduction; network/proxy/security changes and public activation remain outside that authorization. Published bytes, applied migrations, historical receipts and frozen source audits retain their actual versions unchanged.

On 2026-11-15 the owner approved only AD-0023's bounded Contracts Go qualifications: retain the complete selected module graph while separately proving the named upstream metadata entries are absent from each applicable actual tool and Contracts-owned build/test closure; admit only `golang.org/x/exp/typeparams` and `golang.org/x/telemetry` through reviewed latest fixed upstream commits with their disclosed experimental/no-compatibility posture. The scope is Contracts' two existing Go modules, four declared tools and existing Windows/Linux configurations, not a general unused-dependency or other-repository exemption. The Design amendment lists exact eligible names and evidence requirements. Merge Design then this Plan amendment before affected dependency admission. Keep both-module checksums/tidy/security checks and all existing native gates unchanged; classification is acceptance accounting only. Final candidate graphs must be remeasured on both applicable platforms; the dated research is not current acceptance.

Implementation requires an explicit user-authorized list or range of AFV2 task IDs. Record that list as a PLAN ledger note before starting. The design/plan migration alone is not implementation authorization. Never resume any archived task or roadmap item. `plan.py next` names the global next eligible task; the coordinator must still intersect it with the authorized IDs.

Exactly one task is active. Within the authorized range, start the first planned task in graph order whose real dependencies are delivered or complete. Superseded dependencies do not silently count as delivered: update the dependency graph through a reviewed decision. Blocked tasks do not occupy the active slot, and independent eligible work may continue. A failed mandatory MXC profile blocks its admission and dependent Core work; negative probe results are evidence, not permission to weaken the product.

The coordinator owns state/ledger changes and all pushes, PRs, merges and publication. Delegated work is limited to the authorized task/write scope. Each implementation task receives an independent reviewer who did not author it; without one, do not merge. Independent author work within the task may run with bounded tool parallelism; no second product task starts concurrently.

## 2. Task states and evidence

| State | Meaning |
|---|---|
| planned | Not started or parked with preserved branch/worktree and reason |
| active | The single task currently being implemented |
| blocked | Missing named acceptance-register/human prerequisite; independent eligible tasks may continue |
| delivered | Merged at reviewed head, required repository statuses passed, code/development acceptance met and applicable ordinary publication/deploy evidence recorded |
| complete | Delivered plus all its completion prerequisites; never use missing mandatory native safety evidence as an external deferral |
| superseded | Replaced by a reviewed decision with reason; not a ready dependency |

Use tools/plan.py to change state and append the ledger. Each delivered task records every repository PR and merge SHA, plus applicable artifact/deployment identity. The immutable old graph/ledger is never edited. UNKNOWN native or routed effects are not erased to advance a task.

## 3. Verification and independent review

Authors run targeted/affected checks, native scenarios specified by the task, locked restores, analyzers and AOT builds. Use only task-listed external doubles; native isolation/terminal/resource/files/cryptography/state/recovery acceptance remains real. Record exact commands, source/artifact identity, environment, observed outcome and limitations. Tests that merely repeat unchanged evidence are not expanded without a concrete reason.

Fixture permission is specific to the declared boundary. ID-01 may use an external mail peer and authenticator/browser ceremony inputs; HOST-01 may use labeled catalog/provider-fact data through the real resolver; HOST-02 may use a versioned external payment HTTP peer and signed webhook test inputs; HOST-03 may use deployment-provider fixtures for dry-run/failure paths. WEB-01..04 may use typed responses/view models for component rendering and request-ordering checks. ACC-02 may reuse only the named external mail/payment/input peers while running the complete Blazor/Go/PostgreSQL/Node journey. The graph's `fakes_allowed` records the exact limits; other tasks do not inherit these permissions automatically.

Proof/signature verification, origin binding, authorization, entitlement/payment business state, actual database transactions, and native Job/cgroup/PTY/filesystem/recovery behavior are never replaced with a fake success. Ordinary deterministic input vectors, test accounts/keys and controlled faults are test inputs, not evidence that an external provider or OS enforcement was exercised. Provider/mail/domain/merchant authority qualification remains AR-10/H-04 activation evidence. A fixture cannot close that item, establish a published artifact/authority identity or enable public sales. Finished Dashboard control journeys cannot be accepted against synthetic API-success responses.

After pushing, fetch the exact SHA from GitHub into a worktree on each designated MCP host and run that repository's unchanged `python eng/verify.py run-and-report` profile. Windows runs on the owner's native Windows workstation; Linux runs on H-22 native Linux with its real user manager/cgroup delegation. No agent scratch, WSL, SSH or another host substitutes. No bundles or verification records are carried between hosts. Native host prerequisites are installed/configured by the owner.

Every PR needs its actual required statuses (`arcforges/windows` and `arcforges/linux`, or the repository's documented single-host rule) at the reviewed head. External PRs also need their configured hosted CI. No bypass actors, handwritten/copied statuses, weakened steps, hook disabling, `--no-verify`, ruleset/permission changes or automatic merge. If a host is unavailable, report the exact missing capability, leave status missing and stop that merge; complete reviewable non-host work where authorized.

The independent reviewer reads the full latest diff against Design/contracts/requirements, records blocking and nonblocking findings, and reruns only changed validators or disputed evidence. Fixes get delta review; a new code head needs fresh required host profiles. An author-side audit does not satisfy the independent review gate. Plan state/ledger-only PRs retain the existing coordinator-check exception; graph/policy/tool changes require independent review.

## 4. Repository scope and removal

Work in `<repo>/.worktree/<task>` on `task/<task>` or Plan `plan/<topic>` / Design `design/<topic>` branches, never primary main checkouts. Follow each task's repository paths and explicit scope. Necessary solution/central-package/lock/admission entries may change only for the task's declared modules. Larger scope changes require a reviewed Plan amendment.

An explicitly declared new module/file may be created at its listed target path. A nonexistent path does not authorize an alternate name for an existing module: retained/reworked/deleted implementations and their real adapters, generated tables, tests and composition files must be covered by the task's source-audited allowlist. Adding an unrelated project or widening to a whole repository still requires review. CLI-01 delivers offline core/admin commands; FILE-01/02 add the actual data/delete CLI slices; CENTER-02 adds working center-control commands with their local adapter. HOST-03 delivers deployment infrastructure, while DIST-01 assembles the actual completed Go/PostgreSQL/Blazor package after WEB-04 transitively through MIG-01.

Verify replacement before removing critical executors/resource/data safety. Remove disconnected retired modules early. End with one runtime, not permanent Task/Sandbox switches, stubs or unused projects. Preserve shared DesktopPlatform/Contracts consumers and all published artifacts. Applied SQL history/checksums remain immutable; drop obsolete live tables through a forward migration with backups and unresolved-effect checks.

Never unpublish, deprecate or delete published versions. Never admit Contracts 1.0.0-ci.350.1, DesktopPlatform Build.Policy 1.0.0-ci.124.1, or first-party versions whose publishing commit is not an ancestor of producer main. Keep Dependabot PRs untouched. Do not read/print secrets or change network/proxy/security settings.

## 5. Deployment and merge order

Design merges first. Plan host validation then fetches and checks actual Design main and runs the reciprocal traceability checker. Before Plan merge, rerun both host legs if their recorded `design-main` differs from current Design main; a Plan status alone does not encode its Design baseline.

Cloudflare changes occur only through repository scripts and guarded main-push deployment. `workers.dev` and preview surfaces stay off. Unconfigured official surfaces deploy dark. Existing external security-successor admission floors and backup/restore guards remain in force; no historic one-time bootstrap authorization is automatically reused for V2. Self-hosted delivery needs no official subscription.

Official/public activation and outward-facing distribution use AFV2-PROD-01 after its business/provider/legal/domain prerequisites and explicit owner approval. Ordinary first-party package cohorts published by the existing main-push delivery mechanism remain ordinary delivery. No package publication or successful build is relabeled as runtime acceptance. Once the authorized task range completes, stop without inventing further scope.

## 6. Failures and resumption

For a human prerequisite whose Blocks column names the task, set blocked with the ID and reason, preserve its worktree/head, report what is needed, and continue eligible authorized work. A live-business prerequisite blocks activation only when specified; do not stall architecture/code on undecided prices. A mandatory safety/compatibility failure is never waived as such a deferral.

Record interruption state, pushed SHA, uncommitted files and exact next action. On resume fetch/check current main and remote branch before continuing; reuse successful evidence only when its inputs match. Do not restart the whole project or old queue. Fix a defect preventing agreed acceptance within scoped task bounds; do not turn acceptance into unrelated new requirements. Keep builds incremental, avoid repeated full suites/poll loops, and stop after sufficient verification.
