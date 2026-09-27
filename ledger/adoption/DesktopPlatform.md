# DesktopPlatform repository adoption

Owner: `w-20260927-dgov`, DesktopPlatform integration role epoch2. This repository record joins the independently reviewed and merged fourteen slice records. Ordered plan: reuse frozen baseline and repository facts, reconcile all merged slice classifications, record explicit resolved findings, run ledger consistency, peer review and Plan integration. No product rebuild or source change is part of this record.

## Frozen repository facts

- Frozen main `e5ce94221c13d0014781a760c0865b942350be4d`, reviewed instruction head `1657b2e505dec55d5fb60f485c2f727d7091a722`, [DesktopPlatform PR64](https://github.com/ArcForges/DesktopPlatform/pull/64). No open PR at freeze. [Baseline](baseline.md#desktopplatform) retains all exact source, independent review, main publication and provider receipt identities.
- Retained workflows: `deep-check.yml` Windows CodeQL; `native-abi.yml` Windows x64 native compilation/staging; `package-validation.yml` Ubuntu managed locked restore/format/build/offline architecture and packaging checks; `pr-gate.yml` source/security/design/licence/reference/runtime/reconciliation/provenance and aggregate; `publish-nuget.yml` main original-candidate OIDC publication. No macOS or hosted runtime acceptance inferred.
- All ten baseline package identities at candidate `1.0.0-ci.27.1`: `ArcForges.Build.Policy`, `ArcForges.Native.Abstractions`, `ArcForges.Native.Media`, `ArcForges.Native.Colour`, `ArcForges.Native.Image`, `ArcForges.Native.Otio`, plus `ArcForges.Native.{Media,Colour,Image,Otio}.Runtime.win-x64`. Publication [run36334843593](https://github.com/ArcForges/DesktopPlatform/actions/runs/36334843593) succeeded. These immutable historical packages do not authorize republishing retired families.
- Current shared roots at freeze: `DesktopPlatform.slnx`, `win.slnx`, `Directory.Packages.props`, root/build props and locks, `native/CMakeLists.txt`, `eng/packaging/packages.json`, `eng/policy/**`, `eng/provenance/**`. Actual source inventory includes BuildingBlocks placeholders, a Hello ContentSandbox bootstrap, native probe ABI source, policy/build tooling and architecture/probe tests; no complete platform/application capability is inferred.
- Pins at freeze: Design export `5322d698a1b650a52a5a139d986dd85b00b48581`; vcpkg `36677bbd0b3bf11da7376e62e14bffcc54d2eaeb`; managed versions coverlet.collector10.0.1, NetAnalyzers10.0.401, TestSdk18.10.1, xunit.runner.visualstudio3.1.5 and xunit.v3 4.0.1. No Contracts consumer pin in the central package list. These are historical inputs; producer tasks own reviewed changes.
- Actual source/namespace bindings, required additions, remaining scope and per-task blockers are in the corresponding slices below. Shared append/regenerate/resource protocols remain required. This record neither edits implementation nor changes graph dependencies.

## Complete slice set

- [ADOPT.02.app-composition](../tasks/adopt-02-app-composition.md) — complete, exact review/merge evidence in its claim and PR history.
- [ADOPT.02.assistant](../tasks/adopt-02-assistant.md) — complete, exact review/merge evidence in its claim and PR history.
- [ADOPT.02.cloud](../tasks/adopt-02-cloud.md) — complete, exact review/merge evidence in its claim and PR history.
- [ADOPT.02.device-bridge](../tasks/adopt-02-device-bridge.md) — complete, exact review/merge evidence in its claim and PR history.
- [ADOPT.02.execution](../tasks/adopt-02-execution.md) — complete, exact review/merge evidence in its claim and PR history.
- [ADOPT.02.extensions](../tasks/adopt-02-extensions.md) — complete, exact review/merge evidence in its claim and PR history.
- [ADOPT.02.foundation](../tasks/adopt-02-foundation.md) — complete, exact review/merge evidence in its claim and PR history.
- [ADOPT.02.governance](../tasks/adopt-02-governance.md) — complete, exact review/merge evidence in its claim and PR history.
- [ADOPT.02.native](../tasks/adopt-02-native.md) — complete, exact review/merge evidence in its claim and PR history.
- [ADOPT.02.platform](../tasks/adopt-02-platform.md) — complete, exact review/merge evidence in its claim and PR history.
- [ADOPT.02.policy](../tasks/adopt-02-policy.md) — complete, exact review/merge evidence in its claim and PR history.
- [ADOPT.02.release](../tasks/adopt-02-release.md) — complete, exact review/merge evidence in its claim and PR history.
- [ADOPT.02.runtime-proofs](../tasks/adopt-02-runtime-proofs.md) — complete, exact review/merge evidence in its claim and PR history.
- [ADOPT.02.updater](../tasks/adopt-02-updater.md) — complete, exact review/merge evidence in its claim and PR history.

## Combined classification table

148 tasks: 141 gap, 3 inherited, 4 inherited with adjustment. The only inherited tasks are GOV.01–GOV.03, each with its own inherited ledger record.

| Task | Classification | Slice evidence and binding | Adjustment / remaining scope |
|---|---|---|---|
| APP.01 | gap | [ADOPT.02.app-composition](../tasks/adopt-02-app-composition.md) | See slice for exact obligation, bound scope and remaining evidence. |
| APP.04 | gap | [ADOPT.02.app-composition](../tasks/adopt-02-app-composition.md) | See slice for exact obligation, bound scope and remaining evidence. |
| APP.05 | gap | [ADOPT.02.app-composition](../tasks/adopt-02-app-composition.md) | See slice for exact obligation, bound scope and remaining evidence. |
| APP.06 | gap | [ADOPT.02.app-composition](../tasks/adopt-02-app-composition.md) | See slice for exact obligation, bound scope and remaining evidence. |
| APP.07 | gap | [ADOPT.02.app-composition](../tasks/adopt-02-app-composition.md) | See slice for exact obligation, bound scope and remaining evidence. |
| APP.08 | gap | [ADOPT.02.app-composition](../tasks/adopt-02-app-composition.md) | See slice for exact obligation, bound scope and remaining evidence. |
| AST.01 | gap | [ADOPT.02.assistant](../tasks/adopt-02-assistant.md) | See slice for exact obligation, bound scope and remaining evidence. |
| AST.02 | gap | [ADOPT.02.assistant](../tasks/adopt-02-assistant.md) | See slice for exact obligation, bound scope and remaining evidence. |
| AST.03 | gap | [ADOPT.02.assistant](../tasks/adopt-02-assistant.md) | See slice for exact obligation, bound scope and remaining evidence. |
| AST.04 | gap | [ADOPT.02.assistant](../tasks/adopt-02-assistant.md) | See slice for exact obligation, bound scope and remaining evidence. |
| AST.05 | gap | [ADOPT.02.assistant](../tasks/adopt-02-assistant.md) | See slice for exact obligation, bound scope and remaining evidence. |
| AST.06 | gap | [ADOPT.02.assistant](../tasks/adopt-02-assistant.md) | See slice for exact obligation, bound scope and remaining evidence. |
| AST.07 | gap | [ADOPT.02.assistant](../tasks/adopt-02-assistant.md) | See slice for exact obligation, bound scope and remaining evidence. |
| AST.08 | gap | [ADOPT.02.assistant](../tasks/adopt-02-assistant.md) | See slice for exact obligation, bound scope and remaining evidence. |
| AST.09 | gap | [ADOPT.02.assistant](../tasks/adopt-02-assistant.md) | See slice for exact obligation, bound scope and remaining evidence. |
| AST.10 | gap | [ADOPT.02.assistant](../tasks/adopt-02-assistant.md) | See slice for exact obligation, bound scope and remaining evidence. |
| AST.11 | gap | [ADOPT.02.assistant](../tasks/adopt-02-assistant.md) | See slice for exact obligation, bound scope and remaining evidence. |
| AST.12 | gap | [ADOPT.02.assistant](../tasks/adopt-02-assistant.md) | See slice for exact obligation, bound scope and remaining evidence. |
| AST.13 | gap | [ADOPT.02.assistant](../tasks/adopt-02-assistant.md) | See slice for exact obligation, bound scope and remaining evidence. |
| AST.14 | gap | [ADOPT.02.assistant](../tasks/adopt-02-assistant.md) | See slice for exact obligation, bound scope and remaining evidence. |
| AST.15 | gap | [ADOPT.02.assistant](../tasks/adopt-02-assistant.md) | See slice for exact obligation, bound scope and remaining evidence. |
| AST.16 | gap | [ADOPT.02.assistant](../tasks/adopt-02-assistant.md) | See slice for exact obligation, bound scope and remaining evidence. |
| AST.17 | gap | [ADOPT.02.assistant](../tasks/adopt-02-assistant.md) | See slice for exact obligation, bound scope and remaining evidence. |
| AST.18 | gap | [ADOPT.02.assistant](../tasks/adopt-02-assistant.md) | See slice for exact obligation, bound scope and remaining evidence. |
| AST.19 | gap | [ADOPT.02.assistant](../tasks/adopt-02-assistant.md) | See slice for exact obligation, bound scope and remaining evidence. |
| AST.20 | gap | [ADOPT.02.assistant](../tasks/adopt-02-assistant.md) | See slice for exact obligation, bound scope and remaining evidence. |
| AST.21 | gap | [ADOPT.02.assistant](../tasks/adopt-02-assistant.md) | See slice for exact obligation, bound scope and remaining evidence. |
| AST.22 | gap | [ADOPT.02.assistant](../tasks/adopt-02-assistant.md) | See slice for exact obligation, bound scope and remaining evidence. |
| CLOUD.18 | gap | [ADOPT.02.cloud](../tasks/adopt-02-cloud.md) | See slice for exact obligation, bound scope and remaining evidence. |
| CLOUD.38 | gap | [ADOPT.02.cloud](../tasks/adopt-02-cloud.md) | See slice for exact obligation, bound scope and remaining evidence. |
| DEV.03 | gap | [ADOPT.02.device-bridge](../tasks/adopt-02-device-bridge.md) | See slice for exact obligation, bound scope and remaining evidence. |
| DEV.05 | gap | [ADOPT.02.device-bridge](../tasks/adopt-02-device-bridge.md) | See slice for exact obligation, bound scope and remaining evidence. |
| DEV.14 | gap | [ADOPT.02.device-bridge](../tasks/adopt-02-device-bridge.md) | See slice for exact obligation, bound scope and remaining evidence. |
| EXE.01 | gap | [ADOPT.02.execution](../tasks/adopt-02-execution.md) | See slice for exact obligation, bound scope and remaining evidence. |
| EXE.02 | gap | [ADOPT.02.execution](../tasks/adopt-02-execution.md) | See slice for exact obligation, bound scope and remaining evidence. |
| EXE.03 | gap | [ADOPT.02.execution](../tasks/adopt-02-execution.md) | See slice for exact obligation, bound scope and remaining evidence. |
| EXE.04 | gap | [ADOPT.02.execution](../tasks/adopt-02-execution.md) | See slice for exact obligation, bound scope and remaining evidence. |
| EXE.05 | gap | [ADOPT.02.execution](../tasks/adopt-02-execution.md) | See slice for exact obligation, bound scope and remaining evidence. |
| EXE.06 | gap | [ADOPT.02.execution](../tasks/adopt-02-execution.md) | See slice for exact obligation, bound scope and remaining evidence. |
| EXE.07 | gap | [ADOPT.02.execution](../tasks/adopt-02-execution.md) | See slice for exact obligation, bound scope and remaining evidence. |
| EXE.08 | gap | [ADOPT.02.execution](../tasks/adopt-02-execution.md) | See slice for exact obligation, bound scope and remaining evidence. |
| EXE.09 | gap | [ADOPT.02.execution](../tasks/adopt-02-execution.md) | See slice for exact obligation, bound scope and remaining evidence. |
| EXT.00 | gap | [ADOPT.02.extensions](../tasks/adopt-02-extensions.md) | See slice for exact obligation, bound scope and remaining evidence. |
| EXT.01 | gap | [ADOPT.02.extensions](../tasks/adopt-02-extensions.md) | See slice for exact obligation, bound scope and remaining evidence. |
| EXT.03 | gap | [ADOPT.02.extensions](../tasks/adopt-02-extensions.md) | See slice for exact obligation, bound scope and remaining evidence. |
| EXT.05 | gap | [ADOPT.02.extensions](../tasks/adopt-02-extensions.md) | See slice for exact obligation, bound scope and remaining evidence. |
| EXT.07 | gap | [ADOPT.02.extensions](../tasks/adopt-02-extensions.md) | See slice for exact obligation, bound scope and remaining evidence. |
| EXT.09 | gap | [ADOPT.02.extensions](../tasks/adopt-02-extensions.md) | See slice for exact obligation, bound scope and remaining evidence. |
| EXT.90 | gap | [ADOPT.02.extensions](../tasks/adopt-02-extensions.md) | See slice for exact obligation, bound scope and remaining evidence. |
| FND.01 | gap | [ADOPT.02.foundation](../tasks/adopt-02-foundation.md) | See slice for exact obligation, bound scope and remaining evidence. |
| FND.02 | gap | [ADOPT.02.foundation](../tasks/adopt-02-foundation.md) | See slice for exact obligation, bound scope and remaining evidence. |
| FND.03 | gap | [ADOPT.02.foundation](../tasks/adopt-02-foundation.md) | See slice for exact obligation, bound scope and remaining evidence. |
| FND.04 | gap | [ADOPT.02.foundation](../tasks/adopt-02-foundation.md) | See slice for exact obligation, bound scope and remaining evidence. |
| FND.05 | gap | [ADOPT.02.foundation](../tasks/adopt-02-foundation.md) | See slice for exact obligation, bound scope and remaining evidence. |
| FND.06 | gap | [ADOPT.02.foundation](../tasks/adopt-02-foundation.md) | See slice for exact obligation, bound scope and remaining evidence. |
| FND.07 | gap | [ADOPT.02.foundation](../tasks/adopt-02-foundation.md) | See slice for exact obligation, bound scope and remaining evidence. |
| GOV.01 | inherited | [ADOPT.02.governance](../tasks/adopt-02-governance.md) | See slice for exact obligation, bound scope and remaining evidence. |
| GOV.02 | inherited | [ADOPT.02.governance](../tasks/adopt-02-governance.md) | See slice for exact obligation, bound scope and remaining evidence. |
| GOV.03 | inherited | [ADOPT.02.governance](../tasks/adopt-02-governance.md) | See slice for exact obligation, bound scope and remaining evidence. |
| GOV.04 | inherited with adjustment | [ADOPT.02.governance](../tasks/adopt-02-governance.md) | See slice for exact obligation, bound scope and remaining evidence. |
| GOV.13 | gap | [ADOPT.02.governance](../tasks/adopt-02-governance.md) | See slice for exact obligation, bound scope and remaining evidence. |
| GOV.14 | inherited with adjustment | [ADOPT.02.governance](../tasks/adopt-02-governance.md) | See slice for exact obligation, bound scope and remaining evidence. |
| GOV.15 | gap | [ADOPT.02.governance](../tasks/adopt-02-governance.md) | See slice for exact obligation, bound scope and remaining evidence. |
| GOV.17 | gap | [ADOPT.02.governance](../tasks/adopt-02-governance.md) | See slice for exact obligation, bound scope and remaining evidence. |
| GOV.18 | gap | [ADOPT.02.governance](../tasks/adopt-02-governance.md) | See slice for exact obligation, bound scope and remaining evidence. |
| NAT.01 | gap | [ADOPT.02.native](../tasks/adopt-02-native.md) | See slice for exact obligation, bound scope and remaining evidence. |
| NAT.03 | gap | [ADOPT.02.native](../tasks/adopt-02-native.md) | See slice for exact obligation, bound scope and remaining evidence. |
| NAT.05 | gap | [ADOPT.02.native](../tasks/adopt-02-native.md) | Recorded conflict resolved by Design PR70 (5a5a955) and generated Plan PR28; current WP13/ADP-10 governs, no probe/source acceptance inferred. |
| NAT.06 | gap | [ADOPT.02.native](../tasks/adopt-02-native.md) | Recorded conflict resolved by Design PR70 (5a5a955) and generated Plan PR28; current WP13/ADP-10 governs, no probe/source acceptance inferred. |
| NAT.11 | gap | [ADOPT.02.native](../tasks/adopt-02-native.md) | See slice for exact obligation, bound scope and remaining evidence. |
| NAT.13 | gap | [ADOPT.02.native](../tasks/adopt-02-native.md) | See slice for exact obligation, bound scope and remaining evidence. |
| NAT.14 | gap | [ADOPT.02.native](../tasks/adopt-02-native.md) | See slice for exact obligation, bound scope and remaining evidence. |
| NAT.22 | inherited with adjustment | [ADOPT.02.native](../tasks/adopt-02-native.md) | See slice for exact obligation, bound scope and remaining evidence. |
| NAT.24 | gap | [ADOPT.02.native](../tasks/adopt-02-native.md) | See slice for exact obligation, bound scope and remaining evidence. |
| NAT.25 | gap | [ADOPT.02.native](../tasks/adopt-02-native.md) | See slice for exact obligation, bound scope and remaining evidence. |
| NAT.28 | inherited with adjustment | [ADOPT.02.native](../tasks/adopt-02-native.md) | See slice for exact obligation, bound scope and remaining evidence. |
| NAT.29 | gap | [ADOPT.02.native](../tasks/adopt-02-native.md) | See slice for exact obligation, bound scope and remaining evidence. |
| NAT.30 | gap | [ADOPT.02.native](../tasks/adopt-02-native.md) | See slice for exact obligation, bound scope and remaining evidence. |
| PLT.01 | gap | [ADOPT.02.platform](../tasks/adopt-02-platform.md) | See slice for exact obligation, bound scope and remaining evidence. |
| PLT.02 | gap | [ADOPT.02.platform](../tasks/adopt-02-platform.md) | See slice for exact obligation, bound scope and remaining evidence. |
| PLT.03 | gap | [ADOPT.02.platform](../tasks/adopt-02-platform.md) | See slice for exact obligation, bound scope and remaining evidence. |
| PLT.04 | gap | [ADOPT.02.platform](../tasks/adopt-02-platform.md) | See slice for exact obligation, bound scope and remaining evidence. |
| PLT.05 | gap | [ADOPT.02.platform](../tasks/adopt-02-platform.md) | See slice for exact obligation, bound scope and remaining evidence. |
| PLT.06 | gap | [ADOPT.02.platform](../tasks/adopt-02-platform.md) | See slice for exact obligation, bound scope and remaining evidence. |
| PLT.07 | gap | [ADOPT.02.platform](../tasks/adopt-02-platform.md) | See slice for exact obligation, bound scope and remaining evidence. |
| PLT.08 | gap | [ADOPT.02.platform](../tasks/adopt-02-platform.md) | See slice for exact obligation, bound scope and remaining evidence. |
| PLT.09 | gap | [ADOPT.02.platform](../tasks/adopt-02-platform.md) | See slice for exact obligation, bound scope and remaining evidence. |
| PLT.10 | gap | [ADOPT.02.platform](../tasks/adopt-02-platform.md) | See slice for exact obligation, bound scope and remaining evidence. |
| PLT.11 | gap | [ADOPT.02.platform](../tasks/adopt-02-platform.md) | See slice for exact obligation, bound scope and remaining evidence. |
| PLT.12 | gap | [ADOPT.02.platform](../tasks/adopt-02-platform.md) | See slice for exact obligation, bound scope and remaining evidence. |
| PLT.13 | gap | [ADOPT.02.platform](../tasks/adopt-02-platform.md) | See slice for exact obligation, bound scope and remaining evidence. |
| PLT.14 | gap | [ADOPT.02.platform](../tasks/adopt-02-platform.md) | See slice for exact obligation, bound scope and remaining evidence. |
| PLT.15 | gap | [ADOPT.02.platform](../tasks/adopt-02-platform.md) | See slice for exact obligation, bound scope and remaining evidence. |
| PLT.16 | gap | [ADOPT.02.platform](../tasks/adopt-02-platform.md) | See slice for exact obligation, bound scope and remaining evidence. |
| PLT.17 | gap | [ADOPT.02.platform](../tasks/adopt-02-platform.md) | See slice for exact obligation, bound scope and remaining evidence. |
| PLT.18 | gap | [ADOPT.02.platform](../tasks/adopt-02-platform.md) | See slice for exact obligation, bound scope and remaining evidence. |
| PLT.19 | gap | [ADOPT.02.platform](../tasks/adopt-02-platform.md) | See slice for exact obligation, bound scope and remaining evidence. |
| PLT.20 | gap | [ADOPT.02.platform](../tasks/adopt-02-platform.md) | See slice for exact obligation, bound scope and remaining evidence. |
| PLT.21 | gap | [ADOPT.02.platform](../tasks/adopt-02-platform.md) | See slice for exact obligation, bound scope and remaining evidence. |
| PLT.22 | gap | [ADOPT.02.platform](../tasks/adopt-02-platform.md) | See slice for exact obligation, bound scope and remaining evidence. |
| PLT.23 | gap | [ADOPT.02.platform](../tasks/adopt-02-platform.md) | See slice for exact obligation, bound scope and remaining evidence. |
| PLT.24 | gap | [ADOPT.02.platform](../tasks/adopt-02-platform.md) | See slice for exact obligation, bound scope and remaining evidence. |
| PLT.25 | gap | [ADOPT.02.platform](../tasks/adopt-02-platform.md) | See slice for exact obligation, bound scope and remaining evidence. |
| PLT.26 | gap | [ADOPT.02.platform](../tasks/adopt-02-platform.md) | See slice for exact obligation, bound scope and remaining evidence. |
| PLT.27 | gap | [ADOPT.02.platform](../tasks/adopt-02-platform.md) | See slice for exact obligation, bound scope and remaining evidence. |
| PLT.28 | gap | [ADOPT.02.platform](../tasks/adopt-02-platform.md) | See slice for exact obligation, bound scope and remaining evidence. |
| PLT.29 | gap | [ADOPT.02.platform](../tasks/adopt-02-platform.md) | See slice for exact obligation, bound scope and remaining evidence. |
| PLT.30 | gap | [ADOPT.02.platform](../tasks/adopt-02-platform.md) | See slice for exact obligation, bound scope and remaining evidence. |
| PLT.31 | gap | [ADOPT.02.platform](../tasks/adopt-02-platform.md) | See slice for exact obligation, bound scope and remaining evidence. |
| PLT.32 | gap | [ADOPT.02.platform](../tasks/adopt-02-platform.md) | See slice for exact obligation, bound scope and remaining evidence. |
| PLT.33 | gap | [ADOPT.02.platform](../tasks/adopt-02-platform.md) | See slice for exact obligation, bound scope and remaining evidence. |
| PLT.34 | gap | [ADOPT.02.platform](../tasks/adopt-02-platform.md) | See slice for exact obligation, bound scope and remaining evidence. |
| PLT.35 | gap | [ADOPT.02.platform](../tasks/adopt-02-platform.md) | See slice for exact obligation, bound scope and remaining evidence. |
| PLT.36 | gap | [ADOPT.02.platform](../tasks/adopt-02-platform.md) | See slice for exact obligation, bound scope and remaining evidence. |
| PLT.37 | gap | [ADOPT.02.platform](../tasks/adopt-02-platform.md) | See slice for exact obligation, bound scope and remaining evidence. |
| PLT.38 | gap | [ADOPT.02.platform](../tasks/adopt-02-platform.md) | See slice for exact obligation, bound scope and remaining evidence. |
| PLT.39 | gap | [ADOPT.02.platform](../tasks/adopt-02-platform.md) | See slice for exact obligation, bound scope and remaining evidence. |
| PLT.40 | gap | [ADOPT.02.platform](../tasks/adopt-02-platform.md) | See slice for exact obligation, bound scope and remaining evidence. |
| PLT.41 | gap | [ADOPT.02.platform](../tasks/adopt-02-platform.md) | See slice for exact obligation, bound scope and remaining evidence. |
| PLT.42 | gap | [ADOPT.02.platform](../tasks/adopt-02-platform.md) | See slice for exact obligation, bound scope and remaining evidence. |
| PLT.43 | gap | [ADOPT.02.platform](../tasks/adopt-02-platform.md) | See slice for exact obligation, bound scope and remaining evidence. |
| PLT.44 | gap | [ADOPT.02.platform](../tasks/adopt-02-platform.md) | See slice for exact obligation, bound scope and remaining evidence. |
| PLT.45 | gap | [ADOPT.02.platform](../tasks/adopt-02-platform.md) | See slice for exact obligation, bound scope and remaining evidence. |
| PLT.46 | gap | [ADOPT.02.platform](../tasks/adopt-02-platform.md) | See slice for exact obligation, bound scope and remaining evidence. |
| PLT.47 | gap | [ADOPT.02.platform](../tasks/adopt-02-platform.md) | See slice for exact obligation, bound scope and remaining evidence. |
| PLT.48 | gap | [ADOPT.02.platform](../tasks/adopt-02-platform.md) | See slice for exact obligation, bound scope and remaining evidence. |
| PLT.49 | gap | [ADOPT.02.platform](../tasks/adopt-02-platform.md) | See slice for exact obligation, bound scope and remaining evidence. |
| PLT.50 | gap | [ADOPT.02.platform](../tasks/adopt-02-platform.md) | See slice for exact obligation, bound scope and remaining evidence. |
| PLT.51 | gap | [ADOPT.02.platform](../tasks/adopt-02-platform.md) | See slice for exact obligation, bound scope and remaining evidence. |
| PLT.52 | gap | [ADOPT.02.platform](../tasks/adopt-02-platform.md) | See slice for exact obligation, bound scope and remaining evidence. |
| PLT.53 | gap | [ADOPT.02.platform](../tasks/adopt-02-platform.md) | See slice for exact obligation, bound scope and remaining evidence. |
| PLT.54 | gap | [ADOPT.02.platform](../tasks/adopt-02-platform.md) | See slice for exact obligation, bound scope and remaining evidence. |
| PLT.57 | gap | [ADOPT.02.platform](../tasks/adopt-02-platform.md) | See slice for exact obligation, bound scope and remaining evidence. |
| POL.09 | gap | [ADOPT.02.policy](../tasks/adopt-02-policy.md) | See slice for exact obligation, bound scope and remaining evidence. |
| PRF.04 | gap | [ADOPT.02.runtime-proofs](../tasks/adopt-02-runtime-proofs.md) | See slice for exact obligation, bound scope and remaining evidence. |
| PRF.05 | gap | [ADOPT.02.runtime-proofs](../tasks/adopt-02-runtime-proofs.md) | See slice for exact obligation, bound scope and remaining evidence. |
| PRF.06 | gap | [ADOPT.02.runtime-proofs](../tasks/adopt-02-runtime-proofs.md) | See slice for exact obligation, bound scope and remaining evidence. |
| PRF.09 | gap | [ADOPT.02.runtime-proofs](../tasks/adopt-02-runtime-proofs.md) | See slice for exact obligation, bound scope and remaining evidence. |
| REL.10 | gap | [ADOPT.02.release](../tasks/adopt-02-release.md) | See slice for exact obligation, bound scope and remaining evidence. |
| REL.11 | gap | [ADOPT.02.release](../tasks/adopt-02-release.md) | See slice for exact obligation, bound scope and remaining evidence. |
| UPD.01 | gap | [ADOPT.02.updater](../tasks/adopt-02-updater.md) | See slice for exact obligation, bound scope and remaining evidence. |
| UPD.02 | gap | [ADOPT.02.updater](../tasks/adopt-02-updater.md) | See slice for exact obligation, bound scope and remaining evidence. |
| UPD.03 | gap | [ADOPT.02.updater](../tasks/adopt-02-updater.md) | See slice for exact obligation, bound scope and remaining evidence. |
| UPD.04 | gap | [ADOPT.02.updater](../tasks/adopt-02-updater.md) | See slice for exact obligation, bound scope and remaining evidence. |
| UPD.05 | gap | [ADOPT.02.updater](../tasks/adopt-02-updater.md) | See slice for exact obligation, bound scope and remaining evidence. |
| UPD.06 | gap | [ADOPT.02.updater](../tasks/adopt-02-updater.md) | See slice for exact obligation, bound scope and remaining evidence. |
| UPD.07 | gap | [ADOPT.02.updater](../tasks/adopt-02-updater.md) | See slice for exact obligation, bound scope and remaining evidence. |
| UPD.08 | gap | [ADOPT.02.updater](../tasks/adopt-02-updater.md) | See slice for exact obligation, bound scope and remaining evidence. |

## Findings and limits

The native slice originally raised NAT.05's stale four-probe count and NAT.06's retired-media input wording. Design PR70, merged `5a5a9551c8d0a2e5d9d6196a4344d31d832523f3`, and regenerated Plan PR28 resolve those findings against current WP13 and ADP-10. This repository record records the adoption adjustment to **gap** for both tasks: their actual obligations and evidence remain unimplemented, and all current graph prerequisites apply. No unresolved architecture conflict from the slice set remains. Future task implementation can still discover a concrete conflict requiring the normal decision process.

GOV.17/GOV.18 perform native/policy source cleanup separately and remain open; the old source bindings are approved migration inputs, not accepted current-family behavior. Foundation and platform implementation work after freeze is not included in adoption inheritance. A completed slice only opens that repository/lane's tasks; no whole-repository or stage barrier is imposed.

Validation reused original retained CI/provider receipts and inspected source inventories and all merged slice records. The explicit-root Plan ledger consistency check passes. No builds, downloads, runtime/device/browser/live-service/inference tests were performed for this adoption record. Baseline publication establishes its packages only; it is not application, native capability or commercial acceptance. No substitutes introduced. Exact review and future merge identities belong to the claim and this PR history.
