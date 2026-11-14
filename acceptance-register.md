# V2 acceptance and human prerequisites

All items below describe future implementation/activation evidence. Source research and existing V1 acceptance do not satisfy them. A missing required host check also blocks the current documentation PR merge independently of these product tasks.

## Acceptance items

| ID | Item | Status | Blocks | Owner | Evidence / action |
|---|---|---|---|---|---|
| AR-01 | Full Windows official profile | NOT_RUN | AFV2-MXC-04 and dependent Core; final AFV2-ACC-01 | AFV2-MXC-02 | Run MXC-WIN-01..06 on exact qualified native Windows; no pipes-only or separate-feature substitute |
| AR-02 | Full Linux official profile | NOT_RUN | AFV2-MXC-04 and dependent Core; final AFV2-ACC-01 | AFV2-MXC-03 | Run MXC-LNX-01..05 on H-22 with actual PTY/user-manager/cgroup/helpers |
| AR-03 | AOT/native package and distribution admission | NOT_RUN | AFV2-MXC-04 and profile admission | AFV2-MXC-01 | MXC-AOT-01 on both native hosts; exact hashes/source/schema/license/architecture and warning-free publish |
| AR-04 | Crash and unknown ownership recovery | NOT_RUN | AFV2-REC-01 delivery; full native acceptance | AFV2-REC-01 | Same Run owner survives Node loss; supervisor loss/reboot/no PID guessing and exact outer-scope empty tests |
| AR-05 | Owned Sandbox data and deletion safety | NOT_RUN | AFV2-FILE-02 delivery; final acceptance | AFV2-FILE-02 | Native path/identity/managed-use/partial effect/import/export/delete recovery tests; no blanket refusal |
| AR-06 | OS-effective resource budget | NOT_RUN | AFV2-RES-02 delivery and dependent allocation | AFV2-RES-02 | Saturation and desired/applied/readback failures on both hosts; aggregate reductions before increases |
| AR-07 | PostgreSQL guarded upgrade and restore | NOT_RUN | AFV2-CENTER-01 runtime migration admission and live upgrade | AFV2-CENTER-01 | Fresh/schema10/schema11 actual migration runner with 0011 security floor/backup/receipt guards; static DDL is not proof |
| AR-08 | Remote control and data effect consistency | NOT_RUN | AFV2-CENTER-03 delivery and AFV2-ACC-02 final acceptance | AFV2-CENTER-03, AFV2-ACC-02 | Real Node+Go+PG loss/replay/revoke/template tests and final self-host/official journeys |
| AR-09 | Blazor responsive/accessibility and recovery UX | NOT_RUN | AFV2-WEB-04 completion and AFV2-ACC-02 acceptance | AFV2-WEB-04 | Explicit local browser keyboard/focus/viewport/offline/unknown states; no browser/live CI |
| AR-10 | Hosted service/commerce external qualification | NOT_RUN; prices, quotas, trial settings TBD | Mandatory local/self-host mode correctness blocks AFV2-HOST-01; unavailable provider/domain/legal activation blocks AFV2-PROD-01 only | AFV2-HOST-01, AFV2-HOST-02, AFV2-HOST-03, AFV2-ACC-02 | Real self-host independence and official expiry; code uses approved provider fixtures; live provider/account/authority qualification remains explicit |
| AR-11 | Coherent install/update/rollback artifact | NOT_RUN | AFV2-DIST-01 and AFV2-DIST-02 release acceptance | AFV2-DIST-01, AFV2-DIST-02 | Real fresh install and schema-aware update/backup restore; signed exact native cohort |
| AR-12 | Complete V2 release candidate | NOT_RUN | AFV2-ACC-01, AFV2-ACC-02 and AFV2-PROD-01 | AFV2-ACC-01, AFV2-ACC-02 | All mandatory native+remote/data/resource/local/business journeys on same final cohort; unresolved safety cannot be deferred |

## Human prerequisites

| ID | Prerequisite | Current observation | Blocks | Owner / action |
|---|---|---|---|---|
| H-01 | Designated native Windows MCP host with qualified Windows/PSEC prerequisites and repo toolchains | Not exposed to current design session; host health not assessed | Every repository-required Windows merge check; AFV2-MXC-02 native experiments and affected native delivery | Owner supplies existing host connection/prerequisites; never another host, WSL or handwritten status |
| H-02 | H-22 native Linux MCP host with user manager, cgroupv2 delegation and admitted helpers | Not exposed to current design session; host health not assessed | Every repository-required Linux merge check; AFV2-MXC-03 native experiments and affected native delivery | Owner supplies existing host connection/prerequisites; no SSH/proxy or local scratch substitution |
| H-03 | Actual deployment inventory, approved consistent backups and security-successor/provider authority qualification | Last evidence is historical; no live authority assumed | Destructive migration/admission in AFV2-CENTER-01 and production operations in AFV2-HOST-03; not read-only preflight code | Owner/operator confirms configuration without exposing secrets; keep surfaces dark on uncertainty |
| H-04 | Official pricing/terms/provider accounts/legal text/domain and operational approvals | TBD; no invented prices/quotas/trial | AFV2-PROD-01 activation; does not block architecture or development with allowed external fixtures | Owner makes commercial decisions and supplies configured provider/domain/legal assets |
| H-05 | Explicit approval of concrete accepted public rollout and distribution channels | Not requested in design migration | AFV2-PROD-01 outward-facing activation | Present exact cohort/routes/rollback for final approval, after all preparation and qualification |

## Blocking semantics and closure

A prerequisite blocks only the scope named in its Blocks cell. Missing native containment/terminal/resource/data safety is never a business deferral. A task with an unavailable provider can deliver only its specified development-stage code/fixture scope where the task explicitly allows it; it does not mark live/provider qualification proven or activate public surfaces. Mandatory local/self-host entitlement behavior remains a real code/runtime gate.

Close an item with exact source/artifact/environment/command/result and independent review references. Failed experiments stay failed/blocked; do not reset them to pass after a version change without requalification. No retention setting creates a 24-hour development wait. No old acceptance item or one-time bootstrap permission silently authorizes V2 actions.
