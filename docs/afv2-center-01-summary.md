# AFV2-CENTER-01 delivery evidence

The qualified engineering candidate is Cloud `8048042b4026006d6d1cf6f160c82b3adc72746d`,
tree `cf0da85b72b11664e4e85bdfa3a79d32233463b6`. [Cloud PR159](https://github.com/ArcForges/Cloud/pull/159)
merged as `6bd7169607d55c8b647b1a70302ff28ad365d488`. The merge tree equals the
qualified candidate tree. Design baseline is `493022fbf643b484665b2713c9eb8670f2fb2234`.
This record closes F-CTR-01 / AR-07 engineering acceptance. Production H-03
inventory, approved production backups and provider authority remain unproven.

## Delivered behavior

Schema12 appends metadata-only management identities, operations, cursors,
entitlements and cutover evidence. Applied0001–0011 remain byte-for-byte intact.
The finite schema10/valid11 transition captures a consistent logical backup,
checks and fences old writers, preserves uncertain outcomes and commits a new
target-specific admission. Restore uses a new quarantined destination, verifies
the closed catalogue and retained data, and renews destination authority.
Management Store reservation, inspection and account-scoped listing use the
existing bounded transaction layer. Node remains authoritative for Run state.

Usage, failure handling and recovery are documented in
[Cloud's migration guide](https://github.com/ArcForges/Cloud/blob/6bd7169607d55c8b647b1a70302ff28ad365d488/eng/v2-migration/center-01.md).
Failures after the schema11 commit retain the committed floor and writer fence;
repair proceeds forward with distinct backup paths. A failed restore retains
quarantine and cannot be adopted by a later invocation. Rollback requires a
coherent accepted cohort and backup, preserving and reconciling subsequent
uncertain effects. No legacy contraction or production migration was performed.

## Required exact-head profiles

Both hosts independently fetched the candidate from GitHub and ran the unchanged
`python eng/verify.py run-and-report`. Windows used the owner's authorized direct
local access; Linux used the designated H-22 MCP. No status or receipt crossed hosts.

| Host | Result | Original summary | Summary SHA256 |
|---|---|---|---|
| Native Windows DEKU | 10/10 PASS,142s | `Cloud/.git/arcforges-verify/logs/20261116-195553-8048042b4026-win/summary.json` | `700d5134c0a74e2b6fef061888ac45178f6107979946b5a8dd7dfac914a6763d` |
| H-22 `v2202601329473427941` | 17/17 PASS,617s | `/home/sammiller/arcforges/Cloud/.git/arcforges-verify/logs/20261116-195604-8048042b4026-linux/summary.json` | `0348ed33480ad02d61a1012504b12e70d4e94daf3e331a0b7ab311b73dbe5991` |

The final Linux profile includes the actual PostgreSQL race suite, failure and
quarantine cases, UNKNOWN reconciliation, native CLI restore drill, source tests,
.NET, Worker/provenance, licence and actual candidate build. Its candidate log
SHA256 is `bbade7327c94ddaa8a3f80027ae5059f969f085a4f0565331f2c973a1ba16fc1`.
The earlier source317 affected race run passed36 test packages; its original log
SHA256 is `2eceed90c653379734493a4576a18e3160a634921be8d92b4adab5aa9f80f9ac`.
The final candidate retains those Go/harness bytes. Earlier failed formal runs
remain failed evidence; none was edited, copied or relabeled as a pass.

## Exact candidate and executable

The local candidate version is `0.1.0-local.1794830688302`. All paths below are on H-22.

| Identity | Value |
|---|---|
| Image ID | `sha256:cac618a497c43bde7aa8617c7be11d24495837f22745e379e74088bc3903f741` |
| Sealed `docker-image.tar` SHA256 | `adc1c5dacd4c4c80fc8d449e89bc1f3fe207e7c3bb45d6b1888aafb309f49a3b` |
| Candidate manifest SHA256 | `103ae4eeba3d5cbd5f65f79889487cc36e9a1c60ece182d6632eedfbe032c91a` |
| Image provenance SHA256 | `ce1204f2b95a038f2c89002ff2f31b039adab160daecf4f85ab2cfac0ab6d9d3` |
| Actual CLI SHA256 | `8417991d1c1357fd5595583a8c996499252971e4504c8dba2f0307a2439b2591` |
| Active profile | `cloud-release-r137`, SHA256 `dfcce65f7f674180b6f24888094b4b87c9a740b6d9b15a61f050907d4bda8cd4` |

The image-provenance file's actual SHA256 is recorded in
`Cloud/.worktree/afv2-center-01-native/artifacts/afv2-center-01-qualified-r137/candidate-input.json`.
The original candidate is under `/home/sammiller/.cache/arcforges-verify/Cloud/artifacts/candidate`.
The initial extraction found the daemon image absent. The coordinator loaded the
same manifest-hashed sealed tar, verified its image ID, and preserved the existing
audited ELF whose digest matches the image member receipt. No image was rebuilt
or published for this drill. The original extraction script/failure are retained;
the successful selector is `artifacts/afv2-center-01-candidate-input-sealed.py`.

R137 retains all452 previous input names and adds the carried management Store;
all453 input hashes and237Go/201C# carried files match. The complete unchanged
Docker-context suite passed6/6. Dependency admission retains all131 external
package coordinates/integrities; current583 input hashes match. Prior profiles,
reviews, SQL and source-provenance records remain immutable.

## Same-CLI three-path PostgreSQL acceptance

The opt-in driver `artifacts/afv2-center-01-final-drill.py` has SHA256
`bec2a47a7e54bce5a7c9db2eeebac49374036d7b2549f795d35f0016986c9221`.
It ran on H-22 from12:08:18Z to12:08:47Z on2026-11-16, using the same qualified
CLI for every current migration/backup/restore command. PostgreSQL was
`postgres:18.7-alpine3.24@sha256:b6972e1115a4ff8eba5d7f7d19184926d1e16d7d1136ae1e1a7ebf286da0f015`,
with `fsync`, `synchronous_commit` and `full_page_writes` all on in every source
and destination. Real `pg_dump`/`pg_restore` used the existing container transport.

| Starting path | Actual operation | Result |
|---|---|---|
| Fresh | Current CLI creates12, seeds real platform state, captures12, restores a new target12 and verifies preserved state | PASS; fresh credential history a→b |
| Schema10 | Historical sealed8e5 executable creates10; current CLI captures10 and transitions10→11→12; the actual10 archive restores into a new guarded target12 | PASS; actual current ELF/source floor and fresh target generation |
| Valid schema11 | Historicala498 executable creates11; current CLI captures11 and transitions to12; the actual11 archive restores11 then transitions the new target to12 | PASS; distinct destination identity and fresh target generation |

Schema10 fixture ELF SHA256 is `028223a3dcbcbd6d7724558de02409e1e8874d876049f03fed38f47998773ba4`,
source `8e5f6e26aa97b123d9f60b91f780364a094e74cd`. Schema11 fixture ELF SHA256 is
`d65219ed3aeefd45bb33a981fe30260a6573836833b885dde31285dbeff56a5b`, source
`a498b4c48e5d2e0a13ee10b14f9ae4426cb13b80`, whose tree matches baseline mainf470.
These are historical fixture identities, not newly established publisher authority.

The original private report is `/tmp/afv2-center-01-final-drill-fi1bdhah/report.json`,
SHA256 `b5b0fb7ee9be014da2ba226d18d6e6f58f401d16879b5bea2452ba23bcbc6bf2`;
`steps.jsonl` SHA256 is `636935170f3474627f9cb76a5cbf88f476a97f6e3c75a218ec8db9b93f08733a`.
All49 steps passed, exit0, all three targets are current12 with distinct database
identities and the same actual artifact binding. All six owned containers were
confirmed absent afterward. Private archives/metadata remain under that0700
directory; they are fixture data and are not published in this repository.

## Review, delivery and stop boundary

Independent nonauthor `/root/base_review` accepted the complete final source,
metadata, original host receipts, candidate identities and real three-path result,
with no unresolved blocker. [PR159](https://github.com/ArcForges/Cloud/pull/159)
records that review. Ruleset and classic protections were unchanged; both native
statuses succeeded at the reviewed head, required Verify was expected SKIPPED,
and no review thread remained unresolved before normal exact-head merge.

The actual merged-main push [run43864301663](https://github.com/ArcForges/Cloud/actions/runs/43864301663)
completed SKIPPED with zero artifacts, under the owner's existing migration pause.
There was no publication, deployment, production-data migration or public activation.
H-03/PROD-01 remain separate closed gates. [Plan PR140](https://github.com/ArcForges/Plan/pull/140)
contains this completion record. Finish its required shared-record checks/merge,
then stop and report; do not start the next product task without a later resume.
