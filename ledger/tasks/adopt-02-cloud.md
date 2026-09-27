---
task: ADOPT.02.cloud
status: complete
recorded: 2026-09-27
claimant: w-20260927-dother
epoch: 1
---

# DesktopPlatform cloud adoption

## Inputs and scope binding

Assigned reviewer by DesktopPlatform integration owner `w-20260927-dgov`, role epoch 2. Reviewed against [frozen baseline](../adoption/baseline.md#desktopplatform), source `e5ce94221c13d0014781a760c0865b942350be4d`, Design `722e85641c8afb765dafcab5bc0e84d5a22d5a3c`, each mapped task outcome/scope/validation/evidence and its named work-package obligation parts. Frozen open PR inventory is empty. The complete tracked source inventory, bootstrap/native release records, package allowlist, source reconciliation and current project files are the evidence basis.

Security contains AssemblyPlaceholder.cs and no session adapters. No ArcForges.Sync project or sync_outbox implementation exists.

Existing project/package identities are preserved. Paths in the table are repository-relative exact bindings of the planned scopes: absent paths are additions, not renamed existing libraries. New project/lock/inventory entries must use the declared owner protocols; a required edit outside an authorized task scope or declared shared resource first requires a reviewed planning repair. Empty task write scopes mean acceptance over prerequisite-owned artifacts, not permission to modify arbitrary source.

## Classifications

| Task / mapped obligation parts | Classification | Evidence / bound scope | Remaining work and evidence | Conflicts / blockers |
|---|---|---|---|---|
| CLOUD.18; WP-22.07 (full) | gap | Security contains AssemblyPlaceholder.cs and no session adapters. No ArcForges.Sync project or sync_outbox implementation exists. Scope: DesktopPlatform:src/BuildingBlocks/ArcForges.Security/** | System browser, per-product redirects, secure storage and installation-bound tokens are integrated into Platform client primitives; each client owns its own session, no token sharing/device SSO. Required evidence: per-client session isolation results | No unresolved implementation conflict; normal start prerequisites: CLOUD.12, PLT.40. |
| CLOUD.38; WP-25.01 (full) | gap | Security contains AssemblyPlaceholder.cs and no session adapters. No ArcForges.Sync project or sync_outbox implementation exists. Scope: DesktopPlatform:src/BuildingBlocks/ArcForges.Sync/** | The single sync_outbox schema exists client-side: acked shadow plus pending journal, frozen batch hash/revision/range, explicit supersession lineage; a user conflict resolution appends a new local event and never edits the frozen failed batch. Required evidence: every local edit has a durable outcome and exactly one live submission lineage; no conflict silently drops pending content | No unresolved implementation conflict; normal start prerequisites: PLT.01. Completion additionally requires CLOUD.39. |

## Evidence, validation and limits

- Frozen instruction PR #64 was reviewed at `1657b2e505dec55d5fb60f485c2f727d7091a722` and merged as the frozen source. [Main run 36334843593](https://github.com/ArcForges/DesktopPlatform/actions/runs/36334843593) published ten packages at `1.0.0-ci.27.1`. This supports retained build/probe infrastructure only; no missing capability or acceptance is inferred.
- Source evidence: `docs/platform-bootstrap.md`, `docs/native-package-release.md`, `eng/packaging/packages.json`, `eng/policy/reconciliation/source.json`, `DesktopPlatform.slnx`, `src/BuildingBlocks/**/AssemblyPlaceholder.cs`, `src/DesktopHelpers/ArcForges.ContentSandbox/Program.cs`, `native/shared/include/arc/arc_native_abi.h`, `native/arcslate-image-abi/include/arc/arc_slate_image_abi.h`, and the complete frozen Git tree. No claimed current product result is based on an unmerged branch or a historical dated plan.
- Every mapped task is classified once. No task is classified fully inherited, so no inherited completion records are created. Inherited-with-adjustment rows preserve existing work while leaving the named remaining acceptance open.
- Removed-product Media/Colour/Otio/Metal material is retired under ADP-10 and owned by GOV.17/GOV.18. Adoption neither performs nor certifies cleanup; immutable publications and provenance remain preserved.
- Validation performed: source/obligation/receipt consistency review and Plan delivery check. Independent exact-head review and merge are recorded in the PR and claim audit trail. No product build, artifact download, runtime/provider/device/browser/installed-consumer execution or publication recheck.
- P2-017 controls validation venue and cadence. Required future real runtime/hardware/provider acceptance cannot be replaced by compilation or fixtures; unavailable optional local environments are reported honestly, without provisioning. Existing probes are not production substitutes. This ledger opens only the slice tasks subject to prerequisites and any recorded conflicts, not any wider gate or commercial release.
