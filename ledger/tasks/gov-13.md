---
task: GOV.13
status: complete
recorded: 2026-09-28
claimant: af-20260928-g02
epoch: 1
---

# Invariant-to-test accounting

## Delivery and truthful coverage result

- GOV.13 delivers the invariant-accounting mechanism and its CI evidence path. On the merged source commit, the complete canonical catalog and durable registration roster each contain 406 unique invariant IDs. The report classifies all 406 as `not-yet-implemented`: 0 enforced-and-passing, 0 enforced-and-failing, 406 not-yet-implemented. This is an honest report of current coverage, not a claim that all product invariants are implemented.
- The exact package-05 candidate universe was audited against each invariant's `plannedVerification` and completion gate. The audit contains 44 candidates; none of the actual stable cases fully satisfies an invariant's complete obligation. The nearest `ContextSnapshotTests.ProviderRefusesCrossProductInstanceOrEpochBeforeInvokingOwner` case remains explicitly partial for I-024 and I-027 and is not registered as coverage. No API-to-test map or name-based inference was used. Other-owner invariants remain NYI without an accepted external result receipt.
- The TRX normalizer requires exactly one result row per definition `testId`, while distinct parameterized definition IDs may share and aggregate under the stable case FQN. Missing/extra suites, malformed or duplicate definition/result IDs, inconsistent counters, skipped outcomes, and invalid provenance fail closed; skipped tests never count as coverage.
- The generated accounting report, normalized owner receipt, and six TRX files are retained as CI artifacts only; no generated report or ignored TRX was checked in. The accounting result is bound to the exact repository, source commit, workflow run, and attempt.

## Implementation, review, and source validation

- DesktopPlatform [PR #88](https://github.com/ArcForges/DesktopPlatform/pull/88) changed the scoped accounting, roster, audit, tests, workflow, and provenance inventory. Exact reviewed head `f3144a1c7a6023063b8bb87746e9f27813f89ff3` was based on `9e3cff458fbef1ce4326c5d8141e478ac9d11b6b`, independently reviewed GOV.13-only with no findings ([review 5339639222](https://github.com/ArcForges/DesktopPlatform/pull/88#pullrequestreview-5339639222)), and passed all 15 exact-head PR checks in [run 36430027596](https://github.com/ArcForges/DesktopPlatform/actions/runs/36430027596). It was merged as `7cccfcc91f8014c7753e91bcfdef21278b21edda`.
- Pinned .NET 10.0.400 local validation passed: locked restore, format verification, Release solution build with 0 warnings/errors, and 111 `eng` Python tests. Provenance passed for 528 files/140 records; workflow YAML parse and `git diff --check` passed. The hosted suite also supplies the naming/secret and native configure receipts unavailable in the local environment.
- Post-merge explicit-root Plan/Design delivery validation passed with 437 tasks, 50 adoption slices, 99 generated views current, 0 warnings, and a valid ledger. This ledger is based on the Plan main including AND.22 merge `4a4247cf4231dfd2461eaaae4fc6595fc444e52d`.

## Retained hosted accounting evidence

- Post-merge Publish NuGet workflow [run 36433382366](https://github.com/ArcForges/DesktopPlatform/actions/runs/36433382366) completed terminal success on source/merge `7cccfcc91f8014c7753e91bcfdef21278b21edda`; policy, provenance, native, managed pack/AOT, candidate CI, and publisher jobs succeeded. Its `invariant-accounting-36433382366-1` artifact is ID `10974812188`, 52,629 bytes, digest `sha256:50335a3da70c3a45ba4b277a117fa8b12d3f4186b38b2eed5e5dc25a24fb2392`. The report confirms catalog/roster/scan counts 406/406/complete, zero registrations, and 406/406 NYI. It binds run `36433382366`, attempt 1, and merge commit above.
- The retained owner-results receipt SHA-256 is `84a339fd43b0e60d3229b9cd4904d8c1c4aaf7af3bdb480636c4443b0db6eacb`. Six source TRXs reconcile with zero failures: Architecture 100/100 passed; Foundation 65/65; Persistence.Resources 19/21 passed and 2 skipped; Capabilities 15/15; Security 23/23; Persistence 81/81. The skipped resource cases remain non-covering.
- The report's exact inputs include catalog `eng/policy/invariants.json` (406 rows, SHA-256 `ab262ca5cad9a717d9d5b0c77eca6c9249ed825d422dd47c8976ecda34454f05`), roster `eng/accounting/invariant-test-cases.json` (406 rows, 0 registered, SHA-256 `fa0ad3b8879317b9fd53bf29d040a30793fc6df41ea87e40b83fcad1b050f00d`), and the 44-candidate package-05 audit based on source `784f238c4c01590e8de6fe5e1472ed79b70ac222` (SHA-256 `7eb5c0805e390ae55e8e4b31a6b8a2e955f0d9fc0ec84d42dfa69819d90ba16b`).

## Normal publication and limits

- The same post-merge workflow's publisher job `108968583064` successfully exchanged OIDC identity and published the verified candidate. Candidate `nuget-candidate-36433382366-1` is artifact ID `10974867077`, 5,552,236 bytes, digest `sha256:ab3b71160e477742defb9d962c89779c2245faee9feab77d8b83e37e3282003e`. At `2026-09-28T14:24:56Z`, independent NuGet flat-container index queries confirmed version `1.0.0-ci.47.1` visible for all eight allowlisted packages: ArcForges.Build.Policy, ArcForges.Native.Abstractions, ArcForges.Native.Image, ArcForges.Native.Image.Runtime.win-x64, ArcForges.Foundation, ArcForges.Application.Abstractions, ArcForges.Capabilities, and ArcForges.Persistence.Sqlite. Only index metadata was queried; package payloads were not re-downloaded.
- No invariant implementation is implied by the accounting report, and no skipped test or partial case is counted as coverage. Device/runtime behavior and any test beyond the six registered source suites are not claimed. GOV.13's mechanism and truthful baseline are complete; future invariant registrations require tests whose assertions fully satisfy their recorded obligations.
