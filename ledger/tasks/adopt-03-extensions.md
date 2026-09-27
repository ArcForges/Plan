---
task: ADOPT.03.extensions
status: complete
recorded: 2026-09-27
claimant: w-20260927-contracts-lane
epoch: 1
---

# Contracts extensions adoption

Frozen Contracts source `b10b2f6f316bf0c007e00632c5442fc102ebbe6e` and Design `722e85641c8afb765dafcab5bc0e84d5a22d5a3c`; [baseline](../adoption/baseline.md#contracts) records original successful CI/security/publication receipts. Main has only Hello/SayHello and ExtensionHost/RenewLease services, accepted WP03.00–.02 records and schema/profile fixtures. Review compared each mapped obligation with actual authored source and available accepted receipts before deciding classifications. No source cleanup, build, download or runtime cycle is part of adoption.

| Task | Classification | Frozen evidence and actual binding | Remaining scope and prerequisites |
|---|---|---|---|
| EXT.02 | inherited with adjustment | Existing `public/proto/arcforges/publicapi/v1/content.proto` contains accepted StructuredValue/ValueList/ValueRecord and CapabilityArguments/Result boundary records; `public/proto/arcforges/extensions/v1/extensions.proto` contains RenewLease. No ValueSchema or full bidirectional boundary exists. | Reuse those authoritative wire records without duplicating or moving their meaning; implement typed extension layer, ValueSchema, bidirectional validation and inward-containment negatives, then AOT evidence. Bind extension additions to existing Sdk.Contracts generation owner and new DesktopPlatform `src/Extensions/ArcForges.Extensions.Contracts` project only through actual inventory/lock additions. Wait CON.05. Public namespace alone does not mean first-party domain leakage; registry04 explicitly permits the boundary gateway. |
| EXT.04 | gap | No complete manifest/workflow/panel schemas or immutable lifecycle implementation; DesktopPlatform Extensions tree absent. | Author validators and staged lifecycle under extension proto and new DesktopPlatform Packaging/Lifecycle ownership, preserving effect fences. Reuse future CON.16 signed fixture keys only as declared substitute; EXT.02/CON.16 start prerequisites remain. No substitute introduced by adoption. |
| EXT.08 | inherited with adjustment | Existing `src/public/dotnet/ArcForges.Sdk.Contracts`, `ArcForges.Sdk.Client/ExtensionLeaseClient.cs` and `ArcForges.Cli/Program.cs` are accepted WP03 groundwork. CLI only validates inventory shape; no PAT/catalog publication. | Map planned src/SDK paths to these existing actual project/package identities; extend generated SDK/validators/tool projections and CLI PAT/catalog/resource flows and validate parity, preserving names/locks. EXT.02/CLOUD.16 start, EXT.06 real-endpoint completion remain. No CLI product acceptance inherited. |

No task is classified as inherited in this slice, so no inherited completion record is added. Accepted groundwork is reused without widening its original acceptance. No unresolved D-001 conflict was found; planned additions bind to existing package owners and must respect actual source/import/lock inventories. All graph prerequisites remain in force.

Validation: actual source/layout, mapped WP41/WP05/WP50 obligation and receipt consistency review; explicit-root Plan ledger check. No new product/runtime/provider/device/browser/GUI/inference/installed-consumer coverage is claimed. Exact reviewed head and merge identity remain in the slice claim and PR history. See [repository facts](../adoption/Contracts.md) and [schema slice](adopt-03-contracts.md) for accepted evidence and later closure ownership.
