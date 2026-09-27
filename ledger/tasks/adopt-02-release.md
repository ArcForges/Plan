---
task: ADOPT.02.release
status: complete
recorded: 2026-09-27
claimant: w-20260927-dother
epoch: 1
---

# DesktopPlatform release adoption

## Inputs and scope binding

Assigned reviewer by DesktopPlatform integration owner `w-20260927-dgov`, role epoch 2. Reviewed against [frozen baseline](../adoption/baseline.md#desktopplatform), source `e5ce94221c13d0014781a760c0865b942350be4d`, Design `722e85641c8afb765dafcab5bc0e84d5a22d5a3c`, each mapped task outcome/scope/validation/evidence and its named work-package obligation parts. Frozen open PR inventory is empty. The complete tracked source inventory, bootstrap/native release records, package allowlist, source reconciliation and current project files are the evidence basis.

Existing eng/packaging implements prerelease NuGet/native candidate production. eng/packaging/release and eng/release do not exist; bootstrap candidate publication is not production updater signing/cutover or full-family readiness.

Existing project/package identities are preserved. Paths in the table are repository-relative exact bindings of the planned scopes: absent paths are additions, not renamed existing libraries. New project/lock/inventory entries must use the declared owner protocols; a required edit outside an authorized task scope or declared shared resource first requires a reviewed planning repair. Empty task write scopes mean acceptance over prerequisite-owned artifacts, not permission to modify arbitrary source.

## Classifications

| Task / mapped obligation parts | Classification | Evidence / bound scope | Remaining work and evidence | Conflicts / blockers |
|---|---|---|---|---|
| REL.10; WP-50.02 (the shared production update-feed population (hashes, compatibility ranges, minimum versions) and code-signing/publication-pointer cutover only; ArcScope update-matrix testing is REL.02) | gap | Existing eng/packaging implements prerelease NuGet/native candidate production. eng/packaging/release and eng/release do not exist; bootstrap candidate publication is not production updater signing/cutover or full-family readiness. Scope: DesktopPlatform:eng/packaging/release/** | The production update feed is populated with hashes/compatibility ranges/minimum versions for the ArcScope desktop application across Windows/macOS/Linux, store and package-manager listings point at the corresponding signed installer, and a blocked bad version is refused by both the feed and compatibility policy. Required evidence: Feed population record; signed-installer listing consistency; blocked-bad-version refusal evidence. | No unresolved implementation conflict; normal start prerequisites: REL.02, UPD.01, UPD.07. |
| REL.11; WP-50.00 (full); WP-50.08 (full); WP-50.90 (full) | gap | Existing eng/packaging implements prerelease NuGet/native candidate production. eng/packaging/release and eng/release do not exist; bootstrap candidate publication is not production updater signing/cutover or full-family readiness. Scope: Design:docs/assurance/wp50-00-readiness-audit.md, wp50-08-honest-statement.md, wp50-stage-acceptance.md/.json; DesktopPlatform:eng/release/** | Every gate in release-gates.md is evaluated for every surface with a named, resolvable evidence artifact; every still-open gate's blocking consequence is stated; no cross-system failure row in architecture/20-cross-system-lifecycles.md lacks a run test; every public claim is backed by gate evidence, iOS is explicitly stated as outside current scope, and nothing incomplete is presented as complete. Required evidence: Gate-coverage report; claim audit; WP50 stage-acceptance receipt joining REL.02 and REL.04-REL.10. | No unresolved implementation conflict; normal start prerequisites: REL.02, REL.04, REL.05, REL.06, REL.07, REL.08, REL.09, REL.10. |

## Evidence, validation and limits

- Frozen instruction PR #64 was reviewed at `1657b2e505dec55d5fb60f485c2f727d7091a722` and merged as the frozen source. [Main run 36334843593](https://github.com/ArcForges/DesktopPlatform/actions/runs/36334843593) published ten packages at `1.0.0-ci.27.1`. This supports retained build/probe infrastructure only; no missing capability or acceptance is inferred.
- Source evidence: `docs/platform-bootstrap.md`, `docs/native-package-release.md`, `eng/packaging/packages.json`, `eng/policy/reconciliation/source.json`, `DesktopPlatform.slnx`, `src/BuildingBlocks/**/AssemblyPlaceholder.cs`, `src/DesktopHelpers/ArcForges.ContentSandbox/Program.cs`, `native/shared/include/arc/arc_native_abi.h`, `native/arcslate-image-abi/include/arc/arc_slate_image_abi.h`, and the complete frozen Git tree. No claimed current product result is based on an unmerged branch or a historical dated plan.
- Every mapped task is classified once. No task is classified fully inherited, so no inherited completion records are created. Inherited-with-adjustment rows preserve existing work while leaving the named remaining acceptance open.
- Removed-product Media/Colour/Otio/Metal material is retired under ADP-10 and owned by GOV.17/GOV.18. Adoption neither performs nor certifies cleanup; immutable publications and provenance remain preserved.
- Validation performed: source/obligation/receipt consistency review and Plan delivery check. Independent exact-head review and merge are recorded in the PR and claim audit trail. No product build, artifact download, runtime/provider/device/browser/installed-consumer execution or publication recheck.
- P2-017 controls validation venue and cadence. Required future real runtime/hardware/provider acceptance cannot be replaced by compilation or fixtures; unavailable optional local environments are reported honestly, without provisioning. Existing probes are not production substitutes. This ledger opens only the slice tasks subject to prerequisites and any recorded conflicts, not any wider gate or commercial release.
