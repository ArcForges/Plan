---
task: ADOPT.02.policy
status: complete
recorded: 2026-09-27
claimant: w-20260927-dother
epoch: 1
---

# DesktopPlatform policy adoption

## Inputs and scope binding

Assigned reviewer by DesktopPlatform integration owner `w-20260927-dgov`, role epoch 2. Reviewed against [frozen baseline](../adoption/baseline.md#desktopplatform), source `e5ce94221c13d0014781a760c0865b942350be4d`, Design `722e85641c8afb765dafcab5bc0e84d5a22d5a3c`, each mapped task outcome/scope/validation/evidence and its named work-package obligation parts. Frozen open PR inventory is empty. The complete tracked source inventory, bootstrap/native release records, package allowlist, source reconciliation and current project files are the evidence basis.

No ArcForges.Policy project exists. Build.Policy and eng/policy enforce build/repository rules, not scoped runtime configuration, deterministic rollout or last-known-good caching.

Existing project/package identities are preserved. Paths in the table are repository-relative exact bindings of the planned scopes: absent paths are additions, not renamed existing libraries. New project/lock/inventory entries must use the declared owner protocols; a required edit outside an authorized task scope or declared shared resource first requires a reviewed planning repair. Empty task write scopes mean acceptance over prerequisite-owned artifacts, not permission to modify arbitrary source.

## Classifications

| Task / mapped obligation parts | Classification | Evidence / bound scope | Remaining work and evidence | Conflicts / blockers |
|---|---|---|---|---|
| POL.09; WP-44.05 (client-side consumption of scoped resolution/explainability); WP-44.07 (client caching, staleness threshold, fallback to last-known-good then compiled defaults, staleness visible, mid-operation application timing); WP-44.03 (client execution of the deterministic rollout hash so the same subject/version selects the same result on-device) | gap | No ArcForges.Policy project exists. Build.Policy and eng/policy enforce build/repository rules, not scoped runtime configuration, deterministic rollout or last-known-good caching. Scope: DesktopPlatform:src/BuildingBlocks/ArcForges.Policy/** | A single ArcForges.Policy building block resolves, caches, and explains policy identically under Native AOT, falling back from staleness to last-known-good to compiled defaults with the staleness state always visible, and a change never takes effect mid-operation inconsistently. Required evidence: Fallback-chain-to-compiled-defaults test; AOT-clean publish result. | No unresolved implementation conflict; normal start prerequisites: POL.04, CON.12, CON.22. Completion additionally requires POL.11, POL.08. |

## Evidence, validation and limits

- Frozen instruction PR #64 was reviewed at `1657b2e505dec55d5fb60f485c2f727d7091a722` and merged as the frozen source. [Main run 36334843593](https://github.com/ArcForges/DesktopPlatform/actions/runs/36334843593) published ten packages at `1.0.0-ci.27.1`. This supports retained build/probe infrastructure only; no missing capability or acceptance is inferred.
- Source evidence: `docs/platform-bootstrap.md`, `docs/native-package-release.md`, `eng/packaging/packages.json`, `eng/policy/reconciliation/source.json`, `DesktopPlatform.slnx`, `src/BuildingBlocks/**/AssemblyPlaceholder.cs`, `src/DesktopHelpers/ArcForges.ContentSandbox/Program.cs`, `native/shared/include/arc/arc_native_abi.h`, `native/arcslate-image-abi/include/arc/arc_slate_image_abi.h`, and the complete frozen Git tree. No claimed current product result is based on an unmerged branch or a historical dated plan.
- Every mapped task is classified once. No task is classified fully inherited, so no inherited completion records are created. Inherited-with-adjustment rows preserve existing work while leaving the named remaining acceptance open.
- Removed-product Media/Colour/Otio/Metal material is retired under ADP-10 and owned by GOV.17/GOV.18. Adoption neither performs nor certifies cleanup; immutable publications and provenance remain preserved.
- Validation performed: source/obligation/receipt consistency review and Plan delivery check. Independent exact-head review and merge are recorded in the PR and claim audit trail. No product build, artifact download, runtime/provider/device/browser/installed-consumer execution or publication recheck.
- P2-017 controls validation venue and cadence. Required future real runtime/hardware/provider acceptance cannot be replaced by compilation or fixtures; unavailable optional local environments are reported honestly, without provisioning. Existing probes are not production substitutes. This ledger opens only the slice tasks subject to prerequisites and any recorded conflicts, not any wider gate or commercial release.
