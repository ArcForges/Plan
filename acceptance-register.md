# V2 acceptance and human prerequisites

Items below distinguish completed toolchain evidence from future implementation/activation evidence. Source research and existing V1 acceptance do not satisfy them. A missing required host check also blocks the current documentation PR merge independently of these product tasks.

## CENTER-01 qualification on 2026-11-16

F-CTR-01 / AR-07 passed at exact Cloud8048042. Cloud159 merged as
6bd7169607d55c8b647b1a70302ff28ad365d488. Original host receipts, sealed
candidate/image/ELF identities, real PostgreSQL three-path reports and independent
review are in [the delivery evidence](docs/afv2-center-01-summary.md).
H-03 production inventory, approved production backups and provider authority
remain separate closed prerequisites. Merged-main run43864301663 was intentionally
SKIPPED with zero artifacts. No deployment or public activation occurred.

## Acceptance items

| ID | Item | Status | Blocks | Owner | Evidence / action |
|---|---|---|---|---|---|
| AR-01 | Full Windows official profile | NOT_RUN | AFV2-MXC-04 and dependent Core; final AFV2-ACC-01 | AFV2-MXC-02 | Run MXC-WIN-01..06 on exact qualified native Windows; no pipes-only or separate-feature substitute |
| AR-02 | Full Linux official profile | NOT_RUN | AFV2-MXC-04 and dependent Core; final AFV2-ACC-01 | AFV2-MXC-03 | Run MXC-LNX-01..05 on H-22 with actual PTY/user-manager/cgroup/helpers |
| AR-03 | AOT/native package and distribution admission | FAILED — selected1.0.1 cohort rejected | AFV2-MXC-01 admission; dependent AFV2-MXC-02/03/04 profile qualification and Core delivery | AFV2-MXC-01 | Real candidate8252c8f Linux request-environment sentinel observed in owned native argv; Kill/Wait/PID absence and owned unit cleanup proved. Windows bounded observations pass but do not waive Linux failure. [Design PR72](https://github.com/ArcForges/ArcForges-Design/pull/72), [Node draft93](https://github.com/ArcForges/ArcForges/pull/93); supported upstream remedy or explicit reviewed product decision required before new admission. |
| AR-04 | Crash and unknown ownership recovery | NOT_RUN | AFV2-REC-01 delivery; full native acceptance | AFV2-REC-01 | Same Run owner survives Node loss; supervisor loss/reboot/no PID guessing and exact outer-scope empty tests |
| AR-05 | Owned Sandbox data and deletion safety | NOT_RUN | AFV2-FILE-02 delivery; final acceptance | AFV2-FILE-02 | Native path/identity/managed-use/partial effect/import/export/delete recovery tests; no blanket refusal |
| AR-06 | OS-effective resource budget | NOT_RUN | AFV2-RES-02 delivery and dependent allocation | AFV2-RES-02 | Saturation and desired/applied/readback failures on both hosts; aggregate reductions before increases |
| AR-07 | PostgreSQL guarded upgrade and restore | PASS — qualified isolated candidate | AFV2-CENTER-01 engineering migration acceptance; H-03 still gates production admission/live upgrade | AFV2-CENTER-01 | [Final8048042 evidence](docs/afv2-center-01-summary.md): native Win10/10, H22Linux17/17; same actual candidate CLI fresh/schema10/schema11 real PostgreSQL upgrade/backup/restore,49 successful steps and6owned containers absent. UNKNOWN/fault/quarantine guards verified; no production authority claimed |
| AR-08 | Remote control and data effect consistency | NOT_RUN | AFV2-CENTER-03 delivery and AFV2-ACC-02 final acceptance | AFV2-CENTER-03, AFV2-ACC-02 | Real Node+Go+PG loss/replay/revoke/template tests and final self-host/official journeys |
| AR-09 | Blazor responsive/accessibility and recovery UX | NOT_RUN | AFV2-WEB-04 completion and AFV2-ACC-02 acceptance | AFV2-WEB-04 | Explicit local browser keyboard/focus/viewport/offline/unknown states; no browser/live CI |
| AR-10 | Hosted service/commerce/mail external qualification | NOT_RUN; prices, quotas, trial settings TBD; fixture evidence is distinct | Mandatory real local/self-host mode correctness blocks AFV2-HOST-01; unavailable external provider/mail/domain/merchant/legal qualification blocks AFV2-PROD-01 activation only | AFV2-ID-01, AFV2-HOST-01, AFV2-HOST-02, AFV2-HOST-03, AFV2-ACC-02 | Real Go/PostgreSQL proof, authorization, entitlement, idempotency and local continuity are mandatory. Only graph-listed external transport/input fixtures are allowed for development; actual provider sandbox behavior, mail/domain delivery, merchant/authority and live settings remain separately NOT PROVEN until exercised |
| AR-11 | Coherent install/update/rollback artifact | NOT_RUN | AFV2-DIST-01 and AFV2-DIST-02 release acceptance | AFV2-DIST-01, AFV2-DIST-02 | Real fresh install and schema-aware update/backup restore; signed exact native cohort and actual finished Go/PostgreSQL/Blazor self-host product after WEB-04 via MIG-01; HOST-03 infrastructure or old probe assets are insufficient |
| AR-12 | Complete V2 release candidate | NOT_RUN | AFV2-ACC-01, AFV2-ACC-02 and AFV2-PROD-01 | AFV2-ACC-01, AFV2-ACC-02 | All mandatory native+remote/data/resource/local/business journeys on same final cohort; unresolved safety cannot be deferred |
| AR-13 | Necessary toolchain baseline and local/CI parity in all seven delivery repositories | PASS | AFV2-ENV-01 delivery and both dependent roots AFV2-BASE-01 / AFV2-MXC-01 | AFV2-ENV-01 | Completed necessary SDK 11.0.100/C# 15, Go 1.27.4, TypeScript 7.0.2 and supporting Node/npm/Python alignment across all seven repositories. Required native profiles, merges and ordinary publication passed; exact heads, local/CI roots and artifact identities are in the [ENV summary](docs/dependency-upgrade/afv2-env-01-summary.md). Historical records and compatible producer cohorts are retained. |

## Human prerequisites

| ID | Prerequisite | Current observation | Blocks | Owner / action |
|---|---|---|---|---|
| H-01 | Designated native Windows MCP host with qualified Windows/PSEC prerequisites and repo toolchains | MCP reachable; required ENV Windows profiles and selected local tools passed on 2026-11-15, recorded in the [ENV summary](docs/dependency-upgrade/afv2-env-01-summary.md). Composed MXC/PSEC runtime qualification remains pending | Every repository-required Windows merge check; AFV2-MXC-02 native experiments and affected native delivery | Owner supplies existing host connection/prerequisites; never another host, WSL or handwritten status |
| H-02 | H-22 native Linux MCP host with user manager, cgroupv2 delegation and admitted helpers | MCP healthy; 2026-11-17 required Cloud9483 Linux verification failed with ENOSPC: root filesystem user-available space0. This is storage exhaustion, not a transport outage. Earlier ENV profiles and delegation evidence remain valid; composed MXC qualification remains pending | Every repository-required Linux merge check; AFV2-MXC-03 native experiments and affected native delivery | Owner provides capacity or a concrete permitted cleanup target. About15GiB free is a recovery recommendation, not a new acceptance condition. Preserve archives/evidence/unknown caches; no substitute host |
| H-03 | Actual deployment inventory, approved consistent backups and security-successor/provider authority qualification | Last evidence is historical; no live authority assumed | Destructive migration/admission in AFV2-CENTER-01 and production operations in AFV2-HOST-03; not read-only preflight code | Owner/operator confirms configuration without exposing secrets; keep surfaces dark on uncertainty |
| H-04 | Official pricing/terms/provider and sender accounts/legal text/domain and operational approvals | TBD; no invented prices/quotas/trial | AFV2-PROD-01 activation; does not block architecture or development with graph-listed external fixtures | Owner supplies commercial/provider/sender/domain/legal inputs; perform actual provider sandbox, mail/domain and authority qualification before activation, without treating fixture peers as that evidence |
| H-05 | Explicit approval of concrete accepted public rollout and distribution channels | Not requested in design migration | AFV2-PROD-01 outward-facing activation | Present exact cohort/routes/rollback for final approval, after all preparation and qualification |

## Blocking semantics and closure

2026-11-16 BASE-01 preparation completed: Node exact-head Windows15/15 and
H-22 Linux20/20, Cloud Windows10/10 and Linux17/17, Contracts required Linux20/20,
independent review and source merges are recorded in the [handoff](codex-handoff.md)
and ledger. Real SQLite fixtures and8 PostgreSQL inventory tests proved only the
read-only preparation boundary; no migration/runtime/provider AR-01..12 is closed.
H-03 still gates later destructive admission. ENV/AR-13 remain complete/PASS.

2026-11-16 BASE-02 desktop retirement completed: Node PR86 merged
39c2c57fdaf3666ec046a22370aa2f2157c2d058 after finalf95af854 exact-head
Windows15/15 and H-22 Linux21/21, independently reviewed source and actual
78-file/77-digest Node/CLI package inspections on both native hosts. Shared
components, Linux Tmds.DBus/service assets and critical old execution/data guards
remain. See [handoff](codex-handoff.md) and ledger for exact receipts/artifacts.
This retires the isolated scaffold; it does not qualify MXC, V2 runtime/migration
or public activation, and closes no AR-01..12 item. Continue the next eligible
authorized task after recording; no task-boundary stop.

2026-11-16 DATA-01 store primitives completed in Node PR94, merged
1319107b26305e4c6c29574deea5c81f6036e7d1 at reviewed/tested165913b2cdd6.
Both final native data fixtures passed19/19 with0skips; unchanged formal profiles
passedWindows15/15 andH22Linux20/20 at the same source/tree. Applied0001..0015
history and unresolved journals remain preserved. Independent review accepted
the complete owner-backup closure and refusal of unqualified SQL-only retirement;
the original retirement rollback failure remains recorded. Local validation
packages were built, with no publicrelease. This proves the scoped SQLite/key/
identity/replay/backup boundary only; no Run/IPC/CLI/Stop/revocation or official
MXC profile is accepted here. No AR-01..12 row is closed; AR-03 stays FAILED.
Exact receipts/artifacts/rollback and review are in the handoff and ledger.

The owner permits current-machine local Windows access instead of its unstable
MCP. H-22 MCP successfully executed final required Linux profiles. The reconnect
stop rule is three consecutive failures within one outage; success resets the
counter. The earlier cumulative stop was a coordinator interpretation error,
not evidence of VPS failure. H-01/H-02 are not currently blocking this delivery.

A prerequisite blocks only the scope named in its Blocks cell. Missing native containment/terminal/resource/data safety is never a business deferral. A task with an unavailable provider can deliver only its specified development-stage code/fixture scope where the task explicitly allows it; it does not mark live/provider qualification proven or activate public surfaces. Mandatory local/self-host entitlement behavior remains a real code/runtime gate.

Use the actual bounded fixture lists in ID-01, HOST-01..03, WEB-01..04 and ACC-02. Renderer fixtures demonstrate presentation states only; external mail/provider peers demonstrate the production adapter and business code's handling of those inputs only. Signature verification, account/entitlement decisions, PostgreSQL state and native Node effects remain real. Final product journeys do not substitute fabricated success DTOs for a running Center or Node. Record each external provider/mail/authority qualification separately so a development pass cannot silently close AR-10.

Close an item with exact source/artifact/environment/command/result and independent review references. Failed experiments stay failed/blocked; do not reset them to pass after a version change without requalification. No retention setting creates a 24-hour development wait. No old acceptance item or one-time bootstrap permission silently authorizes V2 actions.

### 2026-11-16 native MXC admission failure

MXC-AOT-01 executed exact Node8252c8fc13d5973b27ab76bc18726eab8f21cb96 on
native Windows and designated H-22 Linux. Both AOT publishes had zero warnings;
Windows official signatures/executor/Job-zero observations passed. Linux public
SDK loading, pipe and real PTY passed, but the synthetic request-environment
sentinel appeared in owned native argv. The failed case retained PID3026318,
argv-hit=true and process-absent-after-Kill/Wait=true. The owning systemd unit
was inactive/not-found with emptyControlGroup afterward. No real credential,
raw argv, host setting change or private MXC patch was involved.

The latest Node draft4382988ce5b5ea40f4eb4583534a18bb135d371a adds only whitespace
formatting after tested825; it has no final required full statuses or merge.
Four staging negative cases passed on each native host. Exact originating
artifact/report/command identities remain in the Design result and handoff.
This failure blocks admission and its actual dependent profiles/Core; it does
not block independent API-01/BASE-01-dependent contract work. H-22 connectivity,
user manager and helper availability are not the blocker. Existing ENV/BASE
completion and AR-13 PASS remain valid. No public activation is authorized.
