---
task: ADOPT.08.ai-routing
status: complete
recorded: 2026-09-27
claimant: w-20260927-ai-lane
epoch: 1
---

## Evidence

Reviewed frozen AI main `31f734d7b8aece5f1c87cfda9d5c6ce420bcfc40` against Design `722e85641c8afb765dafcab5bc0e84d5a22d5a3c`, the exact delivery prompts and their mapped work-package obligation parts. [Repository facts](../adoption/AI.md) record source inventory, package pins, retained CI and original publication evidence. [Baseline](../adoption/baseline.md#ai) supplies the independently reviewed retarget PR and candidate. Open AI PR inventory remained empty when inspected for this adoption.

| Task | Classification | Obligation parts reviewed | Frozen source evidence / missing behavior | Bound write scope | Remaining scope | Conflicts / blockers |
|---|---|---|---|---|---|---|
| AIR.00 | gap | WP-43.00 (full) | src/model.ts only performs a fixed greeting tool/final text sequence; src/hello.ts pins one bootstrap model. No admitted multi-capability catalogue, policy snapshot, image/embedding/rerank adapters or canonical C# intent ports exist. | AI:src/providers/workers-ai/**; AI:src/inference/** | Entire outcome and task validation/evidence remain: env.AI.run adapters exist for default/fast text, accepted image context, bge-m3 embedding and bge-reranker-base rerank; model availability/frozen-config/request-limits/tool-stream-shapes are validated before dispatch; C# records admission/routing/supplier version while CF executes the already-admitted intent. | No D-001 conflict identified; start waits CON.10, POL.08. |
| AIR.05 | gap | WP-43.04 (transparency marking mechanism at the provider generation boundary; marking-coverage per artifact type) | No ContentOrigin tree, output marking carrier, marking retry or artifact-type coverage exists. | AI:src/providers/workers-ai/ContentOrigin/** | Entire outcome and task validation/evidence remain: The frozen content-origin profile is implemented at the point AI-generated content is produced; every artifact type carries the required transparency marking; malformed/hash-mismatched marks and marking retry are handled; this satisfies VG-01 once the regime determination is recorded. | No D-001 conflict identified; start waits AIR.00. |
| AIR.07 | gap | WP-43.06 (full) | tests/model.test.ts and dated Hello evidence exercise the bootstrap only; no tests/provider-fixtures catalogue coverage or selected-provider unreachable fixture matrix exists. | AI:tests/provider-fixtures/** | Entire outcome and task validation/evidence remain: Every provider integration is exercised against the provider's own test environment, with its contract shape frozen as recorded fixtures so ordinary CI never depends on provider availability. | No D-001 conflict identified; start waits AIR.00. |
| AIR.08 | gap | WP-43.07 (full) | Dated Hello inference evidence lacks selected capability normalization, metering settlement and client stub-removal proof; no AiMetering integration closure exists. | AI:tests/provider-fixtures/**; Cloud:tests/Cloud.Tests.Integration/AiMetering/** | Entire outcome and task validation/evidence remain: Actual Workers AI responses for each selected capability are recorded and normalized into independent sanitized fixtures; deterministic fixtures run on ordinary CI while the credentialed real-CF candidate gate proves exact Worker/model/config identity; the WP-17.05 stubbed managed provider path is retired. | No D-001 conflict identified; start waits AIR.00, AIR.02, AST.15. |

## Scope binding and validation

All listed implementation paths are planned additions to the existing single private TypeScript workspace, not identities to rename. Keep `package.json`, `package-lock.json`, `wrangler.json`, generated environment declarations and `eng/provenance/files.json` consistent when the owning implementation task introduces modules or published producer pins. Additions use existing source/provenance admission rules. Cross-repository Cloud paths remain owned Cloud module/test additions under the declared host-composition protocol; adoption authorizes no source edits. Workflow entry and route-pin changes follow RES-ai-workflow-and-routes; policy snapshot additions follow RES-private-configuration; architecture fixtures follow RES-architecture-tests.

No task is inherited; each full outcome remains open. Existing Hello admission/version guards, offline model fixtures and WP02 tooling are reusable bounded inputs, not accepted Harness, routing, MCP or complete WP05 behavior. The dated real Hello runs remain historical evidence only. No unresolved architecture conflict or retired-family source binding was identified in this slice; the ordinary prerequisite edges remain binding.

Read-only source, retained CI and original receipt review plus explicit-root `delivery.py check` validate this ledger-only change. No new build, runtime, inference, live-service, artifact download or publication check was run. Product runtime, provider coverage, business authority, metering and device integration remain untested by adoption. Exact reviewed head, ledger PR and merge commit are retained in the claim and PR record. Plan has no CI.
