# Codex handoff — ArcForges V2

## Current DATA P1 fix pushed, new-head qualification pending

Node draftPR94 final candidate165913b2cdd61b66f3fdf7ffe6bff5a062b7f418,
treeb065cefdd50b0104378c1d69375a51c2ea5f8dd6. Only5allowedpaths changed
from1e02: schema16 SQL state/retired_utc UPDATE guard and hash16,2existing
fixturefiles/docs. No retirement product API/automaticrotation added. Reject
unqualified retirement before state changes; suppliedRETIRED fixture refuses
admission/maintenance and reactivation. Original independent failure preserved.
All old1..15SQL/history remain byte-identical. Author ended before base_review
resumed focused delta review; do not merge until actual final acceptance.

Windows currentbuild0warnings/errors33.80s,19/19PASS0skip41.854s,
artifacts/afv2-data-01-retirement-guard-{build,tests,format}-win.log.
H22 final19/nativeformal must wait oldLinuxexclusive finishes to keep required
resource measurements alone. Old1e02 formal processes still own their exact
cached checkouts and report only oldSHA. Windows oldCI has one EventStream
70000 timingbranch failure, full state converged; it overlapped cold baseline
AOT148s. Core/test/gate untouched. Finalhead must get original both fullprofiles;
base39cache now warm. Investigate further only if actual finalhead check fails.

Next root: finish/record oldprofiles, fetch165 independently both hosts, run
H22 changed19fixtures, delta review, new-head unchanged run-and-report both,
merge only reviewed passed head; then complete Plan record and next task.

## Earlier DATA independent review P1: do not merge1e02

Independent reviewer base_review ended with one real reproduced blocker:
known no-effect settlement, backup, existing fixture SQL RETIRED transition,
latest DB rollback while retaining fence allowed old ACTIVE restore. The state
change was only in SQLite, not the independent fence. Expected maintenance was
not thrown. Single nativeWindows real SQLite/file-key case failed,0skip;
review build0warnings/errors. Reproduction retained in isolated
ArcForges/.worktree/review-afv2-data-01-1e02/tests/ArcForges.Node.Store.Tests/
DurableRetirementRollbackReviewTests.cs. Author worktree was not changed.

Reviewer ended before sole author base_audit resumed concentrated fix. Prefer
refusing unqualified DB-only retirement/maintenance, no new retirement product
workflow or automatic rotation. Keep old1..15 bytes/history unchanged and add
precise real fixture. Both old1e02 full profiles may finish but cannot waive
this P1. Root must push fix, H22 same-head changed fixtures, delta review and
both new-head unchanged formal profiles before product merge. No delivery yet.

## Earlier DATA qualification running at1e02

Same source1e02e335b97c25b8a05808c90c82c608f3c31c36, Node draftPR94;
current Plan draftPR127 / branchplan/afv2-data-01-final.
Both native17-case fixtures passed (Windows10.879s, Linux4.418s, zero skips).
H22 host/bench authorAOT completed explicitexit0, both0warnings/errors,
artifacts/afv2-data-01-aot-publish-linux-1e02.log/.exit.
Windows publish log has both0warning completed summaries and exact artifact
hashes in ledger; cross-agent session37666 was unavailable and wrapper exit
not obtained, so do not infer it. Standard four-RID locked restore fixed only
the initial -rwin-x64 invocation mismatch, no source/lock change.

Author ended before sole independent reviewer base_review started. Root owns
native checks/push/PR/merge/records. Unchanged full Node profiles are running:
Windows source fetched independently into .worktree/afv2-data-01-verify;
root execsession40227, common git log20261116-151921-1e02e335b97c-win.
H22 data-native backgroundPID3124628, artifacts/afv2-data-01-formal-linux-1e02.log
and eventual .exit. Actual statuses pending. Preserve all original logs;
no passed full profile, final review, merge or delivery claimed yet.

Next: monitor real profiles, resolve only actual failures/review blockers,
review any source delta and obtain new-head statuses if changed, merge only
reviewed head, record actual merge/delivery, then next eligible authorized task.

## Earlier DATA candidate: complete owner backup closure

Actual shared Plan126 merged709795fbfaee6143d195029d4d14b7cf52773ab5;
both exact-head native profiles5/5 bind Design493, original summaries in ledger.
New Plan worktree .worktree/afv2-data-01-final / plan/afv2-data-01-final;
coordinator owns records, author/reviewer remain serial.

Node PR94 current pushed head1e02e335b97c25b8a05808c90c82c608f3c31c36,
16paths allallowed, no project/package/lock changes. Author source editing stopped.
Catalogue gate now serializes owner creation/backup/restore; restore compares
external latest DB complete owner/epoch/state/history and exact signed fence set.
This fixes the concrete post-backup new-owner omission. Three new real fixtures
cover two-owner/key closure, new-owner rejection and old-DB/new-fence rejection.

Current Windows build0warnings/errors3.43s and17/17PASS0skip10.879s,
artifacts/afv2-data-01-backup-closure-build-win-2.log / backup-closure-tests-win.log.
Initial nullable CS8620 failure retained in backup-closure-build-win.log.
H22 independently fetched1e02: current Store.Tests build0warnings/errors4.75s,
17/17PASS0skip4.418s, original artifacts/afv2-data-01-tests-build-linux-1e02.log
and durable-tests-linux-1e02.log, explicit exits0. Real permissions and two
children are included; effects remain only supplied fixtures/synthetic counter.

Affected host/bench AOT, independent nonauthor review, both exact-head required
Node full profiles and merge remain pending. No product acceptance/delivery yet.
Author transfers Windows AOT session to root before reviewer starts; no second
delegated worker at once. All earlier failures/evidence below stay historical.

## Earlier DATA correction and pending backup closure

Node head564f2dcc38763bd3ecc93cda3060d2dfde5a4e5a is pushed in PR94.
It changes only existing StageProducerAdmissionTests to current schema/current+1;
both original floor-refusal and missing-function assertions remain. Prior full
Store run782 failed only those2: Windows152pass/2expectedskip/2fail123.990s;
H22Linux151pass/3expectedskip/2fail126.257s, explicitexit2 retained. Changed
Stage3/3PASS0skip on Windows3.401s and Linux0.720s; Linux incremental build
0warnings/errors. Logs artifacts/afv2-data-01-stage-fixture-build-linux-564.log
and stage-fixtures-linux-564.log, exits0.

Author base_audit must first finish checking/fixing complete latest-owner closure:
a post-snapshot newly created owner/epoch must invalidate an old backup too;
manifest-listed owners alone are insufficient. This directly affects DATA backup
acceptance. No final review/full profile is started until production source stable.

H22 userfree now3371986944B after measured/bounded cleanup of only four retired
Desktop ignored/untracked bin/obj directories in the existing formal verify cache.
Exact paths/checks are in ledger; no evidence/delivered artifacts/source deleted.
Unchanged Host project locked restore passed in data-native worktree, preparing
for final affected AOT. Native14case782 logs and all failures remain intact.

## Earlier coherent DATA candidate and real native diagnostics

Node draft PR94: https://github.com/ArcForges/ArcForges/pull/94
Branch task/afv2-data-01, exact pushed source782ee4a69e22727db3cf3de7b018b09baa5e56cf;
14paths within allowed scope, no project/package/lock change; author tree clean.
Windows targeted14/14PASS0skip9.769s, Store.Tests build0warnings/errors;
original artifacts/afv2-data-01-{durable-tests-win-5,tests-build-win-5,format-win}.log.
H-22 independently fetched782 into data-native worktree. Release no-restore
warnaserror build0warnings/errors6.86s; same14/14PASS0skip4.240s with real
Linux permissions and two real children. Original artifacts/afv2-data-01-
tests-build-linux-782.log and durable-tests-linux-782.log; explicit exits both0.

These supersede pending source/process snapshots below, retained as history.
No product runtime proof, formal status or delivery claimed. Linux full Store
regression PID3116956 / artifacts/afv2-data-01-store-regression-linux-782.log
still running and already has two StageProducerAdmissionTests failures;
sole delegated author base_audit notified and continues Windows regression.
Fix affected regressions before AOT/final review. Windows affected AOT,
independent review and both unchanged exact-head host profiles remain pending.
Last H-22 user-free310038528bytes; existing verify cache9.3GB was read-only
inspected, no cleanup. Preserve all raw evidence and historical drafts.

## Earlier pending real-process DATA fixture implementation choice

Use the existing Store.Tests MTP executable with exact method filter/no-build
and test-local phase/root, twice: first real process admits/settles with real
SQLite/file keys; next process compacts/replays original epoch/command using
explicit fixture time. The effect is only the allowed synthetic counter.
Existing bench store-growth only admits empty roots and cannot prove this replay.
No new project, solution/tools registration or product environment hook is needed.
Own child timeout/exit/cleanup evidence must be recorded. This scenario is still
pending, not a native pass. The five-case Windows partial result remains separate.

## H-22 dependency preparation for current DATA fixtures

In /home/sammiller/arcforges/ArcForges/.worktree/afv2-data-01-native at clean39c,
eng/check_toolchain.py and locked Store.Tests restore logged Python3.15.2,
SDK11.0.100 and all3Store/Bench/Store.Tests project restores (1.31s).
Original log artifacts/afv2-data-01-dependency-prep-linux.log. This is dependency
preparation only; no product build/test/status. Tracked source remains clean;
last userfree444,755,968bytes. Reuse assets after fetching the exact pushed source;
rerestore only if actual project/lock inputs change. Windows author continues
the remaining real fixtures; the current partial five-case result follows.

## Current DATA partial Windows fixture milestone

Author still implements an uncommitted Windows working-tree variant.
Root read actual artifacts/afv2-data-01-durable-tests-win-1.log:
DurableCommandStoreTests5/5PASS,0skip,2.428s. Latest author Store/Store.Tests
builds passed0warnings/0errors. This is not a committed candidate or Linux/
formal acceptance. Schema15/CAS/fault/permission/real-process/AOT and affected
regression remain pending, so do not deliver or use the old build as latest proof.

Backup code now uses realSQLite onlinecopy, existing V1 sealed-value sanitation,
full epoch-key/manifest closure and independently retained latest authority with
owner-control lock; post-effect observations also advance fence. No backup can
self-certify missing later history. Author reports the five initial cases cover
compaction/reopen,UNKNOWN/terminal exclusion,key/DB-loss no rotation,coherent/stale
effect restore and realSQLite safetyreserve; exact final-head rerun still required.

Additional uncommitted files are DurableStoreBackups.cs and
tests/ArcForges.Node.Store.Tests/DurableCommandStoreTests.cs. All changes remain
under the three allowed paths. Full older snapshot/details follow. H-22 data-native
worktree remains clean39c awaiting first pushed candidate; root alone runs it.

## Current DATA partial build and integration snapshot

Author working tree remains uncommitted, within three allowed directories.
Additional files since earlier snapshot: DurableCommandResults.cs;
NodeStore.cs and Migrations/StoreBackups.cs now modified for integration/backup.
Current uncommitted source also includes DurableEpoch.cs, DurableCommandStore.cs,
Schema/0016-v2-expand.sql, schema-history.json, StoreMigration.cs and
eng/v2-migration/afv2-data-01-source.json. Preserve all current author work.

Partial Windows author diagnostics:
- artifacts/afv2-data-01-toolchain-win.log: actual check_toolchain.py pass after an
  initial missing-artifacts redirection did not execute it.
- artifacts/afv2-data-01-store-restore-win.log: locked Store project restore pass.
- artifacts/afv2-data-01-store-build-win.log: initial CS0121 HMAC-overload failure.
- artifacts/afv2-data-01-store-build-win-2.log: corrected variant Release
  --no-restore -warnaserror -tl:off passed0warnings/0errors1.89s (root read tail).

Latest NodeStore/checkpoint/backup edits are AFTER that built variant and remain
unbuilt/untested. Do not reuse the partial build as final candidate proof.
No product commit, acceptance fixture result or native Linux result yet.
Author is completing backup/restore/real fixtures. Owner history fence advances
on post-admission effect observations too; restore never trusts the backup's own
bundled fence as independent latest-history evidence. No automatic rekey/epoch reset.
Current detailed scope/native venue and older snapshots follow.

## Current DATA source snapshot (implementation in progress)

Windows task/afv2-data-01 currently has uncommitted module-local work:
- src/ArcForges.Node.Store/Migrations/StoreMigration.cs (migration registration)
- src/ArcForges.Node.Store/Schema/schema-history.json (new step history)
- src/ArcForges.Node.Store/Schema/0016-v2-expand.sql (forward V2 expand)
- src/ArcForges.Node.Store/DurableEpoch.cs and DurableCommandStore.cs
- eng/v2-migration/afv2-data-01-source.json (source/mapping evidence)

This is a partial implementation snapshot only. No product commit, build/test
result or native acceptance is claimed. No old0001..0015 file appears modified.
Author base_audit continues; do not overwrite these drafts or treat them as ready.
H-22 remains clean39c in its new data-native worktree. Current task/scope and
baseline details follow; source changes stay in the three permitted paths.

## Current checkpoint: DATA-01 implementation active

Startup Plan125 actually merged926af0616d6738d8cc525bcc93ac59eb8d23f311
at reviewed544132d4413042159c73946c6cd372f4c7418601/tree45cc6bf33aad317c7e52e72782a459a66ff81fe0.
Native Plan Windows141510/Linux141518 each5/5 bind actual Design493022fbf643b484665b2713c9eb8670f2fb2234;
strict status/current head/base/no bypass/zero threads checked before merge.
API-01/cohort481.1 complete, AR03/MXC01 stay failed/blocked in their own range.
DATA-01 is the sole active authorized task; no product acceptance yet.

Sole delegated author base_audit works in Windows
C:/MyFile/Projects/ArcForges/ArcForges/.worktree/afv2-data-01,
branch task/afv2-data-01 baseline39c2c57fdaf3666ec046a22370aa2f2157c2d058.
Current assessment: reuse WAL/single writer/FULL transactions, existing migrations/
backups/protected-key helpers and real-process fixtures; keep every applied0001..0015
byte/checksum/history, V1table and unresolvedintent. Do not reuse legacy24h dedupe
identity eviction for V2. Implement forward schema16/minreader16 and only missing
V2 epoch/HMAC receipt/known-body compaction/UNKNOWN/CAS/reserve/backup primitives.

Only actual DDL conflict is old resource_sample(attempt_id/sampled_at).
Preserve it; new V2 physical table v2_resource_sample maps logical resource_sample
(scope_kind/scope_id/observed_utc) in an explicit eng/v2-migration record.
The Design target is not an upgrade script; this is a narrow physical expand
adaptation, no source table contraction/new naming framework/semantic waiver.
Final independent review must inspect it.

H-22 native worktree exists, clean at39c2 with correct origin:
 /home/sammiller/arcforges/ArcForges/.worktree/afv2-data-01-native
Measured tracked checkout10,359,037bytes, current userfree445,399,040bytes after it.
Python3.15.2/SDK11.0.100 verified; no install, cleanup or duplicate baseline tests.
Root alone handles Linux, formal status/push/PR/merge/Plan. One delegate at a time;
reviewer idle. Author Windows implementation/targeted realfixtures in progress,
no product commit/nativeLinux validation or full status yet. No active nativeprocess.

Record branch: Plan/.worktree/afv2-data-01-progress on
plan/afv2-data-01-progress, base926af06. Next: author candidate/precise source and
test evidence, push, independent H-22 fetch and realSQLite fixtures, fix actual
blockers only, then author-stop/independentreview/final both native Node profiles,
strictmerge and accurate final delivery. Source/protected-key material never logged.
Only the task's explicit synthetic admission effect-counter is permitted; no real
Run/NodeIPC/CLI/Stop/grant-revocation result can be claimed here. Preserve existing
Cloud CI/base/MXC/otherproduct drafts. No production activation. Continue serially.

## Current checkpoint: DATA-01 active after completed API-01

The owner requires continuous serial execution. API-01 and ordinary481.1 cohort
are complete; final Plan124 actually merged7e66141e217b5ad5544c5d1af72cdeabc6f4279e
at reviewedce6ccb17ddc688c89a76761b68a94c78a4d10322/tree94de39d18577a13fade7e5924977a92e1799be6e.
Native Plan Win135941/Linux135929 each5/5 bind actual Design493022fbf643b484665b2713c9eb8670f2fb2234.
Strict both-host/current head/base/no bypass/zero threads and review checked.
This checkpoint supersedes historical task states below.

AFV2-DATA-01 is now the only active task; BASE-01/API-01 dependencies are complete.
No product implementation or validation outcome claimed yet. MXC-01 remains blocked/
AR-03FAILED only in its dependent range; ENV/BASE-01/BASE-02/API-01 stay complete.
No public activation authority or Cloud deployment has been enabled.

Actual baselines fetched: Plan7e66141e217b5ad5544c5d1af72cdeabc6f4279e,
Design493022fbf643b484665b2713c9eb8670f2fb2234,
Node39c2c57fdaf3666ec046a22370aa2f2157c2d058. Git origins verified, primary
Windows/Linux Node checkouts remain unmodified at200d2d25. All existing worktrees
inspected; no previous DATA draft/PR found. Preserve BASE01/MXC/Cloud CI and all
other worktrees. New Windows Node/.worktree/afv2-data-01 on task/afv2-data-01;
Plan/.worktree/afv2-data-01 on plan/afv2-data-01. Product directory is ArcForges,
Design directory is ArcForges-Design (not the old handoff shorthand Design).

Scope: only Node src/ArcForges.Node.Store/**, tests/ArcForges.Node.Store.Tests/**,
eng/v2-migration/**. Read current Node AGENTS/CONTRIBUTING, full task and4Design
refs completed. Keep migration0001..0015 bytes/checksums/min-reader history,
unresolved legacy intents and valid existing WAL/transactions/encryption/backups.
Adapt with forward-expand V2 tables, protected random epoch/HMAC identity,
retained known/UNKNOWN receipts,24h known-body compaction, reserve/capacity and
coherent backup/restore. Add only missing primitives and real fresh/schema15
SQLite/key/permission/close-reopen fixtures. Only explicitly allowed synthetic
admission effect-counter; no native Run/IPC/CLI/Stop/revocation acceptance claim.

Windows uses expressly authorized native local filesystem/tools. H-22 MCP was
freshly called: correct hostv2202601329473427941/usersammiller/origin/workspace,
clean primary/healthy transport. Last disk observation439MiB useravailable;
monitor and reuse known own worktrees/builds, never delete unknown directories.
No active native process. Coordinator owns Plan/nativeLinux/push/PR/merge;
one delegated author or reviewer at a time.

Next: commit/push this startup record, both unchanged Plan native profiles and
merge; then author a bounded keep/adapt/add assessment of actual Store source,
reuse its key/backup/migration helpers and implement complete DATA-01 acceptance.
Do not restart dependency upgrades, old V1 tasks, nativeMXC experiments or unrelated
products. Formal Node final PR requires both native host profiles and independent
review. Every failed primitive remains explicit; no unsafe rollback/epoch reset.

## Current checkpoint: API-01 complete; final Plan record awaits checks/merge

This checkpoint supersedes the historical intermediate snapshots below.
The user requires continuous serial delivery; after this record merges, start
the next eligible authorized task rather than ending at the task boundary.

### Completed API-01

- Contracts PR140: https://github.com/ArcForges/Contracts/pull/140
  Actual merge c22be9a7da5a747b4a14b1b81d78f0ea460f810f, reviewed/tested head
  9d27110969fb3d7b2a347a8b487d945a3721cb56. Both share tree
  318db47ce162b67b57252de44e8925929cceaea2.
- H-22 required unchanged full profile passed all20steps in556s. Original receipt:
  Contracts/.git/arcforges-verify/logs/20261116-132451-9d27110969fb-linux/summary.json,
  SHA25648c4d86ab5ed00c202158f4da901dcac1f5f95bc7e9d5513c7718d9f069df95b.
  Includes649toolingtests, pack/Native AOT, Go/static/test/exchange/vulnerability,
  security and the original shared architecture gate. Independent base_review
  accepted complete source, final deltas and actual final evidence. Strict required
  status/current head/base/no bypass/zero review threads were checked before merge.
- Ordinary cohort1.0.0-ci.481.1 is published:19NuGet packages, retained internal npm
  @arcforges/ai-internal, and go/v1.0.0-ci.481.1. Main-push run43811258953 succeeded,
  actual publishing steps in all3jobs succeeded; Go tag directly points to mergec22.
  https://github.com/ArcForges/Contracts/actions/runs/43811258953
  Candidate artifact14200813608 (16513026bytes), metadata SHA256
  18d53a6d8fd00755d4f6614325dd7ebd123e76f97980ce661ea5ed0546eed13c.
  Only publication metadata was inspected; no repeated downloads/rescans/consumers.
- Windows AOT/Release and exact-source1efa native Go qualifier originals, plus all
  real earlier failures, remain in native locations and the append-only ledger.
  No SQL, old schema/checksum, independent consumer pin or deployment was changed.

plan.py recorded API-01 delivered then complete, including actual PR/merge and all
three publication channels; sequence regenerated. No API acceptance-register row
exists. Keep AR-03FAILED/MXC-01blocked, AR-13PASS and completed ENV/BASE tasks intact.
MXC rejection remains a real privacy failure and blocks its own dependent range.

### Final record before the next task

Plan/.worktree/afv2-api-01-final on plan/afv2-api-01-final; draftPR124:
https://github.com/ArcForges/Plan/pull/124
Base actual Plan main7cfd4d725c0dc3586831af37ea3bc34af38a723c; Design main
493022fbf643b484665b2713c9eb8670f2fb2234. Next: push final record, obtain both
unchanged native Plan5step profiles on that exact head, check both Design-bound
summaries against freshly fetched actual Design main, review/protection/threads
and expected-head merge. Record the actual Plan124 merge in the next startup ledger.
No native or CI process remains running; no source work is uncommitted.

### Next eligible authorized task: AFV2-DATA-01

plan.py next selects DATA-01: add V2 Node persistence and durable mutation receipts.
Dependencies BASE-01/API-01 are complete; AR-03 does not block this store-only task.
Read the full task plus current Node AGENTS/CONTRIBUTING and Design node-store.md,
node-store.sql, migrations.md and contracts README before implementation.
Allowed product paths only: ArcForges src/ArcForges.Node.Store/**,
tests/ArcForges.Node.Store.Tests/**, eng/v2-migration/**. Inspect actual latest Node
main and all worktrees first; preserve existing drafts and use an isolated worktree.
Scope is forward expand migrations, owner_epoch/immutable command-intent receipts,
UNKNOWN preservation/compaction/capacity, coherent database/key backup/restore and
real fresh/schema15 SQLite/WAL/permission/close-reopen fixtures on both native hosts.
Never edit applied0001..0015 or contract live tables. Only the task's explicit
synthetic effect-counter admission fixture is allowed; actual Run/IPC/CLI/Stop/
grant revocation remains CORE-02/REC-01/CLI-01 and cannot be claimed from it.
After Plan124 merges, mark DATA-01 active and ledger the exact scope/baselines,
then implement the smallest complete task. Public activation remains separate PROD-01.

## Current API-01 merged source; ordinary cohort pending

This checkpoint supersedes all intermediate snapshots below.
Contracts PR140 actually merged c22be9a7da5a747b4a14b1b81d78f0ea460f810f.
Reviewed head 9d27110969fb3d7b2a347a8b487d945a3721cb56 and merge have identical
tree 318db47ce162b67b57252de44e8925929cceaea2. H-22 full20/20 PASS556s,
649 tooling tests108.203s and shared architecture229s. Original receipt
20261116-132451-9d27110969fb-linux/summary.json SHA256
48c4d86ab5ed00c202158f4da901dcac1f5f95bc7e9d5513c7718d9f069df95b.
Independent base_review accepted final source and evidence; strict required
Linux success/current head/base/zero threads/no bypass were checked before merge.

Ordinary main-push CI run43811258953, number481/attempt1, exact merge c22:
https://github.com/ArcForges/Contracts/actions/runs/43811258953
Build candidate is provisioning the reviewed native toolchain. Publication has
not yet been confirmed. Graph stays API-01 active; merge evidence is in the ledger until the real delivery transition can attach graph evidence.
No publication identity, delivered/complete state or runtime activation claimed.

Next: inspect this existing CI and actual19NuGet/internalnpm/Go publication
metadata; do not repeat consumers/downloads/rescans or enable deployments.
Then use plan.py delivered/complete, sequence, final Plan124 evidence/handoff,
both native Plan profiles against actual latest Design main493022f, and merge.
Continue the next eligible authorized task. Final-record worktree/branch:
Plan/.worktree/afv2-api-01-final on plan/afv2-api-01-final. No native process is
running; only GitHub ordinary publication CI. User requires continuous serial work.

## Current API-01 candidate9d precise AT-12 integration repair

Candidate9d27110969fb3d7b2a347a8b487d945a3721cb56 is pushed draftContracts140.
Root cause:7 new generated auxiliary public types were absent from existing
WireSchemaCatalog. Only two ArchitectureTests files change (41addlines), binding
exact two V2 owners/three declared output names to their owned protocol anchor,
using existing Services aggregation semantics. Original Contract/Generated/AT12/
hash/drift checks stay; no waiver or policy change. Crossowner/oldowner/nested/
fake-output negatives pass, Windows incremental build0warnings0errors/local
fixtures pass, not a shared formal success. Source1efa Go qualifiers unchanged.

H-22 independently fetched9d and started unchanged full20step profile,
PID3088638, background/home/sammiller/arcforges/logs/afv2-api-01-formal-9d27110.txt.
Shared architecture gate will run once inside this full profile, avoiding an extra
3minute duplicate gate. Independent reviewer base_review is auditing the precise
binding delta against original AT12. Author idle. Observe real final summary/review,
then strict gates/expected-head merge/normal cohort publication. API still active;
no full success, merge or publication yet. DraftPlan124 contains all current records.

## Current API-01 AT-12 diagnosis complete

Safe H-22 diagnostic completed GATE_EXIT1: exactly7 AT-12 findings, only new
Management.V2.csproj(3) and Sandbox.V2.csproj(4), no otherRule/Path findings.
Safe stdout log/home/sammiller/arcforges/logs/afv2-api-01-policy-diagnostic-2ede.txt
SHA425e96cb5c6c1c86dacb04bcf142f23758e32ca2f3088ac80bce4da6473b1c23;
diagnostic.logSHA5bd5dec8e204574c912c72c8836b61c12c145d8776a135ce9b73f5c1ebffb126
in cache ignored artifacts/...-6qfqjd0g. No Message was read/printed.
Source restored byte-identically, HEAD2ede and emptygitstatus rechecked; original
formal failure summary hash unchanged dcd4620b5980ac5b75d4f350f6b07ecb85d20fce8a32f93b45c17151025a8423.
No process remains active from that diagnostic. This never counts as a formal pass.

Author base_audit is reading only pinnedAT-12 and existing Contracts wire/test
binding/catalog to fix the actual new V2 integration. No waiver, threshold,
policy/gate or unrelated product change. Next: precise small fix, targeted check,
independent review/new finalhead formal20step; sourcemerge/cohort/Plancomplete
remain outstanding. API is still the sole active task.

## Current bounded architecture diagnostic process

H-22 diagnostic-only PID3086285 is running on clean2ede in formal cache
/home/sammiller/.cache/arcforges-verify/Contracts. Background log
/home/sammiller/arcforges/logs/afv2-api-01-policy-diagnostic-2ede.txt;
ignored output artifacts/afv2-api-01-policy-diagnostic-2ede-6qfqjd0g.
Helper source/root review and native code hash are in latest ledger. It uses the
existing host lock, rejects live formal PIDs, temporarily prints only sanitized
PolicyFinding.Rule/Path, builds separate ignored output, restores exact original
source bytes in finally BEFORE diagnostic DLL evaluation. Actual Git status was
observed clean after restoration. Original if/throw and nonzero exit remain;
Message is never read/printed, formal verifier/status/receipts untouched.

This is diagnostic only, never a formal pass. Observe its Rule/Path output and
GATE_EXIT, then fix only that actual current V2 integration issue. Author base_audit
is paused awaiting result, no concurrent build/investigation. Current formal2ede
still fails architecture after19passes; draftContracts140/Plan124 preserved.

## Current API-01 architecture gate failure after19passed

Full2ede7f6b8b7b7c65fabc99849d139ead29f3d01a tree
49e1f8f96ee05a2afe355b65d510afb810460797 finished19/20PASS, but architecture-gate
FAILED after203.3s at fixed stage ValidatePolicyResults. All649toolingtests passed;
pack/AOT/Go/static/vulnerability/security/naming/clean checks passed. Native summary
Contracts/.git/arcforges-verify/logs/20261116-130212-2ede7f6b8b7b-linux/summary.json
SHA256dcd4620b5980ac5b75d4f350f6b07ecb85d20fce8a32f93b45c17151025a8423.
Actual required Linux status is failure. No formal process remains running.

HostedPolicyGate.cs receives nonempty PolicyEngine.Check findings, throws fixed
stage-only failure without exposing messages. SDK01-04negativefixtures passed.
Author base_audit is doing bounded safe ruleId/repository-relativepath diagnosis
on the unchanged policy, no full exception/env/secret dumps, no waiver or scan/gate
changes. Fix only the confirmed new V2 integration issue, then targeted validation,
independent delta review and new final-head full status. Revieweridle after accepting
2ede source/testdelta; source acceptance does not waive this actual required failure.
API remains active, draftContracts140/Plan124 preserve current evidence. No delivery.

## Current API-01 candidate2ede formal verification

Candidate2ede7f6b8b7b7c65fabc99849d139ead29f3d01a is pushed draftPR140.
Only two affected tooling-test consumer modules change after96: strict135groups
with old131 retained and4 exact newly audited groups; strict28packages with all
old26 rows retained and2 explicit V2 owners. Author66/66 DependencyAdmission and
11/11 Identity tests pass; original Windows logs are author artifacts/
afv2-api-01-tooling-consumer-dependency-win.log and
...-identity-win.log. No producer/Go/control/security delta; qualification1efa
stays valid. Author idle; base_review independent delta review is active.

H-22 independently fetched2ede and started unchanged full20step
python eng/verify.py run-and-report, PID3074195, background
/home/sammiller/arcforges/logs/afv2-api-01-formal-2ede7f6.txt. Observe actual new
receipt/summary and final review before merge. API remains the only active task,
no complete/merge/publication claim. Plan final record draft124 is on
plan/afv2-api-01-final at Plan/.worktree/afv2-api-01-final. Next: finish formal
profile; check actual strictstatus/currenthead/base/threads; expected-head merge,
normal19NuGet/internalnpm/Go cohort; record completion then next eligible task.

## Current API-01 formal96 tooling consumer failure

Formal96d02cef1eeff087e17ac8aab66891b55169270f tree
0ede4a1fec540bdc809f49ddb6ec4dee68f17d3c FAILED tooling-tests after15passed
steps including pack/AOT/Go-static/test/exchange/vulncheck. Actual receipt
20261116-125104-96d02cef1eef-linux, raw logs original H-22 location below.
648tests/97.559s/26failures:25 historical scan tests require exact global131,
now135 due to4 reviewed API groups; identity_http package count26 now28 due
to2 V2 owners. Source review had accepted96, but formal gate stays failed.

Author base_audit is adapting only test_dependency_admission.py and
test_identity_http.py affected consumers: strict new counts, exact new group
rows/negative inputs and explicit2 new owner identities, preserving old checks.
No >= waiver, gate removal or control/Go input change. Existing1efa native
qualification stays valid. After commit: rootpush, finaldelta review, new full
H-22 profile, gates/merge/ordinary publication; then final Plan completion.
No active native process is carried forward from failed96. Task remains active.

## Current API-01 final96 source, formal check pending

This current checkpoint supersedes earlier snapshots below; all historical
failures and intermediate source/artifact identities remain in this file and ledger.
Plan123 actually merged7cfd4d725c0dc3586831af37ea3bc34af38a723c at independent
revieweda6ec2cc6b262476bdf21b0df883e0fb1d7b934f1; both native5/5 summaries bind
actual Design493022fbf643b484665b2713c9eb8670f2fb2234 (Win124940/Linux124931).

Contracts final96d02cef1eeff087e17ac8aab66891b55169270f is pushed draftPR140.
Independent base_review accepts complete final source and all reviewed deltas,
including exact observed r2 digest rules; no source blocker. Existing generated
C# business bytes still match4d; Go source1efa changes only generated package
comments and has true native qualifiers on both hosts. Immutable r1 stays intact.

H-22 independently fetched96 and is running unchanged full20step verification,
PID3064037, background/home/sammiller/arcforges/logs/afv2-api-01-formal-96d02ce.txt;
formal receipt Contracts/.git/arcforges-verify/logs/
20261116-125104-96d02cef1eef-linux/. Scan, restore and admission have passed;
observe the completed summary before merge. No full success, merge or publication
yet. Root final-record worktree Plan/.worktree/afv2-api-01-final on
plan/afv2-api-01-final base7cfd4d7. Task remains active. Next: real formal result,
protection/head/base/threads check, expected-head merge, normal cohort publication,
final Plan delivered/complete record and next eligible task. Never activate PROD.

## Current API-01 r2 exact qualification and observed hash successors

Metadata candidatee9caf2a6931f4dcf566be98593bb81426d69be18 is pushed draft140;
source1efa1dd Go header fix and derived r2 qualification only. Author is idle.
Windows exacte9ca full existing go static PASS, including original ST1000 and
reviewed/current source qualification; logauthor artifacts/
afv2-api-01-go-static-r2-win.log. Provenance1440files/170records, admission267inputs,
format, generation drift and60vectors passed. Immutable r1 records stay unchanged.

H-22 pinned read-only/no-network redacted scan diagnostic of origin/main..e9ca
found11 new generic-api-key public input SHA256 rows in the immutable r2 successor.
Raw diagnostic log stays author-native artifacts/
afv2-api-01-secret-diagnostic-e9caf2a.log. Root rehashed all11 from Git blobs;
all matched. Policy lines204/1247 duplicate one new Go-r2 record hash; r2 receipt
lines46/91/129/198/231/232/278/410/415 contain9 distinct exact key/hash rows.
This is a diagnostic, never a formal status. Its first invocation failed to import
the Step-injected profile module; the corrected command used the same pinned
image/config/range plus a read-only Git-dir mount for the linked worktree.

Plan PR123 now updates only the existing exact .gitleaks.toml scope purpose to
include actually observed immutable qualification successors with rehashing;
no new path, broad ignore, scanner disabling or threshold changes. Independent
scope review and both required Plan profiles precede adding these exact rules.
Then final Contracts full Linux profile, delta review, merge and normal cohort
publication remain. API is the sole active task, no delivery claim yet.

## Current API-01 required-check failure and bounded repair

H-22 full5417 completed11steps successfully, including pack/Native AOT and
Go generation drift. It then failed go-static ST1000: the two generated V2
validation.go files lack the required Package sandboxv2/managementv2 comment
separation. Treeee0a035464267bc92adf47b94098096eb9e2b116, receipt
20261116-124013-5417f9d12fc5-linux. Later profile steps not run. No publication.

Sole delegate /root/base_audit is fixing only the generator header and regenerating
these files, with targeted Go checks. No generated hand-edit or suppression.
Changed Go bytes require a new source commit and both native Go qualification
collectors; root owns Linux, author can prepare Windows. All previous receipts
stay intact. After derived admission metadata refresh, new full final-head Linux
check and independent delta review remain mandatory. Current task still API-01.

## Current API-01 Go comment repair and native qualifiers

Source1efa1dd761ee4d37028d3d0b2e67fc827d556bc6 is pushed in draft140.
Only generator header and two regenerated Go package comments changed after5417;
Go60vectors passed. Both clean native Go collectors passed same1efa and reported
unchangedSourceAndLocks=true. Windows raw report is in the preserved go-23a4b33
worktree artifacts/afv2-api-01-go-reference-windows-1efa1dd.json, SHA256
21754a48640c6330888b480b1a8b8c46250b10d3d6a8509909f59ab9f50fddf3.
H-22 raw is in preserved268c42e worktree artifacts/
afv2-api-01-go-reference-linux-1efa1dd.json, SHA256
a0214c4b4052d0a8324699730912f8d38f0890135b0ca535a02073a62cd38ca8.
Original raws stay on their hosts; the existing validator derived the portable
Linux summary. Author base_audit is preparing immutable Go provenance/review r2,
then affected checks; no final full profile or source merge yet. Source comments
are the only behavior-neutral Go changes, compatible versions remain fixed.

## Latest API-01 candidate5417

Source5417f9d12fc5bff43dc07590defefb0ba73a68cb fixes215 pack failure with
exactly two V2 solution Project registrations. Windows solution Release build
passed0warnings/0errors; log Contracts/.worktree/afv2-api-01/artifacts/
afv2-api-01-solution-release-fix-win.log SHA256
f74b12f61edd5b02023e50e4089c856a9e14fb38424172a16c3befedae5df35f.
Admission266inputs passes. Independent base_review accepts full215source and
5417delta, explicitly retaining215formal failure until a new full pass.

H-22 fetched5417 independently; unchanged20step full profile PID3055580 is in
/home/sammiller/arcforges/logs/afv2-api-01-formal-5417f9d.txt, actual receipt
Contracts/.git/arcforges-verify/logs/20261116-124013-5417f9d12fc5-linux/.
Observe its real summary; still no final full success, merge or publication.
Plan final evidence is preserved in draftPR123/plan/afv2-api-01-delivery.

## Current API-01 checked scope and formal run

Plan scope PR122 actually merged916cdc5cc5d927c9b6caaecdbaa5063f701f880a
at independently reviewed5594d8cea301c83d640aa7c864ad59331c506918,
treeb554c60077616818d339497ca8ce515bc7d848e0. Native Windows5/5 receipt
20261116-123403-5594d8cea301-win and H-22Linux5/5
20261116-123411-5594d8cea301-linux both bind actual Design493022f. Strict
both-host statuses, current head/base, no bypass and zero threads were checked.

Contracts candidate215ab65ddb48de4a3efeb66392c48a9e25a7974f adds only31lines
to .gitleaks.toml aftera5d: two exact-path groups,11 distinct public key/hash
whole-line generic-api-key rules covering the14 observed duplicate findings.
Author rehashed Git blobs and checked wrong hash/key/path/suffix rejection;
no source, Go/control input, version or scanner behavior otherwise changed.

H-22 independently fetched exact215 and launched unchanged full20step
python eng/verify.py run-and-report, PID3052053, background log
/home/sammiller/arcforges/logs/afv2-api-01-formal-215ab65.txt;
formal logs Contracts/.git/arcforges-verify/logs/
20261116-123608-215ab65ddb48-linux/. The original secret-scan now passes.
Restore, admission, naming, provenance, access and format passed; pack FAILED.
The two V2 projects were absent from ArcForges.Contracts.slnx and project references
built them in Debug; Release inspect-build correctly rejected missing DLLs.
Root is adding only their two solution Project rows and running targeted Windows
Release, then a new pushed-head Linux full profile. This is a build defect, not
a transport/storage failure. Final review must include that delta.
Independent reviewer /root/base_review is inspecting the complete215 diff
against Design/acceptance. No source merge or new package publication yet.

Plan final-record worktree: Plan/.worktree/afv2-api-01-delivery on
plan/afv2-api-01-delivery, base916cdc5. Next observe full native result and
review, fix actual blockers only, then merge/prove normal cohort publication,
record delivered/complete and continue next eligible authorized task.

## Latest API-01 formal-check checkpoint

Contracts draft PR140 is at a5d69f7df56febdd3d2696d4b21cd4ec57fcab9f.
The first native H-22 formal run failed secret-scan (14 generic-api-key findings),
not transport. Receipt: Contracts/.git/arcforges-verify/logs/
20261116-122908-a5d69f7df56f-linux/summary.json; tree
270a1284ab0b28a05b95649e9831dc22626d0426. Clone identity and native-toolchain
passed; later profile steps did not complete and no success is claimed.
All 14 rows were independently recomputed from current Git blobs on H-22:
three distinct policy rows (duplicated in its review snapshot) and eight receipt
rows, all public SHA256 input hashes, all matching current source bytes.

This Plan amendment adds only exact .gitleaks.toml to API-01's Contracts paths
for existing-style AND exact-path/key/digest whole-line generic-api-key false
positive allowlists. Independent scope review and both Plan native statuses are
required before editing that file. Never disable or broadly exempt the scan.
Go/control inputs are unchanged by this file; preserve the already collected
4d92cf5 Windows/Linux qualification and Windows AOT evidence, not repeat them.
Correct Windows AOT report locator is Contracts/.worktree/afv2-api-01-go-23a4b33/
artifacts/afv2-api-01-aot-win-4d92cf5-report.json (full filename prefix).

Next: merge this narrow reviewed scope amendment after both required checks
against actual Design main493022fbf643b484665b2713c9eb8670f2fb2234; fix only
observed digest rules; push a new Contracts head, rerun its native full Linux
profile, resolve independent final-source review, merge and inspect ordinary
19-NuGet/internal-npm/Go cohort delivery. Then record API completion and continue
the next eligible authorized task. API remains active, nothing merged/published.

## Current checkpoint — API-01 active; MXC-01 preserved blocked

The owner requires continuous serial delivery. API-01 is now the only active
task; BASE-01 dependency is complete and AR-03 does not block this contract
work. MXC-01 remains blocked, not delivered/complete; do not resume its rejected
cohort or remove the old product runtime. ENV/BASE-01/BASE-02 remain complete.

Final MXC record Plan PR120 actually merged6367ed1bce7b4b3cdce0ae560ceeae5742cd0706
at reviewedb9448fbc21be7f724ae478bbfad1de418917ac93. Native Plan Windows5/5
receipt20261116-112149-b9448fbc21be-win and H-22Linux5/5
20261116-112116-b9448fbc21be-linux both bind actual Design
493022fbf643b484665b2713c9eb8670f2fb2234. Complete summaries, strict protection,
actual statuses/current head/base/zero threads and independent review were
checked before expected-head merge. Node draft93 remains unmerged at438;
actual825 native failure/artifacts and all exact prior evidence remain below.

A single GitHub MCP connector outage had three consecutive HTTP transport
failures. Retrying that connector stopped. The expressly authorized fallback
uses the existing native Windows gh login: read-only state confirmed PR120
still draft/unmerged, live Design/status/rules were checked, then ready and
expected-head immediate merge succeeded with actual SHA readback. No native
host failed and no status/token/proxy/security setting was changed. Continue
using that existing gh/Git fallback for GitHub; Linux verification must still
use designated H-22 MCP. Never add these failures to a future unrelated outage.

API baselines fetched from actual origins: Plan6367ed1bce7b4b3cdce0ae560ceeae5742cd0706;
Contracts69f3041ab4c6bcee1677d0587aaebbbf54cb98bb;
Design493022fbf643b484665b2713c9eb8670f2fb2234. New Windows worktrees:
Plan/.worktree/afv2-api-01 on plan/afv2-api-01;
Contracts/.worktree/afv2-api-01 on task/afv2-api-01;
Design/.worktree/afv2-api-01-baseline is detached and read-only. Existing drafts,
primary directories and unrelated Cloud CI work remain preserved. H-22
Contracts origin/main69f and tool selection were freshly checked: native host,
clean primary, Python3.15.2/.NET11/Node26.13.1/Go1.27.4; no MCP outage.

Scope: additive sandbox.v2/management.v2 schemas, generated C#/Go and applicable
browser consumers, required validation/vectors/method inventories and ordinary
cohort publication. Keep every published v1 number/meaning/artifact and actual
shared consumer. Use existing generators and exact toolchains; no hand-edited
generated code, retired npm/Maven revival or product runtime implementation.
Contracts requires its actual Linux full profile; Plan requires both hosts.

/root/base_audit is the sole delegated Contracts author after reading all task
refs and repository instructions. The coordinator owns Plan, native Linux,
integration/push/PR/review/merge/publication. Scope activation has no API
implementation or acceptance claim. Next: finish the author's bounded
keep/delete/adapt/add assessment, implement through existing generation and
validation paths, run affected native C#/Go/browser checks, independent review,
exact-head required statuses and normal main-push cohort delivery; record then
continue the next eligible authorized task. Public activation still requires
its separate concrete approval.

### API implementation checkpoint — partial candidate published

Startup Plan PR121 actually merged8665de3ace9243670668970ee35fa826aa68a196
atfc08f5cb34ae6f4de872ba2ca24eff58274edc56. Both Plan native5/5 receipts
20261116-113110-fc08f5cb34ae-win and20261116-113037-fc08f5cb34ae-linux bind
actual Design493022fbf643b484665b2713c9eb8670f2fb2234. The state/evidence-only
coordinator exception was applied; required independent review of the final
Contracts implementation remains mandatory.

Contracts draftPR140 now preserves first partial source
bb4f9bcc5115c8a6ad68690355e705ae37375f6a on task/afv2-api-01 from69f3041.
The coordinator checked all53 changed paths against the task allowlist: none
outside scope. Three specs are adopted byte-for-byte after10-field provenance;
two new public C# owners and two internal Go packages use existing generation,
153 message constraints,42 method classifications and V2-specific wire ceilings.
Author generation and both C# Release package builds passed0warnings. Existing
v1 meanings/limits, retired packages and all protected consumers remain intact.
This partial commit is not final delivery or a fully tested contract cohort.

H-22 independently fetchedbb4 into Contracts/.worktree/afv2-api-01-bb4f9bc.
Actual command in its go/ directory:
GOTOOLCHAIN=local GOFLAGS=-mod=readonly go test
./arcforges/sandbox/v2/... ./arcforges/management/v2/... returned0;
all four proto/connect packages reported [no test files]. This is compilation
only, not a passing protocol-vector test or required formal host status.

/root/base_audit continues local shared positive/negative vectors, descriptor
coverage, browser-compatible C# consumer/AOT, access/generated provenance and
normal dependency review receipts and docs. There is no final required Linux
profile, independent final source review, merge or new publication yet. The
root coordinates Linux diagnostics/integration. New source must be pushed and
fetched by H-22 before its final unchanged full profile. Preserve existing
69f cohort and reject missing/failed validation; no product runtime is in scope.

### Current frozen code —4d92; final metadata/AOT in progress

Contracts draft140 now preserves `4d92cf527652f2bcea69bca5ffc4075272d169ad`.
Go/control code is frozen. Current C#/Go shared vectors are60; C# author,
Windows Go and actual H-22 Go tests pass. This includes GetOperation as a
correlation-only read with original command/epoch, immutable Foundation nested
validation, Unicode scalars, exact compiled RPC request/response/stream mapping
and the existing bounded protocol cases. Generation drift, operation-scope67
and Go-binding20 tooling tests passed at the author checkpoint; original
failures are preserved. No old v1 wire/global validator is changed.

H-22 actual worktree is still `Contracts/.worktree/afv2-api-01-268c42e`, now
checked out at4d92 after independent GitHub fetch. Latest raw collector report
`artifacts/afv2-api-01-go-reference-linux-4d92cf5.json` SHA256:
`f7cf451fa40f84bbb8fc165d280f6e9dd9700193ac6c2e9adcb69d3113626186`.
The source is clean and unchanged. Native Go vector log is
`artifacts/afv2-api-01-go-vectors-4d92cf5.log`. Existing go_report_summary
validated portable metadata references that original report and was supplied
to the author, without copying raw host receipts. Windows same4d92 clean
collector passed too; the current Windows AOT run is using a detached same4d92
tree with ignored outputs. Wait for its actual outcome; old268 AOT remains old.

Author only updates noncontrolled access/provenance/dependency receipts/docs.
Next: push final metadata head, pause author, independent source/receipt review
and unchanged full Contracts Linux verification including actual AOT/exchanges.
Plan current API state stays active. No source merge/new cohort/final required
status or task completion exists yet. Disk recovery details remain below;
599MiB was the last observed free H-22 user space, not a promise the build fits.

### Previous API native checkpoint — code23a, metadata still pending

Contracts draft140 now contains pushed stable Go/control code
`23a4b33dc5dd0ddd5068e8451fc0789322060f99`. Shared vectors are now57;
C# targeted checks and native Windows Go vectors passed. H-22 independently
fetched the same commit and actual Go `TestV2ContractVectors` passed all57,
including Unicode/non-BMP limits and immutable Foundation vocabulary/detail
refusals. These are contract tests, not runtime authorization/dedup acceptance.

H-22 reused the clean diagnostic worktree
`Contracts/.worktree/afv2-api-01-268c42e`, whose actual HEAD is now23a.
Earlier268/8a artifacts remain under its ignored artifacts/. Current raw Go
collector report is `artifacts/afv2-api-01-go-reference-linux-23a4b33.json`,
SHA256 `6e47fc316fcc6a1dd6c12800a0566fe4d727064c01876b372ca200f8a468cc46`.
It reports clean source and unchanged source/locks at exact23a. The Go vector
log is `artifacts/afv2-api-01-go-vectors-23a4b33.log`. The existing collector's
`go_report_summary` validated/derived portable qualification metadata; the raw
host receipt stays on H-22 and is not copied into another host's status.
Author metadata combines real same-source Windows and Linux references; no
version refresh or reused old-source native success is permitted.

A real storage condition occurred: H-22 root ext4 is503GiB, user free29MiB
at failed new8a checkout; inode use17%, so not an MCP/network/inode failure.
Git automatically removed the incomplete new checkout. Root confirmed the
bb4 diagnostic checkout had no modified/untracked/ignored/artifact files and
removed only that reproducible200MiB copy via git worktree remove; exactbb4
remains in GitHub/history. No independent-product or other author's work moved.
Then, after verifying the825 original report/native-stage/manifest hashes,
root removed only bin/obj under its own three previous MxcProbe worktrees
488/676/825 (about382MiB). Source, installed toolchains, officialZIP/NuGet,
published stages/debug files/raw reports and original helper pycache all remain.
The preserved native hashes were checked again after removal. Free space is
now about599MiB; do not clear unknown/global caches. A required build that still
cannot fit must be reported honestly, with no merge or fake status.

The original Windows AOT compile had0warnings, but an old descriptor inventory
assertion failed after new V2 checks passed; its log is retained. The corrected
exact268 Windows AOT full serialization probe passed with dynamic code false,
recorded separately as `artifacts/afv2-api-01-aot-win-268c42e-report.json`.
It is not relabelled as23a/current-fixture proof. Author now finishes access,
generated provenance/dependency receipts and docs; Go/control bytes are frozen
at23a unless an actual acceptance defect requires a new measured source.

Next: finish the noncontrolled metadata candidate, push/fetch its exact SHA,
run the unchanged required Contracts Linux full profile (including actual
native AOT and C#/Go exchanges), independent final source/receipt review,
protected exact-head merge and normal cohort publication. No final full status,
source merge, API completion or new publication exists at this checkpoint.
Plan progress draft122 preserves this record; coordinator retains Plan state.

## Previous checkpoint — MXC-01 blocked; continue independent API-01

MXC-01 is blocked by AR-03, not complete/delivered. The selected official1.0.1
cohort failed the genuine H-22 request-environment argv privacy case. Do not
retry unchanged inputs, weaken the assertion, privately patch MXC, upgrade the
pin without admission, or merge Node draft93. Existing product executors/data
and completed ENV/BASE work remain intact. This is not a host/MCP outage.

Design PR72 actually merged493022fbf643b484665b2713c9eb8670f2fb2234 at reviewed
181540da05d45f33f3f7963855ba0f91d1f5ed72, both native Design4/4 passed (Windows
20261116-111251-181540da05d4-win; H-22Linux20261116-111215-181540da05d4-linux).
Its sources/protocol/F-AOT-01 agree on FAILED and preserve all other future
facts. Plan scope PR119 merged32589ed5ea739fcd813ca33eb03f831f713280be after
independent review and exact-head dual5/5 against then-current Design4472.

The Node branch task/afv2-mxc-01 is pushed through
4382988ce5b5ea40f4eb4583534a18bb135d371a/tree4f581146effc75c65a00104ce6aa76b5278c83b2.
It is clean and only the last whitespace-format delta differs from native
candidate8252c8fc13d5973b27ab76bc18726eab8f21cb96. Native825 results are not
claimed for438. Independent /root/base_review checked the complete source,
original Windows/Linux evidence and rejected admission disposition, and accepted
final Design181 negative records with no blockers. No Node merge/full status or
product acceptance approval exists. All owned native/build processes finished.

Exact originating artifacts, hashes, worktrees, failures and cleanup facts are
preserved in the following checkpoint history and Design result. The source
worktree and all old drafts remain untouched. There is no data migration,
backup/restore or publication/deployment in this probe task.

This final blocked-state record is in Plan/.worktree/afv2-mxc-01-blocked on
plan/afv2-mxc-01-blocked, baseline32589ed5ea739fcd813ca33eb03f831f713280be.
Before it merges, its actual required Plan native legs must bind current Design
493022fbf643b484665b2713c9eb8670f2fb2234; independent final record review remains.
After recording this state, immediately activate AFV2-API-01 (dependency BASE-01
complete; no AR-03 dependency). Do not stop at this boundary. Contracts actual
origin was checked and latest main fetched69f3041ab4c6bcee1677d0587aaebbbf54cb98bb;
primary and old worktrees are preserved. Create a new API worktree, read its
AGENTS/CONTRIBUTING and exact V2 Design refs, then implement/publish additive V2
contracts and generated bindings without changing published v1 meanings.

## Previous checkpoint — MXC-01 native privacy failure; record then continue

MXC-01 remains the only active task while its negative result and blocked state
are made authoritative. Do not admit the candidate or weaken the privacy gate.
Node draft93 preserves tested8252c8fc13d5973b27ab76bc18726eab8f21cb96; no Node
required full statuses or source merge exists. Author is completing whitespace
formatting only and then pausing for independent review.

H-22 independently fetched825, locked restore and actual linux-x64 AOT passed
0warnings/0errors. Native SDK1.0.1 discovery, pipe and real PTY passed. The owned
kill/wait case PID3026318 observed the synthetic environment sentinel in owned
native argv, then killed/waited and confirmed PID absent. Reportok=false/exit1;
unit arcforges-mxc-aot-825-26b98458 is inactive/not-found with emptyControlGroup,
and root confirmed all recordedPIDs absent. This is not an MCP/network/host
failure. No credential was used or exported; only bool/PID evidence is retained.

Exact Linux worktree: ArcForges/.worktree/afv2-mxc-01-8252c8f. Same-host artifacts:
artifacts/mxc-01/{linux-report-825.json,linux-context-825.json,linux-unit-825.log,
linux-unit-cleanup-825.txt,linux-publish-8252c8f.log,stage-825.log}, validstage
`安装 测试825`, and four negative reports under `negative Linux825/`. ReportSHA
2d9fbd329c481e77912a9df5b566a96590eba1aa8c8591f196d9c3664310eafe;
probeSHAd2465732a29fff4edd0d20b8017d3ed9f665254b67fa0af7005f0452d8b45663;
manifestSHA2d2da41778cb1548b6521f4bf1b2f3ab2570ae467d54022e272c8d7c53161aa1.
All four invalid-stage cases reject before native/fixture work. Older488/676
source/artifact diagnostics remain in their own named worktrees. No native job
or build remains running there.

Windows author825 evidence is in Node authorworktree artifacts/mxc-01/
windows-author-8252c8f-summary.json: AOT0warnings, five actual signaturesValid,
five fresh-process executor/Jobzero/argv checks passed, four negative cases
passed. Native-only executable SHA23b9bae909c4bbaa638b5c1985d202e1e22ac6dc9aa28191b0bcc77d6b3a5370,
stagemanifestf903750d347c4709fd02a6fc6c80921604aac587b0935b7c9501d6071c81ce1a.
These are author-native results, not required full repository statuses. Actual
source/tree, paths, commands, warning/signature/cleanup/measurement details are
in the originating summary; coordinator/reviewer must read it before final doc.

Official1.1.0 is not an automatic remedy: bounded exact source inspection still
shows request environment emitted as --setenv key value. That is source-only,
no1.1 runtime/admission claim. A supported upstream remedy or an explicit
reviewed product decision is needed to resume admission. Preserve existing
product executor/data; no private patch or new unreviewed pin.

Next: independent review of Plan119 exact evidence-register allowlist amendment,
merge it after its own native gates; only then edit Design platform F-AOT-01.
Finish Design72 negative evidence/review/dual exact-head gates and merge first;
then final Plan record against actual Design main sets MXC-01 blockedAR-03,
records AR-03 failure, all pending drafts/receipts and next task. Continue
AFV2-API-01 after that record, under existing continuous authorization. No task-
boundary stop, public activation, source merge or runtime pass is implied.

## Previous checkpoint — MXC-01 active; continuous delivery

BASE-02 final Plan PR117 merged a42b00a7c3ad8643812face8796c156518e5607a at reviewed9630064c55893a9a6e4da7b8804eb4f2a6e0f789. Both required Plan native legs passed5/5 (Windows20261116-103722-9630064c5589-win; H-22Linux20261116-103731-9630064c5589-linux), binding actual Design4472ea5a110a3c15c8beeeed14627e44b37103d0.

AFV2-MXC-01 is the sole active task. Baselines: Plan a42b00a7c3ad8643812face8796c156518e5607a, Node39c2c57fdaf3666ec046a22370aa2f2157c2d058, Design4472ea5a110a3c15c8beeeed14627e44b37103d0. New Windows worktrees: each repository/.worktree/afv2-mxc-01 on plan/afv2-mxc-01, task/afv2-mxc-01 and design/afv2-mxc-01 respectively. All previous drafts and native receipts remain preserved.

Scope: exact stable Microsoft.Mxc.Sdk1.0.1 / officialv1.0.1 / schema1.0.0 artifact/license/SBOM admission and standalone C# Native AOT MXC-AOT-01 probes on the actual Windows/H-22 hosts. Keep product runtime, data and shared consumers; no profile-composition or product-performance qualification is claimed. /root/base_audit owns scoped Node probe authoring; coordinator owns Plan/Design and Linux/integration. At this checkpoint no probe code/build/runtime acceptance exists. Linux MCP fresh native preflight passed: actual H-22, SDK11.0.100/Python3.15.2, user manager running, cgroup2fs, bwrap0.12.0. Firewall helper binaries are absent on current PATH; determine whether the bounded default-denied offline probe needs them, never silently install or broaden networking.

Next: implement MXC-AOT-01 within the task allowlist, collect exact official artifacts and genuine native receipts, independent final review and required exact-head host profiles; Design merges before Plan when updated. Continue the next eligible authorized task after recording delivery. No task-boundary stop is authorized. Public PROD-01 activation retains separate concrete approval.

### MXC-01 artifact stage and authoritative scope

Plan start/scope PR118 actually merged c1599bc878f6e9fb1cec7f4d8ae4aaf5d3948b9e
at reviewed2de09dee78dd24bffc3c46dad2270bd92bd07225. The only scope addition is
ArcForges.slnx to register the real probe required by existing repository layout
checks; no checker or product-package change. Final required native receipts:
Windows20261116-104942-2de09dee78dd-win5/5; H-22Linux20261116-104855-2de09dee78dd-linux5/5.
Both bind actual Design4472ea5a110a3c15c8beeeed14627e44b37103d0. Independent
nonauthor /root/base_review accepted; strict actual checks/no bypass/zero threads
were checked before merge. Initial wrong-cwd Windows run only checked historical
2b8b4809ae13 and never qualified PR118; the ledger retains that fact.

Current evidence branch: plan/afv2-mxc-01-evidence in
Plan/.worktree/afv2-mxc-01-evidence, based on that actual scope merge.
Design draft PR72, design/afv2-mxc-01 at fda4637d8e31eae965b9b5e2a4671800d203bc78,
records artifact-only progress; it is not reviewed/verified/merged and no runtime
acceptance is claimed. Design must merge before final Plan validation.

Linux native author venue is ArcForges/.worktree/afv2-mxc-01-author at detached
39c2c57fdaf3666ec046a22370aa2f2157c2d058. Official artifacts and factual
linux-artifact-inspection.json stay in artifacts/mxc-01/official there. ZIP
542051775bytes/SHA0e832239454ba7fcd338ff56218a287eef4c0a01c1484084b869f55feff8abe9;
NuGet14615475bytes/SHAd47b1f70c3fcaaed1705a0c3872807e2878fe8c1b778c0dd9eb9325bf421a672.
All five x64 native files match; upstream SPDX2.2 digest matches but NOASSERTION
licenses are inventory only, not closure approval. DownloadPID3023151 ended.
Actual user namespace probe passed; no host settings or prerequisites changed.

Official1.1.0 was freshly observed (published2026-11-15T05:28:48Z); preserve the
explicit1.0.1 pin and reject unadmitted APIs. No probe code or AOT/runtime pass
exists at this checkpoint. /root/base_audit is implementing scoped Node probe;
root coordinates native Linux and Design/Plan. Continue implementation and
collect complete MXC-AOT-01 evidence, then independent review and exact-head
required native gates. Keep these staging paths and all older drafts/receipts.

## Previous checkpoint — BASE-02 complete; continue MXC-01

The owner explicitly requires continuous serial implementation: complete and
record a task, then proceed without a task-boundary stop. The38 remaining task
IDs were authorized in the2026-11-16 PLAN ledger note. Public PROD-01 activation
still requires its concrete approval. ENV, BASE-01 and BASE-02 now complete in
this evidence change:3complete/37planned/0active. AR-13 PASS; AR-01..12 unchanged.

Plan baseline456ff230ff8f316c40727ca83509c5f919ac6f5f (scope PR116), Design
4472ea5a110a3c15c8beeeed14627e44b37103d0 unchanged. This final record is
plan/afv2-base-02-closeout in Plan/.worktree/afv2-base-02-closeout,
[PR117](https://github.com/ArcForges/Plan/pull/117). Its own required native Plan
checks/merge must still finish before this record reaches main; actual final
head, receipts/Design binding and merge result are recorded on that PR.
Then immediately activate the next eligible task, MXC-01; do not end the run.

### BASE-02 delivered code and acceptance

[Node PR86](https://github.com/ArcForges/ArcForges/pull/86) actually merged
39c2c57fdaf3666ec046a22370aa2f2157c2d058 at tested/reviewed head
f95af854ee2d7198d1d1ddfac4b87dd97ee1d703, tree334e647ec8eb8abcfcd66bb7721fe6d6d87d99e6.
The44-path change removes13 actual Desktop source/test files,26 exclusive
Avalonia/graphics/MicroCom package pins/admissions and current unused notice
copies; adapts actual solution/publish/CI/benchmark/test-suite/docs and existing
packaging to Node/CLI Host plus Windows Supervisor or Linux service units.
There is no desktop application/unused Avalonia in the current solution/package
closure. No nonexistent MCP/hook/toolchain/cache project deletion is claimed.

Tmds.DBus and its notice remain for actual Linux systemd use; all remaining
admission objects/rules/never-admit/exceptions/locks remain unchanged. Shared
DesktopPlatform/Contracts, independent apps, critical old executor/data safety,
Node SQL, toolchain selectors and Linux service source bytes are preserved.
Default adjacent-desktop trust and unavailable Desktop startup/approval copy
retire; legacy kinds/test seam and actual CLI/auth/routing/lifecycle remain.

The final two-test repair only applies the standing exclusive classification
and retains live Job membership plus valid native Windows StartedRecord within
original Tasks.Bound before recoveryAt. It removes the suspended-before-resume
test precondition race. Original3s/128/180000/1500/2000, four input cases and all
strict order/browser/CPU assertions remain; production/helper/runner unchanged.
No data migration, backup/restore, deployment, public channel or SDK/MXC runtime
admission occurred. Existing main-push workflow publishes nothing;0merge-triggered
runs observed at the actual merge, matching unchanged triggers.

### Final real evidence and independent review

Native designated hosts fetched the same exactf95 SHA independently from GitHub
and ran unchanged `python eng/verify.py run-and-report`. Full summaries were read
by coordinator and nonauthor reviewer, every result true/emptyreason:

| Host | Required full result | Originating receipt under ArcForges/.git/arcforges-verify/logs/ |
|---|---|---|
| Windows DEKU, owner-authorized current-machine local access |15/15,2172s |20261116-094125-f95af854ee2d-win |
| H-22 v2202601329473427941/sammiller, designated Linux MCP |21/21 inclactionlint,2051s |20261116-095435-f95af854ee2d-linux |

Actual GitHub both required statuses succeeded atf95. Active strict rule24915109,
no bypass/current head+base and clean PR were checked before expected-head merge.
OpenAI Codex nonauthor /root/base_review accepted complete source, final delta
and final real acceptance evidence, no blockers. Truthful records are on PR86.

Each clean final archive has78files/77matching digests, sourcef95/SDK11.0.100,
actual tested Host bytes, source lock bytes, LICENSE/notices/build-info and
platform assets (WinSupervisor+2locks; Linux3units+Hostlock), no desktop or symbols.
Exact archives and package-inspection.json are preserved on each originating
host under its receipt/artifacts/, before any future canonical-cache reuse:

- Windows ZIP1fc47ca1e8961603bc2fc4110d920dcc873f7f36a7636a17ed30424457921e3f;
  Hostbd88cd0e0ceaae7c80a004c11e6864395f17062e6ff9e9e864dc34aabfe7d5c9;
  Supervisor06e2554d760b066613ab6f96aae6a6963cb1f6a988be1417e767be70a315711a.
- Linux TAR256dfc3b7fc790138236e68fef45ab46b8818b192794af8de4b194fa83d58ea9;
  Hostaa2443203dc4147cbd33e44c8f658a24b0516f3286f32cbf9ec687388228acbe.

These unsigned local verification outputs are not public releases. Canonical
output names are artifacts/packages/arcforges-win-x64.zip or
arcforges-linux-x64.tar.gz; use the preserved receipt copies for this task.

Author diagnostics remain distinct: Windows restore/build0warnings, Repo116,
Tools100+1Linux-onlyskip, Client190, guidance lifecycle2+1environment skip;
repaired exact methods selected with exclusive trait1/1+4/4,0skip and formatpass.
Clean H-22c58 native CLI/Node1/1/package and earlier dirty Windows native/package
checks are author proof only, notf95 statuses. Logs remain in product worktree
artifacts/base02-author/ and Linux .worktree/afv2-base-02-author/artifacts/
base02-author-linux/. No meaningful failure history was rewritten.

### Preserved failures, scope and worktrees

Oldc58 Windows CI failed on two unchanged methods; immutable receipt
20261116-091624-c58b9efb9073-win/win-ci.log contains both assertions/stacks.
Original isolated methods passed1/1+4/4 without replacing the failed full gate.
The native source diagnosis and exact two-test fix were reviewed before editing.
Oldc58 Linux21/21 succeeded, but is history only; its exact clean TAR is retained
in receipt20261116-091813-c58b9efb9073-linux/artifacts/, SHA256
8444ed0691fcd105113e5f8e7c2239ffeaf11abfa06119d22d0267345cc27f72.
No receipt/status was manually edited or copied between hosts.

Scope PR114/115/116 actual merges97ecbf618b642d5e8b4c3a22604765f85a3a41c0,
397c04e546a734c64fe5f3787ae40be6b1c702fc,
456ff230ff8f316c40727ca83509c5f919ac6f5f respectively. Each required exact-head
Windows/Linux5/5 and nonauthor review; both Design contexts matched actual4472ea5a.
Ledger records full heads/receipts and each specific companion path/reason.

Product author Windows .worktree/afv2-base-02 / task/afv2-base-02 is clean atf95;
writer stopped. Formal invoking .worktree/verify-base02-f95af854 exists on both
hosts. Windows session94271 and Linux PID2967445 ended successfully; oldc58
PID2918324 also ended. No task verification process or CI remains pending.
Canonical caches: Windows .worktree/_verify and Linux
/home/sammiller/.cache/arcforges-verify/ArcForges. No unknown cache cleanup.
Earlier Plan scope/delivery/complete worktrees and original BASE-01 drafts remain;
independent Cloud CI draft is untouched. Linux Plan primary remains historically
dirty; never reset it or use it for authoring. Source/cached test outputs stay.

Windows local access supersedes unstable Windows MCP per owner; H-22 requires its
designated MCP. Only three consecutive failed reconnects within one outage stop;
success resets count. All MCP calls this task succeeded. Test failures are not
outages. Only process-local English CLI output was selected for normal publisher
summary parsing, no system/network/proxy/security setting changed.

### Immediate continuation

Finish PR117 native Windows/Linux Plan checks against actual latest Design main,
recheck both design-main context values/current protection and merge only that
reviewed head. `python tools/plan.py next` now returns AFV2-MXC-01, planned:
“Admit stable MXC artifacts and build AOT/provenance probes.” Fetch latest
main/Design, read its complete definition/design refs/allowed paths, record
started/active via plan.py in a fresh worktree and implement it. Do not restart
ENV, frozen V1 work or an unrelated product. Do not stop after this record.

The following completed BASE-01 checkpoint is historical; its former coordinator
stopping language is superseded by the owner's continuous instruction above.

## Historical BASE-01 delivery checkpoint

The owner resumed V2 implementation on 2026-11-16. This round delivered only
BASE-01, after ENV; no second product task started. ENV and AR-13 remain complete /
PASS. The graph now has two complete tasks and38 planned, none active. Stop this
round after the final Plan evidence PR; the next eligible task is BASE-02.

Plan baseline for this evidence is main246bb8d92c106202cb2e45123093db436c4ca2a7
(merged PR112). Design remains4472ea5a110a3c15c8beeeed14627e44b37103d0; no normative
Design change was required. This evidence branch is plan/afv2-base-01-complete in
Plan/.worktree/afv2-base-01-complete, [PR113](https://github.com/ArcForges/Plan/pull/113).
Its own exact-head Windows/Linux gates and merge remain mandatory before this
checkpoint reaches main; final receipts/statuses/review are linked on that PR.

### Delivered source and ordinary delivery

| Repository | Tested head | Actual merge / PR | Required native result |
|---|---|---|---|
| ArcForges | 2c4607cab05967fdd316ebfed5ffea4087fa3f13 | de361dbb189baa3ecfb1389fbaf682191d68766a / [85](https://github.com/ArcForges/ArcForges/pull/85) | Windows15/15, H-22 Linux20/20 |
| Cloud | a498b4c48e5d2e0a13ee10b14f9ae4426cb13b80 | f4708b36fd799025ad7d6fa9e5845e4558e492b3 / [158](https://github.com/ArcForges/Cloud/pull/158) | Windows10/10, H-22 Linux17/17 |
| Contracts | f173cf4124541f33b7b6366fe7b264733a0d6077 | 69f3041ab4c6bcee1677d0587aaebbbf54cb98bb / [139](https://github.com/ArcForges/Contracts/pull/139) | Required single H-22 Linux20/20 |

All product final heads passed independent nonauthor review by OpenAI Codex agent
/root/base_review. Its map-owner findings were repaired and delta reviewed. The
final Node change adds only exclusive/DisableParallelization attributes to one
existing timing-sensitive test; the method body and1s latency assertion remain.
Actual strict/no-bypass rules and final statuses were checked before each merge.

Contracts [ordinary CI43772758290](https://github.com/ArcForges/Contracts/actions/runs/43772758290)
succeeded, publishing17 NuGet packages, internal npm and Go tag1.0.0-ci.467.1.
Compatible existing consumer cohorts remain valid. Cloud [main CI43774372219](https://github.com/ArcForges/Cloud/actions/runs/43774372219)
completed skipped (all18 jobs) under unchanged migration guards: no deployment or
publication. Node has no main-push publication path; no merge-triggered run was
observed. Native verification packages below are local outputs, not a release.

### Acceptance and limits

Read-only preflights distinguish fresh, Node15, Center10/11 and unknown/newer;
source state is never migrated or initialized. Node holds native read protection
and inspects an in-memory SQLite snapshot without source sidecars. Center uses a
single read-only repeatable-read PostgreSQL transaction. Reports expose aggregate
metadata only. Unresolved/active/locked/unknown inputs remain fail-closed;
contraction is always denied. Optional binary hashes do not prove provenance,
and actual deployment/authority remain unknown.

The107-entry module/subasset map covers146 C# projects and40 Go roots, actual
owners/consumers and pinned-audit drift. The fixed-HEAD consumer snapshot covers
10 repositories,215 references and60 central declarations; SHA256
1b20e70b5a4c24e1758fdbf596f09b25e65ae8749e510fddfe6b10306950f8e8.
Independent products and shared DesktopPlatform ContentSandbox v1 are protected.
No executor, runtime route, applied SQL or published bytes were removed/rewritten.
Backup, drain, restore, cutover and rollback prerequisites and later owner tasks
are in ArcForges docs/v2-migration/README.md and the two companion tool READMEs.

Node author fixtures: Windows12 total, one expected Linux-only rename skip;
H-22 Linux12/12, no skips. Cloud H-22 PostgreSQL inventory8/8 used real disposable
PostgreSQL/source DDL and removed its fixture container. Contracts input tests5/5
use temporary Git repositories, not runtime doubles. Final native socket test1/1
on each host preceded full gates. PostgreSQL inventory fixtures do not prove the
guarded CENTER-01 upgrade, schema11 deployment or security/provider authority.
H-03 still gates later destructive admission, and AR-01..12 remain unqualified.
There was no production backup/restore/migration, deployment or public activation.

### Exact receipts and native artifact identities

Each host independently fetched the exact SHA from GitHub into an isolated
worktree and ran unchanged `python eng/verify.py run-and-report`. Full summaries
were read, every result ok=true. Receipts stay on their originating hosts under
<repo>/.git/arcforges-verify/logs/ (Windows roots C:/MyFile/Projects/ArcForges,
Linux roots /home/sammiller/arcforges):

- Node:20261116-075439-2c4607cab059-win (2215s),
  20261116-073919-2c4607cab059-linux (2004s), same tree
  31b85b3b8d1a15be615c9ca75f5a95fb133dc429.
- Cloud:20261116-071745-a498b4c48e5d-win and
  20261116-070913-a498b4c48e5d-linux, same tree
  a05ad1946fe380661186b25fa02f8f394ab2d830.
- Contracts:20261116-065050-f173cf412454-linux, tree
  2469c712dcd9dc5879306df054ee6521be8007fe.
- Prior Plan scope PR110: b5bc9953a7945e9cf9df54d510731e75406e4e3c,
  dual5/5, merge7da363a8b781d13903e8bab88e90f5e230a96e94;
  PR111:d90bcd79544c296b7ab61b5d9d87f1fa577cabc3, dual5/5,
  merge7c8aeea55f27c06763cf3eded2abbcb79099dbc9;
  PR112:01564acfe4bd14590fa0db948c1e9c229d26a730, dual5/5,
  receipts20261116-075030-01564acfe4bd-win/20261116-075023-01564acfe4bd-linux,
  merge246bb8d92c106202cb2e45123093db436c4ca2a7.
  All bind actual Design4472ea5a; no Design mutation or validator bypass.

Native Node host SHA256: Windows
1fa9838d3ab163cea2b02dc571fecf4df3db095e4a8d63ae1f9fec45e9b5aef8;
Linux2c8e988b54e6578b1bbe15d359302c6f6ffe28e68d08cdb17c2727e341f7911a.
Local package SHA256: Windows zip
8f4dc7dac090f032dce1f183a9e6e60854523dd7d9729acf188c867491e1d3b3;
Linux tar.gz c57f8272a17a95806124df72b3441a5b7bbc0fc189a44e35c65eefc9fa2812d0.
Paths are artifacts/publish/<rid>/host/arcforges[.exe] and
artifacts/packages/arcforges-desktop-<rid>.<zip|tar.gz> in the native verifier's
checkout (Windows ArcForges/.worktree/_verify, Linux
/home/sammiller/.cache/arcforges-verify/ArcForges).
Cloud local candidate0.1.0-local.1794784677743 image
sha256:b351e73fbb63fc368035244f25185ac1a196700a5a016400ff45205ba36fbfa2.

### Preserved work and exact next step

No BASE-01 verification process remains running. Prior Windows session85689 and
H-22 PID2852179 ended successfully. No Cloud/Contracts CI remains pending.
Windows product author worktrees <repo>/.worktree/afv2-base-01-resume remain on
task/afv2-base-01-resume at the tested heads above. Node and Cloud each have only
untracked eng/v2-migration/__pycache__/ generated by tests; Contracts is clean.
Untouched ArcForges/Cloud .worktree/afv2-base-01 still contain their original
untracked eng/v2-migration drafts. Cloud/.worktree/cloud-deploy-ci-python retains
its independent uncommitted eng/verification/test_ctr06_bridge_assets.py fix;
do not mix it into V2. Earlier Plan worktrees are preserved.
Linux Plan primary still has its pre-existing staged/unstaged historical edits
(including graph, ledger, policy, tooling and maintenance paths); do not reset or
reuse it for authoring. Use independent worktrees. No unrelated product changed.

The owner permits current-machine local Windows access in place of unstable
Windows MCP; designated H-22 Linux MCP is required. Three consecutive failed
reconnect attempts within one outage stop work; successful calls reset the count.
The earlier cumulative stop was a coordinator interpretation error. Subsequent
H-22 identity, fixture and full-profile calls succeeded. Transport failures alone
do not establish VPS failure. No network/proxy/security settings changed.
Windows verifier needs only process-local DOTNET_CLI_UI_LANGUAGE=en-US and
VSLANG=1033 so unchanged publish scripts can read English zero-warning summaries.
Cloud's existing bridge selectors remain in the ledger/previous checkpoint; no
tool installation or general toolchain upgrade was reopened.

Failure history remains append-only in ledger/ledger.jsonl: prior77459503
resource timeouts and48aac4ed CI timing failures were not reused as final proof.
The latter caused only the standing single-test isolation repair admitted by
PR112. Cloud's narrow public-digest scan exceptions bind exact receipt file and
two exact public key/value lines with positive/negative controls; no rule disabled.
Immutable r1 was retained and input-only r2 used; all131 package coordinates and
locks remain unchanged. Final normal scans and admission checks passed.

After final Plan PR113 merge, fetch latest main/Design and run
`python tools/plan.py next`: it returns AFV2-BASE-02. Read its full definition and
current allowed paths before starting; it is planned, not active. This round
stops at BASE-01 completion. Public rollout still requires PROD-01's separate
concrete approval. Historical sections below describe their dated stopping points
and do not override this checkpoint.

## Prior completed upgrade round — historical stopping point

**ENV is complete, AR-13 is PASS, and the original 39 tasks remain planned.**
This upgrade round is finished; do not start BASE-01, MXC-01
or another task. The original authorization remains in the ledger for a later
resumed round. Public activation retains its separate explicit approval.

Current authority is AD-0022/schema3 and the owner's AD-0023 clarification merged
through [Design #71](https://github.com/ArcForges/ArcForges-Design/pull/71) and
[Plan #108](https://github.com/ArcForges/Plan/pull/108). Preserve completed upgrades
and finish necessary .NET/C#, Go, TypeScript and supporting tools with local/CI
parity. Compatible locked dependencies and published producer cohorts may remain.
Keep normal build/test/AOT/analyzer/security/provenance and required native gates;
do not restart per-dependency freshness research, special upstream-metadata/tag
qualification, additional per-version approval or the optional broader native r5.
Independent Mobile/AI/ArcScope/ArcSlate/ArcNotes remain protected consumers.

## Completed ENV delivery

All seven repositories are delivered. Cloud [#157](https://github.com/ArcForges/Cloud/pull/157)
merged as `d422d7718307f39903de49ee673105a3d0db6b9d` after Windows 10/10 and Linux 18/18
at `7d2d18b6e29157df98b5a63dbb6efe2977f6c632`. Its
[main CI run](https://github.com/ArcForges/Cloud/actions/runs/43706393820) completed as `skipped` under the pre-existing guards. All 18 hosted jobs were skipped: ordinary main-push candidates and deployment were already disabled before ENV. No publication or deployment was attempted. The required native Linux profile built and verified candidate 0.1.0-local.1794739798362 (image sha256:aeb1e68ce06a1a119f0f61ae44c7a29e8fc312c9a3bbdbc0473d664f6f95edfe). Both Cloud primary checkouts were fast-forwarded to the merge.

The [ENV summary](docs/dependency-upgrade/afv2-env-01-summary.md) is the single
table of tested heads, merges, required totals and publication links. In particular:

- [ArcForges #84](https://github.com/ArcForges/ArcForges/pull/84) merged
  `200d2d25b1b40093c3af278993145a92bbf82a78` after Windows 15/15 and Linux 21/21
  at `136670a04d34bb45822fa2908229190d25f479ae`; there is no main-push publication.
- [Contracts #138](https://github.com/ArcForges/Contracts/pull/138) merged
  `2b525ad3d79f404d705e4abe8c30bf4bf477d0a6` after its required single Linux 21/21.
  Ordinary [run463](https://github.com/ArcForges/Contracts/actions/runs/43699575709)
  published 17 NuGet packages, internal npm and the Go tag at `1.0.0-ci.463.1`;
  Go proxy/sumdb resolution succeeded. Compatible consumers may retain 450.1.
- DesktopPlatform's [ordinary publication](https://github.com/ArcForges/DesktopPlatform/actions/runs/43693457102)
  completed all 29 jobs and 21 NuGet packages at `1.0.0-ci.151.1`; compatible 150.1 remains valid.
- Web's [final CI/delivery](https://github.com/ArcForges/Web/actions/runs/43694865856)
  succeeded at merge `69be85d95ea412cc027597ffd0d990bf0e28e50f`, recording
  `web-0.1.0-ci.186.1`; `No targets deployed for arcforges-web` keeps public targets unmounted.

The coordinator recorded ENV delivered then complete through `plan.py` and
closed AR-13 with actual evidence. This state/evidence record retains the required
Plan Windows/Linux checks against actual Design main. Preserve the pre-existing
dirty Linux Plan primary and use isolated worktrees.

## Tool selection and preserved host work

Selected necessary versions are SDK 11.0.100 / C# 15, Go 1.27.4, TypeScript 7.0.2,
Node 26.13.1 / npm 12.2.2 and Python 3.15.2 where used. The
[selection table](docs/dependency-upgrade/afv2-env-01-summary.md#selected-language-tools-and-localci-selection)
records actual local roots and committed CI selectors. The new Windows MCP
default shell was measured at these executable versions; Linux `.profile`
selection was completed earlier. Windows User PATH/profile selection uses
`C:/MyFile/Projects/dev/arcforges-toolchains/activate-language-tools.ps1`, retains
Scoop 11 `DOTNET_ROOT` and removes the fixed User `MSBuildSDKsPath` override.
User environment backup is `tmp/afv2-env-01/windows-language-selection-backup/user-environment.json`.
Machine environment, execution/security policy and old installations were unchanged.

Visual Studio 18.12 installation completed with exit 3010; do not reboot in this round.
Private LLVM 23.1.5 / GNU 2.47 (actual banner 2.47.20260726) and their receipts remain.
The optional broader native r5 WIP in `DesktopPlatform/.worktree/afv2-env-01-native`
is preserved unchanged, not an outstanding mainstream-toolchain requirement.
Earlier OOM/ENOSPC recovery removed only 172 temporary Cloud sealed-tool copies
(20.310 GiB), preserved archives/evidence/logs, and restarted the existing user
manager without configuration changes. It is history, not a current profile pass.

Earlier tooling/managed slices and failed-candidate investigations remain in Git,
the [ledger](ledger/ledger.jsonl), linked PRs and each host's own
`.git/arcforges-verify/logs/`. For example, the
[old bootstrap publication failure](https://github.com/ArcForges/DesktopPlatform/actions/runs/43615837618)
and later [150.1 publication](https://github.com/ArcForges/DesktopPlatform/actions/runs/43678526078)
retain their original outcomes. Do not rerun them or rewrite historical receipts.

## Preserved BASE-01 checkpoint

BASE-01 is parked planned, not delivered. Preserve these uncommitted files on Windows under `C:/MyFile/Projects/ArcForges/`:

- `ArcForges/.worktree/afv2-base-01/eng/v2-migration/preflight.py` and `test_preflight.py`; base `10f692224f94916cfc93fbad971f80ec340c5edf`.
- `Cloud/.worktree/afv2-base-01/eng/v2-migration/preflight.py`; base `6df33c525fcbc20495e46c9c4c011086146da796`.
- `Contracts/.worktree/afv2-base-01` remains unmodified at `de3dba76266e89654be9b4d29d097d525a281c6a`.

The earlier Node author diagnostic had 11 tests OK with one Windows condition skipped; the latest protected-fd/in-memory SQLite snapshot and failure-classification changes are untested. Cloud is an untested draft. Consumer scanning, module map, documentation and PostgreSQL fixtures remain unfinished. No product commit, PR or native acceptance exists for this checkpoint. On a later resumed BASE-01 round, reconcile these worktrees with actual upgraded main and run affected checks; do not count the old author diagnostic as current acceptance.

## Product and verification boundaries

The subsequent product remains the general CLI Sandbox/Run platform with official
stable MXC, real terminals/resources/data safety, free offline local CLI, optional
self-hosted Go Center/Blazor management, and subscription-gated official hosting.
No product MCP/AI/Task-DAG/cache platform or desktop/mobile client is introduced.
Preserve Node schema 15 and Center schema 10/11 guards; mandatory composed P1/runtime
qualification and destructive-migration prerequisites remain future task work.

Use native Windows MCP at `C:/MyFile/Projects/ArcForges/` and H-22 Linux MCP at
`/home/sammiller/arcforges/`; fetch exact candidates independently. Never use
substitute hosts, copied receipts, bypasses or network/security changes. Report in
Simplified Chinese. This round is complete; resume product work only in a later round.
