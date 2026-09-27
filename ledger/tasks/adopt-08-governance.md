---
task: ADOPT.08.governance
status: complete
recorded: 2026-09-27
claimant: w-20260927-ai-lane
epoch: 1
---

## Evidence

Reviewed frozen AI main `31f734d7b8aece5f1c87cfda9d5c6ce420bcfc40` against Design `722e85641c8afb765dafcab5bc0e84d5a22d5a3c`, the exact delivery prompts and their mapped work-package obligation parts. [Repository facts](../adoption/AI.md) record source inventory, package pins, retained CI and original publication evidence. [Baseline](../adoption/baseline.md#ai) supplies the independently reviewed retarget PR and candidate. Open AI PR inventory remained empty when inspected for this adoption.

| Task | Classification | Obligation parts reviewed | Frozen source evidence / missing behavior | Bound write scope | Remaining scope | Conflicts / blockers |
|---|---|---|---|---|---|---|
| GOV.10 | gap | WP-05.00 (AI slice); WP-05.01 (AI slice); WP-05.02 (wire the forbidden-term scanner into AI's own PR build); WP-05.03 (AI's generated-client consumption checks); WP-05.04 (AI banned-API fixtures) | Existing eng/licence-boundary.mjs, dependency-policy.ts and their offline fixtures enforce bounded WP02 inputs. No tests/ArchitectureTests suite, owned expiring exceptions, complete forbidden-term/banned-API and generated-client fixture manifest or published GOV.04/GOV.05 engine consumption exists. | AI:tests/ArchitectureTests/**; AI:eng/policy/exceptions.json | Entire outcome and task validation/evidence remain: AI enforces its own layering/licence/naming/banned-API/contract-consumption rules independently as the sole owner of the Workflow Harness (per WP01's Cloud/AI module split). | No D-001 conflict identified; start waits GOV.04, GOV.05. |

## Scope binding and validation

All listed implementation paths are planned additions to the existing single private TypeScript workspace, not identities to rename. Keep `package.json`, `package-lock.json`, `wrangler.json`, generated environment declarations and `eng/provenance/files.json` consistent when the owning implementation task introduces modules or published producer pins. Additions use existing source/provenance admission rules. Cross-repository Cloud paths remain owned Cloud module/test additions under the declared host-composition protocol; adoption authorizes no source edits. Workflow entry and route-pin changes follow RES-ai-workflow-and-routes; policy snapshot additions follow RES-private-configuration; architecture fixtures follow RES-architecture-tests.

No task is inherited; each full outcome remains open. Existing Hello admission/version guards, offline model fixtures and WP02 tooling are reusable bounded inputs, not accepted Harness, routing, MCP or complete WP05 behavior. The dated real Hello runs remain historical evidence only. No unresolved architecture conflict or retired-family source binding was identified in this slice; the ordinary prerequisite edges remain binding.

Read-only source, retained CI and original receipt review plus explicit-root `delivery.py check` validate this ledger-only change. No new build, runtime, inference, live-service, artifact download or publication check was run. Product runtime, provider coverage, business authority, metering and device integration remain untested by adoption. Exact reviewed head, ledger PR and merge commit are retained in the claim and PR record. Plan has no CI.
