---
task: ADOPT.02.runtime-proofs
status: complete
recorded: 2026-09-27
claimant: w-20260927-dother
epoch: 1
---

## Review inputs and decision

DesktopPlatform integration owner `w-20260927-dgov` (epoch 2) assigned this reviewer the slice. Reviewed the exact [frozen baseline](../adoption/baseline.md#desktopplatform), DesktopPlatform source `e5ce94221c13d0014781a760c0865b942350be4d`, the generated runtime-proofs task records and WP-06.01/02/03/06 plus the continuous-proof package obligation. The frozen baseline has no open PRs. Existing build-policy/native ABI publication receipts establish only their stated bootstrap scope; none is a receipt for these four proof outcomes.

Source inspection used the complete tracked tree at the frozen commit, `docs/platform-bootstrap.md`, the ContentSandbox hello-world `Program.cs`, `tests/NativeAbiTests` and `eng/build/desktop-aot.props`. Neither `tests/LocalRpcAotTests`, `tests/ReleaseArtifactTests`, nor `eng/verification` exists at that commit. Native ABI smoke and AOT build properties do not implement generated local or business transports, realtime recovery or third-party-control admission.

## Task classifications

| Task and obligation | Classification | Evidence and bound write scope | Remaining scope | Conflicts and blockers |
|---|---|---|---|---|
| PRF.04; WP-06.01 full and continuous-proof contribution | gap | Frozen tree has only architecture/native ABI tests. Add `tests/LocalRpcAotTests/**` and `eng/verification/**` in DesktopPlatform; new probe project/list/lock entries require the existing owner protocols, not renaming bootstrap projects. | Two published AOT processes using generated LocalBootstrap and bidirectional Kestrel HTTP/2 named pipes/UDS; same-user authentication, cancellation, reconnect, malformed/unauthorized/resource-bound cases; actual process evidence for VG-04 and permitted continuous compile/static coverage. | No unresolved design conflict. Start requires CON.05 published generated local service closure. |
| PRF.05; WP-06.02 full and continuous-proof contribution | gap | `tests/ReleaseArtifactTests/**` and `eng/verification/**` are planned additions, not existing evidence. Existing native package consumer checks do not call business ingress. | Published generated binary gRPC-Web AOT client against actual Worker/Container ingress, headers/trailers/cancellation/scoped errors/exact values and negative cases; record F-026 evidence. | No unresolved design conflict. Start requires CON.92 and PRF.07. |
| PRF.06; WP-06.03 full and continuous-proof contribution | gap | Add realtime probes beneath `tests/ReleaseArtifactTests/**` and `eng/verification/**`; no corresponding source or acceptance receipt exists in the frozen tree. | EventService.Watch/output streams with Poll/readOutput authoritative recovery against real Worker/Container/DO, including drop/expire/revoke cases; no SignalR or durability inference. | No unresolved design conflict. Start requires PRF.07; exact generated operations remain producer-owned. |
| PRF.09; WP-06.06 full and continuous-proof contribution | gap | Add `eng/verification/probe-evidence/**`; existing general dependency admission is not a UI-control AOT acceptance process or candidate log. | Record the admission process and one actual intended candidate's zero-diagnostic AOT publish evidence, using the candidate selected by PLT.34. | No unresolved design conflict. Start requires PLT.34. |

## Validation and limits

All four mapped tasks were compared against outcomes, obligation parts, write scope, validation and evidence fields. No inherited task records are appropriate. No implementation, downloads, product builds, publication rechecks or runtime tests were performed. P2-017 governs execution venue: continuous retained Windows/Linux compile/static checks do not imply hosted runtime execution; required actual runtime/provider evidence remains local opt-in with an existing environment. No optional missing environment is turned into provisioning work.

This slice opens its four tasks only under their normal prerequisites; it does not close VG-04, F-026, VG-03, WP06 or repository adoption. Retired native families remain GOV.17/GOV.18 cleanup and no source was changed. Validation: delivery ledger consistency check and independent exact-head review before Plan merge; PR, reviewed head and merge are retained in the claim audit trail.
