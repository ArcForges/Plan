# ArcForges implementation sequence

Design baseline: `575ba9f929bcb2806e08b9776d9bdb7b0633358a`. 51 active work packages, 447 owning substeps, 158 dependency edges.

Copy **one code block** below into a fresh or continuing AI task. Each block names the reusable prompt, the exact formal owning section and its reading context. No substitution or whole-WP selection is needed. Start at 00.00; select the next entry yourself after checking the current receipt.

This is an execution index, not a second specification or a progress ledger. A listed/compiled document is not an accepted implementation. Read the prompt and the [reading map](reading-map.md); check the [execution receipts](execution/README.md). Each run must freshly search current related Design beyond these entry points.

Order follows implementation-sequence §9, then owning headings in each WP. Explicit source ordering preserves 42.11 before 42.10 and 43.07 before 43.06. Each .90 is a separate final stage gate. WP20 is future-only; WP27/29 are retired; no missing numeric ID is synthesized. Nested NN.MM.K sections stay with their owning NN.MM[A].

Prerequisites are the direct upstream WPs and preceding substeps within the current WP, at their prescribed stages. The navigation sequence does not add prerequisite edges. Future evidence is pending only where the formal producer matrix explicitly permits it.

## Work-package navigation

| Position | Work package | Substeps | Direct upstream WPs |
|---|---|---:|---|
| 1 | [WP-00 — Specification, Naming and Rights Freeze](#wp-00) | 7 | None |
| 2 | [WP-01 — Repository Reconciliation and Target Layout](#wp-01) | 7 | 00 |
| 3 | [WP-02 — Build Governance, Packaging Policy and Analyzers](#wp-02) | 7 | 01 |
| 4 | [WP-03 — Proto Contract Foundation and License Split](#wp-03) | 9 | 02 |
| 5 | [WP-04 — Identity, Error, Revision and Versioning Primitives](#wp-04) | 7 | 03 |
| 6 | [WP-05 — Architecture and Repository Policy Test Suite](#wp-05) | 8 | 02, 03 |
| 7 | [WP-06 — AOT, Android, CF and Real Artifact Publish Proof](#wp-06) | 9 | 03, 04, 05 |
| 8 | [WP-07 — Local Persistence Foundation](#wp-07) | 8 | 04, 06 |
| 9 | [WP-08 — Private Helper gRPC and Parent Registration](#wp-08) | 8 | 06, 07 |
| 10 | [WP-09 — Capability, Contribution and Resource Model](#wp-09) | 9 | 03, 08 |
| 11 | [WP-10 — Design System and Desktop Shell Foundation](#wp-10) | 10 | 06, 09 |
| 12 | [WP-11 — Security Foundation](#wp-11) | 11 | 04, 08, 09 |
| 13 | [WP-12 — Observability Foundation](#wp-12) | 7 | 04, 06 |
| 14 | [WP-13 — Complete Native Producers and Technical Probes](#wp-13) | 18 | 06, 07, 08, 09, 10, 11, 12 |
| 15 | [WP-14 — Independent Application Composition and Typed Host Ports](#wp-14) | 8 | 08, 09, 10, 11, 13 |
| 16 | [WP-15 — Application Assistant Conversation, History and Project Packages](#wp-15) | 9 | 14 |
| 17 | [WP-16 — Unified Execution Engine](#wp-16) | 9 | 09, 11, 14 |
| 18 | [WP-17 — Complete Embedded Assistant and Cloud Client Surface](#wp-17) | 9 | 06, 15, 16 |
| 19 | [WP-18 — ArcNotes Document Core](#wp-18) | 10 | 07, 10, 14 |
| 20 | [WP-19 — ArcNotes Search, Import, Export and Portability](#wp-19) | 8 | 18 |
| 21 | [WP-21 — Cloudflare Container, D1 Authority and Binding Plans](#wp-21) | 10 | 03, 05, 12 |
| 22 | [WP-22 — Identity, Workspace, Device and Session](#wp-22) | 10 | 11, 21 |
| 23 | [WP-23 — Public Proto APIs and Generated Clients](#wp-23) | 8 | 03, 22 |
| 24 | [WP-24 — gRPC-Web Streams and Durable Event Recovery](#wp-24) | 8 | 23 |
| 25 | [WP-25 — Sync Engine and Blob Lifecycle](#wp-25) | 11 | 19, 24 |
| 26 | [WP-26 — Application Presence and One-Application Tool Bridge](#wp-26) | 8 | 17, 24, 25 |
| 27 | [WP-28 — ArcNotes Bounded Properties and Saved Views](#wp-28) | 8 | 19, 25 |
| 28 | [WP-30 — Kotlin Android Foundation](#wp-30) | 7 | 03, 06, 23, 24, 25 |
| 29 | [WP-33 — ArcScope Acquisition and Session Core](#wp-33) | 9 | 07, 10, 13, 26 |
| 30 | [WP-34 — ArcScope Visualisation, Analysis and Reporting](#wp-34) | 8 | 33 |
| 31 | [WP-35 — ArcScope Integration and Metadata Sync](#wp-35) | 7 | 25, 34 |
| 32 | [WP-36 — ArcSlate Project, Timeline and Media Model](#wp-36) | 9 | 07, 10, 13, 26 |
| 33 | [WP-37 — ArcSlate Playback and Processing Runtime](#wp-37) | 8 | 36 |
| 34 | [WP-38 — ArcSlate Render, Export and Colour Management](#wp-38) | 8 | 37 |
| 35 | [WP-39 — ArcSlate Integration and Portability](#wp-39) | 7 | 25, 38 |
| 36 | [WP-41 — Extension Platform and Integrations](#wp-41) | 9 | 09, 11, 17, 22, 25 |
| 37 | [WP-42 — Commerce, Entitlement and Credits](#wp-42) | 13 | 22, 23 |
| 38 | [WP-44 — Dynamic Policy and Configuration Control Plane](#wp-44) | 9 | 23, 42 |
| 39 | [WP-43 — Workers AI Routing and Metering](#wp-43) | 9 | 25, 42, 44 |
| 40 | [WP-40 — Application-Scoped Knowledge Search and Retrieval](#wp-40) | 8 | 19, 25, 28, 43, 44 |
| 41 | [WP-47 — Static Public Site](#wp-47) | 9 | 00, 02 |
| 42 | [WP-45 — Operations, Support and Trust & Safety](#wp-45) | 12 | 12, 21, 41, 44, 47 |
| 43 | [WP-53 — Desktop Distribution, Update Client and Channels](#wp-53) | 8 | 02, 06, 07, 10, 11, 12, 44, 45 |
| 44 | [WP-46 — D1, R2 and Independent Disaster Recovery](#wp-46) | 8 | 25, 45 |
| 45 | [WP-48 — Account Portal](#wp-48) | 9 | 25, 42, 44, 46, 47 |
| 46 | [WP-51 — ArcScope Deterministic Cloud Simulator](#wp-51) | 7 | 21, 23, 25, 33, 34, 35, 42, 44 |
| 47 | [WP-52 — Sole Cloudflare Workflow Harness](#wp-52) | 8 | 15, 17, 21, 23, 26, 39, 40, 41, 42, 43, 44 |
| 48 | [WP-31 — Complete ArcChat Android Companion](#wp-31) | 8 | 26, 30, 45, 52 |
| 49 | [WP-32 — Android Signing, Distribution and Store Gates](#wp-32) | 8 | 31 |
| 50 | [WP-49 — Web companion Companion](#wp-49) | 8 | 26, 48, 52 |
| 51 | [WP-50 — Full-Platform Production Release](#wp-50) | 10 | 28, 32, 35, 39, 40, 41, 43, 46, 49, 51, 52, 53 |

## Copy one substep

<a id="wp-00"></a>
### WP-00 — Specification, Naming and Rights Freeze

Full WP: [formal source](<C:/MyFile/Projects/ArcForges-Design/docs/planning/work-packages/00-specification-naming-and-rights-freeze.md>). Reading context: [WP00](reading-map.md#wp-00).

Direct upstream WPs: none. Freeze current authority, names, rights and reusable policy evidence. No future package or Cloud manifest is an input; completed source/reference audits are consumed and checked for drift.

<a id="substep-00-00"></a>
#### 001. 00.00 — Product and naming freeze

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 00.00 — Product and naming freeze.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\00-specification-naming-and-rights-freeze.md
Owning section: WP-00.00; explicit anchor: rule-wp-00.00.
Read the common context and WP00 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-00); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-00-01"></a>
#### 002. 00.01 — Glossary and invariant enforcement data

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 00.01 — Glossary and invariant enforcement data.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\00-specification-naming-and-rights-freeze.md
Owning section: WP-00.01; explicit anchor: rule-wp-00.01.
Read the common context and WP00 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-00); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-00-02"></a>
#### 003. 00.02 — Licence boundary declaration

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 00.02 — Licence boundary declaration.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\00-specification-naming-and-rights-freeze.md
Owning section: WP-00.02; explicit anchor: rule-wp-00.02.
Read the common context and WP00 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-00); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-00-03"></a>
#### 004. 00.03 — Reuse and provenance process

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 00.03 — Reuse and provenance process.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\00-specification-naming-and-rights-freeze.md
Owning section: WP-00.03; explicit anchor: rule-wp-00.03.
Read the common context and WP00 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-00); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-00-04"></a>
#### 005. 00.04 — Register the completed reference matrices as versioned planning inputs

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 00.04 — Register the completed reference matrices as versioned planning inputs.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\00-specification-naming-and-rights-freeze.md
Owning section: WP-00.04; explicit anchor: rule-wp-00.04.
Read the common context and WP00 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-00); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-00-05"></a>
#### 006. 00.05 — Stale-claim reconciliation

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 00.05 — Stale-claim reconciliation.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\00-specification-naming-and-rights-freeze.md
Owning section: WP-00.05; explicit anchor: rule-wp-00.05.
Read the common context and WP00 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-00); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-00-90"></a>
#### 007. 00.90 — Verify the owned artifact and real integration

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 00.90 — Verify the owned artifact and real integration.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\00-specification-naming-and-rights-freeze.md
Owning section: WP-00.90; explicit anchor: rule-wp-00.90.
Read the common context and WP00 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-00); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="wp-01"></a>
### WP-01 — Repository Reconciliation and Target Layout

Full WP: [formal source](<C:/MyFile/Projects/ArcForges-Design/docs/planning/work-packages/01-repository-reconciliation-and-target-layout.md>). Reading context: [WP01](reading-map.md#wp-01).

Direct upstream WPs: 00. Reconcile the nine actual repositories against their current HEADs. The ede43db monorepo inventory is historical disposition evidence, not a target tree to recreate.

<a id="substep-01-00"></a>
#### 008. 01.00 — Verify nine independent current repositories

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 01.00 — Verify nine independent current repositories.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\01-repository-reconciliation-and-target-layout.md
Owning section: WP-01.00; explicit anchor: rule-wp-01.00.
Read the common context and WP01 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-01); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-01-01"></a>
#### 009. 01.01 — Implement the frozen contract split

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 01.01 — Implement the frozen contract split.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\01-repository-reconciliation-and-target-layout.md
Owning section: WP-01.01; explicit anchor: rule-wp-01.01.
Read the common context and WP01 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-01); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-01-02"></a>
#### 010. 01.02 — Shared-foundation boundary review

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 01.02 — Shared-foundation boundary review.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\01-repository-reconciliation-and-target-layout.md
Owning section: WP-01.02; explicit anchor: rule-wp-01.02.
Read the common context and WP01 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-01); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-01-03"></a>
#### 011. 01.03 — Execute the native surface dispositions

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 01.03 — Execute the native surface dispositions.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\01-repository-reconciliation-and-target-layout.md
Owning section: WP-01.03; explicit anchor: rule-wp-01.03.
Read the common context and WP01 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-01); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-01-04"></a>
#### 012. 01.04 — Test suite mapping

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 01.04 — Test suite mapping.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\01-repository-reconciliation-and-target-layout.md
Owning section: WP-01.04; explicit anchor: rule-wp-01.04.
Read the common context and WP01 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-01); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-01-05"></a>
#### 013. 01.05 — Apply bounded repository reconciliation

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 01.05 — Apply bounded repository reconciliation.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\01-repository-reconciliation-and-target-layout.md
Owning section: WP-01.05; explicit anchor: rule-wp-01.05.
Read the common context and WP01 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-01); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-01-90"></a>
#### 014. 01.90 — Verify the owned artifact and real integration

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 01.90 — Verify the owned artifact and real integration.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\01-repository-reconciliation-and-target-layout.md
Owning section: WP-01.90; explicit anchor: rule-wp-01.90.
Read the common context and WP01 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-01); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="wp-02"></a>
### WP-02 — Build Governance, Packaging Policy and Analyzers

Full WP: [formal source](<C:/MyFile/Projects/ArcForges-Design/docs/planning/work-packages/02-build-governance-and-analyzer-policy.md>). Reading context: [WP02](reading-map.md#wp-02).

Direct upstream WPs: 01. Own toolchain/build-policy and candidate pipelines. Preserve independent roots and staged producer availability; full functional native packages are WP13.

<a id="substep-02-00"></a>
#### 015. 02.00 — Pin and lock each toolchain

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 02.00 — Pin and lock each toolchain.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\02-build-governance-and-analyzer-policy.md
Owning section: WP-02.00; explicit anchor: rule-wp-02.00.
Read the common context and WP02 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-02); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-02-01"></a>
#### 016. 02.01 — Diagnostic posture

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 02.01 — Diagnostic posture.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\02-build-governance-and-analyzer-policy.md
Owning section: WP-02.01; explicit anchor: rule-wp-02.01.
Read the common context and WP02 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-02); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-02-02"></a>
#### 017. 02.02 — AOT and trim declaration sweep

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 02.02 — AOT and trim declaration sweep.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\02-build-governance-and-analyzer-policy.md
Owning section: WP-02.02; explicit anchor: rule-wp-02.02.
Read the common context and WP02 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-02); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-02-03"></a>
#### 018. 02.03 — Runtime and directory boundaries

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 02.03 — Runtime and directory boundaries.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\02-build-governance-and-analyzer-policy.md
Owning section: WP-02.03; explicit anchor: rule-wp-02.03.
Read the common context and WP02 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-02); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-02-04"></a>
#### 019. 02.04 — Version axis plumbing

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 02.04 — Version axis plumbing.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\02-build-governance-and-analyzer-policy.md
Owning section: WP-02.04; explicit anchor: rule-wp-02.04.
Read the common context and WP02 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-02); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-02-05"></a>
#### 020. 02.05 — Dependency policy

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 02.05 — Dependency policy.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\02-build-governance-and-analyzer-policy.md
Owning section: WP-02.05; explicit anchor: rule-wp-02.05.
Read the common context and WP02 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-02); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-02-90"></a>
#### 021. 02.90 — Verify the owned artifact and real integration

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 02.90 — Verify the owned artifact and real integration.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\02-build-governance-and-analyzer-policy.md
Owning section: WP-02.90; explicit anchor: rule-wp-02.90.
Read the common context and WP02 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-02); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="wp-03"></a>
### WP-03 — Proto Contract Foundation and License Split

Full WP: [formal source](<C:/MyFile/Projects/ArcForges-Design/docs/planning/work-packages/03-contract-foundation-and-licence-split.md>). Reading context: [WP03](reading-map.md#wp-03).

Direct upstream WPs: 02. Produce the complete initial NuGet/npm/Maven contract closure, all concrete operation metadata and independent semantic fixtures. Business handlers belong to later owners; contract completeness cannot be deferred to them.

<a id="substep-03-00"></a>
#### 022. 03.00 — Create the split project structure

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 03.00 — Create the split project structure.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\03-contract-foundation-and-licence-split.md
Owning section: WP-03.00; explicit anchor: rule-wp-03.00.
Read the common context and WP03 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-03); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-03-01"></a>
#### 023. 03.01 — Foundation contract types

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 03.01 — Foundation contract types.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\03-contract-foundation-and-licence-split.md
Owning section: WP-03.01; explicit anchor: rule-wp-03.01.
Read the common context and WP03 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-03); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-03-02"></a>
#### 024. 03.02 — Serialization posture

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 03.02 — Serialization posture.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\03-contract-foundation-and-licence-split.md
Owning section: WP-03.02; explicit anchor: rule-wp-03.02.
Read the common context and WP03 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-03); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-03-03"></a>
#### 025. 03.03 — Capability and resource contract types

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 03.03 — Capability and resource contract types.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\03-contract-foundation-and-licence-split.md
Owning section: WP-03.03; explicit anchor: rule-wp-03.03.
Read the common context and WP03 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-03); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-03-04"></a>
#### 026. 03.04 — Private helper and in-process contract split

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 03.04 — Private helper and in-process contract split.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\03-contract-foundation-and-licence-split.md
Owning section: WP-03.04; explicit anchor: rule-wp-03.04.
Read the common context and WP03 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-03); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-03-05"></a>
#### 027. 03.05 — Complete generated package and schema gate

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 03.05 — Complete generated package and schema gate.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\03-contract-foundation-and-licence-split.md
Owning section: WP-03.05; explicit anchor: rule-wp-03.05.
Read the common context and WP03 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-03); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-03-06"></a>
#### 028. 03.06 — Cross-language compatibility window

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 03.06 — Cross-language compatibility window.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\03-contract-foundation-and-licence-split.md
Owning section: WP-03.06; explicit anchor: rule-wp-03.06.
Read the common context and WP03 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-03); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-03-07"></a>
#### 029. 03.07 — Signed catalog and update format producer

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 03.07 — Signed catalog and update format producer.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\03-contract-foundation-and-licence-split.md
Owning section: WP-03.07; explicit anchor: rule-wp-03.07.
Read the common context and WP03 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-03); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-03-90"></a>
#### 030. 03.90 — Verify the owned artifact and real integration

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 03.90 — Verify the owned artifact and real integration.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\03-contract-foundation-and-licence-split.md
Owning section: WP-03.90; explicit anchor: rule-wp-03.90.
Read the common context and WP03 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-03); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="wp-04"></a>
### WP-04 — Identity, Error, Revision and Versioning Primitives

Full WP: [formal source](<C:/MyFile/Projects/ArcForges-Design/docs/planning/work-packages/04-identity-error-and-versioning-primitives.md>). Reading context: [WP04](reading-map.md#wp-04).

Direct upstream WPs: 03. Implement exact value/error/version primitives without a future database dependency. Use the current producer registry for Foundation ownership and consumer adapters.

<a id="substep-04-00"></a>
#### 031. 04.00 — Shared identity, error and version primitives

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 04.00 — Shared identity, error and version primitives.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\04-identity-error-and-versioning-primitives.md
Owning section: WP-04.00; explicit anchor: rule-wp-04.00.
Read the common context and WP04 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-04); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-04-01"></a>
#### 032. 04.01 — Execution identity and idempotency

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 04.01 — Execution identity and idempotency.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\04-identity-error-and-versioning-primitives.md
Owning section: WP-04.01; explicit anchor: rule-wp-04.01.
Read the common context and WP04 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-04); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-04-02"></a>
#### 033. 04.02 — Revision and sequence

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 04.02 — Revision and sequence.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\04-identity-error-and-versioning-primitives.md
Owning section: WP-04.02; explicit anchor: rule-wp-04.02.
Read the common context and WP04 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-04); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-04-03"></a>
#### 034. 04.03 — Time

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 04.03 — Time.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\04-identity-error-and-versioning-primitives.md
Owning section: WP-04.03; explicit anchor: rule-wp-04.03.
Read the common context and WP04 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-04); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-04-04"></a>
#### 035. 04.04 — Error and reason codes

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 04.04 — Error and reason codes.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\04-identity-error-and-versioning-primitives.md
Owning section: WP-04.04; explicit anchor: rule-wp-04.04.
Read the common context and WP04 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-04); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-04-05"></a>
#### 036. 04.05 — Version axis types

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 04.05 — Version axis types.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\04-identity-error-and-versioning-primitives.md
Owning section: WP-04.05; explicit anchor: rule-wp-04.05.
Read the common context and WP04 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-04); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-04-90"></a>
#### 037. 04.90 — Verify the owned artifact and real integration

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 04.90 — Verify the owned artifact and real integration.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\04-identity-error-and-versioning-primitives.md
Owning section: WP-04.90; explicit anchor: rule-wp-04.90.
Read the common context and WP04 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-04); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="wp-05"></a>
### WP-05 — Architecture and Repository Policy Test Suite

Full WP: [formal source](<C:/MyFile/Projects/ArcForges-Design/docs/planning/work-packages/05-architecture-and-repository-policy-tests.md>). Reading context: [WP05](reading-map.md#wp-05).

Direct upstream WPs: 02, 03. Enforce current architecture and repository policy. A scoped invariant test/accounting contribution does not close every future implementation gate.

<a id="substep-05-00"></a>
#### 038. 05.00 — Layering and reference direction

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 05.00 — Layering and reference direction.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\05-architecture-and-repository-policy-tests.md
Owning section: WP-05.00; explicit anchor: rule-wp-05.00.
Read the common context and WP05 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-05); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-05-01"></a>
#### 039. 05.01 — Licence boundary enforcement

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 05.01 — Licence boundary enforcement.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\05-architecture-and-repository-policy-tests.md
Owning section: WP-05.01; explicit anchor: rule-wp-05.01.
Read the common context and WP05 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-05); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-05-02"></a>
#### 040. 05.02 — Forbidden terms and naming

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 05.02 — Forbidden terms and naming.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\05-architecture-and-repository-policy-tests.md
Owning section: WP-05.02; explicit anchor: rule-wp-05.02.
Read the common context and WP05 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-05); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-05-03"></a>
#### 041. 05.03 — Contract and serialization policy

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 05.03 — Contract and serialization policy.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\05-architecture-and-repository-policy-tests.md
Owning section: WP-05.03; explicit anchor: rule-wp-05.03.
Read the common context and WP05 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-05); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-05-04"></a>
#### 042. 05.04 — Banned APIs and patterns

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 05.04 — Banned APIs and patterns.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\05-architecture-and-repository-policy-tests.md
Owning section: WP-05.04; explicit anchor: rule-wp-05.04.
Read the common context and WP05 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-05); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-05-05"></a>
#### 043. 05.05 — Invariant enforcement accounting

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 05.05 — Invariant enforcement accounting.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\05-architecture-and-repository-policy-tests.md
Owning section: WP-05.05; explicit anchor: rule-wp-05.05.
Read the common context and WP05 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-05); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-05-06"></a>
#### 044. 05.06 — Specification integrity

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 05.06 — Specification integrity.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\05-architecture-and-repository-policy-tests.md
Owning section: WP-05.06; explicit anchor: rule-wp-05.06.
Read the common context and WP05 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-05); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-05-90"></a>
#### 045. 05.90 — Verify the owned artifact and real integration

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 05.90 — Verify the owned artifact and real integration.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\05-architecture-and-repository-policy-tests.md
Owning section: WP-05.90; explicit anchor: rule-wp-05.90.
Read the common context and WP05 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-05); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="wp-06"></a>
### WP-06 — AOT, Android, CF and Real Artifact Publish Proof

Full WP: [formal source](<C:/MyFile/Projects/ArcForges-Design/docs/planning/work-packages/06-aot-jit-and-wasm-publish-proof.md>). Reading context: [WP06](reading-map.md#wp-06).

Direct upstream WPs: 03, 04, 05. Run actual minimal AOT, browser, Kotlin Android and Cloudflare transport/package proofs. Use the designated isolated probe ports; do not require the future full Harness.

<a id="substep-06-00"></a>
#### 046. 06.00 — Desktop Native AOT package proof

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 06.00 — Desktop Native AOT package proof.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\06-aot-jit-and-wasm-publish-proof.md
Owning section: WP-06.00; explicit anchor: rule-wp-06.00.
Read the common context and WP06 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-06); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-06-01"></a>
#### 047. 06.01 — Local RPC under AOT

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 06.01 — Local RPC under AOT.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\06-aot-jit-and-wasm-publish-proof.md
Owning section: WP-06.01; explicit anchor: rule-wp-06.01.
Read the common context and WP06 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-06); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-06-02"></a>
#### 048. 06.02 — Generated gRPC-Web under AOT

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 06.02 — Generated gRPC-Web under AOT.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\06-aot-jit-and-wasm-publish-proof.md
Owning section: WP-06.02; explicit anchor: rule-wp-06.02.
Read the common context and WP06 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-06); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-06-03"></a>
#### 049. 06.03 — Realtime under AOT

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 06.03 — Realtime under AOT.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\06-aot-jit-and-wasm-publish-proof.md
Owning section: WP-06.03; explicit anchor: rule-wp-06.03.
Read the common context and WP06 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-06); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-06-04"></a>
#### 050. 06.04 — Cloudflare Native AOT and D1 proof

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 06.04 — Cloudflare Native AOT and D1 proof.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\06-aot-jit-and-wasm-publish-proof.md
Owning section: WP-06.04; explicit anchor: rule-wp-06.04.
Read the common context and WP06 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-06); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-06-05"></a>
#### 051. 06.05 — React production build and generated SDK proof

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 06.05 — React production build and generated SDK proof.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\06-aot-jit-and-wasm-publish-proof.md
Owning section: WP-06.05; explicit anchor: rule-wp-06.05.
Read the common context and WP06 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-06); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-06-06"></a>
#### 052. 06.06 — Third-party control gate

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 06.06 — Third-party control gate.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\06-aot-jit-and-wasm-publish-proof.md
Owning section: WP-06.06; explicit anchor: rule-wp-06.06.
Read the common context and WP06 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-06); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-06-07"></a>
#### 053. 06.07 — Android gRPC-Web and CF proof

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 06.07 — Android gRPC-Web and CF proof.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\06-aot-jit-and-wasm-publish-proof.md
Owning section: WP-06.07; explicit anchor: rule-wp-06.07.
Read the common context and WP06 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-06); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-06-90"></a>
#### 054. 06.90 — Verify the owned artifact and real integration

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 06.90 — Verify the owned artifact and real integration.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\06-aot-jit-and-wasm-publish-proof.md
Owning section: WP-06.90; explicit anchor: rule-wp-06.90.
Read the common context and WP06 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-06); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="wp-07"></a>
### WP-07 — Local Persistence Foundation

Full WP: [formal source](<C:/MyFile/Projects/ArcForges-Design/docs/planning/work-packages/07-local-persistence-foundation.md>). Reading context: [WP07](reading-map.md#wp-07).

Direct upstream WPs: 04, 06. Produce persistence mechanisms with owner fixtures, exact atomicity/recovery and published package evidence. Product-specific schema behavior remains with product owners.

<a id="substep-07-00"></a>
#### 055. 07.00 — Store abstraction and the single write path

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 07.00 — Store abstraction and the single write path.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\07-local-persistence-foundation.md
Owning section: WP-07.00; explicit anchor: rule-wp-07.00.
Read the common context and WP07 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-07); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-07-01"></a>
#### 056. 07.01 — Journal

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 07.01 — Journal.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\07-local-persistence-foundation.md
Owning section: WP-07.01; explicit anchor: rule-wp-07.01.
Read the common context and WP07 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-07); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-07-02"></a>
#### 057. 07.02 — Snapshot and recovery

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 07.02 — Snapshot and recovery.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\07-local-persistence-foundation.md
Owning section: WP-07.02; explicit anchor: rule-wp-07.02.
Read the common context and WP07 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-07); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-07-03"></a>
#### 058. 07.03 — Migration runner

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 07.03 — Migration runner.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\07-local-persistence-foundation.md
Owning section: WP-07.03; explicit anchor: rule-wp-07.03.
Read the common context and WP07 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-07); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-07-04"></a>
#### 059. 07.04 — Managed resource store

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 07.04 — Managed resource store.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\07-local-persistence-foundation.md
Owning section: WP-07.04; explicit anchor: rule-wp-07.04.
Read the common context and WP07 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-07); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-07-05"></a>
#### 060. 07.05 — Large append store

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 07.05 — Large append store.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\07-local-persistence-foundation.md
Owning section: WP-07.05; explicit anchor: rule-wp-07.05.
Read the common context and WP07 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-07); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-07-06"></a>
#### 061. 07.06 — Derived stores and storage pressure

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 07.06 — Derived stores and storage pressure.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\07-local-persistence-foundation.md
Owning section: WP-07.06; explicit anchor: rule-wp-07.06.
Read the common context and WP07 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-07); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-07-90"></a>
#### 062. 07.90 — Verify the owned artifact and real integration

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 07.90 — Verify the owned artifact and real integration.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\07-local-persistence-foundation.md
Owning section: WP-07.90; explicit anchor: rule-wp-07.90.
Read the common context and WP07 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-07); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="wp-08"></a>
### WP-08 — Private Helper gRPC and Parent Registration

Full WP: [formal source](<C:/MyFile/Projects/ArcForges-Design/docs/planning/work-packages/08-local-ipc-and-registration.md>). Reading context: [WP08](reading-map.md#wp-08).

Direct upstream WPs: 06, 07. Implement private parent/child helper gRPC only. In-process product ports, independent application sessions and future cross-product collaboration do not create local service listeners.

<a id="substep-08-00"></a>
#### 063. 08.00 — Transport and framing

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 08.00 — Transport and framing.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\08-local-ipc-and-registration.md
Owning section: WP-08.00; explicit anchor: rule-wp-08.00.
Read the common context and WP08 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-08); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-08-01"></a>
#### 064. 08.01 — Parent-owned endpoint identity

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 08.01 — Parent-owned endpoint identity.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\08-local-ipc-and-registration.md
Owning section: WP-08.01; explicit anchor: rule-wp-08.01.
Read the common context and WP08 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-08); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-08-02"></a>
#### 065. 08.02 — Child registration lifecycle

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 08.02 — Child registration lifecycle.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\08-local-ipc-and-registration.md
Owning section: WP-08.02; explicit anchor: rule-wp-08.02.
Read the common context and WP08 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-08); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-08-03"></a>
#### 066. 08.03 — Static routing and version refusal

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 08.03 — Static routing and version refusal.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\08-local-ipc-and-registration.md
Owning section: WP-08.03; explicit anchor: rule-wp-08.03.
Read the common context and WP08 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-08); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-08-04"></a>
#### 067. 08.04 — Bounds and concurrency

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 08.04 — Bounds and concurrency.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\08-local-ipc-and-registration.md
Owning section: WP-08.04; explicit anchor: rule-wp-08.04.
Read the common context and WP08 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-08); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-08-05"></a>
#### 068. 08.05 — Disconnect/cancel/retry

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 08.05 — Disconnect/cancel/retry.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\08-local-ipc-and-registration.md
Owning section: WP-08.05; explicit anchor: rule-wp-08.05.
Read the common context and WP08 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-08); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-08-06"></a>
#### 069. 08.06 — Brokered large data

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 08.06 — Brokered large data.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\08-local-ipc-and-registration.md
Owning section: WP-08.06; explicit anchor: rule-wp-08.06.
Read the common context and WP08 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-08); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-08-90"></a>
#### 070. 08.90 — Owned artifacts and real integration

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 08.90 — Owned artifacts and real integration.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\08-local-ipc-and-registration.md
Owning section: WP-08.90; explicit anchor: rule-wp-08.90.
Read the common context and WP08 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-08); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="wp-09"></a>
### WP-09 — Capability, Contribution and Resource Model

Full WP: [formal source](<C:/MyFile/Projects/ArcForges-Design/docs/planning/work-packages/09-capability-contribution-and-resource-model.md>). Reading context: [WP09](reading-map.md#wp-09).

Direct upstream WPs: 03, 08. Implement typed in-process contribution/capability/resource mechanisms over the published contracts, with final validation at the owning application.

<a id="substep-09-00"></a>
#### 071. 09.00 — Application identity and in-process composition

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 09.00 — Application identity and in-process composition.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\09-capability-contribution-and-resource-model.md
Owning section: WP-09.00; explicit anchor: rule-wp-09.00.
Read the common context and WP09 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-09); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-09-01"></a>
#### 072. 09.01 — Static contribution registration

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 09.01 — Static contribution registration.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\09-capability-contribution-and-resource-model.md
Owning section: WP-09.01; explicit anchor: rule-wp-09.01.
Read the common context and WP09 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-09); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-09-02"></a>
#### 073. 09.02 — Capability registry and selection

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 09.02 — Capability registry and selection.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\09-capability-contribution-and-resource-model.md
Owning section: WP-09.02; explicit anchor: rule-wp-09.02.
Read the common context and WP09 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-09); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-09-03"></a>
#### 074. 09.03 — Actions and availability

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 09.03 — Actions and availability.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\09-capability-contribution-and-resource-model.md
Owning section: WP-09.03; explicit anchor: rule-wp-09.03.
Read the common context and WP09 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-09); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-09-04"></a>
#### 075. 09.04 — Context providers and freezing

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 09.04 — Context providers and freezing.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\09-capability-contribution-and-resource-model.md
Owning section: WP-09.04; explicit anchor: rule-wp-09.04.
Read the common context and WP09 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-09); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-09-05"></a>
#### 076. 09.05 — Resources and artifacts

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 09.05 — Resources and artifacts.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\09-capability-contribution-and-resource-model.md
Owning section: WP-09.05; explicit anchor: rule-wp-09.05.
Read the common context and WP09 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-09); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-09-06"></a>
#### 077. 09.06 — Own navigation, hints and health

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 09.06 — Own navigation, hints and health.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\09-capability-contribution-and-resource-model.md
Owning section: WP-09.06; explicit anchor: rule-wp-09.06.
Read the common context and WP09 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-09); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-09-07"></a>
#### 078. 09.07 — Invocation pipeline

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 09.07 — Invocation pipeline.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\09-capability-contribution-and-resource-model.md
Owning section: WP-09.07; explicit anchor: rule-wp-09.07.
Read the common context and WP09 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-09); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-09-90"></a>
#### 079. 09.90 — Verify the owned artifact and real integration

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 09.90 — Verify the owned artifact and real integration.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\09-capability-contribution-and-resource-model.md
Owning section: WP-09.90; explicit anchor: rule-wp-09.90.
Read the common context and WP09 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-09); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="wp-10"></a>
### WP-10 — Design System and Desktop Shell Foundation

Full WP: [formal source](<C:/MyFile/Projects/ArcForges-Design/docs/planning/work-packages/10-design-system-and-desktop-shell.md>). Reading context: [WP10](reading-map.md#wp-10).

Direct upstream WPs: 06, 09. Deliver the reusable desktop shell/design system and applicable UI states. The embedded assistant is a package consumer within each application, not a fourth desktop executable.

<a id="substep-10-00"></a>
#### 080. 10.00 — Token system and theming

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 10.00 — Token system and theming.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\10-design-system-and-desktop-shell.md
Owning section: WP-10.00; explicit anchor: rule-wp-10.00.
Read the common context and WP10 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-10); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-10-01"></a>
#### 081. 10.01 — Windows, panels and layout

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 10.01 — Windows, panels and layout.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\10-design-system-and-desktop-shell.md
Owning section: WP-10.01; explicit anchor: rule-wp-10.01.
Read the common context and WP10 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-10); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-10-02"></a>
#### 082. 10.02 — Command system

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 10.02 — Command system.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\10-design-system-and-desktop-shell.md
Owning section: WP-10.02; explicit anchor: rule-wp-10.02.
Read the common context and WP10 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-10); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-10-03"></a>
#### 083. 10.03 — Scoped settings

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 10.03 — Scoped settings.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\10-design-system-and-desktop-shell.md
Owning section: WP-10.03; explicit anchor: rule-wp-10.03.
Read the common context and WP10 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-10); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-10-04"></a>
#### 084. 10.04 — Attention and notification model

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 10.04 — Attention and notification model.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\10-design-system-and-desktop-shell.md
Owning section: WP-10.04; explicit anchor: rule-wp-10.04.
Read the common context and WP10 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-10); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-10-05"></a>
#### 085. 10.05 — Error presentation

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 10.05 — Error presentation.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\10-design-system-and-desktop-shell.md
Owning section: WP-10.05; explicit anchor: rule-wp-10.05.
Read the common context and WP10 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-10); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-10-06"></a>
#### 086. 10.06 — Lifecycle, menus and shutdown

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 10.06 — Lifecycle, menus and shutdown.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\10-design-system-and-desktop-shell.md
Owning section: WP-10.06; explicit anchor: rule-wp-10.06.
Read the common context and WP10 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-10); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-10-07"></a>
#### 087. 10.07 — Accessibility and localisation baseline

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 10.07 — Accessibility and localisation baseline.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\10-design-system-and-desktop-shell.md
Owning section: WP-10.07; explicit anchor: rule-wp-10.07.
Read the common context and WP10 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-10); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-10-08"></a>
#### 088. 10.08 — Third-party control admission

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 10.08 — Third-party control admission.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\10-design-system-and-desktop-shell.md
Owning section: WP-10.08; explicit anchor: rule-wp-10.08.
Read the common context and WP10 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-10); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-10-90"></a>
#### 089. 10.90 — Verify the owned artifact and real integration

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 10.90 — Verify the owned artifact and real integration.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\10-design-system-and-desktop-shell.md
Owning section: WP-10.90; explicit anchor: rule-wp-10.90.
Read the common context and WP10 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-10); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="wp-11"></a>
### WP-11 — Security Foundation

Full WP: [formal source](<C:/MyFile/Projects/ArcForges-Design/docs/planning/work-packages/11-security-foundation.md>). Reading context: [WP11](reading-map.md#wp-11).

Direct upstream WPs: 04, 08, 09. Implement security mechanisms and the real OS-restricted fixture-parser helper. Production parser composition is WP13.13, not a backwards prerequisite.

<a id="substep-11-00"></a>
#### 090. 11.00 — Principals and the actor chain

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 11.00 — Principals and the actor chain.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\11-security-foundation.md
Owning section: WP-11.00; explicit anchor: rule-wp-11.00.
Read the common context and WP11 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-11); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-11-01"></a>
#### 091. 11.01 — Risk model and classification

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 11.01 — Risk model and classification.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\11-security-foundation.md
Owning section: WP-11.01; explicit anchor: rule-wp-11.01.
Read the common context and WP11 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-11); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-11-02"></a>
#### 092. 11.02 — The decision pipeline and enforcement points

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 11.02 — The decision pipeline and enforcement points.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\11-security-foundation.md
Owning section: WP-11.02; explicit anchor: rule-wp-11.02.
Read the common context and WP11 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-11); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-11-03"></a>
#### 093. 11.03 — Approval, steering and step-up

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 11.03 — Approval, steering and step-up.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\11-security-foundation.md
Owning section: WP-11.03; explicit anchor: rule-wp-11.03.
Read the common context and WP11 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-11); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-11-04"></a>
#### 094. 11.04 — Per-application secrets and session isolation

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 11.04 — Per-application secrets and session isolation.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\11-security-foundation.md
Owning section: WP-11.04; explicit anchor: rule-wp-11.04.
Read the common context and WP11 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-11); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-11-05"></a>
#### 095. 11.05 — Egress control

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 11.05 — Egress control.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\11-security-foundation.md
Owning section: WP-11.05; explicit anchor: rule-wp-11.05.
Read the common context and WP11 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-11); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-11-06"></a>
#### 096. 11.06 — Instruction provenance

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 11.06 — Instruction provenance.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\11-security-foundation.md
Owning section: WP-11.06; explicit anchor: rule-wp-11.06.
Read the common context and WP11 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-11); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-11-07"></a>
#### 097. 11.07 — Capability leases and trust

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 11.07 — Capability leases and trust.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\11-security-foundation.md
Owning section: WP-11.07; explicit anchor: rule-wp-11.07.
Read the common context and WP11 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-11); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-11-08"></a>
#### 098. 11.08 — Audit

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 11.08 — Audit.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\11-security-foundation.md
Owning section: WP-11.08; explicit anchor: rule-wp-11.08.
Read the common context and WP11 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-11); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-11-09"></a>
#### 099. 11.09 — Content helper and OS-enforced isolation

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 11.09 — Content helper and OS-enforced isolation.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\11-security-foundation.md
Owning section: WP-11.09; explicit anchor: rule-wp-11.09.
Read the common context and WP11 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-11); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-11-90"></a>
#### 100. 11.90 — Verify the owned artifact and real integration

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 11.90 — Verify the owned artifact and real integration.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\11-security-foundation.md
Owning section: WP-11.90; explicit anchor: rule-wp-11.90.
Read the common context and WP11 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-11); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="wp-12"></a>
### WP-12 — Observability Foundation

Full WP: [formal source](<C:/MyFile/Projects/ArcForges-Design/docs/planning/work-packages/12-observability-foundation.md>). Reading context: [WP12](reading-map.md#wp-12).

Direct upstream WPs: 04, 06. Deliver reusable observability and explicit privacy/redaction evidence on this stage's actual hosts; later owner operations remain staged.

<a id="substep-12-00"></a>
#### 101. 12.00 — Emission and dimensions

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 12.00 — Emission and dimensions.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\12-observability-foundation.md
Owning section: WP-12.00; explicit anchor: rule-wp-12.00.
Read the common context and WP12 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-12); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-12-01"></a>
#### 102. 12.01 — Correlation and causation

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 12.01 — Correlation and causation.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\12-observability-foundation.md
Owning section: WP-12.01; explicit anchor: rule-wp-12.01.
Read the common context and WP12 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-12); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-12-02"></a>
#### 103. 12.02 — Redaction by construction

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 12.02 — Redaction by construction.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\12-observability-foundation.md
Owning section: WP-12.02; explicit anchor: rule-wp-12.02.
Read the common context and WP12 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-12); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-12-03"></a>
#### 104. 12.03 — Cardinality and sampling

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 12.03 — Cardinality and sampling.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\12-observability-foundation.md
Owning section: WP-12.03; explicit anchor: rule-wp-12.03.
Read the common context and WP12 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-12); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-12-04"></a>
#### 105. 12.04 — Health probes

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 12.04 — Health probes.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\12-observability-foundation.md
Owning section: WP-12.04; explicit anchor: rule-wp-12.04.
Read the common context and WP12 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-12); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-12-05"></a>
#### 106. 12.05 — Desktop diagnostics and consent

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 12.05 — Desktop diagnostics and consent.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\12-observability-foundation.md
Owning section: WP-12.05; explicit anchor: rule-wp-12.05.
Read the common context and WP12 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-12); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-12-90"></a>
#### 107. 12.90 — Verify the owned artifact and real integration

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 12.90 — Verify the owned artifact and real integration.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\12-observability-foundation.md
Owning section: WP-12.90; explicit anchor: rule-wp-12.90.
Read the common context and WP12 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-12); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="wp-13"></a>
### WP-13 — Complete Native Producers and Technical Probes

Full WP: [formal source](<C:/MyFile/Projects/ArcForges-Design/docs/planning/work-packages/13-high-risk-technical-probes.md>). Reading context: [WP13](reading-map.md#wp-13).

Direct upstream WPs: 06, 07, 08, 09, 10, 11, 12. Complete functional native/helper packages, dependencies and clean C17/C# AOT consumers. 13.05 proves all declarations/common layouts; 13.06–13.14 implement families; 13.15/13.90 verify complete packaged exports. 13.04 seeds inventory; 13.16 completes it.

<a id="substep-13-00"></a>
#### 108. 13.00 — Probe A: device tool execution under Native AOT

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 13.00 — Probe A: device tool execution under Native AOT.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\13-high-risk-technical-probes.md
Owning section: WP-13.00; explicit anchor: rule-wp-13.00.
Read the common context and WP13 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-13); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-13-01"></a>
#### 109. 13.01 — Probe B: block editor, store, undo and recovery

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 13.01 — Probe B: block editor, store, undo and recovery.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\13-high-risk-technical-probes.md
Owning section: WP-13.01; explicit anchor: rule-wp-13.01.
Read the common context and WP13 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-13); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-13-02"></a>
#### 110. 13.02 — Probe C: high-throughput acquisition

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 13.02 — Probe C: high-throughput acquisition.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\13-high-risk-technical-probes.md
Owning section: WP-13.02; explicit anchor: rule-wp-13.02.
Read the common context and WP13 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-13); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-13-03"></a>
#### 111. 13.03 — Probe D: native decode and synchronisation

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 13.03 — Probe D: native decode and synchronisation.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\13-high-risk-technical-probes.md
Owning section: WP-13.03; explicit anchor: rule-wp-13.03.
Read the common context and WP13 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-13); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-13-04"></a>
#### 112. 13.04 — Evidence, licence positions and conclusions

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 13.04 — Evidence, licence positions and conclusions.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\13-high-risk-technical-probes.md
Owning section: WP-13.04; explicit anchor: rule-wp-13.04.
Read the common context and WP13 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-13); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-13-05"></a>
#### 113. 13.05 — Common ABI and deterministic failure surface

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 13.05 — Common ABI and deterministic failure surface.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\13-high-risk-technical-probes.md
Owning section: WP-13.05; explicit anchor: rule-wp-13.05.
Read the common context and WP13 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-13); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-13-06"></a>
#### 114. 13.06 — Media reader, probe, frame and seek

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 13.06 — Media reader, probe, frame and seek.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\13-high-risk-technical-probes.md
Owning section: WP-13.06; explicit anchor: rule-wp-13.06.
Read the common context and WP13 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-13); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-13-07"></a>
#### 115. 13.07 — Convert, resample and media writer

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 13.07 — Convert, resample and media writer.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\13-high-risk-technical-probes.md
Owning section: WP-13.07; explicit anchor: rule-wp-13.07.
Read the common context and WP13 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-13); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-13-08"></a>
#### 116. 13.08 — Audio devices

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 13.08 — Audio devices.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\13-high-risk-technical-probes.md
Owning section: WP-13.08; explicit anchor: rule-wp-13.08.
Read the common context and WP13 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-13); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-13-09"></a>
#### 117. 13.09 — Colour transforms

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 13.09 — Colour transforms.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\13-high-risk-technical-probes.md
Owning section: WP-13.09; explicit anchor: rule-wp-13.09.
Read the common context and WP13 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-13); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-13-10"></a>
#### 118. 13.10 — Still-image codecs

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 13.10 — Still-image codecs.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\13-high-risk-technical-probes.md
Owning section: WP-13.10; explicit anchor: rule-wp-13.10.
Read the common context and WP13 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-13); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-13-11"></a>
#### 119. 13.11 — OTIO interchange

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 13.11 — OTIO interchange.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\13-high-risk-technical-probes.md
Owning section: WP-13.11; explicit anchor: rule-wp-13.11.
Read the common context and WP13 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-13); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-13-12"></a>
#### 120. 13.12 — Serial and USB instruments

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 13.12 — Serial and USB instruments.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\13-high-risk-technical-probes.md
Owning section: WP-13.12; explicit anchor: rule-wp-13.12.
Read the common context and WP13 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-13); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-13-13"></a>
#### 121. 13.13 — PDF and production parser containment

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 13.13 — PDF and production parser containment.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\13-high-risk-technical-probes.md
Owning section: WP-13.13; explicit anchor: rule-wp-13.13.
Read the common context and WP13 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-13); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-13-14"></a>
#### 122. 13.14 — Portable graphics and optional OS backends

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 13.14 — Portable graphics and optional OS backends.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\13-high-risk-technical-probes.md
Owning section: WP-13.14; explicit anchor: rule-wp-13.14.
Read the common context and WP13 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-13); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-13-15"></a>
#### 123. 13.15 — Immutable native package production

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 13.15 — Immutable native package production.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\13-high-risk-technical-probes.md
Owning section: WP-13.15; explicit anchor: rule-wp-13.15.
Read the common context and WP13 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-13); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-13-16"></a>
#### 124. 13.16 — Dependency adoption and hardware receipts

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 13.16 — Dependency adoption and hardware receipts.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\13-high-risk-technical-probes.md
Owning section: WP-13.16; explicit anchor: rule-wp-13.16.
Read the common context and WP13 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-13); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-13-90"></a>
#### 125. 13.90 — Verify the owned artifact and real integration

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 13.90 — Verify the owned artifact and real integration.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\13-high-risk-technical-probes.md
Owning section: WP-13.90; explicit anchor: rule-wp-13.90.
Read the common context and WP13 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-13); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="wp-14"></a>
### WP-14 — Independent Application Composition and Typed Host Ports

Full WP: [formal source](<C:/MyFile/Projects/ArcForges-Design/docs/planning/work-packages/14-hub-and-minimal-provider-slice.md>). Reading context: [WP14](reading-map.md#wp-14).

Direct upstream WPs: 08, 09, 10, 11, 13. Compose an independent application using typed host ports and package-only mechanisms. Keep minimal ArcNotes owner behavior in ArcNotes.

<a id="substep-14-00"></a>
#### 126. 14.00 — Application scope and host ports

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 14.00 — Application scope and host ports.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\14-hub-and-minimal-provider-slice.md
Owning section: WP-14.00; explicit anchor: rule-wp-14.00.
Read the common context and WP14 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-14); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-14-01"></a>
#### 127. 14.01 — Minimal ArcNotes application services

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 14.01 — Minimal ArcNotes application services.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\14-hub-and-minimal-provider-slice.md
Owning section: WP-14.01; explicit anchor: rule-wp-14.01.
Read the common context and WP14 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-14); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-14-02"></a>
#### 128. 14.02 — Package consumer composition

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 14.02 — Package consumer composition.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\14-hub-and-minimal-provider-slice.md
Owning section: WP-14.02; explicit anchor: rule-wp-14.02.
Read the common context and WP14 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-14); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-14-03"></a>
#### 129. 14.03 — Idempotency and revision

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 14.03 — Idempotency and revision.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\14-hub-and-minimal-provider-slice.md
Owning section: WP-14.03; explicit anchor: rule-wp-14.03.
Read the common context and WP14 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-14); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-14-04"></a>
#### 130. 14.04 — Approval at the owner

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 14.04 — Approval at the owner.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\14-hub-and-minimal-provider-slice.md
Owning section: WP-14.04; explicit anchor: rule-wp-14.04.
Read the common context and WP14 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-14); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-14-05"></a>
#### 131. 14.05 — Context and artifact integration

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 14.05 — Context and artifact integration.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\14-hub-and-minimal-provider-slice.md
Owning section: WP-14.05; explicit anchor: rule-wp-14.05.
Read the common context and WP14 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-14); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-14-06"></a>
#### 132. 14.06 — Independent lifecycle

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 14.06 — Independent lifecycle.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\14-hub-and-minimal-provider-slice.md
Owning section: WP-14.06; explicit anchor: rule-wp-14.06.
Read the common context and WP14 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-14); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-14-90"></a>
#### 133. 14.90 — Owned artifacts and real integration

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 14.90 — Owned artifacts and real integration.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\14-hub-and-minimal-provider-slice.md
Owning section: WP-14.90; explicit anchor: rule-wp-14.90.
Read the common context and WP14 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-14); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="wp-15"></a>
### WP-15 — Application Assistant Conversation, History and Project Packages

Full WP: [formal source](<C:/MyFile/Projects/ArcForges-Design/docs/planning/work-packages/15-arcchat-conversation-core.md>). Reading context: [WP15](reading-map.md#wp-15).

Direct upstream WPs: 14. Produce isolated per-application assistant history/core packages and exact SQLite/history behavior. Export client fixtures are replaced by actual Cloud owners at WP25.08.

<a id="substep-15-00"></a>
#### 134. 15.00 — Single application history store

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 15.00 — Single application history store.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\15-arcchat-conversation-core.md
Owning section: WP-15.00; explicit anchor: rule-wp-15.00.
Read the common context and WP15 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-15); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-15-01"></a>
#### 135. 15.01 — Branches and window drafts

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 15.01 — Branches and window drafts.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\15-arcchat-conversation-core.md
Owning section: WP-15.01; explicit anchor: rule-wp-15.01.
Read the common context and WP15 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-15); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-15-02"></a>
#### 136. 15.02 — Attachments and provenance

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 15.02 — Attachments and provenance.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\15-arcchat-conversation-core.md
Owning section: WP-15.02; explicit anchor: rule-wp-15.02.
Read the common context and WP15 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-15); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-15-03"></a>
#### 137. 15.03 — Projects and profiles

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 15.03 — Projects and profiles.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\15-arcchat-conversation-core.md
Owning section: WP-15.03; explicit anchor: rule-wp-15.03.
Read the common context and WP15 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-15); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-15-04"></a>
#### 138. 15.04 — Skills

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 15.04 — Skills.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\15-arcchat-conversation-core.md
Owning section: WP-15.04; explicit anchor: rule-wp-15.04.
Read the common context and WP15 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-15); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-15-05"></a>
#### 139. 15.05 — Local search

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 15.05 — Local search.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\15-arcchat-conversation-core.md
Owning section: WP-15.05; explicit anchor: rule-wp-15.05.
Read the common context and WP15 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-15); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-15-06"></a>
#### 140. 15.06 — Local history export and import

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 15.06 — Local history export and import.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\15-arcchat-conversation-core.md
Owning section: WP-15.06; explicit anchor: rule-wp-15.06.
Read the common context and WP15 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-15); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-15-07"></a>
#### 141. 15.07 — Reference and package proof

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 15.07 — Reference and package proof.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\15-arcchat-conversation-core.md
Owning section: WP-15.07; explicit anchor: rule-wp-15.07.
Read the common context and WP15 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-15); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-15-90"></a>
#### 142. 15.90 — Owned artifacts and real integration

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 15.90 — Owned artifacts and real integration.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\15-arcchat-conversation-core.md
Owning section: WP-15.90; explicit anchor: rule-wp-15.90.
Read the common context and WP15 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-15); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="wp-16"></a>
### WP-16 — Unified Execution Engine

Full WP: [formal source](<C:/MyFile/Projects/ArcForges-Design/docs/planning/work-packages/16-unified-execution-engine.md>). Reading context: [WP16](reading-map.md#wp-16).

Direct upstream WPs: 09, 11, 14. Implement the device/product execution chain, command recovery and security. The sole Cloud model/tool loop remains WP52.

<a id="substep-16-00"></a>
#### 143. 16.00 — The execution chain and its persistence

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 16.00 — The execution chain and its persistence.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\16-unified-execution-engine.md
Owning section: WP-16.00; explicit anchor: rule-wp-16.00.
Read the common context and WP16 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-16); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-16-01"></a>
#### 144. 16.01 — Lifecycle states and reason facets

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 16.01 — Lifecycle states and reason facets.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\16-unified-execution-engine.md
Owning section: WP-16.01; explicit anchor: rule-wp-16.01.
Read the common context and WP16 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-16); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-16-02"></a>
#### 145. 16.02 — Failure classification and retry

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 16.02 — Failure classification and retry.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\16-unified-execution-engine.md
Owning section: WP-16.02; explicit anchor: rule-wp-16.02.
Read the common context and WP16 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-16); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-16-03"></a>
#### 146. 16.03 — Child tasks and ownership

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 16.03 — Child tasks and ownership.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\16-unified-execution-engine.md
Owning section: WP-16.03; explicit anchor: rule-wp-16.03.
Read the common context and WP16 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-16); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-16-04"></a>
#### 147. 16.04 — Checkpoints and compensation

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 16.04 — Checkpoints and compensation.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\16-unified-execution-engine.md
Owning section: WP-16.04; explicit anchor: rule-wp-16.04.
Read the common context and WP16 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-16); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-16-05"></a>
#### 148. 16.05 — Approval, steering and budget integration

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 16.05 — Approval, steering and budget integration.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\16-unified-execution-engine.md
Owning section: WP-16.05; explicit anchor: rule-wp-16.05.
Read the common context and WP16 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-16); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-16-06"></a>
#### 149. 16.06 — Progress, outcome and trace

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 16.06 — Progress, outcome and trace.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\16-unified-execution-engine.md
Owning section: WP-16.06; explicit anchor: rule-wp-16.06.
Read the common context and WP16 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-16); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-16-07"></a>
#### 150. 16.07 — Concurrency, loops and storms

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 16.07 — Concurrency, loops and storms.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\16-unified-execution-engine.md
Owning section: WP-16.07; explicit anchor: rule-wp-16.07.
Read the common context and WP16 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-16); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-16-90"></a>
#### 151. 16.90 — Verify the owned artifact and real integration

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 16.90 — Verify the owned artifact and real integration.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\16-unified-execution-engine.md
Owning section: WP-16.90; explicit anchor: rule-wp-16.90.
Read the common context and WP16 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-16); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="wp-17"></a>
### WP-17 — Complete Embedded Assistant and Cloud Client Surface

Full WP: [formal source](<C:/MyFile/Projects/ArcForges-Design/docs/planning/work-packages/17-arcchat-independent-core.md>). Reading context: [WP17](reading-map.md#wp-17).

Direct upstream WPs: 06, 15, 16. Complete embedded assistant navigation, interactions and client mechanisms. Explicit future Cloud/automation/AI fixtures are allowed only until their named real producers, including WP52.06.

<a id="substep-17-00"></a>
#### 152. 17.00 — Complete assistant navigation

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 17.00 — Complete assistant navigation.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\17-arcchat-independent-core.md
Owning section: WP-17.00; explicit anchor: rule-wp-17.00.
Read the common context and WP17 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-17); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-17-01"></a>
#### 153. 17.01 — Cloud client and device runtime

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 17.01 — Cloud client and device runtime.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\17-arcchat-independent-core.md
Owning section: WP-17.01; explicit anchor: rule-wp-17.01.
Read the common context and WP17 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-17); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-17-02"></a>
#### 154. 17.02 — Security and approval surface

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 17.02 — Security and approval surface.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\17-arcchat-independent-core.md
Owning section: WP-17.02; explicit anchor: rule-wp-17.02.
Read the common context and WP17 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-17); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-17-03"></a>
#### 155. 17.03 — Task centre

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 17.03 — Task centre.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\17-arcchat-independent-core.md
Owning section: WP-17.03; explicit anchor: rule-wp-17.03.
Read the common context and WP17 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-17); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-17-04"></a>
#### 156. 17.04 — Automation client

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 17.04 — Automation client.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\17-arcchat-independent-core.md
Owning section: WP-17.04; explicit anchor: rule-wp-17.04.
Read the common context and WP17 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-17); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-17-05"></a>
#### 157. 17.05 — History and AI admission

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 17.05 — History and AI admission.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\17-arcchat-independent-core.md
Owning section: WP-17.05; explicit anchor: rule-wp-17.05.
Read the common context and WP17 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-17); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-17-06"></a>
#### 158. 17.06 — Preview and host context

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 17.06 — Preview and host context.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\17-arcchat-independent-core.md
Owning section: WP-17.06; explicit anchor: rule-wp-17.06.
Read the common context and WP17 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-17); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-17-07"></a>
#### 159. 17.07 — Complete package acceptance

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 17.07 — Complete package acceptance.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\17-arcchat-independent-core.md
Owning section: WP-17.07; explicit anchor: rule-wp-17.07.
Read the common context and WP17 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-17); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-17-90"></a>
#### 160. 17.90 — Owned artifacts and real integration

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 17.90 — Owned artifacts and real integration.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\17-arcchat-independent-core.md
Owning section: WP-17.90; explicit anchor: rule-wp-17.90.
Read the common context and WP17 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-17); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="wp-18"></a>
### WP-18 — ArcNotes Document Core

Full WP: [formal source](<C:/MyFile/Projects/ArcForges-Design/docs/planning/work-packages/18-arcnotes-document-core.md>). Reading context: [WP18](reading-map.md#wp-18).

Direct upstream WPs: 07, 10, 14. Implement accepted Notes document/editor behavior, stable text/cell identity, IME, undo, containment and recovery; consume the existing reference matrix and original implementation boundaries.

<a id="substep-18-00"></a>
#### 161. 18.00 — Block document model

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 18.00 — Block document model.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\18-arcnotes-document-core.md
Owning section: WP-18.00; explicit anchor: rule-wp-18.00.
Read the common context and WP18 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-18); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-18-01"></a>
#### 162. 18.01 — Editor interaction

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 18.01 — Editor interaction.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\18-arcnotes-document-core.md
Owning section: WP-18.01; explicit anchor: rule-wp-18.01.
Read the common context and WP18 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-18); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-18-02"></a>
#### 163. 18.02 — Links, backlinks and outline

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 18.02 — Links, backlinks and outline.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\18-arcnotes-document-core.md
Owning section: WP-18.02; explicit anchor: rule-wp-18.02.
Read the common context and WP18 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-18); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-18-03"></a>
#### 164. 18.03 — Properties and tags

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 18.03 — Properties and tags.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\18-arcnotes-document-core.md
Owning section: WP-18.03; explicit anchor: rule-wp-18.03.
Read the common context and WP18 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-18); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-18-04"></a>
#### 165. 18.04 — Attachments

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 18.04 — Attachments.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\18-arcnotes-document-core.md
Owning section: WP-18.04; explicit anchor: rule-wp-18.04.
Read the common context and WP18 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-18); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-18-05"></a>
#### 166. 18.05 — Undo, history, checkpoint and trash

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 18.05 — Undo, history, checkpoint and trash.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\18-arcnotes-document-core.md
Owning section: WP-18.05; explicit anchor: rule-wp-18.05.
Read the common context and WP18 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-18); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-18-06"></a>
#### 167. 18.06 — Recovery and migration

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 18.06 — Recovery and migration.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\18-arcnotes-document-core.md
Owning section: WP-18.06; explicit anchor: rule-wp-18.06.
Read the common context and WP18 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-18); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-18-07"></a>
#### 168. 18.07 — Capability surface

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 18.07 — Capability surface.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\18-arcnotes-document-core.md
Owning section: WP-18.07; explicit anchor: rule-wp-18.07.
Read the common context and WP18 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-18); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-18-08"></a>
#### 169. 18.08 — Reference drift check

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 18.08 — Reference drift check.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\18-arcnotes-document-core.md
Owning section: WP-18.08; explicit anchor: rule-wp-18.08.
Read the common context and WP18 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-18); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-18-90"></a>
#### 170. 18.90 — Verify the owned artifact and real integration

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 18.90 — Verify the owned artifact and real integration.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\18-arcnotes-document-core.md
Owning section: WP-18.90; explicit anchor: rule-wp-18.90.
Read the common context and WP18 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-18); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="wp-19"></a>
### WP-19 — ArcNotes Search, Import, Export and Portability

Full WP: [formal source](<C:/MyFile/Projects/ArcForges-Design/docs/planning/work-packages/19-arcnotes-search-and-portability.md>). Reading context: [WP19](reading-map.md#wp-19).

Direct upstream WPs: 18. Implement local Notes search and portability. Distinguish local/client fixture acceptance from actual Cloud export production at WP25.08.

<a id="substep-19-00"></a>
#### 171. 19.00 — Local full-text index

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 19.00 — Local full-text index.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\19-arcnotes-search-and-portability.md
Owning section: WP-19.00; explicit anchor: rule-wp-19.00.
Read the common context and WP19 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-19); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-19-01"></a>
#### 172. 19.01 — Query, ranking and permission

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 19.01 — Query, ranking and permission.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\19-arcnotes-search-and-portability.md
Owning section: WP-19.01; explicit anchor: rule-wp-19.01.
Read the common context and WP19 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-19); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-19-02"></a>
#### 173. 19.02 — Citation anchors

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 19.02 — Citation anchors.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\19-arcnotes-search-and-portability.md
Owning section: WP-19.02; explicit anchor: rule-wp-19.02.
Read the common context and WP19 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-19); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-19-03"></a>
#### 174. 19.03 — Saved views

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 19.03 — Saved views.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\19-arcnotes-search-and-portability.md
Owning section: WP-19.03; explicit anchor: rule-wp-19.03.
Read the common context and WP19 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-19); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-19-04"></a>
#### 175. 19.04 — Non-destructive import

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 19.04 — Non-destructive import.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\19-arcnotes-search-and-portability.md
Owning section: WP-19.04; explicit anchor: rule-wp-19.04.
Read the common context and WP19 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-19); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-19-05"></a>
#### 176. 19.05 — Owner-specific portability

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 19.05 — Owner-specific portability.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\19-arcnotes-search-and-portability.md
Owning section: WP-19.05; explicit anchor: rule-wp-19.05.
Read the common context and WP19 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-19); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-19-06"></a>
#### 177. 19.06 — The repository-projection prohibition

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 19.06 — The repository-projection prohibition.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\19-arcnotes-search-and-portability.md
Owning section: WP-19.06; explicit anchor: rule-wp-19.06.
Read the common context and WP19 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-19); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-19-90"></a>
#### 178. 19.90 — Verify the owned artifact and real integration

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 19.90 — Verify the owned artifact and real integration.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\19-arcnotes-search-and-portability.md
Owning section: WP-19.90; explicit anchor: rule-wp-19.90.
Read the common context and WP19 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-19); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="wp-21"></a>
### WP-21 — Cloudflare Container, D1 Authority and Binding Plans

Full WP: [formal source](<C:/MyFile/Projects/ArcForges-Design/docs/planning/work-packages/21-cloud-host-and-persistence.md>). Reading context: [WP21](reading-map.md#wp-21).

Direct upstream WPs: 03, 05, 12. Produce the real Container/Worker/D1 plan bridge, migration, receipts, fenced jobs and selfhost profile. Its integration manifest is progressive; future business owners remain pending.

<a id="substep-21-00"></a>
#### 179. 21.00 — Ingress and host pipeline

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 21.00 — Ingress and host pipeline.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\21-cloud-host-and-persistence.md
Owning section: WP-21.00; explicit anchor: rule-wp-21.00.
Read the common context and WP21 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-21); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-21-01"></a>
#### 180. 21.01 — Finite durable jobs

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 21.01 — Finite durable jobs.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\21-cloud-host-and-persistence.md
Owning section: WP-21.01; explicit anchor: rule-wp-21.01.
Read the common context and WP21 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-21); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-21-02"></a>
#### 181. 21.02 — Twenty-one module boundaries

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 21.02 — Twenty-one module boundaries.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\21-cloud-host-and-persistence.md
Owning section: WP-21.02; explicit anchor: rule-wp-21.02.
Read the common context and WP21 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-21); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-21-03"></a>
#### 182. 21.03 — D1 migration and exact physical mapping

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 21.03 — D1 migration and exact physical mapping.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\21-cloud-host-and-persistence.md
Owning section: WP-21.03; explicit anchor: rule-wp-21.03.
Read the common context and WP21 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-21); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-21-04"></a>
#### 183. 21.04 — Receipts/outbox/archive

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 21.04 — Receipts/outbox/archive.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\21-cloud-host-and-persistence.md
Owning section: WP-21.04; explicit anchor: rule-wp-21.04.
Read the common context and WP21 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-21); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-21-05"></a>
#### 184. 21.05 — Shared atomic families and claims

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 21.05 — Shared atomic families and claims.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\21-cloud-host-and-persistence.md
Owning section: WP-21.05; explicit anchor: rule-wp-21.05.
Read the common context and WP21 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-21); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-21-06"></a>
#### 185. 21.06 — Capacity and Container/D1 integration producer

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 21.06 — Capacity and Container/D1 integration producer.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\21-cloud-host-and-persistence.md
Owning section: WP-21.06; explicit anchor: rule-wp-21.06.
Read the common context and WP21 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-21); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-21-07"></a>
#### 186. 21.07 — Failure isolation and readiness

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 21.07 — Failure isolation and readiness.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\21-cloud-host-and-persistence.md
Owning section: WP-21.07; explicit anchor: rule-wp-21.07.
Read the common context and WP21 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-21); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-21-08"></a>
#### 187. 21.08 — Selfhost.v1 deployment profile

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 21.08 — Selfhost.v1 deployment profile.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\21-cloud-host-and-persistence.md
Owning section: WP-21.08; explicit anchor: rule-wp-21.08.
Read the common context and WP21 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-21); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-21-90"></a>
#### 188. 21.90 — Owned artifacts and real integration

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 21.90 — Owned artifacts and real integration.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\21-cloud-host-and-persistence.md
Owning section: WP-21.90; explicit anchor: rule-wp-21.90.
Read the common context and WP21 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-21); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="wp-22"></a>
### WP-22 — Identity, Workspace, Device and Session

Full WP: [formal source](<C:/MyFile/Projects/ArcForges-Design/docs/planning/work-packages/22-identity-workspace-and-device.md>). Reading context: [WP22](reading-map.md#wp-22).

Direct upstream WPs: 11, 21. Produce real identity/session/browser-ceremony and mail paths with per-application isolation. Current P2-014 excludes sibling Device SSO. Later portal UI is not an authentication-producer prerequisite.

<a id="substep-22-00"></a>
#### 189. 22.00 — Core identity model

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 22.00 — Core identity model.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\22-identity-workspace-and-device.md
Owning section: WP-22.00; explicit anchor: rule-wp-22.00.
Read the common context and WP22 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-22); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-22-01"></a>
#### 190. 22.01 — Native and browser authentication with real mail

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 22.01 — Native and browser authentication with real mail.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\22-identity-workspace-and-device.md
Owning section: WP-22.01; explicit anchor: rule-wp-22.01.
Read the common context and WP22 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-22); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-22-02"></a>
#### 191. 22.02 — Device, installation, instance and session

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 22.02 — Device, installation, instance and session.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\22-identity-workspace-and-device.md
Owning section: WP-22.02; explicit anchor: rule-wp-22.02.
Read the common context and WP22 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-22); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-22-03"></a>
#### 192. 22.03 — Device trust and remote gating

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 22.03 — Device trust and remote gating.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\22-identity-workspace-and-device.md
Owning section: WP-22.03; explicit anchor: rule-wp-22.03.
Read the common context and WP22 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-22); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-22-04"></a>
#### 193. 22.04 — Step-up and sensitive operations

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 22.04 — Step-up and sensitive operations.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\22-identity-workspace-and-device.md
Owning section: WP-22.04; explicit anchor: rule-wp-22.04.
Read the common context and WP22 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-22); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-22-05"></a>
#### 194. 22.05 — PAT and actor authorization

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 22.05 — PAT and actor authorization.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\22-identity-workspace-and-device.md
Owning section: WP-22.05; explicit anchor: rule-wp-22.05.
Read the common context and WP22 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-22); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-22-06"></a>
#### 195. 22.06 — Recovery, account states and deletion

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 22.06 — Recovery, account states and deletion.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\22-identity-workspace-and-device.md
Owning section: WP-22.06; explicit anchor: rule-wp-22.06.
Read the common context and WP22 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-22); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-22-07"></a>
#### 196. 22.07 — Independent native session integration

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 22.07 — Independent native session integration.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\22-identity-workspace-and-device.md
Owning section: WP-22.07; explicit anchor: rule-wp-22.07.
Read the common context and WP22 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-22); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-22-08"></a>
#### 197. 22.08 — Browser cookie-session adapter

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 22.08 — Browser cookie-session adapter.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\22-identity-workspace-and-device.md
Owning section: WP-22.08; explicit anchor: rule-wp-22.08.
Read the common context and WP22 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-22); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-22-90"></a>
#### 198. 22.90 — Verify the owned artifact and real integration

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 22.90 — Verify the owned artifact and real integration.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\22-identity-workspace-and-device.md
Owning section: WP-22.90; explicit anchor: rule-wp-22.90.
Read the common context and WP22 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-22); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="wp-23"></a>
### WP-23 — Public Proto APIs and Generated Clients

Full WP: [formal source](<C:/MyFile/Projects/ArcForges-Design/docs/planning/work-packages/23-public-api-and-generated-clients.md>). Reading context: [WP23](reading-map.md#wp-23).

Direct upstream WPs: 03, 22. Generate/register the complete public contract surface and prove real identity/transport behavior. Future owner fixtures are explicitly replaced at WP25/42/40/51/52; the Android WP06 probe suffices here.

<a id="substep-23-00"></a>
#### 199. 23.00 — Endpoint mapping and validation

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 23.00 — Endpoint mapping and validation.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\23-public-api-and-generated-clients.md
Owning section: WP-23.00; explicit anchor: rule-wp-23.00.
Read the common context and WP23 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-23); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-23-01"></a>
#### 200. 23.01 — Typed protocol and error mapping

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 23.01 — Typed protocol and error mapping.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\23-public-api-and-generated-clients.md
Owning section: WP-23.01; explicit anchor: rule-wp-23.01.
Read the common context and WP23 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-23); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-23-02"></a>
#### 201. 23.02 — Typed queries and revision preconditions

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 23.02 — Typed queries and revision preconditions.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\23-public-api-and-generated-clients.md
Owning section: WP-23.02; explicit anchor: rule-wp-23.02.
Read the common context and WP23 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-23); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-23-03"></a>
#### 202. 23.03 — Idempotency and rate limiting

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 23.03 — Idempotency and rate limiting.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\23-public-api-and-generated-clients.md
Owning section: WP-23.03; explicit anchor: rule-wp-23.03.
Read the common context and WP23 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-23); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-23-04"></a>
#### 203. 23.04 — Resource transport and future-owner boundary

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 23.04 — Resource transport and future-owner boundary.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\23-public-api-and-generated-clients.md
Owning section: WP-23.04; explicit anchor: rule-wp-23.04.
Read the common context and WP23 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-23); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-23-05"></a>
#### 204. 23.05 — Generated C#/TypeScript/Kotlin clients

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 23.05 — Generated C#/TypeScript/Kotlin clients.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\23-public-api-and-generated-clients.md
Owning section: WP-23.05; explicit anchor: rule-wp-23.05.
Read the common context and WP23 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-23); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-23-06"></a>
#### 205. 23.06 — Compatibility window

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 23.06 — Compatibility window.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\23-public-api-and-generated-clients.md
Owning section: WP-23.06; explicit anchor: rule-wp-23.06.
Read the common context and WP23 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-23); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-23-90"></a>
#### 206. 23.90 — Verify the owned artifact and real integration

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 23.90 — Verify the owned artifact and real integration.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\23-public-api-and-generated-clients.md
Owning section: WP-23.90; explicit anchor: rule-wp-23.90.
Read the common context and WP23 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-23); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="wp-24"></a>
### WP-24 — gRPC-Web Streams and Durable Event Recovery

Full WP: [formal source](<C:/MyFile/Projects/ArcForges-Design/docs/planning/work-packages/24-realtime-and-reliable-events.md>). Reading context: [WP24](reading-map.md#wp-24).

Direct upstream WPs: 23. Produce bounded stream/hint delivery and durable cursor/unary recovery. Hints are not business authority; final Task/Harness content is integrated at WP52.

<a id="substep-24-00"></a>
#### 207. 24.00 — Connection and authentication

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 24.00 — Connection and authentication.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\24-realtime-and-reliable-events.md
Owning section: WP-24.00; explicit anchor: rule-wp-24.00.
Read the common context and WP24 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-24); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-24-01"></a>
#### 208. 24.01 — Scoped subscription

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 24.01 — Scoped subscription.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\24-realtime-and-reliable-events.md
Owning section: WP-24.01; explicit anchor: rule-wp-24.01.
Read the common context and WP24 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-24); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-24-02"></a>
#### 209. 24.02 — Cursor and gap handling

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 24.02 — Cursor and gap handling.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\24-realtime-and-reliable-events.md
Owning section: WP-24.02; explicit anchor: rule-wp-24.02.
Read the common context and WP24 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-24); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-24-03"></a>
#### 210. 24.03 — Durable unary fallback

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 24.03 — Durable unary fallback.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\24-realtime-and-reliable-events.md
Owning section: WP-24.03; explicit anchor: rule-wp-24.03.
Read the common context and WP24 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-24); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-24-04"></a>
#### 211. 24.04 — Publication and wake

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 24.04 — Publication and wake.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\24-realtime-and-reliable-events.md
Owning section: WP-24.04; explicit anchor: rule-wp-24.04.
Read the common context and WP24 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-24); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-24-05"></a>
#### 212. 24.05 — Bounded lifecycle

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 24.05 — Bounded lifecycle.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\24-realtime-and-reliable-events.md
Owning section: WP-24.05; explicit anchor: rule-wp-24.05.
Read the common context and WP24 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-24); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-24-06"></a>
#### 213. 24.06 — Reusable consumer adapters

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 24.06 — Reusable consumer adapters.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\24-realtime-and-reliable-events.md
Owning section: WP-24.06; explicit anchor: rule-wp-24.06.
Read the common context and WP24 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-24); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-24-90"></a>
#### 214. 24.90 — Owned artifacts and real integration

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 24.90 — Owned artifacts and real integration.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\24-realtime-and-reliable-events.md
Owning section: WP-24.90; explicit anchor: rule-wp-24.90.
Read the common context and WP24 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-24); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="wp-25"></a>
### WP-25 — Sync Engine and Blob Lifecycle

Full WP: [formal source](<C:/MyFile/Projects/ArcForges-Design/docs/planning/work-packages/25-sync-engine-and-blob-lifecycle.md>). Reading context: [WP25](reading-map.md#wp-25).

Direct upstream WPs: 19, 24. Complete actual R2 lifecycle and Cloud Notes/Chat authority, history import/export, sync and conflicts. Client fixtures from WP15/19 are replaced here.

<a id="substep-25-00"></a>
#### 215. 25.00 — Cloud Notes authority and sync scopes

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 25.00 — Cloud Notes authority and sync scopes.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\25-sync-engine-and-blob-lifecycle.md
Owning section: WP-25.00; explicit anchor: rule-wp-25.00.
Read the common context and WP25 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-25); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-25-01"></a>
#### 216. 25.01 — Pending batches and conflict lineage

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 25.01 — Pending batches and conflict lineage.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\25-sync-engine-and-blob-lifecycle.md
Owning section: WP-25.01; explicit anchor: rule-wp-25.01.
Read the common context and WP25 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-25); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-25-02"></a>
#### 217. 25.02 — Guarded publication and convergent bootstrap

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 25.02 — Guarded publication and convergent bootstrap.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\25-sync-engine-and-blob-lifecycle.md
Owning section: WP-25.02; explicit anchor: rule-wp-25.02.
Read the common context and WP25 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-25); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-25-03"></a>
#### 218. 25.03 — Conflict detection and policies

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 25.03 — Conflict detection and policies.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\25-sync-engine-and-blob-lifecycle.md
Owning section: WP-25.03; explicit anchor: rule-wp-25.03.
Read the common context and WP25 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-25); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-25-04"></a>
#### 219. 25.04 — Deletion and tombstones

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 25.04 — Deletion and tombstones.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\25-sync-engine-and-blob-lifecycle.md
Owning section: WP-25.04; explicit anchor: rule-wp-25.04.
Read the common context and WP25 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-25); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-25-05"></a>
#### 220. 25.05 — Blob lifecycle

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 25.05 — Blob lifecycle.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\25-sync-engine-and-blob-lifecycle.md
Owning section: WP-25.05; explicit anchor: rule-wp-25.05.
Read the common context and WP25 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-25); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-25-06"></a>
#### 221. 25.06 — Availability, protection and data health

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 25.06 — Availability, protection and data health.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\25-sync-engine-and-blob-lifecycle.md
Owning section: WP-25.06; explicit anchor: rule-wp-25.06.
Read the common context and WP25 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-25); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-25-07"></a>
#### 222. 25.07 — Multi-device convergence

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 25.07 — Multi-device convergence.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\25-sync-engine-and-blob-lifecycle.md
Owning section: WP-25.07; explicit anchor: rule-wp-25.07.
Read the common context and WP25 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-25); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-25-08"></a>
#### 223. 25.08 — Real Cloud Notes and Chat export producers

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 25.08 — Real Cloud Notes and Chat export producers.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\25-sync-engine-and-blob-lifecycle.md
Owning section: WP-25.08; explicit anchor: rule-wp-25.08.
Read the common context and WP25 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-25); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-25-09"></a>
#### 224. 25.09 — Application Cloud history and restartable import

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 25.09 — Application Cloud history and restartable import.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\25-sync-engine-and-blob-lifecycle.md
Owning section: WP-25.09; explicit anchor: rule-wp-25.09.
Read the common context and WP25 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-25); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-25-90"></a>
#### 225. 25.90 — Verify the owned artifact and real integration

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 25.90 — Verify the owned artifact and real integration.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\25-sync-engine-and-blob-lifecycle.md
Owning section: WP-25.90; explicit anchor: rule-wp-25.90.
Read the common context and WP25 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-25); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="wp-26"></a>
### WP-26 — Application Presence and One-Application Tool Bridge

Full WP: [formal source](<C:/MyFile/Projects/ArcForges-Design/docs/planning/work-packages/26-remote-action-and-tool-bridge.md>). Reading context: [WP26](reading-map.md#wp-26).

Direct upstream WPs: 17, 24, 25. Implement presence and a durable one-application device bridge with owner reauthorization, deduplication and unknown-effect reconciliation; real model-driven orchestration closes at WP52.

<a id="substep-26-00"></a>
#### 226. 26.00 — Application presence

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 26.00 — Application presence.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\26-remote-action-and-tool-bridge.md
Owning section: WP-26.00; explicit anchor: rule-wp-26.00.
Read the common context and WP26 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-26); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-26-01"></a>
#### 227. 26.01 — Durable target queue

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 26.01 — Durable target queue.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\26-remote-action-and-tool-bridge.md
Owning section: WP-26.01; explicit anchor: rule-wp-26.01.
Read the common context and WP26 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-26); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-26-02"></a>
#### 228. 26.02 — Owner reauthorization

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 26.02 — Owner reauthorization.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\26-remote-action-and-tool-bridge.md
Owning section: WP-26.02; explicit anchor: rule-wp-26.02.
Read the common context and WP26 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-26); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-26-03"></a>
#### 229. 26.03 — Execution and exact result deduplication

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 26.03 — Execution and exact result deduplication.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\26-remote-action-and-tool-bridge.md
Owning section: WP-26.03; explicit anchor: rule-wp-26.03.
Read the common context and WP26 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-26); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-26-04"></a>
#### 230. 26.04 — Remote approval and steering

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 26.04 — Remote approval and steering.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\26-remote-action-and-tool-bridge.md
Owning section: WP-26.04; explicit anchor: rule-wp-26.04.
Read the common context and WP26 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-26); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-26-05"></a>
#### 231. 26.05 — Offline expiry and recovery

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 26.05 — Offline expiry and recovery.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\26-remote-action-and-tool-bridge.md
Owning section: WP-26.05; explicit anchor: rule-wp-26.05.
Read the common context and WP26 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-26); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-26-06"></a>
#### 232. 26.06 — Frozen application locality

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 26.06 — Frozen application locality.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\26-remote-action-and-tool-bridge.md
Owning section: WP-26.06; explicit anchor: rule-wp-26.06.
Read the common context and WP26 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-26); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-26-90"></a>
#### 233. 26.90 — Owned artifacts and real integration

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 26.90 — Owned artifacts and real integration.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\26-remote-action-and-tool-bridge.md
Owning section: WP-26.90; explicit anchor: rule-wp-26.90.
Read the common context and WP26 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-26); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="wp-28"></a>
### WP-28 — ArcNotes Bounded Properties and Saved Views

Full WP: [formal source](<C:/MyFile/Projects/ArcForges-Design/docs/planning/work-packages/28-arcnotes-properties-and-views.md>). Reading context: [WP28](reading-map.md#wp-28).

Direct upstream WPs: 19, 25. Complete Notes typed properties, scalar queries and views using real Cloud owner behavior, preserving existing light scope and import/export fidelity.

<a id="substep-28-00"></a>
#### 234. 28.00 — Typed property schemas

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 28.00 — Typed property schemas.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\28-arcnotes-properties-and-views.md
Owning section: WP-28.00; explicit anchor: rule-wp-28.00.
Read the common context and WP28 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-28); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-28-01"></a>
#### 235. 28.01 — Query model

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 28.01 — Query model.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\28-arcnotes-properties-and-views.md
Owning section: WP-28.01; explicit anchor: rule-wp-28.01.
Read the common context and WP28 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-28); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-28-02"></a>
#### 236. 28.02 — View kinds

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 28.02 — View kinds.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\28-arcnotes-properties-and-views.md
Owning section: WP-28.02; explicit anchor: rule-wp-28.02.
Read the common context and WP28 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-28); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-28-03"></a>
#### 237. 28.03 — Editing through a view

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 28.03 — Editing through a view.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\28-arcnotes-properties-and-views.md
Owning section: WP-28.03; explicit anchor: rule-wp-28.03.
Read the common context and WP28 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-28); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-28-04"></a>
#### 238. 28.04 — Lightness preservation

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 28.04 — Lightness preservation.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\28-arcnotes-properties-and-views.md
Owning section: WP-28.04; explicit anchor: rule-wp-28.04.
Read the common context and WP28 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-28); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-28-05"></a>
#### 239. 28.05 — Supported-schema migration and export fidelity

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 28.05 — Supported-schema migration and export fidelity.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\28-arcnotes-properties-and-views.md
Owning section: WP-28.05; explicit anchor: rule-wp-28.05.
Read the common context and WP28 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-28); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-28-06"></a>
#### 240. 28.06 — Scale

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 28.06 — Scale.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\28-arcnotes-properties-and-views.md
Owning section: WP-28.06; explicit anchor: rule-wp-28.06.
Read the common context and WP28 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-28); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-28-90"></a>
#### 241. 28.90 — Verify the owned artifact and real integration

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 28.90 — Verify the owned artifact and real integration.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\28-arcnotes-properties-and-views.md
Owning section: WP-28.90; explicit anchor: rule-wp-28.90.
Read the common context and WP28 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-28); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="wp-30"></a>
### WP-30 — Kotlin Android Foundation

Full WP: [formal source](<C:/MyFile/Projects/ArcForges-Design/docs/planning/work-packages/30-mobile-shared-architecture.md>). Reading context: [WP30](reading-map.md#wp-30).

Direct upstream WPs: 03, 06, 23, 24, 25. Produce Kotlin Android foundation, Room/security/OS adapters and package-only Maven clients against actual WP23–25. Task/AI fixtures are temporary until WP31/WP52.

<a id="substep-30-00"></a>
#### 242. 30.00 — Android repository identity and toolchain

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 30.00 — Android repository identity and toolchain.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\30-mobile-shared-architecture.md
Owning section: WP-30.00; explicit anchor: rule-wp-30.00.
Read the common context and WP30 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-30); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-30-01"></a>
#### 243. 30.01 — Native module and route boundaries

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 30.01 — Native module and route boundaries.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\30-mobile-shared-architecture.md
Owning section: WP-30.01; explicit anchor: rule-wp-30.01.
Read the common context and WP30 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-30); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-30-02"></a>
#### 244. 30.02 — Android runtime and OS adapters

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 30.02 — Android runtime and OS adapters.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\30-mobile-shared-architecture.md
Owning section: WP-30.02; explicit anchor: rule-wp-30.02.
Read the common context and WP30 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-30); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-30-03"></a>
#### 245. 30.03 — Published gRPC-Web contracts

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 30.03 — Published gRPC-Web contracts.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\30-mobile-shared-architecture.md
Owning section: WP-30.03; explicit anchor: rule-wp-30.03.
Read the common context and WP30 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-30); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-30-04"></a>
#### 246. 30.04 — Room history, drafts and receipts

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 30.04 — Room history, drafts and receipts.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\30-mobile-shared-architecture.md
Owning section: WP-30.04; explicit anchor: rule-wp-30.04.
Read the common context and WP30 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-30); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-30-05"></a>
#### 247. 30.05 — Secure lifecycle and permissions

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 30.05 — Secure lifecycle and permissions.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\30-mobile-shared-architecture.md
Owning section: WP-30.05; explicit anchor: rule-wp-30.05.
Read the common context and WP30 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-30); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-30-90"></a>
#### 248. 30.90 — Foundation integration evidence

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 30.90 — Foundation integration evidence.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\30-mobile-shared-architecture.md
Owning section: WP-30.90; explicit anchor: rule-wp-30.90.
Read the common context and WP30 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-30); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="wp-33"></a>
### WP-33 — ArcScope Acquisition and Session Core

Full WP: [formal source](<C:/MyFile/Projects/ArcForges-Design/docs/planning/work-packages/33-arcscope-acquisition-and-session.md>). Reading context: [WP33](reading-map.md#wp-33).

Direct upstream WPs: 07, 10, 13, 26. Implement real acquisition sources and durable capture/replay with source/framing/time/loss profiles. Synthetic data cannot close required hardware evidence.

<a id="substep-33-00"></a>
#### 249. 33.00 — Sources, adapters and profiles

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 33.00 — Sources, adapters and profiles.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\33-arcscope-acquisition-and-session.md
Owning section: WP-33.00; explicit anchor: rule-wp-33.00.
Read the common context and WP33 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-33); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-33-01"></a>
#### 250. 33.01 — Acquisition pipeline

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 33.01 — Acquisition pipeline.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\33-arcscope-acquisition-and-session.md
Owning section: WP-33.01; explicit anchor: rule-wp-33.01.
Read the common context and WP33 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-33); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-33-02"></a>
#### 251. 33.02 — Session, capture, segments and gaps

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 33.02 — Session, capture, segments and gaps.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\33-arcscope-acquisition-and-session.md
Owning section: WP-33.02; explicit anchor: rule-wp-33.02.
Read the common context and WP33 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-33); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-33-03"></a>
#### 252. 33.03 — Time and channel model

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 33.03 — Time and channel model.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\33-arcscope-acquisition-and-session.md
Owning section: WP-33.03; explicit anchor: rule-wp-33.03.
Read the common context and WP33 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-33); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-33-04"></a>
#### 253. 33.04 — Durable capture and immutability

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 33.04 — Durable capture and immutability.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\33-arcscope-acquisition-and-session.md
Owning section: WP-33.04; explicit anchor: rule-wp-33.04.
Read the common context and WP33 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-33); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-33-05"></a>
#### 254. 33.05 — Replay

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 33.05 — Replay.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\33-arcscope-acquisition-and-session.md
Owning section: WP-33.05; explicit anchor: rule-wp-33.05.
Read the common context and WP33 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-33); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-33-06"></a>
#### 255. 33.06 — Long-running capture in the shell

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 33.06 — Long-running capture in the shell.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\33-arcscope-acquisition-and-session.md
Owning section: WP-33.06; explicit anchor: rule-wp-33.06.
Read the common context and WP33 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-33); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-33-07"></a>
#### 256. 33.07 — Reference drift check

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 33.07 — Reference drift check.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\33-arcscope-acquisition-and-session.md
Owning section: WP-33.07; explicit anchor: rule-wp-33.07.
Read the common context and WP33 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-33); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-33-90"></a>
#### 257. 33.90 — Verify the owned artifact and real integration

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 33.90 — Verify the owned artifact and real integration.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\33-arcscope-acquisition-and-session.md
Owning section: WP-33.90; explicit anchor: rule-wp-33.90.
Read the common context and WP33 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-33); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="wp-34"></a>
### WP-34 — ArcScope Visualisation, Analysis and Reporting

Full WP: [formal source](<C:/MyFile/Projects/ArcForges-Design/docs/planning/work-packages/34-arcscope-analysis-and-reporting.md>). Reading context: [WP34](reading-map.md#wp-34).

Direct upstream WPs: 33. Implement Scope measurements, analyses, decoders, triggers and reports with independent numeric/gap vectors from the product behavior profiles.

<a id="substep-34-00"></a>
#### 258. 34.00 — Visualisation

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 34.00 — Visualisation.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\34-arcscope-analysis-and-reporting.md
Owning section: WP-34.00; explicit anchor: rule-wp-34.00.
Read the common context and WP34 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-34); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-34-01"></a>
#### 259. 34.01 — Triggers

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 34.01 — Triggers.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\34-arcscope-analysis-and-reporting.md
Owning section: WP-34.01; explicit anchor: rule-wp-34.01.
Read the common context and WP34 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-34); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-34-02"></a>
#### 260. 34.02 — Measurements

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 34.02 — Measurements.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\34-arcscope-analysis-and-reporting.md
Owning section: WP-34.02; explicit anchor: rule-wp-34.02.
Read the common context and WP34 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-34); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-34-03"></a>
#### 261. 34.03 — Decoders

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 34.03 — Decoders.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\34-arcscope-analysis-and-reporting.md
Owning section: WP-34.03; explicit anchor: rule-wp-34.03.
Read the common context and WP34 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-34); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-34-04"></a>
#### 262. 34.04 — Analysis and recipes

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 34.04 — Analysis and recipes.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\34-arcscope-analysis-and-reporting.md
Owning section: WP-34.04; explicit anchor: rule-wp-34.04.
Read the common context and WP34 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-34); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-34-05"></a>
#### 263. 34.05 — Annotations, findings and comparison

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 34.05 — Annotations, findings and comparison.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\34-arcscope-analysis-and-reporting.md
Owning section: WP-34.05; explicit anchor: rule-wp-34.05.
Read the common context and WP34 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-34); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-34-06"></a>
#### 264. 34.06 — Reports and reproducibility

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 34.06 — Reports and reproducibility.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\34-arcscope-analysis-and-reporting.md
Owning section: WP-34.06; explicit anchor: rule-wp-34.06.
Read the common context and WP34 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-34); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-34-90"></a>
#### 265. 34.90 — Verify the owned artifact and real integration

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 34.90 — Verify the owned artifact and real integration.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\34-arcscope-analysis-and-reporting.md
Owning section: WP-34.90; explicit anchor: rule-wp-34.90.
Read the common context and WP34 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-34); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="wp-35"></a>
### WP-35 — ArcScope Integration and Metadata Sync

Full WP: [formal source](<C:/MyFile/Projects/ArcForges-Design/docs/planning/work-packages/35-arcscope-integration-and-sync.md>). Reading context: [WP35](reading-map.md#wp-35).

Direct upstream WPs: 25, 34. Complete Scope capability/context, metadata sync and portability. Raw capture upload stays explicit and bounded; real Cloud simulator integration is WP51.

<a id="substep-35-00"></a>
#### 266. 35.00 — Capability surface

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 35.00 — Capability surface.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\35-arcscope-integration-and-sync.md
Owning section: WP-35.00; explicit anchor: rule-wp-35.00.
Read the common context and WP35 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-35); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-35-01"></a>
#### 267. 35.01 — Bounded context provision

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 35.01 — Bounded context provision.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\35-arcscope-integration-and-sync.md
Owning section: WP-35.01; explicit anchor: rule-wp-35.01.
Read the common context and WP35 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-35); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-35-02"></a>
#### 268. 35.02 — Cloud sync scope

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 35.02 — Cloud sync scope.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\35-arcscope-integration-and-sync.md
Owning section: WP-35.02; explicit anchor: rule-wp-35.02.
Read the common context and WP35 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-35); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-35-03"></a>
#### 269. 35.03 — Explicit raw upload

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 35.03 — Explicit raw upload.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\35-arcscope-integration-and-sync.md
Owning section: WP-35.03; explicit anchor: rule-wp-35.03.
Read the common context and WP35 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-35); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-35-04"></a>
#### 270. 35.04 — Import, export and fixtures

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 35.04 — Import, export and fixtures.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\35-arcscope-integration-and-sync.md
Owning section: WP-35.04; explicit anchor: rule-wp-35.04.
Read the common context and WP35 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-35); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-35-05"></a>
#### 271. 35.05 — Extension boundary

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 35.05 — Extension boundary.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\35-arcscope-integration-and-sync.md
Owning section: WP-35.05; explicit anchor: rule-wp-35.05.
Read the common context and WP35 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-35); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-35-90"></a>
#### 272. 35.90 — Verify the owned artifact and real integration

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 35.90 — Verify the owned artifact and real integration.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\35-arcscope-integration-and-sync.md
Owning section: WP-35.90; explicit anchor: rule-wp-35.90.
Read the common context and WP35 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-35); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="wp-36"></a>
### WP-36 — ArcSlate Project, Timeline and Media Model

Full WP: [formal source](<C:/MyFile/Projects/ArcForges-Design/docs/planning/work-packages/36-arcslate-project-and-timeline.md>). Reading context: [WP36](reading-map.md#wp-36).

Direct upstream WPs: 07, 10, 13, 26. Implement Slate project/timeline/editing with exact time and recovery semantics, before playback/render consumers.

<a id="substep-36-00"></a>
#### 273. 36.00 — Project and sequence model

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 36.00 — Project and sequence model.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\36-arcslate-project-and-timeline.md
Owning section: WP-36.00; explicit anchor: rule-wp-36.00.
Read the common context and WP36 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-36); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-36-01"></a>
#### 274. 36.01 — The exact time model

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 36.01 — The exact time model.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\36-arcslate-project-and-timeline.md
Owning section: WP-36.01; explicit anchor: rule-wp-36.01.
Read the common context and WP36 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-36); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-36-02"></a>
#### 275. 36.02 — Media assets and availability

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 36.02 — Media assets and availability.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\36-arcslate-project-and-timeline.md
Owning section: WP-36.02; explicit anchor: rule-wp-36.02.
Read the common context and WP36 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-36); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-36-03"></a>
#### 276. 36.03 — Media library

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 36.03 — Media library.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\36-arcslate-project-and-timeline.md
Owning section: WP-36.03; explicit anchor: rule-wp-36.03.
Read the common context and WP36 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-36); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-36-04"></a>
#### 277. 36.04 — Timeline and tracks

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 36.04 — Timeline and tracks.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\36-arcslate-project-and-timeline.md
Owning section: WP-36.04; explicit anchor: rule-wp-36.04.
Read the common context and WP36 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-36); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-36-05"></a>
#### 278. 36.05 — Editing operations

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 36.05 — Editing operations.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\36-arcslate-project-and-timeline.md
Owning section: WP-36.05; explicit anchor: rule-wp-36.05.
Read the common context and WP36 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-36); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-36-06"></a>
#### 279. 36.06 — Undo, checkpoints and recovery

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 36.06 — Undo, checkpoints and recovery.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\36-arcslate-project-and-timeline.md
Owning section: WP-36.06; explicit anchor: rule-wp-36.06.
Read the common context and WP36 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-36); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-36-07"></a>
#### 280. 36.07 — Reference drift check

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 36.07 — Reference drift check.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\36-arcslate-project-and-timeline.md
Owning section: WP-36.07; explicit anchor: rule-wp-36.07.
Read the common context and WP36 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-36); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-36-90"></a>
#### 281. 36.90 — Verify the owned artifact and real integration

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 36.90 — Verify the owned artifact and real integration.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\36-arcslate-project-and-timeline.md
Owning section: WP-36.90; explicit anchor: rule-wp-36.90.
Read the common context and WP36 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-36); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="wp-37"></a>
### WP-37 — ArcSlate Playback and Processing Runtime

Full WP: [formal source](<C:/MyFile/Projects/ArcForges-Design/docs/planning/work-packages/37-arcslate-playback-and-processing.md>). Reading context: [WP37](reading-map.md#wp-37).

Direct upstream WPs: 36. Implement real native decode/playback, clocks, retime/effect/audio graphs and contained parsing; honor portable paths and optional backend distinctions.

<a id="substep-37-00"></a>
#### 282. 37.00 — Native media boundary

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 37.00 — Native media boundary.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\37-arcslate-playback-and-processing.md
Owning section: WP-37.00; explicit anchor: rule-wp-37.00.
Read the common context and WP37 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-37); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-37-01"></a>
#### 283. 37.01 — Decode and buffers

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 37.01 — Decode and buffers.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\37-arcslate-playback-and-processing.md
Owning section: WP-37.01; explicit anchor: rule-wp-37.01.
Read the common context and WP37 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-37); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-37-02"></a>
#### 284. 37.02 — Playback engine and clock

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 37.02 — Playback engine and clock.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\37-arcslate-playback-and-processing.md
Owning section: WP-37.02; explicit anchor: rule-wp-37.02.
Read the common context and WP37 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-37); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-37-03"></a>
#### 285. 37.03 — Processing graph

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 37.03 — Processing graph.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\37-arcslate-playback-and-processing.md
Owning section: WP-37.03; explicit anchor: rule-wp-37.03.
Read the common context and WP37 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-37); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-37-04"></a>
#### 286. 37.04 — Audio

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 37.04 — Audio.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\37-arcslate-playback-and-processing.md
Owning section: WP-37.04; explicit anchor: rule-wp-37.04.
Read the common context and WP37 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-37); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-37-05"></a>
#### 287. 37.05 — Proxies and caches

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 37.05 — Proxies and caches.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\37-arcslate-playback-and-processing.md
Owning section: WP-37.05; explicit anchor: rule-wp-37.05.
Read the common context and WP37 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-37); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-37-06"></a>
#### 288. 37.06 — Viewer

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 37.06 — Viewer.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\37-arcslate-playback-and-processing.md
Owning section: WP-37.06; explicit anchor: rule-wp-37.06.
Read the common context and WP37 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-37); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-37-90"></a>
#### 289. 37.90 — Verify the owned artifact and real integration

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 37.90 — Verify the owned artifact and real integration.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\37-arcslate-playback-and-processing.md
Owning section: WP-37.90; explicit anchor: rule-wp-37.90.
Read the common context and WP37 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-37); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="wp-38"></a>
### WP-38 — ArcSlate Render, Export and Colour Management

Full WP: [formal source](<C:/MyFile/Projects/ArcForges-Design/docs/planning/work-packages/38-arcslate-render-and-colour.md>). Reading context: [WP38](reading-map.md#wp-38).

Direct upstream WPs: 37. Complete colour, scopes, render/encoding/subtitle profiles and atomic export; verify declared numeric tolerances rather than inventing cross-encoder byte identity.

<a id="substep-38-00"></a>
#### 290. 38.00 — Colour management

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 38.00 — Colour management.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\38-arcslate-render-and-colour.md
Owning section: WP-38.00; explicit anchor: rule-wp-38.00.
Read the common context and WP38 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-38); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-38-01"></a>
#### 291. 38.01 — Video scopes

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 38.01 — Video scopes.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\38-arcslate-render-and-colour.md
Owning section: WP-38.01; explicit anchor: rule-wp-38.01.
Read the common context and WP38 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-38); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-38-02"></a>
#### 292. 38.02 — Render planning and snapshot binding

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 38.02 — Render planning and snapshot binding.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\38-arcslate-render-and-colour.md
Owning section: WP-38.02; explicit anchor: rule-wp-38.02.
Read the common context and WP38 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-38); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-38-03"></a>
#### 293. 38.03 — Render execution and atomic export

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 38.03 — Render execution and atomic export.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\38-arcslate-render-and-colour.md
Owning section: WP-38.03; explicit anchor: rule-wp-38.03.
Read the common context and WP38 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-38); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-38-04"></a>
#### 294. 38.04 — Export presets and encoding

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 38.04 — Export presets and encoding.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\38-arcslate-render-and-colour.md
Owning section: WP-38.04; explicit anchor: rule-wp-38.04.
Read the common context and WP38 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-38); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-38-05"></a>
#### 295. 38.05 — Subtitles and captions

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 38.05 — Subtitles and captions.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\38-arcslate-render-and-colour.md
Owning section: WP-38.05; explicit anchor: rule-wp-38.05.
Read the common context and WP38 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-38); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-38-06"></a>
#### 296. 38.06 — Golden output stability

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 38.06 — Golden output stability.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\38-arcslate-render-and-colour.md
Owning section: WP-38.06; explicit anchor: rule-wp-38.06.
Read the common context and WP38 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-38); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-38-90"></a>
#### 297. 38.90 — Verify the owned artifact and real integration

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 38.90 — Verify the owned artifact and real integration.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\38-arcslate-render-and-colour.md
Owning section: WP-38.90; explicit anchor: rule-wp-38.90.
Read the common context and WP38 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-38); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="wp-39"></a>
### WP-39 — ArcSlate Integration and Portability

Full WP: [formal source](<C:/MyFile/Projects/ArcForges-Design/docs/planning/work-packages/39-arcslate-integration-and-portability.md>). Reading context: [WP39](reading-map.md#wp-39).

Direct upstream WPs: 25, 38. Complete Slate packaging, relink, metadata sync and bidirectional OTIO fidelity. Real AI transcription/adoption integrates later at WP52.

<a id="substep-39-00"></a>
#### 298. 39.00 — Capability surface

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 39.00 — Capability surface.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\39-arcslate-integration-and-portability.md
Owning section: WP-39.00; explicit anchor: rule-wp-39.00.
Read the common context and WP39 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-39); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-39-01"></a>
#### 299. 39.01 — Bounded context provision

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 39.01 — Bounded context provision.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\39-arcslate-integration-and-portability.md
Owning section: WP-39.01; explicit anchor: rule-wp-39.01.
Read the common context and WP39 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-39); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-39-02"></a>
#### 300. 39.02 — Collect, consolidate and the portable package

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 39.02 — Collect, consolidate and the portable package.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\39-arcslate-integration-and-portability.md
Owning section: WP-39.02; explicit anchor: rule-wp-39.02.
Read the common context and WP39 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-39); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-39-03"></a>
#### 301. 39.03 — Cross-device resolution and relink

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 39.03 — Cross-device resolution and relink.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\39-arcslate-integration-and-portability.md
Owning section: WP-39.03; explicit anchor: rule-wp-39.03.
Read the common context and WP39 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-39); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-39-04"></a>
#### 302. 39.04 — Sync scope

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 39.04 — Sync scope.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\39-arcslate-integration-and-portability.md
Owning section: WP-39.04; explicit anchor: rule-wp-39.04.
Read the common context and WP39 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-39); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-39-05"></a>
#### 303. 39.05 — OTIO interchange

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 39.05 — OTIO interchange.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\39-arcslate-integration-and-portability.md
Owning section: WP-39.05; explicit anchor: rule-wp-39.05.
Read the common context and WP39 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-39); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-39-90"></a>
#### 304. 39.90 — Verify the owned artifact and real integration

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 39.90 — Verify the owned artifact and real integration.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\39-arcslate-integration-and-portability.md
Owning section: WP-39.90; explicit anchor: rule-wp-39.90.
Read the common context and WP39 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-39); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="wp-41"></a>
### WP-41 — Extension Platform and Integrations

Full WP: [formal source](<C:/MyFile/Projects/ArcForges-Design/docs/planning/work-packages/41-extension-platform-and-integrations.md>). Reading context: [WP41](reading-map.md#wp-41).

Direct upstream WPs: 09, 11, 17, 22, 25. Produce extension host/protocol, package/connector lifecycle, public SDK/CLI and actual PackageCatalog APIs. WP45.10 consumes these APIs for review/revocation UI.

<a id="substep-41-00"></a>
#### 305. 41.00 — Extension host and supervision

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 41.00 — Extension host and supervision.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\41-extension-platform-and-integrations.md
Owning section: WP-41.00; explicit anchor: rule-wp-41.00.
Read the common context and WP41 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-41); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-41-01"></a>
#### 306. 41.01 — Handshake and protocol versioning

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 41.01 — Handshake and protocol versioning.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\41-extension-platform-and-integrations.md
Owning section: WP-41.01; explicit anchor: rule-wp-41.01.
Read the common context and WP41 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-41); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-41-02"></a>
#### 307. 41.02 — The dual capability boundary

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 41.02 — The dual capability boundary.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\41-extension-platform-and-integrations.md
Owning section: WP-41.02; explicit anchor: rule-wp-41.02.
Read the common context and WP41 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-41); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-41-03"></a>
#### 308. 41.03 — Declarative UI contribution

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 41.03 — Declarative UI contribution.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\41-extension-platform-and-integrations.md
Owning section: WP-41.03; explicit anchor: rule-wp-41.03.
Read the common context and WP41 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-41); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-41-04"></a>
#### 309. 41.04 — Package runtime

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 41.04 — Package runtime.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\41-extension-platform-and-integrations.md
Owning section: WP-41.04; explicit anchor: rule-wp-41.04.
Read the common context and WP41 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-41); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-41-05"></a>
#### 310. 41.05 — PackageCatalog producer and consumers

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 41.05 — PackageCatalog producer and consumers.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\41-extension-platform-and-integrations.md
Owning section: WP-41.05; explicit anchor: rule-wp-41.05.
Read the common context and WP41 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-41); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-41-06"></a>
#### 311. 41.06 — Public SDK and CLI

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 41.06 — Public SDK and CLI.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\41-extension-platform-and-integrations.md
Owning section: WP-41.06; explicit anchor: rule-wp-41.06.
Read the common context and WP41 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-41); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-41-07"></a>
#### 312. 41.07 — MCP placement and connectors

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 41.07 — MCP placement and connectors.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\41-extension-platform-and-integrations.md
Owning section: WP-41.07; explicit anchor: rule-wp-41.07.
Read the common context and WP41 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-41); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-41-90"></a>
#### 313. 41.90 — Verify the owned artifact and real integration

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 41.90 — Verify the owned artifact and real integration.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\41-extension-platform-and-integrations.md
Owning section: WP-41.90; explicit anchor: rule-wp-41.90.
Read the common context and WP41 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-41); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="wp-42"></a>
### WP-42 — Commerce, Entitlement and Credits

Full WP: [formal source](<C:/MyFile/Projects/ArcForges-Design/docs/planning/work-packages/42-commerce-entitlement-and-credits.md>). Reading context: [WP42](reading-map.md#wp-42).

Direct upstream WPs: 22, 23. Implement technical commerce and test-mode proof. Execute 42.11 before 42.10. Actual receipt, payout, pricing activation and customer journey remain gated at WP48/50.

<a id="substep-42-00"></a>
#### 314. 42.00 — Provider adapter boundary

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 42.00 — Provider adapter boundary.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\42-commerce-entitlement-and-credits.md
Owning section: WP-42.00; explicit anchor: rule-wp-42.00.
Read the common context and WP42 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-42); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-42-01"></a>
#### 315. 42.01 — Catalogue and versioned policy

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 42.01 — Catalogue and versioned policy.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\42-commerce-entitlement-and-credits.md
Owning section: WP-42.01; explicit anchor: rule-wp-42.01.
Read the common context and WP42 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-42); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-42-02"></a>
#### 316. 42.02 — Purchase pipeline

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 42.02 — Purchase pipeline.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\42-commerce-entitlement-and-credits.md
Owning section: WP-42.02; explicit anchor: rule-wp-42.02.
Read the common context and WP42 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-42); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-42-03"></a>
#### 317. 42.03 — Provider event inbox

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 42.03 — Provider event inbox.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\42-commerce-entitlement-and-credits.md
Owning section: WP-42.03; explicit anchor: rule-wp-42.03.
Read the common context and WP42 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-42); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-42-04"></a>
#### 318. 42.04 — Entitlement resolver

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 42.04 — Entitlement resolver.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\42-commerce-entitlement-and-credits.md
Owning section: WP-42.04; explicit anchor: rule-wp-42.04.
Read the common context and WP42 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-42); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-42-05"></a>
#### 319. 42.05 — Distribution and enforcement

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 42.05 — Distribution and enforcement.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\42-commerce-entitlement-and-credits.md
Owning section: WP-42.05; explicit anchor: rule-wp-42.05.
Read the common context and WP42 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-42); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-42-06"></a>
#### 320. 42.06 — Quota, usage and storage accounting

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 42.06 — Quota, usage and storage accounting.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\42-commerce-entitlement-and-credits.md
Owning section: WP-42.06; explicit anchor: rule-wp-42.06.
Read the common context and WP42 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-42); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-42-07"></a>
#### 321. 42.07 — Credits

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 42.07 — Credits.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\42-commerce-entitlement-and-credits.md
Owning section: WP-42.07; explicit anchor: rule-wp-42.07.
Read the common context and WP42 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-42); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-42-08"></a>
#### 322. 42.08 — Ledgers and reconciliation

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 42.08 — Ledgers and reconciliation.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\42-commerce-entitlement-and-credits.md
Owning section: WP-42.08; explicit anchor: rule-wp-42.08.
Read the common context and WP42 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-42); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-42-09"></a>
#### 323. 42.09 — Refunds, disputes and evidence

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 42.09 — Refunds, disputes and evidence.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\42-commerce-entitlement-and-credits.md
Owning section: WP-42.09; explicit anchor: rule-wp-42.09.
Read the common context and WP42 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-42); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-42-11"></a>
#### 324. 42.11 — Service term and replenishing capacity

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 42.11 — Service term and replenishing capacity.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\42-commerce-entitlement-and-credits.md
Owning section: WP-42.11; explicit anchor: rule-wp-42.11.
Read the common context and WP42 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-42); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-42-10"></a>
#### 325. 42.10 — Technical commerce closure and live gate staging

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 42.10 — Technical commerce closure and live gate staging.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\42-commerce-entitlement-and-credits.md
Owning section: WP-42.10; explicit anchor: rule-wp-42.10.
Read the common context and WP42 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-42); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-42-90"></a>
#### 326. 42.90 — Verify the owned artifact and real integration

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 42.90 — Verify the owned artifact and real integration.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\42-commerce-entitlement-and-credits.md
Owning section: WP-42.90; explicit anchor: rule-wp-42.90.
Read the common context and WP42 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-42); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="wp-44"></a>
### WP-44 — Dynamic Policy and Configuration Control Plane

Full WP: [formal source](<C:/MyFile/Projects/ArcForges-Design/docs/planning/work-packages/44-dynamic-policy-and-configuration.md>). Reading context: [WP44](reading-map.md#wp-44).

Direct upstream WPs: 23, 42. Produce typed policy/configuration authority with deterministic rollout, history and last-known-good recovery before its AI/search/operations consumers.

<a id="substep-44-00"></a>
#### 327. 44.00 — The four boundaries

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 44.00 — The four boundaries.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\44-dynamic-policy-and-configuration.md
Owning section: WP-44.00; explicit anchor: rule-wp-44.00.
Read the common context and WP44 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-44); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-44-01"></a>
#### 328. 44.01 — Schema-constrained configuration

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 44.01 — Schema-constrained configuration.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\44-dynamic-policy-and-configuration.md
Owning section: WP-44.01; explicit anchor: rule-wp-44.01.
Read the common context and WP44 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-44); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-44-02"></a>
#### 329. 44.02 — Compiled hard limits

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 44.02 — Compiled hard limits.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\44-dynamic-policy-and-configuration.md
Owning section: WP-44.02; explicit anchor: rule-wp-44.02.
Read the common context and WP44 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-44); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-44-03"></a>
#### 330. 44.03 — Features, flags and deterministic rollout

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 44.03 — Features, flags and deterministic rollout.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\44-dynamic-policy-and-configuration.md
Owning section: WP-44.03; explicit anchor: rule-wp-44.03.
Read the common context and WP44 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-44); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-44-04"></a>
#### 331. 44.04 — Kill switches

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 44.04 — Kill switches.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\44-dynamic-policy-and-configuration.md
Owning section: WP-44.04; explicit anchor: rule-wp-44.04.
Read the common context and WP44 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-44); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-44-05"></a>
#### 332. 44.05 — Scoped resolution and explainability

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 44.05 — Scoped resolution and explainability.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\44-dynamic-policy-and-configuration.md
Owning section: WP-44.05; explicit anchor: rule-wp-44.05.
Read the common context and WP44 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-44); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-44-06"></a>
#### 333. 44.06 — Compatibility policy

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 44.06 — Compatibility policy.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\44-dynamic-policy-and-configuration.md
Owning section: WP-44.06; explicit anchor: rule-wp-44.06.
Read the common context and WP44 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-44); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-44-07"></a>
#### 334. 44.07 — Publication, staleness and last-known-good

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 44.07 — Publication, staleness and last-known-good.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\44-dynamic-policy-and-configuration.md
Owning section: WP-44.07; explicit anchor: rule-wp-44.07.
Read the common context and WP44 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-44); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-44-90"></a>
#### 335. 44.90 — Verify the owned artifact and real integration

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 44.90 — Verify the owned artifact and real integration.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\44-dynamic-policy-and-configuration.md
Owning section: WP-44.90; explicit anchor: rule-wp-44.90.
Read the common context and WP44 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-44); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="wp-43"></a>
### WP-43 — Workers AI Routing and Metering

Full WP: [formal source](<C:/MyFile/Projects/ArcForges-Design/docs/planning/work-packages/43-managed-ai-routing-and-metering.md>). Reading context: [WP43](reading-map.md#wp-43).

Direct upstream WPs: 25, 42, 44. Implement actual Workers AI routing/metering and uncertain-outcome handling. Execute 43.07 before 43.06; recorded fixtures complement real supplier/usage evidence.

<a id="substep-43-00"></a>
#### 336. 43.00 — Provider adapters and routing

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 43.00 — Provider adapters and routing.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\43-managed-ai-routing-and-metering.md
Owning section: WP-43.00; explicit anchor: rule-wp-43.00.
Read the common context and WP43 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-43); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-43-01"></a>
#### 337. 43.01 — Tariffs and cost dimensions

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 43.01 — Tariffs and cost dimensions.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\43-managed-ai-routing-and-metering.md
Owning section: WP-43.01; explicit anchor: rule-wp-43.01.
Read the common context and WP43 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-43); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-43-02"></a>
#### 338. 43.02 — Metering and settlement

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 43.02 — Metering and settlement.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\43-managed-ai-routing-and-metering.md
Owning section: WP-43.02; explicit anchor: rule-wp-43.02.
Read the common context and WP43 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-43); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-43-03"></a>
#### 339. 43.03 — Selected supplier and realm routing

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 43.03 — Selected supplier and realm routing.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\43-managed-ai-routing-and-metering.md
Owning section: WP-43.03; explicit anchor: rule-wp-43.03.
Read the common context and WP43 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-43); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-43-04"></a>
#### 340. 43.04 — Provider interaction records and transparency

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 43.04 — Provider interaction records and transparency.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\43-managed-ai-routing-and-metering.md
Owning section: WP-43.04; explicit anchor: rule-wp-43.04.
Read the common context and WP43 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-43); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-43-05"></a>
#### 341. 43.05 — Funding and uncertain outcome proof

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 43.05 — Funding and uncertain outcome proof.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\43-managed-ai-routing-and-metering.md
Owning section: WP-43.05; explicit anchor: rule-wp-43.05.
Read the common context and WP43 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-43); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-43-07"></a>
#### 342. 43.07 — Real-provider metering evidence

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 43.07 — Real-provider metering evidence.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\43-managed-ai-routing-and-metering.md
Owning section: WP-43.07; explicit anchor: rule-wp-43.07.
Read the common context and WP43 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-43); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-43-06"></a>
#### 343. 43.06 — Provider test-environment coverage

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 43.06 — Provider test-environment coverage.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\43-managed-ai-routing-and-metering.md
Owning section: WP-43.06; explicit anchor: rule-wp-43.06.
Read the common context and WP43 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-43); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-43-90"></a>
#### 344. 43.90 — Verify the owned artifact and real integration

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 43.90 — Verify the owned artifact and real integration.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\43-managed-ai-routing-and-metering.md
Owning section: WP-43.90; explicit anchor: rule-wp-43.90.
Read the common context and WP43 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-43); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="wp-40"></a>
### WP-40 — Application-Scoped Knowledge Search and Retrieval

Full WP: [formal source](<C:/MyFile/Projects/ArcForges-Design/docs/planning/work-packages/40-knowledge-search-and-retrieval.md>). Reading context: [WP40](reading-map.md#wp-40).

Direct upstream WPs: 19, 25, 28, 43, 44. Produce actual application-scoped derived search/retrieval with current permissions, consent and citations. No cross-product aggregator is introduced.

<a id="substep-40-00"></a>
#### 345. 40.00 — Source ownership

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 40.00 — Source ownership.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\40-knowledge-search-and-retrieval.md
Owning section: WP-40.00; explicit anchor: rule-wp-40.00.
Read the common context and WP40 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-40); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-40-01"></a>
#### 346. 40.01 — Scoped derived index production

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 40.01 — Scoped derived index production.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\40-knowledge-search-and-retrieval.md
Owning section: WP-40.01; explicit anchor: rule-wp-40.01.
Read the common context and WP40 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-40); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-40-02"></a>
#### 347. 40.02 — Hybrid retrieval and budgets

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 40.02 — Hybrid retrieval and budgets.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\40-knowledge-search-and-retrieval.md
Owning section: WP-40.02; explicit anchor: rule-wp-40.02.
Read the common context and WP40 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-40); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-40-03"></a>
#### 348. 40.03 — Current permission

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 40.03 — Current permission.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\40-knowledge-search-and-retrieval.md
Owning section: WP-40.03; explicit anchor: rule-wp-40.03.
Read the common context and WP40 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-40); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-40-04"></a>
#### 349. 40.04 — Evidence and citations

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 40.04 — Evidence and citations.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\40-knowledge-search-and-retrieval.md
Owning section: WP-40.04; explicit anchor: rule-wp-40.04.
Read the common context and WP40 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-40); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-40-05"></a>
#### 350. 40.05 — Privacy and caches

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 40.05 — Privacy and caches.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\40-knowledge-search-and-retrieval.md
Owning section: WP-40.05; explicit anchor: rule-wp-40.05.
Read the common context and WP40 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-40); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-40-06"></a>
#### 351. 40.06 — Real Cloud query path

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 40.06 — Real Cloud query path.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\40-knowledge-search-and-retrieval.md
Owning section: WP-40.06; explicit anchor: rule-wp-40.06.
Read the common context and WP40 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-40); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-40-90"></a>
#### 352. 40.90 — Owned artifacts and real integration

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 40.90 — Owned artifacts and real integration.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\40-knowledge-search-and-retrieval.md
Owning section: WP-40.90; explicit anchor: rule-wp-40.90.
Read the common context and WP40 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-40); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="wp-47"></a>
### WP-47 — Static Public Site

Full WP: [formal source](<C:/MyFile/Projects/ArcForges-Design/docs/planning/work-packages/47-static-public-site.md>). Reading context: [WP47](reading-map.md#wp-47).

Direct upstream WPs: 00, 02. Produce Web tooling/design system and static site before WP45. Approved-shape test offers/downloads are fixtures; real public projection and activation close at WP50.

<a id="substep-47-00"></a>
#### 353. 47.00 — React static generation and determinism

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 47.00 — React static generation and determinism.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\47-static-public-site.md
Owning section: WP-47.00; explicit anchor: rule-wp-47.00.
Read the common context and WP47 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-47); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-47-01"></a>
#### 354. 47.01 — Versioned public content and pricing inputs

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 47.01 — Versioned public content and pricing inputs.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\47-static-public-site.md
Owning section: WP-47.01; explicit anchor: rule-wp-47.01.
Read the common context and WP47 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-47); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-47-02"></a>
#### 355. 47.02 — Rendering and performance

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 47.02 — Rendering and performance.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\47-static-public-site.md
Owning section: WP-47.02; explicit anchor: rule-wp-47.02.
Read the common context and WP47 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-47); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-47-03"></a>
#### 356. 47.03 — Internationalisation

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 47.03 — Internationalisation.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\47-static-public-site.md
Owning section: WP-47.03; explicit anchor: rule-wp-47.03.
Read the common context and WP47 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-47); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-47-04"></a>
#### 357. 47.04 — Documentation, downloads and legal

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 47.04 — Documentation, downloads and legal.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\47-static-public-site.md
Owning section: WP-47.04; explicit anchor: rule-wp-47.04.
Read the common context and WP47 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-47); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-47-05"></a>
#### 358. 47.05 — Accessibility and analytics

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 47.05 — Accessibility and analytics.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\47-static-public-site.md
Owning section: WP-47.05; explicit anchor: rule-wp-47.05.
Read the common context and WP47 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-47); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-47-06"></a>
#### 359. 47.06 — Independence and deployment

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 47.06 — Independence and deployment.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\47-static-public-site.md
Owning section: WP-47.06; explicit anchor: rule-wp-47.06.
Read the common context and WP47 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-47); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-47-07"></a>
#### 360. 47.07 — Owned consumer design system

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 47.07 — Owned consumer design system.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\47-static-public-site.md
Owning section: WP-47.07; explicit anchor: rule-wp-47.07.
Read the common context and WP47 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-47); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-47-90"></a>
#### 361. 47.90 — Verify the owned artifact and real integration

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 47.90 — Verify the owned artifact and real integration.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\47-static-public-site.md
Owning section: WP-47.90; explicit anchor: rule-wp-47.90.
Read the common context and WP47 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-47); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="wp-45"></a>
### WP-45 — Operations, Support and Trust & Safety

Full WP: [formal source](<C:/MyFile/Projects/ArcForges-Design/docs/planning/work-packages/45-operations-support-and-trust-safety.md>). Reading context: [WP45](reading-map.md#wp-45).

Direct upstream WPs: 12, 21, 41, 44, 47. Build actual Operations UI, customer push sender and PackageCatalog review. Rehearse implemented paths now; backup/Harness/combined disaster evidence joins at WP46/52/50.

<a id="substep-45-00"></a>
#### 362. 45.00 — Service levels and alerting

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 45.00 — Service levels and alerting.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\45-operations-support-and-trust-safety.md
Owning section: WP-45.00; explicit anchor: rule-wp-45.00.
Read the common context and WP45 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-45); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-45-01"></a>
#### 363. 45.01 — Incident process

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 45.01 — Incident process.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\45-operations-support-and-trust-safety.md
Owning section: WP-45.01; explicit anchor: rule-wp-45.01.
Read the common context and WP45 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-45); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-45-02"></a>
#### 364. 45.02 — Runbooks and rehearsal

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 45.02 — Runbooks and rehearsal.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\45-operations-support-and-trust-safety.md
Owning section: WP-45.02; explicit anchor: rule-wp-45.02.
Read the common context and WP45 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-45); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-45-03"></a>
#### 365. 45.03 — Status page

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 45.03 — Status page.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\45-operations-support-and-trust-safety.md
Owning section: WP-45.03; explicit anchor: rule-wp-45.03.
Read the common context and WP45 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-45); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-45-04"></a>
#### 366. 45.04 — Operator console and support access

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 45.04 — Operator console and support access.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\45-operations-support-and-trust-safety.md
Owning section: WP-45.04; explicit anchor: rule-wp-45.04.
Read the common context and WP45 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-45); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-45-05"></a>
#### 367. 45.05 — Break-glass

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 45.05 — Break-glass.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\45-operations-support-and-trust-safety.md
Owning section: WP-45.05; explicit anchor: rule-wp-45.05.
Read the common context and WP45 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-45); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-45-06"></a>
#### 368. 45.06 — Support cases and in-product reporting

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 45.06 — Support cases and in-product reporting.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\45-operations-support-and-trust-safety.md
Owning section: WP-45.06; explicit anchor: rule-wp-45.06.
Read the common context and WP45 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-45); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-45-07"></a>
#### 369. 45.07 — Trust and safety

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 45.07 — Trust and safety.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\45-operations-support-and-trust-safety.md
Owning section: WP-45.07; explicit anchor: rule-wp-45.07.
Read the common context and WP45 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-45); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-45-08"></a>
#### 370. 45.08 — Operational mail and provider drills

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 45.08 — Operational mail and provider drills.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\45-operations-support-and-trust-safety.md
Owning section: WP-45.08; explicit anchor: rule-wp-45.08.
Read the common context and WP45 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-45); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-45-09"></a>
#### 371. 45.09 — Customer push delivery and registration lifecycle

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 45.09 — Customer push delivery and registration lifecycle.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\45-operations-support-and-trust-safety.md
Owning section: WP-45.09; explicit anchor: rule-wp-45.09.
Read the common context and WP45 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-45); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-45-10"></a>
#### 372. 45.10 — Package review and revocation console

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 45.10 — Package review and revocation console.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\45-operations-support-and-trust-safety.md
Owning section: WP-45.10; explicit anchor: rule-wp-45.10.
Read the common context and WP45 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-45); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-45-90"></a>
#### 373. 45.90 — Verify the owned artifact and real integration

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 45.90 — Verify the owned artifact and real integration.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\45-operations-support-and-trust-safety.md
Owning section: WP-45.90; explicit anchor: rule-wp-45.90.
Read the common context and WP45 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-45); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="wp-53"></a>
### WP-53 — Desktop Distribution, Update Client and Channels

Full WP: [formal source](<C:/MyFile/Projects/ArcForges-Design/docs/planning/work-packages/53-desktop-distribution-and-update.md>). Reading context: [WP53](reading-map.md#wp-53).

Direct upstream WPs: 02, 06, 07, 10, 11, 12, 44, 45. Produce the updater and distribution trust with real staged apply/rollback. Keep the source numbering gap: 53.06 does not exist. Test signing proves mechanics; WP50 verifies production release trust.

<a id="substep-53-00"></a>
#### 374. 53.00 — Signed feed and applicable target

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 53.00 — Signed feed and applicable target.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\53-desktop-distribution-and-update.md
Owning section: WP-53.00; explicit anchor: rule-wp-53.00.
Read the common context and WP53 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-53); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-53-01"></a>
#### 375. 53.01 — Background download and staging

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 53.01 — Background download and staging.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\53-desktop-distribution-and-update.md
Owning section: WP-53.01; explicit anchor: rule-wp-53.01.
Read the common context and WP53 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-53); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-53-02"></a>
#### 376. 53.02 — Safe apply and atomic activation

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 53.02 — Safe apply and atomic activation.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\53-desktop-distribution-and-update.md
Owning section: WP-53.02; explicit anchor: rule-wp-53.02.
Read the common context and WP53 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-53); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-53-03"></a>
#### 377. 53.03 — Rollback and migration interlock

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 53.03 — Rollback and migration interlock.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\53-desktop-distribution-and-update.md
Owning section: WP-53.03; explicit anchor: rule-wp-53.03.
Read the common context and WP53 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-53); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-53-04"></a>
#### 378. 53.04 — Channels, staged rollout and security updates

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 53.04 — Channels, staged rollout and security updates.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\53-desktop-distribution-and-update.md
Owning section: WP-53.04; explicit anchor: rule-wp-53.04.
Read the common context and WP53 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-53); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-53-05"></a>
#### 379. 53.05 — Diagnostics and preserving data on uninstall

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 53.05 — Diagnostics and preserving data on uninstall.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\53-desktop-distribution-and-update.md
Owning section: WP-53.05; explicit anchor: rule-wp-53.05.
Read the common context and WP53 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-53); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-53-07"></a>
#### 380. 53.07 — Production catalog and Android distribution trust

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 53.07 — Production catalog and Android distribution trust.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\53-desktop-distribution-and-update.md
Owning section: WP-53.07; explicit anchor: rule-wp-53.07.
Read the common context and WP53 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-53); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-53-90"></a>
#### 381. 53.90 — Verify the owned artifact and real integration

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 53.90 — Verify the owned artifact and real integration.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\53-desktop-distribution-and-update.md
Owning section: WP-53.90; explicit anchor: rule-wp-53.90.
Read the common context and WP53 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-53); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="wp-46"></a>
### WP-46 — D1, R2 and Independent Disaster Recovery

Full WP: [formal source](<C:/MyFile/Projects/ArcForges-Design/docs/planning/work-packages/46-backup-recovery-and-data-health.md>). Reading context: [WP46](reading-map.md#wp-46).

Direct upstream WPs: 25, 45. Prove independent D1/R2 backup and fresh restore, generation fencing and denial of old effects/credentials. Combined active Harness recovery still closes at WP50.

<a id="substep-46-00"></a>
#### 382. 46.00 — D1 and independent object backup

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 46.00 — D1 and independent object backup.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\46-backup-recovery-and-data-health.md
Owning section: WP-46.00; explicit anchor: rule-wp-46.00.
Read the common context and WP46 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-46); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-46-01"></a>
#### 383. 46.01 — Point-in-time and fresh restore

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 46.01 — Point-in-time and fresh restore.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\46-backup-recovery-and-data-health.md
Owning section: WP-46.01; explicit anchor: rule-wp-46.01.
Read the common context and WP46 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-46); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-46-02"></a>
#### 384. 46.02 — Fresh environment rebuild

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 46.02 — Fresh environment rebuild.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\46-backup-recovery-and-data-health.md
Owning section: WP-46.02; explicit anchor: rule-wp-46.02.
Read the common context and WP46 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-46); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-46-03"></a>
#### 385. 46.03 — Drill programme

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 46.03 — Drill programme.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\46-backup-recovery-and-data-health.md
Owning section: WP-46.03; explicit anchor: rule-wp-46.03.
Read the common context and WP46 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-46); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-46-04"></a>
#### 386. 46.04 — Data health

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 46.04 — Data health.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\46-backup-recovery-and-data-health.md
Owning section: WP-46.04; explicit anchor: rule-wp-46.04.
Read the common context and WP46 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-46); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-46-05"></a>
#### 387. 46.05 — Export and realm migration

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 46.05 — Export and realm migration.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\46-backup-recovery-and-data-health.md
Owning section: WP-46.05; explicit anchor: rule-wp-46.05.
Read the common context and WP46 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-46); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-46-06"></a>
#### 388. 46.06 — Backup release gate

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 46.06 — Backup release gate.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\46-backup-recovery-and-data-health.md
Owning section: WP-46.06; explicit anchor: rule-wp-46.06.
Read the common context and WP46 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-46); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-46-90"></a>
#### 389. 46.90 — Owned artifacts and real integration

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 46.90 — Owned artifacts and real integration.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\46-backup-recovery-and-data-health.md
Owning section: WP-46.90; explicit anchor: rule-wp-46.90.
Read the common context and WP46 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-46); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="wp-48"></a>
### WP-48 — Account Portal

Full WP: [formal source](<C:/MyFile/Projects/ArcForges-Design/docs/planning/work-packages/48-account-portal.md>). Reading context: [WP48](reading-map.md#wp-48).

Direct upstream WPs: 25, 42, 44, 46, 47. Deliver real account/session/commerce/export UI using the actual upstream producers; activation still requires the applicable real provider evidence.

<a id="substep-48-00"></a>
#### 390. 48.00 — Account profile and native ceremony integration

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 48.00 — Account profile and native ceremony integration.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\48-account-portal.md
Owning section: WP-48.00; explicit anchor: rule-wp-48.00.
Read the common context and WP48 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-48); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-48-01"></a>
#### 391. 48.01 — Real browser session and step-up acceptance

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 48.01 — Real browser session and step-up acceptance.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\48-account-portal.md
Owning section: WP-48.01; explicit anchor: rule-wp-48.01.
Read the common context and WP48 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-48); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-48-02"></a>
#### 392. 48.02 — Account and security surfaces

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 48.02 — Account and security surfaces.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\48-account-portal.md
Owning section: WP-48.02; explicit anchor: rule-wp-48.02.
Read the common context and WP48 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-48); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-48-03"></a>
#### 393. 48.03 — Workspace, storage and usage

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 48.03 — Workspace, storage and usage.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\48-account-portal.md
Owning section: WP-48.03; explicit anchor: rule-wp-48.03.
Read the common context and WP48 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-48); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-48-04"></a>
#### 394. 48.04 — Subscription, capacity, credits and hosted checkout

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 48.04 — Subscription, capacity, credits and hosted checkout.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\48-account-portal.md
Owning section: WP-48.04; explicit anchor: rule-wp-48.04.
Read the common context and WP48 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-48); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-48-05"></a>
#### 395. 48.05 — Data export and deletion

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 48.05 — Data export and deletion.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\48-account-portal.md
Owning section: WP-48.05; explicit anchor: rule-wp-48.05.
Read the common context and WP48 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-48); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-48-06"></a>
#### 396. 48.06 — Origin security and performance

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 48.06 — Origin security and performance.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\48-account-portal.md
Owning section: WP-48.06; explicit anchor: rule-wp-48.06.
Read the common context and WP48 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-48); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-48-07"></a>
#### 397. 48.07 — Offline, degradation and accessibility

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 48.07 — Offline, degradation and accessibility.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\48-account-portal.md
Owning section: WP-48.07; explicit anchor: rule-wp-48.07.
Read the common context and WP48 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-48); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-48-90"></a>
#### 398. 48.90 — Verify the owned artifact and real integration

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 48.90 — Verify the owned artifact and real integration.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\48-account-portal.md
Owning section: WP-48.90; explicit anchor: rule-wp-48.90.
Read the common context and WP48 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-48); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="wp-51"></a>
### WP-51 — ArcScope Deterministic Cloud Simulator

Full WP: [formal source](<C:/MyFile/Projects/ArcForges-Design/docs/planning/work-packages/51-arcscope-cloud-simulator.md>). Reading context: [WP51](reading-map.md#wp-51).

Direct upstream WPs: 21, 23, 25, 33, 34, 35, 42, 44. Implement real deterministic simulator jobs, fenced D1 segment/checkpoint publication and R2 delivery into Scope. Synthetic results remain labelled and cannot prove hardware.

<a id="substep-51-00"></a>
#### 399. 51.00 — Definitions, versions and bounded evaluation

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 51.00 — Definitions, versions and bounded evaluation.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\51-arcscope-cloud-simulator.md
Owning section: WP-51.00; explicit anchor: rule-wp-51.00.
Read the common context and WP51 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-51); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-51-01"></a>
#### 400. 51.01 — Deterministic generation and faults

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 51.01 — Deterministic generation and faults.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\51-arcscope-cloud-simulator.md
Owning section: WP-51.01; explicit anchor: rule-wp-51.01.
Read the common context and WP51 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-51); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-51-02"></a>
#### 401. 51.02 — Fenced slices and SimulationPacer

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 51.02 — Fenced slices and SimulationPacer.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\51-arcscope-cloud-simulator.md
Owning section: WP-51.02; explicit anchor: rule-wp-51.02.
Read the common context and WP51 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-51); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-51-03"></a>
#### 402. 51.03 — Canonical publication, checkpoints and recovery

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 51.03 — Canonical publication, checkpoints and recovery.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\51-arcscope-cloud-simulator.md
Owning section: WP-51.03; explicit anchor: rule-wp-51.03.
Read the common context and WP51 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-51); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-51-04"></a>
#### 403. 51.04 — Client access and native ingestion

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 51.04 — Client access and native ingestion.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\51-arcscope-cloud-simulator.md
Owning section: WP-51.04; explicit anchor: rule-wp-51.04.
Read the common context and WP51 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-51); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-51-05"></a>
#### 404. 51.05 — Limits, entitlement and lifecycle

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 51.05 — Limits, entitlement and lifecycle.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\51-arcscope-cloud-simulator.md
Owning section: WP-51.05; explicit anchor: rule-wp-51.05.
Read the common context and WP51 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-51); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-51-90"></a>
#### 405. 51.90 — Verify the owned artifact and real integration

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 51.90 — Verify the owned artifact and real integration.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\51-arcscope-cloud-simulator.md
Owning section: WP-51.90; explicit anchor: rule-wp-51.90.
Read the common context and WP51 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-51); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="wp-52"></a>
### WP-52 — Sole Cloudflare Workflow Harness

Full WP: [formal source](<C:/MyFile/Projects/ArcForges-Design/docs/planning/work-packages/52-cloud-harness.md>). Reading context: [WP52](reading-map.md#wp-52).

Direct upstream WPs: 15, 17, 21, 23, 26, 39, 40, 41, 42, 43, 44. Implement the sole Workflow Harness with actual model/usage, local/Cloud/temporary modes, same-application tools and automation. Replace assigned earlier client fixtures and preserve uncertain effects.

<a id="substep-52-00"></a>
#### 406. 52.00 — The turn loop, batching and bounds

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 52.00 — The turn loop, batching and bounds.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\52-cloud-harness.md
Owning section: WP-52.00; explicit anchor: rule-wp-52.00.
Read the common context and WP52 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-52); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-52-01"></a>
#### 407. 52.01 — Context assembly and compaction

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 52.01 — Context assembly and compaction.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\52-cloud-harness.md
Owning section: WP-52.01; explicit anchor: rule-wp-52.01.
Read the common context and WP52 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-52); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-52-02"></a>
#### 408. 52.02 — Approval, cancellation and crash recovery

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 52.02 — Approval, cancellation and crash recovery.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\52-cloud-harness.md
Owning section: WP-52.02; explicit anchor: rule-wp-52.02.
Read the common context and WP52 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-52); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-52-03"></a>
#### 409. 52.03 — Generated streaming and durable output

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 52.03 — Generated streaming and durable output.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\52-cloud-harness.md
Owning section: WP-52.03; explicit anchor: rule-wp-52.03.
Read the common context and WP52 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-52); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-52-04"></a>
#### 410. 52.04 — Provider failure and effect certainty

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 52.04 — Provider failure and effect certainty.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\52-cloud-harness.md
Owning section: WP-52.04; explicit anchor: rule-wp-52.04.
Read the common context and WP52 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-52); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-52-05"></a>
#### 411. 52.05 — Complete own-application execution proof

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 52.05 — Complete own-application execution proof.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\52-cloud-harness.md
Owning section: WP-52.05; explicit anchor: rule-wp-52.05.
Read the common context and WP52 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-52); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-52-06"></a>
#### 412. 52.06 — Durable Cloud automation and authorised scheduling

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 52.06 — Durable Cloud automation and authorised scheduling.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\52-cloud-harness.md
Owning section: WP-52.06; explicit anchor: rule-wp-52.06.
Read the common context and WP52 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-52); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-52-90"></a>
#### 413. 52.90 — Verify the owned artifact and real integration

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 52.90 — Verify the owned artifact and real integration.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\52-cloud-harness.md
Owning section: WP-52.90; explicit anchor: rule-wp-52.90.
Read the common context and WP52 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-52); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="wp-31"></a>
### WP-31 — Complete ArcChat Android Companion

Full WP: [formal source](<C:/MyFile/Projects/ArcForges-Design/docs/planning/work-packages/31-arcchat-mobile-android.md>). Reading context: [WP31](reading-map.md#wp-31).

Direct upstream WPs: 26, 30, 45, 52. Complete the Android UI and companion flows against real Harness, Cloud and one-application bridge. Real push sender WP45.09 is already upstream.

<a id="substep-31-00"></a>
#### 414. 31.00 — Authentication, Home and workspace

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 31.00 — Authentication, Home and workspace.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\31-arcchat-mobile-android.md
Owning section: WP-31.00; explicit anchor: rule-wp-31.00.
Read the common context and WP31 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-31); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-31-01"></a>
#### 415. 31.01 — Conversations and context

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 31.01 — Conversations and context.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\31-arcchat-mobile-android.md
Owning section: WP-31.01; explicit anchor: rule-wp-31.01.
Read the common context and WP31 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-31); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-31-02"></a>
#### 416. 31.02 — Tasks, approvals and automation

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 31.02 — Tasks, approvals and automation.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\31-arcchat-mobile-android.md
Owning section: WP-31.02; explicit anchor: rule-wp-31.02.
Read the common context and WP31 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-31); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-31-03"></a>
#### 417. 31.03 — Library and resources

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 31.03 — Library and resources.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\31-arcchat-mobile-android.md
Owning section: WP-31.03; explicit anchor: rule-wp-31.03.
Read the common context and WP31 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-31); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-31-04"></a>
#### 418. 31.04 — Presence, push, links and settings

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 31.04 — Presence, push, links and settings.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\31-arcchat-mobile-android.md
Owning section: WP-31.04; explicit anchor: rule-wp-31.04.
Read the common context and WP31 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-31); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-31-05"></a>
#### 419. 31.05 — Native interaction and recovery

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 31.05 — Native interaction and recovery.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\31-arcchat-mobile-android.md
Owning section: WP-31.05; explicit anchor: rule-wp-31.05.
Read the common context and WP31 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-31); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-31-06"></a>
#### 420. 31.06 — Scope and licence enforcement

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 31.06 — Scope and licence enforcement.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\31-arcchat-mobile-android.md
Owning section: WP-31.06; explicit anchor: rule-wp-31.06.
Read the common context and WP31 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-31); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-31-90"></a>
#### 421. 31.90 — Complete companion acceptance

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 31.90 — Complete companion acceptance.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\31-arcchat-mobile-android.md
Owning section: WP-31.90; explicit anchor: rule-wp-31.90.
Read the common context and WP31 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-31); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="wp-32"></a>
### WP-32 — Android Signing, Distribution and Store Gates

Full WP: [formal source](<C:/MyFile/Projects/ArcForges-Design/docs/planning/work-packages/32-mobile-release-and-store-gates.md>). Reading context: [WP32](reading-map.md#wp-32).

Direct upstream WPs: 31. Verify signed Android distribution on actual required devices/channels, signing identity, consumption-only rules, push and non-GMS fallback. Missing external access remains a named gate.

<a id="substep-32-00"></a>
#### 422. 32.00 — Signed Android release artifacts

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 32.00 — Signed Android release artifacts.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\32-mobile-release-and-store-gates.md
Owning section: WP-32.00; explicit anchor: rule-wp-32.00.
Read the common context and WP32 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-32); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-32-01"></a>
#### 423. 32.01 — Release runtime inspection

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 32.01 — Release runtime inspection.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\32-mobile-release-and-store-gates.md
Owning section: WP-32.01; explicit anchor: rule-wp-32.01.
Read the common context and WP32 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-32); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-32-02"></a>
#### 424. 32.02 — Dependency and source rights

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 32.02 — Dependency and source rights.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\32-mobile-release-and-store-gates.md
Owning section: WP-32.02; explicit anchor: rule-wp-32.02.
Read the common context and WP32 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-32); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-32-03"></a>
#### 425. 32.03 — Consumption-only enforcement

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 32.03 — Consumption-only enforcement.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\32-mobile-release-and-store-gates.md
Owning section: WP-32.03; explicit anchor: rule-wp-32.03.
Read the common context and WP32 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-32); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-32-04"></a>
#### 426. 32.04 — Play and direct-channel updates

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 32.04 — Play and direct-channel updates.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\32-mobile-release-and-store-gates.md
Owning section: WP-32.04; explicit anchor: rule-wp-32.04.
Read the common context and WP32 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-32); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-32-05"></a>
#### 427. 32.05 — Physical device and recovery gates

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 32.05 — Physical device and recovery gates.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\32-mobile-release-and-store-gates.md
Owning section: WP-32.05; explicit anchor: rule-wp-32.05.
Read the common context and WP32 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-32); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-32-06"></a>
#### 428. 32.06 — Android scope statement

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 32.06 — Android scope statement.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\32-mobile-release-and-store-gates.md
Owning section: WP-32.06; explicit anchor: rule-wp-32.06.
Read the common context and WP32 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-32); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-32-90"></a>
#### 429. 32.90 — Distribution acceptance

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 32.90 — Distribution acceptance.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\32-mobile-release-and-store-gates.md
Owning section: WP-32.90; explicit anchor: rule-wp-32.90.
Read the common context and WP32 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-32); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="wp-49"></a>
### WP-49 — Web companion Companion

Full WP: [formal source](<C:/MyFile/Projects/ArcForges-Design/docs/planning/work-packages/49-arcchat-web-companion.md>). Reading context: [WP49](reading-map.md#wp-49).

Direct upstream WPs: 26, 48, 52. Complete browser Chat UI against actual Cloud/Harness/device bridge. Apply browser session/CSP/fallback policy rather than Android-only or local-desktop behaviors.

<a id="substep-49-00"></a>
#### 430. 49.00 — React Chat profile and design-system integration

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 49.00 — React Chat profile and design-system integration.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\49-arcchat-web-companion.md
Owning section: WP-49.00; explicit anchor: rule-wp-49.00.
Read the common context and WP49 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-49); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-49-01"></a>
#### 431. 49.01 — Conversation and generated output streams

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 49.01 — Conversation and generated output streams.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\49-arcchat-web-companion.md
Owning section: WP-49.01; explicit anchor: rule-wp-49.01.
Read the common context and WP49 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-49); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-49-02"></a>
#### 432. 49.02 — Tasks, approval and steering

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 49.02 — Tasks, approval and steering.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\49-arcchat-web-companion.md
Owning section: WP-49.02; explicit anchor: rule-wp-49.02.
Read the common context and WP49 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-49); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-49-03"></a>
#### 433. 49.03 — Artifacts and sandboxing

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 49.03 — Artifacts and sandboxing.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\49-arcchat-web-companion.md
Owning section: WP-49.03; explicit anchor: rule-wp-49.03.
Read the common context and WP49 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-49); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-49-04"></a>
#### 434. 49.04 — One-application remote control

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 49.04 — One-application remote control.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\49-arcchat-web-companion.md
Owning section: WP-49.04; explicit anchor: rule-wp-49.04.
Read the common context and WP49 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-49); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-49-05"></a>
#### 435. 49.05 — Offline, degradation and accessibility

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 49.05 — Offline, degradation and accessibility.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\49-arcchat-web-companion.md
Owning section: WP-49.05; explicit anchor: rule-wp-49.05.
Read the common context and WP49 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-49); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-49-06"></a>
#### 436. 49.06 — Performance budgets

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 49.06 — Performance budgets.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\49-arcchat-web-companion.md
Owning section: WP-49.06; explicit anchor: rule-wp-49.06.
Read the common context and WP49 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-49); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-49-90"></a>
#### 437. 49.90 — Verify the owned artifact and real integration

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 49.90 — Verify the owned artifact and real integration.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\49-arcchat-web-companion.md
Owning section: WP-49.90; explicit anchor: rule-wp-49.90.
Read the common context and WP49 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-49); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="wp-50"></a>
### WP-50 — Full-Platform Production Release

Full WP: [formal source](<C:/MyFile/Projects/ArcForges-Design/docs/planning/work-packages/50-full-platform-production-release.md>). Reading context: [WP50](reading-map.md#wp-50).

Direct upstream WPs: 28, 32, 35, 39, 40, 41, 43, 46, 49, 51, 52, 53. Join all required real product, platform, provider, store, operational and commercial evidence. Promote the same tested immutable bytes; no required fixture-backed route may pass as release.

<a id="substep-50-00"></a>
#### 438. 50.00 — Release readiness audit

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 50.00 — Release readiness audit.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\50-full-platform-production-release.md
Owning section: WP-50.00; explicit anchor: rule-wp-50.00.
Read the common context and WP50 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-50); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-50-01"></a>
#### 439. 50.01 — Licence, SBOM and copied-content audit

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 50.01 — Licence, SBOM and copied-content audit.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\50-full-platform-production-release.md
Owning section: WP-50.01; explicit anchor: rule-wp-50.01.
Read the common context and WP50 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-50); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-50-02"></a>
#### 440. 50.02 — Desktop release across three platforms

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 50.02 — Desktop release across three platforms.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\50-full-platform-production-release.md
Owning section: WP-50.02; explicit anchor: rule-wp-50.02.
Read the common context and WP50 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-50); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-50-03"></a>
#### 441. 50.03 — Android release

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 50.03 — Android release.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\50-full-platform-production-release.md
Owning section: WP-50.03; explicit anchor: rule-wp-50.03.
Read the common context and WP50 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-50); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-50-04"></a>
#### 442. 50.04 — Cloud production

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 50.04 — Cloud production.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\50-full-platform-production-release.md
Owning section: WP-50.04; explicit anchor: rule-wp-50.04.
Read the common context and WP50 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-50); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-50-05"></a>
#### 443. 50.05 — Commercial launch

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 50.05 — Commercial launch.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\50-full-platform-production-release.md
Owning section: WP-50.05; explicit anchor: rule-wp-50.05.
Read the common context and WP50 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-50); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-50-06"></a>
#### 444. 50.06 — Node-built Web release set and real-browser verification

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 50.06 — Node-built Web release set and real-browser verification.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\50-full-platform-production-release.md
Owning section: WP-50.06; explicit anchor: rule-wp-50.06.
Read the common context and WP50 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-50); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-50-07"></a>
#### 445. 50.07 — Operational readiness

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 50.07 — Operational readiness.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\50-full-platform-production-release.md
Owning section: WP-50.07; explicit anchor: rule-wp-50.07.
Read the common context and WP50 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-50); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-50-08"></a>
#### 446. 50.08 — Honest release statement

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 50.08 — Honest release statement.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\50-full-platform-production-release.md
Owning section: WP-50.08; explicit anchor: rule-wp-50.08.
Read the common context and WP50 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-50); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

<a id="substep-50-90"></a>
#### 447. 50.90 — Verify the owned artifact and real integration

```text
Read and follow C:\MyFile\Projects\arcforges-implementation-prompt.md.
Execute only ArcForges Substep 50.90 — Verify the owned artifact and real integration.
Owning document: C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\50-full-platform-production-release.md
Owning section: WP-50.90; explicit anchor: rule-wp-50.90.
Read the common context and WP50 entry in C:\MyFile\Projects\Plan\reading-map.md (anchor wp-50); then freshly search all related current Design beyond those entry points.
Include this substep's nested sections and applicable WP-wide obligations; do not implement siblings or advance automatically.
```

End of the active sequence. Acceptance of 50.90 requires the real joined evidence defined by Design; the existence of this list closes no product gate.
