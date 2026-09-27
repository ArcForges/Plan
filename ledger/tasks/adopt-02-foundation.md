---
task: ADOPT.02.foundation
status: complete
recorded: 2026-09-27
claimant: w-20260927-foundation
epoch: 1
---

## Evidence and review scope

DesktopPlatform integration owner `w-20260927-dgov` (role epoch 2) assigned this slice to `w-20260927-foundation`. This record applies ADP-01 through ADP-10 to FND.01–FND.07 only, against the [ADOPT.01 frozen baseline](../adoption/baseline.md): DesktopPlatform `e5ce94221c13d0014781a760c0865b942350be4d`, Design `722e85641c8afb765dafcab5bc0e84d5a22d5a3c`, and Plan baseline ledger merge `293d53d51e69`.

Reviewed the [foundation task definitions](https://github.com/ArcForges/ArcForges-Design/blob/722e85641c8afb765dafcab5bc0e84d5a22d5a3c/docs/planning/delivery/lanes/foundation.md), all mapped [WP-04 obligations](https://github.com/ArcForges/ArcForges-Design/blob/722e85641c8afb765dafcab5bc0e84d5a22d5a3c/docs/planning/work-packages/04-identity-error-and-versioning-primitives.md), and these exact frozen inputs:

- `src/BuildingBlocks/ArcForges.Foundation/`: net10.0 project and namespace `ArcForges.Foundation`, `AssemblyPlaceholder.cs`, README explicitly identifying a retained unpublished scaffold, and lock file.
- `src/BuildingBlocks/ArcForges.Application.Abstractions/`: corresponding net10.0 project, namespace and `AssemblyPlaceholder.cs`, README and lock file.
- `tests/`: architecture/build-identity and native probe tests, with no Foundation primitive or round-trip suite. Source/test symbol search found none of the required execution, revision, monotonic-time or outcome implementations.
- `eng/policy/`: no `reason-codes.json`; `eng/packaging/packages.json`: neither Foundation nor Application.Abstractions admitted. Published candidate `1.0.0-ci.27.1` comprises the ten build/native packages listed in the baseline, not these capabilities.
- Frozen open PR inventory: none. [Retarget PR #64](https://github.com/ArcForges/DesktopPlatform/pull/64), reviewed `1657b2e505dec55d5fb60f485c2f727d7091a722`, merged at the frozen head, passed all twelve retained checks. [Original publication run 36334843593](https://github.com/ArcForges/DesktopPlatform/actions/runs/36334843593) succeeded; this reused receipt proves only the existing packages, not FND outcomes.

## Per-task classifications and scope binding

All paths below are relative to DesktopPlatform. Existing project/package identities remain unchanged. No task is inherited, so this slice creates no inherited task records.

| Task | Classification | Evidence and bound write scope | Remaining obligation and evidence | Conflicts / blockers |
|---|---|---|---|---|
| FND.01 | gap | Foundation scaffold above; bind `src/BuildingBlocks/ArcForges.Foundation/**` to its existing project and namespace. | WP-04.00 except FND.07 parts: adapt published Contracts.Foundation exact UUID/revision/enum/error types with validation/generation; identifier/axis compile-negative and absent/default/unknown vectors. Add the exact producer pin, reviewed admission and regenerated lock through build-config protocol. | No conflict; requires CON.91 delivered/inherited ledger evidence before implementation. |
| FND.02 | gap | Foundation and Application.Abstractions scaffolds; bind both existing project trees, preserving their identities. | Full WP-04.01: distinct immutable owner/command/invocation/run/step/attempt identities, canonical hash, effect/retry algebra, typed result/cancellation and lifecycle ports; memory-only vectors, no storage implementation. Add project/dependency/test integration through shared build-config protocol. | No conflict; CON.91 start prerequisite; durable receipt acceptance remains completion prerequisite PLT.01. |
| FND.03 | gap | No revision/sequence implementation or tests; bind existing Foundation tree. | Full WP-04.02: non-interchangeable Revision/SequenceNumber, expected-revision conflict and sequence-gap semantics, including compile-negative comparison evidence. | No conflict; CON.91 start prerequisite. |
| FND.04 | gap | No clock types or tests; bind existing Foundation tree. | Full WP-04.03: distinct Instant/MonotonicTimestamp and injectable clock, canonical instant plus meaningful originating zone; locale, DST and clock-adjustment duration evidence. | No conflict; no additional start prerequisite after this slice. |
| FND.05 | gap | No Outcome/reason implementation; bind Foundation tree and new `eng/policy/reason-codes.json`. | Full WP-04.04: source-generated stable registry, category/retry/effect/message metadata, success/failure/cancellation distinction, required identity/AST codes, invalid-request mapping and safe unknown-reader fallback; completeness and negative vectors. Registry changes use append protocol and are generated, not manually maintained. | No conflict; CON.91 start prerequisite. |
| FND.06 | gap | No axis implementation/tests; bind existing Foundation tree. | Full WP-04.05: all nine distinct axes, parsing/comparison/open and partial ranges; every cross-axis assignment rejected by compile-negative suite. Build-config additions use declared append protocol. | No conflict; no additional start prerequisite after this slice. |
| FND.07 | gap | Foundation and Application.Abstractions absent from actual `eng/packaging/packages.json`; bind that file and `eng/version-sources.json`, preserving published identities and original candidate publication. | Full WP-04.90, external-consumption part of WP-04.00 and TS/Kotlin exact-value projection contribution: admit verified packages, record publication and exact producer identity, actual C#/TS vectors against Contracts fixtures for out-of-safe-range integers, absence/unknown values, duplicate commands and unknown effects. | No conflict; starts after FND.01–FND.06 and CON.91 delivered outcomes. |

## Validation and completion

Performed read-only frozen-source/project/inventory inspection and obligation comparison. Ledger consistency is checked with explicit retained Plan and current Design roots before review. Independent review and this ledger PR's exact reviewed/merge commits are recorded in the ADOPT.02.foundation claim and merged PR history; this file cannot embed its own future merge SHA.

No product builds, public downloads, archive/hash audits or runtime checks were performed. No substitutes introduced. Identifier safety, cross-language correctness, idempotency, time handling, error behavior, package publication and product integration remain untested gaps; scaffold and baseline CI success do not accept them.

No D-001 conflict or out-of-scope adjustment was found. Retired native families/policy data remain owned by GOV.17/GOV.18 and are not cleaned or certified here. Merging this record opens the seven tasks subject to their individual prerequisites; it closes only this adoption review, not any FND implementation or repository adoption.
