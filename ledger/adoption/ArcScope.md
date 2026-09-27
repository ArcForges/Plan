# ArcScope adoption facts

Repository owner: w-20260927-arcscope-lane, integration:ArcScope epoch 2. Frozen main a6899eddc4da7cf338d1a1404f1c0c1b8acc546d; Design 722e85641c8afb765dafcab5bc0e84d5a22d5a3c. [Baseline](baseline.md#arcscope) preserves PR17 reviewed head, merge, branch/open-PR snapshot and publication metadata. No open ArcScope PR existed at freeze; retained task/adopt-01 is historical reviewed work.

## Source and publication evidence

- E1: complete tracked src/tests inventory contains the Avalonia host (Program, ArcScopeApp, MainWindow, LiveSmoke), Core (BuildIdentity, CloudHelloClient, HelloViewModel), and seven bootstrap test files. No product domain, acquisition, capture, analysis, measurement, annotations, report, sync, capability or simulator code exists. README and docs/bootstrap-plan.md expressly limit the bootstrap to Hello and do not claim product authentication/workflows.
- E2: eng/ArcForges.Repository contains LicencePolicy, DependencyPolicy, ProvenancePolicy, IdentityEvidence and command tooling. Existing tests independently enforce these baseline concerns, not every GOV.07 policy. tests/ArchitectureTests and eng/policy/exceptions.json are planned additions; consume published GOV.04/GOV.05 engines rather than duplicate them.
- E3: src/ArcForges.ArcScope/ArcForges.ArcScope.csproj enables PublishAot, IsAotCompatible, warning-as-error linker/AOT and reflection-disabled JSON. Program.cs creates a Hello host, not product annotation handlers or Assistant host ports. Exact central pins: Build.Policy 1.0.0-ci.20.1; Contracts.PublicApi 1.0.0-ci.36.1; Avalonia.Desktop/Themes.Fluent 12.1.3; Grpc.Net.Client/Web 2.84.0; Grpc.AspNetCore 2.83.0; Grpc.AspNetCore.Web 2.84.0; Microsoft.Extensions.Hosting 10.0.12; xunit.v3.mtp-v2 4.0.1. Project locks are committed. No sibling-source reference or separate assistant executable. README's Avalonia 12.1.2 statement is stale relative to central 12.1.3; the next relevant dependency/composition documentation update must align it without changing the exact actual pin.
- E4: the sole retained workflow .github/workflows/ci.yml builds/packages win-x64, win-arm64 and linux-x64. Linux alone performs formatting, repository checks and offline tests; TransportTests are excluded from hosted tests. Quality/secret checks, PR dependency review, C#/Actions CodeQL, Verify, portable publication and publication-result check remain. No hosted GUI/live service/macOS job. [Main CI 36335032606](https://github.com/ArcForges/ArcScope/actions/runs/36335032606) at the frozen SHA passed every applicable job (dependency review correctly skipped on main). Original portable publication v0.1.0-ci.37.1 succeeded; receipts/assets are in the baseline. This is a GitHub portable desktop candidate, not NuGet/npm/Maven publication, installer trust, updater acceptance or commercial release. Preserve ArcScope executable/installation identity, AGPL-3.0-only, licences, notices and provenance inventories.
- E5: Design docs/assurance/reference-coverage/arcscope-serial-studio.md is the completed 31-row design-stage matrix bound to Serial-Studio 639daafb, reviewed 2026-09-05. It excludes proprietary Pro expression and permits controlled behavioural reference only, not copying/translation. That accepted matrix stands; SCOPE.10 still owes current changed/new-material and licence re-verification. No reference source or packaged binary was executed or copied for adoption.

## Actual layout binding

Existing projects are src/ArcForges.ArcScope, src/ArcForges.ArcScope.Core, tests/ArcForges.ArcScope.Tests and eng/ArcForges.Repository. Planned src/ArcScope/ArcScope.* modules are new additions, to be bound to the existing ArcForges.ArcScope namespace convention by their claimant. Planned ArcScope.Desktop specialization binds to the existing desktop host; separate domain/application/infrastructure/acquisition/analysis modules are additions rather than renaming Hello code. APP.02's explicitly named ArcForges.ArcScope.Application/Infrastructure projects are new. Planned test paths are new suites. Existing package and executable identities must not be renamed to match logical paths.

Each new project requires an explicit solution entry, licence boundary/provenance inventory entries, centrally admitted exact package pins and regenerated locks after rebase under RES-product-solutions. Number migrations at merge; append format fixture manifests under RES-arcscope-format-fixtures; Design assurance receipt paths remain in Design. The tables below preserve each task's complete planned scope so its claimant can make the final concrete additions within these bindings. No shared root authorizes cross-owner source consumption or a second product writer.

## Combined classifications

Every task is classified exactly once by the linked six slice records. There are no fully inherited tasks. Bootstrap/source evidence is retained without product completion claims. No D-001 conflict or task-independent source blocker was identified; named prerequisites and missing acceptance evidence remain binding. Historical ArcNotes provenance is attribution, not retired product implementation to delete. CON.23/GOV.17/GOV.18 retain their separate cleanup ownership.

| Task | Classification | Record |
|---|---|---|
| PRF.02 | inherited with adjustment | [runtime proofs](../tasks/adopt-05-runtime-proofs.md) |
| APP.02 | gap | [slice](../tasks/adopt-05-app-composition.md) |
| APP.03 | inherited with adjustment | [slice](../tasks/adopt-05-app-composition.md) |
| SCOPE.01 | gap | [slice](../tasks/adopt-05-arcscope.md) |
| SCOPE.02 | gap | [slice](../tasks/adopt-05-arcscope.md) |
| SCOPE.03 | gap | [slice](../tasks/adopt-05-arcscope.md) |
| SCOPE.04 | gap | [slice](../tasks/adopt-05-arcscope.md) |
| SCOPE.05 | gap | [slice](../tasks/adopt-05-arcscope.md) |
| SCOPE.06 | gap | [slice](../tasks/adopt-05-arcscope.md) |
| SCOPE.07 | gap | [slice](../tasks/adopt-05-arcscope.md) |
| SCOPE.08 | gap | [slice](../tasks/adopt-05-arcscope.md) |
| SCOPE.09 | gap | [slice](../tasks/adopt-05-arcscope.md) |
| SCOPE.10 | inherited with adjustment | [slice](../tasks/adopt-05-arcscope.md) |
| SCOPE.11 | gap | [slice](../tasks/adopt-05-arcscope.md) |
| SCOPE.12 | gap | [slice](../tasks/adopt-05-arcscope.md) |
| SCOPE.13 | gap | [slice](../tasks/adopt-05-arcscope.md) |
| SCOPE.14 | gap | [slice](../tasks/adopt-05-arcscope.md) |
| SCOPE.15 | gap | [slice](../tasks/adopt-05-arcscope.md) |
| SCOPE.16 | gap | [slice](../tasks/adopt-05-arcscope.md) |
| SCOPE.17 | gap | [slice](../tasks/adopt-05-arcscope.md) |
| SCOPE.18 | gap | [slice](../tasks/adopt-05-arcscope.md) |
| SCOPE.19 | gap | [slice](../tasks/adopt-05-arcscope.md) |
| SCOPE.20 | gap | [slice](../tasks/adopt-05-arcscope.md) |
| SCOPE.21 | gap | [slice](../tasks/adopt-05-arcscope.md) |
| SCOPE.22 | gap | [slice](../tasks/adopt-05-arcscope.md) |
| SCOPE.23 | gap | [slice](../tasks/adopt-05-arcscope.md) |
| SCOPE.24 | gap | [slice](../tasks/adopt-05-arcscope.md) |
| SCOPE.25 | gap | [slice](../tasks/adopt-05-arcscope.md) |
| SCOPE.26 | gap | [slice](../tasks/adopt-05-arcscope.md) |
| SCOPE.27 | gap | [slice](../tasks/adopt-05-arcscope.md) |
| GOV.07 | inherited with adjustment | [slice](../tasks/adopt-05-governance.md) |
| REL.02 | inherited with adjustment | [slice](../tasks/adopt-05-release.md) |
| SIM.06 | gap | [slice](../tasks/adopt-05-simulator.md) |

## Validation and scope

Reviewed source and original receipts only, plus explicit-root delivery.py consistency check; no build, download, runtime, device, GUI or live-service cycle. The repository adoption closes only when all six slices are complete in the merged ledger. This does not close any product or commercial gate. All 33 task classifications are review results; unselected implementation is not authorized by their being listed here.
