---
task: GOV.15
status: delivered
recorded: 2026-10-05
claimant: w-c20261005-gov15
epoch: 1
---

# WP05 stage integration verification

## Evidence

- Implementation: [DesktopPlatform #142](https://github.com/ArcForges/DesktopPlatform/pull/142), exact reviewed and merged head `2dfc0971f701d1e8571243b91e75ac5117645da1` (round 1 requested changes at `254d6702ea0d6e8d1e49fadb5a9c6fcb0481b101`; the [round 2 approval](https://github.com/ArcForges/DesktopPlatform/pull/142#issuecomment-5988862698) found the earlier blocking and medium findings closed), merge commit `8bee36bfd13160513743e343fe8b104e17011b53` on DesktopPlatform main. The head's pull-request run [37267308609](https://github.com/ArcForges/DesktopPlatform/actions/runs/37267308609) passed every check, including `stage-integration` and the aggregate `ci` job; the main-push run [37270229806](https://github.com/ArcForges/DesktopPlatform/actions/runs/37270229806) (Publish NuGet, which calls the pull-request gate) succeeded. Provider job status only; no downloads. Reviewer and author share one GitHub account.
- Tool: `eng/stage_integration/` evaluates eleven rules (SI-01..SI-11) over the published package and dependency metadata (NuGet, npm and Gradle locks, package manifests, the producer registries, wrangler and workflow declarations, each repository's own exceptions) of the seven repositories at one pinned commit each, read over HTTPS without cloning or reading source: single registered producer; no cross-repository project, source, submodule or link dependency; the producer access matrix for direct and transitive consumption including packages reached only through a third-party package and registry packages without a policy audience (fail closed); AGPL in an Apache closure only through the consumer's own unexpired RP-03 row; no desktop native or UI asset in Cloud; Mobile imports no AGPL implementation; one Harness owner; each repository's own policy host runs as a command in an unfiltered, unconditional, pull-request-reachable workflow; snapshot completeness, policy binding and age; exception data. 47 offline tests (a positive world and a negative fixture per rule, plus the independent reviewer's surviving mutants). The new `stage-integration` job is in `pr-gate.yml` and in the aggregate `ci` job's `needs`; the repository has no required-status-check rule, so `ci` is the gate.
- Pinned result: snapshot read at DesktopPlatform `5405d80a7e49d7d5b385db6859ab9ab3c5d6dd18`, Contracts `db9df61430cd8a6c3765a7986bcc4b4165307abc`, ArcScope `80dd7f24009a5259cf432551b26d70b634b7b746`, Cloud `ea08736d571cf0f4b44e022117cb44652a392e66`, AI `5421c3789240093b2fce36322c2eb7773325ec7b`, Web `794ef933d3dba836c60b29a481091d40ab4a2b1a`, Mobile `377fa5d6e00b7a50d37d2f8434f915850c6d5b9f`: zero findings; the reviewer re-read the same pins with `drift` and found no difference (reviewer-reported). Hosted main-push runs at those pins all succeeded (claimant-observed, receipt table).
- Design receipts: [Design #228](https://github.com/ArcForges/ArcForges-Design/pull/228), reviewed and merged at `fd516cab9c6e7f65a6ed71040eb5169338f844f7`, merge `64d12ebcd72cac78a170846818d645fa41b9b5d4`: `wp05-90-integration-evidence.md` and `wp05-stage-acceptance.md/.json`, joining GOV.04-GOV.14 (ledger-sourced, labelled) with the observed pins and hosted runs. [Design #235](https://github.com/ArcForges/ArcForges-Design/pull/235) amends the receipt with the merge identity, the merged-head run and the known gaps (open until reviewed and merged).
- Supporting planning repairs, merged before the implementation: [Design #226](https://github.com/ArcForges/ArcForges-Design/pull/226) (merge `e7327fbdb60ed2df63162866a6031512899408fc`) with [Plan #292](https://github.com/ArcForges/Plan/pull/292) (merge `dce0ae9315837b409b0507e1bd4e2505778de11d`) for the workflow job write scope and the `RES-desktopplatform-build-config` append; [Design #230](https://github.com/ArcForges/ArcForges-Design/pull/230) (merge `c4712959a7b6df11c333acb1491c7b83329fa400`) with [Plan #295](https://github.com/ArcForges/Plan/pull/295) (merge `4ad036717f84840a50737de6758d0f8bf7430a8c`) adding the GOV.07 completion prerequisite.

## Why `delivered`

GOV.15's completion prerequisite on GOV.07 is open. GOV.07 is itself delivered, not complete: the ArcScope executable is classified non-production, so its banned-API scan and production-only layer rules are not enforced until the Build.Policy function-pointer scanner repair (GOV.20) lands and ArcScope moves its pin. The stage receipt therefore cannot join ten completed repository results. Complete GOV.15 only after GOV.07 is complete and the stage receipt is amended to say so.

## Known gaps and open items (not claimed as done)

- The snapshot is a pin, not a live view; refresh is manual (`snapshot`, with `drift` as local opt-in comparison). Owner: the DesktopPlatform integration owner, after any merge that changes a repository's published metadata and at least every 45 days; `verify` fails hard once the pin is older. A warning near 30 days and a scheduled refresh are suggested follow-ups, not implemented. Offline `verify` does not bind facts to sources; only `drift` re-reads the providers.
- SI-09 does not detect a gate that is backgrounded, piped to `tee`, in a dead shell branch, or under a job whose `needs` never runs. SI-02 reads locks, manifests and settings only (no project files, `build.gradle.kts` or `NuGet.config`); the foreign-UI denylist is name-pattern based.
- PG-11 stays open: GOV.13 reports 0 of 406 invariants enforced. Metadata cannot close native isolation, Native AOT, Cloudflare or commercial gates.
- GOV.21 (the scheduled Design preview watch) appends to the same `eng/provenance/files.json` and DesktopPlatform policy documents but adds no `ci.needs` entry and touches no `pr-gate.yml`; it does not overlap GOV.15's scope.

## Untested

No runtime, device, GUI, browser, live-service, inference or installed-consumer behaviour; no macOS; Linux and Windows only through hosted CI. No artifact was downloaded, hashed, tagged or republished. Negative fixtures are synthetic worlds, not observations of the real repositories.

## Closure

Substitutes still in use: none introduced. The claim, reviews and receipts are retained on the PRs above. The GOV.15 completion follow-up (state `complete`) needs GOV.07 complete and a reviewed amendment of this record.

## Amendment: snapshot expiry date and blast radius

The snapshot was collected 2026-10-05 and the 45-day bound makes `verify` fail SI-10 from about 2026-11-19. That failure fails the `stage-integration` job, therefore the aggregate `ci` job and the Publish NuGet main run, for every DesktopPlatform change until the DesktopPlatform integration owner runs `snapshot`, reviews the diff and merges the refreshed `snapshot.json`. Follow-up (not implemented): a warning at about 30 days so the refresh precedes the failure, and a scheduled refresh reminder; the refresh is also needed earlier whenever another repository changes its published metadata.
