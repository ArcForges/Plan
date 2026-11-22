# AFV2-ACC-01 final H-22 protected custody

The signed Linux x64 Node from reviewed source `2e7bef628bcf23263dc3c9773b13f362f37a9a83`, tree `2827f24db67bb736fe89d8ff25402748bb49fd76` and canonical main `708bc0d74d8973bcf004d72c3967dd0fed730736` passed the installed protected custody suite **3/3** and the separate accepted-delete guard-loss witness **1/1**. Both native XML receipts have zero failures, skips, not-run cases and errors. The independently reviewed qualification used H-22 `v2202601329473427941`, RUN3 `83b8a2ab06fa4b38baedc0b0d5d3b8a1`, protected ext4 and the existing locked non-login `arcforges-acc01` UID/GID 927. The final test and cleanup receipts passed independent review. [Node PR127](https://github.com/ArcForges/ArcForges/pull/127)

The final apply verified the Ed25519 signature and provisioned six fresh RUN3 instances. It reused the existing native `user@927.service`, private home and verified 335-file read-only runtime. The 519-entry final input inventory comprises those 335 runtime files, 183 harness files and one TestLoad. The seventh protected instance was prepared separately after the final 3/3 passed. The previous RUN2 apply stopped after signature verification when its catalogue loop shadowed the digest function and Python reported `'str' object is not callable`. Its exit 1 and later exact one-off completion are preserved as RUN2 history. RUN3 used the corrected fresh script and its own successful apply receipt. [Earlier custody evidence](afv2-acc-01-evidence.md)

## Signed inputs and reviewed controller

The signed archive is 19,587,306 bytes. The authenticated Linux installer recorded 92 files. The installed RUN3 host and its digest catalogue were rehashed in place. The public key and detached signature used to verify the archive are listed below.

| Input | Absolute H-22 path | SHA-256 |
| --- | --- | --- |
| Signed Linux x64 archive | `/home/sammiller/arcforges/ArcForges/.worktree/acc01-node-2e7bef628bcf-main-publisher-linux/artifacts/packages/signed-425874f4002f4797ad2967a1f80673db/arcforges-linux-x64.tar.gz` | `0d0483444e7aa73633c10d5272de58b5c2a44d737f71ddd0493669f11ba778d5` |
| Signed source envelope | `/home/sammiller/arcforges/ArcForges/.worktree/acc01-node-2e7bef628bcf-main-publisher-linux/artifacts/packages/signed-425874f4002f4797ad2967a1f80673db/arcforges-linux-x64.tar.gz.manifest.json` | `72a50e04dc129de6a2748b3783bac1d239afa8e50b10a50fa40100ae198729eb` |
| Detached Ed25519 signature | `/home/sammiller/arcforges/ArcForges/.worktree/acc01-node-2e7bef628bcf-main-publisher-linux/artifacts/packages/signed-425874f4002f4797ad2967a1f80673db/arcforges-linux-x64.tar.gz.manifest.sig` | `1ebe4b6e0e79c20c8fec84406a38df5b287cde5663869b92dd53993f0406bbb2` |
| Public verification key | `/home/sammiller/arcforges/ArcForges/.git/arcforges-verify/logs/acc01-node-2e7bef628bcf-main-linux-recorded/verification-key.pem` | `72cca0d28567091319a987756ea6912d1cca760f66bf4821bb23d6b03d90edef` |
| Qualified installer receipt | `/home/sammiller/arcforges/ArcForges/.git/arcforges-verify/logs/acc01-node-2e7bef628bcf-main-linux-recorded/installer.json` | `f8e588b09bddcce4a83470251dd46a574ac8b254a77f73c5a236e092663d8cbe` |
| Installed RUN3 digest catalogue | `/var/lib/arcforges/acc01-83b8a2ab06fa4b38baedc0b0d5d3b8a1/cohort/digests.json` | `a4539ff79ebb1ba3472865833a5609fc5d3877ce06f511567b07e105edbe7f4c` |
| Installed RUN3 Node | `/var/lib/arcforges/acc01-83b8a2ab06fa4b38baedc0b0d5d3b8a1/cohort/arcforges` | `a567df7da0b3500a010721246fd858bff9a428499bda785a5fb52e5a20d21cd4` |
| RUN3 locked managed inputs | `/var/lib/arcforges/acc01-83b8a2ab06fa4b38baedc0b0d5d3b8a1/proof/runtime-inputs.json` | `8df6845bb1d85ae91d909cbde955a141993f58b93f22e939e870f40e8fea4bc1` |
| Staged standard suite assembly | `/var/lib/arcforges/acc01-83b8a2ab06fa4b38baedc0b0d5d3b8a1/harness/ArcForges.ClosedLoop.Tests.dll` | `c4db4179c2ae6f94001c28a47463fd9d333c665436efef1696063ac2f2ed179d` |
| Staged TestLoad | `/var/lib/arcforges/acc01-83b8a2ab06fa4b38baedc0b0d5d3b8a1/arcforges-testload` | `77c5d7cf6886c8c781ef3a8531965563092c1aa1fced92331fad9faf9f07bccd` |
| RUN3 custody pins | `/usr/local/lib/arcforges-acc01-witness/6bdd6f4ce6eab765bfe69cf10c04956b1fc7675a85de7c8fbafe62371b08d150.json` | `6bdd6f4ce6eab765bfe69cf10c04956b1fc7675a85de7c8fbafe62371b08d150` |
| RUN3 guard overlay pins | `/usr/local/lib/arcforges-acc01-witness/a40fc25ad15203e47b60f3f2b58fa3fe84d5caee2df3e849ff0b2b71909c940f.json` | `a40fc25ad15203e47b60f3f2b58fa3fe84d5caee2df3e849ff0b2b71909c940f` |
| Fresh approved custody controller | `/usr/local/lib/arcforges-acc01-witness/42a38d3fdf0887b254ccc14becf7385308a67b5fb3bc725c0522a477cc3838d0.py` | `42a38d3fdf0887b254ccc14becf7385308a67b5fb3bc725c0522a477cc3838d0` |
| Guard coordinator | `/usr/local/lib/arcforges-acc01-witness/711ece5d68536d8f850d1275782432e47f3d2c0676d69b5fc402a9971a8b3d82.py` | `711ece5d68536d8f850d1275782432e47f3d2c0676d69b5fc402a9971a8b3d82` |
| Exact administrator | `/usr/local/lib/arcforges-acc01-witness/b1725d17d575572fdfc541dc646332c2069772b372508780820731819dbf7564.py` | `b1725d17d575572fdfc541dc646332c2069772b372508780820731819dbf7564` |
| Read-only collector | `/usr/local/lib/arcforges-acc01-witness/51b2e1a319a9e7ed9118d6667cdf5de2a4751ea0a8d61ee65a6951396304f895.py` | `51b2e1a319a9e7ed9118d6667cdf5de2a4751ea0a8d61ee65a6951396304f895` |
| Root script install receipt | `/home/sammiller/arcforges/ArcForges/.git/arcforges-verify/launches/acc01-final-2e7bef628bcf-tools/ar05-native-927/root-script-install.log` | `0e1498fb038407e0e576a2fcd30b37155081c3f294ebbdba4b09cd1c91a31916` |
| Root pins and coordinator install receipt | `/home/sammiller/arcforges/ArcForges/.git/arcforges-verify/launches/acc01-final-2e7bef628bcf-tools/ar05-native-927/root-pins-coordinator-install.log` | `e13309fcb0d6e06763241952a9c2dc9b41c77ee27e536056be1d977f3350876b` |

## Controller invocations

These are the observed controls for this one completed fixture. The hash-named root-owned artifacts were verified after installation. The controller and administrator ran as root for fixture provisioning and the single guard change. The tests, Node, CLI and payloads ran as UID/GID 927 using the existing native user manager. Both console launches selected only their exact class and wrote private native xUnit XML.

```bash
umask 0077
sudo -n /usr/bin/env -i PATH=/usr/sbin:/usr/bin LANG=C.UTF-8 /usr/bin/python3 -I -B \
  /usr/local/lib/arcforges-acc01-witness/42a38d3fdf0887b254ccc14becf7385308a67b5fb3bc725c0522a477cc3838d0.py \
  --apply --pins /usr/local/lib/arcforges-acc01-witness/6bdd6f4ce6eab765bfe69cf10c04956b1fc7675a85de7c8fbafe62371b08d150.json \
  --pins-sha256 6bdd6f4ce6eab765bfe69cf10c04956b1fc7675a85de7c8fbafe62371b08d150
sudo -n /usr/bin/env -i PATH=/usr/sbin:/usr/bin LANG=C.UTF-8 /usr/bin/python3 -I -B \
  /usr/local/lib/arcforges-acc01-witness/42a38d3fdf0887b254ccc14becf7385308a67b5fb3bc725c0522a477cc3838d0.py --run
sudo -n /usr/bin/env -i PATH=/usr/sbin:/usr/bin LANG=C.UTF-8 /usr/bin/python3 -I -B \
  /usr/local/lib/arcforges-acc01-witness/42a38d3fdf0887b254ccc14becf7385308a67b5fb3bc725c0522a477cc3838d0.py \
  --prepare-guard-loss --pins /usr/local/lib/arcforges-acc01-witness/a40fc25ad15203e47b60f3f2b58fa3fe84d5caee2df3e849ff0b2b71909c940f.json \
  --pins-sha256 a40fc25ad15203e47b60f3f2b58fa3fe84d5caee2df3e849ff0b2b71909c940f
sudo -n /usr/bin/env -i PATH=/usr/sbin:/usr/bin LANG=C.UTF-8 /usr/bin/python3 -I -B \
  /usr/local/lib/arcforges-acc01-witness/711ece5d68536d8f850d1275782432e47f3d2c0676d69b5fc402a9971a8b3d82.py \
  --run-reviewed-witness \
  --extension-file /usr/local/lib/arcforges-acc01-witness/42a38d3fdf0887b254ccc14becf7385308a67b5fb3bc725c0522a477cc3838d0.py \
  --revoker-file /usr/local/lib/arcforges-acc01-witness/b1725d17d575572fdfc541dc646332c2069772b372508780820731819dbf7564.py \
  --expected-host-sha256 a567df7da0b3500a010721246fd858bff9a428499bda785a5fb52e5a20d21cd4 \
  --expected-overlay-inventory-sha256 a40fc25ad15203e47b60f3f2b58fa3fe84d5caee2df3e849ff0b2b71909c940f
```

The read-only controller used `root-snapshot` for root-owned identity and receipt metadata and `ordinary-denials` as ordinary UID 1000. Its exact source and both receipts appear below.

## Protected custody suite

Native xUnit reported 3/3 in 8.330 s. Both the direct console and coordinator exited 0.

- `InstalledSandboxDeletePreservesSiblingAndHostGrantInLinuxCustody` passed managed use, deletion and preservation of sibling and host-grant data.
- `InstalledSandboxDeleteReconcilesInterruptedOwnedBoundariesInLinuxCustody` passed the five positions `after-lock`, `after-quarantine`, `during-removal`, `before-removal-proof` and `before-tombstone`. The intentional before-removal-proof UNKNOWN original remains preserved.
- `InstalledNodeRefusesMissingLinuxCustodyBeforeCreatingState` passed pre-effect refusal. The read-only post-run snapshot confirmed the exact `-unprovisioned` instance remained absent.

| Evidence | Absolute H-22 path | SHA-256 |
| --- | --- | --- |
| RUN3 fresh apply output | `/home/sammiller/arcforges/ArcForges/.git/arcforges-verify/launches/acc01-final-2e7bef628bcf-tools/ar05-native-927/apply.log` | `0b41734ca172c6654ee889f1dd28ab746567f40639ae1e42d164042c3d724f95` |
| RUN3 fresh apply exit 0 | `/home/sammiller/arcforges/ArcForges/.git/arcforges-verify/launches/acc01-final-2e7bef628bcf-tools/ar05-native-927/apply.exit` | `9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa` |
| Native fixture identity ledger | `/var/lib/arcforges/acc01-83b8a2ab06fa4b38baedc0b0d5d3b8a1/fixture.json` | `24e6904411661c95a192423ca0bcd2d230b4b4e9c5fbd67dd7a4e4508e246163` |
| Native suite output | `/var/lib/arcforges/acc01-83b8a2ab06fa4b38baedc0b0d5d3b8a1/proof/custody-suite.log` | `be9d11a2e9437dfa3e29f7f646b280a660a42b6009c3a7b74ef8633ccd3e0cc9` |
| Native suite XML | `/var/lib/arcforges/acc01-83b8a2ab06fa4b38baedc0b0d5d3b8a1/proof/custody-suite.xml` | `c7135d7e107740ff98da72723c93f18603a6725edb3afa1c1d511d359fecee3c` |
| Exact suite counts | `/var/lib/arcforges/acc01-83b8a2ab06fa4b38baedc0b0d5d3b8a1/proof/custody-suite.counts.json` | `94e266c04a0dc85819b9c07ee795c63024e3f9dad314cbb07aa47c4e915af6c8` |
| Direct native exit 0 | `/var/lib/arcforges/acc01-83b8a2ab06fa4b38baedc0b0d5d3b8a1/proof/custody-suite.native.exit` | `9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa` |
| Validated suite exit 0 | `/var/lib/arcforges/acc01-83b8a2ab06fa4b38baedc0b0d5d3b8a1/proof/custody-suite.exit` | `9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa` |
| Suite launch output | `/home/sammiller/arcforges/ArcForges/.git/arcforges-verify/launches/acc01-final-2e7bef628bcf-tools/ar05-native-927/run.log` | `5a728ed00b6d50f0dee2bcd60b1ce172cca784431ac41d0af783157d9aa267b3` |
| Suite launch exit 0 | `/home/sammiller/arcforges/ArcForges/.git/arcforges-verify/launches/acc01-final-2e7bef628bcf-tools/ar05-native-927/run.exit` | `9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa` |
| Historical RUN2 first apply output | `/home/sammiller/arcforges/ArcForges/.git/arcforges-verify/launches/acc01-final-e4c41f68e14d-tools/ar05-native-927/apply.log` | `b4e43897ac95479e773ecd5e87262b80d895cda211a98cfba8461aaa5e8ab76f` |
| Historical RUN2 first apply exit 1 | `/home/sammiller/arcforges/ArcForges/.git/arcforges-verify/launches/acc01-final-e4c41f68e14d-tools/ar05-native-927/apply.exit` | `4355a46b19d348dc2f57c046f8ef63d4538ebb936000f3c9ee954a27460dd865` |

## Guard loss after the original Delete was accepted

The separately compiled RUN3 witness `AcceptedDeleteStopsWhenAdministratorRevokesExactGuard` passed 1/1 in 1.414 s. Administrator PID 1698281, witness PID 1698282 and the coordinator each exited 0. Neither actor log was truncated. The accepted, administrator and observed receipts bind the same original command `01a202b36bdc72f2a265206c2eb540b7`, owner epoch `0569399478d567075d00cc40f6d8e941` and Sandbox `f563eba9d57961bc39683b2ac49e4503`.

The witness observed accepted and locked before the administrator removed readability from the exact guard. The root-owned guard changed from mode `0444` to `0000` on device/inode `65028:1066613` with the original bytes preserved. The original Delete then reported `UNKNOWN`, `RECOVERY_REQUIRED` and `native_13`. The observed checkpoint-to-release interval was 61 ms. The owned tree, sibling and external sentinels matched. The quarantine, successor and removal proof were absent. The original UNKNOWN, data and guard record remain retained.

| Evidence | Absolute H-22 path | SHA-256 |
| --- | --- | --- |
| Actually compiled overlay source | `/home/sammiller/arcforges/ArcForges/.worktree/acc01-2e7-guard-loss-linux/tests/ArcForges.ClosedLoop.Tests/LinuxProtectedGuardLossWitness.cs` | `73a9b802ce73a275b82a22722d23ee32162644748ddd6e51fcad0f5ee9764256` |
| Compiled overlay assembly | `/home/sammiller/arcforges/ArcForges/.worktree/acc01-2e7-guard-loss-linux/tests/ArcForges.ClosedLoop.Tests/bin/Release/net11.0/ArcForges.ClosedLoop.Tests.dll` | `d164fcd56d5a29a7011dc9ab9e58d86c853e8b2b7532823fc8496f8bb2af4335` |
| Executed staged overlay assembly | `/var/lib/arcforges/acc01-83b8a2ab06fa4b38baedc0b0d5d3b8a1/guard-loss-overlay/harness/ArcForges.ClosedLoop.Tests.dll` | `d164fcd56d5a29a7011dc9ab9e58d86c853e8b2b7532823fc8496f8bb2af4335` |
| Staged guard inventory | `/var/lib/arcforges/acc01-83b8a2ab06fa4b38baedc0b0d5d3b8a1/proof/guard-loss-inventory.json` | `a40fc25ad15203e47b60f3f2b58fa3fe84d5caee2df3e849ff0b2b71909c940f` |
| Native locked restore output | `/home/sammiller/arcforges/ArcForges/.git/arcforges-verify/launches/acc01-final-2e7bef628bcf-tools/guard-overlay-build/restore.log` | `79bfeea7316dc08616bd42be292ab5c2d2c44ec414e43c0caf274542e54aaf60` |
| Native overlay build output | `/home/sammiller/arcforges/ArcForges/.git/arcforges-verify/launches/acc01-final-2e7bef628bcf-tools/guard-overlay-build/build.log` | `b9fa4530ddc3462f7956a7adbd2b70e57887531158a48dbe21d05a71463ec9cb` |
| Native overlay build exit 0 | `/home/sammiller/arcforges/ArcForges/.git/arcforges-verify/launches/acc01-final-2e7bef628bcf-tools/guard-overlay-build/exit` | `9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa` |
| Overlay preparation output | `/home/sammiller/arcforges/ArcForges/.git/arcforges-verify/launches/acc01-final-2e7bef628bcf-tools/ar05-native-927/guard-prepare.log` | `da18ec1b0c97d29ef4e975c4214a9226c11fb68f8c1a10532ce60408b45cda47` |
| Native guard admission | `/var/lib/arcforges/acc01-83b8a2ab06fa4b38baedc0b0d5d3b8a1/proof/guard-loss-run/admission.json` | `7e0df1b7aa79bdfe245fb611f20fffb5e1c4e40888d45a6338e70ba6c00e384a` |
| Administrator output | `/var/lib/arcforges/acc01-83b8a2ab06fa4b38baedc0b0d5d3b8a1/proof/guard-loss-run/administrator.log` | `324e81551241b63c9afb31f60bddd9e28fd754b17ede26a953c4cc005e16c003` |
| Native witness output | `/var/lib/arcforges/acc01-83b8a2ab06fa4b38baedc0b0d5d3b8a1/proof/guard-loss-run/witness.log` | `0fa0debd27973e878630174d5847d9f494b5f35e55c5cdd140402a08a0b75032` |
| Native guard XML | `/var/lib/arcforges/acc01-83b8a2ab06fa4b38baedc0b0d5d3b8a1/proof/guard-loss-run/custody-guard-witness.xml` | `57e0c4139408829f2a35890f5db7c4bdb65e7e3836add20ff45707b68141c9a2` |
| Exact guard counts | `/var/lib/arcforges/acc01-83b8a2ab06fa4b38baedc0b0d5d3b8a1/proof/guard-loss-run/counts.json` | `b600bae52e986206027927f1afba7ede1a6c32c41a6c877e737fe9eccbfe7d73` |
| Both native actor exits | `/var/lib/arcforges/acc01-83b8a2ab06fa4b38baedc0b0d5d3b8a1/proof/guard-loss-run/native-exits.json` | `2c05a450ac10a73262690b1bb45d861aa87be042efa83a6dafa499015e3066ed` |
| Coordinator output | `/home/sammiller/arcforges/ArcForges/.git/arcforges-verify/launches/acc01-final-2e7bef628bcf-tools/ar05-native-927/guard-coordinator.log` | `1056975531497daf56ab2cdb738670afc232888ed84a608f6c78ec1890c8389b` |
| Coordinator exit 0 | `/var/lib/arcforges/acc01-83b8a2ab06fa4b38baedc0b0d5d3b8a1/proof/guard-loss-run/exit` | `9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa` |
| Accepted locked operation | `/var/lib/arcforges/acc01-83b8a2ab06fa4b38baedc0b0d5d3b8a1/proof/guard-loss-run/accepted.json` | `cc3419c416d489209db501aa9eaa540192b9966ec92bab5b30dd941e8acb19d6` |
| Administrator guard readback | `/var/lib/arcforges/acc01-83b8a2ab06fa4b38baedc0b0d5d3b8a1/proof/guard-loss-run/administrator.json` | `f21c7caab70c646673814d9bd7e2cbe4b642cbd0d48b5eaff3d0a17f7c3677b9` |
| Original durable outcome | `/var/lib/arcforges/acc01-83b8a2ab06fa4b38baedc0b0d5d3b8a1/proof/guard-loss-run/observed.json` | `f188e5cbb30cfc9f9e2e74ee693bc42a00ea1dae931e670a5fd1b6a5baacb6c2` |
| Primary verdict | `/var/lib/arcforges/acc01-83b8a2ab06fa4b38baedc0b0d5d3b8a1/proof/guard-loss-run/primary.json` | `e095b6126a35b667c586f9402f36d5d16727abcca1059442673cc70b74d260a9` |

## Ordinary-account denials and cleanup identities

Ordinary UID 1000 received native `EACCES` when requesting a writable non-truncating custody-record handle, anonymous creation in the protected instance and a readable private-data directory handle. The instance, private data and custody-record inode identities and the custody-record bytes matched before and after. All six protected suite instances matched their provisioned instance, data, lock and record identities.

The coordinator observed the exact signed guard-witness Node at PID 1698295, birth tick 310931008 and image device/inode `65028:1065708`. Its private socket was `/tmp/af-cl-cc4096140ccc/node.sock`, device/inode `35:29013147`. Post-run readback confirmed the Node identity, descriptor, socket and socket directory absent. Only native user-manager PID 1624559 and its PAM companion PID 1624561 remained for UID 927. Their birth ticks matched the idle admission observations. The native user manager and runtime bus stayed present with `cpu`, `memory` and `pids` delegation. The cleanup receipt reports no issues and no forced direct-child action.

| Evidence | Absolute H-22 path | SHA-256 |
| --- | --- | --- |
| Ordinary-account EACCES and unchanged inode readback | `/home/sammiller/arcforges/ArcForges/.git/arcforges-verify/launches/acc01-final-2e7bef628bcf-tools/ar05-native-927/run3-ordinary-denials.json` | `75bf00f92e0b8affba9f99ea4d28a04c3cd0439fc23f57e0e22be3d9b4512449` |
| Read-only post-RUN3 native snapshot | `/home/sammiller/arcforges/ArcForges/.git/arcforges-verify/launches/acc01-final-2e7bef628bcf-tools/ar05-native-927/post-run3.snapshot.json` | `a812e4c0488b3718c4e15cc3f23c3cd96f5c5b57502e34da78b090313c726942` |
| Exact UID idle before fresh apply | `/var/lib/arcforges/acc01-83b8a2ab06fa4b38baedc0b0d5d3b8a1/proof/idle-before-apply.json` | `57736416b1e2d57b6306189aec27ffdf6ff11a14d93d2a31c76817bcc90e59af` |
| Exact UID idle before suite | `/var/lib/arcforges/acc01-83b8a2ab06fa4b38baedc0b0d5d3b8a1/proof/idle-before-run.json` | `57736416b1e2d57b6306189aec27ffdf6ff11a14d93d2a31c76817bcc90e59af` |
| Live installed Node and socket identities | `/var/lib/arcforges/acc01-83b8a2ab06fa4b38baedc0b0d5d3b8a1/proof/guard-loss-run/native-live-node.json` | `c9a35fe3672dc42cc3a959e6277f2e396eed6d7dce5e949d40388299b1aca264` |
| Guard cleanup identity result | `/var/lib/arcforges/acc01-83b8a2ab06fa4b38baedc0b0d5d3b8a1/proof/guard-loss-run/cleanup.json` | `2f0651108a7d41d1d6b6cdb470c1abd0abe472a6e927b024f5c948770f528ce5` |
| Retained root-owned guard mode 0000 | `/var/lib/arcforges/file02-83b8a2ab06fa4b38baedc0b0d5d3b8a1-guard-loss/sandbox-deletion-owner.v1` | `0b837a1115ec05f7d9d5b4f29dc51075c620c7a9f186efdad85851edd6f023bd` |
