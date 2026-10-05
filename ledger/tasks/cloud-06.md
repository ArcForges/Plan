---
task: CLOUD.06
status: delivered
recorded: 2026-10-05
claimant: w-c20261005-cloud06
epoch: 1
---

# Shared atomic family guarded-batch engine (WP-21.05, engine and fixed module lock order)

The generic engine is merged and green. The state is `delivered`, not `complete`: the graph records CLOUD.63 as a completion prerequisite of CLOUD.06 (`complete: [CLOUD.63]`, "at least two real module family participants exercising the engine under contention"), and WP-21.05's own gate needs it ("two Containers contend, stale holder cannot finalize, exact credits and sync cursor safety"; exact credits are Commerce, cursor safety is Sync). CLOUD.06 proves the generic mechanism they compose. Follow-up: when CLOUD.63 is complete, a worker claims the completion follow-up and runs the real-participant contention scenario.

How to read this record: **claimant-reported** results come from local runs on the claimant's Windows 11 workstation (Node 24.20.0, off the pinned 24.21.0 which is the CI authority; .NET 10.0.401). **Reviewer-reported** results are what the independent reviewer wrote on the pull request (separate worker identity, same GitHub account). Verifiable from GitHub: the pull requests, review comments, merge commits and workflow runs named here.

## Evidence

- **Planning pair.** [Design #244](https://github.com/ArcForges/ArcForges-Design/pull/244) (reviewed head `714d244979325b72b2ef359efb8394f8cc53b151`, merge `fd1f516`) and [Plan #321](https://github.com/ArcForges/Plan/pull/321) (head `8ad7c8a07ddebec0c52757379149349bd10113bb`, merge `3eb43f4b`) bound the write scope (the family registry and grammar in the plan generator, the `platform_command_guard` table and migration, tests, a workerd run, admission and provenance successors, one document) because the CLOUD.02 ownership rule forbids a cross-module plan; they added the CLOUD.03 start edge, amended D1 profile section 4 and model 01 (`platform.command_guard`), and named the minimal edits of existing tests. Both approved by an independent reviewer.
- **Implementation.** [Cloud #49](https://github.com/ArcForges/Cloud/pull/49), merged 2026-10-05 as `32fe8f48c1df87a488687921303f1b5d8c92b6f2` at reviewed head `13b10d89ac83d14c810cc69a03a634b43f2696a6` ([approval](https://github.com/ArcForges/Cloud/pull/49#issuecomment-5997559226) by r-c20261005-cloud06-code, one round, no findings requiring change).
- **What it delivers.** The closed family registry (`storage/plans/families.json`, shipped **empty**) and plan grammar (`families.<family>.<name>`); guards generated from five primitives (authorization, revision, policy, balance, lease) against the physical manifest; the SU-04 order (guards, mutations, a generated release; `platform` first among guards and last among mutations; class and stable key within a module); participant, ownership and guard-coverage rules; plan identity covering the expanded SQL and a generated listing (`families.expanded.json`); `platform_command_guard` (migration `0022`, check `af_guard_failed` classified as `precondition`); the C# `SharedFamilies` engine (`ModuleLockOrder`, `FamilyPlanVerifier`, `FamilyGuards`, `FamilyUnitOfWork`, `FamilyContributor`, `FamilyExecutor` with bounded reread under the original command after a false guard only). The manifest hash and the Worker dictionary are unchanged. Provenance: receipt `cloud-06-r1`, profile `cloud-release-r30`, records `cloud-06-cloud-*-r1`, chained from `com-05-r1` / `r29`.
- **Hosted CI on the reviewed head** (run 37330545030): Source on ubuntu and windows, dependency audit with the all-branch secret scan, four CodeQL jobs, the Native AOT image and Worker build and Verify succeeded; deploy and proof jobs skipped by design.
- **Main push** `32fe8f4` (run 37332893609): Source (ubuntu, windows) and the four CodeQL jobs succeeded; **the all-branch secret scan failed with one leak (details redacted) and Verify failed with it.** The same scan fails on `task/cloud-04` and `task/cloud-08` and on two Dependabot branches at the same time, so the finding is in a ref other than this task's merged commits (not located: no local gitleaks); it is open and reported to the coordinator. This is **not** a publication-confirmed state until that scan is green.
- **Local evidence (claimant-reported):** `npm test` 555/555 (new: 61 generator/primitive/vector cases, 22 cases running the generated SQL on the real migrations in node:sqlite), dependency admission 18, `test:artifact` 10/10, `check:plans`, `check:physical`, policy, licence, provenance, prettier, biome, tsc; `dotnet test --solution Cloud.slnx` 754/754 (498 Cloud tests, 91 of them in `SharedFamilies`; 256 architecture tests); `dotnet format` clean; seven deliberate mutants each failed a test. **Opt-in `npm run test:d1:families:local` on workerd's D1 under Miniflare, 5/5:** 10 false guards each refused whole as `precondition`; a duplicate receipt and a CHECK failure after passing guards rolled the guarded mutations back as `constraint`; 25 rounds of 4 simultaneous writers on one revision gave 25 commits and 75 whole-batch refusals; a stale lease holder cannot finalize; balances compare exactly at 2^53+1 and the int64 maximum.
- **Reviewer-reported:** at the exact head `npm test` 555/555, dependency, plans, physical, licence and provenance checks (the chain recomputes), the workerd run; seven independent mutants all killed (guard always true, lease fence dropped, balance exact columns dropped, revision COALESCE removed, guard-table naming rule removed, migration CHECK loosened, ownership prefix bypassed); security and correctness review of the generated guards (no injection or hand-written guard path), ordering and bounded reread. The reviewer did not re-run dotnet tests (hosted jobs green).

## Known gaps and surviving notes (reviewer's low findings, accepted as stated)

- A revision or authorization guard's `by` list is not checked to cover the table's primary key, and `scope:` on a tenant key is optional; plan authors and the reviewed `families.expanded.json` carry it. Module tasks keep `scope:` on tenant keys.
- A lease's expiry is compared with a caller-supplied instant (`until > now`); a module that writes needs some guard of its own, not one per written row (review convention, SU-04).
- A duplicate delivery whose original already committed ends as a guard refusal after the bounded rereads unless the caller's build callback checks the receipt first (CLOUD.04's commit executor and the module tasks own that check).
- **SU-04 gap for the Architecture Owner:** Support and TrustSafety have no position in the 17-module order although model 01 names TrustSafety in operator mutations; the engine refuses both (registry parser, generator, C#) until the order is extended. Raised in Design #244.
- The write scope as literally listed in the graph is the bound scope of the merged Design #244 (the diff exceeds `SharedFamilies/**` by design).

## Coordination

CLOUD.04 ([Cloud #51](https://github.com/ArcForges/Cloud/pull/51)) already takes the guard table and `0022` (byte-identical to this task's migration) but not the family engine or generator; it rebases and reseals after this merge (next profile `r31`).

## Untested coverage and stated limits

- **Not run, deferred live checks** (need the `RES-cloud-deployment` lease and the proof environment, never CI): that the provider's REST `batch` is one atomic transaction (the binding batch was observed atomic on workerd); real D1 limits and latency; a deployed contention run. CLOUD.70 owns the deployment step that applies `0022`.
- **Not claimed:** two real Container processes, exact credits and sync cursor safety (CLOUD.63, Commerce and Sync participants); any Design family or family plan (none ships: the participant lists are the Architecture Owner's and module tasks append theirs); the Abstractions-level port by which a module project hands contributions to the coordinator (module tasks, COM.16's generic port).
- **Not run locally:** the Native AOT publish (hosted CI built it), macOS, the pinned Node 24.21.0.
- SQLite and workerd are not Cloudflare; the fixture family is a test fixture, not a Design family.
