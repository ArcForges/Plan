---
task: ADOPT.03.governance
status: complete
recorded: 2026-09-27
claimant: w-20260927-contracts-lane
epoch: 1
---

# Contracts governance adoption

Frozen Contracts source `b10b2f6f316bf0c007e00632c5442fc102ebbe6e` and Design `722e85641c8afb765dafcab5bc0e84d5a22d5a3c`; [baseline](../adoption/baseline.md#contracts) records original successful CI/security/publication receipts. Main has only Hello/SayHello and ExtensionHost/RenewLease services, accepted WP03.00–.02 records and schema/profile fixtures. Review compared each mapped obligation with actual authored source and available accepted receipts before deciding classifications. No source cleanup, build, download or runtime cycle is part of adoption.

| Task | Classification | Frozen evidence and actual binding | Remaining scope and prerequisites |
|---|---|---|---|
| GOV.05 | inherited with adjustment | Existing `eng/check_serialization.py`, `eng/check_contract_access.mjs`, `eng/check_naming.py`, generated baselines and StructureTests enforce accepted WP03 posture. No reusable GOV.04 engine or complete Contracts ArchitectureTests exists. | Reuse accepted serialization/import/licence/naming checks while implementing full shared-engine layering/banned-category/contract policy and per-assertion negatives. Bind new tests/ArchitectureTests and eng/policy/exceptions.json; any producer/package integration beyond declared scope needs reviewed planning repair. Wait GOV.04/CON.90/CON.23; no source cleanup here. |
| GOV.16 | gap | No complete operation catalogue, reachability matrix or tests/AuthorizationPolicyTests; Hello/RenewLease cannot prove all actors. | Add new AuthorizationPolicyTests over CON.18 metadata with every effective AZ-04 field, hostile actor chain and identity boundary; completion uses CLOUD.11/PLT.38 real bindings, not fixture approval. No customer service principal or Organization authority. |

No task is classified as inherited in this slice, so no inherited completion record is added. Accepted groundwork is reused without widening its original acceptance. No unresolved D-001 conflict was found; planned additions bind to existing package owners and must respect actual source/import/lock inventories. All graph prerequisites remain in force.

Validation: actual source/layout, mapped WP41/WP05/WP50 obligation and receipt consistency review; explicit-root Plan ledger check. No new product/runtime/provider/device/browser/GUI/inference/installed-consumer coverage is claimed. Exact reviewed head and merge identity remain in the slice claim and PR history. See [repository facts](../adoption/Contracts.md) and [schema slice](adopt-03-contracts.md) for accepted evidence and later closure ownership.

