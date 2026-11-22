# ACC-01 final signed same-Run composition

Windows deku and Linux H-22 each passed one native composition case with zero failures and zero skips. Each case used one interactive Run in a fresh, isolated instance of the stock signed Node. The [main ACC-01 evidence](afv2-acc-01-evidence.md) records the formal host profiles, signed release installation and other acceptance cases.

## Product and test identities

Both signed packages identify producer commit **2e7bef628bcf23263dc3c9773b13f362f37a9a83**, tree **2827f24db67bb736fe89d8ff25402748bb49fd76**, and canonical main **708bc0d74d8973bcf004d72c3967dd0fed730736**. The private launcher's fresh preflight authenticated the Ed25519 archive, verified the stock installation and bound the signed producer to freshly fetched GitHub main. It compared the signed installation, auxiliary probe and auxiliary test assembly against the build receipt. The same auxiliary patch and launcher ran on both hosts.

The `--verifier` input on each host was the reviewed `run-verified-acc01.py`, SHA-256 `67879c4262b338f5a1979e058dfa692433456d9ad3798e8868f6bb69c0d1c49c`. The launcher checked those input bytes and set the final producer commit and tree pins in a private `verify-2e7.py` copy. The executed copies hash to `5d1b70948bddc5007a81473ab1140ad4a764165ea4e411b663549eb6baae887f` on Windows and `0bb43ec86c3249aafd1b1df9249a46d5cc2e57dba0c993e6ab4f750846710e56` on H-22.

| Artifact | Windows deku | Linux H-22 |
| --- | --- | --- |
| Signed archive SHA-256 | c767f8758c7da71f7be1e9ee0018774171dd9e25a403f282341449306fe30573 | 0d0483444e7aa73633c10d5272de58b5c2a44d737f71ddd0493669f11ba778d5 |
| Stock signed installer receipt SHA-256 | 9898a3fe4196f692683da698ced7e8aa44769703cc707f8d2016219dd07e573e | f8e588b09bddcce4a83470251dd46a574ac8b254a77f73c5a236e092663d8cbe |
| Verified signed files | 99 | 92 |
| Auxiliary patch SHA-256 | def5a574caae8465163e607b35ded805f8636d791a92f1dadb2076f43b310155 | def5a574caae8465163e607b35ded805f8636d791a92f1dadb2076f43b310155 |
| Auxiliary launcher SHA-256 | 3da33d2a41d8d52073dd4bf213aef348f809f0dd502ecdf277fadd32b6864c1c | 3da33d2a41d8d52073dd4bf213aef348f809f0dd502ecdf277fadd32b6864c1c |
| Native auxiliary probe SHA-256 | cc71ac9485c2515804e317fa6432b99af00e06f311d2e7a94ee1bcd0445da418 | 2b64b3eb4f7ce13384fc6a2512ad0e664a8188fea5cb1227b5e03517e06d30d4 |
| Auxiliary test assembly SHA-256 | 47c23f1a8fc7cf91f1ae7cb98f8a51880b761b7a4bf7b96a38fe98057892dd6e | e45562f87a6e27fc91bde24cfccbd3e789705dc60daea28b8caea2aff3dd5e5e |

## Same-Run observations

| Observation | Windows deku | Linux H-22 |
| --- | --- | --- |
| Run ID | 8d968fdb914f43a684c96b8c3595d887 | 5a8ec1189361496698bc9e992144e4de |
| Launch SHA-256 | 8157cd78475cb7bb0250c0201f0cb1a24c567435079fb118df15e3a27fc5f6fc | 63a1365aaae9ef4d3343692c6d79d61ff120591b69bf498f802ef80ad3b1fc54 |
| Controlled loopback TCP peer | 127.0.0.1:2446 | 127.0.0.1:42681 |
| Direct successful exchanges, contained accepts | 2, 0 | 2, 0 |
| Contained TCP outcome | The bounded connect ended with OperationCanceledException while the Run's cancellation token was clear | SocketException, native errno 111 (ECONNREFUSED), with an independently identified private network namespace |
| Native process count during pressure | 6 | 6 |
| Sampled cumulative CPU time | 2,312,500 microseconds | 572,321 microseconds |
| Sampled peak memory | 72,699,904 bytes | 68,157,440 bytes |
| Applied CPU after live update | 249 millicores | 250 millicores |
| Memory limit retained after update | 268,435,456 bytes | 268,435,456 bytes |
| Managed test duration | 15.660 seconds | 8.601 seconds |

The root workload emitted native terminal readiness at 24 rows by 80 columns, touched 32 MiB and started two real descendants. Its recorded TCP attempt and ten file operations followed the pressure-ready event. An independent listener exchanged the fixture sentinel directly with the host before and after the contained attempt. The listener received zero connections during the contained attempt. The Windows probe used its four-second socket deadline. The Linux test matched the payload's network and PID namespace inodes to host observations for the held cgroup member and verified that its network namespace differed from the supervisor and host.

Under that same Run identity, the workload wrote and read its private 19-byte sentinel, read an explicitly granted read-only fixture and received a native refusal when writing that grant. Reads and writes of three other synthetic fixtures were refused. These covered the Run's private control directory, the neighboring Sandbox and an ungranted host path. Windows returned Win32 error 5 for all seven denied file operations. Linux returned errno 30 for the write through the read-only mount and errno 2 for the six operations on unavailable paths. The host verified the original fixture bytes, including the private control sentinel during the Run, and on Windows also checked the tested file DACLs. After Stop, the Run's private sentinel bytes persisted and the granted and excluded fixture bytes were unchanged.

The signed Node accepted a live CPU decrease from 500 to 250 requested millicores, with a lower applied CPU reading, the same Run scope and a durable policy revision of 2. The effective memory limit was retained. Linux also read the CPU quota and memory limit directly from the held cgroup. The terminal accepted a native resize to 35 by 107 and input x, then detached. After an actual Node restart, the same Run epoch, launch hash, original supervisor and durable resource revision continued under a fresh authenticated control generation. The test acquired a new terminal writer, observed resize to 38 by 112 and input y, and detached again. The retained terminal output contained the Unicode alternate-screen display.

The Stop receipt recorded an effect of Happened. Both signed Nodes reported GroupEmptyVerified, and the fixture observed the original supervisor, payload root and both known descendants exit. On Windows, the evidence covers native aggregate Job accounting, the prepared executor's birth and actual process lineage and birth for the root and children. The signed supervisor's drained receipt recorded zero payload Job members, the supervisor as the sole remaining aggregate member before its exit, and completed output drain. On Linux, the test bound the native cgroup and mapped namespace-local PIDs to live host process identities, then confirmed that the held cgroup was empty. Both passing cases completed the fixture's teardown checks for the private Node, local channels, isolated owner key and fixture-owned leftovers. The independent TCP listener was closed with the fixture.

This receipt measures the exact default-deny policies and controlled IPv4 loopback endpoints above. External selected TCP or UDP egress remains **unverified** in this final composition. The earlier native profile receipts retain their original policy and topology scope.

## Native commands and raw evidence

The launcher used the already-built private auxiliary worktree, final signed profile and original reviewed verifier. The selected test invocation was the same on both hosts.

```text
dotnet test --project tests/ArcForges.ClosedLoop.Tests/ArcForges.ClosedLoop.Tests.csproj -c Release --no-build --filter-method ArcForges.ClosedLoop.Tests.MxcRunServiceTests.InstalledAcc01ComposesNativeBoundaryInOneInteractiveRun --minimum-expected-tests 1 --fail-skips on
```

Windows launcher invocation

```powershell
$base = 'C:/MyFile/Projects/ArcForges/Cloud/.git/arcforges-verify/cache/center02-pg-18.7-win'
$tools = "$base/acc01-final-aced1eb012fb-tools"
python -I -B "$tools/same-run-composition-2e7bef628bcf-win-imagepath/run-composition.py" --profile "$base/acc01-final-2e7bef628bcf-tools/profile.final.json" --verifier "$tools/run-verified-acc01.py" --worktree 'C:/MyFile/Projects/ArcForges/ArcForges/.worktree/acc01-2e7-composition-author-win' --mode run
```

H-22 launcher invocation

```bash
umask 0077
base=/home/sammiller/arcforges/ArcForges/.git/arcforges-verify/launches
tools="$base/acc01-final-aced1eb012fb-tools.rTOtJyw6"
python3 -I -B "$tools/same-run-composition-2e7bef628bcf-win-imagepath.wkoxjabg/run-composition.py" --profile "$base/acc01-final-2e7bef628bcf-tools/profile.final.json" --verifier "$tools/run-verified-acc01.py" --worktree /home/sammiller/arcforges/ArcForges/.worktree/acc01-2e7-composition-linux --mode run
```

The following private directories hold the original output and their SHA-256 manifests.

- Windows **run.sbzlep3j** at `C:/MyFile/Projects/ArcForges/Cloud/.git/arcforges-verify/cache/center02-pg-18.7-win/acc01-final-aced1eb012fb-tools/same-run-composition-2e7bef628bcf-win-imagepath/run.sbzlep3j`
- Linux **run.bo3mh6ia** at `/home/sammiller/arcforges/ArcForges/.git/arcforges-verify/launches/acc01-final-aced1eb012fb-tools.rTOtJyw6/same-run-composition-2e7bef628bcf-win-imagepath.wkoxjabg/run.bo3mh6ia`

| Raw file | Windows SHA-256 | H-22 SHA-256 |
| --- | --- | --- |
| fixture.log | a0f0cd25b5d2078730e1a4716f38962dc3413e46fa52334eb6a7567b6faf2c46 | 691ca7e8b83adeb5efea2bccc695a5d02d581f26aada5a78adb8ce0f96b08c94 |
| summary.json | 7e4316faa38ed5981e3a6c26ca713851a95717a4e3a9d738579c69ab0b3114b8 | f4ca2b5d79eca1f29d93524392f14785be2477c2be9ea524dbeff1cd7fcc9615 |
| build.json | 2f791d81114e15ec60e672866c2f041f368227c93f30cb993f4eb6169c806d0a | ee454141370a223320adde6565444781b214bc2a52f15d5fe7b3085c9d666356 |
| signed-provenance.json | 14ba822d69e23ccb14a2ba0f7328819f45d409719ebd9bc4a12106624ab7563b | ab880294dda84200181513dabf757d69fe4298db6668599be504892f3961d1ed |
| Primary workload JSONL | 28604.jsonl · b30a085652632817acba5d78a1cab59957774ab922ba72b51eb33f07fd237065 | 2.jsonl · b8c5440c94157a5553b7fd40a812da5e6cb464ef068cbabcafdf158a511fce26 |
| sha256.json | 75c0129f8a641e4bbbbab5b756d87a701fb0114a82a13b2b38f99ca380910f8c | eaddc6d4ec3245951cb01c9720c0c7b2e5c41b058e01f4929c9c1b9b94ab9905 |

## Retained Windows diagnostic

The first Windows attempt on the same signed cohort failed in the auxiliary image-path assertion before the live resource update. The Sandbox API returned a path with a forward slash at one component boundary and the process API returned the same path with a backslash. The revised test canonicalized both full paths before ordinal case-insensitive comparison. Birth and lineage checks remained in effect. Independent review confirmed that the same filename under a different Sandbox still failed the comparison.

The original Windows attempt remains at `C:/MyFile/Projects/ArcForges/Cloud/.git/arcforges-verify/cache/center02-pg-18.7-win/acc01-final-aced1eb012fb-tools/same-run-composition-2e7bef628bcf/run.70esh4q7`. Its fixture.log hashes to e7b3e54a1364a43d45df5c1bb4dc894d7e0fa05ac085792386d0d7701c4dfbd5, its build.json to 1d35927cae223b3e8d42736bcb56429d9d86a5e87404ae65b8e099dd135a48c2 and its primary 31108.jsonl to 3ea4d4c15f642190a8ec5c7d257fc5670aa2dc0580c0994a9139ed6b92604665. The original patch and launcher remain in that attempt's parent directory.

The original Windows auxiliary DLL and PDB remain in `C:/MyFile/Projects/ArcForges/Cloud/.git/arcforges-verify/cache/center02-pg-18.7-win/acc01-final-aced1eb012fb-tools/same-run-composition-2e7bef628bcf-win-imagepath` as prior-ArcForges.ClosedLoop.Tests.dll and prior-ArcForges.ClosedLoop.Tests.pdb. They hash to 6e7325becdf501299f90a0ec337b60308b77d1e5a363670a3878fcde2561a29b and 544ce86f5e83b33961aa9136273634b9530510780199e527f3409e68b221819d. The passing Windows and H-22 receipts use the revised auxiliary test assembly and the same signed product cohort documented above.
