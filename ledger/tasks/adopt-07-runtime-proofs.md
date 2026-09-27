---
task: ADOPT.07.runtime-proofs
status: complete
recorded: 2026-09-27
claimant: w-20260927-cloud-lane
epoch: 1
---

# Cloud runtime-proof adoption

Reviewed by the Cloud integration owner at role epoch 2 against the [frozen baseline](../adoption/baseline.md#cloud), Cloud source `60c5c4288b126c81a09fa5d1944671e9acb87495` and Design `722e85641c8afb765dafcab5bc0e84d5a22d5a3c`. The task prompt, WP-06.04 and WP-06 section 8 item 9 were compared with the source inventory and original publication evidence. Adoption does not execute PRF.07.

| Task | Classification | Evidence and bound scope | Remaining scope | Conflicts / blockers |
|---|---|---|---|---|
| PRF.07 | gap | `src/ArcForges.Cloud/Program.cs` and `HelloEndpoint.cs` implement an anonymous bounded Hello/health host; `Dockerfile` publishes Linux x64 Native AOT into pinned chiseled Ubuntu as non-root; `worker/index.ts`, `worker/router.ts` and `wrangler.json` provide Container ingress. Bind the planned host path to existing `src/ArcForges.Cloud/**`, preserving assembly/package identity; verification additions belong in `eng/verification/**`. Explicit implementation adjustment: real private bindings require coordinated `worker/**`, `wrangler.json`, root dependency locks and CI/provenance inventories under the existing Cloud owner protocols, rather than a second host. | Entire WP-06.04 foundation proof beyond the reusable bootstrap: private named-plan D1 adapter and guarded rollback, exact int64/decimal, DO/Queue/R2 foundation, explicit session/CSRF/revoke, bounded checkpoint/restart and real provider-boundary evidence. Preserve zero trim/AOT diagnostics and continuous allowed main compilation/publication. | No contradictory product implementation found. Published current Contracts schemas/vectors must be checked at implementation; the baseline consumer still pins `1.0.0-ci.74.1`. Dependency readiness alone does not prove the named contract inputs exist. |

## Evidence and limitations

- Cloud [PR #22](https://github.com/ArcForges/Cloud/pull/22) reviewed head `4f37ac16ec70ca421bc227c0c448fb424e5df53f`, merge `60c5c4288b126c81a09fa5d1944671e9acb87495`; original [main run 36335115598](https://github.com/ArcForges/Cloud/actions/runs/36335115598) passed, including the AOT container/Worker candidate and deployment.
- Candidate `cloud-0.1.0-ci.66.1` and original deployment receipt are recorded in the frozen baseline. This proves the deployed bootstrap candidate, not D1/Queue/R2 or authenticated foundation behavior. The Container Durable Object is not evidence for business coordination/checkpoint semantics.
- `wrangler.json` has only `CLOUD_CONTAINER` and the Hello rate limiter; it has no D1, Queue or R2 bindings. The C# source inventory contains no storage, session or CSRF adapter. No full PRF.07 inheritance is claimed, and no inherited task record is created.
- Validation: source, task/obligation, workflow and frozen-receipt review; Plan consistency check. No builds, new provider probes, downloads or runtime tests. Existing bootstrap consumer probes are not registered substitutes for the missing foundation. VG-06 remains open.
- Ledger PR exact-head review and merge are retained by the PR and claim audit trail; this record opens only PRF.07 under its normal prerequisites.
