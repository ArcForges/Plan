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

## ID-01 qualification on 2026-11-17

Bounded recovery, export and deletion passed at Cloud
`8c1c67697ecb6727e71a3ccae44526d21408cec5`; PR160 merged as
`faf5dcb3638916f69fc2b833eea9d8d6d33571e9` with the same verified tree.
Windows10/10 and H22Linux17/17 required checks, real proof/crypto/PostgreSQL/race,
nine fuzz targets, schema13 backup/restore and candidate provenance passed.
Independent final source and original artifact/receipt review passed; see
[ID-01 evidence](docs/afv2-id-01-summary.md). Main-push CI44008751500 intentionally
skipped with zero artifacts. No deployment or public activation occurred.
This development acceptance does not close AR-03, AR-10, H-03, H-04 or H-05.

## Acceptance items

| ID | Item | Status | Blocks | Owner | Evidence / action |
|---|---|---|---|---|---|
| AR-01 | Full Windows official profile | PARTIAL; full qualification not established | AFV2-MXC-04 and dependent Core; final AFV2-ACC-01 | AFV2-MXC-02 | A new assigned IPv6 endpoint passed ordinary host controls on dcd91f6. Both strict selected-egress cases failed with zero peer receipts. Node 32e2ac1 corrects ordinary calibration to require exact independent counters. Its H-22 Linux repository check passed 20/20 and Windows failed at the CI step. WIN04/06 and the full 68-case receipt remain open. The successful repository checks and original Linux timeout on the older dcd91f6 are preserved. H-06 stays retired. See [current evidence](docs/afv2-mxc-02-progress.md). |
| AR-02 | Full Linux official profile | PASS | AFV2-MXC-04 and dependent Core; final AFV2-ACC-01 | AFV2-MXC-03 | H22 full same-cohort profile at50e602a passed72/72 with all cleanup confirmed; original receipt SHA25657f41658b57c18ff350fde2a9afc428c9434946b1aa829735325336019288fcf. Independent source/native review PASS; final022946a differs only by reviewed formatting. Final022 Windows15/15 and H22 Linux20/20 passed; Node PR96 merged687eb3a, Design76/77 merged through41d2532 and Plan checkpoint154 mergedfc96a51. MXC03 completion is recorded with this Plan change; MXC04 product admission remains separate. Preserve every original failed report; namespace-denial injection remains explicitly where-feasible NOT_RUN, DNS support is not claimed beyond observed denial, and stable IPv6/ingress restrictions remain. |
| AR-03 | AOT/native package and distribution admission | PASS — isolated official1.0.1 cohort and scoped source delivery complete | AFV2-MXC-01 actual cohort/AOT/provenance acceptance, then dependent profile qualification | AFV2-MXC-01 | Fresh9a9378bc warning-free AOT, native execution/cleanup and four invalid-stage cases per host passed under the accepted local-process boundary. Independent source/original-evidence review PASS at finald460524d. See [delivery evidence](docs/afv2-mxc-01-summary.md). Old825 FAILED report/argv observations are preserved. Final Windows15/Linux20 checks passed; Node93 mergedb2ebace5 and Design75 mergedaf28dc. Full platform combinations remain separate AR-01/02. |
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
| H-01 | Designated native Windows host with qualified Windows/PSEC prerequisites and repo toolchains | Owner authorizes direct native local Windows access instead of unstable MCP. Final ID01 exact8c1c Windows full10/10 passed144s on DEKU; prior ENV evidence retained. Composed MXC/PSEC qualification remains pending | Every repository-required Windows merge check; AFV2-MXC-02 native experiments and affected native delivery | Use designated native workstation and actual original receipts, never WSL/substitute host/handwritten status |
| H-02 | H-22 native Linux host with user manager, cgroupv2 delegation and admitted helpers | Owner-authorized ssh netcup reaches same v2202601329473427941/sammiller. ID01 exact8c1c full17/17 passed1028s after measured process0077/GMP2/DOTNET2 and bounded cleanup; final scopeOOM0. Root available279349833728B after builds; prior capacity/private-mode/OOM failures remain recorded. ENV/delegation evidence retained; MXC03 composed Linux qualification72/72 and final Node host checks passed, with original receipts in the task summary | Every repository-required Linux merge check; AFV2-MXC-03 native experiments and affected native delivery | Use same designatedH22 original receipts. No substitutehost/copiedstatus/root/network/security changes; cleanup and failed-run evidence retained |
| H-03 | Actual deployment inventory, approved consistent backups and security-successor/provider authority qualification | Last evidence is historical; no live authority assumed | Destructive migration/admission in AFV2-CENTER-01 and production operations in AFV2-HOST-03; not read-only preflight code | Owner/operator confirms configuration without exposing secrets; keep surfaces dark on uncertainty |
| H-04 | Official pricing/terms/provider and sender accounts/legal text/domain and operational approvals | TBD; no invented prices/quotas/trial | AFV2-PROD-01 activation; does not block architecture or development with graph-listed external fixtures | Owner supplies commercial/provider/sender/domain/legal inputs; perform actual provider sandbox, mail/domain and authority qualification before activation, without treating fixture peers as that evidence |
| H-05 | Explicit approval of concrete accepted public rollout and distribution channels | Not requested in design migration | AFV2-PROD-01 outward-facing activation | Present exact cohort/routes/rollback for final approval, after all preparation and qualification |
| H-06 | Retired extra direct Windows-to-VPS endpoint prerequisite | RETIRED: code and host execution use GitHub exact fetch over healthy ssh netcup. Original TCP calibration failures remain historical experiment data, not an SSH failure or a requirement to open a port | None. Required Windows sandbox network effects remain AR-01/MXC-02 acceptance; no pass is inferred | SSH is only the owner-selected Linux execution transport. Do not derive new tests, prohibitions or endpoint approval from that instruction. Implement the original WIN04/06 controlled-endpoint acceptance within task scope, preserving settings and evidence; no network/proxy/firewall changes or extra human prerequisite. |

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

### 2026-11-17 owner-approved local process boundary

The owner explicitly supersedes the local argv-absence admission condition. Visibility
of intentionally supplied workload values in trusted owner/admin OS process metadata
is not publication to Plan/GitHub and must not block development by itself. Public
repositories, shared evidence, ordinary logs and telemetry still exclude real secrets;
actual unauthorized payload access and inherited host credentials remain separate.
At that policy checkpoint AR-03 was pending revised-rule native verification;
the current row above records the subsequent fresh cohort PASS. The original
2026-11-16 observation and its then-applicable failure remain below as dated evidence.

### Historical 2026-11-16 native MXC admission failure

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
Under the then-applicable rule, this failure blocked admission and dependent
profiles/Core; it did not block independent API-01/BASE-01-dependent contract work.
That local-argv-only blocking interpretation is superseded by the 2026-11-17 owner
decision above; full revised-rule cohort/profile evidence is still required. H-22 connectivity,
user manager and helper availability are not the blocker. Existing ENV/BASE
completion and AR-13 PASS remain valid. No public activation is authorized.
