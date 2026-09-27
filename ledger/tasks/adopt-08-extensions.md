---
task: ADOPT.08.extensions
status: complete
recorded: 2026-09-27
claimant: w-20260927-ai-lane
epoch: 1
---

## Evidence

Reviewed frozen AI main `31f734d7b8aece5f1c87cfda9d5c6ce420bcfc40` against Design `722e85641c8afb765dafcab5bc0e84d5a22d5a3c`, the exact delivery prompts and their mapped work-package obligation parts. [Repository facts](../adoption/AI.md) record source inventory, package pins, retained CI and original publication evidence. [Baseline](../adoption/baseline.md#ai) supplies the independently reviewed retarget PR and candidate. Open AI PR inventory remained empty when inspected for this adoption.

| Task | Classification | Obligation parts reviewed | Frozen source evidence / missing behavior | Bound write scope | Remaining scope | Conflicts / blockers |
|---|---|---|---|---|---|---|
| EXT.10 | gap | WP-41.07 (Cloud MCP HTTP placement through the AI Worker adapter); WP-41:sec-8-gate-item-8-mcp-vocabulary-mapping (package-level obligation contribution) | No src/mcp tree or MCP adapter/transport/secret-reference/egress mapping exists. The greeting tool is not an MCP connector. | AI:src/mcp/** | Entire outcome and task validation/evidence remain: Cloud-placed MCP connections route HTTP through the AI Worker adapter only; standard MCP protocol is preserved; each connection has one placement/secret owner and exact failure/egress behavior; MCP content is treated as untrusted data. | No D-001 conflict identified; start waits CON.15. |

## Scope binding and validation

All listed implementation paths are planned additions to the existing single private TypeScript workspace, not identities to rename. Keep `package.json`, `package-lock.json`, `wrangler.json`, generated environment declarations and `eng/provenance/files.json` consistent when the owning implementation task introduces modules or published producer pins. Additions use existing source/provenance admission rules. Cross-repository Cloud paths remain owned Cloud module/test additions under the declared host-composition protocol; adoption authorizes no source edits. Workflow entry and route-pin changes follow RES-ai-workflow-and-routes; policy snapshot additions follow RES-private-configuration; architecture fixtures follow RES-architecture-tests.

No task is inherited; each full outcome remains open. Existing Hello admission/version guards, offline model fixtures and WP02 tooling are reusable bounded inputs, not accepted Harness, routing, MCP or complete WP05 behavior. The dated real Hello runs remain historical evidence only. No unresolved architecture conflict or retired-family source binding was identified in this slice; the ordinary prerequisite edges remain binding.

Read-only source, retained CI and original receipt review plus explicit-root `delivery.py check` validate this ledger-only change. No new build, runtime, inference, live-service, artifact download or publication check was run. Product runtime, provider coverage, business authority, metering and device integration remain untested by adoption. Exact reviewed head, ledger PR and merge commit are retained in the claim and PR record. Plan has no CI.
