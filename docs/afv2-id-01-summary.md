# AFV2-ID-01 engineering evidence

ID-01 development acceptance is complete. [Cloud PR160](https://github.com/ArcForges/Cloud/pull/160)
merged as `faf5dcb3638916f69fc2b833eea9d8d6d33571e9` from verified candidate
`8c1c67697ecb6727e71a3ccae44526d21408cec5`; both have tree
`c56551d9047b32ce28328109af6e4cb12f296f0d`. Design remains
`493022fbf643b484665b2713c9eb8670f2fb2234`. [Plan PR145](https://github.com/ArcForges/Plan/pull/145)
merged scope/checkpoint `e414f268f1c1df8578059cc10d638d0ad880c2c1`;
[Plan PR146](https://github.com/ArcForges/Plan/pull/146) carries this completion record.

## Final verification and delivery

Both designated hosts independently fetched the exact candidate and ran the original
`python eng/verify.py run-and-report` full profile. Independent nonauthor id_review
accepted all source/metadata/deltas and read both original summaries, every logged
hash, the actual Center executable and all ten sealed candidate payloads. No blocking
finding remains. [Final review](https://github.com/ArcForges/Cloud/pull/160#issuecomment-6936955789).

| Host | Original directory under Cloud/.git/arcforges-verify/logs | Result | Summary SHA256 |
|---|---|---|---|
| Native Windows DEKU |20261117-103902-8c1c67697ecb-win|10/10 PASS,144s|e4920b55162696264aca36b22414bb85fdda7d08701dacb553e0400f2131090d|
| Native H22 v2202601329473427941/sammiller via ssh netcup |20261117-105110-8c1c67697ecb-linux|17/17 PASS,1028s|c2dcd44a447338d6b513f6dc8ee7b485f8ec9a5455ead414c29f655927505862|

Linux used only per-process umask0077, GOMAXPROCS2 and DOTNET_PROCESSOR_COUNT2
after measured failures. These change creation mode and runtime/default worker
parallelism; every original project, test, race flag, count, timeout, fuzz target,
real PostgreSQL, native build, restore and image check remained. Final scopeOOM0.
The original .NET suite passed1923 tests,0 failed,1 expected skip. Center passed
all15 checks, including real PG18.7/race, nine fuzz targets, native startup/shutdown
and schema13 seed/dump/restore/migrate/verify. Its executable SHA256 is
`ff80d8500af9a22178555043859d7b19ac0874b0ea3cb24800c8c362d1fb45df`.
Original Center checks and candidate are under
`/home/sammiller/.cache/arcforges-verify/Cloud/artifacts/center/checks.json` and
`/home/sammiller/.cache/arcforges-verify/Cloud/artifacts/candidate/manifest.json`.

Verified local candidate version `0.1.0-local.1794884525048` has clean revision8c1c,
manifest SHA256 `7665990c1a181554b8ba0f3eb030654ddba08ec594a49c794a172d4919c3a48b`,
Docker archive SHA256 `bceeda92aa567b27c74f3f37896795880e63827cd0d157fcb320e50e000c4a0c`,
and image manifest identity
`sha256:9b575530d5856f0906721c5c99461fa998b96c0d6c5fe46bc646e1a0796839f3`.
Worker164579bytes SHA256 is
`a3a9a97925d906d9f37daada0da15f7b20c4d0b43761d723d51c189f23ca17d5`.
All ten payload hashes and current-run generation times were independently verified.
R138/used records and applied SQL0001–0012 remain immutable; r2 admits the necessary
document formatting input without changing the original131 package coordinates.

[Main-push CI44008751500](https://github.com/ArcForges/Cloud/actions/runs/44008751500)
completed intentionally SKIPPED, all jobs skipped and zero artifacts. Cloud deployment
remains paused; the local candidate is not a published release. Real mail/domain/browser/
provider and production authority qualification remains AR10/H03/H04/PROD, not satisfied
by the allowed external transport/input peers. No public activation occurred.

The task's failure behavior, backup/quarantine/restore and rollback instructions are
in Cloud `docs/center-identity.md`, `docs/postgres-store.md` and `docs/center.md`.
Recovery never uplifts old revoked credentials; unresolved provider/UNKNOWN facts and
required audit/financial retention survive. Export never includes local Sandbox data.
HTTP export pages carry at most32KiB raw data (64KiB response envelope), each section
is bounded to256 rows and the full canonical export to2MiB.

## Host recovery and remaining dependency

Initial root disk recovery restored304045109248B user-available space. A later,
separately audited21 old Go build directories freed3947823104B of /tmp tmpfs memory.
Original inventory/deletion records remain in H22
`/home/sammiller/arcforges/logs/afv2-disk-cleanup-20261117/`;
protected systemd/PAM/SSH process-reference visibility limits are explicitly recorded.
Recent failure work, databases, security producers, source and original evidence were
preserved. No root/sudo or host network/security settings were used or changed.
After final builds, root available space is279349833728B; /tmp is6341808128B available.

After ID01 completion, `python tools/plan.py next` returns null:7 complete,1 blocked,
32 planned. All32 planned tasks transitively require MXC01/AR03, whose real Linux
request-environment argv privacy failure remains. Existing stable1.1.0 source review
still found that path; it was neither executed nor admitted. A supported official
remedy or an explicit reviewed product/profile decision must precede new admission;
this task does not weaken that gate. Detailed original failures and development
checkpoints below remain historical evidence, not additional pending ID01 work.

## Historical verification checkpoints

ID-01 is active after the owner authorized local `ssh netcup` to the sameH22,
superseding older MCP-only transport wording. Native host and verification gates
remain unchanged. This is the shared implementation and
verification checkpoint, not a delivered or published result. Initial source is Cloud
`3a22bec5e9e4dc29841fbb3b9e96c4b2362c6d00` in [Cloud PR160](https://github.com/ArcForges/Cloud/pull/160).
Design baseline is `493022fbf643b484665b2713c9eb8670f2fb2234`.
Current candidate is `f6b9edc25f5dcdf4e1c73d5e731f892ec3d4cdaa`, tree
`8af897e46cc0577d06794c787becf1f14411c739`. Independent final source review passed;
Windows formal10/10PASS144s (20261117-052223-f6b9edc25f5d-win). The prior H22 run
was found interrupted(exit-15), withoutsummary, after connection recovery. No old
process/lock remains. The first SSH run failed because inherited umask0002 created
Go test output directories0775, correctly refused by the backup guard. Native
original managementCLI10/11 and protected-parent diagnostics pass with process0077.
The next complete run20261117-100316-f6b9edc25f5d-linux passed management/migrate,
but identityapi/provision were killed; its scope recorded oom_kill2 while swap was
full. Preserve both failures; there is still no final Linux pass.

After measured pressure and independent review, the same unchanged profile is
running under driver3786855 with per-process umask0077 and GOMAXPROCS=2. This limits
runtime/default package parallelism and fuzz workers; all original cases/race,
counts/timeouts, PostgreSQL, nine fuzz targets, restore/image and remaining checks
remain. No product or host configuration change. Original log:
artifacts/afv2-id-01-formal-f6b9-ssh-0077-gmp2-20261117/native.log and exit.
This run ended failure372s: check passed172s, but check-dotnet found the old
architecture inventory assertion expected9 versus actual16. Center was stopped
after that failure. Its scope also recorded one OOM kill, without individual PID
attribution; do not attribute the deterministic assertion to memory. The exact
consumer-path Plan amendment precedes source correction and new-head both-host
verification. Original same-head Windows success remains valid historical evidence.

Historical observation before SSH recovery: H22 launched
run20261117-052230-f6b9edc25f5d-linux, then three consecutiveMCP HTTP502 failures
required stopping retries. The native process was not terminated; outcome is
unknown and last GitHubLinux status pending. No merge or completion is claimed.
On resume inspect that existing run before rerun; preserve the valid Windows leg.

Earlier candidate was `94834c591958dd5d24a0bef92888e0d6c2c2099d`, tree
`ca9a2a1416077cb8093ebb554f9274decaa3e9b3`. Independent source/metadata review
passed and Windows formal10/10 passed344s. Same-head Linux formal verification
reported error after ENOSPC (root volume user-available0); it has not passed.
Original Windows run is20261117-004519-94834c591958-win; Linux failed run is
20261117-004529-94834c591958-linux. No merge, publication or deployment occurred.
Plan141/142 authorize the exact source, migration, metadata and co-located tests.
Owner-authorized audited cleanup restored304.0GB available on H22. Same9483
Linux formal profile20261117-044320-94834c591958-linux failed the required Prettier
check for docs/postgres-store.md; security bridge passed195s. The controller
stopped linux-center and later steps; no full pass. A two-line formatting-only
correction and immutable admissionr2 are now committed. Subsequent16nonnull test
assertions were replaced by real assert.ok guards; a stale ingress negativevector
was adapted to the unregistered legacyRequestAccountDeletion. Both deltas received
independent review; nativeLinux ingress27/27 passed. PriorLinuxdb93 completeGo/race/
PG stage passed before the stalevector interrupted fuzz/later stages, so it was
not a full profile pass. Applied SQL and usedr1/R138 records remain unchanged.
Detailed cleanup inventories remain in H22 arcforges/logs/afv2-disk-cleanup-20261117/.
The owner clarified continued authorization for remaining tasks7–40; finish this
task and records, then continue the next eligible task under unchanged gates.

## Implemented behavior

Recovery accepts the same bounded ceremony for eligible and unknown addresses.
It uses real email-code and WebAuthn verification, one-use receipts, rate limits,
current authoritative account epochs and a lock-held live-email recheck. It
replaces credentials and revokes old remote authority. Provider delivery faults
remain actual failed/pending delivery; the UI never claims that accepted means
sent. External SMTP/mailbox and software-authenticator inputs are the task's
explicit peers; real cryptography and PostgreSQL decisions execute unchanged.

Export projects only explicit server-held account data. Each section is capped
at256rows; the complete canonical JSON is capped at2MiB. Every bounded read
rechecks current account/session authority, expiry and the original full digest.
Changing a snapshot invalidates its old receipt. No export body is persisted in
receipts, and no local Sandbox/Run data is read.

Deletion uses an exact operation/revision/command/proof intent. Confirmation
revokes old sessions, approvals and enrollments. A newly authenticated pending
account is limited to status, cancellation, necessary step-up, sign-out and
read-only reconciliation of an existing successful confirmation command. The
owner maintenance CLI performs actual providerless self-hosted cleanup; personal
credential/proof/name fields are removed. Actual subscription or UNKNOWN remote
facts retain a visible pending state. Cancellation preserves the prior restricted
account state. No local execution or data deletion is emitted.

Schema13 is an original unpublished forward migration. Applied0001–0012, old
oracles, prior cutover facts, financial/audit tombstones and unresolved operations
are preserved. Finite12-to13 captures a real backup, fences all seven schemas and
old connections/membership paths, changes the NOLOGIN runtime generation and
atomically advances role/OID floor/admission. Restore uses a new quarantined
target, revokes copied account/session/proof/export authority and retains deletion
and UNKNOWN facts. Unsupported legacy deletion RPCs are explicitly excluded from
the published inventory because their existing ABI cannot bind the required
proof/plan; typed implemented pages use the actual operation intent.

## Targeted original native evidence

H-22 is `v2202601329473427941`, user`sammiller`, Debian13; the native worktree is
`/home/sammiller/arcforges/Cloud/.worktree/afv2-id-01-native`.
All checks below use native Go1.27.4 with the race detector and actual pinned
PostgreSQL18.7. `fsync`, `synchronous_commit` and `full_page_writes` are on. Native
`pg_dump`/`pg_restore` execute through the owned container. Log paths below are
relative to that worktree. These targeted checks are not required host statuses.

| Exact source | Actual result | Original log |
|---|---|---|
| `be9d2f8ded5819ff50ee8c897f8ebd99dcd3fe36` |10top-level cases PASS: fresh inventory,5identity cases,1session case with3locking subcases,3actual HTTP cases | `artifacts/afv2-id-01-targeted-be9d/native.log` |
| `cba8a20b887e266ffe9f359770dc9ec6573f5d3f` |Changed recovery-channel-removal race, owner-name cleanup and final inventory PASS; exit0 | `artifacts/afv2-id-01-delta-cba8/native.log` |
| `1b690454d52b010b01f4076c5426cf18f0a9108b` |Open-session/management-only writer refusal and SQL-fault rollback PASS; overall exit1 from historical seed parameter ambiguity | `artifacts/afv2-id-01-migrate-1b69/native.log` |
| `abaae9f3836643e8cba489d0e0fb14fed7043ea7` |Finite10/11/12 paths allPASS; overall exit1 from the restore source fixture's missing confirmation fields | `artifacts/afv2-id-01-migrate-abaa/native.log` |
| `3a22bec5e9e4dc29841fbb3b9e96c4b2362c6d00` |Real backup/restore13 PASS3.93s, exit0; epochs7/4 become8/5, old session/proof snapshots are revoked rather than uplifted, deletion/UNKNOWN/cutovers preserved | `artifacts/afv2-id-01-restore-3a22/native.log` |

Only explicit UUID-before-text casts and valid supplied confirmation facts fixed
the two fixture failures. Assertions and production constraints were retained;
these owner-supplied historical data facts are not proof-ceremony success. Initial
pre-Go runner errors and archive-ACL failures remain in their original artifacts.
The actual named-ACL/unnamed-FUNCTION distinction has one exact closed mapping,
with complete-TOC positive/negative tests. A successful MCP call resets the outage
counter; no native outage occurred in this resumed checkpoint.

The first schema13 source oracle was generated from actual`cba8`PostgreSQL:
381unique objects, inventory SHA256
`0f26a23b7e39b4b4f9ab8f859e647f822e6e39eac41c1383028d484121972578`,
catalogue`5fb4f156d72ed7040d839e76d82028ffb3e769a085e319bf501fbe18871ff30b`,
0013normalized SHA256
`9936d566131f26aa470bf63494f0167391a76c0824b2a57c99ef01f4dcde5d4e`.
The canonical inventory is a necessary checked-in source artifact; original native
receipts stay on H22 and are never reused as another host's verification.
The unchanged mandatory foreign-key index check then found one missing index.
A single nullable lifecycle-reference index was added to unpublished0013; no old
SQL or constraint changed. H22`e62dac9b80bc40e4d364cddff39efce370f9609a`passed
that check and captured its actual successor:382objects, inventory SHA256
`4f3eea6a132861d604ff1a94cf53aa320eef9e6bdec546e0ce43be677fa5531e`,
catalogue`ba0db874e2abf564139893cd5009c14873d9e57ea54a1d381d9e2318fbbb1530`,
SQL13SHA`1014d5163065ff585e51bc7ef901c44a10356f53f3597c3be122017d41bde946`.
The final source-oracle binding and exact consumer-test adapters are at`31525fc8`.
Its standard-PG/log/race full identityapi/pages/migrate suites passed89.345s,
79.109s and69.493s, exit0, with no data race. Original native log is
`artifacts/afv2-id-01-compat-3152/native.log`. Earlier381objects remain historical
facts, not rewritten current-admission evidence. Full identity/provision at`70ec`
passed7.156s/19.530s. The original full diagnostic's missing PG preload/log setup
is retained as an orchestration error; no full-suite pass is inferred from it.


## Historical review and then-remaining delivery

Independent`id_review`reviewed the complete core/transport source and the revoked
email, retained hostname and delivery wording fixes. Independent`base_review`
accepted the migration/oracle/fixture slice at`3a22`and read the original native
results. One floor concern was withdrawn after exact-blob verification showed the
correct existing atomic implementation; no speculative duplicate fix was made.

Windows all-Go compilation and browser-script54/54/TypeScript author checks passed.
At that earlier checkpoint, the actual locked Wrangler dry-run built164579bytes, SHA256
`a3a9a97925d906d9f37daada0da15f7b20c4d0b43761d723d51c189f23ca17d5`,
27parsed/26emitted inputs, without publication. Affected real-PG compatibility checks have passed and original metadata closure
is in progress. Final exact-head required
Windows/Linux profiles, final independent review, normal merge and shared complete
state still remain. No final status, merged artifact or publication is invented.

Real mail/domain/supported-browser/provider qualification remains AR10/H04 and
production inventory/authority remains H03. These development peers do not close
external acceptance or authorize public activation. Cloud's deployment pause and
separate AFV2-PROD-01 approval remain in force. Rollback/recovery follows Cloud's
updated postgres-store and identity guides; restore never erases post-backup
UNKNOWN facts or restores old remote authority.
