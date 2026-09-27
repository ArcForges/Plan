---
task: PLT.36
status: complete
recorded: 2026-09-28
claimant: w-20260927-cloud-lane
epoch: 1
---

# Principals and the actor chain

- Implementation: [DesktopPlatform PR72](https://github.com/ArcForges/DesktopPlatform/pull/72). Final independently reviewed implementation head is `21771c5c1b31403ebda83cd500bf1a1676b12ec4`; review [5860683836](https://github.com/ArcForges/DesktopPlatform/pull/72#issuecomment-5860683836). Merge `e769b626c559fab3ea1d0a7eb7c0e60ea159bce6` followed all 12 successful retained checks in [CI36357533231](https://github.com/ArcForges/DesktopPlatform/actions/runs/36357533231).
- Outcome: the existing nonpackable Security project owns a validated immutable human principal qualified by RealmId and UserId, device, installation, session, caller instance, and ordered delegated actors with distinct actor, executor and software identities. Local human provenance does not imply a cloud account or authentication. ActorOperation requires a complete chain and forwards the identical instance through layers.
- Boundary evidence: bounded versioned snapshots preserve complete ordered provenance, reject missing, duplicate, unknown and malformed fields, and restore only UntrustedActorChainEvidence. Decoding is not authentication, authorization, integrity, freshness or replay protection. An altered owner remains untrusted after decoding and reserialization; a serialized trusted assertion is rejected.
- Validation: 23 targeted offline tests passed with existing SDK 10.0.401 and locked Release restore/build, using an invocation-only compatibility target retaining admitted ILLink 10.0.11. Committed SDK 10.0.400 remains unchanged for CI. Tests cover CloudUser and LocalHuman chains, mandatory carrier completeness, same-instance layer propagation, in-memory queue and serialized boundary, immutable ordered identities, default/missing realms and identity fields, distinct realms with equal user IDs, truncation, repeated actor/field, unknown enum/version, forged owner, oversized software/snapshot and invalid UTF-16 with valid supplementary Unicode roundtrip.
- Supporting registrations follow the epoch-1 ADP-07 bindings: owned project/test solution and CI membership, licence/runtime/reconciliation/provenance inventories, and immutable dependency receipt successor retaining the existing external versions and closure. Architecture project/API-to-test registration follows the merged GOV.04 gate; no security suppression or checker algorithm change.
- Limits: this is an offline mechanism receipt, not evidence of live process authentication, persistent queues, product enforcement, live Cloud runtime, or the later PLT.38/PLT.57 decision-pipeline integration. Security remains nonpackable and PLT.46 owns its eventual package/real-integration admission. No public package download, toolchain installation, installed-consumer test, native runtime test or new publication tag was performed.

- Existing GOV.04 owner bundled a narrow array-return scanner repair after the new Security API exposed a null namespace in the actual architecture graph. The three null-safe checks and method/local/lambda regressions are recorded under GOV.04; Security behavior and its 23 passing tests were unchanged. The owner reported 61 passing shared semantic tests; the combined final head received independent review.

- Publication: normal main [Publish NuGet36357898681](https://github.com/ArcForges/DesktopPlatform/actions/runs/36357898681), run31 attempt1, succeeded for source `e769b626c559fab3ea1d0a7eb7c0e60ea159bce6`; publisher job108730267755 verified and transferred the six existing packages at `1.0.0-ci.31.1`. Security remains nonpackable and is not among those packages. Original candidate `nuget-candidate-36357898681-1`, artifact10944389731, digest `sha256:33b411e10941d4b975351be8e64d88c6dc9d3b1480758ea82f5d1e9113d9e0ff` is retained as the package-manifest authority. No public download, repack or republish was performed.
