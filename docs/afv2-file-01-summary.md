# AFV2-FILE-01 verification record

The local DataService and CLI operate on one owned Sandbox file per transfer. Import uses a private stage, bounded chunks, and a durable commit receipt. Export seals a private snapshot and retains it for offset replay until safe closure or expiry. Windows and Linux qualification use the pinned official MXC v1.0.1 packages.

## Publication capabilities

The initial Windows and Linux paths publish to a fresh owned file using the native no-replace operation. A changed target yields `CONFLICT/identity_changed`. An otherwise valid replacement of an existing file requires a qualified, atomic native guard tied to the supplied version. The current paths return `EXECUTION/unsupported_combination` before target effect for a matching-version request whose guard is unavailable. The published message shapes and bindings are unchanged. [Design PR 82](https://github.com/ArcForges/ArcForges-Design/pull/82)

FILE-01 observes the retained snapshot Store hold with the actual native fixture and the production managed-use predicate. FILE-02 covers the fresh `PlanDelete` and `Delete` profile and its native transfer-specific deletion outcome under AR-05.

Import publication runs with Node-managed quiescence, held native file and parent identities, and a final check of the named owned root. An independently changed same-owner namespace can prevent a conclusive observation. The original receipt and owned stage remain available for recovery when native proof is incomplete. The process-interruption observations cover the exact disposable test fixture, selected filesystems, and processes in the native receipts.

## Final installed package

The final source candidate `81438ec1c4fa0d2bb2123acf766e2bac2aded19b` has tree `d7e42f5726b7daa10475a7a4364b505ed976571f`. An independent reviewer approved the cumulative diff and confirmed that the last commit contains repository formatting and the existing import-directive order adjustment.

H-22 verified the 88-file Native AOT package, including 50/50 installed tests with zero skips. The package archive SHA-256 is `4c0f1a3e0eed194d355ca1ad9d12f4e8f283ce5d5708ba9d41f31db45c509150`, its MXC manifest SHA-256 is `a2073ce541160bb546f957099c8eddb8a9431137862f79b4cb54334b659e854f`, and the formal package log `.git/arcforges-verify/logs/20261120-110742-81438ec1c4fa-linux/linux-package.log` has SHA-256 `88bb52a17c2a18b41474570955b5278c24c66247bd19326086fd70fbdbc89cdb`.

Windows deku verified the 93-file Native AOT package, including 50/50 installed tests with zero skips. The package archive SHA-256 is `706cd6e44a12477dc406ae7c744ecbbce97326f72c72dcd5f723188aac9ef71e`, its MXC manifest SHA-256 is `504c2e109633185cf21cdacb89b56068120b984ec14825a65129494bbd42db91`, and the formal retry package log `.git/arcforges-verify/logs/20261120-112947-81438ec1c4fa-win/win-package.log` has SHA-256 `f696c445359cf7a76c6a5df9bafb12cbac8cd24795b0bf7e5f7dd32b9503fafd`.

Package tests exercise real local CLI import, bounded file metadata, two official Runs reading the exact private bytes, a retained export after source mutation, the final chunk replay, the production Store deletion hold before and after verified closure, native path and managed-use refusals, source rewind and explicit restart resume. Five process interruptions preserve the original command and actual native bytes. A Linux interruption with both recorded names still linked to the same owned inode remains UNKNOWN with its recovery journal. Verified completed publication resumes the original successful result and does not repeat the effect.

## Final native profiles

The designated hosts fetch the exact candidate from GitHub and run the repository's unchanged `python eng/verify.py run-and-report` from detached native worktrees.

| Host | Full profile | Private summary | SHA-256 |
| --- | --- | --- | --- |
| Windows deku | 15/15 in 3108 s | `.git/arcforges-verify/logs/20261120-112947-81438ec1c4fa-win/summary.json` | `5e9adf89db1ea477784fcaa4e64e0be622d21063f3b80407fff410af424204a3` |
| Linux H-22 | 20/20 in 2636 s | `.git/arcforges-verify/logs/20261120-110742-81438ec1c4fa-linux/summary.json` | `89fe609aa3e2e6809f92a8fe661166c85a370ad475550c65aad0e394d138b81e` |

GitHub recorded both successful statuses at `81438ec1c4fa0d2bb2123acf766e2bac2aded19b`. Both hosts fetched merged Node main at `d78172739b73c5763ecc58c5b446acd85c495125` and confirmed the verified tree `d7e42f5726b7daa10475a7a4364b505ed976571f`. This delivery covers repository integration and native package verification on the designated hosts. The merge's GitHub workflow list was empty. [Node PR 111](https://github.com/ArcForges/ArcForges/pull/111)

## Design decision verification

Design candidate `7228fde7cbacba50c7a31750166713365537fce0` was independently reviewed at tree `5e5a917a5471e76e92614cbf775b2c9066006d0c`. Both designated host reports passed 4/4. The fetched Design main merge `854725de931da13a19cacb6a2125c67c0fa4c919` has the same tree.

| Host | Private repository receipt | SHA-256 |
| --- | --- | --- |
| Windows deku | `.git/arcforges-verify/logs/20261120-104829-7228fde7cbac-win/summary.json` | `f38b07c9d78bc13e607ace2bdc975c7eb1b3ce31a9afb2fec9be940b90a2ef04` |
| Linux H-22 | `.git/arcforges-verify/logs/20261120-104832-7228fde7cbac-linux/summary.json` | `bd5b4bd9ac80a8b0f18df9047809daa14cabd4ba7637e4ceafd332af1677c857` |

The closure-order clarification records a durable intent before native release and reports `closed_at` after proof of release. Independently reviewed candidate `1131fa078606b5c6260b96c76c84ad25b3471a89`, tree `3f3b65dcbd63d5734c0e8b55cbcfeb2aa52109f0`, passed 4/4 on each designated host. Both fetched Design main at `c6d4e3bd94065a8128eeb780a7a2e013d5f83c75` and confirmed the same tree. [Design PR 83](https://github.com/ArcForges/ArcForges-Design/pull/83)

| Host | Private repository receipt | SHA-256 |
| --- | --- | --- |
| Windows deku | `.git/arcforges-verify/logs/20261120-110010-1131fa078606-win/summary.json` | `6a69793b6904dd444db38a269f8495612aee9ecff947df67ab72c084b6bedce1` |
| Linux H-22 | `.git/arcforges-verify/logs/20261120-110014-1131fa078606-linux/summary.json` | `be254eb06debeb5220b0f336477df7e21c3392f6f7ca8300afc471b0c05c58a4` |

## Earlier candidate observations

Both hosts fetched candidate `c2532752ad4cf4d9d2f2fe07981ad47cbb26d213`, tree `7a03e2054974380046e17df43ac65a3df832282e`, from GitHub. Native build and verified MXC packaging succeeded. The targeted installed tests on this candidate failed before final qualification. [Node PR 111](https://github.com/ArcForges/ArcForges/pull/111)

- Windows passed 0/3 with zero skips. The normal CLI import and typed restart test reached first WriteImport with the pre-settlement revision. The error path accessed the wrong oneof and returned gRPC Unknown. The ordinary path rejection fixture failed independently while creating its temporary junction. The raw log is `.worktree/file01-win-smoke-c253275/artifacts/file01-smoke/10-targeted-native.log`, SHA-256 `33ca91f6893eddb29392969a67e1bff73f9b90865899dc535fb299a3ba4cdc7b`.
- H-22 passed 1/3 with zero skips. The ordinary path and managed-use fixture passed. The CLI import returned `invalid_argument`, and the typed restart test encountered the same revision error path. The raw log is `.git/arcforges-verify/launches/file01-author-c2532752ad4c-linux/native.log`, SHA-256 `27bf34587cdc8514b834f7130ede3e0404eac930c5b27872a88e111d9b4b82ef`.
- The isolated ordinary H-22 CLI reproduction reported `Unable to read beyond the end of the stream.` Its actual Store held the original OPEN Begin transfer at verified offset zero and recorded zero WriteImport receipts. The CLI encountered EOF while reading its local source, before sending a chunk. The private observation JSON in `.git/arcforges-verify/launches/file01-cli-diagnostic-c2532752ad4c-observed-linux/` has SHA-256 `3dee77b169fd09b9adfff7d34ed0535fc31b5560445001578ddf8fe309c4ff91`. The fixture Node stopped normally.

Candidate `b1ebe40211fef23236646e20d8ba0bf0f418e922`, tree `70a3f903abd46d970c67d3fce69fea32887060da`, settled import staging before the first successful reply, bounded its content identity in the durable intent, and propagated native flush errors. Windows passed 2/3 targeted cases with zero skips. The ordinary guard and the orderly restart passed. The remaining case completed actual CLI import and the usage and listing checks, then exceeded the fixture's 64 KiB retained Run output while requesting proof for 1 MiB of bytes. The native log is `.worktree/file01-win-smoke-b1ebe40/artifacts/file01-smoke/06-targeted-native.log`, SHA-256 `0bfa47101072c60504609af0b1affa5b129513e88d45e372051dbd00b5ea5f64`.

H-22 also passed 2/3 on `b1ebe40`, with zero skips. The ordinary guard and the typed orderly restart passed. The remaining CLI local source failure was still present. The native log is `.git/arcforges-verify/launches/file01-author-b1ebe40211fe-linux/native.log`, SHA-256 `4f3781ae88485c9ff713e3c61651e0773d1fa5820a8f58a0523fcde2c4e1f35a`.

On `27b6ec7661f3bcf7fc092ed607d018cc50cd9595`, tree `2c5c940d4821f1edd1911ae3e07f8984eda9240c`, H-22 passed all eight targeted native cases with zero skips. Windows passed five with zero skips, including the genuine CLI import, two original-data Run readbacks, retained snapshot replay and CLI export. Three published interruption cases already matched the original durable operation, content, and stable replay version, then failed because a test compared two separator spellings of the same absolute Windows path. The follow-up normalizes absolute path spelling and retains the existing independent native identity assertions.

| Host | Private targeted log | SHA-256 |
| --- | --- | --- |
| Windows deku | `.worktree/file01-win-smoke-27b6ec7/artifacts/file01-smoke/06-targeted-native.log` | `f8d246a3ffec0d2c30a658e9c14a856410e06d944b1f7923d466b8416bed78bb` |
| Linux H-22 | `.git/arcforges-verify/launches/file01-author-27b6ec7661f3-linux/native.log` | `1fa03aebcdb5357c207206923325f99f3077e226e694eb032ef1906d1cd6ad21` |

The first formal attempt at `c23b6d6eb9b8028f1e70ed2deff14f86b7583fcf` ended on H-22 at `linux-format` with formatting diagnostics. The original `.git/arcforges-verify/logs/20261120-110329-c23b6d6eb9b8-linux/summary.json` has SHA-256 `0d41b7741c12ed1ad7e05a820a4b5c29d3586779c706b686c037c2ce72a1f65b`. Its `linux-format.log` has SHA-256 `2b8e71a2bbb6d835a9ac3147d915c9c5207b6bae98ebf2e3527f333c4073091b`. The obsolete Windows invocation was stopped after the Linux failure and after its build passed. Its last observed stage was `win-ci`. The retained launcher log `.git/arcforges-verify/launches/file01-formal-c23b6d6-win/reporter.log` has SHA-256 `f4674623094c60fd730ce64a4fd18ffeab0a2859e8404793132f3456c4531806`.

The first Windows run of `81438ec` passed the build, CI, schema, Native AOT, and tools checks, then failed `win-closed-loop-native`. The existing legacy signed-file fixture restarted after the first Node descriptor disappeared. The second process returned exit 3 from the Windows single-instance check before reaching Node startup. The fixture reported a remaining isolated secret-store entry after its cleanup attempt. The original `.git/arcforges-verify/logs/20261120-110825-81438ec1c4fa-win/summary.json` has SHA-256 `c9294e3e02b753b35515c6c6ae32b175dccfeaf685b2f26acdc48af0de3c5998`. Its `win-closed-loop-native.log` has SHA-256 `390dbad8210c9b9c154e262131879503da07f02ca61a307ba023eff1febb9ca0`.

The same Windows Native AOT binary, SHA-256 `861f656c897d0dec152f93124d5fe08ee873dfd4a42a4346e0dd57d0ddfaa8d9`, passed a direct rerun of the unchanged fixture 1/1 with zero skips. The diagnostic observed zero running Node processes from that binary at the end. Its log `.git/arcforges-verify/logs/20261120-110825-81438ec1c4fa-win/diagnostic-single-restart/single-restart.log` has SHA-256 `6492b705c20c33a78f8f09e25f5cc19a3028bff5d2abc00c844cf3d0890fea0e`. The fixture's stop waits for endpoint disappearance, which can precede original-process exit and single-instance release. The full Windows retry uses the same source candidate and ordinary profile.
