---
task: CLOUD.72
status: delivered
recorded: 2026-10-11
claimant: w-deku-20261010-cloud-72
epoch: 1
---

# Identity production store, identifier source and enrollment family call over the plan-execution port

The store, the identifier source, the family-execution port, the Workspace read port and the replay mapping are merged, deployed with the production image and green in hosted CI. The status is `delivered`, not `complete`. The outcome says "The Identity service is registered by composition and resolves", and today that holds only in a composition that binds the plan executor. Production resolution is blocked on the production business composition (CLOUD.87: plan executor and recovery generation), not proven. The graph lists no completion prerequisite for CLOUD.72 (`complete: []`). CLOUD.20 is the task that completes on CLOUD.72.

How to read this record:
- **Observed** facts were checked by this author on GitHub with `gh`: pull requests, comments, merge commits, workflow runs and their job conclusions, log lines grepped for specific results, and release metadata. No artifact was downloaded and no secret was printed.
- **Claimant-reported** facts come from the PR body or the merged docs, which the claimant wrote.
- **Reviewer-reported** facts come from the independent review comment on the PR.
- **Coordinator-reported** facts are visible neither in GitHub text nor in a log line.

## Evidence

- **Claim** (read from `claims/cloud-72` at `731a10f0c64fd3c7c2aaf04825bae9ae1d4d8761` with `tools/delivery.py show`):
  - CLOUD.72, epoch 1, claimant `w-deku-20261010-cloud-72`, claimed 2026-10-10T20:02:18Z, state `claimed`.
  - Handoff: head and reviewed are both `0516e95d3a5ef7a4aada69fe7589fde828bacc0e`, and the merge is `92ba1dc9603779943b18bb121687b048a4e77dc1`.
  - Coordinator-reported: the claim is coordinator-held for a local-only Opus 5.5 agent.
  - The handoff has two recording defects. Its `worktree` value is `C:\MyFile\Projects\ArcForges$3\.worktree$4`, an unexpanded substitution. Its `branch` is `Cloud:task/cloud-72`, which `show` prints as `Cloud:Cloud:task/cloud-72`. This ledger PR does not change the record branch.

- **Planning** (observed):
  - Planning repair fix8a, under coordinator ruling S54, re-specified the write scope:
    - [Design #349](https://github.com/ArcForges/ArcForges-Design/pull/349): head `426ff44c5366b440f4101f2deed502530a449d7e`, merged as `43158b85e46630321cc62200223ed3002f6af7ad` at 2026-10-10T20:33:59Z.
    - [Plan #478](https://github.com/ArcForges/Plan/pull/478): head `741a533aaa13534addee9020fea916aed9390231`, merged as `564d91c057ce2560f502351f2111fa3b0a657a47` at 2026-10-10T20:34:03Z.
  - What fix8a added:
    - the three identity read plans and the two workspace read plans;
    - the primitives-only Workspace read port in Abstractions and its Workspace-module implementation;
    - exactly two `IdentityError` members (S54(2));
    - the S54(3) production-resolution limit;
    - the S54(6) realm-level allowlist rows;
    - the outcome text "No new table or migration is added".
  - The later planning repair fix8 assigned CLOUD.87 (production business composition) as the owner of the production plan-executor composition, and appended a CLOUD.72 pointer note. No acceptance, write or edge changed (S57(14)).
    - [Design #350](https://github.com/ArcForges/ArcForges-Design/pull/350): merged as `f4b2299c1b57fb8a9905b9463680cc7bc4686687` at 2026-10-11T01:56:16Z.
    - [Plan #479](https://github.com/ArcForges/Plan/pull/479): merged as `f7cb511a4b58f8d93aec34cd06a19c2e2317e2da` at 2026-10-11T01:56:22Z.
  - CLOUD.87 starts on CLOUD.72. It is not a prerequisite edge of CLOUD.72.

- **Implementation** (observed):
  - Cloud [PR #90](https://github.com/ArcForges/Cloud/pull/90), "[CLOUD.72] Identity production store, identifier source and enrollment family port", head branch `task/cloud-72`, author `deku2026`.
  - It merged at head `0516e95d3a5ef7a4aada69fe7589fde828bacc0e` as `92ba1dc9603779943b18bb121687b048a4e77dc1` on `main` at 2026-10-11T01:44:32Z.
    - The merge commit has two parents: `c291550f73ba64cb9fa4c15d4ec0e731a27dede8` (the previous main) and `0516e95d`. That is consistent with a merge commit, not a squash.
    - Its subject is "[CLOUD.72] Identity production store, identifier source and enrollment family port (#90)".
    - Coordinator-reported, not visible in the PR text: the `gh pr merge --merge --match-head-commit 0516e95…` flags and the `integration:Cloud` role holder, `w-deku-20261010-coord`.
  - The merge changes 55 files (15820 insertions, 67 deletions) in eight commits:
    - `e844e80`: the Abstractions family-execution port (`IModuleFamilyPort`, `IModuleFamilyPortFactory` in `src/ArcForges.Cloud.Modules.Abstractions/Families/ModuleFamilyPort.cs`) and the Storage.D1 FamilyBinding adapter (`FamilyBinding/ModuleFamilyPortFactory.cs`, `FamilyContributionPolicy.cs`). It carries the one reviewed exception: identity contributes the `workspace` statements in `account-enrollment` only.
    - `ac97f64`: the read plans `storage/plans/identity/{credential-get,credential-rows,recovery-active}.sql` and `storage/plans/workspace/{workspace-get,workspace-by-owner}.sql`, plus the regenerated `PlanManifest.g.cs` and `worker/storage/plans.generated.ts`. The CLOUD.11 plans, the tables, the migrations and `families.json` are not in the diff.
    - `7dafdd4`: the replay mapping in `Core/Application/IdentityService.cs` and `Ports.cs`, and the two `IdentityError` members `IdentifierConflict` and `ReceiptExpired` in `Core/Domain/IdentityRules.cs` (6 added lines, nothing removed).
    - `12e7ef8`: the Workspace read port (`Abstractions/Workspace/WorkspaceDirectoryPort.cs`, `IWorkspaceDirectory`), its implementation `Modules.Workspace/Persistence/D1WorkspaceDirectory.cs`, and the `WorkspaceModule.cs` Register entry.
    - `751c954`: `Modules.Identity/Persistence/{D1IdentityStore,IdentityPlans,IdentityRowCodec,RandomIdentityIdSource}.cs`, the `IdentityModule.cs` registration, the `HostModules.cs` append (`ModuleFamilyBindingModule`, beside `ModulePlanBindingModule`) and the store suites.
    - `60be465`: the transcript mode of the opt-in workerd run in `eng/verification/d1-identity-local.ts`. `package.json` is unchanged.
    - `ef15860`: docs (`docs/identity-core.md`, `docs/shared-families.md`, `docs/storage-plans.md`, `AGENTS.md`).
    - `0516e95`: release profile `eng/provenance/artifact-profiles/cloud-release-r51.json` and the successor records described next.
  - Provenance records (observed in the merged files):
    - `cloud-72-cloud-runtime-notices-r1` supersedes `cloud-84-cloud-runtime-notices-r5`. Its image closure is 211 inputs (r50 had 202).
    - `cloud-72-cloud-worker-bundle-r1` supersedes `cloud-84-cloud-worker-bundle-r5`. The production Worker bundle is unchanged: 92603 bytes, sha256 `14f6a5dfabce25250fb26e664e3b029f7ca63f59a6f1b41e7fa20e56cd9715e8`, which is the r51 `worker.sha256`.
    - Each record carries the S25 review fields: reviewer `w-deku-20261010-rev-cloud-72`, `decision: approved`, `reviewedOn: 2026-10-11`, baseline `ef158607aaa1ddda7142c82540200887ac204995`.
    - `eng/policy/dependency-policy.json` changes one line: `artifactRecords` now names the two successors.
    - `tests/worker/release-provenance.test.ts` is not in the diff, so the S29 pin is unchanged, consistent with the unchanged bundle.
  - Dependency receipt: none. No `eng/policy/dependency-reviews/cloud-72-*.json` was added, and no package lock or project file changed. The claimant reports that `check:dependencies` passes, which is the S54(5) and S44(2)(f) condition. The hosted `npm run check` step, which includes it per the PR body, succeeded.
  - ADP-07 supporting files, outside the literal writes. They are listed in the PR body, and the reviewer accepted them as non-blocking:
    - `.dockerignore` (6 lines): allowlist entries for `Abstractions/Families`, `Abstractions/Workspace` and `Storage.D1/FamilyBinding`, the S45(5) precedent, bound in r51;
    - `tests/ArcForges.Cloud.Tests/Reduction/StoragePlanOwnershipTests.cs` (1 line): the exact owner-set assertion gains `workspace`, which makes it stricter.
  - The S54(6) rows in `StoragePlanGeneratorTests.cs` name exactly `identity.credential-get`, `identity.credential-rows`, `identity.recovery-active` and `workspace.workspace-by-owner`. `workspace.workspace-get` binds the workspace id as its scope and is not exempt. The new test `EveryRealmLevelExemptionNamesAnExistingPlanThatCarriesNoScope` refuses an exemption that hides a scoped plan or names a missing one.

- **Review trail** (observed): PR #90 has no GitHub review events and one comment, [6104237613](https://github.com/ArcForges/Cloud/pull/90#issuecomment-6104237613) (2026-10-11T01:34:14Z). It records "Reviewed 0516e95d3a5ef7a4aada69fe7589fde828bacc0e for [CLOUD.72] epoch 1: approved", an independent exact-head review by the session `w-deku-20261010-rev-cloud-72` (Opus 5.5).
  - Reviewer-reported findings:
    - the store, identifier source, family port with its one exception, Workspace read port, replay mapping, receipt-probe design and two `IdentityError` members are real implementations, not stubs;
    - production resolution and the provider D1 run are recorded as blocked, not proven;
    - the r51 image digests were re-derived independently (211 inputs match the git blobs; 9 added and 8 changed against r50);
    - the earlier records are untouched, and the S29 pin is unchanged;
    - no architecture or security rule is weakened;
    - the realm-level exemptions are exact and tested both ways.
  - Non-blocking notes:
    - the ADP-07 files above;
    - the `docs/identity-core.md` plan count is stale (now eleven plans, six reads); line 23 still says "Eight named plans";
    - a `RevokeCredential` replay fallback instant in a rare concurrent anomaly;
    - the brief numbering of S54(6), which sits under S55 in the brief.
  - The PR author, the approving comment and the merge are all under the one GitHub account `deku2026`. Independence rests on the separate reviewer session only.

- **Hosted runs** (all in `ArcForges/Cloud`; job conclusions read with `gh run view --json jobs`):
  - **PR CI run** [38102272282](https://github.com/ArcForges/Cloud/actions/runs/38102272282) (pull_request, head `0516e95d`, 2026-10-11T01:34:11Z to 01:42:48Z) succeeded.
    - Successful jobs: Source (ubuntu-latest), Source (windows-latest), Native AOT image and Worker build, Dependency audit and repository checks, Dependency review, CodeQL (actions, csharp, javascript-typescript) and Verify.
    - Skipped on the PR: Deploy Cloudflare, Deploy Cloudflare proof environment, Proof Cloudflare access and resources.
    - Log lines grepped from Source (ubuntu-latest), job 114360480145 (steps `npm run check` and `npm run check:dotnet`):
      - `tests 757`, `pass 757`, `fail 0`;
      - `Build succeeded.`, `0 Warning(s)`, `0 Error(s)`;
      - dotnet test summary `total: 1891`, `failed: 0`, `succeeded: 1890`, `skipped: 1`.
    - Source (windows-latest) compiles the managed solution only. Its `npm run check` steps are skipped by design.
    - The hosted architecture gate (`EvaluatedRepositoryGate`, in job 114360480117) reports `total: 2`, `succeeded: 2`. `npm audit` reports `found 0 vulnerabilities`.
    - The gate binds the new public APIs to contract tests:
      - `IModuleFamilyPort.ExecuteAsync` and `IModuleFamilyPortFactory.For` to `Families.ModuleFamilyPortTests`;
      - `IWorkspaceDirectory.FindAsync` and `FindByOwnerAsync` to `WorkspaceDirectory.WorkspaceDirectoryTests`.
  - **Main-push CI run** [38102843509](https://github.com/ArcForges/Cloud/actions/runs/38102843509) (push, head `92ba1dc9`, 2026-10-11T01:44:35Z to 01:53:39Z) succeeded.
    - Successful jobs: both Source jobs, the three CodeQL jobs, Dependency audit and repository checks, Native AOT image and Worker build, Verify and Deploy Cloudflare (job 114363516238).
    - Skipped on the push: Dependency review, Deploy Cloudflare proof environment, Proof Cloudflare access and resources.
    - The deploy job logged:
      - `migration step: not applicable (production declares no D1 database; there is nothing to migrate)`;
      - `ci.361.1: digest: sha256:062a28823f6c447ef9c896417028580ecfa88c2371e469b5f1b5c5e4dcf24c80`;
      - `Pushed image: …/arcforges-cloud:ci.361.1`;
      - `Current Version ID: 200b016e-818e-430e-912b-4e773334e390` (the production Worker version);
      - the release URL `…/releases/tag/cloud-0.1.0-ci.361.1`.
  - **Release** `cloud-0.1.0-ci.361.1`, read with `gh release view` by metadata only: prerelease, not a draft, target `92ba1dc9603779943b18bb121687b048a4e77dc1`, published 2026-10-11T01:53:35Z. Assets: `cloud-0.1.0-ci.361.1.tar.gz` (67904094 bytes) and `deployment.json` (431 bytes).
  - **Production** `GET https://arcforges.com/api/healthz`, read by this author at 2026-10-11T02:06Z, returned:
    - `revision` `92ba1dc9603779943b18bb121687b048a4e77dc1`, `nativeAot` true;
    - `artifact.version` `0.1.0-ci.361.1`, `build.buildId` `38102843509.1`, `build.dirty` false.

- **Obligation:** WP-22.00, the CLOUD.72 part: the production persistence and identifier binding of the core identity model.
  - Delivered:
    - the internal D1 `IIdentityStore`, written only against the Abstractions plan-execution port and the new family port;
    - the CSPRNG version 4 `IIdentityIdSource`;
    - the replay and reused-identifier mapping to the service result.
  - The model, the rules, the CLOUD.11 plans and the family stay with CLOUD.11.
  - Exception: the service-resolution part of the outcome holds only in the executor-binding composition (see Scope).

- **Validation against the record's clauses.** These are the C# test classes at `92ba1dc9`. They ran inside the hosted dotnet totals above. This author did not grep per-test results.
  - **Store on plan-port fakes and the SQLite oracle over the real migrations.** `IdentityStoreUnitTests` covers the fakes. `IdentityStoreOracleTests` covers the oracle:
    - `AnEnrollmentCommitsItsRecordsWithTheTailAndEveryReadReturnsThemOnlyInTheirRealm`;
    - `PasskeyAndPasswordCredentialsRoundTripWithTheirMaterial`;
    - `RelabelRenameAndRevokeCommitWithTheirRevisionsAndTheLastCredentialNeedsARecoveryPath`;
    - `ARefusedGuardCommitsNothingNotEvenAReceipt`;
    - `TwentyFiveConcurrentEnrollmentsOfOneCredentialCommitOnce`;
    - `AnUnavailableOrStaleStoreIsATypedFailureAndWritesNothing`.
  - **Enrollment through the family port to the real family plan.** `Families/ModuleFamilyPortOracleTests`:
    - `AnEnrollmentCommitsTheRecordsTheReceiptTheOutboxAndTheChangeRecordTogetherAndReleasesItsGuards`;
    - `ConcurrentEnrollmentsOfOneCredentialCommitOnce`;
    - `AStaleRecoveryGenerationCommitsNothing`.
  - **Identifiers.** `RandomIdentityIdSourceTests`:
    - `EveryIdentifierIsACanonicalVersionFourUuidTheModelAccepts`;
    - `AHundredThousandDrawsNeverRepeat`;
    - `IdentifiersAreNeitherOrderedNorSteppedLikeACounter`.

    Forced collisions, in the oracle suites:
    - `AnEnrollmentWhoseRandomUserIdentifierExistsIsRefusedWholeAndRetriedWithFreshIdentifiers`;
    - `AUserIdentifierHeldInAnotherRealmMeetsThePrimaryKeyAndIsRetriedWithFreshIdentifiers`;
    - `AnAddedCredentialWhoseRandomIdentifierExistsIsRetriedWithAFreshOne`;
    - `ACollidingIdentifierIsRefusedWholeNeverOverwritten`.
  - **Replay mapping.** `IdentityReplayMappingTests`:
    - `IdentityErrorGainsExactlyTheTwoReplayRefusalsAndKeepsEveryExistingMember`;
    - `ConcurrentIdenticalEnrollmentsUnderOneCommandCreateOnceAndTheOtherReplaysAsAnExistingUser`;
    - `AnEnrollmentCommandReusedForAnotherCredentialIsRefusedAndWritesNothing`;
    - `AnEnrollmentReplayPastTheReceiptWindowIsRefusedAndNeverExecutedAsNew`;
    - `AnOutcomeThatStaysUnknownIsResentOnlyAsTheIdenticalCommandAndThenReportedAsAConflict`;
    - the receipt-probe cases (S54(4)).

    On real receipts, in the oracle suites:
    - `ACommitWhoseResponseAndReconciliationWereLostIsResentIdenticallyAndReplaysFromItsReceipt`;
    - `AReceiptWhoseWindowPassedBeforeTheResendIsAnExpiredRefusalAndNothingRunsAgain`;
    - `ACommandIdentifierReusedForAnotherRequestIsAConflictAndWritesNothing`;
    - `AReplayOfTheSameCommandIsAnsweredFromItsReceiptAndExecutesNothing`;
    - `AnExpiredReceiptIsNeverExecutedAsANewCommand`;
    - `AnUnknownOutcomeWithoutAReceiptIsUnknownAndOnlyTheSameCommandIsSentAgain`.
  - **Family port contract.** `ModuleFamilyPortTests`:
    - `AnUnknownFamilyOrAPlanOfAnotherFamilyIsRefusedBeforeTheExecutor`;
    - `ACallerThatIsNotAParticipantIsRefusedBeforeTheExecutor`;
    - `AStatementOfAnotherModuleIsRefusedForEveryCallerOtherThanTheOneReviewedException`;
    - `APlatformStatementIsNeverContributedByAModule`;
    - `TheReviewedExceptionIsOneRowForIdentityContributingWorkspaceInAccountEnrollmentOnly`;
    - `TheExceptionDoesNotHoldInAnotherFamilyWithTheSameParticipantsAndShape`;
    - `EveryExecutorAndReceiptOutcomeBecomesATypedStatusAndNothingIsRetried`.
  - **Architecture.** `IdentityStoreArchitectureTests`:
    - `TheIdentityProjectReferencesOnlyTheAbstractionsProject`;
    - `TheIdentitySourcesReachStorageOnlyThroughTheAbstractionsPorts`;
    - `TheIdentityStoreIsImplementedOnlyByTheD1StoreAcrossTheProductionSources`;
    - a planted-violation scanner test.

    `FamilyPortArchitectureTests`:
    - `ThePortIsPublishedInTheAbstractionsProjectFromPrimitivesOnly`;
    - `OnlyTheFamilyBindingAdapterImplementsThePort`;
    - `TheAdapterReferencesNoModuleAndHoldsNoSqlOrTableName`.
  - **Read plans and the Workspace read port on the SQLite bridge.**
    - `IdentityReadPlanTests`: realm, provider and subject scoping; overload refused, never truncated; the recovery predicate equals the revoke guard; the cross-owner refusal before the executor.
    - `WorkspaceReadPlanTests`: `WorkspaceGetIsScopedByRealm`, `WorkspaceByOwnerIsScopedByRealmAndOwner`.
    - `WorkspaceDirectoryTests`: realm and owner refusals; malformed identifiers refused before any plan call.
  - **DI resolution.** `IdentityCompositionTests`:
    - `UnderTheFoundationConfigurationTheHostResolvesTheServiceOverTheD1StoreAndServesAnEnrollment` (the executor-binding composition);
    - `WithoutTheFoundationConfigurationTheServiceIsListedButNothingResolvesIt` (the production-shaped composition does not resolve).
  - **No CLOUD.11 assertion loosened.** Observed by this author from the PR file patches:
    - the CLOUD.11 test files changed only in `IdentityStatementTests.cs`, where four members move from `private` to `internal` (no assertion line changes);
    - `IdentityHarness.cs` changed, in its test double `InMemoryIdentityStore`: it now models command receipts and outcome scripting, and its `HasActiveRecoveryPathAsync` takes a `RealmId`, following the port signature change in `Ports.cs`;
    - the TypeScript oracle `identity-core-oracle.test.ts` and the vector `identity-plan-calls.json` are not in the diff.

    This author did not assess whether any CLOUD.11 case now runs through a different path in the extended double. The reviewer reports that no rule is weakened.
  - **Opt-in local workerd run** (claimant-reported, recorded once). `docs/identity-core.md` line 126 at `92ba1dc9` reads: "The local run of 2026-10-10 answered 142 calls in 116 steps as recorded."
    - The run executes the C#-built calls of `Identity/Vectors/identity-store-transcript.json` through the production Worker executor on workerd's D1 and compares them generically, with no TypeScript business assertion. `IdentityStoreTranscriptTests` regenerates and checks that transcript in hosted CI.
    - This author did not re-run it, and the review comment does not say it was re-run. It is not a Cloudflare result.

- **Local evidence** (claimant-reported in the PR body; the reviewer reports re-running the gates "in a fresh clone under CI conditions" and refers to the PR body):
  - dotnet build 0 warnings; dotnet test 1890 passed and 1 skipped (pre-existing HAR.00); the coordinator reports 1891 in total, the hosted figure; dotnet format clean;
  - `npm run check` sub-steps run individually: locked restore, test:dependencies, check:plans, check:physical, policy, licence, provenance, check:generated, format, lint, typecheck, npm test 757/757, check:dependencies. Only the toolchain-pin step fails locally (Node 24.20 against the 24.21 pin); the hosted job is the authority;
  - hosted architecture gate 2/2, CodeQL build, npm audit 0, actionlint clean, gitleaks 0 findings over 376 commits;
  - test:artifact 10/10 (S29 pin unchanged); proof Worker dry-run passed;
  - the Native AOT Dockerfile build stage passed in WSL Docker. The coordinator reports an 18,610,872-byte binary, a figure visible in no GitHub text;
  - WSL2 Linux leg: build and format pass. 325 test failures, all caused by node and python missing in WSL. The hosted ubuntu job is authoritative and green.

- **Prerequisite records** on Plan `main`:
  - CLOUD.11 `complete`, COM.16 `complete` and CLOUD.04 `complete`.
  - CLOUD.06 is `delivered`: its completion waits on CLOUD.63. It is a start edge of CLOUD.72, and the enrollment call runs on its engine as delivered.
  - COM.16's record names the production wiring gap that S54(3) and CLOUD.87 now own.

## Scope and status (2026-10-11)

- **Delivered outcome.** Everything below is merged at `92ba1dc9` and part of the production image `ci.361.1`, Worker version `200b016e-818e-430e-912b-4e773334e390`.
  - The production `IIdentityStore` (`D1IdentityStore`, internal; no SQL text, no table name, no Storage.D1 reference).
  - The CSPRNG version 4 `IIdentityIdSource`.
  - The generic Abstractions family-execution port and its Storage.D1 FamilyBinding adapter, with the one reviewed workspace exception.
  - The Workspace read port with its Workspace-module implementation.
  - The five read plans.
  - The replay, reused-identifier, expired and unknown-outcome mapping.
  - The two new `IdentityError` members.
  - The production host serves no Identity method, and production declares no D1 database (deploy log above).
- **Why `delivered`.** The outcome clause "The Identity service is registered by composition and resolves" is met only in a composition that binds the plan executor (`IdentityCompositionTests`). Each open item is named:
  1. **Production resolution of the Identity service:** blocked on the production business composition (CLOUD.87: plan executor and recovery generation), not proven. *Next action:* CLOUD.87 binds `IPlanExecutor` and the recovery generation in production. This record is then updated to `complete` in a follow-up citing the production resolution result.
  2. **Live provider D1 run** (the store's plan calls through the deployed Worker, the enrollment batch at provider limits, concurrent enrollments on the provider): blocked on the production business composition (CLOUD.87), the `RES-cloud-deployment` lease and a proof environment, not proven. The opt-in workerd run is the closest local engine, not a Cloudflare result. The record's validation forbids a hosted runtime or live-service CI run (P2-017), so this item is recorded, not owed as a CI step.
- **Completion edges:** none (`complete: []`). CLOUD.20 completes on CLOUD.72.
- **Claim follow-up** (coordinator): move `claims/cloud-72` to `delivered` and correct the handoff `worktree` and `branch` values noted under Evidence.

## Untested coverage (stated expressly)

- **Production resolution:** blocked on CLOUD.87, not proven. Resolution is proven only in the DI test of the executor-binding composition.
- **Cloudflare D1:** blocked on CLOUD.87, the `RES-cloud-deployment` lease and a proof environment, not proven. SQLite and workerd are not D1.
- **Workerd run:** one local run, claimant-reported (142 calls, 116 steps). It was not re-run by this author or, as far as the review text shows, by the reviewer.
- **Local gate figures:** claimant- and reviewer-reported and not re-run by this author. The hosted figures above are the observed ones. The 1891 total and the 18,610,872-byte AOT binary are coordinator-reported.
- **Per-test hosted results:** not grepped. Only the suite totals were read.
- **Reviewer's non-blocking notes, carried for a later task:**
  - `docs/identity-core.md` line 23 still describes eight identity plans (now eleven, six of them reads);
  - a `RevokeCredential` replay fallback instant in a rare concurrent anomaly.
- **Correlation and change-record version:** the commit context uses the command identifier as the correlation, with no causation, and a constant change-record schema version 1 (the COM.16 precedent, stated in `docs/identity-core.md` "Not claimed").
- **Independence:** the PR, the approval and the merge are under one GitHub account (`deku2026`). Independence rests on the reviewer session `w-deku-20261010-rev-cloud-72`.
- **Coordinator-reported facts:** the claim holder arrangement, the merge flags and the `integration:Cloud` role. The two-parent merge commit is verified.
