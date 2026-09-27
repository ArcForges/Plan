---
task: ADOPT.05.runtime-proofs
status: complete
recorded: 2026-09-27
claimant: w-20260927-arcscope-lane
epoch: 1
---

## Evidence and classification

Reviewed against Design `722e85641c8afb765dafcab5bc0e84d5a22d5a3c`, the PRF.02 prompt and WP-06.00 (ArcScope host only), including the WP-06 section 8 item 9 continuous-main contribution. The frozen source is ArcScope `a6899eddc4da7cf338d1a1404f1c0c1b8acc546d`; [baseline](../adoption/baseline.md#arcscope) records the independently reviewed instruction PR and immutable candidate `v0.1.0-ci.37.1`.

| Task | Classification | Reviewed evidence | Bound write scope | Remaining scope | Conflicts / blockers |
|---|---|---|---|---|---|
| PRF.02 | inherited with adjustment | `src/ArcForges.ArcScope/ArcForges.ArcScope.csproj` enables Native AOT and treats AOT/link warnings as errors. `.github/workflows/ci.yml` compiles and packages win-x64, win-arm64 and linux-x64 on every main push. [Main run 36335032606](https://github.com/ArcForges/ArcScope/actions/runs/36335032606) succeeded for all three Native jobs, static/security gates and portable publication. This preserves the existing compilation/package mechanism, not completed runtime proof. | Existing `src/ArcForges.ArcScope/**` host and `ArcScope.slnx`; append exact producer package references through central `Directory.Packages.props`, regenerate affected project locks and append required CI entries under RES-product-solutions. Existing Core and repository tooling identities remain unchanged. | Consume the actual published Foundation/contract closure required by CON.91/FND.01; establish the bounded host proof with staged available producers, zero trim/AOT/single-file diagnostic evidence, real native-library ABI smoke vectors and actual local per-RID launch evidence. Retain continuous Windows/Linux compilation/package CI; runtime is local opt-in under P2-017, never hosted GUI/installed-consumer CI. Record unavailable runtime platforms honestly. | No D-001 conflict identified in existing bootstrap. Start remains subject to CON.91 and FND.01 ledger evidence. Missing real native consumer/runtime evidence prevents PRF.02 inheritance or completion. |

## Scope binding and limitations

`Program.cs` currently composes a Hello client/view model with Avalonia and Microsoft.Extensions.Hosting; it is not embedded assistant orchestration or private child-channel proof. The central pins are Contracts.PublicApi `1.0.0-ci.36.1` and Build.Policy `1.0.0-ci.20.1`; no Foundation or LocalRpc.Scope package is consumed. Avalonia supplies packaged rendering native dependencies, but a successful AOT compile is not an ABI smoke-vector result. The historical bootstrap record explicitly limits its evidence and transfers no predecessor runtime pass to ArcScope.

Adoption only records this classification. No implementation changes, producer-pin changes, builds, artifact downloads, local runtime or publication verification cycle were performed. The retained applicable CI results and original publication receipt were inspected. No task is classified inherited, so no PRF.02 completion record is created. The slice opens PRF.02 only under normal prerequisite readiness.

## Ledger review

This ledger-only change is validated with `delivery.py check` using this retained Plan worktree and the explicit current Design root. Exact-head peer review and the ledger merge are recorded in the claim and PR; Plan has no CI. No removed-product source cleanup is owned or certified by this slice.
