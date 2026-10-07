# ArcForges delivery task prompts — Cloud Harness

Generated from Design `docs/planning/delivery/delivery-graph.json` by `tools/delivery.py`; do not edit by hand.
Each block is self-contained. Claim a task only when `python tools/delivery.py ready` lists it, with
`python tools/delivery.py claim <TASK-ID> --worker <name>`, then follow `arcforges-implementation.md`.
Tasks are ordered by lane for reading; the order is not a schedule.

## Cloud Harness

```text
Execute ArcForges delivery task HAR.00 — Turn loop, tool batching and bounds (RunWorkflow core).

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\harness.md (anchor task-har-00).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\AI (integration owner: AI integration owner, the holder of roles/integration-ai).
Claim and handoff record: claims/har-00 (python tools/delivery.py claim HAR.00 --worker <name>); task branch task/har-00 in AI; ledger record ledger/tasks/har-00.md.
Kind/size: service/XL. Baseline: not-started.
Outcome: The sole RunWorkflow implements deterministic Workflow identity with C# claim/epoch/generation and actual deployed Worker version; iteration/context references and model/tool dispatch intent persist before effects; immutable outcome receipts persist before continuation; model/tool/parallel/progress/time/step budgets and declared conflict sets are enforced, with a 60-second execution lease renewed every 20 seconds during long awaits.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-52.00 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\52-cloud-harness.md, anchor rule-wp-52.00

Entry condition: adoption slice ADOPT.08.harness is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] CLOUD.01: the single Cloud host and its lease-fenced hosted services
- [contract] CON.15: the generated internal AI HTTP port surface (claim/renew/reconcile/dispatch/control)
- [contract] CON.10: published ToolRequest and StructuredValue records in the task/agent closure
- [artifact] CLOUD.05: lease-fenced finite durable jobs (Cron/Queue/Workflow wake) in the Cloud host
Completion prerequisites (may start earlier; cannot complete before these are complete):
- [integration] AIR.00: a dispatchable model/tool call target

Permitted write scope: AI:src/workflows/RunWorkflow.ts; Cloud:src/Cloud/ArcForges.Cloud.Modules.Task/**
Shared resources (follow the owner protocol): RES-ai-workflow-and-routes (append): The Workflow entry is owned by the turn-loop task; other Harness tasks add steps through their own modules; the route-pin table changes only with a policy snapshot. Any task that runs against the AI deployment environment holds the lease `leases/res-ai-workflow-and-routes` for that live run only.; RES-cloud-host-composition (append): Each module registers through its own module entry point and route fragment; the host composition only lists modules; route and binding conflicts are resolved by the integration owner at merge.
Permitted substitutes (never real integration evidence): SUB-provider-response-fixture: turn-loop/dispatch-intent/budget/conflict-set state-machine correctness under scripted responses Real producer ['AIR.00']; removed by HAR.05; SUB-same-app-fixture-tool: tool-batching, conflict-set enforcement and parallel-limit mechanics Real producer ['AST.11']; removed by HAR.05
Unblocks: AND.24, AST.19, CLOUD.67, HAR.01, HAR.02, HAR.03, HAR.04, HAR.05, HAR.06, WEB.27

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Real Workflow with forced duplicate start, replay, 120-second model await, lease loss/stale outcome, no-progress and every bound test; no automatic effect retry after intent. CF Workflow deployment tests apply to the loop per BR-02; C# integration ports retain the AOT gate. Real CF only at the credentialed candidate gate, not ordinary CI (P2-017).
Completion evidence for the ledger: Loop-bound, crash-resume, no-progress and conflict-batching results.
Notes: Foundational early risk proof: if the CF Workflow model cannot actually sustain the durable claim/epoch/generation + budget semantics at the required step-guard ceiling (24000 steps, 25000 hard ceiling per contracts/05-cloudflare-integration.md), the entire single-Harness architecture is affected.
```

```text
Execute ArcForges delivery task HAR.01 — Context assembly and compaction.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\harness.md (anchor task-har-01).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\AI (integration owner: AI integration owner, the holder of roles/integration-ai).
Claim and handoff record: claims/har-01 (python tools/delivery.py claim HAR.01 --worker <name>); task branch task/har-01 in AI; ledger record ledger/tasks/har-01.md.
Kind/size: service/L. Baseline: not-started.
Outcome: Context assembles through authorized C# ports in a fixed order, pages under one snapshot hash, and retains immutable source pins/content origins; invocable capabilities are filtered before model declaration with budget truncation disclosed; compaction refs are stored derived; source/revision and active grant are revalidated before mutation.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-52.01 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\52-cloud-harness.md, anchor rule-wp-52.01

Entry condition: adoption slice ADOPT.08.harness is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] HAR.00: the turn-loop skeleton to assemble context inside
- [contract] CON.11: typed TranscriptWindow/CompactionRecord records (model 05)
Completion prerequisites (may start earlier; cannot complete before these are complete):
- [integration] SRCH.00: a retrieval/context source to pull from (fixture-backed lexical-only path is sufficient at start)
- [integration] CON.33: actual published execution configuration pin and transcript semantic hash producer

Permitted write scope: AI:src/workflows/context.ts; Cloud:src/Cloud/ArcForges.Cloud.Modules.Task/**
Shared resources (follow the owner protocol): RES-ai-workflow-and-routes (append): The Workflow entry is owned by the turn-loop task; other Harness tasks add steps through their own modules; the route-pin table changes only with a policy snapshot. Any task that runs against the AI deployment environment holds the lease `leases/res-ai-workflow-and-routes` for that live run only.
Unblocks: HAR.05

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Large-context paging, permission loss, stale source, prior-compaction-version, unsupported-capability tests; no raw prompts in Workflow checkpoints; all four model-05 context vectors (under budget, compaction, protected overflow, changed branch) plus wrong role/tool-pair, hash and origin-installation negatives; HC-09 refusal and no-customer-debit-for-compaction assertions; both inline and transient-object input.
Completion evidence for the ledger: Context permission, staleness and compaction results.
Notes: 

docs/decisions/assistant-output-snapshots-and-semantic-profiles-2026-10-07.md: consume actual CON33 snapshot/configuration pin/shared semantic-v1 profiles. Generation/shape/helper publication does not itself implement real output storage, logical-body authorization/decryption, tokenizer materialization, execution or current permissions. Preserve original producer starts and acceptance; no success stub/private DTO or heuristic model budget.
```

```text
Execute ArcForges delivery task HAR.02 — Approval, cancellation and crash recovery.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\harness.md (anchor task-har-02).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\AI (integration owner: AI integration owner, the holder of roles/integration-ai).
Claim and handoff record: claims/har-02 (python tools/delivery.py claim HAR.02 --worker <name>); task branch task/har-02 in AI; ledger record ledger/tasks/har-02.md.
Kind/size: service/L. Baseline: not-started.
Outcome: Approval waiting is bounded (selected wait/reconcile steps, seven-day bound) with reauthorization on resume; explicit cancel/pause/steer controls and C# reconciliation exist; wait/cancel/recovery always yields one canonical outcome or an explicit unknownEffect via the intent-to-owner/provider-evidence-to-deadline-to-user-decision ladder; a UI session closing never cancels a durable Task.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-52.02 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\52-cloud-harness.md, anchor rule-wp-52.02

Entry condition: adoption slice ADOPT.08.harness is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] HAR.00: the turn-loop skeleton to interleave approval into
- [contract] CON.10: published internal admission and commit-before-dispatch port schema
Completion prerequisites (may start earlier; cannot complete before these are complete):
- [integration] COM.12: the real admission/commit-before-dispatch port

Permitted write scope: AI:src/workflows/approval.ts; Cloud:src/Cloud/ArcForges.Cloud.Modules.Task/Approvals/**
Shared resources (follow the owner protocol): RES-ai-workflow-and-routes (append): The Workflow entry is owned by the turn-loop task; other Harness tasks add steps through their own modules; the route-pin table changes only with a policy snapshot. Any task that runs against the AI deployment environment holds the lease `leases/res-ai-workflow-and-routes` for that live run only.; RES-cloud-host-composition (append): Each module registers through its own module entry point and route fragment; the host composition only lists modules; route and binding conflicts are resolved by the integration owner at merge.
Unblocks: CLOUD.67, DEV.13, HAR.05

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Restart Workflow/Cloud during wait/model/tool, missed wake event, expired/stale proposal, cancel race, generation rotation, late evidence tests.
Completion evidence for the ledger: Approval-across-restart, cancellation and uncertain-effect results (PG-18, joint with HAR.04).
```

```text
Execute ArcForges delivery task HAR.03 — Generated streaming and durable output.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\harness.md (anchor task-har-03).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\AI (integration owner: AI integration owner, the holder of roles/integration-ai).
Claim and handoff record: claims/har-03 (python tools/delivery.py claim HAR.03 --worker <name>); task branch task/har-03 in AI; ledger record ledger/tasks/har-03.md.
Kind/size: service/L. Baseline: not-started.
Outcome: execution.readOutput/watchOutput, transient-turn admission/ack/purge and DO projections work per annex 10/model 05; Cloud histories commit canonically while local histories recover verified transient output without a Cloud Chat body; a stream projection never becomes message authority or determines Task state.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-52.03 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\52-cloud-harness.md, anchor rule-wp-52.03
- WP-52:sec-8-gate-item-9-every-surface-converge Sec.8 gate item 9: every surface converges to the same authoritative final answer/artifact with realtime disabled (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\52-cloud-harness.md, package-level obligation

Entry condition: adoption slice ADOPT.08.harness is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] CLOUD.11: actual owner identity/workspace primitive and current read ports
- [artifact] COM.16: actual durable Entitlement owner primitive
- [artifact] CLOUD.75: actual shared persisted realm/recovery authority
- [contract] CON.11: actual published public Execution/Events/history and private stream records
- [contract] CON.10: actual published Task/Chat/profile/tool/content records
Completion prerequisites (may start earlier; cannot complete before these are complete):
- [integration] AST.15: local history recovery of transient output on the client bridge
- [integration] CON.33: actual published output snapshot and final semantic hash producer
- [integration] HAR.00: the turn-loop skeleton producing output to stream
- [integration] AIR.05: the ContentOrigin marking at the provider generation boundary
- [integration] CLOUD.13: actual current native/browser session/device/installation owner integration
- [integration] CLOUD.21: real no-retry production D1/private object transport
- [integration] CLOUD.82: actual opaque same-issuer scoped owner contribution producer
- [integration] AIR.02: real provider usage and exactly-once customer settlement owner integration
- [integration] COM.07: real sole Kernel quota accounting and verified Resource effect integration
- [integration] CON.37: actual published closed read-only lost-admission receipt query and exact two-request intent helpers
- [integration] CLOUD.78: actual fixed transient content/receipt current/due and parent expiry compiler integration

Permitted write scope: AI:src/streams/RunStream.ts; AI:src/streams/** (actual generated RunStream projection, exact owner/attempt/offset/retention/private frames; preserve HAR00 Workflow ownership); AI:tests/run-stream*.test.ts and package.json (only actual owning stream component registration; no dependency or unavailable-provider acceptance waiver); AI:wrangler.json and src/index.ts (only actual owned RunStream DO export/binding and append-only migration at configured environments; preserve private deployment routes and existing loops); Cloud:src/ArcForges.Cloud.Modules.Task/Execution/** (real Task owner output/read/admission/terminal/ack/purge application and neutral injected storage/accounting ports; no foreign SQL); Cloud:src/ArcForges.Cloud.Modules.Chat/Execution/** (real Chat turn/run/output and shared transient body/receipt writer; no fabricated Task or normal history publication in local/temporary mode); Cloud:src/ArcForges.Cloud.Modules.Resource/ExecutionBodies/** (real current owner-authorized logical-body/ticket/decrypt/hash/range and transient object adapters); Cloud:src/ArcForges.Cloud.Modules.Abstractions/Execution/** (closed neutral generated owner/body/source/stream/prepared participant ports and immutable evidence; no caller authority Boolean or copied wire type); Cloud:src/ArcForges.Cloud.Modules.Task/TaskModule.cs, src/ArcForges.Cloud.Modules.Chat/ChatModule.cs and src/ArcForges.Cloud.Modules.Resource/ResourceModule.cs (only actual owned execution service/factory entrypoint registration); Cloud:src/ArcForges.Cloud.Storage.D1/Task/Execution/**, src/ArcForges.Cloud.Storage.D1/Chat/Execution/** and src/ArcForges.Cloud.Storage.D1/Resource/ExecutionBodies/** (actual owned row codecs/immutable generated plan adapters/module factories; preserve exclusive table ownership); Cloud:storage/plans/task/execution/**, storage/plans/chat/execution/** and storage/plans/resource/execution-bodies/** (only actual respective owner read/guard/effect plans for fixed execution variants); Cloud:storage/plans/families/execution-output/** and storage/plans/families/execution-transient/** (closed owner-ordered real terminal/ack/purge and native/browser admission compositions, no arbitrary optional/no-op owner role); Cloud:src/ArcForges.Cloud.Storage.D1/SharedFamilies/FamilyPlanVerifier.cs and src/ArcForges.Cloud.Storage.D1/FamilyBinding/ModuleFamilyPort.cs (only exact closed execution-output/execution-transient scoped families and immutable metadata/factory binding; preserve existing security/unknown-family refusals); Cloud:eng/verification/storage-plans.ts (only exact closed execution family/variant scope registration and actual generated output; no generic SQL/authorization grammar or legacy hash change); Cloud:src/ArcForges.Cloud.Storage.D1/Physical/manifest/chat.json and enums.json (only reviewed Chat-owned chat_transient_output_receipt mapping and exact body/receipt invariants; accepted other tables unchanged); Cloud:src/ArcForges.Cloud.Storage.D1/Migrations/pending/chat__transient-output-receipt.sql (additive exact actual Chat metadata and generated invariant triggers; integration owner allocates final number); Cloud:src/ArcForges.Cloud.Storage.D1/Physical/PhysicalSchema.g.cs and eng/migrations/lock.json (deterministic owned generation and assigned pending successor; preserve all accepted numbered bytes); Cloud:eng/verification/physical-schema.ts (only fixed Chat transient output receipt original/replacement profile and exact generated trigger inventory; no arbitrary SQL marker or shape waiver); Cloud:src/ArcForges.Cloud/Execution/** and src/ArcForges.Cloud/Resources/ExecutionBodies/** (actual existing generated RPC/stream services and signed logical object facade); Cloud:src/ArcForges.Cloud/Composition/ExecutionOutputModule.cs and HostModules.cs (only actual named module entrypoints, neutral port registration and owned ordering; no module-private cross-owner construction); Cloud:src/ArcForges.Cloud/Infrastructure/WorkerExecutionOutputClient.cs (closed existing signed private stream/R2/key/body bridge with real bounds/cancellation and no redirects/proxy); Cloud:worker/execution/** and worker/objects/execution-bodies/** (actual private transient state/key/R2 object and logical-body bridge; no public internal path, raw presign or independent business authority); Cloud:worker/index.ts, worker/router.ts and wrangler.json (only actual owned private handler/export/R2/DO binding/append-only migration/environment wiring; preserve prior migrations/routes/private settings); Cloud:tests/ArcForges.Cloud.Tests/Execution/**, tests/ArcForges.Cloud.Tests/Task/Execution/**, tests/ArcForges.Cloud.Tests/Chat/Execution/** and tests/ArcForges.Cloud.Tests/Resource/ExecutionBodies/** (actual generated/real SQLite/encrypted body/held cancellation/stream/owner/atomic receipt components); Cloud:tests/worker/execution-output*.test.ts, transient-body*.test.ts, execution-body-object*.test.ts and package.json (actual owning component hooks only, all old tests retained); Cloud:tests/worker/support/physical-rows.ts and tests/ArcForges.Cloud.Tests/Physical/PhysicalSchemaTests.cs (only legitimate own correlated receipt fixtures and actual accepted-manifest table count; unchanged constraints/search cap/unrelated fixtures); Cloud:tests/worker/d1-physical-schema.test.ts and execution-output-family*.test.ts (only actual fixed owner invariant and family/unknown/scope/SQL rollback vectors); Cloud:tests/worker/release-provenance.test.ts (only exact actually sealed owned Worker artifact SHA/byte successor literals; preserve all negative/legal/history checks); Cloud:src/ArcForges.Cloud/ArcForges.Cloud.csproj, src/ArcForges.Cloud.Modules.Abstractions/ArcForges.Cloud.Modules.Abstractions.csproj and exact Task/Chat/Resource csproj entries (only actual published mandatory generated Events/PublicApi/Validation/CloudInternal peers, existing neutral port/friend registration; no sibling module references); Cloud:Directory.Packages.props and actual owned affected packages.lock.json (only actual published CON33 and admitted mandatory peer closure required by real execution consumers; no guessed/unrelated upgrade); Cloud:tests/ArchitectureTests/EvaluatedRepositoryGate.cs, tests/ArchitectureTests/ContractConsumptionTests.cs and tests/ArchitectureTests/ExecutionOwnerArchitectureTests.cs (actual public/neutral API mappings and owner source confinement; no fake implementation assertion); Cloud:eng/provenance/files.json, eng/version-sources.json, eng/policy/dependency-policy.json and exact owned dependency-review successors; .dockerignore and owned release metadata (only real owned execution source/package/evaluated-input immutable successors, historical receipts preserved); Cloud:docs/execution-output.md (real APIs/storage/body/hash/permission/lifecycle/unknown/retention and separate acceptance limitations); Cloud:src/ArcForges.Cloud.Modules.Abstractions/Platform/ExecutionAdmissionReceiptPort.cs and src/ArcForges.Cloud.Storage.D1/Platform/ExecutionAdmission/** (narrow owner-resolved real platform command receipt read/co-commit adapter; no generic caller authority or foreign SQL); Cloud:src/ArcForges.Cloud.Storage.D1/Receipts/CommandReceipts.cs and storage/plans/platform/command-load.sql (only actual created/result/identity decoding and generated bounded admission result read, historical replay and refused/expired semantics unchanged); Cloud:storage/plans/families.json and src/ArcForges.Cloud.Storage.D1/SharedFamilies/FamilyDefinitions.cs, FamilyGuards.cs and FamilyPlanVerifier.cs (only finite actual execution family participants/typed profile metadata; no arbitrary owner/scope/grammar or old hash mutation); Cloud:tests/ArcForges.Cloud.Tests/Execution/AdmissionReceiptTests.cs and tests/worker/execution-admission-receipt.test.ts (actual current actor/original intent/scope/result/expiry/unknown and no-paid-dispatch reads); Cloud:src/ArcForges.Cloud.Storage.D1/Receipts/CommitTail.cs and storage/plans/platform/command-record-execution-admission-failure.sql (only bounded generated original admission record co-commit and the closed two-operation failure plan; existing generic receipt/replay/failure semantics unchanged); Cloud:src/ArcForges.Cloud.Storage.D1/Physical/manifest/platform.json and enums.json; src/ArcForges.Cloud.Storage.D1/Migrations/pending/platform__execution-admission-result.sql (only immutable command-FK admission result reference/tuple metadata and closed kind, original PK/ref insertion/update/delete profile; actual integration owner assigns number); Cloud:eng/verification/physical-schema.ts (only closed executionAdmissionResultOriginal sidecar table/key/shape profile and exact trigger inventory; no general immutable-row waiver); Cloud:storage/plans/platform/execution-admission/** and worker/objects/execution-admission/** (actual bounded private immutable original result object stage/verify/read and same-command-FK metadata plans; no whole result BLOB in D1 or original JSON cap raise); Cloud:tests/ArcForges.Cloud.Tests/Execution/AdmissionResultCapacityTests.cs and tests/worker/execution-admission-result.test.ts (actual permitted maximum original result, object tamper/missing/unknown stage, exact small-reference D1 request, FK/order/replace/rollback/expiry and old-tail preservation)
Shared resources (follow the owner protocol): RES-ai-workflow-and-routes (append): The Workflow entry is owned by the turn-loop task; other Harness tasks add steps through their own modules; the route-pin table changes only with a policy snapshot. Any task that runs against the AI deployment environment holds the lease `leases/res-ai-workflow-and-routes` for that live run only.; RES-cloud-d1-migrations (append): One global D1 migration sequence: each module task authors migrations under its module prefix; the integration owner assigns the global sequence number at merge, regenerates the plan manifest and rejects edits to merged migrations; the migrator applies in sequence with receipts.; RES-cloud-host-composition (append): Each module registers through its own module entry point and route fragment; the host composition only lists modules; route and binding conflicts are resolved by the integration owner at merge.; RES-shared-transaction-families (append): Adding a participant to a shared atomic family is a design change through the Architecture Owner; module tasks implement only their declared participation.; RES-cloud-policy-inputs (append): Append only task-owned source/test bindings and immutable successor receipts. Rebase before integration; regenerate actual input hashes and plan manifests; chain from the receipt active on main; preserve all prior versions and records. This protocol admits no unreviewed coordinate, permission or runtime behavior changes.
Unblocks: AND.24, AST.19, CLOUD.67, HAR.05, WEB.27

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Scope/permission, wrong/stale target, loss/retry, expiry and applicable native UI cases; cross-replica read, miss-is-not-eviction, takeover, realtime-disabled equivalence, buffer-lifecycle tests; the same four model-05 context vectors and HC-09/no-debit assertions as HAR.01 (shared testing-requirement text in the WP).
Completion evidence for the ledger: Cross-replica read, miss-is-not-eviction, takeover, realtime-disabled equivalence and buffer-lifecycle results.
Notes: 

docs/decisions/assistant-output-snapshots-and-semantic-profiles-2026-10-07.md: consume actual CON33 snapshot/configuration pin/shared semantic-v1 profiles. Generation/shape/helper publication does not itself implement real output storage, logical-body authorization/decryption, tokenizer materialization, execution or current permissions. Preserve original producer starts and acceptance; no success stub/private DTO or heuristic model budget.

2026-10-07 real execution output producer repair (docs/decisions/execution-output-and-logical-body-producer-2026-10-07.md). Sole source coordinator w-codex-20261006-runtime. Actual Task/Chat owner state, Chat-owned shared transient receipt/content metadata, Resource logical decoded-body facade and AI private disposable stream are concrete production implementations. Progressive core starts actual owner/generated/Entitlement/current realm primitives; original HAR00/AIR05 and AST15/full provider/accounting/permission integrations remain complete gates. Same guarded owner/verified object/provider/usage/settlement terminal batch, C7 sole quota writer, no new Cloud history for local/temporary or phantom Task. Exact raw logical protobuf hash/length/descriptor versus CON33 final semantic hash and ciphertext are distinct. Current origin/session/installation and owner revision remain actual permission. True ack/purge/key loss/expiry and 256KiB snapshot/envelope/1MiB logical body are mandatory. Owned ordinary correlated fixture/count/sealed artifact maintenance is actual-prefix bound, never a production constraint or test waiver. Full model/tokenizer/framing producer remains independently required; no estimates, interface success or hidden provider template admission.

CON37 receipt encodedBody carries only the actual generated GetAdmissionReceiptValue under the closed Platform-resolved execution-admission-receipt resource kind, <=1MiB logical and <=256KiB inline envelope; no MessageDraft type substitution or new generic result cap. Original generic command fingerprints/replay remain unchanged.

2026-10-07 factual terminal state/no-answer clarification (docs/decisions/execution-terminal-state-and-no-answer-registry-2026-10-07.md). ExecutionOutput.state is exact genuine Task/Chat owner state, not receipt/body/stream availability. Only execution.no_answer.completed/failed/canceled with the declared factual state and immutable owner/progress/output optional-lineage proof enters metadata-only terminal sealing; generic generated strings establish no registration. Original tags/schema/command frames/migrations, scopes, starts/outcomes and full acceptance remain unchanged.
```

```text
Execute ArcForges delivery task HAR.04 — Provider failure and effect-certainty classification.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\harness.md (anchor task-har-04).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/har-04 (python tools/delivery.py claim HAR.04 --worker <name>); task branch task/har-04 in Cloud; ledger record ledger/tasks/har-04.md.
Kind/size: service/M. Baseline: not-started.
Outcome: Failure classification keys on whether dispatch occurred, never on whether bytes returned; the unknown path releases customer holds at the reconciliation deadline while retaining supplier liability; no failure path silently resolves unknown to didNotHappen, and no dispatched request is retried automatically.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-52.04 (full): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\52-cloud-harness.md, anchor rule-wp-52.04

Entry condition: adoption slice ADOPT.07.harness is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] HAR.00: dispatch-intent records to classify
- [contract] AIR.06: the worked AI-provider uncertain-outcome/deadline-release pattern
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: Cloud:src/Cloud/ArcForges.Cloud.Modules.Task/EffectCertainty/**
Shared resources (follow the owner protocol): RES-ai-workflow-and-routes (append): The Workflow entry is owned by the turn-loop task; other Harness tasks add steps through their own modules; the route-pin table changes only with a policy snapshot. Any task that runs against the AI deployment environment holds the lease `leases/res-ai-workflow-and-routes` for that live run only.; RES-cloud-host-composition (append): Each module registers through its own module entry point and route fragment; the host composition only lists modules; route and binding conflicts are resolved by the integration owner at merge.; RES-cloud-policy-inputs (append): Append only task-owned source/test bindings and immutable successor receipts. Rebase before integration; regenerate actual input hashes and plan manifests; chain from the receipt active on main; preserve all prior versions and records. This protocol admits no unreviewed coordinate, permission or runtime behavior changes.
Unblocks: HAR.05, HAR.06, OPS.03

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Timeout-before-first-token asserting unknown-not-retry; lost response reconciled against the provider's own record; platform-caused retry charged once and fully visible in supplier cost; deadline-expiry releasing customer hold while retaining supplier liability.
Completion evidence for the ledger: Effect-certainty classification and deadline-release results (PG-18, joint with HAR.02).
```

```text
Execute ArcForges delivery task HAR.05 — Own-application execution proof and fixture turn-endpoint removal.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\harness.md (anchor task-har-05).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\AI (integration owner: AI integration owner, the holder of roles/integration-ai).
Claim and handoff record: claims/har-05 (python tools/delivery.py claim HAR.05 --worker <name>); task branch task/har-05 in AI; ledger record ledger/tasks/har-05.md.
Kind/size: integration/XL. Baseline: not-started.
Outcome: Two end-to-end oracles pass: the ArcScope embedded assistant processes its own selected session range or annotation plus local/cloud history, and Android/Web explicitly target an authorized ArcScope installation for an approved ArcScope command -- covering typed transcript/compaction, promotion/export, binary streams and offline recovery. The WP-17.01 fixture turn endpoint is structurally proven absent from the codebase.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-52.05 (all work except the parts mapped to AST.19, DEV.13): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\52-cloud-harness.md, anchor rule-wp-52.05
- WP-52.90 (structural assertion that the WP-17.01 fixture turn endpoint no longer exists (Sec.8 gate item 10)): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\52-cloud-harness.md, anchor rule-wp-52.90

Entry condition: adoption slice ADOPT.08.harness is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] HAR.00: the complete real turn loop
- [artifact] HAR.01: real context assembly/compaction
- [artifact] HAR.02: real approval/crash recovery
- [artifact] HAR.03: real streaming/durable output
- [artifact] HAR.04: real effect-certainty classification
- [artifact] AST.11: the real device-side tool executor and desktop surfaces in an actual AOT release binary
- [artifact] DEV.08: the real one-application bridge
- [artifact] AST.19: consumer switched from the fixture turn endpoint to the real Harness
- [artifact] DEV.13: consumer switched from the fixture turn endpoint to the real Harness
- [artifact] AND.24: consumer switched from the fixture turn endpoint to the real Harness
- [artifact] WEB.27: consumer switched from the fixture turn endpoint to the real Harness
- [artifact] AIR.00: real Workers AI provider adapters
- [artifact] SCOPE.20: the real ArcScope capability surface the approved ArcScope command invokes
- [artifact] APP.03: ArcScope composed as a clean Native AOT package consumer
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: AI:src/workflows/RunWorkflow.ts; AI:tests/Cloud.Tests.Integration/OwnApp/**
Shared resources (follow the owner protocol): RES-ai-workflow-and-routes (append): The Workflow entry is owned by the turn-loop task; other Harness tasks add steps through their own modules; the route-pin table changes only with a policy snapshot. Any task that runs against the AI deployment environment holds the lease `leases/res-ai-workflow-and-routes` for that live run only.
Unblocks: HAR.90

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Protected-context overflow, stale summary/branch, large transient object, forged tool history, interrupted output/final hash, lost ack, app restart, revoke/epoch change, refused cross-product target -- real device/AOT binary tests run locally/affected-scope per P2-017 (no desktop GUI or device CI), not as a hosted CI job.
Completion evidence for the ledger: Full same-application workflow with every failure variant; structural absence of the WP-17.01 fixture turn endpoint.
Notes: This is the task that performs implementation-sequence.md Sec.3.1's 'Fixture turn endpoint... No WP-52 substep or gate names an extension/MCP-sourced tool call as oracle evidence anywhere in the WP text; both named oracles are native ArcScope commands.
```

```text
Execute ArcForges delivery task HAR.06 — Durable Cloud automation, scheduling and automation-fixture removal.

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\harness.md (anchor task-har-06).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\Cloud (integration owner: Cloud integration owner, the holder of roles/integration-cloud).
Claim and handoff record: claims/har-06 (python tools/delivery.py claim HAR.06 --worker <name>); task branch task/har-06 in Cloud; ledger record ledger/tasks/har-06.md.
Kind/size: service/L. Baseline: not-started.
Outcome: Automation definition/version, trigger schedule/event cursor, occurrence dedup and grant/budget snapshot live in C# Task-owned tables; bounded leased jobs dispatch the same RunWorkflow identity through the existing outbox; disabled/revoked automation stops future occurrences; the labelled WP-17 automation fixture is removed.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-52.06 (automation definition/version, trigger schedule/event cursor, occurrence dedup, grant/budget snapshot, bounded leased dispatch through the existing outbox, disable/revoke control, and removal of the labelled WP-17 automation fixture): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\52-cloud-harness.md, anchor rule-wp-52.06

Entry condition: adoption slice ADOPT.07.harness is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] HAR.00: the RunWorkflow identity automation dispatches into
- [artifact] HAR.04: effect-certainty classification for occurrence dispatch
- [artifact] COM.05: service/grant expiry and budget snapshot ports
Completion prerequisites (may start earlier; cannot complete before these are complete):
- [integration] AST.20: desktop assistant switched to the real automation scheduler
- [integration] AND.24: Android companion switched to real automation occurrences

Permitted write scope: Cloud:src/Cloud/ArcForges.Cloud.Modules.Task/Automation/**
Shared resources (follow the owner protocol): RES-ai-workflow-and-routes (append): The Workflow entry is owned by the turn-loop task; other Harness tasks add steps through their own modules; the route-pin table changes only with a policy snapshot. Any task that runs against the AI deployment environment holds the lease `leases/res-ai-workflow-and-routes` for that live run only.; RES-cloud-host-composition (append): Each module registers through its own module entry point and route fragment; the host composition only lists modules; route and binding conflicts are resolved by the integration owner at merge.; RES-cloud-policy-inputs (append): Append only task-owned source/test bindings and immutable successor receipts. Rebase before integration; regenerate actual input hashes and plan manifests; chain from the receipt active on main; preserve all prior versions and records. This protocol admits no unreviewed coordinate, permission or runtime behavior changes.
Permitted substitutes (never real integration evidence): SUB-automation-fixture: client rendering of schedule/timezone/target/budget and action availability, offline-draft handling only Real producer ['HAR.06']; removed by HAR.06
Unblocks: AST.20, HAR.90

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Duplicate schedule/event, catch-up/coalescing, service/grant expiry, disable-during-wait tests; actual CF occurrence/usage with one linked Task at the credentialed gate.
Completion evidence for the ledger: Real automation scheduling, missed-run policy, occurrence deduplication, cancellation and fixture-removal results (core mechanics).
```

```text
Execute ArcForges delivery task HAR.90 — Verify owned artifact and real integration (Harness).

Task record: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\lanes\harness.md (anchor task-har-90).
Delivery rules: C:\MyFile\Projects\ArcForges-Design\docs\planning\delivery\README.md; execution: C:\MyFile\Projects\Plan\arcforges-implementation.md.
Owning repository: C:\MyFile\Projects\ArcForges\AI (integration owner: AI integration owner, the holder of roles/integration-ai).
Claim and handoff record: claims/har-90 (python tools/delivery.py claim HAR.90 --worker <name>); task branch task/har-90 in AI; ledger record ledger/tasks/har-90.md.
Kind/size: service/M. Baseline: not-started.
Outcome: The specified Worker/Workflow/DO roles are implemented and verified together; context, model/tool loop, approval, retries, cancel, streams and schedule execution run against real C# transactions/ports and selected Workers AI; the named WP-17 fixtures are confirmed removed; this package owns the first complete AI same-application workflow.

Obligations (authoritative definitions; satisfy exactly these parts and their tests/gates):
- WP-52.90 (remaining aggregation/receipt beyond HAR.05's structural assertion): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\52-cloud-harness.md, anchor rule-wp-52.90
- WP-52:p2-010-required-behavior-and-closure-ord P2-010 required behavior and closure: ordinary persistent/temporary ChatTurn and AgentTask through the same RunWorkflow, pure-read vs promoted-effectful mode (package-level obligation contribution): C:\MyFile\Projects\ArcForges-Design\docs\planning\work-packages\52-cloud-harness.md, package-level obligation

Entry condition: adoption slice ADOPT.08.harness is complete in the Plan ledger (DLV-22).
Start prerequisites (before claiming, each contract/artifact/design prerequisite must be delivered or complete and each release prerequisite complete in the Plan ledger; DLV-24):
- [artifact] HAR.05: own-application execution proof
- [artifact] HAR.06: real automation evidence
Completion prerequisites (may start earlier; cannot complete before these are complete):
- none

Permitted write scope: AI:tests/Cloud.Tests.Integration/**
Unblocks: REL.06

Validation (P2-017; no macOS/hosted runtime, device, GUI, browser E2E, live-service, inference or installed-consumer CI): Real C#/CF/R2/device integration; duplicate/lost-ack/approval/restart/stream-tail/terminal-commit cases; usage and provenance. One loop, one canonical business outcome, no unexplained provider retry.
Completion evidence for the ledger: Owned artifact and real-integration receipt: source commit, producer version, candidate hashes, actual runtime/OS/device/provider, scenario, result, real-vs-fixture status.
Notes: Also carries the P2-010 package closure text (ordinary persistent/temporary ChatTurn and AgentTask through the same real RunWorkflow, pure-read vs promoted-effectful mode, transient source expiry/cleanup, platform-funded protected compaction).
```
