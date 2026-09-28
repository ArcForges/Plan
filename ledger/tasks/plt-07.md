---
task: PLT.07
status: complete
recorded: 2026-09-28
claimant: af-20260928-p02
epoch: 1
---

# Derived-store abstraction and storage-pressure model

## Evidence

- Implementation: DesktopPlatform [PR #78](https://github.com/ArcForges/DesktopPlatform/pull/78), final reviewed head `1aa3bd643eb0269aec11b377851972bebf0a5b3a` on base `7cccfcc91f8014c7753e91bcfdef21278b21edda`; independent exact-head clean review [5340776047](https://github.com/ArcForges/DesktopPlatform/pull/78#pullrequestreview-5340776047). Merged as `a893dbc69c6c0dc8c6b5d85cef6eb39097c7a1b3`.
- WP-07.06 (full): added a `DerivedStore` abstraction with canonical-source snapshot/rebuild, declared rebuild cost, and staged replacement that keeps the old derived snapshot intact if projection or pre-publication replacement fails. The storage-pressure model plans deterministic eviction by rebuild cost and last-use, targets only registered derived stores, validates the complete plan, and acquires all planned-store locks before validation/deletion so concurrent usage changes cannot race a delete. Eight defined local derived kinds each have delete-and-rebuild coverage; eviction tests assert canonical data remains unchanged. Regression tests cover failure after replacement staging and concurrent usage updates during eviction.
- Latest-head hosted PR gate [run 36440757255](https://github.com/ArcForges/DesktopPlatform/actions/runs/36440757255) completed successfully, including aggregate CI, managed-packages/pack and accounting, ArchitectureTests (100/100), native Windows, Linux/Windows Local RPC AOT compile, Avalonia AOT probe, and applicable policy/security checks.
- Normal post-merge [Publish NuGet run 36442895007](https://github.com/ArcForges/DesktopPlatform/actions/runs/36442895007) completed successfully on merge commit `a893dbc69c6c0dc8c6b5d85cef6eb39097c7a1b3`; publisher job `109001002744` verified and pushed the same candidate bytes using OIDC. Candidate artifact `nuget-candidate-36442895007-1`, artifact `10979059497`, size 5,552,006 bytes, archive digest `sha256:d8b79204427d95671337390b9c9af7ef5c37dcaf6d4a4598dd12d2babfd0eead`. The verified candidate version is `1.0.0-ci.48.1`, source `a893dbc69c6c0dc8c6b5d85cef6eb39097c7a1b3`, containing the eight existing repository packages: `ArcForges.Build.Policy`, `ArcForges.Native.Abstractions`, `ArcForges.Native.Image`, `ArcForges.Native.Image.Runtime.win-x64`, `ArcForges.Foundation`, `ArcForges.Application.Abstractions`, `ArcForges.Capabilities` and `ArcForges.Persistence.Sqlite`. Independent flat-container index GETs confirmed exact `1.0.0-ci.48.1` visibility for all eight package IDs. No package payload was downloaded for this verification.
- Validation actually performed: pinned .NET SDK 10.0.400 locked solution restore and full-solution format verification passed; Release solution build passed with zero warnings/errors; `ArcForges.Persistence.Derived.Tests` passed 15/15; accounting self-tests passed 10/10. Candidate dependency policy passed (51 NuGet coordinates, 10 Python dependencies, 236 inputs), reconciliation passed (67 active projects, 166 historical), provenance passed against base `7cccfcc` (538 files, 140 records), licence boundary passed (39 projects), and managed runtime ownership passed (7 repositories). Hosted exact-head CI is the final authority for the complete policy/build/AOT/pack gate; local ArchitectureTests were limited by the unchanged GeneratedRegex evaluator (`CS8795`) and are not claimed as passing locally.
- Obligations satisfied: [WP-07.06](https://github.com/ArcForges/ArcForges-Design/blob/main/docs/planning/work-packages/07-local-persistence-foundation.md#rule-wp-07.06) — full; PLT.07 has no completion prerequisites.
- Substitutes still in use: none. The offline regression tests use in-memory canonical-source and derived-store fixtures; they do not claim a product-owned persistent adapter.
- Untested coverage: no product-specific derived-store adapter/integration or hardware power-loss test is claimed; those are outside PLT.07's defined mechanism-and-offline-validation scope.
- Remaining completion prerequisites and next action: none. This ledger record completes PLT.07.
