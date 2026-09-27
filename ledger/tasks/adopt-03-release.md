---
task: ADOPT.03.release
status: complete
recorded: 2026-09-27
claimant: w-20260927-contracts-lane
epoch: 1
---

# Contracts release adoption

Frozen Contracts source `b10b2f6f316bf0c007e00632c5442fc102ebbe6e` and Design `722e85641c8afb765dafcab5bc0e84d5a22d5a3c`; [baseline](../adoption/baseline.md#contracts) records original successful CI/security/publication receipts. Main has only Hello/SayHello and ExtensionHost/RenewLease services, accepted WP03.00–.02 records and schema/profile fixtures. Review compared each mapped obligation with actual authored source and available accepted receipts before deciding classifications. No source cleanup, build, download or runtime cycle is part of adoption.

| Task | Classification | Frozen evidence and actual binding | Remaining scope and prerequisites |
|---|---|---|---|
| REL.07 | gap | Existing candidate packers and eng/provenance, NOTICE/licence/dependency checks cover bootstrap packages. No eng/release-audit rollup across shipped surfaces or final WP50.01 receipt. | Add eng/release-audit and Design wp50-01-audit reports against actual per-surface receipts. REL.02/.04/.05/.06/.08 prerequisite evidence is absent. No repeated package downloads or build cycles; successful bootstrap publication is not complete release audit. |

No task is classified as inherited in this slice, so no inherited completion record is added. Accepted groundwork is reused without widening its original acceptance. No unresolved D-001 conflict was found; planned additions bind to existing package owners and must respect actual source/import/lock inventories. All graph prerequisites remain in force.

Validation: actual source/layout, mapped WP41/WP05/WP50 obligation and receipt consistency review; explicit-root Plan ledger check. No new product/runtime/provider/device/browser/GUI/inference/installed-consumer coverage is claimed. Exact reviewed head and merge identity remain in the slice claim and PR history. See [repository facts](../adoption/Contracts.md) and [schema slice](adopt-03-contracts.md) for accepted evidence and later closure ownership.
