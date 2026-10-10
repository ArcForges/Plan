---
task: CLOUD.84
status: delivered
recorded: 2026-10-10
claimant: w-deku-20261009-cloud-84
epoch: 1
---

# Cloud TypeScript reduction: C# generated tables and policy, thin Worker adapters, proof code out of the production bundle

## Evidence

- **Implementation, in one Cloud pull request** (brief S20(e), with D1 to D16 and D6 as amended by S41; rulings S29, S33 to S35 and S38 to S46):
  - Cloud [PR #83](https://github.com/ArcForges/Cloud/pull/83), "[CLOUD.84] Cloud TypeScript reduction: thin Worker adapter, C# decisions and generated tables", head branch `task/cloud-84`, was reviewed and merged at head `ffd9cea5b9d40b9a01a3d47683af890edbabb14c` as `837fb29f2509b1fa7117948dbd48fa9f805bd502` on `main` at 2026-10-10T10:31:46Z. The merge commit has two parents, `3c59ce34413c94c86ce400fd2950b6372d45abbd` (the previous main, the CLOUD.85 follow-up merge) and `ffd9cea5`. This is consistent with the `--merge` method (verified from the commit). The `--match-head-commit ffd9cea` flag and the `integration:Cloud` role, held by `w-deku-20261008-coord`, are coordinator-reported. Neither is visible in the PR text.
  - The PR has 42 commits, including one merge of `origin/main` (`8c9ca1f`). The merge changes 211 files (22098 insertions, 7965 deletions) against `3c59ce34`. The `wrangler.json` change is one line: `env.proof.main` is set to `worker/proof/entry.ts` (U6, D1). The production configuration, bindings, migrations and vars are unchanged. `.github/workflows/ci.yml` loses the Kotlin gate steps (U1) and gains a pinned `setup-dotnet` step in the candidate job (S41(3)).
  - The status is `delivered`, not `complete` (D13). See Scope for the open completion prerequisites.
  - The PR body predates the three hosted-fix commits (`88cdf70`, `b624943` and `ffd9cea`) and was not updated after them. Its stale lines, read by this author:
    - it says the probe publish is "single-file, with snapshot and restore of the reviewed tool lock", but `ffd9cea` replaced that approach with one non-single-file sealed tool archive (see U2 and the hosted failures below);
    - it names release profile successors `r46` to `r49`, but `b624943` added `r50`;
    - its "Carried" list still names the two proof-route refusal values, which `88cdf70` fixed (see residual 5).

    The commits and the review comments at each head are the authority.

- **Units, with commit SHAs and what each delivered** (Cloud `task/cloud-84`, merged in `837fb29f`; each commit message was read by this author):
  - **U1, Kotlin consumer gate removed** (after AND.40 PR B merged, Mobile `6702e281` at 2026-10-09T15:41:24Z; the U1 commit is dated 2026-10-09T19:53:51Z):
    - `0f81b1adeab8712c526ac21b0b58fbc7279c180e` removes the Java setup, `check:kotlin`, the Gradle wrapper validation, the java-kotlin CodeQL language and its tool download from `ci.yml`. It deletes `tooling/kotlin.ts`, `tests/kotlin-consumer`, `.java-version` and the dependabot gradle entry. It chains receipt `cloud-84-r1` from `cloud-85-r2`.
    - `a660507` (S33(1), ADP-07 supporting): the licence-boundary gradle row, the tool-regenerated `eng/provenance/NOTICE.txt`, and the README, `.gitattributes` and `docs/provenance.md` lines. `third-party/Gradle.LICENSE.txt` stays while `gradle-legal-r1` is active.
    - `8363f4e` (S33(2)): the dependency checker walks first-parent history (`--diff-merges=first-parent`), so a receipt introduced by a merge commit (`cloud-85-r2`, in `0a1f69a`) is found. A fixture-repository regression test is added.
  - **U2, npm Contracts SDKs retired:**
    - `c8193f0` removes `@arcforges/proto`, `@arcforges/api-client` and their `@connectrpc` and `@bufbuild` closure. `@arcforges/ai-internal` is the one npm Contracts dependency.
    - `tooling/build-identity.ts` reads the committed identity record `eng/generated/contracts-identity.json` (S33(3)(a)). That record is a byte copy of the NuGet `ArcForges.Contracts.PublicApi` `source.json`, and `ContractsIdentityTests` pins the equality.
    - The Hello protocol probe is the NuGet Contracts generated client, run as the `probe` command of `tools/ArcForges.Cloud.Generation` (S33(3)(b)).
    - The WP-05.03 `WirePackagePin` rule is refined (S38(1)): the exact pin is required when the package is declared, and a runtime dependency when it is imported. The commit reports 86 fixtures (28 pass, 58 refuse).
    - `73db642` reverted a `docs/harness-proofs.md` sentence as outside the writes. `43e9504` restored it under S39(4).
  - **U3, Worker tables generated from C#:**
    - `9ee8fb8` registers the non-published tool project (S35(1)).
    - `6a41771` generates the method table, transport budgets and edge-guard names from the C# registrations (`HelloModule`, `PipelineProbe`) and the declarations in `src/ArcForges.Cloud/Generation`. The output is `worker/tables/cloud-tables.generated.ts` (S35(2)), checked by `check:generated` in the `npm run check` chain. The regex comparison of `ingress-routes.test.ts` against C# sources is retired.
    - `22e82f4` admits the Generation folder to `.dockerignore` and rebinds receipt `cloud-84-r2`.
  - **U4, correlation reduced to applying generated guards:** `da4b27a`. `CorrelationGuards.cs` declares the canonical UUID shape, the nil value, the field numbers and the traceparent version and flags. `worker/ingress/correlation.ts` applies them and forwards. The strict traceparent parser moves to test support. Every case of `ingress-correlation.test.ts` is kept (16 at the base and 16 at the merge; S34(3)), and `CorrelationGuardTests` is added. `785bd9a` takes the proof CSRF header name from the generated edge guard.
  - **U5, readiness evaluation in C#:** `0e520d9` (S39(1), option A). `ReadinessEvaluator`, `ReadinessModel`, `ReadinessObservations` and `ReadinessVocabulary` are in `src/ArcForges.Cloud/Readiness`. The Worker forwards raw observations through the signed proof `readiness` operation, and it reports transport-only when the Container cannot answer. `worker/readiness/evaluate.ts` and `model.ts` are removed. The proof-host files are ADP-07 supporting under S39(2) and (3). `8017be2` (a review fix) makes a transport-only report judge only the Container, and it names readiness terms from the generated module.
  - **U6, proof entry split out of the production bundle:** `59d9036` (D1). `worker/index.ts` is the production entry and exports `CloudContainer`, `ContainerProxy` and the default handler. `worker/proof/entry.ts` is the proof entry. The candidate seals a second bundle, `proof-worker.js`. `ProductionBundleTests` builds the production bundle with wrangler and scans it. The PR body reports the production bundle at 92 KB, down from 318 KB. The `release-provenance.test.ts` pin at the merge is 92603 bytes, sha256 `14f6a5df…`. `8a380c7` binds profile `cloud-release-r46` and records `cloud-84-cloud-worker-bundle-r1` and `cloud-84-cloud-runtime-notices-r1`.
  - **U7, storage-plan generator in C#:** `045012e`. `plans generate|check` in the tool project reproduces `worker/storage/plans.generated.ts`, `storage/plans/families.expanded.json` and `PlanManifest.g.cs` with one manifest hash. It proved byte parity while the TS generator still existed. `check:plans` runs the C# gate.
  - **U8, TS generator retired and storage adapter reduced:**
    - `9f3e13e` deletes the three TS generator suites.
    - `a172594` (S40) removes every generate, write and CLI entry point from `eng/verification/storage-plans.ts` and keeps its parse and validate helpers as test support. `storage-plan-parity.test.ts` pins the TS-built manifest to the C# output. `StorageGuards.cs` supplies the adapter's deadline and value bounds. The commit records which function went where. Its production dry-run gave an `index.js` byte-identical to the r46 digest.
    - `cfa9661` binds profile `r47`.
  - **U9 and U10, D1 migration runner and deploy decisions in C#** (S41, option A):
    - `e05cd45` adds `src/ArcForges.Cloud.Storage.D1/MigrationRunner` (lease, fence, receipts, chunks, backfill, cutover and contract gating), `src/ArcForges.Cloud.Storage.D1/Deploy` (database selection, release plan, context checks, excluded-build and gate refusals), and a `migrate` command with a C# D1 REST transport in the tool project. The bearer token is read from the environment only. `eng/migrations/deploy.ts`, `cli.ts` and `shim.ts` are argument shims, and the shim checks the sealed digest before it runs the tool. The candidate job gains the pinned `setup-dotnet` step. `RestMigrationClient` and `migrate:dry-run` are removed.
    - `f3042fa`: RP-10 mapping of the new public members.
    - S42 follow-ups:
      - `d672186` moves the 22 SQL statements and the classifier patterns into embedded resources (S42(1));
      - `4cab539` marks `runner.ts`, `catalog.ts`, `sql.ts` and `clients.ts` as test support (S42(2));
      - `8b1c98f` pins the token order (S42(3));
      - `7401882` restores the full column and index shape comparison, with a negative control (S42(4));
      - `590e3a5` adds receipt `cloud-84-r10`;
      - `235d00a` is whitespace only.
  - **U11, standing WorkerAdapter literal check:**
    - `f168a13` (S43) generates the remaining Worker limits and identifier shapes from `WorkerWireLimits` and `ProofWireLimits`. Where the host already defines a value, the declaration references it.
    - It adds `tests/ArchitectureTests/WorkerAdapter/WorkerLiteralScan`, with a closed protocol-constant list, and register rows `HAR40-EX-6` to `HAR40-EX-15` (owner HAR.00) and `CLOUD84-EX-1` to `CLOUD84-EX-11` (owner CLOUD.05, D16).
    - The hosted `EvaluatedRepositoryGate` runs the check (D9).
    - S45 made the budget rule structural:
      - `18753e1` adds closed number rows and `HAR40-EX-16` to `HAR40-EX-18`;
      - `0578375` makes the scan read whole operands and bounds the structural values;
      - `2d154c8` and `a7eb346` make the shim and the probe fail closed in GitHub Actions (S45(3), S46(a));
      - `318e565` fixes the three stale docs (S45(4));
      - `4355c47` is a format-only commit.
  - **U12, factual docs and the release bindings:**
    - `7d3a44b` updates `docs/d1-migration-deployment.md`, `docs/harness-foundation.md`, `docs/cloud-ingress.md` and `AGENTS.md`.
    - `d443b59` binds profile `r48` and refreshes the release-provenance digest (S29).
    - `30cd4ff` adds the S44(1) gitleaks allowlist.
    - `0778850` binds profile `r49` after the review fixes.
  - **Hosted-CI fixes** (see Hosted runs):
    - `88cdf70` orders migration files ordinally and carries the S46(c) items;
    - `b624943` binds profile `r50`;
    - `ffd9cea` seals one non-single-file tool archive.
  - **Release and review records at the merge.** The S25 fields differ by record kind (read by this author at `837fb29f`):
    - dependency receipts `cloud-84-r1` to `cloud-84-r10`, chained, with `r10` bound by `eng/policy/dependency-policy.json`. Each has `review.reviewer` `w-deku-20261009-rev-cloud-84` and `review.decision` `approved`. `review.reviewedOn` is 2026-10-09 for `r1` to `r3` and 2026-10-10 for `r4` to `r10`;
    - release profiles `cloud-release-r46` to `r50`. They carry no reviewer, decision or reviewedOn field; each has only `ownerCommit` (for `r50`, `88cdf70`);
    - provenance records `cloud-84-cloud-worker-bundle-r1` to `r5` and `cloud-84-cloud-runtime-notices-r1` to `r5`, with `r5` named in `artifactRecords`. Each has `review.reviewer` `w-deku-20261009-rev-cloud-84`, `review.decision` `approved` and `review.reviewedOn` 2026-10-10.

    Earlier records stay as immutable history.

- **One-for-one test ports, with counts.** This author counted the TypeScript `test(` blocks at the base `3c59ce34` and the C# `[Fact]`/`[Theory]` methods at `837fb29f`. A theory can expand to several cases, so method counts are not case counts. The mapping was not re-verified case by case here. The reviewer reports at `a7eb346` that the deleted TS suites "are mapped one for one to C#, with counts".

  | Retired TypeScript suite (blocks) | C# replacement at the merge (methods) |
  |---|---|
  | `d1-migration-runner.test.ts` (30) | `Reduction/MigrationRunnerTests.cs` (33: the 30 ports plus the S42(4) negative control and the two `88cdf70` ordering tests) |
  | `d1-migration-deploy.test.ts` (16) | `Reduction/DeployTests.cs` (17: the 16 ports plus the S42(3) token-order test) |
  | `storage-plans-generator.test.ts` (8) | `Reduction/StoragePlanGeneratorTests.cs` (9, including the family-roles case below) |
  | `storage-plan-ownership.test.ts` (10) | `Reduction/StoragePlanOwnershipTests.cs` (10) |
  | `storage-plan-vectors.test.ts` (15) | `Reduction/StoragePlanVectorTests.cs` (15) |
  | `family-plans.test.ts`: the generator-output cases (16 blocks at the base, 13 at the merge) | `StoragePlanGeneratorTests.TheManifestCarriesFamilyRolesAndTheCatalogAndTheWorkerDictionaryCarriesNone` and the existing C# stale, checked-in and expansion tests (`a172594`) |
  | `readiness-model.test.ts` (6) and `readiness-evaluate.test.ts` (19) | `Readiness/ReadinessEvaluatorTests.cs` (10, new) and `HostReadinessTests.cs` (7, changed). The Worker-side cases stay in the new `readiness-transport.test.ts` (20) and `readiness-wire.test.ts` (3) |
  | `identity-structure.test.ts`: the proto-dependent contract scan (10 blocks at the base, 9 at the merge) | `Generation/IdentityContractStructureTests.cs` (3) (S33(3)(c), S38(3)) |
  | `ingress-routes.test.ts`: the C#-source regex comparison (10 blocks at the base, 8 at the merge) | `Generation/GeneratedTablesTests.cs` (7) |

  The new C# guards are `CorrelationGuardTests` (3), `StorageGuardsTests` (6) and `ContractsIdentityTests` (1). The new architecture tests are `WorkerLiteralScanTests` (9) and `ProductionBundleTests` (2). The new TypeScript suites are `d1-migration-shim.test.ts` (19) and `storage-plan-parity.test.ts` (3).

- **Review trail (Cloud PR #83).** The PR has four comments and no GitHub review events. Each comment records `approved` by the independent session `w-deku-20261009-rev-cloud-84`:
  - [6095563762](https://github.com/ArcForges/Cloud/pull/83#issuecomment-6095563762) (2026-10-10T08:12:39Z): a full exact-head review of `a7eb346327a9fb5d26952f46709cbf09269ed760` (39 commits, 206 files).
    - It records the earlier rounds. The loop did not approve `0778850`, because the WorkerAdapter scan was name-gated and the probes `export const bound = 4096`, `return 65536` and `byteLength > 8192` passed. S45 then made the rule structural.
    - Gates it reports: npm test 749, `test:artifact` 10, `test:dependencies` 19, policy 0 findings, dotnet 1602 passed and 1 skipped, actionlint clean, gitleaks 0 over the full history.
    - It reports a production dry-run bundle of 92,765 bytes with no proof symbol, probe parity with the old `verifyProtocol`, and the deleted suites mapped one for one.
  - [6095800467](https://github.com/ArcForges/Cloud/pull/83#issuecomment-6095800467) (08:44:55Z): a delta review of `88cdf70ed355f5b23fc6234b7684776d2b19c502` (11 files). It reports the root cause and the fix of the first hosted failure, an enumeration audit, the regression guard, the S46(c) items, and dotnet 1604 passed and 1 skipped.
  - [6096099980](https://github.com/ArcForges/Cloud/pull/83#issuecomment-6096099980) (09:25:01Z): a delta review of `b6249435b9c78a712caa18a7e35dfc9446bcd382`. It reports successor `cloud-release-r50` (only the `MigrationCatalog.cs` digest changes), records `r5`, all 202 image inputs re-derived, and the Worker bundle unchanged.
  - [6096526210](https://github.com/ArcForges/Cloud/pull/83#issuecomment-6096526210) (10:22:59Z): a delta review of `ffd9cea5b9d40b9a01a3d47683af890edbabb14c`.
    - NU1004 was reproduced under CI conditions. The fix publishes one non-single-file tool. Two publishes gave byte-identical archives, and the tool lock is byte-identical through the candidate.
    - The runners fail closed under `GITHUB_ACTIONS`. The extracted Linux apphost ran `migrate deploy` (a fail-closed refusal) and `probe` in WSL2 Debian.
    - Gates: npm test 756, dotnet 1604 passed and 1 skipped.

  The approval of `ffd9cea` was posted before its hosted run (38044701415, created 10:23:01Z) completed at 10:30:59Z with success. The merge followed at 10:31:46Z. The PR author, every approving comment and the merge are under the one GitHub account `deku2026`, so independence rests on the separate session only. At the merge, the PR check rollup also lists one check named `CodeQL` as `NEUTRAL`, beside the three CodeQL language jobs, which succeeded.

- **Hosted runs.** All runs are in `ArcForges/Cloud`. This author read job conclusions with `gh run view --json`, grepped log lines with `gh run view --log` for specific results, and printed no secret value.
  - **PR run [38037077096](https://github.com/ArcForges/Cloud/actions/runs/38037077096) at `a7eb346`: failure.**
    - Source (ubuntu-latest), job 114169636909, failed in `npm run check:dotnet` on `MigrationRunnerTests.TheIntegrationOwnerNumbersPendingMigrationsInOrderAndLocksThemAndTheLockStaysAppendOnlyAgainstItsBase`. Source (windows-latest) succeeded.
    - **Root cause:** `MigrationFiles.ReadDirectory` used `Directory.GetFiles` without a sort. NTFS lists alphabetically and the Linux runner does not. The retired TS runner sorted with `readdirSync(...).sort()`.
    - **Fix:** `88cdf70`. `MigrationCatalog.SortedSqlNames` applies an ordinal sort, and regression tests cover reversed and shuffled arrivals.
  - **PR run [38038954056](https://github.com/ArcForges/Cloud/actions/runs/38038954056) at `88cdf70`: failure.**
    - Native AOT image and Worker build, job 114176324154, failed in `npm run candidate` with `AssertionError [ERR_ASSERTION]: Changed build input: src/ArcForges.Cloud.Storage.D1/MigrationRunner/MigrationCatalog.cs`. Source (ubuntu-latest) passed this time.
    - **Root cause:** the CI-fix commit changed an image input bound by `cloud-release-r49` without a successor profile.
    - **Fix:** `b624943`, with profile `r50` and records `r5`.
  - **PR run [38041307847](https://github.com/ArcForges/Cloud/actions/runs/38041307847) at `b624943`: failure.**
    - The candidate job, job 114183080517, failed with `error NU1004: The package references have changed for net10.0` on `tools/ArcForges.Cloud.Generation`.
    - **Root cause:** the single-file probe publish turns on the single-file analyzer. Its implicit `Microsoft.NET.ILLink.Tasks` reference is not in the reviewed tool lock, and the CI restore is locked. The local runs had not set the CI environment.
    - **Fix:** `ffd9cea`. It publishes one self-contained, non-single-file linux-x64 tool, sealed as `arcforges-tool.tar` with its digest in the manifest (the S38(2) preferred approach). The lock snapshot-and-restore is removed, and the candidate asserts the lock is unchanged.
  - **PR run [38044701415](https://github.com/ArcForges/Cloud/actions/runs/38044701415) at `ffd9cea`: success.** Every job succeeded, including Native AOT image and Worker build and Verify. Both Deploy jobs and Proof Cloudflare access were skipped.
  - **Main CI run [38045218145](https://github.com/ArcForges/Cloud/actions/runs/38045218145)** (push, head `837fb29f`, 10:31:49Z to 10:41:02Z) succeeded. Every job succeeded except Dependency review and the proof jobs, which were skipped on the push.
    - Source (ubuntu-latest) logged `tests 756`, `pass 756` and `fail 0` for npm, `tests 19` for the dependency tests, and dotnet `total: 1605`, `succeeded: 1604`, `skipped: 1`, `failed: 0`. It also logged `Pinned Node/npm toolchain verified.`
    - Dependency audit and repository checks logged gitleaks `374 commits scanned.` and `no leaks found`. Its "Architecture policy gate (hosted)" step (the `EvaluatedRepositoryGate` filter, D9) passed 2 of 2.
    - Deploy Cloudflare logged:
      - `migration step: not applicable (production declares no D1 database; there is nothing to migrate)`;
      - `Pushed image: …arcforges-cloud:ci.345.1`;
      - the production Container application `arcforges-cloud-cloudcontainer` modified to a new image digest;
      - `Current Version ID: 95e026f3-0a13-49e3-8c08-318a0104d87d`.
    - Prerelease `cloud-0.1.0-ci.345.1` (target `837fb29f`, published 2026-10-10T10:40:58Z; read with `gh release view`, not downloaded) has the assets `cloud-0.1.0-ci.345.1.tar.gz` (67872582 bytes) and `deployment.json` (431 bytes). The CLOUD.85 release `ci.330.1` tarball was 14216450 bytes. This record does not attribute the difference.
  - **Production `https://arcforges.com/api/healthz`**, read by this author on 2026-10-10, returned `revision` `837fb29f2509b1fa7117948dbd48fa9f805bd502`, `artifact.version` `0.1.0-ci.345.1`, `build.buildId` `38045218145.1` and `nativeAot` true.
  - **Proof runs under `RES-cloud-deployment`.** The lease is coordinator-reported as epoch 3, held by `w-deku-20261009-cloud-84`.
    - **Observe run [38045852895](https://github.com/ArcForges/Cloud/actions/runs/38045852895)** (workflow_dispatch at `837fb29f`, 10:42:46Z) succeeded, including Proof Cloudflare access and resources. It logged the proof Container application at `version 14`, `max_instances 4`, image `sha256:c7ca853d…`.
    - **Deploy run [38046437337](https://github.com/ArcForges/Cloud/actions/runs/38046437337)** (workflow_dispatch at `837fb29f`, 10:52:41Z) **failed**. The job "Deploy Cloudflare proof environment" (114198220924) logged, in order:
      - The gated proof D1 step ran the sealed C# migrator: `migration step: proof database arcforges-proof-business, release 837fb29f2509`, then a report with `"status": "passed"`, `"applied": []` and `"schemaVersion": 25`.
      - In `npm run deploy:proof`: `Pushed image: …arcforges-cloud:ci.354.1`; the Web `web-0.1.0-ci.117.1` profile bundle and Site verified; and `No migrations to apply!`.
      - Then the failure: `The entry-point file at "worker/proof/entry.ts" was not found.` The job ended with `Error: node exited with code 1`.
      - **Root cause**, as confirmed by the #89 review: U6 gave `env.proof` its own `main`, which overrides the top-level `main` under `--env proof`. `buildProofConfig` rewrote only the top-level `main`, so Wrangler looked for the source entry next to the generated config. The deploy-proof path is hosted-only, and no local run before the merge exercised it.
    - **Closing observe run [38047010320](https://github.com/ArcForges/Cloud/actions/runs/38047010320)** (11:02:39Z) succeeded. It logged the proof Container application still at `version 14` with the same image `sha256:c7ca853d…`. The image `ci.354.1` was pushed to the registry, but the Container application was not rolled to it.
    - The proof `https://proof.arcforges.com/api/healthz`, read by this author on 2026-10-10 after these runs, returned `revision` `3c59ce34413c94c86ce400fd2950b6372d45abbd`, `artifact.version` `0.1.0-ci.339.1` and `build.buildId` `38009326285.1`. That is the CLOUD.85 follow-up deploy, so the proof Worker was not updated by run 38046437337. The proof Worker version then serving was `0de3e45a`: the line `Current Version ID: 0de3e45a-adbd-4eb0-ac8a-76a7dc223892` of proof deploy run [38009326285](https://github.com/ArcForges/Cloud/actions/runs/38009326285) (grepped by this author; also cited in the CLOUD.85 record), consistent with the healthz `buildId` `38009326285.1`.

- **Follow-up Cloud [PR #89](https://github.com/ArcForges/Cloud/pull/89)**, "[CLOUD.84] Deploy the sealed proof bundle on the proof environment (follow-up)", head `task/cloud-84` at `b84b31ef7887e5efc690ec03e499a4d1ab8ac9a9` (one commit, 3 files: `eng/verification/proof-cloudflare.ts`, `eng/verification/proof-deploy.ts`, `tests/worker/proof-deploy.test.ts`; 87 insertions, 9 deletions).
  - `buildProofConfig` sets `env.proof.main` to the sealed `./candidate/proof-worker.js`. It refuses a `main` outside `./candidate/<name>.js`, and it refuses a candidate whose `env.proof` lost its own entry.
  - Approved at `b84b31e` by `w-deku-20261009-rev-cloud-84` in comment [6097005880](https://github.com/ArcForges/Cloud/pull/89#issuecomment-6097005880) (2026-10-10T11:26:26Z), as an independent exact-head review.
  - The reviewer reproduced the failure with wrangler dry-runs from scratch exports and an assembled deploy-job layout, with no Docker and no credentials. The proof dry-run fails at `837fb29f` with the hosted error and exits 0 at `b84b31e`. The uploaded `proof-worker.js` (sha256 `0c46fd67…`) is byte-identical to the sealed member. The production dry-run is unchanged on both revisions (`worker.js` `14f6a5df…`, the r50 pin). Nothing changes under `tooling/`, `.github/`, `worker/` or `wrangler.json`, so no successor records are needed.
  - Gates reported: npm test 757, plus `check:generated`, format, lint, typecheck, licence, provenance, policy, plans, physical and dependencies.
  - Its CI run [38048403583](https://github.com/ArcForges/Cloud/actions/runs/38048403583) (pull_request at `b84b31e`, created 11:26:17Z, completed 11:34:35Z) succeeded. Every job succeeded except Proof Cloudflare access and both Deploy jobs, which were skipped. The PR check rollup again lists one `CodeQL` check as `NEUTRAL` beside the three CodeQL language jobs, which succeeded.
  - It was merged as `c291550f73ba64cb9fa4c15d4ec0e731a27dede8` at 2026-10-10T11:43:45Z by `deku2026`. The merge commit has two parents, `837fb29f` and `b84b31ef`, consistent with the `--merge` method. See "Proof deploy (D11)" for the runs that followed.

- **Offline validation clauses** (the graph's evidence list):
  - *generate --check receipts:* `check:generated` (the Worker tables) and `check:plans` (the C# plan generator, three outputs with one manifest hash) run in `npm run check`. That passed in both hosted Source jobs of main run 38045218145.
  - *Production bundle scan:* `ProductionBundleTests` runs in `check:dotnet` (passed in the hosted Source jobs). The reviewer's dry-run scan at `a7eb346` and the #89 production dry-run are cited above.
  - *Static scan of `worker/**`:* `WorkerLiteralScan` runs in `check:dotnet` and in the hosted `EvaluatedRepositoryGate` step (2 of 2 passed). Its exceptions are the closed lists and the 29 owned register rows in `eng/policy/harness-architecture-exceptions.json`, all expiring 2027-03-31:
    - `HAR40-EX-1` to `HAR40-EX-5`, from HAR.40;
    - `HAR40-EX-6` to `HAR40-EX-18`, owner HAR.00;
    - `CLOUD84-EX-1` to `CLOUD84-EX-11`, owner CLOUD.05 (D16).
  - *Correlation:* `worker/ingress/correlation.ts` applies the generated guards and forwards (S34(3)). `HAR40-EX-4` (wire-codec, owner CLOUD.69) still covers it.
  - *Edge guards:* `worker/ingress/edge-caller.ts` reads the session cookie name, the CSRF header and the token patterns from the generated module (lines 7 to 14) and only refuses. No test named as a separate edge-guard scan was found. The literal scan covers these files.
  - *Migration-runner oracle:* `MigrationRunnerTests` runs on the SQLite batch oracle (D8), including the stale-migrator, resume-from-`statements_done` and merged-checksum cases that the reviewer mapped. The live proof D1 steps in runs 38046437337 and 38050068108 ran the sealed C# migrator through the D1 REST API and passed, with nothing to apply.
  - *Kotlin gate removal after AND.40:* `0f81b1a`, as above.
  - *Native AOT host build on Windows and WSL2 Debian:* see Scope, gap 4.

## Proof deploy (D11)

All runs are in `ArcForges/Cloud`. This author checked each conclusion with `gh run view --json`, grepped the job logs with `gh run view --log` for the lines quoted, read the release with `gh release view` (metadata only, nothing downloaded), and printed no secret value.

- **History: the failed attempt.** Deploy run [38046437337](https://github.com/ArcForges/Cloud/actions/runs/38046437337) at `837fb29f` failed with `The entry-point file at "worker/proof/entry.ts" was not found.` Root cause: `env.proof.main` overrode the top-level `main` that `buildProofConfig` rewrote (see Hosted runs). It stays recorded as history. PR #89 is the fix.
- **PR #89 merge.** Approved at `b84b31e` in comment [6097005880](https://github.com/ArcForges/Cloud/pull/89#issuecomment-6097005880). Its CI run [38048403583](https://github.com/ArcForges/Cloud/actions/runs/38048403583) succeeded (all checks passed; the deploy and proof jobs were skipped on the pull request). It was merged as `c291550f73ba64cb9fa4c15d4ec0e731a27dede8` at 2026-10-10T11:43:45Z, with parents `837fb29f` and `b84b31ef` (a two-parent merge). The merge flags and the integration role are coordinator-reported.
- **Main CI run for the #89 merge: [38049435694](https://github.com/ArcForges/Cloud/actions/runs/38049435694)** (push, head `c291550f`, 11:43:47Z to 11:53:48Z) succeeded. Every job succeeded except Dependency review and the two proof jobs, which were skipped on the push. This is the second production deploy of CLOUD.84 (see residual 8). The job Deploy Cloudflare (114206925013) logged:
  - `migration step: not applicable (production declares no D1 database; there is nothing to migrate)`;
  - `Pushed image: …arcforges-cloud:ci.357.1`;
  - the production Container application `arcforges-cloud-cloudcontainer` modified from image `sha256:13e178b0…` to `sha256:e72a4f92…`;
  - `Current Version ID: 74d7e722-a4dc-4ded-8751-d3360e82a4e9`. The production Worker version changed from `95e026f3` (run 38045218145) to `74d7e722`.
  - Prerelease `cloud-0.1.0-ci.357.1` (target `c291550f`, published 2026-10-10T11:53:44Z) has the assets `cloud-0.1.0-ci.357.1.tar.gz` (67880125 bytes) and `deployment.json` (431 bytes).
  - Production `https://arcforges.com/api/healthz`, read by this author on 2026-10-10 after the run, returned `revision` `c291550f73ba64cb9fa4c15d4ec0e731a27dede8`, `artifact.version` `0.1.0-ci.357.1`, `build.buildId` `38049435694.1` and `nativeAot` true.
  - The #89 review reports the production Worker bundle unchanged (`14f6a5df…`). The new Worker version and Container image are new deployments of the rebuilt candidate at the new revision. This author did not compare the deployed bundle bytes.
- **`RES-cloud-deployment` lease.** Epoch 3, held by `w-deku-20261009-cloud-84`, was renewed for the proof runs and then released. This is coordinator-reported.
- **Proof deploy run [38050068108](https://github.com/ArcForges/Cloud/actions/runs/38050068108)** (workflow_dispatch at `c291550f`, 11:54:38Z to 12:03:30Z) succeeded. No separate opening observe run was dispatched for this attempt. The run's own job "Proof Cloudflare access and resources" (114207234506) passed every token-access check and found the proof D1, R2 and both queues existing. The job "Deploy Cloudflare proof environment" (114208584603) logged, in order:
  - the gated proof D1 step: `migration step: proof database arcforges-proof-business, release c291550f73ba`, then a report with `"status": "passed"`, `"applied": []` and `"schemaVersion": 25`;
  - in `npm run deploy:proof`: `Pushed image: …arcforges-cloud:ci.358.1`;
  - `Web web-0.1.0-ci.117.1: profile bundle 2070acd9… and Site 735374a5… verified`;
  - `No migrations to apply!`;
  - the proof Container application `arcforges-cloud-proof-foundationcontainer-proof` modified from image `sha256:c7ca853d…` to `sha256:56fbd4f6…` (the `ci.358.1` digest);
  - `Current Version ID: 84ce5952-e34e-4737-bd6d-92a8e02af03b`. The proof Worker version changed from `0de3e45a` (run 38009326285) to `84ce5952`;
  - `Proof environment deployed at https://proof.arcforges.com. This is deployment completion, not live acceptance evidence.`
- **Closing observe run [38050648279](https://github.com/ArcForges/Cloud/actions/runs/38050648279)** (workflow_dispatch at `c291550f`, 12:04:34Z) succeeded. It logged the proof Container application at `version 15`, `max_instances 4`, image `sha256:56fbd4f6…`, with 0 listed instances. The deployment history shows target versions 15, 14, 13 and 12.
- **Proof `https://proof.arcforges.com/api/healthz`**, read by this author on 2026-10-10 after these runs: HTTP 200, `revision` `c291550f73ba64cb9fa4c15d4ec0e731a27dede8`, `artifact.version` `0.1.0-ci.358.1`, `build.buildId` `38050068108.1` and `nativeAot` true.
- **Read-only route checks on the proof origin** (unauthenticated GETs by this author): `/account/` 200, `/chat/` 200, `/` 200, `/proof/v1/x` 401 (the signed proof surface refuses an unsigned caller) and `/session/v1/x` 404. No signed proof operation, Hello round trip or HAR.40 live proof was run (see Untested coverage).
- **D11: met.** One proof deploy of the merged CLOUD.84 code succeeded (run 38050068108) under the lease, at the second attempt and after the #89 fix. The proof origin serves `c291550f`, which contains the `837fb29f` merge. As the deploy log states, this is deployment completion, not live acceptance evidence.

## Scope (2026-10-10)

- **Delivered outcome:**
  - The production Worker is a thin Cloudflare adapter built from `worker/index.ts` alone, with no proof code in its bundle.
  - The method table, transport budgets, edge-guard parameters, correlation guards, readiness vocabulary and the remaining limits and identifier shapes are generated from C# into `worker/tables/cloud-tables.generated.ts`, under a `generate --check` gate.
  - Readiness evaluation, storage-plan generation, the D1 migration runner and the deploy decisions are C#.
  - The npm Contracts dependency is `@arcforges/ai-internal` only, and the Kotlin consumer gate is removed.
  - A standing WorkerAdapter literal check runs in `check:dotnet` and in the hosted gate.
  - Production was deployed at `837fb29f` (run 38045218145, Worker version `95e026f3`) and again at the #89 merge `c291550f` (run 38049435694, Worker version `74d7e722`, release `cloud-0.1.0-ci.357.1`). Both production migration steps report not applicable, and production behaviour (`/api/healthz`, the anonymous Hello) is reported unchanged by the reviewer's dry-run and the worker tests.
  - The proof environment is deployed at `c291550f` (run 38050068108, proof Worker version `84ce5952`), so D11 is met.
- **Deviations from the graph text, each authorised:**
  - The generated module is `worker/tables/cloud-tables.generated.ts`, not `worker/generated/cloud-tables.ts` (S35(2)).
  - The live migration path is the D1 REST API, not wrangler (S41(6), a factual correction).
  - A sealed self-contained C# tool runs the migration decisions in the deploy jobs, not Node (D6 as amended by S41(1)).
  - The TS migration modules and `eng/verification/storage-plans.ts` stay as test support, not reduced or removed (S40(1), S42(2)).
  - Proof-only coordination stays TypeScript under D16.
  - `ingress-correlation.test.ts` stays as Worker transport tests (S34(3)).
- **Status decision: `delivered` (D13).** `python -I rec.py CLOUD.84` was run by this author. The graph lists four `complete` edges: CLOUD.21, CLOUD.05, AND.40 and HAR.03, all integration and all in scope. On the Plan branch this record is written on (from `origin/main` at `ebd43544`):
  - CLOUD.21, CLOUD.05 and HAR.03 have no ledger record, so they are open;
  - AND.40 is `delivered`, not `complete`. The Kotlin gate condition ("after AND.40 delivers") is met, but `delivery.py` counts a completion prerequisite only when it is `complete` or `inherited`, so AND.40 is also a pending completion prerequisite.

  The coordinator's list names CLOUD.21, CLOUD.05 and HAR.03. This record adds AND.40, from the check rule.
- **Gaps against the status rule.** Each gap is named, with its next action.
  1. **D11 proof deploy: met (closed).** The proof deploy at `837fb29f` failed (run 38046437337). After the #89 fix, the proof deploy at `c291550f` succeeded (run 38050068108). See "Proof deploy (D11)". *Next action:* none for D11. The live HAR.40 proofs stay untested (see Untested coverage).
  2. **Completion prerequisites: open.**
     - CLOUD.21: the method/route table is generated from its registered C# public endpoints.
     - CLOUD.05: its job slice budgets are generated from the C# finite-job runner, and the D16 rows `CLOUD84-EX-1` to `11` are removed.
     - HAR.03: the bundle and static scans are re-run on its final `worker/harness` code and `worker/index.ts`.
     - AND.40: recorded `complete`.

     *Next action:* a CLOUD.84 completion follow-up (DLV-41) once these are recorded, re-running `check:generated` and the WorkerAdapter scans against them.
  3. **Queue and coordination policy to C# (outcome clause; CLOUD.05): not done here, by D16.** `worker/foundation/coordination.ts`, `poison.ts`, `durable.ts` and `queue.ts` stay TypeScript in the proof bundle. They are covered by `CLOUD84-EX-1` to `11` (owner CLOUD.05, expiry 2027-03-31). No `Reduction` queue or coordination tests exist yet. *Next action:* CLOUD.05.
  4. **Native AOT host build on Windows and WSL2 Debian (validation): not recorded for CLOUD.84.** The PR trail records the dotnet Release build and tests on both hosted runners and locally. It records no win-x64 or WSL2 Native AOT publish of the host at any CLOUD.84 head. The WSL2 run at `ffd9cea` executed the self-contained tool, not the AOT host. The Linux AOT evidence is the hosted candidate image build and production `nativeAot` true at `837fb29f`. *Next action:* an agent runs the win-x64 and WSL2 Debian AOT publish and smoke at the merged head (WSL2 is allowed for Linux tests), or the coordinator rules that the hosted Linux image build satisfies the clause. The HAR.40 record's note on the WSL SDK 10.0.400 versus the pinned 10.0.401 applies.
  5. **Edge-guard scan receipt (evidence): partly met.** See Evidence: the parameters come from the generated module, and the Worker only refuses. No separate edge-guard scan test is named, and the C# host's enforcement of the same rule was not re-verified by this author. *Next action:* the completion follow-up names the test that is the receipt, or adds one.
- **Rulings applied** (brief section 11):
  - **S29:** CLOUD.84 refreshes the pre-HAR.40 Worker-digest constant in `tests/worker/release-provenance.test.ts` after its last Worker change. Done in `d443b59` and `0778850`. At the merge the pin is `14f6a5df…`, 92603 bytes, and the reviewer reports `test:artifact` 10/10. That result is reviewer-reported only: `test:artifact` is in no `ci.yml` step (residual 5), and this author did not re-run it. It addresses gap 3 of the HAR.40 record (test:artifact 9 of 10), but that gap closes only when it is recorded closed there.
  - **S33:**
    - (1) ADP-07 supporting files for U1 (licence boundary, NOTICE, README, `.gitattributes`, `docs/provenance.md`);
    - (2) the merge-commit receipt defect, fixed with a test before any further receipt;
    - (3) the U2 design: (a) a committed NuGet identity record, (b) a sealed C# Hello probe in place of the npm SDK client with no gate weakened, and (c) a C# identity-structure test;
    - (4) the S29 refresh after the last bundle change.
  - **S34:** transport guards are C# declarations generated into the Worker, and the Worker applies them and forwards.
    - (1) the transport budgets are C# with values unchanged;
    - (2) the HAR.40 envelope and run-alarm constants are not CLOUD.84's but HAR.00's (P2-021 item 6);
    - (3) correlation applies generated guards, keeps refusal before the Container wakes, and keeps every Worker test case.
  - **S35:**
    - (1) the tool project's registrations are supporting edits;
    - (2) the module path is `worker/tables/cloud-tables.generated.ts`, with no contract-authority exemption;
    - (3) successor provenance records are named `cloud-84-*`;
    - (4) the standing rule: registration and inventory edits are supporting, and a rule change stops for a ruling.
  - **S36 and S37** are WEB.40, CLOUD.85 and PRF.11 rulings (the profile CSP `base-uri` and the Tailwind preamble). They do not apply to CLOUD.84.
  - **S38:**
    - (1) the WP-05.03 rule refinement, with fixtures;
    - (2) prefer a non-single-file probe publish; the lock snapshot was an accepted fallback, which `ffd9cea` finally replaced with the preferred approach;
    - (3) only the proto-dependent identity scan moves to C#.
  - **S39:**
    - (1) option A, C# readiness evaluation through the proof operation, with a transport-only Worker report;
    - (2) the proof-host supporting files;
    - (3) the standing proof-host rule;
    - (4) restore the S38(1) wording in `docs/harness-proofs.md`;
    - (5) re-run the U2 gates before U5.
  - **S40:**
    - (1) the TS generator entry points are retired, its helpers stay as test support with a parity test, and the port is an open residual;
    - (2) the storage adapter is reduced to transport, with generated guards and a production dry-run;
    - (3) the factual docs.
  - **S41:**
    - (1) option A, a sealed C# migrator and deploy decisions, with the shim forwarding only;
    - (2) the token reaches the binary through the environment only and is never logged;
    - (3) the pinned `setup-dotnet` step;
    - (4) 30 and 16 tests ported one-for-one;
    - (5) the production not-applicable path is unchanged;
    - (6) the REST-not-wrangler factual correction.
  - **S42:**
    - (1) the SQL goes into embedded resources, with no rule exemption;
    - (2) the TS migration modules stay as test support (an open residual);
    - (3) the TypeScript token order is kept;
    - (4) the full physical-shape strength is restored;
    - (5) the single U9+U10 commit, the retired `migrate:dry-run` and the oracle are accepted.
  - **S43:** the WorkerAdapter literal taxonomy:
    - (1) a HAR.00 carve-out as register rows;
    - (2) a closed protocol-constant list;
    - (3) the remaining values generated now, unchanged;
    - (4) D16 rows owned by CLOUD.05;
    - (5) the bundle successor profile and the S29 refresh.
  - **S44:**
    - (1) one S31-form gitleaks allowlist for `eng/generated/contracts-identity.json`, with positive controls;
    - (2) six judgement calls ratified;
    - (3) profile `r48` was derived by a scratch helper, accepted because `test:artifact` and provenance verify it;
    - (4) README line 6, fixed in `318e565`.
  - **S45:**
    - (1) the budget rule is structural, not name-gated, with closed lists;
    - (2) all 36 review findings are classified;
    - (3) the shim and the probe fail closed in CI;
    - (4) the stale docs are fixed;
    - (5) items recorded only (`.dockerignore` as supporting; the immutable boilerplate in receipts `r4` to `r9`; the missing-HMAC-key short-circuit as a transport precondition).
  - **S46:**
    - (a) the read-only `check` carve-out of the shim under `GITHUB_ACTIONS` is ratified;
    - (b) the items carried as a completion follow-up (residuals below);
    - (c) the trivial items ride with any hosted-CI fix round, which `88cdf70` did.
- **Open residuals and carried items, each with its owner and next action:**
  1. **TS test-support modules (S40(1), S42(2); D13).**
     - The modules: `eng/verification/storage-plans.ts`, and `eng/migrations/runner.ts`, `catalog.ts`, `sql.ts` and `clients.ts`. Each carries a header stating that C# is authoritative and the file is test support.
     - Their consumers include CLOUD.72's `eng/verification/d1-identity-local.ts` (CLOUD.72 owns it; it is outside the CLOUD.84 writes), `eng/verification/physical-schema.ts` (Node build tooling under D4 and D5, not written by CLOUD.84), and the TS suites `commit-tail`, `entitlement-plans`, `family-plans`, `family-oracle`, `module-layout`, `d1-receipts`, the identity suites and the `d1-*-local` drivers.
     - *Owner:* the CLOUD.84 completion follow-up, after CLOUD.72.
     - *Next action:* port the consumer suites to C#, after which CLOUD.72 moves `d1-identity-local.ts` and the coordinator rules on `physical-schema.ts`. Then delete the five files.
  2. **HAR.00 register rows (S43(1), S45(1)(b)): `HAR40-EX-6` to `HAR40-EX-18`**, in `worker/ai/internal/envelope.ts` and `worker/harness/run-alarm-core.ts`, expiring 2027-03-31. *Owner:* HAR.00. *Next action:* HAR.00 declares these values in C#, generates them, narrows the function-level rows (S46(b)), and removes them.
  3. **D16 register rows (S43(4)): `CLOUD84-EX-1` to `CLOUD84-EX-11`**, expiring 2027-03-31. *Owner:* CLOUD.05. *Next action:* as in gap 3.
  4. **S34(2) HAR.00 constants:** the envelope and run-alarm constants keep their "kept in step" comments. *Owner:* HAR.00 (P2-021 item 6 follow-up). *Next action:* as in residual 2.
  5. **S46(b) residue, checked at `837fb29f` by this author.** *Owner:* the CLOUD.84 completion follow-up. *Next action:* one follow-up commit set, with a write-scope ruling for `tooling/licence-boundary.ts`.
     - The root `NOTICE` still names the Kotlin verification client, the Gradle wrapper, and Connect-Kotlin, OkHttp and Kotlin (lines 8 and 12 to 14).
     - `tooling/dependency-policy.ts` `inputNames` still lists `gradle.lockfile`, `settings.gradle.kts`, `build.gradle.kts` and `gradle-wrapper.properties`.
     - `tooling/licence-boundary.ts` `npmOwners` still lists `@arcforges/proto` and `@arcforges/api-client`. That file is not in the CLOUD.84 writes, so its edit needs an ADP-07 supporting ruling.
     - `test:artifact` is in no `ci.yml` step.
     - The other S46(b) items (the `.gradle/` ignore lines, the dependabot `@connectrpc` and `@bufbuild` patterns, AGENTS.md line 8, `docs/bootstrap-plan.md` line 17, and the proof-route refusal values "Enabled" and "1") were fixed in `88cdf70`.
  6. **Shim extracted-folder cleanup** (reviewer, `ffd9cea`, non-blocking): `eng/migrations/shim.ts` does not remove its extracted tool folder. The probe runner in `tooling/protocol.ts` (line 116) does. This is harmless on ephemeral runners. *Owner:* the CLOUD.84 completion follow-up. *Next action:* remove the folder after the run, with a test.
  7. **Proof guard strictness** (#89 reviewer, non-blocking): the `main` guard regex in `buildProofConfig` would also accept `./candidate/worker.js`. Asserting `=== sealedProofBundle` would be stricter. `deploy()` passes the constant, so this is safe today. *Owner:* the CLOUD.84 completion follow-up. *Next action:* tighten the guard, with a refusing test.
  8. **D10 note:** D10 asks for one production deploy from one PR. Merging #89 started a second main push run, [38049435694](https://github.com/ArcForges/Cloud/actions/runs/38049435694), and that run deployed production again (see "Proof deploy (D11)"). Its effect: the production Worker version changed from `95e026f3` to `74d7e722-a4dc-4ded-8751-d3360e82a4e9`, the production Container image changed from `sha256:13e178b0…` to `sha256:e72a4f92…` (`ci.357.1`), the release is `cloud-0.1.0-ci.357.1`, the migration step reported not applicable, and production `/api/healthz` reports `c291550f`. The #89 review reports the production Worker bundle unchanged. So D10's "one production deploy" is not met literally: CLOUD.84 deployed production twice, the second time for a proof-only fix. *Owner:* the coordinator. *Next action:* the coordinator rules whether the second deploy is accepted under D10.

## Untested coverage (stated expressly)

- **Live Workers AI and container proofs (HAR.40).** HAR.40's Proofs 1 to 3 (the Workers AI binding, fenced D1 writes under a real lease, the DO alarm wake after restart, and container capacity) were not run. CLOUD.84 changes the proof entry and the readiness path that those proofs use. The proof origin now serves `c291550f` (run 38050068108), so the CLOUD.84 proof code is live, but only the unauthenticated route checks in "Proof deploy (D11)" were made against it. No signed proof operation was run.
- **Docker candidate locally.** The Docker image build in `npm run candidate` was not run locally by the claimant or the reviewer. It is hosted-only. The reviewer reproduced every candidate step that needs neither Docker nor a secret under CI conditions (`ffd9cea`). The hosted candidate job succeeded at `ffd9cea` and `837fb29f`.
- **Node 24.21 pin.** The local toolchain is Node 24.20 (`npm ci` with `--engine-strict=false`, as recorded in `0e520d9`), so the pin is not met locally. Hosted Source logged `Pinned Node/npm toolchain verified.` at `837fb29f` and is the authority.
- **The Hello probe against a live container or Worker in CI.** In hosted CI the probe is published and sealed, but no hosted log line shows it run. `tooling/project.ts` `testContainer` and `testWorker`, and the production `smoke` in `tooling/cloudflare.ts`, assert that `CI` is not `"true"` and are local opt-in. The probe ran in the reviewer's WSL2 check at `ffd9cea`. The production check here is `/api/healthz`, read by this author. No Hello round trip was made by this author.
- **Live D1 migration with pending work.** The C# migrator ran live twice, against the proof D1 (runs 38046437337 and 38050068108), each time with nothing to apply (`"applied": []`). The lease, fence, backfill, cutover and contract paths are tested only on the SQLite oracle. Production declares no D1.
- **Native AOT host on Windows and WSL2 Debian:** not run for CLOUD.84 (Scope, gap 4).
- **Test-port mapping.** The counts above are block and method counts by this author. The case-by-case one-for-one mapping is reviewer-reported.
- **Local gates.** The npm, dotnet, policy, provenance, dependency, actionlint and gitleaks figures in the review comments were not re-run by this author. The hosted figures from main run 38045218145 are cited above.
- **Release size.** The `ci.345.1` (67872582 bytes) and `ci.357.1` (67880125 bytes) release tarballs were not downloaded or inspected.
- **Proof image `ci.354.1`.** It was pushed to the registry by the failed deploy but never rolled out (the Container application went from version 14 to version 15 with the `ci.358.1` image). It is not assessed.
- **Deployed bundle bytes.** The production and proof Worker versions `74d7e722` and `84ce5952` were not compared byte for byte with the sealed candidate bundles by this author.
- **Independence.** The PR, every approval and the merge are under one GitHub account (`deku2026`). Independence rests on the separate reviewer session `w-deku-20261009-rev-cloud-84`.
- **Coordinator-reported facts.** The `--match-head-commit ffd9cea` flag, the `integration:Cloud` role, the #89 merge flags, and the `RES-cloud-deployment` lease (epoch 3, renewed for the proof runs and then released) are coordinator-reported. The two-parent merge commits (`837fb29f` and `c291550f`), the run conclusions, the log lines (including the Worker versions `0de3e45a`, `95e026f3`, `74d7e722` and `84ce5952`), the release metadata and the healthz and route values are verified by this author.
