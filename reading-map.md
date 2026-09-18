# ArcForges reading map

Design baseline: `575ba9f929bcb2806e08b9776d9bdb7b0633358a`.

This map is navigation, not exhaustive authority. It combines file citations from **the entire body of every active WP**, including late amendments and .90, with concrete authorities found by searching the current corpus. For a selected substep, read its whole WP, then the applicable definitions and tests in these files. Follow section anchors and rule IDs in the original WP; freshly search incoming references and other relevant files too.

A cited later WP or an early reference to a release gate is context, not an additional dependency. The formal graph and producer stage matrix decide which input must exist now. Dated reviews and bound historical inventories explain earlier findings; use their current formal owners for behavior.

## Common context

Read the execution instructions, accepted decisions and planning entry points. Consult the applicable rows of the invariant, traceability, testing and release-gate authorities; do not treat every future release gate as a prerequisite of the current substep.

- [AGENTS.md](<C:/MyFile/Projects/ArcForges-Design/AGENTS.md>)
- [README.md](<C:/MyFile/Projects/ArcForges-Design/README.md>)
- [docs/decisions/README.md](<C:/MyFile/Projects/ArcForges-Design/docs/decisions/README.md>)
- [docs/decisions/phase-1-foundation-decisions.md](<C:/MyFile/Projects/ArcForges-Design/docs/decisions/phase-1-foundation-decisions.md>)
- [docs/decisions/phase-2-specification-decisions.md](<C:/MyFile/Projects/ArcForges-Design/docs/decisions/phase-2-specification-decisions.md>)
- [docs/planning/README.md](<C:/MyFile/Projects/ArcForges-Design/docs/planning/README.md>)
- [docs/planning/implementation-sequence.md](<C:/MyFile/Projects/ArcForges-Design/docs/planning/implementation-sequence.md>)
- [docs/planning/work-packages/README.md](<C:/MyFile/Projects/ArcForges-Design/docs/planning/work-packages/README.md>)
- [docs/planning/producer-artifacts-and-integration.md](<C:/MyFile/Projects/ArcForges-Design/docs/planning/producer-artifacts-and-integration.md>)
- [docs/requirements/README.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/README.md>)
- [docs/architecture/README.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/README.md>)
- [docs/assurance/invariant-coverage.md](<C:/MyFile/Projects/ArcForges-Design/docs/assurance/invariant-coverage.md>)
- [docs/assurance/traceability-matrix.md](<C:/MyFile/Projects/ArcForges-Design/docs/assurance/traceability-matrix.md>)
- [docs/assurance/testing-and-verification-strategy.md](<C:/MyFile/Projects/ArcForges-Design/docs/assurance/testing-and-verification-strategy.md>)
- [docs/assurance/open-gates-register.md](<C:/MyFile/Projects/ArcForges-Design/docs/assurance/open-gates-register.md>)
- [docs/assurance/release-gates.md](<C:/MyFile/Projects/ArcForges-Design/docs/assurance/release-gates.md>)

## Reference sources and exclusions

All reference roots below exist at preparation time and remain read-only. Start with the completed coverage matrix; inspect the relevant source/commit only for this task or drift. A path in an older matrix may use the former root: resolve the actual repository identity at the path below. Do not infer permission to copy from availability or an AI rewrite.

| Area | Actual root(s) | Coverage authority |
|---|---|---|
| Assistant and Android UX | `C:\MyFile\Projects\AionUi` (including `mobile`) | [AionUi matrix](<C:/MyFile/Projects/ArcForges-Design/docs/assurance/reference-coverage/arcchat-aionui.md>) |
| Notes | `C:\MyFile\Projects\AFFiNE`; `C:\MyFile\Projects\siyuan` | [Notes matrix](<C:/MyFile/Projects/ArcForges-Design/docs/assurance/reference-coverage/arcnotes-affine-siyuan.md>) |
| Scope | `C:\MyFile\Projects\Serial-Studio` | [Scope matrix](<C:/MyFile/Projects/ArcForges-Design/docs/assurance/reference-coverage/arcscope-serial-studio.md>) |
| Slate | `C:\MyFile\Projects\ArcVideo`; `C:\MyFile\Projects\ArcVideoFoundation` | [Slate matrix](<C:/MyFile/Projects/ArcForges-Design/docs/assurance/reference-coverage/arcslate-arcvideo.md>) |
| Distribution shape/notices only | `C:\MyFile\Projects\StartArcForges` | [packaged-output boundary](<C:/MyFile/Projects/ArcForges-Design/docs/assurance/reference-coverage/distribution-startarcforges.md>) |

Observe per-file provenance and excluded/proprietary subtrees. Reference capability does not create product scope. Do not execute, unpack, disassemble or reverse engineer StartArcForges binaries. Deprecated input bodies are excluded; historical citations do not reopen them. The old monorepo is not the current implementation root.

## Current authority catalogue

These are available search surfaces, not a demand to read the whole corpus for every substep. The package-specific maps below narrow the initial reading. Current amendments govern historically named files.

### docs/requirements

- [docs/requirements/00-product-scope-and-portfolio.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/00-product-scope-and-portfolio.md>) — ArcForges Product Scope and Portfolio
- [docs/requirements/01-normative-glossary-and-invariants.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/01-normative-glossary-and-invariants.md>) — ArcForges Normative Glossary and Invariant Catalogue
- [docs/requirements/02-identity-account-and-workspace.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/02-identity-account-and-workspace.md>) — Identity, Account, Device, Session and Workspace Requirements
- [docs/requirements/03-cloud-services-and-sync.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/03-cloud-services-and-sync.md>) — Cloud Services, Sync, Assets and Data Integrity Requirements
- [docs/requirements/04-commerce-entitlement-and-credits.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/04-commerce-entitlement-and-credits.md>) — Commerce, Entitlement and AI Credits Requirements
- [docs/requirements/05-ai-and-agent-execution.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/05-ai-and-agent-execution.md>) — AI, Agent Execution, Tasks and Automation Requirements
- [docs/requirements/06-knowledge-search-and-retrieval.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/06-knowledge-search-and-retrieval.md>) — Knowledge, Search and Retrieval Requirements
- [docs/requirements/07-security-privacy-and-trust.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/07-security-privacy-and-trust.md>) — Security, Permission, Privacy and Trust Requirements
- [docs/requirements/08-extensions-and-developer-platform.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/08-extensions-and-developer-platform.md>) — Extensions, Integrations and Developer Platform Requirements
- [docs/requirements/09-shared-desktop-experience.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/09-shared-desktop-experience.md>) — Shared Desktop Experience Requirements
- [docs/requirements/10-distribution-update-and-support.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/10-distribution-update-and-support.md>) — Distribution, Update, Support and Trust & Safety Requirements
- [docs/requirements/11-policy-and-configuration.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/11-policy-and-configuration.md>) — Dynamic Policy and Configuration Requirements
- [docs/requirements/12-quality-and-compatibility-contract.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/12-quality-and-compatibility-contract.md>) — Product Quality and Compatibility Contract
- [docs/requirements/13-data-formats-and-portability.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/13-data-formats-and-portability.md>) — Working Data, Project Formats and Cloud Portability Requirements
- [docs/requirements/README.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/README.md>) — Requirements
- [docs/requirements/products/README.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/products/README.md>) — Product Requirements
- [docs/requirements/products/arcchat-mobile-and-web.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/products/arcchat-mobile-and-web.md>) — Android companion and Web companion — Product Requirements
- [docs/requirements/products/arcchat.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/products/arcchat.md>) — Application Assistant — Feature Requirements
- [docs/requirements/products/arcforges-cloud.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/products/arcforges-cloud.md>) — ArcForges Cloud — Product and Platform Requirements
- [docs/requirements/products/arcforges-web.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/products/arcforges-web.md>) — ArcForges Web — Product Requirements
- [docs/requirements/products/arcnotes.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/products/arcnotes.md>) — ArcNotes — Product Requirements
- [docs/requirements/products/arcscope.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/products/arcscope.md>) — ArcScope — Product Requirements
- [docs/requirements/products/arcslate.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/products/arcslate.md>) — ArcSlate — Product Requirements

### docs/architecture

- [docs/architecture/00-architecture-overview.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/00-architecture-overview.md>) — ArcForges Architecture Overview
- [docs/architecture/01-solution-and-project-layout.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/01-solution-and-project-layout.md>) — Solution and Project Layout
- [docs/architecture/02-contracts-and-protocols.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/02-contracts-and-protocols.md>) — Contracts, Protocols and Shared Semantics
- [docs/architecture/03-local-ipc-and-process-model.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/03-local-ipc-and-process-model.md>) — Application Process and Private Helper IPC
- [docs/architecture/04-desktop-application-architecture.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/04-desktop-application-architecture.md>) — Desktop Application Architecture
- [docs/architecture/05-cloud-architecture.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/05-cloud-architecture.md>) — ArcForges Cloud Architecture
- [docs/architecture/06-data-persistence-and-formats.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/06-data-persistence-and-formats.md>) — Data Persistence and Formats
- [docs/architecture/07-sync-conflict-and-backup.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/07-sync-conflict-and-backup.md>) — Sync, Conflict and Backup Architecture
- [docs/architecture/08-security-architecture.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/08-security-architecture.md>) — Security Architecture
- [docs/architecture/09-ai-and-agent-runtime-architecture.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/09-ai-and-agent-runtime-architecture.md>) — AI and Agent Runtime Architecture
- [docs/architecture/10-web-architecture.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/10-web-architecture.md>) — Web Architecture
- [docs/architecture/11-mobile-architecture.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/11-mobile-architecture.md>) — Mobile Architecture
- [docs/architecture/12-native-interop-and-media.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/12-native-interop-and-media.md>) — Native Interoperability and Media Architecture
- [docs/architecture/13-observability-and-operations.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/13-observability-and-operations.md>) — Observability and Operations Architecture
- [docs/architecture/14-build-packaging-and-release.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/14-build-packaging-and-release.md>) — Build, Packaging and Release Architecture
- [docs/architecture/15-extension-platform-architecture.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/15-extension-platform-architecture.md>) — Extension Platform Architecture
- [docs/architecture/16-billing-and-commerce-architecture.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/16-billing-and-commerce-architecture.md>) — Billing and Commerce Architecture
- [docs/architecture/17-agent-harness.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/17-agent-harness.md>) — Agent Harness
- [docs/architecture/18-editing-and-rich-content.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/18-editing-and-rich-content.md>) — Editing, Rich Content and Preview
- [docs/architecture/19-product-implementation-maps.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/19-product-implementation-maps.md>) — Product Implementation Maps
- [docs/architecture/20-cross-system-lifecycles.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/20-cross-system-lifecycles.md>) — Cross-System Lifecycles
- [docs/architecture/21-platform-and-dependency-matrix.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/21-platform-and-dependency-matrix.md>) — Platform and Dependency Matrix
- [docs/architecture/22-deployment-and-release-execution.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/22-deployment-and-release-execution.md>) — Deployment and Release Execution
- [docs/architecture/23-simulator-and-interchange.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/23-simulator-and-interchange.md>) — Cloud Simulator, Time Model and OTIO Interchange
- [docs/architecture/24-content-and-extension-isolation.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/24-content-and-extension-isolation.md>) — Content and Extension Isolation
- [docs/architecture/25-web-toolchain-and-sdk.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/25-web-toolchain-and-sdk.md>) — Web Toolchain, Generated SDK and Developer Workflow
- [docs/architecture/26-product-behavior-profiles.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/26-product-behavior-profiles.md>) — Initial Product Behavior Profiles
- [docs/architecture/27-platform-projects-and-application-assistants.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/27-platform-projects-and-application-assistants.md>) — Platform Projects and Application Assistants
- [docs/architecture/README.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/README.md>) — Architecture
- [docs/architecture/contracts/00-operation-catalogue.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/00-operation-catalogue.md>) — Operation Catalogue
- [docs/architecture/contracts/01-public-api-operations.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/01-public-api-operations.md>) — Public API Operations
- [docs/architecture/contracts/02-local-rpc-operations.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/02-local-rpc-operations.md>) — In-Process Product Ports and Private Helper Operations
- [docs/architecture/contracts/03-realtime-and-bridge.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/03-realtime-and-bridge.md>) — Realtime Events and the Durable Bridge
- [docs/architecture/contracts/04-protobuf-wire-registry.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/04-protobuf-wire-registry.md>) — Protobuf Wire Registry and Cross-Language Profile
- [docs/architecture/contracts/05-cloudflare-integration.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/05-cloudflare-integration.md>) — Cloudflare Execution and Object Integration
- [docs/architecture/contracts/06-native-functional-abi.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/06-native-functional-abi.md>) — Initial Functional Native ABI and Managed Packages
- [docs/architecture/contracts/07-client-journeys-and-ports.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/07-client-journeys-and-ports.md>) — Client Journeys, Owner Ports and Recovery
- [docs/architecture/contracts/08-extension-and-policy-profiles.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/08-extension-and-policy-profiles.md>) — Initial Extension and Policy Schemas
- [docs/architecture/contracts/09-local-grpc-and-sandbox.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/09-local-grpc-and-sandbox.md>) — Private Child gRPC and Restricted Helper Profile
- [docs/architecture/contracts/10-application-scope-and-streams.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/10-application-scope-and-streams.md>) — Application Scope, History and Public Streams
- [docs/architecture/contracts/11-operation-scope-manifest.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/11-operation-scope-manifest.md>) — Operation Scope Manifest
- [docs/architecture/data-model/00-data-model-overview.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/data-model/00-data-model-overview.md>) — Data Model Overview
- [docs/architecture/data-model/01-cloud-data-model.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/data-model/01-cloud-data-model.md>) — Cloud Data Model
- [docs/architecture/data-model/02-desktop-data-model.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/data-model/02-desktop-data-model.md>) — Desktop Local Data Model
- [docs/architecture/data-model/03-derived-stores.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/data-model/03-derived-stores.md>) — Derived Stores
- [docs/architecture/data-model/04-d1-execution-profile.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/data-model/04-d1-execution-profile.md>) — D1 Execution, Physical Storage and Recovery Profile
- [docs/architecture/data-model/05-application-history.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/data-model/05-application-history.md>) — Application-Owned Assistant History

### docs/experience

- [docs/experience/01-embedded-assistant.md](<C:/MyFile/Projects/ArcForges-Design/docs/experience/01-embedded-assistant.md>) — Embedded Application Assistant
- [docs/experience/02-android-companion.md](<C:/MyFile/Projects/ArcForges-Design/docs/experience/02-android-companion.md>) — Kotlin Android Companion Experience
- [docs/experience/03-state-and-acceptance.md](<C:/MyFile/Projects/ArcForges-Design/docs/experience/03-state-and-acceptance.md>) — Shared Client States and Acceptance
- [docs/experience/README.md](<C:/MyFile/Projects/ArcForges-Design/docs/experience/README.md>) — Client Experience Specifications

## Work-package reading contexts

<a id="wp-00"></a>
### WP-00 — Specification, Naming and Rights Freeze

Parent: [docs/planning/work-packages/00-specification-naming-and-rights-freeze.md](<C:/MyFile/Projects/ArcForges-Design/docs/planning/work-packages/00-specification-naming-and-rights-freeze.md>). Read the **whole file**, including governing prose outside the selected numbered section.

Direct upstream WPs: none. Within this WP, use source heading order shown in [list.md](list.md#wp-00) and verify earlier substep receipts; preserve the declared stage.

Freeze current authority, names, rights and reusable policy evidence. No future package or Cloud manifest is an input; completed source/reference audits are consumed and checked for drift.

Search leads: Product and naming freeze; Glossary and invariant enforcement data; Licence boundary declaration; Reuse and provenance process; Register the completed reference matrices as versioned planning inputs; Stale-claim reconciliation.

Concrete authorities and verification inputs (in addition to common context):

- [docs/architecture/00-architecture-overview.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/00-architecture-overview.md>) — additional current authority.
- [docs/architecture/01-solution-and-project-layout.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/01-solution-and-project-layout.md>) — WP citation.
- [docs/architecture/27-platform-projects-and-application-assistants.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/27-platform-projects-and-application-assistants.md>) — additional current authority.
- [docs/architecture/contracts/04-protobuf-wire-registry.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/04-protobuf-wire-registry.md>) — WP citation.
- [docs/architecture/contracts/05-cloudflare-integration.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/05-cloudflare-integration.md>) — WP citation.
- [docs/assurance/reference-coverage-and-provenance.md](<C:/MyFile/Projects/ArcForges-Design/docs/assurance/reference-coverage-and-provenance.md>) — WP citation.
- [docs/assurance/reference-coverage/README.md](<C:/MyFile/Projects/ArcForges-Design/docs/assurance/reference-coverage/README.md>) — WP citation.
- [docs/requirements/00-product-scope-and-portfolio.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/00-product-scope-and-portfolio.md>) — WP citation.
- [docs/requirements/01-normative-glossary-and-invariants.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/01-normative-glossary-and-invariants.md>) — WP citation.

Bound inventory / historical evidence; follow current normative owners when amended:

- [docs/assurance/family-design-completion-review.md](<C:/MyFile/Projects/ArcForges-Design/docs/assurance/family-design-completion-review.md>)
- [docs/assurance/implementation-state-reconciliation.md](<C:/MyFile/Projects/ArcForges-Design/docs/assurance/implementation-state-reconciliation.md>)

<a id="wp-01"></a>
### WP-01 — Repository Reconciliation and Target Layout

Parent: [docs/planning/work-packages/01-repository-reconciliation-and-target-layout.md](<C:/MyFile/Projects/ArcForges-Design/docs/planning/work-packages/01-repository-reconciliation-and-target-layout.md>). Read the **whole file**, including governing prose outside the selected numbered section.

Direct upstream WPs: 00. Within this WP, use source heading order shown in [list.md](list.md#wp-01) and verify earlier substep receipts; preserve the declared stage.

Reconcile the nine actual repositories against their current HEADs. The ede43db monorepo inventory is historical disposition evidence, not a target tree to recreate.

Search leads: Verify nine independent current repositories; Implement the frozen contract split; Shared-foundation boundary review; Execute the native surface dispositions; Test suite mapping; Apply bounded repository reconciliation.

Concrete authorities and verification inputs (in addition to common context):

- [docs/architecture/00-architecture-overview.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/00-architecture-overview.md>) — WP citation.
- [docs/architecture/01-solution-and-project-layout.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/01-solution-and-project-layout.md>) — WP citation.
- [docs/architecture/19-product-implementation-maps.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/19-product-implementation-maps.md>) — additional current authority.
- [docs/architecture/21-platform-and-dependency-matrix.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/21-platform-and-dependency-matrix.md>) — additional current authority.
- [docs/architecture/25-web-toolchain-and-sdk.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/25-web-toolchain-and-sdk.md>) — WP citation.
- [docs/architecture/27-platform-projects-and-application-assistants.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/27-platform-projects-and-application-assistants.md>) — additional current authority.
- [docs/architecture/contracts/04-protobuf-wire-registry.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/04-protobuf-wire-registry.md>) — WP citation.
- [docs/architecture/contracts/05-cloudflare-integration.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/05-cloudflare-integration.md>) — WP citation.
- [docs/requirements/11-policy-and-configuration.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/11-policy-and-configuration.md>) — WP citation.

Bound inventory / historical evidence; follow current normative owners when amended:

- [docs/assurance/family-design-completion-review.md](<C:/MyFile/Projects/ArcForges-Design/docs/assurance/family-design-completion-review.md>)
- [docs/assurance/implementation-state-reconciliation.md](<C:/MyFile/Projects/ArcForges-Design/docs/assurance/implementation-state-reconciliation.md>)

<a id="wp-02"></a>
### WP-02 — Build Governance, Packaging Policy and Analyzers

Parent: [docs/planning/work-packages/02-build-governance-and-analyzer-policy.md](<C:/MyFile/Projects/ArcForges-Design/docs/planning/work-packages/02-build-governance-and-analyzer-policy.md>). Read the **whole file**, including governing prose outside the selected numbered section.

Direct upstream WPs: 01. Within this WP, use source heading order shown in [list.md](list.md#wp-02) and verify earlier substep receipts; preserve the declared stage.

Own toolchain/build-policy and candidate pipelines. Preserve independent roots and staged producer availability; full functional native packages are WP13.

Search leads: Pin and lock each toolchain; Diagnostic posture; AOT and trim declaration sweep; Runtime and directory boundaries; Version axis plumbing; Dependency policy.

Concrete authorities and verification inputs (in addition to common context):

- [docs/architecture/01-solution-and-project-layout.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/01-solution-and-project-layout.md>) — WP citation.
- [docs/architecture/11-mobile-architecture.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/11-mobile-architecture.md>) — WP citation.
- [docs/architecture/14-build-packaging-and-release.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/14-build-packaging-and-release.md>) — WP citation.
- [docs/architecture/21-platform-and-dependency-matrix.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/21-platform-and-dependency-matrix.md>) — additional current authority.
- [docs/architecture/22-deployment-and-release-execution.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/22-deployment-and-release-execution.md>) — additional current authority.
- [docs/architecture/25-web-toolchain-and-sdk.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/25-web-toolchain-and-sdk.md>) — WP citation.
- [docs/architecture/contracts/04-protobuf-wire-registry.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/04-protobuf-wire-registry.md>) — WP citation.
- [docs/architecture/contracts/05-cloudflare-integration.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/05-cloudflare-integration.md>) — WP citation.
- [docs/requirements/12-quality-and-compatibility-contract.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/12-quality-and-compatibility-contract.md>) — WP citation.

Bound inventory / historical evidence; follow current normative owners when amended:

- [docs/assurance/family-design-completion-review.md](<C:/MyFile/Projects/ArcForges-Design/docs/assurance/family-design-completion-review.md>)
- [docs/assurance/phase-1-official-verification.md](<C:/MyFile/Projects/ArcForges-Design/docs/assurance/phase-1-official-verification.md>)

<a id="wp-03"></a>
### WP-03 — Proto Contract Foundation and License Split

Parent: [docs/planning/work-packages/03-contract-foundation-and-licence-split.md](<C:/MyFile/Projects/ArcForges-Design/docs/planning/work-packages/03-contract-foundation-and-licence-split.md>). Read the **whole file**, including governing prose outside the selected numbered section.

Direct upstream WPs: 02. Within this WP, use source heading order shown in [list.md](list.md#wp-03) and verify earlier substep receipts; preserve the declared stage.

Produce the complete initial NuGet/npm/Maven contract closure, all concrete operation metadata and independent semantic fixtures. Business handlers belong to later owners; contract completeness cannot be deferred to them.

Search leads: Create the split project structure; Foundation contract types; Serialization posture; Capability and resource contract types; Private helper and in-process contract split; Complete generated package and schema gate; Cross-language compatibility window; Signed catalog and update format producer.

Concrete authorities and verification inputs (in addition to common context):

- [docs/architecture/01-solution-and-project-layout.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/01-solution-and-project-layout.md>) — WP citation.
- [docs/architecture/02-contracts-and-protocols.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/02-contracts-and-protocols.md>) — WP citation.
- [docs/architecture/25-web-toolchain-and-sdk.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/25-web-toolchain-and-sdk.md>) — WP citation.
- [docs/architecture/26-product-behavior-profiles.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/26-product-behavior-profiles.md>) — additional current authority.
- [docs/architecture/27-platform-projects-and-application-assistants.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/27-platform-projects-and-application-assistants.md>) — additional current authority.
- [docs/architecture/contracts/00-operation-catalogue.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/00-operation-catalogue.md>) — additional current authority.
- [docs/architecture/contracts/01-public-api-operations.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/01-public-api-operations.md>) — additional current authority.
- [docs/architecture/contracts/02-local-rpc-operations.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/02-local-rpc-operations.md>) — additional current authority.
- [docs/architecture/contracts/03-realtime-and-bridge.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/03-realtime-and-bridge.md>) — additional current authority.
- [docs/architecture/contracts/04-protobuf-wire-registry.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/04-protobuf-wire-registry.md>) — WP citation.
- [docs/architecture/contracts/05-cloudflare-integration.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/05-cloudflare-integration.md>) — WP citation.
- [docs/architecture/contracts/06-native-functional-abi.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/06-native-functional-abi.md>) — additional current authority.
- [docs/architecture/contracts/07-client-journeys-and-ports.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/07-client-journeys-and-ports.md>) — additional current authority.
- [docs/architecture/contracts/08-extension-and-policy-profiles.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/08-extension-and-policy-profiles.md>) — additional current authority.
- [docs/architecture/contracts/09-local-grpc-and-sandbox.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/09-local-grpc-and-sandbox.md>) — WP citation.
- [docs/architecture/contracts/10-application-scope-and-streams.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/10-application-scope-and-streams.md>) — WP citation.
- [docs/architecture/contracts/11-operation-scope-manifest.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/11-operation-scope-manifest.md>) — WP citation.
- [docs/architecture/data-model/00-data-model-overview.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/data-model/00-data-model-overview.md>) — additional current authority.
- [docs/architecture/data-model/01-cloud-data-model.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/data-model/01-cloud-data-model.md>) — WP citation.
- [docs/architecture/data-model/02-desktop-data-model.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/data-model/02-desktop-data-model.md>) — additional current authority.
- [docs/architecture/data-model/03-derived-stores.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/data-model/03-derived-stores.md>) — additional current authority.
- [docs/architecture/data-model/04-d1-execution-profile.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/data-model/04-d1-execution-profile.md>) — additional current authority.
- [docs/architecture/data-model/05-application-history.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/data-model/05-application-history.md>) — additional current authority.
- [docs/requirements/07-security-privacy-and-trust.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/07-security-privacy-and-trust.md>) — WP citation.
- [docs/requirements/12-quality-and-compatibility-contract.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/12-quality-and-compatibility-contract.md>) — WP citation.
- [docs/requirements/13-data-formats-and-portability.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/13-data-formats-and-portability.md>) — WP citation.
- [docs/requirements/products/arcnotes.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/products/arcnotes.md>) — WP citation.
- [docs/requirements/products/arcscope.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/products/arcscope.md>) — WP citation.
- [docs/requirements/products/arcslate.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/products/arcslate.md>) — additional current authority.

Bound inventory / historical evidence; follow current normative owners when amended:

- [docs/assurance/phase-1-official-verification.md](<C:/MyFile/Projects/ArcForges-Design/docs/assurance/phase-1-official-verification.md>)

<a id="wp-04"></a>
### WP-04 — Identity, Error, Revision and Versioning Primitives

Parent: [docs/planning/work-packages/04-identity-error-and-versioning-primitives.md](<C:/MyFile/Projects/ArcForges-Design/docs/planning/work-packages/04-identity-error-and-versioning-primitives.md>). Read the **whole file**, including governing prose outside the selected numbered section.

Direct upstream WPs: 03. Within this WP, use source heading order shown in [list.md](list.md#wp-04) and verify earlier substep receipts; preserve the declared stage.

Implement exact value/error/version primitives without a future database dependency. Use the current producer registry for Foundation ownership and consumer adapters.

Search leads: Shared identity, error and version primitives; Execution identity and idempotency; Revision and sequence; Time; Error and reason codes; Version axis types.

Concrete authorities and verification inputs (in addition to common context):

- [docs/architecture/01-solution-and-project-layout.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/01-solution-and-project-layout.md>) — WP citation.
- [docs/architecture/02-contracts-and-protocols.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/02-contracts-and-protocols.md>) — WP citation.
- [docs/architecture/09-ai-and-agent-runtime-architecture.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/09-ai-and-agent-runtime-architecture.md>) — WP citation.
- [docs/architecture/13-observability-and-operations.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/13-observability-and-operations.md>) — WP citation.
- [docs/architecture/25-web-toolchain-and-sdk.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/25-web-toolchain-and-sdk.md>) — WP citation.
- [docs/architecture/contracts/00-operation-catalogue.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/00-operation-catalogue.md>) — WP citation.
- [docs/architecture/contracts/04-protobuf-wire-registry.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/04-protobuf-wire-registry.md>) — WP citation.
- [docs/architecture/contracts/05-cloudflare-integration.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/05-cloudflare-integration.md>) — WP citation.
- [docs/architecture/data-model/00-data-model-overview.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/data-model/00-data-model-overview.md>) — additional current authority.
- [docs/requirements/01-normative-glossary-and-invariants.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/01-normative-glossary-and-invariants.md>) — WP citation.
- [docs/requirements/12-quality-and-compatibility-contract.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/12-quality-and-compatibility-contract.md>) — WP citation.

<a id="wp-05"></a>
### WP-05 — Architecture and Repository Policy Test Suite

Parent: [docs/planning/work-packages/05-architecture-and-repository-policy-tests.md](<C:/MyFile/Projects/ArcForges-Design/docs/planning/work-packages/05-architecture-and-repository-policy-tests.md>). Read the **whole file**, including governing prose outside the selected numbered section.

Direct upstream WPs: 02, 03. Within this WP, use source heading order shown in [list.md](list.md#wp-05) and verify earlier substep receipts; preserve the declared stage.

Enforce current architecture and repository policy. A scoped invariant test/accounting contribution does not close every future implementation gate.

Search leads: Layering and reference direction; Licence boundary enforcement; Forbidden terms and naming; Contract and serialization policy; Banned APIs and patterns; Invariant enforcement accounting; Specification integrity.

Concrete authorities and verification inputs (in addition to common context):

- [docs/architecture/00-architecture-overview.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/00-architecture-overview.md>) — WP citation.
- [docs/architecture/01-solution-and-project-layout.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/01-solution-and-project-layout.md>) — WP citation.
- [docs/architecture/02-contracts-and-protocols.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/02-contracts-and-protocols.md>) — additional current authority.
- [docs/architecture/08-security-architecture.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/08-security-architecture.md>) — WP citation.
- [docs/architecture/14-build-packaging-and-release.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/14-build-packaging-and-release.md>) — WP citation.
- [docs/architecture/21-platform-and-dependency-matrix.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/21-platform-and-dependency-matrix.md>) — additional current authority.
- [docs/architecture/25-web-toolchain-and-sdk.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/25-web-toolchain-and-sdk.md>) — WP citation.
- [docs/architecture/27-platform-projects-and-application-assistants.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/27-platform-projects-and-application-assistants.md>) — additional current authority.
- [docs/architecture/contracts/04-protobuf-wire-registry.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/04-protobuf-wire-registry.md>) — WP citation.
- [docs/architecture/contracts/05-cloudflare-integration.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/05-cloudflare-integration.md>) — WP citation.
- [docs/architecture/contracts/11-operation-scope-manifest.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/11-operation-scope-manifest.md>) — additional current authority.

Bound inventory / historical evidence; follow current normative owners when amended:

- [docs/assurance/family-design-completion-review.md](<C:/MyFile/Projects/ArcForges-Design/docs/assurance/family-design-completion-review.md>)
- [docs/assurance/implementation-state-reconciliation.md](<C:/MyFile/Projects/ArcForges-Design/docs/assurance/implementation-state-reconciliation.md>)
- [docs/assurance/phase-1-official-verification.md](<C:/MyFile/Projects/ArcForges-Design/docs/assurance/phase-1-official-verification.md>)

<a id="wp-06"></a>
### WP-06 — AOT, Android, CF and Real Artifact Publish Proof

Parent: [docs/planning/work-packages/06-aot-jit-and-wasm-publish-proof.md](<C:/MyFile/Projects/ArcForges-Design/docs/planning/work-packages/06-aot-jit-and-wasm-publish-proof.md>). Read the **whole file**, including governing prose outside the selected numbered section.

Direct upstream WPs: 03, 04, 05. Within this WP, use source heading order shown in [list.md](list.md#wp-06) and verify earlier substep receipts; preserve the declared stage.

Run actual minimal AOT, browser, Kotlin Android and Cloudflare transport/package proofs. Use the designated isolated probe ports; do not require the future full Harness.

Search leads: Desktop Native AOT package proof; Local RPC under AOT; Generated gRPC-Web under AOT; Realtime under AOT; Cloudflare Native AOT and D1 proof; React production build and generated SDK proof; Third-party control gate; Android gRPC-Web and CF proof.

Concrete authorities and verification inputs (in addition to common context):

- [docs/architecture/01-solution-and-project-layout.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/01-solution-and-project-layout.md>) — WP citation.
- [docs/architecture/03-local-ipc-and-process-model.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/03-local-ipc-and-process-model.md>) — additional current authority.
- [docs/architecture/04-desktop-application-architecture.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/04-desktop-application-architecture.md>) — WP citation.
- [docs/architecture/05-cloud-architecture.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/05-cloud-architecture.md>) — WP citation.
- [docs/architecture/11-mobile-architecture.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/11-mobile-architecture.md>) — additional current authority.
- [docs/architecture/12-native-interop-and-media.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/12-native-interop-and-media.md>) — additional current authority.
- [docs/architecture/14-build-packaging-and-release.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/14-build-packaging-and-release.md>) — WP citation.
- [docs/architecture/21-platform-and-dependency-matrix.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/21-platform-and-dependency-matrix.md>) — additional current authority.
- [docs/architecture/25-web-toolchain-and-sdk.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/25-web-toolchain-and-sdk.md>) — WP citation.
- [docs/architecture/contracts/04-protobuf-wire-registry.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/04-protobuf-wire-registry.md>) — WP citation.
- [docs/architecture/contracts/05-cloudflare-integration.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/05-cloudflare-integration.md>) — WP citation.
- [docs/architecture/contracts/09-local-grpc-and-sandbox.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/09-local-grpc-and-sandbox.md>) — WP citation.
- [docs/architecture/contracts/10-application-scope-and-streams.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/10-application-scope-and-streams.md>) — additional current authority.
- [docs/architecture/data-model/04-d1-execution-profile.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/data-model/04-d1-execution-profile.md>) — additional current authority.
- [docs/experience/03-state-and-acceptance.md](<C:/MyFile/Projects/ArcForges-Design/docs/experience/03-state-and-acceptance.md>) — additional current authority.
- [docs/requirements/12-quality-and-compatibility-contract.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/12-quality-and-compatibility-contract.md>) — WP citation.

Bound inventory / historical evidence; follow current normative owners when amended:

- [docs/assurance/phase-1-official-verification.md](<C:/MyFile/Projects/ArcForges-Design/docs/assurance/phase-1-official-verification.md>)

<a id="wp-07"></a>
### WP-07 — Local Persistence Foundation

Parent: [docs/planning/work-packages/07-local-persistence-foundation.md](<C:/MyFile/Projects/ArcForges-Design/docs/planning/work-packages/07-local-persistence-foundation.md>). Read the **whole file**, including governing prose outside the selected numbered section.

Direct upstream WPs: 04, 06. Within this WP, use source heading order shown in [list.md](list.md#wp-07) and verify earlier substep receipts; preserve the declared stage.

Produce persistence mechanisms with owner fixtures, exact atomicity/recovery and published package evidence. Product-specific schema behavior remains with product owners.

Search leads: Store abstraction and the single write path; Journal; Snapshot and recovery; Migration runner; Managed resource store; Large append store; Derived stores and storage pressure.

Concrete authorities and verification inputs (in addition to common context):

- [docs/architecture/01-solution-and-project-layout.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/01-solution-and-project-layout.md>) — WP citation.
- [docs/architecture/04-desktop-application-architecture.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/04-desktop-application-architecture.md>) — WP citation.
- [docs/architecture/06-data-persistence-and-formats.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/06-data-persistence-and-formats.md>) — WP citation.
- [docs/architecture/07-sync-conflict-and-backup.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/07-sync-conflict-and-backup.md>) — additional current authority.
- [docs/architecture/contracts/04-protobuf-wire-registry.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/04-protobuf-wire-registry.md>) — WP citation.
- [docs/architecture/contracts/05-cloudflare-integration.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/05-cloudflare-integration.md>) — WP citation.
- [docs/architecture/data-model/00-data-model-overview.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/data-model/00-data-model-overview.md>) — additional current authority.
- [docs/architecture/data-model/02-desktop-data-model.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/data-model/02-desktop-data-model.md>) — additional current authority.
- [docs/architecture/data-model/03-derived-stores.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/data-model/03-derived-stores.md>) — additional current authority.
- [docs/architecture/data-model/05-application-history.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/data-model/05-application-history.md>) — additional current authority.
- [docs/requirements/01-normative-glossary-and-invariants.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/01-normative-glossary-and-invariants.md>) — WP citation.
- [docs/requirements/07-security-privacy-and-trust.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/07-security-privacy-and-trust.md>) — WP citation.
- [docs/requirements/10-distribution-update-and-support.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/10-distribution-update-and-support.md>) — WP citation.
- [docs/requirements/12-quality-and-compatibility-contract.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/12-quality-and-compatibility-contract.md>) — WP citation.
- [docs/requirements/13-data-formats-and-portability.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/13-data-formats-and-portability.md>) — WP citation.

<a id="wp-08"></a>
### WP-08 — Private Helper gRPC and Parent Registration

Parent: [docs/planning/work-packages/08-local-ipc-and-registration.md](<C:/MyFile/Projects/ArcForges-Design/docs/planning/work-packages/08-local-ipc-and-registration.md>). Read the **whole file**, including governing prose outside the selected numbered section.

Direct upstream WPs: 06, 07. Within this WP, use source heading order shown in [list.md](list.md#wp-08) and verify earlier substep receipts; preserve the declared stage.

Implement private parent/child helper gRPC only. In-process product ports, independent application sessions and future cross-product collaboration do not create local service listeners.

Search leads: Transport and framing; Parent-owned endpoint identity; Child registration lifecycle; Static routing and version refusal; Bounds and concurrency; Disconnect/cancel/retry; Brokered large data.

Concrete authorities and verification inputs (in addition to common context):

- [docs/architecture/03-local-ipc-and-process-model.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/03-local-ipc-and-process-model.md>) — additional current authority.
- [docs/architecture/24-content-and-extension-isolation.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/24-content-and-extension-isolation.md>) — additional current authority.
- [docs/architecture/27-platform-projects-and-application-assistants.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/27-platform-projects-and-application-assistants.md>) — WP citation.
- [docs/architecture/contracts/02-local-rpc-operations.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/02-local-rpc-operations.md>) — additional current authority.
- [docs/architecture/contracts/04-protobuf-wire-registry.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/04-protobuf-wire-registry.md>) — WP citation.
- [docs/architecture/contracts/09-local-grpc-and-sandbox.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/09-local-grpc-and-sandbox.md>) — additional current authority.
- [docs/architecture/contracts/10-application-scope-and-streams.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/10-application-scope-and-streams.md>) — WP citation.
- [docs/architecture/data-model/02-desktop-data-model.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/data-model/02-desktop-data-model.md>) — additional current authority.
- [docs/architecture/data-model/04-d1-execution-profile.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/data-model/04-d1-execution-profile.md>) — WP citation.
- [docs/architecture/data-model/05-application-history.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/data-model/05-application-history.md>) — WP citation.
- [docs/experience/03-state-and-acceptance.md](<C:/MyFile/Projects/ArcForges-Design/docs/experience/03-state-and-acceptance.md>) — WP citation.
- [docs/experience/README.md](<C:/MyFile/Projects/ArcForges-Design/docs/experience/README.md>) — WP citation.

<a id="wp-09"></a>
### WP-09 — Capability, Contribution and Resource Model

Parent: [docs/planning/work-packages/09-capability-contribution-and-resource-model.md](<C:/MyFile/Projects/ArcForges-Design/docs/planning/work-packages/09-capability-contribution-and-resource-model.md>). Read the **whole file**, including governing prose outside the selected numbered section.

Direct upstream WPs: 03, 08. Within this WP, use source heading order shown in [list.md](list.md#wp-09) and verify earlier substep receipts; preserve the declared stage.

Implement typed in-process contribution/capability/resource mechanisms over the published contracts, with final validation at the owning application.

Search leads: Application identity and in-process composition; Static contribution registration; Capability registry and selection; Actions and availability; Context providers and freezing; Resources and artifacts; Own navigation, hints and health; Invocation pipeline.

Concrete authorities and verification inputs (in addition to common context):

- [docs/architecture/01-solution-and-project-layout.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/01-solution-and-project-layout.md>) — WP citation.
- [docs/architecture/02-contracts-and-protocols.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/02-contracts-and-protocols.md>) — WP citation.
- [docs/architecture/04-desktop-application-architecture.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/04-desktop-application-architecture.md>) — additional current authority.
- [docs/architecture/27-platform-projects-and-application-assistants.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/27-platform-projects-and-application-assistants.md>) — additional current authority.
- [docs/architecture/contracts/00-operation-catalogue.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/00-operation-catalogue.md>) — additional current authority.
- [docs/architecture/contracts/02-local-rpc-operations.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/02-local-rpc-operations.md>) — additional current authority.
- [docs/architecture/contracts/04-protobuf-wire-registry.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/04-protobuf-wire-registry.md>) — WP citation.
- [docs/architecture/contracts/05-cloudflare-integration.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/05-cloudflare-integration.md>) — WP citation.
- [docs/architecture/contracts/08-extension-and-policy-profiles.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/08-extension-and-policy-profiles.md>) — additional current authority.
- [docs/architecture/contracts/09-local-grpc-and-sandbox.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/09-local-grpc-and-sandbox.md>) — WP citation.
- [docs/architecture/contracts/10-application-scope-and-streams.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/10-application-scope-and-streams.md>) — additional current authority.
- [docs/requirements/08-extensions-and-developer-platform.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/08-extensions-and-developer-platform.md>) — WP citation.
- [docs/requirements/09-shared-desktop-experience.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/09-shared-desktop-experience.md>) — WP citation.

<a id="wp-10"></a>
### WP-10 — Design System and Desktop Shell Foundation

Parent: [docs/planning/work-packages/10-design-system-and-desktop-shell.md](<C:/MyFile/Projects/ArcForges-Design/docs/planning/work-packages/10-design-system-and-desktop-shell.md>). Read the **whole file**, including governing prose outside the selected numbered section.

Direct upstream WPs: 06, 09. Within this WP, use source heading order shown in [list.md](list.md#wp-10) and verify earlier substep receipts; preserve the declared stage.

Deliver the reusable desktop shell/design system and applicable UI states. The embedded assistant is a package consumer within each application, not a fourth desktop executable.

Search leads: Token system and theming; Windows, panels and layout; Command system; Scoped settings; Attention and notification model; Error presentation; Lifecycle, menus and shutdown; Accessibility and localisation baseline; Third-party control admission.

Concrete authorities and verification inputs (in addition to common context):

- [docs/architecture/01-solution-and-project-layout.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/01-solution-and-project-layout.md>) — WP citation.
- [docs/architecture/04-desktop-application-architecture.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/04-desktop-application-architecture.md>) — WP citation.
- [docs/architecture/10-web-architecture.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/10-web-architecture.md>) — WP citation.
- [docs/architecture/27-platform-projects-and-application-assistants.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/27-platform-projects-and-application-assistants.md>) — additional current authority.
- [docs/architecture/contracts/04-protobuf-wire-registry.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/04-protobuf-wire-registry.md>) — WP citation.
- [docs/architecture/contracts/05-cloudflare-integration.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/05-cloudflare-integration.md>) — WP citation.
- [docs/experience/01-embedded-assistant.md](<C:/MyFile/Projects/ArcForges-Design/docs/experience/01-embedded-assistant.md>) — additional current authority.
- [docs/experience/03-state-and-acceptance.md](<C:/MyFile/Projects/ArcForges-Design/docs/experience/03-state-and-acceptance.md>) — additional current authority.
- [docs/requirements/09-shared-desktop-experience.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/09-shared-desktop-experience.md>) — WP citation.
- [docs/requirements/12-quality-and-compatibility-contract.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/12-quality-and-compatibility-contract.md>) — WP citation.

Bound inventory / historical evidence; follow current normative owners when amended:

- [docs/assurance/phase-1-official-verification.md](<C:/MyFile/Projects/ArcForges-Design/docs/assurance/phase-1-official-verification.md>)

<a id="wp-11"></a>
### WP-11 — Security Foundation

Parent: [docs/planning/work-packages/11-security-foundation.md](<C:/MyFile/Projects/ArcForges-Design/docs/planning/work-packages/11-security-foundation.md>). Read the **whole file**, including governing prose outside the selected numbered section.

Direct upstream WPs: 04, 08, 09. Within this WP, use source heading order shown in [list.md](list.md#wp-11) and verify earlier substep receipts; preserve the declared stage.

Implement security mechanisms and the real OS-restricted fixture-parser helper. Production parser composition is WP13.13, not a backwards prerequisite.

Search leads: Principals and the actor chain; Risk model and classification; The decision pipeline and enforcement points; Approval, steering and step-up; Per-application secrets and session isolation; Egress control; Instruction provenance; Capability leases and trust; Audit; Content helper and OS-enforced isolation.

Concrete authorities and verification inputs (in addition to common context):

- [docs/architecture/01-solution-and-project-layout.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/01-solution-and-project-layout.md>) — WP citation.
- [docs/architecture/08-security-architecture.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/08-security-architecture.md>) — WP citation.
- [docs/architecture/13-observability-and-operations.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/13-observability-and-operations.md>) — WP citation.
- [docs/architecture/24-content-and-extension-isolation.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/24-content-and-extension-isolation.md>) — WP citation.
- [docs/architecture/contracts/00-operation-catalogue.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/00-operation-catalogue.md>) — additional current authority.
- [docs/architecture/contracts/04-protobuf-wire-registry.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/04-protobuf-wire-registry.md>) — WP citation.
- [docs/architecture/contracts/05-cloudflare-integration.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/05-cloudflare-integration.md>) — WP citation.
- [docs/architecture/contracts/09-local-grpc-and-sandbox.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/09-local-grpc-and-sandbox.md>) — WP citation.
- [docs/architecture/contracts/11-operation-scope-manifest.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/11-operation-scope-manifest.md>) — additional current authority.
- [docs/architecture/data-model/00-data-model-overview.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/data-model/00-data-model-overview.md>) — additional current authority.
- [docs/requirements/01-normative-glossary-and-invariants.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/01-normative-glossary-and-invariants.md>) — WP citation.
- [docs/requirements/07-security-privacy-and-trust.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/07-security-privacy-and-trust.md>) — WP citation.

Bound inventory / historical evidence; follow current normative owners when amended:

- [docs/assurance/phase-1-official-verification.md](<C:/MyFile/Projects/ArcForges-Design/docs/assurance/phase-1-official-verification.md>)

<a id="wp-12"></a>
### WP-12 — Observability Foundation

Parent: [docs/planning/work-packages/12-observability-foundation.md](<C:/MyFile/Projects/ArcForges-Design/docs/planning/work-packages/12-observability-foundation.md>). Read the **whole file**, including governing prose outside the selected numbered section.

Direct upstream WPs: 04, 06. Within this WP, use source heading order shown in [list.md](list.md#wp-12) and verify earlier substep receipts; preserve the declared stage.

Deliver reusable observability and explicit privacy/redaction evidence on this stage's actual hosts; later owner operations remain staged.

Search leads: Emission and dimensions; Correlation and causation; Redaction by construction; Cardinality and sampling; Health probes; Desktop diagnostics and consent.

Concrete authorities and verification inputs (in addition to common context):

- [docs/architecture/01-solution-and-project-layout.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/01-solution-and-project-layout.md>) — WP citation.
- [docs/architecture/13-observability-and-operations.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/13-observability-and-operations.md>) — WP citation.
- [docs/architecture/contracts/04-protobuf-wire-registry.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/04-protobuf-wire-registry.md>) — WP citation.
- [docs/architecture/contracts/05-cloudflare-integration.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/05-cloudflare-integration.md>) — WP citation.
- [docs/experience/03-state-and-acceptance.md](<C:/MyFile/Projects/ArcForges-Design/docs/experience/03-state-and-acceptance.md>) — additional current authority.
- [docs/requirements/01-normative-glossary-and-invariants.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/01-normative-glossary-and-invariants.md>) — WP citation.
- [docs/requirements/07-security-privacy-and-trust.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/07-security-privacy-and-trust.md>) — WP citation.
- [docs/requirements/12-quality-and-compatibility-contract.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/12-quality-and-compatibility-contract.md>) — WP citation.

<a id="wp-13"></a>
### WP-13 — Complete Native Producers and Technical Probes

Parent: [docs/planning/work-packages/13-high-risk-technical-probes.md](<C:/MyFile/Projects/ArcForges-Design/docs/planning/work-packages/13-high-risk-technical-probes.md>). Read the **whole file**, including governing prose outside the selected numbered section.

Direct upstream WPs: 06, 07, 08, 09, 10, 11, 12. Within this WP, use source heading order shown in [list.md](list.md#wp-13) and verify earlier substep receipts; preserve the declared stage.

Complete functional native/helper packages, dependencies and clean C17/C# AOT consumers. 13.05 proves all declarations/common layouts; 13.06–13.14 implement families; 13.15/13.90 verify complete packaged exports. 13.04 seeds inventory; 13.16 completes it.

Search leads: Probe A: device tool execution under Native AOT; Probe B: block editor, store, undo and recovery; Probe C: high-throughput acquisition; Probe D: native decode and synchronisation; Evidence, licence positions and conclusions; Common ABI and deterministic failure surface; Media reader, probe, frame and seek; Convert, resample and media writer; Audio devices; Colour transforms; Still-image codecs; OTIO interchange; Serial and USB instruments; PDF and production parser containment; Portable graphics and optional OS backends; Immutable native package production; Dependency adoption and hardware receipts.

Concrete authorities and verification inputs (in addition to common context):

- [docs/architecture/01-solution-and-project-layout.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/01-solution-and-project-layout.md>) — WP citation.
- [docs/architecture/09-ai-and-agent-runtime-architecture.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/09-ai-and-agent-runtime-architecture.md>) — WP citation.
- [docs/architecture/12-native-interop-and-media.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/12-native-interop-and-media.md>) — WP citation.
- [docs/architecture/17-agent-harness.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/17-agent-harness.md>) — WP citation.
- [docs/architecture/18-editing-and-rich-content.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/18-editing-and-rich-content.md>) — additional current authority.
- [docs/architecture/21-platform-and-dependency-matrix.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/21-platform-and-dependency-matrix.md>) — additional current authority.
- [docs/architecture/23-simulator-and-interchange.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/23-simulator-and-interchange.md>) — additional current authority.
- [docs/architecture/24-content-and-extension-isolation.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/24-content-and-extension-isolation.md>) — additional current authority.
- [docs/architecture/26-product-behavior-profiles.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/26-product-behavior-profiles.md>) — additional current authority.
- [docs/architecture/27-platform-projects-and-application-assistants.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/27-platform-projects-and-application-assistants.md>) — additional current authority.
- [docs/architecture/contracts/02-local-rpc-operations.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/02-local-rpc-operations.md>) — WP citation.
- [docs/architecture/contracts/04-protobuf-wire-registry.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/04-protobuf-wire-registry.md>) — WP citation.
- [docs/architecture/contracts/05-cloudflare-integration.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/05-cloudflare-integration.md>) — WP citation.
- [docs/architecture/contracts/06-native-functional-abi.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/06-native-functional-abi.md>) — WP citation.
- [docs/architecture/contracts/09-local-grpc-and-sandbox.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/09-local-grpc-and-sandbox.md>) — WP citation.
- [docs/assurance/reference-coverage-and-provenance.md](<C:/MyFile/Projects/ArcForges-Design/docs/assurance/reference-coverage-and-provenance.md>) — additional current authority.
- [docs/assurance/reference-coverage/arcscope-serial-studio.md](<C:/MyFile/Projects/ArcForges-Design/docs/assurance/reference-coverage/arcscope-serial-studio.md>) — additional current authority.
- [docs/assurance/reference-coverage/arcslate-arcvideo.md](<C:/MyFile/Projects/ArcForges-Design/docs/assurance/reference-coverage/arcslate-arcvideo.md>) — additional current authority.
- [docs/requirements/12-quality-and-compatibility-contract.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/12-quality-and-compatibility-contract.md>) — WP citation.
- [docs/requirements/products/arcnotes.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/products/arcnotes.md>) — additional current authority.
- [docs/requirements/products/arcscope.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/products/arcscope.md>) — WP citation.
- [docs/requirements/products/arcslate.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/products/arcslate.md>) — additional current authority.

Bound inventory / historical evidence; follow current normative owners when amended:

- [docs/assurance/phase-1-official-verification.md](<C:/MyFile/Projects/ArcForges-Design/docs/assurance/phase-1-official-verification.md>)

<a id="wp-14"></a>
### WP-14 — Independent Application Composition and Typed Host Ports

Parent: [docs/planning/work-packages/14-hub-and-minimal-provider-slice.md](<C:/MyFile/Projects/ArcForges-Design/docs/planning/work-packages/14-hub-and-minimal-provider-slice.md>). Read the **whole file**, including governing prose outside the selected numbered section.

Direct upstream WPs: 08, 09, 10, 11, 13. Within this WP, use source heading order shown in [list.md](list.md#wp-14) and verify earlier substep receipts; preserve the declared stage.

Compose an independent application using typed host ports and package-only mechanisms. Keep minimal ArcNotes owner behavior in ArcNotes.

Search leads: Application scope and host ports; Minimal ArcNotes application services; Package consumer composition; Idempotency and revision; Approval at the owner; Context and artifact integration; Independent lifecycle.

Concrete authorities and verification inputs (in addition to common context):

- [docs/architecture/04-desktop-application-architecture.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/04-desktop-application-architecture.md>) — additional current authority.
- [docs/architecture/19-product-implementation-maps.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/19-product-implementation-maps.md>) — additional current authority.
- [docs/architecture/27-platform-projects-and-application-assistants.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/27-platform-projects-and-application-assistants.md>) — WP citation.
- [docs/architecture/contracts/02-local-rpc-operations.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/02-local-rpc-operations.md>) — additional current authority.
- [docs/architecture/contracts/04-protobuf-wire-registry.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/04-protobuf-wire-registry.md>) — WP citation.
- [docs/architecture/contracts/07-client-journeys-and-ports.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/07-client-journeys-and-ports.md>) — additional current authority.
- [docs/architecture/contracts/10-application-scope-and-streams.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/10-application-scope-and-streams.md>) — WP citation.
- [docs/architecture/data-model/04-d1-execution-profile.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/data-model/04-d1-execution-profile.md>) — WP citation.
- [docs/architecture/data-model/05-application-history.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/data-model/05-application-history.md>) — WP citation.
- [docs/experience/01-embedded-assistant.md](<C:/MyFile/Projects/ArcForges-Design/docs/experience/01-embedded-assistant.md>) — additional current authority.
- [docs/experience/03-state-and-acceptance.md](<C:/MyFile/Projects/ArcForges-Design/docs/experience/03-state-and-acceptance.md>) — WP citation.
- [docs/experience/README.md](<C:/MyFile/Projects/ArcForges-Design/docs/experience/README.md>) — WP citation.
- [docs/requirements/products/arcnotes.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/products/arcnotes.md>) — additional current authority.

<a id="wp-15"></a>
### WP-15 — Application Assistant Conversation, History and Project Packages

Parent: [docs/planning/work-packages/15-arcchat-conversation-core.md](<C:/MyFile/Projects/ArcForges-Design/docs/planning/work-packages/15-arcchat-conversation-core.md>). Read the **whole file**, including governing prose outside the selected numbered section.

Direct upstream WPs: 14. Within this WP, use source heading order shown in [list.md](list.md#wp-15) and verify earlier substep receipts; preserve the declared stage.

Produce isolated per-application assistant history/core packages and exact SQLite/history behavior. Export client fixtures are replaced by actual Cloud owners at WP25.08.

Search leads: Single application history store; Branches and window drafts; Attachments and provenance; Projects and profiles; Skills; Local search; Local history export and import; Reference and package proof.

Concrete authorities and verification inputs (in addition to common context):

- [docs/architecture/27-platform-projects-and-application-assistants.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/27-platform-projects-and-application-assistants.md>) — WP citation.
- [docs/architecture/contracts/04-protobuf-wire-registry.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/04-protobuf-wire-registry.md>) — WP citation.
- [docs/architecture/contracts/07-client-journeys-and-ports.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/07-client-journeys-and-ports.md>) — additional current authority.
- [docs/architecture/contracts/10-application-scope-and-streams.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/10-application-scope-and-streams.md>) — WP citation.
- [docs/architecture/data-model/02-desktop-data-model.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/data-model/02-desktop-data-model.md>) — additional current authority.
- [docs/architecture/data-model/03-derived-stores.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/data-model/03-derived-stores.md>) — additional current authority.
- [docs/architecture/data-model/04-d1-execution-profile.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/data-model/04-d1-execution-profile.md>) — WP citation.
- [docs/architecture/data-model/05-application-history.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/data-model/05-application-history.md>) — WP citation.
- [docs/assurance/reference-coverage/arcchat-aionui.md](<C:/MyFile/Projects/ArcForges-Design/docs/assurance/reference-coverage/arcchat-aionui.md>) — additional current authority.
- [docs/experience/01-embedded-assistant.md](<C:/MyFile/Projects/ArcForges-Design/docs/experience/01-embedded-assistant.md>) — additional current authority.
- [docs/experience/03-state-and-acceptance.md](<C:/MyFile/Projects/ArcForges-Design/docs/experience/03-state-and-acceptance.md>) — WP citation.
- [docs/experience/README.md](<C:/MyFile/Projects/ArcForges-Design/docs/experience/README.md>) — WP citation.
- [docs/requirements/products/arcchat.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/products/arcchat.md>) — additional current authority.

<a id="wp-16"></a>
### WP-16 — Unified Execution Engine

Parent: [docs/planning/work-packages/16-unified-execution-engine.md](<C:/MyFile/Projects/ArcForges-Design/docs/planning/work-packages/16-unified-execution-engine.md>). Read the **whole file**, including governing prose outside the selected numbered section.

Direct upstream WPs: 09, 11, 14. Within this WP, use source heading order shown in [list.md](list.md#wp-16) and verify earlier substep receipts; preserve the declared stage.

Implement the device/product execution chain, command recovery and security. The sole Cloud model/tool loop remains WP52.

Search leads: The execution chain and its persistence; Lifecycle states and reason facets; Failure classification and retry; Child tasks and ownership; Checkpoints and compensation; Approval, steering and budget integration; Progress, outcome and trace; Concurrency, loops and storms.

Concrete authorities and verification inputs (in addition to common context):

- [docs/architecture/01-solution-and-project-layout.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/01-solution-and-project-layout.md>) — WP citation.
- [docs/architecture/09-ai-and-agent-runtime-architecture.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/09-ai-and-agent-runtime-architecture.md>) — WP citation.
- [docs/architecture/17-agent-harness.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/17-agent-harness.md>) — WP citation.
- [docs/architecture/contracts/00-operation-catalogue.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/00-operation-catalogue.md>) — additional current authority.
- [docs/architecture/contracts/02-local-rpc-operations.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/02-local-rpc-operations.md>) — additional current authority.
- [docs/architecture/contracts/03-realtime-and-bridge.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/03-realtime-and-bridge.md>) — additional current authority.
- [docs/architecture/contracts/04-protobuf-wire-registry.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/04-protobuf-wire-registry.md>) — WP citation.
- [docs/architecture/contracts/05-cloudflare-integration.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/05-cloudflare-integration.md>) — WP citation.
- [docs/architecture/contracts/07-client-journeys-and-ports.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/07-client-journeys-and-ports.md>) — additional current authority.
- [docs/architecture/contracts/10-application-scope-and-streams.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/10-application-scope-and-streams.md>) — additional current authority.
- [docs/architecture/data-model/00-data-model-overview.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/data-model/00-data-model-overview.md>) — additional current authority.
- [docs/architecture/data-model/01-cloud-data-model.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/data-model/01-cloud-data-model.md>) — additional current authority.
- [docs/architecture/data-model/02-desktop-data-model.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/data-model/02-desktop-data-model.md>) — additional current authority.
- [docs/experience/03-state-and-acceptance.md](<C:/MyFile/Projects/ArcForges-Design/docs/experience/03-state-and-acceptance.md>) — additional current authority.
- [docs/requirements/01-normative-glossary-and-invariants.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/01-normative-glossary-and-invariants.md>) — WP citation.
- [docs/requirements/05-ai-and-agent-execution.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/05-ai-and-agent-execution.md>) — WP citation.
- [docs/requirements/07-security-privacy-and-trust.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/07-security-privacy-and-trust.md>) — WP citation.
- [docs/requirements/12-quality-and-compatibility-contract.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/12-quality-and-compatibility-contract.md>) — WP citation.
- [docs/requirements/13-data-formats-and-portability.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/13-data-formats-and-portability.md>) — WP citation.

<a id="wp-17"></a>
### WP-17 — Complete Embedded Assistant and Cloud Client Surface

Parent: [docs/planning/work-packages/17-arcchat-independent-core.md](<C:/MyFile/Projects/ArcForges-Design/docs/planning/work-packages/17-arcchat-independent-core.md>). Read the **whole file**, including governing prose outside the selected numbered section.

Direct upstream WPs: 06, 15, 16. Within this WP, use source heading order shown in [list.md](list.md#wp-17) and verify earlier substep receipts; preserve the declared stage.

Complete embedded assistant navigation, interactions and client mechanisms. Explicit future Cloud/automation/AI fixtures are allowed only until their named real producers, including WP52.06.

Search leads: Complete assistant navigation; Cloud client and device runtime; Security and approval surface; Task centre; Automation client; History and AI admission; Preview and host context; Complete package acceptance.

Concrete authorities and verification inputs (in addition to common context):

- [docs/architecture/04-desktop-application-architecture.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/04-desktop-application-architecture.md>) — additional current authority.
- [docs/architecture/09-ai-and-agent-runtime-architecture.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/09-ai-and-agent-runtime-architecture.md>) — additional current authority.
- [docs/architecture/27-platform-projects-and-application-assistants.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/27-platform-projects-and-application-assistants.md>) — WP citation.
- [docs/architecture/contracts/04-protobuf-wire-registry.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/04-protobuf-wire-registry.md>) — WP citation.
- [docs/architecture/contracts/07-client-journeys-and-ports.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/07-client-journeys-and-ports.md>) — additional current authority.
- [docs/architecture/contracts/10-application-scope-and-streams.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/10-application-scope-and-streams.md>) — WP citation.
- [docs/architecture/data-model/04-d1-execution-profile.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/data-model/04-d1-execution-profile.md>) — WP citation.
- [docs/architecture/data-model/05-application-history.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/data-model/05-application-history.md>) — WP citation.
- [docs/assurance/reference-coverage/arcchat-aionui.md](<C:/MyFile/Projects/ArcForges-Design/docs/assurance/reference-coverage/arcchat-aionui.md>) — additional current authority.
- [docs/experience/01-embedded-assistant.md](<C:/MyFile/Projects/ArcForges-Design/docs/experience/01-embedded-assistant.md>) — additional current authority.
- [docs/experience/03-state-and-acceptance.md](<C:/MyFile/Projects/ArcForges-Design/docs/experience/03-state-and-acceptance.md>) — WP citation.
- [docs/experience/README.md](<C:/MyFile/Projects/ArcForges-Design/docs/experience/README.md>) — WP citation.
- [docs/requirements/products/arcchat.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/products/arcchat.md>) — additional current authority.

<a id="wp-18"></a>
### WP-18 — ArcNotes Document Core

Parent: [docs/planning/work-packages/18-arcnotes-document-core.md](<C:/MyFile/Projects/ArcForges-Design/docs/planning/work-packages/18-arcnotes-document-core.md>). Read the **whole file**, including governing prose outside the selected numbered section.

Direct upstream WPs: 07, 10, 14. Within this WP, use source heading order shown in [list.md](list.md#wp-18) and verify earlier substep receipts; preserve the declared stage.

Implement accepted Notes document/editor behavior, stable text/cell identity, IME, undo, containment and recovery; consume the existing reference matrix and original implementation boundaries.

Search leads: Block document model; Editor interaction; Links, backlinks and outline; Properties and tags; Attachments; Undo, history, checkpoint and trash; Recovery and migration; Capability surface; Reference drift check.

Concrete authorities and verification inputs (in addition to common context):

- [docs/architecture/01-solution-and-project-layout.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/01-solution-and-project-layout.md>) — WP citation.
- [docs/architecture/06-data-persistence-and-formats.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/06-data-persistence-and-formats.md>) — additional current authority.
- [docs/architecture/12-native-interop-and-media.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/12-native-interop-and-media.md>) — WP citation.
- [docs/architecture/18-editing-and-rich-content.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/18-editing-and-rich-content.md>) — WP citation.
- [docs/architecture/19-product-implementation-maps.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/19-product-implementation-maps.md>) — additional current authority.
- [docs/architecture/26-product-behavior-profiles.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/26-product-behavior-profiles.md>) — additional current authority.
- [docs/architecture/contracts/02-local-rpc-operations.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/02-local-rpc-operations.md>) — additional current authority.
- [docs/architecture/contracts/04-protobuf-wire-registry.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/04-protobuf-wire-registry.md>) — WP citation.
- [docs/architecture/contracts/05-cloudflare-integration.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/05-cloudflare-integration.md>) — WP citation.
- [docs/architecture/data-model/02-desktop-data-model.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/data-model/02-desktop-data-model.md>) — WP citation.
- [docs/architecture/data-model/04-d1-execution-profile.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/data-model/04-d1-execution-profile.md>) — additional current authority.
- [docs/assurance/reference-coverage-and-provenance.md](<C:/MyFile/Projects/ArcForges-Design/docs/assurance/reference-coverage-and-provenance.md>) — WP citation.
- [docs/assurance/reference-coverage/arcnotes-affine-siyuan.md](<C:/MyFile/Projects/ArcForges-Design/docs/assurance/reference-coverage/arcnotes-affine-siyuan.md>) — WP citation.
- [docs/requirements/00-product-scope-and-portfolio.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/00-product-scope-and-portfolio.md>) — WP citation.
- [docs/requirements/07-security-privacy-and-trust.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/07-security-privacy-and-trust.md>) — WP citation.
- [docs/requirements/12-quality-and-compatibility-contract.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/12-quality-and-compatibility-contract.md>) — WP citation.
- [docs/requirements/13-data-formats-and-portability.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/13-data-formats-and-portability.md>) — WP citation.
- [docs/requirements/products/arcnotes.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/products/arcnotes.md>) — WP citation.

<a id="wp-19"></a>
### WP-19 — ArcNotes Search, Import, Export and Portability

Parent: [docs/planning/work-packages/19-arcnotes-search-and-portability.md](<C:/MyFile/Projects/ArcForges-Design/docs/planning/work-packages/19-arcnotes-search-and-portability.md>). Read the **whole file**, including governing prose outside the selected numbered section.

Direct upstream WPs: 18. Within this WP, use source heading order shown in [list.md](list.md#wp-19) and verify earlier substep receipts; preserve the declared stage.

Implement local Notes search and portability. Distinguish local/client fixture acceptance from actual Cloud export production at WP25.08.

Search leads: Local full-text index; Query, ranking and permission; Citation anchors; Saved views; Non-destructive import; Owner-specific portability; The repository-projection prohibition.

Concrete authorities and verification inputs (in addition to common context):

- [docs/architecture/01-solution-and-project-layout.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/01-solution-and-project-layout.md>) — WP citation.
- [docs/architecture/06-data-persistence-and-formats.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/06-data-persistence-and-formats.md>) — WP citation.
- [docs/architecture/07-sync-conflict-and-backup.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/07-sync-conflict-and-backup.md>) — additional current authority.
- [docs/architecture/18-editing-and-rich-content.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/18-editing-and-rich-content.md>) — additional current authority.
- [docs/architecture/26-product-behavior-profiles.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/26-product-behavior-profiles.md>) — additional current authority.
- [docs/architecture/contracts/02-local-rpc-operations.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/02-local-rpc-operations.md>) — WP citation.
- [docs/architecture/contracts/04-protobuf-wire-registry.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/04-protobuf-wire-registry.md>) — WP citation.
- [docs/architecture/contracts/05-cloudflare-integration.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/05-cloudflare-integration.md>) — WP citation.
- [docs/architecture/contracts/07-client-journeys-and-ports.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/07-client-journeys-and-ports.md>) — additional current authority.
- [docs/architecture/data-model/02-desktop-data-model.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/data-model/02-desktop-data-model.md>) — additional current authority.
- [docs/architecture/data-model/03-derived-stores.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/data-model/03-derived-stores.md>) — additional current authority.
- [docs/assurance/reference-coverage/arcnotes-affine-siyuan.md](<C:/MyFile/Projects/ArcForges-Design/docs/assurance/reference-coverage/arcnotes-affine-siyuan.md>) — additional current authority.
- [docs/requirements/06-knowledge-search-and-retrieval.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/06-knowledge-search-and-retrieval.md>) — WP citation.
- [docs/requirements/07-security-privacy-and-trust.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/07-security-privacy-and-trust.md>) — WP citation.
- [docs/requirements/11-policy-and-configuration.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/11-policy-and-configuration.md>) — WP citation.
- [docs/requirements/12-quality-and-compatibility-contract.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/12-quality-and-compatibility-contract.md>) — WP citation.
- [docs/requirements/13-data-formats-and-portability.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/13-data-formats-and-portability.md>) — WP citation.
- [docs/requirements/products/arcnotes.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/products/arcnotes.md>) — WP citation.

<a id="wp-21"></a>
### WP-21 — Cloudflare Container, D1 Authority and Binding Plans

Parent: [docs/planning/work-packages/21-cloud-host-and-persistence.md](<C:/MyFile/Projects/ArcForges-Design/docs/planning/work-packages/21-cloud-host-and-persistence.md>). Read the **whole file**, including governing prose outside the selected numbered section.

Direct upstream WPs: 03, 05, 12. Within this WP, use source heading order shown in [list.md](list.md#wp-21) and verify earlier substep receipts; preserve the declared stage.

Produce the real Container/Worker/D1 plan bridge, migration, receipts, fenced jobs and selfhost profile. Its integration manifest is progressive; future business owners remain pending.

Search leads: Ingress and host pipeline; Finite durable jobs; Twenty-one module boundaries; D1 migration and exact physical mapping; Receipts/outbox/archive; Shared atomic families and claims; Capacity and Container/D1 integration producer; Failure isolation and readiness; Selfhost.v1 deployment profile.

Concrete authorities and verification inputs (in addition to common context):

- [docs/architecture/05-cloud-architecture.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/05-cloud-architecture.md>) — additional current authority.
- [docs/architecture/22-deployment-and-release-execution.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/22-deployment-and-release-execution.md>) — additional current authority.
- [docs/architecture/27-platform-projects-and-application-assistants.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/27-platform-projects-and-application-assistants.md>) — WP citation.
- [docs/architecture/contracts/04-protobuf-wire-registry.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/04-protobuf-wire-registry.md>) — WP citation.
- [docs/architecture/contracts/05-cloudflare-integration.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/05-cloudflare-integration.md>) — additional current authority.
- [docs/architecture/contracts/10-application-scope-and-streams.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/10-application-scope-and-streams.md>) — WP citation.
- [docs/architecture/data-model/00-data-model-overview.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/data-model/00-data-model-overview.md>) — additional current authority.
- [docs/architecture/data-model/01-cloud-data-model.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/data-model/01-cloud-data-model.md>) — additional current authority.
- [docs/architecture/data-model/04-d1-execution-profile.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/data-model/04-d1-execution-profile.md>) — WP citation.
- [docs/architecture/data-model/05-application-history.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/data-model/05-application-history.md>) — WP citation.
- [docs/experience/03-state-and-acceptance.md](<C:/MyFile/Projects/ArcForges-Design/docs/experience/03-state-and-acceptance.md>) — WP citation.
- [docs/experience/README.md](<C:/MyFile/Projects/ArcForges-Design/docs/experience/README.md>) — WP citation.
- [docs/requirements/03-cloud-services-and-sync.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/03-cloud-services-and-sync.md>) — additional current authority.
- [docs/requirements/products/arcforges-cloud.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/products/arcforges-cloud.md>) — additional current authority.

<a id="wp-22"></a>
### WP-22 — Identity, Workspace, Device and Session

Parent: [docs/planning/work-packages/22-identity-workspace-and-device.md](<C:/MyFile/Projects/ArcForges-Design/docs/planning/work-packages/22-identity-workspace-and-device.md>). Read the **whole file**, including governing prose outside the selected numbered section.

Direct upstream WPs: 11, 21. Within this WP, use source heading order shown in [list.md](list.md#wp-22) and verify earlier substep receipts; preserve the declared stage.

Produce real identity/session/browser-ceremony and mail paths with per-application isolation. Current P2-014 excludes sibling Device SSO. Later portal UI is not an authentication-producer prerequisite.

Search leads: Core identity model; Native and browser authentication with real mail; Device, installation, instance and session; Device trust and remote gating; Step-up and sensitive operations; PAT and actor authorization; Recovery, account states and deletion; Independent native session integration; Browser cookie-session adapter.

Concrete authorities and verification inputs (in addition to common context):

- [docs/architecture/01-solution-and-project-layout.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/01-solution-and-project-layout.md>) — WP citation.
- [docs/architecture/08-security-architecture.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/08-security-architecture.md>) — WP citation.
- [docs/architecture/10-web-architecture.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/10-web-architecture.md>) — additional current authority.
- [docs/architecture/25-web-toolchain-and-sdk.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/25-web-toolchain-and-sdk.md>) — WP citation.
- [docs/architecture/contracts/01-public-api-operations.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/01-public-api-operations.md>) — additional current authority.
- [docs/architecture/contracts/04-protobuf-wire-registry.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/04-protobuf-wire-registry.md>) — WP citation.
- [docs/architecture/contracts/05-cloudflare-integration.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/05-cloudflare-integration.md>) — WP citation.
- [docs/architecture/contracts/07-client-journeys-and-ports.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/07-client-journeys-and-ports.md>) — additional current authority.
- [docs/architecture/contracts/10-application-scope-and-streams.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/10-application-scope-and-streams.md>) — additional current authority.
- [docs/architecture/contracts/11-operation-scope-manifest.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/11-operation-scope-manifest.md>) — additional current authority.
- [docs/architecture/data-model/01-cloud-data-model.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/data-model/01-cloud-data-model.md>) — WP citation.
- [docs/architecture/data-model/04-d1-execution-profile.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/data-model/04-d1-execution-profile.md>) — additional current authority.
- [docs/experience/03-state-and-acceptance.md](<C:/MyFile/Projects/ArcForges-Design/docs/experience/03-state-and-acceptance.md>) — additional current authority.
- [docs/requirements/01-normative-glossary-and-invariants.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/01-normative-glossary-and-invariants.md>) — WP citation.
- [docs/requirements/02-identity-account-and-workspace.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/02-identity-account-and-workspace.md>) — WP citation.
- [docs/requirements/07-security-privacy-and-trust.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/07-security-privacy-and-trust.md>) — additional current authority.

<a id="wp-23"></a>
### WP-23 — Public Proto APIs and Generated Clients

Parent: [docs/planning/work-packages/23-public-api-and-generated-clients.md](<C:/MyFile/Projects/ArcForges-Design/docs/planning/work-packages/23-public-api-and-generated-clients.md>). Read the **whole file**, including governing prose outside the selected numbered section.

Direct upstream WPs: 03, 22. Within this WP, use source heading order shown in [list.md](list.md#wp-23) and verify earlier substep receipts; preserve the declared stage.

Generate/register the complete public contract surface and prove real identity/transport behavior. Future owner fixtures are explicitly replaced at WP25/42/40/51/52; the Android WP06 probe suffices here.

Search leads: Endpoint mapping and validation; Typed protocol and error mapping; Typed queries and revision preconditions; Idempotency and rate limiting; Resource transport and future-owner boundary; Generated C#/TypeScript/Kotlin clients; Compatibility window.

Concrete authorities and verification inputs (in addition to common context):

- [docs/architecture/01-solution-and-project-layout.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/01-solution-and-project-layout.md>) — WP citation.
- [docs/architecture/02-contracts-and-protocols.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/02-contracts-and-protocols.md>) — WP citation.
- [docs/architecture/05-cloud-architecture.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/05-cloud-architecture.md>) — WP citation.
- [docs/architecture/25-web-toolchain-and-sdk.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/25-web-toolchain-and-sdk.md>) — WP citation.
- [docs/architecture/contracts/00-operation-catalogue.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/00-operation-catalogue.md>) — WP citation.
- [docs/architecture/contracts/01-public-api-operations.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/01-public-api-operations.md>) — WP citation.
- [docs/architecture/contracts/03-realtime-and-bridge.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/03-realtime-and-bridge.md>) — additional current authority.
- [docs/architecture/contracts/04-protobuf-wire-registry.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/04-protobuf-wire-registry.md>) — WP citation.
- [docs/architecture/contracts/05-cloudflare-integration.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/05-cloudflare-integration.md>) — WP citation.
- [docs/architecture/contracts/07-client-journeys-and-ports.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/07-client-journeys-and-ports.md>) — additional current authority.
- [docs/architecture/contracts/10-application-scope-and-streams.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/10-application-scope-and-streams.md>) — additional current authority.
- [docs/architecture/contracts/11-operation-scope-manifest.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/11-operation-scope-manifest.md>) — additional current authority.
- [docs/architecture/data-model/01-cloud-data-model.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/data-model/01-cloud-data-model.md>) — WP citation.
- [docs/architecture/data-model/04-d1-execution-profile.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/data-model/04-d1-execution-profile.md>) — additional current authority.
- [docs/experience/03-state-and-acceptance.md](<C:/MyFile/Projects/ArcForges-Design/docs/experience/03-state-and-acceptance.md>) — additional current authority.
- [docs/requirements/12-quality-and-compatibility-contract.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/12-quality-and-compatibility-contract.md>) — WP citation.
- [docs/requirements/products/arcnotes.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/products/arcnotes.md>) — WP citation.

<a id="wp-24"></a>
### WP-24 — gRPC-Web Streams and Durable Event Recovery

Parent: [docs/planning/work-packages/24-realtime-and-reliable-events.md](<C:/MyFile/Projects/ArcForges-Design/docs/planning/work-packages/24-realtime-and-reliable-events.md>). Read the **whole file**, including governing prose outside the selected numbered section.

Direct upstream WPs: 23. Within this WP, use source heading order shown in [list.md](list.md#wp-24) and verify earlier substep receipts; preserve the declared stage.

Produce bounded stream/hint delivery and durable cursor/unary recovery. Hints are not business authority; final Task/Harness content is integrated at WP52.

Search leads: Connection and authentication; Scoped subscription; Cursor and gap handling; Durable unary fallback; Publication and wake; Bounded lifecycle; Reusable consumer adapters.

Concrete authorities and verification inputs (in addition to common context):

- [docs/architecture/05-cloud-architecture.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/05-cloud-architecture.md>) — additional current authority.
- [docs/architecture/27-platform-projects-and-application-assistants.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/27-platform-projects-and-application-assistants.md>) — WP citation.
- [docs/architecture/contracts/03-realtime-and-bridge.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/03-realtime-and-bridge.md>) — additional current authority.
- [docs/architecture/contracts/04-protobuf-wire-registry.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/04-protobuf-wire-registry.md>) — WP citation.
- [docs/architecture/contracts/05-cloudflare-integration.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/05-cloudflare-integration.md>) — additional current authority.
- [docs/architecture/contracts/10-application-scope-and-streams.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/10-application-scope-and-streams.md>) — WP citation.
- [docs/architecture/data-model/01-cloud-data-model.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/data-model/01-cloud-data-model.md>) — additional current authority.
- [docs/architecture/data-model/04-d1-execution-profile.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/data-model/04-d1-execution-profile.md>) — WP citation.
- [docs/architecture/data-model/05-application-history.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/data-model/05-application-history.md>) — WP citation.
- [docs/experience/03-state-and-acceptance.md](<C:/MyFile/Projects/ArcForges-Design/docs/experience/03-state-and-acceptance.md>) — WP citation.
- [docs/experience/README.md](<C:/MyFile/Projects/ArcForges-Design/docs/experience/README.md>) — WP citation.
- [docs/requirements/03-cloud-services-and-sync.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/03-cloud-services-and-sync.md>) — additional current authority.

<a id="wp-25"></a>
### WP-25 — Sync Engine and Blob Lifecycle

Parent: [docs/planning/work-packages/25-sync-engine-and-blob-lifecycle.md](<C:/MyFile/Projects/ArcForges-Design/docs/planning/work-packages/25-sync-engine-and-blob-lifecycle.md>). Read the **whole file**, including governing prose outside the selected numbered section.

Direct upstream WPs: 19, 24. Within this WP, use source heading order shown in [list.md](list.md#wp-25) and verify earlier substep receipts; preserve the declared stage.

Complete actual R2 lifecycle and Cloud Notes/Chat authority, history import/export, sync and conflicts. Client fixtures from WP15/19 are replaced here.

Search leads: Cloud Notes authority and sync scopes; Pending batches and conflict lineage; Guarded publication and convergent bootstrap; Conflict detection and policies; Deletion and tombstones; Blob lifecycle; Availability, protection and data health; Multi-device convergence; Real Cloud Notes and Chat export producers; Application Cloud history and restartable import.

Concrete authorities and verification inputs (in addition to common context):

- [docs/architecture/01-solution-and-project-layout.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/01-solution-and-project-layout.md>) — WP citation.
- [docs/architecture/06-data-persistence-and-formats.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/06-data-persistence-and-formats.md>) — additional current authority.
- [docs/architecture/07-sync-conflict-and-backup.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/07-sync-conflict-and-backup.md>) — WP citation.
- [docs/architecture/20-cross-system-lifecycles.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/20-cross-system-lifecycles.md>) — additional current authority.
- [docs/architecture/contracts/01-public-api-operations.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/01-public-api-operations.md>) — additional current authority.
- [docs/architecture/contracts/04-protobuf-wire-registry.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/04-protobuf-wire-registry.md>) — WP citation.
- [docs/architecture/contracts/05-cloudflare-integration.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/05-cloudflare-integration.md>) — WP citation.
- [docs/architecture/contracts/07-client-journeys-and-ports.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/07-client-journeys-and-ports.md>) — additional current authority.
- [docs/architecture/contracts/10-application-scope-and-streams.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/10-application-scope-and-streams.md>) — additional current authority.
- [docs/architecture/data-model/00-data-model-overview.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/data-model/00-data-model-overview.md>) — additional current authority.
- [docs/architecture/data-model/01-cloud-data-model.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/data-model/01-cloud-data-model.md>) — WP citation.
- [docs/architecture/data-model/02-desktop-data-model.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/data-model/02-desktop-data-model.md>) — additional current authority.
- [docs/architecture/data-model/04-d1-execution-profile.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/data-model/04-d1-execution-profile.md>) — additional current authority.
- [docs/architecture/data-model/05-application-history.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/data-model/05-application-history.md>) — additional current authority.
- [docs/experience/03-state-and-acceptance.md](<C:/MyFile/Projects/ArcForges-Design/docs/experience/03-state-and-acceptance.md>) — additional current authority.
- [docs/requirements/01-normative-glossary-and-invariants.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/01-normative-glossary-and-invariants.md>) — WP citation.
- [docs/requirements/03-cloud-services-and-sync.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/03-cloud-services-and-sync.md>) — WP citation.
- [docs/requirements/07-security-privacy-and-trust.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/07-security-privacy-and-trust.md>) — WP citation.
- [docs/requirements/13-data-formats-and-portability.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/13-data-formats-and-portability.md>) — WP citation.
- [docs/requirements/products/arcnotes.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/products/arcnotes.md>) — WP citation.

<a id="wp-26"></a>
### WP-26 — Application Presence and One-Application Tool Bridge

Parent: [docs/planning/work-packages/26-remote-action-and-tool-bridge.md](<C:/MyFile/Projects/ArcForges-Design/docs/planning/work-packages/26-remote-action-and-tool-bridge.md>). Read the **whole file**, including governing prose outside the selected numbered section.

Direct upstream WPs: 17, 24, 25. Within this WP, use source heading order shown in [list.md](list.md#wp-26) and verify earlier substep receipts; preserve the declared stage.

Implement presence and a durable one-application device bridge with owner reauthorization, deduplication and unknown-effect reconciliation; real model-driven orchestration closes at WP52.

Search leads: Application presence; Durable target queue; Owner reauthorization; Execution and exact result deduplication; Remote approval and steering; Offline expiry and recovery; Frozen application locality.

Concrete authorities and verification inputs (in addition to common context):

- [docs/architecture/09-ai-and-agent-runtime-architecture.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/09-ai-and-agent-runtime-architecture.md>) — additional current authority.
- [docs/architecture/27-platform-projects-and-application-assistants.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/27-platform-projects-and-application-assistants.md>) — WP citation.
- [docs/architecture/contracts/02-local-rpc-operations.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/02-local-rpc-operations.md>) — additional current authority.
- [docs/architecture/contracts/03-realtime-and-bridge.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/03-realtime-and-bridge.md>) — additional current authority.
- [docs/architecture/contracts/04-protobuf-wire-registry.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/04-protobuf-wire-registry.md>) — WP citation.
- [docs/architecture/contracts/07-client-journeys-and-ports.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/07-client-journeys-and-ports.md>) — additional current authority.
- [docs/architecture/contracts/10-application-scope-and-streams.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/10-application-scope-and-streams.md>) — WP citation.
- [docs/architecture/contracts/11-operation-scope-manifest.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/11-operation-scope-manifest.md>) — additional current authority.
- [docs/architecture/data-model/01-cloud-data-model.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/data-model/01-cloud-data-model.md>) — additional current authority.
- [docs/architecture/data-model/02-desktop-data-model.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/data-model/02-desktop-data-model.md>) — additional current authority.
- [docs/architecture/data-model/04-d1-execution-profile.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/data-model/04-d1-execution-profile.md>) — WP citation.
- [docs/architecture/data-model/05-application-history.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/data-model/05-application-history.md>) — WP citation.
- [docs/experience/03-state-and-acceptance.md](<C:/MyFile/Projects/ArcForges-Design/docs/experience/03-state-and-acceptance.md>) — WP citation.
- [docs/experience/README.md](<C:/MyFile/Projects/ArcForges-Design/docs/experience/README.md>) — WP citation.
- [docs/requirements/05-ai-and-agent-execution.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/05-ai-and-agent-execution.md>) — additional current authority.

<a id="wp-28"></a>
### WP-28 — ArcNotes Bounded Properties and Saved Views

Parent: [docs/planning/work-packages/28-arcnotes-properties-and-views.md](<C:/MyFile/Projects/ArcForges-Design/docs/planning/work-packages/28-arcnotes-properties-and-views.md>). Read the **whole file**, including governing prose outside the selected numbered section.

Direct upstream WPs: 19, 25. Within this WP, use source heading order shown in [list.md](list.md#wp-28) and verify earlier substep receipts; preserve the declared stage.

Complete Notes typed properties, scalar queries and views using real Cloud owner behavior, preserving existing light scope and import/export fidelity.

Search leads: Typed property schemas; Query model; View kinds; Editing through a view; Lightness preservation; Supported-schema migration and export fidelity; Scale.

Concrete authorities and verification inputs (in addition to common context):

- [docs/architecture/01-solution-and-project-layout.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/01-solution-and-project-layout.md>) — WP citation.
- [docs/architecture/18-editing-and-rich-content.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/18-editing-and-rich-content.md>) — additional current authority.
- [docs/architecture/26-product-behavior-profiles.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/26-product-behavior-profiles.md>) — additional current authority.
- [docs/architecture/contracts/02-local-rpc-operations.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/02-local-rpc-operations.md>) — WP citation.
- [docs/architecture/contracts/04-protobuf-wire-registry.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/04-protobuf-wire-registry.md>) — WP citation.
- [docs/architecture/contracts/05-cloudflare-integration.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/05-cloudflare-integration.md>) — WP citation.
- [docs/architecture/contracts/07-client-journeys-and-ports.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/07-client-journeys-and-ports.md>) — additional current authority.
- [docs/architecture/data-model/01-cloud-data-model.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/data-model/01-cloud-data-model.md>) — additional current authority.
- [docs/architecture/data-model/02-desktop-data-model.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/data-model/02-desktop-data-model.md>) — WP citation.
- [docs/architecture/data-model/03-derived-stores.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/data-model/03-derived-stores.md>) — additional current authority.
- [docs/architecture/data-model/04-d1-execution-profile.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/data-model/04-d1-execution-profile.md>) — additional current authority.
- [docs/assurance/reference-coverage/arcnotes-affine-siyuan.md](<C:/MyFile/Projects/ArcForges-Design/docs/assurance/reference-coverage/arcnotes-affine-siyuan.md>) — additional current authority.
- [docs/requirements/13-data-formats-and-portability.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/13-data-formats-and-portability.md>) — additional current authority.
- [docs/requirements/products/arcnotes.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/products/arcnotes.md>) — WP citation.

<a id="wp-30"></a>
### WP-30 — Kotlin Android Foundation

Parent: [docs/planning/work-packages/30-mobile-shared-architecture.md](<C:/MyFile/Projects/ArcForges-Design/docs/planning/work-packages/30-mobile-shared-architecture.md>). Read the **whole file**, including governing prose outside the selected numbered section.

Direct upstream WPs: 03, 06, 23, 24, 25. Within this WP, use source heading order shown in [list.md](list.md#wp-30) and verify earlier substep receipts; preserve the declared stage.

Produce Kotlin Android foundation, Room/security/OS adapters and package-only Maven clients against actual WP23–25. Task/AI fixtures are temporary until WP31/WP52.

Search leads: Android repository identity and toolchain; Native module and route boundaries; Android runtime and OS adapters; Published gRPC-Web contracts; Room history, drafts and receipts; Secure lifecycle and permissions.

Concrete authorities and verification inputs (in addition to common context):

- [docs/architecture/11-mobile-architecture.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/11-mobile-architecture.md>) — WP citation.
- [docs/architecture/contracts/04-protobuf-wire-registry.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/04-protobuf-wire-registry.md>) — WP citation.
- [docs/architecture/contracts/07-client-journeys-and-ports.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/07-client-journeys-and-ports.md>) — WP citation.
- [docs/architecture/contracts/10-application-scope-and-streams.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/10-application-scope-and-streams.md>) — additional current authority.
- [docs/architecture/data-model/05-application-history.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/data-model/05-application-history.md>) — additional current authority.
- [docs/assurance/reference-coverage/arcchat-aionui.md](<C:/MyFile/Projects/ArcForges-Design/docs/assurance/reference-coverage/arcchat-aionui.md>) — additional current authority.
- [docs/experience/02-android-companion.md](<C:/MyFile/Projects/ArcForges-Design/docs/experience/02-android-companion.md>) — additional current authority.
- [docs/experience/03-state-and-acceptance.md](<C:/MyFile/Projects/ArcForges-Design/docs/experience/03-state-and-acceptance.md>) — additional current authority.
- [docs/requirements/products/arcchat-mobile-and-web.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/products/arcchat-mobile-and-web.md>) — WP citation.

<a id="wp-33"></a>
### WP-33 — ArcScope Acquisition and Session Core

Parent: [docs/planning/work-packages/33-arcscope-acquisition-and-session.md](<C:/MyFile/Projects/ArcForges-Design/docs/planning/work-packages/33-arcscope-acquisition-and-session.md>). Read the **whole file**, including governing prose outside the selected numbered section.

Direct upstream WPs: 07, 10, 13, 26. Within this WP, use source heading order shown in [list.md](list.md#wp-33) and verify earlier substep receipts; preserve the declared stage.

Implement real acquisition sources and durable capture/replay with source/framing/time/loss profiles. Synthetic data cannot close required hardware evidence.

Search leads: Sources, adapters and profiles; Acquisition pipeline; Session, capture, segments and gaps; Time and channel model; Durable capture and immutability; Replay; Long-running capture in the shell; Reference drift check.

Concrete authorities and verification inputs (in addition to common context):

- [docs/architecture/01-solution-and-project-layout.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/01-solution-and-project-layout.md>) — WP citation.
- [docs/architecture/12-native-interop-and-media.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/12-native-interop-and-media.md>) — WP citation.
- [docs/architecture/19-product-implementation-maps.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/19-product-implementation-maps.md>) — WP citation.
- [docs/architecture/21-platform-and-dependency-matrix.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/21-platform-and-dependency-matrix.md>) — additional current authority.
- [docs/architecture/23-simulator-and-interchange.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/23-simulator-and-interchange.md>) — additional current authority.
- [docs/architecture/26-product-behavior-profiles.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/26-product-behavior-profiles.md>) — additional current authority.
- [docs/architecture/contracts/02-local-rpc-operations.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/02-local-rpc-operations.md>) — additional current authority.
- [docs/architecture/contracts/04-protobuf-wire-registry.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/04-protobuf-wire-registry.md>) — WP citation.
- [docs/architecture/contracts/05-cloudflare-integration.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/05-cloudflare-integration.md>) — WP citation.
- [docs/architecture/contracts/06-native-functional-abi.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/06-native-functional-abi.md>) — additional current authority.
- [docs/architecture/data-model/02-desktop-data-model.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/data-model/02-desktop-data-model.md>) — additional current authority.
- [docs/assurance/reference-coverage-and-provenance.md](<C:/MyFile/Projects/ArcForges-Design/docs/assurance/reference-coverage-and-provenance.md>) — WP citation.
- [docs/assurance/reference-coverage/arcscope-serial-studio.md](<C:/MyFile/Projects/ArcForges-Design/docs/assurance/reference-coverage/arcscope-serial-studio.md>) — WP citation.
- [docs/requirements/01-normative-glossary-and-invariants.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/01-normative-glossary-and-invariants.md>) — WP citation.
- [docs/requirements/products/arcscope.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/products/arcscope.md>) — WP citation.

<a id="wp-34"></a>
### WP-34 — ArcScope Visualisation, Analysis and Reporting

Parent: [docs/planning/work-packages/34-arcscope-analysis-and-reporting.md](<C:/MyFile/Projects/ArcForges-Design/docs/planning/work-packages/34-arcscope-analysis-and-reporting.md>). Read the **whole file**, including governing prose outside the selected numbered section.

Direct upstream WPs: 33. Within this WP, use source heading order shown in [list.md](list.md#wp-34) and verify earlier substep receipts; preserve the declared stage.

Implement Scope measurements, analyses, decoders, triggers and reports with independent numeric/gap vectors from the product behavior profiles.

Search leads: Visualisation; Triggers; Measurements; Decoders; Analysis and recipes; Annotations, findings and comparison; Reports and reproducibility.

Concrete authorities and verification inputs (in addition to common context):

- [docs/architecture/01-solution-and-project-layout.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/01-solution-and-project-layout.md>) — WP citation.
- [docs/architecture/19-product-implementation-maps.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/19-product-implementation-maps.md>) — additional current authority.
- [docs/architecture/26-product-behavior-profiles.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/26-product-behavior-profiles.md>) — additional current authority.
- [docs/architecture/contracts/02-local-rpc-operations.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/02-local-rpc-operations.md>) — additional current authority.
- [docs/architecture/contracts/04-protobuf-wire-registry.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/04-protobuf-wire-registry.md>) — WP citation.
- [docs/architecture/contracts/05-cloudflare-integration.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/05-cloudflare-integration.md>) — WP citation.
- [docs/architecture/data-model/02-desktop-data-model.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/data-model/02-desktop-data-model.md>) — WP citation.
- [docs/architecture/data-model/03-derived-stores.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/data-model/03-derived-stores.md>) — additional current authority.
- [docs/assurance/reference-coverage/arcscope-serial-studio.md](<C:/MyFile/Projects/ArcForges-Design/docs/assurance/reference-coverage/arcscope-serial-studio.md>) — additional current authority.
- [docs/requirements/07-security-privacy-and-trust.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/07-security-privacy-and-trust.md>) — WP citation.
- [docs/requirements/12-quality-and-compatibility-contract.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/12-quality-and-compatibility-contract.md>) — WP citation.
- [docs/requirements/13-data-formats-and-portability.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/13-data-formats-and-portability.md>) — WP citation.
- [docs/requirements/products/arcscope.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/products/arcscope.md>) — WP citation.

<a id="wp-35"></a>
### WP-35 — ArcScope Integration and Metadata Sync

Parent: [docs/planning/work-packages/35-arcscope-integration-and-sync.md](<C:/MyFile/Projects/ArcForges-Design/docs/planning/work-packages/35-arcscope-integration-and-sync.md>). Read the **whole file**, including governing prose outside the selected numbered section.

Direct upstream WPs: 25, 34. Within this WP, use source heading order shown in [list.md](list.md#wp-35) and verify earlier substep receipts; preserve the declared stage.

Complete Scope capability/context, metadata sync and portability. Raw capture upload stays explicit and bounded; real Cloud simulator integration is WP51.

Search leads: Capability surface; Bounded context provision; Cloud sync scope; Explicit raw upload; Import, export and fixtures; Extension boundary.

Concrete authorities and verification inputs (in addition to common context):

- [docs/architecture/01-solution-and-project-layout.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/01-solution-and-project-layout.md>) — WP citation.
- [docs/architecture/07-sync-conflict-and-backup.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/07-sync-conflict-and-backup.md>) — additional current authority.
- [docs/architecture/23-simulator-and-interchange.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/23-simulator-and-interchange.md>) — additional current authority.
- [docs/architecture/26-product-behavior-profiles.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/26-product-behavior-profiles.md>) — additional current authority.
- [docs/architecture/contracts/02-local-rpc-operations.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/02-local-rpc-operations.md>) — additional current authority.
- [docs/architecture/contracts/04-protobuf-wire-registry.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/04-protobuf-wire-registry.md>) — WP citation.
- [docs/architecture/contracts/05-cloudflare-integration.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/05-cloudflare-integration.md>) — WP citation.
- [docs/architecture/contracts/06-native-functional-abi.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/06-native-functional-abi.md>) — additional current authority.
- [docs/architecture/data-model/02-desktop-data-model.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/data-model/02-desktop-data-model.md>) — additional current authority.
- [docs/architecture/data-model/04-d1-execution-profile.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/data-model/04-d1-execution-profile.md>) — additional current authority.
- [docs/assurance/reference-coverage/arcscope-serial-studio.md](<C:/MyFile/Projects/ArcForges-Design/docs/assurance/reference-coverage/arcscope-serial-studio.md>) — additional current authority.
- [docs/requirements/01-normative-glossary-and-invariants.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/01-normative-glossary-and-invariants.md>) — WP citation.
- [docs/requirements/07-security-privacy-and-trust.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/07-security-privacy-and-trust.md>) — WP citation.
- [docs/requirements/13-data-formats-and-portability.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/13-data-formats-and-portability.md>) — WP citation.
- [docs/requirements/products/arcscope.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/products/arcscope.md>) — WP citation.

<a id="wp-36"></a>
### WP-36 — ArcSlate Project, Timeline and Media Model

Parent: [docs/planning/work-packages/36-arcslate-project-and-timeline.md](<C:/MyFile/Projects/ArcForges-Design/docs/planning/work-packages/36-arcslate-project-and-timeline.md>). Read the **whole file**, including governing prose outside the selected numbered section.

Direct upstream WPs: 07, 10, 13, 26. Within this WP, use source heading order shown in [list.md](list.md#wp-36) and verify earlier substep receipts; preserve the declared stage.

Implement Slate project/timeline/editing with exact time and recovery semantics, before playback/render consumers.

Search leads: Project and sequence model; The exact time model; Media assets and availability; Media library; Timeline and tracks; Editing operations; Undo, checkpoints and recovery; Reference drift check.

Concrete authorities and verification inputs (in addition to common context):

- [docs/architecture/01-solution-and-project-layout.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/01-solution-and-project-layout.md>) — WP citation.
- [docs/architecture/06-data-persistence-and-formats.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/06-data-persistence-and-formats.md>) — additional current authority.
- [docs/architecture/12-native-interop-and-media.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/12-native-interop-and-media.md>) — WP citation.
- [docs/architecture/19-product-implementation-maps.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/19-product-implementation-maps.md>) — additional current authority.
- [docs/architecture/23-simulator-and-interchange.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/23-simulator-and-interchange.md>) — WP citation.
- [docs/architecture/26-product-behavior-profiles.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/26-product-behavior-profiles.md>) — additional current authority.
- [docs/architecture/contracts/02-local-rpc-operations.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/02-local-rpc-operations.md>) — additional current authority.
- [docs/architecture/contracts/04-protobuf-wire-registry.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/04-protobuf-wire-registry.md>) — WP citation.
- [docs/architecture/contracts/05-cloudflare-integration.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/05-cloudflare-integration.md>) — WP citation.
- [docs/architecture/contracts/06-native-functional-abi.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/06-native-functional-abi.md>) — additional current authority.
- [docs/architecture/data-model/02-desktop-data-model.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/data-model/02-desktop-data-model.md>) — additional current authority.
- [docs/assurance/reference-coverage-and-provenance.md](<C:/MyFile/Projects/ArcForges-Design/docs/assurance/reference-coverage-and-provenance.md>) — WP citation.
- [docs/assurance/reference-coverage/arcslate-arcvideo.md](<C:/MyFile/Projects/ArcForges-Design/docs/assurance/reference-coverage/arcslate-arcvideo.md>) — WP citation.
- [docs/requirements/01-normative-glossary-and-invariants.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/01-normative-glossary-and-invariants.md>) — WP citation.
- [docs/requirements/07-security-privacy-and-trust.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/07-security-privacy-and-trust.md>) — WP citation.
- [docs/requirements/13-data-formats-and-portability.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/13-data-formats-and-portability.md>) — WP citation.
- [docs/requirements/products/arcslate.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/products/arcslate.md>) — WP citation.

<a id="wp-37"></a>
### WP-37 — ArcSlate Playback and Processing Runtime

Parent: [docs/planning/work-packages/37-arcslate-playback-and-processing.md](<C:/MyFile/Projects/ArcForges-Design/docs/planning/work-packages/37-arcslate-playback-and-processing.md>). Read the **whole file**, including governing prose outside the selected numbered section.

Direct upstream WPs: 36. Within this WP, use source heading order shown in [list.md](list.md#wp-37) and verify earlier substep receipts; preserve the declared stage.

Implement real native decode/playback, clocks, retime/effect/audio graphs and contained parsing; honor portable paths and optional backend distinctions.

Search leads: Native media boundary; Decode and buffers; Playback engine and clock; Processing graph; Audio; Proxies and caches; Viewer.

Concrete authorities and verification inputs (in addition to common context):

- [docs/architecture/01-solution-and-project-layout.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/01-solution-and-project-layout.md>) — WP citation.
- [docs/architecture/12-native-interop-and-media.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/12-native-interop-and-media.md>) — WP citation.
- [docs/architecture/21-platform-and-dependency-matrix.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/21-platform-and-dependency-matrix.md>) — additional current authority.
- [docs/architecture/24-content-and-extension-isolation.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/24-content-and-extension-isolation.md>) — additional current authority.
- [docs/architecture/26-product-behavior-profiles.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/26-product-behavior-profiles.md>) — additional current authority.
- [docs/architecture/contracts/04-protobuf-wire-registry.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/04-protobuf-wire-registry.md>) — WP citation.
- [docs/architecture/contracts/05-cloudflare-integration.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/05-cloudflare-integration.md>) — WP citation.
- [docs/architecture/contracts/06-native-functional-abi.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/06-native-functional-abi.md>) — additional current authority.
- [docs/architecture/contracts/09-local-grpc-and-sandbox.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/09-local-grpc-and-sandbox.md>) — additional current authority.
- [docs/architecture/data-model/02-desktop-data-model.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/data-model/02-desktop-data-model.md>) — additional current authority.
- [docs/architecture/data-model/03-derived-stores.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/data-model/03-derived-stores.md>) — additional current authority.
- [docs/assurance/reference-coverage/arcslate-arcvideo.md](<C:/MyFile/Projects/ArcForges-Design/docs/assurance/reference-coverage/arcslate-arcvideo.md>) — additional current authority.
- [docs/requirements/01-normative-glossary-and-invariants.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/01-normative-glossary-and-invariants.md>) — WP citation.
- [docs/requirements/products/arcslate.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/products/arcslate.md>) — WP citation.

<a id="wp-38"></a>
### WP-38 — ArcSlate Render, Export and Colour Management

Parent: [docs/planning/work-packages/38-arcslate-render-and-colour.md](<C:/MyFile/Projects/ArcForges-Design/docs/planning/work-packages/38-arcslate-render-and-colour.md>). Read the **whole file**, including governing prose outside the selected numbered section.

Direct upstream WPs: 37. Within this WP, use source heading order shown in [list.md](list.md#wp-38) and verify earlier substep receipts; preserve the declared stage.

Complete colour, scopes, render/encoding/subtitle profiles and atomic export; verify declared numeric tolerances rather than inventing cross-encoder byte identity.

Search leads: Colour management; Video scopes; Render planning and snapshot binding; Render execution and atomic export; Export presets and encoding; Subtitles and captions; Golden output stability.

Concrete authorities and verification inputs (in addition to common context):

- [docs/architecture/01-solution-and-project-layout.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/01-solution-and-project-layout.md>) — WP citation.
- [docs/architecture/09-ai-and-agent-runtime-architecture.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/09-ai-and-agent-runtime-architecture.md>) — WP citation.
- [docs/architecture/12-native-interop-and-media.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/12-native-interop-and-media.md>) — WP citation.
- [docs/architecture/21-platform-and-dependency-matrix.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/21-platform-and-dependency-matrix.md>) — additional current authority.
- [docs/architecture/23-simulator-and-interchange.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/23-simulator-and-interchange.md>) — WP citation.
- [docs/architecture/26-product-behavior-profiles.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/26-product-behavior-profiles.md>) — additional current authority.
- [docs/architecture/contracts/04-protobuf-wire-registry.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/04-protobuf-wire-registry.md>) — WP citation.
- [docs/architecture/contracts/05-cloudflare-integration.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/05-cloudflare-integration.md>) — WP citation.
- [docs/architecture/contracts/06-native-functional-abi.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/06-native-functional-abi.md>) — additional current authority.
- [docs/architecture/data-model/02-desktop-data-model.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/data-model/02-desktop-data-model.md>) — additional current authority.
- [docs/architecture/data-model/03-derived-stores.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/data-model/03-derived-stores.md>) — additional current authority.
- [docs/assurance/reference-coverage/arcslate-arcvideo.md](<C:/MyFile/Projects/ArcForges-Design/docs/assurance/reference-coverage/arcslate-arcvideo.md>) — additional current authority.
- [docs/requirements/01-normative-glossary-and-invariants.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/01-normative-glossary-and-invariants.md>) — WP citation.
- [docs/requirements/07-security-privacy-and-trust.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/07-security-privacy-and-trust.md>) — WP citation.
- [docs/requirements/13-data-formats-and-portability.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/13-data-formats-and-portability.md>) — WP citation.
- [docs/requirements/products/arcslate.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/products/arcslate.md>) — WP citation.

<a id="wp-39"></a>
### WP-39 — ArcSlate Integration and Portability

Parent: [docs/planning/work-packages/39-arcslate-integration-and-portability.md](<C:/MyFile/Projects/ArcForges-Design/docs/planning/work-packages/39-arcslate-integration-and-portability.md>). Read the **whole file**, including governing prose outside the selected numbered section.

Direct upstream WPs: 25, 38. Within this WP, use source heading order shown in [list.md](list.md#wp-39) and verify earlier substep receipts; preserve the declared stage.

Complete Slate packaging, relink, metadata sync and bidirectional OTIO fidelity. Real AI transcription/adoption integrates later at WP52.

Search leads: Capability surface; Bounded context provision; Collect, consolidate and the portable package; Cross-device resolution and relink; Sync scope; OTIO interchange.

Concrete authorities and verification inputs (in addition to common context):

- [docs/architecture/01-solution-and-project-layout.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/01-solution-and-project-layout.md>) — WP citation.
- [docs/architecture/06-data-persistence-and-formats.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/06-data-persistence-and-formats.md>) — additional current authority.
- [docs/architecture/07-sync-conflict-and-backup.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/07-sync-conflict-and-backup.md>) — additional current authority.
- [docs/architecture/23-simulator-and-interchange.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/23-simulator-and-interchange.md>) — WP citation.
- [docs/architecture/26-product-behavior-profiles.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/26-product-behavior-profiles.md>) — additional current authority.
- [docs/architecture/contracts/02-local-rpc-operations.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/02-local-rpc-operations.md>) — additional current authority.
- [docs/architecture/contracts/04-protobuf-wire-registry.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/04-protobuf-wire-registry.md>) — WP citation.
- [docs/architecture/contracts/05-cloudflare-integration.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/05-cloudflare-integration.md>) — WP citation.
- [docs/architecture/contracts/06-native-functional-abi.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/06-native-functional-abi.md>) — additional current authority.
- [docs/architecture/contracts/07-client-journeys-and-ports.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/07-client-journeys-and-ports.md>) — additional current authority.
- [docs/architecture/data-model/01-cloud-data-model.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/data-model/01-cloud-data-model.md>) — WP citation.
- [docs/architecture/data-model/02-desktop-data-model.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/data-model/02-desktop-data-model.md>) — additional current authority.
- [docs/architecture/data-model/04-d1-execution-profile.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/data-model/04-d1-execution-profile.md>) — additional current authority.
- [docs/assurance/reference-coverage/arcslate-arcvideo.md](<C:/MyFile/Projects/ArcForges-Design/docs/assurance/reference-coverage/arcslate-arcvideo.md>) — additional current authority.
- [docs/requirements/01-normative-glossary-and-invariants.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/01-normative-glossary-and-invariants.md>) — WP citation.
- [docs/requirements/07-security-privacy-and-trust.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/07-security-privacy-and-trust.md>) — WP citation.
- [docs/requirements/13-data-formats-and-portability.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/13-data-formats-and-portability.md>) — WP citation.
- [docs/requirements/products/arcslate.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/products/arcslate.md>) — WP citation.

<a id="wp-41"></a>
### WP-41 — Extension Platform and Integrations

Parent: [docs/planning/work-packages/41-extension-platform-and-integrations.md](<C:/MyFile/Projects/ArcForges-Design/docs/planning/work-packages/41-extension-platform-and-integrations.md>). Read the **whole file**, including governing prose outside the selected numbered section.

Direct upstream WPs: 09, 11, 17, 22, 25. Within this WP, use source heading order shown in [list.md](list.md#wp-41) and verify earlier substep receipts; preserve the declared stage.

Produce extension host/protocol, package/connector lifecycle, public SDK/CLI and actual PackageCatalog APIs. WP45.10 consumes these APIs for review/revocation UI.

Search leads: Extension host and supervision; Handshake and protocol versioning; The dual capability boundary; Declarative UI contribution; Package runtime; PackageCatalog producer and consumers; Public SDK and CLI; MCP placement and connectors.

Concrete authorities and verification inputs (in addition to common context):

- [docs/architecture/01-solution-and-project-layout.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/01-solution-and-project-layout.md>) — WP citation.
- [docs/architecture/08-security-architecture.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/08-security-architecture.md>) — WP citation.
- [docs/architecture/15-extension-platform-architecture.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/15-extension-platform-architecture.md>) — WP citation.
- [docs/architecture/24-content-and-extension-isolation.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/24-content-and-extension-isolation.md>) — additional current authority.
- [docs/architecture/contracts/02-local-rpc-operations.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/02-local-rpc-operations.md>) — additional current authority.
- [docs/architecture/contracts/04-protobuf-wire-registry.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/04-protobuf-wire-registry.md>) — WP citation.
- [docs/architecture/contracts/05-cloudflare-integration.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/05-cloudflare-integration.md>) — WP citation.
- [docs/architecture/contracts/08-extension-and-policy-profiles.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/08-extension-and-policy-profiles.md>) — additional current authority.
- [docs/architecture/contracts/09-local-grpc-and-sandbox.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/09-local-grpc-and-sandbox.md>) — WP citation.
- [docs/architecture/contracts/11-operation-scope-manifest.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/11-operation-scope-manifest.md>) — additional current authority.
- [docs/architecture/data-model/01-cloud-data-model.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/data-model/01-cloud-data-model.md>) — additional current authority.
- [docs/architecture/data-model/02-desktop-data-model.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/data-model/02-desktop-data-model.md>) — additional current authority.
- [docs/experience/03-state-and-acceptance.md](<C:/MyFile/Projects/ArcForges-Design/docs/experience/03-state-and-acceptance.md>) — additional current authority.
- [docs/requirements/01-normative-glossary-and-invariants.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/01-normative-glossary-and-invariants.md>) — WP citation.
- [docs/requirements/08-extensions-and-developer-platform.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/08-extensions-and-developer-platform.md>) — WP citation.

Bound inventory / historical evidence; follow current normative owners when amended:

- [docs/assurance/phase-1-official-verification.md](<C:/MyFile/Projects/ArcForges-Design/docs/assurance/phase-1-official-verification.md>)

<a id="wp-42"></a>
### WP-42 — Commerce, Entitlement and Credits

Parent: [docs/planning/work-packages/42-commerce-entitlement-and-credits.md](<C:/MyFile/Projects/ArcForges-Design/docs/planning/work-packages/42-commerce-entitlement-and-credits.md>). Read the **whole file**, including governing prose outside the selected numbered section.

Direct upstream WPs: 22, 23. Within this WP, use source heading order shown in [list.md](list.md#wp-42) and verify earlier substep receipts; preserve the declared stage.

Implement technical commerce and test-mode proof. Execute 42.11 before 42.10. Actual receipt, payout, pricing activation and customer journey remain gated at WP48/50.

Search leads: Provider adapter boundary; Catalogue and versioned policy; Purchase pipeline; Provider event inbox; Entitlement resolver; Distribution and enforcement; Quota, usage and storage accounting; Credits; Ledgers and reconciliation; Refunds, disputes and evidence; Service term and replenishing capacity; Technical commerce closure and live gate staging.

Concrete authorities and verification inputs (in addition to common context):

- [docs/architecture/01-solution-and-project-layout.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/01-solution-and-project-layout.md>) — WP citation.
- [docs/architecture/16-billing-and-commerce-architecture.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/16-billing-and-commerce-architecture.md>) — WP citation.
- [docs/architecture/20-cross-system-lifecycles.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/20-cross-system-lifecycles.md>) — additional current authority.
- [docs/architecture/contracts/01-public-api-operations.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/01-public-api-operations.md>) — additional current authority.
- [docs/architecture/contracts/04-protobuf-wire-registry.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/04-protobuf-wire-registry.md>) — WP citation.
- [docs/architecture/contracts/05-cloudflare-integration.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/05-cloudflare-integration.md>) — WP citation.
- [docs/architecture/contracts/07-client-journeys-and-ports.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/07-client-journeys-and-ports.md>) — additional current authority.
- [docs/architecture/contracts/08-extension-and-policy-profiles.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/08-extension-and-policy-profiles.md>) — additional current authority.
- [docs/architecture/data-model/00-data-model-overview.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/data-model/00-data-model-overview.md>) — additional current authority.
- [docs/architecture/data-model/01-cloud-data-model.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/data-model/01-cloud-data-model.md>) — WP citation.
- [docs/architecture/data-model/04-d1-execution-profile.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/data-model/04-d1-execution-profile.md>) — additional current authority.
- [docs/assurance/commercial-figure-status.md](<C:/MyFile/Projects/ArcForges-Design/docs/assurance/commercial-figure-status.md>) — additional current authority.
- [docs/requirements/01-normative-glossary-and-invariants.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/01-normative-glossary-and-invariants.md>) — WP citation.
- [docs/requirements/04-commerce-entitlement-and-credits.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/04-commerce-entitlement-and-credits.md>) — WP citation.

Bound inventory / historical evidence; follow current normative owners when amended:

- [docs/assurance/phase-1-official-verification.md](<C:/MyFile/Projects/ArcForges-Design/docs/assurance/phase-1-official-verification.md>)

<a id="wp-44"></a>
### WP-44 — Dynamic Policy and Configuration Control Plane

Parent: [docs/planning/work-packages/44-dynamic-policy-and-configuration.md](<C:/MyFile/Projects/ArcForges-Design/docs/planning/work-packages/44-dynamic-policy-and-configuration.md>). Read the **whole file**, including governing prose outside the selected numbered section.

Direct upstream WPs: 23, 42. Within this WP, use source heading order shown in [list.md](list.md#wp-44) and verify earlier substep receipts; preserve the declared stage.

Produce typed policy/configuration authority with deterministic rollout, history and last-known-good recovery before its AI/search/operations consumers.

Search leads: The four boundaries; Schema-constrained configuration; Compiled hard limits; Features, flags and deterministic rollout; Kill switches; Scoped resolution and explainability; Compatibility policy; Publication, staleness and last-known-good.

Concrete authorities and verification inputs (in addition to common context):

- [docs/architecture/01-solution-and-project-layout.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/01-solution-and-project-layout.md>) — WP citation.
- [docs/architecture/05-cloud-architecture.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/05-cloud-architecture.md>) — WP citation.
- [docs/architecture/16-billing-and-commerce-architecture.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/16-billing-and-commerce-architecture.md>) — additional current authority.
- [docs/architecture/20-cross-system-lifecycles.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/20-cross-system-lifecycles.md>) — additional current authority.
- [docs/architecture/contracts/04-protobuf-wire-registry.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/04-protobuf-wire-registry.md>) — WP citation.
- [docs/architecture/contracts/05-cloudflare-integration.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/05-cloudflare-integration.md>) — WP citation.
- [docs/architecture/contracts/08-extension-and-policy-profiles.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/08-extension-and-policy-profiles.md>) — additional current authority.
- [docs/architecture/contracts/11-operation-scope-manifest.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/11-operation-scope-manifest.md>) — additional current authority.
- [docs/architecture/data-model/01-cloud-data-model.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/data-model/01-cloud-data-model.md>) — WP citation.
- [docs/architecture/data-model/04-d1-execution-profile.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/data-model/04-d1-execution-profile.md>) — additional current authority.
- [docs/experience/03-state-and-acceptance.md](<C:/MyFile/Projects/ArcForges-Design/docs/experience/03-state-and-acceptance.md>) — additional current authority.
- [docs/requirements/11-policy-and-configuration.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/11-policy-and-configuration.md>) — WP citation.

<a id="wp-43"></a>
### WP-43 — Workers AI Routing and Metering

Parent: [docs/planning/work-packages/43-managed-ai-routing-and-metering.md](<C:/MyFile/Projects/ArcForges-Design/docs/planning/work-packages/43-managed-ai-routing-and-metering.md>). Read the **whole file**, including governing prose outside the selected numbered section.

Direct upstream WPs: 25, 42, 44. Within this WP, use source heading order shown in [list.md](list.md#wp-43) and verify earlier substep receipts; preserve the declared stage.

Implement actual Workers AI routing/metering and uncertain-outcome handling. Execute 43.07 before 43.06; recorded fixtures complement real supplier/usage evidence.

Search leads: Provider adapters and routing; Tariffs and cost dimensions; Metering and settlement; Selected supplier and realm routing; Provider interaction records and transparency; Funding and uncertain outcome proof; Real-provider metering evidence; Provider test-environment coverage.

Concrete authorities and verification inputs (in addition to common context):

- [docs/architecture/01-solution-and-project-layout.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/01-solution-and-project-layout.md>) — WP citation.
- [docs/architecture/09-ai-and-agent-runtime-architecture.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/09-ai-and-agent-runtime-architecture.md>) — WP citation.
- [docs/architecture/16-billing-and-commerce-architecture.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/16-billing-and-commerce-architecture.md>) — additional current authority.
- [docs/architecture/17-agent-harness.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/17-agent-harness.md>) — additional current authority.
- [docs/architecture/contracts/04-protobuf-wire-registry.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/04-protobuf-wire-registry.md>) — WP citation.
- [docs/architecture/contracts/05-cloudflare-integration.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/05-cloudflare-integration.md>) — WP citation.
- [docs/architecture/contracts/07-client-journeys-and-ports.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/07-client-journeys-and-ports.md>) — additional current authority.
- [docs/architecture/data-model/00-data-model-overview.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/data-model/00-data-model-overview.md>) — additional current authority.
- [docs/architecture/data-model/01-cloud-data-model.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/data-model/01-cloud-data-model.md>) — additional current authority.
- [docs/architecture/data-model/04-d1-execution-profile.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/data-model/04-d1-execution-profile.md>) — additional current authority.
- [docs/assurance/commercial-figure-status.md](<C:/MyFile/Projects/ArcForges-Design/docs/assurance/commercial-figure-status.md>) — additional current authority.
- [docs/requirements/00-product-scope-and-portfolio.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/00-product-scope-and-portfolio.md>) — WP citation.
- [docs/requirements/01-normative-glossary-and-invariants.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/01-normative-glossary-and-invariants.md>) — WP citation.
- [docs/requirements/04-commerce-entitlement-and-credits.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/04-commerce-entitlement-and-credits.md>) — WP citation.
- [docs/requirements/05-ai-and-agent-execution.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/05-ai-and-agent-execution.md>) — WP citation.
- [docs/requirements/07-security-privacy-and-trust.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/07-security-privacy-and-trust.md>) — WP citation.
- [docs/requirements/11-policy-and-configuration.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/11-policy-and-configuration.md>) — WP citation.
- [docs/requirements/13-data-formats-and-portability.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/13-data-formats-and-portability.md>) — WP citation.
- [docs/requirements/products/arcchat.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/products/arcchat.md>) — WP citation.

Bound inventory / historical evidence; follow current normative owners when amended:

- [docs/assurance/phase-1-official-verification.md](<C:/MyFile/Projects/ArcForges-Design/docs/assurance/phase-1-official-verification.md>)

<a id="wp-40"></a>
### WP-40 — Application-Scoped Knowledge Search and Retrieval

Parent: [docs/planning/work-packages/40-knowledge-search-and-retrieval.md](<C:/MyFile/Projects/ArcForges-Design/docs/planning/work-packages/40-knowledge-search-and-retrieval.md>). Read the **whole file**, including governing prose outside the selected numbered section.

Direct upstream WPs: 19, 25, 28, 43, 44. Within this WP, use source heading order shown in [list.md](list.md#wp-40) and verify earlier substep receipts; preserve the declared stage.

Produce actual application-scoped derived search/retrieval with current permissions, consent and citations. No cross-product aggregator is introduced.

Search leads: Source ownership; Scoped derived index production; Hybrid retrieval and budgets; Current permission; Evidence and citations; Privacy and caches; Real Cloud query path.

Concrete authorities and verification inputs (in addition to common context):

- [docs/architecture/09-ai-and-agent-runtime-architecture.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/09-ai-and-agent-runtime-architecture.md>) — additional current authority.
- [docs/architecture/17-agent-harness.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/17-agent-harness.md>) — additional current authority.
- [docs/architecture/27-platform-projects-and-application-assistants.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/27-platform-projects-and-application-assistants.md>) — WP citation.
- [docs/architecture/contracts/04-protobuf-wire-registry.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/04-protobuf-wire-registry.md>) — WP citation.
- [docs/architecture/contracts/05-cloudflare-integration.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/05-cloudflare-integration.md>) — additional current authority.
- [docs/architecture/contracts/07-client-journeys-and-ports.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/07-client-journeys-and-ports.md>) — additional current authority.
- [docs/architecture/contracts/10-application-scope-and-streams.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/10-application-scope-and-streams.md>) — WP citation.
- [docs/architecture/data-model/01-cloud-data-model.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/data-model/01-cloud-data-model.md>) — additional current authority.
- [docs/architecture/data-model/03-derived-stores.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/data-model/03-derived-stores.md>) — additional current authority.
- [docs/architecture/data-model/04-d1-execution-profile.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/data-model/04-d1-execution-profile.md>) — WP citation.
- [docs/architecture/data-model/05-application-history.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/data-model/05-application-history.md>) — WP citation.
- [docs/experience/03-state-and-acceptance.md](<C:/MyFile/Projects/ArcForges-Design/docs/experience/03-state-and-acceptance.md>) — WP citation.
- [docs/experience/README.md](<C:/MyFile/Projects/ArcForges-Design/docs/experience/README.md>) — WP citation.
- [docs/requirements/06-knowledge-search-and-retrieval.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/06-knowledge-search-and-retrieval.md>) — additional current authority.
- [docs/requirements/products/arcchat.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/products/arcchat.md>) — additional current authority.
- [docs/requirements/products/arcnotes.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/products/arcnotes.md>) — additional current authority.

<a id="wp-47"></a>
### WP-47 — Static Public Site

Parent: [docs/planning/work-packages/47-static-public-site.md](<C:/MyFile/Projects/ArcForges-Design/docs/planning/work-packages/47-static-public-site.md>). Read the **whole file**, including governing prose outside the selected numbered section.

Direct upstream WPs: 00, 02. Within this WP, use source heading order shown in [list.md](list.md#wp-47) and verify earlier substep receipts; preserve the declared stage.

Produce Web tooling/design system and static site before WP45. Approved-shape test offers/downloads are fixtures; real public projection and activation close at WP50.

Search leads: React static generation and determinism; Versioned public content and pricing inputs; Rendering and performance; Internationalisation; Documentation, downloads and legal; Accessibility and analytics; Independence and deployment; Owned consumer design system.

Concrete authorities and verification inputs (in addition to common context):

- [docs/architecture/01-solution-and-project-layout.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/01-solution-and-project-layout.md>) — WP citation.
- [docs/architecture/10-web-architecture.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/10-web-architecture.md>) — WP citation.
- [docs/architecture/14-build-packaging-and-release.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/14-build-packaging-and-release.md>) — additional current authority.
- [docs/architecture/25-web-toolchain-and-sdk.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/25-web-toolchain-and-sdk.md>) — WP citation.
- [docs/architecture/contracts/04-protobuf-wire-registry.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/04-protobuf-wire-registry.md>) — WP citation.
- [docs/architecture/contracts/05-cloudflare-integration.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/05-cloudflare-integration.md>) — WP citation.
- [docs/assurance/reference-coverage/distribution-startarcforges.md](<C:/MyFile/Projects/ArcForges-Design/docs/assurance/reference-coverage/distribution-startarcforges.md>) — additional current authority.
- [docs/experience/03-state-and-acceptance.md](<C:/MyFile/Projects/ArcForges-Design/docs/experience/03-state-and-acceptance.md>) — additional current authority.
- [docs/requirements/09-shared-desktop-experience.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/09-shared-desktop-experience.md>) — additional current authority.
- [docs/requirements/12-quality-and-compatibility-contract.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/12-quality-and-compatibility-contract.md>) — WP citation.
- [docs/requirements/products/arcforges-web.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/products/arcforges-web.md>) — WP citation.

<a id="wp-45"></a>
### WP-45 — Operations, Support and Trust & Safety

Parent: [docs/planning/work-packages/45-operations-support-and-trust-safety.md](<C:/MyFile/Projects/ArcForges-Design/docs/planning/work-packages/45-operations-support-and-trust-safety.md>). Read the **whole file**, including governing prose outside the selected numbered section.

Direct upstream WPs: 12, 21, 41, 44, 47. Within this WP, use source heading order shown in [list.md](list.md#wp-45) and verify earlier substep receipts; preserve the declared stage.

Build actual Operations UI, customer push sender and PackageCatalog review. Rehearse implemented paths now; backup/Harness/combined disaster evidence joins at WP46/52/50.

Search leads: Service levels and alerting; Incident process; Runbooks and rehearsal; Status page; Operator console and support access; Break-glass; Support cases and in-product reporting; Trust and safety; Operational mail and provider drills; Customer push delivery and registration lifecycle; Package review and revocation console.

Concrete authorities and verification inputs (in addition to common context):

- [docs/architecture/01-solution-and-project-layout.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/01-solution-and-project-layout.md>) — WP citation.
- [docs/architecture/10-web-architecture.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/10-web-architecture.md>) — additional current authority.
- [docs/architecture/13-observability-and-operations.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/13-observability-and-operations.md>) — WP citation.
- [docs/architecture/15-extension-platform-architecture.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/15-extension-platform-architecture.md>) — additional current authority.
- [docs/architecture/25-web-toolchain-and-sdk.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/25-web-toolchain-and-sdk.md>) — additional current authority.
- [docs/architecture/contracts/04-protobuf-wire-registry.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/04-protobuf-wire-registry.md>) — WP citation.
- [docs/architecture/contracts/05-cloudflare-integration.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/05-cloudflare-integration.md>) — WP citation.
- [docs/architecture/contracts/07-client-journeys-and-ports.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/07-client-journeys-and-ports.md>) — additional current authority.
- [docs/architecture/contracts/08-extension-and-policy-profiles.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/08-extension-and-policy-profiles.md>) — additional current authority.
- [docs/architecture/contracts/11-operation-scope-manifest.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/11-operation-scope-manifest.md>) — additional current authority.
- [docs/architecture/data-model/01-cloud-data-model.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/data-model/01-cloud-data-model.md>) — WP citation.
- [docs/architecture/data-model/04-d1-execution-profile.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/data-model/04-d1-execution-profile.md>) — additional current authority.
- [docs/experience/03-state-and-acceptance.md](<C:/MyFile/Projects/ArcForges-Design/docs/experience/03-state-and-acceptance.md>) — additional current authority.
- [docs/requirements/07-security-privacy-and-trust.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/07-security-privacy-and-trust.md>) — additional current authority.
- [docs/requirements/10-distribution-update-and-support.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/10-distribution-update-and-support.md>) — WP citation.
- [docs/requirements/12-quality-and-compatibility-contract.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/12-quality-and-compatibility-contract.md>) — WP citation.
- [docs/requirements/products/arcforges-cloud.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/products/arcforges-cloud.md>) — WP citation.
- [docs/requirements/products/arcforges-web.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/products/arcforges-web.md>) — additional current authority.

<a id="wp-53"></a>
### WP-53 — Desktop Distribution, Update Client and Channels

Parent: [docs/planning/work-packages/53-desktop-distribution-and-update.md](<C:/MyFile/Projects/ArcForges-Design/docs/planning/work-packages/53-desktop-distribution-and-update.md>). Read the **whole file**, including governing prose outside the selected numbered section.

Direct upstream WPs: 02, 06, 07, 10, 11, 12, 44, 45. Within this WP, use source heading order shown in [list.md](list.md#wp-53) and verify earlier substep receipts; preserve the declared stage.

Produce the updater and distribution trust with real staged apply/rollback. Keep the source numbering gap: 53.06 does not exist. Test signing proves mechanics; WP50 verifies production release trust.

Search leads: Signed feed and applicable target; Background download and staging; Safe apply and atomic activation; Rollback and migration interlock; Channels, staged rollout and security updates; Diagnostics and preserving data on uninstall; Production catalog and Android distribution trust.

Concrete authorities and verification inputs (in addition to common context):

- [docs/architecture/14-build-packaging-and-release.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/14-build-packaging-and-release.md>) — WP citation.
- [docs/architecture/21-platform-and-dependency-matrix.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/21-platform-and-dependency-matrix.md>) — additional current authority.
- [docs/architecture/22-deployment-and-release-execution.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/22-deployment-and-release-execution.md>) — additional current authority.
- [docs/architecture/contracts/04-protobuf-wire-registry.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/04-protobuf-wire-registry.md>) — additional current authority.
- [docs/architecture/contracts/07-client-journeys-and-ports.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/07-client-journeys-and-ports.md>) — additional current authority.
- [docs/architecture/contracts/08-extension-and-policy-profiles.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/08-extension-and-policy-profiles.md>) — additional current authority.
- [docs/assurance/reference-coverage/distribution-startarcforges.md](<C:/MyFile/Projects/ArcForges-Design/docs/assurance/reference-coverage/distribution-startarcforges.md>) — additional current authority.
- [docs/experience/03-state-and-acceptance.md](<C:/MyFile/Projects/ArcForges-Design/docs/experience/03-state-and-acceptance.md>) — additional current authority.
- [docs/requirements/10-distribution-update-and-support.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/10-distribution-update-and-support.md>) — WP citation.
- [docs/requirements/12-quality-and-compatibility-contract.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/12-quality-and-compatibility-contract.md>) — additional current authority.

<a id="wp-46"></a>
### WP-46 — D1, R2 and Independent Disaster Recovery

Parent: [docs/planning/work-packages/46-backup-recovery-and-data-health.md](<C:/MyFile/Projects/ArcForges-Design/docs/planning/work-packages/46-backup-recovery-and-data-health.md>). Read the **whole file**, including governing prose outside the selected numbered section.

Direct upstream WPs: 25, 45. Within this WP, use source heading order shown in [list.md](list.md#wp-46) and verify earlier substep receipts; preserve the declared stage.

Prove independent D1/R2 backup and fresh restore, generation fencing and denial of old effects/credentials. Combined active Harness recovery still closes at WP50.

Search leads: D1 and independent object backup; Point-in-time and fresh restore; Fresh environment rebuild; Drill programme; Data health; Export and realm migration; Backup release gate.

Concrete authorities and verification inputs (in addition to common context):

- [docs/architecture/07-sync-conflict-and-backup.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/07-sync-conflict-and-backup.md>) — additional current authority.
- [docs/architecture/20-cross-system-lifecycles.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/20-cross-system-lifecycles.md>) — additional current authority.
- [docs/architecture/22-deployment-and-release-execution.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/22-deployment-and-release-execution.md>) — additional current authority.
- [docs/architecture/27-platform-projects-and-application-assistants.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/27-platform-projects-and-application-assistants.md>) — WP citation.
- [docs/architecture/contracts/04-protobuf-wire-registry.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/04-protobuf-wire-registry.md>) — WP citation.
- [docs/architecture/contracts/05-cloudflare-integration.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/05-cloudflare-integration.md>) — additional current authority.
- [docs/architecture/contracts/07-client-journeys-and-ports.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/07-client-journeys-and-ports.md>) — additional current authority.
- [docs/architecture/contracts/10-application-scope-and-streams.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/10-application-scope-and-streams.md>) — WP citation.
- [docs/architecture/data-model/00-data-model-overview.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/data-model/00-data-model-overview.md>) — additional current authority.
- [docs/architecture/data-model/01-cloud-data-model.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/data-model/01-cloud-data-model.md>) — additional current authority.
- [docs/architecture/data-model/02-desktop-data-model.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/data-model/02-desktop-data-model.md>) — additional current authority.
- [docs/architecture/data-model/04-d1-execution-profile.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/data-model/04-d1-execution-profile.md>) — WP citation.
- [docs/architecture/data-model/05-application-history.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/data-model/05-application-history.md>) — WP citation.
- [docs/experience/03-state-and-acceptance.md](<C:/MyFile/Projects/ArcForges-Design/docs/experience/03-state-and-acceptance.md>) — WP citation.
- [docs/experience/README.md](<C:/MyFile/Projects/ArcForges-Design/docs/experience/README.md>) — WP citation.
- [docs/requirements/03-cloud-services-and-sync.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/03-cloud-services-and-sync.md>) — additional current authority.
- [docs/requirements/13-data-formats-and-portability.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/13-data-formats-and-portability.md>) — additional current authority.
- [docs/requirements/products/arcforges-cloud.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/products/arcforges-cloud.md>) — additional current authority.

<a id="wp-48"></a>
### WP-48 — Account Portal

Parent: [docs/planning/work-packages/48-account-portal.md](<C:/MyFile/Projects/ArcForges-Design/docs/planning/work-packages/48-account-portal.md>). Read the **whole file**, including governing prose outside the selected numbered section.

Direct upstream WPs: 25, 42, 44, 46, 47. Within this WP, use source heading order shown in [list.md](list.md#wp-48) and verify earlier substep receipts; preserve the declared stage.

Deliver real account/session/commerce/export UI using the actual upstream producers; activation still requires the applicable real provider evidence.

Search leads: Account profile and native ceremony integration; Real browser session and step-up acceptance; Account and security surfaces; Workspace, storage and usage; Subscription, capacity, credits and hosted checkout; Data export and deletion; Origin security and performance; Offline, degradation and accessibility.

Concrete authorities and verification inputs (in addition to common context):

- [docs/architecture/01-solution-and-project-layout.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/01-solution-and-project-layout.md>) — WP citation.
- [docs/architecture/08-security-architecture.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/08-security-architecture.md>) — WP citation.
- [docs/architecture/10-web-architecture.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/10-web-architecture.md>) — WP citation.
- [docs/architecture/16-billing-and-commerce-architecture.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/16-billing-and-commerce-architecture.md>) — WP citation.
- [docs/architecture/20-cross-system-lifecycles.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/20-cross-system-lifecycles.md>) — additional current authority.
- [docs/architecture/25-web-toolchain-and-sdk.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/25-web-toolchain-and-sdk.md>) — WP citation.
- [docs/architecture/contracts/01-public-api-operations.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/01-public-api-operations.md>) — WP citation.
- [docs/architecture/contracts/04-protobuf-wire-registry.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/04-protobuf-wire-registry.md>) — WP citation.
- [docs/architecture/contracts/05-cloudflare-integration.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/05-cloudflare-integration.md>) — WP citation.
- [docs/architecture/contracts/07-client-journeys-and-ports.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/07-client-journeys-and-ports.md>) — additional current authority.
- [docs/architecture/contracts/10-application-scope-and-streams.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/10-application-scope-and-streams.md>) — additional current authority.
- [docs/architecture/data-model/01-cloud-data-model.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/data-model/01-cloud-data-model.md>) — WP citation.
- [docs/architecture/data-model/04-d1-execution-profile.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/data-model/04-d1-execution-profile.md>) — additional current authority.
- [docs/experience/03-state-and-acceptance.md](<C:/MyFile/Projects/ArcForges-Design/docs/experience/03-state-and-acceptance.md>) — additional current authority.
- [docs/requirements/02-identity-account-and-workspace.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/02-identity-account-and-workspace.md>) — WP citation.
- [docs/requirements/04-commerce-entitlement-and-credits.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/04-commerce-entitlement-and-credits.md>) — additional current authority.
- [docs/requirements/11-policy-and-configuration.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/11-policy-and-configuration.md>) — WP citation.
- [docs/requirements/12-quality-and-compatibility-contract.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/12-quality-and-compatibility-contract.md>) — WP citation.
- [docs/requirements/products/arcforges-web.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/products/arcforges-web.md>) — additional current authority.

<a id="wp-51"></a>
### WP-51 — ArcScope Deterministic Cloud Simulator

Parent: [docs/planning/work-packages/51-arcscope-cloud-simulator.md](<C:/MyFile/Projects/ArcForges-Design/docs/planning/work-packages/51-arcscope-cloud-simulator.md>). Read the **whole file**, including governing prose outside the selected numbered section.

Direct upstream WPs: 21, 23, 25, 33, 34, 35, 42, 44. Within this WP, use source heading order shown in [list.md](list.md#wp-51) and verify earlier substep receipts; preserve the declared stage.

Implement real deterministic simulator jobs, fenced D1 segment/checkpoint publication and R2 delivery into Scope. Synthetic results remain labelled and cannot prove hardware.

Search leads: Definitions, versions and bounded evaluation; Deterministic generation and faults; Fenced slices and SimulationPacer; Canonical publication, checkpoints and recovery; Client access and native ingestion; Limits, entitlement and lifecycle.

Concrete authorities and verification inputs (in addition to common context):

- [docs/architecture/01-solution-and-project-layout.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/01-solution-and-project-layout.md>) — WP citation.
- [docs/architecture/05-cloud-architecture.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/05-cloud-architecture.md>) — WP citation.
- [docs/architecture/23-simulator-and-interchange.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/23-simulator-and-interchange.md>) — WP citation.
- [docs/architecture/26-product-behavior-profiles.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/26-product-behavior-profiles.md>) — additional current authority.
- [docs/architecture/contracts/01-public-api-operations.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/01-public-api-operations.md>) — WP citation.
- [docs/architecture/contracts/04-protobuf-wire-registry.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/04-protobuf-wire-registry.md>) — WP citation.
- [docs/architecture/contracts/05-cloudflare-integration.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/05-cloudflare-integration.md>) — WP citation.
- [docs/architecture/contracts/06-native-functional-abi.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/06-native-functional-abi.md>) — additional current authority.
- [docs/architecture/data-model/00-data-model-overview.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/data-model/00-data-model-overview.md>) — additional current authority.
- [docs/architecture/data-model/01-cloud-data-model.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/data-model/01-cloud-data-model.md>) — WP citation.
- [docs/architecture/data-model/04-d1-execution-profile.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/data-model/04-d1-execution-profile.md>) — additional current authority.
- [docs/requirements/01-normative-glossary-and-invariants.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/01-normative-glossary-and-invariants.md>) — WP citation.
- [docs/requirements/04-commerce-entitlement-and-credits.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/04-commerce-entitlement-and-credits.md>) — additional current authority.
- [docs/requirements/products/arcscope.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/products/arcscope.md>) — WP citation.

<a id="wp-52"></a>
### WP-52 — Sole Cloudflare Workflow Harness

Parent: [docs/planning/work-packages/52-cloud-harness.md](<C:/MyFile/Projects/ArcForges-Design/docs/planning/work-packages/52-cloud-harness.md>). Read the **whole file**, including governing prose outside the selected numbered section.

Direct upstream WPs: 15, 17, 21, 23, 26, 39, 40, 41, 42, 43, 44. Within this WP, use source heading order shown in [list.md](list.md#wp-52) and verify earlier substep receipts; preserve the declared stage.

Implement the sole Workflow Harness with actual model/usage, local/Cloud/temporary modes, same-application tools and automation. Replace assigned earlier client fixtures and preserve uncertain effects.

Search leads: The turn loop, batching and bounds; Context assembly and compaction; Approval, cancellation and crash recovery; Generated streaming and durable output; Provider failure and effect certainty; Complete own-application execution proof; Durable Cloud automation and authorised scheduling.

Concrete authorities and verification inputs (in addition to common context):

- [docs/architecture/01-solution-and-project-layout.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/01-solution-and-project-layout.md>) — WP citation.
- [docs/architecture/09-ai-and-agent-runtime-architecture.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/09-ai-and-agent-runtime-architecture.md>) — WP citation.
- [docs/architecture/17-agent-harness.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/17-agent-harness.md>) — WP citation.
- [docs/architecture/20-cross-system-lifecycles.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/20-cross-system-lifecycles.md>) — WP citation.
- [docs/architecture/contracts/03-realtime-and-bridge.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/03-realtime-and-bridge.md>) — additional current authority.
- [docs/architecture/contracts/04-protobuf-wire-registry.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/04-protobuf-wire-registry.md>) — WP citation.
- [docs/architecture/contracts/05-cloudflare-integration.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/05-cloudflare-integration.md>) — WP citation.
- [docs/architecture/contracts/07-client-journeys-and-ports.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/07-client-journeys-and-ports.md>) — additional current authority.
- [docs/architecture/contracts/10-application-scope-and-streams.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/10-application-scope-and-streams.md>) — additional current authority.
- [docs/architecture/data-model/00-data-model-overview.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/data-model/00-data-model-overview.md>) — WP citation.
- [docs/architecture/data-model/01-cloud-data-model.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/data-model/01-cloud-data-model.md>) — additional current authority.
- [docs/architecture/data-model/03-derived-stores.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/data-model/03-derived-stores.md>) — additional current authority.
- [docs/architecture/data-model/04-d1-execution-profile.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/data-model/04-d1-execution-profile.md>) — additional current authority.
- [docs/architecture/data-model/05-application-history.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/data-model/05-application-history.md>) — additional current authority.
- [docs/experience/03-state-and-acceptance.md](<C:/MyFile/Projects/ArcForges-Design/docs/experience/03-state-and-acceptance.md>) — additional current authority.
- [docs/requirements/01-normative-glossary-and-invariants.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/01-normative-glossary-and-invariants.md>) — WP citation.
- [docs/requirements/05-ai-and-agent-execution.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/05-ai-and-agent-execution.md>) — WP citation.
- [docs/requirements/07-security-privacy-and-trust.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/07-security-privacy-and-trust.md>) — WP citation.
- [docs/requirements/08-extensions-and-developer-platform.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/08-extensions-and-developer-platform.md>) — WP citation.
- [docs/requirements/13-data-formats-and-portability.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/13-data-formats-and-portability.md>) — WP citation.
- [docs/requirements/products/arcchat.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/products/arcchat.md>) — additional current authority.

Bound inventory / historical evidence; follow current normative owners when amended:

- [docs/assurance/phase-1-official-verification.md](<C:/MyFile/Projects/ArcForges-Design/docs/assurance/phase-1-official-verification.md>)

<a id="wp-31"></a>
### WP-31 — Complete ArcChat Android Companion

Parent: [docs/planning/work-packages/31-arcchat-mobile-android.md](<C:/MyFile/Projects/ArcForges-Design/docs/planning/work-packages/31-arcchat-mobile-android.md>). Read the **whole file**, including governing prose outside the selected numbered section.

Direct upstream WPs: 26, 30, 45, 52. Within this WP, use source heading order shown in [list.md](list.md#wp-31) and verify earlier substep receipts; preserve the declared stage.

Complete the Android UI and companion flows against real Harness, Cloud and one-application bridge. Real push sender WP45.09 is already upstream.

Search leads: Authentication, Home and workspace; Conversations and context; Tasks, approvals and automation; Library and resources; Presence, push, links and settings; Native interaction and recovery; Scope and licence enforcement.

Concrete authorities and verification inputs (in addition to common context):

- [docs/architecture/11-mobile-architecture.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/11-mobile-architecture.md>) — WP citation.
- [docs/architecture/contracts/03-realtime-and-bridge.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/03-realtime-and-bridge.md>) — additional current authority.
- [docs/architecture/contracts/04-protobuf-wire-registry.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/04-protobuf-wire-registry.md>) — WP citation.
- [docs/architecture/contracts/07-client-journeys-and-ports.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/07-client-journeys-and-ports.md>) — WP citation.
- [docs/architecture/contracts/10-application-scope-and-streams.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/10-application-scope-and-streams.md>) — additional current authority.
- [docs/assurance/reference-coverage/arcchat-aionui.md](<C:/MyFile/Projects/ArcForges-Design/docs/assurance/reference-coverage/arcchat-aionui.md>) — additional current authority.
- [docs/experience/02-android-companion.md](<C:/MyFile/Projects/ArcForges-Design/docs/experience/02-android-companion.md>) — additional current authority.
- [docs/experience/03-state-and-acceptance.md](<C:/MyFile/Projects/ArcForges-Design/docs/experience/03-state-and-acceptance.md>) — additional current authority.
- [docs/requirements/products/arcchat-mobile-and-web.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/products/arcchat-mobile-and-web.md>) — WP citation.

<a id="wp-32"></a>
### WP-32 — Android Signing, Distribution and Store Gates

Parent: [docs/planning/work-packages/32-mobile-release-and-store-gates.md](<C:/MyFile/Projects/ArcForges-Design/docs/planning/work-packages/32-mobile-release-and-store-gates.md>). Read the **whole file**, including governing prose outside the selected numbered section.

Direct upstream WPs: 31. Within this WP, use source heading order shown in [list.md](list.md#wp-32) and verify earlier substep receipts; preserve the declared stage.

Verify signed Android distribution on actual required devices/channels, signing identity, consumption-only rules, push and non-GMS fallback. Missing external access remains a named gate.

Search leads: Signed Android release artifacts; Release runtime inspection; Dependency and source rights; Consumption-only enforcement; Play and direct-channel updates; Physical device and recovery gates; Android scope statement.

Concrete authorities and verification inputs (in addition to common context):

- [docs/architecture/11-mobile-architecture.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/11-mobile-architecture.md>) — WP citation.
- [docs/architecture/14-build-packaging-and-release.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/14-build-packaging-and-release.md>) — additional current authority.
- [docs/architecture/21-platform-and-dependency-matrix.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/21-platform-and-dependency-matrix.md>) — additional current authority.
- [docs/architecture/22-deployment-and-release-execution.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/22-deployment-and-release-execution.md>) — additional current authority.
- [docs/architecture/contracts/04-protobuf-wire-registry.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/04-protobuf-wire-registry.md>) — WP citation.
- [docs/architecture/contracts/07-client-journeys-and-ports.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/07-client-journeys-and-ports.md>) — WP citation.
- [docs/assurance/reference-coverage/distribution-startarcforges.md](<C:/MyFile/Projects/ArcForges-Design/docs/assurance/reference-coverage/distribution-startarcforges.md>) — additional current authority.
- [docs/experience/02-android-companion.md](<C:/MyFile/Projects/ArcForges-Design/docs/experience/02-android-companion.md>) — additional current authority.
- [docs/experience/03-state-and-acceptance.md](<C:/MyFile/Projects/ArcForges-Design/docs/experience/03-state-and-acceptance.md>) — additional current authority.
- [docs/requirements/10-distribution-update-and-support.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/10-distribution-update-and-support.md>) — additional current authority.
- [docs/requirements/12-quality-and-compatibility-contract.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/12-quality-and-compatibility-contract.md>) — additional current authority.
- [docs/requirements/products/arcchat-mobile-and-web.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/products/arcchat-mobile-and-web.md>) — WP citation.

<a id="wp-49"></a>
### WP-49 — Web companion Companion

Parent: [docs/planning/work-packages/49-arcchat-web-companion.md](<C:/MyFile/Projects/ArcForges-Design/docs/planning/work-packages/49-arcchat-web-companion.md>). Read the **whole file**, including governing prose outside the selected numbered section.

Direct upstream WPs: 26, 48, 52. Within this WP, use source heading order shown in [list.md](list.md#wp-49) and verify earlier substep receipts; preserve the declared stage.

Complete browser Chat UI against actual Cloud/Harness/device bridge. Apply browser session/CSP/fallback policy rather than Android-only or local-desktop behaviors.

Search leads: React Chat profile and design-system integration; Conversation and generated output streams; Tasks, approval and steering; Artifacts and sandboxing; One-application remote control; Offline, degradation and accessibility; Performance budgets.

Concrete authorities and verification inputs (in addition to common context):

- [docs/architecture/01-solution-and-project-layout.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/01-solution-and-project-layout.md>) — WP citation.
- [docs/architecture/10-web-architecture.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/10-web-architecture.md>) — WP citation.
- [docs/architecture/25-web-toolchain-and-sdk.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/25-web-toolchain-and-sdk.md>) — WP citation.
- [docs/architecture/27-platform-projects-and-application-assistants.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/27-platform-projects-and-application-assistants.md>) — additional current authority.
- [docs/architecture/contracts/03-realtime-and-bridge.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/03-realtime-and-bridge.md>) — additional current authority.
- [docs/architecture/contracts/04-protobuf-wire-registry.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/04-protobuf-wire-registry.md>) — WP citation.
- [docs/architecture/contracts/05-cloudflare-integration.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/05-cloudflare-integration.md>) — WP citation.
- [docs/architecture/contracts/07-client-journeys-and-ports.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/07-client-journeys-and-ports.md>) — additional current authority.
- [docs/architecture/contracts/10-application-scope-and-streams.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/10-application-scope-and-streams.md>) — additional current authority.
- [docs/architecture/data-model/05-application-history.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/data-model/05-application-history.md>) — additional current authority.
- [docs/experience/01-embedded-assistant.md](<C:/MyFile/Projects/ArcForges-Design/docs/experience/01-embedded-assistant.md>) — additional current authority.
- [docs/experience/03-state-and-acceptance.md](<C:/MyFile/Projects/ArcForges-Design/docs/experience/03-state-and-acceptance.md>) — additional current authority.
- [docs/requirements/12-quality-and-compatibility-contract.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/12-quality-and-compatibility-contract.md>) — WP citation.
- [docs/requirements/products/arcchat-mobile-and-web.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/products/arcchat-mobile-and-web.md>) — WP citation.
- [docs/requirements/products/arcforges-web.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/products/arcforges-web.md>) — additional current authority.

<a id="wp-50"></a>
### WP-50 — Full-Platform Production Release

Parent: [docs/planning/work-packages/50-full-platform-production-release.md](<C:/MyFile/Projects/ArcForges-Design/docs/planning/work-packages/50-full-platform-production-release.md>). Read the **whole file**, including governing prose outside the selected numbered section.

Direct upstream WPs: 28, 32, 35, 39, 40, 41, 43, 46, 49, 51, 52, 53. Within this WP, use source heading order shown in [list.md](list.md#wp-50) and verify earlier substep receipts; preserve the declared stage.

Join all required real product, platform, provider, store, operational and commercial evidence. Promote the same tested immutable bytes; no required fixture-backed route may pass as release.

Search leads: Release readiness audit; Licence, SBOM and copied-content audit; Desktop release across three platforms; Android release; Cloud production; Commercial launch; Node-built Web release set and real-browser verification; Operational readiness; Honest release statement.

Concrete authorities and verification inputs (in addition to common context):

- [docs/architecture/01-solution-and-project-layout.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/01-solution-and-project-layout.md>) — WP citation.
- [docs/architecture/14-build-packaging-and-release.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/14-build-packaging-and-release.md>) — WP citation.
- [docs/architecture/20-cross-system-lifecycles.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/20-cross-system-lifecycles.md>) — WP citation.
- [docs/architecture/21-platform-and-dependency-matrix.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/21-platform-and-dependency-matrix.md>) — additional current authority.
- [docs/architecture/22-deployment-and-release-execution.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/22-deployment-and-release-execution.md>) — additional current authority.
- [docs/architecture/25-web-toolchain-and-sdk.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/25-web-toolchain-and-sdk.md>) — WP citation.
- [docs/architecture/contracts/04-protobuf-wire-registry.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/04-protobuf-wire-registry.md>) — WP citation.
- [docs/architecture/contracts/05-cloudflare-integration.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/contracts/05-cloudflare-integration.md>) — WP citation.
- [docs/architecture/data-model/04-d1-execution-profile.md](<C:/MyFile/Projects/ArcForges-Design/docs/architecture/data-model/04-d1-execution-profile.md>) — additional current authority.
- [docs/assurance/commercial-figure-status.md](<C:/MyFile/Projects/ArcForges-Design/docs/assurance/commercial-figure-status.md>) — additional current authority.
- [docs/assurance/reference-coverage/distribution-startarcforges.md](<C:/MyFile/Projects/ArcForges-Design/docs/assurance/reference-coverage/distribution-startarcforges.md>) — additional current authority.
- [docs/experience/03-state-and-acceptance.md](<C:/MyFile/Projects/ArcForges-Design/docs/experience/03-state-and-acceptance.md>) — additional current authority.
- [docs/requirements/04-commerce-entitlement-and-credits.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/04-commerce-entitlement-and-credits.md>) — additional current authority.
- [docs/requirements/10-distribution-update-and-support.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/10-distribution-update-and-support.md>) — additional current authority.
- [docs/requirements/12-quality-and-compatibility-contract.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/12-quality-and-compatibility-contract.md>) — WP citation.
- [docs/requirements/products/arcchat-mobile-and-web.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/products/arcchat-mobile-and-web.md>) — additional current authority.
- [docs/requirements/products/arcforges-cloud.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/products/arcforges-cloud.md>) — additional current authority.
- [docs/requirements/products/arcforges-web.md](<C:/MyFile/Projects/ArcForges-Design/docs/requirements/products/arcforges-web.md>) — additional current authority.
