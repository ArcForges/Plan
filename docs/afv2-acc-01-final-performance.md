# ACC-01 final signed continuity and performance evidence

The final Windows and H-22 installations from Node `2e7bef628bcf23263dc3c9773b13f362f37a9a83`, tree `2827f24db67bb736fe89d8ff25402748bb49fd76`, passed the real local Center continuity cases and the extended native performance collector on 2026-11-22. Each collector also verified the interactive terminal stream with a paused reader. The verified producer is an ancestor of canonical Node main `708bc0d74d8973bcf004d72c3967dd0fed730736`. These observations address the continuity and performance portions of ACC-01. The [main ACC-01 evidence](afv2-acc-01-evidence.md) holds the package suite, recovery, data safety and same-Run composition results.

## Verified inputs and invocation

| Input | Windows deku | Linux H-22 |
| --- | --- | --- |
| Native environment | Windows 11 build 26300, x64, 18 logical CPUs, 34,359,738,368 physical RAM bytes | Debian 13 trixie, Linux 6.12.63+deb13-amd64, glibc 2.41, x64, 8 logical CPUs, 16,773,283,840 physical RAM bytes |
| Profile and wrapper | `windows-process-executor-v1` / `win-wrapper-local-v1`, official MXC 1.0.1, ConPTY | `linux-bubblewrap-sdk-v1`, official MXC 1.0.1, native PTY |
| Verified Ed25519 archive SHA-256 / installed files | `c767f8758c7da71f7be1e9ee0018774171dd9e25a403f282341449306fe30573` / 99 | `0d0483444e7aa73633c10d5272de58b5c2a44d737f71ddd0493669f11ba778d5` / 92 |
| Installed Host SHA-256 | `ae6ec95f268d65484ea3d4e5c681de85500c591ed6fcc8d373a46a2ef20ccd02` | `a567df7da0b3500a010721246fd858bff9a428499bda785a5fb52e5a20d21cd4` |
| Bench / TestLoad SHA-256 | `90b97a9bf539d093b0bdbc0f7e7eaef7219fe44fa5b642b8422cd742c70dccbc` / `97f2b9040071aa9f5d660a4520a76ce511852c484d17e26cd098d220474958cc` | `7db7c641c2ce31639be2d30096659f3b768f67c3b55583989a34d123e9e96e6c` / `77c5d7cf6886c8c781ef3a8531965563092c1aa1fced92331fad9faf9f07bccd` |
| Compiled ClosedLoop assembly SHA-256 | `10344c84b368c5cbc46b5d2f680539816c066417bddd24573200e038009697bf` | `c4db4179c2ae6f94001c28a47463fd9d333c665436efef1696063ac2f2ed179d` |
| `profile.final.json` SHA-256 | `84b7fc56a9b6d40087aa9e7774418d7c3dd74d68af43fc1f2b1e8d5faad3e9ae` | `87f5f61af288b03a8ea2be15a732750806cecd8600792b0b93417f1042a02e60` |

Bench reports .NET 11.0.0 on both hosts. The exact installed executable paths are `C:/Users/J7Rdm/AppData/Local/arcforges-acc01-verified-db3c92bd17a8470fbaabb2f09e7bbe05/arcforges.exe` and `/home/sammiller/verified-acc01-node.aCKtb5BC/cohort/arcforges`. The source, archive, signature, installed files, Bench, TestLoad and compiled fixture are bound in the retained per-host provenance.

Each command used these files in the absolute per-host tools directory below. The runner SHA-256 is `0bb43ec86c3249aafd1b1df9249a46d5cc2e57dba0c993e6ab4f750846710e56` on both hosts. The supplementary collector SHA-256 is `69879711a7779c66aad38d49c4a5ee3b54a71a426723b2c55eda1958945bab83` on both hosts. Substitute the host's profile digest above for `<profile-sha256>`. H-22 used process-local `umask 0077`.

```text
python -I -B run-verified-acc01.py --profile profile.final.json --mode host01
python -I -B native-terminal-backpressure.py --runner run-verified-acc01.py --runner-sha256 0bb43ec86c3249aafd1b1df9249a46d5cc2e57dba0c993e6ab4f750846710e56 --profile profile.final.json --profile-sha256 <profile-sha256>
```

The first command exercises `TestHost01InstalledEntitlement` through the existing HOST-01 fixture. The Windows child is `run-host01-fixture-control.ps1 -Scenario HostedEntitlement` with the pinned native inputs. H-22 uses the existing `host01-pair-tools/run_fixture.py` and its Go race-enabled, uncached test selection `^TestHost01InstalledEntitlement$` in `./internal/pages`. The second command runs the checked-in extended performance collector with 50 repeated launches, one warmup, a 15-second idle window and the original slow stdout pipe case. Its additional installed CLI Run uses `run start --terminal on` and `run logs --follow --stream terminal`. The benchmark policy denied ingress, egress and host loopback and used the THROTTLE pressure action and 1,048,576-byte output retention.

## HOST-01 continuity

The existing fixtures ran the real Go Center at `919ad1c08797f1ade53335ad1598166121a359bf`, tree `17d48a4c330e7bac7d3a16010eefdca6e9bc3e65`, with Go 1.27.4 and PostgreSQL 18.7 over isolated loopback. On deku PostgreSQL used the native archive SHA-256 `ead0bbc27fb678fa24dcf86b738981323042abd073c744103bf7f3aed23f9a33`. H-22 ran the pin `postgres:18.7-alpine3.24@sha256:b6972e1115a4ff8eba5d7f7d19184926d1e16d7d1136ae1e1a7ebf286da0f015`, with matching actual image and server version.

| Native result | Windows deku | Linux H-22 |
| --- | ---: | ---: |
| Go `self-hosted` | PASS, 31.02 s | PASS, 19.40 s |
| Go `official-lapse` | PASS, 46.20 s | PASS, 34.54 s |
| Go parent | PASS, 77.21 s | PASS, 53.94 s |
| Installed native child, per case | 1/1 passed, zero skips | 1/1 passed, zero skips |
| Driver and fixture exits | 0 / 0 | 0 / 0 |

Both self-hosted cases enrolled and reconnected over actual local HTTPS without an official plan, credential or hosted entitlement rows. Both official-mode fixtures used labeled provider facts and the actual resolver across the wall-clock expiry boundary. The same device request encountered the official missing-address transport refusal and reached typed validation over local TLS. The original signed V2 connection closed with correlated 4403, and a separately correlated typed read returned `subscription_expired`. The installed child continued its local workflow. The admission log records `automatic readmission refusal observed=false` on both hosts. The observed refusal is for the correlated typed read. Fresh WebSocket admission after expiry remains unverified.

Windows `pg_ctl stop` exited 0, the native fixture receipt reports `verified_stopped` and `verified_no_selected_processes`, and a read-only follow-up found the retained `pgdata` directory with no `postmaster.pid`. The H-22 fixture recorded removal of its owned container `arcforges-center-host01-4464f9e1`. A read-only Docker query for that exact name returned zero entries. Fixture TLS scratch is scoped to the runner's temporary directory. The H-22 result directory retained the public leaf and TLS log.

## Native performance

| Observation | Windows deku | Linux H-22 |
| --- | ---: | ---: |
| First fresh CLI process, no warmup (n=1) | 32.567 ms | 13.869 ms |
| Repeated CLI launches after one warmup, p50 / p95 (n=50) | 28.874 / 34.278 ms | 8.883 / 12.137 ms |
| Node launch to Ready | 0.585 s | 0.185 s |
| Node idle CPU, percent of one core | 1.667% | 1.000% |
| Node first/last idle RSS bytes | 52,674,560 / 53,428,224 | 69,865,472 / 70,701,056 |
| Node first/last private commit bytes | 30,781,440 / 31,531,008 | Unavailable |
| Supervisor idle CPU, percent of one core | 0.312% | 0.667% |
| Supervisor first/last idle RSS bytes | 14,503,936 / 14,852,096 | 19,492,864 / 19,746,816 |
| Supervisor first/last private commit bytes | 6,766,592 / 7,094,272 | Unavailable |
| Held Run start to RUNNING / Stop to verified empty | 0.710 / 0.720 s | 0.553 / 0.549 s |
| Ordinary terminal, rendered bytes / elapsed / throughput | 298,090 / 1.200 s / 248,373 B/s | 262,152 / 0.746 s / 351,495 B/s |
| Ordinary terminal GAP frames / bytes lost | 0 / 0 | 0 / 0 |
| Slow stdout pipe, paused / delivered / dropped / GAPs | 0.882 s / 262,144 / 3,407,892 / 1 | 0.728 s / 327,700 / 3,342,336 / 2 |
| Paired TestLoad payload elapsed wall time, direct / managed | 14 / 14 ms | 18 / 17 ms |
| Paired payload peak RSS, direct / managed | 11,407,360 / 10,276,864 bytes | 10,825,728 / 11,010,048 bytes |
| Direct process and managed operator wall observations | 0.042 / 1.011 s | 0.027 / 1.018 s |
| 1 s / 5 s watcher complete snapshots over about 15 s each | 15 / 3 | 15 / 3 |
| 1 s / 5 s watcher Node CPU change, percentage points vs unwatched Node | −0.417 / −0.208 | +0.200 / +0.067 |

The benchmark times `arcforges --version` from process launch to exit. The first result characterizes that first process only. There was no OS cache flush. Windows earlier `c471` scoped startup comparisons reported first/p50/p95 of 34.184/30.083/33.476 ms. The final Windows p95 is 0.802 ms higher in this sample. The earlier H-22 signed `aced1eb` published capture reported 11.391/7.561/12.167 ms. The final H-22 p50 is 1.322 ms higher in this sample. These are observed comparisons without a universal threshold or statistical conclusion.

The direct and managed TestLoad use the same deterministic one-thread workload with 10,000,000 iterations and seed 1. Payload elapsed time is wall time from TestLoad's stopwatch. The managed boundary includes lifecycle setup, transport, output drain and verified cleanup. The direct boundary covers direct process start through exit. RSS is native payload peak. The full process tree and sampler-only costs remain unmeasured. The watcher values are observed end-to-end Node delivery CPU differences in separate windows, including idle background variation. Windows private commit and Linux RSS use platform-specific process counters.

### Paused native terminal reader

| Native terminal result | Windows ConPTY | Linux PTY |
| --- | ---: | ---: |
| Run ID | `1z2eh190jf86pvrfwbw18fa70x` | `67rcarh7kb9sk9tt0ewr1tcvv5` |
| Pause to verified native group empty / resumed drain | 0.712560 / 0.101200 s | 0.879834 / 0.050490 s |
| Anchor rendered offset | 166 bytes | 28 bytes |
| Rendered final offset | 4,174,581 bytes | 3,670,044 bytes |
| Received / dropped rendered bytes | 212,279 / 3,962,302 | 262,144 / 3,407,900 |
| Actual `slow_consumer` GAP, requested → earliest | 146,700 → 4,109,002 | 196,608 → 3,604,508 |
| Matching fresh retained suffix | 65,579 bytes | 65,536 bytes |
| Rendered rate from post-anchor offset through verified empty | 5,858,333 B/s | 4,171,262 B/s |

The reported rate divides the rendered cursor increase by the pause-to-verified-empty interval. It includes the gated producer and owner inspection interval. Each native owner receipt confirmed an empty Run group before the original reader resumed. Both original and fresh readers agreed on final rendered offset, retained suffix bytes and terminal identity. Each final offset equals the sum of received and explicit dropped rendered bytes. The helper observes the signed installed INTERACTIVE route and actual rendered frames. Its synthetic producer writes controlled bytes and milestones. Native rendering can change the byte count relative to the pipe fixture. The stock report retains its original `missing` entry for native terminal slow consumption because that reading is in the distinct supplementary result.

Both performance driver exits were 0. The collector emits its reports only after the owned Node exits cleanly, the fixture confirms the required Run groups empty, its owned scratch removal completes, and the source and signed/compiled inputs are rechecked. No published release or rollout is inferred.

## Raw receipt locations and SHA-256

These absolute locations refer to the original private host receipts.

- Windows tools directory: `C:/MyFile/Projects/ArcForges/Cloud/.git/arcforges-verify/cache/center02-pg-18.7-win/acc01-final-2e7bef628bcf-tools`.
- Windows PostgreSQL and Go fixture directory: `C:/MyFile/Projects/ArcForges/Cloud/.git/arcforges-verify/cache/center02-pg-18.7-win/host01-fixture-6c57107bed274d0ba0a028033e81b0c2`.
- H-22 tools directory: `/home/sammiller/arcforges/ArcForges/.git/arcforges-verify/launches/acc01-final-2e7bef628bcf-tools`.

| Relative receipt under Windows tools directory | SHA-256 |
| --- | --- |
| `host01-driver.log` | `e856308652680bce01006c394ea2867ba0d7ac4bff2616dae7d7b64e955fd398` |
| `host01.ve_e45_t/fixture.log` | `50c3be03c5a1f6491a2610ab9a5096697e135a3fcf280d79107a65da87eea860` |
| `host01.ve_e45_t/signed-provenance.json` | `59ff4ba132b01ffd13e88a0c211aa057442616e755f7efb7eff46bb5465044bf` |
| `performance-terminal-driver.log` | `9e740351dd6e2e3b9f7f286e94e97fe9b7d6a99a0f091a8fe8126a51da53d353` |
| `native-terminal-perf.3b0m51ff/performance.json` | `fcd3a7bb01b372086b7c83252497ddd7f5fa5f902983d61fc747700771f86b84` |
| `native-terminal-perf.3b0m51ff/native-terminal-backpressure.json` | `ffd66bf9062b5f66508f31991eb906fce896207a1003d25cd6249574d74d995c` |
| `native-terminal-perf.3b0m51ff/native-terminal-owner-exit.json` | `d5373fc9e99d3a0659b43e9d0e60e4305b4b224fe7f0d308383d4da8f9ba212f` |
| `native-terminal-perf.3b0m51ff/native-terminal-paused.jsonl` | `2f99735bc6e5d85922408e9605ada71180e3dd0abcaf9634516f4cd9eb02aa29` |
| `native-terminal-perf.3b0m51ff/native-terminal-fresh.jsonl` | `25c89a2d92133024e0759d287df296b364c3b0c12c57ba8b41a2c5ec915485a6` |
| `native-terminal-perf.3b0m51ff/signed-provenance.json` | `2b16001960b972cb53bdc1f05d5a32d154b0e742390e3c98322f4438425add1a` |

| Relative receipt under Windows PostgreSQL and Go fixture directory | SHA-256 |
| --- | --- |
| `receipt.json` | `bb38b7a21b00f5ab01c5464c194b010a8a5d53227ee9c1caabc8f2c0717e7964` |
| `center04.stdout.log` | `a622e42c33f9e485eaa3793f8d0f0ffd7e0ba1de0adde15ccba71f928a2db22c` |
| `center04.status.json` | `b94866ae3b63dac7cecd393aa524cae6e518fab0838304657889ee7cdf32c021` |
| `pgctl-stop.status.json` | `d75c9ed4891dd91197b0bad4cfac59c51e87d31352c291db3f7b62998f66e32e` |
| `postgres-identity.stdout.log` | `ee1f63b7e6bae2a48561a345f3ff59994ee064d39c34aa00c5ff6b6e5992600a` |

| Relative receipt under H-22 tools directory | SHA-256 |
| --- | --- |
| `host01-driver.log` | `ae0d46ebb0199f33687c103666358d2a7b8faecece1e6a126b192b40b4e0aca6` |
| `host01.jq14urre/fixture.log` | `2a12d181f75cc6fd9d41db4d775616c5bca4edaaca4fc1723c908d9e7c349c44` |
| `host01.jq14urre/local-tls.log` | `2451ed0a7d909e253b1287d21de7532bb36caa0744c80f5da4a96be158009759` |
| `host01.jq14urre/signed-provenance.json` | `c1d96c4e9b2a5ddf28c3bd77ba74ae7ea3d89b2ed850a9454c31c0f60b0e57c9` |
| `performance-terminal-driver.log` | `3e32d1ef853f366e9b10141edad1a1436b60a5866682381b8171a4f7bdbabeb6` |
| `native-terminal-perf.sxnhodwi/performance.json` | `2b1bb7a6e6b5b6297308a89d296719eebd79349ebc1f082050d70d777656561e` |
| `native-terminal-perf.sxnhodwi/native-terminal-backpressure.json` | `fce2cf0d944de13bf9468bfec3bb70743fcbe2d9f01d85bf9a6f2926525b8829` |
| `native-terminal-perf.sxnhodwi/native-terminal-owner-exit.json` | `f321d47d43dbe3a29fe819f394f0afac41feab18bb6315ad42d2d22c9ca82700` |
| `native-terminal-perf.sxnhodwi/native-terminal-paused.jsonl` | `3dbaf872538861901f95d0a555a9cad62235a2a7b415693d90a965e169171f88` |
| `native-terminal-perf.sxnhodwi/native-terminal-fresh.jsonl` | `21757c0c324e7e5ee3555dd74af2340282c801a1fecbf7d9df064f2c1f0ab53d` |
| `native-terminal-perf.sxnhodwi/signed-provenance.json` | `c1d96c4e9b2a5ddf28c3bd77ba74ae7ea3d89b2ed850a9454c31c0f60b0e57c9` |

## Historical failures retained

The first `aced1eb` H-22 performance driver failed before running workloads because Python isolated mode excluded the trusted sibling import. Its original file is `/home/sammiller/arcforges/ArcForges/.git/arcforges-verify/launches/acc01-final-aced1eb012fb-tools.rTOtJyw6/performance.2uy_fomk/fixture.log`, SHA-256 `68f9131d68a7161f3903e6a19071159d247a8b43084eb983f50ca990e0a6f7a4`.

The first `e4c41f6` Windows terminal supplement failed to match its expected anchor. Actual ConPTY rendered the phrase and removed the trailing layout space. The original driver `C:/MyFile/Projects/ArcForges/Cloud/.git/arcforges-verify/cache/center02-pg-18.7-win/acc01-final-e4c41f68e14d-tools/performance-terminal-driver.log` is `cf43c38ebacf12098168c8e55ba820b3ce93282e2212457ae7166b27e756e4bf`. The 166-byte terminal frame remains in `C:/MyFile/Projects/ArcForges/ArcForges/.git/arcforges-verify/launches/acc01-native-terminal-perf/native-terminal-perf.9y2gj_of/native-terminal-paused.jsonl`, SHA-256 `6e4794d7acf6947afc19f6bf89be63364bfb2adb38e3c5243834018081e75622`. The anchor correction and later `e4c41f6` pass are separately recorded in [the main evidence](afv2-acc-01-evidence.md). The original Run stop remains UNKNOWN with its data and receipts retained. Its separate exact service shutdown succeeded. Post-stop confirmation of the original process and native identities is in the same failed evidence directory as `post-stop-owned-native-absence.json`, SHA-256 `d882cdb84e054f0ceb8c6459342db1a6000941c08b80b66f37f10fa85f4e5f10`.
