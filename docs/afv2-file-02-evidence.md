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

The preserved candidate checks the held private parent and the exact owned child before reporting the capability unavailable. The available Linux operations have name-based effects. The original H-22 configuration has no operation that binds these effects to the verified native child identity. The default configuration keeps its pre-effect refusal. See [Linux rename semantics](https://man7.org/linux/man-pages/man2/rename.2.html) and [Linux unlink semantics](https://man7.org/linux/man-pages/man2/unlink.2.html).

## Protected storage candidate

[Plan PR264](https://github.com/ArcForges/Plan/pull/264), merge `568077e5c555dbe97115ea761d0e3f82d9b991ad`, reopened FILE-02 as the only active task. [Design PR86](https://github.com/ArcForges/ArcForges-Design/pull/86), merge `65c50ea74c2a433bba890c51ae237d2a211e5edd`, defines the optional protected Linux configuration. [Plan PR265](https://github.com/ArcForges/Plan/pull/265), merge `052dd8a814e34d049d2ade656b9338e4212f4dc6`, admits the existing test fixture path used to qualify disposable protected storage. Both Plan profiles passed 5/5 for each Plan PR, and the Design profiles passed 4/4 on each native host.

[Node PR112](https://github.com/ArcForges/ArcForges/pull/112) retains `b941e1baeab2aed5e72773be0ef21689e02ceca3` and the prior evidence above. The candidate is `ea81178988700f8df7fc0078b3b615762670dc0c`, tree `5484bc714a22b97a3c2caa5410511a6c33e0b5dc`, based on current Node main `0c7c869237e0c4e2b934a0da02b7d28bfcf467e9`. Its production source is the same as `7c1a77837af264163805651eea4ff6767556c711`. Its subsequent commits adjust two existing native test fixtures. Independent review approved the test changes and the fixes for interruption during startup provenance publication and the Center shutdown-order invariant in the ordinary profile. Both native hosts reported the Center seam assertion at `1fbf9e6d995939fa5c0da7d17b9c63628dbf6976`. After the source fix, the existing Center seam suite passed 35/35 on `deku`.

The new profile requires explicit selection and root-controlled provisioning. A filesystem identity stamp binds its fresh data root and lock. Node rechecks custody at each effect while the existing managed-use gate and durable journal govern admission, recovery and confirmation.

### Windows installed deletion and restart witness

The separately installed `7c1a77837af264163805651eea4ff6767556c711` package passed its 93-file integrity check. The archive SHA-256 was `59d4b9aea5996b1533b3a5bc2486ce55f13bfdb768313ab07f1eb17a15d46db6`. Both installed deletion cases passed, with zero skips. They covered normal removed data and all five interruption checkpoints, including `UNKNOWN` when durable removal proof had not been recorded.

The full profile for `7c1a778` reported one existing Cloud Channel restart fixture failure. The fixture started the replacement after observing the original endpoint stop but before its process released the native instance guard. The replacement exited with code 3 before starting Cloud Link. The isolated original case passed on rerun. [Plan PR266](https://github.com/ArcForges/Plan/pull/266), merge `69f00f5bac27ef35ea0509bf4a7bc5072d96c4c9`, approved the narrow test scope. The current candidate captures the original process handle and requires its actual exit before the replacement starts. The corrected case passed against the Native AOT Host, and independent review confirmed that the original endpoint, payload and credential assertions remain.

### H-22 installed configuration observations

On H-22 `7c1a778` built and published Native AOT. Its initial full profile stopped at packaging because the official MXC release asset was absent from the verifier's default path. The retained host-local GitHub asset matched the pinned SHA-256 `0e832239454ba7fcd338ff56218a287eef4c0a01c1484084b869f55feff8abe9`. Windows acquired the same official version directly from GitHub and matched that digest independently. A fresh H-22 install passed its 88-file integrity check. The installed archive SHA-256 was `bc240a000f133d0d66658bf9619bdce1991de327a32ca47cb3dcf763816cbccb`, and the installed Host SHA-256 was `175af81b322e5de47b7de4bff1af94fb8690a273bb8db797c05d415cbcaf6205`. The installed `InstalledNodeRefusesMissingLinuxCustodyBeforeCreatingState` test passed 1/1 with zero skips and verified that the missing configuration created neither data nor endpoint state.

| Earlier summary under `.git/arcforges-verify/logs/` | Failure | SHA-256 |
| --- | --- | --- |
| `20261121-063612-1fbf9e6d9959-win/summary.json` | Center shutdown seam | `b5286713fc2a39d8c506f07bc67aa2d9dd6262236b980b973ead8d4dc684b77a` |
| `20261121-063612-1fbf9e6d9959-linux/summary.json` | Center shutdown seam | `41712515222eef54dfd28917130de90e64003c088204d1fb04ad0067356850d4` |
| `20261121-064417-7c1a77837af2-linux/summary.json` | Missing local MXC asset input | `2ebba8e293c6daedb20eee48e2731ffcaeeb2d68fa55278ef88372ba782568c0` |
| `20261121-064700-7c1a77837af2-win/summary.json` | Cloud Channel fixture restart before guard release | `113107610d6bddc07bd7214ab04790540d0be24c6714534fb8d70f9cef689c1b` |
| `20261121-065435-7c1a77837af2-linux/summary.json` | Installed resource fixture observed 300 vs 340 millicores | `613d1029bfd3bb0998272dfc1ce566d3b0323aae24118f4801ddaffe9f74095b` |
| `20261121-071250-e53c23b36ede-linux/summary.json` | Resource fixture's refused start exceeded both ceilings | `a5ce6e302a89abda71ae0bcd99fed6cb446a629da5de0395107b9dee2cbd4b68` |

The second H-22 full attempt for `7c1a778` passed 51/52 installed tests with zero skips. The remaining resource fixture observed 300 millicores in place of its earlier 340 reading, consistent with an allowed weighted rebalance between the two reads. The isolated original test passed on the same installed Host. [Plan PR267](https://github.com/ArcForges/Plan/pull/267), merge `af2a538a9f72849f7ae77d30eb533e33c7dab97f`, approved the narrow fixture input repair. The Linux fixture now reserves the configured 500 millicores at admission, so the intervening allocator no longer treats the later explicit increase as growth above an older 450 budget. The exact native and rejection assertions, Windows inputs, and production resource controller remain unchanged.

The first resource fixture adjustment also raised the total of an early Linux refusal probe above the Node ceiling. `e53c23b` exposed this with 51/52 installed tests and the correct `node_cpu_grant_unavailable` outcome for that input. The candidate's refusal probe totals 550 millicores, between the Sandbox ceiling of 500 and the Node ceiling of 600. Its accepted initial cohort still totals 500. The corrected exact test passed twice against the independently installed `e53c23b` Host, whose production sources match the candidate. The raw logs are in `/home/sammiller/file02-resource-final-ea81178.jHpK6X/` and hash to `6b715febb2cd8cc6f04603e106807807fdaa7dd216d06b5fa51e3283b6b82c25` and `c08c13ef464cec7b335e58fe73e82c483a191b14401486933faf4009e885f186`. An earlier concurrent targeted attempt had stopped at the separate page cache observation before reaching this sequence. Its retained `native.log` in `file02-resource-stable.x5AWDc` hashes to `e905f82f23052fe79388acaa863ec0f100ee7d983e3d636279dd4e41706c52f0`.

A disposable local ext4 fixture used the unprivileged numeric UID 60014 for the exact installed Node. The regular `sammiller` account received `Permission denied` when creating a sentinel in the selected data root. Node resumed startup from a partial provisioning stage, published the complete stamp, and restarted with the same stamp. An attempted unselected restart returned `linux_protected_storage_selection_required` before opening its endpoint. The first probe hit the Unix socket path-length limit. The successful probe used shorter temporary paths and removed the disposable root after teardown. It used no dedicated systemd user manager and covers startup, configuration, and host-account exclusion.

The successful raw records are in `/home/sammiller/file02-custody-startup-7c1a778.EKhjPg/`. The earlier failed probe remains in `/home/sammiller/file02-custody-startup-7c1a778.JcQPvt/`.

| Raw file | SHA-256 |
| --- | --- |
| `ordinary-denial.log` | `f77530dd30decd517fa1ccb0e7b4a0ed10a67c590b1cbe41f7a7a0efd8d7552c` |
| `first.status.json` | `e9006f2abf1e8b3cc745df675749dfd6a65fcbc4ca23376c142e6aa74fd2dc8c` |
| `second.status.json` | `1ba0f4ab8d5cbcd1307d8cca4bc0ecda1cbbd0e3c5773a956bb8d93b2e894e08` |
| `first-stamp.sha256`, `second-stamp.sha256` | `6453ee49f28b7a9cc5cdeb20848c13017bdaed6d3a9db9df7eea30239b40d2ce` |
| `omit-selection.stderr.log` | `f77f756b1dbb5a93d31b9e3770639774db4aa87bb54a0b4560aef9d0c68c0b36` |

### H-22 native whole-directory component observations

An isolated ext4 component fixture called the actual Node Core methods from the `7c1a778` build under the reserved numeric UID. It created two owned roots, one external sentinel, 150 private files and a symlink to the external location. The first process moved the exact selected root into quarantine and exited. A new process recovered that same quarantined identity. During a bounded removal pass the fixture revoked the profile's storage protection after the first effect. Node Core refused before the second effect. Restoring the valid fixture configuration allowed a fresh process to complete removal in five bounded passes and confirm actual absence. The sibling and external bytes survived. The disposable directory was removed after testing.

The successful raw records and probe source are under `/home/sammiller/file02-native-component.IifWhA/`. Core assembly SHA-256 was `dc86f692ddfbd15cd32daa82016061a6dc4ed894a15e0e28a9b5bcc04076d18b`. This is native filesystem evidence from the component. It observes process replacement and guard loss without an installed CLI receipt, a Node deletion journal, or an admitted MXC Run.

| Raw file | SHA-256 |
| --- | --- |
| `01-quarantine.log` | `3223101164902df70229d8b781090547690de56874be99b62f5ccfc57b3026e9` |
| `02-guard-loss.log` | `87f69395ae750f7aeb607601c3f2e2799a00cc63b3e096cd7e938617be484caf` |
| `03-removal.log` | `9339db40be32bca508d44806ea03838486dec66ec365bd1981e9633bfd100d33` |

### Candidate package results

H-22 reported all 20 required native checks passing at exact `ea81178`, including both exclusive suites and the startup gate. The verifier's `20261121-073129-ea8117898870-linux/summary.json` has SHA-256 `bae55dd49d42dd81c39acf76c88c8e73fb718df624a73fd8f5d07e22622fe3e1`. Its stock package gate passed all 52 installed tests with zero skips, including the ordinary Linux pre-effect refusal. The 88-file installation archive SHA-256 was `abe55cd3204fdd50b15ad73ad057557c37f58a4aad94901510a95f2e20b19deb`. The matching `linux-package.log` hashes to `42bee328824905f70b8431ea26cfa2188bc780c96d84d007a5c2e88b154e9e97`.

The installed `ea81178` Host (SHA-256 `251f4cc3db1b5d2f25621c77f1a8d5e0b31191c3b83f436f61b36438cd18ffbf`) also passed the selected but unprovisioned startup test 1/1 with zero skips. It confirmed refusal before an instance or endpoint was created. The private raw log `/home/sammiller/file02-installed-denials-ea81178.NLK7xu/native.log` has SHA-256 `565817902c930676b0d3be22d9e5ac041987e07231fdb3abdd9217f345fb1f61`.

The earlier `e53c23b` Windows package step passed 52/52 with zero skips. Its raw log `20261121-071250-e53c23b36ede-win/win-package.log` hashes to `5a8bba7145e54986eb4141b9429441f57f040169cb5b8d2784786d67dc01d543`. The exact `ea81178` first Windows package attempt passed 51/52 with zero skips. Its 93-file installation archive SHA-256 was `c685eafd184747e996d9c15a158148cc46175bf4dc2ad520ea798ecb52efb288`. The unchanged weighted resource fixture received `node_cpu_grant_unavailable` on its second Start before introducing its own pressure. Its initial headroom sample precedes both Sandbox creates and the first Run launch. Each Start evaluates the current live host frame. The raw log `20261121-074047-ea8117898870-win/win-package.log` hashes to `1d62c4eff4ea5d61abfb712fd7980858f108796933870bad8c651375996ba573`. The remaining first-attempt checks and the isolated follow-up retain their separate results.

### Remaining protected Linux acceptance

H-22 retains working native systemd and cgroup v2 for its normal account. The protected acceptance requires a separate host-owner-provisioned non-login identity with the normal native `user@UID` manager and fresh ext4 test roots. The installed optional tier is `ArcForges.ClosedLoop.Tests.SandboxDeleteLinuxCustodyTests`. Until it and the distinct denial observations pass, AR-05 and F-FILE-01 stay open and Node PR112 stays draft.

For the protected installed tier, use independent disposable instances `file02-<runid>-<case>` with a fresh eligible `data` root for each case. The cases are `normal`, `after-lock`, `after-quarantine`, `during-removal`, `before-removal-proof` and `before-tombstone`. The selected unprovisioned case must have no instance directory. Run the exact installed Node and official MXC bundle under the dedicated UID with the normal control groups delegated by its user manager. Set a private `TMPDIR` on ext4 and use `umask 0077` for evidence. Set `ARCFORGES_MXC_DELETE_CUSTODY_RUN_ID` to the 32-character lowercase hex run ID and opt in with `ARCFORGES_LINUX_PROTECTED_STORAGE=1`. The existing package path and TestLoad inputs still apply.

```sh
dotnet test --project tests/ArcForges.ClosedLoop.Tests/ArcForges.ClosedLoop.Tests.csproj -c Release --no-build \
  --filter-class ArcForges.ClosedLoop.Tests.SandboxDeleteLinuxCustodyTests \
  --minimum-expected-tests 3 --fail-skips on
```

Record the ordinary host account's denial on the applicable protected parent and the behavior when custody is revoked during an accepted deletion, along with the exact installed suite results. Separate these from the normal H-22 per-user refusal and the required repository host reports.
