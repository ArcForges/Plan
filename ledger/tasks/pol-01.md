---
task: POL.01
status: complete
recorded: 2026-10-06
claimant: w-codex-20261006-policy
epoch: 1
---

# Structural policy boundaries (WP-44.00)

Implementation is merged, independently reviewed, validated and normally published. This record covers only the four structural policy boundaries, not configuration activation or runtime policy decisions. POL.01 has no completion prerequisites.

## Evidence

- **Authoritative scope.** The reviewed production prerequisite repairs [Design #254](https://github.com/ArcForges/ArcForges-Design/pull/254) and [Plan #344](https://github.com/ArcForges/Plan/pull/344), followed by [Design #255](https://github.com/ArcForges/ArcForges-Design/pull/255) and [Plan #345](https://github.com/ArcForges/Plan/pull/345), bind the actual evaluated architecture tests, module marker, Docker source inclusion and immutable policy/provenance successors. No generated contract or other module's decision implementation was replaced.
- **Source delivery.** [Cloud #66](https://github.com/ArcForges/Cloud/pull/66) merged as `9ba0614e43c76ba00cf2e3c59372c7318732ff93` at independently reviewed head `082a48a99937aaef86ba85f6eb9f883563212a2d`, under Cloud integration owner fencing. The [independent review](https://github.com/ArcForges/Cloud/pull/66#issuecomment-6021918923) approves that exact head for POL.01 epoch 1. Independence is between workers using the same GitHub account.
- **Actual enforcement.** The existing production compilation evaluation now runs `PolicyBoundaryGuard` against every evaluated source syntax node. Its semantic type traversal covers aliases, member symbols, generic arguments, arrays, pointers and containing types. Policy/Configuration remain separate from entitlement decisions, user settings, health and ingress/data-plane types in both directions. The actual legacy root `HealthStatus` and entitlement grant-port types are classified explicitly; neutral owner ports and host composition remain usable. This is a failing semantic architecture gate, not a runtime permission flag.
- **Relevant review repair.** Header-only record declarations exposed a missing declared-type owner. The implementation resolves the nearest declared type rather than attributing a record header to the parent namespace. Independent review also identified the equivalent delegate-header gap; the final head handles base-type and delegate declarations and includes isolated delegate return/parameter regression fixtures.
- **Component evidence, claimant-reported.** All 15 `PolicyBoundaryTests` passed with zero failures/skips after the final delegate fix. The four isolated boundary cases each exercise a record primary constructor, inheritance-only declaration, nested nullable generic/array signature and delegate-only signature. Additional negative cases exercise combined member/alias/generic/array paths, reciprocal boundaries, real root HealthStatus and entitlement grant ports. The neutral composition case passes. No external dependency was mocked for this semantic enforcement.
- **Applicable hosted CI.** [PR CI run 37504793935](https://github.com/ArcForges/Cloud/actions/runs/37504793935) passed all applicable latest-head source checks on Windows/Linux, evaluated architecture/dependency/licence/provenance gates, CodeQL, actual Native AOT image/Worker build and artifact verification. Live Cloudflare proof was skipped by the established validation policy; it is not deployment evidence. Local provenance/NOTICE checks and all 18 dependency-policy cases also passed.
- **Immutable artifact admission.** The successor `cloud-release-r38` and task-owned runtime/Worker records and `pol-01-r1` admission receipt retain previous history and the patched GOV.22 package closure. They bind the new shipped marker and Docker source inclusion to actual source inputs, while preserving unchanged Worker hashes/inputs. No package coordinate, integrity, licence or framework pin was changed.
- **Normal publication.** [Main CI run 37506025024](https://github.com/ArcForges/Cloud/actions/runs/37506025024), bound to merge `9ba0614e43c76ba00cf2e3c59372c7318732ff93`, completed successfully. Its Native AOT image/Worker build, artifact Verify and normal Deploy Cloudflare jobs all succeeded. This is evidence of the existing sealed-candidate publication/deployment pipeline, not mocked component evidence or proof-environment acceptance. Established proof-environment jobs were skipped; no independent live acceptance is claimed.

## Limits and follow-up ownership

The gate proves structural separation of the evaluated production source. It does not prove OS isolation, a real provider, runtime entitlement evaluation or whole-series end-to-end commercial acceptance. No production route or data change is part of this task; `workers.dev` remains disabled. Configuration validation, persistent two-person approval, atomic activation and verified catalogue authority belong to POL.02, and are continuing separately.

Cloud integration owns fenced source merging; the claimant owns normal publication verification and this ledger; the Plan integration owner merges the independently reviewed final ledger. No interactive login or account authorization is a known blocker.
