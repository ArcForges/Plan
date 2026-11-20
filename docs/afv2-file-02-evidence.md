# AFV2-FILE-02 native deletion evidence

## Candidate and acceptance scope

[Node PR 112](https://github.com/ArcForges/ArcForges/pull/112) is the preserved work for preview, guarded admission, quarantine, bounded removal, durable uncertainty and explicit successor recovery. It uses the published Sandbox V2 contract and the existing Store schema. Only the owner-local command can initiate it. No package was publicly published or deployed.

Design 05 section 9 requires successful normal owned-root deletion and explicit interrupted recovery on the designated native Windows and Linux hosts. The Linux capability refusal is observed before admission. It does not meet Linux positive acceptance under AR-05.

## First native candidate

Node `68a3c120a6f1787744a701a5080c1ea1c5ae2b5b`, tree `b557ab5cf22f0ea544ccba6fa92049ba030c4b7a`, was fetched separately from GitHub on `deku` and H-22. Both hosts used the pinned official MXC 1.0.1 archive. The archive SHA-256 was `0e832239454ba7fcd338ff56218a287eef4c0a01c1484084b869f55feff8abe9`.

On `deku`, restore, Release build, Native AOT and package integrity passed. Two installed deletion tests failed with zero skips. A separate run against the exact installed package observed Windows error `native_32`, an original `UNKNOWN` receipt and journal `recovery_required` at revision 3. The original directory remained, and there was no quarantine entry. The Node had retained an extra child lookup from its own private-root validation, which prevented the later exclusive DELETE handle. The qualified-stage REC-01 delete successor selection passed one of two cases. The case without the moved root returned a generic path refusal while the other passed.

The Windows raw files are in the Node repository's preserved `.worktree/file02-win-smoke-68a3c12/artifacts/file02-smoke/`.

| Raw file | SHA-256 |
| --- | --- |
| `06-targeted-native.log` | `fd237c7c477c5c0d67196f088b66731ae953d21f2f54cfbace18c04dec613e03` |
| `08-core-delete-native.log` | `e79ff82da1a9b1089a1afbc64ca4eebf2924342ff4f67dec68f73063fb60927f` |
| `09-deletion-observed.json` | `b62ebf366fc9291f8d3c37c30a5898e55615af98dea77254a3c3759d9e4caa2d` |

On H-22, the two installed tests passed with zero skips. The tests exercised real held export and Run blockers, then verified `linux_exact_directory_mutation_unavailable` after those blockers were gone. The original file data, sibling Sandbox and external grant sentinel remained. No Delete was admitted and no deletion journal or quarantine was created. The exact installation was drained. The raw log is `ArcForges/.git/arcforges-verify/launches/file02-author-68a3c120a6f1-linux/native.log`, SHA-256 `7a054b8009f48b2ce7a85669b84e49f76b613f750268c7cccdd02977f709f88f`. The installer archive SHA-256 is `d26c9b0f38250eff8bfa29c021d7332f3acf4ee8e7103c4f03ef7ce3061708c6`.

## Second native candidate

Node `4994dd8b77193bd6fb0a34e674e021c9a46191c9`, tree `2c954e66fc1ded169ff87b4ce426707574b7bbf8`, releases its extra child lookup before acquiring the same exclusive handle. A known missing original and quarantine is classified as an identity conflict, retaining the native detail.

On `deku`, the installed normal deletion case passed with the exact owned root removed and the sibling Sandbox and external sentinel preserved. The installed interruption case received `native_32` while observing a directory immediately after the Node process joined. The log did not record the checkpoint label or identify another handle owner. Overall the two installed cases were 1/2 with zero skips. Both qualified-stage REC-01 cases passed with zero skips. The raw files are in `.worktree/file02-win-smoke-4994dd8/artifacts/file02-smoke/`.

| Raw file | SHA-256 |
| --- | --- |
| `06-targeted-native.log` | `ee5fd98b875495514c25d4aa81a0b7385da37b0b775c534760344ef9e9f66761` |
| `08-core-delete-native.log` | `6e7afc691576abaea546b7582bbadf0c5c422eb80bd30dfcd09355ef90df78a5` |

On H-22, the installed guarded-refusal cases passed 2/2 with zero skips. The qualified-stage REC-01 selection ran both old cases. They verified the typed pre-effect refusal, then each failed its old assertion of `DELETING` because the fixture's pre-seeded state remained `RECOVERY_REQUIRED`. The installed tier exited 0 and the qualified-stage theory exited 2. The raw log is `ArcForges/.git/arcforges-verify/launches/file02-author-4994dd8b7719-linux/native.log`, SHA-256 `237b6dd7b7e48cd28683bcb843e0e51e6b1dba1810eab6a9356a8f4792495305`.

## Preserved candidate

Node `b941e1baeab2aed5e72773be0ef21689e02ceca3`, tree `978c3e684cba2cd6796a2e1126c4625a8d76a862`, bounds the post-exit test readback retry to three seconds and to `native_32`. It still verifies the exact held identity, actual subtree progress, phase and original replay. The Linux REC-01 test compares the state and revision before and after the refusal. The fixture seeds `RECOVERY_REQUIRED` at revision 2. A newly admitted Delete detaches host grants in its current durable config revision and preserves the prior exact revision. The Node records the native phase, outcome and reason, with a distinct event for secondary failure while persisting an uncertain outcome.

The independent nonauthor review of this exact head confirmed that the original held-parent identity and native mutation requirements remain in force. It also checked durable grant detachment, preserved prior configuration, typed diagnostics, cancellation of the original RPC after acceptance and before reply, and the native identity refusal for a replaced quarantine fixture. No source blocker was found for the exercised Windows path or Linux refusal. Linux positive acceptance remains open.

On `deku`, the independently fetched candidate passed locked build, all four Native AOT components and exact 93-file installation integrity. The two selected installed cases passed 2/2 with zero skips. They covered normal owned-root deletion, live Run and unclosed export protection, unchanged sibling and external data, current grant detachment and immutable prior config, and five real interruption checkpoints. The checkpoint before the absence witness retains `UNKNOWN`. The checkpoint after the witness permits an explicit successor with a fresh revision to settle the original. Both selected REC-01 continuation rows passed against the same actual installed MXC stage with zero skips. Matching installation processes drained to zero. The installer archive SHA-256 is `400049196b1c74022d3882df7822b1b2185314af3cbc46c703bdad748c90dc9b` and installed Host SHA-256 is `8c92a723093f7aa83ad2c2b674abb9a00ebb7baaf255014530c2c087ec2ceca9`.

The `deku` test logs are in `.worktree/file02-win-smoke-b941e1b/artifacts/file02-smoke/`, selected by `FullyQualifiedName~InstalledSandboxDelete` and `FullyQualifiedName~DeleteSuccessorPreservesTheOriginalUnknownAndHeldNativeIdentity` respectively.

| Raw file | SHA-256 |
| --- | --- |
| `06-targeted-native.log` | `957b49dbd905e303c58d95e1706c5e944f2d09a951eccf2f3f78aad62327fc43` |
| `08-core-delete-native.log` | `514406ce1df6e0042df241a187d357c126c74d9ae7c069a4e2683a63443d1515` |

On H-22, the independently fetched candidate passed the same two installed cases and the two actual-stage REC-01 cases with zero skips. These are native pre-effect refusals that preserve the original owned identity, state, revision, config and receipt, with no new successor or fresh deletion journal. No running native Run unit matched the installation after teardown. The 88-file archive SHA-256 is `1ad49f78248129c2979a9f62b39eff23999f9b08d0aa5c4281ad9c18ad0a184f` and installed Host SHA-256 is `6fb38ab2ff072eac2f92c4d7b74baa739ab30755034d9e8c7289db78b13e16ce`. The raw log is `ArcForges/.git/arcforges-verify/launches/file02-author-b941e1baeab2-linux/native.log`, SHA-256 `d1a9b1936678a0506e32e356afdb0ce1c007b2997dc6df4b6ae12663424dd747`.

The Node PR stays draft. The full Node delivery profiles and merge remain pending a candidate that can pass the required Linux positive cases. The targeted native results above are not repository delivery statuses.

## Required Linux qualification

The candidate checks the held private parent and the exact owned child before reporting the capability unavailable. The available Linux operations have name-based effects. The qualified H-22 profile has no operation that binds these effects to the verified native child identity. The next positive acceptance requires a supported native guard for the exact quarantine move and bounded removal, followed by the specified real deletion and recovery runs. Until then the candidate refuses the effect, and AR-05 is open for FILE-02. See [Linux rename semantics](https://man7.org/linux/man-pages/man2/rename.2.html) and [Linux unlink semantics](https://man7.org/linux/man-pages/man2/unlink.2.html).
