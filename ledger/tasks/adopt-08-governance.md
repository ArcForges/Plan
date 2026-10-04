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

## Post-adoption adjustment (2026-10-04)

This is a later adoption adjustment under DLV-22, introduced by the Design governance-chain planning repair [PR 210](https://github.com/ArcForges/ArcForges-Design/pull/210) (Design source head `68827a21b4525660d4f6d2b88c965433ca0dbef6`; the merge commit is retained in the pull request history, since embedding it would change the reviewed head). It does not reopen or replace this completed slice: the front matter, status, recorded date, claimant, epoch and every frozen classification above are unchanged.

| Task | Classification | Evidence and actual source binding | Remaining scope and blockers |
|---|---|---|---|
| GOV.10 | gap (classification unchanged; start edges and write scope rebound) | AI main `31f734d`: a pure Node/TypeScript workspace (`package.json`, `eng/project.mjs`, `eng/licence-boundary.mjs`, `eng/dependency-policy.ts`, `.gitleaks.toml`), no .NET project and no ArcForges.Build.Policy reference, so the row above that names GOV.04/GOV.05 engine consumption cannot be satisfied as written. | Implement the Node/TypeScript mechanism mirroring GOV.11 (necessarily separate code from GOV.04's .NET engine) over `tests/ArchitectureTests/**`, `eng/policy/**`, `eng/provenance/**`, `package.json`, `package-lock.json`, `eng/project.mjs`, the vitest/tsconfig includes and the dependency-review files. The GOV.04 and GOV.05 start edges are replaced by the CON.23 artifact edge for the published naming scanner and policy asset. No security-scanner or `.gitleaks.toml` change is authorized. The planned write scope listed in the table above is superseded by the graph record. |

## Post-adoption adjustment (2026-10-04, GOV.10 supporting scope)

This is a second later adoption adjustment under DLV-22, introduced by the Design planning repair [PR 213](https://github.com/ArcForges/ArcForges-Design/pull/213) (Design source head `9719af54d9ee204b22406f513abbbd440f444515`; the merge commit is retained in the pull request history, since embedding it would change the reviewed head). It does not reopen or replace this completed slice: the front matter, status, recorded date, claimant, epoch, every frozen classification and the first adjustment above are unchanged.

| Task | Classification | Evidence and actual source binding | Remaining scope and blockers |
|---|---|---|---|
| GOV.10 | gap (classification unchanged; supporting write scope extended) | AI main `31f734d`: `eng/build-identity.mjs` reads the retired single-schema field of the producer's `source.json`; the published `@arcforges/proto` candidates that carry the CON.23 naming tools (first `1.0.0-ci.129.1`) declare the ContractSet through the producer's own `build-identity.json` with per-subject versions and one or several schema sources, so the pin cannot be taken without the build identity reading it (as Web GOV.11 did). The immutable `ai-worker-r8` profile repeats the one public protobuf `api_pb.js` digest line that `.gitleaks.toml` accepts for r1 to r7 by exact path pattern. | Implement the remaining scope with the supporting bindings recorded in the graph: `eng/build-identity.mjs`, `eng/version-sources.json`, `eng/tests/build-identity.test.mjs`, `eng/tests/release-provenance.test.mjs`, `tests/tsconfig.json`, `README.md`, `docs/development.md`, and only the exact `ai-worker-r8` path-pattern extension of the existing `.gitleaks.toml` allowlist. No other security-scanner, secret-scan, rule, workflow or dependency change is authorized. |
