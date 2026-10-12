# Legacy disposition (2026-10-12)

What happened to the previous delivery model and its in-flight work when ArcForges became the flagship (ArcForges-Design AD-0001, AD-0013, AD-0014). Nothing here is resumed by the new plan. The facts come from the verified scope status of 2026-10-11 (`C:\MyFile\Projects\ArcForges\.claude\coordinator\scope-status-2026-10-11.md`) and checks of the local repositories on 2026-10-12.

## 1. Repository authority

| Repository | Frozen at | Role |
|---|---|---|
| ArcForges/ArcForges-Design-Parallel | main `64173614` | Read-only design history; cited by commit |
| ArcForges/Plan-Parallel | main `5ccbb392` (`[APP.02] Record delivery (complete) (#488)`) | Read-only plan, ledger and records history |

The new repositories ArcForges/ArcForges-Design and ArcForges/Plan are the only authorities for active work. The local historical clones `C:\MyFile\Projects\ArcForges-Design` and `C:\MyFile\Projects\Plan` track the frozen repositories.

## 2. Superseded mechanisms

| Mechanism | Disposition |
|---|---|
| P2-018 delivery graph and `tools/delivery.py` (claims, leases, follow-ups, roles, integration roles, `build-slot`) | Superseded by `delivery-graph.json` and `tools/plan.py` (serial, no claims or slot) |
| Plan-Parallel `execution-policy.md`, `single-task-command.md`, `arcforges-implementation.md`, entry prompts | Superseded by `execution-policy.md`, `delivery-procedure.md` and `entry-prompts.md` |
| Launcher `C:\MyFile\Projects\ArcForges - Final.md` (2026-10-10 version) | Archived verbatim as [arcforges-final-2026-10-10.md](arcforges-final-2026-10-10.md) (SHA-256 prefix `7c9a64d8994fade6`). The file now holds the new single objective. |
| Early launcher `C:\MyFile\Projects\ArcForges.md` | Archived verbatim as [arcforges-launcher-early.md](arcforges-launcher-early.md). The file now holds a superseded notice. |
| Agent definitions `haiku-worker`: project-level `ArcForges/.claude/agents/haiku-worker.md` (Haiku, build slot, claims) and user-level `%USERPROFILE%/.claude/agents/haiku-worker.md` (model switched to Opus 5.5 on 2026-10-10, but still mandating `delivery.py build-slot run`), with its backup `haiku-worker.md.bak-20261010` | Both moved, not deleted, to `ArcForges/.claude/coordinator/retired-agents/` on 2026-10-12, so no session is offered them (the user-level move followed review finding R-30). Archived here as [legacy-agents/haiku-worker.md](legacy-agents/haiku-worker.md) and [legacy-agents/user-level-haiku-worker.md](legacy-agents/user-level-haiku-worker.md). Reasons: no Haiku (user decision 2026-10-10) and no build slot. |
| "Reviewer coverage" and "Pre-push coverage" practices | Superseded by distinct-evidence verification (execution policy §3) |

## 3. Historical tasks at the switch (2026-10-11 closeout)

| Group | Tasks | Disposition for the new plan |
|---|---|---|
| Complete | CON.41 (Contracts #100, cohort 1.0.0-ci.368.1), APP.02 (ArcScope #27, 485c8d6d), cleanup 5.2 (AI Worker retired through HAR.40) | History. Their merged results are part of the reused baseline ([baseline.md](../baseline.md)). |
| Delivered, completion waiting on deferred checks | PLT.09, PLT.10, PLT.11, PRF.04 (LocalRpc and launch identity), PLT.45, PLT.33 | The merged code is reused: LocalRpc is extended by AF-DP-01. Their deferred human checks correspond to AR-02 (second account) and AR-10 (screen reader). No old completion bookkeeping continues. |
| Delivered, waiting on prerequisites | PLT.15, PLT.24, PLT.46, PLT.20, PLT.40, PLT.44, PLT.32, PLT.57, PLT.35, PLT.53, PRF.02, PRF.05, PRF.11, PRF.06; CLOUD.72, HAR.40 (outside the closure) | Merged code stays where it is. Prerequisite chains (PLT.66, APP.03, the CLOUD.* stream and account chain) are **not** scheduled. The new plan schedules only what the flagship needs, as new AF-* tasks. |
| Merged but not recorded | CON.43: Contracts #101, merged by the user as `b774c322` at the reviewed head; main CI and Security green; cohort 1.0.0-ci.370.1 published | Recorded here as a historical fact. Plan-Parallel is frozen, so its ledger is not updated. 1.0.0-ci.370.1 is admissible: its publishing commit `b774c322` is on Contracts main. |
| Stopped in progress | NAT.01 (DesktopPlatform), POL.01, CLOUD.05, CLOUD.13 (Cloud) | **Their work no longer exists locally.** On 2026-10-12 the worktrees (`DesktopPlatform/.worktree/nat-01`, `Cloud/.worktree/pol-01`, `cloud-05`, `cloud-13`), their local `task/*` branches and the session scratch files were absent. They were removed during the user's disk cleanup after the 2026-10-11 closeout, and none had been pushed. The new plan needs none of them. If a similar capability is needed later, a new task implements it from the design. |
| Not started | PRF.12, PLT.66, APP.03, POL.02, COM.06, CLOUD.12–19, CLOUD.21–23, CLOUD.26, CLOUD.29–34, CLOUD.86, CON.42, CLOUD.88 | Not scheduled. They belong to the superseded family scope. CON.42 and CLOUD.88 (dead Maven configuration) remain optional hygiene (§5). |

## 4. Records left as they were

- **Claims and integration roles.** Plan-Parallel still shows "claimed" claims and expired integration roles (AI, Cloud, Design, DesktopPlatform, Plan) and a claim for CON.43. They are frozen history. The new tooling never reads them, and no lease matters any more.
- **Record nits.** The nits noted on 2026-10-11 (PLT.10/11 handoffs, stale `next` fields, the WEB.40 Cloudflare version note) remain in the frozen history.

## 5. Open user actions from history (optional hygiene; not prerequisites)

| Item | Action (user) |
|---|---|
| 5.1 npm dist-tags | npm `latest` points at the rolled-back 1.0.0-ci.350.1 for four packages. The six pending commands are in the coordinator README: set `latest` to 1.0.0-ci.324.1 for proto, api-client, contract-fixtures and operator-client, and remove `next` from proto and api-client. Nothing is unpublished. |
| 5.3 Maven | Delete the Contracts `maven-central` environment and the `MAVEN_PUBLISH_ENABLED` variable (repository settings are the user's) |

## 6. Standing constraints carried forward

- **Dependabot:** PRs stay untouched. This includes the open PRs for rolled-back versions (Contracts #96, Cloud #84/#88, Web #37, Mobile #28, ArcScope #26).
- **Rolled-back versions:** never pin or admit Contracts 1.0.0-ci.350.1 or DesktopPlatform Build.Policy 1.0.0-ci.124.1.
- **Admission:** never admit a first-party version whose publishing commit is not an ancestor of its producer's main.
