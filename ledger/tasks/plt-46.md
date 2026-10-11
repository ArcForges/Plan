---
task: PLT.46
status: delivered
recorded: 2026-10-11
claimant: w-deku-20261010-plt-46
epoch: 1
---

# Publish Security packages and verify real integration

**Decision: `delivered`, not `complete`.** The four Security packages (`ArcForges.Security`, `ArcForges.Security.Secrets`, `ArcForges.Security.Audit` and `ArcForges.Security.CapabilityEnforcement`) are packed, admitted, merged and published at `1.0.0-ci.131.1`. Two completion edges are still open: PLT.45 and PLT.66 are not `complete`. The durable-audit consumer leg also fails closed for every registry capability at the merged head (S60). Under S52(4) and the fix8 delta 2 note, this task is recorded delivered.

Sources are marked as follows. **Observed** means this author read it from GitHub on 2026-10-11 with `gh pr view`, `gh run view` (including `--log` grep), `gh api` and `git` on the Plan record branches, all read-only, with no artifact downloaded. **Coordinator-reported**, **claimant-reported** and **reviewer-reported** facts are labelled where they appear. This author re-ran no build, test, pack, consumer or scan.

## Evidence

- **Claim** (observed, Plan branch `claims/plt-46` at `eda20063f113c7c74788210b946d5a4715c162d4`):
  - PLT.46 epoch 1, claimant `w-deku-20261010-plt-46`, claimed 2026-10-10T20:03:00Z.
  - The handoff names DesktopPlatform #176, head and reviewed `61e11b7570ba2009fe8dd10ee3239b03841e911c`, and merge `fb8577c3d026966368fd71189f370ea43b77ef73`.
  - The claim is held by the coordinator for a local-only Opus agent (coordinator-reported; the claim note says the same).
  - PLT.46 is a selected row of the Final.md scope (coordinator-reported).
- **Planning authority** (observed). Coordinator ruling S52 narrowed PLT.46 to the four Security packages. Planning repair fix8 carried it into the record (S57(7)):
  - Design [#350](https://github.com/ArcForges/ArcForges-Design/pull/350): head `8d961a09fa819991f064a9600f4759acd70d078e`, merged as `f4b2299c1b57fb8a9905b9463680cc7bc4686687` at 2026-10-11T01:56:16Z.
  - Plan [#479](https://github.com/ArcForges/Plan/pull/479): head `fa0943b6442648fb2ab716be806a51087d4b2f7e`, merged as `f7cb511a4b58f8d93aec34cd06a19c2e2317e2da` at 2026-10-11T01:56:22Z.

  Both merged before #176 (01:57:58Z), so #176 merged under the fix8 text. The fix8 delta 2 note (S60, S61(6)) added the PLT.66 completion edge. The PLT.45 completion edge is in the record from S57(7). The brief text of S60 and S61(6) says "PLT.58". S62(1) rules that this means PLT.66.
- **Implementation** (observed). DesktopPlatform [PR #176](https://github.com/ArcForges/DesktopPlatform/pull/176), "[PLT.46] Publish the four Security packages and record package-level integration evidence", from `task/plt-46`. It changes 15 files (+1308/−43) in three commits:
  - `4a5e1ee9a1df83608837680ca0290164bb03dd4a` appends one new `[[allowlists]]` block to `.gitleaks.toml`, in the S52(2)/S50(3) form:
    - `targetRules ["generic-api-key"]`, `condition "AND"` and `regexTarget "line"`;
    - exact path regexes for `eng/policy/dependency-policy.json` and `eng/policy/dependency-reviews/plt-46-r1.json`;
    - two exact whole-line regexes, one for each indentation, for the successor `ArcForges.Security.Secrets.csproj` digest `7282dd206f5ca9cb59fe8d02e9423ac7080857fba03bd0ccff54410b4e2b6bff`.

    The diff shows no change to any existing block. `eng/test_dependency_policy.py` (+122/−5) registers the new block.
  - `d1bb49cb9f55d90ccfbd9d4c82ee520c9236527f` changes the four project files:
    - all four now pack (`IsPackable true`), with `PackageReadmeFile README.md` and the README/LICENSE/NOTICE.md pack items (S52(3));
    - `None Remove="Tests/**"` is added to Security, Security.Audit and Security.Secrets, but not to CapabilityEnforcement, which packs the parent `../README.md`;
    - a one-line `Description` is added to Security, Security.Secrets and CapabilityEnforcement, and the existing Security.Audit Description is unchanged;
    - no PackageId, reference or version changes.

    The same commit adds:
    - four `eng/packaging/packages.json` rows;
    - the dependency-policy input rebinding, with `reviewReceipt` now `eng/policy/dependency-reviews/plt-46-r1.json`;
    - the immutable receipt `plt-46-r1` (owner `w-deku-20261010-plt-46`, reviewer `w-deku-20261010-rev-plt-46`, decision approved, `previousReceipt` `eng/policy/dependency-reviews/nat-11-r1.json`, baseline `c8280488`, NuGet closure 58 and Python closure 10);
    - its `eng/provenance/files.json` row;
    - four `active-projects.json` blob refreshes;
    - the README status lines.
  - `61e11b7570ba2009fe8dd10ee3239b03841e911c` records the pack and clean-consumer evidence in `plt-46-r1` (+4/-4), plus the `eng/test_desktop_rids.py` fix (+4/-2) and the `eng/policy/dependency-policy.json` mirror (+4/-4).

  The PR body also says (claimant-reported) that `d1bb49c` alone fails `eng/test_desktop_rids.py` and `61e11b7` fixes it, so that one commit is not bisect-clean.
- **ADP-07 supporting files** (observed in the diff; authorised by S52(2)/(3) and the record writes):
  - `.gitleaks.toml` and `eng/test_dependency_policy.py`;
  - `eng/test_desktop_rids.py`: the active-receipt pin moves from `nat-11-r1` to `plt-46-r1`, and the chain check now reads `plt-46-r1` → `nat-11-r1` → `gov-30-r1`, the NAT.11 precedent;
  - the three Security README status lines (Security, Security.Secrets and Security.Audit).
- **Packages are independent of WP13** (observed, `eng/packaging/packages.json` at `fb8577c3`). The four rows depend only on owned `ArcForges.Foundation`, `ArcForges.Security` and `ArcForges.Capabilities`, and on external `ArcForges.Contracts.Foundation 1.0.0-ci.216.1`. Security.Audit also depends on `Microsoft.Data.Sqlite 10.0.12`. Each row requires `lib/net10.0/<id>.dll`, `README.md`, `LICENSE`, `NOTICE.md` and `build-identity.json`. No row names ContentSandbox, Native, a parser or LocalRpcBoundary.
- **Independent review.** [Comment 6103643161](https://github.com/ArcForges/DesktopPlatform/pull/176#issuecomment-6103643161) (2026-10-11T00:13:29Z) records that reviewer `w-deku-20261010-rev-plt-46` (Opus 5.5) approved exact head `61e11b7570ba2009fe8dd10ee3239b03841e911c`. The comment is observed; its content is reviewer-reported:
  - every changed path is a record write or an ADP-07/S52 supporting file;
  - the receipt chains from `nat-11-r1` with unchanged closures;
  - the gitleaks block has the S52(2) form;
  - the pack metadata follows the Contributions pattern;
  - the gates were re-run in a fresh clone;
  - the reviewer's own clean consumer and gitleaks run were clean.

  Non-blocking items in the review:
  - the durable-audit defect (S60), which the reviewer reproduced independently;
  - stale "non-packable until PLT.46" ContentSandbox README lines, routed to fix8 and now owned by PLT.66;
  - a pre-existing Windows-only `TracePolicyTests` isolation race;
  - the pre-existing actionlint `queue` key.

  The PR author, the comment and the merge are under one GitHub account (`deku2026`), and the approval is a comment, not a review event (0 review events). Independence rests on the separate session.
- **PR CI** (observed). PR gate run [38097694269](https://github.com/ArcForges/DesktopPlatform/actions/runs/38097694269) (pull_request) at head `61e11b7570ba2009fe8dd10ee3239b03841e911c` concluded success, with all 22 checks passing:
  - allocate-version, design-policy, licence-policy, provenance-policy, reconciliation-policy, reference-policy, repository-hooks, runtime-policy, stage-integration, secret-scan and `ci`;
  - native-win-x64;
  - managed-packages `pack`;
  - the nine AOT jobs: Realtime, Generated gRPC-Web, Local RPC and Content helper compiles on linux-x64 and win-x64, plus the Avalonia TableView probe (compile only).

  The licence-policy job log shows `test_dependency_policy.py` "Ran 26 tests … OK", including:
  - `test_plt46_group_is_the_exact_successor_project_digest_block`;
  - `test_plt46_group_allows_only_the_active_lines_in_its_two_paths`;
  - `test_plt46_positive_controls_still_fire`.

  The same job runs `test_desktop_rids.py`. Other job log lines:
  - The PR pack job shows "Verified 21 package(s), version 1.0.0-ci.38097694269.1" (source `2b8851dc`, the PR merge ref).
  - The secret-scan job shows `fetch-depth: 0`, "427 commits scanned." and "no leaks found".
- **Merge** (observed). Merge commit `fb8577c3d026966368fd71189f370ea43b77ef73` on DesktopPlatform `main`, at 2026-10-11T01:57:58Z, by `deku2026`:
  - Its parents are `c8280488a1203a5c0160bebeba48ae5f20443f9c` (the previous main, the NAT.11 merge) and the reviewed head `61e11b7570ba2009fe8dd10ee3239b03841e911c`, so it is a merge commit, not a squash.
  - The `--match-head-commit 61e11b75` flag is coordinator-reported.
  - The merge was made under `integration:DesktopPlatform`. Plan `roles/integration-desktopplatform` at `52f8df838309742f277792f6c1dfefd268988aad` shows epoch 2, claimant `w-deku-20261010-coord`, claimed 2026-10-11T01:57:40Z.
  - `fb8577c3` is the current DesktopPlatform `main` at this reading.
- **Main-push publication** (observed). `Publish NuGet` run [38103586975](https://github.com/ArcForges/DesktopPlatform/actions/runs/38103586975) (#131, attempt 1, push to `main` at `fb8577c3`) concluded success, with 24 of 24 jobs succeeding.
  - Pack job 114365158353 (`candidate / managed-packages / pack`):
    - 21 distinct "Successfully created package" lines at `1.0.0-ci.131.1`, including `ArcForges.Security`, `ArcForges.Security.Audit`, `ArcForges.Security.CapabilityEnforcement` and `ArcForges.Security.Secrets`;
    - "Verified 21 package(s), version 1.0.0-ci.131.1, source fb8577c3d026966368fd71189f370ea43b77ef73.";
    - the `eng/packaging` unit tests: "Ran 31 tests … OK".
  - publish job 114366554148, step "Publish the same verified bytes": 21 "Your package was pushed." lines to `https://www.nuget.org/api/v2/package`, including the four Security pushes at 02:12:30Z to 02:12:33Z, each followed by `Created` and "Your package was pushed.".
  - The candidate secret-scan job 114364401951 ran pinned `ghcr.io/gitleaks/gitleaks:v8.30.1@sha256:c00b6bd0aeb3071cbcb79009cb16a60dd9e0a7c60e2be9ab65d25e6bc8abbb7f` and logged "427 commits scanned." and "no leaks found".

  No registry was queried and nothing was downloaded, so indexing and resolution on nuget.org rest on these log lines.
- **Obligation** WP-11.90, the part named by the record: full for the four Security packages. They are packed, admitted (receipt `plt-46-r1`), published in the lockstep cohort `1.0.0-ci.131.1`, and consumed by a clean local consumer from the locally packed candidate (see below). Packaging the signed parent-bound helper, the OS broker and the per-RID helper runtime is out of scope under P2-026 item 20 and S52(1), and is not completed. `ArcForges.Security.LocalRpcBoundary` stays non-packable.
- **Clean-consumer and local evidence** (claimant-reported in `plt-46-r1` `upgradeChecks`; the reviewer reports running an own clean consumer and gitleaks, both clean):
  - **Consumer setup.** One local opt-in console consumer outside every checkout. Its own `NuGet.config` resolves only the six owned ids from the candidate directory, and everything else from nuget.org. It runs a locked restore into a fresh package folder, with warnings as errors. The restored owned packages are byte-identical to the candidate packed at source `d1bb49cb` (version `1.0.0-ci.local.46`).
  - **Runs.** Under the JIT (.NET 10.0.11, Windows 10.0.26300 x64) and as a Native AOT win-x64 executable (SDK 10.0.400, ILCompiler 10.0.11, 0 warnings), 136 of 136 checks passed through the package boundary. They cover:
    - **owner refusal through the gate:** cross-boundary owner refusal through `CapabilityEnforcementGate` over the real `CapabilityInvocationPipeline`. The owner's final validation refuses before the owner runs. An unregistered capability or another owner's capability is refused before evidence. The gate-wrapped operation refuses without an admission;
    - **stale approval and lease revocation:** a changed resource revision, a revoked lease and an aged service decision are each refused at the owner's validation. An approval for a different effect or an expired approval is refused, and a fresh exact approval succeeds;
    - **egress:** decided and audited by the real `EgressAuthority`;
    - **secrets:** `SecretBroker` grants use without revealing the value, redacts references and refuses foreign or revoked grants;
    - **audit:** a real `AuditStore` with `EgressAuditSink` and `CapabilityLeaseEventAuditSink` is read back from a second instance, and a disposed store refuses the transfer and the lease issue (`AuditUnavailable`, `resource.unavailable`).
  - **Real and fixture parts.** The policy, identity, scope, permission and resource sources, the trust facts, the stores and the classifier are fixtures written for the run. The Windows Credential Manager was used through the explicit local opt-in.
  - **Local gates** (Windows, pinned SDK 10.0.400, through the build slot):
    - the locked restore, `dotnet format` and a Release build were clean;
    - ArchitectureTests passed 134 of 134, with one hosted-only test excluded;
    - Capabilities.Tests 77/77, Security.Tests 920/920, Security.Audit.Tests 47/47, and Security.Secrets.Tests 34 passed and 2 skipped (the Credential Manager opt-in);
    - a pack at `d1bb49c` produced nuspec dependency sets equal to the catalogue rows;
    - a full-history gitleaks scan (pinned image, WSL Docker) found 0 (claimant-reported in the PR #176 body, not in the receipt `upgradeChecks`).
  - **Finding (S60).** Registry capability keys such as `IChatOperations.AppendUserMessage` are not canonical `AuditCapabilityId` keys. With the durable sinks behind the gate, an allowed egress of a registry capability is refused (`decision.s08.unavailable`, owner not run, no row), and a lease issue is refused with `AuditUnavailable`. The composition fails closed, and durable audit of registry capabilities is not proven.
- **WP-11 package-acceptance statement (S52(4))** (observed on Plan `main` at `e327eb69`):
  - PLT.36, PLT.37, PLT.38, PLT.39, PLT.41, PLT.42 and PLT.43 are `complete`.
  - PLT.40, PLT.44, PLT.45 and PLT.57 are `delivered`, not complete.
  - PLT.66 has no ledger record and no claim branch.
- **Substitutes still in use:** none in the packages. The consumer's fixtures above are run-local, not shipped.

## Scope (2026-10-11)

- **Rulings applied:**
  - S52 (1) to (4);
  - S57(7), through fix8;
  - S60, S61(6) and S62(1): the fix is owned by PLT.66, and PLT.46 has a completion edge on PLT.66;
  - the merge-order rules of the fix8 delta notes. PLT.46 merged first among PLT.46, PLT.66 and NAT.01, so PLT.66 and NAT.01 rebase on this receipt, gitleaks block and `active-projects.json` rows.
- **APP.03 and APP.02 part B** consume the four packages only from this main-push candidate (`1.0.0-ci.131.1`, run 38103586975 at `fb8577c3`) or a later DesktopPlatform main candidate. The rolled-back `1.0.0-ci.110.1` to `1.0.0-ci.124.1` versions are never admitted (S53(1)). Combining these packages with `ArcForges.Contracts.LocalRpc.Scope` 324.1 or later still needs the PLT.66 Contracts move (S56(1)), because the cohort pins `ArcForges.Contracts.Foundation 1.0.0-ci.216.1`.
- **Out of scope, not completed:** packaging of the signed parent-bound helper, the OS broker and the per-RID helper runtime (S52(1)).

## Untested coverage (stated expressly)

- **Published bytes in a consumer:** the clean consumer used bytes packed locally at `d1bb49cb`. The hosted candidate was built from `fb8577c3` on Linux and published as `1.0.0-ci.131.1`, and no consumer has restored those bytes. Blocked on a consumer run against the published cohort (the PLT.46 completion follow-up on the PLT.66 cohort, or APP.03), not proven.
- **OS isolation:** cross-referenced from PLT.45 and not re-run here. Windows (AppContainer and Job Object) is observed only in the PLT.45 record, at `9d26125`, before the helper changed. Linux is blocked on a real Linux-kernel run of the PLT.45 profile, not proven. win-arm64 is blocked on a Windows ARM64 host, not proven (PLT.45 graph note). macOS is never claimed (P2-023).
- **Durable audit of registry capabilities:** blocked on the PLT.66 audit-identity fix (S60), not proven. At `61e11b75` that leg fails closed.
- **Native AOT of a consumer:** win-x64 only (claimant-reported). Native AOT on linux-x64 or any other RID is blocked on a consumer publish on that RID, not proven. The hosted AOT jobs are compile-only for other projects.
- **Product host:** no product host composes the gate with the durable sinks. Blocked on APP.03, not proven.
- **Other checks:** a second Windows account is blocked on the section 0e user deferral, not proven. Performance is not measured.
- **Local gates and the consumer run:** claimant- and reviewer-reported. This author re-ran none of them.
- **Independence:** one GitHub account, so independence rests on the session. The merge flag text is coordinator-reported.

## Remaining completion prerequisites and next action

1. **PLT.45 to `complete`** (integration edge): real OS denial and parent-death cleanup of the content helper observed on every supported RID. Open: PLT.45 is `delivered`. Its graph notes set the follow-up's acceptance: a Windows re-run at the recorded head, a Linux run in local WSL2 (blocked on a real Linux-kernel run of the PLT.45 profile with multithread Landlock, not proven), and win-arm64 blocked on a Windows ARM64 host, not proven. NAT.14 is no longer part of it (out of scope; S1, S8). *Next action:* the PLT.45 completion follow-up.
2. **PLT.66 to `complete`** (integration edge): the PLT.66 cohort carrying the S60 registry-key-to-`AuditCapabilityId` mapping in `ArcForges.Security.Audit`. Open: PLT.66 is unclaimed and waits on CON.43. *Next action:* PLT.66 delivers its cohort.
3. **PLT.46 completion follow-up (epoch 2)**, after both edges are complete. It re-runs the durable-audit consumer leg on the PLT.66 cohort: Security.Audit and CapabilityEnforcement, with the durable egress and lease sinks behind the gate, using registry keys. It also runs the clean consumer against the published bytes and cites PLT.45's completed isolation matrix. The WP-11 package acceptance stays open while PLT.40, PLT.44, PLT.45 and PLT.57 are delivered, not complete.
4. **Claim:** after this record merges, the coordinator sets `claims/plt-46` epoch 1 to `delivered`.
