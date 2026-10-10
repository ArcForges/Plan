---
task: CON.40
status: delivered
recorded: 2026-10-10
claimant: w-deku-20261010-con-40
epoch: 1
---

# C#-only SDK standardization: TypeScript and Kotlin/Maven publication stopped, @arcforges/ai-internal kept

## Evidence

- **Implementation, in one Contracts pull request** (brief S20(f), S47, S48 and S50):
  - Contracts [PR #97](https://github.com/ArcForges/Contracts/pull/97), "[CON.40] C#-only SDK standardization: retire TypeScript and Kotlin/Maven publication; keep @arcforges/ai-internal", head branch `task/con-40`, base `main` at `330e46bd158bfbb7cdc94c7006565c87e27b1cc6`. It was opened at 2026-10-10T17:53:45Z by `deku2026`. The reviewed head is `15d94d97431cfa3676cd4dda5bf3a2737d368d9f`. The PR has 10 commits and changes 3005 files (19578 insertions, 890212 deletions), as read with `gh pr view 97`. It merged at 2026-10-10T18:11:17Z as merge commit `5615821917922c7c262b8f43bba1285fa9791444` (parents `330e46bd` and `15d94d97`). See "Merge and publication".
  - The claim is `claims/con-40`, epoch 1, claimant `w-deku-20261010-con-40`, claimed at 2026-10-10T09:51:27Z. At `20b98c46` its handoff names PR #97 with `head` and `reviewed` both equal to `15d94d97`. The coordinator holds `integration:Contracts` (S20(f) decision 12). That role holding is public state: Plan branch `roles/integration-contracts` at `c7265da0` ("Claim integration:Contracts epoch 1 by w-deku-20261008-coord"), read by this author after a fetch.
  - The status is `delivered`, not `complete` (S20(f) decision 3). See Scope for the open completion prerequisites.
  - The PR body requires a merge commit, not a squash. `test_con40_secret_scan_allowlists_bind_only_exact_public_digest_tuples` reads each receipt at the commit that added it.

- **Units, with commit SHAs** (the PR body's table, checked against the PR commit list; the order is the S47(12) order, with C4 before C3):

  | Unit | Commit | What it delivered |
  |---|---|---|
  | C1 | `c1eb778` | C# SDK parity suites: `tests/StructureTests/Con40SdkCases.cs` (registered by one line in `tests/StructureTests/Program.cs`), `tests/ArchitectureTests/Sdk/SdkArchitectureTests.cs` (rules SDK-01 to SDK-04, each with negative fixtures), and the case map `eng/policy/con-40-test-map.json`. `tests/public/HelloClient` is unchanged (S47(3)). |
  | C2 | `d64a655` | The build harness is rewired to the C# suites and `@arcforges/ai-internal`, and the Kotlin restore and build calls leave `eng/contracts.py`. It adds receipt `con-40-r1`. |
  | C4 | `17d16e8` | CI and Dependabot cutover: `setup-java`, the Gradle wrapper validation, the `publish-maven` job and the `codeql-kotlin` job are removed, and so are the gradle ecosystem and the retired npm groups in `dependabot.yml`. `.java-version` is deleted. It adds receipt `con-40-r2`. |
  | C3 | `5ac2995` | The Kotlin and Maven channel, the Gradle build and central signing are retired. The three Maven catalog rows are kept and marked retired. It adds receipt `con-40-r3` and record `contract-bindings-con-40-r1`. |
  | C5 | `6106207` | The TypeScript generators and packages are retired except `@arcforges/ai-internal`. The four npm catalog rows are kept and marked retired, and `NPM_IDS` is `("@arcforges/ai-internal",)`. The `package-lock.json` change is limited to the removed workspaces (S47(7)). It adds receipt `con-40-r4` and record `contract-bindings-con-40-r2`. |
  | C6 | `d078d3b` | Receipt-driven provenance retirements (S47(5)), retired access rows kept and marked (S47(4)), the foundation-inventory `outputRetirement` marking (S47(6)), the five PDF RPCs marked retired (CON.04, P2-022), and receipt `con-40-r5`. |
  | C7 | `7aeea9d` | The docs and policy text for the C#-only channel list, and the ai-internal inventory text (S47(11)). Documentation only. |
  | C8 | `baf6e81` | `eng/policy/publication-stops/con-40.json`, the publication-stop evidence for the seven retired identities (S50(1)). |
  | S50(2) | `ca01b4e` | `eng/check_contract_access.mjs` takes the retired set from the union of the base and head catalogs. `ci.yml` drops two stale upload paths. |
  | S50(3) | `15d94d9` | Six exact-row `.gitleaks.toml` allowlist blocks (22 regexes) covering exactly the 24 `generic-api-key` false positives. The count pin goes from 83 to 89, and an exact-tuple test is added. |

  Every one of the 10 commits carries a `Signed-off-by` trailer (checked with `git log` by this author). The reviewer reports that each trailer matches the commit's author and committer.

- **Review trail (Contracts PR #97).** The PR has one comment and no GitHub review events. Comment [6100479241](https://github.com/ArcForges/Contracts/pull/97#issuecomment-6100479241), posted 2026-10-10T17:54:03Z by `deku2026`, reads "Reviewed 15d94d97431cfa3676cd4dda5bf3a2737d368d9f for [CON.40] epoch 1: approved". The reviewer is the independent session `w-deku-20261008-rev-con-40` (Opus 5.5), which authored none of the change. The rounds are in the implementation and review journals of workflows `wf_5116606e-ca5` and `wf_921b16f0-839`:
  - **Round 1 at `7aeea9d`: not approved.** The one material finding was that the hosted Security "Secret scan" would fail. A full-history gitleaks scan with the S31 method found 24 leaks at the head and 0 at base `330e46b`. All 24 are `generic-api-key` matches on public 64-hex SHA-256 input digests, in `eng/policy/dependency-policy.json` (2 at `d64a655` and 2 at `d078d3b`) and in `eng/policy/dependency-reviews/con-40-r1.json` to `r5.json` (4 each). The refix made no commit, because `.gitleaks.toml` was outside the CON.40 writes and no ruling covered it. It prepared a scratch proposal instead.
  - **Round 2 at `7aeea9d`: not approved**, with the same material finding. A new non-blocking finding: `checkRetiredHistory` took the retired set from the head catalog only, so a catalog-and-policy erasure of a retired identity passed `check_contract_access.mjs` on its own. `check_provenance.py` still refused it. The refix again made no commit, and asked for a ruling.
  - **Round 3 at `7aeea9d`: not approved**, with the same material finding. The reviewer confirmed everything else: the 107-case test map, the S47(4) and S47(5) rule probes both ways, the publication channels, the S47(7) lock diff, scope and DCO. The reviewer did not ratify the S25 fields while the gitleaks finding stood.
  - **S50 ruling (2026-10-10).** The coordinator ruled after the third round: C8 now (S50(1)), the two accepted non-blocking fixes (S50(2)), the exact-row gitleaks blocks as the last commit (S50(3)), the recorded follow-ups (S50(4)), the owner-only step (S50(5)) and a delta review (S50(6)). CLOUD.84 was delivered (Plan #476, `335c20fc`), so the S47(13) hold on C8 and the merge was lifted.
  - **Delta round at `15d94d9`: approved.** It covers C8 `baf6e81`, S50(2) `ca01b4e` and S50(3) `15d94d9`. The reviewer reports that `git diff 7aeea9d..15d94d9` touches 8 files and that `7aeea9d` is otherwise byte-identical. The delta round reported:
    - C8 covers all 7 identities. Its publication runs, consumer merges, delivered ledgers and consumer-main greps were re-checked read-only with `gh` and `git`.
    - The S50(2) erasure probe is now refused by `check_contract_access.mjs` alone, against both the unmarked base and a retired base. The `7aeea9d` code passes the same probe, which is the control.
    - The S50(3) change is a pure append. Each of the 24 findings is covered by exactly one of the 22 regexes, and no regex is unused. The reviewer's positive controls fire 4 of 4. The full-history scan with the hosted flags (image `c00b6bd0aeb3`, `--network none`, 330 commits) reports 0.
    - The gates are listed under "Validation actually performed".
  - The approval was posted before PR #97's hosted run completed. The hosted run then passed every required context at `15d94d9`. See "PR CI run" under "Merge and publication".
  - The PR author, the review comment and the claimant all run under the one GitHub account `deku2026`, so independence rests on the separate session only.

- **S25 ratification.** The delta approval ratifies the S25 fields of every CON.40 record at `15d94d9`. Each record names reviewer `w-deku-20261008-rev-con-40`, `decision` `approved` and `reviewedOn` 2026-10-10:
  - dependency receipts `eng/policy/dependency-reviews/con-40-r1.json` to `con-40-r5.json`, chained from `con-25-r1`, with `r5` bound by `eng/policy/dependency-policy.json`;
  - provenance records `eng/provenance/records/contract-bindings-con-40-r1.json` and `-r2.json`;
  - retirement receipts `eng/provenance/retirements/con-40-npm.json` and `con-40-maven.json` (schemaVersion 2, review owner "Licensing and Provenance Owner", Design commit `2817cdbd`);
  - `eng/policy/publication-stops/con-40.json` (review owner `w-deku-20261010-con-40`).

  No `decision: pending` was committed. The reviewer withheld this ratification in round 3 and gave it at `15d94d9`. This author read the review blocks of both retirement receipts and the publication-stop record.

- **ADP-07 supporting files** (outside the record's writes; S47(2) and S50(3); listed in the PR body), checked with `git diff --name-status 330e46bd 15d94d9`:
  - S47(2), changed: `eng/generate_shapes.py` and `eng/generate_values.py` (modified: C# output only, with the TypeScript output dropped); `eng/generate_fixtures.py` (deleted: its only output was the contract-fixtures package); `tests/tooling/test_signed_formats.py` and `tests/tooling/test_artifact_retirement.py` (modified).
  - S47(2), named but unchanged: `tests/tooling/test_con07_generator_guards.py`, `test_con15_d1_execute_plan.py` and `test_con15_schema_root_bindings.py` pass without edits.
  - S50(3): `.gitleaks.toml` (76 inserted lines, an append only). `tests/tooling/test_dependency_admission.py` is also changed by S50(3), but it is in the writes.
  - Supporting inventory edits inside the writes: `eng/provenance/files.json` rows for the new files, and the regenerated `eng/provenance/NOTICE.txt`.
  - The reviewer reports, for rounds 2 and 3, that every changed file is inside the CON.40 writes or in this list.

- **Per retiring identity: last published version, consumer migration and stop record.** The source is `eng/policy/publication-stops/con-40.json` at `15d94d9`, read by this author. Its run and log facts are from read-only `gh run view` and job-log greps by the C8 author, re-checked by the delta reviewer. This author did not re-run them, and no package was downloaded or queried from a registry.

  | Identity | Last published | Last published from `main` | Pinned consumers (immutable, S20(f) decision 2) | State |
  |---|---|---|---|---|
  | npm `@arcforges/proto` (public) | `1.0.0-ci.350.1`, run 37597754997 (#350, job 112721199401), dist-tag `latest`, source `74c298c9` (rolled back, not on main) | `1.0.0-ci.324.1`, run 37388554007 (#324, `330e46bd`) | AI `ec40ec45`: `1.0.0-ci.287.1`; DesktopPlatform `c8280488`: `1.0.0-ci.113.1` | stopped |
  | npm `@arcforges/api-client` (public) | `1.0.0-ci.350.1`, as above | `1.0.0-ci.324.1`, as above | none | stopped |
  | npm `@arcforges/contract-fixtures` (public) | `1.0.0-ci.350.1`, as above | `1.0.0-ci.324.1`, as above | DesktopPlatform: `1.0.0-ci.113.1` | stopped |
  | npm `@arcforges/operator-client` (internal) | `1.0.0-ci.350.1`, as above | `1.0.0-ci.324.1`, as above | DesktopPlatform stage-integration policy rows only, with no dependency declaration (S47(13)) | stopped |
  | Maven `io.github.arcforges:contracts-proto` | last immutable Central release `1.0.0-ci.60.1` (run 35542448605 attempt 2, job 106166419843, "Maven Central: PUBLISHED", source `ef9e0aa`); last mutable `1.0.0-SNAPSHOT` upload by run 350 (job 112721199585) | `1.0.0-SNAPSHOT` by run 324 | none | stopped |
  | Maven `io.github.arcforges:contracts-connect-client` | as for contracts-proto | as for contracts-proto | none | stopped |
  | Maven `io.github.arcforges:contract-fixtures` | as for contracts-proto. The C8 author notes that the run-60 log does not list modules one by one, so this row rests on `docs/releasing.md` at `ef9e0aa` and the `PUBLISHED` line. | as for contracts-proto | none | stopped |

  - Commit `2e04759` (2026-09-20) moved main's Maven version to `1.0.0-SNAPSHOT`. No `vX.Y.Z` tag and no GitHub release exist in Contracts. Main runs 355 and 356 skipped every publisher.
  - **Consumer-migration receipts** (the record's `consumerMigration`; all three tasks are `delivered` on Plan `origin/main` at `335c20fc`):
    - WEB.40 (`ledger/tasks/web-40.md`): Web #35 merged as `c8588681` and #38 as `049f6a58`. The npm Contracts packages left Web in commit `2a5e17f`.
    - AND.40 (`ledger/tasks/and-40.md`): Mobile #24 merged as `43ecb25b` and #25 (PR B) as `6702e281`. PR B retired the Kotlin, KMP and Gradle app.
    - CLOUD.84 (`ledger/tasks/cloud-84.md`, Plan #476 `335c20fc`): Cloud #83 merged as `837fb29f` and #89 as `c291550f`. `c8193f0` removed `@arcforges/proto` and `@arcforges/api-client`, so `@arcforges/ai-internal` is Cloud's one npm Contracts dependency.
  - **Consumer scans** (`git grep` of each `origin/main` after a fetch only). Cloud was scanned at `c291550f`, Web at `dd0a5de3` and Mobile at `6702e281`. In each repository, `consumerReferences` is empty: there is no dependency declaration, lock entry, import or install step for any retired identity. The remaining hits are classified in the record as:
    - binding history (S47(9));
    - immutable receipts, records and notices (S47(10) for Mobile);
    - documentation;
    - the Web `.gitleaks.toml` rows;
    - policy name lists and string-literal negative fixtures.

    The delta reviewer's own grep agrees on the file sets. Its per-identity line counts differ slightly because it grepped different spellings: for example, Cloud contracts-connect-client is 0 by exact coordinate and 2 in the record. Its other nit: the record's "snapshot.json (3 rows)" for DesktopPlatform is 2 lines plus `policy.json:130`.
  - **The stop itself** (the record's `stop`):
    - `eng/contract-packages.json` keeps each row and marks it retired with task CON.40.
    - The TypeScript and Kotlin generators and producer sources are removed.
    - `eng/publish_tools.py` `CHANNELS` is `('nuget', 'npm')`. A `maven` request and any npm identity outside `NPM_IDS` are refused before any registry read or upload.
    - `.github/workflows/ci.yml` has the jobs `candidate`, `verify`, `publish-nuget` and `publish-npm`.
    - A repository grep finds one npm publish call, limited to `NPM_IDS`, and no Maven, Gradle or Sonatype publication step.
    - The receipts are `con-40-npm.json` and `con-40-maven.json`.
    - The stop takes effect from the first main push after the merge: CI run 38074767207 (#363) at `56158219`, which published no retired identity (see "Merge and publication").
  - **No registry action.** `registryActions` (unpublish, deprecate, delete, distTagChange) is empty. The record states that nothing is unpublished, deprecated or deleted, and that no dist-tag is changed.

- **`@arcforges/ai-internal` retained-package receipt.** The publication-stop record's `retained` block reads: "publication unchanged: eng/contracts.py NPM_IDS is ('@arcforges/ai-internal',) (S20(f) decision 13)". The twelve NuGet packages are also "publication unchanged". The ai-internal sources are unchanged except `src/internal/ts/ai-internal/README.md`. That README now states that the npm pipeline is restricted to this package, that the package is published public (`publishConfig`) and that its contract access stays internal (S47(11)). The local candidate holds 12 `.nupkg`, one `.tgz` (`@arcforges/ai-internal`), 13 descriptor sets and a manifest, with no `mavenVersion`. The 13-descriptor-set count is the one reported by the GL implementer and by review rounds 1 and 2. Round 3 reported 15 descriptor sets, and the delta round gave no count. The published versions after the merge are `1.0.0-ci.363.1`: the twelve NuGet packages and `@arcforges/ai-internal` (see "Publication").

- **TypeScript and Kotlin to C# test mapping inventory.** `eng/policy/con-40-test-map.json`, as counted by this author at `15d94d9`:
  - 107 retired cases from 29 source files: 93 from `.mjs` suites, 2 from `.ts` files and 12 from the Kotlin case files. They map to 149 C# anchors, 60 of them distinct.
  - `retained` lists `tests/public/HelloClient/**`, `HelloHost/**`, `SerializationProbe/**` and `tests/public/ai-internal.test.mjs`.
  - `git diff` against `330e46bd` shows 34 deleted files under `tests/public` and one added (`ai-internal.test.mjs`).
  - `Con40SdkCases.TestMap` fails if an anchor is missing or a remaining `tests/public/*.mjs` title is unmapped. StructureTests reports "107 retired TypeScript and Kotlin cases, 149 C# anchors verified" in every gate run.
  - The reviewer's coverage script found every `test()` title of the 22 deleted `.mjs` and `.ts` suites mapped, and every case group of the 7 Kotlin case files.
  - Two negative fixtures are retired with stated reasons, not ported: textual UUID spellings (the C# boundary takes `System.Guid`; the zero-UUID refusal is kept) and the fractional `partNumber` (a C# `long` cannot hold 1.5; schema-refused typed values are used instead).
  - C5 added `SignedFormatCodecs`, so that the CON.16 signed-format vectors run against the generated C# codecs.

- **Docs, policy, dependency-admission and contract-access diff** (`git diff --name-status 330e46bd 15d94d9`):
  - Docs: `docs/releasing.md`, `docs/maven-central.md`, `docs/kotlin-artifacts-plan.md`, `docs/kotlin-grpc-web-plan.md`, `docs/consuming.md`, `docs/architecture.md` and `docs/validation.md`; `README.md`, `AGENTS.md`, `CONTRIBUTING.md`, `SECURITY.md` and `NOTICE`; `src/internal/ts/ai-internal/README.md`. The three Maven and Kotlin pages carry retirement banners and are kept as history.
  - Policy:
    - added: `eng/policy/con-40-test-map.json` and `eng/policy/publication-stops/con-40.json`;
    - modified: `eng/policy/contract-access.json`, `eng/policy/dependency-policy.json`, `eng/policy/licence-boundary.json`, `eng/contract-packages.json` and `eng/foundation-inventory.json`.
  - Dependency admission: receipts `con-40-r1` to `r5` (added), with `dependency-policy.json` bound to `r5`.
  - Provenance:
    - `contract-bindings-con-40-r1` and `-r2` (added);
    - retirement receipts `con-40-npm` and `con-40-maven` (added);
    - `eng/provenance/retirements/contracts-client-wp03-00.json`, accepted unchanged as committed history.
  - Contract access:
    - the 7 retired owner rows are marked retired CON.40;
    - the 2,863 retired distribution rows are kept byte-identical;
    - `retiredOperations` holds the five PDF RPCs;
    - the deleted Gradle and npm workspace build inputs are removed, and the changed root inputs are rebound.

    The reviewer notes (non-blocking) that the top-level `reviewedOn` and `sourceCommit` of `contract-access.json` were not refreshed.
  - CI: `.github/workflows/ci.yml`, `.github/workflows/security.yml` and `.github/dependabot.yml`. `.java-version` is deleted.

- **CON.17 golden vectors and `check_compatibility`.**
  - `git diff --shortstat 330e46bd 15d94d9` is empty, read by this author, for:
    - `eng/compatibility/**` (every pinned `.binpb`, `window.json` and `later-services-window.json`);
    - `fixtures/public/con-17-compat-hash.json`;
    - `src/public/dotnet/ArcForges.Contracts.Foundation/CanonicalSemanticHash.cs`;
    - `tests/StructureTests/SemanticHashCases.cs` and `CompatibilityCases.cs`;
    - the `con17-*` provenance records and receipts;
    - every proto under `internal/` and `public/` (26 files).
  - The retired TypeScript `semantic-hash.ts` and `semantic-hash.test.mjs` are deleted and mapped. The C# `CanonicalSemanticHash` stays the single authority (CON.17).
  - Results (implementer- and reviewer-reported, not re-run by this author):
    - `check_compatibility.py --window` passed with 0 errors at C6;
    - `check_compatibility --window` passed inside the `contracts.py build` gate at `7aeea9d` (rounds 1 to 3) and at `15d94d9` (GL unit and delta round);
    - StructureTests passed in each of those runs;
    - the compatibility and later-services exchanges passed.

- **Retired-marking diff of the sandbox README and `eng/policy/contract-access.json`** (read by this author):
  - `src/internal/dotnet/ArcForges.Contracts.LocalRpc.Sandbox/README.md` gains one paragraph (+2 lines, the only change in that package). It states that `OpenPdf`, `GetPdfPage`, `ExtractPdfText`, `RenderPdfTile` and `ClosePdf` are retired (P2-022, CON.40), and that they stay in the published `arcforges.local.sandbox.v1` schema and the generated package unchanged. No new consumer may call them.
  - `eng/policy/contract-access.json` `retiredOperations` lists those five methods of `arcforges.local.sandbox.v1.ContentSandboxService`, each with `decision` `P2-022` and `task` `CON.40`.
  - `internal/proto/arcforges/local/sandbox/v1/sandbox.proto` and the generated sandbox C# are unchanged.
  - The access check refuses removing a marking and marking an undeclared operation. `contract_access.test.mjs` pins exactly the five marks (reviewer probes, rounds 1 to 3).
  - **`check_compatibility` for `arcforges.local.sandbox.v1`.** `eng/compatibility/later-services-window.json` pins `local-sandbox-1.0.0-ci.287.1.binpb` as previous and minimum for `ArcForges.Contracts.LocalRpc.Sandbox`, with `ContentSandboxService` at 15 methods. The comparison is additive-only. The `--window` check over it passed in the runs above. No log quoted in the journals prints a per-package line for the sandbox. The no-removed and no-reserved-number result rests on the window pass and on the unchanged `sandbox.proto`.

- **Validation actually performed.** These are local runs under CI conditions: `CI=true`, `GITHUB_ACTIONS=true`, a pull_request context with base `330e46b`, a fresh `NUGET_PACKAGES`, .NET SDK 10.0.400 and the workstation build slot. Unless an item says otherwise, they are reported by the GL implementer and by the delta reviewer at `15d94d9`. This author re-ran none of them:
  - `python -I -m unittest discover -s tests/tooling`: 428 tests OK.
  - `dotnet restore --locked-mode` passed, the Release build passed with 0 warnings, and StructureTests (with `Con40SdkCases`) and ArchitectureTests (SDK-01 to SDK-04, and `--hosted` with `GITHUB_JOB=secrets`) passed.
  - `check_naming` (998 files, 0 findings), `check_provenance --owner Contracts --base ''`, `check_licences`, `dependency_admission`, `generate --check`, `check_foundation --generated --self-test` (14 negative cases), `check_serialization`, `check_operation_scope`, `check_compatibility --window` and `node eng/check_contract_access.mjs` all passed. `contract_access.test.mjs` passed 24 of 24, and ai-internal `npm test` 4 of 4.
  - The Native AOT serialization probe on win-x64 passed (31 binary, 51 JSON, 1174 messages).
  - Pack through the S47(7) shim produced 12 `.nupkg`, the ai-internal `.tgz`, 13 descriptor sets and a manifest, and "Verified candidate contents". The descriptor-set count is from the GL implementer and rounds 1 and 2 (round 3 reported 15).
  - gitleaks with the S31 method over the full history, with the hosted flags, found 0 at `15d94d9`.
  - actionlint 1.7.12 reports only the pre-existing `queue` key at `ci.yml:165`.
  - The scripted `package-lock.json` diff is limited to the removed workspaces, their links, 8 packages only they reached, the root manifest entry and the dev flag of `@bufbuild/protobuf` (S47(7)). This diff was run by the C5 implementer and by review rounds 1 to 3 at `7aeea9d`, not at `15d94d9`. It still holds at `15d94d9`, because `package-lock.json` is byte-identical between `7aeea9d` and `15d94d9`.

- **Hosted-only steps** (hosted CI at the reviewed head is authoritative; S47(7)):
  - the Node 24.21.0 and npm 11.19.0 pins (`check_tools`, engine-strict `npm ci`) and the npm 11 pack. Locally, Node 24.20.0 and npm 12.0.2 ran with a shim;
  - the linux-x64 Native AOT serialization probe and its evidence file (locally win-x64);
  - CodeQL (csharp, javascript-typescript, python) and dependency review;
  - the hosted Secret scan (locally WSL Docker by the S31 method);
  - the artifact uploads;
  - the `publish-nuget` and `publish-npm` jobs, which run on main push only.

  These ran in the PR CI run and the main-push run under "Merge and publication". The hosted Build candidate passed at both `15d94d9` and `56158219`, and the publish jobs ran on the main push only.

- **Obligations satisfied** (the graph's parts):
  - WP-03.05 (partial): the C# generated package, descriptor manifest and schema gate stay, and the TypeScript and Kotlin packages retire, with `@arcforges/ai-internal` kept.
  - WP-03.06 (partial): the compatibility window, binpb pins, reserved numbers and golden vectors stay unchanged, and the C# `CanonicalSemanticHash` is the single authority.
- **Substitutes still in use:** none named by the graph for CON.40. The AI and DesktopPlatform pins are immutable published versions kept under S20(f) decision 2, not substitutes.

## Merge and publication

The run, job and PR facts below were read by this author with `gh pr view`, `gh run view` and `gh api` (read-only) on 2026-10-10. The log facts come from the main-push CI job log saved by the coordinator, which this author grepped.

- **PR CI run** at head `15d94d97431cfa3676cd4dda5bf3a2737d368d9f` (pull_request event). The final conclusion of every required context is shown below.
  - CI run [38073599030](https://github.com/ArcForges/Contracts/actions/runs/38073599030) (#362): success.
    - Build candidate: success (job 114275856668, 17:53:53Z to 18:02:31Z).
    - **Verify** (required): success (job 114277562444).
    - Publish NuGet and Publish npm: skipped, as expected on a pull request.
  - Security run [38073598978](https://github.com/ArcForges/Contracts/actions/runs/38073598978) (#367): success.
    - **Secret scan** (required): success (job 114275856312, 17:53:52Z to 18:09:55Z, 16m3s).
    - **Dependency review** (required): success (job 114275856413).
    - **CodeQL (csharp)** (required): success (job 114275856585).
    - **CodeQL (javascript-typescript)** (required): success (job 114275856384).
    - **CodeQL (python)** (required): success (job 114275856402).
  - **CodeQL** (required, the code-scanning results check): neutral (check run 114276052570). GitHub counts a neutral conclusion as passing a required check.
  - The coordinator observed merge state `CLEAN` before merging (coordinator-reported; after the merge `gh` reports `UNKNOWN`).
- **Merge commit:** `5615821917922c7c262b8f43bba1285fa9791444`, a merge commit, not a squash. Its parents are `330e46bd158bfbb7cdc94c7006565c87e27b1cc6` (main before the merge) and `15d94d97431cfa3676cd4dda5bf3a2737d368d9f` (the reviewed head). Its message is "Merge pull request #97 from ArcForges/task/con-40". PR #97 shows `mergedAt` 2026-10-10T18:11:17Z and `mergedBy` `deku2026`.
  - The command was `gh pr merge 97 --merge --match-head-commit 15d94d97431cfa3676cd4dda5bf3a2737d368d9f`. It ran under `integration:Contracts`, held by coordinator `w-deku-20261008-coord`, epoch 1 (role branch `roles/integration-contracts`). The command text is coordinator-reported. The merge type, the parents and the head match are public state.
- **Main-push run** at `56158219` (push event):
  - CI run [38074767207](https://github.com/ArcForges/Contracts/actions/runs/38074767207) (#363): success.
    - Build candidate (job 114279330804): success. Its log shows "CON.40 test map: 107 retired TypeScript and Kotlin cases, 149 C# anchors verified", "Ran 428 tests" and "Verified candidate contents: 1.0.0-ci.363.1".
    - Verify (job 114280399246): success.
    - Publish NuGet (job 114280419212): success.
    - Publish npm (job 114280419629): success.
  - Security run [38074767162](https://github.com/ArcForges/Contracts/actions/runs/38074767162) (#368): success.
    - CodeQL (csharp), CodeQL (javascript-typescript), CodeQL (python) and Secret scan: success.
    - Dependency review: skipped, because it runs on pull requests only.
- **Publication**, version `1.0.0-ci.363.1`, from the main-push CI job log:
  - **NuGet:** 12 pushes to `https://www.nuget.org/api/v2/package`, each followed by "Your package was pushed.":
    - `ArcForges.Contracts.Foundation`, `ArcForges.Contracts.PublicApi` and `ArcForges.Contracts.Events`;
    - `ArcForges.Sdk.Contracts`, `ArcForges.Contracts.Validation`, `ArcForges.Sdk.Client` and `ArcForges.Cli`;
    - `ArcForges.Contracts.LocalRpc.Platform`, `.LocalRpc.Sandbox`, `.LocalRpc.Chat` and `.LocalRpc.Scope`;
    - `ArcForges.Contracts.CloudInternal`.
  - **npm:** exactly one `npm publish` call, and one `+` line: `+ @arcforges/ai-internal@1.0.0-ci.363.1`.
    - The call was `npm publish .../arcforges-ai-internal-1.0.0-ci.363.1.tgz --access public --tag latest --ignore-scripts`, with Node 24.21.0 and npm 11.19.0 (resolved from `.node-version`).
    - The log reads "Publishing to https://registry.npmjs.org/ with tag latest and public access". A signed provenance statement was published to the sigstore transparency log (logIndex 3190848548).
  - **No retired identity published.** The log has no publish step, `+` line or push line for any of the seven retired identities. There is no Maven job and no Maven, Gradle or Sonatype upload step. The retired package names appear only in the WP03.00 gate summary of Build candidate, which lists `retiredPackages` (the seven identities), `retiredDistributionFiles` 2863 and `retiredOperations` (the five PDF RPCs). Other Maven and Gradle words in the log are test names and a fetched archive branch name. The `digest-mismatch: error` lines are the `download-artifact` input setting, not errors.
  - **No registry action.** Nothing was unpublished, deprecated or deleted, and no dist-tag of a retired identity changed. The `latest` dist-tag of the four retired npm identities is therefore unchanged (see Owner note 1). This rests on the job log; no registry was queried.

## Scope (2026-10-10)

- **Delivered outcome (at the reviewed head):**
  - C# is the only first-party SDK language for business clients.
  - The TypeScript and Kotlin generators, generated outputs and producer sources are removed, except `@arcforges/ai-internal`, which keeps its pipeline.
  - The seven retiring identities are marked retired, and new publication of them stops from the first main push after the merge. Their published versions stay immutable and resolvable.
  - The Contracts TypeScript and Kotlin tests are migrated one for one to C#.
  - The release docs, policies, dependency-admission and contract-access records follow the C#-only channel list.
  - The five ContentSandbox PDF RPCs are marked retired, and the schema is unchanged.
- **Status decision: `delivered` (S20(f) decision 3).** `python -I rec.py CON.40` lists three integration `complete` edges: WEB.40, AND.40 and CLOUD.84. On Plan `origin/main` at `335c20fc` all three are `delivered`, not `complete`. `delivery.py` counts a completion prerequisite only when it is `complete` or `inherited`, so all three are open. Their stated conditions, "consumer merged" with no first-party npm or Maven import of the retiring identities, are met at the scanned heads (C8 consumer scans). Those scans are not the completion of those tasks.
- **S47(3) plan-text correction (HelloClient).** The outcome text names `tests/public/HelloClient` among the TypeScript and Kotlin tests to migrate. That is a plan-text error: `tests/public/HelloClient` is a C# project, used by `eng/contracts.py build --inspect-build` and `tests/tooling/test_build_identity.py`, and it stays unchanged. This record corrects the text as S47(3) directs. The reviewer confirmed it unchanged, with `HelloHost` and `SerializationProbe`. The reviewer also notes (non-blocking) that the retired gRPC-Web consumer cases (`package-consumer.ts` and Kotlin `Main.kt`) map to `HelloClient`'s native-gRPC `Usage`. No consumer diagnostic exercises gRPC-Web any more. These are local opt-in diagnostics (P2-017).
- **Rulings applied:**
  - S20(f): consumers are Cloud, Web and Mobile at main; AI and DesktopPlatform keep their immutable pins; retired rows are kept and marked; receipt-driven provenance retirements; C# verification replaces the TypeScript oracle; the Node access-check tooling is kept; the gradle ecosystem and the retired npm groups leave Dependabot; the coordinator claims `integration:Contracts`; `@arcforges/ai-internal` publication is unchanged; delivered, not complete.
  - S47 (1) to (13); S48 (the start edge on CLOUD.84 removed by fix7, Design #348 and Plan #475; the merge and C8 stay gated); S50 (1) to (6); S25.
- **Owner notes** (from the PR body; none changed by this task):
  1. **npm `latest` dist-tag.** The `latest` dist-tag of the four retired npm identities still points at `1.0.0-ci.350.1`. That version was published from the rolled-back commit `74c298c9` and is not admitted as a first-party pin (brief section 10, rolled-back package rule). Changing the dist-tag is a registry action that needs the user. *Next action:* the user decides whether to move `latest` to `1.0.0-ci.324.1`, or leave it.
  2. **MAVEN_\* secrets (optional).** The `MAVEN_*` secrets, `MAVEN_PUBLISH_ENABLED` and the `maven-central` environment are no longer read by any workflow. Removing them is an optional owner follow-up (S50(5)).
  3. **Required CodeQL (java-kotlin) check: done by the user and verified.** Contracts main branch protection required "CodeQL (java-kotlin)", which CON.40 removes, so the check could never report (S50(5)). The user removed it on 2026-10-10. The coordinator read it back with `gh api`, and this author read the same public state again after the merge (`gh api repos/ArcForges/Contracts/branches/main/protection` and `.../rulesets`): the required contexts are Verify, Dependency review, Secret scan, CodeQL (csharp), CodeQL (javascript-typescript), CodeQL (python) and CodeQL; strict is true; `enforce_admins` is true; and the `protectmain` ruleset (23009568, active) was last updated 2026-10-07, so it is unchanged.
- **Dependabot (S47(8) and S51).** State read by this author with `gh pr view` on 2026-10-10, before the merge:
  - **#93** "Bump the protobuf group with 2 updates" (`@bufbuild/protoc-gen-es` and `@bufbuild/protobuf` 2.15.0 to 2.16.0) touches `package.json`, `package-lock.json` and the `package.json` files of the retiring workspaces `src/internal/ts/operator-client`, `src/public/ts/api-client` and `src/public/ts/proto`. It is open, and its Build candidate, Verify and Secret scan checks failed. Under S47(8) it is left to Dependabot's automatic rebase or close after the merge. If it is not auto-closed, it is closed with a scope explanation, but only in a way that keeps its branch (S51: closing can delete the branch, which conflicts with section 0a item 2).
  - **#95** "Bump the actions group across 1 directory with 6 updates" touches `.github/workflows/ci.yml` and `security.yml`, which conflict with C4. It is open, with its checks passing at its own head. Under S47(8) it is left to Dependabot's rebase after the merge, and then the normal admission flow (S51).
  - **#96** "Bump ArcForges.Contracts.PublicApi from 1.0.0-ci.113.1 to 1.0.0-ci.350.1" pins the rolled-back run 350 at `74c298c9`. It is open, and its checks failed. **Never merge** (S50(5), S51). It is not closed by the coordinator; closing it is the user's choice.
  - **Outcome after the merge (S47(8)), read by this author with `gh pr view` and `gh api`:**
    - #93 was closed by Dependabot at 2026-10-10T18:11:27Z, 10 seconds after the merge, in state `CONFLICTING`. Dependabot's comment says the group that created it was removed from the configuration. Its head branch no longer exists.
    - #95 was closed by Dependabot at 2026-10-10T18:14:37Z, in state `CONFLICTING`. Dependabot's comment says the dependencies are updatable in another way. Its head branch no longer exists.
    - Neither was closed by the coordinator, so the S51 branch concern does not arise from any coordinator action.
    - Dependabot opened two replacements: #98 "Bump @bufbuild/protobuf from 2.15.0 to 2.16.0" (18:12:24Z) and #99 "Bump the actions group across 1 directory with 5 updates" (18:14:41Z). Both follow the normal dependency admission flow and are not part of CON.40.
    - #96 is still open. It stays never-merge (S51).
- **Consumer follow-ups (S47(9) and S47(10)), owned by the consumer tasks:**
  - S47(9): the consumer-side binding records that pin digests of Contracts paths, including the Kotlin lockfile digests, stay as immutable history. They are Cloud `eng/generated/contracts-identity.json`, Web `eng/contracts/ArcForges.Contracts.PublicApi/1.0.0-ci.287.1/source.json` and Mobile `eng/policy/contracts-source.json`. *Next action:* re-pinning goes to the completion follow-ups of CLOUD.84, WEB.40 and AND.40.
  - S47(10): Mobile `android-resources-r14` binds the two retired Maven notices. *Next action:* an AND.40 completion follow-up.
- **Recorded follow-ups, not fixed here (S50(4); in the PR body):**
  1. the unused StructureTests foundation-exchange modes (`tests/StructureTests/Program.cs` lines 67 and 121);
  2. the dead `eng/documentation_tools.py`, with the still-active `dokka-*-licence` records for `third-party/dokka`;
  3. the unused TypeScript helpers in `eng/foundation_semantics.py` and the unused `TS_RULES` in `eng/con06_inprocess.py`;
  4. the stale `.prettierignore` entries;
  5. the two negative fixtures retired with reasons (see the test map);
  6. the pre-existing actionlint `queue` key in the `publish-npm` job.

  The C4 commit body wrongly says actionlint was not installed. History is not rewritten, and the PR body corrects it.

  Other non-blocking review items, recorded:
  - the SDK architecture rules self-register through `[ModuleInitializer]` and can end a process that loads the assembly, because `tests/ArchitectureTests/Program.cs` is outside the writes;
  - `contracts.binpb` still takes its schema closure from the retired `@arcforges/proto` catalog row;
  - the C3 and C5 commits are not bisect-green for `check_contract_access.mjs` and `check_foundation --generated` until C6.

  *Owner:* a later Contracts cleanup task. *Next action:* a coordinator ruling on that task's writes.
- **Remaining completion prerequisites and next action (delivered only):**
  1. **Merge and publication (this task):** done. #97 was merged as `5615821917922c7c262b8f43bba1285fa9791444` with `--match-head-commit 15d94d97431cfa3676cd4dda5bf3a2737d368d9f`, after every required context passed. Main-push run 38074767207 published only the twelve NuGet packages and `@arcforges/ai-internal` at `1.0.0-ci.363.1`, and no retired identity. *Next action:* the ledger merge (this record's Plan PR), then the claim is set to `delivered`.
  2. **WEB.40, AND.40 and CLOUD.84 to `complete`:** open. Each completes through its own DLV-41 follow-up and open gaps (see their records). *Next action:* a CON.40 completion follow-up (DLV-41) once all three are complete. It re-runs the consumer scans at their completion heads and confirms that no retired identity was published since the merge.

## Untested coverage (stated expressly)

- **Hosted CI, merge and publication:** observed through `gh` and the main-push job log only (see "Merge and publication"). No registry was queried and no published package was downloaded. Whether the twelve NuGet packages and `@arcforges/ai-internal@1.0.0-ci.363.1` are indexed and resolvable rests on the push and publish log lines.
- **Local gates:** reviewer- and implementer-reported. This author re-ran none of them. The local runs shimmed the Node and npm pins and the npm 12 `pack --json` shape, and ran the AOT probe on win-x64 only. The ArchitectureTests local fixtures once failed on a stale `bin/obj` tree and passed after a rebuild (C8 and round 1), which is not attributed to CON.40.
- **Publication facts:** the run, job and log facts for runs 60, 324 and 350 are from the C8 author's read-only `gh` reads and the delta reviewer's re-check. This author did not re-read those logs. No registry was queried and no package was downloaded. The npm `latest` dist-tag state rests on the run-350 publish log, not on a live registry read.
- **Maven `contract-fixtures` 1.0.0-ci.60.1:** this row rests on `docs/releasing.md` at `ef9e0aa` and the run-level `PUBLISHED` line. No module-level line confirms it. `1.0.0-SNAPSHOT` is mutable, and the provider may expire it.
- **Sandbox compatibility:** no per-package `check_compatibility` output for `arcforges.local.sandbox.v1` is quoted in the journals. The result rests on the `--window` pass and the unchanged proto.
- **gRPC-Web consumer path:** no consumer diagnostic exercises gRPC-Web after the TypeScript and Kotlin consumers retired.
- **Consumer scans:** the scans are at the heads named in C8 (Cloud `c291550f`, Web `dd0a5de3`, Mobile `6702e281`). Later consumer commits are not scanned here.
- **Independence:** the PR author, the review comment and the claimant are under one GitHub account (`deku2026`). Independence rests on the separate session `w-deku-20261008-rev-con-40`.
- **Coordinator-reported facts:** the exact merge command text and the `CLEAN` merge state before the merge. The `integration:Contracts` role (Plan `roles/integration-contracts` at `c7265da0`), the branch-protection state and the merge result were confirmed from public state.
