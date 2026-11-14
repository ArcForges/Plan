# V2 baseline and readiness

Design baseline main: `ArcForges/ArcForges-Design@62172622550fff73a553135ca178f9b7117c9cbd`. Plan baseline main: `ArcForges/Plan@742ed2660c5e934e1df86f90e54198b3a199e2b1`. Full implementation/consumer commits and open dependency PRs are in the Design source audit; all product sources are read-only during this migration.

The new graph contains 39 tasks in nine stages. The first eligible task is AFV2-BASE-01. AFV2-MXC-01 is an independent source/artifact-admission root; serial execution still follows the authorized range and file order. Native profile admission is a hard dependency of Core replacement. Hosting/entitlement/commerce precede final Dashboard integration because subscription pages need actual APIs.

No V2 task is delivered by the design migration. Native engine experiments, PostgreSQL guarded upgrade, live provider qualification and final browser/runtime acceptance have not been run here. Native host checks for documentation PRs remain separately required. Do not interpret successfully generated documents as product validation.

All retired plan facts live in the [frozen baseline](history/v1-20261114-notice.md). H-01/H-02 name designated host access. H-03 concerns actual deployed-state and backup/admission authority. H-04/H-05 concern official external activation, not new architecture choices. See [acceptance register](acceptance-register.md).
